# Ductless Mini Split vs Central Air — DESIGN

Status: Approved design direction with documented PRD overrides  
Approved visual reference: `Design.png`  
Source of truth for structure/data/interaction: `PRD.md`

## 1. Design direction to preserve

Preserve the mature DELLA ecommerce character shown in `Design.png`:

- a wide, pale product-led Hero rather than an editorial header;
- Spectral display typography paired with Poppins UI/body typography;
- DELLA navy and blue on white and restrained light-blue surfaces;
- compact 4px-radius commerce buttons;
- clean, low-shadow cards with thin borders;
- centered section headings and disciplined whitespace;
- four-product desktop merchandising density;
- a minimal light-blue comparison table;
- a compact pale-cyan installation confirmation bar;
- late-page two-column FAQ and contextual closing CTA.

The overall page should feel calm, high-consideration, product-forward, and recognizably DELLA. Preserve the mockup's visual restraint; do not make the new price/cart controls feel promotional.

## 2. Authority and override rule

The approved mockup controls visual rhythm, hierarchy, card feel, composition, and relative density. It does not control final product data or behavior.

Apply this priority when implementing:

1. Latest explicit owner decision
2. `PRD.md`
3. This `DESIGN.md`
4. `PLAN.md`
5. `Design.png`
6. DELLA/PageFly/Memorial reference files

Never copy generated text, product data, price, fitting-area data, policy claims, or interaction behavior from the mockup when it conflicts with PRD.

## 3. Mandatory mockup overrides

The following details in `Design.png` are obsolete and must not be reproduced:

1. **Delete the product-area path tabs.** The visible `Ductless / Mini Splits`, `Central Air`, and `Supplement / Problem Areas` tabs duplicate the Gateway. Gateway is the sole path selector.
2. **Do not default to ADD/Ductless on organic visits.** With no valid `?path=`, all Gateway cards are unselected and the shopping area displays a neutral prompt.
3. **Restore one concise condition line to each Gateway card.** The mockup is too compressed to preserve the ductwork/problem-area qualifiers reliably.
4. **Separate result from action.** A card shows a recommended starting result and then an action-oriented button.
5. **Replace the mockup's `View Product`-only cards.** Approved cards display price and a transactional state: `Add To Cart`, `Choose Options`, or `Sold Out`, plus a quieter PDP link.
6. **Preserve asymmetric merchandising.** Ductless remains use-case/room-led; Central remains capacity-led.
7. **Add a quiet `Change Project` control** beside or directly below the active shopping-panel heading. It returns to the Gateway; it is not another selector.
8. **Do not generate a new long mockup.** Central, Supplement, neutral, variant, cart, and mobile states are completed and validated in the browser implementation.

## 4. Visual tokens

```css
--navy: #0E1953;
--blue: #5884E7;
--blue-hover: #6B95EF;
--blue-light: #EDF2FF;
--blue-surface: #F4F7FF;
--trust-bg: #DDF7FF;
--gray-50: #F8F9FB;
--gray-100: #F0F2F6;
--gray-200: #E2E6EE;
--gray-300: #C9D1E3;
--text-body: #0E1952;
--text-muted: #53617F;
--white: #FFFFFF;
```

Use Spectral for headings, product names, large capacities, and prices. Use Poppins for body copy, labels, specifications, controls, and buttons.

Target typography:

- H1: 48–56px desktop; 34–42px mobile; line-height about 1.08–1.12.
- H2: 30–36px desktop; 27–31px mobile.
- Body: 16–17px desktop; 16px mobile; line-height about 1.55–1.65.
- Eyebrows/spec labels: 11–13px, concise, uppercase where shown in the mockup.
- Price: Spectral Bold, visually stronger than specifications but below the main product-path heading.

## 5. Layout and section treatment

### Hero

- Preserve the mockup's pale, product-led banner composition and copy-left/equipment-right balance.
- Use the approved H1 exactly: `Ductless Mini Split vs Central Air`.
- Keep the two compact CTAs and generous negative space.
- Product imagery must remain contained and uncropped; the equipment should not collide with copy at intermediate widths.
- No Benefit Strip, announcement bar, product card, price, promotion, or trust strip above or inside the Hero.

### Project Gateway

- Preserve the three-column framed-card layout and restrained line icons.
- Default: three white cards with gray borders and no selected state.
- Selected: blue border, pale-blue surface, optional thin top rule; do not fill the whole card navy.
- Each card order: icon/eyebrow → project title → concise condition → result line → action button.
- Keep the Not Sure Product Finder link as a quiet centered escape hatch below all three cards.
- Buttons and card contents must align vertically without forcing conditions into unreadably small type.

### Conditional shopping area

- Preserve the open merchandising area and four-card density from the mockup, but remove the duplicate tabs.
- Neutral state should be deliberately compact: centered prompt, one brief sentence, and visual breathing room. It must not look like an error or empty component.
- Active heading names the selected path; a quiet underlined `Change Project` control sits nearby without competing with commerce CTAs.

#### Ductless cards

Order:

`use-case/room label → product image → title → compact specs → price → Add To Cart/Choose Options/Sold Out → View Product`

- Keep the mockup's clear 1 Room, 1 Larger Space, 2 Rooms/Dual Zone, and 4 Rooms/Quad Zone distinctions.
- Keep consistent product-media height and restrained spec chips.
- Price and ATC are new, but the card must remain readable rather than becoming a dense PDP tile.

#### Central cards

Order:

`large BTU capacity → SEER2/fitting-area reference → product image → title → price → Add To Cart/Choose Options/Sold Out → View System`

- Large BTU labels are the primary differentiator, especially because 24K/34K/47K share an approved image.
- Use DELLA's live official fitting-area wording exactly when verified; do not force every value into an `Up to` pattern.
- Keep the shared professional load-calculation disclaimer visually connected to the grid.
- Include collection and installer actions below the grid without turning each card into an installer pitch.

#### Supplement panel

- Use one compact visual/category panel, not a product grid.
- 2026-08-17 (owner-approved, final): no enclosing band or card — the panel content sits directly on the shop-section background. Header is a single human-voiced panel H2 "You Know the Room." with no description line and no in-panel H3 (the heading+description+H3 triple was owner-rejected as too much). Body: one lead paragraph ("The one that never quite keeps up…") + 13px confirm fine print + CTAs. Right: the Serena transparent cutout floating chromeless over a warm ground shadow. The three problem spaces ("The garage or workshop" / "The addition or converted space" / "That one room") are unboxed text columns separated by `#dce4f3` hairlines across the full width, stacking to hairline rows on mobile. Owner-rejected along the way: the boxed packshot, an accent-bar card list, a pale-blue band, a warm-gradient band (any enclosing container), and heading stacks. Rules: no boxes within boxes, no accent-bar card lists, no band, one heading only; imagery floats chromeless with a ground shadow; warmth comes from copy voice, not added surfaces.
- Explain that the supplemental mini split is a separate ductless system for a specific problem area.
- Show `Shop Wall-Mounted Mini Splits` and `Find Partner HVAC Installer`.
- Do not use integrated-hybrid-system language.

### Verify section

- Preserve the mockup's light-blue comparison header, fine rules, navy row labels, short cells, and absence of winner styling.
- Keep the installation confirmation immediately below the comparison as one pale-cyan horizontal bar.
- On mobile, transform each comparison row into a stacked card with the criterion first and both system answers below.

### FAQ

- Preserve the compact, late-page appearance and two-column desktop distribution.
- Use native `details/summary`; keep answer text visibly subordinate.
- Mobile uses one column and comfortable 44px minimum summary targets.

### Contextual final CTA

- Preserve the mockup's compact pale-cyan container.
- Content changes with active path; do not repeat the Gateway.
- Default state supports Product Finder and installer; selected states route to the relevant collection and installer.

## 6. Buttons and commerce states

- Primary commerce: solid DELLA blue or navy, white text, 4px radius, at least 44px high.
- Secondary: white or transparent, navy text, light gray/blue border.
- Product ATC: full width.
- PDP detail link: quiet text/underline action below ATC.
- `Choose Options`: visually primary enough to be discoverable, but copy must make clear that PDP selection is required.
- `Sold Out`: disabled, muted, and not styled like an actionable control.
- Loading state: `Adding…`; prevent duplicate submission.
- Success is followed by same-tab navigation to Cart in production V1; no cart drawer or success modal.

Do not show compare-at prices, discount styling, coupons, sale badges, financing, or promotion copy.

## 7. Interaction design

- Gateway cards are semantic buttons with visible focus and `aria-pressed`.
- A user selection activates one card, shows its panel, updates final CTA, updates analytics attributes, updates only the URL `path` parameter, then scrolls to shopping unless reduced motion is requested.
- A URL preselection activates state without scrolling past the Hero.
- `Change Project` returns focus to the active/first Gateway card and scrolls to the Gateway.
- All DELLA links open in the same tab.
- Do not depend on hover to explain selection or availability.

## 8. Responsive rules

- 1440/1280: full 1200px container; four product cards; three Gateway cards.
- 1024/768: Gateway may remain three columns only if conditions remain readable; otherwise use two plus one or stack. Product grid becomes two columns.
- 430/390: one-column Gateway; two-column product grid only if titles, prices, and buttons remain readable.
- 360 and below: product grid becomes one column rather than compressing transactional controls.
- Hero stacks copy above equipment; preserve complete equipment silhouettes.
- FAQ becomes one column.
- Installation bar stacks copy and actions cleanly.
- No horizontal page overflow at any required viewport.

## 9. Asset strategy

- Localize Spectral and Poppins font files from approved DELLA reference assets.
- Localize all eight supplied product images into `assets/products/`; preserve original source mappings in `sources.md`.
- Build Hero from localized Serena 12K and Central 34K equipment assets; do not crop essential equipment.
- Use simple inline SVG or CSS icons for Gateway only if they match the mockup's thin navy line style. Decorative icons use empty accessibility labels.
- Do not use `Design.png` as a flattened page background or crop AI-rendered product imagery from it.

## 10. Visual QA criteria

- First impression is DELLA ecommerce, not an SEO blog or SaaS page.
- Hero closely preserves the mockup's balance and hierarchy.
- No Benefit Strip or duplicate shopping tabs.
- Gateway conditions, results, and actions remain scannable.
- Neutral state is clear and intentional.
- Ductless and Central card hierarchies are visibly different for a reason.
- Price and ATC fit naturally without promotional residue.
- All commerce states align without card-height collapse.
- Central repeated images remain distinguishable by capacity.
- Comparison is legible on mobile without horizontal scrolling.
- Focus states, selected states, disabled states, and reduced motion are visually complete.

