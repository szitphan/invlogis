// Máy đo lề đều + bo đồng tâm (DEC-165, DEC-194) cho /figma-screen Bước 6 (A1).
// Chạy bằng use_figma (Plugin API), CHỈ ĐỌC: không vẽ, không sửa node.
// Cách dùng: đọc file này, thay ROOTS bằng id các artboard cần đo, gửi toàn văn làm `code`.
//   PAD_IDS (tuỳ chọn): id khung muốn ép đo lề dù tên không khớp.
// Kết quả mỗi artboard: fail (phải sửa), warn (chuyển reviewer), ok, lines.
//   FAIL · bo góc: khối có hình nằm trong vùng góc khung mà không đồng tâm (R = r + lề ± 1, hai lề góc chênh ≤ 1).
//   FAIL · lề: khung lớn (thẻ, nhóm, khối phụ, khối tóm tắt, thẻ chọn) có lề nhìn thấy 4 phía chênh > 1.
//   WARN · lề: khung có nền khác (auto-layout, lề ≥ 12, cao ≥ 56) lề nhìn thấy chênh > 1.
const ROOTS = ['<artboardId>'];
const PAD_IDS = [];

const SKIP = /^(Kẻ|Máy đo|Dải|Đường canh|Nhãn phương án|Lớp mờ|Pin|Home indicator|Chừa chỗ|Ghi chú|Chú thích)/;
const BIG = /^(Thẻ|Nhóm|Khối|Tóm tắt|Lựa chọn|Card|Group|Base \/ Card|\.card)/i;
const CTRL = /^(Nút|Button|Ô nhập|Ô tìm|Ô ·|Text Field|Chip|Tab|Công tắc|Switch|Thanh|Bar|Pill|Radio|Ô đầu dòng|Khung icon|Avatar|Ô icon|Icon|Sheet|Dialog|Toast|Status|Chân màn|Đầu màn|Header|Footer|Nav)/i;

function bv(n){if(n.visible===false)return false;const f='fills' in n&&Array.isArray(n.fills)&&n.fills.some(p=>p.visible!==false&&(p.opacity==null||p.opacity>0.02));const s='strokes' in n&&Array.isArray(n.strokes)&&n.strokes.some(p=>p.visible!==false)&&(n.strokeWeight===figma.mixed||n.strokeWeight>0);return f||s}
function bfill(n){if(!('fills' in n)||!Array.isArray(n.fills))return '';const p=n.fills.find(q=>q.visible!==false&&q.type==='SOLID');return p?['r','g','b'].map(k=>Math.round(p.color[k]*255)).join(',')+'@'+(p.opacity==null?1:+p.opacity.toFixed(2)):''}
function bcr(n){const m=Math.min(n.width,n.height)/2;if(n.type==='ELLIPSE')return [m,m,m,m];if(!('cornerRadius' in n))return [0,0,0,0];if(n.cornerRadius!==figma.mixed){const r=Math.min(n.cornerRadius,m);return [r,r,r,r]}return [n.topLeftRadius,n.topRightRadius,n.bottomRightRadius,n.bottomLeftRadius].map(r=>Math.min(r,m))}
function inIc(n){let a=n;while(a&&a.type!=='PAGE'){if(a.name&&a.name.startsWith('icon/'))return true;a=a.parent}return false}
function bco(n,root){let a=n.parent;while(a&&a.type!=='PAGE'){if(['FRAME','INSTANCE','COMPONENT'].includes(a.type)&&bv(a))return Math.max(...bcr(a))>0.5?a:null;if(a===root)return null;a=a.parent}return null}

// Bo góc: mỗi khối có hình (khác màu khung) → góc gần nhất của khung bo ngoài gần nhất.
function CHK3(root){const res=[];const all=root.findAll(n=>['FRAME','INSTANCE','COMPONENT','RECTANGLE','ELLIPSE'].includes(n.type)&&!SKIP.test(n.name)&&bv(n)&&!inIc(n)&&Math.min(n.width,n.height)>8);
 for(const I of all){const O=bco(I,root);if(!O)continue;if(bfill(I)===bfill(O)&&!(Array.isArray(I.strokes)&&I.strokes.length))continue;
  const a=I.absoluteBoundingBox,b=O.absoluteBoundingBox;if(!a||!b)continue;if(a.width>=b.width-0.5&&a.height>=b.height-0.5)continue;
  const ri=bcr(I),ro=bcr(O);const dl=a.x-b.x,dt=a.y-b.y,dr=b.x+b.width-a.x-a.width,db=b.y+b.height-a.y-a.height;let best=null;
  for(const [k,dx,dy,R,r] of [['TL',dl,dt,ro[0],ri[0]],['TR',dr,dt,ro[1],ri[1]],['BR',dr,db,ro[2],ri[2]],['BL',dl,db,ro[3],ri[3]]]){
   if(R<=0.5||dx<-0.5||dy<-0.5)continue;const zone=dx<R-0.5&&dy<R-0.5;if(!zone&&!(dx<R+12&&dy<R+12))continue;
   const eq=Math.abs(dx-dy)<=1,conc=Math.abs(R-(r+dx))<=1&&Math.abs(R-(r+dy))<=1;
   const f={I,O,k,R:Math.round(R*10)/10,r:Math.round(r*10)/10,dx:Math.round(dx),dy:Math.round(dy),zone,ok:zone?(eq&&conc):true,eq,conc};
   if(!best||(f.zone&&!best.zone)||(f.zone===best.zone&&!f.ok&&best.ok))best=f}
  if(best)res.push(best)}
 return res}

// Lề nhìn thấy: hộp bao nội dung thấy được (chữ, icon, hình, khối có nền khác màu khung).
// Bỏ đường kẻ (mỏng ≤ 2) và khối cùng màu nền khung (đi vào trong); khung giãn ngang chỉ tính tới mép nội dung của nó.
function CBOX(fr){let x0=1e9,y0=1e9,x1=-1e9,y1=-1e9;const pf=bfill(fr);
 const box=(ax,ay,aw,ah,onlyX)=>{x0=Math.min(x0,ax);x1=Math.max(x1,ax+aw);if(!onlyX){y0=Math.min(y0,ay);y1=Math.max(y1,ay+ah)}};
 const stroked=c=>'strokes' in c&&Array.isArray(c.strokes)&&c.strokes.some(p=>p.visible!==false)&&(c.strokeWeight===figma.mixed||c.strokeWeight>0);
 const walk=n=>{for(const c of n.children||[]){if(c.visible===false||SKIP.test(c.name)||c.layoutPositioning==='ABSOLUTE')continue;const a=c.absoluteBoundingBox;if(!a)continue;
   if(c.type==='LINE'||(['RECTANGLE','VECTOR'].includes(c.type)&&Math.min(a.width,a.height)<=2))continue;
   const shaped=bv(c)&&!(bfill(c)===pf&&!stroked(c));
   if(c.type==='TEXT'||c.name.startsWith('icon/')||c.type==='ELLIPSE'||c.type==='RECTANGLE'||shaped){box(a.x,a.y,a.width,a.height);continue}
   if('children' in c&&(c.layoutSizingHorizontal==='FILL'||c.layoutGrow===1)){const pl=c.paddingLeft||0,pr=c.paddingRight||0;box(a.x+pl,a.y,a.width-pl-pr,a.height,true)}
   if('children' in c)walk(c)}};
 walk(fr);return {x0,y0,x1,y1}}
function PADV(fr){const b=fr.absoluteBoundingBox,c=CBOX(fr);if(c.x0>c.x1)return null;return [c.y0-b.y,b.x+b.width-c.x1,b.y+b.height-c.y1,c.x0-b.x].map(v=>Math.round(v))}

const fmt=v=>Number.isInteger(v)?''+v:v.toFixed(1);
const nm=n=>n.name.slice(0,36)+' ('+n.id+')';
// Khung nằm trong instance (component thư viện): người vẽ không sửa được bên trong → WARN "sửa ở thư viện".
function libOf(n,root){let a=n,top=null;while(a&&a!==root&&a.type!=='PAGE'){if(a.type==='INSTANCE')top=a;a=a.parent}return top}
async function compName(n){if(n.type!=='INSTANCE')return '';const m=await n.getMainComponentAsync();if(!m)return '';return (m.parent&&m.parent.type==='COMPONENT_SET'?m.parent:m).name}

const out=[];
{let pg=await figma.getNodeByIdAsync(ROOTS[0]);while(pg&&pg.type!=='PAGE')pg=pg.parent;if(pg)await figma.setCurrentPageAsync(pg)}
for(const id of ROOTS){const root=await figma.getNodeByIdAsync(id);if(!root){out.push({id,error:'không thấy node'});continue}
 const lines=[];let fail=0,warn=0,ok=0;
 for(const f of CHK3(root)){
  if(f.ok){ok++;continue}
  const lib=libOf(f.O,root);const t=`bo góc · ${nm(f.I)} trong ${nm(f.O)} góc ${f.k}: R ${fmt(f.R)} ≠ r ${fmt(f.r)} + lề ${f.dx}${f.eq?'':' (lề '+f.dx+'/'+f.dy+')'} → cần r ${Math.max(0,Math.round(f.R-f.dx))} hoặc R ${Math.round(f.r+f.dx)}, hoặc lề ≥ R`;
  if(lib){warn++;lines.push(`WARN · ${t} — trong component ${lib.name.slice(0,30)}, sửa ở thư viện`)}else{fail++;lines.push('FAIL · '+t)}}
 const frames=root.findAll(n=>['FRAME','INSTANCE','COMPONENT'].includes(n.type)&&n.visible!==false&&!SKIP.test(n.name)&&!inIc(n)&&bv(n)&&n.width>=48&&n.height>=40&&'children' in n&&n.children.length>0);
 for(const f of frames){const cn=await compName(f);const big=PAD_IDS.includes(f.id)||((BIG.test(f.name)||BIG.test(cn))&&!CTRL.test(f.name));
  const other=!big&&!CTRL.test(f.name)&&!CTRL.test(cn)&&f.layoutMode&&f.layoutMode!=='NONE'&&Math.min(f.paddingTop,f.paddingRight,f.paddingBottom,f.paddingLeft)>=12&&f.height>=56&&f.width>=120;
  if(!big&&!other)continue;const pv=PADV(f);if(!pv)continue;const d=Math.max(...pv)-Math.min(...pv);
  if(d<=1){ok++;continue}
  const t=`lề · ${nm(f)}: trên ${pv[0]} · phải ${pv[1]} · dưới ${pv[2]} · trái ${pv[3]} (chênh ${d})`;const lib=libOf(f,root);
  if(big&&!lib){fail++;lines.push('FAIL · '+t)}else{warn++;lines.push('WARN · '+t+(lib?` — trong component ${lib.name.slice(0,30)}, sửa ở thư viện`:''))}}
 out.push({id,name:root.name,fail,warn,ok,lines})}
return out;
