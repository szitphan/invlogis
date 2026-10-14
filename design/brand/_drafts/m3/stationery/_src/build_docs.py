import re, pathlib, html, subprocess
from docx import Document
from docx.shared import Pt, Mm, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
root=pathlib.Path(__file__).resolve().parent.parent
LOGO=root/"assets/logo/invlogis-by-innvie.png"
INK=RGBColor(0x0E,0x14,0x42); SLATE=RGBColor(0x4A,0x53,0x80); COB=RGBColor(0x2F,0x43,0xDB)
PHRE=re.compile(r'(\[[^\]]*\])')

def render(src,out):
    subprocess.run(["python3",str(root/"../../_tools/render.py"),str(src),str(out)],check=True,capture_output=True)

# ---------------- docx helpers ----------------
def set_font(run,name,size=None,bold=None,italic=None,color=None):
    run.font.name=name
    rpr=run._element.get_or_add_rPr(); rf=rpr.find(qn('w:rFonts'))
    if rf is None: rf=OxmlElement('w:rFonts'); rpr.insert(0,rf)
    for a in ('w:ascii','w:hAnsi','w:cs','w:eastAsia'): rf.set(qn(a),name)
    if size: run.font.size=Pt(size)
    if bold is not None: run.font.bold=bold
    if italic is not None: run.font.italic=italic
    if color is not None: run.font.color.rgb=color
def shade_run(run,fill="FFD3C0"):
    rpr=run._element.get_or_add_rPr(); s=OxmlElement('w:shd')
    s.set(qn('w:val'),'clear'); s.set(qn('w:color'),'auto'); s.set(qn('w:fill'),fill); rpr.append(s)
def shade_cell(cell,fill):
    tcPr=cell._element.get_or_add_tcPr(); s=OxmlElement('w:shd')
    s.set(qn('w:val'),'clear'); s.set(qn('w:color'),'auto'); s.set(qn('w:fill'),fill); tcPr.append(s)
def borders(tbl,color="C4CDFF",inside=True,sz=4,only_h=False):
    tblPr=tbl._element.tblPr; b=OxmlElement('w:tblBorders')
    names=['top','bottom']+([] if only_h else ['left','right'])+(['insideH']+([] if only_h else ['insideV']) if inside else [])
    for n in names:
        e=OxmlElement('w:'+n); e.set(qn('w:val'),'single'); e.set(qn('w:sz'),str(sz)); e.set(qn('w:space'),'0'); e.set(qn('w:color'),color); b.append(e)
    tblPr.append(b)
def no_borders(tbl):
    tblPr=tbl._element.tblPr; b=OxmlElement('w:tblBorders')
    for n in ['top','left','bottom','right','insideH','insideV']:
        e=OxmlElement('w:'+n); e.set(qn('w:val'),'nil'); b.append(e)
    tblPr.append(b)
def para_border(p,side='bottom',color="2F43DB",sz=6,space=4):
    pPr=p._element.get_or_add_pPr(); pb=OxmlElement('w:pBdr'); e=OxmlElement('w:'+side)
    e.set(qn('w:val'),'single'); e.set(qn('w:sz'),str(sz)); e.set(qn('w:space'),str(space)); e.set(qn('w:color'),color); pb.append(e); pPr.append(pb)
def cell_margins(tbl,top=60,bottom=60,left=90,right=90):
    m=OxmlElement('w:tblCellMar')
    for k,v in (('top',top),('left',left),('bottom',bottom),('right',right)):
        e=OxmlElement('w:'+k); e.set(qn('w:w'),str(v)); e.set(qn('w:type'),'dxa'); m.append(e)
    tbl._element.tblPr.append(m)
def add_text(p,text,font,size,bold=False,italic=False,color=INK):
    for part in PHRE.split(text):
        if not part: continue
        r=p.add_run(part); ph=bool(PHRE.fullmatch(part))
        set_font(r,font,size,bold,italic,color)
        if ph: shade_run(r)
def pfmt(p,before=0,after=4,line=1.25,align=None,keep=False):
    f=p.paragraph_format; f.space_before=Pt(before); f.space_after=Pt(after); f.line_spacing=line
    if align is not None: p.alignment=align
    if keep: f.keep_with_next=True
def field(p,instr,font,size,color):
    r=p.add_run(); set_font(r,font,size,color=color)
    for t,txt in (('begin',None),('instr',instr),('end',None)):
        if t=='instr':
            e=OxmlElement('w:instrText'); e.set(qn('xml:space'),'preserve'); e.text=txt
        else:
            e=OxmlElement('w:fldChar'); e.set(qn('w:fldCharType'),t)
        r._element.append(e)

def new_doc(body_font,head_font,hdr_lines,ftr_text,top=42,bottom=26):
    d=Document(); s=d.sections[0]
    s.page_width=Mm(210); s.page_height=Mm(297)
    s.left_margin=s.right_margin=Mm(22); s.top_margin=Mm(top); s.bottom_margin=Mm(bottom)
    s.header_distance=Mm(12); s.footer_distance=Mm(10)
    st=d.styles['Normal']; st.font.name=body_font; st.font.size=Pt(10.5)
    rpr=st.element.get_or_add_rPr(); rf=rpr.find(qn('w:rFonts'))
    if rf is None: rf=OxmlElement('w:rFonts'); rpr.insert(0,rf)
    for a in ('w:ascii','w:hAnsi','w:cs','w:eastAsia'): rf.set(qn(a),body_font)
    st.font.color.rgb=INK
    # header: logo left, info right
    h=s.header; h.is_linked_to_previous=False
    t=h.add_table(1,2,Mm(166)); no_borders(t); t.autofit=False
    t.columns[0].width=Mm(70); t.columns[1].width=Mm(96)
    c0,c1=t.rows[0].cells; c0.width=Mm(70); c1.width=Mm(96)
    p=c0.paragraphs[0]; p.add_run().add_picture(str(LOGO),height=Mm(13)); pfmt(p,0,0,1)
    first=True
    for ln in hdr_lines:
        p=c1.paragraphs[0] if first else c1.add_paragraph(); first=False
        add_text(p,ln,body_font,8,color=SLATE); pfmt(p,0,0,1.2,WD_ALIGN_PARAGRAPH.RIGHT)
    hp=h.paragraphs[0]; pfmt(hp,0,0,1); hp.paragraph_format.line_spacing=Pt(17); hp.paragraph_format.line_spacing_rule=__import__('docx.enum.text',fromlist=['x']).WD_LINE_SPACING.EXACTLY; para_border(hp,'bottom',"2F43DB",6,0)
    # move the empty first paragraph after the table (so border sits under it)
    h._element.remove(hp._element); h._element.append(hp._element)
    f=s.footer; f.is_linked_to_previous=False
    p=f.paragraphs[0]; add_text(p,ftr_text,body_font,7.5,color=SLATE); pfmt(p,0,0,1.2,WD_ALIGN_PARAGRAPH.LEFT)
    para_border(p,'top',"C4CDFF",4,6)
    p2=f.add_paragraph(); pfmt(p2,2,0,1,WD_ALIGN_PARAGRAPH.RIGHT)
    r=p2.add_run("Trang "); set_font(r,body_font,7.5,color=SLATE)
    field(p2,"PAGE",body_font,7.5,SLATE)
    r=p2.add_run(" / "); set_font(r,body_font,7.5,color=SLATE)
    field(p2,"NUMPAGES",body_font,7.5,SLATE)
    d._fonts=(body_font,head_font)
    return d

def d_title(d,vn,en,meta=None):
    bf,hf=d._fonts
    p=d.add_paragraph(); add_text(p,vn,hf,20,color=INK); pfmt(p,6,0,1.1,WD_ALIGN_PARAGRAPH.CENTER)
    p=d.add_paragraph(); add_text(p,en,bf,10,italic=True,color=SLATE); pfmt(p,0,6,1.1,WD_ALIGN_PARAGRAPH.CENTER)
    if meta:
        p=d.add_paragraph(); add_text(p,meta,bf,10,color=INK); pfmt(p,0,10,1.2,WD_ALIGN_PARAGRAPH.CENTER)
def d_h(d,text,en=None):
    bf,hf=d._fonts
    p=d.add_paragraph(); add_text(p,text,hf,12,color=INK)
    if en: add_text(p,"  /  "+en,bf,9,italic=True,color=SLATE)
    pfmt(p,12,4,1.2,keep=True)
def d_p(d,text,italic=False,color=INK,size=10.5,after=5,indent=0,align=WD_ALIGN_PARAGRAPH.JUSTIFY):
    bf,hf=d._fonts
    p=d.add_paragraph(); add_text(p,text,bf,size,italic=italic,color=color); pfmt(p,0,after,1.35,align)
    if indent: p.paragraph_format.left_indent=Mm(indent)
def d_kv(d,rows):
    bf,hf=d._fonts
    t=d.add_table(len(rows),2); no_borders(t); t.autofit=False; cell_margins(t,30,30,0,60)
    for i,(k,v) in enumerate(rows):
        a,b=t.rows[i].cells; a.width=Mm(48); b.width=Mm(118)
        add_text(a.paragraphs[0],k,bf,10,color=SLATE); add_text(b.paragraphs[0],v,bf,10)
        for c in (a,b): pfmt(c.paragraphs[0],0,0,1.25)
    d.add_paragraph().paragraph_format.space_after=Pt(2)
def d_table(d,head,rows,widths,aligns,total_rows=0):
    bf,hf=d._fonts
    t=d.add_table(1+len(rows),len(head)); borders(t); cell_margins(t); t.autofit=False
    t.alignment=WD_TABLE_ALIGNMENT.CENTER
    for j,x in enumerate(head):
        c=t.rows[0].cells[j]; c.width=Mm(widths[j]); shade_cell(c,"E6EAF8")
        vn,_,en=x.partition("|"); p=c.paragraphs[0]; add_text(p,vn,bf,8.5,bold=True); 
        if en:
            p.add_run().add_break(); add_text(p,en,bf,7.5,italic=True,color=SLATE)
        pfmt(p,0,0,1.15,WD_ALIGN_PARAGRAPH.CENTER)
    # repeat header
    trPr=t.rows[0]._tr.get_or_add_trPr(); e=OxmlElement('w:tblHeader'); e.set(qn('w:val'),'true'); trPr.append(e)
    for i,row in enumerate(rows):
        for j,x in enumerate(row):
            c=t.rows[i+1].cells[j]; c.width=Mm(widths[j])
            bold = i>=len(rows)-total_rows
            add_text(c.paragraphs[0],x,bf,9,bold=bold)
            pfmt(c.paragraphs[0],0,0,1.2,{'l':WD_ALIGN_PARAGRAPH.LEFT,'r':WD_ALIGN_PARAGRAPH.RIGHT,'c':WD_ALIGN_PARAGRAPH.CENTER}[aligns[j]])
            if bold: shade_cell(c,"FAF8F4")
    d.add_paragraph().paragraph_format.space_after=Pt(2)
def d_sig(d,blocks):
    bf,hf=d._fonts
    t=d.add_table(1,len(blocks)); no_borders(t); t.autofit=False
    w=166/len(blocks)
    for i,(a,b,c) in enumerate(blocks):
        cell=t.rows[0].cells[i]; cell.width=Mm(w)
        p=cell.paragraphs[0]; add_text(p,a,bf,10,bold=True); pfmt(p,0,0,1.2,WD_ALIGN_PARAGRAPH.CENTER)
        p=cell.add_paragraph(); add_text(p,b,bf,8.5,italic=True,color=SLATE); pfmt(p,0,0,1.2,WD_ALIGN_PARAGRAPH.CENTER)
        p=cell.add_paragraph(); add_text(p,"(Ký, ghi rõ họ tên, đóng dấu)",bf,8.5,color=SLATE); pfmt(p,0,40,1.2,WD_ALIGN_PARAGRAPH.CENTER)
        p=cell.add_paragraph(); add_text(p,c,bf,10); pfmt(p,0,0,1.2,WD_ALIGN_PARAGRAPH.CENTER)
    tr=t.rows[0]._tr; trPr=tr.get_or_add_trPr(); e=OxmlElement('w:cantSplit'); trPr.append(e)

# ---------------- HTML twin ----------------
def h_esc(t):
    return "".join(f'<span class="ph">{html.escape(p)}</span>' if PHRE.fullmatch(p) else html.escape(p) for p in PHRE.split(t) if p)
def html_doc(blocks,hdr_lines,ftr,title):
    css=open(root/"_src/doc.css",encoding="utf-8").read().replace("{P}","../")
    out=[f'<!doctype html><meta charset=utf-8><title>{title}</title><style>{css}</style>']
    out.append('<table class="pg"><thead><tr><td><div class="hd"><img src="../assets/logo/invlogis-by-innvie.png"><div class="hi">'+"<br>".join(h_esc(x) for x in hdr_lines)+'</div></div></td></tr></thead>')
    out.append(f'<tfoot><tr><td><div class="ft">{h_esc(ftr)}</div></td></tr></tfoot><tbody><tr><td><main>')
    for b in blocks:
        k=b[0]
        if k=='title':
            out.append(f'<h1>{h_esc(b[1])}</h1><div class="en">{h_esc(b[2])}</div>'+(f'<div class="meta">{h_esc(b[3])}</div>' if len(b)>3 and b[3] else ''))
        elif k=='h': out.append(f'<h2>{h_esc(b[1])}'+(f' <i>/ {h_esc(b[2])}</i>' if len(b)>2 and b[2] else '')+'</h2>')
        elif k=='p': out.append(f'<p class="{b[2] if len(b)>2 else ""}">{h_esc(b[1])}</p>')
        elif k=='kv': out.append('<table class="kv">'+"".join(f'<tr><td>{h_esc(a)}</td><td>{h_esc(v)}</td></tr>' for a,v in b[1])+'</table>')
        elif k=='table':
            _,head,rows,widths,al,tot=b
            th="".join(f'<th style="width:{w}mm">{h_esc(x.partition("|")[0])}'+(f'<br><i>{h_esc(x.partition("|")[2])}</i>' if "|" in x else '')+'</th>' for x,w in zip(head,widths))
            tr="".join('<tr'+(' class="tot"' if i>=len(rows)-tot else '')+'>'+"".join(f'<td class="{a}">{h_esc(c)}</td>' for c,a in zip(r,al))+'</tr>' for i,r in enumerate(rows))
            out.append(f'<table class="grid"><thead><tr>{th}</tr></thead>{tr}</table>')
        elif k=='sig':
            out.append('<table class="sig"><tr>'+"".join(f'<td><b>{h_esc(a)}</b><br><i>{h_esc(e)}</i><br><span>(Ký, ghi rõ họ tên, đóng dấu)</span><div class="sp"></div>{h_esc(c)}</td>' for a,e,c in b[1])+'</tr></table>')
    out.append('</main></td></tr></tbody></table>')
    return "".join(out)

def build(name,folder,blocks,hdr_lines,ftr,title):
    folder=root/folder
    for bf,hf,suf in (("Be Vietnam Pro","Lexend",""),("Arial","Arial","-arial")):
        d=new_doc(bf,hf,hdr_lines,ftr)
        for b in blocks:
            k=b[0]
            if k=='title': d_title(d,b[1],b[2],b[3] if len(b)>3 else None)
            elif k=='h': d_h(d,b[1],b[2] if len(b)>2 else None)
            elif k=='p':
                o=b[2] if len(b)>2 else ""
                d_p(d,b[1],italic='i' in o.split(),color=SLATE if 'm' in o.split() else INK,size=9 if 'm' in o.split() else 10.5,indent=8 if 'ind' in o.split() else 0)
            elif k=='kv': d_kv(d,b[1])
            elif k=='table': d_table(d,b[1],b[2],b[3],b[4],b[5])
            elif k=='sig': d_sig(d,b[1])
        d.save(folder/f"{name}{suf}.docx")
    (folder/f"_{name}.html").write_text(html_doc(blocks,hdr_lines,ftr,title),encoding="utf-8")
    render(folder/f"_{name}.html",folder/f"{name}.pdf")
    (folder/f"_{name}.html").unlink()

HDR=["[chờ: tên pháp nhân đầy đủ]","[chờ: địa chỉ] · MST [chờ: MST]","[chờ: số điện thoại] · [chờ: email] · [chờ: domain]"]
FTR="Invlogis by innvie · [chờ: tên pháp nhân đầy đủ] · MST [chờ: MST] · [chờ: địa chỉ]"
