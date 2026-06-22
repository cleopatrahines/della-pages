# PLAN.md - 12000 BTU vs 18000 BTU Mini Split

Status: implementation plan, awaiting approval before HTML build
Source of truth: `PRD.md`
Visual constraints: `DESIGN.md` and the approved design draft image

## Implementation Gate

Do not start HTML implementation until the user approves this plan.

Before implementation, verify live product data. If any locked PDP cannot be accessed, any live selling price cannot be parsed, or any required image URL is unavailable, stop and report the missing-items list instead of generating final HTML.

## Step 1 - Verify Product Data Manifest

Goal:

Confirm the eight locked PDPs, live selling prices, product titles, image availability, and spec chips.

Spec summary:

- Inputs: eight PDP URLs and eight CDN image URLs from `PRD.md`.
- Outputs: verified product manifest for implementation.
- Outputs also include a `verified_at` timestamp for each live price capture.
- Boundaries: do not add, remove, reorder, or replace products.

Files or modules likely involved:

- Future local implementation file in this project folder.
- `PRD.md` product manifest.

Acceptance criteria:

- All eight PDPs are reachable.
- All eight live selling prices are parsed.
- Price evidence includes `verified_at` timestamp for each product because standalone HTML prices are static snapshots.
- All eight image URLs resolve.
- Spec chips are based only on verified PDP/title data.
- Sold-out products are kept with `View Product` and no sold-out badge.

Validation command or manual check:

- Use a live browser or approved network fetch to inspect each PDP and image URL.
- Check the visible price or Shopify product JSON when available.

Expected verification evidence:

- A short table listing product, final title, price, `verified_at`, image status, and chip set.

Rollback or risk note:

- If any required item fails, stop implementation and report the missing-items list. Do not substitute collection products.

## Step 2 - Extract Local Reference Patterns And Assets

Goal:

Reuse Della visual patterns and exact Premium Della Services section from the local reference page.

Spec summary:

- Inputs: single-zone reference HTML, design draft image, Della design system references.
- Outputs: asset/style map for hero, product cards, services, and scenarios.
- Outputs also include a four-item scenario image map for approval before final HTML build.
- Boundaries: do not copy full nav/header/footer. Copy Premium Della Services exactly.

Files or modules likely involved:

- `C:\Users\18041\Desktop\della-pages\single-zone-vs-multi-zone-mini-split\single-zone-vs-multi-zone-mini-split.html`
- `C:\Users\18041\Desktop\della-pages\12000 BTU vs 18000 BTU Mini Split\12k vs. 18k Design Drafts.png`
- Future HTML/CSS output file.

Acceptance criteria:

- Product card visual approach matches the single-zone page.
- Premium Della Services section content, icons, and layout are copied from single-zone.
- Scenario images are selected from Della-owned/local page assets when possible.
- Scenario image map is approved before final HTML build.

Validation command or manual check:

- Inspect local reference HTML around product-card and services sections.
- Confirm selected image URLs render.

Expected verification evidence:

- Services section source line/location noted.
- Scenario image map listed before final HTML handoff.

Rollback or risk note:

- If scenario images are weak but available, report the chosen closest-fit image rather than using AI-generated scenes.
- If required local absolute paths are unavailable, stop and ask the user to provide the reference HTML or assets. Do not rebuild from memory.

## Step 3 - Build Standalone Page Skeleton

Goal:

Create the standalone landing page structure without Shopify header/footer.

Spec summary:

- Inputs: `PRD.md` section order and `DESIGN.md` visual constraints.
- Outputs: initial HTML/CSS skeleton with correct page order.
- Boundaries: no calculator, no canonical, no schema, no OG/social metadata.

Files or modules likely involved:

- Future HTML file in `C:\Users\18041\Desktop\della-pages\12000 BTU vs 18000 BTU Mini Split`.

Acceptance criteria:

- Section order exactly follows PRD.
- H1, SEO title, and meta description match PRD.
- Page uses Della typography/color tokens and clean responsive wrappers.

Validation command or manual check:

- Open the local HTML page in a browser and inspect top-to-bottom section order.
- Inspect `<title>` and `<meta name="description">`.

Expected verification evidence:

- Browser screenshot or short section-order checklist.

Rollback or risk note:

- If skeleton drifts into blog/article layout, adjust back to ecommerce decision-page structure before product work.

## Step 4 - Implement Decision And Education Modules

Goal:

Build hero, choose cards, sizing note, sizing factors, comparison table, and Bigger Is Not Always Better.

Spec summary:

- Inputs: PRD-approved copy and design constraints.
- Outputs: decision modules with collection CTAs and conservative sizing language.
- Boundaries: no calculator, no unverified performance claims, no extra modules.

Files or modules likely involved:

- Future HTML/CSS output file.

Acceptance criteria:

- Hero has exactly two collection CTAs.
- Choose cards have exactly five bullets each.
- Sizing factors have exactly six cards with approved copy.
- Comparison table has exactly six rows and no SKU/price data.
- On mobile, the comparison table becomes stacked comparison cards, not a horizontally scrolling table.
- Bigger Is Not Always Better uses `Right-sized comfort` vs `Oversized system risk` framing.

Validation command or manual check:

- Manual copy review against `PRD.md`.
- Browser check at desktop and mobile widths.

Expected verification evidence:

- Copy checklist with pass/fail for each required module.

Rollback or risk note:

- If copy starts to imply guaranteed coverage or that 18K is inherently better, revise before continuing.

## Step 5 - Implement Product Sections

Goal:

Add two visible product groups using the fixed eight products and verified live prices.

Spec summary:

- Inputs: verified product manifest from Step 1.
- Outputs: two product sections, each with four product cards and one collection CTA.
- Boundaries: no tabs, no dynamic collection auto-fill, no product replacement, no sale badges.

Files or modules likely involved:

- Future HTML/CSS output file.

Acceptance criteria:

- Product group 1 shows exactly four 12K products.
- Product group 2 shows exactly four 18K products.
- Each card shows image, title, verified chips, live selling price, and `View Product` CTA.
- Product chip labels use consistent front-end formatting such as `Up to 550 sq. ft.` and `Up to 1,000 sq. ft.`.
- Each group includes its `Shop All` collection CTA.
- Della links open in same tab.

Validation command or manual check:

- Browser click test for each product and collection link.
- Visual check for product-card alignment and no overflow.

Expected verification evidence:

- Product/link checklist with 10 same-tab links: 8 PDP links + 2 collection CTAs.

Rollback or risk note:

- If live price data changes after initial capture, update the hardcoded price before handoff or report that live pricing needs Shopify-side dynamic rendering.

## Step 6 - Implement Scenarios, Services, FAQ, Bottom CTA, Mobile Sticky CTA

Goal:

Complete the trust, FAQ, and closing conversion sections.

Spec summary:

- Inputs: four approved scenarios, exact Premium Della Services reference section, five FAQs, bottom CTA copy.
- Outputs: final lower-page modules and mobile sticky CTA.
- Boundaries: no extra scenarios, no rewritten Services copy, no FAQ schema, no extra bottom note.

Files or modules likely involved:

- Future HTML/CSS output file.

Acceptance criteria:

- Four scenario cards only, each with real lifestyle image.
- Premium Della Services is copied from the single-zone page.
- Five FAQs appear in approved order.
- FAQ #4 starts with `Not necessarily in the way that matters.`
- Bottom CTA has two collection cards and short positioning lines only.
- Mobile sticky CTA appears only on mobile, 56 to 64 px tall, with `Shop 12K` and `Shop 18K`.

Validation command or manual check:

- Browser check on desktop and mobile.
- Mobile scroll to footer to confirm sticky CTA does not cover content.

Expected verification evidence:

- Screenshots of lower page desktop and mobile.
- Sticky CTA pass/fail note.

Rollback or risk note:

- If Services copied styles conflict with this page, adjust surrounding spacing only. Do not rewrite service-card content unless the user approves.

## Step 7 - SEO, Accessibility, And Data Integrity Pass

Goal:

Make the page launch-safe for SEO and ads without adding unsupported metadata.

Spec summary:

- Inputs: final HTML draft.
- Outputs: cleaned HTML with correct metadata, alt text, links, and no placeholders.
- Boundaries: no canonical, no FAQ schema, no OG/social meta in this version.

Files or modules likely involved:

- Future HTML output file.

Acceptance criteria:

- Title and meta description match PRD.
- One H1 only.
- H2/H3 hierarchy is logical.
- All images have meaningful alt text.
- No placeholder copy or placeholder images remain.
- No fake prices, fake claims, sale badges, or unverified discounts remain.

Validation command or manual check:

- Inspect HTML metadata and heading order.
- Search final file for placeholder terms such as `TODO`, `placeholder`, `lorem`, `sale`, `discount`, `coupon`, `price shown`, `from $`, `review`, `stars`, `calculator`, `guaranteed`, `guarantee`, and `best for all`.

Expected verification evidence:

- Metadata/heading checklist.
- Placeholder scan result summary.

Rollback or risk note:

- If any required price or image cannot be verified, revert product section to blocked status and report missing data rather than shipping incomplete HTML.

## Step 8 - Browser QA Across Viewports

Goal:

Verify the final page visually and behaviorally before handoff.

Spec summary:

- Inputs: final HTML page.
- Outputs: QA evidence across desktop, tablet, and mobile.
- Boundaries: do not run broad unrelated tests.

Files or modules likely involved:

- Future HTML output file.

Acceptance criteria:

- Desktop layout has no obvious overlap or horizontal scroll.
- Tablet layout remains readable.
- Mobile layout stacks cleanly.
- Sticky CTA appears only on mobile.
- Hero product visual is not blank and uses real product images.
- Product cards, Services section, FAQ, and bottom CTA render correctly.
- Same-site links open in the same tab.

Validation command or manual check:

- Browser screenshots at approximately 1440 px desktop, 768 px tablet, and 390 to 430 px mobile.
- Link click checks for representative collection and PDP links.

Expected verification evidence:

- Screenshot list and a short pass/fail QA summary.

Rollback or risk note:

- If mobile sticky CTA covers content, adjust padding and sticky height before handoff.

## Step 9 - Final Review And Handoff

Goal:

Deliver a clean, explainable page artifact without unrelated clutter.

Spec summary:

- Inputs: final HTML/CSS and QA evidence.
- Outputs: final handoff summary.
- Boundaries: do not commit, branch, or push unless the user explicitly asks.

Files or modules likely involved:

- Final HTML file.
- Optional screenshot artifacts only if the user requests keeping them.

Acceptance criteria:

- Only intended deliverables are left in the project folder.
- Temporary scripts, scratch files, and test exports are removed unless explicitly needed.
- Final report explains what changed, what was verified, and what remains unverified.

Validation command or manual check:

- Check folder contents.
- Review final page manually once after QA fixes.

Expected verification evidence:

- Concise final summary with validation results.

Rollback or risk note:

- Keep documentation and implementation separate. If the user rejects implementation direction, update PRD/DESIGN/PLAN before further coding.

## Implementation Stop Conditions

Stop and report before generating final HTML if any of these happen:

- Any locked PDP URL is inaccessible.
- Any live selling price cannot be parsed.
- Any required product image URL is unavailable.
- Product data conflicts with the manifest in a way that could mislead shoppers.
- The Services section cannot be copied from the single-zone reference page.
- Any required local reference path is unavailable and the user has not provided replacement reference files or assets.
- The final page would require adding a claim that has not been approved.

## Final Verification Evidence To Report

When implementation is complete, report only high-signal evidence:

- Product price verification: pass/fail, `verified_at`, and any changed prices.
- Product image verification: pass/fail.
- Link verification: pass/fail for collection and PDP links.
- Responsive QA: pass/fail for desktop, tablet, mobile.
- Sticky CTA: pass/fail on mobile and hidden on desktop.
- Content guardrails: pass/fail for no fake prices, no sale badges, no unapproved schema/canonical.

