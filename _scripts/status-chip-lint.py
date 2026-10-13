#!/usr/bin/env python3
"""Gate chip trạng thái — tên bước và nhãn trạng thái không vượt chỗ của Chip trạng thái.

Rule: design/ui-common/screen-patterns.md § CMP-09 R18 + design/design.md § Ánh xạ trạng thái nghiệp vụ.
Thẻ bước desktop (giãn 290–360) chứa tên + mã bên trái và Chip trạng thái bên phải; thẻ mobile 156×56 chỉ có
tên + chữ trạng thái màu (không chip). Tên bước và nhãn trạng thái quá MAX_CHARS thì chip đè hoặc cắt tên/mã,
chữ mobile tràn thẻ — chặn từ tài liệu.

Kiểm:
  1. `*-states.md`: nhãn hiển thị trong khối stateDiagram (`Ma : Nhãn`). Mục `## State:` có dòng
     `<!-- chip-the-buoc: khong -->` thì bỏ qua (đối tượng không bao giờ là một bước trên cây quy trình).
  2. Mọi bảng có cột "Bước" và cột "Tạo từ" (bảng liên quy trình): ô cột Bước.

Dùng:  python3 _scripts/status-chip-lint.py [file.md ...]   (không tham số = quét docs/)
Thoát 1 khi có FAIL.
"""
import re
import sys
import unicodedata
from pathlib import Path

MAX_CHARS = 14
SKIP_MARK = "<!-- chip-the-buoc: khong -->"
ROOT = Path(__file__).resolve().parent.parent


def nlen(s: str) -> int:
    return len(unicodedata.normalize("NFC", s.strip()))


def check_states(path: Path, lines: list[str]) -> list[str]:
    out, section, skip, in_diagram = [], "", False, False
    for i, line in enumerate(lines, 1):
        if line.startswith("## State:"):
            section, skip, in_diagram = line[3:].strip(), False, False
            continue
        if SKIP_MARK in line:
            skip = True
        if line.strip().startswith("```mermaid"):
            in_diagram = True
            continue
        if in_diagram and line.strip().startswith("```"):
            in_diagram = False
            continue
        if not in_diagram or skip or "-->" in line:
            continue
        m = re.match(r"^\s+([A-Za-z_][\w]*)\s*:\s*(.+?)\s*$", line)
        if m and nlen(m.group(2)) > MAX_CHARS:
            out.append(f"FAIL {path}:{i} [{section}] nhãn \"{m.group(2)}\" {nlen(m.group(2))} ký tự > {MAX_CHARS}")
    return out


def cells(row: str) -> list[str]:
    return [c.strip() for c in row.strip().strip("|").split("|")]


def check_step_tables(path: Path, lines: list[str]) -> list[str]:
    out, col = [], None
    for i, line in enumerate(lines, 1):
        if not line.lstrip().startswith("|"):
            col = None
            continue
        cs = cells(line)
        if col is None:
            low = [c.lower() for c in cs]
            if "bước" in low and "tạo từ" in low:
                col = low.index("bước")
            continue
        if set(line.replace("|", "").strip()) <= set("-: "):
            continue
        name = re.sub(r"[`*_\[\]]", "", cs[col]) if col < len(cs) else ""
        if name and nlen(name) > MAX_CHARS:
            out.append(f"FAIL {path}:{i} tên bước \"{name}\" {nlen(name)} ký tự > {MAX_CHARS}")
    return out


def main(argv: list[str]) -> int:
    files = [Path(a).resolve() for a in argv] or sorted((ROOT / "docs").rglob("*.md"))
    fails, checked = [], 0
    for f in files:
        if any(p.startswith("zz-") for p in f.parts):
            continue
        lines = f.read_text(encoding="utf-8").splitlines()
        rel = f.relative_to(ROOT) if ROOT in f.parents else f
        if f.name.endswith("-states.md"):
            fails += check_states(rel, lines)
            checked += 1
        fails += check_step_tables(rel, lines)
    for line in fails:
        print(line)
    print(f"status-chip-lint: {len(fails)} FAIL · {checked} states.md · giới hạn {MAX_CHARS} ký tự")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
