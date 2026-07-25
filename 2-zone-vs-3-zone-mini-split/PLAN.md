# PLAN: 2-Zone vs 3-Zone Mini Split

## Goal

Build a standalone Della landing-page HTML demo for the `2-Zone vs 3-Zone Mini Split` page after PRD and design alignment.

The implementation must preserve the approved design draft's ecommerce rhythm while following PRD overrides for content, products, prices, removed sections, and FAQ count.

## File Structure

Project folder:

`C:\Users\18041\Desktop\della-pages\2-zone-vs-3-zone-mini-split`

Planned files:

- `PRD.md` - source of truth for scope, content, products, and rules.
- `DESIGN.md` - visual handoff and mockup overrides.
- `PLAN.md` - implementation and QA plan.
- `2-zone-vs-3-zone-mini-split.html` - final standalone HTML demo.
- `assets/` - local fonts and stable generated/composited hero or scenario assets, if used.
- `HANDOFF.md` - create when implementation starts or before commit/push review.

Do not create duplicate `index.html` unless explicitly requested.

## Step 1: Product Price And Availability Verification

Goal:

Verify the eight PRD-approved products before implementation.

Inputs:

- Product URLs and image URLs in `PRD.md`.

Outputs:

- Current live price for each product.
- Availability signal for each product where visible.
- Rating only if reliably visible and easy to capture.

Boundaries:

- Do not substitute products without user approval.
- Do not invent prices, compare-at prices, sale badges, coupon labels, or ratings.

Validation command or manual check:

- Open/read each product page or Shopify JSON if available.
- Record current visible price and any rating evidence used.

Expected verification evidence:

- A concise implementation note or final QA summary listing each product and captured price.

Rollback or risk note:

- If any product page cannot be verified or is unavailable, stop and ask before proceeding.

## Step 2: Asset Preparation

Goal:

Prepare reliable review assets without copying unnecessary clutter.

Inputs:

- Design draft image.
- Existing Della PageFly font assets where available.
- Product image URLs from PRD.
- Optional generated/composited hero and scenario images.

Outputs:

- Local fonts in `assets/` if needed.
- Final hero/scenario assets in `assets/` if generated or copied for stable review.

Boundaries:

- Do not use the design draft as final sliced image.
- Do not keep temporary screenshots or unused draft images.

Validation command or manual check:

- Browser render confirms assets load.
- File listing confirms no temporary clutter.

Expected verification evidence:

- Asset list in final summary or `HANDOFF.md`.

Rollback or risk note:

- If hero/scenario assets are not ready, use product-led placeholders only if clearly marked in notes and visually acceptable for review.

## Step 3: HTML/CSS Implementation

Goal:

Create `2-zone-vs-3-zone-mini-split.html` as a standalone landing-page demo.

Inputs:

- `PRD.md`
- `DESIGN.md`
- Live product price capture
- Approved assets

Outputs:

- Complete static HTML with inline CSS/JS unless a later decision changes implementation mode.

Boundaries:

- Do not include top benefit strip.
- Do not include standalone install planning band.
- Do not include `Find Partner HVAC Installer` in services.
- Do not include custom newsletter or footer.
- Do not use `Add to Cart`.
- Do not include fake promo or financing claims.

Acceptance criteria:

- Section order matches PRD.
- Visual rhythm follows design draft where allowed.
- Product tabs contain exactly four approved products per tab.
- Product prices are present and live-verified.
- FAQ contains exactly five questions.

Validation command or manual check:

- Open local HTML in browser or via local server if needed.
- Inspect DOM/source for forbidden sections and product URLs.

Expected verification evidence:

- Browser screenshots and link/tabs/FAQ test summary.

Rollback or risk note:

- If price capture becomes stale before launch, refresh prices before final handoff.

## Step 4: Interactions And Accessibility

Goal:

Make page controls usable and keyboard accessible.

Inputs:

- Product tabs
- FAQ accordion
- CTA links

Outputs:

- Accessible tab behavior or robust button-based tab toggle.
- FAQ with semantic `details/summary` or equivalent accessible markup.
- Visible focus states.

Acceptance criteria:

- Tabs can be operated by keyboard.
- FAQ can be opened and closed by keyboard.
- CTAs have clear labels.
- No text-only icon buttons without accessible names.

Validation command or manual check:

- Keyboard tab through page.
- Browser click tests for hero CTAs, room-count strip, product tabs, product cards, FAQ, bottom CTA.

Expected verification evidence:

- QA summary naming checked interactions.

Rollback or risk note:

- If full ARIA tabs add complexity, use simpler button toggles with clear `aria-pressed`/hidden panel states.

## Step 5: SEO And Schema

Goal:

Add stable SEO metadata and FAQ schema.

Inputs:

- SEO title/meta/H1 from PRD.
- Final visible FAQ text.

Outputs:

- Title and meta description.
- FAQPage JSON-LD matching visible FAQ.

Boundaries:

- Omit canonical until final Shopify URL is confirmed.
- Do not add Product/Offer schema unless dynamic price/inventory data can remain accurate.

Acceptance criteria:

- H1 appears once.
- FAQ schema has exactly the five visible FAQ questions and answers.
- No noindex/nofollow.

Validation command or manual check:

- Inspect source for title, meta, H1, FAQ JSON-LD.

Expected verification evidence:

- QA summary confirming schema count and canonical status.

Rollback or risk note:

- If FAQ copy changes, regenerate JSON-LD at the same time.

## Step 6: Responsive QA

Goal:

Verify desktop and mobile usability.

Inputs:

- Implemented HTML.

Outputs:

- QA results and screenshots.

Acceptance criteria:

- No horizontal overflow or overlapping text at 390px, 430px, and 1280px.
- Hero, product cards, table, service cards, FAQ, and bottom CTA are readable.
- Product prices fit inside cards.

Validation command or manual check:

- Browser screenshots at 1280px, 430px, and 390px.
- Canvas/visual check for blank assets if generated imagery is used.

Expected verification evidence:

- Final report listing checked viewports and any residual risks.

Rollback or risk note:

- If product cards are cramped at mobile widths, switch to single-column cards under the affected breakpoint.

## Step 7: Repository Hygiene And Handoff

Goal:

Keep the project folder clean and ready for review.

Inputs:

- Final files and assets.

Outputs:

- No temporary files.
- `HANDOFF.md` if implementation has started.
- Concise final QA report.

Acceptance criteria:

- No duplicate HTML outputs unless approved.
- No temporary screenshot directories.
- No unused generated images.
- No debug-only logging.

Validation command or manual check:

- File listing and targeted inspection.

Expected verification evidence:

- Final response names kept files and why they are kept.

Rollback or risk note:

- Do not commit or push without explicit user approval.

## Current Stop Conditions

Stop and ask the user if:

- A PRD-approved product is unavailable or price cannot be verified.
- The user wants PageFly/custom liquid instead of standalone HTML before demo implementation.
- A design change would reintroduce the removed benefit strip or install planning band.
- Product substitutions are needed.

## Next Action

If approved, begin implementation by verifying live prices for the eight products, then create the standalone HTML demo.
## Latest Implementation Addendum

Before coding, apply latest user corrections:

- Update product tabs so each active panel contains only matching zone-count products.
- Verify live prices for all eight PRD products and show prices in cards.
- Use real Della product imagery for hero/product cards; do not use distorted AI equipment.
- Implement four Home Situation cards, not six.
- Implement five FAQ items.
- Do not include the Della comfort updates newsletter strip.
- Do not build a custom full Shopify footer in the standalone demo.
- Keep global styles aligned to Della/PageFly tokens and compact ecommerce layout.

## Latest Room-Count Strip Removal

The early room-count path strip has been removed after user review. QA should confirm `.path-strip` is absent while the bottom collection CTA remains present.
