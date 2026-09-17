# Mini Split vs Window AC vs Portable AC — PRD

版本：2026-09-17 产品透明素材与排版精修版。用户已授权 Codex 研究、规划、制图和审核，OpenCode / DeepSeek 编码。当前交付为本地独立 HTML 审核版；发布需另行授权。

项目：`C:\Users\18041\Desktop\della-pages\Mini Split vs Window AC vs Portable AC`
入口：`mini-split-vs-window-ac-vs-portable-ac.html`
语言：US English。页面类型：比较选购专题，服务研究型自然流量和广告。

## 目标与结构

帮助用户基于安装条件、使用方式与初始投入选择房间空调类别，再查看对应 DELLA 商品。单房间/独立空间是主要范围，多房间问题留在相关问答内。

1. Hero：H1 和一句短说明。画面完整展示用户指定设备。
2. 视觉比较：三列产品图、类别名和一句适用方向，仅 Setup / Upfront 两组简短差异，每列有对应商品入口。
3. 商品：三 Tab，4/4/3 精选商品。Portable 桌面三卡均分整行。
4. 解释：安装图 + 四个默认收起的问题，展开后解释安装、噪音、参数口径与成本。
5. 服务：直接复用 Ductless Mini Split vs Central Air 的 Premium Della Services。
6. FAQ：Whole House 的宽幅单列样式，四问、默认全收起；最后为 Whole House 浅蓝横幅式三类购物入口。

## 内容层级

Hero 不再有三个小商品入口。各节清理重复 section intro、fit-check 条、coverage 页脚、图片 caption、accordion 关闭态第二行摘要、收尾辅助段落。

规格数值、SACC/ASHRAE、型号、电压与 Up to 保留为商品事实。租房许可、负荷、排风、能效和采暖条件放入默认折叠正文，不在模块外堆提示条。全部 details，包括完整型号、解释项和 FAQ，初始均关闭。

## 组件来源

| 部位 | 当前采用来源 |
|---|---|
| Hero | 当前本地桌面/移动素材；删 HTML 小入口 |
| 下方全部容器 | Whole House：max-width 1360px；桌面 padding 24px；手机 16px |
| 比较 | Dreame 的大图、对齐和留白；本页三类别、两条差异 |
| 商品卡 | Whole House：直角、大图、短系列名、容量副行、实线规格、完整型号、价格、navy 按钮 |
| Services | Central Air：左标题、浅蓝居中卡、蓝圆白图标、链接标题及源组件正文 |
| FAQ | Whole House：全宽、Spectral 问题、细线、chevron、原生 details |
| 收尾 | Whole House 浅蓝横幅，左标题右三个同等级按钮 |

精确规则由 DESIGN.md / LOCKED-COPY.md / products.json 控制；本轮素材与排版细节见 LAYOUT-REFINEMENT.md，FAQ 取舍见 FAQ-DECISION-REVIEW.md。布局图为 `design/final-mockup-v6.png`，Portable 面板为 `design/portable-panel-v6.png`。

## 商品、路由与状态

维持 products.json 的 4 款 Mini Split、4 款 Window、3 款 Portable。研究快照日期保留，实施完成前复核价格和可购买状态。

- Mini Split：`https://dellahome.com/collections/mini-split-single-zone`
- Window：`https://dellahome.com/collections/window-ac`
- Portable：`https://dellahome.com/collections/portable-ac`
- 多房间辅助链接进入相关 FAQ：`https://dellahome.com/pages/single-zone-vs-multi-zone`

比较动作激活商品 Tab，并滚动到商品标题/Tab 可见的位置。直接 Tab 选择同步 URL，保持滚动位置。初始锚点、hashchange、Back/Forward 正确恢复；历史恢复不重复埋点，不冒充新的主动选择。

## 技术与验收

比较区和全部 11 商品使用 assets/products-cutout 的透明 PNG 衍生素材，原 JPG 保留。用户已批准程序化精确抠图：只改透明度和外围留白，保留机身、Logo 与配件原始 RGB。所有 H2 使用 Della AC Spectral 32px / 500 / 1.15 / #0E1953，各断点一致。比较图区桌面约 280px 高；Evidence 标题下间隔桌面 32px、手机 24px，左右图文垂直居中。

作用域 HTML/CSS/JS、本地字体和图片、真实 DOM、无框架。Spectral 标题/系列名/问题，Poppins 正文与控件；navy 激活态和商品按钮、品牌蓝点缀。

手机 Hero 初始按 4:3 占位；所有机器不被裁切或标签遮挡。手机比较列局部横滑，左右控制可发现，后一个栏目可见一部分；无 JS 可原生滚动。展开正文一直在 DOM。

Title/description 按锁定文案。最终 Shopify URL 未提供，不填假 canonical；不默认加入 FAQPage 或虚构评级。正式 Shopify 商品事实由 Liquid/批准的数据机制承担，当前不编辑线上主题。

1440/1280/1024/768/430/390/360：核对宽度、无遮挡、4/4/3、全部初始折叠、型号价格、URL 状态、无 JS、键盘、reduced motion、图片占位和无页面横溢。

## 已解决的最新决定

2026-09-17：按用户框选删除 Hero 小入口及外部说明小字，重做比较层级；宽度/商品卡/FAQ 对标 Whole House；Portable 桌面三等分；服务改为 Central Air 来源；收尾采用 Whole House；全部折叠项默认关闭。

用户最新指定的 Central Air 服务组件断点优先于上一轮两列建议：<=820px 两列，<=560px 一列，本轮照此复制；外容器仍用 Whole House 宽度。旧审核中的 URL/埋点、图片比例、无遮挡要求继续有效；六行表、首项默认展开等由本轮规则替代。
