# PRD：Ceiling Cassette vs Wall Mount

## 目标

Comparison guide。说明两种室内机的外观、安装和使用取舍，允许用户据已知房间条件确定先比较哪种，然后浏览商品。未知安装条件不能阻止查看两种产品。

## 2026-09-20 已确定事项

- 唯一视觉基准为用户上传的 SELECTED_DESIGN.png。接受的是构图、模块节奏和图文关系；不代表确认图内产品数据或错误推荐。
- 按所选图保留选型区左场景、右问题。使用 assets/selector-alternatives.png，图下写清两种替代安装位置示意，非施工图。
- Hero 单一轻奢客厅、一个 cassette、一枚 Compare the styles 按钮跳到 #decision-checker。不加导航、公告、信任 bar 或第二枚 Hero 按钮。
- quick-answer 独立解释模块已删除，保持这一状态。
- 比较区固定两种类型，产品图表头、两组内容、六个维度；没有型号下拉和购买控件。
- 产品区和 Services 不重新设计、不重写内容。保留四个 tabs 的现有图文与商品联动，保留真实整套产品图、规格、价格、View Product 和 line-set 注释。
- FAQ 可见问题改成五条，答案以本文件为准；保持当前 details/summary 样式。同步现有 FAQPage。
- 页尾按所选图使用 Explore both indoor-unit styles 和两个等权品类按钮。没有品类商品卡、重复安装说明或深色大背景。

## 当前改动范围

Hero / #decision-checker / #comparison / FAQ 内容与关联 schema / 页尾 CTA，以及上述区域需要的资产。共用 CSS 改动不得造成商品区与 Services 变化。

## 链接

- Hero → #decision-checker
- 比较辅助入口 → #comparison
- Cassette → https://dellahome.com/collections/ceiling-cassette-mini-split
- Wall Mount → https://dellahome.com/collections/wall-mounted-mini-split
- 安装帮助沿用当前 https://dellahome.com/pages/find-a-installer
- PDP 保持当前真实链接。新外链遵循项目原有 target/rel 约定。

## 选型逻辑契约

state.ceiling / state.wall = yes, no, unknown；state.priority = look, work, neutral。沿用已有可行性优先 resolver。初始不预选，未答全不推荐，Compare both styles 始终可达。Reset 恢复初始状态。

| ceiling | wall | look / work / neutral 的预期类别 |
|---|---|---|
| no | no | 三种均为安装帮助；不推荐任一类型 |
| no | unknown | 三种均为先核实墙面 |
| unknown | no | 三种均为先核实天花 |
| unknown | unknown | 三种均为核实安装位置；两类仍可浏览 |
| no | yes | 三种均为先比较壁挂机 |
| yes | no | 三种均为先比较 cassette |
| unknown | yes | 三种均为先比较壁挂机，明确天花尚未确认 |
| yes | unknown | 三种均为先比较 cassette，明确墙面尚未确认 |
| yes | yes | look → cassette；work → wall；neutral → 两者比较 |

优先项显示 Clear walls / Less ceiling work / Either，内部保留 look/work/neutral。Clear walls 与“保留墙面空间”对应，不擅自许诺所有 cassette 更隐蔽。结果简化为标题＋一句原因＋一句核实项＋下一步。不要将旧 copy、reasons、verify 中的同义句全部叠加。

选定图展示 yes/yes/look，正确结果为：

Compare ceiling cassettes first

Both locations may work, and you prefer to keep the walls clear.

Confirm drainage and service access before ordering.

View cassette options → cassette collection；Compare both styles → #comparison。

两项 unknown 示例：Check the installation locations；Ask an installer to assess ceiling space and wall placement. 主入口安装帮助，保留 Compare both styles。不得出现“确认前不许比较商品”的文案。

## Comparison 文案

标题：Ceiling cassette or wall mount?

| 分组 / 维度 | Ceiling Cassette | Wall Mount |
|---|---|---|
| PLACEMENT & APPEARANCE / Indoor position | Recessed into the ceiling | Mounted high on the wall |
| Visible indoors | Ceiling panel | Wall-mounted unit |
| Airflow | From above | Across the room |
| INSTALLATION & ACCESS / Space to plan | Ceiling cavity and drain route | Wall clearances and line route |
| Filter access | From below the ceiling panel | From the front panel |
| Installation work | Ceiling opening and finish work | Wall mounting and line routing |

描述安装形式；不推导某种类型总是更便宜、安静、省电或只能用于某种房间。型号具体要求以其说明书为准。

## FAQ：五条完整替换文案

### Can a ceiling cassette be installed in a finished ceiling?

It may be possible. Before ordering, ask an installer to check the space above the ceiling, framing, drainage and service access. The quote should also account for opening and repairing the finished ceiling.

### Is the listed product price the full installed cost?

Check the product listing for what is included. Ask for an itemized installation quote covering labor, electrical work, refrigerant piping, drainage and any ceiling or wall repairs. Confirm whether the selected configuration includes a line set.

### Can ceiling cassette and wall-mounted units share one outdoor unit?

Only if the specific indoor and outdoor models are approved to work together. Ask DELLA or your installer to confirm the combination and capacity limits before buying. Matching the brand or adding up BTU ratings is not enough to establish compatibility.

### Is one style always quieter or more efficient?

No. Compare the ratings for the complete matched system and the indoor noise specifications for the operating mode you will use. Placement, room acoustics and installation also affect what you hear.

### Can I install either system myself?

Check the installation requirements for the exact model before buying. Installation includes electrical connections, refrigerant piping, drainage and mounting. Arrange qualified help for work you are not equipped or permitted to perform, and review the model's installation and warranty requirements.

## 数据与发布边界

保留本地商品快照，不宣称价格已重新核实。Services 保留用户冻结的模块；本轮不代表重新核实其政策承诺。生成图不提供技术尺寸或可行性证明。不要修改 canonical、URL、产品数据、index 指令或提交/发布。
