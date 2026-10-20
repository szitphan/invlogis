#!/usr/bin/env python3
"""DS v2 — sinh phần máy của tài liệu component (DEC-118, DEC-183) từ JSON xuất bằng _scripts/figma-component-export.js.

  python3 _scripts/ds-v2-component-doc.py <export.json> <doc.md>                  # ghi khối máy không tên
  python3 _scripts/ds-v2-component-doc.py <export.json> <doc.md> --block mobile   # ghi khối máy tên `mobile`
  python3 _scripts/ds-v2-component-doc.py <export.json> <doc.md> [--block …] --check
                                                                                  # không ghi; exit 1 nếu khối lệch

Ghi vào giữa hai dấu của khối: `<!-- auto:begin -->` … `<!-- auto:end -->` (không tên, cú pháp cũ, vẫn chạy như trước)
hoặc `<!-- auto:begin NAME -->` … `<!-- auto:end NAME -->` (khối có tên, chọn bằng `--block NAME`). Một md chứa được nhiều
khối có tên, vd Text Field có `web` (Base / Text Field) và `mobile` (Base / Text Field / Mobile): xuất từng component rồi
ghi vào khối tương ứng. Nội dung khối: thuộc tính, biến thể, màu theo phần, số đo theo phần, kiểu chữ. Trục nào không làm
đổi giá trị thì tự bỏ khỏi bảng (vd màu nút không đổi theo Content). Phần người viết nằm ngoài các dấu, script không đụng tới.
"""
import json
import re
import sys
from datetime import date
from pathlib import Path

NAME_RE = re.compile(r"^[A-Za-z0-9_-]+$")
MARK_RE = re.compile(r"(?m)^<!-- auto:begin(?: ([A-Za-z0-9_-]+))? -->[ \t]*$")


def markers(name=None):
    """Cặp dấu của khối: không tên → `<!-- auto:begin -->` (cú pháp cũ); có tên → `<!-- auto:begin NAME -->`."""
    tag = f" {name}" if name else ""
    return f"<!-- auto:begin{tag} -->", f"<!-- auto:end{tag} -->"


COLOR_COLS = [("bg", "Nền"), ("border", "Viền"), ("text", "Chữ"), ("icon", "Icon"), ("effect", "Vòng focus"), ("shadow", "Bóng")]
METRIC_COLS = [("height", "Cao"), ("width", "Rộng"), ("paddingLeft", "Lề trái"), ("paddingRight", "Lề phải"),
               ("paddingTop", "Lề trên"), ("paddingBottom", "Lề dưới"), ("itemSpacing", "Khoảng giữa"),
               ("topLeftRadius", "Bo"), ("maxWidth", "Rộng tối đa"), ("strokeWeight", "Viền"), ("icon", "Cỡ icon")]
# Trường mà None nghĩa là "không có phần đó" (gộp được với giá trị khác), không phải "trong suốt".
PRESENCE = {"text", "icon"}


def compatible(a, b):
    for k in set(a) | set(b):
        x, y = a.get(k), b.get(k)
        if x == y:
            continue
        if k in PRESENCE and (x is None or y is None):
            continue
        return False
    return True


def merge(a, b):
    return {k: (a.get(k) if a.get(k) is not None else b.get(k)) for k in set(a) | set(b)}


def reduce_axes(table, keys):
    """Bỏ dần trục không làm đổi giá trị; trả (trục giữ lại, {bộ giá trị: dữ liệu đã gộp})."""
    rows = [(k.split(" · "), v) for k, v in table.items()]
    keep = list(range(len(keys)))
    changed = True
    while changed:
        changed = False
        for i in list(keep):
            trial = [j for j in keep if j != i]
            groups, ok = {}, True
            for parts, v in rows:
                kk = tuple(parts[j] for j in trial)
                if kk in groups:
                    if not compatible(groups[kk], v):
                        ok = False
                        break
                    groups[kk] = merge(groups[kk], v)
                else:
                    groups[kk] = dict(v)
            if ok:
                keep, changed = trial, True
                break
    out = {}
    for parts, v in rows:
        kk = tuple(parts[j] for j in keep)
        out[kk] = merge(out[kk], v) if kk in out else dict(v)
    return [keys[j] for j in keep], out


def cell(v, transparent=False):
    if v is None:
        return "trong suốt" if transparent else "—"
    if v == "IMAGE":
        return "ảnh (phủ kín)"
    return f"`{v}`" if isinstance(v, str) and "/" in v else str(v)


def order_of(keys, props):
    opts = {p["name"]: p["options"] or [] for p in props}
    return lambda kk: tuple(opts.get(a, []).index(x) if x in opts.get(a, []) else 99 for a, x in zip(keys, kk))


def prop_default(p):
    """Mặc định của thuộc tính. Slot không có defaultValue (xuất ra không có khóa `default`) → "—"."""
    v = p.get("default")
    if v is None or v == "":
        return "—"
    if isinstance(v, bool):
        return "bật" if v else "tắt"
    return v


def prop_values(p):
    """Cột Giá trị: tuỳ chọn của biến thể; Slot, Đổi component thì liệt kê component được nhận (preferred values)."""
    if p.get("options"):
        return " · ".join(p["options"])
    if p.get("preferred"):
        return "nhận: " + " · ".join(p["preferred"])
    return "—"


def axes_line(d):
    """Dòng tóm tắt biến thể. Component đơn (không có trục) không in "trục ."."""
    n = d["variants"]
    if d["axes"]:
        return f"{n} biến thể · trục {' × '.join(d['axes'])}."
    return "Component đơn, không có trục biến thể." if n <= 1 else f"{n} biến thể · không có trục biến thể."


def render(d, name=None):
    begin, end = markers(name)
    tag = f" · khối `{name}`" if name else ""
    L = [begin, f"<!-- Máy sinh từ Figma `{d['name']}` ({d['id']}){tag} ngày {date.today().isoformat()} bằng "
                f"_scripts/ds-v2-component-doc.py. Không sửa tay: sửa trên Figma rồi xuất lại. -->", ""]
    L += ["### Thuộc tính", "", "| Thuộc tính | Loại | Mặc định | Giá trị |", "|---|---|---|---|"]
    kind = {"VARIANT": "Biến thể", "TEXT": "Chữ", "BOOLEAN": "Bật tắt", "INSTANCE_SWAP": "Đổi component", "SLOT": "Slot"}
    for p in d["props"]:
        L.append(f"| {p['name']} | {kind.get(p['type'], p['type'])} | {prop_default(p)} | {prop_values(p)} |")
    L += ["", axes_line(d), ""]
    ck, colors = reduce_axes(d["colors"], d["colorKeys"])
    cols = [c for c in COLOR_COLS if any(v.get(c[0]) is not None for v in colors.values())]
    L += ["### Màu theo phần (token)", "", "| " + " | ".join(ck + [c[1] for c in cols]) + " |", "|" + "---|" * (len(ck) + len(cols))]
    for kk in sorted(colors, key=order_of(ck, d["props"])):
        v = colors[kk]
        L.append("| " + " | ".join(list(kk) + [cell(v.get(c), transparent=(c == "bg")) for c, _ in cols]) + " |")
    mk, metrics = reduce_axes(d["metrics"], d["metricKeys"])
    mcols = [c for c in METRIC_COLS if len({json.dumps(v.get(c[0])) for v in metrics.values()}) > 1
             or any(v.get(c[0]) not in (None, 0) for v in metrics.values())]
    L += ["", "### Số đo theo phần (token)", "", "| " + " | ".join(mk + [c[1] for c in mcols]) + " |", "|" + "---|" * (len(mk) + len(mcols))]
    for kk in sorted(metrics, key=order_of(mk, d["props"])):
        v = metrics[kk]
        L.append("| " + " | ".join(list(kk) + [cell(v.get(c)) for c, _ in mcols]) + " |")
    L += ["", "### Kiểu chữ", "", "| Lớp chữ | Text style |", "|---|---|"]
    for k, v in d["text"].items():
        L.append(f"| {k} | `{v}` |")
    L += ["", end]
    return "\n".join(L)


def line_marks(text, marker):
    """Vị trí các dòng chỉ gồm đúng `marker` (dấu nhắc trong câu chữ, trong `code` không tính)."""
    return [m for m in re.finditer(rf"(?m)^{re.escape(marker)}[ \t]*$", text)]


def find_block(text, name=None):
    """Vị trí [a, b) của khối `name` trong text; None nếu thiếu; ValueError nếu dấu trùng hoặc ngược thứ tự."""
    begin, end = markers(name)
    bs, es = line_marks(text, begin), line_marks(text, end)
    if not bs and not es:
        return None
    if len(bs) != 1 or len(es) != 1:
        raise ValueError(f"dấu {begin} / {end} phải có đúng một cặp, mỗi dấu một dòng riêng (gặp {len(bs)} / {len(es)})")
    a, b = bs[0].start(), es[0].end()
    if es[0].start() < a:
        raise ValueError(f"dấu {end} nằm trước {begin}")
    return a, b


def main():
    argv = sys.argv[1:]
    check = "--check" in argv
    block_name = None
    if "--block" in argv:
        i = argv.index("--block")
        if i + 1 >= len(argv) or not NAME_RE.match(argv[i + 1]):
            print("--block cần tên gồm chữ, số, '-' hoặc '_' (vd --block mobile)")
            sys.exit(2)
        block_name = argv[i + 1]
        del argv[i:i + 2]
    argv = [a for a in argv if a != "--check"]
    if len(argv) != 2:
        print(__doc__)
        sys.exit(2)
    d = json.loads(Path(argv[0]).read_text(encoding="utf-8"))
    doc = Path(argv[1])
    text = doc.read_text(encoding="utf-8")
    try:
        pos = find_block(text, block_name)
    except ValueError as e:
        print(f"{doc}: {e}")
        sys.exit(2)
    if pos is None:
        begin, end = markers(block_name)
        have = [m.group(1) or "(không tên)" for m in MARK_RE.finditer(text)]
        print(f"{doc}: thiếu dấu {begin} / {end}" + (f"; file có khối: {', '.join(have)} — chọn bằng --block" if have else ""))
        sys.exit(2)
    a, b = pos
    block = render(d, block_name)
    old = text[a:b]
    strip_date = lambda s: "\n".join(l for l in s.splitlines() if not l.startswith("<!-- Máy sinh"))
    label = f"phần máy{f' `{block_name}`' if block_name else ''}"
    if check:
        same = strip_date(old) == strip_date(block)
        print(f"{doc}: {label} {'khớp Figma' if same else 'LỆCH — xuất lại và chạy không có --check'}")
        sys.exit(0 if same else 1)
    doc.write_text(text[:a] + block + text[b:], encoding="utf-8")
    print(f"Đã ghi {label} vào {doc} ({block.count(chr(10)) + 1} dòng)")


if __name__ == "__main__":
    main()
