"""Chữ ký email + phong bì DL + TrimBox/BleedBox cho PDF danh thiếp."""
import pathlib,subprocess,fitz
root=pathlib.Path(__file__).resolve().parent.parent
RN=str(root/"../../_tools/render.py")
def rd(src,out,size=None,scale=None):
    c=["python3",RN,str(src),str(out)]
    if size: c+=["--size",size,"--scale",str(scale or 1)]
    subprocess.run(c,check=True,capture_output=True)
URL="https://[chờ: domain]/brand/email/logo-by-innvie-email.png"
PH="background:#FFD3C0"
def sig(lang):
    vi=lang=='vi'
    tag="Khai mở cách vận hành mới." if vi else "Open a new way to operate."
    L=dict(T="Điện thoại" if vi else "Phone",E="Email",W="Web",A="Địa chỉ" if vi else "Address")
    F="font-family:Arial,Helvetica,sans-serif;"
    ph=lambda t:f'<span style="{PH}">[{t}]</span>'
    def row(k,v): return f'<tr><td style="{F}font-size:12px;line-height:18px;color:#2F43DB;font-weight:bold;width:72px;padding:0;">{k}</td><td style="{F}font-size:12px;line-height:18px;color:#0E1442;padding:0;">{v}</td></tr>'
    # logo cao ~56 px, 1x ~ 22 px (logo-spec Mục 2): padding 22 px dưới logo, 12 px (0,5x) bên trái
    return f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><title>Email signature {lang}</title></head>
<body style="margin:0;padding:16px;background:#ffffff;">
<!-- Chữ ký email Invlogis ({lang}) · table-based · inline style · không dùng web font -->
<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="600" style="width:600px;max-width:600px;border-collapse:collapse;">
 <tr><td style="padding:0 0 4px 12px;{F}font-size:14px;line-height:20px;color:#0E1442;font-weight:bold;">{ph("chờ: Họ và tên")}</td></tr>
 <tr><td style="padding:0 0 10px 12px;{F}font-size:12px;line-height:18px;color:#4A5380;">{ph("chờ: Chức danh")}</td></tr>
 <tr><td style="padding:0 0 10px 0;border-top:2px solid #2F43DB;font-size:0;line-height:0;height:1px;">&nbsp;</td></tr>
 <tr><td style="padding:0 0 10px 12px;"><table role="presentation" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;">
   {row(L["T"],ph("chờ: số điện thoại"))}
   {row(L["E"],ph("chờ: email"))}
   {row(L["W"],ph("chờ: domain"))}
   {row(L["A"],ph("chờ: địa chỉ"))}
 </table></td></tr>
 <tr><td style="padding:12px 0 22px 12px;"><img src="{URL}" width="150" alt="Invlogis by innvie" style="display:block;border:0;width:150px;height:auto;"></td></tr>
 <tr><td style="padding:0 0 0 12px;{F}font-size:11px;line-height:16px;color:#4A5380;">{tag}</td></tr>
</table></body></html>'''
d=root/'email-signature'
for l in ('vi','en'):
    h=sig(l); (d/f'signature-{l}.html').write_text(h,encoding='utf-8')
    (d/'_p.html').write_text(h.replace(URL,'logo-by-innvie-email.png'),encoding='utf-8')
    rd(d/'_p.html',d/f'signature-{l}-preview.png','640x270',2)
(d/'_p.html').unlink()

# ---- envelope: trim 220x110, bleed 3 mm -> page 226x116
F="""@font-face{font-family:BVP;font-weight:400;src:url(../assets/fonts/BeVietnamPro-400.ttf)}"""
def env(bleed):
    W,H=(226,116) if bleed else (220,110); o=3 if bleed else 0
    return f'''<!doctype html><meta charset=utf-8><style>{F}@page{{size:{W}mm {H}mm;margin:0}}*{{margin:0;padding:0}}
body{{width:{W}mm;height:{H}mm;position:relative;overflow:hidden;font-family:BVP,Arial,sans-serif;color:#0E1442;background:#fff;-webkit-print-color-adjust:exact}}
.ph{{background:#FFD3C0}}.lg{{position:absolute;left:{14+o}mm;top:{12+o}mm;width:42mm}}
.rt{{position:absolute;left:{14+o}mm;top:{39+o}mm;font-size:7.5pt;line-height:1.45;color:#4A5380}}
.to{{position:absolute;left:{100+o}mm;top:{58+o}mm;font-size:11pt;line-height:1.6}}.to small{{display:block;font-size:8pt;color:#4A5380}}
.bar{{position:absolute;right:0;top:0;width:{3+o}mm;height:{H}mm;background:linear-gradient(180deg,#0E1442,#2F43DB 55%,#7B55FF)}}
</style><img class=lg src="../assets/logo/invlogis-by-innvie.png">
<div class=rt><span class=ph>[chờ: tên pháp nhân đầy đủ]</span><br><span class=ph>[chờ: địa chỉ]</span><br>MST <span class=ph>[chờ: MST]</span></div>
<div class=to><small>Kính gửi / To</small><span class=ph>[chờ: tên người nhận]</span><br><span class=ph>[chờ: đơn vị]</span><br><span class=ph>[chờ: địa chỉ người nhận]</span></div><div class=bar></div>'''
e=root/'envelope'
(e/'_e.html').write_text(env(True),encoding='utf-8'); rd(e/'_e.html',e/'_t.pdf')
(e/'_e.html').write_text(env(False),encoding='utf-8'); rd(e/'_e.html',e/'envelope-dl-preview.png','832x416',2)
(e/'_e.html').unlink()
def boxes(src,dst,trim,bleed):
    doc=fitz.open(src); mm=72/25.4
    for p in doc:
        r=lambda b:fitz.Rect(*[v*mm for v in b])
        p.set_trimbox(r(trim)); p.set_bleedbox(r(bleed))
    doc.save(dst); doc.close()
boxes(e/'_t.pdf',e/'envelope-dl.pdf',(3,3,223,113),(0,0,226,116)); (e/'_t.pdf').unlink()
c=root/'business-card'
boxes(c/'business-card-print.pdf',c/'_b.pdf',(11,11,101,66),(8,8,104,69)); (c/'_b.pdf').replace(c/'business-card-print.pdf')
