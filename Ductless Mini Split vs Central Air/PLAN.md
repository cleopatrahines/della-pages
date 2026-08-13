# Ductless Mini Split vs Central Air — Implementation Plan

Status: Ready for implementation after live product snapshot  
Project: `C:\Users\18041\Desktop\della-pages\Ductless Mini Split vs Central Air`  
Primary output: `ductless-mini-split-vs-central-air.html`

## 1. Source hierarchy

1. Latest owner instruction
2. `PRD.md`
3. `DESIGN.md`
4. This plan
5. Approved `Design.png`
6. DELLA design-system/PageFly reference files

The mockup controls visual direction. PRD controls content, products, data, claims, routing, states, and interactions.

## 2. Planned project files

```text
Ductless Mini Split vs Central Air/
├─ PRD.md
├─ GEMINI_DESIGN_PROMPT.md
├─ Design.png
├─ DESIGN.md
├─ PLAN.md
├─ ductless-mini-split-vs-central-air.html
├─ sources.md
├─ HANDOFF.md
└─ assets/
   ├─ fonts/
   │  ├─ Spectral-Regular.woff2
   │  ├─ Spectral-PageFly-Medium.woff2
   │  ├─ Spectral-Bold.woff2
   │  ├─ Poppins-400.woff2
   │  └─ Poppins-600.woff2
   └─ products/
      ├─ serena-12k.webp
      ├─ vario-18k.webp
      ├─ vario-dual-28k.webp
      ├─ vario-quad-35k.webp
      ├─ central-24k.webp
      ├─ central-34k.webp
      ├─ central-47k.webp
      └─ central-53k.webp
```

Do not create a duplicate `index.html`. Add a Liquid adapter file only if the confirmed Shopify deployment surface requires a separate theme-section/template artifact; document that decision in `HANDOFF.md` before creating it.

## 3. Pre-implementation live verification

Before writing final product markup:

1. Verify all eight owner-approved PDPs still resolve and remain the intended products.
2. Capture current title, price, availability, variant count/options, intended purchasable variant ID, and official fitting/coverage wording.
3. Verify both collections, Product Finder, and installer URLs.
4. Preserve owner-supplied product identity and image mapping unless a conflict is reported to the owner.
5. Record source URL, captured value, and verification date in `sources.md`.
6. Determine whether each product state is:
   - one unambiguous available variant → ATC;
   - customer choice required → Choose Options;
   - unavailable → Sold Out.

Do not infer an intended variant from `variants[0]`.

## 4. Runtime and product-data architecture

Build one namespaced page component using Vanilla HTML, CSS, and JavaScript. Use `.della-system-compare` as the root namespace; avoid global element selectors and PageFly-generated classes.

### Production Shopify priority

1. **Liquid first:** if the final Shopify template/section evaluates Liquid, resolve all eight products by handle with `all_products`, render current price/availability/variant metadata server-side, and serialize only the minimal state needed by the page script. Eight handles stay below Shopify's 20-handle per-page limit.
2. **Ajax Product API fallback:** if the confirmed PageFly/custom-HTML surface cannot evaluate Liquid, fetch current Shopify product data on the same Shopify storefront and hydrate the cards. Document this fallback and its loading/error state in `HANDOFF.md`.
3. Do not make Product JSON requests when Liquid has already supplied valid data.

### Static/GitHub preview

- Render a dated implementation snapshot from `sources.md` so layout can be reviewed.
- Clearly mark runtime as preview in code/data attributes, not in prominent user-facing page copy.
- Disable real cart transactions outside the DELLA Shopify storefront.
- Preview buttons demonstrate ATC/Choose Options/Sold Out visual states; PDP and collection links may remain functional same-tab links.

## 5. Cart behavior

- For an unambiguous available variant on Shopify, POST quantity 1 and its exact variant ID to the locale-aware Cart API using `window.Shopify.routes.root + 'cart/add.js'`.
- Disable the button and show `Adding…` during submission.
- On success, navigate in the same tab to the locale-aware cart route.
- On a 422 or network error, restore the button and show a concise accessible inline error; do not silently redirect or claim success.
- Do not open or implement a theme cart drawer.
- Choose Options and PDP links open in the same tab.
- Never run the real cart request on GitHub/local preview.

## 6. HTML structure

Implement these six blocks only:

1. Hero / Direct Answer
2. Project Gateway
3. Conditional Shopping Area
4. Verify Comparison + Installation Bar
5. Compact FAQ
6. Contextual Final CTA

All three shopping panels remain in the DOM. Add `.js` to the document root early; CSS hides inactive panels only when JavaScript is active. Without JavaScript, show Ductless, Central, and Supplement sequentially with clear headings.

Do not implement Benefit Strip, Quick Answer, duplicate path tabs, Home Situations, Services, testimonials, newsletter, calculator, carousel, or any unapproved module.

## 7. Path-state implementation

Use one state variable: `null`, `ductless`, `central`, or `supplement`.

On initialization:

- parse `path` from `new URL(window.location.href)`;
- accept only the three valid values;
- apply a valid preselection without auto-scroll;
- otherwise preserve neutral state and show the neutral shopping prompt.

On Gateway selection:

- set `aria-pressed` and active visual state;
- show only the selected panel;
- update panel heading and contextual final CTA;
- update analytics data attributes;
- preserve every query parameter and update only `path` using `history.replaceState`;
- smooth-scroll to the shopping area unless reduced motion is enabled.

On neutral/reset:

- remove `path` while preserving all other query parameters;
- use `replaceState`, not `pushState`;
- do not refresh.

`Change Project` scrolls to the Gateway and moves focus to the appropriate Gateway control. It does not create a second selector.

## 8. Product-card implementation

### Ductless

- Use-case/room label
- Local product image
- Product name
- Zone/BTU/SEER2/coverage reference
- Current price
- ATC, Choose Options, or Sold Out
- View Product

### Central

- Prominent BTU capacity
- SEER2 and official live-verified DELLA fitting-area wording
- Local product image
- Product name
- Current price
- ATC, Choose Options, or Sold Out
- View System

Use a single grid/card foundation only for spacing and responsive behavior. Preserve distinct internal hierarchies; do not normalize both paths into the same information order.

Below Central, include the professional load-calculation disclaimer and installer/collection actions. Supplement uses no product grid.

## 9. CSS implementation

- Inline page CSS in the final HTML unless Shopify integration requires extraction.
- Define all tokens under `.della-system-compare` or uniquely prefixed custom properties.
- Add local `@font-face` declarations with `font-display: swap`.
- Use CSS Grid for Gateway, product grids, comparison desktop layout, and FAQ.
- Use consistent product-media aspect boxes and explicit image width/height to control CLS.
- Provide visible `:focus-visible` states.
- Provide selected, loading, disabled, error, and neutral states.
- Respect `prefers-reduced-motion`.
- Avoid horizontal carousels and table overflow on mobile.

## 10. Responsive implementation

Required QA widths: 1440, 1280, 1024, 768, 430, 390, and 360px.

- Desktop: three Gateway cards, four product cards, desktop comparison table, two-column FAQ.
- Tablet: decide three/stacked Gateway based on real text fit; two product columns.
- Mobile: one Gateway column; two product columns only where readable; one column at 360px or whenever CTA/title fit fails.
- Convert each comparison row into a stacked mobile comparison card.
- Stack installation-bar and final-CTA actions without overflow.
- Use one-column FAQ.

## 11. Accessibility

- Use semantic `main`, sections, headings, buttons, links, product articles, and native FAQ details/summary.
- Gateway controls use `aria-pressed`; panels use appropriate hidden/inert treatment when inactive.
- Do not leave focus inside a panel when it becomes hidden.
- Provide a polite live region for cart status/errors.
- Touch targets are at least 44px.
- Product alt text remains concise; decorative Hero duplicates use empty alt.
- Keyboard-test Gateway, Change Project, product actions, FAQ, and final CTA.

## 12. SEO and metadata

- One H1: `Ductless Mini Split vs Central Air`.
- Use approved title and meta description from PRD.
- Visible FAQ and FAQPage JSON-LD must match exactly.
- Do not hide an SEO essay or product-panel content solely for crawlers.
- Target production URL: `https://dellahome.com/pages/ductless-mini-split-vs-central-air`.
- Do not hard-code the production canonical in static/GitHub preview.
- After the Shopify Page/handle exists, production theme metadata uses Liquid `canonical_url`.

## 13. Analytics

Add data hooks for:

- `della_path_selected`
- `della_product_click`
- `della_add_to_cart`
- `della_collection_click`
- `della_installer_click`
- `della_final_cta_click`

Include path, product handle/variant where applicable, position, source section, and destination. Guard any existing `window.gtag` call; do not load or initialize analytics.

## 14. Performance and assets

- Download and convert the eight approved product images to WebP without altering product identity.
- Use the Hero equipment assets eagerly; lazy-load below-fold products.
- Include intrinsic image dimensions.
- Do not base64-embed large assets or add third-party libraries.
- Use local fonts and product assets for stable review.
- Avoid animation beyond modest state/hover transitions.

## 15. QA sequence

1. Validate document structure, one H1, metadata, and exact product mapping.
2. Test neutral, ductless, central, and supplement states.
3. Test all three valid `?path=` values and an invalid value.
4. Confirm every non-path query parameter survives path selection and clearing.
5. Test no-JS panel visibility.
6. Test all eight product states/data and same-tab PDP/collection links.
7. On Shopify, test ATC success, 422/error handling, and same-tab Cart navigation; confirm GitHub/local cannot transact.
8. Test FAQ UI and exact JSON-LD match.
9. Test keyboard/focus, reduced motion, and screen-reader state attributes.
10. Screenshot and inspect every required viewport for overflow, card alignment, Hero crop, CTA fit, and comparison readability.
11. Check console errors and broken local assets.
12. Record results and remaining integration risks in `HANDOFF.md` and the final QA report.

## 16. Stop conditions

Stop and report instead of guessing if:

- the Shopify deployment surface is still unknown and production Liquid/Ajax binding cannot be selected safely;
- any approved PDP is missing or conflicts with owner-supplied identity;
- a product's intended variant cannot be resolved unambiguously;
- official Central fitting-area wording is unavailable or inconsistent;
- production Page/handle is not created when canonical integration is requested;
- cart behavior cannot be tested on the Shopify storefront.

Do not compensate for missing data by inventing price, variant, fitting area, availability, or claims.

## 17. Commit and push conditions

- No commit or push until implementation and browser QA are complete.
- Check repository, branch, and working tree before staging.
- Preserve unrelated user changes.
- Obtain explicit owner approval before commit/push.

