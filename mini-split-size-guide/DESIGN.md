# DESIGN: Della Mini Split Size Guide

Last updated: 2026-05-28  
Visual reference: `C:\Users\18041\Desktop\della-pages\Mini Split Size Guide\ui设计图.png`  
Scope source of truth: `PRD.md`

## 1. Design Role

This document translates the approved long-page mockup into implementation guidance. The mockup is the visual source for composition, spacing rhythm, section feel, and hierarchy. `PRD.md` remains the source of truth for product data, BTU ranges, SEO, copy constraints, CTA rules, and non-goals.

Do not implement `index.html` from the mockup alone. Reconcile every section against `PRD.md`.

## 2. Visual Direction To Preserve

Preserve these qualities from the mockup:

- Clean Della ecommerce guide feel: navy text, blue actions, white space, light blue surfaces.
- Wide hero with left editorial copy and right product-led lifestyle room image.
- Top one-line trust strip.
- Compact BTU selector cards immediately after hero.
- Semantic sizing table with clear blue header.
- `What Changes Your BTU` as a focused visual + checklist section.
- Lifestyle-driven room match grid with photographic cards.
- Product merchandising tabs with product cards.
- `Right Size` comparison module with three states.
- Installer checklist paired with outdoor unit / install visual.
- Lower service/trust cards and compact FAQ.

The page should feel like a polished Della ecommerce landing page, not a blog article, not a generic AI template, and not a SaaS calculator.

## 3. Required PRD Overrides

These mockup elements must not be copied literally:

- BTU ranges: replace mockup ranges such as `250-450`, `450-650`, `1,400-2,000` with PRD/Della collection ranges.
- Product data: replace mockup placeholder product names such as Breeze, Aura, Cassette, and Floor Console with real products from PRD product tables.
- Product images: use the user-provided Della CDN product image URLs, not cropped/extracted mockup images.
- Product order: final HTML places `Bigger Is Not Always Better` before `Shop Mini Splits by BTU`, even though the mockup shows product tabs first.
- Top strip copy: use PRD copy, not unverified mockup claims like `2-Year Della Warranty`.
- Prices: do not use mockup prices. Capture live product prices during implementation or omit price lines if unreliable.
- CTA labels: PDP cards use `View Product`; collection cards use `Shop 9K` etc.; no `Add To Cart`.

## 4. Section Design Notes

### Top Benefit Strip

Visual:

- Thin navy bar across the top.
- Three evenly spaced trust items.
- Small line icons are acceptable if simple and consistent.

Final copy:

- Free Shipping Sitewide
- Find Partner HVAC Installer
- 24/7 Live Chat Support

Do not use the mockup's `2-Year Della Warranty` unless verified separately.

### Hero

Preserve:

- Left H1 block with short copy and two CTAs.
- Right bright modern American room with visible wall-mounted mini split.
- Small static BTU cue chips near the unit.

Correct:

- H1 should follow PRD: `Mini Split Size Guide: Find the Right BTU for Your Room`.
- Primary CTA: `Find My Starting BTU`.
- Secondary CTA: `Shop by BTU`.
- Cue chips should use PRD-aligned range examples, e.g. `12K BTU`, `401-550 sq ft`, `Bedroom / Office`, `Adjust for sun & insulation`.

Avoid:

- calculator dashboard
- input fields, sliders, forms
- glassmorphism panels
- complex data widgets
- over-layered floating UI

Mobile:

- Preserve H1 and CTAs first.
- Reduce chips to 1-2 or hide secondary chips if the image crowds the copy.

### BTU Selector

Preserve:

- Five clean cards.
- 12K lightly highlighted as default.
- Minimal arrow/link affordance.

Correct ranges:

- 9K: up to about 400 sq ft
- 12K: 401-550 sq ft
- 18K: 551-1,000 sq ft
- 24K: 1,001-1,500 sq ft
- 36K: 1,501-2,500 sq ft

Mobile:

- Horizontal scroll strip with scroll-snap.
- Stable card width around 72-82vw or min-width 230-260px.
- Show a peek of the next card.
- No 2-column mobile grid.

### Sizing Chart

Preserve:

- Blue-tinted table header.
- Compact, scannable rows.
- Last column links to shop path.

Correct:

- Use PRD ranges only.
- Use "starting point" language.
- Avoid guaranteed coverage language.

Mobile:

- Table must remain readable.
- Horizontal overflow is acceptable if styled cleanly.

### Sizing Notes

The mockup uses a house cutaway with numbered notes. This visual logic is good, but implementation can simplify if final assets are not available.

Preferred implementation:

- One focused panel.
- Left: product/room visual or simple home-room illustration.
- Right: checklist notes.
- Mobile: stack visual above notes.

Required notes:

- Insulation
- Sun exposure
- Ceiling height
- Open layout
- Heat load

Avoid five equal icon cards.

### Room Match

Preserve:

- Photographic lifestyle cards.
- Mixed card sizes are acceptable.
- Text overlay should be readable.

Final card logic:

- Bedroom / Office
- Studio / apartment main room
- Garage / Shed
- Open Living Room
- Sunroom / Attic
- Large Open Area

Each card gets:

- scene name
- short description or cue
- suggested BTU range
- lightweight text link

Do not use filled buttons in every card.

### Right Size Module

Move before product tabs in final HTML.

Preserve visual intent:

- Three side-by-side states.
- `Right Size` highlighted.
- Clear comparison of too small, right size, too large.

Content:

- Too Small: runs constantly / struggles on hot days
- Right Size: steadier comfort / better humidity control
- Too Large: short cycling / uneven comfort / poor humidity control

### Product Tabs

Preserve:

- Tab toolbar.
- Product cards in a clean grid.
- White product cards with clear product image, title, bullets/specs, price, CTA.

Correct:

- Default tab: 12K.
- PDP CTA: `View Product`.
- Use PRD product names, URLs, and image URLs.
- Capture live prices before implementation.
- 36K tab has one product plus installer confirmation note.
- No AI placeholder product names.
- No `Add To Cart`, coupon copy, save badges, countdowns, or fake discounts.

### Installer Checklist

Preserve:

- Image + checklist pairing.
- Practical install confidence tone.

Checklist:

- Outdoor unit placement and clearance
- Line-set and drain route
- Electrical panel and breaker
- Indoor wall location and airflow

CTA can include:

- Find Partner HVAC Installer
- Contact Della Support

### Premium Della Services

Reuse the service-card section from `single-zone-vs-multi-zone-mini-split.html`.

Cards:

- Free & Fast Shipping
- Pay in 6 Months, 0% APR
- 24x7 Live Chat Support
- Lifetime Coverage (Mini Splits)

Keep it lower-page and compact.

### FAQ

Keep compact and near the bottom.

Rules:

- Maximum 6 FAQ items.
- 2-4 sentence answers.
- Accordion interaction.
- Include FAQ JSON-LD in final HTML.

## 5. Typography And Color

Use PRD/Della design system:

- H1/H2/H3/product title: Spectral, Georgia, serif.
- Body/buttons/tabs: Poppins, Arial, sans-serif.
- Navy: `#0E1953`.
- Blue: `#5884E7`.
- Blue hover: `#6B95EF`.
- Blue light: `#EDF2FF`.
- Blue surface: `#F4F7FF`.
- Trust background: `#DDF7FF`.
- White and light gray surfaces.

Avoid:

- purple gradients
- beige/brown palettes
- glassmorphism
- heavy shadows
- decorative orbs
- oversized icons

## 6. Responsive Behavior

Desktop:

- 1200px max container.
- 32px side padding.
- 5-card BTU row preferred.
- Product grid 4 columns when data allows.

Tablet:

- BTU selector can use scroll or 3+2.
- Product cards may use 2 columns.

Mobile:

- 16px side padding.
- Hero copy remains primary.
- BTU selector horizontal scroll with snap.
- Product cards 2 columns if text fits; otherwise 1 column is acceptable for readability.
- Tables may horizontally scroll.
- No text overlap.
- Touch targets at least 44px high.

## 7. Assets

V1:

- Product images use provided Della CDN URLs.
- Do not extract product images from the mockup.
- Do not download all product images unless loading fails or an offline demo is required.

Hero/support imagery:

- The mockup's visual direction can be matched with generated or local imagery later.
- If no final hero asset is provided, implementation can use a CSS/HTML composition and Della product image as a placeholder, but should report that the hero asset is pending.

## 8. Visual QA Criteria

Pass criteria:

- The implementation reads as a Della ecommerce guide, not a blog.
- Hero, BTU selector, table, sizing notes, room match, right-size module, product tabs, installer checklist, services, and FAQ are all present.
- PRD override rules are respected.
- Product cards use real PRD product data.
- No calculator UI appears.
- No AI placeholder products or ranges remain.
- Mobile layout has no overlap or unreadable controls.
