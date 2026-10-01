---
type: shared-conventions
status: draft
updated: 2026-10-01
links:
  - docs/design.md
  - docs/_shared/screen-patterns.md
  - docs-input/ui-common/web/web-common-rules.md
---

# UI Common Rules (GR) + lỗi dùng chung (E-common)

Quy tắc giao diện chung toàn hệ thống web. UC/màn gọi theo mã `Theo GR-xx`, chỉ điền phần **UC phải
khai báo**; khác quy tắc chung thì ghi override + lý do. Component dùng chung ở
[[docs/_shared/screen-patterns.md|UI Common Components (CMP)]].

Câu chữ (lỗi, xác nhận, rỗng, toast) theo `docs/design.md` › Content & Formatting › Copy động: ngôi
"bạn", câu ngắn, không "Vui lòng". Định dạng hiển thị chi tiết đã có ở design.md — GR trỏ về mục đó.

| Mã | Quy tắc | Chi tiết ở design.md | Nguồn gốc |
|---|---|---|---|
| GR-01 | Input / Textbox | Nhập liệu và kiểm tra | 2.1 |
| GR-02 | Select / Dropdown | Nhập liệu và kiểm tra | 2.2 |
| GR-03 | Date Picker + hiển thị ngày giờ | Ngày giờ | 2.3 |
| GR-04 | Định dạng tiền | Số và tiền tệ | 2.4 |
| GR-05 | Định dạng số | Số và tiền tệ | 2.5 |
| GR-06 | Làm tròn | Số và tiền tệ | 2.6 |
| GR-07 | Email | Nhập liệu và kiểm tra | 2.7 |
| GR-08 | Số điện thoại | Thông tin liên hệ và địa chỉ | 2.8 |
| GR-09 | Thanh tìm kiếm | Quy tắc bảng danh sách | 2.9 |
| GR-10 | Trường không có thông tin | — | 2.10 |
| GR-11 | Sinh mã bản ghi | — | 2.11 |
| GR-12 | Trạng thái rỗng / đang tải | States + Copy động | 2.12 |
| GR-13 | Dữ liệu chưa lưu | Copy động › Hộp xác nhận | 2.13 |
| GR-14 | Căn lề trong bảng | Quy tắc bảng danh sách | 2.14 |
| GR-15 | Phân loại thông báo lỗi | Copy động + Nhập liệu và kiểm tra | 2.15 |
| GR-16 | Freeze cột | Quy tắc bảng danh sách | 2.16 |
| GR-17 | Nhóm dữ liệu (Group By) | Quy tắc bảng danh sách | 2.17 |
| GR-18 | Sắp xếp | Quy tắc bảng danh sách | 2.18 |
| GR-19 | Export | Quy tắc bảng danh sách | 2.19 |
| GR-20 | Lọc theo cột | Quy tắc bảng danh sách + Bộ lọc nâng cao | 2.20 |

---

## Nhập liệu

### GR-01 — Input / Textbox
- **Khi nào kiểm:** On Blur (rời trường) và On Submit (kiểm mọi trường, kể cả trường chưa chạm).
- **Submit có lỗi:** inline error mọi trường lỗi, cuộn tới lỗi đầu tiên, không gửi, nút về thường.
- **Submit hợp lệ:** nút loading + vô hiệu; server trả lỗi → hiện lỗi, giữ form, nút về thường.
- **Độ dài:** Tiêu đề tối đa 50 (`E-common-002`) · text ngắn 255, không gõ thêm được, dán vượt tự cắt · textarea 1000 (hoặc theo UC), có đếm ký tự, dán vượt tự cắt.
- **Bắt buộc:** nhãn có `*`; bỏ trống → `E-common-001`.
- **UC phải khai báo:** trường nào bắt buộc; loại trường (tiêu đề / ngắn / textarea); giới hạn khác mặc định; rule riêng của trường (`E-{feature}-NNN`).
- **design.md:** Nhập liệu và kiểm tra

### GR-02 — Select / Dropdown
- Chọn 1, hoặc chọn nhiều (giá trị hiện dạng tag trong ô). Danh sách từ server: tìm gần đúng khi gõ.
- Bắt buộc chưa chọn → `E-common-001` (dạng "Chọn …").
- **UC phải khai báo:** nguồn danh sách; chọn 1 hay nhiều; giá trị mặc định; phụ thuộc trường khác.
- **design.md:** Nhập liệu và kiểm tra

### GR-03 — Date Picker + hiển thị ngày giờ
- Gõ trực tiếp hoặc chọn từ lịch. Hiển thị `dd/mm/yyyy`, có giờ `dd/mm/yyyy hh:mm` (24 giờ). Các dạng khác (tương đối, khoảng ngày): design.md › Ngày giờ.
- Sai định dạng → `E-common-003`.
- **UC phải khai báo:** có giờ không; khoảng cho phép (vd không chọn ngày quá khứ) + lỗi riêng.
- **design.md:** Ngày giờ

### GR-04 — Định dạng tiền
- Mặc định VND; danh sách đơn vị quản lý ở hệ thống, không sửa trên giao diện. Tự chèn `,` hàng nghìn khi gõ. Hiển thị `100,000 đ` / `100,000 VND`; ngoại tệ `50 USD · 25,000 VND/USD`.
- **UC phải khai báo:** trường tiền nào có ngoại tệ; nguồn tỷ giá.
- **design.md:** Số và tiền tệ

### GR-05 — Định dạng số
- Chỉ cho số và `.` thập phân, chặn ký tự khác. Hàng nghìn `,`, thập phân `.`.
- **UC phải khai báo:** khoảng giá trị hợp lệ (vd > 0) + lỗi riêng.
- **design.md:** Số và tiền tệ

### GR-06 — Làm tròn
- Số học và USD: 2 chữ số thập phân, làm tròn nửa lên. VND: không lẻ, luôn làm tròn lên hàng đơn vị. Áp cho hiển thị, tính toán và lưu.
- **UC phải khai báo:** chỉ khi khác quy tắc (override + lý do).
- **design.md:** Số và tiền tệ

### GR-07 — Email
- Phải có `@`. Sai → `E-common-004`.
- **design.md:** Nhập liệu và kiểm tra

### GR-08 — Số điện thoại
- Chỉ số, đầu số `0` hoặc `84`, tối đa 11 ký tự. Hiển thị theo design.md › Thông tin liên hệ. Sai → `E-common-005`.
- **design.md:** Thông tin liên hệ và địa chỉ

## Danh sách và bảng

### GR-09 — Thanh tìm kiếm
- Tìm gần đúng toàn bộ dữ liệu bảng. Chạy khi Enter hoặc rời ô; màn realtime debounce 300ms. Trường cố định (trạng thái, phân loại) không tìm được → tooltip liệt kê, dùng lọc thay thế.
- **UC phải khai báo:** trường tìm được / không tìm được; có realtime không.
- **design.md:** Quy tắc bảng danh sách

### GR-14 — Căn lề trong bảng
- Số, tiền, % căn phải · ngày giờ căn giữa · văn bản, trạng thái căn trái · tiêu đề cột theo dữ liệu.
- **design.md:** Quy tắc bảng danh sách

### GR-16 — Freeze cột
- Chỉ khi bảng cuộn ngang: cột đầu (Tên/Mã) cố định trái, cột hành động cố định phải, bóng nhẹ ở cạnh trong.
- **UC phải khai báo:** cột cố định nếu khác Tên/Mã.
- **design.md:** Quy tắc bảng danh sách

### GR-17 — Nhóm dữ liệu
- Nút Nhóm trên toolbar, chọn 1 cột; Xoá để bỏ. Dòng cha = giá trị + số bản ghi. Nhóm đầu mở sẵn tối đa 10 dòng, nhóm khác thu gọn; >10 có "Xem thêm" (+10). Phân trang theo nhóm.
- **UC phải khai báo:** cột được phép nhóm.
- **design.md:** Quy tắc bảng danh sách; Phân trang danh sách

### GR-18 — Sắp xếp
- Click tiêu đề cột: tăng → giảm → mặc định. Mỗi lúc 1 cột. Mặc định mới nhất trước (thời gian tạo giảm dần).
- **UC phải khai báo:** sort mặc định nếu khác; cột không sort được (override + lý do).
- **design.md:** Quy tắc bảng danh sách

### GR-19 — Export
- Xuất PDF / Excel toàn bộ dữ liệu sau lọc, nhóm, tuỳ chỉnh cột, gồm mọi trang.
- **UC phải khai báo:** có export không; định dạng nào; quyền.
- **design.md:** Quy tắc bảng danh sách

### GR-20 — Lọc theo cột
- Nhập giá trị/ID → ô tìm · chọn giá trị → dropdown · ngày → khoảng ngày (chỉ ngày, không giờ) · số/tiền/% → Từ – Đến. Cách trình bày: CMP-05.
- **UC phải khai báo:** cột lọc được + kiểu lọc.
- **design.md:** Quy tắc bảng danh sách; Bộ lọc nâng cao

## Hiển thị và trạng thái

### GR-10 — Trường không có thông tin
- Ghi chú: ẩn hẳn · ID/Mã: `N/A` · trường khác: `-`.
- **design.md:** —

### GR-11 — Sinh mã bản ghi
- Sinh sau khi bản ghi được phê duyệt; trước đó nhận diện bằng người tạo, ngày tạo, trạng thái. Feature không có phê duyệt hoặc tạo tự động → sinh ngay khi tạo.
- **UC phải khai báo:** thời điểm sinh nếu khác; prefix/format mã (theo tài liệu format mã của dự án).
- **design.md:** —

### GR-12 — Trạng thái rỗng / đang tải
- Chưa có dữ liệu: hình + mô tả + nút Tạo mới (nếu có quyền).
- Lọc không ra kết quả: thông báo không có kết quả + nút Xoá bộ lọc, không có Tạo mới.
- Đang tải: skeleton theo số cột/dòng hiện tại. Câu chữ theo design.md › Copy động.
- **UC phải khai báo:** nội dung trạng thái rỗng (cái gì rỗng + CTA).
- **design.md:** Trạng thái giao diện; Copy động

### GR-13 — Dữ liệu chưa lưu
- Đóng tab / trình duyệt / tải lại: hộp confirm gốc của trình duyệt.
- Bấm Huỷ trên form đã nhập: CMP-03 (Huỷ form).
- **UC phải khai báo:** form nào áp dụng.
- **design.md:** Copy động

### GR-15 — Phân loại thông báo lỗi

| | Loại 1 — Inline | Loại 2 — Popup Error | Loại 3 — Toast Error |
|---|---|---|---|
| Khi nào | Lỗi của 1 trường (định dạng, bắt buộc, giá trị không hợp lệ); On Blur / On Submit | Lỗi chỉ biết sau khi submit do đối chiếu dữ liệu server (trùng mã, vượt hạn mức, ràng buộc nghiệp vụ); không gắn trường nào | Lỗi kỹ thuật/hệ thống (API lỗi, mất kết nối, timeout, 5xx); người dùng không tự sửa được |
| Vị trí | Dưới trường | Modal giữa màn, có nền mờ | Toast góc trên phải (CMP-01) |
| Hiển thị | Viền trường + câu lỗi màu error | Tiêu đề lỗi + mô tả + Đóng; thêm Thử lại nếu retry được | Nền error |
| Hành vi | Tự ẩn khi giá trị hợp lệ | Không tự đóng; đóng xong giữ nguyên form | Tự ẩn sau 3 giây, không chặn |

- **UC phải khai báo:** mỗi lỗi nghiệp vụ (`E-{feature}-NNN`) thuộc loại nào; lỗi Loại 2 có Thử lại không.
- **design.md:** Copy động; Nhập liệu và kiểm tra

---

## Lỗi dùng chung (E-common)

UC dùng lại mã dưới, **không tạo `E-{feature}-NNN` trùng nghĩa**. Câu lỗi riêng cho 1 trường (vd "Nhập
tên cây dầu.") vẫn là E-common-001 với `[tên trường]` điền cụ thể.

| ID | Loại (GR-15) | Khi nào | Câu hiển thị | Quy tắc |
|---|---|---|---|---|
| E-common-001 | Inline | Trường bắt buộc bỏ trống khi submit | "Nhập [tên trường]." · Select: "Chọn [tên trường]." | GR-01, GR-02 |
| E-common-002 | Inline | Tiêu đề vượt 50 ký tự | "Tối đa 50 ký tự." | GR-01 |
| E-common-003 | Inline | Ngày sai định dạng | "Hãy nhập ngày tháng theo định dạng: dd/mm/yyyy" | GR-03 |
| E-common-004 | Inline | Email sai định dạng | "Email không đúng định dạng." | GR-07 |
| E-common-005 | Inline | SĐT sai định dạng | "Số điện thoại không đúng định dạng." | GR-08 |
| E-common-006 | Inline | File sai định dạng | "File không đúng định dạng." | CMP-10 |
| E-common-007 | Inline | File vượt dung lượng | "Dung lượng file tối đa 250MB." | CMP-10 |
| E-common-008 | Toast | Lỗi hệ thống / API / timeout | "Đã xảy ra lỗi. Thử lại sau." | GR-15 Loại 3 |
| E-common-009 | Toast | Mất kết nối mạng | "Mất kết nối. Kiểm tra mạng và thử lại." | GR-15 Loại 3 |
| E-common-010 | Toast | Phiên đăng nhập hết hạn | "Phiên làm việc đã hết hạn. Đăng nhập lại." | GR-15 Loại 3 |
