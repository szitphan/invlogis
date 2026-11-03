#!/usr/bin/env python3
"""Sinh function list Fleetio từ FR trong SRS + bảng ghi đè theo run-notes. Chạy từ gốc repo."""
import re,json,html,glob,pathlib,sys
D=pathlib.Path('docs/_research/fleetio')
fr={}
LV={'repair':7,'reminders-inspection':7,'parts-purchasing-fuel':7,'saas-platform':7,'location-dispatch':7,'vehicle':6,'tires':6} # cột Mức của từng SRS
for f in glob.glob(str(D/'srs/*-spec.md')):
    g=re.search(r'fleetio-(.*)-spec',f).group(1)
    for l in open(f):
        if l.startswith('| FR-fleetio'):
            c=[x.strip() for x in l.strip().strip('|').split('|')]
            n=c[0].rsplit('-',1)[1]; i=LV.get(g,6); fr[(g,n)]=dict(id=c[0],t=c[1],d=c[2],src=c[i].replace('`',''))
def lv(s):
    s=re.sub(r'\(bản trước[^)]*\)','',s)
    h=('Chạy' in s); o=('Docs' in s or 'Xem' in s or 'chưa' in s or 'một phần' in s or 'Một phần' in s)
    return 'part' if h and o else 'run' if h else 'view' if 'Xem' in s else 'docs'
R='repair';N='reminders-inspection';K='parts-purchasing-fuel';V='vehicle';S='saas-platform';L='location-dispatch';T='tires'
MOD=[('Dashboard, tổng quan',[(S,['008','015','016'])],'platform'),
('Vehicles · Danh sách, hồ sơ xe',[(V,['001','002','003','004','005','006','007','008']),(V,['020', '021', '022', '023', '024', '025', '026']),(S,['039'])],'platform'),
('Vehicles · Gán xe',[(V,['009','010','011','012']),(V,['027', '028', '029'])],'—'),
('Vehicles · Số đồng hồ',[(V,['013','014','015','016']),(V,['030', '031', '032', '044'])],'—'),
('Vehicles · Lốp',[(T,[f'{i:03}' for i in range(1,31)])],'tires'),
('Vehicles · Chi phí, thay xe',[(V,['018','019']),(V,['033', '034', '040'])],'—'),
('Fleet Map',[(L,['001','002','003','004','005','006','007','008','009','013']),(L,['023', '024', '029', '030', '031', '032'])],'location'),
('Places, Geofence',[(L,['010','011']),(L,['025', '026', '027', '028'])],'location'),
('Jobs',[(L,['012']),(L,['014', '015', '016', '017', '018', '019', '020', '021', '022'])],'location'),
('Inspections',[(N,[f'{i:03}' for i in range(13,23)]),(N,['032', '033', '034', '036', '038'])],'reminders'),
('Issues',[(R,['001','002','003','004','005','019','022']),(R,['026', '027', '028']),(S,['042', '053'])],'repair'),
('Faults',[(R,['023','024'])],'repair'),
('Service Reminders',[(N,[f'{i:03}' for i in range(1,11)]),(N,['023', '024', '025', '026', '027', '028', '039'])],'reminders'),
('Service Programs',[(N,['011']),(N,['029', '030'])],'reminders'),
('Renewals',[(N,['012']),(N,['031'])],'reminders'),
('Work Orders',[(R,['006','007','008','009','010','011','012','013','015','017','018','020','021']),(R,['029', '030', '031', '032', '033', '034', '036', '039', '040'])],'repair'),
('Service History',[(R,['014'])],'repair'),
('Service Tasks',[(R,['016']),(R,['041'])],'repair'),
('Warranties',[(R,['025']),(R,['038']),(V,['035', '036', '037', '039'])],'repair'),
('Parts & Inventory',[(K,['001','002','003','004','005','006','007','008','014']),(K,['025', '026', '027', '038'])],'parts'),
('Purchase Orders',[(K,['009','010','011','012','013']),(K,['028', '029', '030', '031', '032', '037'])],'parts'),
('Vendors',[(K,['015','016']),(K,['035'])],'parts'),
('Fuel',[(K,['017','018','019','020','021','022']),(K,['033', '034', '036'])],'parts'),
('Reports, hỏi dữ liệu',[(S,['019','020']),(S,['051', '052'])],'platform'),
('Automations',[(S,['012','013','014']),(S,['030', '031', '032', '033', '034', '035', '036', '037']),(V,['045'])],'platform'),
('Settings, quyền',[(S,['001','002','003','004','005','006','007','023']),(S,['044', '045', '046', '047', '048', '050']),(R,['035']),(V,['043', '046'])],'platform'),
('Tính năng chung',[(S,['009','010','011','017','018','021','022','024']),(S,['038', '043'])],'platform'),
('Tích hợp, API',[(S,['027','028','029']),(S,['049']),(L,['033'])],'platform'),
]
# Ghi đè: kết quả đã chạy thật, có trong run-notes
OVR={(V,'008'):('run','Linked Vehicles đầu kéo và mooc'),(V,'012'):('run','Thêm, trùng, sửa đè người'),(V,'013'):('run','Lệch ngày bị từ chối'),(V,'014'):('part','Exceeds Max chạy; Out of Sequence không tái hiện trên web'),(V,'015'):('run','Void, Unvoid, Conflict Source'),(V,'018'):('run','Một lần, định kỳ'),(V,'019'):('run','Máy tính tự nhập, chỉ đọc'),(R,'025'):('run','Tạo Warranty, Opportunity trên lệnh'),(L,'010'):('run','Vùng tròn, đa giác, sửa bán kính'),(L,'001'):('run','Vị trí giả lập: danh sách theo khoảng cách'),(L,'002'):('run','Vị trí giả lập: bật tắt lớp'),(L,'004'):('run','Phiếu kiểm web tạo vị trí; phiếu dầu, phiếu dịch vụ không có ô vị trí'),(L,'005'):('part','Lọc chạy một phần'),(L,'006'):('run','Vị trí giả lập: panel, Nearby, Quick Add'),(L,'007'):('run','Vị trí giả lập: đường nét đứt'),(L,'008'):('part','Satellite, Grayscale chạy; Street View không kéo được'),(L,'009'):('run','Màu theo độ tươi: 30 phút, 1 giờ'),(L,'011'):('run','Vị trí giả lập: Entered, Exited, Automation TEST chạy 2 lần'),(L,'012'):('run','Tạo, gán, trùng, kết thúc, tự gán theo vùng'),(L,'013'):('run','Xem sau khi có vị trí'),(R,'003'):('part','4/5 cách; Get Service at Shop cần bật Shop Network'),(R,'004'):('run','Đóng, mở lại'),(R,'005'):('run','Hạn, Overdue'),(R,'013'):('run','Mở lại lệnh đã Completed'),(R,'007'):('run','Một sự cố ở 2 lệnh'),(R,'011'):('run','Open, Pending, điều kiện hoàn thành'),(N,'005'):('run','Đóng bằng lệnh, phiếu dịch vụ, sớm, lùi ngày'),(N,'006'):('run','Hết hạn, đồng hồ đổi, hoãn rồi hoàn thành'),(N,'011'):('run','Tạo, thêm đầu việc, gắn xe'),(N,'012'):('run','Gia hạn xe'),(S,'012'):('run','Tạo, bật, chạy, tắt, Archive'),(S,'014'):('run','Đọc đủ 18 mẫu'),(V,'001'):('run','Tạo xe; sau đó chạm trần 5 xe của gói thử'),(V,'011'):('run','Trùng xe chặn, trùng người không chặn'),
(R,'002'):('run','Tay, từ phiếu kiểm, mã lỗi Sample'),(R,'006'):('run','Form đủ trường, số lệnh'),(R,'008'):('run','Công, phụ tùng, lỗi tiền 100 lần'),(R,'009'):('run','Thêm công, rate liên hệ'),(R,'010'):('run','Tổng, lệch tiền'),(R,'012'):('run','Điều kiện, số cuối nhỏ hơn đầu'),(R,'014'):('run','Entry tạo tay, sửa'),(R,'016'):('run','Tạo, trùng, archive; không thấy Merge'),(R,'018'):('part','Copy chạy; Print chưa đọc được PDF'),(R,'020'):('run','Nhiều sự cố, Discard, bỏ việc'),(R,'021'):('run','Đủ, thiếu, Rerun, sai số'),(R,'023'):('view','Chỉ dữ liệu Sample'),(R,'025'):('part','Tạo, Opportunity; xe TEST-SUA chưa dựng'),
(N,'001'):('run','Mốc từ 0, biên'),(N,'004'):('run','Biên ngưỡng, Void'),(N,'007'):('run','Menu Resolve'),(N,'008'):('run','Công thức khớp'),(N,'009'):('docs','Không bật vì đổi Cài đặt'),(N,'013'):('run','Dựng, phiên bản Past Version'),(N,'014'):('part','11 loại đọc; 8 loại lưu'),(N,'015'):('run','Bắt buộc, ghi chú, E-001, E-003'),(N,'016'):('part','Workflow không tạo được lệnh; chưa lưu'),(N,'017'):('part','Gán Daily; chưa qua ngày'),(N,'018'):('run','Không có nháp; lệch múi giờ'),(N,'019'):('run','Gộp lỗi lặp, Acknowledge'),(N,'020'):('part','Web không có câu xác nhận'),(N,'021'):('part','Vị trí giả; cờ từng mục cần app'),(N,'022'):('view','Cấu hình'),
(K,'002'):('run','Nhiều kho, tồn theo kho'),(K,'005'):('run','Chỉnh âm không chặn'),(K,'006'):('run','Tự cắt số lượng'),(K,'007'):('run','Biên điểm đặt lại'),(K,'008'):('part','Static; FIFO, LIFO cần đổi Cài đặt'),(K,'010'):('part','Tự duyệt; Pending, Rejected cần người thứ hai'),(K,'013'):('run','Vào kho, vào lệnh'),(K,'019'):('part','Capacity; Personal, Void'),(K,'021'):('view','Cần tích hợp'),(K,'022'):('run','Nhập tay có cảnh báo, biên 60 và 60,5'),
(S,'001'):('view','Đọc đủ'),(S,'008'):('run','Đích từng thẻ'),(S,'013'):('run','Nhiều loại'),(S,'017'):('run','Theo dõi, comment'),(S,'019'):('part','49 báo cáo; mở sâu 1; Share có link công khai'),(S,'020'):('run','Trả lời sai số'),(S,'023'):('run','Chạm trần 5 xe'),(S,'024'):('view','Không tải tệp')}
EXTRA={'Vehicles · Lốp':[('Lốp là đối tượng độc lập, kho lốp','Fleetio không có','run','Tháo xong chỉ còn lịch sử')],
'Fleet Map':[('Gom cụm marker','Mới thử 2 xe','part','Chưa đủ kết luận')],
'Renewals':[('Gia hạn liên hệ','','part','Tạo, chưa mở chi tiết')],
}
BLOCK=[('Tools','Không mở trial theo chọn của user'),('Advanced Analytics','Không mở trial theo chọn của user'),('Custom Records, trường tuỳ chỉnh','Không mở theo chọn của user; chỉ có tài liệu hãng'),('App Fleetio Go','Chưa xem; cần điện thoại'),('Kết nối thật GPS, ERP, thanh toán','Không kết nối; cần tài khoản ngoài')]
LBL={'run':'Đã chạy','part':'Một phần','view':'Chỉ xem','docs':'Tài liệu','none':'Chưa','block':'Không mở'}
ORD={'none':0,'docs':1,'view':2,'part':3,'run':4,'block':0}
rows=[]
for m,src,ag in MOD:
    for g,ns in src:
        for n in ns:
            x=fr[(g,n)]; a,b=lv(x['src']),x['src']
            if (g,n) in OVR:
                c_,b=OVR[(g,n)]
                if ORD[c_]<ORD[a]: a=c_
                elif ORD[c_]>ORD[a]: b=b+' · SRS ghi: '+x['src']
            rows.append(dict(m=m,t=x['t'],d=re.sub(r'\s+',' ',x['d'])[:140],s=a,e=b,id=x['id'],ag=ag))
    for t,d,a,b in EXTRA.get(m,[]): rows.append(dict(m=m,t=t,d=d,s=a,e=b,id='',ag=ag))
for t,why in BLOCK: rows.append(dict(m='Ngoài phạm vi đợt này',t=t,d=why,s='block',e=why,id='',ag='—'))
ACT=set(sys.argv[1:]) or {'tires','repair','reminders','parts','platform'}
for r in rows: r['running']=r['ag'] in ACT
cnt={k:sum(1 for r in rows if r['s']==k) for k in LBL}
# md
L_=['---','type: research','feature: fleetio','status: draft','updated: 2026-11-03','links:','  - docs/_research/fleetio/README.md','---','','# Fleetio: danh sách chức năng và mức đã đi','',f'Tổng {len(rows)} chức năng: '+' · '.join(f'{LBL[k]} {cnt[k]}' for k in LBL)+'.','','`Đã chạy` = tự thao tác, thấy kết quả. `Một phần` = đi được một nhánh. `Chỉ xem` = thấy giao diện, chưa thao tác. `Tài liệu` = chỉ đọc tài liệu hãng.','']
for m in dict.fromkeys(r['m'] for r in rows):
    L_+=[f'## {m}','','| Chức năng | Mô tả | Mức | Đã đi tới đâu |','|---|---|---|---|']
    for r in rows:
        if r['m']==m: L_.append('| {} | {} | {} | {} |'.format(r['t'],r['d'].replace('|','/'),LBL[r['s']],r['e'].replace('|','/')))
    L_.append('')
(D/'fleetio-function-list.md').write_text('\n'.join(L_))
json.dump(dict(rows=rows,cnt=cnt,lbl=LBL),open(D/'run-notes/_function_list.json','w'),ensure_ascii=False)
print(len(rows),cnt)

# trang HTML
logo=''
for p in ['design/brand/innvie-v1/innvie-logo-reverse.svg','design/brand/innvie/innvie-logo-reverse.svg']:
    if pathlib.Path(p).exists(): logo=pathlib.Path(p).read_text(); break
logo=re.sub(r'<\?xml.*?\?>','',logo)
data=json.dumps(rows,ensure_ascii=False).replace('</','<\\/')
tot=len(rows)
PAGE='''<!DOCTYPE html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Fleetio: danh sách chức năng và mức đã đi</title>
<link href="https://fonts.googleapis.com/css2?family=Cal+Sans&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root{--b:#0036B5;--ink:#171717;--mu:#5b6472;--line:#e5e8ee;--bg:#f6f7f9}*{box-sizing:border-box}body{margin:0;font:14px/1.5 Inter,system-ui,sans-serif;color:var(--ink);background:var(--bg)}
.band{background:var(--b);color:#fff;padding:20px 24px;display:flex;gap:16px;align-items:center}.band svg{height:26px;width:auto}.band h1{font:400 22px/1.2 "Cal Sans",Inter,sans-serif;margin:0}
main{max-width:1180px;margin:0 auto;padding:20px 16px 60px}.lead{margin:0 0 16px;color:var(--mu)}mark{background:#fff3b0;color:inherit;padding:0 2px}
.stat{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:8px;margin-bottom:12px}.st{background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 12px;text-align:left;cursor:pointer;font:inherit;color:inherit}.st b{display:block;font:400 22px "Cal Sans",Inter}.st.on{outline:2px solid var(--b)}
.prog{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:8px;margin-bottom:12px}.pc{background:var(--b);color:#fff;border-radius:12px;padding:14px 16px}.pc.alt{background:#fff;color:var(--ink);border:1px solid var(--line)}.pc b{display:block;font:400 34px/1.1 "Cal Sans",Inter}.pc small{display:block;margin-top:4px;opacity:.85;font-size:12px}.bar{display:flex;height:10px;border-radius:6px;overflow:hidden;margin:0 0 16px;background:var(--line)}.bar i{display:block}
.tool{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:16px;align-items:center}input[type=search]{flex:1;min-width:200px;padding:8px 10px;border:1px solid var(--line);border-radius:8px;font:inherit}label{display:flex;gap:6px;align-items:center;color:var(--mu)}
section{background:#fff;border:1px solid var(--line);border-radius:12px;margin-bottom:12px;overflow:hidden}section>h2{font:400 16px "Cal Sans",Inter;margin:0;padding:12px 14px;border-bottom:1px solid var(--line);display:flex;gap:8px;align-items:center;justify-content:space-between}.mini{display:flex;height:6px;width:120px;border-radius:4px;overflow:hidden;background:var(--line)}.mini i{display:block}
table{width:100%;border-collapse:collapse}td,th{padding:9px 14px;text-align:left;vertical-align:top;border-top:1px solid var(--line)}th{font-size:12px;color:var(--mu);font-weight:500;border-top:0}td.n{font-weight:600;width:24%}td.d{color:var(--mu)}td.e{width:24%}
.p{display:inline-block;padding:1px 8px;border-radius:99px;font-size:12px;font-weight:500;white-space:nowrap}.run{background:#dcf5e4;color:#0b6b33}.part{background:#fff0cc;color:#7a5200}.view{background:#e4ecfb;color:#0036b5}.docs{background:#eee;color:#444}.none{background:#fde4e4;color:#a11616}.block{background:#ececf2;color:#555}.dig{display:block;margin-top:4px;font-size:12px;color:#0036b5}
@media(max-width:720px){td.d{display:none}th.d{display:none}td.n{width:auto}td.e{width:auto}}
</style></head><body><div class="band">__LOGO__<h1>Fleetio: danh sách chức năng và mức đã đi</h1></div><main>
<p class="lead">__T__ chức năng, theo menu thật của Fleetio và SRS phân tích ngược. <mark>Chỉ tính "Đã chạy" khi tự thao tác và thấy kết quả</mark>, bằng dữ liệu TEST trên tài khoản dùng thử. Cập nhật 03/11/2026. Danh sách lấy từ SRS sau khi viết lại đủ 7 nhóm, nên mỗi chức năng được tách nhỏ hơn bản trước và mức lấy theo cột Mức của SRS; hai nguồn lệch thì tính mức thấp hơn. Phần chưa trọn chủ yếu vì gói thử 5 xe, tài khoản 1 người dùng, hoặc cần đổi Cài đặt. Các phần tính theo vị trí giả lập được ghi rõ ở từng dòng. Charging đã bỏ khỏi danh sách theo yêu cầu.</p>
<div class="prog" id="prog"></div><div class="stat" id="stat"></div><div class="bar" id="bar"></div>
<div class="tool"><input type="search" id="q" placeholder="Tìm chức năng"><input type="checkbox" id="dig" hidden></div><div id="list"></div></main>
<script>const R=__DATA__;const L={run:'Đã chạy',part:'Một phần',view:'Chỉ xem',docs:'Tài liệu',none:'Chưa',block:'Không mở'},C={run:'#34a853',part:'#f2b01e',view:'#5b8def',docs:'#a7adb8',none:'#e25555',block:'#cfd2da'};let F=null;
const E=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
function draw(){const n=k=>R.filter(r=>r.s===k).length,T=R.length,W=Math.round((n('run')+n('part')*.5)/T*100),X=Math.round(n('run')/T*100),Y=Math.round((n('run')+n('part')+n('view')+n('docs'))/T*100);document.getElementById('prog').innerHTML=`<div class="pc"><b>${W}%</b>Tiến độ tổng<small>Đã chạy tính đủ, một phần tính nửa: (${n('run')} + ${n('part')}/2) trên ${T}</small></div><div class="pc alt"><b>${X}%</b>Đã chạy trọn<small>${n('run')} trên ${T} chức năng</small></div><div class="pc alt"><b>${Y}%</b>Đã biết tới, kể cả chỉ xem, đọc tài liệu<small>Còn lại: chưa đi và không mở</small></div>`;const q=document.getElementById('q').value.toLowerCase(),dg=document.getElementById('dig').checked;const cnt={};R.forEach(r=>cnt[r.s]=(cnt[r.s]||0)+1);
document.getElementById('stat').innerHTML=Object.keys(L).map(k=>`<button class="st ${F===k?'on':''}" data-k="${k}"><b>${cnt[k]||0}</b>${L[k]}</button>`).join('');
document.getElementById('bar').innerHTML=Object.keys(L).map(k=>`<i style="width:${(cnt[k]||0)/R.length*100}%;background:${C[k]}"></i>`).join('');
const v=R.filter(r=>(!F||r.s===F)&&(!dg||r.running)&&(!q||(r.t+r.d+r.m).toLowerCase().includes(q)));const ms=[...new Set(v.map(r=>r.m))];
document.getElementById('list').innerHTML=ms.map(m=>{const all=R.filter(r=>r.m===m),rs=v.filter(r=>r.m===m);const mini=Object.keys(L).map(k=>{const n=all.filter(r=>r.s===k).length;return n?`<i style="width:${n/all.length*100}%;background:${C[k]}"></i>`:''}).join('');
return `<section><h2>${E(m)}<span class="mini">${mini}</span></h2><table><tr><th>Chức năng</th><th class="d">Mô tả</th><th>Mức</th><th>Đã đi tới đâu</th></tr>${rs.map(r=>`<tr><td class="n">${E(r.t)}</td><td class="d">${E(r.d)}</td><td><span class="p ${r.s}">${L[r.s]}</span>${r.running?'<span class="dig">Đang đào sâu</span>':''}</td><td class="e">${E(r.e)}</td></tr>`).join('')}</table></section>`}).join('')||'<p>Không có mục khớp.</p>';
document.querySelectorAll('.st').forEach(b=>b.onclick=()=>{F=F===b.dataset.k?null:b.dataset.k;draw()})}
document.getElementById('q').oninput=draw;document.getElementById('dig').onchange=draw;draw();</script></body></html>'''
(D/'fleetio-function-list.html').write_text(PAGE.replace('__LOGO__',logo).replace('__DATA__',data).replace('__T__',str(tot)))
