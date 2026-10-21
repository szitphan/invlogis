---
type: brainstorm
feature: invoice-management
status: draft
updated: 2026-10-21
links:
  - docs-input/sop/apas-thanh-toan-doi-soat/apas-thanh-toan-doi-soat.md
  - docs-input/sop/delta-3-0-master-plan/delta-3-0-master-plan.md
  - docs-input/sop/quan-ly-quy-thanh-toan/quan-ly-quy-thanh-toan.md
  - docs-input/sop/sop-cung-cap-dich-vu-tong-quat.md
  - docs-input/sop/sim-ke-khai-thue-tu-dong/sim-ke-khai-thue-tu-dong.md
  - docs-input/tich-hop/vis-sim-cong-tac-chuan-bi/vis-sim-cong-tac-chuan-bi.md
  - docs-input/sop/vis-giam-sat-doi-xe/vis-giam-sat-doi-xe.md
  - docs/debt-management/brainstorms/debt-management.md
  - docs/payment-on-behalf/brainstorms/payment-on-behalf.md
  - docs/fund-payments/brainstorms/fund-payments.md
  - docs/service-delivery/brainstorms/service-delivery.md
  - docs/_product/prd.md
---

# Hoá đơn đầu vào, đầu ra và kê khai thuế

> Brainstorm khung lập 2026-10-21, tách khối hoá đơn khỏi `debt-management` (DEC-251). Mục 4 ghi điểm đã chốt ở phỏng vấn SIM 14/10/2026; chưa phỏng vấn đầy đủ.

## 1. Idea Seed

Hoá đơn đầu vào tự về và tự khớp với khoản tiền đã chi; hoá đơn vô chủ và hoá đơn trả bằng tiền cá nhân có luồng duyệt riêng; hoá đơn đầu ra phát hành, điều chỉnh, thay thế từ bảng kê đã chốt; dữ liệu hoá đơn đã định danh đẩy sang phần mềm kế toán để kê khai thuế hằng tháng.

## 2. Context

Delta gọi phần này là các phân hệ IIP (hoá đơn đầu vào), SII (phát hành hoá đơn) và ATR (kê khai thuế) của APAS (17/10/2026). Feature chưa có trong Feature Map của PRD sản phẩm (PRD OQ-6, OQ-17).

Ranh giới:
- `debt-management`: lập, chốt bảng kê; công nợ phải thu, phải trả; hạn mức, gia hạn nợ. Bảng kê đã chốt là đầu vào để phát hành hoá đơn ở đây.
- `payment-on-behalf`: Yêu cầu thanh toán, QR, lệnh chi qua ngân hàng, mã giao dịch ngân hàng (mã FT). Feature này dùng mã FT để khớp hoá đơn.
- `fund-payments`: tạm ứng, dư nợ tạm ứng, phiếu chi, phiếu thu. Hoá đơn khớp xong thì ghi giảm dư nợ tạm ứng ở đó.
- `service-delivery`: JobID nhận chi phí từ hoá đơn đã duyệt (E15) và số hoá đơn đầu ra (trạng thái "Đã xuất hoá đơn").
- Khối đọc chứng từ dùng chung (DIS) đọc ảnh, PDF; feature này nhận dữ liệu đã tách.

## 3. Mục nguồn đã giao

| Nguồn | Tài liệu | Mục | Ghi chú sổ đối chiếu |
|---|---|---|---|
| SRC-07 | Phân hệ APAS — Hệ thống tự động hóa thanh toán & Đối soát công nợ | Luồng xử lý Hóa đơn đầu vào | gói dữ liệu hóa đơn đã tách (MST, ký hiệu, số, ngày, tiền trước thuế, thuế, tổng) chuyển IIP |
| SRC-07 | Phân hệ APAS — Hệ thống tự động hóa thanh toán & Đối soát công nợ | 3.2 Phát hành và điều chỉnh hóa đơn tự động (SII) | lệch SOP tổng quát 4.10; mới ở bản 17/10: chỉ phát hành hóa đơn thay thế khi Mẫu 04/SS-HĐĐT đã ký số và gửi Cục thuế thành công |
| SRC-07 | Phân hệ APAS — Hệ thống tự động hóa thanh toán & Đối soát công nợ | 3.3 Tự động đối soát hóa đơn đầu vào và thanh toán (IIP) | A9 (`transport-dispatch`) có một phần; lệch A9 vs IIP; pháp nhân Delta Vận tải (SIM) vs Delta Hải Phòng (VIS-SIM). Bản 17/10: đầu vào chỉ XML meInvoice + JSON DIS; định danh 2 lớp; kiểm trùng trước đối chiếu; khớp 1-1 thêm lệch ngày ≤3 ngày + bảng ánh xạ MST/tên tài khoản; N-1, 1-N sai số 0 VND, lệch vào hàng chờ 24 giờ; 3 trường hợp, chi tiền cá nhân duyệt ba cấp CBQL → Kế toán → BGĐ |
| SRC-07 | Phân hệ APAS — Hệ thống tự động hóa thanh toán & Đối soát công nợ | 3.3.3 Quản lý hóa đơn vô chủ | trước là 3.3.5; bản 17/10 chia 2 nhóm: lỗi đối soát (kế toán gán mã FT, trả về danh mục chờ thanh toán của nhân viên) và xuất nhầm MST (từ chối hoặc chấp nhận tạo Yêu cầu thanh toán theo Quy trình 5.3); ⚠ theo SOP Quản lý quỹ & Thanh toán, có hóa đơn là Quy trình 5.2 (5.3 là không hóa đơn), cần hỏi khách |
| SRC-07 | Phân hệ APAS — Hệ thống tự động hóa thanh toán & Đối soát công nợ | 3.3.4 Quy trình thanh toán hóa đơn không có mã FT (trả bằng tiền cá nhân) | kê JobID + nhóm phí, duyệt CBQL → Kế toán → BGĐ; JobID kế toán tự tạo Yêu cầu thanh toán, JobID nghiệp vụ chuyển vào JobID đó; "Quy trình 5.2" ở đây là Thanh toán có hóa đơn của SOP Quản lý quỹ & Thanh toán (đánh số riêng từng SOP, không lệch với 3.2) |
| SRC-07 | Phân hệ APAS — Hệ thống tự động hóa thanh toán & Đối soát công nợ | 3.4 Tự động kê khai & nộp báo cáo thuế hàng tháng (ATR) | nội dung SRC-25 (`_coverage/sim-ke-khai-thue-tu-dong.md`) gộp vào; tờ khai 01/GTGT, 05/KK-TNCN, 01/NTNN; ký MISA eSign, nộp T-VAN MISA mTax trước ngày 20; upload hóa đơn + chốt lương trước ngày 12, IIP đẩy AMIS trước ngày 15 |
| SRC-07 | Phân hệ APAS — Hệ thống tự động hóa thanh toán & Đối soát công nợ | IV. Rủi ro vận hành | 4.2 hàng đợi ký số, thử lại 1/5/15 phút, quá 5 lần "Ký số lỗi" báo kế toán; 4.3 đồng bộ ngược sang MISA AMIS ghi mã FT vào "Số chứng từ gốc" |
| SRC-07 | Phân hệ APAS — Hệ thống tự động hóa thanh toán & Đối soát công nợ | 5.1 Hướng dẫn phân loại hóa đơn | nhóm mã phí 02xx/0201/03xx; bản 17/10 đổi: nhóm 02 khác, 01, 04, 05 "phân loại theo JobID kế toán" (trước: không cần phân loại bước 2) |
| SRC-30 | Phần mềm Delta 3.0 — Thiết kế kiến trúc & Lộ trình phát triển | 2.1.2 Liên kết ngoại vi | Delta MIS đẩy bút toán từng giao dịch sang Misa qua API để Misa lập tờ khai thuế, BCTC; "cần xác định quy tắc chia sẻ dữ liệu giữa Delta MIS và Misa để hạn chế việc chỉnh sửa" (câu hỏi mở) |
| SRC-30 | Phần mềm Delta 3.0 — Thiết kế kiến trúc & Lộ trình phát triển | 7.2 API Phần mềm kế toán Misa gặp sự cố | hàng chờ cô lập + tự gửi lại mỗi 15 phút đến khi thông |
| SRC-31 | Quy trình quản lý quỹ & Thanh toán | Đính kèm 01 Quản lý hóa đơn đầu vào (AI01) | bản 20/06; APAS 17/10 thay AI01 bằng DIS + IIP (SRC-07 2.2, 3.3), đối chiếu khi viết IIP |
| SRC-03 | Quy trình cung cấp dịch vụ tổng quát | 4.10 Giải pháp phát hành hóa đơn | lệch với SIM (SIM ghi QT 5.2, SOP ghi 5.4) |
| SRC-24 | Tích hợp hệ thống VIS & SIM — Công tác chuẩn bị | 2.3 Phân hệ SIM — Tích hợp Open API MISA meInvoice & AMIS | ký số Cloud HSM, đồng bộ ngược tạo chứng từ chi |
| SRC-24 | Tích hợp hệ thống VIS & SIM — Công tác chuẩn bị | 3.2 MISA (meInvoice, AMIS, eSign Cloud) | Open API meInvoice, eSign Cloud, webhook/pull hóa đơn đầu vào, đồng bộ ngược AMIS ghi mã FT vào số chứng từ gốc |
| SRC-06 | Phân hệ VIS — Hệ thống giám sát phương tiện & Quản trị đội xe | Bước 4 - Đối soát hóa đơn cuối kỳ | cuối kỳ chỉ kiểm phát sinh: vé mồ côi, trạm "Chờ VETC", khớp tổng hoá đơn (BL-164) |

## 4. Đã chốt từ phỏng vấn SIM 14/10/2026

Trả lời của user trên trang phỏng vấn ngày 14/10, đối chiếu lại với APAS 17/10 ngày 21/10. Đưa vào Mục 4–7 chuẩn khi phỏng vấn đầy đủ.

- **Hoá đơn trùng, 3 trường hợp** (khoá trùng: mã số thuế người bán + ký hiệu + số hoá đơn): cùng hoá đơn về từ 2 nguồn (ảnh lái xe tải, XML từ MISA về sau) thì gộp, giữ XML làm bản gốc; 2 người tải cùng hoá đơn thì bản sau trỏ về bản đầu; hoá đơn đã dùng hoặc đang chờ duyệt ở yêu cầu khác thì từ chối, không xoá.
- **Lái xe tải hoá đơn trên Lệnh vận tải**, hoá đơn nối qua Yêu cầu thanh toán của Lệnh đó.
- **Tệp hoá đơn tải lên** tối đa 50 MB, 5 tệp mỗi hoá đơn.
- **Trạng thái hoá đơn đầu ra:** Chờ phát hành, Chờ ký, Đã cấp mã, Đã gửi khách; nhánh Ký số lỗi (kế toán bấm thử lại), Bị từ chối cấp mã (Cục thuế từ chối vì sai dữ liệu, không tự thử lại, kế toán sửa bảng kê), Bị thay thế, Bị điều chỉnh.
- **Đồng bộ sang MISA AMIS lỗi:** để lâu thì công nợ nhà cung cấp vẫn "chưa thanh toán" (có thể trả lần hai), sổ tiền gửi lệch sổ phụ ngân hàng, có thể mất khấu trừ thuế đầu vào. Lỗi kết nối thì hệ thống tự thử lại; lỗi dữ liệu (mã nhà cung cấp, tài khoản kế toán chưa có) hoặc lỗi còn tồn khi gần hạn ngày 15 thì tạo việc cho kế toán. Có bảng đối chiếu cuối ngày: giao dịch có mã FT mà phần mềm kế toán chưa có chứng từ.
- **Sổ phụ ngân hàng:** đề xuất chỉ phần mềm mình nhận sổ phụ (nối được mã FT với JobID); phần mềm kế toán nhận chứng từ đã định danh, không tự kéo sổ phụ, để một giao dịch không thành hai chứng từ.
- **Thuế nhà thầu:** chỉ gắn cờ cho hoá đơn của nhà cung cấp nước ngoài theo quốc gia trong danh mục đối tác; kế toán tính số thuế trên phần mềm kế toán. Lập tờ khai, ký số, nộp Cục thuế: ngoài phạm vi (MISA làm).
- **Nhắc tải hoá đơn** trước hạn ngày 12 hằng tháng, nhắc sớm theo cấu hình, mặc định 3 ngày; hạn đẩy dữ liệu sang phần mềm kế toán ngày 15.
- **Thông báo:** trong app và thông báo đẩy; email cho khách (hoá đơn) và cho kế toán khi cảnh báo nặng; SMS chỉ cho cảnh báo nặng.

**APAS 17/10 đã trả lời:**
- Hoá đơn trả bằng tiền cá nhân (không có mã FT) duyệt 3 cấp: cán bộ quản lý, kế toán, ban giám đốc (mục 3.3.4). Đóng câu hỏi 2 bước hay 3 bước (BL-111).
- Hoá đơn vô chủ còn 2 nhóm: lỗi đối soát (kế toán gán mã FT, trả về danh mục chờ thanh toán) và xuất nhầm mã số thuế (mục 3.3.3).
- Lệch tiền dù 1 đồng: cấm tự duyệt, vào hàng chờ tra soát 24 giờ cho kế toán xử lý tay (mục 3.3.2). Bản 17/10 không còn câu tự tạo phiếu chi hoàn tiền sau 24 giờ, đúng hướng user chọn ngày 14/10.
- Đọc ảnh, PDF do khối DIS làm (mục 2.2); IIP chỉ nhận dữ liệu đã tách.
- Phân loại hoá đơn: nhóm 01, 02 khác, 04, 05 theo JobID kế toán; nhóm 03 và 02 xuất lại theo JobID nghiệp vụ (phụ lục 5.1).

## 5. Open Questions

| ID | Câu hỏi | Nguồn khách | Trạng thái |
|---|---|---|---|
| OQ-1 | Luồng xuất hoá đơn đầu ra: ai lập yêu cầu (CS hay kế toán); một hoá đơn cho cả bảng kê hay có khách tách theo JobID? | Phân hệ APAS (17/10/2026), mục 3.2 | Còn mở (user chọn hỏi khách 14/10) |
| OQ-2 | Sơ đồ kê khai thuế vẫn ghi "Xử lý hoá đơn vô chủ: Tạo Phiếu chi hoàn tiền". Hoàn tiền tự động có còn không, hay chỉ sau duyệt tay? | Phân hệ APAS (17/10/2026), mục 3.4 sơ đồ luồng dữ liệu | Còn mở (dư từ BL-111) |
| OQ-3 | Mục 3.3.3 nhóm 2 ghi "Yêu cầu thanh toán có hoá đơn (Quy trình 5.3)", nhưng theo SOP Quản lý quỹ & Thanh toán thì có hoá đơn là Quy trình 5.2. Quy trình nào đúng? | Phân hệ APAS (17/10/2026), mục 3.3.3; Quy trình quản lý quỹ & Thanh toán, mục 5.2, 5.3 | Còn mở (BL-214) |
| OQ-4 | Tài liệu thuế ghi phần mềm tự tính thuế nhà thầu (2% TNDN, 5% GTGT). Đề xuất: phần mềm chỉ gắn cờ, kế toán tính trên phần mềm kế toán. Delta có đồng ý? | Phân hệ APAS (17/10/2026), mục 3.4 | Còn mở |
| OQ-5 | Delta có đang bật kết nối ngân hàng trong MISA AMIS không? | Chưa có trong tài liệu khách gửi | Còn mở |
| OQ-6 | Tên người bán "gần đúng" với tên tài khoản nhận: ngưỡng nào thì coi là khớp, hay chỉ dùng bảng ánh xạ mã số thuế ↔ tài khoản? | Phân hệ APAS (17/10/2026), mục 3.3.2 | Còn mở |
| OQ-7 | Hoá đơn tổng VETC cuối kỳ và hoá đơn dầu mua ngoài có đi qua IIP như hoá đơn đầu vào thường không, ai duyệt, gắn JobID nào? | Phân hệ VIS (18/10/2026), mục 3.1.3 Bước 4 | Còn mở (BL-120, BL-164) |
| OQ-8 | Hoá đơn trả bằng tiền cá nhân: hoàn cho người tải hoá đơn hay người đã chi, khi CS tải hộ hoá đơn lái xe đã trả? | Phân hệ APAS (17/10/2026), mục 3.3.4 | Còn mở |

## 6. Next Steps

- `/brainstorm invoice-management` — phỏng vấn đầy đủ từ các mục nguồn ở Mục 3, dùng lại điểm đã chốt ở Mục 4
