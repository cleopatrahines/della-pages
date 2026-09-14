# Shopify Handoff

## Production URL

Use `/pages/ceiling-cassette-vs-wall-mount-mini-split`.

## Redirect

After the new page is live, redirect the existing blog article to the new page:

`/blogs/della-blog/mini-split-ceiling-cassette-vs-wall-mount-for-your-home`

Target:

`/pages/ceiling-cassette-vs-wall-mount-mini-split`

Use a 301 redirect so the old article does not keep competing for the same query intent.

## Canonical

Set canonical to:

`https://dellahome.com/pages/ceiling-cassette-vs-wall-mount-mini-split`

## Product Data

The local demo does not hard-code prices. Product CTAs use `See Current Price` or `View Product` so the evergreen page does not become stale when PDP pricing changes.

For Shopify publish, either keep this CTA pattern or replace the popular pick cards with dynamic Shopify product data.

## Tracking

Recommended events:

- `cta_click_collection_wall_mount`
- `cta_click_collection_ceiling_cassette`
- `product_click_wall_mount`
- `product_click_ceiling_cassette`
- `decision_checker_answer`
- `decision_checker_result`
- `faq_expand`
- `support_link_click`

## QA Before Publish

- Check all product links and collection links.
- Confirm old blog redirect is active.
- Confirm mobile CTAs are visible and tappable.
- Confirm no sale-specific copy remains.
- Confirm no static price copy or demo pricing note remains.
- Confirm images have meaningful alt text.
- Confirm page title and meta description are set in Shopify.

## Product-card reuse — 2026-09-14

Owner authorized continuing the single-page rollout. Current implementation preserves eight products, their original PDP and Add to Cart variant IDs, the four project sets, checker logic, hero, comparison, room scenes, services and FAQ. Cards display installation style, short series/title, capacity or indoor combination, separate outdoor capacity, voltage, efficiency, coverage, full-name disclosure and the selected variant price. Two single-zone cassette cart variants have no line set; cards label that configuration and link to the original PDP for line-set selection. Vario 12K price is updated to the verified $779.96. Source evidence: commerce-product-data.json.

Desktop uses four columns from 1200px, medium screens two, and mobile through 780px one card with full-width specifications, disclosure and purchase. Static default cards and dynamic project renders match. Arrow keys/Home/End operate the project tabs. Local Chrome verification: 56/56 checks across four groups at 1440/1280/1199/1024/800/780/430/390/360px, product text at 200% on 390/1024px, model disclosure, original checker, comparison toggle, no-JS initial cards, images, metadata/schema preservation and script errors. Cart destinations were inspected without adding items.

Evidence and backup: C:/Users/18041/Documents/Playground/della-ui-review-20260911/cassette-wall-pilot-20260914/. Prices are dated snapshots; shared hydration and Shopify-theme integration remain separate. Local review is ready; this revision has not been committed or pushed. Next action: visual review and explicit publication instruction, then the next single page.