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
