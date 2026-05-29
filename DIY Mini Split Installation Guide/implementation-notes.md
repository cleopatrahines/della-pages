# Implementation Notes: Della DIY Mini Split Installation Guide

Last updated: 2026-05-29  
Project folder: `C:\Users\18041\Desktop\della-pages\DIY Mini Split Installation Guide`

## Final Grill-Me Decisions

- Final Shopify URL handle: `/pages/diy-mini-split-installation-guide`.
- Add canonical only if the final Shopify URL is implemented/known in the HTML plan.
- V1 displays no prices anywhere.
- Do not include 0% APR Financing, Lifetime Coverage, money-back, return-policy, rebate, warranty, tax-credit, or other unverified policy claims.
- Approved service/support cues only: Free Shipping Sitewide, Find Partner HVAC Installer, Installation Videos, Manuals & Troubleshooting, Contact or Live Chat Support.
- External Della/support links in local static demo use `target="_blank" rel="noopener"` unless later changed for Shopify.
- FAQPage JSON-LD is allowed only after final visible FAQ copy is stable and matches exactly.
- Do not add HowTo schema.
- Do not add Product schema in V1 unless reliable product data is available and separately approved.
- Final HTML may slightly deviate from the AI mockup if real assets require it, but must preserve the hero logic: left-side copy plus right-side Della mini split / outdoor unit / planning cue.
- After HTML completion, run responsive QA at 1440px, 768px, 430px, and 390px.
- After HTML and QA, pause for user review. Do not commit or push until user approves.
- If PRD, design image, and implementation reference conflict, PRD wins for copy, product paths, safety wording, color hierarchy, schema, service claims, and pricing.

## Product Card Scope

V1 `Shop The Installation Essentials` should only include installation essentials as product/collection cards:

- DELLA Rental Install Kit
- DELLA Mini Split Line Set
- Installation Accessories

Do not include Wall-Mounted Mini Splits or Mini Split AC as product cards inside this section.

Mini split systems may still appear as collection/path CTAs in:

- Hero
- Early path selector
- Match the system to the install complexity
- Bottom CTA

If a fourth card is needed for visual balance, use a light path/support card such as `Need the system first?`, not a product card.

## Asset Notes To Fill During Implementation

Record final image mapping here when HTML implementation starts:

| Page Area | Selected Image | Source | Confidence | Notes |
| --- | --- | --- | --- | --- |
| Hero | `Stock image/sORjR3Kw.jpeg` | User-provided local stock asset | High | Shows Della-style system, line set, accessories, and planning layout; best match for install-prep hero |
| Before checkout split panel | `Stock image/z4i-vLJQ.jpeg` | User-provided local stock asset | High | Shows outdoor unit and line-set cover route, matching checkout route planning |
| Rental Install Kit card | `Stock image/DELLA-rental_kit_step_by_step-30.webp` | User-provided local stock asset | High | Direct rental/tool kit visual; no price shown |
| Mini Split Line Set card | `Stock image/048-CW-1214_048-CW-1214-01.webp` | User-provided local stock asset | High | Direct line set/accessory visual; no price shown |
| Installation Accessories card | `Stock image/sORjR3Kw.jpeg` | User-provided local stock asset | Medium | Broad accessory/system layout used as category visual; does not imply exact SKU bundle |
| System complexity cards | `BTaM22Yw.jpeg`, `bAGi6O7g.png`, `0Pb5ub6w.png`, `048-CW-1214_048-CW-1214-01.webp` | User-provided local stock assets | Medium | Used as path/category visuals, not product proof |
| Bottom CTA | `Stock image/FaPdtcrA.png` | User-provided local stock asset | Medium | Della system visual used decoratively |

If an exact PDP image cannot be verified, use the closest Della-approved product/category visual and record the gap. Do not present uncertain visuals as verified exact PDP assets.

## Visual Optimization Notes

- Placeholder letter icons were replaced with inline SVG icons in the trust strip, decision cards, steps, path cards, support hub, and hero cue chips.
- The Rental Install Kit image remains visually louder/redder than the rest of the Della navy/light-blue palette, but it is the clearest available install-tool image in the supplied assets. Keep as direct tool visual unless a calmer Della PDP kit image is supplied later.
- The Installation Accessories card uses a broad Della install-planning flat-lay visual instead of a confirmed collection image. Treat it as a category visual, not exact SKU proof.
- The bottom CTA and system-path cards use local Della/category visuals as path guidance, not product proof.
- Final visual pass tightened mobile container width, balanced narrow-screen headings, reduced overly loose module spacing, and kept the navy-first hierarchy with #5884E7 reserved for secondary accents.

## QA Notes

- Checked static guardrails after the visual pass: one H1, no Add To Cart, no prices, no financing/warranty/policy claims, no HowTo schema, no Product schema, and no remaining letter-placeholder icons.
- FAQPage JSON-LD remains present with 6 FAQ entities and should continue to match the visible FAQ copy if FAQ text changes later.
- Responsive screenshots were generated for 1440px, 768px, 430px, and 390px. The mobile path selector intentionally remains a horizontal scroll/snap row; core content stacks below it.
- No commit or push performed. Pause for user review before any git action.

## Safety Guardrails

Final copy must not include:

- detailed refrigerant charging steps
- detailed electrical wiring steps
- warranty guarantees
- legal/code/permit guarantees
- claims that anyone can fully install without professional help

Use cautious language around licensed/certified professional support, permits, HOA, local requirements, exact model manuals, and Della support.
