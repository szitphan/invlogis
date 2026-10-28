#!/usr/bin/env python3
"""Sinh page.json cho Input (vòng 1 Brainstorm).
Chạy: python3 design/v2/components/_work/input/build.py && python3 _scripts/ds-component-page.py input
Đầu vào đã chốt: thẻ Input trên trang Chốt biến thể Base (artifact VQDsMrBW37W3QWVTPN79qC, db variants/input v6, 26/10):
Type 13 · Size SM MD LG · State 7 · Phần kèm Label, Required, Help Icon, Hint · mobile "same".
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "_forms"))
from kit import CSS, SCREEN_CSS, ic, mini, vg, vg_row, write  # noqa: E402

OUT = Path(__file__).parent / "page.json"


# ---------- control ----------
def otp(vals="482", n=6, st=""):
    boxes = "".join(f'<span class="ob{" on" if i == len(vals) and "is-focus" in st else ""}">{vals[i] if i < len(vals) else ""}</span>' for i in range(n))
    return f'<div class="otp {st}">{boxes}</div>'


def ctl(t="default", v=None, ph="Nhập…", size="md", st="", long=None, err=False):
    """Ô nhập theo Type. v = giá trị (None → placeholder). long = giá trị chữ dài cho trạng thái 'Chữ dài'."""
    if t == "otp":
        return otp(v or "", st=st)
    val = f'<span class="v nl">{v}</span>' if v else f'<span class="ph nl">{ph}</span>'
    if long:
        val += f'<span class="v lg" data-show="state:long">{long}</span>'
    lead, trail = "", ""
    if t == "icon":
        lead = f'<span class="ic">{ic("search")}</span>'
    elif t == "lead-text":
        lead = '<span class="ad l">+84</span>'
    elif t == "lead-dd":
        lead = f'<span class="ad l dd">VN{ic("chev", 14)}</span>'
    elif t == "trail-text":
        trail = '<span class="ad r">kg</span>'
    elif t == "trail-btn":
        trail = f'<span class="ab">{ic("search", 14)}Tra cứu</span>'
    elif t == "password":
        trail = f'<span class="ic">{ic("eye")}</span>'
    elif t == "number":
        lead = f'<span class="nb l" data-show="D7:a">{ic("minus", 14)}</span>'
        trail = (f'<span class="nb r" data-show="D7:a">{ic("plus", 14)}</span>'
                 f'<span class="ns" data-show="D7:b"><i>{ic("chevup", 12)}</i><i>{ic("chev", 12)}</i></span>'
                 '<span class="sub" data-show="D7:c">chuyến</span>')
    elif t == "tags":
        lead = ('<span class="tg t-sm">Hàng lạnh<button class="x" aria-label="Bỏ">' + ic("x", 12) + '</button></span>'
                '<span class="tg t-sm">Dễ vỡ<button class="x" aria-label="Bỏ">' + ic("x", 12) + '</button></span>')
    elif t == "date":
        lead = f'<span class="ic">{ic("cal")}</span>'
    elif t == "file":
        lead = f'<span class="ic">{ic("clip")}</span>'
        trail = '<span class="ab">Chọn tệp</span>'
    elif t == "payment":
        lead = '<span class="pc">VISA</span>'
    eic = f'<span class="eic" data-show="D4:a">{ic("err")}</span>' if err else ""
    live_eic = f'<span class="eic" data-show="D4:a state:error">{ic("err")}</span>' if err == "live" else ""
    return (f'<div class="ctl s-{size} t-{t} {st}">{lead}{val}{eic if err is True else live_eic}'
            f'{trail}</div>')


def field(label, c, req=False, hlp=False, hint=None, err=None, live=False, mob=False):
    star = "<span class=req>*</span>" if req else ""
    lb = ""
    if label:
        hi = f'<span class="hi" data-show="D6:a">{ic("help", 14)}</span>' if hlp else ""
        lb = f'<div class="lb"{' data-show="D2:a"' if mob else ""}>{label}{star}{hi}</div>'
    if hlp and c.startswith('<div class="ctl'):
        c = c[:-6] + f'<span class="ic hin" data-show="D6:b">{ic("help")}</span></div>'
    if mob and label and c.startswith('<div class="ctl'):
        c = c.replace('">', f'"><span class="lbi" data-show="D2:b">{label}{star}</span>', 1)
    foot = ""
    if err and err is not True:
        foot = f'<div class="fe"><span data-show="D4:b">{ic("err", 14)}</span>{err}</div>'
    elif hint:
        foot = f'<div class="hn">{hint}</div>'
    if live and err:
        foot = f'<div class="fe" data-show="state:error"><span data-show="D4:b">{ic("err", 14)}</span>{live}</div>'
        if hint:
            foot += f'<div class="hn nh">{hint}</div>'
    return f'<div class="f{" m" if mob else ""}" data-cmp{" data-live" if live else ""}>{lb}{c}{foot}</div>'


# ---------- CSS riêng Input ----------
FOCUS = lambda o: (f'.pv[data-D1={o}] .ctl.is-focus,.pv[data-D1={o}][data-state=focus] [data-live] .ctl,'
                   f'.pv[data-D1={o}] .otp.is-focus .ob.on')
CSS_INPUT = r"""
.pv[data-state=long] [data-live] .nl{display:none}
.pv[data-state=error] [data-live] .nh{display:none}
.pv[data-state=disabled] [data-live] .v{color:var(--fg4)}
.ctl.t-tags{flex-wrap:wrap;padding-top:3px;padding-bottom:3px;gap:4px 6px}
.ctl.t-tags .ph,.ctl.t-tags .v{flex:1 1 60px}
.nb{align-self:stretch;width:32px;display:grid;place-items:center;color:var(--fg2);flex:none}
.nb.l{margin-left:-12px;border-right:1px solid var(--line2)}.nb.r{margin-right:-12px;border-left:1px solid var(--line2)}
.ctl.t-number .v,.ctl.t-number .ph{text-align:center}
.pv[data-D7=b] .ctl.t-number .v,.pv[data-D7=c] .ctl.t-number .v{text-align:left}
.ns{display:flex;flex-direction:column;margin-right:-6px;color:var(--fg3)}.ns i{display:block;line-height:0;padding:1px 2px}
.pc{font:800 10px/14px Inter;letter-spacing:.5px;color:#1A1F71;border:1px solid var(--line);border-radius:4px;padding:2px 4px;flex:none;background:#fff}
.otp{display:flex;gap:8px}
.ob{width:40px;height:48px;border:1px solid var(--line2);border-radius:8px;display:grid;place-items:center;font:600 20px Inter;color:var(--fg);box-sizing:border-box;background:var(--bg)}
.ob.on{border-color:var(--focus);box-shadow:inset 0 0 0 1px var(--focus)}
.otp.is-err .ob{border-color:var(--err-bd)}.otp.is-dis .ob{background:var(--muted);color:var(--fg4)}
.m .ob{width:46px;height:56px;border-radius:12px}
/* D1 focus */
.pv[data-D1=b] .ctl.is-focus,.pv[data-D1=b][data-state=focus] [data-live] .ctl,.pv[data-D1=b] .otp .ob.on{border-color:var(--focus);box-shadow:0 0 0 4px var(--ring)}
.pv[data-D1=c] .ctl.is-focus,.pv[data-D1=c][data-state=focus] [data-live] .ctl,.pv[data-D1=c] .otp .ob.on{border-color:var(--line2);box-shadow:0 0 0 2px var(--bg),0 0 0 4px var(--focus)}
.pv[data-D1=b] .ctl.is-err.is-focus{box-shadow:0 0 0 4px rgba(240,68,56,.18)}
/* D2 mobile nhãn trong ô */
.mw{display:contents}
.lbi{display:block;font:500 12px/16px Inter;color:var(--fg3)}
.pv[data-D2=b] .m .ctl{--h:56px;background:var(--muted);border-color:transparent;flex-wrap:wrap;align-content:center;row-gap:0}
.pv[data-D2=b] .m .ctl .lbi{flex:0 0 100%}
.pv[data-D2=b] .m .ctl .ad{align-self:center;border:0;margin:0;padding:0}
.pv[data-D2=b] .m .ctl.is-focus,.pv[data-D2=b][data-state=focus] .m[data-live] .ctl{background:var(--bg);border-color:var(--focus)}
.pv[data-D2=b] .m .ctl.is-err,.pv[data-D2=b][data-state=error] .m[data-live] .ctl{border-color:var(--err-bd)}
/* D3 addon */
.pv[data-D3=b] .ad.l{border-right:0;padding-right:0;background:none}
.pv[data-D3=b] .ad.r{border-left:0;padding-left:0;background:none}
.pv[data-D3=a] .ad{background:var(--bg2)}
.pv[data-D3=a] .ad.dd{background:none}
/* D5 read only */
.pv[data-D5=b] .ctl.is-ro,.pv[data-D5=b][data-state=readonly] [data-live] .ctl{background:var(--bg);border-style:dashed;border-color:var(--line2)}
.pv[data-D5=c] .ctl.is-ro,.pv[data-D5=c][data-state=readonly] [data-live] .ctl{background:none;border-color:transparent;padding-left:0;box-shadow:none}
/* D6 help trong ô: chỉ hiện khi có giá trị trống chỗ */
.hin{margin-left:auto}
.ctl.is-err .ab,.pv[data-state=error] [data-live] .ab{border-color:var(--err-bd)}
.ctl.is-dis .ab{background:var(--muted);color:var(--fg4)}
"""


# ---------- dữ liệu mẫu ----------
LONG_ADDR = "Kho CFS Tân Cảng Sóng Thần, Lô C2, Đường số 4, KCN Sóng Thần 2, P. Dĩ An, TP. Dĩ An, Bình Dương"
TYPES = [
    ("default", "Default", "Kho Sóng Thần, Bình Dương", "Địa chỉ giao"),
    ("icon", "Leading Icon", None, "Tìm lệnh, xe, lái xe…"),
    ("lead-text", "Leading Text", "903 412 568", ""),
    ("lead-dd", "Leading Dropdown", "0903 412 568", ""),
    ("trail-text", "Trailing Text", "24.500", ""),
    ("trail-btn", "Trailing Button", "TGHU 881234 5", ""),
    ("password", "Password", "••••••••••", ""),
    ("number", "Number", "3", ""),
    ("tags", "Tags", None, "Thêm nhãn…"),
    ("otp", "OTP", "482", ""),
    ("date", "Date", "28/10/2026", ""),
    ("file", "File", "bien-ban-giao-hang.pdf", ""),
    ("payment", "Payment", "•••• •••• •••• 4821", ""),
]
LABELS = {"default": "Địa chỉ giao", "icon": "Tìm kiếm", "lead-text": "Số điện thoại", "lead-dd": "Số điện thoại",
          "trail-text": "Trọng lượng hàng", "trail-btn": "Số container", "password": "Mật khẩu", "number": "Số chuyến",
          "tags": "Nhãn hàng", "otp": "Mã xác thực", "date": "Ngày giao", "file": "Biên bản giao", "payment": "Thẻ nhiên liệu"}


def tf(t, size="md", st="", v="__", label=True, hint=None, err=None, mob=False, req=False, hlp=False):
    row = next(r for r in TYPES if r[0] == t)
    val = row[2] if v == "__" else v
    return field(LABELS[t] if label else None, ctl(t, val, row[3] or "Nhập…", size, st, err=bool(err)),
                 req=req, hlp=hlp, hint=hint, err=err, mob=mob)


# ---------- điểm cần quyết ----------
def m(over, inner, w=420, plat="web"):
    base = {"D1": "a", "D2": "a", "D3": "a", "D4": "a", "D5": "a", "D6": "a", "D7": "a", "state": "x"}
    return mini({**base, **over}, inner, w, plat)


def pair(*fs):
    return '<div style="display:flex;flex-direction:column;gap:14px">' + "".join(fs) + "</div>"


FOC = pair(tf("default", st="is-focus", hint="Ghi rõ số lô, đường để lái xe tìm được."), tf("trail-btn", st="is-focus is-err", err="Số container sai định dạng (4 chữ + 7 số)."))
MOB = pair(tf("default", mob=True, req=True), tf("trail-text", mob=True, st="is-focus"), tf("date", mob=True))
ADD = pair(tf("lead-dd"), tf("trail-text"), tf("trail-btn"))
ERR = pair(tf("trail-btn", st="is-err", err="Số container sai định dạng (4 chữ + 7 số)."))
RO = pair(field("Mã lệnh", ctl("default", "LVT-2026-0412", st="is-ro")), field("Khách hàng", ctl("default", "Công ty TNHH Delta Logistics", st="is-ro")))
HLP = pair(tf("trail-text", hlp=True, hint="Tổng trọng lượng hàng, không tính vỏ container."), tf("default", hlp=True, v=None))
NUM = pair(tf("number"), tf("number", st="is-focus"))

decisions = [
 {"id": "D1", "title": "Ô đang gõ (Focus) trông thế nào",
  "why": "Cả họ form (Input, Select, Multiselect) dùng chung cách vẽ focus — chốt ở đây, các trang sau theo. Astryx: viền 2px than chì (DEC-184). Untitled: viền 1px màu nhấn + vòng mờ 4px.",
  "source": "DEC-184 · DEC-207 · foundations Mục 9 (vùng chạm và focus)",
  "options": [
   {"label": "Viền 2px than chì (như hiện tại)", "desc": "Rõ trên nền trắng, không lấn ô bên cạnh; lỗi = viền đỏ 2px.", "rec": True, "preview": m({"D1": "a"}, FOC), "ideas": ["I3", "I4"]},
   {"label": "Viền 1px + vòng mờ 4px (Untitled)", "desc": "Mềm, hiện đại; vòng mờ nhạt khó thấy trên màn ngoài trời, cần khe giữa các ô ≥ 8.", "preview": m({"D1": "b"}, FOC), "ideas": ["I1", "I2"]},
   {"label": "Vòng focus tách rời (khe 2 + vòng 2)", "desc": "Giống vòng focus của nút (foundations Mục 9) — một luật cho mọi control; ô cao thêm 4px khi focus.", "preview": m({"D1": "c"}, FOC), "ideas": ["I8"]}],
  "untitled": m({"D1": "b"}, FOC), "untitledNote": "ring-4 brand-100 + viền brand-300",
  "astryx": m({"D1": "a"}, FOC), "astryxNote": "DEC-184: viền 2px border/focus"},
 {"id": "D2", "title": "App: nhãn trên ô hay trong ô",
  "why": "Trang chốt biến thể ghi Input mobile = “same” (cùng cấu tạo web). DEC-207 cũ đặt nhãn trong ô nền xám cao 52 cho app. Hai cách khác cấu tạo nên cần chốt lại.",
  "source": "variants/input (mobile: same) · DEC-207",
  "options": [
   {"label": "Nhãn trên ô, ô trắng cao 48 (cùng web)", "desc": "Một cấu tạo cho cả hai nền tảng; chữ nhãn luôn thấy cả khi gõ; form dài hơn.", "rec": True, "preview": m({"D2": "a"}, MOB, 360, "mobile"), "ideas": ["I9", "I1"]},
   {"label": "Nhãn trong ô, nền xám cao 56 (DEC-207)", "desc": "Gọn chiều cao form, giống app ngân hàng; addon và tag khó xếp trong ô.", "preview": m({"D2": "b"}, MOB, 360, "mobile"), "ideas": ["I3"]}],
  "untitled": m({"D2": "a"}, MOB, 360, "mobile"), "untitledNote": "web-first, mobile giữ nhãn trên",
  "astryx": m({"D2": "b"}, MOB, 360, "mobile"), "astryxNote": "Text Field / Mobile (DEC-207)"},
 {"id": "D3", "title": "Chữ đầu/cuối ô (+84, kg, VN ▾)",
  "why": "Type Leading Text, Leading Dropdown, Trailing Text, Trailing Button. Có vạch ngăn thì đọc rõ là “đơn vị”, nhưng ô trông nặng hơn.",
  "source": "Untitled input-leading-text / input-trailing-button",
  "options": [
   {"label": "Có vạch ngăn, nền nhạt (Untitled)", "desc": "Đơn vị tách hẳn khỏi giá trị; giống ô nhập tiền ở ERP.", "rec": True, "preview": m({"D3": "a"}, ADD), "ideas": ["I1", "I5"]},
   {"label": "Chữ xám trong ô, không vạch", "desc": "Nhẹ, gọn; đơn vị dễ lẫn với giá trị khi số dài.", "preview": m({"D3": "b"}, ADD), "ideas": ["I8", "I5"]}],
  "untitled": m({"D3": "a"}, ADD), "astryx": m({"D3": "b"}, ADD), "astryxNote": "InputGroup prefix/suffix"},
 {"id": "D4", "title": "Báo lỗi",
  "why": "Màu đỏ không đủ (Do's and Don'ts b: không chỉ dựa vào màu). Cần thêm icon — đặt trong ô hay ở dòng chữ lỗi.",
  "source": "design.md Do's and Don'ts (b) · Accessibility",
  "options": [
   {"label": "Icon ! trong ô + chữ lỗi đỏ dưới (Untitled)", "desc": "Thấy lỗi ngay tại ô khi lướt form dài.", "preview": m({"D4": "a"}, ERR), "ideas": ["I1"]},
   {"label": "Icon ở đầu dòng chữ lỗi", "desc": "Ô giữ trọn chỗ cho giá trị; không đụng icon cuối ô (lịch, mắt, chevron).", "rec": True, "preview": m({"D4": "b"}, ERR), "ideas": ["I4", "I3"]}],
  "untitled": m({"D4": "a"}, ERR), "astryx": m({"D4": "b"}, ERR), "astryxNote": "statusMessage dưới ô"},
 {"id": "D5", "title": "Chỉ đọc (Read Only)",
  "why": "Mã lệnh, khách hàng đã khoá sau khi tạo — người dùng phải phân biệt được với ô bị tắt (Disabled) và ô nhập được.",
  "source": "variants/input State Read Only",
  "options": [
   {"label": "Nền xám nhạt, viền nhạt", "desc": "Rõ là không sửa được; dễ lẫn với Disabled nếu chữ cũng nhạt — giữ chữ đậm.", "rec": True, "preview": m({"D5": "a"}, RO), "ideas": ["I4"]},
   {"label": "Nền trắng, viền nét đứt", "desc": "Khác hẳn Disabled; nét đứt hơi lạ với người dùng ERP.", "preview": m({"D5": "b"}, RO), "ideas": ["I6"]},
   {"label": "Bỏ khung, chỉ còn chữ", "desc": "Như trang chi tiết; form trộn ô có khung và không khung trông lệch hàng.", "preview": m({"D5": "c"}, RO), "ideas": ["I3"]}],
  "untitled": m({"D5": "a"}, RO), "untitledNote": "Untitled không có Read Only riêng — dùng disabled",
  "astryx": m({"D5": "a"}, RO)},
 {"id": "D6", "title": "Icon trợ giúp (?)",
  "why": "Phần kèm Help Icon đã chốt. Đặt cạnh nhãn hay trong ô bên phải.",
  "source": "variants/input Phần kèm Help Icon",
  "options": [
   {"label": "Cạnh nhãn", "desc": "Không lấn chỗ giá trị, không đụng icon cuối ô.", "rec": True, "preview": m({"D6": "a"}, HLP), "ideas": ["I4", "I5"]},
   {"label": "Trong ô bên phải (Untitled)", "desc": "Gần chỗ gõ; trùng chỗ với icon lỗi, mắt, chevron.", "preview": m({"D6": "b"}, HLP), "ideas": ["I1"]}],
  "untitled": m({"D6": "b"}, HLP), "astryx": m({"D6": "a"}, HLP), "astryxNote": "tooltip cạnh nhãn"},
 {"id": "D7", "title": "Ô số (Number)",
  "why": "Số chuyến, số container, số ngày — đổi số nhỏ. Nút −/+ dễ bấm trên app, nhưng ô rộng hơn.",
  "source": "variants/input Type Number",
  "options": [
   {"label": "Nút − / + hai bên", "desc": "Dễ bấm bằng ngón tay, rõ là ô số.", "rec": True, "preview": m({"D7": "a"}, NUM), "ideas": ["I6"]},
   {"label": "Mũi tên lên/xuống bên phải", "desc": "Gọn như ô số của trình duyệt; mũi tên nhỏ khó bấm trên app.", "preview": m({"D7": "b"}, NUM), "ideas": ["I4"]},
   {"label": "Chỉ gõ, đơn vị cuối ô", "desc": "Gọn nhất; hợp số lớn (tiền, kg) hơn số đếm.", "preview": m({"D7": "c"}, NUM), "ideas": ["I5"]}],
  "untitled": m({"D7": "c"}, NUM), "untitledNote": "Untitled không có stepper riêng", "astryx": m({"D7": "b"}, NUM), "astryxNote": "NumberInput"},
]

# ---------- ý tưởng cộng đồng ----------
def idea_pv(over, inner, w=380, plat="web"):
    return m(over, inner, w, plat)


ideas = [
 {"id": "I1", "source": "Untitled UI", "url": "https://www.untitledui.com/react/components/inputs", "title": "Untitled UI — Input đủ Type",
  "why": "Bộ đủ nhất: addon đầu/cuối có vạch, icon lỗi trong ô, help icon trong ô, vòng focus mờ 4px.",
  "pick": {"D1": "b", "D3": "a", "D4": "a", "D6": "b", "D7": "c"}},
 {"id": "I2", "source": "shadcn/ui", "url": "https://ui.shadcn.com/docs/components/input-otp", "title": "shadcn/ui — Input + Input OTP",
  "why": "Ô OTP ô vuông nối liền, ô đang nhập có vòng; ô thường gọn, ring mờ.", "pick": {"D1": "b", "D3": "b"}},
 {"id": "I3", "source": "Material 3", "url": "https://m3.material.io/components/text-fields/overview", "title": "Material 3 — Outlined text field",
  "why": "Focus viền dày 2px; nhãn lồng trong ô (filled) trên app; lỗi có icon ở dòng hỗ trợ.", "pick": {"D1": "a", "D2": "b", "D4": "b", "D5": "c"}},
 {"id": "I4", "source": "Atlassian", "url": "https://atlassian.design/components/textfield/examples", "title": "Atlassian — Textfield",
  "why": "Viền 2px khi focus, ô chỉ đọc nền xám, icon lỗi ở đầu dòng thông báo; ? cạnh nhãn.", "pick": {"D1": "a", "D4": "b", "D5": "a", "D6": "a", "D7": "b"}},
 {"id": "I5", "source": "Shopify Polaris", "url": "https://polaris.shopify.com/components/selection-and-input/text-field", "title": "Polaris — TextField prefix/suffix",
  "why": "Tiền tố/hậu tố là chữ xám trong ô, không vạch — nhẹ cho form dày.", "pick": {"D3": "b", "D6": "a", "D7": "c"}},
 {"id": "I6", "source": "Carbon", "url": "https://carbondesignsystem.com/components/number-input/usage/", "title": "Carbon — Number input",
  "why": "Nút −/+ gắn liền ô, có vạch ngăn; ô chỉ đọc viền nét đứt.", "pick": {"D7": "a", "D5": "b"}},
 {"id": "I7", "source": "Stripe", "url": "https://docs.stripe.com/payments/elements", "title": "Stripe Elements — ô thẻ",
  "why": "Ô thẻ có logo hãng đầu ô, số thẻ nhóm 4; báo lỗi ngay dưới ô có icon.", "pick": {"D4": "b"}},
 {"id": "I8", "source": "Vercel Geist", "url": "https://vercel.com/geist/input", "title": "Geist — Input tối giản",
  "why": "Đơn vị chữ xám không vạch; focus là vòng tách rời giống nút.", "pick": {"D1": "c", "D3": "b"}},
 {"id": "I9", "source": "Apple HIG", "url": "https://developer.apple.com/design/human-interface-guidelines/text-fields", "title": "Apple HIG — Text fields",
  "why": "Trên iOS nhãn đặt trên hoặc trước ô, ô cao ≥ 44; không nhồi nhãn vào trong ô.", "pick": {"D2": "a"}},
]
IDEA_PV = {
 "I1": pair(tf("trail-btn", st="is-err", err="Số container sai định dạng."), tf("lead-text", st="is-focus")),
 "I2": pair(field("Mã xác thực", otp("482", st="is-focus")), tf("default", st="is-focus")),
 "I3": pair(tf("default", mob=True, st="is-focus"), tf("date", mob=True)),
 "I4": pair(tf("trail-text", hlp=True, st="is-focus"), field("Mã lệnh", ctl("default", "LVT-2026-0412", st="is-ro"))),
 "I5": pair(tf("trail-text"), tf("lead-text")),
 "I6": pair(tf("number"), field("Mã lệnh", ctl("default", "LVT-2026-0412", st="is-ro"))),
 "I7": pair(tf("payment", st="is-err", err="Số thẻ chưa đủ 16 số.")),
 "I8": pair(tf("trail-text", st="is-focus"), tf("default")),
 "I9": pair(tf("default", mob=True, req=True), tf("number", mob=True)),
}
for i in ideas:
    plat = "mobile" if i["id"] in ("I3", "I9") else "web"
    i["preview"] = idea_pv(i.pop("pick"), IDEA_PV[i["id"]], 380 if plat == "web" else 340, plat)

REC = {d["id"]: chr(97 + next(k for k, o in enumerate(d["options"]) if o.get("rec"))) for d in decisions}
presets = [{"id": "rec", "label": "Đề xuất", "pick": REC},
           {"id": "untitled", "label": "Untitled UI", "pick": {"D1": "b", "D2": "a", "D3": "a", "D4": "a", "D5": "a", "D6": "b", "D7": "c"}},
           {"id": "astryx", "label": "Astryx hiện tại", "pick": {"D1": "a", "D2": "b", "D3": "b", "D4": "b", "D5": "a", "D6": "a", "D7": "b"}}]
for i in ideas:
    pk = {**REC}
    for d in decisions:
        if any(i["id"] in (o.get("ideas") or []) for o in d["options"]):
            pk[d["id"]] = chr(97 + next(k for k, o in enumerate(d["options"]) if i["id"] in (o.get("ideas") or [])))
    presets.append({"id": i["id"], "label": f'{i["id"]} · {i["source"]}', "pick": pk})


# ---------- màn ví dụ ----------
LIVE = field("Số container", ctl("trail-btn", "TGHU 881234 5", "VD: TGHU 881234 5", long="TGHU 881234 5 — vỏ 40HC, hãng tàu Evergreen, hạ bãi Cát Lái cổng B", err="live"),
             req=True, hint="4 chữ cái + 7 chữ số, in trên cửa container.", err=True, live="Số container sai định dạng (4 chữ + 7 số).")
S_ORDER = ('<div class="pad"><div class="card form"><div class="h">Thông tin lệnh</div><div class="grid2">'
           + field("Mã lệnh", ctl("default", "LVT-2026-0412", st="is-ro"))
           + field("Khách hàng", ctl("default", "Công ty TNHH Delta Logistics"), req=True)
           + LIVE
           + tf("trail-text", req=True, hlp=True)
           + tf("lead-dd", req=True)
           + field("Cước vận chuyển", ctl("trail-text", "8.500.000").replace(">kg<", ">VND<"))
           + tf("date", req=True)
           + tf("number")
           + '<div class="span2">' + field("Nhãn hàng", ctl("tags", None, "Thêm nhãn…"), hint="Lái xe thấy nhãn này trên app.") + '</div>'
           + '<div class="span2">' + field("Địa chỉ giao", ctl("default", LONG_ADDR)) + '</div>'
           + '<div class="span2">' + tf("file") + '</div>'
           + '</div><div class="acts"><button class="bt">Huỷ</button><button class="bt pri">Lưu lệnh</button></div></div></div>')
S_LOGIN = ('<div class="login"><div class="lgc"><div class="lgl">invlogis</div><b>Đăng nhập cổng đối tác</b><span class="s">Nhà xe, đại lý dùng tài khoản do Delta cấp.</span>'
           + field("Email", ctl("icon", "dieuphoi@nhaxeanphat.vn").replace(ic("search"), ic("user")))
           + field("Mật khẩu", ctl("password", "••••••••••"))
           + '<button class="bt pri" style="height:40px">Tiếp tục</button><div class="mdv2"></div>'
           + '<b style="font-size:15px">Nhập mã xác thực</b><span class="s">Mã 6 số đã gửi tới 0903 •••• 68, hết hạn sau 04:52.</span>'
           + '<div class="f" data-cmp data-live>' + otp("482", st="is-focus") + '<div class="fe" data-show="state:error"><span data-show="D4:b">' + ic("err", 14) + '</span>Mã không đúng, còn 2 lần thử.</div></div>'
           + '</div></div>')
MLIVE = field("Số tiền", ctl("trail-text", "350.000", "0", long="1.250.000.000", err="live").replace(">kg<", ">VND<"), req=True, err=True,
              live="Vượt hạn mức tạm ứng còn lại (300.000 VND).", hint="Hạn mức tạm ứng còn 300.000 VND.", mob=True)
S_COST = ('<div class="mpad"><div class="mcard"><b>LVT-2026-0412</b><span class="s">Cát Lái → Sóng Thần · 51C-482.19</span></div>'
          + field("Loại chi phí", ctl("default", "Phí cầu đường"), req=True, mob=True)
          + MLIVE
          + field("Ngày phát sinh", ctl("date", "28/10/2026"), req=True, mob=True)
          + tf("payment", mob=True)
          + field("Ghi chú", ctl("default", None, "VD: trạm BOT Phú Mỹ"), mob=True)
          + '</div><div class="mfoot"><button class="bt pri big">Gửi chi phí</button></div>')
S_OTP = ('<div class="mpad" style="padding-top:24px"><b style="font-size:20px;line-height:28px">Nhập mã xác thực</b>'
         '<span class="s" style="color:var(--fg3)">Mã 6 số gửi tới 0903 •••• 68</span>'
         '<div class="f m" data-cmp data-live>' + otp("48", st="is-focus") + '<div class="fe" data-show="state:error"><span data-show="D4:b">' + ic("err", 14) + '</span>Mã không đúng, còn 2 lần thử.</div></div>'
         + field("Mật khẩu mới", ctl("password", "••••••••"), mob=True, hint="Ít nhất 8 ký tự, có chữ và số.")
         + '</div><div class="mfoot"><button class="bt pri big">Xác nhận</button></div>')

# ---------- bảng biến thể ----------
STATES_V = [("Placeholder", "", None), ("Hover", "is-hover", None), ("Focus", "is-focus", None), ("Filled", "", "v"),
            ("Disabled", "is-dis", "v"), ("Error", "is-err", "v"), ("Read Only", "is-ro", "v")]


MANY_TAGS = "".join(f'<span class="tg t-sm">{t}<button class="x" aria-label="Bỏ">{ic("x", 12)}</button></span>'
                    for t in ("Hàng nguy hiểm loại 3", "Cần xe nâng", "Giao giờ hành chính", "Container lạnh -18°C"))


def g_web():
    blocks = []
    blocks.append(vg_row("Type", [(n, tf(t, label=False)) for t, n, _, _ in TYPES], 4, "13 loại · Size MD · Filled"))
    blocks.append(vg_row("Size", [(s, tf("trail-text", size=s.lower(), label=False)) for s in ("SM", "MD", "LG")], 3, "28 · 32 · 40"))
    cells = []
    for name, st, v in STATES_V:
        val = "Kho Sóng Thần, Bình Dương" if v else None
        err = "Chưa nhập địa chỉ giao." if st == "is-err" else None
        cells.append((name, field(None, ctl("default", val, "Địa chỉ giao", st=st, err=bool(err)), err=err)))
    blocks.append(vg_row("State", cells, 4, "7 trạng thái · Type Default"))
    blocks.append(vg_row("State × Type có icon cuối", [(n, tf(t, st=s, label=False)) for t in ("date", "password") for n, s in (("Focus", "is-focus"), ("Disabled", "is-dis"))], 4))
    blocks.append(vg_row("Phần kèm", [
        ("Label", tf("default")), ("Label + Required", tf("default", req=True)),
        ("Label + Help Icon", tf("default", hlp=True)), ("Label + Hint", tf("default", hint="Ghi rõ số lô, đường."))], 4))
    blocks.append(vg_row("Chữ dài", [("1 dòng, cắt …", field("Địa chỉ giao", ctl("default", LONG_ADDR))),
                                     ("Tags nhiều — xuống dòng", field("Nhãn hàng", ctl("tags", None, "Thêm nhãn…").replace('<span class="ph', MANY_TAGS + '<span class="ph', 1)))], 2, "luật chữ dài DEC-261"))
    return vg(blocks)


def g_mob():
    blocks = [vg_row("Type", [(n, tf(t, mob=True)) for t, n, _, _ in TYPES if t not in ("lead-text", "trail-btn", "file")], 1, "cùng cấu tạo web · cao 48"),
              vg_row("State", [(n, field("Địa chỉ giao", ctl("default", "Kho Sóng Thần" if v else None, "Nhập địa chỉ", st=st, err=st == "is-err"),
                                     err="Chưa nhập địa chỉ giao." if st == "is-err" else None, mob=True)) for n, st, v in STATES_V], 1)]
    return vg(blocks)


screens = [
 {"id": "order-web", "name": "Tạo lệnh vận tải", "device": "web", "title": "Tạo lệnh vận tải", "crumb": "Lệnh vận tải",
  "note": "Form dày nhiều Type. Ô Số container nhận trạng thái ở Bảng chọn › Hiển thị (bấm vào ô để focus).", "html": S_ORDER},
 {"id": "login-web", "name": "Đăng nhập + OTP", "device": "web", "shell": "none", "note": "Password + OTP. Ô OTP nhận trạng thái Lỗi.", "html": S_LOGIN},
 {"id": "cost-app", "name": "Báo chi phí", "device": "mobile", "title": "Báo chi phí dọc đường", "back": True, "tabs": False,
  "note": "Ô Số tiền nhận trạng thái ở Bảng chọn.", "html": S_COST},
 {"id": "otp-app", "name": "Nhập OTP", "device": "mobile", "title": "Đổi mật khẩu", "back": True, "tabs": False, "note": "OTP + Password trên app.", "html": S_OTP},
 {"id": "variants-web", "name": "Bảng biến thể", "device": "web", "shell": "none", "note": "Mọi Type, Size, State, Phần kèm đã chốt — đổi phương án ở Bảng chọn để thấy cả bảng đổi theo.", "html": g_web()},
 {"id": "variants-app", "name": "Bảng biến thể", "device": "mobile", "shell": "none", "note": "Biến thể trên app (393).", "html": g_mob()},
]

page = {
 "component": "Input", "slug": "input", "title": "Input Review",
 "subtitle": "Base component · vòng 1 Brainstorm — biến thể đã chốt ở trang Chốt biến thể Base (13 Type · SM MD LG · 7 State). Trang này chỉ hỏi chi tiết hình.",
 "round": "brainstorm",
 "refs": {
  "untitled": {"summary": "13 Type (icon, chữ, dropdown đầu; chữ, nút cuối; mật khẩu, số, tag, OTP, ngày, tệp, thẻ). Cỡ sm 40 · md 44, bo <mark>8</mark>, focus <mark>ring-4</mark> mờ, icon lỗi trong ô.",
               "source": "design/_ref/untitled-ui/react/components/base/input/ · untitledui.com/react/components/inputs"},
  "astryx": {"summary": "TextInput cao 32, bo 10, focus viền 1px + inset ring; DS v2 vòng 4 đổi thành viền 2px than chì (DEC-184); app nhãn trong ô nền xám 52 (DEC-207).",
             "source": "design/design.md › Form Controls · design/v2/components/l1/text-field.md"},
  "usage": ["Mọi form web + app: lệnh vận tải, báo chi phí, hồ sơ xe, lái xe", "Đăng nhập cổng đối tác (Password, OTP)", "Ô tìm đầu danh sách (Leading Icon)"],
  "platform": "Nhóm A — một bộ, cỡ theo Platform (web 28 · 32 · 40, app 48). Trang chốt biến thể ghi mobile “same” — D2 hỏi lại vì DEC-207 cũ khác cấu tạo."},
 "css": CSS + CSS_INPUT, "cssScreen": SCREEN_CSS + r"""
.login{min-height:760px;display:grid;place-items:center;background:var(--bg2)}
.lgc{width:400px;background:var(--bg);border:1px solid var(--line);border-radius:16px;padding:28px;display:flex;flex-direction:column;gap:14px}
.lgc .lgl{font:700 20px Inter;letter-spacing:-.3px}.lgc b{font-size:20px;line-height:28px}.lgc .s{color:var(--fg3);font-size:13.5px;margin-top:-8px}
.mdv2{height:1px;background:var(--line);margin:6px 0}
""",
 "states": [{"key": "default", "label": "Mặc định"}, {"key": "hover", "label": "Hover"}, {"key": "focus", "label": "Đang gõ"},
            {"key": "error", "label": "Lỗi"}, {"key": "disabled", "label": "Tắt"}, {"key": "readonly", "label": "Chỉ đọc"}, {"key": "long", "label": "Chữ dài"}],
 "ideas": ideas, "decisions": decisions, "presets": presets, "screens": screens,
 "proto": [{"sel": "[data-live] .ctl,[data-live] .otp", "state": "focus", "toggle": True}],
 "protoHint": "bấm vào ô đang thử để focus, bấm ra ngoài để thôi",
}

write(OUT, page, decisions)
