# Soát location-2 (section 7265:374742, 15 màn)

| Màn | Kết quả | Đã sửa gì | Còn lệch gì |
|---|---|---|---|
| 3.2 jobs-board | Đã sửa | Trả thẻ BSA105TRNS, BSA106TRNS (cột cắt như ảnh); thêm toast "Đã tạo việc thành công" | Không có nút "..." ở đầu cột việc; ảnh xe trong thẻ là chữ XE |
| 3.3 job-add-modal | Khớp | - | - |
| 3.4 job-assign-modal | Đã sửa | Nền đúng ảnh: Chưa gán 2, thẻ TEST-XE-01 (đã chọn, Xe con) và TEST-XE-LOP (Xe đầu kéo); thanh lọc "1 Hành động" + "Xoá chọn" (ẩn Loại xe, Bộ lọc) | Chữ sau "Clear" bị modal che nên "Xoá chọn" là suy từ "Clear" |
| 3.5 job-assign-overlap-error | Đã sửa | Sửa nền như 3.4 | như 3.4 |
| 3.6 job-unassign-modal | Đã sửa | Chưa gán 24, trả thẻ 105, 106; cột 2 thêm thẻ TEST-XE-01 đã chọn + "Đang làm: 2 phút"; thanh lọc như 3.4 | Cột thứ 3 (tên kết thúc "...2-Tu-dong", đếm 0) chưa vẽ vì tên bị modal che |
| 3.7 job-detail | Khớp | - | Thiếu link "← Việc" trên tiêu đề (đã có breadcrumb); thiếu avatar xe trong bảng Gán việc; bản đồ là placeholder |
| 3.8 job-assignment-history | Khớp | - | Thiếu avatar xe trong cột Xe |
| 3.9 job-completed | Đã sửa | Thêm toast "Đã hoàn thành việc thành công" | như 3.7 |
| 3.10 jobs-board-geofence-chip | Đã sửa | Trả thẻ 105, 106; thêm toast hoàn tất tính tuân thủ | - |
| 3.11 job-history-auto-geofence | Đã sửa | Thêm toast | - |
| 4.1 automation-geofence-conditions | Đã sửa | Thêm nhãn "Tuỳ chọn" ở tiêu đề thanh bên; chân thanh bên lên sát nội dung (không còn dính đáy); thêm toast | Nút "Thêm điều kiện" dùng Primary tối thay vì xanh (theo quy ước) |
| 4.2 automation-geofence-saved | Đã sửa | Thêm "+ Thêm điều kiện", "+ Thêm hành động", dòng "Ngăn trùng bình luận: —"; thêm mô tả 2 hộp email; thêm toast | "Bật lúc" để `—` (ảnh mờ, không đọc được); giờ trong mô tả Email tóm tắt (ảnh mờ) bỏ không ghi |
| 4.4 vehicle-automation-comments | Đã sửa | Giờ báo cáo #31 là 7 giờ 5 phút; Đang mở 5; thêm dòng #42; địa chỉ Vị trí gần nhất; hàng Năm, Hãng xe, Mẫu xe, Phiên bản (—); tab "Nhắc gia hạn"; toast Lệnh sửa chữa #102; frame cao 1145 (Main, Sidebar 1145), dời ảnh gốc xuống y=4265 | Dòng sự cố thứ 3 (bị cắt, không đọc được) và nút "Xử lý" ở #42 chưa vẽ; khối Nhắc bảo dưỡng ảnh không thấy, để trống |
| 5.1 inspection-submission-location | Khớp | - | Ảnh cuộn, chỉ thấy nửa dưới; các dòng trên là `—` |
| 5.2 inspection-pretrip-simulated | Đã sửa | 3 dòng cuối (Gương nhìn sau, Đèn và phản quang, Phanh đỗ) thêm giá trị `—` | Giá trị 3 dòng đó bị toast che trong ảnh; không vẽ toast vì sẽ che nội dung |

Chưa chạy layoutAudit từng màn. Chụp lại 0.4 sau sửa: 3.2, 3.4, 3.5, 3.6, 3.9, 3.10, 4.1, 4.2, 4.4, 5.2 đều ổn.
