/* Họ thẻ v2 — sửa bảng 5446:13957 theo góp ý 06/10. 2 lượt figma_write:
   PHẦN A (component Hàng danh sách + icon component) · PHẦN B (thay thẻ 1/2/3/6/8, xoá KPI).
   Mỗi lượt dán HELPER + phần tương ứng. */

/* ===== HELPER ===== */
await figma.setCurrentPage("5218:51306");
const P={wrench:"M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z",truck:"M3 6h11v10H3zM14 9h4l3 3v4h-7M7.5 19a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3zM17.5 19a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3z",alert:"M12 9v4M12 17h.01M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z",pin:"M12 21s7-6.1 7-12a7 7 0 1 0-14 0c0 5.9 7 12 7 12zM12 11a2 2 0 1 0 0-4 2 2 0 0 0 0 4z",user:"M20 21a8 8 0 0 0-16 0M12 13a5 5 0 1 0 0-10 5 5 0 0 0 0 10z",chev:"M9 6l6 6-6 6",cal:"M8 2v4M16 2v4M3 9h18M5 4h14a2 2 0 0 1 2 2v13a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z",receipt:"M5 3h14v18l-3-2-2 2-2-2-2 2-2-2-3 2zM9 8h6M9 12h6",clock:"M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18zM12 7v5l3 2",check:"M5 12l5 5L20 7",gauge:"M12 14l4-4M3.3 19a10 10 0 1 1 17.4 0",fuel:"M3 22V5a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v17M3 22h12M3 10h12M15 13h2a2 2 0 0 1 2 2v3a1.5 1.5 0 0 0 3 0V9l-3-3",edit:"M12 20h9M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z",truck2:"M3 6h11v10H3z"};
const K={ink:"#121214",ink2:"#5c5c66",w:"#ffffff"};
const ST={wait:["wait","Chờ sửa","clock"],quote:["wait","Đang báo giá","receipt"],fix:["doing","Đang sửa","wrench"],ok:["done","Đã duyệt","check"]};
const STC={wait:"#8a5300",doing:"#5536c4",done:"#1b7542",bad:"#b42318"};
const ic=(n,s=20,c=K.ink,w=1.8)=>({type:"ICON",name:"icon/"+n,svg:`<svg width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="${w}" stroke-linecap="round" stroke-linejoin="round"><path d="${P[n]}"/></svg>`});
const T=(c,st,fill="$lab/ink",x={})=>({type:"TEXT",name:x.name||c.slice(0,30),characters:c,textStyle:st,fill,...x});
const TW=(c,st,fill="$lab/ink",x={})=>T(c,st,fill,{layoutAlign:"STRETCH",textAutoResize:"HEIGHT",...x});
const TG=(c,st,fill="$lab/ink",x={})=>T(c,st,fill,{layoutGrow:1,textAutoResize:"HEIGHT",...x});
const H=(name,p,ch=[])=>({type:"FRAME",name,layoutMode:"HORIZONTAL",counterAxisAlignItems:"CENTER",primaryAxisSizingMode:(p.layoutAlign==="STRETCH"||p.layoutGrow)?"FIXED":"AUTO",counterAxisSizingMode:"AUTO",itemSpacing:0,...p,children:ch});
const V=(name,p,ch=[])=>({type:"FRAME",name,layoutMode:"VERTICAL",primaryAxisSizingMode:"AUTO",counterAxisSizingMode:(p.layoutAlign==="STRETCH"||p.layoutGrow)?"FIXED":"AUTO",itemSpacing:0,...p,children:ch});
const sp=()=>({type:"FRAME",name:"đẩy",layoutGrow:1,height:1});
const kẻ=(name="Kẻ")=>({type:"FRAME",name,layoutAlign:"STRETCH",height:1,fill:"$lab/rule"});
const S={layoutAlign:"STRETCH"},G={layoutGrow:1};
const R=(t)=>({tokens:{cornerRadius:t}});
const BD={stroke:"$lab/rule",strokeWeight:1,strokeAlign:"INSIDE"};
const circ=(name,size,fill,child,x={})=>H(name,{width:size,height:size,primaryAxisSizingMode:"FIXED",counterAxisSizingMode:"FIXED",primaryAxisAlignItems:"CENTER",...(fill?{fill}:{}),...R("lab/r/pill"),...x},child?[child]:[]);
const icc=(n,o={})=>circ("Icon tròn · "+n,o.size||36,o.fill||"$lab/well",ic(n,o.is||17,o.c||K.ink));
const ib=(n,label,o={})=>circ("Nút "+label,o.size||42,o.fill===undefined?"$lab/card":o.fill,ic(n,o.is||20,o.c||K.ink),o.x||{});
const pill=k=>{const[t,l,i]=ST[k];return H("Trạng thái · "+l,{height:26,counterAxisSizingMode:"FIXED",paddingLeft:8,paddingRight:10,itemSpacing:4,fill:`$lab/st/${t}-bg`,...R("lab/r/pill")},[ic(i,14,STC[t],2),T(l,"Lab/Pill",`$lab/st/${t}`,{name:"Nhãn trạng thái"})])};
const card=(name,ch,o={})=>V(name,{...S,fill:"$lab/card",itemSpacing:o.gap??12,tokens:{cornerRadius:"lab/r/card",padding:"lab/sp/16"},...BD},ch);
const recH=(icon,code,k)=>H("Đầu thẻ",{...S,itemSpacing:10},[icc(icon),TG(code,"Lab/Body strong","$lab/ink",{textAutoResize:"WIDTH_AND_HEIGHT"}),pill(k)]);
const metaRow=(n,t)=>H("Dòng · "+t,{itemSpacing:8},[ic(n,16,K.ink2),T(t,"Lab/Meta","$lab/ink-2")]);
const meta=(rows)=>V("Thông tin",{...S,itemSpacing:8},rows.map(r=>metaRow(...r)));
const veh=(plate,model)=>H("Thẻ con · xe",{...S,itemSpacing:10,paddingLeft:12,paddingRight:12,paddingTop:10,paddingBottom:10,fill:"$lab/well",...R("lab/r/inner")},[icc("truck",{fill:"$lab/card",is:18}),V("Xe",{...G,itemSpacing:2},[T(plate,"Lab/Body strong"),T(model,"Lab/Sub","$lab/ink-3")])]);
const strip=(txt)=>H("Dải cảnh báo",{...S,itemSpacing:8,paddingLeft:12,paddingRight:12,paddingTop:9,paddingBottom:9,fill:"$lab/st/wait-bg",cornerRadius:14},[ic("alert",16,STC.wait),TG(txt,"Lab/Small medium","$lab/st/wait")]);
const chip=(n,t)=>H("Chip · "+t,{height:36,counterAxisSizingMode:"FIXED",paddingLeft:12,paddingRight:12,itemSpacing:6,fill:"$lab/well",...R("lab/r/pill")},[ic(n,15),T(t,"Lab/Small medium")]);
const col=async(prefix)=>((await figma.searchNodes({query:"Cột · "+prefix,nodeId:"5446:13957",limit:5})).nodes||[]).find(n=>n.name.startsWith("Cột · "+prefix));
/* thay thẻ (con thứ 2 trở đi) của 1 cột bằng spec mới */
const replaceCard=async(prefix,specs)=>{const c=await col(prefix);const ch=await figma.getChildren(c.id);for(const x of ch.slice(1))await figma.delete(x.id);
 const ids=[];for(const s of specs)ids.push((await figma.create({...s,parentId:c.id})).id);return ids;};

/* ===== PHẦN A — component ===== */
const X0=13000,Y0=-1400;
const icons={};
for(const [i,n] of ["wrench","receipt","alert","cal","truck","fuel"].entries()){
 const c=await figma.create({type:"COMPONENT",name:"Lab/Icon/"+n,x:X0+i*40,y:Y0,width:17,height:17,children:[{...ic(n,17),x:0,y:0}]});icons[n]=c.id;}
const row=await figma.create({type:"COMPONENT",name:"Lab/Hàng danh sách",x:X0,y:Y0+60,width:329,layoutMode:"VERTICAL",primaryAxisSizingMode:"AUTO",counterAxisSizingMode:"FIXED",fill:"$lab/card",children:[
 kẻ("Kẻ trên"),
 H("Hàng",{...S,itemSpacing:12,paddingTop:12,paddingBottom:12},[circ("Icon tròn",36,"$lab/well",null),
  V("Chữ",{...G,itemSpacing:2},[TW("Tiêu đề hàng","Lab/Row","$lab/ink",{name:"Tiêu đề"}),TW("Dòng phụ","Lab/Sub","$lab/ink-3",{name:"Phụ"})]),
  pill("wait"),
  V("Giá trị",{counterAxisAlignItems:"MAX"},[T("3.200.000","Lab/Body strong","$lab/ink",{name:"Số"}),T("chờ duyệt","Lab/Cap","$lab/ink-3",{name:"Ghi chú số"})]),
  {...ic("chev",18),name:"Mũi tên"}])]});
const find=async(q)=>((await figma.searchNodes({query:q,nodeId:row.id,limit:10})).nodes||[]).find(n=>n.name===q);
const holder=await find("Icon tròn");
const inst=await figma.instantiate(icons.wrench,{parentId:holder.id});
const L={kẻ:await find("Kẻ trên"),pill:await find("Trạng thái · Chờ sửa"),val:await find("Giá trị"),chev:await find("Mũi tên"),t:await find("Tiêu đề"),s:await find("Phụ"),pt:await find("Nhãn trạng thái"),n:await find("Số"),nn:await find("Ghi chú số")};
const props=[["Kẻ trên","BOOLEAN",true,L.kẻ],["Trạng thái","BOOLEAN",false,L.pill],["Giá trị","BOOLEAN",false,L.val],["Mũi tên","BOOLEAN",true,L.chev],
 ["Tiêu đề","TEXT","Tiêu đề hàng",L.t],["Phụ","TEXT","Dòng phụ",L.s],["Nhãn trạng thái","TEXT","Chờ sửa",L.pt],["Số","TEXT","3.200.000",L.n],["Ghi chú số","TEXT","chờ duyệt",L.nn],["Icon","INSTANCE_SWAP",icons.wrench,{id:inst.id}]];
const res=[];for(const [name,type,defaultValue,layer] of props)res.push(await figma.addComponentProperty(row.id,{name,type,defaultValue,layerId:layer.id}));
await figma.setComponentDescription(row.id,"Hàng trong thẻ danh sách (họ thẻ #2). Đường kẻ nằm TRONG hàng: tắt `Kẻ trên` ở hàng đầu. Bên phải: bật 1 trong Trạng thái / Giá trị / Mũi tên. Màu nhãn trạng thái cố định Chờ sửa — đổi màu bằng override.");
state.cmp={row:row.id,icons};return {row:row.id,icons,res};

/* ===== PHẦN B — thay thẻ trên bảng ===== */
// 1. Thẻ bản ghi: bỏ cảnh báo, xe xuống cuối + biến thể có số lượng/tiền
await replaceCard("1.",[
 card("Thẻ bản ghi · lệnh sửa chữa",[recH("wrench","LSC-0918","wait"),meta([["pin","Xưởng nhà · Hà Đông"],["user","Trần Minh Đức"],["clock","Hạn 05/10"]]),veh("29C-456.78","Isuzu QKR")]),
 T("Biến thể có số lượng / tiền","Lab/Small medium","$lab/ink-2"),
 card("Thẻ bản ghi · có số lượng",[recH("fuel","PCD-0312","ok"),
  H("Số liệu",{...S,counterAxisAlignItems:"MAX"},[V("Số lượng",{itemSpacing:0},[T("Số lượng","Lab/Cap","$lab/ink-3"),T("120 lít","Lab/Stat")]),sp(),V("Thành tiền",{itemSpacing:0,counterAxisAlignItems:"MAX"},[T("Thành tiền","Lab/Cap","$lab/ink-3"),T("2.640.000 ₫","Lab/Body strong")])]),
  kẻ(),meta([["pin","Petrolimex Thường Tín"],["user","Phạm Văn Hùng"],["clock","06/10 06:40"]]),veh("30E-789.01","Hyundai HD320")])]);
// 2. Hàng danh sách: thẻ ráp từ instance component
{const c=await col("2.");const ch=await figma.getChildren(c.id);for(const x of ch.slice(1))await figma.delete(x.id);
 const box=await figma.create({...V("Hàng danh sách",{...S,fill:"$lab/card",paddingLeft:16,paddingRight:16,paddingTop:4,paddingBottom:4,...R("lab/r/card"),...BD}),parentId:c.id});
 const rows=[{"Kẻ trên":false,"Tiêu đề":"Thay 2 lốp sau","Phụ":"LSC-0918 · 29C-456.78","Trạng thái":true,"Mũi tên":false},
  {"Tiêu đề":"Bảo dưỡng 40.000 km","Phụ":"LSC-0924 · 29H-881.20","Trạng thái":true,"Mũi tên":false},
  {"Tiêu đề":"Báo giá BG-0391","Phụ":"Gara Minh Phát","Giá trị":true,"Mũi tên":false,"Số":"3.200.000","Ghi chú số":"chờ duyệt","Icon":state.cmp.icons.receipt}];
 for(const p of rows){const i=await figma.instantiate(state.cmp.row,{parentId:box.id});await figma.modify(i.id,{layoutAlign:"STRETCH"});await figma.setInstanceProperties(i.id,p);}}
// 3. Thẻ theo dõi tiến trình: thanh 4 đoạn thay stepper
const seg=(n)=>V("Tiến trình",{...S,itemSpacing:8},[H("Nhãn bước",{...S},[T("Bước "+(n+1)+"/4 · Báo giá","Lab/Small medium"),sp(),T("Gửi 06/10 07:12","Lab/Cap","$lab/ink-3")]),
 H("Thanh 4 đoạn",{...S,itemSpacing:4},[0,1,2,3].map(i=>({type:"FRAME",name:"Đoạn "+(i+1)+(i<n?" · xong":i===n?" · đang":" · chưa"),layoutGrow:1,height:6,cornerRadius:3,fill:i<n?"$lab/ink":i===n?"$lab/ink-3":"$lab/well"}))),
 T("Tiếp theo: Sửa chữa","Lab/Cap","$lab/ink-3")]);
await replaceCard("3.",[card("Thẻ theo dõi tiến trình",[recH("alert","BCSC-0412","quote"),TW("Phanh kêu, rung khi phanh gấp","Lab/Title"),seg(1)])]);
// 4. KPI: xoá cả cột
{const c=await col("4.");await figma.delete(c.id);}
// 6. Thẻ phương tiện: thêm lái xe, km xuống chip, bỏ chip đăng kiểm
await replaceCard("6.",[card("Thẻ phương tiện",[H("Đầu thẻ",{...S,itemSpacing:10},[icc("truck",{size:44,is:20}),V("Xe",{...G,itemSpacing:0},[T("29C-456.78","Lab/Body strong"),T("Isuzu QKR","Lab/Cap","$lab/ink-3")]),pill("fix")]),
 meta([["pin","Xưởng nhà · Hà Đông"],["user","Lái xe: Trần Văn Nam"]]),strip("Đăng kiểm hết hạn trong 5 ngày"),
 H("Chỉ số",{...S,itemSpacing:6},[chip("fuel","62%"),chip("gauge","182.430 km"),sp(),ib("chev","Chi tiết xe",{size:36,fill:"$lab/well",is:18})])])]);
// 8. Tóm tắt tiền: nút chữ Sửa → nút icon bút
{const c=await col("8.");const old=((await figma.searchNodes({query:"Nút Sửa",nodeId:c.id,limit:5})).nodes||[]).find(n=>n.name==="Nút Sửa");
 const head=((await figma.searchNodes({query:"Đầu",nodeId:c.id,limit:10})).nodes||[]).find(n=>n.name==="Đầu");
 await figma.delete(old.id);await figma.create({...ib("edit","Sửa hạng mục",{size:36,fill:"$lab/well",is:17}),parentId:head.id});}
// tiêu đề bảng
{const t=((await figma.searchNodes({query:"Họ thẻ dùng chung",nodeId:"5446:13957",limit:3})).nodes||[])[0];await figma.setText(t.id,"Họ thẻ dùng chung · 9 loại (v2)");}
return "ok";
