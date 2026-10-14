from PIL import Image, ImageDraw, ImageFont
import pathlib
R=pathlib.Path(__file__).parent; P=R/"previews"
items=[("login-web-default-desktop","1 · Đăng nhập, desktop"),("login-web-tenant-desktop","1 · Đăng nhập, khách (P-logo)"),
("login-web-default-mobile","1 · Đăng nhập, mobile"),("login-web-tenant-mobile","1 · Đăng nhập, mobile khách"),
("splash-mobile-a","2 · Splash A (giữ DEC-037)"),("splash-mobile-b","2 · Splash B (đề xuất)"),
("app-icon-in-context","3 · Icon app"),("browser-tab","4 · Tab trình duyệt"),
("email-moi-nguoi-dung","5 · Email mời"),("email-ma-xac-thuc","5 · Email OTP"),("email-dat-lai-mat-khau","5 · Email đặt lại MK"),
("loading-screen","6 · Màn tải"),("loading-motion-frames","6 · Chuyển động logo"),("about-screen","6 · Giới thiệu")]
f=ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Unicode.ttf",22)
H=520; cells=[]
for n,t in items:
    im=Image.open(P/f"{n}.png").convert("RGB"); s=H/im.height; im=im.resize((int(im.width*s),H),Image.LANCZOS); cells.append((im,t))
W=2600; x=y=40; rows=[[]]
for im,t in cells:
    if x+im.width+40>W: rows.append([]); x=40
    rows[-1].append((im,t)); x+=im.width+40
sheet=Image.new("RGB",(W,len(rows)*(H+80)+40),"#e9e9ee"); d=ImageDraw.Draw(sheet); y=40
for r in rows:
    x=40
    for im,t in r:
        d.text((x,y),t,fill="#333",font=f); sheet.paste(im,(x,y+36)); x+=im.width+40
    y+=H+80
sheet.save(P/"contact-sheet.png"); print(sheet.size)
