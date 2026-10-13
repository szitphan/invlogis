#!/usr/bin/env python3
"""Ảnh chụp thẻ cho board kéo-thả (/board) — JSON 1 document `board/state` trong db của artifact.

Repo là nguồn sự thật: script chỉ ĐỌC (queue.py + _workspace/backlog.md + run card), không ghi gì.
Phiên điều phối (/board sync) đẩy JSON này lên db; trang chỉ gửi yêu cầu chuyển thẻ (db `requests`).

Mỗi thẻ: id, kind (task|run), col, title, feature, detail, moves (cột được phép kéo sang).
Cột: open ⬜ · planned 📝 · running ⚙ · blocked ⛔ · review 🔍 · done ✅
Thao tác kéo hợp lệ (phiên điều phối kiểm lại lần nữa trước khi áp):
  task manual   open    → done     đóng task
  run card      planned → running  duyệt card (Cửa 1) + mở Terminal chạy /run-task resume
  task 🔍       review  → done     duyệt land (land + commit + drop)

  python3 _scripts/board-snapshot.py            JSON ra stdout
  python3 _scripts/board-snapshot.py --out F    ghi file F (để ArtifactData đọc bằng file_path)
"""
import importlib.util
import json
import os
import re
import sys
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("queue_mod", os.path.join(ROOT, "_scripts", "queue.py"))
Q = importlib.util.module_from_spec(spec)
spec.loader.exec_module(Q)

DONE_KEEP = 12          # số task ✅ gần nhất giữ lại cho cột Xong
DETAIL_MAX = 1800       # cắt chi tiết để document < 256 KiB


def backlog_rows(md):
    p = os.path.join(md, "_workspace/backlog.md")
    head = ["ID", "Việc", "Nguồn", "Xong khi", "Trạng thái", "Tạo", "Xong", "Bằng chứng"]
    rows = []
    for ln in open(p, encoding="utf-8") if os.path.exists(p) else []:
        if ln.startswith("| BL-"):
            c = [x.strip() for x in ln.strip().strip("|").split("|")]
            rows.append(dict(zip(head, c + [""] * (len(head) - len(c)))))
    return rows


def plain(s):
    return re.sub(r"`", "", s or "").strip()


def card_text(md, rel, num):
    p = os.path.join(md, rel)
    if not os.path.exists(p):
        return ""
    txt = open(p, encoding="utf-8").read()
    return Q.section(txt, num).strip()[:DETAIL_MAX]


def worktree_item(c, w, md):
    """Worktree không có run card — nói rõ đang ở đâu và làm gì tiếp."""
    slug, ahead, dirty = c["feature"], w.get("ahead", 0), w.get("dirty", 0)
    rel = os.path.relpath(w.get("dir", ""), md) if w.get("dir") else f".claude/worktrees/{slug}"
    if not ahead and not dirty:
        col, title, meta = "open", f"Worktree {slug} trống — chưa bắt đầu", "0 commit · không có file sửa dở · chưa có run card"
        nxt = (f"Việc tiếp:\n• Giao AI chạy: /run-task {slug} \"<mục tiêu>\"\n"
               f"• Hoặc làm tay: mở terminal tại {rel} rồi chạy claude\n"
               f"• Không cần nữa: _scripts/wt.sh drop {slug}")
    elif not ahead:
        col, title, meta = "running", f"Đang sửa tay trong worktree {slug}", f"{dirty} file chưa commit · chưa có run card"
        nxt = f"Đang có người sửa tại {rel}. Xong thì commit trong worktree rồi _scripts/wt.sh ready {slug} \"<tóm tắt>\"."
    else:
        col, title, meta = "running", f"Worktree {slug}: {ahead} commit, chưa báo xong", f"{ahead} commit · {dirty} file chưa commit · chưa có run card"
        nxt = f"Xong việc thì chạy _scripts/wt.sh ready {slug} \"<tóm tắt>\" — thẻ sẽ sang Chờ duyệt land."
    return {"id": "wt:" + c["branch"], "kind": "worktree", "col": col, "title": title, "feature": slug,
            "detail": nxt, "meta": meta, "moves": []}


def build():
    d = Q.collect()
    md = d["main"]
    wts = {w["branch"]: w for w in d["worktrees"]}
    items = []
    review_ids = {t["id"] for t in d["lanes"]["review"]}
    for t in d["lanes"]["review"]:
        rep = "\n\n".join(card_text(md, c, 9) for c in t["cards"]) or "(không có run card — review bằng /queue)"
        items.append({"id": t["id"], "kind": "task", "col": "review", "title": plain(t["what"]),
                      "feature": t["branch"].replace("feat/", ""), "detail": rep,
                      "meta": t["state"], "moves": ["done"]})
    for key in ("blocked", "planned", "running"):
        for c in d["lanes"][key]:
            if not c["path"]:  # worktree không có run card
                items.append(worktree_item(c, wts.get(c["branch"], {}), md))
                continue
            detail = card_text(md, c["path"], 6) if key == "blocked" else card_text(md, c["path"], 1)
            items.append({"id": "run:" + c["path"], "kind": "run", "col": key, "title": c["title"],
                          "feature": c["feature"], "detail": detail,
                          "meta": f"{c['steps_done']}/{c['steps_total']} bước" + (f" · {c['open_questions']} câu hỏi" if key == "blocked" else "")
                                  + (f" · {c['last_log']}" if c["last_log"] else ""),
                          "moves": ["running"] if key == "planned" else []})
    shown = {i["id"][3:] for i in items if i["kind"] == "worktree"} | {t["branch"] for t in d["lanes"]["review"]}
    carded = {c["branch"] for k in ("blocked", "planned", "running") for c in d["lanes"][k] if c["path"]}
    for br, w in wts.items():  # worktree trống (queue.py không tính là đang chạy) vẫn hiện ở cột Mở
        if br not in shown and br not in carded and not w.get("ready"):
            items.append(worktree_item({"feature": w["slug"], "branch": br}, w, md))
    rows = backlog_rows(md)
    done = []
    for r in rows:
        if r["ID"] in review_ids:
            continue
        st = r["Trạng thái"]
        if st.startswith("✅"):
            done.append(r)
            continue
        manual = plain(r["Xong khi"]) == "manual"
        items.append({"id": r["ID"], "kind": "task", "col": "open", "title": plain(r["Việc"]),
                      "feature": "", "detail": f"Xong khi: {plain(r['Xong khi'])}\nNguồn: {plain(r['Nguồn'])}",
                      "meta": f"{st} · {r['Tạo']}", "moves": ["done"] if manual else []})
    done.sort(key=lambda r: r["Xong"], reverse=True)
    for r in done[:DONE_KEEP]:
        items.append({"id": r["ID"], "kind": "task", "col": "done", "title": plain(r["Việc"]), "feature": "",
                      "detail": plain(r["Bằng chứng"]), "meta": r["Xong"], "moves": []})
    return {"updated_at": datetime.now().strftime("%Y-%m-%d %H:%M"), "waiting_on_you": d["waiting_on_you"],
            "items": items}


if __name__ == "__main__":
    data = build()
    out = json.dumps(data, ensure_ascii=False)
    if "--out" in sys.argv:
        open(sys.argv[sys.argv.index("--out") + 1], "w", encoding="utf-8").write(out)
        print(f"{len(data['items'])} thẻ · {len(out)//1024} KiB")
    else:
        print(out)
