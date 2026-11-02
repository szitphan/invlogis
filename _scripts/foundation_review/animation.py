#!/usr/bin/env python3
"""SPEC trang review Animation bổ sung: phản hồi thao tác, dữ liệu đổi, logistics, trạng thái tải. Không mở lại DEC-333. Dựng: python3 _scripts/foundation_review/build.py animation"""
import collections
import os
import re

import kit
from kit import ROOT, icon, panes, rows

OK, DIFF, GAP, OWN = "st-ok", "st-diff", "st-gap", "st-own"
LAB = {OK: "Giống", DIFF: "Khác có lý do", GAP: "Mình thiếu", OWN: "Chỉ mình có"}


def st(s):
    return f'<span class="{s}">{LAB[s]}</span>'


# ---------- đếm thật trên code Untitled ----------
UDIR = ROOT / "design/_ref/untitled-ui/react/components"
_u = []
for r, _, fs in os.walk(UDIR):
    for f in fs:
        if f.endswith(".tsx") and ".demo." not in f and ".story." not in f:
            _u.append((os.path.relpath(os.path.join(r, f), UDIR), open(os.path.join(r, f), encoding="utf-8", errors="ignore").read()))


def ucount(p):
    return sum(1 for _, x in _u if re.search(p, x, flags=re.I))


U_FILES = len(_u)
U_SHAKE = ucount(r"shake|wiggle")
U_ACC = ucount(r"accordion|disclosure")
U_COUNT = ucount(r"countUp|count-up|AnimatedNumber|NumberFlow")
U_PATHLEN = ucount(r"pathLength")
U_FLASH = ucount(r"animate-(?:flash|highlight)|row-?highlight")
U_MAP = ucount(r"mapbox|leaflet|maplibre|google\.maps")
U_SCAN = ucount(r"scanner|barcode|qr-?scan")
U_PULL = ucount(r"pull-?to-?refresh|PullToRefresh")
U_OFFLINE = ucount(r"navigator\.onLine")
U_CLIP = ucount(r"useClipboard|clipboard")
U_SKEL = ucount(r"skeleton")
U_STEP = ucount(r"progress-?steps?|ProgressSteps?")
# biểu đồ đặt thuộc tính ở file demo, nên đếm riêng cả demo
U_CHART_OFF = sum(open(os.path.join(r, f), encoding="utf-8", errors="ignore").read().count("isAnimationActive={false}") for r, _, fs in os.walk(UDIR / "application/charts") for f in fs if f.endswith(".demo.tsx"))

# ---------- khung xem thử ----------
CHECK = '<svg class="an-chk" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path pathLength="1" d="M4 12l5 5L20 6"/></svg>'


def v_(label, inner, mode="once", seq="", fn="", rec=False, btn="Phát", cls="", hold=""):
    a = f' data-seq="{seq}"' if seq else ""
    a += f' data-fn="{fn}"' if fn else ""
    a += f' data-hold="{hold}"' if hold else ""
    r = '<span class="an-rec">khuyến nghị</span>' if rec else ""
    return (f'<div class="an-st {cls}" data-mode="{mode}"{a}><div class="an-head"><span class="type-caption an-lab">{label}{r}</span>'
            f'<button class="tp-btn sec an-play" type="button"><span class="type-label">{btn}</span></button></div><div class="an-box">{inner}</div></div>')


def grid(*vs):
    return f'<div class="an-vars">{"".join(vs)}</div>'


def both(fn, platform="web"):
    return panes(lambda m, p: fn(), platforms=(platform,))


def light(fn):
    return panes(lambda m, p: fn(), modes=("light",))


# --- an00
def pv_scale():
    bar = lambda n, w, c, x: f'<div class="an-tl"><span class="type-caption an-tln">{n}</span><span class="an-tlb"><i class="{c}" style="width:{w}%"></i></span><span class="type-caption tp-num">{x}</span></div>'
    return ('<div class="an-tls">' + bar("Đổi icon, số: <code>duration/fast</code>", 125 / 15, "", "125")
            + bar("Lúc đóng: <code>duration/exit</code>", 200 / 15, "", "200")
            + bar("Vẽ dấu check, mở khối: <code>duration/medium</code>", 300 / 15, "", "300")
            + bar("Phai nền: <code>duration/slow</code>", 500 / 15, "", "500")
            + bar("Giữ dấu xong: <code>duration/slow</code> × 2", 1000 / 15, "an-calc", "1000")
            + bar("Tô dòng vừa đổi: <code>duration/slow</code> × 3", 100, "an-calc", "1500") + "</div>")


# --- an01
def pv_presets():
    ch = lambda n, sub, inner, mode="once", seq="": v_(f"<code>{n}</code> · {sub}", inner, mode=mode, seq=seq)
    return grid(
        ch("fade-in", "mờ dần", '<div class="tp-card an-p-fade"><span class="type-body">Cập nhật lúc 14:30</span></div>'),
        ch("draw", "vẽ nét", f'<div class="an-ok an-p-draw">{CHECK}</div>'),
        ch("swap", "đổi tại chỗ", f'<div class="an-swap an-big" data-swap><span class="an-l1">{icon("copy", "tp-ic-lg")}</span><span class="an-l2">{icon("check", "tp-ic-lg")}</span></div>', seq="done:1000"),
        ch("flash", "tô rồi phai", '<div class="an-row an-p-flash"><span class="type-code">LVT-2026-0412</span></div>'),
        ch("expand", "mở cao", f'<div class="an-acc" ><div class="an-acc-b"><div><div class="type-body an-acc-t">Tài xế nhận container tại cổng B.</div></div></div></div>', mode="toggle"),
        ch("glide", "di chuyển", f'<div class="an-glide"><span class="an-mk">{icon("truck", "tp-ic-sm")}</span></div>', mode="toggle"))


# --- an02
def _res(kind, c):
    if kind == "ok":
        g = '<path class="an-s1" pathLength="1" d="M4 12l5 5L20 6"/>'
    else:
        g = '<path class="an-s1" pathLength="1" d="M6 6l12 12"/><path class="an-s2" pathLength="1" d="M18 6 6 18"/>'
    return (f'<div class="an-res an-res-{kind} {c}"><i class="an-r1"></i><i class="an-r2"></i><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{g}</svg></div>')


def _pair(c):
    return f'<div class="an-pair"><div class="an-col">{_res("ok", c)}<div class="type-label an-msg">Đã duyệt lệnh</div></div><div class="an-col">{_res("no", c)}<div class="type-label an-msg">Chưa gửi được</div></div></div>'


def pv_success():
    return grid(v_("Ba nhịp theo mẫu, không nảy, tổng 600", _pair("an-r-stage"), rec=True),
                v_("Ba nhịp + nảy như mẫu, tổng 1125", _pair("an-r-bounce")),
                v_("Một nhịp: đĩa mờ dần, dấu vẽ 300", _pair("an-r-one")))


# --- an03
def pv_error():
    fld = lambda c: (f'<div class="tp-fld {c}"><span class="type-label">Cước dự kiến</span><div class="tp-inp e"><span class="type-body tp-num">12.500</span></div>'
                     '<div class="type-hint tp-err an-hint">Cước thấp hơn định mức của tuyến.</div></div>')
    return grid(v_("Dòng lỗi mờ dần, viền đổi màu, không rung", fld("an-e-fade"), rec=True),
                v_("Rung ngang 3 nhịp", fld("an-e-shake")),
                v_("Đổi ngay", fld("")))


# --- an04
def _btn(extra=""):
    return (f'<span class="tp-btn an-swap an-sb {extra}"><span class="an-l0 type-label">Duyệt lệnh</span><span class="an-l1 an-spn">{icon("loader-circle")}</span>'
            f'<span class="an-l2">{icon("check")}</span></span>')


def pv_button():
    return grid(v_("Xoay rồi hiện dấu, giữ 1 giây, về nhãn", _btn(), mode="seq", seq="load:900,done:1000", rec=True),
                v_("Xoay rồi về nhãn, báo bằng toast", _btn(), mode="seq", seq="load:900"),
                v_("Xoay rồi hiện dấu, đứng nguyên", _btn(), mode="seq", seq="load:900,done:3000"))


# --- an05
def pv_icon():
    z = lambda c: f'<span class="tp-btn sec an-swap an-sc {c}"><span class="an-l1">{icon("copy")}</span><span class="an-l2">{icon("check")}</span></span><span class="type-code">TCLU 482915-3</span>'
    return grid(v_("Mờ chéo + phóng 95", f'<div class="an-inl">{z("")}</div>', mode="seq", seq="done:1000", rec=True),
                v_("Đổi ngay", f'<div class="an-inl">{z("an-hard")}</div>', mode="seq", seq="done:1000"))


# --- an06
def _rowt(c=""):
    r = lambda code, route, ch, x, k="": f'<div class="an-row {k}"><span class="type-code">{code}</span><span class="type-body an-grow">{route}</span>{ch}</div>'
    swapchip = '<span class="an-chipw"><span class="tp-chip tp-y an-c0">Chờ duyệt</span><span class="tp-chip tp-b an-c1">Đang chạy</span></span>'
    return ('<div class="an-rows">' + r("LVT-2026-0411", "ICD Phước Long → Bình Dương", '<span class="tp-chip tp-g">Hoàn thành</span>', "")
            + r("LVT-2026-0412", "Cát Lái → KCN Long Hậu", swapchip, "", c)
            + r("LVT-2026-0409", "Hiệp Phước → Đồng Nai", '<span class="tp-chip tp-y">Chờ duyệt</span>', "") + "</div>")


def pv_flash():
    return grid(v_("Tô nền 1 giây rồi phai", _rowt("an-p-flash"), rec=True, cls="an-w an-chips"),
                v_("Chỉ chip đổi", _rowt(), cls="an-w an-chips"))


# --- an07
def _kpi(k):
    return f'<div class="tp-card an-kpi"><div class="type-caption tp-sub">Lệnh đang chạy</div><div class="type-display tp-num an-num" data-kind="{k}">128</div></div>'


def pv_number():
    return grid(v_("Số mờ dần", _kpi("fade"), fn="num", rec=True), v_("Đếm chạy 300", _kpi("count"), fn="num"), v_("Đổi ngay", _kpi("none"), fn="num"))


# --- an08
def _newrows(kind):
    row = lambda c, rt, cl="": f'<div class="an-row {cl}"><span class="type-code">{c}</span><span class="type-body an-grow">{rt}</span></div>'
    if kind == "pill":
        ins = '<div class="an-pillw"><span class="an-pill type-label">Có 2 lệnh mới</span></div>'
    else:
        ins = f'<div class="an-acc an-ins-{kind}"><div class="an-acc-b"><div>{row("LVT-2026-0413", "Cát Lái → Tân Tạo", "an-p-flash" if kind == "push" else "")}</div></div></div>'
    return f'<div class="an-rows">{ins}{row("LVT-2026-0412", "Cát Lái → KCN Long Hậu")}{row("LVT-2026-0411", "ICD Phước Long → Bình Dương")}</div>'


def pv_new():
    return grid(v_("Báo “Có 2 lệnh mới”, bấm mới chèn", _newrows("pill"), rec=True, cls="an-w"),
                v_("Tự chèn, dòng dưới bị đẩy xuống", _newrows("push"), cls="an-w"),
                v_("Tự chèn, không chạy", _newrows("hard"), cls="an-w"))


# --- an09
def _prog(k):
    return f'<div class="an-prog"><div class="type-caption an-prt"><span>Ảnh chứng từ.jpg</span><span class="tp-num an-prn">60%</span></div><div class="an-bar"><i class="an-bari {k}" style="transform:translateX(-40%)"></i></div></div>'


def pv_progress():
    return grid(v_("Trượt <code>duration/fast</code> theo mốc", _prog("an-smooth"), fn="prog", rec=True),
                v_("Nhảy theo mốc", _prog(""), fn="prog"),
                v_("Chưa biết %: spinner như <code>field-upload</code>", f'<div class="an-inl"><span class="an-spn an-keep">{icon("loader-circle")}</span><span class="type-body">Đang tải ảnh…</span></div>', mode="loop"))


# --- an10
def _acc(c=""):
    return (f'<div class="tp-card an-acc-card {c}"><div class="tp-top"><span class="type-title-3">Thông tin chuyến</span><span class="an-chev tp-fg2">{icon("chevron-down")}</span></div>'
            '<div class="an-acc-b"><div><div class="type-body an-acc-t">51C-482.15 · mooc 51R-091.44. Tài xế Nguyễn Văn Hoà nhận container tại cổng B, kiểm tra niêm phong trước khi rời cảng.</div></div></div></div>')


def pv_expand():
    return grid(v_("Mở <code>duration/medium</code>, đóng <code>duration/exit</code>", _acc(), mode="toggle", rec=True, btn="Mở/đóng"),
                v_("Cả hai <code>duration/fast</code>", _acc("an-accf"), mode="toggle", btn="Mở/đóng"),
                v_("Đổi ngay, chevron vẫn xoay", _acc("an-acc0"), mode="toggle", btn="Mở/đóng"))


# --- an11
def _sk(c):
    return (f'<div class="an-sk {c}"><div class="an-skh"><i></i><i></i><i></i></div><div class="an-skc"><div class="type-code tp-sub">LVT-2026-0412</div><div class="type-title-3">Cát Lái → KCN Long Hậu</div>'
            '<div class="type-body tp-sub">51C-482.15 · Nguyễn Văn Hoà</div></div></div>')


def pv_load():
    return grid(v_("Nội dung mờ dần <code>duration/fast</code>", _sk("an-skf"), mode="seq", seq="load:800,show:400", rec=True),
                v_("Đổi ngay", _sk(""), mode="seq", seq="load:800,show:400"),
                v_("Mờ dần + trượt 8, <code>duration/medium</code>", _sk("an-skm"), mode="seq", seq="load:800,show:600"))


# --- an12
def _map(k):
    return f'<div class="an-map" data-kind="{k}"><svg viewBox="0 0 240 120" preserveAspectRatio="none" aria-hidden="true"><path d="M10 100 C 60 100, 70 30, 120 40 S 190 90, 232 20" fill="none" stroke="currentColor" stroke-width="3" stroke-dasharray="1 7" stroke-linecap="round"/></svg><span class="an-mk an-mk2">{icon("truck", "tp-ic-sm")}</span></div>'


def pv_map():
    return grid(v_("Trượt <code>duration/medium</code> khi có điểm mới", _map("glide"), fn="map", rec=True, cls="an-w"),
                v_("Nội suy suốt chu kỳ, linear", _map("lerp"), fn="map", cls="an-w"),
                v_("Nhảy tới điểm mới", _map("jump"), fn="map", cls="an-w"))


# --- an13
def _steps(c=""):
    s = lambda n, cl: f'<span class="an-step {cl}"><i></i><b class="type-caption">{n}</b></span>'
    return (f'<div class="an-steps {c}">{s("Nhận lệnh", "on")}<span class="an-link on"><i></i></span>{s("Đến cảng", "on")}<span class="an-link an-nxt"><i></i></span>{s("Đang chạy", "an-nxtd")}<span class="an-link"><i></i></span>{s("Hoàn thành", "")}</div>')


def pv_steps():
    return grid(v_("Vạch chạy <code>duration/medium</code>, chấm đổi <code>duration/fast</code> nối tiếp", _steps("an-sf"), rec=True, cls="an-w"),
                v_("Đổi ngay", _steps("an-s0"), cls="an-w"))


# --- an14
def _scan(c):
    return f'<div class="an-cam {c}"><i class="k a"></i><i class="k b"></i><i class="k c"></i><i class="k d"></i><i class="an-line"></i><span class="an-camok">{CHECK}</span></div>'


def pv_scan():
    return grid(v_("Khung đứng yên, nhận mã thì xanh + vẽ dấu", _scan("an-c1"), mode="seq", seq="done:1400", rec=True),
                v_("Vạch quét chạy lặp, tối đa 5 giây", _scan("an-c2"), mode="loop"),
                v_("Khung đứng yên, nhận mã thì sang màn sau", _scan("an-c3"), mode="seq", seq="done:400"))


# --- an15
def _pull(k):
    head = {"sys": f'<span class="an-spn an-keep">{icon("loader-circle")}</span>', "truck": f'<span class="an-truck">{icon("truck", "tp-ic-lg")}</span>'}[k]
    row = lambda c: f'<div class="an-row"><span class="type-code">{c}</span></div>'
    return f'<div class="an-pull"><div class="an-pullh">{head}</div><div class="an-pullb">{row("LVT-2026-0412")}{row("LVT-2026-0411")}{row("LVT-2026-0409")}</div></div>'


def pv_pull():
    return grid(v_("Của nền tảng: <code>RefreshIndicator</code> trên Android, kiểu Cupertino trên iOS", _pull("sys"), mode="seq", seq="pull:1300", rec=True),
                v_("Tự vẽ: xe tải chạy qua", _pull("truck"), mode="seq", seq="pull:1300"))


# --- an16
def _off(k):
    return (f'<div class="an-off {k}"><div class="an-offb"><div><div class="an-offi an-bad">{icon("wifi-off")}<span class="type-label">Mất mạng. Đã lưu trên máy, sẽ gửi khi có mạng.</span></div>'
            f'<div class="an-offi an-good">{icon("wifi")}<span class="type-label">Đã có mạng lại</span></div></div></div><div class="an-offc"><div class="type-title-3">Lệnh của tôi</div><div class="type-body tp-sub">3 lệnh trong hôm nay</div></div></div>')


def pv_offline():
    return grid(v_("Dải mở cao đẩy nội dung, có mạng thì xanh 1 giây rồi đóng", _off("an-o1"), mode="seq", seq="off:1500,back:1000,close:400", rec=True),
                v_("Dải mờ dần đè lên nội dung", _off("an-o2"), mode="seq", seq="off:1500,back:1000,close:400"),
                v_("Đổi ngay", _off("an-o3"), mode="seq", seq="off:1500,back:1000"))


# --- an17
def _chart(k):
    hs = [46, 68, 38, 84, 60, 72]
    bars = "".join(f'<i style="height:{h}%;--i:{n}"></i>' for n, h in enumerate(hs))
    return f'<div class="an-chart {k}">{bars}</div>'


def pv_chart():
    return grid(v_("Mờ dần <code>duration/fast</code>, cột đứng yên", _chart("an-ch1"), rec=True),
                v_("Không chạy, như Untitled", _chart("")),
                v_("Cột mọc <code>duration/medium</code>", _chart("an-ch2")),
                v_("Cột mọc lần lượt, tổng 300", _chart("an-ch3")))


# ---------- màn thật chạy được ----------
def overlay(_body):
    nav = lambda ic, x, on="": f'<div class="tp-nav {on}">{icon(ic)}<span class="type-label">{x}</span></div>'
    rw = lambda code, r, s, m, ch, k="": (f'<tr class="{k}"><td><div class="type-code">{code}</div></td><td>{ch}</td><td><div class="type-body">{r}</div><div class="type-caption tp-sub">{s}</div></td>'
                                          f'<td><span class="type-body tp-num">{m}</span></td></tr>')
    chipsw = '<span class="an-chipw"><span class="tp-chip tp-y an-c0">Chờ duyệt</span><span class="tp-chip tp-b an-c1">Đang chạy</span></span>'
    web = (f'<div class="tp-f tp-web an-scene" id="anWeb" data-platform="web"><aside class="tp-side"><div class="tp-logo">{kit.mini_mark()}</div><div class="type-caption-caps tp-grp">Vận hành</div>'
           f'{nav("clipboard-list", "Lệnh vận tải", "on")}{nav("container", "Phương tiện")}{nav("user-round", "Tài xế")}{nav("fuel", "Nhiên liệu")}</aside>'
           '<div class="tp-main"><div class="tp-top"><div><div class="type-title-1">Lệnh vận tải</div><div class="type-body tp-sub">Theo dõi và duyệt lệnh trong ngày.</div></div></div>'
           '<div class="tp-kpis"><div class="tp-card"><div class="type-caption tp-sub">Lệnh đang chạy</div><div class="type-display tp-num an-num" id="anK1">128</div></div>'
           '<div class="tp-card"><div class="type-caption tp-sub">Chờ duyệt</div><div class="type-display tp-num an-num" id="anK2">16</div></div>'
           '<div class="tp-card"><div class="type-caption tp-sub">Doanh thu hôm nay</div><div class="type-display tp-num">412 tr ₫</div></div></div>'
           '<div class="tp-card"><div class="an-inl"><span class="type-title-3">Danh sách lệnh</span><span class="an-newpill"><span class="an-pill type-label">Có 2 lệnh mới</span></span></div><table class="tp-tb"><thead><tr><th><span class="type-caption-caps">Mã lệnh</span></th><th><span class="type-caption-caps">Trạng thái</span></th><th><span class="type-caption-caps">Tuyến · xe</span></th><th><span class="type-caption-caps">Cước</span></th></tr></thead><tbody>'
           + rw("LVT-2026-0411", "ICD Phước Long → Bình Dương", "51D-120.77 · Trần Quốc Việt", "2.480.000 ₫", '<span class="tp-chip tp-g">Hoàn thành</span>')
           + rw("LVT-2026-0412", "Cát Lái → KCN Long Hậu", "51C-482.15 · Nguyễn Văn Hoà", "1.250.000 ₫", chipsw, "an-sflash")
           + rw("LVT-2026-0409", "Cảng Hiệp Phước → Đồng Nai", "50H-338.02 · Lê Thị Ệ", "980.000 ₫", '<span class="tp-chip tp-y">Chờ duyệt</span>')
           + "</tbody></table></div></div></div>")
    app = (f'<div class="tp-f tp-app an-scene" id="anApp" data-platform="mobile"><div class="an-off an-o1"><div class="an-offb"><div><div class="an-offi an-bad">{icon("wifi-off")}<span class="type-label">Mất mạng. Đã lưu trên máy, sẽ gửi khi có mạng.</span></div>'
           f'<div class="an-offi an-good">{icon("wifi")}<span class="type-label">Đã có mạng lại</span></div></div></div></div>'
           f'<div class="tp-appbar"><div style="flex:1;min-width:0"><div class="type-title-2">Chi tiết lệnh</div><div class="type-caption tp-sub">LVT-2026-0412</div></div><span class="tp-fg2">{icon("bell", "tp-ic-lg")}</span></div>'
           f'<div class="tp-pad"><div class="tp-card"><div class="type-heading">Tiến độ chuyến</div>{_steps("an-sf")}</div><div class="tp-card"><div class="type-heading">Thông tin chuyến</div><div class="type-body">Cảng Cát Lái → KCN Long Hậu, Cần Giuộc, Long An</div><div class="type-caption tp-sub">51C-482.15 · mooc 51R-091.44</div></div></div>'
           f'<div class="tp-foot"><span class="tp-btn wide an-swap an-sb"><span class="an-l0 type-label">Đến nơi giao hàng</span><span class="an-l1 an-spn">{icon("loader-circle")}</span><span class="an-l2">{icon("check")}</span></span></div></div>')
    return ('<div class="an-scenebar"><button class="tp-btn an-scenego" type="button" id="anGo"><span class="type-label">Chạy kịch bản 6 giây</span></button>'
            '<span class="type-caption an-lab" id="anLog">Bấm để xem toàn bộ phương án khuyến nghị trên một chuyến xe.</span></div>'
            f'<div class="tp-h">Web <small>· điều vận thấy lệnh đổi trạng thái (an06, an07, an08)</small></div><div class="tp-scroll"><div class="tp-row">{web}</div></div>'
            f'<div class="tp-h">App <small>· lái xe mất mạng, có lại, báo đến nơi (an16, an04, an13)</small></div><div class="tp-scroll"><div class="tp-row">{app}</div></div>')


# ---------- CSS ----------
CSS = r"""
body.an-rm{--duration-fast:0ms;--duration-medium:0ms;--duration-slow:0ms;--duration-exit:0ms}
.an-rmbar{display:flex;flex-wrap:wrap;gap:8px 12px;align-items:center;margin:8px 0;padding:8px 12px;background:#fff;border:1px solid #E2E8F0;border-radius:10px}
.an-nt,.an-nt *{transition:none!important;animation:none!important}
.pane code{background:var(--color-bg-tertiary);color:inherit}
.an-vars{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:var(--space-lg)}
.an-st{display:grid;gap:var(--space-sm);align-content:start;min-width:0}.an-st.an-w{grid-column:1/-1}
.an-head{display:flex;justify-content:space-between;align-items:center;gap:var(--space-md);min-height:32px}
.an-lab{color:var(--color-text-secondary);min-width:0}.an-lab code{font-size:11px}
.an-rec{display:inline-block;margin-left:6px;color:var(--color-text-success-primary);font-weight:600}
.an-play{height:28px;padding:0 var(--space-md);cursor:pointer;border:0;font:inherit;flex:none}.an-play:focus-visible,.an-scenego:focus-visible{outline:2px solid var(--color-action-primary);outline-offset:2px}
.an-box{min-height:88px;display:grid;align-items:center;min-width:0}
.an-col{display:grid;justify-items:center;gap:var(--space-sm)}.an-msg{text-align:center}.an-inl{display:flex;align-items:center;gap:var(--space-md);min-width:0;flex-wrap:wrap}
.an-grow{flex:1;min-width:0}
/* preset */
@keyframes an-fade{from{opacity:0}to{opacity:1}}
@keyframes an-fadeup{from{opacity:0;transform:translateY(4px)}to{opacity:1;transform:none}}
@keyframes an-up8{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
@keyframes an-draw{from{stroke-dashoffset:1}to{stroke-dashoffset:0}}
@keyframes an-flash{0%,66%{background:var(--color-utility-blue-50)}100%{background:transparent}}
@keyframes an-shake{0%,100%{transform:none}17%,50%,83%{transform:translateX(-4px)}33%,67%{transform:translateX(4px)}}
@keyframes an-border{from{border-color:var(--color-border-input)}to{border-color:var(--color-border-error)}}
@keyframes an-spin{to{transform:rotate(360deg)}}
.an-p-fade{}.go .an-p-fade,.go.an-p-fade{animation:an-fade var(--duration-fast) var(--easing-standard) both}
.an-chk{width:24px;height:24px;display:block}.an-chk path{stroke-dasharray:1;stroke-dashoffset:0}
.an-ok{width:44px;height:44px;border-radius:var(--radius-full);display:grid;place-items:center;background:var(--color-bg-success-primary);color:var(--color-fg-success-primary)}
.go .an-p-draw .an-chk path{animation:an-draw var(--duration-medium) var(--easing-standard) both}
.go .an-p-draw{animation:an-fade var(--duration-fast) var(--easing-standard) both}
.go .an-p-flash{animation:an-flash calc(var(--duration-slow) * 3) linear both}
.go .an-e-fade .an-hint{animation:an-fadeup var(--duration-fast) var(--easing-standard) both}.go .an-e-fade .tp-inp{animation:an-border var(--duration-fast) var(--easing-standard) both}
.go .an-e-shake .tp-inp{animation:an-shake var(--duration-medium) linear both}
/* kết quả theo mẫu an02 */
.an-pair{display:grid;grid-template-columns:1fr 1fr;gap:var(--space-sm)}
.an-res{position:relative;width:56px;height:56px;display:grid;place-items:center;color:var(--color-fg-white)}.an-res i{position:absolute;border-radius:var(--radius-full)}.an-r1{inset:0}.an-r2{inset:6px}.an-res svg{position:relative;width:26px;height:26px}.an-res path{stroke-dasharray:1;stroke-dashoffset:0}
.an-res-ok .an-r1{background:var(--color-bg-success-secondary)}.an-res-ok .an-r2{background:var(--color-bg-success-solid)}.an-res-no .an-r1{background:var(--color-bg-error-secondary)}.an-res-no .an-r2{background:var(--color-bg-error-solid)}
@keyframes an-pop{from{transform:scale(0)}to{transform:none}}
@keyframes an-pop-b{0%{transform:scale(0)}45%{transform:scale(1.12)}70%{transform:scale(.94)}100%{transform:none}}
.go .an-r-stage .an-r1{animation:an-pop var(--duration-medium) var(--easing-standard) both}.go .an-r-stage .an-r2{animation:an-pop var(--duration-medium) var(--easing-standard) var(--duration-fast) both}
.go .an-r-stage .an-s1{animation:an-draw var(--duration-medium) var(--easing-standard) var(--duration-medium) both}.go .an-r-stage .an-res-no .an-s1,.go .an-res-no.an-r-stage .an-s1{animation-duration:var(--duration-fast)}.go .an-res-no.an-r-stage .an-s2{animation:an-draw var(--duration-fast) var(--easing-standard) calc(var(--duration-medium) + var(--duration-fast)) both}
.go .an-r-bounce .an-r1,.go .an-res.an-r-bounce .an-r1{animation:an-pop-b calc(var(--duration-slow) * 2) linear both}.go .an-r-bounce .an-r2{animation:an-pop-b calc(var(--duration-slow) * 2) linear var(--duration-fast) both}
.go .an-r-bounce .an-s1{animation:an-draw var(--duration-medium) var(--easing-standard) var(--duration-slow) both}.go .an-res-no.an-r-bounce .an-s2{animation:an-draw var(--duration-medium) var(--easing-standard) calc(var(--duration-slow) + var(--duration-fast)) both}
.go .an-r-one .an-r1,.go .an-r-one .an-r2{animation:an-fade var(--duration-fast) var(--easing-standard) both}.go .an-r-one path{animation:an-draw var(--duration-medium) var(--easing-standard) both}
/* đổi tại chỗ */
.an-swap{display:inline-grid;place-items:center}.an-swap>*{grid-area:1/1;transition:opacity var(--duration-fast) var(--easing-standard),transform var(--duration-fast) var(--easing-standard)}
.an-swap .an-l1,.an-swap .an-l2{opacity:0;transform:scale(.95)}.an-sc .an-l1,.an-big .an-l1{opacity:1;transform:none}.an-big{justify-self:center}
.an-sb{min-width:132px;width:fit-content}.tp-btn.wide.an-sb{width:100%}
[data-s=load] .an-sb .an-l0{opacity:0}[data-s=load] .an-sb .an-l1{opacity:1;transform:none}
[data-s=done] .an-sb .an-l0{opacity:0}[data-s=done] .an-sb .an-l2{opacity:1;transform:none}
[data-s=done] .an-sc .an-l1,[data-s=done] .an-big .an-l1{opacity:0;transform:scale(.95)}[data-s=done] .an-sc .an-l2,[data-s=done] .an-big .an-l2{opacity:1;transform:none;color:var(--color-fg-success-primary)}
.an-hard>*{transition:none}.an-sc{width:36px;padding:0}
.an-spn{display:inline-flex}.an-spn svg{animation:an-spin calc(var(--duration-slow) * 2) linear infinite}
body.an-rm .an-spn svg{animation:none}
/* dòng */
.an-rows{display:grid;border:1px solid var(--color-border-secondary);border-radius:var(--radius-md);overflow:hidden}
.an-row{display:flex;align-items:center;gap:var(--space-md);padding:var(--space-md) var(--space-lg);border-bottom:1px solid var(--color-border-secondary);min-width:0;flex-wrap:wrap}.an-rows>:last-child .an-row,.an-rows>.an-row:last-child{border-bottom:0}
.an-chipw{display:inline-grid}.an-chipw>*{grid-area:1/1;justify-self:end;transition:opacity var(--duration-fast) var(--easing-standard)}.an-c1{opacity:0}
.go.an-chips .an-c0,.go .an-sflash .an-c0{opacity:0}.go.an-chips .an-c1,.go .an-sflash .an-c1{opacity:1}
.go .an-sflash td{animation:an-flash calc(var(--duration-slow) * 3) linear both}
/* số */
.an-kpi{gap:var(--space-xxs)}.an-num.an-run{animation:an-fade var(--duration-fast) var(--easing-standard) both}
/* dòng mới */
.an-pillw{display:flex;justify-content:center;padding:var(--space-xs);overflow:hidden;height:0;padding:0}
.go .an-pillw{height:auto;padding:var(--space-xs);animation:an-fadeup var(--duration-fast) var(--easing-standard) both}
.an-pill{display:inline-flex;height:24px;align-items:center;padding:0 var(--space-md);border-radius:var(--radius-full);background:var(--color-action-primary);color:var(--color-text-inverse)}
.an-newpill{opacity:0;transition:opacity var(--duration-fast) var(--easing-standard)}.go .an-newpill{opacity:1}
.an-acc-b{display:grid;grid-template-rows:0fr;transition:grid-template-rows var(--duration-exit) var(--easing-exit)}.an-acc-b>div{overflow:hidden;min-height:0}.an-acc-t{padding-top:var(--space-xs)}
.open .an-acc-b,.go .an-ins-push .an-acc-b{grid-template-rows:1fr;transition:grid-template-rows var(--duration-medium) var(--easing-standard)}
.go .an-ins-hard .an-acc-b{grid-template-rows:1fr;transition:none}
.an-accf .an-acc-b,.open .an-accf .an-acc-b{transition-duration:var(--duration-fast)}.an-acc0 .an-acc-b,.open .an-acc0 .an-acc-b{transition:none}
.an-chev{display:inline-flex;transition:transform var(--duration-fast) var(--easing-standard)}.open .an-chev{transform:rotate(180deg)}
/* tiến độ */
.an-prog{display:grid;gap:var(--space-xs)}.an-prt{display:flex;justify-content:space-between;gap:var(--space-md)}
.an-bar{height:8px;border-radius:var(--radius-full);background:var(--color-bg-quaternary);overflow:hidden}.an-bari{display:block;height:100%;border-radius:inherit;background:var(--color-action-primary)}
.an-smooth{transition:transform var(--duration-fast) linear}
.an-keep svg{width:var(--icon-size-lg);height:var(--icon-size-lg);animation-play-state:paused}.go .an-keep svg,[data-s] .an-keep svg{animation-play-state:running}
/* tải → nội dung */
.an-sk{position:relative;min-height:88px}.an-skh{display:none;gap:var(--space-sm)}.an-skh i{display:block;height:14px;border-radius:var(--radius-sm);background:var(--color-bg-quaternary)}.an-skh i:nth-child(2){width:80%}.an-skh i:nth-child(3){width:55%}
[data-s=load] .an-skh{display:grid}[data-s=load] .an-skc{display:none}
[data-s=show] .an-skf .an-skc{animation:an-fade var(--duration-fast) var(--easing-standard) both}[data-s=show] .an-skm .an-skc{animation:an-up8 var(--duration-medium) var(--easing-standard) both}
/* bản đồ */
.an-map{position:relative;height:120px;border-radius:var(--radius-md);background:var(--color-bg-secondary);color:var(--color-border-primary);overflow:hidden;border:1px solid var(--color-border-secondary)}.an-map svg:first-child{width:100%;height:100%;display:block}
.an-mk{position:absolute;display:grid;place-items:center;width:28px;height:28px;border-radius:var(--radius-full);background:var(--color-action-primary);color:var(--color-text-inverse)}
.an-mk2{left:0;top:0;transform:translate(8px,84px)}
.an-glide{position:relative;height:60px}.an-glide .an-mk{left:0;top:16px;transition:left var(--duration-medium) var(--easing-standard)}.open .an-glide .an-mk{left:calc(100% - 28px)}
/* bước */
.an-steps{display:flex;align-items:flex-start;gap:var(--space-xs);min-width:0}.an-step{display:grid;justify-items:center;gap:var(--space-xs);flex:none;width:64px;text-align:center}.an-step i{display:block;width:14px;height:14px;border-radius:var(--radius-full);background:var(--color-bg-quaternary)}.an-step.on i{background:var(--color-action-primary)}
.an-step b{font-weight:400;color:var(--color-text-tertiary)}.an-step.on b{color:var(--color-text-primary)}
.an-link{flex:1;height:2px;margin:6px -18px 0;background:var(--color-bg-quaternary);overflow:hidden;min-width:8px}.an-link i{display:block;height:100%;background:var(--color-action-primary);transform:scaleX(0);transform-origin:left}.an-link.on i{transform:none}
.an-nxtd i{transition:background-color var(--duration-fast) var(--easing-standard) var(--duration-medium)}.an-s0 .an-nxtd i{transition:none}.an-nxt i{transition:transform var(--duration-medium) var(--easing-standard)}.an-s0 .an-nxt i{transition:none}
.go .an-nxt i,[data-ok] .an-nxt i{transform:none}.go .an-nxtd i,[data-ok] .an-nxtd i{background:var(--color-action-primary)}
/* quét */
.an-cam{position:relative;height:128px;border-radius:var(--radius-md);background:var(--neutral-900);overflow:hidden;color:var(--color-text-white,var(--neutral-50))}
.an-cam .k{position:absolute;width:22px;height:22px;border:2px solid var(--neutral-50);transition:border-color var(--duration-fast) var(--easing-standard)}
.an-cam .a{left:22%;top:14%;border-right:0;border-bottom:0}.an-cam .b{right:22%;top:14%;border-left:0;border-bottom:0}.an-cam .c{left:22%;bottom:14%;border-right:0;border-top:0}.an-cam .d{right:22%;bottom:14%;border-left:0;border-top:0}
.an-line{position:absolute;left:24%;right:24%;top:18%;height:2px;background:var(--color-fg-success-secondary);opacity:0}
@keyframes an-scan{from{top:18%}to{top:80%}}
.go .an-c2 .an-line{opacity:1;animation:an-scan calc(var(--duration-slow) * 2) linear infinite alternate}
.an-camok{position:absolute;inset:0;display:grid;place-items:center;opacity:0;color:var(--color-fg-success-secondary)}
[data-s=done] .an-c1 .k,[data-s=done] .an-c3 .k{border-color:var(--color-fg-success-secondary)}
[data-s=done] .an-c1 .an-camok{opacity:1}[data-s=done] .an-c1 .an-chk path{animation:an-draw var(--duration-medium) var(--easing-standard) both}
/* kéo làm mới */
.an-pull{overflow:hidden;border:1px solid var(--color-border-secondary);border-radius:var(--radius-md);position:relative;height:128px}
.an-pullh{position:absolute;left:0;right:0;top:12px;display:flex;justify-content:center;opacity:0;transition:opacity var(--duration-fast) var(--easing-standard);color:var(--color-fg-secondary)}
.an-pullb{transition:transform var(--duration-medium) var(--easing-standard);background:var(--color-bg-primary)}
[data-s=pull] .an-pullh{opacity:1}[data-s=pull] .an-pullb{transform:translateY(44px)}
.an-truck{display:inline-flex}@keyframes an-truck{from{transform:translateX(-90px)}to{transform:translateX(90px)}}[data-s=pull] .an-truck{animation:an-truck calc(var(--duration-slow) * 2) linear infinite}
/* mất mạng */
.an-off{border-radius:var(--radius-md);overflow:hidden;position:relative}.an-st .an-off{border:1px solid var(--color-border-secondary);min-height:96px}
.an-offb{display:grid;grid-template-rows:0fr;transition:grid-template-rows var(--duration-exit) var(--easing-exit)}.an-offb>div{overflow:hidden;min-height:0;position:relative}
.an-offi{display:flex;align-items:flex-start;gap:var(--space-md);padding:var(--space-md) var(--space-lg)}.an-bad{background:var(--color-bg-warning-primary);color:var(--color-text-primary)}.an-good{display:none;background:var(--color-bg-success-primary);color:var(--color-text-success-primary)}
[data-s=back] .an-bad{display:none}[data-s=back] .an-good{display:flex}
[data-s=off] .an-offb,[data-s=back] .an-offb{grid-template-rows:1fr;transition:grid-template-rows var(--duration-medium) var(--easing-standard)}
.an-offc{padding:var(--space-md) var(--space-lg)}
.an-o2 .an-offb{position:absolute;left:0;right:0;top:0;z-index:1;opacity:0;grid-template-rows:1fr;transition:opacity var(--duration-exit) var(--easing-exit)}[data-s=off] .an-o2 .an-offb,[data-s=back] .an-o2 .an-offb{opacity:1;transition:opacity var(--duration-medium) var(--easing-standard)}
.an-o3 .an-offb,[data-s=off] .an-o3 .an-offb,[data-s=back] .an-o3 .an-offb{transition:none}
/* biểu đồ */
.an-chart{height:96px;display:flex;align-items:flex-end;gap:var(--space-sm);border-bottom:1px solid var(--color-border-secondary)}.an-chart i{flex:1;display:block;border-radius:var(--radius-sm) var(--radius-sm) 0 0;background:var(--color-utility-blue-500);transform-origin:bottom}
@keyframes an-grow{from{transform:scaleY(0)}to{transform:none}}
.go .an-ch1{animation:an-fade var(--duration-fast) var(--easing-standard) both}.go .an-ch2 i{animation:an-grow var(--duration-medium) var(--easing-standard) both}
.go .an-ch3 i{animation:an-grow var(--duration-fast) var(--easing-standard) both;animation-delay:calc((var(--duration-medium) - var(--duration-fast)) / 5 * var(--i))}
/* thang */
.an-tls{display:grid;gap:var(--space-sm)}.an-tl{display:grid;grid-template-columns:minmax(0,300px) minmax(0,1fr) 44px;gap:var(--space-md);align-items:center}.an-tl code{font-size:11px}.an-tlb{display:block;height:10px;background:var(--color-bg-tertiary);border-radius:var(--radius-full);overflow:hidden}.an-tlb i{display:block;height:100%;background:var(--color-action-primary);border-radius:inherit}.an-tlb i.an-calc{background:var(--color-utility-blue-500)}
.an-tl .tp-num{text-align:right}
/* cảnh */
.an-scenebar{display:flex;flex-wrap:wrap;gap:var(--space-md);align-items:center;margin:8px 0}.an-scenego{border:0;font:inherit;cursor:pointer}
.an-scene .tp-app{min-height:0}.tp-app.an-scene{min-height:560px}
@media(max-width:820px){.an-tl{grid-template-columns:minmax(0,1fr) 44px}.an-tlb{display:none}}
"""

# ---------- JS ----------
JS = r"""
(function(){
 const fmt=n=>String(n);
 const dur=(el,n)=>parseFloat(getComputedStyle(el).getPropertyValue(n))||0;
 const clear=s=>{(s._ts||[]).forEach(clearTimeout);s._ts=[];if(s._raf)cancelAnimationFrame(s._raf)};
 const later=(s,f,ms)=>{s._ts=s._ts||[];s._ts.push(setTimeout(f,ms))};
 const bump=(el,c)=>{el.classList.remove(c);void el.offsetWidth;el.classList.add(c)};
 const rewind=(el,fn)=>{el.classList.add('an-nt');fn();void el.offsetWidth;el.classList.remove('an-nt');void el.offsetWidth};
 const FN={
  num(s){const n=s.querySelector('.an-num'),k=n.dataset.kind,from=+n.textContent,to=from===128?131:128;
   if(k==='none'){n.textContent=fmt(to);return}
   if(k==='fade'){n.textContent=fmt(to);bump(n,'an-run');return}
   const T=dur(s,'--duration-medium'),t0=performance.now();if(!T){n.textContent=fmt(to);return}
   const step=t=>{const p=Math.min(1,(t-t0)/T);n.textContent=fmt(Math.round(from+(to-from)*p));if(p<1)s._raf=requestAnimationFrame(step)};s._raf=requestAnimationFrame(step)},
  prog(s){const b=s.querySelector('.an-bari'),l=s.querySelector('.an-prn');[12,31,58,76,100].forEach((p,i)=>later(s,()=>{b.style.transform=`translateX(-${100-p}%)`;l.textContent=p+'%'},i*420));
   b.style.transform='translateX(-100%)';l.textContent='0%'},
  map(s){const pts=[[3,70],[30,18],[52,30],[80,8]],box=s.querySelector('.an-map'),m=box.querySelector('.an-mk2'),k=box.dataset.kind;const T=2000;
   m.style.transition=k==='glide'?'transform var(--duration-medium) var(--easing-standard)':k==='lerp'?`transform ${T}ms linear`:'none';
   const place=([x,y])=>{const w=box.clientWidth,h=box.clientHeight;m.style.transform=`translate(${x*w/100}px,${y*h/100}px)`};
   m.style.transition='none';place(pts[0]);void m.offsetWidth;
   m.style.transition=k==='glide'?'transform var(--duration-medium) var(--easing-standard)':k==='lerp'?`transform ${T}ms linear`:'none';
   pts.slice(1).forEach((p,i)=>later(s,()=>place(p),(i*T)+60))}
 };
 document.addEventListener('click',e=>{const b=e.target.closest('.an-play');if(!b)return;const s=b.closest('.an-st'),m=s.dataset.mode;clear(s);
  const lab=b.querySelector('.type-label');
  if(s.dataset.fn){FN[s.dataset.fn](s);return}
  if(m==='toggle'){s.classList.toggle('open');return}
  if(m==='loop'){if(s.classList.contains('go')){s.classList.remove('go');lab.textContent='Phát';return}s.classList.add('go');lab.textContent='Dừng';later(s,()=>{s.classList.remove('go');lab.textContent='Phát'},5000);return}
  if(m==='seq'||s.dataset.seq){rewind(s,()=>s.removeAttribute('data-s'));let at=0;s.dataset.seq.split(',').forEach(x=>{const [n,t]=x.split(':');later(s,()=>s.setAttribute('data-s',n),at);at+=+t});later(s,()=>s.removeAttribute('data-s'),at);return}
  rewind(s,()=>s.classList.remove('go'));s.classList.add('go')});
 // giả lập giảm chuyển động: đưa bốn biến thời gian về 0 như tokens.css làm khi máy bật
 const rm=document.getElementById('anRm');
 if(rm)rm.addEventListener('click',e=>{const x=e.target.closest('button');if(!x)return;rm.querySelectorAll('button').forEach(y=>y.setAttribute('aria-pressed',String(y===x)));document.body.classList.toggle('an-rm',x.dataset.v==='on')});
 const note=document.getElementById('anRmNote');if(note&&matchMedia('(prefers-reduced-motion: reduce)').matches)note.textContent='Máy này đang bật giảm chuyển động nên các bản xem thử hiện ngay. Tắt trong cài đặt máy để xem chuyển động.';
 // kịch bản một chuyến xe
 const go=document.getElementById('anGo');
 if(go)go.addEventListener('click',()=>{const W=document.getElementById('anWeb'),A=document.getElementById('anApp'),L=document.getElementById('anLog'),K1=document.getElementById('anK1'),K2=document.getElementById('anK2'),S=go;clear(S);
  const tell=t=>{L.textContent=t};rewind(W,()=>W.classList.remove('go'));rewind(A,()=>{A.removeAttribute('data-s');A.removeAttribute('data-ok')});K1.textContent='128';K2.textContent='16';
  tell('App: mất mạng, dải cảnh báo mở, nội dung bị đẩy xuống.');A.setAttribute('data-s','off');
  later(S,()=>{tell('App: có mạng lại, dải xanh giữ 1 giây.');A.setAttribute('data-s','back')},1500);
  later(S,()=>{tell('App: dải đóng. Lái xe bấm Đến nơi giao hàng, nút xoay.');A.setAttribute('data-s','load')},2500);
  later(S,()=>{tell('App: xong, nút hiện dấu 1 giây, vạch tiến độ chạy sang bước Đang chạy.');A.setAttribute('data-s','done');A.setAttribute('data-ok','1')},3400);
  later(S,()=>{A.removeAttribute('data-s')},4400);
  later(S,()=>{tell('Web: dòng vừa đổi được tô rồi phai, chip đổi, số mờ dần, báo “Có 2 lệnh mới” thay vì tự đẩy bảng.');W.classList.add('go');K1.textContent='129';K2.textContent='15';bump(K1,'an-run');bump(K2,'an-run')},3500);
  later(S,()=>tell('Xong. Bấm lại để xem lần nữa, đổi Tối hoặc bật giả lập giảm chuyển động để so.'),6000)});
})();
"""

# ---------- bảng ----------
CMP = [
    ["Dấu check vẽ nét", f"Không có; <code>pathLength</code> trong {U_PATHLEN} file", "Chưa có", OWN, "an02"],
    ["Rung ô lỗi", f"Không rung; {U_SHAKE} file có <code>shake</code>", "Không rung", OK, "an03"],
    ["Nút đang xử lý", "<code>button.tsx</code> <code>isLoading</code>: ẩn chữ, spinner giữa nút, không có pha xong", "Spinner chờ 300 (mt09), chưa có pha xong", OWN, "an04"],
    ["Đổi icon tại chỗ", f"Không có; {U_CLIP} file có <code>clipboard</code>", "Chưa có", OWN, "an05"],
    ["Tô dòng vừa đổi", f"Không có; {U_FLASH} file", "Chưa có; mt16 đã bỏ chấm nhấp nháy", OWN, "an06"],
    ["Số đổi", f"Không có; {U_COUNT} file đếm chạy", "Chưa có", OWN, "an07"],
    ["Dòng mới từ máy chủ", "Không có", "mt17 chỉ phủ lọc, sắp xếp", OWN, "an08"],
    ["Thanh tiến độ", "<code>progress-indicators.tsx</code>: <code>transition duration-75 ease-linear</code>, chạy <code>transform</code>", "Có linear, chưa ghi số", DIFF, "an09"],
    ["Mở, đóng khối", f"Không có; {U_ACC} file <code>accordion</code>", "Chỉ có chevron (mt12)", OWN, "an10"],
    ["Skeleton sang nội dung", f"Không có; {U_SKEL} file <code>skeleton</code>", "Có skeleton, chưa có pha sang", OWN, "an11"],
    ["Xe trên bản đồ", f"Không có; {U_MAP} file bản đồ", "<code>map-marker.md</code> có xoay, chưa có chạy", OWN, "an12"],
    ["Tiến độ theo bước", f"Không có; {U_STEP} file <code>progress-steps</code>", "Chưa có", OWN, "an13"],
    ["Quét mã", f"Không có; {U_SCAN} file", "Chưa có", OWN, "an14"],
    ["Kéo làm mới", f"Không có; {U_PULL} file, Untitled là web", "Chưa có; mt14 giữ mặc định nền tảng", OWN, "an15"],
    ["Dải mất mạng", f"Không có; {U_OFFLINE} file đọc <code>navigator.onLine</code>", "Chưa có", OWN, "an16"],
    ["Biểu đồ", f"Tắt: {U_CHART_OFF} chỗ <code>isAnimationActive={{false}}</code> trong demo <code>charts</code>", "Chưa có luật", DIFF, "an17"],
]
CNT = collections.Counter(r[3] for r in CMP)
TABLE = rows(["Animation", "Untitled UI v8", "Mình đang có", "Trạng thái", "Mục"], [[a, b, c, st(d), f'<a href="#{e}">{e}</a>'] for a, b, c, d, e in CMP])

KEPT = rows(["Đã chốt", "Nội dung", "Ảnh hưởng tới trang"], [
    ["DEC-333", "Bốn thời gian 125 · 300 · 500 · 200, hai đường cong, hover, menu, dialog, sheet, toast, tab, skeleton, spinner, splash, giảm chuyển động, WCAG", "Mọi mục dưới đây chỉ dùng các số này"],
    ["DEC-333 (mt16)", "Bỏ chấm nhấp nháy trên danh sách, bảng, bản đồ", "Tô dòng an06 chạy một lần, không lặp"],
    ["DEC-333 (mt17)", "Dòng hiện lần lượt, chặn tổng 300, không khoá thao tác", "an08 và an17 không vượt mức chặn"],
    ["DEC-333 (mt14)", "Chuyển màn app giữ mặc định nền tảng", "an15 đi cùng hướng"],
    ["DEC-139", "Không bounce, không lò xo", "Không phương án nào nảy, kể cả dấu check"],
    ["DEC-327", "Lớp phủ 35% + <code>backdrop-blur/lg</code>", "Trang không đụng tới"],
])

BUNDLE = rows(["Mục", "Animation", "Thời gian", "Đường cong", "Thuộc tính chạy", "Giảm chuyển động"], [
    ["an02", "Dấu kết quả", "Đĩa <code>duration/medium</code>, đĩa trong trễ <code>duration/fast</code>, dấu sau <code>duration/medium</code>", "standard", "<code>transform</code>, <code>stroke-dashoffset</code>", "Hiện ngay"],
    ["an03", "Lỗi biểu mẫu", "<code>duration/fast</code>", "standard", "<code>opacity</code>, <code>border-color</code>", "Hiện ngay"],
    ["an04", "Nút xong", "<code>duration/fast</code>, giữ 1000", "standard", "<code>opacity</code>, <code>transform</code>", "Đổi ngay, vẫn giữ 1000"],
    ["an05", "Đổi icon", "<code>duration/fast</code>, giữ 1000", "standard", "<code>opacity</code>, <code>transform</code>", "Đổi ngay, vẫn giữ 1000"],
    ["an06", "Tô dòng", "Giữ 1000, phai <code>duration/slow</code>", "linear", "<code>background</code>", "Giữ nền 1500 rồi tắt ngay"],
    ["an07", "Số đổi", "<code>duration/fast</code>", "standard", "<code>opacity</code>", "Đổi ngay"],
    ["an08", "Báo dòng mới", "<code>duration/fast</code>", "standard", "<code>opacity</code>, trượt 4", "Hiện ngay"],
    ["an09", "Tiến độ", "<code>duration/fast</code>", "linear", "<code>transform</code>", "Nhảy theo mốc"],
    ["an10", "Mở, đóng khối", "Mở <code>duration/medium</code>, đóng <code>duration/exit</code>", "standard, exit", "<code>grid-template-rows</code>", "Đổi ngay"],
    ["an11", "Skeleton sang nội dung", "<code>duration/fast</code>", "standard", "<code>opacity</code>", "Đổi ngay"],
    ["an12", "Xe trên bản đồ", "<code>duration/medium</code>", "standard", "<code>transform</code>", "Nhảy tới điểm mới"],
    ["an13", "Tiến độ bước", "Vạch <code>duration/medium</code>, chấm <code>duration/fast</code> nối tiếp", "standard", "<code>transform</code>, <code>background</code>", "Đổi ngay"],
    ["an14", "Quét mã", "Khung <code>duration/fast</code>, dấu <code>duration/medium</code>", "standard", "<code>border-color</code>, <code>stroke-dashoffset</code>", "Hiện ngay"],
    ["an15", "Kéo làm mới", "Của nền tảng", "Của nền tảng", "Của nền tảng", "Theo nền tảng"],
    ["an16", "Dải mất mạng", "Mở <code>duration/medium</code>, đóng <code>duration/exit</code>", "standard, exit", "<code>grid-template-rows</code>", "Đổi ngay, vẫn giữ 1000"],
    ["an17", "Biểu đồ", "<code>duration/fast</code>", "standard", "<code>opacity</code>", "Hiện ngay"],
])

NONE = "Không có luật riêng trong <code>design/design.md</code> mục Motion."
FINAL = ("Khi bạn chốt: mình cập nhật <code>design-system/tokens.json</code> → sinh <code>design-system/tokens.css</code> + handoff → sửa <code>design-system/foundations/motion.md</code> (thêm mục 10.11 Animation bổ sung) → cập nhật biến Figma cùng lượt → ghi DEC; "
         "trang này không đổi trạng thái <b>motion</b>, vẫn chờ bạn đặt <b>motion = approved</b> (<code>ds-foundation-status.py set motion approved</code>) như trang Chuyển động. Component đang có bị đánh stale và sync dần (rule ds-stale). "
         "Việc riêng của trang: Figma không có biến thời gian, nên trên Figma chỉ ghi tên preset vào ghi chú prototype; sau đó ghi preset vào spec <code>design-system/components/application/field-upload.md</code>, <code>design-system/components/application/map-marker.md</code> và spec nút khi tới lượt.")

SPEC = dict(
    slug="animation", short="phần Animation bổ sung",
    title="Foundations · Animation bổ sung — 16 chuyển động còn thiếu",
    subtitle="Mở rộng trang Chuyển động (DEC-333) · chọn từng mục · 02/11/2026",
    lead=("<a href='https://claude.ai/artifact/4SWQns5vxjpAtfXP3J4NaY'>Trang Chuyển động</a> đã chốt <b>thời gian và đường cong</b> cho overlay, menu, toast, skeleton, spinner. Trang này định nghĩa phần còn thiếu: <mark>phản hồi sau thao tác, dữ liệu đổi khi đang xem, và các việc riêng của logistics</mark> như xe trên bản đồ, quét mã, mất mạng. "
          "Kết luận chính: <mark>không thêm bậc thời gian nào</mark>, chỉ thêm một bộ preset có tên để dev và AI không tự ghép. Trang chỉ chạy khi bạn bấm <b>Phát</b>. <mark>Chưa sửa token nào.</mark>"
          '</p><div class="an-rmbar"><span class="tp-lab">Giả lập giảm chuyển động</span><span class="tp-seg" id="anRm"><button data-v="off" aria-pressed="true">Tắt</button><button data-v="on" aria-pressed="false">Bật</button></span><span class="small muted" id="anRmNote">Bật để xem mỗi mục còn lại gì khi bốn biến thời gian về 0.</span></div><p class="small muted">'
          "<b>Vòng 2:</b> các mục khác đã chốt, chỉ còn <a href='#an02'>an02</a> cần chọn theo mẫu bạn gửi. Nhóm mục: Cấu trúc (an00, an01) · Phản hồi thao tác (an02 đến an05) · Dữ liệu đổi (an06 đến an11) · Logistics và app (an12 đến an16) · Biểu đồ (an17)."),
    kpis=[("16", "animation mới cần chốt", ""), ("0", "bậc thời gian thêm vào", "ok"), (str(CNT[GAP]), "chỗ Untitled có, mình thiếu", "ok" if not CNT[GAP] else "bad"), (str(CNT[OWN]), "chỗ chỉ mình cần", ""), (f"{U_FILES}", "file code Untitled đã đếm", "")],
    tag_kind=None,
    screens=dict(title="Xem trên màn thật",
                 intro="Một chuyến xe từ hai phía, dùng toàn bộ phương án khuyến nghị: lái xe trên app mất mạng rồi báo đến nơi, điều vận trên web thấy lệnh đổi. Web rộng 1280, menu 240 (DEC-039), app 393.",
                 overlay_html=overlay),
    sections=[
        dict(title="Bảng đối chiếu từng bậc — Untitled ↔ mình",
             intro=f"Đếm trên {U_FILES} file <code>.tsx</code> trong <code>design/_ref/untitled-ui/react/components</code>, bỏ demo. Số “file” là số file khớp từ khoá, có thể khớp vào phần không phải chuyển động; dòng ghi “Không có” nghĩa là không tìm thấy trong code đã tải về. Untitled là thư viện web, nên phần lái xe và logistics phải tự định nghĩa.",
             html=TABLE),
        dict(title="Đã chốt, không mở lại", html=KEPT),
        dict(title="Bộ chung đề xuất (nếu chọn hết theo khuyến nghị)",
             intro="Mỗi dòng dùng biến có sẵn, không có số trần. Cột cuối là việc code phải làm khi bật giảm chuyển động.", html=BUNDLE),
    ],
    items=[
        dict(id="an00", grp="Cấu trúc", title="Có cần thêm bậc thời gian không",
             why="16 animation mới đều ghép được từ bốn biến của DEC-333. Hai mốc mới là <mark>1000 để giữ dấu xong</mark> và <mark>1500 để tô dòng</mark>; cả hai là bội của <code>--duration-slow</code>, như cách <code>spinner/period</code> đang ghi <code>calc(var(--duration-slow) * 2)</code>. Viết kiểu đó thì giảm chuyển động tự về 0, nên phần giữ dấu và giữ nền phải đếm bằng bộ đếm giờ riêng.",
             untitled="Không có biến thời gian: <code>raw/theme.css</code> chỉ có <code>--animate-marquee</code>, <code>--animate-caret-blink</code>.",
             ours="<code>duration/fast</code> 125, <code>duration/exit</code> 200, <code>duration/medium</code> 300, <code>duration/slow</code> 500.",
             astryx="Ba dải 125 · 300 · 700 (<code>design/design.md</code> mục Motion).",
             tokens=[("duration/hold", "1000", "Chỉ khi chọn phương án thêm bậc")],
             pv=light(pv_scale),
             opts=[("keep", "Không thêm: ghi bội số của duration/slow, bộ đếm giờ giữ riêng", True), ("add", "Thêm duration/hold 1000, dùng chung cho spinner", False)]),
        dict(id="an01", grp="Cấu trúc", title="Đóng gói thành preset có tên hay chỉ ghi bảng luật",
             why="Bảng luật chỉ nói số; mỗi nơi vẫn tự viết <code>@keyframes</code>. Trong <code>design-system/components/_work</code> đã có <mark>5 tên keyframes tự đặt</mark> như <code>car</code>, <code>pl</code>, <code>spin-wait</code>. Preset có tên sinh một nguồn cho web và Flutter, AI vẽ màn cũng gọi được theo tên.",
             untitled="Dùng lớp có sẵn của Tailwind: <code>animate-in</code>, <code>fade-in</code>, <code>zoom-in-95</code>.",
             ours="<code>design-system/foundations/motion.md</code> mục 10.3 là bảng luật, không có preset.",
             astryx="Không có preset. <code>design/design.md</code> chỉ ghi dải và đường cong.",
             tokens=[("motion/preset/fade-in", "opacity 0 → 1, duration/fast, easing/standard", "Số, nội dung sau skeleton, biểu đồ"),
                     ("motion/preset/draw", "stroke-dashoffset 1 → 0, duration/medium, easing/standard", "Dấu kết quả"),
                     ("motion/preset/swap", "mờ chéo + phóng 95, duration/fast, easing/standard", "Đổi icon, nút xong"),
                     ("motion/preset/flash", "giữ 1000, phai duration/slow, linear", "Dòng vừa đổi"),
                     ("motion/preset/expand", "mở duration/medium + standard, đóng duration/exit + exit", "Khối mở rộng, dải mất mạng"),
                     ("motion/preset/glide", "transform, duration/medium, easing/standard", "Xe trên bản đồ")],
             note="Phụ thuộc an00: nếu chọn thêm <code>duration/hold</code> thì <code>motion/preset/flash</code> trỏ vào biến đó thay cho bội số.",
             pv=light(pv_presets),
             opts=[("preset", "Thêm 6 preset vào tokens.json, sinh @keyframes và InvMotion", True), ("doc", "Chỉ ghi bảng luật trong motion.md, tự viết ở từng nơi", False)]),
        dict(id="an02", grp="Phản hồi thao tác · vòng 2", title="Dấu kết quả theo mẫu Lottie Wizard bạn gửi",
             why=("Bạn ghi tham khảo <a href='https://dribbble.com/shots/27204078-Finance-Success-Failure-Lottie-Animation'>Finance Success &amp; Failure Lottie Animation</a>. Mình xem từng khung hình của video 4 giây: <mark>chấm nở thành đĩa hai lớp, rồi dấu mới vẽ nét</mark>, xong sau khoảng 1,4 giây; bên thất bại dấu X vẽ từng nét và có một cung chạy quanh viền. Đĩa co giãn như nảy, và video lặp lại. "
                  "Mình giữ <b>ba nhịp</b> vì đó là điểm hay của mẫu, rút còn 600 để lái xe không phải chờ, và chỉ <b>chạy một lần</b>. Bỏ cung chạy viền vì trông như còn đang xử lý. Dùng cho cả thành công và thất bại, chỉ ở kết quả quan trọng; thao tác thường để toast lo (an04)."),
             untitled=f"Không có. <code>pathLength</code> xuất hiện ở {U_PATHLEN} file, không phải dấu kết quả.",
             ours="Chưa có. <code>color/bg/success-solid</code>, <code>color/bg/error-solid</code> có sẵn cho đĩa.", astryx=NONE,
             note="Chọn phương án nảy là <b>mở lại DEC-139</b> (không bounce, không lò xo), bằng chứng là mẫu bạn gửi. Mẫu gốc là file Lottie; cả ba phương án dựng bằng CSS và Flutter vẽ tương đương, không thêm thư viện, nên giảm chuyển động vẫn về 0.",
             pv=both(pv_success),
             opts=[("stage", "Ba nhịp, không nảy: đĩa ngoài duration/medium, đĩa trong trễ duration/fast, dấu vẽ sau duration/medium", True), ("bounce", "Ba nhịp + nảy như mẫu, mở lại DEC-139", False), ("one", "Một nhịp: đĩa mờ dần duration/fast, dấu vẽ duration/medium", False)]),
        dict(id="an03", grp="Phản hồi thao tác", title="Báo lỗi biểu mẫu: có rung ô nhập không",
             why=f"Rung gây chú ý nhưng <mark>khó đọc số khi đang rung</mark>. Untitled không rung ({U_SHAKE} file). Lỗi cước, số km cần đọc ngay, nên dòng lỗi mờ dần 125 kèm viền đổi màu là vừa.",
             untitled="Không rung; <code>input.tsx</code> đổi màu viền theo <code>isInvalid</code>.",
             ours="<code>color/border/error</code>, <code>color/text/error-primary</code> đã có, chưa có luật chạy.", astryx=NONE,
             pv=both(pv_error),
             opts=[("fade", "Dòng lỗi mờ dần + trượt 4, viền đổi màu duration/fast, không rung", True), ("shake", "Rung ngang 3 nhịp trong duration/medium", False), ("none", "Đổi ngay", False)]),
        dict(id="an04", grp="Phản hồi thao tác", title="Nút sau khi xử lý xong",
             why="mt09 đã chốt spinner chờ 300 mới hiện, nhưng chưa nói <mark>pha sau đó</mark>. Nhãn đổi ngay về “Duyệt lệnh” khiến người dùng tưởng chưa ăn lệnh và bấm lại. Giữ dấu check 1 giây rồi về nhãn; <b>nút giữ nguyên bề rộng</b> để bố cục không nhảy, và không chặn bấm theo mt17.",
             untitled="<code>button.tsx</code>: <code>isLoading</code> ẩn chữ, spinner giữa nút, hết tải là về nhãn; không có pha xong.",
             ours="<code>design-system/components/_work/buttons/page.json</code> có spinner, chưa có pha xong.",
             astryx="Spinner của Button chờ <code>duration-medium-min</code> rồi mới hiện (<code>design/design.md</code> mục Motion).",
             pv=both(pv_button),
             opts=[("hold", "Spinner → dấu check giữ 1000 → về nhãn", True), ("toast", "Spinner → về nhãn, kết quả báo bằng toast", False), ("stay", "Spinner → dấu check đứng nguyên, nút khoá", False)]),
        dict(id="an05", grp="Phản hồi thao tác", title="Đổi icon tại chỗ: sao chép mã container, ghim, đánh dấu",
             why="Điều vận hay sao chép mã container, biển số. Mờ chéo + phóng 95 trong 125 giúp <mark>thấy rõ đã ăn lệnh</mark> mà không kéo mắt. Icon ở lại dấu check 1 giây rồi về icon gốc.",
             untitled=f"Không có luật chung; {U_CLIP} file có <code>clipboard</code>.",
             ours="Chưa có. Phóng 95 đã dùng cho dialog (<code>design-system/foundations/motion.md</code> mục 10.3).", astryx=NONE,
             pv=both(pv_icon),
             opts=[("swap", "Mờ chéo + phóng 95 duration/fast, giữ 1000 rồi về", True), ("hard", "Đổi ngay, giữ 1000 rồi về", False)]),
        dict(id="an06", grp="Dữ liệu đổi", title="Dòng vừa đổi trong bảng điều vận",
             why="Điều vận nhìn bảng dày, trạng thái đổi từ xa. Chỉ đổi chip thì <mark>rất dễ sót</mark>. Tô nền 1 giây rồi phai chạy đúng <b>một lần</b>, khác chấm nhấp nháy đã bỏ ở mt16. Quá 5 dòng đổi cùng lúc thì không tô, chỉ đổi chip, tránh cả bảng loé; <b>số 5 là đề xuất</b>, chưa đo. Trong 1 giây đó chip xanh hoà vào nền, chữ vẫn đọc được. Khi giảm chuyển động: nền giữ 1,5 giây rồi tắt ngay, nhờ bộ đếm giờ.",
             untitled=f"Không có; <code>table.tsx</code> không tô dòng, {U_FLASH} file khớp từ khoá.",
             ours="<code>color/utility/blue-50</code> có sẵn; mt16 cấm lặp, chưa nói chạy một lần.", astryx=NONE,
             pv=both(pv_flash),
             opts=[("flash", "Tô color/utility/blue-50 giữ 1000, phai duration/slow, chạy một lần, quá 5 dòng thì không tô", True), ("chip", "Chỉ chip đổi màu duration/fast", False)]),
        dict(id="an07", grp="Dữ liệu đổi", title="Số đổi: KPI, số trên huy hiệu",
             why="Đếm chạy đẹp nhưng <mark>trong 300 đó số trên màn là số sai</mark>; với cước và doanh thu thì không nên. Chữ số dùng <code>tabular-nums</code> để không nhảy bề rộng. Số trên huy hiệu theo cùng luật, chuông không lắc.",
             untitled=f"Không có; {U_COUNT} file có <code>countUp</code> hoặc <code>NumberFlow</code>.",
             ours="Màn mẫu đã dùng <code>tabular-nums</code>; chưa có luật chạy.", astryx=NONE,
             pv=both(pv_number),
             opts=[("fade", "Số mờ dần duration/fast, không đếm", True), ("count", "Đếm chạy trong duration/medium", False), ("none", "Đổi ngay", False)]),
        dict(id="an08", grp="Dữ liệu đổi", title="Lệnh mới từ máy chủ khi đang xem danh sách",
             why="Bảng tự đẩy xuống đúng lúc đang bấm thì <mark>bấm nhầm lệnh</mark>, rủi ro thật với duyệt lệnh. Báo “Có 2 lệnh mới”, bấm mới chèn; chèn xong dùng luật lần lượt của mt17. Luôn báo, kể cả khi đang ở đầu danh sách, để một cách làm cho mọi trường hợp.",
             untitled="Không có; bảng <code>table.tsx</code> không có luật dòng mới.",
             ours="mt17 chỉ phủ lọc, sắp xếp, phân trang (<code>design-system/foundations/motion.md</code> mục 10.5).", astryx=NONE,
             pv=both(pv_new),
             opts=[("pill", "Báo “Có n lệnh mới”, bấm mới chèn", True), ("push", "Tự chèn, mở cao duration/medium + tô nền", False), ("hard", "Tự chèn, không chạy", False)]),
        dict(id="an09", grp="Dữ liệu đổi", title="Thanh tiến độ: tải ảnh chứng từ, xuất báo cáo",
             why="Mạng ngoài đường đi từng nấc, nhảy thẳng trông như giật. Trượt 125 linear là đủ mượt, <mark>không tô vượt số thật</mark>. Mình không có bậc 75 như Untitled; 125 chỉ dài hơn 50 ms. Chưa biết phần trăm thì dùng spinner như đã chốt ở <code>field-upload</code>, không thêm kiểu thanh chạy lặp.",
             untitled="<code>progress-indicators.tsx</code>: <code>transition duration-75 ease-linear</code>, chạy <code>transform</code>.",
             ours="<code>design-system/components/application/field-upload.md</code> dùng spinner; chưa có luật thanh.", astryx=NONE,
             pv=both(pv_progress),
             opts=[("smooth", "Trượt duration/fast linear bằng transform; chưa biết % thì spinner", True), ("jump", "Nhảy theo mốc; chưa biết % thì spinner", False)]),
        dict(id="an10", grp="Dữ liệu đổi", title="Mở, đóng khối: chi tiết chuyến, nhóm trong biểu mẫu, xoá dòng",
             why="Mở chạy cao giúp <mark>giữ mạch đọc</mark> khi nội dung bên dưới dịch chuyển. Đóng dùng cặp <code>duration/exit</code> + <code>easing/exit</code> như dialog. Xoá dòng cũng co lại theo cách này. Chạy bằng <code>grid-template-rows</code> nên không cần đo chiều cao bằng JS.",
             untitled=f"Không có component ({U_ACC} file <code>accordion</code>).",
             ours="Chevron xoay <code>duration/fast</code> (mt12), bề rộng menu medium; chưa có chiều cao.", astryx=NONE,
             pv=both(pv_expand),
             opts=[("anim", "Mở duration/medium, đóng duration/exit; chevron duration/fast", True), ("fast", "Mở, đóng đều duration/fast", False), ("none", "Đổi ngay, chevron vẫn xoay", False)]),
        dict(id="an11", grp="Dữ liệu đổi", title="Từ skeleton sang nội dung, đổi trang trên web",
             why="Skeleton đã chốt ở mt08 nhưng lúc chuyển sang nội dung thật chưa có luật. Mờ dần 125 che được khác biệt nhỏ về bố cục. Đổi trang web cũng dùng preset này cho vùng nội dung, menu đứng yên; không trượt vì <mark>điều vận đổi trang nhiều</mark>, chạy dài sẽ thấy chậm.",
             untitled=f"Không có; {U_SKEL} file <code>skeleton</code>.",
             ours="<code>design-system/foundations/motion.md</code> mục 10.4 có skeleton, chưa có pha sang. Chuyển màn app giữ nền tảng (mt14).",
             astryx="Chuyển trang dùng <code>Skeleton</code> (<code>design/design.md</code> mục Splash).",
             pv=both(pv_load),
             opts=[("fade", "Mờ dần duration/fast, không trượt", True), ("none", "Đổi ngay", False), ("slide", "Mờ dần + trượt 8, duration/medium", False)]),
        dict(id="an12", grp="Logistics và app", title="Xe trên bản đồ khi có điểm GPS mới",
             why="Nội suy liên tục trông mượt nhưng <mark>vẽ xe ở vị trí không có thật</mark> và tốn máy khi có hàng trăm xe. Trượt 300 khi có điểm mới giữ mắt theo được, giữa hai điểm xe đứng yên đúng với dữ liệu. Điểm mới ngoài khung nhìn hoặc xa quá thì đặt ngay. Hướng xe xoay theo <code>map-marker</code>. <b>Chu kỳ GPS thật của EUP chưa có số</b>; bản xem thử giả định 2 giây.",
             untitled=f"Không có; {U_MAP} file dùng <code>mapbox</code>, <code>leaflet</code>.",
             ours="<code>design-system/components/application/map-marker.md</code>: code xoay riêng <code>Figure</code>, chưa có luật chạy.", astryx=NONE,
             note="Cần xác nhận chu kỳ GPS từ EUP. Nếu trên 30 giây thì trượt có thể không còn ý nghĩa, và mình sẽ đề xuất lại.",
             pv=both(pv_map),
             opts=[("glide", "Trượt duration/medium khi có điểm mới, xa quá thì đặt ngay", True), ("lerp", "Nội suy linear suốt chu kỳ", False), ("jump", "Nhảy tới điểm mới", False)]),
        dict(id="an13", grp="Logistics và app", title="Bước tiến độ của lệnh vận tải",
             why="Khi lái xe chuyển bước, vạch chạy rồi chấm mới sáng giúp <mark>thấy rõ đi từ đâu tới đâu</mark>. Tổng 425 chỉ khi đang xem màn đó; mở màn lần đầu thì hiện ngay, không chạy lại tiến độ đã qua.",
             untitled=f"Không có; {U_STEP} file <code>progress-steps</code> trong code đã tải về.",
             ours="Chưa có spec bước; <code>duration/medium</code> đã dùng cho gạch chân tab (mt11).", astryx=NONE,
             pv=both(pv_steps, "mobile"),
             opts=[("fill", "Vạch duration/medium, chấm duration/fast nối tiếp; mở màn lần đầu thì hiện ngay", True), ("none", "Đổi ngay", False)]),
        dict(id="an14", grp="Logistics và app", title="Quét mã container, QR",
             why="Vạch chạy lặp là <mark>trang trí, không báo gì về việc máy đã nhận mã chưa</mark>; camera đã đang chạy nên màn không tĩnh. Khung đứng yên rồi xanh + vẽ dấu khi nhận được là tín hiệu thật. Ngoài trời, xanh trên nền camera cần đi kèm dấu check, không chỉ dựa vào màu.",
             untitled=f"Không có; {U_SCAN} file có <code>barcode</code> hoặc <code>scanner</code>.",
             ours="Icon <code>scan-line</code>, <code>qr-code</code> có sẵn; chưa có màn quét.", astryx=NONE,
             pv=both(pv_scan, "mobile"),
             opts=[("frame", "Khung đứng yên, nhận mã thì xanh duration/fast + vẽ dấu duration/medium", True), ("line", "Vạch quét lặp linear, dừng sau 5 giây theo 10.8", False), ("next", "Khung đứng yên, nhận mã thì sang màn sau ngay", False)]),
        dict(id="an15", grp="Logistics và app", title="Kéo làm mới trên app",
             why="Đi cùng mt14: hành vi vuốt người dùng đã quen trên từng hệ điều hành, tự vẽ thì <mark>phải tự làm lại lực kéo, giảm chuyển động, trợ năng</mark>. Bản xem thử chỉ là mô phỏng, kéo thật phải thử trên máy.",
             untitled=f"Không có; {U_PULL} file <code>PullToRefresh</code>. Untitled là thư viện web.",
             ours="<code>design-system/foundations/motion.md</code> mục 10.9: chuyển màn giữ mặc định nền tảng.", astryx=NONE,
             pv=both(pv_pull, "mobile"),
             opts=[("sys", "Dùng mặc định của nền tảng", True), ("own", "Tự vẽ xe tải chạy qua", False)]),
        dict(id="an16", grp="Logistics và app", title="Dải mất mạng, có mạng lại",
             why="Lái xe có thể mất sóng trên đường và cần biết <mark>việc vừa làm đã lưu chưa</mark>. Dải mở cao đẩy nội dung để không che nút; có mạng lại thì xanh 1 giây rồi đóng. Mất mạng dưới 2 giây không báo, tránh nhấp nháy khi chuyển trạm; <b>số 2 giây là đề xuất</b>. Chữ trong dải luôn có icon, không chỉ dựa vào màu.",
             untitled=f"Không có; {U_OFFLINE} file đọc <code>navigator.onLine</code>. Chữ <code>offline</code> trong <code>avatar.tsx</code> là trạng thái người dùng.",
             ours="Icon <code>wifi-off</code> có sẵn; <code>design-system/components/base/alert-notification.md</code> có Alert, chưa có dải mạng.", astryx=NONE,
             pv=both(pv_offline, "mobile"),
             opts=[("push", "Dải mở cao duration/medium đẩy nội dung; có mạng xanh giữ 1000, đóng duration/exit", True), ("over", "Dải mờ dần đè lên nội dung", False), ("none", "Đổi ngay", False)]),
        dict(id="an17", grp="Biểu đồ", title="Biểu đồ khi tải và khi lọc",
             why=f"Untitled tắt hẳn: {U_CHART_OFF} chỗ <code>isAnimationActive={{false}}</code>. Điều vận hay lọc, <mark>cột mọc lại mỗi lần lọc thì khó so số</mark>, nên cột không mọc. Khác Untitled một điểm: lúc tải xong vẫn mờ dần 125, để biểu đồ đi cùng luật nội dung sau skeleton ở an11; đổi bộ lọc thì đổi ngay.",
             untitled=f"Demo <code>charts</code>: {U_CHART_OFF} chỗ <code>isAnimationActive={{false}}</code>.",
             ours="Chưa có component biểu đồ trong <code>design-system/components/application</code>.", astryx=NONE,
             pv=both(pv_chart),
             opts=[("fade", "Mờ dần duration/fast khi tải, đổi lọc thì đổi ngay", True), ("off", "Không chạy, như Untitled", False), ("grow", "Cột mọc duration/medium khi tải, đổi lọc thì đổi ngay", False), ("stagger", "Cột mọc lần lượt, chặn tổng duration/medium", False)]),
    ],
    final=FINAL,
    css=CSS,
    js=JS,
)
