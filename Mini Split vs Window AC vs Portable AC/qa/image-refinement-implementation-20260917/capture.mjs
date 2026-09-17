import { spawn } from 'node:child_process';
import { writeFileSync, existsSync, readFileSync } from 'node:fs';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { dirname, join, normalize, extname } from 'node:path';
import http from 'node:http';
import zlib from 'node:zlib';

const here = dirname(fileURLToPath(import.meta.url));
const project = normalize(join(here, '..', '..'));
const outDir = here;

const CHROME_CANDIDATES = [
  'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
  'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
  'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe',
  'C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe'
];
const MIME = { '.html':'text/html; charset=utf-8', '.css':'text/css; charset=utf-8', '.js':'text/javascript; charset=utf-8', '.png':'image/png', '.jpg':'image/jpeg', '.webp':'image/webp', '.svg':'image/svg+xml', '.woff2':'font/woff2', '.json':'application/json' };

const results = { page: null, checks: [], failures: [], screenshots: [], consoleErrors: [], failedRequests: [] };
function record(name, pass, detail) { results.checks.push({ name, pass, detail }); if (!pass) { results.failures.push({ name, detail }); } }
function assertEq(name, actual, expected, extra) { const pass = JSON.stringify(actual) === JSON.stringify(expected); record(name, pass, { actual, expected, ...(extra || {}) }); return pass; }
function assertTrue(name, cond, detail) { record(name, !!cond, detail); return !!cond; }

const EXPECTED = [
  { id:'p01', title:'Vario', cap:'9,000 BTU', rows:[['Coverage','Up to 400 sq. ft.'],['Voltage','230V'],['Efficiency','20 SEER2']], price:'$729.96', variant:'50314477076768', img:'assets/products-cutout/p01.png', w:1793, h:1791 },
  { id:'p02', title:'Serena', cap:'12,000 BTU', rows:[['Coverage','Up to 550 sq. ft.'],['Voltage','115V'],['Efficiency','22 SEER2']], price:'$799.96', variant:'50334430429472', img:'assets/products-cutout/p02.png', w:1808, h:1728 },
  { id:'p03', title:'Serena', cap:'18,000 BTU', rows:[['Coverage','Up to 1,000 sq. ft.'],['Voltage','230V'],['Efficiency','22 SEER2']], price:'$1,049.96', variant:'50340329029920', img:'assets/products-cutout/p03.png', w:1808, h:1728 },
  { id:'p04', title:'Optima Pro', cap:'12,000 BTU', rows:[['Coverage','Up to 550 sq. ft.'],['Voltage','230V'],['Efficiency','25 SEER2']], price:'$1,249.96', variant:'50351018475808', img:'assets/products-cutout/p04.png', w:1758, h:1702 },
  { id:'p05', title:'Fenestra', cap:'5,000 BTU', rows:[['Coverage','Up to 150 sq. ft.'],['Features','Mechanical controls'],['Voltage','115V']], price:'$169.96', variant:'45528183570720', img:'assets/products-cutout/p05.png', w:1672, h:1295 },
  { id:'p06', title:'Fenestra', cap:'8,000 BTU', rows:[['Coverage','Up to 350 sq. ft.'],['Features','Remote / app control'],['Voltage','115V']], price:'$269.96', variant:'45528218075424', img:'assets/products-cutout/p06.png', w:1717, h:1356 },
  { id:'p07', title:'Miri', cap:'8,000 BTU', rows:[['Coverage','Up to 350 sq. ft.'],['Features','Inverter'],['Voltage','115V']], price:'$379.96', variant:'48298757751072', img:'assets/products-cutout/p07.png', w:1796, h:1283 },
  { id:'p08', title:'Fenestra', cap:'12,000 BTU', rows:[['Coverage','Up to 550 sq. ft.'],['Features','Remote / app control'],['Voltage','115V']], price:'$359.96', variant:'45528149885216', img:'assets/products-cutout/p08.png', w:1717, h:1356 },
  { id:'p09', title:'Smart Portable AC', cap:'8,000 BTU SACC', rows:[['ASHRAE','12,000 BTU'],['Coverage','Up to 350 sq. ft.'],['Features','Cool / Fan / Dry / Auto']], price:'$309.96', variant:'51348045758752', img:'assets/products-cutout/p09.png', w:1729, h:1684 },
  { id:'p10', title:'Smart Portable AC', cap:'10,000 BTU SACC', rows:[['ASHRAE','14,000 BTU'],['Coverage','Up to 450 sq. ft.'],['Features','Cool / Fan / Dry / Auto']], price:'$379.96', variant:'51348125090080', img:'assets/products-cutout/p10.png', w:1729, h:1684 },
  { id:'p11', title:'Sylro', cap:'12,000 BTU SACC', rows:[['ASHRAE','15,500 BTU'],['Coverage','Up to 550 sq. ft.'],['Features','Dual hose / inverter']], price:'$599.96', variant:'51603403145504', img:'assets/products-cutout/p11.png', w:1755, h:1686 }
];

function sleep(ms) { return new Promise((r) => setTimeout(r, ms)); }

function analyzePng(buf) {
  let pos = 8; let width = 0, height = 0, bitDepth = 8, colorType = 6, interlace = 0; const idat = [];
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
  const channels = colorType === 6 ? 4 : colorType === 2 ? 3 : colorType === 0 ? 1 : 4;
  const bpp = channels; const stride = width * bpp; const out = Buffer.alloc(height * stride);
  let rp = 0;
  for (let y = 0; y < height; y++) {
    const filter = raw[rp++]; const row = raw.subarray(rp, rp + stride); rp += stride;
    const prev = y > 0 ? out.subarray((y - 1) * stride, y * stride) : Buffer.alloc(stride);
    const dest = out.subarray(y * stride, (y + 1) * stride);
    for (let x = 0; x < stride; x++) {
      const a = x >= bpp ? dest[x - bpp] : 0; const b = prev[x]; const c = x >= bpp ? prev[x - bpp] : 0; let v = row[x];
      if (filter === 1) { v = (v + a) & 0xff; }
      else if (filter === 2) { v = (v + b) & 0xff; }
      else if (filter === 3) { v = (v + ((a + b) >> 1)) & 0xff; }
      else if (filter === 4) { const p = a + b - c; const pa = Math.abs(p - a), pb = Math.abs(p - b), pc = Math.abs(p - c); const pr = pa <= pb && pa <= pc ? a : (pb <= pc ? b : c); v = (v + pr) & 0xff; }
      dest[x] = v;
    }
  }
  const step = Math.max(1, Math.floor(Math.min(width, height) / 220));
  const counts = new Map(); let total = 0, diff = 0; const c0 = [out[0], out[1], out[2]];
  for (let y = 0; y < height; y += step) {
    for (let x = 0; x < width; x += step) {
      const i = y * stride + x * bpp; const r = out[i], g = out[i + 1], b = out[i + 2];
      const key = ((r >> 4) << 8) | ((g >> 4) << 4) | (b >> 4); counts.set(key, (counts.get(key) || 0) + 1); total++;
      if (Math.abs(r - c0[0]) + Math.abs(g - c0[1]) + Math.abs(b - c0[2]) > 36) { diff++; }
    }
  }
  return { width, height, distinct: counts.size, nonUniform: total ? diff / total : 0 };
}

function parseRgb(s) {
  const m = s.match(/rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)/);
  if (!m) { return [0, 0, 0, 1]; }
  return [Number(m[1]), Number(m[2]), Number(m[3]), m[4] === undefined ? 1 : Number(m[4])];
}
function luminance([r, g, b]) {
  const f = (v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
  return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b);
}
function contrast(a, b) { const la = luminance(a), lb = luminance(b); const hi = Math.max(la, lb), lo = Math.min(la, lb); return (hi + 0.05) / (lo + 0.05); }

async function main() {
  let chrome = null, server = null;
  try {
    let delayHeroMs = 0;
    server = http.createServer((req, res) => {
      let rel = decodeURIComponent(req.url.split('?')[0]);
      if (rel === '/' || rel === '') { rel = '/mini-split-vs-window-ac-vs-portable-ac.html'; }
      const file = normalize(join(project, rel));
      const send = () => {
        if (!file.startsWith(project) || !existsSync(file)) { res.writeHead(404); res.end('nf'); return; }
        try { res.writeHead(200, { 'Content-Type': MIME[extname(file).toLowerCase()] || 'application/octet-stream', 'Cache-Control': 'no-store' }); res.end(readFileSync(file)); }
        catch { res.writeHead(500); res.end('e'); }
      };
      if (delayHeroMs && /hero-mobile\.png$/.test(rel)) { setTimeout(send, delayHeroMs); return; }
      send();
    });
    server.delayHeroMs = (v) => { delayHeroMs = v; };
    await new Promise((r) => server.listen(0, '127.0.0.1', r));
    const port = server.address().port;
    const base = `http://127.0.0.1:${port}`;
    const pageUrl = `${base}/mini-split-vs-window-ac-vs-portable-ac.html`;
    results.page = pageUrl;

    const bin = CHROME_CANDIDATES.find((c) => existsSync(c));
    if (!bin) { throw new Error('No Chrome/Edge binary'); }
    const profile = join(process.env.TEMP || '.', 'opencode', 'qa-imgref-' + Date.now());
    chrome = spawn(bin, ['--headless=new','--disable-gpu','--no-first-run','--no-default-browser-check','--hide-scrollbars','--force-device-scale-factor=1','--disable-extensions','--disable-background-networking','--disable-renderer-backgrounding','--disable-backgrounding-occluded-windows','--remote-allow-origins=*','--remote-debugging-port=0',`--user-data-dir=${profile}`,'about:blank'], { stdio: 'ignore' });

    const watchdog = setTimeout(() => {
      results.failures.push({ name: 'watchdog', detail: 'exceeded 420s' });
      try { writeFileSync(join(outDir, 'qa-results.json'), JSON.stringify(results, null, 2)); } catch {}
      try { spawn('taskkill', ['/PID', String(chrome.pid), '/F', '/T'], { stdio: 'ignore' }); } catch {}
      process.exit(1);
    }, 600000);
    watchdog.unref();

    const portFile = join(profile, 'DevToolsActivePort');
    let devPort = 0;
    for (let i = 0; i < 90 && !devPort; i++) { await sleep(300); if (existsSync(portFile)) { devPort = parseInt(readFileSync(portFile, 'utf8').split('\n')[0], 10); } }
    if (!devPort) { throw new Error('devtools port'); }
    const list = await new Promise((resolve, reject) => { http.get(`http://127.0.0.1:${devPort}/json/list`, (r) => { let d = ''; r.on('data', (c) => (d += c)); r.on('end', () => resolve(JSON.parse(d))); }).on('error', reject); });
    const target = list.find((t) => t.type === 'page');
    const ws = new WebSocket(target.webSocketDebuggerUrl);
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

    await send('Page.enable'); await send('Runtime.enable'); await send('Log.enable'); await send('Network.enable'); await send('DOM.enable'); await send('CSS.enable');
    await send('Page.addScriptToEvaluateOnNewDocument', { source: 'window.dataLayer = window.dataLayer || [];' });
    on('Runtime.exceptionThrown', (p) => results.consoleErrors.push('exception: ' + (p.exceptionDetails?.exception?.description || p.exceptionDetails?.text)));
    on('Log.entryAdded', (p) => { if (p.entry.level === 'error') { results.consoleErrors.push('log: ' + p.entry.text); } });
    on('Network.loadingFailed', (p) => { if (!p.canceled) { results.failedRequests.push(p.errorText); } });
    on('Network.responseReceived', (p) => { const s = p.response?.status || 0; if (s >= 400) { results.failedRequests.push(s + ' ' + p.response.url); } });

    async function evaluate(expression) { const r = await send('Runtime.evaluate', { expression, returnByValue: true, awaitPromise: true }); if (r.exceptionDetails) { throw new Error('eval: ' + JSON.stringify(r.exceptionDetails).slice(0, 300)); } return r.result.value; }
    async function setViewport(width, height) { await send('Emulation.setDeviceMetricsOverride', { width, height, deviceScaleFactor: 1, mobile: false }); }
    async function goto(url) {
      console.error('[qa] goto ' + url.slice(-42));
      await send('Page.navigate', { url: 'about:blank' }); await once('Page.loadEventFired').catch(() => {}); await sleep(80);
      const loaded = once('Page.loadEventFired').catch(() => {});
      await send('Page.navigate', { url }); await loaded;
      await send('Page.bringToFront').catch(() => {});
      await sleep(200);
      await evaluate('document.fonts && document.fonts.ready ? document.fonts.ready.then(()=>true) : true');
    }
    async function primeImages() {
      const h = await evaluate('document.documentElement.scrollHeight');
      for (let y = 0; y <= h; y += 600) { await evaluate('window.scrollTo(0,' + y + ')'); await sleep(35); }
      await evaluate('window.scrollTo(0,' + h + ')'); await sleep(220);
      await evaluate('window.scrollTo(0,0)');
      await evaluate("Promise.all(Array.from(document.images).filter(i => i.complete && i.naturalWidth > 0).map(i => (i.decode ? i.decode().catch(()=>{}) : Promise.resolve()))).then(()=>true)");
      await send('Page.bringToFront').catch(() => {});
      await sleep(150);
    }
    async function captureClip(name, clip) { const r = await send('Page.captureScreenshot', { format: 'png', fromSurface: true, clip: { ...clip, scale: 1 } }); writeFileSync(join(outDir, name), Buffer.from(r.data, 'base64')); results.screenshots.push(name); return Buffer.from(r.data, 'base64'); }
    async function screenshot(name) { await primeImages(); const r = await send('Page.captureScreenshot', { format: 'png', captureBeyondViewport: true, fromSurface: true }); writeFileSync(join(outDir, name), Buffer.from(r.data, 'base64')); results.screenshots.push(name); }
    async function keyEvent(k, code, vk) { await send('Input.dispatchKeyEvent', { type: 'keyDown', key: k, code, windowsVirtualKeyCode: vk, nativeVirtualKeyCode: vk }); await send('Input.dispatchKeyEvent', { type: 'keyUp', key: k, code, windowsVirtualKeyCode: vk, nativeVirtualKeyCode: vk }); await sleep(140); }
    async function forcePseudo(selector, pseudo) {
      const doc = await send('DOM.getDocument', { depth: -1 });
      const node = await send('DOM.querySelector', { nodeId: doc.root.nodeId, selector });
      if (!node || !node.nodeId) { return false; }
      await send('CSS.forcePseudoState', { nodeId: node.nodeId, forcedPseudoClasses: pseudo });
      return true;
    }
    async function clearPseudo(selector) { await forcePseudo(selector, []); }

    // ================= A. typography: all H2 =================
    for (const w of [1440, 1280, 1024, 768, 430, 390, 360, 1920]) {
      await setViewport(w, 900);
      await goto(pageUrl);
      const h2 = await evaluate(`(() => ({
        list: Array.from(document.querySelectorAll('h2')).map((h) => { const c = getComputedStyle(h); return { t: h.textContent.trim().slice(0, 24), family: c.fontFamily, size: c.fontSize, weight: c.fontWeight, lh: c.lineHeight, color: c.color }; }),
        fontsLoaded: document.fonts.check('500 32px "Della AC Spectral"')
      }))()`);
      const ok = h2.list.length === 6 && h2.list.every((x) => x.size === '32px' && x.weight === '500' && Math.abs(parseFloat(x.lh) - 36.8) <= 0.6 && /Della AC Spectral/.test(x.family) && x.color === 'rgb(14, 25, 83)');
      assertTrue(`h2-style-${w}`, ok, { h2: h2.list });
      assertTrue(`h2-font-loaded-${w}`, h2.fontsLoaded === true, h2);
      if (w === 1440) { await screenshot('desktop-1440-mini-split.png'); }
      if (w === 1920) { await screenshot('desktop-1920-full.png'); }
      if (w === 768) { await screenshot('tablet-768-full.png'); }
      if (w === 360) { await screenshot('mobile-360-full.png'); }
    }

    // ================= B. images: 14 cutout refs + dims + mapping =================
    await setViewport(1440, 900);
    await goto(pageUrl);
    const imgRefs = await evaluate(`Array.from(document.images).map((i) => ({ src: i.getAttribute('src'), w: i.getAttribute('width'), h: i.getAttribute('height') }))`);
    const cutouts = imgRefs.filter((i) => /products-cutout/.test(i.src || ''));
    assertEq('cutout-image-count', cutouts.length, 14);
    assertEq('old-jpg-refs', imgRefs.filter((i) => /assets\/products\/p\d+\.jpg/.test(i.src || '')).length, 0);
    const dimsOk = cutouts.every((i) => Number(i.w) > 800 && Number(i.h) > 800 && i.w !== '2000');
    assertTrue('cutout-dimensions', dimsOk, cutouts);
    const cmpImgs = await evaluate(`Array.from(document.querySelectorAll('#comparison .cmp-col__media img')).map((i) => i.getAttribute('src'))`);
    assertEq('compare-images', cmpImgs, ['assets/products-cutout/p01.png', 'assets/products-cutout/p07.png', 'assets/products-cutout/p11.png']);
    const cards = await evaluate(`Array.from(document.querySelectorAll('.product-card')).map((c) => ({
      title: c.querySelector('.product-title').textContent.trim(),
      cap: c.querySelector('.product-capacity') ? c.querySelector('.product-capacity').textContent.trim() : '',
      rows: Array.from(c.querySelectorAll('.product-meta > div')).map((d) => [d.querySelector('dt').textContent.trim(), d.querySelector('dd').textContent.trim()]),
      price: c.querySelector('.product-price').textContent.trim(),
      href: c.querySelector('.product-link').getAttribute('href'),
      img: c.querySelector('.product-image').getAttribute('src'),
      iw: Number(c.querySelector('.product-image').getAttribute('width')),
      ih: Number(c.querySelector('.product-image').getAttribute('height')),
      hasFullName: !!c.querySelector('.product-full-name')
    }))`);
    assertEq('card-count', cards.length, 11);
    const mism = [];
    EXPECTED.forEach((e, i) => { const g = cards[i]; if (!g || g.title !== e.title || g.cap !== e.cap || JSON.stringify(g.rows) !== JSON.stringify(e.rows) || g.price !== e.price || !g.href.includes('variant=' + e.variant) || g.img !== e.img || g.iw !== e.w || g.ih !== e.h || !g.hasFullName) { mism.push({ i, e, g }); } });
    assertTrue('card-data-and-image-mapping', mism.length === 0, { mism });
    assertEq('composite-identity-unique', new Set(cards.map((c) => c.title + '|' + c.cap + '|' + (c.href.match(/variant=(\d+)/) || [])[1])).size, 11);

    // ================= C. compare media size + actual painted product =================
    await setViewport(1440, 900);
    await goto(pageUrl);
    await primeImages();
    const cmpHeights = await evaluate(`(() => ({
      media: Array.from(document.querySelectorAll('#comparison .cmp-col__media')).map((m) => Math.round(m.getBoundingClientRect().height)),
      imgs: Array.from(document.querySelectorAll('#comparison .cmp-col__media img')).map((i) => ({ w: Math.round(i.getBoundingClientRect().width), h: Math.round(i.getBoundingClientRect().height), complete: i.complete, nat: i.naturalWidth }))
    }))()`);
    assertTrue('compare-media-height-1440', cmpHeights.media.every((h) => Math.abs(h - 280) <= 1), cmpHeights);
    assertTrue('compare-images-enlarged', cmpHeights.imgs.every((i) => i.h >= 180 && i.complete && i.nat > 0), cmpHeights.imgs);
    const mediaRect = await evaluate(`(() => { const r = document.querySelector('#comparison .cmp-col__media').getBoundingClientRect(); return { x: Math.round(r.left), y: Math.round(r.top), width: Math.round(r.width), height: Math.round(r.height) }; })()`);
    await evaluate('window.scrollTo(0,0)'); await sleep(120);
    const cmpPng = await captureClip('compare-media-painted-1440.png', mediaRect);
    const cmpStat = analyzePng(cmpPng);
    assertTrue('compare-media-painted-pixels', cmpStat.nonUniform > 0.03 && cmpStat.distinct > 6 && !cmpStat.unsupported, cmpStat);

    for (const [w, expectH] of [[1024, 235], [768, 235], [430, 220], [390, 220], [360, 220]]) {
      await setViewport(w, 900);
      await goto(pageUrl);
      const hh = await evaluate(`Math.round(document.querySelector('#comparison .cmp-col__media').getBoundingClientRect().height)`);
      assertTrue(`compare-media-height-${w}`, Math.abs(hh - expectH) <= 1, { hh, expectH });
    }

    // ================= D. evidence spacing + vertical centering =================
    async function evidenceGeom() {
      return await evaluate(`(() => {
        const h2 = document.querySelector('#evidence .section-title').getBoundingClientRect();
        const grid = document.querySelector('.evidence-grid').getBoundingClientRect();
        const img = document.querySelector('.evidence-media').getBoundingClientRect();
        const list = document.querySelector('.ev-list').getBoundingClientRect();
        return { h2Gap: Math.round(grid.top - h2.bottom), imgCenter: img.top + img.height / 2, listCenter: list.top + list.height / 2, imgH: Math.round(img.height), listH: Math.round(list.height) };
      })()`);
    }
    for (const w of [1440, 1280, 768, 390]) {
      await setViewport(w, 1000);
      await goto(pageUrl);
      const g = await evidenceGeom();
      if (w > 1100) {
        assertTrue(`evidence-h2-gap-${w}`, Math.abs(g.h2Gap - 32) <= 1, g);
        assertTrue(`evidence-centered-${w}`, Math.abs(g.imgCenter - g.listCenter) <= 2, g);
      } else {
        assertTrue(`evidence-h2-gap-${w}`, Math.abs(g.h2Gap - 24) <= 1, g);
      }
    }
    await setViewport(1440, 1000);
    await goto(pageUrl);
    await screenshot('evidence-closed-1440.png');
    await evaluate(`Array.from(document.querySelectorAll('.ev-item')).forEach((d) => { if (!d.open) { d.querySelector('summary').click(); } })`);
    await sleep(600);
    const gOpen = await evidenceGeom();
    assertTrue('evidence-centered-expanded-1440', Math.abs(gOpen.imgCenter - gOpen.listCenter) <= 2, gOpen);
    assertTrue('evidence-expanded-natural', gOpen.listH > 300, gOpen);
    await screenshot('evidence-expanded-1440.png');

    // ================= E. details counts / closed =================
    await goto(pageUrl);
    const details = await evaluate(`(() => ({ total: document.querySelectorAll('details').length, open: document.querySelectorAll('details[open]').length, faq: document.querySelectorAll('.faq-item').length, ev: document.querySelectorAll('.ev-item').length, identity: document.querySelectorAll('.product-identity').length, faqQ: Array.from(document.querySelectorAll('.faq-item summary')).map((s) => s.textContent.trim()) }))()`);
    assertEq('details-total', details.total, 19);
    assertEq('details-open-initial', details.open, 0);
    assertEq('faq-count', details.faq, 4);
    assertEq('evidence-count', details.ev, 4);
    assertEq('identity-count', details.identity, 11);
    assertEq('faq-questions', details.faqQ, ['Which options can work in a rental?', "What if a window AC doesn't fit my window?", 'Can one unit cool two rooms with the doors closed?', 'Can a mini split handle my winter heating?']);

    // ================= F. business data / removed nodes / container =================
    const struct = await evaluate(`(() => { const q = (s) => document.querySelectorAll(s).length; return {
      fitcheck: q('.fitcheck'), coverage: q('.coverage-note'), multiroom: q('.panel__secondary'), intro: q('.section__intro'),
      evLabel: q('.evidence__label'), heroCats: q('.hero__cats'), oldTable: q('table.cmp'), oldNote: q('.cmp__note'), caption: q('.evidence-media figcaption'),
      cols: q('#comparison .cmp-col'), rowsPer: Array.from(document.querySelectorAll('#comparison .cmp-col')).map((c) => c.querySelectorAll('.cmp-row').length)
    }; })()`);
    assertEq('removed-nodes', { fitcheck: struct.fitcheck, coverage: struct.coverage, multiroom: struct.multiroom, intro: struct.intro, evLabel: struct.evLabel, heroCats: struct.heroCats, oldTable: struct.oldTable, oldNote: struct.oldNote, caption: struct.caption }, { fitcheck:0, coverage:0, multiroom:0, intro:0, evLabel:0, heroCats:0, oldTable:0, oldNote:0, caption:0 });
    assertEq('comparison-cols', struct.cols, 3);
    assertEq('comparison-rows', struct.rowsPer, [2, 2, 2]);

    // ================= G. strip rail boundaries + contrast =================
    for (const w of [360, 390, 430]) {
      await setViewport(w, 844);
      await goto(pageUrl);
      const st = await evaluate(`(() => {
        const strip = document.getElementById('cmp-strip');
        const first = strip.querySelector('.cmp-col');
        const wrap = document.querySelector('.cmp-nav');
        const pad = parseFloat(getComputedStyle(document.getElementById('della-ac-compare')).getPropertyValue('--pad-x'));
        return { scrollLeft: strip.scrollLeft, firstLeft: Math.round(first.getBoundingClientRect().left), pad: pad, hidden: wrap.hidden, prev: document.querySelector('[data-cmp-prev]').disabled, next: document.querySelector('[data-cmp-next]').disabled, snap: getComputedStyle(strip).scrollSnapType, scrollPad: getComputedStyle(strip).scrollPaddingInlineStart };
      })()`);
      assertTrue(`rail-start-${w}`, st.hidden === false && st.scrollLeft <= 1 && Math.abs(st.firstLeft - st.pad) <= 1 && st.prev === true && st.next === false, st);
      await evaluate(`document.querySelector('[data-cmp-next]').click()`); await sleep(650);
      const mid = await evaluate(`(() => ({ left: Math.round(document.getElementById('cmp-strip').scrollLeft), prev: document.querySelector('[data-cmp-prev]').disabled }))()`);
      assertTrue(`rail-mid-${w}`, mid.left > 40 && mid.prev === false, mid);
      await evaluate(`(() => { const s = document.getElementById('cmp-strip'); s.scrollLeft = s.scrollWidth; s.dispatchEvent(new Event('scroll')); })()`); await sleep(400);
      const end = await evaluate(`(() => { const s=document.getElementById('cmp-strip'); return { left: Math.round(s.scrollLeft), max: Math.round(s.scrollWidth - s.clientWidth), next: document.querySelector('[data-cmp-next]').disabled }; })()`);
      assertTrue(`rail-end-${w}`, end.next === true && end.left >= end.max - 2, end);
      await evaluate(`document.querySelector('[data-cmp-prev]').click()`); await sleep(700);
      await evaluate(`(() => { const s = document.getElementById('cmp-strip'); s.scrollTo({ left: 0, behavior: 'auto' }); })()`); await sleep(300);
      const back = await evaluate(`(() => { const s=document.getElementById('cmp-strip'); return { left: s.scrollLeft, prev: document.querySelector('[data-cmp-prev]').disabled }; })()`);
      assertTrue(`rail-back-${w}`, back.left <= 1 && back.prev === true, back);
    }

    // contrast of small text states (measure rendered elements in real states)
    await setViewport(1280, 900);
    await goto(pageUrl);
    // make every relevant element rendered: window panel visible, identity + answers open
    await evaluate(`document.getElementById('tab-window-ac').click()`);
    await evaluate(`document.querySelectorAll('.product-identity').forEach((d) => { if (!d.open) { d.querySelector('summary').click(); } })`);
    await evaluate(`document.querySelectorAll('.faq-item').forEach((d) => { if (!d.open) { d.querySelector('summary').click(); } })`);
    await evaluate(`document.querySelectorAll('.ev-item').forEach((d) => { if (!d.open) { d.querySelector('summary').click(); } })`);
    await sleep(400);
    async function colorOf(sel) { return await evaluate(`(() => { const el = document.querySelector(${JSON.stringify(sel)}); if (!el) return null; const cs = getComputedStyle(el); let bgEl = el, bg = 'rgba(0, 0, 0, 0)'; while (bgEl) { const b = getComputedStyle(bgEl).backgroundColor; if (b && b !== 'rgba(0, 0, 0, 0)' && b !== 'transparent') { bg = b; break; } bgEl = bgEl.parentElement; } return { fg: cs.color, bg: bg, rendered: el.getBoundingClientRect().width > 0 }; })()`); }
    const contrastTargets = [
      { name: 'faq-open', sel: '.faq-item summary', force: [] },
      { name: 'ev-open', sel: '.ev-item summary', force: [] },
      { name: 'identity-hover', sel: '#window-ac-products .product-identity summary', force: ['#window-ac-products .product-identity summary'] },
      { name: 'fitlink-hover', sel: '#window-ac-products .product-fit-link', force: ['#window-ac-products .product-fit-link'] },
      { name: 'answer-link-hover', sel: '.faq-answer a', force: ['.faq-answer a'] },
      { name: 'default-collection-link', sel: '#window-ac-products .collection-link', force: [] }
    ];
    for (const t of contrastTargets) {
      for (const f of t.force) { await forcePseudo(f, ['hover']); }
      await sleep(120);
      const c = await colorOf(t.sel);
      assertTrue(`contrast-${t.name}-exists`, !!c && c.rendered, c);
      if (c) {
        const ratio = contrast(parseRgb(c.fg), parseRgb(c.bg));
        assertTrue(`contrast-${t.name}`, ratio >= 4.5, { fg: c.fg, bg: c.bg, ratio: Math.round(ratio * 100) / 100 });
      }
      for (const f of t.force) { await clearPseudo(f); }
    }

    // ================= H. Hero actually painted (pixels) =================
    await setViewport(1440, 900);
    await goto(pageUrl);
    await primeImages();
    const heroInfo = await evaluate(`(() => { const i = document.querySelector('.hero-media img'); const r = i.getBoundingClientRect(); return { src: i.currentSrc.split('/').pop(), complete: i.complete, nat: i.naturalWidth, rect: { x: Math.round(r.left), y: Math.round(r.top), width: Math.round(r.width), height: Math.round(r.height) } }; })()`);
    assertTrue('hero-image-loaded', heroInfo.complete && heroInfo.nat > 0 && /hero-desktop\.png$/.test(heroInfo.src), heroInfo);
    const heroPng = await captureClip('hero-painted-1440.png', { x: 0, y: 0, width: 1440, height: Math.min(514, heroInfo.rect.height) });
    const heroPx = analyzePng(heroPng);
    assertTrue('hero-painted-pixels', heroPx.nonUniform > 0.15 && heroPx.distinct > 20 && !heroPx.unsupported, heroPx);

    // ================= I. R3 delayed mobile hero =================
    await send('Network.setCacheDisabled', { cacheDisabled: true });
    server.delayHeroMs(2600);
    await setViewport(390, 844);
    await send('Page.navigate', { url: 'about:blank' }); await once('Page.loadEventFired').catch(() => {}); await sleep(80);
    const domReady = once('Page.domContentEventFired', 20000).catch(() => {});
    await send('Page.navigate', { url: pageUrl }); await domReady;
    await sleep(120);
    const before = await evaluate(`(() => { const img = document.querySelector('.hero-media img'); const h = document.querySelector('.hero-media').getBoundingClientRect(); const c = document.getElementById('comparison').getBoundingClientRect(); return { complete: img.complete, heroH: Math.round(h.height), cmpTop: Math.round(c.top + window.scrollY) }; })()`);
    for (let i = 0; i < 80; i++) { await sleep(150); const d = await evaluate(`document.querySelector('.hero-media img').complete && document.querySelector('.hero-media img').naturalWidth > 0`); if (d) { break; } }
    await sleep(150);
    const after = await evaluate(`(() => { const h = document.querySelector('.hero-media').getBoundingClientRect(); const c = document.getElementById('comparison').getBoundingClientRect(); return { heroH: Math.round(h.height), cmpTop: Math.round(c.top + window.scrollY) }; })()`);
    assertTrue('r3-reserved-before-load', before.complete === false, before);
    assertTrue('r3-hero-height-stable', Math.abs(before.heroH - after.heroH) <= 1, { before, after });
    assertTrue('r3-comparison-not-pushed', Math.abs(before.cmpTop - after.cmpTop) <= 1, { before, after });
    server.delayHeroMs(0);
    await send('Network.setCacheDisabled', { cacheDisabled: false });

    // ================= J. tab / URL / history regression =================
    await setViewport(1280, 900);
    await goto(pageUrl);
    await evaluate('window.dataLayer = []');
    await evaluate(`document.querySelector('#comparison a[href="#window-ac-products"]').click()`); await sleep(400);
    const j1 = await evaluate(`({ hash: location.hash, tab: document.querySelector('.tab[aria-selected="true"]').textContent.trim() })`);
    assertEq('url-window-link', j1, { hash: '#window-ac-products', tab: 'Window AC' }, j1);
    await evaluate(`document.getElementById('tab-portable-ac').click()`); await sleep(200);
    const j2 = await evaluate(`({ hash: location.hash, tab: document.querySelector('.tab[aria-selected="true"]').textContent.trim() })`);
    assertEq('url-portable-tab', j2, { hash: '#portable-ac-products', tab: 'Portable AC' }, j2);
    { const l = once('Page.loadEventFired').catch(() => {}); await send('Page.reload'); await l; await sleep(300); }
    const j3 = await evaluate(`({ hash: location.hash, tab: document.querySelector('.tab[aria-selected="true"]').textContent.trim() })`);
    assertEq('url-reload-retains', j3, { hash: '#portable-ac-products', tab: 'Portable AC' }, j3);
    await evaluate('window.dataLayer = []');
    await evaluate('history.back()'); await sleep(500);
    const j4 = await evaluate(`({ hash: location.hash, tab: document.querySelector('.tab[aria-selected="true"]').textContent.trim(), dl: window.dataLayer.slice() })`);
    assertEq('history-back-tab', { hash: j4.hash, tab: j4.tab }, { hash: '#window-ac-products', tab: 'Window AC' }, j4);
    assertTrue('history-single-event', j4.dl.length === 1 && j4.dl[0].selection === 'history', j4.dl);
    await evaluate(`document.getElementById('tab-mini-split').click()`); await sleep(150);
    await evaluate('window.scrollTo(0,0)'); await sleep(100);
    const scrollAfter = await evaluate('Math.round(window.scrollY)');
    assertEq('tab-click-no-scroll', scrollAfter, 0, { scrollAfter });

    // ================= K. no-JS regression =================
    await send('Emulation.setScriptExecutionDisabled', { value: true });
    await setViewport(1280, 900);
    await goto(pageUrl);
    const nojs = await evaluate(`(() => ({ tabsVisible: getComputedStyle(document.querySelector('.tabs')).display !== 'none', panels: Array.from(document.querySelectorAll('.panel')).map((p) => p.hidden), cards: document.querySelectorAll('.product-card').length, purchase: document.querySelectorAll('.product-link').length, collections: document.querySelectorAll('.collection-link').length, overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth + 1 }))()`);
    assertTrue('nojs-tabs-hidden', nojs.tabsVisible === false, nojs);
    assertEq('nojs-panels', nojs.panels, [false, false, false]);
    assertEq('nojs-cards', nojs.cards, 11);
    assertEq('nojs-purchase', nojs.purchase, 11);
    assertEq('nojs-collections', nojs.collections, 3);
    assertTrue('nojs-no-overflow', !nojs.overflow, nojs);
    await screenshot('nojs-1280-full.png');
    await send('Emulation.setScriptExecutionDisabled', { value: false });

    // ================= L. layout: overflow, container, portable =================
    for (const w of [1920, 1440, 1280, 1024, 768, 430, 390, 360]) {
      await setViewport(w, 900);
      await goto(pageUrl);
      const m = await evaluate(`(() => { const de = document.documentElement; const c = document.querySelector('.della-ac-compare .container'); const cs = getComputedStyle(c); return { overflow: de.scrollWidth > de.clientWidth + 1, bodyOverflow: document.body.scrollWidth > de.clientWidth + 1, maxWidth: cs.maxWidth, padL: cs.paddingLeft, contentW: Math.round(c.clientWidth - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight)) }; })()`);
      assertTrue(`overflow-${w}`, !m.overflow && !m.bodyOverflow, m);
      assertEq(`container-max-${w}`, m.maxWidth, '1360px');
      if (w === 1440) { assertTrue('container-1440-content-1312', Math.abs(m.contentW - 1312) <= 1, m); }
      if (w === 430) { assertEq('container-430-pad', m.padL, '16px'); }
    }
    for (const w of [1920, 1440, 1280]) {
      await setViewport(w, 1000);
      await goto(pageUrl);
      await evaluate(`document.getElementById('tab-portable-ac').click()`); await sleep(150);
      const p = await evaluate(`(() => { const g = document.querySelector('#portable-ac-products .product-grid'); const t = getComputedStyle(g).gridTemplateColumns.trim().split(/\\s+/).filter(Boolean); const ws = Array.from(document.querySelectorAll('#portable-ac-products .product-card')).map((c) => Math.round(c.getBoundingClientRect().width)); return { tracks: t.length, widths: ws }; })()`);
      assertEq(`portable-tracks-${w}`, p.tracks, 3, p);
      assertTrue(`portable-equal-${w}`, Math.max(...p.widths) - Math.min(...p.widths) <= 1, p.widths);
    }

    // ================= M. reduced motion + file:// =================
    await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'reduce' }] });
    await setViewport(390, 844);
    await goto(pageUrl);
    assertTrue('reduced-motion-no-overflow', !(await evaluate('document.documentElement.scrollWidth > document.documentElement.clientWidth + 1')));
    await send('Emulation.setEmulatedMedia', { features: [] });

    const fileUrl = pathToFileURL(join(project, 'mini-split-vs-window-ac-vs-portable-ac.html')).href;
    await setViewport(1280, 900);
    await goto(fileUrl);
    const fileCheck = await evaluate(`(() => ({ cards: document.querySelectorAll('.product-card').length, cutouts: document.querySelectorAll('img[src*="products-cutout"]').length, fonts: document.fonts.check('500 32px "Della AC Spectral"'), tab: document.querySelector('.tab[aria-selected="true"]').textContent.trim() }))()`);
    assertEq('file-cards', fileCheck.cards, 11);
    assertEq('file-cutouts', fileCheck.cutouts, 14);
    assertTrue('file-fonts', fileCheck.fonts, fileCheck);
    assertEq('file-default-tab', fileCheck.tab, 'Mini Split');

    // per-tab screenshots
    await setViewport(1440, 900);
    await goto(pageUrl);
    await evaluate(`document.getElementById('tab-window-ac').click()`); await screenshot('desktop-1440-window-ac.png');
    await evaluate(`document.getElementById('tab-portable-ac').click()`); await screenshot('desktop-1440-portable-ac.png');
    await setViewport(390, 844);
    await goto(pageUrl);
    await screenshot('mobile-390-mini-split.png');
    await evaluate(`document.getElementById('tab-window-ac').click()`); await screenshot('mobile-390-window-ac.png');
    await evaluate(`document.getElementById('tab-portable-ac').click()`); await screenshot('mobile-390-portable-ac.png');

    // final: images all resolve, no console errors
    await setViewport(1440, 900);
    await goto(pageUrl);
    await primeImages();
    const finalImgs = await evaluate(`(() => ({ failed: Array.from(document.images).filter((i) => i.complete && i.naturalWidth === 0).map((i) => i.getAttribute('src')), total: document.images.length }))()`);
    assertEq('no-failed-images', finalImgs.failed, [], finalImgs);
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
