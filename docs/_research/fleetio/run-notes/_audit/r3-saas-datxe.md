# Soát r3 · SaaS · Đặt xe (Section 7386:470002, 7 màn)

| Màn | Kết quả | Đã sửa gì | Còn lệch gì |
|---|---|---|---|
| 5.14 reservation-detail-requested (7386:464778) | Khớp | — | Toast "Restoring Work Order #106" không vẽ (theo brief). Avatar BT cạnh Người vận hành không vẽ (link chữ). |
| 5.15 reservation-approve-dialog (7386:468420) | Đã sửa | Lớp phủ đổi hex #0a0a0a + opacity 0.5 sang token `$color/bg/overlay_solid` (#0a0a0a80, cùng giá trị nhìn) | Nút đóng là chữ "Đóng" thay vì icon X của ảnh (giữ, đã duyệt). Toast Restoring không vẽ. |
| 5.16 reservation-detail-approved (7386:465476) | Khớp | — | Toast "Restoring" bỏ; toast "Đã duyệt đặt xe thành công" đã có. |
| 5.17 reservation-auto-approved-charges (7386:466583) | Khớp | — | Toast Restoring bỏ. |
| 5.18 reservation-charges-flat-fee (7386:467183) | Khớp | — | Toast Restoring bỏ; toast "Đã sửa đặt xe thành công" đã có. |
| 5.19 reservation-vehicle-overlap (7386:469111) | Đã sửa | Lớp phủ sang token (như 5.15). Tooltip dời lên (y 321 sang 313) và danh sách xe đệm trên 38, dòng xe đệm 4: tooltip không còn đè tên xe TEST-DAUKEO-2, dropdown không che nhãn "Nhận xe *". Tooltip nền đã gắn sẵn biến (`$color/bg/primary_solid` = #171717), hex chỉ là giá trị giải ra. | Nhãn "05/11/2026" giữ như đã ghi; VIN/SN giữ `—`; toast Restoring không vẽ. |
| 5.20 reservation-completed (7386:467803) | Khớp | — | Toast Restoring bỏ; toast "Đã hoàn tất đặt xe thành công" đã có. |

Ngày đã đọc theo kiểu Mỹ rồi đổi: 11/10/2026 8:47pm là 10/11/2026 20:47; 11/23 là 23/11; 11/03/2026 8:45pm là 03/11/2026 20:45. Số liệu, dòng phí, tổng (70.000 / 280.000 / 110.000) khớp ảnh. Số đồng hồ 2.510 / 2.560 km khớp.

## a11y_audit đủ 7 màn
| Lỗi | Màn | Xử lý |
|---|---|---|
| nontext-contrast 1.4.11: nút "Thêm" (Secondary) viền 1.09:1 | cả 7 màn (id 7386:465397, 468427, 465483, 466590, 467190, 469118, 467810) | Không sửa: là kiểu Secondary của component Button (đồng bộ toàn file), sửa phải ở component |
| text-contrast: Value 2.31:1 của Select "Nhóm xe dùng chung" | 5.15 (I7386:469018;6658:194031), 5.19 (I7386:469709;6658:194031) | Không sửa: trạng thái Disabled của component Select (WCAG miễn trừ control disabled; ảnh gốc cũng xám) |
Không có lỗi ngoài component. Không có lỗi target-size, icon-only-name, input-label.

## layoutAudit 5.19
Các cảnh báo "đè nhau" chủ yếu từ ảnh nền mờ dưới lớp phủ (Main) và lỗi tràn của Sidebar (agent khác phụ trách), không có lỗi id ngoài `I7…` thuộc component cần sửa.
