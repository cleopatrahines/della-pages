# PLAN：本地还原与验收

## 执行前

1. 读取项目 AGENTS.md（如有）、HANDOFF.md 及本包 PRD/DESIGN；旧任务与本包冲突时以本包为准。
2. 检查当前 git status；不回滚用户修改。创建带时间戳的 HTML 备份。
3. 记录当前 #products、#services 外观及其 DOM、相关 CSS/JS。它们是冻结基线。
4. 将本包文档复制到项目 docs/selected-design-20260920；素材复制到项目 assets 的新文件名。保留原图和备份，不覆盖同名不同内容的资产。

## 资产准备

- SELECTED_DESIGN.png 是参考图，不作为网页背景或大切片。
- assets/hero-luxury.png → Hero。
- assets/selector-alternatives.png → 选型器左侧位置示意。
- 场景 tabs、字体及商品图继续用项目已有 assets/数据。
- 转换 WebP/提供响应式尺寸，维持原始纵横比；PNG 保留源文件。机器此前已确认 Python Pillow 可读取这些图片，可检查其 WebP 编码支持；不要仅因没有 magick/cwebp 就报告无法转图，也不必默认安装依赖。
- Hero eager，设 width/height，合适 srcset/sizes；其余图按位置 lazy。手机裁切优先保住设备。

## 实现

1. Hero 替换当前双图结构，单场景和单 CTA；保留 H1/SEO 意图。
2. #decision-checker 改为左场景、右表单，复用原生 radio 和 resolver，精简结果重复文案。
3. #comparison 重排图表头与分组表，去掉隐藏行控制；手机使用属性标签上方、两值下方。
4. FAQ 更新五条并同步 JSON-LD。
5. 页尾替换为短标题＋两按钮。
6. 移除被替代区域的死规则及事件，避免一层层覆盖；不清理无关模块。

## 验证

- 实际浏览器点击 27 种完整答案组合，与 PRD 矩阵逐条比较；初始/答1题/答2题/重置不推荐；unknown 不等于 no。
- tabs 依次及快速切换，最终 image/alt/copy/product set 一致。无须改写已正确逻辑。
- 桌面/手机 Hero、选型器、中性/推荐/安装帮助状态、完整比较、FAQ 和页尾截图。
- 1440/1280/1024/768/430/390/360 实测页面宽度、溢出元素、字体、图片加载；不得用全局 overflow:hidden 掩盖越界。
- 键盘 radio/Tab/reset/tablist/FAQ、focus-visible、reduced motion、console、坏图/空链接。
- visible FAQ 与 JSON-LD 比较解码后的五个问答。
- 产品/Services DOM与数据无非预期变化，截图回归。样式测试不是只有 scrollWidth 相等。

## 交付停点

交付完整本地版本及 docs/selected-design-20260920/qa 中的截图和结果。HANDOFF 记录当前文件、备份、素材来源、差异、未决事项。停本地等 Codex 视觉审核；不提交/推送/发布。不将通过功能检查当作已通过视觉审核。
