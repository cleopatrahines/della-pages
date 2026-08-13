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

## Full verification

After all 5 fixes the complete QA suite was re-run: **50/50 checks passed**, zero console errors, zero failed assets, no horizontal overflow at 360/390/430/768/1024/1280/1440, all four path states + invalid-param + no-JS + keyboard + reduced-motion + preview-ATC-guard verified, and fresh screenshots were compared against `Design.png`.

## Deliberately not changed

No strategy, structure, product, price, path-logic, or copy changes were made. All edits are presentation fidelity fixes versus the approved `Design.png`/`DESIGN.md`. Reported-only items (P3-1 analytics event naming, P3-2 OG metadata, P3-3 production hydration availability gap) remain listed in `KIMI_AUDIT.md` for the Shopify integration round.
