# Project handoff

Project: `C:\Users\18041\Desktop\della-pages\Mini Split vs Window AC vs Portable AC`
Date: 2026-09-17.

## Final review and commit authorization — 2026-09-17

Owner accepted the final page and authorized a local Git commit. Codex reviewed the final HTML SHA256 594E411912104FED9E8FF5F5AD76DF23210784A81D08DDFC2FC9DC2401F17151, inspected desktop/mobile and separately painted Hero captures, and reran the existing Chrome QA suite: 121/121 passed. Comparison scale/proportions are accepted. Hero contains H1 and lead; price-to-button spacing is 16px across product cards. Core docs now reflect those final owner instructions.

See RELEASE-QA.md and qa/codex-final-review-20260917/qa-results.json. Commit scope is this page's runtime assets, product data, maintenance documents and compact QA evidence. Historic images, research bundles and unrelated pages remain local. Remote push and publication are separate from this authorized local commit.

## Implemented refinement — 2026-09-17

Codex prepared 11 true-alpha PNGs from eight unique originals with the owner-approved pixel-preserving programmatic workflow. Original JPEGs remain. products.json maps PNG paths and intrinsic dimensions; product facts are unchanged. **DeepSeek applied this refinement to the HTML and it is now browser-verified — see "Implementation status — image refinement 2026-09-17" below.** Asset evidence is Codex's `qa/image-refinement-20260917/` (preserved, untouched).

Active assignment was **DEEPSEEK_IMAGE_REFINEMENT_TASK.md**. Applied changes: transparent media in comparison and product cards, larger comparison images (280/235/220px), all H2 32px Spectral 500, Evidence spacing + vertical centering, four purchase-decision FAQs with drainage moved into the installation answer. All 19 disclosures are closed initially.

Carry-forward finishing checks (now fixed and verified): mobile comparison first/last logical boundary, interactive small-text contrast, and desktop Hero screenshot painting.

Previous HTML baseline: SHA256 C4401808…; current: SHA256 594E4119… (66,058 bytes, after the owner-directed hero button removal and card price/button spacing change). Core docs and the previous manifest are archived under qa/image-refinement-20260917/before. Historical notes below record earlier states and do not override the current status.

## Owner's current instruction

Codex handles research, planning, imagery and review. OpenCode / DeepSeek writes the page implementation. The owner authorized Codex to correct remaining issues in the submitted mockup and prepare a concrete coding task. No further grill-me interview is requested.

## Current state

- Six-section decision-commerce structure retained.
- Corrected layout baseline: `design/final-mockup-v6.png`.
- Independent hero desktop/mobile and installation illustration under assets; latest imagery follows the owner's supplied DELLA indoor/outdoor units, keeps both fully visible, and uses natural architectural transitions without white graphic dividers.
- Window and portable machines also follow owner-supplied references. The selected portable scene example uses a smooth front, top outlet and two hoses; this illustration does not imply that every portable SKU has the same hose design.
- 11 real selected products, selected-variant URLs and research-time prices in products.json; original product images downloaded locally.
- Final English copy and all answers in LOCKED-COPY.md.
- DESIGN.md and PLAN.md define responsive behavior and implementation tests.
- Current implementation assignment: DEEPSEEK_IMAGE_REFINEMENT_TASK.md; PORTABLE layout reference design/portable-panel-v6.png.
- HTML implemented and locally browser-tested across three rounds (2026-09-16 first pass, V6 visual refresh, image refinement). Current status: "Implementation status — image refinement 2026-09-17" below; reports `QA-REPORT.md`, `QA-REPORT-VISUAL-REFRESH.md`, `QA-REPORT-IMAGE-REFINEMENT.md`.

## Implementation status (OpenCode / DeepSeek, 2026-09-16)

Delivered, not committed or published.

- `mini-split-vs-window-ac-vs-portable-ac.html`: single standalone page, inline CSS/JS scoped under `.della-ac-compare`, local fonts and images. No frameworks, no runtime network dependency, no analytics install.
- All six sections built in order with real DOM from `LOCKED-COPY.md`; all 11 products, prices, spec rows and selected-variant URLs baked into the initial HTML from `products.json` (so `file://` preview needs no JSON fetch). `products.json` remains the maintenance source.
- Three tabs only (Mini Split / Window AC / Portable AC), initial counts 4/4/3, no All Products, no questionnaire, no blank fourth card.
- Hero uses `assets/hero-desktop.png` / `assets/hero-mobile.png` at intrinsic ratio (switch at 1100px, copy stacks above the image below that); evidence uses `assets/installation-comparison.png`. No fixed-height cover crop; both mini-split units stay visible.
- Real tab, anchor, hashchange, Back/Forward, keyboard, no-JS and reduced-motion behavior; native `<details>` accordions.
- Product facts re-verified live on 2026-09-16: all 11 selected variants match `products.json` (price, availability, SKU) and all destination links return 200. Full evidence in `QA-REPORT.md` §7.

New files: `QA-REPORT.md`; `qa/capture.mjs` (CDP harness, no npm dependency); `qa/qa-results.json`; 14 screenshots `qa/*.png`.

## Implementation status — visual refresh 2026-09-17 (OpenCode / DeepSeek)

Delivered, not committed or published. First-pass evidence and `qa/codex-review-20260917/` were preserved.

- Rebuilt to the V6 design: Hero without category thumbnails; three open image-led comparison columns with only Setup/Upfront; Whole House 1360px border-box container (24px desktop / 16px mobile padding); Whole House product-card grammar with 4/4/3 products and three equal desktop Portable tracks; Evidence with no overlay labels or caption; Central Air Services component with the original embedded icons and 4/2/1 breakpoints; Whole House full-width FAQ and pale closing band; every disclosure closed initially.
- Carry-forward fixes completed: equipment no longer covered by labels (R1); Tab/URL/history synchronised with deduplicated events via one idempotent state path (R2); mobile Hero reserves the true 4:3 ratio before load, 0px shift under a 2.6s delay (R3); product specs are a valid `dl`; no-JS hides the tab controls and shows all 11 products.
- Note: the earlier "restore two-column mobile services" request is superseded by the latest owner instruction to reuse Central Air's 4/2/1 breakpoints (2 at ≤820px, 1 at ≤560px). This was implemented and measured.
- Product facts re-verified live on 2026-09-17: 11/11 selected variants match `products.json` (price, availability, SKU); all destination links resolve 200. Evidence in `qa/visual-refresh-20260917/live-verification-20260917.md`.

New files this round: `QA-REPORT-VISUAL-REFRESH.md`; `qa/visual-refresh-20260917/capture.mjs` (assertion-based runner, exits non-zero on failure); `qa-results.json`; `live-verification-20260917.md`; 16 screenshots. Round result: 103/103 assertions pass, 0 console errors, 0 failed requests.

### Open items for Codex review (V6)

1. Hero copy column is 27% wide at desktop with `Window AC` and `Portable AC` kept on one line (three lines at 1440). Accepted by Codex V6 review; kept.
2. Comparison strip at ≤767px shows ~82% columns with a next-column peek and 44px arrow controls when scrollable. Accepted; the first/last rail boundary was fixed in the image-refinement round.
3. Shopify embedding still needs: larger `scroll-margin-top` for the theme header, dropping the top-level `html,body` margin reset, **keeping or migrating the `.js` initialization** (do NOT delete it — `:not(.js) .tabs`/`.cmp-nav` depend on it), and Liquid/server-rendered product facts. No canonical, tracking or schema was added.

## Implementation status — image refinement 2026-09-17 (OpenCode / DeepSeek)

Delivered, not committed or published. Earlier evidence folders were preserved.

- All 14 image positions (3 comparison + 11 cards) use the transparent `assets/products-cutout/pNN.png` `localImage` with each file's intrinsic `width`/`height`; original JPEGs retained; media stays white with `contain`, no blend/filter/crop.
- Comparison media 280px desktop (>1100), 235px at 768–1100, 220px ≤767, equal media row, each image at its own ratio (p07 capped at 330px width).
- All six H2 are `'Della AC Spectral'`, 32px, 500, line-height 1.15, `#0E1953` at every tested width; conflicting Services/mobile/closing sizes removed.
- Evidence H2 gap 32px desktop / 24px mobile, grid vertically centred (image/list centre Δ ≤ 0.01px closed, ≤ 0.01px expanded, list height natural 251→945px).
- FAQ is the four current questions; portable drainage moved into the "What needs to fit?" Evidence answer. 19 disclosures, all closed initially.
- V6-1 fixed: rail start keeps 16px padding, `scroll-padding-inline` matches, previous disabled at the logical start, next disabled at the end, round-trip verified at 360/390/430.
- V6-2 fixed: small-text hover/open now navy or `#466FCB`; measured 4.53–16.37:1. Brand blue kept for icons/borders/arrows.
- V6-3 verified: `hero-painted-1440.png` clip has distinct 862 / nonUniform 0.80 — the desktop Hero picture is really drawn in the capture, not just a sized box.
- Owner-directed follow-ups: the hero `Compare the options` button was removed (with its unused CSS rule) so the hero shows only H1 + lead, vertically centred; and the product-card price now has 16px of breathing space before the `View Product` button. Re-ran the suite after each change: 121/121 still pass.
- Regression kept green: 1360px container (1312 at 1440), no page overflow, Portable three equal tracks, Tab/URL/history one-event recovery, no-JS shows all 11 products, reduced motion, `file://`.

Runner: `qa/image-refinement-implementation-20260917/capture.mjs` (exits non-zero on failure). Result: **121 assertions, 121 passed, 0 failed**, 14 screenshots. Report: `QA-REPORT-IMAGE-REFINEMENT.md`. Full data: `qa-results.json`.

### Remaining review notes (image-refinement round)

1. Confirm the comparison column images read as clearly larger and that the per-shape ratio (window AC wider/shorter) is acceptable versus a forced equal size.
2. Confirm the 280/235/220px media heights and the 330px max image width match intent at 1920 (image widths remain capped at 330 by design).
3. Commercial facts were not re-fetched this pass; the same-day `qa/visual-refresh-20260917/live-verification-20260917.md` recheck (11/11 variants, all links 200) stands and facts are unchanged.

## What to use

Use the final mockup for structure and visual rhythm, the independent assets for actual image elements, the copy document for all text, and the product manifest for commerce facts. The user-supplied mockup and old generation prompt are retained as inputs, not implementation authorities.

## Resolved content choices

- Comparison does not declare Mini Split a universal performance winner.
- Primary scope is single-room/independent-space cooling, with a small multi-room link.
- Exactly three category tabs, no All Products.
- Four evidence questions explain decision factors; four FAQ questions address rental permission, unsuitable windows, separate rooms and winter heating.
- Generic service links preserve policy scope instead of promising universal lifetime coverage.
- Per-variant price and voltage are tied to the same PDP URL.
- Window-fit information absent from the evidence is not invented from cabinet dimensions.

## Work completed by DeepSeek in the first pass (2026-09-16), superseded by the V6 refresh

Implemented the HTML and accessible responsive interactions, rechecked product availability/price and links (network was available), and ran the PLAN tests. Documented in `QA-REPORT.md`, `qa/qa-results.json` and `qa/*.png`. This describes the pre-V6 page; the current implementation is in "Implementation status — visual refresh 2026-09-17".

Open items for Codex to review or decide:

1. Confirm the active tab treatment (navy fill / white text for AA) against the mockup, which showed brand blue. Chosen for contrast per DESIGN.md's small-text rule.
2. Confirm the desktop hero heading wraps to four lines at 1440px inside the ~25% copy column; acceptable per DESIGN, but flagged in case a tighter heading is preferred.
3. For Shopify embedding: raise `scroll-margin-top` past the theme header, drop the top-level `html,body` margin reset, and replace the baked-in snapshot with Liquid/server-rendered product facts. No canonical, tracking or schema was added, by instruction.

## Deployment boundary

This is a local review build. Final Shopify URL and the production product-data integration are not provided. Omit a fabricated canonical. Static preview prices must be replaced by live Shopify-owned facts or an approved refresh process for long-term deployment.

Local commit authorized by the owner on 2026-09-17 after final review. Remote push, publishing, sibling-page edits and live Shopify changes remain outside scope.

## QA completed by Codex before coding

Reviewed the user image and generated correction against the six-section PRD; removed misleading category rankings and the extra tab; inspected generated image assets and supplied corrections; checked manifest counts/variant identities and downloaded 11 images; visually spot-checked p01/p07/p11; checked project documents and references. This is design/data handoff QA, not final HTML QA.

## Models and execution

The latest user-specified division supersedes the earlier default Luna coding delegation. No coding subagent or separate OpenCode session was launched by Codex. The user will pass the implementation task to DeepSeek. The tools do not expose a service-tier setting for that external session, so none is asserted.

## Codex independent review — 2026-09-17

Status: revision requested; HTML unchanged by Codex. See CODEX-REVIEW-2026-09-17.md and DEEPSEEK_REVISION_TASK.md.

Navy active tabs are accepted. Required fixes: remove equipment-obscuring labels, synchronize selected tab/URL and deduplicate history events, reserve the correct mobile Hero aspect ratio before loading, and restore two-column mobile services. Improve the desktop title to keep Portable AC together. Small semantic/no-JS corrections are included in the revision task. (The two-column mobile Services item was later superseded by the owner's V6 instruction to reuse Central Air's 4/2/1 breakpoints; the other items were fixed in the 2026-09-17 refresh.)

Independently checked 11 product cards against products.json: all prices, full titles, specs, variant URLs and image paths match. Review evidence is in qa/codex-review-20260917. Product live status was not newly audited on September 17. DeepSeek should implement and test revision 2, preserve first-pass evidence, and return it for Codex review. No commit/push/publish authorized.


## Codex V6 independent review — 2026-09-17

Visual direction accepted, with a focused finishing pass remaining. Hero 27% / three lines and mobile comparison 82% / 44px controls are accepted. Fix logical first/last scroll boundaries, interactive small-text contrast, and regenerate desktop Hero screenshot evidence after actual painting. See CODEX-V6-REVIEW-2026-09-17.md and DEEPSEEK_V6_FINISH_TASK.md. Independent evidence: qa/codex-v6-review-20260917.

The Hero image is visible in foreground browsing of the unchanged source, so the blank automated screenshots are treated as an evidence/capture issue rather than a confirmed missing-image page defect. Codex did not modify the HTML. Product mapping and one-event history recovery were independently checked.

Shopify note correction: preserve or relocate the .js initialization responsibility; do not simply remove its only inline initializer, because the no-JS CSS would then hide controls. Shopify integration and publishing remain separate, unauthorized work.

Resolution of this review's items: V6-1 rail boundaries, V6-2 interactive small-text contrast and V6-3 desktop Hero paint evidence were fixed and verified in the 2026-09-17 image-refinement round; the V6-4 wording correction is applied above. See `QA-REPORT-IMAGE-REFINEMENT.md` and `qa/image-refinement-implementation-20260917/`.
