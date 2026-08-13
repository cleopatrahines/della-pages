# KIMI_AUDIT — Ductless Mini Split vs Central Air

Auditor: Kimi (k3) · Date: 2026-08-13
Scope: local static HTML only (`ductless-mini-split-vs-central-air.html`). No Shopify/PageFly import, no cart testing, no canonical, no Liquid, no git operations.
Authority order applied: PRD.md > DESIGN.md > Design.png > PLAN.md > current HTML.
Skills read and enforced: `della-page-builder/SKILL.md`, `frontend-design/SKILL.md`.

---

## Executive Summary

The page is in **very good shape**. Implementation faithfully follows the locked strategy: Hero → Project Gateway → Conditional Shopping → Verify → FAQ → Contextual Final CTA, with no forbidden modules (no Quick Answer, Benefit Strip, duplicate tabs, Services, promo blocks, review walls, or fourth Gateway card). All 8 products, asymmetric Ductless/Central card hierarchies, the 3 ATC / 5 Choose Options split, and the fitting-area omission rule are correctly implemented.

Browser QA across 7 viewports × neutral/ductless/central/supplement/no-JS states produced **50/50 passing checks** with zero console errors and zero broken assets.

**Issues found and fixed (all P2, visual fidelity vs `Design.png`):**

1. Desktop Hero H1 exceeded the DESIGN.md size range (65px vs spec 48–56px) and wrapped to 3 lines at ≥1280px. Fixed (`65px` → `56px`).
2. Hero CTAs wrapped to a vertical stack at all desktop widths (measured: buttons need 516px, copy column was 499px) while the mockup shows them side-by-side. Fixed by rebalancing the hero grid (.86/1.14 → .92/1.08) and tightening button padding at ≤1024px.
3. Hero lead was a single paragraph; the mockup's rhythm (and PRD's three sentences) call for three short paragraphs. Split — wording unchanged.
4. Comparison table header was text-only; the mockup shows small product thumbnails in the header cells. Added (existing local assets, `alt=""` decorative).
5. FAQ items were unnumbered; the mockup numbers them 1.–6. Added via CSS counter (no markup change, native `details/summary` preserved).

**Overall conclusion after revision: page passes audit and now matches the approved mockup composition on all verified dimensions. 50/50 QA checks pass.**

> Revision note: the first audit pass under-weighted visual fidelity to `Design.png` and only fixed the H1. After owner feedback, a second pixel-level comparison pass identified and fixed items 2–5 above.

---

## Verified strengths (audit evidence)

| Area | Evidence |
|---|---|
| Strategy compliance | 6 blocks only, in locked order; neutral organic default; no forbidden modules found in DOM |
| Product matrix | 8 products, correct handles/PDPs/images; 3 `button[data-variant-id]` ATC + 5 `Choose Options` anchors; no `variants[0]` guessing (explicit variant IDs from `sources.md`) |
| Asymmetric merchandising | Ductless: role label → image → title → specs → price → action → View Product. Central: large BTU → SEER2 reference → image → title → price → action → View System. Confirmed in DOM and screenshots |
| Central fitting-area | Correctly omitted; "Professional sizing required" + load-calculation disclaimer present |
| Path state machine | `?path=ductless/central/supplement` preselect without auto-scroll (scrollY=0 verified); invalid `?path=bogus` stays neutral; `replaceState` preserves `utm_source`/`gclid`/`fbclid`; Change Project removes only `path`, restores default CTA, moves focus to Gateway |
| No-JS fallback | All 3 panels render sequentially and readable; neutral prompt correctly hidden; screenshot-verified |
| FAQ | 6 visible `details/summary`; JSON-LD FAQPage matches visible Q&A **exactly** (programmatic string comparison, 6/6) |
| Semantics/a11y | Single H1; heading order H1→H2→H3→H4 with no skips; Gateway buttons are `<button aria-pressed>`; inactive panels get `aria-hidden`+`inert`; `role="status"` live region for cart; decorative hero images `alt=""` inside `aria-hidden`; product alts concise |
| Performance/CLS | Local fonts with `font-display:swap`; explicit image width/height; fixed media boxes with `object-fit:contain`; hero `fetchpriority="high"`, products `loading="lazy"`; no third-party libraries |
| Reduced motion | `prefers-reduced-motion` media query kills transitions/animations; JS scroll honors it |
| Preview cart guard | ATC clicks on `file://` show "Preview only" status, no navigation, no network request |
| No horizontal overflow | bodyWidth == viewportWidth at 360/390/430/768/1024/1280/1440 in all tested states |

---

## Issues

### P0 — none

No blockers. Page structure, strategy, products, pricing display, and path logic all conform to PRD.

### P1 — none

No high-severity defects found in this round's scope.

### P2 — fixed

**P2-1 · Desktop Hero H1 oversized, 3-line wrap breaks approved composition**
- Evidence: `.dsc-hero h1` used `clamp(45px,4.6vw,65px)`. At 1440px the computed 65px made "Ductless Mini Split" ≈536px wide vs a ≈499px copy column, wrapping to 3 lines ("Ductless Mini / Split / vs Central Air"). `Design.png` shows 2 lines; DESIGN.md specifies H1 48–56px desktop.
- Location: CSS `.dsc-hero h1`.
- Fix: clamp max `65px` → `56px`. Measured text width at 56px = 462px < column → 2 lines restored at 1280/1440; screenshot-verified.
- Status: **Fixed.**

**P2-2 · Hero CTAs wrapped vertically instead of side-by-side**
- Evidence: measured in Chrome — "Find My Best Starting Point" 265.25px + "Compare the Tradeoffs" 238.81px + 12px gap = 516px, but the hero copy column was 498.8px (`.86fr` of the grid), so the buttons wrapped to two rows at 1440/1280/1024. `Design.png` shows both CTAs on one row.
- Location: CSS `.dsc-hero__inner` grid template.
- Fix: grid `.86fr/1.14fr` → `.92fr/1.08fr` (copy column → 533.6px, visual column 626px ≥ its 480px min); added `gap:10px; padding-inline:14px` for hero actions at ≤1024px so 1024px (480px column) also keeps one row. Measured after fix: 1 row at 1440/1280/1024.
- Status: **Fixed.**

**P2-3 · Hero lead paragraph structure did not match mockup rhythm**
- Evidence: mockup shows three short copy blocks (ductless sentence / central sentence / "Start with the project…"); HTML rendered one long paragraph. PRD supporting copy is exactly these three sentences, so splitting is presentation-only.
- Fix: split into three `.dsc-hero__lead` paragraphs with `.dsc-hero__lead+.dsc-hero__lead{margin-top:14px}`. Wording unchanged.
- Status: **Fixed.**

**P2-4 · Comparison table header missing product thumbnails**
- Evidence: `Design.png` shows a small mini-split image and a small central-system image inside the light-blue header cells; HTML header was text-only.
- Fix: added `loading="lazy"`, `alt=""` (decorative) thumbnails using existing localized assets (`serena-12k.jpg`, `central-34k.jpg`) with `.dsc-table thead img{height:52px;object-fit:contain;margin:8px auto 0}`. Header text retained for accessibility; mobile stacked view unaffected (thead is visually hidden there).
- Status: **Fixed.**

**P2-5 · FAQ items unnumbered vs mockup's 1.–6.**
- Evidence: `Design.png` numbers the six FAQs (left column 1–3, right 4–6); HTML had no numbers.
- Fix: pure-CSS counter (`counter-reset:faq` on `.dsc-faq__grid`, `summary:before{content:counter(faq) "."}`) — no markup change, native `details/summary` and FAQ JSON-LD untouched.
- Status: **Fixed.**

### P3 — reported, intentionally not changed

**P3-1 · Gateway "Find My System" escape-hatch link carries `data-analytics-event="della_final_cta_click"`**
- Location: HTML line 230. It is a Product Finder link under the Gateway, not the final CTA; the event name is semantically misleading. PLAN.md's hook list has no dedicated product-finder event, so any rename is a taxonomy decision, not a defect fix. Recommend owner decide the event name before production analytics wiring.

**P3-2 · OG metadata minimal**
- `og:title` ("Ductless Mini Split vs Central Air | DELLA") differs from the approved title tag, and there is no `og:image`. Acceptable for static preview; production social metadata should be finalized at Shopify integration. Not changed (metadata strategy belongs to deployment round).

**P3-3 · Production hydration does not re-verify Choose Options products**
- In `hydrate()`, availability re-check and Sold-Out downgrade only run for button/ATC actions; the 5 `Choose Options` anchors (Serena 12K + 4 Central) never get a Sold Out state if they go unavailable. Impact is low (PDP handles unavailability), and this is production-runtime behavior outside this round's local-HTML scope. Flagged for the Shopify integration round.

---

## Unimplemented suggestions (with reasons)

| Suggestion | Why not implemented |
|---|---|
| Unify/normalize Ductless and Central cards | Explicitly forbidden by PRD §5; asymmetry is the strategy |
| Add Quick Answer / Benefit Strip / Services / reviews | Explicitly forbidden modules |
| Add Central fitting-area figures | No verified official data (`sources.md` 2026-08-13); PRD requires omission until verified |
| Add canonical / og:url | Production URL not yet live; PRD forbids hard-coding canonical in preview |
| Rename analytics event on Product Finder link (P3-1) | Taxonomy decision reserved for owner |
| Extract inline CSS/JS, add build tooling | Forbidden this round (no new dependencies/frameworks); single-file inline is the delivery format |
| Convert images to WebP per PLAN.md file tree | HTML + assets currently use `.jpg` consistently and all load; renaming format is cosmetic, zero user-facing value, and risks breaking the verified asset mapping. Left as-is |

## Shopify/PageFly follow-up risks

1. **Style pollution**: page CSS is namespaced under `.della-system-compare` — good. Residual risk: PageFly global resets (`* { margin }`, img rules) could affect the wrapper; verify after embed. The page sets `body style="margin:0"` inline, which PageFly/Shopify may strip — harmless inside a theme, but confirm.
2. **`.js` class collision**: the no-JS/JS switch relies on `document.documentElement.classList.replace('no-js','js')` in an inline head script. Shopify themes also toggle a `js` class on `<html>`; behavior is compatible (both mean "JS on"), but if the theme removes `no-js` before this script runs, `replace()` silently no-ops while the theme adds `js` — end state is still correct. Low risk, verify once embedded.
3. **Cart runtime untested**: `/cart/add.js` POST, 422 handling, and same-tab cart navigation can only be validated on the live storefront (HANDOFF.md already notes this).
4. **Liquid vs Ajax decision pending**: PLAN.md prefers `all_products` Liquid hydration (8 handles < 20 limit); if PageFly surface can't evaluate Liquid, the Ajax fallback in the script is already in place. Decide at integration.
5. **Choose Options availability gap** (P3-3) should be closed during production hydration work.
6. **Analytics**: `window.gtag` calls are guarded; CustomEvent `della:analytics` is dispatched for theme-level listeners. Confirm the production analytics stack reads one of these before launch.
7. **Canonical**: enable Liquid `canonical_url` only after the Page handle `ductless-mini-split-vs-central-air` exists.

## QA summary (full detail in `k3-qa-report.json`)

- 50 checks, 50 passed, 0 failed.
- Viewports: 1440 / 1280 / 1024 / 768 / 430 / 390 / 360 — no horizontal overflow, all images loaded.
- States: neutral, `?path=ductless`, `?path=central`, `?path=supplement`, invalid `?path=`, gateway click switching, Change Project reset, FAQ toggle, keyboard Enter activation, focus states, reduced motion, no-JS, preview ATC guard.
- Console errors: none. Failed local assets: none.
- Screenshots reviewed against `Design.png` for brand consistency, hero hierarchy, gateway clarity, card efficiency, mobile rhythm, CTA/path consistency, and price/action prominence.
