# Architecture

## Page Model

The page is a standalone static artifact:

- One HTML file contains metadata, styles, content, and minimal JavaScript.
- Local fonts and images are stored in `assets/`.
- External links point to Shopify collections, PDPs, and Della support pages.

## Content Flow

The page moves from fast decision to evidence to product action:

1. Verdict
2. Fit decision
3. Comparison details
4. Room scenarios
5. Product cards
6. Installation constraints
7. Support/trust
8. FAQ/final CTA

## Shopify Migration

The standalone HTML is intended as a pre-Shopify demo. For production Shopify, product cards should ideally be replaced by collection/product blocks or Liquid-driven product data.
