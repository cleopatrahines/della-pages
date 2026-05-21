# Della Memorial Day Sale Design System Extraction

Source reference: https://dellahome.com/pages/memorial-day-sale  
Purpose: reusable design rules for Della topical landing pages in `C:\Users\18041\Desktop\della-pages`.

## Extraction Status

This is a page-level extraction, not just a mood note. It records the visible content structure, reusable UI rules, typography assumptions, product-card grammar, spacing, CTA hierarchy, and what must not be copied from the campaign.

Limitations:
- The reference is a live Shopify campaign page. Some exact CSS class names and private theme files are not exposed in the text extraction.
- Exact values below combine the Memorial Day page evidence with the current Della scenario pages in this folder, which use the same Della page family: Roboto, navy `#0E1953`, action blue `#5884E7`, light-blue support panels, 4px buttons, and white product cards.

## Visible Memorial Day Page Structure

The reference page is an ecommerce campaign page with this sequence:

1. Announcement/header area
   - Messages: `Free Shipping For ALL Order`, `Flexible Financing starts at 0% APR.`, `Orders paid via Shop Pay may earn 1% Shop Cash`.
   - For non-sale topic pages, reuse the trust-bar idea but not financing unless requested.

2. Full campaign hero image
   - Desktop asset name shown by Shopify: `DELLA_2800x1000px ...jpg`.
   - Mobile asset name shown by Shopify: `DELLA_960x1200px ...jpg`.
   - Rule: hero is visually led, wide, direct, and ecommerce-first. It is not a long editorial hero and not a SaaS card layout.

3. Subscription / lead capture strip
   - Heading: `Subscribe to Get 5% Discount on Your First Order`.
   - Subscriber count and a short button.
   - Rule: secondary conversion modules are compact and direct.

4. Lifestyle image band
   - Heading: `Cool Comfort for Every Workout`.
   - Uses two large images before dense copy.
   - Rule: break up commerce pages with visual use-case proof, not explanatory walls of text.

5. Featured campaign/product block
   - Heading: `Pre-Sale: Della 42" Smart Tower Fan`.
   - Product image, short benefit bullets, price/compare price, one CTA.
   - Rule: product modules pair one strong visual with concise benefit claims.

6. Mini split product merchandising section
   - Heading: `Stay Cool All Summer Long with Mini Splits`.
   - Offer line appears under heading on the campaign page.
   - Product card pattern: image, product title, current price, compare-at price, `Add To Cart`.
   - For decision pages, keep the card pattern but change CTA to `View Product`.

7. Secondary product merchandising section
   - Heading: `Effortless Cooling with Window & Portable ACs`.
   - Same card pattern repeated.
   - Rule: repeated ecommerce sections are acceptable when the grid is visually consistent.

8. Giveaway / referral / trust / review blocks
   - Campaign-specific modules appear after product paths.
   - For topic pages, replace these with installer, rebate, warranty, and support confidence modules.

9. FAQ
   - Compact Q/A section near the bottom.
   - Rule: FAQ supports purchase confidence, but should not turn the page into a blog.

10. Footer
   - Newsletter, Della slogan `Make every room your comfort zone.`, shop/support/about links, payment icons.

## Typography System

Use:
- Font family: `Roboto`, fallback `Arial`, `sans-serif`.
- Body: 16-17px desktop, 16px mobile, line-height 1.6.
- H1: 40-58px desktop, 34-44px mobile, font-weight 700, line-height 1.05-1.1.
- H2: 25-36px desktop, 28-32px mobile, font-weight 700.
- H3/product title: 15-18px, font-weight 700.
- Label/eyebrow: 12px, uppercase, 0.13-0.14em letter spacing, blue text on light-blue pill.

Avoid:
- 70-90px oversized SaaS hero type.
- Negative letter spacing beyond subtle `-0.02em`.
- Decorative display fonts.
- Paragraph-first page openings.

## Color Tokens

Use these as the working Della topical-page tokens:

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
--text-body: #1A2550;
--text-muted: #5C6A8A;
--white: #FFFFFF;
```

Rules:
- Navy is for headings, dark panels, and high-confidence decision areas.
- Blue is for primary ecommerce buttons and active states.
- Light blue is for section labels, selector hover states, and low-emphasis backgrounds.
- Trust cards use pale cyan/light blue, not white cards with heavy shadows.
- White is the default product-card and content-card background.

Avoid:
- Purple gradients.
- Beige/brown palettes.
- Dense dark-blue sections stacked back to back.
- Sale red unless the page is actually a promotion.

## Buttons

Base:
- Height: 48px desktop; 44-48px mobile.
- Border radius: 4px.
- Padding: 12px 24px.
- Weight: 700.
- No pill buttons for primary ecommerce CTAs.

Button types:
- Primary commerce: blue fill, white text.
- Navy button: navy fill, white text.
- Secondary: white/transparent fill, navy text, light gray border.
- Product CTA: full width inside product card, `View Product`.

Hover:
- Primary can invert to white with blue text.
- Outline can shift to light-blue background.
- Product card can lift slightly, but do not over-animate.

Avoid:
- Gradient buttons.
- More than three CTA treatments on one page.
- `Add To Cart` on high-consideration mini split comparison pages unless explicitly requested.

## Layout And Spacing

Desktop:
- Container: 1200px max, 32px side padding.
- Section rhythm: 72-80px vertical padding.
- Compact product/support sections: 52-64px.
- Grid gaps: 14-24px.

Mobile:
- 16px side padding.
- Section rhythm: 48-56px.
- Product cards stack one column.
- Horizontal room selector can scroll, but touch targets must stay large.

Reference pattern:
- The Memorial page is visual-first and product-first.
- Topic pages should show the decision path above the product grid, but product cards must arrive early.

## Hero Rules For Topic Pages

Memorial uses a full campaign image. For non-promo topic pages:

Use:
- Wide image-led commerce hero with text over a real product/use-case background.
- Short H1, one-sentence answer, two CTAs, and a compact decision note.
- Room-count path selector directly below the hero.
- A hint of trust/shop content visible in the first viewport.

Avoid:
- Full editorial article intro.
- Split-screen SaaS hero cards as the main hero.
- Dark explanation cards as the main hero.
- Holiday hero image, countdown, code, or sale badge.
- Generic SaaS cards with abstract icons.

## Trust Cards

Use the screenshot-like pattern:
- Three equal cards.
- Pale blue background.
- Left circular icon.
- Two-line copy.
- Right-aligned `Learn more`.

Approved copy for this project:
- `Free Shipping` / `Ships in 24 hours`
- `24/7 Live Chat` / `Weekday technical help`
- `Lifetime Warranty` / `Mini split systems`

Do not use:
- `0% APR` on this page.
- Federal tax credit claims as a main trust message.

## Product Card Pattern

Memorial card pattern:
- White card.
- Large product image.
- Product title.
- Current price.
- Compare-at price when available.
- One CTA.

For mini split decision pages:
- Show 4 cards per active room-count panel.
- CTA is `View Product`, not `Add To Cart`.
- Include compact specs: zone count/BTU, SEER2 or indoor unit configuration, coverage.
- Keep product image area consistent to avoid layout shift.
- Use tabs or selector buttons for 1, 2, 3, 4, 5 rooms.
- Keep the product section visually open like a merchandising grid; avoid placing a card grid inside another heavy card.

Avoid:
- Product cards in the first hero screen.
- Editorial recommendation cards pretending to be products.
- More than 4 visible product cards per panel.

## Tables And Decision Modules

Comparison table:
- Light-blue header.
- Minimal borders.
- Navy first column.
- Short cells.
- No winner badges.

Advanced decision:
- Use a two-column layout.
- One navy panel and one white panel can work.
- Keep bullets short.
- This belongs after the product cards for ad users.

Buyer notes:
- Use three short cards.
- One navy card can highlight the key nuance.
- Do not make this a long essay.

## FAQ

Use:
- FAQ near the bottom.
- Six questions for this page.
- Native `details/summary` acceptable for HTML demo.
- FAQ schema can be included, but do not rely on rich results.

Avoid:
- 10+ FAQ items.
- Repeating the entire article in FAQ form.

## Do Not Copy From Memorial Day Sale

Do not copy:
- Memorial Day holiday theme.
- Countdown timers.
- Discount code `HONOR10`.
- Sale red badges.
- Giveaway mechanics.
- Referral commission copy.
- `Add To Cart` primary behavior.
- Financing as a trust message for this decision page.

Copy/adapt:
- Visual-first ecommerce rhythm.
- Product merchandising section.
- Direct short headings.
- Light-blue trust cards.
- Compact CTA style.
- Bottom FAQ placement.
- Footer/newsletter confidence style if needed later.

## Application To Single-Zone vs Multi-Zone

Required module order:
1. Commerce hero with direct answer.
2. 1-5 room collection strip.
3. Trust cards.
4. Quick answer.
5. Single vs multi comparison table.
6. Product tabs with 4 visible product cards.
7. One multi-zone vs multiple single-zone.
8. Buyer notes.
9. Scenario cards.
10. Cost and installation planning.
11. Support confidence block.
12. Six-item FAQ.
13. Bottom collection strip.

Success criteria:
- Looks like Della ecommerce, not a generic AI blog.
- Product cards visually resemble Della merchandising.
- First task is still path selection, not immediate add-to-cart.
- Mobile has no horizontal text overflow.
- No stale promo, financing, or federal tax-credit claim.
