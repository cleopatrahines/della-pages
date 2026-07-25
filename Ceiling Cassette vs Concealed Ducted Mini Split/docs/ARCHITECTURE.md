# Architecture

## Current State

The project has completed a blocked Step 5 acceptance run. The current static preview has shared namespaced CSS/JavaScript, final local visual assets, and current QA evidence. Shopify Liquid and JSON markup do not exist yet. Step 6 remains gated until the required browser recheck and named HVAC/product diagram review are resolved or explicitly accepted.

## System Boundaries

### Landing Page Body

Owns the nine approved sections, content hierarchy, product tabs, FAQ presentation, CTA paths, conceptual diagrams, and page-specific styles and behavior.

### Static Preview Boundary

- Renders the Landing Page Body alone.
- Uses static Preview Prices captured on a recorded date.
- Uses relative local assets and approved Della CDN product images.
- Does not reproduce Storefront Chrome.

### Shopify Production Boundary

- Renders the same Landing Page Body once inside a dedicated Liquid section.
- Resolves the eight approved products and dynamic Production Prices.
- Is mounted once by `templates/page.ceiling-cassette-vs-concealed-ducted.json`.
- Relies on the active theme for Storefront Chrome, money formatting context, page SEO fields, and canonical output.

## Planned File Responsibilities

| File | Responsibility |
| --- | --- |
| `ceiling-cassette-vs-concealed-ducted-mini-split.html` | Static review body and static prices |
| `assets/della-hidden-mini-split-comparison.css` | Namespaced tokens, layouts, components, responsive behavior, local font faces, and reduced-motion handling |
| `assets/della-hidden-mini-split-comparison.js` | Accessible product-tab state, keyboard behavior, progressive enhancement, and Shopify section-reload initialization |
| `sections/ceiling-cassette-vs-concealed-ducted-mini-split.liquid` | Shopify body and dynamic product-price rendering |
| `templates/page.ceiling-cassette-vs-concealed-ducted.json` | Mounts the section once |
| `assets/della-*.woff2` | Flat runtime font assets usable by preview CSS and Shopify theme assets |
| `assets/della-service-*.png` | Flat runtime Premium Della Services icons |
| `assets/della-project-*.webp` | Approved flat runtime project-scene assets |
| `assets/fonts/` and `assets/images/services/` | Step 1 source archive for localized originals |
| `implementation-notes.md` | Data snapshots, source evidence, asset status, and handoff risks |

## Data Flow

### Preview

Official Shopify product JSON at capture time -> verified snapshot record -> static price and availability in preview product cards.

### Production

Approved product handle -> Shopify product object -> availability and price state -> Liquid money formatting -> product card.

Static product identity and approved image choice remain governed by PRD. Live Shopify data may detect drift but must not silently substitute a product.

## Interaction Flow

- Product tabs expose one Recommended Product Set at a time.
- Default state is Ceiling Cassette unless an approved earlier in-page selection establishes a preference.
- FAQ uses native disclosure controls and starts collapsed.
- Links remain usable without JavaScript.
- Stable data attributes identify CTA location and destination without inventing analytics event names.

## External Contracts

- Della product and collection URLs.
- Shopify public product JSON for Step 1 snapshots.
- Shopify product objects and money filters for production.
- Active Della theme Header/Footer, metadata, and canonical behavior.
- Official Della manuals for conceptual planning relationships.
- Official Della coupon page for current service-label verification.

## Asset Boundary

- Mockups and reference screenshots are never embedded or sliced.
- Product images may remain on the official Della CDN.
- Fonts and service icons have flat runtime copies so the same relative CSS paths work in preview and Shopify.
- `della-project-open-concept.webp` and `della-project-finished-basement.webp` are approved reused scenes.
- Hero uses the supplied responsive local banner pair; its foreground copy and CTAs remain HTML.
- New-Construction and Multi-Room-Renovation use supplied local scene images; no placeholder media remains in page markup.
- Installation diagrams use supplied conceptual local images and still require Della product/HVAC review before publication.

## Known Integration Gaps

- The active Shopify theme source and preview environment are not available.
- Existing Della analytics event naming is unknown.
- Final Shopify page URL is not confirmed.
- Final New-Construction and Multi-Room-Renovation scene assets are not yet approved; this blocks visual acceptance, not Step 3 structure work.
