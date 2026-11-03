#!/usr/bin/env python3
import sys
"""Sinh page.json cho Field Upload (vòng 1 Brainstorm) — nháp, chưa ghi repo.
Chạy: python3 design-system/components/_work/field-upload/build.py && python3 _scripts/ds-component-page.py field-upload
Đầu vào đã chốt: thẻ File upload trên trang Chốt biến thể Application (artifact L3pzcVoU11rCka42c9tHoS, db variants/fileupload 27/10).
"""
import json
from pathlib import Path

OUT = Path(__file__).parent / "page.json"

# ---------- icon (Lucide, nét 2) ----------
P = {
    "cloud": '<path d="M7 18a5 5 0 0 1-.5-10A6 6 0 0 1 18 9a4 4 0 0 1-1 9"/><path d="M12 12v8M9 15l3-3 3 3"/>',
    "upload": '<path d="M12 15V4M7 9l5-5 5 5"/><path d="M4 15v4a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-4"/>',
    "trash": '<path d="M3 6h18M8 6V4h8v2M6 6l1 14h10l1-14"/>',
    "x": '<path d="M6 6l12 12M18 6L6 18"/>',
    "ok": '<circle cx="12" cy="12" r="9"/><path d="M8 12l3 3 5-6"/>',
    "err": '<circle cx="12" cy="12" r="9"/><path d="M15 9l-6 6M9 9l6 6"/>',
    "cam": '<path d="M4 8h3l2-3h6l2 3h3v11H4z"/><circle cx="12" cy="13" r="3.5"/>',
    "img": '<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10" r="2"/><path d="M21 16l-5-5-9 9"/>',
    "folder": '<path d="M3 6h6l2 2h10v11H3z"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "retry": '<path d="M20 11a8 8 0 1 0-2.3 5.7"/><path d="M20 5v6h-6"/>',
    "dl": '<path d="M12 4v11M7 10l5 5 5-5"/><path d="M4 19h16"/>',
    "pin": '<path d="M12 21s7-6 7-11a7 7 0 0 0-14 0c0 5 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/>',
}
def ic(k, s=20):
    return (f'<svg class="i" viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" '
            f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{P[k]}</svg>')

# ---------- dữ liệu mẫu cố định ----------
F_PDF = ("HD-0001234-Petrolimex.pdf", "1,2 MB", "PDF")
F_XML = ("HD-0001234-Petrolimex.xml", "18 KB", "XML")
F_JPG = ("bien-ban-giao-hang-LVT-2026-0412.jpg", "2,4 MB", "JPG")
F_BIG = ("anh-su-co-container-TGHU8812345.jpg", "14,8 MB", "JPG")
F_LONG = ("Hoa-don-GTGT-0001234-Cong-ty-TNHH-Van-tai-Delta-Logistics-chi-nhanh-Cat-Lai-thang-10-2026-ban-chinh.pdf", "3,1 MB", "PDF")
HINT = "PDF, XML, JPG hoặc PNG, tối đa 10 MB"
ERR_BIG = "Vượt 10 MB. Chọn file nhỏ hơn hoặc chụp lại."
ERR_REQ = "Cần tải ít nhất một hoá đơn."

# ---------- phần tử ----------
# File type icon của DS (DS · Foundations › Misc icons, set 6657:165918), cỡ MD 40: tờ giấy gập góc + nhãn đuôi.
# Type có sẵn: PDF · DOC · XLS · CSV · IMG · ZIP · VID · Other. JPG/PNG → IMG; XML chưa có loại riêng → Other.
FT = {"PDF": ("PDF", "var(--color-file-type-pdf)", 30), "DOC": ("DOC", "var(--color-file-type-doc)", 33), "XLS": ("XLS", "var(--color-file-type-xls)", 29), "CSV": ("CSV", "var(--color-file-type-csv)", 32),
      "IMG": ("IMG", "var(--color-file-type-img)", 30), "ZIP": ("ZIP", "var(--color-file-type-zip)", 25), "VID": ("VID", "var(--color-file-type-vid)", 28)}  # DEC-335 ms02, ms03
FT_ALIAS = {"JPG": "IMG", "PNG": "IMG", "XML": "Other"}
def ftype(kind):
    t = FT_ALIAS.get(kind, kind)
    badge = ""
    if t in FT:
        lab, col, w = FT[t]
        badge = (f'<rect x="2" y="17" width="{w}" height="18" rx="2" fill="{col}"/>'
                 f'<text x="{2 + w / 2}" y="30" text-anchor="middle" font-family="Inter" font-size="12" font-weight="600" fill="#fff">{lab}</text>')
    return (f'<svg class="ft" viewBox="0 0 40 40" width="40" height="40" role="img" aria-label="Tệp {kind}">'
            f'<path d="M8 1H25L33 9V39H8Z" fill="var(--color-bg-primary)" stroke="var(--color-border-primary)" stroke-width="1.5"/>'
            f'<path d="M25 1V9H33" fill="none" stroke="var(--color-border-primary)" stroke-width="1.5"/>{badge}</svg>')

def frow(f, status="done", pct=100, msg=None):
    """Dòng file: status = uploading | done | error. D4 a = thanh tiến độ, b = nền tiến độ. D5 a/b = vị trí nút."""
    name, size, kind = f
    if status == "done":
        st = f'<span class="st ok">{ic("ok", 14)}Xong</span>'
    elif status == "error":
        st = f'<span class="st er">{ic("err", 14)}{msg or "Tải lỗi"}</span>'
    else:
        st = f'<span class="st up">{ic("cloud", 14)}Đang tải {pct}%</span>'
    bar = f'<div class="bar" data-show="D4:a"><i style="width:{pct}%"></i></div>' if status == "uploading" else ""
    fill = f'<i class="fill" data-show="D4:b" style="width:{pct}%"></i>' if status == "uploading" else ""
    retry_a = '<button class="lkr" data-show="D5:a">Thử lại</button>' if status == "error" else ""
    retry_b = f'<button class="bt sm" data-show="D5:b">{ic("retry", 14)}Thử lại</button>' if status == "error" else ""
    del_a = f'<button class="ib del" data-show="D5:a" aria-label="Xoá file">{ic("trash", 16)}</button>'
    del_b = f'<button class="ib" data-show="D5:b" aria-label="Xoá file">{ic("x", 16)}</button>'
    return (f'<div class="fr {status}">{fill}{ftype(kind)}<div class="fm"><div class="fn">{name}</div>'
            f'<div class="fs"><span>{size}</span><span class="sep"></span>{st}</div>{bar}{retry_a}</div>'
            f'<div class="fa">{retry_b}{del_b}</div>{del_a}</div>')

def zone(state="", compact_btn="Chọn file"):
    """Vùng chọn file web — D2 a vùng thả đủ, b vùng thả gọn 1 hàng, c chỉ nút. state: '' | hover | disabled | error."""
    cls = f"dz {state}".strip()
    dis = " disabled" if state == "disabled" else ""
    hover_txt = "Thả file vào đây" if state == "hover" else None
    full = (f'<div class="{cls} dz-a" data-show="D2:a" tabindex="0" role="button"><span class="fi">{ic("cloud")}</span>'
            f'<div class="dz-t">{f"<b>{hover_txt}</b>" if hover_txt else "<b class=lk>Bấm để chọn file</b> hoặc kéo thả vào đây"}</div>'
            f'<div class="dz-h">{HINT}</div></div>')
    comp = (f'<div class="{cls} dz-b" data-show="D2:b"><span class="fi sm">{ic("cloud", 18)}</span>'
            f'<div class="dz-m"><div class="dz-t">{f"<b>{hover_txt}</b>" if hover_txt else "<b>Kéo thả file vào đây</b>"}</div>'
            f'<div class="dz-h">{HINT}</div></div><button class="bt"{dis}>{ic("upload", 16)}{compact_btn}</button></div>')
    btn = (f'<div class="dz-c {state}" data-show="D2:c"><button class="bt"{dis}>{ic("upload", 16)}Tải file lên</button>'
           f'<span class="dz-h">{HINT}</span></div>')
    return full + comp + btn

def field(label, files=(), req=True, state="", err=None, single=False, hint=None):
    """Field web: nhãn + vùng chọn + danh sách. single=True: D3 b ẩn vùng chọn khi đã có file."""
    lab = f'<div class="lb">{label}{"<span class=req>*</span>" if req else ""}</div>'
    z = zone(state)
    if single and files:
        z = f'<div data-show="D3:a">{z}</div>'
    lst = f'<div class="fl">{"".join(files)}</div>' if files else ""
    foot = f'<div class="fe">{ic("err", 14)}{err}</div>' if err else (f'<div class="hn">{hint}</div>' if hint else "")
    return f'<div class="fu" data-cmp>{lab}{z}{lst}{foot}</div>'

# ---------- app ----------
def afield(label, files=(), req=True, state="", err=None, grid=False, sheet=False):
    """Field app: D1 nhãn trên / trong khung · D6 nguồn chọn · D7 lưới ảnh / dòng."""
    dis = " disabled" if state == "disabled" else ""
    lab_out = f'<div class="lb" data-show="D1:a">{label}{"<span class=req>*</span>" if req else ""}</div>'
    lab_in = f'<div class="lbi">{label}{"<span class=req>*</span>" if req else ""}</div>'
    tap = (f'<div class="az {state}" data-show="D6:a"><span class="fi">{ic("cam", 24)}</span><div class="az-m">'
           f'<span data-show="D1:b">{lab_in}</span><div class="dz-t"><b>Chụp ảnh hoặc chọn tệp</b></div>'
           f'<div class="dz-h">Ảnh, PDF tối đa 10 MB</div></div></div>')
    two = (f'<div class="az2 {state}" data-show="D6:b"><span data-show="D1:b" style="grid-column:1/-1">{lab_in}</span>'
           f'<button class="bt big"{dis}>{ic("cam", 18)}Chụp ảnh</button><button class="bt big"{dis}>{ic("folder", 18)}Chọn tệp</button></div>')
    if grid:
        tiles = "".join(files)
        add = f'<button class="tl add" data-show="D6:c" aria-label="Thêm ảnh">{ic("plus", 22)}<span>Thêm ảnh</span></button>'
        body = f'<div class="gr" data-show="D7:a">{tiles}{add}</div>'
        rows = f'<div class="fl" data-show="D7:b">{"".join(rowify(files))}</div>'
        cgrid = "" if files else ""
        lst = body + rows + cgrid
    else:
        lst = f'<div class="fl">{"".join(files)}</div>' if files else ""
        add = f'<div class="gr" data-show="D6:c"><button class="tl add" aria-label="Thêm">{ic("plus", 22)}<span>Thêm</span></button></div>'
        lst = lst + add
    foot = f'<div class="fe">{ic("err", 14)}{err}</div>' if err else ""
    sh = SHEET if sheet else ""
    return f'<div class="fu m" data-cmp>{lab_out}{tap}{two}{lst}{foot}{sh}</div>'

def tile(n, status="done", pct=100, label=None):
    shade = ["#C9D4E0", "#D8CFC2", "#C4D1C8", "#D3C9D8"][n % 4]
    over = ""
    if status == "uploading":
        over = f'<span class="tov"><i class="ring" style="--p:{pct}"></i>{pct}%</span>'
    elif status == "error":
        over = f'<span class="tov er">{ic("retry", 18)}Thử lại</span>'
    cap = f'<span class="tcap">{label}</span>' if label else ""
    return (f'<div class="tl {status}" data-meta="{label or ""}"><span class="ph sh{n % 4}">{ic("img", 22)}</span>{over}{cap}'
            f'<button class="tx" aria-label="Xoá ảnh">{ic("x", 12)}</button></div>')

def rowify(tiles_html):
    # bản "dòng có ảnh nhỏ" cho D7 b — dựng lại từ nhãn của tile
    out = []
    for i, t in enumerate(tiles_html):
        st = "uploading" if "tov\"" in t and "%" in t else ("error" if "tov er" in t else "done")
        lab = t.split('data-meta="')[1].split('"')[0] or f"Ảnh {i + 1}"
        out.append(frow((f"{lab}.jpg", "2,1 MB", "JPG"), st, 48 if st == "uploading" else 100,
                        "Mất kết nối" if st == "error" else None).replace(ftype("JPG"),
                        f'<span class="th sh{i % 4}">{ic("img", 16)}</span>'))
    return out

SHEET = (f'<div class="scr" data-show="D6:a"></div><div class="sht" data-show="D6:a"><i class="hd"></i><div class="sh-t">Thêm ảnh hoá đơn</div>'
         f'<div class="sh-i">{ic("cam")}Chụp ảnh</div><div class="sh-i">{ic("img")}Chọn từ thư viện</div><div class="sh-i">{ic("folder")}Chọn tệp (PDF)</div></div>')

CSS = r"""
.pv{position:relative;
 
 color:var(--color-text-primary);font:14px/20px Inter,system-ui,sans-serif}
.pv[data-theme=dark]{
 }
.i{flex:none;display:block}
button{font:inherit;color:inherit}
.bt{height:32px;padding:0 12px;border:1px solid var(--color-border-primary);border-radius:8px;background:var(--color-bg-primary);display:inline-flex;align-items:center;gap:6px;font:600 13px/18px Inter;white-space:nowrap;cursor:pointer}
.bt.sm{height:28px;padding:0 8px;font-size:12.5px}.bt.big{height:48px;justify-content:center;border-radius:var(--radius-control);font-size:14px}
.pv .md-f .bt.pri.pri{background:var(--color-action-primary)!important;color:var(--color-text-inverse)!important;border-color:var(--color-action-primary)!important}
.bt[disabled]{opacity:.5;cursor:not-allowed}
.ib{width:32px;height:32px;border:0;background:none;border-radius:8px;display:inline-flex;align-items:center;justify-content:center;color:var(--color-text-tertiary);cursor:pointer;flex:none}
/* ---- field ---- */
.fu{display:flex;flex-direction:column;gap:6px;min-width:0;position:relative}
.lb{font:500 14px/20px Inter;color:var(--color-text-secondary);display:flex;gap:4px}
.lbi{font:500 12px/16px Inter;color:var(--color-text-tertiary);display:flex;gap:4px;margin-bottom:2px}
.req{color:var(--color-text-error-primary)}
.hn{font-size:12.5px;line-height:18px;color:var(--color-text-tertiary)}
.fe{font-size:12.5px;line-height:18px;color:var(--color-text-error-primary);display:flex;gap:6px;align-items:center}
/* vùng thả */
.dz{border:1px solid var(--color-border-input);border-radius:12px;background:var(--color-bg-primary);cursor:pointer}
.pv[data-D8=b] .dz,.pv[data-D8=b] .az{border-style:dashed;border-color:var(--color-border-input)}
.dz-a{padding:16px 24px;display:flex;flex-direction:column;align-items:center;gap:4px;text-align:center}
.dz-b{padding:12px 12px 12px 14px;display:flex;align-items:center;gap:12px;flex-wrap:wrap}
.dz-m{flex:1;min-width:150px}
.dz-c{display:flex;align-items:center;gap:12px;flex-wrap:wrap}
.dz-t{font-size:13.5px;line-height:20px;color:var(--color-text-tertiary)}.dz-t b{color:var(--color-text-primary);font-weight:600}.dz-t .lk{text-decoration:underline;text-underline-offset:2px}
.dz-h{font-size:12px;line-height:18px;color:var(--color-text-tertiary)}
.fi{width:40px;height:40px;border-radius:10px;border:1px solid var(--color-border-secondary);display:inline-flex;align-items:center;justify-content:center;color:var(--color-text-secondary);background:var(--color-bg-primary);flex:none;margin-bottom:8px}
.dz-b .fi,.fi.sm{width:36px;height:36px;margin:0}
.dz.hover{border:2px solid var(--color-focus-ring);background:var(--color-bg-primary_hover)}
.pv[data-D8=b] .dz.hover{border-style:dashed;border-color:var(--color-focus-ring)}
.dz.hover .fi{color:var(--color-text-primary)}
.dz.disabled,.az.disabled{background:var(--color-bg-disabled);cursor:not-allowed;opacity:.6}
.dz.error,.az.error,.az2.error .bt{border-color:var(--color-border-error)}
.dz-c.disabled .bt{opacity:.5}
/* dòng file */
.fl{display:flex;flex-direction:column;gap:8px}
.fr{position:relative;display:flex;gap:12px;align-items:flex-start;padding:12px 8px 12px 14px;border:1px solid var(--color-border-secondary);border-radius:12px;background:var(--color-bg-primary);overflow:hidden;min-width:0}
.fr.error{border-color:var(--color-border-error)}
.fr .fill{position:absolute;left:0;top:0;bottom:0;background:var(--color-bg-quaternary);z-index:0}
.fr>*{position:relative}
.ft{flex:none;display:block}
.th{width:40px;height:40px;border-radius:8px;display:flex;align-items:center;justify-content:center;color:var(--color-text-tertiary);flex:none}
.fm{flex:1;min-width:0}
.fn{font:500 13.5px/20px Inter;color:var(--color-text-primary);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.fs{display:flex;align-items:center;gap:8px;font-size:12.5px;line-height:18px;color:var(--color-text-tertiary);margin-top:1px;flex-wrap:wrap}
.sep{width:1px;height:12px;background:var(--color-border-primary)}
.st{display:inline-flex;align-items:center;gap:4px;font-weight:500}.st.ok{color:var(--color-text-success-primary)}.st.er{color:var(--color-text-error-primary)}
.bar{height:6px;border-radius:99px;background:var(--color-bg-quaternary);margin-top:8px;overflow:hidden}.bar i{display:block;height:100%;background:var(--color-accent-solid);border-radius:99px}
.lkr{border:0;background:none;padding:0;margin-top:6px;font:600 13px/18px Inter;color:var(--color-text-error-primary);cursor:pointer}
.fa{display:flex;gap:4px;align-items:center;align-self:center}
.del{align-self:flex-start;margin-top:-6px;margin-right:-2px}
/* ---- app ---- */
.fu.m .lb{font-size:13px}
.az{border:1px solid var(--color-border-input);border-radius:var(--radius-card);padding:14px;display:flex;gap:12px;align-items:center;background:var(--color-bg-primary)}
.az .fi{margin:0;border-radius:50%;width:48px;height:48px;background:var(--color-bg-tertiary);border:0}
.az-m{flex:1;min-width:0}
.az2{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.gr{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
.tl{position:relative;aspect-ratio:1;border-radius:var(--radius-inner);overflow:hidden;border:1px solid var(--color-border-secondary)}
.tl .ph{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;color:var(--color-fg-tertiary)}
.tl.add{border:1px dashed var(--color-border-input);background:var(--color-bg-primary);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;font:500 11.5px Inter;color:var(--color-text-secondary);cursor:pointer}
.tl.error{border:2px solid var(--color-border-error)}
.tov{position:absolute;inset:0;background:var(--color-bg-overlay_solid);color:var(--color-text-white);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;font:600 12px Inter}
.tov.er{background:var(--color-bg-error-overlay)}
.ring{width:24px;height:24px;border-radius:50%;background:conic-gradient(var(--color-fg-white) calc(var(--p)*1%),var(--color-bg-overlay_solid) 0)}
.tcap{position:absolute;left:6px;bottom:6px;right:6px;font:600 10.5px/14px Inter;color:var(--color-text-white);background:var(--color-bg-overlay_solid);padding:0 4px;border-radius:4px;width:max-content;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.tx{position:absolute;top:5px;right:5px;width:22px;height:22px;border-radius:50%;border:0;background:var(--color-bg-overlay_solid);color:var(--color-text-white);display:flex;align-items:center;justify-content:center}
.scr{position:absolute;inset:0;background:var(--color-bg-overlay);backdrop-filter:blur(var(--backdrop-blur-lg));z-index:8;border-radius:inherit}
.sht{position:absolute;left:0;right:0;bottom:0;z-index:9;background:var(--color-bg-primary_alt);border-radius:var(--radius-overlay) var(--radius-overlay) 0 0;padding:8px 16px 24px;display:flex;flex-direction:column}
.sht .hd{width:36px;height:4px;border-radius:2px;background:var(--color-bg-quaternary);align-self:center;margin-bottom:12px}
.sh-t{font:600 17px/24px Inter;margin-bottom:6px}
.sh-i{height:52px;display:flex;align-items:center;gap:12px;border-bottom:1px solid var(--color-border-secondary);font:500 15px Inter}
/* ---- màn ---- */
.pad{padding:16px 24px 24px;display:flex;flex-direction:column;gap:16px}.mpad{padding:12px 16px 96px;display:flex;flex-direction:column;gap:16px}
table{width:100%;border-collapse:collapse}td,th{padding:11px 16px;border-bottom:1px solid var(--color-border-secondary);text-align:left;font-size:13px}th{color:var(--color-text-tertiary);font-weight:500;background:var(--color-bg-secondary)}
.tb{border:1px solid var(--color-border-secondary);border-radius:12px;overflow:hidden}
.chip{display:inline-block;font:500 12px/18px Inter;padding:2px 8px;border-radius:999px;background:var(--color-utility-neutral-100)}
.mw{position:absolute;inset:0;background:var(--color-bg-overlay);backdrop-filter:blur(var(--backdrop-blur-lg));display:flex;align-items:flex-start;justify-content:center;padding-top:56px;z-index:6}
.md{width:560px;background:var(--color-bg-primary_alt);border-radius:var(--radius-overlay);border:1px solid var(--shadow-xl-border);box-shadow:var(--shadow-xl);display:flex;flex-direction:column}
.md-h{padding:20px 24px 8px;display:flex;gap:12px;align-items:flex-start}.md-h b{font:600 18px/28px Inter;display:block}.md-h span{color:var(--color-text-tertiary);font-size:13.5px}
.md-b{padding:12px 24px 8px;display:flex;flex-direction:column;gap:16px}
.md-f{padding:16px 24px 20px;display:flex;justify-content:flex-end;gap:8px}
.inp{height:32px;border:1px solid var(--color-border-input);border-radius:8px;padding:0 10px;display:flex;align-items:center;color:var(--color-text-tertiary);font-size:13.5px}
.ta{height:64px;align-items:flex-start;padding-top:6px}
.card{border:1px solid var(--color-border-secondary);border-radius:12px;padding:16px 20px;display:flex;flex-direction:column;gap:16px}
.card .h{font:600 15px/22px Inter;display:flex;justify-content:space-between;align-items:center}
.cols{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:20px}
dl{display:grid;grid-template-columns:130px 1fr;gap:6px 12px;margin:0;font-size:13px}dt{color:var(--color-text-tertiary)}dd{margin:0}
.mcard{border:1px solid var(--color-border-secondary);border-radius:var(--radius-card);padding:12px 14px;display:flex;flex-direction:column;gap:2px}
.mcard b{font-size:15px}.mcard span{color:var(--color-text-tertiary);font-size:13px}
.pt{display:flex;gap:8px;align-items:center;font:600 14px Inter}.pt .chip{margin-left:auto;font-weight:500}
.cta{position:sticky;bottom:0;height:52px;border:0;border-radius:var(--radius-control);background:var(--color-action-primary);color:var(--color-text-inverse);font:600 16px Inter;width:100%}
.pv[data-platform=mobile] .cols{grid-template-columns:1fr}
"""

# Hình nhỏ nằm trong .pv của kit (không mang lựa chọn) → luật ẩn data-show của kit sẽ ẩn nhầm.
# Hình nhỏ dùng data-mshow + luật ẩn riêng theo .pvm gần nhất (MSHOW_CSS, sinh sau khi có decisions).
def mini(attrs, inner, w=440):
    a = " ".join(f'data-{k}="{v}"' for k, v in attrs.items())
    inner = inner.replace('data-show="', 'data-mshow="')
    return f'<div class="pv pvm" {a} style="padding:6px;max-width:{w}px">{inner}</div>'

BASE = {"D1": "a", "D2": "b", "D3": "b", "D4": "a", "D5": "a", "D6": "a", "D7": "a", "D8": "a", "state": "x"}
def m(over, inner, w=440):
    return mini({**BASE, **over}, inner, w)

# mảnh dùng nhiều lần
W_EMPTY = field("Hoá đơn", hint=None)
W_UP = field("Hoá đơn", [frow(F_PDF, "uploading", 64), frow(F_XML, "done")])
W_ERR = field("Hoá đơn", [frow(F_BIG, "error", msg="Vượt 10 MB")])
W_SINGLE = field("Biên bản giao hàng", [frow(F_JPG, "done")], single=True)
A_EMPTY = afield("Ảnh hoá đơn")
A_GRID = afield("Ảnh tại điểm giao", [tile(0, label="Cổng kho"), tile(1, "uploading", 48, "Container"), tile(2, "error", label="Seal")], grid=True)
A_ROW = afield("Ảnh hoá đơn", [frow(("hoa-don-dau-0412.jpg", "2,1 MB", "JPG"), "uploading", 48)])

# ---------- điểm cần quyết ----------
decisions = [
 {"id": "D1", "title": "Nhãn trên app: trên khung hay trong khung",
  "why": "Text Field app đặt nhãn trong ô (DEC-207). Ô tải file không có chữ gõ vào, nên nhãn trong khung phải chia chỗ với lời gọi “Chụp ảnh hoặc chọn tệp”.",
  "source": "design-system/components/l1/text-field.md › Mobile · DEC-207",
  "options": [
   {"label": "Nhãn trên khung (như web)", "desc": "Một cấu tạo cho cả hai nền tảng; lời gọi trong khung đọc rõ.", "rec": True, "preview": m({"D1": "a"}, A_EMPTY, 360), "ideas": ["I10", "I11"]},
   {"label": "Nhãn trong khung (như Text Field app)", "desc": "Đồng bộ nhìn với ô nhập app; khung cao hơn, lời gọi xuống dòng 2.", "preview": m({"D1": "b"}, A_EMPTY, 360)}],
  "untitled": m({"D1": "a"}, A_EMPTY, 360), "untitledNote": "Untitled chỉ có web: nhãn ngoài, vùng thả mobile 343",
  "astryx": m({"D1": "b"}, A_EMPTY, 360), "astryxNote": "FileInput app: nhãn trong ô như TextField"},
 {"id": "D2", "title": "Kiểu ô chọn file trong form web",
  "why": "Form ERP dày (modal tạo, drawer sửa, khối chứng từ). Vùng thả đủ của Untitled cao khoảng 126; một form có 2–3 ô tải file sẽ chiếm nửa modal.",
  "source": "file-upload-base.tsx dòng 203–235 (FileUploadDropZone) · file-upload-trigger.tsx",
  "options": [
   {"label": "Vùng thả đủ (icon + 2 dòng)", "desc": "Như Untitled. Rõ nhất, hợp form chỉ có một ô tải hoặc màn nhập chứng từ.", "preview": m({"D2": "a"}, W_EMPTY), "ideas": ["I1", "I2", "I6"]},
   {"label": "Vùng thả gọn 1 hàng + nút Chọn file", "desc": "Cao 62, vẫn kéo thả được; nút luôn thấy (bàn phím, người không quen kéo thả).", "rec": True, "preview": m({"D2": "b"}, W_EMPTY), "ideas": ["I4", "I7"]},
   {"label": "Chỉ nút Tải file lên", "desc": "Gọn nhất, giống ô nhập; mất kéo thả, file chỉ thấy sau khi chọn.", "preview": m({"D2": "c"}, W_EMPTY), "ideas": ["I5"]}],
  "untitled": m({"D2": "a"}, W_EMPTY), "untitledNote": "FileUploadDropZone + FileTrigger (nút) là 2 phần riêng",
  "astryx": m({"D2": "c", "D8": "b"}, W_EMPTY), "astryxNote": "FileInput: nút chọn + tên file"},
 {"id": "D3", "title": "Ô nhận đúng 1 file: còn vùng chọn sau khi đã có file?",
  "why": "Nhiều chỗ chỉ nhận 1 file (biên bản giao hàng, phiếu cân, ảnh đăng kiểm). Untitled luôn giữ vùng thả; khi đã đủ file, vùng thả là chỗ bấm thừa.",
  "source": "Untitled demo (luôn giữ) · NSW, Singapore GDS (một file: thay bằng dòng file)",
  "options": [
   {"label": "Giữ vùng chọn, file nằm dưới", "desc": "Như Untitled; chọn file mới thì thay file cũ — dễ thay nhầm.", "preview": m({"D3": "a"}, W_SINGLE), "ideas": ["I1"]},
   {"label": "Dòng file thay chỗ vùng chọn", "desc": "Gọn, nói rõ “đã đủ”; muốn đổi thì xoá rồi chọn lại.", "rec": True, "preview": m({"D3": "b"}, W_SINGLE), "ideas": ["I5", "I8"]}],
  "untitled": m({"D3": "a"}, W_SINGLE), "untitledNote": "luôn giữ dropzone",
  "astryx": m({"D3": "b", "D2": "c"}, W_SINGLE), "astryxNote": "FileInput đổi thành tên file"},
 {"id": "D4", "title": "Dòng file mặc định trong form",
  "why": "Bạn đã tick dựng cả hai kiểu tiến độ (Bar, Fill). Còn chọn kiểu nào là mặc định khi kéo ra và dùng trong các màn mẫu.",
  "source": "FileListItemProgressBar / FileListItemProgressFill (file-upload-base.tsx dòng 260, 317)",
  "options": [
   {"label": "Thanh tiến độ dưới tên", "desc": "Đọc % rõ; dòng cao hơn khi đang tải (khoảng 78).", "rec": True, "preview": m({"D4": "a"}, field("Hoá đơn", [frow(F_PDF, "uploading", 64)])), "ideas": ["I3", "I9"]},
   {"label": "Nền tiến độ chạy sau dòng", "desc": "Dòng không đổi cao; % mờ hơn, khó thấy trên nền nhạt.", "preview": m({"D4": "b"}, field("Hoá đơn", [frow(F_PDF, "uploading", 64)])), "ideas": ["I2"]}],
  "untitled": m({"D4": "a"}, field("Hoá đơn", [frow(F_PDF, "uploading", 64)])), "untitledNote": "demo đặt Bar trước",
  "astryx": m({"D4": "a"}, field("Hoá đơn", [frow(F_PDF, "uploading", 64)])), "astryxNote": "Thumbnail Uploading (không có thanh trong dòng)"},
 {"id": "D5", "title": "Nút xoá và Thử lại trên dòng file",
  "why": "Dòng lỗi phải có đường sửa ngay tại chỗ. Vị trí nút quyết định dòng có bị cắt tên khi file dài.",
  "source": "file-upload-base.tsx dòng 298, 308 (ButtonUtility Delete góc trên phải + link Try again)",
  "options": [
   {"label": "Thùng rác góc trên + link Thử lại dưới", "desc": "Như Untitled; tên file có trọn bề rộng.", "rec": True, "preview": m({"D5": "a"}, field("Hoá đơn", [frow(F_BIG, "error", msg="Vượt 10 MB")])), "ideas": ["I9"]},
   {"label": "Nút Thử lại + X cùng hàng bên phải", "desc": "Thấy hai việc cùng chỗ; tên bị ép ngắn hơn khoảng 110px.", "preview": m({"D5": "b"}, field("Hoá đơn", [frow(F_BIG, "error", msg="Vượt 10 MB")])), "ideas": ["I4"]}],
  "untitled": m({"D5": "a"}, field("Hoá đơn", [frow(F_BIG, "error", msg="Vượt 10 MB")])), "untitledNote": "Delete + link-destructive Try again",
  "astryx": m({"D5": "b"}, field("Hoá đơn", [frow(F_BIG, "error", msg="Vượt 10 MB")])), "astryxNote": "nút X bên phải"},
 {"id": "D6", "title": "App: chọn nguồn ảnh / tệp",
  "why": "Bạn đã tick Camera. Lái xe chụp tại chỗ là chính (hoá đơn dầu, ảnh tại điểm), đôi khi chọn PDF có sẵn. Drag-drop không dùng trên điện thoại.",
  "source": "transport-dispatch D1 (điểm chụp ảnh bắt buộc) · invoice-management B1 (lái xe tải ảnh hoá đơn) · Filestack, Oracle mobile capture",
  "options": [
   {"label": "Một ô bấm → sheet 3 lựa chọn", "desc": "Chụp ảnh / Thư viện / Tệp; giống thói quen iOS, Android. Thêm một chạm.", "rec": True, "preview": m({"D6": "a"}, afield("Ảnh hoá đơn", sheet=False), 360), "ideas": ["I10"]},
   {"label": "Hai nút Chụp ảnh | Chọn tệp", "desc": "Chụp ngay một chạm; chiếm hai nút lớn trong form.", "preview": m({"D6": "b"}, A_EMPTY, 360), "ideas": ["I11"]},
   {"label": "Ô “+” trong lưới ảnh", "desc": "Gọn nhất khi đã có ảnh; ô trống lần đầu kém rõ là làm gì.", "preview": m({"D6": "c"}, A_EMPTY, 360), "ideas": ["I3"]}],
  "untitled": m({"D6": "a"}, A_EMPTY, 360), "untitledNote": "không có bản app — vùng thả mobile web 343",
  "astryx": m({"D6": "c", "D1": "b"}, A_EMPTY, 360), "astryxNote": "Thumbnail Placeholder (ô +)"},
 {"id": "D7", "title": "App: ảnh đã chụp hiện thế nào",
  "why": "Bạn đã tick Grid. Ảnh tại điểm cần nhìn được nội dung (seal, container) để tự kiểm trước khi gửi.",
  "source": "transport-dispatch D1 · Astryx Thumbnail Image / Loading / Uploading",
  "options": [
   {"label": "Lưới 3 cột, ảnh vuông", "desc": "Thấy ảnh ngay, đếm được số ảnh; tên ảnh là nhãn điểm chụp.", "rec": True, "preview": m({"D7": "a"}, A_GRID, 360), "ideas": ["I3", "I11"]},
   {"label": "Dòng file có ảnh nhỏ", "desc": "Giống web, đọc được tên + dung lượng; ảnh 40 khó soi.", "preview": m({"D7": "b"}, A_GRID, 360), "ideas": ["I1"]}],
  "untitled": m({"D7": "b"}, A_GRID, 360), "untitledNote": "chỉ có dòng file",
  "astryx": m({"D7": "a"}, A_GRID, 360), "astryxNote": "Thumbnail lưới"},
 {"id": "D8", "title": "Viền vùng thả",
  "why": "Nét đứt là ký hiệu quen của “thả vào đây”; Untitled dùng nét liền cho đồng bộ với ô nhập.",
  "source": "file-upload-base.tsx dòng 203 (ring-1 ring-secondary, rounded-xl) · Astryx FileInput",
  "options": [
   {"label": "Nét liền 1px (Untitled)", "desc": "Đồng bộ ô nhập, card; lúc kéo vào đổi viền đậm 2px.", "rec": True, "preview": m({"D8": "a", "D2": "a"}, W_EMPTY), "ideas": ["I6", "I8"]},
   {"label": "Nét đứt", "desc": "Nhận ra ngay là chỗ thả; nổi hơn các ô nhập xung quanh.", "preview": m({"D8": "b", "D2": "a"}, W_EMPTY), "ideas": ["I1", "I2"]}],
  "untitled": m({"D8": "a", "D2": "a"}, W_EMPTY), "untitledNote": "ring 1px, bo 12",
  "astryx": m({"D8": "b", "D2": "a"}, W_EMPTY), "astryxNote": "viền nét đứt"},
]

# ---------- ý tưởng cộng đồng ----------
ideas = [
 {"id": "I1", "source": "21st.dev", "url": "https://21st.dev/@joyco/components/file-dropzone.md", "title": "File Dropzone — xem trước ảnh, kiểm loại và cỡ",
  "why": "Kiểm loại và dung lượng ngay khi thả, báo lỗi từng file; ảnh có xem trước. Hợp ảnh sự cố, ảnh hoá đơn.",
  "preview": m({"D2": "a", "D8": "b"}, field("Ảnh sự cố", [frow(F_JPG, "done"), frow(F_BIG, "error", msg="Vượt 10 MB")]))},
 {"id": "I2", "source": "21st.dev", "url": "https://21st.dev/@vijayksingh/components/drop-zone.md", "title": "Drop Zone — sáng lên khi kéo vào, rung khi từ chối",
  "why": "Trạng thái Hover nói “thả vào đây”; file sai loại thì vùng thả báo ngay, không để người dùng thả rồi mới biết.",
  "preview": m({"D2": "a", "D8": "b"}, f'<div class="fu">{zone("hover")}</div>')},
 {"id": "I3", "source": "21st.dev", "url": "https://21st.dev/@wensity/components/file-uploader.md", "title": "File Uploader — ô ảnh, thẻ tài liệu, vòng tiến độ",
  "why": "Ảnh hiện thành ô vuông, tài liệu thành thẻ; vòng tiến độ nằm trên ảnh. Gợi ý cho lưới ảnh app.",
  "preview": m({"D7": "a", "D6": "c"}, A_GRID, 360)},
 {"id": "I4", "source": "21st.dev", "url": "https://21st.dev/@mohammed-saif-ibrahim/components/file-upload.md", "title": "File Upload — nút Chọn luôn thấy, xoá từng file",
  "why": "Nút chọn file luôn hiện cạnh vùng thả: dùng được bằng bàn phím, không phụ thuộc kéo thả.",
  "preview": m({"D2": "b", "D5": "b"}, W_UP)},
 {"id": "I5", "source": "PatternFly", "url": "https://patternfly.org/2022.11/components/file-upload/design-guidelines", "title": "File upload một file — ô gọn như input",
  "why": "Ô một file gọn như ô nhập, có nút Duyệt và Xoá; khuyên tách bản nhiều file. Hợp form dày.",
  "preview": m({"D2": "c", "D3": "b"}, W_SINGLE)},
 {"id": "I6", "source": "Maersk Design System", "url": "https://designsystem.maersk.com/components/file-upload/index.html", "title": "Kéo thả là mặc định (ngành vận tải biển)",
  "why": "Hệ thống của hãng tàu: dùng bản kéo thả cho đa số chỗ, tránh đặt ô tải file trong modal nhỏ.",
  "preview": m({"D2": "a"}, W_UP)},
 {"id": "I7", "source": "NSW Design System", "url": "https://designsystem.nsw.gov.au/components/file-upload/", "title": "Tên file dài cắt gọn, lỗi nói rõ cách sửa",
  "why": "Cắt tên dài thay vì xuống dòng; câu lỗi theo mẫu GOV.UK: nói cái sai và cách sửa.",
  "preview": m({"D2": "b"}, field("Hoá đơn", [frow(F_LONG, "done")], err=None))},
 {"id": "I8", "source": "Singapore GDS", "url": "https://designsystem.tech.gov.sg/components/file-upload", "title": "Ba trạng thái file rõ ràng + thứ tự focus",
  "why": "Đang tải, thành công, đã tải; hướng dẫn bàn phím và focus. Làm khung cho mục trợ năng.",
  "preview": m({"D2": "b"}, W_UP)},
 {"id": "I9", "source": "Telerik Design System", "url": "https://telerik.com/design-system/docs/components/upload/usage", "title": "Danh sách tải lên: cắt tên, trạng thái từng file",
  "why": "Không giới hạn độ dài tên nên luôn cắt; mỗi file có trạng thái và hành động riêng (thử lại, xoá).",
  "preview": m({"D2": "c"}, field("Chứng từ", [frow(F_PDF, "done"), frow(F_BIG, "error", msg="Vượt 10 MB")]))},
 {"id": "I10", "source": "Filestack (mobile)", "url": "https://blog.filestack.com/optimizing-document-upload-ui-mobile-devices", "title": "Mobile: chụp trực tiếp + chọn thư viện, không kéo thả",
  "why": "Trên điện thoại, chụp ảnh và chọn thư viện là hai đường chính; kéo thả hầu như không dùng; nên tải nền khi mạng chậm.",
  "preview": m({"D6": "a"}, A_ROW, 360)},
 {"id": "I11", "source": "Oracle Mobile UX", "url": "https://www.oracle.com/webfolder/ux/mobile/pattern/capture.html", "title": "Capture — chụp chứng từ ngay trong luồng",
  "why": "Mẫu chụp ảnh của ứng dụng doanh nghiệp: nút chụp nổi bật, ảnh vừa chụp hiện ngay để kiểm.",
  "preview": m({"D6": "b", "D7": "a"}, A_GRID, 360)},
]

presets = [
 {"id": "rec", "label": "Đề xuất", "pick": {d["id"]: chr(97 + next(i for i, o in enumerate(d["options"]) if o.get("rec"))) for d in decisions}},
 {"id": "untitled", "label": "Theo Untitled", "pick": {"D1": "a", "D2": "a", "D3": "a", "D4": "a", "D5": "a", "D6": "a", "D7": "b", "D8": "a"}},
 {"id": "astryx", "label": "Astryx hiện tại", "pick": {"D1": "b", "D2": "c", "D3": "b", "D4": "a", "D5": "b", "D6": "c", "D7": "a", "D8": "b"}},
]
REC = presets[0]["pick"]
for i in ideas:
    pick = dict(REC)
    for d in decisions:
        for k, o in enumerate(d["options"]):
            if i["id"] in (o.get("ideas") or []):
                pick[d["id"]] = chr(97 + k)
    pr = {"id": i["id"], "label": f'Ý tưởng {i["id"]} · {i["source"].split(" (")[0]}', "pick": pick}
    if i["id"] in ("I3", "I10", "I11"):
        pr["screen"] = 2
    presets.append(pr)

# ---------- màn demo ----------
def by_state(parts):
    """parts: {state: html} → mỗi khối chỉ hiện ở trạng thái của nó."""
    return "".join(f'<div data-show="state:{k}" style="display:contents">{v}</div>' for k, v in parts.items())

INV_FIELD = by_state({
 "default": field("Hoá đơn", hint=None),
 "uploading": field("Hoá đơn", [frow(F_PDF, "uploading", 64), frow(F_XML, "done")]),
 "done": field("Hoá đơn", [frow(F_PDF, "done"), frow(F_XML, "done")]),
 "error": field("Hoá đơn", [frow(F_BIG, "error", msg="Vượt 10 MB"), frow(F_XML, "done")]),
 "required": field("Hoá đơn", state="error", err=ERR_REQ),
 "hover": field("Hoá đơn", state="hover"),
 "disabled": field("Hoá đơn", state="disabled", hint="Hoá đơn đã khớp với khoản chi, không đổi được."),
 "long": field("Hoá đơn", [frow(F_LONG, "done"), frow(F_PDF, "uploading", 64)]),
})
S_INVOICE = (
 '<div class="pad"><div class="tb"><table><tr><th>Số hoá đơn</th><th>Người bán</th><th>Ngày</th><th>Tổng tiền (₫)</th><th>Trạng thái</th></tr>'
 '<tr><td>0001231</td><td>Petrolimex Sài Gòn</td><td>24/10/2026</td><td>12.480.000</td><td><span class="chip">Đã khớp</span></td></tr>'
 '<tr><td>0001232</td><td>VETC</td><td>25/10/2026</td><td>3.150.000</td><td><span class="chip">Chờ khớp</span></td></tr>'
 '<tr><td>0001233</td><td>Cảng Cát Lái</td><td>26/10/2026</td><td>1.920.000</td><td><span class="chip">Chờ khớp</span></td></tr></table></div></div>'
 '<div class="mw"><div class="md"><div class="md-h"><span class="fi" style="margin:0">' + ic("upload") + '</span><div><b>Tải hoá đơn đầu vào</b>'
 '<span>Ảnh hoặc PDF hoá đơn do đối tác giao tay. Hoá đơn điện tử tự về, không cần tải.</span></div></div>'
 '<div class="md-b"><div class="fu"><div class="lb">Chi nhánh</div><div class="inp">Cát Lái</div></div>' + INV_FIELD +
 '<div class="fu"><div class="lb">Ghi chú</div><div class="inp ta">Nhập ghi chú cho kế toán</div></div></div>'
 '<div class="md-f"><button class="bt">Huỷ</button><button class="bt pri">Lưu hoá đơn</button></div></div></div>')

DOC_FIELDS = by_state({
 "default": field("Biên bản giao hàng", single=True) + field("Phiếu cân", req=False, single=True, hint="Chỉ cần với hàng rời."),
 "uploading": field("Biên bản giao hàng", [frow(F_JPG, "uploading", 38)], single=True) + field("Phiếu cân", req=False, single=True),
 "done": field("Biên bản giao hàng", [frow(F_JPG, "done")], single=True) + field("Phiếu cân", [frow(("phieu-can-0412.pdf", "640 KB", "PDF"), "done")], req=False, single=True),
 "error": field("Biên bản giao hàng", [frow(F_BIG, "error", msg="Vượt 10 MB")], single=True) + field("Phiếu cân", req=False, single=True),
 "required": field("Biên bản giao hàng", state="error", err="Cần biên bản giao hàng để hoàn tất lệnh.", single=True) + field("Phiếu cân", req=False, single=True),
 "hover": field("Biên bản giao hàng", state="hover", single=True) + field("Phiếu cân", req=False, single=True),
 "disabled": field("Biên bản giao hàng", [frow(F_JPG, "done")], state="disabled", single=True) + field("Phiếu cân", req=False, state="disabled", single=True, hint="Lệnh đã hoàn tất, chứng từ chỉ xem."),
 "long": field("Biên bản giao hàng", [frow(F_LONG, "done")], single=True) + field("Phiếu cân", req=False, single=True),
})
S_DOCS = ('<div class="pad"><div class="cols"><div class="card"><div class="h">Thông tin lệnh</div><dl>'
          '<dt>Tuyến</dt><dd>Cảng Cát Lái → KCN Sóng Thần</dd><dt>Xe · lái xe</dt><dd>51C-482.19 · Trần Văn Bình</dd>'
          '<dt>Container</dt><dd>TGHU8812345 · 40\' HC</dd><dt>Giao lúc</dt><dd>14:20 26/10/2026</dd></dl></div>'
          '<div class="card"><div class="h">Chứng từ giao hàng<button class="bt sm">Tải tất cả</button></div>' + DOC_FIELDS + '</div></div></div>')

APP_COST = by_state({
 "default": afield("Ảnh hoá đơn", sheet=False),
 "uploading": afield("Ảnh hoá đơn", [frow(("hoa-don-dau-0412.jpg", "2,1 MB", "JPG"), "uploading", 48)]),
 "done": afield("Ảnh hoá đơn", [frow(("hoa-don-dau-0412.jpg", "2,1 MB", "JPG"), "done")]),
 "error": afield("Ảnh hoá đơn", [frow(("hoa-don-dau-0412.jpg", "2,1 MB", "JPG"), "error", msg="Mất kết nối")]),
 "required": afield("Ảnh hoá đơn", state="error", err="Cần ảnh hoá đơn để ghi chi phí."),
 "hover": afield("Ảnh hoá đơn", sheet=True),
 "disabled": afield("Ảnh hoá đơn", [frow(("hoa-don-dau-0412.jpg", "2,1 MB", "JPG"), "done")], state="disabled"),
 "long": afield("Ảnh hoá đơn", [frow(F_LONG, "done")]),
})
S_APP_COST = ('<div class="mpad"><div class="mcard"><b>LVT-2026-0412</b><span>Cát Lái → Sóng Thần · 51C-482.19</span></div>'
              '<div class="fu m"><div class="lb">Loại chi phí<span class="req">*</span></div><div class="inp" style="height:48px;border-radius:var(--radius-field);color:var(--color-text-primary)">Dầu diesel</div></div>'
              '<div class="fu m"><div class="lb">Số tiền<span class="req">*</span></div><div class="inp" style="height:48px;border-radius:var(--radius-field);color:var(--color-text-primary)">1.250.000 ₫</div></div>'
              + APP_COST + '<button class="cta">Ghi chi phí</button></div>')

APP_PHOTO = by_state({
 "default": afield("Ảnh tại điểm giao", grid=True, req=True),
 "uploading": afield("Ảnh tại điểm giao", [tile(0, label="Cổng kho"), tile(1, "uploading", 48, "Container")], grid=True),
 "done": afield("Ảnh tại điểm giao", [tile(0, label="Cổng kho"), tile(1, label="Container"), tile(2, label="Seal"), tile(3, label="Biên bản")], grid=True),
 "error": afield("Ảnh tại điểm giao", [tile(0, label="Cổng kho"), tile(1, label="Container"), tile(2, "error", label="Seal")], grid=True, err="1 ảnh chưa gửi được. Bấm ảnh để thử lại."),
 "required": afield("Ảnh tại điểm giao", [tile(0, label="Cổng kho")], grid=True, err="Còn thiếu ảnh: Container, Seal."),
 "hover": afield("Ảnh tại điểm giao", [tile(0, label="Cổng kho")], grid=True, sheet=True),
 "disabled": afield("Ảnh tại điểm giao", [tile(0, label="Cổng kho"), tile(1, label="Container")], grid=True, state="disabled"),
 "long": afield("Ảnh tại điểm giao", [tile(0, label="Cổng kho số 3 KCN Sóng Thần"), tile(1, label="Container TGHU8812345")], grid=True),
})
S_APP_PHOTO = ('<div class="mpad"><div class="mcard"><div class="pt">' + ic("pin", 18) + 'Điểm giao · Kho Sóng Thần<span class="chip">Bước 3/4</span></div>'
               '<span>Cần 3 ảnh: Cổng kho, Container, Seal</span></div>' + APP_PHOTO + '<button class="cta">Xác nhận đã giao</button></div>')

MSHOW_CSS = ",".join(f'.pvm:not([data-{d["id"]}="{chr(97 + i)}"]) [data-mshow~="{d["id"]}:{chr(97 + i)}"]'
                     for d in decisions for i in range(len(d["options"]))) + "{display:none!important}"
CSS += MSHOW_CSS

page = {
 "component": "Field Upload",
 "slug": "field-upload",
 "title": "Field Upload Review",
 "subtitle": "Application component · nhóm B (cùng họ, khác cấu tạo web / app) · vòng 1 Brainstorm",
 "round": "brainstorm",
 "refs": {
  "untitled": {"summary": "Ba phần: <mark>FileUploadDropZone</mark> (featured icon + “Click to upload or drag and drop” + gợi ý loại/cỡ, lỗi đỏ khi sai loại/vượt cỡ), "
               "<mark>FileListItem</mark> Progress Bar / Progress Fill (icon loại file 40, tên cắt, dung lượng, Uploading/Complete/Failed, Delete + Try again) "
               "và <mark>FileTrigger</mark> (nút chọn file, có <code>defaultCamera</code> cho chụp ảnh). Không có nhãn/gợi ý field — phần đó ráp từ Form.",
               "source": "design/_ref/untitled-ui/react/components/application/file-upload/file-upload-base.tsx · base/file-upload-trigger/file-upload-trigger.tsx"},
  "astryx": {"summary": "<mark>FileInput</mark> (nút chọn + tên file) và <mark>Thumbnail</mark> Image / Placeholder / Loading / Uploading cho ảnh.",
             "source": "design/design.md › FileInput, Thumbnail"},
  "usage": ["invoice-management B1 · web · nhân viên tải ảnh/PDF hoá đơn đầu vào (modal)",
            "transport-dispatch · web · chứng từ giao hàng của lệnh (biên bản, phiếu cân)",
            "transport-dispatch D1 · app · lái xe chụp ảnh bắt buộc tại điểm, thiếu ảnh thì chặn bước",
            "transport-dispatch · app · ghi chi phí chuyến kèm ảnh hoá đơn",
            "service-delivery A11 · web/app · tải chứng từ khách để tạo JobID nháp",
            "shipment-coordination · app · hiện trường chụp ảnh hàng, tải Lệnh nâng hàng (OQ-40)"],
  "platform": "Đã chốt ở trang Application (27/10): <mark>Tách bản Mobile</mark>, dựng theo cấu tạo Untitled, dựng đủ Drop zone Default/Hover/Disabled/Error · "
              "File row Uploading/Complete/Error · Progress Bar + Fill · File icon + Thumbnail · App Camera + Grid. Trang này chỉ hỏi phần còn mở: "
              "lớp <b>field</b> (nhãn, bắt buộc, gợi ý, lỗi) bọc quanh, và cách bày trên form."},
 "css": CSS,
 "states": [{"key": "default", "label": "Chưa có file"}, {"key": "hover", "label": "Kéo vào / mở chọn"}, {"key": "uploading", "label": "Đang tải"},
            {"key": "done", "label": "Đã tải xong"}, {"key": "error", "label": "File lỗi"}, {"key": "required", "label": "Thiếu bắt buộc"},
            {"key": "disabled", "label": "Khoá"}, {"key": "long", "label": "Tên dài"}],
 "ideas": ideas, "decisions": decisions, "presets": presets,
 "screens": [
  {"id": "invoice-web", "name": "Tải hoá đơn đầu vào", "device": "web", "width": 1280, "nav": "Hoá đơn", "title": "Hoá đơn đầu vào",
   "note": "Modal nhiều file (PDF + XML cùng hoá đơn). Trạng thái “Kéo vào” = đang kéo file vào vùng thả.", "html": S_INVOICE},
  {"id": "docs-web", "name": "Chứng từ giao hàng", "device": "web", "width": 1280, "nav": "Lệnh vận tải", "crumb": "Lệnh vận tải", "title": "LVT-2026-0412",
   "note": "Hai ô một file trong khối của màn chi tiết — xem D3 (vùng chọn còn hay mất sau khi có file).", "html": S_DOCS},
  {"id": "photo-app", "name": "Chụp ảnh tại điểm", "device": "mobile", "title": "Giao hàng", "back": True, "tabs": False, "nav": "Lệnh",
   "note": "Ảnh bắt buộc theo điểm chụp; thiếu ảnh thì chặn nút xác nhận. Trạng thái “Kéo vào / mở chọn” = sheet chọn nguồn.", "html": S_APP_PHOTO},
  {"id": "cost-app", "name": "Ghi chi phí chuyến", "device": "mobile", "title": "Ghi chi phí", "back": True, "tabs": False, "nav": "Lệnh",
   "note": "Một ảnh hoá đơn cho một khoản chi; lỗi mạng thì Thử lại tại dòng.", "html": S_APP_COST}],
}

# ================= Vòng 2 — Preview (28/10) =================
# Tổ hợp chốt ở Brainstorm: D1 A · D2 A (giữ cả 3 kiểu làm biến thể Type) · D3 B · D4 B (nền tiến độ) · D5 A · D6 A · D7 B (dòng) · D8 A
PICK = {"D1": "a", "D2": "a", "D3": "b", "D4": "b", "D5": "a", "D6": "a", "D7": "b", "D8": "a"}

# ô nhỏ lồng .pv cần biến tối khi trang bật Dark (kit chỉ đổi data-theme của .pv ngoài)
DARK = CSS.split(".pv[data-theme=dark]{", 1)[1].split("}", 1)[0]
page["css"] += ".pv[data-theme=dark] .pv{" + DARK + "}" + r"""
.dz.focus,.bt.focus,.ib.focus,.az.focus,.lkr.focus{outline:2px solid var(--color-focus-ring);outline-offset:2px}
.ib.hv{background:var(--color-bg-primary_hover);color:var(--color-text-primary)}.dz.hv{border-color:var(--color-border-input);background:var(--color-bg-primary_hover)}
.pv[data-platform=mobile] .fr{padding:12px 4px 12px 12px;border-radius:var(--radius-field)}
.pv[data-platform=mobile] .fr .ib{width:40px;height:40px}
.pv[data-platform=mobile] .fn{font-size:14px}
.lb{display:block}.req{margin-left:var(--upload-required-gap)}
.fe{align-items:flex-start}.fe .i{margin-top:2px}
.dz-c.hv .bt{background:var(--color-bg-primary_hover)}.dz-c.focus .bt{outline:2px solid var(--color-focus-ring);outline-offset:2px}.dz-c.error .bt{border-color:var(--color-border-error)}
.mf .fu{position:static}
.mf{box-sizing:border-box;position:relative;width:351px;min-height:300px;padding:16px;display:flex;flex-direction:column;gap:16px;background:var(--color-bg-primary);overflow:hidden}
.mf.tall{min-height:520px}
.gl{font:600 12px/16px Inter;color:var(--color-text-tertiary);text-transform:uppercase;letter-spacing:.04em}
"""

def pvc(inner, w=480, over=None, plat="web"):
    a = {**PICK, **(over or {}), "state": "x", "platform": plat}
    return mini(a, inner, w)

def cell(lab, inner):
    return f'<div class="ex" style="display:flex;flex-direction:column;gap:6px;width:max-content;max-width:100%"><span style="font:500 11px Inter;color:var(--color-text-tertiary)">{lab}</span>{inner}</div>'

def row(title, cells, note=""):
    return (f'<div style="font:600 13px Inter,system-ui,sans-serif;margin:24px 0 4px">{title}</div>'
            + (f'<div style="font:12px/18px Inter,system-ui,sans-serif;color:var(--color-text-tertiary);margin-bottom:8px">{note}</div>' if note else '<div style="height:4px"></div>')
            + f'<div style="display:flex;flex-wrap:wrap;gap:20px;align-items:flex-start">{"".join(cells)}</div>')

def zone_only(t, state=""):
    return pvc(f'<div style="width:{440 if t != "c" else 380}px">{zone(state)}</div>', over={"D2": t})

TYPES = [("a", "Vùng thả đủ (mặc định)"), ("b", "Vùng thả gọn 1 hàng"), ("c", "Chỉ nút")]

def grid_web():
    h = ""
    for t, nm in TYPES:
        cells = [cell("Default", zone_only(t)), cell("Hover chuột", zone_only(t, "hv"))]
        if t != "c":
            cells.append(cell("Đang kéo file vào", zone_only(t, "hover")))
        cells += [cell("Focus bàn phím", zone_only(t, "focus")),
                  cell("Disabled", zone_only(t, "disabled")), cell("Error (thiếu bắt buộc / sai loại)", zone_only(t, "error"))]
        h += row(f"Vùng chọn file — Type {nm}", cells,
            {"a": "Dùng khi field là nội dung chính của modal / màn (tải hoá đơn). Bấm cả vùng hoặc kéo thả.",
             "b": "Dùng trong khối của màn chi tiết, nhiều field xếp dọc. Nút “Chọn file” là đích bấm chính.",
             "c": "Dùng ở bảng / hàng chật, hoặc khi kéo thả không có nghĩa (một file nhỏ). Gợi ý nằm cạnh nút."}[t])
    h += row("Dòng file — nền tiến độ (Progress Fill)", [
        cell("Đang tải 64%", pvc(f'<div style="width:440px">{frow(F_PDF, "uploading", 64)}</div>')),
        cell("Xong", pvc(f'<div style="width:440px">{frow(F_XML, "done")}</div>')),
        cell("Lỗi — vượt cỡ", pvc(f'<div style="width:440px">{frow(F_BIG, "error", msg="Vượt 10 MB")}</div>')),
        cell("Lỗi — mất kết nối", pvc(f'<div style="width:440px">{frow(F_PDF, "error", msg="Mất kết nối")}</div>')),
        cell("Hover nút xoá", pvc(f'<div style="width:440px">{frow(F_XML, "done").replace("ib del", "ib del hv")}</div>')),
        cell("Focus link Thử lại", pvc(f'<div style="width:440px">{frow(F_BIG, "error", msg="Vượt 10 MB").replace("class=\"lkr\"", "class=\"lkr focus\"")}</div>'))],
        "Icon loại file = File type icon của DS (Misc icons), cỡ MD 40. Nền tiến độ chạy từ trái; % ghi ở dòng phụ. Xoá luôn ở góc trên phải.")
    h += row("Icon loại file và ảnh nhỏ", [
        cell("PDF", pvc(f'<div style="width:300px">{frow(F_PDF, "done")}</div>', w=320)),
        cell("XML — chưa có loại riêng, tạm Other", pvc(f'<div style="width:300px">{frow(F_XML, "done")}</div>', w=320)),
        cell("IMG (JPG, PNG)", pvc(f'<div style="width:300px">{frow(F_BIG, "done")}</div>', w=320)),
        cell("Ảnh — hiện ảnh nhỏ", pvc('<div style="width:300px">' + frow(F_JPG, "done").replace(ftype("JPG"),
             f'<span class="th sh0">{ic("img", 16)}</span>') + '</div>', w=320))])
    h += row("Field đủ (nhãn · vùng chọn · danh sách · gợi ý / lỗi)", [
        cell("Nhiều file — chưa có", pvc(f'<div style="width:440px">{field("Hoá đơn", hint="Mỗi hoá đơn tải cả PDF và XML nếu có.")}</div>')),
        cell("Nhiều file — đang tải + xong", pvc(f'<div style="width:440px">{W_UP}</div>')),
        cell("Thiếu bắt buộc", pvc(f'<div style="width:440px">{field("Hoá đơn", state="error", err=ERR_REQ)}</div>')),
        cell("Khoá (đã khớp khoản chi)", pvc(f'<div style="width:440px">{field("Hoá đơn", [frow(F_PDF, "done")], state="disabled", hint="Hoá đơn đã khớp với khoản chi, không đổi được.")}</div>')),
        cell("Không bắt buộc", pvc(f'<div style="width:440px">{field("Phiếu cân", req=False, hint="Chỉ cần với hàng rời.", single=True)}</div>', over={"D2": "b"})),
        cell("Một file — chưa có (Type gọn)", pvc(f'<div style="width:440px">{field("Biên bản giao hàng", single=True)}</div>', over={"D2": "b"})),
        cell("Một file — có file: dòng thay vùng chọn", pvc(f'<div style="width:440px">{W_SINGLE}</div>', over={"D2": "b"})),
        cell("Một file — Type chỉ nút", pvc(f'<div style="width:440px">{field("Biên bản giao hàng", single=True)}</div>', over={"D2": "c"}))],
        "Nhãn 14 Medium trên khung (như Text field web). Ô một file: có file thì vùng chọn ẩn, xoá file thì hiện lại.")
    h += row("Chữ dài", [
        cell("Tên file dài — cắt 1 dòng, tooltip đủ", pvc(f'<div style="width:440px">{frow(F_LONG, "done")}</div>')),
        cell("Ở bề rộng 320", pvc(f'<div style="width:320px">{field("Hoá đơn GTGT đầu vào của nhà cung cấp nhiên liệu", [frow(F_LONG, "uploading", 38)], hint="PDF, XML, JPG hoặc PNG, tối đa 10 MB mỗi file; tối đa 20 file một lần")}</div>', w=340, over={"D2": "b"})),
        cell("Lỗi dài xuống dòng", pvc(f'<div style="width:320px">{field("Hoá đơn", state="error", err="File HD-0001234.xml không đúng định dạng hoá đơn điện tử. Tải lại file XML gốc từ cổng của người bán.")}</div>', w=340, over={"D2": "b"}))],
        "Tên file không xuống dòng (cắt giữa không làm — giữ đuôi trong cột loại). Nhãn, gợi ý và lỗi được xuống dòng.")
    return h

def mf(inner, tall=False):
    return pvc(f'<div class="mf{" tall" if tall else ""}">{inner}</div>', w=363, plat="mobile")

def grid_mob():
    f1 = mf('<span class="gl">Chưa có · thiếu · khoá</span>' + afield("Ảnh hoá đơn")
            + afield("Ảnh hoá đơn", state="error", err="Cần ảnh hoá đơn để ghi chi phí.")
            + afield("Ảnh hoá đơn", state="disabled"))
    f2 = mf('<span class="gl">Bấm ô → sheet chọn nguồn</span>' + afield("Ảnh hoá đơn", sheet=True), tall=True)
    f3 = mf('<span class="gl">Ảnh tại điểm — dạng dòng</span>' + afield("Ảnh tại điểm giao",
            [tile(0, label="Cổng kho"), tile(1, "uploading", 48, "Container"), tile(2, "error", label="Seal")], grid=True,
            err="1 ảnh chưa gửi được. Bấm Thử lại."), tall=True)
    f4 = mf('<span class="gl">Một file · chữ dài</span>' + afield("Ảnh hoá đơn", [frow(("hoa-don-dau-0412.jpg", "2,1 MB", "JPG"), "uploading", 48)])
            + afield("Ảnh hoá đơn", [frow(("hoa-don-dau-0412.jpg", "2,1 MB", "JPG"), "done")])
            + afield("Ảnh biên bản giao hàng có chữ ký và đóng dấu của kho nhận", [frow(F_LONG, "done")]), tall=True)
    return [f1, f2, f3, f4]

page["round"] = "preview"
page["subtitle"] = ("Application component · nhóm B · vòng 2 Preview — tổ hợp đã chốt: "
                    + " · ".join(f"{k} {v.upper()}" for k, v in PICK.items()) + " (D2: giữ cả 3 kiểu làm biến thể)")
page["preview"] = {"version": "1", "pick": PICK,
                   "changes": "icon loại file lấy theo File type icon của DS (Misc icons, MD 40; XML tạm Other); bản đầu theo lựa chọn vòng 1: vùng chọn 3 Type (đủ / gọn / nút), dòng file nền tiến độ, app ảnh dạng dòng",
                   "blocks": [{"title": "Web", "platform": "web", "note": "Field 440 · vùng thả đủ / gọn / nút · dòng file 64 · nhãn 14 trên khung", "html": grid_web()},
                              {"title": "Mobile (app)", "platform": "mobile", "note": "Khung 393 · ô bấm mở sheet · ảnh dạng dòng · nút xoá vùng bấm 44",
                               "frames": grid_mob()}]}

# Khai giá trị preview — vòng 3 đối chiếu foundation (ds-foundation-check.py)
# sel = chỗ trong CSS để tab Foundation vẽ lại hình theo token (bắt buộc với ds-foundation-check)
PART_SEL = {
 "Field": ".fu", "Label": ".lb", "Required mark": ".req", "Hint": ".hn", "Error text": ".fe", "Error icon": ".fe .i",
 "Dropzone": ".dz", "Dropzone full": ".dz-a", "Dropzone compact": ".dz-b", "Dropzone button only": ".dz-c",
 "Dropzone text": ".dz-t", "Dropzone link": ".dz-t b", "Dropzone hint": ".dz-h", "Featured icon": ".fi",
 "Featured icon compact": ".dz-b .fi,.fi.sm", "Dropzone hover": ".dz.hv", "Dropzone drag-over": ".dz.hover",
 "Dropzone disabled": ".dz.disabled,.az.disabled", "Dropzone error": ".dz.error,.az.error,.az2.error .bt",
 "Focus ring": ".dz.focus,.bt.focus,.ib.focus,.az.focus,.lkr.focus", "Choose button": ".bt", "File list": ".fl",
 "File row": ".fr", "File row error": ".fr.error", "Progress fill": ".fr .fill", "File type icon": ".ft", "Thumbnail": ".th",
 "File name": ".fn", "File meta": ".fs", "File meta divider": ".sep", "Status done": ".st.ok", "Status error": ".st.er",
 "Status uploading": ".st.up", "Status icon": ".st .i", "Retry link": ".lkr", "Delete button": ".ib", "Delete button hover": ".ib.hv",
 "App tap area": ".az", "App tap icon": ".az .fi", "Sheet": ".sht", "Sheet grabber": ".sht .hd", "Sheet title": ".sh-t",
 "Sheet item": ".sh-i", "Scrim": ".scr"}
MOB_SEL = {"Label": ".fu.m .lb", "File row": ".pv[data-platform=mobile] .fr", "File name": ".pv[data-platform=mobile] .fn",
           "Delete button": ".pv[data-platform=mobile] .fr .ib"}
ICON_SEL = {"Featured icon": ".fi .i", "Choose button": ".bt .i", "Delete button": ".ib .i", "App tap icon": ".az .fi .i",
            "Sheet item": ".sh-i .i"}
CSSP = {("Focus ring", "focus-width"): "outline-width", ("Focus ring", "focus-offset"): "outline-offset",
        ("Focus ring", "color"): "outline-color", ("Retry link", "height"): "line-height",
        ("File meta divider", "color"): "background", ("Scrim", "background"): "background",
        ("Sheet", "radius"): ["border-top-left-radius", "border-top-right-radius"]}
V = []
def v(part, prop, value, **kw):
    sel = kw.pop("sel", None) or (ICON_SEL.get(part) if prop == "icon-size" else None) or \
          (MOB_SEL.get(part) if kw.get("platform") == "Mobile" else None) or PART_SEL[part]
    row = {"part": part, "prop": prop, "value": value, "sel": sel, **kw}
    if (part, prop) in CSSP:
        row["cssProp"] = CSSP[(part, prop)]
    V.append(row)
W_, M_ = {"platform": "Web"}, {"platform": "Mobile"}
page["css"] += ".st.up{color:var(--color-text-secondary)}.az{min-height:72px;box-sizing:border-box}"
v("Field", "gap", 6)
v("Label", "font-size", 14, **W_); v("Label", "line-height", 20, **W_); v("Label", "font-weight", 500); v("Label", "color", "#525252", role="text", on="#FFFFFF")
v("Label", "font-size", 13, **M_)
v("Required mark", "color", "#B42318", role="text", on="#FFFFFF")
v("Hint", "font-size", 12.5); v("Hint", "line-height", 18); v("Hint", "color", "#737373", role="text", on="#FFFFFF")
v("Error text", "font-size", 12.5); v("Error text", "color", "#B42318", role="text", on="#FFFFFF"); v("Error icon", "icon-size", 14)
v("Dropzone", "radius", 12, **W_); v("Dropzone", "border-width", 1); v("Dropzone", "border-color", "#D4D4D4", role="decorative", on="#FFFFFF")
v("Dropzone", "background", "#FFFFFF")
v("Dropzone full", "padding-y", 16, **W_); v("Dropzone full", "padding-x", 24, **W_); v("Dropzone full", "gap", 4, **W_)
v("Dropzone compact", "padding", 12, **W_); v("Dropzone compact", "padding-left", 14, **W_); v("Dropzone compact", "gap", 12, **W_)
v("Dropzone button only", "gap", 12, **W_)
v("Dropzone text", "font-size", 13.5); v("Dropzone text", "line-height", 20); v("Dropzone text", "color", "#737373", role="text", on="#FFFFFF")
v("Dropzone link", "color", "#171717", role="text", on="#FFFFFF"); v("Dropzone link", "font-weight", 600)
v("Dropzone hint", "font-size", 12); v("Dropzone hint", "line-height", 18); v("Dropzone hint", "color", "#737373", role="text", on="#FFFFFF")
v("Featured icon", "size", 40, **W_); v("Featured icon", "radius", 10, **W_); v("Featured icon", "icon-size", 20)
v("Featured icon", "border-color", "#E5E5E5", role="decorative", on="#FFFFFF"); v("Featured icon", "color", "#525252", role="icon", on="#FFFFFF")
v("Featured icon compact", "size", 36, **W_)
v("Dropzone hover", "background", "#F5F5F5", state="hover"); v("Dropzone hover", "border-color", "#737373", role="border", on="#FFFFFF", state="hover")
v("Dropzone drag-over", "border-width", 2, state="drag"); v("Dropzone drag-over", "border-color", "#171717", role="border", on="#FAFAFA", state="drag")
v("Dropzone drag-over", "background", "#FAFAFA", state="drag")
v("Dropzone disabled", "background", "#F5F5F5", state="disabled"); v("Dropzone disabled", "opacity", 0.6, state="disabled")
v("Dropzone error", "border-color", "#F04438", role="border", on="#FFFFFF", state="error")
v("Focus ring", "focus-width", 2); v("Focus ring", "focus-offset", 2); v("Focus ring", "color", "#262626", role="border", on="#FFFFFF")
v("Choose button", "height", 32, **W_, control=True, interactive=True, hitArea=32); v("Choose button", "padding-x", 12, **W_)
v("Choose button", "radius", 8); v("Choose button", "gap", 6); v("Choose button", "font-size", 13); v("Choose button", "font-weight", 600)
v("Choose button", "border-color", "#D4D4D4", role="decorative", on="#FFFFFF"); v("Choose button", "icon-size", 16)
v("File list", "gap", 8)
v("File row", "padding-y", 12, **W_); v("File row", "padding-left", 14, **W_); v("File row", "padding-right", 8, **W_); v("File row", "gap", 12)
v("File row", "radius", 12, **W_); v("File row", "radius", 14, **M_); v("File row", "padding-left", 12, **M_); v("File row", "padding-right", 4, **M_)
v("File row", "border-color", "#E5E5E5", role="decorative", on="#FFFFFF"); v("File row error", "border-color", "#F04438", role="border", on="#FFFFFF", state="error")
v("Progress fill", "background", "#F5F5F5", role="decorative", on="#FFFFFF")
v("File type icon", "size", 40)  # instance File type icon / Size=MD của DS (Misc icons) — màu, chữ theo set gốc
v("Thumbnail", "size", 40); v("Thumbnail", "radius", 8)
v("File name", "font-size", 13.5, **W_); v("File name", "font-size", 14, **M_); v("File name", "line-height", 20); v("File name", "font-weight", 500)
v("File name", "color", "#171717", role="text", on="#FFFFFF")
v("File meta", "font-size", 12.5); v("File meta", "line-height", 18); v("File meta", "gap", 8); v("File meta", "color", "#737373", role="text", on="#FFFFFF")
v("File meta divider", "height", 12); v("File meta divider", "color", "#D4D4D4", role="decorative", on="#FFFFFF")
v("Status done", "color", "#1B7542", role="text", on="#FFFFFF"); v("Status error", "color", "#B42318", role="text", on="#FFFFFF")
v("Status uploading", "color", "#525252", role="text", on="#F5F5F5"); v("Status icon", "icon-size", 14)
v("Retry link", "font-size", 13); v("Retry link", "font-weight", 600); v("Retry link", "color", "#B42318", role="text", on="#FFFFFF")
v("Retry link", "height", 18, interactive=True, hitArea=24, **W_)
v("Delete button", "size", 32, **W_, interactive=True, hitArea=32); v("Delete button", "size", 40, **M_, interactive=True, hitArea=44)
v("Delete button", "radius", 8); v("Delete button", "icon-size", 16); v("Delete button", "color", "#737373", role="icon", on="#FFFFFF")
v("Delete button hover", "background", "#F5F5F5", state="hover")
v("App tap area", "radius", 16, **M_); v("App tap area", "padding", 14, **M_); v("App tap area", "gap", 12, **M_)
v("App tap area", "min-height", 72, **M_, interactive=True, hitArea=72); v("App tap area", "border-color", "#D4D4D4", role="decorative", on="#FFFFFF", **M_)
v("App tap icon", "size", 48, **M_); v("App tap icon", "background", "#F5F5F5", **M_); v("App tap icon", "icon-size", 24, **M_)
v("Sheet", "radius", 28, **M_); v("Sheet", "padding-x", 16, **M_); v("Sheet", "padding-bottom", 24, **M_)
v("Sheet grabber", "width", 36, **M_); v("Sheet grabber", "height", 4, **M_)
v("Sheet title", "font-size", 17, **M_); v("Sheet title", "line-height", 24, **M_); v("Sheet title", "font-weight", 600, **M_)
v("Sheet item", "height", 52, **M_, interactive=True, hitArea=52); v("Sheet item", "gap", 12, **M_); v("Sheet item", "font-size", 15, **M_); v("Sheet item", "icon-size", 20, **M_)
v("Scrim", "background", "color/bg/overlay", **M_)
# phần còn lại của CSS component (khai đủ để máy chấm hết)
v("Choose button", "background", "#FFFFFF"); v("Choose button", "line-height", 18)
v("Choose button hover", "background", "#F5F5F5", sel=".dz-c.hv .bt", state="hover")
v("Choose button focus", "focus-offset", 2, sel=".dz-c.focus .bt", cssProp="outline-offset")
v("Choose button focus", "color", "#262626", sel=".dz-c.focus .bt", cssProp="outline-color", role="border", on="#FFFFFF")
v("Choose button error", "border-color", "#F04438", sel=".dz-c.error .bt", role="border", on="#FFFFFF", state="error")
v("Required mark", "margin-left", 2)
v("Error text", "line-height", 18); v("Error text", "gap", 6); v("Error icon", "margin-top", 2, sel=".fe .i")
v("Dropzone compact text", "min-width", 150, sel=".dz-m")
v("Dropzone link", "underline-offset", 2, sel=".dz-t .lk", cssProp="text-underline-offset")
v("Featured icon", "margin-bottom", 8)
v("Featured icon drag-over", "color", "#171717", sel=".dz.hover .fi", role="icon", on="#FAFAFA", state="drag")
v("File row", "background", "#FFFFFF")
v("Thumbnail", "color", "#737373", role="decorative", on="#C9D4E0")
v("File meta", "margin-top", 1); v("File meta divider", "width", 1)
v("Status icon", "gap", 4, sel=".st")
v("Retry link", "margin-top", 6)
v("Delete button", "margin-top", 6, sel=".del", cssProp="margin-top", tpl="calc(-1 * $)"); v("Delete button", "margin-right", 2, sel=".del", cssProp="margin-right", tpl="calc(-1 * $)")
v("Delete button hover", "color", "#171717", role="icon", on="#F5F5F5", state="hover")
v("App tap area", "background", "#FFFFFF", **M_)
v("Sheet", "background", "#FFFFFF", **M_); v("Sheet", "padding-top", 8, **M_)
v("Sheet grabber", "radius", 2, **M_); v("Sheet grabber", "background", "#D4D4D4", role="decorative", on="#FFFFFF", **M_)
v("Sheet grabber", "margin-bottom", 12, **M_); v("Sheet title", "margin-bottom", 6, **M_)
v("Sheet item", "border-color", "#E5E5E5", role="decorative", on="#FFFFFF", cssProp="border-bottom-color", **M_)
page["values"] = V

# Tách CSS: khung màn mẫu → cssScreen (không chấm); phương án không chọn → cssIgnore (có lý do)
import re
SCREEN = re.compile(r"^(\.pv|\.pad|\.mpad|table|td,th|th|\.tb|\.chip|\.mw|\.md|\.inp|\.ta|\.card|\.cols|dl|dt|dd|\.mcard|\.pt|\.cta|\.mf|\.gl|\.bt\.pri|\.pv\[data-platform=mobile\] \.cols)(\b|[^\w-]|$)")
cmp_css, scr_css = [], []
for sel, body in re.findall(r"([^{}]+)\{([^{}]*)\}", re.sub(r"/\*.*?\*/", "", page["css"], flags=re.S)):
    s = sel.strip()
    keep_cmp = s.startswith(".pv[data-theme=dark]") or s.startswith(".pv[data-D") or s.startswith(".pvm") \
               or s.startswith(".pv[data-platform=mobile] .f") or (s == ".pv" and False)
    (cmp_css if keep_cmp or not SCREEN.match(s) else scr_css).append(f"{s}{{{body}}}")
page["css"], page["cssScreen"] = "\n".join(cmp_css), "\n".join(scr_css) + "\n.sh0{background:#C9D4E0}.sh1{background:#D8CFC2}.sh2{background:#C4D1C8}.sh3{background:#D3C9D8}"
NOT_PICKED = "phương án không chọn ở vòng 1 — chỉ dùng cho trang Brainstorm"
page["cssIgnore"] = [
 {"sel": ".lbi", "why": "D1 B (nhãn trong khung app) — " + NOT_PICKED},
 {"sel": ".bar", "why": "D4 A (thanh tiến độ) — " + NOT_PICKED}, {"sel": ".bar i", "why": "D4 A — " + NOT_PICKED},
 {"sel": ".az2", "why": "D6 B (hai nút Chụp ảnh | Chọn tệp) — " + NOT_PICKED},
 {"sel": ".bt.big", "why": "D6 B — " + NOT_PICKED},
 {"sel": ".bt.sm", "why": "D5 B (nút Thử lại bên phải) — " + NOT_PICKED},
 {"sel": ".fa", "why": "D5 B (cụm nút bên phải) — " + NOT_PICKED},
 *[{"sel": x, "why": "D7 A (lưới ảnh) / D6 C (ô +) — " + NOT_PICKED}
   for x in (".gr", ".tl", ".tl .ph", ".tl.add", ".tl.error", ".tov", ".tov.er", ".ring", ".tcap", ".tx")],
 {"sel": ".lb", "props": ["gap"], "why": "nhãn đổi sang display:block (dấu * theo dòng chữ) — gap không còn tác dụng"},
]

# Preview bản 1 duyệt 28/10 (trong chat, kèm sửa icon loại file theo DS) → vòng 3 đối chiếu foundation
page["round"] = "foundation"

# vòng 5 — review Figma (tab 4)
import json as _json, pathlib as _pl
page["round"] = "review"
page["reviews"] = _json.loads((_pl.Path(__file__).parent / "reviews.json").read_text())
page["figma"] = {"url": "https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=6975-226270", "label": "Section Field upload 6975:226270 · Demo 6978:232794 trên DS · Application components"}

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_lib"))
from pvkit import tok_css_nested  # noqa: E402
page["css"] = tok_css_nested() + page["css"]
from icon_dec329 import apply as _dec329  # noqa
_dec329(page)  # DEC-329: cỡ, nét, màu icon
OUT.write_text(json.dumps(page, ensure_ascii=False, indent=1))
print("ok", OUT, len(ideas), "ý tưởng ·", len(decisions), "điểm ·", len(page["screens"]), "màn ·", len(V), "giá trị")
