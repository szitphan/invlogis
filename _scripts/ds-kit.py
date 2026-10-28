#!/usr/bin/env python3
"""Kho dựng preview cho /figma-component --html: foundations + component đã có, kèm trạng thái.

  python3 _scripts/ds-kit.py                       # in kho: 9 mục foundations + mọi component md (base, application)
  python3 _scripts/ds-kit.py <slug> --uses a,b     # ghi page["kit"] của _work/<slug>: 9 mục + component preview ráp vào

Preview phải ráp từ kho này (token tokens.css + CSS/anatomy của component đã có). Mục / component chưa `approved` vẫn
dùng, trang review gắn nhãn "chưa duyệt" (user chốt 28/10).
"""
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMP = ROOT / "design/v2/components"


def foundations():
    spec = importlib.util.spec_from_file_location("dfs", ROOT / "_scripts/ds-foundation-status.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return [{"key": r["key"], "name": r["name"], "status": r["status"]} for r in m.read()[3]]


def components():
    out = []
    for p in sorted(COMP.glob("*/*.md")):
        if p.parent.name.startswith("_"):
            continue
        s = p.read_text(encoding="utf-8")
        st = re.search(r"^status:\s*(\S+)", s, re.M)
        title = re.search(r"^#\s+(.+)$", s, re.M)
        out.append({"slug": p.stem, "group": p.parent.name, "name": (title.group(1).strip() if title else p.stem)[:60],
                    "status": st.group(1) if st else "draft", "path": str(p.relative_to(ROOT))})
    return out


def main():
    av = sys.argv[1:]
    fs, cs = foundations(), components()
    if not av or av[0].startswith("--"):
        print("Foundations:"); [print(f"  {f['key']:<12} {f['status']:<10} {f['name']}") for f in fs]
        print("Component:"); [print(f"  {c['group']}/{c['slug']:<24} {c['status']:<10} {c['name']}") for c in cs]
        return
    slug = av[0]
    spec = importlib.util.spec_from_file_location("deps", ROOT / "_scripts/ds-deps.py")
    deps = importlib.util.module_from_spec(spec); spec.loader.exec_module(deps)
    reg_uses = {u["child"]: u for u in deps.reg()["components"].get(slug, {}).get("uses", [])}
    uses = [x.strip() for x in (av[av.index("--uses") + 1] if "--uses" in av else "").split(",") if x.strip()] or list(reg_uses)
    byslug = {c["slug"]: c for c in cs}
    comps = []
    for u in uses:
        ru = reg_uses.get(u, {})
        c = dict(byslug.get(u) or {"slug": u, "group": "", "name": u, "status": "chưa dựng", "path": ""})
        c.update(version=deps.version(u), role=ru.get("role", "embed"), provisional=bool(ru.get("provisional")) or u not in byslug,
                 parts=ru.get("parts", ""), stale=False)
        comps.append(c)
    pj = COMP / "_work" / slug / "page.json"
    page = json.loads(pj.read_text())
    page["kit"] = {"foundations": fs, "components": comps}
    inh = deps.reg().get("inherited", {}).get(slug)  # component này là con: quyết định chốt sẵn từ cha (DEC-292)
    if inh:
        page["inherited"] = inh
    pj.write_text(json.dumps(page, ensure_ascii=False, indent=1))
    nd = [f["name"] for f in fs if f["status"] != "approved"] + [c["name"] for c in comps if c["status"] != "approved"]
    print(f"Đã ghi kit cho {slug}: {len(fs)} mục foundations, {len(uses)} component · chưa duyệt {len(nd)}: {', '.join(nd) or '—'}")


if __name__ == "__main__":
    main()
