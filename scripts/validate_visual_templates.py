#!/usr/bin/env python3
"""Lightweight preflight for Rustfield visual templates.

This intentionally checks structure and delivery contracts rather than pixel
similarity. It is safe to run without installing third-party packages.
"""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"


def fail(errors: list[str], path: Path, message: str) -> None:
    errors.append(f"{path.name}: {message}")


def main() -> int:
    errors: list[str] = []
    html_files = sorted(TEMPLATES.glob("*.html"))
    if not html_files:
        print("FAIL: templates directory is empty")
        return 1

    for path in html_files:
        html = path.read_text(encoding="utf-8")
        name = path.name

        for src in re.findall(r'<img[^>]+src="([^"]+)"', html):
            if not src.startswith(("data:", "http://", "https://", "${")) and not (path.parent / src).exists():
                fail(errors, path, f"图片路径不可用：{src}")

        if not re.search(r"<!doctype html>", html, re.I):
            fail(errors, path, "缺少 <!doctype html>")
        if "prefers-reduced-motion" not in html:
            fail(errors, path, "缺少 prefers-reduced-motion 降级")

        if name == "cards-3x4.html":
            required = {
                'width:1080px': "卡片宽度不是 1080px",
                'height:1440px': "卡片高度不是 1440px",
                'data-card': "缺少可切换的卡片标记",
                'exportCurrentCard': "缺少单卡导出入口",
                'exportAllCards': "缺少整组导出入口",
            }
            for needle, message in required.items():
                if needle not in html:
                    fail(errors, path, message)

        elif name == "wechat-article.html":
            required = {
                '677px': "公众号预览没有 677px 阅读宽度",
                'copyInlineArticle': "缺少公众号片段复制入口",
                'articleData': "缺少可替换的文章数据对象",
                '<section': "缺少 section 文章结构",
            }
            for needle, message in required.items():
                if needle not in html:
                    fail(errors, path, message)

        elif name == "soft-retro-visual-handbook.html":
            required = {
                '完整视觉规范': "缺少完整手册标题或定位",
                'motion-toggle': "缺少动效暂停控制",
                'atlas': "缺少组件图谱展示",
                '@keyframes': "缺少动效示例",
                '1080×1440': "缺少 3:4 小红书格式说明",
                '677px': "缺少公众号格式说明",
                'Applied Tutorial Example': "缺少完整横向教程应用示例",
                'assets/reference-folder-alpha.png': "缺少透明参考文件夹素材",
                'assets/silver-metal-star-alpha.png': "缺少透明灰银金属素材",
                'assets/chrome-cursor-alpha.png': "缺少透明银灰光标素材",
                '--gradient-blue-pink:': "缺少统一的柔和蓝粉渐变 Token",
                '--window-major-border:': "缺少统一的大窗口机身 Token",
                'class="route-arrow': "缺少自适应关系轨道",
                'class="tree-branches"': "缺少结构化决策树分支",
                'class="window tutorial-window"': "教程示例缺少复古窗口结构",
                'class="hero-diagram relationship"': "顶部关系示例缺少稳定的结构",
                'class="window window-major hero-window"': "缺少大窗口灰色立体外框",
                'filled-pink': "缺少纯信号粉按钮",
                'filled-blue': "缺少纯编辑蓝按钮",
                '.mechanism-grid{grid-template-columns:1fr}': "窄屏下信息关系仍会被压成双栏",
            }
            for needle, message in required.items():
                if needle not in html:
                    fail(errors, path, message)
            if html.count('class="atlas-item"') != 52:
                fail(errors, path, "组件图谱必须保留 52 个组件族")
            if html.count('data-window-variant=') != 6:
                fail(errors, path, "窗口外观选择必须保留 6 种")
            if html.count('class="tree-branch-wrap') != 3:
                fail(errors, path, "决策树必须保留 3 条结构化分支")
            if "connector-layer" in html or "marker-end=" in html:
                fail(errors, path, "关系组件不得继续使用固定坐标覆盖层")
            if re.search(r'<mark\b(?![^>]*class="signal-mark")', html):
                fail(errors, path, "存在未声明 signal-mark 的浏览器默认高亮")
            if re.search(r'(?:background|fill)\s*[:=]\s*["\']?(?:yellow|#ff0(?:000)?|#ffff00)', html, re.I):
                fail(errors, path, "存在不属于系统的黄色高亮")
            if re.search(r'fill\s*=\s*["\'](?:#000(?:000)?|black)["\']', html, re.I):
                fail(errors, path, "数据图表存在纯黑色实心图层")

        elif name != "template-index.html":
            for pattern, message in {
                r'class="[^"]*\bscreen\b[^"]*"': "缺少页面屏幕容器",
                r'class="[^"]*\btitlebar\b[^"]*"': "缺少窗口标题栏",
                r'(?:class="[^"]*\bcontrols\b[^"]*"|class="[^"]*\bwindow-controls\b[^"]*")': "缺少窗口控制符",
            }.items():
                if not re.search(pattern, html):
                    fail(errors, path, message)

    if errors:
        print("FAIL: Rustfield 模板结构检查未通过")
        print("\n".join(f"- {error}" for error in errors))
        return 1

    print(f"PASS: {len(html_files)} 个模板通过结构、格式与动效降级检查")
    return 0


if __name__ == "__main__":
    sys.exit(main())
