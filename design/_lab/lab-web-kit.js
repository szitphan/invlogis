/* UI Lab web kit — icon, dữ liệu mẫu, khung trang (A/B/C). Dùng chung cho lab-web*.html. CHƯA phải design system. */
/* ===================== Icon (nét kiểu Lucide) ===================== */
const P={
 search:'<circle cx="11" cy="11" r="7.5"/><path d="m20.5 20.5-4.2-4.2"/>',
 bell:'<path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"/>',
 plus:'<path d="M5 12h14M12 5v14"/>',minus:'<path d="M5 12h14"/>',
 down:'<path d="m6 9 6 6 6-6"/>',right:'<path d="m9 18 6-6-6-6"/>',left:'<path d="m15 18-6-6 6-6"/>',up:'<path d="m18 15-6-6-6 6"/>',
 dash:'<rect x="3" y="3" width="7" height="9" rx="1.5"/><rect x="14" y="3" width="7" height="5" rx="1.5"/><rect x="14" y="12" width="7" height="9" rx="1.5"/><rect x="3" y="16" width="7" height="5" rx="1.5"/>',
 inbox:'<path d="M22 12h-6l-2 3h-4l-2-3H2"/><path d="M5.45 5.11 2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11z"/>',
 board:'<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M8 7v7M12 7v4M16 7v9"/>',
 truck:'<path d="M14 18V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v11a1 1 0 0 0 1 1h2"/><path d="M15 18H9"/><path d="M19 18h2a1 1 0 0 0 1-1v-3.65a1 1 0 0 0-.22-.62l-3.48-4.35A1 1 0 0 0 17.52 8H14"/><circle cx="17" cy="18" r="2"/><circle cx="7" cy="18" r="2"/>',
 file:'<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M16 13H8M16 17H8M10 9H8"/>',
 brief:'<rect width="20" height="14" x="2" y="6" rx="2"/><path d="M16 20V4a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>',
 clock:'<circle cx="12" cy="12" r="9.5"/><path d="M12 7v5l3 2"/>',
 alert:'<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4M12 17h.01"/>',
 train:'<rect width="16" height="16" x="4" y="3" rx="2"/><path d="M4 11h16M12 3v8M8 19l-2 3M18 22l-2-3M8 15h.01M16 15h.01"/>',
 users:'<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>',
 user:'<circle cx="12" cy="8" r="4"/><path d="M4 21v-1a6 6 0 0 1 6-6h4a6 6 0 0 1 6 6v1"/>',
 cal:'<rect width="18" height="18" x="3" y="4" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
 chart:'<path d="M3 3v18h18"/><path d="M18 17V9M13 17V5M8 17v-3"/>',
 sliders:'<path d="M4 21v-7M4 10V3M12 21v-9M12 8V3M20 21v-5M20 12V3M1 14h6M9 8h6M17 16h6"/>',
 filter:'<path d="M3 5h18M6 12h12M10 19h4"/>',
 more:'<circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/><circle cx="5" cy="12" r="1"/>',
 vmore:'<circle cx="12" cy="12" r="1"/><circle cx="12" cy="5" r="1"/><circle cx="12" cy="19" r="1"/>',
 pin:'<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
 cam:'<path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3l-2.5-3z"/><circle cx="12" cy="13" r="3"/>',
 temp:'<path d="M14 4v10.54a4 4 0 1 1-4 0V4a2 2 0 0 1 4 0Z"/>',
 wallet:'<path d="M19 7V4a1 1 0 0 0-1-1H5a2 2 0 0 0 0 4h15a1 1 0 0 1 1 1v4h-3a2 2 0 0 0 0 4h3a1 1 0 0 0 1-1v-2a1 1 0 0 0-1-1"/><path d="M3 5v14a2 2 0 0 0 2 2h15a1 1 0 0 0 1-1v-4"/>',
 hist:'<path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5M12 7v5l4 2"/>',
 check:'<path d="M20 6 9 17l-5-5"/>',x:'<path d="M18 6 6 18M6 6l12 12"/>',
 eye:'<path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z"/><circle cx="12" cy="12" r="3"/>',
 eyeoff:'<path d="M9.88 9.88a3 3 0 1 0 4.24 4.24M10.73 5.08A10.43 10.43 0 0 1 12 5c7 0 10 7 10 7a13.16 13.16 0 0 1-1.67 2.68M6.61 6.61A13.53 13.53 0 0 0 2 12s3 7 10 7a9.74 9.74 0 0 0 5.39-1.61M2 2l20 20"/>',
 grip:'<circle cx="9" cy="6" r=".8"/><circle cx="15" cy="6" r=".8"/><circle cx="9" cy="12" r=".8"/><circle cx="15" cy="12" r=".8"/><circle cx="9" cy="18" r=".8"/><circle cx="15" cy="18" r=".8"/>',
 list:'<path d="M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01"/>',
 export:'<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M17 8l-5-5-5 5M12 3v12"/>',
 phone:'<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.79 19.79 0 0 1 2.12 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>',
 pkg:'<path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><path d="M3.27 6.96 12 12.01l8.73-5.05M12 22.08V12"/>',
 route:'<circle cx="6" cy="19" r="3"/><path d="M9 19h8.5a3.5 3.5 0 0 0 0-7h-11a3.5 3.5 0 0 1 0-7H15"/><circle cx="18" cy="5" r="3"/>',
 panel:'<rect width="18" height="18" x="3" y="3" rx="2"/><path d="M9 3v18"/>',
 spark:'<path d="M12 3l1.9 5.8L20 10.7l-5.8 1.9L12 18.5l-1.9-5.9L4 10.7l6.1-1.9z"/>',
 arrowur:'<path d="M7 17 17 7M8 7h9v9"/>',arrowr:'<path d="M5 12h14M13 6l6 6-6 6"/>',
 msg:'<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
 home:'<path d="M3 10.5 12 3l9 7.5V20a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>',
 ware:'<path d="M22 8.35V20a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V8.35A2 2 0 0 1 3.26 6.5l8-3.2a2 2 0 0 1 1.48 0l8 3.2A2 2 0 0 1 22 8.35Z"/><path d="M6 18h12M6 14h12"/>',
 upload:'<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M17 8l-5-5-5 5M12 3v12"/>',
 sort:'<path d="m3 16 4 4 4-4M7 20V4M21 8l-4-4-4 4M17 4v16"/>',
 refresh:'<path d="M3 12a9 9 0 0 1 15.5-6.2L21 8M21 3v5h-5M21 12a9 9 0 0 1-15.5 6.2L3 16M3 21v-5h5"/>',
};
const I=(n,c="")=>`<svg class="ic ${c}" viewBox="0 0 24 24" aria-hidden="true">${P[n]||""}</svg>`;

/* ===================== Dữ liệu mẫu (theo wireframe dispatch-board-flow) ===================== */
const ST={lap:"Đã lập",giao:"Đã giao lái xe",nhan:"Lái xe đã nhận",chay:"Đang thực hiện",chot:"Lái xe đã chốt",duyet:"Đã duyệt",huy:"Huỷ"};
/* Chip trạng thái kiểu mobile lab (chốt 12/10): pill, nền nhạt + icon + chữ, không chấm. Chỉ ở chế độ Theo DS. */
P.nav='<path d="m3 11 19-9-9 19-2-8-8-2z"/>';P.pen='<path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"/>';P.ccheck='<path d="M18 6 7 17l-5-5"/><path d="m22 10-7.5 7.5L13 16"/>';P.xc='<circle cx="12" cy="12" r="9"/><path d="m15 9-6 6M9 9l6 6"/>';
const STI={lap:["idle","pen"],giao:["blue","truck"],nhan:["accept","check"],chay:["doing","nav"],chot:["wait","clock"],duyet:["done","ccheck"],huy:["bad","xc"]};
const st=(k,t)=>document.body.classList.contains("ds")&&STI[k]?`<span class="stp ${STI[k][0]}">${I(STI[k][1],"s")}${t||ST[k]}</span>`:`<span class="st c-${k}">${t||ST[k]}</span>`;
const ORD=[
 {id:"LVT-0459",s:"lap",car:"15C-333.44",drv:"",from:"Kho CFS Đình Vũ",to:"Kho An Phát",type:"CFS nhập",job:"JB-0131-00",time:"—",flag:["red","Lái xe từ chối"]},
 {id:"LVT-0461",s:"lap",car:"15C-999.00",drv:"Hoà Đặng",av:"a3",from:"Kho CFS Đình Vũ",to:"Kho An Phát",type:"CFS nhập",job:"JB-0133-00",time:"14:00"},
 {id:"LVT-0458",s:"giao",car:"15C-111.22",drv:"Sơn Phạm",av:"a2",from:"Cảng Tân Vũ",to:"Kho Minh An",type:"FCL nhập",job:"JB-0123-01",time:"13:00"},
 {id:"LVT-0454",s:"giao",car:"15C-616.07",drv:"Khánh Lý",av:"a4",from:"KCN Tràng Duệ",to:"Cảng Đình Vũ",type:"FCL xuất",job:"JB-0121-00",time:"15:30"},
 {id:"LVT-0453",s:"nhan",car:"15C-888.21",drv:"Hùng Vũ",av:"a5",from:"Cảng Nam Đình Vũ",to:"KCN VSIP",type:"FCL xuất",job:"JB-0119-02",time:"14:30"},
 {id:"LVT-0456",s:"chay",car:"15C-456.78",drv:"Tú Lê",av:"a1",from:"TCS Nội Bài",to:"Kho Hải Long",type:"Air nhập",job:"JB-0124-00",time:"11:30"},
 {id:"LVT-0452",s:"chay",car:"29C-123.45",drv:"Quân Ngô",av:"a2",from:"Vựa Đồng Tháp",to:"Tân Thanh",type:"CBT",job:"JB-0118-00",time:"10:45",flag:["amb","Trễ 25 phút"]},
 {id:"LVT-0451",s:"chay",car:"15C-404.33",drv:"Phúc Đỗ",av:"a3",from:"TCS Nội Bài",to:"Kho Hải Long",type:"Air nhập",job:"JB-0117-00",time:"12:15"},
 {id:"LVT-0450",s:"chot",car:"15C-202.19",drv:"Minh Trần",av:"a4",from:"Kho Hải Long",to:"Cảng Lạch Huyện",type:"FCL xuất",job:"JB-0115-01",time:"09:40"},
 {id:"LVT-0447",s:"duyet",car:"15C-515.60",drv:"Đức Phan",av:"a5",from:"ICD Hải Dương",to:"Kho An Phát",type:"Hàng lạnh",job:"JB-0112-00",time:"08:20"},
 {id:"LVT-0448",s:"duyet",car:"15C-777.12",drv:"Long Bùi",av:"a1",from:"Cảng Tân Vũ",to:"KCN Đình Vũ",type:"FCL nhập",job:"JB-0113-00",time:"08:50"},
 {id:"LVT-0449",s:"huy",car:"15C-310.08",drv:"—",from:"Kho Minh An",to:"Cảng Tân Vũ",type:"FCL xuất",job:"JB-0114-00",time:"—"},
];
const ini=n=>n&&n!=="—"?n.split(" ").map(w=>w[0]).slice(-2).join(""):"—";
const drv=o=>o.drv&&o.drv!=="—"?`<span class="row" style="gap:7px"><span class="av ${o.av||""}">${ini(o.drv)}</span>${o.drv}</span>`:`<span class="faint">Chưa có lái xe</span>`;
const flag=o=>o.flag?`<span class="flag ${o.flag[0]}">${o.flag[1]}</span>`:"";

/* ===================== Khung trang ===================== */
let SHELL="A";
const NAV=[["dash","Tổng quan","db"],["inbox","Việc của tôi","",4],["board","Theo dõi xếp xe","board"],["file","Lệnh vận tải","list"],["brief","JobID",""],["alert","Cảnh báo hạn","",2],["train","Kế hoạch tàu hoả",""]];
function navItems(active){
  return NAV.map(([ic,t,k,b])=>`<div class="nv ${k&&k===active?"on":""}">${I(ic)}<span>${t}</span>${b?`<span class="bd">${b}</span>`:""}</div>`).join("")+
   `<div class="ngrp">Đội xe</div><div class="nv">${I("truck")}<span>Xe</span><span class="bd g">18</span></div><div class="nv">${I("users")}<span>Lái xe</span></div><div class="nv">${I("cal")}<span>Phân công trực</span></div>
    <div class="ngrp">Báo cáo</div><div class="nv">${I("chart")}<span>Hiệu suất xe</span></div>`;
}
const WS=`<div class="wsb"><div class="lg">D</div><div class="grow"><div class="t1">Delta Logistics</div><div class="t2">Điều phối vận tải</div></div>${I("down","s faint")}</div>`;
function shell(active,crumb,body){
  if(SHELL==="E"||SHELL==="Ec"){const col=SHELL==="Ec";
    const it=(ic,t,on,bd)=>`<div class="e-it ${on?"on":""}" title="${t}">${I(ic)}${col?"":`<span>${t}</span>`}${bd?`<span class="e-bd">${bd}</span>`:""}</div>`;
    const grp=t=>col?`<div class="e-sep"></div>`:`<div class="e-grp">${t}</div>`;
    return `<div class="app shD shE ${col?"col":""}"><div class="side">
      <div class="e-top"><div class="lg">D</div>${col?"":`<div class="grow"><div class="t1">Delta</div><div class="t2">Điều phối vận tải</div></div><span class="btn icon sm ghost">${I("panel","s")}</span>`}</div>
      ${it("dash","Bảng tổng",active==="db")}${it("inbox","Việc của tôi",0,4)}
      ${grp("Điều phối")}${it("board","Theo dõi xếp xe",active==="board")}${it("file","Lệnh vận tải",active==="list")}${it("brief","JobID")}${it("alert","Cảnh báo hạn",0,2)}${it("train","Kế hoạch tàu hoả")}
      ${grp("Đội xe")}${it("truck","Xe")}${it("users","Lái xe")}${it("cal","Phân công trực")}
      ${grp("Báo cáo")}${it("chart","Hiệu suất xe")}
      <div class="sfootD">${col?`<div class="tile">${I("truck","s")}</div>`:`<div class="mod"><span class="tile">${I("truck","s")}</span>ĐIỀU PHỐI</div><div class="fac">${I("pin","s")}<span class="grow">Cơ sở Hải Phòng</span>${I("down","s")}</div>`}</div></div>
      <div class="mainwrap"><div class="hdrE">${col?`<span class="btn icon sm ghost">${I("panel","s")}</span>`:""}<span class="faint">Điều phối</span>${I("right","s faint")}<span style="color:var(--ink);font-weight:500">${crumb}</span>
        <span style="margin-left:auto" class="btn icon sm ghost">${I("search","s")}</span>${document.body.classList.contains("ds")?`<span class="btn sm" title="Đổi chi nhánh" style="gap:6px;margin:0 4px">${I("pin","s")}Chi nhánh Hải Phòng${I("down","s faint")}</span>`:""}<span style="position:relative" class="btn icon sm ghost">${I("bell","s")}<span style="position:absolute;top:3px;right:4px;width:8px;height:8px;border-radius:50%;background:#ef4444;box-shadow:0 0 0 2px #fff"></span></span><span class="av a1" style="width:28px;height:28px;margin-left:4px">TN</span></div>
      <div class="main">${body}</div></div></div>`;}
  if(SHELL==="D"||SHELL==="Dc"){const col=SHELL==="Dc";
    const m1=(ic,t,open,chev)=>`<div class="m1 ${open?"open":""}" title="${t}">${I(ic)}${col?"":`<span>${t}</span>${chev?`<span class="chev">${I(open?"up":"down","s")}</span>`:""}`}</div>`;
    const sub=[["Theo dõi xếp xe","board"],["Lệnh vận tải","list"],["JobID",""],["Cảnh báo hạn","",2]];
    return `<div class="app shD ${col?"col":""}"><div class="side">
      <div class="logo"><div class="lg">D</div>${col?"":`<span class="h" style="font-weight:700;font-size:15px">Delta</span><span class="btn icon sm ghost" style="margin-left:auto">${I("panel","s")}</span>`}</div>
      ${m1("dash","Bảng tổng",active==="db")}${m1("truck","Điều phối",true,1)}${col?"":`<div class="m2wrap">${sub.map(s=>`<div class="m2 ${s[1]&&s[1]===active?"on":""}">${s[0]}${s[2]?`<span class="bd">${s[2]}</span>`:""}</div>`).join("")}</div>`}
      ${m1("users","Đội xe",false,1)}${m1("train","Kế hoạch tàu hoả",false,1)}${m1("chart","Báo cáo",false)}
      <div class="sfootD">${col?`<div class="tile">${I("truck","s")}</div>`:`<div class="mod"><span class="tile">${I("truck","s")}</span>ĐIỀU PHỐI</div><div class="fac">${I("pin","s")}<span class="grow">Cơ sở Hải Phòng</span>${I("down","s")}</div>`}</div></div>
      <div class="mainwrap"><div class="hdr">${col?`<span class="btn icon sm ghost">${I("panel","s")}</span>`:""}<span class="faint">Điều phối</span>${I("right","s faint")}<span style="color:var(--ink);font-weight:500">${crumb}</span>
        <span style="margin-left:auto;position:relative" class="btn icon ghost">${I("bell")}<span style="position:absolute;top:4px;right:5px;min-width:16px;height:16px;border-radius:999px;background:#ef4444;color:#fff;font-size:10px;font-weight:700;display:flex;align-items:center;justify-content:center;padding:0 4px">3</span></span>
        <span class="row" style="gap:8px"><span class="av l a1">TN</span><span style="line-height:1.2"><span style="display:block;color:var(--ink);font-weight:600">Thảo Nguyễn</span><span class="faint" style="font-size:11.5px">Điều vận</span></span>${I("down","s faint")}</span></div>
      <div class="main">${body}</div></div></div>`;}
  if(SHELL==="A")return `<div class="app shA">
    <div class="tb"><div class="ws">${WS}</div><div class="srch"><div>${I("search","s")}Tìm Lệnh, JobID, biển số, lái xe<span style="margin-left:auto;font-size:11.5px">Ctrl K</span></div></div>
      <div class="row" style="gap:6px"><span class="btn icon ghost">${I("bell")}</span><span class="av l a1">TN</span></div></div>
    <div class="side">${navItems(active)}<div class="sfoot"><div class="facility">${I("ware","s faint")}<span class="grow">Cơ sở Hải Phòng</span>${I("down","s faint")}</div></div></div>
    <div class="main">${body}</div></div>`;
  if(SHELL==="B")return `<div class="app shB">
    <div class="rail"><div class="wsb" style="padding:0;margin-bottom:8px"><div class="lg">D</div></div>
      <div class="ri on">${I("truck")}</div><div class="ri">${I("ware")}</div><div class="ri">${I("wallet")}</div><div class="ri">${I("users")}</div>
      <div style="margin-top:auto" class="ri">${I("sliders")}</div><span class="av a1">TN</span></div>
    <div class="side"><div style="padding:4px 8px 10px"><div class="h" style="font-weight:700;font-size:15px">Điều phối</div><div class="faint" style="font-size:12px">Cơ sở Hải Phòng</div></div>${navItems(active)}</div>
    <div class="mainwrap"><div class="crumb">${I("panel","faint")}<span class="faint">Điều phối</span>${I("right","s faint")}<span style="color:var(--ink);font-weight:500">${crumb}</span>
      <span style="margin-left:auto" class="pill">${I("search","s")}Tìm nhanh<span class="faint" style="margin-left:18px">Ctrl K</span></span><span class="btn icon sm ghost">${I("bell")}</span></div>
      <div class="main">${body}</div></div></div>`;
  return `<div class="app shC">
    <div class="side">${WS}<div class="pill" style="height:34px;border-radius:10px;margin-bottom:8px">${I("search","s")}Tìm nhanh<span class="faint" style="margin-left:auto">Ctrl K</span></div>${navItems(active)}
      <div class="sfoot"><div class="facility">${I("ware","s faint")}<span class="grow">Cơ sở Hải Phòng</span>${I("down","s faint")}</div><div class="row" style="padding:4px 6px"><span class="av l a1">TN</span><div class="grow"><div style="font-weight:600;font-size:13px">Thảo Nguyễn</div><div class="faint" style="font-size:11.5px">Điều vận</div></div>${I("bell","faint")}</div></div></div>
    <div class="main">${body}</div></div>`;
}


/* ---------- Brand theo khách (chốt 12/10 vòng 3) ----------
   Hiện tại brand CHỈ thay logo (ô chữ cái / ảnh logo + tên app). Bộ màu và component khác chưa liên quan:
   menu đang chọn, tab, link, nút chính… giữ trung tính. Khách khai 1 màu (P-mau-thuong-hieu); chữ trên ô logo
   tự chọn trắng hoặc #171717 theo tương phản. */
const BRAND={neutral:"#262626",innvie:"#0036B5",delta:"#2E7449"};
const hex2rgb=h=>{h=h.replace("#","");return [0,2,4].map(i=>parseInt(h.substr(i,2),16)/255)};
const lum=c=>{const l=c.map(v=>v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4));return .2126*l[0]+.7152*l[1]+.0722*l[2]};
const contrast=(a,b)=>{const x=lum(a),y=lum(b);return (Math.max(x,y)+.05)/(Math.min(x,y)+.05)};
function applyBrand(hex){
  const st=document.body.style,K=["--p","--on-p","--ps","--pt"];
  if(!hex){K.forEach(k=>st.removeProperty(k));return null}
  const c=hex2rgb(hex),onBrand=contrast([1,1,1],c)>=contrast(hex2rgb("#171717"),c)?"#ffffff":"#171717";
  st.setProperty("--p",hex);st.setProperty("--on-p",onBrand);          // chỉ logo dùng --p/--on-p
  st.setProperty("--ps","#f1f1f1");st.setProperty("--pt","#262626");    // menu đang chọn, link… trung tính
  return {brand:hex,onBrand};
}
