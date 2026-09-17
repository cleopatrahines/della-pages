# 商品实现清单

本页选品由 Codex 在本次研究阶段确定；用户没有指定单个 SKU。以 `products.json` 为机器可读来源。日期：2026-09-16；原始采集时间保存在 JSON 的 capturedAt。

已核验：Shopify collection products JSON 的产品身份、变体、价格与 available；Window PDP 技术字段；Portable 集合 SACC/ASHRAE；产品图来自 Shopify 返回的对应产品或变体图片。available 表示可购买，不表示仓库现货或送达时效。

## 展示顺序与选品理由

| ID | 面板 | 简短名称 | 容量 | 变体 | 研究时价格 USD | 展示理由 |
|---|---|---|---|---|---|---|
| p01 | Mini Split | Vario | 9,000 BTU | 230V | 729.96 | 单房间较小容量起点 |
| p02 | Mini Split | Serena | 12,000 BTU | 115V | 799.96 | 不同容量/电气选择；链接固定为该变体 |
| p03 | Mini Split | Serena | 18,000 BTU | 230V | 1,049.96 | 较大单空间的容量选择 |
| p04 | Mini Split | Optima Pro | 12,000 BTU | 230V | 1,249.96 | 不同热泵系列与效率选择 |
| p05 | Window AC | Fenestra | 5,000 BTU | Default Title | 169.96 | 小空间、机械控制 |
| p06 | Window AC | Fenestra | 8,000 BTU | Default Title | 269.96 | 常规智能控制选项 |
| p07 | Window AC | Miri | 8,000 BTU | Default Title | 379.96 | 同容量的变频选项 |
| p08 | Window AC | Fenestra | 12,000 BTU | Default Title | 359.96 | 较大房间容量选择 |
| p09 | Portable AC | Smart Portable AC | 8,000 BTU SACC / 12,000 ASHRAE | Default Title | 309.96 | 当前较低 SACC 档位 |
| p10 | Portable AC | Smart Portable AC | 10,000 BTU SACC / 14,000 ASHRAE | Default Title | 379.96 | 中间 SACC 档位 |
| p11 | Portable AC | Sylro | 12,000 BTU SACC / 15,500 ASHRAE | Default Title | 599.96 | 双风管与变频选项 |

理由仅用于维护选品配置，不自动作为 Best / Recommended 等消费者标签。p02 和 p03 使用 Serena 系列标题，紧邻的容量副行分别显示 12,000 BTU 与 18,000 BTU；以系列、容量和变体组合识别商品。p04 不展示未经条件说明的低温额定数字。

## 数据规则

- 精确完整 title、handle、productId、variantId、sku、url、imageUrl 和本地图片路径均在 products.json。
- p02 必须展示 115V 的 $799.96，与带该 variant ID 的 PDP 链接一致。另一个 230V 变体的 $779.96 不能作为这张卡的售价。
- compare_at_price=0 不代表划线价，全部省略假折扣。
- coverage 是厂家建议面积，以 `Up to ...` 保留口径；不保证实际负荷匹配。
- 有些 Shopify 图片文件名带不同容量，站点在多个型号间共用媒体。以产品/变体对象的媒体关联为准，不能从文件名反推出规格。
- p01–p04 容量、SEER2 和面积与对应标题/描述匹配，电压来自 variant option，未靠 SKU 字符串推算。
- p05–p08 的电压和容量已核对 PDP；p07 的 Inverter 是产品明确属性。不要把 PDP 的泛称 Efficiency Ratio 15.0 自动改写成未经确认的 CEER。
- p06 PDP 有 Window Range 23–36 inches；可在其展开信息中保留这个标签，但它不包含全部窗型/最小高度条件。其余选定窗机没有在本轮证据中得到完整窗口开口范围，通过完整型号折叠区内的 Check window fit 引导 PDP。机身外形尺寸不能当作安装开口尺寸。
- p09/p10 的 URL handle 含旧面积数字，当前标题和集合分别显示 350/450 sq. ft.。保留原 URL，显示已核对的当前标题与面积。
- p09/p10 不在本次卡片上断言单风管；只显示已核对运行模式。p11 双风管/变频已在官方描述确认。
- Portable Sylro 14K/10K SACC 本次不可购买，不选入。后续恢复销售也不自动挤进精选区。

## 证据文件

- `evidence/catalog-handoff-snapshot.json`：三个集合原始数据。
- `evidence/window-spec-evidence.json`：四个窗机 PDP 技术字段摘录。
- `evidence/portable-rating-evidence.json`：SACC/ASHRAE/面积对应关系。
- `assets/products/p01.jpg` 至 `p11.jpg`：原始 Shopify 图片；下载成功后已抽查 p01/p07/p11 外观与品类匹配。

价格和可购买状态是研究快照，实施交付前应复核；无法联网时明确记录未复核，不宣称实时。若某变体不可购买，减少卡片并保留集合入口，不暗换型号或电压。

## 与页面文案的关系

商品身份和规格按本清单及 manifest；卡片字段布局按 LOCKED-COPY/DESIGN。官方 PDP 中的泛化节能、低温、认证、折扣、保修和噪音营销语并未全部纳入本页，不从原始 body_html 直接复制到卡片。
