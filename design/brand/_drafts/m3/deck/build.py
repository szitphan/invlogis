#!/usr/bin/env python3
"""Dựng bộ deck bán hàng Invlogis: HTML + PPTX + PDF + previews.
   python3 build.py            dựng HTML + PPTX + kiểm tra (nhanh)
   python3 build.py --render   thêm PNG từng slide, contact-sheet, PDF (cần Chrome)
Nguồn nội dung: slides.py. Phần tử và đo chữ: lib.py. Mẫu slide: build_template.py."""
import sys, shutil, subprocess, html, re
from pathlib import Path
from PIL import Image
from lib import *
from slides import build_slides

OUT_HTML = HERE / "invlogis-sales-deck.html"
OUT_PPTX = HERE / "invlogis-sales-deck.pptx"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# ---------------------------------------------------------------- assets
def prep_assets():
    for d in ("fonts", "bg", "logo"): (ASSETS / d).mkdir(parents=True, exist_ok=True)
    for f in set(FONT_FILES.values()):
        shutil.copy(SRC / "fonts" / f, ASSETS / "fonts" / f)
    for code in ["n1-chamdem", "n2-cobalt", "n3-chamtim", "n4-periwinkle", "n5-giay-lua", "n6-muc-cobalt"]:
        shutil.copy(SRC / "backgrounds" / f"bg-{code}_1920x1080.jpg", ASSETS / "bg" / f"bg-{code}_1920x1080.jpg")
    shutil.copy(SRC / "backgrounds" / "doc-hero-n3_1920x1080.png", ASSETS / "bg" / "doc-hero-n3_1920x1080.png")
    for n in ["invlogis-primary", "invlogis-reverse", "invlogis-by-innvie-reverse", "invlogis-symbol-reverse"]:
        svg = ASSETS / "logo" / f"{n}.svg"; shutil.copy(SRC / "logo" / f"{n}.svg", svg)
        png = ASSETS / "logo" / f"{n}.png"
        if not png.exists():  # PNG trong suốt cho PPTX (logo gốc vẫn là SVG vector)
            vb = list(map(float, re.search(r'viewBox="([^"]+)"', svg.read_text()).group(1).split()))
            h = 400; w = round(h * vb[2] / vb[3])
            subprocess.run([sys.executable, str(TOOLS / "render.py"), str(svg), str(png), "--size", f"{w}x{h}"], check=True, capture_output=True)

# ---------------------------------------------------------------- HTML
def rgba(c, a):
    r, g, b = hex2rgb(c); return f"rgba({r},{g},{b},{a:g})"

def run_html(txt):
    if isinstance(txt, tuple):
        t, o = txt; st = []
        if "color" in o: st.append(f"color:{o['color']}")
        if "weight" in o: st.append(f"font-weight:{o['weight']}")
        if "font" in o: st.append(f"font-family:'{CSS_FAMILY[o['font']]}'")
        return f'<span style="{";".join(st)}">{html.escape(t)}</span>'
    return html.escape(txt)

def el_html(e):
    if e["t"] == "rect":
        st = [f"left:{e['x']:g}px", f"top:{e['y']:g}px", f"width:{e['w']:g}px", f"height:{e['h']:g}px"]
        if e["grad"]:
            ang, stops = e["grad"]
            st.append("background:linear-gradient(%gdeg,%s)" % (ang, ",".join(f"{rgba(c, a)} {p*100:g}%" for p, c, a in stops)))
        elif e["fill"]:
            st.append(f"background:{rgba(e['fill'], e['a'])}")
        if e["line"]: st.append(f"border:{e['lw']:g}px solid {rgba(e['line'], e['la'])}")
        if e["r"]: st.append(f"border-radius:{e['r']:g}px")
        if e["blur"]: st.append(f"backdrop-filter:blur({e['blur']}px);-webkit-backdrop-filter:blur({e['blur']}px)")
        return f'<div class="e" style="{";".join(st)}"></div>'
    if e["t"] == "img":
        return f'<img class="e" src="{e["path"]}" alt="" style="left:{e["x"]:g}px;top:{e["y"]:g}px;width:{e["w"]:g}px;height:{e["h"]:g}px">'
    ps = []
    for p in e["paras"]:
        runs = p if isinstance(p, list) else [p]
        ps.append('<p style="margin:0 0 %gpx">%s</p>' % (e["gap"], "".join(run_html(r) for r in runs)))
    jc = {"t": "flex-start", "m": "center", "b": "flex-end"}[e["anchor"]]
    al = {"l": "left", "c": "center", "r": "right"}[e["align"]]
    st = [f"left:{e['x']:g}px", f"top:{e['y']:g}px", f"width:{e['w']:g}px", f"height:{e['h']:g}px",
          f"font-family:'{CSS_FAMILY[e['font']]}',sans-serif", f"font-size:{e['size']:g}px", f"font-weight:{e['weight']}",
          f"color:{e['color']}", f"text-align:{al}", f"line-height:{e['lh']:g}", f"letter-spacing:{e['ls']:g}em", f"justify-content:{jc}"]
    return f'<div class="e t" style="{";".join(st)}">{"".join(ps)}</div>'

def build_html(slides):
    faces = "\n".join(
        "@font-face{font-family:'%s';font-weight:%d;src:url(assets/fonts/%s) format('truetype');font-display:block}" % (CSS_FAMILY[f], w, fn)
        for (f, w), fn in FONT_FILES.items())
    secs = []
    for i, s in enumerate(slides, 1):
        body = "\n".join(el_html(e) for e in s.els)
        secs.append(f'<section class="slide" id="s{i}" data-name="{html.escape(s.name)}" style="background-image:url({s.bg})">\n{body}\n</section>')
    nl = "\n"
    doc = f"""<!doctype html>
<html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Invlogis · Bản giới thiệu</title>
<style>
{faces}
*{{box-sizing:border-box}}
html,body{{margin:0;height:100%;background:#05071a;overflow:hidden}}
#stage{{position:absolute;left:0;top:0;width:1920px;height:1080px;transform-origin:0 0}}
.slide{{position:absolute;left:0;top:0;width:1920px;height:1080px;overflow:hidden;background-size:cover;background-position:center;background-color:{NIGHT};display:none;-webkit-font-smoothing:antialiased}}
.slide.on{{display:block}}
.e{{position:absolute}}
.t{{display:flex;flex-direction:column}}
img.e{{display:block}}
#bar{{position:fixed;left:0;bottom:0;height:3px;background:{COBALT};transition:width .25s;z-index:5}}
#hint{{position:fixed;right:14px;bottom:10px;font:12px 'JetBrains Mono',monospace;color:#97A6FF;opacity:0;transition:opacity .4s;z-index:5}}
body:hover #hint{{opacity:.7}}
body.single #bar,body.single #hint{{display:none}}
@page{{size:1920px 1080px;margin:0}}
@media print{{
 html,body{{overflow:visible;height:auto;background:none}}
 #stage{{position:static;transform:none!important;width:1920px;height:auto}}
 .slide{{display:block!important;position:relative;break-after:page;page-break-after:always;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
 #bar,#hint{{display:none}}
}}
</style></head><body>
<div id="stage">
{nl.join(secs)}
</div>
<div id="bar"></div><div id="hint">← → · Space · Home/End · F toàn màn hình</div>
<script>
(function(){{
 var S=[].slice.call(document.querySelectorAll('.slide')),st=document.getElementById('stage'),cur=0;
 var single=new URLSearchParams(location.search).get('s');
 function fit(){{var k=Math.min(innerWidth/1920,innerHeight/1080);
  st.style.transform=single?'none':'translate('+((innerWidth-1920*k)/2)+'px,'+((innerHeight-1080*k)/2)+'px) scale('+k+')';}}
 function go(n){{cur=Math.max(0,Math.min(S.length-1,n));S.forEach(function(s,i){{s.classList.toggle('on',i===cur)}});
  document.getElementById('bar').style.width=((cur+1)/S.length*100)+'%';
  if(!single)try{{history.replaceState(null,'','#'+(cur+1))}}catch(e){{}}}}
 if(single){{document.body.classList.add('single');go(+single-1)}}else{{go((parseInt(location.hash.slice(1))||1)-1)}}
 addEventListener('resize',fit);fit();
 addEventListener('keydown',function(e){{var k=e.key;
  if(k==='ArrowRight'||k===' '||k==='PageDown'||k==='Enter')go(cur+1);
  else if(k==='ArrowLeft'||k==='PageUp'||k==='Backspace')go(cur-1);
  else if(k==='Home')go(0);else if(k==='End')go(S.length-1);
  else if(k==='f'||k==='F'){{document.fullscreenElement?document.exitFullscreen():document.documentElement.requestFullscreen()}}
  if([' ','ArrowRight','ArrowLeft','PageDown','PageUp'].indexOf(k)>=0)e.preventDefault();}});
 document.addEventListener('click',function(e){{if(single)return;go(e.clientX>innerWidth*0.3?cur+1:cur-1)}});
 var tx=null;addEventListener('touchstart',function(e){{tx=e.touches[0].clientX}});
 addEventListener('touchend',function(e){{if(tx===null)return;var d=e.changedTouches[0].clientX-tx;if(Math.abs(d)>40){{go(cur+(d<0?1:-1));}}tx=null}});
}})();
</script></body></html>"""
    OUT_HTML.write_text(doc, encoding="utf-8")

# ---------------------------------------------------------------- PPTX
from pptx import Presentation
from pptx.util import Emu, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR, MSO_AUTO_SIZE
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn
from lxml import etree

PX = 6350  # EMU mỗi px (1920px = 13,333in)
A = "http://schemas.openxmlformats.org/drawingml/2006/main"
def px(v): return Emu(int(round(v * PX)))

def set_alpha(color_el, a):
    if a < 1:
        al = etree.SubElement(color_el, qn("a:alpha")); al.set("val", str(int(a * 100000)))

def strip_style(shape):
    st = shape._element.find(qn("p:style"))
    if st is not None: shape._element.remove(st)

def grad_xml(ang_css, stops):
    ang = int(((ang_css - 90) % 360) * 60000)
    gs = "".join(f'<a:gs pos="{int(p*100000)}"><a:srgbClr val="{c.lstrip("#")}"><a:alpha val="{int(a*100000)}"/></a:srgbClr></a:gs>' for p, c, a in stops)
    return etree.fromstring(f'<a:gradFill xmlns:a="{A}" rotWithShape="1"><a:gsLst>{gs}</a:gsLst><a:lin ang="{ang}" scaled="0"/></a:gradFill>')

def pptx_rect(sl, e):
    shp = sl.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE if e["r"] else MSO_SHAPE.RECTANGLE, px(e["x"]), px(e["y"]), px(e["w"]), px(e["h"]))
    strip_style(shp)
    if e["r"]: shp.adjustments[0] = min(0.5, e["r"] / min(e["w"], e["h"]))
    spPr = shp._element.spPr
    if e["grad"]:
        spPr.find(qn("a:prstGeom")).addnext(grad_xml(*e["grad"]))
    elif e["fill"]:
        shp.fill.solid(); shp.fill.fore_color.rgb = RGBColor.from_string(e["fill"].lstrip("#"))
        set_alpha(spPr.find(qn("a:solidFill")).find(qn("a:srgbClr")), e["a"])
    else:
        shp.fill.background()
    if e["line"]:
        shp.line.color.rgb = RGBColor.from_string(e["line"].lstrip("#")); shp.line.width = Emu(int(e["lw"] * PX))
        set_alpha(spPr.find(qn("a:ln")).find(qn("a:solidFill")).find(qn("a:srgbClr")), e["la"])
    else:
        shp.line.fill.background()
    return shp

def set_fonts(rPr, name):
    for tag in ("a:latin", "a:ea", "a:cs"):
        for old in rPr.findall(qn(tag)): rPr.remove(old)
        el = etree.SubElement(rPr, qn(tag)); el.set("typeface", name)

def pptx_text(sl, e):
    tb = sl.shapes.add_textbox(px(e["x"]), px(e["y"]), px(e["w"]), px(e["h"]))
    fill_tf(tb.text_frame, e)
    return tb

def fill_tf(tf, e):
    tf.word_wrap = True; tf.auto_size = MSO_AUTO_SIZE.NONE
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = {"t": MSO_ANCHOR.TOP, "m": MSO_ANCHOR.MIDDLE, "b": MSO_ANCHOR.BOTTOM}[e["anchor"]]
    for i, para in enumerate(e["paras"]):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = {"l": PP_ALIGN.LEFT, "c": PP_ALIGN.CENTER, "r": PP_ALIGN.RIGHT}[e["align"]]
        p.line_spacing = Pt(e["size"] * e["lh"] * 0.5)
        p.space_after = Pt(e["gap"] * 0.5); p.space_before = Pt(0)
        for r_ in (para if isinstance(para, list) else [para]):
            txt, o = (r_ if isinstance(r_, tuple) else (r_, {}))
            f, w, c = o.get("font", e["font"]), o.get("weight", e["weight"]), o.get("color", e["color"])
            if (f, w) not in PPTX_FAMILY: w = 400
            run = p.add_run(); run.text = txt
            run.font.size = Pt(e["size"] * 0.5); run.font.color.rgb = RGBColor.from_string(c.lstrip("#")); run.font.bold = False
            rPr = run._r.get_or_add_rPr(); set_fonts(rPr, PPTX_FAMILY[(f, w)])
            if e["ls"]: rPr.set("spc", str(int(e["ls"] * e["size"] * 0.5 * 100)))

# layout theo tên trong invlogis-template.pptx; số = chỉ số layout
LAY = {"cover": 0, "divider": 1, "content": 2, "two": 3, "big": 4, "quote": 5, "device": 6, "closing": 7, "dark": 8, "blank": 9}
# slide -> (layout, {placeholder: tiền tố văn bản của phần tử}); "title" = tiêu đề, số = idx placeholder
PHMAP = {
 1: ("cover", {"title": "Khai mở", 1: "Nền tảng vận hành", 2: "Bản giới thiệu"}),
 2: ("content", {1: "[02", "title": "Mỗi lô hàng", 2: "Cùng một số container xuất"}),
 3: ("divider", {1: "[03", "title": "Chứng từ vào", 2: "Invlogis dùng AI"}),
 4: ("content", {1: "[04", "title": "Ba bước", 2: "Bạn duyệt trước"}),
 5: ("content", {1: "[05", "title": "Một lô, từ", 2: "Cùng một số container đi"}),
 6: ("device", {1: "[06", "title": "Một hồ sơ lô hàng, trên", 2: "Văn phòng"}),
 7: ("dark", {1: "[07", "title": "AI nằm", 2: "Các module"}),
 8: ("content", {1: "[08", "title": "Làm cho"}),
 9: ("big", {1: "[09", "title": "~110.000", 2: "lô hàng mỗi năm", 3: "Nền tảng vận hành đã chạy", 4: "[chờ: nhận xét"}),
 10: ("content", {1: "[10", "title": "Một lõi", 2: "Khách thứ hai"}),
 11: ("dark", {1: "[11", "title": "Ba điều"}),
 12: ("content", {1: "[12", "title": "Những điều bạn", 2: "Phần chưa chốt"}),
 13: ("dark", {1: "[13", "title": "Từ vận hành"}),
 14: ("dark", {1: "[14", "title": "Thử trên", 2: "Bạn mang vài"}),
 15: ("quote", {1: "[15", "title": "innvie =", 2: "Invlogis, sản phẩm của innvie"}),
 16: ("closing", {1: "[16", "title": "Khai mở cách", 2: "Mang đến vài", 4: "Invlogis là sản phẩm"}),
}
# khối do layout vẽ sẵn (bỏ khỏi slide để không trùng): khung thiết bị (slide 6), thẻ kính số lớn (slide 9)
LAYOUT_RECTS = {6: {(120, 320, 1100, 600), (100, 920, 1140, 16), (142, 342, 1056, 556), (1380, 270, 340, 660), (1394, 284, 312, 632), (1496, 298, 108, 28)},
                9: {(1100, 200, 700, 330)}}

def set_slide_bg(sl, path):
    _, rid = sl.part.get_or_add_image_part(str(HERE / path))
    NSS = ('xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" '
           'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"')
    bg = etree.fromstring(f'<p:bg {NSS}><p:bgPr><a:blipFill dpi="0" rotWithShape="1"><a:blip r:embed="{rid}"/><a:srcRect/><a:stretch><a:fillRect/></a:stretch></a:blipFill><a:effectLst/></p:bgPr></p:bg>')
    sl._element.cSld.insert(0, bg)

def build_pptx(slides):
    import build_template; build_template.build()
    prs = Presentation(str(HERE / "invlogis-template.pptx"))   # layout của mẫu: đổi layout trong PowerPoint dùng được
    ids = prs.slides._sldIdLst
    for sid in list(ids):
        prs.part.drop_rel(sid.rId); ids.remove(sid)
    layouts = list(prs.slide_layouts)
    report = []
    for n, s in enumerate(slides, 1):
        lname, pm = PHMAP[n]
        sl = prs.slides.add_slide(layouts[LAY[lname]])
        set_slide_bg(sl, s.bg)
        used = set(); phs = {}
        for key, prefix in pm.items():
            for e in s.els:
                if e["t"] == "text" and id(e) not in used and ptxt(e["paras"][0]).startswith(prefix):
                    used.add(id(e)); phs[key] = e; break
            else: raise SystemExit(f"slide {n}: không thấy phần tử '{prefix}'")
        filled = []
        for key, e in phs.items():
            shp = sl.shapes.title if key == "title" else sl.placeholders[key]
            shp.left, shp.top, shp.width, shp.height = px(e["x"]), px(e["y"]), px(e["w"]), px(e["h"])
            fill_tf(shp.text_frame, e); filled.append(key)
        for shp in list(sl.placeholders):   # bỏ ô giữ chỗ không dùng
            k = "title" if shp.placeholder_format.type is not None and shp.placeholder_format.idx == 0 else shp.placeholder_format.idx
            if k not in phs: shp._element.getparent().remove(shp._element)
        for e in s.els:
            if id(e) in used: continue
            if e["t"] == "img" and "logo" in e["path"]: continue          # logo do layout cung cấp
            if e["t"] == "rect" and (round(e["x"]), round(e["y"]), round(e["w"]), round(e["h"])) in LAYOUT_RECTS.get(n, ()): continue
            if e["t"] == "rect": pptx_rect(sl, e)
            elif e["t"] == "img": sl.shapes.add_picture(str(HERE / e["path"]), px(e["x"]), px(e["y"]), px(e["w"]), px(e["h"]))
            else: pptx_text(sl, e)
        if s.notes: sl.notes_slide.notes_text_frame.text = s.notes
        report.append((n, sl.slide_layout.name, filled))
    prs.core_properties.title = "Invlogis · Bản giới thiệu"; prs.core_properties.author = "Invlogis"
    prs.save(OUT_PPTX)
    return report

# ---------------------------------------------------------------- QA
def lum(c):
    c = [x / 255 for x in c]; c = [x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]
def ratio(a, b):
    l1, l2 = sorted([lum(a), lum(b)], reverse=True); return (l1 + .05) / (l2 + .05)
def ptxt(p): return "".join(r if isinstance(r, str) else r[0] for r in (p if isinstance(p, list) else [p]))

def qa(slides):
    """Tràn hộp chữ (đo bằng phông thật) + tương phản chữ trên nền thật (ảnh nền + thẻ chồng)."""
    warns, rep = [], []
    for n, s in enumerate(slides, 1):
        bgim = Image.open(HERE / s.bg).convert("RGB").resize((W, H))
        for idx, e in enumerate(s.els):
            if e["t"] != "text": continue
            lines = sum(len(wrap(ptxt(p), e["font"], e["weight"], e["size"], e["w"] - 2, e["ls"])) for p in e["paras"])
            need = lines * e["size"] * e["lh"] + (len(e["paras"]) - 1) * e["gap"]
            if need > e["h"] + 2:
                warns.append(f"[tràn] slide {n}: '{ptxt(e['paras'][0])[:40]}' cần {need:.0f}px > hộp {e['h']:.0f}px")
            maxw = max(text_w(ptxt(p), e["font"], e["weight"], e["size"]) for p in e["paras"])
            tw = min(e["w"], maxw); cx0 = e["x"]
            if e["align"] == "r": cx0 = e["x"] + e["w"] - tw
            elif e["align"] == "c": cx0 = e["x"] + (e["w"] - tw) / 2
            y0 = e["y"] if e["anchor"] == "t" else e["y"] + (e["h"] - need) / (2 if e["anchor"] == "m" else 1)
            crop = bgim.crop((int(max(0, cx0)), int(max(0, y0)), int(min(W, cx0 + tw)), int(min(H, max(y0 + 4, y0 + need))))).resize((24, 8))
            ccx, ccy = cx0 + tw / 2, y0 + need / 2
            backs = [r for r in s.els[:idx] if r["t"] == "rect" and r["fill"] and not r["grad"] and r["a"] >= .5 and r["h"] > 6
                     and r["x"] <= ccx <= r["x"] + r["w"] and r["y"] <= ccy <= r["y"] + r["h"]]
            worst = 99
            for col in crop.getdata():
                for r in backs:
                    rc = hex2rgb(r["fill"]); col = tuple(rc[i] * r["a"] + col[i] * (1 - r["a"]) for i in range(3))
                worst = min(worst, ratio(hex2rgb(e["color"]), col))
            big = e["size"] >= 36
            rep.append((n, ptxt(e["paras"][0])[:30], e["size"], round(worst, 2)))
            if worst < (3.0 if big else 4.5):
                warns.append(f"[tương phản] slide {n}: '{ptxt(e['paras'][0])[:40]}' {worst:.2f}:1 < {3.0 if big else 4.5}")
    return warns, rep

# ---------------------------------------------------------------- render
def shot(url, out, w=1920, h=1080):
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--allow-file-access-from-files",
                    "--force-device-scale-factor=1", f"--window-size={w},{h+200}", f"--screenshot={out}", url], check=True, capture_output=True)
    Image.open(out).crop((0, 0, w, h)).convert("RGB").save(out)

def render(n):
    (HERE / "previews").mkdir(exist_ok=True)
    for i in range(1, n + 1):
        shot(OUT_HTML.as_uri() + f"?s={i}", HERE / "previews" / f"slide-{i:02d}.png")
    cols, tw, th, g = 4, 480, 270, 16
    rows = (n + cols - 1) // cols
    sheet = Image.new("RGB", (cols * tw + (cols + 1) * g, rows * th + (rows + 1) * g), "#05071a")
    for i in range(n):
        im = Image.open(HERE / "previews" / f"slide-{i+1:02d}.png").resize((tw, th), Image.LANCZOS)
        sheet.paste(im, (g + (i % cols) * (tw + g), g + (i // cols) * (th + g)))
    sheet.save(HERE / "previews" / "contact-sheet.png")
    subprocess.run([sys.executable, str(TOOLS / "render.py"), str(OUT_HTML), str(HERE / "invlogis-sales-deck.pdf")], check=True, capture_output=True)

if __name__ == "__main__":
    prep_assets()
    slides = build_slides()
    build_html(slides); build_pptx(slides)
    warns, rep = qa(slides)
    for w in warns: print(w)
    print(f"{len(slides)} slide · {len(rep)} hộp chữ · tương phản thấp nhất {min(r[3] for r in rep)}:1 · {len(warns)} cảnh báo")
    if "--render" in sys.argv: render(len(slides)); print("đã render previews + PDF")
