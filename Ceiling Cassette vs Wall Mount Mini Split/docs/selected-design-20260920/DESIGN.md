# DESIGN：用户选定长图的实现规范

依据 SELECTED_DESIGN.png。用户选择视觉方向；交互与事实以 PRD.md 为准。保留图的整体气质，不改为白底左右分栏 Hero、白底产品图选型区、深蓝色整段或新的导航。

## 品牌与尺度

使用项目本地 Spectral-Regular / Spectral-Bold 与 Poppins 400/600。Navy #0E1953、blue #5884E7；白底及浅灰分组条。内容约 1200px 最大宽度，桌面侧距至少 32px，手机 16–20px。所选图宽约 718px 是压缩整页示意，不能按图片像素当 CSS 字号。H1 桌面约 44–54px、手机 32–36px；H2 桌面 30–36px；正文 15–16px，比较单元 14–16px。

## Hero

全宽图片，桌面高度约 500–580px；左侧文案与下方容器对齐，宽约 450px。暖白空墙留给文字，设备保留在天花右上区域。仅必要的轻微局部对比度处理，不使用遮盖半图的浓渐变。一个 44–48px navy 按钮。

H1: Ceiling Cassette vs Wall Mount Mini Split

副标题: Compare placement, installation and everyday access.

按钮: Compare the styles

assets/hero-luxury.png 是无字原始母图，与设计稿场景相近，不是从网页稿抠出的截图。不得裁掉设备或把设备再放大。手机文字在上、场景在下，色调连续、无外框，图片裁切保设备完整。

## 选型器

标题 Which style fits your room?；副标题 Check the space before choosing the indoor unit.

桌面左侧场景约 54%、右侧问题约 46%，24–32px 间距。场景使用 assets/selector-alternatives.png。不得换回两个白底 packshot。可以用 HTML 加 1/2 两个小标记，对应天花与墙面；不要烘焙按钮入图片。

图注必须可见：Alternative installation locations, illustrated together. Not an installation drawing.

图中剖面仅用于位置示意，没有经过施工校核。不要添加尺寸、结构改造建议或与任意具体型号保证匹配的陈述。

问题标签：Ceiling installation checked? / A usable high-wall location? / Your priority。

三组选项原生 radio + label，控件以细边框、圆点表示状态，44px 最小触控高度。结果在右栏问题下方，用紧凑浅蓝区域；纠正图中 yes/yes/look 的推荐。初始结果为一行提示，不预选复制截图答案。保留 Compare both styles 与 reset。结果变更不抢焦点，aria-live 仅播报短结论。

手机：标题→场景（适当缩短但设备完整）→题目→结果。题目选项能换行，不能缩到不可读。

## 比较

两类室内机白底大图在各自数据列正上方。左标签列约 22%，其余等分。真实 indoor 图优先；若本地只有整套图，可用容器裁切只呈现上部室内机，保留原图、避免变形，必须截图检查边缘和机身完整性。cc-12k.jpg 与 wm-12k-vario.jpg 保留为商品数据源，不用生成图替代真实商品图。

两条浅灰组标题＋六行值，细分隔线，无大圆角外壳、没有下拉菜单或胜者标签。文本依 PRD。桌面保持一眼横向比较，不折叠。

手机：每个属性标题单独占一整行，下方 cassette / wall 两个等宽值并列；避免 sticky 左标签列挡住值。保留类型名称对应关系，不强制横滑，不把两种方案拆成前后两张大卡。用语义 table 或有等价可访问标题关联的结构实现。

## 保留的商品模块与 Services

截图中简化的商品卡不能作为实现源码：完整保留当前 #products 的四 tab、场景、商品卡、实际规格/价格/详情和交互。当前 #services 内容、图标和四卡布局保留。只通过新区域的局部选择器做样式，避免改全局 h2/.section/.btn 后波及这两块。

## FAQ 与页尾

FAQ 样式保留当前页面，替换 PRD 中五条文案，同步已有 JSON-LD。页尾按选定图：浅灰平面区、居中短标题 Explore both indoor-unit styles、Shop Ceiling Cassette 和 Shop Wall Mount 两枚等权按钮。手机按钮可上下排列。无额外产品卡、图标、服务条或长解释。

## 与设计图之间的必要偏差

1. 推荐结果纠正并加原因。
2. 选型场景标注概念性替代位置。
3. 产品和 Services 使用现有真实版本，不使用生成的文案/价格/简卡。
4. FAQ 五条替代六条。
5. 手机实际排版需按可读性适配。
