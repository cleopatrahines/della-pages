# Implementation plan — image and typography refinement 2026-09-17

Work in `C:\Users\18041\Desktop\della-pages\Mini Split vs Window AC vs Portable AC`. Update the existing slug HTML. The owner assigns code to OpenCode / DeepSeek and art/planning/review to Codex.

## Read order

DEEPSEEK_IMAGE_REFINEMENT_TASK → PRD → LOCKED-COPY → DESIGN → LAYOUT-REFINEMENT → REFERENCE-MAP-2026-09-17 → products.json / PRODUCTS. The V6 full-page and Portable panel images control visual composition; copy/data/source-component specifications control implementation details.

## Current refinement sequence

1. Apply all transparent localImage paths and intrinsic dimensions from products.json, including comparison p01/p07/p11. Keep original JPEG assets.
2. Increase comparison media using DESIGN/LAYOUT-REFINEMENT; preserve complete products and equal media rows.
3. Unify every H2 to the owner-specified 32px Spectral, weight 500, line-height 1.15, navy at every breakpoint.
4. Add Evidence heading spacing and vertically center the image/questions.
5. Use the four current FAQ answers in LOCKED-COPY and include portable drainage in the installation answer.
6. Resolve the carried-forward logical rail boundary and interactive text contrast items.
7. Capture actual painted images and run the current task acceptance checks; preserve earlier QA.

## Established page requirements

1. Inspect the current file and preserve prior QA. Use current core documents rather than the historical initial image-generation prompt.
2. Establish the Whole House global container: 1360px including 24px side padding, mobile 16px. Remove hidden nested width limits while retaining the current root namespace.
3. Remove Hero category thumbnails/links and vertically center the remaining H1 and lead. Preserve the whole desktop/mobile scenes and fix initial mobile image aspect ratio.
4. Replace the six-row comparison with the specified three visual columns and two short aligned rows. Use actual p01/p07/p11 images. Mobile gets a local scroll strip with accessible arrows and native no-JS scrolling.
5. Port Whole House's product-card styling and structure; use this page's field mappings. Desktop Mini/Window four columns, Portable three columns spanning the row. Three tabs only. Series H3 plus capacity/variant provides product identity.
6. Remove section introductions, fit-check strips, coverage footer, Evidence caption/overlay labels/closed summaries and the product-area multi-room helper link. Keep technical answers in DOM inside closed accordions.
7. Port Central Air Services and its original icon images, title links, copy and 4/2/1 breakpoints; use the new global container. Port Whole House FAQ and closing-band treatment.
8. All disclosure elements initially closed. Preserve keyboard, focus, multiple-open and reduced-motion behavior.
9. Resolve the previously reproduced Tab/URL/history issue and duplicate events using a single coherent state flow. Selection updates URL without forcing scroll; comparison links reveal the product heading/tabs; Back/Forward and initial hashes restore correctly.
10. Recheck all 11 selected variant facts when public access is available. A failure to verify must be documented, not converted into fabricated price/availability. No new availability labels from historical data.
11. Run the scoped QA below, fix failures, and update HANDOFF.

## Verification

Test 1440/1280/1024/768/430/390/360 and additionally one 1920px desktop width for the new container. Preserve a 1360px border-box desktop container; at 1440px content should be about 1312px, subject to scrollbar width. Measure actual DOM geometry rather than estimating pixels from a zoomed screenshot.

Assertions:

- no page-level overflow;
- three equal Portable columns with no fourth empty track above 900px;
- all initial details closed, including FAQ/Evidence/full-model disclosures;
- deleted helper nodes absent, not merely visually hidden;
- old six-row table and rating callout absent; new comparison has all three categories and only Setup/Upfront rows;
- complete machines/hose paths visible, no overlaid labels;
- 11 cards with correct full model identities, mapped spec values, prices, selected-variant URLs and corresponding images;
- duplicate short series names allowed, composite identity unique;
- Window entry → Portable tab → reload retains Portable; Back/Forward consistent; one actual state transition does not emit two identical view events;
- default/hash/history state distinguished from active user selection;
- comparison scroll arrows work with keyboard, are not trapped, and are hidden when no scrolling is possible; no-JS native scroll and every purchase link remain usable;
- no-JS hides inert product-tab controls and displays all 11 products;
- delayed hero-mobile response does not change reserved image height or push comparison down;
- fonts, local images, buttons, service links, accordion animation and reduced-motion handling work.

Use real failure conditions in the QA runner; do not output ok:true independently of assertions. Record image dimensions/section positions for the delayed-load check; do not report that as a formal CLS score.

## Deliver

Update `mini-split-vs-window-ac-vs-portable-ac.html`; save new implementation screenshots/results in `qa/image-refinement-implementation-20260917/`; create `QA-REPORT-IMAGE-REFINEMENT.md`; update HANDOFF with actual status and remaining limits. Keep first-pass and Codex review evidence intact.

No new framework/dependency, sibling-page changes, global configuration edits, commit, push, Shopify theme edit or publishing. This remains a local review build; production canonical, theme header offset and live Shopify facts are later integration work.
