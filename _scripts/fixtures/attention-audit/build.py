# Fixture A7 (attention-audit): màn Lệnh vận tải × 3 kiểu breadcrumb. Chạy: python3 _scripts/fixtures/attention-audit/build.py
from pathlib import Path
OUT = Path(__file__).parent

ICON = {
 "home": '<path d="M3 10l9-7 9 7v10a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>',
 "cr": '<path d="M9 6l6 6-6 6"/>',
 "search": '<circle cx="11" cy="11" r="7"/><path d="M21 21l-4-4"/>',
 "bell": '<path d="M6 16V11a6 6 0 0 1 12 0v5l2 2H4z"/><path d="M10 20a2 2 0 0 0 4 0"/>',
 "help": '<circle cx="12" cy="12" r="9"/><path d="M9.5 9a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .9-1 1.6V14M12 17h.01"/>',
 "grid": '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/>',
 "route": '<circle cx="6" cy="19" r="2"/><circle cx="18" cy="5" r="2"/><path d="M8 19h8a3 3 0 0 0 0-6H8a3 3 0 0 1 0-6h8"/>',
 "truck": '<path d="M3 6h11v10H3zM14 9h4l3 3v4h-7"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
 "map": '<path d="M9 4L3 6v14l6-2 6 2 6-2V4l-6 2z"/><path d="M9 4v14M15 6v14"/>',
 "users": '<circle cx="9" cy="8" r="4"/><path d="M2 21c1-4 4-6 7-6s6 2 7 6"/>',
 "wallet": '<rect x="3" y="6" width="18" height="14" rx="2"/><path d="M3 10h18M16 15h2"/>',
 "plus": '<path d="M12 5v14M5 12h14"/>',
 "filter": '<path d="M3 5h18l-7 8v6l-4 2v-8z"/>',
}
def ic(k, s=18):
    return (f'<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round">{ICON[k]}</svg>')

# Ba kiểu breadcrumb: font, màu tầng trên, màu + đậm trang hiện tại, cỡ icon nhà
VARIANTS = {
 "fail-breadcrumb-dam":   dict(size=16, w=600, up="#171717", cur="#171717", cw=700, home=18, sep="#525252"),
 "warn-breadcrumb-hien-tai":    dict(size=14, w=500, up="#737373", cur="#171717", cw=600, home=16, sep="#D4D4D4"),
 "pass-breadcrumb-nhe":         dict(size=13, w=400, up="#737373", cur="#525252", cw=500, home=14, sep="#D4D4D4"),
}

MENU = [(None, [("grid", "Tổng quan", "")]),
        ("Vận tải", [("route", "Lệnh vận tải", "12"), ("truck", "Bảng điều phối", ""), ("map", "Theo dõi chuyến", "")]),
        ("Danh mục", [("users", "Khách hàng", ""), ("map", "Tuyến đường", "")]),
        ("Tài chính", [("wallet", "Chi phí chuyến", "")])]
ROWS = [("LVT-2026-0412", "Cát Lái → Sóng Thần", "51C-123.45", "Trần Văn Bình", "Đang chạy", "info"),
        ("LVT-2026-0413", "Hiệp Phước → VSIP 2", "51D-678.90", "Lê Minh Châu", "Đang chạy", "info"),
        ("LVT-2026-0414", "Cát Lái → Long Hậu", "51C-246.80", "Phạm Quốc Huy", "Chờ nhận", "warn"),
        ("LVT-2026-0415", "ICD Long Bình → KCN Mỹ Phước 3", "50H-112.23", "Ngô Thanh Tâm", "Chờ duyệt", "warn"),
        ("LVT-2026-0416", "Cát Lái → Tân Vạn", "51C-135.79", "Trần Văn Bình", "Hoàn thành", "ok"),
        ("LVT-2026-0417", "Cát Lái → KCN Tân Tạo", "51C-777.12", "Đỗ Hữu Lộc", "Đang chạy", "info"),
        ("LVT-2026-0418", "Hiệp Phước → Bình Dương", "51D-224.66", "Vũ Đức Anh", "Chờ nhận", "warn"),
        ("LVT-2026-0419", "Cát Lái → Nhơn Trạch", "51C-908.31", "Lê Minh Châu", "Hoàn thành", "ok"),
        ("LVT-2026-0420", "ICD Phước Long → VSIP 1", "50H-338.04", "Phạm Quốc Huy", "Đang chạy", "info"),
        ("LVT-2026-0421", "Cát Lái → Sóng Thần", "51C-551.20", "Trần Văn Bình", "Chờ duyệt", "warn")]

CSS = """
*{box-sizing:border-box}body{margin:0;font:400 14px/20px Inter,sans-serif;color:#171717;background:#fff}
.app{display:flex;width:1280px;height:800px;overflow:hidden}
.sb{width:240px;flex:none;border-right:1px solid #E5E5E5;padding:12px;display:flex;flex-direction:column;gap:2px}
.lg{display:flex;align-items:center;gap:8px;padding:4px 6px 14px;font:400 18px "Cal Sans",Inter}
.lo{width:28px;height:28px;border-radius:8px;background:#0036B5;color:#fff;display:grid;place-items:center;font:600 12px Inter}
.gh{font:600 11px/16px Inter;letter-spacing:.05em;text-transform:uppercase;color:#737373;padding:14px 8px 4px}
.it{display:flex;align-items:center;gap:10px;height:36px;padding:0 10px;border-radius:8px;color:#525252;font-weight:500}
.it.on{background:#F5F5F5;color:#171717;font-weight:600}
.it .c{margin-left:auto;font:600 11px/18px Inter;color:#1F4FB8;background:#E7EFFD;border-radius:999px;padding:0 7px}
.mn{flex:1;display:flex;flex-direction:column;min-width:0}
.hd{height:44px;display:flex;align-items:center;gap:6px;padding:0 24px;border-bottom:1px solid #E5E5E5}
.bc{display:flex;align-items:center;gap:2px;white-space:nowrap}
.sp{flex:1}
.ib{width:32px;height:32px;border-radius:8px;display:grid;place-items:center;color:#525252;position:relative}
.nc{position:absolute;top:-2px;right:-4px;min-width:18px;height:18px;padding:0 5px;border-radius:999px;font:600 11px/18px Inter;background:#D92D20;color:#fff;box-shadow:0 0 0 2px #fff}
.av{width:32px;height:32px;border-radius:50%;background:#F5F5F5;border:1px solid #E5E5E5;display:grid;place-items:center;font:600 12px Inter;color:#525252;margin-left:4px}
.ct{padding:24px;flex:1;background:#fff}
.ph{display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:16px}
h1{font:400 24px/32px "Cal Sans",Inter;margin:0}.sub{margin:2px 0 0;color:#737373}
.btn{height:36px;display:inline-flex;align-items:center;gap:6px;padding:0 14px;border-radius:8px;background:#262626;color:#fff;font-weight:600}
.btn2{height:36px;display:inline-flex;align-items:center;gap:6px;padding:0 12px;border-radius:8px;border:1px solid #D4D4D4;color:#171717;font-weight:500}
.tl{display:flex;gap:8px;margin-bottom:12px}
.srch{width:280px;height:36px;border:1px solid #D4D4D4;border-radius:8px;display:flex;align-items:center;gap:8px;padding:0 10px;color:#737373}
table{width:100%;border-collapse:collapse;font-size:13px}
th{text-align:left;font-weight:500;color:#737373;background:#FAFAFA;height:40px;padding:0 12px;border-bottom:1px solid #E5E5E5}
td{height:48px;padding:0 12px;border-bottom:1px solid #E5E5E5;white-space:nowrap}
td.id{font-weight:600}
.chip{display:inline-flex;align-items:center;gap:5px;height:22px;padding:0 8px;border-radius:999px;font:500 12px/18px Inter}
.chip:before{content:"";width:6px;height:6px;border-radius:50%;background:currentColor}
.info{color:#1F4FB8;background:#E7EFFD}.ok{color:#1B7542;background:#E8F5EC}.warn{color:#8A5300;background:#FFF3DC}
"""

def page(v):
    sep = f'<span style="color:{v["sep"]};display:grid;place-items:center;width:16px">{ic("cr", 14)}</span>'
    up = f'style="color:{v["up"]};font:{v["w"]} {v["size"]}px/20px Inter"'
    bc = (f'<nav class="bc" data-attn="khung:breadcrumb"><span style="color:{v["up"]};display:grid">{ic("home", v["home"])}</span>{sep}'
          f'<span {up}>Điều phối vận tải</span>{sep}'
          f'<span style="color:{v["cur"]};font:{v["cw"]} {v["size"]}px/20px Inter">Lệnh vận tải</span></nav>')
    sb = ['<aside class="sb" data-attn="khung:menu-trai"><div class="lg"><span class="lo">in</span>invlogis</div>']
    for g, items in MENU:
        if g: sb.append(f'<div class="gh">{g}</div>')
        for i, t, n in items:
            sb.append(f'<div class="it{" on" if t == "Lệnh vận tải" else ""}">{ic(i)}<span>{t}</span>{f"<b class=c>{n}</b>" if n else ""}</div>')
    sb.append("</aside>")
    rows = "".join(f'<tr><td class="id">{a}</td><td>{b}</td><td>{c}</td><td>{d}</td><td><span class="chip {k}">{e}</span></td><td>28/10 08:30</td></tr>'
                   for a, b, c, d, e, k in ROWS)
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Cal+Sans&family=Inter:wght@400;500;600;700&display=block" rel="stylesheet">
<style>{CSS}</style></head><body><div class="app">{"".join(sb)}<div class="mn">
<header class="hd" id="hd">{bc}<span class="sp"></span><span style="display:flex;gap:6px;align-items:center" data-attn="khung:icon-phai"><span class="ib">{ic("search")}</span><span class="ib">{ic("help")}</span>
<span class="ib">{ic("bell")}<b class="nc">3</b></span><span class="av">NA</span></span></header>
<main class="ct"><div class="ph" id="ph"><div data-attn="tieu-de:tieu-de"><h1>Lệnh vận tải</h1><p class="sub">128 lệnh trong tháng 10</p></div>
<div style="display:flex;gap:8px" data-attn="hanh-dong:nut-chinh"><span class="btn2">Xuất Excel</span><span class="btn">{ic("plus",16)}Tạo lệnh</span></div></div>
<div class="tl" data-attn="phu:cong-cu"><span class="srch">{ic("search",16)}Tìm mã lệnh, biển số…</span><span class="btn2">{ic("filter",16)}Bộ lọc</span></div>
<table data-attn="chinh:bang"><tr><th>Mã lệnh</th><th>Tuyến</th><th>Biển số</th><th>Lái xe</th><th>Trạng thái</th><th>Giờ đi</th></tr>{rows}</table>
</main></div></div></body></html>"""

OUT.mkdir(parents=True, exist_ok=True)
for name, v in VARIANTS.items():
    (OUT / f"{name}.html").write_text(page(v), encoding="utf-8")
print("ok")
