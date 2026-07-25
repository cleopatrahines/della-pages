# Implementation Notes: 2-Zone vs 3-Zone Mini Split

## Price Snapshot

Prices were captured from Della official Shopify product JSON endpoints on 2026-06-24.

| Product | Price | Available |
| --- | ---: | --- |
| DELLA Vario Series 20000 BTU Dual Zone Mini Split AC (9K + 9K) - Up to 800 Sq.Ft. | $1,829.96 | Yes |
| DELLA Optima Series 18000 BTU Dual Zone Mini Split AC (9K + 12K) - Up to 950 Sq.Ft. | $2,039.96 | Yes |
| DELLA Optima Series 18000 BTU Dual Zone Mini Split AC (12K + 12K) - Up to 1100 Sq.Ft. | $2,089.96 | Yes |
| DELLA Vario Series 28000 BTU Dual Zone Mini Split AC (12K + 18K) - Up to 1550 Sq.Ft. | $2,339.96 | Yes |
| DELLA Vario Series 28000 BTU Tri-Zone Mini Split AC (9K + 9K + 12K) - Up to 1350 Sq.Ft. | $2,484.96 | Yes |
| DELLA Optima Series 27000 BTU Tri-Zone Mini Split AC (9K + 12K + 12K) - Up to 1500 Sq.Ft. | $2,784.96 | Yes |
| DELLA Vario Series 35000 BTU Tri-Zone Mini Split AC (9K + 12K + 18K) - Up to 1950 Sq.Ft. | $3,204.96 | Yes |
| DELLA 35000 BTU Tri-Zone Ceiling Cassette Mini Split AC (12K + 12K + 18K) - Up to 2100 Sq.Ft. | $4,564.96 | Yes |

## Static Demo Risk

The standalone HTML contains static price text. If the page is published through Shopify, prices should be refreshed immediately before launch or rendered dynamically through Shopify/Liquid/PageFly product data.

## Asset Notes

Local assets copied into `assets/`:

- Spectral font files.
- Poppins font files.
- Four existing Della home situation images.

Product card images were derived from the approved Della CDN image URLs and saved as `assets/product-blended-01.webp` through `assets/product-blended-08.webp`. The edge-connected source-image background was shifted to the card pale-blue surface, while the units were left intact; product media uses `object-fit: contain` and normal blending. The product tab feature images use local `2-Zone.webp` and `3-Zone.webp`.

## Schema Notes

FAQPage JSON-LD is included and matches the five visible FAQ questions.

No Product/Offer schema was added because static demo price/inventory data can become stale.

No canonical tag was added because the final Shopify URL is not confirmed.

## Post-QA Change

The `Get Della Comfort Updates` newsletter strip was removed after user review. The page now ends with the bottom CTA section.

## Post-QA Service Block Change

Premium Della Services was replaced with the block from `C:\Users\18041\Desktop\della-pages\12000 BTU vs 18000 BTU Mini Split\12000-btu-vs-18000-btu-mini-split.html` per user request. This latest instruction overrides earlier service-card copy restrictions for this section.

Current service cards:

- Free & Fast Shipping
- Pay in 6 Months, 0% APR
- 24×7 Live Chat Support
- Lifetime Coverage (Mini Splits)

## Post-QA FAQ Style Change

The FAQ content and FAQPage JSON-LD were kept unchanged. The visible FAQ accordion style was changed to follow the `Before you choose 12K or 18K` reference block: single-column line-separated items, Spectral question text, muted 15px answers, and arrow-style open/close icon.
## Post-QA Bottom CTA Style Change

The bottom CTA was changed to match the 12K vs 18K reference collection block. It now uses two text-only white cards on a pale-blue section, keeps the existing navy button hover behavior, removes product images, and removes the extra multi-zone text link.

## Product Card Background Lightening - 2026-06-25

After visual review, the product media surface was lightened from the page product surface `#F4F7FF` to a card-image-specific `#FBFDFF`. The eight `product-blended-*.webp` assets were regenerated from the preserved originals so the baked image background matches the lighter card surface. Product artwork was not redrawn, masked, clipped, or blended with CSS effects.

## Product Image Residue Cleanup - 2026-06-25

The `product-blended-*.webp` assets were regenerated with stricter near-background residue cleanup after visual review found remaining gray edge marks. `product-blended-08.webp` received an additional targeted cleanup to remove the distracting upper mounting-board and black-speck residue from the ceiling-cassette image. Remaining fine gray marks are product edge/shadow detail and were preserved to avoid damaging the equipment artwork.

## Product Image Over-Cleanup Rollback - 2026-06-25

The stricter residue cleanup was rolled back because it made the white equipment look covered or washed out. Current `product-blended-*.webp` files are regenerated from `product-original-*.webp` with conservative edge-connected background replacement only. Do not rerun broad near-white residue cleanup unless a manual mask is created for each product, because automated cleanup can damage white equipment detail.

## Product 08 Single-Image Restore - 2026-06-25

`product-blended-08.webp` was restored from `product-original-08.webp` only. Do not apply the batch background-fusion cleanup to this ceiling-cassette image again unless a manual mask is used, because the original top hardware creates gray patch artifacts when processed automatically.

## Product Image Visibility Micro-Adjustment - 2026-06-25

`product-blended-01.webp` through `product-blended-07.webp` now use a slightly deeper pale-blue background (`#F8FAFF`) plus subtle equipment edge/detail contrast enhancement so white indoor units do not disappear into the image surface. `product-blended-08.webp` remains restored from the original and should not be batch-processed without manual masking.

## Product Image Background Deepening - 2026-06-25

Product-card media background is now `#F4F7FF` instead of `#F8FAFF`. `product-blended-01.webp` through `product-blended-07.webp` were regenerated to match this slightly deeper pale-blue surface. `product-blended-08.webp` remains restored from the original and should stay excluded from batch image processing.

## Product Image White-Surface Restore - 2026-06-25

`product-blended-01.webp` through `product-blended-07.webp` are restored from the original product images so machine surfaces remain white and are no longer tinted by card background processing. Product media background is now `#FFFFFF`. Do not use flood-fill background replacement on these white equipment images unless manual masks are created first.

## Product Media Background Matched To Source Images - 2026-06-25

The product-card media background now uses sampled source-image background color `#EEECE8` for product images 01-07, while product 08 keeps a white media override. Product images themselves remain original-white and should not be background-tinted or flood-filled.

## Product 08 Media Background Unification - 2026-06-25

Removed the inline white background override from product 08's `.product-media`, so it now uses shared `#EEECE8`. The image itself remains original-white; internal white source-image background is still present unless product 08 is manually masked or carefully recolored.

## Product 08 Internal Background Match - 2026-06-25

`product-blended-08.webp` was regenerated by replacing near-pure-white internal background pixels with `#EEECE8`, matching the product media surface. This step touched only product 08 and did not batch-process the other product images.

## Scenario Card Height + Image Swap - 2026-06-25

The `Which Home Setup Sounds Closest to Yours?` cards now follow the 12K vs 18K reference section sizing: fixed 216px image height, smaller centered text block, 15px bold scenario titles, and 18px grid gap. Scenario images are loaded from the four user-provided project-root `.webp` files rather than the older `assets/home-situations-*.webp` files.

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
