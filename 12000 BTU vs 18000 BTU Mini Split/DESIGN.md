# DESIGN.md - 12000 BTU vs 18000 BTU Mini Split

Status: approved design direction for documentation
Primary visual reference: `C:\Users\18041\Desktop\della-pages\12000 BTU vs 18000 BTU Mini Split\12k vs. 18k Design Drafts.png`
Primary implementation reference: `C:\Users\18041\Desktop\della-pages\single-zone-vs-multi-zone-mini-split\single-zone-vs-multi-zone-mini-split.html`

## Design Goal

Build a Della ecommerce decision page that feels credible, clean, and product-led. The page should look like a Della landing page, not a generic HVAC blog, SaaS comparison page, or AI-generated mockup.

Preserve the design draft's general rhythm while replacing any generic or fake visuals with real Della product imagery and local Della page patterns.

## Design Priorities

1. Make the 12K vs 18K choice visible immediately.
2. Keep collection CTAs more prominent than PDP CTAs.
3. Make sizing guidance easy to scan, not academic.
4. Use product cards that match the existing Della single-zone page style.
5. Keep mobile compact and conversion-focused.
6. Avoid unverified sales, fake calculators, and generic template visuals.

## Brand System

Use Della's existing light ecommerce visual language from the provided files and reference page.

Reference files:

- `C:\Users\18041\Desktop\della-pages\page.pf-ef33e2e6.json.txt`
- `C:\Users\18041\Desktop\della-pages\pf-ef33e2e6.liquid.txt`
- `C:\Users\18041\Desktop\della-pages\della-memorial-day-design-system.md`
- `https://dellahome.com/pages/coupon-code`
- `C:\Users\18041\Desktop\della-pages\single-zone-vs-multi-zone-mini-split\single-zone-vs-multi-zone-mini-split.html`

Typography:

- Serif headings/product titles: Spectral first, Georgia fallback.
- Body, buttons, tabs, and utility labels: Poppins first, Arial fallback.
- Do not use viewport-based font scaling.
- Letter spacing should be 0 unless a local Della reference already uses a small label treatment.

Color direction:

- Primary navy: `#0E1953`
- Della blue: `#5884E7`
- Della blue hover: `#6B95EF`
- Light blue surface: `#EDF2FF`
- Secondary light surface: `#F4F7FF`
- Cyan-light accent: `#DDF7FF`
- White cards with subtle blue-gray borders

Buttons:

- Use squared Della buttons with about 4 px radius.
- No pill buttons.
- No glassmorphism.
- No gradient CTA buttons unless already present in exact copied reference blocks.
- Primary CTA should feel solid and high-contrast.

Avoid:

- Dark SaaS hero cards
- Purple-blue gradient landing-page look
- Decorative orbs or bokeh backgrounds
- Fake AI lifestyle/product composites
- Overly rounded cards
- Nested cards
- Marketing hero with generic stock imagery

## Layout Rules

Use a centered content wrapper consistent with the single-zone page. Maintain generous but practical whitespace. Avoid oversized hero text that pushes the comparison visual below the first viewport on desktop.

Cards should use small radii and clean borders. Product cards should match the existing Della product-grid feeling shown in the single-zone reference page.

Responsive behavior:

- Desktop: two-column hero, two-column decision cards, multi-column product grid.
- Tablet: hero can stack if needed; product grid can move to 2 columns.
- Mobile: single-column sections, tight spacing, sticky bottom CTA, no horizontal scroll.

## Section Design Notes

### Hero

Visual concept:

- Light blue Della ecommerce banner background.
- Left side: H1, short shopper-friendly copy, two CTAs.
- Right side: real product comparison visual using locked product images.
- The 12K and 18K products should feel balanced, not like one is the obvious winner.

Hero image implementation:

- Use real Della product images from the locked product manifest.
- Use DELLA Optima Series 12000 BTU 24 SEER2 Ultra Heat Mini Split AC as the hero 12K representative image.
- Use DELLA Serena Series 18000 BTU 22 SEER2 Mini Split Heat Pump AC as the hero 18K representative image.
- Arrange the two real product images side by side with `12K` and `18K` labels.
- Do not generate new product images.
- Do not use the full Shopify navigation or a copied site header.

CTA order:

1. `Shop 12000 BTU Mini Splits`
2. `Shop 18000 BTU Mini Splits`

No third CTA in hero.

### Choose 12K / Choose 18K

Use two strong side-by-side cards. Each card should feel like a clear path, not a dense checklist.

Each card has exactly five bullets. Small check/icon treatments are acceptable if they match Della's visual system.

### Light Sizing Note

Use one compact text band below the choose cards. It should be noticeable but not a warning banner. No chips, calculator fields, or long disclaimer block.

### Sizing Factors

Use six cards in a clean grid. The design draft's card rhythm can be followed, but copy must use the PRD-approved conservative wording.

Each card includes:

- Factor title
- One-sentence explanation
- One small tendency label at the bottom

The labels should be visually secondary. They guide direction without pretending to calculate the answer.

### Comparison Table

Keep the table simple and readable. It compares buying-path logic, not technical product data.

Rules:

- Six rows only.
- Two main value columns: 12000 BTU and 18000 BTU.
- No price, SEER2, exact model, SKU, or product image in this table.
- On mobile, convert the comparison table into stacked comparison cards instead of horizontal scroll.
- CTA buttons below the table route to the two collections.

### Bigger Is Not Always Better

This module should be short, high-contrast, and visual.

Left:

- Heading
- Required short copy
- `Learn About Sizing` anchor back to sizing factors

Right:

- Two side-by-side mini panels: `Right-sized comfort` and `Oversized system risk`
- Use check or simple list styling.
- Do not make the oversized panel look like an attack on 18K products.

### Product Groups

Do not use tabs. Use two visible stacked groups for SEO and scanability.

Product card design should follow the single-zone reference:

- Large product image area
- Serif product title
- Compact spec chips
- Bold price
- Solid navy `View Product` button
- Clean border, white background

Each group has a collection CTA on the right side of the heading row on desktop, and near the bottom or stacked under copy on mobile.

Spec chips:

- Use actual specs only.
- Preferred order: BTU, SEER2, coverage.
- Optional fourth chip only when verified, such as Ultra Heat, Cloud Air, or Heat Pump.
- Do not invent coverage chips.
- Use front-end coverage chip labels exactly as `Up to 550 sq. ft.` and `Up to 1,000 sq. ft.` when verified.
- Keep chips visually separate; do not concatenate BTU, SEER2, coverage, and Heat Pump into a single chip.

Price display:

- Show live selling price only.
- Do not show compare-at price.
- Do not show sale badges, coupons, or discount labels.

### Room Scenarios

Use four scenario cards with real lifestyle images.

Visual approach:

- Image on top or left, compact text below or beside depending on viewport.
- Each card includes scenario name and one direction label.
- Do not expand beyond four cards in this version.

Image source rule:

- Use Della-owned/local page images where possible.
- If the exact scene does not exist, use the closest credible Della lifestyle image from existing local pages.
- Do not use fake AI scenes.

### Premium Della Services

Copy this section directly from the single-zone reference page:

`C:\Users\18041\Desktop\della-pages\single-zone-vs-multi-zone-mini-split\single-zone-vs-multi-zone-mini-split.html`

Do not rewrite the first implementation pass.

Must preserve:

- Section label: `Service confidence`
- Heading: `Premium Della Services`
- Four-card layout
- Card titles
- Icon URLs
- Responsive behavior

The copied service cards are:

- `Free & Fast Shipping`
- `Pay in 6 Months, 0% APR`
- `24x7 Live Chat Support`
- `Lifetime Coverage (Mini Splits)`

### FAQ

Use compact accordions or a clean FAQ stack consistent with the Della page style. Keep FAQ text direct and conservative.

Use the exact five FAQ questions and short answers from `PRD.md`. Do not let implementation rewrite the FAQ answers freely.

Do not add FAQ schema.

### Bottom CTA

Use two collection cards. This should feel like a final path decision, not a long closing essay.

Card copy:

- 12K: `For bedrooms, offices, and smaller enclosed rooms.`
- 18K: `For larger rooms, open layouts, garages, and sunrooms.`

No extra global note under the cards.

### Mobile Sticky CTA

Show only on mobile.

- Fixed to bottom.
- Height 56 to 64 px.
- Buttons: `Shop 12K` and `Shop 18K`.
- Add bottom padding to the page so content is not covered.
- No close icon, no popup behavior, no promo text.

## Mockup Interpretation Rules

The design draft is a visual guide, not a data source.

Use the mockup for:

- Section rhythm
- Visual hierarchy
- Overall 12K vs 18K decision feel
- Light blue ecommerce direction

Do not use the mockup for:

- Fake prices
- Fake product images
- Unverified product names
- Full nav/header patterns
- Generic claims not approved in the PRD

## Accessibility And UX Requirements

- All images need meaningful alt text.
- Product image alt should include product family and BTU where practical.
- CTA labels must be clear without surrounding context.
- Mobile text must not overflow cards or buttons.
- Sticky CTA must not cover final content.
- Color contrast must be acceptable for buttons, text, and small labels.
- Keyboard focus states should be visible for links and buttons.

## Visual QA Checklist

Before final handoff, verify:

- Desktop hero shows both CTAs and real 12K/18K product visual cleanly.
- Mobile hero stacks without product image overflow.
- Product cards align and prices do not shift layout awkwardly.
- The two product groups are visible without tab interaction.
- Services section visually matches the single-zone reference.
- FAQ accordions, if used, are accessible and do not jump layout unexpectedly.
- Mobile sticky CTA appears only on mobile and does not cover bottom CTA or FAQ.
- No placeholder text, fake images, or unverified promo claims remain.

