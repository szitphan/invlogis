#!/usr/bin/env python3
"""Trang tổng hợp Animation bổ sung so với Untitled (DEC-336). Chạy preset bằng đúng lớp .anim-* của tokens.css. Dựng: python3 _scripts/foundation_review/animation_summary.py"""
import json
import re

from kit import ROOT

SRC = ROOT / "design-system/_review/foundations/motion-summary.html"
OUT = ROOT / "design-system/_review/foundations/animation-summary.html"
TCSS = (ROOT / "design-system/tokens.css").read_text(encoding="utf-8")
TJ = json.loads((ROOT / "design-system/tokens.json").read_text(encoding="utf-8"))
BASE = re.search(r"<style>(.*?)</style>", SRC.read_text(encoding="utf-8"), re.S).group(1)
HEAD = re.search(r'<link rel="stylesheet"[^>]*>', SRC.read_text(encoding="utf-8")).group(0)

SAME, DIFF, OWN = ("same", "Giống"), ("diff", "Khác có lý do"), ("own", "Riêng của mình")
OFF = "<span class=off>Khác khuyến nghị</span>"

GROUPS = [
    ("Cấu trúc", [
        ("an00", False, "Không thêm bậc; mốc giữ 1000, 1500 là bội của <code>duration/slow</code>", "Không có biến thời gian", DIFF),
        ("an01", False, "<mark>8 preset có tên</mark> trong <code>tokens.json</code>, sinh <code>.anim-*</code> và <code>InvMotionPreset</code>", "Dùng lớp có sẵn của Tailwind", DIFF),
    ]),
    ("Phản hồi thao tác", [
        ("an02", False, "<mark>Ba nhịp, tổng 600</mark>, chạy một lần, không nảy, cho cả thành công và thất bại <span class=mut>Theo mẫu Lottie Wizard, bỏ độ nảy và phần lặp</span>", "Không có", OWN),
        ("an03", True, "Lỗi biểu mẫu <mark>đổi ngay</mark>, không chạy, không rung", "Không rung", SAME),
        ("an04", True, "Spinner rồi về nhãn, <mark>kết quả báo bằng toast</mark>", "<code>isLoading</code> về nhãn, không có pha xong", SAME),
        ("an05", False, "Đổi icon mờ chéo + phóng 95, giữ 1000", "Không có luật chung", OWN),
    ]),
    ("Dữ liệu đổi", [
        ("an06", False, "Dòng vừa đổi tô <code>color/utility/blue/50</code>, giữ 1000, phai 500, chạy một lần", "Không có", OWN),
        ("an07", False, "Số mờ dần, không đếm chạy", "Không có", OWN),
        ("an08", True, "<mark>Luôn báo “Có n lệnh mới”</mark>, bấm thì dòng mở cao + tô nền <span class=mut>Bạn chọn kết hợp hai phương án</span>", "Không có", OWN),
        ("an09", False, "Tiến độ trượt 125 linear; chưa biết % thì spinner", "<code>duration-75 ease-linear</code>", DIFF),
        ("an10", False, "Mở 300, đóng 200; xoá dòng cũng co lại", "Không có component", OWN),
        ("an11", False, "Skeleton sang nội dung, đổi trang web: mờ dần 125", "Không có skeleton", OWN),
    ]),
    ("Logistics và app", [
        ("an12", False, "Xe trượt 300 khi có điểm GPS mới, giữa hai điểm đứng yên", "Không có bản đồ", OWN),
        ("an13", False, "Bước tiến độ: vạch 300, chấm 125 nối tiếp", "Không có", OWN),
        ("an14", True, "<mark>Vạch quét lặp</mark>, sau 5 giây dừng + gợi ý nhập tay, nhận mã thì sang màn sau <span class=mut>Bạn chọn kết hợp hai phương án</span>", "Không có", OWN),
        ("an15", False, "Kéo làm mới theo mặc định của nền tảng", "Không có, Untitled là web", OWN),
        ("an16", False, "Dải mất mạng đẩy nội dung; có mạng xanh 1000 rồi đóng", "Không có", OWN),
    ]),
    ("Biểu đồ", [
        ("an17", True, "<mark>Cột mọc 300 khi tải</mark>, đổi lọc thì đổi ngay", f"Tắt: <code>isAnimationActive={{false}}</code>", DIFF),
    ]),
]
ROWS = [r for _, g in GROUPS for r in g]
CNT = {k: sum(1 for r in ROWS if r[4] is k) for k in (SAME, DIFF, OWN)}
N_OFF = sum(1 for r in ROWS if r[1])

CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" class="s"><path class="p anim-draw" pathLength="1" d="M4 12l5 5L20 6"/></svg>'
CROSS = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" class="s"><path class="p anim-draw" pathLength="1" d="M6 6l12 12"/><path class="p anim-draw d2" pathLength="1" d="M18 6 6 18"/></svg>'
BARS = "".join(f'<i class="anim-grow" style="height:{h}%"></i>' for h in (46, 68, 38, 84, 60, 72))
STAGE = [
    ("fade-in", '<b class="num big anim-fade-in">128</b>'),
    ("pop", '<i class="dot anim-pop"></i>'),
    ("draw", f'<span class="ink">{CHECK}</span>'),
    ("swap", '<span class="ink big anim-swap">✓</span>'),
    ("flash", '<span class="row anim-flash"><code>LVT-2026-0412</code></span>'),
    ("expand", '<span class="acc anim-expand"><span><span class="in">51C-482.15 · mooc 51R-091.44</span></span></span>'),
    ("glide", '<i class="xe anim-glide"></i>'),
    ("grow", f'<span class="bars">{BARS}</span>'),
]
PRESET = "".join(f'<div class="ps" data-p="{n}"><div class="sc">{x}</div><div class="ft"><code>{n}</code><button type="button">Phát</button></div></div>' for n, x in STAGE)

CSS = BASE + r"""
.ps-g{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:12px}.ps{border:1px solid var(--line);border-radius:12px;padding:10px;background:var(--card)}
.sc{height:96px;border-radius:8px;background:color-mix(in srgb,var(--line) 30%,transparent);display:grid;place-items:center;overflow:hidden;margin-bottom:8px;color:var(--fg)}
.ft{display:flex;justify-content:space-between;align-items:center}.ft button,.res-go{border:1px solid var(--line);background:var(--card);color:var(--fg);border-radius:8px;padding:4px 10px;font:600 12px Inter;cursor:pointer}
.big{font:600 26px Inter}.dot{width:44px;height:44px;border-radius:50%;background:#4F86F7;display:block}.ink svg{width:44px;height:44px;display:block}
.row{display:block;width:90%;padding:8px 10px;border-radius:6px}.acc{width:90%;border:1px solid var(--line);border-radius:8px;min-height:18px}.acc .in{display:block;padding:8px 10px;font-size:12px}.ps.op .acc{--x:1}
.xe{width:22px;height:22px;border-radius:50%;background:var(--fg);display:block;justify-self:start;margin-left:10px}.ps.mv .xe{transform:translateX(150px)}
.bars{display:flex;align-items:flex-end;gap:6px;height:76px;width:80%}.bars i{flex:1;background:#4F86F7;border-radius:3px 3px 0 0;display:block}
.res{display:flex;gap:36px;flex-wrap:wrap;align-items:center}.mk{position:relative;width:72px;height:72px;display:grid;place-items:center;color:#fff}.mk i{position:absolute;border-radius:50%}.mk .o{inset:0}.mk .n{inset:7px}.mk svg{position:relative;width:32px;height:32px}
.mk.ok .o{background:var(--color-bg-success-secondary)}.mk.ok .n{background:var(--color-bg-success-solid)}.mk.no .o{background:var(--color-bg-error-secondary)}.mk.no .n{background:var(--color-bg-error-solid)}
.res.go .o{animation:inv-pop var(--duration-medium) var(--easing-standard) both}.res.go .n{animation:inv-pop var(--duration-medium) var(--easing-standard) var(--duration-fast) both}
.res.go .ok .p{animation:inv-draw var(--duration-medium) var(--easing-standard) var(--duration-medium) both}.res.go .no .p{animation:inv-draw var(--duration-fast) var(--easing-standard) var(--duration-medium) both}.res.go .no .p.d2{animation-delay:calc(var(--duration-medium) + var(--duration-fast))}
.s .p{stroke-dasharray:1}
"""

JS = r"""
document.querySelectorAll('.ps button').forEach(function(b){b.addEventListener('click',function(){var p=b.closest('.ps'),n=p.dataset.p;
 if(n==='expand'){var a=p.querySelector('.anim-expand');a.dataset.open=a.dataset.open==='true'?'false':'true';return}
 if(n==='glide'){p.classList.toggle('mv');return}
 var c='anim-'+n;p.querySelectorAll('.'+c).forEach(function(e){e.classList.remove(c);void e.getBoundingClientRect();e.classList.add(c)})})});
document.getElementById('resGo').addEventListener('click',function(){var r=document.getElementById('res');r.classList.remove('go');void r.offsetWidth;r.classList.add('go')});
"""

rows = []
for g, items in GROUPS:
    rows.append(f'<tr class="g"><th colspan="4" scope="colgroup">{g}</th></tr>')
    for i, off, chot, unt, st in items:
        rows.append(f'<tr><td class="id">{i}{OFF if off else ""}</td><td>{chot}</td><td>{unt}</td><td><span class="pill {st[0]}">{st[1]}</span></td></tr>')

HTML = f"""<!DOCTYPE html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Animation so với Untitled</title>
{HEAD}
<style>{TCSS}{CSS}</style></head><body>
<div class="band"><div><div><h1>Animation bổ sung: bản chốt so với Untitled</h1><p>18 mục · DEC-336 · tokens.json {TJ["version"]} · 02/11/2026</p></div></div></div>
<main>
<section><p>Untitled gần như <mark>không có các animation này</mark>, nên {CNT[OWN]}/{len(ROWS)} mục là luật riêng cho điều vận và lái xe. Không thêm bậc thời gian nào, mọi preset đi qua biến có sẵn nên giảm chuyển động tự về 0.</p>
<div class="kp"><div><b>{CNT[SAME]}</b>Giống Untitled</div><div><b>{CNT[DIFF]}</b>Khác có lý do</div><div><b>{CNT[OWN]}</b>Riêng của mình</div><div><b>{N_OFF}</b>Mục bạn chọn khác khuyến nghị</div></div></section>
<section><h2>Dấu kết quả</h2><div class="vis"><div class="res" id="res"><div class="mk ok"><i class="o"></i><i class="n"></i>{CHECK}</div><div class="mk no"><i class="o"></i><i class="n"></i>{CROSS}</div><button class="res-go" id="resGo" type="button">Phát</button></div>
<p class="mut">Dấu tích đi từ nét ngắn sang nét dài. Dấu X vẽ từ trên trái rồi từ trên phải.</p></div></section>
<section><h2>8 preset, chạy bằng lớp <code>.anim-*</code> thật</h2><div class="ps-g">{PRESET}</div></section>
<section><h2>18 mục đã chốt</h2><div class="tw"><table><thead><tr><th>Mục</th><th>Phương án chốt</th><th>Untitled</th><th>So sánh</th></tr></thead><tbody>{"".join(rows)}</tbody></table></div></section>
<section><h2>Ghi chú</h2><p><b>Trên Figma</b></p><ul><li>Trang <code>DS · Foundations</code>, nhóm Chuyển động, có thêm khối Preset animation chạy bằng keyframe và bảng Animation theo việc.</li>
<li>Figma chỉ chạy keyframe khi khung hiện ra, không chạy theo cú bấm, và lặp lại khi Present. Trong sản phẩm, dấu kết quả chỉ chạy một lần.</li>
<li>Mẫu <code>flash</code> trên Figma tô bằng mã màu, vì keyframe không nhận biến.</li></ul>
<p><b>Còn việc</b></p><ul><li>Chu kỳ GPS thật của EUP chưa có số; trên 30 giây thì xem lại an12.</li><li>Ngưỡng 5 dòng (an06) và 2 giây (an16) là đề xuất, chưa đo.</li><li>Component dùng preset khi tới lượt sync, theo task trong backlog.</li></ul></section>
</main><script>{JS}</script></body></html>
"""
OUT.write_text(HTML, encoding="utf-8")
print(OUT.relative_to(ROOT), len(HTML) // 1024, "KB", {k[1]: v for k, v in CNT.items()}, "khác khuyến nghị", N_OFF)
