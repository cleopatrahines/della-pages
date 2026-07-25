# Next Chat Prompt: 2-Zone vs 3-Zone Mini Split Landing Page

你接下来继续这个 Della 页面项目。请先使用 `della-page-builder` skill，并阅读项目里的：

- `C:\Users\18041\Desktop\della-pages\2-zone-vs-3-zone-mini-split\HANDOFF.md`
- `C:\Users\18041\Desktop\della-pages\2-zone-vs-3-zone-mini-split\PRD.md`
- `C:\Users\18041\Desktop\della-pages\2-zone-vs-3-zone-mini-split\DESIGN.md`
- `C:\Users\18041\Desktop\della-pages\2-zone-vs-3-zone-mini-split\PLAN.md`
- `C:\Users\18041\Desktop\della-pages\2-zone-vs-3-zone-mini-split\implementation-notes.md`

不要从头重做，在现有版本上继续微调。保持简洁中文沟通。不要 commit、push、建分支，除非用户明确批准。

项目路径：

`C:\Users\18041\Desktop\della-pages\2-zone-vs-3-zone-mini-split`

主文件：

`C:\Users\18041\Desktop\della-pages\2-zone-vs-3-zone-mini-split\2-zone-vs-3-zone-mini-split.html`

## 当前页面定位

这是 Della 的 `2-Zone vs 3-Zone Mini Split` 研究型决策页 + 商品导购页，不是博客页，也不是直接复制 collection 页。目标是帮用户判断 2-zone 还是 3-zone 更适合，再导向对应集合或产品。

## 当前关键状态

- Hero 使用 `banner.webp` 作为背景图。
- Hero 右侧旧产品图已删除。
- Hero 文案已缩短：`Two bedrooms, bedroom + office, upstairs rooms, or an addition? Match the right zone count to each space.`
- Hero 两个按钮都是 `btn btn-navy` 样式。
- 早期 room-count path strip 已删除。
- 所有 H2 使用 32px Spectral / Georgia，颜色 `#0E1953`。
- `Choose 2-Zone or 3-Zone by Room Count` 的两个卡片按钮已水平对齐。
- `Shop Della 2-Zone and 3-Zone Mini Splits` 的 feature 图使用本地：
  - `2-Zone.webp`
  - `3-Zone.webp`
- 产品 tabs 分为 `2-Zone Systems` 和 `3-Zone Systems`，不能混产品。
- 产品卡只用已确认真实产品，按钮是 `View Product`，不能用 `Add To Cart`。
- 产品价格是 2026-06-24 从 Shopify JSON 抓取的静态价格；上线前需要刷新或改成 Shopify 动态价格。
- Premium Della Services 直接照搬 12K vs 18K 参考页服务块：Free & Fast Shipping / Pay in 6 Months, 0% APR / 24×7 Live Chat Support / Lifetime Coverage (Mini Splits)。这是用户最新明确要求，覆盖之前“不放 0% APR”的旧限制。
- FAQ 文案严格 5 个问题；FAQ 样式参考 12K vs 18K 页面 `Before you choose 12K or 18K` 区块。
- Bottom CTA `Ready to Choose Your Zone Count?` 参考 12K vs 18K 页面 `Start with the collection that matches your room`：浅蓝背景、两张白色文字卡、不要图片、不要 `More than three rooms? View all multi-zone systems`，按钮 hover 保持 `btn btn-navy`。

## 最新产品图处理状态

用户刚重点要求处理产品卡图片背景：前几张源图自带灰色方块，最后一张 ceiling cassette 图片四角为白色，所以看起来更融合。

当前已处理完成：

- HTML 产品卡图片引用已切到：`assets/product-blended-01.webp` 到 `assets/product-blended-08.webp`。
- 这些图是从本地原图生成的，只替换“四周连通的源图背景”为卡片浅蓝，不动机器本体。
- 保留 `assets/product-original-01.webp` 到 `assets/product-original-08.webp` 作为来源备份。
- 已删除早期试做的 `product-integrated-*.webp` 和 `product-integrated2-*.webp`。
- `.product-media` 当前应保持：`height: 262px`、`padding: 18px`、背景 `var(--product-surface)`。
- `.product-media img` 当前应保持：`object-fit: contain`、`mix-blend-mode: normal`。
- 不要再改回 `mix-blend-mode: multiply`，也不要用遮罩/覆盖层处理产品图；之前会导致方块变暗或机器被盖住。

最新浏览器检查：

- Desktop 1600px：2-Zone 产品卡视觉确认，灰色方块不再明显，机器没有被遮挡。
- Desktop 1600px：3-Zone 产品卡视觉确认，包括 ceiling cassette 卡，背景基本一致。
- Mobile 390px：无横向溢出。

## 重要参考页

`C:\Users\18041\Desktop\della-pages\12000 BTU vs 18000 BTU Mini Split\12000-btu-vs-18000-btu-mini-split.html`

这个参考页用于：

- Premium Della Services block。
- FAQ 样式。
- Bottom CTA 样式。
- 产品卡图片区节奏：浅蓝 media、262px 高度、18px padding、contain 展示。

## 已知风险 / 未决事项

- 产品价格是静态快照，上线前需要刷新或接 Shopify 动态价格。
- 最终 Shopify URL 未确认，所以还没加 canonical。
- 最终部署方式未确认：PageFly 还是 Shopify custom liquid。
- 当前是 standalone HTML demo，不包含完整 Shopify header/footer。
- 不要 commit/push/建分支，除非用户明确批准。

## 下一轮建议工作方式

1. 按用户的新截图或新要求继续微调现有 HTML/CSS。
2. 不要重做页面，不要替换已确认产品数据。
3. 如涉及页面结构、文案策略、产品数据、图片处理方式，更新 `HANDOFF.md` 和必要的项目记录。
4. 修改后用浏览器至少检查 1280 或 1600 桌面、430、390 移动端；重点看无横向溢出、按钮对齐、产品图不被裁切/遮挡。
5. 最终只做简洁中文汇报：改了什么、检查了什么、是否还有风险。
