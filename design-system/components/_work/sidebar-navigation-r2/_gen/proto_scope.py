import json,sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
import scope_variants as SV
ic=SV.ic
BRS={"hcm":("CN Hồ Chí Minh","TP. Hồ Chí Minh · Dùng gần nhất","Chi nhánh Hồ Chí Minh"),"hp":("CN Hải Phòng","Hải Phòng","Chi nhánh Hải Phòng")}
MODS={"vt":("Vận tải","truck","blue"),"bd":("Bảo dưỡng sửa chữa","wrench","yellow"),"dau":("Quản lý dầu","fuel","green")}
UNIT={"bd":("xưởng","Xưởng"),"dau":("cây dầu","Cây dầu")}
FAC={("bd","hcm"):[("f1","Xưởng Cát Lái","Phường Cát Lái, TP. Thủ Đức · Dùng gần nhất"),("f2","Xưởng Sóng Thần","KCN Sóng Thần, Bình Dương"),("f3","Xưởng Tân Vạn","Ngã ba Tân Vạn, Dĩ An")],
     ("bd","hp"):[("f1","Xưởng Đình Vũ","KCN Đình Vũ, Hải An")],
     ("dau","hcm"):[("f1","Cây dầu Cát Lái","Bãi xe Cát Lái · Dùng gần nhất"),("f2","Cây dầu Sóng Thần","Bãi xe Sóng Thần")],
     ("dau","hp"):[("f1","Cây dầu Đình Vũ","Bãi xe Đình Vũ")]}
OUT={"bd":"Sửa lưu động, gửi xưởng ngoài","dau":"Đổ dầu tại cây xăng ngoài"}
def row(attr,val,title,sub,lead,tone=None,sys_=False):
    lead_h=(f'<span class="mt t-{tone}">{ic(lead,16)}</span>' if tone else f'<span class="oi">{ic(lead,16)}</span>')
    return (f'<div class="so pz-r{" sys" if sys_ else ""}" data-{attr}="{val}" role="radio">{lead_h}<span class="ot"><span class="o1">{title}</span>'
            f'<span class="o2">{sub}</span></span><span class="ok">{ic("check",16)}</span></div>')
def combos():
    out=[]
    for b in BRS:
        out.append((b,"vt",None))
        for m in ("bd","dau"):
            fs=FAC[(m,b)]
            keys=(["all"] if len(fs)>1 else [])+["out"]+[f for f,_,_ in fs]
            out+= [(b,m,k) for k in keys]
    return out
def ckey(b,m,f): return f"{b}-{m}" + (f"-{f}" if f else "")
def fac_label(b,m,f):
    if m=="vt": return "Toàn chi nhánh"
    if f=="all": return f"Tất cả {UNIT[m][0]}"
    if f=="out": return "Ngoài cơ sở"
    return next(t for k,t,_ in FAC[(m,b)] if k==f)
def dialog():
    c1=('<div class="sdcol" role="radiogroup" aria-label="1 · Chi nhánh">'
        f'<div class="sdt">1 · Chi nhánh<button class="sdi" aria-label="Tìm chi nhánh">{ic("search",16)}</button></div>'
        + '<div class="so pz-dis"><span class="oi">'+ic("org",16)+'</span><span class="ot"><span class="o1">Delta Logistics</span><span class="o2">Công ty mẹ · Toàn tổ chức</span></span></div><div class="sdv"></div>'
        + "".join(row("b",k,t,s,"building") for k,(t,s,_) in BRS.items())
        + row("b","x","CN Đà Nẵng","Chưa mở module nào","building").replace('pz-r','pz-dis')
        + '</div>')
    def msub(m):
        if m=="vt": return "Không chia cơ sở"
        return "".join(f'<span class="bx" data-k="{b}">{len(FAC[(m,b)])} {UNIT[m][0]}</span>' for b in BRS)
    c2=('<div class="sdcol" role="radiogroup" aria-label="2 · Module">'
        f'<div class="sdt">2 · Module<button class="sdi" aria-label="Tìm module">{ic("search",16)}</button></div>'
        + "".join(row("m",k,t,msub(k),i,tone) for k,(t,i,tone) in MODS.items()) + '</div>')
    blocks=[f'<div class="c3" data-k="vt"><div class="sdt">3 · Cơ sở</div>{SV.empty("Vận tải không chia cơ sở","Dữ liệu xem theo cả chi nhánh.")}</div>']
    for (m,b),fs in FAC.items():
        many=len(fs)>1; u,U=UNIT[m]
        head=f'<div class="sdt">3 · {U}' + (f'<button class="sdi" aria-label="Tìm {u}">{ic("search",16)}</button>' if many else '') + '</div>'
        rows=(row("f","all",f"Tất cả {u}",f"{len(fs)} {u} · xem tổng hợp","layers",sys_=True) if many else "")
        rows+=row("f","out","Ngoài cơ sở",OUT[m],"pin",sys_=True)+'<div class="sdv"></div>'
        rows+="".join(row("f",k,t,s,"pin") for k,t,s in fs)
        note='' if many else f'<div class="c3n">Chi nhánh này chỉ có 1 {u} — đã chọn sẵn.</div>'
        blocks.append(f'<div class="c3" data-k="{m}-{b}">{head}{rows}{note}</div>')
    c3='<div class="sdcol" role="radiogroup" aria-label="3 · Cơ sở">'+"".join(blocks)+'</div>'
    foot="".join(f'<b class="fk" data-k="{ckey(*c)}">{MODS[c[1]][0]} · {fac_label(*c)} · {BRS[c[0]][0]}</b>'.replace(" · Toàn chi nhánh","") for c in combos())
    oks="".join(f'<button class="bt pri big0 sdok" data-k="{ckey(*c)}">Chọn</button>' for c in combos())
    return ('<div class="scr scs" data-show="state:scope"></div>'
            '<div class="scd pz" data-show="state:scope" data-cmp role="dialog" aria-label="Đổi phạm vi làm việc">'
            f'<div class="sdh"><b>Đổi phạm vi làm việc</b><button class="sdx" data-close aria-label="Đóng">{ic("x",18)}</button></div>'
            f'<div class="sdc">{c1}{c2}{c3}</div>'
            f'<div class="sdf"><span class="sdfh">Đang chọn: {foot}</span><button class="bt big0" data-close>Huỷ</button>{oks}</div></div>')
def card_inner():
    ck=[("def","vt","Vận tải","Toàn chi nhánh")]+[(ckey(*c),c[1],MODS[c[1]][0],fac_label(*c)) for c in combos()]
    tiles="".join(f'<span class="ckv cki" data-k="{k}">{ic(MODS[m][1],18)}</span>' for k,m,_,_ in ck)
    b="".join(f'<span class="ckv" data-k="{k}">{t}</span>' for k,_,t,_ in ck)
    s="".join(f'<span class="ckv" data-k="{k}">{f}</span>' for k,_,_,f in ck)
    return f'<span class="sic">{tiles}</span><div class="smm"><b>{b}</b><span>{s}</span></div>'
def branch_line():
    ks=[("def","hcm")]+[(ckey(*c),c[0]) for c in combos()]
    return "".join(f'<span class="ckv" data-k="{k}">{BRS[b][2]}</span>' for k,b in ks)
def css():
    C=[".scd.pz .so .ok{visibility:hidden}.scd.pz .c3{display:none;flex-direction:column;gap:2px;flex:1}",
       ".scd.pz .pz-dis{opacity:.5;cursor:not-allowed}.c3n{font-size:12px;line-height:16px;color:var(--fg3);padding:8px}",
       ".scd.pz .bx{display:none}.ckv{display:none}",
       ".pv:not([data-ck]) .ckv[data-k=def]{display:inline}.pv:not([data-ck]) .sic .ckv[data-k=def]{display:contents}"]
    SEL="background:#F5F5F5"
    for b in BRS:
        C.append(f'.pv[data-sbr={b}] .scd.pz .so[data-b={b}]{{{SEL}}}.pv[data-sbr={b}] .scd.pz .so[data-b={b}] .ok{{visibility:visible}}.pv[data-sbr={b}] .scd.pz .bx[data-k={b}]{{display:inline}}')
    for m in MODS:
        C.append(f'.pv[data-smod={m}] .scd.pz .so[data-m={m}]{{{SEL}}}.pv[data-smod={m}] .scd.pz .so[data-m={m}] .ok{{visibility:visible}}')
    C.append('.pv[data-smod=vt] .scd.pz .c3[data-k=vt]{display:flex}')
    for (m,b) in FAC: C.append(f'.pv[data-smod={m}][data-sbr={b}] .scd.pz .c3[data-k="{m}-{b}"]{{display:flex}}')
    for f in ("all","out","f1","f2","f3"):
        C.append(f'.pv[data-sfac={f}] .scd.pz .c3 .so[data-f={f}]{{{SEL}}}.pv[data-sfac={f}] .scd.pz .c3 .so[data-f={f}] .ok{{visibility:visible}}')
    for c in combos():
        k=ckey(*c); b,m,f=c
        cond=f'.pv[data-sbr={b}][data-smod={m}]'+(f'[data-sfac={f}]' if f else '')
        C.append(f'{cond} .scd.pz .fk[data-k="{k}"],{cond} .scd.pz .sdok[data-k="{k}"]{{display:inline-flex}}')
        C.append(f'.pv[data-ck="{k}"] .ckv[data-k="{k}"]{{display:inline}}.pv[data-ck="{k}"] .sic .ckv[data-k="{k}"]{{display:contents}}')
    C.append(".scd.pz .sdok{display:none}")
    # sdok display:none phải đứng trước luật hiện — đưa lên đầu
    return ".scd.pz .sdok,.scd.pz .fk{display:none}\n"+"\n".join(c for c in C if c!=".scd.pz .sdok{display:none}")
def proto():
    P=[{"sel":".clp,[data-live-sb] .lg","state":"slim","toggle":True},
       {"sel":".scope","state":"scope","toggle":True,"set":{"sbr":"hcm","smod":"vt","sfac":"none"}},
       {"sel":".scd [data-close]","close":True}]
    for b in BRS: P.append({"sel":f'.scd.pz .so[data-b={b}]',"set":{"sbr":b,"sfac":"f1"}})
    for m in MODS: P.append({"sel":f'.scd.pz .so[data-m={m}]',"set":{"smod":m,"sfac":"f1" if m!="vt" else "none"}})
    for f in ("all","out","f1","f2","f3"): P.append({"sel":f'.scd.pz .c3 .so[data-f={f}]',"set":{"sfac":f}})
    for c in combos(): P.append({"sel":f'.scd.pz .sdok[data-k="{ckey(*c)}"]',"state":"default","set":{"ck":ckey(*c)}})
    return P
