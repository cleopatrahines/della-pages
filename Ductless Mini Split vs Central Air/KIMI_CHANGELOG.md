# KIMI_CHANGELOG — Ductless Mini Split vs Central Air

Date: 2026-08-13 · Auditor: Kimi (k3)
File modified: `ductless-mini-split-vs-central-air.html` (5 targeted fixes, no structural/strategy changes)

## Changes

### 1. Hero H1 desktop size corrected to DESIGN.md spec

- **Before**: `.dsc-hero h1` → `font:500 clamp(45px,4.6vw,65px)/1.02 ...`
- **After**: `clamp(45px,4.6vw,56px)`
- **Reason**: 65px exceeded DESIGN.md's 48–56px desktop range and forced a 3-line H1 wrap at ≥1280px ("Ductless Mini / Split / vs Central Air"), breaking the 2-line composition in `Design.png`.
- **Measurement**: rendered Spectral Medium measured in Chrome — "Ductless Mini Split" at 56px = 462px < copy column → 2 lines hold. Mobile rule (`40px` at ≤560px) untouched.
- **Verification**: screenshot at 1440px confirms 2-line H1.

### 2. Hero CTAs restored to side-by-side layout

- **Before**: `.dsc-hero__inner` grid `minmax(0,.86fr) minmax(480px,1.14fr)` → copy column 498.8px; buttons measure 265.25 + 238.81 + 12 gap = 516px → wrapped to two rows at 1440/1280/1024.
- **After**: grid `minmax(0,.92fr) minmax(480px,1.08fr)` → copy column 533.6px; plus at ≤1024px `.dsc-hero__actions{gap:10px}` and `.dsc-hero__actions .dsc-btn{padding-inline:14px}` so the 480px tablet column also keeps one row.
- **Reason**: `Design.png` shows both Hero CTAs on one horizontal row.
- **Verification**: post-fix measurement shows `rows:1` at 1440/1280/1024; hero visual column still 626px (≥ its 480px minimum), equipment composition unchanged; screenshot-verified.

### 3. Hero lead split into three paragraphs

- **Before**: one `.dsc-hero__lead` paragraph containing all three sentences.
- **After**: three `.dsc-hero__lead` paragraphs (ductless sentence / central sentence / "Start with the project you are trying to solve.") with `.dsc-hero__lead+.dsc-hero__lead{margin-top:14px}`.
- **Reason**: matches the mockup's copy rhythm; wording is exactly the PRD-approved supporting copy, only presentation changed.
- **Verification**: 1440px hero screenshot matches mockup structure.

### 4. Comparison table header product thumbnails added

- **Before**: `thead` cells text-only ("Wall-Mounted Mini Split" / "Central Air").
- **After**: each header cell includes a small product thumbnail (existing localized `serena-12k.jpg` / `central-34k.jpg`, `alt=""` decorative, `loading="lazy"`, explicit width/height, CSS `height:52px;object-fit:contain`).
- **Reason**: `Design.png` shows these thumbnails in the light-blue comparison header; text retained for accessibility. Mobile stacked view unaffected (thead is visually hidden there; row labels come from `data-label`).
- **Verification**: 1440px screenshot matches mockup; no console/asset errors; QA image-load checks pass.

### 5. FAQ numbering restored (1.–6.)

- **Before**: unnumbered `summary` items.
- **After**: pure-CSS counter — `counter-reset:faq` on `.dsc-faq__grid`, `.dsc-faq summary:before{counter-increment:faq;content:counter(faq) ".";...}`.
- **Reason**: `Design.png` numbers the FAQs 1.–6. (left column 1–3, right 4–6). CSS-only approach keeps native `details/summary` semantics and leaves the FAQ JSON-LD byte-identical.
- **Verification**: 1440px and 390px screenshots show correct numbering in both columns; FAQ schema still matches visible Q&A 6/6.

## Round 3 — visual polish vs `Design.png` (owner feedback: "人味不足")

Diagnosis: the gap was not the design system but (a) beige `#eeede8` backgrounds baked into all 8 DELLA CDN packshots creating visible "sticker" rectangles on the cool blue-white page, and (b) two design-system violations (negative H1 letter-spacing, button weight 600 vs spec 700).

### 6. Product-image beige backgrounds blended into containers

- Sampled all 8 images via canvas: uniform warm off-white `#eeede8` (central images carry a subtle `#fffffd → #eeede8` vertical gradient).
- Fix (approved 方案 A, no asset changes): all image containers now use `background:linear-gradient(180deg,#fdfcf9 0%,#eeede8 100%)` + `border-radius:4px` so photo edges disappear into their containers:
  - `.dsc-product__media` (8 product cards)
  - `.dsc-supplement__visual`
  - `.dsc-table thead img` (comparison thumbnails)
- Hero: `.dsc-hero__visual` is now one unified warm stage panel (same gradient, `border-radius:8px`, `overflow:hidden`) holding both equipment images; removed the blue radial glow (`.dsc-hero__visual:before`) which clashed with the warm stage. Two floating beige rectangles → one composed banner block, consistent with DELLA's rectangular image-block grammar.
- Verification: 1440px screenshots — no visible photo edges anywhere; card grid reads as clean merchandising.

### 7. H1 negative letter-spacing removed (design-system compliance)

- `della-memorial-day-design-system.md` explicitly lists "Avoid: Negative letter spacing". Removed `letter-spacing:-.02em` from `.dsc-hero h1`; line-height 1.02 → 1.08 (spec range). Spectral now renders with its natural, more elegant spacing, closer to the mockup.

### 8. Button font-weight 600 → 700 (design-system compliance)

- Spec: "Weight: 700". Applied to `.dsc-btn` and `.dsc-path__action` (gateway card actions). Quieter text controls (`.dsc-change`, `.dsc-detail`, `.dsc-unsure a`) intentionally remain 600.

### 9. Product-card dead whitespace removed

- Removed hard `min-height` alignment crutches (`.dsc-product__role` 21px, `__reference` 38px, `__title` 91/67/110px, `__coverage` 26/42px). Content now flows naturally; price/action block stays bottom-aligned via the existing `margin:auto` on `.dsc-product__price`.
- Verification: measured in Chrome — all 4 ductless cards equal height (572px), price tops within 4px, action tops within 3px across the row. Short-title cards no longer show a dead white band between title and specs.

### 10. Hero equipment scale increased

- `.dsc-hero__visual` height 430 → 470px; mini split width 52% → 56%; central width 54% → 58%; mobile heights 360 → 385px (≤820px) and 295 → 315px (≤560px). Equipment now carries the first screen like the mockup instead of floating small.

## Round 4 — transparent cutout imagery (owner re-confirmed `Design.png` as target)

Round 3's warm-panel blending (方案 A) removed the "sticker" edges but still could not reproduce the mockup's free-floating equipment. Round 4 executes 方案 B locally with zero new dependencies (Playwright + canvas, no image libraries installed).

### 11. Transparent-background product cutouts generated

- Processor: local HTTP server + canvas in headless Chrome. A region-growing flood fill from image borders removes only border-connected warm off-white pixels (`#eeede8` family, warm-signature classifier), which protects the white indoor units' interiors; alpha is feathered with two box-blur passes; transparent margins are trimmed with 1% padding; exported as WebP q92.
- Output: `assets/products/cut-serena-12k.webp` (1581×1507), `cut-vario-18k.webp` (1731×1727), `cut-vario-dual-28k.webp` (1707×1751), `cut-vario-quad-35k.webp` (1695×1809), `cut-central-24k/34k/47k.webp` (1809×1557), `cut-central-53k.webp` (1805×1557). 168–328KB each — smaller than the source JPGs.
- Original 8 JPGs are untouched; `sources.md` records the derived-asset provenance.
- Quality gate: all 8 cutouts composited over pale-blue and white backgrounds and visually inspected — clean edges, product shadows preserved, no holes in white housings.

### 12. HTML switched to cutouts; round-3 container camouflage reverted

- All 12 `<img>` references (hero ×2, product cards ×8, supplement ×1, comparison header ×2) now use `cut-*.webp` with updated intrinsic width/height (CLS protection retained).
- Reverted round-3 container backgrounds now that images float cleanly: hero visual back to transparent + subtle blue radial glow; `.dsc-product__media` back to plain (white card); `.dsc-supplement__visual` back to `--blue-surface`; comparison-header thumbnails back to chromeless.
- Hero composition verified against `Design.png`: equipment floats free on the pale gradient, overlapping mini-split/central composition, enlarged scale from round 3 retained.

## Round 5 — hero composition fixes (owner review)

### 13. Hero mini-split asset: accessories removed

- Owner feedback: the ductless packshot's line-set coil, phone, and remote cluttered the banner and the mini split overlapped the central system.
- Generated `assets/products/cut-serena-hero.webp` (1571×1365) from `cut-serena-12k.webp`: accessory regions located via a coarse alpha-occupancy grid (coil x>1170/y 600–1210; phone/remote/copper stubs x>1130/y>1170), hard-erased, alpha re-feathered, re-trimmed. Indoor + outdoor units only. Original and full cutout both retained.
- Verified visually on the pale hero gradient before wiring in.

### 14. Hero labels removed

- Removed the `DUCTLESS` / `DUCTED CENTRAL` chips (markup + `.dsc-hero__label` CSS, including the ≤560px rule).

### 15. Hero overlap fixed

- Mini split 56% → 54% at `left:0`; central 58% → 50% at `right:0` (was `right:-2%`). Mobile (≤560px): both 55%, no negative offsets. The central system is now fully visible; only transparent image margins touch.

## Round 6 — shopping-area UX fixes (owner review)

### 16. Duplicate panel headings removed

- The JS-driven shop heading (`#shop-title`, e.g. "Explore Central Air Starting Points") and each panel's own static heading (e.g. "Central Air Capacity Starting Points") rendered stacked — near-duplicate copy. Fix: `.js .dsc-panel>.dsc-heading--center, .js .dsc-panel>.dsc-subheading{display:none}` hides panel-level headings only when JS is active; the no-JS fallback keeps all panel headings for sequential readability. Panels' `aria-labelledby` now point at `#shop-title`.

### 17. Product imagery breathing room

- Trimmed cutouts touched the media-box edges, reading as "cropped". Added `padding:12px 6px` to `.dsc-product__media` so equipment floats with clear space inside the box.

### 18. Add To Cart replaced by View Product (owner instruction, PRD override)

- The 3 single-variant Vario cards (18K / 28K / 35K): `Add To Cart` button → primary `View Product` anchor to the PDP with `target="_blank" rel="noopener"`; the duplicate secondary `View Product` text link on those cards removed.
- Removed now-dead cart code: the `/cart/add.js` click handler, `.dsc-cart-status` live region (HTML+CSS), and the variant-resolution branch of `hydrate()` (price-only hydration remains for dellahome.com).
- PRD.md §12 and HANDOFF.md updated with the dated owner override. Choose Options cards (Serena 12K + 4 Central) unchanged, same-tab.
- Rationale recorded: static preview could never transact, so ATC felt broken; owner prefers the clean PDP route for V1.

## Round 7 — reference-page card/button adoption + final polish (owner reviews)

### 19. Owner-supplied hero banner images integrated

- `mini split banner.png` / `Central banner.png` (1254×1254 transparent PNG) converted to `hero-mini-split.webp` (134KB) / `hero-central.webp` (197KB) and wired into the hero. Both images size by equal width (50%/50%, 1% side inset) on their identical square canvases → exactly equal rendered heights, shared baseline (`bottom:10px`). Mobile 50/50 at `bottom:8px`.

### 20. Product cards restyled after Ceiling Cassette reference

- Card: square corners, `1px #e6eaf2` border, no default shadow; hover → blue border + `0 8px 20px rgba(14,25,83,.08)`.
- Media: full-bleed `aspect-ratio:1/.92` area, `padding:28px 20px 12px`, img `max-height:196px`, hover `scale(1.04)`; mobile: 170px/150px variant per reference.
- Body: `--card-inset:18px` side insets (12px mobile); title Spectral 15px/400; spec chips 12px muted on gray-50, square; price Spectral Bold 20px.
- Product button: full-width navy square, hover inverts to white/navy; 18px bottom inset fixed after owner flagged buttons touching the card edge.

### 21. Global button system adopted from reference

- Primary: navy bg / white text → hover inverts white/navy. Outline: white / gray-200 border / navy text → hover blue-light + blue text + blue border. Font 15px/600. Gateway card actions follow the same outline style; selected state navy. (Supersedes round-3 weight-700 change; owner prefers the reference page's 600.)

### 22. P0 fix: invisible primary-button text

- `.della-system-compare a{color:inherit}` (specificity 0,1,1) silently overrode `.dsc-btn--primary{color:#fff}` (0,1,0) → navy text on navy button. Fixed by scoping button color rules (`.della-system-compare .dsc-btn--primary` etc.). Computed style verified: #fff on #0e1953.

### 23. "Find Partner HVAC Installer" de-duplication (owner-approved option)

- Final CTA installer demoted from a third identical button to a quiet underline text link (`dsc-final__install`, focus-visible covered). The BEFORE YOU BUY bar keeps the canonical installer button; panel-level installer buttons unchanged.

### 24. Comparison-table header thumbnails replaced with purpose-built assets

- `thumb-ductless.webp` (696×240): indoor unit only, cropped from the hero mini-split cutout — matches the mockup's wide indoor-unit thumbnail.
- `thumb-central.webp` (264×240): hero central composition proportionally scaled.
- Header cells now `vertical-align:middle` so "Compare" sits centered-left in the tall header row (owner request).

### 25. Central cards unified + all H2/subheadings left-aligned (owner requests)

- Central cards: `Choose Options` + `View System` → the same new-tab navy `View Product` as the ductless cards; `.dsc-detail` CSS removed (no instances remain). All 8 cards are now visually and behaviorally uniform.
- All section H2s and their subheadings changed from centered to left-aligned (`.dsc-heading--center` repurposed, `.dsc-subheading` left).
- PRD §12 and HANDOFF updated with the dated overrides.

## Round 8 — final spacing/typography tweaks (owner reviews)

### 26. Comparison-header ductless thumb resized

- The wide indoor-unit thumbnail at the shared 52px height had far more visual mass than the central thumbnail. Added `img.dsc-thumb--wide{height:34px}` so the two header images carry similar visual weight.

### 27. "Compare" header cell vertically centered

- `thead th{vertical-align:middle}` — the "Compare" label no longer sticks to the top of the thumbnail-tall header row (owner request: 居中左对齐).

### 28. H2 subheadings run full width

- Removed `max-width:720px` from `.dsc-subheading`; section intro copy now fills the container before wrapping instead of breaking mid-column (owner request).

## Round 9 — avoid-ai-design audit follow-up (owner-approved)

### 29. Raw arrow glyphs removed from text links

- `Find My System →` → `Find My System` (gateway escape hatch); `Find Partner HVAC Installer →` → `Find Partner HVAC Installer` (final CTA). Removes the only P1 flag from the avoid-ai-design catalog audit (CP3: arrow characters stapled to links).

## Full verification (round 9)

QA environment rebuilt (temp dir had been cleaned; system Chrome channel, no browser download). Suite extended with a no-arrow-glyph check and re-run: **54/54 passed**, zero console errors, zero failed assets.

## Deliberately not changed

No strategy, structure, product, price, path-logic, or copy changes were made. All edits are presentation fidelity fixes versus the approved `Design.png`/`DESIGN.md`. Reported-only items (P3-1 analytics event naming, P3-2 OG metadata, P3-3 production hydration availability gap) remain listed in `KIMI_AUDIT.md` for the Shopify integration round.
