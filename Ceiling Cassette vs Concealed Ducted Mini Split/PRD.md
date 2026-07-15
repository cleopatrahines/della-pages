# PRD: Ceiling Cassette vs Concealed Ducted Mini Split

## Document Status

- Status: PRD, design, and plan approved; final local image integration complete; Step 5 awaits browser recheck and HVAC/product review
- Page structure: Frozen nine-section decision path; no authored Benefit Strip
- Last updated: 2026-07-15
- Current workflow gate: Step 5 static-preview acceptance blocked
- Approved mockup sequence: `设计稿1.png` -> `设计稿2.png` -> `设计稿3.png`
- Mockup decision: no second-round mockup will be generated; current images remain the visual baseline and PRD/DESIGN overrides are authoritative
- Next permitted action: run browser acceptance and record named HVAC/product review, then rerun Step 5
- Not yet permitted: Shopify Liquid section or JSON page template

## Page Summary

Create an evergreen Della comparison landing page for `Ceiling Cassette vs Concealed Ducted Mini Split`.

The page must serve research-led organic traffic and paid ad traffic while guiding shoppers toward the correct Della collection and product starting point. It is a purchase-decision page, not a long educational blog post and not a clone of either collection page.

The page's job is to help visitors answer:

> Is a ceiling cassette or concealed ducted mini split the better installation path for my project?

## Page Type

- Primary type: Comparison guide
- Secondary type: Collection-support page
- Funnel role: SEO research traffic plus Google and paid-social landing traffic
- Commercial intensity: Medium
- Product timing: After project fit, key differences, and installation feasibility
- Primary conversion model: Collection routing first, curated PDP starting points second

## Core Strategy

The page must move the visitor through this decision path:

1. Confirm that the page answers the exact comparison query.
2. Give an actionable answer within approximately 30 seconds.
3. Match the visitor's project type to a practical starting path.
4. Clarify the key differences without becoming a technical article.
5. Confirm whether the home or project can support the installation.
6. Present a small number of Della systems as answers, not inventory.
7. Reinforce trust and route the visitor to the appropriate collection or PDP.

The page must not frame one indoor-unit type as the universal winner.

## Primary Audience

- Homeowners planning a renovation, addition, finished basement, or new construction project.
- Shoppers who want a less visible alternative to a wall-mounted mini split.
- Paid-ad visitors who need a fast answer before they will browse products.
- Secondary audience: light-commercial buyers planning offices, studios, shops, or other open spaces.

## Primary User Decision

Help the visitor understand:

- Start with a ceiling cassette for an open room or open-plan area where central ceiling placement and multi-directional airflow are useful.
- Start with concealed ducted when the project can accommodate a hidden indoor handler and short duct runs, especially when a central-air-style finished appearance is a priority.
- Treat finished basements and other retrofit conditions as conditional decisions based on ceiling access, cavity depth, duct route, drainage, and service access.
- Confirm final equipment selection, sizing, airflow design, electrical requirements, and installation feasibility with a qualified HVAC installer.

## Target URLs

Primary collection routes:

- Ceiling Cassette Mini Split: https://dellahome.com/collections/ceiling-cassette-mini-split
- Concealed Ducted Mini Split: https://dellahome.com/collections/concealed-ducted-mini-split

Support route:

- Find Partner HVAC Installer: https://dellahome.com/pages/find-a-installer

Suggested Shopify path:

- `/pages/ceiling-cassette-vs-concealed-ducted-mini-split`

Local project path:

- `C:\Users\18041\Desktop\della-pages\Ceiling Cassette vs Concealed Ducted Mini Split`

Planned local/GitHub preview filename:

- `ceiling-cassette-vs-concealed-ducted-mini-split.html`

Planned Shopify production format:

- Dedicated Shopify Online Store 2.0 section with dynamic product prices: `sections/ceiling-cassette-vs-concealed-ducted-mini-split.liquid`.
- Dedicated JSON page template: `templates/page.ceiling-cassette-vs-concealed-ducted.json`.
- Store both artifacts inside this project folder using the same `sections/` and `templates/` paths expected by the Shopify theme.
- Do not implement the production page through PageFly Product Elements or a PageFly Custom Code block.
- The local/GitHub preview contains the landing-page body only and does not include a Della Header or Footer.
- The Shopify production page inherits and displays the active Della theme's normal global Header and Footer; the dedicated section must not duplicate them.

Do not create a duplicate `index.html` unless a later approved plan defines a redirect or duplicate-shell strategy.

## SEO Requirements

H1:

`Ceiling Cassette vs Concealed Ducted Mini Split`

The H1 must remain the exact comparison phrase. Do not replace it with a softer headline such as `Choose the Right Hidden Mini Split System`.

Suggested SEO title:

`Ceiling Cassette vs Concealed Ducted Mini Split | Della`

Suggested meta description:

`Compare ceiling cassette vs concealed ducted mini splits by project type, appearance, airflow, and installation needs. Find the right Della system.`

Primary keyword:

- ceiling cassette vs concealed ducted mini split

Secondary keyword themes:

- ceiling cassette vs ducted mini split
- concealed ducted vs ceiling cassette
- hidden mini split options
- ceiling cassette mini split
- concealed ducted mini split
- ceiling cassette installation requirements
- concealed ducted installation requirements

SEO boundaries:

- Do not turn the page into a full installation guide.
- Do not duplicate collection-page product depth.
- Keep the exact comparison intent on this page.
- Use existing Della blog content for supporting depth and internal links.
- Add a canonical tag only after the final Shopify URL is confirmed.
- Do not invent BreadcrumbList markup.
- Add FAQPage JSON-LD only after visible FAQ copy is final and publishable; schema must match the visible answers exactly.
- Do not add Product schema for the curated product module.

## Cannibalization And Internal-Link Plan

The new page should own the direct comparison intent. Existing Della articles should continue to own narrower informational intent:

- Concealed ducted installation: https://dellahome.com/blogs/della-blog/concealed-ducted-mini-split-installation
- Mini split indoor unit types: https://dellahome.com/blogs/della-blog/5-types-of-mini-split-indoor-units
- Ceiling cassette and joist fit: https://dellahome.com/blogs/della-blog/which-ceiling-cassette-mini-splits-fit-standard-16-inch-joists

The landing page may link to these guides where they help resolve installation questions. A later SEO implementation pass should add contextual links from the relevant articles back to this comparison page.

## Approved Page Structure

The following structure is frozen. Do not add standalone modules without updating this PRD and receiving user approval.

1. Hero
2. Quick Answer
3. Find the Best Fit for Your Project
4. Ceiling Cassette vs Concealed Ducted: Key Differences
5. Installation Requirements
6. Start With These Della Systems
7. Trust
8. FAQ
9. Bottom CTA

## First-Round Design Audit

Reviewed files:

- `设计稿1.png`
- `设计稿2.png`
- `设计稿3.png`

The three files represent one continuous page in the order listed above. Keep them as three same-width, visually continuous design segments rather than regenerating one extremely tall image. This preserves text clarity, product-image accuracy, and section-level revision control.

Overall assessment:

- Structure completeness: 10/10
- Della brand alignment: 8.2/10
- Decision efficiency: 8.4/10
- Commercial routing: 8.6/10
- Technical credibility: pending HVAC/product review
- Overall first-round score: 8.5/10

The structure is correct and must not be rebuilt. The required revision is a targeted reduction in poster-like presentation so the page more efficiently moves visitors through `project fit -> installation feasibility -> appropriate collection`.

Mandatory design corrections:

1. Remove all internal section numbers from the rendered page, including `5.`, `6.`, `7.`, `8. TRUST`, `9. FAQ`, and `10. CTA`. Documentation numbering in this PRD does not authorize visible numbering in the UI. Optional short semantic labels such as `COMPARE`, `PLAN YOUR INSTALLATION`, and `SHOP DELLA SYSTEMS` may be used without numbers.
2. Replace `Whole-Home Renovation` with `Multi-Room Renovation`. Do not imply that one system or one listed product necessarily conditions an entire home.
3. Keep the installation-diagram format, but do not ship AI-generated technical diagrams without HVAC/product review. Every indicated component, direction, access point, and relationship must be verified or redrawn from approved technical sources.
4. Replace the first-round Trust cards with a direct implementation of the `Premium Della Services` section from the 2-Zone vs 3-Zone reference page.
5. The exact trust label `Lifetime Coverage (Mini Splits)` is permitted subject to launch-time verification, but do not expand it into `lifetime coverage on the compressor and parts` or any other detailed coverage statement unless the exact current Della policy supports that wording.
6. Reduce Quick Answer height by approximately 25% so it remains a fast routing module and does not delay the primary project-fit section.
7. Use two product tabs in the live page. The two category groups shown one after another in the design are two tab states, not two simultaneously expanded sections.
8. Make the Hero comparison immediately identifiable with subtle HTML labels for `Ceiling Cassette` and `Concealed Ducted`. Reduce the weight and brightness of the diagonal divider.
9. Keep the FAQ compact and visually closer to the Bottom CTA.
10. Replace the Bottom CTA with the approved two collection-path card layout from the 2-Zone vs 3-Zone reference; use no product thumbnails or decorative waves.

Design-source hierarchy:

- This PRD controls scope, product identity, factual copy, claims, links, and acceptance criteria.
- The mockup controls approved visual composition, imagery direction, hierarchy, and rhythm where it does not conflict with this PRD.
- Current Della sources control product, support, warranty, and policy facts.
- AI-generated or mockup text and diagrams are never factual sources.

## Section Requirements

### 1. Hero

Required H1:

`Ceiling Cassette vs Concealed Ducted Mini Split`

Purpose:

- Confirm the exact search intent immediately.
- Establish that the page is a decision guide.
- Provide direct collection routes without forcing an immediate purchase.

Required content direction:

- One short decision-focused paragraph.
- Two primary collection CTAs.
- A comparison visual that clearly communicates ceiling cassette vs concealed ducted.

CTA labels:

- `Shop Ceiling Cassette Mini Splits`
- `Shop Concealed Ducted Mini Splits`

Hero message direction:

- Ceiling cassette: open spaces, clean ceiling integration, multi-directional airflow.
- Concealed ducted: hidden handler, discreet supply and return grilles, renovation or new-construction planning.

Visual direction:

- Wide Della ecommerce banner, not an article header and not a SaaS split-screen dashboard.
- Preserve clean copy space on the left and place the comparison visual on the right.
- The visual must show a recognizable ceiling cassette and a recognizable concealed ducted/vent result.
- Add subtle HTML overlay labels for `Ceiling Cassette` and `Concealed Ducted` so the two sides are immediately understandable without relying on the image alone.
- If the approved diagonal split is retained, reduce the divider's thickness and contrast so the room and equipment remain dominant.
- Use separate desktop and mobile compositions.
- Product or installation imagery must be Della-owned, approved, or generated specifically for the approved design mockup.
- Do not use fake product models, fake specifications, sale graphics, or AI-generated policy copy.

### 2. Quick Answer

Purpose:

- Give paid-ad and fast-scanning visitors a useful answer within approximately 30 seconds.
- Act as conversion insurance for visitors who will not read the entire page.

Recommended heading:

`Ceiling Cassette or Concealed Ducted? Start Here.`

Ceiling cassette cues:

- Open spaces
- Clean ceiling appearance
- Multi-directional airflow

Concealed ducted cues:

- Renovation or new construction
- Hidden vents and concealed equipment
- Central-air-style finished appearance

Rules:

- Keep the module concise.
- Reduce the first-round mockup's module height by approximately 25%; shrink product imagery and excess vertical padding while keeping three cues and the routing CTA for each path.
- Treat this as a fast decision band, not a second product-merchandising section.
- Do not add a quiz, calculator, form, slider, or fake result engine.
- Do not present either choice as the universal winner.

### 3. Find the Best Fit for Your Project

Required H2:

`Find the Best Fit for Your Project`

Purpose:

- Serve as the primary decision module and the main differentiation from generic comparison content.
- Translate HVAC format differences into recognizable project situations.

Use exactly four project scenarios:

#### Open-Concept Living Area

Starting recommendation: Ceiling Cassette

Reason cues:

- Central ceiling placement
- Multi-directional airflow
- Keeps wall space open

#### Finished Basement

Starting recommendation: Depends on the ceiling and duct path

Reason cues:

- Ceiling cassette may fit when a suitable central ceiling opening and service access are available.
- Concealed ducted may fit when a soffit, utility area, or ceiling cavity can support the handler and short duct runs.
- Do not force a single answer.

#### New Construction

Starting recommendation: Concealed Ducted

Reason cues:

- Ceiling and framing plans are still accessible.
- Supply and return locations can be planned early.
- Supports a cleaner finished appearance.

#### Multi-Room Renovation

Starting recommendation: Concealed Ducted

Reason cues:

- Can be planned with the revised layout when suitable ceiling cavities and duct paths are available.
- Can create an integrated appearance across several planned spaces.
- Preserves a central-air-style visual result without implying whole-home coverage from one system.

Scenario rules:

- Use real project/lifestyle imagery, not generic icons.
- Keep reasoning short and practical.
- Use `starting recommendation`, `often`, `may`, or `depends`; avoid guarantees.
- Use labels such as `Start With Ceiling Cassette`, `Check Concealed Ducted First`, and `Depends on Ceiling Access` instead of absolute recommendation badges.
- Do not expand beyond these four scenarios in V1.

### 4. Ceiling Cassette vs Concealed Ducted: Key Differences

Required H2:

`Ceiling Cassette vs Concealed Ducted: Key Differences`

Purpose:

- Merge basic explanation and comparison into one scannable section.
- Support organic search and AI/search extraction without creating a blog-style content wall.

Do not create separate standalone sections titled `What Is a Ceiling Cassette?` and `What Is Concealed Ducted?`.

Use a semantic comparison table with these rows:

| Decision Point | Ceiling Cassette | Concealed Ducted |
| --- | --- | --- |
| Best for | Open rooms and shared spaces | Renovations, new construction, and hidden-air-distribution layouts |
| Visible indoors | A ceiling-mounted cassette panel | Supply and return grilles |
| Air distribution | Air begins from one central ceiling location | Air travels through ducts to planned outlets |
| Installation planning | Ceiling opening, support, drainage, line set, and service clearance | Concealed indoor unit, duct design, supply/return placement, drainage, and service access |
| Ceiling space | Localized space around the cassette body | More space for the indoor unit and duct routes |
| Central-air appearance | Low-profile ceiling equipment remains visible | Closest visual result to conventional central air |

Table rules:

- No winner badges.
- No guaranteed comfort, savings, or coverage claims.
- Do not claim that multiple outlets automatically provide independent room-by-room temperature control.
- Keep all six rows, but keep each cell to one concise sentence or phrase; do not shrink type to fit dense copy.
- On small screens, use accessible stacked comparison cards instead of crushing the table columns.

### 5. Installation Requirements

Purpose:

- Resolve the primary purchase objection: `Can my project actually support this installation?`
- Reduce unqualified PDP clicks without becoming a full installation tutorial.

Ceiling cassette planning relationships:

- Ceiling opening
- Available clearance
- Drain route
- Line-set route
- Service/filter access

Concealed ducted planning relationships:

- Indoor unit space
- Supply duct route
- Return-air path
- Drain route
- Service/filter access

Rules:

- Keep the module purchase-focused and compact.
- Use two equal-height cards with simplified two-dimensional conceptual planning diagrams, not realistic equipment cutaways.
- Use a white background, thin lines, restrained arrows, and Navy, Della Blue, and Light Blue accents.
- Place the building/ceiling relationship on the left and the corresponding planning checklist on the right or below it.
- Add this label to both diagrams: `Conceptual planning diagram — not to scale`.
- End the module after the two planning cards. Do not add a shared confirmation note, installer CTA, or extra checklist bar below them.
- Do not show exact installation depths or dimensions, unverified internal routing, specific connection counts or locations, precise supply/return directions, official-looking equipment cutaways, DIY steps, or construction sequences.
- Prefer relationships supported across the official manuals for the eight recommended products. If a detail cannot be confirmed across the relevant product family, abstract or omit it.
- Replace or redraw every AI-generated technical detail from the first-round mockup; visual plausibility is not evidence.
- Do not publish DIY refrigerant guidance.
- Do not quote installed-cost ranges.
- Do not make legal, permit, code, or installation guarantees.

### 6. Start With These Della Systems

Required H2:

`Start With These Della Systems`

Purpose:

- Turn the comparison into a practical shopping starting point.
- Present products as answers to the decision, not as an inventory grid.

Use two accessible tabs:

- `Ceiling Cassette`
- `Concealed Ducted`

Each tab must contain:

- Four recommended products from the approved reference set for the same indoor-unit type.
- Keep all four product cards visually equal; do not add a starting-point badge or enlarge any card into a separate feature panel.
- A short project-fit explanation.
- One `View Product` CTA per displayed product.
- One collection-level `More Options` CTA.

Only one tab panel may be visible at a time. The two four-product groups shown sequentially in the design mockup represent the two tab states and must not be implemented as two vertically stacked product groups. The four cards use one consistent grid and card size without a featured or recommended badge.

Approved layout source:

- Use the product-module layout from `single-zone-vs-multi-zone-mini-split.html`, specifically `Find the Della setup that matches your rooms`, as the direct visual and spacing reference.
- Desktop screenshot reference: `product-layout-reference.png`.
- 430px mobile screenshot reference: `product-layout-mobile-reference.png`.
- Replace its five room-count tabs with exactly two system tabs: `Ceiling Cassette` and `Concealed Ducted`.
- Preserve its compact tab toolbar, right-aligned collection CTA, concise category introduction, open four-column product grid, bordered white cards, specification chips, visible price, and full-width navy `View Product` CTA.
- Do not use the large category image/banner from the 2-Zone vs 3-Zone module.
- Do not use the project-scenario tabs or mixed-category product logic from `ceiling-cassette-vs-wall-mount-mini-split.html`; project selection has already been completed earlier on this page.
- Do not use `Add to Cart` or direct cart links from any reference implementation.

Tab behavior:

- Tabs: `Ceiling Cassette` and `Concealed Ducted`.
- Default to `Ceiling Cassette` when no earlier in-page choice exists.
- When an approved in-page choice control identifies one system type, activate the matching tab when the visitor reaches this section.
- Keep the active state visible and expose the tab relationship to assistive technology.

#### Ceiling Cassette Recommended Starting Point

Role:

- Open-space recommendation

Product:

- DELLA 18,000 BTU 20.5 SEER2 Ceiling Cassette Ductless Mini Split AC - Up to 1000 Sq.Ft.

PDP:

- https://dellahome.com/products/della-18-000-btu-seer2-20-5-ceiling-cassette-ductless-mini-split-ac-up-to-1000-sq-ft

Image:

- https://dellahome.com/cdn/shop/files/Cassette-AC-Listing-1-2.jpg?crop=center&height=1200&v=1783495745&width=1200

Fit cues:

- Larger living areas
- Open layouts
- Central ceiling placement

#### Concealed Ducted Recommended Starting Point

Role:

- Hidden-layout recommendation

Product:

- DELLA 22000 BTU 19 SEER2 Concealed Ducted Mini Split Air Conditioner

PDP:

- https://dellahome.com/products/della-22000-btu-19-seer2-concealed-ducted-mini-split-air-conditioner

Image:

- https://dellahome.com/cdn/shop/files/Ducted-AC-Listing-1-2.jpg?crop=center&height=1200&v=1782970448&width=1200

Fit cues:

- Renovations or new construction
- Hidden handler and grille-based finish
- Projects with a planned duct route

Collection CTAs:

- `More Ceiling Cassette Options` -> https://dellahome.com/collections/ceiling-cassette-mini-split
- `More Concealed Ducted Options` -> https://dellahome.com/collections/concealed-ducted-mini-split

Product-card rules:

- CTA is `View Product`, never `Add to Cart`.
- Do not add direct cart URLs.
- Product identity and images come from this PRD and official Della sources, never from the design mockup.
- A current selling price is required on every product card.
- Local/GitHub HTML preview: use a static price snapshot captured from the live Shopify PDP or product JSON during implementation and record the capture date in implementation notes.
- Shopify production page: render the current product price dynamically from Shopify Liquid product data.
- Screenshot and mockup prices are layout references only.
- Label a variable product price as `From` where appropriate.
- If a required price cannot be captured reliably or conflicts between live sources, stop and request review instead of inventing or silently omitting it.
- Omit compare-at prices, discount percentages, coupons, and sale badges unless separately approved from a current promotion source.
- Ratings may be shown only if captured reliably from a live source; otherwise omit them.
- If a featured product becomes unavailable, stop and request approval before substituting another product.
- The four recommended products in each tab are the exact four corresponding entries in the Approved Product Reference Set.
- Display the complete approved product title and allow natural wrapping; do not truncate or replace it with an invented marketing name.

### 7. Trust

Purpose:

- Reinforce purchase confidence after the decision and product path are established.
- Keep service reassurance late in the page, not as an interruption to the comparison flow.

Required H2:

`Premium Della Services`

Required service labels, copied from the approved reference and subject to launch-time verification:

- `Free & Fast Shipping`
- `Pay in 6 Months, 0% APR`
- `24×7 Live Chat Support`
- `Lifetime Coverage (Mini Splits)`

Rules:

- Directly reproduce the structure, typography, spacing, icon treatment, and responsive behavior of the `Premium Della Services` section in `2-zone-vs-3-zone-mini-split.html`.
- Use the same four official icon assets referenced by that section.
- Desktop: four columns. Tablet: two columns. Mobile: one column, matching the reference implementation.
- Cards remain borderless, white, centered, and compact; icon size is approximately 44px and service labels use Poppins at approximately 18px.
- Do not add supporting paragraphs, `Learn more` links, or extra trust topics.
- Verify all four service labels against current Della sources immediately before publication. If exact wording is no longer supportable, stop and request user approval instead of silently substituting copy.
- Do not expand `Lifetime Coverage (Mini Splits)` into a compressor, parts, labor, duration, or eligibility statement inside this section.
- Do not add a newsletter or email-capture module.

### 8. FAQ

Purpose:

- Resolve the final comparison, installation, and product-selection questions.
- Keep the section compact and near the bottom.

Use three non-repetitive, high-value questions:

1. `Can one concealed ducted unit serve more than one room?`
2. `Does a ceiling cassette require a drop ceiling?`
3. `How should I size a ceiling cassette or concealed ducted mini split?`

FAQ rules:

- Answers must be concise, qualified, and written in natural American English.
- Do not repeat the full page inside the FAQ.
- Do not make universal installation, zoning, cost, or coverage claims.
- Use the layout, typography, spacing, divider, arrow, hover, and open-state treatment from `2-Zone vs 3-Zone Mini Split Questions` in `2-zone-vs-3-zone-mini-split.html`.
- Use one single-column `details`/`summary` list with transparent backgrounds, thin horizontal dividers, no card radius, Spectral question text, and Poppins answer text.
- Use the H2 `Ceiling Cassette vs Concealed Ducted Mini Split Questions`.
- Keep all six questions collapsed by default.
- Remove the visible `9. FAQ` task label and keep the section visually close to the Bottom CTA.
- FAQPage JSON-LD is allowed only after final visible copy is approved and must match exactly.

### 9. Bottom CTA

Purpose:

- End with the same two decision paths introduced in the hero.
- Give visitors a collection route without forcing a PDP choice.

Use two collection path cards:

Ceiling Cassette Mini Splits:

- Positioning: `For open spaces that benefit from central ceiling placement and multi-directional airflow.`
- CTA: `Shop Ceiling Cassette`

Concealed Ducted Mini Splits:

- Positioning: `For projects designed around a concealed handler, discreet grilles, and short duct runs.`
- CTA: `Shop Concealed Ducted`

Do not add a third product category or unrelated global-shop CTA.

Visual direction:

- Directly reproduce the two-path layout, typography, card treatment, spacing, and responsive behavior of `Ready to Choose Your Zone Count?` in `2-zone-vs-3-zone-mini-split.html`.
- Use the H2 `Ready to Choose Your Hidden Mini Split Type?`.
- Desktop uses two equal collection path cards; mobile stacks them in one column.
- Use a light product-surface background, white cards, restrained blue border/shadow, Spectral card headings, short Poppins copy, and navy CTA buttons.
- Replace only the title, path copy, collection names, button labels, and URLs with the approved Ceiling Cassette and Concealed Ducted content.
- Do not add product thumbnails or retain the first-round mockup's decorative wave graphics.

## Approved Product Reference Set

The following eight products form the two V1 Recommended Product Sets. All four Ceiling Cassette products appear in the Ceiling Cassette tab, and all four Concealed Ducted products appear in the Concealed Ducted tab. The two featured starting points receive compact badges but remain equal-size cards in their respective four-product grids.

### Ceiling Cassette References

| Role | Product | URL | Image |
| --- | --- | --- | --- |
| Smaller single-zone reference | DELLA 12,000 BTU 22 SEER2 Ceiling Cassette Ductless Mini Split AC - Up to 550 Sq.Ft. | https://dellahome.com/products/della-12-000-btu-seer2-22-ceiling-cassette-ductless-mini-split-ac-up-to-550-sq-ft | https://dellahome.com/cdn/shop/files/Cassette-AC-Listing-1-2.jpg?crop=center&height=1800&v=1783495745&width=1800 |
| Featured open-space starting point | DELLA 18,000 BTU 20.5 SEER2 Ceiling Cassette Ductless Mini Split AC - Up to 1000 Sq.Ft. | https://dellahome.com/products/della-18-000-btu-seer2-20-5-ceiling-cassette-ductless-mini-split-ac-up-to-1000-sq-ft | https://dellahome.com/cdn/shop/files/Cassette-AC-Listing-1-2.jpg?crop=center&height=1200&v=1783495745&width=1200 |
| Dual-zone reference | DELLA 18000 BTU Dual Zone Ceiling Cassette Mini Split AC (9K + 12K) - Up to 950 Sq.Ft. | https://dellahome.com/products/18000-btu-dual-zone-ceiling-cassette-mini-split-ac-9k-12k-up-to-950-sq-ft | https://dellahome.com/cdn/shop/files/1D2-CC_D_056eb49d-31a3-4402-920e-17cd4d4fbf38.jpg?crop=center&height=1200&v=1755745005&width=1200 |
| Tri-zone reference | DELLA 27000 BTU Tri-Zone Ceiling Cassette Mini Split AC (9K + 12K + 12K) - Up to 1500 Sq.Ft. | https://dellahome.com/products/27000-btu-tri-zone-ceiling-cassette-mini-split-ac-9k-12k-12k-up-to-1500-sq-ft | https://dellahome.com/cdn/shop/files/1D3-CC_T_e52ae078-2560-488b-8430-acdab6394c3e.jpg?crop=center&height=1200&v=1755745031&width=1200 |

### Concealed Ducted References

| Role | Product | URL | Image |
| --- | --- | --- | --- |
| Smaller single-zone reference | DELLA 11000 BTU 19 SEER2 Concealed Ducted Mini Split Air Conditioner | https://dellahome.com/products/della-11000-btu-19-seer2-concealed-ducted-mini-split-air-conditioner | https://dellahome.com/cdn/shop/files/Ducted-AC-Listing-1-4.jpg?crop=center&height=1800&v=1782970934&width=1800 |
| Featured hidden-layout starting point | DELLA 22000 BTU 19 SEER2 Concealed Ducted Mini Split Air Conditioner | https://dellahome.com/products/della-22000-btu-19-seer2-concealed-ducted-mini-split-air-conditioner | https://dellahome.com/cdn/shop/files/Ducted-AC-Listing-1-2.jpg?crop=center&height=1200&v=1782970448&width=1200 |
| Dual-zone reference | DELLA 27000 BTU Dual Zone Concealed Ducted Mini Split Heat Pump AC (9.5K + 17K) | https://dellahome.com/products/della-27000-btu-dual-zone-concealed-ducted-mini-split-heat-pump-ac-9-5k-17k | https://dellahome.com/cdn/shop/files/1D3-DC_D912_533cfd3a-40b4-4f1b-9a12-2a2d989cf813.jpg?crop=center&height=1200&v=1770103031&width=1200 |
| Tri-zone reference | DELLA 34000 BTU Tri-Zone Concealed Ducted Mini Split Heat Pump AC (9.5K + 11K + 17K) | https://dellahome.com/products/della-34000-btu-tri-zone-concealed-ducted-mini-split-heat-pump-ac-9-5k-11k-17k | https://dellahome.com/cdn/shop/files/1D4-DC_T9912_97d14683-fb42-42d6-9473-d279dd0b26e6.jpg?crop=center&height=1200&v=1770103053&width=1200 |

## Design System Requirements

Use the Della topical PageFly / Memorial Day / coupon-code visual language.

Primary local sources:

- `C:\Users\18041\Desktop\della-pages\della页面设计规范\della-memorial-day-design-system.md`
- `C:\Users\18041\Desktop\della-pages\della页面设计规范\page.pf-ef33e2e6.json.txt`
- `C:\Users\18041\Desktop\della-pages\della页面设计规范\pf-ef33e2e6.liquid.txt`
- `C:\Users\18041\Desktop\della-pages\memorial-day-sale`
- https://dellahome.com/pages/coupon-code

Comparison-page references:

- `C:\Users\18041\Desktop\della-pages\2-zone-vs-3-zone-mini-split\2-zone-vs-3-zone-mini-split.html`
- `C:\Users\18041\Desktop\della-pages\single-zone-vs-multi-zone-mini-split\single-zone-vs-multi-zone-mini-split.html`
- `C:\Users\18041\Desktop\della-pages\12000 BTU vs 18000 BTU Mini Split\12000-btu-vs-18000-btu-mini-split.html`
- `C:\Users\18041\Desktop\della-pages\Ceiling Cassette vs Wall Mount Mini Split\ceiling-cassette-vs-wall-mount-mini-split.html`

Required visual tokens:

- Heading and product-title font: Spectral, fallback Georgia, serif.
- Body, button, tab, and table font: Poppins, fallback Arial, sans-serif.
- Navy: `#0E1953`.
- Brand blue: `#5884E7`.
- Hover blue: `#6B95EF`.
- Light-blue surfaces: `#EDF2FF`, `#F4F7FF`, `#DDF7FF`.
- Primary ecommerce buttons: blue or navy fill, white text, 4px radius.
- Product cards: white, open merchandising layout, restrained border or shadow.
- Section rhythm: coherent long-scroll ecommerce page, not disconnected component stacks.

Visual prohibitions:

- No generic SaaS dashboard hero.
- No glassmorphism.
- No decorative orbs.
- No purple gradients.
- No oversized generic icon grid.
- No holiday or sale styling.
- No coupon, countdown, discount, or fake urgency.
- No pill-shaped primary ecommerce buttons.
- No AI-generated product names, specifications, prices, policies, or warranty claims.

## Mobile Behavior

- Primary review widths: 390px and 430px mobile, 768px tablet, 1280px laptop, and 1440px desktop.
- Hero must use a dedicated mobile composition; text must not overlap the comparison visual.
- Hero CTAs may stack vertically when required.
- Project scenario cards should become a single-column stack or a deliberate swipe pattern with a visible next-card cue.
- Comparison table should become stacked comparison cards on small screens; avoid compressed unreadable columns.
- Product tabs must be keyboard accessible and touch targets must be at least 44px.
- Product module shows only the active four-product system tab.
- At 390px and 430px, the active product set uses a two-column `2 x 2` grid matching `product-layout-mobile-reference.png`.
- Below 360px, the product grid becomes one column.
- Mobile cards retain the complete product title, 2-3 concise verified specification chips, visible price, and full-width `View Product` button.
- Product titles wrap naturally without clipping; card content and buttons align consistently across each row.
- FAQ should use accessible `details` and `summary` behavior unless the approved design requires an equivalent accessible button accordion.
- No horizontal page overflow, clipped headings, overlapping CTA text, or content hidden behind sticky elements.
- Do not add a mobile sticky purchase bar unless later approved in `DESIGN.md` and `PLAN.md`.

## Interaction And Accessibility Requirements

- Exactly one H1.
- Semantic H2/H3 hierarchy.
- Visible keyboard focus states.
- Tabs must support correct ARIA roles and keyboard navigation if implemented as ARIA tabs.
- FAQ controls must be keyboard accessible.
- Touch targets must be at least 44px.
- Images require useful, concise alt text; decorative images must be hidden from assistive technology.
- Comparison data must remain available in semantic HTML even when mobile presentation changes.
- Same-site Della links should open in the same tab in the Shopify version.
- GitHub/local review may use new-tab behavior only when documented in the implementation plan.

## Paid Traffic And Measurement Requirements

- Preserve the page's fast-decision path; do not insert content modules between Quick Answer and project fit.
- Add stable tracking labels or data attributes for hero collection CTAs, product CTAs, installer CTA, and bottom collection CTAs.
- Preserve relevant advertising parameters when routing to collection or product pages if the final Shopify implementation requires explicit pass-through.
- Parameters to consider: `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term`, `gclid`, and `fbclid`.
- Do not invent analytics event names before the existing Della tracking convention is inspected.

## Content And Claim Guardrails

- Use natural American English.
- Tone: experienced, direct, practical, and purchase-supportive.
- Prefer `starting point`, `often`, `may`, `depends`, and `confirm with an installer` over universal claims.
- Do not promise comfort, energy savings, coverage, noise levels, installation ease, or code compliance unless supported by the exact product/source context.
- Do not imply that all rooms connected to one concealed handler have independent temperature control.
- Do not claim that a ceiling cassette is invisible; the ceiling panel remains visible.
- Do not claim that concealed ducted is identical to central AC; describe it as the closest visual result among the two compared options.
- Do not quote installed-cost ranges.
- Do not publish unverified financing, tax-credit, rebate, warranty, or lifetime-coverage claims.

## Non-Goals

- No long-form blog article.
- No separate `What Is a Ceiling Cassette?` module.
- No separate `What Is Concealed Ducted?` module.
- No interactive calculator or quiz.
- No collection clone or eight-card product grid.
- No `Add to Cart` CTA.
- No direct cart URLs.
- No custom or duplicated Shopify Header, global navigation, or Footer inside the standalone preview or dedicated landing-page section; normal theme Header/Footer remain visible around the Shopify production page.
- No newsletter or email capture.
- No promo, coupon, countdown, sale badge, or fake urgency.
- No installed-cost estimator.
- No mixed-indoor-unit compatibility claims without a Della compatibility source.
- No extra project scenarios beyond the approved four in V1.
- No additional standalone page modules without a PRD change and user approval.

## Acceptance Criteria

### Strategy And Structure

- The page follows the exact nine-section approved order.
- No extra standalone module is inserted.
- The user can understand the basic difference within the Hero and Quick Answer.
- `Find the Best Fit for Your Project` is the main decision module and uses exactly four scenarios.
- The comparison explanation and table remain one combined section.
- Installation feasibility appears before product recommendations.
- No internal section number or design-task label appears in the rendered UI.
- The fourth project scenario is `Multi-Room Renovation`, not `Whole-Home Renovation`.

### SEO

- H1 exactly matches `Ceiling Cassette vs Concealed Ducted Mini Split`.
- Exactly one H1 exists.
- Content targets comparison intent without duplicating the full installation guides or collection pages.
- Canonical is omitted until the final Shopify URL is confirmed.
- FAQPage JSON-LD is omitted until final visible FAQ copy is approved.

### Merchandising

- Product area uses two accessible tabs with four approved recommended products per tab in V1.
- Only one four-product tab panel is visible at a time; the two categories are never stacked as an eight-product page section.
- The eight approved products appear as equal cards without a featured or recommended badge.
- All eight product identities match this PRD unless the user approves a substitution.
- Every product CTA says `View Product`.
- Every product card displays a current verified selling price, using `From` when appropriate.
- Preview HTML prices are live-verified static snapshots with a recorded capture date; Shopify production prices are dynamically rendered through Liquid.
- Each tab includes a collection-level `More Options` CTA.
- The active tab uses a concise category introduction, four-card grid, and collection CTA without a large category banner or a second project selector.
- No invented price, rating, sale, or product data appears.

### Brand And UX

- Visual styling follows the Della PageFly/Memorial topical system.
- Hero feels like a mature Della ecommerce banner.
- Spectral and Poppins are used in their approved roles.
- Buttons, colors, spacing, and card styling follow the approved tokens.
- The page does not resemble a SaaS dashboard or generic AI template.
- Mobile layouts work at 390px and 430px without overflow or overlap.
- Product cards render as two columns at both 390px and 430px, with complete readable titles, visible prices, specification chips, and full-width CTAs.
- Tabs, FAQ, and CTAs are keyboard accessible with visible focus states.
- Quick Answer is visibly more compact than the first-round mockup and does not overpower project fit.
- Trust directly matches the approved `Premium Della Services` reference structure and four verified service labels.
- FAQ matches the approved single-column border-only accordion reference and starts fully collapsed.
- Bottom CTA matches the approved two-path card reference with two collection destinations.
- The Hero identifies both system types with accessible HTML labels and a restrained divider.
- The Bottom CTA presents two explicit collection paths without prominent generic wave decoration.
- Preview HTML renders no Header or Footer; Shopify production renders the active theme's normal Header/Footer exactly once around the dedicated landing-page section.

### Technical Credibility

- Installation visuals are explicitly conceptual, two-dimensional, and marked `not to scale`.
- Only the approved planning relationships are shown; exact dimensions, internal routing, connection counts/positions, precise airflow directions, and construction steps are absent.
- Installation diagrams and shared disclaimer have a recorded review by an appropriate Della product or HVAC reviewer before publication.
- Retained relationships are checked against official Della product documentation for the relevant product family.
- No unverified AI-generated technical detail or coverage-policy statement remains in the publishable page.

### Conversion And Tracking

- Hero and bottom CTA route to both approved collections.
- Product CTAs route to the approved PDPs.
- Installation CTA routes to the current Della installer page.
- Tracking hooks distinguish hero, product, installer, and bottom collection clicks.
- No promotional claim or urgency mechanism is introduced without approval.

## Verification Harness For Later Implementation

Evidence required before the HTML can be considered complete:

- Source inspection confirming the exact section order and one H1.
- Desktop screenshots at approximately 1280px and 1440px.
- Tablet screenshot at approximately 768px.
- Mobile screenshots at approximately 390px and 430px.
- Mobile product-grid check confirming two columns at 390px and 430px and one column below 360px.
- Click checks for hero collection CTAs, product tabs, all visible PDP CTAs, collection `More Options` CTAs, installer CTA, and bottom CTAs.
- Keyboard checks for tabs and FAQ.
- Overflow and text-overlap checks at all review widths.
- Product title, URL, image, availability, and price-source comparison against this PRD and live Shopify data.
- Price parity check between every preview HTML snapshot, every Shopify Liquid-rendered production price, and the corresponding live PDP at QA time.
- Schema inspection confirming FAQPage is absent until approved, or exactly matches visible FAQ when later added.
- Review confirming no fake or stale promo, coupon, pricing, rating, warranty, or financing content remains.
- Installation-visual review confirming both `not to scale` labels, the shared professional-confirmation note, and the absence of prohibited technical detail.

Pass conditions:

- All approved structure, content roles, and routes are present.
- No prohibited module or claim appears.
- The featured product module feels like a recommendation, not a collection clone.
- The page is usable with keyboard and touch input.
- Visual QA matches the approved Della design direction.

Failure signals:

- H1 is changed to a non-comparison phrase.
- Additional educational modules turn the page into a blog.
- Product merchandising appears before project fit and installation feasibility.
- Both four-product category groups are expanded at the same time.
- A mockup-only section number or task label remains visible.
- `Whole-Home Renovation` remains in customer-facing copy.
- An unverified technical diagram or detailed lifetime-coverage claim remains.
- `Add to Cart`, direct cart URLs, or invented promotions appear.
- The comparison implies that one concealed handler automatically gives independent control to every outlet or room.
- Mobile comparison content becomes unreadable or horizontally breaks the page.
- AI mockup placeholder content is copied into final product or policy data.

## Resolved Decisions

1. The final page structure contains exactly ten sections and is frozen.
2. The page is a purchase-decision guide, not a conventional product comparison article.
3. The exact comparison keyword remains the H1.
4. Quick Answer remains directly after the Hero for paid-traffic efficiency.
5. `Find the Best Fit for Your Project` is the core module.
6. Project-fit scenarios are limited to Open-Concept Living Area, Finished Basement, New Construction, and Multi-Room Renovation.
7. Finished Basement receives a conditional answer rather than a forced recommendation.
8. Basic explanation and the comparison table are merged into one Key Differences section.
9. Installation Requirements remains before product merchandising.
10. Product merchandising uses two system-type tabs with four approved recommended products per tab; only one category tab is visible at a time.
11. Ceiling Cassette starts with the 18,000 BTU single-zone product.
12. Concealed Ducted starts with the 22,000 BTU single-zone product.
13. Product CTAs use `View Product`; collections use `More Options` and shop-path CTAs.
14. Trust and FAQ remain late in the page.
15. Structure optimization is considered complete; post-launch improvements should change module weight or copy based on GSC, paid-search terms, and click data rather than adding modules by default.
16. The three supplied mockup files are three continuous design segments, not three pages and not three simultaneously visible tab states.
17. Internal section numbers are design-task annotations and must not appear in the live UI.
18. Quick Answer, Trust, and FAQ must be compressed in the revised design; the project-fit and installation decision path retains priority.
19. Technical installation illustrations require product/HVAC verification before publication.
20. The exact reference label `Lifetime Coverage (Mini Splits)` is included in Premium Della Services subject to launch-time verification; expanded compressor, parts, labor, or eligibility claims remain excluded unless separately approved.
21. The product module directly follows the `Find the Della setup that matches your rooms` layout from the Single-Zone vs Multi-Zone reference, adapted to two system tabs and four products per tab; it uses no large category banner and no project-scenario selector.
22. Every product card displays a current verified price; the supplied screenshot is a layout reference and never a product-price source.
23. Local/GitHub HTML uses live-verified static price snapshots, while the Shopify production implementation uses Liquid-rendered dynamic prices.
24. Shopify production uses a dedicated Online Store 2.0 Liquid section plus a dedicated JSON page template, not PageFly product components.
25. Local/GitHub preview contains no Header or Footer; Shopify production keeps the active theme's normal global Header/Footer, and the dedicated section does not recreate them.
26. Product cards follow the supplied 430px reference: two columns at 390px and 430px, one column below 360px, complete product titles, specification chips, price, and full-width `View Product` CTAs.
27. Installation Requirements uses two equal-height simplified planning diagrams showing only five approved relationships per system, with `not to scale` labels and a shared professional-confirmation disclaimer; detailed AI cutaways and unverified installation specifics are prohibited.
28. Trust directly reproduces the `Premium Della Services` reference section, including its heading, four service labels, icon treatment, and 4-column/2-column/1-column responsive behavior.
29. FAQ directly uses the single-column border-only accordion style from `2-Zone vs 3-Zone Mini Split Questions`, with this page's six questions collapsed by default.
30. Bottom CTA directly uses the two collection-path card layout from `Ready to Choose Your Zone Count?`, adapted to Ceiling Cassette and Concealed Ducted.

## Pending Inputs For Later Stages

These items do not block this PRD but must be resolved before or during their named stage:

- Step 1 evidence review and asset-path approval: required before implementation Step 2.
- Final approved desktop and mobile hero assets: required before HTML implementation.
- Final project-scenario image map: required before HTML implementation.
- Official manual review for all eight recommended products: the single-zone cassette, single-zone concealed-ducted, and 140-page multi-zone family manuals were verified on 2026-07-14. The multi-zone family manual covers both cassette and concealed-ducted indoor-unit planning relationships. Some product-specific PDF links on the PDPs resolve to AHRI certificates or a broken file, so the common family manual is the usable source of truth; details are recorded in `implementation-notes.md`.
- Named Della product or HVAC reviewer: required before the conceptual installation diagrams are accepted for publication.
- Current official support, shipping, installer, registration, and warranty-policy wording: verify before final trust copy is frozen.
- Final FAQ answer copy: required before FAQPage JSON-LD.
- Live verification of all eight product availabilities and preview price snapshots: required during implementation.
- Existing Della analytics event convention: inspect before final tracking implementation.
- Final Shopify URL: confirm before adding canonical.
- Exact Della theme integration details needed by the dedicated section/template, including product-setting conventions and checks that global Header/Footer render once without duplicated spacing: inspect before `PLAN.md`.

## Stage Gate

This PRD is the current source of truth for scope, structure, product strategy, SEO intent, and acceptance criteria.

## 2026-07-15 — Final Local Image Integration Override

The user supplied final local assets for the Hero, Quick Answer, Project Fit, Key Differences, and Installation Requirements. These files replace all temporary scene media, Hero product-image composition, comparison overlays, and inline planning SVGs in the static preview and future Shopify implementation. Product-card identity images, product data, prices, links, tabs, FAQ, and section order remain unchanged.

- Use the local responsive Hero pair (`banner desktop.webp`, `banner mobile.webp`) in a `<picture>` element; keep H1, paragraph, and collection CTAs as HTML.
- Use the supplied Quick Answer, Project Fit, comparison, and planning files directly from the page directory with meaningful alternate text and intrinsic dimensions.
- The static preview has no authored benefit strip. Shopify production uses only the active theme chrome and must not add a duplicate page-level benefit strip.
- Trust H2 is `Why Shop Della?`. Its four approved labels are `Free Shipping Sitewide`, `24/7 Live Chat Support`, `Lifetime Coverage on Mini Splits`, and `Product Guidance Before You Buy`. Financing is excluded.
- The supplied planning images are approved conceptual diagrams for this page. No additional technical detail may be overlaid or inferred from them.

Next step after the blocked Step 5 run:

1. Run responsive browser acceptance against the final local image set.
2. Record approval from a named Della product/HVAC reviewer for both conceptual planning diagrams.
3. Rerun Step 5 and return updated acceptance evidence.
4. Do not begin Liquid or JSON until Step 5 passes or the user explicitly accepts the remaining blockers.

Recorded workflow override:

- The user supplied a complete three-part mockup directly after PRD approval, so a retrospective `GEMINI_DESIGN_PROMPT.md` is unnecessary. The risk is controlled by the documented design audit and the explicit override rules in `DESIGN.md`.
- The user explicitly chose not to generate a revised mockup. The risk of visual ambiguity is controlled by `DESIGN.md`, the two saved product-layout screenshots, and direct section references to existing Della HTML for Products, Trust, FAQ, and Bottom CTA.

Do not bypass this order without recording the override and its risk.
