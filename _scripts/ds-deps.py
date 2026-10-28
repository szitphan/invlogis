#!/usr/bin/env python3
"""Quan hệ cha–con giữa component DS v2 + báo cha cần sync khi con đổi (DEC-292). Nguồn: design/v2/components/_deps.json.

  python3 _scripts/ds-deps.py tree                 # cây: cha dùng con nào (role, tạm), con được cha nào dùng
  python3 _scripts/ds-deps.py version <slug>       # phiên bản hiện tại của 1 component
  python3 _scripts/ds-deps.py impact <child>       # con này đổi thì cha nào bị ảnh hưởng
  python3 _scripts/ds-deps.py inherited <child>    # quyết định chốt sẵn từ cha (brainstorm con hiện làm mặc định)
  python3 _scripts/ds-deps.py check [--write] [--backlog]
      so phiên bản con trong page.kit của cha với bản hiện tại → cha "cần sync"; --write ghi cờ stale vào page.kit
      (trang hiện ⚠); --backlog thêm task "Sync <cha> theo <con>" (Xong khi page.kit có đúng phiên bản mới).

Phiên bản = 10 ký tự sha1 của phần quyết định hình dạng: _work/<slug> (answers brainstorm + css + values) nếu có,
không thì file md (bỏ dòng updated). Con chưa có gì → "chua-dung".
"""
import hashlib
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMP = ROOT / "design/v2/components"
REG = COMP / "_deps.json"


def reg():
    return json.loads(REG.read_text()) if REG.exists() else {"components": {}, "inherited": {}}


def md_of(slug):
    for p in COMP.glob(f"*/{slug}.md"):
        if not p.parent.name.startswith("_"):
            return p
    return None


def version(slug):
    w = COMP / "_work" / slug
    if (w / "page.json").exists():
        p = json.loads((w / "page.json").read_text())
        a = json.loads((w / "answers.json").read_text()) if (w / "answers.json").exists() else {}
        core = {"answers": {k: v.get("choice") for k, v in a.items() if k.startswith("brainstorm-")},
                "css": p.get("css"), "values": p.get("values")}
        return hashlib.sha1(json.dumps(core, ensure_ascii=False, sort_keys=True).encode()).hexdigest()[:10]
    m = md_of(slug)
    if m:
        s = re.sub(r"^updated:.*$", "", m.read_text(encoding="utf-8"), flags=re.M)
        return hashlib.sha1(s.encode()).hexdigest()[:10]
    return "chua-dung"


def parents_of(child, r):
    return [(p, u) for p, d in r["components"].items() for u in d.get("uses", []) if u["child"] == child]


def check(write=False, backlog=False):
    r = reg()
    out = []
    for parent in r["components"]:
        pj = COMP / "_work" / parent / "page.json"
        if not pj.exists():
            continue
        page = json.loads(pj.read_text())
        kit = page.get("kit") or {}
        changed = False
        for c in kit.get("components") or []:
            now = version(c["slug"])
            old = c.get("version")
            stale = bool(old) and old != now
            if stale:
                out.append({"parent": parent, "child": c["slug"], "old": old, "new": now})
            if c.get("stale") != stale or c.get("versionNow") != now:
                c["stale"], c["versionNow"] = stale, now
                changed = True
        if write and changed:
            pj.write_text(json.dumps(page, ensure_ascii=False, indent=1))
    if backlog and out:
        bl = ROOT / "_workspace/backlog.md"
        s = bl.read_text(encoding="utf-8")
        n = max(int(x) for x in re.findall(r"^\| BL-(\d+)", s, re.M)) + 1
        lines = s.split("\n")
        last = max(i for i, l in enumerate(lines) if re.match(r"^\| BL-\d+ \|", l) and "| ✅ |" not in l)
        add = []
        for o in out:
            task = f"Sync {o['parent']} theo {o['child']} (con đổi {o['old']} → {o['new']}): dựng lại preview, chạy lại bước 3/review"
            if task.split(" (")[0] in s:
                continue
            add.append(f"| BL-{n:03d} | {task} | ds-deps (DEC-292) | `grep:design/v2/components/_work/{o['parent']}/page.json:\"version\": \"{o['new']}\"` "
                       f"| ⬜ | {date.today().isoformat()} |  |  |  |  |")
            n += 1
        if add:
            lines[last + 1:last + 1] = add
            bl.write_text("\n".join(lines), encoding="utf-8")
            subprocess.run([sys.executable, str(ROOT / "_scripts/intake-sync.py")], cwd=ROOT, capture_output=True)
            print(f"Thêm {len(add)} task backlog")
    return out


def main():
    av = sys.argv[1:]
    r = reg()
    cmd = av[0] if av else "tree"
    if cmd == "tree":
        for p, d in r["components"].items():
            print(f"{p}  (bản {version(p)})")
            for u in d.get("uses", []):
                print(f"  └ {u['child']:<22} {u['role']:<7} {'tạm' if u.get('provisional') else '   '} bản {version(u['child'])}"
                      + (f" — {u['parts']}" if u.get("parts") else ""))
        for c, items in r.get("inherited", {}).items():
            print(f"chốt sẵn cho {c}: " + "; ".join(f"{i['id']} {i['title']} ({i['from']}, {i['dec']})" for i in items))
    elif cmd == "version":
        print(version(av[1]))
    elif cmd == "impact":
        ps = parents_of(av[1], r)
        print("\n".join(f"{p} · {u['role']}" + (" · tạm" if u.get("provisional") else "") for p, u in ps) or "không cha nào dùng")
    elif cmd == "inherited":
        print(json.dumps(r.get("inherited", {}).get(av[1], []), ensure_ascii=False, indent=1))
    elif cmd == "check":
        out = check("--write" in av, "--backlog" in av)
        print("\n".join(f"⚠ {o['parent']} cần sync theo {o['child']} ({o['old']} → {o['new']})" for o in out) or "Không cha nào cần sync")
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
