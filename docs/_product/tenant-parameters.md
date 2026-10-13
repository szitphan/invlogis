---
type: tenant-parameters
status: draft
status_changed: 2026-10-14
status_reason: "đã review upstream, không cần sửa"
updated: 2026-10-12
tenant_terms: [Delta, DK05, dGas, Nam Khánh, Phú Lợi, Pan Hải An]
links:
  - docs/_product/saas-core-vs-tenant.md
  - docs/service-delivery/brainstorms/service-delivery.md
  - docs/shipment-coordination/brainstorms/shipment-coordination.md
  - docs/transport-dispatch/brainstorms/transport-dispatch.md
  - docs/cross-process-flow/srs/cross-process-flow-spec.md
---

# Tham số theo khách

Mỗi dòng là một chỗ mà khách khác có thể cần giá trị khác. Tài liệu nghiệp vụ ghi mã `P-…` kèm giá trị của khách trong ngoặc; phần mềm đọc giá trị từ cấu hình của từng khách.

Kiểu: **Số** (con số, khoảng thời gian, tỷ lệ) · **Danh sách** (các lựa chọn khách sửa được) · **Bật/tắt** (tính năng một khách dùng, một khách không).

| Mã | Tham số | Kiểu | Tầng | Mặc định sản phẩm | Delta | Ai sửa | Dùng ở | Nguồn |
|---|---|---|---|---|---|---|---|---|
| P-nguong-tam-ung | Ngưỡng cách trả một khoản chi: dưới thì tạm ứng, từ ngưỡng trở lên tạo việc cho CS phụ trách + kế toán | Số (₫/khoản) | Cấu hình | chưa chốt | 5.000.000 ₫ | Admin khách | Điều phối E2 | Quy trình cung cấp dịch vụ tổng quát |
| P-ca-truc-ngoai-gio | Khung giờ trực ngoài giờ; người trực có quyền tự giao việc trong ca | Số (giờ bắt đầu–kết thúc) | Cấu hình | chưa chốt | 17h30–8h | Admin khách | Điều phối B3b | Quy trình điều phối mục 4 |
| P-ban-giao-ca-truc | Bàn giao việc đang dở đầu ca, cuối ca trực | Bật/tắt | Cấu hình | bật | bật | Admin khách | Điều phối B3b | Trả lời Delta 10/10 (OQ-26) |
| P-ly-do-chuyen-viec | Lý do bắt buộc khi CS bấm "Chuyển việc" | Danh sách | Cấu hình | chưa chốt | Hết giờ làm việc · Khác (tự ghi) | Admin khách | Điều phối B2 | Trả lời Delta 10/10 (OQ-25) |
| P-so-nguoi-goi-y-nhan-viec | Số người phần mềm gợi ý khi giao việc hiện trường | Số (người) | Cấu hình | 3 | 2–3 | Admin khách | Điều phối B3a | Brainstorm Điều phối |
| P-gop-giao-viec-ha-vo | Gộp giao việc Lệnh hạ vỏ theo vận đơn + nơi hạ khi JobID có 1 container | Bật/tắt | Cấu hình | chưa chốt | bật | Admin khách | Điều phối B4 | Trả lời Delta 10/10 (OQ-27) |
| P-duyet-chi-ngoai-dinh-muc | Luồng xin duyệt khoản chi ngoài định mức trên app trước khi chi | Bật/tắt | Cấu hình | bật | tắt | Admin khách | Điều phối E1 | Trả lời Delta 10/10 (OQ-29) |
| P-theo-doi-tien-hoan-nang-vo | Theo dõi tiền nâng vỏ chờ hoàn, cảnh báo quá hạn | Bật/tắt | Cấu hình | bật | tắt | Admin khách | Điều phối B5 | Trả lời Delta 10/10 (OQ-28) |
| P-han-hoan-tien-nang-vo | Số ngày chờ tiền nâng vỏ hoàn trước khi cảnh báo | Số (ngày) | Cấu hình | 7 | không dùng (tắt) | Admin khách | Điều phối B5 | Giao nhận hàng hoá (18/9/2026) |
| P-hinh-thuc-ky-bien-ban | Cách khách ký biên bản giao hàng | Danh sách | Cấu hình | chưa chốt | Ký điện tử · Biên bản giấy (cả hai) | Admin khách | Điều phối A7 | Trả lời Delta 10/10, xác nhận 12/10 (OQ-20) |
| P-email-bien-ban-giao-hang | Tự email biên bản cho CS và khách khi lái xe xác nhận | Bật/tắt | Cấu hình | chưa chốt | bật | Admin khách | Điều phối A7 | Trả lời Delta 10/10 (OQ-20) |
| P-ty-le-chia-lai-noi-bo | Cách chia lợi nhuận giao dịch nội bộ giữa chi nhánh | Số (tỷ lệ + cơ sở chia) | Gói: Đa chi nhánh | chưa chốt | 50/50 theo lãi gộp, sau khi chốt bảng kê công nợ | Admin khách | Điều phối B7 | Trả lời Delta 10/10 (OQ-4) |
| P-gio-mien-phi-luu-xe | Số giờ lưu xe miễn phí trước khi tính phí lưu ca | Số (giờ) | Gói: CBT | chưa chốt | 72 giờ | Admin khách | Điều phối E8 | Giao nhận hàng hoá (18/9/2026); tự tính chờ OQ-33 |
| P-ky-chot-duong-sat | Ngày chốt kỳ shipment list đường sắt | Danh sách (ngày trong tháng) | Gói: Đường sắt | chưa chốt | ngày 25 · cuối tháng | Admin khách | Điều phối D7, E3 | Giao nhận hàng hoá (18/9/2026) |
| P-nguon-don-gia-duong-sat | Nguồn đơn giá đường sắt | Danh sách | Gói: Đường sắt | chưa chốt | CS nhập tay (giai đoạn 1); báo giá Sales (giai đoạn 2) | Admin khách | Điều phối E3 | Trả lời Delta 10/10 (OQ-30) |
| P-chu-ky-nhac-nhiet | Chu kỳ nhắc nhập nhật ký nhiệt độ, theo loại hàng lạnh | Số (giờ/lần, theo loại hàng) | Gói: Hàng lạnh | chưa chốt | chưa chốt (OQ-43) | Trưởng điều vận | Điều phối D2 | Giao nhận hàng hoá (18/9/2026) |
| P-thoi-gian-cho-nhan-viec | Bao lâu không bấm nhận thì việc quay về cán bộ quản lý | Số (phút) | Cấu hình | chưa chốt | chưa chốt (OQ-41) | Admin khách | Điều phối 6.4 | — |
| P-nhac-jobid-dung-cong-no | Sau bao lâu nhắc CS về JobID dừng vì công nợ | Số (ngày) | Cấu hình | chưa chốt | chưa chốt (OQ-42) | Admin khách | Điều phối 6.4 | — |
| P-logo | Logo và tên app hiện ở góc menu, màn đăng nhập, splash mobile, splash web | Tệp logo + tên hiển thị | Cấu hình | chữ cái đầu tên khách trên ô vuông | Đã nhận logo gốc 12/10/2026 (`design/brand/delta/delta-logo-goc.jpg`, jpg nền trắng; chờ bản nền trong) | Admin khách | Khung trang (menu, đăng nhập, splash) | Chốt UI 12/10/2026 (design.md § Thương hiệu theo khách, § Splash web) |
| P-mau-logo | Màu nền ô logo. Chỉ ô logo đổi màu; nút, menu, tab, link và màu trạng thái giữ trung tính | Mã màu | Cấu hình | #262626 | #1B7B46 (user chốt 13/10/2026) | Admin khách | Khung trang (menu, đăng nhập) | Chốt UI 12/10/2026 (design.md § Thương hiệu theo khách) |
| P-mau-ma-quy-trinh | Mẫu mã quy trình: tiền tố, thành phần (chi nhánh, năm), số chữ số, chu kỳ đánh lại số | Mẫu mã | Cấu hình | `QT-[Mã chi nhánh]-[YY]-[XXXX]`, đánh lại theo năm | `QT-[Mã chi nhánh]-[YY]-[XXXX]`, đánh lại theo năm | Admin khách | Liên quy trình BR-004 | Chốt 12/10/2026 (cross-process-flow OQ-10) |
