#!/usr/bin/env python3
"""Dựng log toàn vault từ file mảnh — để nhiều worktree/branch ghi song song không xung đột.

Hook không ghi thẳng vào `_workspace/changelog.md` / `_workspace/staleness.md` nữa. Mỗi sự kiện
là 1 dòng bảng, append vào file mảnh `_workspace/{log}.d/{YYYY-MM-DD}--{branch}.md`. Hai branch
khác nhau không bao giờ ghi chung 1 mảnh → merge chỉ là thêm file. File tổng là file SINH RA
(gitignore), dựng lại từ mảnh sau mỗi lần ghi và khi mở phiên.

Dùng:
  python3 _scripts/logbook.py build [changelog|staleness]   # dựng file tổng (mặc định: cả 2)
  python3 _scripts/logbook.py add <log> <row>               # append 1 dòng vào mảnh của branch hiện tại + dựng lại
  python3 _scripts/logbook.py migrate                       # 1 lần: chuyển dòng của file tổng cũ sang mảnh 0000-history.md
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WS = ROOT / "_workspace"

LOGS = {
    "changelog": {
        "title": "# Changelog",
        "note": "> Lịch sử thay đổi toàn vault — mới nhất ở cuối. **File sinh ra, đừng sửa tay**: "
                "dựng từ `_workspace/changelog.d/` bởi `_scripts/logbook.py`. Writer duy nhất của mảnh: "
                "hook `auto-changelog.sh`. Xem `.claude/rules/changelog.md`.",
        "header": "| Ngày | Skill | Người | File | Ghi chú |",
        "sep": "|---|---|---|---|---|",
    },
    "staleness": {
        "title": "# Staleness Log",
        "note": "> Lan truyền `status: stale` khi upstream đổi — mới nhất ở cuối. **File sinh ra, đừng "
                "sửa tay**: dựng từ `_workspace/staleness.d/` bởi `_scripts/logbook.py`. Writer duy nhất "
                "của mảnh: hook `post-edit-stale.sh`.",
        "header": "| Ngày | Upstream đổi | Downstream bị đánh stale | Lý do |",
        "sep": "|---|---|---|---|",
    },
}

ROW_DATE = re.compile(r"^\|\s*(\d{4}-\d{2}-\d{2})\s*\|")


def branch_slug() -> str:
    try:
        b = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "--abbrev-ref", "HEAD"],
                           capture_output=True, text=True, timeout=5).stdout.strip()
    except Exception:
        b = ""
    b = b or "nobranch"
    return re.sub(r"[^A-Za-z0-9._-]+", "-", b).strip("-") or "nobranch"


def rows_of(path: Path) -> list[str]:
    return [l.rstrip("\n") for l in path.read_text(encoding="utf-8").splitlines() if ROW_DATE.match(l)]


def build(name: str) -> int:
    cfg = LOGS[name]
    frag_dir = WS / f"{name}.d"
    rows: list[tuple[str, str, int, str]] = []
    if frag_dir.is_dir():
        for frag in sorted(frag_dir.glob("*.md")):
            for i, r in enumerate(rows_of(frag)):
                rows.append((ROW_DATE.match(r).group(1), frag.name, i, r))
    # Ổn định: theo ngày, rồi tên mảnh, rồi thứ tự trong mảnh. 0000-history.md đứng trước mọi mảnh cùng ngày.
    rows.sort(key=lambda t: (t[0], t[1], t[2]))
    out = [cfg["title"], "", cfg["note"], "", cfg["header"], cfg["sep"], *[t[3] for t in rows]]
    target = WS / f"{name}.md"
    tmp = target.with_suffix(".md.tmp")
    tmp.write_text("\n".join(out) + "\n", encoding="utf-8")
    tmp.replace(target)  # atomic — reader không bao giờ thấy file dở
    return len(rows)


def add(name: str, row: str) -> None:
    frag_dir = WS / f"{name}.d"
    frag_dir.mkdir(parents=True, exist_ok=True)
    m = ROW_DATE.match(row)
    if not m:
        sys.exit(f"logbook: dòng không bắt đầu bằng '| YYYY-MM-DD |': {row!r}")
    frag = frag_dir / f"{m.group(1)}--{branch_slug()}.md"
    if frag.exists() and row in frag.read_text(encoding="utf-8").splitlines():
        return  # dedupe double-fire cùng nội dung
    with frag.open("a", encoding="utf-8") as f:  # O_APPEND — an toàn khi nhiều agent cùng branch
        f.write(row + "\n")
    build(name)


def migrate() -> None:
    for name in LOGS:
        old = WS / f"{name}.md"
        frag_dir = WS / f"{name}.d"
        hist = frag_dir / "0000-history.md"
        if hist.exists():
            print(f"{name}: đã migrate trước đó ({hist.relative_to(ROOT)}) — bỏ qua")
            continue
        rows = rows_of(old) if old.exists() else []
        frag_dir.mkdir(parents=True, exist_ok=True)
        hist.write_text("\n".join(rows) + ("\n" if rows else ""), encoding="utf-8")
        n = build(name)
        print(f"{name}: {len(rows)} dòng → {hist.relative_to(ROOT)} · dựng lại {n} dòng")


def main(argv: list[str]) -> None:
    cmd = argv[1] if len(argv) > 1 else "build"
    if cmd == "build":
        for name in (argv[2:] or list(LOGS)):
            build(name)
    elif cmd == "add" and len(argv) == 4 and argv[2] in LOGS:
        add(argv[2], argv[3])
    elif cmd == "migrate":
        migrate()
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main(sys.argv)
