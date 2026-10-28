#!/usr/bin/env python3
"""Tách "css" của page.json (/figma-component --html) thành CSS component và CSS khung màn demo ("cssScreen").

Vì sao: ds-foundation-check chấm mọi giá trị trần trong "css". Màn demo (vỏ ứng dụng, bảng dữ liệu mẫu, lề trang) không
lên Figma, để chung thì đếm thành hàng trăm dòng "Chưa khai" giả và làm --bind ra nhiều ứng viên sai.

Cách xếp một rule: lấy class ở phần chủ (compound cuối) của từng bộ chọn.
  - class có trong phần tử component (cây con của phần tử data-cmp ở screens, hoặc bảng biến thể preview.blocks/demos) → component
  - phần tử có data-show / data-any theo phương án (D1:…) hoặc trạng thái (state:…) cũng là component (lớp mở, banner…)
  - bộ chọn bắt đầu bằng .pv[data-…] / .pv:not(…), có [data-show]/[data-any], :root/.pv thuần → component
  - mọi class chủ chỉ xuất hiện ngoài component → khung màn
  - bộ chọn không class (table, td, dl…) → xét mọi class trong bộ chọn; không có class nào thì xem thẻ đó có trong component không
Rule nhóm (a,b{}) mà các bộ chọn lệch nhau → tách thành 2 rule.

Dùng:
  python3 _scripts/ds-css-split.py design/v2/components/_work/{slug}            # in đề xuất (rule chuyển sang cssScreen)
  python3 _scripts/ds-css-split.py design/v2/components/_work/{slug} --write    # ghi page.json (css + cssScreen)
  thêm --inline: style inline có số/màu trong screens → class phụ "il-…" + rule trong css (rồi mới tách)
Chạy lại an toàn: rule đã ở cssScreen giữ nguyên. Soát danh sách in ra — rule xếp nhầm thì sửa tay page.json.
"""
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path


class Walk(HTMLParser):
    def __init__(self, all_cmp=False):
        super().__init__()
        self.stack, self.cmp_cls, self.scr_cls, self.cmp_tag, self.all = [], set(), set(), set(), all_cmp

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cond = (a.get("data-show") or "") + " " + (a.get("data-any") or "")
        inside = self.all or "data-cmp" in a or bool(re.search(r"\b(D\d+|state):", cond)) or any(x for x in self.stack)
        cls = set((a.get("class") or "").split())
        (self.cmp_cls if inside else self.scr_cls).update(cls)
        if inside:
            self.cmp_tag.add(tag)
        if tag not in ("br", "img", "input", "hr", "meta", "link", "path", "circle", "rect", "line", "polyline"):
            self.stack.append(inside)

    def handle_endtag(self, tag):
        if tag not in ("br", "img", "input", "hr", "meta", "link", "path", "circle", "rect", "line", "polyline") and self.stack:
            self.stack.pop()


def rules(css):
    """[(prelude, body)] — @media/@supports giữ nguyên khối, xếp theo bộ chọn bên trong."""
    out, i, n = [], 0, len(css)
    while i < n:
        j = css.find("{", i)
        if j < 0:
            break
        pre = css[i:j].strip()
        depth, k = 1, j + 1
        while k < n and depth:
            depth += {"{": 1, "}": -1}.get(css[k], 0)
            k += 1
        out.append((pre, css[j + 1:k - 1]))
        i = k
    return out


def split_sel(s):
    out, d, cur = [], 0, ""
    for ch in s:
        d += ch in "([" and 1 or ch in ")]" and -1 or 0
        if ch == "," and not d:
            out.append(cur.strip()); cur = ""
        else:
            cur += ch
    out.append(cur.strip())
    return [x for x in out if x]


def subject(sel):
    parts = re.split(r"\s+|>|\+|~", re.sub(r"\[[^\]]*\]|\([^)]*\)", "", sel).strip())
    parts = [p for p in parts if p]
    return parts[-1] if parts else ""


def kind(sel, W):
    s = sel.strip()
    if re.match(r"^(:root|:host|\.pv)(\[[^\]]*\])*$", s) or re.match(r"^\.pv(\[data-(D\d+|state|theme|platform)|:not\()", s) \
            or "[data-show" in s or "[data-any" in s or "[data-cmp" in s:
        return "cmp"
    subj = subject(s)
    cls = set(re.findall(r"\.([\w-]+)", subj)) - {"pv"}
    if cls:
        return "cmp" if cls & W.cmp_cls else ("scr" if cls <= W.scr_cls or not (cls & W.cmp_cls) else "cmp")
    allc = set(re.findall(r"\.([\w-]+)", s)) - {"pv"}
    if allc:
        return "cmp" if allc & W.cmp_cls else "scr"
    tag = re.match(r"^[a-z0-9]+", subj or "")
    return "cmp" if tag and tag.group(0) in W.cmp_tag else "scr"


def inline_to_class(page):
    """--inline: style inline (có số/màu) trên phần tử có class → class phụ + rule trong css, để khai và vẽ lại được."""
    made, n = {}, 0

    def name(style):
        t = re.sub(r"[^a-z0-9]+", "-", style.lower().replace("px", "")).strip("-")
        return "il-" + t[:40]

    def fix(m):
        nonlocal n
        tag, pre, style, post = m.group(1), m.group(2), m.group(3), m.group(4)
        cm = re.search(r'class="([^"]*)"', pre + post)
        if not cm or not re.search(r"\d|#", style):
            return m.group(0)
        first = cm.group(1).split()[0]; nm = name(style)
        made[f".{first}.{nm}"] = style.strip().rstrip(";")
        n += 1
        out = (pre + post).replace(cm.group(0), f'class="{cm.group(1)} {nm}"', 1)
        return f"<{tag}{out}>"
    for sc in page.get("screens") or []:
        sc["html"] = re.sub(r'<([a-z][a-z0-9]*)([^>]*?)\sstyle="([^"]*)"([^>]*)>', fix, sc.get("html") or "")
    if made:
        page["css"] = (page.get("css") or "") + "\n" + "\n".join(f"{k}{{{v}}}" for k, v in made.items())
    return n, len(made)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        sys.exit("thiếu đường dẫn _work/{slug}")
    p = Path(args[0]); pp = p / "page.json" if p.is_dir() else p
    page = json.loads(pp.read_text())
    if "--inline" in sys.argv:
        n, k = inline_to_class(page)
        print(f"--inline: {n} style inline → {k} class phụ trong css")
    W = Walk()
    for sc in page.get("screens") or []:
        W.feed(sc.get("html") or "")
    Wb = Walk(all_cmp=True)
    pv = page.get("preview") or {}
    for b in (pv.get("blocks") or []) + (pv.get("demos") or []):
        for h in [b.get("html")] + list(b.get("frames") or []):
            Wb.feed(h or "")
    W.cmp_cls |= Wb.cmp_cls; W.cmp_tag |= Wb.cmp_tag
    W.scr_cls -= W.cmp_cls
    cmp_css, scr_css, moved = [], [], []
    for pre, body in rules(re.sub(r"/\*.*?\*/", "", page.get("css") or "", flags=re.S)):
        if pre.startswith("@"):
            inner_c, inner_s = [], []
            for p2, b2 in rules(body):
                sels = split_sel(p2)
                c = [x for x in sels if kind(x, W) == "cmp"]; s_ = [x for x in sels if x not in c]
                if c: inner_c.append(f"{','.join(c)}{{{b2}}}")
                if s_: inner_s.append(f"{','.join(s_)}{{{b2}}}"); moved.append(f"{pre} {','.join(s_)}")
            if inner_c: cmp_css.append(f"{pre}{{{''.join(inner_c)}}}")
            if inner_s: scr_css.append(f"{pre}{{{''.join(inner_s)}}}")
            continue
        sels = split_sel(pre)
        c = [x for x in sels if kind(x, W) == "cmp"]; s_ = [x for x in sels if x not in c]
        if c: cmp_css.append(f"{','.join(c)}{{{body}}}")
        if s_: scr_css.append(f"{','.join(s_)}{{{body}}}"); moved.append(",".join(s_))
    print(f"{len(moved)} rule sang cssScreen:")
    for m in moved:
        print("  ", m[:140])
    if "--write" in sys.argv:
        page["css"] = "\n".join(cmp_css)
        page["cssScreen"] = ((page.get("cssScreen") or "") + "\n" + "\n".join(scr_css)).strip()
        pp.write_text(json.dumps(page, ensure_ascii=False, indent=1))
        print(f"Đã ghi {pp}")


if __name__ == "__main__":
    main()
