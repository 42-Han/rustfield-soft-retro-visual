---
name: soft-retro-visual
description: "为 Rustfield 个人内容制作粉蓝灰、复古窗口结构、现代酸性细节的视觉页面与 HTML 演示。适用于 AI/设计教程、横向视频画面、落地页、知识分享页、图文卡片和 PPT；当需要统一色彩、组件、版式、动效或进行去 AI 味视觉审查时使用。"
---

# Rustfield Soft Retro Visual

用这套视觉系统制作时，优先让人感到“有趣、有审美、有判断”。复古窗口只是信息结构，不是整页的装饰。现代感来自粉蓝配色、编辑式留白、少量精致的材质和有节奏的动效。

## 工作流程

1. 先读 [品牌 DNA](references/brand-dna.md)，确认 Rustfield 的颜色、字体、气质、IP 与禁忌；需要了解系统如何借鉴 Esther 时，再读 [对照表](references/esther-parity-map.md)。
2. 明确介质：横向 16:9 教程、演示页面、Landing、App 型页面、1080×1440 小红书图文、公众号文章或 PPT。
3. 从 [场景路由](references/scene-router.md) 选择本次内容的输出场景；再从 [布局图谱](references/layout-atlas.md) 选一个结构。不要为一页内容同时套多个版式。
4. 写清这一页唯一要传达的观点，再从流程、树状决策、对比、引用、数据叙事或演示中选一种内容机制。不要在同一屏混用多种机制。
5. 阅读 [色彩与材质](references/tokens.md)；再按需要加载[组件](references/components.md)、[组件目录](references/component-catalog.md)、[信息组织](references/information-forms.md)、[版式](references/composition.md)或[动效](references/motion.md)。
6. 对 16:9 按“四层页面语法”搭建：底图 → 一个灰色窗口 → 信息 → 可选点睛物。3:4 与公众号读取各自的场景规范，不强行套横向窗口。
7. 最后运行 `scripts/validate_visual_templates.py`；如果是公众号交付，再对最终 section 片段运行 `scripts/inline-wechat-check.py`，并执行[质量检查](references/quality-gate.md)。不通过检查时，先删减标签、嵌套卡片和无意义效果，再增加元素。

## 核心规则

- 一屏只保留一个主标题、一句辅助说明和一个主要内容机制。
- 横向教程播放优先采用单幕演示：默认只显示一个场景，通过点击当前画面或方向键／空格键推进，不要求观众连续滚动页面，也不额外堆叠底部控制栏。
- 窗口分为三层：最大层级使用有厚度的灰色机身并嵌入标题栏与三枚控制符；中间层级保留标题栏和内容面；小层级可以省略标题栏，只保留灰色、粉色或透明细框。三层不能混成同一种重量。
- 窗口颜色提供蓝色、粉色、灰色、蓝粉渐变、灰色渐变和银色框等选择；先保证文字对比和画面层级，再按内容气质自由组合，不把某一种颜色机械绑定到固定用途。
- 品牌收尾标签只在需要强化个人记忆点时使用；每个标签保持独立、短小、圆角贴纸质感，避免拉成一条横向分隔栏。
- 使用粉蓝作为独立信息信号；蓝粉渐变只用于低对比底纹、转场面或明确选择的窗口外观，并经过低饱和中间色柔和过渡，不用于正文强调。
- 深蓝默认只用于主窗口标题栏和一个当前状态；次级窗口可用灰、粉或浅蓝，不让深蓝占据整张画面。
- 阴影只用于最外层主窗口、必要的重点物件，以及需要“窗口机身感”的次级窗口；次级窗口采用低饱和蓝/粉环境影与内高光，避免硬灰色投影或每个元素都浮起。
- 将复古感放在窗口比例、灰色斜面和标题栏上；将现代感放在留白、配色和高质量三维材质上。
- 使用 3D 物件前，先说明它为什么出现：解释工具、指向步骤、形成关键记忆点或建立气氛。
- 3D 点缀必须和内容建立关系：优先复用视觉手册中的透明素材（`assets/reference-folder-alpha.png`、`assets/silver-metal-star-alpha.png`、`assets/chrome-cursor-alpha.png`）；文件夹表示收集与归类，星体表示转折与记忆点，光标表示选择与路径。只有在确实需要空间记忆时才补充其他 3D 物件。孤零零的球体、轨道环和无指向星星一律删除。材质要有高光路径和统一光向，默认不混入粉蓝渐变或彩虹反光。
- 不使用默认霓虹光晕、廉价金属贴纸、密集小字、无理由的卡片嵌套或通用“AI 控制台”界面。

## 按任务读取参考

- 需要确定配色、背景和材质：读 [tokens.md](references/tokens.md)。
- 需要确定品牌基因或替换个人身份：读 [brand-dna.md](references/brand-dna.md)。
- 需要搭建页面或 HTML：读 [components.md](references/components.md) 与 [composition.md](references/composition.md)。
- 需要完整组件选择：读 [component-catalog.md](references/component-catalog.md)。
- 需要决定内容做成教程、演示、网页或卡片：读 [scene-router.md](references/scene-router.md) 与 [layout-atlas.md](references/layout-atlas.md)。
- 需要做横向教程：读 [scene-tutorial.md](references/scene-tutorial.md)。
- 需要做 Landing 或 App 型页面：读 [scene-landing.md](references/scene-landing.md) 或 [scene-app.md](references/scene-app.md)。
- 需要做 1080×1440 小红书图文：读 [scene-cards.md](references/scene-cards.md)，从 [cards-3x4.html](templates/cards-3x4.html) 开始。
- 需要做公众号文章：读 [scene-wechat.md](references/scene-wechat.md)，从 [wechat-article.html](templates/wechat-article.html) 开始。
- 需要从零开始搭一页或选择现成页面结构：读 [模板使用说明](references/template-authoring.md)。
- 需要直接翻看整套视觉系统：打开 [完整视觉手册](templates/soft-retro-visual-handbook.html)；它是连续阅读的可视化规范，不是目录页。
- 需要表达流程、树状关系、对比或数据：读 [information-forms.md](references/information-forms.md)。
- 需要处理证据标注、图表分层或外部组件方法：读 [reference-translation.md](references/reference-translation.md)。
- 需要加漂浮、CRT 或镜头感：读 [motion.md](references/motion.md) 与 [动效配方](references/motion-recipes.md)。
- 准备交付或需要审美复核：读 [quality-gate.md](references/quality-gate.md)。

## 输出要求

说明本页的主观点与采用的内容机制；列出使用的关键 Token 和组件；当有动效或特殊材质时，说明它如何不干扰信息层级。交付 HTML 时，保留静态可读状态并提供 `prefers-reduced-motion` 降级。
