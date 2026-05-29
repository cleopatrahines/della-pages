# DESIGN: Della DIY Mini Split Installation Guide

Last updated: 2026-05-29  
Project folder: `C:\Users\18041\Desktop\della-pages\DIY Mini Split Installation Guide`  
Approved design mockup: `C:\Users\18041\Desktop\della-pages\DIY Mini Split Installation Guide\Design draft.png`  
Asset folder: `C:\Users\18041\Desktop\della-pages\DIY Mini Split Installation Guide\Stock image`  
Scope source of truth: `PRD.md`

## 1. Design Role

This document translates the approved design mockup into implementation guidance. The mockup controls layout rhythm, hierarchy, visual direction, and section feel. `PRD.md` controls page structure, product names, URLs, CTA labels, safety wording, SEO, schema, product-card rules, and non-goals.

The implementation should recreate the mockup structure and visual feeling, but it must not copy blurry AI-generated text, fake product data, fake support claims, fake warranty/policy language, or unsafe installation wording.

## 2. Critical Interpretation

The design draft is a strong fit for the page type: it looks like an official Della installation-prep landing page, not a pure article or a hard-sell product grid. It correctly shows:

- slim trust strip
- ecommerce banner hero
- early installation path selector
- DIY boundary module
- high-level installation steps
- tools/parts checklist
- before-checkout split panel
- install essentials cards
- system complexity cards
- support hub
- compact FAQ
- bottom CTA

The main correction required in final HTML is color hierarchy. The mockup overuses `#5884E7` as a primary blue. Final implementation must be more navy-first:

- `#0E1953` is the Della primary brand color and should lead headings, primary CTAs, important icons, section emphasis, product/card titles, bottom CTA, and authority moments.
- `#5884E7` should be secondary: hover states, small links, cue chips, subtle icon accents, and secondary borders.
- `#EDF2FF`, `#F4F7FF`, and `#DDF7FF` can be used for soft backgrounds, support panels, trust cards, and calm checklist modules.
- The page must not feel like a bright-blue SaaS template.

## 3. Implementation Reference Boundary

Use:

`C:\Users\18041\Desktop\della-pages\mini-split-size-guide\mini-split-size-guide.html`

as a code and visual implementation reference only.

Reference these implementation traits:

- local `@font-face` loading pattern
- Spectral/Poppins font hierarchy
- type scale and line-height restraint
- section spacing and compact section variants
- 1200px-ish container system
- card padding, border, radius, and light shadow treatment
- button sizing, hover, and focus treatment
- product-card grammar
- FAQ accordion behavior using `details/summary`
- mobile breakpoints and responsive card stacking
- scoped CSS style patterns

Do not copy:

- Mini Split Size Guide section order
- BTU selector logic
- sizing table content
- BTU product tabs
- product data
- FAQ questions
- old text/content
- any page-specific JS that exists only for BTU tabs

## 4. Mockup Section Notes

### Slim Benefit Strip

Follow the mockup's compact navy strip. Keep only PRD-approved support/trust language:

- Free Shipping Sitewide
- Find Partner HVAC Installer
- 24/7 Live Chat Support

Do not add global header navigation, search, cart, account, sale banners, or payment icons.

### Hero

Follow the mockup's left-copy/right-visual ecommerce banner. Preserve:

- short eyebrow
- large Spectral H1
- concise body
- two CTAs
- cue chips
- visible wall-mounted indoor unit, outdoor unit, planning tablet, and tool bag mood

Correct:

- Make the primary hero CTA navy.
- Use blue as secondary accent.
- Keep hero body to max two short desktop lines.
- Final copy comes from PRD/DESIGN, not blurry mockup text.

### Choose Your Installation Path

Follow the five-card selector from the mockup. Cards should feel like path cards, not product cards.

Final paths:

- Need a system
- Planning wall-mounted
- Need accessories
- Need install tools
- Want pro help

Mobile may use horizontal scroll/snap if needed.

### DIY Boundaries / Decision Band

Follow the three-card module, but keep copy safety-aware and concise:

- Plan yourself
- Confirm before checkout
- Use qualified help

Use this module to prevent unsafe full-DIY interpretation.

### Install Steps At A Glance

Follow the six-step visual timeline from the mockup. It should remain an overview, not a detailed HowTo tutorial.

Correct:

- No HowTo schema.
- No detailed refrigerant charging or electrical wiring instructions.
- Include exact-model manual reminder.

### Tools & Parts Checklist

Follow the three-column checklist module:

- System parts
- Mounting and routing
- Setup tools

Keep icons subtle. Use short checklist phrases. Do not create a dense blog-like paragraph block.

### Before Checkout Checklist

Follow the split image/checklist panel. This is a high-trust conversion module and should be visually calmer than a product grid.

Use PRD checklist items:

- voltage
- panel capacity
- line set
- drain route
- outdoor clearance
- wall route
- permits / HOA
- airflow
- manual compatibility

### Shop The Installation Essentials

Follow the mockup's merchandising rhythm, but correct the card scope. The design draft shows four cards including Wall-Mounted Mini Splits. Final HTML must not copy that as a product card in this section.

Cards:

- Rental Install Kit
- Mini Split Line Set
- Installation Accessories

Optional fourth card for visual balance:

- Need the system first?
  - This is a light path/support card, not a product card.
  - It may link to Mini Split Systems and/or Wall-Mounted Mini Splits.

Correct:

- No prices.
- No ratings/review counts.
- No sale badges.
- No `Add To Cart`.
- Product images must come from approved Della live/CDN images or user-provided stock assets, not AI mockup product proof.
- Wall-Mounted Mini Splits and Mini Split AC can appear in hero, path selector, system complexity, or bottom CTA, but not as installation-essential product cards.

### Match The System To The Install Complexity

Follow the mockup's four-card visual section. This section routes by install complexity, not BTU.

Cards:

- Wall-mounted
- Multi-zone
- Cassette & concealed
- Accessories

Keep copy short and pragmatic.

### Install Help Hub

Follow the four support cards:

- Installation Videos
- Manuals & Troubleshooting
- Find Partner HVAC Installer
- Contact Support

This module should feel official and support-led, not like footer links.

### FAQ

Follow the compact accordion placement. Final FAQ uses the PRD-approved 6-question plan, not the tiny text in the mockup.

### Bottom CTA

Follow the dark navy CTA band. It should be navy-first and confident, with three low-pressure CTAs:

- Shop Mini Split Systems
- Shop Installation Accessories
- Find Partner HVAC Installer

Do not include footer/newsletter/payment elements after it.

## 5. Asset Direction

Available local stock folder:

- `048-CW-1214_048-CW-1214-01.webp`
- `0Pb5ub6w.png`
- `bAGi6O7g.png`
- `BTaM22Yw.jpeg`
- `DELLA-rental_kit_step_by_step-30.webp`
- `F_GrRdSQ.jpeg`
- `FaPdtcrA.png`
- `lo864m_A.png`
- `sORjR3Kw.jpeg`
- `z4i-vLJQ.jpeg`

Implementation should map assets only after visual inspection. Use these assets if they match PRD-approved product/category roles. If an exact product image is uncertain, use the closest approved Della product/category visual and record the gap in `implementation-notes.md`.

Rules:

- Do not invent product images.
- Do not use AI mockup product images as final product data.
- Do not invent product specs.
- Use short, natural alt text.
- Product identity remains controlled by PRD-approved URLs.

## 6. Copy Direction

Use final human-readable copy from PRD/DESIGN, not blurry mockup text.

Copy rules:

- Hero body max 2 short lines.
- Section intro max 1-2 sentences.
- Cards use short heading + short cue + CTA.
- Avoid paragraphs longer than 60-70 words.
- Checklists use short action phrases.
- Keep language calm, official, and practical.
- Do not make legal, permit, warranty, or code guarantees.

## 7. Visual QA Criteria

Pass criteria:

- Looks like a mature Della Shopify topical page.
- Recreates the approved mockup structure without copying unsafe AI text.
- Navy-first hierarchy is corrected.
- `#5884E7` is secondary, not primary.
- No global Shopify header/footer/nav/cart/search/account.
- No prices, ratings, fake sale badges, coupons, countdowns, or `Add To Cart`.
- No HowTo schema implication in the design or implementation.
- Product cards appear after decision/checklist modules.
- Support paths are visible and official.
- Mobile layout has no overlap, clipped text, or horizontal page overflow.
