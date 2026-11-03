# Soát nhóm vehicle và reminders (20 màn)

Section 7261:351361 (13 màn) và 7265:380586 (7 màn). Soát từng màn với ảnh gốc, chụp scale 0.4 đến 0.8.

| Màn | Kết quả | Đã sửa gì | Còn lệch gì |
|---|---|---|---|
| 1.2 vehicle-more-actions | Khớp | Không | Phần thân dưới menu ngoài khung ảnh, không so được |
| 1.3 vehicle-cost-of-ownership | Đã sửa | Cột biểu đồ dựng lại: cột tím token gần nhất (Status Chip/Purple/Foreground), chạm đúng vạch 1.500k và vạch 0, rộng theo ảnh. Ảnh ở trạng thái cuộn xuống nên thay thân: thêm Thông số kỹ thuật, Tài chính; cột phải thành Kiểm tra sắp đến hạn, Mã lỗi nghiêm trọng, Triệu hồi (bỏ Vị trí, Sự cố, Nhắc bảo dưỡng ngoài ảnh, dùng visible=false). Ô ảnh xe SEM thành "ĐẦU" | Tiêu đề khối Kiểm tra sắp đến hạn suy từ câu rỗng (ảnh cắt mất tiêu đề). Danh sách "Chia theo loại" dưới biểu đồ ngoài khung ảnh, giữ |
| 2.2 assignment-add | Khớp | Không | Ảnh tách ngày và giờ thành 2 ô, bản vẽ gộp 1 ô "03/11/2026 00:40" (component Input lồng sâu, không tách). Lịch tháng nền đánh dấu ngày 2, ảnh là ngày 3 (nền bị phủ, bỏ qua) |
| 2.3 assignment-week | Đã sửa | Ô tìm điền "TEST"; tiêu đề cột hôm nay T3 03 màu đỏ; ô ảnh xe thêm RMO/CON/ĐẦU | Thanh gán màu đậm hơn ảnh (ảnh nhạt, không viền); lịch tháng ảnh đánh dấu ngày 5, bản vẽ ngày 2; nút "..." cạnh Thêm gán xe và chấm trạng thái xanh trên ảnh xe chưa có; cột đầu bản vẽ là CN 01, ảnh cuộn từ T2 02 |
| 2.4 assignment-overlap | Khớp | Không | Ảnh có dòng gợi ý dưới dòng lỗi "không được trùng"; Input trạng thái lỗi chỉ hiện dòng lỗi. Tách ngày/giờ như 2.2. Nút Lưu ảnh màu xanh, bản vẽ theo primary tối của dự án |
| 2.5 assignment-edit | Khớp | Không | Tách ngày/giờ như 2.2 |
| 2.6 assignment-detail | Đã sửa | Thêm dòng đường dẫn "Xe › TEST-XE-LOP › Gán xe" trên tiêu đề | Hàng thông tin bản vẽ có khung viền từng hàng, ảnh chỉ có đường kẻ; huy hiệu Tương lai ảnh nền vàng đậm; ảnh có avatar toán tử; nút "..." |
| 3.2 meter-reject-backdate | Đã sửa | Nền xe: tên TEST-XE-LOP, số đồng hồ 5.500 km, người lái Chưa gán, loại Xe đầu kéo, ô ảnh ĐẦU; Sự cố đang mở thành rỗng, Nhắc bảo dưỡng thành rỗng, thêm khối Nhắc gia hạn | Nền bị phủ, chỉ đúng cấu trúc |
| 3.3 meter-reject-forward | Đã sửa | Như 3.2 (cùng nền) | Như 3.2 |
| 3.4 meter-history-conflict | Đã sửa | Chip lọc Xe tô xanh (Green/Background, đã chọn như ảnh) | Bảng thiếu cột checkbox, ảnh xe SEM có chấm xanh, vạch cam bên trái hàng đã vô hiệu; nút "..." cạnh Thêm số đồng hồ; mũi tên phân trang; Void ảnh là dấu tick, bản vẽ chữ "Có"; popup Learn bỏ theo quy ước |
| 5.2 expense-recurring | Đã sửa | Ghi chú "Chi phí thử nghiệm" thành "TEST expense" (dữ liệu TEST) | Khối Ảnh, Tài liệu dưới form ngoài khung ảnh, giữ |
| 5.3 expense-future | Đã sửa | Chip lọc Xe tô xanh | Như 3.4: checkbox, ảnh xe, nút "...", mũi tên phân trang, tab Tương lai ảnh dùng gạch chân |
| 6.2 replacement-params | Đã sửa | Màu biểu đồ xanh lá thành xanh ngọc (Teal token, cột dưới hex #5ab6b0 vì không có token đủ đậm); Năm 8 chi phí dầu "2,5" thành "—" (ô bị toast che) | Ảnh cuộn xuống chỉ thấy từ 0,50 trở xuống, bản vẽ vẽ cả biểu đồ từ 1,00 (có đường, nhãn ảnh không thấy rõ); ảnh có ký hiệu ₫ trong ô chi phí dầu, bản vẽ không |
| 1.6 reminder-after-work-order | Khớp | Không | Ảnh có avatar BT, avatar xe CAR, avatar người vận hành T; bản vẽ không |
| 1.7 reminder-list-compliance | Đã sửa | Thêm hàng thứ 9 TEST-NHAC-F hoan thanh som (Sắp tới, Mỗi 6 tháng hoặc 9.000 km, tuân thủ 100%; Đến hạn, Hoàn thành lần cuối ghi "—" vì popup Learn che) | Nút "..." cạnh Bật dự báo; avatar xe CAR; ngày dd/mm đã đổi hợp lệ |
| 2.7 inspection-tire-axle-error | Khớp | Không | Không |
| 2.8 inspection-tire-remark-required | Khớp | Không | Ảnh cuộn giữa danh sách, bản vẽ bắt đầu từ tiêu đề Lốp |
| 2.9 inspection-tire-fail-summary | Đã sửa | Thêm liên kết "← Lịch sử kiểm tra" trên tiêu đề | Khung bản đồ để trống đúng (ảnh đã che); avatar xe, người nộp |
| 2.10 inspection-tire-fail-detail | Đã sửa | Thêm dòng Ngoài trái (3LO) Độ sâu gai, giá trị "—" (ảnh cắt nửa dòng) | Khung bản đồ để trống đúng |
| 2.13 item-failure-needs-action | Khớp | Không | Nút "..." cuối hàng; avatar xe CAR |

## Tổng kết
- Khớp ngay: 8 (1.2, 2.2, 2.4, 2.5, 1.6, 2.7, 2.8, 2.13). Đã sửa: 12. Chưa soát: không.
- Lỗi lặp lại: (1) ảnh ở trạng thái cuộn nhưng bản vẽ vẽ đầu trang (1.3, 3.2, 3.3, 6.2); (2) thiếu avatar xe/chấm trạng thái, nút "..." (hầu hết danh sách); (3) hàng cuối bị popup che bị bỏ (1.7, 2.10); (4) Input ngày giờ gộp 1 ô thay vì tách 2.
- Chưa dùng được: Input lồng không cho tách ngày/giờ hay thêm dòng gợi ý khi lỗi, cần sửa component.
