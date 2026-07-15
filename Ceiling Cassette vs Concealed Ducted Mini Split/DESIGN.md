# DESIGN: Ceiling Cassette vs Concealed Ducted Mini Split

## Status

- Status: Approved by user on 2026-07-14
- Date: 2026-07-14
- Page type: Della comparison and collection-support landing page
- Visual baseline: `设计稿1.png` -> `设计稿2.png` -> `设计稿3.png`
- Mockup decision: no revised long-form mockup will be generated
- Current gate: Step 5 acceptance blocked by two project-scene placeholders and named HVAC/product review
- Implementation is not authorized by this document alone

## Design Objective

Create a mature Della ecommerce decision page that helps a visitor move through this sequence with minimal friction:

`identify the two systems -> match the project -> confirm installation feasibility -> compare products -> enter the correct collection`

The page should feel visual and commercial, but not like a sale page, long article, technical manual, SaaS interface, or collection clone.

## Scope And Non-Goals

This document defines the visual and interaction treatment for the ten frozen PRD sections. It does not add sections, change products, authorize claims, set live prices, or finalize implementation details.

Do not add:

- A calculator, quiz, form, sticky purchase bar, newsletter, or popup.
- A separate definition section for either system type.
- A global Header or Footer inside the authored landing-page body.
- `Add to Cart`, direct cart URLs, coupons, countdowns, sale badges, or artificial urgency.
- Exact installation dimensions, construction instructions, or official-looking technical cutaways.
- Decorative waves, orbs, glass effects, purple gradients, or generic AI landing-page decoration.

## Source Hierarchy

When sources conflict, apply them in this order:

1. Latest explicit user decision.
2. `PRD.md` for structure, products, copy roles, factual claims, links, and acceptance criteria.
3. This `DESIGN.md` for visual composition, responsive behavior, and mockup overrides.
4. `CONTEXT.md` for canonical project language.
5. Approved local reference sections and saved screenshots.
6. The three supplied mockup images for overall visual direction and section rhythm.

The mockups are not sources for product names, prices, specifications, warranty details, support policies, or technical installation facts.

## Approved Design Sources

Primary mockup sequence:

- `设计稿1.png`: Hero, Quick Answer, Project Fit. The visible top Benefit Strip is intentionally omitted.
- `设计稿2.png`: Key Differences, Installation Requirements, Products.
- `设计稿3.png`: Trust, FAQ, Bottom CTA.

Direct component references:

- Products: `C:\Users\18041\Desktop\della-pages\single-zone-vs-multi-zone-mini-split\single-zone-vs-multi-zone-mini-split.html`, section `Find the Della setup that matches your rooms`.
- Product desktop state: `product-layout-reference.png`.
- Product 430px state: `product-layout-mobile-reference.png`.
- Trust: `C:\Users\18041\Desktop\della-pages\2-zone-vs-3-zone-mini-split\2-zone-vs-3-zone-mini-split.html`, section `Premium Della Services`.
- FAQ: the same reference page, section `2-Zone vs 3-Zone Mini Split Questions`.
- Bottom CTA: the same reference page, section `Ready to Choose Your Zone Count?`.

Brand-system references:

- `C:\Users\18041\Desktop\della-pages\della页面设计规范\della-memorial-day-design-system.md`
- `C:\Users\18041\Desktop\della-pages\della页面设计规范\page.pf-ef33e2e6.json.txt`
- `C:\Users\18041\Desktop\della-pages\della页面设计规范\pf-ef33e2e6.liquid.txt`
- Della Memorial Day/PageFly topical-page design tokens.

## Visual Direction To Preserve

Preserve these qualities from the mockups:

- Navy-led Della brand presence with generous white space.
- Spectral serif headings and Poppins interface/body copy.
- A lifestyle-led comparison Hero with both systems visible immediately.
- Large project imagery that makes abstract HVAC choices feel relevant to a real home.
- A clear progression from decision support into product merchandising.
- White product cards, pale-blue support surfaces, restrained borders, and low-shadow ecommerce styling.
- Use left-aligned section H2s and lead text; omit standalone eyebrow labels such as `Quick Answer`, `Choose by Project`, `Compare`, and `Shop Della Systems`. At desktop widths, retain H2s and their lead text on one line when the container permits; smaller layouts may wrap naturally.

Do not copy the mockups literally where this document defines an override.

## Page Frame And Rhythm

- Content container: maximum width approximately 1200px.
- Desktop side padding: 32px.
- Tablet side padding: 24px.
- Mobile side padding: 16px.
- Standard desktop section padding: 72-80px.
- Compact sections: 48-64px.
- Mobile section padding: 48-56px, with tighter spacing for Trust, FAQ, and Bottom CTA.
- Common grid gap: 16-24px.
- Avoid repeated heavy card shells around entire sections.
- The five decision sections before Products should feel connected, not like isolated presentation slides.

The supplied mockup files have different pixel widths. They establish composition, not literal page width. The implementation must use one consistent container and breakpoint system.

## Design Tokens

### Color

- Navy: `#0E1953`.
- Della Blue: `#5884E7`.
- Hover Blue: `#6B95EF`.
- Light Blue: `#EDF2FF`.
- Blue Surface: `#F4F7FF`.
- Trust Cyan: `#DDF7FF` where required outside the directly referenced Trust module.
- Body text: `#0E1952`.
- Muted text: `#53617F`.
- Border gray: `#E2E6EE`.
- White: `#FFFFFF`.

No purple, sale red, beige-led palette, or decorative gradient should become a primary page treatment.

### Typography

- H1, H2, H3, product titles, and FAQ questions: Spectral, Georgia, serif.
- Body copy, buttons, tabs, labels, tables, prices, and service labels: Poppins, Arial, sans-serif, except where the approved product reference uses Spectral for the product name and price.
- H1 desktop: approximately 48-56px, line-height 1.08-1.12.
- H1 mobile: approximately 34-40px.
- Every section H2 desktop: 32px, Spectral/Georgia serif, Navy `#0E1953`; no section-specific oversized H2 treatment.
- Every section H2 mobile: 32px, matching the approved shared H2 style.
- Body: 16px mobile and 16-17px desktop, line-height 1.55-1.65.
- Small labels: 12-14px, Poppins 500-600.
- Do not use negative letter spacing or oversized 70px-plus SaaS-style headings.

### Buttons

- Height: 48px desktop; minimum 44px mobile.
- Radius: 4px.
- Primary: navy or Della Blue fill with white text.
- Secondary: white or transparent with navy border and navy text.
- Product CTA: full width, navy, `View Product`.
- Hover: restrained color inversion or approved blue shift; no scale or bounce animation.
- Focus: visible 2px outline with sufficient offset.

### Cards And Surfaces

- Content cards: white, 1px light border, minimal or no shadow.
- Product cards: white, open merchandising layout, consistent media area and row-aligned CTA.
- Scenario cards: image-led, restrained border/radius, compact body copy.
- Comparison table: pale-blue header, thin borders, navy first column, no winner states.
- Avoid nesting a card grid inside another visually heavy card.

## Section Design Specifications

### Hero

Preserve the left-copy/right-comparison composition from `设计稿1.png`.

- Keep the exact PRD H1 and two collection CTAs.
- The right side shows a ceiling cassette room and a concealed-ducted grille result.
- Add subtle HTML overlay labels: `Ceiling Cassette` and `Concealed Ducted`.
- Retain the diagonal comparison concept only with a thinner, lower-contrast divider.
- Copy remains short and vertically centered.
- Do not place product prices, badges, promo messages, or technical claims in the Hero.

Mobile uses a dedicated composition:

- Copy and CTAs first.
- Comparison image below, with both labels visible.
- CTAs stack when two buttons cannot remain at least 44px high without cramped text.
- Do not overlay body text on the comparison image.

### Quick Answer

Preserve the two-option structure from `设计稿1.png`, but reduce its first-round height by approximately 25%.

- Keep one card per system type.
- Reduce image height and excess padding.
- Keep exactly three short cues and one collection CTA per card.
- Treat it as a routing decision band, not a second product section.
- Desktop: two columns.
- Mobile: one column; keep both cards compact and visually equal.

### Find The Best Fit For Your Project

Preserve the 2 x 2 image-card composition from `设计稿1.png`.

- Use exactly four scenarios from the PRD.
- Replace `Whole-Home Renovation` with `Multi-Room Renovation`.
- Use qualified labels such as `Start With Ceiling Cassette`, `Check Concealed Ducted First`, and `Depends on Ceiling Access`.
- Keep images dominant and explanatory copy brief.
- Do not turn these cards into clickable product cards unless `PLAN.md` explicitly assigns a collection route.
- Desktop/tablet: 2 x 2 where space permits.
- Mobile: single-column stack.

### Key Differences

Preserve the visual comparison and semantic table concept from `设计稿2.png`.

- Remove the visible internal number and task label.
- Keep one combined H2 section; do not split definitions into new modules.
- The two top visuals use a pale-blue title strip, a room scene, restrained blue conceptual airflow arrows, and a small official Della system thumbnail. They must visually parallel the approved comparison mockup without presenting exact engineering geometry.
- The table uses the approved visual hierarchy: pale-blue column headers, a Navy decision-point column with white text, thin gray dividers, and centered concise copy.
- Use the six approved rows: Best for, Visible indoors, Air distribution, Installation planning, Ceiling space, and Central-air appearance.
- Desktop: three-column semantic table.
- Mobile: accessible stacked comparison cards that retain every row and both system values.
- No winner badges, scores, or universal recommendation.

### Installation Requirements

Replace the first-round technical cutaways from `设计稿2.png` with two equal-height conceptual planning cards.

- Style: simplified two-dimensional diagram, white background, thin navy/blue lines, minimal arrows.
- Match the approved installation mockup's card grammar: centered compact system title, diagram-first upper area, compact blue circular-check list below, equal card heights, rounded light-gray border, and no nested gray diagram shell.
- Card structure: building or ceiling relationship first, planning list below it.
- Ceiling Cassette items: Ceiling opening, Available clearance, Drain route, Line-set route, Service/filter access.
- Concealed Ducted items: Indoor unit space, Supply duct route, Return-air path, Drain route, Service/filter access.
- Add `Conceptual planning diagram — not to scale` to both diagrams.
- End the module after the two planning cards; do not add a shared professional-confirmation note, installer CTA, chip bar, or extra checklist below them.
- Desktop: two equal columns.
- Mobile: one column.

Do not depict exact dimensions, internal piping, connection counts, official-looking sections, precise outlet direction, or construction order.

### Start With These Della Systems

Replace the stacked product groups in `设计稿2.png` with the approved `Find the Della setup that matches your rooms` layout.

Structure:

- Left-aligned section heading and concise introduction.
- Compact toolbar with two accessible tabs: `Ceiling Cassette` and `Concealed Ducted`.
- Collection-level `More Options` CTA aligned to the toolbar on desktop.
- One concise category introduction below the toolbar.
- One active four-product grid at a time.
- No category image banner and no project-type selector.

Product-card treatment:

- Four equal-size cards; no oversized feature card.
- Keep all four cards equal; do not show a `Recommended Starting Point` or other featured badge.
- Complete approved product title with natural wrapping.
- Two or three verified specification chips.
- Visible verified price.
- Full-width navy `View Product` CTA.
- Use one warm light-gray product stage (`#f5f4f1`) for all cassette cards. Preserve the supplied single-zone JPEGs without filters, and blend the white-background multi-zone JPEGs into that stage without replacing or generating any product image.
- No ratings, compare-at price, discount, coupon, sale badge, or `Add to Cart` unless a later PRD change authorizes it.

Responsive behavior:

- Desktop: four columns.
- Tablet: two columns.
- 390px and 430px: two columns matching `product-layout-mobile-reference.png`.
- Below 360px: one column.
- Tabs remain at least 44px high and should fit as two equal options without horizontal scrolling.
- On mobile the collection CTA moves below the tab control and becomes full width if needed.

Price treatment differs by delivery environment:

- Preview HTML: dated, live-verified static snapshot.
- Shopify production: dynamic Liquid-rendered price.
- Visual styling must remain the same in both builds.

### Why Shop Della?

Do not follow the Trust cards in `设计稿3.png`. Keep the compact four-item Della service-reference grammar, with the user-approved decision-page labels.

- H2: `Why Shop Della?`.
- Exact service labels: `Free Shipping Sitewide`, `24/7 Live Chat Support`, `Lifetime Coverage on Mini Splits`, and `Product Guidance Before You Buy`.
- Use the same borderless, centered white-card treatment. The first three items reuse approved local icons; the guidance item uses the approved inline line icon.
- Approximate icon size: 44px.
- Service label: Poppins, approximately 18px, regular weight.
- Do not add supporting paragraphs or expand coverage details.
- Desktop: four columns.
- Tablet: two columns.
- Mobile: one column, matching the reference implementation.

All four labels must be reverified immediately before publication. Unsupported wording is a stop condition, not permission for silent substitution.

### FAQ

Do not follow the two-column card accordion in `设计稿3.png`. Directly use the single-column style from `2-Zone vs 3-Zone Mini Split Questions`.

- H2: `Ceiling Cassette vs Concealed Ducted Mini Split Questions`.
- Use the six PRD questions.
- All items start collapsed.
- Transparent background, thin horizontal dividers, no card radius or filled answer panel.
- Spectral question text at approximately 20px desktop.
- Poppins answer text at approximately 15px with line-height around 1.7.
- Use the same restrained chevron, hover, open-state color, and spacing behavior as the reference.
- Use native `details` and `summary` unless implementation requirements prove an equivalent accessible accordion is necessary.
- Desktop and mobile remain one column.

### Bottom CTA

Do not follow the decorative wave banner in `设计稿3.png`. Directly use the two-path card layout from `Ready to Choose Your Zone Count?`.

- H2: `Ready to Choose Your Hidden Mini Split Type?`.
- Light product-surface section background.
- Two equal white path cards with restrained blue border and soft shadow.
- Card headings use Spectral; body and buttons use Poppins.
- Each card contains one short PRD positioning sentence and one collection CTA.
- Desktop: two columns.
- Mobile: one column.
- Do not add product thumbnails, a third path, decorative waves, or a global-shop CTA.

## Responsive Matrix

| Section | Desktop | Tablet | 390/430px | Below 360px |
| --- | --- | --- | --- | --- |
| Hero | Copy + comparison visual | Balanced split | Stacked copy then visual | Stacked |
| Quick Answer | 2 columns | 2 columns if readable | 1 column | 1 column |
| Project Fit | 2 x 2 | 2 x 2 | 1 column | 1 column |
| Comparison | Semantic table | Semantic table or stacked | Stacked comparison cards | Stacked comparison cards |
| Installation | 2 columns | 2 columns if readable | 1 column | 1 column |
| Products | 4 columns | 2 columns | 2 columns | 1 column |
| Services | 4 columns | 2 columns | 1 column | 1 column |
| FAQ | 1 column | 1 column | 1 column | 1 column |
| Bottom CTA | 2 columns | 2 columns | 1 column | 1 column |

## Interaction And State

### Product Tabs

- Only one tab panel is visible at a time.
- Default: `Ceiling Cassette` unless an earlier approved page choice has established a preferred system during the current visit.
- Support click, Enter, Space, Arrow Left, Arrow Right, Home, and End.
- Use correct `tablist`, `tab`, and `tabpanel` relationships with managed `tabindex`.
- Changing tabs must not move keyboard focus unexpectedly or scroll the page horizontally.

### FAQ

- All questions begin collapsed.
- Summary controls are keyboard operable and expose their expanded state.
- The page may allow multiple questions open at once; do not add complex exclusive-accordion logic without a conversion or accessibility reason.

### Links And Tracking Hooks

- All Della collection and product links stay in the same tab in Shopify production.
- Preview behavior may open external Della links in a new tab only if `PLAN.md` documents it.
- Add stable location/path attributes for Hero, Quick Answer, product, installer, and Bottom CTA links.
- Do not invent analytics event names before the Della convention is inspected.

## Accessibility

- Exactly one H1.
- Semantic H2/H3 hierarchy matching the nine-section structure.
- Minimum 44px interactive targets.
- Visible keyboard focus on buttons, tabs, FAQ summaries, and links.
- Text and controls meet WCAG AA contrast targets.
- Product, project, and system images use concise meaningful alt text; decorative icons use empty alt text or are hidden.
- Comparison content remains semantic and available to assistive technology in desktop and mobile presentations.
- Diagrams use HTML labels or accessible SVG text alternatives; no critical information may exist only as text baked into an image.
- Respect reduced-motion preferences; no interaction requires animation.

## Asset Strategy

- Keep all project assets and reference documents under `C:\Users\18041\Desktop\della-pages\Ceiling Cassette vs Concealed Ducted Mini Split`.
- Do not slice or crop text, products, diagrams, or cards from the full-page mockup images.
- The three mockups remain visual references only.
- Product identity images use the exact official Della CDN URLs in the PRD; preview-critical copies may be localized during implementation for stable review.
- Product desktop and mobile screenshots remain reference images and must not be embedded in the final page.
- Trust uses the four official icon assets from the approved reference HTML.
- Hero and project-scene images require approved reusable source files or newly generated/localized assets before implementation is considered visually complete.
- Installation diagrams use the user-supplied local conceptual planning files. Do not crop, redraw, overlay, or infer additional technical detail.
- Spectral and Poppins font files should be localized when the existing Della assets are available.

## 2026-07-15 Final Local Asset Map

- Hero: `banner desktop.webp` (2800 × 1000) and `banner mobile.webp` (960 × 1200), rendered with a responsive `<picture>` and no CSS-drawn divider.
- Quick Answer: `Ceiling Cassette mini split.webp` and `Concealed Ducted Mini Split.webp` (1200 × 900), cropped only by their native 4:3 display frames.
- Project Fit: `Open Concept Living Area.webp`, `Finished Basement.webp`, `New Construction.webp` (1600 × 1000), and `Whole-HomeRenovation.png` (1586 × 992), each inside a 16:10 frame. The fourth displayed title remains `Multi-Room Renovation`.
- Key Differences: `Ceiling Cassette.webp` and `Concealed Ducted.webp` (1600 × 1000), each inside a 16:10 frame with no secondary product, airflow, or label overlays.
- Installation Requirements: `Ceiling Cassette Planning.webp` and `Concealed Ducted Planning.webp` (1500 × 1000), each contained without cropping inside a 3:2 white frame. The HTML `not to scale` note remains below each diagram.
- Standalone preview has no authored benefit strip. Trust remains a separate late-page section under `Why Shop Della?`.

## Mockup Overrides

The following replacements are mandatory:

| Mockup element | Final design rule |
| --- | --- |
| Visible section numbers `5`-`10` | Remove completely |
| `Whole-Home Renovation` | Use `Multi-Room Renovation` |
| Large Quick Answer cards | Reduce total height by about 25% |
| Detailed installation cutaways | Replace with conceptual planning diagrams |
| Two product groups stacked vertically | Render as two mutually exclusive tabs |
| Featured product plus three smaller cards | Render four equal cards with no featured or starting-point badge |
| Trust cards in `设计稿3.png` | Replace with direct Premium Della Services reference |
| Two-column FAQ cards | Replace with direct single-column divider accordion reference |
| Decorative Bottom CTA banner | Replace with direct two collection-path card reference |
| Mockup product/pricing/policy text | Replace from PRD and current Shopify data |

## Preview And Production Consistency

The local/GitHub HTML and Shopify production section must share:

- Identical section order and visual hierarchy.
- Identical approved copy, products, images, tabs, FAQ, and CTAs.
- Identical responsive and accessibility behavior.
- Identical product-card visual design.

Allowed differences:

- Preview prices are dated static snapshots; Shopify prices are dynamic.
- Preview contains no global Header/Footer; Shopify is wrapped once by the normal Della theme Header/Footer.
- Shopify assets may use theme/CDN filters where the preview uses explicit local or CDN paths.

## Visual Acceptance Criteria

The design is ready for implementation planning only when all of the following are accepted:

- The current mockups are treated as a baseline, not literal final screens.
- Every Mockup Override above is understood as mandatory.
- No new section has been introduced.
- Hero immediately distinguishes both system types.
- Project Fit remains the visual and decision center of the page.
- Installation visuals read as planning aids, not official instructions.
- Product merchandising matches both saved product-layout references.
- Services, FAQ, and Bottom CTA match their direct Della references.
- Mobile behavior is unambiguous at 390px and 430px.
- No claim, price, product, or technical fact is sourced from the mockup.

## Known Asset And Verification Gaps

These items do not block approval of this design document, but they block final implementation acceptance where applicable:

- Reusable desktop and mobile Hero source assets are supplied and mapped.
- Final project-scenario source image map is supplied and mapped.
- Two multi-zone concealed-ducted manual sources still require successful verification.
- A named product or HVAC reviewer is still required for the conceptual planning diagrams.
- All four Premium Della Services labels require launch-time verification.
- Final FAQ answer copy and FAQPage JSON-LD are not yet approved.
- Current prices and availability for all eight products must be captured during implementation.
- Existing Della analytics event naming and the final Shopify canonical URL remain unconfirmed.

## Next Gate

Stop after this document.

After the user approves `DESIGN.md`, create `PLAN.md` with separate, verifiable steps for:

- Asset preparation.
- Preview HTML.
- Shopify Liquid section.
- JSON page template.
- Dynamic versus preview price handling.
- Responsive and accessibility behavior.
- Browser, link, price, claim, and visual QA.

Do not implement HTML, Liquid, JSON, or theme changes before `PLAN.md` is approved.
