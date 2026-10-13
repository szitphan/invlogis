---
type: shared-conventions
status: draft
updated: 2026-10-12
links:
  - design/design.md
  - design/ui-common/screen-patterns.md
  - docs-input/ui-common/web/web-common-rules.md
  - docs-input/ui-common/app/app-common-rules.md
---

# UI Common Rules (GR) + lỗi dùng chung (E-common)

Quy tắc giao diện chung toàn hệ thống, web và app. UC/màn gọi theo mã `Theo GR-xx`, chỉ điền phần **UC phải
khai báo**; khác quy tắc chung thì ghi override + lý do. Chỗ app khác web ghi ở dòng **Mobile** trong từng
mục; GR-21…GR-26 chỉ áp app. Component dùng chung ở
[[design/ui-common/screen-patterns.md|UI Common Components (CMP)]].

Câu chữ (lỗi, xác nhận, rỗng, toast) theo `design/design.md` › Content & Formatting › Copy động: ngôi
"bạn", câu ngắn, không "Vui lòng". Định dạng hiển thị chi tiết đã có ở design.md — GR trỏ về mục đó.

| Mã | Quy tắc | Chi tiết ở design.md | Nguồn gốc |
|---|---|---|---|
| GR-01 | Input / Textbox | Nhập liệu và kiểm tra | 2.1 · app 2.2 |
| GR-02 | Select / Dropdown | Nhập liệu và kiểm tra | 2.2 · app 2.3 |
| GR-03 | Date Picker + hiển thị ngày giờ | Ngày giờ | 2.3 · app 2.6 |
| GR-04 | Định dạng tiền | Số và tiền tệ | 2.4 · app 2.4 |
| GR-05 | Định dạng số | Số và tiền tệ | 2.5 · app 2.5 |
| GR-06 | Làm tròn | Số và tiền tệ | 2.6 · app 2.4 |
| GR-07 | Email | Nhập liệu và kiểm tra | 2.7 · app 2.7 |
| GR-08 | Số điện thoại | Thông tin liên hệ và địa chỉ | 2.8 · app 2.8 |
| GR-09 | Thanh tìm kiếm | Quy tắc bảng danh sách | 2.9 · app 2.9 |
| GR-10 | Trường không có thông tin | — | 2.10 · app 2.10 |
| GR-11 | Sinh mã yêu cầu và mã bản ghi | — | 2.11 · app 2.11 · cross-process-flow (12/10/2026) |
| GR-12 | Trạng thái rỗng / đang tải | States + Copy động | 2.12 · MSC-09, MSC-10 |
| GR-13 | Dữ liệu chưa lưu | Copy động › Hộp xác nhận | 2.13 · app 2.13 |
| GR-14 | Căn lề trong bảng | Quy tắc bảng danh sách | 2.14 (chỉ web) |
| GR-15 | Phân loại thông báo lỗi | Copy động + Nhập liệu và kiểm tra | 2.15 · app 2.12 |
| GR-16 | Freeze cột | Quy tắc bảng danh sách | 2.16 (chỉ web) |
| GR-17 | Nhóm dữ liệu (Group By) | Quy tắc bảng danh sách | 2.17 (chỉ web) |
| GR-18 | Sắp xếp | Quy tắc bảng danh sách | 2.18 (chỉ web) |
| GR-19 | Export | Quy tắc bảng danh sách | 2.19 (chỉ web) |
| GR-20 | Lọc theo cột | Quy tắc bảng danh sách + Bộ lọc nâng cao | 2.20 (chỉ web) |
| GR-21 | Nút bấm | — | app 2.1 |
| GR-22 | Kéo để làm mới | — | app 2.14 |
| GR-23 | Cuộn danh sách | Phân trang danh sách | app 2.15 |
| GR-24 | Điều hướng app | — | app 2.16 |
| GR-25 | Trạng thái kết nối mạng | Copy động | app 2.17 |
| GR-26 | Popup chặn | Copy động | app 2.18 |
| GR-27 | Dữ liệu đã cũ | Copy động | cross-process-flow (12/10/2026) |
| GR-28 | Không có quyền xem (web) | Copy động | cross-process-flow (12/10/2026) |

---

## Nhập liệu

### GR-01 — Input / Textbox
- **Khi nào kiểm:** On Blur (rời trường) và On Submit (kiểm mọi trường, kể cả trường chưa chạm).
- **Submit có lỗi:** inline error mọi trường lỗi, cuộn tới lỗi đầu tiên, không gửi, nút về thường.
- **Submit hợp lệ:** nút loading + vô hiệu; server trả lỗi → hiện lỗi, giữ form, nút về thường.
- **Độ dài:** Tiêu đề tối đa 50 (`E-common-002`) · text ngắn 255, không gõ thêm được, dán vượt tự cắt · textarea 1000 (hoặc theo UC), có đếm ký tự, dán vượt tự cắt.
- **Bắt buộc:** nhãn có `*`; bỏ trống → `E-common-001`.
- **UC phải khai báo:** trường nào bắt buộc; loại trường (tiêu đề / ngắn / textarea); giới hạn khác mặc định; rule riêng của trường (`E-{feature}-NNN`).
- **Mobile:** mở đúng bàn phím theo loại trường (chữ · số · email · điện thoại · số thập phân); icon ✕ trong ô khi có nội dung, chạm để xoá hết. Textarea tối đa 1000 như web, bộ đếm chỉ hiện khi còn ≤ 200 ký tự (tài liệu app ghi 4000 — đã chốt 1000, 2026-10-04).
- **design.md:** Nhập liệu và kiểm tra

### GR-02 — Select / Dropdown
- Chọn 1, hoặc chọn nhiều (giá trị hiện dạng tag trong ô). Danh sách từ server: tìm gần đúng khi gõ.
- Bắt buộc chưa chọn → `E-common-001` (dạng "Chọn …").
- **UC phải khai báo:** nguồn danh sách; chọn 1 hay nhiều; giá trị mặc định; phụ thuộc trường khác.
- **Mobile:** mở `BottomSheet` thay dropdown (design.md › BottomSheet, `.Content · Chọn một` / `Chọn nhiều`); có ô tìm khi danh sách > 10 mục. Chọn 1: chạm là chọn và đóng. Chọn nhiều: checkbox + nút **Xong** cố định đáy. Chọn người: avatar + tên đậm, dòng 2 mã · chức vụ; đã chọn hiện avatar nhỏ + "Mã - Tên" trong ô.
- **design.md:** Nhập liệu và kiểm tra

### GR-03 — Date Picker + hiển thị ngày giờ
- Gõ trực tiếp hoặc chọn từ lịch. Hiển thị `dd/mm/yyyy`, có giờ `dd/mm/yyyy hh:mm` (24 giờ). Các dạng khác (tương đối, khoảng ngày): design.md › Ngày giờ.
- Sai định dạng → `E-common-003`.
- **UC phải khai báo:** có giờ không; khoảng cho phép (vd không chọn ngày quá khứ) + lỗi riêng.
- **Mobile:** mở bộ chọn ngày của hệ điều hành hoặc bánh xe cuộn tuỳ ngữ cảnh; định dạng và lỗi như web.
- **design.md:** Ngày giờ

### GR-04 — Định dạng tiền
- Mặc định VND; danh sách đơn vị quản lý ở hệ thống, không sửa trên giao diện. Tự chèn `,` hàng nghìn khi gõ. Hiển thị `100,000 đ` / `100,000 VND`; ngoại tệ `50 USD · 25,000 VND/USD`.
- **UC phải khai báo:** trường tiền nào có ngoại tệ; nguồn tỷ giá.
- **Mobile:** dùng chung web.
- **design.md:** Số và tiền tệ

### GR-05 — Định dạng số
- Chỉ cho số và `.` thập phân, chặn ký tự khác. Hàng nghìn `,`, thập phân `.`.
- **UC phải khai báo:** khoảng giá trị hợp lệ (vd > 0) + lỗi riêng.
- **Mobile:** dùng chung web; mở bàn phím số / số thập phân.
- **design.md:** Số và tiền tệ

### GR-06 — Làm tròn
- Số học và USD: 2 chữ số thập phân, làm tròn nửa lên. VND: không lẻ, luôn làm tròn lên hàng đơn vị. Áp cho hiển thị, tính toán và lưu.
- **UC phải khai báo:** chỉ khi khác quy tắc (override + lý do).
- **Mobile:** dùng chung web.
- **design.md:** Số và tiền tệ

### GR-07 — Email
- Phải có `@`. Sai → `E-common-004`.
- **Mobile:** tự mở bàn phím email.
- **design.md:** Nhập liệu và kiểm tra

### GR-08 — Số điện thoại
- Chỉ số, đầu số `0` hoặc `84`, tối đa 11 ký tự. Hiển thị theo design.md › Thông tin liên hệ. Sai → `E-common-005`.
- **Mobile:** tự mở bàn phím số, chặn ký tự khác số.
- **design.md:** Thông tin liên hệ và địa chỉ

## Danh sách và bảng

GR-14, GR-16…GR-20 chỉ áp web — app không có bảng nhiều cột (danh sách dạng List, cuộn theo GR-23).

### GR-09 — Thanh tìm kiếm
- Tìm gần đúng toàn bộ dữ liệu bảng. Chạy khi Enter hoặc rời ô; màn realtime debounce 300ms. Trường cố định (trạng thái, phân loại) không tìm được → tooltip liệt kê, dùng lọc thay thế.
- **UC phải khai báo:** trường tìm được / không tìm được; có realtime không.
- **Mobile:** luôn realtime, debounce 300ms. Không ra kết quả → GR-12 (tìm không ra). Trường cố định → lọc bằng CMP-05.
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
- **Mobile:** dùng chung web (tài liệu app ghi `--` — đã chốt `-`, 2026-10-04).
- **design.md:** —

### GR-11 — Sinh mã yêu cầu và mã bản ghi
- Bản ghi phải phê duyệt có 2 mã:
  - **Mã yêu cầu** sinh ngay khi gửi duyệt lần đầu, dạng `YC-[Prefix]-[Định danh]-[4 số]` ([Định danh] giống mã bản ghi). Hiện khi bản ghi Chờ phê duyệt / Đã từ chối / Đã thu hồi. Sửa rồi gửi lại giữ nguyên mã yêu cầu.
  - **Mã bản ghi** sinh khi được phê duyệt, dạng `[Prefix]-[Định danh]-[4 số]`. Từ lúc này hiện mã bản ghi; mã yêu cầu vẫn lưu kèm bản ghi.
- Bản nháp chưa gửi chưa có mã; nhận diện bằng người tạo, ngày tạo, trạng thái.
- Feature không có phê duyệt hoặc tạo tự động → chỉ có mã bản ghi, sinh ngay khi tạo.
- Tìm theo mã: tìm được cả mã yêu cầu lẫn mã bản ghi.
- **UC phải khai báo:** prefix + định danh (theo tài liệu format mã của dự án); thời điểm sinh nếu khác.
- **Mobile:** dùng chung web.
- **design.md:** —

### GR-12 — Trạng thái rỗng / đang tải
- Chưa có dữ liệu: hình + mô tả + nút Tạo mới (nếu có quyền).
- Lọc không ra kết quả: thông báo không có kết quả + nút Xoá bộ lọc, không có Tạo mới.
- Đang tải: skeleton theo số cột/dòng hiện tại. Câu chữ theo design.md › Copy động.
- **UC phải khai báo:** nội dung trạng thái rỗng (cái gì rỗng + CTA).
- **Mobile (MSC-09, MSC-10):** rỗng = hình minh hoạ + tiêu đề + mô tả + CTA (chỉ khi có quyền tạo) — hình minh hoạ chưa có chuẩn (design.md KG-29). Tải lần đầu: skeleton theo hình bố cục thật, hiệu ứng shimmer; tải xong chuyển mờ sang dữ liệu. Không tải được dữ liệu: màn lỗi = `EmptyState` lỗi + nút **Thử lại** (design.md › Quy ước chung của component dự án).
- **design.md:** Trạng thái giao diện; Copy động

### GR-13 — Dữ liệu chưa lưu
- Đóng tab / trình duyệt / tải lại: hộp confirm gốc của trình duyệt.
- Bấm Huỷ trên form đã nhập: CMP-03 (Huỷ form).
- **UC phải khai báo:** form nào áp dụng.
- **Mobile:** Back hoặc vuốt back khi form đã đổi so với ban đầu → CMP-03 Mobile: "Thoát mà không lưu?" · "Dữ liệu đã nhập sẽ mất." → `[Thoát]` (destructive) `[Ở lại]`. Form chưa đổi → thoát luôn. Câu gốc app 2.13: "Bạn có chắc muốn thoát? Dữ liệu đã nhập sẽ bị mất."
- **design.md:** Copy động

### GR-15 — Phân loại thông báo lỗi

| | Loại 1 — Inline | Loại 2 — Popup Error | Loại 3 — Toast Error |
|---|---|---|---|
| Khi nào | Lỗi của 1 trường (định dạng, bắt buộc, giá trị không hợp lệ); On Blur / On Submit | Lỗi chỉ biết sau khi submit do đối chiếu dữ liệu server (trùng mã, vượt hạn mức, ràng buộc nghiệp vụ); không gắn trường nào | Lỗi kỹ thuật/hệ thống (API lỗi, mất kết nối, timeout, 5xx); người dùng không tự sửa được |
| Vị trí | Dưới trường | Modal giữa màn, có nền mờ | Toast góc trên phải (CMP-01) |
| Hiển thị | Viền trường + câu lỗi màu error | Tiêu đề lỗi + mô tả + Đóng; thêm Thử lại nếu retry được | Nền error |
| Hành vi | Tự ẩn khi giá trị hợp lệ | Không tự đóng; đóng xong giữ nguyên form | Tự ẩn sau 3 giây, không chặn |

- **UC phải khai báo:** mỗi lỗi nghiệp vụ (`E-{feature}-NNN`) thuộc loại nào; lỗi Loại 2 có Thử lại không.
- **Mobile:**
  - Loại 1: như web, chữ error + icon cảnh báo dưới trường.
  - Loại 2: bottom sheet cùng khung CMP-03 Mobile — icon lỗi + tiêu đề lỗi + mô tả + nút **Đóng** full width; retry được thì **Thử lại** là nút chính đứng trên, **Đóng** ghost đứng dưới; khoá đóng như hàng 8 CMP-03 Mobile (chạm nền / vuốt xuống không đóng); đóng xong giữ nguyên form. Tài liệu app không có loại này — bổ sung 2026-10-04, chưa có chuẩn trong design.md.
  - Loại 3: toast CMP-01 (Mobile).
  - Không tải được dữ liệu cả màn: màn lỗi theo GR-12 (Mobile). Lỗi phiên/quyền: GR-26.
- **design.md:** Copy động; Nhập liệu và kiểm tra

### GR-27 — Dữ liệu đã cũ
- Màn đang mở (danh sách, popup, sheet) mà dữ liệu vừa đổi ở nơi khác: hiện banner tông neutral đầu vùng nội dung "[Đối tượng] vừa có cập nhật." kèm nút **Tải lại**. Không tự tải lại, để người dùng không mất chỗ đang xem.
- Bấm Tải lại: tải dữ liệu mới, giữ chỗ đang xem nếu còn (vd bước đang chọn, bộ lọc), rồi ẩn banner.
- **UC phải khai báo:** màn nào áp dụng; từ thay cho [Đối tượng] (vd "Quy trình", "Danh sách"); giữ lại gì sau khi tải lại.
- **Mobile:** dùng chung web; banner nằm ngay dưới header màn hoặc header sheet.
- **design.md:** Copy động

### GR-28 — Không có quyền xem (web)
- Mở thẳng đường dẫn một trang không có quyền menu → vùng nội dung hiện `E-common-011` + nút **Về trang chủ**; header và menu trái vẫn hiện.
- Bấm mở một bản ghi không có quyền xem → popup Loại 2 (GR-15) câu `E-common-011` + nút **Đóng**, ở lại màn đang xem.
- Một khối trong màn (panel, tab) không có quyền xem → câu `E-common-011` tại chỗ thay nội dung khối; phần còn lại dùng bình thường.
- **UC phải khai báo:** trường hợp nào áp dụng; quyền của nghiệp vụ nào quyết định.
- **Mobile:** theo GR-26 (popup chặn, nút Quay lại).
- **design.md:** Copy động

## App (chỉ mobile)

### GR-21 — Nút bấm
- Chạm Gửi / Lưu / Tạo mới → kiểm mọi trường bắt buộc; lỗi inline, cuộn tới lỗi đầu tiên.
- Đang xử lý: spinner + vô hiệu nút, chống chạm đúp.
- Nút chính trong form hoặc `BottomSheet` luôn full width.
- Nút xoá/huỷ tông error, không làm nút chính — luôn là nút phụ hoặc ở vị trí thứ yếu.
- **design.md:** —

### GR-22 — Kéo để làm mới
- Kéo xuống khi đang ở đầu màn → tải lại dữ liệu, về đầu danh sách.
- Áp mọi màn danh sách và màn chi tiết.
- **UC phải khai báo:** màn nào không áp (override + lý do).
- **design.md:** —

### GR-23 — Cuộn danh sách
- Cuộn tới 80% cuối → tự tải thêm 20 mục; spinner nhỏ ở cuối khi đang tải; hết dữ liệu → "Đã hiển thị tất cả kết quả".
- Chạm thanh tiêu đề → cuộn về đầu danh sách.
- Danh sách có nhóm: tiêu đề nhóm dính lại khi cuộn qua.
- **UC phải khai báo:** số mục mỗi lần nếu khác 20; danh sách có nhóm không, nhóm theo gì.
- **design.md:** Phân trang danh sách

### GR-24 — Điều hướng app
- Back: nút Back, vuốt từ trái sang phải (iOS) hoặc cử chỉ back (Android) → màn trước.
- Deep link: chạm thông báo (CMP-02) → mở thẳng màn chi tiết bản ghi.
- `BottomSheet` / popup: vuốt xuống hoặc chạm nền → đóng; trừ CMP-12, GR-26 và hành động không hoàn tác (CMP-03).
- **UC phải khai báo:** màn đích của deep link.
- **design.md:** —

### GR-25 — Trạng thái kết nối mạng
- Mất kết nối → banner tông neutral đầu màn "Không có kết nối internet", giữ tới khi có mạng lại.
- Có mạng lại → banner tông success "Đã kết nối lại", tự ẩn sau 2 giây; tự gửi lại các yêu cầu đang chờ.
- Yêu cầu thất bại do mạng → toast `E-common-009`.
- **design.md:** Copy động

### GR-26 — Popup chặn
- Popup cùng khung CMP-03 Mobile nhưng **không đóng** khi chạm nền hay vuốt xuống — chỉ đóng bằng nút.
- Phiên hết hạn → `E-common-010`, nút **Đăng nhập lại** (duy nhất).
- Mở màn không có quyền → `E-common-011`, nút **Quay lại**.
- Quyền tài khoản vừa thay đổi → `E-common-012`, nút **Tải lại ngay** (duy nhất).
- Chuyển site là hộp xác nhận đóng được → CMP-03 Mobile, không thuộc mục này.
- **design.md:** Copy động

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
| E-common-010 | Toast (web) · Popup chặn (app) | Phiên đăng nhập hết hạn | "Phiên làm việc đã hết hạn. Đăng nhập lại." | GR-15 Loại 3 · GR-26 |
| E-common-011 | Tại chỗ / Popup Loại 2 (web) · Popup chặn (app) | Mở màn, bản ghi hoặc khối không có quyền xem | "Bạn không có quyền xem thông tin này. Liên hệ quản trị viên để được cấp quyền." | GR-28 · GR-26 |
| E-common-012 | Popup chặn (app) | Quyền tài khoản vừa thay đổi | "Quyền của tài khoản vừa thay đổi. Tải lại để áp dụng." | GR-26 |

Câu gốc tài liệu app (2.17, 2.18) đã viết lại theo design.md › Copy động (bỏ "Vui lòng"):
"Phiên đăng nhập hết hạn. Vui lòng đăng nhập lại để tiếp tục." → E-common-010 ·
"Bạn không có quyền xem thông tin này. Vui lòng liên hệ quản trị viên." → E-common-011 ·
"Tài khoản của bạn vừa được thay đổi phân quyền. Vui lòng tải lại để áp dụng thay đổi mới." → E-common-012 ·
"Không thể kết nối. Vui lòng kiểm tra mạng và thử lại." → E-common-009.
