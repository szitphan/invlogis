import sys; sys.path.insert(0,str(__import__('pathlib').Path(__file__).parent))
from build_docs import *

# ---- letterhead ----
LH=[('p','Số / No.: [chờ: số công văn]','m'),
('p','[chờ: địa danh], ngày [chờ: ngày] tháng [chờ: tháng] năm [chờ: năm]','m'),
('p','Kính gửi: Quý công ty [chờ: tên đơn vị nhận]'),
('p','V/v: [chờ: trích yếu nội dung]'),
('p','Invlogis trân trọng gửi tới Quý công ty [chờ: nội dung thư, đoạn mở đầu].'),
('p','[chờ: đoạn nội dung tiếp theo]'),
('p','Trân trọng cảm ơn Quý công ty và rất mong nhận được phản hồi.'),
('sig',[('ĐẠI DIỆN [chờ: tên pháp nhân đầy đủ]','On behalf of the company','[chờ: Họ và tên, chức danh]'),('','','')][:1]),
]
build("letterhead","letterhead",LH,HDR,FTR,"Giấy tiêu đề Invlogis")

# ---- quotation ----
Q=[('title','BÁO GIÁ','QUOTATION','Số / No.: BG-[chờ: số báo giá] · Ngày / Date: [chờ: dd/mm/yyyy] · Hiệu lực / Valid for: [chờ: số ngày] ngày'),
('h','1. Bên báo giá','Supplier'),
('kv',[('Đơn vị','[chờ: tên pháp nhân đầy đủ] (Invlogis by innvie)'),('Địa chỉ','[chờ: địa chỉ]'),('Mã số thuế','[chờ: MST]'),('Người liên hệ','[chờ: họ tên] · [chờ: chức danh] · [chờ: số điện thoại] · [chờ: email]')]),
('h','2. Khách hàng','Customer'),
('kv',[('Kính gửi','Quý công ty [chờ: tên khách hàng]'),('Địa chỉ','[chờ: địa chỉ khách hàng]'),('Mã số thuế','[chờ: MST khách hàng]'),('Người nhận','[chờ: họ tên, chức danh]')]),
('p','Invlogis trân trọng gửi tới Quý công ty bảng báo giá dưới đây. Đơn vị tiền tệ: [chờ: VND].'),
('h','3. Bảng báo giá','Price schedule'),
('table',['STT|No.','Dịch vụ|Service','ĐVT|Unit','SL|Qty','Đơn giá|Unit price','Thành tiền|Amount','VAT'],
 [['1','[chờ: tên dịch vụ / module]','[chờ]','[chờ]','[chờ: đơn giá]','[chờ: thành tiền]','[chờ]'],
  ['2','[chờ: phí triển khai ban đầu]','[chờ]','[chờ]','[chờ: đơn giá]','[chờ: thành tiền]','[chờ]'],
  ['3','[chờ: phí thuê bao theo kỳ]','[chờ]','[chờ]','[chờ: đơn giá]','[chờ: thành tiền]','[chờ]'],
  ['4','[chờ: hạng mục khác]','[chờ]','[chờ]','[chờ: đơn giá]','[chờ: thành tiền]','[chờ]'],
  ['','Cộng tiền hàng / Subtotal','','','','[chờ: tổng]',''],
  ['','Thuế GTGT / VAT','','','','[chờ: tiền thuế]',''],
  ['','Tổng cộng / Total','','','','[chờ: tổng cộng]','']],
 [10,50,16,13,26,30,16],'cllrrrc',3),
('p','Bằng chữ / In words: [chờ: số tiền bằng chữ]'),
('h','4. Điều khoản','Terms'),
('p','4.1. Hiệu lực báo giá: [chờ: số ngày] ngày kể từ ngày phát hành.'),
('p','4.2. Thanh toán: [chờ: điều khoản thanh toán, đợt, hạn, hình thức].'),
('p','4.3. Phạm vi và thời gian triển khai: [chờ: phạm vi, mốc bàn giao].'),
('p','4.4. Các khoản chưa bao gồm: [chờ: liệt kê].'),
('p','4.5. Điều khoản thương mại khác: [chờ: nội dung đã được bộ phận thương mại / pháp lý duyệt].'),
('p','Trân trọng cảm ơn sự quan tâm của Quý công ty.'),
('sig',[('ĐẠI DIỆN BÊN BÁO GIÁ','Supplier','[chờ: họ tên, chức danh]'),('XÁC NHẬN CỦA KHÁCH HÀNG','Customer acceptance','[chờ: họ tên, chức danh]')]),
]
build("bao-gia-template","quotation",Q,HDR,FTR,"Mẫu báo giá Invlogis")

# ---- contract ----
LAW="[Cần luật sư duyệt]"
def art(n,vn,en,items):
    r=[('h',f'Điều {n}. {vn}',en)]
    for i,t in enumerate(items,1): r.append(('p',f'{n}.{i}. {t} {LAW}'))
    return r
C=[('title','HỢP ĐỒNG DỊCH VỤ','SERVICE AGREEMENT','Số / No.: [chờ: số hợp đồng] · Ngày / Date: [chờ: dd/mm/yyyy]'),
('p','BẢN MẪU KHUNG, CHƯA PHẢI VĂN BẢN PHÁP LÝ. Mọi nội dung điều khoản bên dưới là chỗ trống để luật sư soạn và duyệt trước khi dùng. Không ký, không gửi khách khi chưa duyệt.','i'),
('p','Căn cứ pháp lý: [chờ: danh mục văn bản pháp luật áp dụng] '+LAW),
('h','Điều 1. Các bên','Parties'),
('kv',[('BÊN A (Bên cung cấp)','[chờ: tên pháp nhân đầy đủ] (Invlogis by innvie)'),('Địa chỉ','[chờ: địa chỉ]'),('Mã số thuế','[chờ: MST]'),('Đại diện','[chờ: họ tên] · [chờ: chức danh] · theo [chờ: giấy ủy quyền, nếu có]'),('Điện thoại / Email','[chờ: số điện thoại] · [chờ: email]'),('Tài khoản','[chờ: số tài khoản, ngân hàng]'),
 ('BÊN B (Khách hàng)','Quý công ty [chờ: tên khách hàng]'),('Địa chỉ','[chờ: địa chỉ khách hàng]'),('Mã số thuế','[chờ: MST khách hàng]'),('Đại diện','[chờ: họ tên, chức danh]'),('Thông tin các bên','[chờ: đối chiếu đăng ký kinh doanh] '+LAW)]),
]
C+=art(2,'Giải thích từ ngữ','Definitions',['Các thuật ngữ: Dịch vụ, Phần mềm Invlogis, Dữ liệu khách hàng, Tài khoản người dùng, Ngày làm việc, Sự cố [chờ: định nghĩa từng thuật ngữ].'])
C+=art(3,'Phạm vi dịch vụ','Scope of services',['Gói và module cung cấp: [chờ: danh sách module theo báo giá số BG-[chờ: số báo giá]].','Cấu hình theo khách: [chờ: tham số / danh mục cấu hình thuộc phạm vi].','Đào tạo, triển khai, hỗ trợ: [chờ: phạm vi, mốc bàn giao].','Nội dung nằm ngoài phạm vi: [chờ: liệt kê].'])
C+=art(4,'Phí và thanh toán','Fees and payment',['Các khoản phí: [chờ: phí triển khai, phí thuê bao, phí phát sinh].','Kỳ, hạn, hình thức thanh toán: [chờ: nội dung].','Hóa đơn và thuế GTGT: [chờ: nội dung].','Chậm thanh toán: [chờ: nội dung].','Điều chỉnh giá: [chờ: nội dung].'])
C+=art(5,'Mức độ dịch vụ (SLA) và an toàn dữ liệu','SLA and data security',['Thời gian hoạt động cam kết: [chờ: chỉ số SLA].','Thời gian phản hồi và xử lý sự cố: [chờ: bảng mức độ].','Sao lưu và khôi phục: [chờ: nội dung].','Bảo vệ dữ liệu cá nhân và dữ liệu khách hàng, nơi lưu trữ: [chờ: nội dung].','Bồi thường, giới hạn trách nhiệm: [chờ: nội dung].'])
C+=art(6,'Bảo mật thông tin','Confidentiality',['Phạm vi thông tin mật: [chờ: nội dung].','Nghĩa vụ của mỗi bên và thời hạn: [chờ: nội dung].'])
C+=art(7,'Thời hạn và chấm dứt hợp đồng','Term and termination',['Thời hạn hiệu lực: [chờ: thời hạn, gia hạn].','Quyền chấm dứt, thông báo, xử lý dữ liệu khi chấm dứt: [chờ: nội dung].','Bất khả kháng: [chờ: nội dung].'])
C+=art(8,'Giải quyết tranh chấp','Dispute resolution',['Thương lượng, hòa giải, cơ quan giải quyết, luật áp dụng: [chờ: nội dung].'])
C+=art(9,'Điều khoản chung','General provisions',['Sửa đổi, bổ sung, phụ lục, ngôn ngữ, số bản, hiệu lực: [chờ: nội dung].','Phụ lục: [chờ: Phụ lục 1 Báo giá · Phụ lục 2 SLA · Phụ lục 3 Xử lý dữ liệu].'])
C+=[('p','Hợp đồng lập thành [chờ: số bản] bản có giá trị như nhau, mỗi bên giữ [chờ: số bản] bản. '+LAW),
('sig',[('ĐẠI DIỆN BÊN A','Party A','[chờ: họ tên, chức danh]'),('ĐẠI DIỆN BÊN B','Party B','[chờ: họ tên, chức danh]')])]
build("hop-dong-template","contract",C,HDR,FTR,"Mẫu hợp đồng dịch vụ Invlogis")
