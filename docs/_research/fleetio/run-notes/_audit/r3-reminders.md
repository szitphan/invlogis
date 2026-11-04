# Soát nhóm reminders / inspection (lượt 3-5, 22 màn)

Section 7332:455253 (18 màn, lượt 3-4) và 7332:464302 (4 màn, lượt 5). Soát từng màn với ảnh gốc, chụp scale 0.5 đến 1.

| Màn | Kết quả | Đã sửa gì | Còn lệch gì |
|---|---|---|---|
| 2.19 inspection-form-smart-upload-review | Khớp | Không | Ảnh: ô Mô tả nền xám, ô Màu có icon cấm, thanh PDF nhiều nút; bản vẽ đơn giản hoá. Mục kiểm tra thứ 3 trở đi ngoài khung ảnh |
| 2.15 inspection-form-vehicles | Khớp | Không | Chip Form Status tô xanh (đang lọc) và avatar xe CAR chưa có |
| 2.21 inspection-inventory-adjustment-deduct | Khớp | Không | Ngày 11/03/2026 5:56pm đã đổi đúng 03/11/2026 17:56. Ảnh có panel Bình luận mở, bản vẽ theo quy ước rãnh nút |
| 2.17 inspection-photo-webcam-only | Khớp | Không | Thiếu icon camera và icon webcam tắt trong popup (nút X thay bằng chữ Đóng) |
| 2.16 inspection-schedule-due-soon | Đã sửa | Tab đang chọn là "Tất cả" (ảnh), bản vẽ chọn "Sắp đến hạn": đổi lại | Vạch cam bên trái hàng, chấm trạng thái xanh avatar xe, dấu tick Đặt tay thay bằng chữ "Có" |
| 2.6 inspection-submit-form | Khớp | Không | Ảnh có con trỏ chuột, viền ô Xe xanh (focus) |
| 2.14 inspection-workflow-add | Đã sửa | Thêm icon vào 3 thẻ điều kiện (circle-check, circle-x, clipboard-check) | Chấm số bước 1, 2 ảnh là hình tròn xám đậm |
| 2.20 inspection-workflow-fail-issues | Khớp | Không | Ảnh có panel Bình luận mở, avatar xe SEM, toast không có |
| 1.10 program-vehicles-add | Đã sửa | Bỏ 4 nhãn trường tự thêm (Số đồng hồ chính, Toán tử, Đơn vị, Điều kiện 2): ảnh không có nhãn | Hàng đầu ảnh là 3 ô xám (vô hiệu) kèm icon khoá; bản vẽ ô thường. Menu bên đánh dấu Nhắc việc, ảnh đánh dấu Bộ lịch (menu 13 mục, thuộc agent Sidebar) |
| 1.17 reminder-compliance-km-boundary | Khớp | Không | Ảnh mờ: Hạn kế tiếp, cột Hạn/Hoàn thành giữ `—` |
| 1.14 reminder-compliance-multi | Khớp | Không | Ngày Oct 11 / 01/19/2027 đã đổi dd/mm. Avatar xe, người vận hành chưa có |
| 1.5 reminder-detail-overdue | Khớp | Không | Dòng cuối khối Thông tin ngoài khung ảnh. Avatar xe, toán tử chưa có |
| 1.12 reminder-draft-work-order | Đã sửa | Ẩn 3 dòng chữ mẫu "Mô tả ngắn giải thích lựa chọn này." dưới đầu việc (ảnh không có) | Icon cảnh báo trước dòng "Giải quyết…", mũi tên bung ở cuối dòng |
| 1.13 reminder-record-history | Khớp | Không | Giờ 12:18pm=12:18, 1:07am=01:07, 12:59am=00:59 đều đúng. Ảnh: icon tìm cạnh ô, dùng chữ Tìm |
| 1.9 reminder-resolve | Đã sửa | Menu Xử lý dời xuống y=130, không còn đè hàng nút (ảnh menu nằm dưới nút Xử lý) | Icon bên phải từng mục menu chưa có |
| 1.8 reminder-snooze | Khớp | Không | Ngày 11/10/2026 (Mỹ) = 10/11/2026 đúng; 12:17pm = 12:17 |
| 1.11 renewal-new | Khớp | Không | Ngày 11/03/2026 = 03/11/2026 đúng |
| 1.16 service-smart-upload-review | Khớp | Không | Số tiền ảnh dạng "50,00 ₫" bản vẽ "50 ₫". Toast hai cái cách nhau rộng hơn ảnh |
| 1.19 reminder-forecast-next-due-popover | Đã sửa | Chuyển "Đã bật dự báo" lên góc phải khối (ảnh) | Bốn hàng đầu bảng (BSA110TRNS, BSA103TRNS, BSA109TRNS, TEST-NHAC-E) bị popup che cột Trạng thái, Hạn kế tiếp nên bỏ. Banner quảng bá tên công ty thật: không vẽ. Toast "Khôi phục Lệnh sửa chữa #106" chưa vẽ. Tag "Sample" của Fleetio bỏ |
| 1.20 reminder-forecast-meter-popover | Đã sửa | Chuyển "Đã bật dự báo" lên góc phải khối Đến hạn kế tiếp | Phần dưới popup Dự báo đồng hồ ngoài khung ảnh. Toast chưa vẽ |
| 1.21 reminder-forecast-group-week | Khớp | Không đổi | Bảng trong khung: Content 1035 cao, bảng 666 cao, rộng 1192 trong 1616 (không tràn; audit layout chỉ báo lỗi trong Sidebar, Header). Ảnh cuộn ngang còn các cột Đã gán lúc, bản vẽ bỏ; cột Ngày hoàn thành. Toast, tag Sample chưa vẽ |
| 1.22 reminder-forecast-not-available | Đã sửa | Chuyển "Đã bật dự báo" lên góc phải khối | Giá trị Đồng hồ chính bị tooltip che, giữ "Không có dự báo, còn 461 km" (461 khớp ảnh). Toast chưa vẽ |

## a11y_audit (figma_read op a11y_audit)

Chạy trên 5 màn đại diện (2.19, 2.15, 1.10, 1.21, 1.22). 17 màn còn lại chưa chạy riêng: cùng component nên lỗi lặp lại.
- nontext-contrast: nút Secondary (Thêm, Sửa, Bộ lọc, Nhóm, Theo dõi...) viền 1.09:1, cần 3:1. Lỗi ở component Button, không sửa ngoài component.
- target-size: Checkbox, Radio 16x16 dưới 24 (component).
- text-contrast: nhãn Radio vô hiệu 2.31:1 (component Radio, trạng thái vô hiệu).
- Không có lỗi nào nằm ngoài component để sửa.

## Lỗi lặp lại

Chữ mẫu / nhãn tự thêm trong component (2 màn); tab chọn sai (1); lệch vị trí khối nhỏ (menu, dòng "Đã bật dự báo"); toast và tag "Sample" chưa vẽ ở nhóm forecast; avatar xe CAR/SEM và dấu tick/chấm trạng thái thường thiếu.
