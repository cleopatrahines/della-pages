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

The local demo uses static prices checked on 2026-05-26:

- 12K ceiling cassette: `$1,394.96`
- 18K ceiling cassette: `$1,784.96`
- 18K dual-zone ceiling cassette: `$2,769.96`
- 27K tri-zone ceiling cassette: `$3,779.96`
- 12K wall mount: `$799.96`
- 18K wall mount: `$1,049.96`
- 18K dual-zone wall mount: `$2,039.96`
- 28K tri-zone wall mount: `$2,484.96`

Before Shopify publish, re-check current PDP pricing or replace the static product cards with Shopify dynamic product data.

## Tracking

Recommended events:

- `cta_click_collection_wall_mount`
- `cta_click_collection_ceiling_cassette`
- `product_click_wall_mount`
- `product_click_ceiling_cassette`
- `faq_expand`
- `support_link_click`

## QA Before Publish

- Check all product links and collection links.
- Confirm old blog redirect is active.
- Confirm mobile CTAs are visible and tappable.
- Confirm no sale-specific copy remains.
- Confirm product prices are current.
- Confirm images have meaningful alt text.
- Confirm page title and meta description are set in Shopify.
