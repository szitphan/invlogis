---
type: research
keyword: "Fleetio: phụ tùng, mua hàng, nhà cung cấp, nhiên liệu, công cụ"
status: draft
status_changed: 2026-11-03
status_reason: "đã review upstream, không cần sửa"
updated: 2026-11-03
links:
  - docs/_product/prd.md
  - docs/_product/saas-core-vs-tenant.md
  - docs/_research/2026-11-02-fleetio-app-teardown.md
  - docs/_research/fleetio/run-notes/parts-purchasing-fuel.md
---

# Giải pháp tham khảo: Phụ tùng, mua hàng và nhiên liệu

> Khuyến nghị: **Nên tham khảo** cho `purchasing`, `stock-movement`. **Chỉ lấy vài luật cảnh báo** cho nhóm nhiên liệu, vì Delta đã đi sâu hơn Fleetio. Không học cách Fleetio xử lý số vượt: tồn âm, chuyển kho, nhận vượt, trả quá số đều không chặn, có chỗ cắt số hoặc mất dấu âm mà vẫn báo thành công.

## 1. Idea Seed

Đơn mua đi qua từng trạng thái với một nút chính duy nhất ở mỗi bước. Khi nhận hàng, chọn nhập kho hay đưa vào lệnh sửa, và đường nào cũng đi qua kho nên sổ kho không mất dấu. Mỗi kho hiện tồn, điểm đặt lại, đang về, đã xuất cho lệnh. Mỗi biến động có sổ ghi số trước, số sau và chứng từ, kể cả khi sửa hoặc xoá dòng lệnh.

## 2. Context

**Feature Invlogis liên quan:** `purchasing` (#19), `stock-movement` (#20), `inventory-count` (#21), `workshop-payment` (#22), `business-partners` (#8), `product-catalog` (#7), `fuel-allowance` (#14), `fuel-issuing` (#27), `fuel-stations` (#25), `vehicle-telematics`.

**Tầng:** Gói Bảo dưỡng đội xe, Gói Nhiên liệu, Gói Giám sát nhiên liệu theo `docs/_product/saas-core-vs-tenant.md`.

**Nguồn và bằng chứng:** hai đợt chạy thật trên tài khoản dùng thử. Đợt 02/11/2026: phụ tùng `TEST-BRAKE-PAD-01`, kho `TEST-KHO-01`, nhà cung cấp `TEST-NCC-01`, Purchase Order #1, Work Order #100, hai phiếu dầu. Đợt 03/11/2026: kho `TEST-KHO-01`, `TEST-KHO-02`; phụ tùng `TEST-KHO-PT-A`, `TEST-KHO-PT-B`; ba nhà cung cấp `TEST-KHO-NCC-01`, `-02`, `-DAU`; PO #2 (Closed), PO #3 (Received, Full); WO #102; 14 phiếu dầu `TEST-KHO-F1` đến `F14` trên xe `TEST-KHO-01`. Chi tiết từng case: [[docs/_research/fleetio/run-notes/parts-purchasing-fuel.md|Nhật ký chạy]] và [[docs/_research/fleetio/srs/fleetio-parts-purchasing-fuel-spec.md|SRS]] Mục "Ma trận case".

**Cài đặt lúc chạy (chỉ đọc, không đổi):** Static Pricing, tắt tự đóng đơn, bật Track Inventory mặc định, bán kính cảnh báo dầu Fleetio: 2 dặm. Tài khoản chỉ có một người dùng, người đó có quyền duyệt.

**Nhãn bằng chứng:** `Chạy` đã thao tác và thấy kết quả · `Xem` thấy trên giao diện, không thao tác · `Docs` theo tài liệu công khai của hãng · `Suy` suy ra · `GĐ` giả định.

**Ngoài phạm vi:** Charging History (sạc xe điện) không xem theo yêu cầu user; Tools không mở trial theo lựa chọn của user.

## 3. User Types (preliminary)

| User Type | Pain Point | Primary Need |
|---|---|---|
| Nhân viên xưởng | Không biết phụ tùng còn hay đang về | Thấy tồn, đang về ngay khi lập lệnh |
| Nhân viên kho xưởng | Lệch tồn, không truy được | Sổ kho có số trước, số sau, chứng từ |
| Người duyệt mua | Đơn nhỏ cũng phải duyệt | Tự duyệt dưới ngưỡng |
| Quản lý cây dầu | Khó phát hiện đổ dầu bất thường | Cảnh báo tự động |

### 3.1 Tác vụ chính

| Vai trò | Tác vụ | Tần suất | Mức quan trọng | Ghi chú |
|---|---|---|---|---|
| Nhân viên xưởng | Lập đơn mua | Mỗi ngày | Cao | |
| Người duyệt | Duyệt đơn | Mỗi ngày | Cao | |
| Nhân viên kho xưởng | Nhận hàng, xuất cho lệnh | Mỗi ngày | Cao | Sai làm lệch tồn và chi phí |
| Nhân viên kho xưởng | Chỉnh tồn, chuyển kho, kiểm kê hàng loạt | Chưa đo | Trung bình | Fleetio không chặn số vượt |
| Nhân viên kho xưởng | Trả hàng nhà cung cấp | Chưa đo | Trung bình | Fleetio không có lý do đóng thiếu |
| Nhân viên cây dầu | Ghi phiếu cấp dầu | Mỗi ngày | Cao | |

## 4. Capabilities Breakdown

### P0 — must have

- K1 [Mới] [Gói: Bảo dưỡng đội xe] **Đơn mua theo trạng thái, một nút chính mỗi bước:** Approve, Mark as Purchased, Receive, Close; ghi ai làm ở mỗi bước. Fleetio: `Chạy` hết Draft, Approved, Purchased, Partial, Full, Closed và các đường lùi. Áp vào `purchasing`.
- K2 [Mới] [Gói: Bảo dưỡng đội xe] **Nhận hàng một phần nhiều lần;** lần sau tự gợi ý số còn lại. Fleetio: `Chạy`, nhận 5 trên 12 thì lần sau gợi ý 7; đợt trước nhận 4 rồi 6 trên 10.
- K3 [Mới] [Gói: Bảo dưỡng đội xe] **Ba nơi đến khi nhận:** nhập kho, thêm vào lệnh đang có, tạo lệnh mới. Fleetio: `Chạy` nhập kho và lệnh đang có; lệnh mới `Chạy` đến bước huỷ form. Áp vào `purchasing`, `stock-movement`.
- K4 [Mới] [Gói: Bảo dưỡng đội xe] **Thẻ tồn theo kho:** tồn hiện tại, điểm đặt lại, đang về theo đơn mua, đã xuất cho lệnh; bốn nút chỉnh, chuyển, đặt mua, menu. Fleetio: `Chạy`. Hợp với nhiều bãi đầu kéo, mooc. Áp vào `stock-movement`.
- K5 [Mới] [Gói: Bảo dưỡng đội xe] **Sổ kho:** ngày, kho, loại biến động, chứng từ, lý do, nhà cung cấp, số biến động, số trước, số sau, người làm. Sáu loại Initial, Manual, Transfer, Purchase Order, Work Order, Bulk Update. Fleetio: `Chạy`.
- K6 [Mới] [Gói: Bảo dưỡng đội xe] **Tìm phụ tùng hiện tồn từng kho** ngay trong ô chọn; phụ tùng chưa bật ở kho của đơn thì xám, có khoá. Fleetio: `Chạy`.
- K22 [Mới] [Gói: Bảo dưỡng đội xe] **Sổ kho ghi bù khi sửa hoặc xoá dòng lệnh:** giảm số lượng dòng hoặc xoá dòng thì sổ tự cộng lại, loại Work Order kèm số lệnh. Fleetio: `Chạy`. Dễ đối soát khi kiểm kê.

### P1 — should have

- K7 [Mới] [Gói: Bảo dưỡng đội xe] [Cấu hình] **Phương pháp tính giá tồn:** Trung bình, FIFO, LIFO, Giá cố định. Fleetio: `Chạy` Giá cố định, ba phương pháp còn lại `Xem`. Cần kế toán Delta quyết.
- K8 [Mới] [Gói: Bảo dưỡng đội xe] [Cấu hình] **Tự duyệt đơn dưới ngưỡng tiền.** Fleetio: `Xem` mẫu Automation. Ngưỡng là tham số mới, chưa có mã.
- K9 [Mới] [Gói: Bảo dưỡng đội xe] [Cấu hình] **Tự đóng đơn khi nhận đủ.** Fleetio: `Xem` cấu hình; khi tắt thì phải Close tay (`Chạy`).
- K10 [Mới] [Gói: Bảo dưỡng đội xe] **Nguồn phụ tùng trên lệnh:** "None (No Inventory Adjustment)" hoặc lấy từ kho. Fleetio: `Chạy`. Hợp với phụ tùng mua ngoài dùng ngay.
- K11 [Mới] [Cấu hình] **Phân loại nhà cung cấp quyết định họ xuất hiện ở đâu:** Sạc, Nhiên liệu, Phụ tùng, Dịch vụ, Xe; form tự tick theo ngữ cảnh. Fleetio: `Chạy`: đơn mua chỉ thấy nhà cung cấp có Parts, phiếu dầu chỉ thấy nhà cung cấp có Fuel. Áp vào `business-partners`.
- K12 [Mới] [Cấu hình] **Tạo nhanh đối tượng ngay trong ô chọn.** Fleetio: `Chạy`, với nhà cung cấp.
- K13 [Mới] [Gói: Nhiên liệu] **Phiếu dầu tính ngay:** quãng đường, mức tiêu hao, chi phí trên km, so với lần trước. Fleetio: `Chạy`. Đơn vị xem Mục 6.5.
- K14 [Mới] [Gói: Nhiên liệu] [Cấu hình] **Cờ trên phiếu dầu:** Cá nhân, Đổ một phần, Đặt lại mức dùng. Fleetio: `Chạy` cả ba. Đổ một phần được cộng dồn nên tiêu hao đúng; hợp đầu kéo đổ nhiều cây dầu dọc đường.
- K15 [Mới] [Gói: Giám sát nhiên liệu] [Cấu hình] **Cảnh báo sai vị trí đổ dầu**, theo bán kính khách đặt. Fleetio: `Xem` cấu hình, bán kính 2 dặm; không chạy được vì cần định vị và thẻ. Bán kính là tham số mới, chưa có mã.
- K16 [Mới] [Gói: Giám sát nhiên liệu] **Cảnh báo đổ vượt dung tích bình.** Fleetio: `Chạy` với phiếu nhập tay, chỉ cần đã khai dung tích, không cần tích hợp. Bản trước ghi sai là không kích hoạt khi nhập tay. Với đầu kéo cần khai đúng tổng bình.
- K23 [Mới] [Gói: Bảo dưỡng đội xe] **Trả hàng bằng điều chỉnh trên đơn:** nhập số âm tới mức đã nhận, tồn giảm, đơn lùi về nhận một phần. Fleetio: `Chạy` ở trạng thái nhận đủ. Lấy cơ chế, bỏ cách cắt số không báo.
- K24 [Mới] [Gói: Bảo dưỡng đội xe] **Nhận vào lệnh đi qua kho hai bước:** cộng kho trước, trừ khi lưu lệnh; huỷ form lệnh thì hàng vẫn ở kho. Fleetio: `Chạy`. Hợp phụ tùng đặt riêng cho xe nằm xưởng.
- K25 [Mới] [Gói: Bảo dưỡng đội xe] **Điều chỉnh tồn hai ô liên động:** gõ số biến động hoặc số mới, ô kia tự tính; bắt buộc lý do từ danh sách, cho phép số lẻ. Fleetio: `Chạy`. Danh sách lý do là tham số mới, chưa có mã.
- K26 [Mới] [Gói: Nhiên liệu] **Huỷ phiếu dầu bằng cờ Void:** số đồng hồ gạch ngang, không đẩy đồng hồ xe, không tính quãng đường. Fleetio: `Chạy`.

### P2 — nice to have

- K17 [Mới] [Gói: Bảo dưỡng đội xe] **Cập nhật phụ tùng hàng loạt** (Bulk Manage Parts): tab theo kho, sửa ô là tự lưu, có in phiếu kiểm kê. Fleetio: `Chạy` sửa số và tắt kho; Print Worksheet `Xem`. Không hỏi lý do nên chỉ hợp kiểm kê có kiểm soát.
- K18 [Mới] [Gói: Bảo dưỡng đội xe] **Đánh giá nhà cung cấp** bằng cột Rating. Fleetio: `Xem` cột.
- K19 [Mới] [Gói: Nhiên liệu] **Nhập giao dịch từ thẻ nhiên liệu.** Fleetio: `Xem` cấu hình WEX chỉ đọc; không có màn gán thẻ thử được. Cần tìm đối tác tương ứng ở Việt Nam.
- K20 [Mới] [Cấu hình] **Sạc xe điện:** phiên sạc, điện năng, đơn giá. Ngoài phạm vi theo yêu cầu user. Fleetio: `Xem` cột ở đợt đầu, không xem thêm.
- K21 [Mới] [Gói: Bảo dưỡng đội xe] **Quản lý công cụ:** nhóm loại nhắc riêng, gán cho người, nhắc không tự lặp. Fleetio: `Docs`, là gói thêm; không mở trial theo lựa chọn của user.
- K27 [Mới] [Gói: Bảo dưỡng đội xe] **Nhiều nhà cung cấp và lịch sử giá trên một phụ tùng:** thêm tay trong Purchase History, đơn mua tự thêm dòng, trang phụ tùng vẽ biểu đồ giá. Fleetio: `Chạy`.
- K28 [Mới] [Gói: Bảo dưỡng đội xe] **Sao chép đơn:** mở form mới điền sẵn, giữ giá đơn cũ, số đơn tăng. Fleetio: `Chạy`.

## 5. Core Flows (Happy Path)

### 5.1 Mua và nhận hàng

`Chạy` trọn với Purchase Order #1, #2, #3.

1. Lập đơn: chọn một nhà cung cấp, một kho, thêm dòng; đơn giá lấy từ danh mục, sửa được.
2. Lưu nháp hoặc lưu kèm duyệt. Đơn 0 dòng lưu được nhưng Approve khoá.
3. Duyệt, đánh dấu đã mua. Mỗi nút một cú bấm, không hộp xác nhận.
4. Nhận hàng một hoặc nhiều lần, chọn số lượng và nơi đến. Tồn đổi ngay.
5. Trả hàng bằng Make Adjustment nếu cần.
6. Đóng đơn. Đóng được cả khi nhận thiếu, không ghi lý do.

```
Draft ─> Approved ─> Purchased ─> Received, Partial ─> Received, Full ─> Closed
  ^          │  ^        │             ^      │              │
  └──────────┘  └────────┘             │      └── Closed     │
 Save as Draft   Unmark                └── Make Adjustment ──┘

Draft ─> Pending Approval ─┬─ Approved      (Docs, tài khoản một người không thấy nút)
                           └─ Rejected
```

Không có trạng thái hay nút huỷ riêng; thoát đơn chỉ có Close (từ Partial, Full) hoặc Delete. Closed không có nút mở lại.

### 5.2 Xuất phụ tùng cho lệnh

`Chạy` với Work Order #100, #102.

1. Trên lệnh, tìm phụ tùng, thấy tồn từng kho.
2. Chọn kho hoặc None, số lượng, gắn đầu việc nếu có. Form báo "This will make an inventory adjustment".
3. Lưu lệnh: tồn giảm ngay, ghi sổ kho kèm số lệnh, không chờ hoàn thành.
4. Sửa số lượng hoặc xoá dòng: sổ ghi bù.
5. Hoàn thành lệnh: sổ không có dòng mới, sinh Service Entry, Edit khoá. Mở lại: sổ không đổi, liên kết Service Entry biến mất.

```
Lệnh Open ─> Thêm phụ tùng từ kho ─> Lưu ─> Tồn giảm + Sổ kho (chứng từ: lệnh)
                                      │
                 Sửa số, xoá dòng ────┴─> Sổ ghi bù, tồn cộng lại
```

### 5.3 Tồn kho theo kho

`Chạy` với `TEST-KHO-PT-A`, `TEST-KHO-PT-B`.

1. Khai kho ở Settings.
2. Bật phụ tùng tại kho, nhập tồn đầu (ghi Initial).
3. Nhập qua đơn hoặc chỉnh tay có lý do.
4. Xuất khi lưu dòng lệnh; sửa hoặc xoá dòng thì sổ ghi bù.
5. Bulk Manage để kiểm kê.

### 5.4 Ghi phiếu dầu

`Chạy` 14 phiếu.

1. Chọn xe, ngày, số đồng hồ, số lít, đơn giá.
2. Chọn loại dầu, nhà cung cấp, tham chiếu; bật cờ Personal, Partial, Reset nếu cần.
3. Lưu: hệ thống tính tiêu hao, chi phí trên km, so với lần trước, gắn Capacity Alert.
4. Cộng vào chi phí xe; số đồng hồ mới đẩy nhắc bảo dưỡng.

```
Phiếu dầu ─┬─> Tổng tiền
           ├─> Quãng đường, tiêu hao, chi phí trên km (cần phiếu trước)
           ├─> Capacity Alert (số lít lớn hơn dung tích đã khai)
           ├─> Chi phí xe (tính cả Personal, Void)
           └─> Số km xe ─> Nhắc bảo dưỡng
```

## 6. System Behavior Deep Dive

### 6.1 Decision Points

| ID | Flow | Khi nào | YES | NO |
|---|---|---|---|---|
| D1 | 5.1 | Người lập có quyền duyệt | Lưu kèm duyệt, Approve | Chờ duyệt (`Docs`) |
| D2 | 5.1 | Hàng dùng ngay cho lệnh | Nhận vào lệnh, qua kho hai bước | Nhận vào kho |
| D3 | 5.2 | Lấy từ kho | Trừ tồn | Không đổi tồn |
| D4 | 5.4 | Có phiếu trước | Tính tiêu hao | Hiện N/A |
| D5 | 5.1 | Nhận thiếu, không đợi nữa | Close, không lý do | Nhận tiếp |
| D6 | 5.1 | Trả hàng | Make Adjustment số âm (Full, Closed) | Không có đường khác; Receive gõ âm thành nhận dương |
| D7 | 5.4 | Đã khai dung tích và số lít lớn hơn | Capacity Alert | Không cảnh báo |
| D8 | 5.4 | Phiếu trước là Partial | Cộng dồn số lít | Tính từ phiếu đó |

### 6.2 Scenario Matrix

Bảng đủ từng case ở SRS Mục "Ma trận case". Dưới đây là các case đổi cách hiểu nhất.

| From State | To State | Rule | Action | Result | Bằng chứng |
|---|---|---|---|---|---|
| Tồn 4 | Xuất 6 | Không chặn | Lưu | Tồn -2, nhãn "Out of Stock" | `Chạy` |
| Tồn 10 | Chỉnh -20, lý do Lost | Không chặn | Lưu | Tồn -10, không cảnh báo | `Chạy` |
| Tồn 6,5 | Chuyển 100 | Cắt theo tồn | Save | Báo thành công, chỉ chuyển 6,5, không báo đã cắt | `Chạy` |
| Đặt 12, nhận 5 | Mở nhận lần 2 | Tự gợi ý số còn lại | Gợi ý 7 | Partial | `Chạy` |
| Đặt 12 | Gõ 100 | Không chặn | Lưu | 105/12, tồn tăng đủ, tiền theo số đặt | `Chạy` |
| Đã nhận 5 | Receive gõ -5 | Mất dấu âm | Lưu | Nhận thêm +5, không báo | `Chạy` |
| Đã nhận 5 | Make Adjustment -6 | Cắt về -5 | Lưu | Sổ -5, tồn 2 thành -3, về Partial, không báo đã cắt | `Chạy` |
| Dòng PT-B 0/5 | Close | Cho đóng | Xác nhận | Closed, không ghi lý do | `Chạy` |
| Closed | Edit đơn giá | Không khoá dưới Static | Lưu | Tổng tính lại | `Chạy` |
| Có đơn tại kho | Tắt kho ở Bulk | Chặn | Gạt Active | Báo không tắt được | `Chạy` |
| Bình 60 | Phiếu 100 lít | Vượt dung tích | Lưu | Capacity Exception Volume "100 liters" | `Chạy` |
| Bình 60 | Phiếu 60 lít | Bằng dung tích | Lưu | Không cảnh báo | `Chạy` |

### 6.3 State Transitions

| Entity | Từ | Sang | Trigger | Quay lại được? | Bằng chứng |
|---|---|---|---|---|---|
| Đơn mua | Draft | Approved | Approve, Save & Approve | Có, Save as Draft; mất dòng Approved By | `Chạy` |
| Đơn mua | Approved | Purchased | Mark as Purchased | Có, Unmark as Purchased | `Chạy` |
| Đơn mua | Purchased | Received, Partial | Nhận một phần | Không có nút; chỉ về Approved trước khi nhận | `Chạy` |
| Đơn mua | Purchased | Received, Full | Nhận đủ một lần | Về Partial khi điều chỉnh giảm | `Chạy` |
| Đơn mua | Received, Partial | Received, Full | Nhận đủ | Có, Make Adjustment số âm | `Chạy` |
| Đơn mua | Received, Partial | Closed | Close, xác nhận | Không có nút mở lại | `Chạy` |
| Đơn mua | Received, Full | Closed | Close | Không có nút mở lại | `Chạy` |
| Đơn mua | Draft | Pending Approval | Submit for Approval | Chưa biết | `Docs` |
| Đơn mua | Pending Approval | Approved, Rejected | Người duyệt | Gửi lại Rejected chưa biết | `Docs` |
| Tồn tại kho | Không nhãn | Low Stock | Tồn từ điểm đặt lại trở xuống, trên 0 | Có, tồn vượt điểm | `Chạy` |
| Tồn tại kho | Low Stock, không nhãn | Out of Stock | Tồn từ 0 trở xuống | Có | `Chạy` |

Trạng thái đơn mua do hệ thống cố định, trang cấu hình không có nút thêm (`Xem`), khác với trạng thái lệnh sửa.

### 6.4 Interrupted Transactions

| Tình huống | Hệ thống còn lại gì | Resume | Cleanup |
|---|---|---|---|
| Xuất quá tồn, hàng chưa về | Tồn âm | Nhận hàng bù lên | Không tự xử lý |
| Nhận vào lệnh mới rồi huỷ form | Hàng ở kho, đơn thành Full, không có lệnh; có báo trước | Tự xuất cho lệnh khác | Không cần (`Chạy`) |
| Nhận vào lệnh đang có | Sổ +5 trước, -5 khi lưu lệnh | Lưu form lệnh | Không cần (`Chạy`) |
| Xoá dòng lệnh đã trừ kho | Sổ cộng lại đủ số (`Chạy`) | — | Tự động |
| Mở lại lệnh đã hoàn thành | Sổ không đổi, Service Entry mất liên kết | Sửa rồi hoàn thành lại | Chưa thử hoàn thành lại |
| Xoá cả lệnh đã trừ kho | Chưa biết, đã huỷ ở hộp xác nhận | — | OQ-9 |

### 6.5 Other Edge Cases

- **Không nên học, số vượt im lặng:** Fleetio cho tồn âm ở chỉnh tồn và xuất cho lệnh, nhận vượt không cảnh báo (`Chạy`). Invlogis cần quyết định chặn, cảnh báo, hay cho âm theo cấu hình.
- **Không nên học, cắt số mà báo thành công:** chuyển 100 khi có 6,5 chỉ chuyển 6,5; điều chỉnh -6 trên 5 nhận được cắt còn -5; gõ -5 ở Receive thành +5 (`Chạy`). Invlogis phải báo rõ số thực làm.
- **Thời điểm trừ kho:** trừ khi lưu lệnh, không chờ hoàn thành; hoàn thành lệnh không ghi sổ (`Chạy`). Với xưởng có xuất kho thực tế, nên gắn với phiếu xuất.
- **Không nên học, đơn vị sai:** xe dùng km và lít nhưng phiếu dầu hiện mpg (US). Giá trị đổi đúng: 29,40 mpg bằng 12,5 km/lít (`Chạy`). Invlogis cần lít trên 100 km.
- **Không nên học, lệch tiền 100 lần trên VND:** ở hộp Add Part gõ đúng và form đúng; lệch xuất hiện ở trang chi tiết lệnh, Service Entry và báo cáo dầu. Trang chi tiết xe lại đúng. Làm sai chi phí sửa chữa theo xe (`Chạy`, đã lặp lại). Bản trước ghi lệch ở hộp thêm phụ tùng là chưa đúng chỗ.
- **Không nên học, ô Shipping:** gõ 20000 thành 2.000.000, gõ 200 mới ra 20.000; ô Unit Cost của dòng thì đúng (`Chạy`).
- **Tự duyệt:** người tạo đơn tự duyệt được, một cú bấm, không hộp xác nhận (`Chạy`). Không kiểm được việc tách người vì tài khoản một người. Delta có thể cần tách hai người.
- **Vai trò của kho:** ở trang phụ tùng từng báo "You do not have access to any Part Locations" ngay sau khi tạo kho, trong khi form đơn mua vẫn chọn được kho (`Chạy` đợt 02/11). Chưa rõ nguyên nhân, `Suy` do dữ liệu quyền cũ trong phiên.
- **Số đồng hồ:** lùi cùng ngày không chặn (2.900 khi đã có 4.000), lùi ngày với số cao bị chặn, lùi ngày với số thấp lưu được và không đổi phiếu sau (`Chạy`).
- **Cảnh báo dầu không tự gỡ:** sửa phiếu từ 100 xuống 50 lít, cảnh báo vẫn còn, cột vẫn 100 (`Chạy`).
- **Enter trong ô Country:** vừa chọn vừa lưu form nhà cung cấp, ba lần đều vậy; dễ tạo bản ghi sớm (`Chạy`).
- **Không có trường thay thế, tương thích xe** trên form phụ tùng; chỉ có Replaced Parts trong bảo hành ở lệnh (`Xem`, chưa tìm ở nơi khác).
- **Giới hạn gói:** thanh "5 of 5" trên Vehicles; Save Vehicle quay mãi, không báo lỗi, xe không được tạo (`Chạy`). Giới hạn 5 xe là `Suy`.

### 6.6 Giải pháp đáng học

| Giải pháp | Vì sao | Hợp với Invlogis ở đâu |
|---|---|---|
| Thẻ tồn 4 số theo từng kho | Xưởng biết hàng đang về và đã xuất cho lệnh | Nhiều bãi đầu kéo, mooc |
| Sổ kho có số trước, số sau, chứng từ cho mọi biến động, kể cả sửa và xoá dòng lệnh | Dễ đối soát khi kiểm kê | `stock-movement`, `inventory-count` |
| Nhận thẳng vào lệnh đi qua kho hai bước, hàng không mất khi huỷ form | Không mất dấu nhập xuất | Phụ tùng đặt riêng cho xe nằm xưởng |
| Gộp phiếu không đầy khi tính tiêu hao, Reset khi thiếu phiếu | Tiêu hao không bị sai vì đổ lẻ | Đầu kéo đổ nhiều cây dầu dọc đường |
| Capacity Alert chỉ cần dung tích bình, không cần tích hợp | Rẻ, chạy được ngay | Đầu kéo cần khai đúng tổng bình |

### 6.7 Điểm yếu, Invlogis nên làm khác

| Điểm yếu của Fleetio | Đề xuất Invlogis |
|---|---|
| Tồn âm, chuyển kho, nhận vượt, trả quá số không chặn; có chỗ cắt số, mất dấu âm mà vẫn báo thành công | Báo rõ số yêu cầu và số thực làm; chặn hay cho vượt theo tham số khách, tham số mới, chưa có mã |
| Tiền VND lệch 100 lần ở chi tiết lệnh, Service Entry, báo cáo dầu | Một quy tắc định dạng tiền xuyên suốt, có kiểm thử cho tiền không có phần lẻ |
| Đơn Closed vẫn sửa được giá, không mở lại, không có lý do đóng thiếu | Khoá giá sau đóng; bắt lý do khi đóng thiếu; mở lại có quyền riêng |
| Không có huỷ đơn sau Approved, chỉ lùi Draft hoặc Delete | Trạng thái Huỷ có lý do |
| Cảnh báo dầu không xoá khi sửa phiếu | Tính lại cảnh báo khi sửa phiếu |
| Số đồng hồ lùi cùng ngày không chặn | Cảnh báo khi số thấp hơn phiếu đã có |
| Bulk sửa tồn không hỏi lý do | Bắt lý do hoặc gắn đợt kiểm kê |
| Enter lưu form sớm ở ô chọn | Enter chỉ chọn, nút Lưu mới lưu |

## 7. Validation, Limits & Wording

### 7.1 Validation rules

| Field | Rule | Bằng chứng |
|---|---|---|
| Đơn mua | Bắt buộc nhà cung cấp, kho; chọn đủ mới hiện dòng hàng | `Chạy` |
| Dòng đơn mua | Không trùng phụ tùng trong một đơn; số lượng 0 vẫn duyệt được | `Chạy` |
| Phụ tùng | Mã phụ tùng bắt buộc và duy nhất | `Xem` |
| Kho | Tên duy nhất | `Chạy` |
| Điều chỉnh tồn | Lý do bắt buộc, Save khoá khi trống | `Chạy` |
| Điểm đặt lại | Tài liệu nói phải lớn hơn 0; thực tế lưu được 0 | `Chạy` |
| Nhà cung cấp | Bắt buộc tên, địa chỉ, thành phố, tỉnh, mã bưu chính, quốc gia; phân loại không bắt buộc | `Chạy` |
| Phiếu dầu | Bắt buộc xe, ngày, số đồng hồ (kể cả Void), số lít; 0 lít vẫn lưu được | `Chạy` |
| Hoàn thành lệnh | Cần Started At, Start Odometer theo cài đặt tài khoản | `Chạy` |

Mã bưu chính bắt buộc không hợp với Việt Nam; Invlogis không nên bắt.

### 7.2 Limits & Quotas (exact values)

| Tham số | Giá trị | Window | Behavior khi vượt |
|---|---|---|---|
| Bán kính cảnh báo đổ dầu | Fleetio: 2 dặm, có Disabled | Mỗi giao dịch | Gắn cảnh báo (`Docs`, chưa chạy) |
| Số xe trên tài khoản dùng thử | Fleetio: "5 of 5" | Tài khoản | Save Vehicle quay mãi, không báo lỗi (`Chạy`, giới hạn `Suy`) |
| Số lý do điều chỉnh | Fleetio: 11 | — | Broken, Checked Inventory, Expired, Found, Lost, Miscellaneous, Received, Sold, Stolen, Transferred, Used |

### 7.3 Wording samples (exact strings)

#### Success messages

| Tình huống | Wording |
|---|---|
| Duyệt | "Purchase Order #2 approved" |
| Đã mua | "Purchase Order #1 marked as purchased" |
| Bỏ đã mua | "unmarked as purchased" |
| Nhận hàng | "Purchase Order #1 was successfully received" |
| Điều chỉnh đơn | "was successfully adjusted" |
| Đóng đơn | "was successfully closed" |
| Sửa đơn | "was successfully updated" |
| Sửa phụ tùng | "Part was successfully updated" |
| Chuyển kho | "Parts transfer was successful." |
| Bulk | "All changes saved" |

#### Info / neutral messages

| Tình huống | Wording |
|---|---|
| Lấy từ kho | "This will make an inventory adjustment" |
| Chưa chọn đủ | "Select a Vendor and Part Location first." |
| Tắt kho | "A location cannot be disabled if the part is used on any incomplete Work Orders, or on Purchase Orders in any status." |
| Make Adjustment | "Negative values are allowed up to the quantity received on this order." |
| Đóng đơn | "Are you sure you want to close the selected purchase order?" |
| Nhận vào lệnh có sẵn | "These parts will be received to your inventory before being added to the selected work order." |
| Nhận vào lệnh mới | "Your received parts will remain in inventory even if you don't save this work order." |
| Mở lại lệnh | "Changing this completed Work Order to an incomplete Status will automatically restore any archived parts, part locations, and contacts associated with line items." |
| Xoá dòng lệnh | "Are you sure you want to permanently delete this line item?" |
| Xoá lệnh | "All data will be lost forever." |
| Phiếu không có nơi đổ | "Location is unknown or not available" |

#### Error messages

| Tình huống | Wording |
|---|---|
| Trùng tên kho | "has already been taken", "Part Location could not be created" |
| Tắt kho khi có đơn | "This part can't be deactivated because it's used in one or more purchase orders at this location." |
| Dòng trùng | "Part TEST-KHO-PT-A is duplicated", "Purchase Order could not be created" |
| Hoàn thành lệnh thiếu | "Please edit and fix the following errors: Started At can't be blank", "Start Odometer can't be blank (per your account settings)" |
| Void trống số, nhà cung cấp thiếu trường | "can't be blank" |
| Lùi ngày số cao | "must be less than 1,000 or marked as void" |

## 8. Assumptions

- Quy trình mua của Delta có nhiều cấp duyệt hơn Fleetio; cần đối chiếu.
- Lệnh hút dầu, lệch dầu của Delta giữ nguyên theo `vehicle-telematics`, không thay bằng cảnh báo của Fleetio.
- Toàn bộ kết quả về giá tính dưới Static Pricing; FIFO, LIFO, Average chưa thử vì không đổi cài đặt.

## 9. Risks

| Rủi ro | Mức | Giảm thiểu |
|---|---|---|
| Cho tồn âm làm lệch sổ kho | Cao | Cấu hình theo khách, có cảnh báo và báo cáo |
| Cắt số không báo làm người dùng tin số sai | Cao | Báo số yêu cầu và số thực làm |
| Nhận thẳng vào lệnh làm mất dấu nhập xuất | Trung | Ghi đủ hai bút toán như Fleetio |
| Phương pháp giá khác kế toán Việt Nam | Cao | Hỏi kế toán trước |
| Học theo bảng dữ liệu Fleetio với tiền không có phần lẻ | Cao | Kiểm thử VND trên mọi trang tổng hợp |

## 10. Success Criteria (preliminary)

- Mọi biến động kho truy được về chứng từ.
- Xưởng biết tồn và hàng đang về ngay trên lệnh.
- Mọi thao tác số vượt đều báo rõ số thực làm.

## 11. Open Questions

| ID | Câu hỏi | Trạng thái | Nguồn khách |
|---|---|---|---|
| OQ-1 | Delta có cho xuất kho âm không? Trừ kho lúc nào? Fleetio: cho âm, trừ khi lưu dòng lệnh | Mở | Chưa có trong tài liệu khách gửi |
| OQ-2 | Delta tính giá tồn theo phương pháp nào? | Mở | Chưa có trong tài liệu khách gửi |
| OQ-3 | Duyệt đơn có theo ngưỡng tiền, có được tự duyệt không? | Mở | Chưa có trong tài liệu khách gửi |
| OQ-4 | Có nhận hàng thẳng vào lệnh sửa không? Fleetio luôn đi qua kho hai bước | Mở | Chưa có trong tài liệu khách gửi |
| OQ-5 | Có cần cảnh báo vị trí đổ dầu ở cây dầu ngoài không? | Mở | Chưa có trong tài liệu khách gửi |
| OQ-6 | Fleetio huỷ đơn, đóng thiếu, nhận vượt, trả hàng thế nào? | Đã trả lời: không có nút huỷ sau Approved, chỉ Delete hoặc lùi Draft; đóng được khi nhận thiếu; nhận vượt được; trả hàng qua Make Adjustment ở Full và Closed. Phần Rejected chuyển sang OQ-8 | Không áp dụng |
| OQ-7 | Xoá dòng phụ tùng có hoàn kho không? | Đã trả lời: có, sổ +20, tồn về 9,5. Phần xoá lệnh chuyển sang OQ-9 | Không áp dụng |
| OQ-8 đến OQ-20 | Các điểm Fleetio chưa thử được | Mở, liệt kê ở SRS Mục 12 | Không áp dụng |
| OQ-21 | Khi nhận vượt, trả quá số, đóng thiếu, Delta muốn chặn, cảnh báo hay chỉ ghi nhận? | Mở | Chưa có trong tài liệu khách gửi |

## 12. Next Steps

- Dùng Mục 4, Mục 6.6, Mục 6.7 làm gợi ý khi `/brainstorm purchasing`, `/brainstorm stock-movement`.
- Đưa ý K15, K16 vào danh sách đối chiếu với `vehicle-telematics`.
