# Ductless Mini Split vs Central Air — PRD

Status: Approved for implementation planning  
Page type: Comparison guide / research-intent decision landing page  
Brand: DELLA  
Final project folder: `C:\Users\18041\Desktop\della-pages\Ductless Mini Split vs Central Air`  
Planned HTML filename: `ductless-mini-split-vs-central-air.html`

## 1. Purpose

Build a standalone Shopify/PageFly-compatible HTML landing page that:

- ranks for research and commercial-investigation searches around mini split vs central air;
- gives Google/Meta visitors a clear, message-matched decision path;
- helps a homeowner choose a system architecture quickly, then moves directly into relevant products;
- routes qualified visitors to the correct DELLA collection, product path, or support path;
- feels like a mature DELLA ecommerce page rather than a long blog post or generic SaaS comparison template.

The page's first job is to answer: **What HVAC project is the visitor trying to solve, and what is the right DELLA starting path?** Its second job is to route the visitor to the appropriate collection, PDP, Product Finder, or installer path.

## 2. Strategic conclusion

The page must not declare a universal winner and must not recommend Multi Zone to everyone.

The decision logic is project-led:

1. **Replace** an existing whole-home ducted system → start with Central Air.
2. **Add** comfort without relying on whole-home ductwork → start with Wall-Mounted Mini Splits.
3. **Supplement** a working central system in a problem room or isolated space → consider a separate Wall-Mounted Mini Split and confirm the project with an installer.

This produces a more accurate and durable conversion path than a standard pros/cons article or an unqualified product grid.

### First-principles value

The page is a **guided shopping page**, not an HVAC article. Every section must perform one of three jobs:

1. help the visitor recognize the right system path;
2. present the approved DELLA products for that path;
3. remove a purchase or installation objection.

If a block does not perform one of these jobs, remove it. Keep paragraphs short, use visual comparison and product imagery, and allow visitors to reach the relevant shopping path immediately after the Hero and Project Gateway.

## 3. Verified DELLA merchandising facts

Verified on 2026-08-13 from live DELLA pages:

- `https://dellahome.com/collections/wall-mounted-mini-split` is the best existing top-level **ductless wall-mounted mini split** shopping path. The collection currently includes both single-zone and multi-zone configurations.
- Do not publish the absolute claim that every individual configuration was manually verified as ductless. Use the collection as the consumer-facing ductless path without making an unnecessary catalog-wide absolute statement.
- `https://dellahome.com/collections/central-air-conditioner` is the correct **Central Air** shopping path.
- The Central Air collection currently contains four products: 24K, 34K, 47K, and 53K BTU.
- The current DELLA Central Air assortment consists of ducted inverter heat-pump systems with an indoor air handler and outdoor unit, providing heating and cooling. The page must not describe the assortment as cooling-only central AC or as every possible traditional central-air configuration.
- The current Central Air collection SEO copy contains conflicting statements suggesting suitability for older homes without ductwork and minimal structural modification. Do not reuse those claims on this page; they conflict with the actual ducted products and should be handled as a separate collection-page content correction.
- Generic DELLA Single Zone and Multi Zone collections also contain cassette and concealed-ducted systems. They should not automatically be treated as pure wall-mounted ductless destinations for ad message match.

## 4. Routing architecture

### Primary comparison paths

| Visitor decision | CTA | Destination |
|---|---|---|
| Replace a whole-home ducted system | Show Central Air Options | conditional Central Air panel, then `https://dellahome.com/collections/central-air-conditioner` |
| Add comfort without relying on ductwork | Show Ductless Options | conditional Wall-Mounted Mini Split panel, then `https://dellahome.com/collections/wall-mounted-mini-split` |
| Supplement a problem room or isolated space | Explore This Path | conditional supplemental Mini Split panel plus installer route |
| Not sure | Find My System | `https://dellahome.com/pages/hvac-product-finder` |
| Installation guidance | Find Partner HVAC Installer | `https://dellahome.com/pages/find-a-installer` |

### Ductless subpaths

- One room or one open area → Single-Zone Wall-Mounted Ductless.
- Two or more separated rooms needing independent control → Multi-Zone Wall-Mounted Ductless.
- If stable Shopify filter URLs cannot be generated and QA'd, create dedicated curated collections instead of sending ad traffic to generic mixed-mount Single Zone/Multi Zone collections.

### Supplement path

Keep a visible third answer for homes that already have central air but have a persistent problem room, addition, garage, attic, or other isolated load: retain central air and consider a separate mini split for the specific space. This is guidance, not a bundled or integrated-system promise.

## 5. Product merchandising rules

- The Hero routes to the Project Gateway or Verify section; no PDP cards, prices, discounts, or `Add To Cart` in the first screen. Price and cart actions begin only inside the conditional shopping area.
- The approved shopping area is required and appears immediately after the Project Gateway.
- Use three conditional shopping panels: `Central`, `Ductless`, and `Supplement`. Do not force Ductless and Central into identical UI.
- The Project Gateway is the only path selector. Do not add Ductless/Central/Supplement tabs above the shopping panel. Show a quiet `Change Project` control that returns focus and scroll position to the Gateway.
- The Ductless panel uses four room/zone-led product cards. The Central panel uses four capacity-led cards. The Supplement panel uses a compact category/installer route and does not repeat a third four-product grid.
- With JavaScript disabled, all shopping panels remain present and readable in the DOM. With JavaScript enabled, only the active panel is shown.
- Desktop/laptop shows four cards in one row; tablet/mobile shows two cards per row when readable, matching the PageFly/Memorial merchandising density.
- Product cards are transactional: show the current verified price and use `Add To Cart` as the primary CTA. Keep `View Product` or `View System` as a quieter secondary link.
- A PDP example is a starting point, not a sizing recommendation for a specific home.
- Product identity and source images below are supplied by the project owner and take priority. Live PDP verification is used only to detect conflicts or stale data.
- Ductless card hierarchy: use-case/room label → product image → product title → compact zone/BTU/SEER2 specs → current price → `Add To Cart` → `View Product`.
- Central card hierarchy: prominent BTU capacity → SEER2 and verified DELLA fitting-area reference → product image → product title → current price → `Add To Cart` → `View System`.
- Production price, availability, and purchasable variant ID must come from Shopify Liquid product data whenever the deployment surface supports Liquid. Eight handles fit within Shopify's `all_products` limit of 20 unique handles per page.
- If the chosen PageFly/custom-HTML deployment surface cannot evaluate Liquid product objects, use the Shopify Ajax Product API as the documented fallback rather than silently freezing production snapshots.
- Never take product data from an AI mockup or memory. Record the local/GitHub preview price snapshot and verification date in `sources.md`; the preview snapshot is not the production source of truth.
- If a product is unavailable, replace `Add To Cart` with a disabled `Sold Out` state. If a product requires a variant choice that cannot be resolved safely on the card, route the primary action to the PDP instead of adding an arbitrary variant.
- A product may show direct `Add To Cart` only when exactly one intended, available, purchasable variant can be resolved without customer input. Otherwise show `Choose Options` linking to the PDP.
- In the Shopify storefront, V1 adds the resolved variant using the locale-aware Cart API and then navigates to the store cart in the same tab. Do not build or invoke a theme-specific cart drawer.
- In the static/GitHub preview, cart controls demonstrate layout and states only and must not perform a real cart transaction.
- Do not display compare-at price, automatic discount, rebate, coupon, percentage-off badge, sale badge, or checkout-only promotion in V1.
- Verified DELLA fitting-area ranges may be shown as secondary shopping-reference information on Central Air cards. They must not be presented as a sizing recommendation, and a professional load-calculation disclaimer is required. Do not insert specific Central fitting-area figures until they are live-verified immediately before implementation.
- For Wall-Mounted products, owner-supplied and live-verified coverage information may be shown as secondary reference data. It must not become a page-generated sizing recommendation.
- Localize the supplied CDN images into `assets/products/` during implementation while preserving the source URL mapping.
- The supplied/live primary images for the 24K, 34K, and 47K Central products are identical. Keep the approved image mapping unless the owner supplies alternatives; distinguish those cards with prominent BTU and SEER2 labels.

### Approved product matrix

#### Wall Mount Mini Split

| Shopping role | Product | Verified card data | PDP | Supplied image |
|---|---|---|---|---|
| Single zone / one-room starting point | DELLA Serena Series 12000 BTU 22 SEER2 Mini-Split Heat Pump AC - Up to 550 Sq.Ft. | 12K BTU · 22 SEER2 · Single Zone | `https://dellahome.com/products/serena-series-12000-btu-seer2-22-mini-split-heat-pump-ac-up-to-550-sq-ft` | `https://dellahome.com/cdn/shop/files/048-MS-9K1VR-22S-M-01-O.jpg?crop=center&height=1800&v=1780545014&width=1800` |
| Single zone / larger-space starting point | DELLA Vario Series 18000 BTU 21 SEER2 Mini Split Heat Pump AC - Up to 1000 Sq.Ft. | 18K BTU · 21 SEER2 · Single Zone | `https://dellahome.com/products/vario-series-18000-btu-seer2-21-mini-split-heat-pump-ac-up-to-1000-sq-ft` | `https://dellahome.com/cdn/shop/files/048-TL-9K1VB-19S-1_932732dc-a208-4bf9-bb0d-ee61d0856e0d.jpg?v=1780387243` |
| Two-room starting point | DELLA Vario Series 28000 BTU Dual Zone Mini Split AC (12K + 12K) - Up to 1100 Sq.Ft. | 28K system · 12K + 12K · 20 SEER2 · Dual Zone | `https://dellahome.com/products/vario-series-28000-btu-dual-zone-mini-split-ac-12k-12k-up-to-1100-sq-ft` | `https://dellahome.com/cdn/shop/files/1D3-TL_D1212_89c1fe91-6325-40c2-ac84-e89fd4743a02.jpg?crop=center&height=2000&v=1780905212&width=2000` |
| Four-room starting point | DELLA Vario Series 35000 BTU Quad Zone Mini Split AC (9K + 9K + 9K + 12K) - Up to 1750 Sq.Ft. | 35K system · 9K + 9K + 9K + 12K · 19 SEER2 · Quad Zone | `https://dellahome.com/products/vario-series-35000-btu-quad-zone-mini-split-ac-9k-9k-9k-12k-up-to-1750-sq-ft` | `https://dellahome.com/cdn/shop/files/1D4-TL_Q99912_f8f5c086-8053-4b9a-966b-4f9c394964c7.jpg?v=1780905135` |

#### Central Air

| Shopping role | Product | Verified card data | PDP | Supplied image |
|---|---|---|---|---|
| Ducted Central option | DELLA 24,000 BTU 18 SEER2 Ducted Central Air Conditioner with Air Handler | 24K BTU · 18 SEER2 | `https://dellahome.com/products/della-24-000-btu-18-seer2-ducted-central-air-conditioner-with-air-handler` | `https://dellahome.com/cdn/shop/files/T-24K-I_O_35b1c741-8960-4931-b681-88fc1b1bba17.jpg?v=1783908021` |
| Ducted Central option | DELLA 34,000 BTU 19 SEER2 Ducted Central Air Conditioner with Air Handler | 34K BTU · 19 SEER2 | `https://dellahome.com/products/della-34-000-btu-19-seer2-ducted-central-air-conditioner-with-air-handler` | `https://dellahome.com/cdn/shop/files/T-24K-I_O_35b1c741-8960-4931-b681-88fc1b1bba17.jpg?v=1783908021` |
| Ducted Central option | DELLA 47,000 BTU 18 SEER2 Ducted Central Air Conditioner with Air Handler | 47K BTU · 18 SEER2 | `https://dellahome.com/products/della-47-000-btu-18-seer2-ducted-central-air-conditioner-with-air-handler` | `https://dellahome.com/cdn/shop/files/T-24K-I_O_35b1c741-8960-4931-b681-88fc1b1bba17.jpg?v=1783908021` |
| Ducted Central option | DELLA 53,000 BTU 17 SEER2 Ducted Central Air Conditioner with Air Handler | 53K BTU · 17 SEER2 | `https://dellahome.com/products/della-53-000-btu-17-seer2-ducted-central-air-conditioner-with-air-handler` | `https://dellahome.com/cdn/shop/files/T-60K-I_O_pp1.jpg?v=1783924308` |

## 6. Page structure

The page uses **6 compact blocks** and follows one decision sequence: `Answer → Identify Project → Shop the Right Path → Verify → FAQ → Convert`. It opens directly with the Hero. There is no Benefit Strip, Quick Answer block, independent Home Situations section, Premium Services section, or large standalone Installation section.

### 1. Ecommerce comparison hero — Direct Answer

Purpose: match the query, explain the architectural difference quickly, and send the visitor to the decision control.  
H1: `Ductless Mini Split vs Central Air`  
Supporting copy: `Wall-mounted ductless mini splits give you flexible room-by-room or multi-zone comfort without relying on whole-home ductwork. Central air uses an air handler and duct system to distribute comfort throughout the home. Start with the project you are trying to solve.`  
Primary CTA: `Find My Best Starting Point` → Project Gateway.  
Secondary CTA: `Compare the Tradeoffs` → Verify section.  
Visual: a wide, product-led DELLA ecommerce banner using a Serena 12K packshot and Central 34K system packshot as the initial composition. Do not place product cards in the Hero.

### 2. Project Gateway — What Are You Trying to Solve?

Purpose: convert an abstract equipment comparison into three recognizable projects.  
Format: three accessible button cards on desktop and a single column on mobile. No quiz and no long decision matrix.

- `REPLACE` — `Replace a Whole-Home Ducted System` → `Start with Central Air`.
- `ADD` — `Add Comfort Without Relying on Ductwork` → `Start with Wall-Mounted Mini Splits`.
- `SUPPLEMENT` — `Fix Problem Areas Without Replacing Everything` → `Consider a Supplemental Mini Split`.

Each card must retain one concise condition line, followed by a distinct result line and action button:

- Replace condition: the home already has usable whole-home ductwork. Result: `Start with Central Air`. Button: `Show Central Air Options`.
- Add condition: the project needs comfort without relying on whole-home ductwork. Result: `Start with Wall-Mounted Mini Splits`. Button: `Show Ductless Options`.
- Supplement condition: the central system still serves most of the home, but an isolated space needs more comfort. Result: `Consider a Supplemental Mini Split`. Button: `Explore This Path`.

Treat each result as a starting path, not a guaranteed system prescription. A supplemental mini split is a separate ductless system used to address a specific space; do not describe it as an integrated hybrid package.

Below the three primary cards, add one visually quiet uncertainty escape hatch rather than a fourth project card: `Not sure which project fits? Find My System →` linking to `https://dellahome.com/pages/hvac-product-finder`.

### 3. Conditional shopping area — Shop the Right Path

Initial state: `Choose a Project Above to See Your Starting Options`. Do not default to Ductless or Central for an unparameterized visit.

Do not show a second set of path tabs. The panel heading includes a quiet `Change Project` control that returns the visitor to the Gateway.

- **Ductless:** four room/zone-led cards for the approved 12K single-zone, 18K single-zone, 28K dual-zone, and 35K quad-zone systems. End with `Shop All Wall-Mounted Mini Splits`.
- **Central:** four capacity-led cards for the approved 24K, 34K, 47K, and 53K systems. Capacity is the primary visual cue; SEER2 and any implementation-time live-verified DELLA fitting-area range are secondary shopping-reference information. Capacity and SEER2 labels must visually distinguish the three cards sharing the same supplied image. End with `Shop All Central Air` and `Find Partner HVAC Installer`.
- **Supplement:** one compact category visual and explanation, with `Shop Wall-Mounted Mini Splits` and `Find Partner HVAC Installer`. Do not repeat another product grid.

Card actions: current verified price → primary `Add To Cart` when an unambiguous available variant exists, otherwise `Choose Options` or disabled `Sold Out` → secondary `View Product` for Ductless or `View System` for Central. Do not show promotional language or discount styling. Coverage/fitting-area figures are shopping references only and require a sizing disclaimer. Preserve the asymmetric Ductless and Central card hierarchies above.

### 4. Verify — Compact comparison plus installation reality bar

Comparison heading: `Mini Split vs Central Air: What Actually Changes?`  
Comparison rows: distribution, whole-home ductwork, room control, indoor equipment, installation scope, and retrofit flexibility. Use no winner badge, checkmark contest, or red X. On mobile, each table row becomes a stacked comparison card rather than a horizontally scrolling wide table.

Immediately follow with one compact pale-blue `BEFORE YOU BUY` bar: `Confirm the Installation Before Choosing the Final System`. Mention equipment sizing, duct condition, electrical requirements, line routing, equipment placement, and installation scope. CTAs: `Find Partner HVAC Installer` and `Find My System`.

### 5. Compact FAQ

Use six native `<details>/<summary>` questions:

1. What is the main difference between a ductless mini split and central air?
2. Can a ductless mini split heat and cool an entire house?
3. Can I add a mini split if I already have central air?
4. Does central air require ductwork?
5. Is a mini split always more efficient than central air?
6. How should I size a mini split or central air system?

Keep answers concise and qualified. Add FAQPage JSON-LD only when visible answers are final; schema must exactly match them.

### 6. Contextual final CTA

The CTA updates from the selected project path rather than asking the same question again.

- Default: `Still Deciding?` → `Find My System` + installer.
- Ductless: `Ready to Build Your Ductless Setup?` → Wall-Mounted collection + installer.
- Central: `Ready to Explore Central Air?` → Central Air collection + installer.
- Supplement: `Ready to Target the Problem Area?` → Wall-Mounted collection + installer.

Use a pale-cyan surface rather than a heavy navy promotional banner.

## 7. SEO direction

Primary keyword: `mini split vs central air`  
Primary supporting phrase: `ductless mini split vs central air`

Supporting intent/phrases:

- ductless vs central air;
- mini split vs central AC;
- central air vs mini split;
- mini split or central air;
- multi zone mini split vs central air;
- whole house mini split vs central air;
- mini split for a house without ductwork;
- mini split for an old house;
- central air with existing ductwork;
- ducted heat pump vs ductless heat pump;
- room-by-room temperature control;
- mini split zoning.

These are intent and entity targets, not claims about search volume.

SEO title: `Mini Split vs Central Air: Which Is Right for Your Home? | DELLA`  
Meta description: `Compare ductless mini splits and central air by ductwork, room count, zoning, installation, and comfort goals. Find the DELLA system path that fits your home.`  
H1: `Ductless Mini Split vs Central Air`

Entity coverage should naturally include: ductwork, ductless heat pump, ducted heat pump, outdoor unit, indoor head, air handler, refrigerant lines, supply registers, thermostat, zone control, inverter, SEER2, HSPF2, heating/cooling load, insulation, ceiling height, window exposure, climate/design temperature, electrical service, condensate drainage, and professional load calculation.

Canonical must be omitted until the final Shopify URL is known.

## 8. Claims policy

### Stable facts that may be stated directly

- Ductless mini splits do not require central ductwork.
- A ducted central system distributes conditioned air through ducts/registers.
- Single-zone systems serve one primary zone; multi-zone systems connect multiple indoor zones to an outdoor system.
- DELLA's current wall-mounted collection is the brand's ductless shopping path.
- DELLA's current Central Air products are ducted heat-pump and air-handler systems that provide heating and cooling.

### HVAC guidance requiring qualifiers

Use `can`, `may`, `often`, `typically`, `a starting point`, and `depending on the home` for statements about:

- installation disruption;
- suitability for older homes;
- zoning advantages;
- the value of existing ductwork;
- duct-related losses;
- comfort, noise, efficiency, maintenance, and operating cost.

### Must be confirmed by DELLA or a qualified installer

- exact installed cost, ROI, annual or percentage savings;
- system size for a specific house or room;
- cold-climate capacity and backup heat needs;
- existing-duct and thermostat compatibility;
- electrical/panel work, permits, and code requirements;
- line-set limits and multi-zone connected-capacity rules;
- installation scope, product availability, current policy, warranty, and support claims.

Never declare either system universally cheaper, quieter, more efficient, easier to maintain, or better for resale.

## 9. Visual system

Primary references, in order:

1. `della-memorial-day-design-system.md`
2. `page.pf-ef33e2e6.json.txt`
3. `pf-ef33e2e6.liquid.txt`
4. local Memorial Day screenshots/assets
5. live `https://dellahome.com/pages/coupon-code`
6. existing DELLA comparison pages for information patterns, not as authority to preserve their inconsistent UI.

Required visual grammar:

- Spectral for headings/product titles; Poppins for body, buttons, decision controls, and tables.
- Navy `#0E1953`, blue `#5884E7`, blue hover `#6B95EF`, light surfaces `#EDF2FF`, `#F4F7FF`, and `#DDF7FF`.
- 1200px desktop container; approximately 72–80px desktop and 48–56px mobile section rhythm.
- 4px-radius, 44–48px-high ecommerce buttons.
- Wide, image-led ecommerce hero with separate mobile crop.
- Clean collection/product cards with light borders/shadows; comparison table with light-blue header and no winner badge.
- FAQ late in the page and compact.

Do not use: holiday/coupon content, countdowns, sale red, glassmorphism, purple gradients, decorative orbs, oversized SaaS typography, generic AI icon grids, pill-shaped primary CTAs, heavy shadows, or a hero product carousel.

## 10. Mobile and accessibility

- Design for 390px first, then verify 360px, 430px, 768px, 1024px, 1280px, and 1440px.
- No horizontal page overflow.
- Comparison tables must become readable stacked rows or a clearly signposted accessible horizontal region; do not compress text into unreadable columns.
- Decision controls must be keyboard operable, have visible focus states, and expose selected state to assistive technology.
- Scenario/path cards require adequate tap targets and must not depend on hover.
- Images need concise descriptive alt text; decorative images use empty alt text.
- Respect reduced-motion preference.

### Progressive enhancement and interaction

- Gateway controls must be semantic `<button>` elements with `aria-pressed`, visible focus, and Enter/Space support.
- JavaScript state is `null`, `central`, `ductless`, or `supplement`; selecting a path updates the active card, shopping panel, contextual final CTA, and analytics hook.
- On a user click, smooth-scroll to the shopping area unless reduced motion is requested.
- Support `?path=ductless`, `?path=central`, and `?path=supplement` for ad message matching. A valid URL parameter preselects the path but must not auto-scroll past the Hero.
- When a visitor changes path, use `URL` and `history.replaceState` to update only the `path` query parameter, preserving every other query parameter such as UTM, `gclid`, and `fbclid`. Returning to neutral removes `path`; path changes do not refresh the page or create Back-button history entries.
- The canonical remains the clean, parameter-free Shopify URL.
- All three shopping panels must exist in the HTML. With JavaScript disabled they display sequentially; JavaScript progressively enhances them into conditional panels.
- Add guarded analytics hooks for path selection, PDP clicks, collection clicks, installer clicks, and final CTA clicks. Do not load or initialize a second analytics library, and do not throw an error when `window.gtag` is absent.
- All DELLA PDP, collection, cart, Product Finder, and installer destinations open in the same tab.

## 11. Non-goals

- No full HVAC sizing or cost calculator.
- No universal winner.
- No default recommendation of Multi Zone.
- No long editorial blog layout.
- No Benefit Strip or other pre-Hero module.
- No independent Quick Answer block; the Hero supplies the direct answer.
- No independent Home Situations, Premium Services, or large Installation Guide module.
- No exact installation-cost table, savings percentage, ROI, or monthly-bill estimate.
- No product selection based on square footage alone.
- No promotion/coupon/countdown language.
- No product grid before the visitor sees the Hero and Project Gateway.
- No compare-at price, automatic discount, coupon, rebate badge, sale badge, or hard-coded promotional claim in product cards.
- No attempt to cover cassette, floor-ceiling, or concealed-ducted mini splits as equal primary branches; they may be a short edge-case note or internal link only.

## 12. Resolved decisions

- **Owner override 2026-08-13 (supersedes the V1 Add To Cart rules in §5 and below):** the three single-variant Vario products no longer use `Add To Cart`. Their primary action is `View Product` opening the PDP in a **new tab** (`target="_blank" rel="noopener"`), and the duplicate secondary `View Product` link is removed on those cards. Static-preview cart code and the variant-ID hydration logic were removed with it. The five `Choose Options` cards (Serena 12K + four Central systems) are unchanged and remain same-tab. Reason: in the static/GitHub preview ATC could never transact and felt broken; the owner prefers a clean PDP route for V1.
- **Owner override 2026-08-13 (follow-up):** the Serena 12K card's `Choose Options` + secondary link was also replaced by the same new-tab `View Product` primary action so all four Ductless cards are uniform. Only the four Central cards retain `Choose Options` + `View System`.
- **Owner override 2026-08-13 (final):** the four Central cards' `Choose Options` + `View System` were also replaced by the same new-tab `View Product` primary action. All eight product cards are now uniform: price → navy `View Product` (new tab). The `View Product`/`View System` asymmetry and all cart/variant rules in §5 are fully superseded for V1.
- **Owner override 2026-08-13 (Hero):** hero lead shortened to one ~25-word paragraph; the secondary `Compare the Tradeoffs` CTA is removed — it leaked visitors past the Project Gateway, which conflicts with the page's first job. Single primary CTA `Find My Best Starting Point` → Gateway. Hero imagery is now a single composed `hero-vs.webp` (owner-supplied product banners composited; plain lowercase "vs" wordmark, no badge, per owner review, 1157×503).
- **Owner override 2026-08-14 (comparison H2):** "Mini Split vs Central Air: What Actually Changes?" → "Mini Split vs Central Air: What Changes?" — "actually" is a humanizer §7 watch word; owner delegated the call and approved removal. Supersedes §6.4's heading text.
- **Owner override 2026-08-14 (confidence-gate refinements, from merged ChatGPT+Kimi review):** (1) Ductless gateway card widened to "Condition Your Home or Spaces Without Relying on Ductwork" with condition "Condition one room, several rooms, or a whole home without a duct system." — covers whole-home no-duct projects without a fourth card. (2) Comparison table gains two number-free rows: Primary Cost Drivers and Efficiency Depends On. (3) Neutral shopping state slimmed from a dashed placeholder box to one quiet line. (4) Hero primary CTA becomes path-matched when a path is active ("See Central Air Starting Points" / "See Wall-Mounted Mini Splits" → #shop-path), restoring "Find My Best Starting Point" in neutral. (5) og:image added (generated asset; absolute CDN URL at integration). (6) 24/7 Live Support links to the verified `dellahome.com/pages/contact`. Rejected from the same review: deleting Premium Della Services (owner-added for ad trust) and restoring the FAQ to six (owner-trimmed duplicates).
- **Owner override 2026-08-13 (visual):** button system and product-card styling follow the Ceiling Cassette vs Wall Mount reference page (navy primary with invert hover, gray-border outline with blue-light hover, square-corner product cards with hover zoom); section H2s and their subheadings are left-aligned rather than centered; the final CTA's installer action is a quiet text link instead of a third identical button.
- **Owner override 2026-08-13 (FAQ content):** the six-question FAQ is trimmed to four — "What is the main difference…" (duplicates the Hero direct answer) and "Does central air require ductwork?" (duplicates the comparison table row) are removed. FAQPage JSON-LD reduced to the same four entries, byte-matched. This supersedes §6.5's six-question list.
- **Owner override 2026-08-13 (FAQ layout):** FAQ switches from the two-column numbered layout to the Ceiling Cassette vs Concealed Ducted reference style: single column, Spectral 20px questions, chevron affordance, blue open/hover state. Content unchanged apart from the trim above.
- **Owner override 2026-08-13 (Services module):** despite §11's non-goal, the owner approved adding the `Premium Della Services` trust section (Free & Fast Shipping / 30-Day Money-Back / 24/7 Live Support / Lifetime Warranty, copied from the sizing-calculator mockup) between the Verify installation bar and the FAQ, because the page also serves as an ad landing page where trust elements matter. Policy copy is owner-supplied from the approved mockup.

- Page classifier: Comparison guide.
- Primary decision: identify whether the project is Replace, Add, or Supplement, then route to the appropriate starting path.
- Primary routing: two main collections plus eight owner-approved PDPs.
- Ductless primary collection: Wall Mounted Mini Split.
- Central primary collection: Central Air Conditioner.
- Multi Zone is not the universal recommendation.
- Hero is a DELLA ecommerce comparison banner, not a blog header or product carousel.
- The page opens directly with the Hero; there is no pre-Hero content module.
- Page purpose is conversion-led guided shopping, not long-form education.
- The Project Gateway is the primary decision control and uses Replace / Add / Supplement.
- Gateway cards retain a concise condition, separate recommended starting result, and action-oriented button.
- Not Sure is a quiet Product Finder escape hatch beneath the three Gateway cards, not a fourth project path.
- The approved conditional shopping area appears immediately after the Project Gateway.
- Gateway is the only path selector; the shopping area has no duplicate tabs and provides only a quiet `Change Project` return control.
- Ductless and Central use deliberately asymmetric merchandising: room/zone-led versus capacity-led.
- Supplement uses a compact category/installer route rather than a repeated product grid.
- The initial organic state is neutral; advertising may preselect a path with a validated `?path=` parameter.
- Final CTA copy and destination update from the selected path.
- Wall Mount product ladder: 12K Single Zone, 18K Single Zone, 28K Dual Zone, and 35K Quad Zone.
- Central product ladder: 24K, 34K, 47K, and 53K ducted systems with air handlers.
- V1 product cards display current verified price and use `Add To Cart` as the primary action, with `View Product` or `View System` as a secondary link.
- Ductless cards remain use-case/room-led; Central cards remain capacity-led even though both can display price and cart actions.
- Production price, availability, and variant IDs are Liquid-first Shopify data; Ajax Product API is the fallback only where PageFly cannot bind Liquid. Local-preview snapshots must be dated and must not become the production source of truth.
- Direct ATC requires one unambiguous available variant; variant choice routes to PDP and unavailable products show `Sold Out`.
- Successful production V1 ATC navigates to the DELLA cart in the same tab; GitHub/static preview performs no cart transaction.
- All DELLA shopping/support destinations use same-tab navigation.
- Path changes preserve every existing query parameter, update only `path` via `replaceState`, and remove it when returning to neutral.
- Supplied product image URLs are the identity source and will be localized during implementation.
- Product data/prices will not be invented or taken from an AI mockup.
- The supplied ChatGPT implementation brief is approved as strategic input, subject to this PRD's removal of the Benefit Strip and its HVAC claim/data guardrails.
- `Design.png` is the approved visual reference and will not be regenerated. `DESIGN.md` overrides its obsolete duplicate tabs and `View Product`-only product cards.
- Target Shopify URL: `https://dellahome.com/pages/ductless-mini-split-vs-central-air`. Production canonical is enabled only after the Shopify Page/handle exists and is confirmed, using Shopify's Liquid `canonical_url`; the static/GitHub preview does not hard-code a production canonical.
- Final HTML is gated behind this approved PRD, the approved `Design.png`, `DESIGN.md`, and `PLAN.md`.

## 13. Implementation handoff

- Approved mockup: `Design.png`. Do not regenerate it; document all PRD-over-mockup changes in `DESIGN.md`.
- Keep the owner-supplied repeated Central product-image mapping for V1 and distinguish cards with prominent capacity/SEER2 labels unless the owner supplies approved alternatives.
- Immediately before implementation, live-verify all eight products, official Central fitting-area wording, price, availability, and intended variant state; record the snapshot and date in `sources.md`.
- Confirm whether the final Shopify placement evaluates Liquid. Use Liquid/all_products when supported; otherwise use the Ajax Product API fallback documented in `PLAN.md`.
- Confirm the actual Shopify Page handle before enabling `canonical_url` in production.

## 14. Acceptance criteria

- The first screen clearly matches `ductless mini split vs central air` intent.
- A visitor can select Replace, Add, Supplement, or Not Sure without reading the full page.
- The conditional shopping area appears immediately after the Project Gateway.
- Ductless and Central panels each show four correct products with working PDP CTAs; Supplement does not duplicate the grids.
- The Project Gateway includes a visible `Not sure which project fits? Find My System →` escape hatch without adding a fourth card.
- Gateway cards include concise conditions, distinct result lines, and action buttons; no duplicate path tabs appear in the shopping area.
- Product cards use the approved image mapping, verified BTU/SEER2/zone data, current verified price, working `Add To Cart`, and a secondary PDP link, with no promotion residue.
- Add-to-cart uses the correct purchasable Shopify variant, handles unavailable products safely, and never silently adds an arbitrary variant when a choice is required.
- Successful production ATC reaches the DELLA cart in the same tab; static/GitHub preview cannot modify a real cart.
- Central cards may show only live-verified DELLA fitting-area ranges as secondary reference data, paired with a professional load-calculation disclaimer; unverified figures are omitted.
- No path incorrectly treats every mini split shopper as Multi Zone.
- Collection links are verified and message-matched.
- Project selection updates the active state, visible shopping panel, contextual final CTA, and analytics attributes.
- `?path=central`, `?path=ductless`, and `?path=supplement` preselect correctly without auto-scrolling.
- Path changes preserve all non-path query parameters and use `replaceState`; clearing the choice removes `path`.
- With JavaScript disabled, all shopping paths remain visible and usable.
- Central content accurately represents the current ducted heat-pump/air-handler assortment.
- Product, policy, price, availability, variant, sizing, and savings claims are live-verified or omitted.
- Page visually follows the current DELLA PageFly/Memorial/coupon ecommerce system.
- Mobile, keyboard, focus, accordions, decision controls, links, and schema are QA'd before approval.
- No horizontal overflow at 360px, 390px, 430px, 768px, 1024px, 1280px, or 1440px.
- No commit or push occurs before browser QA and explicit owner approval.

## 15. Research inputs reviewed

- DELLA live Wall Mounted Mini Split collection
- DELLA live Central Air Conditioner collection
- DELLA live Central Air product details
- All eight owner-supplied product PDPs and their primary-image mappings
- DELLA live Coupon Code page
- Local Memorial Day design-system markdown, PageFly JSON/Liquid export, and screenshots
- Five existing DELLA comparison-page HTML files supplied by the project owner
- ChatGPT web-research output, audited against the live DELLA sources above
- Approved `Design.png`, reviewed against this PRD
- Shopify official Cart API reference, `all_products` Liquid object reference, and theme SEO metadata/canonical guidance, reviewed 2026-08-13
