# PLAN: Della DIY Mini Split Installation Guide Implementation

Last updated: 2026-05-29  
Project folder: `C:\Users\18041\Desktop\della-pages\DIY Mini Split Installation Guide`  
Final HTML after approval: `diy-mini-split-installation-guide.html`  
Do not implement HTML until `PRD.md`, `DESIGN.md`, and this plan are accepted.

## 1. Objective

Recreate the approved design draft as a standalone static Shopify-ready HTML page while preserving PRD-controlled content, URLs, CTA labels, safety boundaries, product rules, schema rules, and non-goals.

Source hierarchy:

1. `PRD.md` controls product names, URLs, CTA labels, safety wording, section order, product-card rules, SEO, schema, and non-goals.
2. `Design draft.png` controls layout rhythm, hierarchy, visual direction, and section feel.
3. `DESIGN.md` controls mockup interpretation and required corrections.
4. `mini-split-size-guide.html` controls implementation style reference only.

## 2. Files To Create Or Update

Create:

- `diy-mini-split-installation-guide.html`

Create only if needed:

- `implementation-notes.md` for asset gaps, image source uncertainty, or later price-capture notes.

Do not create:

- duplicate `index.html`
- global theme files
- temporary export artifacts in the project root

Required:

- Create `implementation-notes.md` when implementation starts. Record image sources, asset gaps, no-price decision, schema decision, no-policy-claim decision, and installation safety guardrails.

## 3. Final Section Order

Implement in this order:

1. Slim benefit strip
2. Hero
3. Choose your installation path
4. DIY boundaries / decision band
5. Install steps at a glance
6. Tools & parts checklist
7. Before checkout checklist split panel
8. Shop the installation essentials
9. Match the system to the install complexity
10. Install help hub
11. FAQ
12. Bottom CTA

Do not add global Shopify header/footer/navigation.

## 4. HTML And CSS Approach

Build a standalone static HTML page for Shopify custom page use:

- Use one outer wrapper: `.diy-install-guide-page`.
- Scope all CSS under the wrapper or use low-leak selectors.
- Use inline CSS and minimal inline JS unless implementation requires otherwise.
- Load local fonts using the same pattern as `mini-split-size-guide.html` if font files are available or copied into the project.
- Use semantic sections, one H1, logical H2/H3 hierarchy.
- Use anchor links for hero/path CTAs and approved external URLs for product/support paths.

Implementation reference from `mini-split-size-guide.html`:

- font-face loading style
- container widths
- section spacing
- card radius/border/padding
- button dimensions and focus states
- FAQ `details/summary`
- mobile breakpoints

Do not copy BTU-specific structure, copy, products, or JS.

## 5. Color And Visual Rules

Correct the mockup's blue-heavy balance:

- Primary brand/authority color: `#0E1953`.
- Secondary accent: `#5884E7`.
- Hover/accent: `#6B95EF`.
- Soft panels: `#EDF2FF`, `#F4F7FF`, `#DDF7FF`.

Use navy for:

- main headings
- primary CTAs
- product/card titles
- key icons
- bottom CTA
- authority moments

Use blue for:

- hover states
- text links
- cue chips
- subtle icon accents
- secondary borders

Avoid a bright-blue SaaS look.

## 6. Asset Plan

Inputs:

- Approved design mockup: `Design draft.png`
- Stock folder: `Stock image`
- Della live/CDN images where needed

Implementation steps:

1. Inspect available stock images before choosing final image mappings.
2. Use local stock images when they clearly match hero, checklist, product/category, or support roles.
3. For PDP cards, use approved Della live/CDN product imagery or matching user-provided product assets.
4. If exact image identity is uncertain, record the issue in `implementation-notes.md` and use the closest approved Della/category visual.

Rules:

- Do not use AI mockup product crops as product data.
- Do not invent product imagery or specs.
- No prices in V1.
- Short natural alt text.

## 7. CTA And Link Plan

Use PRD-approved URLs only:

- Mini Split AC: `https://dellahome.com/pages/mini-split-ac`
- Wall-Mounted Mini Splits: `https://dellahome.com/collections/wall-mounted-mini-split`
- Accessories: `https://dellahome.com/collections/accessories`
- DELLA Rental Install Kit: `https://dellahome.com/products/della-diy-install-kit-rental-for-air-conditioners-hvac`
- DELLA Mini Split Line Set: `https://dellahome.com/products/della-mini-split-line-set`
- Find Partner HVAC Installer: `https://dellahome.com/pages/find-a-installer`
- Product Video Center / Installation Videos: `https://dellahome.com/pages/product-video-center`
- Manuals & Troubleshooting: `https://support.dellahome.com/hc/en-us/categories/39323161385883-User-Manuals-Troubleshoot`
- Contact Support: `https://dellahome.com/pages/contact`

CTA labels:

- Start the Install Checklist
- Shop Installation Essentials
- Shop Mini Split Systems
- Shop Wall-Mounted
- View Rental Kit
- View Line Set
- Shop Accessories
- Shop Options
- Watch Videos
- View Manuals
- Find Installer
- Contact Support

All external links use `target="_blank" rel="noopener"` unless the project later chooses same-tab behavior.

## 8. Product Card Rules

Product cards:

- Rental Install Kit
- Mini Split Line Set
- Installation Accessories

Optional visual-balance card:

- Need the system first?
  - This is a path/support card, not a product card.
  - It may link to Mini Split AC and/or Wall-Mounted Mini Splits.

Rules:

- No prices.
- No `Add To Cart`.
- No ratings/review counts.
- No fake discount, sale badge, coupon, countdown, warranty claim, or policy claim.
- Use PRD-approved route identity.
- Product cards are low-pressure next-step cards.
- Do not include Wall-Mounted Mini Splits or Mini Split AC as product cards inside `Shop the installation essentials`.
- Mini split systems can still appear in Hero, Early Path Selector, Match The System To The Install Complexity, and Bottom CTA.

## 9. Safety Copy Plan

Use cautious wording around:

- refrigerant
- vacuum/leak checks
- electrical
- permits/HOA/local code
- warranty
- final commissioning
- exact model manual requirements

Do not include:

- detailed refrigerant charging steps
- detailed electrical wiring steps
- legal/code guarantees
- warranty guarantees
- "anyone can install without a pro" claims

The high-level steps module is an overview/checklist, not a technical HowTo.

## 10. Schema Plan

- Do not add HowTo schema.
- FAQPage JSON-LD may be added only if final visible FAQ text is stable and matches exactly.
- No Product schema in V1.
- No canonical unless final Shopify URL is confirmed.

## 11. Responsive Plan

Test and tune:

- desktop around 1440px
- tablet around 768px
- mobile around 390px
- large mobile around 430px if path cards or CTA text are risky

Responsive rules:

- No horizontal page overflow.
- No clipped CTA text.
- No overlapping hero elements.
- Path cards may become horizontal scroll/snap on mobile.
- Checklists and cards stack cleanly.
- Product/collection cards can become one column on narrow mobile if two columns become cramped.
- Reduce nonessential hero chips on mobile if they crowd text.

## 12. QA Checklist

Before reporting completion:

- Exactly one H1.
- No header/footer/nav/search/cart/account/newsletter/payment icons.
- Navy-first color hierarchy corrected.
- `#5884E7` not overused as primary.
- No prices.
- No `Add To Cart`.
- No fake sale/coupon/countdown/rating/review elements.
- No unsafe install claims.
- No HowTo schema.
- Product/support links use PRD-approved URLs.
- External links include `target="_blank" rel="noopener"`.
- FAQ accordion works.
- FAQ JSON-LD, if present, matches visible FAQ exactly.
- Desktop/tablet/mobile checked.
- No horizontal overflow.
- No clipped text or overlapped UI.
- No AI placeholder text remains.
- Asset gaps recorded in `implementation-notes.md` if any.
- Final HTML exists at `C:\Users\18041\Desktop\della-pages\DIY Mini Split Installation Guide\diy-mini-split-installation-guide.html`.
- Pause after HTML and QA for user review.
- Do not commit or push until user approves.

## 13. Stop Conditions

Stop and ask before implementation or report a blocker if:

- a required product image cannot be mapped confidently and no acceptable category visual exists
- the design mockup conflicts with PRD safety/product rules in a way not covered by `DESIGN.md`
- the user requests prices, warranty claims, financing, or policy claims without verified source data
- the final Shopify canonical URL becomes required before HTML completion
