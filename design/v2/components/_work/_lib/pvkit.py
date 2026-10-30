"""Phần dùng chung cho build.py của các trang Base (brainstorm gọn, 28/10).

tok_css(): tokens.css đổi phạm vi sang `.pv` để preview dùng thẳng biến thật (Light/Dark theo data-theme,
Web/Mobile theo data-platform của khung) — không gõ mã màu tay.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
TOKENS_CSS = ROOT / "design/v2/tokens.css"

P = {
    "navigation": '<path d="M3 11l19-9-9 19-2-8-8-2z"/>',
    "triangle-alert": '<path d="M10.3 3.9L1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/><path d="M12 9v4M12 17h.01"/>',
    "hourglass": '<path d="M5 22h14M5 2h14M17 22v-4.2a2 2 0 0 0-.6-1.4L12 12l-4.4 4.4a2 2 0 0 0-.6 1.4V22M7 2v4.2a2 2 0 0 0 .6 1.4L12 12l4.4-4.4a2 2 0 0 0 .6-1.4V2"/>',
    "circle-check": '<circle cx="12" cy="12" r="10"/><path d="M9 12l2 2 4-4"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    "image": '<rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="9" cy="9" r="2"/><path d="M21 15l-3.1-3.1a2 2 0 0 0-2.8 0L6 21"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "arrow-r": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "x": '<path d="M6 6l12 12M18 6L6 18"/>',
    "trash": '<path d="M3 6h18M8 6V4h8v2M6 6l1 14h10l1-14"/>',
    "dl": '<path d="M12 4v11M7 10l5 5 5-5"/><path d="M4 19h16"/>',
    "edit": '<path d="M4 20h4L19 9l-4-4L4 16z"/><path d="M14 6l4 4"/>',
    "more": '<circle cx="5" cy="12" r="1"/><circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/>',
    "filter": '<path d="M3 5h18l-7 8v6l-4-2v-4z"/>',
    "check": '<path d="M5 12l5 5 9-10"/>',
    "minus": '<path d="M6 12h12"/>',
    "help": '<circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .9-1 1.5V14M12 17h.01"/>',
    "info": '<circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8h.01"/>',
    "err": '<circle cx="12" cy="12" r="9"/><path d="M12 8v5M12 16h.01"/>',
    "lock": '<rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21c1-4 4-6 8-6s7 2 8 6"/>',
    "camera": '<path d="M4 8h3l2-3h6l2 3h3v11H4z"/><circle cx="12" cy="13" r="3.5"/>',
    "truck": '<path d="M3 6h11v10H3zM14 9h4l3 3v4h-7"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
    "building": '<path d="M4 21V5l8-3v19M12 8h8v13M8 7h.01M8 11h.01M8 15h.01M16 12h.01M16 16h.01M2 21h20"/>',
    "send": '<path d="M4 12l16-8-6 16-3-7z"/>',
    "save": '<path d="M5 4h11l3 3v13H5z"/><path d="M8 4v5h7M8 20v-6h8v6"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="M21 21l-4-4"/>',
    "dot": '<circle cx="12" cy="12" r="4" fill="currentColor"/>',
    "chev": '<path d="M9 6l6 6-6 6"/>',
    "settings": '<circle cx="12" cy="12" r="3"/><path d="M19 12a7 7 0 0 0-.1-1.3l2-1.6-2-3.4-2.4 1a7 7 0 0 0-2.2-1.3L14 3h-4l-.4 2.4A7 7 0 0 0 7.5 6.7l-2.4-1-2 3.4 2 1.6A7 7 0 0 0 5 12c0 .4 0 .9.1 1.3l-2 1.6 2 3.4 2.4-1a7 7 0 0 0 2.2 1.3L10 21h4l.4-2.4a7 7 0 0 0 2.2-1.3l2.4 1 2-3.4-2-1.6c.1-.4.1-.9.1-1.3z"/>',
}


def ic(k, s=20, cls="i"):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" '
            f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{P[k]}</svg>')


def tok_css():
    """tokens.css → phạm vi .pv. Bỏ brand phụ, @media, class .type-* (component tự viết font)."""
    css = TOKENS_CSS.read_text()
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"@media[^{]*\{(?:[^{}]*\{[^{}]*\})*[^{}]*\}", "", css)
    out = []
    for sel, body in re.findall(r"([^{}]+)\{([^{}]*)\}", css):
        sel = " ".join(sel.split())
        if sel.startswith(".") or "data-brand=\"" in sel and not sel.startswith(":root"):
            continue
        if sel.startswith(":root") or sel == '[data-theme="light"]':
            new = ".pv"
        elif sel == '[data-theme="dark"]':
            new = ".pv[data-theme=dark]"
        elif sel == '[data-platform="mobile"]':
            new = ".pv[data-platform=mobile]"
        else:
            continue
        body = " ".join(body.split())
        out.append(f"{new}{{{body}}}")
    return "".join(out)


# chữ theo thang v2 (Web | Mobile đổi bằng biến type-*-size của mode Platform)
BASE_CSS = """
.pv{font:var(--type-body-size)/var(--type-body-line-height) var(--font-body);color:var(--color-text-primary);background:var(--color-bg-surface)}
.pv *{box-sizing:border-box}
.vt{padding:20px 24px;display:flex;flex-direction:column;gap:22px;background:var(--color-bg-surface)}
.pv[data-platform=mobile] .vt{padding:16px}
.vh{font:600 13px/18px var(--font-body);color:var(--color-text-secondary-strong);margin-bottom:8px;display:flex;gap:8px;align-items:baseline}
.vh small{font:400 12px/16px var(--font-body);color:var(--color-text-tertiary)}
.vg{display:flex;flex-wrap:wrap;gap:12px;align-items:center}
.vgrid{display:grid;gap:10px 14px;align-items:center}
.vl{font:500 11px/14px var(--font-code);color:var(--color-text-tertiary);white-space:nowrap}
.card{background:var(--color-bg-surface);border:1px solid var(--color-border-default);border-radius:var(--radius-card)}
.pv .muted{color:var(--color-text-secondary)}
.pg{padding:20px 24px}
.pv[data-platform=mobile] .pg{padding:16px}
.tbl{width:100%;border-collapse:collapse}
.tbl th,.tbl td{padding:10px 16px;border-bottom:1px solid var(--color-border-default);text-align:left;font-size:13px;line-height:18px;vertical-align:middle}
.tbl th{color:var(--color-text-secondary);font-weight:500;background:var(--color-bg-muted)}
.row{display:flex;align-items:center;gap:12px}
.sp{flex:1}
.mono{font-family:var(--font-code);font-size:12px}
.sec-t{font:600 15px/22px var(--font-body);margin:0 0 4px}
"""


def hide_css(page):
    """data-hide="saving long" → ẩn khi đang ở MỘT trong các trạng thái đó (kit chỉ có data-show = AND)."""
    return "".join(f'.pv[data-state="{st["key"]}"] [data-hide~="{st["key"]}"]{{display:none!important}}' for st in page.get("states", []))


def write(out_path, page):
    page["css"] = page.get("css", "") + hide_css(page)
    # giữ lịch sử góp ý (bản trước / hoàn lại) do ds-snap.py ghi — dựng lại trang không được xoá
    if Path(out_path).exists():
        old = json.loads(Path(out_path).read_text())
        for k in ("snaps", "cmtSnap", "cmtChanges"):
            if k in old and k not in page:
                page[k] = old[k]
    Path(out_path).write_text(json.dumps(page, ensure_ascii=False, indent=1))
    print(f"Đã ghi {out_path}")
