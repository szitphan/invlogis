#!/usr/bin/env python3
"""Sinh trang artifact duyệt component (/figma-component --html) từ khung
.claude/skills/figma-component/html-kit/review-page.html.

Đầu vào: design/v2/components/_work/{slug}/page.json (+ check.json nếu đã chạy ds-foundation-check.py --write)
Đầu ra:  design/v2/components/_work/{slug}/{slug}-review.html — publish file này bằng Artifact (cùng đường dẫn
         mỗi lần để giữ một link; capabilities {db:{}, user:{}}).

Dùng: python3 _scripts/ds-component-page.py <slug> [--check]
  --check  chỉ kiểm page.json đủ khoá theo vòng, không ghi.
"""
import base64
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KIT = ROOT / ".claude/skills/figma-component/html-kit/review-page.html"
LOGO = ROOT / "design/brand/innvie-v1/logo-color.png"
WORK = ROOT / "design/v2/components/_work"

NEED = {
    "brainstorm": ["component", "slug", "refs", "ideas", "decisions", "screens", "presets"],
    "preview": ["preview", "values"],
    "foundation": ["values"],
    "review": ["reviews"],
}
ORDER = ["brainstorm", "preview", "foundation", "review"]


def die(msg, code=2):
    print(f"ds-component-page: {msg}", file=sys.stderr)
    sys.exit(code)


def js_json(obj):
    # nhúng an toàn trong <script type=application/json>
    return json.dumps(obj, ensure_ascii=False).replace("</", "<\\/")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        die("thiếu slug")
    d = Path(args[0]) if Path(args[0]).is_dir() else WORK / args[0]
    slug = d.name
    page_p = d / "page.json"
    if not page_p.exists():
        die(f"không thấy {page_p}")
    page = json.loads(page_p.read_text())
    rnd = page.get("round", "brainstorm")
    if rnd not in ORDER:
        die(f"round phải là một trong {ORDER}")
    missing = [k for r in ORDER[:ORDER.index(rnd) + 1] for k in NEED[r] if not page.get(k)]
    if rnd == "foundation" and not (d / "check.json").exists():
        missing.append("check.json (chạy ds-foundation-check.py --write)")
    ideas = page.get("ideas") or []
    warn = []
    if ideas and len(ideas) < 8:
        warn.append(f"chỉ có {len(ideas)} ý tưởng cộng đồng (mục tiêu 8–12)")
    for i in ideas:
        if not i.get("url"):
            warn.append(f"ý tưởng {i.get('id')} thiếu link nguồn")
    for dc in page.get("decisions") or []:
        if len(dc.get("options") or []) < 2:
            warn.append(f"điểm {dc.get('id')} có ít hơn 2 phương án")
    screens = page.get("screens") or []
    if screens and not any(s.get("device") == "mobile" for s in screens):
        warn.append("chưa có màn demo Mobile")
    if screens and not any(s.get("device") != "mobile" for s in screens):
        warn.append("chưa có màn demo Web")
    pids = {p.get("id") for p in page.get("presets") or []}
    for need in ("untitled", "astryx", "rec"):
        if page.get("presets") is not None and need not in pids:
            warn.append(f"thiếu bộ chọn sẵn '{need}'")
    for i in ideas:
        if i.get("id") not in pids:
            warn.append(f"ý tưởng {i.get('id')} chưa có bộ chọn sẵn để xem trên màn")
    dec_ids = {dc.get("id") for dc in page.get("decisions") or []}
    for p in page.get("presets") or []:
        bad = [k for k in (p.get("pick") or {}) if k not in dec_ids]
        if bad:
            warn.append(f"bộ chọn {p.get('id')} trỏ tới điểm không có: {', '.join(bad)}")
    for w in warn:
        print(f"  ⚠ {w}")
    if missing:
        die(f"vòng {rnd} thiếu: {', '.join(missing)}", 1)
    if "--check" in sys.argv:
        print(f"page.json đủ cho vòng {rnd}.")
        return
    check = json.loads((d / "check.json").read_text()) if (d / "check.json").exists() else None
    # Preview khoá theo tổ hợp user đã chốt ở Brainstorm (answers.json dump từ db của artifact)
    ans_p = d / "answers.json"
    if page.get("preview") and ans_p.exists():
        ans = json.loads(ans_p.read_text())
        pick = {}
        for dc in page.get("decisions") or []:
            c = (ans.get(f"brainstorm-{dc['id']}") or {}).get("choice")
            if c is not None:
                pick[dc["id"]] = chr(97 + int(c))
        page["preview"]["pick"] = {**pick, **(page["preview"].get("pick") or {})}
    html = KIT.read_text()
    logo = "data:image/png;base64," + base64.b64encode(LOGO.read_bytes()).decode()
    title = page.get("title") or f"{page['component']} Review"
    html = (html.replace("__TITLE__", title).replace("__LOGO__", logo)
            .replace("/*__PAGE__*/", js_json(page))
            .replace("/*__CHECK__*/", js_json(check) if check else "null"))
    out = d / f"{slug}-review.html"
    out.write_text(html)
    print(f"Đã sinh {out} ({len(html)//1024} KB) · vòng {rnd}")


if __name__ == "__main__":
    main()
