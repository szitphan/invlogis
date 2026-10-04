#!/usr/bin/env python3
"""Áp bố cục thư mục của dự án lên mọi tham chiếu đường dẫn (D-04, D-05 trong _guides/pipeline.md).

Kit cài từ ngoài (BA-Kit, figma-skills, design-system-astryx) gõ cứng đường dẫn cũ
(`docs/design.md`, `docs/_shared/changelog.md`...). Chạy lại script này SAU MỖI LẦN cài hoặc
cập nhật kit để đổi sang bố cục của dự án — idempotent, chạy nhiều lần không hỏng.

  python3 _scripts/relayout.py            # sửa file
  python3 _scripts/relayout.py --check    # chỉ liệt kê file còn đường dẫn cũ, exit 1 nếu có

Không đụng: lịch sử (`_workspace/changelog.md`, `_workspace/staleness.md`), `.git/`,
`node_modules/`, bản gốc khách gửi (`docs-input/**/source/`), graph KG (build lại).
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Thứ tự quan trọng: đường dẫn dài/cụ thể trước.
MAP = [
    ("docs/_shared/screen-patterns.md", "design/ui-common/screen-patterns.md"),
    ("docs/_shared/conventions.md", "design/ui-common/conventions.md"),
    ("docs/_shared/images/", "design/ui-common/images/"),
    ("docs/_shared/changelog.md", "_workspace/changelog.md"),
    ("docs/_shared/staleness.md", "_workspace/staleness.md"),
    ("docs/_shared/backlog.md", "_workspace/backlog.md"),
    ("docs/_shared/.status-state", "_workspace/.status-state"),
    ("docs/_shared/kg", "_workspace/kg"),
    ("docs/design-tokens.css", "design/design-tokens.css"),
    ("docs/design.md", "design/design.md"),
    ("docs/components.md", "design/components.md"),
    ("docs/ba-crosswalk.md", "design/ba-crosswalk.md"),
    ("docs/figma-library-keys.json", "design/figma-library-keys.json"),
    ("docs/setup-figma.md", "design/setup-figma.md"),
    ("docs/design-backlog.md", "design/design-backlog.md"),
    ("docs/workflow-figma-screen.md", "_guides/workflow-figma-screen.md"),
    ("docs/pipeline.md", "_guides/pipeline.md"),
]

SCAN_DIRS = [".claude", ".agents", ".codex", "_templates", "_scripts", "_guides",
             "design", "docs", "docs-input", "_workspace"]
SCAN_FILES = ["CLAUDE.md", "AGENTS.md", ".gitignore"]
TEXT_EXT = {".md", ".mjs", ".js", ".py", ".sh", ".json", ".toml", ".html", ".css", ".yaml",
            ".yml", ".txt", ".puml", ".d2", ""}
SKIP_DIRS = {".git", "node_modules", "source", ".staging", "__pycache__", ".status-state"}
SKIP_FILES = {
    "_workspace/changelog.md", "_workspace/staleness.md",
    "_scripts/relayout.py",
}


def iter_files():
    for f in SCAN_FILES:
        p = os.path.join(ROOT, f)
        if os.path.isfile(p):
            yield p
    for d in SCAN_DIRS:
        base = os.path.join(ROOT, d)
        for cur, dirs, files in os.walk(base):
            dirs[:] = [x for x in dirs if x not in SKIP_DIRS]
            for name in files:
                if os.path.splitext(name)[1] in TEXT_EXT:
                    yield os.path.join(cur, name)


def main():
    check = "--check" in sys.argv
    changed = []
    for path in iter_files():
        rel = os.path.relpath(path, ROOT)
        if rel in SKIP_FILES:
            continue
        try:
            text = open(path, encoding="utf-8").read()
        except (UnicodeDecodeError, OSError):
            continue
        new = text
        for old, dst in MAP:
            new = new.replace(old, dst)
        if new != text:
            changed.append(rel)
            if not check:
                open(path, "w", encoding="utf-8").write(new)
    verb = "Còn đường dẫn cũ ở" if check else "Đã đổi đường dẫn trong"
    print(f"{verb} {len(changed)} file")
    for rel in changed:
        print("  " + rel)
    sys.exit(1 if (check and changed) else 0)


if __name__ == "__main__":
    main()
