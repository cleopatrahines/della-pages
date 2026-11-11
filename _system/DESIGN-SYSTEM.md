# DELLA topic landing pages — design system v4

Reference page: `Mini Split for Bedroom/mini-split-for-bedroom.html`. Open it next to this file; every other page must feel like it was made by the same hand.

## Why
Manager feedback: the old pages are not "大气" and don't match dellahome.com. History: v2 (warm cream/sand/navy) was liked; v3 (all-white, cool) was "too white". v4 = v2 look refined, with the feel of the two main references: https://dellahome.com/pages/coupon-code and https://dellahome.com/pages/black-friday-early-deals — cream page, sand bands, **navy image + panel blocks**, real lifestyle photos. Keep a topic-page character (sizing tiles, steps, proof bar) rather than copying the promo layout. No eyebrow labels. Text a size larger than v2 (body 17px, lead 18px, nothing under 12px).

Measured on dellahome.com: body **Inter Tight**, headings **Spectral** with negative tracking, cream `#FFFEFB`, sand `#F5F3ED`, sky `#D8F0F7`, navy `#0B133D` / `#0E1952`, **pill buttons**.

## Files
- `_system/della-landing-v2.css` — the only place shared CSS lives. Pages hold a synced copy between `/* === DELLA SYSTEM v2 START` … `END === */` (marker names stay "v2").
- `_system/della-landing-v2.js` — shared JS: reveal, sticky sub-nav with active pill, `.seg` tabs (`seg.dellaSet(key)`, `della:tab` event), phone swipe-rail dots, step accordion with image swap, mobile buy bar, live Shopify price/stock, `window.dellaTrack`, `window.dellaScrollTo`.
- `_system/modules.html` — ICONS sprite and TRUST block (synced verbatim), plus HERO / SUBNAV / STEP ACCORDION / FAQ / CTA / BUY BAR templates.
- `python _system/sync.py` — fills every page listed in it (`--check` reports stale pages).
- `_system/tools/gen_della.py` — image generation. `_system/tools/qa.mjs` — screenshots + error/overflow check at 1440 and 390.

## Page skeleton (in this order)
1. **Hero** (template). Keep the page's H1 text exactly. **No eyebrow and no buttons** — H1 + one sentence only. Desktop 16:9 photo with calm left side; phones get their own vertical photo above the copy.
2. **Proof bar** — 3 or 4 numbers already stated on the page or in its product data. Never invent a spec.
3. **Sub-nav** — 3–5 anchors + FAQ, "Shop now" button.
4. The page's own sections, **same order and same copy as before**, rebuilt with system components.
5. **TRUST** (synced module) — replaces any "Premium Della Services" section and its H2.
6. **FAQ** (template) — all existing Q&As verbatim, first one `open`, FAQPage JSON-LD kept.
7. **Final CTA** (template) — existing heading/copy/buttons, navy card with photo on the right (photo on top on phones); buttons `.btn-white` + `.btn-ghost-white`.
8. **Buy bar** (template) — phones only, short label + "from $X" taken from the page's products.

## Components (use these before writing page CSS)
| Need | Use |
|---|---|
| Spacing | Every section uses `--gap` (112 / 88 / 72px). Two plain cream sections in a row share one gap automatically; the final CTA has a smaller `--gap-end` below it. Do not set section padding in page CSS. |
| Section wrapper | `section.sec` on the cream page (+ `.bg-white` / `.bg-sand` / `.bg-sky` / `.bg-navy`) — never two sand bands in a row (TRUST is sand) |
| Section title | `header.sec-head` (`.h2` left, `.lead` right). **No eyebrow labels anywhere.** A heading under an H2 (e.g. "Shop … by Capacity") is an `h3.h3` inside `.sub-head` |
| Labels | Never put chips or badges on top of a photo where they can cover the unit; put them in the card body (`.tile-tags`). Big numbers on photos sit bottom-left only. |
| Scenario / room / path cards | `.tile-grid` (`style="--cols:2|3|4"`, add `.rail` to swipe on phones) + `.tile` (`.tile-media`, `.chip`, `.tile-body`); big number on photo = `.tile-media--shade` + `.tile-cap`; selected state `.is-selected` |
| Facts inside cards | `dl.kv` rows, `ul.ticks` checklist |
| Big statement | `.feature` (photo + navy panel with `.h2`, copy, `.feature-points`; `.feature--rev` puts the photo right) — one or two per page; numbers must already be on the page |
| Products | `.p-grid` + `.p-card` (template in `modules.html`): label line above the photo, white photo area, `h3.p-title` + `.p-cap` capacity, `dl.p-specs` rows (Coverage / Efficiency / Voltage…), `details.p-name` "Full model name" holding `.p-full`, price + stock, full-width button. Keep handles, links, prices, data-attributes. The section title above product cards is an `h2`. |
| Capacity / type switch | `.seg[role=tablist][data-tabs=x]` + `[data-tab]` buttons + `[data-panel]` panels inside `[data-tab-scope=x]` |
| Image + steps | `.split` + `figure.split-media.has-steps` (one img per step) + `ol.steps[data-media=figId]` accordion + `.paths` link cards. On phones the step image moves inside the open step |
| Comparison | `.cmp-wrap > table.cmp` |
| Callout | `.note` (sky) |

Site header: dellahome.com has a sticky header (68px phone / 84px desktop). The shared JS measures it into `--hdr`; the sticky sub-nav and anchor jumps sit below it, so never hard-code `top:0` for sticky elements. Headings use Spectral 500, as on dellahome.com.

Rules: pill buttons only; at most one navy primary button per card; links use `.link-arrow`; icons from the sprite only; headings left-aligned; `.reveal` on headers/cards. Clickable cards: whole card selects, buttons inside still work, no page jump. Page CSS goes after the system block, scoped by section class, and stays short. Check phones at 390px: no overflow, tap targets ≥ 44px, swipe rails show dots.

## Imagery
Modern light-luxury interiors, like https://www.homary.com/room-ideas and https://www.povison.com/ : greige/taupe limewash or plaster walls, panel moulding, dark walnut and fluted wood, travertine, cream boucle, velvet, layered neutral linen with one accent color (sage, rust, chocolate, ink blue), brushed brass, sculptural lamps, warm natural light. **No people, no hands, no pets** (the existing Bedroom CTA photo with a dog is the one approved exception). Avoid pale blond wood and plain white bedding in every shot. Clean and crisp, never hazy or yellow-cast. **Every image on a page is a different scene** (room, time of day, palette, angle, distance).
- The DELLA indoor unit must keep its real proportions (about 3:1 width to height, flat front, level) and be fully visible with wall space around it. Reject and regenerate any image where it is warped, cropped or covered.
- Indoor wall unit: reference `_refs/waiji.png` — `"kind": "indoor"` (default). Outdoor condenser: `_refs/aq.png` — `"kind": "outdoor"`. No unit: `"kind": "plain"`.
- Ceiling cassette / ducted: describe the unit carefully; use the page's existing product images as reference if needed.
- **4K WebP.** Hero and CTA 3840×2160 (left ~45% calm for text); phone hero 2160×3840; cards, steps and feature 3072×2048. The script also writes `<name>-1920.webp`; use it as `src` and list both in `srcset`. Make a 1080-wide copy for the phone hero.
- Jobs file example: `_system/tools/jobs-bedroom.json`. Images go in `<page folder>/assets/v5/`. About $0.15 per 4K image — tell the user the total.

## Don't
- Change H1, title, meta, canonical, URLs, product handles, prices, or tracking event names.
- Delete body copy or FAQ answers; rewrite target keywords.
- Add facts that aren't already on the page.
- Edit the synced blocks inside a page (edit `_system/` and run sync instead).
