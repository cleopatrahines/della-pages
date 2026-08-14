# NEXT CHAT PROMPT — Ductless Mini Split vs Central Air

> Copy everything below the line into a new conversation to continue this project.

---

你现在接手一个已完成本地设计与 QA 的 DELLA 专题落地页项目。先完整读取以下文件再动手：

**必读 Skill（强制执行规范）**：
- `C:\Users\18041\.codex\skills\della-page-builder\SKILL.md`（含 2026-08 新增的 Production Lessons 章节，来自本项目的沉淀）
- `C:\Users\18041\.codex\skills\avoid-ai-design\SKILL.md` + `references/ai-tells-catalog.md`
- `C:\Users\18041\Desktop\skills\humanizer\SKILL.md`
- `C:\Users\18041\Desktop\skills\stop-slop\SKILL.md`

**项目文件**（`C:\Users\18041\Desktop\della-pages\Ductless Mini Split vs Central Air\`）：
1. `PRD.md` —— 权威策略源。注意 §12 里所有带日期的 **Owner override**（2026-08-13/14），它们的优先级高于正文旧规则
2. `HANDOFF.md` —— 集成期规则（广告守则、双数据源、KPI、衰减触发器）
3. `KIMI_CHANGELOG.md` —— Round 1–15 全部改动记录
4. `KIMI_AUDIT.md` —— 审核报告 + avoid-ai-design 附录 + 长期多视角附录
5. `sources.md` —— 产品价格快照（2026-08-13）、图片映射、派生资产溯源
6. `Design.png` —— 批准的视觉参考
7. `ductless-mini-split-vs-central-air.html` —— 最终页面
8. `k3-qa-report.json` —— 最新 QA 结果（57/57 通过）

## 当前状态

- **页面已完成并上线 GitHub Pages**：`https://cleopatrahines.github.io/della-pages/Ductless%20Mini%20Split%20vs%20Central%20Air/ductless-mini-split-vs-central-air.html`，已置顶于仓库 index.html 目录页
- **Git**：本地与 `cleopatrahines/della-pages` master 完全同步（最新 commit `8f8faa9`）。注意远端有另一台机器的 sizing-calculator 项目，push 前必须先 fetch/merge
- **QA**：57/57 通过（7 视口无溢出、4 路径状态、无 JS 回退、键盘、reduced motion、0 控制台错误）

## 已锁定的最终形态（不要再改）

- 结构：Hero（VS 合成图 + 25 词文案 + 单 CTA）→ Gateway（Replace/Add/Supplement 三卡，Not sure 轻链接）→ 条件商品区（8 卡统一 navy View Product 新窗口）→ 对比表（8 行含成本/效率行）→ BEFORE YOU BUY 安装条 → Premium Della Services（owner 指定保留）→ FAQ（4 条，owner 精简过）→ 情境化底部 CTA
- 按钮体系沿用 Ceiling Cassette 参考页（navy 主按钮反白 hover、灰边副按钮）
- 文案已过 humanizer + stop-slop 终审（43/50）；避免 AI 设计审核零命中
- **不要做的事**：不加新板块、不恢复被删的 FAQ 两条、不恢复 ATC、不恢复对比表列高亮、不动 Services（这些是 owner 明确决定，回滚=违抗指令）

## 待办（Shopify/PageFly 集成轮次，按 HANDOFF.md 执行）

1. 确认 Shopify 页面 handle 后启用 Liquid `canonical_url`（静态版不得硬编码 canonical）
2. 价格管道：Liquid `all_products` 优先（8 handle < 20 上限），PageFly 面不支持则走 Ajax Product API fallback；**必须验证 hydrate 真实生效**，否则页面会静默展示 2026-08-13 快照价格
3. og:image 换成 Shopify CDN 绝对地址（HTML 里有注释标记）
4. GA4 接线：现有 `della:*` CustomEvent + 守卫式 gtag 钩子；KPI 按 HANDOFF（Qualified Action / Correction 不算失败 / Final Path × Source）
5. 嵌入后检查 PageFly 样式污染（页面 CSS 挂在 `.della-system-compare` 作用域下）和 `<html>` 的 no-js/js class 兼容
6. 广告上线守则：通用对比广告不带 `?path=`，只有明确路径的广告才加

## QA 环境重建（临时目录会被系统清理）

```powershell
mkdir C:\Users\18041\AppData\Local\Temp\opencode; cd 到该目录
npm init -y; npm install playwright   # 不需要 playwright install，用本机 Chrome
```
QA 脚本用 `chromium.launch({channel:'chrome'})` 驱动系统 Chrome。历史 QA 脚本要点见 `k3-qa-report.json` 的检查项清单。

## 工作方式约定

- 改代码前先读 PRD §12 的 owner override 清单，避免回滚 owner 决策
- 每个改动跑完整 QA 并截图复核；QA 报告写新文件不覆盖旧的
- Git 操作先问；commit message 用祈使句英文短句
- 最小有效修改；不为展示工作量制造改动
