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
    results = []
    for r in sorted(reqs, key=lambda x: (x.get("createdAt", ""), x.get("id", ""))):
        ok, change, note = check_one(r, seen_ack)
        results.append({"id": r.get("id"), "type": r.get("type"), "path": r.get("path") or r.get("title", ""),
                         "change": change, "ok": ok, "note": note, "req": r})

    if check:
        print("[/dashboard sync] Sẽ thực hiện:")
        print("  # | loại         | đích                                              | thay đổi           | kiểm")
        for i, x in enumerate(results, 1):
            mark = "OK" if x["ok"] is True else "⚠ " + x["note"] if x["ok"] == "confirm" else "❌ " + x["note"]
            print(f"  {i} | {x['type']:<12} | {x['path'][:50]:<50} | {x['change'][:18]:<18} | {mark}")
        n_ok = sum(1 for x in results if x["ok"] is True)
        print(f"\n  {n_ok}/{len(results)} hợp lệ. Mục ❌ sẽ đánh dấu 'rejected' kèm lý do; mục ⚠ giữ 'pending' tới khi anh xác nhận.")
        return

    out, n_bl, bl_rows, acks = [], bl_next(), [], []
    for x in results:
        r = x["req"]
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
    print(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
