# Della Memorial Day Sale Design System Extraction

Source reference: https://dellahome.com/pages/memorial-day-sale  
Purpose: reusable design rules for Della topical landing pages in `C:\Users\18041\Desktop\della-pages`.

## Extraction Status

This is a page-level extraction, not just a mood note. It records the visible content structure, reusable UI rules, typography assumptions, product-card grammar, spacing, CTA hierarchy, and what must not be copied from the campaign.

Limitations:
- The current live Shopify page is PageFly-generated, so most exact style values are emitted through runtime class names and PageFly assets rather than clean source CSS.
- The extraction below is based on the live PageFly template files `pf-ef33e2e6.liquid.txt` and `page.pf-ef33e2e6.json.txt`, plus the current Della scenario pages in this folder.

## Confirmed PageFly Source

Evidence that this is the current 2026 Memorial Day page:
- Shopify admin page `Memorial Day Sale` is visible as of `May 18, 2026 at 11:52 PM PDT`.
- The page is bound to template `pf-ef33e2e6`.
- The exported JSON section is `pf-ef33e2e6`.
- The campaign copy says `May. 19 - May. 26`, `Save 10% on Orders $300+ or 12% on Orders $2,000+`, and `2X reward points`.
- PageFly page setting: `pageId` = `ef33e2e6-faec-494b-b829-e47b938fc106`, `pageTitle` = `Promotions`, PageFly version `4.26.3.31`.

Confirmed PageFly section order:
1. `pf-f432`: desktop and mobile full hero image.
   - Desktop image ratio `2.8`.
   - Mobile image ratio `1`.
   - Rule: Della campaign heroes are banner-led, not split-screen SaaS layouts.
2. `pf-3195`: horizontal anchor/category strip.
   - Desktop shows 6 items.
   - Tablet shows 4 items.
   - Mobile shows 2 items.
   - Rule: use compact horizontal navigation for major paths.
3. `pf-829c`: visual subscription/lead-capture banner.
   - Separate desktop and mobile assets.
   - Rule: support conversions should be visual and compact, not long copy blocks.
4. `pf-6172`: image-left/content-right feature block.
   - Uses one large image, concise heading/copy/list, and underline CTA with arrow.
   - Rule: when adding explanatory content, pair it with a real visual.
5. `pf-26c3`, `pf-4726`, `pf-5f4a`, `pf-60a1`, `pf-aaba`: product merchandising sections.
   - Tabs are horizontal.
   - Product list slider shows 4 cards on desktop/laptop, 2 on tablet/mobile.
   - Product card sequence is image, badge, title, Loox rating, price, hidden coupon, CTA.
   - Rule: product areas should feel like collection merchandising, not editorial cards.
6. `pf-2915`, `pf-2b8c`: two-card visual guide/social sections.
   - Rule: secondary image blocks are clean, large, and low-copy.
7. `pf-3f4b`: FAQ accordion.
   - Split into two columns on desktop.
   - Rule: FAQ is near the bottom and compact.
8. `pf-1623`: trust badge slider.
   - Desktop/tablet show 4 items, mobile shows 2.
   - Actual trust copy includes financing, but this decision page must omit `0% APR`.

Confirmed reusable visual grammar:
- Hero: desktop ratio around `2.8`, separate mobile crop, image-first.
- Public Memorial Day page is closer to a finished graphic banner than to a component hero; topical pages should mimic the banner composition without copying promotion copy.
- For mini-split decision pages, hero imagery should be product-led where possible: product packshots or system imagery carry the first screen better than a generic room photo.
- Navigation strip: horizontal slider/grid, not oversized feature cards.
- Product section: centered heading, tabs, category visual/copy, product cards.
- Product grid density: 4 cards desktop, 2 cards mobile.
- Trust badges: light-blue cards, icon above/left, short text, slider/grid behavior.
- FAQ: accordion, late-page, concise.

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

## Local Demo Asset Rule

When the user asks to match the Memorial Day PageFly page, copy the useful PageFly assets into the local demo folder and reference the local files directly. Do not leave critical visuals dependent on Shopify CDN loading during review.

Current copied local placeholders:
- `banner desktop.webp`: topic-specific desktop hero image for the Single-Zone vs Multi-Zone page.
- `banner mobile.webp`: topic-specific mobile hero image for the Single-Zone vs Multi-Zone page.
- `memorial-category.png`: category/product lifestyle visual.
- `Spectral-Regular.woff2`, `Spectral-PageFly-Medium.woff2`, `Spectral-Bold.woff2`: PageFly heading and product-card display fonts.
- `Poppins-400.woff2` and `Poppins-600.woff2`: PageFly body, button, tab, and support-copy fonts.

Use Memorial Day assets only as layout placeholders. For final topic pages, replace campaign-specific holiday copy, dates, discount text, and sale badges with evergreen mini-split decision graphics or topic-specific Della product imagery.

Product cards should also use local copies of the PDP images in demo files so browser review does not show empty product-media boxes.

## Typography System

Use:
- Heading font: `Spectral Regular`, fallback `Georgia`, `serif`.
- Emphasized display/product price font: `Spectral Bold`, fallback `Georgia`, `serif`.
- Body/button/subheading font: `Poppins`, fallback `Arial`, `sans-serif`.
- Body: 16-17px desktop, 16px mobile, line-height 1.6.
- H1: 40-58px desktop, 34-44px mobile, `Spectral Regular`, line-height 1.08-1.12.
- H2: 25-36px desktop, 28-32px mobile, `Spectral Regular`.
- H3/category headings: `Spectral Regular`.
- Product titles: `Spectral Regular`; product prices and small badges can use `Spectral Bold`.
- Buttons, tabs, labels, body copy: `Poppins` 400 or 600.
- Label/eyebrow: 12px, uppercase, no added letter spacing.

Avoid:
- 70-90px oversized SaaS hero type.
- Roboto or generic Google-font defaults.
- Negative letter spacing.
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
--text-body: #0E1952;
--text-muted: #0E1952;
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
- Product merchandising follows PageFly density: 2 cards per row on mobile when titles and buttons still fit.
- Horizontal room selector can scroll, but touch targets must stay large.

Reference pattern:
- The Memorial page is visual-first and product-first.
- Topic pages should show the decision path above the product grid, but product cards must arrive early.

## Hero Rules For Topic Pages

Memorial uses a full campaign image. For non-promo topic pages:

Use:
- The approved scenario-page hero grammar: one full-width background image, foreground copy block, H1, one or two short sentences, and two CTAs.
- A wide ecommerce banner image with the Memorial Day desktop ratio (`2800x1000`, about `2.8:1`). Keep the left side clean for copy and place the product/room visual to the right.
- Topic-specific hero imagery. For comparison pages, the background should show the comparison concept visually, not only a generic lifestyle room.
- Memorial Day typography and button style: Spectral for the H1, Poppins for body/buttons, blue or navy commerce buttons, 4px radius, compact button height.
- A slim Della benefit strip above the hero when the page is used as an ad landing page.
- Room-count path selector directly below the hero.
- A hint of trust/shop content visible in the first viewport.

Avoid:
- Gradient overlays or decorative gradient backgrounds for this page's hero.
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
1. Della benefit strip.
2. Commerce banner hero with direct answer.
3. 1-5 room collection strip.
4. Quick answer decision band.
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
