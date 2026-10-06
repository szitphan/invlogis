/* Form sự cố v2 — dán HELPER (đầu file) rồi phần chạy cuối file. */
await figma.setCurrentPage("5218:51306");
const P={wrench:"M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z",truck:"M3 6h11v10H3zM14 9h4l3 3v4h-7M7.5 19a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3zM17.5 19a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3z",alert:"M12 9v4M12 17h.01M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z",pin:"M12 21s7-6.1 7-12a7 7 0 1 0-14 0c0 5.9 7 12 7 12zM12 11a2 2 0 1 0 0-4 2 2 0 0 0 0 4z",chev:"M9 6l6 6-6 6",clock:"M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18zM12 7v5l3 2",check:"M5 12l5 5L20 7",x:"M18 6 6 18M6 6l12 12",fuel:"M3 22V5a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v17M3 22h12M3 10h12M15 13h2a2 2 0 0 1 2 2v3a1.5 1.5 0 0 0 3 0V9l-3-3",back:"M19 12H5M12 19l-7-7 7-7",scan:"M4 8V6a2 2 0 0 1 2-2h2M16 4h2a2 2 0 0 1 2 2v2M20 16v2a2 2 0 0 1-2 2h-2M8 20H6a2 2 0 0 1-2-2v-2M7 12h10",box:"M21 8 12 3 3 8v8l9 5 9-5zM3 8l9 5 9-5M12 13v8",camera:"M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3zM12 17a4 4 0 1 0 0-8 4 4 0 0 0 0 8z",image:"M3 5h18v14H3zM3 16l5-5 4 4 3-3 6 6M15 9h.01",plus:"M12 5v14M5 12h14",file:"M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8zM14 3v5h5M9 13h6M9 17h6",bell:"M6 8a6 6 0 1 1 12 0c0 7 3 9 3 9H3s3-2 3-9M10.3 21a1.94 1.94 0 0 0 3.4 0",search:"M11 19a8 8 0 1 0 0-16 8 8 0 0 0 0 16zM21 21l-4.3-4.3"};
const K={ink:"#121214",ink2:"#5c5c66",ink3:"#93939d",w:"#ffffff"};
const ic=(n,s=20,c=K.ink,w=1.8)=>({type:"ICON",name:"icon/"+n,svg:`<svg width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="${w}" stroke-linecap="round" stroke-linejoin="round"><path d="${P[n]}"/></svg>`});
const T=(c,st,fill="$lab/ink",x={})=>({type:"TEXT",name:x.name||c.slice(0,30),characters:c,textStyle:st,fill,...x});
const TW=(c,st,fill="$lab/ink",x={})=>T(c,st,fill,{layoutAlign:"STRETCH",textAutoResize:"HEIGHT",...x});
const TG=(c,st,fill="$lab/ink",x={})=>T(c,st,fill,{layoutGrow:1,textAutoResize:"HEIGHT",...x});
const H=(name,p,ch=[])=>({type:"FRAME",name,layoutMode:"HORIZONTAL",counterAxisAlignItems:"CENTER",primaryAxisSizingMode:(p.layoutAlign==="STRETCH"||p.layoutGrow)?"FIXED":"AUTO",counterAxisSizingMode:"AUTO",itemSpacing:0,...p,children:ch});
const V=(name,p,ch=[])=>({type:"FRAME",name,layoutMode:"VERTICAL",primaryAxisSizingMode:"AUTO",counterAxisSizingMode:(p.layoutAlign==="STRETCH"||p.layoutGrow)?"FIXED":"AUTO",itemSpacing:0,...p,children:ch});
const sp=()=>({type:"FRAME",name:"đẩy",layoutGrow:1,height:1});
const gap=(h)=>({type:"FRAME",name:"cách",width:1,height:h});
const kẻ=()=>({type:"FRAME",name:"Kẻ",layoutAlign:"STRETCH",height:1,fill:"$lab/rule"});
const S={layoutAlign:"STRETCH"},G={layoutGrow:1};
const R=(t)=>({tokens:{cornerRadius:t}});
const BD={stroke:"$lab/rule",strokeWeight:1,strokeAlign:"INSIDE"};
const circ=(name,size,fill,child,x={})=>H(name,{width:size,height:size,primaryAxisSizingMode:"FIXED",counterAxisSizingMode:"FIXED",primaryAxisAlignItems:"CENTER",...(fill?{fill}:{}),...R("lab/r/pill"),...x},child?[child]:[]);
const icc=(n,o={})=>circ("Icon tròn · "+n,o.size||36,o.fill||"$lab/well",ic(n,o.is||17,o.c||K.ink));
const ib=(n,label,o={})=>circ("Nút "+label,o.size||42,o.fill===undefined?"$lab/card":o.fill,ic(n,o.is||20,o.c||K.ink),o.x||{});
const btn=(label,kind,o={})=>H("Nút "+label,{height:o.h||52,counterAxisSizingMode:"FIXED",primaryAxisAlignItems:"CENTER",paddingLeft:20,paddingRight:20,itemSpacing:8,fill:kind==="pri"?"$lab/primary":"$lab/well",...R("lab/r/pill"),...(o.p||{})},[T(label,"Lab/Button",kind==="pri"?"$lab/on-primary":"$lab/ink")]);
const stepper=(n,times)=>{const L=["Báo sự cố","Báo giá","Sửa chữa","Nghiệm thu"];
 const ln=(on,vis)=>({type:"FRAME",name:"Nối",layoutGrow:1,height:2,cornerRadius:1,...(vis?{fill:on?"$lab/ink":"$lab/dash"}:{})});
 return H("Thanh tiến trình",{...S,counterAxisAlignItems:"MIN"},L.map((l,i)=>V("Bước · "+l,{...G,counterAxisAlignItems:"CENTER",itemSpacing:2},[
  H("Chấm + nối",{...S,itemSpacing:6},[ln(i<=n,i>0),i<n?circ("Chấm · xong",24,"$lab/ink",ic("check",13,K.w,3)):i===n?circ("Chấm · đang",24,"$lab/card",circ("lõi",8,"$lab/ink"),{stroke:"$lab/ink",strokeWeight:2,strokeAlign:"INSIDE"}):circ("Chấm · chưa",24,"$lab/card",null,{stroke:"$lab/dash",strokeWeight:2,strokeAlign:"INSIDE"}),ln(i<n,i<3)]),
  V("cách",{height:4,primaryAxisSizingMode:"FIXED"}),T(l,"Lab/Step"),T(times[i]||" ","Lab/Step time","$lab/ink-3")])));};
const statusBar=()=>({type:"FRAME",name:"Status bar",width:393,height:54,children:[T("9:41","Lab/Status bar","$lab/ink",{x:46,y:18}),{type:"FRAME",name:"Dynamic Island",x:133.5,y:11,width:126,height:37,fill:"#000000",cornerRadius:18.5},
 {type:"ICON",name:"icon/he-thong",x:300,y:21,svg:`<svg width="70" height="12" viewBox="0 0 70 12"><rect x="0" y="7" width="3" height="4" rx="1" fill="#121214"/><rect x="4.5" y="5" width="3" height="6" rx="1" fill="#121214"/><rect x="9" y="2.5" width="3" height="8.5" rx="1" fill="#121214"/><rect x="13.5" y="0" width="3" height="11" rx="1" fill="#121214"/><path transform="translate(22 0)" d="M8 10.5 10.3 8a3.3 3.3 0 0 0-4.6 0zM3.6 5.8a6.3 6.3 0 0 1 8.8 0l1.4-1.4a8.3 8.3 0 0 0-11.6 0zM.8 3a10.3 10.3 0 0 1 14.4 0l1.4-1.4A12.3 12.3 0 0 0-.6 1.6z" fill="#121214"/><rect x="43.5" y=".5" width="22" height="11" rx="3.5" fill="none" stroke="#121214" stroke-opacity=".4"/><rect x="45" y="2" width="17" height="8" rx="2" fill="#121214"/><rect x="66.5" y="4" width="1.5" height="4" rx=".75" fill="#121214" fill-opacity=".4"/></svg>`}]});
const homeInd=()=>({type:"FRAME",name:"Home indicator",layoutPositioning:"ABSOLUTE",x:129.5,y:839,width:134,height:5,fill:"$lab/ink",...R("lab/r/pill")});
const screen=(name,body,overlays,x,y)=>V(name,{x,y,width:393,height:852,primaryAxisSizingMode:"FIXED",counterAxisSizingMode:"FIXED",fill:"$lab/page-c",clipsContent:true,cornerRadius:0},[statusBar(),V("Nội dung",{...S,...G,primaryAxisSizingMode:"FIXED",paddingLeft:16,paddingRight:16,paddingTop:4,paddingBottom:120,itemSpacing:0,clipsContent:true},body),...overlays,homeInd()]);
/* ---- phần tử form ---- */
const tag=(t)=>H("Nhãn · "+t,{paddingLeft:8,paddingRight:8,paddingTop:2,paddingBottom:2,fill:"$lab/rule",...R("lab/r/pill")},[T(t,"Lab/Pill")]);
const hdr=(n,left)=>V("Đầu form",{...S,itemSpacing:14,paddingTop:6,paddingBottom:18},[H("Thanh đầu",{...S,itemSpacing:8},[ib(left,left==="x"?"Đóng":"Quay lại",{x:BD}),TG("Báo cáo sự cố","Lab/H3","$lab/ink",{textAlignHorizontal:"CENTER"}),H("Bước "+n+"/3",{paddingLeft:12,paddingRight:12,paddingTop:6,paddingBottom:6,fill:"$lab/card",...BD,...R("lab/r/pill")},[T(n+"/3","Lab/Small medium","$lab/ink-2")])]),
 H("Thanh tiến độ",{...S,itemSpacing:6},[1,2,3].map(i=>({type:"FRAME",name:"Đoạn "+i,layoutGrow:1,height:4,cornerRadius:2,fill:i<=n?"$lab/ink":"$lab/well"})))]);
const title=(t,s)=>V("Tiêu đề",{...S,itemSpacing:4,paddingBottom:18},[TW(t,"Lab/H2"),TW(s,"Lab/Small","$lab/ink-2")]);
const fl=(t)=>V("Nhãn trường · "+t,{...S,paddingBottom:7},[T(t,"Lab/Small medium","$lab/ink-2")]);
const ffl=()=>V("Trường phương tiện",{...S,paddingBottom:18},[H("Ô chọn xe",{...S,itemSpacing:12,paddingLeft:14,paddingRight:14,paddingTop:10,paddingBottom:10,fill:"$lab/well",cornerRadius:18},[icc("truck",{fill:"$lab/card",is:18}),V("Giá trị",{...G,itemSpacing:1},[T("Phương tiện","Lab/Cap","$lab/ink-3"),H("Biển số",{itemSpacing:6},[T("30E-789.01","Lab/Body strong"),tag("Xe đang nhận")]),T("Hyundai HD320 · Km 182.430","Lab/Sub","$lab/ink-2")]),ic("chev",18)])]);
const types=[["alert","Phanh","rít, rung, yếu"],["truck","Lốp","thủng, mòn, nổ"],["wrench","Động cơ","đèn báo, hụt ga"],["fuel","Nhiên liệu","rò, hao bất thường"],["scan","Điện","ắc quy, đèn"],["box","Khác","thân vỏ, điều hoà…"]];
const opt=([i,l,s],on)=>V("Lựa chọn · "+l+(on?" · đang chọn":""),{...G,padding:14,itemSpacing:10,cornerRadius:18,fill:on?"$lab/card":"$lab/well",...(on?{stroke:"$lab/primary",strokeWeight:2,strokeAlign:"INSIDE"}:{})},[H("Đầu",{...S},[circ("Icon",38,on?"$lab/primary":"$lab/card",ic(i,19,on?K.w:K.ink)),sp(),...(on?[circ("Dấu chọn",20,"$lab/primary",ic("check",12,K.w,3.2))]:[])]),V("Chữ",{...S,itemSpacing:2},[T(l,"Lab/Row"),T(s,"Lab/Cap","$lab/ink-3")])]);
const sc2=()=>V("Lưới loại sự cố",{...S,itemSpacing:10,paddingBottom:18},[0,2,4].map(k=>H("Hàng",{...S,itemSpacing:10},[opt(types[k],k===0),opt(types[k+1],false)])));
const segc=(on)=>H("Chọn mức độ",{...S,padding:4,fill:"$lab/well",...R("lab/r/pill")},["Nhẹ","Trung bình","Nghiêm trọng"].map((t,i)=>H("Mức · "+t,{...G,height:38,counterAxisSizingMode:"FIXED",primaryAxisAlignItems:"CENTER",...R("lab/r/pill"),...(i===on?{fill:"$lab/card",effects:[{type:"DROP_SHADOW",color:"#00000014",offset:{x:0,y:1},radius:2,spread:0}]}:{})},[T(t,i===on?"Lab/Small medium":"Lab/Small",i===on?"$lab/ink":"$lab/ink-2")])));
const help=(t)=>V("Giải thích",{...S,paddingTop:6,paddingBottom:18,paddingLeft:2},[TW(t,"Lab/Cap","$lab/ink-3")]);
const yn=(on)=>H("Còn chạy được",{...S,itemSpacing:10},["Còn chạy","Phải dừng xe"].map((t,i)=>H("Đáp án · "+t,{...G,height:52,counterAxisSizingMode:"FIXED",primaryAxisAlignItems:"CENTER",itemSpacing:8,fill:i===on?"$lab/ink":"$lab/well",...R("lab/r/pill")},[...(i===on?[ic("check",17,K.w,2.4)]:[]),T(t,"Lab/Row",i===on?"$lab/on-primary":"$lab/ink")])));
const hint=(n,t)=>H("Gợi ý",{...S,itemSpacing:10,counterAxisAlignItems:"MIN",paddingLeft:14,paddingRight:14,paddingTop:12,paddingBottom:12,fill:"$lab/well",cornerRadius:18},[circ("Icon",24,"$lab/card",ic(n,14)),TG(t,"Lab/Small","$lab/ink-2")]);
const img=(name,big)=>H(name,{layoutGrow:1,layoutAlign:"STRETCH",primaryAxisAlignItems:"CENTER",fill:big?"#b4b7bf":"$lab/well",cornerRadius:18},[ic(big===2?"plus":"image",20,big?K.w:K.ink3),...(big===1?[circ("Nút xoá ảnh",22,"#00000073",ic("x",12,K.w,2.4),{layoutPositioning:"ABSOLUTE",x:78,y:6})]:[])]);
const shots=()=>H("Ảnh",{...S,height:190,counterAxisSizingMode:"FIXED",itemSpacing:8,counterAxisAlignItems:"MIN"},[V("Chụp ảnh",{width:133,layoutAlign:"STRETCH",counterAxisSizingMode:"FIXED",primaryAxisSizingMode:"FIXED",primaryAxisAlignItems:"CENTER",counterAxisAlignItems:"CENTER",itemSpacing:6,fill:"$lab/ink",cornerRadius:18},[ic("camera",26,K.w),T("Chụp ảnh","Lab/Small medium","$lab/on-primary")]),
 V("Cột 2",{width:106,layoutAlign:"STRETCH",counterAxisSizingMode:"FIXED",primaryAxisSizingMode:"FIXED",itemSpacing:8},[img("Ảnh 1",1),{...img("Ô trống"),fill:"$lab/well"}]),V("Cột 3",{width:106,layoutAlign:"STRETCH",counterAxisSizingMode:"FIXED",primaryAxisSizingMode:"FIXED",itemSpacing:8},[img("Ảnh 2",1),{...img("Thêm ảnh"),children:[ic("plus",20,K.ink3)]}])]);
const qchip=(t)=>H("Gợi ý nhanh · "+t,{height:32,counterAxisSizingMode:"FIXED",paddingLeft:12,paddingRight:12,itemSpacing:4,...BD,...R("lab/r/pill")},[ic("plus",13,K.ink2,2.2),T(t,"Lab/Small","$lab/ink-2")]);
const arow=(n,b,s)=>H("Hàng · "+b,{...S,itemSpacing:12,paddingTop:10,paddingBottom:10},[icc(n,{size:44,is:19}),V("Chữ",{...G,itemSpacing:1},[TW(b,"Lab/Body strong"),T(s,"Lab/Sub","$lab/ink-3")]),T("Đổi","Lab/Small medium")]);
const kvr=(l,v)=>H("Cặp · "+l,{...S,paddingTop:8,paddingBottom:8},[T(l,"Lab/Meta","$lab/ink-2"),sp(),T(v,"Lab/Body strong")]);
const kvs=(rows)=>V("Cặp nhãn – giá trị",{...S},rows.flatMap((r,i)=>[...(i?[kẻ()]:[]),kvr(...r)]));
const rv=(t,edit,ch)=>V("Khối xem lại · "+t,{...S,itemSpacing:6,paddingLeft:16,paddingRight:16,paddingTop:14,paddingBottom:14,fill:"$lab/well",...R("lab/r/card")},[H("Đầu",{...S},[T(t,"Lab/Title"),sp(),...(edit?[H("Nút Sửa · "+t,{height:30,counterAxisSizingMode:"FIXED",paddingLeft:12,paddingRight:12,itemSpacing:4,fill:"$lab/card",...R("lab/r/pill")},[ic("file",13),T("Sửa","Lab/Small medium")])]:[])]),...ch]);
const foot=(btns)=>H("Chân màn",{layoutPositioning:"ABSOLUTE",x:0,y:752,width:393,primaryAxisSizingMode:"FIXED",paddingLeft:16,paddingRight:16,paddingTop:14,paddingBottom:34,itemSpacing:10,fill:"$lab/page-c"},btns);
const sheetWrap=(ch)=>[{type:"FRAME",name:"Nền mờ",layoutPositioning:"ABSOLUTE",x:0,y:0,width:393,height:852,fill:"#0a0a0e6b"},
 V("Sheet",{layoutPositioning:"ABSOLUTE",x:8,y:400,width:377,counterAxisSizingMode:"FIXED",paddingLeft:18,paddingRight:18,paddingTop:8,paddingBottom:20,fill:"$lab/card",cornerRadius:36,effects:[{type:"DROP_SHADOW",color:"#0000002e",offset:{x:0,y:-10},radius:40,spread:0}]},[H("Tay nắm",{...S,primaryAxisAlignItems:"CENTER",paddingBottom:10},[{type:"FRAME",name:"Thanh nắm",width:40,height:5,cornerRadius:3,fill:"$lab/dash"}]),...ch])];
const shHead=(t)=>H("Đầu sheet",{...S,paddingBottom:12},[T(t,"Lab/H3"),sp(),ib("x","Đóng",{size:38,fill:"$lab/well",is:18})]);

const done=()=>[gap(70),H("Dấu xong",{...S,primaryAxisAlignItems:"CENTER",paddingBottom:30},[circ("Đã gửi",96,"$lab/ink",ic("check",44,K.w,2.6),{stroke:"$lab/well",strokeWeight:12,strokeAlign:"OUTSIDE"})]),
 V("Chữ xong",{...S,counterAxisAlignItems:"CENTER",itemSpacing:4,paddingBottom:24},[T("Đã gửi báo cáo","Lab/H2"),T("Mã BCSC-0413 · 06/10/2026 07:18","Lab/Small","$lab/ink-2")]),
 V("Tiến trình",{...S,itemSpacing:8,padding:16,fill:"$lab/well",...R("lab/r/card")},[T("Tiến trình","Lab/Cap","$lab/ink-3"),stepper(1,["07:18"])]),gap(18),hint("bell","Bạn sẽ nhận thông báo khi có báo giá và khi xe được xếp lịch sửa.")];
/* ===== v2 (07/10) theo góp ý form ===== */
P.user="M20 21a8 8 0 0 0-16 0M12 13a5 5 0 1 0 0-10 5 5 0 0 0 0 10z";
const SEC={x0:80,y:2180}; /* toạ độ tương đối trong Section 5446:15413 */
const types2=[["alert","Phanh","Kêu rít, rung vô lăng, phanh yếu hoặc bị lệch khi phanh"],["truck","Lốp","Thủng, non hơi, mòn bất thường hoặc nổ lốp"],["wrench","Động cơ","Đèn báo lỗi, hụt ga, nóng máy hoặc khói bất thường"],["fuel","Nhiên liệu","Rò rỉ, có mùi nhiên liệu hoặc hao bất thường"],["scan","Điện","Ắc quy yếu, đèn hỏng hoặc không đề được máy"],["box","Khác","Thân vỏ, điều hoà, cửa, gương và bộ phận khác"]];
const radio=(on)=>circ(on?"Chọn · đang chọn":"Chọn",22,null,null,on?{stroke:"$lab/primary",strokeWeight:7,strokeAlign:"INSIDE"}:{stroke:"#c8c8d0",strokeWeight:2,strokeAlign:"INSIDE"});
const optRow=([i,l,s],on)=>H("Lựa chọn · "+l+(on?" · đang chọn":""),{...S,itemSpacing:12,paddingLeft:14,paddingRight:14,paddingTop:12,paddingBottom:12,cornerRadius:18,fill:on?"$lab/card":"$lab/well",...(on?{stroke:"$lab/primary",strokeWeight:2,strokeAlign:"INSIDE"}:{})},[circ("Icon",38,on?"$lab/primary":"$lab/card",ic(i,19,on?K.w:K.ink)),V("Chữ",{...G,itemSpacing:2},[T(l,"Lab/Row"),TW(s,"Lab/Sub","$lab/ink-3")]),radio(on)]);
const typeList=()=>V("Danh sách loại sự cố",{...S,itemSpacing:8,paddingBottom:18},types2.map((t,k)=>optRow(t,k===0)));
const step1v2=()=>[hdr(1,"x"),title("Xe gặp vấn đề gì?","Chọn nhanh, mô tả chi tiết ở bước sau."),ffl(),fl("Loại sự cố"),typeList(),fl("Mức độ"),segc(1),help("Trung bình: xe vẫn chạy được nhưng cần kiểm tra sớm."),fl("Xe còn chạy được không?"),yn(0)];
const vehCard=([p,m,on,t])=>H("Thẻ xe · "+p+(on?" · đang chọn":""),{...S,itemSpacing:12,paddingLeft:14,paddingRight:14,paddingTop:12,paddingBottom:12,cornerRadius:18,fill:"$lab/card",...(on?{stroke:"$lab/primary",strokeWeight:2,strokeAlign:"INSIDE"}:BD)},[icc("truck",{is:17}),V("Chữ",{...G,itemSpacing:1},[H("Biển số",{itemSpacing:6},[T(p,"Lab/Body strong"),...(t?[tag(t)]:[])]),T(m,"Lab/Sub","$lab/ink-3")]),radio(on)]);
const vehicles2=[["30E-789.01","Hyundai HD320 · Km 182.430",1,"Xe đang nhận"],["29H-123.45","Hino FG 15T · Km 96.210",0],["29C-456.78","Isuzu QKR · Km 141.880",0],["30F-222.90","Hyundai HD210 · Km 210.050",0]];
const sheetVeh2=()=>sheetWrap([shHead("Chọn phương tiện"),H("Ô tìm",{...S,height:48,counterAxisSizingMode:"FIXED",paddingLeft:16,paddingRight:6,itemSpacing:8,fill:"$lab/well",...R("lab/r/pill")},[ic("search",18,K.ink3),T("Tìm biển số","Lab/Body","$lab/ink-3")]),gap(12),
 V("Danh sách xe",{...S,itemSpacing:8},vehicles2.map(vehCard)),
 H("Không thấy xe",{...S,primaryAxisAlignItems:"CENTER",itemSpacing:6,paddingTop:14,paddingBottom:14},[ic("alert",15,K.ink2),T("Không thấy xe của bạn?","Lab/Small medium","$lab/ink-2")]),btn("Chọn xe này","pri",{p:S})]);
const rvW=(t,edit,ch)=>({...rv(t,edit,ch),fill:"$lab/card",...BD});
const step3v2=()=>[hdr(3,"back"),title("Kiểm tra trước khi gửi","Chạm \"Sửa\" để chỉnh từng phần."),
 rvW("Xe và sự cố",1,[kvs([["Phương tiện","30E-789.01"],["Loại sự cố","Phanh"],["Mức độ","Trung bình"],["Xe còn chạy","Có"]])]),gap(12),
 rvW("Ảnh và mô tả",1,[TW("Phanh kêu rít và rung vô lăng khi phanh gấp. Từ sáng nay.","Lab/Meta","$lab/ink-2"),H("Ảnh nhỏ",{itemSpacing:6,paddingTop:2},[1,2].map(i=>({type:"FRAME",name:"Ảnh nhỏ "+i,width:52,height:52,cornerRadius:12,fill:"#b4b7bf"}))),kvs([["Vị trí","QL1A, Thường Tín"],["Phát hiện","Hôm nay, 07:05"]])]),gap(12),
 rvW("Người báo",0,[kvs([["Họ tên","Phạm Văn Hùng"],["Số điện thoại","0912 345 678"]])])];
/* sheet sửa = đúng nội dung bước 1, cao gần hết màn */
const sheetEditFull=()=>[{type:"FRAME",name:"Nền mờ",layoutPositioning:"ABSOLUTE",x:0,y:0,width:393,height:852,fill:"#0a0a0e6b"},
 V("Sheet",{layoutPositioning:"ABSOLUTE",x:0,y:56,width:393,height:830,primaryAxisSizingMode:"FIXED",counterAxisSizingMode:"FIXED",paddingLeft:16,paddingRight:16,paddingTop:8,fill:"$lab/card",cornerRadius:28,clipsContent:true},[
  H("Tay nắm",{...S,primaryAxisAlignItems:"CENTER",paddingBottom:10},[{type:"FRAME",name:"Thanh nắm",width:40,height:5,cornerRadius:3,fill:"$lab/dash"}]),
  shHead("Sửa xe và sự cố"),ffl(),fl("Loại sự cố"),typeList(),fl("Mức độ"),segc(1),
  H("Chân sheet",{layoutPositioning:"ABSOLUTE",x:0,y:696,width:393,primaryAxisSizingMode:"FIXED",paddingLeft:16,paddingRight:16,paddingTop:14,paddingBottom:34,itemSpacing:10,fill:"$lab/card",stroke:"$lab/rule",strokeWeight:1,strokeAlign:"INSIDE"},[btn("Huỷ","sec",{p:G}),btn("Lưu thay đổi","pri",{p:G})])])];
const footV=(btns)=>V("Chân màn",{layoutPositioning:"ABSOLUTE",x:0,y:690,width:393,counterAxisSizingMode:"FIXED",paddingLeft:16,paddingRight:16,paddingTop:14,paddingBottom:34,itemSpacing:10,fill:"$lab/page-c"},btns);
const fix=async(id,extra={})=>{const find=async(q)=>((await figma.searchNodes({query:q,nodeId:id,limit:30})).nodes||[]).filter(x=>x.name===q);
 const want={"Chân màn":null,"Home indicator":{x:129.5,y:839},"Nền mờ":{x:0,y:0},"Chân sheet":{x:0,y:696},...extra};
 for(const [nm,pos] of Object.entries(want))for(const x of await find(nm))await figma.modify(x.id,{layoutPositioning:"ABSOLUTE",...(pos==="bottom8"?{x:8,y:852-8-x.h}:pos||{x:0,y:852-x.h})});};
const mk=async(i,name,body,ov,extra)=>{const s=await figma.create({...screen(name,body,ov,SEC.x0+i*473,SEC.y),parentId:"5446:15413"});await fix(s.id,extra);return s.id;};

/* ===== CHẠY ===== */
for(const id of ["5446:14688","5446:14818","5446:15112","5446:15211","5446:15341"]){try{await figma.delete(id);}catch(e){}}
const out={};
out.b1=await mk(0,"4.1-mob · bao-su-co · b1-xe-va-su-co",step1v2(),[foot([btn("Tiếp tục","pri",{p:G})])]);
out.sheetXe=await mk(1,"4.1-mob · bao-su-co · sheet-chon-xe",step1v2(),sheetVeh2(),{"Sheet":"bottom8"});
out.b3=await mk(3,"4.1-mob · bao-su-co · b3-xem-lai",step3v2(),[foot([btn("Gửi báo cáo","pri",{p:G})])]);
out.sheetSua=await mk(4,"4.1-mob · bao-su-co · sheet-sua-xe-va-su-co",step3v2(),sheetEditFull(),{"Sheet":{x:0,y:56}});
out.done=await mk(5,"4.1-mob · bao-su-co · da-gui",done(),[footV([btn("Xem báo cáo","pri",{p:S}),btn("Về trang chủ","sec",{p:S})])]);
state.form2=out;return out;
