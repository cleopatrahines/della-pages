# DESIGN: 2-Zone vs 3-Zone Mini Split

## Source Of Truth

This design handoff is based on:

- `PRD.md`
- `Reference Image for the Design Draft.png`
- Della PageFly / Memorial / coupon-code visual references

The design image controls visual rhythm, spacing, section composition, and ecommerce feel.

The PRD controls content, product data, price rules, CTA behavior, section inclusion/exclusion, FAQ count, SEO, and final implementation rules.

## Overall Visual Direction To Preserve

Preserve the design draft's Della ecommerce landing-page feel:

- Wide product-led hero with pale blue background and strong Della navy typography.
- Left-aligned hero copy and CTAs, with product comparison imagery on the right.
- Compact room-count strip overlapping or sitting directly under the hero.
- Two large quick-answer cards with simple line icons and full-width CTAs.
- Product tabs after the decision cards, using a PageFly-style large category visual plus product card grid.
- Scenario image cards using realistic home spaces.
- Light-blue decision/support surfaces with navy headings.
- Clean comparison table with short cells, light borders, and no winner badge.
- Late-page service cards, compact FAQ, and bottom collection cards.

The page should feel like a Della Shopify commerce page, not a blog post, SaaS dashboard, or generic comparison article.

## Required Mockup Overrides

The design draft contains several items that must not be implemented because they conflict with the approved PRD and user decisions.

### Remove Top Benefit Strip

Do not implement the top benefit strip shown above the main navigation in the draft.

Removed items include:

- `Free & Fast Shipping`
- `24x7 Live Chat Support`
- `Lifetime Coverage`
- `Find Partner HVAC Installer`

The page starts with the hero area when pasted into the standalone landing page body. If the final Shopify theme adds its own global header, do not duplicate it inside the page HTML.

### Remove Install Planning Band

Do not implement the design draft's standalone section titled similar to:

`Confirm the Install Path Before Choosing the Final System`

Do not implement its checklist, image split, or CTAs.

Installation complexity may be mentioned briefly only inside the comparison table or FAQ when it directly affects the 2-zone vs 3-zone decision.

### Remove Find Partner HVAC Installer From Services

The design draft's `Premium Della Services` block includes `Find Partner HVAC Installer`. Replace it.

Approved service-card direction:

- `Free & Fast Shipping`
- `24x7 Live Chat Support`
- `Lifetime Coverage (Mini Splits)`
- `Warranty Registration`

Do not use financing claims unless explicitly approved later.

### FAQ Must Be Five Items

The design draft shows six FAQ entries. Implement exactly five high-value purchase questions from the PRD.

### Product Cards Must Use PRD Products

Do not copy product names, images, prices, ratings, or grouping from the design draft.

Use only the eight user-approved products in `PRD.md`.

Product cards must show live-verified prices during implementation. If live price cannot be verified, stop and ask before omitting price or using any stale value.

### Do Not Copy Footer Or Newsletter

The design draft includes a newsletter/footer area. Do not implement a custom Shopify footer or newsletter section inside this standalone page.

The bottom CTA collection cards should be the final page-owned conversion module.

## Typography

Use the topical Della font system:

- H1, H2, H3, product titles: `Spectral`, fallback `Georgia`, serif.
- Body, buttons, tabs, cards, table text: `Poppins`, fallback `Arial`, sans-serif.
- H1 should be substantial but not oversized. Preserve the draft's calm ecommerce scale.
- No negative letter spacing.
- Avoid viewport-based font scaling.

## Color And Surface Rules

Use:

- Navy: `#0E1953`
- Della blue: `#5884E7`
- Hover blue: `#6B95EF`
- Light blue: `#EDF2FF`
- Blue surface: `#F4F7FF`
- Trust/pale cyan surface: `#DDF7FF`
- White product cards and white content cards

Avoid:

- Purple gradients
- Dark stacked sections
- Glassmorphism
- Decorative orbs
- Sale red or coupon badges
- Heavy shadows

## Section-Specific Design Notes

### Hero

Follow the design draft's wide commerce banner direction:

- Left copy block with H1, short copy, and two CTAs.
- Right side shows 2-zone and 3-zone product setups.
- Keep the 2-zone and 3-zone labels above product imagery if they remain clean and readable.
- Hero visual must use product-led Della assets or a Della-style generated/composited image.
- Do not include nav/header UI inside the standalone HTML unless required by the final deployment mode.

### Room-Count Path Strip

Preserve the compact strip style under the hero.

Use only:

- `2 Rooms / 2-Zone`
- `3 Rooms / 3-Zone`
- `More than 3 rooms / View Multi-Zone`

Do not expand this into equal 1-zone, 4-zone, and 5-zone cards.

### Quick Answer Cards

Preserve the two-card layout, icon style, pale background, and full-width CTA feel.

Use PRD copy and approved URLs.

### Product Merchandising

Preserve:

- Centered heading and short supporting copy.
- Two horizontal tabs.
- Large category visual row above product cards.
- Four product cards per active tab on desktop.

Override:

- Product names, images, specs, prices, and order must come from PRD/live verification, not the mockup.
- Product CTA must be `View Product`, not `Add to Cart`.
- Product price is required and must be live-verified.

### Scenario Cards

Preserve image-card format and compact labels.

Use six PRD scenario concepts. Cards can use real or generated home images, but should not look like abstract icons or generic stock placeholders.

### More Zones Module And Comparison Table

The draft merges the `More zones` module and the comparison table into one visual band. This is acceptable if the content remains readable and does not feel cramped.

Keep:

- Light-blue surface.
- Three concise explanation points.
- Short comparison table.

Remove any separate install-planning checklist after it.

### Premium Della Services

Keep a compact late-page services block.

Use four approved service cards and exclude `Find Partner HVAC Installer`.

### FAQ

Use a compact two-column desktop layout if it remains readable.

Implement exactly five FAQ items.

### Bottom CTA

Preserve the two-card final collection choice structure, styled after the 12K vs 18K page's `Start with the collection that matches your room` block. Use text-only white cards on a pale-blue section; do not include product images or the extra multi-zone text link.

Do not add a newsletter/footer after it in the standalone page.

## Mobile Rules

- Hero copy must remain readable and must not overlap product imagery.
- Product tabs should remain accessible and obvious.
- Product cards may switch to one column under narrow mobile if two columns cause cramped prices or titles.
- Tables may horizontally scroll on small screens.
- FAQ should stack cleanly.
- No horizontal page overflow at 390px or 430px.

## Asset Strategy

- Use the supplied design image as visual reference only, not as a sliced final asset.
- Use user-provided product image URLs from PRD for product cards.
- Hero and scenario images may be generated or composited, but final data/text must follow PRD.
- Localize key fonts and stable hero/scenario assets into the project folder for reliable review when implementation begins.
- Do not localize temporary screenshots or unused drafts as final assets.

## Visual QA Criteria

Before reporting implementation complete later, verify:

- The page looks like a Della commerce landing page.
- Removed top benefit strip is not present.
- Removed install planning band is not present.
- `Find Partner HVAC Installer` is not present in services.
- Product cards use the eight approved products and live prices.
- FAQ has exactly five visible questions.
- Desktop 1280px, mobile 390px, and mobile 430px have no overlap or horizontal overflow.
- Buttons, tabs, FAQ, and product links are keyboard-accessible and visibly focusable.
## Latest User Corrections For Implementation

The implementation must use `Reference Image for the Design Draft.png` as the main visual reference but not copy it blindly.

Apply these visual/content corrections:

- Product tabs must never mix 3-zone products into the active 2-zone panel.
- Use real product titles, URLs, images, current live prices, and configuration chips from PRD/live verification.
- Do not invent ratings, review counts, SEER2, sale badges, discounts, or product claims.
- Hero product groups must clearly communicate `1 outdoor + 2 indoor units` and `1 outdoor + 3 indoor units`.
- Decision center should combine three readable decision cards with the comparison table.
- Home Situation section should use four image cards only, each with one label chip and one short heading.
- Bottom CTA should follow the 12K vs 18K bottom collection block: pale-blue area, two equal white text-only collection cards, no product images, and no extra multi-zone text link.
- Header/footer in final Shopify should come from the Shopify theme when possible. The standalone HTML demo should not rebuild the full AI footer.
- Newsletter / comfort updates strip is removed and must not be implemented.

## Latest Hero Banner Override

User correction on 2026-06-24 overrides the earlier product-comparison hero mockup direction:

- Use `banner.webp` as a full hero background image without a white overlay.
- Do not render the old right-side 2-zone/3-zone product image groups in the hero.
- Use one short supporting sentence under the H1.
- Style both hero CTAs as matching navy buttons.

## Latest Room-Count Strip Removal

User correction on 2026-06-24 removes the early room-count path strip under the hero. Do not render the four-column `Start with the rooms that need their own indoor unit` block. The page should transition from the hero directly into the first decision section.
