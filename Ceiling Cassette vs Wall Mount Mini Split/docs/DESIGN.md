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
2. Hero: full-bleed lifestyle banner, concise verdict, two collection CTAs.
3. Path panel: overlay commerce navigation for Ceiling Cassette, Wall Mount, Compare Fit, and Find Installer.
4. Quick answer: two path cards, one for ceiling cassette and one for wall mount.
5. Decision checker: five install-fit questions with a recommended starting path.
6. Head-to-head comparison: compact 8-row comparison with stacked mobile cards.
7. Choose by room: lifestyle scene cards for open living, bedroom/office/rental, sunroom, retrofit, and remodel.
8. Installation feasibility: installer checks for both indoor unit types.
9. Product path: two collection cards followed by popular comparison picks.
10. Mix indoor unit styles, services, FAQ, and bottom CTA.

## Product Cards

Use product merchandising as a decision path instead of a sale grid:
- two collection path cards first
- popular side-by-side picks after the collection decision
- image
- product name
- compact spec tags
- system type and best-fit use case
- `See Current Price` or `View Product` button

Do not show demo pricing notes, compare-at price, coupon code, or sale badges. If Shopify dynamic product data is not wired, use `See Current Price` as the PDP CTA.

## Responsive Rules

- Desktop product grid: four cards per row.
- Mobile comparison picks: one card group per row; paired product options stack inside the group when needed.
- CTAs must stay at least 44px tall.
- No horizontal scroll.
- Text should not overlap imagery or buttons.

## Product-card reuse — 2026-09-14

Owner authorized continuing the single-page rollout. Current implementation preserves eight products, their original PDP and Add to Cart variant IDs, the four project sets, checker logic, hero, comparison, room scenes, services and FAQ. Cards display installation style, short series/title, capacity or indoor combination, separate outdoor capacity, voltage, efficiency, coverage, full-name disclosure and the selected variant price. Two single-zone cassette cart variants have no line set; cards label that configuration and link to the original PDP for line-set selection. Vario 12K price is updated to the verified $779.96. Source evidence: commerce-product-data.json.

Desktop uses four columns from 1200px, medium screens two, and mobile through 780px one card with full-width specifications, disclosure and purchase. Static default cards and dynamic project renders match. Arrow keys/Home/End operate the project tabs. Local Chrome verification: 56/56 checks across four groups at 1440/1280/1199/1024/800/780/430/390/360px, product text at 200% on 390/1024px, model disclosure, original checker, comparison toggle, no-JS initial cards, images, metadata/schema preservation and script errors. Cart destinations were inspected without adding items.

Evidence and backup: C:/Users/18041/Documents/Playground/della-ui-review-20260911/cassette-wall-pilot-20260914/. Prices are dated snapshots; shared hydration and Shopify-theme integration remain separate. Local review is ready; this revision has not been committed or pushed. Next action: visual review and explicit publication instruction, then the next single page.