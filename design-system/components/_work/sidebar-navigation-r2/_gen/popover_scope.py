"""Popover 2 cột chọn phạm vi (DEC-288 D4 A, user chọn lại 28/10 thay hộp thoại 3 cột).
Đầu: chi nhánh + Đổi chi nhánh (chuyển sang danh sách chi nhánh). Trái Module, phải Cơ sở. Chọn là chuyển ngay.
Rê chuột qua module → cột Cơ sở đổi theo (proto hover); dấu ✓ theo phạm vi đang áp."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import scope_variants as SV
import proto_scope as PS
ic = SV.ic
SV.ICONS.update({"arr": '<path d="M5 12h14M13 6l6 6-6 6"/>', "out": '<path d="M9.3 4.2A7 7 0 0 1 19 9c0 1.6-.6 3.3-1.5 4.9M15 17.6c-1.4 1.8-3 3.4-3 3.4s-7-6.5-7-12c0-.9.2-1.8.5-2.6"/><path d="M3 3l18 18"/>'})
BRS, MODS, FAC, UNIT, OUT = PS.BRS, PS.MODS, PS.FAC, PS.UNIT, PS.OUT
ckey, fac_label, combos = PS.ckey, PS.fac_label, PS.combos


def row(attrs, title, sub, lead, tone=None, sys_=False, cls=""):
    lead_h = f'<span class="mt t-{tone}">{ic(lead, 16)}</span>' if tone else f'<span class="oi">{ic(lead, 16)}</span>'
    a = " ".join(f'data-{k}="{v}"' for k, v in attrs.items())
    return (f'<div class="so{" sys" if sys_ else ""} {cls}" {a} role="radio">{lead_h}<span class="ot"><span class="o1">{title}</span>'
            f'<span class="o2">{sub}</span></span><span class="ok">{ic("check", 16)}</span></div>')


def sfield(ph, scope):
    return (f'<div class="sds on sf" data-sq="{scope}" role="search">{ic("search", 16)}<span class="sph">{ph}</span><i class="car"></i>'
            f'<button class="sdq" aria-label="Đóng tìm">{ic("x", 14)}</button></div>')


def head(b_fixed=None):
    names = "".join(f'<b class="bn" data-k="{k}">{t}</b>' for k, (t, _, _) in BRS.items()) if not b_fixed else f'<b>{BRS[b_fixed][0]}</b>'
    return (f'<div class="poh"><span class="pok">{ic("building", 16)}Chi nhánh</span>{names}'
            f'<button class="lk">Đổi chi nhánh{ic("arr", 14)}</button></div>')


def mod_col(b=None):
    def sub(m):
        if m == "vt":
            return "Không chia cơ sở"
        if b:
            return f"{len(FAC[(m, b)])} {UNIT[m][0]}"
        return "".join(f'<span class="bx" data-k="{bb}">{len(FAC[(m, bb)])} {UNIT[m][0]}</span>' for bb in BRS)
    rows = ""
    for k, (t, i, tone) in MODS.items():
        if k == "vt" and not b:  # Vận tải chuyển ngay → mỗi chi nhánh một dòng (ghi đúng phạm vi)
            rows += "".join(row({"m": "vt", "b": bb, "ck": ckey(bb, "vt", None)}, t, sub(k), i, tone, cls="vtb") for bb in BRS)
        else:
            rows += row({"m": k}, t, sub(k), i, tone)
    return (f'<div class="sdcol cm" role="radiogroup" aria-label="Module"><div class="sdt">Module'
            f'<button class="sdi" aria-label="Tìm module">{ic("search", 16)}</button></div>{sfield("Tìm module…", "m")}{rows}</div>')


def fac_block(m, b, q=None):
    fs = FAC[(m, b)]
    many = len(fs) > 1
    u, U = UNIT[m]
    top = (f'<div class="sds on" role="search">{ic("search", 16)}<b class="sq">{q}</b><button class="sdq" aria-label="Xoá và đóng tìm">{ic("x", 14)}</button></div>'
           if q else '<div class="sdt">Cơ sở' + (f'<button class="sdi" aria-label="Tìm {u}">{ic("search", 16)}</button>' if many else "") + '</div>'
           + (sfield(f"Tìm {u}…", "f") if many else ""))
    fl = [x for x in fs if not q or q.lower() in x[1].lower()]
    rows = ""
    if not q:
        rows += row({"f": "all", "ck": ckey(b, m, "all")}, f"Tất cả {u}", f"{len(fs)} {u} · xem tổng hợp", "layers", sys_=True) if many else ""
        rows += row({"f": "out", "ck": ckey(b, m, "out")}, "Ngoài cơ sở", OUT[m], "out", sys_=True) + '<div class="sdv"></div>'
    rows += "".join(row({"f": k, "ck": ckey(b, m, k)}, t, s, "pin") for k, t, s in fl) if fl else SV.empty(f"Không tìm thấy {u}", "Thử tên hoặc khu vực khác.")
    note = "" if many or q else f'<div class="c3n">Chi nhánh này chỉ có 1 {u}.</div>'
    return f'<div class="c3" data-k="{m}-{b}">{top}{rows}{note}</div>'


def vt_block():
    return f'<div class="c3" data-k="vt"><div class="sdt">Cơ sở</div>{SV.empty("Vận tải không chia cơ sở", "Bấm Vận tải để chuyển, dữ liệu xem theo cả chi nhánh.")}</div>'


def branch_view():
    rows = (row({}, "Delta Logistics", "Công ty mẹ · Toàn tổ chức", "org", cls="pz-dis") + '<div class="sdv"></div>'
            + "".join(row({"b": k}, t, s, "building") for k, (t, s, _) in BRS.items())
            + row({}, "CN Đà Nẵng", "Chưa mở module nào", "building", cls="pz-dis"))
    return (f'<div class="pbr"><div class="poh"><button class="pbk" aria-label="Quay lại">{ic("chev", 16)}</button>'
            f'<span class="pok">Đổi chi nhánh</span></div>'
            f'<div class="sdcol"><div class="sbx" role="search">{ic("search", 16)}<span class="sph">Tìm chi nhánh, tỉnh thành…</span></div>'
            f'{sfield("Tìm chi nhánh, tỉnh thành…", "b")}{rows}</div></div>')


def popover():
    c3 = vt_block() + "".join(fac_block(m, b) for (m, b) in FAC)
    return (f'<div class="pop pz" data-show="state:scope" data-cmp role="dialog" aria-label="Đổi phạm vi làm việc">'
            f'<div class="pmain">{head()}<div class="pob">{mod_col()}<div class="sdcol" role="radiogroup" aria-label="Cơ sở">{c3}</div></div></div>'
            f'{branch_view()}</div>')


def static(kind):
    """Bản tĩnh cho Bảng biến thể."""
    if kind == "branch":
        return f'<div class="pop st pz-br">{branch_view().replace("pbr", "pbr on")}</div>'
    m, b, q = {"many": ("bd", "hcm", None), "one": ("bd", "hp", None), "dau": ("dau", "hcm", None), "q": ("bd", "hcm", "Sóng")}.get(kind, (None, "hcm", None))
    if kind == "vt":
        c3 = vt_block().replace('class="c3"', 'class="c3 on"')
        mods = mod_col("hcm").replace('data-m="vt"', 'data-m="vt" data-on')
    else:
        c3 = fac_block(m, b, q).replace('class="c3"', 'class="c3 on"', 1)
        mods = mod_col(b).replace(f'data-m="{m}"', f'data-m="{m}" data-on')
        c3 = c3.replace(f'data-ck="{ckey(b, m, "f1")}"', f'data-ck="{ckey(b, m, "f1")}" data-on')
    return f'<div class="pop st">{head(b)}<div class="pob">{mods}<div class="sdcol">{c3}</div></div></div>'


def board_rows():
    vg_row = SV.vg_row
    return (vg_row("Popover chọn phạm vi · 2 cột (DEC-288 D4 A)", [
        ("Module chia cơ sở · nhiều xưởng (HCM)", static("many")), ("Module chia cơ sở · 1 xưởng (Hải Phòng)", static("one"))], 2,
        "mở từ thẻ phạm vi; bấm cơ sở là chuyển ngay")
        + vg_row("Popover · trường hợp khác", [
            ("Module không chia cơ sở (Vận tải)", static("vt")), ("Cây dầu · Tất cả / Ngoài cơ sở", static("dau")),
            ("Đang tìm xưởng", static("q")), ("Đổi chi nhánh", static("branch"))], 2))


CSS = r"""
/* popover chọn phạm vi 2 cột (DEC-288 D4 A, đổi lại 28/10) */
.scope{cursor:pointer}.scope:hover{background:var(--muted)}.pv[data-state=scope] .scope{background:#F5F5F5}
.pop{position:absolute;z-index:31;left:284px;bottom:12px;width:600px;background:var(--bg);border:1px solid var(--line);border-radius:12px;box-shadow:var(--shadow);display:flex;flex-direction:column;overflow:hidden}
.pop.st{position:relative;left:auto;bottom:auto;width:100%;max-width:600px}
.poh{display:flex;align-items:center;gap:8px;min-height:48px;box-sizing:border-box;padding:8px 12px 8px 16px;border-bottom:1px solid var(--line)}
.pok{display:inline-flex;align-items:center;gap:6px;font:400 14px/20px Inter;color:var(--fg3)}
.poh b{font:600 14px/20px Inter;color:var(--fg);min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.poh .lk{margin-left:auto;display:inline-flex;align-items:center;gap:4px;border:0;background:none;font:500 13px/18px Inter;color:var(--fg);text-decoration:none;text-underline-offset:2px;cursor:pointer;white-space:nowrap;padding:4px}.poh .lk:hover{text-decoration:underline}
.pop .sf{display:none}.sph{color:var(--fg4)}.car{width:1px;height:16px;background:var(--fg);margin-left:-6px;animation:car calc(var(--duration-slow) * 2) steps(1) infinite}@keyframes car{50%{opacity:0}}
.pbk{width:28px;height:28px;border:0;background:none;border-radius:6px;display:grid;place-items:center;color:var(--fg2);cursor:pointer;transform:rotate(90deg)}
.poh .sdi{margin-left:auto}
.pop.pz,.pop.st{height:440px}.pmain{display:flex;flex-direction:column;flex:1;min-height:0}
.pob{display:grid;grid-template-columns:1fr 1fr;flex:1;min-height:0}.pob>.sdcol,.pbr>.sdcol{overflow-y:auto;min-height:0}.pbr>.sdcol{flex:1}
.pob>.sdcol>.sdt,.pob>.sdcol .c3>.sdt{position:sticky;top:-8px;z-index:1;background:var(--bg);margin-top:-8px;padding-top:8px;min-height:40px}
.pop .sdcol .sds,.pop .pbr .sbx{position:sticky;top:0;z-index:1;box-shadow:0 -8px 0 var(--bg),0 4px 0 var(--bg)}.pop .pbr .sbx{background:var(--bg)}.pop .sdcol .sds{background:var(--bg)}
.sdcol{display:flex;flex-direction:column;gap:2px;padding:8px;min-width:0}.pob>.sdcol+.sdcol{border-left:1px solid var(--line)}
.sdt{display:flex;align-items:center;min-height:32px;margin:0 0 4px;padding:0 2px 0 8px;box-sizing:border-box;font:600 11px/16px Inter;letter-spacing:.05em;text-transform:uppercase;color:var(--fg3)}
.sdi{margin-left:auto;width:28px;height:28px;border:0;background:none;border-radius:6px;color:var(--fg3);display:grid;place-items:center;cursor:pointer}.sdi:hover{background:var(--muted);color:var(--fg)}
.sds{display:flex;align-items:center;gap:8px;height:32px;border:1px solid var(--focus);box-shadow:inset 0 0 0 1px var(--focus);border-radius:8px;padding:0 4px 0 10px;color:var(--fg);font-size:14px;margin:0 0 4px}
.sds .sq{font-weight:400}.sdq{margin-left:auto;width:24px;height:24px;border:0;background:none;border-radius:6px;color:var(--fg3);display:grid;place-items:center}
.so{display:flex;align-items:center;gap:10px;min-height:48px;box-sizing:border-box;padding:8px;border-radius:8px;cursor:pointer}
.so:hover{background:#FAFAFA}
.so .oi{width:28px;height:28px;border-radius:8px;background:#FAFAFA;color:var(--fg3);display:grid;place-items:center;flex:none}
.mt{display:grid;place-items:center;border-radius:8px;flex:none;width:28px;height:28px}

.mt.t-blue{background:#E7EFFD;color:#1F4FB8}.mt.t-yellow{background:#FFF3DC;color:#8A5300}
.mt.t-green{background:#E8F5EC;color:#1B7542}
.so .ot{flex:1;min-width:0;display:flex;flex-direction:column}
.so .o1{font:500 14px/20px Inter;color:var(--fg);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.so .o2{font:400 12px/16px Inter;color:var(--fg3);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.so .ok{color:var(--fg);display:inline-flex;visibility:hidden}
.so.sys .o1{font-weight:600}.sdv{height:1px;background:var(--line);margin:4px 8px;flex:none}
.so[data-on]{background:#F5F5F5}.so[data-on] .ok{visibility:visible}.so[data-on] .o2{color:#525252}
.pz-dis{opacity:.5;cursor:not-allowed}.pz-dis:hover{background:none}
.sde{margin:auto;text-align:center;display:flex;flex-direction:column;gap:4px;padding:24px;max-width:220px}.sde b{font:600 14px/20px Inter}.sde span{font-size:13px;line-height:18px;color:var(--fg3)}
.sde .sdei{width:40px;height:40px;border-radius:50%;background:#F5F5F5;color:var(--fg3);display:grid;place-items:center;margin:0 auto 8px}
.c3{display:none;flex-direction:column;gap:2px;flex:1}.c3.on{display:flex}
.c3n{font-size:12px;line-height:16px;color:var(--fg3);padding:8px}
.pbr{display:none;flex-direction:column;flex:1;min-height:0}.pbr.on{display:flex}
.pop .bx,.pop .bn,.pop .vtb{display:none}
.ckv{display:none}.pv:not([data-ck]) .ckv[data-k=def]{display:inline}.pv:not([data-ck]) .sic .ckv[data-k=def]{display:contents}
.pv[data-theme=dark] .so[data-on],.pv[data-theme=dark][data-state=scope] .scope{background:#262626}.pv[data-theme=dark] .so:hover,.pv[data-theme=dark] .so .oi{background:#171717}
.pv[data-theme=dark] .sde .sdei{background:#262626}
"""


def css():
    C = [CSS]
    for b in BRS:
        C.append(f'.pv[data-sbr={b}] .pop.pz .bn[data-k={b}]{{display:inline}}.pv[data-sbr={b}] .pop.pz .bx[data-k={b}]{{display:inline}}'
                 f'.pv[data-sbr={b}] .pop.pz .vtb[data-b={b}]{{display:flex}}.pv[data-sbr={b}] .pop.pz .pbr .so[data-b={b}]{{background:#F5F5F5}}'
                 f'.pv[data-sbr={b}] .pop.pz .pbr .so[data-b={b}] .ok{{visibility:visible}}')
    C.append('.pv[data-sview=br] .pop.pz .pmain{display:none}.pv[data-sview=br] .pop.pz .pbr{display:flex}')
    for q in ("m", "f", "b"):
        col = {"m": ".cm", "f": ".c3", "b": ".pbr .sdcol"}[q]
        C.append(f'.pv[data-sq={q}] .pop.pz {col} .sds.sf[data-sq={q}]{{display:flex}}.pv[data-sq={q}] .pop.pz {col} > .sdt{{display:none}}')
    C.append('.sbx{display:flex;align-items:center;gap:8px;height:32px;box-sizing:border-box;border:1px solid var(--line2);border-radius:8px;padding:0 10px;color:var(--fg3);font-size:14px;margin:0 0 4px;cursor:text}'
             '.pv[data-sq=b] .pop.pz .pbr .sbx{display:none}')
    for m in MODS:
        # nền theo module đang xem (rê chuột hoặc bấm); dấu ✓ theo phạm vi đang áp (data-ck)
        C.append(f'.pv[data-smod={m}] .pop.pz .so[data-m={m}]{{background:#F5F5F5}}')
    C.append('.pv:not([data-ck]) .pop.pz .so.vtb[data-b=hcm] .ok{visibility:visible}')
    for c in combos():
        if c[1] != "vt":
            C.append(f'.pv[data-ck="{ckey(*c)}"] .pop.pz .cm .so[data-m={c[1]}] .ok{{visibility:visible}}')
    C.append('.pv[data-smod=vt] .pop.pz .c3[data-k=vt]{display:flex}')
    for (m, b) in FAC:
        C.append(f'.pv[data-smod={m}][data-sbr={b}] .pop.pz .c3[data-k="{m}-{b}"]{{display:flex}}')
    for c in combos():
        k = ckey(*c)
        C.append(f'.pv[data-ck="{k}"] .pop.pz .so[data-ck="{k}"]{{background:#F5F5F5}}.pv[data-ck="{k}"] .pop.pz .so[data-ck="{k}"] .ok{{visibility:visible}}')
        C.append(f'.pv[data-ck="{k}"] .ckv[data-k="{k}"]{{display:inline}}.pv[data-ck="{k}"] .sic .ckv[data-k="{k}"]{{display:contents}}')
    return "\n".join(C)


def proto():
    P = [{"sel": ".clp,[data-live-sb] .lg", "state": "slim", "toggle": True},
         {"sel": ".scope", "state": "scope", "toggle": True, "set": {"sbr": "hcm", "smod": "bd", "sview": "main", "sq": "none"}},
         {"sel": ".pop.pz .lk", "set": {"sview": "br", "sq": "none"}}, {"sel": ".pop.pz .pbk", "set": {"sview": "main", "sq": "none"}},
         {"sel": ".pop.pz .cm .sdi", "set": {"sq": "m"}}, {"sel": ".pop.pz .c3 .sdi", "set": {"sq": "f"}},
         {"sel": ".pop.pz .pbr .sbx", "set": {"sq": "b"}}, {"sel": ".pop.pz .sdq", "set": {"sq": "none"}}]
    for b in BRS:
        P.append({"sel": f'.pop.pz .pbr .so[data-b={b}]', "set": {"sbr": b, "sview": "main"}})
        P.append({"sel": f'.pop.pz .so.vtb[data-b={b}]', "state": "default", "set": {"smod": "vt", "ck": ckey(b, "vt", None)}})
    for m in ("bd", "dau"):
        P.append({"sel": f'.pop.pz .so[data-m={m}]', "set": {"smod": m, "sq": "none"}})
        P.append({"sel": f'.pop.pz .cm .so[data-m={m}]', "hover": True, "set": {"smod": m}})
    P.append({"sel": '.pop.pz .cm .so.vtb', "hover": True, "set": {"smod": "vt"}})  # rê Vận tải → cột phải báo không chia cơ sở
    for c in combos():
        if c[1] != "vt":
            P.append({"sel": f'.pop.pz .c3 .so[data-ck="{ckey(*c)}"]', "state": "default", "set": {"ck": ckey(*c)}})
    return P
