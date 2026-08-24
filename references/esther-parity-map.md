# Esther → Rustfield 对照表

这份表记录对 Esther 设计系统的结构性借鉴。借鉴的是“如何把审美变成可执行系统”的方法，不复制 Esther 的品牌身份、颜色、字体、头像、Logo、IP 或具体模板代码。

| Esther 层级 | Esther 内容 | Rustfield 对应 | 处理结论 |
| --- | --- | --- | --- |
| Skill workflow | 7 步：澄清、读规范、拷模板、选布局、选组件、自检、交付 | `SKILL.md` + `scene-router.md` + `template-authoring.md` | 保留流程，增加 16:9 / 3:4 / 公众号格式路由 |
| Brand DNA | 颜色、字体、气质、头像、禁忌、间距、响应式 | `brand-dna.md` + `tokens.md` | 新增独立品牌层，完全使用 Rustfield token |
| Tutorial scene | 教程页面的色板、布局、动画和内容语气 | `scene-tutorial.md` + 现有 16:9 模板 | 归档现有成果，不重新做第二套窗口 |
| Landing scene | Hero、价值、证据、CTA、动效 | `scene-landing.md` + `landing-16x9.html` | 补齐一个起始模板 |
| App scene | 侧栏、工作区、Tab、Modal、Canvas | `scene-app.md` + `app-16x9.html` | 补齐为 Rustfield 的单窗口工作区 |
| Cards scene | 1080×1440、多页卡片、导出、封面/内容/尾页 | `scene-cards.md` + `cards-3x4.html` | 迁移规格与工作流，重做视觉 |
| WeChat scene | 677px、section-only、内联样式、base64、手动断行 | `scene-wechat.md` + `wechat-article.html` | 迁移输出约束，保持 Rustfield 文章气质 |
| Layouts | 16 种布局模式 | `layout-atlas.md` | 扩展为 16 种并增加格式适用标签 |
| Components | 52 个组件家族 | `component-catalog.md` + `components.md` | 完整列出并分为启用、条件启用、避免；核心组件保留详细语法 |
| Templates | tutorial / landing / app / cards / wechat | `templates/*.html` | 5 类输出都提供可直接打开的起始文件 |
| Checklist | P0 / P1 / P2 质量分级 | `quality-gate.md` + validators | 增加尺寸、断行、导出和公众号兼容检查 |

## 组件迁移原则

- Esther 的杂志卡片、编号、Pull Quote、流程条、Do/Don't、时间线、Tab、Canvas、签名档等信息关系适合迁移。
- Esther 的黄底、衬线字体、深色卡片、红色圆点和 bounce 动效不迁移；对应地改为 Rustfield 的粉蓝标记、灰色窗口、银灰语义物和低频进入。
- Esther 的交互组件只有在目标输出允许交互时启用：16:9 播放页和 HTML 预览可用，公众号复制产物和 PNG 卡片禁用。
- 3D 物件不作为组件数量补足，只有内容关系能解释时才启用。
