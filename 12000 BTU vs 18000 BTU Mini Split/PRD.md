# 12000 BTU vs 18000 BTU Mini Split Landing Page PRD

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

Approved visual target: `C:\Users\18041\.codex\generated_images\01a08f7c-0b7f-7bc2-91fc-5cf47de38e45\exec-2910a291-f6e0-4c39-998d-abcb6ca89f09.png`.

- The capacity section uses one architectural room panorama above a light-blue comparison band with equal 12K/18K actions, area references and conditional room guidance. Both actions jump to the corresponding product group.
- The factors section places a room-detail photograph beside five tabs: Sun, Layout, Insulation, Ceiling and Heat load. Each tab changes its explanation and the matching spatial annotation. Room area is covered with connected layout. Sun is initially active.
- Tabs expose tab/tablist/tabpanel semantics with arrow, Home and End navigation. Without JavaScript, all explanations are visible and inactive controls are hidden.
- Right-sizing guidance uses a navy living-room background with the owner-requested blue airflow effect and a white button leading to products. On narrow mobile, the scene sits above the copy and button.
- Scene images are generated illustrations, not evidence of installed capacity or model specifications. Original product cards and their data remain unchanged.
- Current order: hero, capacity comparison, sizing factors, right-sizing banner, products, services, FAQ, bottom collections. Mobile product-stage shopping bar remains available.
- Implementation follows the approved combined visual direction. Site publishing and shared-component rollout are not requested.

Status: implemented; information-hierarchy pilot verified 2026-09-11
Page type: Della topical decision page + paid landing page
Audience: United States Della shoppers comparing 12K vs 18K mini splits before browsing products

## Objective

Create a Della landing page that helps shoppers decide whether to begin with 12000 BTU or 18000 BTU mini splits. The page should serve research-driven SEO traffic and paid ad traffic without becoming a technical sizing calculator or a SKU-first product listing.

The page should answer one practical buying question: when is 12K likely enough, and when is 18K worth checking?

## Primary Conversion Paths

Primary CTAs route to collections:

- Shop 12000 BTU Mini Splits: https://dellahome.com/collections/12000-btu-mini-split
- Shop 18000 BTU Mini Splits: https://dellahome.com/collections/18000-btu-mini-split

PDPs are secondary. Product cards later in the page use `View Product` and route to the locked PDP URLs in the product manifest.

All same-site Della collection and PDP links open in the same tab. Do not use `target="_blank"` for Della links.

## Strategic Positioning

The page must not imply that shoppers should automatically size up to 18K. It should balance both paths:

- 12K can be the better place to start for enclosed bedrooms, offices, and smaller living areas.
- 18K is worth checking for larger rooms, open layouts, garages, sunrooms, higher ceilings, stronger sun, and higher heat load.

Use conservative sizing language. Do not make guaranteed coverage, comfort, efficiency, bill savings, or installation claims.

## SEO Requirements

H1:

`12000 BTU vs 18000 BTU Mini Split: When to Size Up`

SEO title:

- If Shopify automatically appends the brand: use the H1 as the title.
- If Shopify does not append the brand: `12000 BTU vs 18000 BTU Mini Split: When to Size Up | Della`

Meta description:

`Compare 12K vs 18K Della mini splits by room size, layout, insulation, sun exposure, and heat load. Learn when to size up.`

SEO constraints:

- Do not add canonical until the final Shopify URL is confirmed.
- Do not add breadcrumb markup.
- Do not add FAQPage JSON-LD for this draft.
- Do not add OG/social metadata for this draft.
- Do not cite or link external sources on the front-end page.

## Content Guardrails

Use natural American English. Tone should be about 70% expert judgment and 30% ecommerce guidance: credible, clear, friendly, and close to shopper language.

Required sizing disclaimer concept:

`Actual sizing depends on insulation, ceiling height, sun exposure, climate, room layout, and heat load. Confirm final sizing with a qualified installer.`

Avoid repeating `starting point` mechanically. Prefer varied wording such as `common reference`, `practical fit`, `worth checking`, and `may move the choice toward 12K or 18K`.

Do not build a calculator. No square-footage input, no dynamic BTU output, and no false precision.

## Required Page Order

1. Hero with 12K and 18K collection paths
2. Choose 12K if / Choose 18K if
3. Light sizing note
4. Sizing factors
5. 12K vs 18K comparison table
6. Bigger Is Not Always Better
7. Recommended 12000 BTU and 18000 BTU products
8. Room scenarios
9. Premium Della Services, copied from the single-zone reference page
10. FAQ
11. Bottom CTA with two collection path cards
12. Mobile-only sticky bottom CTA

## Section Requirements

### Hero

Use a light blue Della ecommerce banner feel, not a dark SaaS card and not a fake AI product mockup.

Hero left:

- H1: `12000 BTU vs 18000 BTU Mini Split: When to Size Up`
- Hero short copy: `Trying to avoid a mini split that feels too weak or too big? Compare 12K vs 18K by room size, layout, sun, and heat load before you shop.`
- Hero should not include an eyebrow label above the H1.
- Do not place an extra helper sentence under the hero CTA buttons.
- Two primary CTAs: `Shop 12000 BTU Mini Splits` and `Shop 18000 BTU Mini Splits`

Hero right:

- Hero 12K card copy: `For bedrooms, offices, and enclosed rooms where right-sized comfort beats extra capacity.`
- Hero 18K card copy: `For larger, sunnier, or more open spaces where 12K may have to work too hard.`
- Use real product imagery from the locked 8-product manifest.
- Hero 12K representative product: DELLA Optima Series 12000 BTU 24 SEER2 Ultra Heat Mini Split AC.
- Hero image source override: use local file `12k.webp` supplied in the project folder.
- Hero 18K representative product: DELLA Serena Series 18000 BTU 22 SEER2 Mini Split Heat Pump AC.
- Hero image source override: use local file `18k.webp` supplied in the project folder.
- Build a side-by-side 12K vs 18K visual.
- Add clear `12K` and `18K` labels.
- Do not use AI-generated product imagery.
- Do not copy a full Shopify nav/header into the hero.

### Choose Cards

Use two cards with five bullets each.

12K card bullets:

- Up to 550 sq. ft. as a common reference
- Enclosed single room
- Bedroom, office, or small living area
- Standard ceiling height
- Moderate sun and heat load

18K card bullets:

- Up to 1,000 sq. ft. as a common reference
- Larger or more open space
- Garage, sunroom, or open living area
- Higher ceiling
- Stronger sun exposure or higher heat load

### Light Sizing Note

Use one short note, no chips:

`Most rooms are not decided by square footage alone. Layout, insulation, sun exposure, ceiling height, and heat load can move the choice toward 12K or 18K.`

### Sizing Factors

Keep six cards. Use this copy:

| Factor | Copy | Tag |
| --- | --- | --- |
| Room Size | Larger rooms usually need more capacity. | May push toward 18K |
| Insulation | Better insulation can reduce cooling/heating demand. | May support 12K |
| Sun Exposure | Direct sun can increase heat gain. | May push toward 18K |
| Ceiling Height | Higher ceilings add air volume. | May push toward 18K |
| Open Layout | Open spaces may need more capacity than enclosed rooms. | May push toward 18K |
| Heat Load | Appliances, people, garages, and kitchens add load. | Needs installer review |

### Comparison Table

Keep exactly six rows. Do not turn the table into a technical encyclopedia or SKU table. Do not include price, SEER2, model names, installation quotes, or product images in this table.

Rows:

1. Best room-size reference
2. Common spaces
3. When it commonly fits
4. What to check
5. Install planning
6. Best next step

The table compares buying-path logic, not guaranteed performance.

Mobile behavior: on mobile, convert the 12K vs 18K comparison table into stacked comparison cards. Do not use a horizontally scrolling table.

### Bigger Is Not Always Better

Required heading:

`Bigger Is Not Always Better`

Required copy:

`A higher BTU rating does not automatically mean better comfort or lower bills. Proper sizing helps balance comfort, efficiency, runtime, and humidity control.`

CTA: `Learn About Sizing`, anchored back to sizing factors.

Right-side visual comparison:

Right-sized comfort:

- Even, steady comfort
- Better humidity control
- Efficient operation
- More consistent temps
- Longer system life

Oversized system risk:

- Short cycling
- Higher humidity
- Uneven comfort
- More wear and tear
- Higher costs

Do not frame these risks as `18K problems`. Frame them as oversized-system risks.

### Product Sections

Use two stacked visible groups. Do not use tabs.

Group 1:

- Section title: `12000 BTU Mini Splits`
- Heading: `Shop 12K Mini Splits for Smaller Rooms`
- Copy: `Best for enclosed bedrooms, offices, and smaller living areas where one room needs dedicated comfort.`
- Four locked product cards
- CTA: `Shop All 12000 BTU Mini Splits`

Group 2:

- Section title: `18000 BTU Mini Splits`
- Heading: `Shop 18K Mini Splits for Larger Spaces`
- Copy: `Best for larger rooms, open layouts, garages, sunrooms, and spaces with more heat load.`
- Four locked product cards
- CTA: `Shop All 18000 BTU Mini Splits`

Product card rules:

- Show image, product title, spec chips, live selling price, and `View Product` CTA.
- Do not show compare-at price, strikethrough price, sale badge, coupon, countdown, discount percent, or `Price shown in Shopify` copy.
- If a product is sold out, keep the card, keep `View Product`, do not add a sold-out badge, and do not replace the SKU.
- If any locked PDP is inaccessible, live price cannot be parsed, or image URL is unavailable, stop final HTML generation and output a missing-items list.
- Live price verification evidence must include `verified_at` timestamp because standalone HTML prices are static snapshots.

Spec chip rules:

- Use actual specs only.
- Preferred order: BTU, SEER2, coverage.
- Optional fourth chip only when clearly supported by title/PDP, such as `Ultra Heat`, `Cloud Air`, or `Heat Pump`.
- Do not invent coverage chips when coverage is not verified.
- Front-end coverage chip format must be `Up to 550 sq. ft.` or `Up to 1,000 sq. ft.`.
- Keep chips as separate items in the approved order. Do not merge them into one sentence.

### Product Manifest

The eight products are locked. Do not auto-fill from collection pages. Do not replace products.

| Group | Product title for planning | PDP URL | Image URL | Planned spec chips | Live price source | Collection CTA URL |
| --- | --- | --- | --- | --- | --- | --- |
| 12K | DELLA Optima Series 12000 BTU 24 SEER2 Ultra Heat Mini Split AC | https://dellahome.com/products/optima-series-12000-btu-seer2-24-ultra-heat-mini-split-ac-up-to-550-sq-ft | https://dellahome.com/cdn/shop/files/TP_6a7b63f4-9ce7-4af4-9b4a-a56873b66147.jpg?crop=center&height=1800&v=1764061301&width=1800 | 12000 BTU; 24 SEER2; Up to 550 sq. ft.; Ultra Heat | PDP live price or Shopify product JSON | https://dellahome.com/collections/12000-btu-mini-split |
| 12K | DELLA Vario Series 12000 BTU 23 SEER2 Mini Split Heat Pump AC | https://dellahome.com/products/vario-series-12000-btu-seer2-23-mini-split-heat-pump-ac-up-to-550-sq-ft | https://dellahome.com/cdn/shop/files/TL-NEW_8819b5ba-1b5a-4398-af5a-01c9a82d095e.jpg?crop=center&height=1200&v=1753232832&width=1200 | 12000 BTU; 23 SEER2; Up to 550 sq. ft.; Heat Pump | PDP live price or Shopify product JSON | https://dellahome.com/collections/12000-btu-mini-split |
| 12K | DELLA Umbra Series 12000 BTU 17 SEER2 Mini Split Heat Pump AC | https://dellahome.com/products/umbra-series-12000btu-seer2-17-mini-split-heat-pump-ac | https://dellahome.com/cdn/shop/files/JPB.jpg?crop=center&height=1200&v=1731029992&width=1200 | 12000 BTU; 17 SEER2; Heat Pump; coverage only if verified | PDP live price or Shopify product JSON | https://dellahome.com/collections/12000-btu-mini-split |
| 12K | DELLA Serena Cloud Air Series 12000 BTU 22 SEER2 Mini Split Heat Pump AC | https://dellahome.com/products/della-serena-cloud-air-series-12000-btu-22-seer2-mini-split-heat-pump-ac-up-to-550-sq-ft | https://dellahome.com/cdn/shop/files/9K1VR-22S-MX-I-O_01.jpg?crop=center&height=1200&v=1776763354&width=1200 | 12000 BTU; 22 SEER2; Up to 550 sq. ft.; Cloud Air | PDP live price or Shopify product JSON | https://dellahome.com/collections/12000-btu-mini-split |
| 18K | DELLA Serena Series 18000 BTU 22 SEER2 Mini Split Heat Pump AC | https://dellahome.com/products/serena-series-18000-btu-seer2-22-mini-split-heat-pump-ac-up-to-1000-sq-ft | https://dellahome.com/cdn/shop/files/M.jpg?crop=center&height=1200&v=1750938870&width=1200 | 18000 BTU; 22 SEER2; Up to 1,000 sq. ft.; Heat Pump | PDP live price or Shopify product JSON | https://dellahome.com/collections/18000-btu-mini-split |
| 18K | DELLA Vario Series 18000 BTU 21 SEER2 Mini Split Heat Pump AC | https://dellahome.com/products/vario-series-18000-btu-seer2-21-mini-split-heat-pump-ac-up-to-1000-sq-ft | https://dellahome.com/cdn/shop/files/TL-NEW_8819b5ba-1b5a-4398-af5a-01c9a82d095e.jpg?crop=center&height=1800&v=1753232832&width=1800 | 18000 BTU; 21 SEER2; Up to 1,000 sq. ft.; Heat Pump | PDP live price or Shopify product JSON | https://dellahome.com/collections/18000-btu-mini-split |
| 18K | DELLA Umbra Series 18000 BTU 19 SEER2 Mini Split Heat Pump AC | https://dellahome.com/products/umbra-series-18000btu-seer2-19-mini-split-heat-pump-ac | https://dellahome.com/cdn/shop/files/JPB.jpg?crop=center&height=1800&v=1731029992&width=1800 | 18000 BTU; 19 SEER2; Heat Pump; coverage only if verified | PDP live price or Shopify product JSON | https://dellahome.com/collections/18000-btu-mini-split |
| 18K | DELLA Serena Cloud Air Series 18000 BTU 22 SEER2 Mini Split Heat Pump AC | https://dellahome.com/products/della-serena-cloud-air-series-18000-btu-22-seer2-mini-split-heat-pump-ac-up-to-1000-sq-ft | https://dellahome.com/cdn/shop/files/9K1VR-22S-MX-I-O_01.jpg?crop=center&height=1800&v=1776763354&width=1800 | 18000 BTU; 22 SEER2; Up to 1,000 sq. ft.; Cloud Air | PDP live price or Shopify product JSON | https://dellahome.com/collections/18000-btu-mini-split |

### Room Scenarios

Use exactly four scenario cards. Each card must include a real lifestyle image. If no perfect local Della lifestyle image exists, use the closest credible Della-owned image from existing local pages.

Before final HTML build, produce a scenario image map with the four image URLs or local asset paths and get approval. Do not silently choose weak lifestyle images in the final page.

| Scenario | Direction label |
| --- | --- |
| Bedroom or home office | 12K starting point |
| Small living room | 12K or 18K based on layout |
| Garage or sunroom | Check 18K |
| Open living and dining area | 18K starting point |

Do not expand beyond these four scenarios.

### Premium Della Services

Copy the Premium Della Services section directly from:

`C:\Users\18041\Desktop\della-pages\single-zone-vs-multi-zone-mini-split\single-zone-vs-multi-zone-mini-split.html`

Use the same section structure, text, visual treatment, and icon URLs. Do not rewrite this section for the first implementation pass.

Required copied content includes:

- Section label: `Service confidence`
- Heading: `Premium Della Services`
- `Free & Fast Shipping`
- `Pay in 6 Months, 0% APR`
- `24x7 Live Chat Support`
- `Lifetime Coverage (Mini Splits)`

### FAQ

Use five high-value pre-purchase FAQs with these exact short answers as the implementation source. Do not add FAQ schema.

1. `Is 12,000 BTU or 18,000 BTU better for my room?`

   It depends on the room, not just the BTU number. A 12,000 BTU mini split is usually a better fit for smaller enclosed rooms, while 18,000 BTU is worth checking for larger, more open, sunnier, or higher-load spaces. Use this page as a buying guide and confirm final sizing with a qualified installer.

2. `How many square feet can a 12,000 BTU mini split cover?`

   Della 12,000 BTU models are commonly referenced for enclosed rooms up to 550 sq. ft. Actual fit depends on insulation, ceiling height, sun exposure, climate, layout, and heat load. If the room is open, very sunny, or used as a garage or sunroom, check the sizing factors before choosing.

3. `How many square feet can an 18,000 BTU mini split cover?`

   Della 18,000 BTU models are commonly referenced for larger or more open rooms up to 1,000 sq. ft. That does not mean every 1,000 sq. ft. space is the right fit. High ceilings, poor insulation, strong sun, and heat-producing appliances can change the load.

4. `Will an 18K mini split cool faster than a 12K?`

   Not necessarily in the way that matters. A larger system may change the room temperature quickly, but comfort depends on proper sizing, steady runtime, humidity control, and room conditions. If the room is smaller and enclosed, 12K may be the more appropriate path; if it is larger, open, sunny, or high-load, 18K is worth checking.

5. `Should I choose 18K for a garage, sunroom, or open living area?`

   It is worth checking 18K for garages, sunrooms, and open living areas because those spaces often have more sun exposure, air volume, or heat load. That does not mean 18K is automatically enough or always the right choice. Confirm final sizing with a qualified installer, especially for garages and sunrooms.
### Bottom CTA

Use two collection path cards and no extra global note.

12K card:

- CTA: `Shop 12000 BTU Mini Splits`
- Positioning line: `For bedrooms, offices, and smaller enclosed rooms.`

18K card:

- CTA: `Shop 18000 BTU Mini Splits`
- Positioning line: `For larger rooms, open layouts, garages, and sunrooms.`

### Mobile Sticky CTA

Add mobile-only sticky bottom CTA. Do not show on desktop.

- Button 1: `Shop 12K`
- Button 2: `Shop 18K`
- Height: 56 to 64 px
- Add page-bottom padding so sticky CTA does not cover FAQ, services, or bottom CTA content.
- No popup, no discount bar, no email capture.

## Non-Goals

- No full BTU calculator.
- No product auto-fill from collection pages.
- No dynamic tabbed product module.
- No full Shopify header or footer.
- No top benefit strip in this version.
- No breadcrumb.
- No canonical yet.
- No FAQ schema.
- No external citation block.
- No fake AI product imagery.
- No sale mechanics unless Della specifically confirms them in live data and the user approves.

## Acceptance Criteria

- Page clearly routes shoppers to 12K and 18K collections before PDPs.
- Product section uses exactly the eight locked PDPs in the manifest.
- Live selling price is displayed for each product, or implementation stops with a missing-items list.
- Coverage copy is conservative and avoids guarantees.
- Bigger Is Not Always Better educates on right-sizing without making 18K feel negative.
- Premium Della Services is copied from the single-zone reference page.
- Mobile sticky CTA appears only on mobile and does not cover content.
- All same-site Della links open in the same tab.
- No placeholders, fake prices, fake reviews, fake badges, or unverified claims remain in the final HTML.

## Pending Implementation Inputs To Verify

These are not blocking this PRD, but must be checked before final HTML generation:

- Live selling price for all eight PDPs.
- PDP accessibility for all eight URLs.
- Image accessibility for all eight CDN URLs.
- Lifestyle image selections for the four scenario cards.
- Whether Shopify automatically appends `Della` to SEO titles.
- Final Shopify URL, before adding canonical in any later version.







