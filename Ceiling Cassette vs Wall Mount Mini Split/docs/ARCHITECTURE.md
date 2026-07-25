# Architecture

## Page Model

The page is a standalone static artifact:

- One HTML file contains metadata, styles, content, and minimal JavaScript.
- Local fonts and images are stored in `assets/`.
- External links point to Shopify collections, PDPs, and Della support pages.

## Content Flow

The page moves from fast decision to evidence to product action:

1. Full-bleed verdict hero
2. Overlay commerce path selection
3. Two-path quick answer
4. Five-question decision checker
5. Compact head-to-head comparison
6. Lifestyle room-fit scenarios
7. Installation feasibility checks
8. Collection-first product path and popular picks
9. Mixed indoor unit guidance
10. Services, FAQ, and final CTA

## Shopify Migration

The standalone HTML is intended as a pre-Shopify demo. For production Shopify, product cards should ideally be replaced by collection/product blocks or Liquid-driven product data.
