import subprocess,geom as g,numpy as np,importlib,sys
from PIL import Image
R=(777,41,868,131)
word="".join(g.WORD)
svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 248" width="900" height="248"><path fill="{g.BLACK}" fill-rule="evenodd" d="{word}"/><rect x="{g.BAR[0]}" y="{g.BAR[1]}" width="{g.BAR[2]}" height="{g.BAR[3]}" fill="{g.GREEN}"/><path fill="{g.BLACK}" fill-rule="evenodd" d="{g.ring()}"/><path fill="{g.BLACK}" d="{g.r_path(*R)}"/></svg>'
open('t.svg','w').write(svg)
open('t.html','w').write(f'<html><body style="margin:0;background:#fff">{svg}</body></html>')
import os
subprocess.run(['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome','--headless=new','--disable-gpu','--hide-scrollbars','--force-device-scale-factor=1','--window-size=900,448','--screenshot='+os.path.abspath('t.png'),'file://'+os.path.abspath('t.html')],capture_output=True)
t=np.array(Image.open('t.png').convert('RGB').crop((0,0,900,248))).astype(int)
s=Image.open('new.png').convert('RGBA');bg=Image.new('RGBA',s.size,'white');bg.alpha_composite(s);s=np.array(bg.convert('RGB')).astype(int)
ms=s.sum(2)<450;mt=t.sum(2)<450
print('IoU tổng',round((ms&mt).sum()/(ms|mt).sum(),4))
for nm,(x0,x1) in dict(D=(0,180),EL=(180,462),T=(420,585),A=(545,747),reg=(747,900)).items():
    a,b=ms[:,x0:x1],mt[:,x0:x1];print(nm,round((a&b).sum()/(a|b).sum(),4),end=' · ')
gs=(s[...,1]-s[...,0]>60);gt=(t[...,1]-t[...,0]>60);print('green',round((gs&gt).sum()/(gs|gt).sum(),4))
d=np.full(s.shape,255,'uint8');d[ms&mt]=(190,190,190);d[ms&~mt]=(230,40,40);d[~ms&mt]=(30,90,240)
Image.fromarray(d).resize((1800,496),Image.NEAREST).save('diff.png')
