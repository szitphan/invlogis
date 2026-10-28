#!/usr/bin/env python3
"""Sinh page.json cho Badge + Avatar — brainstorm gọn (28/10).
Chạy: python3 design/v2/components/_work/badge-avatar/build.py && python3 _scripts/ds-component-page.py badge-avatar
Biến thể đã chốt: trang Chốt biến thể Base (VQDsMrBW37W3QWVTPN79qC, db variants/badge v2, variants/avatar v6, 26/10).
Điểm cần quyết từ trang Duyệt Base components (41DSsnEhvrQfZ1sggELNtq), chưa trả lời: R1, R2, L12, L13, R10 + viền màu Badge.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_lib"))
from pvkit import ic, tok_css, BASE_CSS, write  # noqa: E402

OUT = Path(__file__).parent / "page.json"

COLORS = [("gray", "Gray", "neutral"), ("blue", "Blue", "blue"), ("green", "Green", "green"), ("yellow", "Yellow", "yellow"),
          ("red", "Red", "red"), ("teal", "Teal", "teal"), ("purple", "Purple", "purple"), ("orange", "Orange", "orange")]


def bd(label, color="gray", typ="pill", size="md", icon=None, count=None, x=False, attrs=""):
    """typ = pill | badge | modern ; icon = dot | <tên icon>"""
    inner = ""
    if icon == "dot":
        inner += '<i class="bdot"></i>'
    elif icon:
        inner += ic(icon, 12, "bi")
    inner += f'<span class="bl">{label}</span>'
    if count is not None:
        inner += f'<b class="bc">{count}</b>'
    if x:
        inner += f'<button class="bx" aria-label="Bỏ {label}">{ic("x", 12)}</button>'
    return f'<span class="bd {typ} {size} c-{color}{" hasx" if x else ""}" {attrs}>{inner}</span>'


# ---------- Avatar ----------
# ảnh mẫu: chân dung vẽ bằng SVG (không tải ảnh ngoài)
def face(i):
    skins = ["#E8B894", "#C98F68", "#F1C9A5", "#B97A56"]
    hair = ["#2B2B2B", "#4A3426", "#1E1E1E", "#6B4A2E"]
    bg = ["#CFE0F7", "#E3DBFE", "#C6EDEB", "#FFE2C2"]
    return (f'<svg viewBox="0 0 40 40" class="aimg" aria-hidden="true"><rect width="40" height="40" fill="{bg[i % 4]}"/>'
            f'<circle cx="20" cy="17" r="8" fill="{skins[i % 4]}"/><path d="M12 15c0-6 4-9 8-9s8 3 8 9c-2-3-5-4-8-4s-6 1-8 4z" fill="{hair[i % 4]}"/>'
            f'<path d="M6 40c1-8 7-12 14-12s13 4 14 12z" fill="{["#3468D7", "#2B847C", "#6A50E4", "#C2410C"][i % 4]}"/></svg>')


def av(size="md", content="initials", text="TB", status=None, i=0, attrs=""):
    if content == "image":
        inner = face(i)
    elif content == "icon":
        inner = ic("user", 20, "ai")
    elif content == "upload":
        inner = ic("camera", 20, "ai")
    else:
        inner = f'<span class="at">{text}</span>'
    st = f'<i class="ast {status}" aria-label="{ {"on": "Đang trực", "off": "Ngoại tuyến", "busy": "Đang chạy chuyến", "away": "Tạm vắng"}[status]}"></i>' if status else ""
    return f'<span class="av {size} {content}" {attrs}>{inner}{st}</span>'


def company(size="md", text="DL"):
    return f'<span class="av {size} co"><span class="at">{text}</span></span>'


def group(n=4, more=3, size="sm"):
    people = ["TB", "LC", "PD", "NA", "HV"]
    items = "".join(av(size, "image" if k % 2 == 0 else "initials", people[k], i=k) for k in range(n))
    return f'<span class="ag {size}">{items}<span class="av {size} more"><span class="at">+{more}</span></span></span>'


def label_group(name, sub, size="md", status=None, content="image", i=0, text="TB"):
    return (f'<span class="alg {size}">{av(size, content, text, status, i)}<span class="tx2"><b>{name}</b><span>{sub}</span></span></span>')


def add_btn(size="md"):
    return f'<button class="av {size} add" aria-label="Thêm người">{ic("plus", 16, "ai")}</button>'


SIZES = [("xs", "XS"), ("sm", "SM"), ("md", "MD"), ("lg", "LG"), ("xl", "XL"), ("xxl", "XXL")]

CSS = tok_css() + BASE_CSS + """
/* ===== Badge ===== chữ type/chip-sm-strong mọi cỡ (DEC-277) */
.bd{display:inline-flex;align-items:center;gap:var(--chip-icon-gap);height:var(--chip-height);padding:0 var(--chip-padding-x);
 font:600 var(--chip-font-size-sm)/var(--chip-line-height-sm) var(--font-body);white-space:nowrap;max-width:var(--chip-label-max-width);
 border:1px solid transparent;vertical-align:middle;color:var(--c-fg);background:var(--c-bg)}
.bd .bl{overflow:hidden;text-overflow:ellipsis;min-width:0}
.bd.sm{height:var(--chip-height-sm);padding:0 var(--chip-padding-x-sm)}.bd.lg{height:var(--chip-height-lg);padding:0 var(--chip-padding-x-lg)}
.bd.pill{border-radius:var(--radius-chip)}.bd.badge{border-radius:var(--radius-badge)}
.bd.modern{border-radius:var(--radius-badge);background:var(--color-bg-surface);color:var(--color-text-secondary-strong);border-color:var(--color-border-strong);box-shadow:0 1px 2px var(--color-shadow-sm)}
.bd .bdot{width:6px;height:6px;border-radius:50%;background:var(--c-dot);flex:none}
.bd.modern .bi{color:var(--c-dot)}
.bd .bi{flex:none}
.bd .bc{font-weight:600;padding:0 5px;border-radius:3px;background:color-mix(in srgb,var(--c-fg) 12%,transparent);line-height:16px}
.bd.modern .bc{background:var(--color-bg-selected)}
.bd .bx{border:0;background:none;padding:0;margin-right:-4px;width:16px;height:16px;border-radius:3px;display:grid;place-items:center;color:inherit;opacity:.6;cursor:pointer}
.c-gray{--c-bg:var(--color-chip-gray-bg);--c-fg:var(--color-chip-gray-fg);--c-dot:var(--neutral-500);--c-ring:var(--neutral-200)}
.c-blue{--c-bg:var(--color-chip-blue-bg);--c-fg:var(--color-chip-blue-fg);--c-dot:var(--blue-600);--c-ring:var(--blue-200)}
.c-green{--c-bg:var(--color-chip-green-bg);--c-fg:var(--color-chip-green-fg);--c-dot:var(--green-600);--c-ring:var(--green-200)}
.c-yellow{--c-bg:var(--color-chip-yellow-bg);--c-fg:var(--color-chip-yellow-fg);--c-dot:var(--yellow-600);--c-ring:var(--yellow-200)}
.c-red{--c-bg:var(--color-chip-red-bg);--c-fg:var(--color-chip-red-fg);--c-dot:var(--red-600);--c-ring:var(--red-200)}
.c-teal{--c-bg:var(--color-chip-teal-bg);--c-fg:var(--color-chip-teal-fg);--c-dot:var(--teal-600);--c-ring:var(--teal-200)}
.c-purple{--c-bg:var(--color-chip-purple-bg);--c-fg:var(--color-chip-purple-fg);--c-dot:var(--purple-600);--c-ring:var(--purple-200)}
.c-orange{--c-bg:var(--color-chip-orange-bg);--c-fg:var(--color-chip-orange-fg);--c-dot:var(--orange-600);--c-ring:var(--orange-200)}
.pv[data-theme=dark] .bd{--c-ring:color-mix(in srgb,var(--c-fg) 35%,transparent)}
/* D1 nút X: a bỏ khỏi Badge (Tag lo) · b giữ */
[data-D1=a] .bd .bx{display:none}
[data-D1=a] .xonly{display:none!important}
[data-D1=b] .xtag{display:none}
/* D2 viền màu: a có viền {màu}/200 như Untitled · b không viền (lượt 1) */
[data-D2=a] .bd.pill,[data-D2=a] .bd.badge{border-color:var(--c-ring)}
/* D3 màu phân loại: a teal/tím/cam chỉ cho Loại · b dùng tự do */
[data-D3=a] .st-free{display:none}[data-D3=b] .st-rule{display:none}
/* ===== Avatar ===== D6 thang cỡ */
.av{--s:40px;--fs:16px;--dot:10px;position:relative;display:inline-grid;place-items:center;width:var(--s);height:var(--s);border-radius:50%;flex:none;
 background:var(--avatar-bg);color:var(--avatar-fg);vertical-align:middle}
.av .aimg{width:100%;height:100%;border-radius:50%;display:block}
.av .at{font:600 var(--fs)/1 var(--font-body);letter-spacing:-.01em}
.av .ai{width:calc(var(--s) * .5);height:calc(var(--s) * .5)}
.av.icon{background:var(--color-bg-selected);color:var(--color-icon-secondary)}
.av.upload,.av.add{background:transparent;border:1px dashed var(--avatar-upload-border);color:var(--avatar-upload-fg);cursor:pointer}
.av.co{border-radius:calc(var(--s) * .22);background:var(--color-chip-blue-bg);color:var(--color-chip-blue-fg)}
.av.more{background:var(--avatar-overflow-bg);color:var(--color-text-primary)}
.av .ast{position:absolute;right:0;bottom:0;width:var(--dot);height:var(--dot);border-radius:50%;box-shadow:0 0 0 1.5px var(--color-bg-surface)}
.ast.on{background:var(--color-status-success-icon)}.ast.busy{background:var(--color-status-danger-icon)}.ast.away{background:var(--color-status-warning-icon)}
.ast.off{background:var(--neutral-400)}
[data-D5=a] .ast.off{background:var(--color-bg-surface);box-shadow:inset 0 0 0 1.5px var(--neutral-400),0 0 0 1.5px var(--color-bg-surface)}
/* D6: a thang Untitled 24·32·40·48·56·64 · b thang token hiện tại 20·24·36·48·64·88 */
.av.xs{--s:24px;--fs:10px;--dot:6px}.av.sm{--s:32px;--fs:12px;--dot:8px}.av.md{--s:40px;--fs:14px;--dot:10px}
.av.lg{--s:48px;--fs:16px;--dot:12px}.av.xl{--s:56px;--fs:18px;--dot:14px}.av.xxl{--s:64px;--fs:22px;--dot:16px}
[data-D6=b] .av.xs{--s:20px;--fs:9px;--dot:6px}[data-D6=b] .av.sm{--s:var(--avatar-size-sm);--fs:10px;--dot:var(--avatar-status-size-sm)}
[data-D6=b] .av.md{--s:var(--avatar-size-md);--fs:13px;--dot:var(--avatar-status-size-md)}[data-D6=b] .av.lg{--s:var(--avatar-size-lg);--fs:16px;--dot:var(--avatar-status-size-lg)}
[data-D6=b] .av.xl{--s:var(--avatar-size-xl);--fs:22px;--dot:var(--avatar-status-size-xl)}[data-D6=b] .av.xxl{--s:var(--avatar-size-xxl);--fs:28px;--dot:var(--avatar-status-size-xxl)}
.szl{font:500 11px/14px var(--font-code);color:var(--color-text-tertiary)}
[data-D6=a] .szl.b,[data-D6=b] .szl.a{display:none}
/* Avatar group — D4: a avatar sau đè avatar trước (Untitled) · b avatar đầu nằm trên (DEC-242) */
.ag{display:inline-flex;align-items:center}.ag .av{box-shadow:0 0 0 var(--avatar-ring) var(--color-bg-surface)}
.ag .av+.av{margin-left:var(--avatar-group-overlap-sm)}.ag.md .av+.av{margin-left:var(--avatar-group-overlap-md)}
[data-D4=b] .ag .av:nth-child(1){z-index:6}[data-D4=b] .ag .av:nth-child(2){z-index:5}[data-D4=b] .ag .av:nth-child(3){z-index:4}
[data-D4=b] .ag .av:nth-child(4){z-index:3}[data-D4=b] .ag .av:nth-child(5){z-index:2}
/* Label group */
.alg{display:inline-flex;align-items:center;gap:10px;min-width:0;max-width:240px}
.alg .tx2{display:flex;flex-direction:column;min-width:0}.alg b{font:600 14px/20px var(--font-body);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.alg .tx2 span{font-size:12px;line-height:16px;color:var(--color-text-secondary);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.alg.sm b{font-size:13px;line-height:18px}.alg.sm{gap:8px}
/* Màn demo */
.tbar{display:flex;align-items:center;gap:12px;padding:0 24px 12px}
.sk{display:inline-block;height:12px;border-radius:6px;background:var(--color-bg-selected);animation:pl 1.2s ease-in-out infinite}
@keyframes pl{50%{opacity:.5}}
.empty{padding:48px 24px;text-align:center;color:var(--color-text-secondary)}
.mrow{display:flex;align-items:center;gap:12px;padding:12px 16px;border-bottom:1px solid var(--color-border-default)}
.mrow .tx2{flex:1;min-width:0}.mrow b{display:block;font:600 15px/20px var(--font-body);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.mrow .s{font-size:13px;line-height:18px;color:var(--color-text-secondary)}
.prof{display:flex;flex-direction:column;align-items:center;gap:8px;padding:20px 16px 12px}
.flt{display:flex;gap:8px;padding:0 24px 12px;flex-wrap:wrap}
.tg{display:inline-flex;align-items:center;gap:4px;height:24px;padding:0 4px 0 8px;border:1px solid var(--color-border-strong);border-radius:6px;font:600 12px/18px var(--font-body);color:var(--color-text-secondary-strong)}
.tg button{border:0;background:none;padding:0;width:16px;height:16px;display:grid;place-items:center;color:inherit;opacity:.6}
"""

# ---------- Bảng biến thể Web ----------
def badge_matrix():
    head = '<div class="vl"></div>' + "".join(f'<div class="vl">{n}</div>' for _, n, _ in COLORS)
    rows = ""
    for typ, n in (("pill", "Pill Color"), ("badge", "Badge Color"), ("modern", "Badge Modern")):
        rows += f'<div class="vl">{n}</div>' + "".join(
            f'<div>{bd("Nhãn", c, typ, icon="dot" if typ == "modern" else None)}</div>' for c, _, _ in COLORS)
    return f'<div class="vgrid" style="grid-template-columns:100px repeat(8,max-content)">{head}{rows}</div>'


def badge_icons():
    out = '<div class="vl"></div>' + "".join(f'<div class="vl">{x}</div>' for x in ("None", "Dot", "Leading", "Count", "X Close"))
    for sz, lab in (("sm", "SM"), ("md", "MD"), ("lg", "LG")):
        out += (f'<div class="vl">{lab}</div><div>{bd("Đang chạy", "blue", "pill", sz)}</div><div>{bd("Đang chạy", "blue", "pill", sz, "dot")}</div>'
                f'<div>{bd("Đã giao", "green", "pill", sz, "check")}</div><div>{bd("Chờ điều", "yellow", "pill", sz, count=12)}</div>'
                f'<div>{bd("Hàng lạnh", "teal", "badge", sz, x=True)}</div>')
    return f'<div class="vgrid" style="grid-template-columns:40px repeat(5,max-content)">{out}</div>'


def av_ladder():
    head = '<div class="vl"></div>' + "".join(
        f'<div><span class="szl a">{n} · {p}</span><span class="szl b">{n} · {q}</span></div>'
        for (_, n), p, q in zip(SIZES, (24, 32, 40, 48, 56, 64), (20, 24, 36, 48, 64, 88)))
    rows = ""
    for content, lab in (("image", "Image"), ("initials", "Initials"), ("icon", "Icon"), ("upload", "Upload")):
        rows += f'<div class="vl">{lab}</div>' + "".join(f'<div>{av(s, content, "TB", i=k)}</div>' for k, (s, _) in enumerate(SIZES))
    rows += '<div class="vl">Company</div>' + "".join(f'<div>{company(s)}</div>' for s, _ in SIZES)
    return f'<div class="vgrid" style="grid-template-columns:80px repeat(6,72px)">{head}{rows}</div>'


VAR_WEB = f"""<div class="vt">
<div><div class="vh">Badge · Type × Color <small>Size=MD · chữ type/chip-sm-strong (DEC-277)</small></div>{badge_matrix()}</div>
<div><div class="vh">Badge · Size × Icon <small>22 · 24 · 28</small></div>{badge_icons()}
 <p class="vl xtag" style="margin-top:6px;white-space:normal">D1 = A: Badge không có X — cột X Close chuyển sang Tag (xem bộ lọc trên màn danh sách).</p></div>
<div><div class="vh">Chữ dài <small>1 dòng, cắt "…", rộng tối đa 160</small></div>
 <div class="vg">{bd("Chờ chứng từ hải quan tại cảng Cát Lái", "yellow", "pill", icon="dot")}{bd("Hàng nguy hiểm nhóm 3 — chất lỏng dễ cháy", "red", "badge")}</div></div>
<div><div class="vh">Avatar · Content × Size <small>status = chấm góc dưới phải</small></div>{av_ladder()}</div>
<div class="row" style="gap:40px;align-items:flex-start;flex-wrap:wrap">
 <div><div class="vh">Status</div><div class="vg">{av("lg", "image", status="on", i=0)}{av("lg", "image", status="off", i=1)}{av("lg", "initials", "LC", status="busy")}{av("lg", "initials", "PD", status="away")}</div>
  <div class="vg" style="margin-top:6px"><span class="vl">Online</span><span class="vl" style="margin-left:22px">Offline</span><span class="vl" style="margin-left:18px">Busy</span><span class="vl" style="margin-left:26px">Away</span></div></div>
 <div><div class="vh">Avatar group <small>tối đa 4 + ô "+n"</small></div><div class="vg">{group(4, 3, "sm")}{group(4, 12, "md")}</div></div>
 <div><div class="vh">Label group</div><div style="display:flex;flex-direction:column;gap:12px">{label_group("Trần Văn Bình", "Lái xe · 51C-123.45", "md", "on")}{label_group("Nguyễn Thị Hồng Nhung Phương", "Điều phối viên ca đêm · Kho Sóng Thần", "md", content="initials", text="NP")}</div></div>
 <div><div class="vh">Add</div><div class="vg">{add_btn("sm")}{add_btn("md")}</div></div>
</div>
</div>"""

VAR_APP = f"""<div class="vt">
<div><div class="vh">Badge trên app <small>cùng số đo (nhóm A)</small></div>
 <div class="vg">{bd("Đang chạy", "blue", "pill", icon="dot")}{bd("Đã giao", "green", "pill", icon="check")}{bd("Trễ 25 phút", "red", "pill")}{bd("Hàng lạnh", "teal", "badge")}{bd("Chờ điều", "yellow", "pill", count=3)}</div></div>
<div><div class="vh">Avatar + status</div><div class="vg">{av("sm", "image", status="on", i=0)}{av("md", "image", status="busy", i=1)}{av("lg", "initials", "LC", status="away")}{av("xl", "image", status="off", i=2)}</div></div>
<div><div class="vh">Label group</div>{label_group("Trần Văn Bình", "Lái xe · 51C-123.45", "md", "on")}</div>
<div><div class="vh">Ảnh hồ sơ (Upload)</div><div class="vg">{av("xxl", "upload")}{av("xxl", "image", i=3)}</div></div>
<div><div class="vh">Avatar group</div>{group(4, 2, "sm")}</div>
</div>"""

# ---------- Màn demo ----------
ROWS = [
    ("LVT-2026-0412", "Cát Lái → ICD Sóng Thần", ("Đang chạy", "blue"), ("Container khô", "gray"), ("Trần Văn Bình", "51C-123.45", 0)),
    ("LVT-2026-0413", "Hiệp Phước → VSIP 2", ("Trễ 25 phút", "red"), ("Hàng lạnh", "teal"), ("Lê Minh Châu", "51D-678.90", 1)),
    ("LVT-2026-0414", "Cát Lái → Long Hậu", ("Chờ điều", "yellow"), ("Hàng nguy hiểm", "orange"), None),
    ("LVT-2026-0415", "Cái Mép → Tân Uyên", ("Đã giao", "green"), ("Hàng quá khổ", "purple"), ("Phạm Quốc Dũng", "51C-246.80", 2)),
]


def lst_rows(long=False):
    out = ""
    for k, (code, route, (st, sc), (ty, tc), drv) in enumerate(ROWS):
        if long and k == 0:
            st, route = "Chờ chứng từ hải quan tại cảng Cát Lái", "Tân Cảng Cát Lái (cổng B) → ICD Sóng Thần, Dĩ An, Bình Dương"
        free = bd(st, sc, "pill", icon="dot", attrs="data-cmp")
        # D3 a: cột trạng thái chỉ dùng màu có nghĩa; teal/tím/cam ở cột Loại (Badge Modern)
        typ = (f'<span class="st-rule">{bd(ty, tc, "modern", icon="dot", attrs="data-cmp")}</span>'
               f'<span class="st-free">{bd(ty, tc, "badge", attrs="data-cmp")}</span>')
        d = (label_group(drv[0], drv[1], "sm", ["on", "busy", "off"][drv[2]], i=drv[2]) if drv
             else f'<span class="muted" style="font-size:13px">Chưa điều</span>')
        out += (f'<tr><td class="mono">{code}</td><td style="max-width:260px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">{route}</td>'
                f'<td>{free}</td><td>{typ}</td><td>{d}</td></tr>')
    return out


SK = "".join(f'<tr><td><span class="sk" style="width:110px"></span></td><td><span class="sk" style="width:180px"></span></td><td><span class="sk" style="width:80px;height:22px;border-radius:11px"></span></td><td><span class="sk" style="width:90px"></span></td><td><span class="sk" style="width:24px;height:24px;border-radius:50%"></span> <span class="sk" style="width:100px"></span></td></tr>' for _ in range(4))

LIST = f"""<div class="tbar"><span class="muted" style="font-size:13px">Ca trực hôm nay</span>{group(4, 3, "sm")}<span class="sp"></span>
<span class="muted" style="font-size:13px">48 lệnh</span></div>
<div class="flt"><span class="xtag tg">Đang chạy <button aria-label="Bỏ lọc">{ic("x", 12)}</button></span><span class="xtag tg">Hàng lạnh <button aria-label="Bỏ lọc">{ic("x", 12)}</button></span>
<span class="xonly" style="display:contents">{bd("Đang chạy", "blue", "badge", x=True, attrs="data-cmp")}{bd("Hàng lạnh", "teal", "badge", x=True, attrs="data-cmp")}</span></div>
<div style="padding:0 24px"><table class="tbl card" style="overflow:hidden"><tr><th>Mã lệnh</th><th>Tuyến</th><th>Trạng thái</th><th>Loại hàng</th><th>Lái xe</th></tr>
<tbody data-hide="loading empty long">{lst_rows()}</tbody><tbody data-show="state:long">{lst_rows(True)}</tbody><tbody data-show="state:loading">{SK}</tbody></table>
<div class="empty card" data-show="state:empty" style="margin-top:-1px;border-top:0">Chưa có lệnh nào khớp bộ lọc.</div></div>"""

DRIVERS = [("Trần Văn Bình", "51C-123.45 · Cát Lái → Sóng Thần", "on", ("Đang chạy", "blue"), 0),
           ("Lê Minh Châu", "51D-678.90 · Hiệp Phước → VSIP 2", "busy", ("Trễ 25 phút", "red"), 1),
           ("Phạm Quốc Dũng", "51C-246.80 · nghỉ ca", "off", ("Nghỉ", "gray"), 2),
           ("Hoàng Văn Em", "51C-555.12 · chờ lệnh tại bãi", "away", ("Chờ lệnh", "yellow"), 3)]
APP = (f'<div class="prof">{av("xxl", "image", status="on", i=3, attrs="data-cmp")}<b style="font:600 17px/24px var(--font-body)">Nguyễn Văn An</b>'
       f'<span class="muted" style="font-size:13px">Đội trưởng ca ngày</span></div>'
       f'<div class="vh" style="padding:4px 16px 0">Lái xe trong đội</div>'
       + "".join(f'<div class="mrow" data-hide="loading empty">{av("md", "image" if k != 1 else "initials", "LC", s, i=k, attrs="data-cmp")}<div class="tx2"><b>{n if k or True else n}</b><div class="s">{sub}</div></div>{bd(st, sc, "pill", icon="dot", attrs="data-cmp")}</div>'
                 for k, (n, sub, s, (st, sc), _) in enumerate(DRIVERS))
       + "".join('<div class="mrow" data-show="state:loading"><span class="sk" style="width:40px;height:40px;border-radius:50%"></span><div class="tx2"><span class="sk" style="width:140px"></span><br><span class="sk" style="width:200px;margin-top:6px"></span></div></div>' for _ in range(3))
       + '<div class="empty" data-show="state:empty">Đội chưa có lái xe.</div>')
APP = APP.replace("<b>Trần Văn Bình</b>", "<b>Trần Văn Bình</b>")


def mini(attrs, inner, platform=None):
    a = " ".join(f'data-{k}="{v}"' for k, v in attrs.items())
    return f'<div class="op" {a} style="padding:16px;display:flex;gap:10px;flex-wrap:wrap;align-items:center">{inner}</div>'


TBL3 = lambda d: mini({"D3": d}, f'<table class="tbl card" style="width:auto"><tr><th>Trạng thái</th><th>Loại hàng</th></tr>'
                                 f'<tr><td>{bd("Đang chạy", "blue", "pill", icon="dot")}</td><td><span class="st-rule">{bd("Hàng lạnh", "teal", "modern", icon="dot")}</span><span class="st-free">{bd("Hàng lạnh", "teal", "badge")}</span></td></tr>'
                                 f'<tr><td>{bd("Trễ 25 phút", "red", "pill", icon="dot")}</td><td><span class="st-rule">{bd("Quá khổ", "purple", "modern", icon="dot")}</span><span class="st-free">{bd("Quá khổ", "purple", "badge")}</span></td></tr></table>')

page = {
    "component": "Badge · Avatar",
    "slug": "badge-avatar",
    "title": "Badge · Avatar Review",
    "subtitle": "Base component · Badge, Avatar (+ Company, Group, Label group, Add) · nhóm A (dùng chung web và app)",
    "round": "brainstorm",
    "brief": True,
    "refs": {
        "untitled": {
            "summary": "Badge 3 kiểu <mark>pill-color · color · modern</mark>, 3 cỡ, có dot / icon / nút X; Pill và Badge Color có <mark>viền màu nhạt</mark> (ring-1). Avatar 7 cỡ 16–64, initials nền xám, chấm Online xanh / Offline xám đặc, group: avatar sau đè avatar trước.",
            "source": "design/_ref/untitled-ui/react/components/base/badges/badges.tsx · avatar/avatar.tsx · avatar-label-group.tsx",
        },
        "astryx": {
            "summary": "Chip trạng thái bo tròn hẳn, nền nhạt, không viền (Status Chip); avatar spec v2 cũ 5 cỡ 24·36·48·64·88, chấm Offline rỗng, nhóm: avatar đầu nằm trên (DEC-242).",
            "source": "design/v2/components/l1/status-chip.md · l1/avatar.md · l1/avatar-group.md",
        },
        "usage": [
            "Mọi bảng danh sách: cột Trạng thái, Loại (Badge)",
            "cross-process-flow · search-process, create-next-step (Badge)",
            "Header web: nút tài khoản chỉ avatar (DEC-290) · app: hồ sơ lái xe, danh sách đội",
        ],
        "platform": "Nhóm A — một bộ, cùng số đo web và app. Đã chốt biến thể 26/10: Badge Type 3 × Color 8 × Icon 5 × Size 3; Avatar Content 4 × Size 6 × Status 4 + Group, Label group, Add, Company. Brainstorm gọn: 6 điểm còn mở từ lượt duyệt Figma 1.",
    },
    "css": CSS,
    "states": [
        {"key": "default", "label": "Có dữ liệu"},
        {"key": "long", "label": "Chữ dài"},
        {"key": "loading", "label": "Đang tải"},
        {"key": "empty", "label": "Rỗng"},
    ],
    "ideas": [],
    "decisions": [
        {"id": "D1", "title": "Badge có nút X không",
         "why": "Lượt 1 cho Badge có <mark>X Close</mark> (để làm chip lọc). Untitled coi Badge là <b>chỉ đọc</b>; thứ bỏ được là <b>Tag</b> (đã có component riêng, DEC-284). Giữ cả hai → hai cách vẽ chip lọc (mục R1).",
         "source": "Trang Duyệt Base components › R1 · Figma Badge 6657:165736 · DEC-284 (Tag)",
         "options": [
             {"label": "Bỏ X, chip lọc dùng Tag", "desc": "Badge chỉ đọc; bộ lọc dùng Tag (viền, nút X 16).", "rec": True,
              "preview": mini({"D1": "a"}, f'{bd("Đang chạy", "blue", "pill", icon="dot")}<span class="tg">Đang chạy <button aria-label="Bỏ">{ic("x", 12)}</button></span>')},
             {"label": "Giữ X trong Badge", "desc": "Badge có thêm Icon=X Close; Tag và Badge cùng làm chip lọc.",
              "preview": mini({"D1": "b"}, f'{bd("Đang chạy", "blue", "pill", icon="dot")}{bd("Đang chạy", "blue", "badge", x=True)}')},
         ],
         "untitled": mini({"D1": "a"}, bd("Label", "blue", "pill")), "untitledNote": "BadgeWithButton chỉ ở demo; filter dùng Tag",
         "astryx": mini({"D1": "b"}, bd("Đang lọc", "gray", "pill", x=True)), "astryxNote": "chip có X"},
        {"id": "D2", "title": "Viền màu cho Pill / Badge Color",
         "why": "Untitled thêm <mark>viền màu nhạt</mark> (màu/200) quanh Pill Color và Badge Color — tách được badge khỏi dòng đang chọn / hover (nền xám). v2 chưa có token này; thêm thì cần 8 token viền.",
         "source": "badges.tsx (ring-1 ring-{color}-200) · Trang Duyệt Base › token badge/border",
         "options": [
             {"label": "Có viền màu nhạt", "desc": "Như Untitled; thêm token `chip/{màu}/border`.",
              "preview": mini({"D2": "a"}, "".join(bd(n, c, "pill") for c, n in (("blue", "Đang chạy"), ("green", "Đã giao"), ("yellow", "Chờ điều"), ("gray", "Nháp"))))},
             {"label": "Không viền", "desc": "Như lượt 1 và Status Chip cũ; ít token, gọn khi nhiều badge.", "rec": True,
              "preview": mini({"D2": "b"}, "".join(bd(n, c, "pill") for c, n in (("blue", "Đang chạy"), ("green", "Đã giao"), ("yellow", "Chờ điều"), ("gray", "Nháp"))))},
         ],
         "untitled": mini({"D2": "a"}, bd("Label", "blue", "pill")), "untitledNote": "ring-1 ring-inset",
         "astryx": mini({"D2": "b"}, bd("Đang chạy", "blue", "pill")), "astryxNote": "không viền"},
        {"id": "D3", "title": "Teal, tím, cam chỉ cho phân loại",
         "why": "Trạng thái cần màu <mark>có nghĩa</mark> (xanh lá xong, đỏ lỗi, vàng chờ…). Teal / tím / cam không có nghĩa trạng thái — dùng cho <b>Loại</b> (hàng lạnh, quá khổ) ở dạng Badge Modern (chấm màu, nền trắng) để không lẫn với cột trạng thái (mục R2).",
         "source": "Trang Duyệt Base components › R2 · Figma demo bảng lệnh 6657:165305",
         "options": [
             {"label": "Ghi thành luật", "desc": "Cột Trạng thái: Pill có nghĩa. Cột Loại: Badge Modern chấm màu.", "rec": True, "preview": TBL3("a")},
             {"label": "Không ghi luật", "desc": "Mỗi màn tự chọn kiểu và màu.", "preview": TBL3("b")},
         ]},
        {"id": "D4", "title": "Avatar group: avatar nào nằm trên",
         "why": "DEC-242 cũ: <mark>avatar đầu nằm trên</mark>. Untitled: avatar sau đè avatar trước (mép phải của mỗi avatar bị che). Mục L12.",
         "source": "Trang Duyệt Base components › L12 · DEC-242 · avatar.demo.tsx",
         "options": [
             {"label": "Như Untitled (sau đè trước)", "rec": True, "desc": "Ô +n ở cuối nằm trên cùng, đọc tự nhiên trái → phải.",
              "preview": mini({"D4": "a"}, group(4, 3, "md"))},
             {"label": "Đầu nằm trên (DEC-242)", "desc": "Người đầu tiên (người phụ trách) thấy trọn.",
              "preview": mini({"D4": "b"}, group(4, 3, "md"))},
         ]},
        {"id": "D5", "title": "Chấm Offline",
         "why": "Spec cũ: <mark>chấm rỗng viền xám</mark>; Untitled: chấm đặc xám. Chấm rỗng phân biệt được với Online khi in đen trắng / mù màu (mục L13).",
         "source": "Trang Duyệt Base components › L13 · Figma 6657:166192",
         "options": [
             {"label": "Chấm rỗng", "rec": True, "desc": "Khác Online cả hình lẫn màu.",
              "preview": mini({"D5": "a"}, av("lg", "image", status="on", i=0) + av("lg", "image", status="off", i=1))},
             {"label": "Chấm đặc xám", "desc": "Như Untitled.",
              "preview": mini({"D5": "b"}, av("lg", "image", status="on", i=0) + av("lg", "image", status="off", i=1))},
         ]},
        {"id": "D6", "title": "Thang cỡ Avatar",
         "why": "Lượt 1 đổi tên <mark>SM 24 → XS</mark> và thêm SM 32 (mục R10) theo Untitled; token hiện tại vẫn là 24 · 36 · 48 · 64 · 88. Cần chốt một thang cho cả Avatar và Company avatar.",
         "source": "Trang Duyệt Base components › R10 · tokens.json avatar/size/* · avatar.tsx sizes",
         "options": [
             {"label": "Theo Untitled 24 → 64", "rec": True, "desc": "XS 24 · SM 32 · MD 40 · LG 48 · XL 56 · XXL 64. Bước đều 8, khớp cao control 32 / 40.",
              "preview": mini({"D6": "a"}, "".join(av(s, "image", i=k) for k, (s, _) in enumerate(SIZES)))},
             {"label": "Theo token hiện tại", "desc": "XS 20 · SM 24 · MD 36 · LG 48 · XL 64 · XXL 88. Ảnh hồ sơ to hơn.",
              "preview": mini({"D6": "b"}, "".join(av(s, "image", i=k) for k, (s, _) in enumerate(SIZES)))},
         ]},
    ],
    "presets": [
        {"id": "rec", "label": "Đề xuất", "pick": {"D1": "a", "D2": "b", "D3": "a", "D4": "a", "D5": "a", "D6": "a"}},
        {"id": "untitled", "label": "Theo Untitled", "pick": {"D1": "a", "D2": "a", "D3": "a", "D4": "a", "D5": "b", "D6": "a"}},
        {"id": "astryx", "label": "Astryx hiện tại", "pick": {"D1": "b", "D2": "b", "D3": "b", "D4": "b", "D5": "a", "D6": "b"}},
    ],
    "screens": [
        {"id": "var-web", "name": "Bảng biến thể", "device": "web", "width": 1280, "shell": "none",
         "note": "Toàn bộ biến thể đã chốt 26/10, đổi theo D1–D6 và Light/Dark.", "html": VAR_WEB},
        {"id": "var-app", "name": "Bảng biến thể", "device": "mobile", "shell": "none", "note": "Cùng component trên khung app 393.", "html": VAR_APP},
        {"id": "list-web", "name": "Danh sách lệnh", "device": "web", "width": 1280, "nav": "Lệnh vận tải", "title": "Lệnh vận tải",
         "note": "Badge ở cột Trạng thái và Loại; Avatar label group ở cột Lái xe; Avatar group ở thanh ca trực. Bảng chọn › Hiển thị đổi Đang tải / Rỗng / Chữ dài.", "html": LIST},
        {"id": "team-app", "name": "Đội lái xe", "device": "mobile", "nav": "Tài khoản", "title": "Đội của tôi",
         "note": "Avatar có chấm trạng thái + Badge trạng thái chuyến.", "html": APP},
    ],
}

write(OUT, page)
