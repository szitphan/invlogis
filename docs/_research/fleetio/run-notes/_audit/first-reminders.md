# Soát nhóm first-reminders (9 màn)

| Màn | Kết quả | Đã sửa gì | Còn lệch gì |
|---|---|---|---|
| 1.1 reminders-list 7224:242810 | Đã sửa | Thêm nút `Thêm` (ảnh có nút "...") cạnh Thêm nhắc bảo dưỡng, id 7280:411261 | Dòng 6-9 bị popup che nên không vẽ (theo quy ước) |
| 1.2 program-new 7226:255910 | Khớp | — | — |
| 1.3 renewals-list 7224:243686 | Đã sửa | Thêm nút `Thêm` ("..."), id 7280:411268 | — |
| 1.4 reminder-new 7226:250333 | Khớp | — | Cột Xem trước lịch do người vẽ tự đặt (đã biết, giữ); ảnh để trống |
| 2.1 inspection-form 7226:257694 | Đã sửa | Nút Sửa của khối Mục kiểm tra đổi Primary sang Tertiary (ảnh là liên kết xanh có bút chì, không có nút đặc) | Chỉ 3/23 mục vì ảnh chỉ thấy vậy (đã biết, giữ) |
| 2.2 inspection-items-edit 7226:261139 | Khớp | — | 10 mục theo ảnh (đã biết) |
| 2.3 inspection-submission 7226:264639 | Đã sửa | Nút In đổi Primary sang Secondary (ảnh: Print nền trắng viền) | — |
| 2.4 item-failures 7224:244480 | Đã sửa | Thêm nút `Thêm` ("..."), id 7280:411275 | — |
| 2.5 inspection-schedules 7224:245062 | Đã sửa | Thêm nút `Thêm` ("..."), id 7280:411282 | — |

Đã kiểm: ngày mm/dd sang dd/mm đúng (1.1, 1.3, 2.3, 2.4, 2.5), 6:14pm sang 18:14 đúng, không có ô nhập trống dù ảnh có giá trị, đủ dòng khối Thông tin, checkbox/radio đúng loại.
Không đổi kích thước frame nên không phải dời nhóm ảnh gốc. Chưa chạy layoutAudit, chỉ soát bằng ảnh chụp.
Ghi chú: 2.1 và 2.3 giờ không còn nút Primary vì ảnh gốc không có nút đặc. Tên layer vài nút còn tiếng Anh (Add Service Reminder, Start Inspection), chưa đổi.
