# Soát nhóm vehicle + saas đợt đầu (section 7226:264416, 7226:268050, 11 màn)

| Màn | Kết quả | Đã sửa gì | Còn lệch gì |
|---|---|---|---|
| 1.1 vehicle-detail (7224:248722) | Khớp | - | Thiếu nút icon cảm biến cạnh Theo dõi (nhỏ); cột Bình luận chỉ có rãnh nút theo quy ước; ô Nhắc bảo dưỡng ghi `—` vì ảnh cắt |
| 2.1 assignments (7226:252545) | Khớp | - | Thiếu chip "Tìm hiểu"/mũi tên cạnh tiêu đề và nút icon bật cột phải (chrome); popup Learn không vẽ; vạch giờ hiện tại đã là đỏ đúng |
| 3.1 meter-history (7224:249518) | Đã sửa | Thêm cột checkbox (header + 7 dòng) | Thiếu mũi tên sắp xếp ở cột Ngày ghi số |
| 4.1 tire-readings (7226:258364) | Khớp | - | - |
| 5.1 expense-new (7226:259805) | Đã sửa | Ô Số tiền bỏ giá trị mẫu "0", bỏ chevron (ảnh để trống, chỉ có ₫) | Ký hiệu ₫ ở cuối ô, ảnh ở đầu ô |
| 6.1 replacement (7226:261671) | Khớp | Không đổi gì | Vạch thay tối ưu hiện cam đỏ nét đứt, ảnh nét chấm: chưa xác nhận; năm 7, 8 và Giá trị thanh lý ảnh không đọc được, giữ `—`/bỏ |
| 1.1 dashboard (7224:245711) | Khớp | - | 3 thẻ (Tất cả mã lỗi, Nhắc gia hạn xe, Nhắc gia hạn liên hệ): ảnh chỉ thấy đỉnh chữ số, không đọc được, giữ `—`; việc làm quen dùng ô vuông, ảnh là vòng tròn trạng thái |
| 2.1 reports (7224:247155) | Đã sửa | Thêm 2 thẻ hàng 4: Lịch kiểm tra, Danh sách sự cố (mô tả Lịch kiểm tra bị cắt trong ảnh, viết theo phần thấy); lưới tự giãn | Thẻ bị popup che nên không có nhãn nhóm; nút Lưới giữ kiểu chọn (là nút đang chọn của bộ chuyển Lưới/Danh sách) |
| 3.1 automation-builder (7226:251840) | Khớp | - | - |
| 4.1 maintenance-settings (7226:254170) | Đã sửa | Số lệnh tiếp theo 101 thành 106, gợi ý "cao nhất 105" (theo ảnh và run-notes repair); ẩn nút Lưu (ảnh không có); mục 4 thành "Bắt buộc danh mục trên dòng việc" kèm mô tả, mục 5 "Tắt sửa lý do sửa chữa mặc định..." kèm mô tả, mục 6 "Tắt sửa mã danh mục mặc định (Hệ thống, Cụm, Bộ phận)..." không mô tả; ẩn nhóm Phàn nàn/nguyên nhân/khắc phục và khối Phụ trội (ảnh không có); menu Cài đặt thêm tiêu đề "Kiểm tra" và 3 mục Vị trí/Danh mục/Nhà sản xuất phụ tùng | Chữ ảnh mờ, số 106/105 đọc từ ảnh kèm ghi chú SRS; frame vẫn cao 1393 (còn trống phía dưới); mục "Task Reminder Types" đầu menu bị cắt trong ảnh |
| 4.2 record-sets (7226:259013) | Đã sửa | Thêm checkbox chọn tất cả ở header, biểu tượng khoá đầu mỗi dòng (căn lại cột Tên) | Nhóm "Developer" cuối menu chỉ thấy tiêu đề, không vẽ |

Số liệu: 6 Khớp ngay, 5 Đã sửa (meter-history, expense-new, reports, maintenance-settings, record-sets). Không đổi chiều cao frame nào nên không phải dời nhóm ảnh gốc.
Loại lỗi lặp: thiếu cột checkbox ở bảng, dòng/thẻ cuối bị bỏ khi ảnh cuộn dài, mục suy đoán không có trong ảnh (maintenance), giá trị mẫu trong ô nhập.
