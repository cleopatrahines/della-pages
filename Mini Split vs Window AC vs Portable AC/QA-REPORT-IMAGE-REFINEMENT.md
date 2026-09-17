# QA report — image, typography and evidence refinement (2026-09-17)

Build: `mini-split-vs-window-ac-vs-portable-ac.html` — 66,225 bytes, SHA256 `682BA16593B961A9E8AE243B016986F715C17B9AF03E18481DC8426C1E4CB89C`.
Round: transparent product images, comparison scale, unified H2, Evidence alignment, four-question FAQ, plus the carried-forward V6-1/V6-2/V6-3/V6-4 items.
Status: implemented and locally browser-tested; returned to Codex for review. Local review build only — not committed, pushed or published.

Earlier evidence preserved: `qa/` (first pass), `qa/codex-review-20260917/`, `qa/visual-refresh-20260917/`, and Codex's asset evidence `qa/image-refinement-20260917/` (untouched).

## 1. Changes this round

- Images: all 14 image positions (3 comparison + 11 cards) now use the transparent `assets/products-cutout/p01.png`–`p11.png` from `localImage`, with each file's intrinsic `width`/`height` from `products.json` (no 2000×2000 metadata). Original JPEGs kept under `assets/products/`; media stays on white with `contain`, no blend/filter/crop.
- Comparison media: 280px high above 1100px (image max-width 330px), 235px at 768–1100px, 220px at ≤767px; each image keeps its own aspect ratio.
- All H2 unified: `'Della AC Spectral', Georgia, serif`, 32px, weight 500, line-height 1.15, `#0E1953`, at every breakpoint. Removed the conflicting Services 36/31/29, generic-mobile 28 and closing 26 declarations.
- Evidence: H2-to-grid gap 32px desktop / 24px mobile; grid `align-items:center`; stacked gap 28px ≤1100px.
- FAQ: reduced to the four current questions; portable drainage moved into the Evidence "What needs to fit?" answer. 19 disclosures total, all closed initially.
- Owner-directed follow-up: removed the hero `Compare the options` button and its now-unused `.hero-copy .btn` rule. The hero keeps H1 + lead only, vertically centred; machines remain fully visible. The `#comparison` section id is kept and the nav code is unchanged.
- Owner-directed follow-up: added breathing space inside the product card purchase area — the price now has a 16px bottom margin (and 16px top padding) so it no longer sits flush against the `View Product` button. Applies to all three tabs.
- Owner-directed follow-up: at ≤600px the three product tabs stay on one row (equal-width `flex:1 1 0`, 14px, 8px gap, no wrap). Verified at 430/390/360: all three share one baseline, equal widths, total width under the tab bar, no page overflow.

## 2. How it was tested

Runner `qa/image-refinement-implementation-20260917/capture.mjs` — Node static server + Chrome 152.0.7977.77 headless-new over CDP (no npm dependency). Run: `node qa/image-refinement-implementation-20260917/capture.mjs`. The runner records every check and **exits non-zero if any assertion fails**. This run: **121 assertions, 121 passed, 0 failed**, 14 screenshots.

New verification techniques in this runner:

- A small in-runner PNG decoder (zlib inflate + scanline defilter) analyses `Page.captureScreenshot` clips to prove real pixels: `nonUniform` colour variation and distinct-colour count, so a painted scene is distinguished from a blank/plain rectangle.
- `CSS.forcePseudoState` measures real `:hover` states, and elements are opened/activated so `[open]` states are measured on rendered nodes.
- `Page.bringToFront` plus image `decode()` (bounded to completed images) before capture, addressing the earlier blank-desktop-screenshot concern.

## 3. Measured results

### Typography (all six H2, every tested width)
`checks h2-style-1440..360` — 6/6 H2 at each of 1440/1280/1024/768/430/390/360/1920 are `family "Della AC Spectral", Georgia, "Times New Roman", serif`, `32px`, `weight 500`, `line-height 36.8px`, `color rgb(14,25,83)`; `document.fonts.check('500 32px "Della AC Spectral"')` is true.

### Images and comparison scale
- `cutout-image-count` 14; `old-jpg-refs` 0; dimensions all >800 and not 2000.
- `card-data-and-image-mapping` 11/11 cards match `products.json` for series, capacity, three rows, price, `variant=` URL, image path and intrinsic size.
- Compare media heights: 280/280/280 at 1440; rendered image boxes 280×280 (p01), 330×236 (p07, capped at 330 width), 291×280 (p11) — equal media rows, each at its own ratio.
- 1024/768 → 235px; 430/390/360 → 220px.
- `compare-media-painted-pixels` (417×280 clip of column 1): `nonUniform 0.50`, `distinct 262` — the product is actually drawn, not a blank box.

### Evidence
- `evidence-h2-gap-1440` = 32px; `evidence-centered-1440` image centre 2580.43 vs list centre 2580.42 (Δ ≈ 0.01px).
- Expanded: `evidence-centered-expanded-1440` image centre 2832.29 vs list centre 2832.30, list height grew 251 → 945px with no fixed answer height.
- ≤1100px: gap 24px, stacked.

### FAQ / disclosures
`details-total` 19, `details-open-initial` 0, FAQ 4, Evidence 4, identity 11. FAQ questions exactly: rental / window AC doesn't fit / two rooms with doors closed / winter heating. Related single-zone-vs-multi-zone link kept in the two-rooms answer.

### V6-1 — comparison rail boundaries (fixed)
At 360/390/430: `rail-start` → `scrollLeft 0`, first card left = 16px = `--pad-x`, `scroll-padding-inline-start 16px`, previous disabled, next enabled; `rail-mid` → next scrolls and previous enables; `rail-end` → `scrollLeft == max` and next disabled; `rail-back` → returns to `scrollLeft 0` with previous disabled. No delay/one-shot flags; the fix is `scroll-padding-inline` matching the container padding plus honest first/last boundary logic.

### V6-2 — interactive small-text contrast (fixed)
All rules now use navy or `--blue-hover #466FCB`; brand blue remains for icons/borders/arrows. Measured: FAQ open 4.53:1 (on `#F8F9FB`), Evidence open 4.78:1, identity hover 4.78:1, "Check window fit" hover 4.78:1, FAQ answer link hover 4.53:1, default collection link 16.37:1. All ≥ 4.5:1.

### V6-3 — desktop Hero actually painted (fixed/verified)
`hero-painted-1440.png` (1440×514 clip): `distinct 862`, `nonUniform 0.80` — the scene is present in the rendered framebuffer, not just a sized element. This confirms the hero paint fix from the previous round and satisfies the "prove the picture, not the box" requirement. (Root cause last round was the `height:100%`+`aspect-ratio` collapse plus the picture background covering the copy; no CSS was rewritten blind.)

### Regression kept green
1360px container (1440 content 1312, padding 24; 430 padding 16); no page-level overflow at 1920/1440/1280/1024/768/430/390/360; Portable three equal tracks at 1920/1440/1280 (423/423/423); Tab/URL/history: Window link → URL+tab, Portable tab → URL+tab, reload retains Portable, Back restores Window with exactly one `selection:history` event, tab click does not scroll; no-JS hides tab controls and shows all 11 products with 11 purchase + 3 collection links and no overflow; reduced motion no overflow; `file://` opens with 11 cards, 14 cutouts and fonts loaded; 0 console errors, 0 failed requests, 0 failed images.

## 4. Data and assets

Commercial facts are unchanged this round. The 2026-09-17 live recheck stands (`qa/visual-refresh-20260917/live-verification-20260917.md`): 11/11 selected variants matched `products.json` (price/availability/SKU) and all destination links resolved 200; no new fetch was performed in this pass. Cutout files, hashes, crop bounds and alpha/RGB checks are Codex's asset evidence in `qa/image-refinement-20260917/cutout-report.json`; this report verifies the page implementation, not a new price check.

## 5. V6-4 — HANDOFF correction

The Shopify integration list previously said to remove the inline `.js` bootstrap. That was wrong and is corrected in `HANDOFF.md`: the `.js` initialisation must be kept or migrated into the theme bootstrap, because `:not(.js) .tabs`/`.cmp-nav` rely on it — deleting it would hide the tab and comparison controls.

## 6. Not verified / limitations

- Only installed Chrome 152 headless was used; no real devices, Safari or Firefox. Touch inertia/snap feel on hardware was not exercised (Chrome CSS viewport + DOM only).
- Pixel checks sample at a stride rather than every pixel and cover the hero, the first comparison column and the full-page captures; they are a paint-presence check, not a formal image diff.
- The cutout method is a conservative white-page removal; `PRODUCT-IMAGE-PROCESSING.md` notes residual enclosed coil areas and original contact shadows. Dark-background rendering is out of scope for this page.
- Shopify theme embedding, canonical and production analytics remain later integration work.

## 7. Files

- `mini-split-vs-window-ac-vs-portable-ac.html` (66,225 bytes; SHA256 `682BA165…`)
- `qa/image-refinement-implementation-20260917/`: `capture.mjs`, `qa-results.json`, 14 screenshots (1440 three tabs full page, 390 three tabs full page, 360/768/1920, Evidence closed/expanded, painted clips, no-JS)
- `QA-REPORT-IMAGE-REFINEMENT.md` (this file), updated `HANDOFF.md`
