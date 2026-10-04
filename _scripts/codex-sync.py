#!/usr/bin/env python3
"""Sinh bản Codex từ nguồn Claude — KHÔNG sửa tay bản Codex, sửa `.claude/` rồi chạy lại.

Nguồn (sửa ở đây)              → Bản Codex (máy sinh)
  .claude/skills/**              → .agents/skills/**        (chép nguyên, chỉ viết lại đường dẫn tương đối)
  .claude/agents/*.md            → .codex/agents/*.toml     (name + description + developer_instructions)
  CLAUDE.md                      → AGENTS.md                (thêm khối ghi chú Codex ở đầu)

Đường dẫn:
  * Đường dẫn tuyệt đối từ gốc repo (`.claude/rules/...`, `.claude/skills/kg/engine/...`) GIỮ NGUYÊN —
    file thật nằm ở đó, Codex đọc được. KHÔNG đổi thành `.Codex/...` (thư mục đó không tồn tại).
  * Đường dẫn tương đối (`../../rules/x.md`) được tính lại từ vị trí bản sao để vẫn trỏ đúng file gốc.
  * `rules/`, `hooks/`, `scripts/` dùng chung, không chép.

Chạy:
  python3 _scripts/codex-sync.py           # ghi
  python3 _scripts/codex-sync.py --check   # chỉ kiểm, exit 1 nếu bản Codex lệch nguồn
"""
import os
import re
import shutil
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC_SKILLS = ROOT / ".claude/skills"
DST_SKILLS = ROOT / ".agents/skills"
SRC_AGENTS = ROOT / ".claude/agents"
DST_AGENTS = ROOT / ".codex/agents"
SRC_GUIDE = ROOT / "CLAUDE.md"
DST_GUIDE = ROOT / "AGENTS.md"

SKIP_DIRS = {"node_modules", "__pycache__", ".git"}
SKIP_FILES = {".DS_Store"}
TEXT_EXT = {".md"}

# `../` lặp ≥1 lần rồi tới 1 đoạn đường dẫn. Chỉ viết lại khi đích thật tồn tại và nằm ngoài cây được chép.
REL_RE = re.compile(r"(?<![\w./-])((?:\.\./)+)([A-Za-z_][\w.\-]*(?:/[\w.\-{}]*)*)")

AGENTS_NOTE = """> **Bản cho Codex — máy sinh từ `CLAUDE.md` bởi `_scripts/codex-sync.py`. KHÔNG sửa tay file này.**
> Skill của Codex nằm ở `.agents/skills/` (bản sao của `.claude/skills/`), agent ở `.codex/agents/*.toml`
> (bản chuyển của `.claude/agents/*.md`). Rules, hooks, scripts, templates dùng chung — đường dẫn
> `.claude/rules/...`, `.claude/scripts/...` bên dưới là file thật, đọc trực tiếp.
> Muốn đổi skill/agent/hướng dẫn: sửa bản trong `.claude/` hoặc `CLAUDE.md`, rồi chạy
> `python3 _scripts/codex-sync.py`.

"""


def rewrite_relative(text: str, src_file: Path, dst_file: Path, copied_root: Path) -> str:
    """Tính lại `../..` từ vị trí bản sao, cho các đích nằm NGOÀI cây được chép."""

    def repl(m: re.Match) -> str:
        ups, rest = m.group(1), m.group(2)
        first = rest.split("/")[0]
        target = (src_file.parent / ups / first).resolve()
        try:
            target.relative_to(copied_root.resolve())
            return m.group(0)  # đích nằm trong cây được chép → bản sao cũng có, giữ nguyên
        except ValueError:
            pass
        if not target.exists():
            return m.group(0)  # không phải đường dẫn thật (ví dụ, placeholder) → giữ nguyên
        new_first = os.path.relpath(target, dst_file.parent)
        return new_first + rest[len(first):]

    return REL_RE.sub(repl, text)


def build_skills() -> dict[Path, bytes]:
    out: dict[Path, bytes] = {}
    for dirpath, dirnames, filenames in os.walk(SRC_SKILLS):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            if name in SKIP_FILES:
                continue
            src = Path(dirpath) / name
            dst = DST_SKILLS / src.relative_to(SRC_SKILLS)
            data = src.read_bytes()
            if src.suffix in TEXT_EXT:
                text = rewrite_relative(data.decode("utf-8"), src, dst, SRC_SKILLS)
                data = text.encode("utf-8")
            out[dst] = data
    return out


def parse_frontmatter(text: str) -> tuple[dict, str]:
    m = re.match(r"^---\n(.*?)\n---\n?", text, re.S)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        kv = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if kv:
            meta[kv.group(1)] = kv.group(2).strip()
    return meta, text[m.end():]


def toml_basic(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def toml_multiline(s: str) -> str:
    if "'''" not in s:
        return "'''\n" + s + "'''"
    esc = s.replace("\\", "\\\\").replace('"""', '\\"\\"\\"')
    return '"""\n' + esc + '"""'


def build_agents() -> dict[Path, bytes]:
    out: dict[Path, bytes] = {}
    for src in sorted(SRC_AGENTS.glob("*.md")):
        meta, body = parse_frontmatter(src.read_text(encoding="utf-8"))
        name = meta.get("name") or src.stem
        desc = meta.get("description", "").strip().strip("'\"")
        dst = DST_AGENTS / f"{src.stem}.toml"
        body = rewrite_relative(body.lstrip("\n"), src, dst, SRC_AGENTS)
        doc = (
            f"# Máy sinh từ .claude/agents/{src.name} bởi _scripts/codex-sync.py — KHÔNG sửa tay.\n"
            f"name = {toml_basic(name)}\n"
            f"description = {toml_basic(desc)}\n"
            f"developer_instructions = {toml_multiline(body)}\n"
        )
        tomllib.loads(doc)  # hỏng TOML thì dừng ngay, không ghi
        out[dst] = doc.encode("utf-8")
    return out


def build_guide() -> dict[Path, bytes]:
    return {DST_GUIDE: (AGENTS_NOTE + SRC_GUIDE.read_text(encoding="utf-8")).encode("utf-8")}


def existing(root: Path, pattern: str) -> set[Path]:
    if not root.exists():
        return set()
    return {
        p for p in root.rglob(pattern)
        if p.is_file() and not any(part in SKIP_DIRS for part in p.relative_to(root).parts)
    }


def main() -> int:
    check = "--check" in sys.argv
    want = {**build_skills(), **build_agents(), **build_guide()}
    stale = (existing(DST_SKILLS, "*") | existing(DST_AGENTS, "*.toml")) - set(want)
    stale = {p for p in stale if p.name not in SKIP_FILES}
    changed = [p for p, data in want.items() if not p.exists() or p.read_bytes() != data]

    rel = lambda p: p.relative_to(ROOT)
    if check:
        for p in sorted(changed):
            print(f"lệch   {rel(p)}")
        for p in sorted(stale):
            print(f"thừa   {rel(p)}")
        if changed or stale:
            print(f"✗ Bản Codex lệch nguồn: {len(changed)} file cần cập nhật, {len(stale)} file thừa. "
                  f"Chạy: python3 _scripts/codex-sync.py")
            return 1
        print(f"✓ Bản Codex khớp nguồn ({len(want)} file).")
        return 0

    for p in changed:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(want[p])
    for p in stale:
        p.unlink()
    # dọn thư mục rỗng sau khi xoá file thừa
    for root in (DST_SKILLS, DST_AGENTS):
        for d in sorted((x for x in root.rglob("*") if x.is_dir()), key=lambda x: -len(x.parts)):
            if d.name not in SKIP_DIRS and not any(d.iterdir()):
                d.rmdir()
    print(f"✓ Đã đồng bộ: {len(changed)} file ghi, {len(stale)} file thừa đã xoá, tổng {len(want)} file.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
