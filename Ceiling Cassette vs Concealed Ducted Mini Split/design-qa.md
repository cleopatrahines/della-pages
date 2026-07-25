# Design QA — Step 5 Complete Static Preview Acceptance

## Scope

- State reviewed: original ten-section static preview, with focused Step 4 review of sections 7–10. The top Benefit Strip was removed after this audit and needs a focused visual recheck.
- Source visual truth: `设计稿1.png`, `设计稿2.png`, `设计稿3.png`, `product-layout-reference.png`, `product-layout-mobile-reference.png`, and the local 2-zone reference page.
- Required overrides: `DESIGN.md`, `PRD.md`, and the approved asset decision in `implementation-notes.md`.
- Viewports checked: 1440, 1280, 768, 430, and 390 pixels.

## Evidence

- `qa-evidence/implementation-top.png`
- `qa-evidence/implementation-project.png`
- `qa-evidence/implementation-placeholders.png`
- `qa-evidence/implementation-compare.png`
- `qa-evidence/implementation-installation.png`
- `qa-evidence/della-step3-mobile-390-quick-final.png`
- `qa-evidence/della-step3-qa-board-comparison.png`
- `qa-evidence/della-step3-qa-board-placeholders.png`
- `qa-evidence/step4-desktop-products-cassette.png`
- `qa-evidence/step4-desktop-products-ducted.png`
- `qa-evidence/step4-desktop-trust-faq.png`
- `qa-evidence/step4-desktop-bottom-cta.png`
- `qa-evidence/step4-mobile-430-cassette.png`
- `qa-evidence/step4-mobile-430-card-detail.png`
- `qa-evidence/step5/01-desktop-1440-entry.png`
- `qa-evidence/step5/02-desktop-1440-project-compare.png`
- `qa-evidence/step5/03-desktop-1440-differences.png`
- `qa-evidence/step5/04-desktop-1440-installation.png`
- `qa-evidence/step5/05-desktop-1440-products-cassette.png`
- `qa-evidence/step5/06-desktop-1440-products-ducted.png`
- `qa-evidence/step5/07-mobile-430-products-cassette.png`
- `qa-evidence/step5/08-mobile-430-products-ducted.png`
- `qa-evidence/step5/09-mobile-430-trust-faq.png`
- `qa-evidence/step5/10-mobile-430-faq-open.png`
- `qa-evidence/step5/11-mobile-430-bottom-cta.png`
- `qa-evidence/step5/viewport-1280.png`
- `qa-evidence/step5/viewport-768.png`
- `qa-evidence/step5/viewport-430.png`
- `qa-evidence/step5/viewport-390.png`
- `qa-evidence/step5/viewport-350.png`

## Comparison History

1. Initial browser pass found the comparison product imagery rendering at excessive height and the desktop H1 wrapping to four lines. Product imagery was capped at 360px on desktop/240px on mobile and the H1 was adjusted to three lines.
2. The mobile Quick Answer CTA wrapped unnecessarily. Mobile button padding and type size were reduced within the approved 44px-plus target; both CTA labels now remain on one line at 390px.
3. Final browser checks found no horizontal overflow at the approved breakpoints and no console warnings or errors.
4. Step 4 side-by-side inspection confirmed the four-card product grammar and the directly reused Premium Della Services rhythm. The FAQ and Bottom CTA preserve the reference typography, dividers, spacing, and pale-blue close while using page-specific copy.
5. Responsive checks confirmed two product columns at 430/389, one below 360, and no button or tab overflow. Both product states and keyboard tab selection were verified.
6. Step 5 recaptured the complete decision flow in the current run and compared it with the three user-supplied mockups plus the approved direct component references.
7. Current official product JSON reconfirmed all eight prices, availability states, `From` requirements, variant counts, and featured-image identities. The current official service source reconfirmed all four Premium Della Services labels.

## Step 5 Flow Audit

1. **Entry and Quick Answer — healthy.** The exact comparison H1, two Collection Paths, immediate system labels, and compressed quick-routing cards make the next action clear without a promotional or SaaS treatment. Evidence: `01-desktop-1440-entry.png` and the five viewport entry captures.
2. **Project Fit — blocked by assets.** The first two image-led cards are clear and credible; New Construction and Multi-Room Renovation still show pending-approval placeholders and break the otherwise mature page rhythm. Evidence: `02-desktop-1440-project-compare.png`.
3. **Key Differences — healthy.** The combined visual/table treatment is more concise than the mockup, retains all six semantic factors, and avoids winner claims. Evidence: `03-desktop-1440-differences.png`.
4. **Installation decision — conditionally healthy.** The simplified diagrams communicate planning relationships and include both not-to-scale labels plus the professional-confirmation note. Visual and copy safety pass; publication still requires named HVAC/product review. Evidence: `04-desktop-1440-installation.png`.
5. **Recommended Product Sets — healthy.** Two system tabs expose four equal cards at a time, preserve full titles/prices/CTAs, and keep collection routing aligned with the active system. The in-app desktop screenshot surface cropped the visible right edge even though DOM bounds, document width, and card measurements remained fully inside the viewport; mobile captures and layout measurements provide the unambiguous visual evidence. Evidence: `05`–`08`.
6. **Premium Della Services, FAQ, and close — healthy.** Trust directly follows the approved reference; all six native disclosures open and close; the final two Collection Paths are clear and compact. Evidence: `09`–`11`.

## Accessibility And Evidence Limits

- Confirmed: semantic regions/headings, native links/buttons/details, tab/tabpanel relationships, managed `tabindex`, visible keyboard focus, 46px-plus mobile targets, no horizontal overflow, responsive reflow, image dimensions, useful alt text, and reduced-motion source rules.
- Arrow Left/Right, Home, and End changed tab selection and focus correctly. The in-app automation surface moved focus but did not synthesize the browser's native button/summary click activation from Enter/Space; native HTML semantics are present, but a real-browser manual Enter/Space check remains the final verification step.
- No claim of full WCAG conformance is made; screen-reader announcement behavior and production-theme interactions require later environment testing.

## Topical Decision QA Score

| Dimension | Score |
| --- | ---: |
| Search intent match | 9.8/10 |
| DTC conversion path clarity | 9.5/10 |
| Della/PageFly visual alignment | 8.9/10 |
| Data/source-truth compliance | 9.8/10 |
| Product merchandising appropriateness | 9.6/10 |
| Mobile UX | 9.3/10 |
| Accessibility/interactions | 9.1/10 |
| AI-template risk avoidance | 9.7/10 |

The structure and implemented components are strong; the visual-alignment score is capped by the two unresolved scene placeholders, not by a need for another module or structural redesign.

## Findings

- **[P2] Final scene assets are still missing for New Construction and Multi-Room Renovation.** The current neutral panels are intentionally temporary and follow the user-approved placeholder path, but they do not match the image-led Project Fit cards in the mockup. Replace them with approved, non-technical 4:3 interior/build scenes before final visual acceptance. Do not show generated HVAC equipment.
- **Accepted deviation — Hero:** official product imagery and CSS replace the mockup's unverified lifestyle composite. This is the approved factual-safety path and keeps both system types immediately identifiable in HTML.
- **Accepted deviation — Quick Answer:** the section is intentionally shorter than the mockup so Project Fit remains the primary decision module.
- **Accepted deviation — Installation:** simplified editable planning diagrams replace technical-looking cutaways. They show only the five approved relationships for each system and include the required not-to-scale label and professional-confirmation disclaimer.
- **[P3] Final technical publication review remains required.** The diagrams avoid precise dimensions and equipment internals, but a named Della product/HVAC reviewer must approve them before publication.
- **Step 4 passed — Recommended Systems:** two accessible tabs expose four products at a time, prices and collection paths remain readable, and only the two approved cards carry the Starting Point badge.
- **Step 4 passed — Trust/FAQ/close:** the services strip directly follows the approved reference; FAQ remains compact and collapsed by default; the closing block presents two equal Collection Paths without decorative distraction.

## Implementation Checklist

- [x] Exactly one approved H1.
- [x] The original ten-section audit completed; the current PRD defines nine sections after removal of the top Benefit Strip.
- [x] No Header, Footer, visible task numbering, or `Whole-Home Renovation` wording.
- [x] Hero labels identify both system types in HTML.
- [x] Six semantic comparison rows remain available on desktop; six accessible factor cards replace the table visually on mobile.
- [x] Installation content contains no exact dimensions, cutaways, DIY steps, or unverified port positions.
- [x] CTA targets, local assets, responsive layout, and console state were checked.
- [x] Both four-product tab states, dynamic collection CTA, keyboard tab controls, and native FAQ disclosures were checked.
- [x] Product cards were checked at desktop, two-column mobile, and sub-360 one-column states.
- [ ] Replace both temporary project-scene panels.
- [ ] Record named HVAC/product approval for the conceptual diagrams.

## Final Result

`blocked`

Step 5 was executed and the result remains blocked. Replace or explicitly approve the two project-scene placeholders and record named HVAC/product review, then rerun Step 5. Step 6, Liquid, and JSON are not authorized while this acceptance result is blocked.
