# 动效配方

这份配方把 Rustfield Soft Retro Visual 的动效拆成可以复用的节奏单元。动效的职责是说明“先看哪里、事情如何推进、哪个状态正在变化”，不是让页面持续热闹。

## 使用顺序

1. 先确定这一屏唯一的主要机制，再决定是否需要动效。
2. 只选择一个主配方，最多加一个辅助配方。
3. 先做静态状态，再加进入、推进或聚焦动作。
4. 在 `prefers-reduced-motion` 下保留最终状态，不让内容消失或变得不可读。

## 配方总表

| 配方 | 用来表达 | 推荐节奏 | 可连续循环？ |
| --- | --- | --- | --- |
| `window-enter` | 页面进入、窗口落定 | 120–220ms | 否 |
| `text-sequence` | 建立阅读顺序 | 每项间隔 40–90ms | 否 |
| `flow-signal` | 流程从当前步骤推进到下一步 | 420–760ms | 否 |
| `focus-pulse` | 标出一个证据或关键点 | 1.6–2.4s | 可，低频 |
| `chart-reveal` | 让趋势线逐步出现 | 520–900ms | 否 |
| `soft-float` | 给有语义的小物件空气感 | 6–10s | 可 |
| `silver-rotation` | 展示真实银灰 3D 物件的体积 | 12–24s | 可 |
| `crt-local` | 进入屏幕、素材或转场 | 180–360ms | 否 |

## 01 / WINDOW ENTER

适用于主窗口整体进入。窗口作为一个整体落定，不把标题栏、正文、按钮拆成互相竞争的入场动画。

```css
.window-enter {
  animation: window-enter 180ms cubic-bezier(.2,.8,.2,1) both;
}

@keyframes window-enter {
  from { opacity:0; transform:translateY(10px); }
  to { opacity:1; transform:translateY(0); }
}
```

## 02 / TEXT SEQUENCE

适用于主标题、辅助说明、主要机制的阅读顺序。标题先出现，说明随后，装饰最后或不出现。

```css
.sequence-item { animation: text-in 180ms ease-out both; }
.sequence-item:nth-child(2) { animation-delay:60ms; }
.sequence-item:nth-child(3) { animation-delay:120ms; }

@keyframes text-in {
  from { opacity:0; transform:translateY(5px); }
  to { opacity:1; transform:translateY(0); }
}
```

## 03 / FLOW SIGNAL

适用于流程轨道。只让粉色信号、当前节点或指针推进一次；不要让所有节点持续闪烁。

```css
.flow-signal { position:relative; }
.flow-signal::after {
  content:"";
  position:absolute;
  left:0;
  top:50%;
  width:12px;
  height:12px;
  border-radius:50%;
  background:var(--pink);
  transform:translate(-50%,-50%);
  animation: signal-move 620ms ease-in-out both;
}

@keyframes signal-move {
  from { left:0; }
  to { left:100%; }
}
```

## 04 / FOCUS PULSE

适用于局部证据、一个关键词或一个结论点。呼吸感应该很轻，静态状态也要有清晰边界。

```css
.focus-pulse {
  animation: focus-pulse 2s ease-in-out infinite;
}

@keyframes focus-pulse {
  0%,100% { box-shadow:0 0 0 0 rgb(240 138 183 / .10); }
  50% { box-shadow:0 0 0 7px rgb(240 138 183 / .18); }
}
```

## 05 / CHART REVEAL

适用于一条趋势线或一个关键点。坐标、网格先稳定，数据线随后出现，粉色点最后落在结论位置。不要用黑色实心几何块代替数据。

```css
.chart-line {
  stroke-dasharray:420;
  stroke-dashoffset:420;
  animation: chart-reveal 760ms ease-out 120ms forwards;
}

@keyframes chart-reveal { to { stroke-dashoffset:0; } }
```

## 06 / SOFT FLOAT

适用于有语义的小物件：资料文件夹、回形针、轨道环或经过清理的透明素材。它不能挡住标题，也不能让抽象色球成为默认装饰。

```css
.soft-float {
  animation: soft-float 8s ease-in-out infinite;
}

@keyframes soft-float {
  0%,100% { transform:translateY(6px); }
  50% { transform:translateY(-6px); }
}
```

## 07 / SILVER ROTATION

只给真实的银灰 3D 素材使用。材质需要有体积、明确的光线与干净的透明边缘；如果只是 CSS 做出的平面图形，就不要把它称作 3D。

```css
.silver-rotation {
  animation: silver-rotation 18s ease-in-out infinite;
  transform-origin:center;
}

@keyframes silver-rotation {
  0%,100% { transform:rotate(-4deg); }
  50% { transform:rotate(4deg); }
}
```

## 08 / CRT LOCAL

CRT 只作为局部屏幕、素材对比或转场纹理。推荐短暂出现后稳定，不要让扫描线一直穿过正文。

```css
.crt-local::after {
  content:"";
  position:absolute;
  inset:0;
  pointer-events:none;
  opacity:.35;
  background:repeating-linear-gradient(
    0deg,
    transparent 0 5px,
    rgb(49 88 158 / .10) 5px 6px
  );
  animation: crt-in 240ms ease-out both;
}

@keyframes crt-in {
  from { opacity:0; }
  to { opacity:.35; }
}
```

## HTML 与 Remotion 的对应关系

HTML 原型可以先用上面的 CSS 验证节奏。进入 Remotion 或 HyperFrames 后，把每个配方当成一个时间段：用帧驱动 `opacity`、`translateY`、`strokeDashoffset` 或旋转角度，保持同样的总时长和先后顺序。不要把 CSS 的无限循环直接搬进视频导出；视频里应该给循环设定明确的入场、停留和离场区间。

## 动效自检

- 关掉动效后，主标题、正文和关系仍然完整可读。
- 动效是否解释了顺序、选择、证据、变化或气氛中的至少一个？
- 是否只有一个动作在争夺当前注意力？
- 漂浮／旋转是否低频、低振幅，并远离正文基线？
- 真实 3D 素材的阴影方向是否和窗口一致？
- 是否已经提供 `prefers-reduced-motion` 降级？
