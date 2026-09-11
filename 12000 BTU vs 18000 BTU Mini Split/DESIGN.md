# DESIGN.md - 12000 BTU vs 18000 BTU Mini Split

## Approved residence hero — 2026-09-11

Owner-selected visual: `exec-0443fb86-1b15-45cd-b2ad-230727a43687.png`. The hero uses a contemporary residence with limestone, walnut, sculptural ivory seating and a wall-mounted mini split. White HTML heading and actions overlay the dark left side on desktop; mobile presents the right-hand room crop above a navy text/action area.

H1 wording and both fragment destinations remain unchanged. Subtitle: “Find the right capacity for your room, before you shop.” The rest of the page retains its existing layout and markup.

Asset: `assets/hero-luxury-residence.webp`, generated from the approved mockup as a text-free background (`exec-480abd41-3120-4181-9a47-b2c7874c07a0.png`) and converted to WebP. The room/device is illustrative; product specifications remain in the product cards.

QA: 45 checks passed across 1440, 1280, 1024, 768, 430, 390 and 360px, including asset loading, overflow, both hero anchors and keyboard flow, five factor tabs, eight product URLs, expandable model names, FAQ and no-JavaScript behavior. Desktop/mobile screenshots reviewed. Evidence and backups: `C:\Users\18041\Documents\Playground\della-ui-review-20260911\luxury-hero`. This hero revision has not been committed or published.

## Commerce refinement — 2026-09-11

- Hero retains its image, H1 wording and decision/shopping paths. Balanced heading wrapping, revised type size and image/text proportions keep the headline together.
- Two independent product groups retain their original four product destinations each. Cards reuse the Bedroom hierarchy: short series title, actual capacity, aligned Efficiency/Coverage/Voltage rows, expandable full model name, price and View Product button. Mobile uses image/title above full-width specs and purchase controls.
- Product titles, voltages and price ranges were checked against public Shopify product JSON. Optima's original URL redirects on the official site to Optima CloudAir; its displayed title/image follow that destination. Its base option excludes the line set, which is called out visibly. Serena CloudAir 12K shows both 115V and 230V; products with differing variant prices show From.
- Service icons/text form a compact strip. Existing promises link to shipping, installments, contact and warranty pages; policy text remains as supplied.
- FAQ keeps native disclosure behavior with generous click targets and revised spacing. The final collection area is one compact section with two equally weighted buttons.
- Previously approved illustrated sections, airflow artwork, factor tabs, anchor destinations and the 1180px container alignment remain intact.
- Visual reference review: Della coupon page and Bedroom card conventions are primary; Insta360, EcoFlow, Govee, Anker and Dreame supplied examples of product emphasis, compact service information and restrained detail presentation. Insta360 redirected to the China storefront; no regional product facts were copied.
- QA: 45 checks passed at 1440, 1280, 1024, 768, 430, 390 and 360px. Includes overflow, five factor tabs and keyboard navigation, original eight product URLs, four products per group, visible voltage, full-name keyboard expansion, service/image loading, FAQ, two final buttons and no-JavaScript reading.
- Evidence and pre-edit backups: `C:\Users\18041\Documents\Playground\della-ui-review-20260911\commerce-refinement`.
- Product data is a timestamped snapshot. Shopify theme integration, screen-reader testing and conversion impact are not verified. No commit or publication is requested.

## Resolved Decisions — 2026-09-11

All three illustrated modules use the same container as the products: maximum 1180px, 20px desktop/tablet gutters and 14px mobile gutters. The room panorama, blue capacity band, factor layout and navy banner share identical outer edges. Verified at seven widths (360–1440px).

Approved visual target: `C:\Users\18041\.codex\generated_images\01a08f7c-0b7f-7bc2-91fc-5cf47de38e45\exec-2910a291-f6e0-4c39-998d-abcb6ca89f09.png`.

- The capacity section uses one architectural room panorama above a light-blue comparison band with equal 12K/18K actions, area references and conditional room guidance. Both actions jump to the corresponding product group.
- The factors section places a room-detail photograph beside five tabs: Sun, Layout, Insulation, Ceiling and Heat load. Each tab changes its explanation and the matching spatial annotation. Room area is covered with connected layout. Sun is initially active.
- Tabs expose tab/tablist/tabpanel semantics with arrow, Home and End navigation. Without JavaScript, all explanations are visible and inactive controls are hidden.
- Right-sizing guidance uses a navy living-room background with the owner-requested blue airflow effect and a white button leading to products. On narrow mobile, the scene sits above the copy and button.
- Scene images are generated illustrations, not evidence of installed capacity or model specifications. Original product cards and their data remain unchanged.
- Current order: hero, capacity comparison, sizing factors, right-sizing banner, products, services, FAQ, bottom collections. Mobile product-stage shopping bar remains available.
- Implementation follows the approved combined visual direction. Site publishing and shared-component rollout are not requested.


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

