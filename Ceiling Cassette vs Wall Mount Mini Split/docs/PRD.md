# Ceiling Cassette vs Wall Mount Mini Split PRD

## Objective

Create an evergreen Della decision landing page for `Ceiling Cassette vs Wall Mount Mini Split` that supports research-led organic traffic and paid ad traffic.

## Target URL

Shopify target path: `/pages/ceiling-cassette-vs-wall-mount-mini-split`

Local demo path: `Ceiling Cassette vs Wall Mount Mini Split/ceiling-cassette-vs-wall-mount-mini-split.html`

## Primary Audience

- Homeowners comparing indoor unit types before buying.
- Ad visitors searching for a fast answer and a product path.
- Researchers deciding whether ceiling access, wall space, airflow, or visual finish matters more.

## Positioning

Wall mount is the default choice for most homes because it is easier to place, simpler to install, and more familiar for single-room upgrades. Ceiling cassette is the better fit when shoppers want a cleaner built-in look, have usable ceiling space, or need more even airflow in an open room.

## Conversion Paths

- Primary: Wall-Mounted Mini Splits collection.
- Secondary: Ceiling Cassette Mini Split collection.
- Product-level: four ceiling cassette PDPs and four wall mount PDPs.

## SEO Intent

- Primary keyword: ceiling cassette vs wall mount mini split.
- Secondary themes: ceiling cassette mini split, wall mounted mini split, mini split indoor unit types, mini split for open room, ceiling cassette installation requirements.

## Scope

Included:
- Standalone HTML page.
- Local product images and fonts.
- Full-bleed lifestyle hero with desktop/mobile `picture` sources.
- Overlay commerce navigation for Ceiling Cassette, Wall Mount, Compare Fit, and Find Installer.
- Two quick-answer path cards, a five-question decision checker, stacked mobile comparison cards, lifestyle room-fit cards, installation feasibility checks, collection path cards, and popular comparison picks.
- Product picks with BTU, area, system type, use case, and `See Current Price` / `View Product` CTAs.
- Shopify handoff notes.
- Docs-first planning and acceptance harness.

Excluded:
- Shopify Liquid implementation.
- Dynamic Shopify product cards.
- Live 301 redirect setup.
- Promotion, coupon, or compare-at price content.

## Acceptance Criteria

- Page opens locally and through GitHub Pages.
- H1 and title target the comparison keyword.
- Above the fold gives a clear recommendation and two collection CTAs.
- Hero uses local desktop/mobile lifestyle banners and no product mockup comparison stage.
- Product area starts with two collection path cards, then shows popular picks without static demo pricing notes.
- All critical visuals load from local files.
- Mobile hero, commerce nav, comparison, product cards, FAQ, and bottom CTA do not create horizontal overflow.
- No old blog URL competes as the intended final canonical target.
- Only scoped files are staged and committed.

## Product-card reuse — 2026-09-14

Owner authorized continuing the single-page rollout. Current implementation preserves eight products, their original PDP and Add to Cart variant IDs, the four project sets, checker logic, hero, comparison, room scenes, services and FAQ. Cards display installation style, short series/title, capacity or indoor combination, separate outdoor capacity, voltage, efficiency, coverage, full-name disclosure and the selected variant price. Two single-zone cassette cart variants have no line set; cards label that configuration and link to the original PDP for line-set selection. Vario 12K price is updated to the verified $779.96. Source evidence: commerce-product-data.json.

Desktop uses four columns from 1200px, medium screens two, and mobile through 780px one card with full-width specifications, disclosure and purchase. Static default cards and dynamic project renders match. Arrow keys/Home/End operate the project tabs. Local Chrome verification: 56/56 checks across four groups at 1440/1280/1199/1024/800/780/430/390/360px, product text at 200% on 390/1024px, model disclosure, original checker, comparison toggle, no-JS initial cards, images, metadata/schema preservation and script errors. Cart destinations were inspected without adding items.

Evidence and backup: C:/Users/18041/Documents/Playground/della-ui-review-20260911/cassette-wall-pilot-20260914/. Prices are dated snapshots; shared hydration and Shopify-theme integration remain separate. Local review is ready; this revision has not been committed or pushed. Next action: visual review and explicit publication instruction, then the next single page.