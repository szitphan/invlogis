#!/usr/bin/env python3
"""A5 — audit luật thị giác đo được trên cây node Figma (Fitts, Hick, Miller, proximity, spacing,
readability, 60/30/10).

Rule: .claude/rules/ui-review.md Mục 2 (bảng luật → ngưỡng). Ngưỡng là hằng số dưới đây — sửa thì sửa
cả bảng trong rule. Luật cần mắt người (phân cấp màu, Jakob…) KHÔNG nằm ở đây — việc của reviewer.

Đầu vào: JSON của `figma_read get_design_context` (params `{nodeId, depth: 20, detail: "full"}`) cho
**một artboard**, lưu ra file. Toạ độ con tương đối với cha; gốc = artboard.

Dùng:  python3 _scripts/visual-audit.py <screen.json> [--part <vùng.json> ...] [<screen2.json> ...] [--platform web|mobile]
       (mặc định tự nhận: tên có "-mob" hoặc rộng ≤ 480 → mobile)
Thoát 1 khi có FAIL.

Giới hạn (in ở cuối báo cáo, không giấu):
  - Cây node không có fontWeight → không đo phân cấp đậm/nhạt.
  - `mainComponent` chỉ có ở ~200 instance đầu; còn lại nhận diện qua componentProperties + tên layer.
    Tỷ lệ nhận diện < MIN_RECOGNIZED → in cảnh báo, kết quả F/H/M có thể thiếu.
"""
import colorsys
import json
import re
import sys
from pathlib import Path

# --- Ngưỡng (đồng bộ .claude/rules/ui-review.md Mục 2) ---
F1_DANGER_GAP = 8          # px giữa nút nguy hiểm và nút chính
F2_THUMB_ZONE = 0.40       # mobile: nút chính phải nằm trong 40% dưới màn
H1_MAX_ACTIONS = 5         # nút ngang hàng trong 1 nhóm
H2_MAX_OPTIONS = 7         # tab / segmented / mục menu
M1_MAX_FIELDS = 7          # field trong 1 khối không có tiêu đề nhóm
M2_MAX_COLUMNS = 9         # cột bảng hiện (web)
R1_MAX_SIZES = {"web": 5, "mobile": 4}
R2_MIN_FONT = 12
R3_MAX_CPL = 90            # ký tự / dòng
C1_MAX_ACCENT = 0.15
C1_MIN_NEUTRAL = 0.60
C2_MAX_HUES = 3
NEUTRAL_SAT = 0.15         # độ bão hoà dưới mức này = trung tính
MIN_RECOGNIZED = 0.80
MOBILE_GRID = 8

# Khớp trên TÊN (layer + set + component) — không khớp khoá thuộc tính (vd `statusMessage` của field)
RE_BUTTON = re.compile(r"button|^nút\b", re.I)
RE_FIELD = re.compile(r"field|input|textbox|textarea|selector|dropdown|date ?time|combobox|ô nhập|ô tìm|search ?box", re.I)
RE_OPTION = re.compile(r"\btab\b|tabs? ?item|segment|menu ?item|mục menu", re.I)
RE_HEADER = re.compile(r"table ?header|header ?cell|^cột ·", re.I)
RE_STATUS = re.compile(r"chip trạng thái|badge|status ?(chip|dot)|^chip\b", re.I)
RE_ICON = re.compile(r"^icon|xdsicon|icon=", re.I)
RE_SKIP = re.compile(r"pagination|phân trang|khung trang|menu trái|thanh trên|device", re.I)
# Vỏ thiết bị giả lập — không phải nội dung màn, bỏ khỏi mọi phép đo
RE_CHROME = re.compile(r"^(status bar|home indicator|dynamic island)$", re.I)
# Khớp trên KHOÁ thuộc tính khi mainComponent bị cắt
KEYS_HEADER = {"sortable", "resizable", "has filter"}
KEYS_FIELD = {"placeholder", "showlabel", "descriptiontext", "statusmessage"}
VARIANT_KEYS = ("variant", "kiểu", "loại", "type")
BUTTON_VARIANTS = ("primary", "secondary", "ghost", "destructive", "tertiary", "danger")


def names_of(n):
    mc = n.get("mainComponent") or {}
    return " | ".join(p for p in (n.get("name", ""), mc.get("setName", ""), mc.get("name", "")) if p)


def prop_keys(n):
    return {k.split("#")[0].strip().lower() for k in (n.get("componentProperties") or {})}


def is_identified(n):
    return bool(n.get("mainComponent") or n.get("componentProperties"))


def variant_of(n):
    mc = n.get("mainComponent") or {}
    for src in [mc.get("name", "")] + [f"{k.split('#')[0]}={v}" for k, v in (n.get("componentProperties") or {}).items()]:
        for seg in str(src).split(","):
            if "=" in seg:
                k, v = seg.split("=", 1)
                if k.strip().lower() in VARIANT_KEYS:
                    return v.strip().lower()
    return ""


def role_of(n):
    if n.get("type") != "INSTANCE":
        return None
    names, keys = names_of(n), prop_keys(n)
    if RE_SKIP.search(names):
        return "frame"
    if RE_ICON.search(names) and not RE_BUTTON.search(names):
        return "icon"
    if RE_STATUS.search(names):
        return "status"
    if RE_HEADER.search(names) or keys & KEYS_HEADER:
        return "header"
    if RE_BUTTON.search(names) or variant_of(n) in BUTTON_VARIANTS:
        return "button"
    if RE_OPTION.search(names):
        return "option"
    if RE_FIELD.search(names) or keys & KEYS_FIELD:
        return "field"
    return None


def button_kind(n):
    v = variant_of(n)
    if v in ("destructive", "danger") or re.search(r"destructive|danger|xoá|xóa", names_of(n), re.I):
        return "danger"
    return v or "other"


# --- Duyệt cây: thêm toạ độ tuyệt đối, cha, đường dẫn ---
class Node:
    __slots__ = ("raw", "parent", "ax", "ay", "w", "h", "path", "in_instance", "children", "role")

    def __init__(self, raw, parent, ax, ay, in_instance):
        self.raw, self.parent, self.ax, self.ay = raw, parent, ax, ay
        self.w, self.h = raw.get("w", 0), raw.get("h", 0)
        self.path = (parent.path + [raw.get("name", "?")]) if parent else [raw.get("name", "?")]
        self.in_instance = in_instance
        self.children = []
        self.role = role_of(raw)

    def __getattr__(self, k):  # tiện đọc trường raw
        raise AttributeError(k)

    def get(self, k, d=None):
        return self.raw.get(k, d)

    def label(self):
        return " › ".join(self.path[-3:])


def build(raw, parent=None, ox=0.0, oy=0.0, in_instance=False):
    if raw.get("visible") is False or RE_CHROME.match(raw.get("name", "")):
        return None
    ax = ox + (raw.get("x", 0) if parent else 0)
    ay = oy + (raw.get("y", 0) if parent else 0)
    node = Node(raw, parent, ax, ay, in_instance)
    # Nội dung trong SLOT (vd Content của Device / Frame, Khung trang) là khung tự dựng, không phải ruột thư viện
    child_in = False if raw.get("type") == "SLOT" else (in_instance or raw.get("type") == "INSTANCE")
    for c in raw.get("children", []) or []:
        cn = build(c, node, ax, ay, child_in)
        if cn:
            node.children.append(cn)
    return node


def walk(n):
    yield n
    for c in n.children:
        yield from walk(c)


def walk_raw(r):
    yield r
    for c in r.get("children", []) or []:
        yield from walk_raw(c)


def gap(a, b):
    dx = max(0, max(a.ax, b.ax) - min(a.ax + a.w, b.ax + b.w))
    dy = max(0, max(a.ay, b.ay) - min(a.ay + a.h, b.ay + b.h))
    return max(dx, dy) if (dx == 0 or dy == 0) else (dx * dx + dy * dy) ** 0.5


def hex_hsv(h):
    h = h.lstrip("#")[:6]
    if len(h) != 6:
        return None
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    return colorsys.rgb_to_hsv(r, g, b)


# --- Các check ---
def audit(root, platform):
    out = []  # (level, code, label, msg)
    nodes = list(walk(root))
    insts = [n for n in nodes if n.get("type") == "INSTANCE"]
    top_insts = [n for n in insts if not n.in_instance]
    ident = sum(1 for n in top_insts if is_identified(n) or n.role)
    rate = ident / len(top_insts) if top_insts else 1.0

    # Fitts
    for p in nodes:
        btns = [c for c in p.children if c.role == "button"]
        prim = [b for b in btns if button_kind(b) == "primary"]
        for d in (b for b in btns if button_kind(b) == "danger"):
            for pr in prim:
                g = gap(d, pr)
                if g < F1_DANGER_GAP:
                    out.append(("WARN", "F1", d.label(), f"nút nguy hiểm cách nút chính {g:.0f}px < {F1_DANGER_GAP}"))
        others = [b for b in btns if button_kind(b) in ("secondary", "ghost", "tertiary", "other")]
        for pr in prim:
            if others and pr.h < max(o.h for o in others):
                out.append(("WARN", "F3", pr.label(), f"nút chính cao {pr.h:.0f}px < nút phụ cùng nhóm {max(o.h for o in others):.0f}px"))
    if platform == "mobile":
        for b in nodes:
            if b.role == "button" and button_kind(b) == "primary":
                cy = b.ay + b.h / 2
                if cy < root.h * (1 - F2_THUMB_ZONE):
                    out.append(("WARN", "F2", b.label(), f"nút chính ở {cy / root.h:.0%} chiều cao — ngoài vùng ngón cái (40% dưới)"))

    # Hick
    for p in nodes:
        nb = sum(1 for c in p.children if c.role == "button")
        if nb > H1_MAX_ACTIONS:
            out.append(("WARN", "H1", p.label(), f"{nb} nút ngang hàng > {H1_MAX_ACTIONS}"))
        no = sum(1 for c in p.children if c.role == "option")
        if no > H2_MAX_OPTIONS:
            out.append(("WARN", "H2", p.label(), f"{no} lựa chọn (tab/segment/menu) > {H2_MAX_OPTIONS}"))

    # Miller
    def field_block(f):
        a = f.parent
        while a and not (a.get("layoutMode") == "VERTICAL" and not a.in_instance):
            a = a.parent
        return a
    blocks = {}
    for f in nodes:
        if f.role == "field" and not f.in_instance:
            b = field_block(f)
            if b:
                blocks.setdefault(id(b), (b, []))[1].append(f)
    for b, fs in blocks.values():
        if len(fs) > M1_MAX_FIELDS:
            has_heading = any(c.get("type") == "TEXT" and (c.get("fontSize") or 0) >= 16 for c in b.children)
            if not has_heading:
                out.append(("WARN", "M1", b.label(), f"{len(fs)} field trong 1 khối, không có tiêu đề nhóm (> {M1_MAX_FIELDS})"))
    if platform == "web":
        for p in nodes:
            nh = sum(1 for c in p.children if c.role == "header")
            if nh > M2_MAX_COLUMNS:
                out.append(("WARN", "M2", p.label(), f"bảng {nh} cột hiện > {M2_MAX_COLUMNS}"))

    # Proximity — chỉ khung tự dựng (ngoài instance), cùng hướng auto-layout
    for p in nodes:
        if p.in_instance or p.get("type") == "INSTANCE" or not p.get("layoutMode") or len(p.children) < 2:
            continue
        sp = p.get("itemSpacing") or 0
        if sp <= 0:
            continue
        for c in p.children:
            if c.get("type") != "FRAME" or c.get("layoutMode") != p.get("layoutMode") or len(c.children) < 2:
                continue
            sc = c.get("itemSpacing") or 0
            if sc >= sp:
                out.append(("WARN", "P1", c.label(), f"khoảng cách trong nhóm {sc:.0f} ≥ giữa nhóm {sp:.0f} — gom nhóm mập mờ"))

    # Spacing — mobile lưới 8pt cho lề (padding) và khoảng cách giữa các khối xếp dọc (design.md › Mẫu
    # bố cục M chỉ áp margin/gutter); khoảng cách trong một hàng (nhãn–giá trị, icon–chữ) không xét. Gộp 1 dòng
    if platform == "mobile":
        bad = []
        for p in nodes:
            if p.in_instance or p.get("type") == "INSTANCE" or not p.get("layoutMode"):
                continue
            vals = list((p.get("padding") or {}).values())
            if p.get("layoutMode") == "VERTICAL" and len(p.children) >= 2:
                vals.append(p.get("itemSpacing") or 0)
            odd = sorted({v for v in vals if v and v % MOBILE_GRID})
            if odd:
                bad.append(f"{p.get('name')} ({', '.join(f'{v:g}' for v in odd)})")
        if bad:
            out.append(("WARN", "S1", root.label(), f"{len(bad)} khung lệch lưới {MOBILE_GRID}pt: " + "; ".join(bad[:5]) + (" …" if len(bad) > 5 else "")))

    # Readability
    texts = [n for n in nodes if n.get("type") == "TEXT" and n.get("fontSize")]
    sizes = sorted({t.get("fontSize") for t in texts})
    if len(sizes) > R1_MAX_SIZES[platform]:
        out.append(("WARN", "R1", root.label(), f"{len(sizes)} cỡ chữ ({', '.join(f'{s:g}' for s in sizes)}) > {R1_MAX_SIZES[platform]}"))
    small = [t for t in texts if t.get("fontSize") < R2_MIN_FONT]
    if small:
        lvl = "FAIL" if platform == "mobile" else "WARN"
        ex = "; ".join(f"{t.label()} {t.get('fontSize'):g}px" for t in small[:3])
        out.append((lvl, "R2", root.label(), f"{len(small)} chữ < {R2_MIN_FONT}px: {ex}" + (" …" if len(small) > 3 else "")))
    for t in texts:
        fs = t.get("fontSize")
        chars = len(t.get("characters") or "")
        if t.h > fs * 1.9 and chars:
            cpl = min(chars, t.w / (fs * 0.5))
            if cpl > R3_MAX_CPL:
                out.append(("WARN", "R3", t.label(), f"~{cpl:.0f} ký tự/dòng > {R3_MAX_CPL}"))

    # 60/30/10 — diện tích sơn riêng (trừ phần con phủ), bỏ chữ/icon/vector
    def in_status(n):
        a = n
        while a:
            if a.role == "status":
                return True
            a = a.parent
        return False

    def coverage(n):
        if n.get("type") in ("TEXT", "VECTOR"):
            return 0
        if n.get("fill"):
            return n.w * n.h
        return min(n.w * n.h, sum(coverage(c) for c in n.children))

    area = {}
    hues = set()
    for n in nodes:
        f = n.get("fill")
        if not f or n.get("type") in ("TEXT", "VECTOR") or n.role == "icon":
            continue
        own = max(0.0, n.w * n.h - sum(coverage(c) for c in n.children))
        if own <= 0:
            continue
        area[f] = area.get(f, 0) + own
        hsv = hex_hsv(f)
        if hsv and hsv[1] >= NEUTRAL_SAT and hsv[2] > 0.2 and not in_status(n):
            hues.add(int(hsv[0] * 360) // 30)
    total = sum(area.values()) or 1
    neutral = sum(a for c, a in area.items() if (hex_hsv(c) or (0, 0, 0))[1] < NEUTRAL_SAT or (hex_hsv(c) or (0, 0, 0))[2] <= 0.2)
    accent = total - neutral
    ranked = sorted(area.items(), key=lambda kv: -kv[1])
    dom = ranked[0][1] / total if ranked else 0
    info = (f"trội {ranked[0][0] if ranked else '-'} {dom:.0%} · trung tính {neutral / total:.0%} · nhấn {accent / total:.0%}")
    if accent / total > C1_MAX_ACCENT:
        out.append(("WARN", "C1", root.label(), f"màu nhấn {accent / total:.0%} > {C1_MAX_ACCENT:.0%} ({info})"))
    elif neutral / total < C1_MIN_NEUTRAL:
        out.append(("WARN", "C1", root.label(), f"trung tính {neutral / total:.0%} < {C1_MIN_NEUTRAL:.0%} ({info})"))
    else:
        out.append(("INFO", "C1", root.label(), info))
    if len(hues) > C2_MAX_HUES:
        out.append(("WARN", "C2", root.label(), f"{len(hues)} sắc độ đậm khác nhau > {C2_MAX_HUES} (không tính chip/badge trạng thái)"))

    return out, rate, len(top_insts)


def load(path):
    d = json.loads(Path(path).read_text(encoding="utf-8"))
    return d.get("tree") or d.get("node") or d, d.get("mainComponentTruncated") or 0


def graft(tree, part):
    """Thay node cùng id trong cây chính bằng vùng con đọc riêng (đủ mainComponent). Trả True nếu ghép được."""
    if not isinstance(tree, dict):
        return False
    for i, c in enumerate(tree.get("children", []) or []):
        if c.get("id") == part.get("id"):
            tree["children"][i] = part
            return True
        if graft(c, part):
            return True
    return False


def main(argv):
    platform = None
    screens = []  # [(file, [part files])]
    it = iter(argv)
    for a in it:
        if a == "--platform":
            platform = next(it, None)
        elif a == "--part":
            p = next(it, None)
            if not screens or not p:
                print("--part phải đứng sau file màn chính")
                return 2
            screens[-1][1].append(p)
        else:
            screens.append((a, []))
    if not screens:
        print(__doc__)
        return 2
    fails = 0
    for f, parts in screens:
        raw, truncated = load(f)
        for p in parts:
            praw, _ = load(p)
            if not graft(raw, praw):
                print(f"⚠ --part {p}: không tìm thấy node {praw.get('id')} trong {f}")
        if truncated:  # đếm lại trên cây đã ghép, chỉ instance tự đặt (ngoài ruột instance khác)
            truncated = sum(1 for r in walk_raw(raw) if r.get("type") == "INSTANCE" and not r.get("mainComponent")
                            and not str(r.get("id", "")).startswith("I"))
        root = build(raw)
        plat = platform or ("mobile" if re.search(r"-mob\b", raw.get("name", "")) or raw.get("w", 9999) <= 480 else "web")
        res, rate, ninst = audit(root, plat)
        print(f"== {raw.get('name', f)} ({plat}, {raw.get('w', 0):g}×{raw.get('h', 0):g})")
        for lvl, code, lab, msg in sorted(res, key=lambda r: ("FAIL", "WARN", "INFO").index(r[0])):
            print(f"{lvl} {code} {lab} — {msg}")
        nf = sum(1 for r in res if r[0] == "FAIL")
        nw = sum(1 for r in res if r[0] == "WARN")
        fails += nf
        print(f"Tổng: {nf} FAIL / {nw} WARN · nhận diện {rate:.0%} ({ninst} instance)")
        if truncated:
            print(f"ℹ {truncated} instance thiếu mainComponent (cây lớn bị cắt) — đã nhận diện qua componentProperties/tên layer.")
        if rate < MIN_RECOGNIZED:
            print(f"⚠ Nhận diện < {MIN_RECOGNIZED:.0%}: F/H/M có thể thiếu — đọc lại vùng con bằng get_design_context "
                  f"rồi chạy lại với --part <vùng.json>.")
        print("Không đo: độ đậm chữ (cây node không có fontWeight), phân cấp màu, Jakob → @visual-reviewer / @usability-reviewer.")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
