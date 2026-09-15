# Mini Split for Whole House — PRD

版本：六章节方案与商品定稿，2026-09-15。
阶段：用户已接受最新桌面长图作为实施视觉参考，授权转入实现；按本文覆盖项修正图稿偏差。HTML 尚未实施。
项目路径：`C:\Users\18041\Desktop\della-pages\Mini Split for Whole House`。
最终 HTML 文件名：`mini-split-for-whole-house.html`。
研究依据：同目录 `RESEARCH-REVIEW.md`。商品依据：`PRODUCTS.md` 与 `products.json`。批准视觉参考：`design/approved-desktop-reference.png`。实施规格：`DESIGN.md`、`PLAN.md`。`GEMINI_DESIGN_PROMPT.md` 为已有文案来源，若与本PRD或DESIGN的明确覆盖项冲突，以当前实施规格为准。

## 实施确认与图稿覆盖项

用户确认按当前返图进入代码实现，本轮无需再次生成整页、局部或手机设计图。

- Hero 只保留标题、说明与CTA；页面内容区域不另放DELLA logo。Shopify全站页头由现有主题提供。
- What Your Home Needs 与其他主体模块共用居中内容容器，图片完整约束在左列内，按固定比例裁切，文字与图片顶对齐。图稿中该图贴左边界的出血效果不作为实现目标。
- Hero下方采用四项产品价值短条：Room-by-Room Control、Heating & Cooling、Indoor Style Options、2–6 Zone Options；不采用泛化节能或全年性能保证。
- Hero副文案使用本文条件式直接回答，恢复本页“能否用于整屋”的搜索答案，不使用图稿里perfect climate等泛化保证。
- 剖面图保留住宅与标注布局。房间标注须落到正确空间；原图房间家具不清晰时标签用Closed rooms，说明仍解释关门空间的送风需求，不指着客厅称为卧室。图下恢复一套Multi-Zone与多个系统的对应说明，不能用两个室外机图片代表室内机形式。
- 九款商品与价格以products.json为准，卡片直接使用assets/products原图；特别是P3为Optima 5-Zone，不能复制图稿误写的3-Zone。恢复价格基础说明、同步需求提醒与View All Multi-Zone Systems入口。
- What Your Home Needs右侧四项采用2×2或更宽松的纵列，按实际可读性响应式调整；图片不得覆盖文字、超出容器或制造页面横向滚动。
- Plan the Full Project按最新图稿的“顶部标题、左图右侧三项说明”结构实施，具体文案及CTA以本节05为准。
- FAQ使用本文原六问及GEMINI_DESIGN_PROMPT.md中对应答案，不复制图稿替换后的泛化FAQ。底部为Find Your Multi-Zone System。
- 图稿仅作为布局与气质参考，生成的文字、设备参数、标识、安装关系不作为事实依据。

## 1. 页面目的

页面类型：Use-case landing page，以整屋研究决策为核心，承担 Multi-Zone collection 的商业导流。
目标市场：美国住宅业主；页面使用自然美式英语。
主要需求：研究 mini split 能否用于整屋供暖制冷、理解整屋需要怎样的覆盖、查看相关 DELLA 系统并推进安装前确认。

页面完成四个可观察结果：

1. 用户理解经过正确设计的 mini split 系统可以服务整屋，结果取决于空间覆盖、负荷和设备选择。
2. 用户能区分开放生活区、关门房间、不同楼层的规划需求。
3. 用户能直接进入 DELLA Multi-Zone 总集合或 2–6 Zone 路径。
4. 用户知道设备价格之外应规划什么，并能找到房间估算工具与安装商入口。

## 2. 核心叙事

先看见住宅里的舒适生活，再理解系统如何服务各空间，然后看商品与项目推进方式。
消费者记住的一句话：Whole-home comfort starts with a plan for every space.

布局以六个主要视觉章节组织。产品价值说明为首章下的短条；最终行动为 FAQ 后的紧凑收尾。章节数量只是组织方式，不是流量或转化指标。

## 3. 内容边界

| 页面 | 负责的核心问题 |
|---|---|
| Whole House | 整屋项目是否值得推进；各空间如何得到覆盖；完整项目需确认什么 |
| Single-Zone vs Multi-Zone | 系统数量与独立性；房间数/系列/形式/电压筛选 |
| Sizing Calculator | 单个空间的规划估算 |
| Multi-Zone collection / PDP | 具体产品浏览、规格及购买 |
| 安装商与设备资料 | 房间负荷、设计条件设备能力、兼容组合及安装可行性 |

允许简短重复用户完成当前判断所必需的知识。内容的主问题、深度和行动应清楚区分。Whole House 保留一套或多套系统的简短示意及权衡，但不以完整对比或新的推荐工具组织页面。

## 4. 行动与链接

主要商业动作：Shop Multi-Zone Systems。
Hero 次级动作：See How It Works，页内锚点至整屋视觉。
商品卡：View Product。
全页主要商业按钮保持相同含义。

| 用途 | URL |
|---|---|
| 主集合 | https://dellahome.com/collections/mini-split-multi-zone |
| 2 Zone | https://dellahome.com/collections/2-zone-mini-split |
| 3 Zone | https://dellahome.com/collections/3-zone-mini-split |
| 4 Zone | https://dellahome.com/collections/4-zone-mini-split |
| 5 Zone | https://dellahome.com/collections/5-zone-mini-split |
| 6 Zone | https://dellahome.com/collections/6-zone-mini-split |
| 房间估算 | https://dellahome.com/pages/mini-split-sizing-calculator |
| 系统比较 | https://dellahome.com/pages/single-zone-vs-multi-zone |
| 安装商入口 | https://dellahome.com/pages/find-a-installer |
| 已有风管的商品替代入口 | https://dellahome.com/collections/central-air-conditioner |

实施时验证链接状态。页内锚点当前页移动；外链沿用项目 skill 的新标签页规则并加 noopener。最终 Shopify 站内导航行为在实施计划中统一。

## 5. 六个视觉章节

### 01 — Whole-home comfort，直接回答与生活横幅

H1 草案：Mini Splits for Whole-House Comfort。
副文案草案：Yes. Mini splits can heat and cool a whole house when the equipment and layout match its rooms and climate. Explore DELLA multi-zone options and see what your project needs.

一个宽幅真实感住宅视觉：可感知客厅与相邻空间的关系，设备自然出现。文字区域保持干净，文字为 HTML。视觉呈现生活结果与真实产品存在感。
正文与主次 CTA 尽量完整出现在典型手机首屏或首屏紧邻位置，包含 Shopify 自带页头后的真实高度需验证。

紧随Hero的短条为四项简明产品价值，桌面四列、平板/手机两列。已有风管的比较提醒放入What Your Home Needs，并链接至已核实的Central Air集合。

Hero 与情境短条不加独立商品网格。可配置紧凑页内导航：How It Works / Systems / Project Planning；手机优先保证主 CTA 可达而不是增加多层固定栏。

### 02 — A Plan for Every Space，整屋核心视觉

本模块的首要任务是解释整屋覆盖。

一张住宅剖面底图配三处可读标注：

- Open living areas：相连空间需要结合负荷、布局和送风确认覆盖。
- Closed bedrooms：关门房间要有明确的供暖制冷分配方式。
- Different floors：各层条件和管路位置会影响分区与系统安排。

固定显示三条简短解释，用户无需点击即可得到主要知识。点击编号可增加局部高亮或展开补充信息，不输出个性化型号建议。

图示验收：

- 画面只表达空间关系和规划原则；图注为 Illustrative layout. Equipment and installation plans vary by home.
- 房间名、编号和标注线由 HTML/SVG 绘制，底图不含不可编辑文字。
- 住宅完整性优先；对卫生间、走廊等辅助空间可以合并说明：Other spaces also need a planned heating and cooling approach.
- 不用气流箭头穿墙表示覆盖，不靠开门暗示关门房间仍必然舒适，不显示未经验证的温度或均匀覆盖热力图。
- 如标注冷媒线，应明确它不是风管或气流；没有型号和工程验证时不绘制具体施工管线。
- 不将某个房屋面积、房间总数与一个具体套装绑定为推荐。

系统安排为图下紧凑补充：一套 Multi-Zone 可减少室外机数量；多个独立系统可增加系统独立性。用一台与两台DELLA室外机的参考产品图说明，深度对比链接至 Single-Zone vs Multi-Zone。主图不依赖切换系统数量才可理解。

移动端：房屋概览后接局部裁切和对应说明，不能把整张桌面标注图缩到文字不可读。默认静态内容在 JS 不可用时仍完整。

### 03 — Explore DELLA Multi-Zone Systems，完整Zone选项与商品卡

保留Zone侧栏与Format筛选，商品目录为45款已核实配置，每个2–6 Zone九款（壁挂5、卡式2、隐藏风管2）。全部状态默认显示9款，通过2–6 Zone筛选查看各自9款，商品区右下角集合链接进入完整购物页；每个Zone可直接看九款。切换筛选和Reset重置展示数量到9，Zone与Format取交集，计数使用真实匹配数。当前45款是选定目录，不冒充全店商品总数。

商品卡采用Bedroom页细节：顶部Zone/形式小标签、留白产品图、Spectral500系列标题、系统标称BTU与Zone容量行、横线规格表（Indoor units/Efficiency/Voltage）、Full model name原生details、大号价格、日期快照对应的Available状态、深蓝按钮与反色hover。手机<=600px单列以保证六区长配置可读，平板与桌面沿用响应式网格。

卡片用build_product_cards.py从products.json生成，全部45款静态注入；无JS仍能看到全部商品，筛选/加载更多隐藏。图片来自官方PDP主图，筛选不生成虚构组合。

基础价、管线/安装说明、检查日期放在网格下方共享说明。低于9款时显示实际结果，不填充不匹配商品。持续保留全Multi-Zone及对应Zone集合入口。

### 04 — Room-by-room sizing

图片使用现有needs-della-k4.png，左图右文，保留品牌调性。一个明确标题、两段说明和一个低强调估算入口，不使用编号、图标或四宫格。

H2：Size your system room by room.
正文：Size the system around each room’s heating and cooling needs. Floor area alone won’t tell you which equipment to choose.
正文：If this will be your main heat source, confirm its winter capacity and whether backup heat is needed.
CTA：Get a room sizing estimate，链接至现有Sizing Calculator。

### 05 — Installation planning

桌面左文右图，使用现有planning-della-k4.png，手机图片在前、文字随后。主体为成本理解与正确下一步；不重复商品网格的购买动作。

H2：Plan your installation budget.
正文：Ask for a quote that covers equipment, labor, line sets, electrical work, drainage and any permits or repairs.
唯一主CTA：Find a Partner Installer，链接至现有安装商查找页；不承诺免费设计、到货或安装时效。
Before you order使用原生details，默认关闭，展开含以下四项：
- Confirm room loads and the approved indoor/outdoor unit combination.
- Review piping, drainage and electrical routes, with access for cleaning and service.
-
- Bring your floor plan, room dimensions, current HVAC details and heating goals.

### 06 — Whole-House Mini Split FAQs

FAQ只承担正文没有充分回答的选购疑问，保留三问：
1. Do I need an indoor unit in every room? 补充开放区域/风管分区可能服务多个空间，以及关门房间的送风安排。
2. Can one outdoor unit serve my whole house? 补充室内机组合、安装限制及室内容量合计不等于室外机同步输出。
3. What about fresh air, filtration, and humidity? 补充供暖制冷之外的配套需求。

FAQ采用Bedroom页的单列手风琴、字体、颜色、分隔线和箭头；左右宽度继承Whole House主体.container，桌面最大1360px含24px侧边距，手机16px。正文已回答的整屋可行性、冬季主要供暖、预算不另设重复问题。默认不添加FAQPage schema。末尾保留简短品牌收口及主集合CTA。
## 6. 商品与数据管理

当前商品源为products.json与PRODUCTS.md，2026-09-15核实45个唯一商品ID，2–6 Zone各9个。字段包括官方名称、SKU、PDP、图片、基础价格、可售状态、室内组合、系统标称BTU和实际效率口径。检查证据evidence/catalog-k8。

首屏顺序保留此前P5/P1/P6/P7/P8/P2/P9/P3/P4，其后追加扩充商品。商品卡不把选择范围等同于全店库存。Serena有SEER/SEER2描述冲突时采用官方规格栏SEER，其他按已核实SEER2值。发布前复核价格与可售状态。

## 7. 视觉约束

主规范：`..\della页面设计规范\della-memorial-day-design-system.md`。
配套源：该目录的 `page.pf-ef33e2e6.json.txt`、`pf-ef33e2e6.liquid.txt`。
本地视觉参考：`..\memorial-day-sale`。

- 标题、商品标题 Spectral；正文、按钮、标签 Poppins。
- Navy #0E1953，Blue #5884E7，浅色 #EDF2FF / #F4F7FF，白色为主要内容底色。
- 蓝底白字主按钮，4px 圆角；hover 和实际字号对比度在实施时检查。
- 最大内容宽约 1200px，桌面侧边距32px、手机16px；按规范保持自然章节间距。
- 宽幅 Hero，独立手机裁切；实物产品与住宅场景共同承担视觉，不做纯文字开头。
- 章节节奏：生活横幅 → 房屋关系大图 → 开放商品陈列 → 安装/住宅局部说明 → 紧凑项目推进 → FAQ。
- 辅助说明以行、文字带和局部标注表达，避免连续等高图标卡片。
- 从 EcoFlow 借关系可视化，从 Insta360/Anker 借产品存在感和信息分层；所有字体、颜色和按钮仍遵循 DELLA。
- 图像表达的效果必须与文字承诺一致。未经真实证据支持的案例、用户评价与节省数字省略。

## 8. 文案与 SEO

主意图：mini split for whole house；自然覆盖 whole-house mini split、whole-home heating and cooling、multi-zone system。
Title 草案：Mini Splits for Whole-House Heating & Cooling | DELLA。
Meta 草案：Explore mini splits for whole-house comfort. See how room layout, heating needs, and installation shape your plan, then browse DELLA multi-zone systems.
一个可见 H1；正文和 FAQ 为可抓取 HTML；核心答案不只存在于图片或点击后。
正式 Shopify URL 尚未确认，canonical 在确认后设置。预览页索引策略在发布计划中定义，避免形成公开重复页面。
默认不加无依据的 Product/Review/FAQ 聚合结构化数据。引用来源以少量相关帮助链接或事实记录支持，不把前台变成资料目录。
整页主文案初始预算约 650–900 英文词（含 FAQ，不含完整商品名与站点页头页脚），以可读性和问题完整性为验收，非硬性 SEO 字数。

## 9. 性能、响应式与可访问性

- 核心答案、商品入口、图例不依赖 JS 初始化才能出现。
- 热点若实现，使用按钮、可见焦点、键盘访问及对应说明；触摸用户无需 hover。
- 避免滚动劫持、长串视频和首屏依赖大型 3D。主图提供静态有效版本。
- Hero 优先加载，以下媒体按需加载，图像设置固有尺寸。图片使用适当格式与手机资源。
- 标题、商品配置和按钮保持可读；图标不能替代必要标签。
- QA 视口：390、430、768、1280、1440px；验证页面无横向溢出、图例可读、CTA 不被 sticky UI 遮住。
- 下阶段同时检查性能、链接、图片加载、语义结构、焦点、折叠行为和 reduced-motion。

## 10. 商业验证

按自然/付费和新访客/回访区分指标。主指标为进入相关集合后的有效商品探索、加购和购买；安装入口点击作为辅助推进指标。主图互动是诊断指标，不能替代购买结果。
实施时记录 CTA 位置、目标集合/商品及来源渠道，沿用网站已有事件与隐私机制，不默认加入新追踪服务。
不对 SEO 排名、广告转化或流量增益给出未经测试的评分。首次上线后依据实际流失点再调整商品位置与模块长度。

## 11. 交付阶段与验收

本轮交接包含PRD.md、DESIGN.md、PLAN.md、HANDOFF.md、ZCODE_IMPLEMENTATION_TASK.md、已有商品资料与九张原图，以及design/approved-desktop-reference.png。
下一阶段：zcode直接实现HTML并完成浏览器验证。六章节与当前图稿已经足以开工，不重新规划页面或再次生图。移动端响应式与交互状态按本文实现。

图稿可以定布局与氛围；PRD 和核实商品数据决定最终文字、参数、CTA、兼容关系及范围。zcode 应拆出可维护 HTML/CSS/SVG，不把整页长图直接当网站。

发布验收必须同时满足：

1. 看首屏即可理解主题并找到购物入口。
2. 看核心图即可说出整屋规划与房间数购物的区别。
3. 用户不用完成测验或多次点击就能看到主要信息。
4. 商品和辅助集合路径真实有效，图稿中的占位数据全部替换或省略。
5. 主要供暖、组合匹配与关门送风说明清楚且紧凑。
6. 风险说明与商品、预算及安装节点对应，项目推进方式明确。
7. 手机文本、图片、CTA 与键盘访问验证通过。
8. 所有已核实事实及待维护数据记录来源和日期。

商品清单与实施视觉参考已落实。正式canonical和安装入口的地区结果仍待相应阶段确认；本地实现可继续。HTML、浏览器QA和上线尚未完成。


## 2026-09-15 Codex接手后的当前实施

保持六章、九款商品与当前内容边界。主剖面使用独立写实建筑渲染，Hero使用现代轻奢客厅场景，Plan使用安装规划人物场景；都不需要再次生成整页稿。实际素材与来源见assets/SOURCES.md。What Your Home Needs继续使用既有住宅照片并统一容器边界。标注与文字为HTML可访问内容，页面七档响应式及真实鼠标键盘QA见qa-codex-k2.md。


## 当前视觉校准（2026-09-15，K3）

用户要求进一步贴近提供的设计稿。当前实现以稿件的比例与布局为准：桌面最大容器1360px（含24px左右内边距），Hero约410px；图标背景条、环绕房屋的左右标注、全商品区居中标题、紧凑三列三行陈列、What Your Home Needs的图文比例、Plan的顶部标题与左图右文、左对齐FAQ、浅蓝收尾条均已校准。当前1440px整页约4427px，参考稿同宽约4320px；保留的价格说明、真实FAQ和锚点会造成合理高度差异。

正文继续使用条件式Hero答案、原六问FAQ、九个真实SKU；不采用图稿的错误商品名或泛化性能保证。Hero独立logo保持省略，04图片收在容器内。图稿照片以参考图驱动的四张独立生成素材接近原构图，不承诺逐像素一致；原图与商品图保持。

桌面Plan主CTA与安装商链接在空间允许时同排，手机可换行；这是本轮贴合稿件的当前布局。桌面剖面线指向具体空间，手机取消叠加线并顺序展示完整说明。

代码中CSS按当前布局整理为一套响应式规则，已去除K2叠加样式。证据见qa-codex-k3.md和evidence/codex-k3。

## K4 DELLA机型场景更新（2026-09-15）

按用户提供的品牌产品图，将四张场景中的室内/室外机外观重建为DELLA参考外观。当前图片为hero-della-k4.png、cutaway-della-k4.png、needs-della-k4.png、planning-della-k4.png，位于assets/scene。产品参考原件归档于assets/brand-references。
室内机采用白底DELLA壁挂机的机身、Logo、显示及出风口细节；室外机采用蓝底套装与外墙图的外壳、格栅及蓝色品牌标识。暗底室内机图作为备用参考保存。九张商品官方原图不变，未改商品数据、文案、CSS或JS。
场景图属于参考产品的生成编辑合成，不能作为精确SKU或兼容组合证明；商品卡仍使用官方原图。小尺寸剖面设备按自然比例呈现，Logo不放大成独立广告标记。
1440和390px定向QA：13张图均加载/解码，9款卡片存在，无页面横向溢出，无pageerror；1440px页面高度保持4427px。证据在evidence/codex-k4。布局及交互沿用K3验证。本轮未发布。

## K6 当前标题与说明规则（2026-09-15）

移除四处重复的eyebrow小标签及对应CSS；每章直接以主标题开场。Plan的H2使用Plan the Full Project。剖面图注为Example layout. Final system design varies by home.；低温能力提醒合并到Winter heating正文，取消独立needs-note；计算器旁只保留Planning estimate only.。不移除设备价格范围、示意性质或计算器估算边界。九款商品与交互保持。
1440与390px检查无横向溢出、无eyebrow残留、无独立needs-note，标题与九款卡片存在，截图及JSON存于evidence/codex-k6。未发布。

## K7 FAQ样式（2026-09-15）

按用户明确要求，FAQ直接采用线上Bedroom Mini Split FAQs的单列版式和样式细节。来源：https://cleopatrahines.github.io/della-pages/Mini%20Split%20for%20Bedroom/mini-split-for-bedroom.html。本轮下载并核对公开源码和真实浏览器展开/关闭截图。
当前FAQ：#f8f9fb背景、48px上下padding、独立1200px容器、居中Spectral500/32px标题、28px列表顶间距、#e2e6ee横分隔线、最后一项无底线；问题Spectral500/20px（<=560px为18px）、60px最小行高（手机56px）、18px上下padding，右侧CSS箭头随展开旋转，悬停/展开使用品牌蓝；答案15px/1.7。保留原生details多项独立展开与键盘行为，六组Whole House问答原文保持不变，移除FAQ副标题和旧双列卡片样式。
1440/768/390px验证布局、字体、背景、容器尺寸及六问；真实点击展开与Enter收起通过，无页面横向溢出。证据evidence/codex-k7。原HTML备份evidence/before-k7。未发布。

## K9 用户明确要求移除零散小字（2026-09-15）

前台移除：剖面下方Example layout图注、商品网格下方共享shop-notes、需求区Have usable ducts提醒、Estimate a Room旁Planning estimate only，以及收尾下方的价格/核实日期footnote。对应节点和无用CSS一起删除，剖面与系统卡之间保持12px正常间距。不得由后续生成器重新添加这些小字。
具体来源日期、价格基础、概念图性质与验证条件继续记录于项目资料；正文和FAQ保持。没有改动45款商品、Bedroom样式卡片、分页、筛选或FAQ样式。
1440/390px检查五类节点均为0、无横向溢出、45款数据和6组FAQ存在、默认9款；6 Zone点击仍显示9款。证据evidence/codex-k9。未发布。

## K10 当前衔接（2026-09-15）

用户认为系统安排双卡无必要，当前页面移除One multi-zone system / Multiple systems双卡及其专属Compare Single-Zone vs Multi-Zone链接，剖面图后直接进入商品区。相关HTML和CSS删除。FAQ保留一套或多套系统的答案；45款商品及分页保持。
1440/390px验证模块无残留、章节正常相接、无横向溢出、45款商品和6问存在。证据evidence/codex-k10。未发布。


## K13 全页文案定稿（2026-09-15）

按humanizer/stop-slop与avoid-ai-design进行完整审核，当前HTML采用18处针对性文案修改，详见EDITORIAL-VISUAL-REVIEW.md。保留原技术限定与45款商品数据，不恢复先前删除的小字或系统双卡。主尺寸标题为Size your system room by room，安装标题为Plan your installation budget，收尾为Find Your Multi-Zone System。后续以当前HTML及该审查记录为当前文案依据。


## K14 商品图与底部动作（2026-09-15）

用户明确选择程序化批量去背景。当前45款使用透明衍生图，原图保留，保持机身、Logo与产品内容像素。商品图采用近满卡宽的正方形媒体区域和contain，保留少量边距。商品区只有右下角一个集合链接，按所选Zone更新目的地。默认All展示9款，选择每个Zone展示9款；不设Show More按钮或额外分页。卡片规格、价格、完整型号与45款目录不变。图片处理与验收见PRODUCT-IMAGE-PROCESSING.md。

## CTA interaction (K15)
Filled page CTAs use a white/navy hover state with a 1px lift and a light-blue pressed state. Text CTA arrows move subtly on pointer hover. Keyboard focus remains visible; reduced-motion settings suppress displacement. Content, destination URLs and product data are unchanged. Verified real pointer hover/press, keyboard focus and five viewport widths (390–1440px); evidence: evidence/codex-k15.


## Current section flow (K18)
Hero and benefit strip → house layout → product catalogue → room sizing → FAQ and final collection CTA. The anchor navigation links to How It Works and Systems. Room sizing flows directly into the FAQ.


Hero navigation (K21): the banner provides the shopping and house-layout entry points. The benefit strip is followed directly by the house-layout section.


H2 typography (K22): every H2 uses Spectral / Georgia / serif, 32px, weight 400, line-height 1.12 and #0E1953 across viewport sizes. Section-specific spacing and alignment remain in their layout rules.
