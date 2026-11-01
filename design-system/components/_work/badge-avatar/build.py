#!/usr/bin/env python3
"""Sinh page.json cho Badge + Avatar — brainstorm gọn (28/10).
Chạy: python3 design-system/components/_work/badge-avatar/build.py && python3 _scripts/ds-component-page.py badge-avatar
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

CSS_A = """
/* khung màn Bản B (thay style inline) */
/* góp ý 29/10: thử chữ badge 500 trong bảng danh sách (cột Trạng thái + Loại hàng); DEC-277 đang là 600 */
.tbl .fb .fl{font-weight:500}
[data-sx="bools4"]{grid-template-columns:60px repeat(4,max-content)}[data-sx="bools5"]{grid-template-columns:60px repeat(5,max-content)}
[data-sx="sx1"]{grid-template-columns:100px repeat(8,max-content)}
[data-sx="sx2"]{grid-template-columns:70px repeat(6,96px)}
[data-sx="sx3"]{gap:48px;align-items:flex-start;flex-wrap:wrap}
[data-sx="sx4"]{gap:28px}
[data-sx="sx5"]{gap:24px}
[data-sx="sx6"]{font-size:13px}
[data-sx="sx7"]{max-width:260px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
[data-sx="sx8"]{display:contents}
[data-sx="sx9"]{padding:0 24px}
[data-sx="sx10"]{overflow:hidden}
[data-sx="sx11"]{margin-top:-1px;border-top:0}
[data-sx="sx12"]{font:600 17px/24px var(--font-body)}
[data-sx="sx13"]{padding:4px 16px 0}
[data-sx="sx14"]{width:36px;height:36px;border-radius:50%}
[data-sx="sx15"]{width:140px}
[data-sx="sx16"]{width:200px;margin-top:6px}
[data-sx="sx17"]{display:flex;flex-direction:column;gap:12px}
[data-sx="sx18"]{font-size:15px;font-weight:600}
[data-sx="sx19"]{gap:8px}
[data-sx="sx20"]{display:flex;flex-direction:column;gap:14px;margin-top:16px}
[data-sx="sx21"]{width:320px}
/* ===== Bản A (đã thay bằng Bản B) — chỉ còn cho hình D1–D6 vòng brainstorm ===== */
/* ===== Badge ===== chữ type/chip-sm-strong mọi cỡ (DEC-277) */
.bd{display:inline-flex;align-items:center;gap:var(--space-xs);height:var(--size-3xl);padding:0 var(--space-lg);
 font:600 var(--chip-font-size-sm)/var(--chip-line-height-sm) var(--font-body);white-space:nowrap;max-width:var(--size-11xl);
 border:1px solid transparent;vertical-align:middle;color:var(--c-fg);background:var(--c-bg)}
.bd .bl{overflow:hidden;text-overflow:ellipsis;min-width:0}
.bd.sm{height:var(--chip-height-sm);padding:0 var(--chip-padding-x-sm)}.bd.lg{height:var(--chip-height-lg);padding:0 var(--chip-padding-x-lg)}
.bd.pill{border-radius:var(--radius-chip)}.bd.badge{border-radius:var(--radius-badge)}
.bd.modern{border-radius:var(--radius-badge);background:var(--color-bg-primary);color:var(--color-text-tertiary_strong);border-color:var(--color-border-primary);box-shadow:0 1px 2px var(--color-shadow-sm)}
.bd .bdot{width:6px;height:6px;border-radius:50%;background:var(--c-dot);flex:none}
.bd.modern .bi{color:var(--c-dot)}
.bd .bi{flex:none}
.bd .bc{font-weight:600;padding:0 5px;border-radius:3px;background:color-mix(in srgb,var(--c-fg) 12%,transparent);line-height:16px}
.bd.modern .bc{background:var(--color-bg-selected)}
.bd .bx{border:0;background:none;padding:0;margin-right:-4px;width:16px;height:16px;border-radius:3px;display:grid;place-items:center;color:inherit;opacity:.6;cursor:pointer}
.c-gray{--c-bg:var(--color-utility-neutral-100);--c-fg:var(--color-utility-neutral-600);--c-dot:var(--color-utility-neutral-500);--c-ring:var(--color-utility-neutral-200)}
.c-blue{--c-bg:var(--color-utility-blue-50);--c-fg:var(--color-utility-blue-700);--c-dot:var(--color-utility-blue-600);--c-ring:var(--color-utility-blue-200)}
.c-green{--c-bg:var(--color-utility-green-50);--c-fg:var(--color-utility-green-700);--c-dot:var(--color-utility-green-600);--c-ring:var(--color-utility-green-200)}
.c-yellow{--c-bg:var(--color-utility-yellow-50);--c-fg:var(--color-utility-yellow-700);--c-dot:var(--color-utility-yellow-600);--c-ring:var(--color-utility-yellow-200)}
.c-red{--c-bg:var(--color-utility-red-50);--c-fg:var(--color-utility-red-700);--c-dot:var(--color-utility-red-600);--c-ring:var(--color-utility-red-200)}
.c-teal{--c-bg:var(--color-utility-teal-50);--c-fg:var(--color-utility-teal-700);--c-dot:var(--color-utility-teal-600);--c-ring:var(--color-utility-teal-200)}
.c-purple{--c-bg:var(--color-utility-purple-50);--c-fg:var(--color-utility-purple-700);--c-dot:var(--color-utility-purple-600);--c-ring:var(--color-utility-purple-200)}
.c-orange{--c-bg:var(--color-utility-orange-100);--c-fg:var(--color-utility-orange-800);--c-dot:var(--color-utility-orange-600);--c-ring:var(--color-utility-orange-200)}
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
 background:var(--color-accent-bg);color:var(--color-accent-fg);vertical-align:middle}
.av .aimg{width:100%;height:100%;border-radius:50%;display:block}
.av .at{font:600 var(--fs)/1 var(--font-body);letter-spacing:-.01em}
.av .ai{width:calc(var(--s) * .5);height:calc(var(--s) * .5)}
.av.icon{background:var(--color-bg-selected);color:var(--color-fg-quaternary)}
.av.upload,.av.add{background:transparent;border:1px dashed var(--color-border-input);color:var(--color-text-tertiary);cursor:pointer}
.av.co{border-radius:calc(var(--s) * .22);background:var(--color-utility-blue-50);color:var(--color-utility-blue-700)}
.av.more{background:var(--color-bg-secondary);color:var(--color-text-primary)}
.av .ast{position:absolute;right:0;bottom:0;width:var(--dot);height:var(--dot);border-radius:50%;box-shadow:0 0 0 1.5px var(--color-bg-primary)}
.ast.on{background:var(--color-fg-success-primary)}.ast.busy{background:var(--color-fg-error-primary)}.ast.away{background:var(--color-fg-warning-primary)}
.ast.off{background:var(--color-utility-neutral-400)}
[data-D5=a] .ast.off{background:var(--color-bg-primary);box-shadow:inset 0 0 0 1.5px var(--color-utility-neutral-400),0 0 0 1.5px var(--color-bg-primary)}
/* D6: a thang Untitled 24·32·40·48·56·64 · b thang token hiện tại 20·24·36·48·64·88 */
.av.xs{--s:24px;--fs:10px;--dot:6px}.av.sm{--s:32px;--fs:12px;--dot:8px}.av.md{--s:40px;--fs:14px;--dot:10px}
.av.lg{--s:48px;--fs:16px;--dot:12px}.av.xl{--s:56px;--fs:18px;--dot:14px}.av.xxl{--s:64px;--fs:22px;--dot:16px}
[data-D6=b] .av.xs{--s:20px;--fs:9px;--dot:6px}[data-D6=b] .av.sm{--s:var(--size-4xl);--fs:10px;--dot:var(--size-md)}
[data-D6=b] .av.md{--s:var(--avatar-size-md);--fs:13px;--dot:var(--avatar-status-size-md)}[data-D6=b] .av.lg{--s:var(--size-6xl);--fs:16px;--dot:var(--size-lg)}
[data-D6=b] .av.xl{--s:var(--size-7xl);--fs:22px;--dot:var(--avatar-status-size-xl)}[data-D6=b] .av.xxl{--s:var(--avatar-size-xxl);--fs:28px;--dot:var(--size-xl)}
.szl{font:500 11px/14px var(--font-code);color:var(--color-text-disabled)}
[data-D6=a] .szl.b,[data-D6=b] .szl.a{display:none}
/* Avatar group — D4: a avatar sau đè avatar trước (Untitled) · b avatar đầu nằm trên (DEC-242) */
.ag{display:inline-flex;align-items:center}.ag .av{box-shadow:0 0 0 var(--size-xxs) var(--color-bg-primary)}
.ag .av+.av{margin-left:var(--avatar-group-overlap-sm)}.ag.md .av+.av{margin-left:var(--avatar-group-overlap-md)}
[data-D4=b] .ag .av:nth-child(1){z-index:6}[data-D4=b] .ag .av:nth-child(2){z-index:5}[data-D4=b] .ag .av:nth-child(3){z-index:4}
[data-D4=b] .ag .av:nth-child(4){z-index:3}[data-D4=b] .ag .av:nth-child(5){z-index:2}
/* Label group */
.alg{display:inline-flex;align-items:center;gap:10px;min-width:0;max-width:240px}
.alg .tx2{display:flex;flex-direction:column;min-width:0}.alg b{font:600 14px/20px var(--font-body);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.alg .tx2 span{font-size:12px;line-height:16px;color:var(--color-text-tertiary);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.alg.sm b{font-size:13px;line-height:18px}.alg.sm{gap:8px}
/* Màn demo */
.tbar{display:flex;align-items:center;gap:12px;padding:0 24px 12px}
.sk{display:inline-block;height:12px;border-radius:6px;background:var(--color-bg-selected);animation:pl 1.2s ease-in-out infinite}
@keyframes pl{50%{opacity:.5}}
.empty{padding:48px 24px;text-align:center;color:var(--color-text-tertiary)}
.mrow{display:flex;align-items:center;gap:12px;padding:12px 16px;border-bottom:1px solid var(--color-border-secondary)}
.mrow .tx2{flex:1;min-width:0}.mrow b{display:block;font:600 15px/20px var(--font-body);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.mrow .s{font-size:13px;line-height:18px;color:var(--color-text-tertiary)}
.prof{display:flex;flex-direction:column;align-items:center;gap:8px;padding:20px 16px 12px}
.flt{display:flex;gap:8px;padding:0 24px 12px;flex-wrap:wrap}
.dh{display:flex;align-items:center;gap:10px;margin-bottom:16px}
.kv{display:grid;grid-template-columns:140px 1fr;gap:14px 16px;margin:0;font-size:14px;line-height:20px}.kv dt{color:var(--color-text-tertiary)}.kv dd{margin:0;min-width:0}
.tg{display:inline-flex;align-items:center;gap:4px;height:24px;padding:0 4px 0 8px;border:1px solid var(--color-border-primary);border-radius:6px;font:600 12px/18px var(--font-body);color:var(--color-text-tertiary_strong)}
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

# =====================================================================================
# Bản B — theo cấu trúc Figma hiện tại (Section Badges 6657:165305 · Avatars 6657:165741, đo 29/10).
# Bản A (ở trên) giữ nguyên như bản đã đăng artifact; chọn bản ở điểm V.
# =====================================================================================
FSIZES = [("xs", "XS", 24), ("sm", "SM", 32), ("md", "MD", 36), ("lg", "LG", 48), ("xl", "XL", 64), ("xxl", "XXL", 88)]
FTYPES = [("pc", "Pill Color"), ("po", "Pill Outline"), ("bc", "Badge Color"), ("bo", "Badge Outline"), ("bm", "Badge Modern"), ("dt", "Dot")]


def fbd(label="Đang chạy", color="gray", typ="pc", size="md", dot=True, icon=None, count=None, count_only=None, x=False, attrs=""):
    """Badge Figma: Type × Color × Size + boolean Has Dot / Has Icon Leading / Has Count / Count Only / Has X Close / Has Label."""
    inner = ""
    if count_only is not None:
        inner = f'<span class="flw fco">{count_only}</span>'
    else:
        if icon:
            inner += f'<span class="fdw iw">{ic(icon, 14, "fi").replace('stroke-width="2"', 'stroke-width="2.5"')}</span>'
        elif dot:
            inner += '<span class="fdw"><i class="fdot"></i></span>'
        inner += f'<span class="flw"><span class="fl">{label}</span></span>'
        if count is not None:
            inner += f'<b class="fcnt">{count}</b>'
        if x:
            inner += f'<button class="fx" aria-label="Bỏ {label}">{ic("x", 14)}</button>'
    return f'<span class="fb {typ} {size} c-{color}" {attrs}>{inner}</span>'


def fstatus(status):
    if not status:
        return ""
    lab = {"on": "Đang trực", "off": "Ngoại tuyến", "busy": "Đang chạy chuyến", "away": "Tạm vắng"}[status]
    return f'<i class="fst {status}" aria-label="{lab}"><i></i></i>'


def fav(size="md", content="initials", text="NA", status=None, i=0, attrs=""):
    """Avatar Figma: Content Image | Loading | Initials | Icon | Upload × Size XS–XXL; Status = instance lồng _Avatar status."""
    if content in ("image", "loading"):
        inner = '<span class="fph" role="img" aria-label="Ảnh đại diện"></span>'
    elif content == "icon":
        inner = ic("user", 20, "fai")
    else:
        inner = f'<span class="fat">{text}</span>'
    if content == "loading":
        inner += ('<span class="fscrim"></span><svg class="fspin" viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="6" fill="none" '
                  'stroke="#fff" stroke-opacity=".3" stroke-width="2"/><path d="M8 2a6 6 0 0 1 6 6" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"/></svg>')
    if content in ("upload", "loading"):
        inner += f'<span class="fup{" dis" if content == "loading" else ""}" aria-label="Đổi ảnh đại diện">{ic("camera", 12, "fupi")}</span>'
    st = fstatus(status) if content not in ("upload", "loading") else ""
    return f'<span class="fa {size} {content}" {attrs}>{inner}{st}</span>'


def fcompany(size="md", content="initials", text="DL"):
    inner = {"image": ic("image", 16, "fai"), "icon": ic("building", 16, "fai")}.get(content, f'<span class="fat">{text}</span>')
    return f'<span class="fa {size} co {content}">{inner}</span>'


def fgroup(size="md", more=3):
    s = {"xs": "xs", "md": "md", "lg": "lg"}[size]
    items = "".join(f'<span class="fgw{" n" if k else ""}">{fav(s, "initials" if k % 2 else "image", ["TB", "LC", "PD", "NA"][k], i=k)}</span>' for k in range(4))
    return f'<span class="fg {s}">{items}<span class="fgw n"><span class="fa {s} more"><span class="fat">+{more}</span></span></span></span>'


def flg(name="Nguyễn Văn An", sub="Lái xe · 51C-123.45", size="md", status=None, content="initials", text="NA", i=0):
    av_size = {"sm": "sm", "md": "md", "lg": "lg"}[size]
    return f'<span class="flg {size}">{fav(av_size, content, text, status, i)}<span class="ftx"><b>{name}</b><span>{sub}</span></span></span>'


def fadd(state="default"):
    if state == "loading":
        return ('<button class="fadd loading" aria-label="Thêm người" aria-busy="true" disabled><svg viewBox="0 0 16 16" aria-hidden="true">'
                '<circle cx="8" cy="8" r="6" fill="none" stroke="currentColor" stroke-opacity=".3" stroke-width="2"/>'
                '<path d="M8 2a6 6 0 0 1 6 6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button>')
    return f'<button class="fadd {state}" aria-label="Thêm người"{" disabled" if state == "disabled" else ""}>{ic("plus", 24)}</button>'


import base64  # noqa: E402
PHOTO = base64.b64encode((Path(__file__).parent / "assets/avatar-photo.jpg").read_bytes()).decode()  # ảnh mẫu Figma 6657:166104 (Unsplash)

CSS = tok_css() + """
.c-gray{--c-bg:var(--color-utility-neutral-100);--c-fg:var(--color-utility-neutral-600);--c-dot:var(--color-utility-neutral-500);--c-ring:var(--color-utility-neutral-200)}
.c-blue{--c-bg:var(--color-utility-blue-50);--c-fg:var(--color-utility-blue-700);--c-dot:var(--color-utility-blue-600);--c-ring:var(--color-utility-blue-200)}
.c-green{--c-bg:var(--color-utility-green-50);--c-fg:var(--color-utility-green-700);--c-dot:var(--color-utility-green-600);--c-ring:var(--color-utility-green-200)}
.c-yellow{--c-bg:var(--color-utility-yellow-50);--c-fg:var(--color-utility-yellow-700);--c-dot:var(--color-utility-yellow-600);--c-ring:var(--color-utility-yellow-200)}
.c-red{--c-bg:var(--color-utility-red-50);--c-fg:var(--color-utility-red-700);--c-dot:var(--color-utility-red-600);--c-ring:var(--color-utility-red-200)}
.c-teal{--c-bg:var(--color-utility-teal-50);--c-fg:var(--color-utility-teal-700);--c-dot:var(--color-utility-teal-600);--c-ring:var(--color-utility-teal-200)}
.c-purple{--c-bg:var(--color-utility-purple-50);--c-fg:var(--color-utility-purple-700);--c-dot:var(--color-utility-purple-600);--c-ring:var(--color-utility-purple-200)}
.c-orange{--c-bg:var(--color-utility-orange-100);--c-fg:var(--color-utility-orange-800);--c-dot:var(--color-utility-orange-600);--c-ring:var(--color-utility-orange-200)}
"""
CSS += f".fa .fph{{position:absolute;inset:0;border-radius:inherit;background:url(data:image/jpeg;base64,{PHOTO}) center/cover}}"
CSS += """
/* ===================== Bản B — theo Figma ===================== */
/* Badge theo spec Status chip (DEC-310): chữ type/caption-strong (SM type/chip-sm-strong 12/18) · chấm 8 → chữ 6 · icon 14 → chữ 4 · lề phía chấm/icon 6/8/10, phía chữ 10/12/14. Số đo viết theo từng cỡ để trang đối chiếu ghi đè đúng cỡ */
.fb{display:inline-flex;align-items:center;vertical-align:middle;white-space:nowrap;font:600 var(--type-caption-size)/var(--type-caption-line-height) var(--font-body);outline-offset:-1px}
.fb.pc,.fb.po{border-radius:var(--radius-full)}
.fb.sm{height:22px;gap:var(--space-xs);padding-left:var(--space-sm);font-size:var(--chip-font-size-sm);line-height:var(--chip-line-height-sm)}
.fb.pc.sm,.fb.po.sm{padding-right:var(--chip-padding-x-sm)}
.fb.bc.sm,.fb.bo.sm,.fb.bm.sm{padding-right:var(--chip-padding-x-sm);border-radius:6px}
.fb.sm .fcnt{height:16px}
.fb.bc.sm .fcnt,.fb.bo.sm .fcnt,.fb.bm.sm .fcnt{border-radius:3px}
.fb.md{height:24px;gap:var(--space-xs);padding-left:var(--space-md)}
.fb.pc.md,.fb.po.md{padding-right:var(--space-lg)}
.fb.bc.md,.fb.bo.md,.fb.bm.md{padding-right:var(--space-lg);border-radius:6px}
.fb.md .fcnt{height:16px}
.fb.bc.md .fcnt,.fb.bo.md .fcnt,.fb.bm.md .fcnt{border-radius:3px}
.fb.lg{height:28px;gap:var(--space-xs);padding-left:var(--chip-padding-x-icon-lg)}
.fb.pc.lg,.fb.po.lg{padding-right:var(--chip-padding-x-lg)}
.fb.bc.lg,.fb.bo.lg,.fb.bm.lg{padding-right:var(--chip-padding-x-lg);border-radius:8px}
.fb.lg .fcnt{height:20px}
.fb.bc.lg .fcnt,.fb.bo.lg .fcnt,.fb.bm.lg .fcnt{border-radius:4px}
/* Có ô đếm: lề phải thu về chip/count-inset 3 · 3 · 4 để ô đếm cách đều trên, dưới, phải (DEC-303, DEC-310) */
.fb.sm:has(.fcnt){padding-right:var(--chip-count-inset)}
.fb.md:has(.fcnt),.fb.lg:has(.fcnt){padding-right:var(--space-xs)}
/* Count Only (chỉ có số): khung số đệm trái space/xs 4 → số cách đều hai bên 10 · 12 · 14 (DEC-310) */
.fb .flw.fco{padding-left:var(--space-xs)}
/* Type Dot: không nền, không lề, chữ type/caption 400 màu text/primary (SM 12/18), chấm theo màu */
.fb.dt[class]{background:transparent;color:var(--color-text-primary);font-weight:400;padding-left:0;padding-right:0;outline:0}
/* viền (user 29/10): Pill Outline màu theo sắc 200 · Badge Outline + Modern xám. Viết riêng từng màu — không qua biến chung để trang đối chiếu không đè mọi badge */
/* màu theo sắc, viết riêng từng màu (không qua biến chung) */
.fb.c-gray{background:var(--color-utility-neutral-100);color:var(--color-utility-neutral-600)}.fb.c-gray .fdot{background:var(--color-utility-neutral-600)}.fb.c-gray .fi{color:var(--color-utility-neutral-600)}
.fb.c-blue{background:var(--color-utility-blue-50);color:var(--color-utility-blue-700)}.fb.c-blue .fdot{background:var(--color-utility-blue-700)}.fb.c-blue .fi{color:var(--color-utility-blue-700)}
.fb.c-green{background:var(--color-utility-green-50);color:var(--color-utility-green-700)}.fb.c-green .fdot{background:var(--color-utility-green-700)}.fb.c-green .fi{color:var(--color-utility-green-700)}
.fb.c-yellow{background:var(--color-utility-yellow-50);color:var(--color-utility-yellow-700)}.fb.c-yellow .fdot{background:var(--color-utility-yellow-700)}.fb.c-yellow .fi{color:var(--color-utility-yellow-700)}
.fb.c-red{background:var(--color-utility-red-50);color:var(--color-utility-red-700)}.fb.c-red .fdot{background:var(--color-utility-red-700)}.fb.c-red .fi{color:var(--color-utility-red-700)}
.fb.c-teal{background:var(--color-utility-teal-50);color:var(--color-utility-teal-700)}.fb.c-teal .fdot{background:var(--color-utility-teal-700)}.fb.c-teal .fi{color:var(--color-utility-teal-700)}
.fb.c-purple{background:var(--color-utility-purple-50);color:var(--color-utility-purple-700)}.fb.c-purple .fdot{background:var(--color-utility-purple-700)}.fb.c-purple .fi{color:var(--color-utility-purple-700)}
.fb.c-orange{background:var(--color-utility-orange-100);color:var(--color-utility-orange-800)}.fb.c-orange .fdot{background:var(--color-utility-orange-800)}.fb.c-orange .fi{color:var(--color-utility-orange-800)}
.fb.bm{outline:1px solid var(--color-border-primary)} /* Badge Outline viền theo màu như Pill Outline (user 29/10) */
.fb.po.c-gray,.fb.bo.c-gray{outline:1px solid var(--color-utility-neutral-200)}.fb.po.c-blue,.fb.bo.c-blue{outline:1px solid var(--color-utility-blue-200)}.fb.po.c-green,.fb.bo.c-green{outline:1px solid var(--color-utility-green-200)}.fb.po.c-yellow,.fb.bo.c-yellow{outline:1px solid var(--color-utility-yellow-200)}.fb.po.c-red,.fb.bo.c-red{outline:1px solid var(--color-utility-red-200)}.fb.po.c-teal,.fb.bo.c-teal{outline:1px solid var(--color-utility-teal-200)}.fb.po.c-purple,.fb.bo.c-purple{outline:1px solid var(--color-utility-purple-200)}.fb.po.c-orange,.fb.bo.c-orange{outline:1px solid var(--color-utility-orange-200)}
.fb.bm[class]{background:var(--color-bg-primary);color:var(--color-text-primary)}
.fb .fdw{display:inline-flex;align-items:center}

.fb .fdw:not(.iw){margin-right:var(--space-xxs)} /* chấm → chữ = space/xs 4 + 2 = space/sm 6 (DEC-310) */
.fb .fdot{width:var(--size-sm);height:var(--size-sm);border-radius:50%;display:block}
.fb .fi{width:14px;height:14px;display:block}
.fb .flw{display:inline-flex;min-width:0;max-width:160px}
.fb .fl{overflow:hidden;text-overflow:ellipsis;min-width:0}
.fb .fcnt{display:inline-flex;align-items:center;padding:0 6px;font:400 var(--chip-count-font-size)/var(--chip-count-line-height) var(--font-body);background:var(--color-bg-primary)}
.fb .fco{font:400 var(--chip-count-font-size)/var(--chip-count-line-height) var(--font-body)} /* Count Only: caption 400 cố định (review R3, R11) */
.fb.pc .fcnt,.fb.po .fcnt{border-radius:var(--radius-full)}
.fb.bm .fcnt{background:var(--color-bg-secondary)}

/* Avatar: XS 24 · SM 32 · MD 36 · LG 48 · XL 64 · XXL 88 · chữ Initials 500. Số đo viết thẳng theo từng cỡ (lý do như Badge) */
.fa{position:relative;display:inline-grid;place-items:center;flex:none;border-radius:50%;background:var(--color-accent-bg);color:var(--color-accent-fg);vertical-align:middle}
.fa .aimg{width:100%;height:100%;border-radius:inherit;display:block}
.fa .fat{font-weight:500;font-family:var(--font-body)}
.fa .fai{color:var(--color-fg-quaternary)}
.fa .fscrim{position:absolute;inset:0;border-radius:50%;background:var(--color-bg-overlay)}
.fa .fspin{position:absolute;animation:fsp 1s linear infinite}
@keyframes fsp{to{transform:rotate(360deg)}}
.fa .fup{position:absolute;right:0;bottom:0;border-radius:50%;background:var(--color-bg-primary);border:1px solid var(--color-border-secondary);display:grid;place-items:center;color:var(--color-fg-quaternary)}
.fa .fup.dis{background:var(--color-bg-secondary)}.fa .fup.dis .fupi{opacity:.4}
/* _Avatar status: chấm + viền trắng 2; Offline = chấm rỗng viền xám 2. Vị trí tương đương mọi cỡ: tâm chấm trên mép tròn ở góc 45° (lệch khỏi góc khung 0,1464 × cỡ) */
.fa .fst{position:absolute;padding:2px;border-radius:50%;background:var(--color-bg-primary);display:block;line-height:0}
.fa .fst>i{display:block;border-radius:50%}
.fst.on>i{background:var(--color-fg-success-primary)}.fst.busy>i{background:var(--color-fg-error-primary)}.fst.away>i{background:var(--color-fg-warning-primary)}
.fst.off>i{background:var(--color-bg-primary);border:2px solid var(--color-utility-neutral-500);box-sizing:border-box}
.fa.xs{width:24px;height:24px}
.fa.xs .fat{font-size:12px;line-height:16px}
.fa.xs .fai{width:14px;height:14px}
.fa.xs .fspin{width:12px;height:12px}
.fa.xs .fup{width:14px;height:14px}
.fa.xs .fupi{width:12px;height:12px}
.fa.xs .fst{right:-1.5px;bottom:-1.5px}
.fa.xs .fst>i{width:6px;height:6px}
.fa.sm{width:32px;height:32px}
.fa.sm .fat{font-size:12px;line-height:16px}
.fa.sm .fai{width:16px;height:16px}
.fa.sm .fspin{width:14px;height:14px}
.fa.sm .fup{width:16px;height:16px}
.fa.sm .fupi{width:12px;height:12px}
.fa.sm .fst{right:-1.3px;bottom:-1.3px}
.fa.sm .fst>i{width:8px;height:8px}
.fa.md{width:var(--avatar-size-md);height:var(--avatar-size-md)}
.fa.md .fat{font-size:14px;line-height:20px}
.fa.md .fai{width:20px;height:20px}
.fa.md .fspin{width:16px;height:16px}
.fa.md .fup{width:16px;height:16px}
.fa.md .fupi{width:12px;height:12px}
.fa.md .fst{right:-1.7px;bottom:-1.7px}
.fa.md .fst>i{width:10px;height:10px}
.fa.lg{width:var(--size-6xl);height:var(--size-6xl)}
.fa.lg .fat{font-size:17px;line-height:24px}
.fa.lg .fai{width:24px;height:24px}
.fa.lg .fspin{width:20px;height:20px}
.fa.lg .fup{width:20px;height:20px}
.fa.lg .fupi{width:14px;height:14px}
.fa.lg .fst{right:-1.0px;bottom:-1.0px}
.fa.lg .fst>i{width:12px;height:12px}
.fa.xl{width:var(--size-7xl);height:var(--size-7xl)}
.fa.xl .fat{font-size:20px;line-height:28px}
.fa.xl .fai{width:24px;height:24px}
.fa.xl .fspin{width:24px;height:24px}
.fa.xl .fup{width:24px;height:24px}
.fa.xl .fupi{width:16px;height:16px}
.fa.xl .fst{right:0.4px;bottom:0.4px}
.fa.xl .fst>i{width:14px;height:14px}
.fa.xxl{width:var(--avatar-size-xxl);height:var(--avatar-size-xxl)}
.fa.xxl .fat{font-size:24px;line-height:32px}
.fa.xxl .fai{width:24px;height:24px}
.fa.xxl .fspin{width:28px;height:28px}
.fa.xxl .fup{width:32px;height:32px}
.fa.xxl .fupi{width:20px;height:20px}
.fa.xxl .fst{right:2.9px;bottom:2.9px}
.fa.xxl .fst>i{width:16px;height:16px}
/* Company avatar: vuông bo theo cỡ, viền 1 */
.fa.co{border-radius:6px;border:1px solid var(--color-border-secondary)}.fa.co.image{background:var(--color-bg-primary)}
.fa.co.xs{border-radius:4px}.fa.co.lg{border-radius:8px}.fa.co.xl{border-radius:12px}.fa.co.xxl{border-radius:16px}
/* Avatar group: mỗi avatar trong khung trắng đệm 2, chồng −6/−8/−12; ô +n nền muted */
.fg{display:inline-flex;align-items:center}.fg .fgw{display:inline-flex;padding:2px;border-radius:50%;background:var(--color-bg-primary);position:relative}
.fg.xs .fgw.n{margin-left:var(--avatar-group-overlap-sm)}.fg.md .fgw.n{margin-left:var(--avatar-group-overlap-md)}.fg.lg .fgw.n{margin-left:var(--avatar-group-overlap-lg)}
.fg .fa.more{background:var(--color-bg-secondary);color:var(--color-text-tertiary_strong)}
[data-D4=b] .fg .fgw:nth-child(1){z-index:5}[data-D4=b] .fg .fgw:nth-child(2){z-index:4}[data-D4=b] .fg .fgw:nth-child(3){z-index:3}[data-D4=b] .fg .fgw:nth-child(4){z-index:2}
/* Avatar label group: rộng 240, cách 8; SM 32 + 14/20 · 12/16 · MD 36 + 14/20 · 14/20 · LG 48 + 14/20 · 14/20 */
.flg{display:inline-flex;align-items:center;gap:8px;width:240px;max-width:100%;min-width:0}
.flg .ftx{display:flex;flex-direction:column;min-width:0;flex:1}
.flg b{font:600 14px/20px var(--font-body);color:var(--color-text-primary);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.flg .ftx span{font:400 var(--avatar-label-subtitle-size)/var(--avatar-label-subtitle-line-height) var(--font-body);color:var(--color-text-tertiary);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
/* Avatar add button: State Default · Hover · Focus · Disabled, 36 */
.fadd{width:48px;height:48px;border-radius:50%;border:1px dashed var(--color-border-primary);background:var(--color-bg-primary);color:var(--color-fg-quaternary);
 display:inline-grid;place-items:center;padding:0;cursor:pointer}
.fadd svg{width:24px;height:24px}.fadd.hover,.fadd:hover{background:var(--color-bg-primary_hover)}
.fadd.loading{cursor:progress}.fadd.loading svg{animation:fsp 1s linear infinite}
.fadd.focus,.fadd:focus-visible{outline:var(--focus-width) solid var(--focus-color);outline-offset:var(--focus-offset)}
.fadd:disabled{opacity:.4;cursor:not-allowed}
.vnote{font:400 12px/16px var(--font-body);color:var(--color-text-disabled);white-space:normal}
"""


def f_badge_types():
    head = '<div class="vl"></div>' + "".join(f'<div class="vl">{n}</div>' for _, n, _ in COLORS)
    rows = "".join(f'<div class="vl">{n}</div>' + "".join(f'<div>{fbd("Đang chạy", c, t)}</div>' for c, _, _ in COLORS) for t, n in FTYPES)
    return f'<div class="vgrid" data-sx="sx1">{head}{rows}</div>'


def f_badge_bools(x=True):
    cols = ("Has Dot (mặc định)", "Has Icon Leading", "Has Count", "Count Only") + (("Has X Close",) if x else ())
    out = '<div class="vl"></div>' + "".join(f'<div class="vl">{x}</div>' for x in cols)
    for sz, lab in (("sm", "SM 22"), ("md", "MD 24"), ("lg", "LG 28")):
        out += (f'<div class="vl">{lab}</div><div>{fbd("Đang chạy", "blue", "pc", sz)}</div>'
                f'<div>{fbd("Đã giao", "green", "pc", sz, icon="truck")}</div>'
                f'<div>{fbd("Chờ điều", "yellow", "pc", sz, count=12)}</div>'
                f'<div>{fbd(color="red", typ="pc", size=sz, count_only=12)}</div>'
                + (f'<div>{fbd("Hàng lạnh", "teal", "bc", sz, x=True)}</div>' if x else ""))
    return f'<div class="vgrid" data-sx="bools{len(cols)}">{out}</div>'


def f_badge_types_size():
    out = '<div class="vl"></div>' + "".join(f'<div class="vl">{n}</div>' for n in ("Badge Color", "Badge Color + Count", "Badge Outline + Count", "Badge Modern + Count"))
    for sz, lab in (("sm", "SM 22"), ("md", "MD 24"), ("lg", "LG 28")):
        out += (f'<div class="vl">{lab}</div><div>{fbd("Hàng lạnh", "teal", "bc", sz)}</div><div>{fbd("Chờ điều", "yellow", "bc", sz, count=12)}</div>'
                f'<div>{fbd("Chờ điều", "yellow", "bo", sz, count=12)}</div><div>{fbd("Hàng lạnh", "teal", "bm", sz, count=3)}</div>')
    return f'<div class="vgrid" data-sx="bools4">{out}</div>'


def f_av_matrix():
    head = '<div class="vl"></div>' + "".join(f'<div class="vl">{n} · {px}</div>' for _, n, px in FSIZES)
    rows = ""
    for content, lab in (("image", "Image"), ("loading", "Loading"), ("initials", "Initials"), ("icon", "Icon"), ("upload", "Upload")):
        rows += f'<div class="vl">{lab}</div>' + "".join(f'<div>{fav(s, content, "NA", i=k % 4)}</div>' for k, (s, _, _) in enumerate(FSIZES))
    return f'<div class="vgrid" data-sx="sx2">{head}{rows}</div>'


def f_co_matrix():
    head = '<div class="vl"></div>' + "".join(f'<div class="vl">{n}</div>' for _, n, _ in FSIZES)
    rows = "".join(f'<div class="vl">{lab}</div>' + "".join(f'<div>{fcompany(s, c)}</div>' for s, _, _ in FSIZES)
                   for c, lab in (("image", "Image"), ("initials", "Initials"), ("icon", "Icon")))
    return f'<div class="vgrid" data-sx="sx2">{head}{rows}</div>'


def f_status_matrix():
    head = '<div class="vl"></div>' + "".join(f'<div class="vl">{n}</div>' for _, n, _ in FSIZES)
    rows = "".join(f'<div class="vl">{lab}</div>' + "".join(f'<div>{fav(s, "initials", "NA", st)}</div>' for s, _, _ in FSIZES)
                   for st, lab in ((None, "None"), ("on", "Online"), ("off", "Offline"), ("busy", "Busy"), ("away", "Away")))
    return f'<div class="vgrid" data-sx="sx2">{head}{rows}</div>'


VNOTE = '<p class="vnote">Bản B theo Figma: viền (D2), chấm Offline (D5) và thang cỡ (D6) lấy đúng như Figma, không đổi theo D2/D5/D6. D1, D3, D4 vẫn áp dụng.</p>'

VAR_WEB_F = f"""<div class="vt">{VNOTE}
<div><div class="vh">Badge · Type × Color <small>Size=MD · 5 kiểu theo Figma (6657:165736)</small></div>{f_badge_types()}</div>
<div><div class="vh">Badge · Size × phần thêm <small>boolean, không phải biến thể · SM 22 · MD 24 · LG 28</small></div>{f_badge_bools()}</div>
<div><div class="vh">Chữ dài <small>khung chữ tối đa 160, cắt "…"</small></div>
 <div class="vg">{fbd("Chờ chứng từ hải quan tại cảng Cát Lái", "yellow", "pc")}{fbd("Hàng nguy hiểm nhóm 3 — chất lỏng dễ cháy", "red", "bc")}{fbd("Hàng lạnh âm 18 độ, cần cắm điện", "teal", "bm")}</div></div>
<div><div class="vh">Avatar · Content × Size <small>5 nội dung × 6 cỡ (6657:166192)</small></div>{f_av_matrix()}</div>
<div class="row" data-sx="sx3">
 <div><div class="vh">Company avatar · Content × Size</div>{f_co_matrix()}</div>
 <div><div class="vh">_Avatar status · Status × Size <small>instance lồng, nội bộ</small></div>{f_status_matrix()}</div>
</div>
<div class="row" data-sx="sx3">
 <div><div class="vh">Avatar group · Size <small>XS · MD · LG</small></div><div class="vg" data-sx="sx4">{fgroup("xs")}{fgroup("md")}{fgroup("lg")}</div></div>
 <div><div class="vh">Avatar add button · State</div><div class="vg">{fadd("default")}{fadd("loading")}{fadd("hover")}{fadd("focus")}{fadd("disabled")}</div></div>
</div>
<div><div class="vh">Avatar label · Size <small>avatar + tên + dòng phụ, rộng 240 (Figma đang đặt tên set "Avatar label group" → đổi khi sửa Figma)</small></div><div class="vg" data-sx="sx5">{flg(size="sm")}{flg(size="md")}{flg(size="lg")}
 {flg("Nguyễn Hoàng Thị Phương Thảo", "Điều phối viên ca đêm · Đội Sóng Thần", "md", text="NP")}</div></div>
</div>"""

VAR_APP_F = f"""<div class="vt">{VNOTE}
<div><div class="vh">Badge trên app <small>cùng số đo (nhóm A)</small></div>
 <div class="vg">{fbd("Đang chạy", "blue", "pc")}{fbd("Đã giao", "green", "pc", icon="check")}{fbd("Trễ 25 phút", "red", "po")}{fbd("Hàng lạnh", "teal", "bm")}{fbd("Chờ điều", "yellow", "pc", count=3)}</div></div>
<div><div class="vh">Avatar + status</div><div class="vg">{fav("sm", "image", status="on", i=0)}{fav("md", "image", status="busy", i=1)}{fav("lg", "initials", "LC", status="away")}{fav("xl", "image", status="off", i=2)}</div></div>
<div><div class="vh">Avatar label</div>{flg("Trần Văn Bình", "Lái xe · 51C-123.45", "md", "on", "image", i=0)}</div>
<div><div class="vh">Ảnh hồ sơ <small>Upload → Loading → Image</small></div><div class="vg">{fav("xxl", "upload", "NA")}{fav("xxl", "loading", i=3)}{fav("xxl", "image", i=3)}</div></div>
<div><div class="vh">Avatar group</div>{fgroup("md", 2)}</div>
</div>"""


def lst_rows_f(long=False):
    out = ""
    for k, (code, route, (st, sc), (ty, tc), drv) in enumerate(ROWS):
        if long and k == 0:
            st, route = "Chờ chứng từ hải quan tại cảng Cát Lái", "Tân Cảng Cát Lái (cổng B) → ICD Sóng Thần, Dĩ An, Bình Dương"
        # bảng danh sách: badge trạng thái dạng Icon Leading (góp ý 29/10), icon theo bộ icon badge trên Figma
        icon = {"Đang chạy": "navigation", "Trễ 25 phút": "triangle-alert", "Chờ điều": "hourglass", "Đã giao": "circle-check"}.get(st, "clock")
        free = fbd(st, sc, "pc", icon=icon, attrs="data-cmp")
        typ = (f'<span class="st-rule">{fbd(ty, tc, "bm", attrs="data-cmp")}</span>'
               f'<span class="st-free">{fbd(ty, tc, "bc", attrs="data-cmp")}</span>')
        d = (flg(drv[0], drv[1], "sm", None, "image", i=drv[2]) if drv  # danh sách: avatar không có chấm trạng thái (góp ý 29/10)
             else '<span class="muted" data-sx="sx6">Chưa điều</span>')
        out += (f'<tr><td class="mono">{code}</td><td data-sx="sx7">{route}</td>'
                f'<td>{free}</td><td>{typ}</td><td>{d}</td></tr>')
    return out


LIST_F = f"""<div class="tbar"><span class="muted" data-sx="sx6">Ca trực hôm nay</span>{fgroup("xs", 3)}<span class="sp"></span>
<span class="muted" data-sx="sx6">48 lệnh</span></div>
<div class="flt"><span class="xtag tg">Đang chạy <button aria-label="Bỏ lọc">{ic("x", 12)}</button></span><span class="xtag tg">Hàng lạnh <button aria-label="Bỏ lọc">{ic("x", 12)}</button></span>
</div>
<div data-sx="sx9"><table class="tbl card" data-sx="sx10"><tr><th>Mã lệnh</th><th>Tuyến</th><th>Trạng thái</th><th>Loại hàng</th><th>Lái xe</th></tr>
<tbody data-hide="long">{lst_rows_f()}</tbody><tbody data-show="state:long">{lst_rows_f(True)}</tbody></table></div>"""

APP_F = (f'<div class="prof">{fav("xxl", "image", status="on", i=3, attrs="data-cmp")}<b data-sx="sx12">Nguyễn Văn An</b>'
         f'<span class="muted" data-sx="sx6">Đội trưởng ca ngày</span></div>'
         f'<div class="vh" data-sx="sx13">Lái xe trong đội</div>'
         + "".join(f'<div class="mrow">{fav("md", "image" if k != 1 else "initials", "LC", s, i=k, attrs="data-cmp")}<div class="tx2"><b>{n}</b><div class="s">{sub}</div></div>{fbd(st, sc, "pc", attrs="data-cmp")}</div>'
                   for k, (n, sub, s, (st, sc), _) in enumerate(DRIVERS))
)


# ---------- Vòng 2 · Preview (tổ hợp chốt 29/10: V=B theo Figma · D1 A bỏ X · D3 A · D4 A) ----------
PICK = {"V": "b", "D1": "a", "D2": "b", "D3": "a", "D4": "a", "D5": "a", "D6": "a"}
_pa = " ".join(f'data-{k}="{v}"' for k, v in PICK.items())

PV_WEB = f"""<div class="vt">
<div><div class="vh">Badge · Type × Color <small>Size=MD</small></div>{f_badge_types()}</div>
<div><div class="vh">Badge · Size × phần thêm <small>boolean · SM 22 · MD 24 · LG 28 · không có X (D1 = A, chip lọc dùng Tag)</small></div>{f_badge_bools(False)}</div>
<div><div class="vh">Badge Color · Outline · Modern theo cỡ <small>bo 6 · 6 · 8, ô đếm bo đồng tâm 3 · 3 · 4</small></div>{f_badge_types_size()}</div>
<div><div class="vh">Chữ dài <small>khung chữ tối đa 160, cắt "…", tooltip hiện đủ</small></div>
 <div class="vg">{fbd("Chờ chứng từ hải quan tại cảng Cát Lái", "yellow", "pc")}{fbd("Hàng nguy hiểm nhóm 3 — chất lỏng dễ cháy", "red", "bc")}{fbd("Hàng lạnh âm 18 độ, cần cắm điện", "teal", "bm")}</div></div>
<div><div class="vh">Avatar · Content × Size</div>{f_av_matrix()}</div>
<div><div class="vh">_Avatar status · Status × Size <small>instance lồng, nội bộ</small></div>{f_status_matrix()}</div>
<div><div class="vh">Company avatar · Content × Size</div>{f_co_matrix()}</div>
<div class="row" data-sx="sx3">
 <div><div class="vh">Avatar group · Size</div><div class="vg" data-sx="sx4">{fgroup("xs")}{fgroup("md")}{fgroup("lg")}</div></div>
 <div><div class="vh">Avatar add button · State</div><div class="vg">{fadd("default")}{fadd("loading")}{fadd("hover")}{fadd("focus")}{fadd("disabled")}</div></div>
</div>
<div><div class="vh">Avatar label · Size <small>rộng 240</small></div><div class="vg" data-sx="sx5">{flg(size="sm")}{flg(size="md")}{flg(size="lg")}
 {flg("Nguyễn Hoàng Thị Phương Thảo", "Điều phối viên ca đêm · Đội Sóng Thần", "md", text="NP")}</div></div>
</div>"""

PV_MOB = [
    f"""<div class="vt"><div><div class="vh">Badge</div><div class="vg">{fbd("Đang chạy", "blue", "pc")}{fbd("Đã giao", "green", "pc", icon="check")}{fbd("Trễ 25 phút", "red", "po")}{fbd("Chờ điều", "yellow", "pc", count=3)}{fbd("Hàng lạnh", "teal", "bm")}{fbd(color="red", count_only=5)}</div></div>
<div><div class="vh">Chữ dài</div><div class="vg">{fbd("Chờ chứng từ hải quan tại cảng Cát Lái", "yellow", "pc")}</div></div></div>""",
    f"""<div class="vt"><div><div class="vh">Avatar + status</div><div class="vg">{fav("sm", "image", status="on")}{fav("md", "image", status="busy")}{fav("lg", "initials", "LC", status="away")}{fav("xl", "image", status="off")}</div></div>
<div><div class="vh">Avatar label · Avatar group</div><div data-sx="sx17">{flg("Trần Văn Bình", "Lái xe · 51C-123.45", "md", "on", "image")}{flg("Nguyễn Hoàng Thị Phương Thảo", "Điều phối viên ca đêm · Đội Sóng Thần", "md", text="NP")}{fgroup("md", 2)}</div></div></div>""",
    f"""<div class="vt"><div><div class="vh">Ảnh hồ sơ <small>Upload → Loading → Image</small></div><div class="vg">{fav("xxl", "upload", "NA")}{fav("xxl", "loading")}{fav("xxl", "image", status="on")}</div></div>
<div><div class="vh">Company avatar</div><div class="vg">{fcompany("lg", "image")}{fcompany("lg", "initials")}{fcompany("lg", "icon")}</div></div></div>""",
]

DETAIL_F = f"""<div class="pg">
<div class="dh"><span class="mono" data-sx="sx18">LVT-2026-0412</span>
 <span data-hide="long">{fbd("Đang chạy", "blue", "pc", "lg", attrs="data-cmp")}</span><span data-show="state:long">{fbd("Chờ chứng từ hải quan tại cảng Cát Lái", "yellow", "pc", "lg", attrs="data-cmp")}</span>
 {fbd("Hàng lạnh", "teal", "bm", "lg", attrs="data-cmp")}<span class="sp"></span>
 <span class="muted" data-sx="sx6">Người theo dõi</span>{fgroup("xs", 2)}{fadd()}</div>
<dl class="kv">
 <dt>Khách hàng</dt><dd><span class="row" data-sx="sx19">{fcompany("sm", "initials", "DL")}<span>Delta Logistics</span></span></dd>
 <dt>Tuyến</dt><dd>Cát Lái → ICD Sóng Thần</dd>
 <dt>Lái xe</dt><dd>{flg("Trần Văn Bình", "51C-123.45 · đang chạy chuyến", "md", "busy", "image")}</dd>
 <dt>Điều phối</dt><dd>{flg("Nguyễn Hoàng Thị Phương Thảo", "Điều phối viên ca đêm · Đội Sóng Thần", "sm", text="NP")}</dd>
</dl>
</div>"""

PROFILE_F = f"""<div class="prof">
<span data-hide="upload uploading">{fav("xxl", "image", status="on", attrs="data-cmp")}</span>
<span data-show="state:uploading">{fav("xxl", "loading", attrs="data-cmp")}</span>
<span data-show="state:upload">{fav("xxl", "upload", "NA", attrs="data-cmp")}</span>
<span class="muted" data-sx="sx6" data-hide="upload uploading">Chạm vào ảnh để đổi ảnh đại diện</span>
<span class="muted" data-sx="sx6" data-show="state:upload">Chưa có ảnh. Chạm biểu tượng máy ảnh để thêm</span>
<span class="muted" data-sx="sx6" data-show="state:uploading">Đang tải ảnh lên…</span></div>
<div class="mrow"><div class="tx2"><div class="s">Họ và tên</div><b data-hide="long">Nguyễn Văn An</b><b data-show="state:long">Nguyễn Hoàng Thị Phương Thảo</b></div></div>
<div class="mrow"><div class="tx2"><div class="s">Vai trò</div><b>Lái xe · Đội Sóng Thần</b></div>{fbd("Đang trực", "green", "pc", attrs="data-cmp")}</div>
<div class="mrow"><div class="tx2"><div class="s">Xe đang nhận</div><b>51C-123.45 · mooc 51R-045.67</b></div></div>"""

preview = {
    "version": 2, "pick": PICK,
    "changes": "Bản 29/10 theo tổ hợp chốt: Bản B (đúng cấu trúc Figma) · Badge bỏ X Close, chip lọc dùng Tag (D1 = A) · teal/tím/cam chỉ cho cột Loại ở dạng Badge Modern (D3 = A) · nhóm avatar: avatar sau đè avatar trước (D4 = A). "
               "Thêm màn Chi tiết lệnh (web) và Ảnh hồ sơ (app: Upload → Loading → Image). Bản 2: bỏ trạng thái Đang tải / Rỗng của màn (không phải trạng thái của component); trạng thái chỉ còn Có dữ liệu, Chữ dài và biến thể Content Upload / Loading của Avatar.",
    "blocks": [
        {"title": "Web", "platform": "web", "note": "Badge 5 kiểu × 8 màu × 3 cỡ + phần thêm · Avatar 5 nội dung × 6 cỡ · status · Company · Group · Add · Avatar label · chữ dài",
         "html": f'<div class="pv pvp" {_pa} data-platform="web" data-state="x">{PV_WEB}</div>'},
        {"title": "Mobile (app)", "platform": "mobile", "note": "Nhóm A — cùng số đo web: badge, avatar + status, avatar label, ảnh hồ sơ",
         "frames": [f'<div class="pv pvp" {_pa} data-platform="mobile" data-state="x">{h}</div>' for h in PV_MOB]},
    ],
}


VALUES = [
 # Badge
 {"part": "Badge", "prop": "height", "value": 22, "platform": "Web", "size": "SM", "sel": ".fb.sm"},
 {"part": "Badge", "prop": "height", "value": 24, "platform": "Web", "size": "MD", "sel": ".fb.md"},
 {"part": "Badge", "prop": "height", "value": 28, "platform": "Web", "size": "LG", "sel": ".fb.lg"},
 {"part": "Badge", "prop": "padding-left", "value": 6, "platform": "Web", "size": "SM", "sel": ".fb.sm", "cssProp": "padding-left"},
 {"part": "Badge", "prop": "padding-left", "value": 8, "platform": "Web", "size": "MD", "sel": ".fb.md", "cssProp": "padding-left"},
 {"part": "Badge", "prop": "padding-left", "value": 10, "platform": "Web", "size": "LG", "sel": ".fb.lg", "cssProp": "padding-left"},
 {"part": "Badge", "prop": "padding-right", "value": 10, "platform": "Web", "size": "SM", "sel": ".fb.pc.sm,.fb.po.sm,.fb.bc.sm,.fb.bo.sm,.fb.bm.sm", "cssProp": "padding-right"},
 {"part": "Badge", "prop": "padding-right", "value": 12, "platform": "Web", "size": "MD", "sel": ".fb.pc.md,.fb.po.md,.fb.bc.md,.fb.bo.md,.fb.bm.md", "cssProp": "padding-right"},
 {"part": "Badge", "prop": "padding-right", "value": 14, "platform": "Web", "size": "LG", "sel": ".fb.pc.lg,.fb.po.lg,.fb.bc.lg,.fb.bo.lg,.fb.bm.lg", "cssProp": "padding-right"},
 {"part": "Badge", "prop": "gap", "value": 4, "platform": "Web", "size": "SM", "sel": ".fb.sm", "cssProp": "gap"},
 {"part": "Badge", "prop": "gap", "value": 4, "platform": "Web", "size": "MD", "sel": ".fb.md", "cssProp": "gap"},
 {"part": "Badge", "prop": "gap", "value": 4, "platform": "Web", "size": "LG", "sel": ".fb.lg", "cssProp": "gap"},
 {"part": "Badge", "prop": "radius", "value": 6, "platform": "Web", "size": "MD", "sel": ".fb.bc.md,.fb.bo.md,.fb.bm.md", "cssProp": "border-radius"},
 {"part": "Badge", "prop": "radius", "value": 8, "platform": "Web", "size": "LG", "sel": ".fb.bc.lg,.fb.bo.lg,.fb.bm.lg", "cssProp": "border-radius"},
 {"part": "Badge · Label", "prop": "max-width", "value": 160, "platform": "Web", "sel": ".fb .flw"},
 {"part": "Badge · Dot", "prop": "size", "value": 6, "platform": "Web", "sel": ".fb .fdot", "cssProp": ["width", "height"]},
 {"part": "Badge · có Count", "prop": "padding-right", "value": 3, "platform": "Web", "size": "SM", "sel": ".fb.sm:has(.fcnt)", "cssProp": "padding-right"},
 {"part": "Badge · có Count", "prop": "padding-right", "value": 4, "platform": "Web", "size": "LG", "sel": ".fb.md:has(.fcnt),.fb.lg:has(.fcnt)", "cssProp": "padding-right"},
 {"part": "Badge · Count Only", "prop": "padding-left", "value": 4, "platform": "Web", "sel": ".fb .flw.fco", "cssProp": "padding-left"},
 {"part": "Badge · Dot", "prop": "margin-right", "value": 2, "platform": "Web", "sel": ".fb .fdw:not(.iw)", "cssProp": "margin-right"},
 {"part": "Badge · Icon", "prop": "size", "value": 14, "platform": "Web", "sel": ".fb .fi", "cssProp": ["width", "height"]},
 {"part": "Badge · Count", "prop": "padding-x", "value": 6, "platform": "Web", "sel": ".fb .fcnt", "cssProp": "padding", "tpl": "0 $"},
 # Avatar
 {"part": "Avatar", "prop": "size", "value": 24, "platform": "Web", "size": "XS", "sel": ".fa.xs", "cssProp": ["width", "height"]},
 {"part": "Avatar", "prop": "size", "value": 32, "platform": "Web", "size": "SM", "sel": ".fa.sm", "cssProp": ["width", "height"]},
 {"part": "Avatar · Initials", "prop": "font-size", "value": 14, "platform": "Web", "size": "MD", "sel": ".fa.md .fat"},
 {"part": "Avatar · Initials", "prop": "font-size", "value": 17, "platform": "Web", "size": "LG", "sel": ".fa.lg .fat"},
 {"part": "Avatar · Status", "prop": "size", "value": 10, "platform": "Web", "size": "MD", "sel": ".fa.md .fst>i", "cssProp": ["width", "height"]},
 {"part": "Avatar · Status ring", "prop": "padding", "value": 2, "platform": "Web", "sel": ".fa .fst"},
 {"part": "Avatar · Upload", "prop": "size", "value": 16, "platform": "Web", "size": "MD", "sel": ".fa.md .fup", "cssProp": ["width", "height"]},
 {"part": "Company avatar", "prop": "radius", "value": 6, "platform": "Web", "size": "MD", "sel": ".fa.co", "cssProp": "border-radius"},
 {"part": "Company avatar", "prop": "radius", "value": 16, "platform": "Web", "size": "XXL", "sel": ".fa.co.xxl", "cssProp": "border-radius"},
 {"part": "Avatar group · ring", "prop": "padding", "value": 2, "platform": "Web", "sel": ".fg .fgw"},
 {"part": "Avatar label", "prop": "gap", "value": 8, "platform": "Web", "sel": ".flg"},
 {"part": "Avatar label", "prop": "width", "value": 240, "platform": "Web", "sel": ".flg"},
 {"part": "Avatar label · Title", "prop": "font-size", "value": 14, "platform": "Web", "sel": ".flg b", "cssProp": "font", "tpl": "600 $/20px var(--font-body)"},
 {"part": "Avatar add button", "prop": "size", "value": 48, "platform": "Web", "sel": ".fadd", "cssProp": ["width", "height"], "interactive": True, "hitArea": 48},
]


REVIEWS = [
 {"id": "R1", "agent": "visual-reviewer", "severity": "Cao", "node": "6657:165736", "changesLook": True,
  "text": "<b>Badge Orange gần Yellow</b> trên nền nhạt — cam (chỉ cho phân loại) dễ đọc nhầm là cảnh báo. Anh đã chọn <b>Sửa</b>; phương án cụ thể chờ duyệt: xem chế độ <i>Sau khi sửa</i>.",
  "fix": "Chip cam: nền <b>orange-100</b> #FBEAD7 (đang orange-50 #FFF7ED), chữ <b>orange-800</b> #A03201 (đang orange-700 #C2410C) — ngả đỏ-cam, tách khỏi chip vàng (nền #FFF3DC, chữ #8A5300). Đổi token color/utility/orange/100, /fg (ảnh hưởng mọi chip cam).",
  "after": ".pv .fb.c-orange:not(.bm){background:var(--color-utility-orange-100)!important;color:var(--color-utility-orange-800)!important}.pv .fb.c-orange .fdot{background:var(--color-utility-orange-800)!important}", "screen": "list-web", "state": "default", "sel": ".fb.c-orange", "where": "Danh sách lệnh · Web, cột Loại hàng (Hàng nguy hiểm)"},
 {"id": "R2", "agent": "visual + accessibility", "severity": "Cao", "node": "6657:165851", "changesLook": True,
  "text": "<b>Chấm Online / Busy / Away chỉ khác màu</b> (WCAG 1.4.1, tỷ lệ giữa các màu 1,1–1,2); ở XS 6 / SM 8 khó phân biệt, Offline XS gần như chấm đặc. Spec đã thêm chữ trạng thái + aria-label + không bật Status ở XS.",
  "fix": "Thêm hình trong chấm (tích / gạch / đồng hồ) từ MD trở lên — hoặc giữ như hiện tại, dựa vào chữ thay thế đã ghi trong spec."},
 {"id": "R3", "agent": "uxui-reviewer", "severity": "Cao", "node": "6657:165736", "changesLook": True,
  "text": "<b>Count Only</b> (số đứng thẳng trên nền badge) đang <b>12/18 · 600</b> như nhãn; ô đếm (Has Count) đã đổi sang <b>type/caption 12/16 · 400</b>.",
  "fix": "Chọn: giữ Count Only đậm (nó đứng thay nhãn) — hoặc đổi sang caption 400 cho đồng bộ với ô đếm."},
 {"id": "R4", "agent": "uxui-reviewer", "severity": "Trung", "node": "6658:191370", "changesLook": True,
  "text": "<b>Icon plus của nút thêm</b> đang là biến thể icon Size=20 kéo giãn lên 24; nét 1,67 chưa theo DEC-300 (nét 2).",
  "fix": "Đổi sang biến thể icon Size=24 (nét đúng thang) — nét có thể dày lên chút."},
 {"id": "R5", "agent": "visual-reviewer", "severity": "Trung", "node": "6658:191370", "changesLook": True,
  "text": "<b>Nút thêm: Default và Hover gần như giống nhau</b>, viền nét đứt nhạt — nhấn yếu.",
  "fix": "Hover đổi nền rõ hơn (color/bg/primary_hover) hoặc viền đậm một bậc ở Default."},
 {"id": "R6", "agent": "visual + accessibility", "severity": "Trung", "node": "6657:166325", "changesLook": True,
  "text": "<b>Ô \"+n\" của Avatar group</b> chữ xám trên nền xám nhạt (4,54 : 1, sát ngưỡng) — nhìn như disabled.",
  "fix": "Chữ ô +n đổi sang color/text/tertiary_strong (dư biên tương phản)."},
 {"id": "R7", "agent": "visual-reviewer", "severity": "Trung", "node": "6657:165736", "changesLook": True,
  "text": "<b>Viền Badge Outline / Modern</b> (color/border/primary) mảnh, ranh giới mờ khi badge nằm trên nền xám của bảng.",
  "fix": "Tăng một bậc xám viền — hoặc giữ (viền là trang trí, chữ mang nghĩa)."},
 {"id": "R8", "agent": "visual + uxui", "severity": "Trung", "node": "6657:166192", "changesLook": True,
  "text": "<b>Upload / Loading ở XS–MD</b>: nút máy ảnh 14–16 che gần hết chữ \"NA\", spinner rất nhỏ; vùng chạm dưới 24 (WCAG 2.5.8).",
  "fix": "Bỏ biến thể Upload / Loading ở XS, SM, MD (spec đã ghi Upload chỉ dùng từ LG) — hoặc giữ cho đủ ma trận."},
 {"id": "R9", "agent": "visual-reviewer", "severity": "Trung", "node": "6657:167713", "changesLook": True,
  "text": "<b>Company avatar dạng Image (placeholder)</b> viền và icon rất nhạt, ở XS/SM gần như biến mất.",
  "fix": "Tăng đậm icon placeholder (color/fg/quaternary) và viền một bậc."},
 {"id": "R10", "agent": "uxui-reviewer", "severity": "Trung", "node": "6657:167394", "changesLook": False,
  "text": "<b>Avatar label thiếu thuộc tính</b>: không có boolean Has Subtitle, không swap avatar (Image / Initials / Company); Avatar group cũng không swap từng avatar.",
  "fix": "Thêm boolean Has Subtitle + instance swap cho avatar trong Avatar label và Avatar group (không đổi hình)."},
 {"id": "R11", "agent": "uxui-reviewer", "severity": "Thấp", "node": "6653:264", "changesLook": True,
  "text": "<b>type/caption trên app là 13/18</b> (web 12/16) — số đếm và dòng phụ Avatar label trên app sẽ khác web, trái nhóm A \"cùng số đo\".",
  "fix": "Thêm token cố định cho số đếm / dòng phụ 12/16 — hoặc chấp nhận app 13/18 và ghi ngoại lệ trong spec."},
 {"id": "R12", "agent": "uxui-reviewer", "severity": "Thấp", "node": "6658:191370", "changesLook": False,
  "text": "<b>Nút thêm chưa có trạng thái đang xử lý</b> (thêm người gọi máy chủ).",
  "fix": "Thêm State=Loading (spinner thay dấu +) — hoặc để nơi dùng hiện thông báo, không cần state."},
 {"id": "R13", "agent": "accessibility (review 30/10)", "severity": "Trung", "node": "6657:165736", "changesLook": False,
  "text": "<b>Spec tự mâu thuẫn về focus</b> (WCAG 2.4.7): mục Trạng thái ghi badge không có hover / focus, nhưng mục Trợ năng cho badge bị cắt \"…\" mang <code>tabindex=\"0\"</code> để mở tooltip — đã nhận focus thì phải có vòng focus, set chưa có.",
  "fix": "<b>Đề xuất (Sửa):</b> bỏ <code>tabindex</code> trên badge; tooltip toàn văn mở khi focus dòng / ô chứa badge (spec đã có). <b>Bỏ qua</b> = giữ tabindex và phải thêm trạng thái Focus (đổi hình)."},
 {"id": "R14", "agent": "accessibility (review 30/10)", "severity": "Trung", "node": "6657:165736", "changesLook": True,
  "text": "<b>Cỡ chữ hệ thống lớn (Dynamic Type, zoom 200%)</b> (WCAG 1.4.4): badge cao cố định 22/24/28, ô đếm 16/20 và chữ số 12/16 cố định — khi người dùng tăng cỡ chữ, số không lớn theo, nhãn bị cắt nhiều hơn mà app không có tooltip.",
  "fix": "Ghi trong spec: chiều cao là <b>tối thiểu</b> (min-height), chữ nhãn và số co theo cỡ chữ hệ thống, chặn trên ở mức AX3. Cỡ mặc định không đổi."},
 {"id": "R15", "agent": "visual-reviewer (review 30/10)", "severity": "Trung", "node": "6657:165736", "changesLook": False,
  "text": "<b>Type Dot đủ 8 màu</b> nhưng ở chấm 6×6, Red / Orange và Green / Teal gần như không phân biệt; DEC-303 đã giới hạn Teal / tím / cam cho phân loại ở Modern.",
  "fix": "Ghi luật: Type Dot chỉ dùng 5 màu trạng thái (Gray · Blue · Green · Yellow · Red); Teal / Purple / Orange chỉ ở Badge Modern. Biến thể vẫn giữ trên Figma."},
 {"id": "R16", "agent": "visual-reviewer (review 30/10)", "severity": "Thấp", "node": "6657:165736", "changesLook": True,
  "text": "<b>Count Only nền nhạt, số 400</b> trông yếu khi dùng làm chỉ báo thông báo (mắt dễ bỏ qua).",
  "fix": "Thêm kiểu Count Only nền đặc (nền <code>color/utility/red/700</code>, chữ trắng) cho chỉ báo thông báo — <b>Bỏ qua</b> nếu Count Only chỉ dùng cho số lượng thường."},
 {"id": "R17", "agent": "visual-reviewer (review 30/10)", "severity": "Thấp", "node": "6657:165736", "changesLook": True,
  "text": "<b>Badge Modern nặng hơn Pill Color</b> khi cạnh nhau (chữ 600 đen trên trắng + viền) — nhãn phân loại có thể lấn nhãn trạng thái trong cùng dòng bảng.",
  "fix": "Thử chữ Modern <code>color/text/tertiary</code> — <b>Bỏ qua</b> = giữ, chỉ ghi luật cột Trạng thái đứng trước cột Loại.", "after": ".pv .fb.bm[class]{color:var(--color-text-tertiary)!important}", "screen": "list-web", "state": "default", "sel": ".fb.bm", "where": "Danh sách lệnh · Web, cột Loại hàng"}
]
# Ảnh Trước / Sau cho từng điểm review (user 30/10: xem trước và sau khi sửa để đánh giá)
import base64 as _b64
for _r in REVIEWS:
    _f = Path(__file__).parent / "assets" / "review" / f"{_r['id']}.jpg"
    if _f.exists():
        _r["img"] = "data:image/jpeg;base64," + _b64.b64encode(_f.read_bytes()).decode()



def ver(a, b):
    """V = a: bản hiện tại trên artifact · b: theo Figma."""
    return f'<div data-show="V:a">{a}</div><div data-show="V:b">{b}</div>'


page = {
    "component": "Badge · Avatar",
    "slug": "badge-avatar",
    "title": "Badge · Avatar Review",
    "subtitle": "Base component · Badge, Avatar (+ Company, Group, Label group, Add) · nhóm A (dùng chung web và app)",
    "round": "review",
    "reviews": REVIEWS,
    "figma": {"url": "https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=6657-165741", "label": "Section Badges 6657:165305 · Avatars 6657:165741 trên DS · Base components"},
    "brief": True,
    "preview": preview,
    "refs": {
        "untitled": {
            "summary": "Badge 3 kiểu <mark>pill-color · color · modern</mark>, 3 cỡ, có dot / icon / nút X; Pill và Badge Color có <mark>viền màu nhạt</mark> (ring-1). Avatar 7 cỡ 16–64, initials nền xám, chấm Online xanh / Offline xám đặc, group: avatar sau đè avatar trước.",
            "source": "design/_ref/untitled-ui/react/components/base/badges/badges.tsx · avatar/avatar.tsx · avatar-label-group.tsx",
        },
        "astryx": {
            "summary": "Chip trạng thái bo tròn hẳn, nền nhạt, không viền (Status Chip); avatar spec v2 cũ 5 cỡ 24·36·48·64·88, chấm Offline rỗng, nhóm: avatar đầu nằm trên (DEC-242).",
            "source": "design-system/components/l1/status-chip.md · l1/avatar.md · l1/avatar-group.md",
        },
        "usage": [
            "Mọi bảng danh sách: cột Trạng thái, Loại (Badge)",
            "cross-process-flow · search-process, create-next-step (Badge)",
            "Header web: nút tài khoản chỉ avatar (DEC-290) · app: hồ sơ lái xe, danh sách đội",
        ],
        "platform": "Nhóm A — một bộ, cùng số đo web và app. Đã chốt biến thể 26/10: Badge Type 3 × Color 8 × Icon 5 × Size 3; Avatar Content 4 × Size 6 × Status 4 + Group, Label group, Add, Company. Brainstorm gọn: 6 điểm còn mở từ lượt duyệt Figma 1.",
    },
    "css": CSS,
    "cssScreen": BASE_CSS + CSS_A,
    "values": VALUES,
    "cssIgnore": [{"sel": ".fb", "props": ["outline-offset"], "why": "Viền 1px của Pill/Badge Outline và Modern vẽ bằng outline lùi vào trong 1px — tương đương stroke Inside trên Figma, không phải khoảng cách."}],
    "states": [
        {"key": "default", "label": "Có dữ liệu"},
        {"key": "long", "label": "Chữ dài"},
        {"key": "upload", "label": "Avatar · Upload (chưa có ảnh)"},
        {"key": "uploading", "label": "Avatar · Loading (đang tải ảnh)"},
    ],
    "ideas": [],
    "decisions": [
        {"id": "V", "title": "Phiên bản để duyệt",
         "why": "<mark>Bản A</mark> = bản đang đăng trên artifact (Badge 3 kiểu, Avatar 4 nội dung, thang cỡ chọn ở D6). "
                "<mark>Bản B</mark> = dựng lại theo <b>cấu trúc Figma hiện tại</b>: Badge 5 kiểu (thêm Pill Outline, Badge Outline) + công tắc Dot / Icon / Count / Count Only / X; "
                "Avatar 5 nội dung (thêm Loading), cỡ 24·32·36·48·64·88, Status là instance lồng, Company 3 nội dung, Group XS/MD/LG, Label group SM/MD/LG, Add button 4 trạng thái.",
         "source": "Figma Section Badges 6657:165305 · Avatars 6657:165741 (đo 29/10)",
         "options": [
             {"label": "Bản A · hiện tại", "desc": "Giữ nguyên bản trên artifact, D2/D5/D6 còn mở.",
              "preview": mini({"V": "a"}, bd("Đang chạy", "blue", "pill", icon="dot") + bd("Hàng lạnh", "teal", "badge") + av("md", "image", status="on", i=0) + av("md", "upload"))},
             {"label": "Bản B · theo Figma", "desc": "Theo đúng component đang có trên Figma; D2/D5/D6 lấy theo Figma.", "rec": True,
              "preview": mini({"V": "b"}, fbd("Đang chạy", "blue", "pc") + fbd("Hàng lạnh", "teal", "bo") + fav("md", "image", status="on", i=0) + fav("md", "upload"))},
         ]},
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
        {"id": "rec", "label": "Đề xuất", "pick": {"V": "a", "D1": "a", "D2": "b", "D3": "a", "D4": "a", "D5": "a", "D6": "a"}},
        {"id": "untitled", "label": "Theo Untitled", "pick": {"V": "a", "D1": "a", "D2": "a", "D3": "a", "D4": "a", "D5": "b", "D6": "a"}},
        {"id": "figma", "label": "Bản B · Figma", "pick": {"V": "b", "D1": "b", "D2": "a", "D3": "a", "D4": "a", "D5": "a", "D6": "b"}},
        {"id": "astryx", "label": "Astryx hiện tại", "pick": {"V": "a", "D1": "b", "D2": "b", "D3": "b", "D4": "b", "D5": "a", "D6": "b"}},
    ],
    "screens": [
        {"id": "list-web", "name": "Danh sách lệnh", "device": "web", "width": 1280, "nav": "Lệnh vận tải", "title": "Lệnh vận tải",
         "note": "Badge ở cột Trạng thái (Pill) và Loại (Badge Modern); Avatar label ở cột Lái xe; Avatar group ở thanh ca trực; bộ lọc dùng Tag. Bảng chọn › Hiển thị đổi Chữ dài.", "html": LIST_F},
        {"id": "detail-web", "name": "Chi tiết lệnh", "device": "web", "width": 1280, "nav": "Lệnh vận tải", "title": "Chi tiết lệnh",
         "note": "Badge LG ở đầu trang; Company avatar cạnh tên khách; Avatar label lái xe (MD, có status) và điều phối (SM); Avatar group + nút thêm người theo dõi.", "html": DETAIL_F},
        {"id": "team-app", "name": "Đội lái xe", "device": "mobile", "nav": "Tài khoản", "title": "Đội của tôi",
         "note": "Avatar có chấm trạng thái + Badge trạng thái chuyến.", "html": APP_F},
        {"id": "profile-app", "name": "Ảnh hồ sơ", "device": "mobile", "nav": "Tài khoản", "title": "Hồ sơ", "back": True,
         "note": "Đổi ảnh đại diện theo biến thể Content của Avatar: Upload (chưa có ảnh) → Loading (đang tải) → Image (Có dữ liệu). Chữ dài = tên dài.", "html": PROFILE_F},
    ],
}

write(OUT, page)
