# PLAN: Ceiling Cassette vs Concealed Ducted Mini Split

## Status And Execution Gate

- Status: Approved; Step 5 acceptance run completed with blockers
- Date: 2026-07-14
- Approved inputs: `PRD.md`, `DESIGN.md`, `CONTEXT.md`, the three mockup images, the two product-layout screenshots, and ADR 0001
- Current gate: Step 5 static-preview acceptance blocked
- Current implementation step: Step 5 executed; not accepted
- Next permitted action: replace/approve the two project-scene assets, record named HVAC/product review, then rerun Step 5; do not begin Liquid or JSON
- Not authorized by this plan alone: Shopify theme deployment, production publication, git commit, or git push

## Step 5.1 — Final Local Image Integration

Status: Source implementation and static validation complete on 2026-07-15; browser validation is blocked by local `file:` URL policy.

Scope:

- Replace only the Hero, Quick Answer, Project Fit, Key Differences, and Installation Requirements visuals with the user-supplied local final files.
- Keep the approved page copy, products, prices, collection/PDP routes, tracking attributes, FAQ, and product-tab JavaScript unchanged.
- Remove the former Hero product composition, Key Differences overlays/SVG arrows/labels, installation inline SVGs, and Project Fit placeholder media.
- Do not add a standalone-preview benefit strip; Shopify production uses only the active theme chrome.
- Replace the Trust financing item with the user-approved pre-purchase guidance item; do not add financing or expanded warranty claims.

Harness:

- Confirm exact relative image paths, intrinsic dimensions, `loading`/`decoding` attributes, and no obsolete composite or placeholder selectors in source.
- Serve the local preview and check image load, console, overflow, CTA/tab/FAQ behavior, and responsive layouts at 1440, 1200, 768, and 390 pixels.
- Treat unavailable local-browser automation as a named verification blocker rather than claiming visual acceptance.

## Objective

Build one comparison-focused Della Landing Page Body in two delivery forms:

1. A local/GitHub static preview with dated, verified Preview Prices and no Header or Footer.
2. A dedicated Shopify Online Store 2.0 section plus JSON page template with dynamic Production Prices and the active theme's normal Header and Footer exactly once.

Both forms must preserve the frozen nine-section decision path, approved product sets, Della visual system, responsive behavior, accessibility behavior, and collection/PDP routing.

## Scope Boundaries

In scope:

- The nine approved sections only.
- Two mutually exclusive product tabs with four products per tab.
- Shared CSS and JavaScript behavior across preview and Shopify builds.
- Static preview prices captured from current Shopify data.
- Dynamic Shopify prices resolved from the eight approved product handles.
- Conceptual planning diagrams that show only approved planning relationships.
- SEO-ready semantic markup, stable tracking attributes, and FAQ schema only after FAQ copy is approved.
- Browser and Shopify integration QA.

Out of scope:

- New page modules, a calculator, quiz, sticky bar, newsletter, or promotion.
- PageFly components or a PageFly Custom Code implementation.
- Custom Header, navigation, or Footer markup.
- `Add to Cart`, cart URLs, ratings, compare-at prices, coupons, or sale badges.
- Product substitution without user approval.
- Official-looking installation diagrams, exact dimensions, DIY procedures, or unverified claims.
- Automatic propagation of UTM or click IDs unless the existing Della measurement implementation proves it is required.
- A duplicate `index.html`.

## Source Of Truth

Apply sources in this order:

1. Latest explicit user instruction.
2. `PRD.md` for scope, products, copy roles, facts, routes, and acceptance.
3. `DESIGN.md` for visual composition, responsive behavior, and mockup overrides.
4. `CONTEXT.md` for canonical terminology.
5. ADR 0001 for production architecture.
6. Approved local reference HTML and saved screenshots.
7. The three mockup images for composition only.

Mockup text, prices, technical drawings, and policy copy are never factual sources.

## Planned File Structure

All deliverables stay under:

`C:\Users\18041\Desktop\della-pages\Ceiling Cassette vs Concealed Ducted Mini Split`

Existing and planned files:

| Path | Responsibility | Stage |
| --- | --- | --- |
| `PRD.md` | Product and acceptance source of truth | Existing; updated at gates |
| `DESIGN.md` | Approved visual and responsive rules | Existing; approved |
| `CONTEXT.md` | Canonical project language | Existing |
| `PLAN.md` | Ordered implementation and verification plan | This gate |
| `AGENTS.md` | Project-specific workflow, verification, and repository rules | Step 1 |
| `TECH_STACK.md` | Minimal technical choices and tradeoffs | Step 1 |
| `docs/ARCHITECTURE.md` | Preview/Shopify boundaries and data flow | Step 1, then updated |
| `docs/MODULARITY.md` | File ownership and maintainability constraints | Step 1, then updated |
| `docs/PROGRESS.md` | Step-by-step execution evidence | Step 1 onward |
| `docs/adr/0001-use-os2-section-and-json-template.md` | Accepted production architecture | Existing |
| `implementation-notes.md` | Price snapshot, claim checks, source records, asset gaps | Step 1 onward |
| `HANDOFF.md` | Current implementation and QA state | Step 1 onward |
| `ceiling-cassette-vs-concealed-ducted-mini-split.html` | Header/Footer-free local and GitHub preview | Steps 3-4 |
| `assets/della-hidden-mini-split-comparison.css` | Shared namespaced visual and responsive system | Step 2 |
| `assets/della-hidden-mini-split-comparison.js` | Shared tabs and minimal measurement helpers | Steps 2 and 4 |
| `assets/images/` | Approved hero, project, diagram, and localized review assets | Steps 1-2 |
| `sections/ceiling-cassette-vs-concealed-ducted-mini-split.liquid` | Dedicated Shopify Landing Page Body | Step 6 |
| `templates/page.ceiling-cassette-vs-concealed-ducted.json` | Dedicated OS 2.0 template containing the section once | Step 7 |

The root project-document convention is retained because it is already established. Do not create duplicate copies under `docs/`.

## Product And Collection Data Contract

The implementation uses exactly two System Types and exactly four products per Recommended Product Set.

| System Type | Product handle | Role | Badge |
| --- | --- | --- | --- |
| Ceiling Cassette | `della-12-000-btu-seer2-22-ceiling-cassette-ductless-mini-split-ac-up-to-550-sq-ft` | Smaller single-zone | None |
| Ceiling Cassette | `della-18-000-btu-seer2-20-5-ceiling-cassette-ductless-mini-split-ac-up-to-1000-sq-ft` | Open-space starting point | Recommended Starting Point |
| Ceiling Cassette | `18000-btu-dual-zone-ceiling-cassette-mini-split-ac-9k-12k-up-to-950-sq-ft` | Dual-zone | None |
| Ceiling Cassette | `27000-btu-tri-zone-ceiling-cassette-mini-split-ac-9k-12k-12k-up-to-1500-sq-ft` | Tri-zone | None |
| Concealed Ducted | `della-11000-btu-19-seer2-concealed-ducted-mini-split-air-conditioner` | Smaller single-zone | None |
| Concealed Ducted | `della-22000-btu-19-seer2-concealed-ducted-mini-split-air-conditioner` | Hidden-layout starting point | Recommended Starting Point |
| Concealed Ducted | `della-27000-btu-dual-zone-concealed-ducted-mini-split-heat-pump-ac-9-5k-17k` | Dual-zone | None |
| Concealed Ducted | `della-34000-btu-tri-zone-concealed-ducted-mini-split-heat-pump-ac-9-5k-11k-17k` | Tri-zone | None |

Collection Paths:

- Ceiling Cassette: `https://dellahome.com/collections/ceiling-cassette-mini-split`
- Concealed Ducted: `https://dellahome.com/collections/concealed-ducted-mini-split`

Implementation rules:

- Preview product identity, URLs, and approved CDN image URLs come from the PRD.
- Preview prices are captured from live Shopify on the implementation date and recorded in `implementation-notes.md` with source and timestamp.
- Shopify resolves the eight exact product handles and renders current price through Liquid money filters. Use `From` only when the product price varies.
- Product titles, URLs, images, and price sources must be reconciled against the PRD before release. No handle, product, or image substitution is silent.
- If a product is missing, unavailable, conflicts with the PRD, or has no reliable price, publication stops for user review.
- Only the selected System Type's four cards are visible. DOM and assistive-technology state must agree about which panel is active.

## Asset Contract

- The full-page mockups and product-layout screenshots are review references only and are not embedded or sliced.
- Product cards use the exact approved Della CDN image URLs unless a localized copy is required for stable preview review.
- Hero and four project-scene images use the user-supplied final local source map.
- Installation diagrams use the user-supplied conceptual local planning files; no extra technical overlays or AI raster cutaways are permitted.
- Trust icons are taken from the approved local `Premium Della Services` reference and their current source is recorded.
- Existing Spectral and Poppins assets should be reused or localized when available. Do not add a new font dependency when existing theme or project assets satisfy the design.
- Every retained image has an origin, usage purpose, alt-text decision, and localization status in `implementation-notes.md`.

## Shared Implementation Rules

- Namespace page classes and selectors so the section does not leak styles into the Shopify theme.
- Share the same CSS and JavaScript files between preview and production where Shopify asset loading permits it.
- Keep JavaScript progressive: content and links remain usable without JavaScript; JavaScript enhances tab state and optional measurement hooks.
- Use native `details` and `summary` for FAQ unless a verified accessibility issue requires another implementation.
- Use semantic table markup on wider screens and an accessible stacked presentation on small screens without duplicating conflicting assistive content.
- Use explicit image dimensions or aspect ratios to limit layout shift.
- Same-site production links open in the same tab. Preview links may open Della in a new tab with `rel="noopener"`, and that difference must be recorded.
- Stable `data-` attributes identify CTA location and destination path. Do not invent analytics event names.
- Do not copy ad query parameters to outbound links unless Della's existing tracking convention requires it; native analytics attribution is preferred over URL fragmentation.

## Implementation Steps

### Step 1 — Lock Sources, Assets, Claims, And Project Memory

Result: Completed on 2026-07-14 with the unresolved Hero/project-scene asset decision and unavailable active Shopify theme environment recorded as blockers for later acceptance.

Goal:

Create a verified implementation input set before UI code is written.

Spec:

- Add project-specific `AGENTS.md`, `TECH_STACK.md`, architecture, modularity, progress, implementation-notes, and handoff documents without duplicating PRD/DESIGN intent.
- Inspect the two approved local reference HTML pages and the Della design-system files for exact component assets and integration conventions.
- Verify all eight live PDPs for title, URL, availability, current selling price, price variability, and current image behavior.
- Record a dated Preview Price snapshot for each product.
- Verify the installer route and the four Premium Della Services labels against current Della sources.
- Locate official product manuals and record what installation relationships are supported across each relevant family; unresolved multi-zone concealed-ducted manuals remain explicitly unverified.
- Create the hero/project-scene asset map and identify any asset that still needs user supply or generation.
- Inspect available target-theme integration information. If no active theme source or preview environment is available, record that Shopify integration remains a later external validation gate.
- Draft final FAQ answers from approved claims and mark them pending content approval before schema is enabled.

Likely files:

- `AGENTS.md`
- `TECH_STACK.md`
- `docs/ARCHITECTURE.md`
- `docs/MODULARITY.md`
- `docs/PROGRESS.md`
- `implementation-notes.md`
- `HANDOFF.md`
- `assets/images/`

Acceptance criteria:

- Eight products have a complete source record and no silent substitutions.
- Eight current Preview Prices and a capture date are recorded.
- Trust labels and installer URL have current evidence or are marked as blockers.
- Every hero/project asset has an approved source or a named unresolved gap.
- Installation content is limited to the approved conceptual relationships.
- Shopify-theme information gaps are explicit.

Validation and evidence:

- Local path/link audit of references.
- Live source records with timestamps in `implementation-notes.md`.
- Asset inventory and hashes for localized files.
- Review of document consistency against PRD, DESIGN, CONTEXT, and ADR 0001.

Failure signals and stop conditions:

- Any product price cannot be verified or conflicts between reliable sources.
- Any product is unavailable or changed enough to require substitution.
- A Premium Della Services label is unsupported.
- Required hero/project imagery has no approved usable source.
- The installation diagram would need unverified technical detail.

Rollback/risk note:

This step changes documents and assets only. Remove unapproved localized assets rather than carrying placeholders into implementation.

### Step 2 — Build The Shared Visual And Interaction Foundation

Result: completed on 2026-07-14. Shared scoped CSS/JavaScript, runtime-ready flat assets, the approved two-image reuse map, responsive browser evidence, and accessibility evidence are recorded in `docs/PROGRESS.md` and `implementation-notes.md`.

Goal:

Create one namespaced CSS/JavaScript foundation shared by preview and Shopify.

Spec:

- Implement approved tokens, typography, container, spacing, buttons, cards, tables, tabs, focus states, reduced-motion behavior, and breakpoint rules.
- Define the exact responsive matrix for 1440, 1280, 768, 430, 390, and below 360 pixels.
- Prepare progressive product-tab behavior and native FAQ styling.
- Keep selectors scoped to the Landing Page Body.

Likely files:

- `assets/della-hidden-mini-split-comparison.css`
- `assets/della-hidden-mini-split-comparison.js`
- `docs/ARCHITECTURE.md`
- `docs/PROGRESS.md`

Acceptance criteria:

- No global element selector can unintentionally restyle the theme outside the section.
- Buttons and tabs meet the 44px minimum target.
- Focus states are visible and WCAG AA color targets are documented.
- No animation is required to understand or use the page.
- CSS covers all approved breakpoints without creating a mobile horizontal scroller.

Validation and evidence:

- Static selector review.
- CSS syntax check where tooling is available.
- Minimal local fixture proving tab keyboard behavior and focus treatment.
- Diff review confirming no promotional or generic AI visual patterns.

Failure signals and stop conditions:

- Styles require global theme overrides.
- Two-column product cards cannot remain legible at 390px.
- The tab control requires horizontal scrolling.

### Step 3 — Implement Preview Decision Sections

Result: completed on 2026-07-14. The original decision-section build, responsive behavior, semantic comparison content, conceptual planning diagrams, and browser/static QA are recorded in `docs/PROGRESS.md` and `design-qa.md`. The top Benefit Strip was subsequently removed by user request on 2026-07-15. Final visual acceptance remains blocked by the two approved temporary project-scene placeholders.

Goal:

Build the decision-support half of the static preview before merchandising.

Spec:

- Implement Hero, Quick Answer, Project Fit, Key Differences, and Installation Requirements in the frozen order.
- Use exactly one H1 with the approved phrase.
- Use exactly four project scenarios and `Multi-Room Renovation`.
- Build conceptual planning diagrams with the exact `not to scale` label and shared professional-confirmation note.
- Keep Quick Answer visibly more compact than the mockup and preserve Project Fit as the primary decision module.

Likely files:

- `ceiling-cassette-vs-concealed-ducted-mini-split.html`
- Shared CSS/JS and approved assets
- `docs/PROGRESS.md`
- `HANDOFF.md`

Acceptance criteria:

- Decision sections are in the approved order with no extra module or visible internal numbering.
- Hero labels identify both System Types in HTML.
- The six comparison rows remain semantic and complete.
- Installation diagrams contain no prohibited technical detail.
- Preview contains no Header or Footer.

Validation and evidence:

- HTML structure audit for heading count, section order, links, and forbidden terms.
- Browser screenshots at 1440, 768, and 390 pixels for the decision sections.
- Keyboard and screen-reader-oriented semantics inspection.
- Overflow and text-overlap check.

Failure signals and stop conditions:

- `Whole-Home Renovation`, task numbers, mockup copy, or technical cutaway details remain.
- Hero/project assets do not meet the approved visual direction.
- Comparison information becomes inaccessible on mobile.

### Step 4 — Implement Preview Sections 7 Through 10

Goal:

Complete the static preview with curated products, trust, FAQ, and two-path conversion close.

Spec:

- Build the two accessible System Type tabs and show four approved products in the active panel only.
- Use the recorded static Preview Prices and the approved Starting Point badges.
- Directly reproduce the approved Della reference grammar for Premium Della Services, the single-column FAQ, and the two-path Bottom CTA.
- Keep all FAQ items collapsed by default.
- Add stable CTA location/path attributes without custom event names.

Likely files:

- Preview HTML
- Shared CSS/JS and trust assets
- `implementation-notes.md`
- `docs/PROGRESS.md`
- `HANDOFF.md`

Acceptance criteria:

- Each tab has four equal-size product cards, full titles, 2-3 verified chips, price, and `View Product` CTA.
- Only the 18K cassette and 22K ducted cards have the Starting Point badge.
- Only one tab panel is exposed as active.
- Services contains exactly four verified labels and matching approved icons.
- FAQ has six approved questions, one column, and no FAQ schema until answers are approved.
- Bottom CTA has exactly two Collection Paths.

Validation and evidence:

- Click and keyboard checks for tablist, Arrow keys, Home, End, Enter, and Space.
- Link audit for all visible product and collection CTAs in both tab states.
- Price/title/image comparison against `implementation-notes.md` and PRD.
- Browser screenshots for both product tab states at 1440, 430, 390, and 350 pixels.

Failure signals and stop conditions:

- Eight products are stacked at once.
- Cards clip titles or hide prices/CTAs.
- Static prices lack capture evidence.
- Unverified service or FAQ claims appear.

Result: completed on 2026-07-14. The preview now contains the original ten-section version, two accessible four-product tabs, dated static prices, the approved Premium Della Services treatment, three non-repetitive collapsed native FAQ disclosures, and two final Collection Paths. The top Benefit Strip was removed by user request on 2026-07-15, leaving the current approved nine-section version. Focused structure, interaction, responsive, link, image, overflow, and console checks are recorded in `docs/PROGRESS.md` and `design-qa.md`. Overall visual acceptance remains blocked by the two known project-scene placeholders and the required named HVAC/product review.

### Step 5 — Accept The Complete Static Preview

Goal:

Establish a browser-verified visual and behavioral baseline before Shopify conversion.

Spec:

- Review the full page at all approved viewports.
- Compare page rhythm to the three mockups and direct component references while enforcing all DESIGN overrides.
- Test every path, both product tab states, FAQ controls, keyboard flow, focus, reduced motion, and no-JavaScript fallback.
- Check console, layout shift risks, broken assets, and horizontal overflow.

Likely files:

- Preview HTML and shared assets
- `docs/PROGRESS.md`
- `HANDOFF.md`
- Optional QA screenshots under a clearly named review directory

Acceptance criteria:

- Exact nine-section order and exactly one H1.
- Two product columns at both 390px and 430px; one column below 360px.
- No clipping, overlap, unexpected scroll, broken image, or console error.
- Links, tabs, FAQ, and focus behavior pass.
- Visual direction reads as a mature Della ecommerce page, not a poster, article, or SaaS template.

Validation and evidence:

- Screenshots at 1440, 1280, 768, 430, 390, and 350 pixels.
- Browser interaction log for all CTAs, both tabs, and all FAQs.
- Automated HTML/link checks where available plus manual visual comparison.
- Source scan for prohibited phrases, task numbers, Header/Footer, fake prices, promos, and `Add to Cart`.

Failure signals and stop conditions:

- Any acceptance criterion in PRD or DESIGN fails.
- Preview needs a structural change rather than a scoped visual fix; update the plan before proceeding.

Result: acceptance run completed on 2026-07-14 with a `blocked` result. Structure, responsive behavior, product tabs, the current three FAQ controls, link mapping, image loading, focus visibility, reduced-motion/no-JavaScript source behavior, console state, and current product price/availability parity passed. Final acceptance failed because the New Construction and Multi-Room Renovation cards still contain explicit pending-approval placeholders. Publication also remains blocked until a named Della product/HVAC reviewer approves both conceptual planning diagrams. Evidence is recorded under `qa-evidence/step5/`, `design-qa.md`, and `docs/PROGRESS.md`.

### Step 6 — Build The Shopify OS 2.0 Section

Goal:

Translate the accepted Landing Page Body into a dedicated Liquid section with dynamic Production Prices.

Spec:

- Reproduce the accepted preview markup, copy, interactions, and asset usage inside one dedicated section.
- Resolve the eight exact product handles through Shopify product objects and render current price with Shopify money formatting.
- Prefix variable prices with `From` only when Shopify reports a price range.
- Preserve exact tab grouping, badges, CTA labels, and approved image behavior.
- Load shared section assets without duplicating them or affecting global theme CSS.
- Provide a safe editor-visible failure state for missing product objects, while treating any missing product as a publication blocker.

Likely files:

- `sections/ceiling-cassette-vs-concealed-ducted-mini-split.liquid`
- Shared assets
- `docs/ARCHITECTURE.md`
- `docs/PROGRESS.md`
- `HANDOFF.md`

Acceptance criteria:

- All eight prices come from Shopify product data; no hard-coded production price exists.
- Preview and production product/card behavior is visually equivalent.
- Liquid does not add Header, navigation, or Footer markup.
- Product objects remain the exact approved handles.
- Section assets and scripts initialize once even when the theme editor reloads the section.

Validation and evidence:

- Liquid/theme syntax check using the available Shopify theme tooling or a target-theme preview.
- Source scan proving no production price literals.
- Product-handle and money-filter audit.
- Theme-editor reload and tab/FAQ smoke test when an environment is available.

Failure signals and stop conditions:

- Shopify cannot resolve one of the approved products.
- Price output differs from the live PDP at the same QA time.
- The section depends on PageFly or duplicates Storefront Chrome.
- Target-theme compatibility cannot be tested; implementation may continue as a draft, but production acceptance stops.

### Step 7 — Build And Validate The Dedicated JSON Page Template

Goal:

Mount the section once inside the active Shopify theme page shell.

Spec:

- Create the dedicated page JSON template containing the comparison section exactly once.
- Keep the template free of custom Header/Footer sections.
- Confirm the active theme provides normal Header and Footer around the page.
- Confirm no PageFly section or legacy page body duplicates the Landing Page Body.

Likely files:

- `templates/page.ceiling-cassette-vs-concealed-ducted.json`
- `docs/ARCHITECTURE.md`
- `docs/PROGRESS.md`
- `HANDOFF.md`

Acceptance criteria:

- JSON is valid and references the correct section type once.
- Shopify page renders one Landing Page Body and one normal theme Header/Footer pair.
- No duplicate whitespace, nested page shell, or PageFly content appears.

Validation and evidence:

- JSON parse check.
- Theme preview screenshot of top, middle, and bottom page boundaries.
- DOM/source inspection for one H1, one section instance, one Header, and one Footer.

Failure signals and stop conditions:

- Active theme structure is unavailable for validation.
- Header/Footer is missing, duplicated, or implemented inside the custom section.

### Step 8 — Finalize SEO, FAQ Schema, And Measurement Hooks

Goal:

Finalize search and measurement details only after content and Shopify routing are stable.

Spec:

- Confirm SEO title and meta description in the Shopify page/admin workflow.
- Let the active theme own canonical output; confirm the final URL before asserting canonical behavior.
- Add FAQPage JSON-LD only after visible FAQ answers receive approval, and keep it byte-for-content equivalent in meaning.
- Retain stable CTA location/path attributes.
- Inspect the existing Della analytics convention before adding any event integration. If no convention is available, stop at data attributes.
- Do not add BreadcrumbList or Product schema.

Likely files:

- Liquid section if FAQ schema is approved
- `implementation-notes.md`
- `docs/PROGRESS.md`
- `HANDOFF.md`

Acceptance criteria:

- Exactly one H1 and approved metadata.
- Canonical behavior matches the confirmed Shopify URL and active theme.
- FAQ schema is absent when FAQ answers are not approved, or exactly matches all visible approved FAQ content.
- No invented event names, URL-parameter rewriting, Product schema, or BreadcrumbList appears.

Validation and evidence:

- Rendered source and structured-data validation.
- Metadata/canonical inspection on the Shopify preview or production-candidate URL.
- CTA attribute inventory and analytics-convention reference.

Failure signals and stop conditions:

- Final URL or theme canonical ownership is unknown.
- FAQ copy is still provisional.
- Measurement requirements would require speculative custom JavaScript.

### Step 9 — Run Final Preview And Shopify Acceptance QA

Goal:

Prove that both delivery forms meet the same approved behavior and that production data is current.

Spec:

- Repeat responsive, interaction, accessibility, link, claim, schema, and visual checks in both environments.
- Compare all eight Preview Prices, Liquid Production Prices, and live PDP prices at the same QA time.
- Reverify product availability, trust labels, installer route, and the installation-diagram review record.
- Confirm the Shopify Header/Footer appears exactly once and the preview has neither.
- Inspect changed files and remove temporary, debug, placeholder, or unused artifacts.

Likely files:

- All implementation artifacts
- `implementation-notes.md`
- `docs/ARCHITECTURE.md`
- `docs/MODULARITY.md`
- `docs/PROGRESS.md`
- `HANDOFF.md`

Acceptance criteria:

- Every PRD, DESIGN, and plan criterion passes or is explicitly blocked.
- Price parity passes for all eight products.
- All approved viewports and interactions pass in preview and Shopify.
- Claims and schema are current and supported.
- No placeholder asset, stale price, duplicated code path, dead file, or global style leak remains.

Validation and evidence:

- Browser screenshots at 1440, 1280, 768, 430, 390, and 350 pixels for both delivery forms where possible.
- Keyboard traversal and tab/FAQ interaction record.
- Link and product-data audit.
- Price parity table with timestamp.
- Structured-data, console, overflow, and source scans.
- Diff necessity and repository hygiene review.

Failure signals and stop conditions:

- Any price mismatch, unsupported claim, broken route, missing asset, accessibility failure, or unresolved technical-diagram review.
- Shopify environment is unavailable; local acceptance can pass, but production acceptance cannot.

### Step 10 — Handoff And Optional Git Checkpoint

Goal:

Produce a resumable, reviewable handoff and stop before external state changes.

Spec:

- Update all project memory with completed steps, commands/checks, evidence, known risks, and exact next action.
- Provide deployment instructions for copying theme assets, section, and template into the target theme and assigning the page template.
- Check git status and diff without modifying unrelated user work.
- Commit or push only after separate explicit user approval, target repository/branch confirmation, and current QA evidence.

Likely files:

- `HANDOFF.md`
- `docs/PROGRESS.md`
- `docs/ARCHITECTURE.md`
- `docs/MODULARITY.md`
- `implementation-notes.md`

Acceptance criteria:

- Handoff lists current files, approved decisions, QA status, unresolved blockers, deployment steps, and commit/push authorization state.
- No unrelated file is staged or changed.
- No commit, push, theme upload, or publication occurs without explicit approval.

Validation and evidence:

- Final path inventory, git status, and diff review.
- Cross-check of HANDOFF against actual file and QA state.

Failure signals and stop conditions:

- QA evidence is stale or incomplete.
- Target repository, branch, or theme is uncertain.

## Verification Matrix

| Invariant | Preview evidence | Shopify evidence |
| --- | --- | --- |
| Exact nine-section order | HTML/source audit | Rendered DOM/source audit |
| Exactly one H1 | HTML parser/manual source check | Theme-rendered DOM check |
| No preview Header/Footer | Top/bottom screenshot and DOM | Not applicable |
| Theme Header/Footer once | Not applicable | DOM and boundary screenshots |
| Four products per active tab | Both tab screenshots and DOM state | Both tab screenshots and DOM state |
| Static vs dynamic price contract | Dated snapshot table | Liquid/PDP parity table |
| Product grid responsive rules | 430, 390, and 350 screenshots | Same widths in theme preview |
| Keyboard tabs and FAQ | Interaction log | Theme-preview interaction log |
| No prohibited technical claims | Source/content scan | Rendered source/content scan |
| FAQ schema rule | Absent or exact visible match | Structured-data validation |
| Stable CTA routing | Link audit | Link audit in rendered theme |
| No global style leakage | Isolated preview review | Theme page comparison and selector review |

## Known Preconditions And Residual Risks

The plan is implementable, but these inputs can block later acceptance:

- Approved reusable Hero and project-scene source assets are not yet mapped.
- Two multi-zone concealed-ducted manual sources remain unverified.
- A named Della product or HVAC reviewer is required before the conceptual diagrams are publishable.
- The four Premium Della Services labels require launch-time revalidation.
- FAQ answers require approval before FAQPage schema is enabled.
- An active Della theme source or preview environment is required for final section/template integration, price rendering, and Header/Footer validation.
- Existing Della analytics event conventions and final Shopify URL remain unconfirmed.

These risks do not block approval of this plan. They are explicit Step 1 or later stop conditions and must not be hidden with placeholders or assumptions.

## Commit, Push, And Publication Conditions

Do not commit, push, upload to a live theme, assign the production page template, or publish until all of the following are true:

- Steps 1-9 are complete or every remaining blocker is explicitly accepted by the user.
- Browser QA evidence is current.
- All eight products pass price and availability checks.
- Claim and technical-diagram reviews are recorded.
- Git status and diff are reviewed for unrelated changes.
- Target repository, branch, and Shopify theme are confirmed.
- The user explicitly approves the requested external action.

## Next Gate

Step 5 has been executed but the static preview is not accepted. The remaining acceptance blockers are the two explicit project-scene placeholders and named Della product/HVAC approval for the conceptual diagrams.

Replace or approve those assets/reviews, then rerun Step 5. Do not begin Step 6, Liquid, or JSON while Step 5 remains blocked.
