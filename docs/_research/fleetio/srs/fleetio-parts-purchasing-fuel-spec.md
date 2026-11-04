---
type: research
feature: fleetio-parts-purchasing-fuel
status: draft
status_changed: 2026-11-03
status_reason: "đã review upstream, không cần sửa"
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
| FR-fleetio-parts-purchasing-fuel-001 | Danh mục phụ tùng | Mã duy nhất, mô tả, nhóm, hãng, mã hãng, UPC, đơn giá, đơn vị, bảo hành, ảnh, tài liệu. Không có trường thay thế, tương thích xe trong form, danh sách, menu phụ tùng (K23, K24, K26); danh sách có cột Linked Service Tasks (K25). Đơn giá gõ lúc tạo có lần không được lưu (K18). | P0 | [Gói: Bảo dưỡng đội xe] | demo | Đợt đầu, K18, K23–K26 | `Chạy` lượt 3: Form không có thay thế, tương thích | Lấy cho `product-catalog`, thêm tương thích xe và phụ tùng thay thế |
| FR-fleetio-parts-purchasing-fuel-002 | Kho và hoạt động theo kho | Phụ tùng bật tại nhiều kho, mỗi kho có vị trí dãy, hàng, ô; số lượng; điểm đặt lại. Tên kho không trùng. Kho khai ở Settings; bật phụ tùng tại kho thì nhập tồn đầu, ghi Initial. | P0 | [Gói: Bảo dưỡng đội xe] | test | K2, K20, luồng kho | `Chạy` | Lấy |
| FR-fleetio-parts-purchasing-fuel-003 | Thẻ tồn | Theo kho: Current Qty, Reorder Point, Pending PO Qty, WO Current Qty; bốn nút điều chỉnh, chuyển kho, đặt mua, menu (Edit, View History). Cách tính Pending PO Qty xem FR-fleetio-parts-purchasing-fuel-039. | P0 | [Gói: Bảo dưỡng đội xe] | demo | Mục Tồn kho | `Chạy` | Lấy cho `stock-movement`, hợp nhiều bãi đầu kéo, mooc |
| FR-fleetio-parts-purchasing-fuel-004 | Sổ kho | Mỗi biến động ghi ngày, kho, loại, chứng từ, lý do, nhà cung cấp, số biến động, số trước, số sau, người, ghi chú. Sáu loại: Initial, Manual, Transfer, Purchase Order, Work Order, Bulk Update. Câu ghi đi theo nguồn: "Received: -1.0" khi điều chỉnh đơn (D18), "Adjustment: 9.5 → 0.0" khi sửa ở Bulk (S8). | P0 | [Gói: Bảo dưỡng đội xe] | test | K3–K19, D18, S8 | `Chạy` đủ sáu loại | Lấy |
| FR-fleetio-parts-purchasing-fuel-005 | Điều chỉnh tồn | Hộp theo một kho: Adjust Quantity và New Quantity liên động, lý do bắt buộc trong 11 giá trị, ghi chú, chấp nhận số lẻ. Không chặn giảm quá tồn. Hàng loạt xem FR-fleetio-parts-purchasing-fuel-025. | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | test | K3–K6 | `Chạy` (bản trước `Docs`) | Lấy cho `inventory-count`, cảnh báo khi xuống âm; danh sách lý do là tham số mới, chưa có mã |
| FR-fleetio-parts-purchasing-fuel-006 | Chuyển kho | Nhập số chuyển, chọn kho đích, danh sách đích chỉ gồm kho còn lại kèm tồn. Nút khoá khi tồn từ 0 trở xuống. Nhập quá tồn thì cắt về tồn hiện có, vẫn báo thành công. | P1 | [Gói: Bảo dưỡng đội xe] | test | K7–K9 | `Chạy` (bản trước `Docs`) | Lấy, chặn hoặc báo rõ số đã chuyển |
| FR-fleetio-parts-purchasing-fuel-007 | Cảnh báo tồn thấp | Nhãn theo từng kho: Low Stock khi tồn trên 0 và từ điểm đặt lại trở xuống, số màu cam; Out of Stock khi từ 0 trở xuống. Điểm đặt lại 0: tồn 0 là Out of Stock, không hiện Low Stock; tồn 0,5 không nhãn (S5, S6). Danh sách Parts tô đỏ Total Quantity khi một kho hết dù tổng còn nhiều (S9). Gửi email theo tài liệu hãng, không chạy vì không gửi email (S10). | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | test | S1–S10 | `Chạy` một phần lượt 3: Biên tồn 0 chạy; email giữ Docs | Lấy; điểm đặt lại theo từng kho |
| FR-fleetio-parts-purchasing-fuel-008 | Tính giá tồn | Chọn một trong Average Cost, FIFO, LIFO, Static Pricing. Static: Unit Cost phụ tùng giữ theo danh mục dù đơn mua giá khác; Total Inventory Value theo Unit Cost; phụ tùng không giá tính 0. FIFO, LIFO, Average chưa đổi, chưa đo giá xuất kho; chỉ đọc câu chữ màn đổi, xem FR-fleetio-parts-purchasing-fuel-045 (K29–K37). | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | phân tích | K17, K18, K29–K37 | `Chạy` Static; `Xem` ba phương pháp còn lại | Cần kế toán Delta quyết |
| FR-fleetio-parts-purchasing-fuel-009 | Lập đơn mua | Một nhà cung cấp, một kho rồi mới thêm dòng; chỉ hiện nhà cung cấp có Parts; đơn giá lấy từ danh mục, sửa được; giảm giá, phí vận chuyển, thuế; tài liệu. Lưu được đơn 0 dòng; dòng trùng bị chặn; dòng số lượng 0 không bị chặn. | P0 | [Gói: Bảo dưỡng đội xe] | demo | D1–D7 | `Chạy` | Lấy cho `purchasing`, chặn dòng số lượng 0 |
| FR-fleetio-parts-purchasing-fuel-010 | Duyệt đơn | Có quyền duyệt thì Save & Approve hoặc Approve, một cú bấm, không hộp xác nhận, duyệt được đơn của mình. Không có quyền thì Submit for Approval, người có quyền duyệt hoặc từ chối; nhánh này không chạy được vì cần người thứ hai không có quyền duyệt (D32). | P0 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | test | D17, D32, ma trận đơn | `Chạy` nhánh có quyền; `Docs` nhánh còn lại | Lấy, thêm nhiều cấp nếu Delta cần, tách người lập và người duyệt theo cấu hình |
| FR-fleetio-parts-purchasing-fuel-011 | Một nút chính mỗi bước | Approve, Mark as Purchased, Receive, Close; ghi người và thời điểm mỗi bước. | P0 | [Gói: Bảo dưỡng đội xe] | demo | Ma trận đơn | `Chạy` | Lấy |
| FR-fleetio-parts-purchasing-fuel-012 | Nhận hàng | Bảng Item, Total Received, Total Ordered, Receive; nhận nhiều lần, lần sau gợi ý số còn lại. Không chặn nhận vượt. Trạng thái tính theo từng dòng: vượt ở một dòng, dòng khác 0 vẫn Partial. | P0 | [Gói: Bảo dưỡng đội xe] | test | D8–D11 | `Chạy` | Lấy, cảnh báo nhận vượt theo tham số mới, chưa có mã |
| FR-fleetio-parts-purchasing-fuel-013 | Nơi đến khi nhận | Inventory, Existing work order, New work order. Hai nhánh lệnh đều nhập kho trước, trừ khi lưu lệnh, dòng ghi chú "From PO #n". `Docs`: chỉ với Static Pricing; phương pháp khác chưa thử. | P1 | [Gói: Bảo dưỡng đội xe] | demo | D14, D15 | `Chạy` Inventory và lệnh có sẵn; lệnh mới `Chạy` đến bước huỷ form | Lấy, cả hai bút toán |
| FR-fleetio-parts-purchasing-fuel-014 | Xuất phụ tùng cho lệnh | Chọn phụ tùng thấy tồn từng kho; lấy từ kho hoặc None không trừ kho; gắn đầu việc. Trừ ngay khi lưu. Không cảnh báo khi vượt tồn. | P0 | [Gói: Bảo dưỡng đội xe] | test | K10, K12, K13 | `Chạy` | Lấy, thêm kiểm tồn |
| FR-fleetio-parts-purchasing-fuel-015 | Nhà cung cấp | Tên, địa chỉ, thành phố, tỉnh, mã bưu chính, quốc gia bắt buộc; liên hệ; phân loại Charging, Fuel, Parts, Service, Vehicle không bắt buộc nhưng quyết định nơi được chọn; nhãn; đánh giá là số: bộ lọc có "Vendor Rating", "is equal to", ô "Search number" (N13); cột Rating hiện "...", rê chuột "Rating not available" ở cả 20 nhà cung cấp (N14), form sửa, danh sách, Find Shops không thấy nơi nhập hay sinh điểm, nguồn điểm chưa rõ (N10, N15). Danh sách có cột Labels, Archived At, tab Archived; trang chi tiết có thêm Tools Vendor (N9). Sạc ngoài phạm vi theo yêu cầu user. | P1 | [Cấu hình] | test | D1, N1, N2, N9, N10, F-NCC | `Chạy` một phần lượt 4: Rating là số; nguồn điểm chưa rõ | Lấy cho `business-partners`, bỏ bắt mã bưu chính |
| FR-fleetio-parts-purchasing-fuel-016 | Tạo nhanh trong ô chọn | Gõ tên chưa có thì chọn Create, mở form với tên điền sẵn và phân loại theo ngữ cảnh. | P1 | [Lõi] | demo | Đợt đầu | `Chạy` | Lấy, cần chọn rõ ràng |
| FR-fleetio-parts-purchasing-fuel-017 | Phiếu dầu | Xe, ngày, số đồng hồ, số lít, đơn giá, loại dầu, nơi đổ, tham chiếu, ảnh, tài liệu. Nơi đổ chỉ gồm nhà cung cấp có Fuel; có nhà cung cấp thì hiện bản đồ và tạo vị trí xe, xem FR-fleetio-parts-purchasing-fuel-042. Lưu được 0 lít. | P0 | [Gói: Nhiên liệu] | demo | F1, F11, F-NCC | `Chạy` | Đối chiếu `fuel-issuing`, chặn 0 lít |
| FR-fleetio-parts-purchasing-fuel-018 | Tính tiêu hao | Từ phiếu trước theo số đồng hồ: quãng đường, tiêu hao, chi phí trên km, chênh so với lần trước. Cộng dồn phiếu Partial. Tính đúng nhưng xe km, lít vẫn hiện mpg. | P0 | [Gói: Nhiên liệu] | test | F1–F6 | `Chạy` | Lấy, dùng lít trên 100 km |
| FR-fleetio-parts-purchasing-fuel-019 | Cờ phiếu dầu | Personal vẫn tính tiêu hao, vào Cost of Ownership và cộng vào thẻ tổng Fuel History (F22). Partial cộng dồn sang phiếu sau. Reset usage: phiếu đó không usage, phiếu sau Usage "N/A" nhưng vẫn có tiêu hao. | P1 | [Gói: Nhiên liệu] | test | F3–F7, F20, F22 | `Chạy` lượt 3: Void, Personal vẫn cộng thẻ tổng | Lấy Đổ một phần, Đặt lại; hợp đầu kéo đổ nhiều cây dầu; hiện rõ Usage sau Reset |
| FR-fleetio-parts-purchasing-fuel-020 | Thẻ tổng hợp dầu | Tổng tiền, tổng lượng, tiêu hao trung bình, chi phí trung bình theo bộ lọc, tính lại khi đổi lọc. Tính cả phiếu Void, Personal (F22). Trên VND sai 100 lần: 80.100 ₫ so với 8.010.000 ₫ (T9), 22.100 ₫ so với 2.210.000 ₫ khi lọc (T10). | P1 | [Gói: Nhiên liệu] | demo | T3–T5, T9, T10, F16, F22 | `Chạy` | Lấy cho `fuel-stations`, sửa tiền |
| FR-fleetio-parts-purchasing-fuel-021 | Cảnh báo sai vị trí | Vị trí xe khi đổ xa nhà cung cấp hơn bán kính đặt thì gắn Vendor Location Alert; tắt được. Chỉ thấy tên loại ở bộ lọc (F18); không chạy được vì cần tích hợp thẻ, định vị (F23). | P1 | [Gói: Giám sát nhiên liệu] [Cấu hình] | test | F-VLA, F18, F23 | `Xem` cấu hình, `Docs`; không chạy vì cần tích hợp | Lấy, bán kính là tham số mới, chưa có mã |
| FR-fleetio-parts-purchasing-fuel-022 | Cảnh báo vượt dung tích | Số lít lớn hơn dung tích bình đã khai thì gắn Capacity Alert và ghi Capacity Exception Volume, kể cả phiếu nhập tay. Bằng dung tích không cảnh báo; chưa khai không kiểm. Sửa phiếu không gỡ cảnh báo. Bản trước ghi nhập tay không kích hoạt là sai. | P1 | [Gói: Giám sát nhiên liệu] | test | F9, F9b, F13, F14, F1b | `Chạy` | Lấy, chỉ cần dung tích bình; đầu kéo khai đúng tổng bình; tính lại khi sửa phiếu |
| FR-fleetio-parts-purchasing-fuel-023 | Phiên sạc | Ngoài phạm vi theo yêu cầu user. Ghi nhận cũ: giờ bắt đầu, kết thúc, thời lượng, điện năng, đơn giá, chi phí, chi phí trên km. | P2 | [Cấu hình] | demo | F-Sạc | `Xem` cột ở đợt đầu, không xem thêm | Ngoài phạm vi theo yêu cầu user |
| FR-fleetio-parts-purchasing-fuel-024 | Công cụ | Quản lý công cụ, gán người, nhắc riêng; nhắc không tự lặp, resolve xong phải tạo lại; là gói thêm. | P2 | [Gói: Bảo dưỡng đội xe] | demo | Tài liệu hãng | `Docs` | Cân nhắc, nên cho nhắc lặp |
| FR-fleetio-parts-purchasing-fuel-025 | Bulk Manage Parts | Tab theo kho; cột Aisle, Row, Bin, Active?, Track Inventory, Current Qty, Last Quantity Update; sửa ô là tự lưu, sổ loại Bulk Update, không hỏi lý do, kể cả đưa tồn về 0 (S8); Print Worksheet xem FR-fleetio-parts-purchasing-fuel-041. | P2 | [Gói: Bảo dưỡng đội xe] | test | K19, K20, S8 | `Chạy` lượt 3: Print Worksheet tự tải PDF | Lấy cho `inventory-count`, gắn đợt kiểm kê hoặc lý do |
| FR-fleetio-parts-purchasing-fuel-026 | Nhiều nhà cung cấp, lịch sử giá | Thêm nhà cung cấp, giá trong Purchase History; đơn mua tự thêm dòng lịch sử; trang phụ tùng vẽ biểu đồ giá. | P2 | [Gói: Bảo dưỡng đội xe] | demo | K22 | `Chạy` | Lấy |
| FR-fleetio-parts-purchasing-fuel-027 | Sửa, xoá dòng phụ tùng trên lệnh | Sửa số lượng hoặc xoá dòng thì sổ ghi bù, loại Work Order kèm số lệnh; xoá có hộp xác nhận. | P0 | [Gói: Bảo dưỡng đội xe] | test | K11, K16 | `Chạy` | Lấy |
| FR-fleetio-parts-purchasing-fuel-028 | Make Adjustment trên đơn | Có ở Full, Closed; không có ở Partial, Purchased. Tick từng dòng rồi nhập; bảng Item, Total Received, Total Ordered, Adjustment; nút Make Adjustment mờ tới khi tick; số âm tới mức đã nhận; quá thì cắt không báo; ghi sổ. Từ Full về Partial, "Received in Full By" vẫn còn. Từ Closed vẫn Closed: đổi số nhận và tồn mà không mở lại đơn, không hỏi lý do (D18). | P1 | [Gói: Bảo dưỡng đội xe] | test | D12, D18 | `Chạy` lượt 3: Từ Closed: giảm 1, vẫn Closed | Lấy cơ chế, báo khi cắt, xoá dấu nhận đủ khi lùi |
| FR-fleetio-parts-purchasing-fuel-029 | Đóng đơn | Close từ Partial, Full; hộp xác nhận; đóng được khi nhận thiếu, không ghi lý do; ghi Closed By. Không có nút mở lại. Không có trạng thái, nút huỷ riêng. | P1 | [Gói: Bảo dưỡng đội xe] | test | D13, ma trận đơn | `Chạy` | Bắt lý do khi đóng thiếu, thêm trạng thái Huỷ |
| FR-fleetio-parts-purchasing-fuel-030 | Sửa đơn theo trạng thái | Draft: nhà cung cấp, kho mở, có Add Line Item, nút xoá dòng, "Save as Draft", "Save & Approve". Approved: đủ trường, thêm bớt dòng được, "Save as Draft", "Save & Approve". Purchased, Partial, Full: khoá nhà cung cấp, kho, không thêm bớt dòng; sửa số, giá được; nút "Save Purchase Order"; Purchased còn sửa được Label, Description, Discount, Shipping, Tax, không cảnh báo đã gửi nhà cung cấp. Draft đổi kho, nhà cung cấp không xoá dòng, không hỏi lại; xoá dòng không có hộp xác nhận (D38). Full tăng số đặt vẫn "Received, Full", không có Receive dù còn thiếu (D36, D37). Closed vẫn Edit đơn giá, tổng tính lại. | P1 | [Gói: Bảo dưỡng đội xe] | test | Ma trận đơn, D26, D30, D31, D36–D38 | `Chạy` lượt 4: Draft, Full lưu thật | Khoá giá từ khi đóng |
| FR-fleetio-parts-purchasing-fuel-031 | Lùi trạng thái đơn | Save as Draft từ Approved về Draft, nằm trong form Edit, không có trong menu; mất dòng Approved By. Unmark as Purchased từ Purchased về Approved, một cú bấm. Make Adjustment từ Full về Partial. Lùi trạng thái không giảm Pending PO Qty (D27–D29); Purchase Date, Purchased By vẫn in trên PDF (D35). | P1 | [Gói: Bảo dưỡng đội xe] | test | PO #2, PO #3, PO #4, D12, D27–D29, D33, D35 | `Chạy` | Lấy, giữ lịch sử người duyệt cũ |
| FR-fleetio-parts-purchasing-fuel-032 | Sao chép đơn | Make a Copy mở form mới điền sẵn nhà cung cấp, kho, dòng, số đặt, giá đơn cũ, chiết khấu; số tăng lên; không chép số đã nhận; lưu ra Draft. Có trong menu Approved, Purchased, Closed. | P2 | [Gói: Bảo dưỡng đội xe] | demo | D16, D21, D33 | `Chạy` | Lấy |
| FR-fleetio-parts-purchasing-fuel-033 | Void phiếu dầu | Tick Void, số đồng hồ vẫn bắt buộc; lưu thì số gạch ngang, đồng hồ xe không đổi, không Usage; vẫn tính vào chi phí xe và vẫn cộng vào Total Volume, Total Fuel Cost của Fuel History (F22). Nên Void chỉ là bỏ qua đồng hồ, không phải huỷ phiếu. | P1 | [Gói: Nhiên liệu] | test | F10, F22, T6 | `Chạy` | Lấy, không cộng chi phí |
| FR-fleetio-parts-purchasing-fuel-034 | Bộ lọc phiếu dầu | Date, Vehicle, Vehicle Group, Vendor, Filters; panel có Add Filter, Add Filter Group, Fleetio: tối đa 3 nhóm OR. Date mặc định 30 ngày gần nhất, có biểu tượng khoá. Vendor liệt kê mọi nhà cung cấp, khác form phiếu chỉ cho Fuel. Trường lọc: Date, Fuel Alert Type, Fuel Transaction, Fuel Type, Partial, Personal, Reference, Reset, Transaction Card Number, Transaction Driver ID, Transaction Driver Name, Transaction Vehicle ID, Vendor, Void Status; 24 trường Vehicle; 6 trường Vendor. Xoá điều kiện áp ngay; thêm điều kiện phải bấm Apply. | P2 | [Gói: Nhiên liệu] | demo | F-Lọc, F15–F21 | `Chạy` lượt 3: Vendor, Alert Type, Personal chạy | Lấy |
| FR-fleetio-parts-purchasing-fuel-035 | Trang nhà cung cấp | Tab Overview, Fuel Entries, Purchase Orders theo phân loại; tab đơn liệt kê đơn của nhà cung cấp. "Network Status: Invite" không bấm vì mời người ngoài (N11). Find Shops xem FR-fleetio-parts-purchasing-fuel-040. | P2 | [Cấu hình] | demo | N3–N5, N11 | `Chạy` một phần lượt 3: Find Shops chạy, không thêm; Invite chặn | Lấy tab |
| FR-fleetio-parts-purchasing-fuel-036 | Thẻ dầu trên phiếu | Ô Fuel Card ghi "No"; cấu hình WEX chỉ đọc; không có màn gán thẻ thử được. Dữ liệu thẻ gắn ở mức phiếu: bộ lọc có Transaction Card Number, Transaction Driver ID, Transaction Driver Name, Transaction Vehicle ID. | P2 | [Gói: Nhiên liệu] | demo | F-Thẻ, F24 | `Xem` | Tìm đối tác Việt Nam |
| FR-fleetio-parts-purchasing-fuel-037 | In và lịch sử bản ghi đơn | Print: mở tab "Preparing your PDF...", ra `purchase_order_{số}.pdf` một trang gồm thông tin đơn, người và ngày từng bước, dòng hàng, Subtotal, Discount, Shipping, Tax, Total, Description; đầu trang in tên, địa chỉ tài khoản; tiền kiểu US. View Record History: hộp có ô "Select Date Range", cột Date, Changes By, Changes Made; ghi từng chuyển trạng thái và đổi tiền; phần ảnh đọc được không có dòng số nhận (D20, OQ-22). | P2 | [Gói: Bảo dưỡng đội xe] | demo | Ma trận đơn, D19, D20, D34, D35 | `Chạy` lượt 3: PDF, Record History, thêm Make a Copy | Lấy |
| FR-fleetio-parts-purchasing-fuel-038 | Tác động của hoàn thành, mở lại lệnh | Hoàn thành: sổ không có dòng mới, sinh Service Entry, Edit khoá; cần Started At, Start Odometer theo cài đặt. Mở lại: sổ không đổi, liên kết Service Entry biến mất, phần archive được khôi phục theo câu báo. | P1 | [Gói: Bảo dưỡng đội xe] | test | K14, K15 | `Chạy` | Lấy, giữ dấu Service Entry đã huỷ |
| FR-fleetio-parts-purchasing-fuel-039 | Số đang về theo trạng thái đơn | Đơn chưa Edit: Draft, Approved không tính, tính từ Purchased. Đơn Draft đã Edit và lưu: số vào Pending ngay dù chưa duyệt, theo số mới mỗi lần lưu (D40, D41). Sửa số đặt ở Purchased cập nhật ngay. Sửa tăng số đặt ở Full không cộng Pending (D37). Lùi về Approved, Draft không giảm; mua lại không nhân đôi. | P1 | [Gói: Bảo dưỡng đội xe] | test | D22–D29, D37, D40, D41 | `Chạy` một phần lượt 4: Đo PO #4, #5; Approved đã Edit chưa đo | Tính theo trạng thái hiện tại của đơn, không ghi lúc lưu form; đơn nháp không vào số đang về |
| FR-fleetio-parts-purchasing-fuel-040 | Tìm xưởng (Find Shops) | Hộp "Select service shops and easily save them to your vendors list", ô "Enter address, city or ZIP/postal code", ô "Shop type", "Let's Go". Ra khoảng 30 cửa hàng kèm bản đồ, chữ "All Results". Tick thì hiện "SELECTED", "Clear selection", ghim đổi đỏ, nhãn khoảng cách, nút "Add Vendor". | P2 | [Cấu hình] | demo | N7, N8 | `Chạy` tới bước tick; Add Vendor không bấm | Cân nhắc, cần nguồn dữ liệu xưởng ở Việt Nam |
| FR-fleetio-parts-purchasing-fuel-041 | Phiếu kiểm kê in | Print Worksheet ở Bulk Manage: một cú bấm, không mở tab, tự tải PDF theo kho đang chọn. PDF một trang: tên, địa chỉ tài khoản; Part, Category, Manufacturer, Aisle, Row, Bin, Current Qty kèm mốc thời gian, ô trống New Qty để kiểm đếm tay. Một cú bấm ra 3 file giống hệt. | P2 | [Gói: Bảo dưỡng đội xe] | demo | K27, K28 | `Chạy` | Lấy cho `inventory-count`, tải đúng một file |
| FR-fleetio-parts-purchasing-fuel-042 | Phiếu dầu tạo vị trí xe | Form phiếu dầu không có ô vị trí. Chọn nhà cung cấp trên phiếu thì Location History có một dòng "Fuel Entry" tại địa chỉ nhà cung cấp, xe hiện trên Fleet Map; form không báo. Chi tiết ở FR-fleetio-location-dispatch-004. | P1 | [Gói: Nhiên liệu] | test | F25 | `Chạy` | Cân nhắc, nếu lấy thì báo rõ trên form |
| FR-fleetio-parts-purchasing-fuel-043 | Loại cảnh báo dầu | Fuel Alert Type có đúng 3 giá trị: "Vendor Location Alert", "Fuel Capacity Alert", "Missing GPS Location Alert". Lọc được theo loại. | P2 | [Gói: Giám sát nhiên liệu] | demo | F18, F19, F23 | `Chạy` lọc Fuel Capacity Alert; hai loại còn lại `Xem` tên | Lấy cách lọc theo loại; Missing GPS cần xác định điều kiện |
| FR-fleetio-parts-purchasing-fuel-044 | Menu trang phụ tùng | "Update Quantity", "Archive" (mờ với PT-A), "View Record History". | P2 | [Gói: Bảo dưỡng đội xe] | demo | K26 | `Xem` | Lấy, nêu lý do khi Archive bị khoá |
| FR-fleetio-parts-purchasing-fuel-045 | Đổi phương pháp tính giá tồn | Settings › Parts & Inventory › Inventory Valuation Method: 4 radio có mô tả, không có nút Save. Chọn radio khác mới hiện khối cảnh báo, ô tích "I am aware the change I am about to make is permanent and can not be reversed" và nút "Activate" xám tới khi đủ điều kiện. Hai link trên hộp mở danh sách bản ghi chặn ở tab mới; chỉ lệnh chưa xong có dòng phụ tùng mới tính (K39, K42). Không có bản xem thử giá trị tồn. | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | phân tích | K30–K44 | `Xem` câu chữ; chưa bấm Activate, chưa đo giá | Chốt phương pháp cùng kế toán trước go-live; lấy cách chặn trước khi đổi, thêm xem thử tác động |

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
| BR-fleetio-parts-purchasing-fuel-007 | Tài liệu hãng: điểm đặt lại phải lớn hơn 0. Thực tế lưu được 0, tồn dương không nhãn, tồn 0 là Out of Stock. | [Gói: Bảo dưỡng đội xe] | Khai kho | FR-fleetio-parts-purchasing-fuel-007 | `Docs`; `Chạy` trái tài liệu (S4–S7) |
| BR-fleetio-parts-purchasing-fuel-008 | Lùi được từ Purchased về Approved bằng Unmark as Purchased, một cú bấm, không hỏi. | [Gói: Bảo dưỡng đội xe] | Sửa đơn | FR-fleetio-parts-purchasing-fuel-031 | `Chạy` (bản trước `Docs`) |
| BR-fleetio-parts-purchasing-fuel-009 | Tự đóng khi nhận đủ nếu bật; khi tắt phải Close tay. | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Nhận đủ | FR-fleetio-parts-purchasing-fuel-011 | `Xem` cấu hình; `Chạy` nhánh tắt |
| BR-fleetio-parts-purchasing-fuel-010 | Trạng thái đơn mua do hệ thống cố định. | [Gói: Bảo dưỡng đội xe] | Cấu hình | FR-fleetio-parts-purchasing-fuel-011 | `Xem` |
| BR-fleetio-parts-purchasing-fuel-011 | Phiếu đầu không có tiêu hao, cần phiếu trước. | [Gói: Nhiên liệu] | Lưu phiếu | FR-fleetio-parts-purchasing-fuel-018 | `Chạy` (F1) |
| BR-fleetio-parts-purchasing-fuel-012 | Vendor Location Alert cần có cả tích hợp nhiên liệu và thiết bị định vị. Không áp cho Capacity Alert, xem BR-fleetio-parts-purchasing-fuel-031. | [Gói: Giám sát nhiên liệu] | Có giao dịch | FR-fleetio-parts-purchasing-fuel-021 | `Docs` |
| BR-fleetio-parts-purchasing-fuel-013 | Chỉnh tồn không chặn giảm quá tồn, không cảnh báo. | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Chỉnh tồn | FR-fleetio-parts-purchasing-fuel-005 | `Chạy` (K3) |
| BR-fleetio-parts-purchasing-fuel-014 | Chuyển kho cắt số về tồn hiện có, không báo đã cắt; khoá khi tồn từ 0 trở xuống. | [Gói: Bảo dưỡng đội xe] | Chuyển kho | FR-fleetio-parts-purchasing-fuel-006 | `Chạy` (K7, K8) |
| BR-fleetio-parts-purchasing-fuel-015 | Sửa số lượng hoặc xoá dòng phụ tùng trên lệnh thì sổ ghi bù đúng chênh lệch. | [Gói: Bảo dưỡng đội xe] | Sửa, xoá dòng | FR-fleetio-parts-purchasing-fuel-027 | `Chạy` (K11, K16) |
| BR-fleetio-parts-purchasing-fuel-016 | Hoàn thành hoặc mở lại lệnh không tạo dòng sổ kho. | [Gói: Bảo dưỡng đội xe] | Đổi trạng thái lệnh | FR-fleetio-parts-purchasing-fuel-038 | `Chạy` (K14, K15) |
| BR-fleetio-parts-purchasing-fuel-017 | Một đơn một nhà cung cấp, một kho; khoá hai ô này từ Purchased trở đi, không phải từ lúc nhận như bản trước; Draft, Approved còn mở. | [Gói: Bảo dưỡng đội xe] | Lập, sửa đơn | FR-fleetio-parts-purchasing-fuel-009 | `Chạy` (D3, D26); Draft, Full `Xem` form (D30, D31) |
| BR-fleetio-parts-purchasing-fuel-018 | Một phụ tùng chỉ một dòng trong đơn. | [Gói: Bảo dưỡng đội xe] | Lưu đơn | FR-fleetio-parts-purchasing-fuel-009 | `Chạy` (D4) |
| BR-fleetio-parts-purchasing-fuel-019 | Đơn 0 dòng lưu được, Approve khoá; dòng số lượng 0 duyệt được. | [Gói: Bảo dưỡng đội xe] | Duyệt | FR-fleetio-parts-purchasing-fuel-010 | `Chạy` (D5) |
| BR-fleetio-parts-purchasing-fuel-020 | Giảm giá tính trên tạm tính; thuế tính trên phần sau giảm, không gồm phí vận chuyển. | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Tính tổng | FR-fleetio-parts-purchasing-fuel-009 | `Chạy` (D6) |
| BR-fleetio-parts-purchasing-fuel-021 | Nhận vượt không chặn, tồn tăng đủ số nhận. Trạng thái Full khi mọi dòng đạt số đặt. | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Nhận | FR-fleetio-parts-purchasing-fuel-012 | `Chạy` (D9, D10); điều kiện Full `Suy` |
| BR-fleetio-parts-purchasing-fuel-022 | Ô Receive bỏ dấu âm: gõ số âm thành nhận dương, không báo. | [Gói: Bảo dưỡng đội xe] | Nhận | FR-fleetio-parts-purchasing-fuel-012 | `Chạy` (D11) |
| BR-fleetio-parts-purchasing-fuel-023 | Make Adjustment chỉ có ở Full, Closed; số âm cắt về số đã nhận, không báo; giảm từ Full thì về Partial, giảm từ Closed thì vẫn Closed. | [Gói: Bảo dưỡng đội xe] | Trả hàng | FR-fleetio-parts-purchasing-fuel-028 | `Chạy` (D12, D18) |
| BR-fleetio-parts-purchasing-fuel-024 | Đóng được đơn khi nhận thiếu, không yêu cầu lý do. | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Close | FR-fleetio-parts-purchasing-fuel-029 | `Chạy` (D13) |
| BR-fleetio-parts-purchasing-fuel-025 | Không có huỷ đơn; thoát đơn chỉ có Close (từ Partial, Full) hoặc Delete; Closed không có nút mở lại. | [Gói: Bảo dưỡng đội xe] | Kết thúc đơn | FR-fleetio-parts-purchasing-fuel-029 | `Chạy` nút; Delete `Xem` |
| BR-fleetio-parts-purchasing-fuel-026 | Nhận vào lệnh luôn qua kho hai bước; huỷ form lệnh thì hàng ở lại kho, đơn vẫn đổi trạng thái. | [Gói: Bảo dưỡng đội xe] | Nhận vào lệnh | FR-fleetio-parts-purchasing-fuel-013 | `Chạy` (D14, D15) |
| BR-fleetio-parts-purchasing-fuel-027 | Người có quyền duyệt tự duyệt đơn của mình được. Tách người chưa kiểm được. | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Duyệt | FR-fleetio-parts-purchasing-fuel-010 | `Chạy` (D17) |
| BR-fleetio-parts-purchasing-fuel-028 | Phiếu Partial không có tiêu hao, số lít cộng vào phiếu đầy kế tiếp. | [Gói: Nhiên liệu] | Lưu phiếu | FR-fleetio-parts-purchasing-fuel-019 | `Chạy` (F3, F4) |
| BR-fleetio-parts-purchasing-fuel-029 | Reset usage ngắt chuỗi: phiếu đó không usage, phiếu sau hiện Usage "N/A" nhưng vẫn tính tiêu hao từ phiếu Reset. | [Gói: Nhiên liệu] | Lưu phiếu | FR-fleetio-parts-purchasing-fuel-019 | `Chạy` (F5, F6) |
| BR-fleetio-parts-purchasing-fuel-030 | Phiếu Personal và Void vẫn cộng vào chi phí xe và thẻ tổng Fuel History; Personal vẫn tính tiêu hao. | [Gói: Nhiên liệu] | Lưu phiếu | FR-fleetio-parts-purchasing-fuel-019 | `Chạy` (F7, F22, T6) |
| BR-fleetio-parts-purchasing-fuel-031 | Capacity Alert khi số lít lớn hơn dung tích đã khai, không cần tích hợp; không gỡ khi sửa phiếu. | [Gói: Giám sát nhiên liệu] | Lưu phiếu | FR-fleetio-parts-purchasing-fuel-022 | `Chạy` (F9, F9b, F13, F14, F1b) |
| BR-fleetio-parts-purchasing-fuel-032 | Số đồng hồ lùi cùng ngày không chặn; lùi ngày với số cao bị chặn, trừ khi Void; lùi ngày với số thấp lưu được, không đổi phiếu sau. | [Gói: Nhiên liệu] | Lưu phiếu | FR-fleetio-parts-purchasing-fuel-017 | `Chạy` (F8, F12, F12b) |
| BR-fleetio-parts-purchasing-fuel-033 | Phiếu Void vẫn bắt buộc số đồng hồ, không cập nhật đồng hồ xe, không có Usage. | [Gói: Nhiên liệu] | Void | FR-fleetio-parts-purchasing-fuel-033 | `Chạy` (F10) |
| BR-fleetio-parts-purchasing-fuel-034 | Phân loại nhà cung cấp quyết định nơi chọn được: Parts cho đơn mua, Fuel cho phiếu dầu. Bộ lọc Fuel History thì liệt kê mọi nhà cung cấp, kể cả không có Fuel. | [Cấu hình] | Chọn nhà cung cấp | FR-fleetio-parts-purchasing-fuel-015 | `Chạy` (D1, F-NCC, F16) |
| BR-fleetio-parts-purchasing-fuel-035 | Sửa tồn trong Bulk tự lưu, ghi Bulk Update, không hỏi lý do. | [Gói: Bảo dưỡng đội xe] | Sửa ô | FR-fleetio-parts-purchasing-fuel-025 | `Chạy` (K19) |
| BR-fleetio-parts-purchasing-fuel-036 | Điều chỉnh tồn ở hộp thường bắt buộc lý do. | [Gói: Bảo dưỡng đội xe] | Chỉnh tồn | FR-fleetio-parts-purchasing-fuel-005 | `Chạy` (K6) |
| BR-fleetio-parts-purchasing-fuel-037 | Nhãn tồn: từ 0 trở xuống là Out of Stock; trên 0 và từ điểm đặt lại trở xuống là Low Stock; còn lại không nhãn. Tồn 0 với điểm 0 thì Out of Stock thắng. | [Gói: Bảo dưỡng đội xe] | Mọi biến động | FR-fleetio-parts-purchasing-fuel-007 | `Chạy` (S1–S3, S5–S7) |
| BR-fleetio-parts-purchasing-fuel-038 | Dưới Static Pricing, giá trị tồn tính theo Unit Cost danh mục, không theo đơn giá đơn mua; không có giá thì tính 0. | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Tính giá trị tồn | FR-fleetio-parts-purchasing-fuel-008 | `Chạy` (K17, K18) |
| BR-fleetio-parts-purchasing-fuel-039 | Tên kho không trùng. | [Gói: Bảo dưỡng đội xe] | Tạo kho | FR-fleetio-parts-purchasing-fuel-002 | `Chạy` (K2) |
| BR-fleetio-parts-purchasing-fuel-040 | Chọn phụ tùng trên đơn: chưa bật tại kho của đơn thì xám, có khoá. | [Gói: Bảo dưỡng đội xe] | Thêm dòng | FR-fleetio-parts-purchasing-fuel-009 | `Chạy` (D2) |
| BR-fleetio-parts-purchasing-fuel-041 | Với đơn chưa Edit, Pending PO Qty tính từ Purchased; Draft và Approved không tính. Không áp cho đơn đã Edit và lưu, xem BR-fleetio-parts-purchasing-fuel-050. Lượt đầu ghi 12 ở Approved của PO #2; ảnh Record History cho thấy đơn đó có lần sửa tiền trước khi duyệt lại, nên có thể khớp quy tắc đã Edit (`Suy`, OQ-13). | [Gói: Bảo dưỡng đội xe] | Đổi trạng thái đơn | FR-fleetio-parts-purchasing-fuel-039 | `Chạy` (D22–D24), PO #4 |
| BR-fleetio-parts-purchasing-fuel-042 | Lùi từ Purchased về Approved rồi Draft không trừ Pending PO Qty; mua lại không nhân đôi. | [Gói: Bảo dưỡng đội xe] | Lùi trạng thái | FR-fleetio-parts-purchasing-fuel-039 | `Chạy` (D27–D29), PO #4; công thức `Suy` |
| BR-fleetio-parts-purchasing-fuel-043 | Make Adjustment từ Closed đổi số nhận và tồn, ghi sổ, đơn vẫn Closed, không hỏi lý do, không cần mở lại. | [Gói: Bảo dưỡng đội xe] | Điều chỉnh đơn đã đóng | FR-fleetio-parts-purchasing-fuel-028 | `Chạy` (D18) |
| BR-fleetio-parts-purchasing-fuel-044 | Sửa số đặt ở Purchased cập nhật Pending PO Qty ngay, không cảnh báo đơn đã gửi nhà cung cấp. | [Gói: Bảo dưỡng đội xe] | Sửa đơn | FR-fleetio-parts-purchasing-fuel-030 | `Chạy` (D25, D26) |
| BR-fleetio-parts-purchasing-fuel-045 | Make a Copy không chép số đã nhận; lưu ra Draft với số đơn mới. | [Gói: Bảo dưỡng đội xe] | Sao chép đơn | FR-fleetio-parts-purchasing-fuel-032 | `Chạy` (D21) |
| BR-fleetio-parts-purchasing-fuel-046 | Unmark as Purchased không xoá Purchase Date, Purchased By; PDF của đơn Approved vẫn in hai trường này. | [Gói: Bảo dưỡng đội xe] | Lùi trạng thái | FR-fleetio-parts-purchasing-fuel-031 | `Chạy` (D35) |
| BR-fleetio-parts-purchasing-fuel-047 | Chọn nhà cung cấp trên phiếu dầu tạo vị trí xe tại địa chỉ nhà cung cấp, form không báo. | [Gói: Nhiên liệu] | Lưu phiếu | FR-fleetio-parts-purchasing-fuel-042 | `Chạy` (F25) |
| BR-fleetio-parts-purchasing-fuel-048 | Bộ lọc Fuel History luôn có điều kiện Date khoá; số nhóm OR do Fleetio giới hạn (Fleetio: 3). | [Gói: Nhiên liệu] | Lọc | FR-fleetio-parts-purchasing-fuel-034 | `Chạy` (F15) |
| BR-fleetio-parts-purchasing-fuel-049 | Danh sách Parts tô đỏ Total Quantity khi một kho hết hàng, dù tổng các kho còn nhiều. | [Gói: Bảo dưỡng đội xe] | Mọi biến động | FR-fleetio-parts-purchasing-fuel-007 | `Chạy` (S9) |
| BR-fleetio-parts-purchasing-fuel-050 | Đơn Draft đã Edit và lưu thì số đặt vào Pending PO Qty của kho trên đơn, dù chưa duyệt; lưu lại thì theo số mới. | [Gói: Bảo dưỡng đội xe] | Lưu Draft đã sửa | FR-fleetio-parts-purchasing-fuel-039 | `Chạy` (D40, D41), PO #5; thao tác nào kích hoạt chưa tách riêng |
| BR-fleetio-parts-purchasing-fuel-051 | Sửa số đặt không tính lại trạng thái: đơn Full tăng số đặt vẫn "Received, Full", không có Receive. | [Gói: Bảo dưỡng đội xe] | Sửa đơn | FR-fleetio-parts-purchasing-fuel-030 | `Chạy` (D36, D37) |
| BR-fleetio-parts-purchasing-fuel-052 | Đổi kho, nhà cung cấp trên Draft giữ nguyên dòng hàng, không hỏi lại; xoá dòng không có hộp xác nhận. | [Gói: Bảo dưỡng đội xe] | Sửa Draft | FR-fleetio-parts-purchasing-fuel-030 | `Chạy` (D38) |
| BR-fleetio-parts-purchasing-fuel-053 | Báo cáo đơn mua cộng cả đơn Draft vào Total Amount. | [Gói: Bảo dưỡng đội xe] | Xem báo cáo | FR-fleetio-parts-purchasing-fuel-037 | `Chạy` (D42), theo nhật ký nhóm nền tảng |
| BR-fleetio-parts-purchasing-fuel-054 | Theo câu chữ màn: đổi phương pháp tính giá là vĩnh viễn, không đảo được, phải tích ô nhận thức rồi Activate. | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Đổi phương pháp | FR-fleetio-parts-purchasing-fuel-045 | `Xem` (K30, K37); chưa kiểm chứng bằng thao tác |
| BR-fleetio-parts-purchasing-fuel-055 | Theo câu chữ màn, điều kiện kích hoạt: mọi phụ tùng có Unit Cost từ mức tối thiểu trở lên, không số lẻ (Fleetio: ₫1); riêng FIFO, LIFO phải hoàn thành mọi lệnh dở có dòng phụ tùng, còn lệnh dở thì migration thất bại. | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Activate | FR-fleetio-parts-purchasing-fuel-045 | `Xem` (K35, K36) |
| BR-fleetio-parts-purchasing-fuel-056 | Theo câu chữ màn, hệ quả khi đổi: tồn hiện có nhận giá bằng Unit Cost danh mục ở mọi kho; tồn phụ tùng Archived về 0. Riêng FIFO, LIFO: dòng phụ tùng trên lệnh cũ không sửa được nữa; phụ tùng đã dùng trên lệnh không đổi được bật, tắt theo dõi tồn. Riêng Average: trả hàng về kho không tính lại giá trung bình theo đơn giá âm hoặc bằng 0 của lệnh cũ. | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Sau migration | FR-fleetio-parts-purchasing-fuel-045 | `Xem` (K32–K35); chưa đo |
| BR-fleetio-parts-purchasing-fuel-057 | Điều kiện lệnh dở của FIFO, LIFO chỉ tính lệnh chưa xong có dòng phụ tùng; lệnh không có dòng phụ tùng không tính. | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Activate | FR-fleetio-parts-purchasing-fuel-045 | `Chạy` (K39, K42) |

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
| E-fleetio-parts-purchasing-fuel-020 | Lệch tiền 100 lần ở báo cáo dầu | Fuel History, Total Fuel Cost, Cost per km, Avg. Cost nhỏ hơn đúng 100 lần, kể cả khi lọc (T9, T10) | critical | FR-fleetio-parts-purchasing-fuel-020 | Không báo | Chi tiết xe đúng, đối chiếu ở đó. Không nên học | `Chạy`; Avg. Cost đúng là `Suy` |
| E-fleetio-parts-purchasing-fuel-021 | Nhà cung cấp thiếu trường | "can't be blank" | minor | FR-fleetio-parts-purchasing-fuel-015 | Form | Nhập đủ | `Chạy` |
| E-fleetio-parts-purchasing-fuel-022 | Enter lưu form sớm | Enter trong ô Country vừa chọn vừa lưu | major | FR-fleetio-parts-purchasing-fuel-015 | Bản ghi tạo sớm | Sửa bản ghi. Không nên học | `Chạy`, ba lần |
| E-fleetio-parts-purchasing-fuel-023 | Thêm xe khi hết hạn mức | Save Vehicle quay mãi, không báo lỗi, thanh "5 of 5" | major | Ngoài nhóm này | Form xe | Giới hạn là `Suy` | `Chạy` |
| E-fleetio-parts-purchasing-fuel-024 | Mất giá lúc tạo phụ tùng | Giá gõ lúc tạo không được lưu, chưa rõ vì sao | major | FR-fleetio-parts-purchasing-fuel-001 | Giá trị tồn 0 | Sửa phụ tùng | `Chạy` |
| E-fleetio-parts-purchasing-fuel-025 | Đơn Closed vẫn sửa được giá | "was successfully updated" trên đơn đã đóng | major | FR-fleetio-parts-purchasing-fuel-030 | Tổng đổi | Không nên học | `Chạy` |
| E-fleetio-parts-purchasing-fuel-026 | Số đang về thừa sau khi lùi đơn | Không báo; đơn về Approved, Draft mà Pending PO Qty vẫn 15 và 5 sau khi tải lại | major | FR-fleetio-parts-purchasing-fuel-039 | Thẻ tồn | Chưa thấy cách trừ; dễ đặt hàng sai. Không nên học | `Chạy`, chỉ đo trên PO #4 |
| E-fleetio-parts-purchasing-fuel-027 | Đơn Closed vẫn đổi số nhận, tồn | "Purchase Order #2 was successfully adjusted"; đơn không mở lại, không hỏi lý do | major | FR-fleetio-parts-purchasing-fuel-028 | Đơn vẫn Closed | Đọc sổ kho. Không nên học | `Chạy` |
| E-fleetio-parts-purchasing-fuel-028 | Phiếu Void vẫn cộng vào tổng | Không báo; Total Volume, Total Fuel Cost tính cả phiếu Void | major | FR-fleetio-parts-purchasing-fuel-033 | Thẻ tổng Fuel History | Lọc theo Void Status (chưa thử). Không nên học | `Chạy` |
| E-fleetio-parts-purchasing-fuel-029 | Print Worksheet tải nhiều file | Một cú bấm tải 3 PDF giống hệt; toast "Complete: Bulk Manage Parts Worksheet" | minor | FR-fleetio-parts-purchasing-fuel-041 | Không mở tab | Xoá bản thừa. Không nên học | `Chạy` |
| E-fleetio-parts-purchasing-fuel-030 | Định dạng tiền không thống nhất | PDF đơn và Record History hiện kiểu US, web hiện kiểu Việt Nam | minor | FR-fleetio-parts-purchasing-fuel-037 | Không báo | Không nên học | `Chạy`; Record History `Xem` ảnh |
| E-fleetio-parts-purchasing-fuel-031 | Tô đỏ tổng khi một kho hết | Total Quantity 121 tô đỏ vì một kho về 0 | minor | FR-fleetio-parts-purchasing-fuel-007 | Danh sách Parts | Mở từng kho để biết kho nào. Không nên học | `Chạy` |
| E-fleetio-parts-purchasing-fuel-032 | Đơn nháp vào số đang về | Không báo; PO #5 Draft đã Edit làm Pending KHO-02 từ 0 thành 15, rồi 7 | major | FR-fleetio-parts-purchasing-fuel-039 | Thẻ tồn | Chưa thấy cách loại trừ; hàng ảo dẫn tới đặt thiếu. Không nên học | `Chạy`, PO #5 |
| E-fleetio-parts-purchasing-fuel-033 | Đơn báo đủ hàng khi đang thiếu | Không báo; đặt 15, nhận 12 vẫn "Received, Full", không có Receive | major | FR-fleetio-parts-purchasing-fuel-030 | Trạng thái đơn, menu | Chưa thử đường nhận 3 còn lại. Không nên học | `Chạy`, PO #3 |
| E-fleetio-parts-purchasing-fuel-034 | Báo cáo đơn cộng cả Draft | Không báo; Total Amount ₫3,574,040 gồm đơn Draft #5 ₫574,040 | major | FR-fleetio-parts-purchasing-fuel-037 | Báo cáo purchase_orders | Lọc trừ Draft, chưa thử. Không nên học | `Chạy` |
| E-fleetio-parts-purchasing-fuel-035 | Chưa đủ điều kiện đổi phương pháp giá | Hộp nêu "2 part(s)" chưa có Unit Cost, "3 Work Order(s)" dở; "An incomplete Work Order at the time of migration will cause the migration to fail." | major | FR-fleetio-parts-purchasing-fuel-045 | Activate xám | Sửa phụ tùng hoặc Parts Import; hoàn thành lệnh | `Xem` câu chữ; thất bại chưa gặp |
| E-fleetio-parts-purchasing-fuel-036 | Lệnh không hoàn thành được vì dòng công | "Please edit and fix the following errors: Started At can't be blank", "Work Order Labor Line Items is invalid" khi đổi #103 sang Completed | major | FR-fleetio-parts-purchasing-fuel-045 | Chặn đổi trạng thái; bút chì dòng công xám | Còn nút "Remove labor line item", chưa bấm. Một dòng công chặn đổi phương pháp giá cả tài khoản. Không nên học | `Chạy`; nguyên nhân do contact Sample `Suy` |

## 6A. Ma trận case

Tiền ghi nguyên giá trị đã thử trên tài khoản VND. Điều không xảy ra cũng ghi là kết quả.

### Tồn và kho

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| S1 Không nhãn | Tồn 6 và 6,5, điểm đặt lại 5 | Không nhãn, đủ nút | `Chạy` |
| S2 Low Stock | Tồn 3, và đúng bằng 5, điểm đặt lại 5 | Nhãn "Low Stock", số màu cam, đủ nút | `Chạy` |
| S3 Out of Stock | Tồn 0 và -10 | Nhãn "Out of Stock", nút chuyển kho khoá | `Chạy` |
| S4 Điểm đặt lại 0 | Lưu điểm 0, tồn 9,5 | Lưu được dù tài liệu nói phải lớn hơn 0, "Part was successfully updated", không nhãn. Tồn về 0 với điểm 0 xem S5 | `Chạy` |
| S5 Tồn 0, điểm đặt lại 0 | PT-A kho KHO-02, sửa ở Bulk 9,5 thành 0 | Nhãn "Out of Stock"; ô đếm danh sách Out of Stock 1, Low Stock 0: Out of Stock thắng | `Chạy` |
| S6 Tồn 0,5, điểm đặt lại 0 | Sửa ở Bulk | Không nhãn | `Chạy` |
| S7 Tồn 9,5, điểm đặt lại 0 | Trả về 9,5 ở Bulk | Không nhãn | `Chạy` |
| S8 Sổ kho khi sửa ở Bulk | 9,5 thành 0 | Ghi "Adjustment: 9.5 → 0.0", chứng từ Bulk Update, không hỏi lý do | `Chạy` |
| S9 Một kho hết, tổng còn nhiều | Total Quantity PT-A 121 | Danh sách Parts vẫn tô đỏ số 121 | `Chạy` |
| S10 Email cảnh báo tồn thấp | Tồn xuống ngưỡng | Không gửi, không chạy theo ràng buộc không gửi email; giữ `Docs` | Không chạy |
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
| K23 Thay thế, tương thích xe | Form phụ tùng | Không thấy trường nào; chỉ có Replaced Parts trong bảo hành ở lệnh. Lượt 3 rà tiếp, xem K24–K26 | `Xem` |
| K24 Form New Part | Mở form, không lưu | Part Number, Description, Photo, Document, Category, Manufacturer, Manufacturer Part #, UPC, Unit Cost, Measurement Unit, Warranty, Locations, Purchase History. Không có trường thay thế, tương thích xe | `Chạy` phần form |
| K25 Danh sách Parts | Đọc cột | Có cột "Linked Service Tasks": nơi duy nhất nối phụ tùng với việc khác. Trang này chưa rà | `Xem` |
| K26 Menu trang phụ tùng | Mở menu PT-A | "Update Quantity", "Archive" (mờ với PT-A), "View Record History". Không có mục thay thế, tương thích. Vì sao Archive mờ chưa rõ | `Xem` |
| K27 Print Worksheet | Bulk Manage Parts, một cú bấm | Toast "Complete: Bulk Manage Parts Worksheet", "Click here if download doesn't start". Không mở tab, tự tải PDF, ra 3 bản giống hệt | `Chạy` |
| K28 Nội dung Worksheet | PDF 39 KB, 1 trang, in theo kho đang chọn | Tên, địa chỉ tài khoản; Part, Category, Manufacturer, Aisle, Row, Bin, Current Qty kèm mốc "Yesterday", "Today", ô trống New Qty. Không lưu ảnh vì có địa chỉ tài khoản | `Chạy` |
| K29 FIFO, LIFO, Average | Đổi cài đặt cấp tài khoản | Lượt 3, 4 bị cấm. Lượt 5 được phép đổi nhưng dừng trước Activate vì hộp ghi không đảo được, xem K30–K37; chưa đo giá xuất kho; OQ-11 còn mở | Không chạy |
| K30 Cách đổi phương pháp | Settings, Inventory Valuation Method, đang Static Pricing | 4 radio, không có nút Save. Chọn radio khác mới hiện khối cảnh báo, ô tích "I am aware the change I am about to make is permanent and can not be reversed", nút "Activate" xám | `Xem`, settings-valuation-fifo-permanent-warning |
| K31 Mô tả phương pháp | Đọc radio | Average: "When adding a Part to a Work Order, Fleetio will use the current average unit cost for the selected inventory location." FIFO: "The price applied to the work order will be the price from the earliest quantity until depleted." LIFO: "...from the latest quantity until depleted." FIFO, LIFO giữ "dated inventory record" ở từng kho. Static: Unit Cost đặt tay, không tự đổi theo điều chỉnh tồn hay đơn mua | `Xem` |
| K32 Cảnh báo chung | Chọn Average, FIFO, LIFO | "Archived part quantities will be reset to 0" | `Xem`, chưa đo |
| K33 Cảnh báo riêng Average | Chọn Average | "For Part Line Items with negative or $0.00 unit costs on Work Orders created before this migration: if the Parts are returned to inventory after migration, Fleetio will not recalculate your Average Unit Cost using negative or $0.00 unit costs. Consider updating to a positive value." | `Xem`, chưa đo |
| K34 Cảnh báo riêng FIFO, LIFO | Chọn FIFO, LIFO | "Any parts with inventory tracking disabled at a location and have ever been used on a Work Order cannot be enabled for tracking after this migration"; "Any parts with inventory tracking enabled at a location and have ever been used on a Work Order cannot be disabled for tracking after this migration"; "Part line items on Work Orders created before this migration will be permanently uneditable after this migration" | `Xem`, chưa đo |
| K35 Điều kiện Unit Cost | Mọi phương pháp | "All parts must have a unit cost of ₫1 or greater (limited to 0 decimal places). We will use the Unit Cost value stored on the primary Part record as the effective price for each individual unit of current inventory of that Part, across all Part Locations." Tài khoản hiện "2 part(s)" chưa có Unit Cost; có link "Download the CSV", "Parts Import" | `Xem` |
| K36 Điều kiện lệnh dở | FIFO, LIFO | "For LIFO/FIFO, all incomplete Work Orders with part line items must be completed. An incomplete Work Order at the time of migration will cause the migration to fail." Tài khoản hiện "3 Work Order(s)" dở, có link danh sách | `Xem` |
| K37 Dừng trước Activate | Chọn lần lượt 3 radio, không tích ô, không bấm | Chọn radio không lưu gì; tải lại trang vẫn Static Pricing, ô tích trống. Không có lịch sử migration hay bản xem thử giá trị tồn. "Không đảo được" chỉ theo câu chữ, chưa kiểm chứng | `Chạy` phần chọn radio và tải lại |
| K38 Link "2 part(s)" | Lượt 6, lọc thiếu giá và có theo dõi tồn | TEST-KHO-PT-B (tồn 8), TEST-NHAC-PT (tồn 7). Làm được, chưa điền giá | `Chạy` đọc |
| K39 Link "3 Work Order(s)" | Lọc chưa xong và có dòng phụ tùng | #100, #102, #103, đều lệnh TEST. #100, #102 chưa thử, chưa đụng | `Chạy` đọc |
| K40 Hoàn thành Lệnh #103 | Đổi sang Completed | "Please edit and fix the following errors: Started At can't be blank", "Work Order Labor Line Items is invalid". Dòng công dùng contact Sample; nguyên nhân do contact này là suy ra | `Chạy`, nguyên nhân `Suy` |
| K41 Sửa dòng công #103 | Form Edit | Nút bút chì dòng công xám. Còn nút "Remove labor line item", chưa bấm vì brief cấm xoá; đã Cancel, không lưu gì | `Chạy` |
| K42 Lệnh không có dòng phụ tùng | #111, trước và sau khi đóng | Số trên link vẫn 3: lệnh này không tính vào điều kiện | `Chạy` |
| K43 Đổi sang FIFO | User duyệt đổi một chiều | Bị chặn ở #103, dừng trước Activate: không tích ô, không bấm. Tải lại vẫn Static Pricing. Chưa đo giá xuất, trả về kho, sửa dòng lệnh cũ, bật tắt theo dõi tồn, giá trị tồn sau đổi, báo cáo | Không chạy |
| K44 Giá chụp trước khi đổi | Static, danh sách phụ tùng TEST | BRAKE-PAD-01 tồn 3, 300.000 ₫; PT-A 130,5, 100.000 ₫; PT-B 8, trống; LOP-MODEL-01 không theo dõi, 3.000.000 ₫; NHAC-PT 7, trống. Mốc để so nếu đổi sau này | `Chạy` đọc |

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
| D18 Make Adjustment từ Closed | PO #2 Closed, tick PT-A, nhập -1 | "Purchase Order #2 was successfully adjusted". Qty Received 110 xuống 109; đơn vẫn Closed, khác từ Full về Partial. Sổ "Received: -1.0", chứng từ PO #2; tồn KHO-01 còn 121. Không mở lại đơn, không hỏi lý do | `Chạy`, po-adjust-closed |
| D19 Lịch sử bản ghi đơn | PO #2, "View Record History" | Hộp "Record History", ô "Select Date Range", cột Date, Changes By, Changes Made. Ghi "State changed from Received Partial to Closed", "Received Full to Received Partial", "Approved to Draft"; ghi đổi Tax 1, Discount, Subtotal, Total Amount | `Chạy`, po-record-history |
| D20 Record History có ghi số nhận không | Phần đọc được trong ảnh: 7 dòng trạng thái, 2 nhóm đổi tiền | Không thấy dòng nào về số nhận; lần nhận, lần điều chỉnh chỉ hiện qua dòng trạng thái. Hộp còn thanh cuộn, phần dưới không đọc được, ảnh không rõ chụp trước hay sau D18 | `Xem` ảnh, OQ-22 |
| D21 Make a Copy từ Closed | PO #2, "Make a Copy", "Save as Draft" | Form "New Purchase Order" số 4, chép nhà cung cấp, kho, 2 dòng, số đặt 12 và 5, giá, chiết khấu. Không chép số đã nhận. "Purchase Order was successfully created", PO #4 Draft | `Chạy` |
| D22 Pending khi Draft, chưa Edit | PO #4 mới tạo từ Copy, đặt 12 | Pending PO Qty 0, Current Qty 121. Draft đã Edit xem D40, D41 | `Chạy` |
| D23 Pending khi Approved, chưa Edit | PO #4 đặt 12 | Pending PO Qty 0, Current Qty 121. Lượt đầu ghi 12 ở Approved của PO #2; Approved đã Edit chưa đo riêng (OQ-13) | `Chạy` |
| D24 Pending khi Purchased | PO #4 đặt 12 | Pending PO Qty 12, Current Qty 121 | `Chạy` |
| D25 Pending khi sửa số đặt | PO #4 Purchased, 12 thành 15 | Pending PO Qty 15, Current Qty 121 | `Chạy` |
| D26 Sửa đơn ở Purchased | PO #4, Edit, "Save Purchase Order" | Vendor, Part Location khoá xám; không có Add Line Item, nút xoá dòng; sửa được Label, số, giá, Description, Discount, Shipping, Tax. Lưu được, không cảnh báo đã gửi nhà cung cấp | `Chạy`, po-edit-purchased |
| D27 Unmark as Purchased | PO #4, menu | "Purchase Order #4 unmarked as purchased", về Approved. Pending PT-A vẫn 15, PT-B vẫn 5 sau khi tải lại trang | `Chạy` |
| D28 Lùi tiếp về Draft | Edit ở Approved, "Save as Draft" | "Purchase Order was successfully updated", về Draft, mất dòng Approved By. Pending vẫn 15 | `Chạy` |
| D29 Mua lại | Approve, "Mark as Purchased" | Pending vẫn 15, không nhân đôi. Số đã vào Pending không bị trừ khi lùi là suy ra, chỉ đo ở PO #4. Cuối cùng PO #4 Purchased, đặt 15 và 5, chưa nhận | `Chạy`, công thức `Suy` |
| D30 Form sửa ở Draft | Xem, không lưu | Vendor, Part Location mở; có "Add Line Item", nút xoá dòng, "Save as Draft", "Save & Approve" | `Xem` form |
| D31 Form sửa ở Received, Full | PO #3, xem, không lưu | Vendor, Part Location khoá; không thêm bớt dòng; ô số, giá mở; nút "Save Purchase Order" | `Xem` form |
| D32 Pending Approval, Rejected | Cần người thứ hai không có quyền duyệt | Không chạy được vì cấm mời người ngoài; giữ OQ-8, OQ-20 | Không chạy |
| D33 Menu theo trạng thái | Approved; Purchased | Approved: "Mark as Purchased", "Print", "Make a Copy", "View Record History", "Delete"; không có mục lùi về Draft, phải vào Edit. Purchased: "Receive", "Unmark as Purchased", "Print", "Make a Copy", "View Record History", "Delete" | `Chạy` |
| D34 In đơn | PO #4 Approved, "Print" | Tab mới "Preparing your PDF...", ra `purchase_order_4.pdf` 1 trang: Number, Status, Vendor, Part Location, Created Date, Created By, Approval Date, Approved By, Purchase Date, Purchased By, Closed Date, Closed By; dòng hàng; Subtotal, Discount, Shipping, Tax, Total; Description. Đầu trang in tên, địa chỉ tài khoản | `Chạy`, po-print-pdf |
| D35 PDF sau khi Unmark | PO #4 Approved sau Unmark | Vẫn in Purchase Date, Purchased By: dữ liệu không bị xoá khi lùi | `Chạy`, po-print-pdf |
| D36 Sửa đơn Full có lưu | PO #3 đặt 12, nhận 12; PT-A 12 thành 15, 90.000 thành 95.000 | "Purchase Order was successfully updated". Đặt 15, nhận 12, vẫn "Received, Full"; Total 1.069.760 thành 1.405.100 ₫. Đã trả về số cũ sau khi đo | `Chạy` |
| D37 Sau khi tăng số đặt ở Full | Còn thiếu 3 | Menu vẫn "Close", "Make Adjustment", "Print", "Make a Copy", "View Record History", "Delete"; không có "Receive". Thẻ PT-A giữ Current Qty 121, Pending 15, Unit Cost 100.000: không cộng Pending, không đổi giá danh mục | `Chạy` |
| D38 Sửa đơn Draft có lưu | PO #5: đổi kho, xoá dòng PT-B, đổi nhà cung cấp, "Save as Draft" | "Purchase Order was successfully updated". Đổi kho, nhà cung cấp không xoá dòng, không hỏi lại; xoá dòng không có hộp xác nhận | `Chạy` |
| D39 Copy đơn đã sửa | PO #3 sau khi sửa, "Make a Copy" | Lấy số đặt, giá đã sửa (15; 95.000), không lấy số nhận | `Chạy` |
| D40 Pending khi Draft đã Edit | PO #5 chưa từng Approve, kho KHO-02, số 15, tải lại trang | Pending KHO-02 từ 0 thành 15; KHO-01 giữ 15 của PO #4. Sửa kết luận "chỉ tính từ Purchased" của lượt 3 | `Chạy` |
| D41 Sửa số trên Draft | PO #5, số 7, "Save as Draft" | Pending KHO-02 thành 7, theo số mới, không cộng dồn. Lần sửa cuối về 6 chưa đọc lại thẻ | `Chạy` |
| D42 Báo cáo đơn mua | Báo cáo purchase_orders, lọc Vendor TEST-NCC-01 | 2 dòng #1, #5; Total Amount ₫3,574,040 gồm cả đơn Draft #5 ₫574,040. Biểu đồ "Total by Vendor" trục chỉ tới 20k trong khi tổng 3,5 triệu | `Chạy`, theo nhật ký nhóm nền tảng |
| D43 Vẫn không chạy được ở lượt 4 | Pending Approval, Rejected; FIFO, LIFO, Average; email tồn thấp; Invite | Cần người thứ hai, đổi cài đặt, gửi email, mời người ngoài. Automation có Update Status "Approved", "Rejected" nhưng hãng bắt điều kiện Pending Approval | Không chạy |

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
| F-Lọc Bộ lọc | Date, Vehicle, Vehicle Group, Vendor, Filters | Mở bộ lọc theo xe, có Add Filter, Add Filter Group. Lượt 3 thử thêm, xem F15–F21 | `Chạy` |
| F-Thẻ Thẻ dầu | Fuel Card trên phiếu | Ô "No"; cài đặt WEX chỉ đọc; không có màn gán thẻ thử được. Không tích hợp | `Xem` |
| F-VLA Vendor Location Alert | Cần định vị và thẻ | Cần tích hợp nên chưa thử | Không chạy |
| F-Sạc Charging History | — | Ngoài phạm vi theo yêu cầu user, không xem | Không chạy |
| F15 Date mặc định | Mở panel Filters | 30 ngày gần nhất, là điều kiện có biểu tượng khoá. Panel: "You can create up to 3 "OR" filter types. To add more filters, use "AND" within the filter builder." | `Chạy`, fuel-filter-alert-type |
| F16 Lọc Vendor | Chọn nhiều | Liệt kê mọi nhà cung cấp, kể cả không có Fuel, khác form phiếu. Lọc NCC-DAU: 1 phiếu, thẻ tổng tính lại | `Chạy` |
| F17 Trường lọc | Add Filter | Date, Fuel Alert Type, Fuel Transaction, Fuel Type, Partial, Personal, Reference, Reset, Transaction Card Number, Transaction Driver ID, Transaction Driver Name, Transaction Vehicle ID, Vendor, Void Status; 24 trường Vehicle; 6 trường Vendor | `Chạy` |
| F18 Fuel Alert Type | Mở ô chọn | Đúng 3 giá trị: "Vendor Location Alert", "Fuel Capacity Alert", "Missing GPS Location Alert" | `Chạy`, fuel-filter-alert-type |
| F19 Lọc Fuel Capacity Alert | Date 30 ngày và Fuel Alert Type | 2 phiếu 60,5 lít và 50 lít; phiếu 50 lít là phiếu sửa từ 100, xác nhận F9b | `Chạy`, fuel-filter-alert-type |
| F20 Lọc Personal | Thêm điều kiện | Đúng 1 phiếu 10 lít | `Chạy` |
| F21 Áp bộ lọc | Thêm, xoá điều kiện | Xoá một điều kiện thì danh sách áp ngay; thêm điều kiện phải bấm Apply | `Chạy` |
| F22 Void, Personal trong thẻ tổng | Lọc xe KHO-01, cộng tay 14 phiếu | Tổng tay 400,5 lít bằng 105,80 gallons, khớp Total Volume. Phiếu Void 20 lít vẫn cộng vào Total Volume, Total Fuel Cost; bỏ Void chỉ còn 100,5 gallons. Personal cũng cộng. Void không loại khỏi thống kê | `Chạy` |
| F23 Cảnh báo sai vị trí | Cần tích hợp thẻ, định vị | Không chạy được, chỉ thấy tên loại ở bộ lọc; giữ OQ-14 | Không chạy |
| F24 Thẻ dầu trên phiếu | Không kết nối WEX | Không có màn gán thẻ nếu không tích hợp. Bộ lọc có Transaction Card Number, Transaction Driver ID, Transaction Driver Name, Transaction Vehicle ID: dữ liệu thẻ gắn ở mức phiếu | `Xem` |
| F25 Phiếu dầu tạo vị trí xe | TEST-DAUKEO-2 chưa có vị trí, phiếu 100 km, 5 lít, 20.000 ₫, chọn NCC-02 | Location History có 1 dòng "Fuel Entry"; xe hiện trên Fleet Map; form không báo. Chi tiết ở nhóm Vị trí, FR-fleetio-location-dispatch-004 | `Chạy` |

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
| T9 Thẻ tổng, 14 phiếu | Cộng tay 8.010.000 ₫ | Hiện 80.100 ₫, lặp lại lỗi T3 | `Chạy` |
| T10 Thẻ tổng khi lọc | 2 phiếu 1.210.000 ₫ và 1.000.000 ₫, tổng 2.210.000 ₫ | Total Fuel Cost hiện 22.100 ₫; Avg. Cost 757 ₫/gallon, đúng khoảng 75.700 khi lấy 2.210.000 chia 29,19 gallons | `Xem` ảnh fuel-filter-alert-type; giá trị đúng `Suy` |
| T11 Tiền trên PDF đơn | PO #4 | Total ₫1,575,200 kiểu US, web hiện 1.575.200 ₫; số đúng, chỉ khác định dạng. Thuế 8% trên phần sau giảm khớp D6 | `Chạy`, po-print-pdf |
| T12 Tiền trong Record History | PO #2 | Hiện kiểu US, ví dụ Total Amount ₫1,429,400 thành ₫1,312,760 | `Xem` ảnh po-record-history |

### Nhà cung cấp

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| N1 Trường bắt buộc | Trống Tên, Address, City, State, Zip, Country | "can't be blank" | `Chạy` |
| N2 Phân loại | Không chọn | Không bắt buộc, nhưng quyết định nơi được chọn | `Chạy` |
| N3 Tab theo phân loại | NCC-DAU chỉ Fuel; NCC-02 cả hai; NCC-01 Parts | NCC-DAU không có tab Purchase Orders; NCC-02 có Fuel Entries và Purchase Orders; tab đơn của NCC-01 liệt kê #3 và #2 | `Chạy` |
| N4 Network Status | "Network Status: Invite" | Không bấm | `Xem` |
| N5 Find Shops | Nút Add Vendors | Lượt đầu thấy, không mở; lượt 3 đã mở, xem N7, N8 | `Xem` |
| N6 Enter trong ô Country | Chọn quốc gia bằng Enter | Vừa chọn vừa lưu form, ba lần đều vậy; dễ tạo bản ghi sớm | `Chạy` |
| N7 Mở Find Shops | Gõ một thành phố công khai, "Let's Go" | Hộp "Select service shops and easily save them to your vendors list", ô "Enter address, city or ZIP/postal code", ô "Shop type". Khoảng 30 cửa hàng thật kèm bản đồ, chữ "All Results". Không lưu ảnh vì có địa chỉ thật | `Chạy` |
| N8 Tick một cửa hàng | Không bấm Add Vendor | Hiện "SELECTED", "Clear selection", ghim đổi đỏ, nhãn khoảng cách, nút "Add Vendor". Không thêm vì sẽ tạo bản ghi trùng tên doanh nghiệp thật, đã huỷ | `Chạy` đến bước tick |
| N9 Danh sách, trang chi tiết | Đọc giao diện | Danh sách có cột Rating, Labels, Archived At; tab Charging, Fuel, Parts, Service, Vehicle, Archived. Trang chi tiết có thêm "Tools Vendor". Lưu trữ, khôi phục chưa thử. Charging ngoài phạm vi theo yêu cầu user | `Xem` |
| N10 Rating | Mọi nhà cung cấp TEST | Cột hiện "...", rê chuột "Rating not available". Phần đọc được của form Edit Vendor không có chỗ nhập điểm, suy ra không do người dùng nhập, nguồn chưa rõ | `Chạy`, nguồn `Suy` |
| N11 Network Status | "Network Status: Invite" | Không bấm vì mời người ngoài; giữ một nửa OQ-15 | Không chạy |
| N12 Trường lọc Vendor | Vendors, Filters, Add Filter | "Archived", "Archived at", "Classification", "Contact Email", "Contact Name", "Contact Phone", "Labels", "Minority Owned (MBE)", "Network Status", "Phone", "Preferred", "Rating", "State/Province/Region", "Watcher", "Website", "Women Owned (MBE)" | `Chạy` |
| N13 Lọc Rating | Chọn Rating, không Apply | "Vendor Rating", "is equal to", ô "Search number": điểm là số | `Chạy` |
| N14 Rating trên danh sách | 20 nhà cung cấp, cả Sample lẫn TEST | Đều hiện "..." và "Rating not available" | `Chạy` |
| N15 Rating ở Find Shops | Thẻ cửa hàng, bóng ghim | Chỉ có tên, địa chỉ hoặc loại, khoảng cách, dấu xanh; không có điểm. Nguồn điểm vẫn chưa rõ; có thể cần Shop Network là suy đoán, Enable Shop Network là đổi cài đặt nên không thử | `Chạy`, nguồn `Suy` |

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
* [ ] OQ-8: Pending Approval, Rejected chạy thế nào, đơn Rejected có gửi lại được không? Cần tài khoản có người không có quyền duyệt. Lượt 3 vẫn không chạy được vì cấm mời người ngoài (D32) — Nguồn khách: không áp dụng
* [ ] OQ-9: Xoá cả lệnh có hoàn kho không? Đã huỷ ở hộp xác nhận (K21) — Nguồn khách: không áp dụng
* [ ] OQ-10: Delete đơn mua ảnh hưởng gì đến tồn và sổ kho? Chưa bấm — Nguồn khách: không áp dụng
* [ ] OQ-11: Dưới FIFO, LIFO, Average: giá trị tồn, sửa giá sau khi nhận, nhận vào lệnh chạy thế nào? Một phần lượt 5, từ câu chữ màn, chưa đo (`Xem`, K32–K35): tồn đầu lấy Unit Cost danh mục; FIFO, LIFO khoá sửa dòng phụ tùng lệnh cũ. Lượt 6 chỉ biết thêm điều kiện cụ thể, FIFO chưa đổi, chưa đo: bị chặn ở Lệnh #103 "Work Order Labor Line Items is invalid" (K38–K43). Giá xuất, giá trị tồn sau khi nhận, sửa giá sau khi nhận, nhận vào lệnh vẫn mở — Nguồn khách: không áp dụng
* [ ] OQ-12: Đổi vị trí dòng lệnh sang None thì sổ kho ghi gì? Chưa thử — Nguồn khách: không áp dụng
* [ ] OQ-13: Đơn Draft có tính vào Pending PO Qty không? Một phần lượt 4, mở lại vì lượt 3 kết luận quá rộng: Draft chưa Edit không tính (PO #4); Draft đã Edit và lưu thì tính, theo số mới (PO #5, D40, D41, `Chạy`). Còn chưa rõ: thao tác nào kích hoạt, vì lần lưu của PO #5 gộp đổi kho, nhà cung cấp, xoá dòng; Approved đã Edit chưa đo; Edit ở Full lại không cộng Pending (D37) — Nguồn khách: không áp dụng
* [ ] OQ-14: Vendor Location Alert kích hoạt thế nào khi có định vị và thẻ? Cần tích hợp, lượt 3 vẫn không chạy được, chỉ thấy tên loại ở bộ lọc (F23) — Nguồn khách: không áp dụng
* [ ] OQ-15: Find Shops, Network Status: Invite làm gì? Một phần lượt 3: Find Shops tìm cửa hàng kèm bản đồ, tick được, Add Vendor không bấm (N7, N8, `Chạy`); Invite không bấm vì mời người ngoài, phần này còn mở (N11) — Nguồn khách: không áp dụng
* [ ] OQ-16: Vì sao giá gõ lúc tạo phụ tùng PT-B không được lưu? (K18) — Nguồn khách: không áp dụng
* [x] OQ-17: Tồn về 0 khi điểm đặt lại bằng 0 thì nhãn gì? Chưa thử (S4) Trả lời lượt 3: Out of Stock thắng, Low Stock không hiện (`Chạy`) — Nguồn khách: không áp dụng
* [ ] OQ-18: Mốc 1.000 trong câu "must be less than 1,000 or marked as void" lấy từ đâu? (F12) — Nguồn khách: không áp dụng
* [ ] OQ-19: Thay thế, tương thích xe có ở nơi khác ngoài form phụ tùng không? (K23) Một phần lượt 3: không có trong form, danh sách, menu phụ tùng; chưa rà trang Linked Service Tasks (`Chạy`) — Nguồn khách: không áp dụng
* [ ] OQ-20: Có tách được người lập và người duyệt không? Không kiểm được với tài khoản một người (D17, D32) — Nguồn khách: không áp dụng
* [ ] OQ-21: Khi nhận vượt, trả quá số, đóng thiếu, Delta muốn chặn, cảnh báo hay chỉ ghi nhận? — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-22: Record History có ghi đổi số nhận không? Phần đọc được trong ảnh chỉ có trạng thái và tiền (D20) — Nguồn khách: không áp dụng
* [ ] OQ-23: Vì sao Archive mờ với PT-A, điều kiện lưu trữ phụ tùng là gì? (K26) — Nguồn khách: không áp dụng
* [ ] OQ-24: Điểm Rating của nhà cung cấp đến từ đâu? Lượt 4: điểm là số, chưa thấy nơi nhập hay sinh điểm; Shop Network là suy đoán (N10, N13–N15) — Nguồn khách: không áp dụng
* [ ] OQ-25: Pending PO Qty sau khi lùi trạng thái tính theo công thức nào, có đúng với đơn khác PO #4 không? (D27–D29) — Nguồn khách: không áp dụng
* [ ] OQ-26: "Missing GPS Location Alert" kích hoạt khi nào? Chỉ thấy tên ở bộ lọc (F18) — Nguồn khách: không áp dụng
* [ ] OQ-27: Delta có cần sửa số nhận sau khi đóng đơn không, nếu có thì phải mở lại hay lập phiếu điều chỉnh? Fleetio: sửa thẳng, không lý do (D18) — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-28: Dòng công dùng contact Sample có đúng là nguyên nhân "Work Order Labor Line Items is invalid" không? Chưa tách riêng (K40) — Nguồn khách: không áp dụng

## Phát hiện lượt 3 (03/11)

Nguồn: `run-notes/parts-purchasing-fuel.md`, mục Lượt 3.

- Pending PO Qty không giảm khi lùi Purchased về Approved rồi Draft; duyệt và mua lại không nhân đôi. Chỉ đo trên PO #4. Xem FR-fleetio-parts-purchasing-fuel-039, BR-fleetio-parts-purchasing-fuel-041, BR-fleetio-parts-purchasing-fuel-042, E-fleetio-parts-purchasing-fuel-026, D22–D29.
- Make Adjustment từ Closed đổi số nhận và tồn, đơn vẫn Closed. Xem FR-fleetio-parts-purchasing-fuel-028, BR-fleetio-parts-purchasing-fuel-043, E-fleetio-parts-purchasing-fuel-027, D18.
- Phiếu dầu Void vẫn cộng vào Total Volume, Total Fuel Cost. Thẻ tổng lệch 100 lần: 80.100 ₫ so với 8.010.000 ₫. Xem FR-fleetio-parts-purchasing-fuel-033, BR-fleetio-parts-purchasing-fuel-030, E-fleetio-parts-purchasing-fuel-020, E-fleetio-parts-purchasing-fuel-028, F22, T9, T10.
- Fuel Alert Type có 3 giá trị, có "Missing GPS Location Alert". Xem FR-fleetio-parts-purchasing-fuel-043, F18, OQ-26.
- Print Worksheet tự tải PDF, không hỏi; PDF có địa chỉ tài khoản. Xem FR-fleetio-parts-purchasing-fuel-041, E-fleetio-parts-purchasing-fuel-029, K27, K28.

## Phát hiện lượt 4 (03/11)

Nguồn: `run-notes/parts-purchasing-fuel.md`, mục Lượt 4; báo cáo đơn mua theo `run-notes/platform.md`.

- Đơn Draft đã Edit và lưu thì số vào Pending PO Qty ngay; "chỉ tính từ Purchased" chỉ đúng với đơn chưa Edit. Xem BR-fleetio-parts-purchasing-fuel-050, E-fleetio-parts-purchasing-fuel-032, D40, D41, OQ-13.
- Đơn Full tăng số đặt vẫn "Received, Full", không có Receive, không cộng Pending. Xem BR-fleetio-parts-purchasing-fuel-051, E-fleetio-parts-purchasing-fuel-033, D36, D37.
- Rating là số, nguồn điểm chưa rõ. Xem N13–N15, OQ-24.
- Total Amount của báo cáo đơn mua cộng cả Draft. Xem BR-fleetio-parts-purchasing-fuel-053, E-fleetio-parts-purchasing-fuel-034, D42.

## Phát hiện lượt 5 (03/11)

Nguồn: `run-notes/parts-purchasing-fuel.md`, mục Lượt 5. FIFO, LIFO, Average chưa đổi, chưa đo; mọi điều dưới đây là câu chữ màn (`Xem`).

- Đổi phương pháp là migration một chiều, có điều kiện chặn trước và ô tích nhận thức, không có xem thử. Xem FR-fleetio-parts-purchasing-fuel-045, BR-fleetio-parts-purchasing-fuel-054, BR-fleetio-parts-purchasing-fuel-055, K30, K35–K37.
- Hệ quả theo câu chữ: tồn nhận giá Unit Cost danh mục, tồn Archived về 0, FIFO và LIFO khoá dòng phụ tùng lệnh cũ. Xem BR-fleetio-parts-purchasing-fuel-056, K32–K35, OQ-11.

## Phát hiện lượt 6 (03/11)

Nguồn: `run-notes/parts-purchasing-fuel.md`, mục Lượt 6. FIFO chưa đổi, chưa đo; chỉ biết thêm điều kiện.

- Bị chặn ở Lệnh #103: "Work Order Labor Line Items is invalid", dòng công không sửa được, chỉ còn xoá. Xem E-fleetio-parts-purchasing-fuel-036, K40, K41, K43, OQ-28.
- Điều kiện lệnh dở chỉ tính lệnh có dòng phụ tùng. Xem BR-fleetio-parts-purchasing-fuel-057, K39, K42.
