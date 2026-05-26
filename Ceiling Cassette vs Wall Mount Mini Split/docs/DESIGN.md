# Design Notes

## Visual Source

Use the Della Memorial Day PageFly visual system as the brand source:
- Spectral for headings and prices.
- Poppins for body, buttons, labels, tabs, and product-card details.
- Navy `#0E1953` for headings and high-confidence CTA areas.
- Blue `#5884E7` for commerce emphasis and active states.
- Light blue surfaces for decision, support, and trust modules.

Use the existing `single-zone-vs-multi-zone-mini-split.html` page for comparison-page layout grammar and product card behavior, but not as a hard copy.

## Direction

The page should feel like a DTC ecommerce decision page, not a blog article. It should answer the comparison quickly, then provide enough installation and product guidance to move the shopper into a collection or PDP.

## Page Structure

1. Hero: one-sentence verdict, two collection CTAs, product-form comparison visual.
2. Quick decision strip: who should choose each indoor unit type.
3. Comparison table: appearance, installation, airflow, maintenance, cost, best spaces.
4. Room scenarios: bedroom, open living area, finished basement, remodel.
5. Product merchandising: ceiling cassette cards and wall mount cards.
6. Installation fit notes: ceiling clearance, attic/joist access, wall space, drain line.
7. Trust/support strip: free shipping, installer finder, support, warranty/rebate links.
8. FAQ and final CTA.

## Product Cards

Follow the existing local comparison page card pattern:
- image
- product name
- compact spec tags
- price
- `View Product` button

Show current transaction price only. Do not show compare-at price, coupon code, or sale badges.

## Responsive Rules

- Desktop product grid: four cards per row.
- Mobile product grid: two cards per row when text still fits.
- CTAs must stay at least 44px tall.
- No horizontal scroll.
- Text should not overlap imagery or buttons.
