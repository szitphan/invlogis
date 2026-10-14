"""Tab "Hệ thống cũ" của /dashboard: feature tái lập từ SRS cũ, theo module, kèm nguồn + tiến độ cải tiến.

Nguồn dữ liệu (đọc, không ghi):
  docs/_reverse/reverse-plan.json      danh sách feature + module + khoảng trang nguồn. Chưa land → đọc bản trong
                                       worktree `.claude/worktrees/*/docs/_reverse/reverse-plan.json`
  docs/_reverse/{feature}/             bộ reverse đã ghi (main hoặc worktree)
  docs/_product/legacy-issues.md       sổ vấn đề gắn feature (cột Feature có `slug` hoặc `*`)
  docs-input/_coverage/*.md            sổ đối chiếu: mục `➡ {feature}` = chưa xử lý, ✅ có `docs/{feature}/` = đã đưa vào
  docs/{feature}/brainstorms/*.md      đã có brainstorm cải tiến chưa
"""
import json
import re
from pathlib import Path


def _plan(root):
    p = root / "docs/_reverse/reverse-plan.json"
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8")), None
    for q in sorted((root / ".claude/worktrees").glob("*/docs/_reverse/reverse-plan.json")):
        return json.loads(q.read_text(encoding="utf-8")), q.parents[2]
    return None, None


def _issues(root):
    p = root / "docs/_product/legacy-issues.md"
    out = []
    if not p.exists():
        return out
    for ln, line in enumerate(p.read_text(encoding="utf-8").split("\n"), 1):
        if line.startswith("| ISS-"):
            c = [x.strip() for x in line.strip().strip("|").split("|")]
            if len(c) >= 6:
                out.append({"id": c[0], "title": c[1], "feats": c[3], "state": c[5], "line": ln})
    return out


def _mobile_pages(root, src):
    """Dòng file SRS Mobile → số trang (mốc `<!-- Trang N -->` gần nhất phía trên)."""
    p = root / src["file"]
    pages, cur = {}, None
    if p.exists():
        for i, l in enumerate(p.read_text(encoding="utf-8").split("\n"), 1):
            m = re.match(r"<!-- Trang (\d+) -->", l)
            if m:
                cur = int(m.group(1))
            pages[i] = cur
    return pages


def legacy_view(root, ledgers):
    plan, wt = _plan(root)
    if not plan:
        return None
    src = plan["sources"]
    mpage = _mobile_pages(root, src["mobile"])
    web_file, mob_file = src["web"]["file"], src["mobile"]["file"]
    web_txt = (root / web_file).read_text(encoding="utf-8").split("\n") if (root / web_file).exists() else []
    web_line = {int(m.group(1)): i for i, l in enumerate(web_txt, 1) for m in [re.match(r"<!-- Page (\d+) -->", l)] if m}
    issues = _issues(root)
    feats = []
    for f in plan["features"]:
        slug = f["slug"]
        srcs = []
        for p in f["parts"]:
            for a, b in p["web_pages"]:
                srcs.append({"label": f"{src['web']['short']} tr.{a}" + (f"–{b}" if b != a else ""),
                             "path": web_file, "line": web_line.get(a), "part": p["name"]})
            for a, b in p["mobile_lines"]:
                pa, pb = mpage.get(a), mpage.get(b)
                lab = f"{src['mobile']['short']} tr.{pa}" + (f"–{pb}" if pb and pb != pa else "") if pa else f"{src['mobile']['short']} dòng {a}–{b}"
                srcs.append({"label": lab, "path": mob_file, "line": a, "part": p["name"]})
        total = done = 0
        first = None
        for sid, led in ledgers.items():
            for r in led["rows"]:
                mine_todo = r["result"].startswith("➡") and r["result"].split(" ", 1)[-1].strip() == slug
                mine_done = "✅" in r["result"] and f"docs/{slug}/" in r["where"]
                if mine_todo or mine_done:
                    total += 1
                    done += mine_done
                    if first is None and mine_todo:
                        first = (led["path"], r["line"])
        base = None
        for cand in [root] + ([wt] if wt else []):
            if (cand / "docs/_reverse" / slug / f"{slug}-reverse-spec.md").exists():
                base = cand
                break
        rev = {"state": "none", "text": "chưa chạy", "path": None}
        if base is not None:
            prev = f"docs/_reverse/{slug}/{slug}-reverse-preview.html"
            rev = {"state": "done", "text": "xong" + (" (trong worktree)" if base != root else ""),
                   "path": prev if (base / prev).exists() and base == root else f"docs/_reverse/{slug}/{slug}-reverse-spec.md"}
        elif f.get("pilot"):
            rev = {"state": "next", "text": "chạy thử đầu tiên", "path": None}
        iss = [i for i in issues if f"`{slug}`" in i["feats"]]
        glob_iss = [i for i in issues if "`*`" in i["feats"]]
        bs = sorted((root / "docs" / slug / "brainstorms").glob("*.md")) if (root / "docs" / slug).is_dir() else []
        feats.append({"slug": slug, "name": f["name"], "module": f.get("module", "—"), "sources": srcs,
                      "changes": f["changes"], "ledger": {"done": done, "total": total, "first": first},
                      "reverse": rev, "issues": iss, "global_issues": glob_iss,
                      "brainstorm": str(bs[0].relative_to(root)) if bs else None})
    mods = []
    for f in feats:
        top = f["module"].split(" › ")[0]
        if not mods or mods[-1]["name"] != top:
            if any(m["name"] == top for m in mods):
                next(m for m in mods if m["name"] == top)["feats"].append(f)
                continue
            mods.append({"name": top, "feats": []})
        mods[-1]["feats"].append(f)
    return {"modules": mods, "worktree": str(wt.relative_to(root)) if wt else None,
            "decision": plan.get("modules_decision", ""), "count": len(feats),
            "issues_total": len(issues), "issues_path": "docs/_product/legacy-issues.md"}


def render_legacy(lv, link, E):
    """HTML cho tabpanel p-legacy. `link`, `E` lấy từ dashboard-build (link 2 chế độ VS Code/GitHub, escape)."""
    h = ['<div role="tabpanel" id="p-legacy" aria-labelledby="t-legacy" hidden>']
    if not lv:
        h.append('<div class="panel"><h2>Hệ thống cũ</h2><p class="muted">Chưa có kế hoạch reverse '
                 '(<code>docs/_reverse/reverse-plan.json</code>). Chạy <code>/reverse-doc</code> trước.</p></div></div>')
        return "".join(h)
    allf = [f for m in lv["modules"] for f in m["feats"]]
    n_rev = sum(1 for f in allf if f["reverse"]["state"] == "done")
    n_bs = sum(1 for f in allf if f["brainstorm"])
    led_d = sum(f["ledger"]["done"] for f in allf)
    led_t = sum(f["ledger"]["total"] for f in allf)
    h.append('<div class="panel"><h2>Hệ thống cũ → cải tiến</h2><p class="muted" style="margin:0">'
             f'{lv["count"]} feature tái lập từ SRS cũ (web + mobile) · reverse xong {n_rev}/{lv["count"]} · '
             f'brainstorm cải tiến {n_bs}/{lv["count"]} · mục nguồn đã đưa vào tài liệu mới {led_d}/{led_t} · '
             + link(lv["issues_path"], f'{lv["issues_total"]} vấn đề cần giải quyết') + '. '
             + (f'Kế hoạch đang ở worktree <code>{E(lv["worktree"])}</code> (chưa land). ' if lv["worktree"] else "")
             + f'Module gắn tạm: {E(lv["decision"])}.</p></div>')
    for m in lv["modules"]:
        h.append(f'<div class="panel"><h2>{E(m["name"])} <span class="muted">({len(m["feats"])})</span></h2>'
                 '<div class="scroll"><table class="srct"><thead><tr><th>Feature</th><th>Nguồn</th>'
                 '<th>Mục nguồn</th><th>Reverse</th><th>Vấn đề cần giải quyết</th><th>Brainstorm</th></tr></thead><tbody>')
        for f in m["feats"]:
            sub = f["module"].split(" › ")[1] if " › " in f["module"] else ""
            multi = len({s["part"] for s in f["sources"]}) > 1
            out, seen = [], set()
            for s in f["sources"]:
                if multi and s["part"] not in seen:
                    seen.add(s["part"])
                    out.append(f'<span class="muted" style="font-size:11px">Phần: {E(s["part"])}</span>')
                out.append(link(s["path"], E(s["label"]), s["line"]))
            srcs = "<br>".join(out)
            if f["changes"]:
                srcs += "<br>" + "<br>".join(f'<span class="chip yellow">thay đổi</span> {E(c["id"])} ({E(c["desc"])})' for c in f["changes"])
            L = f["ledger"]
            lc = ("green" if L["total"] and L["done"] == L["total"] else "yellow" if L["done"] else "gray")
            led = (link(L["first"][0], f'<span class="chip {lc}">{L["done"]}/{L["total"]}</span>', L["first"][1])
                   if L["first"] else f'<span class="chip {lc}">{L["done"]}/{L["total"]}</span>') if L["total"] else '<span class="muted">—</span>'
            r = f["reverse"]
            rc = {"done": "green", "next": "blue"}.get(r["state"], "gray")
            rev = link(r["path"], f'<span class="chip {rc}">{E(r["text"])}</span>') if r["path"] else f'<span class="chip {rc}">{E(r["text"])}</span>'
            def short(t, n=110):
                return t if len(t) <= n else t[:n].rsplit(" ", 1)[0].rstrip(",;:—-") + "…"
            iss = "<br>".join(link(lv["issues_path"], f'<span class="tag">{E(i["id"])}</span>', i["line"]) + " " + E(short(i["title"]))
                              for i in f["issues"])
            if f["global_issues"]:
                iss += ("<br>" if iss else "") + '<span class="muted">+ ' + ", ".join(E(i["id"]) for i in f["global_issues"]) + " (mọi feature)</span>"
            bs = link(f["brainstorm"], '<span class="chip green">có</span>') if f["brainstorm"] else '<span class="chip gray">chưa có</span>'
            h.append(f'<tr data-s="{E(f["slug"] + " " + f["name"])}"><td><b>{E(f["name"])}</b><br>'
                     f'<span class="muted mono" style="font-size:11px">{E(f["slug"])}</span>'
                     + (f'<br><span class="muted" style="font-size:11px">{E(sub)}</span>' if sub else "")
                     + f'</td><td>{srcs}</td><td>{led}</td><td>{rev}</td><td class="iss">{iss or "<span class=muted>—</span>"}</td><td>{bs}</td></tr>')
        h.append("</tbody></table></div></div>")
    h.append("</div>")
    return "".join(h)
