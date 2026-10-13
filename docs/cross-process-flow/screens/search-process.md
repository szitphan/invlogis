# Tra cứu danh sách Quy trình

> Flow `search-process` · thiết bị `web` · bảng chép từ `docs/cross-process-flow/html-wireframe/search-process.html` ngày 2026-10-13. Giao diện là frame Figma; bảng 5 cột là hợp đồng — sửa qua `/figma-sync` hoặc `/cr`.

## Screen: process-list — Danh sách Quy trình

- **screenId:** 2.1 · web
- **Figma:** [2.1 · web](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5600-132884)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Menu {Module} › Quy trình | Menu | Click | • Xem CMP-11 — mục "Quy trình" trong menu mỗi module<br>• Chỉ hiện với người được Admin cấp quyền theo module (FR-cross-process-flow-019)<br>• Luồng liên module hiện ở danh sách của cả 2 module (FR-cross-process-flow-015)<br>• Chỉ gồm quy trình thuộc chi nhánh người dùng được phân quyền dữ liệu (FR-cross-process-flow-015)<br>• Đang tải → [2.1] · Loading; tải lỗi → khối lỗi [2.1] · Load error; không có quyền menu mà mở thẳng đường dẫn → [2.1] · No permission |
| 2 | Ô tìm | Textbox | Text | • Theo GR-09: tìm được mã quy trình + mã của bất kỳ bản ghi trong cây; không tìm theo Luồng, Trạng thái, Chi nhánh (dùng bộ lọc)<br>• Tìm mã quy trình, mã yêu cầu hoặc mã bản ghi chứa chuỗi đã gõ ở bất kỳ vị trí nào (vd "0410" ra quy trình chứa PXK-0410), không phân biệt hoa thường, chạy sau khi ngừng gõ 0,3 giây; kết quả trong tối đa 1 giây (FR-cross-process-flow-016, NFR-cross-process-flow-009)<br>• Dưới 3 ký tự: chưa tìm, không báo lỗi (D7); không ra kết quả → [2.1] · No search results<br>• Placeholder "Tìm mã quy trình, mã yêu cầu, mã bản ghi…" (nêu đúng trường tìm được) |
| 3 | Bộ lọc | Button | Click | • Xem CMP-05 — Filter Drawer. Trường lọc: Luồng (chọn nhiều) · Trạng thái (chọn nhiều) · Chi nhánh (chọn) · Cập nhật lần cuối (khoảng ngày, chỉ ngày) (FR-cross-process-flow-017, GR-20)<br>• Không có giá trị mặc định, không có phụ thuộc giữa các trường<br>• Badge trên nút = số điều kiện đang áp dụng |
| 4 | Chip điều kiện lọc | Chip | Click | • Hàng 2 thanh công cụ: mỗi điều kiện 1 chip "[Cột]: [giá trị]"; bấm chip → sửa điều kiện, × → xoá điều kiện đó (CMP-05, design.md › Bộ lọc nâng cao) |
| 5 | Xoá tất cả | Button | Click | • Xoá mọi chip, không xoá từ khoá trong ô tìm; chỉ hiện khi có điều kiện |
| 6 | Số kết quả | Label | ReadOnly | • "n kết quả" căn phải hàng 2 — tổng duy nhất của danh sách sau tìm + lọc (design.md › Bộ lọc nâng cao) |
| 7 | Tuỳ chỉnh cột | Button | Click | • Xem CMP-06: 10 cột theo thứ tự FR-cross-process-flow-015, hiện hết mặc định; cột khoá: Mã quy trình |
| 8 | Xuất ▾ | Button | Click | • Theo GR-19, FR-cross-process-flow-022: PDF hoặc Excel đúng tập dữ liệu đang thấy (sau tìm, lọc, sắp, mọi trang) và đúng các cột đang hiện theo thứ tự đang cấu hình<br>• 1 dòng = 1 quy trình; khối thông tin phụ: Thời gian xuất · Người xuất · Tổng số dòng · Tiêu chí lọc; sheet "DS - Quy trình"; file Export_DanhSach_QuyTrinh_.xlsx; trang in nằm ngang<br>• Ai xem được menu Quy trình của module thì xuất được |
| 9 | Cột Mã quy trình | Label | ReadOnly | • Theo P-mau-ma-quy-trinh (Delta: QT-[Mã chi nhánh]-[YY]-[XXXX]); quy trình dựng từ dữ liệu cũ: QT-[Mã chi nhánh]-LG-[XXXX], Cập nhật lần cuối = ngày chuyển dữ liệu (vd QT-HP-LG-0004)<br>• Cột khoá, không ẩn được |
| 10 | Cột Luồng | Label | ReadOnly | • Tên luồng theo bảng liên quy trình |
| 11 | Cột Bản ghi gốc | Label | ReadOnly | • Tên bước + mã của nút đầu cây |
| 12 | Cột Phương tiện / khách hàng | Link | Click | • Bấm ô → màn chi tiết Phương tiện hoặc Xe của khách hàng (FR-cross-process-flow-018), ngoài feature<br>• Không có thông tin: "-" (GR-10) |
| 13 | Cột Tiến độ | Label | ReadOnly | • "Xong x/y bước" |
| 14 | Cột Nhánh phát sinh | Label | ReadOnly | • Số nhánh phát sinh, căn phải |
| 15 | Cột Bước đang chờ | Label | ReadOnly | • Bước chờ lâu nhất: tên bước · trạng thái (lấy theo bản ghi) · chờ bao lâu; nhiều bước cùng chờ thì thêm dòng "+n bước khác" (FR-cross-process-flow-015)<br>• Chờ bao lâu tính riêng từng bước, từ lúc bước vào trạng thái hiện tại: "n phút" (dưới 1 giờ) · "n giờ" (dưới 24 giờ) · "n ngày"<br>• Quy trình Đã dừng: hiện bước của luồng chính bị từ chối/thu hồi; nhánh phát sinh bị từ chối không làm quy trình dừng nhưng vẫn hiện ở cột này kèm trạng thái (BR-cross-process-flow-002)<br>• Quy trình Đã hoàn thành: "-" (GR-10) |
| 16 | Cột Trạng thái | Badge | ReadOnly | • Đang triển khai · Đã dừng · Đã hoàn thành (FR-cross-process-flow-002), nhãn chữ |
| 17 | Cột Chi nhánh | Label | ReadOnly | • Chi nhánh lúc tạo quy trình (BR-cross-process-flow-004) |
| 18 | Cột Cập nhật lần cuối | Label | ReadOnly | • dd/mm/yyyy hh:mm, căn giữa<br>• Override GR-18: mặc định sắp giảm dần theo cột này (thay thời gian tạo) — lý do: người theo dõi cần thấy quy trình vừa có biến động trước |
| 19 | Dòng quy trình | Row | Click | • Bấm dòng (ngoài ô Phương tiện) → popup sơ đồ ngay trên danh sách, chưa chọn bước nào [2.2] (FR-cross-process-flow-018) |
| 20 | Phân trang | Pagination | Click | • Xem CMP-04, mặc định: trái ô "50 / trang" (25 / 50 / 100), phải Trước · số trang · Sau; không có nhãn tổng (design.md › Phân trang, chốt 12/10/2026)<br>• Mẫu chỉ 46 kết quả nên có 1 trang; theo design.md 1 trang thì ẩn số trang và Trước/Sau — vẽ để minh hoạ vị trí |

### Trạng thái: Empty — Danh sách rỗng

- **Figma:** [2.1 · web · Empty](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5600-144980)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Trạng thái rỗng | Label | ReadOnly | • Theo GR-12: "Chưa có quy trình nào." + "Quy trình tự tạo khi có bản ghi đầu tiên được gửi."<br>• Không có nút Tạo mới — quy trình chỉ tạo tự động (FR-cross-process-flow-001) |
| 2 | Ô tìm, Bộ lọc, Xuất | Button | Click | • Vẫn hiện như màn [2.1] |

### Trạng thái: Loading — Danh sách đang tải

- **Figma:** [2.1 · web · Loading](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5600-137717)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Skeleton bảng | Skeleton | ReadOnly | • Theo GR-12: skeleton theo 10 cột đang hiện (FR-cross-process-flow-015)<br>• Trang 50 dòng hiện trong tối đa 2 giây (NFR-cross-process-flow-009)<br>• Thanh công cụ và bộ lọc dùng được ngay; tải xong → [2.1] / [2.1] · Empty, lỗi → [2.1] · Load error |

### Trạng thái: Load error — Danh sách tải lỗi

- **Figma:** [2.1 · web · Load error](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5600-152243)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Khối lỗi | Label | ReadOnly | • Thay vùng bảng: "Không tải được danh sách." + câu E-common-008 (FR-cross-process-flow-015)<br>• Override GR-15: khối lỗi tại chỗ thay toast — lý do: toast tự ẩn sau 3 giây làm mất nút Thử lại (spec Mục 10)<br>• Giữ thanh công cụ, ô tìm và chip lọc đang chọn |
| 2 | Thử lại | Button | Click | • Tải lại với đúng ô tìm và bộ lọc đang chọn → [2.1] · Loading |

### Trạng thái: No filter results — Lọc không ra kết quả

- **Figma:** [2.1 · web · No filter results](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5600-149822)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Trạng thái không có kết quả | Label | ReadOnly | • Ô tìm trống, bộ lọc ra 0 dòng: "Không có quy trình phù hợp với bộ lọc." (FR-cross-process-flow-017)<br>• Có từ khoá trong ô tìm → dùng câu của [2.1] · No search results<br>• Không có nút Tạo mới |
| 2 | Xoá bộ lọc | Button | Click | • Xoá mọi điều kiện lọc → [2.1] |

### Trạng thái: No permission — Trang không có quyền

- **Figma:** [2.1 · web · No permission](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5600-154664)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Nội dung không có quyền | Label | ReadOnly | • Người không có quyền menu Quy trình mở thẳng đường dẫn danh sách: vùng nội dung hiện câu E-common-011 "Bạn không có quyền xem thông tin này. Liên hệ quản trị viên để được cấp quyền." (FR-cross-process-flow-019)<br>• Menu bên trái không có mục Quy trình; quy tắc chung cho web đang đề xuất thêm (BL-064) |
| 2 | Về trang chủ | Button | Click | • Về trang chủ của người dùng |

### Trạng thái: No search results — Tìm không ra

- **Figma:** [2.1 · web · No search results](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5600-147401)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Trạng thái không có kết quả | Label | ReadOnly | • Theo GR-12: "Không tìm thấy quy trình chứa mã "[mã]"." — [mã] là chuỗi đang gõ<br>• Không có nút Tạo mới |
| 2 | Xoá bộ lọc | Button | Click | • Xoá ô tìm và mọi điều kiện lọc → [2.1] (UC tra cứu 5a2) |

### Trạng thái: Update banner — Danh sách có banner cập nhật

- **Figma:** [2.1 · web · Update banner](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5600-140138)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Banner cập nhật | Banner | ReadOnly | • Theo GR-27, [Đối tượng] = "Danh sách": "Danh sách vừa có cập nhật." đầu vùng nội dung (FR-cross-process-flow-020)<br>• Không tự tải lại; hiện banner tối đa 2 giây sau khi bản ghi đổi (NFR-cross-process-flow-003) |
| 2 | Tải lại | Button | Click | • Tải dữ liệu mới, giữ ô tìm + bộ lọc + trang đang xem, rồi ẩn banner → [2.1] |

## Screen: list-process-diagram — Popup sơ đồ trên danh sách

- **screenId:** 2.2 · web
- **Figma:** [2.2 · web](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5600-142559)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Popup sơ đồ | Popup | Click | • Như [1.2] nhưng mở từ danh sách: chưa chọn bước nào, panel đóng, không có ghim "Ở đây" (FR-cross-process-flow-006, -018)<br>• Chọn bước → panel như [1.2] (có bản ghi), [1.3] chưa tạo, [1.4] ngã rẽ, [1.5] không có quyền, [1.6] công nợ, [1.7] có bản ghi trước |
| 2 | Đóng × | Button | Click | • Về danh sách [2.1], giữ ô tìm và bộ lọc |
| 3 | Chip Điều kiện x/y | Chip | Click | • Như [1.2] (Xem CMP-09 #4): bấm chip → tooltip điều kiện neo dưới chip; popup vẫn chưa chọn bước nào |
