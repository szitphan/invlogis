---
type: brainstorm
feature: debt-management
status: draft
updated: 2026-10-20
links:
  - docs-input/sop/apas-thanh-toan-doi-soat/apas-thanh-toan-doi-soat.md
  - docs-input/sop/delta-3-0-master-plan/delta-3-0-master-plan.md
  - docs-input/sop/quan-ly-quy-thanh-toan/quan-ly-quy-thanh-toan.md
  - docs-input/sop/sop-cung-cap-dich-vu-tong-quat.md
  - docs-input/tich-hop/vis-sim-cong-tac-chuan-bi/vis-sim-cong-tac-chuan-bi.md
  - docs/_product/prd.md
  - docs/service-delivery/brainstorms/service-delivery.md
---

# Công nợ, hoá đơn và bảng kê

> Brainstorm khung lập 2026-10-20 để nhận các mục nguồn đã giao cho feature này (DEC-230). Chưa phỏng vấn.

## 1. Idea Seed

Quản lý bảng kê và công nợ phải thu, phải trả theo JobID; duyệt doanh thu; mua ngoài dịch vụ; phát hành hoá đơn; đối soát hoá đơn đầu vào (kể cả hoá đơn vô chủ); kê khai thuế; kết nối MISA. Cung cấp kết quả kiểm nợ quá hạn, hạn mức tín dụng và gia hạn nợ cho bước duyệt JobID của `service-delivery`.

## 2. Context

Feature chưa có trong Feature Map của PRD sản phẩm (PRD OQ-6, OQ-17).

Ranh giới với `service-delivery`: JobID là nơi ghi chi phí, doanh thu; feature này sở hữu quy trình riêng và trả kết quả về JobID.

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
| SRC-31 | Quy trình quản lý quỹ & Thanh toán | 4.10 Thanh toán nhà cung cấp | nhận dữ liệu từ Quy trình quản lý nợ phải trả (SRC-03 5.3); chặn thanh toán NCC qua quy trình khác; hạn trả sau tính theo cách 1/cách 2, lưu trên danh mục NCC; comment 08–09/10 về lý do tách 6 quy trình |
| SRC-31 | Quy trình quản lý quỹ & Thanh toán | 5.7 Quy trình thanh toán nhà cung cấp |  |
| SRC-31 | Quy trình quản lý quỹ & Thanh toán | Đính kèm 01 Quản lý hóa đơn đầu vào (AI01) | bản 20/06; APAS 17/10 thay AI01 bằng DIS + IIP (SRC-07 2.2, 3.3), đối chiếu khi viết IIP |
| SRC-03 | Quy trình cung cấp dịch vụ tổng quát | 4.3 Mua ngoài dịch vụ | nhà cung cấp, phân loại, quy trình mua ngoài; kê khai trên JobID (4.2.7) ở lại service-delivery |
| SRC-03 | Quy trình cung cấp dịch vụ tổng quát | 4.3.5 Phương thức thanh toán chi phí mua ngoài (mã phí 02xx) | nhóm mã phí 02xx/0201/03xx |
| SRC-03 | Quy trình cung cấp dịch vụ tổng quát | 4.5 Lệch pha giữa kỳ thanh toán và kỳ hạch toán | kỳ ghi chi phí về muộn |
| SRC-03 | Quy trình cung cấp dịch vụ tổng quát | 4.5.3 Ghi nhận doanh thu và chi phí |  |
| SRC-03 | Quy trình cung cấp dịch vụ tổng quát | 4.10 Giải pháp phát hành hóa đơn | lệch với SIM (SIM ghi QT 5.2, SOP ghi 5.4) |
| SRC-03 | Quy trình cung cấp dịch vụ tổng quát | 5.3 Quy trình quản lý nợ phải trả |  |
| SRC-03 | Quy trình cung cấp dịch vụ tổng quát | 5.4 Quy trình quản lý nợ phải thu |  |
| SRC-24 | Tích hợp hệ thống VIS & SIM — Công tác chuẩn bị | 2.3 Phân hệ SIM — Tích hợp Open API MISA meInvoice & AMIS | ký số Cloud HSM, đồng bộ ngược tạo chứng từ chi |
| SRC-24 | Tích hợp hệ thống VIS & SIM — Công tác chuẩn bị | 3.2 MISA (meInvoice, AMIS, eSign Cloud) | Open API meInvoice, eSign Cloud, webhook/pull hóa đơn đầu vào, đồng bộ ngược AMIS ghi mã FT vào số chứng từ gốc |

## 4. Open Questions

Chưa có — sinh khi phỏng vấn.

## 5. Next Steps

- `/brainstorm debt-management` — phỏng vấn đầy đủ từ các mục nguồn ở Mục 3
