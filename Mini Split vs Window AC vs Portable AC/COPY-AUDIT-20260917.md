# 页面文案审核与定稿 — 2026-09-17

结论：当前页面的方向符合购买引导目标，主要问题集中在少数抽象问法、书面表达和重复检查提示。采用 12 处局部调整；保留模块、商品字段、CTA、服务来源组件和四个 FAQ。文案定稿已写入 LOCKED-COPY.md，DeepSeek 已接入 HTML；Codex 最终核对通过。下文记录文案定稿时的审核依据。

## 页面价值判断

这页要帮助用户判断自己的房间能装哪类空调、是否值得承担固定安装费用，再进入对应商品。衡量一句话是否有用，看它能否帮助用户排除不适合的选项、理解真实取舍或继续购物。自然的电商文案可以简洁、直接并包含购买动作；无需刻意加入个人经历、随意语气或俏皮句。

现有“比较 → 商品 → 可展开解释 → 服务 → FAQ/购物入口”满足这个目标。无需新增教育模块、更多 FAQ、文案副标题或 SEO 段落。此次修订片段的词数从380变为388（含问题标题），增加来自把模糊指代写清楚；不是整页扩写，也不以删字数量衡量质量。

## 实际检查范围

从当前 HTML 提取225条文本记录，包括标题、meta description、段落、商品字段、完整型号、链接、按钮、折叠内容和非空alt；存在嵌套文本记录，因此225并非独立句子数。检查了三个商品面板，而非只看首屏或默认Tab。

| 部分 | 结论与处理 |
|---|---|
| Title / meta / H1 | 保留。主题明确，元描述说明比较维度和商品路径，没有夸大收益。 |
| Hero | 调整一句。把 everyday comfort 落到 noise，明确用于选择房间空调。H1和无按钮布局保持。 |
| 三品类比较 | 保留。短标签与重复的Setup/Upfront是便于对照的UI，不能当作模板腔删除。Usually lower upfront的限定保留。 |
| 商品区 / 三Tab / 11卡 | 保留。系列、BTU、SACC、ASHRAE、Up to、电压、能效、价格、型号及商品链接属于事实；标题中品牌原有的Ultra Quiet或Drainage-Free不作为全品类承诺扩写。 |
| 安装解释 | 问题点明installation；答案合并重复的permission/manual提示，保留室外位置、穿墙、排水、电气、窗体支撑和室外排风。 |
| 噪音解释 | 问题改为房间噪音的影响因素；答案前三句有效，保留，仅简化末句测试条件表达。 |
| 评级解释 | 问题点明BTU和efficiency；将容量是否适合房间与不同能效测试口径拆开说明。保留DOE/Energy Star原链接。 |
| 安装投入解释 | 明确mini split与installation cost；less initial commitment改为有条件的前期费用判断；保留可能无法回本的限制。 |
| 服务 | 保留用户指定的Premium Della Services及四项来源文案。现有句子已明确链接用途，未承诺免费配送、任意退货或全产品相同保修。 |
| FAQ租房 | 保留问题，解释permitted/compatible为设备适配和楼宇允许两件事。 |
| FAQ窗户 | 保留问题，把model-specific checks和feasible换成检查窗体要求、是否能安装；室外排热前提仍明确。 |
| FAQ两个关门房间 | 整题保留。直接指出气流限制并给出各房间/多区路径；Not reliably是回答真实问题，非刻意的戏剧性短句。 |
| FAQ冬季采暖 | 保留问题，将heat load解释为房间所需热量，用minimum operating temperature代替带审稿语气的claim；保留低温输出和备用热源判断。 |
| 收尾 / CTA / alt /窗体补充 | 保留。购物入口和图像说明功能清楚，不为避免常见词而改掉已批准标签。 |

## 代表性调整

| 原文 | 定稿 | 读者收益 |
|---|---|---|
| What needs to fit? | What does installation involve? | 不展开也能知道解释什么。 |
| Where will you hear the equipment? | What affects noise in the room? | 直接对应日常使用疑问。 |
| How should you compare ratings? | How do BTU and efficiency ratings differ? | 区分容量和效率。 |
| When is a permanent system worth considering? | When is a mini split worth the installation cost? | 点明设备和付出。 |
| less initial commitment | may cost less upfront | 明确费用，并保留不确定性。 |
| permitted, compatible window or venting arrangements | a window or venting setup that fits the model and is allowed by your building | 把压缩在形容词中的两个条件说清楚。 |

完整旧文/新文/DOM定位/修改原因见 copy-replacements-20260917.json。12处中包括4个问题标题、Hero一句、4个Evidence答案和3个FAQ答案。

## 使用的编辑标准

- 用户指定 [humanizer](C:/Users/18041/Desktop/skills/humanizer/SKILL.md)：先判断内容和表达问题，保留事实、必要限制和品牌已批准表达。
- 用户指定 [stop-slop](C:/Users/18041/Desktop/skills/stop-slop/SKILL.md)：对同一份修订稿做句子层面的精简，不再重写一遍。
- 已读取 [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) 当前页面。该页是观察性建议，部分条目针对维基语境；本次用于检查空泛分析和程式化表达，不作为AI作者鉴定或电商禁词表。

没有依据单个词、三列对比、问答标题或语法整齐推断“AI率”。没有发现需清理的聊天尾句、伪造引用、占位符或工具引用标记。站内技术内容仅在原有已核对事实范围内改写，此轮不等同于重新核实实时价格、保修政策或HVAC性能。

## 保留条件与验收

12条旧文在当前HTML各出现一次，且与原LOCKED-COPY逐条匹配；新文均为定稿。核对may、房间范围、安装许可、向室外排热、噪音测量条件、SACC比较口径、SEER2/CEER不可直接比数值及低温热量限制，未增加效率百分比、节能承诺或绝对优劣。

当前HTML比提交1baf1c3多两条手机Tab布局样式。本次没有修改HTML，实施时应从当前工作文件继续，保留这两条样式。图片、商品JSON及交互逻辑不在文案改动范围内。审稿依据指纹与清单在qa/copy-review-20260917。
