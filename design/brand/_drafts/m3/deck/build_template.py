#!/usr/bin/env python3
"""Dựng invlogis-template.pptx: bộ layout thương hiệu (8 layout) + 8 slide mẫu giải thích cách dùng.
   python3 build_template.py   (cần chạy build.py trước một lần để có assets/)"""
import re
from pptx import Presentation
from pptx.util import Emu
from pptx.opc.constants import RELATIONSHIP_TYPE as RT
from pptx.oxml import parse_xml
from lxml import etree
from lib import *

PX = 6350
NS = ('xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
      'xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" '
      'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"')
E = lambda v: int(round(v * PX))
BGP = lambda code: HERE / f"assets/bg/bg-{code}_1920x1080.jpg"
LG = lambda n: HERE / f"assets/logo/{n}.png"

class Ids:
    def __init__(self): self.n = 1
    def __call__(self): self.n += 1; return self.n

def ph(ids, name, typ, idx, x, y, w, h, font, wt, size, color, prompt, anchor="t", align="l", lh=1.2, ls=0, lvl2=False):
    fam = PPTX_FAMILY[(font, wt)]
    idxa = f' idx="{idx}"' if idx is not None else ""
    ta = f' type="{typ}"' if typ else ""
    fonts = f'<a:latin typeface="{fam}"/><a:ea typeface="{fam}"/><a:cs typeface="{fam}"/>'
    spc = f' spc="{int(ls * size * 0.5 * 100)}"' if ls else ""
    l2 = ""
    if lvl2:
        l2 = (f'<a:lvl2pPr marL="{E(40)}" indent="{-E(28)}"><a:lnSpc><a:spcPts val="{int(size*lh*0.5*100)}"/></a:lnSpc>'
              f'<a:spcBef><a:spcPts val="600"/></a:spcBef><a:buFont typeface="Be Vietnam Pro"/><a:buChar char="–"/>'
              f'<a:defRPr sz="{int(size*0.5*0.9*100)}"><a:solidFill><a:srgbClr val="{color.lstrip("#")}"/></a:solidFill>{fonts}</a:defRPr></a:lvl2pPr>')
    return parse_xml(f'''<p:sp {NS}><p:nvSpPr><p:cNvPr id="{ids()}" name="{name}"/><p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr><p:nvPr><p:ph{ta}{idxa}/></p:nvPr></p:nvSpPr>
<p:spPr><a:xfrm><a:off x="{E(x)}" y="{E(y)}"/><a:ext cx="{E(w)}" cy="{E(h)}"/></a:xfrm></p:spPr>
<p:txBody><a:bodyPr lIns="0" tIns="0" rIns="0" bIns="0" anchor="{anchor}"><a:normAutofit/></a:bodyPr>
<a:lstStyle><a:lvl1pPr marL="0" indent="0" algn="{align}"><a:lnSpc><a:spcPts val="{int(size*lh*0.5*100)}"/></a:lnSpc><a:spcBef><a:spcPts val="0"/></a:spcBef><a:buNone/>
<a:defRPr sz="{int(size*0.5*100)}" b="0"{spc}><a:solidFill><a:srgbClr val="{color.lstrip("#")}"/></a:solidFill>{fonts}</a:defRPr></a:lvl1pPr>{l2}</a:lstStyle>
<a:p><a:r><a:rPr lang="vi-VN"/><a:t>{prompt}</a:t></a:r></a:p></p:txBody></p:sp>''')

def rect(ids, name, x, y, w, h, fill, alpha=1.0, line=None, r=0):
    geom = "roundRect" if r else "rect"
    av = f'<a:avLst><a:gd name="adj" fmla="val {int(min(.5, r/min(w,h))*100000)}"/></a:avLst>' if r else "<a:avLst/>"
    a = f'<a:alpha val="{int(alpha*100000)}"/>' if alpha < 1 else ""
    ln = f'<a:ln w="{E(1.5)}"><a:solidFill><a:srgbClr val="{line.lstrip("#")}"><a:alpha val="45000"/></a:srgbClr></a:solidFill></a:ln>' if line else "<a:ln><a:noFill/></a:ln>"
    return parse_xml(f'''<p:sp {NS}><p:nvSpPr><p:cNvPr id="{ids()}" name="{name}"/><p:cNvSpPr/><p:nvPr userDrawn="1"/></p:nvSpPr>
<p:spPr><a:xfrm><a:off x="{E(x)}" y="{E(y)}"/><a:ext cx="{E(w)}" cy="{E(h)}"/></a:xfrm><a:prstGeom prst="{geom}">{av}</a:prstGeom>
<a:solidFill><a:srgbClr val="{fill.lstrip("#")}">{a}</a:srgbClr></a:solidFill>{ln}</p:spPr></p:sp>''')

def pic(ids, name, rid, x, y, w, h):
    return parse_xml(f'''<p:pic {NS}><p:nvPicPr><p:cNvPr id="{ids()}" name="{name}"/><p:cNvPicPr><a:picLocks noChangeAspect="1"/></p:cNvPicPr><p:nvPr userDrawn="1"/></p:nvPicPr>
<p:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></p:blipFill>
<p:spPr><a:xfrm><a:off x="{E(x)}" y="{E(y)}"/><a:ext cx="{E(w)}" cy="{E(h)}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></p:spPr></p:pic>''')

def set_bg(layout, path):
    _, rid = layout.part.get_or_add_image_part(str(path))
    cSld = layout._element.cSld
    for old in cSld.findall("{http://schemas.openxmlformats.org/presentationml/2006/main}bg"): cSld.remove(old)
    bg = parse_xml(f'<p:bg {NS}><p:bgPr><a:blipFill dpi="0" rotWithShape="1"><a:blip r:embed="{rid}"/><a:srcRect/><a:stretch><a:fillRect/></a:stretch></a:blipFill><a:effectLst/></p:bgPr></p:bg>')
    cSld.insert(0, bg)

def logo(layout, ids, name, x, y, h, ratio):
    _, rid = layout.part.get_or_add_image_part(str(LG(name)))
    return pic(ids, "Logo " + name, rid, x, y, h * ratio, h)

R_PRIMARY, R_BYINNVIE = 3.5617, 2.6856

def build():
    prs = Presentation(); prs.slide_width = Emu(12192000); prs.slide_height = Emu(6858000)
    # --- theme: phông + màu
    theme = prs.slide_master.part.part_related_by(RT.THEME)
    x = theme.blob.decode("utf8")
    x = re.sub(r'(<a:majorFont>\s*<a:latin typeface=")[^"]*', r'\1Lexend Light', x)
    x = re.sub(r'(<a:minorFont>\s*<a:latin typeface=")[^"]*', r'\1Be Vietnam Pro', x)
    for tag, col in [("dk1", INK), ("lt1", WHITE), ("dk2", NIGHT), ("lt2", PAPER), ("accent1", COBALT), ("accent2", PERI),
                     ("accent3", "#7B55FF"), ("accent4", "#E24C9A"), ("accent5", "#FF7A59"), ("accent6", SLATE), ("hlink", COBALT), ("folHlink", NAVY)]:
        x = re.sub(rf'(<a:{tag}>)\s*<a:(?:srgbClr|sysClr)[^>]*?/>\s*(</a:{tag}>)', rf'\1<a:srgbClr val="{col.lstrip("#")}"/>\2', x, flags=re.S)
    x = re.sub(r'<a:clrScheme name="[^"]*"', '<a:clrScheme name="Invlogis"', x)
    x = re.sub(r'<a:fontScheme name="[^"]*"', '<a:fontScheme name="Invlogis"', x)
    theme._blob = x.encode("utf8")
    prs.slide_master.background.fill.solid()
    from pptx.dml.color import RGBColor
    prs.slide_master.background.fill.fore_color.rgb = RGBColor.from_string(PAPER.lstrip("#"))

    L = list(prs.slide_layouts)
    for lay in L[10:]: prs.slide_layouts.remove(lay)
    L = list(prs.slide_layouts)[:10]
    for lay in L:
        for shp in list(lay.shapes): shp._element.getparent().remove(shp._element)

    def add(lay, *els):
        for e in els: lay.shapes._spTree.append(e)
    def mono_label(ids, n, c): return ph(ids, "Nhãn mục", "body", n, 120, 76, 1200, 36, "m", 400, 22, c, "[Số mục · Tên mục]", lh=1.0, ls=0.04)

    # 1 · Bìa
    lay = L[0]; lay._element.cSld.set("name", "1 Bìa"); ids = Ids(); set_bg(lay, BGP("n6-muc-cobalt"))
    add(lay, logo(lay, ids, "invlogis-by-innvie-reverse", 120, 96, 150, R_BYINNVIE),
        ph(ids, "Tiêu đề", "title", None, 120, 360, 1380, 330, "d", 300, 124, WHITE, "Tiêu đề bìa: khẩu hiệu hoặc tên buổi giới thiệu (tối đa 2 dòng)", lh=1.08),
        ph(ids, "Phụ đề", "body", 1, 120, 740, 1100, 130, "b", 400, 32, PERI_L, "Một câu nói rõ buổi này dành cho ai, về điều gì (tối đa 2 dòng)", lh=1.4),
        ph(ids, "Ngày và người trình bày", "body", 2, 120, 996, 1000, 28, "m", 400, 20, PERI_L, "[Ngày · người trình bày]", lh=1.0))
    # 2 · Ngăn mục
    lay = L[1]; lay._element.cSld.set("name", "2 Ngăn mục"); ids = Ids(); set_bg(lay, BGP("n3-chamtim"))
    add(lay, ph(ids, "Số mục", "body", 1, 120, 330, 600, 44, "m", 400, 28, PERI, "[02]", lh=1.0),
        ph(ids, "Tiêu đề", "title", None, 120, 400, 1500, 300, "d", 300, 96, WHITE, "Tên phần mới, 1–2 dòng", lh=1.1),
        ph(ids, "Mô tả ngắn", "body", 2, 120, 760, 1100, 120, "b", 400, 30, PERI_L, "Một câu dẫn vào phần này (không bắt buộc)", lh=1.45),
        logo(lay, ids, "invlogis-reverse", 120, 996, 36, R_PRIMARY))
    # 3 · Tiêu đề + nội dung
    lay = L[2]; lay._element.cSld.set("name", "3 Tiêu đề + nội dung"); ids = Ids(); set_bg(lay, BGP("n5-giay-lua"))
    add(lay, mono_label(ids, 1, NAVY),
        ph(ids, "Tiêu đề", "title", None, 120, 126, 1560, 150, "d", 300, 66, INK, "Tiêu đề nêu kết luận, không nêu chủ đề (tối đa 2 dòng)", lh=1.12),
        ph(ids, "Nội dung", "body", 2, 120, 330, 1680, 600, "b", 400, 28, INK, "Nội dung chính: câu ngắn, một ý một câu. Cấp 2 dùng gạch đầu dòng.", lh=1.45, lvl2=True),
        logo(lay, ids, "invlogis-primary", 120, 996, 36, R_PRIMARY))
    # 4 · Hai cột
    lay = L[3]; lay._element.cSld.set("name", "4 Hai cột"); ids = Ids(); set_bg(lay, BGP("n5-giay-lua"))
    add(lay, mono_label(ids, 1, NAVY),
        ph(ids, "Tiêu đề", "title", None, 120, 126, 1560, 150, "d", 300, 66, INK, "Tiêu đề so sánh hoặc hai mặt của một ý", lh=1.12),
        rect(ids, "Thẻ trái", 120, 330, 820, 600, WHITE, .88, INK, 28), rect(ids, "Thẻ phải", 980, 330, 820, 600, WHITE, .88, INK, 28),
        ph(ids, "Cột trái", "body", 2, 156, 366, 748, 528, "b", 400, 26, INK, "Cột trái: ví dụ trước / vấn đề / hiện trạng", lh=1.45, lvl2=True),
        ph(ids, "Cột phải", "body", 3, 1016, 366, 748, 528, "b", 400, 26, INK, "Cột phải: ví dụ sau / giải pháp / kết quả", lh=1.45, lvl2=True),
        logo(lay, ids, "invlogis-primary", 120, 996, 36, R_PRIMARY))
    # 5 · Số lớn
    lay = L[4]; lay._element.cSld.set("name", "5 Số lớn"); ids = Ids(); set_bg(lay, BGP("n2-cobalt"))
    add(lay, mono_label(ids, 1, WHITE),
        ph(ids, "Số lớn", "title", None, 112, 190, 980, 250, "d", 300, 210, WHITE, "~110.000", lh=1.05),
        ph(ids, "Đơn vị", "body", 2, 120, 440, 900, 80, "d", 300, 56, WHITE, "đơn vị của con số", lh=1.1),
        ph(ids, "Giải thích", "body", 3, 120, 540, 900, 160, "b", 400, 32, WHITE, "Một câu giải thích con số, kèm phạm vi và nguồn", lh=1.4),
        rect(ids, "Thẻ kính", 1100, 200, 700, 330, NIGHT, .6, PERI, 28),
        ph(ids, "Chú thích", "body", 4, 1140, 240, 620, 250, "d", 300, 34, WHITE, "Trích dẫn khách hoặc lưu ý đọc đúng con số", lh=1.35),
        logo(lay, ids, "invlogis-reverse", 120, 996, 36, R_PRIMARY))
    # 6 · Trích dẫn
    lay = L[5]; lay._element.cSld.set("name", "6 Trích dẫn"); ids = Ids(); set_bg(lay, BGP("n4-periwinkle"))
    add(lay, mono_label(ids, 1, NAVY),
        ph(ids, "Trích dẫn", "title", None, 120, 200, 1500, 480, "d", 300, 64, INK, "“Lời trích ngắn của khách, 1–3 câu.”", lh=1.25),
        ph(ids, "Nguồn trích", "body", 2, 120, 760, 1200, 80, "m", 400, 22, NAVY, "— Tên · chức vụ · doanh nghiệp (chỉ khi khách đồng ý; nếu không, ghi ẩn danh)", lh=1.4),
        logo(lay, ids, "invlogis-primary", 120, 996, 36, R_PRIMARY))
    # 7 · Sản phẩm trên thiết bị
    lay = L[6]; lay._element.cSld.set("name", "7 Sản phẩm trên thiết bị"); ids = Ids(); set_bg(lay, BGP("n2-cobalt"))
    add(lay, mono_label(ids, 1, WHITE),
        ph(ids, "Tiêu đề", "title", None, 120, 126, 1500, 100, "d", 300, 68, WHITE, "Tiêu đề nói điều người dùng làm được", lh=1.1),
        ph(ids, "Phụ đề", "body", 2, 120, 236, 1200, 50, "b", 400, 28, WHITE, "Một dòng mô tả màn hình", lh=1.3),
        rect(ids, "Khung laptop", 120, 320, 1100, 600, NIGHT, 1, None, 30), rect(ids, "Chân laptop", 100, 920, 1140, 16, PERI_L, 1, None, 8),
        rect(ids, "Màn laptop", 142, 342, 1056, 556, PAPER, 1, None, 14),
        rect(ids, "Khung điện thoại", 1380, 270, 340, 660, NIGHT, 1, None, 58), rect(ids, "Màn điện thoại", 1394, 284, 312, 632, PAPER, 1, None, 46),
        rect(ids, "Tai thỏ", 1496, 298, 108, 28, NIGHT, 1, None, 14),
        parse_xml(f'''<p:sp {NS}><p:nvSpPr><p:cNvPr id="{ids()}" name="Ảnh màn web"/><p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr><p:nvPr><p:ph type="pic" idx="13"/></p:nvPr></p:nvSpPr>
<p:spPr><a:xfrm><a:off x="{E(142)}" y="{E(342)}"/><a:ext cx="{E(1056)}" cy="{E(556)}"/></a:xfrm></p:spPr>
<p:txBody><a:bodyPr anchor="ctr"/><a:lstStyle><a:lvl1pPr algn="ctr"><a:buNone/><a:defRPr sz="1400"><a:solidFill><a:srgbClr val="4A5380"/></a:solidFill></a:defRPr></a:lvl1pPr></a:lstStyle><a:p><a:r><a:rPr lang="vi-VN"/><a:t>Chèn ảnh màn hình web (tỉ lệ 1056 x 556)</a:t></a:r></a:p></p:txBody></p:sp>'''),
        parse_xml(f'''<p:sp {NS}><p:nvSpPr><p:cNvPr id="{ids()}" name="Ảnh màn app"/><p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr><p:nvPr><p:ph type="pic" idx="14"/></p:nvPr></p:nvSpPr>
<p:spPr><a:xfrm><a:off x="{E(1394)}" y="{E(340)}"/><a:ext cx="{E(312)}" cy="{E(576)}"/></a:xfrm></p:spPr>
<p:txBody><a:bodyPr anchor="ctr"/><a:lstStyle><a:lvl1pPr algn="ctr"><a:buNone/><a:defRPr sz="1200"><a:solidFill><a:srgbClr val="4A5380"/></a:solidFill></a:defRPr></a:lvl1pPr></a:lstStyle><a:p><a:r><a:rPr lang="vi-VN"/><a:t>Chèn ảnh màn app (312 x 576)</a:t></a:r></a:p></p:txBody></p:sp>'''),
        logo(lay, ids, "invlogis-reverse", 120, 996, 36, R_PRIMARY))
    # 8 · Kết
    lay = L[7]; lay._element.cSld.set("name", "8 Kết"); ids = Ids(); set_bg(lay, BGP("n1-chamdem"))
    add(lay, mono_label(ids, 1, PERI),
        ph(ids, "Tiêu đề", "title", None, 120, 150, 1500, 260, "d", 300, 112, WHITE, "Lời kêu gọi hành động, 1–2 dòng", lh=1.08),
        ph(ids, "Bước tiếp theo", "body", 2, 120, 450, 1000, 150, "b", 400, 32, PERI_L, "Một việc cụ thể người xem làm tiếp theo", lh=1.42),
        ph(ids, "Liên hệ", "body", 3, 120, 720, 1500, 120, "d", 300, 30, WHITE, "Email · điện thoại · website", lh=1.4),
        logo(lay, ids, "invlogis-by-innvie-reverse", 120, 890, 110, R_BYINNVIE),
        ph(ids, "Chữ ký pháp nhân", "body", 4, 560, 940, 1240, 40, "m", 400, 20, PERI_L, "Invlogis là sản phẩm của [tên pháp nhân innvie] · [địa chỉ] · [MST]", align="r", lh=1.4))

    # 9 · Tiêu đề + nội dung, nền tối (cho trang nội dung trên nền chàm/cobalt)
    lay = L[8]; lay._element.cSld.set("name", "9 Tiêu đề + nội dung (nền tối)"); ids = Ids(); set_bg(lay, BGP("n1-chamdem"))
    add(lay, mono_label(ids, 1, PERI),
        ph(ids, "Tiêu đề", "title", None, 120, 126, 1560, 150, "d", 300, 66, WHITE, "Tiêu đề nêu kết luận, không nêu chủ đề (tối đa 2 dòng)", lh=1.12),
        ph(ids, "Nội dung", "body", 2, 120, 330, 1680, 600, "b", 400, 28, PERI_L, "Nội dung chính trên nền tối: câu ngắn, một ý một câu.", lh=1.45, lvl2=True),
        logo(lay, ids, "invlogis-reverse", 120, 996, 36, R_PRIMARY))
    L[9]._element.cSld.set("name", "10 Trống (không nền)")
    # --- slide mẫu
    S = list(prs.slide_layouts)
    def fill(sl, **kw):
        for idx, txt in kw.items():
            if idx == "title": sl.shapes.title.text = txt
            else: sl.placeholders[int(idx[1:])].text = txt
    sl = prs.slides.add_slide(S[0]); fill(sl, title="Bìa: khẩu hiệu hoặc tên buổi giới thiệu", p1="Phụ đề: một câu nói rõ buổi này dành cho ai. Lockup 'by innvie' chỉ ở bìa và trang cuối.", p2="[Ngày · người trình bày]")
    sl = prs.slides.add_slide(S[1]); fill(sl, title="Ngăn mục: tên phần mới", p1="[02]", p2="Dùng giữa các phần dài. Nền tím chàm, chữ trắng.")
    sl = prs.slides.add_slide(S[2]); fill(sl, title="Tiêu đề nêu kết luận, không nêu chủ đề", p1="[01 · Tên mục]", p2="Nội dung chính, câu ngắn.\nThêm ý phụ bằng cách bấm Tab để xuống cấp 2.")
    sl = prs.slides.add_slide(S[3]); fill(sl, title="Hai cột: so sánh trước và sau", p1="[03 · Tên mục]", p2="Cột trái: hiện trạng.\nMỗi cột tối đa 4 ý.", p3="Cột phải: kết quả.\nMỗi cột tối đa 4 ý.")
    sl = prs.slides.add_slide(S[4]); fill(sl, title="~110.000", p1="[07 · Tên mục]", p2="lô hàng mỗi năm", p3="Số lớn: một con số, kèm phạm vi và nguồn ngay dưới. Chỉ dùng số thật.", p4="Thẻ kính: trích dẫn khách hoặc lưu ý đọc đúng con số.")
    sl = prs.slides.add_slide(S[5]); fill(sl, title="“Lời trích ngắn của khách, 1–3 câu.”", p1="[Khách tham chiếu · ẩn danh]", p2="— Chỉ ghi tên khi khách đồng ý bằng văn bản.")
    sl = prs.slides.add_slide(S[6]); fill(sl, title="Sản phẩm trên thiết bị: nói điều người dùng làm được", p1="[04 · Sản phẩm]", p2="Bấm biểu tượng ảnh trong khung để chèn ảnh màn hình. Ghi 'Dữ liệu minh hoạ' nếu là số mẫu.")
    sl = prs.slides.add_slide(S[8]); fill(sl, title="Nền tối: dùng cho trang nội dung đậm", p1="[07 · Tên mục]", p2="Cùng cấu trúc layout 3, chữ trắng trên nền chàm.")
    sl = prs.slides.add_slide(S[7]); fill(sl, title="Kết: một lời kêu gọi", p1="[13 · Bước tiếp theo]", p2="Một việc cụ thể người xem làm tiếp theo.", p3="[email] · [điện thoại] · [website]", p4="Invlogis là sản phẩm của [tên pháp nhân innvie] · [địa chỉ] · [MST]")
    prs.core_properties.title = "Invlogis · Mẫu slide"; prs.core_properties.author = "Invlogis"
    out = HERE / "invlogis-template.pptx"; prs.save(out); print(out)

if __name__ == "__main__": build()
