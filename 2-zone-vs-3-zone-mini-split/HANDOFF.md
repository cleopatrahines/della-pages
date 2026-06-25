# HANDOFF: 2-Zone vs 3-Zone Mini Split

## Project Path

`C:\Users\18041\Desktop\della-pages\2-zone-vs-3-zone-mini-split`

## Current Files

- `PRD.md`
- `DESIGN.md`
- `PLAN.md`
- `2-zone-vs-3-zone-mini-split.html`
- `implementation-notes.md`
- `HANDOFF.md`
- `Reference Image for the Design Draft.png`
- `assets/`
- `outputs/`
- `NEXT_CHAT_PROMPT.md`

## Latest Approved Strategy

Build a Della topical decision landing page plus ecommerce guide for visitors choosing between 2-zone and 3-zone mini split systems.

The implementation uses the supplied design draft as visual reference, but PRD content wins over the mockup.

Key approved rules:

- No top benefit strip.
- No standalone install planning band.
- No `Find Partner HVAC Installer` in Premium Della Services.
- Product cards use the eight approved real products only.
- Product prices are required and were captured from live Shopify product JSON on 2026-06-24.
- Product cards use `View Product`, not `Add To Cart`.
- FAQ contains exactly five purchase-focused questions; content stays unchanged while visual styling now follows the 12K vs 18K reference FAQ block.
- Della comfort updates newsletter strip removed per user request.
- No coupon, sale, countdown, federal tax credit, Memorial Day, or American flag visuals. The only financing copy is the service-card text copied from the approved 12K vs 18K reference block.

## Latest Approved Design Image

`C:\Users\18041\Desktop\della-pages\2-zone-vs-3-zone-mini-split\Reference Image for the Design Draft.png`

## Implementation Status

Standalone HTML demo has been created:

`C:\Users\18041\Desktop\della-pages\2-zone-vs-3-zone-mini-split\2-zone-vs-3-zone-mini-split.html`

The demo omits full Shopify header/footer. Final Shopify deployment should use the real theme header/footer where possible.

## QA Status

Completed checks:

- 2-zone active tab has four 2-zone products only.
- 3-zone active tab has four 3-zone products only.
- Product CTAs are `View Product`.
- Prices are visible on all product cards.
- No `Add To Cart`.
- No `Find Partner HVAC Installer`.
- No top benefit strip.
- No standalone install planning band.
- FAQ has five visible items.
- FAQPage JSON-LD has five items and matches visible FAQ questions.
- No page-level horizontal overflow at desktop and mobile checks.
- Hero labels exist: `1 outdoor + 2 indoor units` and `1 outdoor + 3 indoor units`.

QA screenshots:

- `outputs/qa-desktop-1280.png`
- `outputs/qa-mobile-430.png`
- `outputs/qa-mobile-390.png`

## Known Risks

- Product prices are static in this standalone HTML demo. Refresh prices before publishing or move prices to dynamic Shopify/Liquid rendering.
- Hero uses official product JPGs. They are real product images, not AI-distorted, but they are not fully transparent cutouts.
- Newsletter form/comfort updates strip was removed per user request.
- Final Shopify canonical URL is not included because the final Shopify page URL has not been confirmed.
- Final deployment mode, PageFly vs Shopify custom liquid, remains open after demo approval.

## Next Codex Action

If the demo direction is approved, prepare final Shopify-ready version:

1. Refresh live prices.
2. Decide final deployment mode.
3. Adapt same HTML/CSS into PageFly/custom liquid constraints.
4. Add final canonical only after the Shopify URL is known.

## Commit/Push Status

No commit or push has been approved.

## Post-QA Service Block Change

Premium Della Services was replaced with the block from `C:\Users\18041\Desktop\della-pages\12000 BTU vs 18000 BTU Mini Split\12000-btu-vs-18000-btu-mini-split.html` per user request. This latest instruction overrides earlier service-card copy restrictions for this section.

Current service cards:

- Free & Fast Shipping
- Pay in 6 Months, 0% APR
- 24×7 Live Chat Support
- Lifetime Coverage (Mini Splits)

## Post-QA FAQ Style Change

The `2-Zone vs 3-Zone Mini Split Questions` section keeps the same five FAQ questions and answers, but its accordion styling was updated to match the `Before you choose 12K or 18K` block from `C:\Users\18041\Desktop\della-pages\12000 BTU vs 18000 BTU Mini Split\12000-btu-vs-18000-btu-mini-split.html`.

FAQPage JSON-LD remains five questions and matches the visible FAQ content.
## Post-QA Bottom CTA Style Change

The `Ready to Choose Your Zone Count?` section now follows the `Start with the collection that matches your room` block from the 12K vs 18K reference page: pale-blue section, two equal white text-only collection cards, no product images, and no `More than three rooms? View all multi-zone systems` link. The existing `btn btn-navy` button hover behavior was preserved.
## Post-QA Hero Banner Change

The hero was updated per user request on 2026-06-24:

- `banner.webp` is now used as the hero background image.
- The old right-side product comparison images were removed from the hero HTML.
- Hero support copy is one short sentence focused on common buyer situations: two bedrooms, bedroom + office, upstairs rooms, and additions.
- Both hero CTAs now use the same `btn btn-navy` styling.

## Post-QA Room-Count Strip Removal

The early room-count path strip under the hero was removed per user request on 2026-06-24. The hero now flows directly into the `Choose 2-Zone or 3-Zone by Room Count` section. The bottom two-card CTA remains.

## Post-QA Product Imagery Change

The product tab feature images now use local `2-Zone.webp` and `3-Zone.webp`. The feature image media uses `object-fit: cover` and fills its full left-side block.

The eight product-card images now use local background-blended WebP files generated from the approved Della product images:

- `assets/product-blended-01.webp` through `assets/product-blended-08.webp`

Only the edge-connected product-image background was shifted to the card pale-blue surface, so the units themselves are not covered or clipped. The product media keeps the 12K vs 18K reference sizing rhythm (`height: 262px`, `padding: 18px`, `object-fit: contain`) and uses normal blending so the image background does not create a darker square.

## Latest Handoff Update - 2026-06-25

Latest user-requested fix focused on the product-card image backgrounds in `Shop Della 2-Zone and 3-Zone Mini Splits`.

Current implementation details:

- Product cards now reference `assets/product-blended-01.webp` through `assets/product-blended-08.webp`.
- These files were generated from the approved local originals by replacing only the edge-connected source-image background with the page's pale-blue product surface.
- The unit artwork itself was not masked, covered, clipped, or recolored.
- `assets/product-original-01.webp` through `assets/product-original-08.webp` are intentionally kept as source backups.
- Earlier temporary trial assets named `product-integrated-*.webp` and `product-integrated2-*.webp` were removed.
- CSS for `.product-media` is now aligned to the 12K vs 18K reference rhythm: `height: 262px`, `padding: 18px`, `object-fit: contain` on the image, and `mix-blend-mode: normal`.

Verification performed in browser after the latest change:

- Desktop 1600px: 2-Zone product cards visually checked; gray source-image square no longer dominates and units are not covered.
- Desktop 1600px: 3-Zone product cards visually checked; card image backgrounds visually align with the pale-blue product media area, including the ceiling cassette card.
- Mobile 390px: checked no horizontal overflow after the product image update.

Next chat should continue from the existing HTML only. Do not re-run old background-removal attempts that use masks, overlays, or `mix-blend-mode: multiply`; those either left darker squares or risked visually muting white units.

## Product Card Background Lightening - 2026-06-25

User reported that the product-card image surface still looked too dark and visually muted the white equipment. The product-card media surface was lightened from the page product surface `#F4F7FF` to a card-image-specific `#FBFDFF`, and `assets/product-blended-01.webp` through `assets/product-blended-08.webp` were regenerated from the preserved `product-original-*.webp` backups using the same edge-connected background replacement approach.

No masks, overlays, clipping, redrawing, or `mix-blend-mode: multiply` were introduced. Product grouping, prices, CTAs, dimensions, and card structure were left unchanged.

Browser QA after this lightening pass:

- Desktop 1600px: visually checked both 2-Zone and 3-Zone product-card sections; product-card media background computes to `rgb(251, 253, 255)`, and the white equipment is more visible against the lighter surface.
- Mobile 390px: confirmed no horizontal overflow.
- Product images: confirmed all eight `product-blended-*.webp` files load with complete natural dimensions after scrolling through both tabs.

## Product Image Residue Cleanup - 2026-06-25

Follow-up cleanup after user flagged remaining visible gray shadow/residue in the product-card images. The eight `product-blended-*.webp` files were regenerated with a stricter near-background cleanup pass. `product-blended-08.webp` also received a targeted cleanup of the upper mounting-board / black-speck residue so the ceiling cassette card no longer shows the distracting top hardware marks in the product-card crop.

The cleanup intentionally stops short of deleting remaining real equipment edges, louvers, side panels, and grille shadows, because removing those would visibly damage the product artwork. HTML structure, products, prices, CTAs, and tab behavior were unchanged.

QA after cleanup:

- Desktop 1600px: visually checked 2-Zone and 3-Zone product tabs after the residue pass.
- Mobile 390px: confirmed no horizontal overflow.
- Known note: some subtle gray lines remain where they are part of the actual unit edge/shadow, not removable background residue.

## Product Image Over-Cleanup Rollback - 2026-06-25

After user review, the stricter residue cleanup was judged to wash out / cover parts of the white equipment. The eight `product-blended-*.webp` files were regenerated again from the preserved `product-original-*.webp` sources using only conservative edge-connected background replacement. This restores equipment edges, logos, louvers, grille detail, and natural product shadows.

Current accepted tradeoff: a small amount of original source-image edge shadow may remain, but product visibility takes priority over fully removing every faint gray mark.

QA after rollback:

- Desktop 1600px: checked both 2-Zone and 3-Zone tabs; product bodies are visible again.
- Mobile 390px: confirmed no horizontal overflow.

## Product 08 Single-Image Restore - 2026-06-25

After user review, only the ceiling cassette product card image was adjusted. `assets/product-blended-08.webp` was restored directly from `assets/product-original-08.webp` because the background-fusion pass created visible gray patch artifacts around the top ceiling-cassette hardware. No other product images, HTML, CSS, product data, prices, or layout were changed in this step.

QA:

- Desktop 1600px: checked the 3-Zone tab; the fourth product card no longer shows the gray patch artifact.
- Confirmed the 3-Zone product images load and there is no desktop horizontal overflow.

## Product Image Visibility Micro-Adjustment - 2026-06-25

User noted that the white equipment still blended too strongly into the product-card image background. To improve readability without repeating the over-cleaning issue, only `product-blended-01.webp` through `product-blended-07.webp` were regenerated from the preserved originals with a slightly deeper pale-blue image background (`#F8FAFF`) and a subtle light-edge/detail contrast lift. `product-blended-08.webp` was left unchanged from the prior single-image restore to avoid recreating the ceiling-cassette gray patch artifact.

The product card media surface in the HTML was updated to `#F8FAFF` so the generated image background and card surface match. Product data, prices, CTAs, layout, and tab behavior were unchanged.

QA:

- Desktop 1600px: checked both 2-Zone and 3-Zone tabs after the visibility adjustment.
- Mobile 390px: confirmed no horizontal overflow.

## Product Image Background Deepening - 2026-06-25

User confirmed the direction should be slightly darker, not lighter, so white equipment separates from the media surface. The product-card image surface was changed from `#F8FAFF` to `#F4F7FF`. `product-blended-01.webp` through `product-blended-07.webp` were regenerated from the preserved originals using the same deeper pale-blue background and only a very light edge/detail separation pass.

`product-blended-08.webp` was left unchanged from the single-image restore to avoid reintroducing the ceiling-cassette gray patch artifact.

QA:

- Desktop 1600px: checked both 2-Zone and 3-Zone product tabs; white equipment has stronger separation from the product-card media surface.
- Mobile 390px: confirmed no horizontal overflow.

## Product Image White-Surface Restore - 2026-06-25

User clarified that the machine surfaces should not receive the product-card background color; the equipment should retain its original white product-image appearance. `product-blended-01.webp` through `product-blended-07.webp` were restored directly from their `product-original-*.webp` sources. `product-blended-08.webp` remains the previously restored original version. The product media surface in HTML was changed to white (`#FFFFFF`) so the product images do not appear tinted by a pale-blue background.

Current rule: do not run automated background replacement or near-white cleanup over the machine surfaces. If future background removal is required, it needs manual product masks, not flood-fill color replacement.

QA:

- Desktop 1600px: checked both 2-Zone and 3-Zone tabs; machine surfaces remain original white.
- Mobile 390px: confirmed no horizontal overflow.

## Product Media Background Matched To Source Images - 2026-06-25

User clarified the product image itself should not be tinted; instead the media background should inherit the product image's own background color. The product images were left/restored as original-white equipment. The product-card media background is now set to the sampled source-image background `#EEECE8` for products 01-07. Product 08 keeps a white (`#FFFFFF`) media override because its restored source image background is white.

Current rule: do not recolor or flood-fill machine surfaces. If the product-card image square is visible, adjust the surrounding media background to match the source image background, not the equipment.

QA:

- Desktop 1600px: checked both 2-Zone and 3-Zone tabs; machine surfaces remain original white and the media background matches the source-image tone.
- Mobile 390px: confirmed no horizontal overflow.

## Product 08 Media Background Unification - 2026-06-25

User asked why the ceiling-cassette product card did not receive the same media-background color. The previous white inline override was removed from `product-blended-08.webp`'s media wrapper, so it now uses the shared `#EEECE8` product media background. The image file itself was not processed in this step, so the source image's internal white square remains visible.

QA: checked the fourth 3-Zone product card at desktop; media wrapper computes to `rgb(238, 236, 232)`.

## Product 08 Internal Background Match - 2026-06-25

User requested that the ceiling-cassette image's internal white background also match the other product cards. Only `assets/product-blended-08.webp` was regenerated from `product-original-08.webp` by replacing near-pure-white internal background pixels with the shared media color `#EEECE8`. Machine shadows, edges, dark grilles, remotes, labels, and colored details were preserved.

QA:

- Desktop 1600px: checked the fourth 3-Zone card and full 3-Zone product row; product 08 now visually matches the `#EEECE8` media surface.
- Confirmed no desktop horizontal overflow.

## Scenario Card Height + Image Swap - 2026-06-25

User requested the `Which Home Setup Sounds Closest to Yours?` four-card section to match the shorter card height of the `Which Room Sounds Most Like Yours?` section in the 12K vs 18K reference page. The current page's scenario cards now use the reference-style fixed 216px image height, tighter 12px/14px body padding, compact 15px bold body-font titles, 18px grid gap, and centered card body text.

The four scenario images were replaced with the user-provided local files in the project root:

- `Two Bedrooms.webp`
- `Bedroom and Home Office.webp`
- `Three Upstairs Rooms.webp`
- `A Bedroom, Nursery, and Office.webp`

No product cards, product images, prices, CTAs, tabs, FAQ, services, or bottom CTA were changed in this step.

Scenario card labels were also shortened to match the user-provided image subjects, allowing the card height to match the 12K vs 18K reference section rather than staying taller due to multi-line headings.

## Scenario Image Aspect Ratio Adjustment - 2026-06-25

User noted the four scenario images were too shallow and hard to read. The `Which Home Setup Sounds Closest to Yours?` card images now use `aspect-ratio: 7 / 5` with `height: auto` instead of a fixed 216px height. This intentionally makes the cards slightly taller than the previous reference-height pass so the room images are more legible. No product cards or product media were changed.

## Scenario Image Distortion Fix - 2026-06-25

The 7:5 ratio is now applied to a `.scenario-media` wrapper instead of directly forcing the `<img>` element into that ratio. The images fill the wrapper with `width: 100%`, `height: 100%`, and `object-fit: cover`, preserving natural image proportions while cropping to the card frame. This fixes the visible stretching/compression on the first scenario image.

## Scenario Image Sharpness Pass - 2026-06-25

User noted the mini split units inside the four scenario images looked blurry at card size. The original user-provided files in the project root were preserved. Four enhanced copies were generated in `assets/` as `scenario-sharp-01.webp` through `scenario-sharp-04.webp` using a conservative unsharp/contrast pass, and the `Which Home Setup Sounds Closest to Yours?` cards now point to those enhanced copies.

This step only affects the four scenario lifestyle images. Product cards, product media assets, product prices, tabs, and CTAs were not changed.

## Scenario Image Focus Crop Pass - 2026-06-25

The previous sharpness-only pass did not sufficiently improve perceived clarity because the mini split units were too small inside the full-room compositions. Four closer 7:5 crops were generated from the original user-provided scene images as `assets/scenario-focus-01.webp` through `assets/scenario-focus-04.webp`, then lightly sharpened. The scenario cards now point to these focus-crop images so the wall units occupy more card area.

The original root-level scene images and earlier `scenario-sharp-*.webp` files are preserved. Product-card assets and layout remain unchanged.
