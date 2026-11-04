#!/usr/bin/env python3
"""Rà lại vòng 3 của component Base sau khi foundation đổi: mỗi dòng so Đã duyệt → Foundation mới → Gap.

Không đụng thư mục đã duyệt: tạo `_work/{slug}-r3/` (tiền lệ sidebar-navigation-r2).
  python3 _scripts/ds-round3.py <slug> [...]     # dựng lại page + check + gap + trang review
  python3 _scripts/ds-round3.py --all
Nguồn "đã duyệt": check.json gần nhất + answers.json của `_work/{slug}/` (hoặc approved-answers.json trong -r3);
trang chưa từng chọn thì lấy bộ có sẵn (BASE[slug]["preset"]) và ghi rõ.
"""
import importlib.util
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / "design-system/components/_work"
sys.path.insert(0, str(ROOT / "_scripts"))
spec = importlib.util.spec_from_file_location("chk", ROOT / "_scripts/ds-foundation-check.py")
chk = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chk)

# own = class thuộc component; phần còn lại trên trang là khung màn demo hoặc component khác (đối chiếu ở trang riêng)
BASE = {
    "buttons": {"preset": "figma", "own": {".bt": "Nút", ".spn": "Spinner", ".hitnote": "Ghi chú vùng chạm"},
                "figma": {"url": "https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=6657-163199", "label": "Section Buttons trên Figma"},
                "decided_in_review": {"var.color-action-primary-pressed.base": "Đã quyết ở bước Review (DEC-351)", "var.color-bg-error-solid_hover.base": "Đã quyết ở bước Review (DEC-351)"},
                "css_append": ("[data-V=b] .bt.ter.h{background:var(--color-bg-selected)}"  # DEC-351
                               "[data-V=b] .bt.dz.ter.h{background:var(--color-bg-error-primary_hover)}"
                               "[data-V=b] .bt.dz.ter.p{background:var(--color-bg-error-primary_pressed);color:var(--color-text-error-primary_pressed)}"
                               "[data-D2=b] .bt.dz.sec.p{color:var(--color-text-error-primary_pressed)}"
                               ".bt.lkg.h{color:var(--color-text-secondary)}"
                               ".bt.ld{color:var(--color-text-tertiary_strong)!important}"
                               "[data-V=b] .bt.lkg.ld{color:var(--color-text-tertiary)!important}"),
                "css_patch": [(".bt.dz.pri.h,.bt.dz.pri.p{background:var(--color-bg-error-solid_hover)",  # DEC-349
                               ".bt.dz.pri.p{background:var(--color-bg-error-solid_pressed)}.bt.dz.pri.h{background:var(--color-bg-error-solid_hover)")]},
    "input": {"preset": "rec", "own": {".ctl": "Ô nhập", ".ad": "Khối gắn liền", ".ab": "Nút trong ô", ".lb": "Nhãn", ".hn": "Gợi ý",
                                       ".fe": "Lỗi", ".f": "Field", ".nb": "Bước số", ".ob": "Ô OTP (nút)", ".otp": "OTP", ".pc": "Mật khẩu",
                                       ".tg": "Tag trong ô"}},
    "select": {"preset": "rec", "patch": "select_round2", "own": {".ctl": "Ô chọn", ".caret": "Mũi tên", ".mi": "Dòng menu", ".mn": "Menu", ".msr": "Ô tìm menu",
                                        ".lb": "Nhãn", ".hn": "Gợi ý", ".fe": "Lỗi", ".f": "Field", ".mem": "Dòng thành viên",
                                        ".dot": "Chấm", ".rd": "Radio", ".ro": "Dòng nhiều thông tin", ".scb": "Thanh cuộn",
                                        ".sht": "Bottom sheet"}},
    "multiselect": {"preset": "rec", "own": {".ctl": "Ô chọn", ".cbx": "Checkbox", ".lb": "Nhãn", ".hn": "Gợi ý", ".f": "Field",
                                             ".mem": "Dòng thành viên", ".dot": "Chấm", ".mi": "Dòng menu", ".mn": "Menu",
                                             ".mft": "Chân menu", ".more": "+N", ".msr": "Ô tìm menu", ".oc": "Ô đếm",
                                             ".sht": "Bottom sheet", ".tg": "Tag", ".tw": "Khung tag"}},
    "tag": {"preset": "rec", "own": {".tg": "Tag", ".cbx": "Checkbox", ".dot": "Chấm", ".flag": "Cờ", ".tags": "Nhóm tag"}},
    "form-controls": {},
    "badge-avatar": {"css_patch": [(".fa.xl .fat{font-size:20px;line-height:28px}", ".fa.xl .fat{font-size:20px;line-height:30px}")],  # DEC-358
                     "values_patch": [(".fa.xl .fat", "line-height", 30), (".fa.lg .fat", "line-height", 28)]},
    "tooltip": {},
    "alert-notification": {},
}
# dòng "thêm token mới": tên đề xuất hiện trên trang, người dùng chốt rồi mới thêm vào tokens.json
FULL_WIDTH = {"token": "100% khung chứa, không tạo token", "value": "100%", "opts": ["Dùng 100% khung chứa, không tạo token"]}
PROPOSE = {
    ".bt.max-width.both": {"token": "button/max-width"},
    ".tg.max-width.both": {"token": "tag/max-width"},
    ".mn.min-width.both": {"token": "menu/min-width"},
    ".mn.max-height.both": {"token": "menu/max-height"},
    "toast.width.web": {"token": "toast/width"},
    "badge-·-label.max-width.web": {"token": "badge/label-max-width"},
    "label.max-width.web": {"token": "control-label/max-width"},
    "toast.width.mobile": FULL_WIDTH,
    "checkbox-label-mobile.width.mobile": FULL_WIDTH,
    "group-item.width.mobile": FULL_WIDTH,
}
MENU_ROWS = "".join(f'<div class="mi"><span class="ml">Cảng số {i}</span></div>' for i in range(1, 15))
MENU_DEMOS = [("Menu ít mục, chữ ngắn · rộng tối thiểu 200", '<div class="mn" data-limit="mn-min" style="position:static;width:max-content"><div class="mi"><span class="ml">Có</span></div><div class="mi"><span class="ml">Không</span></div></div>', 200),
              ("Menu nhiều mục · cao tối đa 320, cuộn trong menu", f'<div class="mn" data-limit="mn-max" style="position:static;width:240px;overflow:auto">{MENU_ROWS}</div>', None)]
LONG = "Xác nhận hoàn tất giao container lạnh cho khách hàng Cát Lái trong ca đêm"
BADGE_ICON = '<svg class="fi" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.25" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 6h11v10H3zM14 9h4l3 3v4h-7"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/></svg>'
# ô demo cho giới hạn rộng/cao: màn, [(tiêu đề, html, thước px)], dòng → chỗ soi
DEMOS = {
    "input": ("variants-web", [("Chữ dài · tag trong ô rộng tối đa 200", f'<span class="tg t-sm" data-limit="tg" style="white-space:nowrap;overflow:hidden">{LONG}</span>', 200)], {".tg.max-width.both": "[data-limit=tg]"}),
    "tag": ("variants-web", [("Chữ dài · rộng tối đa 200", f'<span class="tg t-md" data-limit="tg"><span class="tl nl">{LONG}</span></span>', 200)], {".tg.max-width.both": "[data-limit=tg]"}),
    "multiselect": ("variants-web", [("Chữ dài · tag rộng tối đa 200", f'<span class="tg t-sm" data-limit="tg"><span class="tl">{LONG}</span></span>', 200), *MENU_DEMOS],
                    {".tg.max-width.both": "[data-limit=tg]", ".mn.min-width.both": "[data-limit=mn-min]", ".mn.max-height.both": "[data-limit=mn-max]"}),
    "select": ("variants-web", MENU_DEMOS, {".mn.min-width.both": "[data-limit=mn-min]", ".mn.max-height.both": "[data-limit=mn-max]"}),
    "badge-avatar": ("list-web", [("Chữ dài · nhãn rộng tối đa 160", f'<span class="fb pc md c-blue" data-limit="fb"><span class="flw"><span class="fl">{LONG}</span></span></span>', 160),
                     ("Icon theo màu · Gray, Teal, Purple, Orange", '<span style="display:flex;gap:8px">' + "".join(f'<span class="fb pc md c-{c}"><span class="fdw iw">{BADGE_ICON}</span><span class="flw"><span class="fl">Đang chạy</span></span></span>' for c in ("gray", "teal", "purple", "orange")) + '</span>', None)],
                     {"badge-·-label.max-width.web": "[data-limit=fb] .flw"}),
    "form-controls": ("var-web", [("Chữ dài · nhãn rộng tối đa 360", f'<label class="cl sm" data-limit="cl"><span class="cb sm off" role="checkbox" aria-checked="false"></span><span class="lt"><span class="lb">{LONG}</span><span class="hn">{LONG}</span></span></label>', 360)],
                      {"label.max-width.web": "[data-limit=cl]"}),
    "tooltip": ("var-web", [("Chữ dài · Supporting rộng tối đa 320", f'<span class="tt a-bottom sup p-top" role="tooltip" data-limit="tt"><b>Tổng trọng lượng</b><span>{LONG}</span></span>', 320)],
                {"tooltip-supporting.max-width.web": "[data-limit=tt]"}),
}
# dòng trên CSS nhưng không phần tử nào dùng ở tổ hợp đã chốt: không hỏi người dùng
DEAD = {"select": {".sht-.mi.min-height.both": "luật thừa: bottom sheet dùng dòng .ro, không có .mi",
                   ".rd.on.border.both": "radio chỉ hiện ở phương án D1=c; tổ hợp đã chốt D1=b không có radio"}}
GAP = {
    "none": "Không gap",
    "moved": "Foundation đổi số",
    "renamed": "Token đổi tên",
    "unbuilt": "Token đã duyệt chưa có",
    "pending": "Đã duyệt, trang chưa áp",
    "exception": "Ngoại lệ đã duyệt",
    "open": "Chưa từng quyết",
}


def run(*args):
    return subprocess.run([sys.executable, *args], cwd=ROOT, capture_output=True, text=True, stdin=subprocess.DEVNULL)


def label(part, own):
    m = [c for c in own if re.search(re.escape(c) + r"(?![\w-])", part or "")]
    return own[max(m, key=lambda c: (part.find(c), len(c)))] + f" ({part})" if m else None


def select_round2(p):
    """Select: user chốt vòng 1 trên trang rà lại 03/11, D4 thêm phương án theo loại trường. Giữ ở đây để chạy lại không mất."""
    d4 = next(d for d in p["decisions"] if d["id"] == "D4")
    for o in d4["options"]:
        o.pop("rec", None)
    d4["options"].append({"label": "Theo loại trường: ngắn cùng dòng, dài xuống dòng",
                          "desc": "Chọn khi dùng component, không tự đo chữ: quận, mã, chức vụ cùng dòng; địa chỉ, ghi chú xuống dòng hai.",
                          "rec": True})
    pick = {"D1": "b", "D2": "c", "D3": "a", "D4": "c", "D5": "b", "D6": "a", "D7": "a"}
    next(x for x in p["presets"] if x["id"] == "rec")["pick"]["D4"] = "c"
    p["round"] = "preview"
    p["preview"] = {"version": 2, "pick": pick, "blocks": [],
                    "changes": "Theo lựa chọn vòng 1: D5 đổi sang ô tìm đầu menu. D4 thêm kiểu theo loại trường, xem ở màn Biến thể, nhóm Chữ phụ theo loại trường. D2 và D4 theo đề xuất."}
    p["css"] += ("\n.pv[data-D4=c] .mi.sup-below:has(.ms){padding-top:6px;padding-bottom:6px}"
                 "\n.pv[data-D4=c] .mi.sup-below .ml{white-space:normal}"
                 "\n.pv[data-D4=c] .mi.sup-below .ms{display:block;margin:0;font-size:12px;line-height:18px}")
    def row(name, sub, below):
        return (f'<div class="mi{" sup-below" if below else ""}"><span class="rd"></span><span class="ml">{name}'
                f'<span class="ms">{sub}</span></span><span class="ck"></span></div>')
    cols = [("Inline · trường ngắn", [("Cảng Cát Lái", "Thủ Đức", 0), ("ICD Phước Long", "Thủ Đức", 0), ("Cảng Hiệp Phước", "Nhà Bè", 0)]),
            ("Below · trường dài", [("Cảng Cát Lái", "Đường Nguyễn Thị Định, Phường Cát Lái, TP. Thủ Đức, TP.HCM", 1),
                                    ("Cảng Cái Mép (TCIT)", "Khu cảng Cái Mép, Phú Mỹ, Bà Rịa – Vũng Tàu", 1)]),
            ("Inline · tên dài, hết chỗ thì cắt", [("Cảng Container Quốc tế Cái Mép – Thị Vải (TCIT)", "Phú Mỹ", 0)])]
    # D5=b: ô tìm nằm trong menu, kính lúp trên ô thành thừa
    search_ic = re.compile(r'(<div class="ctl[^"]*"[^>]*><span class="ic")(><svg[^>]*>(?:(?!</svg>).)*?(?:cx="11"|m21 21|M21 21|L21 21)(?:(?!</svg>).)*?</svg></span>)')
    for sc in p["screens"]:
        sc["html"] = search_ic.sub(r'\1 data-show="D5:a"\2', sc["html"])
    for sc in p["screens"]:
        if sc["id"] not in ("variants-web", "variants-app"):
            continue
        n = 3 if sc["id"] == "variants-web" else 1
        cells = "".join(f'<div class="vgc"><span class="cap">{c}</span><div class="mn">{"".join(row(*r) for r in rs)}</div></div>' for c, rs in cols)
        block = (f'<div class="vgs" data-show="D4:c"><h3>Chữ phụ theo loại trường (D4)<small>Thuộc tính Supporting position</small></h3>'
                 f'<div class="vgr" style="grid-template-columns:repeat({n},minmax(0,1fr))">{cells}</div></div>')
        anchor = '<div class="vgs"><h3>Option nhiều thông tin (D2)'
        if anchor not in sc["html"]:
            sys.exit("select_round2: không thấy nhóm D2 trong " + sc["id"])
        sc["html"] = sc["html"].replace(anchor, block + anchor, 1)


def apply_comment_fixes(slug, dst):
    """Góp ý trên trang rà lại: `_work/{slug}-r3/comment_fixes.py` giữ bản sửa, chạy lại script không mất, mỗi góp ý hoàn lại được riêng."""
    f = dst / "comment_fixes.py"
    if not f.exists():
        return
    sp = importlib.util.spec_from_file_location(f"cmt_{slug}", f)
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    pg, before = dst / "page.json", dst / ".page-before.json"
    p = json.loads(pg.read_text())
    p["preview"].update(m.PREVIEW)
    pg.write_text(json.dumps(p, ensure_ascii=False, indent=1))
    for cid, fix in m.FIXES:
        before.write_text(pg.read_text())
        p = json.loads(pg.read_text())
        fix(p)
        pg.write_text(json.dumps(p, ensure_ascii=False, indent=1))
        r = run("_scripts/ds-snap.py", "change", f"{slug}-r3", str(before), cid)
        if r.returncode:
            sys.exit(f"{slug}: ds-snap {cid}: {r.stdout} {r.stderr}")
    before.unlink()


# Dòng màu khai từ CSS: `values` gốc của các trang này chưa từng khai màu nên nhóm Màu ở tab 3 trống
COLOR_FROM_CSS = {"badge-avatar": {".fb": "Badge", ".fa": "Avatar", ".fg": "Avatar group", ".flg": "Avatar label", ".fadd": "Avatar add",
                                   ".fst": "Status", ".fup": "Upload"},
                  "tag": None, "select": None, "multiselect": None, "input": None}  # None = dùng BASE[slug]["own"]
COLOR_DECL = re.compile(r"(?:^|;)\s*(color|background(?:-color)?|border(?:-[a-z]+)*|outline(?:-color)?|fill|stroke)\s*:\s*([^;]+)")


def color_values(p, slug):
    """Khai 1 dòng values cho mỗi khai báo màu của component trong CSS, role theo công dụng (prop), không theo tên token."""
    if slug not in COLOR_FROM_CSS:
        return 0
    own = COLOR_FROM_CSS[slug] or BASE[slug].get("own") or {}
    d = json.loads((ROOT / "design-system/tokens.json").read_text())["collections"]
    names = {chk.css_var(n)[6:-1]: n for n in d["Semantic"]["color"]}
    pick = (p.get("preview") or {}).get("pick") or {}
    rules = VAR_ONLY.sub("", re.sub(r"/\*.*?\*/", "", p.get("css") or "", flags=re.S))
    p["values"] = [v for v in p["values"] if not v.get("fromCss")]  # chạy lại không nhân đôi
    have = {(v.get("sel"), v.get("prop")) for v in p["values"]}
    new = tokens_now()
    n = 0
    for sel, body in re.findall(r"([^{}]+)\{([^{}]*)\}", rules):
        sel = " ".join(sel.split())
        parts = []
        for one in sel.split(","):
            one = one.strip()
            if not any(re.search(re.escape(c) + r"(?![\w-])", one) for c in own) or DEMO_SEL.search(one):
                continue
            if any(k in pick and pick[k] != x for k, x in re.findall(r"\[data-(D\d+|V)=(\w+)\]", one)):
                continue
            parts.append(re.sub(r"^\[data-", ".pv[data-", one))
        plain = [x for x in parts if not re.search(r":(hover|focus|active)", x)]
        parts = plain or parts
        if not parts:
            continue
        decl = COLOR_DECL.findall(body)
        tok = {}
        for prop, val in decl:
            m = re.search(r"var\(--([\w-]+)", val)
            tok[prop] = names.get(m.group(1)) if m else None
        on = tok.get("background") or tok.get("background-color")
        for prop, val in decl:
            m = re.search(r"var\(--([\w-]+)", val)
            hx = re.search(r"#[0-9a-fA-F]{3,8}\b", val)
            value = names.get(m.group(1)) if m else (hx.group(0) if hx else None)
            if not value:
                continue
            fg = value.startswith("color/fg/") or value.endswith("/fg")
            if prop == "color":
                row = {"prop": "color", "role": "icon" if value.startswith("color/fg/") else "text"}
            elif prop.startswith("background"):
                row = {"prop": "background", "role": "icon" if fg else "fill"}
            elif prop in ("fill", "stroke"):
                row = {"prop": prop, "role": "icon"}
            else:
                row = {"prop": "border-color", "role": "border"}
                if prop.startswith("outline"):
                    row["cssProp"] = "outline-color"
                elif prop not in ("border", "border-color"):
                    side = re.match(r"border-(top|right|bottom|left)", prop)
                    if not side:
                        continue
                    row["cssProp"] = f"border-{side.group(1)}-color"
            s = ",".join(parts)
            if (s, row["prop"]) in have:
                continue
            have.add((s, row["prop"]))
            row |= {"part": label(s, own) or s, "sel": s, "platform": "Both", "value": value, "fromCss": True}
            if m:  # value = mã màu để thẻ có ô màu thật, token = token CSS đang dùng (không gợi ý đổi sang token trùng số)
                row["token"] = value
                hexv = final("--" + m.group(1), new, "base")
                if hexv and hexv.startswith("#"):
                    row["value"] = hexv
            if on and prop == "color" and not re.search(r"is-dis|\.dis\b|disabled", s):  # chữ disabled được miễn tương phản (WCAG 1.4.3)
                row["on"] = on
            p["values"].append(row)
            n += 1
    return n


def init(slug):
    src, dst, cfg = WORK / slug, WORK / f"{slug}-r3", BASE[slug]
    dst.mkdir(exist_ok=True)
    p = json.loads((src / "page.json").read_text())
    old_ans = json.loads((src / "answers.json").read_text()) if (src / "answers.json").exists() else {}
    if (dst / "approved-answers.json").exists():
        old_ans.update(json.loads((dst / "approved-answers.json").read_text()))
    for a, b in cfg.get("css_patch") or []:
        if a not in p["css"]:
            sys.exit(f"{slug}: css_patch không khớp: {a}")
        p["css"] = p["css"].replace(a, b)
    p["css"] += cfg.get("css_append", "")
    for sel, prop, val in cfg.get("values_patch") or []:
        hit = [v for v in p["values"] if v.get("sel") == sel and v.get("prop") == prop]
        if not hit:
            sys.exit(f"{slug}: values_patch không khớp: {sel} {prop}")
        for v in hit:
            v["value"] = val
    p["round"] = "foundation"
    p["slug"] = f"{slug}-r3"
    p["title"] = f"{p.get('component') or slug} · Rà vòng 3"
    p.pop("reviews", None)
    p.pop("dsStale", None)
    if cfg.get("preset"):
        preset = next(x for x in p["presets"] if x["id"] == cfg["preset"])
        p["preview"] = {"version": 1, "pick": preset["pick"], "blocks": [],
                        "changes": f"Chưa từng chọn trên trang: khoá theo bộ {preset.get('label') or cfg['preset']}."}
        p["values"] = [{"part": "seed", "prop": "gap", "platform": "Both", "value": 8, "sel": ".pv"}]
    if cfg.get("patch"):
        globals()[cfg["patch"]](p)
    (dst / "page.json").write_text(json.dumps(p, ensure_ascii=False, indent=1))
    apply_comment_fixes(slug, dst)
    keep = {k: v for k, v in old_ans.items() if k.startswith("brainstorm-")}
    if (dst / "answers.json").exists():  # lựa chọn đã lưu ngay trên trang rà lại không được mất khi chạy lại
        keep |= json.loads((dst / "answers.json").read_text())
    (dst / "answers.json").write_text(json.dumps(keep, ensure_ascii=False, indent=1))
    if cfg.get("preset"):
        r = run("_scripts/ds-foundation-check.py", str(dst), "--declare")
        if r.returncode not in (0, 1):
            sys.exit(r.stderr)
        p = json.loads((dst / "page.json").read_text())
        p["values"] = [v for v in p["values"] if v.get("part") != "seed"] or p["values"]
        (dst / "page.json").write_text(json.dumps(p, ensure_ascii=False, indent=1))
    p = json.loads((dst / "page.json").read_text())
    if color_values(p, slug):
        (dst / "page.json").write_text(json.dumps(p, ensure_ascii=False, indent=1))
    return old_ans


def approved_of(old, ans):
    """(kind, token, value, note) của dòng đã duyệt; kind None = chưa quyết."""
    a = ans.get("foundation-" + old["id"]) or {}
    res = chk.resolve(old, a)
    note = (a.get("note") or "").strip()
    if res["kind"] == "pending":
        return None, None, None, note
    if res["kind"] == "token":
        return "token", res.get("token"), res.get("value", old.get("value")), note
    return res["kind"], res.get("token"), res.get("value", old.get("value")), note


def color_now(tk, theme):
    return {n: hx for hx, ls in tk["colors"][theme].items() for n, _ in ls}


TOKEN_BLOCK = re.compile(r"(?:(?<=\})|^)\s*(\.pv(?:\[data-(?:theme=dark|platform=mobile)\])?)\{((?:\s*--[\w-]+\s*:[^;{}]+;?)+)\s*\}")
VAR_ONLY = re.compile(r"[^{}]+\{(?:\s*--[\w-]+\s*:[^;{}]+;?)+\s*\}")
DEMO_SEL = re.compile(r"(^|[\s,>])\.(vg|vgs|vgr|vgc|vt|vh|vl|vnote|vgrid|pg|ph|sec-t|tbl|kv|foot|form|fld|dlg|mcard|mbar|hscroll|row|acts|chip)(?![\w-])")


def var_blocks(css, sels):
    """scope -> {biến: giá trị}. sels: selector -> scope."""
    out = {"base": {}, "dark": {}, "mobile": {}}
    for sel, body in TOKEN_BLOCK.findall(css) if sels is None else []:
        scope = {".pv": "base", ".pv[data-theme=dark]": "dark", ".pv[data-platform=mobile]": "mobile"}[sel]
        out[scope].update({k: v.strip() for k, v in re.findall(r"(--[\w-]+)\s*:\s*([^;{}]+)", body)})
    return out


def tokens_now():
    css = re.sub(r"/\*.*?\*/", "", (ROOT / "design-system/tokens.css").read_text(), flags=re.S)
    css = re.sub(r"@media[^{]*\{(?:[^{}]*\{[^{}]*\})*[^{}]*\}", "", css)
    out = {"base": {}, "dark": {}, "mobile": {}}
    for sel, body in re.findall(r"([^{}]+)\{([^{}]*)\}", css):
        sel = " ".join(sel.split())
        scope = "dark" if sel == '[data-theme="dark"]' else "mobile" if sel == '[data-platform="mobile"]' else \
            "base" if sel.startswith(":root") or sel == '[data-theme="light"]' else None
        if scope:
            out[scope].update({k: v.strip() for k, v in re.findall(r"(--[\w-]+)\s*:\s*([^;{}]+)", body)})
    return out


def final(name, blocks, scope, depth=0):
    """Giá trị cuối của biến ở một phạm vi; None nếu không có."""
    v = blocks[scope].get(name, blocks["base"].get(name))
    if v is None or depth > 8:
        return v
    def sub(m):
        return final(m.group(1), blocks, scope, depth + 1) or m.group(0)
    return " ".join(re.sub(r"var\((--[\w-]+)[^()]*\)", sub, v).lower().split())


def add_demos(page, slug):
    """Ô demo chữ dài, kèm thước đúng số giới hạn, để thấy giới hạn trên hình."""
    scr = page["screens"]
    if slug == "buttons":  # bảng biến thể đã có khối Chữ dài: chỉ thêm thước và chỗ soi
        h = scr[0]["html"]
        mark, btn = '<div class="vg"><button class="bt pri md " ><span class=tx>Xác nhận hoàn tất', '<button class="bt pri md " ><span class=tx>Xác nhận hoàn tất'
        if mark not in h:
            sys.exit("buttons: không thấy khối Chữ dài")
        scr[0]["html"] = h.replace(mark, ruler(240) + mark.replace(btn, btn.replace('md " >', 'md " data-limit="bt">')))
        return {".bt.max-width.both": "[data-limit=bt]"}
    if slug not in DEMOS:
        return {}
    sid, blocks, ats = DEMOS[slug]
    sc = next(x for x in scr if x["id"] == sid)
    sc["html"] += "".join(f'<div style="padding:16px 24px;display:flex;flex-direction:column;gap:8px;align-items:flex-start;background:var(--color-bg-primary)">'
                          f'<div style="font:500 12px/16px var(--font-body);color:var(--color-text-tertiary)">{t}</div>{ruler(px) if px else ""}{html}</div>' for t, html, px in blocks)
    return ats


def ruler(px):
    return (f'<div style="width:{px}px;box-sizing:border-box;border:1px solid var(--color-text-tertiary);border-top:0;height:6px;margin-bottom:2px"></div>'
            f'<div style="font:500 11px/14px var(--font-body);color:var(--color-text-tertiary);margin-bottom:6px">Thước {px}</div>')


def embed_now(css):
    """Thay bản token nhúng trong trang bằng tokens.css hiện tại, để mọi bước và mọi chế độ vẽ theo số mới. Biến cục bộ của trang giữ nguyên."""
    new, done = tokens_now(), set()
    def sub(m):
        sel = m.group(1)
        scope = {".pv": "base", ".pv[data-theme=dark]": "dark", ".pv[data-platform=mobile]": "mobile"}[sel]
        vals = {}
        for k, v in re.findall(r"(--[\w-]+)\s*:\s*([^;{}]+)", m.group(2)):
            if k in new[scope]:
                vals[k] = new[scope][k]
            elif scope == "base" or not any(k in new[x] for x in new):
                vals[k] = v.strip()  # biến cục bộ hoặc token đã bỏ; ở Dark/Mobile mà gốc còn thì thừa kế gốc
        if scope not in done:
            vals = {**new[scope], **vals}
            done.add(scope)
        return m.group(0)[:m.start(1) - m.start(0)] + sel + "{" + " ".join(f"{k}: {v};" for k, v in vals.items()) + "}"
    out = TOKEN_BLOCK.sub(sub, css)
    after = var_blocks(out, None)
    bad = [(v, sc) for sc in new for v in new[sc] if final(v, after, sc) != final(v, new, sc)]
    if bad or len(done) < 2:
        sys.exit(f"embed_now: trang còn lệch tokens.css: {bad[:5]} · khối đã thay: {done}")
    return out


def var_rows(page, own):
    """Bản token nhúng trong trang so với tokens.css hiện tại, chỉ biến component đang dùng."""
    css = page.get("css") or ""
    old = var_blocks(css, None)
    new = tokens_now()
    ledger = json.loads((ROOT / "design-system/components/_token-ledger.json").read_text()).get("colorRename") or {}
    names = {}
    d = json.loads((ROOT / "design-system/tokens.json").read_text())["collections"]
    for n in list(d["Platform"]["vars"]) + list(d["Semantic"]["color"]):
        names[chk.css_var(n)[6:-1]] = n
    rules = VAR_ONLY.sub("", re.sub(r"/\*.*?\*/", "", css, flags=re.S))
    used = {}
    for sel, body in re.findall(r"([^{}]+)\{([^{}]*)\}", rules):
        sel = " ".join(sel.split())
        if DEMO_SEL.search(sel) and not (own and any(re.search(re.escape(c) + r"(?![\w-])", sel) for c in own)):
            continue
        if own and not any(re.search(re.escape(c) + r"(?![\w-])", sel) for c in own):
            continue
        parts = []
        for one in sel.split(","):  # bỏ phần chỉ thuộc phương án đã loại
            pick = page["preview"].get("pick") or {}
            if not any(k in pick and pick[k] != x for k, x in re.findall(r"\[data-(D\d+|V)=(\w+)\]", one)):
                parts.append(re.sub(r"^\[data-", ".pv[data-", one.strip()))  # thuộc tính nằm ngay trên .pv
        if not parts:
            continue
        for v in re.findall(r"var\((--[\w-]+)", body):
            used.setdefault(v, []).extend(parts)
    rows = []
    for v, sel in sorted(used.items()):
        if not any(v in old[sc] for sc in old):  # biến cục bộ của component, không phải token
            continue
        gone = not any(v in new[sc] for sc in new)
        for scope, plat, theme in (("base", "Web", "Light"), ("mobile", "Mobile", "Light"), ("dark", "Both", "Dark")):
            a, b = final(v, old, scope), final(v, new, scope)
            if gone and scope != "base":
                continue
            if not gone and (a == b or a is None or b is None):
                continue
            if scope != "base" and final(v, old, "base") == a and final(v, new, "base") == b:
                continue  # phạm vi này chỉ thừa kế dòng gốc
            tok = names.get(v[2:]) or v[2:]
            ren = ledger.get(tok) if gone else None
            ren = ren.get("to") if isinstance(ren, dict) else ren
            to = {"token": ren or tok, "value": b, "css": chk.css_var(ren) if ren else b} if (ren or not gone) else None
            pre = v[2:].split("-")[0]
            group = {"color": "color", "type": "type", "font": "type", "radius": "radius", "shadow": "effect", "icon": "icon",
                     "width": "grid", "duration": "spacing", "easing": "spacing"}.get(pre, "spacing")
            rows.append({"id": f"var.{v[2:]}.{scope}", "part": f"Token {tok}", "prop": "giá trị token", "platform": "Both" if group == "color" else plat, "size": "",
                         "state": "", "theme": theme, "value": a, "sel": ".pv[data-theme=dark]" if scope == "dark" else ".pv:not([data-theme=dark])" if group == "color" else ".pv", "at": ",".join(dict.fromkeys(sel))[:400].rsplit(",", 1)[0] if len(",".join(dict.fromkeys(sel))) > 400 else ",".join(dict.fromkeys(sel)), "cssProps": [v],
                         "tpl": None, "noOverride": None, "soi": None, "cat": "near", "tokens": [], "bind": None, "to": to,
                         "visible": True, "suggest": (to or {}).get("token"), "rules": [],
                         "note": (f"Token đã bỏ khỏi tokens.css" + (f", tên mới {ren}" if ren else ", chưa có tên thay")) if gone else "Foundation đã đổi số, hình trên trang đã theo số mới",
                         "group": group, "decided": False, "must": True, "appr": f"Bản trước: {a}", "gap": "renamed" if gone else "moved",
                         "gapLabel": GAP["renamed" if gone else "moved"], "isVar": True})
    return rows


def post(slug, old_ans):
    src, dst, cfg = WORK / slug, WORK / f"{slug}-r3", BASE[slug]
    r = run("_scripts/ds-foundation-check.py", str(dst), "--write")
    if not (dst / "check.json").exists():
        sys.exit(f"{slug}: {r.stdout[-400:]} {r.stderr[-400:]}")
    c = json.loads((dst / "check.json").read_text())
    old = {x["id"]: x for x in (json.loads((src / "check.json").read_text())["rows"] if (src / "check.json").exists() else [])}
    tk = chk.load_tokens()
    cols = {t: color_now(tk, t) for t in ("Light", "Dark")}
    own = cfg.get("own")
    rows, ignored = [], list(c.get("ignored") or [])
    for x in c["rows"]:
        if x["id"] in DEAD.get(slug, {}):
            ignored.append({"sel": x.get("sel"), "props": [x.get("prop")], "why": DEAD[slug][x["id"]]})
            continue
        if own:
            lb = label(x.get("part") or "", own)
            is_screen = x["cat"] == "undeclared" and str(x.get("part") or x.get("sel") or "").startswith("màn")
            if x.get("audit") and x.get("sel"):  # luật chữ/icon chỉ giữ phần thuộc component
                html = " ".join(sc.get("html") or "" for sc in json.loads((dst / "page.json").read_text())["screens"])
                mine = [z.strip() for z in x["sel"].split(",") if any(re.search(re.escape(k) + r"(?![\w-])", z) for k in own)
                        and re.search(r'class="?[^">]*\b' + re.escape(re.findall(r"\.([\w-]+)", z)[-1]) + r"\b", html)]
                if mine:
                    x["sel"] = ", ".join(mine)
                else:
                    x["audit_foreign"] = True
            if is_screen or x.pop("audit_foreign", False) or (not lb and not x.get("audit")):
                ignored.append({"sel": x.get("sel") or x.get("part"), "props": [x.get("prop")], "why": "khung màn demo hoặc component khác, không thuộc component này"})
                continue
            if lb:
                x["part"] = lb
        if x.get("audit") and re.fullmatch(r"[\d.]+/[\d.]+", str((x.get("fix") or {}).get("value"))):
            sz, lh = x["fix"]["value"].split("/")
            x["fix"]["set"] = {"font-size": f"{sz}px", "line-height": f"{lh}px"}
        if x["cat"] == "new" and x["id"] in PROPOSE:
            x["proposal"] = {"value": x.get("value"), **PROPOSE[x["id"]]}
        o = old.get(x["id"])
        kind, tok, val, note = approved_of(o, old_ans) if o else (None, None, None, "")
        mode = "Mobile" if x.get("platform") == "Mobile" else "Web"
        now = None
        if tok:
            if tok in tk["plat"]:
                now = tk["plat"][tok][mode]
            elif tok in cols[x.get("theme") or "Light"]:
                now = cols[x.get("theme") or "Light"][tok]
        exists = bool(tok) and (now is not None or tok in tk["effects"] or " " in tok or "/" not in tok)
        if not o and own:
            ap = f"Preview bộ {cfg['preset']}, chưa từng chọn: {x.get('value')}"
        elif not o:
            ap = "Dòng mới, chưa có ở lần duyệt trước"
        elif kind is None:
            ap = f"Chưa quyết: {o.get('value')}"
        elif kind == "token":
            ap = f"{tok} = {val}"
        elif kind == "new-token":
            ap = f"Giữ {val}, tạo token mới"
        else:
            ap = {"fix": f"Sửa theo luật: {tok or val}", "rule-change": f"Đổi luật, giữ {val}", "exception": f"Ngoại lệ, giữ {val}"}[kind]
        if note:
            ap += f" · ghi chú: {note}"
        if kind == "token" and tok and not exists:
            g = "renamed"
        elif kind == "token" and val == tok:  # dòng màu khai bằng tên token: còn token là còn đúng
            g = "none" if x["cat"] == "ok" else "pending"
        elif kind == "token" and now is not None and str(now).upper() != str(val).upper():
            try:
                same = float(now) == float(val)
            except (TypeError, ValueError):
                same = False
            g = "none" if same else "moved"
        elif kind == "new-token":
            g = "none" if x["cat"] == "ok" else "unbuilt"
        elif kind in ("rule-change", "exception"):
            g = "exception"
        elif kind in ("token", "fix"):
            g = "none" if x["cat"] == "ok" else "pending"
        else:
            g = "none" if x["cat"] == "ok" else "open"
        if g == "none" and x["cat"] != "ok":
            g = "pending" if kind else "open"
        x.update(appr=ap, gap=g, gapLabel=GAP[g], apprNow=now)
        if slug == "select" and re.search(r"\.sht \.mi|\.rd\.on", str(x.get("sel"))):
            x["soi"] = {"state": "open"}
        if x.get("sel") == ".ctl.is-err.is-focus":
            x["soi"] = {"add": {".ctl.is-err": "is-focus"}}
        if g == "pending" and kind == "token" and exists:  # lựa chọn cũ còn hiệu lực: không hỏi lại, xem trước theo token đã duyệt
            cssv = chk.css_var(tok) if "/" in tok else None
            x.update(cat="ok", bind={"token": tok, "css": cssv}, must=False, visible=False, to=None)
        elif g == "pending":
            x["must"] = bool(x.get("must"))
        elif g == "moved":
            x["must"] = True
        elif g in ("renamed", "exception", "none"):
            x["must"] = x["must"] if x["cat"] != "ok" and g != "exception" else False
        rows.append(x)
    rows += var_rows(json.loads((dst / "page.json").read_text()), own)
    c["rows"], c["ignored"] = rows, ignored
    cnt = {k: 0 for k in ("ok", "near", "new", "conflict", "undeclared")}
    gaps = {k: 0 for k in GAP}
    for x in rows:
        cnt[x["cat"]] = cnt.get(x["cat"], 0) + 1
        if x.get("gap"):
            gaps[x["gap"]] += 1
    if (dst / "reviews.json").exists():  # số đổi theo lựa chọn ở vòng 5: đã quyết ở đó, không hỏi lại
        for x in rows:
            if x["id"] in cfg.get("decided_in_review", {}):
                x["must"], x["note"] = False, cfg["decided_in_review"][x["id"]]
    c["counts"], c["gaps"] = cnt, gaps
    c["open"] = sum(1 for x in rows if x.get("must") or x["cat"] == "undeclared")
    (dst / "check.json").write_text(json.dumps(c, ensure_ascii=False, indent=1))
    p = json.loads((dst / "page.json").read_text())
    p["css"] = embed_now(p["css"])
    ats = add_demos(p, slug)
    if (dst / "reviews.json").exists():  # vòng 5: kết quả 3 agent review
        p["reviews"], p["round"] = json.loads((dst / "reviews.json").read_text()), "review"
        p["figma"] = cfg.get("figma")
    for x in rows:
        if x["id"] in ats:
            x["at"] = ats[x["id"]]
    (dst / "check.json").write_text(json.dumps(c, ensure_ascii=False, indent=1))
    (dst / "page.json").write_text(json.dumps(p, ensure_ascii=False, indent=1))
    r = run("_scripts/ds-component-page.py", str(dst))
    if r.returncode:
        sys.exit(f"{slug}: {r.stdout} {r.stderr}")
    p = json.loads((dst / "page.json").read_text())
    print(f"{slug}: {len(rows)} dòng · ignored {len(ignored)} · cần quyết {c['open']} · gap {({k: v for k, v in gaps.items() if v})}")


def main():
    slugs = list(BASE) if "--all" in sys.argv else [a for a in sys.argv[1:] if not a.startswith("--")]
    for s in slugs:
        post(s, init(s))


if __name__ == "__main__":
    main()
