# 外部参考转译

这份参考不是复制代码或视觉品牌，而是记录哪些开源项目的结构方法值得转译到 Rustfield。

## 证据与局部标注

- [react-image-annotation](https://github.com/Secretmapper/react-image-annotation) 将矩形、点和椭圆标注作为独立覆盖层处理。转译到 Rustfield：证据画面保持完整，框选只指出一个局部；解释文字要么作为证据外的独立说明，要么完整放进标注框，不让文字压在证据边界上。
- [Excalidraw](https://github.com/excalidraw/excalidraw) 把图像、形状、箭头和文本视为可组合的画布元素。转译到 Rustfield：只保留一个主要证据和一个局部标注，不把证据页做成截图墙或无限画布。

## 图表与数据叙事

- [Observable Plot](https://github.com/observablehq/plot) 使用分层图形语法组织数据。转译到 Rustfield：底图网格、背景面积、趋势线、重点点位和文字注释分层；每层都降低对比度，只有一个结论使用粉色强调。
- [Recharts](https://github.com/recharts/recharts) 将坐标轴、网格、线条和标记拆成可组合部件。转译到 Rustfield：不要用深色实心几何块替代数据；结构线用浅灰蓝，背景面积使用低透明度，数据线用单一粉色，标记点保留空气感。

## 关系图与组件系统

- [xyflow](https://github.com/xyflow/xyflow) 的核心是节点与边的关系，而不是卡片本身。转译到 Rustfield：流程、树和关系画布必须先明确连接关系，再设计节点外观；箭头和连接线不能被内容卡片挤成装饰线。
- [Figma Simple Design System](https://github.com/figma/sds) 将基础原子、布局组合和页面示例分层组织。转译到 Rustfield：Skill 文档保持“Token → 组件 → 布局 → 场景模板”的顺序，避免每个模板各自发明一套样式。

## Rustfield 的保留判断

- 外部项目提供的是结构方法，不改变 Rustfield 的粉蓝灰配色、灰色复古窗口、低密度排版和去 AI 味原则。
- 图表页不做通用仪表盘；证据页不做通用标注工具；比较页不做卡片堆叠。所有形式仍然服务于一页一个观点。
