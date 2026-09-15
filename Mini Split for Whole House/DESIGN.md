# Whole House — 实施视觉规格

状态：2026-09-15，用户接受最新返图作为实现参考，要求Hero不显示独立logo、What Your Home Needs图片收进容器。视觉参考：design/approved-desktop-reference.png。

## 保留

- 明亮现代轻奢住宅，暖白、浅灰、烟熏木与柔和自然光；DELLA蓝白UI。
- 宽幅Hero、完整房屋剖面、Zone侧栏+三列九款商品、住宅局部与规划模块、左图右文安装模块、双列FAQ。
- 标题Spectral，正文/按钮Poppins；颜色、按钮沿用项目本地PageFly设计规范。

## 必须覆盖图稿的部分

1. Hero无单独品牌logo，无仿造全站header/footer。
2. What Your Home Needs为正常居中容器双栏，不做出血。容器max-width约1200px，padding-inline桌面32px/手机16px；grid子项min-width:0，图片display:block;width:100%;height:100%;object-fit:cover，媒体容器aspect-ratio约4/3并局部overflow:hidden。不能用全页overflow-x:hidden掩盖宽度错误。
3. Hero、情境条、系统安排和FAQ的最终含义来自PRD。图稿中的营销改写不自动采用。
4. 产品图为本地九张官方原图。所有型号、配置、SEER2和价格由products.json生成；图稿中的P3名称错误等全部覆盖。
5. 商品价旁恢复“Base equipment price. Line sets and installation extra. Images show optional line sets.”及同步需求提示。
6. 剖面标注语义正确，房间家具不能证明卧室时用Closed rooms；设备数量示意与文字一致，不把室外机图片标成室内形式。
7. 仅当工程上能正确表达时才有高亮热点，正文与图例默认可见；不输出个性化设备建议。
8. Plan模块：标题上方/顶部，图左、三项短说明右。主CTA Shop Multi-Zone Systems，辅助Find a Partner Installer独立成行，底部准备清单为折叠项。

## 资产与清晰度

- 参考图是用户提供的低分辨率整页长图，仅用于视觉比对。保留原始PNG，不将它放大后作为整页网页。
- 优先寻找项目及现有DELLA素材内适合的原图，保留同一住宅调性。图稿无文字的局部可作临时裁切素材，但记录其原始像素限制；不能截图复制文字、按钮、产品网格或FAQ。
- CSS裁切负责适配布局，不更改参考图本身；本任务不要求再次生图。缺少大尺寸独立Hero/剖面源图时先完成可运行页面并记录资产质量限制，不虚称高清复刻。
- 产品原图2000×2000，直接使用本地文件；加载时保留固有比例。界面文字、标签、连接线、按钮用HTML/SVG重建。
- 字体尽量复用已有本地Spectral/Poppins字体；按路径和实际字重核实，不临时引入新字体。

## 响应式与视觉验收

- 1440/1280桌面：统一容器、清楚层级，商品侧栏只在商品模块内吸附。
- 768：空间不足时改变列数，避免挤压商品和标签。
- 390/430：Hero内容可读，商品导航改为横向或下拉，商品1–2列，图片与文字上下排列。布局由代码适配，不要求手机设计图。
- What Your Home Needs图片四周边界与同级模块对齐，所有断点无横向溢出。
- 图片覆盖与文字实际边界分开检查；阴影、圆角克制，不新增装饰渐变和浮层。
- 检查正文/按钮色彩对比度、焦点、键盘、reduced-motion及资源缺失。


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

## K5 两处短条优化（2026-09-15）

Hero下方改为四项价值说明，产品功能与已核实集合范围对应：Room-by-Room Control / Separate temperature settings；Heating & Cooling / Both in one heat pump system；Indoor Style Options / Wall-mounted, cassette or ducted；2–6 Zone Options / Explore a range of configurations。桌面四列、手机两列，不引入节省账单或全年性能承诺。
剖面下方以一台及两台DELLA室外机的参考图说明One multi-zone system和Multiple systems，图文一致。不是室内机形式对比，也不据此推断具体SKU兼容性。保留单一的深度比较链接。已有风管的判断移到需求规划区。
新素材assets/scene/della-outdoor-cutout-k5.png由用户的della-system-blue.png参照提取生成，原始生成文件exec-2854b7e0-3b3f-4585-bda5-644a8217d8a1.png保留；这是产品参考衍生图，九张PDP原图仍不变。
1440/768/390px定向检查无横向溢出，四项价值与两张系统卡完整，三处设备图片加载正常，九款商品存在；真实点击3 Zone+卡式仍返回1款。证据evidence/codex-k5。未发布。

## K6 当前标题与说明规则（2026-09-15）

移除四处重复的eyebrow小标签及对应CSS；每章直接以主标题开场。Plan的H2使用Plan the Full Project。剖面图注为Example layout. Final system design varies by home.；低温能力提醒合并到Winter heating正文，取消独立needs-note；计算器旁只保留Planning estimate only.。不移除设备价格范围、示意性质或计算器估算边界。九款商品与交互保持。
1440与390px检查无横向溢出、无eyebrow残留、无独立needs-note，标题与九款卡片存在，截图及JSON存于evidence/codex-k6。未发布。

## K7 FAQ样式（2026-09-15）

按用户明确要求，FAQ直接采用线上Bedroom Mini Split FAQs的单列版式和样式细节。来源：https://cleopatrahines.github.io/della-pages/Mini%20Split%20for%20Bedroom/mini-split-for-bedroom.html。本轮下载并核对公开源码和真实浏览器展开/关闭截图。
当前FAQ：#f8f9fb背景、48px上下padding、独立1200px容器、居中Spectral500/32px标题、28px列表顶间距、#e2e6ee横分隔线、最后一项无底线；问题Spectral500/20px（<=560px为18px）、60px最小行高（手机56px）、18px上下padding，右侧CSS箭头随展开旋转，悬停/展开使用品牌蓝；答案15px/1.7。保留原生details多项独立展开与键盘行为，六组Whole House问答原文保持不变，移除FAQ副标题和旧双列卡片样式。
1440/768/390px验证布局、字体、背景、容器尺寸及六问；真实点击展开与Enter收起通过，无页面横向溢出。证据evidence/codex-k7。原HTML备份evidence/before-k7。未发布。


## K8 当前商品陈列（2026-09-15）

根据用户要求，商品目录扩至45款，2–6 Zone各9款，每组5壁挂/2卡式/2隐藏风管；全部默认9款、每次增加9款。卡片按Bedroom页规格表、完整型号展开、大号价格、Available快照与深蓝按钮样式实施。手机<=600px单列，平板/桌面保持网格。以当前products.json、PRODUCTS.md和PRD第03/06节为准。

浏览器验证：1440/1280/768/430/390均无横向溢出；各Zone=9、各Zone与Format交集5/2/2；分页9/18/27/36/45、筛选重置分页、完整型号鼠标展开/Enter收起、45款官方名称与PDP映射、无JS45款回退通过。证据evidence/codex-k8。未发布。

## K9 用户明确要求移除零散小字（2026-09-15）

前台移除：剖面下方Example layout图注、商品网格下方共享shop-notes、需求区Have usable ducts提醒、Estimate a Room旁Planning estimate only，以及收尾下方的价格/核实日期footnote。对应节点和无用CSS一起删除，剖面与系统卡之间保持12px正常间距。不得由后续生成器重新添加这些小字。
具体来源日期、价格基础、概念图性质与验证条件继续记录于项目资料；正文和FAQ保持。没有改动45款商品、Bedroom样式卡片、分页、筛选或FAQ样式。
1440/390px检查五类节点均为0、无横向溢出、45款数据和6组FAQ存在、默认9款；6 Zone点击仍显示9款。证据evidence/codex-k9。未发布。

## K10 当前衔接（2026-09-15）

用户认为系统安排双卡无必要，当前页面移除One multi-zone system / Multiple systems双卡及其专属Compare Single-Zone vs Multi-Zone链接，剖面图后直接进入商品区。相关HTML和CSS删除。FAQ保留一套或多套系统的答案；45款商品及分页保持。
1440/390px验证模块无残留、章节正常相接、无横向溢出、45款商品和6问存在。证据evidence/codex-k10。未发布。

## K11 FAQ当前规则（2026-09-15）

FAQ与本页主体共用.container，保留Bedroom的手风琴样式；左右边界不另设独立1200px容器。仅保留每房是否需要室内机、一台室外机能否服务全屋、新风过滤湿度三问，答案原文保持。四档1440/1280/768/390px测量FAQ列表与前一模块正文边界完全一致；点击展开和Enter收起通过，45款商品不变。证据evidence/codex-k11。未发布。


## K12 尺寸与安装两模块（2026-09-15）

用户希望减少AI模板感、拥挤和重复信息。采用DELLA品牌内的精简图文呈现：尺寸区左图右文、一个42px标题与两段16px正文、一个估算链接；安装区左右交替，默认一段预算说明、一个安装商按钮、Before you order折叠检查项。现有两张图片和六章顺序不变，不新增小标识、脚注、图标或编号。正文见PRD第04/05节。

共享主按钮恢复蓝底白字，商品卡深蓝按钮保持。保留45款商品、分页、Zone/Format交集与三问FAQ。1440/1280/768/430/390验证无横向溢出，图片解码、原生展开及键盘收起通过，6Zone+卡式=2。证据evidence/codex-k12。未发布。


## K13 全页文案/视觉审核

保持DELLA品牌与当前布局；剖面标注正文为13px，配合具体的空间说明。没有新增标签、脚注或装饰。实际修改与待办详见EDITORIAL-VISUAL-REVIEW.md。


## K14 当前商品卡媒体

商品图框为正方形、左右14px（手机12px）边距，透明图contain，宽度约87%–93%卡宽，替代固定180px高度图。保留Bedroom的标题/规格/价格/按钮细节。网格底部唯一集合按钮右对齐；无Show More。验证见evidence/codex-k14。

## CTA interaction (K15)
Filled page CTAs use a white/navy hover state with a 1px lift and a light-blue pressed state. Text CTA arrows move subtly on pointer hover. Keyboard focus remains visible; reduced-motion settings suppress displacement. Content, destination URLs and product data are unchanged. Verified real pointer hover/press, keyboard focus and five viewport widths (390–1440px); evidence: evidence/codex-k15.


## Current section flow (K18)
Hero and benefit strip → house layout → product catalogue → room sizing → FAQ and final collection CTA. The anchor navigation links to How It Works and Systems. Room sizing flows directly into the FAQ.


Closing CTA spacing: page content reserves 64px below the CTA on desktop and 40px below it at widths up to 767px, using main-container padding.


Product collection CTA: right-aligned navy text with a horizontal arrow, 44px minimum hit area, subtle arrow movement on hover and visible keyboard focus. Zone-specific destinations and labels update together.


Hero navigation (K21): the banner provides Shop Multi-Zone Systems and See How It Works. The benefit strip flows directly into the house-layout section.


H2 typography (K22): every H2 uses Spectral / Georgia / serif, 32px, weight 400, line-height 1.12 and #0E1953 across viewport sizes. Section-specific spacing and alignment remain in their layout rules.


Closing heading has 12px spacing before its supporting copy. The room-sizing link shares the collection CTA's navy text, horizontal arrow, hover movement and keyboard focus styles.
