# Whole House — release acceptance

Verified 2026-09-15 against the final static HTML.

## Scope
Hero and benefit strip; annotated house layout; 45-product catalogue with zone/type filters; room sizing; three FAQs and closing collection CTA. Six H2 elements use 32px Spectral, weight 400. Latest owner-approved spacing, navy text links and button interactions are retained.

## Verification
- 45 official product JSON records: title, variant ID, SKU, price and availability match products.json. Selected variants are the PDP defaults.
- All 45 actual product URLs and all seven collection/tool destinations return HTTP 200.
- 45 displayed efficiency and voltage values checked against the official PDP specification fields. The catalogue preserves SEER versus SEER2 as labelled in those fields.
- 24 combinations of zone/type filters: expected counts, persistent format selection, reset and correct zone collection URL.
- Real mouse, keyboard radio navigation, touch controls, FAQs, cutaway markers, hover and reduced-motion behavior pass.
- Seven viewport widths: 1440, 1280, 1024, 768, 430, 390 and 360px; no page-level horizontal overflow.
- 48 images decode, local fonts load, one H1, six consistent H2s, no broken page anchors, no page script errors.
- No-JavaScript view exposes all 45 products and native FAQ disclosures.
- Product image delivery uses lossless WebP; three scene images use quality-90 WebP. Total referenced image size falls from 32.31MB to 15.69MB. Original images remain in the local project.

## Copy review
The page answers whole-home feasibility with conditions, explains closed-room distribution and room-by-room sizing, and routes visitors to actual systems. It avoids guaranteed whole-house coverage, universal heating claims, invented savings and unsupported installation quotes. No additional section or broad rewrite was needed. Existing owner-approved copy and removed footnotes remain as requested.

## Operating limits
Prices and availability are a verified static snapshot, not a live Shopify feed. Refresh products.json and regenerate cards before subsequent campaigns or after catalogue changes. Illustrations are conceptual, not an equipment design or installation record. This GitHub Pages release does not install the page in the DELLA Shopify theme or configure ad analytics.

## Regeneration
Run `python build_product_cards.py` from the project. Product facts and image paths are maintained in products.json. Preserve the release image paths when rebuilding.
