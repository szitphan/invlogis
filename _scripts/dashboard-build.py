#!/usr/bin/env python3
"""
dashboard-build.py — dựng dashboard BA tất định: gom nguồn máy → 1 JSON → 1 file HTML.

Thay bước Claude tự ghép HTML trong /dashboard (mỗi lần mỗi khác, tốn token). Cùng đầu vào thì
ra cùng HTML (không có giờ phút trong trang — chỉ ngày). Thiết kế chốt ở đề xuất Dashboard BA v2
(artifact 2026-10-13, 3 vòng phản hồi): trục tiến độ theo workflow thật, verdict theo giai đoạn,
kanban 6 cột đủ doc, link mở file local trong VS Code (GitHub dự phòng).

Nguồn (chỉ đọc, không sửa doc nào):
  _scripts/workspace-status.py  docs, coverage FR↔US↔UC, action items, freshness, quality
  _scripts/queue.py --json      làn "Chờ bạn"
  _scripts/saas-layer-lint.py   FAIL/WARN của spec
  .claude/skills/kg/engine/kg-query.mjs orphans   node mồ côi trong userflow (bỏ qua nếu KG lỗi)
  _workspace/backlog.md · _workspace/staleness.md · docs-input/README.md · docs/reports/figma-audit/

Dùng:
  python3 _scripts/dashboard-build.py [--feature <slug>] [--out <path>]
  python3 _scripts/dashboard-build.py --summary   in số liệu cho bảng L1, KHÔNG ghi file
  python3 _scripts/dashboard-build.py --json      in data model, KHÔNG ghi file
"""

import argparse
import glob
import html
import importlib.util
import json
import os
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GITHUB = "https://github.com/szitphan/invlogis/blob/main/"
META_DIRS = {"meetings", "exports", "reports", "cr", "inbox", "userguide", "guides"}

# Trục tiến độ: 8 cột chính + 3 cột ẩn (URD/BRD/PRD — chỉ hiện khi bật).
STAGES = [("nguon", "Nguồn"), ("brainstorm", "Brainstorm"), ("oq", "Chốt OQ"), ("srs", "SRS"),
          ("userflow", "Userflow"), ("figma", "Figma"), ("usac", "US/AC"), ("test", "Test")]
HIDDEN_STAGES = [("urd", "URD"), ("brd", "BRD"), ("prd", "PRD")]
PHASE_OF = {"nguon": "khám phá", "brainstorm": "khám phá", "oq": "khám phá",
            "srs": "đặc tả & thiết kế", "userflow": "đặc tả & thiết kế", "figma": "đặc tả & thiết kế",
            "usac": "bàn giao", "test": "bàn giao"}

KANBAN = [("draft", "Draft"), ("in-review", "In Review"), ("revisions", "Revisions"),
          ("approved", "Approved"), ("shipped", "Shipped"), ("stale", "Stale")]
STATUS_TO_COL = {"draft": "draft", "captured": "draft", "in-progress": "draft", "active": "draft",
                 "in-review": "in-review", "review": "in-review", "revisions": "revisions",
                 "approved": "approved", "done": "approved", "processed": "approved",
                 "shipped": "shipped", "stale": "stale"}
OQ_CLOSED_RE = re.compile(r"^(Đã chốt|Đóng|Bỏ)", re.IGNORECASE)


# ─── helpers ────────────────────────────────────────────────────────────────

def read(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return ""


def rel(p: Path) -> str:
    return str(p.relative_to(ROOT))


def frontmatter(text: str) -> dict:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    fm = {}
    if m:
        for line in m.group(1).split("\n"):
            lm = re.match(r'^(\w+):\s*"?([^"\n]*)"?\s*$', line)
            if lm and lm.group(1) not in fm:
                fm[lm.group(1)] = lm.group(2).strip()
    return fm


def table_cells(line: str) -> list:
    """Tách 1 dòng bảng Markdown, giữ `\\|` (pipe đã escape) trong ô."""
    parts = line.strip().replace("\\|", "\x00").strip("|").split("|")
    return [c.replace("\x00", "|").strip() for c in parts]


def run(cmd: list, timeout=120):
    try:
        r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=timeout)
        return r.returncode, r.stdout
    except (OSError, subprocess.TimeoutExpired):
        return -1, ""


def load_workspace_status():
    spec = importlib.util.spec_from_file_location("ws", ROOT / "_scripts" / "workspace-status.py")
    ws = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ws)
    return ws


# ─── nguồn dữ liệu ──────────────────────────────────────────────────────────

def scan_features(feature_filter):
    out = []
    for d in sorted((ROOT / "docs").iterdir()):
        name = d.name
        if not d.is_dir() or name.startswith("_") or name.startswith("zz-") or name in META_DIRS:
            continue
        if feature_filter and name != feature_filter:
            continue
        out.append(name)
    return out


def scan_oq(feature):
    """Dòng bảng `| OQ-n | … | <trạng thái> |` trong mọi doc của feature. Mở = không bắt đầu
    bằng Đã chốt / Đóng / Bỏ (ô cuối của dòng)."""
    rows = []
    for p in sorted((ROOT / "docs" / feature).rglob("*.md")):
        for i, line in enumerate(read(p).split("\n"), 1):
            m = re.match(r"^\|\s*OQ-(\d+)\s*\|", line)
            if not m:
                continue
            cells = [c for c in table_cells(line) if c]
            state = cells[-1] if len(cells) > 1 else ""
            rows.append({"id": f"OQ-{m.group(1)}", "path": rel(p), "line": i,
                         "question": cells[1] if len(cells) > 1 else "",
                         "open": not OQ_CLOSED_RE.match(state)})
    return rows


def lint_spec(spec_path: Path):
    if not spec_path.exists():
        return None
    code, out = run([sys.executable, "_scripts/saas-layer-lint.py", rel(spec_path)])
    if code == -1:
        return None
    return {"fail": len(re.findall(r"^\s*FAIL\b", out, re.M)),
            "warn": len(re.findall(r"^\s*WARN\b", out, re.M)),
            "first_warn_line": (lambda m: int(m.group(1)) if m else None)(
                re.search(r"^\s*(?:FAIL|WARN) \S+?:(\d+)", out, re.M))}


def kg_userflow_orphans(feature):
    code, out = run(["node", ".claude/skills/kg/engine/kg-query.mjs", "orphans", "--feature", feature, "--all"])
    if code != 0 or "KG-ERROR" in out:
        return None
    sec = re.search(r"### Node không có edge.*?\n(.*?)(?:\n### |\Z)", out, re.S)
    if not sec:
        return 0
    return sum(1 for l in sec.group(1).split("\n") if l.startswith("| screen:") and "userflow.md" in l)


def latest_figma_audit(feature):
    files = sorted(glob.glob(str(ROOT / "docs/reports/figma-audit" / f"*-{feature}-figma-audit.md")))
    if not files:
        return None
    p = Path(files[-1])
    m = re.search(r"\*\*Cao (\d+) · Trung (\d+) · Thấp (\d+)\*\*", read(p))
    return {"path": rel(p), "date": p.name[:10],
            "cao": int(m.group(1)) if m else 0, "trung": int(m.group(2)) if m else 0,
            "thap": int(m.group(3)) if m else 0}


def parse_backlog():
    text = read(ROOT / "_workspace/backlog.md")
    sec = re.search(r"## Đang mở\n(.*?)(?:\n## |\Z)", text, re.S)
    rows = []
    for line in (sec.group(1) if sec else "").split("\n"):
        if not line.startswith("| BL-"):
            continue
        c = table_cells(line)
        if len(c) < 6:
            continue
        c += [""] * (10 - len(c))
        rows.append({"id": c[0], "task": c[1], "source": c[2], "done_when": c[3], "state": c[4], "created": c[5],
                     "due": c[8], "manual": c[9]})
    return rows


def parse_sources():
    rows = []
    for line in read(ROOT / "docs-input/README.md").split("\n"):
        if not re.match(r"^\| SRC-\d+ \|", line):
            continue
        c = table_cells(line)
        rows.append({"id": c[0], "file": c[1].strip("`"), "group": c[2], "feed": c[3]})
    return rows


def parse_ledgers():
    """Sổ đối chiếu docs-input/_coverage/*.md → {SRC-nn: {name, path, rows:[{muc, result, where}]}}."""
    out = {}
    for p in sorted((ROOT / "docs-input/_coverage").glob("*.md")):
        text = read(p)
        h = re.search(r"^#\s*Sổ đối chiếu:\s*(.+?)\s*\((SRC-\d+)\)", text, re.M)
        if not h:
            continue
        rows = []
        for line in text.split("\n"):
            if not line.startswith("| ") or line.startswith("| Mục") or line.startswith("|---"):
                continue
            c = table_cells(line) + ["", ""]
            rows.append({"muc": c[0], "result": c[1], "where": c[2]})
        out[h.group(2)] = {"name": h.group(1), "path": rel(p), "rows": rows}
    return out


def source_name(src, ledgers):
    """Tên hiển thị của nguồn: H1 file nguồn; H1 kiểu mục lục/in đậm → tên ở sổ đối chiếu; cuối cùng là tên file."""
    led = ledgers.get(src["id"])
    p = ROOT / "docs-input" / src["file"]
    h1 = ""
    if p.suffix == ".md" and p.exists():
        m = re.search(r"^#\s+(.+)$", read(p), re.M)
        h1 = m.group(1).strip() if m else ""
    if h1 and not h1.startswith("**") and "MỤC LỤC" not in h1.upper():
        return h1
    if led:
        return led["name"]
    stem = Path(src["file"]).stem.replace("-", " ")
    return stem[:1].upper() + stem[1:]


def feed_ratio(feed):
    m = re.search(r"(\d+)/(\d+)", feed)
    return (int(m.group(1)), int(m.group(2))) if m else None


def source_cell(feature, ledgers):
    """Cột Nguồn của trục tiến độ: mục sổ đối chiếu thuộc feature (➡ feature hoặc path docs/feature/)."""
    done = total = 0
    redo = pending = False
    first = None
    for src, led in sorted(ledgers.items()):
        for r in led["rows"]:
            mine = f"➡ {feature}" in r["result"] or f"docs/{feature}/" in r["where"]
            if not mine:
                continue
            total += 1
            first = first or led["path"]
            if "✅" in r["result"]:
                done += 1
            elif "🔄" in r["result"]:
                redo = True
            elif "➖" not in r["result"]:
                pending = True
    if not total:
        return cell("none", "", note="chưa có mục sổ đối chiếu nào thuộc feature này")
    state = "block" if redo else "part" if pending else "done"
    return cell(state, f"{done}/{total}", first, note="có mục 🔄 bản mới chưa rà" if redo else "")


def parse_params():
    rows = []
    for line in read(ROOT / "docs/_product/tenant-parameters.md").split("\n"):
        if not re.match(r"^\|\s*P-", line):
            continue
        c = table_cells(line) + [""] * 9
        rows.append({"code": c[0], "default": c[4], "tenant": c[5],
                     "open": "chưa chốt" in (c[4] + " " + c[5]).lower()})
    return rows


def orphan_worktrees():
    code, out = run(["git", "worktree", "list", "--porcelain"])
    res = []
    if code != 0:
        return res
    for blk in out.strip().split("\n\n"):
        path = re.search(r"^worktree (.+)$", blk, re.M)
        br = re.search(r"^branch refs/heads/(.+)$", blk, re.M)
        b = br.group(1) if br else "(detached)"
        if path and Path(path.group(1)) != ROOT and not b.startswith("feat/"):
            res.append({"path": path.group(1), "branch": b})
    return res


def parse_staleness():
    rows = []
    for line in read(ROOT / "_workspace/staleness.md").split("\n"):
        if not line.startswith("| 20"):
            continue
        c = table_cells(line)
        if len(c) < 3:
            continue
        up, down = c[1].strip("`"), c[2].strip("`")
        rows.append({"date": c[0], "upstream": up, "downstream": down,
                     "dead": not (ROOT / down).exists()})
    return rows


# ─── trục tiến độ ───────────────────────────────────────────────────────────

def cell(state, text="", path=None, line=None, note=""):
    """state: done (đậm) · part (nhạt) · block (viền đỏ) · none (xám, chưa tới)."""
    return {"state": state, "text": text, "path": path, "line": line, "note": note}


def feature_row(feature, cov, oqs, lint, orphans, audit, ledgers):
    base = ROOT / "docs" / feature
    st = {}
    st["nguon"] = source_cell(feature, ledgers)

    bs = base / "brainstorms" / f"{feature}.md"
    if bs.exists():
        s = frontmatter(read(bs)).get("status", "draft")
        st["brainstorm"] = cell("done" if s == "approved" else "block" if s == "stale" else "part", s, rel(bs))
    else:
        st["brainstorm"] = cell("none")

    open_oq = [o for o in oqs if o["open"]]
    if oqs:
        first = open_oq[0] if open_oq else oqs[0]
        if open_oq:
            st["oq"] = cell("block" if bs.exists() else "part", f"{len(open_oq)} OQ", first["path"], first["line"])
        else:
            st["oq"] = cell("done", "0 OQ", first["path"], first["line"])
    else:
        st["oq"] = cell("done" if bs.exists() else "none", "0 OQ" if bs.exists() else "")

    spec = base / "srs" / f"{feature}-spec.md"
    fr_total = (cov or {}).get("fr_total", 0)
    if spec.exists():
        s = frontmatter(read(spec)).get("status", "draft")
        fail = (lint or {}).get("fail", 0)
        warn = (lint or {}).get("warn", 0)
        label = f"{fr_total} FR" + (f" · {fail} FAIL" if fail else f" · {warn} WARN" if warn else "")
        state = "block" if (fail or s == "stale") else "done" if fr_total and s in ("approved", "shipped") else "part"
        st["srs"] = cell(state, label, rel(spec), (lint or {}).get("first_warn_line"),
                         "spec stale" if s == "stale" else "")
    else:
        st["srs"] = cell("none")

    uf = base / "srs" / f"{feature}-userflow.md"
    if uf.exists():
        if orphans:
            st["userflow"] = cell("part", f"{orphans} mồ côi", rel(uf))
        else:
            st["userflow"] = cell("done", "✓" if orphans == 0 else "có", rel(uf),
                                  note="" if orphans == 0 else "KG lỗi — chưa đếm node mồ côi")
    else:
        st["userflow"] = cell("none")

    sidx = base / "screens" / f"{feature}-screen-index.md"
    screens = [p for p in (base / "screens").glob("*.md") if p.name != sidx.name] if (base / "screens").is_dir() else []
    if sidx.exists() or screens:
        txt = f"{len(screens)} màn"
        state = "part"
        if audit and audit["cao"]:
            state, txt = "block", f"{len(screens)} màn · {audit['cao']} Cao"
        st["figma"] = cell(state, txt, rel(sidx) if sidx.exists() else rel(screens[0]))
    else:
        st["figma"] = cell("none")

    if fr_total and not cov.get("us_total"):
        # Có FR mà chưa viết US nào = chưa tới bước này (xám), không phải đang làm.
        st["usac"] = cell("none", f"0/{fr_total}")
    elif fr_total:
        covd = cov.get("fr_covered", 0)
        orphan_us = len(cov.get("us_orphan", []))
        uidx = base / "userstories" / f"{feature}-story-index.md"
        st["usac"] = cell("block" if orphan_us else "done" if covd == fr_total else "part",
                          f"{covd}/{fr_total}", rel(uidx) if uidx.exists() else None)
    else:
        st["usac"] = cell("none")

    uc_total = (cov or {}).get("uc_total", 0)
    if uc_total and (fr_total and cov.get("fr_covered")):
        untested = len(cov.get("uc_untested", []))
        st["test"] = cell("done" if not untested else "part", f"{uc_total - untested}/{uc_total} UC")
    else:
        st["test"] = cell("none")

    for key, _ in HIDDEN_STAGES:
        cands = [base / f"{feature}-{key}.md", base / "brainstorms" / f"{feature}-{key}.md"]
        hit = next((p for p in cands if p.exists()), None)
        if hit:
            s = frontmatter(read(hit)).get("status", "draft")
            st[key] = cell("done" if s in ("approved", "shipped") else "part", s, rel(hit))
        else:
            st[key] = cell("none")

    reached = [k for k, _ in STAGES if st[k]["state"] != "none"]
    furthest = reached[-1] if reached else None
    done_n = sum(1 for k, _ in STAGES if st[k]["state"] == "done")
    return {"feature": feature, "stages": st, "furthest": furthest,
            "furthest_idx": [k for k, _ in STAGES].index(furthest) if furthest else -1,
            "done": done_n, "blocks": [k for k, _ in STAGES if st[k]["state"] == "block"],
            "open_oq": len(open_oq), "oq_rows": oqs, "lint": lint, "audit": audit,
            "screens": len(screens)}


# ─── kanban ─────────────────────────────────────────────────────────────────

def build_kanban(feature_filter):
    cards, loose = [], []
    lifecycle_by_dir = {}
    all_md = sorted((ROOT / "docs").rglob("*.md"))
    metas = {}
    for p in all_md:
        r = rel(p)
        if "/cr/" in r:
            continue
        fm = frontmatter(read(p))
        if feature_filter and fm.get("feature", "") != feature_filter and f"docs/{feature_filter}/" not in r:
            continue
        metas[r] = (p, fm)
        if "status" in fm:
            lifecycle_by_dir.setdefault(str(p.parent), []).append(r)
    by_path = {}
    for r, (p, fm) in metas.items():
        if "status" not in fm:
            continue
        text = read(p)
        h1 = re.search(r"^#\s+(.+)$", text, re.M)
        status = fm.get("status", "draft")
        card = {"path": r, "title": h1.group(1).strip() if h1 else p.stem, "type": fm.get("type", ""),
                "feature": fm.get("feature", ""), "status": status, "prev": fm.get("status_prev", ""),
                "col": STATUS_TO_COL.get(status, "draft"), "updated": fm.get("updated", ""), "children": []}
        cards.append(card)
        by_path[r] = card
    for r, (p, fm) in metas.items():
        if "status" in fm:
            continue
        parents = lifecycle_by_dir.get(str(p.parent), [])
        if parents:
            by_path[sorted(parents)[0]]["children"].append(r)
        else:
            loose.append(r)
    for c in cards:
        c["children"].sort()
    order = {k: i for i, (k, _) in enumerate(KANBAN)}
    cards.sort(key=lambda c: (order[c["col"]], c["updated"] or "", c["path"]))
    return {"cards": cards, "loose": sorted(loose), "total": len(metas)}


# ─── tổng hợp ───────────────────────────────────────────────────────────────

def priority_score(blocking, due, today, spread, age_days):
    """Điểm ưu tiên 0–100 (Dashboard v2, đã duyệt): Chặn 40/25 · Hạn 25/15 · Lan 4đ/đơn vị trần 20 ·
    Tuổi 1đ/2 ngày trần 15. Trả (tổng, bảng thành phần) để trang hiện cách tính."""
    chan = {"full": 40, "part": 25}.get(blocking, 0)
    han = 0
    if due:
        try:
            left = (date.fromisoformat(due) - today).days
            han = 25 if left <= 7 else 15 if left <= 14 else 0
        except ValueError:
            han = 0
    lan = min(20, 4 * max(0, spread))
    tuoi = min(15, max(0, age_days) // 2)
    parts = {"Chặn": chan, "Hạn": han, "Lan": lan, "Tuổi": tuoi}
    return sum(parts.values()), parts


def build_queue(rows, backlog, stale_docs, actions, ledgers, worktrees, today):
    """Hàng việc chung: task BL đang mở + việc máy phát hiện, cùng 1 thang điểm. Ưu tiên tay thắng điểm."""
    by_feat = {r["feature"]: r for r in rows}

    def feat_block(f, first_only=False):
        r = by_feat.get(f)
        return bool(r and r["blocks"])

    items = []
    for b in backlog:
        if b["state"].startswith("✅"):
            continue
        blob = f'{b["task"]} {b["source"]} {b["done_when"]}'
        feats = [f for f in by_feat if f in blob]
        docs_n = len(set(re.findall(r"docs/[\w./-]+\.md", blob)))
        try:
            age = (today - date.fromisoformat(b["created"])).days
        except ValueError:
            age = 0
        score, parts = priority_score("full" if any(feat_block(f) for f in feats) else None,
                                      b["due"], today, len(feats) + docs_n, age)
        link_path = next(iter(re.findall(r"(docs/[\w./-]+\.md)", blob)), "_workspace/backlog.md")
        items.append({"kind": "BL", "id": b["id"], "title": re.sub(r"`", "", b["task"])[:150], "score": score,
                      "parts": parts, "manual": b["manual"], "path": link_path, "line": None, "due": b["due"]})

    # Máy: doc stale gom theo feature (project-level gom chung)
    groups = {}
    for d in stale_docs:
        groups.setdefault(d["feature"] or "_dự án", []).append(d)
    for f, ds in sorted(groups.items()):
        r = by_feat.get(f)
        blocking = "full" if r and ({"brainstorm", "srs"} & set(r["blocks"])) else "part" if r else None
        age = max((d["days_since_update"] for d in ds if d["days_since_update"] >= 0), default=0)
        score, parts = priority_score(blocking, "", today, len(ds), age)
        label = f if f != "_dự án" else "doc dự án"
        items.append({"kind": "Máy", "id": f"stale:{f}", "title": f"{label}: {len(ds)} doc stale chờ rà hoặc reset",
                      "score": score, "parts": parts, "manual": "", "path": ds[0]["path"], "line": None, "due": ""})
    # Máy: OQ mở của feature chưa có task BL nào nhắc tới
    mentioned = " ".join(f'{b["task"]} {b["source"]} {b["done_when"]}' for b in backlog if not b["state"].startswith("✅"))
    for r in rows:
        if r["open_oq"] and r["feature"] not in mentioned:
            o = r["stages"]["oq"]
            score, parts = priority_score("full", "", today, r["open_oq"], 0)
            items.append({"kind": "Máy", "id": f"oq:{r['feature']}", "title": f"{r['feature']}: {r['open_oq']} câu hỏi mở chưa có task",
                          "score": score, "parts": parts, "manual": "", "path": o["path"], "line": o["line"], "due": ""})
        lint = r.get("lint") or {}
        if lint.get("fail"):
            score, parts = priority_score("full", "", today, lint["fail"], 0)
            items.append({"kind": "Máy", "id": f"lint:{r['feature']}", "title": f"{r['feature']}: {lint['fail']} lỗi FAIL tầng SaaS",
                          "score": score, "parts": parts, "manual": "", "path": r["stages"]["srs"]["path"],
                          "line": r["stages"]["srs"]["line"], "due": ""})
        a = r.get("audit")
        if a and a["cao"]:
            try:
                age = (today - date.fromisoformat(a["date"])).days
            except ValueError:
                age = 0
            score, parts = priority_score("part", "", today, a["cao"], age)
            items.append({"kind": "Máy", "id": f"figma:{r['feature']}", "title": f"Audit Figma {r['feature']}: {a['cao']} mục mức Cao",
                          "score": score, "parts": parts, "manual": "", "path": a["path"], "line": None, "due": ""})
    # Máy: nguồn có bản mới (🔄) chưa rà
    for src, led in sorted(ledgers.items()):
        n = sum(1 for x in led["rows"] if "🔄" in x["result"])
        if n:
            score, parts = priority_score(None, "", today, n, 0)
            items.append({"kind": "Máy", "id": f"src:{src}", "title": f"{src} {led['name']}: {n} mục bản mới chưa rà",
                          "score": score, "parts": parts, "manual": "", "path": led["path"], "line": None, "due": ""})
    # Máy: worktree không có branch feat/*
    for w in worktrees:
        score, parts = priority_score(None, "", today, 0, 0)
        items.append({"kind": "Máy", "id": f"wt:{w['branch']}", "title": f"Worktree {w['branch']} không theo feat/* (dọn bằng wt.sh drop)",
                      "score": score, "parts": parts, "manual": "", "path": None, "line": None, "due": ""})
    # Máy: việc engine phát hiện (review kẹt, US thiếu AC, CR…)
    for a in actions:
        if "Stale" in a["title"]:
            continue  # đã gom ở nhóm stale
        m = a["metric"]
        age = m.get("days_in_review") or m.get("days_since_update") or m.get("days_since_apply") or 0
        score, parts = priority_score(None, "", today, 1, age)
        items.append({"kind": "Máy", "id": f"act:{a['target_path']}", "title": a["title"], "score": score,
                      "parts": parts, "manual": "", "path": a["target_path"], "line": None, "due": ""})

    rank = lambda i: 0 if i["manual"].upper() == "P0" else 2 if i["manual"].lower() == "để sau" else 1
    items.sort(key=lambda i: (rank(i), -i["score"], i["kind"], i["id"]))
    return items


def light(n, ok, warn):
    return "green" if n <= ok else "amber" if n <= warn else "red"


def build(feature_filter=None):
    today = date.today()
    ws = load_workspace_status()
    docs = ws.scan_docs(ROOT, feature_filter, today)
    features = scan_features(feature_filter)
    coverage = {c["feature"]: c for c in ws.compute_coverage(ROOT, features, today)}
    crs = ws.scan_crs(ROOT, feature_filter, today)
    stories = ws.scan_user_stories(ROOT, feature_filter)
    actions = ws.compute_action_items(docs, crs, stories, today)

    ledgers = parse_ledgers()
    rows = []
    for f in features:
        spec = ROOT / "docs" / f / "srs" / f"{f}-spec.md"
        uf = ROOT / "docs" / f / "srs" / f"{f}-userflow.md"
        rows.append(feature_row(f, coverage.get(f), scan_oq(f), lint_spec(spec),
                                kg_userflow_orphans(f) if uf.exists() else None, latest_figma_audit(f), ledgers))
    # Feature chậm nhất lên đầu: giai đoạn xa nhất thấp hơn trước, rồi ít ô xong hơn, rồi tên.
    rows.sort(key=lambda r: (r["furthest_idx"], r["done"], r["feature"]))

    rc, qout = run([sys.executable, "_scripts/queue.py", "--json"])
    try:
        queue = json.loads(qout) if rc == 0 else {}
    except json.JSONDecodeError:
        queue = {}
    lanes = queue.get("lanes", {})
    if feature_filter:
        lanes = {k: [x for x in v if x.get("feature") == feature_filter] for k, v in lanes.items()}
    waiting = sum(len(lanes.get(k, [])) for k in ("review", "blocked", "planned"))

    backlog = parse_backlog()
    sources = parse_sources()
    stale_log = parse_staleness()
    stale_docs = sorted([d for d in docs if d.get("is_stale")], key=lambda d: d["path"])
    kanban = build_kanban(feature_filter)
    params = parse_params()
    for s_ in sources:
        s_["name"] = source_name(s_, ledgers)
        s_["ratio"] = feed_ratio(s_["feed"])
        s_["ledger"] = ledgers.get(s_["id"], {}).get("path")
    work = build_queue(rows, backlog, stale_docs, actions, ledgers,
                       [] if feature_filter else orphan_worktrees(), today)

    # Độ tươi chỉ theo tuổi (stale có đèn riêng) — workspace-status.compute_freshness đã tách.
    fresh = ws.compute_freshness(docs)
    quality = ws.compute_quality(ROOT, docs, feature_filter)

    open_oq = sum(r["open_oq"] for r in rows)
    dead_log = [s for s in stale_log if s["dead"]]
    not_fed = [s for s in sources if s["feed"].startswith("⬜")]
    feedable = [s for s in sources if not s["feed"].startswith("➖")]
    open_bl = [b for b in backlog if not b["state"].startswith("✅")]

    # Verdict theo giai đoạn: pha = giai đoạn của số đông feature; nút thắt = cột có nhiều ô chặn nhất.
    phases = {}
    for r in rows:
        if r["furthest"]:
            phases[PHASE_OF[r["furthest"]]] = phases.get(PHASE_OF[r["furthest"]], 0) + 1
    phase = max(sorted(phases), key=lambda k: phases[k]) if phases else None
    block_count = {k: sum(1 for r in rows if k in r["blocks"]) for k, _ in STAGES}
    neck = max([k for k, _ in STAGES], key=lambda k: (block_count[k], -[s for s, _ in STAGES].index(k)))
    lint_fail = sum((r["stages"]["srs"]["text"].count("FAIL") and 1) for r in rows)
    if not rows:
        verdict = {"level": "gray", "title": "Chưa có feature nào",
                   "summary": "Bắt đầu với /brainstorm hoặc /intake."}
    else:
        level = "red" if (len(lanes.get("blocked", [])) or lint_fail) else "amber" if any(block_count.values()) or waiting else "green"
        neck_label = dict(STAGES)[neck]
        if block_count[neck]:
            if neck == "oq":
                neck_txt = f"nút thắt là {open_oq} câu hỏi mở ({block_count[neck]} feature đang chờ chốt)"
            else:
                neck_txt = f"nút thắt ở cột {neck_label} ({block_count[neck]} feature)"
        else:
            neck_txt = "không có cột nào đang chặn"
        verdict = {"level": level, "title": f"Đang ở giai đoạn {phase}: {neck_txt}",
                   "summary": " · ".join(x for x in [
                       f"{waiting} việc chờ anh duyệt" if waiting else "Không có việc nào chờ anh duyệt",
                       f"{len(stale_docs) + len(dead_log)} mục stale chờ xác nhận" if (stale_docs or dead_log) else "",
                       f"{len(not_fed)} nguồn khách chưa feed" if not_fed else ""] if x)}

    tiles = [
        {"key": "waiting", "label": "Chờ bạn", "value": waiting, "light": "green" if not waiting else "amber",
         "sub": f"{len(lanes.get('review', []))} duyệt land · {len(lanes.get('blocked', []))} chặn · {len(lanes.get('planned', []))} card"},
        {"key": "oq", "label": "Câu hỏi mở", "value": open_oq, "light": light(open_oq, 0, 20),
         "sub": " · ".join(f"{r['feature']} {r['open_oq']}" for r in sorted(rows, key=lambda r: -r["open_oq"]) if r["open_oq"]) or "không còn",
         "path": next((r["stages"]["oq"]["path"] for r in sorted(rows, key=lambda r: -r["open_oq"]) if r["open_oq"]), None),
         "line": next((r["stages"]["oq"]["line"] for r in sorted(rows, key=lambda r: -r["open_oq"]) if r["open_oq"]), None)},
        {"key": "stale", "label": "Stale chờ xác nhận", "value": len(stale_docs) + len(dead_log),
         "light": light(len(stale_docs), 0, 5), "sub": f"{len(stale_docs)} doc · {len(dead_log)} dòng log trỏ file đã xoá",
         "path": "_workspace/staleness.md"},
        {"key": "src", "label": "Nguồn chưa feed", "value": f"{len(not_fed)}/{len(feedable)}",
         "light": light(len(not_fed), 0, 5), "sub": "không tính nguồn ➖", "path": "docs-input/README.md"},
        {"key": "backlog", "label": "Hàng việc", "value": len(work), "light": "gray",
         "sub": f"{len(open_bl)} task backlog · {len(work) - len(open_bl)} việc máy phát hiện", "path": "_workspace/backlog.md"},
    ]

    return {
        "generated": today.isoformat(), "scope": feature_filter or "project", "root": str(ROOT),
        "verdict": verdict, "tiles": tiles, "lanes": lanes, "actions": actions, "work": work,
        "sources": sources, "params": params,
        "features": rows, "kanban": kanban, "stale_docs": stale_docs, "stale_log": stale_log,
        "freshness": fresh, "quality": quality, "coverage": coverage,
        "counts": {"docs_md": kanban["total"], "features": len(rows), "sources": len(sources),
                   "backlog_open": len(open_bl), "open_oq": open_oq},
    }


# ─── render ─────────────────────────────────────────────────────────────────

E = html.escape


def link(path, label, line=None, cls=""):
    """Link 2 chế độ: data-local (vscode://file, mặc định) + data-gh (GitHub dự phòng)."""
    if not path:
        return f'<span class="{cls}">{label}</span>'
    loc = f"vscode://file{ROOT}/{path}" + (f":{line}" if line else "")
    gh = GITHUB + path + (f"#L{line}" if line else "")
    return (f'<a class="{cls}" href="{E(loc)}" data-local="{E(loc)}" data-gh="{E(gh)}" '
            f'title="{E(path)}">{label}</a>')


CSS = """
:root{--bg:#f4f6f6;--panel:#fff;--fg:#1d2a2c;--muted:#5d6e70;--line:#d9e1e1;--track:#e8eeee;
--accent:#0f6e74;--accent-soft:#dcefef;--ok:#2f7d46;--warn:#a86a00;--bad:#b4372f;--gray:#8a9799;
--f:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;--m:ui-monospace,Menlo,Consolas,monospace}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#121819;--panel:#1a2223;--fg:#dde6e6;--muted:#93a4a5;--line:#2c3a3b;--track:#243031;--accent:#5cc3c9;--accent-soft:#1c3638;--ok:#62c07f;--warn:#e0a63c;--bad:#ec7a70;--gray:#7b8a8b;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#121819;--panel:#1a2223;--fg:#dde6e6;--muted:#93a4a5;--line:#2c3a3b;--track:#243031;--accent:#5cc3c9;--accent-soft:#1c3638;--ok:#62c07f;--warn:#e0a63c;--bad:#ec7a70;--gray:#7b8a8b;color-scheme:dark}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:14px/1.55 var(--f);padding:0 16px}
.page{max-width:1120px;margin:0 auto;padding-block:20px 48px;display:flex;flex-direction:column;gap:16px}
a{color:var(--accent);text-underline-offset:2px}a:focus-visible,button:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
code,.mono{font-family:var(--m);font-size:.85em}
.bar{display:flex;flex-wrap:wrap;gap:6px 14px;align-items:center;background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:10px 14px}
.bar b{font-size:1rem}.muted{color:var(--muted)}
.seg{display:inline-flex;gap:4px;align-items:center;font-size:.78rem}
.seg button,.tabs button{font:inherit;font-size:.8rem;border:1px solid var(--line);background:var(--panel);color:var(--muted);padding:3px 10px;border-radius:6px;cursor:pointer}
.seg button[aria-pressed="true"],.tabs button[aria-selected="true"]{border-color:var(--accent);color:var(--accent);background:var(--accent-soft);font-weight:600}
.tabs{display:flex;gap:4px;flex-wrap:wrap;margin-left:auto}
.verdict{background:var(--panel);border:1px solid var(--line);border-left:6px solid var(--gray);border-radius:8px;padding:12px 16px}
.verdict b{display:block;font-size:1.05rem}.v-red{border-left-color:var(--bad)}.v-amber{border-left-color:var(--warn)}.v-green{border-left-color:var(--ok)}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:10px}
.tile{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:10px 12px;display:flex;flex-direction:column;gap:2px;min-width:0;color:inherit;text-decoration:none}
a.tile:hover{border-color:var(--accent)}
.tile .lab{font-size:.72rem;color:var(--muted);text-transform:uppercase;letter-spacing:.06em}
.tile .big{font-size:1.5rem;font-weight:700;font-variant-numeric:tabular-nums;line-height:1.2}
.tile .sub{font-size:.78rem;color:var(--muted)}
.l-red{color:var(--bad)}.l-amber{color:var(--warn)}.l-green{color:var(--ok)}.l-gray{color:var(--fg)}
h2{font-size:1rem;margin:4px 0 0}
.panel{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:10px 14px}
.panel ul{list-style:none;margin:6px 0 0;padding:0;display:flex;flex-direction:column;gap:6px}
.panel li{display:flex;flex-wrap:wrap;gap:4px 8px;align-items:baseline;min-width:0}
.panel li code{margin-left:auto}
.chip{display:inline-block;font-size:.7rem;font-weight:600;padding:0 7px;border-radius:999px;border:1px solid currentColor;white-space:nowrap}
.scroll{overflow-x:auto}
.stages{display:grid;grid-template-columns:160px repeat(var(--n),minmax(70px,1fr));gap:3px;font-size:.76rem;min-width:760px}
.stages .h{color:var(--muted);text-align:center}
.stages .f{font-weight:600;font-size:.82rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;padding:4px 0}
.cell{border-radius:4px;padding:4px 2px;text-align:center;font-variant-numeric:tabular-nums;background:var(--track);color:var(--muted);text-decoration:none;min-height:1.9em}
.cell.done{background:var(--accent);color:var(--panel)}.cell.part{background:var(--accent-soft);color:var(--accent);font-weight:600}
.cell.block{background:transparent;border:1px dashed var(--bad);color:var(--bad);font-weight:600}
a.cell:hover{outline:1px solid var(--accent)}
.hidden-col{display:none}body.show-hidden .hidden-col{display:block}
.kb{display:grid;grid-template-columns:repeat(6,minmax(160px,1fr));gap:8px;min-width:1000px}
.kcol{background:var(--track);border-radius:8px;padding:6px;display:flex;flex-direction:column;gap:6px}
.kcol h3{margin:2px 4px;font-size:.8rem;display:flex;justify-content:space-between}.kcol h3 span{color:var(--muted);font-weight:400}
.kcol.stale{background:color-mix(in srgb,var(--warn) 12%,var(--track))}
.kcard{background:var(--panel);border:1px solid var(--line);border-radius:6px;padding:6px 8px;font-size:.78rem;display:flex;flex-direction:column;gap:2px;min-width:0}
.kcard a{font-weight:600;color:var(--fg);text-decoration:none;overflow-wrap:anywhere}.kcard a:hover{color:var(--accent);text-decoration:underline}
.kcard .km{color:var(--muted);font-size:.7rem;overflow-wrap:anywhere}
.kcard details{font-size:.7rem}.kcard details a{font-weight:400}
table{border-collapse:collapse;width:100%;font-size:.84rem}th,td{text-align:left;padding:6px 8px;border-bottom:1px solid var(--line);vertical-align:top}
th{font-size:.72rem;color:var(--muted);text-transform:uppercase;letter-spacing:.05em}tr:last-child td{border-bottom:none}
.num{font-variant-numeric:tabular-nums}
footer{color:var(--muted);font-size:.78rem}
[role="tabpanel"]{display:flex;flex-direction:column;gap:12px}
.tag{display:inline-block;font-family:var(--m);font-size:.68rem;font-weight:600;padding:0 6px;border-radius:4px;background:var(--accent-soft);color:var(--accent)}
.tag-m{background:var(--track);color:var(--warn)}
.score{font-variant-numeric:tabular-nums;font-weight:700;min-width:2.2ch;text-align:right;color:var(--accent);cursor:help}
ul.work li.more-row{display:none}ul.work.all li.more-row{display:flex}
.seg-btn{margin-top:8px;font:inherit;font-size:.78rem;border:1px solid var(--line);background:var(--panel);color:var(--accent);padding:3px 10px;border-radius:6px;cursor:pointer}
.pcell{display:flex;gap:8px;align-items:center;min-width:140px}
.pbar{flex:1;height:7px;background:var(--track);border-radius:4px;overflow:hidden;min-width:60px}.pbar i{display:block;height:100%;background:var(--accent)}
"""

JS = """
(function(){
  var K='ba-dash-linkmode',mode='local';try{mode=localStorage.getItem(K)||'local'}catch(e){}
  function apply(){
    [].forEach.call(document.querySelectorAll('a[data-gh]'),function(a){
      if(mode==='gh'){a.href=a.getAttribute('data-gh');a.target='_blank';a.rel='noopener'}
      else{a.href=a.getAttribute('data-local');a.removeAttribute('target')}});
    [].forEach.call(document.querySelectorAll('[data-mode]'),function(b){b.setAttribute('aria-pressed',String(b.getAttribute('data-mode')===mode))});
  }
  document.addEventListener('click',function(e){
    var b=e.target.closest&&e.target.closest('[data-mode]');
    if(b){mode=b.getAttribute('data-mode');try{localStorage.setItem(K,mode)}catch(err){}apply();return}
    var mb=e.target.closest&&e.target.closest('#btn-more');
    if(mb){var ul=document.querySelector('ul.work');var on=!ul.classList.contains('all');ul.classList.toggle('all',on);mb.setAttribute('aria-pressed',String(on));mb.textContent=on?'Thu gọn':mb.getAttribute('data-l')||mb.textContent;return}
    var h=e.target.closest&&e.target.closest('#btn-hidden');
    if(h){var on=!document.body.classList.contains('show-hidden');document.body.classList.toggle('show-hidden',on);h.setAttribute('aria-pressed',String(on))}
  });
  var tabs=[].slice.call(document.querySelectorAll('[role="tab"]'));
  function show(t){tabs.forEach(function(b){var on=b===t;b.setAttribute('aria-selected',String(on));document.getElementById(b.getAttribute('aria-controls')).hidden=!on});
    try{localStorage.setItem('ba-dash-tab',t.id)}catch(e){}}
  tabs.forEach(function(b,i){b.addEventListener('click',function(){show(b)});
    b.addEventListener('keydown',function(e){var d=e.key==='ArrowRight'?1:e.key==='ArrowLeft'?-1:0;if(!d)return;var n=tabs[(i+d+tabs.length)%tabs.length];n.focus();show(n)})});
  try{var s=localStorage.getItem('ba-dash-tab');if(s&&document.getElementById(s))show(document.getElementById(s))}catch(e){}
  apply();
})();
"""


def render(m):
    v = m["verdict"]
    out = []
    w = out.append
    title = f"BA Dashboard — invlogis" + (f" · {m['scope']}" if m["scope"] != "project" else "")
    w(f'<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">')
    w(f"<title>{E(title)}</title><style>{CSS}</style></head><body><main class=\"page\">")
    c = m["counts"]
    w('<div class="bar"><b>invlogis</b>'
      f'<span class="muted">{c["features"]} feature · {c["docs_md"]} doc · {c["sources"]} nguồn · {c["backlog_open"]} task · {m["generated"]}</span>'
      '<span class="seg" role="group" aria-label="Mở link bằng"><span class="muted">Mở bằng</span>'
      '<button type="button" data-mode="local" aria-pressed="true">VS Code</button>'
      '<button type="button" data-mode="gh" aria-pressed="false">GitHub</button></span>'
      '<div class="tabs" role="tablist" aria-label="Tab dashboard">'
      '<button role="tab" id="t-today" aria-selected="true" aria-controls="p-today">Hôm nay</button>'
      '<button role="tab" id="t-feat" aria-selected="false" aria-controls="p-feat">Feature</button>'
      '<button role="tab" id="t-kb" aria-selected="false" aria-controls="p-kb">Kanban</button>'
      '<button role="tab" id="t-src" aria-selected="false" aria-controls="p-src">Nguồn khách</button>'
      '<button role="tab" id="t-health" aria-selected="false" aria-controls="p-health">Sức khỏe vault</button>'
      '</div></div>')

    # Hôm nay
    w('<div role="tabpanel" id="p-today" aria-labelledby="t-today">')
    w(f'<div class="verdict v-{v["level"]}"><b>{E(v["title"])}</b><span class="muted">{E(v["summary"])}</span></div>')
    w('<div class="tiles">')
    for t in m["tiles"]:
        inner = (f'<span class="lab">{E(t["label"])}{" ↗" if t.get("path") else ""}</span>'
                 f'<span class="big l-{t["light"]}">{E(str(t["value"]))}</span><span class="sub">{E(t["sub"])}</span>')
        w(link(t.get("path"), inner, t.get("line"), "tile") if t.get("path") else f'<div class="tile">{inner}</div>')
    w("</div>")
    lanes = m["lanes"]
    names = [("review", "Chờ duyệt land"), ("blocked", "Chặn, chờ trả lời"), ("planned", "Card chờ duyệt"), ("running", "Đang chạy")]
    items = [(n, x) for k, n in names for x in lanes.get(k, [])]
    w('<div class="panel"><h2>Chờ bạn</h2><ul>')
    if not items:
        w('<li class="muted">Không có việc nào chờ bạn.</li>')
    for i, (n, x) in enumerate(items, 1):
        steps = f"bước {x.get('steps_done', 0)}/{x.get('steps_total', 0)}" if x.get("steps_total") else ""
        w(f'<li><span class="chip">{E(n)}</span><b>{E(x.get("feature", ""))}</b><span class="muted">{E(x.get("title", ""))} {E(steps)} · {E(x.get("last_log", ""))}</span><code>/queue {i}</code></li>')
    w("</ul></div>")
    work = m["work"]
    w(f'<div class="panel"><h2>Hàng việc ({len(work)}) · xếp theo điểm ưu tiên</h2>'
      '<p class="muted" style="margin:2px 0 0;font-size:.78rem">Điểm = Chặn 40/25 + Hạn 25/15 + Lan 4đ mỗi doc/feature (trần 20) + Tuổi 1đ/2 ngày (trần 15). '
      'Cột <i>Ưu tiên</i> trong backlog: <code>P0</code> luôn lên đầu, <code>để sau</code> luôn xuống cuối.</p><ul class="work">')
    if not work:
        w('<li class="muted">Không có việc nào.</li>')
    for i, x in enumerate(work):
        tip = " + ".join(f"{k} {v}" for k, v in x["parts"].items()) + f" = {x['score']}"
        extra = ' class="more-row"' if i >= 10 else ""
        man = f'<span class="chip">{E(x["manual"])}</span>' if x["manual"] else ""
        due = f'<span class="muted">hạn {E(x["due"])}</span>' if x["due"] else ""
        label = f'{E(x["id"])} · {E(x["title"])}' if x["kind"] == "BL" else E(x["title"])
        w(f'<li{extra}><span class="score" title="{E(tip)}">{x["score"]}</span>'
          f'<span class="tag{" tag-m" if x["kind"] == "Máy" else ""}">{x["kind"]}</span>{man}'
          f'{link(x["path"], label, x.get("line"))}{due}</li>')
    w("</ul>")
    if len(work) > 10:
        w(f'<button type="button" class="seg-btn" id="btn-more" aria-pressed="false" data-l="Xem hết {len(work)} việc">Xem hết {len(work)} việc</button>')
    w("</div></div>")

    # Feature
    w('<div role="tabpanel" id="p-feat" aria-labelledby="t-feat" hidden>')
    w('<p class="muted" style="margin:0">Ô đậm = xong · ô nhạt = đang làm · viền đỏ = đang giữ feature lại · xám = chưa tới. '
      'Bấm ô để mở file. Feature chậm nhất lên đầu. '
      '<button type="button" id="btn-hidden" class="seg" aria-pressed="false" style="border:1px solid var(--line);border-radius:6px;background:var(--panel);color:var(--muted);cursor:pointer;font:inherit;font-size:.78rem;padding:2px 8px">Hiện cột ẩn URD/BRD/PRD</button></p>')
    cols = STAGES + HIDDEN_STAGES
    w(f'<div class="scroll"><div class="stages" style="--n:{len(STAGES)}" id="stages">')
    w("<span></span>" + "".join(f'<span class="h">{E(l)}</span>' for _, l in STAGES)
      + "".join(f'<span class="h hidden-col">{E(l)}</span>' for _, l in HIDDEN_STAGES))
    for r in m["features"]:
        w(f'<span class="f" title="{E(r["feature"])}">{E(r["feature"])}</span>')
        for k, _ in cols:
            ce = r["stages"][k]
            hid = " hidden-col" if k in dict(HIDDEN_STAGES) else ""
            cls = f'cell {ce["state"]}{hid}'
            t = E(ce["text"])
            if ce.get("note"):
                cls_title = f' title="{E(ce["note"])}"'
            else:
                cls_title = ""
            if ce.get("path"):
                w(link(ce["path"], t, ce.get("line"), cls).replace("<a ", f"<a{cls_title} ", 1))
            else:
                w(f'<span class="{cls}"{cls_title}>{t}</span>')
    w("</div></div>")
    w("<style>body.show-hidden #stages{--n:%d}</style>" % len(cols))
    lint_rows = [(r["feature"], r["lint"], r["stages"]["srs"]) for r in m["features"] if r.get("lint")]
    n_fail = sum(l["fail"] for _, l, _ in lint_rows)
    n_warn = sum(l["warn"] for _, l, _ in lint_rows)
    p_open = [p for p in m["params"] if p["open"]]
    audits = [(r["feature"], r["audit"]) for r in m["features"] if r.get("audit")]
    n_screens = sum(r.get("screens", 0) for r in m["features"])
    w('<div class="tiles">')
    first_lint = next(((s_["path"], s_["line"]) for _, l, s_ in lint_rows if l["fail"] or l["warn"]), (None, None))
    inner = (f'<span class="lab">Tầng SaaS ↗</span><span class="big {"l-red" if n_fail else "l-amber" if n_warn else "l-green"}">'
             f'{n_fail} FAIL · {n_warn} WARN</span><span class="sub">saas-layer-lint trên {len(lint_rows)} spec</span>')
    w(link(first_lint[0], inner, first_lint[1], "tile") if first_lint[0] else f'<div class="tile">{inner}</div>')
    inner = (f'<span class="lab">Tham số P chưa chốt ↗</span><span class="big {"l-amber" if p_open else "l-green"}">'
             f'{len(p_open)}/{len(m["params"])}</span><span class="sub">bảng tham số theo khách</span>')
    w(link("docs/_product/tenant-parameters.md", inner, None, "tile"))
    if audits:
        f_, a_ = sorted(audits, key=lambda x: x[1]["date"])[-1]
        inner = (f'<span class="lab">Figma ↗</span><span class="big {"l-red" if a_["cao"] else "l-green"}">'
                 f'{a_["cao"]} · {a_["trung"]} · {a_["thap"]}</span><span class="sub">Cao · Trung · Thấp — audit {E(f_)} {E(a_["date"])} · {n_screens} màn</span>')
        w(link(a_["path"], inner, None, "tile"))
    else:
        w(f'<div class="tile"><span class="lab">Figma</span><span class="big">{n_screens} màn</span><span class="sub">chưa có audit</span></div>')
    w("</div>")
    oq_rows = [o for r in m["features"] for o in r["oq_rows"] if o["open"]]
    w(f'<div class="panel"><h2>Câu hỏi mở ({len(oq_rows)})</h2><div class="scroll"><table><thead><tr><th>Feature</th><th>Mã</th><th>Câu hỏi</th></tr></thead><tbody>')
    for o in oq_rows:
        feat = o["path"].split("/")[1]
        w(f'<tr><td>{E(feat)}</td><td class="mono">{link(o["path"], E(o["id"]), o["line"])}</td><td>{E(o["question"][:160])}</td></tr>')
    w("</tbody></table></div></div></div>")

    # Kanban
    kb = m["kanban"]
    w('<div role="tabpanel" id="p-kb" aria-labelledby="t-kb" hidden>')
    n_child = sum(len(x["children"]) for x in kb["cards"])
    w(f'<p class="muted" style="margin:0">{len(kb["cards"])} doc có status · {n_child} doc đi theo doc chỉ mục · {len(kb["loose"])} doc không thuộc nhóm nào. '
      'Kéo thả để đổi status: đợt P2 (<code>/dashboard sync</code>).</p>')
    w('<div class="scroll"><div class="kb">')
    for key, label in KANBAN:
        cs = [x for x in kb["cards"] if x["col"] == key]
        w(f'<div class="kcol {key}"><h3>{E(label)} <span>{len(cs)}</span></h3>')
        for x in cs:
            meta = " · ".join(s for s in [x["type"], x["feature"], x["updated"],
                                          f"trước: {x['prev']}" if key == "stale" and x["prev"] else ""] if s)
            w(f'<div class="kcard">{link(x["path"], E(x["title"]))}<span class="km">{E(meta)}</span>')
            if x["children"]:
                w(f'<details><summary>+{len(x["children"])} file đi kèm</summary>'
                  + "<br>".join(link(ch, E(ch.split("/")[-1])) for ch in x["children"]) + "</details>")
            w("</div>")
        w("</div>")
    w("</div></div>")
    if kb["loose"]:
        w('<div class="panel"><h2>Doc không có status</h2><ul>' + "".join(f"<li>{link(p, E(p))}</li>" for p in kb["loose"]) + "</ul></div>")
    w("</div>")

    # Nguồn khách
    srcs = m["sources"]
    w('<div role="tabpanel" id="p-src" aria-labelledby="t-src" hidden>')
    w('<p class="muted" style="margin:0">Thanh = mục đã đối chiếu / tổng mục (sổ <code>docs-input/_coverage/</code>). Nguồn ít được xử lý nhất lên đầu. Bấm mã để mở nguồn, bấm số để mở sổ đối chiếu.</p>')
    def src_key(x):
        r = x["ratio"]
        if x["feed"].startswith("➖"):
            return (3, 0, x["id"])
        if r:
            return (1, r[0] / r[1] if r[1] else 1, x["id"])
        return (0, 0, x["id"])
    w('<div class="panel"><div class="scroll"><table><thead><tr><th>Mã</th><th>Tên</th><th>Nhóm</th><th>Đối chiếu</th><th>Feed</th></tr></thead><tbody>')
    for x in sorted(srcs, key=src_key):
        r = x["ratio"]
        pct = int(100 * r[0] / r[1]) if r and r[1] else 0
        bar = (f'<div class="pbar"><i style="width:{pct}%"></i></div>' + link(x["ledger"], f"{r[0]}/{r[1]}", None, "num")) if r else ""
        w(f'<tr><td class="mono">{link("docs-input/" + x["file"], E(x["id"]))}</td><td>{E(x["name"])}</td>'
          f'<td class="muted">{E(x["group"])}</td><td class="pcell">{bar}</td><td>{E(x["feed"].split(" ")[0])}</td></tr>')
    w("</tbody></table></div></div></div>")

    # Sức khỏe
    w('<div role="tabpanel" id="p-health" aria-labelledby="t-health" hidden>')
    sd, sl = m["stale_docs"], m["stale_log"]
    last_up = {}
    for s in sl:
        last_up[s["downstream"]] = s
    w(f'<div class="panel"><h2>Doc stale ({len(sd)})</h2><ul>')
    for d in sd:
        s = last_up.get(d["path"])
        why = f"← {s['upstream']} đổi {s['date']}" if s else ""
        w(f'<li>{link(d["path"], E(d["path"]))}<span class="muted">{E(why)}</span></li>')
    if not sd:
        w('<li class="muted">Không có doc stale.</li>')
    w("</ul></div>")
    dead = [s for s in sl if s["dead"]]
    w(f'<div class="panel"><h2>Dòng log stale trỏ file đã xoá ({len(dead)}/{len(sl)})</h2>'
      '<p class="muted" style="margin:4px 0 0">Nút "Đã biết, reset" sẽ có ở đợt P2 (<code>/dashboard sync</code>).</p><ul>')
    for s in dead:
        w(f'<li><span class="mono">{E(s["downstream"])}</span><span class="muted">← {E(s["upstream"])} · {E(s["date"])}</span></li>')
    w("</ul></div>")
    q = m["quality"]
    crit = m["freshness"].get("critical", [])
    w('<div class="tiles">')
    w(f'<div class="tile"><span class="lab">Độ tươi TB (chỉ theo tuổi)</span><span class="big">{E(str(m["freshness"].get("avg")))}đ</span><span class="sub">{len(crit)} doc &lt; 40đ</span></div>')
    w(f'<div class="tile"><span class="lab">Review quá hạn</span><span class="big">{len(q.get("review_overdue", []))}</span><span class="sub">in-review &gt; 7 ngày</span></div>')
    w(f'<div class="tile"><span class="lab">Doc thiếu links</span><span class="big">{len(q.get("missing_links", []))}</span><span class="sub">urd/brd/prd/srs</span></div>')
    w("</div>")
    if q.get("review_overdue"):
        w('<div class="panel"><h2>Review quá hạn</h2><ul>' + "".join(
            f'<li>{link(r["path"], E(r["path"]))}<span class="muted">{r["days"]} ngày</span></li>' for r in q["review_overdue"]) + "</ul></div>")
    if crit:
        w('<div class="panel"><h2>Doc lâu chưa sửa (&lt; 40đ)</h2><ul>' + "".join(
            f'<li>{link(r["path"], E(r["path"]))}<span class="muted">{r["days"]} ngày · {r["score"]}đ</span></li>' for r in crit) + "</ul></div>")
    w("</div>")

    scope_arg = "" if m["scope"] == "project" else f" {m['scope']}"
    w(f'<footer>Dựng lại: <code>/dashboard{E(scope_arg)}</code> hoặc <code>python3 _scripts/dashboard-build.py{E(" --feature " + m["scope"] if scope_arg else "")}</code> · {m["generated"]}</footer>')
    w(f"</main><script>{JS}</script></body></html>")
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--feature", default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--json", action="store_true", help="in data model, không ghi file")
    ap.add_argument("--summary", action="store_true", help="in số liệu cho bảng L1, không ghi file")
    a = ap.parse_args()

    m = build(a.feature)
    out = Path(a.out) if a.out else ROOT / "docs/_shared" / (f"dashboard-{a.feature}.html" if a.feature else "dashboard.html")
    if a.json:
        print(json.dumps(m, ensure_ascii=False, indent=2, default=str))
        return
    page = render(m)
    if a.summary:
        c = m["counts"]
        print(f"Dashboard: {out.relative_to(ROOT) if out.is_absolute() and ROOT in out.parents else out}")
        print(f"  Verdict: {m['verdict']['title']}")
        print(f"  {c['features']} feature · {c['docs_md']} doc · {c['open_oq']} OQ mở · {c['sources']} nguồn · {c['backlog_open']} task mở")
        print(f"  Ghi đè ~{len(page.encode()) // 1024} KB" + (" (file đã có)" if out.exists() else " (file mới)"))
        return
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")
    print(f"Đã ghi {out} ({len(page.encode()) // 1024} KB)")


if __name__ == "__main__":
    main()
