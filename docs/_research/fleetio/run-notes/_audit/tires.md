# Soát nhóm tires (section 7265:374144, 19 màn)

| Màn | Kết quả | Đã sửa gì | Còn lệch gì |
|---|---|---|---|
| 1.1 tire-management-empty | Khớp | | 6 ô sơ đồ trục đúng |
| 1.2 axle-setup-step1 | Khớp | | Ô avatar nhỏ cạnh tên xe trống (ảnh có chữ SEM), nhẹ |
| 1.3 axle-setup-axle-type | Khớp | | Như 1.2 |
| 1.4 axle-setup-known | Khớp | | |
| 1.5 axle-config-options | Khớp | | |
| 1.6 tire-management-6x4 | Khớp | | Sơ đồ đúng vị trí, tên ô, Lái/Dẫn động |
| 1.7 tire-management-trailer | Đã sửa | Ẩn badge "0" cạnh "Lốp đã lắp" (ảnh không có); thêm icon bánh răng ở trạng thái rỗng | |
| 2.1 tire-install | Đã sửa | Xoá toast "Đã cập nhật cấu hình trục" (ảnh không có toast) | |
| 2.2 tire-management-installed | Khớp | | Sơ đồ đúng: LF/RF 12/32 110, hàng 2 14/32 100, hàng 3 3/32 đỏ 60 |
| 2.3 tire-edit | Khớp | | |
| 2.4 tire-management-trailer-12-spare | Đã sửa | Thêm tab "Nhắc gia hạn" (ảnh có Renewal Reminders) | Giá trị sơ đồ đọc từ ảnh 907px nên không chắc: 2LO "5/32" màu cam trong khi 1LO "5/32" đỏ (danh sách bên phải ghi 2LO = 5), 3LO có thể là 10 hoặc 16. Màu từng ô khớp ảnh. 4 toast nền "Complete: ..." của Fleetio chưa vẽ (không liên quan lốp) |
| 3.1 tire-rotate | Khớp | | Ô thumbnail lốp là ô xám trống (ảnh có icon) |
| 3.2 tire-rotate-result-undo | Khớp | | Ảnh cuộn xuống cuối danh sách, Figma hiện đầu danh sách; đủ 10 dòng |
| 3.3 tire-rotate-name-required | Đã sửa | Chip số km dòng 2LI đổi "0 km" thành "—" (ảnh bị cắt, chữ chip dài hơn "0 km") | Chỉ có 6 dòng, ảnh cắt ở 2LI nên không vẽ thêm |
| 4.1 tire-remove | Khớp | | Nền sơ đồ còn trạng thái trước đảo (ảnh nền đã đảo), bị lớp phủ che |
| 5.2 tire-readings-data | Khớp | | |
| 5.3 tire-readings-filter-warning | Khớp | | Cột bên phải ảnh bị cắt, để "—" |
| 5.4 tire-readings-boundary | Đã sửa | Nới cột Xe 165, Cách đọc 170, Tuổi thọ 90 (hết xuống dòng "Kiểm tra #126051306", "100.000 km", tên xe bị cắt); hạ Ngày đọc/Ngày lắp 120, Mã 90 | Toast "Complete: Calculating Service Reminders..." che 2 dòng ảnh, chưa vẽ |
| 5.5 tire-activity | Đã sửa | Sửa 8 dòng đảo lốp sai vị trí đích (vd 3RO > 2RI, không phải 3RO > 3RI); cột Ngày lắp của 3 dòng "Đã lắp" từ "—" thành 03/11/2026 | |

Tổng: 13 khớp ngay, 6 đã sửa. Lỗi lặp: toast thừa/thiếu, chữ xuống dòng do cột hẹp, dữ liệu dòng đảo chép sai.
