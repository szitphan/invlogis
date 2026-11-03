---
type: research
feature: fleetio-parts-purchasing-fuel
status: draft
updated: 2026-11-03
links:
  - docs/_research/fleetio/fleetio-parts-purchasing-fuel.md
  - docs/_research/fleetio/run-notes/parts-purchasing-fuel.md
  - docs/_product/saas-core-vs-tenant.md
---

# Phụ tùng, mua hàng, nhà cung cấp, nhiên liệu — SRS phân tích ngược từ Fleetio

> Mô tả **Fleetio đang làm gì**, kèm đề xuất cho Invlogis. Chưa phải yêu cầu đã chốt với Delta.

**Nhãn bằng chứng:** `Chạy` đã thao tác và thấy kết quả · `Xem` thấy trên giao diện, không thao tác · `Docs` tài liệu công khai · `Suy` suy ra · `GĐ` giả định.

**Điều kiện chạy:** tài khoản dùng thử, một người dùng có quyền duyệt. Cài đặt chỉ đọc, không đổi: Static Pricing, tắt tự đóng đơn, bật Track Inventory mặc định, bán kính cảnh báo dầu Fleetio: 2 dặm.

## 1. Scope

**Trong phạm vi:** Part, Part Location, Inventory, Purchase Order, Vendor, Fuel Entry, Tool (chỉ theo tài liệu).

**Ngoài phạm vi:** Charging Entry (Charging History) ngoài phạm vi theo yêu cầu user, giữ lại FR-fleetio-parts-purchasing-fuel-023 để không mất ghi nhận cũ. Thẻ nhiên liệu Mỹ WEX, Comdata, EFS chỉ ghi nhận sự tồn tại; đặt hàng PartsTech. Không thay quản lý cây dầu, hút dầu của Delta, chúng sâu hơn Fleetio.

## 2. Actors & Stakeholders

| Actor | Loại | Mục tiêu | Trong scope? | Tương đương Invlogis |
|---|---|---|---|---|
| Người lập đơn | Người | Lập đơn mua | Có | Nhân viên xưởng |
| Người duyệt | Người | Duyệt, từ chối | Có | Theo quy trình Delta |
| Người nhận hàng | Người | Nhận, nhập kho, trả hàng, đóng đơn | Có | Nhân viên kho xưởng |
| Nhân viên kho | Người | Khai kho, chỉnh tồn, chuyển kho, kiểm kê | Có | Nhân viên kho xưởng |
| Operator | Người | Ghi phiếu dầu | Có | Lái xe, Nhân viên cây dầu |
| Thẻ nhiên liệu, Telematics | Ngoài | Đẩy giao dịch, vị trí | Có | EUP, cây dầu |

## 3. Functional Requirements (FR)

| ID | Title | Description | Priority | Tầng | Verify by | Source | Mức thực tế | Đề xuất Invlogis |
|---|---|---|---|---|---|---|---|---|
| FR-fleetio-parts-purchasing-fuel-001 | Danh mục phụ tùng | Mã duy nhất, mô tả, nhóm, hãng, mã hãng, UPC, đơn giá, đơn vị, bảo hành, ảnh, tài liệu. Không thấy trường thay thế, tương thích xe (K23). Đơn giá gõ lúc tạo có lần không được lưu (K18). | P0 | [Gói: Bảo dưỡng đội xe] | demo | Đợt đầu, K18, K23 | `Chạy`; K23 `Xem` | Lấy cho `product-catalog`, thêm tương thích xe và phụ tùng thay thế |
| FR-fleetio-parts-purchasing-fuel-002 | Kho và hoạt động theo kho | Phụ tùng bật tại nhiều kho, mỗi kho có vị trí dãy, hàng, ô; số lượng; điểm đặt lại. Tên kho không trùng. Kho khai ở Settings; bật phụ tùng tại kho thì nhập tồn đầu, ghi Initial. | P0 | [Gói: Bảo dưỡng đội xe] | test | K2, K20, luồng kho | `Chạy` | Lấy |
| FR-fleetio-parts-purchasing-fuel-003 | Thẻ tồn | Theo kho: Current Qty, Reorder Point, Pending PO Qty, WO Current Qty; bốn nút điều chỉnh, chuyển kho, đặt mua, menu (Edit, View History). | P0 | [Gói: Bảo dưỡng đội xe] | demo | Mục Tồn kho | `Chạy` | Lấy cho `stock-movement`, hợp nhiều bãi đầu kéo, mooc |
| FR-fleetio-parts-purchasing-fuel-004 | Sổ kho | Mỗi biến động ghi ngày, kho, loại, chứng từ, lý do, nhà cung cấp, số biến động, số trước, số sau, người, ghi chú. Sáu loại: Initial, Manual, Transfer, Purchase Order, Work Order, Bulk Update. | P0 | [Gói: Bảo dưỡng đội xe] | test | K3–K19 | `Chạy` đủ sáu loại | Lấy |
| FR-fleetio-parts-purchasing-fuel-005 | Điều chỉnh tồn | Hộp theo một kho: Adjust Quantity và New Quantity liên động, lý do bắt buộc trong 11 giá trị, ghi chú, chấp nhận số lẻ. Không chặn giảm quá tồn. Hàng loạt xem FR-fleetio-parts-purchasing-fuel-025. | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | test | K3–K6 | `Chạy` (bản trước `Docs`) | Lấy cho `inventory-count`, cảnh báo khi xuống âm; danh sách lý do là tham số mới, chưa có mã |
| FR-fleetio-parts-purchasing-fuel-006 | Chuyển kho | Nhập số chuyển, chọn kho đích, danh sách đích chỉ gồm kho còn lại kèm tồn. Nút khoá khi tồn từ 0 trở xuống. Nhập quá tồn thì cắt về tồn hiện có, vẫn báo thành công. | P1 | [Gói: Bảo dưỡng đội xe] | test | K7–K9 | `Chạy` (bản trước `Docs`) | Lấy, chặn hoặc báo rõ số đã chuyển |
| FR-fleetio-parts-purchasing-fuel-007 | Cảnh báo tồn thấp | Nhãn theo từng kho: Low Stock khi tồn trên 0 và từ điểm đặt lại trở xuống, số màu cam; Out of Stock khi từ 0 trở xuống. Gửi email theo tài liệu hãng. | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | test | S1–S4 | `Chạy` nhãn; `Docs` email | Lấy; điểm đặt lại theo từng kho |
| FR-fleetio-parts-purchasing-fuel-008 | Tính giá tồn | Chọn một trong Average Cost, FIFO, LIFO, Static Pricing. Static: Unit Cost phụ tùng giữ theo danh mục dù đơn mua giá khác; Total Inventory Value theo Unit Cost; phụ tùng không giá tính 0. | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | phân tích | K17, K18 | `Chạy` Static; `Xem` ba phương pháp còn lại | Cần kế toán Delta quyết |
| FR-fleetio-parts-purchasing-fuel-009 | Lập đơn mua | Một nhà cung cấp, một kho rồi mới thêm dòng; chỉ hiện nhà cung cấp có Parts; đơn giá lấy từ danh mục, sửa được; giảm giá, phí vận chuyển, thuế; tài liệu. Lưu được đơn 0 dòng; dòng trùng bị chặn; dòng số lượng 0 không bị chặn. | P0 | [Gói: Bảo dưỡng đội xe] | demo | D1–D7 | `Chạy` | Lấy cho `purchasing`, chặn dòng số lượng 0 |
| FR-fleetio-parts-purchasing-fuel-010 | Duyệt đơn | Có quyền duyệt thì Save & Approve hoặc Approve, một cú bấm, không hộp xác nhận, duyệt được đơn của mình. Không có quyền thì Submit for Approval, người có quyền duyệt hoặc từ chối. | P0 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | test | D17, ma trận đơn | `Chạy` nhánh có quyền; `Docs` nhánh còn lại | Lấy, thêm nhiều cấp nếu Delta cần, tách người lập và người duyệt theo cấu hình |
| FR-fleetio-parts-purchasing-fuel-011 | Một nút chính mỗi bước | Approve, Mark as Purchased, Receive, Close; ghi người và thời điểm mỗi bước. | P0 | [Gói: Bảo dưỡng đội xe] | demo | Ma trận đơn | `Chạy` | Lấy |
| FR-fleetio-parts-purchasing-fuel-012 | Nhận hàng | Bảng Item, Total Received, Total Ordered, Receive; nhận nhiều lần, lần sau gợi ý số còn lại. Không chặn nhận vượt. Trạng thái tính theo từng dòng: vượt ở một dòng, dòng khác 0 vẫn Partial. | P0 | [Gói: Bảo dưỡng đội xe] | test | D8–D11 | `Chạy` | Lấy, cảnh báo nhận vượt theo tham số mới, chưa có mã |
| FR-fleetio-parts-purchasing-fuel-013 | Nơi đến khi nhận | Inventory, Existing work order, New work order. Hai nhánh lệnh đều nhập kho trước, trừ khi lưu lệnh, dòng ghi chú "From PO #n". `Docs`: chỉ với Static Pricing; phương pháp khác chưa thử. | P1 | [Gói: Bảo dưỡng đội xe] | demo | D14, D15 | `Chạy` Inventory và lệnh có sẵn; lệnh mới `Chạy` đến bước huỷ form | Lấy, cả hai bút toán |
| FR-fleetio-parts-purchasing-fuel-014 | Xuất phụ tùng cho lệnh | Chọn phụ tùng thấy tồn từng kho; lấy từ kho hoặc None không trừ kho; gắn đầu việc. Trừ ngay khi lưu. Không cảnh báo khi vượt tồn. | P0 | [Gói: Bảo dưỡng đội xe] | test | K10, K12, K13 | `Chạy` | Lấy, thêm kiểm tồn |
| FR-fleetio-parts-purchasing-fuel-015 | Nhà cung cấp | Tên, địa chỉ, thành phố, tỉnh, mã bưu chính, quốc gia bắt buộc; liên hệ; phân loại Charging, Fuel, Parts, Service, Vehicle không bắt buộc nhưng quyết định nơi được chọn; nhãn; đánh giá. | P1 | [Cấu hình] | test | D1, N1, N2, F-NCC | `Chạy`; đánh giá `Xem` | Lấy cho `business-partners`, bỏ bắt mã bưu chính |
| FR-fleetio-parts-purchasing-fuel-016 | Tạo nhanh trong ô chọn | Gõ tên chưa có thì chọn Create, mở form với tên điền sẵn và phân loại theo ngữ cảnh. | P1 | [Lõi] | demo | Đợt đầu | `Chạy` | Lấy, cần chọn rõ ràng |
| FR-fleetio-parts-purchasing-fuel-017 | Phiếu dầu | Xe, ngày, số đồng hồ, số lít, đơn giá, loại dầu, nơi đổ, tham chiếu, ảnh, tài liệu. Nơi đổ chỉ gồm nhà cung cấp có Fuel; có nhà cung cấp thì hiện bản đồ. Lưu được 0 lít. | P0 | [Gói: Nhiên liệu] | demo | F1, F11, F-NCC | `Chạy` | Đối chiếu `fuel-issuing`, chặn 0 lít |
| FR-fleetio-parts-purchasing-fuel-018 | Tính tiêu hao | Từ phiếu trước theo số đồng hồ: quãng đường, tiêu hao, chi phí trên km, chênh so với lần trước. Cộng dồn phiếu Partial. Tính đúng nhưng xe km, lít vẫn hiện mpg. | P0 | [Gói: Nhiên liệu] | test | F1–F6 | `Chạy` | Lấy, dùng lít trên 100 km |
| FR-fleetio-parts-purchasing-fuel-019 | Cờ phiếu dầu | Personal vẫn tính tiêu hao và vào Cost of Ownership. Partial cộng dồn sang phiếu sau. Reset usage: phiếu đó không usage, phiếu sau Usage "N/A" nhưng vẫn có tiêu hao. | P1 | [Gói: Nhiên liệu] | test | F3–F7 | `Chạy` (bản trước `Xem`) | Lấy Đổ một phần, Đặt lại; hợp đầu kéo đổ nhiều cây dầu; hiện rõ Usage sau Reset |
| FR-fleetio-parts-purchasing-fuel-020 | Thẻ tổng hợp dầu | Tổng tiền, tổng lượng, tiêu hao trung bình, chi phí trung bình theo bộ lọc. Trên VND sai 100 lần. | P1 | [Gói: Nhiên liệu] | demo | T3–T5 | `Chạy` | Lấy cho `fuel-stations`, sửa tiền |
| FR-fleetio-parts-purchasing-fuel-021 | Cảnh báo sai vị trí | Vị trí xe khi đổ xa nhà cung cấp hơn bán kính đặt thì gắn Vendor Location Alert; tắt được. | P1 | [Gói: Giám sát nhiên liệu] [Cấu hình] | test | F-VLA | `Xem` cấu hình, `Docs`; không chạy vì cần tích hợp | Lấy, bán kính là tham số mới, chưa có mã |
| FR-fleetio-parts-purchasing-fuel-022 | Cảnh báo vượt dung tích | Số lít lớn hơn dung tích bình đã khai thì gắn Capacity Alert và ghi Capacity Exception Volume, kể cả phiếu nhập tay. Bằng dung tích không cảnh báo; chưa khai không kiểm. Sửa phiếu không gỡ cảnh báo. Bản trước ghi nhập tay không kích hoạt là sai. | P1 | [Gói: Giám sát nhiên liệu] | test | F9, F9b, F13, F14, F1b | `Chạy` | Lấy, chỉ cần dung tích bình; đầu kéo khai đúng tổng bình; tính lại khi sửa phiếu |
| FR-fleetio-parts-purchasing-fuel-023 | Phiên sạc | Ngoài phạm vi theo yêu cầu user. Ghi nhận cũ: giờ bắt đầu, kết thúc, thời lượng, điện năng, đơn giá, chi phí, chi phí trên km. | P2 | [Cấu hình] | demo | F-Sạc | `Xem` cột ở đợt đầu, không xem thêm | Ngoài phạm vi theo yêu cầu user |
| FR-fleetio-parts-purchasing-fuel-024 | Công cụ | Quản lý công cụ, gán người, nhắc riêng; nhắc không tự lặp, resolve xong phải tạo lại; là gói thêm. | P2 | [Gói: Bảo dưỡng đội xe] | demo | Tài liệu hãng | `Docs` | Cân nhắc, nên cho nhắc lặp |
| FR-fleetio-parts-purchasing-fuel-025 | Bulk Manage Parts | Tab theo kho; cột Aisle, Row, Bin, Active?, Track Inventory, Current Qty, Last Quantity Update; sửa ô là tự lưu, sổ loại Bulk Update, không hỏi lý do; Print Worksheet. | P2 | [Gói: Bảo dưỡng đội xe] | test | K19, K20 | `Chạy`; Print Worksheet `Xem` | Lấy cho `inventory-count`, gắn đợt kiểm kê hoặc lý do |
| FR-fleetio-parts-purchasing-fuel-026 | Nhiều nhà cung cấp, lịch sử giá | Thêm nhà cung cấp, giá trong Purchase History; đơn mua tự thêm dòng lịch sử; trang phụ tùng vẽ biểu đồ giá. | P2 | [Gói: Bảo dưỡng đội xe] | demo | K22 | `Chạy` | Lấy |
| FR-fleetio-parts-purchasing-fuel-027 | Sửa, xoá dòng phụ tùng trên lệnh | Sửa số lượng hoặc xoá dòng thì sổ ghi bù, loại Work Order kèm số lệnh; xoá có hộp xác nhận. | P0 | [Gói: Bảo dưỡng đội xe] | test | K11, K16 | `Chạy` | Lấy |
| FR-fleetio-parts-purchasing-fuel-028 | Make Adjustment trên đơn | Có ở Full, Closed; bảng Item, Total Received, Total Ordered, Adjustment; số âm tới mức đã nhận; quá thì cắt không báo; ghi sổ; về Partial; "Received in Full By" vẫn còn. | P1 | [Gói: Bảo dưỡng đội xe] | test | D12 | `Chạy` từ Full; từ Closed `Xem` nút | Lấy cơ chế, báo khi cắt, xoá dấu nhận đủ khi lùi |
| FR-fleetio-parts-purchasing-fuel-029 | Đóng đơn | Close từ Partial, Full; hộp xác nhận; đóng được khi nhận thiếu, không ghi lý do; ghi Closed By. Không có nút mở lại. Không có trạng thái, nút huỷ riêng. | P1 | [Gói: Bảo dưỡng đội xe] | test | D13, ma trận đơn | `Chạy` | Bắt lý do khi đóng thiếu, thêm trạng thái Huỷ |
| FR-fleetio-parts-purchasing-fuel-030 | Sửa đơn theo trạng thái | Draft sửa mọi thứ; Approved đủ trường; Purchased có Edit; Partial khoá nhà cung cấp, kho, không thêm bớt dòng, sửa số và giá được; Full, Closed vẫn Edit, tổng tính lại. | P1 | [Gói: Bảo dưỡng đội xe] | test | Ma trận đơn | `Chạy` Approved, Partial, Closed; còn lại `Xem` | Khoá giá từ khi đóng |
| FR-fleetio-parts-purchasing-fuel-031 | Lùi trạng thái đơn | Save as Draft từ Approved về Draft, mất dòng Approved By. Unmark as Purchased từ Purchased về Approved, một cú bấm. Make Adjustment từ Full về Partial. | P1 | [Gói: Bảo dưỡng đội xe] | test | PO #2, PO #3, D12 | `Chạy` | Lấy, giữ lịch sử người duyệt cũ |
| FR-fleetio-parts-purchasing-fuel-032 | Sao chép đơn | Make a Copy mở form mới điền sẵn, giữ giá đơn cũ, số tăng lên. | P2 | [Gói: Bảo dưỡng đội xe] | demo | D16 | `Chạy` | Lấy |
| FR-fleetio-parts-purchasing-fuel-033 | Void phiếu dầu | Tick Void, số đồng hồ vẫn bắt buộc; lưu thì số gạch ngang, đồng hồ xe không đổi, không Usage; vẫn tính vào chi phí xe. | P1 | [Gói: Nhiên liệu] | test | F10, T6 | `Chạy` | Lấy, không cộng chi phí |
| FR-fleetio-parts-purchasing-fuel-034 | Bộ lọc phiếu dầu | Date, Vehicle, Vehicle Group, Vendor, Filters; mở bộ lọc theo xe có Add Filter, Add Filter Group. | P2 | [Gói: Nhiên liệu] | demo | F-Lọc | `Chạy` lọc xe; còn lại `Xem` | Lấy |
| FR-fleetio-parts-purchasing-fuel-035 | Trang nhà cung cấp | Tab Overview, Fuel Entries, Purchase Orders theo phân loại; tab đơn liệt kê đơn của nhà cung cấp. "Network Status: Invite", "Find Shops" có Add Vendors. | P2 | [Cấu hình] | demo | N3–N5 | `Chạy` tab; `Xem` Network Status, Find Shops | Lấy tab |
| FR-fleetio-parts-purchasing-fuel-036 | Thẻ dầu trên phiếu | Ô Fuel Card ghi "No"; cấu hình WEX chỉ đọc; không có màn gán thẻ thử được. | P2 | [Gói: Nhiên liệu] | demo | F-Thẻ | `Xem` | Tìm đối tác Việt Nam |
| FR-fleetio-parts-purchasing-fuel-037 | In và lịch sử bản ghi đơn | Print, View Record History trên đơn. | P2 | [Gói: Bảo dưỡng đội xe] | demo | Ma trận đơn | `Xem` | Lấy |
| FR-fleetio-parts-purchasing-fuel-038 | Tác động của hoàn thành, mở lại lệnh | Hoàn thành: sổ không có dòng mới, sinh Service Entry, Edit khoá; cần Started At, Start Odometer theo cài đặt. Mở lại: sổ không đổi, liên kết Service Entry biến mất, phần archive được khôi phục theo câu báo. | P1 | [Gói: Bảo dưỡng đội xe] | test | K14, K15 | `Chạy` | Lấy, giữ dấu Service Entry đã huỷ |

## 4. Non-Functional Requirements (NFR)

| ID | Category | Requirement | Priority | Acceptance |
|---|---|---|---|---|
| NFR-fleetio-parts-purchasing-fuel-001 | truy vết | Mỗi biến động kho truy được chứng từ và người. | P0 | `Chạy` đủ sáu loại |
| NFR-fleetio-parts-purchasing-fuel-002 | quyền | Quyền nhận hàng tách với quyền chỉnh số lượng. | P0 | `Docs`: Receive Purchase Orders, Update Inventory Quantities |
| NFR-fleetio-parts-purchasing-fuel-003 | toàn vẹn tiền | Đơn giá và tổng tiền trên mọi trang phải đúng định dạng tiền của khách. | P0 | Fleetio không đạt, xem E-005, E-012, E-020 |
| NFR-fleetio-parts-purchasing-fuel-004 | khối lượng | Số giao dịch kho, dầu cao điểm của Invlogis: TBD — đội sản phẩm — khi chi tiết hoá. | P1 | TBD |
| NFR-fleetio-parts-purchasing-fuel-005 | minh bạch | Thao tác làm khác số người dùng nhập phải báo số thực làm. Đề xuất Invlogis. | P0 | Fleetio không đạt, xem E-008, E-014, E-015 |

## 5. Business Rules

| ID | Rule | Tầng | Trigger | Implements FR | Source |
|---|---|---|---|---|---|
| BR-fleetio-parts-purchasing-fuel-001 | Không tắt phụ tùng tại kho nếu phụ tùng đang trong lệnh chưa xong hoặc đơn mua ở bất kỳ trạng thái nào. | [Gói: Bảo dưỡng đội xe] | Tắt kho | FR-fleetio-parts-purchasing-fuel-002 | `Chạy` nhánh đơn (K20); `Xem` nhánh lệnh |
| BR-fleetio-parts-purchasing-fuel-002 | Phải có ít nhất một kho mới tạo được đơn. | [Gói: Bảo dưỡng đội xe] | Tạo đơn | FR-fleetio-parts-purchasing-fuel-009 | `Docs` |
| BR-fleetio-parts-purchasing-fuel-003 | Tổng đơn tính theo số đặt, kể cả phần chưa nhận hay nhận vượt; số nhận mới vào tồn. | [Gói: Bảo dưỡng đội xe] | Nhận | FR-fleetio-parts-purchasing-fuel-012 | `Chạy` (D9), `Docs` |
| BR-fleetio-parts-purchasing-fuel-004 | Trừ kho ngay khi lưu dòng phụ tùng trên lệnh, kể cả lệnh Open. | [Gói: Bảo dưỡng đội xe] | Lưu lệnh | FR-fleetio-parts-purchasing-fuel-014 | `Chạy` (K10) |
| BR-fleetio-parts-purchasing-fuel-005 | Fleetio cho tồn âm ở xuất cho lệnh và chỉnh tồn, chỉ gắn nhãn Out of Stock. Đề xuất Invlogis: mặc định chặn, cho phép âm theo tham số khách (tham số mới, chưa có mã). | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Xuất quá tồn | FR-fleetio-parts-purchasing-fuel-014 | `Chạy` (K3, K12) |
| BR-fleetio-parts-purchasing-fuel-006 | Tài liệu hãng: không sửa đơn giá sau khi nhận, đã dùng cho lệnh thì khoá vĩnh viễn, Closed khoá; áp với tính giá nâng cao. Thực tế dưới Static Pricing: Closed vẫn sửa được đơn giá, tổng tính lại. | [Gói: Bảo dưỡng đội xe] | Sửa đơn | FR-fleetio-parts-purchasing-fuel-030 | `Docs`; `Chạy` nhánh Static; phương pháp khác chưa thử |
| BR-fleetio-parts-purchasing-fuel-007 | Tài liệu hãng: điểm đặt lại phải lớn hơn 0. Thực tế lưu được 0, tồn dương không nhãn. | [Gói: Bảo dưỡng đội xe] | Khai kho | FR-fleetio-parts-purchasing-fuel-007 | `Docs`; `Chạy` trái tài liệu (S4) |
| BR-fleetio-parts-purchasing-fuel-008 | Lùi được từ Purchased về Approved bằng Unmark as Purchased, một cú bấm, không hỏi. | [Gói: Bảo dưỡng đội xe] | Sửa đơn | FR-fleetio-parts-purchasing-fuel-031 | `Chạy` (bản trước `Docs`) |
| BR-fleetio-parts-purchasing-fuel-009 | Tự đóng khi nhận đủ nếu bật; khi tắt phải Close tay. | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Nhận đủ | FR-fleetio-parts-purchasing-fuel-011 | `Xem` cấu hình; `Chạy` nhánh tắt |
| BR-fleetio-parts-purchasing-fuel-010 | Trạng thái đơn mua do hệ thống cố định. | [Gói: Bảo dưỡng đội xe] | Cấu hình | FR-fleetio-parts-purchasing-fuel-011 | `Xem` |
| BR-fleetio-parts-purchasing-fuel-011 | Phiếu đầu không có tiêu hao, cần phiếu trước. | [Gói: Nhiên liệu] | Lưu phiếu | FR-fleetio-parts-purchasing-fuel-018 | `Chạy` (F1) |
| BR-fleetio-parts-purchasing-fuel-012 | Vendor Location Alert cần có cả tích hợp nhiên liệu và thiết bị định vị. Không áp cho Capacity Alert, xem BR-fleetio-parts-purchasing-fuel-031. | [Gói: Giám sát nhiên liệu] | Có giao dịch | FR-fleetio-parts-purchasing-fuel-021 | `Docs` |
| BR-fleetio-parts-purchasing-fuel-013 | Chỉnh tồn không chặn giảm quá tồn, không cảnh báo. | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Chỉnh tồn | FR-fleetio-parts-purchasing-fuel-005 | `Chạy` (K3) |
| BR-fleetio-parts-purchasing-fuel-014 | Chuyển kho cắt số về tồn hiện có, không báo đã cắt; khoá khi tồn từ 0 trở xuống. | [Gói: Bảo dưỡng đội xe] | Chuyển kho | FR-fleetio-parts-purchasing-fuel-006 | `Chạy` (K7, K8) |
| BR-fleetio-parts-purchasing-fuel-015 | Sửa số lượng hoặc xoá dòng phụ tùng trên lệnh thì sổ ghi bù đúng chênh lệch. | [Gói: Bảo dưỡng đội xe] | Sửa, xoá dòng | FR-fleetio-parts-purchasing-fuel-027 | `Chạy` (K11, K16) |
| BR-fleetio-parts-purchasing-fuel-016 | Hoàn thành hoặc mở lại lệnh không tạo dòng sổ kho. | [Gói: Bảo dưỡng đội xe] | Đổi trạng thái lệnh | FR-fleetio-parts-purchasing-fuel-038 | `Chạy` (K14, K15) |
| BR-fleetio-parts-purchasing-fuel-017 | Một đơn một nhà cung cấp, một kho; khoá hai ô này sau khi nhận. | [Gói: Bảo dưỡng đội xe] | Lập, sửa đơn | FR-fleetio-parts-purchasing-fuel-009 | `Chạy` (D3) |
| BR-fleetio-parts-purchasing-fuel-018 | Một phụ tùng chỉ một dòng trong đơn. | [Gói: Bảo dưỡng đội xe] | Lưu đơn | FR-fleetio-parts-purchasing-fuel-009 | `Chạy` (D4) |
| BR-fleetio-parts-purchasing-fuel-019 | Đơn 0 dòng lưu được, Approve khoá; dòng số lượng 0 duyệt được. | [Gói: Bảo dưỡng đội xe] | Duyệt | FR-fleetio-parts-purchasing-fuel-010 | `Chạy` (D5) |
| BR-fleetio-parts-purchasing-fuel-020 | Giảm giá tính trên tạm tính; thuế tính trên phần sau giảm, không gồm phí vận chuyển. | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Tính tổng | FR-fleetio-parts-purchasing-fuel-009 | `Chạy` (D6) |
| BR-fleetio-parts-purchasing-fuel-021 | Nhận vượt không chặn, tồn tăng đủ số nhận. Trạng thái Full khi mọi dòng đạt số đặt. | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Nhận | FR-fleetio-parts-purchasing-fuel-012 | `Chạy` (D9, D10); điều kiện Full `Suy` |
| BR-fleetio-parts-purchasing-fuel-022 | Ô Receive bỏ dấu âm: gõ số âm thành nhận dương, không báo. | [Gói: Bảo dưỡng đội xe] | Nhận | FR-fleetio-parts-purchasing-fuel-012 | `Chạy` (D11) |
| BR-fleetio-parts-purchasing-fuel-023 | Make Adjustment chỉ có ở Full, Closed; số âm cắt về số đã nhận, không báo; giảm thì về Partial. | [Gói: Bảo dưỡng đội xe] | Trả hàng | FR-fleetio-parts-purchasing-fuel-028 | `Chạy` (D12) |
| BR-fleetio-parts-purchasing-fuel-024 | Đóng được đơn khi nhận thiếu, không yêu cầu lý do. | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Close | FR-fleetio-parts-purchasing-fuel-029 | `Chạy` (D13) |
| BR-fleetio-parts-purchasing-fuel-025 | Không có huỷ đơn; thoát đơn chỉ có Close (từ Partial, Full) hoặc Delete; Closed không có nút mở lại. | [Gói: Bảo dưỡng đội xe] | Kết thúc đơn | FR-fleetio-parts-purchasing-fuel-029 | `Chạy` nút; Delete `Xem` |
| BR-fleetio-parts-purchasing-fuel-026 | Nhận vào lệnh luôn qua kho hai bước; huỷ form lệnh thì hàng ở lại kho, đơn vẫn đổi trạng thái. | [Gói: Bảo dưỡng đội xe] | Nhận vào lệnh | FR-fleetio-parts-purchasing-fuel-013 | `Chạy` (D14, D15) |
| BR-fleetio-parts-purchasing-fuel-027 | Người có quyền duyệt tự duyệt đơn của mình được. Tách người chưa kiểm được. | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Duyệt | FR-fleetio-parts-purchasing-fuel-010 | `Chạy` (D17) |
| BR-fleetio-parts-purchasing-fuel-028 | Phiếu Partial không có tiêu hao, số lít cộng vào phiếu đầy kế tiếp. | [Gói: Nhiên liệu] | Lưu phiếu | FR-fleetio-parts-purchasing-fuel-019 | `Chạy` (F3, F4) |
| BR-fleetio-parts-purchasing-fuel-029 | Reset usage ngắt chuỗi: phiếu đó không usage, phiếu sau hiện Usage "N/A" nhưng vẫn tính tiêu hao từ phiếu Reset. | [Gói: Nhiên liệu] | Lưu phiếu | FR-fleetio-parts-purchasing-fuel-019 | `Chạy` (F5, F6) |
| BR-fleetio-parts-purchasing-fuel-030 | Phiếu Personal và Void vẫn cộng vào chi phí xe; Personal vẫn tính tiêu hao. | [Gói: Nhiên liệu] | Lưu phiếu | FR-fleetio-parts-purchasing-fuel-019 | `Chạy` (F7, T6) |
| BR-fleetio-parts-purchasing-fuel-031 | Capacity Alert khi số lít lớn hơn dung tích đã khai, không cần tích hợp; không gỡ khi sửa phiếu. | [Gói: Giám sát nhiên liệu] | Lưu phiếu | FR-fleetio-parts-purchasing-fuel-022 | `Chạy` (F9, F9b, F13, F14, F1b) |
| BR-fleetio-parts-purchasing-fuel-032 | Số đồng hồ lùi cùng ngày không chặn; lùi ngày với số cao bị chặn, trừ khi Void; lùi ngày với số thấp lưu được, không đổi phiếu sau. | [Gói: Nhiên liệu] | Lưu phiếu | FR-fleetio-parts-purchasing-fuel-017 | `Chạy` (F8, F12, F12b) |
| BR-fleetio-parts-purchasing-fuel-033 | Phiếu Void vẫn bắt buộc số đồng hồ, không cập nhật đồng hồ xe, không có Usage. | [Gói: Nhiên liệu] | Void | FR-fleetio-parts-purchasing-fuel-033 | `Chạy` (F10) |
| BR-fleetio-parts-purchasing-fuel-034 | Phân loại nhà cung cấp quyết định nơi chọn được: Parts cho đơn mua, Fuel cho phiếu dầu. | [Cấu hình] | Chọn nhà cung cấp | FR-fleetio-parts-purchasing-fuel-015 | `Chạy` (D1, F-NCC) |
| BR-fleetio-parts-purchasing-fuel-035 | Sửa tồn trong Bulk tự lưu, ghi Bulk Update, không hỏi lý do. | [Gói: Bảo dưỡng đội xe] | Sửa ô | FR-fleetio-parts-purchasing-fuel-025 | `Chạy` (K19) |
| BR-fleetio-parts-purchasing-fuel-036 | Điều chỉnh tồn ở hộp thường bắt buộc lý do. | [Gói: Bảo dưỡng đội xe] | Chỉnh tồn | FR-fleetio-parts-purchasing-fuel-005 | `Chạy` (K6) |
| BR-fleetio-parts-purchasing-fuel-037 | Nhãn tồn: từ 0 trở xuống là Out of Stock; trên 0 và từ điểm đặt lại trở xuống là Low Stock; còn lại không nhãn. | [Gói: Bảo dưỡng đội xe] | Mọi biến động | FR-fleetio-parts-purchasing-fuel-007 | `Chạy` (S1–S3) |
| BR-fleetio-parts-purchasing-fuel-038 | Dưới Static Pricing, giá trị tồn tính theo Unit Cost danh mục, không theo đơn giá đơn mua; không có giá thì tính 0. | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Tính giá trị tồn | FR-fleetio-parts-purchasing-fuel-008 | `Chạy` (K17, K18) |
| BR-fleetio-parts-purchasing-fuel-039 | Tên kho không trùng. | [Gói: Bảo dưỡng đội xe] | Tạo kho | FR-fleetio-parts-purchasing-fuel-002 | `Chạy` (K2) |
| BR-fleetio-parts-purchasing-fuel-040 | Chọn phụ tùng trên đơn: chưa bật tại kho của đơn thì xám, có khoá. | [Gói: Bảo dưỡng đội xe] | Thêm dòng | FR-fleetio-parts-purchasing-fuel-009 | `Chạy` (D2) |

## 6. Error Matrix

| Error ID | Title | Trigger | Severity | Related FR | Screen state | Recovery | Mức |
|---|---|---|---|---|---|---|---|
| E-fleetio-parts-purchasing-fuel-001 | Chưa chọn đủ | "Select a Vendor and Part Location first." | minor | FR-fleetio-parts-purchasing-fuel-009 | Khối dòng hàng khoá | Chọn đủ | `Chạy` |
| E-fleetio-parts-purchasing-fuel-002 | Chưa có quyền kho | "You do not have access to any Part Locations" | major | FR-fleetio-parts-purchasing-fuel-002 | Hộp quản lý kho | Cấp Record Set; lần sau tự hết, chưa rõ nguyên nhân | `Chạy` đợt 02/11 |
| E-fleetio-parts-purchasing-fuel-003 | Xuất quá tồn | Không báo; tồn âm. Hộp Add Part chỉ ghi "This will make an inventory adjustment" | major | FR-fleetio-parts-purchasing-fuel-014 | Nhãn Out of Stock sau khi lưu | Nhận hàng bù, xoá dòng. Không nên học | `Chạy` |
| E-fleetio-parts-purchasing-fuel-004 | Tiêu hao sai đơn vị | Xe km, lít nhưng hiện mpg; giá trị đổi ra đúng | minor | FR-fleetio-parts-purchasing-fuel-018 | Phiếu dầu, danh sách | Không nên học | `Chạy` |
| E-fleetio-parts-purchasing-fuel-005 | Lệch tiền 100 lần ở lệnh | Hộp Add Part và form đúng; trang chi tiết lệnh, Service Entry hiện gấp 100 lần. Bản trước ghi lệch ở hộp Add Part là chưa đúng chỗ | critical | FR-fleetio-parts-purchasing-fuel-014 | Không báo | Không nên học | `Chạy`, đã lặp lại |
| E-fleetio-parts-purchasing-fuel-006 | Trùng tên kho | "has already been taken", "Part Location could not be created" | minor | FR-fleetio-parts-purchasing-fuel-002 | Form kho | Đổi tên | `Chạy` |
| E-fleetio-parts-purchasing-fuel-007 | Chỉnh giảm quá tồn | Không báo; tồn âm | major | FR-fleetio-parts-purchasing-fuel-005 | Out of Stock sau khi lưu | Chỉnh lại. Không nên học | `Chạy` |
| E-fleetio-parts-purchasing-fuel-008 | Chuyển quá tồn bị cắt | "Parts transfer was successful." dù chỉ chuyển phần có | major | FR-fleetio-parts-purchasing-fuel-006 | Save vẫn mở | Đọc sổ kho mới biết. Không nên học | `Chạy` |
| E-fleetio-parts-purchasing-fuel-009 | Hoàn thành lệnh thiếu dữ liệu | "Please edit and fix the following errors: Started At can't be blank", "Start Odometer can't be blank (per your account settings)" | minor | FR-fleetio-parts-purchasing-fuel-038 | Chặn đổi trạng thái | Nhập đủ | `Chạy` |
| E-fleetio-parts-purchasing-fuel-010 | Tắt kho khi có đơn | "This part can't be deactivated because it's used in one or more purchase orders at this location." | minor | FR-fleetio-parts-purchasing-fuel-025 | Bulk Manage, không tắt | Xử lý đơn trước; Delete đơn chưa thử | `Chạy` |
| E-fleetio-parts-purchasing-fuel-011 | Dòng trùng | "Part TEST-KHO-PT-A is duplicated", "Purchase Order could not be created" | minor | FR-fleetio-parts-purchasing-fuel-009 | Form đơn | Gộp dòng | `Chạy` |
| E-fleetio-parts-purchasing-fuel-012 | Ô Shipping sai 100 lần | Không báo, xem D7 | major | FR-fleetio-parts-purchasing-fuel-009 | Tổng sai | Gõ số chia 100. Không nên học | `Chạy` |
| E-fleetio-parts-purchasing-fuel-013 | Nhận vượt | Không chặn, không cảnh báo | major | FR-fleetio-parts-purchasing-fuel-012 | Nhận hiện vượt số đặt | Make Adjustment | `Chạy` |
| E-fleetio-parts-purchasing-fuel-014 | Mất dấu âm ở Receive | Gõ số âm thành nhận dương, không báo | major | FR-fleetio-parts-purchasing-fuel-012 | Báo nhận thành công | Make Adjustment. Không nên học | `Chạy` |
| E-fleetio-parts-purchasing-fuel-015 | Trả quá số bị cắt | "was successfully adjusted" dù đã cắt số | major | FR-fleetio-parts-purchasing-fuel-028 | Về Partial | Đọc sổ. Không nên học | `Chạy` |
| E-fleetio-parts-purchasing-fuel-016 | Số đồng hồ lùi cùng ngày | Không báo; phiếu sau không tính lại | major | FR-fleetio-parts-purchasing-fuel-017 | Phiếu lưu bình thường | Sửa phiếu. Không nên học | `Chạy` |
| E-fleetio-parts-purchasing-fuel-017 | Cảnh báo dầu không gỡ | Sửa số lít nhỏ lại, cảnh báo và cột vẫn giữ số cũ | minor | FR-fleetio-parts-purchasing-fuel-022 | Fuel History | Chưa thấy cách gỡ. Không nên học | `Chạy` |
| E-fleetio-parts-purchasing-fuel-018 | Void trống số đồng hồ | "can't be blank" | minor | FR-fleetio-parts-purchasing-fuel-033 | Form phiếu | Nhập số | `Chạy` |
| E-fleetio-parts-purchasing-fuel-019 | Lùi ngày, số cao | "must be less than 1,000 or marked as void" | minor | FR-fleetio-parts-purchasing-fuel-017 | Form phiếu | Sửa số hoặc Void | `Chạy` |
| E-fleetio-parts-purchasing-fuel-020 | Lệch tiền 100 lần ở báo cáo dầu | Fuel History, Total Fuel Cost, Cost per km, Avg. Cost nhỏ hơn đúng 100 lần | critical | FR-fleetio-parts-purchasing-fuel-020 | Không báo | Chi tiết xe đúng, đối chiếu ở đó. Không nên học | `Chạy`; Avg. Cost đúng là `Suy` |
| E-fleetio-parts-purchasing-fuel-021 | Nhà cung cấp thiếu trường | "can't be blank" | minor | FR-fleetio-parts-purchasing-fuel-015 | Form | Nhập đủ | `Chạy` |
| E-fleetio-parts-purchasing-fuel-022 | Enter lưu form sớm | Enter trong ô Country vừa chọn vừa lưu | major | FR-fleetio-parts-purchasing-fuel-015 | Bản ghi tạo sớm | Sửa bản ghi. Không nên học | `Chạy`, ba lần |
| E-fleetio-parts-purchasing-fuel-023 | Thêm xe khi hết hạn mức | Save Vehicle quay mãi, không báo lỗi, thanh "5 of 5" | major | Ngoài nhóm này | Form xe | Giới hạn là `Suy` | `Chạy` |
| E-fleetio-parts-purchasing-fuel-024 | Mất giá lúc tạo phụ tùng | Giá gõ lúc tạo không được lưu, chưa rõ vì sao | major | FR-fleetio-parts-purchasing-fuel-001 | Giá trị tồn 0 | Sửa phụ tùng | `Chạy` |
| E-fleetio-parts-purchasing-fuel-025 | Đơn Closed vẫn sửa được giá | "was successfully updated" trên đơn đã đóng | major | FR-fleetio-parts-purchasing-fuel-030 | Tổng đổi | Không nên học | `Chạy` |

## 6A. Ma trận case

Tiền ghi nguyên giá trị đã thử trên tài khoản VND. Điều không xảy ra cũng ghi là kết quả.

### Tồn và kho

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| S1 Không nhãn | Tồn 6 và 6,5, điểm đặt lại 5 | Không nhãn, đủ nút | `Chạy` |
| S2 Low Stock | Tồn 3, và đúng bằng 5, điểm đặt lại 5 | Nhãn "Low Stock", số màu cam, đủ nút | `Chạy` |
| S3 Out of Stock | Tồn 0 và -10 | Nhãn "Out of Stock", nút chuyển kho khoá | `Chạy` |
| S4 Điểm đặt lại 0 | Lưu điểm 0, tồn 9,5 | Lưu được dù tài liệu nói phải lớn hơn 0, "Part was successfully updated", không nhãn. Chưa thử tồn về 0 với điểm 0 | `Chạy` |
| C1 Xuất quá tồn đợt đầu | Tồn 4, xuất 6 | Tồn -2, Out of Stock, nhận thêm 6 về 4 | `Chạy` đợt 02/11 |
| C2 Nhận hai lần đợt đầu | Đặt 10, nhận 4 rồi 6 | Received, Full | `Chạy` đợt 02/11 |
| K1 Thêm xe | Thanh "5 of 5" trên Vehicles | Save Vehicle quay mãi, không báo lỗi, xe không được tạo; lần trước đó tạo được. Giới hạn 5 xe là suy ra | `Chạy`, giới hạn `Suy` |
| K2 Trùng tên kho | Tạo TEST-KHO-01 lần 2 | "has already been taken", "Part Location could not be created" | `Chạy` |
| K3 Chỉnh giảm quá tồn | Tồn 10, chỉnh -20, lý do Lost | Lưu được, tồn -10, không cảnh báo | `Chạy`, part-adjust-dialog |
| K4 Chỉnh bằng số mới | Gõ New Quantity 0 | Adjust Quantity tự thành 10; hai ô liên động | `Chạy` |
| K5 Số lẻ | +0,5 | Tồn 6,5, chấp nhận | `Chạy` |
| K6 Lý do | Trống lý do | Save khoá. 11 lý do: Broken, Checked Inventory, Expired, Found, Lost, Miscellaneous, Received, Sold, Stolen, Transferred, Used | `Chạy` |
| K7 Chuyển quá tồn | Có 6,5, chuyển 100, nút Save vẫn mở | "Parts transfer was successful."; chỉ chuyển 6,5, sổ ghi -6,5 và +6,5, không báo đã cắt số | `Chạy`, part-transfer-dialog |
| K8 Chuyển khi hết | Tồn từ 0 trở xuống | Nút chuyển khoá | `Chạy` |
| K9 Kho đích | Có 2 kho | Chỉ hiện kho còn lại kèm tồn | `Chạy` |
| K10 Trừ kho khi lưu lệnh | PT-B 5 cái, WO Open | -5 ngay lúc lưu | `Chạy` |
| K11 Sửa số lượng dòng | 5 thành 3 | Sổ +2, loại Work Order #102 | `Chạy` |
| K12 Xuất quá tồn | PT-A 20, kho 9,5 | Không cảnh báo ở hộp Add Part, tồn -10,5. Hộp chỉ ghi "This will make an inventory adjustment" | `Chạy` |
| K13 Không trừ kho | Ô Part Location | Có lựa chọn "None (No Inventory Adjustment)" | `Chạy` |
| K14 Hoàn thành lệnh | Open sang Completed | Sổ không có dòng mới; sinh Service Entry; Edit khoá. Thiếu thì "Please edit and fix the following errors: Started At can't be blank", "Start Odometer can't be blank (per your account settings)" | `Chạy` |
| K15 Mở lại lệnh | Completed sang Open | "Changing this completed Work Order to an incomplete Status will automatically restore any archived parts, part locations, and contacts associated with line items."; sổ không đổi; liên kết Service Entry biến mất | `Chạy` |
| K16 Xoá dòng sau khi mở lại | Xoá PT-A 20, hộp "Are you sure you want to permanently delete this line item?" | Sổ +20, tồn về 9,5 | `Chạy` |
| K17 Giá khi nhập nhiều giá | Static: danh mục 100.000, đơn 90.000 | Unit Cost phụ tùng giữ 100.000; Total Inventory Value 13.750.000 = 131,5 x 100.000 + 2 x 300.000. FIFO, LIFO, Average không thử | `Chạy` Static |
| K18 Phụ tùng không có giá | PT-B | Giá trị tồn tính 0. Giá gõ lúc tạo không được lưu, chưa rõ vì sao | `Chạy` |
| K19 Bulk Manage | Tab theo kho; sửa ô | "All changes saved"; -1 thành 8, sổ loại Bulk Update +9, không hỏi lý do | `Chạy`, parts-bulk-manage |
| K20 Tắt kho khi có đơn | Gạt Active ở Bulk | Không tắt: "This part can't be deactivated because it's used in one or more purchase orders at this location." | `Chạy` |
| K21 Xoá cả lệnh | Hộp "All data will be lost forever." | Đã huỷ ở hộp xác nhận vì là xoá vĩnh viễn. Xoá lệnh có hoàn kho không vẫn chưa biết | Không chạy |
| K22 Nhiều nhà cung cấp | Thêm NCC-02 giá 110.000 trong Purchase History | Lưu được, trang phụ tùng vẽ biểu đồ giá 90.000 đến 110.000; đơn tự thêm dòng lịch sử | `Chạy` |
| K23 Thay thế, tương thích xe | Form phụ tùng | Không thấy trường nào; chỉ có Replaced Parts trong bảo hành ở lệnh. Chưa tìm ở nơi khác | `Xem` |

### Đơn mua

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| D1 Chọn nhà cung cấp | NCC-DAU chỉ có Fuel | Chỉ hiện nhà cung cấp có Parts; NCC-DAU không có | `Chạy` |
| D2 Tìm phụ tùng | PT-B không bật ở KHO-02 | Hiện tồn tại kho của đơn; PT-B xám, có khoá | `Chạy` |
| D3 Một đơn nhiều kho | Ô Part Location trên đơn | Không được: Part Location một giá trị cho cả đơn, khoá sau khi nhận | `Chạy` |
| D4 Dòng trùng | Hai dòng PT-A | "Part TEST-KHO-PT-A is duplicated", "Purchase Order could not be created" | `Chạy` |
| D5 Dòng số lượng 0 | Duyệt đơn có dòng 0 | Duyệt được, không chặn | `Chạy` |
| D6 Thuế, phí, giảm | Tạm tính 1.250.000, giảm 10%, Shipping 20.000, thuế 8% | Giảm -125.000, thuế 90.000, tổng 1.235.000: thuế tính trên phần sau giảm, không gồm phí | `Chạy` |
| D7 Lỗi ô Shipping | Gõ 20000 | Thành 2.000.000; gõ 200 mới ra 20.000. Ô Unit Cost của dòng thì đúng | `Chạy` |
| D8 Nhận thiếu | Nhận 5 trên 12 | Partial, lần sau gợi ý 7 | `Chạy`, po-receive-dialog |
| D9 Nhận vượt | Gõ 100 | Thành 105 trên 12, sau đó 110 trên 12: không chặn, không cảnh báo; tồn tăng đủ; tiền đơn vẫn theo số đặt | `Chạy` |
| D10 Vượt ở một dòng, dòng khác 0 | Hai dòng | Vẫn Partial | `Chạy` |
| D11 Trả hàng ở Receive | Gõ -5 | Thành nhận +5, mất dấu âm, không báo | `Chạy` |
| D12 Trả hàng bằng Make Adjustment | -6 trên 5 đã nhận, "Negative values are allowed up to the quantity received on this order." | Cắt còn -5, không báo; sổ -5, tồn 2 thành -3, về Partial; "Received in Full By" vẫn còn | `Chạy`, po-make-adjustment |
| D13 Đóng khi nhận thiếu | PT-B 0 trên 5, "Are you sure you want to close the selected purchase order?" | Đóng được, không ghi lý do | `Chạy`, po-closed-partial |
| D14 Nhận vào lệnh có sẵn | "These parts will be received to your inventory before being added to the selected work order." | Mở form lệnh với dòng ghi chú "From PO #2"; sổ +5 trước, -5 khi lưu lệnh | `Chạy`, po-receive-existing-wo |
| D15 Nhận vào lệnh mới, huỷ form | "Your received parts will remain in inventory even if you don't save this work order." | Hàng ở lại kho, đơn thành Full, không có lệnh | `Chạy` |
| D16 Copy | Make a Copy | Mở form mới điền sẵn, giữ giá đơn cũ, số tăng lên #3 | `Chạy` |
| D17 Duyệt đơn của mình | Một người dùng có quyền duyệt | Được, một cú bấm, không hộp xác nhận. Không kiểm được tách người vì tài khoản một người, không mời người ngoài | `Chạy` |

### Dầu

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| F1 Phiếu đầu | 2.000 km, 50 lít, 20.000 ₫ | Usage "N/A", không tiêu hao; tổng 1.000.000 | `Chạy` |
| F2 Đầy tiếp | 500 km, 40 lít | 29,40 mpg (US) bằng 12,5 km/lít, đúng, nhưng xe km, lít vẫn hiện mpg | `Chạy` |
| F3, F4 Không đầy rồi đầy | 2.700 km 10 lít partial, 3.000 km 20 lít | F3 không có tiêu hao; F4 39,20 mpg bằng 500 km trên 30 lít: cộng dồn phiếu partial, đúng | `Chạy` |
| F5, F6 Bỏ lần | 3.500 Reset usage, 3.800 | F5 không usage; F6 Usage "N/A" nhưng vẫn có 35,28 mpg bằng 300 km trên 20 lít | `Chạy` |
| F7 Personal | 10 lít | Tính tiêu hao bình thường; vẫn cộng vào Cost of Ownership | `Chạy` |
| F8 Số đồng hồ lùi cùng ngày | 2.900 khi đã có 4.000 | Lưu được, không báo; lấy phiếu trước theo số đồng hồ (2.700), Usage 200. F4 vẫn hiện 300 | `Chạy` |
| F9 Vượt bình | 100 lít, bình 60 | Có cảnh báo: icon Alerts, Capacity Exception Volume "100 liters". Khác bản trước của FR-022 | `Chạy`, fuel-history-capacity-alert |
| F9b Sửa phiếu vượt | 100 thành 50 lít | Cảnh báo không mất, cột vẫn 100 | `Chạy` |
| F13, F14 Biên bình | 60 lít; 60,5 lít | Bằng bình không cảnh báo; 60,5 có cảnh báo | `Chạy` |
| F1b Chưa khai dung tích | 50 lít | Không kiểm | `Chạy` |
| F11 0 lít | 4.800 km | Lưu được, tổng 0 ₫ | `Chạy` |
| F10 Void | Tick Void, trống số | "can't be blank"; ghi 50.000 thì lưu, số gạch ngang, đồng hồ xe vẫn 4.800, không Usage | `Chạy` |
| F12 Lùi ngày, số cao | 20/10, 9.000 km | "must be less than 1,000 or marked as void". Chưa rõ mốc 1.000 lấy từ đâu | `Chạy`, fuel-entry-odometer-backdate-error |
| F12b Lùi ngày, số thấp | 20/10, 900 km | Lưu được, không đổi phiếu sau | `Chạy` |
| F-NCC Nhà cung cấp trên phiếu | Mở ô chọn | Chỉ nhà cung cấp có Fuel: NCC-02, NCC-DAU; NCC-01 không có. Phiếu có NCC-DAU hiện bản đồ, phiếu không có ghi "Location is unknown or not available" | `Chạy` |
| F-Lọc Bộ lọc | Date, Vehicle, Vehicle Group, Vendor, Filters | Mở bộ lọc theo xe, có Add Filter, Add Filter Group; chỉ thử lọc xe | `Chạy` lọc xe |
| F-Thẻ Thẻ dầu | Fuel Card trên phiếu | Ô "No"; cài đặt WEX chỉ đọc; không có màn gán thẻ thử được. Không tích hợp | `Xem` |
| F-VLA Vendor Location Alert | Cần định vị và thẻ | Cần tích hợp nên chưa thử | Không chạy |
| F-Sạc Charging History | — | Ngoài phạm vi theo yêu cầu user, không xem | Không chạy |

### Tiền trên VND

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| T1 Chi tiết WO, dòng PT-B | Giá trị đúng 50.000 theo form sửa | Hiện 5.000.000 | `Chạy`, đã lặp lại |
| T2 Chi tiết WO, tổng; Service Entry | Giá trị đúng 2.550.000 | Hiện 255.000.000 | `Chạy`, đã lặp lại |
| T3 Fuel History, Total Fuel Cost | Đúng 8.010.000 cộng theo dòng | Hiện 80.100 | `Chạy`, đã lặp lại |
| T4 Fuel, Cost per km | Đúng 1.600 | Hiện 16 ₫ | `Chạy`, đã lặp lại |
| T5 Fuel History, Avg. Cost | Đúng khoảng 75.700 ₫/gallon | Hiện 757 ₫ | `Chạy`; giá trị đúng `Suy` |
| T6 Trang chi tiết xe | Fuel & Energy Costs | Đúng: 7.610.000, 1.770 ₫/km, tính cả Personal, Void; không tính phiếu 20/10 vì thẻ "This Month" | `Chạy` |
| T7 Hộp Add Part | Gõ 120000 | Form ra đúng; lệch chỉ xuất hiện ở trang chi tiết, Service Entry theo con số sai | `Chạy` |
| T8 Lưu form không đổi gì | Bấm lưu | Số trên chi tiết không tăng thêm, nhưng trang vẫn đứng ở form nên chưa chắc lần lưu đó đã chạy | `Chạy`, chưa chắc |

### Nhà cung cấp

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| N1 Trường bắt buộc | Trống Tên, Address, City, State, Zip, Country | "can't be blank" | `Chạy` |
| N2 Phân loại | Không chọn | Không bắt buộc, nhưng quyết định nơi được chọn | `Chạy` |
| N3 Tab theo phân loại | NCC-DAU chỉ Fuel; NCC-02 cả hai; NCC-01 Parts | NCC-DAU không có tab Purchase Orders; NCC-02 có Fuel Entries và Purchase Orders; tab đơn của NCC-01 liệt kê #3 và #2 | `Chạy` |
| N4 Network Status | "Network Status: Invite" | Không bấm | `Xem` |
| N5 Find Shops | Nút Add Vendors | Thấy, không mở | `Xem` |
| N6 Enter trong ô Country | Chọn quốc gia bằng Enter | Vừa chọn vừa lưu form, ba lần đều vậy; dễ tạo bản ghi sớm | `Chạy` |

## 7. Success Criteria

| ID | Outcome nghiệp vụ | Đo bằng | Mốc đạt |
|---|---|---|---|
| SC-fleetio-parts-purchasing-fuel-01 | Tồn hệ thống khớp thực tế | Chênh lệch khi kiểm kê | TBD |
| SC-fleetio-parts-purchasing-fuel-02 | Biết hàng đang về khi lập lệnh | Thẻ tồn đủ 4 số | Có sẵn |
| SC-fleetio-parts-purchasing-fuel-03 | Phát hiện đổ dầu bất thường | Tỉ lệ phiếu có cảnh báo được xử lý | TBD |

## 8. Data Entities (tóm tắt — chi tiết ở erd.md)

Part, Part Location, Part Stock, Inventory Activity, Purchase Order, PO Line, Part Vendor Price, WO Part Line, Vendor, Fuel Entry; Charging Entry ngoài phạm vi theo yêu cầu user. Xem [[docs/_research/fleetio/srs/fleetio-parts-purchasing-fuel-erd.md|ERD]].

## 9. Flows (tóm tắt — chi tiết ở flows.md)

Xem [[docs/_research/fleetio/srs/fleetio-parts-purchasing-fuel-flows.md|Flows]], [[docs/_research/fleetio/srs/fleetio-parts-purchasing-fuel-states.md|States]], [[docs/_research/fleetio/srs/fleetio-parts-purchasing-fuel-usecases.md|Use case]], [[docs/_research/fleetio/srs/fleetio-parts-purchasing-fuel-userflow.md|User flow]].

## 10. Screens

Ảnh thật và bảng mô tả: [[docs/_research/fleetio/srs/fleetio-parts-purchasing-fuel-screens.md|Màn hình]]. Không áp `CMP`, `GR` vì mô tả sản phẩm của bên khác.

## 11. Constraints, Dependencies & Assumptions

| Giả định | Invalidate nếu sai |
|---|---|
| Tính giá Static Pricing đang bật trên tài khoản dùng thử, đọc được ở cài đặt, không đổi khi chạy | Quy tắc đơn giá phải đọc lại theo phương pháp khác |
| `GĐ` Quy trình cây dầu Delta giữ nguyên, chỉ học luật cảnh báo | Cần viết lại phần nhiên liệu |
| Tài khoản chỉ có một người dùng có quyền duyệt, không mời người ngoài | Nhánh Pending Approval, Rejected và tách người phải chạy lại |

## 12. Open Questions

* [ ] OQ-1: Delta có cho xuất âm, trừ kho lúc nào? Fleetio: cho âm, trừ khi lưu dòng lệnh — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-2: Tính giá tồn theo phương pháp nào? — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-3: Duyệt đơn theo ngưỡng, có tự duyệt không? — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-4: Có nhận hàng thẳng vào lệnh không? Fleetio luôn đi qua kho hai bước — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-5: Có cần cảnh báo vị trí đổ dầu ở cây dầu ngoài không? — Nguồn khách: chưa có trong tài liệu khách gửi
* [x] OQ-6: Fleetio có huỷ đơn sau Approved, đóng đơn nhận thiếu, nhận vượt số đặt, trả hàng, gửi lại đơn Rejected không? Đã trả lời: không có nút huỷ sau Approved, chỉ Delete hoặc lùi Draft; đóng được khi nhận thiếu; nhận vượt được; trả hàng qua Make Adjustment, ở Full và Closed. Gửi lại đơn Rejected chưa trả lời được vì tài khoản một người, chuyển sang OQ-8 — Nguồn khách: không áp dụng
* [x] OQ-7: Xoá lệnh hoặc dòng phụ tùng có hoàn kho không? Đã trả lời: xoá dòng có hoàn kho (K16). Xoá lệnh chưa thử, chuyển sang OQ-9 — Nguồn khách: không áp dụng
* [ ] OQ-8: Pending Approval, Rejected chạy thế nào, đơn Rejected có gửi lại được không? Cần tài khoản có người không có quyền duyệt — Nguồn khách: không áp dụng
* [ ] OQ-9: Xoá cả lệnh có hoàn kho không? Đã huỷ ở hộp xác nhận (K21) — Nguồn khách: không áp dụng
* [ ] OQ-10: Delete đơn mua ảnh hưởng gì đến tồn và sổ kho? Chưa bấm — Nguồn khách: không áp dụng
* [ ] OQ-11: Dưới FIFO, LIFO, Average: giá trị tồn, sửa giá sau khi nhận, nhận vào lệnh chạy thế nào? Không đổi cài đặt nên chưa thử — Nguồn khách: không áp dụng
* [ ] OQ-12: Đổi vị trí dòng lệnh sang None thì sổ kho ghi gì? Chưa thử — Nguồn khách: không áp dụng
* [ ] OQ-13: Đơn Draft có tính vào Pending PO Qty không? Chưa đo riêng — Nguồn khách: không áp dụng
* [ ] OQ-14: Vendor Location Alert kích hoạt thế nào khi có định vị và thẻ? Cần tích hợp — Nguồn khách: không áp dụng
* [ ] OQ-15: Find Shops, Network Status: Invite làm gì? Thấy, không mở — Nguồn khách: không áp dụng
* [ ] OQ-16: Vì sao giá gõ lúc tạo phụ tùng PT-B không được lưu? (K18) — Nguồn khách: không áp dụng
* [ ] OQ-17: Tồn về 0 khi điểm đặt lại bằng 0 thì nhãn gì? Chưa thử (S4) — Nguồn khách: không áp dụng
* [ ] OQ-18: Mốc 1.000 trong câu "must be less than 1,000 or marked as void" lấy từ đâu? (F12) — Nguồn khách: không áp dụng
* [ ] OQ-19: Thay thế, tương thích xe có ở nơi khác ngoài form phụ tùng không? (K23) — Nguồn khách: không áp dụng
* [ ] OQ-20: Có tách được người lập và người duyệt không? Không kiểm được với tài khoản một người (D17) — Nguồn khách: không áp dụng
* [ ] OQ-21: Khi nhận vượt, trả quá số, đóng thiếu, Delta muốn chặn, cảnh báo hay chỉ ghi nhận? — Nguồn khách: chưa có trong tài liệu khách gửi
