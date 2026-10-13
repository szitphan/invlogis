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
import hashlib
import html
import importlib.util
import json
import os
import re
import subprocess
import sys
from datetime import date, timedelta
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
    start = text[:sec.start(1)].count("\n") + 1 if sec else 0
    for n, line in enumerate((sec.group(1) if sec else "").split("\n")):
        if not line.startswith("| BL-"):
            continue
        c = table_cells(line)
        if len(c) < 6:
            continue
        c += [""] * (10 - len(c))
        rows.append({"id": c[0], "task": c[1], "source": c[2], "done_when": c[3], "state": c[4], "created": c[5],
                     "due": c[8], "manual": c[9], "line": start + n})
    return rows


def line_of(path, pattern):
    """Số dòng (1-based) đầu tiên khớp regex trong file; None nếu không có."""
    for i, l in enumerate(read(ROOT / path).split("\n"), 1):
        if re.search(pattern, l):
            return i
    return None


def cond_text(cond):
    """Dịch điều kiện Xong khi (cú pháp backlog) sang câu đọc được."""
    cond = cond.strip().strip("`")
    if not cond:
        return ""
    if cond == "manual":
        return "Anh tự đóng (đổi Trạng thái thành ✅)"
    out = []
    for part in [x.strip() for x in cond.split("&&")]:
        neg = part.startswith("!")
        body = part[1:] if neg else part
        kind, _, rest = body.partition(":")
        if kind == "exists":
            out.append(("chưa có" if neg else "có") + f" file {rest.split('/')[-1]}")
        elif kind == "grep":
            f_, _, rx = rest.partition(":")
            rx_h = rx.replace("\\", "").replace("^", "").replace("$", "")
            out.append(f"{f_.split('/')[-1]} " + ("hết" if neg else "có") + f" “{rx_h}”")
        elif kind == "fed":
            out.append(f"nguồn {rest} đối chiếu xong")
        elif kind == "branch":
            out.append(f"branch {rest} đã land (xoá)" if neg else f"có branch {rest}")
        else:
            out.append(part)
    return " · và ".join(out)


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
        for ln, line in enumerate(text.split("\n"), 1):
            if not line.startswith("| ") or line.startswith("| Mục") or line.startswith("|---"):
                continue
            c = table_cells(line) + ["", "", ""]
            rows.append({"muc": c[0], "result": c[1], "where": c[2], "note": c[3], "line": ln})
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


PENDING_MARKS = ("⏳", "⬜", "🔄")


def row_feature(r, features):
    """Feature của 1 mục sổ đối chiếu: `➡ f` / path docs/f/ (chắc chắn) hoặc mục còn chờ có nhắc tên f
    ở cột Ở đâu/Ghi chú (đoán — chỉ khi đúng 1 feature được nhắc)."""
    sure = [f for f in features if f"➡ {f}" in r["result"] or f"docs/{f}/" in r["where"]]
    if sure:
        return sure, "sure"  # 1 mục có thể thuộc nhiều feature — tính cho mỗi feature
    if any(m in r["result"] for m in PENDING_MARKS):
        hit = [f for f in features if f in r["where"] + " " + r["note"]]
        if len(hit) == 1:
            return hit, "guess"
    return [], None


def unassigned_rows(ledgers, features):
    """Mục còn chờ (⏳/⬜/🔄) không gắn được feature nào — cần anh hoặc /intake ghi `➡ {feature}`."""
    out = []
    for src, led in sorted(ledgers.items()):
        for r in led["rows"]:
            if any(m in r["result"] for m in PENDING_MARKS) and "➡" not in r["result"] and not row_feature(r, features)[0]:
                out.append({"src": src, "path": led["path"], "line": r["line"], "muc": r["muc"]})
    return out


def source_cell(feature, ledgers, features=()):
    """Cột Nguồn của trục tiến độ: mục sổ đối chiếu thuộc feature (chắc chắn hoặc đoán qua tên feature)."""
    done = total = 0
    redo = pending = False
    first = None
    feats = list(features) or [feature]
    for src, led in sorted(ledgers.items()):
        for r in led["rows"]:
            mine = feature in row_feature(r, feats)[0]
            if not mine:
                continue
            total += 1
            if first is None or (("✅" not in r["result"]) and not first[2]):
                first = (led["path"], r["line"], "✅" not in r["result"])
            if "✅" in r["result"]:
                done += 1
            elif "🔄" in r["result"]:
                redo = True
            elif "➖" not in r["result"]:
                pending = True
    if not total:
        return cell("none", "", note="chưa có mục sổ đối chiếu nào thuộc feature này")
    state = "block" if redo else "part" if pending else "done"
    return cell(state, f"{done}/{total}", first[0], first[1] if first[2] else None,
                note="có mục 🔄 bản mới chưa rà" if redo else "")


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


def stale_acked():
    t = read(ROOT / "_workspace/stale-ack.md")
    return set(re.findall(r"^\| \d{4}-\d{2}-\d{2} \| `([^`]+)` \|", t, re.M))


def oq_history(only=None, weeks=8, today=None):
    """OQ mở/đóng cuối mỗi tuần (Chủ nhật) từ lịch sử git + điểm hôm nay từ working tree.
    Tất định theo trạng thái git. Buổi họp = file docs/meetings/decks/YYYY-MM-DD-*.md."""
    today = today or date.today()
    last_sun = today - timedelta(days=(today.weekday() + 1) % 7 or 7)
    points = []

    def count(lines):
        o = c = 0
        for ln in lines:
            m = re.match(r"^(?:[^:]+:)?docs/([^/]+)/[^:]+:\d+:(\|.*)$", ln)
            fd = m.group(1) if m else ""
            # Lịch sử tính MỌI folder feature lúc đó (kể cả feature đã tách/đổi tên), trừ khi lọc 1 feature.
            if not m or fd.startswith("_") or fd.startswith("zz-") or fd in META_DIRS or (only and fd != only):
                continue
            cells = [x for x in table_cells(m.group(2)) if x]
            if not cells or not re.match(r"^OQ-\d+$", cells[0]):
                continue
            if OQ_CLOSED_RE.match(cells[-1] if len(cells) > 1 else ""):
                c += 1
            else:
                o += 1
        return o, c

    for k in range(weeks - 1, -1, -1):
        d = last_sun - timedelta(days=7 * k)
        code, rev = run(["git", "rev-list", "-1", f"--before={d.isoformat()} 23:59:59", "HEAD"])
        rev = rev.strip()
        if code != 0 or not rev:
            continue
        code, out = run(["git", "grep", "-n", "-E", r"^\| *OQ-[0-9]+", rev, "--", "docs/*.md", "docs/**/*.md"])
        o, c = count(out.splitlines()) if code in (0, 1) else (0, 0)
        points.append({"date": d.isoformat(), "open": o, "closed": c})
    code, out = run(["git", "grep", "-n", "--untracked", "-E", r"^\| *OQ-[0-9]+", "--", "docs/*.md", "docs/**/*.md"])
    o, c = count(out.splitlines()) if code in (0, 1) else (0, 0)
    points.append({"date": today.isoformat(), "open": o, "closed": c, "now": True})
    decks = sorted({p.name[:10] for p in (ROOT / "docs/meetings/decks").glob("*.md") if re.match(r"\d{4}-\d{2}-\d{2}", p.name)})
    return {"points": points, "decks": decks}


def audit_items(path):
    items, level = [], None
    for ln, line in enumerate(read(ROOT / path).split("\n"), 1):
        if line.startswith("## "):
            h = re.match(r"^## Mức (Cao|Trung|Thấp)", line)
            level = h.group(1) if h else None
            continue
        if level and line.startswith("| ") and not line.startswith("| Mã") and not line.startswith("|---"):
            c = table_cells(line) + ["", ""]
            items.append({"level": level, "code": c[0], "what": c[1], "where": c[2], "line": ln})
    return items


def figma_runs():
    rows = []
    for line in read(ROOT / "_workspace/figma-runs.md").split("\n"):
        m = re.match(r"^\| (\d{4}-\d{2}-\d{2}) \d{2}:\d{2} \| ([^|]+?) \| ([^|]+?) \| (bắt đầu|xong) \|$", line)
        if m:
            rows.append({"date": m.group(1), "feature": m.group(2), "flow": m.group(3), "event": m.group(4)})
    return rows


def figma_board(features):
    """Thẻ Review Figma: mục audit mới nhất mỗi feature. Cột do máy đặt:
    Mới · Đang sửa (có /figma-screen đang chạy) · Chờ đo lại (đã chạy xong sau ngày audit) · Xong (audit trước có, audit mới không còn).
    Kéo tay (Bỏ qua + lý do, hoặc chỉnh cột) lưu trong kho của trang artifact, đè lên cột máy."""
    runs = figma_runs()
    cards = []
    for f in features:
        files = sorted(glob.glob(str(ROOT / "docs/reports/figma-audit" / f"*-{f}-figma-audit.md")))
        if not files:
            continue
        latest = rel(Path(files[-1]))
        a_date = Path(files[-1]).name[:10]
        state = {}
        for r in runs:
            if r["feature"] == f:
                state[r["flow"]] = r
        running = any(r["event"] == "bắt đầu" for r in state.values())
        redone = any(r["event"] == "xong" and r["date"] >= a_date for r in state.values())
        col = "dang-sua" if running else "cho-do-lai" if redone else "moi"
        key = lambda it: hashlib.sha1(f"{f}|{it['code']}|{it['what'][:80]}".encode()).hexdigest()[:10]
        cur = audit_items(latest)
        cur_keys = {key(it) for it in cur}
        for it in cur:
            cards.append({"id": key(it), "feature": f, "col": col, "report": latest, "date": a_date, **it})
        if len(files) > 1:
            prev = rel(Path(files[-2]))
            for it in audit_items(prev):
                if key(it) not in cur_keys:
                    cards.append({"id": key(it), "feature": f, "col": "xong", "report": prev,
                                  "date": Path(files[-2]).name[:10], **it})
    lv = {"Cao": 0, "Trung": 1, "Thấp": 2}
    cards.sort(key=lambda c: (c["feature"], lv.get(c["level"], 9), c["code"], c["id"]))
    return cards


def dashboard_state():
    try:
        return json.loads(read(ROOT / ".claude/state/dashboard.json") or "{}")
    except json.JSONDecodeError:
        return {}


def parse_staleness():
    rows = []
    for line in read(ROOT / "_workspace/staleness.md").split("\n"):
        if not line.startswith("| 20"):
            continue
        c = table_cells(line)
        if len(c) < 3:
            continue
        bt = lambda x: (re.search(r"`([^`]+)`", x) or re.search(r"(\S+)", x) or [None, ""])[1]
        up, down = bt(c[1]), bt(c[2])
        rows.append({"date": c[0], "upstream": up, "downstream": down,
                     "dead": not (ROOT / down).exists()})
    ack = stale_acked()
    return [r for r in rows if not (r["dead"] and r["downstream"] in ack)]


# ─── trục tiến độ ───────────────────────────────────────────────────────────

def cell(state, text="", path=None, line=None, note=""):
    """state: done (đậm) · part (nhạt) · block (viền đỏ) · none (xám, chưa tới)."""
    return {"state": state, "text": text, "path": path, "line": line, "note": note}


def feature_row(feature, cov, oqs, lint, orphans, audit, ledgers, features=()):
    base = ROOT / "docs" / feature
    st = {}
    st["nguon"] = source_cell(feature, ledgers, features)

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


def build_queue(rows, backlog, stale_docs, actions, ledgers, worktrees, today, stale_log=()):
    """Hàng việc chung: task BL đang mở + việc máy phát hiện, cùng 1 thang điểm. Ưu tiên tay thắng điểm.
    Mỗi việc có: why (vì sao có việc), done_when (máy kiểm) + done_text (câu đọc được), nơi mở (path + dòng + gợi ý)."""
    by_feat = {r["feature"]: r for r in rows}
    STAGE_KW = {"nguon": r"SRC-\d|nguồn|feed|đối chiếu", "brainstorm": r"brainstorm", "oq": r"\bOQ\b|OQ-\d|câu hỏi|\bchốt",
                "srs": r"-spec\b|\bSRS\b|\bFR-", "userflow": r"userflow|luồng", "figma": r"figma|\bmàn\b|wireframe|screen",
                "usac": r"\bUS-\d|story|\bAC\b", "test": r"\btest"}

    def blocking_for(blob, feats, paths=()):
        """'full' nếu chạm ô chặn chính (ô đỏ đầu tiên) của 1 feature, 'part' nếu chạm ô đỏ khác, None nếu không."""
        level = None
        for f in feats:
            r = by_feat.get(f)
            if not r or not r["blocks"]:
                continue
            touched = set()
            for k in r["blocks"]:
                # Ô OQ trỏ cùng file với brainstorm → chỉ nhận theo từ khoá, không theo đường dẫn.
                cp = r["stages"][k].get("path") if k != "oq" else None
                if (cp and (cp in blob or cp in paths)) or re.search(STAGE_KW[k], blob, re.I):
                    touched.add(k)
            if r["blocks"][0] in touched:
                return "full"
            if touched:
                level = "part"
        return level
    up_of = {}
    for s_ in stale_log:
        up_of[s_["downstream"]] = s_

    def item(kind, id_, title, score, parts, why, done_when, path=None, line=None, hint="",
             doc=None, doc_line=None, doc_hint="", manual="", due=""):
        return {"kind": kind, "id": id_, "title": title, "score": score, "parts": parts, "why": why,
                "done_when": done_when, "done_text": cond_text(done_when), "path": path, "line": line,
                "hint": hint, "doc": doc, "doc_line": doc_line, "doc_hint": doc_hint, "manual": manual, "due": due}

    items = []
    for b in backlog:
        if b["state"].startswith("✅"):
            continue
        blob = f'{b["task"]} {b["source"]} {b["done_when"]}'
        act_blob = f'{b["task"]} {b["done_when"]}'
        feats = [f for f in by_feat if f in act_blob]  # feature việc tác động (không tính cột Nguồn)
        docs_n = len(set(re.findall(r"docs/[\w./-]+\.md", blob)))
        try:
            age = (today - date.fromisoformat(b["created"])).days
        except ValueError:
            age = 0
        # Chặn xét theo nội dung việc + điều kiện Xong khi, KHÔNG theo cột Nguồn (nguồn là nơi phát sinh, không phải nơi việc tác động).
        score, parts = priority_score(blocking_for(act_blob, feats), b["due"], today, len(feats) + docs_n, age)
        doc = next(iter(re.findall(r"((?:docs|docs-input|_scripts|\.claude)/[\w./-]+\.\w+)", blob)), None)
        doc = doc if doc and "*" not in doc and (ROOT / doc).exists() else None
        src = re.sub(r"`", "", b["source"]).strip()
        why = " · ".join(x for x in [f"Nguồn: {src}" if src and src != "—" else "", f"mở từ {b['created']}" if b["created"] else "",
                                     b["state"] if b["state"] not in ("⬜", "") else ""] if x)
        items.append(item("BL", b["id"], re.sub(r"`", "", b["task"]), score, parts, why, b["done_when"],
                          "_workspace/backlog.md", b["line"], f"dòng {b['id']}", doc, None, "tài liệu liên quan",
                          b["manual"], b["due"]))

    # Máy: doc stale gom theo feature (project-level gom chung)
    groups = {}
    for d in stale_docs:
        groups.setdefault(d["feature"] or "_dự án", []).append(d)
    for f, ds in sorted(groups.items()):
        r = by_feat.get(f)
        blocking = blocking_for("", [f], {d["path"] for d in ds}) if r else None
        age = max((d["days_since_update"] for d in ds if d["days_since_update"] >= 0), default=0)
        score, parts = priority_score(blocking, "", today, len(ds), age)
        label = f if f != "_dự án" else "Doc dự án (_shared, _product, meetings)"
        ups = sorted({up_of[d["path"]]["upstream"].split("/")[-1] for d in ds if d["path"] in up_of})
        why = (f"Upstream đổi ({', '.join(ups[:3])}{'…' if len(ups) > 3 else ''}) nên {len(ds)} doc bị đánh stale. "
               "Rà từng doc: không cần sửa → reset (tab Sức khỏe), cần sửa → sửa rồi reset.")
        items.append(item("Máy", f"stale:{f}", f"{label}: {len(ds)} doc stale chờ rà", score, parts, why,
                          " && ".join(f"!grep:{d['path']}:^status: stale" for d in ds),
                          ds[0]["path"], line_of(ds[0]["path"], r"^status:"), "dòng status (doc đầu tiên)"))
    # Máy: OQ mở của feature chưa có task BL nào nhắc tới
    mentioned = " ".join(f'{b["task"]} {b["source"]} {b["done_when"]}' for b in backlog if not b["state"].startswith("✅"))
    for r in rows:
        if r["open_oq"] and r["feature"] not in mentioned:
            o = r["stages"]["oq"]
            score, parts = priority_score("full" if r["blocks"][:1] == ["oq"] else "part", "", today, r["open_oq"], 0)
            items.append(item("Máy", f"oq:{r['feature']}", f"{r['feature']}: {r['open_oq']} câu hỏi mở chưa có task theo dõi",
                              score, parts, "Câu hỏi mở đang chặn feature đi tiếp mà backlog chưa có task nào nhắc tới. "
                              "Chốt qua /deck hoặc hỏi khách.", f"!grep:docs/{r['feature']}/**/*.md:Còn mở",
                              o["path"], o["line"], "câu hỏi mở đầu tiên"))
        lint = r.get("lint") or {}
        if lint.get("fail"):
            score, parts = priority_score("full" if r["blocks"][:1] == ["srs"] else "part", "", today, lint["fail"], 0)
            items.append(item("Máy", f"lint:{r['feature']}", f"{r['feature']}: {lint['fail']} lỗi FAIL tầng SaaS", score, parts,
                              "Quy tắc thiếu nhãn tầng hoặc dùng mã P chưa có trong bảng tham số (saas-layer-lint).", "manual",
                              r["stages"]["srs"]["path"], r["stages"]["srs"]["line"], "dòng lỗi đầu tiên"))
        a = r.get("audit")
        if a and a["cao"]:
            try:
                age = (today - date.fromisoformat(a["date"])).days
            except ValueError:
                age = 0
            score, parts = priority_score("full" if r["blocks"][:1] == ["figma"] else "part", "", today, a["cao"], age)
            cao = [x for x in audit_items(a["path"]) if x["level"] == "Cao"]
            what = re.sub(r"`", "", cao[0]["what"]) if cao else ""
            items.append(item("Máy", f"figma:{r['feature']}", f"Audit Figma {r['feature']}: {a['cao']} mục mức Cao", score, parts,
                              f"Audit {a['date']}: {what[:120]}. Sửa trên Figma rồi chạy lại /figma-audit.",
                              f"grep:docs/reports/figma-audit/*-{r['feature']}-figma-audit.md:\\*\\*Cao 0 ",
                              a["path"], cao[0]["line"] if cao else None, "mục mức Cao"))
    # Máy: nguồn có bản mới (🔄) chưa rà
    for src, led in sorted(ledgers.items()):
        n = sum(1 for x in led["rows"] if "🔄" in x["result"])
        if n:
            score, parts = priority_score(None, "", today, n, 0)
            items.append(item("Máy", f"src:{src}", f"{src} {led['name']}: {n} mục bản mới chưa rà", score, parts,
                              "Khách gửi bản mới; các mục đổi/thêm cần rà lại vào brainstorm.", f"!grep:{led['path']}:🔄",
                              led["path"], line_of(led["path"], "🔄"), "mục 🔄 đầu tiên"))
    # Máy: worktree không có branch feat/*
    for w in worktrees:
        score, parts = priority_score(None, "", today, 0, 0)
        items.append(item("Máy", f"wt:{w['branch']}", f"Worktree {w['branch']} không theo feat/*", score, parts,
                          f"Worktree ở {w['path'].split('/')[-1]} không thuộc quy ước feat/<feature>. Dọn bằng wt.sh drop nếu không dùng.",
                          f"!branch:{w['branch']}"))
    # Máy: việc engine phát hiện (review kẹt, US thiếu AC, CR…)
    for a in actions:
        if "Stale" in a["title"]:
            continue  # đã gom ở nhóm stale
        m = a["metric"]
        age = m.get("days_in_review") or m.get("days_since_update") or m.get("days_since_apply") or 0
        score, parts = priority_score(None, "", today, 1, age)
        st_ = re.search(r"^(Stuck review|US thiếu AC|Draft)", a["title"])
        kind_ = st_.group(1) if st_ else ""
        dw = (f"!grep:{a['target_path']}:^status: in-review" if kind_ == "Stuck review"
              else f"grep:{a['target_path']}:AC-" if kind_ == "US thiếu AC" else "manual")
        title = {"Stuck review": f"Review kẹt {age} ngày: {a['target_path'].split('/')[-1]}",
                 "US thiếu AC": f"Story thiếu AC: {a['target_path'].split('/')[-1]}",
                 "Draft": f"Draft {age} ngày chưa sửa: {a['target_path'].split('/')[-1]}"}.get(kind_, a["title"])
        why = {"Stuck review": f"Doc ở in-review {age} ngày (quá 7). Duyệt (approved), trả về (revisions) hoặc về draft — kéo thẻ ở tab Kanban.",
               "US thiếu AC": "Story chưa có tiêu chí chấp nhận. Chạy /ac.",
               "Draft": "Draft lâu không sửa — còn cần không?"}.get(kind_, "Engine workspace-status phát hiện.")
        items.append(item("Máy", f"act:{a['target_path']}", title, score, parts, why, dw,
                          a["target_path"], line_of(a["target_path"], r"^status:"), "dòng status"))

    rank = lambda i: 0 if i["manual"].upper() == "P0" else 2 if i["manual"].lower() == "để sau" else 1
    items.sort(key=lambda i: (rank(i), -i["score"], i["kind"], i["id"]))
    return items


def light(n, ok, warn):
    return "green" if n <= ok else "amber" if n <= warn else "red"


def build(feature_filter=None, light_mode=False):
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
                                kg_userflow_orphans(f) if uf.exists() else None, latest_figma_audit(f), ledgers,
                                scan_features(None)))
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
                       [] if feature_filter else orphan_worktrees(), today, stale_log)
    history = {"points": [], "decks": []} if light_mode else oq_history(feature_filter, today=today)
    fboard = figma_board(features)
    spec_ = importlib.util.spec_from_file_location("st", ROOT / ".claude/skills/status/engine/status.py")
    try:
        st_mod = importlib.util.module_from_spec(spec_)
        spec_.loader.exec_module(st_mod)
        transitions = {k: sorted(v) for k, v in st_mod.TRANSITIONS.items()}
    except Exception:
        transitions = {}

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
    unassigned = unassigned_rows(ledgers, scan_features(None))
    if not rows:
        verdict = {"level": "gray", "title": "Chưa có feature nào",
                   "summary": "Bắt đầu với /brainstorm hoặc /intake."}
    else:
        level = "pending"  # chấm sau khi có 5 ô: màu tệ nhất trong các ô (bỏ xám); có việc bị chặn chờ trả lời → đỏ
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

    if verdict["level"] == "pending":
        order = {"red": 0, "amber": 1, "green": 2}
        lights = [t["light"] for t in tiles if t["light"] in order]
        worst = min(lights, key=lambda c: order[c]) if lights else "green"
        verdict["level"] = "red" if (lanes.get("blocked") or lint_fail) else worst

    return {
        "unassigned": unassigned,
        "generated": today.isoformat(), "scope": feature_filter or "project", "root": str(ROOT),
        "verdict": verdict, "tiles": tiles, "lanes": lanes, "actions": actions, "work": work,
        "sources": sources, "params": params, "history": history, "figma_board": fboard,
        "transitions": transitions, "state": dashboard_state(),
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
    # GitHub render .md bỏ qua #L → thêm ?plain=1 để mở mã nguồn, tô đúng dòng.
    gh = GITHUB + path + (("?plain=1" if path.endswith(".md") else "") + f"#L{line}" if line else "")
    return (f'<a class="{cls}" href="{E(loc)}" data-local="{E(loc)}" data-gh="{E(gh)}" '
            f'title="{E(path + (f":{line}" if line else ""))}">{label}</a>')


def where(path, line=None, hint=""):
    """Nhãn nơi link tới: tên file · dòng N · gợi ý phần."""
    if not path:
        return ""
    name = path.split("/")[-1]
    return " · ".join(x for x in [name, f"dòng {line}" if line else "", hint] if x)


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
table.work tr.more-row{display:none}table.work.all tr.more-row{display:table-row}
table.work{min-width:980px}table.work td{font-size:.82rem}table.work td.opens a{white-space:nowrap}
table.work td.btns{white-space:nowrap}table.work td.btns .mini{display:block;margin:0 0 4px}
tr.dismissed{display:none}body.show-dismissed tr.dismissed{display:table-row;opacity:.55}
.seg-btn{margin-top:8px;font:inherit;font-size:.78rem;border:1px solid var(--line);background:var(--panel);color:var(--accent);padding:3px 10px;border-radius:6px;cursor:pointer}
.pcell{display:flex;gap:8px;align-items:center;min-width:140px}
.mini{font:inherit;font-size:.72rem;padding:1px 8px;border-radius:999px;border:1px solid var(--accent);background:var(--accent);color:var(--panel);cursor:pointer}
.mini.ghost{background:none;color:var(--accent)}.mini:disabled{opacity:.6;cursor:default;border-style:dashed}
.panel li .mini:first-of-type{margin-left:auto}
li.dismissed{display:none!important}body.show-dismissed li.dismissed{display:flex!important;opacity:.55}
.pendbar{font-size:.78rem;font-weight:600;color:var(--warn);border:1px dashed var(--warn);border-radius:6px;padding:2px 8px}
.kb5{grid-template-columns:repeat(5,minmax(170px,1fr));min-width:900px}
.kbody{display:flex;flex-direction:column;gap:6px;min-height:40px}
.kcol.over{box-shadow:inset 0 0 0 2px var(--accent)}.kcol.bad{box-shadow:inset 0 0 0 2px var(--bad)}
.kcard[draggable="true"]{cursor:grab}
.kcard select{font:inherit;font-size:.7rem;background:var(--bg);color:var(--fg);border:1px solid var(--line);border-radius:4px;max-width:100%}
.kcard .pend{color:var(--warn);font-weight:600;font-size:.7rem}
.frow{display:flex;gap:4px;flex-wrap:wrap;align-items:center}
.reason{font-size:.72rem;display:flex;flex-direction:column;gap:2px}.reason input{font:inherit;font-size:.74rem;padding:2px 4px;border:1px solid var(--line);border-radius:4px;background:var(--bg);color:var(--fg)}
.hist{display:grid;grid-template-columns:auto 1fr auto;gap:4px 10px;align-items:center;font-size:.78rem}
.hb{display:flex;height:12px;background:var(--track);border-radius:3px;overflow:hidden}
.hb .ho{background:var(--accent)}.hb .hc{background:color-mix(in srgb,var(--accent) 35%,var(--track))}
.hl{color:var(--muted);white-space:nowrap}
.pbar{flex:1;height:7px;background:var(--track);border-radius:4px;overflow:hidden;min-width:60px}.pbar i{display:block;height:100%;background:var(--accent)}
"""

JS = """
(function(){
  var K='ba-dash-linkmode',def=window.__DEFMODE||'local',mode=def;try{mode=localStorage.getItem(K)||def}catch(e){}
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
    if(mb){var ul=document.querySelector('.work');var on=!ul.classList.contains('all');ul.classList.toggle('all',on);mb.setAttribute('aria-pressed',String(on));mb.textContent=on?'Thu gọn':mb.getAttribute('data-l')||mb.textContent;return}
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


FIGMA_COLS = [("moi", "Mới"), ("dang-sua", "Đang sửa"), ("cho-do-lai", "Chờ đo lại"), ("xong", "Xong"), ("bo-qua", "Bỏ qua")]


def act(label, key, req, A, cls="act"):
    """Nút tạo yêu cầu (chỉ bản artifact). req lưu vào kho trang, /dashboard sync áp vào repo."""
    if not A:
        return ""
    return (f'<button type="button" class="{cls}" data-key="{E(key)}" data-label="{E(label)}" '
            f"data-req='{E(json.dumps(req, ensure_ascii=False))}'>{E(label)}</button>")


AJS = r"""
(function(){
  var data=JSON.parse(document.getElementById('dash-data').textContent);
  var db=null,pending={},dismissed={},fig={};
  var COLS_DOC=['draft','in-review','revisions','approved','shipped','stale'];
  var COLS_FIG=[['moi','Mới'],['dang-sua','Đang sửa'],['cho-do-lai','Chờ đo lại'],['xong','Xong'],['bo-qua','Bỏ qua']];
  var NAME={'draft':'Draft','in-review':'In Review','revisions':'Revisions','approved':'Approved','shipped':'Shipped','stale':'Stale'};
  function hid(s){var x=5381;for(var i=0;i<s.length;i++){x=((x*33)^s.charCodeAt(i))>>>0}return 'k'+x.toString(36)+s.length.toString(36)}
  function say(t){var n=document.getElementById('sync-note');if(n)n.textContent=t}
  function fail(e){say(e&&e.code==='invalid_argument'?'Không có quyền ghi vào trang này.':'Chưa lưu được, thử lại sau.')}
  function need(){if(!db){say('Chưa kết nối kho dữ liệu của trang — thao tác tạm tắt.');return false}return true}
  function addReq(key,req){if(!need())return;var body=Object.assign({},req,{key:key,state:'pending',createdAt:new Date().toISOString()});
    pending[key]=body;paint();db.collection('requests').doc(hid(key)).set(body).catch(fail)}
  function dropReq(key){if(!need())return;delete pending[key];paint();db.collection('requests').doc(hid(key)).delete().catch(fail)}
  function allowed(c){var st=c.dataset.status,a=(data.transitions[st]||[]).slice();if(st==='stale'&&c.dataset.prev&&a.indexOf(c.dataset.prev)<0)a.unshift(c.dataset.prev);return a}
  function colOf(st){return COLS_DOC.indexOf(st)>=0?st:'draft'}
  function moveDoc(c,to){var key='status:'+c.dataset.path,from=c.dataset.status;
    if(to===from){if(pending[key])dropReq(key);return}
    if(allowed(c).indexOf(to)<0){say('Không chuyển được "'+c.dataset.title+'" sang '+(NAME[to]||to)+'. '+(to==='stale'?'Cột Stale do hook tự đặt.':'Luồng hợp lệ: '+(allowed(c).map(function(x){return NAME[x]||x}).join(', ')||'không có')+'.'));
      var el=document.querySelector('.kcol[data-col="'+to+'"]:not(.fcol)');if(el){el.classList.add('bad');setTimeout(function(){el.classList.remove('bad')},700)}return}
    addReq(key,{type:'status',path:c.dataset.path,from:from,to:to,title:c.dataset.title});
    say('"'+c.dataset.title+'": '+(NAME[from]||from)+' → '+(NAME[to]||to)+'. Chờ /dashboard sync.')}
  function moveFig(c,to){if(!need())return;var id=c.dataset.fid;
    if(to===c.dataset.col){delete fig[id];paint();db.collection('figma').doc(id).delete().catch(fail);return}
    var o={col:to,reason:(fig[id]&&fig[id].reason)||'',at:new Date().toISOString()};fig[id]=o;paint();
    db.collection('figma').doc(id).set(o).catch(fail);
    if(to==='bo-qua'){var inp=c.querySelector('.reason input');if(inp)setTimeout(function(){inp.focus()},0)}}
  function counts(){[].forEach.call(document.querySelectorAll('.kcol'),function(k){var n=k.querySelector('h3 .n'),b=k.querySelector('.kbody');if(n&&b)n.textContent=b.children.length})}
  function paint(){
    var n=Object.keys(pending).length,pe=document.getElementById('pending');
    if(pe){pe.hidden=!n;pe.textContent=n+' yêu cầu chờ /dashboard sync'}
    [].forEach.call(document.querySelectorAll('.act'),function(b){var p=pending[b.dataset.key];b.disabled=!!p;b.textContent=p?'Chờ sync':b.dataset.label});
    [].forEach.call(document.querySelectorAll('.kcard[data-path]'),function(c){
      var p=pending['status:'+c.dataset.path],to=p?p.to:c.dataset.status;
      var body=document.querySelector('.kcol[data-col="'+colOf(to)+'"]:not(.fcol) .kbody');
      if(body&&c.parentNode!==body)body.appendChild(c);
      var b=c.querySelector('.pend');if(b){b.hidden=!p;b.textContent=p?('→ '+(NAME[p.to]||p.to)+' · chờ sync'):''}
      var sel=c.querySelector('.kmove');if(sel){var cur=p?p.to:'';sel.innerHTML='';var o=document.createElement('option');o.value='';o.textContent=p?'Huỷ chuyển':'Chuyển sang…';sel.appendChild(o);
        allowed(c).forEach(function(v){var x=document.createElement('option');x.value=v;x.textContent=(c.dataset.status==='stale'&&v===c.dataset.prev?'Đã biết, reset → ':'')+(NAME[v]||v);if(v===cur)x.selected=true;sel.appendChild(x)});
        sel.hidden=!allowed(c).length}});
    [].forEach.call(document.querySelectorAll('[data-wid]'),function(li){var d=dismissed[hid(li.dataset.wid)];li.classList.toggle('dismissed',!!(d&&d.sig===li.dataset.sig))});
    var nd=document.querySelectorAll('.dismissed').length,t=document.getElementById('btn-dismissed');
    if(t){t.hidden=!nd;t.textContent=(document.body.classList.contains('show-dismissed')?'Ẩn ':'Hiện ')+nd+' việc đã ẩn'}
    [].forEach.call(document.querySelectorAll('.fcard'),function(c){var o=fig[c.dataset.fid],col=o?o.col:c.dataset.col;
      var body=document.querySelector('.fcol[data-col="'+col+'"] .kbody');if(body&&c.parentNode!==body)body.appendChild(c);
      var r=c.querySelector('.reason');if(r){r.hidden=col!=='bo-qua';var inp=r.querySelector('input');if(inp&&document.activeElement!==inp)inp.value=(o&&o.reason)||''}
      var bk=c.querySelector('.fback');if(bk)bk.hidden=!o;
      var sel=c.querySelector('.fmove');if(sel){sel.innerHTML='';var o0=document.createElement('option');o0.value='';o0.textContent='Chuyển sang…';sel.appendChild(o0);
        COLS_FIG.forEach(function(k){if(k[0]===col)return;var x=document.createElement('option');x.value=k[0];x.textContent=k[1];sel.appendChild(x)})}});
    counts()}
  document.addEventListener('click',function(e){
    var b=e.target.closest&&e.target.closest('.act');if(b&&!b.disabled){addReq(b.dataset.key,JSON.parse(b.dataset.req));return}
    var d=e.target.closest&&e.target.closest('.dismiss');if(d){if(!need())return;var id=hid(d.dataset.id);dismissed[id]={sig:d.dataset.sig};paint();db.collection('dismissed').doc(id).set({id:d.dataset.id,sig:d.dataset.sig,at:new Date().toISOString()}).catch(fail);return}
    var sd=e.target.closest&&e.target.closest('#btn-dismissed');if(sd){document.body.classList.toggle('show-dismissed');paint();return}
    var fbk=e.target.closest&&e.target.closest('.fback');if(fbk){var c=fbk.closest('.fcard');moveFig(c,c.dataset.col)}});
  document.addEventListener('change',function(e){
    var s=e.target;if(s.classList.contains('kmove')){var c=s.closest('.kcard');moveDoc(c,s.value||c.dataset.status)}
    else if(s.classList.contains('fmove')&&s.value){moveFig(s.closest('.fcard'),s.value)}
    else if(s.closest&&s.closest('.reason')){if(!need())return;var fc=s.closest('.fcard'),id=fc.dataset.fid,o=Object.assign({},fig[id]||{col:'bo-qua'},{reason:s.value,at:new Date().toISOString()});fig[id]=o;db.collection('figma').doc(id).set(o).catch(fail);say('Đã lưu lý do bỏ qua.')}});
  document.addEventListener('dragstart',function(e){var c=e.target.closest&&e.target.closest('.kcard[draggable="true"]');if(!c)return;
    e.dataTransfer.setData('text/plain',c.dataset.fid?('fig:'+c.dataset.fid):('doc:'+c.dataset.path));e.dataTransfer.effectAllowed='move'});
  [].forEach.call(document.querySelectorAll('.kcol'),function(k){
    k.addEventListener('dragover',function(e){e.preventDefault();k.classList.add('over')});
    k.addEventListener('dragleave',function(){k.classList.remove('over')});
    k.addEventListener('drop',function(e){e.preventDefault();k.classList.remove('over');var v=e.dataTransfer.getData('text/plain')||'';
      if(v.indexOf('fig:')===0&&k.classList.contains('fcol')){var fc=document.querySelector('.fcard[data-fid="'+v.slice(4)+'"]');if(fc)moveFig(fc,k.dataset.col)}
      else if(v.indexOf('doc:')===0&&!k.classList.contains('fcol')){var p=v.slice(4),c=[].filter.call(document.querySelectorAll('.kcard[data-path]'),function(x){return x.dataset.path===p})[0];if(c)moveDoc(c,k.dataset.col)}})});
  paint();
  if(window.claude&&window.claude.use){window.claude.use('db').then(function(d){
    if(!d){say('Chỉ xem: không kết nối được kho dữ liệu của trang.');return}
    db=d;
    db.collection('requests').where('state','==','pending').onSnapshot(function(sn){pending={};sn.docs.forEach(function(x){if(x.exists){var v=x.data();pending[v.key]=v}});paint()},function(){say('Mất kết nối kho dữ liệu.')});
    db.collection('dismissed').onSnapshot(function(sn){dismissed={};sn.docs.forEach(function(x){if(x.exists)dismissed[x.id]=x.data()});paint()},function(){});
    db.collection('figma').onSnapshot(function(sn){fig={};sn.docs.forEach(function(x){if(x.exists)fig[x.id]=x.data()});paint()},function(){});
  },function(){say('Chỉ xem: không kết nối được kho dữ liệu của trang.')})}else{say('Chỉ xem: mở trên claude.ai để thao tác.')}
})();
"""


def render(m, artifact=False):
    A = artifact
    v = m["verdict"]
    out = []
    w = out.append
    title = "Invlogis BA Dashboard" + (f" · {m['scope']}" if m["scope"] != "project" else "")
    url = m.get("state", {}).get("artifact_url", "")
    if A:
        # Artifact: nội dung trang, không doctype/html/head/body (nền tảng tự bọc).
        w(f'<title>{E(title)}</title><style>{CSS}</style><main class="page">')
    else:
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
      '</div>'
      + ('<span class="pendbar" id="pending" hidden></span><span class="muted" id="sync-note" role="status" aria-live="polite"></span>' if A else
         (f'<span class="muted">Thao tác (kéo thẻ, reset stale…): <a href="{E(url)}" target="_blank" rel="noopener">bản artifact</a></span>' if url else ""))
      + '</div>')

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
      '<p class="muted" style="margin:2px 0 6px;font-size:.78rem">Điểm = Chặn 40/25 + Hạn 25/15 + Lan 4đ mỗi doc/feature (trần 20) + Tuổi 1đ/2 ngày (trần 15). '
      'Cột <i>Ưu tiên</i> trong backlog: <code>P0</code> luôn lên đầu, <code>để sau</code> luôn xuống cuối. '
      '<b>BL</b> = task trong backlog (tự đóng khi điều kiện Xong khi đúng) · <b>Máy</b> = việc dashboard tự phát hiện (tự hết khi tín hiệu hết).</p>')
    if not work:
        w('<p class="muted">Không có việc nào.</p>')
    else:
        w('<div class="scroll"><table class="work"><thead><tr><th class="num">Điểm</th><th>Việc</th><th>Vì sao</th>'
          '<th>Xong khi</th><th>Hạn · Ưu tiên</th><th>Mở ở đâu</th>' + ("<th></th>" if A else "") + '</tr></thead><tbody>')
        for i, x in enumerate(work):
            parts = " · ".join(f"{k} {v}" for k, v in x["parts"].items() if v) or "0"
            cls = ["more-row"] if i >= 10 else []
            attrs = ""
            if x["kind"] == "Máy":
                attrs = f' data-wid="{E(x["id"])}" data-sig="{E(x["title"])}"'
            tag = f'<span class="tag{" tag-m" if x["kind"] == "Máy" else ""}">{E(x["id"] if x["kind"] == "BL" else "Máy")}</span>'
            dm = " · ".join(v for v in [E(x["due"]) if x["due"] else "", f'<span class="chip">{E(x["manual"])}</span>' if x["manual"] else ""] if v) or '<span class="muted">—</span>'
            opens = []
            if x["path"]:
                opens.append(link(x["path"], E(where(x["path"], x["line"], x["hint"])), x["line"]))
            if x.get("doc"):
                opens.append(link(x["doc"], E(where(x["doc"], x.get("doc_line"), x.get("doc_hint", ""))), x.get("doc_line")))
            btns = ""
            if A and x["kind"] == "Máy":
                btns = (act("Đưa vào backlog", f"bl:{x['id']}", {"type": "to-backlog", "title": x["title"],
                                                                 "done_when": x.get("done_when") or "manual", "source": "dashboard"}, A, "act mini")
                        + f'<button type="button" class="dismiss mini ghost" data-id="{E(x["id"])}" data-sig="{E(x["title"])}">Đã biết</button>')
            w(f'<tr class="{" ".join(cls)}"{attrs}><td class="num"><span class="score">{x["score"]}</span><br><small class="muted">{E(parts)}</small></td>'
              f'<td>{tag} {E(x["title"])}</td><td class="muted">{E(x["why"])}</td>'
              f'<td title="{E(x["done_when"])}">{E(x["done_text"]) or "<span class=muted>—</span>"}</td>'
              f'<td>{dm}</td><td class="opens">{"<br>".join(opens) or "<span class=muted>—</span>"}</td>'
              + (f'<td class="btns">{btns}</td>' if A else "") + "</tr>")
        w("</tbody></table></div>")
    if len(work) > 10:
        w(f'<button type="button" class="seg-btn" id="btn-more" aria-pressed="false" data-l="Xem hết {len(work)} việc">Xem hết {len(work)} việc</button>')
    if A:
        w('<button type="button" class="seg-btn" id="btn-dismissed" hidden></button>')
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
    un = m.get("unassigned", [])
    if un:
        by_src = {}
        for u in un:
            by_src.setdefault(u["src"], []).append(u)
        w(f'<p class="muted" style="margin:0;font-size:.82rem"><b>{len(un)} mục nguồn chưa gắn feature</b> (còn ⏳/⬜, chưa có <code>➡ feature</code> '
          'nên không tính vào cột Nguồn của feature nào): '
          + " · ".join(link(us[0]["path"], f'{E(src)} ({len(us)})', us[0]["line"]) for src, us in sorted(by_src.items()))
          + '. Mục ⏳/⬜ có nhắc tên feature ở cột Ở đâu/Ghi chú được tính tạm cho feature đó.</p>')
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
    hist = m.get("history", {})
    pts = hist.get("points", [])
    if pts:
        mx = max([p_["open"] + p_["closed"] for p_ in pts] + [1])
        decks = hist.get("decks", [])
        w('<div class="panel"><h2>Câu hỏi mở theo tuần</h2><p class="muted" style="margin:2px 0 6px;font-size:.78rem">'
          'Cuối mỗi tuần (Chủ nhật) theo lịch sử git, dòng cuối là hôm nay. Thanh đậm = còn mở, nhạt = đã đóng. ◆ = tuần có buổi họp deck.</p>'
          '<div class="hist">')
        prev_d = None
        for p_ in pts:
            meet = [d for d in decks if (prev_d is None or d > prev_d) and d <= p_["date"]]
            lab = ("hôm nay" if p_.get("now") else p_["date"][5:].replace("-", "/"))
            w(f'<span class="hl">{E(lab)}{" ◆" if meet else ""}</span>'
              f'<span class="hb" title="{p_["open"]} mở · {p_["closed"]} đã đóng'
              + (f' · họp {", ".join(meet)}' if meet else "") + '">'
              f'<i class="ho" style="width:{100 * p_["open"] / mx:.1f}%"></i><i class="hc" style="width:{100 * p_["closed"] / mx:.1f}%"></i></span>'
              f'<span class="hn num">{p_["open"]} · {p_["closed"]}</span>')
            prev_d = p_["date"]
        w("</div></div>")
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
    how = ("Kéo thẻ hoặc chọn <i>Chuyển sang</i> → thành yêu cầu, áp vào repo khi chạy <code>/dashboard sync</code>."
           if A else (f'Kéo thả đổi status trên <a href="{E(url)}" target="_blank" rel="noopener">bản artifact</a>.' if url
                      else "Kéo thả đổi status trên bản artifact (publish bằng <code>/dashboard</code>)."))
    w(f'<p class="muted" style="margin:0">{len(kb["cards"])} doc có status · {n_child} doc đi theo doc chỉ mục · {len(kb["loose"])} doc không thuộc nhóm nào. {how}</p>')
    w('<div class="scroll"><div class="kb">')
    for key, label in KANBAN:
        cs = [x for x in kb["cards"] if x["col"] == key]
        w(f'<div class="kcol {key}" data-col="{key}"><h3>{E(label)} <span class="n">{len(cs)}</span></h3><div class="kbody">')
        for x in cs:
            meta = " · ".join(s for s in [x["type"], x["feature"], x["updated"],
                                          f"trước: {x['prev']}" if key == "stale" and x["prev"] else ""] if s)
            dattr = (f' data-path="{E(x["path"])}" data-status="{E(x["status"])}" data-prev="{E(x["prev"])}" '
                     f'data-title="{E(x["title"])}"' + (' draggable="true"' if A else ""))
            w(f'<div class="kcard"{dattr}>{link(x["path"], E(x["title"]))}<span class="km">{E(meta)}</span>'
              + ('<span class="pend" hidden></span><select class="kmove" aria-label="Chuyển sang cột"></select>' if A else ""))
            if x["children"]:
                w(f'<details><summary>+{len(x["children"])} file đi kèm</summary>'
                  + "<br>".join(link(ch, E(ch.split("/")[-1])) for ch in x["children"]) + "</details>")
            w("</div>")
        w("</div></div>")
    w("</div></div>")
    # Review Figma
    fb = m.get("figma_board", [])
    if fb:
        w('<h2>Review Figma</h2><p class="muted" style="margin:0">Mục từ báo cáo audit mới nhất. Máy đặt cột: <code>/figma-screen</code> đang chạy → Đang sửa · chạy xong sau ngày audit → Chờ đo lại · '
          'audit sau không còn → Xong. ' + ("Kéo tay để chỉnh; <i>Bỏ qua</i> cần ghi lý do. Lưu ngay trên trang, không cần sync." if A else "Chỉnh tay trên bản artifact.") + '</p>')
        w('<div class="scroll"><div class="kb kb5">')
        for key, label in FIGMA_COLS:
            cs = [x for x in fb if x["col"] == key]
            w(f'<div class="kcol fcol" data-col="{key}"><h3>{E(label)} <span class="n">{len(cs)}</span></h3><div class="kbody">')
            for x in cs:
                lv = {"Cao": "l-red", "Trung": "l-amber", "Thấp": "muted"}.get(x["level"], "")
                w(f'<div class="kcard fcard" data-fid="{E(x["id"])}" data-col="{E(x["col"])}"' + (' draggable="true"' if A else "") + '>'
                  f'<span class="km"><b class="{lv}">{E(x["level"])}</b> · {E(x["feature"])} · {E(x["code"])}</span>'
                  f'<span>{E(re.sub(r"`", "", x["what"])[:160])}</span>'
                  f'<span class="km">{link(x["report"], E(re.sub(r"`", "", x["where"])[:90]))}</span>'
                  + ('<label class="reason" hidden>Lý do bỏ qua <input type="text" maxlength="200"></label>'
                     '<span class="frow"><select class="fmove" aria-label="Chuyển sang cột"></select>'
                     '<button type="button" class="fback mini ghost" hidden>Về cột máy</button></span>' if A else "")
                  + "</div>")
            w("</div></div>")
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
    un_by = {}
    for u in m.get("unassigned", []):
        un_by.setdefault(u["src"], []).append(u)
    w('<div class="panel"><div class="scroll"><table><thead><tr><th>Mã</th><th>Tên</th><th>Nhóm</th><th>Đối chiếu</th><th>Chưa gắn feature</th><th>Feed</th></tr></thead><tbody>')
    for x in sorted(srcs, key=src_key):
        r = x["ratio"]
        pct = int(100 * r[0] / r[1]) if r and r[1] else 0
        bar = (f'<div class="pbar"><i style="width:{pct}%"></i></div>' + link(x["ledger"], f"{r[0]}/{r[1]}", None, "num")) if r else ""
        w(f'<tr><td class="mono">{link("docs-input/" + x["file"], E(x["id"]))}</td><td>{E(x["name"])}</td>'
          f'<td class="muted">{E(x["group"])}</td><td class="pcell">{bar}</td>'
          f'<td class="num">{link(un_by[x["id"]][0]["path"], str(len(un_by[x["id"]])) + " mục", un_by[x["id"]][0]["line"]) if x["id"] in un_by else ""}</td>'
          f'<td>{E(x["feed"].split(" ")[0])}</td></tr>')
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
        ln = line_of(d["path"], r"^status:")
        up = (f'<span class="muted">← upstream </span>{link(s["upstream"], E(where(s["upstream"])))}<span class="muted"> đổi {E(s["date"])}</span>'
              if s and (ROOT / s["upstream"]).exists() else (f'<span class="muted">← {E(s["upstream"])} đổi {E(s["date"])}</span>' if s else ""))
        w(f'<li>{link(d["path"], E(d["path"]) + f" <span class=muted>· dòng {ln}</span>", ln)}{up}'
          + act("Đã biết, reset", f"reset:{d['path']}", {"type": "stale-reset", "path": d["path"]}, A, "act mini")
          + act("Cần rà", f"review:{d['path']}", {"type": "stale-review", "path": d["path"]}, A, "act mini ghost") + "</li>")
    if not sd:
        w('<li class="muted">Không có doc stale.</li>')
    w("</ul></div>")
    dead = [s for s in sl if s["dead"]]
    w(f'<div class="panel"><h2>Dòng log stale trỏ file đã xoá ({len(dead)}/{len(sl)})</h2>'
      + ('<p class="muted" style="margin:4px 0 0">File đích không còn nên không sửa được. Bấm "Đã biết, reset" để ghi vào <code>_workspace/stale-ack.md</code> khi chạy <code>/dashboard sync</code>.</p><ul>'
         if A else '<p class="muted" style="margin:4px 0 0">Xác nhận reset trên bản artifact.</p><ul>'))
    seen_dead = set()
    for s in dead:
        if s["downstream"] in seen_dead:
            continue
        seen_dead.add(s["downstream"])
        w(f'<li><span class="mono">{E(s["downstream"])}</span><span class="muted">← {E(s["upstream"])} · {E(s["date"])}</span>'
          + act("Đã biết, reset", f"ack:{s['downstream']}", {"type": "log-ack", "path": s["downstream"], "upstream": s["upstream"]}, A, "act mini")
          + "</li>")
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
    if A:
        data = {"transitions": m.get("transitions", {}), "generated": m["generated"]}
        # Trong claude.ai link vscode:// thường bị chặn → bản artifact mặc định mở GitHub (đổi được bằng nút).
        w(f'</main><script type="application/json" id="dash-data">{json.dumps(data, ensure_ascii=False)}</script>'
          f"<script>window.__DEFMODE='gh'</script><script>{JS}</script><script>{AJS}</script>")
    else:
        w(f"</main><script>{JS}</script></body></html>")
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--feature", default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--json", action="store_true", help="in data model, không ghi file")
    ap.add_argument("--summary", action="store_true", help="in số liệu cho bảng L1, không ghi file")
    ap.add_argument("--artifact", action="store_true",
                    help="ghi bản artifact (có thao tác, không doctype) — mặc định .claude/state/dashboard-artifact.html")
    ap.add_argument("--line", action="store_true", help="in 1 dòng cho session-init (nhanh, không đọc lịch sử git)")
    a = ap.parse_args()

    if a.line:
        m = build(a.feature, light_mode=True)
        url = m.get("state", {}).get("artifact_url", "")
        n = len(m["work"])
        print(f"  📊 {m['verdict']['title']} · {n} việc — "
              + (f"dashboard: {url} (có thao tác trên trang → /dashboard sync)" if url else "xem: /dashboard"))
        return
    m = build(a.feature)
    if a.artifact:
        out = Path(a.out) if a.out else ROOT / ".claude/state" / (f"dashboard-artifact-{a.feature}.html" if a.feature else "dashboard-artifact.html")
        page = render(m, artifact=True)
        if a.summary:
            print(f"Artifact: {out.relative_to(ROOT)} (~{len(page.encode()) // 1024} KB)")
            return
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page, encoding="utf-8")
        print(f"Đã ghi {out} ({len(page.encode()) // 1024} KB)")
        return
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
