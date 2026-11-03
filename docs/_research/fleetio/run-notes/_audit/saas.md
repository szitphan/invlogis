# Soát nhóm saas (section 7271:385568, 15 màn)

| Màn | Kết quả | Đã sửa gì | Còn lệch gì |
|---|---|---|---|
| 2.2 report-issues (7261:354030) | Khớp | - | Toast che dòng bảng nên không vẽ; ô Hạn/Người phụ trách ghi `—` trong khi ảnh để trống (chấp nhận) |
| 2.3 ai-analyst-issues (7265:361946) | Đã sửa | Thêm liên kết "Quay lại" (thu Thân 44px để vừa khung) | Thiếu 2 nút icon nhỏ (bảng/biểu đồ, phóng to) trên khối kết quả |
| 3.2 automation-templates (7265:365962) | Khớp | - | Toast che hộp thoại nên không vẽ |
| 3.3 automation-list-data (7265:365199) | Đã sửa | Thêm 4 toast (1 Đang xử lý + 3 Hoàn tất) | - |
| 3.4 automation-detail (7265:368281) | Đã sửa | Thêm dòng "Tạo bởi ... · Cập nhật ..." cuối trang; thêm toast | - |
| 3.5 automation-run-history (7265:369280) | Đã sửa | Nền đổi sang đúng tự động hoá Geofence: Đang bật (badge xanh, công tắc bật), Bật lúc 03/11/2026 01:19, Bản ghi kích hoạt Sự kiện vùng địa lý, v.1, Tạo lúc 01:19, lượt chạy 2/2/0, hoạt động "1 phút trước", dòng cuối trang; thêm 2 toast | Phần Tóm tắt các bước phía sau hộp thoại vẫn là nội dung AUTO-01 (ảnh gốc bị che, đọc không ra) |
| 3.6 automation-run-result (7265:371635) | Đã sửa | Nền AUTO-01 Đang bật, Bật lúc 01:19, Tạo lúc 01:18, lượt chạy 1/1/0, thêm dòng Hoạt động "cập nhật" (false sang true, phiên bản trống sang 1), dòng cuối trang, 2 toast | Thời gian dòng Hoạt động thứ hai ghi `—` (bị toast che trong ảnh) |
| 3.7 automation-self-trigger-runs (7265:372278) | Đã sửa | Nền AUTO-02 Đang bật, Bật lúc/Tạo lúc 01:22, v.1, lượt chạy 2/2/0, 2 dòng Hoạt động, dòng cuối trang, 3 toast | Thời gian 2 dòng Hoạt động ghi `—` (bị toast che) |
| 3.8 automation-archived (7265:374145) | Đã sửa | Đưa dải "Bản ghi này đã được lưu trữ" xuống dưới tiêu đề (đúng thứ tự ảnh); ẩn chip Đã tắt, công tắc, nút Thêm/Sửa (ảnh không có); thêm link "Xem lịch sử" ở Phiên bản hiện tại; Hoạt động thành 2 dòng "cập nhật" (true sang false); dòng cuối trang | Thời gian Hoạt động `—`, chi tiết dòng 2 `—` (ảnh bị toast che/cắt); toast che ô Thất bại nên không vẽ |
| 3.9 automation-comment-result (7265:374743) | Đã sửa | Thêm dòng "Tạo vài giây trước · Cập nhật vài giây trước" | - |
| 4.3 record-set-conditions (7265:376229) | Đã sửa | Ẩn mục "Xuất dữ liệu tài khoản" và "Kết nối SAML" (ảnh không có); thêm toast. Ô Mô tả giữ ô nhập thường (đã biết) | Nền Cài đặt đang có thêm sidebar chính bên trái (ảnh thay bằng menu Cài đặt), thuộc phạm vi Sidebar nên không đụng |
| 5.1 contact-no-access (7265:377978) | Khớp | - | - |
| 5.3 recalls-list (7265:379764) | Đã sửa | Thêm cột checkbox (header + dòng); thêm 4 dòng (10/09/2025 D2582; 10/09/2025 F1023; 25/04/2023 FL871 23V298000; 01/11/2022 FL858 22V817000) | Ảnh rất mờ: ngày các dòng 1-10 chưa chắc chắn (đã thử phóng 2x, chỉ đọc được gần đúng); biển xe dòng 11-12 ghi `—`; dòng 13-16 trong ảnh không đọc được và bị popup che nên không thêm; mã chiến dịch dòng 12 (FL858) đọc gần đúng |
| 5.4 motor-pool-reservations (7270:382171) | Khớp | - | - |
| 5.5 documents-empty (7270:382767) | Khớp | - | - |

Loại lỗi lặp: nền hộp thoại chép từ màn khác (3.5-3.7), thiếu dòng "Tạo bởi/Cập nhật" cuối trang, thiếu toast không che nội dung, phần tử tự thêm (3.8, 4.3).
Chưa soát bằng số đo pixel: chỉ so bằng mắt qua ảnh chụp 0.4-0.5; toast Complete dùng chung 1 mẫu (icon vòng tròn dấu tích, Đang xử lý đổi sang màu info).
