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

1. Announcement strip: Della trust points.
2. Hero: comparison visual, concise verdict, two collection CTAs.
3. Path panel: install-type commerce navigation.
4. Quick answer: product image plus short decision guidance.
5. Setup summary and comparison table: the core SEO answer.
6. Room scene rows: four real residential install situations.
7. Product merchandising: two tabs, ceiling cassette and wall mount.
8. Installation and value: cost path and install complexity.
9. Trust/support strip: shipping, financing, live chat, installer path.
10. FAQ and bottom CTA.

## Product Cards

Follow the existing local comparison page card pattern:
- image
- product name
- compact spec tags
- price
- `View Product` button

Show current transaction price only. Do not show compare-at price, coupon code, or sale badges. Use two product tabs instead of two stacked product blocks so the page feels more like a DTC commerce landing page.

## Responsive Rules

- Desktop product grid: four cards per row.
- Mobile product grid: two cards per row when text still fits.
- CTAs must stay at least 44px tall.
- No horizontal scroll.
- Text should not overlap imagery or buttons.
