---
type: tenant-parameters
status: stale
status_prev: draft
status_changed: 2026-10-14
status_reason: "đã review upstream, không cần sửa"
updated: 2026-10-20
tenant_terms: [Delta, DK05, dGas, Nam Khánh, Phú Lợi, Pan Hải An]
links:
  - docs/_product/saas-core-vs-tenant.md
  - docs/service-delivery/brainstorms/service-delivery.md
  - docs/shipment-coordination/brainstorms/shipment-coordination.md
  - docs/transport-dispatch/brainstorms/transport-dispatch.md
  - docs/cross-process-flow/srs/cross-process-flow-spec.md
  - docs/account-access/brainstorms/account-access.md
---

# Tham số theo khách

Mỗi dòng là một chỗ mà khách khác có thể cần giá trị khác. Tài liệu nghiệp vụ ghi mã `P-…` kèm giá trị của khách trong ngoặc; phần mềm đọc giá trị từ cấu hình của từng khách.

Kiểu: **Số** (con số, khoảng thời gian, tỷ lệ) · **Danh sách** (các lựa chọn khách sửa được) · **Bật/tắt** (tính năng một khách dùng, một khách không).

| Mã | Tham số | Kiểu | Tầng | Mặc định sản phẩm | Delta | Ai sửa | Dùng ở | Nguồn |
|---|---|---|---|---|---|---|---|---|
| P-nguong-tam-ung | Hạn mức chi tiền mặt một khoản: nhân viên chỉ được trả bằng tiền cá nhân dưới ngưỡng; từ ngưỡng trở lên trả từ tài khoản công ty | Số (₫/khoản) | Cấu hình | chưa chốt | 5.000.000 ₫ (hạn mức chi tiền mặt, OQ-68) | Admin khách | Cung cấp dịch vụ E2 | Quy trình cung cấp dịch vụ tổng quát mục 4.6; Phân hệ APAS (17/10/2026) mục 3.3 |
| P-ca-truc-ngoai-gio | Khung giờ trực ngoài giờ; người trực có quyền tự giao việc trong ca | Số (giờ bắt đầu–kết thúc) | Cấu hình | chưa chốt | 17h30–8h | Admin khách | Điều phối B3b | Quy trình điều phối mục 4 |
| P-ban-giao-ca-truc | Bàn giao việc đang dở đầu ca, cuối ca trực | Bật/tắt | Cấu hình | bật | bật | Admin khách | Điều phối B3b | Trả lời Delta 10/10 (OQ-26) |
| P-ly-do-chuyen-viec | Lý do bắt buộc khi CS bấm "Chuyển việc" | Danh sách | Cấu hình | chưa chốt | Hết giờ làm việc · Khác (tự ghi) | Admin khách | Điều phối B2 | Trả lời Delta 10/10 (OQ-25) |
| P-so-nguoi-goi-y-nhan-viec | Số người phần mềm gợi ý khi giao việc hiện trường | Số (người) | Cấu hình | 3 | 2–3 | Admin khách | Điều phối B3a | Brainstorm Điều phối |
| P-gop-giao-viec-ha-vo | Gộp giao việc Lệnh hạ vỏ theo vận đơn + nơi hạ khi JobID có 1 container | Bật/tắt | Cấu hình | chưa chốt | bật | Admin khách | Điều phối B4 | Trả lời Delta 10/10 (OQ-27) |
| P-duyet-chi-ngoai-dinh-muc | Luồng xin duyệt khoản chi ngoài định mức trên app trước khi chi | Bật/tắt | Cấu hình | bật | tắt | Admin khách | Điều phối E1 | Trả lời Delta 10/10 (OQ-29) |
| P-theo-doi-tien-hoan-nang-vo | Theo dõi tiền nâng vỏ chờ hoàn, cảnh báo quá hạn | Bật/tắt | Cấu hình | bật | tắt | Admin khách | Điều phối B5 | Trả lời Delta 10/10 (OQ-28) |
| P-han-hoan-tien-nang-vo | Số ngày chờ tiền nâng vỏ hoàn trước khi cảnh báo | Số (ngày) | Cấu hình | 7 | không dùng (tắt) | Admin khách | Điều phối B5 | Giao nhận hàng hoá (18/9/2026) |
| P-duyet-chot-so-container | Chốt số container thực nhận cần cán bộ quản lý hiện trường duyệt | Bật/tắt | Cấu hình | bật | bật (chờ xác nhận OQ-71) | Admin khách | Điều phối B16 | Phỏng vấn Điều phối 21/10/2026 |
| P-han-duyet-dieu-phoi | Số giờ chờ duyệt chốt số container, việc phát sinh trước khi nhắc lại cán bộ quản lý hiện trường | Số (giờ) | Cấu hình | chưa chốt | chưa chốt (OQ-77) | Admin khách | Điều phối B16, B18 | Phỏng vấn Điều phối 21/10/2026 |
| P-hinh-thuc-ky-bien-ban | Cách khách ký biên bản giao hàng | Danh sách | Cấu hình | chưa chốt | Ký điện tử · Biên bản giấy (cả hai) | Admin khách | Điều phối A7 | Trả lời Delta 10/10, xác nhận 12/10 (OQ-20) |
| P-email-bien-ban-giao-hang | Tự email biên bản cho CS và khách khi lái xe xác nhận | Bật/tắt | Cấu hình | chưa chốt | bật | Admin khách | Điều phối A7 | Trả lời Delta 10/10 (OQ-20) |
| P-ty-le-chia-lai-noi-bo | Cách chia lợi nhuận giao dịch nội bộ giữa chi nhánh | Số (tỷ lệ + cơ sở chia) | Gói: Đa chi nhánh | chưa chốt | 50/50 theo lãi gộp, sau khi chốt bảng kê công nợ | Admin khách | Điều phối B7 | Trả lời Delta 10/10 (OQ-4) |
| P-gio-mien-phi-luu-xe | Số giờ lưu xe miễn phí trước khi tính phí lưu ca | Số (giờ) | Gói: CBT | chưa chốt | 72 giờ | Admin khách | Điều phối E8 | Giao nhận hàng hoá (18/9/2026); tự tính chờ OQ-33 |
| P-ky-chot-duong-sat | Ngày chốt kỳ Bảng kê đường sắt | Danh sách (ngày trong tháng) | Gói: Đường sắt | chưa chốt | ngày 25 · cuối tháng | Admin khách | Điều phối D7, E3 | Giao nhận hàng hoá (18/9/2026) |
| P-nguon-don-gia-duong-sat | Nguồn đơn giá đường sắt | Danh sách | Gói: Đường sắt | chưa chốt | CS nhập tay (giai đoạn 1); báo giá Sales (giai đoạn 2) | Admin khách | Điều phối E3 | Trả lời Delta 10/10 (OQ-30) |
| P-chu-ky-nhac-nhiet | Chu kỳ nhắc nhập nhật ký nhiệt độ, theo loại hàng lạnh | Số (giờ/lần, theo loại hàng) | Gói: Hàng lạnh | chưa chốt | chưa chốt (OQ-43) | Trưởng điều vận | Điều phối D2 | Giao nhận hàng hoá (18/9/2026) |
| P-thoi-gian-cho-nhan-viec | Bao lâu không bấm nhận thì việc quay về cán bộ quản lý | Số (phút) | Cấu hình | chưa chốt | chưa chốt (OQ-41) | Admin khách | Điều phối 6.4 | — |
| P-nhac-jobid-dung-cong-no | Sau bao lâu nhắc CS về JobID dừng vì công nợ | Số (ngày) | Cấu hình | chưa chốt | chưa chốt (OQ-42) | Admin khách | Điều phối 6.4 | — |
| P-logo | Logo và tên app hiện ở góc menu, màn đăng nhập, splash mobile, splash web | Tệp logo + tên hiển thị | Cấu hình | chữ cái đầu tên khách trên ô vuông | Đã nhận logo gốc 12/10/2026 (`design/brand/delta/delta-logo-goc.jpg`, jpg nền trắng; chờ bản nền trong) | Admin khách | Khung trang (menu, đăng nhập, splash) | Chốt UI 12/10/2026 (design.md § Thương hiệu theo khách, § Splash web) |
| P-mau-logo | Màu nền ô logo. Chỉ ô logo đổi màu; nút, menu, tab, link và màu trạng thái giữ trung tính | Mã màu | Cấu hình | #262626 | #1B7B46 (user chốt 13/10/2026) | Admin khách | Khung trang (menu, đăng nhập) | Chốt UI 12/10/2026 (design.md § Thương hiệu theo khách) |
| P-mau-ma-quy-trinh | Mẫu mã quy trình: tiền tố, thành phần (chi nhánh, năm), số chữ số, chu kỳ đánh lại số | Mẫu mã | Cấu hình | `QT-[Mã chi nhánh]-[YY]-[XXXX]`, đánh lại theo năm | `QT-[Mã chi nhánh]-[YY]-[XXXX]`, đánh lại theo năm | Admin khách | Liên quy trình BR-004 | Chốt 12/10/2026 (cross-process-flow OQ-10) |
| P-khoang-gps-toi-da | Khoảng hở tối đa giữa 2 điểm GPS liền nhau mà phần mềm còn dùng để kết luận xe qua hay tránh trạm vé | Số (giây hoặc mét) | Cấu hình | chưa chốt | chưa chốt (OQ-48) | Admin khách | Điều phối E10 | VIS mục 2.2.6 |
| P-dang-nhap-bang-sdt | Cho đăng nhập bằng số điện thoại ngoài tên tài khoản, email | Bật/tắt | Cấu hình | tắt | tắt | Admin khách | Tài khoản A1 | Phỏng vấn account-access 15/10 |
| P-so-lan-sai-mat-khau | Số lần nhập sai mật khẩu liên tiếp (chung web, app) thì tạm khoá | Số (lần) | Cấu hình | 5 | 5 | Admin khách | Tài khoản A2 | SRS Web tr.251 |
| P-thoi-gian-tam-khoa | Thời gian tạm khoá trước khi tự mở | Số (phút) | Cấu hình | 30 phút | 30 phút | Admin khách | Tài khoản A3 | Phỏng vấn account-access 15/10 |
| P-han-mat-khau-tam | Hiệu lực mật khẩu tạm của tài khoản mới hoặc được đặt lại | Số (giờ) | Cấu hình | 72 giờ | 72 giờ | Admin khách | Tài khoản A5 | Phỏng vấn account-access 15/10 |
| P-het-phien-khong-thao-tac | Web không ghi nhớ: hết phiên sau thời gian không thao tác | Số (giờ) | Cấu hình | 8 giờ | 8 giờ | Admin khách | Tài khoản A8 | Phỏng vấn account-access 15/10 |
| P-thoi-han-ghi-nho | Giữ phiên khi web chọn ghi nhớ; app giữ phiên tới khi không mở quá thời hạn | Số (ngày) | Cấu hình | 30 ngày | 30 ngày | Admin khách | Tài khoản A8 | Phỏng vấn account-access 15/10 |
| P-cho-gui-lai-ma | Thời gian chờ giữa 2 lần gửi link, mã OTP hoặc yêu cầu hỗ trợ | Số (giây) | Cấu hình | 60 giây | 60 giây | Admin khách | Tài khoản B1 | SRS Web tr.263 (cũ: 1 phút) |
| P-so-lan-gui-ma-moi-gio | Số lần gửi link, mã tối đa mỗi tài khoản trong 1 giờ | Số (lần) | Cấu hình | 5 | 5 | Admin khách | Tài khoản B1 | Phỏng vấn account-access 15/10 |
| P-han-ma-otp | Hiệu lực mã OTP đặt lại mật khẩu | Số (phút) | Cấu hình | 5 phút | 5 phút | Admin khách | Tài khoản B2 | SRS Mobile tr.57 |
| P-so-lan-sai-otp | Số lần nhập sai mã OTP tối đa | Số (lần) | Cấu hình | 5 | 5 | Admin khách | Tài khoản B2 | SRS Mobile tr.58 |
| P-email-ho-tro-mat-khau | Địa chỉ nhận yêu cầu Liên hệ IT khi quên mật khẩu | Danh sách (email) | Cấu hình | chưa chốt | it@delta.com.vn | Admin khách | Tài khoản B3 | SRS Web tr.263 |
| P-chinh-sach-mat-khau | Độ dài tối thiểu và loại ký tự bắt buộc của mật khẩu | Danh sách | Cấu hình | 8 ký tự, chữ thường, chữ hoa, số, ký tự đặc biệt | như mặc định | Admin khách | Tài khoản B4 | SRS Web tr.271 |
| P-so-ngay-lich-su-hoat-dong | Số ngày lịch sử hoạt động người dùng xem được | Số (ngày) | Cấu hình | 90 ngày | 90 ngày | Admin khách | Tài khoản D2 | Phỏng vấn account-access 15/10 |
| P-ngon-ngu-giao-dien | Ngôn ngữ giao diện cho chọn | Danh sách | Cấu hình | Tiếng Việt, Tiếng Anh | Tiếng Việt, Tiếng Anh | Admin khách | Tài khoản D3 | SRS Web tr.162 (bỏ tiếng Nhật) |
| P-huong-dan-cap-tai-khoan | Dòng hướng dẫn người chưa có tài khoản trên màn đăng nhập | Danh sách (nội dung) | Cấu hình | "Chưa có tài khoản? Liên hệ quản trị viên." | như mặc định | Admin khách | Tài khoản D5 | SRS Mobile tr.46 |
| P-han-link-dat-lai | Hiệu lực link đặt lại mật khẩu trên web | Số (phút) | Cấu hình | chưa chốt | 30 phút | Admin khách | Tài khoản B1 | SRS Web tr.264 |
| P-han-tao-mat-khau | Thời gian để lưu mật khẩu mới sau khi mở link hoặc nhập đúng mã đặt lại | Số (phút) | Cấu hình | 15 phút | 15 phút | Admin khách | Tài khoản BR-023 | Review SRS account-access 15/10 |
| P-van-toc-ket-xe | Vận tốc tối đa để xét kẹt xe khi máy nổ, xe vẫn nhích | Số (km/h) | Cấu hình | chưa chốt | 5 km/h (chờ xác nhận, transport-dispatch OQ-57) | Admin khách | Điều vận I3; Dữ liệu xe S2 | VIS mục 2.2.3 |
| P-thoi-gian-ket-xe | Kẹt liên tục bao lâu thì ghi kẹt xe | Số (phút) | Cấu hình | chưa chốt | 10 phút (chờ xác nhận, OQ-57) | Admin khách | Điều vận I3; Dữ liệu xe S2 | VIS mục 2.2.3 |
| P-thoi-gian-no-may-ngu | Máy nổ, xe đứng yên bao lâu thì ghi nổ máy ngủ | Số (phút) | Cấu hình | chưa chốt | 10 phút (chờ xác nhận, vehicle-telematics OQ-4) | Admin khách | Dữ liệu xe S3 | VIS mục 2.2.4 |
| P-khoang-dung-giua-ket-xe | Khoảng đứng yên tối đa giữa 2 đoạn kẹt xe mà vẫn tính là kẹt cứng | Số (phút) | Cấu hình | chưa chốt | chưa chốt (OQ-57) | Admin khách | Dữ liệu xe S4 | Phỏng vấn VIS 15/10 |
| P-lech-cung-duong-eta | Lệch so với cung đường bao nhiêu thì gọi lại dịch vụ bản đồ tính ETA | Số (%) | Cấu hình | chưa chốt | chưa chốt (VIS ghi "x%", OQ-57) | Admin khách | Điều vận I1 | VIS mục 2.2.1 |
| P-lech-km-gps-lenh | Km GPS lệch km cung đường trên Lệnh bao nhiêu thì báo người duyệt Lệnh | Số (%) | Cấu hình | chưa chốt | chưa chốt | Admin khách | Điều vận I9 | Review VIS v2 (20/10) |
| P-cung-dai-eta | Cung dài hơn mức này thì tính lại ETA định kỳ | Số (km) | Cấu hình | chưa chốt | 300 km | Admin khách | Điều vận I1 | VIS mục 2.2.1 |
| P-chu-ky-eta-cung-dai | Chu kỳ tính lại ETA cho cung dài | Số (phút) | Cấu hình | chưa chốt | 30 phút | Admin khách | Điều vận I1 | VIS mục 2.2.1 |
| P-quet-lai-vetc | Chờ bao lâu thì tra lại giao dịch thu phí cho trạm GPS đã qua mà chưa có giao dịch | Số (phút) | Cấu hình | chưa chốt | 120 phút | Admin khách | Điều vận I7 | VIS mục 3.1.3 |
| P-han-duyet-lenh | Lệnh hết chạy bao lâu chưa duyệt thì nhắc người duyệt, báo trưởng điều vận | Số (giờ) | Cấu hình | chưa chốt | chưa chốt (OQ-59) | Admin khách | Điều vận I13 | Review VIS r9 (19/10) |
| P-han-khieu-nai | Lái xe được khiếu nại một khoản trong bao nhiêu ngày từ lúc nhận thông báo | Số (ngày) | Cấu hình | chưa chốt | chưa chốt (OQ-60) | Admin khách | Điều vận I14 | Review VIS v4 (20/10) |
| P-quay-cat | Ghi nhận lượt quay cắt container tại nhà máy (vùng nhà máy, đầu kéo quay cắt khai trong danh mục địa điểm) | Bật/tắt | Cấu hình | tắt | bật | Admin khách | Điều vận Q1 | Camera AI (11/8/2026) mục 1, 3; GPS thay Camera AI (chốt 20/10) |
| P-quang-toi-thieu-quay-cat | Mooc đi dưới quãng này giữa ghép và tách thì không tính lượt quay cắt (móc thử) | Số (mét) | Cấu hình | chưa chốt | chưa chốt (OQ-61) | Admin khách | Điều vận Q2 | Camera AI (11/8/2026) mục 1, 3; GPS thay Camera AI (chốt 20/10) |
| P-gop-luot-quay-cat | Cùng mooc ghép, tách liên tiếp trong khoảng này thì gộp một lượt quay cắt | Số (phút) | Cấu hình | chưa chốt | chưa chốt (OQ-61) | Admin khách | Điều vận Q6 | Camera AI (11/8/2026) mục 1, 3; GPS thay Camera AI (chốt 20/10) |
| P-don-gia-luong-quay-cat | Đơn giá lương lái xe cho mỗi lượt quay cắt | Số (₫/lượt) | Cấu hình | chưa chốt | chưa chốt (OQ-62) | Admin khách | Điều vận Q5 | Camera AI (11/8/2026) mục 1, 3; GPS thay Camera AI (chốt 20/10) |
| P-dinh-muc-dau-quay-cat | Định mức dầu cho mỗi lượt quay cắt, cộng vào dầu chờ nhận (Gói Nhiên liệu) | Số (lít/lượt) | Gói: Nhiên liệu | chưa chốt | chưa chốt (OQ-62) | Admin khách | Điều vận Q5 | Camera AI (11/8/2026) mục 1, 3; GPS thay Camera AI (chốt 20/10) |
| P-chu-ky-doc-dau-tat-may | Chu kỳ đọc mức dầu khi xe tắt máy | Số (phút) | Cấu hình | chưa chốt | 30 phút (VIS mục 2.2 ghi 30–60, OQ-4) | Admin khách | Dữ liệu xe K1 | VIS mục 2.2, 3.5 |
| P-nguong-hut-dau | Dầu giảm bao nhiêu trong bao lâu thì nghi hút dầu | Số (lít trong phút) | Cấu hình | chưa chốt | 5 lít trong dưới 3 phút, dùng chung ngưỡng với EUP | Admin khách | Dữ liệu xe S7 | VIS mục 3.5 |
| P-nguong-do-dau | Dầu tăng bao nhiêu trong bao lâu thì ghi sự kiện đổ dầu | Số (lít trong phút) | Cấu hình | chưa chốt | 20 lít trong 10 phút, dùng chung ngưỡng với EUP | Admin khách | Dữ liệu xe S6 | VIS mục 3.6 |
| P-thoi-gian-o-bai-tim-vo | Xe ở bãi khác bao lâu thì tính là đi tìm vỏ | Số (phút) | Cấu hình | chưa chốt | 10 phút | Admin khách | Điều vận I5 | VIS mục 3.3 |
| P-khung-ghep-phieu-dau | Khung giờ ghép sự kiện đổ dầu với phiếu cấp dầu | Số (phút) | Cấu hình | chưa chốt | chưa chốt (vehicle-telematics OQ-13) | Admin khách | Cấp dầu (chưa lập) | Phỏng vấn VIS 15/10 |
| P-dung-sai-dau-thuc-do | Lệch bao nhiêu giữa lít cảm biến và lít thực bơm vẫn coi là khớp | Số (lít hoặc %) | Cấu hình | chưa chốt | chưa chốt (OQ-13) | Admin khách | Cấp dầu (chưa lập) | VIS mục 3.6 |
| P-dung-sai-day-binh | Thiếu bao nhiêu so với dung tích bình vẫn coi là đầy | Số (lít) | Cấu hình | chưa chốt | chưa chốt (OQ-13) | Admin khách | Cấp dầu (chưa lập) | Phỏng vấn VIS 15/10 |
| P-thoi-gian-on-dinh-cam-bien | Chờ bao lâu sau khi bơm mới đọc dầu tồn | Số (phút) | Cấu hình | chưa chốt | chưa chốt (OQ-13) | Admin khách | Cấp dầu (chưa lập) | Phỏng vấn VIS 15/10 |
| P-nguong-chay-ngoai-lenh | Xe không có Lệnh đi bao xa hoặc bao lâu thì cảnh báo | Số (km hoặc phút) | Cấu hình | chưa chốt | chưa chốt (vehicle-management OQ-3) | Admin khách | Dữ liệu xe S8; Quản lý phương tiện V2 | Phỏng vấn VIS 15/10 |
| P-han-xu-ly-su-viec | Hạn xử lý sự việc (hút dầu, chạy ngoài Lệnh, lệch dầu) trước khi nhắc, báo trưởng bộ phận | Số (ngày) | Cấu hình | chưa chốt | chưa chốt (OQ-4) | Admin khách | Dữ liệu xe X1 | Phỏng vấn VIS 15/10 |
| P-so-lan-loi-cam-bien | Số lần lỗi thiết bị trong kỳ thì báo kiểm tra thiết bị | Số (lần/kỳ) | Cấu hình | chưa chốt | chưa chốt (OQ-4) | Admin khách | Dữ liệu xe G2 | Phỏng vấn VIS 15/10 |
| P-thoi-gian-giu-gps | Giữ dữ liệu GPS thô bao lâu để tra ngược | Số (tháng) | Cấu hình | chưa chốt | chưa chốt (OQ-4) | Admin khách | Dữ liệu xe G5 | Phỏng vấn VIS 15/10 |
| P-giu-du-lieu-chua-khai | Giữ dữ liệu của thiết bị GPS chưa khai trên hồ sơ xe bao lâu để chờ khai | Số (ngày) | Cấu hình | chưa chốt | chưa chốt (OQ-16) | Admin khách | Dữ liệu xe G6 | Review VIS r10 (19/10) |
| P-mat-du-lieu-ca-doi | Cả đội xe không có dữ liệu bao lâu thì coi là nhà cung cấp ngừng gửi, báo Admin khách | Số (phút) | Cấu hình | chưa chốt | chưa chốt (OQ-16) | Admin khách | Dữ liệu xe G7 | Review VIS r10 (19/10) |
| P-qua-gio-ket-thuc-lenh | GPS hỏng: quá giờ kết thúc dự kiến bao lâu thì nhắc lái xe, điều vận | Số (phút) | Cấu hình | chưa chốt | chưa chốt (OQ-4) | Admin khách | Dữ liệu xe 6.5 | Phỏng vấn VIS 15/10 |
| P-nhac-tat-may | Nhắc lái xe tắt máy trên app khi nổ máy ngủ | Bật/tắt | Cấu hình | chưa chốt | chờ khách (vehicle-telematics OQ-5) | Admin khách | Dữ liệu xe S10 | Phỏng vấn VIS 15/10 |
| P-bu-dau-xep-hang | Bù dầu như kẹt xe khi xe xếp hàng chờ trong vùng cảng, bãi, kho mà máy vẫn nổ | Bật/tắt | Cấu hình | chưa chốt | chờ khách (transport-dispatch OQ-52) | Admin khách | Điều vận I4 | VIS mục 3.2 |
| P-tinh-tien-tranh-tram | Người duyệt Lệnh được chọn "Tính cho lái xe" với trạm tránh, ngoài cung đường | Bật/tắt | Cấu hình | chưa chốt | bật (review r14, 15/10/2026) | Admin khách | Điều vận I8 | VIS mục 2.2.6, 3.1.3 |
| P-chan-duyet-khi-con-tram | Còn trạm tránh, ngoài cung đường chưa xử lý thì chưa duyệt được Lệnh | Bật/tắt | Cấu hình | chưa chốt | bật (review r14, 15/10/2026) | Admin khách | Điều vận I8 | Phỏng vấn VIS 15/10 |
| P-cho-nhap-km-tay | Xe không có GPS: cho nhập tay km trên biên bản bàn giao, thu hồi (bắt ghi lý do) | Bật/tắt | Cấu hình | chưa chốt | tắt (km không sửa tay, review r15, 15/10/2026) | Admin khách | Quản lý phương tiện B4 | Phỏng vấn VIS 15/10 |
| P-dau-cho-nhan-vao-thuong | Dầu chờ nhận còn tồn khi thu hồi xe, lái xe nghỉ việc thì vào thưởng lương lái xe | Bật/tắt | Cấu hình | chưa chốt | bật (review r16, 15/10/2026) | Admin khách | Quản lý phương tiện B5; Cấp dầu | Phỏng vấn VIS 15/10 |
| P-duyet-tao-mat-hang | Mặt hàng, dịch vụ kỹ thuật mới và mọi thay đổi (sửa, ngừng dùng, dùng lại, xoá) phải qua duyệt mới có hiệu lực | Bật/tắt | Cấu hình | bật | bật | Admin khách | Danh mục hàng hoá A4; Dịch vụ kỹ thuật S1 | SRS Web tr.284 (Lưu đồ trạng thái chung cho danh mục) |
| P-don-vi-tinh | Đơn vị tính chọn được cho mặt hàng, dịch vụ | Danh sách | Cấu hình | cái, bộ, hộp, tấm, lít, mét, cuộn, lần | cái, bộ, hộp, tấm, lít, mét, cuộn, lần | Admin khách | Danh mục hàng hoá E1; Dịch vụ kỹ thuật S2 | SRS Web tr.301, 337, 372, 408, 440 |
| P-he-thong-tong-thanh | Hệ thống tổng thành xe (1 chữ số trong mã, tối đa 10 giá trị) | Danh sách | Cấu hình | 0 Không xác định, 1 Động cơ – làm mát, 2 Hệ thống truyền lực, 3 Hệ thống gầm, 4 Hệ thống điện, 5 Nhiên liệu – khí nạp, 6 Phụ và cabin | như mặc định | Admin khách | Danh mục hàng hoá E1, mã; Dịch vụ kỹ thuật S4 | SRS Web tr.301 |
| P-nhom-hang | Cây nhóm hàng; mỗi nhóm có cờ bắt buộc theo dõi serial và mã nhóm trong mã hàng (01 Lốp, 02 Ắc quy, cố định) | Danh sách | Cấu hình | Phụ tùng › Lốp, Ắc quy, Khác | Phụ tùng › Lốp (bắt buộc serial, mã 01), Ắc quy (bắt buộc serial, mã 02); nhóm khác chưa chốt | Admin khách | Danh mục hàng hoá A1, A14, A15 | SRS Web tr.406–408, 438–440; ISS-02 |
| P-loai-cong-cu-dung-cu | Loại công cụ dụng cụ (2 chữ số đầu mã công cụ) | Danh sách | Cấu hình | 01 Cầm tay, 02 Lớn | 01 Cầm tay, 02 Lớn | Admin khách | Danh mục hàng hoá E1, mã | SRS Web tr.372, 388 |
| P-nhom-xe-dich-vu-ky-thuat | Nhóm xe theo tải trọng trong mã dịch vụ kỹ thuật (2 chữ số; báo giá tra đơn giá theo nhóm) | Danh sách | Cấu hình | chưa chốt | 00 Khác (gồm xe nâng, máy phát điện), 01 Tải 1–5 tấn, 02 Tải trên 5–13 tấn, 03 Đầu kéo container, 04 Sơ mi rơ mooc | Admin khách | Dịch vụ kỹ thuật S4, S5 | SRS Web tr.319–320 |
| P-so-ngay-nhan-vua-thay-doi | Số ngày mặt hàng, dịch vụ hiện nhãn "Vừa thay đổi" sau khi đề xuất sửa được duyệt | Số (ngày) | Cấu hình | 7 | 7 | Admin khách | Danh mục hàng hoá C1 | Brainstorm danh mục hàng hoá (Vòng 2, 16/10) |
| P-loai-jobid | Bộ loại JobID: mã, tên, chứng từ định danh, ai tạo, mục phạm vi dịch vụ được chọn | Danh sách | Lõi, Cấu hình | chưa chốt | J01–J12 (`service-delivery` Mục 5.3) | Admin khách | Cung cấp dịch vụ B8, B9 | Quy trình cung cấp dịch vụ tổng quát mục 4.2.1, 4.9.1–4.9.2 |
| P-kenh-nhan-chung-tu | Kênh nhận chứng từ khách để phần mềm đọc và tạo JobID nháp | Danh sách | Cấu hình | tải lên app, web | Zalo OA, Telegram, WeChat, Gmail, tải lên app, web | Admin khách | Cung cấp dịch vụ A11 | Phân hệ APAS (17/10/2026) mục 2.2.1 |
| P-so-thang-binh-quan-han-muc | Số tháng gần nhất lấy bình quân doanh thu dịch vụ + phí trả hộ để tính hạn mức khi khách có nợ quá hạn | Số (tháng) | Cấu hình | chưa chốt | 6 | Admin khách | Cung cấp dịch vụ DP-01 | Quy trình cung cấp dịch vụ tổng quát mục 4.9.5 |
| P-cap-duyet-gia-han-no | Các bước duyệt yêu cầu gia hạn nợ quá hạn | Danh sách | Cấu hình | chưa chốt | Cán bộ quản lý → Ban giám đốc | Admin khách | Cung cấp dịch vụ B13 | Quy trình cung cấp dịch vụ tổng quát mục 4.9.4 |
| P-so-ngay-gia-han-no-toi-da | Số ngày tối đa một lần gia hạn nợ quá hạn | Số (ngày) | Cấu hình | chưa chốt | chưa chốt (OQ-67) | Admin khách | Cung cấp dịch vụ B13 | Quy trình cung cấp dịch vụ tổng quát mục 4.9.4 |
| P-tien-te-thanh-toan | Tiền tệ khách được thanh toán phí dịch vụ | Danh sách | Cấu hình | VND | VND, USD | Admin khách | Cung cấp dịch vụ D11 | Giao nhận hàng hoá (18/9/2026) mục 3.4.1.1 |
| P-nhan-tien-mat-phi-dich-vu | Nhận thanh toán phí dịch vụ bằng tiền mặt | Bật/tắt | Cấu hình | chưa chốt | tắt | Admin khách | Cung cấp dịch vụ D11 | Giao nhận hàng hoá (18/9/2026) mục 3.4.1.1 |
| P-ky-bao-cao | Độ dài kỳ báo cáo nội bộ (kỳ hạch toán) mà doanh thu, chi phí JobID hoàn thành được ghi vào | Số (kỳ) | Lõi, Cấu hình | tháng | tháng (00:00 ngày đầu – 24:00 ngày cuối) | Admin khách | Cung cấp dịch vụ E18 | Quy trình cung cấp dịch vụ tổng quát mục 4.9.3 |
| P-thoi-gian-luu-chung-tu | Thời gian giữ chứng từ kế toán, thuế, hải quan trên hệ thống | Số (năm) | Cấu hình | chưa chốt | 10 năm | Admin khách | PRD 9.1 | Phần mềm Delta 3.0 (16/10/2026) mục 6.2 |
| P-thoi-gian-luu-log | Thời gian giữ log hệ thống và log gọi AI | Số (tháng) | Cấu hình | chưa chốt | 6 tháng | Admin khách | PRD 9.1 | Phần mềm Delta 3.0 (16/10/2026) mục 6.2 |
| P-gioi-han-luot-goi-ai | Số lượt gọi AI tối đa cho một tác vụ, vượt thì ngắt và chuyển làm tay | Số (lượt) | Cấu hình | chưa chốt | 10 | Admin khách | PRD 9.1 | Phần mềm Delta 3.0 (16/10/2026) mục 7.5 |
| P-gioi-han-thoi-gian-tac-vu-ai | Thời gian chạy tối đa của một tác vụ AI, vượt thì ngắt và chuyển làm tay | Số (phút) | Cấu hình | chưa chốt | 3 phút | Admin khách | PRD 9.1 | Phần mềm Delta 3.0 (16/10/2026) mục 7.5 |
| P-quy-tac-ghep-mooc | Mức ghép (Được, Cảnh báo, Chặn, Cần hỏi) cho từng loại mooc × cấu hình container (rỗng, 1×20, 2×20, 1×40, 1×45) khi xếp tổ hợp | Bảng | Lõi, Cấu hình | theo `design/v2/vehicles.md` mục 5.1 | chưa chốt (OQ-66, OQ-67 Điều phối) | Admin khách | Điều phối F10 | lab-combo (11/10/2026), DEC-267 |
