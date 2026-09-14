# Next Chat Handoff: Ceiling Cassette vs Wall Mount Mini Split

## Current Page

- Local page file: `C:\Users\18041\Desktop\della-pages\Ceiling Cassette vs Wall Mount Mini Split\ceiling-cassette-vs-wall-mount-mini-split.html`
- Handoff file: `C:\Users\18041\Desktop\della-pages\Ceiling Cassette vs Wall Mount Mini Split\NEXT_CHAT_HANDOFF.md`
- GitHub Pages path: `https://cleopatrahines.github.io/della-pages/Ceiling%20Cassette%20vs%20Wall%20Mount%20Mini%20Split/ceiling-cassette-vs-wall-mount-mini-split.html`
- Shopify target path: `/pages/ceiling-cassette-vs-wall-mount-mini-split`

This page should stay a Della premium ecommerce decision landing page. It is both an SEO decision page and an advertising landing page, so the flow should balance explanation, quick decision support, and early product shopping.

Avoid turning the page into:

- a long SEO article
- a SaaS/dashboard UI
- an AI-looking component stack
- a generic collection grid
- a heavy checklist/manual page

## Hard Constraints

Do not change unless the user explicitly asks:

- SEO `<title>`: `Ceiling Cassette vs Wall Mount Mini Split: Which Is Right for You?`
- Meta description
- H1 text: `Ceiling Cassette vs Wall Mount Mini Split`
- Canonical
- FAQPage schema
- Existing collection URLs
- Existing product URLs
- Installer URL

Do not stage or commit unless the user explicitly asks. If staging is requested, stage only the files directly related to the current task. The repo has unrelated dirty/untracked files; do not revert, stage, or edit them unless requested.

Known separate worktree items may exist:

- `della-memorial-day-design-system.md`
- `page.pf-ef33e2e6.json.txt`
- `pf-ef33e2e6.liquid.txt`
- this handoff file may be modified because the user explicitly asked to update it

## Links To Preserve

Collections:

- `https://dellahome.com/collections/ceiling-cassette-mini-split`
- `https://dellahome.com/collections/wall-mounted-mini-split`

Installer:

- `https://dellahome.com/pages/find-a-installer`

Products:

- `https://dellahome.com/products/della-12-000-btu-seer2-22-ceiling-cassette-ductless-mini-split-ac-up-to-550-sq-ft`
- `https://dellahome.com/products/della-18-000-btu-seer2-20-5-ceiling-cassette-ductless-mini-split-ac-up-to-1000-sq-ft`
- `https://dellahome.com/products/18000-btu-dual-zone-ceiling-cassette-mini-split-ac-9k-12k-up-to-950-sq-ft`
- `https://dellahome.com/products/27000-btu-tri-zone-ceiling-cassette-mini-split-ac-9k-9k-9k-up-to-1200-sq-ft`
- `https://dellahome.com/products/vario-series-12000-btu-seer2-23-mini-split-heat-pump-ac-up-to-550-sq-ft`
- `https://dellahome.com/products/serena-series-18000-btu-seer2-22-mini-split-heat-pump-ac-up-to-1000-sq-ft`
- `https://dellahome.com/products/optima-series-18000-btu-dual-zone-mini-split-ac-9k-12k-up-to-950-sq-ft`
- `https://dellahome.com/products/vario-series-28000-btu-tri-zone-mini-split-ac-9k-9k-12k-up-to-1350-sq-ft`

## Current Section Order

1. `announcement-strip`
2. `hero`
3. `quick-answer`
4. Airflow & Visibility: `What changes after the indoor unit is installed?`
5. `#decision-checker`: `Find the better starting point for your room.`
6. `#comparison`: `What changes between ceiling cassette and wall mount?`
7. `#installation`: lightweight installer reminder inside the comparison section
8. `#products`: `Choose by project type, then compare popular picks`
9. `#rooms`: `Match the indoor unit to the space`
10. Services
11. FAQ
12. Bottom CTA

Important current decisions:

- There is no standalone Installation Feasibility section anymore.
- `#installation` is now an `<aside class="comparison-installer-note" id="installation">` below the comparison table.
- There is no standalone `Choose your collection path` section anymore.
- Collection links now live in the product module bottom fallback strip.
- The Mixed Indoor Units / `Can one home use both styles?` note has been deleted.
- Do not bring back the old hero commerce/path nav, old installation checklist table, mixed indoor units block, or large collection cards unless the user explicitly asks.

## Global Style Notes

- Brand direction: premium ecommerce landing page, Della-like, clean, practical, human.
- Brand colors in use: navy `#0E1953`, blue `#5884E7`, light blues `#EDF2FF` / `#DDF7FF`.
- Headings use Spectral / Georgia; body uses Poppins.
- A late global rule exists: `main.page h2 { font-size: 32px; ... }`.
- Be careful with section-specific `h2` selectors; ID specificity can override global `main.page h2`.
- Avoid `white-space: nowrap` as a layout fix.
- Keep letter spacing at `0` unless preserving existing micro-label styles.
- Avoid heavy shadows, large glows, glassmorphism, frosted overlays, yellow/beige cards, or large navy blocks unless the user specifically requests that visual direction.

## Completed Section Status

### Hero

- Simplified to background image, H1, short subcopy, and two CTAs.
- Removed hero quick verdict, chips, proof badges, floating cards, and path nav.
- Current subcopy: `Compare the cleaner ceiling look with the simpler wall placement before you choose your mini split.`

### Quick Answer

- Reworked into image + concise content split.
- Current H2: `Start with ceiling access or wall placement.`
- CTAs: `Check Ceiling Fit`, `Check Wall Fit`.
- Avoid adding back extra bullets or duplicate product cards here.

### Airflow & Visibility

- Uses polished inline SVG diagram cards.
- Keeps 3 bullets per card.
- Current H2: `What changes after the indoor unit is installed?`
- Subcopy: `The indoor unit style affects where air starts, how visible the system feels, and how routine access works.`

### Decision Checker

- Section ID: `#decision-checker`.
- Current H2: `Find the better starting point for your room.`
- Reworked into a guided selector with 5 question cards and a right-side result panel.
- Desktop right result panel is sticky and intentionally pushed down with `margin-top: clamp(150px, 12vw, 210px); top: 112px;`.
- Mobile result panel is static below the questions.
- The title should stay in the left question column; do not make it span full section width.
- Current JS is vanilla and should be preserved unless specifically requested.
- Keep safety note: `Installer confirmation is still required before purchase.`

### Head-to-head Comparison

- Section ID: `#comparison`.
- Current H2: `What changes between ceiling cassette and wall mount?`
- Current subcopy: `Both can heat and cool a room. The key differences are placement, airflow, access, and install complexity.`
- Table reduced to 6 rows:
  1. Installation location
  2. Airflow
  3. Room fit
  4. Install path
  5. Maintenance access
  6. Visual & cost path
- Left header label is `Compare`, not `Feature`.
- Desktop uses `.comparison-panel` + `.comparison-table`.
- Mobile uses stacked table rows, no horizontal scroll.
- Mobile default shows first 4 differences; rows 5-6 are hidden with `.is-collapsed-mobile`.
- Button `.comparison-toggle` toggles:
  - `View more differences`
  - `Show fewer differences`

### Installer Reminder

- Anchor ID: `#installation`.
- Current HTML is not a section; it is an aside under the comparison table:
  - `.comparison-installer-note`
  - `.comparison-installer-note__copy`
  - `.comparison-installer-note__actions`
- Current copy:
  - Label: `Installer note`
  - Text: `Before checkout, confirm sizing, drainage, line-set routing, electrical, and outdoor placement with your installer.`
- CTAs are text links, not buttons:
  - `Find Partner HVAC Installer`
  - `Review Products`
- Do not recreate a second installer table, checklist dashboard, or standalone installation section.

### Product Shopping Module

- Section ID: `#products`.
- Current class: `.project-products-section`.
- Current H2: `Choose by project type, then compare popular picks`
- This module now appears immediately after the comparison/installer note.
- Structure:
  - `.project-product-tabs`
  - `.project-product-feature`
  - `.project-product-grid`
  - `.product-collection-fallback`
- Product cards use `.project-product-card`.
- Product module is tabbed by project type:
  - `Open living room`
  - `Bedroom or office`
  - `Garage or rental`
  - `Remodel or finished ceiling`
- Tabs update feature banner copy and the active 4-product set using scoped vanilla JS.
- Do not show more than 4 product cards in one active set.
- Product cards currently show image, title, tags, price, and Add to Cart.
- The rating/review row was removed after the user pointed at it and asked to remove it. Do not re-add ratings unless the user explicitly asks.
- Product images use the Della CDN URLs supplied by the user. Do not replace with fake or remote search images.
- Add to Cart uses verified Shopify variant IDs in JS. Preserve them.

Current product data in JS:

- `cc12`: 12K ceiling cassette, `$1,394.96`, variant `50962261868832`
- `cc18`: 18K ceiling cassette, `$1,784.96`, variant `50962170511648`
- `ccDual`: dual-zone ceiling cassette, `$2,769.96`, variant `50602499801376`
- `ccTri`: tri-zone ceiling cassette, `$3,779.96`, variant `50602500292896`
- `wm12`: 12K wall mount, `$799.96`, variant `50314672013600`
- `wm18`: 18K wall mount, `$1,049.96`, variant `50340329029920`
- `wmDual`: dual-zone wall mount, `$2,039.96`, variant `50589452206368`
- `wmTri`: tri-zone wall mount, `$2,484.96`, variant `50576037576992`

Current tab product sets:

- `living`: `cc12`, `wm12`, `cc18`, `wm18`
- `bedroom`: `wm12`, `wm18`, `cc12`, `cc18`
- `garage`: `wm12`, `wm18`, `wmDual`, `wmTri`
- `remodel`: `cc12`, `cc18`, `ccDual`, `ccTri`

### Product Collection Fallback

- The old `Choose your collection path` large card section has been removed.
- Current fallback is inside `#products`, below `.project-product-grid`.
- HTML class:
  - `.product-collection-fallback`
  - `.product-collection-fallback__links`
- Copy:
  - `Not ready to pick a model?`
  - `Browse Ceiling Cassette collection`
  - `Browse Wall Mount collection`
- CTA style: text links, not large buttons.
- Mobile: fallback links stack to one column with 40px min-height.

### Choose by Room

- Section ID: `#rooms`.
- Current H2: `Match the indoor unit to the space`.
- This section now appears after the product shopping module.
- It should feel like supplemental guidance for users who still need more room-type context, not a primary conversion module.
- Current subcopy: `Use these common room types as starting points. Final fit still depends on ceiling access, wall placement, BTU sizing, and installer review.`
- Layout is 2 featured cards + 3 supporting cards.
- Featured cards are image-on-top, text-below. Do not reintroduce frosted overlay or text over image.
- Supporting cards do not have deep-blue primary buttons.
- Current section has reduced top padding after being moved below products.

### Services, FAQ, Bottom CTA

- Services remains after rooms.
- FAQ remains after services.
- FAQ schema remains unchanged and must be preserved.
- Bottom CTA remains last.

## Current Important CSS Classes

Comparison:

- `.comparison-section`
- `.comparison-panel`
- `.comparison-table`
- `.comparison-table__label`
- `.comparison-table__sub`
- `.comparison-installer-note`
- `.comparison-installer-note__copy`
- `.comparison-installer-note__actions`
- `.comparison-toggle`
- `.is-collapsed-mobile`

Products:

- `.project-products-section`
- `.project-products__head`
- `.project-product-tabs`
- `.project-product-tab`
- `.project-product-feature`
- `.project-product-feature__media`
- `.project-product-feature__content`
- `.project-product-grid`
- `.project-product-card`
- `.project-product-card__image`
- `.project-product-card__title`
- `.project-product-card__meta`
- `.project-product-card__price`
- `.product-collection-fallback`
- `.product-collection-fallback__links`

Rooms:

- `#rooms`
- `.room-grid`
- `.room-card`
- `.room-card.is-large`
- `.room-card__media`
- `.room-card__body`
- `.room-tag`
- `.room-actions`

Do not resurrect these removed structures unless explicitly requested:

- `.installer-precheck-section`
- `.install-scenarios-section`
- `.install-callout-section`
- `.installer-handbook-module`
- `.installer-guide-panel`
- `.collection-paths`
- `.collection-card`
- `.mixed-units-note-section`
- `.mixed-units-note`

## Validation Already Done

Recent checks were done in Chrome/local file:

- `1440px`
- `768px`
- `430px`
- `390px`
- `375px`

Confirmed:

- Current module order is Airflow -> Decision Checker -> Comparison -> Product Shopping -> Rooms -> Services -> FAQ.
- Product module appears immediately after comparison.
- Product module defaults to 4 product cards.
- Product tabs are present and product card switching works.
- Product collection fallback appears below the product grid.
- Old collection large cards are gone.
- Mixed Indoor Units note is gone.
- Standalone Installation Feasibility section is gone.
- `#installation` anchor exists once on the comparison installer note.
- No horizontal overflow at checked mobile widths.
- Fallback collection links stack correctly on mobile.
- Console had no errors during latest browser check.
- `git diff --check` passed for the HTML file except the existing LF/CRLF warning.
- SEO title, meta description, canonical, H1, and FAQPage schema were spot-checked as still present.

## How To Work In Next Chat

1. Read this handoff first.
2. Read the current HTML before editing.
3. Only edit the section the user names.
4. Do not add new sections unless explicitly asked.
5. Do not change protected SEO/schema/URL fields.
6. For product cards, do not invent fake prices, reviews, ratings, SKUs, or variant IDs.
7. After each edit, report:
   - which HTML section changed
   - which CSS classes changed
   - which breakpoints were verified
8. Use browser checks for frontend polish, especially `375`, `390`, `430`, `768`, `1440`.

## Suggested Next-Chat Prompt

```text
请先读取并遵守这个交接文档：

C:\Users\18041\Desktop\della-pages\Ceiling Cassette vs Wall Mount Mini Split\NEXT_CHAT_HANDOFF.md

我要继续优化 Della 的 Ceiling Cassette vs Wall Mount Mini Split 落地页。当前页面文件是：

C:\Users\18041\Desktop\della-pages\Ceiling Cassette vs Wall Mount Mini Split\ceiling-cassette-vs-wall-mount-mini-split.html

重要限制：
1. 不要修改 SEO title。
2. 不要修改 meta description。
3. 不要修改 H1 文案。
4. 不要修改 canonical。
5. 不要修改 FAQPage schema。
6. 不要修改现有 collection URL、product URL、installer URL。
7. 不要新增模块，除非我明确要求。
8. 不要引入外部库。
9. 不要提交无关文件；仓库里可能有未提交文件，不要碰。
10. 每次只改我指定的 section，完成后说明修改了哪些 HTML section、哪些 CSS class、验证了哪些断点。

页面方向：
- 保持 Della 品牌系统：navy #0E1953、blue #5884E7、light blue #EDF2FF / #DDF7FF、Spectral heading、Poppins body。
- 视觉参考 Della coupon-code / Memorial Day 页面和 single-zone-vs-multi-zone-mini-split.html，但不要照搬文案。
- 目标是 premium ecommerce decision landing page，不是 SEO 文章页，也不是 AI 组件模板。
- 页面既服务 SEO 决策用户，也服务广告落地页用户，所以产品购买模块要保持靠前、清楚、可转化。
- 移动端重点检查 375px、390px、430px、768px、1440px。

当前页面关键状态：
- 模块顺序已经调整为：Airflow / Decision Checker / Comparison / Products / Rooms / Services / FAQ。
- #installation 已经不是独立 section，而是 comparison table 下方的轻量 installer note。
- #products 是 tabs + feature banner + 4 张产品卡 + collection fallback。
- 独立 Choose your collection path 大卡片已经删除，collection links 只保留在产品区底部 fallback。
- Mixed Indoor Units / Can one home use both styles? 板块已经删除。
- 产品卡当前展示 image / title / tags / price / Add to Cart；rating/review 行已按用户要求移除，不要擅自加回。

接下来我会告诉你具体要优化哪个 section；请先读当前 HTML，再按我指定范围局部修改。
```

## Product-card reuse — 2026-09-14

Owner authorized continuing the single-page rollout. Current implementation preserves eight products, their original PDP and Add to Cart variant IDs, the four project sets, checker logic, hero, comparison, room scenes, services and FAQ. Cards display installation style, short series/title, capacity or indoor combination, separate outdoor capacity, voltage, efficiency, coverage, full-name disclosure and the selected variant price. Two single-zone cassette cart variants have no line set; cards label that configuration and link to the original PDP for line-set selection. Vario 12K price is updated to the verified $779.96. Source evidence: commerce-product-data.json.

Desktop uses four columns from 1200px, medium screens two, and mobile through 780px one card with full-width specifications, disclosure and purchase. Static default cards and dynamic project renders match. Arrow keys/Home/End operate the project tabs. Local Chrome verification: 56/56 checks across four groups at 1440/1280/1199/1024/800/780/430/390/360px, product text at 200% on 390/1024px, model disclosure, original checker, comparison toggle, no-JS initial cards, images, metadata/schema preservation and script errors. Cart destinations were inspected without adding items.

Evidence and backup: C:/Users/18041/Documents/Playground/della-ui-review-20260911/cassette-wall-pilot-20260914/. Prices are dated snapshots; shared hydration and Shopify-theme integration remain separate. Local review is ready; this revision has not been committed or pushed. Next action: visual review and explicit publication instruction, then the next single page.