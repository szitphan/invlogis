/* UI Lab — đổi font tiêu đề trên màn thật (chốt Manrope 09/10/2026; Geist/Cal Sans giữ để đối chiếu).
   Nút nổi góc dưới trái. Lựa chọn lưu chung mọi trang lab; ?hf=geist|manrope|cal&hn=on|off&hw=page|600|700 để mở thẳng.
   Không đụng .k-phone nên #check không bị ảnh hưởng. Chưa phải quyết định design system. */
(function(){
  const F={geist:["Geist","-0.02em"],manrope:["Manrope","-0.02em"],cal:["Cal Sans","0"]};
  const HEAD=".k-h1,.k-h2,.k-sec h3,.k-chdr .ct,.d-sh-t,.k-rec-t,.k-event .t,.k-who .t1,.big-t,.sec h3,.chdr .ct,.ttl,.cf-t,.d-ctitle,.rv-h,.ac .big,.ac .huge,.ac-h .t";
  const NUM=".k-hero .n,.k-kpi .n,.k-stat .n,.h-num,.kpi .n,.k-kv .tot,.items .tot,.d-foot .tot b";
  let S={hf:"manrope",hn:"on",hw:"page"};
  try{Object.assign(S,JSON.parse(localStorage.getItem("uilab-hf")||"{}"))}catch(e){}
  const q=new URLSearchParams(location.search);["hf","hn","hw"].forEach(k=>{if(q.has(k))S[k]=q.get(k)});
  if(!F[S.hf])S.hf="manrope";

  const lk=document.createElement("link");lk.rel="stylesheet";
  lk.href="https://fonts.googleapis.com/css2?family=Cal+Sans&family=Geist:wght@500;600;700;800&family=Manrope:wght@500;600;700;800&display=swap";
  document.head.appendChild(lk);
  const st=document.createElement("style");document.head.appendChild(st);

  function apply(){
    const [fam,ls]=F[S.hf],cal=S.hf==="cal";
    const w=cal?"font-weight:400!important;":S.hw==="page"?"":`font-weight:${S.hw}!important;`;
    const rule=`{font-family:"${fam}",Inter,sans-serif!important;${w}${cal?"letter-spacing:0!important;":`letter-spacing:${ls}!important;`}}`;
    st.textContent=`:is(${HEAD})${rule}`+(S.hn==="on"?`:is(${NUM})${rule}`:"")+`
#lab-hf{position:fixed;left:12px;bottom:12px;z-index:9999;display:flex;flex-wrap:wrap;gap:6px 10px;align-items:center;max-width:calc(100vw - 24px);
 padding:8px 10px;border-radius:16px;background:rgba(18,18,20,.92);color:#fff;font:12px/1.3 Inter,sans-serif;box-shadow:0 8px 24px rgba(0,0,0,.25)}
#lab-hf .g{display:flex;background:rgba(255,255,255,.12);border-radius:999px;padding:2px}
#lab-hf button{font:inherit;border:0;background:none;color:#fff;padding:4px 10px;border-radius:999px;cursor:pointer}
#lab-hf button.on{background:#fff;color:#121214}`;
    document.querySelectorAll("#lab-hf button").forEach(b=>b.classList.toggle("on",S[b.parentElement.dataset.k]===b.dataset.v));
  }
  function bar(){
    const d=document.createElement("div");d.id="lab-hf";
    d.innerHTML=`<span>Tiêu đề</span><div class="g" data-k="hf"><button data-v="geist">Geist</button><button data-v="manrope">Manrope</button><button data-v="cal">Cal Sans</button></div>
<span>Độ đậm</span><div class="g" data-k="hw"><button data-v="page">Theo màn</button><button data-v="600">600</button><button data-v="700">700</button></div>
<span>Số lớn</span><div class="g" data-k="hn"><button data-v="on">Font tiêu đề</button><button data-v="off">Inter</button></div>`;
    d.addEventListener("click",e=>{const b=e.target.closest("button");if(!b)return;S[b.parentElement.dataset.k]=b.dataset.v;
      try{localStorage.setItem("uilab-hf",JSON.stringify(S))}catch(x){}apply()});
    document.body.appendChild(d);apply();
  }
  apply();
  if(location.hash!=="#check")(document.body?bar():document.addEventListener("DOMContentLoaded",bar));
})();
