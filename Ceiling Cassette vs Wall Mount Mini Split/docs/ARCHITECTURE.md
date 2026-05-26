# Architecture

## Page Model

The page is a standalone static artifact:

- One HTML file contains metadata, styles, content, and minimal JavaScript.
- Local fonts and images are stored in `assets/`.
- External links point to Shopify collections, PDPs, and Della support pages.

## Content Flow

The page moves from fast decision to evidence to product action:

1. Verdict
2. Commerce path selection
3. Quick answer
4. Comparison details
5. Room scenarios
6. Product tabs
7. Installation and value
8. Support/trust
9. FAQ/final CTA

## Shopify Migration

The standalone HTML is intended as a pre-Shopify demo. For production Shopify, product cards should ideally be replaced by collection/product blocks or Liquid-driven product data.
