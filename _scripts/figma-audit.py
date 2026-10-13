#!/usr/bin/env python3
"""Rà nhất quán NHIỀU màn đã vẽ trên Figma (lớp 1 của /figma-audit).

Rule: .claude/rules/ui-review.md (lớp 1 = máy đo, lớp 2 = reviewer) · tên frame:
.claude/rules/naming-conventions.md mục *Màn hình & flow* · quy chuẩn icon: design/design.md
*Iconography & Imagery*.

Đầu vào: JSON của `figma_read get_design_context` `{nodeId, depth: 20, detail: "full"}` — một file
mỗi artboard (`{"tree": …}`), hoặc một file gom nhiều artboard (`[{"tree": …}, …]`, hay kết quả
`figma_write` `{"result": [...]}`). Frame đọc được tên theo quy ước `1.1 · web · slug[ · Trạng thái]`.

Dùng:  python3 _scripts/figma-audit.py <a.json> [...] [--userflow docs/{f}/srs/{f}-userflow.md]
         [--design design/design.md] [--vars vars.json] [--out report.md]
Thoát 1 khi có mục mức Cao.

Mã kiểm:
  K1 giá trị không gắn token (chỉ node tự dựng, không tính bên trong instance thư viện)
  K2 cùng vai trò (cùng tên layer) mà khác giá trị giữa các màn
  K3 nút: cùng nhãn khác biến thể/cỡ giữa các màn; >1 nút Primary trong một nhóm
  K4 icon (kể cả icon bị thay trong instance): cỡ, độ dày nét, màu nét, icon giữ chỗ, icon theo hành động,
     cùng nhãn khác icon, vector tự vẽ
  K5 khối tự dựng trùng tên component (nghi tách rời) — đầu vào cho /figma-component --scan
  K6 mã bản ghi cùng loại khác giá trị trong một flow — cần người soát

Máy KHÔNG kiểm: nhãn/nghiệp vụ đúng hay sai, thẩm mỹ, thứ bậc thị giác (việc của reviewer).
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ICON_SIZES = {12, 14, 16, 18, 20, 24}
STROKE_PER_24 = 1.8          # design.md: nét 1.8 trên khung 24
STROKE_PER_24_CHIP = 2.0     # icon trong chip trạng thái
STROKE_TOL = 0.08
PLACEHOLDER_ICONS = {"icon/circle-dashed"}

RE_FRAME = re.compile(r"^(\d+(?:\.\d+)*) · (web|mob) · ([a-z0-9-]+)(?: · (.+))?$")
RE_VARIANT = re.compile(r"(?:^|, )Variant=([^,]+)")
RE_SIZE = re.compile(r"(?:^|, )Size=([^,]+)", re.I)
RE_BUTTON_NAME = re.compile(r"button|^nút\b", re.I)
RE_CHIP = re.compile(r"chip trạng thái|status chip", re.I)
RE_CODE = re.compile(r"\b([A-Z]{2,5})-(?:[A-Z]{2,4}-)?\d{3,}\b")
GENERIC_NAMES = re.compile(r"^(frame|group|rectangle|vector|text|label|icon|container|content|slot|"
                           r"wrapper|row|col|column|stack|auto layout|line|ellipse)\s*\d*$", re.I)
BUTTON_VARIANTS = ("primary", "secondary", "ghost", "destructive", "tertiary", "danger", "outline", "link")


def load_trees(path):
    d = json.loads(Path(path).read_text())
    if isinstance(d, dict) and "result" in d:
        d = d["result"]
    if isinstance(d, dict) and "tree" in d:
        return [d["tree"]]
    if isinstance(d, list):
        return [x["tree"] if isinstance(x, dict) and "tree" in x else x for x in d]
    return [d]


def own(n):
    """Node tự dựng trên màn (không phải lớp bên trong một instance)."""
    return not str(n.get("id", "")).startswith("I")


def mc_name(n):
    m = n.get("mainComponent") or {}
    return m.get("name", "") if isinstance(m, dict) else str(m)


def bound(n, *keys):
    bv = n.get("boundVariables") or {}
    return any(k in bv for k in keys)


def fill_var(n):
    """Id biến đang gắn cho màu (fills là list alias), không gắn thì mã màu."""
    f = (n.get("boundVariables") or {}).get("fills")
    if isinstance(f, list) and f:
        f = f[0]
    return f.get("id", n.get("fill")) if isinstance(f, dict) else n.get("fill")


def walk(n, anc=()):
    """Duyệt node đang hiện, kèm chuỗi tổ tiên."""
    if n.get("visible") is False:
        return
    yield n, anc
    for c in n.get("children") or []:
        yield from walk(c, anc + (n,))


def first_text(n):
    for x, _ in walk(n):
        if x.get("type") == "TEXT" and (x.get("characters") or "").strip():
            return x["characters"].strip()
    return ""


def button_variant(n):
    """Biến thể nút ('primary'…) nếu node là instance nút, không thì ''."""
    mc = mc_name(n)
    m = RE_VARIANT.search(mc)
    if n.get("type") != "INSTANCE" or not m or not (RE_BUTTON_NAME.search(n.get("name", "")) or "State=" in mc):
        return ""
    v = m.group(1).strip().lower()
    return v if v in BUTTON_VARIANTS else ""


def norm_label(s):
    return re.sub(r"\s+", " ", s).strip().lower()


def parse_action_icons(design_md):
    """Bảng 'Icon theo hành động' trong design.md → {nhãn thường: tên icon}."""
    if not design_md or not Path(design_md).exists():
        return {}
    t = Path(design_md).read_text()
    m = re.search(r"Icon theo hành động[^:]*:(.*?)(?:\n\* |\n\n)", t, re.S)
    if not m:
        return {}
    out = {}
    for label, icon in re.findall(r"([^·`]+?)\s*`([a-z0-9-]+)`", m.group(1)):
        for lb in label.split("/"):
            lb = lb.strip(" .\n")
            if lb:
                out[lb.lower()] = icon
    return out


def parse_userflow(path):
    """[#] → flow đầu tiên ở cột 'Thuộc flow' của Mục 2."""
    if not path or not Path(path).exists():
        return {}
    flows = {}
    sec = re.search(r"## 2\. Danh sách màn hình\n(.*?)\n## ", Path(path).read_text(), re.S)
    if not sec:
        return {}
    for line in sec.group(1).splitlines():
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) >= 3 and re.match(r"^\d+(\.\d+)*$", c[0]):
            flows[c[0]] = c[-1].split(",")[0].strip()
    return flows


class Report:
    def __init__(self):
        self.items = []   # (mức, mã, nội dung, nơi)

    def add(self, level, code, msg, where):
        self.items.append((level, code, msg, where))

    def count(self, level):
        return len({(i[1], i[2]) for i in self.items if i[0] == level})


def audit(frames, action_icons, flow_of, var_names):
    rep = Report()
    vn = lambda i: var_names.get(i, i)  # noqa: E731

    def where(fr, n):
        return f"`{fr}` › {n.get('name', '?')} ({n.get('id')})"

    k1 = defaultdict(list)                     # (prop, value) → nơi
    text_roles = defaultdict(lambda: defaultdict(set))   # tên layer → (cỡ, màu) → frame
    box_roles = defaultdict(lambda: defaultdict(set))    # tên layer → (bo, gap, padding) → frame
    btn_by_label = defaultdict(lambda: defaultdict(set))  # nhãn → (biến thể, cỡ) → frame
    icon_by_label = defaultdict(lambda: defaultdict(set))  # nhãn nút → icon → frame
    icon_use = defaultdict(set)
    inst_names = set()
    own_frames_by_name = defaultdict(set)
    codes = defaultdict(lambda: defaultdict(set))  # flow → tiền tố → {mã}
    stroke_bad = defaultdict(list)                 # (cỡ, nét, cần, trong chip) → [(icon, nơi)]
    code_frames = defaultdict(set)

    for fr_name, root in frames:
        m = RE_FRAME.match(fr_name)
        flow = flow_of.get(m.group(1), m.group(1).split(".")[0]) if m else "?"
        dev = m.group(2) if m else "?"
        for n, anc in walk(root):
            t = n.get("type")
            mc = mc_name(n)
            if t == "INSTANCE":
                inst_names.add(n.get("name", ""))
            # K6 mã bản ghi (kể cả chữ override trong instance)
            if t == "TEXT":
                for cm in RE_CODE.finditer(n.get("characters") or ""):
                    codes[flow][cm.group(1)].add(cm.group(0))
                    code_frames[cm.group(0)].add(fr_name)
            # K1 + K2 trên node tự dựng
            if own(n) and n is not root:
                if t == "TEXT":
                    if n.get("fill") and not bound(n, "fills"):
                        k1[("màu chữ", n["fill"])].append(where(fr_name, n))
                    if n.get("fontSize") and not bound(n, "fontSize"):
                        k1[("cỡ chữ", n["fontSize"])].append(where(fr_name, n))
                    nm = n.get("name", "")
                    if nm and not GENERIC_NAMES.match(nm) and nm != (n.get("characters") or "")[:len(nm)]:
                        text_roles[(dev, nm)][(n.get("fontSize"), vn(fill_var(n)))].add(fr_name)
                elif t in ("FRAME", "RECTANGLE"):
                    if n.get("fill") and not bound(n, "fills"):
                        k1[("màu nền", n["fill"])].append(where(fr_name, n))
                    r = n.get("cornerRadius")
                    if isinstance(r, (int, float)) and r > 0 and not bound(n, "topLeftRadius", "cornerRadius"):
                        k1[("bo góc", r)].append(where(fr_name, n))
                    gap = n.get("itemSpacing")
                    if isinstance(gap, (int, float)) and gap > 0 and not bound(n, "itemSpacing"):
                        k1[("khoảng cách", gap)].append(where(fr_name, n))
                    pad = n.get("padding") or {}
                    if any(v for v in pad.values()) and not bound(n, "paddingLeft", "paddingTop", "paddingRight", "paddingBottom"):
                        k1[("padding", tuple(pad.values()))].append(where(fr_name, n))
                    nm = n.get("name", "")
                    if t == "FRAME":
                        own_frames_by_name[nm].add(where(fr_name, n))
                    if nm and not GENERIC_NAMES.match(nm):
                        box_roles[(dev, nm)][(r, gap, tuple(pad.values()) if pad else None)].add(fr_name)
            # K3 nút
            if t == "INSTANCE" and RE_VARIANT.search(mc) and (RE_BUTTON_NAME.search(n.get("name", "")) or "State=" in mc):
                variant = RE_VARIANT.search(mc).group(1).strip()
                if variant.lower() in BUTTON_VARIANTS:
                    size = (RE_SIZE.search(mc).group(1).strip() if RE_SIZE.search(mc) else "?")
                    label = first_text(n)
                    if label:
                        btn_by_label[norm_label(label)][(variant, size)].add(fr_name)
                    for x, _ in walk(n):
                        if x.get("type") == "INSTANCE" and mc_name(x).startswith("icon/") and label:
                            icon_by_label[norm_label(label)][mc_name(x)].add(fr_name)
                            exp = action_icons.get(norm_label(label))
                            if exp and mc_name(x) != f"icon/{exp}":
                                rep.add("Trung", "K4", f"Nút \"{label}\" dùng `{mc_name(x)}`, design.md quy định `icon/{exp}`", where(fr_name, x))
            # K3: >1 Primary trong cùng nhóm (con trực tiếp của một khung)
            if t in ("FRAME", "INSTANCE") and n.get("children"):
                prim = [c for c in n["children"] if c.get("visible") is not False and button_variant(c) == "primary"]
                if len(prim) > 1:
                    rep.add("Cao", "K3", f"{len(prim)} nút Primary cùng một nhóm: " + ", ".join(f'"{first_text(c)}"' for c in prim), where(fr_name, n))
            # K4 icon
            if t == "INSTANCE" and mc.startswith("icon/"):
                size = round(n.get("w") or 0)
                icon_use[mc].add(fr_name)
                if mc in PLACEHOLDER_ICONS:
                    rep.add("Trung", "K4", f"Icon mặc định của thư viện `{mc}` đang hiện — xác nhận là có chủ ý (vd trạng thái Chưa tạo)", where(fr_name, n))
                if size not in ICON_SIZES:
                    rep.add("Cao", "K4", f"`{mc}` cỡ {size}px — cho phép {sorted(ICON_SIZES)}", where(fr_name, n))
                in_chip = any(RE_CHIP.search(a.get("name", "") + " " + mc_name(a)) for a in anc)
                per24 = STROKE_PER_24_CHIP if in_chip else STROKE_PER_24
                for v, _ in walk(n):
                    if v.get("type") == "VECTOR" and v.get("strokeCount"):
                        want = round(size * per24 / 24, 2)
                        sw = v.get("strokeWeight")
                        if isinstance(sw, (int, float)) and size in ICON_SIZES and abs(sw - want) > STROKE_TOL:
                            stroke_bad[(size, round(sw, 2), want, in_chip)].append((mc, where(fr_name, n)))
                        if not bound(v, "strokes"):
                            rep.add("Trung", "K4", f"`{mc}` màu nét không gắn token", where(fr_name, n))
                        break
            if t == "VECTOR" and own(n) and not any(mc_name(a).startswith("icon/") for a in anc):
                rep.add("Trung", "K4", "Vector tự vẽ, không phải instance `icon/<tên>` (bỏ qua nếu là logo/hình minh hoạ)", where(fr_name, n))

    # K4 nét icon gom theo (cỡ, nét): thường là icon resize mà không đặt lại nét
    for (size, sw, want, chip), hits in sorted(stroke_bad.items()):
        icons = sorted({h[0] for h in hits})
        rep.add("Trung", "K4", f"{len(hits)} icon {size}px để nét {sw}, cần ≈ {want}" + (" (trong chip)" if chip else "")
                + f" — {len(icons)} loại: " + ", ".join(f"`{i}`" for i in icons[:8]) + (" …" if len(icons) > 8 else ""),
                "; ".join(h[1] for h in hits[:3]) + (" …" if len(hits) > 3 else ""))
    # K1 gom theo giá trị
    for (prop, val), places in sorted(k1.items(), key=lambda x: -len(x[1])):
        level = "Cao" if prop.startswith("màu") else "Trung" if prop in ("cỡ chữ", "bo góc") else "Thấp"
        frames_n = len({p.split("`")[1] for p in places})
        rep.add(level, "K1", f"{prop} `{val}` không gắn token — {len(places)} chỗ / {frames_n} màn", "; ".join(places[:4]) + (" …" if len(places) > 4 else ""))
    # K2 vai trò lệch giữa màn
    for (dev, nm), combos in text_roles.items():
        frs = set().union(*combos.values())
        if len(combos) > 1 and len(frs) > 1:
            det = " · ".join(f"cỡ {c[0]} màu {c[1]}: {len(f)} màn" for c, f in combos.items())
            rep.add("Trung", "K2", f"[{dev}] Chữ \"{nm}\" khác nhau giữa các màn — {det}", ", ".join(sorted(frs))[:300])
    for (dev, nm), combos in box_roles.items():
        frs = set().union(*combos.values())
        if len(combos) > 1 and len(frs) > 1:
            det = " · ".join(f"bo {c[0]} gap {c[1]} pad {c[2]}: {len(f)} màn" for c, f in combos.items())
            rep.add("Trung", "K2", f"[{dev}] Khối \"{nm}\" khác nhau giữa các màn — {det}", ", ".join(sorted(frs))[:300])
    # K3 cùng nhãn khác biến thể
    for lb, combos in btn_by_label.items():
        if len(combos) > 1:
            det = " · ".join(f"{v}/{s}: {', '.join(sorted(f))}" for (v, s), f in combos.items())
            rep.add("Trung", "K3", f"Nút \"{lb}\" khác biến thể/cỡ giữa các màn — {det}", "")
    # K4 cùng nhãn khác icon
    for lb, icons in icon_by_label.items():
        if len(icons) > 1:
            rep.add("Trung", "K4", f"Nút \"{lb}\" dùng {len(icons)} icon khác nhau: " + " · ".join(f"`{i}` ({len(f)} màn)" for i, f in icons.items()), "")
    # K5 tự dựng trùng tên component
    for nm in sorted(inst_names & set(own_frames_by_name)):
        if nm and not GENERIC_NAMES.match(nm):
            places = sorted(own_frames_by_name[nm])
            rep.add("Trung", "K5", f"Khung tự dựng tên \"{nm}\" trùng tên component đang dùng — nghi tách rời hoặc dựng lại", "; ".join(places[:3]))
    # K6 mã bản ghi
    for flow, prefixes in codes.items():
        for pf, cs in prefixes.items():
            lone = sorted(c for c in cs if len(code_frames[c]) == 1)
            if len(cs) > 1 and lone:
                for c in lone:
                    rep.add("Thấp", "K6", f"Flow {flow}: `{c}` chỉ có ở 1 màn, các màn khác dùng " + ", ".join(f"`{x}`" for x in sorted(cs - {c})[:4]) + " — soát dữ liệu mẫu có cùng một bản ghi không", ", ".join(sorted(code_frames[c])))
    return rep, icon_use


def render(rep, icon_use, frames, skipped):
    lines = ["# Figma audit — lớp 1 (máy đo)", "",
             f"Màn đã đọc: {len(frames)} · bỏ qua (tên không theo quy ước): {len(skipped)}", "",
             f"**Cao {rep.count('Cao')} · Trung {rep.count('Trung')} · Thấp {rep.count('Thấp')}**", ""]
    for level in ("Cao", "Trung", "Thấp"):
        rows = [i for i in rep.items if i[0] == level]
        if not rows:
            continue
        lines += [f"## Mức {level}", "", "| Mã | Sai lệch | Ở đâu |", "|---|---|---|"]
        seen = set()
        for _, code, msg, wh in sorted(rows, key=lambda r: r[1]):
            key = (code, msg)
            if key in seen:
                continue
            seen.add(key)
            lines.append(f"| {code} | {msg.replace('|', '/')} | {wh.replace('|', '/')} |")
        lines.append("")
    lines += ["## Icon đang dùng", "", "| Icon | Số màn |", "|---|---|"]
    lines += [f"| `{i}` | {len(f)} |" for i, f in sorted(icon_use.items(), key=lambda x: -len(x[1]))]
    if skipped:
        lines += ["", "Bỏ qua: " + ", ".join(f"`{s}`" for s in skipped)]
    lines += ["", "Máy KHÔNG kiểm: nghiệp vụ/nhãn đúng sai, thẩm mỹ, thứ bậc thị giác — xem lớp 2 (reviewer)."]
    return "\n".join(lines)


def main(argv):
    files, opts, i = [], {}, 0
    while i < len(argv):
        if argv[i].startswith("--"):
            opts[argv[i][2:]] = argv[i + 1]
            i += 2
        else:
            files.append(argv[i])
            i += 1
    if not files:
        print(__doc__)
        return 2
    frames, skipped = [], []
    for f in files:
        for t in load_trees(f):
            nm = t.get("name", "")
            (frames if RE_FRAME.match(nm) else skipped).append((nm, t) if RE_FRAME.match(nm) else nm)
    var_names = json.loads(Path(opts["vars"]).read_text()) if opts.get("vars") else {}
    rep, icon_use = audit(frames, parse_action_icons(opts.get("design", "design/design.md")),
                          parse_userflow(opts.get("userflow")), var_names)
    out = render(rep, icon_use, frames, skipped)
    if opts.get("out"):
        Path(opts["out"]).write_text(out + "\n")
        print(f"Đã ghi {opts['out']}")
    print(out if not opts.get("out") else f"Cao {rep.count('Cao')} · Trung {rep.count('Trung')} · Thấp {rep.count('Thấp')}")
    return 1 if rep.count("Cao") else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
