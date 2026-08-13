# DELLA — Ductless Mini Split vs Central Air
## Full-Page Ecommerce Landing Page Mockup Prompt

Create a polished, high-fidelity **full-page long-scroll desktop ecommerce landing-page mockup image** for DELLA. This is a visual design task only. **Do not generate HTML, CSS, JavaScript, wireframes, or written strategy.**

The page is an evergreen comparison and guided-shopping landing page for:

`Ductless Mini Split vs Central Air`

It must support research-intent SEO traffic and Google/Meta advertising while looking like a mature DELLA Shopify ecommerce page—not an article, SaaS website, dashboard, or generic AI landing page.

## Source of truth and conflict rule

The approved project PRD is the source of truth:

`C:\Users\18041\Desktop\della-pages\Ductless Mini Split vs Central Air\PRD.md`

Visual references, in priority order:

1. `C:\Users\18041\Desktop\della-pages\della页面设计规范\della-memorial-day-design-system.md`
2. `C:\Users\18041\Desktop\della-pages\della页面设计规范\page.pf-ef33e2e6.json.txt`
3. `C:\Users\18041\Desktop\della-pages\della页面设计规范\pf-ef33e2e6.liquid.txt`
4. `C:\Users\18041\Desktop\della-pages\memorial-day-sale`
5. DELLA coupon-code page and existing DELLA comparison pages for ecommerce rhythm only

If this prompt, an AI-generated visual, or a reference page conflicts with the PRD, **the PRD wins** for structure, products, content, claims, CTA destinations, and interaction logic.

## First-principles goal

The page must help a homeowner answer:

**What HVAC project am I trying to solve, and what is the right DELLA starting path?**

The decision model is:

- **Replace** an existing whole-home ducted system → Central Air starting path
- **Add** comfort without relying on whole-home ductwork → Wall-Mounted Mini Split starting path
- **Supplement** a working central system in an isolated problem area → separate Wall-Mounted Mini Split plus installer guidance

Treat every result as a starting point, not a guaranteed HVAC prescription.

The page sequence is fixed:

`Answer → Identify Project → Shop the Right Path → Verify → FAQ → Convert`

Do not add modules.

## Critical opening rule

**The page begins directly with the Hero.**

There is:

- no Benefit Strip;
- no announcement/trust strip above the Hero;
- no standalone Quick Answer block;
- no navigation/header/footer inside this custom landing-page design;
- no promotional campaign chrome.

The Hero itself supplies the direct answer.

## Artboard and presentation

- Produce one coherent **1440px-wide desktop long-scroll page mockup**.
- Use a centered content container of approximately 1200px with 32px side padding.
- Show the `ADD` path selected in the mockup so the Ductless shopping grid can be designed visibly. This is only a visual demonstration of the active state.
- Do **not** imply that Ductless is selected by default in production. The real organic page begins neutral; valid ad parameters may preselect a path.
- Also show enough clear visual-system logic that Central and Supplement panels can reuse the same section shell while retaining their intentionally different merchandising formats.
- Do not place browser chrome, design-tool UI, annotations, arrows, measurements, or explanatory callouts around the final page.

## DELLA visual direction

Create a clean, visual-first, product-first DELLA ecommerce page with restrained editorial polish.

Typography:

- H1, H2, H3, and product titles: **Spectral Regular**, fallback Georgia serif
- Body, buttons, labels, controls, tables: **Poppins**, fallback Arial sans-serif
- H1: approximately 48–56px desktop, short and composed
- H2: approximately 30–36px
- Body: 16–17px with comfortable line height

Color system:

- Navy: `#0E1953`
- DELLA blue: `#5884E7`
- Blue hover/accent: `#6B95EF`
- Light blue: `#EDF2FF`
- Blue surface: `#F4F7FF`
- Pale cyan trust/confirmation surface: `#DDF7FF`
- Light borders: `#E2E6EE`
- Main body text: `#0E1952`
- White: `#FFFFFF`

Component grammar:

- Ecommerce buttons: 4px radius, 48px height, compact 12px × 24px padding
- Primary buttons: navy or DELLA blue fill with white text
- Secondary buttons: white with a subtle border and navy text
- Cards: white, 4–6px radius, light border, minimal shadow
- Active path card: `#5884E7` border, `#F4F7FF` background, optional thin blue top rule
- Product media areas: consistent height, white background, packshots centered with `object-fit: contain` behavior
- Section rhythm: approximately 72–80px main spacing and 52–64px compact spacing

Avoid excessive rounded corners, floating layers, heavy shadows, dense dark sections, and decorative visual noise.

---

# Fixed page structure

## BLOCK 1 — Ecommerce comparison Hero / Direct Answer

Create a wide DELLA ecommerce banner with an approximate 2.8:1 visual grammar. Use a clean white, very light blue, or neutral background—not a gradient-heavy background.

Left side:

H1:

`Ductless Mini Split vs Central Air`

Supporting copy:

`Wall-mounted ductless mini splits give you flexible room-by-room or multi-zone comfort without relying on whole-home ductwork. Central air uses an air handler and duct system to distribute comfort throughout the home. Start with the project you are trying to solve.`

Primary CTA:

`Find My Best Starting Point`

Secondary CTA:

`Compare the Tradeoffs`

Right side:

- Build a restrained product composition using a DELLA Serena 12K wall-mounted mini split packshot and a DELLA 34K central air outdoor-unit/air-handler packshot.
- Make the two system architectures immediately legible without adding explanatory cards.
- Keep enough negative space around equipment.
- Do not place product prices, sale badges, comparison winner labels, or product cards in the Hero.

The Hero should feel like a finished DELLA ecommerce banner, not a blog masthead or SaaS split-screen panel.

## BLOCK 2 — Project Gateway / Identify Project

Heading:

`What Are You Trying to Solve?`

Subcopy:

`Start with the project, not the equipment. Choose the situation closest to your home and we’ll show you the most useful DELLA starting point.`

Use three equal-width project cards on desktop:

### Card 1

Eyebrow: `REPLACE`

Title: `Replace a Whole-Home Ducted System`

Copy: `Your home already has usable ductwork and you are replacing the primary ducted HVAC equipment.`

Result: `Start with Central Air`

Button: `Show Central Air Options`

### Card 2 — show this selected in the mockup

Eyebrow: `ADD`

Title: `Add Comfort Without Relying on Ductwork`

Copy: `You need comfort in an older home, addition, garage, converted room, or several spaces without depending on a whole-home duct system.`

Result: `Start with Wall-Mounted Mini Splits`

Button: `Show Ductless Options`

### Card 3

Eyebrow: `SUPPLEMENT`

Title: `Fix Problem Areas Without Replacing Everything`

Copy: `Your central system still serves most of the home, but one or more rooms need additional comfort.`

Result: `Consider a Supplemental Mini Split`

Button: `Explore This Path`

Below the three cards, add a visually quiet inline escape hatch—not a fourth card:

`Not sure which project fits?  Find My System →`

The Gateway is the page’s most important interaction. It should be prominent and easy to scan, but not oversized or gimmicky. Avoid quiz styling, large icons, and a dark active card.

## BLOCK 3 — Conditional Shopping Area / Shop the Right Path

In this full-page mockup, show the **Ductless / ADD state** visibly because the ADD Gateway card is selected.

Heading:

`Build Your Wall-Mounted Mini Split Setup`

Copy:

`Start with the number and size of spaces you want to condition. Final equipment sizing still depends on the room load and installation plan.`

Show four DELLA ecommerce product cards in one desktop row:

1. `1 ROOM` — Serena Series 12K — 22 SEER2
2. `1 LARGER SPACE` — Vario Series 18K — 21 SEER2
3. `2 ROOMS / DUAL ZONE` — Vario Series 28K — 12K + 12K — 20 SEER2
4. `4 ROOMS / QUAD ZONE` — Vario Series 35K — 9K + 9K + 9K + 12K — 19 SEER2

Product-card hierarchy:

`consistent product image → room/zone eyebrow → product title → compact specifications → current price → full-width Add To Cart button → quiet View Product link`

Below the grid, show:

`Shop All Wall-Mounted Mini Splits`

Include one concise sizing note beneath the merchandise area. Reserve a clear price line on every product card and show `Add To Cart` as the primary full-width button. Because this is an AI visual mockup, use a clearly non-authoritative placeholder price such as `$X,XXX.XX`; Codex will replace it with current verified Shopify data. Do not show compare-at prices, ratings, coupon text, promotion badges, winner badges, or fake stock status.

### Central active-state design rule

Although the main mockup shows Ductless active, define the visual grammar so the alternate Central state can use four **capacity-first** cards:

- 24K BTU / 18 SEER2
- 34K BTU / 19 SEER2
- 47K BTU / 18 SEER2
- 53K BTU / 17 SEER2

Central hierarchy must be:

`large capacity label → SEER2 → optional verified DELLA fitting-area reference → product image → title → current price → Add To Cart → quiet View System link`

Any fitting-area range is secondary reference information only. Do not invent a number in the mockup. Use a neutral placeholder such as `Verified fitting-area reference` if it must appear visually. The implemented page will insert only live-verified DELLA data and will include a professional load-calculation disclaimer.

### Supplement active-state design rule

The Supplement state is a compact category/installer panel—not a third four-product grid. It explains that a separate wall-mounted mini split may address a garage, addition, converted space, or persistent hot/cold room while the central system continues serving the rest of the home.

Actions:

- `Shop Wall-Mounted Mini Splits`
- `Find Partner HVAC Installer`

Do not call this an integrated hybrid system or hybrid package.

## BLOCK 4 — Verify

### Compact comparison

Heading:

`Mini Split vs Central Air: What Actually Changes?`

Subcopy:

`Both paths can provide home comfort. The main differences are how air is distributed, how rooms are controlled, and what the installation requires.`

Create a clean comparison table with three columns:

- Compare
- Wall-Mounted Mini Split
- Central Air

Use only six rows:

- Distribution
- Whole-home ductwork
- Room control
- Indoor equipment
- Installation scope
- Retrofit flexibility

Use a light-blue header, minimal borders, short cells, and a stronger navy first column. Do not use checkmarks, red X marks, winner badges, `Best`, or recommendation coloring.

### Installation reality bar

Immediately below the table, place one compact pale-cyan horizontal bar.

Eyebrow: `BEFORE YOU BUY`

Heading: `Confirm the Installation Before Choosing the Final System`

Copy: `Confirm equipment sizing, duct condition, electrical requirements, line routing, equipment placement, and installation scope before purchase.`

Actions:

- `Find Partner HVAC Installer`
- `Find My System`

This is a compact confirmation bar, not a separate large installation section.

## BLOCK 5 — Compact FAQ

Use a restrained native-accordion visual near the bottom of the page. Show six concise questions:

1. `What is the main difference between a ductless mini split and central air?`
2. `Can a ductless mini split heat and cool an entire house?`
3. `Can I add a mini split if I already have central air?`
4. `Does central air require ductwork?`
5. `Is a mini split always more efficient than central air?`
6. `How should I size a mini split or central air system?`

Keep the FAQ visually compact. Do not turn answers into article-length copy.

## BLOCK 6 — Contextual Final CTA

Show the Ductless-selected final state because ADD is active in this mockup.

Use a pale-cyan `#DDF7FF` surface, not a heavy navy sales banner.

Heading:

`Ready to Build Your Ductless Setup?`

Primary CTA:

`Shop Wall-Mounted Mini Splits`

Secondary CTA:

`Find Partner HVAC Installer`

The implemented component will change its heading and destination for default, Central, and Supplement states. Do not add a second decision selector here.

---

# Mobile design expectations

The final implementation will be checked at 360px, 390px, 430px, 768px, 1024px, 1280px, and 1440px. Design the desktop mockup so it has a clear responsive interpretation:

- Hero copy and product composition stack cleanly on mobile.
- Gateway becomes three stacked full-width cards followed by the inline Not Sure escape hatch.
- Product grid becomes two columns when readable and one column below approximately 380px if titles or CTAs become cramped.
- No product carousel.
- Comparison table transforms into stacked comparison cards by row; do not require horizontal scrolling.
- Buttons remain at least 44px high.
- No clipped headings, overlapping buttons, tiny table text, or horizontal page overflow.

# Content and data caveat

This image is a visual reference only.

- Product names, product images, product URLs, BTU, SEER2, fitting-area ranges, prices, availability, variant IDs, policy text, CTA destinations, and FAQ answers must come from the PRD and verified DELLA/Shopify sources during implementation.
- Any generated image text that differs from the PRD is placeholder text and must not be copied into production.
- Any price visible in the AI mockup is layout placeholder text only. Do not treat it as product data. The implemented page must use current verified Shopify price and availability.
- Do not invent discounts, compare-at prices, reviews, warranties, financing, rebates, tax credits, savings percentages, coverage promises, installer promises, or sizing recommendations.
- Exact Central fitting-area figures are intentionally omitted from this prompt pending implementation-time live verification.

# Negative prompt

Do not create:

- Benefit Strip or announcement bar
- standalone Quick Answer block
- navigation or footer
- SaaS dashboard or app interface
- split-screen SaaS cards as the Hero
- glassmorphism
- decorative orbs
- purple or heavy gradients
- oversized 70–90px typography
- generic icon feature grid
- large-radius pill cards or pill primary buttons
- heavy shadows
- winner badge, `Best Choice`, red X, or checkmark war
- Memorial Day graphics, holiday language, coupons, countdowns, sale badges, financing, rebates, or tax-credit claims
- fake prices presented as real data, compare-at prices, fake promotions, or `Buy Now`
- testimonials, review carousel, influencer section, email signup, or popup
- Home Situations section
- Premium DELLA Services section
- separate Installation Guide section
- decision quiz, calculator, or long SEO article blocks
- extra sections of any kind

# Final visual test

The finished image should immediately read as:

**DELLA ecommerce decision landing page**

It should not read as:

**SEO blog, generic comparison article, AI template, SaaS landing page, or promotional sale page.**

Every visible block must move the visitor closer to the correct next action. Preserve strong whitespace, disciplined ecommerce rhythm, concise copy, clear product imagery, and DELLA’s navy/blue/light-blue visual system.
