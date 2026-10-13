# Tạo nghiệp vụ tiếp theo, chặn thu hồi/xoá

> Flow `create-next-step` · thiết bị `web` · bảng chép từ `docs/cross-process-flow/html-wireframe/create-next-step.html` ngày 2026-10-13. Giao diện là frame Figma; bảng 5 cột là hợp đồng — sửa qua `/figma-sync` hoặc `/cr`.

## Screen: new-record-detail — Màn chi tiết bản ghi mới

- **screenId:** 3.1 · web
- **Figma:** [3.1 · web](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5600-157912)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Dòng quy trình | Row | Click | • Như [1.1]; bước mới gắn "Ở đây" khi người tạo vào màn chi tiết (FR-cross-process-flow-003)<br>• "Bước trước: Sửa chữa LSC-0930"; tóm tắt cập nhật số bước ("Xong 5/9 bước · 3 nhánh phát sinh")<br>• Ghi nhận gửi và thêm bước cùng thành công hoặc cùng không; cây không nhận thì bản ghi giữ nháp (FR-cross-process-flow-003) |
| 2 | Thẻ bước mới trên sơ đồ | Card | Click | • Bản ghi gửi thành công → bước Đang triển khai nối về bản ghi tạo ra nó (R1, FR-cross-process-flow-003, -004)<br>• Bước khai "nhiều bản ghi" (Xuất kho): YC-PXK-0418 thành bước anh em thứ 3 cạnh PXK-0410, PXK-0415, không ghi "lần 1/2" (BR-cross-process-flow-008, FR-cross-process-flow-013) |
| 3 | Trạng thái bản ghi | Badge | ReadOnly | • Trạng thái của nghiệp vụ (vd "Chờ phê duyệt")<br>• Chưa được duyệt nên tiêu đề và thẻ bước mang mã yêu cầu YC-PXK-0418; duyệt xong đổi sang mã bản ghi (BR-cross-process-flow-012) |
| 4 | Toast gửi thành công | Toast | ReadOnly | • Theo toast của nghiệp vụ được tạo (CMP-01); liên quy trình không tự gửi thông báo (BR-cross-process-flow-010) |

## Screen: step-already-requested — Popup E-cross-process-flow-001

- **screenId:** 3.2 · web
- **Figma:** [3.2 · web](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5600-158266)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Popup lỗi | Popup | ReadOnly | • E-cross-process-flow-001, GR-15 Loại 2 Popup, không có Thử lại (FR-cross-process-flow-013)<br>• Đang chờ: "Bước [Tên bước] đã có yêu cầu khác đang chờ phê duyệt. Chờ yêu cầu đó được xử lý rồi gửi lại." — [Tên bước] = bước khai "1 bản ghi" đang gửi<br>• Đã xong: "Bước [Tên bước] đã hoàn thành với [mã]. Không gửi thêm được."; gửi lại bản ghi Đã thay thế cũng chặn bằng lỗi này (BR-cross-process-flow-011)<br>• Hai người cùng gửi thì chỉ người gửi trước được nhận; bản cũ đang Đã thu hồi/từ chối thì không chặn — bản mới thay thế (xem [1.7])<br>• Tiêu đề popup "Không thể gửi"; app: sheet lỗi Loại 2 cùng nội dung (FR-cross-process-flow-012) |
| 2 | Đóng | Button | Click | • Đóng popup, form giữ nguyên, bản nháp giữ lại (FR-cross-process-flow-013)<br>• Tải lại màn bản ghi trước thì nút tạo ẩn theo điều kiện của nghiệp vụ (UC tạo nghiệp vụ 5a2) |

## Screen: has-child-step — Popup E-cross-process-flow-002

- **screenId:** 3.4 · web
- **Figma:** [3.4 · web](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5600-158620)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Popup lỗi | Popup | ReadOnly | • E-cross-process-flow-002, GR-15 Loại 2 Popup, không có Thử lại (FR-cross-process-flow-014)<br>• Thu hồi: "Không thể thu hồi vì đã có [Danh sách bước] tạo từ bản ghi này." · Xoá: tiêu đề "Không thể xoá", câu "Không thể xoá vì đã có [Danh sách bước] tạo từ bản ghi này."<br>• [Danh sách bước] = tối đa 2 bước kèm mã, thêm "và n bước khác" khi nhiều hơn (vd LSC-0930 có 5 bước con)<br>• Hiện chưa nghiệp vụ nào cho thu hồi/xoá khi đã có bước con (spec Mục 11 — giả định) |
| 2 | Đóng | Button | Click | • Về màn chi tiết [1.1], bản ghi giữ nguyên trạng thái |

## Screen: source-revoked — Popup E-cross-process-flow-003

- **screenId:** 3.3 · web
- **Figma:** [3.3 · web](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5600-158974)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Popup lỗi | Popup | ReadOnly | • E-cross-process-flow-003, GR-15 Loại 2: bản ghi nguồn vừa bị thu hồi trong lúc gửi — thu hồi thắng (FR-cross-process-flow-003)<br>• Câu: "Không thể gửi vì [Tên bước] [mã] vừa bị thu hồi. Bản nháp đã được giữ."<br>• Bản ghi không được ghi nhận gửi, cây không đổi; app: sheet lỗi Loại 2 cùng nội dung |
| 2 | Giữ bản nháp | Button | Click | • Nút chính: đóng popup, bản nháp giữ lại chờ bản ghi nguồn được gửi lại |
| 3 | Xoá bản nháp | Button | Click | • Nút phụ kiểu nguy hiểm; Xem CMP-03 để xác nhận rồi xoá bản nháp |
