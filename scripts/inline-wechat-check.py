#!/usr/bin/env python3
"""Check the final HTML fragment intended for a WeChat editor.

Run this against the copied fragment, not against wechat-article.html itself.
The preview workbench is allowed to contain div/style/script; the delivered
fragment is deliberately much smaller and uses inline styles only.
"""

from pathlib import Path
import re
import sys


FORBIDDEN = (
    r"<\s*(?:html|head|body|main|article|figure|div|style|script|button|link)\b",
    r"\bclass\s*=",
    r"\bid\s*=",
    r"<\s*style\b",
    r"<\s*script\b",
)


def main() -> int:
    if len(sys.argv) != 2:
        print("用法：python3 scripts/inline-wechat-check.py /path/to/fragment.html")
        return 2

    path = Path(sys.argv[1]).expanduser()
    if str(path) == "/dev/stdin":
        html = sys.stdin.read()
    elif not path.is_file():
        print(f"FAIL: 找不到片段文件：{path}")
        return 1
    else:
        html = path.read_text(encoding="utf-8")
    errors: list[str] = []
    if "<section" not in html:
        errors.append("最终片段至少应包含一个 section")
    if "style=" not in html:
        errors.append("公众号片段必须使用 inline style")
    if "677px" not in html:
        errors.append("文章结构应保留 677px 阅读宽度契约")
    for pattern in FORBIDDEN:
        if re.search(pattern, html, re.I):
            errors.append(f"包含不适合直接粘贴的结构：{pattern}")

    if errors:
        print("FAIL: 公众号 inline 片段检查未通过")
        print("\n".join(f"- {error}" for error in errors))
        return 1

    print(f"PASS: {path.name if str(path) != '/dev/stdin' else 'stdin'} 可作为公众号 inline HTML 片段继续处理")
    return 0


if __name__ == "__main__":
    sys.exit(main())
