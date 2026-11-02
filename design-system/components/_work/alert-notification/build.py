#!/usr/bin/env python3
import sys
"""Sinh page.json cho Alert & Notification (vòng 1 Brainstorm) — nháp, chưa ghi repo."""
import json
from pathlib import Path

OUT = Path(__file__).parent / "page.json"

# ---------- icon (Lucide, nét) ----------
P = {
    "ok": '<circle cx="12" cy="12" r="9"/><path d="M8 12l3 3 5-6"/>',
    "warn": '<path d="M12 3l9.5 17h-19z"/><path d="M12 10v4M12 17h.01"/>',
    "err": '<circle cx="12" cy="12" r="9"/><path d="M12 8v5M12 16h.01"/>',
    "info": '<circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8h.01"/>',
    "x": '<path d="M6 6l12 12M18 6L6 18"/>',
    "truck": '<path d="M3 6h11v10H3zM14 9h4l3 3v4h-7"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
    "file": '<path d="M14 3H6v18h12V7z"/><path d="M14 3v4h4M9 13h6M9 17h4"/>',
    "upload": '<path d="M12 15V4M7 9l5-5 5 5"/><path d="M4 15v4a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-4"/>',
    "download": '<path d="M12 4v11M7 10l5 5 5-5"/><path d="M4 15v4a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-4"/>',
    "import": '<path d="M14 3H6v18h12V7z"/><path d="M14 3v4h4M12 11v6M9 14l3 3 3-3"/>',
    "wifi": '<path d="M2 8.5a15 15 0 0 1 20 0M5 12a10 10 0 0 1 14 0M8.5 15.5a5 5 0 0 1 7 0M12 19h.01"/><path d="M3 3l18 18"/>',
}
def ic(k, s=20):
    return f'<svg class="i" viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{P[k]}</svg>'

# ---------- phần tử ----------
def toast(tone, title, desc="", actions=(), timer=True, extra="", lead=None, body=""):
    acts = "".join(f'<button class="lk{" pri" if i == 0 else ""}">{a}</button>' for i, a in enumerate(actions))
    lead = lead or f'<span class="ib">{ic(tone)}</span>'
    return (f'<div class="ts {tone}" data-cmp {extra}>{lead}'
            f'<div class="tx"><div class="tt">{title}</div>{f"<div class=ds>{desc}</div>" if desc else ""}{body}'
            f'{f"<div class=ac>{acts}</div>" if acts else ""}</div>'
            f'<button class="cl" aria-label="Đóng">{ic("x", 16)}</button>'
            f'{"<i class=tm></i>" if timer else ""}</div>')

# Type=Icon: icon nội dung, tông trung tính
def t_icon(icon, title, desc="", actions=(), extra=""):
    return toast("nt", title, desc, actions, extra=extra, lead=f'<span class="ib">{ic(icon)}</span>')

# Type=Avatar: người gây ra sự kiện
def t_avatar(ini, title, desc="", actions=(), extra="", online=True):
    return toast("nt", title, desc, actions, extra=extra,
                 lead=f'<span class="av">{ini}{"<i class=on></i>" if online else ""}</span>')

# Type=Progress: tải lên / xuất / nhập — không tự ẩn khi đang chạy
def t_prog(icon, title, pct, meta, actions=("Huỷ",), tone="nt", extra=""):
    bar = (f'<div class="pg"><div class="pb"><i style="width:{pct}%"></i></div><span>{pct}%</span></div>'
           f'<div class="ds">{meta}</div>') if pct is not None else ""
    return toast(tone, title, "" if pct is not None else meta, actions, timer=(pct is None and tone == "ok"), extra=extra,
                 lead=f'<span class="ib">{ic(icon if tone == "nt" else tone)}</span>', body=bar)

def alert(tone, title, desc="", actions=(), close=True, extra=""):
    acts = "".join(f'<button class="bt{" pri" if i == 0 else ""}">{a}</button>' for i, a in enumerate(actions))
    return (f'<div class="al {tone}{" stack" if len(actions) > 1 else ""}" data-cmp {extra}><span class="ib">{ic(tone)}</span>'
            f'<div class="tx"><div class="tt">{title}</div>{f"<div class=ds>{desc}</div>" if desc else ""}</div>'
            f'{f"<div class=ac>{acts}</div>" if acts else ""}'
            f'{"<button class=cl aria-label=Đóng>" + ic("x", 16) + "</button>" if close else ""}</div>')

def banner(show=True):
    return (f'<div class="bn" data-cmp {'data-show="D7:a"' if show else ""}>{ic("wifi", 18)}<span><b>Mất kết nối máy chủ.</b> '
            f'Dữ liệu trên màn có thể chưa mới nhất.</span><button class="bt">Thử lại</button></div>')

LONG = ("Đã gửi lệnh LVT-2026-0412 cho tài xế Trần Văn Bình — tuyến Cảng Cát Lái → KCN Sóng Thần, "
        "container 40' HC, giao trước 16:00")

def toasts(mobile=False):
    return (f'<div class="tz{" m" if mobile else ""}">'
            + toast("ok", "Đã gửi lệnh LVT-2026-0412", "" if mobile else "Tài xế nhận được thông báo trên app.", extra='data-show="state:default"')
            + toast("ok", "Đã huỷ lệnh LVT-2026-0413", "", ("Hoàn tác",), extra='data-show="state:action"')
            + toast("ok", LONG, "", ("Xem lệnh",), extra='data-show="state:long"')
            + toast("err", "Không gửi được lệnh", "Kiểm tra kết nối mạng rồi thử lại.", ("Thử lại",), timer=False, extra='data-show="state:error"')
            + t_prog("download", "Đang xuất 128 lệnh ra Excel", 40, "Khoảng 20 giây nữa", extra='data-show="state:stack"')
            + toast("warn", "Lệnh LVT-2026-0415 chưa có xe", "", ("Gán xe",), extra='data-show="state:stack"')
            + toast("ok", "Đã gửi lệnh LVT-2026-0412", "", (), extra='data-show="state:stack"')
            + t_avatar("LC", "Lê Minh Châu đã nhận lệnh LVT-2026-0413", "2 phút trước", ("Xem lệnh",), extra='data-show="state:avatar"')
            + t_icon("truck", "Xe 51C-123.45 đã vào cổng Cát Lái", "Lệnh LVT-2026-0412 · 09:42", ("Xem lệnh",), extra='data-show="state:icon"')
            + t_prog("upload", "Đang tải lên biên bản giao container.pdf", 64, "1,2 MB / 1,9 MB", extra='data-show="state:progress"')
            + "</div>")

def rows(n=4):
    data = [("LVT-2026-0412", "Cát Lái → Sóng Thần", "51C-123.45", "Trần Văn Bình", "Đang chạy"),
            ("LVT-2026-0413", "Hiệp Phước → VSIP 2", "51D-678.90", "Lê Minh Châu", "Đã huỷ"),
            ("LVT-2026-0414", "Cát Lái → Long Hậu", "51C-246.80", "Phạm Quốc Dũng", "Chờ nhận"),
            ("LVT-2026-0415", "ICD Phước Long → Tân Uyên", "—", "—", "Chưa gán xe")]
    return "".join(f"<tr><td class=mono>{a}</td><td>{b}</td><td class=mono>{c}</td><td>{d}</td><td><span class=chip>{e}</span></td></tr>" for a, b, c, d, e in data[:n])

# ---------- màn ----------
S_LIST_WEB = ('<div class="pad">' + alert("info", "Danh sách vừa có cập nhật.", "", ("Tải lại",), close=False)
    + '<div class="tb"><table><tr><th>Mã lệnh</th><th>Tuyến</th><th>Xe</th><th>Lái xe</th><th>Trạng thái</th></tr>'
    + rows() + "</table></div></div>" + toasts())

S_DETAIL_WEB = ('<div class="pad grid2"><div class="card"><div class="h">Thông tin lệnh</div>'
    '<dl><dt>Mã lệnh</dt><dd class=mono>LVT-2026-0412</dd><dt>Tuyến</dt><dd>Cảng Cát Lái → KCN Sóng Thần</dd>'
    '<dt>Xe</dt><dd class=mono>51C-123.45 · đầu kéo + mooc 40\'</dd><dt>Lái xe</dt><dd>Trần Văn Bình</dd></dl>'
    + alert("ok", "Tài xế đã nhận lệnh lúc 08:15.", "", (), close=True)
    + '</div><div class="card"><div class="h">Quy trình</div>'
    + alert("err", "Không tải được quy trình.", "Phần còn lại của lệnh vẫn dùng bình thường.", ("Thử lại",), close=False)
    + '</div><div class="card span2"><div class="h">Chứng từ</div>'
    + alert("warn", "Thiếu biên bản giao container.", "Lệnh chỉ hoàn tất khi đủ chứng từ.", ("Tải lên", "Xem yêu cầu"), close=False)
    + "</div></div>" + toasts())

S_LIST_APP = ('<div class="mpad">' + alert("info", "Danh sách vừa có cập nhật.", "", ("Tải lại",), close=False) + "</div>"
    + "".join(f'<div class="mrow"><div class="mono b">{a}</div><div class="sub">{b} · {c}</div><span class="chip">{e}</span></div>'
              for a, b, c, d, e in [("LVT-2026-0412", "Cát Lái → Sóng Thần", "51C-123.45", "", "Đang chạy"),
                                    ("LVT-2026-0414", "Cát Lái → Long Hậu", "51C-246.80", "", "Chờ nhận"),
                                    ("LVT-2026-0415", "ICD Phước Long → Tân Uyên", "chưa có xe", "", "Chưa gán xe")])
    + toasts(mobile=True))

S_DETAIL_APP = ('<div class="mpad">'
    + alert("warn", "Thiếu biên bản giao container.", "Chụp biên bản để hoàn tất lệnh.", ("Chụp ảnh",), close=False)
    + '<div class="card m"><div class="h">LVT-2026-0412</div><dl><dt>Tuyến</dt><dd>Cát Lái → Sóng Thần</dd>'
      '<dt>Xe</dt><dd class=mono>51C-123.45</dd><dt>Giao trước</dt><dd>16:00 hôm nay</dd></dl></div>'
    + '<div class="card m"><div class="h">Quy trình</div>'
    + alert("err", "Không tải được quy trình.", "", ("Thử lại",), close=False) + "</div>"
    + '<button class="cta">Xác nhận đã giao</button></div>' + toasts(mobile=True))

# ---------- CSS (vẽ tự do; giá trị lấy gần DS v2 cho dễ đối chiếu ở vòng 3) ----------
CSS = r"""
.pv{position:relative;
 
 
 color:var(--color-text-primary);font:14px/20px Inter,system-ui,sans-serif}
.pv[data-theme=dark]{
 
 }
.mono{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:13px}
.pad{padding:16px 24px 24px;display:flex;flex-direction:column;gap:16px}.mpad{padding:12px 16px;display:flex;flex-direction:column;gap:12px}
.tb{border:1px solid var(--color-border-secondary);border-radius:12px;overflow:hidden}
table{width:100%;border-collapse:collapse}td,th{padding:11px 16px;border-bottom:1px solid var(--color-border-secondary);text-align:left;font-size:13px}tr:last-child td{border-bottom:0}th{color:var(--color-text-secondary);font-weight:500;background:var(--color-bg-secondary)}
.chip{display:inline-block;font:500 12px/18px Inter;padding:2px 8px;border-radius:999px;background:var(--color-utility-neutral-100);color:var(--color-text-primary)}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:16px}.span2{grid-column:span 2}
.card{border:1px solid var(--color-border-secondary);border-radius:12px;padding:16px;display:flex;flex-direction:column;gap:12px}.card.m{padding:14px}
.card .h{font:600 15px/22px Inter}
dl{display:grid;grid-template-columns:110px 1fr;gap:6px 12px;margin:0;font-size:13px}dt{color:var(--color-text-secondary)}dd{margin:0}
.mrow{padding:12px 16px;border-bottom:1px solid var(--color-border-secondary);display:grid;grid-template-columns:1fr auto;gap:2px 8px}.mrow .b{font-weight:600}.mrow .sub{color:var(--color-text-secondary);font-size:13px;grid-column:1}.mrow .chip{grid-row:1/span 2;grid-column:2;align-self:center}
.cta{height:52px;border:0;border-radius:var(--radius-control);background:var(--color-action-primary);color:var(--color-text-inverse);font:600 16px Inter;margin-top:8px}
.i{flex:none;display:block}
/* ---- màu theo tone ---- */
.ok{--t:var(--color-text-success-primary);--ti:var(--color-fg-success-primary);--tbg:var(--color-bg-success-primary);--tbd:var(--color-border-success_subtle)}.warn{--t:var(--color-text-warning-primary);--ti:var(--color-fg-warning-primary);--tbg:var(--color-bg-warning-primary);--tbd:var(--color-border-warning_subtle)}
.err{--t:var(--color-text-error-primary);--ti:var(--color-fg-error-primary);--tbg:var(--color-bg-error-primary);--tbd:var(--color-border-error_subtle)}.info{--t:var(--color-text-info-primary);--ti:var(--color-fg-info-primary);--tbg:var(--color-bg-info-primary);--tbd:var(--color-border-info_subtle)}
/* ---- Toast (Notification) ---- */
.tz{position:absolute;z-index:5;display:flex;flex-direction:column;gap:8px;width:var(--width-xs);max-width:calc(100% - 2 * var(--grid-margin));right:24px;top:80px}
.pv[data-D4=b] .tz:not(.m){top:auto;bottom:24px}
.pv[data-D4=c] .tz:not(.m){right:auto;left:calc(50% + 120px);transform:translateX(-50%)}
.tz.m{left:12px;right:12px;width:auto;top:52px}
.pv[data-D8=b] .tz.m{top:auto;bottom:76px}
.ts{position:relative;display:flex;gap:12px;align-items:flex-start;padding:12px;border-radius:12px;box-shadow:var(--shadow-xl);overflow:hidden;
 background:var(--color-bg-primary);color:var(--color-text-primary);border:1px solid var(--shadow-xl-border)}
.ts .ib{color:var(--ti);display:grid;place-items:center}
.ts .tx{flex:1;min-width:0;padding-top:1px}.ts .tt{font-weight:600;font-size:14px;line-height:20px;overflow:hidden;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical}
.ts .ds{color:var(--color-text-secondary);font-size:12px;line-height:18px;margin-top:2px}
.ac{display:flex;gap:12px;margin-top:6px}
.lk{border:0;background:none;padding:0;font:600 12px/18px Inter;position:relative;color:var(--color-text-secondary);cursor:pointer}.lk.pri{color:var(--color-text-primary)}
.cl{position:relative;border:0;background:none;padding:2px;color:var(--color-text-secondary);cursor:pointer;display:grid;place-items:center;margin:-2px -2px 0 0;opacity:.8}
.tm{position:absolute;left:0;bottom:0;height:4px;width:62%;background:var(--ti);display:none}
.pv[data-D6=b] .tm{display:block}
/* D1 kiểu toast: a đảo nền (Astryx) · b trắng + icon màu (Untitled) · c nền nhạt theo tone */
.pv[data-D1=a] .ts{background:var(--color-bg-primary_solid);color:var(--color-text-inverse);border-color:transparent}
.pv[data-D1=a] .ts .ds,.pv[data-D1=a] .ts .lk,.pv[data-D1=a] .ts .cl{color:color-mix(in srgb,var(--color-text-inverse) 72%,transparent)}
.pv[data-D1=a] .ts .lk.pri{color:var(--color-text-inverse);text-decoration:underline}
.pv[data-D1=a] .ts .ib{color:color-mix(in srgb,var(--ti) 55%,var(--color-text-inverse))}
.pv[data-D1=a] .ts.err{background:var(--color-bg-error-solid);color:var(--color-text-white)}.pv[data-D1=a] .ts.err .ib,.pv[data-D1=a] .ts.err .ds,.pv[data-D1=a] .ts.err .lk,.pv[data-D1=a] .ts.err .cl{color:var(--color-text-white)}
.pv[data-D1=c] .ts{background:var(--tbg);border-color:var(--tbd);box-shadow:var(--shadow-xl)}
.pv[data-D1=c] .ts .tt{color:var(--t)}
.cl::after,.lk::after{content:"";position:absolute;left:50%;top:50%;width:24px;height:24px;min-width:100%;transform:translate(-50%,-50%)}
.pv[data-platform=mobile] .cl::after,.pv[data-platform=mobile] .lk::after{width:44px;height:44px}
.pv[data-platform=mobile] .ts .ac{gap:24px}
/* nút trong alert trên app: bậc SM 36 + vùng bấm 44 */
.pv[data-platform=mobile] .al .bt{height:36px;position:relative}.pv[data-platform=mobile] .al .bt::after{content:"";position:absolute;inset:-4px 0}
/* Type Icon / Avatar / Progress */
.nt{--t:var(--color-text-primary);--ti:var(--color-fg-tertiary);--tbg:var(--color-bg-tertiary);--tbd:var(--color-border-secondary)}
.av{width:32px;height:32px;border-radius:999px;background:var(--color-accent-bg);color:var(--color-accent-fg);font:600 12px/32px Inter;text-align:center;position:relative;flex:none;margin:-6px 0 -6px -2px}
.pv[data-theme=dark] .av{background:var(--color-accent-bg);color:var(--color-accent-fg)}
.av .on{position:absolute;right:-1px;bottom:-1px;width:10px;height:10px;border-radius:999px;background:var(--color-fg-success-secondary);border:2px solid var(--color-bg-primary)}
.pg{display:flex;align-items:center;gap:10px;margin-top:8px}.pb{flex:1;height:6px;border-radius:999px;background:var(--color-bg-quaternary);overflow:hidden}
.pb i{display:block;height:100%;background:var(--color-fg-info-primary);border-radius:999px}.pg span{font:500 12px/18px Inter;color:var(--color-text-secondary);font-variant-numeric:tabular-nums;min-width:32px;text-align:right}
.pg+.ds{font-size:12px;margin-top:2px}
/* ---- Alert ---- */
.al{display:flex;gap:12px;align-items:flex-start;padding:12px;border-radius:10px;border:1px solid var(--tbd);background:var(--tbg)}
.al .ib{color:var(--ti);display:grid;place-items:center}
.al .tx{flex:1;min-width:0;padding-top:1px}.al .tt{font-weight:600;color:var(--t)}.al .ds{font-size:12px;line-height:18px;color:var(--color-text-primary);margin-top:2px}
.al .ac{margin:0;align-self:center;flex:none}
.bt{height:32px;padding:0 12px;border-radius:8px;border:1px solid var(--color-border-secondary);background:var(--color-bg-primary);color:var(--color-text-primary);font:600 13px Inter;cursor:pointer}
.al .cl{align-self:flex-start}
/* D5 hành động: a dưới chữ · b căn phải cùng hàng */
.pv[data-D5=a] .al{flex-wrap:wrap}.pv[data-D5=a] .al .ac{order:3;flex-basis:100%;padding-left:32px;margin-top:8px}
.pv[data-D5=a] .al .cl{order:2}
.al.stack{flex-wrap:wrap}.al.stack .ac{order:3;flex-basis:100%;padding-left:32px;margin-top:8px}.pv[data-D3=a] .al.stack .ac{padding-left:44px}
/* D2 kiểu alert: a nền nhạt + viền · b trắng + vạch trái · c trắng + viền màu */
.pv[data-D2=b] .al{background:var(--color-bg-primary);border-color:var(--color-border-secondary);border-left:4px solid var(--ti);padding-left:12px}
.pv[data-D2=b] .al .tt{color:var(--color-text-primary)}
.pv[data-D2=c] .al{background:var(--color-bg-primary);border-color:var(--t)}.pv[data-D2=c] .al .tt{color:var(--color-text-primary)}
/* D3 icon: a vòng nền (featured) · b icon trần */
.pv[data-D3=a] .ib{width:32px;height:32px;border-radius:999px;background:var(--tbg);margin:-6px 0 -6px -2px;box-shadow:0 0 0 4px color-mix(in srgb,var(--tbg) 45%,transparent)}
.pv[data-D3=a][data-D1=a] .ts .ib{background:color-mix(in srgb,var(--color-text-inverse) 14%,transparent);box-shadow:none}
.pv[data-D3=a] .ib .i{width:20px;height:20px}
/* ---- Banner toàn trang (D7) ---- */
.bn{display:flex;align-items:center;gap:10px;padding:8px 24px;background:var(--color-bg-warning-primary);color:var(--color-text-warning-primary);border-bottom:1px solid var(--color-border-warning_subtle);font-size:13px}
.bn span{flex:1}.bn b{font-weight:600}.bn .bt{height:28px;border-color:var(--color-border-warning_subtle);background:transparent;color:var(--color-text-warning-primary)}
.pv[data-platform=mobile] .bn{padding:8px 16px}
.pv[data-platform=mobile] .grid2{grid-template-columns:1fr}
"""

# hình mẫu nhỏ cho thẻ phương án / ý tưởng (cùng CSS, kèm data-* cục bộ qua wrapper .pv lồng)
def mini(attrs, inner):
    a = " ".join(f'data-{k}="{v}"' for k, v in attrs.items())
    return f'<div class="pv" {a} style="padding:4px;max-width:420px">{inner}</div>'

T_OK = toast("ok", "Đã gửi lệnh LVT-2026-0412", "Tài xế nhận được thông báo trên app.", ("Xem lệnh",), timer=True)
T_UNDO = toast("ok", "Đã huỷ lệnh LVT-2026-0413", "", ("Hoàn tác",))
A_ERR = alert("err", "Không tải được quy trình.", "Phần còn lại của lệnh vẫn dùng bình thường.", ("Thử lại",), close=False)
A_INFO = alert("info", "Danh sách vừa có cập nhật.", "", ("Tải lại",), close=False)
BASE = {"D1": "b", "D2": "a", "D3": "b", "D4": "a", "D5": "b", "D6": "a", "D7": "a", "D8": "a"}
def m(over, inner):
    return mini({**BASE, **over}, inner)

decisions = [
 {"id": "D1", "title": "Kiểu Notification (toast)", "why": "Toast hiện đè lên màn — nền quyết định toast nổi tới đâu và có lẫn với nội dung không.",
  "source": "Astryx: design.md › Feedback & Status (toast nền đảo) · Untitled: Notifications (nền trắng, icon màu)",
  "options": [
   {"label": "Nền tối đảo màu", "desc": "Nổi nhất trên màn sáng; toast lỗi nền đỏ. Như Astryx hiện tại.", "preview": m({"D1": "a"}, T_OK), "ideas": ["I5", "I7"]},
   {"label": "Nền trắng, icon màu", "desc": "Nhẹ, đọc như thẻ; tone nằm ở icon. Như Untitled.", "rec": True, "preview": m({"D1": "b"}, T_OK), "ideas": ["I3", "I8"]},
   {"label": "Nền nhạt theo tone", "desc": "Thấy ngay loại tin; dễ lẫn với Alert trong trang.", "preview": m({"D1": "c"}, T_OK), "ideas": ["I4"]}],
  "untitled": m({"D1": "b", "D3": "a"}, T_OK), "untitledNote": "trắng + featured icon",
  "astryx": m({"D1": "a"}, toast("ok", "Đã lưu thay đổi", "", (), timer=False)), "astryxNote": "Toast nền đảo 360px, bo 12"},
 {"id": "D2", "title": "Kiểu Alert (trong trang)", "why": "Alert nằm cố định trong luồng nội dung (banner cập nhật GR-27, lỗi khối có Thử lại).",
  "source": "cross-process-flow 1.x · GR-27 · Astryx Banner",
  "options": [
   {"label": "Nền nhạt + viền màu", "desc": "Rõ loại tin nhất. Như Untitled và Astryx.", "rec": True, "preview": m({"D2": "a"}, A_ERR), "ideas": ["I4"]},
   {"label": "Trắng + vạch trái", "desc": "Gọn, ít màu khi nhiều alert trên một màn.", "preview": m({"D2": "b"}, A_ERR), "ideas": ["I2", "I10"]},
   {"label": "Trắng + viền màu", "desc": "Nhẹ nhất; tone dựa vào icon và viền.", "preview": m({"D2": "c"}, A_ERR)}],
  "untitled": m({"D2": "a", "D3": "a"}, A_ERR), "untitledNote": "nền nhạt, featured icon",
  "astryx": m({"D2": "a"}, A_ERR), "astryxNote": "Banner status info/success/warning/error"},
 {"id": "D3", "title": "Icon", "why": "Icon mang nghĩa (không chỉ màu) — kiểu icon quyết định độ nặng của khối.",
  "source": "Untitled: featured icon · Astryx: icon trần",
  "options": [
   {"label": "Vòng nền (featured)", "desc": "Như Untitled; nổi, tốn chỗ hơn.", "preview": m({"D3": "a"}, T_OK), "ideas": ["I3"]},
   {"label": "Icon trần 20", "desc": "Gọn, hợp bảng dày dữ liệu.", "rec": True, "preview": m({"D3": "b"}, T_OK)}]},
 {"id": "D4", "title": "Vị trí toast — Web", "why": "CMP-01 đang ghi góc trên phải; Untitled cho phép trên hoặc dưới phải, giữ một chỗ cho cả sản phẩm.",
  "source": "CMP-01 · Untitled Notifications (Positioning)",
  "options": [
   {"label": "Trên phải", "desc": "Theo CMP-01 hiện tại; gần chuông và tài khoản.", "rec": True, "preview": "<div style='font:13px Inter;padding:8px'>Mở màn demo để xem vị trí.</div>"},
   {"label": "Dưới phải", "desc": "Không che header, nút lọc; xa mắt hơn.", "preview": "<div style='font:13px Inter;padding:8px'>Mở màn demo để xem vị trí.</div>", "ideas": ["I6"]},
   {"label": "Giữa trên", "desc": "Dễ thấy nhất; che tiêu đề trang.", "preview": "<div style='font:13px Inter;padding:8px'>Mở màn demo để xem vị trí.</div>"}]},
 {"id": "D5", "title": "Chỗ đặt nút hành động trong Alert", "why": "Alert lỗi khối có Thử lại, banner cập nhật có Tải lại.",
  "source": "cross-process-flow view-process #1 · GR-27",
  "options": [
   {"label": "Dưới chữ", "desc": "Như Untitled floating; chữ dài không bị bóp.", "preview": m({"D5": "a"}, A_ERR)},
   {"label": "Căn phải cùng hàng", "desc": "Gọn một dòng, hợp alert ngắn.", "rec": True, "preview": m({"D5": "b"}, A_ERR), "ideas": ["I9"]}]},
 {"id": "D6", "title": "Đếm giờ tự ẩn của toast", "why": "CMP-01 tự ẩn sau 3 giây; người dùng không biết còn bao lâu để bấm Hoàn tác.",
  "source": "CMP-01 · ý tưởng I1",
  "options": [
   {"label": "Không hiện", "desc": "Sạch; dừng đếm khi rê chuột.", "rec": True, "preview": m({"D6": "a"}, T_UNDO)},
   {"label": "Thanh mỏng ở đáy", "desc": "Thấy thời gian còn lại, hợp toast có Hoàn tác.", "preview": m({"D6": "b"}, T_UNDO), "ideas": ["I1"]}]},
 {"id": "D7", "title": "Banner toàn trang (sự cố hệ thống)", "why": "Untitled có full-width banner cho sự cố phiên (mất kết nối, bảo trì) — sản phẩm chưa có chỗ báo lỗi mạng kéo dài.",
  "source": "Untitled Alerts (Full-width) · E-common-008/009",
  "options": [
   {"label": "Dựng, dính đầu vùng nội dung", "desc": "Một dải mảnh, không tự ẩn, có Thử lại.", "rec": True, "preview": mini(BASE, banner(False))},
   {"label": "Chưa dựng lần này", "desc": "Dùng toast lỗi như hiện tại.", "preview": "<div style='font:13px Inter;padding:8px;color:var(--color-text-tertiary)'>Không có banner.</div>"}]},
 {"id": "D8", "title": "Vị trí toast — App", "why": "CMP-01 Mobile: vị trí chưa có chuẩn. Untitled khuyên trên đầu vì dưới dễ nằm dưới ngón tay và thanh tab.",
  "source": "CMP-01 › Mobile · Untitled Notifications",
  "options": [
   {"label": "Trên, dưới thanh trạng thái", "desc": "Không đè nút chính chân màn.", "rec": True, "preview": "<div style='font:13px Inter;padding:8px'>Mở màn app để xem.</div>"},
   {"label": "Dưới, trên thanh tab", "desc": "Kiểu snackbar Android; gần ngón cái để bấm Hoàn tác.", "preview": "<div style='font:13px Inter;padding:8px'>Mở màn app để xem.</div>", "ideas": ["I8"]}]},
]

ideas = [
 {"id": "I1", "source": "Dribbble", "url": "https://dribbble.com/dsmotaa/collections/4891147-Notifications-component",
  "title": "Toast có thanh đếm giờ", "why": "Bộ sưu tập toast concept cho web app: thanh mỏng cho biết toast còn hiện bao lâu — hợp toast có Hoàn tác.",
  "preview": m({"D6": "b"}, T_UNDO)},
 {"id": "I2", "source": "Dribbble", "url": "https://dribbble.com/search/alert-banner",
  "title": "Inline alert vạch trái", "why": "\"Inline Alerts Exploration\": nền trắng, vạch màu bên trái — đọc như một dòng ghi chú, không làm loãng màn nhiều dữ liệu.",
  "preview": m({"D2": "b"}, A_ERR)},
 {"id": "I3", "source": "Dribbble", "url": "https://dribbble.com/LukeDowding/collections/6840272-Alerts-Notifications",
  "title": "Toast thẻ trắng, featured icon", "why": "Bộ Alerts/Notifications (có shot \"Confirmation toast — Untitled UI\"): thẻ trắng, icon trong vòng nền, mô tả phụ + link hành động.",
  "preview": m({"D1": "b", "D3": "a"}, T_OK)},
 {"id": "I4", "source": "Dribbble", "url": "https://dribbble.com/thiagoalmmeida/collections/6539201-Alerts",
  "title": "Alert nền nhạt theo tone", "why": "Bộ Alerts kiểu \"Cozy Design System\": nền pastel theo loại tin, tiêu đề cùng màu tone.",
  "preview": m({"D1": "c", "D2": "a"}, toast("warn", "Lệnh LVT-2026-0415 chưa có xe", "", ("Gán xe",)))},
 {"id": "I5", "source": "Dribbble", "url": "https://dribbble.com/DimaMoistsrapishvili/collections/4626919-Notification",
  "title": "Toast tối, có Hoàn tác", "why": "\"Toast & NUX b2b\": toast đảo nền tối, một nút chữ gạch chân để hoàn tác — rất gần Astryx hiện tại.",
  "preview": m({"D1": "a"}, T_UNDO)},
 {"id": "I6", "source": "21st.dev", "url": "https://21st.dev/@felipemenezes098/components/banner-12.md",
  "title": "Nhiều thông báo xếp chồng", "why": "\"Stacked Notification Banners\": mỗi tin có icon, tiêu đề, nút đóng riêng; đóng tin này không ảnh hưởng tin khác. Untitled khuyên tối đa 3.",
  "preview": m({}, toast("info", "Đang xuất 128 lệnh ra Excel…", "", (), timer=False) + "<div style='height:8px'></div>" + toast("ok", "Đã gửi lệnh LVT-2026-0412", "", ()))},
 {"id": "I7", "source": "21st.dev", "url": "https://21st.dev/@reshaped/components/reshaped-toast.md",
  "title": "Toast Reshaped — mặc định đảo nền", "why": "Mặc định nền đảo, thêm neutral/primary/positive/critical; hành động có thể xếp dọc khi chữ dài.",
  "preview": m({"D1": "a", "D3": "b"}, toast("err", "Không gửi được lệnh", "Kiểm tra kết nối mạng rồi thử lại.", ("Thử lại",), timer=False))},
 {"id": "I8", "source": "21st.dev", "url": "https://21st.dev/@wensity/components/toast.md",
  "title": "Toast 4 loại + nút hành động", "why": "success / error / warning / info, có nút hành động, đặt được vị trí — gần nhất với 4 loại của CMP-01.",
  "preview": m({"D1": "b"}, toast("info", "Lệnh LVT-2026-0412 vừa đổi tài xế", "", ("Xem",)))},
 {"id": "I9", "source": "21st.dev", "url": "https://21st.dev/@lavikatiyar/components/alert-banner.md",
  "title": "Alert banner có nút bên phải", "why": "Alert đóng được, có hành động căn phải cùng hàng — hợp banner \"vừa có cập nhật\" + Tải lại.",
  "preview": m({"D5": "b"}, A_INFO)},
 {"id": "I10", "source": "Red Hat UX", "url": "https://ux.redhat.com/patterns/alert/style/",
  "title": "Alert trong trang — hệ thống lớn", "why": "Red Hat: alert inline có vạch màu, toast có thể ở lại tới khi đóng; quy định rõ khi nào được tự ẩn.",
  "preview": m({"D2": "b", "D5": "a"}, alert("warn", "Thiếu biên bản giao container.", "Lệnh chỉ hoàn tất khi đủ chứng từ.", ("Tải lên", "Xem yêu cầu"), close=False))},
 {"id": "I11", "source": "Screens Design (màn app thật)", "url": "https://screensdesign.com/explore/ui-elements/toasts/",
  "title": "Toast app ở trên đầu", "why": "Bộ màn app thật: toast trên cùng xác nhận thao tác, không đè nút chính ở chân màn — cùng hướng Untitled khuyên cho mobile.",
  "preview": m({"D1": "b"}, toast("ok", "Đã nhận lệnh LVT-2026-0412", "", (), timer=False))},
]

presets = [
 {"id": "rec", "label": "Đề xuất", "pick": {d["id"]: chr(97 + next(i for i, o in enumerate(d["options"]) if o.get("rec"))) for d in decisions}},
 {"id": "untitled", "label": "Theo Untitled", "pick": {"D1": "b", "D2": "a", "D3": "a", "D4": "a", "D5": "a", "D6": "a", "D7": "a", "D8": "a"}},
 {"id": "astryx", "label": "Astryx hiện tại", "pick": {"D1": "a", "D2": "a", "D3": "b", "D4": "a", "D5": "b", "D6": "a", "D7": "b", "D8": "a"}},
]
for i in ideas:
    pick = dict(BASE)
    for d in decisions:
        for k, o in enumerate(d["options"]):
            if i["id"] in (o.get("ideas") or []):
                pick[d["id"]] = chr(97 + k)
    pr = {"id": i["id"], "label": f'Ý tưởng {i["id"]} · {i["source"].split(" (")[0]}', "pick": pick}
    if i["id"] in ("I8", "I11"):
        pr["screen"] = 2
    presets.append(pr)

page = {
 "component": "Alert & Notification",
 "slug": "alert-notification",
 "title": "Alert Notification Review",
 "subtitle": "Base component · nhóm A (dùng chung web và app; khác bề rộng và vị trí) · vòng 1 Brainstorm",
 "round": "brainstorm",
 "refs": {
  "untitled": {"summary": "Hai component: <mark>Alerts</mark> (floating trong cột nội dung, full-width cho sự cố phiên; 6 màu) và <mark>Notifications</mark> (toast 504px, 9 type: icon theo tone, avatar, ảnh, tiến độ; luôn có nút đóng; tối đa 3 tin; mobile hiện trên đầu).",
               "source": "untitledui.com/components/alerts · /notifications (bản free React không có code hai component này)"},
  "astryx": {"summary": "<mark>Banner</mark> bền trong trang (info/success/warning/error, đóng được, vùng hành động) và <mark>Toast</mark> tạm thời nền đảo 360px bo 12, loại default/error.",
             "source": "design/design.md › Feedback & Status · CMP-01 (Figma 172:56853)"},
  "usage": ["Toast sau hành động — CMP-01 (mọi feature), vd cross-process-flow «Toast gửi thành công»",
            "Banner «Danh sách / Quy trình vừa có cập nhật» — GR-27, cross-process-flow search-process, view-process",
            "Banner lỗi khối có Thử lại — cross-process-flow view-process #1",
            "App: banner dưới header sheet sơ đồ — cross-process-flow (Mobile)"],
  "platform": "Nhóm A (DEC-279): cùng cấu tạo, số đo theo mode Platform. Vị trí toast là quy định cấp màn (D4, D8). Notification Center (CMP-02) là component Application riêng, ngoài lần này."},
 "css": CSS,
 "states": [{"key": "default", "label": "Mặc định"}, {"key": "action", "label": "Có Hoàn tác"}, {"key": "error", "label": "Toast lỗi"}, {"key": "avatar", "label": "Avatar"}, {"key": "icon", "label": "Icon"}, {"key": "progress", "label": "Tiến trình"},
            {"key": "stack", "label": "3 tin chồng"}, {"key": "long", "label": "Chữ dài"}],
 "ideas": ideas, "decisions": decisions, "presets": presets,
 "screens": [
  {"id": "list-web", "name": "Danh sách lệnh vận tải", "device": "web", "width": 1280, "nav": "Lệnh vận tải", "title": "Lệnh vận tải",
   "note": "Khối xanh = Alert «vừa có cập nhật» (GR-27) · toast ở vị trí theo D4.", "html": S_LIST_WEB},
  {"id": "detail-web", "name": "Chi tiết lệnh", "device": "web", "width": 1280, "nav": "Lệnh vận tải", "crumb": "Lệnh vận tải", "title": "LVT-2026-0412",
   "note": "Alert trong từng khối: thành công (đóng được), lỗi khối có Thử lại, cảnh báo thiếu chứng từ có 2 hành động.", "html": S_DETAIL_WEB},
  {"id": "list-app", "name": "Lệnh của tôi", "device": "mobile", "title": "Lệnh vận tải", "nav": "Lệnh",
   "note": "App tài xế: Alert cập nhật dưới header; toast theo D8.", "html": S_LIST_APP},
  {"id": "detail-app", "name": "Chi tiết lệnh", "device": "mobile", "title": "LVT-2026-0412", "back": True, "tabs": False, "nav": "Lệnh",
   "note": "Nút chính chân màn — xem toast có đè nút khi đặt dưới (D8 = B).", "html": S_DETAIL_APP}],
}
# ================= Vòng 2 — Preview (tổ hợp user chốt 28/10) =================
ANS = json.loads((Path(__file__).parent / "answers.json").read_text())
PICK = {d["id"]: chr(97 + ANS[f"brainstorm-{d['id']}"]["choice"]) for d in decisions}
TONES = [("ok", "Thành công"), ("info", "Thông tin"), ("warn", "Cảnh báo"), ("err", "Lỗi")]
T_COPY = {"ok": ("Đã gửi lệnh LVT-2026-0412", "Tài xế nhận được thông báo trên app.", ("Xem lệnh",)),
          "info": ("Lệnh LVT-2026-0412 vừa đổi tài xế", "Lê Minh Châu thay Trần Văn Bình.", ("Xem",)),
          "warn": ("Lệnh LVT-2026-0415 chưa có xe", "Gán xe trước 14:00 để kịp giờ giao.", ("Gán xe",)),
          "err": ("Không gửi được lệnh", "Kiểm tra kết nối mạng rồi thử lại.", ("Thử lại",))}
A_COPY = {"ok": ("Tài xế đã nhận lệnh lúc 08:15.", "", ()),
          "info": ("Danh sách vừa có cập nhật.", "", ("Tải lại",)),
          "warn": ("Thiếu biên bản giao container.", "Lệnh chỉ hoàn tất khi đủ chứng từ.", ("Tải lên",)),
          "err": ("Không tải được quy trình.", "Phần còn lại của lệnh vẫn dùng bình thường.", ("Thử lại",))}

def grid(mobile):
    w = "100%" if mobile else "var(--width-xs)"
    cell = lambda lab, inner: (f'<div style="display:flex;flex-direction:column;gap:6px;width:{w}">'
                               f'<div style="font:500 11px Inter;color:var(--color-text-tertiary)">{lab}</div>{inner}</div>')
    row = lambda title, cells: (f'<div style="font:600 13px Inter;margin:18px 0 8px">{title}</div>'
                                f'<div style="display:flex;flex-wrap:wrap;gap:16px">{"".join(cells)}</div>')
    tz = lambda inner: f'<div class="tz static{" m" if mobile else ""}">{inner}</div>'
    h = row("Notification — 4 loại, có mô tả và hành động", [cell(l, tz(toast(t, *T_COPY[t]))) for t, l in TONES])
    h += row("Notification — Icon (icon nội dung, tông trung tính)", [
        cell("Xe / chuyến", tz(t_icon("truck", "Xe 51C-123.45 đã vào cổng Cát Lái", "Lệnh LVT-2026-0412 · 09:42", ("Xem lệnh",)))),
        cell("Chứng từ", tz(t_icon("file", "Biên bản giao container đã được ký", "Lệnh LVT-2026-0412", ("Xem",))))])
    h += row("Notification — Avatar (do người khác làm)", [
        cell("Một hành động", tz(t_avatar("LC", "Lê Minh Châu đã nhận lệnh LVT-2026-0413", "2 phút trước", ("Xem lệnh",)))),
        cell("Hai hành động", tz(t_avatar("TB", "Trần Văn Bình gửi 3 ảnh chứng từ", "Lệnh LVT-2026-0412 · vừa xong", ("Xem ảnh", "Để sau"), online=False)))])
    h += row("Notification — Tiến trình (không tự ẩn khi đang chạy)", [
        cell("Tải lên", tz(t_prog("upload", "Đang tải lên biên bản giao container.pdf", 64, "1,2 MB / 1,9 MB"))),
        cell("Xuất", tz(t_prog("download", "Đang xuất 128 lệnh ra Excel", 40, "Khoảng 20 giây nữa"))),
        cell("Nhập", tz(t_prog("import", "Đang nhập 52 lệnh từ tệp lenh-thang-10.xlsx", 80, "42 / 52 lệnh"))),
        cell("Xong — tự ẩn, có tải xuống", tz(t_prog("download", "Đã xuất 128 lệnh ra Excel", None, "lenh-van-tai-28-10.xlsx · 312 KB", ("Tải xuống",), tone="ok"))),
        cell("Lỗi — giữ tới khi đóng", tz(t_prog("upload", "Không tải lên được biên bản", None, "Mất kết nối khi đang tải lên.", ("Thử lại",), tone="err")))])
    h += row("Notification — các dạng", [
        cell("Chỉ tiêu đề", tz(toast("ok", "Đã lưu thay đổi", "", ()))),
        cell("Có Hoàn tác", tz(toast("ok", "Đã huỷ lệnh LVT-2026-0413", "", ("Hoàn tác",)))),
        cell("Chữ dài — tiêu đề tối đa 2 dòng", tz(toast("ok", LONG, "", ("Xem lệnh",)))),
        ])
    h += row("Alert — 4 loại", [cell(l, alert(t, *A_COPY[t], close=(t == "ok"))) for t, l in TONES])
    h += row("Alert — các dạng", [
        cell("Hai hành động", alert("warn", "Thiếu biên bản giao container.", "Lệnh chỉ hoàn tất khi đủ chứng từ.", ("Tải lên", "Xem yêu cầu"), close=False)),
        cell("Đóng được", alert("info", "Bạn đang xem lệnh của chi nhánh Bình Dương.", "", (), close=True)),
        cell("Chữ dài — xuống dòng, không cắt", alert("err", "Không tải được quy trình của lệnh LVT-2026-0412 do máy chủ quy trình không phản hồi.", "Phần còn lại của lệnh vẫn dùng bình thường; dữ liệu đã nhập không bị mất.", ("Thử lại",), close=False))])
    a = " ".join(f'data-{k}="{x}"' for k, x in PICK.items())
    return f'<div class="pv" {a} data-platform="{"mobile" if mobile else "web"}" style="padding:16px">{h}</div>'

CSS_PREVIEW = ".tz.static{position:static;width:100%;transform:none}"

page["css"] = CSS + CSS_PREVIEW
page["round"] = "foundation"
page["subtitle"] = "Base component · nhóm A · vòng 2 Preview — tổ hợp đã chốt: " + " · ".join(f"{k} {v.upper()}" for k, v in PICK.items())
page["preview"] = {"version": "2", "changes": "đã áp quyết định vòng 3: vùng bấm 24/44, nút alert app 36, viền alert đậm, padding 12, chữ phụ 12, thanh giờ 4, icon 20",
                   "pick": PICK,
                   "blocks": [{"title": "Web", "platform": "web", "note": "Toast 384 · alert theo cột nội dung", "html": grid(False)},
                              {"title": "Mobile", "platform": "mobile", "note": "Toast và alert rộng 361 (lề 16)",
                               "frames": [grid(True)]}]}

# Khai giá trị preview — vòng 3 đối chiếu foundation (ds-foundation-check.py)
V = []
def v(part, prop, value, **kw):
    V.append({"part": part, "prop": prop, "value": value, **kw})
for plat in ("Web", "Mobile"):
    v("Toast", "width", 400 if plat == "Web" else 361, platform=plat)
    v("Toast", "padding-y", 12, platform=plat); v("Toast", "padding-left", 12, platform=plat); v("Toast", "padding-right", 12, platform=plat)
    v("Toast", "gap", 12, platform=plat); v("Toast", "radius", 12, platform=plat)
    v("Toast close", "size", 20, platform=plat, interactive=True, hitArea=24 if plat == "Web" else 44)
    v("Toast action", "height", 18, platform=plat, interactive=True, hitArea=24 if plat == "Web" else 44)
    v("Alert", "padding-y", 12, platform=plat); v("Alert", "padding-x", 12, platform=plat); v("Alert", "gap", 12, platform=plat); v("Alert", "radius", 10, platform=plat)
    v("Alert button", "height", 32 if plat == "Web" else 36, platform=plat, control=True, interactive=True, hitArea=32 if plat == "Web" else 44)
    v("Alert button", "padding-x", 12, platform=plat); v("Alert button", "radius", 8, platform=plat)
    v("Toast stack", "gap", 8, platform=plat)
    v("Toast zone", "margin", 24 if plat == "Web" else 12, platform=plat)
v("Toast", "shadow", "shadow/xl"); v("Toast timer", "height", 4)
v("Featured icon", "size", 32); v("Featured icon", "icon-size", 20); v("Featured icon ring", "width", 4); v("Icon", "icon-size", 20); v("Close icon", "icon-size", 16)
v("Title", "font-size", 14); v("Title", "line-height", 20); v("Title", "font-weight", 600)
v("Description", "font-size", 12); v("Description", "line-height", 18)
v("Action", "font-size", 12); v("Action", "font-weight", 600)
v("Avatar", "size", 32); v("Avatar status", "size", 10); v("Progress", "height", 6); v("Progress", "radius", 9999); v("Progress", "gap", 10); v("Percent", "font-size", 12); v("Meta", "font-size", 12)
v("Toast", "background", "#FFFFFF"); v("Toast", "border-color", "#E5E5E5", role="decorative", on="#FFFFFF")
v("Title", "color", "#171717", role="text", on="#FFFFFF"); v("Description", "color", "#737373", role="text", on="#FFFFFF")
v("Action secondary", "color", "#737373", role="text", on="#FFFFFF"); v("Close icon", "color", "#737373", role="icon", on="#FFFFFF")
for t, (txt, ic_, bg, bd) in {"ok": ("#1B7542", "#348D57", "#E8F5EC", "#93CFA6"), "warn": ("#8A5300", "#A56A21", "#FFF3DC", "#E3B87A"),
                               "err": ("#B42318", "#D23C2E", "#FDECEC", "#FFA19C"), "info": ("#1F4FB8", "#3468D7", "#E7EFFD", "#93B9FF")}.items():
    v(f"Featured icon {t}", "background", bg)
    v(f"Icon {t}", "color", ic_, role="icon", on=bg, state=t)
    v(f"Alert {t}", "border-color", txt, role="border", on="#FFFFFF", state=t)
    v(f"Timer {t}", "background", ic_, role="fill", on="#FFFFFF", state=t)
v("Avatar", "background", "#E7EFFD"); v("Avatar initials", "color", "#1F4FB8", role="text", on="#E7EFFD")
v("Avatar status", "background", "#348D57", role="fill", on="#FFFFFF")
v("Icon neutral", "color", "#737373", role="icon", on="#F5F5F5"); v("Featured icon neutral", "background", "#F5F5F5")
v("Progress track", "background", "#F5F5F5", role="decorative", on="#FFFFFF"); v("Progress fill", "background", "#3468D7", role="fill", on="#F5F5F5")
v("Percent", "color", "#737373", role="text", on="#FFFFFF")
page["values"] = V

# ================= Vòng 5 — Review Figma (3 agent, 28/10) =================
page["round"] = "review"
page["figma"] = {"url": "https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=6862-203175", "label": "Section Alerts & notifications (+ Demo 6862:204019)"}
page["reviews"] = [
 {"id": "R1", "agent": "accessibility", "severity": "Cao", "node": "6862:202736", "changesLook": False,
  "text": "<b>2.2.1 — toast có nút hành động tự ẩn sau 3 giây</b> (CMP-01): người dùng bàn phím, trình đọc màn hình không kịp tới nút Xem lệnh / Hoàn tác; trên app không có rê chuột để dừng đếm.",
  "fix": "Toast có hành động: tối thiểu 10 giây (hoặc không tự ẩn), app dừng đếm khi chạm giữ và khi TalkBack/VoiceOver bật; Hoàn tác làm lại được ở chỗ khác. Sửa = ghi luật vào CMP-01 + spec (không đổi hình)."},
 {"id": "R2", "agent": "visual-reviewer", "severity": "Cao", "node": "6862:203392", "changesLook": True,
  "text": "<b>Toast trắng trên nền trắng tách nền yếu</b> — chỉ có bóng elev/2, ở góc dưới phải dễ bị bỏ lỡ; trên app gần như hoà vào danh sách.",
  "fix": "Đổi bóng sang elev/3 (không đổi nền, không đổi vị trí)."},
 {"id": "R3", "agent": "visual-reviewer", "severity": "Trung", "node": "6862:203392", "changesLook": True,
  "text": "<b>Alert viền đậm nổi hơn cả tiêu đề trang</b> — Alert Info «Danh sách vừa có cập nhật» nổi quá mức quan trọng; 2 alert viền đỏ/cam cùng màn tranh điểm nhìn.",
  "fix": "Info dùng viền nhạt `border/info_subtle` (đạt 3:1 không bắt buộc vì icon + chữ đã báo loại tin), giữ viền đậm cho Warning/Error; hoặc ghi luật tối đa 1 alert viền đậm mỗi vùng."},
 {"id": "R4", "agent": "visual-reviewer", "severity": "Trung", "node": "6862:203529", "changesLook": True,
  "text": "<b>Tiêu đề web nét 500, app nét 600</b> — dùng `type/label` theo DEC-133 nên tiêu đề toast/alert trên web nhìn như chữ thường; preview duyệt là 600 ở cả hai.",
  "fix": "Dùng text style nét 600 cho tiêu đề (vd thêm `type/label-strong` 14/20 600) — cần thêm 1 text style foundation."},
 {"id": "R5", "agent": "visual-reviewer", "severity": "Thấp", "node": "6862:203147", "changesLook": True,
  "text": "<b>Alert 2 nút cùng tông</b> — «Tải lên» và «Xem yêu cầu» ngang hàng, không thấy hành động chính.",
  "fix": "Nút đầu Secondary, nút thứ hai Link Gray (giống toast)."},
 {"id": "R6", "agent": "accessibility", "severity": "Trung", "node": "6862:203176", "changesLook": True,
  "text": "<b>2.5.8 app — 2 link trong toast cách 12</b>, vùng bấm 44 chồng nhau (spec ghi 24).",
  "fix": "Khoảng cách link đọc biến theo mode (web 12, app 24) — cần biến Platform mới hoặc dùng biến có sẵn đúng giá trị."},
 {"id": "R7", "agent": "accessibility", "severity": "Thấp", "node": "6862:202736", "changesLook": True,
  "text": "<b>Tiêu đề toast cắt «…» sau 2 dòng</b> trong khi toast tự ẩn — phần bị cắt không đọc lại được ở đâu.",
  "fix": "Không cắt tiêu đề (chỉ cắt mô tả); hoặc giữ cắt và ghi luật «tiêu đề toast ≤ 80 ký tự»."},
 {"id": "R8", "agent": "uxui-reviewer", "severity": "Thấp", "node": "6862:203412", "changesLook": False,
  "text": "<b>GR-27 «vừa có cập nhật» dùng tone nào?</b> GR-27 nói tông trung tính; Alert chỉ có 4 Tone, demo đang dùng Info.",
  "fix": "Ghi GR-27 dùng Tone = Info (không thêm Tone Neutral)."},
 {"id": "R9", "agent": "uxui-reviewer", "severity": "Cao", "node": "6862:202736", "changesLook": False,
  "text": "<b>CMP-01 và GR-15 Loại 3 còn luật cũ</b> — «góc trên phải», «toast lỗi tự ẩn 3 giây» — mâu thuẫn DEC-286.",
  "fix": "Sửa CMP-01 (đã trình bảng Trước → Sau trong chat) và GR-15 Loại 3 cùng lượt: dưới phải / trên thanh tab, lỗi và tiến trình không tự ẩn."},
]

OUT.parent.mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_lib"))
from pvkit import tok_css_nested  # noqa: E402
page["css"] = tok_css_nested() + page["css"]
from icon_dec329 import apply as _dec329  # noqa
_dec329(page)  # DEC-329: cỡ, nét, màu icon
OUT.write_text(json.dumps(page, ensure_ascii=False, indent=1))
print("ok", OUT, len(ideas), "ý tưởng ·", len(decisions), "điểm")
