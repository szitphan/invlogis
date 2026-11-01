#!/usr/bin/env python3
"""Trạng thái 9 mục foundations DS v2 — nguồn: bảng `<!-- foundation-status -->` trong design-system/foundations/README.md.

  python3 _scripts/ds-foundation-status.py list [--json]
  python3 _scripts/ds-foundation-status.py set <mã> <draft|in-review|revisions|approved> [--note "…"] [--by /skill] [--dry]
  python3 _scripts/ds-foundation-status.py apply <file.json> [--dry]   # [{"key":"color","to":"approved","note":"…"}]

Dashboard (yêu cầu `ds-status`) và trang duyệt foundations dùng `apply`. Ghi bằng script nên tự ghi changelog
(như dashboard-apply.py). Nhãn trên Figma (trang 🎨 DS · Foundations) Claude ghi sau khi đổi — lệnh in danh sách cần ghi.
"""
import json
import os
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MD = ROOT / "design-system/foundations/README.md"
REL = "design-system/foundations/README.md"
START, END = "<!-- foundation-status -->", "<!-- /foundation-status -->"
STATUSES = ("draft", "in-review", "revisions", "approved")
FLOW = {"draft": {"in-review", "approved"}, "in-review": {"revisions", "approved", "draft"},
        "revisions": {"in-review", "approved"}, "approved": {"revisions"}}
LABEL = {"draft": "Nháp", "in-review": "Đang duyệt", "revisions": "Cần sửa", "approved": "Đã duyệt"}
TODAY = date.today().isoformat()


def read():
    s = MD.read_text(encoding="utf-8")
    a, b = s.index(START), s.index(END)
    rows = []
    for line in s[a:b].splitlines():
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) >= 6 and c[0] not in ("Mã", "---") and not set(c[0]) <= {"-"}:
            rows.append({"key": c[0], "name": c[1], "where": c[2], "status": c[3], "date": c[4], "note": c[5]})
    return s, a, b, rows


def write(s, a, b, rows):
    body = [START, "| Mã | Mục | Ở đâu | Trạng thái | Ngày | Ghi chú |", "|---|---|---|---|---|---|"]
    body += [f"| {r['key']} | {r['name']} | {r['where']} | {r['status']} | {r['date']} | {r['note']} |" for r in rows]
    MD.write_text(s[:a] + "\n".join(body) + "\n" + s[b:], encoding="utf-8")


def changelog(note, by):
    author = os.environ.get("CLAUDE_CHANGELOG_AUTHOR") or "manual"
    note = " ".join(note.replace("|", "\\|").split())
    subprocess.run([sys.executable, str(ROOT / "_scripts/logbook.py"), "add", "changelog",
                    f"| {TODAY} | {by} | {author} | `{REL}` | {note} |"], cwd=ROOT, capture_output=True)


def apply(changes, dry=False, by="/figma-component"):
    s, a, b, rows = read()
    idx = {r["key"]: r for r in rows}
    out = []
    for ch in changes:
        k, to = ch.get("key"), ch.get("to")
        r = idx.get(k)
        if not r:
            out.append({"key": k, "ok": False, "msg": f"không có mục `{k}` (có: {', '.join(idx)})"})
            continue
        if to not in STATUSES:
            out.append({"key": k, "ok": False, "msg": f"trạng thái `{to}` không hợp lệ"})
            continue
        if to == r["status"]:
            out.append({"key": k, "ok": True, "msg": "không đổi", "changed": False})
            continue
        if to not in FLOW[r["status"]]:
            out.append({"key": k, "ok": False, "msg": f"không đi được {r['status']} → {to}"})
            continue
        frm = r["status"]
        r.update(status=to, date=TODAY, note=(ch.get("note") or "").replace("|", "/")[:120])
        out.append({"key": k, "ok": True, "changed": True, "msg": f"{frm} → {to}", "figma": LABEL[to], "name": r["name"]})
    changed = [o for o in out if o.get("changed")]
    if changed and not dry:
        write(s, a, b, rows)
        changelog("trạng thái foundations: " + "; ".join(f"{o['name']} {o['msg']}" for o in changed), by)
    return out


def main():
    av = [x for x in sys.argv[1:]]
    dry = "--dry" in av
    if not av or av[0] == "list":
        _, _, _, rows = read()
        if "--json" in av:
            print(json.dumps(rows, ensure_ascii=False, indent=1))
        else:
            for r in rows:
                print(f"{r['key']:<12} {r['status']:<10} {r['date']}  {r['name']}" + (f" — {r['note']}" if r["note"] else ""))
        return
    by = av[av.index("--by") + 1] if "--by" in av else "/figma-component"
    if av[0] == "set" and len(av) >= 3:
        note = av[av.index("--note") + 1] if "--note" in av else ""
        out = apply([{"key": av[1], "to": av[2], "note": note}], dry, by)
    elif av[0] == "apply" and len(av) >= 2:
        out = apply(json.loads(Path(av[1]).read_text()), dry, by)
    else:
        sys.exit(__doc__)
    print(json.dumps(out, ensure_ascii=False, indent=1))
    sys.exit(0 if all(o["ok"] for o in out) else 1)


if __name__ == "__main__":
    main()
