# PLAN: Della Mini Split Size Guide Implementation

Last updated: 2026-05-28  
Do not implement `index.html` until the user approves this plan.

## 1. Objective

Build a static HTML demo for the Della Mini Split Size Guide after PRD and design docs are approved.

Target output:

- `C:\Users\18041\Desktop\della-pages\Mini Split Size Guide\index.html`

Supporting files:

- `PRD.md`
- `DESIGN.md`
- `PLAN.md`
- optional `assets/` only if local images/fonts become necessary
- optional `implementation-notes.md` or inline HTML comment for dated product price snapshot

## 2. Source Priority

Use sources in this order:

1. `PRD.md` for scope, content decisions, BTU ranges, product data, CTA rules, SEO, non-goals.
2. `DESIGN.md` for visual interpretation of `ui设计图.png`.
3. `ui设计图.png` for composition and visual rhythm.
4. Existing local Della pages for reusable patterns.
5. Live Della product pages or Shopify JSON only for current price capture.

Do not let the mockup override PRD content/data rules.

## 3. Implementation Steps

### Step 1: Prepare Product Data

Goal:

- Build a structured in-code product data map grouped by 9K, 12K, 18K, 24K, and 36K.

Inputs:

- PRD product table.
- Live product pages or Shopify JSON endpoints for prices.

Outputs:

- Product data in `index.html` JS object or static HTML card markup.
- Price snapshot notes with date/time and source method.

Boundaries:

- Use only PRD product URLs and image URLs.
- Use exact Della CDN image URLs for V1.
- Do not use AI mockup product names, images, or prices.
- Do not invent prices.

Acceptance criteria:

- All PRD products are mapped.
- 36K has only one product and an installer confirmation note.
- Price line is present only when reliable current price was captured.
- Compare-at price appears only if reliable.

Validation:

- Open product data map and compare each URL/image against PRD.
- Check price snapshot record.

Rollback/risk:

- If price capture fails, omit price lines and continue with image/title/spec/CTA.

### Step 2: Build HTML Structure

Goal:

- Create semantic static HTML sections in PRD order.

Section order:

1. Top benefit strip
2. Hero
3. Choose Your Starting Mini Split Size
4. Mini Split BTU Chart by Room Size
5. What Can Change Your BTU Size?
6. Choose by How the Room Is Used
7. Bigger Is Not Always Better
8. Shop Mini Splits by BTU
9. Before You Order, Confirm These With Your Installer
10. Premium Della Services
11. FAQ

Inputs:

- PRD section copy and constraints.
- DESIGN visual section guidance.

Outputs:

- `index.html` section skeleton.

Acceptance criteria:

- One H1 only.
- H2 sequence follows the PRD.
- No calculator UI.
- Multi-zone appears only as one small cross-link note.
- Top strip uses final PRD copy.

Validation:

- Inspect rendered headings and section order.
- Search HTML for forbidden placeholder copy.

Rollback/risk:

- If section count becomes too long visually, do not remove PRD-required sections without user approval; tighten copy first.

### Step 3: Style With Della Tokens

Goal:

- Match Della coupon/Memorial Day design language while respecting the mockup.

Inputs:

- PRD color tokens.
- DESIGN typography and layout notes.

Outputs:

- Inline CSS in `index.html`.

Acceptance criteria:

- Spectral-style headings and Poppins-style body/buttons.
- Navy/blue/light-blue visual system.
- Buttons are 4px radius, not pill gradients.
- No heavy shadows, glassmorphism, generic icon-grid styling, or decorative orbs.

Validation:

- Browser visual review at desktop and mobile.
- CSS scan for one-note palette or disallowed effects.

Rollback/risk:

- If the page feels too close to existing scenario-page UI, prioritize coupon/Memorial Day design system over old demo styling.

### Step 4: Implement Lightweight Interactions

Goal:

- Add only approved interactions.

Allowed:

- BTU selector anchors or switches product tabs.
- Product tabs switch between 9K/12K/18K/24K/36K.
- FAQ accordion expands/collapses.

Disallowed:

- calculator
- input fields
- sliders
- form submission
- dynamic BTU formula
- result panel

Acceptance criteria:

- Product tabs are keyboard-accessible.
- FAQ is keyboard-accessible.
- Selector buttons/links have visible focus states.
- No heavy carousel JS.

Validation:

- Click and keyboard test each tab and FAQ item.
- Mobile test horizontal BTU selector with scroll-snap.

Rollback/risk:

- If tab JS creates accessibility issues, use simpler anchor-based visible sections.

### Step 5: Add SEO And Schema

Goal:

- Make the static demo ready for Shopify adaptation.

Inputs:

- PRD SEO requirements.

Outputs:

- Title tag.
- Meta description.
- Semantic table.
- FAQ JSON-LD.
- Descriptive alt text.

Acceptance criteria:

- Title: `Mini Split Size Guide: Find the Right BTU for Your Room | Della`.
- Meta description follows PRD.
- FAQ JSON-LD parses as valid JSON.
- Links use descriptive anchor text.

Validation:

- Inspect page source.
- Validate JSON manually or with a local parser.

Rollback/risk:

- If final Shopify URL is unknown, avoid hardcoding canonical unless user supplies URL.

### Step 6: Browser QA

Goal:

- Verify the page is visually stable and usable.

Viewports:

- Desktop around 1440px.
- Tablet around 768px.
- Mobile around 390px.

Acceptance criteria:

- No text overlap.
- Hero image/cue chips do not crowd H1/CTA.
- Mobile BTU selector scrolls and snaps.
- Table is readable or cleanly scrollable.
- Product cards do not overflow.
- 36K tab looks intentional with one product.
- FAQ and tabs work.
- All CTAs link to correct destinations.

Evidence to report:

- File path.
- Viewports checked.
- CTA/link QA summary.
- Price snapshot status.
- Any unverified external behavior.

## 4. Product Data Mapping

BTU collections:

- 9K: `https://dellahome.com/collections/9000-btu-mini-split`
- 12K: `https://dellahome.com/collections/12000-btu-mini-split`
- 18K: `https://dellahome.com/collections/18000-btu-mini-split`
- 24K: `https://dellahome.com/collections/24000-btu-mini-split`
- 36K: `https://dellahome.com/collections/36000-btu-mini-split`

Product source:

- Use PRD Section 12 product table.
- Product card CTA: `View Product`.
- Tab-level CTA: `View All 12K Options` or matching BTU label.

Price source:

- Live product page or Shopify JSON.
- Capture date/time.
- Omit price line if unreliable.

## 5. Responsive Rules

Desktop:

- 1200px max content width.
- 32px side padding.
- BTU selector can be 5-across.
- Product grid 4 cards when enough products exist.

Tablet:

- Product grid 2 columns.
- BTU selector can scroll or use 3+2 if clean.

Mobile:

- 16px side padding.
- BTU selector horizontal scroll with scroll-snap.
- Card width around 72-82vw or min-width 230-260px.
- Show next-card peek.
- Product grid 2 columns only if readable; otherwise 1 column.
- Touch targets minimum 44px.
- FAQ rows easy to tap.

## 6. QA Checklist

Content:

- One H1.
- Correct H2 order.
- Della BTU ranges only.
- No AI placeholder range remains.
- No AI placeholder product remains.
- No mockup product prices remain.
- No calculator language or UI.
- FAQ max 6.

Links:

- Five BTU collection links correct.
- All PDP links correct.
- Multi-zone cross-link correct.
- Installer/support links either correct or clearly marked if target unknown.
- External links include `target="_blank" rel="noopener"` where appropriate.

Visual:

- Della navy/blue design system.
- No glassmorphism.
- No gradient hero.
- No heavy shadow stack.
- Product cards distinct from scenario cards.
- Right-size module before product tabs.

Interaction:

- Product tabs work.
- BTU selector works as anchor/tab switch if implemented.
- FAQ accordion works.
- Keyboard focus visible.

Data:

- Price snapshot recorded or price omitted.
- Compare-at price only if reliable.
- 36K one-product state intentional.

## 7. Known Non-Goals

- No interactive calculator.
- No room dimension form.
- No multi-zone matrix.
- No whole-home sizing guide.
- No `Add To Cart`.
- No coupon or discount badges.
- No invented products.
- No invented prices.
- No copying AI mockup product data.

## 8. Stop Conditions

Stop and ask before implementing if:

- final design image conflicts with PRD in a way not covered by DESIGN.md
- product price capture fails broadly and the user explicitly expects visible prices
- required hero/support imagery is missing and no acceptable placeholder approach is obvious
- Shopify URL/canonical requirements are needed before HTML can be finalized

## 9. Current Status

This plan is ready for user review. Do not create `index.html` until approved.
