#!/usr/bin/env python3
"""Hàng đợi "Chờ bạn" — gom việc đang cần người dùng trong repo: nguồn số liệu duy nhất cho /queue,
dòng tóm tắt của session-init và làn "Chờ bạn" của /dashboard.

Bốn làn (thứ tự = thứ tự ưu tiên hiển thị):
  review   🔍 chờ duyệt land   — task 🔍 trong _workspace/backlog.md (wt.sh ready), kèm báo cáo run card nếu có
  blocked  ⛔ chặn, chờ trả lời — run card run_state: blocked (còn câu hỏi chưa trả lời ở Mục 6)
  planned  📝 card chờ duyệt    — run card run_state: planned (Cửa 1 chưa duyệt)
  running  ⚙ đang chạy          — run card run_state: running + worktree feat/* chưa báo ready (chỉ để xem)

Run card: docs/{feature}/_runs/*.md — ở checkout chính VÀ trong từng worktree .claude/worktrees/*/
(card sống trong worktree khi đang chạy; bản worktree ưu tiên hơn bản main cùng đường dẫn).
Card run_state: review mà branch đã bị drop → coi là đã land, không hiện.

Dùng:
  python3 _scripts/queue.py                 bảng 4 làn
  python3 _scripts/queue.py --json          dữ liệu cho /dashboard, /queue
  python3 _scripts/queue.py --summary       1 dòng cho session-init ("" khi không có gì chờ)
  python3 _scripts/queue.py check "<cond>"  chấm điều kiện Xong khi (cú pháp backlog) — exit 0 đúng / 1 sai
"""
import glob
import importlib.util
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BACKLOG = "_workspace/backlog.md"
LANES = [("review", "🔍 Chờ duyệt land"), ("blocked", "⛔ Chặn, chờ trả lời"),
         ("planned", "📝 Card chờ duyệt"), ("running", "⚙ Đang chạy")]


def git(*a, cwd=ROOT):
    try:
        r = subprocess.run(["git", "-C", cwd, *a], capture_output=True, text=True, timeout=10)
        return r.stdout.strip() if r.returncode == 0 else None
    except Exception:
        return None


def main_dir():
    common = git("rev-parse", "--path-format=absolute", "--git-common-dir")
    return os.path.dirname(common) if common else ROOT


def worktrees(md):
    out, cur = [], {}
    for ln in (git("worktree", "list", "--porcelain", cwd=md) or "").splitlines() + [""]:
        if ln.startswith("worktree "):
            cur = {"dir": ln[9:]}
        elif ln.startswith("branch "):
            cur["branch"] = ln[7:].replace("refs/heads/", "")
        elif not ln and cur.get("branch", "").startswith("feat/"):
            br = cur["branch"]
            head = git("rev-parse", br, cwd=md)
            ready = git("config", "--get", f"branch.{br}.wtready", cwd=md)
            cur.update(slug=br[5:], ahead=int(git("rev-list", "--count", f"main..{br}", cwd=md) or 0),
                       dirty=len((git("status", "--porcelain", cwd=cur["dir"]) or "").splitlines()),
                       ready=("" if not ready else "ok" if ready == head else "changed"))
            out.append(cur)
            cur = {}
    return out


def frontmatter(txt):
    m = re.match(r"^---\n(.*?)\n---\n", txt, re.S)
    fm = {}
    for ln in (m.group(1).splitlines() if m else []):
        k, _, v = ln.partition(":")
        if v and not ln.startswith(" "):
            fm[k.strip()] = v.split("#")[0].strip()
    return fm


def section(txt, num):
    m = re.search(rf"^## {num}\..*?$(.*?)(?=^## \d+\.|\Z)", txt, re.M | re.S)
    return m.group(1) if m else ""


def table_rows(block):
    rows = [ln for ln in block.splitlines() if ln.startswith("|") and not re.match(r"^\|[\s\-|:]+\|$", ln)]
    return [[c.strip() for c in r.strip("|").split("|")] for r in rows[1:]]  # bỏ header


def read_card(path, md):
    txt = open(path, encoding="utf-8").read()
    fm = frontmatter(txt)
    title = (re.search(r"^# (?:Run:\s*)?(.+)$", txt, re.M) or [None, os.path.basename(path)])[1]
    steps = table_rows(section(txt, 3))
    done = sum(1 for r in steps if len(r) > 6 and r[6].startswith("✅"))
    qs = [r for r in table_rows(section(txt, 6)) if len(r) > 5 and r[2] and not r[5]]
    log = [ln[2:] for ln in section(txt, 8).splitlines() if ln.startswith("- ")]
    rel = os.path.relpath(path, md)
    return {"path": rel, "feature": fm.get("feature", ""), "title": title.strip(),
            "run_state": fm.get("run_state", ""), "mode": fm.get("mode", ""),
            "branch": fm.get("branch", ""), "approved": fm.get("approved", ""),
            "updated": fm.get("updated", ""), "steps_done": done, "steps_total": len(steps),
            "open_questions": len(qs), "last_log": log[-1] if log else ""}


def cards(md, wts):
    found = {}
    for base in [md] + [w["dir"] for w in wts]:
        for p in sorted(glob.glob(os.path.join(base, "docs", "*", "_runs", "*.md"))):
            key = os.path.relpath(p, base)
            if base != md or key not in found:  # bản trong worktree thắng bản main
                found[key] = p
    return [read_card(p, md) for p in found.values()]


def review_tasks(md):
    p = os.path.join(md, BACKLOG)
    if not os.path.exists(p):
        return []
    out = []
    for ln in open(p, encoding="utf-8"):
        if ln.startswith("| BL-"):
            c = [x.strip() for x in ln.strip().strip("|").split("|")]
            if len(c) > 4 and c[4].startswith("🔍"):
                br = (re.search(r"`(feat/[^`]+)`", c[2]) or [None, ""])[1]
                out.append({"id": c[0], "what": c[1], "branch": br, "state": c[4], "since": c[5] if len(c) > 5 else ""})
    return out


def collect():
    md = main_dir()
    wts = worktrees(md)
    live = {w["branch"] for w in wts} | {b for b in (git("for-each-ref", "--format=%(refname:short)", "refs/heads/feat/", cwd=md) or "").splitlines()}
    cs = [c for c in cards(md, wts) if not (c["run_state"] in ("review", "done") and c["branch"] not in live)]
    by_branch = {}
    for c in cs:
        by_branch.setdefault(c["branch"], []).append(c)
    lanes = {k: [] for k, _ in LANES}
    for t in review_tasks(md):
        t["cards"] = [c["path"] for c in by_branch.get(t["branch"], [])]
        lanes["review"].append(t)
    for c in cs:
        if c["run_state"] in ("blocked", "planned", "running"):
            lanes[c["run_state"]].append(c)
    carded = {c["branch"] for c in cs if c["run_state"] in ("running", "blocked", "planned", "review")}
    for w in wts:
        if not w["ready"] and w["branch"] not in carded:  # worktree làm tay, không có run card
            lanes["running"].append({"path": "", "feature": w["slug"], "title": "(làm tay, không có run card)",
                                     "branch": w["branch"], "run_state": "manual", "steps_done": 0,
                                     "steps_total": 0, "open_questions": 0,
                                     "last_log": f"{w['ahead']} commit · {w['dirty']} file chưa commit"})
    return {"main": md, "worktrees": wts, "lanes": lanes,
            "waiting_on_you": len(lanes["review"]) + len(lanes["blocked"]) + len(lanes["planned"])}


def render(d):
    out = [f"Chờ bạn: {d['waiting_on_you']} việc"]
    n = 0
    for key, label in LANES:
        items = d["lanes"][key]
        out.append(f"\n{label} ({len(items)})")
        if not items:
            out.append("   —")
        for it in items:
            n += 1
            if key == "review":
                out.append(f"  [{n}] {it['id']} {it['what']} · {it['state']} · từ {it['since']}")
                for c in it["cards"]:
                    out.append(f"       run card: {c}")
            else:
                prog = f"{it['steps_done']}/{it['steps_total']} bước" if it["steps_total"] else ""
                extra = f" · {it['open_questions']} câu hỏi" if key == "blocked" else ""
                out.append(f"  [{n}] {it['feature']} — {it['title']} · {prog}{extra}".rstrip(" ·"))
                if it["path"]:
                    out.append(f"       {it['path']}")
                if it["last_log"]:
                    out.append(f"       ↳ {it['last_log']}")
    return "\n".join(out)


def main(argv):
    if len(argv) > 2 and argv[1] == "check":
        spec = importlib.util.spec_from_file_location("intake_sync", os.path.join(ROOT, "_scripts", "intake-sync.py"))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        ok, ev = mod.check(argv[2], {})
        print(("✅ " + ev) if ok else "❌ chưa thoả")
        sys.exit(0 if ok else 1)
    d = collect()
    if "--json" in argv:
        print(json.dumps(d, ensure_ascii=False, indent=1))
    elif "--summary" in argv:
        if d["waiting_on_you"] or d["lanes"]["running"]:
            L = d["lanes"]
            print(f"  ⏳ Chờ bạn: {d['waiting_on_you']} (🔍 {len(L['review'])} duyệt land · ⛔ {len(L['blocked'])} chặn · "
                  f"📝 {len(L['planned'])} card) · ⚙ {len(L['running'])} đang chạy — /queue để xem")
    else:
        print(render(d))


if __name__ == "__main__":
    main(sys.argv)
