"""Tab "Design system" của /dashboard — quản lý DS v2 theo 3 nhóm: Foundations · Base components · Application components
(+ component đang brainstorm chưa có spec md). Bản cũ l1 đã bỏ (DEC-312).

Dữ liệu (chỉ đọc, tất định):
  design-system/tokens.json, foundations.md          — số token theo collection, phiên bản
  design-system/components/{base,application}/*.md — trạng thái md, node Figma md trỏ tới (qua ds-v2-sync-check.specs)
  design-system/components/_work/{slug}/             — state.json (vòng, link trang review), check.json (tab 3), page.json +
                                                   answers.json (điểm review Figma chưa quyết)
  .claude/state/figma/ds-v2-snapshot.json        — ảnh chụp Figma: nhãn trạng thái đang có, ngày chụp
  ds-v2-sync-check.py --figma <snapshot>         — FAIL/WARN theo từng md
"""
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

TIER_NAME = {"base": "Base components", "application": "Application components"}


def _sync_mod(root):
    spec = importlib.util.spec_from_file_location("ds_sync", root / "_scripts/ds-v2-sync-check.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _json(p):
    try:
        return json.loads(Path(p).read_text())
    except Exception:
        return None


def _work(root, slug):
    d = root / "design-system/components/_work" / slug
    if not d.is_dir():
        return None
    st = _json(d / "state.json") or {}
    ck = _json(d / "check.json") or {}
    page = _json(d / "page.json") or {}
    ans = _json(d / "answers.json") or {}
    rv = page.get("reviews") or []
    rv_open = [r["id"] for r in rv if (ans.get("review-" + r["id"]) or {}).get("choice") is None]
    c = ck.get("counts") or {}
    open_n = ck.get("open")
    if open_n is None and ck.get("rows"):
        open_n = sum(1 for r in ck["rows"] if r.get("must") and not r.get("decided")) + c.get("undeclared", 0)
    return {"round": st.get("round") or page.get("round"), "url": st.get("artifact_url"),
            "approved": st.get("approved") or {}, "figma": st.get("figma") or {},
            "check": {"ok": c.get("ok", 0), "near": c.get("near", 0), "new": c.get("new", 0),
                      "conflict": c.get("conflict", 0), "undeclared": c.get("undeclared", 0),
                      "open": open_n, "no_sel": ck.get("no_sel")} if ck else None,
            "reviews": len(rv), "rv_open": rv_open, "title": page.get("component")}


def ds_view(root):
    root = Path(root)
    if not (root / "design-system/tokens.json").exists():
        return None
    m = _sync_mod(root)
    tk = _json(root / "design-system/tokens.json") or {}
    cols = tk.get("collections") or {}
    fcount = []
    for name, c in cols.items():
        n = 0
        for k, v in (c.items() if isinstance(c, dict) else []):
            if k in ("color", "number") and isinstance(v, dict):
                n += len(v)
            elif k == "vars" and isinstance(v, dict):
                n += len(v)
        if n:
            fcount.append({"name": name, "n": n})
    snap_p = root / ".claude/state/figma/ds-v2-snapshot.json"
    snap = _json(snap_p) or {}
    # FAIL / WARN theo md (chạy sync-check một lần)
    issues, f4 = {}, {"fail": 0, "warn": 0}
    try:
        args = [sys.executable, str(root / "_scripts/ds-v2-sync-check.py")] + (["--figma", str(snap_p)] if snap else [])
        out = subprocess.run(args, capture_output=True, text=True, cwd=root, timeout=120).stdout
        code = None
        for line in out.splitlines():
            mm = re.match(r"^([RF]\d):", line)
            if mm:
                code = mm.group(1)
                continue
            mm = re.match(r"^\s+([✕!])\s+(.*)$", line)
            if not mm or not code:
                continue
            kind = "fail" if mm.group(1) == "✕" else "warn"
            if code == "F4":
                f4[kind] += 1
            pm = re.search(r"(design-system/components/[\w/-]+\.md)", mm.group(2))
            if pm:
                d = issues.setdefault(pm.group(1), {"fail": 0, "warn": 0, "first": []})
                d[kind] += 1
                if kind == "fail" and len(d["first"]) < 2:
                    d["first"].append(f"{code} " + mm.group(2).split(": ", 1)[-1])
    except Exception:
        out = ""
    comps = {c["id"]: c for c in snap.get("components") or []}
    secs = {s["id"]: s for s in snap.get("sections") or []}
    file_key = snap.get("fileKey")
    groups = {t: [] for t in ("base", "application")}
    md_slugs = set()
    for s in m.specs():
        md_slugs.add(s["slug"])
        own = [comps[i] for _, i in s["refs"] if i in comps and comps[i]["type"] == "COMPONENT_SET"]
        fig_now = None
        if own:
            fig_now = own[0].get("status") or (secs.get(own[0].get("section") or "", {}).get("badge"))
        first_node = (s["refs"][0][1] if s["refs"] else None)
        title = next((l[2:].strip() for l in s["text"].splitlines() if l.startswith("# ")), s["slug"])
        groups[s["tier"]].append({
            "slug": s["slug"], "title": title, "path": s["path"], "status": s["status"] or "—",
            "label_need": m.figma_label(s), "label_now": fig_now, "on_figma": bool(own),
            "figma_url": f"https://www.figma.com/design/{file_key}/?node-id={first_node.replace(':', '-')}"
            if file_key and first_node else None,
            "work": _work(root, s["slug"]), "sync": issues.get(s["path"], {"fail": 0, "warn": 0, "first": []})})
    wdir = root / "design-system/components/_work"
    drafts = []
    for d in sorted(wdir.iterdir()) if wdir.is_dir() else []:
        if d.is_dir() and d.name not in md_slugs and (d / "page.json").exists():
            w = _work(root, d.name)
            drafts.append({"slug": d.name, "title": (w or {}).get("title") or d.name, "work": w})
    def prio(c):
        w = c["work"] or {}
        ck = w.get("check") or {}
        return (-c["sync"]["fail"], -((ck.get("open") or 0) + len(w.get("rv_open") or [])), c["slug"])
    for t in groups:
        groups[t].sort(key=prio)
    pages = {p["name"]: p["id"] for p in snap.get("pages") or []}
    unref = {}
    if snap:
        allrefs = {i for s in m.specs() for _, i in s["refs"]}
        for c in comps.values():
            if c["type"] == "COMPONENT_SET" and c["id"] not in allrefs and not c["name"].startswith(("_", ".", "icon/")):
                unref.setdefault(c["page"], []).append(c["name"])
    return {"version": tk.get("version"), "collections": fcount, "foundations_md": "design-system/foundations/README.md",
            "tokens_path": "design-system/tokens.json", "snap": {"taken": snap.get("taken"), "fileKey": file_key,
                                                              "pages": pages, "path": ".claude/state/figma/ds-v2-snapshot.json"},
            "f4": f4, "groups": groups, "drafts": drafts, "unref": unref, "fstatus": _fstatus(root), "deps": _deps(root)}


def _deps(root):
    """Component stale theo con lồng trong nó / foundation nó dùng (ds-deps.py check, DEC-292, DEC-302) + cây cha–con."""
    try:
        spec = importlib.util.spec_from_file_location("deps", Path(root) / "_scripts/ds-deps.py")
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        r = m.reg()
        out, notes = m.check()
        return {"stale": out, "notes": notes, "tree": {p: d.get("uses", []) for p, d in r["components"].items() if d.get("uses")}}
    except Exception:
        return {"stale": [], "tree": {}}


def _fstatus(root):
    """9 mục foundations + trạng thái — bảng foundation-status trong foundations.md (_scripts/ds-foundation-status.py)."""
    try:
        spec = importlib.util.spec_from_file_location("dfs", Path(root) / "_scripts/ds-foundation-status.py")
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        rows = m.read()[3]
        for r in rows:
            r["next"] = sorted(m.FLOW.get(r["status"], ()), key=m.STATUSES.index)
        return rows
    except Exception:
        return []


FS_CHIP = {"draft": ("gray", "Nháp"), "in-review": ("amber", "Đang duyệt"), "revisions": ("red", "Cần sửa"),
           "approved": ("green", "Đã duyệt")}
FS_ACT = {"in-review": "Gửi duyệt", "approved": "Duyệt", "revisions": "Cần sửa", "draft": "Về nháp"}


def _fpage():
    try:
        return json.loads((Path(__file__).resolve().parent.parent / "design-system/_review/foundations-status.json").read_text())["url"]
    except Exception:
        return ""


def _fs_table(rows, E, act):
    """Bảng trạng thái 9 mục; mỗi dòng có nút đổi trạng thái (yêu cầu ds-status, /dashboard sync áp vào foundations.md)."""
    h = ['<p style="margin:10px 0 6px"><b>Trạng thái từng mục</b> <span class="muted">— component chỉ coi mục '
         '<b>Đã duyệt</b> là chuẩn; bấm nút tạo yêu cầu, <code>/dashboard sync</code> ghi vào foundations.md và nhãn Figma'
         + (f' · <a href="{E(_fpage())}" target="_blank" rel="noopener">trang duyệt có xem thử</a>' if _fpage() else "") + '</span></p>'
         '<div class="scroll"><table class="srct"><thead><tr><th>Mục</th><th>Ở đâu</th><th>Trạng thái</th><th>Ngày</th>'
         '<th>Đổi</th></tr></thead><tbody>']
    for r in rows:
        c, lb = FS_CHIP.get(r["status"], ("gray", r["status"]))
        btns = "".join(act(FS_ACT.get(t, t), f"ds-status:{r['key']}",
                           {"type": "ds-status", "key": r["key"], "from": r["status"], "to": t, "title": r["name"]})
                       for t in r.get("next") or [])
        h.append(f'<tr data-s="{E(r["name"])}"><td>{E(r["name"])}</td><td class="muted">{E(r["where"])}</td>'
                 f'<td><span class="chip {c}">{lb}</span>{(" <span class=muted>" + E(r["note"]) + "</span>") if r["note"] else ""}</td>'
                 f'<td>{E(r["date"])}</td><td>{btns}</td></tr>')
    h.append("</tbody></table></div>")
    return "".join(h)


def render_ds(v, link, E, act=lambda *a, **k: ""):
    h = ['<div role="tabpanel" id="p-ds" aria-labelledby="t-ds" hidden>']
    if not v:
        h.append('<div class="panel"><h2>Design system</h2><p class="muted">Chưa có <code>design-system/tokens.json</code>.</p></div></div>')
        return "".join(h)
    allc = [c for t in ("base", "application") for c in v["groups"][t]]
    nfail = sum(c["sync"]["fail"] for t in v["groups"].values() for c in t)
    nopen = sum(((c["work"] or {}).get("check") or {}).get("open") or 0 for c in allc) + \
        sum(((d["work"] or {}).get("check") or {}).get("open") or 0 for d in v["drafts"])
    nrv = sum(len((c["work"] or {}).get("rv_open") or []) for c in allc)
    snap = v["snap"]
    fk = snap.get("fileKey")

    def fig_page(name):
        pid = snap["pages"].get(name)
        return (f' · <a href="https://www.figma.com/design/{fk}/?node-id={pid.replace(":", "-")}" target="_blank" rel="noopener">'
                f'mở trang Figma</a>') if fk and pid else ""
    h.append('<div class="panel"><h2>Design system v2</h2><p class="muted" style="margin:0">'
             f'tokens {E(str(v["version"] or ""))} · {len(allc)} component có spec · {len(v["drafts"])} đang brainstorm · '
             f'<b>{nopen}</b> dòng đối chiếu foundation chờ chọn · <b>{nrv}</b> điểm review Figma chưa quyết · '
             f'Figma ↔ repo: <b>{nfail}</b> FAIL'
             + (f' (ảnh chụp {E(snap["taken"])}, ' + link(snap["path"], "snapshot") + ')' if snap.get("taken") else " (chưa chụp Figma)")
             + '. Kiểm lại: <code>python3 _scripts/ds-v2-sync-check.py --figma .claude/state/figma/ds-v2-snapshot.json</code></p></div>')
    dp = v.get("deps") or {}
    if dp.get("stale") or dp.get("tree"):
        st = dp.get("stale") or []
        h.append('<div class="panel"><h2>Component lồng nhau</h2>'
                 + ('<p><span class="chip red">' + str(len(st)) + ' stale</span> ' + " · ".join(
                     f'<b>{E(o["slug"])}</b> theo {E("; ".join(o["reasons"]))}' for o in st) + '</p>' if st else
                    '<p class="muted" style="margin:0 0 6px">Không component nào stale (theo con lồng trong nó hoặc foundation).</p>')
                 + "".join(f'<p class="muted" style="margin:2px 0">ℹ {E(n)}</p>' for n in dp.get("notes") or [])
                 + "".join(f'<p style="margin:2px 0"><b>{E(p)}</b> dùng: ' + ", ".join(
                     E(u["child"]) + (" (neo)" if u.get("role") == "anchor" else "") + (" <span class=muted>tạm</span>" if u.get("provisional") else "")
                     for u in us) + "</p>" for p, us in (dp.get("tree") or {}).items())
                 + '<p class="muted" style="margin:6px 0 0">Sổ <code>design-system/components/_deps.json</code> · '
                 '<code>python3 _scripts/ds-deps.py check --write --backlog</code> (DEC-292, DEC-302)</p></div>')
    # Foundations
    f4 = v["f4"]
    f4c = "green" if not f4["fail"] else "red"
    h.append('<div class="panel"><h2>Foundations</h2><p class="muted" style="margin:0 0 8px">'
             + link(v["foundations_md"], "foundations/") + " · " + link(v["tokens_path"], "tokens.json")
             + fig_page("DS · Foundations")
             + f' · biến Figma ↔ tokens.json: <span class="chip {f4c}">{"khớp" if not f4["fail"] else str(f4["fail"]) + " lệch"}</span></p>'
             + (_fs_table(v.get("fstatus") or [], E, act) if v.get("fstatus") else "")
             + '<div class="scroll"><table class="srct"><thead><tr><th>Collection</th><th>Số token</th></tr></thead><tbody>'
             + "".join(f'<tr data-s="{E(c["name"])}"><td>{E(c["name"])}</td><td>{c["n"]}</td></tr>' for c in v["collections"])
             + "</tbody></table></div></div>")

    def row(c, md=True):
        w = c.get("work") or {}
        ck = w.get("check")
        if ck:
            o = ck.get("open") or 0
            t3 = (f'<span class="chip {"yellow" if o else "green"}">{o} chờ chọn</span><br><span class="muted" style="font-size:11px">'
                  f'khớp {ck["ok"]} · lệch {ck["near"]} · token mới {ck["new"]}'
                  + (f' · <b>chưa khai {ck["undeclared"]}</b>' if ck["undeclared"] else "")
                  + (f' · thiếu sel {ck["no_sel"]}' if ck.get("no_sel") else "") + "</span>")
        else:
            t3 = '<span class="muted">—</span>'
        rv = w.get("reviews") or 0
        ro = w.get("rv_open") or []
        rvc = (f'<span class="chip {"yellow" if ro else "green"}">{len(ro)}/{rv} chưa quyết</span>' if rv else '<span class="muted">—</span>')
        rnd = {"brainstorm": "1 Brainstorm", "preview": "2 Preview", "foundation": "3 Foundation", "figma": "4 Figma",
               "review": "5 Review Figma", "done": "xong"}.get(w.get("round"), w.get("round") or "—")
        links = []
        if md:
            links.append(link(c["path"], "spec"))
        if w.get("url"):
            links.append(f'<a href="{E(w["url"])}" target="_blank" rel="noopener">trang review</a>')
        if c.get("figma_url"):
            links.append(f'<a href="{E(c["figma_url"])}" target="_blank" rel="noopener">Figma</a>')
        if md:
            need, now = c["label_need"], c["label_now"]
            stc = "green" if now == need else ("red" if c["on_figma"] else "gray")
            st = (f'<span class="chip gray">{E(c["status"])}</span><br><span class="muted" style="font-size:11px">Figma: </span>'
                  f'<span class="chip {stc}">{E(now or "chưa có nhãn")}</span>'
                  + ("" if now == need else f'<br><span class="muted" style="font-size:11px">cần “{E(need)}”</span>'))
            sy = c["sync"]
            syc = ('<span class="chip red">' + f'{sy["fail"]} FAIL</span>' if sy["fail"] else '<span class="chip green">khớp</span>') \
                + (f' <span class="muted" style="font-size:11px">{sy["warn"]} cảnh báo</span>' if sy["warn"] else "")
            if sy["first"]:
                syc += '<br><span class="muted" style="font-size:11px">' + "<br>".join(E(x[:90]) for x in sy["first"]) + "</span>"
        else:
            st, syc = '<span class="chip gray">chưa có spec</span>', '<span class="muted">—</span>'
        return (f'<tr data-s="{E(c["slug"] + " " + c["title"])}"><td><b>{E(c["title"])}</b><br>'
                f'<span class="muted mono" style="font-size:11px">{E(c["slug"])}</span></td><td>{st}</td><td>{E(rnd)}</td>'
                f'<td>{t3}</td><td>{rvc}</td><td>{syc}</td><td>{" · ".join(links) or "—"}</td></tr>')
    head = ('<div class="scroll"><table class="srct"><thead><tr><th>Component</th><th>Trạng thái (md · Figma)</th><th>Vòng</th>'
            '<th>Đối chiếu foundation</th><th>Review Figma</th><th>Figma ↔ repo</th><th>Mở</th></tr></thead><tbody>')
    for t, page in (("base", "DS · Base components"), ("application", "DS · Application components")):
        cs = v["groups"][t]
        drafts = []
        if not cs:
            continue
        un = v["unref"].get(page or "", [])
        h.append(f'<div class="panel"><h2>{E(TIER_NAME[t])} <span class="muted">({len(cs)})</span></h2>'
                 + (f'<p class="muted" style="margin:0 0 8px">{fig_page(page)[3:]}'
                    + (f' · {len(un)} component set trên trang chưa có spec md' if un else "") + "</p>" if page else "")
                 + head + "".join(row(c) for c in cs)
                 + "".join(row({**d, "path": None}, md=False) for d in drafts)
                 + "</tbody></table></div>"
                 + (f'<details><summary class="muted">Set trên Figma chưa có spec ({len(un)})</summary><p class="muted">'
                    + E(", ".join(sorted(un))) + "</p></details>" if un else "")
                 + "</div>")
    if v["drafts"]:
        h.append(f'<div class="panel"><h2>Đang dựng — chưa có spec md <span class="muted">({len(v["drafts"])})</span></h2>'
                 + head + "".join(row({**d, "path": None}, md=False) for d in v["drafts"]) + "</tbody></table></div></div>")
    h.append("</div>")
    return "".join(h)
