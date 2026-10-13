#!/usr/bin/env python3
"""
dashboard-apply.py — áp các yêu cầu anh bấm trên trang artifact dashboard vào repo (`/dashboard sync`).

Trang artifact không ghi được repo: mỗi thao tác thành 1 yêu cầu trong kho dữ liệu của trang
(collection `requests`). Claude đọc yêu cầu `state: pending` bằng ArtifactData, ghi ra 1 file JSON,
rồi gọi script này:

  python3 _scripts/dashboard-apply.py --check requests.json    kiểm từng yêu cầu → bảng L1 (không ghi gì)
  python3 _scripts/dashboard-apply.py requests.json            áp các yêu cầu hợp lệ, in kết quả JSON

Loại yêu cầu:
  status        {path, from, to}     đổi status doc qua engine /status (apply, hoặc restore khi rời stale về status_prev)
  stale-reset   {path}               doc stale → status trước đó (engine restore)
  stale-review  {path}               thêm task BL "Rà lại {path}", Xong khi doc hết stale
  log-ack       {path, upstream}     dòng log stale trỏ file đã xoá → ghi _workspace/stale-ack.md (staleness.md là file sinh, không sửa)
  to-backlog    {title, done_when, source}  thêm task BL từ việc máy phát hiện
  board-move    {item, from, to}     thẻ tab Luồng việc (gộp /board): kiểm lại với ảnh chụp mới (board-snapshot.py).
                                     Task manual Mở → Xong: script đóng dòng backlog. Card → Đang chạy (duyệt + chạy) và
                                     🔍 → Xong (duyệt land): trả state "claude" — Claude làm theo /dashboard SKILL mục Sync.

"Đã biết" (ẩn việc máy) và di chuyển thẻ Review Figma chỉ sống trong kho của trang — không qua script này.
Mọi đổi status đi qua `.claude/skills/status/engine/status.py` (luồng hợp lệ + changelog do engine lo).
"""
import json
import os
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENGINE = ROOT / ".claude/skills/status/engine/status.py"
BACKLOG = ROOT / "_workspace/backlog.md"
ACK = ROOT / "_workspace/stale-ack.md"
TODAY = date.today().isoformat()
ACK_HEAD = ("# Stale đã xác nhận\n\n"
            "> Dòng log stale trỏ file không còn, anh đã bấm \"Đã biết, reset\" trên dashboard. Ghi bởi "
            "`_scripts/dashboard-apply.py`; `dashboard-build.py` bỏ các dòng này khỏi số \"Stale chờ xác nhận\".\n\n"
            "| Ngày xác nhận | Downstream | Upstream |\n|---|---|---|\n")


def status_of(path):
    p = ROOT / path
    if not p.exists():
        return None, None
    m = re.match(r"^---\n(.*?)\n---\n", p.read_text(encoding="utf-8"), re.S)
    fm = m.group(1) if m else ""
    st = re.search(r"^status:\s*(\S+)", fm, re.M)
    prev = re.search(r"^status_prev:\s*(\S+)", fm, re.M)
    return (st.group(1) if st else None), (prev.group(1) if prev else None)


def engine(args, dry):
    env = dict(os.environ)
    env.setdefault("CLAUDE_SKILL_NAME", "/dashboard")
    env.setdefault("CLAUDE_CHANGELOG_NOTE", "dashboard sync")
    cmd = [sys.executable, str(ENGINE)] + args + (["--dry-run"] if dry else [])
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, env=env)
    return r.returncode, (r.stdout + r.stderr).strip()


def bl_next():
    nums = [int(n) for n in re.findall(r"^\| BL-(\d+)", BACKLOG.read_text(encoding="utf-8"), re.M)]
    return max(nums, default=0) + 1


def bl_add(rows):
    """Chèn dòng vào cuối bảng Đang mở (intake-sync sẽ chuẩn hoá lại khi chạy)."""
    text = BACKLOG.read_text(encoding="utf-8")
    i = text.index("\n## Đã xong")
    head = text[:i].rstrip("\n") + "\n"
    BACKLOG.write_text(head + "".join(rows) + text[i:], encoding="utf-8")


def bl_row(n, task, source, cond):
    esc = lambda s: s.replace("|", "\\|")
    return f"| BL-{n:03d} | {esc(task)} | {esc(source)} | `{cond}` | ⬜ | {TODAY} |  |  |  |  |\n"


def board_snapshot():
    import importlib.util
    spec = importlib.util.spec_from_file_location("bs", ROOT / "_scripts/board-snapshot.py")
    bs = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bs)
    return {i["id"]: i for i in bs.build()["items"]}


def bl_close(task_id, note):
    """Đóng task manual: Trạng thái ✅, Xong = hôm nay, Bằng chứng (rule backlog.md mục 3). intake-sync chuyển dòng sang Đã xong."""
    lines = BACKLOG.read_text(encoding="utf-8").split("\n")
    for i, ln in enumerate(lines):
        if ln.startswith(f"| {task_id} |"):
            c = [x.strip() for x in re.split(r"(?<!\\)\|", ln.strip())[1:-1]]
            c += [""] * (10 - len(c))
            c[4], c[6], c[7] = "✅", TODAY, note
            lines[i] = "| " + " | ".join(c) + " |"
            BACKLOG.write_text("\n".join(lines), encoding="utf-8")
            return True
    return False


def acked():
    if not ACK.exists():
        return set()
    return set(re.findall(r"^\| \d{4}-\d{2}-\d{2} \| `([^`]+)` \|", ACK.read_text(encoding="utf-8"), re.M))


def last_line(out):
    line = out.splitlines()[-1] if out else "engine từ chối"
    return re.sub(r"^❌\s*", "", line)


def check_one(r, seen_ack):
    """Trả (ok, mô tả thay đổi, ghi chú). ok ∈ True | False | 'confirm'."""
    t = r.get("type")
    path = r.get("path", "")
    if t in ("status", "stale-reset", "stale-review"):
        cur, prev = status_of(path)
        if cur is None:
            return False, path, "file không còn hoặc không có status"
    if t == "status":
        frm, to = r.get("from"), r.get("to")
        if cur != frm:
            return False, f"{frm} → {to}", f"status hiện là {cur}, không còn là {frm} — kéo lại trên trang"
        if cur == "stale" and to == prev:
            code, out = engine(["restore", path], True)
        else:
            code, out = engine(["apply", to, path] + (["--confirm-upstream"] if r.get("confirm_upstream") else []), True)
        if code == 3:
            return "confirm", f"{frm} → {to}", "upstream chưa approved/shipped — cần anh xác nhận"
        return code == 0, f"{frm} → {to}", "" if code == 0 else last_line(out)
    if t == "stale-reset":
        if cur != "stale":
            return False, "reset stale", f"doc không còn stale (status {cur})"
        if not prev:
            return False, "reset stale", "thiếu status_prev — dùng /status để chọn status đích"
        code, out = engine(["restore", path], True)
        return code == 0, f"stale → {prev}", "" if code == 0 else last_line(out)
    if t == "stale-review":
        if cur != "stale":
            return False, "thêm task rà", f"doc không còn stale (status {cur})"
        return True, "thêm task BL", f"Rà lại {path}"
    if t == "log-ack":
        if path in seen_ack:
            return False, "ghi stale-ack", "đã xác nhận trước đó"
        if (ROOT / path).exists():
            return False, "ghi stale-ack", "file vẫn còn — dùng reset stale cho doc"
        return True, "ghi stale-ack", f"← {r.get('upstream', '')}"
    if t == "board-move":
        snap = r.get("_snap") or {}
        it = snap.get(r.get("item"))
        if not it:
            return False, "kéo thẻ", "thẻ không còn trong luồng việc (đã đóng hoặc đổi)"
        if it["col"] != r.get("from"):
            return False, "kéo thẻ", f"thẻ đã sang cột {it['col']} từ lúc kéo — kéo lại trên trang"
        if r.get("to") not in it.get("moves", []):
            return False, "kéo thẻ", f"không cho kéo {r.get('from')} → {r.get('to')}"
        if it["kind"] == "task" and r["from"] == "open":
            return True, "đóng task", it["title"][:60]
        if it["kind"] == "run":
            return "claude", "duyệt card + chạy", "Claude: sửa card (approved, run_state running), commit trong worktree, mở Terminal /run-task resume"
        return "claude", "duyệt land", "Claude: làm như /queue làn 🔍 (Figma nháp nếu có → wt.sh land → commit → drop)"
    if t == "to-backlog":
        if not r.get("title") or not r.get("done_when"):
            return False, "thêm task BL", "thiếu tên việc hoặc điều kiện Xong khi"
        return True, "thêm task BL", r["title"][:80]
    return False, t or "?", "loại yêu cầu không hỗ trợ"


def main():
    a = sys.argv[1:]
    check = "--check" in a
    files = [x for x in a if not x.startswith("--")]
    if len(files) != 1:
        print(__doc__)
        sys.exit(2)
    reqs = json.loads(Path(files[0]).read_text(encoding="utf-8"))
    if isinstance(reqs, dict):
        reqs = reqs.get("requests", [])
    seen_ack = acked()
    snap = board_snapshot() if any(r.get("type") == "board-move" for r in reqs) else {}
    for r in reqs:
        if r.get("type") == "board-move":
            r["_snap"] = snap
    results = []
    for r in sorted(reqs, key=lambda x: (x.get("createdAt", ""), x.get("id", ""))):
        ok, change, note = check_one(r, seen_ack)
        results.append({"id": r.get("id"), "type": r.get("type"), "path": r.get("path") or r.get("item") or r.get("title", ""),
                         "change": change, "ok": ok, "note": note, "req": r})

    if check:
        print("[/dashboard sync] Sẽ thực hiện:")
        print("  # | loại         | đích                                              | thay đổi           | kiểm")
        for i, x in enumerate(results, 1):
            mark = ("OK" if x["ok"] is True else "⚠ " + x["note"] if x["ok"] == "confirm"
                    else "▶ " + x["note"] if x["ok"] == "claude" else "❌ " + x["note"])
            print(f"  {i} | {x['type']:<12} | {x['path'][:50]:<50} | {x['change'][:18]:<18} | {mark}")
        n_ok = sum(1 for x in results if x["ok"] is True)
        print(f"\n  {n_ok}/{len(results)} hợp lệ. Mục ❌ sẽ đánh dấu 'rejected' kèm lý do; mục ⚠ giữ 'pending' tới khi anh xác nhận.")
        return

    out, n_bl, bl_rows, acks = [], bl_next(), [], []
    for x in results:
        r = x["req"]
        if x["ok"] == "claude":  # việc cần Claude làm tiếp (duyệt card + chạy / duyệt land) — không đánh dấu xong ở đây
            out.append({"id": x["id"], "state": "claude", "note": x["note"], "item": r.get("item"), "action": x["change"]})
            continue
        if x["ok"] is not True:
            out.append({"id": x["id"], "state": "pending" if x["ok"] == "confirm" else "rejected", "note": x["note"]})
            continue
        t = r["type"]
        if t == "status":
            cur, prev = status_of(r["path"])
            code, msg = engine(["restore", r["path"]] if (cur == "stale" and r["to"] == prev) else
                               ["apply", r["to"], r["path"]] + (["--confirm-upstream"] if r.get("confirm_upstream") else []), False)
        elif t == "stale-reset":
            code, msg = engine(["restore", r["path"]], False)
        elif t == "stale-review":
            bl_rows.append(bl_row(n_bl, f"Rà lại `{r['path']}` theo upstream đã đổi (từ dashboard)", "dashboard",
                                  f"!grep:{r['path']}:^status: stale"))
            code, msg, n_bl = 0, f"BL-{n_bl:03d}", n_bl + 1
        elif t == "to-backlog":
            bl_rows.append(bl_row(n_bl, r["title"] + " (từ dashboard)", r.get("source") or "dashboard", r["done_when"]))
            code, msg, n_bl = 0, f"BL-{n_bl:03d}", n_bl + 1
        elif t == "board-move":
            ok_ = bl_close(r["item"], f"kéo trên dashboard {TODAY}")
            code, msg = (0, "đã đóng task") if ok_ else (1, "không tìm thấy dòng backlog")
        elif t == "log-ack":
            acks.append(f"| {TODAY} | `{r['path']}` | `{r.get('upstream', '')}` |\n")
            code, msg = 0, "stale-ack"
        out.append({"id": x["id"], "state": "applied" if code == 0 else "rejected",
                    "note": msg if code == 0 else (msg.splitlines()[-1] if msg else "lỗi")})
    if bl_rows:
        bl_add(bl_rows)
    if acks:
        if not ACK.exists():
            ACK.write_text(ACK_HEAD, encoding="utf-8")
        with ACK.open("a", encoding="utf-8") as f:
            f.writelines(acks)
    for r in reqs:
        r.pop("_snap", None)
    print(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
