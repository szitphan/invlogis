/* UI Lab kit — icon, mảnh giao diện dùng chung, và chế độ tự kiểm (#check). */
const P={
home:"M3 10.5 12 3l9 7.5V20a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z",
cal:"M8 2v4M16 2v4M3 9h18M5 4h14a2 2 0 0 1 2 2v13a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z",
scan:"M4 8V6a2 2 0 0 1 2-2h2M16 4h2a2 2 0 0 1 2 2v2M20 16v2a2 2 0 0 1-2 2h-2M8 20H6a2 2 0 0 1-2-2v-2M7 12h10",
bell:"M6 8a6 6 0 1 1 12 0c0 7 3 9 3 9H3s3-2 3-9M10.3 21a1.94 1.94 0 0 0 3.4 0",
user:"M20 21a8 8 0 0 0-16 0M12 13a5 5 0 1 0 0-10 5 5 0 0 0 0 10z",
search:"M11 19a8 8 0 1 0 0-16 8 8 0 0 0 0 16zM21 21l-4.3-4.3",
filter:"M4 6h9M17 6h3M4 12h3M11 12h9M4 18h11M19 18h1M15 4v4M9 10v4M17 16v4",
plus:"M12 5v14M5 12h14",chev:"M9 6l6 6-6 6",down:"M6 9l6 6 6-6",back:"M19 12H5M12 19l-7-7 7-7",
more:"M6 12h.01M12 12h.01M18 12h.01",x:"M18 6 6 18M6 6l12 12",check:"M5 12l5 5L20 7",
wrench:"M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z",
truck:"M3 6h11v10H3zM14 9h4l3 3v4h-7M7.5 19a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3zM17.5 19a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3z",
alert:"M12 9v4M12 17h.01M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z",
camera:"M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3zM12 17a4 4 0 1 0 0-8 4 4 0 0 0 0 8z",
pin:"M12 21s7-6.1 7-12a7 7 0 1 0-14 0c0 5.9 7 12 7 12zM12 11a2 2 0 1 0 0-4 2 2 0 0 0 0 4z",
clock:"M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18zM12 7v5l3 2",
phone:"M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z",
msg:"M21 12a8 8 0 0 1-11.6 7.1L3 21l1.9-6.4A8 8 0 1 1 21 12z",
file:"M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8zM14 3v5h5M9 13h6M9 17h6",
fuel:"M3 22V5a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v17M3 22h12M3 10h12M15 13h2a2 2 0 0 1 2 2v3a1.5 1.5 0 0 0 3 0V9l-3-3",
clip:"M9 3h6v3H9zM15 4.5h2a2 2 0 0 1 2 2V19a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6.5a2 2 0 0 1 2-2h2M9 13l2 2 4-4",
receipt:"M5 3h14v18l-3-2-2 2-2-2-2 2-2-2-3 2zM9 8h6M9 12h6",chart:"M4 20V10M10 20V4M16 20v-7M22 20H2",
box:"M21 8 12 3 3 8v8l9 5 9-5zM3 8l9 5 9-5M12 13v8",up:"M7 17 17 7M8 7h9v9",
gauge:"M12 14l4-4M3.3 19a10 10 0 1 1 17.4 0",shield:"M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"};
const I=(n,s=20,w=1.8)=>`<svg class="k-ic" aria-hidden="true" focusable="false" width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="${w}" stroke-linecap="round" stroke-linejoin="round"><path d="${P[n]}"/></svg>`;
const SB=`<div class="k-sb"><span>9:41</span><span style="display:flex;align-items:center"><svg width="17" height="11" viewBox="0 0 17 11"><rect x="0" y="7" width="3" height="4" rx="1" fill="currentColor"/><rect x="4.5" y="5" width="3" height="6" rx="1" fill="currentColor"/><rect x="9" y="2.5" width="3" height="8.5" rx="1" fill="currentColor"/><rect x="13.5" y="0" width="3" height="11" rx="1" fill="currentColor"/></svg><svg width="16" height="11" viewBox="0 0 16 11"><path d="M8 10.5 10.3 8a3.3 3.3 0 0 0-4.6 0zM3.6 5.8a6.3 6.3 0 0 1 8.8 0l1.4-1.4a8.3 8.3 0 0 0-11.6 0zM.8 3a10.3 10.3 0 0 1 14.4 0l1.4-1.4A12.3 12.3 0 0 0-.6 1.6z" fill="currentColor"/></svg><svg width="26" height="12" viewBox="0 0 26 12"><rect x=".5" y=".5" width="22" height="11" rx="3.5" fill="none" stroke="currentColor" opacity=".4"/><rect x="2" y="2" width="17" height="8" rx="2" fill="currentColor"/><rect x="23.5" y="4" width="1.5" height="4" rx=".75" fill="currentColor" opacity=".4"/></svg></span></div>`;

const ST={wait:["wait","Chờ sửa","clock"],doing:["doing","Đang sửa","wrench"],accept:["accept","Chờ nghiệm thu","clip"],
  done:["done","Đã nghiệm thu","check"],bad:["bad","Từ chối nghiệm thu","x"],quote:["wait","Đang báo giá","receipt"],
  run:["done","Đang chạy","truck"],fix:["doing","Đang sửa","wrench"],ready:["idle","Sẵn sàng","check"]};
const pill=k=>`<span class="k-pill ${ST[k][0]}">${I(ST[k][2],14,2)}${ST[k][1]}</span>`;
const seg=n=>`<div class="k-seg">${[0,1,2,3].map(i=>`<i class="${i<n?"on":""}"></i>`).join("")}</div>`;
const stepper=(n,times=[])=>{const L=["Báo sự cố","Báo giá","Sửa chữa","Nghiệm thu"];
  return `<div class="k-stp">${L.map((l,i)=>`<div class="st ${i<n?"done":i===n?"cur":""}"><div class="dc">${i<n?I("check",13,3):""}</div><div class="nm">${l}</div><div class="tm">${times[i]||"&nbsp;"}</div></div>`).join("")}</div>`};
const phone=(surface,body,overlay="")=>`<div class="k k-phone s-${surface}"><div class="k-scr">${SB}${body}</div>${overlay}<div class="k-homebar"></div></div>`;
/* labels=true: tab có chữ dưới icon (luật nav-label-icon). Nút Quét giữa là hành động, không phải tab. */
const navBar=(labels=false)=>`<nav class="k-nav" aria-label="Điều hướng chính">${[["home","Trang chủ",1],["cal","Lịch"],null,["bell","Thông báo"],["user","Tôi"]].map(x=>x?`<a class="t ${x[2]?"on":""}" aria-label="${x[1]}"${x[2]?' aria-current="page"':""}>${I(x[0],labels?20:22)}${labels?`<span>${x[1]}</span>`:""}</a>`:`<button class="scan" aria-label="Quét mã" style="border:0">${I("scan",22)}</button>`).join("")}</nav>`;

/* Lưu trạng thái + nút chọn trên thanh lab */
function labStore(key,def){let S=Object.assign({},def);try{Object.assign(S,JSON.parse(localStorage.getItem(key)||"{}"))}catch(e){}
  const q=new URLSearchParams(location.search);Object.keys(def).forEach(k=>{if(q.has(k))S[k]=q.get(k)});
  S.save=()=>{try{const c=Object.assign({},S);delete c.save;localStorage.setItem(key,JSON.stringify(c))}catch(e){}};return S}
function labBindOpts(S,rerender){
  const sync=()=>document.querySelectorAll(".lab-opts[data-k]").forEach(o=>o.querySelectorAll("button").forEach(b=>b.classList.toggle("on",S[o.dataset.k]===b.dataset.v)));
  document.addEventListener("click",e=>{const b=e.target.closest(".lab-opts[data-k] button");if(!b)return;S[b.parentElement.dataset.k]=b.dataset.v;S.save();rerender();sync()});
  sync();
}
function labToast(m){const t=document.getElementById("lab-toast");if(!t)return;t.textContent=m;t.style.display="block";setTimeout(()=>t.style.display="none",1800)}
function labCopy(txt){(navigator.clipboard?navigator.clipboard.writeText(txt):Promise.reject()).then(()=>labToast("Đã copy — dán vào chat"),()=>prompt("Copy đoạn này:",txt))}

/* Chế độ tự kiểm: mở trang với #check → ghi kết quả vào <pre id="labcheck">.
   Bắt: (1) chữ đè chữ trong cùng 1 lớp, (2) phần tử tràn ra ngoài thẻ/khung máy,
   (3) chữ bị cắt "…" (chỉ báo, không phải lỗi). */
function labCheck(){
  const out={overlap:[],escape:[],ellipsis:[]};
  const txt=el=>(el.textContent||"").trim().replace(/\s+/g," ").slice(0,40);
  const layerOf=el=>el.closest(".k-foot,.k-nav,.k-sheet,[data-layer],.k-scr");
  document.querySelectorAll(".k-phone").forEach((ph,pi)=>{
    const tag=ph.closest("[data-check]")?.dataset.check||("phone "+pi);
    const leaves=[...ph.querySelectorAll("*")].filter(el=>{
      if(!el.childNodes.length)return false;
      const own=[...el.childNodes].some(n=>n.nodeType===3&&n.textContent.trim());
      const r=el.getBoundingClientRect();return own&&r.width>0&&r.height>0});
    for(let i=0;i<leaves.length;i++)for(let j=i+1;j<leaves.length;j++){
      const a=leaves[i],b=leaves[j];if(a.contains(b)||b.contains(a))continue;
      if(layerOf(a)!==layerOf(b))continue;
      const A=a.getBoundingClientRect(),B=b.getBoundingClientRect();
      const ox=Math.min(A.right,B.right)-Math.max(A.left,B.left),oy=Math.min(A.bottom,B.bottom)-Math.max(A.top,B.top);
      if(ox>2&&oy>2)out.overlap.push(`${tag}: "${txt(a)}" ⟷ "${txt(b)}"`);
    }
    const scr=ph.querySelector(".k-scr");const R=scr.getBoundingClientRect();
    ph.querySelectorAll(".k-scr *").forEach(el=>{
      const r=el.getBoundingClientRect();if(!r.width)return;
      if(el.closest(".k-tabs,.glow,.mp"))return; /* .mp = bản đồ, cắt mép là chủ ý */
      if(el.ownerSVGElement)return; /* hình bên trong <svg> luôn bị viewBox cắt */
      if(r.right>R.right+1||r.left<R.left-1)out.escape.push(`${tag}: <${el.className||el.tagName}> "${txt(el)}" lố ${Math.round(Math.max(r.right-R.right,R.left-r.left))}px`);
      const cs=getComputedStyle(el);
      if(cs.textOverflow==="ellipsis"&&el.scrollWidth>el.clientWidth+1)out.ellipsis.push(`${tag}: "${txt(el)}"`);
    });
    ph.querySelectorAll(".k-card,.k-kpi,.k-well,.k-tile").forEach(box=>{
      const B=box.getBoundingClientRect();
      box.querySelectorAll("*").forEach(el=>{const r=el.getBoundingClientRect();if(!r.width||el.closest(".k-tabs"))return;
        if(r.right>B.right+1||r.bottom>B.bottom+1)out.escape.push(`${tag}: "${txt(el)}" tràn khỏi <${box.className}>`)})});
  });
  const pre=document.createElement("pre");pre.id="labcheck";pre.textContent=JSON.stringify(out,null,1);document.body.appendChild(pre);
  return out;
}
if(location.hash==="#check")window.addEventListener("load",()=>setTimeout(labCheck,300));
