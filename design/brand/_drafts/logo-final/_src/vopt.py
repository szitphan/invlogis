import pathlib
H=pathlib.Path(__file__).parent
def emb(n): return (H/n).read_text().replace('<svg ','<svg preserveAspectRatio="xMinYMid meet" ',1)
# id trùng giữa các SVG nhúng → đổi tiền tố
def emb_u(n,u):
    s=emb(n)
    import re
    return re.sub(r'(id="|url\(#)([sdv]\d+)', lambda m:m.group(1)+u+m.group(2), s)
opts=[(1,"Gradient nhẹ","v giữ nguyên dáng Lexend, tô dải mực chàm → cobalt từ đầu cánh xuống đáy.","Vẫn là một vùng màu khác giữa chữ: mắt dừng ở v, mất nhịp; đơn sắc thì mất hết ý."),
      (2,"Nếp gấp","v cùng nét Lexend, chỉ cắt đầu hai cánh chéo 14° song song nếp gấp của chữ i.","Cùng ngôn ngữ với i, không đổi màu; nhưng dưới ~48px vết cắt gần như biến mất, cạnh n và l lại thấy “lệch” nhẹ."),
      (3,"Nguyên bản + dồn lụa về i","v Lexend nguyên bản, cùng màu mực. Toàn bộ chi tiết lụa nằm ở chữ i đầu.","Đề xuất. Một điểm nhấn duy nhất, tám chữ đều nhịp; i lụa vừa là chữ đầu vừa là ký hiệu.")]
import re, build
items,_=build.shape(build.LEX(),"invlogis",build.TRACK)
xn=items[1]["x"]; xl=items[3]["x"]+175
def zoom(k):
    s=emb_u(f"v{k}.svg",f"z{k}")
    return re.sub(r'viewBox="[^"]+"', f'viewBox="{xn-30:.0f} 180 {xl-xn+30:.0f} 660"', s, count=1)
cards=""
for k,t,d,n in opts:
    rec=(k==3)
    cards+=f'''<div class="card{' rec' if rec else ''}"><div class="hd"><span class="num">{k}</span><span class="t">{t}</span>{'<span class="badge">Đề xuất</span>' if rec else ''}</div>
<div class="big">{emb_u(f"v{k}.svg",f"o{k}")}</div>
<div class="row"><div class="sm s48">{emb_u(f"v{k}.svg",f"p{k}")}</div><div class="sm s24">{emb_u(f"v{k}.svg",f"q{k}")}</div><div class="sm s24">{emb_u(f"v{k}-mono.svg",f"r{k}")}</div></div>
<div class="lab">48px · 24px · đơn sắc 24px</div>
<div class="zoom">{zoom(k)}</div><div class="lab">phóng to “nvl” — đầu cánh và đáy chữ v</div>
<p class="d">{d}</p><p class="n">{n}</p></div>'''
html=f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:BVP;src:url(BeVietnamPro-400.ttf)}}@font-face{{font-family:BVP;font-weight:500;src:url(BeVietnamPro-500.ttf)}}
@font-face{{font-family:Lex;src:url(LexendVF.ttf);font-weight:100 900}}
*{{box-sizing:border-box;margin:0}}body{{width:1600px;height:900px;background:#FAF8F4;font-family:BVP;color:#0E1442;padding:30px 56px}}
.eb{{font:400 15px Lex;letter-spacing:.14em;text-transform:uppercase;color:#2F43DB}}h1{{font:300 44px/1.15 Lex;margin:10px 0 6px}}
.sub{{font-size:17px;color:#4A5380;margin-bottom:18px}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}}
.card{{background:#fff;border:1px solid #E1E4F0;border-radius:22px;padding:22px 26px;height:660px;position:relative}}
.card.rec{{border:1.5px solid #2F43DB;box-shadow:0 0 0 5px #E6EAF8}}
.hd{{display:flex;align-items:center;gap:12px}}.num{{width:34px;height:34px;border-radius:50%;border:1px solid #0E1442;display:grid;place-items:center;font:400 17px Lex}}
.t{{font:400 21px Lex}}.badge{{margin-left:auto;font:500 13px BVP;color:#fff;background:#2F43DB;border-radius:99px;padding:5px 12px}}
.big{{height:180px;display:flex;align-items:center;justify-content:center;border-bottom:1px solid #EEF0F6;margin-bottom:12px}}.big svg{{width:380px;height:auto}}
.row{{display:flex;align-items:center;gap:26px;height:70px}}.sm svg{{display:block;width:auto}}.s48 svg{{height:48px}}.s24 svg{{height:24px}}
.zoom{{height:120px;background:#FAF8F4;border-radius:12px;display:flex;justify-content:center;margin-top:4px}}.zoom svg{{height:120px;width:auto}}.lab{{font-size:13px;color:#8B93B8;margin:4px 0 8px}}.d{{font-size:16px;line-height:1.5;margin-bottom:10px}}.n{{font-size:15px;line-height:1.5;color:#4A5380}}
.rec .n{{color:#2F43DB;font-weight:500}}
</style></head><body><div class="eb">Logo Invlogis · việc 2.1 · vẽ lại chữ v</div><h1>Ba phương án chữ v trong “invlogis”</h1>
<div class="sub">Cùng Lexend 340, cùng chữ i lụa ở đầu; chỉ khác chữ v. Nguyên tắc: v phải cùng độ đậm, cùng nhịp với các chữ khác.</div>
<div class="grid">{cards}</div></body></html>'''
(H/"v-options.html").write_text(html)
