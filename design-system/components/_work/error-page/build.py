#!/usr/bin/env python3
"""Sinh page.json cho Error Page — trang lỗi dùng chung (404 · không có quyền · lỗi hệ thống · mất mạng · bảo trì).
Vòng 1 Brainstorm, hình vẽ tự do (chưa gắn token; vòng 3 đối chiếu foundation).
Chạy: python3 design-system/components/_work/error-page/build.py && python3 _scripts/ds-component-page.py error-page
Nguồn quy ước: design/ui-common/conventions.md GR-28 (không có quyền, web), GR-25 (mất mạng, app), GR-26 (popup chặn, app),
bảng E-common (008, 011). Chưa có mã E-common cho 404, bảo trì → câu chữ ở đây là đề xuất (điểm D7).
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "_forms"))
from kit import CSS, SCREEN_CSS, mini, vg, vg_row, write  # noqa: E402
sys.path.insert(0, str(ROOT))
from illos import ALL as ILLOS, CSS as ILLO_CSS  # noqa: E402  (minh hoạ theo mẫu Figma Test 1209:1060)

ILLO = {("default" if k == "s404" else k): f() for k, _, f in ILLOS}

OUT = ROOT / "page.json"

# ---------- icon (Lucide, nét 2) ----------
IC = {
    "search": '<circle cx="11" cy="11" r="7"/><path d="M21 21l-4-4"/>',
    "fileq": '<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6"/><path d="M10 13a2 2 0 1 1 3 1.7c-.6.3-1 .7-1 1.3M12 19h.01"/>',
    "lock": '<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
    "alert": '<path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/><path d="M12 9v4M12 17h.01"/>',
    "wifioff": '<path d="M2 2l20 20M8.5 16.5a5 5 0 0 1 7 0M2 8.8a15 15 0 0 1 4.2-2.6M10.7 5.1A15 15 0 0 1 22 8.8M5 12.9a10 10 0 0 1 5.2-2.7M16.8 11a10 10 0 0 1 2.2 1.9M12 20h.01"/>',
    "tool": '<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z"/>',
    "home": '<path d="M3 11l9-8 9 8"/><path d="M5 10v10h14V10"/>',
    "back": '<path d="M19 12H5M12 19l-7-7 7-7"/>',
    "copy": '<rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15V5a2 2 0 0 1 2-2h10"/>',
    "refresh": '<path d="M21 12a9 9 0 1 1-3-6.7L21 8"/><path d="M21 3v5h-5"/>',
    "truck": '<path d="M3 6h11v10H3zM14 9h4l3 3v4h-7"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
    "route": '<circle cx="6" cy="19" r="3"/><path d="M9 19h8.5a3.5 3.5 0 0 0 0-7h-11a3.5 3.5 0 0 1 0-7H15"/><circle cx="18" cy="5" r="3"/>',
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21c1-4 4-6 8-6s7 2 8 6"/>',
    "chevr": '<path d="M9 6l6 6-6 6"/>',
}


def ic(k, s=20, cls="i"):
    return (f'<svg class="{cls}" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{IC[k]}</svg>')


# ---------- nội dung từng trạng thái ----------
# (key, nhãn, icon, tone, mã, tiêu đề, mô tả, nút chính, nút phụ)
ST = [
    ("default", "404 · Không tìm thấy", "fileq", "gray", "404", "Không tìm thấy trang",
     "Đường dẫn có thể đã sai, hoặc trang đã bị xoá hay chuyển chỗ.", ("home", "Về trang chủ"), ("back", "Quay lại")),
    ("s403", "Không có quyền", "lock", "yellow", "403", "Không có quyền xem",
     "Bạn không có quyền xem thông tin này. Liên hệ quản trị viên để được cấp quyền.", ("home", "Về trang chủ"), None),
    ("s500", "Lỗi hệ thống", "alert", "red", "500", "Hệ thống đang gặp sự cố",
     "Đã xảy ra lỗi. Thử lại sau.", ("refresh", "Thử lại"), ("home", "Về trang chủ")),
    ("offline", "Mất kết nối", "wifioff", "gray", "", "Không có kết nối internet",
     "Kiểm tra mạng rồi thử lại. Thao tác chưa gửi sẽ tự gửi khi có mạng.", ("refresh", "Thử lại"), None),
    ("maint", "Bảo trì", "tool", "blue", "503", "Hệ thống đang bảo trì",
     "Invlogis tạm dừng để nâng cấp, dự kiến xong lúc 22:00 ngày 30/10/2026. Dữ liệu của bạn vẫn an toàn.", ("refresh", "Thử lại"), None),
]
STATE_KEYS = [s[0] for s in ST]
LONG_PATH = "/dieu-phoi/lenh-van-tai/LVT-2026-0412/chung-tu/hoa-don-van-chuyen-cang-cat-lai-kcn-song-than-binh-duong"


def block(key, icon, tone, code, title, desc, pri, sec, live=True, only=None):
    """Một khối lỗi. live=True: hiện theo state của Bảng chọn (data-show). only: ép một trạng thái (bảng biến thể)."""
    show = "" if only else f' data-show="state:{key}{" state:long" if key == "default" else ""}"'
    show = f' data-e404' if not only and key == "default" else show
    btns = ""
    if sec:
        btns += f'<button class="bt ep-sec">{ic(sec[0], 16)}{sec[1]}</button>'
    btns += f'<button class="bt pri ep-pri">{ic(pri[0], 16)}{pri[1]}</button>'
    meta = (f'<div class="ep-meta" data-show="D5:b">'
            + (f'<span>Mã lỗi {code}</span><span class="ep-dot">·</span>' if code else "")
            + '<span>Mã tra cứu <b class="mono">7F3A-21C9</b></span>'
            f'<button class="ep-cp" aria-label="Sao chép mã tra cứu">{ic("copy", 14)}</button></div>'
            f'<div class="ep-meta" data-show="D5:c"><a class="ep-link">Báo lỗi cho quản trị viên</a></div>')
    path = (f'<div class="ep-path" data-show="state:long">Đường dẫn: <span class="mono">{LONG_PATH}</span></div>'
            if key == "default" else "")
    sugg = ""
    if key in ("default",):
        sugg = ('<div class="ep-sugg" data-show="D4:b"><div class="ep-sh">Có thể bạn cần</div>'
                + "".join(f'<a class="ep-li">{ic(i, 18)}<span><b>{t}</b><small>{d}</small></span>{ic("chevr", 16)}</a>'
                          for i, t, d in (("truck", "Lệnh vận tải", "Danh sách lệnh đang chạy"),
                                          ("route", "Tuyến", "Tuyến và điểm giao nhận"),
                                          ("user", "Lái xe", "Hồ sơ và lịch lái xe")))
                + '</div>'
                '<div class="ep-sugg" data-show="D4:c"><div class="ep-dym">Có phải bạn muốn mở '
                '<a class="ep-link mono">LVT-2026-0412</a>?</div></div>')
    srch = ('<div class="ep-search" data-show="D3:c">' + ic("search", 16)
            + '<span>Tìm lệnh, xe, lái xe…</span></div>') if key == "default" else ""
    big = f'<div class="ep-code" data-show="D2:b">{code or "!"}</div>'
    feat = f'<div class="ep-feat t-{tone}" data-show="D2:a">{ic(icon, 24)}</div>'
    illo = f'<div class="ep-illo t-{tone}" data-show="D2:c">{illus(icon)}</div>'
    illo += f'<div class="ep-ill2" data-show="D2:d">{ILLO.get(key, "")}</div>'
    illo += f'<div class="ep-ill2 il-line" data-show="D2:e">{ILLO.get(key, "")}</div>'
    cmp = " data-cmp" if live else ""
    return (f'<div class="ep st-{key}"{show}{cmp}><div class="ep-art"><div class="ep-grid" data-show="D2:a"></div>{feat}{big}{illo}</div>'
            f'<div class="ep-text"><h2 class="ep-t">{title}</h2><p class="ep-d">{desc}</p>{path}</div>'
            f'{srch}<div class="ep-acts">{btns}</div>{sugg}{meta}</div>')


def illus(icon):
    """Hình minh hoạ nét đơn sắc: tấm bản đồ + xe tải + icon lỗi (D2 c)."""
    return ('<svg width="160" height="112" viewBox="0 0 160 112" fill="none" stroke="currentColor" stroke-width="2" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            '<path d="M14 26l40-12 52 12 40-12v72l-40 12-52-12-40 12z" fill="var(--color-bg-secondary)"/><path d="M54 14v72M106 26v72" opacity=".4"/>'
            '<path d="M30 70c14-18 34 6 50-10s30-14 46-4" stroke-dasharray="4 5" opacity=".7"/>'
            '<g transform="translate(58 46) scale(1.6)" stroke-width="1.6">' + IC["truck"] + '</g>'
            f'<g transform="translate(112 18) scale(1.3)" stroke-width="1.8">{IC[icon]}</g></svg>')


def all_states(live=True):
    return "".join(block(*s[:1], *s[2:], live=live) for s in ST)


CSS_EP = r"""
.ep{display:flex;flex-direction:column;align-items:center;text-align:center;gap:24px;max-width:480px;margin:0 auto;padding:64px 24px;position:relative}
.ep-art{position:relative;display:flex;align-items:center;justify-content:center;min-height:48px}
.ep-grid{position:absolute;width:336px;height:336px;left:50%;top:50%;transform:translate(-50%,-50%);pointer-events:none;
 background-image:linear-gradient(var(--color-border-secondary) 1px,transparent 1px),linear-gradient(90deg,var(--color-border-secondary) 1px,transparent 1px);background-size:48px 48px;
 -webkit-mask-image:radial-gradient(circle,#000 0,transparent 70%);mask-image:radial-gradient(circle,#000 0,transparent 70%)}
.ep-feat{position:relative;width:48px;height:48px;border-radius:10px;display:flex;align-items:center;justify-content:center;border:1px solid var(--color-border-primary);background:var(--color-bg-primary);color:var(--color-text-secondary);box-shadow:var(--elev-1)}
.ep-feat.t-red{color:var(--color-fg-error-primary)}.ep-feat.t-yellow{color:var(--color-fg-warning-primary)}.ep-feat.t-blue{color:var(--color-fg-info-primary)}
.ep-code{font:600 96px/104px Inter;letter-spacing:-2px;color:var(--color-text-primary)}
.ep-illo{color:var(--color-text-tertiary)}.ep-ill2 .il{width:160px;height:150px}.pv[data-platform=mobile] .ep-ill2 .il{width:128px;height:120px}.ep-cell .ep-ill2 .il{width:128px;height:120px}.ep-illo.t-red{color:var(--color-fg-error-primary)}.ep-illo.t-yellow{color:var(--color-fg-warning-primary)}.ep-illo.t-blue{color:var(--color-fg-info-primary)}
.ep-text{display:flex;flex-direction:column;gap:8px;position:relative}
.ep-t{margin:0;font:600 24px/32px Inter;color:var(--color-text-primary)}
.ep-d{margin:0;font:400 16px/24px Inter;color:var(--color-text-tertiary)}
.ep-path{font-size:13px;line-height:18px;color:var(--color-text-tertiary);overflow-wrap:anywhere;padding:8px 12px;background:var(--color-bg-tertiary);border-radius:8px;text-align:left}
.ep-acts{display:flex;gap:12px;justify-content:center;position:relative}
.ep-acts .bt{height:40px;padding:0 16px;font-size:14px}
.ep-search{display:flex;align-items:center;gap:8px;width:100%;max-width:360px;height:40px;padding:0 12px;border:1px solid var(--color-border-primary);border-radius:8px;color:var(--color-fg-quaternary);background:var(--color-bg-primary);position:relative}
.ep-sugg{width:100%;position:relative}
.ep-sh{font:500 13px/18px Inter;color:var(--color-text-tertiary);text-align:left;margin-bottom:8px}
.ep-li{display:flex;align-items:center;gap:12px;padding:12px;border:1px solid var(--color-border-secondary);border-radius:10px;margin-bottom:8px;text-align:left;color:var(--color-text-secondary);cursor:pointer;background:var(--color-bg-primary)}
.ep-li span{flex:1;display:flex;flex-direction:column}.ep-li b{color:var(--color-text-primary);font-weight:600}.ep-li small{font-size:13px;color:var(--color-text-tertiary)}
.ep-dym{font-size:14px;color:var(--color-text-secondary)}
.ep-meta{display:flex;align-items:center;gap:6px;font-size:13px;line-height:18px;color:var(--color-text-tertiary);position:relative}
.ep-meta b{color:var(--color-text-secondary);font-weight:500}.ep-dot{color:var(--color-fg-quaternary)}
.ep-cp{border:0;background:none;padding:4px;margin:-4px 0;border-radius:6px;color:var(--color-text-tertiary);cursor:pointer;display:inline-flex}
.ep-link{color:var(--color-text-primary);text-decoration:underline;text-underline-offset:3px;cursor:pointer;font-weight:500}
/* D1 bố cục */
.pv[data-platform=web][data-D1=b] .ep{flex-direction:row-reverse;flex-wrap:wrap;text-align:left;align-items:center;max-width:880px;gap:24px 64px;justify-content:space-between}
.pv[data-platform=web][data-D1=b] .ep-art{flex:0 0 280px;min-height:240px;order:0}
.pv[data-platform=web][data-D1=b] .ep>:not(.ep-art){flex:0 0 calc(100% - 344px)}
.pv[data-platform=web][data-D1=b] .ep-acts{justify-content:flex-start}
.pv[data-platform=web][data-D1=b] .ep-meta{justify-content:flex-start}
.pv[data-platform=web][data-D1=c] .ep{background:var(--color-bg-primary);border:1px solid var(--color-border-secondary);border-radius:16px;padding:40px 32px;box-shadow:var(--elev-3);margin-top:48px;margin-bottom:48px}
.pv[data-platform=web][data-D1=c] .ep-host{background-color:var(--color-bg-secondary);background-image:radial-gradient(var(--color-border-primary) 1px,transparent 1px);background-size:20px 20px}
.ep-host{min-height:100%;display:flex;flex-direction:column;justify-content:center}
/* D6 app */
.pv[data-platform=mobile] .ep{padding:48px 16px 24px;gap:20px;max-width:none}
.pv[data-platform=mobile] .ep-t{font-size:20px;line-height:28px}
.pv[data-platform=mobile] .ep-d{font-size:15px;line-height:22px}
.pv[data-platform=mobile] .ep-code{font-size:72px;line-height:80px}
.pv[data-platform=mobile] .ep-grid{width:288px;height:288px}
.pv[data-platform=mobile] .ep-acts{flex-direction:column-reverse;width:100%;gap:8px}
.pv[data-platform=mobile] .ep-acts .bt{height:48px;border-radius:12px;font-size:15px;width:100%}
.pv[data-platform=mobile][data-D6=a] .ep-host{min-height:640px}
.pv[data-platform=mobile][data-D6=a] .ep{min-height:640px}
.pv[data-platform=mobile][data-D6=a] .ep-acts{margin-top:auto}
.pv[data-platform=mobile] .ep-cp{padding:12px;margin:-12px -8px}
/* 404 hiện ở cả state default và long */
.pv:not([data-state=default]):not([data-state=long]) [data-e404]{display:none}
/* trang ngoài vỏ (chưa đăng nhập) */
.ep-out{min-height:720px;display:flex;flex-direction:column;background:var(--color-bg-primary)}
.ep-out .ep-top{height:64px;display:flex;align-items:center;padding:0 32px;border-bottom:1px solid var(--color-border-secondary);font:700 18px/24px Inter;letter-spacing:-.3px}
.ep-out .ep-host{flex:1}
.ep-out .ep-foot{padding:16px 32px;color:var(--color-text-tertiary);font-size:13px;display:flex;justify-content:space-between;border-top:1px solid var(--color-border-secondary)}
.ep-cell{border:1px solid var(--color-border-secondary);border-radius:12px;overflow:hidden;background:var(--color-bg-primary)}
.ep-cell .ep{padding:32px 16px;gap:16px}
.ep-cell .ep-t{font-size:18px;line-height:26px}.ep-cell .ep-d{font-size:14px;line-height:20px}
.ep-cell .ep-code{font-size:56px;line-height:64px}
.ep-cell .ep-grid{width:240px;height:240px}
"""

# ---------- hình nhỏ cho phương án ----------
BASE = {"D1": "a", "D2": "a", "D3": "a", "D4": "a", "D5": "a", "D6": "a"}


def m(over, key="default", w=440, plat="web", wrap=True):
    s = next(x for x in ST if x[0] == key)
    inner = block(s[0], *s[2:], live=False, only=key)
    inner = f'<div class="ep-cell">{inner}</div>' if wrap else inner
    return mini({**BASE, **over, "state": key}, inner, w, plat)


decisions = [
 {"id": "D1", "title": "Bố cục trên web",
  "why": "Trang lỗi nằm trong vùng nội dung (sidebar, header vẫn hiện — GR-28) hoặc toàn trang khi chưa đăng nhập. Bố cục quyết mắt đọc gì trước: hình, chữ hay lối thoát.",
  "source": "GR-28 · Untitled 404-pages 01 (giữa), 02 (chia đôi) · Mixpanel, Clutch (giữa)",
  "options": [
   {"label": "Giữa vùng nội dung", "desc": "Hình → tiêu đề → mô tả → nút, căn giữa, rộng tối đa 480. Gọn, hợp cả trong vỏ lẫn ngoài vỏ.", "rec": True,
    "preview": m({"D1": "a"}), "ideas": ["I1", "I4", "I5"]},
   {"label": "Chia đôi chữ trái, hình phải", "desc": "Như Untitled 02. Rộng 880, hợp trang ngoài vỏ; trong vỏ ở 1280 còn ~1000 thì vẫn vừa.",
    "preview": m({"D1": "b", "D2": "c"}, w=760, wrap=True), "ideas": ["I2"]},
   {"label": "Thẻ nổi giữa nền chấm", "desc": "Khối lỗi trong thẻ có bóng, nền chấm mờ. Tách hẳn khỏi nội dung, nhưng thêm một lớp khung.",
    "preview": mini({**BASE, "D1": "c", "state": "default"}, '<div class="ep-host" style="padding:8px 16px">' + block("default", *ST[0][2:], live=False, only="default") + "</div>", 520),
    "ideas": ["I12"]}],
  "untitled": m({"D1": "a"}), "untitledNote": "404-pages 01: căn giữa, featured icon + nền lưới mờ",
  "astryx": '<div class="ep-cell" style="padding:24px;text-align:center;color:var(--color-text-tertiary)">Astryx chưa có trang lỗi — GR-28 chỉ ghi “vùng nội dung hiện E-common-011 + nút Về trang chủ”.</div>',
  "astryxNote": "chưa có"},
 {"id": "D2", "title": "Hình phía trên chữ",
  "why": "Cùng một khung cho 5 loại lỗi; hình phải phân biệt được loại lỗi mà không chỉ dựa vào màu (Do's (b)).",
  "source": "foundations · Featured icon 48/24 · Untitled 404-pages · 21st.dev Error 404 (số lớn)",
  "options": [
   {"label": "Featured icon + lưới mờ", "desc": "Icon 24 trong ô 48 có viền, nền lưới mờ dần. Mỗi loại lỗi một icon. Dùng lại Featured icon có sẵn.", "rec": True,
    "preview": m({"D2": "a"}, "s500"), "ideas": ["I1", "I5"]},
   {"label": "Mã lỗi số lớn", "desc": "“404”, “500” cỡ 96. Dễ nhận ra với người quen web; mất kết nối không có mã thì phải dùng “!”.",
    "preview": m({"D2": "b"}, "default"), "ideas": ["I6", "I7"]},
   {"label": "Hình minh hoạ nét", "desc": "Bản đồ + xe tải + icon lỗi, đơn sắc. Có chất logistics nhưng phải vẽ thêm 5 hình.",
    "preview": m({"D2": "c"}, "offline"), "ideas": ["I4", "I10"]}],
  "untitled": m({"D2": "a"}, "default"), "untitledNote": "featured icon + background pattern grid",
  "astryx": '<div class="ep-cell" style="padding:24px;text-align:center;color:var(--color-text-tertiary)">EmptyState Astryx: icon 48 trần, không nền.</div>', "astryxNote": "EmptyState"},
 {"id": "D3", "title": "Nút trên trang 404",
  "why": "Người mở link sai cần một lối ra. Trong vỏ đã có sidebar, nên nút chỉ cần lối ngắn nhất; GR-28 (không quyền) giữ một nút Về trang chủ.",
  "source": "GR-28 · Untitled 404-pages 02 (ô tìm) · SaaSFrame Conduktor (một nút)",
  "options": [
   {"label": "Về trang chủ + Quay lại", "desc": "Nút chính Về trang chủ, nút phụ Quay lại (về màn trước trong lịch sử).", "rec": True,
    "preview": m({"D3": "a"}), "ideas": ["I1", "I2"]},
   {"label": "Chỉ Về trang chủ", "desc": "Một nút, như Mixpanel. Mất lối quay lại nhanh khi mở nhầm từ một màn đang làm.",
    "preview": m({"D3": "b"}).replace('<button class="bt ep-sec">', '<button class="bt ep-sec" style="display:none">'), "ideas": ["I4"]},
   {"label": "Nút + ô tìm", "desc": "Thêm ô tìm lệnh, xe, lái xe. Trùng ô tìm trên header khi đang trong vỏ.",
    "preview": m({"D3": "c"}), "ideas": ["I2", "I8"]}]},
 {"id": "D4", "title": "Gợi ý lối đi trên 404",
  "why": "Link hỏng thường từ thông báo cũ, email hoặc tin nhắn. Gợi ý trang gần đúng giúp đi tiếp mà không phải tìm lại.",
  "source": "Untitled 404-pages 05 (helpful links) · 21st.dev 404 Did You Mean",
  "options": [
   {"label": "Không gợi ý", "desc": "Chỉ nút. Gọn nhất; trong vỏ đã có sidebar làm lối tắt.", "rec": True, "preview": m({"D4": "a"})},
   {"label": "Danh sách lối tắt", "desc": "3 mục theo quyền của người dùng (Lệnh vận tải, Tuyến, Lái xe).", "preview": m({"D4": "b"}), "ideas": ["I3"]},
   {"label": "“Có phải bạn muốn mở…”", "desc": "Đoán bản ghi từ đường dẫn (mã lệnh còn đọc được). Cần dev đoán được; chưa chắc làm được.",
    "preview": m({"D4": "c"}), "ideas": ["I8"]}]},
 {"id": "D5", "title": "Thông tin để báo hỗ trợ",
  "why": "Khi người dùng gọi hỗ trợ, đội vận hành cần biết lỗi gì, lúc nào. Mã tra cứu giúp tìm log mà không phải hỏi lại.",
  "source": "SaaSFrame Front 404 · Untitled 404-pages 07 (bảo trì)",
  "options": [
   {"label": "Không hiện", "desc": "Chỉ chữ cho người dùng.", "preview": m({"D5": "a"}, "s500")},
   {"label": "Mã lỗi + mã tra cứu", "desc": "Dòng nhỏ “Mã lỗi 500 · Mã tra cứu 7F3A-21C9” + nút sao chép.", "rec": True,
    "preview": m({"D5": "b"}, "s500"), "ideas": ["I9"]},
   {"label": "Link báo lỗi", "desc": "“Báo lỗi cho quản trị viên” — gửi kèm đường dẫn và giờ. Cần luồng nhận báo lỗi.",
    "preview": m({"D5": "c"}, "s500")}]},
 {"id": "D6", "title": "Trang lỗi trên app",
  "why": "App dùng ngoài bãi, một tay. GR-21: nút chính full width; câu hỏi là nút nằm đáy màn hay ngay dưới chữ.",
  "source": "GR-21 · GR-25 · Unacademy no connection (UXcel) · vp0 offline",
  "options": [
   {"label": "Nút ở đáy màn", "desc": "Hình và chữ giữa màn, nút full width ghim đáy, gần ngón cái.", "rec": True,
    "preview": mini({**BASE, "D6": "a", "state": "offline"}, '<div class="ep-host" style="min-height:480px">' + block("offline", *ST[3][2:], live=False, only="offline").replace("min-height:640px", "") + "</div>", 300, "mobile"),
    "ideas": ["I10", "I11"]},
   {"label": "Nút ngay dưới chữ", "desc": "Cả khối căn giữa màn, nút liền dưới mô tả. Gần mắt hơn, xa ngón cái hơn.",
    "preview": mini({**BASE, "D6": "b", "state": "offline"}, '<div class="ep-host" style="min-height:480px">' + block("offline", *ST[3][2:], live=False, only="offline") + "</div>", 300, "mobile"),
    "ideas": ["I10"]}]},
 {"id": "D7", "title": "Câu chữ 404 và bảo trì",
  "why": "Bảng E-common chưa có mã cho 404 và bảo trì; 500 dùng E-common-008, không quyền dùng E-common-011. Cần chốt câu rồi thêm mã E-common-013, 014.",
  "source": "design/ui-common/conventions.md › Lỗi dùng chung · design.md › Content & Formatting (Viết như người nói)",
  "options": [
   {"label": "Nói nguyên nhân + việc làm tiếp", "desc": "“Không tìm thấy trang” · “Đường dẫn có thể đã sai, hoặc trang đã bị xoá hay chuyển chỗ.”", "rec": True,
    "preview": m({}, "default")},
   {"label": "Ngắn, một câu", "desc": "“Không tìm thấy trang” · “Trang này không tồn tại.”",
    "preview": m({}, "default").replace("Đường dẫn có thể đã sai, hoặc trang đã bị xoá hay chuyển chỗ.", "Trang này không tồn tại.")}]},
]

D2_D = {"label": "Minh hoạ nhân vật (mẫu Figma)", "desc": "Đồ vật có mặt (thư mục, ổ khoá, máy chủ, đám mây, container), nét xám than, mảng tím xám, một chấm cam trong huy hiệu. Thân thiện, nhận ra loại lỗi ngay; cỡ 128×120, thêm hình mới phải vẽ cùng ngôn ngữ.",
        "preview": m({"D2": "d"}, "s500"), "ideas": ["I13"]}
decisions[1]["options"].append(D2_D)
decisions[1]["options"].append({"label": "Minh hoạ chỉ nét", "desc": "Cùng bộ hình D2-d nhưng bỏ mảng tím xám: nền trong hình trắng, chỉ còn nét + huy hiệu màu. Nhẹ, hợp nền trắng DS v2; huy hiệu thành điểm nhấn duy nhất, hình khối bớt nổi.",
                                "preview": m({"D2": "e"}, "s500"), "ideas": ["I13"]})

ideas = [
 {"id": "I1", "source": "Untitled UI", "url": "https://www.untitledui.com/react/marketing/404-pages", "title": "404 căn giữa, featured icon + lưới mờ",
  "why": "Khung chuẩn của Untitled: icon có viền trên nền lưới mờ dần, tiêu đề, mô tả, hai nút. Gọn, dùng lại được cho mọi loại lỗi.",
  "preview": m({"D1": "a", "D2": "a"})},
 {"id": "I2", "source": "Untitled UI", "url": "https://untitledui.com/react/marketing/404-pages/not-found-page-02", "title": "Chia đôi, có ô tìm",
  "why": "Chữ trái, hình phải, thêm ô tìm. Hợp trang ngoài vỏ, rộng.", "preview": m({"D1": "b", "D2": "c", "D3": "c"}, w=760)},
 {"id": "I3", "source": "Untitled UI", "url": "https://untitledui.com/react/marketing/404-pages/not-found-page-05", "title": "404 kèm lối tắt",
  "why": "Danh sách vài trang hay dùng ngay dưới nút. Đi tiếp không cần sidebar.", "preview": m({"D4": "b"})},
 {"id": "I4", "source": "SaaSFrame · Mixpanel", "url": "https://www.saasframe.io/examples/mixpanel-404-page", "title": "Một hình, một nút",
  "why": "Khoảng trắng chiếm phần lớn, một nút Về trang chủ. Bình tĩnh, chuyên nghiệp.", "preview": m({"D2": "c"}).replace('<button class="bt ep-sec">', '<button class="bt ep-sec" style="display:none">')},
 {"id": "I5", "source": "SaaSFrame · Clutch", "url": "https://www.saasframe.io/examples/clutch-404-page", "title": "Tiêu đề rõ + icon động",
  "why": "Tiêu đề nói thẳng lỗi gì, icon nhỏ chuyển động nhẹ, một nút nổi bật.", "preview": m({"D2": "a"})},
 {"id": "I6", "source": "21st.dev", "url": "https://21st.dev/@shadcnstore/components/error-page-1.md", "title": "Mã lỗi lớn + hai nút",
  "why": "Số 404 làm hình chính, không cần minh hoạ. Hợp người dùng quen web.", "preview": m({"D2": "b"})},
 {"id": "I7", "source": "21st.dev", "url": "https://21st.dev/@dhileepkumargm/components/shadcn-404.md", "title": "shadcn 404 gọn, theo theme",
  "why": "Chỉ chữ và số, đổi theo Light/Dark. Không phụ thuộc hình vẽ.", "preview": m({"D2": "b", "D3": "b"}).replace('<button class="bt ep-sec">', '<button class="bt ep-sec" style="display:none">')},
 {"id": "I8", "source": "21st.dev", "url": "https://21st.dev/@ziegfiroyt/components/error9.md", "title": "404 “Có phải bạn muốn…”",
  "why": "Hiện đường dẫn sai và gợi ý trang gần đúng nhất. Giúp người mở link cũ trong email.", "preview": m({"D4": "c"})},
 {"id": "I9", "source": "SaaSFrame · Front", "url": "https://www.saasframe.io/examples/front-404-page", "title": "Kèm thông tin hỗ trợ",
  "why": "Dòng nhỏ dưới nút cho người cần báo lỗi. Không làm rối phần chính.", "preview": m({"D5": "b"}, "s500")},
 {"id": "I10", "source": "UXcel · Unacademy", "url": "https://app.uxcel.com/showcase/empty-state-design-for-unacademy-042", "title": "App mất kết nối + Thử lại",
  "why": "Câu chính, gợi ý kiểm tra mạng, một nút Thử lại. Mẫu chuẩn cho màn mất mạng trên app.",
  "preview": mini({**BASE, "D2": "c", "state": "offline"}, '<div class="ep-cell">' + block("offline", *ST[3][2:], live=False, only="offline") + "</div>", 300, "mobile")},
 {"id": "I11", "source": "vp0", "url": "https://vp0.com/blogs/offline-mode-mobile-app-empty-state-ui", "title": "Mất mạng: giữ dữ liệu cũ",
  "why": "Chỉ hiện màn lỗi khi không có gì để xem; có dữ liệu cũ thì giữ và báo bằng banner nhỏ (đúng GR-25).",
  "preview": '<div class="pv pvm" data-platform="mobile" style="padding:8px;max-width:300px"><div class="ep-cell"><div style="padding:8px 12px;background:var(--color-bg-tertiary);font-size:13px;color:var(--color-text-secondary)">Không có kết nối internet</div><div class="mcard" style="margin:12px"><b class="mono">LVT-2026-0412</b><span class="s">Cát Lái → Sóng Thần · 51C-123.45</span></div><div class="mcard" style="margin:0 12px 12px"><b class="mono">LVT-2026-0413</b><span class="s">Hiệp Phước → VSIP 2</span></div></div></div>'},
 {"id": "I12", "source": "Figma Community", "url": "https://www.figma.com/templates/404-page-designs/", "title": "Thẻ nổi trên nền hoa văn",
  "why": "Khối lỗi trong thẻ có bóng, nền hoa văn mờ. Tách trang lỗi khỏi nội dung thường.",
  "preview": mini({**BASE, "D1": "c", "state": "default"}, '<div class="ep-host" style="padding:8px 16px">' + block("default", *ST[0][2:], live=False, only="default") + "</div>", 520)},
 {"id": "I13", "source": "Figma · mẫu của anh", "url": "https://www.figma.com/design/MmVrTuz96Zg1zV5gBgoqB8/Test?node-id=1209-1060", "title": "Thư mục mặt buồn, dấu hỏi cam",
  "why": "Nhân vật hoá đồ vật: mắt X, miệng mếu, khói bốc; nét xám than, một chấm cam duy nhất trong huy hiệu tròn. Bộ D2-d vẽ lại 5 loại lỗi + 3 màn rỗng theo đúng ngôn ngữ này.",
  "preview": m({"D2": "d"})},
]

presets = [
 {"id": "rec", "label": "Đề xuất", "pick": {"D1": "a", "D2": "a", "D3": "a", "D4": "a", "D5": "b", "D6": "a", "D7": "a"}},
 {"id": "untitled", "label": "Theo Untitled", "pick": {"D1": "a", "D2": "a", "D3": "a", "D4": "b", "D5": "a", "D6": "b", "D7": "a"}},
 {"id": "astryx", "label": "Astryx hiện tại", "pick": {"D1": "a", "D2": "a", "D3": "b", "D4": "a", "D5": "a", "D6": "b", "D7": "b"}},
 {"id": "I1", "label": "I1 · Untitled căn giữa", "pick": {"D1": "a", "D2": "a", "D3": "a", "D4": "a", "D5": "a", "D6": "a", "D7": "a"}},
 {"id": "I5", "label": "I5 · Clutch", "pick": {"D1": "a", "D2": "a", "D3": "b", "D4": "a", "D5": "a", "D6": "a", "D7": "a"}},
 {"id": "I7", "label": "I7 · shadcn 404", "pick": {"D1": "a", "D2": "b", "D3": "b", "D4": "a", "D5": "a", "D6": "a", "D7": "b"}},
 {"id": "I11", "label": "I11 · vp0 mất mạng", "pick": {"D1": "a", "D2": "a", "D3": "a", "D4": "a", "D5": "a", "D6": "a", "D7": "a"}, "screen": 2},
 {"id": "I2", "label": "I2 · Untitled chia đôi", "pick": {"D1": "b", "D2": "c", "D3": "c", "D4": "a", "D5": "a", "D6": "a", "D7": "a"}},
 {"id": "I3", "label": "I3 · Untitled lối tắt", "pick": {"D1": "a", "D2": "a", "D3": "a", "D4": "b", "D5": "a", "D6": "a", "D7": "a"}},
 {"id": "I4", "label": "I4 · Mixpanel", "pick": {"D1": "a", "D2": "c", "D3": "b", "D4": "a", "D5": "a", "D6": "a", "D7": "b"}},
 {"id": "I6", "label": "I6 · Mã lỗi lớn", "pick": {"D1": "a", "D2": "b", "D3": "a", "D4": "a", "D5": "a", "D6": "a", "D7": "a"}},
 {"id": "I8", "label": "I8 · Có phải bạn muốn", "pick": {"D1": "a", "D2": "a", "D3": "a", "D4": "c", "D5": "a", "D6": "a", "D7": "a"}},
 {"id": "I9", "label": "I9 · Kèm mã hỗ trợ", "pick": {"D1": "a", "D2": "a", "D3": "a", "D4": "a", "D5": "b", "D6": "a", "D7": "a"}},
 {"id": "I10", "label": "I10 · App mất mạng", "pick": {"D1": "a", "D2": "c", "D3": "a", "D4": "a", "D5": "a", "D6": "a", "D7": "a"}, "screen": 2},
 {"id": "I12", "label": "I12 · Thẻ nổi", "pick": {"D1": "c", "D2": "a", "D3": "a", "D4": "a", "D5": "a", "D6": "a", "D7": "a"}},
 {"id": "I13", "label": "I13 · Minh hoạ mẫu Figma", "pick": {"D1": "a", "D2": "d", "D3": "a", "D4": "a", "D5": "b", "D6": "a", "D7": "a"}},
]
# D3 b: ẩn nút phụ; D7 b: câu ngắn — luật CSS trên màn sống
CSS_EP += r"""
.pv[data-D3=b] .st-default .ep-sec{display:none}
.pv[data-D7=b] .st-default .ep-d{font-size:0}.pv[data-D7=b] .st-default .ep-d::after{content:"Trang này không tồn tại.";font-size:16px}
.pv[data-platform=mobile][data-D7=b] .st-default .ep-d::after{font-size:15px}
"""

HOST = lambda inner: f'<div class="ep-host">{inner}</div>'

S_IN = HOST(all_states())
S_OUT = ('<div class="ep-out"><div class="ep-top">invlogis</div>' + HOST(all_states())
         + '<div class="ep-foot"><span>© 2026 innvie</span><span>Hỗ trợ: 1900 0000</span></div></div>')
S_APP = HOST(all_states())


def grid(plat):
    cols = 3 if plat == "web" else 1
    rows = [vg_row("5 loại lỗi · bố cục đang chọn", [(s[1], f'<div class="ep-cell">{block(s[0], *s[2:], live=False, only=s[0])}</div>') for s in ST], cols,
                   "icon và nút đổi theo loại lỗi"),
            vg_row("Chữ dài", [("404 · đường dẫn dài", '<div class="ep-cell">' + block("default", *ST[0][2:], live=False, only="default")
                                .replace('data-show="state:long"', "") + "</div>"),
                               ("Bảo trì · mô tả dài", '<div class="ep-cell">' + block("maint", *ST[4][2:], live=False, only="maint") + "</div>")],
                   2 if plat == "web" else 1, "đường dẫn xuống dòng ở mọi ký tự; tiêu đề không cắt")]
    return vg(rows)


_ILLO_GRID = lambda cls, title: (f'<h3 style="margin:24px 24px 0;font:600 15px/22px Inter">{title}</h3>'
                                  f'<div class="{cls}" style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px;padding:12px 24px 8px">'
            + "".join(f'<figure class="ep-cell" style="margin:0;padding:20px 12px 14px;display:flex;flex-direction:column;align-items:center;gap:10px">{f()}'
                      f'<figcaption style="font-size:13px;color:var(--color-text-tertiary)">{l}</figcaption></figure>' for k, l, f in ILLOS) + '</div>')
ILLO_SET = _ILLO_GRID("", "Có mảng (D2-d)") + _ILLO_GRID("il-line", "Chỉ nét (D2-e)")

screens = [
 {"id": "in-web", "name": "Trong ứng dụng", "device": "web", "nav": "Lệnh vận tải", "crumb": "Điều phối", "title": "Không tìm thấy trang", "heading": False,
  "note": "Người dùng đã đăng nhập mở một đường dẫn hỏng (từ thông báo cũ, email). Sidebar và header vẫn hiện — GR-28. Đổi loại lỗi ở Bảng chọn › Hiển thị.",
  "html": S_IN},
 {"id": "out-web", "name": "Ngoài ứng dụng", "device": "web", "shell": "none",
  "note": "Chưa đăng nhập hoặc lỗi trước khi vào được vỏ (500, bảo trì): toàn trang, chỉ logo và chân trang.", "html": S_OUT},
 {"id": "app", "name": "Trên app", "device": "mobile", "title": "Lệnh vận tải", "back": True, "nav": "Lệnh",
  "note": "Mở deep link hỏng hoặc mất mạng khi chưa có dữ liệu để hiện (có dữ liệu cũ thì giữ + banner, GR-25).", "html": S_APP},
 {"id": "variants-web", "name": "Bảng biến thể", "device": "web", "shell": "none", "note": "5 loại lỗi + chữ dài, theo bố cục đang chọn.", "html": grid("web")},
 {"id": "variants-app", "name": "Bảng biến thể", "device": "mobile", "shell": "none", "note": "Cùng bộ trên app.", "html": grid("mobile")},
 {"id": "illos", "name": "Bộ minh hoạ", "device": "web", "shell": "none",
  "note": "12 hình theo mẫu Figma 1209:1060, hai kiểu: có mảng (D2-d) và chỉ nét (D2-e) — 5 loại lỗi, 3 màn không có dữ liệu, 2 thành công, 2 thất bại (dùng khi làm Empty State / màn kết quả, BL-224). Đổi Light/Dark ở Bảng chọn.", "html": ILLO_SET},
]

page = {
 "component": "Error Page", "slug": "error-page", "title": "Error Page Review",
 "subtitle": "Shared asset · trang lỗi dùng chung — 404, không có quyền, lỗi hệ thống, mất kết nối, bảo trì. Nhóm B: cùng cấu tạo, app đổi chỗ nút.",
 "round": "brainstorm",
 "refs": {
  "untitled": {"summary": "Bộ <mark>404-pages</mark> (marketing, bản Pro): căn giữa hoặc chia đôi, featured icon trên nền lưới mờ, ô tìm, lối tắt, bản bảo trì. Bản mở chỉ có <mark>shared-assets</mark>: illustrations, background-patterns.",
               "source": "untitledui.com/react/marketing/404-pages · design/_ref/untitled-ui/react/components/shared-assets/"},
  "astryx": {"summary": "Chưa có trang lỗi. Có EmptyState (icon 48 + chữ + nút) và quy ước GR-28: vùng nội dung hiện E-common-011 + nút Về trang chủ.",
             "source": "design/design.md › States · design/ui-common/conventions.md GR-25, GR-26, GR-28"},
  "usage": ["Mọi feature web · mở đường dẫn hỏng hoặc không có quyền (GR-28)",
            "Cross-process-flow · khối lỗi “Không tải được sơ đồ.” (E-common-008)",
            "App lái xe · deep link từ thông báo (GR-24), mất mạng khi chưa có dữ liệu (GR-25)",
            "Toàn hệ thống · bảo trì có hẹn giờ"],
  "platform": "Nhóm B (DEC-279): cùng cấu tạo; app nút full width (GR-21), D6 hỏi chỗ đặt nút. Không quyền trên app vẫn là popup chặn (GR-26), không dùng trang này."},
 "css": CSS + CSS_EP + ILLO_CSS, "cssScreen": SCREEN_CSS,
 "states": [{"key": k, "label": l} for k, l, *_ in ST] + [{"key": "long", "label": "Chữ dài (404)"}],
 "ideas": ideas, "decisions": decisions, "presets": presets, "screens": screens,
}

write(OUT, page, decisions, brief=False)
