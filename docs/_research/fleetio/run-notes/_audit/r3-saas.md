# Soát nhóm r3-saas (lượt 3-4 và lượt 5)

Section 7332:442609 (lượt 3-4), 7332:464302 (lượt 5). Nguồn so: `docs/_research/fleetio/srs/images/<slug>.jpg`.

| Màn | Kết quả | Đã sửa gì | Còn lệch gì |
|---|---|---|---|
| 7332:415712 report-expense-entries-500 | Khớp | — | Thiếu logo và chấm vàng "Partially Degraded" (chrome Fleetio, bỏ qua theo quy ước) |
| 7332:416419 ai-analyst-vehicle-not-exist | Khớp | — | Không vẽ tooltip rê chuột trên ảnh gốc |
| 7332:419603 automation-version-v1-lech | Khớp | — | Hộp Tóm tắt các bước thiếu icon tròn xanh và đường nối giữa 3 bước |
| 7332:423111 automation-run-failure | Đã sửa | Thẻ nền "Thành công 3, Thất bại 0" sửa thành 0 và 1 (ảnh: Successful 0, Failed 1); thêm liên kết "Xem" ở dòng Phiên bản (7332:464309) | Ô "Tổng lượt chạy" nằm sau hộp thoại, không đọc được, giữ 3 |
| 7332:429435 automation-vehicle-status-flip | Đã sửa | Xe là Semi Truck chứ không phải "Xe con": avatar XE CON sang SEM, loại sang "Xe đầu kéo"; số đồng hồ 2.200 sang 100 km; trạng thái Đang dùng sang Ngừng dùng (badge xanh dương, 2 chỗ); Người lái TEST-LAI-XE sang "Chưa gán"; Loại nhiên liệu giữ "—" | Ảnh có Loại nhiên liệu = Gasoline (Xăng) nhưng giá trị bị che một phần; chưa điền. Giá trị Số đồng hồ ở khối chi tiết bị hộp thoại che, đặt 100 km theo dòng đầu trang |
| 7332:431958 record-history-issue | Khớp | — | — |
| 7332:432653 notifications-inbox | Đã sửa | Nền là sự cố #55 TEST-NEN-D2 khong khop nhom, không phải #31: tiêu đề, breadcrumb, Sự cố # 55, Tóm tắt, Mô tả "—", Ưu tiên "Chưa có ưu tiên", Xe TEST-DAUKEO-2, Việc hiện tại "Chưa gán", Ngày báo cáo 03/11/2026 16:50, Nguồn "—". Dòng thời gian còn 1 sự kiện "Bảo Tín đã mở sự cố này / 13 phút", ẩn 2 sự kiện thừa và liên kết (visible=false, không xoá) | Dòng "Ưu tiên" thiếu dòng phụ "No Priority" (ảnh có 2 dòng). Dòng Nguồn và Người phụ trách bị che dưới khung, đặt "—" |
| 7332:433552 documents-list-file | Đã sửa | Thêm cột checkbox (header + dòng), thu cột Tên tệp 520 sang 484 | Thiếu nút phân trang trước/sau cạnh "1 - 1/1". Popup Learn bỏ theo quy ước |
| 7332:462479 motor-pool-add | Đã sửa | Ô Tên "Nội dung đã nhập" sang TEST-NEN-POOL-01; Loại xe sang "Xe đầu kéo"; menu Cài đặt thêm "Cài đặt chi phí", "Cài đặt quản lý lốp", "Loại nhắc công cụ"; thêm toast "Hoàn tất: Khôi phục dữ liệu Lệnh sửa chữa #106" (7332:464420) | (1) Ô Nhóm: ảnh là chip "11/05/2026" trong ô đa chọn, đọc không chắc đó là tên nhóm hay ngày, giữ "11/05/2026" ở Select đơn. (2) Loại xe và Trạng thái xe ảnh là ô đa chọn có chip, Figma là Select đơn. (3) Nút Huỷ/Lưu ảnh nằm trong cùng hàng, đã khớp. (4) Menu Cài đặt phía trên (Custom Widgets...), "Cài đặt kiểm tra" chưa vẽ. (5) Ảnh có nền che nên không so được khung bảng rỗng |
| 7332:463305 reservation-validation | Đã sửa | Lỗi mẫu "Nói rõ sai gì và cách sửa" thay bằng "phải tồn tại" (Người vận hành) và "bắt buộc với nhóm xe dùng chung này" (Lý do chuyến đi); ô Lý do chuyến đi bỏ chữ mẫu "Nội dung đã nhập"; Loại xe sang "Xe đầu kéo"; thêm toast thành công (7332:464423) phía trên toast thất bại | Nền thiếu thanh Tìm/Xe/lọc phía trên bảng và thẻ "Tổng quan đặt xe" phía dưới (bị che một phần). Loại xe ảnh là ô đa chọn có chip. Toast ảnh có icon và nút đóng, vẽ bản gọn không icon |

## a11y_audit (từng màn)

| Màn | Lỗi |
|---|---|
| report-expense-entries-500 | 0 |
| ai-analyst-vehicle-not-exist | 1: viền nút "Tất cả mô hình dữ liệu" 1.09:1 (cần 3:1) |
| automation-version-v1-lech | 2: viền nút Thêm, Sửa 1.09:1 |
| automation-run-failure | 3: viền Thêm, Sửa, "Xem toàn bộ nhật ký" 1.09:1 |
| automation-vehicle-status-flip | 9: 6 link/nút cao 20px (<24px: Xem tất cả x2, Thêm nhắc bảo dưỡng, Thêm sự cố, Tuỳ chỉnh bố cục, Sửa nhãn) và viền Theo dõi, Thêm, Sửa 1.09:1 |
| record-history-issue | 3: viền Edit Labels, Unwatch, Edit 1.09:1 |
| notifications-inbox | 6: viền Trả lời x3, Edit Labels, Unwatch, Edit 1.09:1 |
| documents-list-file | 4 lỗi viền 1.09:1 (Loại tệp, Loại vị trí, Bộ lọc, Tuỳ chỉnh xem) + 1 review: "Menu dòng" 24x20 |
| motor-pool-add | 3: checkbox 20x20 x2 (trong hộp thoại), viền "Thêm nhóm xe dùng chung" 1.09:1 |
| reservation-validation | 5: 4 chữ ngày giờ placeholder (03/11/2026, 20:22) tương phản 2.52:1 (cần 4.5:1); viền "Thêm đặt xe" 1.09:1 |

Nguyên nhân gốc: tất cả lỗi viền 1.09:1 và kích thước 20px nằm trong component nút Secondary/Tertiary và Checkbox của thư viện (instance), sửa phải ở component, ngoài phạm vi. Chữ placeholder ngày giờ mờ là màu placeholder của Input/Date trong component. Không sửa gì ngoài component vì không có lỗi nào còn lại nằm ở khung hay chữ tự dựng.

## Không đụng
Sidebar, Header (agent khác). Mọi frame giữ nguyên id, vị trí; không xoá node.
