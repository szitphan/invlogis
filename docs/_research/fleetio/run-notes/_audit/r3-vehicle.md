# Soát r3 · Phương tiện lượt 3-4 (10 màn)

| Màn | Kết quả | Đã sửa | Còn lệch |
|---|---|---|---|
| 3.6 meter-bulk-void-secondary (7332:446554) | Đã sửa | Chữ "Số đồng hồ hiện tại", "Số giờ hiện tại" đỏ sang xám (ảnh xám); thêm cờ đỏ dòng 4.928 km | Ảnh chỉ thấy 12/17 dòng, 5 dòng cuối không có trong ảnh |
| 3.5 meter-out-of-sequence-autovoid (7332:449760) | Đã sửa | Thêm cờ đỏ dòng 2.499 km | Ô Nguồn dòng bị che (ảnh làm mờ), để "—" |
| 1.7 trailer-linked-two-vehicles (7332:443269) | Đã sửa | Ô ảnh xe "XE CON" thành "RƠ MOÓC" | Ảnh có cột Bình luận mở (trạng thái rỗng), màn chỉ có rãnh nút; ảnh cuộn giữa trang, màn từ đầu trang |
| 1.8 vehicle-add-multiple-step1 (7332:452886) | Đã sửa | Điền 3 dòng dữ liệu vào ô dán (004/022/437 + VIN + thành phố) | Thiếu mũi tên ">" giữa 2 bước (chrome nhỏ) |
| 1.6 vehicle-archive-confirm (7332:417298) | Đã sửa | Thêm nút đóng X | Không |
| 1.11 vehicle-attach-shared-document (7332:441823) | Đã sửa | Thêm nút X; ô ảnh "XE CON" thành "ĐẦU KÉO" | Nền: ảnh là trang Bộ lịch bảo dưỡng rỗng + cột Bình luận; màn là chi tiết xe, tab Nhắc bảo dưỡng (cùng cấu trúc, lệch nhẹ) |
| 1.9 vehicle-manage-overview-layout (7332:424383) | Đã sửa | Thêm nút X | Nút bỏ thẻ là "×" đúng |
| 1.10 vehicle-service-programs-empty (7332:439301) | Đã sửa | Ô ảnh "XE CON" thành "ĐẦU KÉO" | Thiếu hình minh hoạ cờ lê trên khối rỗng, cột Bình luận mở, tooltip "Thêm hành động" (bỏ) |
| 1.5 vehicle-status-history (7332:420487) | Khớp | Không | Không (5 dòng, giờ, thời lượng, màu chấm đều đúng) |
| 1.4 vin-decode-review (7332:436930) | Đã sửa | Thêm nút X; 11 ô "-" tăng tương phản | Nền: ảnh là form Sửa xe (menu Chi tiết/Bảo dưỡng/Vòng đời...), màn là trang chi tiết xe. Còn lệch, không rẻ để sửa |

## a11y_audit (từng màn)
Lỗi nằm trong component hoặc chrome Fleetio, không sửa:
- Viền nút Secondary 1.09:1 (nontext-contrast, 1.4.11): cả 10 màn (Theo dõi/Thêm/Sửa, Huỷ, Đóng, Tạo bộ lịch, ô lọc bảng).
- Link kích thước 20px dưới 24px (2.5.8): Sửa nhãn, Xem tất cả, Thêm sự cố, Thêm nhắc bảo dưỡng, Tuỳ chỉnh bố cục (7 màn chi tiết).
- Checkbox 16px (2.5.8): màn manage-overview và vin-decode (component Checkbox).
- Nhãn nút Primary disabled 2.31:1 (attach-shared-document, manage-overview): đúng trạng thái disabled như ảnh.
- trailer-linked: "✓" 4.12:1 (7332:444127), chưa sửa.
- Nút X vừa thêm 20x20 (review, 2.5.8): giống Fleetio, để nguyên.
Đã sửa: 11 ô "-" ở vin-decode (4.22:1 sang text/secondary).

## Loại lỗi lặp lại
- Hộp thoại thiếu nút X đóng (4/5 hộp thoại).
- Ô ảnh xe ghi "XE CON" cho mọi loại xe (ảnh: CAR/SEM/TRA).
- Chữ phụ đỏ thay vì xám; thiếu cờ đỏ.
- Nền sau lớp phủ không đúng cấu trúc (vin-decode, attach-shared-document).
