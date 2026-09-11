# HANDOFF - 12000 BTU vs 18000 BTU Mini Split

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

Project path: `C:\Users\18041\Desktop\della-pages\12000 BTU vs 18000 BTU Mini Split`

Primary HTML: `12000-btu-vs-18000-btu-mini-split.html`

## Current Objective

Continue refining the Della topical decision landing page for `12000 BTU vs 18000 BTU Mini Split`.

The page should help shoppers decide whether to start with the 12000 BTU collection or the 18000 BTU collection. It should feel like a Della ecommerce decision page, not a generic article, calculator, or hard-sell product grid.

## Source Priority

Use this priority if anything conflicts:

1. User's latest explicit instruction in the active conversation.
2. This `HANDOFF.md` and `NEXT_CODEX_PROMPT.md`.
3. `PRD.md`.
4. `DESIGN.md`.
5. `PLAN.md`.
6. Approved design draft image.
7. Existing Della reference pages and Della/PageFly design-system files.

Important: several late visual revisions override older PRD/PLAN notes. Do not restore the old comparison table, old hero two-image treatment, or longer scenario/factor copy from earlier docs.

## Current Files

- `PRD.md`
- `DESIGN.md`
- `PLAN.md`
- `implementation-notes.md`
- `HANDOFF.md`
- `NEXT_CODEX_PROMPT.md`
- `12000-btu-vs-18000-btu-mini-split.html`
- `12k vs. 18k Design Drafts.png`
- `12k.webp`
- `18k.webp`
- `12k-hero-transparent.webp`
- `18k-hero-transparent.webp`
- `hero-12k-18k-showcase.webp`
- `assets/`

## Current Page Structure

Current section order:

1. `hero`
2. `choose-section`
3. `factors-section` with `id="sizing-factors"`
4. `right-size-section`
5. `products-section`
6. `scenarios-section`
7. `services-section`
8. `faq-section`
9. `bottom-cta`
10. `mobile-sticky`

The old standalone `compare-section` / `12K vs 18K at a glance` module was removed because it duplicated `choose-section`. Do not restore it unless the user explicitly asks.

## Latest Approved Strategy

- Page type: Della topical decision landing page.
- Audience: US Della shoppers, natural American English.
- Balance: expert sizing judgment first, ecommerce routing second.
- Routing: collection-first, PDP-second.
- Hero and decision CTAs route to collections:
  - `https://dellahome.com/collections/12000-btu-mini-split`
  - `https://dellahome.com/collections/18000-btu-mini-split`
- Product cards remain locked to the 8 approved PDPs only. Do not auto-fill or replace from collections.
- Product card CTA: `View Product`.
- Della same-site collection/PDP links open in same tab, no `target="_blank"`.
- No calculator, no inputs, no sliders.
- No canonical for now.
- No FAQ schema for now unless the user asks.
- No sale/coupon/countdown language.
- Conservative sizing language only: use `common reference`, `worth checking`, `may`, `depends`, and installer confirmation language. Do not imply guaranteed coverage or guaranteed savings.

## Latest Implementation Notes

### Global H2 Style

- Every visible page `h2` should use the inspector-screenshot style.
- Global `h2` CSS is the source of truth: `#0E1953`, `Spectral, Georgia, serif`, about `32px`, `font-weight: 400`, `line-height: 1.14`.
- Do not add section-specific `h2` font-family, font-size, weight, or color overrides unless the user explicitly asks.

### Hero / Banner

- H1 must remain: `12000 BTU vs 18000 BTU Mini Split: When to Size Up`.
- Hero subcopy is one concise sentence: `Worried a 12000 BTU mini split will struggle, but an 18000 BTU mini split will overshoot your room?`
- Hero background is `#CBDCF6`.
- Hero right side now uses one unified showcase image: `hero-12k-18k-showcase.webp`.
- Do not rebuild hero right side with two `.hero-product` blocks, `.hero-badge`, `12k.webp`, or `18k.webp`.
- The user explicitly rejected the two independent product-card-like hero blocks.
- The current showcase asset was edited so the image border/background blends into `#CBDCF6` and the obvious base/floor shadow is removed from the image pixels.
- Do not alter the machine units or recreate the base unless the user asks; recent complaint was only about the remaining bottom shadow.
- Hero CTAs only:
  - `Shop 12000 BTU Mini Splits`
  - `Shop 18000 BTU Mini Splits`
- The temporary hover change that made 12K buttons turn white was rolled back. Do not reapply it unless the user asks again.

### Choose Section

- Section title: `Choose the path that fits the room`.
- Section intro copy was removed.
- This is the only quick 12K/18K routing module.
- Two choice cards use left blue inline SVG house icons and right-side content.
- Cards have more relaxed height and bullet spacing; preserve the less-crowded feel.
- Body text was shifted left for more room, and CTAs are bottom-aligned.
- Keep CTA styling consistent with current page button system.

### Icon System For Choose + Sizing Factors

- Only `choose-section` and `factors-section` icons were intentionally optimized.
- Keep inline SVG only. Do not use icon fonts, external images, remote resources, third-party icon libraries, gradients, badges, or filled icons.
- Choose icons use unified `viewBox="0 0 64 64"`, `fill="none"`, `stroke="currentColor"`, round caps/joins, CSS-controlled Della blue `#5884E7`.
- Factor icons use unified `viewBox="0 0 24 24"`, `fill="none"`, `stroke="currentColor"`, round caps/joins, CSS-controlled Della blue `#5884E7`.

### Sizing Factors / What Can Move The Decision

- Section title: `What can move the decision?`.
- This section should be compact and design-draft-like, not long-copy cards.
- Desktop target: 6 cards in one row.
- Each card has: blue inline SVG icon, compact title, very short explanation, and `.tag` at the bottom.
- Tags should stay one line where possible:
  - `May push toward 18K`
  - `May support 12K`
  - `Needs installer review`
- Keep tags in the current pale-blue style. Do not change to orange/green warning badges unless user asks.

### Bigger Is Not Always Better

- Keep the section short and visual.
- Do not imply 18K is bad. Frame risks as `Oversized system risk`.

### Products

- Product set is locked to 8 PDPs, 4 for 12K and 4 for 18K.
- Product cards show prices captured from live PDPs at implementation time.
- If prices are refreshed and any specified PDP cannot be reached or parsed, stop and report missing items.
- Do not hide sold-out products and do not replace SKUs.
- Keep `View Product` CTA.
- Product image containers use `var(--blue-surface)` and product images use `mix-blend-mode: multiply` to reduce visible white image backgrounds.

### Scenarios

- This section follows the compact design draft, not the earlier long-copy version.
- Section title is left-aligned: `Which Room Sounds Most Like Yours?`, using the same global H2 style.
- No intro paragraph under the title.
- Keep 4 scenario cards only, each with image + room line with arrow + one sizing cue line:
  - `Bedroom or home office ->` / `12K starting point`
  - `Small living room ->` / `12K or 18K based on layout`
  - `Garage or sunroom ->` / `check 18K`
  - `Open living and dining area ->` / `18K starting point`
- Do not restore explanatory paragraphs inside scenario cards.

### Services

- Premium Della Services was copied from the single-zone reference page.
- Do not change this section unless the user asks.

### FAQ

- Keep 5 compact buyer-anxiety FAQs.
- FAQ visual/interaction style follows `single-zone-vs-multi-zone-mini-split.html` reference FAQ, while preserving this page's font system.
- FAQ uses divider-line `details/summary` rows, navy default question text, brand-blue hover/open question text, and rotating arrow icon.
- FAQ question font should use `Spectral, Georgia, serif`.
- Q4 is `Is bigger always safer when choosing between 12K and 18K?`.
- Do not add FAQ schema unless asked.

### Bottom CTA / Mobile Sticky

- Bottom CTA: two collection path cards only.
- Mobile sticky CTA is approved:
  - `Shop 12K`
  - `Shop 18K`
- Desktop should not show sticky CTA.
- Keep page bottom padding so sticky CTA does not cover bottom CTA.

## Pilot QA — 2026-09-11

40/40 checks passed across 1440, 1280, 1024, 768, 430, 390 and 360px. Includes overflow, both capacity anchors and focus, uncertain-user link, all five factor panels/annotations, arrow/Home/End navigation, mobile shopping-bar states, FAQ keyboard operation, image loading, no script errors, no-JavaScript navigation and complete factor copy, retained products and unchanged schema status.

Desktop/mobile screenshots reviewed against the approved layout. Evidence: `C:\Users\18041\Documents\Playground\della-ui-review-20260911\12k-18k-approved`.

Prices and policy statements were not refreshed; Shopify theme overlays, screen-reader testing and conversion impact remain unverified. No commit/push requested.

## Earlier QA Status

Latest checks performed after hero asset update:

- Hero image source is `hero-12k-18k-showcase.webp`.
- Hero background computed as `rgb(203, 220, 246)` / `#CBDCF6`.
- Hero image natural size: `1672 x 941`.
- Desktop check at about 1440px: no horizontal overflow.
- Mobile check at about 390px: no horizontal overflow.
- Pixel-level check confirmed the old bottom shadow areas in the official hero asset were replaced with `#CBDCF6`-matching background in sampled lower-floor points.

Earlier static/source checks:

- choice cards: 2
- compare sections: 0
- factor cards: 6
- product cards: 8
- scenario cards: 4
- FAQ items: 5
- no old `compare-section`, no old `12K vs 18K at a glance` heading

Recommended next QA before Shopify paste-in:

- Visual pass in actual browser at 1440, 1280, 430, and 390 widths after any new change.
- Re-verify static product prices before publication because prices are snapshots.

Additional QA performed on 2026-06-23:

- Static source check confirmed: `hero-12k-18k-showcase.webp` is used once; `.hero-product` blocks are absent; `compare-section` is absent; no `12K vs 18K at a glance` heading; no FAQ schema; no canonical; no Della same-site links using `target="_blank"`.
- Browser viewport checks passed at 1440px desktop, 1280px laptop, 430px mobile emulation, and 390px mobile emulation.
- No horizontal overflow was detected at the checked desktop or mobile widths.
- Hero background remains `rgb(203, 220, 246)` / `#CBDCF6`; hero image natural size remains `1672 x 941`; mobile hero image stays inside the viewport.
- Global visible `h2` styling still matches the inspector-approved style: Spectral/Georgia, `32px`, weight `400`, navy `#0E1953`.
- Mobile sticky CTA displays only on mobile, stays about 64px tall, and does not overlap the bottom CTA at page end.
- FAQ click check passed; the first FAQ row opens as expected.
- Product cards still show the 8 locked products and static prices from `implementation-notes.md`.

## Known Risks / Notes

- Product prices are static snapshots. Re-verify before Shopify paste-in or final publication.
- Some docs may still mention old structure; use this handoff and latest user instruction as current truth.
- Hero asset has been edited directly; if a future user asks to restore prior shadows/background, use source history or backup assets rather than guessing.
- No commit/push is currently approved in this latest handoff context.

## Next Action

In the next conversation, start by reading `HANDOFF.md` and `NEXT_CODEX_PROMPT.md`, then only continue the user's requested visual/content refinement. Do not broaden scope, restore old removed sections, add schema, change product set, or commit/push unless explicitly requested.
