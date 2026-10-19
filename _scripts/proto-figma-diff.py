#!/usr/bin/env python3
"""So prototype HTML đã duyệt với màn Figma bằng số đo (/figma-proto-check).

Rule: .claude/skills/figma-proto-check/SKILL.md. Hai bên đo cùng một khuôn:
  - prototype: _scripts/proto-probe.js (Chrome headless, style thật sau khi trình duyệt tính)
  - Figma:     .claude/skills/figma-proto-check/references/figma-probe.js (use_figma, Plugin API thật)

Lệnh:
  probe <prototype.html> --screen <slug> [--state <State>] [--device web|app] --out <dir>
        → <dir>/proto-<slug>[--<state>].json + .png (2x, đã cắt theo khung màn)
  diff  --proto P.json --figma F.json [--frame <nodeId>] --screen "1.3 · web" [--state <State>]
        [--ledger docs/{f}/html-design/{f}-proto-check.md] [--proto-png P.png --figma-png F.png --crop-out <dir>]
        [--proto-within "<chữ>"] [--figma-within "<chữ>"] --out <diff.json>
        → danh sách chỗ Mới / Lệch, mỗi chỗ có Khoá ổn định để ghi sổ quyết định
  report <diff.json> [...] [--out report.md]
        → bảng markdown theo từng màn, theo thứ tự đưa vào (= thứ tự flow)

Giới hạn (in ở cuối báo cáo, không giấu):
  - Ghép phần tử theo chữ hiển thị; khối không có chữ ghép checkbox, đường kẻ, icon (theo tên rồi vị trí), ảnh/logo (theo thứ tự).
  - State prototype chỉ đúng khi prototype có PROTO_STATES (quy ước /prototype-html); thiếu → cảnh báo.
  - Màu so theo hex (sai số nhỏ); bóng đổ so lớp đầu; không so nội dung ảnh, gradient.
  - Ảnh Figma từ get_screenshot có thể là 1x: crop tự tính tỷ lệ theo bề rộng ảnh / khung.
Thoát 0 kể cả khi có lệch (đây là báo cáo để người duyệt, không phải gate).
"""
import argparse
import difflib
import hashlib
import html
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROBE_JS = ROOT / "_scripts" / "proto-probe.js"
TOL_PX = 1        # kích thước, bo góc
TOL_GAP = 2       # khoảng cách giữa hai dòng chữ, lề trong
TOL_COLOR = 18    # tổng chênh R+G+B

DEVICES = {"web": (1920, 1080), "app": (430, 932)}


# ───────────────────────── probe (prototype) ─────────────────────────

def find_chrome():
    cands = []
    cache = Path.home() / "Library/Caches/ms-playwright"
    if cache.exists():
        cands += sorted(cache.glob("chromium-*/chrome-mac*/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing"), reverse=True)
        cands += sorted(cache.glob("chromium-*/chrome-linux*/chrome"), reverse=True)
    cands += [Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")]
    for name in ("google-chrome", "chromium", "chromium-browser"):
        w = shutil.which(name)
        if w:
            cands.append(Path(w))
    for c in cands:
        if c.exists():
            return str(c)
    sys.exit("Không tìm thấy Chrome/Chromium (cần Playwright chromium hoặc Google Chrome).")


def cmd_probe(a):
    src = Path(a.prototype).resolve()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    chrome = find_chrome()
    tmp = Path(tempfile.mkdtemp(prefix="proto-probe-"))
    page = tmp / src.name
    page.write_text(src.read_text(encoding="utf-8") + "\n<script>\n" + PROBE_JS.read_text(encoding="utf-8") + "\n</script>\n", encoding="utf-8")
    q = []
    if a.state:
        q.append("state=" + a.state.replace(" ", "%20"))
    if a.device:
        q.append("device=" + a.device)
    url = page.as_uri() + "#" + a.screen + ("?" + "&".join(q) if q else "")
    w, h = DEVICES.get(a.device or "web", DEVICES["web"])
    base = [chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--window-size={w},{h}",
            "--virtual-time-budget=6000"]  # không dùng --user-data-dir: Chrome treo ở lần chạy đầu của profile mới
    dom = subprocess.run(base + ["--dump-dom", url], capture_output=True, text=True, timeout=120).stdout
    m = list(re.finditer(r'<pre id="__probe"[^>]*>(.*?)</pre>', dom, re.S))
    m = m[-1] if m else None
    if not m:
        sys.exit(f"Probe không trả kết quả cho {url} (prototype lỗi JS hoặc chưa tải xong).")
    data = json.loads(html.unescape(m.group(1)))
    stem = f"proto-{a.screen}" + (f"--{slug(a.state)}" if a.state else "")
    shot = tmp / "shot.png"
    subprocess.run(base + ["--force-device-scale-factor=2", f"--screenshot={shot}", url], capture_output=True, timeout=120)
    if shot.exists() and data.get("root"):
        crop_png(shot, out / f"{stem}.png", data["root"], scale=2, absolute=True)
        data["png"] = str(out / f"{stem}.png")
    (out / f"{stem}.json").write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    shutil.rmtree(tmp, ignore_errors=True)
    n_text = sum(1 for n in data.get("nodes", []) if n["kind"] == "text")
    print(f"{stem}.json: {n_text} chữ, {len(data.get('nodes', [])) - n_text} khung" + "".join(f"\n  ⚠ {w}" for w in data.get("warnings", [])))


def crop_png(src, dst, rect, scale=2, absolute=False, pad=0):
    try:
        from PIL import Image
    except ImportError:
        shutil.copy(src, dst)
        return
    im = Image.open(src)
    x = rect.get("x", 0) if absolute else rect["x"]
    y = rect.get("y", 0) if absolute else rect["y"]
    box = (max(0, int((x - pad) * scale)), max(0, int((y - pad) * scale)),
           min(im.width, int((x + rect["w"] + pad) * scale)), min(im.height, int((y + rect["h"] + pad) * scale)))
    im.crop(box).save(dst)


# ───────────────────────── diff ─────────────────────────

def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")


def norm(t):
    t = (t or "").replace(" ", " ")
    if t.strip() and set(t.strip()) <= set("•●*"):
        return "•"                         # ô mật khẩu: số chấm là giá trị mẫu, chỉ so kiểu chữ
    t = re.sub(r"\s*\*\s*$", "", t)          # dấu * bắt buộc so riêng
    return re.sub(r"\s+", " ", t).strip().lower()


def rgb(h):
    if not h:
        return None
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def color_diff(a, b):
    if (a is None) != (b is None):
        return True
    if a is None:
        return False
    ra, rb = rgb(a), rgb(b)
    alpha = lambda h: int(h.lstrip("#")[6:8], 16) if len(h.lstrip("#")) == 8 else 255
    return sum(abs(x - y) for x, y in zip(ra, rb)) > TOL_COLOR or abs(alpha(a) - alpha(b)) > 30


def fmt_color(h):
    return h or "không có"


def expand_compact(d):
    """Dạng gọn của figma-probe.js → khuôn chung (giống proto-probe.js)."""
    comps, raw = d.get("c", []), d["n"]
    ids = [x.get("id") or f"#{i}" for i, x in enumerate(raw)]
    nodes = []
    for i, x in enumerate(raw):
        r = x["r"]
        nd = {"id": ids[i], "parent": ids[x["p"]] if x.get("p") is not None else None,
              "rect": {"x": r[0], "y": r[1], "w": r[2], "h": r[3]}}
        if x.get("c") is not None:
            nd["comp"] = comps[x["c"]]
        nd["instanceId"] = ids[i] if x.get("root") else (ids[x["in"]] if x.get("in") is not None else None)
        if x["k"] == "t":
            nd.update(kind="text", text=x["t"], font=x.get("f"), size=x.get("s"), weight=x.get("w"),
                      lineHeight=x.get("lh"), color=x.get("col"), decoration=x.get("dec", "NONE"),
                      upper=bool(x.get("up")), align=x.get("al", "LEFT"), letterSpacing=x.get("ls", 0))
            if x.get("seg"):
                nd["segments"] = [{"text": s[0], "weight": s[1], "color": s[2], "decoration": s[3]} for s in x["seg"]]
        else:
            nd.update(kind="box", role=x.get("role", "box"), name=x.get("nm"), fill=x.get("fill"),
                      stroke=x.get("st"), strokeWidth=x.get("sw", 0), radius=x.get("rad", 0),
                      padding=x.get("pad", [0, 0, 0, 0]), gap=x.get("gap"),
                      direction={"V": "VERTICAL", "H": "HORIZONTAL"}.get(x.get("dir")),
                      shadow=x.get("sh"), icon=x.get("ic"), iconColor=x.get("icol"))
            if x.get("pc") is not None:
                nd["parentComp"] = comps[x["pc"]]
        nodes.append(nd)
    return {"side": "figma", "frameId": d.get("frameId"), "name": d.get("name"),
            "root": {"w": d["root"][0], "h": d["root"][1]}, "warnings": [], "nodes": nodes}


def load_figma(path, frame_id):
    d = json.loads(Path(path).read_text(encoding="utf-8"))
    if isinstance(d, dict) and "n" in d:
        return expand_compact(d)
    comps = []
    if isinstance(d, dict) and "frames" in d:
        comps, frames = d.get("comps", []), d["frames"]
    elif isinstance(d, list):
        frames = d
    else:
        frames = [d]
    if frame_id:
        frames = [f for f in frames if f.get("frameId") == frame_id]
    if len(frames) != 1:
        sys.exit(f"{path}: cần đúng 1 frame (dùng --frame <nodeId>), đang có {len(frames)}")
    f = frames[0]
    for n in f["nodes"]:
        if "c" in n:
            n["comp"] = comps[n["c"]]
        n.setdefault("padding", [0, 0, 0, 0])
        n.setdefault("radius", 0)
    return f


def contains(outer, inner, slack=1):
    return (inner["x"] >= outer["x"] - slack and inner["y"] >= outer["y"] - slack and
            inner["x"] + inner["w"] <= outer["x"] + outer["w"] + slack and
            inner["y"] + inner["h"] <= outer["y"] + outer["h"] + slack)


def within(side, text):
    """Giới hạn một bên vào khung nhỏ nhất chứa chữ `text` (so 1 component với DS ở --before)."""
    if not text:
        return side
    t = [n for n in side["nodes"] if n["kind"] == "text" and norm(n["text"]) == norm(text)]
    if not t:
        sys.exit(f'Không thấy chữ "{text}" để giới hạn vùng so')
    boxes = [n for n in side["nodes"] if n["kind"] == "box" and contains(n["rect"], t[0]["rect"])
             and (n.get("fill") or n.get("stroke") or n.get("role") not in (None, "box"))]
    if not boxes:
        return side
    b = min(boxes, key=lambda n: n["rect"]["w"] * n["rect"]["h"])
    side = dict(side)
    side["nodes"] = [n for n in side["nodes"] if contains(b["rect"], n["rect"])]
    return side


class Differ:
    def __init__(self, P, F, screen, state):
        self.P, self.F, self.screen, self.state = P, F, screen, state or ""
        self.items = []
        self.pt = [n for n in P["nodes"] if n["kind"] == "text" and n["text"].strip() != "*"]
        self.p_req = [n for n in P["nodes"] if n["kind"] == "text" and n["text"].strip() == "*"]
        self.ft = [n for n in F["nodes"] if n["kind"] == "text" and n["text"].strip() != "*"]
        self.f_req = [n for n in F["nodes"] if n["kind"] == "text" and n["text"].strip() == "*"]  # dấu * node riêng (XDSFieldLabel «Bắt buộc»)
        self.pairs = []  # (p, f)

    # ── khoá + ghi mục
    def add(self, typ, element, prop, pv, fv, where, node=None):
        key = "k-" + hashlib.sha1(f"{self.screen}|{self.state}|{element}|{prop}".encode()).hexdigest()[:8]
        self.items.append({"key": key, "type": typ, "element": element, "prop": prop,
                           "proto": pv, "figma": fv, "where": where,
                           "figmaNode": node.get("id") if node else None})

    def where_text(self, f):
        c = f.get("comp")
        return f"Component: {c['name']}" + (f" ({c['page']})" if c.get("page") else "") if c else "Màn"

    def where_box(self, f, prop):
        c = f.get("comp")
        if not c:
            return "Màn"
        is_root = f.get("instanceId") is not None and f.get("instanceId") == f.get("id")
        if prop == "Rộng" or (is_root and prop == "Cao"):
            return "Màn"
        return f"Component: {c['name']}" + (f" ({c['page']})" if c.get("page") else "")

    # ── 1. ghép chữ
    def match_texts(self):
        used_f = set()
        by_key = {}
        for f in sorted(self.ft, key=lambda n: (n["rect"]["y"], n["rect"]["x"])):
            by_key.setdefault(norm(f["text"]), []).append(f)
        rest = []
        for p in sorted(self.pt, key=lambda n: (n["rect"]["y"], n["rect"]["x"])):
            cands = [f for f in by_key.get(norm(p["text"]), []) if f["id"] not in used_f]
            if cands:
                f = cands[0]
                used_f.add(f["id"])
                self.pairs.append((p, f))
            else:
                rest.append(p)
        # gần giống: chữ đã sửa câu
        for p in rest:
            best, score = None, 0.0
            for f in self.ft:
                if f["id"] in used_f:
                    continue
                s = difflib.SequenceMatcher(None, norm(p["text"]), norm(f["text"])).ratio()
                if s > score:
                    best, score = f, s
            if best and score >= 0.75:
                used_f.add(best["id"])
                self.pairs.append((p, best))
                self.add("Lệch", short(p["text"]), "Chữ", p["text"], best["text"], self.where_text(best), best)
            else:
                self.add("Mới", short(p["text"]), "Phần tử", "có", "Figma chưa có", "Màn")
        for f in self.ft:
            if f["id"] not in used_f:
                self.add("Thừa", short(f["text"]), "Phần tử", "không có", "Figma có", self.where_text(f), f)

    # ── 2. kiểu chữ
    def compare_text_styles(self):
        for p, f in self.pairs:
            el, w = short(p["text"]), self.where_text(f)
            if abs(p["size"] - f["size"]) > 0.5:
                self.add("Lệch", el, "Cỡ chữ", p["size"], f["size"], w, f)
            if p["weight"] != f["weight"]:
                self.add("Lệch", el, "Độ đậm", p["weight"], f["weight"], w, f)
            if not p.get("placeholder") and p.get("lineHeight") and f.get("lineHeight") and abs(p["lineHeight"] - f["lineHeight"]) > TOL_PX:
                self.add("Lệch", el, "Line-height", p["lineHeight"], f["lineHeight"], w, f)
            if color_diff(p.get("color"), f.get("color")):
                self.add("Lệch", el, "Màu chữ", fmt_color(p.get("color")), fmt_color(f.get("color")), w, f)
            if (p.get("decoration") or "NONE") != (f.get("decoration") or "NONE"):
                self.add("Lệch", el, "Gạch chân", p.get("decoration") or "NONE", f.get("decoration") or "NONE", w, f)
            if abs((p.get("letterSpacing") or 0) - (f.get("letterSpacing") or 0)) > 0.2:
                self.add("Lệch", el, "Giãn chữ", p.get("letterSpacing") or 0, f.get("letterSpacing") or 0, w, f)
            if bool(p.get("upper")) != bool(f.get("upper")):
                self.add("Lệch", el, "Viết hoa", p.get("upper"), f.get("upper"), w, f)
            if p.get("font") and f.get("font") and p["font"].lower() != f["font"].lower():
                self.add("Lệch", el, "Font", p["font"], f["font"], w, f)
            self.compare_required_mark(p, f)

    def compare_required_mark(self, p, f):
        req = [r for r in self.p_req if abs(r["rect"]["y"] - p["rect"]["y"]) <= 4 and 0 <= r["rect"]["x"] - (p["rect"]["x"] + p["rect"]["w"]) <= 12]
        fseg = next((s for s in (f.get("segments") or []) if s["text"].strip() == "*"), None)
        fnode = next((r for r in self.f_req if abs(r["rect"]["y"] - f["rect"]["y"]) <= 4 and 0 <= r["rect"]["x"] - (f["rect"]["x"] + f["rect"]["w"]) <= 12), None)
        if fnode and not fseg:
            fseg = fnode
        f_has = f["text"].rstrip().endswith("*") or fnode is not None
        if not req and not f_has:
            return
        el = short(p["text"]) + " — dấu *"
        if req and not f_has:
            self.add("Lệch", el, "Phần tử", "có", "Figma không có", self.where_text(f), f)
        elif f_has and not req and not p["text"].rstrip().endswith("*"):
            self.add("Lệch", el, "Phần tử", "không có", "Figma có", self.where_text(f), f)
        elif req:
            fcol = fseg["color"] if fseg else f.get("color")
            if color_diff(req[0].get("color"), fcol):
                self.add("Lệch", el, "Màu", fmt_color(req[0].get("color")), fmt_color(fcol), self.where_text(f), f)

    # ── 3. khung chứa chữ (thẻ, nút, ô nhập, khối nền)
    def text_set(self, side_nodes, box, idx_of):
        return frozenset(i for t, i in idx_of.items() if contains(box["rect"], t))

    def best_box(self, boxes):
        visual = [b for b in boxes if b.get("fill") or b.get("stroke")]
        ctrl = [b for b in boxes if b.get("role") not in (None, "box")]
        pool = visual or ctrl or boxes
        return min(pool, key=lambda n: n["rect"]["w"] * n["rect"]["h"])

    def match_boxes(self):
        p_idx = {id(p): i for i, (p, f) in enumerate(self.pairs)}
        f_idx = {id(f): i for i, (p, f) in enumerate(self.pairs)}
        p_rect = {i: p["rect"] for i, (p, f) in enumerate(self.pairs)}
        f_rect = {i: f["rect"] for i, (p, f) in enumerate(self.pairs)}

        def group(nodes, rects):
            g = {}
            for b in nodes:
                if b["kind"] != "box" or b.get("parent") is None:
                    continue
                s = frozenset(i for i, r in rects.items() if contains(b["rect"], r))
                if s:
                    g.setdefault(s, []).append(b)
            return g

        gp, gf = group(self.P["nodes"], p_rect), group(self.F["nodes"], f_rect)
        out = []
        for s, pb in gp.items():
            if s not in gf:
                continue
            p, f = self.best_box(pb), self.best_box(gf[s])
            if not (p.get("fill") or p.get("stroke") or f.get("fill") or f.get("stroke") or p.get("role") not in (None, "box")):
                continue
            label = self.box_label(p, s)
            out.append((label, p, f, s))
        return out

    def box_label(self, p, s):
        first = min(s)
        t = short(self.pairs[first][0]["text"], 28)
        kind = {"button": "Nút", "input": "Ô nhập", "link": "Link", "checkbox": "Checkbox"}.get(p.get("role"), "Khung")
        return f"{kind} «{t}»" + (f" +{len(s) - 1} chữ" if len(s) > 1 and kind == "Khung" else "")

    def compare_boxes(self):
        matched = self.match_boxes()
        visual = [(p, f) for _, p, f, _ in matched if p.get("fill") or p.get("stroke")]

        def width_follows_parent(p, f):
            # Rộng lệch chỉ vì khung cha có lề trong khác (đã báo ở khung cha) → không báo lại.
            for vp, vf in visual:
                if vp is p or not contains(vp["rect"], p["rect"]) or not contains(vf["rect"], f["rect"]):
                    continue
                dl = (p["rect"]["x"] - vp["rect"]["x"]) - (f["rect"]["x"] - vf["rect"]["x"])
                if abs((p["rect"]["w"] - f["rect"]["w"]) + 2 * dl) <= TOL_GAP:
                    return True
            return False

        for label, p, f, s in matched:
            pr, fr = p["rect"], f["rect"]
            if abs(pr["w"] - fr["w"]) > TOL_PX and not (p.get("role") == "box" and not p.get("fill") and not p.get("stroke")) \
                    and not width_follows_parent(p, f):
                self.add("Lệch", label, "Rộng", pr["w"], fr["w"], self.where_box(f, "Rộng"), f)
            if abs(pr["h"] - fr["h"]) > TOL_PX:
                self.add("Lệch", label, "Cao", pr["h"], fr["h"], self.where_box(f, "Cao"), f)
            if abs((p.get("radius") or 0) - (f.get("radius") or 0)) > TOL_PX and (p.get("fill") or p.get("stroke") or f.get("fill") or f.get("stroke")):
                self.add("Lệch", label, "Bo góc", p.get("radius") or 0, f.get("radius") or 0, self.where_box(f, "Bo góc"), f)
            if color_diff(p.get("fill"), f.get("fill")):
                self.add("Lệch", label, "Nền", fmt_color(p.get("fill")), fmt_color(f.get("fill")), self.where_box(f, "Nền"), f)
            if color_diff(p.get("stroke"), f.get("stroke")) or abs((p.get("strokeWidth") or 0) - (f.get("strokeWidth") or 0)) > 0.5:
                pv = f"{p.get('strokeWidth') or 0}px {fmt_color(p.get('stroke'))}" if p.get("stroke") else "không có"
                fv = f"{f.get('strokeWidth') or 0}px {fmt_color(f.get('stroke'))}" if f.get("stroke") else "không có"
                self.add("Lệch", label, "Viền", pv, fv, self.where_box(f, "Viền"), f)
            if shadow_diff(p.get("shadow"), f.get("shadow")):
                self.add("Lệch", label, "Bóng đổ", fmt_shadow(p.get("shadow")), fmt_shadow(f.get("shadow")), self.where_box(f, "Bóng đổ"), f)
            # lề trong suy từ vị trí chữ đầu tiên (cùng cách đo cho cả hai bên)
            pi = [self.pairs[i][0]["rect"] for i in s]
            fi = [self.pairs[i][1]["rect"] for i in s]
            pl, fl = min(r["x"] for r in pi) - pr["x"], min(r["x"] for r in fi) - fr["x"]
            pt, ft = min(r["y"] for r in pi) - pr["y"], min(r["y"] for r in fi) - fr["y"]
            if p.get("role") not in ("button",) and abs(pl - fl) > TOL_GAP and (p.get("fill") or p.get("stroke") or p.get("role") == "input"):
                self.add("Lệch", label, "Lề trong trái", pl, fl, self.where_box(f, "Lề trong"), f)
            if abs(pt - ft) > TOL_GAP and (p.get("fill") or p.get("stroke")) and len(s) > 1:
                self.add("Lệch", label, "Lề trong trên", pt, ft, self.where_box(f, "Lề trong"), f)

    # ── 4. nhịp dọc + xếp hàng giữa các chữ liền nhau
    def compare_rhythm(self):
        seq = sorted(range(len(self.pairs)), key=lambda i: (self.pairs[i][0]["rect"]["y"], self.pairs[i][0]["rect"]["x"]))
        for a, b in zip(seq, seq[1:]):
            pa, fa = self.pairs[a]
            pb, fb = self.pairs[b]
            p_row = overlap_y(pa["rect"], pb["rect"])
            f_row = overlap_y(fa["rect"], fb["rect"])
            el = f"«{short(pa['text'], 22)}» → «{short(pb['text'], 22)}»"
            same_inst = fa.get("instanceId") and fa.get("instanceId") == fb.get("instanceId")
            where = self.where_text(fa) if same_inst else "Màn"
            if p_row != f_row:
                self.add("Lệch", el, "Xếp hàng", "cùng hàng" if p_row else "xếp dọc", "cùng hàng" if f_row else "xếp dọc", where, fb)
                continue
            if p_row:
                pg = pb["rect"]["x"] - (pa["rect"]["x"] + pa["rect"]["w"])
                fg = fb["rect"]["x"] - (fa["rect"]["x"] + fa["rect"]["w"])
                if pg > 0 and fg > 0 and abs(pg - fg) > TOL_GAP and max(pg, fg) < 120:
                    self.add("Lệch", el, "Khoảng cách ngang", pg, fg, where, fb)
            else:
                pg = pb["rect"]["y"] - (pa["rect"]["y"] + pa["rect"]["h"])
                fg = fb["rect"]["y"] - (fa["rect"]["y"] + fa["rect"]["h"])
                if abs(pg - fg) > TOL_GAP:
                    self.add("Lệch", el, "Khoảng cách dọc", pg, fg, where, fb)

    # ── 5. canh lề chữ trong khung có nền/viền gần nhất
    def compare_align(self):
        def frame_of(side, t):
            boxes = [n for n in side["nodes"] if n["kind"] == "box" and (n.get("fill") or n.get("stroke"))
                     and contains(n["rect"], t["rect"]) and n.get("parent") is not None]
            return min(boxes, key=lambda n: n["rect"]["w"] * n["rect"]["h"]) if boxes else None

        def cls(t, b):
            left = t["rect"]["x"] - b["rect"]["x"]
            right = b["rect"]["x"] + b["rect"]["w"] - (t["rect"]["x"] + t["rect"]["w"])
            if abs(left - right) <= 4:
                return "giữa"
            return "trái" if left < right else "phải"

        for p, f in self.pairs:
            bp, bf = frame_of(self.P, p), frame_of(self.F, f)
            if not bp or not bf or p["rect"]["w"] > bp["rect"]["w"] * 0.8:
                continue
            cp, cf = cls(p, bp), cls(f, bf)
            if cp != cf:
                self.add("Lệch", short(p["text"]), "Canh lề", cp, cf, self.where_text(f) if f.get("comp") else "Màn", f)

    # ── 6. khối không có chữ: checkbox, đường kẻ
    def compare_textless(self):
        def leaf_checkbox(side):
            c = [n for n in side["nodes"] if n["kind"] == "box" and n.get("role") in ("checkbox", "radio") and (n.get("stroke") or n.get("fill") or n.get("tag") == "input")]
            keep = [n for n in c if not any(o is not n and contains(n["rect"], o["rect"]) and o["rect"]["w"] < n["rect"]["w"] for o in c)]
            return sorted(keep, key=lambda n: (n["rect"]["y"], n["rect"]["x"]))
        for i, (p, f) in enumerate(zip(leaf_checkbox(self.P), leaf_checkbox(self.F))):
            label = f"Checkbox #{i + 1}"
            if abs(p["rect"]["w"] - f["rect"]["w"]) > TOL_PX or abs(p["rect"]["h"] - f["rect"]["h"]) > TOL_PX:
                self.add("Lệch", label, "Kích thước", f"{p['rect']['w']}×{p['rect']['h']}", f"{f['rect']['w']}×{f['rect']['h']}", self.where_box(f, "Kích thước"), f)
            if abs((p.get("radius") or 0) - (f.get("radius") or 0)) > TOL_PX and p.get("radius") is not None:
                self.add("Lệch", label, "Bo góc", p.get("radius") or 0, f.get("radius") or 0, self.where_box(f, "Bo góc"), f)

        def dividers(side):
            return [n for n in side["nodes"] if n["kind"] == "box" and (n.get("fill") or n.get("stroke"))
                    and n["rect"]["w"] >= 40 and n["rect"]["h"] <= 2]
        pd, fd = dividers(self.P), dividers(self.F)
        if len(pd) != len(fd):
            self.add("Lệch", "Đường kẻ ngang", "Số lượng", len(pd), len(fd), "Màn", fd[0] if fd else None)

    # ── 7. icon: ghép theo tên, còn lại ghép theo vị trí (đã trừ độ lệch khung suy từ các cặp chữ)
    def offset(self):
        if not self.pairs:
            return 0, 0
        dx = sorted(f["rect"]["x"] - p["rect"]["x"] for p, f in self.pairs)
        dy = sorted(f["rect"]["y"] - p["rect"]["y"] for p, f in self.pairs)
        return dx[len(dx) // 2], dy[len(dy) // 2]

    def icon_where(self, f):
        c = f.get("parentComp")
        return f"Component: {c['name']}" + (f" ({c['page']})" if c.get("page") else "") if c else "Màn"

    def anchor(self, icon, side):
        """Cặp chữ «cùng hàng» với icon (ưu tiên chữ chồng dải dọc của icon, gần nhất theo chiều ngang)."""
        r = icon["rect"]; cx, cy = r["x"] + r["w"] / 2, r["y"] + r["h"] / 2
        best, score = None, None
        for i, pf in enumerate(self.pairs):
            t = pf[side]["rect"]
            same_row = t["y"] <= cy <= t["y"] + t["h"] or r["y"] <= t["y"] + t["h"] / 2 <= r["y"] + r["h"]
            gap = max(0, t["x"] - (r["x"] + r["w"]), r["x"] - (t["x"] + t["w"]))
            sc = (0 if same_row else 1, gap if same_row else abs(t["y"] + t["h"] / 2 - cy) * 3 + gap)
            if score is None or sc < score:
                best, score = i, sc
        return best

    def icon_label(self, p, f):
        a = self.anchor(p, 0)
        return f"Icon {p.get('icon') or (f or {}).get('icon') or '?'}" + (f" cạnh «{short(self.pairs[a][0]['text'], 24)}»" if a is not None else "")

    def compare_icons(self):
        ALIAS = {"spinner": "loader", "loader-circle": "loader", "loader-2": "loader"}
        GENERIC = {"", "icon", "icon-button", "button", "iconbutton"}
        icon_key = lambda n: (lambda k: ALIAS.get(k, k))(re.sub(r"[^a-z0-9]+", "-", (n or "").lower().split("/")[-1]).strip("-"))
        pi = [n for n in self.P["nodes"] if n["kind"] == "box" and n.get("role") == "icon" and n["rect"]["w"] <= 48]
        fi = [n for n in self.F["nodes"] if n["kind"] == "box" and n.get("role") == "icon"]
        dx, dy = self.offset()
        dist = lambda p, f: abs(p["rect"]["x"] + dx - f["rect"]["x"]) + abs(p["rect"]["y"] + dy - f["rect"]["y"])
        pairs, used = [], set()
        for p in sorted(pi, key=lambda n: (n["rect"]["y"], n["rect"]["x"])):
            same = [f for f in fi if id(f) not in used and icon_key(f.get("icon")) == icon_key(p.get("icon")) and dist(p, f) <= 120]
            if same:
                f = min(same, key=lambda f: dist(p, f)); used.add(id(f)); pairs.append((p, f))
        # Icon Figma đặt tên chung («Icon Button», «Icon») → ghép với icon prototype cùng hàng với cùng 1 cặp chữ;
        # không báo «khác icon» vì không biết tên thật.
        for p in [p for p in pi if not any(p is a for a, _ in pairs)]:
            ap = self.anchor(p, 0)
            gen = [f for f in fi if id(f) not in used and icon_key(f.get("icon")) in GENERIC and self.anchor(f, 1) == ap]
            if ap is not None and gen:
                f = min(gen, key=lambda f: dist(p, f)); used.add(id(f)); pairs.append((p, f))
        for p in [p for p in pi if not any(p is a for a, _ in pairs)]:
            near = [f for f in fi if id(f) not in used and dist(p, f) <= 16]
            if near:
                f = min(near, key=lambda f: dist(p, f)); used.add(id(f)); pairs.append((p, f))
                self.add("Lệch", self.icon_label(p, f), "Icon", p.get("icon") or "?", f.get("icon") or "?", self.icon_where(f), f)
            else:
                self.add("Mới", self.icon_label(p, None), "Phần tử", "có", "Figma chưa có", "Màn")
        for f in fi:
            if id(f) not in used:
                self.add("Thừa", f"Icon {f.get('icon') or '?'}", "Phần tử", "không có", "Figma có", self.icon_where(f), f)
        for p, f in pairs:
            lab = self.icon_label(p, f)
            if abs(p["rect"]["w"] - f["rect"]["w"]) > TOL_PX or abs(p["rect"]["h"] - f["rect"]["h"]) > TOL_PX:
                self.add("Lệch", lab, "Kích thước", f"{p['rect']['w']}×{p['rect']['h']}", f"{f['rect']['w']}×{f['rect']['h']}", self.icon_where(f), f)
            if p.get("iconColor") and f.get("iconColor") and color_diff(p["iconColor"], f["iconColor"]):
                self.add("Lệch", lab, "Màu", p["iconColor"], f["iconColor"], self.icon_where(f), f)

    # ── 8. ảnh / logo: so kích thước theo thứ tự trên → dưới
    def compare_images(self):
        pi = sorted([n for n in self.P["nodes"] if n["kind"] == "box" and n.get("role") == "image"], key=lambda n: n["rect"]["y"])
        fi = sorted([n for n in self.F["nodes"] if n["kind"] == "box" and (n.get("role") == "image" or
                     (n.get("comp") and re.search(r"logo", n["comp"]["name"], re.I) and n.get("instanceId") == n.get("id")))], key=lambda n: n["rect"]["y"])
        for i, (p, f) in enumerate(zip(pi, fi)):
            if abs(p["rect"]["w"] - f["rect"]["w"]) > TOL_GAP or abs(p["rect"]["h"] - f["rect"]["h"]) > TOL_GAP:
                self.add("Lệch", f"Ảnh/logo #{i + 1}", "Kích thước", f"{p['rect']['w']}×{p['rect']['h']}", f"{f['rect']['w']}×{f['rect']['h']}", self.where_box(f, "Kích thước"), f)
        if len(pi) != len(fi):
            self.add("Lệch", "Ảnh/logo", "Số lượng", len(pi), len(fi), "Màn", fi[0] if fi else None)

    def run(self):
        self.match_texts()
        self.compare_text_styles()
        self.compare_boxes()
        self.compare_rhythm()
        self.compare_align()
        self.compare_textless()
        self.compare_icons()
        self.compare_images()
        return self.items


def overlap_y(a, b):
    top, bot = max(a["y"], b["y"]), min(a["y"] + a["h"], b["y"] + b["h"])
    return bot - top > min(a["h"], b["h"]) * 0.5


def short(t, n=40):
    t = re.sub(r"\s+", " ", t or "").strip()
    return t if len(t) <= n else t[: n - 1] + "…"


def read_ledger(path):
    """Sổ quyết định: bảng markdown có cột Khoá + Quyết định.

    Sổ có thể gộp nhiều dòng máy vào 1 dòng quyết định (vd `c01` = dấu * mất đỏ ở 22 chỗ): bảng
    "Khoá máy" có cột Khoá + Dòng (vd `k-1a2b3c4d` → `c01`); dòng máy nhận Quyết định của dòng gộp.
    """
    if not path or not Path(path).exists():
        return {}
    rows, header = {}, None
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            header = None if not line.strip() else header
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if header is None:
            header = cells
            continue
        if set("".join(cells)) <= set("-: "):
            continue
        row = dict(zip(header, cells))
        k = row.get("Khoá", "").strip("` ")
        if k:
            rows[k] = row
    for k, row in list(rows.items()):
        ref = row.get("Dòng", "").strip("` ")
        if ref and not row.get("Quyết định") and ref in rows:
            rows[k] = dict(row, **{"Quyết định": rows[ref].get("Quyết định", ""), "Gộp vào": ref})
    return rows


SUPPRESS = ("theo ds", "giữ figma", "bỏ qua")


def cmd_diff(a):
    P = json.loads(Path(a.proto).read_text(encoding="utf-8"))
    F = load_figma(a.figma, a.frame)
    P, F = within(P, a.proto_within), within(F, a.figma_within)
    items = Differ(P, F, a.screen, a.state).run()
    ledger = read_ledger(a.ledger)
    kept, suppressed, regress = [], 0, 0
    for it in items:
        row = ledger.get(it["key"])
        dec = (row or {}).get("Quyết định", "").lower()
        if row and any(dec.startswith(s) for s in SUPPRESS):
            suppressed += 1
            continue
        if row and dec.startswith("theo prototype"):
            it["note"] = "đã duyệt sửa theo prototype nhưng Figma vẫn lệch"
            regress += 1
        elif row:
            it["note"] = f"sổ ghi: {row.get('Quyết định', '')}"
        if row and row.get("Gộp vào"):
            it["group"] = row["Gộp vào"]
        kept.append(it)
    res = {"screen": a.screen, "state": a.state or "", "frame": F.get("frameId"), "frameName": F.get("name"),
           "proto": a.proto, "figma": a.figma, "warnings": P.get("warnings", []) + F.get("warnings", []),
           "suppressed": suppressed, "regressed": regress, "items": kept}
    if a.proto_png and a.figma_png and a.crop_out:
        res["crops"] = crop_pair(P, F, a)
    Path(a.out).write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    n_new = sum(1 for i in kept if i["type"] == "Mới")
    print(f"{a.screen}{' · ' + a.state if a.state else ''}: {n_new} mới · {len(kept) - n_new} lệch · {suppressed} đã chốt trong sổ" +
          (f" · {regress} đã duyệt mà chưa sửa" if regress else "") + "".join(f"\n  ⚠ {w}" for w in res["warnings"]))


def png_scale(png, data, default):
    """Tỷ lệ ảnh/khung của từng bên: get_screenshot của Figma có thể trả 1x dù xin 3840."""
    try:
        from PIL import Image
        w = (data.get("root") or {}).get("w")
        return Image.open(png).width / w if w else default
    except Exception:
        return default


def shadow_diff(a, b):
    if bool(a) != bool(b):
        return True
    if not a:
        return False
    return color_diff(a[0], b[0]) or any(abs(x - y) > TOL_PX for x, y in zip(a[1:], b[1:]))


def fmt_shadow(v):
    return f"{v[1]:g} {v[2]:g} {v[3]:g} {v[4]:g} {v[0]}" if v else "không có"


def crop_pair(P, F, a):
    """Cắt hai ảnh về cùng vùng nội dung (bao các chữ đã ghép) để đặt cạnh nhau."""
    def bbox(nodes):
        xs = [n["rect"] for n in nodes if n["kind"] == "text" or n.get("role") in ("icon", "image")]
        if not xs:
            return None
        x0, y0 = min(r["x"] for r in xs), min(r["y"] for r in xs)
        x1, y1 = max(r["x"] + r["w"] for r in xs), max(r["y"] + r["h"] for r in xs)
        return {"x": x0, "y": y0, "w": x1 - x0, "h": y1 - y0}
    out = Path(a.crop_out)
    out.mkdir(parents=True, exist_ok=True)
    stem = slug(a.screen + " " + (a.state or ""))
    res = {}
    for side, data, png in (("proto", P, a.proto_png), ("figma", F, a.figma_png)):
        b = bbox(data["nodes"])
        if b:
            dst = out / f"{stem}-{side}.png"
            crop_png(png, dst, b, scale=png_scale(png, data, a.scale), pad=48)
            res[side] = str(dst)
    return res


# ───────────────────────── report ─────────────────────────

def cmd_report(a):
    lines = []
    tot_new = tot_dev = 0
    for p in a.diffs:
        d = json.loads(Path(p).read_text(encoding="utf-8"))
        items = d["items"]
        n_new = sum(1 for i in items if i["type"] == "Mới")
        tot_new += n_new
        tot_dev += len(items) - n_new
        title = d["screen"] + (f" · {d['state']}" if d["state"] else "")
        lines.append(f"### {title}\n")
        lines.append(f"Figma: `{d.get('frameName') or d.get('frame')}` · {n_new} mới · {len(items) - n_new} lệch · {d['suppressed']} đã chốt trong sổ\n")
        for w in d.get("warnings", []):
            lines.append(f"> ⚠ {w}\n")
        if not items:
            lines.append("Khớp prototype.\n")
            continue
        lines.append("| # | Loại | Phần tử | Thuộc tính | Prototype | Figma | Sửa ở | Khoá |")
        lines.append("|---|---|---|---|---|---|---|---|")
        order = {"Mới": 0, "Thừa": 1, "Lệch": 2}
        for n, it in enumerate(sorted(items, key=lambda i: (order[i["type"]], i["where"] == "Màn", i["element"])), 1):
            note = f" ({it['note']})" if it.get("note") else ""
            lines.append(f"| {n} | {it['type']} | {esc(it['element'])} | {it['prop']} | {esc(it['proto'])} | {esc(it['figma'])}{note} | {esc(it['where'])} | `{it['key']}` |")
        lines.append("")
    head = [f"# Đối chiếu prototype ↔ Figma\n", f"Tổng: {tot_new} mới · {tot_dev} lệch\n",
            "Giới hạn: ghép theo chữ hiển thị; icon ghép theo tên/vị trí; không so nội dung ảnh, gradient.\n"]
    text = "\n".join(head + lines)
    if a.out:
        Path(a.out).write_text(text, encoding="utf-8")
        print(f"Đã ghi {a.out}: {tot_new} mới · {tot_dev} lệch")
    else:
        print(text)


def esc(v):
    return str(v).replace("|", "\\|")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("probe")
    p.add_argument("prototype")
    p.add_argument("--screen", required=True)
    p.add_argument("--state")
    p.add_argument("--device", choices=["web", "app"])
    p.add_argument("--out", required=True)
    p.set_defaults(fn=cmd_probe)
    d = sub.add_parser("diff")
    d.add_argument("--proto", required=True)
    d.add_argument("--figma", required=True)
    d.add_argument("--frame")
    d.add_argument("--screen", required=True)
    d.add_argument("--state")
    d.add_argument("--ledger")
    d.add_argument("--proto-within")
    d.add_argument("--figma-within")
    d.add_argument("--proto-png")
    d.add_argument("--figma-png")
    d.add_argument("--crop-out")
    d.add_argument("--scale", type=float, default=2)
    d.add_argument("--out", required=True)
    d.set_defaults(fn=cmd_diff)
    r = sub.add_parser("report")
    r.add_argument("diffs", nargs="+")
    r.add_argument("--out")
    r.set_defaults(fn=cmd_report)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
