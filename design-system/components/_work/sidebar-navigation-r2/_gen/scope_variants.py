import json,sys
from pathlib import Path
W=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(W/"_forms")); from kit import ic, vg_row, P as ICONS
src=(W/"sidebar-navigation-r2/build.py").read_text()
blk=src[src.index("ICONS.update({"):src.index("})",src.index("ICONS.update({"))+2]; exec(blk)
ICONS.update({"building":'<path d="M4 21V5a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v16M16 9h2a2 2 0 0 1 2 2v10M3 21h18M8 7h4M8 11h4M8 15h4"/>',
  "check":'<path d="M5 12l5 5L20 7"/>',"x":'<path d="M6 6l12 12M18 6L6 18"/>',"pin":'<path d="M12 21s7-6.5 7-12a7 7 0 0 0-14 0c0 5.5 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/>',
  "org":'<rect x="9" y="3" width="6" height="5" rx="1"/><rect x="3" y="16" width="6" height="5" rx="1"/><rect x="15" y="16" width="6" height="5" rx="1"/><path d="M12 8v4M6 16v-2h12v2"/>',
  "clock":'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',"layers":'<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',"wifi-off":'<path d="M2 8.8a15 15 0 0 1 4.2-2.6M10.7 5.1A15 15 0 0 1 22 8.8M5 12.5a10 10 0 0 1 5.2-2.8M19 12.5a10 10 0 0 0-2.2-1.6M8.5 16.4a5 5 0 0 1 7 0M12 20h.01M3 3l18 18"/>'})
def opt(title,sub,lead,st="",tone=None,sys_=False):
    lead_h=(f'<span class="mt t-{tone}">{ic(lead,16)}</span>' if tone else f'<span class="oi">{ic(lead,16)}</span>')
    sel="sel" in st
    return (f'<div class="so {st}{" sys" if sys_ else ""}" role="radio" aria-checked="{"true" if sel else "false"}">{lead_h}'
            f'<span class="ot"><span class="o1">{title}</span><span class="o2">{sub}</span></span>'
            + (f'<span class="ok">{ic("check",16)}</span>' if sel else "") + '</div>')
BRS=[("Delta Logistics","Công ty mẹ · Toàn tổ chức","org"),("CN Hồ Chí Minh","TP. Hồ Chí Minh · Dùng gần nhất","building"),
    ("CN Hải Phòng","Hải Phòng","building"),("CN Bà Rịa – Vũng Tàu (Cái Mép – Thị Vải)","Bà Rịa – Vũng Tàu","building"),("CN Đà Nẵng","Đà Nẵng","building")]
MDS=[("Vận tải","Không chia cơ sở","truck","blue"),("Quản lý phương tiện","Không chia cơ sở","list","teal"),
    ("Bảo dưỡng sửa chữa","3 xưởng","wrench","yellow"),("Quản lý dầu","2 cây dầu","fuel","green"),
    ("Nhân sự","Không chia cơ sở","users","purple"),("Danh mục","Cấp công ty","db","gray")]
EMPTY_IC=[("không chia cơ sở","building"),("Không tìm thấy","search"),("đang phát triển","clock"),("Không tải được","wifi-off")]
def empty(t,s,btn=""):
    k=next((i for w,i in EMPTY_IC if w.lower() in t.lower()),"building")
    return f'<div class="sde"><span class="sdei">{ic(k,20)}</span><b>{t}</b><span>{s}</span>{btn}</div>'
def col(title,body,search=None):
    return (f'<div class="sdcol" role="radiogroup" aria-label="{title}"><div class="sdt">{title}</div>'
            + (f'<div class="sds">{ic("search",16)}<span>{search}</span></div>' if search else "") + body + '</div>')
def sbox(ph, q=None):
    return {"ph": ph, "q": q}
def col(title,body,search=None):
    if not search: head=f'<div class="sdt">{title}</div>'
    elif search["q"]:
        head=(f'<div class="sds on" role="search">{ic("search",16)}<b class="sq">{search["q"]}</b>'
              f'<button class="sdq" aria-label="Xoá và đóng tìm">{ic("x",14)}</button></div>')
    else:
        head=f'<div class="sdt">{title}<button class="sdi" aria-label="{search["ph"][:-1]}">{ic("search",16)}</button></div>'
    return f'<div class="sdcol" role="radiogroup" aria-label="{title}">' + head + body + '</div>'
FACS=[("Xưởng Cát Lái","Phường Cát Lái, TP. Thủ Đức"),("Xưởng Sóng Thần","KCN Sóng Thần, Bình Dương"),("Xưởng Tân Vạn","Ngã ba Tân Vạn, Dĩ An")]
def dlg(mod="Vận tải", branch="CN Hồ Chí Minh", c1="list", c2="list", c3=None, static=False, q1=None, q2=None, q3=None):
    fac = mod=="Bảo dưỡng sửa chữa"
    # cột 1
    brs=[x for x in BRS if not q1 or q1.lower() in x[0].lower()]
    b1 = (empty("Không tìm thấy chi nhánh","Thử tên hoặc tỉnh thành khác.") if not brs else
          "".join(opt(t,s,l,"sel" if t==branch else "") + ('<div class="sdv"></div>' if l=="org" else "") for t,s,l in brs))
    s1 = sbox("Tìm chi nhánh, tỉnh thành…", q1)
    # cột 2
    if c2=="dev":
        b2=empty("Tính năng đang phát triển","Xem dữ liệu toàn tổ chức sẽ có ở bản sau."); s2=None
    else:
        mds=[x for x in MDS if not q2 or q2.lower() in x[0].lower()]
        b2=(empty("Không tìm thấy module","Thử tên khác, vd Dầu, Xưởng.") if not mds else "".join(opt(t,s,l,"sel" if t==mod else "",tone) for t,s,l,tone in mds))
        s2=sbox("Tìm module…", q2)
    # cột 3
    s3=None
    if c3=="error": b3=empty("Không tải được danh sách","Kiểm tra kết nối rồi thử lại.",'<button class="bt">Thử lại</button>'); t3="3 · Xưởng"
    elif c2=="dev": b3=""; t3="3 · Cơ sở"
    elif fac:
        fs=[x for x in FACS if not q3 or q3.lower() in x[0].lower()]
        sysrow="" if q3 else opt("Tất cả xưởng","3 xưởng · xem tổng hợp","layers",sys_=True)+'<div class="sdv"></div>'
        b3=(sysrow+"".join(opt(t,s,"pin","sel" if t=="Xưởng Cát Lái" else "") for t,s in fs)) if fs else empty("Không tìm thấy xưởng","Thử tên hoặc khu vực khác.")
        t3="3 · Xưởng"; s3=sbox("Tìm xưởng…", q3)
    else: b3=empty(f"{mod} không chia cơ sở","Dữ liệu xem theo cả chi nhánh."); t3="3 · Cơ sở"
    pick = (f"{mod} · Xưởng Cát Lái · {branch}" if fac and c3!="error" else f"{mod} · {branch}")
    if c2=="dev": pick="Delta Logistics · toàn tổ chức"
    dis=' disabled' if c2=="dev" or c3=="error" else ''
    cls="scd st" if static else "scd"
    show='' if static else ' data-show="state:scope"'
    return (('' if static else '<div class="scr scs" data-show="state:scope"></div>')
     + f'<div class="{cls}"{show} data-cmp role="dialog" aria-label="Đổi phạm vi làm việc">'
     f'<div class="sdh"><b>Đổi phạm vi làm việc</b><button class="sdx" data-close aria-label="Đóng">{ic("x",18)}</button></div><div class="sdc">'
     + col("1 · Chi nhánh",b1,s1) + col("2 · Module",b2,s2) + col(t3,b3,s3) + '</div>'
     f'<div class="sdf"><span class="sdfh">Đang chọn: <b>{pick}</b></span><button class="bt big0" data-close>Huỷ</button><button class="bt pri big0" data-close{dis}>Chọn</button></div></div>')
def card(st="", collapsed=False):
    c=(f'<div class="scope {st}"><span class="sic">{ic("truck", 18)}</span><div class="smm"><b>Vận tải</b><span>Toàn chi nhánh</span></div>'
       f'<span class="scw">{ic("swap", 16)}</span></div>')
    if collapsed: return f'<div class="sb k-slim" style="min-height:0;width:64px;border:0;padding:8px">{c}</div>'
    return f'<div class="sb" style="min-height:0;width:280px;border:0;padding:8px">{c}</div>'
def tile(tone,icon,s):
    return f'<span class="mt t-{tone} s{s}">{ic(icon,20 if s==32 else 16)}</span>'
def board_rows():
    R=[]
    STS=[("Default",""),("Hover","is-hover"),("Focus","is-focus"),("Open","is-open"),("Read-only","is-ro")]
    R.append(vg_row("Thẻ phạm vi · State × Collapsed",[(f"{n} · False",card(c)) for n,c in STS]+[(f"{n} · True",card(c,True)) for n,c in STS],5,
                    "Read-only = chỉ một phạm vi, không icon đổi, tooltip \"Chỉ có một phạm vi làm việc\""))
    R.append(vg_row("Ô module · Tone × Size",[(f"{t.title()} · {s}",tile(t,i,s)) for s in (32,28) for _,_,i,t in MDS],6,"màu theo module, cấu hình theo khách"))
    R.append(vg_row("Dòng chọn (Scope option) · State",[(n,f'<div style="width:300px">{opt("CN Hồ Chí Minh","TP. Hồ Chí Minh · Dùng gần nhất","building",c)}</div>') for n,c in
                    [("Default",""),("Hover","is-hover"),("Selected","sel"),("Focus","is-focus")]]
                    +[("Dòng hệ thống + vạch chia",f'<div style="width:300px">{opt("Tất cả xưởng","3 xưởng · xem tổng hợp","layers",sys_=True)}<div class="sdv"></div></div>'),
                      ("Có ô module",f'<div style="width:300px">{opt("Bảo dưỡng sửa chữa","3 xưởng","wrench","",tone="yellow")}</div>')],3))
    R.append(vg_row("Hộp thoại · Facility = Has (module chia cơ sở) — tìm thu về nút kính lúp ở tiêu đề cột",[("Bảo dưỡng sửa chữa · Xưởng Cát Lái",dlg("Bảo dưỡng sửa chữa",static=True))],1))
    R.append(vg_row("Hộp thoại · Facility = None",[("Vận tải · không chia cơ sở",dlg(static=True))],1))
    R.append(vg_row("Hộp thoại · No result (cột 1)",[("Tìm chi nhánh không ra",dlg(c1="none",q1="Cần Thơ",static=True))],1))
    R.append(vg_row("Hộp thoại · Tìm module và cơ sở",[("Bấm kính lúp cột 2, cột 3 rồi gõ \"dầu\", \"Sóng\" — ô tìm thay dòng tiêu đề, lọc ngay khi gõ",dlg("Bảo dưỡng sửa chữa",q2="dầu",q3="Sóng",static=True)),
                    ("Tìm không ra ở cột 2 và cột 3",dlg("Bảo dưỡng sửa chữa",q2="kho",q3="Long An",static=True))],1))
    R.append(vg_row("Hộp thoại · In development (cột 2)",[("Chọn công ty mẹ — nút Chọn tắt (DEC-289)",dlg(branch="Delta Logistics",c2="dev",static=True))],1))
    R.append(vg_row("Hộp thoại · Load error (cột 3)",[("Không tải được danh sách xưởng — nút Thử lại",dlg("Bảo dưỡng sửa chữa",c3="error",static=True))],1))
    return "".join(R)
CSS=r"""
/* biến thể phạm vi */
.scope.is-hover{background:var(--muted)}.scope.is-focus{box-shadow:0 0 0 2px var(--bg),0 0 0 4px var(--focus)}.scope.is-open{background:#F5F5F5}
.scope.is-ro{cursor:default}.scope.is-ro .scw{display:none}.scope.is-ro:hover{background:none}
.so.is-hover{background:#FAFAFA}.so.is-focus{box-shadow:inset 0 0 0 2px var(--focus)}
.so.sys .o1{font-weight:600}.sdv{height:1px;background:var(--line);margin:4px 8px;flex:none}
.mt.s32{width:32px;height:32px}.mt.s28{width:28px;height:28px}
.scd.st{position:relative;left:auto;top:auto;transform:none;width:960px;max-width:none;border:1px solid var(--line)}
.scd.st .sdc{min-height:360px}
.sds .sq{font-weight:400;color:var(--fg)}
.sde .bt{align-self:center;margin-top:8px}
.bt.pri[disabled]{background:var(--muted);border-color:var(--muted);color:var(--fg4);cursor:not-allowed}
.pv[data-theme=dark] .scope.is-open{background:#262626}.pv[data-theme=dark] .so.is-hover{background:#171717}
"""

CSS2=r"""
/* tìm trong hộp thoại: nút kính lúp ở tiêu đề cột → bấm mới mở ô tìm (DEC-297, góp ý 28/10 "ô search thô") */
.sdt{display:flex;align-items:center;min-height:32px;margin:4px 0;padding:0 2px 0 8px;box-sizing:border-box}
.sdi{margin-left:auto;width:28px;height:28px;border:0;background:none;border-radius:6px;color:var(--fg3);display:grid;place-items:center;cursor:pointer}
.sdi:hover{background:var(--muted);color:var(--fg)}
.sdcol>.sds.on{margin:4px 0;border-color:var(--focus);box-shadow:inset 0 0 0 1px var(--focus);padding:0 4px 0 10px}
.sdq{margin-left:auto;width:24px;height:24px;border:0;background:none;border-radius:6px;color:var(--fg3);display:grid;place-items:center;cursor:pointer}
"""

CSS3=r"""
/* góp ý 28/10: tiêu đề cột viết hoa như nhãn nhóm; trạng thái rỗng có icon tròn */
.sdt{text-transform:uppercase;letter-spacing:.05em;font-size:11px;line-height:16px}
.sde .sdei{width:40px;height:40px;border-radius:50%;background:#F5F5F5;color:var(--fg3);display:grid;place-items:center;margin:0 auto 8px}
.pv[data-theme=dark] .sde .sdei{background:#262626}
"""
