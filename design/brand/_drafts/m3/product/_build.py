#!/usr/bin/env python3
"""Dựng HTML các điểm chạm sản phẩm (m3/product). Chạy: python3 _build.py"""
import pathlib, re
R = pathlib.Path(__file__).parent
RENDER = R / "../../_tools/render.py"

FONTS = """
@font-face{font-family:Lexend;font-weight:300;src:url(assets/fonts/Lexend-300.ttf)}
@font-face{font-family:Lexend;font-weight:400;src:url(assets/fonts/Lexend-400.ttf)}
@font-face{font-family:Lexend;font-weight:600;src:url(assets/fonts/Lexend-600.ttf)}
@font-face{font-family:"Be Vietnam Pro";font-weight:400;src:url(assets/fonts/BeVietnamPro-400.ttf)}
@font-face{font-family:"Be Vietnam Pro";font-weight:500;src:url(assets/fonts/BeVietnamPro-500.ttf)}
@font-face{font-family:"Be Vietnam Pro";font-weight:600;src:url(assets/fonts/BeVietnamPro-600.ttf)}
"""
# Token sản phẩm (design-tokens.css, chỉ đọc) — giữ nguyên, không dùng màu thương hiệu trong UI
PROD = """
:root{--accent:#262626;--on-accent:#fff;--surface:#fff;--body:#f1f1f1;--tx:#171717;--tx2:#737373;
--bd:#d4d4d4;--bd-d:rgba(0,0,0,.08);--err:#a50c25;
--ink:#0E1442;--cobalt:#2F43DB;--paper:#FAF8F4}
*{box-sizing:border-box}html,body{margin:0}
body{font-family:Inter,"Be Vietnam Pro",system-ui,sans-serif;color:var(--tx);font-size:14px;line-height:1.45;-webkit-font-smoothing:antialiased}
.lex{font-family:Lexend,"Be Vietnam Pro",sans-serif}
label{display:block;font-size:13px;font-weight:500;margin-bottom:6px}
.in{height:40px;border:1px solid var(--bd);border-radius:8px;padding:0 12px;display:flex;align-items:center;font-size:14px;color:var(--tx);background:#fff}
.in.ph{color:var(--tx2)}
.in.focus{border-color:var(--accent);box-shadow:0 0 0 3px rgba(38,38,38,.18)}
.btn{height:40px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-weight:500;font-size:14px;gap:8px}
.btn.pri{background:var(--accent);color:var(--on-accent)}
.btn.out{border:1px solid var(--bd);background:#fff;color:var(--tx)}
a,.lnk{color:var(--accent);text-decoration:underline;text-underline-offset:2px;font-weight:500}
.sep{display:flex;align-items:center;gap:12px;color:var(--tx2);font-size:12px;margin:18px 0}
.sep:before,.sep:after{content:"";flex:1;height:1px;background:var(--bd)}
.tile{border-radius:10px;background:#0F6B5C;color:#fff;display:grid;place-items:center;font-weight:600}
.tenant{display:flex;align-items:center;gap:10px}
.tenant b{font-size:15px;font-weight:600;letter-spacing:-.01em}
"""

def page(title, w, h, css, body):
    return f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><style>{FONTS}{PROD}html,body{{width:{w}px;height:{h}px;overflow:hidden}}{css}</style></head><body>{body}</body></html>"""

def write(name, w, h, title, css, body):
    (R / name).write_text(page(title, w, h, css, body), encoding="utf-8")

TENANT_LOGO = '<div class="tenant"><div class="tile" style="width:40px;height:40px;font-size:18px">M</div><b>Công ty Vận tải Mẫu</b></div>'

# ---------- 1. Đăng nhập ----------
def form(tenant, mobile):
    logo = f'<div style="margin-bottom:{24 if mobile else 32}px">{TENANT_LOGO}</div>' if tenant else ""
    return f"""{logo}
<h1 style="font-size:{22 if mobile else 24}px;line-height:1.25;margin:0 0 6px;font-weight:600;letter-spacing:-.015em">Đăng nhập</h1>
<p style="margin:0 0 24px;color:var(--tx2)">{'Chào mừng trở lại. Nhập thông tin tài khoản của bạn.'}</p>
<div style="margin-bottom:16px"><label>Email</label><div class="in focus">an.nguyen@congtymau.vn</div></div>
<div style="margin-bottom:8px"><label>Mật khẩu</label><div class="in ph">••••••••••</div></div>
<div style="text-align:right;margin-bottom:20px"><a class="lnk" style="font-size:13px">Quên mật khẩu?</a></div>
<div class="btn pri">Đăng nhập</div>
<div class="sep">hoặc tiếp tục với</div>
<div class="btn out">Đăng nhập một lần (SSO)</div>"""

def login(tenant, mobile):
    name = f"login-web-{'tenant' if tenant else 'default'}-{'mobile' if mobile else 'desktop'}.html"
    w, h = (390, 844) if mobile else (1440, 900)
    if not mobile:
        brand_logo = ('<div style="font-size:13px;letter-spacing:.08em;text-transform:uppercase;opacity:.85">Vận hành trên</div>'
                      '<img src="assets/invlogis-reverse.svg" style="height:44px;display:block;margin-top:10px">') if tenant else \
                     '<img src="assets/invlogis-reverse.svg" style="height:52px;display:block">'
        line = "Khai mở cách<br>vận hành mới."
        css = f"""body{{display:flex;background:#fff}}
.panel{{width:760px;height:900px;position:relative;color:#fff;background:#0E1442 url(assets/bg-n3-chamtim_1920x1080.jpg) center/cover;padding:56px 64px;display:flex;flex-direction:column;justify-content:space-between}}
.panel h2{{font-family:Lexend;font-weight:300;font-size:56px;line-height:1.1;margin:0;letter-spacing:-.01em;max-width:520px}}
.panel small{{font-size:13px;opacity:.85}}
.side{{flex:1;display:flex;flex-direction:column;justify-content:center;align-items:center;position:relative}}
.fw{{width:380px}}
.foot{{position:absolute;bottom:32px;left:0;right:0;text-align:center;font-size:12px;color:var(--tx2)}}"""
        body = f"""<div class="panel"><div>{brand_logo}</div><h2>{line}</h2><small>© 2026 innvie · Điều khoản · Bảo mật</small></div>
<div class="side"><div class="fw">{form(tenant, False)}</div>
<div class="foot">Cần hỗ trợ? <span class="lnk">Liên hệ quản trị viên</span></div></div>"""
    else:
        hdr_logo = ('<div style="font-size:11px;letter-spacing:.08em;text-transform:uppercase;opacity:.9">Vận hành trên</div><img src="assets/invlogis-reverse.svg" style="height:28px;display:block;margin-top:6px">'
                    ) if tenant else '<img src="assets/invlogis-reverse.svg" style="height:40px;display:block">'
        hh = 220 if tenant else 280
        css = f"""body{{position:relative;background:linear-gradient(rgba(11,16,51,.42),rgba(11,16,51,.42)),#0E1442 url(assets/bg-n1-chamdem_1080x1350.jpg) top/cover}}
.hd{{height:{hh}px;padding:56px 28px 0;color:#fff}}
.hd h2{{font-family:Lexend;font-weight:300;font-size:30px;line-height:1.15;margin:{'0' if tenant else '28px'} 0 0}}
.sheet{{position:absolute;top:{hh-24}px;left:0;right:0;bottom:0;background:#fff;border-radius:24px 24px 0 0;padding:32px 24px 0}}
.mf{{position:absolute;bottom:24px;left:0;right:0;text-align:center;font-size:12px;color:var(--tx2)}}"""
        body = f"""<div class="hd">{hdr_logo}{'' if tenant else '<h2>Khai mở cách<br>vận hành mới.</h2>'}</div>
<div class="sheet">{form(tenant, True)}<div class="mf">© 2026 innvie · Điều khoản · Bảo mật</div></div>"""
    write(name, w, h, "Đăng nhập" + (" (khách)" if tenant else ""), css, body)
    return name, w, h

# ---------- 2. Splash mobile ----------
def splash(ver):
    name = f"splash-mobile-{ver}.html"
    tag = ("PHIÊN BẢN A · GIỮ NGUYÊN DEC-037" if ver == "a" else "PHIÊN BẢN B · ĐỀ XUẤT (CHỜ FOUNDER DUYỆT)")
    if ver == "a":
        foot = '<div style="font-size:13px;color:var(--tx2)">Được phát triển bởi</div><img src="assets/innvie-logo.svg" style="height:26px;margin-top:8px;display:block">'
    else:
        foot = '<div style="font-size:13px;color:var(--tx2);margin-bottom:6px">Vận hành trên</div><img src="assets/invlogis-by-innvie.svg" style="height:72px;display:block">'
    css = f"""body{{background:#fff;position:relative}}
.c{{position:absolute;top:0;bottom:130px;left:0;right:0;display:grid;place-items:center}}
.f{{position:absolute;bottom:40px;left:0;right:0;display:flex;flex-direction:column;align-items:center}}
.tag{{position:absolute;top:14px;left:0;right:0;text-align:center;font:600 10px/1 Inter,'Be Vietnam Pro';letter-spacing:.08em;color:#a3a3a3}}"""
    body = f"""<div class="tag">{tag}</div>
<div class="c"><div class="tenant" style="gap:14px"><div class="tile" style="width:72px;height:72px;font-size:34px;border-radius:16px">M</div><b style="font-size:22px">Công ty<br>Vận tải Mẫu</b></div></div>
<div class="f">{foot}</div>"""
    write(name, 390, 844, "Splash mobile " + ver.upper(), css, body)
    return name, 390, 844

# ---------- 3. Icon app trong ngữ cảnh ----------
def app_icon():
    def tile(label, bg, glyph=""):
        return f'<div class="ap"><div class="ic" style="background:{bg}">{glyph}</div><span>{label}</span></div>'
    gl = lambda p: f'<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{p}</svg>'
    fill = [("Lịch", "#6b7280", gl('<rect x="4" y="5" width="16" height="15" rx="2"/><path d="M4 10h16M9 3v4M15 3v4"/>')),
            ("Ghi chú", "#9a8a4f", gl('<path d="M6 4h12v16H6z"/><path d="M9 9h6M9 13h6"/>')),
            ("Bản đồ", "#4f8a6b", gl('<path d="M12 21s7-6 7-11a7 7 0 0 0-14 0c0 5 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/>')),
            ("Thời tiết", "#4a78a8", gl('<circle cx="12" cy="12" r="4"/><path d="M12 3v2M12 19v2M3 12h2M19 12h2"/>')),
            ("Máy tính", "#555", gl('<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M8 7h8M8 12h2M14 12h2M8 16h2M14 16h2"/>')),
            ("Ảnh", "#a7678a", gl('<rect x="4" y="5" width="16" height="14" rx="2"/><circle cx="9" cy="10" r="1.5"/><path d="M4 17l5-4 4 3 3-2 4 3"/>')),
            ("Đồng hồ", "#3f3f46", gl('<circle cx="12" cy="12" r="8"/><path d="M12 8v4l3 2"/>'))]
    ios_icons = "".join(tile(l, c, g) for l, c, g in fill[:3]) + \
        '<div class="ap"><div class="ic" style="background:url(assets/app-icon-1024.png) center/cover"></div><span>Invlogis</span></div>' + \
        "".join(tile(l, c, g) for l, c, g in fill[3:7]) + tile("Ghi chú", "#9a8a4f", gl('<path d="M6 4h12v16H6z"/>')) + tile("Ảnh", "#a7678a", gl('<rect x="4" y="5" width="16" height="14" rx="2"/>'))
    and_icons = "".join(tile(l, c, g) for l, c, g in fill[:3]) + \
        '<div class="ap"><div class="ic and"><img src="assets/android-background-432.png"><img src="assets/android-foreground-432.png"></div><span>Invlogis</span></div>' + \
        "".join(tile(l, c, g) for l, c, g in fill[3:7])
    dock = lambda: "".join(f'<div class="ic" style="background:{c}">{g}</div>' for _, c, g in fill[4:7] + [fill[0]])
    css = """body{background:#e9e9ee;display:flex;gap:56px;padding:48px 60px;font-family:Inter,'Be Vietnam Pro',sans-serif}
.col{width:390px}.ttl{font:600 13px 'Be Vietnam Pro';letter-spacing:.06em;color:#555;margin-bottom:14px;text-transform:uppercase}
.ph{position:relative;width:390px;height:700px;border-radius:44px;overflow:hidden;background:url(assets/bg-n4-periwinkle_1920x1080.jpg) 30% center/cover;box-shadow:0 20px 50px rgba(14,20,66,.28);padding:56px 24px 0}
.sb{position:absolute;top:16px;left:34px;right:34px;display:flex;justify-content:space-between;color:#fff;font:600 14px Inter,'Be Vietnam Pro'}
.g{display:grid;grid-template-columns:repeat(4,60px);justify-content:space-between;row-gap:24px}
.ap{display:flex;flex-direction:column;align-items:center;gap:6px}.ap span{color:#fff;font-size:11px;text-shadow:0 1px 2px rgba(0,0,0,.45)}
.ic{width:60px;height:60px;border-radius:13.5px;display:grid;place-items:center;overflow:hidden;position:relative}
.ph.an .ic{border-radius:50%}
.ic.and{background:none;overflow:hidden}
.ic.and img{position:absolute;width:90px;height:90px;left:-15px;top:-15px}
.dock{position:absolute;left:14px;right:14px;bottom:16px;height:84px;border-radius:30px;background:rgba(255,255,255,.28);display:flex;justify-content:space-around;align-items:center;backdrop-filter:blur(12px)}
.note{margin-top:14px;font-size:12px;color:#555;line-height:1.5}
.sz{width:230px;padding-top:36px}.sz .r{display:flex;align-items:flex-end;gap:14px;margin-bottom:18px;font-size:11px;color:#555}
.sz img{display:block;background:#fff}"""
    body = f"""<div class="col"><div class="ttl">iOS · 60 pt (3x)</div><div class="ph"><div class="sb"><span>9:41</span><span>5G ▮</span></div><div class="g">{ios_icons}</div><div class="dock">{dock()}</div></div>
<div class="note">Icon phương án B, tệp <code>app-icon-1024.png</code> (vuông, iOS tự bo góc 22,4%).</div></div>
<div class="col"><div class="ttl">Android · 48 dp, mặt nạ tròn</div><div class="ph an"><div class="sb"><span>9:41</span><span>5G ▮</span></div><div class="g">{and_icons}</div><div class="dock">{dock()}</div></div>
<div class="note">Adaptive icon: lớp nền + lớp trước 432 px, vùng an toàn 66 dp, mặt nạ tròn.</div></div>
<div class="sz"><div class="ttl">Kích thước thật</div>
<div class="r"><img src="assets/app-icon-1024.png" width="60" height="60" style="border-radius:13.5px">60 · Home</div>
<div class="r"><img src="assets/app-icon-1024.png" width="40" height="40" style="border-radius:9px">40 · Spotlight</div>
<div class="r"><img src="assets/app-icon-1024.png" width="29" height="29" style="border-radius:6.5px">29 · Cài đặt</div>
<div class="r"><img src="assets/app-icon-1024.png" width="20" height="20" style="border-radius:4.5px">20 · Thông báo</div>
<div class="r"><img src="assets/apple-touch-icon-180.png" width="90" height="90" style="border-radius:20px">90 · Touch icon web</div></div>"""
    write("app-icon-in-context.html", 1200, 860, "Icon app trong ngữ cảnh", css, body)
    return "app-icon-in-context.html", 1200, 860

# ---------- 4. Tab trình duyệt ----------
def browser_tab():
    def bar(dark):
        c = dict(bg="#202124", tab="#35363a", fg="#e8eaed", fg2="#9aa0a6", url="#202124", page="#171717", pagefg="#e5e5e5") if dark else \
            dict(bg="#dee1e6", tab="#ffffff", fg="#202124", fg2="#5f6368", url="#ffffff", page="#f1f1f1", pagefg="#171717")
        ico = "assets/favicon-32.png"
        return f"""<div class="win" style="background:{c['page']};color:{c['pagefg']}">
<div class="tabs" style="background:{c['bg']}"><div class="dots"><i style="background:#ff5f57"></i><i style="background:#febc2e"></i><i style="background:#28c840"></i></div>
<div class="tab on" style="background:{c['tab']};color:{c['fg']}"><img src="{ico}"><span>Đơn hàng · Invlogis</span><b style="color:{c['fg2']}">×</b></div>
<div class="tab" style="color:{c['fg2']}"><img src="{ico}"><span>Lệnh vận tải · Invlogis</span><b>×</b></div>
<div class="tab" style="color:{c['fg2']}"><div class="gen"></div><span>Tài liệu khác</span><b>×</b></div></div>
<div class="addr" style="background:{c['tab']}"><span style="color:{c['fg2']}">←  →  ⟳</span><div class="url" style="background:{'#f1f3f4' if not dark else '#202124'};color:{c['fg']}">🔒 app.invlogis.example/don-hang</div></div>
<div style="padding:22px 28px"><div style="width:220px;height:14px;border-radius:7px;background:{'#333' if dark else '#d4d4d4'}"></div></div></div>"""
    css = """body{background:#cfd2d9;padding:36px 40px;display:flex;flex-direction:column;gap:30px;font-family:'Be Vietnam Pro',sans-serif}
.lab{font:600 12px 'Be Vietnam Pro';letter-spacing:.06em;color:#444;margin-bottom:8px;text-transform:uppercase}
.win{width:760px;height:150px;border-radius:10px;overflow:hidden;box-shadow:0 6px 20px rgba(0,0,0,.2)}
.tabs{height:42px;display:flex;align-items:flex-end;gap:2px;padding:0 10px}
.dots{display:flex;gap:7px;align-items:center;height:38px;margin-right:14px}.dots i{width:12px;height:12px;border-radius:50%;display:block}
.tab{width:210px;height:34px;border-radius:9px 9px 0 0;display:flex;align-items:center;gap:8px;padding:0 12px;font-size:12px}
.tab img{width:16px;height:16px;image-rendering:auto}.tab span{flex:1;white-space:nowrap}.tab b{font-weight:400;font-size:14px}
.gen{width:16px;height:16px;border-radius:50%;background:#9aa0a6}
.addr{height:38px;display:flex;align-items:center;gap:16px;padding:0 14px;font-size:12px}
.url{flex:1;height:26px;border-radius:13px;display:flex;align-items:center;padding:0 14px}
.row{display:flex;gap:40px;align-items:flex-end}.zoom{display:flex;gap:14px;align-items:flex-end;font-size:11px;color:#444}
.zoom div{text-align:center}.zoom img{display:block;margin:0 auto 4px;image-rendering:pixelated}"""
    body = f"""<div><div class="lab">Tab · nền sáng</div>{bar(False)}</div><div><div class="lab">Tab · nền tối</div>{bar(True)}</div>
<div class="zoom"><div><img src="assets/favicon-16.png" width="16"><span>16 px</span></div><div><img src="assets/favicon-16.png" width="64"><span>16 ×4</span></div>
<div><img src="assets/favicon-32.png" width="32"><span>32 px</span></div><div><img src="assets/favicon-48.png" width="48"><span>48 px</span></div>
<div style="font-size:12px;max-width:380px;text-align:left;line-height:1.5;padding-left:20px">Favicon <code>favicon.svg</code> + PNG 16/32/48. Ký hiệu chữ i không có khung nên đọc được trên cả hai nền; trên nền tối tab Chrome giữ nguyên màu cobalt.</div></div>"""
    write("browser-tab.html", 840, 640, "Favicon trong tab trình duyệt", css, body)
    return "browser-tab.html", 840, 640

# ---------- 5. Email ----------
FONT_E = "-apple-system,'Segoe UI',Roboto,Helvetica,Arial,sans-serif"
def email(slug, preheader, title, intro, middle, button, after, fine):
    btn = f'''<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:28px 0 8px"><tr><td align="center" bgcolor="#262626" style="border-radius:8px"><a href="https://app.invlogis.example/{slug}" style="display:inline-block;padding:13px 28px;font-family:{FONT_E};font-size:15px;font-weight:600;color:#ffffff;text-decoration:none;border-radius:8px">{button}</a></td></tr></table>''' if button else ""
    html = f"""<!doctype html>
<html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="x-apple-disable-message-reformatting"><title>{title}</title></head>
<body style="margin:0;padding:0;background-color:#f1f1f1">
<div style="display:none;max-height:0;overflow:hidden;opacity:0;color:#f1f1f1">{preheader}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#f1f1f1"><tr><td align="center" style="padding:24px 12px">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" style="width:100%;max-width:600px;background-color:#ffffff;border-radius:12px;overflow:hidden">
<tr><td bgcolor="#0E1442" style="background-color:#0E1442;padding:28px 36px"><img src="https://[chờ: tên miền]/brand/email/logo-reverse.png" width="150" height="43" alt="Invlogis" style="display:block;border:0;height:auto"></td></tr>
<tr><td style="padding:36px 36px 8px;font-family:{FONT_E};color:#171717">
<h1 style="margin:0 0 14px;font-size:22px;line-height:1.3;font-weight:600;color:#171717">{title}</h1>
<p style="margin:0 0 14px;font-size:15px;line-height:1.6;color:#171717">{intro}</p>
{middle}{btn}
<p style="margin:14px 0 0;font-size:14px;line-height:1.6;color:#737373">{after}</p></td></tr>
<tr><td style="padding:24px 36px 0"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td style="border-top:1px solid #e5e5e5;font-size:0;line-height:0">&nbsp;</td></tr></table></td></tr>
<tr><td style="padding:12px 36px 32px;font-family:{FONT_E};font-size:12px;line-height:1.6;color:#737373">{fine}<br>Email gửi tự động từ Invlogis, đừng trả lời thư này.<br>© 2026 innvie · Invlogis là sản phẩm của innvie.</td></tr>
</table></td></tr></table></body></html>"""
    (R / "email" / f"{slug}.html").write_text(html, encoding="utf-8")
    return f"email/{slug}.html", 680, 0

def emails():
    out = []
    out.append(email("moi-nguoi-dung", "An Nguyễn mời bạn tham gia Công ty Vận tải Mẫu trên Invlogis.", "Bạn được mời vào Công ty Vận tải Mẫu",
        "<b>An Nguyễn</b> đã mời bạn tham gia không gian làm việc của <b>Công ty Vận tải Mẫu</b> trên Invlogis với vai trò <b>Điều phối viên</b>.",
        '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background-color:#f1f1f1;border-radius:8px"><tr><td style="padding:14px 16px;font-family:@@F@@;font-size:14px;line-height:1.7;color:#171717"><span style="color:#737373">Email của bạn</span><br><b>binh.tran@congtymau.vn</b><br><span style="color:#737373">Lời mời có hiệu lực</span><br><b>7 ngày, đến 21/10/2026</b></td></tr></table>'.replace('@@F@@', FONT_E),
        "Chấp nhận lời mời", "Nếu nút không bấm được, hãy sao chép đường dẫn sau vào trình duyệt:<br><span style='word-break:break-all'>https://app.invlogis.example/moi-nguoi-dung</span>",
        "Bạn nhận thư này vì có người nhập email của bạn khi mời thành viên. Nếu bạn không biết người này, hãy bỏ qua thư."))
    out.append(email("ma-xac-thuc", "Mã xác thực của bạn là 482 619, dùng trong 10 phút.", "Mã xác thực của bạn",
        "Nhập mã dưới đây để xác nhận đăng nhập vào Invlogis. Mã có hiệu lực trong <b>10 phút</b>.",
        '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin:22px 0 4px"><tr><td align="center" bgcolor="#f1f1f1" style="background-color:#f1f1f1;border-radius:8px;padding:20px 12px;font-family:\'SFMono-Regular\',Menlo,Consolas,monospace;font-size:34px;letter-spacing:10px;font-weight:600;color:#171717">482&nbsp;619</td></tr></table>',
        "", "Vì an toàn, không chia sẻ mã này cho bất kỳ ai, kể cả nhân viên Invlogis.",
        "Nếu bạn không yêu cầu mã này, hãy đổi mật khẩu ngay hoặc liên hệ quản trị viên của bạn."))
    out.append(email("dat-lai-mat-khau", "Đặt lại mật khẩu Invlogis, liên kết hết hạn sau 60 phút.", "Đặt lại mật khẩu",
        "Chúng tôi nhận được yêu cầu đặt lại mật khẩu cho tài khoản <b>binh.tran@congtymau.vn</b>. Bấm nút dưới đây để chọn mật khẩu mới. Liên kết hết hạn sau <b>60 phút</b>.",
        "", "Đặt mật khẩu mới", "Nếu bạn không yêu cầu, hãy bỏ qua thư này, mật khẩu hiện tại vẫn giữ nguyên.<br>Yêu cầu từ trình duyệt Chrome trên macOS, 14/10/2026 10:32.",
        "Nút không hoạt động? Sao chép: https://app.invlogis.example/dat-lai-mat-khau"))
    return out

# ---------- 6. Loading + About ----------
def logo_svg():
    s = (R / "../../../invlogis/logo/logo-motion.html").read_text(encoding="utf-8")
    m = re.search(r'<svg id="logo".*?</svg>', s, re.S)
    svg = m.group(0); n = [0]
    def k(mm):
        n[0] += 1; return f'<path class="lt" style="--k:{n[0]-1}"'
    return re.sub(r'<path class="lt"', k, svg)

MOTION_CSS = """#logo{width:240px;height:auto;overflow:visible;display:block}
.ii[data-part=stem]{transform-box:fill-box;transform-origin:50% 100%;animation:rise .7s cubic-bezier(.22,1,.36,1) both}
.ii[data-part=dot]{transform-box:fill-box;transform-origin:50% 100%;animation:fold .7s cubic-bezier(.65,0,.35,1) .45s both}
.lt{animation:show .55s cubic-bezier(.16,1,.3,1) calc(.9s + var(--k) * 70ms) both}
@keyframes rise{from{transform:scaleY(0)}to{transform:scaleY(1)}}
@keyframes fold{0%{transform:scaleY(-1);opacity:0}25%{opacity:1}100%{transform:scaleY(1);opacity:1}}
@keyframes show{from{opacity:0;transform:translateX(-60px)}to{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){.ii,.lt{animation:none!important}}"""

def loading():
    svg = logo_svg()
    css = MOTION_CSS + """
body{background:#fff;position:relative}.c{position:absolute;inset:0 0 100px;display:grid;place-items:center}
.f{position:absolute;bottom:40px;left:0;right:0;text-align:center;font-size:13px;color:var(--tx2)}"""
    body = f'<div class="c">{svg}</div>'
    write("loading-screen.html", 390, 844, "Màn hình tải", css, body)
    write("loading-screen-end.html", 390, 844, "Màn hình tải (khung cuối)", css + ".ii,.lt{animation:none!important}", body)
    # filmstrip 5 khung (tạm dừng tại mốc thời gian)
    frames = [200, 600, 1000, 1300, 2300]
    cells = "".join(f'<div class="cell" style="--t:{t}ms"><div class="s">{svg}</div><span>{t} ms</span></div>' for t in frames)
    css2 = MOTION_CSS.replace("#logo{width:240px", "#logo{width:200px") + """
.cell .ii,.cell .lt{animation-play-state:paused!important}
.cell .ii[data-part=stem]{animation-delay:calc(0ms - var(--t))!important}
.cell .ii[data-part=dot]{animation-delay:calc(450ms - var(--t))!important}
.cell .lt{animation-delay:calc(900ms + var(--k) * 70ms - var(--t))!important}
body{background:#f1f1f1;display:flex;gap:16px;padding:20px;font-family:'Be Vietnam Pro',sans-serif}
.cell{width:230px;height:300px;background:#fff;border-radius:12px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:20px;font-size:12px;color:#737373}
.cell .s{width:200px;display:flex;justify-content:center}"""
    write("loading-motion-frames.html", 1230, 340, "Chuyển động logo, 5 khung", css2, cells)
    return [("loading-screen.html", 390, 844), ("loading-motion-frames.html", 1230, 340)]

def about():
    css = """body{background:#fff;position:relative}
.top{height:56px;display:flex;align-items:center;padding:0 16px;gap:12px;font-weight:600;font-size:16px;margin-top:36px;border-bottom:1px solid var(--bd-d)}
.hero{text-align:center;padding:44px 24px 24px}
.item{display:flex;justify-content:space-between;padding:16px 20px;border-bottom:1px solid var(--bd-d);font-size:14px}
.item span:last-child{color:var(--tx2)}
.ft{position:absolute;bottom:34px;left:0;right:0;text-align:center;font-size:12px;color:var(--tx2)}"""
    body = """<div class="top"><span style="font-size:20px">‹</span>Giới thiệu</div>
<div class="hero"><img src="assets/invlogis-by-innvie.svg" style="height:92px;display:block;margin:0 auto 22px">
<div style="font-size:14px;color:var(--tx2)">Phiên bản 1.0.0 (build 100)</div>
<p style="margin:18px 0 0;font-size:14px;line-height:1.55;color:var(--tx)">Nền tảng vận hành vận tải cho doanh nghiệp logistics: điều phối, theo dõi và đối soát trên một hệ thống.</p></div>
<div style="margin-top:12px"><div class="item"><span>Dành cho</span><span>Công ty Vận tải Mẫu</span></div>
<div class="item"><span>Điều khoản sử dụng</span><span>›</span></div><div class="item"><span>Chính sách bảo mật</span><span>›</span></div><div class="item"><span>Giấy phép mã nguồn mở</span><span>›</span></div></div>
<div class="ft">Invlogis là sản phẩm của innvie<br>© 2026 innvie. Bảo lưu mọi quyền.</div>"""
    write("about-screen.html", 390, 844, "Màn hình Giới thiệu", css, body)
    return "about-screen.html", 390, 844

if __name__ == "__main__":
    import subprocess, sys
    jobs = []
    for t in (False, True):
        for m in (False, True):
            jobs.append(login(t, m))
    jobs += [splash("a"), splash("b"), app_icon(), browser_tab()]
    jobs += loading() + [about()]
    for n, w, h in jobs:
        out = R / "previews" / (pathlib.Path(n).stem + ".png")
        if n == "loading-screen.html": n = "loading-screen-end.html"
        subprocess.run([sys.executable, str(RENDER), str(R / n), str(out), "--size", f"{w}x{h}", "--scale", "1" if w > 1000 else "2"], check=True, capture_output=True)
    for n, _, _ in emails():
        out = R / "previews" / ("email-" + pathlib.Path(n).stem + ".png")
        tmp = R / "email" / "_preview.html"  # bản xem thử: logo trỏ về PNG cục bộ
        tmp.write_text((R / n).read_text(encoding="utf-8").replace("https://[chờ: tên miền]/brand/email/", "../assets/email/"), encoding="utf-8")
        n = "email/_preview.html"
        subprocess.run([sys.executable, str(RENDER), str(R / n), str(out), "--size", "680x760", "--scale", "1"], check=True, capture_output=True)
    (R / "email" / "_preview.html").unlink(missing_ok=True)
    print("ok")
