# Soát nhóm repair-1 (section 7261:348952, 17 màn)

| Màn | Kết quả | Đã sửa gì | Còn lệch gì |
|---|---|---|---|
| 1.4 issue-close-dialog | Khớp | | Cột Bình luận mở của Fleetio thể hiện bằng rãnh nút theo quy ước |
| 1.5 issue-closed | Đã sửa | Toast "Sự cố #38" thành "#36" (ảnh ghi #36, Fleetio tự lệch với trường #38) | Không vẽ nội dung ngăn Bình luận (rãnh nút theo quy ước) |
| 1.6 issue-resolve-note-dialog | Khớp | | |
| 1.7 issue-resolved-note | Khớp | | |
| 1.8 issue-shop-network | Đã sửa | Ô logo: 9 ô trống thành 10 ô (ảnh có 10 logo), ghi tên: Pep Boys Fleet, Big O Tires, Brakes Plus, Firestone, Discount Tire, Meineke, Midas, Monro, Valvoline | Ô 1 (logo khiên, đầu hàng) không đọc được tên, để trống. Tên ô 3 (Big O Tires) và ô 6 (Discount Tire) đọc từ logo nhỏ, độ chắc trung bình |
| 1.9 issue-draft-running | Đã sửa | Thêm 2 dòng Thông tin cuối: Ngày đến hạn —, Số km đến hạn — (ảnh có Due Date, Due Odometer) | |
| 1.10 issue-draft-ready | Đã sửa | Thêm Ngày đến hạn —, Số km đến hạn —. Việc hiện tại và Ngày báo cáo đã có sẵn khi soát | |
| 1.11 issue-reopen-locked | Đã sửa | Thêm dòng Số km đến hạn 2.201 km (ảnh Due Odometer 2,201 km); thêm dòng dưới thẻ "Tạo 24 phút trước · Cập nhật vài giây trước" | Ngày đến hạn đã có |
| 1.12 issue-menu-locked-tooltip | Đã sửa | Thêm Ngày đến hạn —, Số km đến hạn —; thêm dòng "Tạo 2 phút trước · Cập nhật vài giây trước" | |
| 1.13 issue-resolve-menu | Khớp | | Ảnh có ô nhập bình luận cuối ngăn phải (rãnh nút theo quy ước) |
| 2.4 wo-form-issues-lines | Đã sửa | Dòng việc: Công 0 ₫, Phụ tùng 600.005 ₫, Tạm tính 600.005 ₫ (trước để trống); Danh mục "1 - Khung gầm", Hệ thống "013 - Phanh"; đơn giá phụ tùng 300.000 ₫ (trước —); thêm ô Tìm đầu việc | Thiếu nhãn xám "Không có nhắc bảo dưỡng" cạnh tiêu đề Dòng việc; thiếu cột Thành tiền của dòng phụ tùng (ảnh có 2 ô tiền, ô bị toast che nửa, chữ số 300.000 chắc ~80%); khối Thông tin và Sự cố ngoài khung ảnh nên không đối chiếu được |
| 2.5 wo-add-part | Khớp | | Nền bị phủ khác trạng thái (Parts 0 trong ảnh), bỏ qua |
| 2.6 wo-add-labor | Đã sửa | Ô "Đặt thời gian ghi công" từ hình tròn (radio) thành ô vuông (checkbox) | Nền bị phủ khác nhẹ, bỏ qua |
| 2.7 wo-link-issues | Khớp | | |
| 2.8 wo-draft-review | Khớp | | Thiếu icon thích/không thích và mũi tên mở rộng từng đầu việc (nhỏ) |
| 2.9 wo-draft-add-menu | Khớp | | Thiếu icon bên phải mục menu (nhỏ) |
| 2.10 wo-from-draft | Đã sửa | Ngày sự cố 13:33 thành 01:33 (ảnh 1:33am); thêm khối Tạm tính +0 ₫ / Công 0 ₫ / Phụ tùng 0 ₫ dưới dòng việc | Dòng "Phụ thu công/Phụ tùng" bên dưới trong ảnh bị cắt, không đọc được |

Ghi chú: số lệch của Fleetio giữ nguyên (toast #36 vs trường #38; Phụ tùng 600.005 vs đơn giá 300.000). Mọi màn đã soát, không màn nào bỏ sót. Chưa chạy layoutAudit từng màn.
