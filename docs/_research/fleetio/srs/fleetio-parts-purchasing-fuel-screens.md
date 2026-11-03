---
type: research
feature: fleetio-parts-purchasing-fuel
updated: 2026-11-03
---

# Phụ tùng, mua hàng, nhiên liệu — Màn hình thật

Ảnh chụp từ tài khoản dùng thử ngày 02/11/2026 và 03/11/2026, dùng nội bộ để phân tích. Mã lỗi và mã case dẫn về SRS Mục 6 và 6A.

## 1.1 Chi tiết phụ tùng

![Phụ tùng](images/part-detail.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Đầu trang | Chữ | — | Mã, Category, Manufacturer, Mfr. Part Number, UPC, Unit Cost |
| 2 | Tab Overview, Inventory Activity, Work Order Activity, Purchase History | Tab | — | — |
| 3 | Locations | Khối | — | Mỗi kho một thẻ; Manage bật tắt kho |
| 4 | Thẻ kho | Số | — | Current Qty, Reorder Point, Pending PO Qty, WO Current Qty; 4 nút chỉnh, chuyển, đặt mua, menu (Edit, View History); Watch. Nhãn Low Stock số màu cam, Out of Stock khoá nút chuyển |
| 5 | Details | Khối | — | Thông tin phụ tùng, bảo hành |

## 1.2 Sổ kho

![Sổ kho](images/inventory-activity.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Lọc Adjusted By, Part Location, Adjustment Type | Lọc | — | — |
| 2 | Date, Part Location | Cột | — | — |
| 3 | Adjustment Type | Cột | Liên kết | Initial Purchase Order, Work Order, Purchase Order, kèm số chứng từ |
| 4 | Reason, Vendor | Cột | — | — |
| 5 | Adjustment, Previous, New Qty | Cột | Số | Thấy rõ 4, -6, +6 và tồn 4, -2, 4 |
| 6 | Adjusted By, Comment | Cột | — | — |

## 2.3 Form đơn mua

![Form đơn mua](images/po-new.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Số đơn | Số | — | Tự tăng |
| 2 | Vendor, Part Location | Chọn | Bắt buộc | Chọn đủ mới mở dòng hàng |
| 3 | Label | Chọn | — | — |
| 4 | Line Items | Bảng | — | Part, Qty, Unit Cost, Amount |
| 5 | Documents | Tải | — | — |
| 6 | Save as Draft, Save & Approve | Nút | — | Có quyền duyệt thì thấy Save & Approve |

## 2.1 Chi tiết đơn mua

![Đơn mua](images/po-detail.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Nhãn trạng thái | Badge | — | Cạnh tiêu đề |
| 2 | Nút chính | Nút | — | Approve, Mark as Purchased, Receive, Close theo trạng thái |
| 3 | Details | Khối | — | Status, Part Location, Vendor, Created, Approved, Purchased, Received in Full By kèm thời gian |
| 4 | Line Items | Bảng | — | Qty Ordered, Qty Received, Unit Cost, Subtotal |
| 5 | Tổng | Khối | Tiền | Subtotal, Discount, Shipping, Tax, Total |

## 2.2 Danh sách nhà cung cấp

![Nhà cung cấp](images/vendors.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Tab All, Charging, Fuel, Parts, Service, Vehicle, Archived | Tab | — | Theo phân loại |
| 2 | Cột | Bảng | — | Name, Full Address, Phone, Website, Contact, Labels, Rating, Watchers |
| 3 | Find Shops | Nút | — | Tìm xưởng, có Add Vendors; thấy, không mở |

## 3.1 Chi tiết phiếu dầu

![Phiếu dầu](images/fuel-entry.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Thẻ số | Số | — | Volume, Fuel Price, Total, Usage, Fuel Economy, Cost, kèm chênh so với lần trước |
| 2 | Location | Bản đồ | — | Phiếu có nhà cung cấp Fuel hiện bản đồ; phiếu không có ghi "Location is unknown or not available" |
| 3 | Details | Khối | — | Vehicle, Date, Odometer, Vendor, Fuel Type, Fuel Card (ô "No"), Reference, Previous Entry |

## 3.2 Danh sách dầu

![Danh sách dầu](images/fuel-list.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Thẻ tổng | Số | — | Total Fuel Cost, Total Volume, Avg. Economy theo quãng đường, theo giờ, Avg. Cost |
| 2 | Cột | Bảng | — | Vehicle, Date, Vendor, Meter, Usage, Volume, Total, Economy, Cost per Meter, Alerts, Capacity Exception Volume, Location Exception Distance |

## 1.3 Hộp điều chỉnh tồn

![Hộp điều chỉnh tồn](images/part-adjust-dialog.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Location | Chữ | — | Khoá theo kho của thẻ tồn |
| 2 | Adjust Quantity | Nhập | Số | Liên động với New Quantity; nhận số lẻ, số âm; giảm quá tồn vẫn lưu, tồn âm, không cảnh báo (K3, E-007) |
| 3 | New Quantity | Nhập | Số | Gõ 0 khi tồn -10 thì Adjust Quantity tự thành 10 (K4) |
| 4 | Reason | Chọn | Bắt buộc | 11 lý do: Broken, Checked Inventory, Expired, Found, Lost, Miscellaneous, Received, Sold, Stolen, Transferred, Used; trống thì Save khoá (K6) |
| 5 | Comment | Nhập | Chữ | Ghi chú; ràng buộc chưa ghi |

## 1.4 Hộp chuyển kho

![Hộp chuyển kho](images/part-transfer-dialog.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Current Location | Chữ | — | Kho nguồn |
| 2 | Current Quantity | Chữ | Số | Tồn kho nguồn |
| 3 | Quantity to Transfer | Nhập | Số | Lớn hơn tồn vẫn cho Save; chỉ chuyển phần có, báo "Parts transfer was successful." (K7, E-008) |
| 4 | New Location | Chọn | Bắt buộc theo luồng | Chỉ hiện kho còn lại kèm tồn (K9). Mở hộp khi tồn từ 0 trở xuống không được, nút khoá (K8) |

## 1.5 Sổ kho đủ loại biến động

![Sổ kho đủ loại](images/inventory-activity-adjust-transfer.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Bảng biến động | Bảng | — | Cùng cột với màn 1.2 |
| 2 | Adjustment Type | Cột | Liên kết | Có Initial, Manual, Transfer, Purchase Order, Work Order, Bulk Update; nhật ký chỉ ghi "đủ loại", mỗi ảnh có loại nào cần đối chiếu ảnh |
| 3 | Dòng ghi bù | Dòng | Số | Sửa số lượng dòng lệnh +2 (K11); xoá dòng lệnh +20 (K16); chuyển kho -6,5 và +6,5 (K7) |

## 1.6 Cập nhật phụ tùng hàng loạt

![Cập nhật hàng loạt](images/parts-bulk-manage.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Tab theo kho | Tab | — | Mỗi kho một tab |
| 2 | Aisle, Row, Bin | Nhập | Chữ | Vị trí; nhật ký không ghi lần sửa |
| 3 | Active? | Gạt | Bật, tắt | Có đơn tại kho thì không tắt: E-010 (K20) |
| 4 | Track Inventory | Gạt | Bật, tắt | Thấy; nhật ký không ghi lần sửa |
| 5 | Current Qty | Nhập | Số | Sửa là tự lưu, "All changes saved"; -1 thành 8, sổ Bulk Update +9, không hỏi lý do (K19) |
| 6 | Last Quantity Update | Chữ | Ngày | Thấy; định dạng chưa ghi |
| 7 | Print Worksheet | Nút | — | `Xem`, không bấm |

## 2.4 Hộp nhận hàng

![Hộp nhận hàng](images/po-receive-dialog.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Item | Chữ | — | Phụ tùng trên dòng |
| 2 | Total Received | Chữ | Số | Đã nhận |
| 3 | Total Ordered | Chữ | Số | Đã đặt |
| 4 | Receive | Nhập | Số | Lần sau gợi ý số còn lại (D8); vượt không chặn (D9, E-013); số âm thành dương (D11, E-014) |
| 5 | Nơi đến | Chọn | — | Inventory, Existing work order, New work order |

## 2.5 Hộp nhận vào lệnh có sẵn

![Nhận vào lệnh có sẵn](images/po-receive-existing-wo.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Item, Total Received, Total Ordered, Receive | Bảng | Số | Như màn 2.4 |
| 2 | Nơi đến Existing work order | Chọn | — | Báo "These parts will be received to your inventory before being added to the selected work order." Sau đó mở form lệnh với dòng ghi chú "From PO #2"; sổ +5 trước, -5 khi lưu lệnh (D14) |
| 3 | Ô chọn lệnh | Chọn | — | Nhật ký không mô tả riêng ô này, xem ảnh |

## 2.6 Sửa đơn đã nhận một phần

![Sửa đơn đã nhận](images/po-edit-received-partial.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Vendor | Chọn | Khoá | Không đổi được sau khi nhận |
| 2 | Part Location | Chọn | Khoá | Không đổi được sau khi nhận |
| 3 | Line Items | Bảng | Số, tiền | Sửa số và giá được; không có Add Line Item |

## 2.7 Hộp điều chỉnh số nhận

![Make Adjustment](images/po-make-adjustment.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Item | Chữ | — | Phụ tùng trên dòng |
| 2 | Total Received | Chữ | Số | Đã nhận |
| 3 | Total Ordered | Chữ | Số | Đã đặt |
| 4 | Adjustment | Nhập | Số | "Negative values are allowed up to the quantity received on this order."; -6 trên 5 cắt còn -5, không báo (D12, E-015); lưu xong về Partial |

## 2.8 Đơn đã đóng khi nhận thiếu

![Đơn đóng khi thiếu](images/po-closed-partial.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Closed By | Chữ | Người, thời gian | Dấu người đóng |
| 2 | Received in Full By | Chữ | Người, thời gian | Còn dấu dù đơn đã lùi về Partial và đóng thiếu (D12, D13) |
| 3 | Line Items | Bảng | Số | PT-B 0 trên 5; không có ô lý do đóng (D13) |
| 4 | Nút hành động | Nút | — | Make Adjustment, Edit, Copy, Delete; không có nút mở lại |

## 3.3 Lịch sử dầu có cảnh báo dung tích

![Cảnh báo dung tích](images/fuel-history-capacity-alert.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Alerts | Cột | Icon | Có icon khi số lít lớn hơn dung tích đã khai (F9, F14); bằng dung tích không có (F13); chưa khai không kiểm (F1b) |
| 2 | Capacity Exception Volume | Cột | Số lít | "100 liters" với bình 60; sửa phiếu xuống 50 vẫn giữ 100 (F9b, E-017) |
| 3 | Location Exception Distance | Cột | Khoảng cách | Thấy cột; không chạy được vì cần tích hợp (F-VLA) |

## 3.4 Lỗi lùi ngày, số đồng hồ cao

![Lỗi số đồng hồ](images/fuel-entry-odometer-backdate-error.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Ngày | Chọn | Ngày | Lùi về 20/10 |
| 2 | Odometer | Nhập | Số | 9.000 km báo "must be less than 1,000 or marked as void" (F12, E-019); 900 km lưu được (F12b) |
| 3 | Void | Ô tick | Bật, tắt | Đường thoát lỗi theo câu báo; trống số thì "can't be blank" (F10, E-018) |
