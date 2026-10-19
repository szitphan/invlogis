#!/usr/bin/env python3
"""DS v2 — sinh phần máy của tài liệu component (DEC-118, DEC-183) từ JSON xuất bằng _scripts/figma-component-export.js.

  python3 _scripts/ds-v2-component-doc.py <export.json> <doc.md>           # ghi phần máy vào doc.md
  python3 _scripts/ds-v2-component-doc.py <export.json> <doc.md> --check   # không ghi; exit 1 nếu doc.md lệch

Ghi vào giữa hai dấu `<!-- auto:begin -->` và `<!-- auto:end -->`: thuộc tính, biến thể, màu theo phần, số đo theo phần,
kiểu chữ. Trục nào không làm đổi giá trị thì tự bỏ khỏi bảng (vd màu nút không đổi theo Content). Phần người viết nằm
ngoài hai dấu, script không đụng tới.
"""
import json
import sys
from datetime import date
from pathlib import Path

BEGIN, END = "<!-- auto:begin -->", "<!-- auto:end -->"
COLOR_COLS = [("bg", "Nền"), ("border", "Viền"), ("text", "Chữ"), ("icon", "Icon"), ("effect", "Vòng focus")]
METRIC_COLS = [("height", "Cao"), ("width", "Rộng"), ("paddingLeft", "Lề trái"), ("paddingRight", "Lề phải"),
               ("paddingTop", "Lề trên"), ("paddingBottom", "Lề dưới"), ("itemSpacing", "Khoảng giữa"),
               ("topLeftRadius", "Bo"), ("maxWidth", "Rộng tối đa"), ("icon", "Cỡ icon")]
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


def render(d):
    L = [BEGIN, f"<!-- Máy sinh từ Figma `{d['name']}` ({d['id']}) ngày {date.today().isoformat()} bằng "
                f"_scripts/ds-v2-component-doc.py. Không sửa tay: sửa trên Figma rồi xuất lại. -->", ""]
    L += ["### Thuộc tính", "", "| Thuộc tính | Loại | Mặc định | Giá trị |", "|---|---|---|---|"]
    kind = {"VARIANT": "Biến thể", "TEXT": "Chữ", "BOOLEAN": "Bật tắt", "INSTANCE_SWAP": "Đổi component", "SLOT": "Slot"}
    for p in d["props"]:
        L.append(f"| {p['name']} | {kind.get(p['type'], p['type'])} | {({True: 'bật', False: 'tắt'}.get(p['default'], p['default']) if isinstance(p['default'], bool) else p['default'])} | {' · '.join(p['options']) if p['options'] else '—'} |")
    L += ["", f"{d['variants']} biến thể · trục {' × '.join(d['axes'])}.", ""]
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
    L += ["", END]
    return "\n".join(L)


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    d = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    doc = Path(sys.argv[2])
    text = doc.read_text(encoding="utf-8")
    if BEGIN not in text or END not in text:
        print(f"{doc}: thiếu dấu {BEGIN} / {END}")
        sys.exit(2)
    a, b = text.index(BEGIN), text.index(END) + len(END)
    block = render(d)
    old = text[a:b]
    strip_date = lambda s: "\n".join(l for l in s.splitlines() if not l.startswith("<!-- Máy sinh"))
    if "--check" in sys.argv:
        same = strip_date(old) == strip_date(block)
        print(f"{doc}: phần máy {'khớp Figma' if same else 'LỆCH — xuất lại và chạy không có --check'}")
        sys.exit(0 if same else 1)
    doc.write_text(text[:a] + block + text[b:], encoding="utf-8")
    print(f"Đã ghi phần máy vào {doc} ({block.count(chr(10)) + 1} dòng)")


if __name__ == "__main__":
    main()
