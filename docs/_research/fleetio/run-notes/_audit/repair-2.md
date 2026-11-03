# Soát nhóm repair-2 (section 7265:363040, 15 màn)

Ảnh gốc rộng 756 đến 907 px, chữ nhỏ nên giờ phút và vài tiêu đề đọc không chắc. Không màn nào Khớp ngay hoàn toàn: mọi màn đều thiếu toast hoặc lệch nhỏ.

| Màn | Kết quả | Đã sửa gì | Còn lệch gì |
|---|---|---|---|
| 2.11 wo-completed | Đã sửa | Thêm 2 toast thiếu (Đồng bộ xe vào bộ lịch bảo dưỡng, Khôi phục dữ liệu lệnh #102); Hoàn thành thực tế 01:23 thành 01:21 (khớp thời lượng 2 phút) | Giờ bắt đầu 01:18 hay 01:19 không chắc; toast che mép phải dòng cuối của bảng như ảnh |
| 2.12 wo-reopen-confirm | Đã sửa | Thêm 2 toast; đồng bộ giờ hoàn thành 01:21 | Không |
| 2.13 wo-make-copy | Đã sửa | Bỏ hàng Số đồng hồ bắt đầu và Vô hiệu (ảnh không có); thêm Người phụ trách, Nhãn, Nhà cung cấp, Số hoá đơn, Số PO; checkbox "Dùng số đồng hồ bắt đầu" bỏ chọn + dòng mô tả; giờ ngày sự cố 13:27; thêm 4 toast; nới frame cao 2061, dời ảnh gốc xuống y 2181 | Giờ 13:27 đọc không chắc; các khối Sự cố, Dòng việc, Tổng hợp chi phí nằm dưới mép ảnh nên không soát được, giữ nguyên |
| 2.14 wo-complete-errors | Đã sửa | Nút Theo dõi thành Bỏ theo dõi (ảnh là Unwatch) | Ô Phụ tùng ghi "—" vì ảnh chỉ thấy "30.001.7" bị toast che; thiếu cụm avatar cạnh nút (chưa vẽ) |
| 2.15 wo-100x-after-save | Khớp | Không | Không |
| 2.16 wo-warranty-before | Đã sửa | Thêm toast thứ hai "Cập nhật lệnh sửa chữa thành công" | Không |
| 2.17 wo-warranty-opportunity | Khớp | Không | Không |
| 3.2 se-from-wo | Đã sửa | Thêm khối Sự cố đã xử lý (#35, #37 theo bảng đặc tả; ảnh đọc được số mờ), nút So sánh cạnh tiêu đề Dòng việc, 2 toast; giờ hoàn thành 01:21 | Tiêu đề hai sự cố trong khối không đọc được nên chỉ ghi mã; số #35/#37 lấy từ đặc tả, ảnh mờ (#87/#86?); số lệnh trong toast thứ hai (#103) không chắc |
| 3.3 se-deleted-not-found | Đã sửa | Thêm 3 toast | Số lệnh trong toast (#104, #103, #102 theo ảnh mờ) không chắc |
| 6.2 warranty-form | Đã sửa | Mẫu phạm vi bảo hành từ Disabled sang Placeholder "Vui lòng chọn"; thêm ô Đơn vị (Năm); bỏ ô Mã danh mục (ảnh chỉ có mô tả và nút) | Radio ảnh dạng thẻ nền xanh, Figma radio thường; ô Không giới hạn nằm dưới hàng, ảnh nằm cạnh Quãng đường |
| 6.3 warranty-new-vehicles | Đã sửa | Thêm toast "Lưu chi phí định kỳ" | Ô số đồng hồ chưa có hậu tố km |
| 6.4 warranty-new-template | Đã sửa | Thêm toast | Không |
| 6.5 warranty-new-standard | Đã sửa | Mô tả để trống (trước là "1"), Nhà sản xuất để trống (trước "50000"), Thời hạn "1", Quãng đường "50.000 km"; thêm mô tả phân loại bảo dưỡng; thêm toast | Không |
| 6.6 warranty-maintenance-codes | Đã sửa | Thêm toast | Nền sau lớp phủ còn ô Mã danh mục (không soát, nền bị che) |
| 6.7 warranty-list | Đã sửa | Thêm 2 toast (Lưu chi phí định kỳ, Đã tạo các bảo hành thành công) | Không |

Lỗi lặp lại: thiếu toast (11 màn); giá trị ô gõ nhầm chỗ (6.5); phần tử thêm ngoài ảnh (2.13, 6.2).
Ghi chú: không còn lỗi layoutAudit ngoài component (kiểm 2.13, 3.2, 6.2, 6.5, 2.16). Sidebar, Header không sửa. Không tạo section mới.
