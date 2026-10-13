#!/usr/bin/env python3
"""
figma-runs.py — sổ lần chạy /figma-screen, để bảng Review Figma của /dashboard tự chuyển cột.

  bắt đầu chạy trên flow  → mục audit của feature sang "Đang sửa"
  chạy xong               → sang "Chờ đo lại" (audit lần sau quyết định Xong / bật về Mới)

Dùng:
  python3 _scripts/figma-runs.py start <feature> <flow-slug>
  python3 _scripts/figma-runs.py done  <feature> <flow-slug>
  python3 _scripts/figma-runs.py list               in lần chạy đang mở (có "bắt đầu", chưa "xong")

Ghi vào `_workspace/figma-runs.md` (append, 1 dòng/sự kiện). Không đụng file nào khác.
"""
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG = ROOT / "_workspace" / "figma-runs.md"
HEAD = ("# Lần chạy /figma-screen\n\n"
        "> Sinh bởi `_scripts/figma-runs.py` — `/figma-screen` ghi \"bắt đầu\" sau khi duyệt kế hoạch và \"xong\" khi báo kết quả.\n"
        "> `/dashboard` đọc để chuyển cột bảng Review Figma. Đừng sửa tay.\n\n"
        "| Lúc | Feature | Flow | Sự kiện |\n|---|---|---|---|\n")


def rows():
    if not LOG.exists():
        return []
    out = []
    for line in LOG.read_text(encoding="utf-8").split("\n"):
        m = re.match(r"^\| (\d{4}-\d{2}-\d{2} \d{2}:\d{2}) \| ([^|]+?) \| ([^|]+?) \| (bắt đầu|xong) \|$", line)
        if m:
            out.append({"at": m.group(1), "feature": m.group(2), "flow": m.group(3), "event": m.group(4)})
    return out


def open_runs():
    state = {}
    for r in rows():
        key = (r["feature"], r["flow"])
        state[key] = r if r["event"] == "bắt đầu" else None
    return [v for v in state.values() if v]


def main():
    a = sys.argv[1:]
    if a[:1] == ["list"]:
        for r in open_runs():
            print(f'{r["at"]}  {r["feature"]} / {r["flow"]}  (đang chạy)')
        return
    if len(a) != 3 or a[0] not in ("start", "done"):
        print(__doc__)
        sys.exit(2)
    ev = "bắt đầu" if a[0] == "start" else "xong"
    feature, flow = a[1].strip(), a[2].strip()
    if not re.match(r"^[a-z0-9-]+$", feature) or not re.match(r"^[a-z0-9-]+$", flow):
        print("feature và flow phải là slug kebab-case", file=sys.stderr)
        sys.exit(2)
    LOG.parent.mkdir(parents=True, exist_ok=True)
    if not LOG.exists():
        LOG.write_text(HEAD, encoding="utf-8")
    with LOG.open("a", encoding="utf-8") as f:
        f.write(f"| {datetime.now():%Y-%m-%d %H:%M} | {feature} | {flow} | {ev} |\n")
    print(f"[figma-runs] {feature}/{flow}: {ev}")


if __name__ == "__main__":
    main()
