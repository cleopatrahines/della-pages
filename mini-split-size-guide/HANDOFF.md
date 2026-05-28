# Mini Split Size Guide - Next Chat Handoff

Last updated: 2026-05-28

## Project Location

- Project folder: `C:\Users\18041\Desktop\della-pages\mini-split-size-guide`
- Main HTML: `C:\Users\18041\Desktop\della-pages\mini-split-size-guide\mini-split-size-guide.html`
- Source documents:
  - `PRD.md`
  - `DESIGN.md`
  - `PLAN.md`
  - `ui设计图.png`

## Current Status

The Mini Split Size Guide static landing page has been created and iterated. It should not be restarted from scratch.

The page is intended to be a Della BTU decision landing page, not a blog article and not a hard-selling collection page. Its primary job is to help users choose a starting BTU tier, then route them naturally into Della BTU collections.

Current file state:

- `mini-split-size-guide.html` exists and includes inline CSS/JS.
- Local font files are present and referenced.
- Local placeholder/lifestyle images from the single-zone vs multi-zone page are present and used.
- Product cards use real Della product URLs and product images from the PRD.
- Product prices were captured as page data, with the snapshot note kept internal rather than visible in the page copy.
- Product CTA remains `View Product`; no `Add To Cart`.
- FAQ is limited to 6 questions and includes FAQ JSON-LD.
- Product tabs default to 12K and include keyboard support.
- 36K tab uses 1 real product card plus a sizing/installer note.
- The page has not been committed or pushed.

## Source Of Truth Priority

Use this priority order:

1. `PRD.md` controls scope, content, BTU ranges, product data, CTA rules, SEO, and non-goals.
2. `DESIGN.md` explains how to interpret `ui设计图.png` visually.
3. `PLAN.md` gives implementation and QA steps.
4. `ui设计图.png` is only a visual/layout reference. It is not a source for product names, prices, BTU ranges, or policies.

Do not copy AI mockup data if it conflicts with the PRD.

## Hard Rules That Must Stay

- Use Della collection-aligned BTU ranges:
  - 9K: up to about 400 sq ft
  - 12K: 401-550 sq ft
  - 18K: 551-1,000 sq ft
  - 24K: 1,001-1,500 sq ft
  - 36K: 1,501-2,500 sq ft
- Do not use broader placeholder ranges like `250-450` or `450-650`.
- Do not add an interactive BTU calculator.
- Do not expand into a full multi-zone / whole-home sizing guide.
- Keep only one light cross-link to the single-zone vs multi-zone guide.
- Do not use sale badges, coupon language, countdowns, discount percentage labels, or `Add To Cart`.
- PDP product card CTA: `View Product`.
- Collection path CTA: `Shop 9K`, `Shop 12K`, `Shop 18K`, `Shop 24K`, `Shop 36K`.
- Product prices may show only if captured reliably; do not invent prices.
- 36K must stay lower-weight than 9K/12K/18K/24K and must not be padded with fake products.

## Important Recent Fix

The `Choose by How the Room Is Used` / Room Match section was just corrected after the user compared it against the design mockup.

Current Room Match direction:

- Desktop layout is a 5-column, 2-row bento grid.
- First row:
  - `Open Living Room` large card spanning 2 columns
  - `Bedroom / Office` small card
  - `Studio` small card
  - `Garage / Shed` small card
- Second row:
  - `Large Open Area` large card spanning 3 columns
  - `Sunroom / Attic` large card spanning 2 columns
- Mobile layout remains single column.
- Mobile title was adjusted so it no longer clips at 390px.

Static checks after this fix:

- Room cards: 6
- Five-column desktop Room Match grid exists
- Mobile Room Match H2 fix exists
- `Add To Cart`: not present
- Wrong AI range `250-450`: not present

## Known Visual / QA Focus For Next Chat

Do not redo the page. Continue polishing from the current HTML.

Priority checks:

- Compare the current page against `ui设计图.png`.
- Inspect the full page at desktop 1440px, tablet 768px, and mobile 390px.
- Confirm the Room Match bento grid now feels close enough to the design.
- Continue improving overall Della Shopify landing-page maturity if needed:
  - Hero visual balance
  - BTU selector density
  - sizing table polish
  - product tabs merchandising feel
  - installer/support visual
  - mobile spacing and no horizontal overflow
- If using browser screenshots, keep temporary screenshots/files under `C:\Users\18041\Documents\Playground` and delete them before finishing.

## Git / Workspace Notes

The repo currently has unrelated or pre-existing changes outside this project. Do not stage, revert, or modify them unless explicitly asked.

Known unrelated/pre-existing items from the last status check:

- Modified: `Ceiling Cassette vs Wall Mount Mini Split/ceiling-cassette-vs-wall-mount-mini-split.html`
- Modified: `della-memorial-day-design-system.md`
- Untracked: `Ceiling Cassette vs Wall Mount Mini Split/NEXT_CHAT_HANDOFF.md`
- Untracked: `page.pf-ef33e2e6.json.txt`
- Untracked: `pf-ef33e2e6.liquid.txt`
- Untracked/current project folder: `mini-split-size-guide/`

Do not commit or push until the user explicitly approves after QA.

## Suggested Next Chat Prompt

```text
继续做 C:\Users\18041\Desktop\della-pages\mini-split-size-guide 这个项目。

请先读取：
- C:\Users\18041\Desktop\della-pages\mini-split-size-guide\HANDOFF.md
- C:\Users\18041\Desktop\della-pages\mini-split-size-guide\PRD.md
- C:\Users\18041\Desktop\della-pages\mini-split-size-guide\DESIGN.md
- C:\Users\18041\Desktop\della-pages\mini-split-size-guide\PLAN.md
- C:\Users\18041\Desktop\della-pages\mini-split-size-guide\ui设计图.png
- C:\Users\18041\Desktop\della-pages\mini-split-size-guide\mini-split-size-guide.html

不要从头重做。当前 HTML 已经存在，主要继续做视觉精修和 QA。

注意：
1. PRD.md 是内容、BTU 范围、产品数据、CTA、SEO、non-goals 的最高优先级。
2. DESIGN.md 和 ui设计图.png 只作为视觉方向参考。
3. 不要照抄设计图里的错误 BTU 范围、AI 产品名、AI 产品图、价格或政策文案。
4. 保持 Della collection-aligned ranges：
   - 9K: up to about 400 sq ft
   - 12K: 401-550 sq ft
   - 18K: 551-1,000 sq ft
   - 24K: 1,001-1,500 sq ft
   - 36K: 1,501-2,500 sq ft
5. 不要 interactive BTU calculator。
6. 不要 Add To Cart、coupon、sale badge、countdown、discount percent。
7. 36K tab 只能是 1 个真实产品卡 + sizing/installer note。
8. 不要 commit / push，除非我明确批准。

上一轮刚修过 Room Match：
- desktop 已改成 5-column / 2-row bento grid
- 第一行：Open Living Room 大卡 + Bedroom/Office + Studio + Garage/Shed
- 第二行：Large Open Area 大卡 + Sunroom/Attic 大卡
- mobile 是单列，390px 标题不应再截断

下一步请先用浏览器/截图检查当前页面：
- desktop 1440px
- tablet 768px
- mobile 390px

重点看：
- Room Match 是否已经接近设计稿
- Hero 是否像 Della 正式 landing page
- Product tabs 是否像真实 Shopify merchandising
- 390px mobile 是否不挤、不横向溢出
- 图片/图标是否还有明显占位感

检查后如果需要小修，直接增量修改 mini-split-size-guide.html，不要推倒重写。完成后报告改了什么、验证了什么、还有什么未验证。
```
