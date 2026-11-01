#!/usr/bin/env python3
"""Khung chung trang review Foundations theo Untitled (khuôn trang Màu, Chữ) — 6 trang icon, logo, effect, spacing, radius, grids.

Mỗi trang là một file SPEC `_scripts/foundation_review/<slug>.py`; kit lo band, thanh tiến độ, màn thật, mục chọn, chốt, lưu db.
Dựng + kiểm: `python3 _scripts/foundation_review/build.py <slug>`. Xem luật viết SPEC ở BRIEF.md cùng thư mục.
Chỉ dùng biến thật của design-system/tokens.css; đề xuất đè bằng `.tp-f.tp-prop{...}` trong screens.proposal_css.
"""
import html
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
TCSS = (ROOT / "design-system/tokens.css").read_text(encoding="utf-8")
MARK = re.sub(r"<\?xml[^>]*>", "", (ROOT / "design/brand/innvie-v1/mark-color.svg").read_text())
ICONS = Path(__file__).parent / "_icons"
LUCIDE = "1.58.0"  # DEC-156
E = html.escape

PAGE_CSS = r"""
*{box-sizing:border-box}body{margin:0;font:14px/21px Inter,system-ui,sans-serif;color:#171717;background:#F5F7FB}
.band{background:#0036B5;color:#fff;padding:20px 32px;display:flex;align-items:center;gap:14px}
.band svg{width:36px;height:36px;flex:none}.band h1{margin:0;font:400 26px/32px "Cal Sans",Inter,sans-serif}.band p{margin:2px 0 0;opacity:.88}
.wrap{max-width:1180px;margin:0 auto;padding:16px 24px 80px}
h2{font:400 20px/28px "Cal Sans",Inter,sans-serif;margin:26px 0 10px;display:flex;align-items:center;gap:8px}
h2::before{content:"";width:10px;height:10px;background:#00A2FF;flex:none}
mark{background:color-mix(in srgb,#00A2FF 28%,transparent);color:inherit;padding:0 2px;border-radius:3px}
.muted{color:#64748B}.small{font-size:12.5px;line-height:18px}.rv code{font:12px/16px "JetBrains Mono",monospace;background:#EEF2F8;padding:1px 4px;border-radius:4px;color:#171717}
.lead{font-size:15px;line-height:23px;margin:6px 0 4px}
.kpis{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:10px;margin:14px 0}
.kpi{background:#fff;border:1px solid #E2E8F0;border-radius:14px;padding:12px 14px}.kpi b{display:block;font:400 26px/32px "Cal Sans",Inter}
.kpi span{font-size:12px;color:#475569}.kpi.bad b{color:#B42318}.kpi.ok b{color:#067647}
.cmp{width:100%;border-collapse:collapse;background:#fff;border:1px solid #E2E8F0;font-size:13px}
.cmp th,.cmp td{padding:7px 10px;border-bottom:1px solid #EEF2F6;text-align:left;vertical-align:top}.cmp th{background:#F8FAFC;color:#475569;font-weight:600;font-size:12px}
.cmp td.n{font-variant-numeric:tabular-nums;text-align:right;white-space:nowrap}.st-ok{color:#067647;font-weight:600}.st-gap{color:#B42318;font-weight:600}.st-diff{color:#B54708;font-weight:600}.st-own{color:#5925DC;font-weight:600}
.tw{overflow-x:auto;border-radius:14px;border:1px solid #E2E8F0;margin:10px 0}.tw .cmp{border:0}
.item{background:#fff;border:1px solid #E2E8F0;border-radius:16px;padding:16px 18px;margin:12px 0}
.item.done{border-color:#0036B5;box-shadow:0 0 0 1px #0036B5}
.item h3{margin:0 0 4px;font:600 16px/22px Inter;display:flex;gap:8px;align-items:baseline}.item h3 .id{font:600 12px "JetBrains Mono";color:#0036B5}
.grp{display:inline-block;font:600 11px/18px Inter;background:#E7EFFD;color:#0036B5;border-radius:999px;padding:0 8px;margin-bottom:6px}
.src{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin:10px 0}.src div{background:#F8FAFC;border:1px solid #EEF2F6;border-radius:10px;padding:8px 10px;font-size:12.5px;line-height:18px;min-width:0}
.src b{display:block;font-size:11px;color:#475569;margin-bottom:2px}
.newt{font-size:12.5px;margin:6px 0}.newt td{padding:4px 8px}
.pvt{font:600 12.5px/18px Inter;margin-top:10px}
.pvbox{background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:12px;margin-top:4px;overflow-x:auto}
.pvw{display:grid;grid-template-columns:1fr 1fr;gap:10px}.pv3{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.pane{border-radius:12px;padding:14px;border:1px solid var(--color-border-secondary);background:var(--color-bg-primary);color:var(--color-text-primary);min-height:60px;overflow:hidden;font-family:var(--font-body);min-width:0}
.pane>.lab{font:600 11px/14px Inter;color:var(--color-text-tertiary);margin-bottom:8px;display:block}
.cr{display:inline-block;width:fit-content;justify-self:start;font:600 10.5px/14px "JetBrains Mono";padding:1px 5px;border-radius:5px;margin-left:4px;white-space:nowrap}.cr.p{background:#DCFCE7;color:#14532D}.cr.f{background:#FEE2E2;color:#7F1D1D}
.opts{display:flex;flex-wrap:wrap;gap:6px;margin-top:10px;align-items:center}.opts button{border:1px solid #CBD5E1;background:#fff;border-radius:999px;padding:7px 13px;font:600 13px Inter;cursor:pointer;color:#171717}
.opts button[aria-pressed=true]{background:#0036B5;color:#fff;border-color:#0036B5}.opts .rec{font:600 10px Inter;color:#067647;margin-left:4px}
.opts button[aria-pressed=true] .rec{color:#BBF7D0}.opts button:focus-visible{outline:2px solid #0036B5;outline-offset:2px}
.rv textarea{width:100%;margin-top:8px;border:1px solid #CBD5E1;border-radius:10px;padding:8px 10px;font:13px Inter;min-height:38px;resize:vertical}
.saved{font-size:12px;color:#067647;margin-left:6px}.note{font-size:12.5px;line-height:18px;background:#FFFAEB;border:1px solid #FEDF89;border-radius:10px;padding:7px 10px;margin:8px 0}
.fin{background:#fff;border:2px solid #0036B5;border-radius:16px;padding:16px 18px}
.sticky{position:sticky;top:0;z-index:30;background:#F5F7FB;padding:8px 0;border-bottom:1px solid #E2E8F0;display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.pbar{height:8px;border-radius:99px;background:#E2E8F0;flex:1;min-width:120px;overflow:hidden}.pbar i{display:block;height:100%;background:#0036B5;width:0}
.othernav{display:flex;flex-wrap:wrap;gap:6px;margin:10px 0 0}.othernav a{font:600 12px/18px Inter;border:1px solid #CBD5E1;border-radius:999px;padding:3px 10px;background:#fff;color:#0036B5;text-decoration:none}.othernav a.on{background:#0036B5;color:#fff;border-color:#0036B5}
.tp-zone{position:relative}.tp-bar{display:flex;flex-wrap:wrap;gap:8px 16px;align-items:center;margin:12px 0;padding:8px 12px;position:sticky;top:48px;z-index:20;background:#fff;border:1px solid #D4D4D4;border-radius:10px;box-shadow:0 4px 12px rgba(16,24,40,.08)}
.tp-seg{display:inline-flex;border:1px solid #D4D4D4;border-radius:8px;overflow:hidden}
.tp-seg button{all:unset;cursor:pointer;padding:6px 12px;font:500 13px/18px Inter,sans-serif;color:#404040;background:#fff}
.tp-seg button[aria-pressed=true]{background:#0036B5;color:#fff}.tp-seg button:focus-visible{outline:2px solid #0036B5;outline-offset:-2px}
.tp-lab{font:500 12px/16px Inter,sans-serif;color:#525252;margin-right:6px}
.tp-h{font:600 14px/20px Inter,sans-serif;margin:20px 0 8px;color:#171717}.tp-h small{font-weight:400;color:#525252}
.tp-scroll{overflow-x:auto;padding-bottom:8px}.tp-row{display:flex;gap:16px;align-items:flex-start;width:max-content}
/* màn demo — mọi số đo đọc từ token, đề xuất đè ở .tp-f.tp-prop */
.tp-f{--d-logo:24px;background:var(--color-bg-primary);color:var(--color-text-primary);border:1px solid var(--color-border-secondary);border-radius:var(--radius-card);overflow:hidden;font-family:var(--font-body);position:relative}
.tp-web{width:1180px;display:grid;grid-template-columns:216px minmax(0,1fr);min-height:560px}.tp-webs{width:680px;min-height:520px}.tp-webc{width:680px;min-height:320px}
.tp-app{width:375px;min-height:720px;display:flex;flex-direction:column}
.tp-side{border-right:1px solid var(--color-border-secondary);padding:var(--space-xl) var(--space-lg);display:grid;gap:var(--space-xs);align-content:start}
.tp-logo{display:flex;align-items:center;gap:var(--space-md);margin-bottom:var(--space-lg)}.tp-logo svg{height:var(--d-logo);width:auto}
.tp-nav{display:flex;align-items:center;gap:var(--space-md);padding:var(--space-sm) var(--space-md);border-radius:var(--radius-menu-item);color:var(--color-text-tertiary)}.tp-nav.on{background:var(--color-bg-selected);color:var(--color-text-primary)}
.tp-grp{margin-top:var(--space-lg);padding:0 var(--space-md);color:var(--color-text-tertiary)}
.tp-main{padding:var(--layout-screen-inset);display:grid;grid-template-columns:minmax(0,1fr);gap:var(--layout-title-gap);align-content:start;min-width:0}.tp-pad{padding:var(--layout-screen-inset);display:grid;gap:var(--layout-list-gap);align-content:start;flex:1}
.tp-top{display:flex;justify-content:space-between;align-items:center;gap:var(--space-lg)}.tp-sub{color:var(--color-text-tertiary)}
.tp-card{border:1px solid var(--elev-1-border);border-radius:var(--radius-card);padding:var(--layout-card-padding);display:grid;gap:var(--space-md);background:var(--color-bg-primary);box-shadow:var(--elev-1);min-width:0}
.tp-kpis{display:grid;grid-template-columns:repeat(3,1fr);gap:var(--space-lg)}.tp-num{font-variant-numeric:tabular-nums}
.tp-tb{width:100%;border-collapse:collapse}.tp-tb th{text-align:left;padding:var(--space-md) var(--space-lg);color:var(--color-text-tertiary);border-bottom:1px solid var(--color-border-secondary)}.tp-tb td{padding:var(--space-lg);border-bottom:1px solid var(--color-border-secondary);vertical-align:top}
.tp-chip{display:inline-flex;align-items:center;height:22px;padding:0 var(--space-md);border-radius:var(--radius-chip);font-size:var(--font-size-xs);line-height:var(--line-height-xs-tight);font-weight:500;white-space:nowrap}
.tp-g{background:var(--color-utility-green-50);color:var(--color-utility-green-700)}.tp-b{background:var(--color-utility-blue-50);color:var(--color-utility-blue-700)}.tp-y{background:var(--color-utility-yellow-50);color:var(--color-utility-yellow-700)}
.tp-kv{display:grid;grid-template-columns:120px minmax(0,1fr);gap:var(--space-sm) var(--space-lg);margin:0}.tp-kv dt{color:var(--color-text-tertiary)}.tp-kv dd{margin:0}
.tp-btn{display:inline-flex;align-items:center;justify-content:center;gap:var(--space-sm);height:var(--control-height-md);padding:0 var(--space-xl);border-radius:var(--radius-control);background:var(--color-action-primary);color:var(--color-text-inverse);white-space:nowrap}
.tp-btn.sec{background:var(--color-bg-primary);color:var(--color-text-primary);box-shadow:inset 0 0 0 1px var(--color-border-primary)}.tp-btn.wide{width:100%}
.tp-fld{display:grid;gap:var(--space-xs)}.tp-inp{display:flex;align-items:center;gap:var(--space-md);min-height:var(--control-height-md);border:1px solid var(--color-border-input);border-radius:var(--radius-field);padding:0 var(--space-lg);background:var(--color-bg-primary)}.tp-ph{color:var(--color-text-placeholder)}.tp-err{color:var(--color-text-error-primary)}.tp-inp.e{border-color:var(--color-border-error)}
.tp-appbar{padding:var(--space-lg) var(--layout-screen-inset);border-bottom:1px solid var(--color-border-secondary);display:flex;align-items:center;gap:var(--space-md)}.tp-foot{padding:var(--space-lg) var(--layout-screen-inset);border-top:1px solid var(--color-border-secondary);display:flex;gap:var(--space-md)}
.tp-menu{position:absolute;right:var(--layout-screen-inset);top:96px;width:200px;background:var(--color-bg-primary_alt);border:1px solid var(--elev-2-border);border-radius:var(--radius-menu);box-shadow:var(--elev-2);padding:var(--space-xs);display:grid;gap:2px;z-index:2}
.tp-menu>span{display:flex;align-items:center;gap:var(--space-md);padding:var(--space-sm) var(--space-md);border-radius:var(--radius-menu-item)}
.tp-scrim{position:absolute;inset:0;background:var(--color-bg-overlay);display:flex}.tp-scrim.c{align-items:center;justify-content:center}.tp-scrim.b{align-items:flex-end}
.tp-dlg{background:var(--color-bg-primary_alt);display:grid;gap:var(--space-lg);padding:var(--space-2xl);border-radius:var(--radius-overlay);width:440px;box-shadow:var(--elev-3)}.tp-sheet{width:100%;border-radius:var(--radius-overlay) var(--radius-overlay) 0 0}.tp-acts{display:flex;gap:var(--space-md);justify-content:flex-end}
.tp-ic{display:inline-flex;flex:none}.tp-ic svg{width:var(--ic,16px);height:var(--ic,16px);display:block}
.tp-ic-sm{--ic:var(--icon-size-sm)}.tp-ic-md{--ic:var(--icon-size-md)}.tp-ic-lg{--ic:var(--icon-size-lg)}.tp-fg2{color:var(--color-fg-secondary)}
.tp-note{position:absolute;z-index:3;pointer-events:none}
/* nhãn số đo đọc trực tiếp từ trình duyệt */
[data-tags="on"] [data-tag]{outline:1px dashed color-mix(in srgb,#00A2FF 70%,transparent);outline-offset:-1px;position:relative}
[data-tags="on"] [data-tag]::after{content:attr(data-tag);position:absolute;right:0;top:0;z-index:4;padding:0 4px;border-radius:0 0 0 4px;background:#0036B5;color:#fff;font:500 10px/14px "JetBrains Mono",monospace;white-space:nowrap}
/* lưới cột phủ lên màn (trang Grids) */
.tp-gridov{position:absolute;pointer-events:none;inset:0 auto 0 auto;display:none;z-index:3}
[data-gridov="on"] .tp-gridov{display:grid}.tp-gridov i{background:color-mix(in srgb,#F04438 14%,transparent);height:100%;display:block}
@media(max-width:820px){.src,.pvw,.pv3{grid-template-columns:minmax(0,1fr)}.wrap{padding:12px 14px 60px}.band{padding:16px 18px}}
"""

PAGE_JS = r"""
const D=JSON.parse(document.getElementById('data').textContent);const $=s=>document.querySelector(s);const $$=s=>[...document.querySelectorAll(s)];
const ST={};let db=null,uid=null;const LS='frv-'+D.slug+'-';const E=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const ALL=[...D.items.map(i=>i.id),'_final'];
function paint(){D.items.forEach(it=>{const h=document.querySelector(`.item[data-id="${it.id}"]`);if(!h)return;const s=ST[it.id]||{};h.classList.toggle('done',!!s.choice);h.querySelectorAll('[data-a]').forEach(b=>b.setAttribute('aria-pressed',String(s.choice===b.dataset.a)));const sv=h.querySelector('[data-saved]');if(sv)sv.textContent=s.choice?'Đã lưu':'';const ta=h.querySelector('textarea');if(ta&&document.activeElement!==ta)ta.value=s.note||''});
 const f=ST._final||{},fh=$('#fin');if(fh){fh.querySelectorAll('[data-a]').forEach(b=>b.setAttribute('aria-pressed',String(f.choice===b.dataset.a)));const sv=fh.querySelector('[data-saved]');if(sv)sv.textContent=f.choice?'Đã lưu':'';const ta=fh.querySelector('textarea');if(ta&&document.activeElement!==ta)ta.value=f.note||''}
 const n=D.items.filter(i=>ST[i.id]?.choice).length;$('#cnt').textContent=n;$('#pfill').style.width=(100*n/Math.max(1,D.items.length))+'%'}
async function save(id){const x={...ST[id],at:Date.now(),by:uid};try{localStorage.setItem(LS+id,JSON.stringify(x))}catch(e){}if(db)try{await db.doc('decisions/'+id).set(x)}catch(e){}}
document.addEventListener('click',e=>{const b=e.target.closest('button[data-a]');if(!b)return;const id=b.closest('[data-id]').dataset.id;ST[id]={...(ST[id]||{}),choice:ST[id]?.choice===b.dataset.a?null:b.dataset.a};paint();save(id)});
document.addEventListener('input',e=>{const ta=e.target;if(ta.tagName!=='TEXTAREA')return;const h=ta.closest('[data-id]');if(!h)return;const id=h.dataset.id;ST[id]={...(ST[id]||{}),note:ta.value};clearTimeout(ta._t);ta._t=setTimeout(()=>save(id),500)});
ALL.forEach(id=>{try{const x=JSON.parse(localStorage.getItem(LS+id)||'null');if(x)ST[id]=x}catch(e){}});paint();
(async()=>{if(!window.claude?.use)return;const [d,u]=await Promise.all([claude.use('db'),claude.use('user')]);if(!d)return;db=d;try{uid=u?await u.id():null}catch(e){}
 let first=true;db.collection('decisions').onSnapshot(sn=>{const inDb=new Set(sn.docs.map(x=>x.id));if(first){first=false;Object.keys(ST).forEach(id=>{if(!inDb.has(id)&&(ST[id].choice||ST[id].note))save(id)})}
 let ch=false;sn.docs.forEach(x=>{const v=x.data();if(v&&(!ST[x.id]||(v.at||0)>(ST[x.id].at||0))){ST[x.id]=v;ch=true}});if(ch)paint()},()=>{})})();
// tỉ lệ tương phản đo trên trang: <span class="cr" data-fg="--x" data-bg="--y" data-min="3">
function rgb(c){const m=c.match(/rgba?\(([^)]+)\)/);if(m){const p=m[1].split(/[ ,\/]+/).map(parseFloat);return p.length>3?p:[...p,1]}return null}
function col(el,v,prop){const p=document.createElement('i');p.style.cssText=`position:absolute;width:0;height:0;${prop}:var(${v})`;el.appendChild(p);const c=getComputedStyle(p)[prop==='color'?'color':'backgroundColor'];p.remove();const cv=document.createElement('canvas').getContext('2d');cv.fillStyle=c;cv.fillRect(0,0,1,1);const d=cv.getImageData(0,0,1,1).data;return[d[0],d[1],d[2],d[3]/255]}
function lum(a){const f=x=>{x/=255;return x<=.03928?x/12.92:Math.pow((x+.055)/1.055,2.4)};return .2126*f(a[0])+.7152*f(a[1])+.0722*f(a[2])}
function over(f,b){const a=f[3];return[0,1,2].map(i=>f[i]*a+b[i]*(1-a))}
function contrast(){$$('.cr[data-fg]').forEach(s=>{const b=col(s.parentElement,s.dataset.bg,'background-color'),f=col(s.parentElement,s.dataset.fg,'color');const bb=over(b,[255,255,255]),ff=over(f,bb);const l1=lum(ff),l2=lum(bb);const r=(Math.max(l1,l2)+.05)/(Math.min(l1,l2)+.05);const min=+(s.dataset.min||4.5);s.textContent=r.toFixed(2).replace('.',',')+':1';s.classList.toggle('p',r>=min);s.classList.toggle('f',r<min)})}
// nhãn số đo màn demo: chế độ do trang chọn (spacing, radius, effect, icon)
const TAG={radius:{sel:'.tp-card,.tp-btn,.tp-inp,.tp-dlg,.tp-chip,.tp-nav.on,.tp-menu,.tp-menu>span',f:c=>'r '+Math.round(parseFloat(c.borderTopLeftRadius))},
 spacing:{sel:'.tp-main,.tp-pad,.tp-card,.tp-side,.tp-appbar,.tp-foot,.tp-dlg',f:c=>{const n=x=>Math.round(parseFloat(x)||0);const g=c.rowGap&&c.rowGap!=='normal'?' · gap '+n(c.rowGap):'';return'p '+n(c.paddingTop)+'/'+n(c.paddingLeft)+g}},
 effect:{sel:'.tp-card,.tp-menu,.tp-dlg,.tp-scrim',f:(c,e)=>e.classList.contains('tp-scrim')?'overlay · blur '+(c.backdropFilter==='none'?'0':c.backdropFilter):(c.boxShadow==='none'?'không bóng':c.boxShadow.split(/,(?![^(]*\))/).length+' lớp bóng')},
 icon:{sel:'.tp-ic',f:(c,e)=>{const s=e.querySelector('svg');return s?Math.round(s.getBoundingClientRect().width)+' · nét '+(+getComputedStyle(s).strokeWidth||0):''}}};
function tag(){const W=$('#tpWrap');if(!W)return;const k=TAG[D.tagKind];if(!k)return;W.querySelectorAll(k.sel).forEach(e=>{e.setAttribute('data-tag',k.f(getComputedStyle(e),e))})}
$$('#tpBar .tp-seg').forEach(s=>s.addEventListener('click',ev=>{const b=ev.target.closest('button');if(!b)return;s.querySelectorAll('button').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));const W=$('#tpWrap'),k=s.dataset.k,v=b.dataset.v;
 if(k==='set')W.querySelectorAll('.tp-f').forEach(f=>f.classList.toggle('tp-prop',v==='prop'));if(k==='theme')W.setAttribute('data-theme',v);if(k==='tags')W.setAttribute('data-tags',v);if(k==='gridov')W.setAttribute('data-gridov',v);
 tag();contrast();if(window.afterToggle)afterToggle()}));
// tự kiểm: lỗi JS, biến CSS không có giá trị, phần tử tràn khung, tương phản rớt ngoài mục đánh dấu cho phép
const errs=[];addEventListener('error',e=>errs.push(String(e.message)));
function selfcheck(){const out={errors:errs,emptyVars:[],overflow:[],crFail:[],items:D.items.length};
 const seen=new Set();$$('.rv [style]').forEach(el=>{(el.getAttribute('style').match(/var\(--[\w-]+/g)||[]).forEach(v=>{const n=v.slice(4);if(!seen.has(n)&&!getComputedStyle(el).getPropertyValue(n).trim()){seen.add(n);out.emptyVars.push(n)}})});
 $$('.item,.pane,.tp-card').forEach(el=>{if(el.closest('.pvbox')&&!el.classList.contains('pane'))return;if(el.scrollWidth>el.clientWidth+1&&getComputedStyle(el).overflowX==='visible')out.overflow.push((el.dataset.id||el.className)+' '+el.scrollWidth+'>'+el.clientWidth)});
 $$('.cr.f').forEach(s=>out.crFail.push(s.dataset.fg+' / '+s.dataset.bg+' '+s.textContent));
 const p=document.createElement('pre');p.id='__selfcheck';p.style.display='none';p.textContent=JSON.stringify(out);document.body.appendChild(p)}
function ready(){tag();contrast();if(window.afterToggle)afterToggle();selfcheck()}
if(document.fonts&&document.fonts.ready)document.fonts.ready.then(ready);else ready();
"""


def icon(name, cls="tp-ic-md"):
    """Icon Lucide thật (bản DEC-156), cache ở _icons/; màu theo currentColor, cỡ theo lớp tp-ic-{sm,md,lg} = biến icon/size/*."""
    ICONS.mkdir(exist_ok=True)
    p = ICONS / f"{name}.svg"
    if not p.exists():
        r = subprocess.run(["curl", "-sSLf", "--max-time", "20", f"https://cdn.jsdelivr.net/npm/lucide-static@{LUCIDE}/icons/{name}.svg"],
                           capture_output=True, text=True)
        if r.returncode:
            raise SystemExit(f"Không có icon Lucide '{name}' ({LUCIDE}): {r.stderr.strip()}")
        p.write_text(r.stdout)
    s = re.sub(r"<!--.*?-->", "", p.read_text(), flags=re.S)
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r'class="[^"]*"', 'aria-hidden="true"', s)
    return f'<span class="tp-ic {cls}">{s}</span>'


def cr(fg, bg, minimum=4.5):
    """Nhãn tương phản đo trên trang. fg, bg là tên token dạng color/text/primary."""
    return f'<span class="cr" data-fg="{v(fg)}" data-bg="{v(bg)}" data-min="{minimum}"></span>'


def v(token):
    return "--" + token.replace("/", "-")


def panes(body, modes=("light", "dark"), platforms=("web",), labels=None):
    """Xem thử trong item: một ô cho mỗi tổ hợp chế độ × nền tảng, biến đọc đúng theo data-theme/data-platform."""
    name = {"light": "Sáng", "dark": "Tối", "web": "Web", "mobile": "Mobile"}
    cells = []
    for m in modes:
        for p in platforms:
            lab = " · ".join(([name[m]] if len(modes) > 1 else []) + ([name[p]] if len(platforms) > 1 else []))
            b = body(m, p) if callable(body) else body
            cells.append(f'<div class="pane" data-theme="{m}" data-platform="{p}">'
                         + (f'<span class="lab">{E(lab)}</span>' if lab else "") + f"{b}</div>")
    cls = "pv3" if len(cells) == 3 else "pvw" if len(cells) in (2, 4) else ""
    return f'<div class="{cls}">{"".join(cells)}</div>'


def rows(headers, data, cls="cmp"):
    """Bảng đối chiếu. Ô bắt đầu bằng 'n:' căn phải số; ô là html sẵn."""
    th = "".join(f"<th>{h}</th>" for h in headers)
    tr = []
    for r in data:
        rc = ""
        if isinstance(r, dict):
            rc, r = f' class="{r["cls"]}"', r["cells"]
        tds = "".join(f'<td class="n">{c[2:]}</td>' if isinstance(c, str) and c.startswith("n:") else f"<td>{c}</td>" for c in r)
        tr.append(f"<tr{rc}>{tds}</tr>")
    return f'<div class="tw"><table class="{cls}"><thead><tr>{th}</tr></thead><tbody>{"".join(tr)}</tbody></table></div>'


def t(cls, text, extra=""):
    """Chữ theo text style thật: t('title-1','Lệnh vận tải')."""
    return f'<span class="type-{cls} {extra}" style="display:block">{text}</span>'


def mini_mark():
    p = ROOT / "design/brand/invlogis/logo/invlogis-symbol.svg"
    return re.sub(r"<\?xml[^>]*>", "", p.read_text()) if p.exists() else MARK


def demo_screens(logo_svg=None):
    """Bộ màn mẫu (DEC ds-demo-screen-set): danh sách, chi tiết, biểu mẫu, xác nhận cho Web + App, mọi số đọc từ token."""
    logo = logo_svg or mini_mark()
    nav = lambda ic, x, on="": f'<div class="tp-nav {on}">{icon(ic)}<span class="type-label">{x}</span></div>'
    chip = lambda c, x: f'<span class="tp-chip {c}">{x}</span>'
    kpi = lambda a, b, c: f'<div class="tp-card"><div class="type-caption tp-sub">{a}</div><div class="type-display tp-num">{b}</div><div class="type-hint tp-sub">{c}</div></div>'
    row = lambda code, r, s, m, tm, c, x: (f'<tr><td><div class="type-code">{code}</div></td><td><div class="type-body">{r}</div><div class="type-caption tp-sub">{s}</div></td>'
                                           f'<td><span class="type-body tp-num">{m}</span></td><td><span class="type-caption tp-sub tp-num">{tm}</span></td><td>{chip(c, x)}</td>'
                                           f'<td><span class="tp-fg2">{icon("ellipsis-vertical")}</span></td></tr>')
    web_list = (f'<div class="tp-f tp-web" data-platform="web"><aside class="tp-side"><div class="tp-logo">{logo}<span class="type-title-3">Invlogis</span></div>'
                f'<div class="type-caption-caps tp-grp">Vận hành</div>{nav("truck", "Lệnh vận tải", "on")}{nav("container", "Phương tiện")}{nav("users", "Tài xế")}{nav("fuel", "Nhiên liệu")}'
                f'<div class="type-caption-caps tp-grp">Danh mục</div>{nav("building-2", "Khách hàng")}{nav("settings", "Cài đặt")}</aside>'
                f'<div class="tp-main"><div class="tp-top"><div><div class="type-title-1">Lệnh vận tải</div><div class="type-body tp-sub">Theo dõi và duyệt lệnh trong ngày.</div></div>'
                f'<span class="tp-btn">{icon("plus")}<span class="type-label">Tạo lệnh</span></span></div>'
                f'<div class="tp-kpis">{kpi("Lệnh đang chạy", "128", "Tăng 12 so với hôm qua")}{kpi("Chờ duyệt", "16", "Quá hạn 3 lệnh")}{kpi("Doanh thu hôm nay", "412 tr ₫", "Cập nhật lúc 14:30")}</div>'
                f'<div class="tp-card"><div class="type-title-3">Danh sách lệnh</div><table class="tp-tb"><thead><tr><th><span class="type-caption-caps">Mã lệnh</span></th><th><span class="type-caption-caps">Tuyến · xe</span></th><th><span class="type-caption-caps">Cước</span></th><th><span class="type-caption-caps">Thời gian</span></th><th><span class="type-caption-caps">Trạng thái</span></th><th></th></tr></thead><tbody>'
                + row("LVT-2026-0412", "Cát Lái → KCN Long Hậu", "51C-482.15 · Nguyễn Văn Hoà", "1.250.000 ₫", "14:30 · 01/11/2026", "tp-b", "Đang chạy")
                + row("LVT-2026-0411", "ICD Phước Long → Bình Dương", "51D-120.77 · Trần Quốc Việt", "2.480.000 ₫", "09:15 · 01/11/2026", "tp-g", "Hoàn thành")
                + row("LVT-2026-0409", "Cảng Hiệp Phước → Đồng Nai", "50H-338.02 · Lê Thị Ệ", "980.000 ₫", "16:40 · 31/10/2026", "tp-y", "Chờ duyệt")
                + f'</tbody></table></div><div class="tp-menu" style="top:auto;bottom:40px">'
                f'<span>{icon("pencil")}<span class="type-body">Sửa lệnh</span></span><span>{icon("copy")}<span class="type-body">Nhân bản</span></span><span class="tp-err">{icon("trash-2")}<span class="type-body">Huỷ lệnh</span></span></div></div></div>')
    kv = '<dl class="tp-kv"><dt><span class="type-caption">Tuyến</span></dt><dd><div class="type-body">Cảng Cát Lái → KCN Long Hậu, Cần Giuộc, Long An</div></dd><dt><span class="type-caption">Xe · mooc</span></dt><dd><div class="type-body">51C-482.15 · mooc 51R-091.44</div></dd><dt><span class="type-caption">Tài xế</span></dt><dd><div class="type-body">Nguyễn Văn Hoà</div></dd><dt><span class="type-caption">Cước</span></dt><dd><div class="type-body tp-num">1.250.000 ₫</div></dd></dl>'
    fields = lambda: (f'<div class="tp-fld"><span class="type-label">Mã container</span><div class="tp-inp"><span class="type-body">TCLU 482915-3</span></div><div class="type-hint tp-sub">11 ký tự, gồm 4 chữ và 7 số.</div></div>'
                      f'<div class="tp-fld"><span class="type-label">Điểm giao</span><div class="tp-inp"><span class="type-body tp-ph" style="flex:1">Chọn điểm giao</span><span class="tp-fg2">{icon("chevron-down")}</span></div></div>'
                      f'<div class="tp-fld"><span class="type-label">Cước dự kiến</span><div class="tp-inp e"><span class="type-body tp-num">12.500</span></div><div class="type-hint tp-err">Cước thấp hơn định mức của tuyến. Kiểm tra lại số tiền.</div></div>')
    web_detail = (f'<div class="tp-f tp-webs" data-platform="web"><div class="tp-main"><div class="tp-top"><div><div class="type-code tp-sub">LVT-2026-0412</div><div class="type-title-1">Chi tiết lệnh vận tải</div></div>{chip("tp-b", "Đang chạy")}</div>'
                  f'<div class="tp-card"><div class="type-title-3">Thông tin chuyến</div>{kv}</div><div class="tp-card"><div class="type-title-3">Ghi chú điều vận</div><div class="type-body">Tài xế nhận container tại cổng B, kiểm tra niêm phong trước khi rời cảng.</div><div class="type-caption tp-sub">Cập nhật 14:30 · 01/11/2026</div></div></div></div>')
    web_form = f'<div class="tp-f tp-webs" data-platform="web"><div class="tp-main"><div class="type-title-1">Tạo lệnh vận tải</div><div class="tp-card"><div class="type-title-3">Hàng hoá</div>{fields()}</div></div></div>'
    web_dlg = ('<div class="tp-f tp-webc" data-platform="web"><div class="tp-scrim c"><div class="tp-dlg"><div class="type-title-2">Duyệt lệnh LVT-2026-0412?</div><div class="type-body tp-sub">Lệnh sẽ gửi tới tài xế Nguyễn Văn Hoà ngay sau khi duyệt.</div>'
               '<div class="tp-acts"><span class="tp-btn sec"><span class="type-label">Để sau</span></span><span class="tp-btn"><span class="type-label">Duyệt lệnh</span></span></div></div></div></div>')
    bar = lambda ti, sub="", ic="": f'<div class="tp-appbar">{ic}<div style="flex:1;min-width:0"><div class="type-title-2">{ti}</div>' + (f'<div class="type-caption tp-sub">{sub}</div>' if sub else "") + f'</div><span class="tp-fg2">{icon("bell", "tp-ic-lg")}</span></div>'
    acard = lambda code, c, x, r, s, m, tm: (f'<div class="tp-card"><div class="tp-top"><span class="type-code tp-sub">{code}</span>{chip(c, x)}</div><div class="type-title-3">{r}</div><div class="type-body tp-sub">{s}</div>'
                                             f'<div class="tp-top"><span class="type-label tp-num">{m}</span><span class="type-caption tp-sub tp-num">{tm}</span></div></div>')
    cards = (acard("LVT-2026-0412", "tp-b", "Đang chạy", "Cát Lái → KCN Long Hậu", "51C-482.15 · Nguyễn Văn Hoà", "1.250.000 ₫", "14:30 · 01/11")
             + acard("LVT-2026-0411", "tp-g", "Hoàn thành", "ICD Phước Long → Bình Dương", "51D-120.77 · Trần Quốc Việt", "2.480.000 ₫", "09:15 · 01/11")
             + acard("LVT-2026-0409", "tp-y", "Chờ duyệt", "Cảng Hiệp Phước → Đồng Nai", "50H-338.02 · Lê Thị Ệ", "980.000 ₫", "16:40 · 31/10"))
    app_list = f'<div class="tp-f tp-app" data-platform="mobile">{bar("Lệnh của tôi", "3 lệnh trong hôm nay")}<div class="tp-pad">{cards}</div></div>'
    app_detail = (f'<div class="tp-f tp-app" data-platform="mobile">{bar("Chi tiết lệnh", "LVT-2026-0412", icon("chevron-left", "tp-ic-lg"))}<div class="tp-pad"><div class="tp-card"><div class="type-heading">Thông tin chuyến</div>{kv}</div>'
                  f'<div class="tp-card"><div class="type-heading">Ghi chú điều vận</div><div class="type-body">Tài xế nhận container tại cổng B, kiểm tra niêm phong trước khi rời cảng.</div></div></div><div class="tp-foot"><span class="tp-btn wide"><span class="type-label">Bắt đầu chuyến</span></span></div></div>')
    app_form = f'<div class="tp-f tp-app" data-platform="mobile">{bar("Báo cáo sự cố", "", icon("chevron-left", "tp-ic-lg"))}<div class="tp-pad">{fields()}</div><div class="tp-foot"><span class="tp-btn wide"><span class="type-label">Gửi báo cáo</span></span></div></div>'
    app_sheet = (f'<div class="tp-f tp-app" data-platform="mobile">{bar("Lệnh của tôi", "3 lệnh trong hôm nay")}<div class="tp-pad">{cards}</div><div class="tp-scrim b"><div class="tp-dlg tp-sheet"><div class="type-title-3">Kết thúc chuyến LVT-2026-0412?</div>'
                 '<div class="type-body tp-sub">Bạn sẽ không sửa được số km sau khi kết thúc. Kiểm tra lại trước khi xác nhận.</div><span class="tp-btn wide"><span class="type-label">Kết thúc chuyến</span></span><span class="tp-btn wide sec"><span class="type-label">Để sau</span></span></div></div></div>')
    return (f'<div class="tp-h">Web <small>· danh sách, có menu nổi</small></div><div class="tp-scroll"><div class="tp-row">{web_list}</div></div>'
            f'<div class="tp-h">Web <small>· chi tiết, biểu mẫu, hộp xác nhận</small></div><div class="tp-scroll"><div class="tp-row">{web_detail}{web_form}{web_dlg}</div></div>'
            f'<div class="tp-h">App <small>· danh sách, chi tiết, biểu mẫu, sheet xác nhận (rộng 375)</small></div><div class="tp-scroll"><div class="tp-row">{app_list}{app_detail}{app_form}{app_sheet}</div></div>')


NAV = [("icon", "Icon"), ("logo", "Logo"), ("effect", "Effect styles"), ("spacing", "Khoảng cách"), ("radius", "Bo góc"), ("grids", "Lưới")]


def _item(it):
    tok = ""
    if it.get("tokens"):
        rs = "".join(f"<tr><td><code>{E(a)}</code></td><td>{b}</td><td class='muted'>{c}</td></tr>" for a, b, c in it["tokens"])
        tok = f'<div class="tw"><table class="cmp newt"><tr><th>Token đề xuất</th><th>Giá trị</th><th>Dùng cho</th></tr>{rs}</table></div>'
    note = f'<div class="note">{it["note"]}</div>' if it.get("note") else ""
    pv = f'<div class="pvt">Xem thử</div><div class="pvbox">{it["pv"]}</div>' if it.get("pv") else ""
    opts = "".join(f'<button data-a="{E(k)}" aria-pressed="false">{E(l)}{"<span class=rec>khuyến nghị</span>" if r else ""}</button>' for k, l, r in it["opts"])
    return (f'<div class="item" id="{it["id"]}" data-id="{it["id"]}"><span class="grp">{E(it["grp"])}</span><h3><span class="id">{it["id"]}</span>{E(it["title"])}</h3><div>{it["why"]}</div>'
            f'<div class="src"><div><b>Untitled UI v8</b>{it["untitled"]}</div><div><b>Mình đang có</b>{it["ours"]}</div><div><b>Astryx hiện tại (mốc)</b>{it["astryx"]}</div></div>'
            f'{tok}{note}{pv}<div class="opts">{opts}<span class="saved" data-saved></span></div><textarea placeholder="Ghi chú (tuỳ chọn)"></textarea></div>')


def render(spec, urls=None):
    """SPEC → một trang HTML hoàn chỉnh. urls: {slug: link} cho thanh chuyển trang."""
    urls = urls or {}
    nav = "".join(f'<a class="{"on" if s == spec["slug"] else ""}" href="{urls.get(s, "#")}">{n}</a>' for s, n in NAV if s == spec["slug"] or s in urls)
    kp = "".join(f'<div class="kpi {c}"><b>{a}</b><span>{b}</span></div>' for a, b, c in spec["kpis"])
    sc = spec.get("screens") or {}
    gridbtn = ('<span><span class="tp-lab">Phủ lưới</span><span class="tp-seg" data-k="gridov"><button data-v="off" aria-pressed="true">Tắt</button><button data-v="on" aria-pressed="false">Bật</button></span></span>'
               if sc.get("gridov") else "")
    seg_set = ('<span><span class="tp-lab">Bộ giá trị</span><span class="tp-seg" data-k="set"><button data-v="cur" aria-pressed="false">Hiện tại</button><button data-v="prop" aria-pressed="true">Sau khi đổi</button></span></span>'
               if sc.get("proposal_css") else "")
    tags = ('<span><span class="tp-lab">Nhãn số đo</span><span class="tp-seg" data-k="tags"><button data-v="off" aria-pressed="true">Tắt</button><button data-v="on" aria-pressed="false">Bật</button></span></span>'
            if spec.get("tag_kind") else "")
    screens = ""
    if sc:
        body = demo_screens(sc.get("logo_svg"))
        if sc.get("proposal_css"):
            body = body.replace('class="tp-f ', 'class="tp-f tp-prop ')
        if sc.get("overlay_html"):
            body = sc["overlay_html"](body)
        screens = (f'<h2>{E(sc.get("title", "Xem trên màn thật"))}</h2><p class="small">{sc["intro"]}</p><div class="tp-zone">'
                   f'<div class="tp-bar" id="tpBar">{seg_set}<span><span class="tp-lab">Chế độ</span><span class="tp-seg" data-k="theme"><button data-v="light" aria-pressed="true">Sáng</button><button data-v="dark" aria-pressed="false">Tối</button></span></span>{tags}{gridbtn}</div>'
                   f'<div id="tpWrap" data-tags="off" data-theme="light" data-gridov="off">{body}</div></div>')
    secs = "".join(f'<h2>{E(s["title"])}</h2>' + (f'<p class="small">{s["intro"]}</p>' if s.get("intro") else "") + s["html"] for s in spec["sections"])
    items = "".join(_item(i) for i in spec["items"])
    blob = json.dumps({"slug": spec["slug"], "tagKind": spec.get("tag_kind"), "items": [{"id": i["id"]} for i in spec["items"]]}, ensure_ascii=False).replace("</", "<\\/")
    fin = spec["final"]
    fopts = '<button data-a="approve" aria-pressed="false">Duyệt, áp theo lựa chọn từng mục</button><button data-a="rec" aria-pressed="false">Duyệt, mục chưa chọn thì theo khuyến nghị</button><button data-a="more" aria-pressed="false">Cần thêm một vòng</button>'
    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(spec["title"])}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;700&family=Cal+Sans&display=swap">
<style>{TCSS}{PAGE_CSS}{sc.get("proposal_css", "")}{spec.get("css", "")}</style></head><body>
<div class="band">{MARK}<div><h1>{E(spec["title"])}</h1><p>{spec["subtitle"]}</p></div></div>
<div class="wrap rv"><div class="othernav">{nav}</div><p class="lead">{spec["lead"]}</p><div class="kpis">{kp}</div>
<div class="sticky"><span class="small"><b><span id="cnt">0</span>/{len(spec["items"])}</b> mục đã chọn</span><div class="pbar"><i id="pfill"></i></div><a class="small" href="#fin-h">Xuống phần chốt</a></div>
{screens}{secs}<h2>Các mục cần chọn</h2><p class="small">Mỗi mục có bản đang dùng, Untitled và Astryx để so, phần xem thử dựng bằng biến thật. Bấm lại để bỏ chọn; ghi chú và lựa chọn lưu trên trang, mở máy khác vẫn còn. Chưa có token nào bị sửa.</p>{items}
<h2 id="fin-h">Chốt {E(spec["short"])}</h2><div class="fin" id="fin" data-id="_final"><p style="margin-top:0">{fin}</p><div class="opts">{fopts}<span class="saved" data-saved></span></div><textarea placeholder="Ghi chú chung"></textarea></div></div>
<script id="data" type="application/json">{blob}</script><script>{PAGE_JS}{spec.get("js", "")}</script></body></html>"""
