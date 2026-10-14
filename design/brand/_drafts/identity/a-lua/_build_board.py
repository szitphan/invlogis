#!/usr/bin/env python3
import base64, pathlib, subprocess, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _build_apps import *
def f64(n): return "data:image/png;base64,"+b64(H/n)
sv=lambda n: img((H/n).read_text())
sw=lambda hexc,name,role,fg="#fff": f'<div style="background:{hexc};color:{fg};padding:16px 14px;height:104px;border-radius:14px;border:1px solid rgba(14,20,66,.12);display:flex;flex-direction:column;justify-content:flex-end"><div style="font-family:Lexend;font-size:15px">{name}</div><div style="font-size:12px;opacity:.85">{hexc} · {role}</div></div>'
body=f'''
<div style="position:absolute;inset:0;background:var(--paper)"></div>
<div style="position:absolute;left:64px;right:64px;top:48px">
 <div style="display:flex;justify-content:space-between;align-items:flex-end"><div><div class="mono" style="font-family:Lexend;font-size:14px;letter-spacing:.14em;text-transform:uppercase;color:var(--cobalt)">Hướng A · Lụa</div>
 <h1 class="display" style="font-size:54px;margin-top:8px">Dữ liệu chảy mượt như lụa</h1></div><img src="{sv('invlogis-by-innvie.svg')}" style="height:56px"></div>
 <p style="margin-top:18px;font-size:19px;line-height:1.55;color:var(--mute);max-width:1100px">Chứng từ giấy, tin nhắn, file rời rạc được “gấp” lại thành một dòng dữ liệu liền mạch. Ký hiệu là một dải lụa gấp thành chữ i: chấm và thân là hai nửa của cùng một nếp gấp. Chữ nhẹ, rộng, thoáng; độ tin cậy đến từ nền giấy ấm, mực chàm đậm và những nhãn chứng từ nhỏ.</p>
 <div class="hair" style="margin-top:26px;color:var(--ink)"></div>

 <div style="font-family:Lexend;font-size:13px;letter-spacing:.12em;text-transform:uppercase;margin:22px 0 14px;color:var(--mute)">01 · Logo và biến thể</div>
 <div style="display:grid;grid-template-columns:1.55fr 1fr;gap:16px">
  <div class="frame" style="--p:8px;--r:22px;border-color:rgba(14,20,66,.15)"><div style="height:210px;border-radius:15px;background:#fff;display:flex;align-items:center;justify-content:center"><img src="{sv('invlogis-logo.svg')}" style="width:62%"></div></div>
  <div class="frame" style="--p:8px;--r:22px;border-color:rgba(14,20,66,.15)"><div style="height:210px;border-radius:15px;background:#0B1033;display:flex;align-items:center;justify-content:center"><img src="{sv('invlogis-logo-reverse.svg').replace('fill=%220B1033%22','')}" style="width:80%"></div></div>
 </div>
 <div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:16px;margin-top:16px">
  <div style="height:150px;border-radius:15px;background:#fff;border:1px solid rgba(14,20,66,.12);display:flex;align-items:center;justify-content:center"><img src="{sv('invlogis-logo-mono.svg')}" style="width:76%"></div>
  <div style="height:150px;border-radius:15px;background:#fff;border:1px solid rgba(14,20,66,.12);display:flex;align-items:center;justify-content:center"><img src="{sv('invlogis-by-innvie.svg')}" style="width:68%"></div>
  <div style="height:150px;border-radius:15px;background:#fff;border:1px solid rgba(14,20,66,.12);display:flex;align-items:center;justify-content:center;gap:28px"><img src="{sv('invlogis-symbol.svg')}" style="height:104px"><img src="{sv('invlogis-symbol-mono.svg')}" style="height:104px"></div>
  <div style="height:150px;border-radius:15px;background:#fff;border:1px solid rgba(14,20,66,.12);display:flex;align-items:center;justify-content:center;flex-direction:column;gap:14px"><img src="{sv('innvie-logo.svg')}" style="width:64%"><span style="font-size:12px;color:var(--mute)">innvie · chữ ký pháp nhân</span></div>
 </div>
 <div style="margin-top:8px;font-size:12px;color:var(--mute)">Trên: logo chính (màu) và bản nền tối. Hàng dưới: đơn sắc · có chữ ký “by innvie” · ký hiệu (màu, đơn sắc) · logo innvie. Chi tiết riêng: chữ v có cánh phải là dải lụa cobalt vắt lên cánh trái, ngăn bằng khe mảnh; chấm i luôn là nếp gấp nghiêng.</div>

 <div style="font-family:Lexend;font-size:13px;letter-spacing:.12em;text-transform:uppercase;margin:26px 0 14px;color:var(--mute)">02 · Thử cỡ nhỏ và đơn sắc</div>
 <div style="display:flex;gap:16px;align-items:stretch">
  <div style="flex:1.1;border-radius:15px;background:#fff;border:1px solid rgba(14,20,66,.12);padding:18px 22px;display:flex;align-items:flex-end;gap:26px">
   <div style="text-align:center"><img src="{f64('favicon-16.png')}" style="width:16px;height:16px;display:block;margin:0 auto 8px"><span style="font-size:11px">16px</span></div>
   <div style="text-align:center"><img src="{f64('favicon-32.png')}" style="width:32px;height:32px;display:block;margin:0 auto 8px"><span style="font-size:11px">32px</span></div>
   <div style="text-align:center"><img src="{f64('favicon-32.png')}" style="width:128px;height:128px;image-rendering:pixelated;display:block;margin:0 auto 8px;border-radius:20px"><span style="font-size:11px">32px phóng 4×</span></div>
   <div style="text-align:center"><img src="{f64('app-icon-1024.png')}" style="width:96px;height:96px;border-radius:22px;display:block;margin:0 auto 8px"><span style="font-size:11px">icon app</span></div></div>
  <div style="flex:1;border-radius:15px;background:#fff;border:1px solid rgba(14,20,66,.12);padding:18px 22px;display:flex;align-items:center;gap:30px">
   <div><img src="{sv('invlogis-logo.svg')}" style="width:160px;display:block"><div style="font-size:11px;margin-top:6px">160px</div></div>
   <div><img src="{sv('invlogis-logo.svg')}" style="width:96px;display:block"><div style="font-size:11px;margin-top:6px">96px</div></div>
   <div><img src="{sv('invlogis-logo-mono.svg')}" style="width:96px;display:block"><div style="font-size:11px;margin-top:6px">đơn sắc 96px</div></div></div>
 </div>

 <div style="font-family:Lexend;font-size:13px;letter-spacing:.12em;text-transform:uppercase;margin:26px 0 14px;color:var(--mute)">03 · Màu</div>
 <div style="display:grid;grid-template-columns:repeat(6,1fr);gap:10px">
  {sw('#2F43DB','Cobalt','chủ đạo')}{sw('#0E1442','Mực chàm','chữ, nền tối')}{sw('#97A6FF','Periwinkle','gradient sáng','#0E1442')}{sw('#E6EAF8','Xanh khói','nền phụ','#0E1442')}{sw('#FAF8F4','Giấy ấm','nền chính','#0E1442')}{sw('#4A5380','Xám chàm','chữ phụ')}</div>
 <div style="margin-top:12px;height:88px;border-radius:14px;position:relative;overflow:hidden"><div style="position:absolute;inset:0;background:linear-gradient(90deg,#0E1442,#2F43DB 32%,#7B55FF 56%,#E24C9A 78%,#FF7A59)"></div><div class="silk" style="background:none"><div class="grain"></div></div><div style="position:absolute;left:18px;bottom:10px;color:#fff;font-size:12px">Gradient chiến dịch: mực chàm → cobalt → tím → hồng → san hô, neo về xanh</div></div>

 <div style="font-family:Lexend;font-size:13px;letter-spacing:.12em;text-transform:uppercase;margin:26px 0 14px;color:var(--mute)">04 · Chữ</div>
 <div style="display:grid;grid-template-columns:1.2fr 1fr;gap:16px">
  <div><div class="display" style="font-size:50px;line-height:1.1">Chứng từ Việt, vào thẳng hồ sơ.</div><div style="font-size:12px;color:var(--mute);margin-top:8px">Lexend Light · hiển thị (OFL, đủ dấu tiếng Việt)</div></div>
  <div><div style="font-size:16px;line-height:1.6">Be Vietnam Pro làm chữ thân: Booking Note, eDO, EIR, phiếu cân và tờ khai có mã QR được đọc vào đúng trường, đúng mốc, minh bạch cho từng lô hàng.</div><div style="font-size:12px;color:var(--mute);margin-top:8px">Be Vietnam Pro Regular/Medium · thân (OFL)</div>
  <div style="margin-top:10px"><span class="chip dk" style="--cs:13px;border-color:rgba(14,20,66,.3)">[Booking Note]</span> <span class="chip dk" style="--cs:13px;border-color:rgba(14,20,66,.3)">[eDO]</span> <span class="chip dk" style="--cs:13px;border-color:rgba(14,20,66,.3)">[EIR]</span></div></div></div>

 <div style="font-family:Lexend;font-size:13px;letter-spacing:.12em;text-transform:uppercase;margin:26px 0 14px;color:var(--mute)">05 · Ứng dụng mẫu</div>
 <div style="display:flex;gap:20px;align-items:flex-start">
  <div style="flex:1.78"><img src="{f64('deck-cover.png')}" style="width:100%;border-radius:12px;border:1px solid rgba(14,20,66,.15);display:block"><div style="font-size:12px;color:var(--mute);margin-top:6px">Bìa deck 1920×1080</div></div>
  <div style="flex:.8"><img src="{f64('social-post.png')}" style="width:100%;border-radius:12px;display:block"><div style="font-size:12px;color:var(--mute);margin-top:6px">Bài mạng xã hội 1080×1350</div></div>
  <div style="flex:.4"><img src="{f64('splash-mobile.png')}" style="width:100%;border-radius:16px;display:block"><div style="font-size:12px;color:var(--mute);margin-top:6px">Splash 390×844</div></div></div>
</div>'''
(H/"board.html").write_text(page(1600,2000,body))
subprocess.run(["python3",str(R),str(H/"board.html"),str(H/"board.png"),"--size","1600x2000"],check=True,capture_output=True)
print("board ok")
