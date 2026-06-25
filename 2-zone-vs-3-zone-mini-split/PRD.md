# PRD: 2-Zone vs 3-Zone Mini Split Landing Page

## Page Summary

Create a Della topical decision landing page for `2-Zone vs 3-Zone Mini Split`.

This page is a research-led decision page plus ecommerce guide. It is not a blog article and not a duplicated collection page. The visitor already has multi-zone intent and is blocked on whether two indoor heads are enough, whether the third room needs independent control, how BTU mix affects the choice, and whether buying a 2-zone system can be expanded later.

## Page Type

- Primary type: Comparison guide
- Secondary type: Collection-support page
- Funnel role: SEO research traffic plus paid ad landing page
- Commercial intensity: Medium-high. Product cards should appear early, after the quick decision framework.

## Primary User Decision

Help the visitor decide:

- Choose 2-zone when two enclosed rooms need separate comfort from one outdoor unit.
- Choose 3-zone when three rooms or areas need their own indoor units, schedules, and temperature control.
- Do not buy a third head by default. More zones are useful only when the room count, BTU mix, and install route justify the added equipment.

## Target URLs

Primary collection routes:

- 2-Zone Mini Split: https://dellahome.com/collections/2-zone-mini-split
- 3-Zone Mini Split: https://dellahome.com/collections/3-zone-mini-split

Secondary route:

- Multi-Zone Mini Split: https://dellahome.com/collections/mini-split-multi-zone

Suggested page slug:

- `2-zone-vs-3-zone-mini-split`

## SEO Targets

SEO title:

`2-Zone vs 3-Zone Mini Split: Which Setup Fits Your Home?`

Meta description:

`Compare 2-zone vs 3-zone mini splits by room count, BTU mix, layout, and install path. Shop Della 2-zone and 3-zone systems.`

H1:

`2-Zone vs 3-Zone Mini Split`

Primary intent:

- Compare 2-zone vs 3-zone mini split systems.
- Route users to the correct Della collection.
- Avoid competing directly with the collection pages for pure `2 zone mini split` and `3 zone mini split` intent.

## Design System Requirements

Use Della topical PageFly / Memorial / coupon-code visual language:

- Heading and product-title font: Spectral, fallback Georgia, serif.
- Body, button, tab, and table font: Poppins, fallback Arial, sans-serif.
- Navy: `#0E1953`.
- Brand blue: `#5884E7`.
- Hover blue: `#6B95EF`.
- Light surfaces: `#EDF2FF`, `#F4F7FF`, `#DDF7FF`.
- Buttons: 4px radius, ecommerce style, not pill-shaped.
- Product cards: image, title, optional rating, optional live price, spec chips, `View Product` CTA.
- Hero: wide ecommerce banner, not a blog header and not a SaaS dashboard.

Reference sources:

- `C:\Users\18041\Desktop\della-pages\page.pf-ef33e2e6.json.txt`
- `C:\Users\18041\Desktop\della-pages\pf-ef33e2e6.liquid.txt`
- `C:\Users\18041\Desktop\della-pages\della-memorial-day-design-system.md`
- `https://dellahome.com/pages/coupon-code`
- Local comparison references in `C:\Users\18041\Desktop\della-pages`

## Approved Section Order

1. Hero wide ecommerce banner
2. Room-count path strip
3. Quick Answer two decision cards
4. Product merchandising tabs
5. Scenario cards
6. More Zones Is Not Always Better
7. 2-Zone vs 3-Zone comparison table
8. Premium Della Services
9. FAQ with FAQPage JSON-LD
10. Bottom CTA collection path cards

## Explicitly Removed Sections

Do not include a top Benefit Strip.

Removed copy:

- Free and Fast Shipping
- 24x7 Live Chat Support
- Lifetime Coverage (Mini Splits)
- Find Partner HVAC Installer

Do not include a standalone Install Planning Band.

Removed scope:

- Line-set route checklist
- Drainage checklist
- Electrical checklist
- Outdoor unit placement checklist
- Indoor unit placement checklist
- Installer quote checklist
- Installer / rebate / product CTA band

Installation concerns may be mentioned briefly inside the comparison table or FAQ only when needed to explain the 2-zone vs 3-zone decision.

## Section Requirements

### 1. Hero Wide Ecommerce Banner

H1:

`2-Zone vs 3-Zone Mini Split`

Hero copy:

`Choose a 2-zone mini split when two rooms need separate comfort from one outdoor unit. Choose a 3-zone mini split when three rooms or areas need their own indoor units, schedules, and temperature control.`

Primary CTAs:

- `Shop 2-Zone Mini Splits` -> https://dellahome.com/collections/2-zone-mini-split
- `Shop 3-Zone Mini Splits` -> https://dellahome.com/collections/3-zone-mini-split

Visual direction:

- Wide banner with left copy space and right product/room visual.
- Preferred visual concept: one outdoor unit to two indoor heads vs one outdoor unit to three indoor heads.
- No fake discount badge, countdown, coupon code, or sale styling.

### 2. Room-Count Path Strip

Use compact routing cards or strip items:

- `2 Rooms / 2-Zone` -> 2-zone collection
- `3 Rooms / 3-Zone` -> 3-zone collection
- `More than 3 rooms / View Multi-Zone` -> multi-zone collection

The strip should narrow the choice instead of showing equal 1-5 zone paths.

### 3. Quick Answer Two Decision Cards

H2:

`Choose 2-Zone or 3-Zone by the rooms that need their own indoor unit`

2-zone card heading:

`Start with 2-Zone if...`

2-zone cues:

- Two enclosed rooms need separate comfort.
- Common for two bedrooms, a bedroom plus office, or an addition plus nearby room.
- The third area is a hallway, open pass-through, or rarely used room.
- You want fewer indoor units, fewer line-set routes, and a simpler starting point.
- One room may need a larger indoor unit, so compare BTU mix before choosing.

3-zone card heading:

`Start with 3-Zone if...`

3-zone cues:

- Three rooms need their own indoor units.
- Common for a whole upstairs, three bedrooms, or bedroom plus office plus living area.
- Rooms are used on different schedules.
- One outdoor unit is preferred over multiple outdoor condensers.
- The installer can route lines, drains, and power cleanly to all three indoor units.

### 4. Product Merchandising Tabs

H2:

`Shop Della 2-Zone and 3-Zone Mini Splits`

Tabs:

- `2-Zone Systems`
- `3-Zone Systems`

Rules:

- Show four products per tab.
- Use user-specified products only.
- Product CTA: `View Product`.
- Do not use `Add to Cart`.
- Price is required. Capture current live Shopify price during implementation. Never hard-code guessed or stale prices.
- Rating is optional. If used, capture from live Shopify or omit.
- Include concise spec chips: zone count, BTU/head mix, coverage, series or installation type.

### 5. Scenario Cards

H2:

`Which home setup sounds closest to yours?`

Cards:

- `Two bedrooms on the same floor` -> Start with 2-Zone
- `Bedroom + home office` -> Start with 2-Zone
- `Addition + nearby room` -> Start with 2-Zone
- `Three upstairs bedrooms` -> Start with 3-Zone
- `Primary bedroom + nursery + office` -> Start with 3-Zone
- `Open living area + two rooms` -> Check 3-Zone and BTU mix

Use realistic room combinations, not abstract HVAC concepts.

### 6. More Zones Is Not Always Better

H2:

`More zones do not automatically mean better comfort`

Core copy:

`A 3-zone mini split gives you one more indoor unit, but the right choice still depends on the BTU mix, room load, and install route. A stronger 2-zone setup may fit two rooms better than a smaller 3-zone setup spread across rooms that do not need separate control.`

Subpoints:

- `Count rooms first`: Each room that needs its own temperature usually needs its own indoor unit.
- `Then check BTU mix`: A 9K + 9K system and a 12K + 18K system solve different problems.
- `Do not buy a third head just in case`: Adding a zone later depends on whether the outdoor unit supports more heads, has enough capacity, and has available connection ports.

### 7. Comparison Table

H2:

`2-Zone vs 3-Zone Mini Split Comparison`

Columns:

- Compare
- 2-Zone Mini Split
- 3-Zone Mini Split

Rows:

- Best starting point
- Indoor units
- Common home patterns
- BTU planning
- Install complexity
- When not to choose
- Next step

Use short table cells. Do not include winner badges.

### 8. Premium Della Services

Keep a compact four-card Della service confidence block near the bottom.

Approved service-card direction:

- `Free & Fast Shipping`
- `24x7 Live Chat Support`
- `Lifetime Coverage (Mini Splits)`
- `Warranty Registration`

Do not make this a top-page benefit strip.

Do not include `Find Partner HVAC Installer` in Premium Della Services.

Avoid unverified financing claims unless approved later.

### 9. FAQ

H2:

`2-Zone vs 3-Zone Mini Split Questions`

FAQ items, limited to five high-value pre-purchase questions:

1. `Is a 2-zone or 3-zone mini split better for my home?`
2. `Can a 2-zone mini split cool three rooms?`
3. `Can I add a third zone later?`
4. `Does each room get its own temperature setting?`
5. `How do I choose the right BTU mix for a 2-zone or 3-zone mini split?`

Add FAQPage JSON-LD only when visible FAQ copy is final. JSON-LD must match visible FAQ content.

### 10. Bottom CTA

Use two collection path cards:

2-Zone Mini Splits:

`For two rooms that need separate comfort from one outdoor unit.`

CTA: `Shop 2-Zone`

3-Zone Mini Splits:

`For three rooms that need dedicated indoor units and separate comfort settings.`

CTA: `Shop 3-Zone`

No secondary multi-zone text link in the bottom CTA after user correction. Keep this section focused on the two main collection choices.

## Product Data

### 2-Zone Mini Split Products

| Role | Product | URL | Image | Key chips |
| --- | --- | --- | --- | --- |
| Common two rooms | DELLA Vario Series 20000 BTU Dual Zone Mini Split AC (9K + 9K) - Up To 800 Sq.Ft. | https://dellahome.com/products/vario-series-20000-btu-dual-zone-mini-split-ac-9k-9k-up-to-800-sq-ft | https://dellahome.com/cdn/shop/files/1D2-TL_D99_fecce979-0aa5-40ed-a7bb-65d0c80a6b23.jpg?crop=center&height=1200&v=1780905223&width=1200 | 2-zone; 20K BTU; 9K + 9K; up to 800 sq ft; Vario |
| Bedroom + office | DELLA Optima Series 18000 BTU Dual Zone Mini Split AC (9K + 12K) - Up To 950 Sq.Ft. | https://dellahome.com/products/optima-series-18000-btu-dual-zone-mini-split-ac-9k-12k-up-to-950-sq-ft | https://dellahome.com/cdn/shop/files/1D2-TP_D912-A_028f88a1-a3e8-4512-bc8f-e444dcd291ff.jpg?crop=center&height=1800&v=1780969812&width=1800 | 2-zone; 18K BTU; 9K + 12K; up to 950 sq ft; Optima |
| Balanced two rooms | DELLA Optima Series 18000 BTU Dual Zone Mini Split AC (12K + 12K) - Up To 1100 Sq.Ft. | https://dellahome.com/products/optima-series-18000-btu-dual-zone-mini-split-ac-12k-12k-up-to-1100-sq-ft | https://dellahome.com/cdn/shop/files/1D2-TP_D99-A_95d1424f-8db4-46bb-b79a-7828c384a92d.jpg?crop=center&height=1200&v=1780969806&width=1200 | 2-zone; 18K BTU; 12K + 12K; up to 1100 sq ft; Optima |
| Mixed load | DELLA Vario Series 28000 BTU Dual Zone Mini Split AC (12K + 18K) - Up To 1550 Sq.Ft. | https://dellahome.com/products/vario-series-28000-btu-dual-zone-mini-split-ac-12k-18k-up-to-1550-sq-ft | https://dellahome.com/cdn/shop/files/1D3-TL_D1218_99d7dd07-21fc-47a2-9e71-e6bea06a920c.jpg?crop=center&height=1200&v=1780905210&width=1200 | 2-zone; 28K BTU; 12K + 18K; up to 1550 sq ft; Vario |

### 3-Zone Mini Split Products

| Role | Product | URL | Image | Key chips |
| --- | --- | --- | --- | --- |
| Balanced three rooms | DELLA Vario Series 28000 BTU Tri Zone Mini Split AC (9K + 9K + 12K) - Up To 1350 Sq.Ft. | https://dellahome.com/products/vario-series-28000-btu-tri-zone-mini-split-ac-9k-9k-12k-up-to-1350-sq-ft | https://dellahome.com/cdn/shop/files/1D3-TL_T9912_0597eaf3-1189-496d-8194-bec1e7fa6ad5.jpg?crop=center&height=1200&v=1780905188&width=1200 | 3-zone; 28K BTU; 9K + 9K + 12K; up to 1350 sq ft; Vario |
| Two small + one medium | DELLA Optima Series 27000 BTU Tri Zone Mini Split AC (9K + 12K + 12K) - Up To 1500 Sq.Ft. | https://dellahome.com/products/optima-series-27000-btu-tri-zone-mini-split-ac-9k-12k-12k-up-to-1500-sq-ft | https://dellahome.com/cdn/shop/files/1D3-TP_T91212-A_354d6f97-48da-4f26-b828-5855053cf9bc.jpg?crop=center&height=1200&v=1780969716&width=1200 | 3-zone; 27K BTU; 9K + 12K + 12K; up to 1500 sq ft; Optima |
| Mixed load | DELLA Vario Series 35000 BTU Tri Zone Mini Split AC (9K + 12K + 18K) - Up To 1950 Sq.Ft. | https://dellahome.com/products/vario-series-35000-btu-tri-zone-mini-split-ac-9k-12k-18k-up-to-1950-sq-ft | https://dellahome.com/cdn/shop/files/1D4-TL_T91218_dda038b5-09e6-4c86-ac87-97e951c563c0.jpg?crop=center&height=1800&v=1780905173&width=1800 | 3-zone; 35K BTU; 9K + 12K + 18K; up to 1950 sq ft; Vario |
| Ceiling cassette option | DELLA 35000 BTU Tri Zone Ceiling Cassette Mini Split AC (12K + 12K + 18K) - Up To 2100 Sq.Ft. | https://dellahome.com/products/35000-btu-tri-zone-ceiling-cassette-mini-split-ac-12k-12k-18k-up-to-2100-sq-ft | https://dellahome.com/cdn/shop/files/1D4-CC_T_50f4d111-bdfd-4748-af4a-f6c648c28d6b.jpg?crop=center&height=1200&v=1755745046&width=1200 | 3-zone; 35K BTU; 12K + 12K + 18K; up to 2100 sq ft; ceiling cassette |

## Product Data Rules

- Product identity is user-specified and should not be replaced by AI mockup output.
- Product prices are required. Capture current live prices from Shopify during implementation.
- If a live price cannot be verified, stop and ask before omitting price or using a stale value.
- Compare-at prices, sale badges, coupon labels, and discount claims must not be invented.
- Product ratings should be live-captured or omitted.
- If a product becomes unavailable before implementation, stop and ask before substituting.

## Non-Goals

- Do not create a long blog-style article.
- Do not copy the full collection page.
- Do not include a top benefit strip.
- Do not include a standalone install planning band.
- Do not add a calculator unless explicitly requested.
- Do not use `Add to Cart` CTAs.
- Do not use fake promo, coupon, sale, countdown, or financing claims.
- Do not over-merchandise 4-zone or 5-zone paths.

## Verification Harness For Later Implementation

Behavior to prove:

- Page routes users clearly to 2-zone and 3-zone collections.
- Product tabs show exactly the approved 4 products per zone group.
- Product cards show live-verified prices.
- Removed sections do not appear.
- Mobile view has no horizontal overflow, overlapping text, or cramped product cards.
- FAQ schema matches visible FAQ content.
- External Della links use approved URLs.

Evidence to collect:

- Desktop screenshot around 1280px.
- Mobile screenshots around 390px and 430px.
- Browser click checks for hero CTAs, path strip, product card CTAs, tabs, FAQ, and bottom CTA.
- DOM or source inspection for FAQPage JSON-LD.
- Product URL and image URL comparison against this PRD.

Pass criteria:

- Visual style matches Della/PageFly topical ecommerce language.
- No blog-style opening or generic SaaS dashboard styling.
- No removed benefit strip or install planning band.
- Live product prices are present and verified.
- No fake prices, sale claims, or unapproved financing claims.
- Each tab contains only approved products.
- CTA labels match the page's decision-guide role.

Failure cases to reject:

- Product cards use `Add to Cart`.
- Product prices are missing, guessed, or stale.
- Page includes the removed top benefit strip.
- Page includes the removed install planning band.
- Product data is invented or substituted without approval.
- Mobile layout hides or overlaps CTA/product text.

## Resolved Decisions

1. Final implementation mode for the next build step: create a standalone HTML demo first, then decide PageFly or Shopify custom liquid after visual review.
2. Next step: create `GEMINI_DESIGN_PROMPT.md` before HTML implementation.
3. Hero asset: create a new Della-style 2-head vs 3-head visual instead of relying only on a generic room image.
4. Product prices: required. Capture live prices from Shopify during implementation.
5. Product ratings: use only if they can be captured reliably from live pages; otherwise omit ratings.
6. Product order: keep the PRD order fixed.
7. Product tabs: default to `2-Zone Systems`.
8. Room-count strip: do not expose separate 4-zone or 5-zone cards; use one secondary multi-zone route.
9. Premium Della Services: keep near the bottom, but do not include `Find Partner HVAC Installer`.
10. Installation complexity: may be mentioned briefly in table or FAQ, but no standalone Install Planning Band.
11. Expansion-later copy: answer conservatively and tie it to outdoor-unit support, capacity, and available ports.
12. No BTU calculator or interactive quiz in V1.
13. Scenario cards may include light text-link CTAs, not heavy repeated buttons.
14. FAQ count: exactly five high-value pre-purchase questions.
15. FAQPage JSON-LD: add only after visible FAQ copy is final and keep it identical to the visible FAQ.
16. Canonical: omit in standalone demo until final Shopify URL is confirmed.
17. Product and collection links: same-tab in Shopify implementation; demo may use new-tab links for review convenience.
18. Sale, coupon, countdown, save badge, and financing claims are not allowed unless explicitly approved later.
19. `More zones do not automatically mean better comfort` stays after product and scenario sections.
20. Local fonts and stable local assets may be copied into the project folder for reliable HTML review.
21. Create `DESIGN.md` and `PLAN.md` before HTML implementation.
22. Core section order is fixed; only minor visual rhythm adjustments are allowed.

## Open Decisions

1. Final Shopify URL for canonical tag.
2. Whether product ratings can be reliably captured from live product pages during implementation.
3. Whether the final deployed version should be PageFly or Shopify custom liquid after the standalone HTML demo is approved.


## Design Mockup Status

Approved design draft path:

`C:\Users\18041\Desktop\della-pages\2-zone-vs-3-zone-mini-split\Reference Image for the Design Draft.png`

Use the design draft for visual rhythm, ecommerce hierarchy, spacing, and Della/PageFly-style composition.

Do not use the design draft as final source for product data, prices, FAQ count, service-card copy, removed sections, or footer/newsletter content.

Mockup-specific overrides:

- Remove the top benefit strip shown in the draft.
- Remove the standalone install planning band shown in the draft.
- Remove `Find Partner HVAC Installer` from Premium Della Services.
- Implement exactly five FAQ questions, not the six shown in the draft.
- Use only the eight PRD-approved products, not the draft product placeholders.
- Product prices are required and must be live-verified during implementation.
- Do not implement the newsletter/footer area shown in the draft unless separately requested.

## Current Status

- Page structure: approved with removed top benefit strip and removed install planning band.
- Product list: approved from user-provided URLs and images.
- Product prices: required and must be captured live during implementation.
- FAQ: limited to five purchase-focused questions.
- Premium Della Services: must not include Find Partner HVAC Installer.
- Design mockup received and reviewed.
- `DESIGN.md` and `PLAN.md` created.
- Next recommended step: verify live product prices, then begin standalone HTML demo implementation if approved.
## Latest Implementation Corrections

User-provided corrections on 2026-06-24 override earlier ambiguous design notes.

Product tabs and product cards:

- Create exactly two tab panels: `2-Zone Systems` and `3-Zone Systems`.
- Active `2-Zone Systems` panel must show only real 2-zone products from `/collections/2-zone-mini-split`.
- Active `3-Zone Systems` panel must show only real 3-zone products from `/collections/3-zone-mini-split`.
- Use the confirmed product list only.
- Do not invent BTU combinations, product names, prices, ratings, SEER2 values, coverage claims, sale badges, or review counts.
- Product card structure: product image, product title, configuration chips, full-width navy `View Product` CTA.
- Do not use `Add To Cart`.

Hero refinement:

- Keep the left copy and right product comparison on Della blue display platforms.
- Add labels near the product groups: `1 outdoor + 2 indoor units` and `1 outdoor + 3 indoor units`.
- Use real transparent Della product images where possible.
- 2-zone group must show exactly one outdoor unit and two indoor units.
- 3-zone group must show exactly one outdoor unit and three indoor units.
- Do not rely on AI-distorted equipment.

Decision center:

- Keep the combined decision center after Home Situation section.
- Left side has three clear decision cards: `Count the Rooms`, `Size Each Room`, `Plan the Routes`.
- Right side has the comparison table.
- Text must not be too small.
- Table cells must be short and practical.
- Do not use green checkmarks, red X marks, winner badges, or language implying 3-zone is always better.

Home Situation cards:

- Keep four lifestyle cards.
- Use only a small `2-Zone` or `3-Zone` label chip plus a short card heading.
- Approved headings: `Two Bedrooms Need Separate Comfort`, `Bedroom and Home Office Run on Different Schedules`, `Three Upstairs Rooms Need Separate Control`, `Bedroom, Nursery, and Office Need Separate Settings`.
- Do not add long paragraphs.

Bottom CTA:

- Use the `Start with the collection that matches your room` reference structure from the 12K vs 18K page: pale-blue section, two equal white collection cards, text-only cards, no product images.
- Remove the `More than three rooms? View all multi-zone systems` link from this final CTA.

Header/footer/newsletter:

- Use the real Shopify theme header and footer where possible in final Shopify deployment.
- Do not rebuild the footer from the AI screenshot unless necessary.
- Newsletter / comfort updates strip is removed and must not be implemented.

Global style:

- Container max-width: 1200px.
- Heading font: Spectral / Georgia fallback.
- Body and buttons: Poppins / Arial fallback.
- Navy: `#0E1953`.
- Blue: `#5884E7`.
- Light Blue: `#EDF2FF`.
- Product Surface: `#F4F7FF`.
- Trust Cyan: `#DDF7FF`.
- Border Gray: `#E2E6EE`.
- Button radius: 4px.
- Card radius: 4px to 6px.
- Section padding: about 64px to 76px.
- Product/support/FAQ compact sections: about 52px to 64px.

Avoid:

- Pill buttons.
- Heavy shadows.
- Random icons.
- Fake product information.
- Sale badges.
- Fake prices.
- Fake ratings.
- 0% APR claims unless confirmed.
- Federal tax credit claims.
- Memorial Day imagery.
- American flag visuals.
- Overly dense dark navy sections.

## Latest Hero Banner Override

User correction on 2026-06-24 overrides earlier hero visual notes:

- Use `banner.webp` as the hero/banner background image without a white overlay.
- Remove the previous right-side 2-zone and 3-zone product comparison images from the hero.
- Keep the H1 `2-Zone vs 3-Zone Mini Split`.
- Keep hero supporting copy to one sentence focused on the visitor's room/layout pain point: two bedrooms, bedroom + office, upstairs rooms, or an addition.
- Hero CTAs `Shop 2-Zone Mini Splits` and `Shop 3-Zone Mini Splits` should use the same navy button styling.

## Latest Room-Count Strip Removal

User correction on 2026-06-24 removes the early room-count path strip shown under the hero. The page should move directly from the hero into the first decision section. Keep the bottom two-card collection CTA near the end.
