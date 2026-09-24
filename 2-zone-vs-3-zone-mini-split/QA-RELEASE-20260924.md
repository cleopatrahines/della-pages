# 2-Zone vs 3-Zone page — release QA

Owner authorized commit and push on 2026-09-24. Repository: `cleopatrahines/della-pages`; publication branch: `master`, repository root. Public page: https://cleopatrahines.github.io/della-pages/2-zone-vs-3-zone-mini-split/2-zone-vs-3-zone-mini-split.html

## Final scope

- Updated hero illustration and room-count comparison A.
- Approved scene explorer B with four distinct scene images and independent keyboard-accessible controls.
- Approved SVG connection-planning B, typography alignment and requested copy removals.
- Eight transparent product images and two category feature images.
- Services copied from the specified Ductless/Central Air reference; room-count buttons reuse the bottom CTA style.

## Verification

30 focused final browser checks passed against the final HTML in an isolated headless Chrome instance:

- All HTML images decode; all 22 unique local runtime references exist with correct case-sensitive path spelling.
- Eight product-card texts/specifications/prices match the previously committed page.
- Both product groups show four products; all four scene selections reveal the correct image, zone and collection route. Scene/product controls are independent.
- All action destinations retain the approved Della domain; keyboard selection/focus, reduced motion and no-JavaScript scene fallback work.
- SVG equipment/connection counts and page IDs are correct.
- Four service icons load; five visible FAQ items match FAQPage JSON-LD and the accordion expands.
- No horizontal overflow at 1440, 1280, 768, 390 or 360px; final desktop/mobile screenshots inspected.
- No JavaScript exceptions; requested note removals retained; `git diff --check` passed.

## Data and evidence

Product pricing is the existing static snapshot recorded on 2026-09-14; this visual release preserves the approved product data rather than asserting a fresh price check. Services wording follows the owner's specified reference.

Runtime assets, the selected three design mockups, and page documents are included. Unselected concepts, temporary outputs and other pages are outside this release.

Local QA evidence and the exact release path manifest: `C:/Users/18041/Documents/Playground/della-publish-20260924/`. Earlier per-section evidence remains linked in `HANDOFF.md`.
