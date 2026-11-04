---
type: research
feature: fleetio-parts-purchasing-fuel
updated: 2026-11-03
---

# Phụ tùng, mua hàng, nhiên liệu — Use cases

## Use cases

| UC | Tên | Actor | FR | Màn | Lỗi | OQ |
|---|---|---|---|---|---|---|
| UC-manage-part | Khai phụ tùng và kho | Nhân viên kho | 001, 002, 008, 026, 044 | 1.1 | E-002, E-006, E-024 | OQ-2, OQ-11, OQ-16, OQ-19, OQ-23 |
| UC-change-valuation | Đổi phương pháp tính giá tồn | Quản trị tài khoản | 008, 045 | 1.8 | E-035, E-036 | OQ-2, OQ-11, OQ-28 |
| UC-adjust-stock | Điều chỉnh, chuyển kho | Nhân viên kho | 003–007 | 1.1, 1.2, 1.3, 1.4, 1.5 | E-007, E-008, E-031 | — |
| UC-bulk-count | Kiểm kê hàng loạt | Nhân viên kho | 025, 041 | 1.6, 1.7 | E-010, E-029 | — |
| UC-create-po | Lập và duyệt đơn | Người lập, Người duyệt | 009–011, 030–032, 039 | 2.1, 2.3, 2.11 | E-001, E-011, E-012, E-026 | OQ-3, OQ-8, OQ-20, OQ-25 |
| UC-review-po | Sao chép, in, xem lịch sử đơn | Người lập, Nhân viên kho | 032, 037 | 2.9, 2.10, 2.12 | E-030 | OQ-22 |
| UC-receive-po | Nhận hàng | Nhân viên kho | 012, 013 | 2.1, 2.4, 2.5 | E-013, E-014 | OQ-4, OQ-11 |
| UC-return-close-po | Trả hàng, đóng đơn | Nhân viên kho | 028–030 | 2.6, 2.7, 2.8, 2.9 | E-015, E-025, E-027 | OQ-10, OQ-21 |
| UC-issue-part | Xuất phụ tùng cho lệnh | Nhân viên xưởng | 014, 027, 038 | Sửa lệnh | E-003, E-005, E-009 | OQ-1, OQ-9, OQ-12 |
| UC-manage-vendor | Khai nhà cung cấp, tìm xưởng | Nhân viên xưởng | 015, 016, 035, 040 | 2.2, 2.13 | E-021, E-022 | OQ-15, OQ-24 |
| UC-log-fuel | Ghi phiếu dầu | Lái xe, Nhân viên cây dầu | 017–022, 033, 036, 042, 043 | 3.1, 3.3, 3.4 | E-004, E-016–E-019, E-028 | OQ-5, OQ-14, OQ-18, OQ-26 |
| UC-review-fuel | Lọc và đối soát phiếu dầu | Quản lý cây dầu | 020, 034, 043 | 3.2, 3.3, 3.5 | E-020, E-028 | OQ-26 |

Số FR, lỗi viết tắt, đầy đủ có tiền tố `fleetio-parts-purchasing-fuel`. Mã case dẫn về SRS Mục 6A. FR-023 Phiên sạc ngoài phạm vi theo yêu cầu user nên không có UC; FR-024 Công cụ chỉ theo tài liệu nên chưa có UC.

## UC-manage-part — Khai phụ tùng và kho

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Tạo kho trong cài đặt | Kho hiện trong danh mục |
| 2 | Tạo phụ tùng: mã, đơn giá | Trang phụ tùng, chưa có kho |
| 3 | Bật phụ tùng tại kho, nhập tồn đầu | Hiện thẻ tồn, sổ loại Initial |
| 4 | Thêm nhà cung cấp, giá trong Purchase History | Trang phụ tùng vẽ biểu đồ giá |

**Nhánh:** 1a Trùng tên kho: E-fleetio-parts-purchasing-fuel-006. 2a Giá gõ lúc tạo không được lưu: E-fleetio-parts-purchasing-fuel-024. 2b Form không có thay thế, tương thích xe (K24). 3a Chưa có quyền kho: E-fleetio-parts-purchasing-fuel-002. 3b Điểm đặt lại 0 lưu được (S4); tồn 0 thì Out of Stock (S5). 5a Lưu trữ phụ tùng: "Archive" mờ với PT-A, chưa chạy (K26).

## UC-change-valuation — Đổi phương pháp tính giá tồn

Bước 1, 2 `Chạy`; bước 3 trở đi theo câu chữ màn, chưa chạy.

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Mở Inventory Valuation Method | 4 radio có mô tả, không có nút Save |
| 2 | Chọn phương pháp khác | Hiện cảnh báo, điều kiện, ô tích, Activate xám; chưa lưu gì |
| 3 | Dọn dữ liệu, tích ô nhận thức | Activate mở khi đủ điều kiện |
| 4 | Activate | Tồn nhận giá Unit Cost, tồn Archived về 0 |

**Nhánh:** 2a Tải lại trang: vẫn Static Pricing. 3a Thiếu Unit Cost, còn lệnh dở: E-fleetio-parts-purchasing-fuel-035. 3b Lệnh dở không hoàn thành được vì dòng công: E-fleetio-parts-purchasing-fuel-036, chặn cả việc đổi (K40, K43). 4a FIFO, LIFO: dòng phụ tùng lệnh cũ không sửa được nữa. 4b Đổi lại: câu chữ ghi không đảo được, chưa kiểm chứng.

## UC-adjust-stock — Điều chỉnh, chuyển kho

`Chạy`. Bản trước ghi theo tài liệu hãng, chưa chạy.

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Chọn điều chỉnh, gõ số biến động hoặc số mới | Hai ô liên động, chấp nhận số lẻ |
| 2 | Chọn lý do trong 11 giá trị, ghi chú | Save mở khi có lý do |
| 3 | Lưu | Ghi sổ loại Manual, cập nhật tồn và nhãn |
| 4 | Hoặc chuyển: số lượng, kho đích trong danh sách kho còn lại | Trừ một kho, cộng kho khác, sổ loại Transfer |

**Nhánh:** 1a Giảm quá tồn: lưu được, tồn âm, E-fleetio-parts-purchasing-fuel-007. 4a Tồn từ 0 trở xuống: nút chuyển khoá. 4b Chuyển quá tồn: cắt về tồn hiện có, vẫn báo thành công, E-fleetio-parts-purchasing-fuel-008.

## UC-bulk-count — Kiểm kê hàng loạt

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Mở Bulk Manage, chọn tab kho | Bảng Aisle, Row, Bin, Active?, Track Inventory, Current Qty, Last Quantity Update |
| 2 | Sửa ô Current Qty | Tự lưu, "All changes saved", sổ loại Bulk Update, không hỏi lý do |
| 3 | Print Worksheet để đếm tay | Tự tải PDF theo kho đang chọn, có ô New Qty trống; không mở tab |

**Nhánh:** 2a Gạt Active khi có đơn: không tắt, E-fleetio-parts-purchasing-fuel-010. 2b Về 0 với điểm đặt lại 0: Out of Stock, danh sách tô đỏ tổng (S5, S9). 3a Một cú bấm ra 3 file: E-fleetio-parts-purchasing-fuel-029.

## UC-create-po — Lập và duyệt đơn

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Chọn nhà cung cấp, kho | Chỉ hiện nhà cung cấp có Parts; mở khối dòng hàng |
| 2 | Thêm dòng, số lượng | Hiện tồn tại kho của đơn; lấy đơn giá, tính tổng, giảm giá, phí, thuế |
| 3 | Save as Draft hoặc Save & Approve | Lưu; ghi người tạo |
| 4 | Approve | Ghi người duyệt, một cú bấm, không hộp xác nhận |

**Nhánh:** 1a Chưa chọn đủ: E-fleetio-parts-purchasing-fuel-001. 2a Phụ tùng chưa bật ở kho: xám, có khoá. 2b Dòng trùng: E-fleetio-parts-purchasing-fuel-011. 2c Ô Shipping sai: E-fleetio-parts-purchasing-fuel-012. 3a Không có quyền: Submit for Approval (`Docs`, lượt 3 không chạy được, D32). 4a Từ chối: Rejected (`Docs`). 4b Automation tự duyệt dưới ngưỡng (`Xem`). 4c Đơn 0 dòng: Approve khoá. 4d Dòng số lượng 0: duyệt được. 5a Lùi: Save as Draft trong form Edit ở Approved, mất Approved By. 5b Copy: xem UC-review-po. 5c Sửa ở Purchased: khoá nhà cung cấp, kho, không thêm bớt dòng; Pending theo số đặt mới, không cảnh báo (D25, D26). 5d Unmark as Purchased: Pending không giảm, E-fleetio-parts-purchasing-fuel-026.

**Tiêu chí số đang về:** đơn chưa Edit: Draft, Approved tính 0, từ Purchased mới tính (D22–D24). Đơn Draft đã Edit và lưu: tính ngay, E-fleetio-parts-purchasing-fuel-032 (D40, D41).

## UC-review-po — Sao chép, in, xem lịch sử đơn

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Menu đơn, Make a Copy | Form mới số kế tiếp, chép nhà cung cấp, kho, dòng, số đặt, giá, chiết khấu; không chép số đã nhận |
| 2 | Save as Draft | "Purchase Order was successfully created", đơn Draft |
| 3 | Menu đơn, Print | Tab mới "Preparing your PDF...", PDF một trang |
| 4 | Menu đơn, View Record History | Hộp liệt kê ngày, người, thay đổi; lọc theo khoảng ngày |

**Nhánh:** 3a Đơn đã Unmark: PDF vẫn in Purchase Date, Purchased By (D35). 3b Tiền kiểu US khác web: E-fleetio-parts-purchasing-fuel-030. 4a Số nhận không thấy trong phần đọc được (D20, OQ-22).

## UC-receive-po — Nhận hàng

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Mark as Purchased | Ghi người mua, nút chuyển thành Receive |
| 2 | Receive: nhập số, chọn nơi đến | Hiện đã nhận, đã đặt |
| 3 | Xác nhận | Đổi trạng thái, tồn tăng, ghi sổ |

**Nhánh:** 1a Unmark as Purchased: về Approved, không hỏi. 2a Vào lệnh đang có: nhập kho trước, mở form lệnh, trừ khi lưu lệnh (`Chạy` D14; `Docs` chỉ với Static Pricing). 2b Vào lệnh mới, huỷ form: hàng ở lại kho, đơn thành Full (`Chạy` D15). 2c Nhận vượt: không chặn, E-fleetio-parts-purchasing-fuel-013. 2d Gõ số âm: thành dương, E-fleetio-parts-purchasing-fuel-014.

## UC-return-close-po — Trả hàng, đóng đơn

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Make Adjustment ở Full: tick dòng, nhập số âm | Bảng Item, Total Received, Total Ordered, Adjustment; nút mờ tới khi tick |
| 2 | Lưu | Sổ giảm, tồn giảm, về Partial, "Received in Full By" vẫn còn |
| 3 | Close, xác nhận | Closed, ghi Closed By |

**Nhánh:** 1a Âm quá số đã nhận: cắt, không báo, E-fleetio-parts-purchasing-fuel-015. 3a Còn thiếu: vẫn đóng được, không ghi lý do. 4a Sửa đơn giá sau đóng: được, E-fleetio-parts-purchasing-fuel-025. 4b Mở lại: không có nút. 4c Huỷ: không có nút; Delete chưa bấm. 4d Make Adjustment sau đóng: số nhận và tồn giảm, vẫn Closed, không hỏi lý do, E-fleetio-parts-purchasing-fuel-027. 2a Tăng số đặt ở Full: vẫn Full, không có Receive, E-fleetio-parts-purchasing-fuel-033.

## UC-issue-part — Xuất phụ tùng cho lệnh

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Tìm phụ tùng trên lệnh | Hiện tồn từng kho |
| 2 | Chọn kho, số lượng, đơn giá, đầu việc, ghi chú | Báo sẽ điều chỉnh tồn |
| 3 | Lưu lệnh | Trừ ngay, ghi sổ |
| 4 | Hoàn thành lệnh | Sổ không có dòng mới, sinh Service Entry, Edit khoá |

**Nhánh:** 2a Chọn None: không trừ kho. 2b Vượt tồn: không chặn, E-fleetio-parts-purchasing-fuel-003. 3a Sửa số lượng: sổ ghi bù. 3b Xoá dòng: sổ cộng lại. 3c Trang chi tiết lệnh, Service Entry lệch tiền: E-fleetio-parts-purchasing-fuel-005. 4a Thiếu Started At, Start Odometer: E-fleetio-parts-purchasing-fuel-009. 5a Mở lại: sổ không đổi, mất liên kết Service Entry.

## UC-manage-vendor — Khai nhà cung cấp

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Gõ tên trong ô chọn, chọn Create; hoặc từ danh sách | Mở form, phân loại theo ngữ cảnh |
| 2 | Nhập địa chỉ, liên hệ, phân loại | Bắt buộc tên, địa chỉ, thành phố, tỉnh, mã bưu chính, quốc gia; phân loại không bắt buộc |
| 3 | Lưu | Điền vào ô chọn ban đầu |
| 4 | Mở trang nhà cung cấp | Tab Overview, Fuel Entries, Purchase Orders theo phân loại |

**Nhánh:** 2a Thiếu trường: E-fleetio-parts-purchasing-fuel-021. 2b Enter ở ô Country: lưu sớm, E-fleetio-parts-purchasing-fuel-022. 1a Tìm xưởng qua Find Shops: tìm, tick được; Add Vendor không bấm (N7, N8). 4a Rating là số, hiện "Rating not available", nguồn chưa rõ (N10, N13–N15). 4b Network Status: Invite không bấm (N11).

## UC-log-fuel — Ghi phiếu dầu

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Chọn xe | Mở số đồng hồ, số lít, đơn giá; hiện số gần nhất |
| 2 | Nhập, chọn loại dầu, nhà cung cấp có Fuel, cờ, ảnh | Tính tiền |
| 3 | Lưu | Trang phiếu có quãng đường, tiêu hao, chi phí, chênh so với lần trước; số đồng hồ đẩy nhắc; có nhà cung cấp thì hiện bản đồ |

**Nhánh:** 3a Phiếu đầu: N/A. 3b Partial: cộng dồn sang phiếu đầy. 3c Reset: phiếu sau Usage N/A nhưng vẫn có tiêu hao. 3d Personal: vẫn tính tiêu hao, chi phí. 3e Void: bắt buộc số đồng hồ, E-fleetio-parts-purchasing-fuel-018; đồng hồ xe không đổi; vẫn cộng vào thẻ tổng, E-fleetio-parts-purchasing-fuel-028. 3f Vượt dung tích đã khai: Capacity Alert (`Chạy`), E-fleetio-parts-purchasing-fuel-017 khi sửa phiếu. 3g Số đồng hồ lùi cùng ngày: E-fleetio-parts-purchasing-fuel-016. 3h Lùi ngày, số cao: E-fleetio-parts-purchasing-fuel-019. 3i Giao dịch từ thẻ, có định vị: Vendor Location Alert (`Docs`, lượt 3 không chạy được). 3j Có chọn nhà cung cấp: tạo vị trí xe, form không báo (F25).

## UC-review-fuel — Lọc và đối soát phiếu dầu

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Mở Fuel History | Date 30 ngày gần nhất, có biểu tượng khoá; thẻ tổng |
| 2 | Chọn Vendor, Vehicle, Vehicle Group; hoặc Filters, Add Filter, Apply | Danh sách và thẻ tổng tính lại |
| 3 | Lọc Fuel Alert Type | Ba loại; Fuel Capacity Alert ra các phiếu vượt, kể cả phiếu đã sửa nhỏ lại |
| 4 | Đối chiếu tổng | Thẻ tổng tính cả Void, Personal |

**Nhánh:** 2a Xoá điều kiện: áp ngay. 2b Ô Vendor liệt kê mọi nhà cung cấp, khác form phiếu. 4a Tổng tiền lệch 100 lần: E-fleetio-parts-purchasing-fuel-020; đối chiếu ở trang chi tiết xe (T6). 4b Void làm tổng cao hơn thực tế: E-fleetio-parts-purchasing-fuel-028.
