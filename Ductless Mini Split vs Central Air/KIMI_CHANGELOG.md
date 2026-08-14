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

## Round 10 — FAQ audit/trim + Services trust section (owner decisions)

### 30. FAQ content audited against page's first-principles value and trimmed

- Audit: Q1 (main difference) duplicates the Hero direct answer + comparison-table Distribution row; Q4 (central air ductwork) duplicates the Whole-Home Ductwork table row and the Replace gateway condition. Q2/Q3/Q5/Q6 answer buying/sizing objections not covered elsewhere.
- Owner-approved: removed Q1 and Q4; FAQPage JSON-LD reduced to the same 4 entries (verified byte-match by QA).

### 31. FAQ restyled to the Ceiling Cassette vs Concealed Ducted reference

- Two-column numbered grid → single-column list: hairline dividers, Spectral 20px/500 questions, chevron affordance (CSS border chevron, rotates on open), blue hover/open state, 15px/1.7 muted answers. Markup keeps native `details/summary`; the CSS counter numbering was removed with the old layout.

### 32. Premium Della Services section added (owner override of PRD §11 non-goal)

- Rationale (owner): the page doubles as an ad landing page; trust elements matter.
- The mockup's `<section id="services">` was extracted byte-exact from the downloaded mockup (base64 icons verbatim) and adapted to the page namespace: `sec→dsc-services`, `container→dsc-container`, `svc-*→dsc-svc*`, H2 follows the page's left-aligned heading rule. Mockup colors kept (#EFF3FE cards, #6E8BE5 icon discs, #3D62D2 titles — all within the DELLA blue family).
- Position: between the Verify installation bar and the FAQ, per owner instruction. Responsive: 4 → 2 (≤1024px) → 2 compact (≤560px) → 1 (≤379px via existing product breakpoint rules... verified 2-col compact at 390px).
- Policy copy is owner-supplied from the approved mockup; recorded in PRD §12.

## Round 11 — taste-skill-inspired polish + hero rethink (owner decisions)

### 33. Services section brought onto brand tokens

- Mockup colors mapped to page tokens: `#eff3fe → --blue-light`, `#6e8be5 → --blue`, `#3d62d2 → --navy`, `#3a3a3a → --muted`, radius 14px → 6px (page card radius).
- The four 50px base64 PNG icons (~15KB) replaced with hand-drawn thin-line SVGs in the Gateway icon style (truck / return arrow / chat / shield, white stroke on the blue disc, `aria-hidden`). Fixed a regex mishap during replacement that ate the first card; all four cards verified present.

### 34. Micro fixes from the audit

- `.dsc-heading--center` naming debt removed (class deleted everywhere; the JS panel-heading-hide rule retargeted to `.js .dsc-panel>.dsc-heading`).
- `section[id]{scroll-margin-top:24px}` — anchor jumps no longer paste section titles to the viewport edge.
- FAQ answers now expand smoothly (grid-template-rows 0fr→1fr + padding transition; reduced-motion still kills it globally).

### 35. Comparison table reflects the selected path

- `setPath()` now sets `data-highlight` on `.dsc-table`: ductless/supplement → mini-split column, central → central column, neutral → none. Very subtle `#eef3fd` tint; it mirrors the visitor's own choice, so it does not violate the no-winner-badge rule.

### 36. Hero: shorter copy, single CTA, VS composite (owner requests)

- Lead: three paragraphs (~52 words) → one ~25-word paragraph keeping the SEO entities (wall-mounted ductless mini splits, room-by-room, whole-home ductwork, air handler, ducts).
- Removed the `Compare the Tradeoffs` secondary CTA: it anchored visitors past the Project Gateway, conflicting with the page's first job. One CTA remains: `Find My Best Starting Point`.
- `hero-vs.webp` (1157×503, 85KB) composited programmatically from the two owner-supplied transparent banner images — real product photos with correct DELLA logos, VS badge drawn in Spectral Bold navy. Recommended over AI regeneration precisely because image generators cannot reproduce the brand marks. The two separate hero images and their CSS were removed; the visual column now hosts one centered image at all breakpoints.
- The requested GPT image-generation prompt (kept as a fallback option) is documented in the round-11 report reply and below:

> "A wide e-commerce hero banner composition on a soft pale-blue studio gradient background (#F5F9FF fading into #EDF6FF): on the left, a white wall-mounted ductless mini split system — a sleek rectangular indoor unit mounted above a white outdoor condenser with a round black fan grille; on the right, a dark gray central HVAC system — a tall rectangular indoor air handler cabinet beside a dark gray outdoor condenser; floating between them at center, a small circular white badge with a thin navy border containing the text 'VS' in elegant navy serif type; both systems share one invisible floor line with soft realistic contact shadows, gentle studio lighting from the upper left, photorealistic product photography, clean minimal composition with generous negative space, no other text, no labels, no logos, no watermarks, wide 2.2:1 aspect ratio."

## Round 12 — owner reversions and VS refinement

### 37. Comparison-table column highlight reverted

- Owner reviewed the selected-column tint and asked to revert. Removed the `data-highlight` CSS rules and the `setPath()` JS hook; the comparison table is back to a uniform neutral surface in all path states.

### 38. Services icons restored to the original mockup assets

- Owner preferred the original icons. The four hand-drawn line SVGs were replaced by the original base64 PNG icons extracted byte-exact from the downloaded sizing-calculator mockup (truck / return / chat / wrench). The token-based colors and Spectral/Poppins typography from round 11 stay, per owner instruction ("字体不用改回去了").

### 39. VS mark simplified

- Regenerated `hero-vs.webp` (1157×503): the white circle badge is gone; a lowercase "vs" sits at the vertical center of the gap between the two systems. Final sizing after owner feedback: Spectral Bold 64px, solid navy — clearly visible without touching either product group (the gap is ~100px wide; the word spans ~55px).

## Round 13 — merged ChatGPT+Kimi review implementation (owner-approved scope)

### 40. Ductless gateway card widened (whole-home no-duct blind spot)

- Title: "Add Comfort Without Relying on Ductwork" → "Condition Your Home or Spaces Without Relying on Ductwork"; condition → "Condition one room, several rooms, or a whole home without a duct system." Eyebrow stays "Add"; no fourth card added. Fixes the real coverage gap for old-house/whole-home ductless projects.

### 41. Comparison table: +2 number-free rows

- "Primary Cost Drivers" and "Efficiency Depends On" — answers the cost/efficiency sub-intent structurally without unverified numbers or winner language.

### 42. Neutral shopping state slimmed

- The 260px dashed placeholder box ("Choose a Project Above…" + icon) replaced with one quiet line: "Choose a project above to see the DELLA starting options for that path." Products still appear on selection; no-JS fallback unchanged (all panels visible sequentially).

### 43. Hero CTA message-matches the active path

- When a path is active (URL preselect or click): hero CTA becomes "See Central Air Starting Points" / "See Wall-Mounted Mini Splits" → #shop-path. Neutral restores "Find My Best Starting Point" → #project-gateway.

### 44. og:image added

- Generated `assets/products/og-image.png` (1200×630): brand gradient, Spectral title, tagline, VS composition with real product photos. Meta tag ships with an integration comment to swap in the absolute Shopify CDN URL at launch.

### 45. 24/7 Live Support linked

- Services item title now links to the verified `https://dellahome.com/pages/contact` (fetched and confirmed live 2026-08-14).

### 46. Documented integration-era rules in HANDOFF

- Ad-ops message-match rule (`?path=` only for path-explicit ads), dual source of truth (Shopify facts vs page merchandising config), KPI framing (Qualified Action / Correction-as-success / Final Path × Source), decay triggers. Rejected items recorded in PRD §12: deleting Premium Della Services and restoring the 6-question FAQ (both are recent explicit owner decisions).

## Full verification (round 13)

QA extended (8 comparison rows, og:image presence, hero-CTA path matching) and re-run: **57/57 passed**, zero console errors, zero failed assets, no overflow at any required viewport. Gateway/table/services/hero screenshot-verified at 1440px.

## Deliberately not changed

No strategy, structure, product, price, path-logic, or copy changes were made. All edits are presentation fidelity fixes versus the approved `Design.png`/`DESIGN.md`. Reported-only items (P3-1 analytics event naming, P3-2 OG metadata, P3-3 production hydration availability gap) remain listed in `KIMI_AUDIT.md` for the Shopify integration round.

## Round 14 — installer de-dup, copy pass (humanizer + stop-slop), spacing

### 47. "Find Partner HVAC Installer" fully de-duplicated

- Only the BEFORE YOU BUY bar keeps the installer button (it is bound to the confirm-installation copy). Central panel footer and Supplement panel installers demoted to quiet underline text links (`.dsc-panel-link`), matching the final-CTA treatment. Per path view: 1 button + text links max.

### 48. Full copy pass with humanizer + stop-slop skills

- Both skills read and applied to every visible string (extracted from the live DOM, no-JS render).
- Changed:
  - Verify subheading: "Both paths can provide home comfort. The main differences are…" → "Both systems heat and cool your home. The differences are in how air moves, how rooms are controlled, and what installation involves." (weak copula + hedge removed, active voice)
  - Supplement panel: "…may be worth considering for a garage, addition, converted space, or persistent hot or cold room." → "…can cover a garage, addition, converted space, or a room that stays too hot or cold." (hedge stack removed, "can" retained per claims policy)
  - FAQ Q2/Q3 answers: passive "It can be used / can be considered" → active "it can handle / can cover"; JSON-LD re-synced byte-exact (both replacements hit exactly 2 locations each).
- Kept deliberately (documented): "Start with the project, not the equipment." (negative parallelism, but approved-mockup copy doing real corrective work); claims-policy hedges "primarily/usually/can/may" (PRD §8 outranks style rules); the three "Ready to…" final-CTA variants (intentional dynamic template); Services policy copy (owner-supplied verbatim).
- Flagged, not changed (PRD-locked §6.4): comparison H2 "What Actually Changes?" — "actually" is a humanizer §7 watch word; heading is PRD-approved copy, so any change needs owner sign-off.
- stop-slop score after pass: Directness 9, Rhythm 8, Trust 9, Authenticity 8, Density 9 = 43/50 (threshold 35).

### 49. Section spacing tightened

- Rhythm reduced for a 7-section page: `.dsc-section` 76→64px, `.dsc-section--compact`/`dsc-services` 58→48px, final CTA 56/72→48/56px; mobile (≤820px) 60/50→48/40px. Page height at 1440px: 3584px.

## Full verification (round 14)

QA re-run after each change set: **57/57 passed**, zero console errors, no overflow at any viewport. Full-page screenshot verified at 1440px.

## Round 15 — heading tidy + owner-delegated decision

### 50. Comparison H2: "What Actually Changes?" → "What Changes?"

- Owner delegated the decision; removed the humanizer §7 watch word. PRD §12 records the override of §6.4.

## Full verification (round 15)

QA re-run: **57/57 passed**, zero console errors.
