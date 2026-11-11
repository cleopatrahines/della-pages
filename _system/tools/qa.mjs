import { chromium } from 'playwright-core';
const [,, url, prefix] = process.argv;
const b = await chromium.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe' });
const errs = [];
for (const w of [1440, 390]) {
  const p = await b.newPage({ viewport: { width: w, height: 900 } });
  p.on('pageerror', e => errs.push(`${w}: ${e.message}`));
  p.on('console', m => { if (m.type() === 'error') errs.push(`${w} console: ${m.text()}`); });
  p.on('requestfailed', r => errs.push(`${w} failed: ${r.url().slice(0, 120)}`));
  await p.goto(url, { waitUntil: 'load' });
  const H = await p.evaluate(() => document.body.scrollHeight);
  for (let y = 0; y < H; y += 600) { await p.evaluate(y => scrollTo(0, y), y); await p.waitForTimeout(120); }
  await p.evaluate(() => scrollTo(0, 0)); await p.waitForTimeout(2600);
  await p.screenshot({ path: `${prefix}-${w}.png`, fullPage: true });
  const ov = await p.evaluate(() => document.documentElement.scrollWidth - innerWidth);
  if (ov > 0) errs.push(`${w}: horizontal overflow ${ov}px`);
  await p.close();
}
console.log(errs.length ? errs.join('\n') : 'no errors');
await b.close();
