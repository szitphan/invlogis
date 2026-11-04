# Soát màn Fleetio lượt 3-5 (nhóm r3-parts-repair)

Soát 17 màn so với ảnh gốc. a11y_audit chạy cả 17 màn; layoutAudit sau sửa: 0 lỗi ngoài component ở 14 màn đã sửa.

| Màn | Kết quả | Đã sửa gì | Còn lệch gì |
|---|---|---|---|
| 7332:428164 fuel-filter-alert-type | Khớp | - | - |
| 7332:436048 po-adjust-closed | Đã sửa | Thêm dòng "Người đóng" (ảnh có Closed By); ẩn nút Primary "Đóng" tự thêm (có reaction nên chỉ ẩn, không xoá) | Nút X của modal đang là chữ "Đóng hộp" |
| 7332:440965 po-edit-purchased | Đã sửa | Dòng Phí vận chuyển: thêm giá trị nhập 20000 và 20.000 ₫ | Thiếu huy hiệu đếm "2" cạnh "Dòng hàng"; thiếu ảnh thumb phụ tùng |
| 7332:450722 po-print-pdf | Đã sửa | Tiền đổi sang dạng 1.350.000 ₫ (9 ô) | - |
| 7332:438416 po-record-history | Đã sửa | 7 câu tiền đổi sang dấu chấm; ẩn nút "Đóng" tự thêm ở nền | - |
| 7332:426103 fault-rules | Khớp | - | Menu trái Cài đặt dài hơn ảnh (ảnh cuộn giữa), chấp nhận |
| 7332:418132 issue-resolved-negative-ttr | Đã sửa | Nút Mở lại State Default (bật); "~15 giờ" thành "-15 giờ 16 phút" | - |
| 7332:422102 vehicle-warranties-tab | Đã sửa | Xoá 3 tab ảnh không có (Quản lý lốp, Hoạt động lốp, Nhắc bảo dưỡng; không có reaction) | - |
| 7332:452037 wo-print-pdf | Đã sửa | Tiền đổi dấu chấm (11 ô) | Thiếu icon cờ lê, người, chấm than ở dòng việc |
| 7332:445228 wo-warranty-claim-fields | Khớp | - | - |
| 7332:455289 settings-valuation-fifo-permanent-warning | Đã sửa | Nhãn ô tích về 1 dòng; "₫1" thành "1 ₫" | - |
| 7332:458807 shop-network-enable-denied | Đã sửa | Thêm toast "Hoàn tất: Khôi phục... #105" (Toast DS, tuyệt đối góc phải dưới) | Icon "i" trong hộp lỗi |
| 7332:459288 warranty-template-list | Đã sửa | Thêm toast khôi phục #106; "TEST-HANG,", giữ dấu phẩy như ảnh | - |
| 7332:459828 warranty-template-preview | Đã sửa | Thêm toast khôi phục #106 | Nút ⋯ đang là chữ "Thêm"; thiếu icon X, ⓘ ở ô chọn mẫu |
| 7332:460482 warranty-oem-template-preview | Đã sửa | Thêm toast khôi phục #106 | như trên |
| 7332:461904 warranty-template-change | Đã sửa | Lớp phủ opacity 0.5 thành 1 (hiện đủ); thêm toast #106 | - |
| 7332:461188 wo-status-custom-list | Đã sửa | Chấm màu Đang mở thành cyan, dòng TEST-SUA Xong thành tím; thêm toast #106 | Thiếu icon ổ khoá, tay kéo, ô tích đầu dòng và icon Hoàn thành ở cột Loại; nút ⋯ là chữ "Thêm" |

## Lỗi a11y từ a11y_audit (nằm trong component, không sửa)
- Nút Secondary/ghost (Thêm, Sửa, Bỏ theo dõi, Bộ lọc, chip lọc): viền 1.09:1, cần 3:1. Lặp ở hầu hết màn có thanh nút.
- Radio và Checkbox 20x20px dưới 24px; viền Radio 1:1 trên nền khối (455289, 459828, 460482, 461904).
- Chữ nút disabled 2.31:1 (po-adjust-closed "Thực hiện điều chỉnh", po-edit-purchased Select khoá): chữ trạng thái vô hiệu, được phép.
- Hint của Radio 4.22:1 (459828, 460482).
- Không có lỗi: po-print-pdf, fault-rules, vehicle-warranties-tab, wo-print-pdf, shop-network, warranty-template-list, wo-status-custom-list.

## Ghi chú
- Chấm cyan #06aed4 và tím #7a5af8 dùng hex (chưa tra được token tương ứng).
- Toast bổ sung: 358807 dùng component Toast DS (tối); các màn bảo hành và trạng thái lệnh dùng bản nhân từ toast xanh viền có sẵn để khớp bảng toast đã vẽ trong cùng màn. Hai kiểu chưa đồng nhất.
- Số tiền kiểu Fleetio trên PDF/lịch sử ghi bản ghi đã đổi sang dấu chấm theo bảng quy đổi.
- Chưa soát: không có màn nào bị bỏ.
