import { spawn } from 'node:child_process';
import { writeFileSync, existsSync, readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join, normalize, extname } from 'node:path';
import http from 'node:http';
import zlib from 'node:zlib';

const here = dirname(fileURLToPath(import.meta.url));
const project = normalize(join(here, '..', '..'));
const outDir = here;

const CHROME = [
  'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
  'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
  'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe',
  'C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe'
].find((c) => existsSync(c));
const MIME = { '.html':'text/html; charset=utf-8', '.css':'text/css', '.js':'text/javascript', '.png':'image/png', '.jpg':'image/jpeg', '.svg':'image/svg+xml', '.woff2':'font/woff2', '.json':'application/json' };

const results = { checks: [], failures: [], screenshots: [], consoleErrors: [], failedRequests: [] };
function record(name, pass, detail) { results.checks.push({ name, pass, detail }); if (!pass) { results.failures.push({ name, detail }); } }
function assertTrue(name, cond, detail) { record(name, !!cond, detail); return !!cond; }
function assertEq(name, actual, expected, extra) { const pass = JSON.stringify(actual) === JSON.stringify(expected); record(name, pass, { actual, expected, ...(extra || {}) }); return pass; }
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

function analyzePng(buf) {
  let pos = 8, width = 0, height = 0, bitDepth = 8, colorType = 6, interlace = 0; const idat = [];
  while (pos + 8 <= buf.length) {
    const len = buf.readUInt32BE(pos); const type = buf.toString('ascii', pos + 4, pos + 8);
    const data = buf.subarray(pos + 8, pos + 8 + len);
    if (type === 'IHDR') { width = data.readUInt32BE(0); height = data.readUInt32BE(4); bitDepth = data[8]; colorType = data[9]; interlace = data[12]; }
    else if (type === 'IDAT') { idat.push(data); }
    else if (type === 'IEND') { break; }
    pos += 12 + len;
  }
  if (interlace !== 0 || bitDepth !== 8) { return { width, height, distinct: 0, nonUniform: 1, unsupported: true }; }
  const raw = zlib.inflateSync(Buffer.concat(idat));
  const ch = colorType === 6 ? 4 : colorType === 2 ? 3 : colorType === 0 ? 1 : 4;
  const stride = width * ch; const out = Buffer.alloc(height * stride); let rp = 0;
  for (let y = 0; y < height; y++) {
    const filter = raw[rp++]; const row = raw.subarray(rp, rp + stride); rp += stride;
    const prev = y > 0 ? out.subarray((y - 1) * stride, y * stride) : Buffer.alloc(stride);
    const dest = out.subarray(y * stride, (y + 1) * stride);
    for (let x = 0; x < stride; x++) {
      const a = x >= ch ? dest[x - ch] : 0, b = prev[x], c = x >= ch ? prev[x - ch] : 0; let v = row[x];
      if (filter === 1) { v = (v + a) & 0xff; } else if (filter === 2) { v = (v + b) & 0xff; }
      else if (filter === 3) { v = (v + ((a + b) >> 1)) & 0xff; }
      else if (filter === 4) { const p = a + b - c, pa = Math.abs(p - a), pb = Math.abs(p - b), pc = Math.abs(p - c); const pr = pa <= pb && pa <= pc ? a : (pb <= pc ? b : c); v = (v + pr) & 0xff; }
      dest[x] = v;
    }
  }
  const step = Math.max(1, Math.floor(Math.min(width, height) / 220));
  const counts = new Map(); let total = 0, diff = 0; const c0 = [out[0], out[1], out[2]];
  for (let y = 0; y < height; y += step) {
    for (let x = 0; x < width; x += step) {
      const i = y * stride + x * ch; const r = out[i], g = out[i + 1], b = out[i + 2];
      counts.set(((r >> 4) << 8) | ((g >> 4) << 4) | (b >> 4), 1); total++;
      if (Math.abs(r - c0[0]) + Math.abs(g - c0[1]) + Math.abs(b - c0[2]) > 36) { diff++; }
    }
  }
  return { width, height, distinct: counts.size, nonUniform: total ? diff / total : 0 };
}

async function main() {
  let chrome = null, server = null;
  try {
    server = http.createServer((req, res) => {
      let rel = decodeURIComponent(req.url.split('?')[0]);
      if (rel === '/' || rel === '') { rel = '/mini-split-vs-window-ac-vs-portable-ac.html'; }
      const file = normalize(join(project, rel));
      if (!file.startsWith(project) || !existsSync(file)) { res.writeHead(404); res.end('nf'); return; }
      res.writeHead(200, { 'Content-Type': MIME[extname(file).toLowerCase()] || 'application/octet-stream', 'Cache-Control': 'no-store' });
      res.end(readFileSync(file));
    });
    await new Promise((r) => server.listen(0, '127.0.0.1', r));
    const pageUrl = `http://127.0.0.1:${server.address().port}/mini-split-vs-window-ac-vs-portable-ac.html`;

    const profile = join(process.env.TEMP || '.', 'opencode', 'qa-copy-' + Date.now());
    chrome = spawn(CHROME, ['--headless=new','--disable-gpu','--no-first-run','--no-default-browser-check','--hide-scrollbars','--force-device-scale-factor=1','--disable-extensions','--disable-background-networking','--disable-renderer-backgrounding','--disable-backgrounding-occluded-windows','--remote-allow-origins=*','--remote-debugging-port=0',`--user-data-dir=${profile}`,'about:blank'], { stdio: 'ignore' });
    const watchdog = setTimeout(() => { results.failures.push({ name: 'watchdog', detail: 'timeout' }); try { writeFileSync(join(outDir, 'qa-results.json'), JSON.stringify(results, null, 2)); } catch {} try { spawn('taskkill', ['/PID', String(chrome.pid), '/F', '/T'], { stdio: 'ignore' }); } catch {} process.exit(1); }, 300000);
    watchdog.unref();

    const portFile = join(profile, 'DevToolsActivePort');
    let devPort = 0;
    for (let i = 0; i < 90 && !devPort; i++) { await sleep(300); if (existsSync(portFile)) { devPort = parseInt(readFileSync(portFile, 'utf8').split('\n')[0], 10); } }
    if (!devPort) { throw new Error('devtools port'); }
    const list = await new Promise((resolve, reject) => { http.get(`http://127.0.0.1:${devPort}/json/list`, (r) => { let d = ''; r.on('data', (c) => (d += c)); r.on('end', () => resolve(JSON.parse(d))); }).on('error', reject); });
    const ws = new WebSocket(list.find((t) => t.type === 'page').webSocketDebuggerUrl);
    await new Promise((resolve, reject) => { ws.addEventListener('open', resolve); ws.addEventListener('error', reject); });

    const pending = new Map(); const listeners = new Map(); let msgId = 0;
    ws.addEventListener('message', (ev) => {
      const msg = JSON.parse(ev.data);
      if (msg.id && pending.has(msg.id)) { const { resolve, reject, timer } = pending.get(msg.id); pending.delete(msg.id); clearTimeout(timer); if (msg.error) { reject(new Error(JSON.stringify(msg.error))); } else { resolve(msg.result); } }
      else if (msg.method) { (listeners.get(msg.method) || []).forEach((fn) => fn(msg.params)); }
    });
    function send(method, params = {}) { const id = ++msgId; return new Promise((resolve, reject) => { const timer = setTimeout(() => { pending.delete(id); reject(new Error('CDP timeout ' + method)); }, 30000); pending.set(id, { resolve, reject, timer }); ws.send(JSON.stringify({ id, method, params })); }); }
    function on(method, fn) { if (!listeners.has(method)) { listeners.set(method, []); } listeners.get(method).push(fn); }
    function once(method, ms = 20000) { return new Promise((resolve, reject) => { const t = setTimeout(() => reject(new Error('event ' + method)), ms); const fn = (p) => { clearTimeout(t); const a = listeners.get(method) || []; const i = a.indexOf(fn); if (i >= 0) { a.splice(i, 1); } resolve(p); }; on(method, fn); }); }

    await send('Page.enable'); await send('Runtime.enable'); await send('Log.enable'); await send('Network.enable');
    on('Runtime.exceptionThrown', (p) => results.consoleErrors.push('exception: ' + (p.exceptionDetails?.exception?.description || p.exceptionDetails?.text)));
    on('Log.entryAdded', (p) => { if (p.entry.level === 'error') { results.consoleErrors.push('log: ' + p.entry.text); } });
    on('Network.loadingFailed', (p) => { if (!p.canceled) { results.failedRequests.push(p.errorText); } });
    on('Network.responseReceived', (p) => { const s = p.response?.status || 0; if (s >= 400) { results.failedRequests.push(s + ' ' + p.response.url); } });

    async function evaluate(expression) { const r = await send('Runtime.evaluate', { expression, returnByValue: true, awaitPromise: true }); if (r.exceptionDetails) { throw new Error('eval: ' + JSON.stringify(r.exceptionDetails).slice(0, 300)); } return r.result.value; }
    const setViewport = (width, height) => send('Emulation.setDeviceMetricsOverride', { width, height, deviceScaleFactor: 1, mobile: false });
    async function goto(url) {
      await send('Page.navigate', { url: 'about:blank' }); await once('Page.loadEventFired').catch(() => {}); await sleep(80);
      const loaded = once('Page.loadEventFired').catch(() => {});
      await send('Page.navigate', { url }); await loaded;
      await send('Page.bringToFront').catch(() => {});
      await sleep(220);
      await evaluate('document.fonts && document.fonts.ready ? document.fonts.ready.then(()=>true) : true');
    }
    async function primeImages() {
      const h = await evaluate('document.documentElement.scrollHeight');
      for (let y = 0; y <= h; y += 600) { await evaluate('window.scrollTo(0,' + y + ')'); await sleep(30); }
      await evaluate('window.scrollTo(0,0)');
      await evaluate("Promise.all(Array.from(document.images).filter(i => i.complete && i.naturalWidth > 0).map(i => (i.decode ? i.decode().catch(()=>{}) : Promise.resolve()))).then(()=>true)");
      await evaluate('new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r))).then(()=>true)');
      await send('Page.bringToFront').catch(() => {});
      await sleep(150);
    }
    async function screenshot(name) { await primeImages(); const r = await send('Page.captureScreenshot', { format: 'png', captureBeyondViewport: true, fromSurface: true }); writeFileSync(join(outDir, name), Buffer.from(r.data, 'base64')); results.screenshots.push(name); }

    const changes = JSON.parse(readFileSync(join(project, 'copy-replacements-20260917.json'), 'utf8')).changes;

    // ---------- A. selector-based copy mapping in the live DOM ----------
    await setViewport(1440, 900);
    await goto(pageUrl);
    const dom = await evaluate(`(() => {
      const get = (sel) => { const el = document.querySelector(sel); return el ? el.textContent.replace(/\\s+/g, ' ').trim() : null; };
      const out = {};
      ${changes.map((c, i) => `out[${JSON.stringify(c.id)}] = get(${JSON.stringify(c.selector)});`).join('\n      ')}
      return out;
    })()`);
    let mapOk = true;
    for (const c of changes) {
      const got = dom[c.id];
      const norm = (s) => s.replace(/\s+/g, ' ').trim();
      const pass = got !== null && norm(got) === norm(c.new);
      if (!pass) { mapOk = false; record('copy-' + c.id, false, { selector: c.selector, got, expected: c.new }); }
      else { record('copy-' + c.id, true, { selector: c.selector }); }
    }
    assertTrue('copy-mapping-all-12', mapOk, { mapped: Object.keys(dom).length });

    // ---------- B. invariants / immutable fields ----------
    const inv = await evaluate(`(() => {
      const q = (s) => document.querySelectorAll(s).length;
      return {
        details: q('details'), open: q('details[open]'), faq: q('.faq-item'), ev: q('.ev-item'), cards: q('.product-card'), h2: q('h2'),
        energy: !!document.querySelector('.ev-item:nth-of-type(3) a[href*="energy.gov"]'),
        energyStar: !!document.querySelector('.ev-item:nth-of-type(3) a[href*="energystar.gov"]'),
        multiZone: !!document.querySelector('.faq-item:nth-of-type(3) a[href*="single-zone-vs-multi-zone"]'),
        prices: Array.from(document.querySelectorAll('.product-price')).map((p) => p.textContent.trim()),
        ctas: Array.from(document.querySelectorAll('.product-link')).map((a) => a.textContent.replace(/\\s+/g,' ').trim()),
        variantLinks: Array.from(document.querySelectorAll('.product-link')).filter((a) => /variant=\\d+/.test(a.getAttribute('href'))).length,
        tabOneRowCss: matchMedia('(max-width:600px)').matches
      };
    })()`);
    assertEq('inv-details', inv.details, 19);
    assertEq('inv-open', inv.open, 0);
    assertEq('inv-faq', inv.faq, 4);
    assertEq('inv-evidence', inv.ev, 4);
    assertEq('inv-cards', inv.cards, 11);
    assertEq('inv-h2', inv.h2, 6);
    assertTrue('inv-source-links', inv.energy && inv.energyStar, inv);
    assertTrue('inv-multizone-link', inv.multiZone, inv);
    assertEq('inv-prices', inv.prices, ['$729.96','$799.96','$1,049.96','$1,249.96','$169.96','$269.96','$379.96','$359.96','$309.96','$379.96','$599.96']);
    assertEq('inv-cta-11', inv.ctas.filter((t) => t.startsWith('View Product')).length, 11);
    assertEq('inv-variant-links', inv.variantLinks, 11);

    // ---------- C. Hero lead wrapping / not covered (1440, 390) ----------
    for (const w of [1440, 390]) {
      await setViewport(w, 900);
      await goto(pageUrl);
      await primeImages();
      const hero = await evaluate(`(() => {
        const lead = document.querySelector('.hero-lead');
        const copy = document.querySelector('.hero-copy');
        const img = document.querySelector('.hero-media img');
        const lr = lead.getBoundingClientRect(), cr = copy.getBoundingClientRect(), ir = img.getBoundingClientRect();
        const cx = Math.round(lr.left + lr.width / 2), cy = Math.round(lr.top + lr.height / 2);
        const top = document.elementFromPoint(cx, cy);
        const lh = parseFloat(getComputedStyle(lead).lineHeight);
        return { lines: Math.round(lr.height / lh), leadRight: Math.round(lr.right), copyRight: Math.round(cr.right), imgLeft: Math.round(ir.left), onTop: !!(top && lead.contains(top)), leadH: Math.round(lr.height), imgW: Math.round(ir.width), imgH: Math.round(ir.height) };
      })()`);
      assertTrue(`hero-lead-not-covered-${w}`, hero.onTop === true, hero);
      assertTrue(`hero-lead-within-copy-${w}`, hero.leadRight <= hero.copyRight + 1, hero);
      if (w === 1440) {
        assertTrue('hero-lead-wraps-1440', hero.lines >= 1 && hero.lines <= 3, hero);
        const heroImg = await evaluate(`(() => { const i = document.querySelector('.hero-media img'); return { complete: i.complete, nat: i.naturalWidth, src: i.currentSrc.split('/').pop() }; })()`);
        assertTrue('hero-image-loaded-1440', heroImg.complete && heroImg.nat > 0 && /hero-desktop\.png$/.test(heroImg.src), heroImg);
        const clip = await send('Page.captureScreenshot', { format: 'png', fromSurface: true, clip: { x: 0, y: 0, width: 1440, height: Math.min(514, hero.imgH), scale: 1 } });
        const clipBuf = Buffer.from(clip.data, 'base64');
        writeFileSync(join(outDir, 'copy-1440-hero-clip.png'), clipBuf); results.screenshots.push('copy-1440-hero-clip.png');
        const px = analyzePng(clipBuf);
        assertTrue('hero-scene-painted-1440', px.nonUniform > 0.15 && px.distinct > 20 && !px.unsupported, px);
        await screenshot('copy-1440-hero-full.png');
      } else { await screenshot('copy-390-hero-full.png'); }
    }

    // ---------- D. Evidence closed then expanded: no clipping, questions readable ----------
    await setViewport(1440, 1000);
    await goto(pageUrl);
    const closed = await evaluate(`(() => ({
      questions: Array.from(document.querySelectorAll('.ev-item > summary')).map((s) => s.textContent.trim()),
      open: document.querySelectorAll('.ev-item[open]').length,
      h2Gap: Math.round(document.querySelector('.evidence-grid').getBoundingClientRect().top - document.querySelector('#evidence .section-title').getBoundingClientRect().bottom)
    }))()`);
    assertEq('evidence-questions', closed.questions, ['What does installation involve?', 'What affects noise in the room?', 'How do BTU and efficiency ratings differ?', 'When is a mini split worth the installation cost?']);
    assertEq('evidence-closed', closed.open, 0);
    assertEq('evidence-h2-gap-1440', closed.h2Gap, 32);
    await screenshot('copy-1440-evidence-closed.png');
    await evaluate(`Array.from(document.querySelectorAll('.ev-item')).forEach((d) => { if (!d.open) { d.querySelector('summary').click(); } })`);
    await sleep(600);
    const expanded = await evaluate(`(() => {
      const items = Array.from(document.querySelectorAll('.ev-item'));
      const clipped = items.map((d) => { const p = d.querySelector('.ev-answer > p'); return { open: d.open, scrollH: p.scrollHeight, clientH: p.clientHeight }; }).filter((x) => x.scrollH > x.clientH + 1);
      const img = document.querySelector('.evidence-media').getBoundingClientRect();
      const list = document.querySelector('.ev-list').getBoundingClientRect();
      return { allOpen: items.every((d) => d.open), clipped, imgCenter: img.top + img.height / 2, listCenter: list.top + list.height / 2 };
    })()`);
    assertTrue('evidence-all-open', expanded.allOpen, expanded);
    assertEq('evidence-answers-not-clipped', expanded.clipped, [], expanded.clipped);
    assertTrue('evidence-centered-expanded-1440', Math.abs(expanded.imgCenter - expanded.listCenter) <= 2, expanded);
    await screenshot('copy-1440-evidence-expanded.png');

    // ---------- E. 360 narrow + tabs + comparison entry ----------
    await setViewport(360, 844);
    await goto(pageUrl);
    const narrow = await evaluate(`(() => ({
      overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth + 1,
      leadLines: Math.round(document.querySelector('.hero-lead').getBoundingClientRect().height / parseFloat(getComputedStyle(document.querySelector('.hero-lead')).lineHeight)),
      tabTops: Array.from(document.querySelectorAll('.tab')).map((t) => Math.round(t.getBoundingClientRect().top))
    }))()`);
    assertTrue('narrow-360-no-overflow', !narrow.overflow, narrow);
    assertTrue('narrow-360-lead-wraps', narrow.leadLines >= 1 && narrow.leadLines <= 3, narrow);
    assertEq('narrow-360-tabs-one-row', new Set(narrow.tabTops).size, 1);
    await screenshot('copy-360-full.png');

    await setViewport(1440, 900);
    await goto(pageUrl);
    await evaluate(`document.querySelector('#comparison a[href="#window-ac-products"]').click()`);
    await sleep(500);
    const entry = await evaluate(`({ tab: document.querySelector('.tab[aria-selected="true"]').textContent.trim(), hash: location.hash, hidden: document.getElementById('window-ac-products').hidden })`);
    assertEq('comparison-entry-activates', { tab: entry.tab, hash: entry.hash, hidden: entry.hidden }, { tab: 'Window AC', hash: '#window-ac-products', hidden: false }, entry);
    await evaluate(`document.getElementById('tab-portable-ac').click()`); await sleep(200);
    const tabSwitch = await evaluate(`({ tab: document.querySelector('.tab[aria-selected="true"]').textContent.trim(), hash: location.hash })`);
    assertEq('tab-switch-works', tabSwitch, { tab: 'Portable AC', hash: '#portable-ac-products' }, tabSwitch);
    await screenshot('copy-1440-full.png');

    assertEq('console-errors', results.consoleErrors, []);
    assertEq('failed-requests', results.failedRequests, []);

    ws.close();
  } catch (err) {
    results.failures.push({ name: 'harness-exception', detail: String(err && err.stack ? err.stack : err) });
    record('harness-exception', false, String(err));
  } finally {
    if (server) { try { server.close(); } catch {} }
    if (chrome && chrome.pid) { try { spawn('taskkill', ['/PID', String(chrome.pid), '/F', '/T'], { stdio: 'ignore' }); } catch {} }
  }
  results.summary = { checks: results.checks.length, passed: results.checks.filter((c) => c.pass).length, failed: results.failures.length, screenshots: results.screenshots.length };
  writeFileSync(join(outDir, 'qa-results.json'), JSON.stringify(results, null, 2));
  console.log(JSON.stringify({ summary: results.summary, failures: results.failures }, null, 2));
  if (results.failures.length > 0) { process.exitCode = 1; }
}

main();
