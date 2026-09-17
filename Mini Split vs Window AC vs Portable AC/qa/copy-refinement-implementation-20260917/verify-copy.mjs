import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const here = dirname(fileURLToPath(import.meta.url));
const project = join(here, '..', '..');
const j = JSON.parse(readFileSync(join(project, 'copy-replacements-20260917.json'), 'utf8'));
const html = readFileSync(join(project, 'mini-split-vs-window-ac-vs-portable-ac.html'), 'utf8');

let ok = true;
for (const c of j.changes) {
  const oldPresent = html.includes(c.old);
  const newPresent = html.includes(c.new);
  if (oldPresent || !newPresent) { ok = false; }
  if (oldPresent || !newPresent) { console.log(`FAIL ${c.id}: oldPresent=${oldPresent} newPresent=${newPresent}`); }
  else { console.log(`ok   ${c.id}`); }
}
console.log('ALL 12 OK:', ok);
if (!ok) { process.exitCode = 1; }

const inv = {
  details: (html.match(/<details/g) || []).length,
  open: (html.match(/<details[^>]*\bopen\b/g) || []).length,
  faq: (html.match(/class="faq-item"/g) || []).length,
  ev: (html.match(/class="ev-item"/g) || []).length,
  cards: (html.match(/class="product-card"/g) || []).length,
  h2: (html.match(/<h2/g) || []).length,
  energyLink: html.includes('energy.gov/cmei/buildings/portable-air-conditioners'),
  energyStarLink: html.includes('energystar.gov/products/room_air_conditioners'),
  multiZoneLink: html.includes('pages/single-zone-vs-multi-zone'),
  tabOneRowCss: html.includes('.tab{flex:1 1 0;min-width:0;padding:0 8px;font-size:14px'),
  priceGapCss: html.includes('margin:auto var(--card-inset) 16px;padding-top:16px'),
  oldHeroLead: html.includes('everyday comfort'),
  faqQuestions: Array.from(html.matchAll(/class="faq-item">\s*<summary>([^<]+)<\/summary>/g)).map((m) => m[1])
};
console.log(JSON.stringify(inv, null, 1));
