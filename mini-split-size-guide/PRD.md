# PRD: Della Mini Split Size Guide Landing Page

Last updated: 2026-05-28  
Project folder: `C:\Users\18041\Desktop\della-pages\Mini Split Size Guide`  
Primary deliverable planned after approval: `index.html`

## 1. Objective

Create a static HTML demo landing page for `dellahome.com` titled:

**Mini Split Size Guide: Find the Right BTU for Your Room**

The page should capture research-oriented organic traffic and also work as a paid-ad landing page. Its primary job is not to immediately sell one product. Its primary job is to help users answer:

> "What mini split BTU size do I probably need?"

After that decision is framed, the page should naturally route users to Della's BTU collection pages:

- 9,000 BTU: https://dellahome.com/collections/9000-btu-mini-split
- 12,000 BTU: https://dellahome.com/collections/12000-btu-mini-split
- 18,000 BTU: https://dellahome.com/collections/18000-btu-mini-split
- 24,000 BTU: https://dellahome.com/collections/24000-btu-mini-split
- 36,000 BTU: https://dellahome.com/collections/36000-btu-mini-split

## 2. Positioning Decision

This page should be a **BTU decision landing page**, not:

- a generic HVAC blog article
- a hard-sell collection page
- a coupon or promo page
- a calculator-style SaaS lead-gen page

Recommended balance:

- First 40%: help the user choose a starting BTU
- Middle 35%: guide users into Della BTU collection paths
- Final 25%: installation confidence, right-sizing trust, support, FAQ

The page should feel like a mature Della ecommerce guide: direct, visual, brand-consistent, useful, and lightly commercial.

## 3. Audience And Intent

Primary audience:

- sizing-first researchers searching queries such as `mini split size guide`, `what size mini split do I need`, `mini split BTU chart`
- homeowners comparing BTU options before shopping
- paid-ad visitors who need a decision path before a collection click

Secondary audience:

- ready-to-buy shoppers who already know room size
- comparison shoppers deciding between 9K, 12K, 18K, 24K, and 36K
- users with installation uncertainty around voltage, line-set routing, and professional sizing confirmation

Primary scope:

- Help users choose a starting BTU for one room or one main space.
- Keep the first version focused on single-room / single-zone starting BTU decisions.
- Route users to 9K / 12K / 18K / 24K / 36K BTU collections.
- Explain that square footage is only a starting point and should be adjusted for insulation, sun exposure, ceiling height, layout, and heat load.

Out of scope for the main page:

- full multi-zone sizing section
- 2-zone / 3-zone / 4-zone product matrix
- whole-home sizing calculator
- whole-home load guide
- multi-zone product selector
- interactive BTU calculator
- input fields, sliders, or form submission
- dynamic BTU formula
- `calculate my BTU` result panel
- room dimension calculator

Primary user action:

- choose a likely BTU tier
- click into the corresponding Della BTU collection

Secondary user actions:

- use the BTU chart to validate a rough size
- understand when to move up one tier
- contact support or find an HVAC installer
- continue to resources, rebate center, warranty registration, or related sizing pages

## 4. Research Basis

### Della Collection Facts

Verified on 2026-05-28 from Della collection pages:

| BTU path | Current collection range/filter | Current result count | UX implication |
| --- | --- | ---: | --- |
| 9K | `0 - 400` sq ft | 8 results | Strong primary path |
| 12K | `401 - 550` sq ft | 12 results | Strongest merchandising path |
| 18K | `551 - 1000` sq ft | 6 results | Strong primary path |
| 24K | `1001 - 1500` sq ft | 4 results | Valid path, slightly lower depth |
| 36K | `1501 - 2500` sq ft | 1 result | Keep in selector, downweight in merchandising |

Implementation rule:

- Use these Della collection ranges consistently in the BTU selector, sizing chart, room-use copy, and shop-path copy.
- Do not substitute broader generic HVAC estimate ranges in the final HTML.
- If an AI design mockup uses broader visual placeholder ranges such as `9K = 250-450 sq ft` or `12K = 450-650 sq ft`, treat those as visual placeholders only and correct the final HTML to the Della collection-aligned ranges.
- Frame ranges as starting points, not guaranteed coverage.
- Preferred wording: `starting point`, `up to about`, `often fits`, `adjust for room conditions`, `confirm with installer`.
- HVAC complexity should be handled later in `What Can Change Your BTU Size?` and `Before You Order, Confirm These With Your Installer`.

Source pages:

- https://dellahome.com/collections/9000-btu-mini-split
- https://dellahome.com/collections/12000-btu-mini-split
- https://dellahome.com/collections/18000-btu-mini-split
- https://dellahome.com/collections/24000-btu-mini-split
- https://dellahome.com/collections/36000-btu-mini-split

### HVAC Guidance

Use square footage as a starting point, not a final load calculation.

Source principles:

- ACCA Manual J is the ANSI-recognized standard for producing residential HVAC equipment sizing loads. Source: https://www.acca.org/technical-manual/manual-j
- ENERGY STAR guidance warns that oversized air conditioners can cycle on and off more frequently and may not dehumidify effectively. Source: https://www.energystar.gov/sites/default/files/2025-03/2025%20Room%20AC%20Factsheet.pdf
- ENERGY STAR's right-sized air conditioner material reinforces that oversized systems can have short run times and reduced humidity control. Source: https://www.energystar.gov/ia/home_improvement/home_sealing/RightSized_AirCondFS_2005.pdf

Implementation wording should avoid absolute guarantees. Preferred language:

- "starting point"
- "often"
- "may"
- "move up when"
- "confirm with your installer"
- "for many rooms"

Avoid:

- "perfect for every room"
- "guaranteed to cool"
- "always choose"
- "one 36K unit can cool your whole home"

## 5. Design References

Use these local files as brand and UI references:

- `C:\Users\18041\Desktop\della-pages\page.pf-ef33e2e6.json.txt`
- `C:\Users\18041\Desktop\della-pages\pf-ef33e2e6.liquid.txt`
- `C:\Users\18041\Desktop\della-pages\della-memorial-day-design-system.md`

Use Della coupon / Memorial Day pages for:

- ecommerce banner rhythm
- typography
- button style
- product-card grammar
- trust strip behavior
- FAQ placement
- section spacing and merchandising density

Do not copy:

- sale dates
- coupon code language
- countdowns
- holiday design
- "Save Now" behavior
- discount badges
- giveaway or referral copy
- `Add To Cart` as the primary action

Existing Della demo pages may be used for layout logic only:

- `single-zone-vs-multi-zone-mini-split.html`: room-use chooser, installation confirmation logic
- `mini-split-for-garage.html`: before-you-size logic, sizing caveats
- `mini-split-for-apartment.html`: choose-by-main-room structure
- `mini-split-for-attic.html`: square footage plus heat-load factors
- `mini-split-for-shed.html`: BTU-first decision structure
- `mini-split-for-basement.html`: right-sizing and install caveats
- `mini-split-for-sunroom.html`: sun exposure and one-tier-up logic

Do not copy the visual style from the GitHub demo pages if it conflicts with the current Della coupon / Memorial Day design system.

External SEO structure reference:

- `https://centralairinstallcost.com/cost-by-home-size` may be used only for content-structure thinking: quick answer, complete size table, how sizing is calculated, Manual J mention, and oversizing/undersizing explanation.
- Do not copy its UI pattern, visual styling, section aesthetics, template-like card layout, or generic AI-blog presentation.
- Translate any useful structure into Della's own ecommerce decision-page grammar: BTU snapshot, sizing table, adjustment factors, right-sizing warning, and collection paths.

## 6. AI Design Draft Workflow

The intended creative workflow for this page is:

1. Gemini writes the prompt for a full-page long-form landing page design draft.
2. GPT generates the full-page long image design mockup from that prompt.
3. The user sends the design image to Codex.
4. Codex studies the image, maps it back to the PRD requirements, and recreates the page as static HTML/CSS.

Implications:

- PRD requirements remain the source of truth for content, strategy, SEO, CTA logic, product data, and technical constraints.
- The generated long image becomes the source of truth for visual composition after the user approves it.
- If the image conflicts with PRD strategy, Codex should flag the conflict before implementation instead of blindly copying it.
- Codex should replicate the approved image's layout, hierarchy, spacing, and visual rhythm, while preserving Della brand tokens and accessible HTML.
- The image should not override critical constraints: no `Add To Cart`, no heavy promotion, no fake 36K depth, no unsupported sizing claims, and no SaaS dashboard look.

Gemini prompt requirements:

- Ask for a tall full-page ecommerce landing page design, not a web-app dashboard.
- Include all core sections from this PRD in order.
- Make the page look like a Della branded ecommerce sizing guide.
- Use product-led visual language, compact BTU decision cards, a clean sizing table, restrained product/collection cards, right-sizing warning, installer checklist, trust cards, and FAQ.
- Hero should combine a Della-style wall-mounted mini split, a modern American room scene, and 2-4 lightweight static BTU/room-size cue chips.
- Avoid gradients, glassmorphism, generic icon-card grids, blog-style walls of text, and promo/sale visual language.
- Do not create a calculator dashboard hero.

When the design image is later provided:

- Codex should create or update implementation planning docs before coding if needed.
- Codex should identify any sections in the image that are missing from the PRD or conflict with the PRD.
- Codex should implement the page in `index.html`, verify desktop/mobile rendering, and report visual deviations that could not be matched.

## 7. Brand And UI Requirements

Typography:

- H1, H2, H3, product title: `Spectral`, fallback `Georgia`, `serif`
- Body, buttons, tabs, labels: `Poppins`, fallback `Arial`, `sans-serif`
- H1 desktop: 40-58px
- H1 mobile: 34-44px
- Body: 16-17px desktop, 16px mobile, line-height around 1.6
- No negative letter spacing

Color tokens:

```css
--navy: #0E1953;
--blue: #5884E7;
--blue-hover: #6B95EF;
--blue-light: #EDF2FF;
--blue-surface: #F4F7FF;
--trust-bg: #DDF7FF;
--gray-50: #F8F9FB;
--gray-100: #F0F2F6;
--gray-200: #E2E6EE;
--gray-300: #C9D1E3;
--text-body: #0E1952;
--white: #FFFFFF;
```

Buttons:

- Primary: blue fill, white text
- Secondary: white or transparent fill, navy text, light border
- Border radius: 4px
- Height: 44-48px
- PDP product card CTA: `View Product`
- Collection/card CTA: `Shop 9K`, `Shop 12K`, `Shop 18K`, `Shop 24K`, `Shop 36K`
- Tab-level CTA: `View All 12K Options` or matching BTU option label
- Do not use pill CTAs, gradient CTAs, or `Add To Cart`

Layout:

- Desktop container: 1200px max-width, 32px side padding
- Mobile side padding: 16px
- Desktop section rhythm: 72-80px
- Mobile section rhythm: 48-56px
- Product/collection cards: 4 columns desktop when enough items exist; 2 columns mobile
- 36K should not be forced into a fake 4-card layout

Avoid:

- AI-template look
- SaaS dashboard calculator hero
- glassmorphism
- purple gradients
- decorative orbs
- giant generic icon cards
- heavy shadows
- cards nested inside cards
- a hero that is mostly paragraph text

## 8. Conversion Strategy

Primary conversion path:

1. User lands on the page.
2. User understands the page is a quick BTU sizing guide.
3. User scans the BTU selector.
4. User checks the chart or adjustment factors.
5. User clicks a BTU collection CTA.

CTA hierarchy:

- Hero primary: `Find My Starting BTU`
- Hero secondary: `Shop by BTU`
- BTU path cards: `Shop 9K`, `Shop 12K`, `Shop 18K`, `Shop 24K`, `Shop 36K`
- PDP product cards: `View Product`
- Tab-level collection CTA: `View All 12K Options` or matching BTU option label
- Installer module: `Find Partner HVAC Installer`, `Contact Della Support`
- Bottom CTA: `Start with Your Room Size`, `Compare All BTU Sizes`

36K treatment:

- Keep 36K in the BTU selector because it is a legitimate large-space path.
- Downweight it in product merchandising because the collection currently has only one result.
- Copy should frame it as "very large or high-load spaces" and recommend confirming layout before checkout.

## 9. Page Structure

### 01. Top Benefit Strip

Purpose:

- establish ecommerce confidence without turning the page into a promotion

Items:

- Free Shipping Sitewide
- Find Partner HVAC Installer
- 24/7 Live Chat Support

Rules:

- Keep this as a very light one-line strip.
- It should establish quick ecommerce trust before the hero.
- It does not replace the lower-page `Premium Della Services` section.
- Do not lead with financing in the top strip. Financing appears in the reused `Premium Della Services` section later.

### 02. Hero

H1:

`Mini Split Size Guide: Find the Right BTU for Your Room`

Subcopy:

`Start with your room size, then adjust for insulation, sun exposure, ceiling height, and how the room is used. Compare 9K, 12K, 18K, 24K, and 36K mini split options.`

Primary CTA:

- `Find My Starting BTU`

Secondary CTA:

- `Shop by BTU`

Visual direction:

- wide Della ecommerce banner feel
- product-led lifestyle banner, not a pure product ad
- right side should show a modern American room with a clearly visible Della-style wall-mounted mini split
- include a few lightweight static sizing cue chips so the hero reads as a size guide, not just a lifestyle page
- recommended cue chips: `12K BTU`, `401-550 sq ft`, `Bedroom / Office`, `Adjust for sun & insulation`
- optional simple room outline or square-foot cue is acceptable if it stays subtle
- no full dashboard calculator in the hero
- no product cards in the hero
- no input fields, sliders, forms, SaaS analytics cards, graph widgets, or complex data panels
- no glassmorphism or over-layered floating UI
- hero visual must not overpower the H1, short body copy, or two CTA buttons
- on mobile, reduce cue chips to 1-2 or hide secondary chips if they crowd the image

### 03. Choose Your Starting Mini Split Size

Purpose:

- provide the core decision path immediately after the hero
- act as a static sizing selector, not a calculator

Use 5 compact collection path cards:

| Card | Copy | CTA |
| --- | --- | --- |
| 9,000 BTU | Small bedrooms, offices, enclosed spaces up to about 400 sq ft | Shop 9K |
| 12,000 BTU | Bedrooms, studios, and main rooms around 401-550 sq ft | Shop 12K |
| 18,000 BTU | Larger rooms and open areas around 551-1,000 sq ft | Shop 18K |
| 24,000 BTU | Large open spaces around 1,001-1,500 sq ft | Shop 24K |
| 36,000 BTU | Very large or high-load spaces around 1,501-2,500 sq ft | Shop 36K |

These ranges must match Della's collection filters in the first implementation. Do not use broader visual-placeholder ranges in final HTML.

Interaction:

- desktop can use a clean 5-card row or 3+2 grid
- mobile must use a horizontally scrollable collection-path strip, not a 2-column grid
- use CSS `overflow-x` with `scroll-snap`; do not require custom heavy carousel JS
- mobile card width should be stable, around 72-82% of viewport width or a fixed min-width around 230-260px
- show a small peek of the next card to signal that the strip is scrollable
- touch targets must be at least 44px high
- keep card content concise: BTU number, sq-ft range, short room cue, CTA
- avoid tiny text and multiline overflow
- active/hover states should be subtle Della blue, not large animations
- cards may anchor to the sizing chart or activate the matching product tab
- do not collect user inputs or calculate a BTU result
- the default 12K card may be lightly highlighted, but do not use a `best`, `winner`, or similar badge
- tablet may use horizontal scroll or 3+2 depending on available width

### 04. Mini Split BTU Chart by Room Size

Purpose:

- satisfy SEO, AI extraction, and quick-answer intent

Table columns:

- Room size
- Common room examples
- Starting BTU
- Move up when

Tone:

- concise, not bloggy
- "starting point" language
- "move up when" notes are the trust-builder

Expected rows:

- up to about 400 sq ft: 9K
- 401-550 sq ft: 12K
- 551-1,000 sq ft: 18K
- 1,001-1,500 sq ft: 24K
- 1,501-2,500 sq ft: 36K

### 05. What Can Change Your BTU Size?

Purpose:

- prevent the page from being an oversimplified chart
- establish Della as a helpful buying guide

Required factors:

- insulation quality
- sun exposure and window area
- ceiling height
- open layout vs enclosed room
- heat-generating use such as garage gym, workshop, kitchen-adjacent room, sunroom, or attic

Design:

- implement this as a single `Sizing Notes` panel
- do not use five separate factor icon cards
- left side: product/room visual, simple home-room illustration, or Della-style lifestyle visual
- right side: compact checklist-style sizing notes
- mobile: stack visual above notes
- keep notes short, scannable, and decision-focused
- use a calm Della-style guidance panel with light-blue background or a white card inside a soft blue section

Key message:

`Square footage is the starting point, not the final answer.`

Suggested subcopy:

`Square footage is the starting point. Room conditions can move your BTU choice up or down.`

Recommended note structure:

- Insulation: Poor insulation may require moving up one BTU tier.
- Sun exposure: South-facing rooms or large windows can add heat load.
- Ceiling height: Taller ceilings increase the air volume that needs conditioning.
- Open layout: Connected spaces may need a larger capacity or a different system plan.
- Heat load: Garages, gyms, kitchens, and sunrooms may need extra capacity.

Avoid:

- generic icon-grid layout
- five equal white cards with oversized icons
- SaaS/dashboard styling
- technical or alarmist language

### 06. Choose by How the Room Is Used

Purpose:

- translate sizing into real household scenarios
- borrow the useful logic from existing Della scenario pages

Cards:

- Bedroom / office: usually 9K or 12K
- Studio / apartment main room: often 12K
- Garage / shed: often 12K or 18K depending on insulation
- Open living room: often 18K or 24K
- Sunroom / attic: often one tier higher because of heat gain
- Large open area: 24K or 36K, confirm layout

Each card should include:

- short scenario phrase
- likely BTU range
- one lightweight text-link CTA to the most relevant collection, sizing section, or product tab

CTA rules:

- Do not use filled blue buttons on every scenario card.
- Keep strong CTA buttons for the BTU selector and product tabs.
- Scenario cards should remain light, scannable, and lifestyle-oriented.
- Use subtle navy or blue text links.
- No repeated full-width buttons.
- No sale-style CTA.
- No `Add To Cart`.
- Keep scenario cards visually distinct from product cards.

Recommended card structure:

- scene name
- one short description or use case
- suggested BTU range
- light text link

Example link patterns:

- Bedroom / Office: `View 12K options`
- Garage / Shed: `View garage sizing notes`
- Open Living Room: `View 18K options`
- Sunroom / Attic: `Compare 18K and 24K`
- Large Open Area: `View large-space options`

If the scenario has sizing uncertainty, the link can point to the sizing chart or activate a product tab rather than going directly to a product.

Multi-zone / whole-home cross-link:

- Include only one concise split-path note near the sizing chart, room-match section, or installer checklist.
- This note should support routing, not become a major section.
- Suggested copy: `Sizing more than one room? If you want independent comfort in multiple rooms, start with this guide for each room's BTU range, then compare single-zone vs. multi-zone system options.`
- CTA: `Compare Single-Zone vs. Multi-Zone Mini Splits`
- Link target should be the existing single-zone vs multi-zone guide.
- Do not add a full multi-zone sizing chart, 2-zone / 3-zone / 4-zone layout guide, whole-home sizing calculator, or multi-zone product selector.

### 07. Bigger Is Not Always Better

Purpose:

- build trust and prevent bad sizing behavior
- correct the common assumption that a larger BTU system is automatically better
- prepare users to compare product models and prices with a better sizing mindset

Core points:

- oversized systems may short cycle
- short cycling can reduce humidity control and comfort
- undersized systems may run constantly and struggle on high-load days

Required structure:

- use a concise 3-column comparison, not a large educational wall
- columns: `Too Small`, `Right Size`, `Too Large`
- `Too Small`: runs constantly / struggles on hot days
- `Right Size`: steadier comfort / better humidity control
- `Too Large`: short cycling / uneven comfort / poor humidity control
- lightly highlight `Right Size` as the preferred middle state

Design:

- one high-confidence module
- navy or light-blue treatment
- short, supportive language
- no fear-based copy

Order rule:

- This section must appear before `Shop Mini Splits by BTU`.
- Even if an AI mockup places product tabs before the right-size module, final HTML should follow the PRD order because this module is part of the sizing decision flow.

### 08. Shop Mini Splits by BTU

Purpose:

- convert users after they have seen the sizing logic
- provide ecommerce continuity without over-selling

Required first implementation:

- include real PDP-style product cards in this middle/lower merchandising section
- keep the earlier hero-adjacent BTU selector as collection path cards only
- use tabs for 9K / 12K / 18K / 24K / 36K
- model the interaction pattern after the `Find the Della setup that matches your rooms` section from the local `single-zone-vs-multi-zone-mini-split.html` page: tab toolbar, category intro block, then product grid
- use Della product-card grammar visually and route product cards to PDP URLs
- default active tab should be `12K` unless implementation testing shows a better default
- BTU selector cards earlier on the page should be able to anchor or switch users into the matching BTU product tab when practical

Product card rules:

- PDP product card CTA must be `View Product`
- tab-level or collection CTA can use `View All 12K Options` or the matching BTU label
- no `Add To Cart`
- no sale badges
- no coupon code copy
- show current product prices in the cards
- show current sale/current price as the primary price
- show compare-at price as a strikethrough only if it can be reliably collected from the live product page
- if compare-at price is unavailable or inconsistent, show only the current price
- collect prices immediately before implementation or final review because price is volatile ecommerce data
- record the collection date in implementation notes or page comments if prices are hardcoded in the static demo
- do not invent missing prices or reuse stale prices from memory
- do not show coupon codes, discount percentages, countdowns, or `Save` badges

36K treatment:

- show one card or one collection card plus an installer confirmation note
- do not fake a 4-card grid

### 09. Before You Order, Confirm These With Your Installer

Purpose:

- help users understand what still needs professional or project-specific confirmation
- support Google Ads trust and high-ticket purchase confidence

Checklist:

- room-by-room load or sizing check
- voltage and electrical panel capacity
- line-set and drain route
- outdoor unit placement and clearance

CTAs:

- `Find Partner HVAC Installer`
- `Contact Della Support`

### 10. Support Confidence

Purpose:

- reinforce Della support without adding a heavy ecommerce block

Implementation decision:

- Reuse the `Premium Della Services` section from the local `single-zone-vs-multi-zone-mini-split.html` page.
- Copy the section layout and four-card service structure directly unless later brand references override it.
- This is a lower-page confidence section, not a replacement for the hero or BTU decision modules.

Cards to reuse:

- Free & Fast Shipping
- Pay in 6 Months, 0% APR
- 24x7 Live Chat Support
- Lifetime Coverage (Mini Splits)

Design:

- keep the same Della service-card grammar as the reference page
- keep it compact and late-page
- do not expand it into a major explanatory section
- do not move this full four-card block above the hero or immediately after the hero

### 11. Mini Split Size Guide FAQs

Maximum 6 FAQ items:

1. What size mini split do I need?
2. Is 12,000 BTU enough for a bedroom or studio?
3. When should I move from 12K to 18K?
4. Is a 24K mini split too large for one room?
5. Can one 36K mini split cool multiple rooms?
6. Why should I not oversize a mini split?

FAQ rules:

- maximum 6 FAQ items in the first version
- concise answers, usually 2-4 sentences
- each FAQ should answer a buying or sizing objection
- avoid repeating the whole page
- keep FAQ near the bottom and visually compact
- include FAQ JSON-LD in the final HTML
- do not use FAQ as the main SEO content container
- do not add extra FAQ just to chase long-tail keywords in the first version

Long-tail coverage should mainly come from:

- H2 headings
- BTU selector labels
- sizing chart rows
- adjustment factor copy
- room scenario cards
- FAQ schema

## 10. SEO Requirements

Primary keyword:

- `mini split size guide`

Secondary keyword themes:

- `what size mini split do I need`
- `mini split BTU chart`
- `mini split sizing chart`
- `9000 BTU mini split`
- `12000 BTU mini split`
- `18000 BTU mini split`
- `24000 BTU mini split`
- `36000 BTU mini split`
- `mini split for room size`

Recommended metadata:

- Title: `Mini Split Size Guide: Find the Right BTU for Your Room | Della`
- Meta description: `Use Della's mini split size guide to compare 9K, 12K, 18K, 24K, and 36K BTU options by room size, layout, insulation, and sun exposure.`

Required structured data:

- FAQPage JSON-LD
- BreadcrumbList optional if final Shopify URL is known

SEO content constraints:

- H1 must appear once
- H2s should match the section sequence
- table should be semantic HTML
- links should use descriptive anchor text
- external links should use `target="_blank" rel="noopener"` in demo HTML
- avoid unsupported technical claims

## 11. Measurement Plan

Primary conversion events:

- click on BTU collection CTA
- click on product/collection card CTA

Secondary events:

- hero `Find My Starting BTU`
- hero `Shop by BTU`
- installer CTA
- support CTA
- FAQ expand
- BTU tab change if tabs are used
- mobile horizontal selector interaction if implemented

Post-launch review:

- scroll depth to BTU selector
- click distribution by BTU tier
- 36K click rate vs bounce risk
- paid-ad CVR compared with direct collection landing pages
- organic query growth around size-guide terms
- whether users use chart CTAs or product module CTAs more often

## 12. Product Card Data

Use this product data when the design or implementation includes PDP-style product cards. If the first implementation uses collection cards only, keep this data available for the later merchandising module.

Product card rules:

- PDP product card CTA should be `View Product`.
- Do not use `Add To Cart`.
- Do not add sale badges, coupon copy, or discount language unless a separate promo brief is approved.
- V1 product images should use the exact Della CDN image URLs provided in this section for speed and accuracy.
- Do not invent product images.
- Do not extract product images from an AI-generated mockup.
- Do not download all product images into `assets/` during the first implementation unless loading fails.
- Add proper width/height attributes where practical, `object-fit`, `loading="lazy"`, and descriptive alt text.
- For above-the-fold hero or critical visual images, use preload or `fetchpriority` only if needed.
- Asset localization can be handled as a separate review/handoff step if needed.
- Product cards should show prices.
- Product cards should show the current sale/current price as the main price.
- Compare-at price may appear as a strikethrough only if it is reliably available on the live product page.
- If compare-at price is missing or unstable, show only the current price.
- Price data must be collected from the live Della product pages, or a Shopify product JSON endpoint if available, immediately before implementation or final review.
- If prices are hardcoded for the static HTML demo, mark them as a dated snapshot and treat them as volatile data.
- Do not invent missing prices or use stale remembered prices.
- Do not show coupon codes, discount percentages, countdowns, or `Save` badges in this sizing guide.
- 36K has one product path and should be treated as a large-space confirmation path, not a fully stocked featured tab.

Price capture process:

- Query each live product page or Shopify product JSON endpoint before writing final product cards.
- Record captured price data in an implementation note with date/time.
- If current price is clearly visible, display current price.
- If compare-at price is clearly visible and stable, display compare-at price as a secondary strikethrough price.
- If compare-at price is not visible or uncertain, do not invent it.
- If price cannot be fetched reliably, do not make up a price. Either omit the price line or mark it internally as `needs manual confirmation`.
- Do not use prices from an AI mockup. The mockup is only for layout and visual hierarchy.
- Since this is a Mini Split Size Guide, price is helpful but not mandatory. If price scraping is unreliable, omit prices rather than showing incorrect prices.

Recommended implementation record format:

- product title
- product URL
- image URL
- current price snapshot
- compare-at price snapshot, if visible
- date/time captured
- source method: live product page or Shopify JSON
- any products needing manual confirmation

Avoid for pricing:

- invented prices
- stale manual prices
- coupon-adjusted prices
- checkout-only discount prices
- hidden promo pricing
- fake compare-at pricing
- sale badges or discount labels

When to localize product images later:

- local browser review shows broken or slow image loading
- the user requests a fully offline demo
- final handoff requires all demo assets to be self-contained
- CDN hotlinking or the review environment causes issues
- image compression or cropping needs to be controlled locally

Shopify/PageFly note:

- For the actual Shopify/PageFly implementation, Shopify CDN product images are acceptable and expected.
- Local assets are more important for generated hero/support visuals or offline static demo review than for every product card.

### 9,000 BTU Products

| Product | Product URL | Image URL |
| --- | --- | --- |
| Della Serena Cloud Air Series 9000 BTU 22 SEER2 Mini Split Heat Pump AC up to 400 sq ft | https://dellahome.com/products/della-serena-cloud-air-series-9000-btu-22-seer2-mini-split-heat-pump-ac-up-to-400-sq-ft | https://dellahome.com/cdn/shop/files/9K1VR-22S-MX-I-O_01.jpg?crop=center&height=1800&v=1776763354&width=1800 |
| Optima Series 9000 BTU SEER2 24 Ultra Heat Mini Split AC up to 400 sq ft | https://dellahome.com/products/optima-series-9000-btu-seer2-24-ultra-heat-mini-split-ac-up-to-400-sq-ft | https://dellahome.com/cdn/shop/files/TP_6a7b63f4-9ce7-4af4-9b4a-a56873b66147.jpg?crop=center&height=1200&v=1764061301&width=1200 |
| Vario Series 9000 BTU SEER2 20 Mini Split Heat Pump AC up to 400 sq ft | https://dellahome.com/products/vario-series-9000-btu-seer2-20-mini-split-heat-pump-ac-up-to-400-sq-ft | https://dellahome.com/cdn/shop/files/048-TL-9K1VB-19S-01.jpg?crop=center&height=1200&v=1750225850&width=1200 |
| Della Vario Series 9000 BTU 19 SEER2 Mini Split Heat Pump AC R-454B up to 400 sq ft | https://dellahome.com/products/della-vario-series-9000-btu-19-seer2-mini-split-heat-pump-ac-r-454b-up-to-400-sq-ft | https://dellahome.com/cdn/shop/files/048-TL-9K1VB-19S-01.jpg?crop=center&height=1800&v=1750225850&width=1800 |

### 12,000 BTU Products

| Product | Product URL | Image URL |
| --- | --- | --- |
| Optima Series 12000 BTU SEER2 24 Ultra Heat Mini Split AC up to 550 sq ft | https://dellahome.com/products/optima-series-12000-btu-seer2-24-ultra-heat-mini-split-ac-up-to-550-sq-ft | https://dellahome.com/cdn/shop/files/TP_6a7b63f4-9ce7-4af4-9b4a-a56873b66147.jpg?crop=center&height=1800&v=1764061301&width=1800 |
| Vario Series 12000 BTU SEER2 23 Mini Split Heat Pump AC up to 550 sq ft | https://dellahome.com/products/vario-series-12000-btu-seer2-23-mini-split-heat-pump-ac-up-to-550-sq-ft | https://dellahome.com/cdn/shop/files/TL-NEW_8819b5ba-1b5a-4398-af5a-01c9a82d095e.jpg?crop=center&height=1200&v=1753232832&width=1200 |
| Umbra Series 12000BTU SEER2 17 Mini Split Heat Pump AC | https://dellahome.com/products/umbra-series-12000btu-seer2-17-mini-split-heat-pump-ac | https://dellahome.com/cdn/shop/files/JPB.jpg?crop=center&height=1200&v=1731029992&width=1200 |
| Della Serena Cloud Air Series 12000 BTU 22 SEER2 Mini Split Heat Pump AC up to 550 sq ft | https://dellahome.com/products/della-serena-cloud-air-series-12000-btu-22-seer2-mini-split-heat-pump-ac-up-to-550-sq-ft | https://dellahome.com/cdn/shop/files/9K1VR-22S-MX-I-O_01.jpg?crop=center&height=1200&v=1776763354&width=1200 |

### 18,000 BTU Products

| Product | Product URL | Image URL |
| --- | --- | --- |
| Serena Series 18000 BTU SEER2 22 Mini Split Heat Pump AC up to 1000 sq ft | https://dellahome.com/products/serena-series-18000-btu-seer2-22-mini-split-heat-pump-ac-up-to-1000-sq-ft | https://dellahome.com/cdn/shop/files/M.jpg?crop=center&height=1200&v=1750938870&width=1200 |
| Vario Series 18000 BTU SEER2 21 Mini Split Heat Pump AC up to 1000 sq ft | https://dellahome.com/products/vario-series-18000-btu-seer2-21-mini-split-heat-pump-ac-up-to-1000-sq-ft | https://dellahome.com/cdn/shop/files/TL-NEW_8819b5ba-1b5a-4398-af5a-01c9a82d095e.jpg?crop=center&height=1800&v=1753232832&width=1800 |
| Umbra Series 18000BTU SEER2 19 Mini Split Heat Pump AC | https://dellahome.com/products/umbra-series-18000btu-seer2-19-mini-split-heat-pump-ac | https://dellahome.com/cdn/shop/files/JPB.jpg?crop=center&height=1800&v=1731029992&width=1800 |
| Della Serena Cloud Air Series 18000 BTU 22 SEER2 Mini Split Heat Pump AC up to 1000 sq ft | https://dellahome.com/products/della-serena-cloud-air-series-18000-btu-22-seer2-mini-split-heat-pump-ac-up-to-1000-sq-ft | https://dellahome.com/cdn/shop/files/9K1VR-22S-MX-I-O_01.jpg?crop=center&height=1800&v=1776763354&width=1800 |

### 24,000 BTU Products

| Product | Product URL | Image URL |
| --- | --- | --- |
| Vario Series 24000 BTU SEER2 21 Mini Split Heat Pump AC up to 1500 sq ft | https://dellahome.com/products/vario-series-24000-btu-seer2-21-mini-split-heat-pump-ac-up-to-1500-sq-ft | https://dellahome.com/cdn/shop/files/TL-NEW_8819b5ba-1b5a-4398-af5a-01c9a82d095e.jpg?crop=center&height=1800&v=1753232832&width=1800 |
| Della 23,000 BTU SEER2 22.5 Ceiling Cassette Ductless Mini Split AC up to 1500 sq ft | https://dellahome.com/products/della-23-000-btu-seer2-22-5-ceiling-cassette-ductless-mini-split-ac-up-to-1500-sq-ft | https://dellahome.com/cdn/shop/files/pp.jpg?crop=center&height=1200&v=1764061000&width=1200 |
| Della Serena Cloud Air Series 23000 BTU 22 SEER2 Mini Split Heat Pump AC up to 1500 sq ft | https://dellahome.com/products/della-serena-cloud-air-series-23000-btu-22-seer2-mini-split-heat-pump-ac-up-to-1500-sq-ft | https://dellahome.com/cdn/shop/files/9K1VR-22S-MX-I-O_01.jpg?crop=center&height=1200&v=1776763354&width=1200 |
| Della Motto Series 23000 BTU 19 SEER2 Mini Split Heat Pump AC up to 1500 sq ft | https://dellahome.com/products/della-motto-series-23000-btu-19-seer2-mini-split-heat-pump-ac-up-to-1500-sq-ft | https://dellahome.com/cdn/shop/files/12K2VRH-19S-JA-I-O_01_pp.jpg?crop=center&height=1200&v=1775200317&width=1200 |

### 36,000 BTU Products

| Product | Product URL | Image URL |
| --- | --- | --- |
| TL Series 36000 BTU SEER2 19 Mini Split Heat Pump AC up to 2500 sq ft | https://dellahome.com/products/tl-series-36000-btu-seer2-19-mini-split-heat-pump-ac-up-to-2500-sq-ft | https://dellahome.com/cdn/shop/files/TL-NEW_8819b5ba-1b5a-4398-af5a-01c9a82d095e.jpg?crop=center&height=1800&v=1753232832&width=1800 |

## 13. Implementation Requirements

Deliverable:

- `index.html` in `C:\Users\18041\Desktop\della-pages\Mini Split Size Guide`

Recommended project files:

- `PRD.md` - this document
- `DESIGN.md` - create only after the final long-page design image is supplied
- `PLAN.md` - create after `PRD.md` and `DESIGN.md` are fixed
- `index.html` - final static demo
- `assets/` - local images/fonts if used

Documentation flow:

1. `PRD.md` now.
   - Defines page purpose, search intent, section order, collection routing, BTU ranges, product-card rules, non-goals, CTA/SEO boundaries, implementation constraints, and product data source rules.
2. `DESIGN.md` after final mockup is supplied.
   - Documents which parts of the mockup should be followed visually, which parts should be overridden by the PRD, Della design tokens, typography, spacing, cards, buttons, tabs, mobile behavior, and mockup-specific corrections.
3. `PLAN.md` after `DESIGN.md`.
   - Becomes the execution checklist for file structure, asset handling, HTML/CSS/JS steps, product data mapping, responsive behavior, QA checklist, validation harness, and follow-up items.

Important:

- Do not create `DESIGN.md` or `PLAN.md` in the first stage unless the user explicitly asks.
- Do not let `DESIGN.md` override `PRD.md`.
- `PRD.md` remains the source of truth for scope, content, product data, SEO, and conversion decisions.
- The design mockup is a visual reference, not a data source.

Technical:

- static HTML with inline CSS and minimal JS is acceptable
- no dependency on Shopify runtime for local review
- avoid relying on Shopify CDN for critical hero/product imagery
- all links should work in the local demo
- layout must be responsive at desktop, tablet, and mobile widths
- allowed lightweight interactions: BTU selector anchor/tab switch behavior, product tabs, FAQ accordions
- disallowed interactions: BTU calculator, input fields, sliders, form submissions, dynamic formula result panels

Future cross-link:

- When a dedicated Mini Split BTU Calculator page exists, this page may include one small cross-link such as `Need a more detailed estimate? Try our Mini Split BTU Calculator.`
- Do not build that calculator into this page.

Accessibility:

- meaningful heading order
- keyboard-accessible accordions/tabs
- visible focus states
- table readable on mobile
- text contrast should meet standard ecommerce readability expectations
- no text overlap at mobile widths

## 14. Validation Harness

Before implementation:

- confirm final section order through grill-me
- confirm whether the first version uses collection cards only or includes PDP-style cards
- confirm whether 36K is shown as a low-emphasis path in merchandising

After implementation:

- open local `index.html` in browser
- inspect desktop viewport around 1440px
- inspect mobile viewport around 390px
- verify no overlap in hero, BTU selector, table, tabs/cards, FAQ
- click every BTU CTA and confirm correct Della collection URL
- verify FAQ accordion and tab/selector interactions
- verify all external links use `target="_blank" rel="noopener"`
- verify page has one H1 and logical H2 sequence
- verify FAQ JSON-LD parses as valid JSON
- verify temporary assets or scratch files are not left in the folder

Pass evidence to report:

- file path of generated HTML
- list of verified viewport sizes
- list of clicked CTA paths
- any unverified Shopify-only behavior

## 15. Risks And Mitigations

Risk: page feels too blog-like.  
Mitigation: keep hero visual and ecommerce-grade, put BTU selector immediately after hero, use Della collection cards early.

Risk: page feels too sales-heavy.  
Mitigation: delay PDP-style product cards until after sizing chart, adjustment factors, room match, and right-sizing guidance; use `View Product`, not `Add To Cart`.

Risk: 36K appears over-promoted despite only one current product.  
Mitigation: keep 36K in selector but downweight in merchandising with an installer confirmation note.

Risk: sizing advice appears too absolute.  
Mitigation: use "starting point" language and include installer/Manual J caveats.

Risk: UI feels AI-generated.  
Mitigation: follow Della design system, avoid generic icons, avoid dashboard calculator hero, use restrained cards and product-led visuals.

Risk: hardcoded product prices become stale.  
Mitigation: capture prices from live product pages or Shopify JSON before implementation, mark them as a dated snapshot, and omit price lines when reliable prices cannot be captured.

Risk: long image design conflicts with PRD strategy.  
Mitigation: Codex should identify conflicts before implementation and ask for a decision instead of copying a problematic section.

Risk: product images load during design review but fail later in a local or Shopify context.  
Mitigation: use the provided URLs for design planning and static demo if acceptable; copy key images locally into `assets/` if reliable local review becomes required.

## 16. Resolved Decisions

- V1 includes PDP-style product cards in the lower `Shop Mini Splits by BTU` merchandising section.
- The earlier hero-adjacent BTU selector remains collection path cards only.
- Product tabs use the pattern from `single-zone-vs-multi-zone-mini-split.html`: tab toolbar, category intro block, product grid.
- Default product tab is `12K`.
- PDP product card CTA is `View Product`.
- Collection path CTA labels are `Shop 9K`, `Shop 12K`, `Shop 18K`, `Shop 24K`, `Shop 36K`.
- Tab-level CTA can use `View All 12K Options` or the matching BTU label.
- Product cards show current sale/current price when reliably captured.
- Compare-at price appears only when reliably captured; otherwise only current price is shown.
- Price display is not a V1 blocker. If reliable current price cannot be captured quickly, omit the price line rather than delaying implementation or inventing a price.
- Product images use the provided Della CDN URLs in V1 unless loading fails or an offline/self-contained handoff is required.
- Hero uses product-led lifestyle visual plus lightweight BTU cue chips, not a calculator dashboard.
- BTU selector, sizing chart, and shop-path copy use Della collection-aligned ranges.
- No multi-zone / whole-home expansion; only one small cross-link to the existing single-zone vs multi-zone guide.
- No interactive BTU calculator in V1.
- Top benefit strip remains a very light one-line strip.
- Premium Della Services reuses the existing service-card section from the single-zone vs multi-zone page.
- FAQ max is 6.
- Mobile BTU selector uses horizontal scroll with scroll-snap.
- `Bigger Is Not Always Better` appears before product tabs.
- `What Changes Your BTU Size?` is a single `Sizing Notes` panel.
- Room-use cards use text links, not filled buttons.
- Current stage creates `PRD.md`, `DESIGN.md`, and `PLAN.md`; no `index.html` until user approval.

## 17. Final Design Mockup Override Notes

The provided design image is:

`C:\Users\18041\Desktop\della-pages\Mini Split Size Guide\ui设计图.png`

Use it as the visual source for composition, hierarchy, rhythm, and section feel. Do not use it as the source for final product data, BTU ranges, pricing, or policy copy.

Specific override rules:

1. BTU ranges in the design image cannot be copied when they conflict with PRD ranges.
   - Do not use visual placeholder ranges such as `250-450`, `450-650`, `650-1,000`, `1,000-1,400`, or `1,400-2,000`.
   - Final HTML must use Della collection-aligned ranges: 9K up to about 400 sq ft, 12K 401-550 sq ft, 18K 551-1,000 sq ft, 24K 1,001-1,500 sq ft, 36K 1,501-2,500 sq ft.
2. Product cards in the design image cannot be copied as product data.
   - Do not use AI placeholder names such as Breeze, Aura, Cassette, or Floor Console unless they match a real PRD product entry.
   - Use only the product titles, product URLs, and image URLs from the PRD product data table.
3. Product section order in the design image must be corrected.
   - If the mockup places product tabs before `Bigger Is Not Always Better`, final HTML still follows PRD order: `Bigger Is Not Always Better` before `Shop Mini Splits by BTU`.
4. Top strip copy in the design image is visual reference only.
   - Do not use uncertain claims such as `2-Year Della Warranty` unless verified separately.
   - Final top strip copy should follow PRD copy or the latest approved copy.
5. Pricing in the design image must not be used.
   - Capture live prices during implementation or omit the price line if reliable capture fails.
6. Visual layout may be followed closely.
   - Preserve the clean navy/blue Della look, wide hero, product-led room visual, BTU selector row, structured chart, lifestyle scenario grid, product tab rhythm, right-size comparison, installer checklist, service cards, and compact FAQ.

## 18. Final Direction

Build this as a Della-branded **BTU decision guide**:

- content-first enough to rank and satisfy research intent
- conversion-focused enough to work as a paid landing page
- ecommerce-native enough to feel like Della
- restrained enough to avoid hard-sell friction

The first implementation should prioritize:

1. BTU selector
2. sizing chart
3. adjustment factors
4. room-use matcher
5. right-sizing guidance
6. product tabs with real PRD product data
7. installer confidence
8. service confidence and FAQ

PDP-style cards are required in the lower merchandising section for V1, but they should not dominate the page or appear before the sizing decision flow.
