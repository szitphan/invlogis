"""Thư viện dùng chung cho build.py và build_template.py: màu, phông, đo chữ, phần tử slide."""
from pathlib import Path
from PIL import ImageFont

HERE = Path(__file__).resolve().parent
BRAND = HERE.parents[2]            # design/brand
SRC = BRAND / "invlogis"           # bộ nhận diện đã duyệt (Mốc 2)
TOOLS = BRAND / "_drafts" / "_tools"
ASSETS = HERE / "assets"

W, H = 1920, 1080
INK, NIGHT, NAVY = "#0E1442", "#0B1033", "#17206F"
COBALT, PERI, PERI_L = "#2F43DB", "#97A6FF", "#C4CDFF"
SMOKE, PAPER, SLATE, WHITE = "#E6EAF8", "#FAF8F4", "#4A5380", "#FFFFFF"
SLATE_T = "#343C6A"   # chữ phụ trên nền sáng/periwinkle (đạt 4,5:1 trên cả vùng gradient)
LAV = "#E0E4FA"

FONT_FILES = {
    ("d", 300): "Lexend-300.ttf", ("d", 400): "Lexend-400.ttf", ("d", 600): "Lexend-600.ttf",
    ("b", 300): "BeVietnamPro-300.ttf", ("b", 400): "BeVietnamPro-400.ttf",
    ("b", 500): "BeVietnamPro-500.ttf", ("b", 600): "BeVietnamPro-600.ttf",
    ("m", 400): "JetBrainsMono-400.ttf", ("m", 500): "JetBrainsMono-500.ttf",
}
CSS_FAMILY = {"d": "Lexend", "b": "Be Vietnam Pro", "m": "JetBrains Mono"}
# tên họ chữ của bản tĩnh (name ID 1) — dùng trong PPTX
PPTX_FAMILY = {
    ("d", 300): "Lexend Light", ("d", 400): "Lexend", ("d", 600): "Lexend SemiBold",
    ("b", 300): "Be Vietnam Pro Light", ("b", 400): "Be Vietnam Pro", ("b", 500): "Be Vietnam Pro Medium",
    ("b", 600): "Be Vietnam Pro SemiBold", ("m", 400): "JetBrains Mono", ("m", 500): "JetBrains Mono Medium",
}
_fc = {}
def pil_font(f, w, size):
    k = (f, w, round(size))
    if k not in _fc:
        _fc[k] = ImageFont.truetype(str(SRC / "fonts" / FONT_FILES[(f, w)]), round(size))
    return _fc[k]

def text_w(s, f, w, size, ls=0.0):
    return pil_font(f, w, size).getlength(s) + ls * size * len(s)

def wrap(s, f, w, size, width, ls=0.0):
    lines, cur = [], ""
    for word in s.split(" "):
        t = (cur + " " + word).strip()
        if cur and text_w(t, f, w, size, ls) > width:
            lines.append(cur); cur = word
        else:
            cur = t
    lines.append(cur)
    return lines

def hex2rgb(h):
    h = h.lstrip("#"); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

# ---------- phần tử ----------
class Slide:
    def __init__(self, name, bg=None, notes="", mode="dark"):
        self.name, self.bg, self.notes, self.mode = name, bg, notes, mode
        self.els = []
    def add(self, e): self.els.append(e); return e

def R(s, x, y, w, h, fill=None, a=1.0, line=None, lw=1.5, la=1.0, r=0, grad=None, blur=0):
    return s.add(dict(t="rect", x=x, y=y, w=w, h=h, fill=fill, a=a, line=line, lw=lw, la=la, r=r, grad=grad, blur=blur))

def IMG(s, path, x, y, w, h):
    return s.add(dict(t="img", path=path, x=x, y=y, w=w, h=h))

def T(s, x, y, w, h, paras, size=28, font="b", weight=400, color=INK, align="l", lh=1.3,
      anchor="t", ls=0.0, gap=0, nowrap=False):
    """paras: str (\\n tách đoạn) | list[para]; para: str | list[run]; run: str | (str, {color,weight,font})."""
    if isinstance(paras, str): paras = paras.split("\n")
    return s.add(dict(t="text", x=x, y=y, w=w, h=h, paras=paras, size=size, font=font, weight=weight,
                      color=color, align=align, lh=lh, anchor=anchor, ls=ls, gap=gap, nowrap=nowrap))

def chip(s, x, y, text, color=COBALT, fill=WHITE, a=0.0, size=20, h=44, line=None, weight=400, align="l", pad=18, w=None):
    """Nhãn mono kiểu [eDO]; trả về chiều rộng."""
    tw = text_w(text, "m", weight, size) + 2 * pad
    cw = w or tw
    ax = x if align == "l" else (x - cw if align == "r" else x - cw / 2)
    R(s, ax, y, cw, h, fill=fill if a else None, a=a, line=line or color, lw=1.5, la=0.9, r=h / 2)
    T(s, ax, y, cw, h, text, size=size, font="m", weight=weight, color=color, align="c", anchor="m", lh=1.0)
    return cw

def label(s, text, dark=True, c=None):
    T(s, 120, 76, 1200, 36, text, size=22, font="m", color=(c or PERI) if dark else NAVY, ls=0.04, lh=1.0)

def footer(s, n, dark=True, note=None, c=None):
    logo = "assets/logo/invlogis-reverse.png" if dark else "assets/logo/invlogis-primary.png"
    IMG(s, logo, 120, 996, 36 * 3.5617, 36)
    T(s, 1500, 1000, 300, 28, ("%s%02d" % ((note + "  ·  ") if note else "", n)), size=20, font="m",
      color=(c or PERI_L) if dark else SLATE_T, align="r", lh=1.0)

def field(s, x, y, w, key, val, dark=False, h=84, fill=LAV, fa=1.0, vs=26, ks=16, line=None):
    R(s, x, y, w, h, fill=fill, a=fa, line=line, r=14)
    T(s, x + 20, y + 12, w - 40, 22, key, size=ks, font="m", color=SLATE_T, ls=0.08, lh=1.0)
    T(s, x + 20, y + 38, w - 40, 38, val, size=vs, font="b", weight=500, color=INK, lh=1.1)
