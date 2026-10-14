import fitz,os,tempfile,pathlib
from PIL import Image
root=pathlib.Path(__file__).resolve().parent.parent; os.chdir(root)
td=tempfile.mkdtemp()
def pg(f):
    p=os.path.join(td,"a.png"); fitz.open(f)[0].get_pixmap(dpi=80).save(p); return Image.open(p).convert("RGB")
L=lambda f:Image.open(f).convert("RGB")
def row(ims,H,W=1800,pad=30):
    cs=[i.resize((int(i.width*H/i.height),H),Image.LANCZOS) for i in ims]
    im=Image.new("RGB",(W,H+2*pad),"#E6EAF8"); x=pad
    for c in cs: im.paste(c,(x,pad)); x+=c.width+pad
    return im
r1=row([L("business-card/business-card-front.png"),L("business-card/business-card-back.png"),L("envelope/envelope-dl-preview.png"),L("email-signature/signature-vi-preview.png")],195)
r2=row([pg("letterhead/letterhead.pdf"),pg("quotation/bao-gia-template.pdf"),pg("contract/hop-dong-template.pdf")],700)
s=Image.new("RGB",(1800,r1.height+r2.height),"#E6EAF8"); s.paste(r1,(0,0)); s.paste(r2,(0,r1.height)); s.save("previews/contact-sheet.png")
