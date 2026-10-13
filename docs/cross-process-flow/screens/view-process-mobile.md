# Xem quy trình trên Delta Super App

> Flow `view-process-mobile` · thiết bị `mob` · bảng chép từ `docs/cross-process-flow/html-wireframe/view-process-mobile.html` ngày 2026-10-13. Giao diện là frame Figma; bảng 5 cột là hợp đồng — sửa qua `/figma-sync` hoặc `/cr`.

## Screen: record-detail — App — màn chi tiết có thẻ quy trình

- **screenId:** 1.1 · mob
- **Figma:** [1.1 · mob](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5600-159935)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Thẻ quy trình | Card | Click | • Xem CMP-09 Mobile: tên luồng là chính ("Sửa chữa xe Delta"), dòng tóm tắt là phụ: thanh tiến độ · "Xong x/y bước · n nhánh phát sinh" · "Bước trước / Phát sinh từ" (FR-cross-process-flow-005, -021)<br>• Không thuộc quy trình hoặc luồng độc lập chưa có nhánh → không có thẻ (D1)<br>• Chạm thẻ → sheet đang tải [1.2] · Loading rồi sheet sơ đồ [1.2]; tải lỗi → [1.1] · Load error<br>• Thẻ hiện trong tối đa 2 giây, không bắt màn chi tiết chờ (NFR-cross-process-flow-002); đang tải → skeleton thẻ [1.1] · Loading |
| 2 | Header màn chi tiết | Header | Click | • ← quay lại · mã bản ghi · icon lịch sử Xem CMP-08 (Mobile); thuộc nghiệp vụ |
| 3 | Nút tạo nghiệp vụ tiếp theo | Button | Click | • Chỉ có ở nghiệp vụ có màn trên app (cột "Có trên app" của bảng liên quy trình), cùng điều kiện D6 như web; nút cố định đáy (thumb zone) (FR-cross-process-flow-012)<br>• Lỗi E-cross-process-flow-001 / -003 khi gửi: sheet lỗi Loại 2 (GR-15 Mobile), nội dung như [3.2] / [3.3] |

### Trạng thái: Load error — App — thẻ quy trình tải lỗi

- **Figma:** [1.1 · mob · Load error](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5600-160682)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Thẻ lỗi | Banner | ReadOnly | • "Không tải được quy trình." thay chỗ thẻ quy trình; màn chi tiết vẫn dùng bình thường (FR-cross-process-flow-005) |
| 2 | Thử lại | Button | Click | • Vùng chạm tối thiểu 44 (design.md › Touch Targets); được → [1.1] |

### Trạng thái: Loading — App — thẻ quy trình đang tải

- **Figma:** [1.1 · mob · Loading](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5600-160508)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Skeleton thẻ quy trình | Skeleton | ReadOnly | • Theo GR-12 (Mobile): skeleton theo hình thẻ thật, có shimmer; tải xong chuyển mờ sang thẻ [1.1] (FR-cross-process-flow-005)<br>• Màn chi tiết dùng được ngay; tải lỗi → [1.1] · Load error |

## Screen: process-diagram — App — sheet sơ đồ

- **screenId:** 1.2 · mob
- **Figma:** [1.2 · mob](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5600-160887)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Sheet sơ đồ | BottomSheet | Click | • Xem CMP-09 Mobile: mở từ đáy, che gần hết màn; header tên luồng + mã + trạng thái quy trình + ×<br>• Vuốt xuống, chạm nền hoặc × → đóng, về [1.1] (conventions — BottomSheet)<br>• Hiện đủ trong tối đa 2 giây (NFR-cross-process-flow-001) |
| 2 | Card tóm tắt | Card | ReadOnly | • Xem CMP-09 Mobile: thanh tiến độ + số bước theo trạng thái ("4 xong · 2 đang chờ/làm · 1 chưa tạo"); không lặp dòng "Xong x/y bước" (đã có ở thẻ [1.1]) |
| 3 | Cây dọc | Tree | Click | • Cây rẽ nhánh dọc, thẻ cùng dạng web (R7, R16, R10); vuốt ngang khi cây rộng hơn màn (FR-cross-process-flow-021)<br>• Mở từ màn chi tiết: thẻ "Ở đây" được chọn sẵn (viền đậm) — sheet bước chưa tự mở để không che cây<br>• Chụm hai ngón để thu phóng, vuốt để kéo; không có nút thu phóng (FR-cross-process-flow-006, -021)<br>• Chạm thẻ → sheet bước [4.1], [1.3]–[1.6] |
| 4 | Chip Điều kiện x/y | Chip | Click | • Xem CMP-09 Mobile: chạm chip trên đường → tooltip như web [1.2] (mỗi điều kiện 1 dòng ✓ / ○ kèm mã nguồn + "Bước trước khác (đường riêng): …"), neo dưới chip, rộng tối đa bằng vùng cây<br>• Chạm ra ngoài hoặc chạm lại chip để đóng; không mở sheet bước<br>• Cây mẫu LSC-0941 chưa có bước nào ≥2 bước trước cùng vào — chip chỉ hiện khi có |

### Trạng thái: Loading — App — sheet sơ đồ đang tải

- **Figma:** [1.2 · mob · Loading](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5600-161816)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Sheet đang tải | BottomSheet | ReadOnly | • Theo GR-12 (Mobile): "Đang tải sơ đồ…" + khung xám theo hình thẻ<br>• Tải xong → [1.2]; lỗi → [1.2] · Load error |

### Trạng thái: Load error — App — sheet sơ đồ lỗi

- **Figma:** [1.2 · mob · Load error](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5600-161987)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Khối lỗi trong sheet | Label | ReadOnly | • Tiêu đề "Không tải được sơ đồ." + câu E-common-008 "Đã xảy ra lỗi. Thử lại sau." hoặc E-common-009 "Mất kết nối. Kiểm tra mạng và thử lại." (FR-cross-process-flow-006)<br>• Override GR-15: lỗi tại chỗ thay toast (spec Mục 10) |
| 2 | Thử lại | Button | Click | • Nút chính dưới câu mô tả; chạm → [1.2] · Loading |

### Trạng thái: Update banner — App — sheet sơ đồ có banner

- **Figma:** [1.2 · mob · Update banner](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5600-162173)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Banner cập nhật | Banner | ReadOnly | • Theo GR-27 (Mobile): ngay dưới header sheet, "Quy trình vừa có cập nhật." (FR-cross-process-flow-020)<br>• Hiện banner tối đa 2 giây sau khi bản ghi đổi (NFR-cross-process-flow-003) |
| 2 | Tải lại | Button | Click | • Tải lại cây, giữ bước đang chọn → [1.2] |

## Screen: step-sheet — App — sheet bước

- **screenId:** 4.1 · mob
- **Figma:** [4.1 · mob](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5600-162600)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Sheet bước | BottomSheet | ReadOnly | • Chồng lên sheet sơ đồ; đầu sheet: tên, mã, pill trạng thái có viền, nhãn đặt bên phải, không nền màu (CMP-09 Mobile)<br>• Không header riêng, không ×: dòng đầu "‹ Sơ đồ quy trình" (Button Ghost LG) hoặc vuốt xuống / chạm nền → về sheet sơ đồ [1.2] (CMP-09 Mobile) |
| 2 | Lịch sử hoạt động | List | ReadOnly | • Theo CMP-08: 5 dòng mới nhất + "Xem tất cả" (mẫu có 2 dòng vì bản ghi mới có 2 hoạt động) |
| 3 | Mở màn hình chi tiết | Button | Click | • Nút chính full width cố định đáy; đẩy màn mới, Back về màn trước, sheet đã đóng (FR-cross-process-flow-010)<br>• Chỉ có nút khi app có màn chi tiết của loại bản ghi đó (hiện có Đơn mua HHDV, Lệnh sửa chữa, Báo cáo sự cố); loại khác: sheet vẫn có lịch sử, không có nút (FR-cross-process-flow-009)<br>• Bản ghi vừa bị thu quyền: Theo GR-26 popup chặn E-common-011 "Bạn không có quyền xem thông tin này. Liên hệ quản trị viên để được cấp quyền.", nút Quay lại về sheet sơ đồ<br>• Bản ghi đã bị xoá: sheet lỗi Loại 2 E-cross-process-flow-004 + Tải lại sơ đồ, nội dung như [1.9] |

## Screen: step-not-created — App — sheet bước chưa tạo

- **screenId:** 1.3 · mob
- **Figma:** [1.3 · mob](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5600-163096)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Sheet bước chưa tạo | BottomSheet | ReadOnly | • Mã N/A (GR-10), "Chưa tạo"; "Chưa có hoạt động. Bước này chưa được tạo." (D2)<br>• Không có lịch sử, không có nút |

## Screen: branch-point — App — sheet ngã rẽ

- **screenId:** 1.4 · mob
- **Figma:** [1.4 · mob](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5600-163629)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Sheet ngã rẽ | BottomSheet | ReadOnly | • Tên "Chưa xác định nơi sửa", dòng phụ = điều kiện ("Tuỳ nơi sửa"), chip chờ theo điều kiện khai ở bảng liên quy trình (Delta: "Chờ chọn gara", Vàng)<br>• Khối "Hướng có thể đi" lấy từ bảng liên quy trình (D5, R6) + câu "Chốt nơi sửa khi phê duyệt báo giá thì ngã rẽ thành nhánh thật."<br>• Không có lịch sử, không có nút |

## Screen: debt-step — App — sheet công nợ

- **screenId:** 1.6 · mob
- **Figma:** [1.6 · mob](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5600-164169)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Sheet công nợ | BottomSheet | ReadOnly | • Tên "Công nợ", dòng phụ tên NCC, chip trạng thái bước (R8, FR-cross-process-flow-004)<br>• Khối "Chứng từ": dòng "Công nợ {Tên NCC}" + chip "Chưa đối soát" (theo component CMP-09)<br>• KHÔNG có nút "Mở bảng công nợ" — Delta Super App không có màn Bảng công nợ (OQ-2 chốt 12/10/2026) |

## Screen: step-no-permission — App — sheet bước không có quyền

- **screenId:** 1.5 · mob
- **Figma:** [1.5 · mob](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5600-164723)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Sheet không có quyền | BottomSheet | ReadOnly | • E-common-011 "Bạn không có quyền xem thông tin này. Liên hệ quản trị viên để được cấp quyền." tại chỗ; ẩn lịch sử và nút (FR-cross-process-flow-009, NFR-cross-process-flow-004)<br>• Override GR-26 như web (spec Mục 10)<br>• Quyền theo phân quyền xem của nghiệp vụ ứng với bước, như nhau cho mọi người dùng kể cả Lái xe; lý do phát sinh vẫn hiện nếu có (FR-cross-process-flow-009) |
