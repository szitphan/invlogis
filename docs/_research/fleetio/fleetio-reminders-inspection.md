---
type: research
keyword: "Fleetio: nhắc bảo dưỡng, bộ lịch, gia hạn giấy tờ, kiểm tra xe"
status: draft
status_changed: 2026-11-03
status_reason: "đã review upstream, không cần sửa"
updated: 2026-11-03
links:
  - docs/_product/prd.md
  - docs/_research/fleetio/fleetio-repair.md
  - docs/_research/2026-11-02-fleetio-app-teardown.md
  - docs/_research/fleetio/run-notes/reminders-inspection.md
  - docs/_research/fleetio/run-notes/tires.md
  - docs/_research/fleetio/run-notes/location-dispatch.md
---

# Giải pháp tham khảo: Nhắc bảo dưỡng và kiểm tra xe

> Khuyến nghị: **Nên tham khảo mạnh** cho `reminders`. **Kiểm tra xe chưa có feature ở Invlogis**, có thể là tính năng mới đáng cân nhắc, cần hỏi Delta. Tài liệu mô tả Fleetio đang làm gì; đề xuất cho Invlogis tách riêng, chưa phải yêu cầu đã chốt.

## 1. Idea Seed

Xe được nhắc bảo dưỡng theo thời gian hoặc số km, trục nào đến trước thì tính trục đó. Số km đến từ mọi nguồn nên trạng thái nhắc tự đổi ngay khi lưu. Hoàn thành qua lệnh hoặc phiếu dịch vụ thì kỳ sau tính từ lần làm thật. Giấy tờ là loại nhắc riêng, gia hạn bằng cách sửa tay ngày. Lái xe làm phiếu kiểm tra trên biểu mẫu tự dựng; mục Không đạt tự thành sự cố, lỗi lặp gộp vào sự cố đang mở; phiếu tự gắn chuyến đang chạy và vị trí nộp.

## 2. Context

**Feature Invlogis liên quan:** `reminders` (#18), chưa chi tiết hoá, thuộc Gói Bảo dưỡng đội xe. Kiểm tra xe: tìm "kiểm tra xe", "checklist" trong brainstorm Phương tiện và Lệnh vận tải không ra kết quả; chưa chắc tài liệu khách không có.

**Nguồn và bằng chứng:** chạy thật hai đợt trên tài khoản dùng thử. Đợt 02/11/2026: nhắc "Brake Pads Replacement" trên `TEST-XE-01`; biểu mẫu `TEST - Pre-trip inspection`, `TEST - Quick check`; phiếu #125988723. Đợt 03/11/2026: 8 đầu việc `TEST-NHAC-A..H`, bộ lịch `TEST-NHAC-BO-LICH`, gia hạn xe và liên hệ, biểu mẫu `TEST-NHAC-PHIEU`, lệnh #101, các phiếu dịch vụ, phiếu kiểm và sự cố #47 đến #50, cộng phiếu kiểm lốp (`TEST-LOP kiem lop`) và phiếu có vị trí giả lập. Chi tiết ở [[docs/_research/fleetio/run-notes/reminders-inspection.md|ghi chú chạy]].

**Nhãn bằng chứng:** `Chạy` đã thao tác · `Chạy (vị trí giả lập)` thao tác với toạ độ giả · `Xem` thấy trên giao diện · `Docs` tài liệu hãng · `Suy` suy ra · `GĐ` giả định.

**Giới hạn đợt chạy:** gói dùng thử chặn ở 5 xe ("Your plan is limited to 5 vehicles"), nên không có xe riêng để thử mooc không đồng hồ, xe giờ máy, đồng hồ phụ, phiếu riêng đầu kéo và mooc. Lịch kiểm cần qua ngày thật nên Due Soon, Overdue, Skipped chưa thấy. App Fleetio Go chưa kiểm.

## 3. User Types (preliminary)

| User Type | Pain Point | Primary Need |
|---|---|---|
| Quản lý phương tiện | Xe quá hạn bảo dưỡng mới biết | Danh sách sắp đến hạn, quá hạn |
| Nhân viên xưởng | Đặt lịch từng xe rất tốn công | Bộ lịch theo dòng xe |
| Lái xe | Phiếu giấy mất thời gian | Kiểm nhanh trên điện thoại |
| Admin của khách | Mỗi khách một mẫu phiếu | Tự dựng biểu mẫu, không cần lập trình |

### 3.1 Tác vụ chính

| Vai trò | Tác vụ | Tần suất | Mức quan trọng | Ghi chú |
|---|---|---|---|---|
| Quản lý phương tiện | Rà nhắc đến hạn | Mỗi ngày | Cao | Bỏ sót làm hỏng xe, trễ đăng kiểm |
| Nhân viên xưởng | Xử lý nhắc thành lệnh | Mỗi ngày | Cao | |
| Lái xe | Nộp phiếu kiểm tra | Mỗi ca | Cao | Kiểm khống làm mất giá trị dữ liệu |
| Admin của khách | Dựng biểu mẫu, gán xe | Hiếm | Trung | |

## 4. Capabilities Breakdown

### P0 — must have

- N1 [Mới] [Gói: Bảo dưỡng đội xe] [Cấu hình] **Nhắc theo hai trục:** thời gian và số km, trục nào đến trước, mỗi trục có ngưỡng Sắp đến hạn riêng; chỉ cần một trục, thiếu cả hai bị chặn; ngưỡng phải nhỏ hơn chu kỳ. `Chạy`. Fleetio: ngưỡng điền sẵn 2 tuần, 500 km. Chu kỳ, ngưỡng là tham số mới, chưa có mã.
- N2 [Mới] [Gói: Bảo dưỡng đội xe] **Trạng thái tự đổi ngay khi lưu số km, từ bất kỳ nguồn nào, không chờ job đêm.** `Chạy`: đo đủ biên còn 501, 500, 1, 0, -1 km ra Upcoming, Due Soon, Due Soon, Overdue, Overdue. Đúng mốc đã Overdue dù chữ vẫn ghi "0 kilometers remaining". Lấy theo trục xấu nhất.
- N3 [Mới] [Gói: Bảo dưỡng đội xe] **Tự lấy lần hoàn thành gần nhất** từ lịch sử khi tạo nhắc; chưa từng làm thì hiện "Never logged for this vehicle". `Chạy`.
- N4 [Mới] [Gói: Bảo dưỡng đội xe] **Xem trước lịch:** form hiện 5 kỳ tới và báo lỗi ngưỡng ngay trong khối xem trước. `Chạy`. Điểm yếu: form Edit không làm mới theo số mới.
- N5 [Mới] [Gói: Bảo dưỡng đội xe] [Cấu hình] **Nhắc giấy tờ xe, người** theo loại, mỗi xe một nhắc cho mỗi loại, có ngày đến hạn và ngưỡng báo trước. `Chạy`. Fleetio: loại xe là Emission Test, Inspection, Insurance, Registration; loại liên hệ là Certification, License Renewal; ngưỡng mặc định xe 3 tuần, liên hệ 4 tuần. Thêm loại mới chưa thử. Danh sách loại, ngưỡng là tham số mới, chưa có mã.
- N6 [Mới] [Gói: Bảo dưỡng đội xe] **Từ nhắc đi thẳng sang xử lý:** nút Resolve trên từng dòng: Add to Work Order (mới hoặc có sẵn), Add to service history; menu: tạm hoãn, Recalculate Compliance. `Chạy`. Draft Work Order xám, có icon khoá, bấm không phản hồi; Find a shop, Send Notifications chỉ `Xem`.
- N19 [Mới] [Gói: Bảo dưỡng đội xe] **Kỳ sau tính từ lần làm thật:** ngày và số đồng hồ của lần hoàn thành, không từ mốc dự kiến; làm sớm là mất phần còn lại của chu kỳ. `Chạy`.
- N20 [Mới] [Gói: Bảo dưỡng đội xe] **Lệnh chưa xong không đổi trạng thái nhắc:** lệnh Open chỉ gắn dải "This Service Task was added to Work Order"; Completed mới tính kỳ mới và sinh Service Entry. `Chạy`.
- N21 [Mới] [Gói: Bảo dưỡng đội xe] **Đầu việc khớp là nhận:** ghi Service Entry có đúng đầu việc thì nhắc tự coi là đã làm, không cần đi từ nhắc. `Chạy`.
- N22 [Mới] [Gói: Bảo dưỡng đội xe] **Đặt tay mốc kỳ tới:** mặc định hôm nay + chu kỳ, đồng hồ hiện tại + chu kỳ; tự tắt sau một lần hoàn thành. `Chạy`. Đây là đường đúng để xe đã chạy lâu không bị quá hạn ngay.

### P1 — should have

- N7 [Mới] [Gói: Bảo dưỡng đội xe] [Cấu hình] **Biểu mẫu kiểm tra tự dựng** với 10 loại mục và Section: Pass/Fail, Number, Free Text, Dropdown, Date/Time, Meter Entry, Photo, Signature, Inventory Adjustment, Tire Readings. `Chạy` phần cấu hình; Inventory Adjustment, Photo chưa làm trên phiếu. Meter Entry chỉ một mục mỗi biểu mẫu. Áp cho feature mới, đề xuất tên `vehicle-inspection`.
- N8 [Mới] [Gói: Bảo dưỡng đội xe] [Cấu hình] **Luật theo mục:** đổi nhãn Đạt/Không đạt, cho N/A, bắt ảnh hoặc ghi chú khi Đạt, khi Không đạt; Number có khoảng, ngoài khoảng tự Fail, biên tính là đạt; Dropdown gắn "Fail item if chosen". `Chạy`.
- N9 [Mới] [Gói: Bảo dưỡng đội xe] **Workflow theo biểu mẫu:** ba trigger (mục đạt, mục lỗi, nộp phiếu); action đổi trạng thái xe, gửi email, tạo sự cố, gán và bỏ gán người với xe. Biểu mẫu mới có sẵn một workflow "ANY Failed Inspection Item → Create an issue". `Chạy` tạo sự cố và tắt workflow; các action khác `Xem`. Không có action tạo lệnh sửa chữa.
- N10 [Mới] [Gói: Bảo dưỡng đội xe] **Vòng đời mục lỗi:** Needs Action, Open Issue, Acknowledged, Resolved, có Failure Timeline. `Chạy`. Needs Action chỉ ra khi workflow tắt; Acknowledged là điểm cuối, không quay lại. Áp vào `incident-report`.
- N11 [Mới] [Gói: Bảo dưỡng đội xe] [Cấu hình] **Gán biểu mẫu theo luật:** mọi xe, theo thuộc tính xe, hoặc xe cụ thể; lịch Daily đến Yearly, bắt đầu trễ, nhắc người lái; không đặt lịch thì dùng "as needed". `Chạy` phần gán xe cụ thể với lịch Daily. Không thấy lịch theo số đồng hồ trong form.
- N12 [Mới] [Gói: Bảo dưỡng đội xe] **Bộ lịch theo dòng xe:** một bộ nhiều đầu việc nhiều xe, đồng hồ chính và phụ; chỉ gắn xe cùng đơn vị đồng hồ; có "Set First Service". `Chạy`. Sửa lịch trên bộ làm nhắc đang chạy đổi trạng thái sau xử lý ngầm.
- N13 [Mới] [Gói: Bảo dưỡng đội xe] **Tỷ lệ tuân thủ** theo lịch sử đúng hạn, trễ, ghi từng lần ("3 weeks, 6 days ahead · 1,600 kilometers ahead"). `Chạy`. Ngày sớm nhưng km vượt vẫn Late. Mức trễ 10% chu kỳ là `Docs`, chưa đo biên. Là tham số mới, chưa có mã.
- N14 [Mới] [Gói: Bảo dưỡng đội xe] [Cấu hình] **Chống kiểm khống bằng vị trí:** cảnh báo khi một tỉ lệ mục được kiểm từ cùng vị trí, hoặc một mục lệch xa các mục khác. `Xem` cấu hình; `Docs` Fleetio: Proximity Threshold 50–100%, mặc định 80%, Distance Threshold mặc định 100 m. `Chạy (vị trí giả lập)`: trên web không kích hoạt được, mọi phiếu `location_exception` false, gói tin chỉ có một cặp toạ độ cấp phiếu. Ngưỡng là tham số mới, chưa có mã.
- N15 [Mới] [Gói: Bảo dưỡng đội xe] [Cấu hình] **Cấm dùng ảnh có sẵn:** chỉ cho chụp bằng camera. `Xem`, bật mặc định, chưa thử chụp. Rất hợp với thói quen gửi lại ảnh cũ.
- N23 [Mới] [Gói: Bảo dưỡng đội xe] **Bảng đối chiếu trước khi gán bộ lịch:** cột Service Task, Conflicting, Duplicate, New Interval, kèm câu cảnh báo chung. `Chạy`. Nhắc tay trùng đầu việc giữ nguyên mã, đổi sang lịch bộ.
- N24 [Mới] [Gói: Bảo dưỡng đội xe] **Gộp nhiều nhắc vào một lệnh:** hộp Resolve liệt kê mọi nhắc của xe để tick thêm. `Chạy`. Vào xưởng làm luôn nhiều việc.
- N25 [Mới] [Gói: Bảo dưỡng đội xe] **Gộp lỗi lặp:** mục lỗi lại khi sự cố còn mở không sinh sự cố mới, chỉ thêm dòng Item Failures và mốc Failure Timeline; sau Resolved thì sinh sự cố mới. `Chạy`.
- N26 [Mới] [Gói: Bảo dưỡng đội xe] **Phiếu ăn theo chuyến đang chạy:** trường Job tự gắn việc đang gán cho xe lúc nộp. `Chạy`. Liên kết kiểm trước chuyến với Lệnh vận tải.
- N27 [Mới] [Gói: Bảo dưỡng đội xe] **Phiên bản biểu mẫu:** sửa mẫu không đổi phiếu cũ, phiếu cũ mang nhãn "Past Version"; phiếu đã nộp không sửa được. `Chạy`.
- N28 [Mới] [Gói: Bảo dưỡng đội xe] **Đọc lốp từ phiếu:** tự sinh ô theo cấu hình trục, khai trục và lắp lốp thiếu ngay trong phiếu, ghi về Tire Readings. `Chạy`. Spare không vào phiếu; mức tối thiểu của biểu mẫu tách khỏi mức của lốp.
- N29 [Mới] [Gói: Bảo dưỡng đội xe] **Vị trí nộp phiếu thành vị trí xe:** phiếu ghi vị trí trình duyệt, sinh Location Entry, xe lên bản đồ. `Chạy (vị trí giả lập)`. Máy chủ tin toạ độ gửi lên, không phát hiện toạ độ giả.

### P2 — nice to have

- N16 [Mới] [Gói: Bảo dưỡng đội xe] **Chuyển phiếu giấy thành biểu mẫu số** từ PDF hoặc ảnh bằng AI. `Xem`, nhãn Beta, chưa tải gì. Hợp với khách đang dùng phiếu giấy.
- N17 [Mới] [Gói: Bảo dưỡng đội xe] **Dự đoán ngày đến hạn** từ số km trung bình ngày. `Xem` nút Enable Forecasting, chưa bật vì là cài đặt cấp tài khoản; kết quả dự báo chỉ `Docs`.
- N18 [Mới] [Gói: Bảo dưỡng đội xe] **Thời lượng làm phiếu và nguồn nộp** ghi tự động. `Chạy`: "Duration 2m 17s", "Fleetio Web App". Thời lượng quá ngắn là dấu hiệu kiểm khống (`Suy`).
- N30 [Mới] [Gói: Bảo dưỡng đội xe] **KPI đếm theo xe:** 2 nhắc Overdue trên 1 xe vẫn là "Overdue Vehicles 1". `Chạy`. Hợp câu hỏi "bao nhiêu xe cần vào xưởng".

## 5. Core Flows (Happy Path)

### 5.1 Vòng đời một nhắc bảo dưỡng

Đã chạy trọn vòng, kể cả đóng nhắc bằng lệnh và bằng phiếu dịch vụ.

1. Dựng đầu việc, tạo nhắc lẻ hoặc gán bộ lịch. Nhắc chưa có lịch sử: mốc km là bội số chu kỳ tính từ 0, mốc thời gian tính từ hôm nay; muốn tính từ số hiện tại thì đặt tay.
2. Số km tăng từ lệnh, phiếu đổ dầu, phiếu kiểm, nhập tay hay thiết bị.
3. Hệ thống đổi trạng thái ngay khi lưu, theo trục xấu nhất.
4. Người dùng xử lý từ Resolve hoặc tạm hoãn.
5. Lệnh Open chưa đổi gì; lệnh Completed hoặc Service Entry mới tính kỳ mới từ lần làm và ghi On-Time hoặc Late.
6. Không có trạng thái Đóng: nhắc lặp vòng.

```
Upcoming ── còn ≤ ngưỡng ──> Due Soon ── đồng hồ ≥ mốc ──> Overdue
    ▲                           ▲                            │
    │                           └── void đồng hồ, lùi ───────┤
    └────── hoàn thành: kỳ mới từ lần làm, ra trạng thái theo mốc mới ─┘
              Tạm hoãn: về trạng thái thường khi hết hạn hoặc Remove Snooze
```

### 5.2 Gia hạn giấy tờ

1. Tạo nhắc theo loại, chọn xe hoặc liên hệ, ngày đến hạn, ngưỡng.
2. Trạng thái Due Soon, Overdue theo ngày.
3. Gia hạn: sửa tay Due Date sang kỳ mới. Không có Resolve, không lưu lịch sử, không tải giấy tờ mới.

### 5.3 Kiểm tra xe

1. Admin dựng biểu mẫu, từ trống, từ mẫu có sẵn hoặc từ phiếu giấy (`Xem`).
2. Admin gán xe, đặt lịch nếu cần; xử lý ngầm hơn 1 phút, trong lúc đó ô chọn xe rỗng.
3. Lái xe chọn biểu mẫu và xe, làm phiếu một lần xong, không có nháp. Hệ thống ghi giờ bắt đầu, vị trí, chuyến đang chạy.
4. Nộp phiếu: mục lỗi có workflow tự thành sự cố (gộp nếu đang mở); workflow tắt thì Needs Action. Xem tiếp [[docs/_research/fleetio/fleetio-repair.md|Sửa chữa]] Mục 5.2.

```
Dựng biểu mẫu ─> Gán xe, lịch ─> Làm phiếu ─> Nộp ─┬─ Đạt hết: lưu lịch sử
                                                   ├─ Lỗi, workflow bật: Sự cố ─> Lệnh hoặc Resolve with Note
                                                   └─ Lỗi, workflow tắt: Needs Action ─> Acknowledge hoặc Create Issue
```

## 6. System Behavior Deep Dive

### 6.1 Decision Points

| ID | Flow | Khi nào | YES | NO |
|---|---|---|---|---|
| D1 | 5.1 | Nhiều xe cùng lịch | Dùng bộ lịch | Nhắc riêng từng xe |
| D2 | 5.1 | Nhắc đến hạn, chưa sửa được | Tạm hoãn đến ngày chọn | Xử lý ngay |
| D3 | 5.3 | Biểu mẫu có lịch | Theo dõi đến hạn, quá hạn | Làm khi cần, không bao giờ quá hạn (`Docs`) |
| D4 | 5.3 | Vị trí các mục gần như trùng nhau | Gắn Location Exception (`Docs`) | Bình thường; trên web luôn rơi vào nhánh này |
| D5 | 5.1 | Nhắc chưa có lịch sử, xe đã chạy nhiều | Đặt tay mốc kỳ tới | Quá hạn ngay vì mốc tính từ 0 |
| D6 | 5.3 | Workflow "mục lỗi tạo sự cố" đang bật | Sinh hoặc gộp sự cố | Needs Action |
| D7 | 5.3 | Sự cố của mục đó còn mở | Gộp, thêm mốc thời gian | Sự cố mới, không mở lại sự cố cũ |

### 6.2 Cases đã chạy

Đủ ở [[docs/_research/fleetio/srs/fleetio-reminders-inspection-spec.md|SRS]] Mục 13, gồm cả điều không xảy ra.

### 6.3 State Transitions

| Entity | Từ | Sang | Trigger | Quay lại được? | Bằng chứng |
|---|---|---|---|---|---|
| Nhắc | Upcoming | Due Soon | Còn ≤ ngưỡng | Có khi mốc đổi | `Chạy` |
| Nhắc | Due Soon | Overdue | Đồng hồ ≥ mốc, hoặc đến ngày | Có: Void đồng hồ, hoàn thành, sửa chu kỳ | `Chạy` |
| Nhắc | Overdue | Due Soon | Void đồng hồ, hoặc hoàn thành khi mốc mới gần | Có | `Chạy` |
| Nhắc | Overdue | Upcoming | Sửa chu kỳ, không dấu vết | Có | `Chạy` |
| Nhắc | Overdue | Snoozed | Chọn ngày hoãn ở tương lai | Tự về dưới 2 phút sau mốc, hoặc Remove Snooze, hoặc hoàn thành | `Chạy` |
| Gia hạn | Due Soon | Overdue | Sửa ngày về quá khứ | Có, sửa ngày | `Chạy` |
| Mục lỗi | (nộp phiếu) | Issue #n | Workflow bật | Không | `Chạy` |
| Mục lỗi | (nộp phiếu) | Needs Action | Workflow tắt | Không | `Chạy` |
| Mục lỗi | Needs Action | Acknowledged | Acknowledge, ghi chú tuỳ chọn | Không, trạng thái cuối | `Chạy` |
| Mục lỗi | Needs Action | Open Issue | Create Issue | Chưa biết | `Xem`, chưa bấm |
| Mục lỗi | Open Issue | Resolved | Resolve with Note | Reopen chưa bấm | `Chạy` |

### 6.4 Interrupted Transactions

| Tình huống | Hệ thống còn lại gì | Resume | Cleanup |
|---|---|---|---|
| Không có quyền vị trí | Vẫn làm được phiếu, có cảnh báo | Phiếu ghi "Location permission was not enabled" | Không có |
| Rời form phiếu đang làm | Trình duyệt chặn "Leave site?", phiếu mất | Không có nháp ở Inspection History (`Chạy`) | Không có |
| Đổi biểu mẫu sau khi đã có phiếu | Phiếu cũ giữ nhãn cũ, nhãn "Past Version" (`Chạy`) | Không cần | Không có |
| Đang xử lý ngầm gán xe vào biểu mẫu | Tab xe rỗng, ô chọn xe "No options" hơn 1 phút (`Chạy`) | Tự xong, không báo ở tab đang mở | Không có |
| Đang đồng bộ bộ lịch | Nhắc cũ chưa đổi khoảng 1 phút (`Chạy`) | Thông báo "Complete" | Không có |

### 6.5 Other Edge Cases

- **Xe không có GPS, không có số km mới:** nhắc theo số km đứng yên, chỉ trục thời gian còn tác dụng (`Suy`).
- **Số km bất thường** có thể đẩy sai trạng thái nhắc; xem [[docs/_research/fleetio/fleetio-vehicle.md|Phương tiện]] Mục 6.5. Void số sai thì trạng thái lùi ngay (`Chạy`).
- **Mục Đọc lốp, xe chưa khai trục:** nộp phiếu thì báo lỗi, nhưng mục hiện hộp "More info needed" cho người kiểm khai trục ngay trong phiếu, Done xong tự sinh lốp (`Chạy`). Bản trước ghi là chặn cứng, lái xe không tự sửa được: sai.
- **Mục Đọc lốp, xe thiếu lốp:** hộp "Install Missing Tires" lắp ngay trong phiếu, không hỏi gì thêm (`Chạy`).
- **Mooc chưa gán biểu mẫu:** "No inspection forms exist yet" dù tài khoản có biểu mẫu; câu chữ gây hiểu nhầm (`Chạy`).
- **Tài khoản chưa có phân loại** khi gán biểu mẫu: chưa thử.
- **Lệch múi giờ thiết bị và tài khoản:** số đồng hồ bị chặn sai, mục Date/Time lệch 13 giờ, không báo (`Chạy`).

## 7. Validation, Limits & Wording

### 7.1 Validation rules

| Field | Rule | Bằng chứng |
|---|---|---|
| Nhắc | Bắt buộc xe, đầu việc; có ít nhất một trục | `Chạy` |
| Ngưỡng nhắc | Nhỏ hơn chu kỳ; bằng cũng bị chặn; so đúng khi khác đơn vị | `Chạy` |
| Ngày hoãn | Không chặn ngày đã qua; không có ô lý do | `Chạy` |
| Mục Không đạt | Bắt ghi chú nếu cấu hình; lớp ghi chú chỉ lưu khi gõ vào ô Comment | `Chạy` |
| Mục Đạt | Một số mục bắt ghi chú | `Chạy` |
| Xác nhận cuối | Phải tick ở biểu mẫu có ô này; không có trong kiểu Signature mặc định | `Chạy` |
| Số đồng hồ | Phải khớp lịch sử theo thời điểm, hoặc Void | `Chạy` |
| Hoàn thành lệnh | Bắt Started At, số đồng hồ, theo Cài đặt tài khoản | `Chạy` |
| Giấy tờ | Bắt buộc xe, loại, ngày đến hạn; mỗi xe một nhắc cho mỗi loại | `Chạy` |
| Resolve with Note | Note bắt buộc | `Chạy` |
| Acknowledge | Comments không bắt buộc | `Chạy` |

### 7.2 Limits & Quotas (exact values)

| Tham số | Giá trị | Window | Behavior khi vượt |
|---|---|---|---|
| Thông báo nhắc | Fleetio: 7 giờ sáng khi đến hạn, sau đó mỗi tuần | Đến khi xử lý | Theo cài đặt thông báo của từng người (`Xem`) |
| Ngưỡng nhắc mặc định | Fleetio: 2 tuần, 500 km | Mỗi nhắc | Sửa được (`Chạy`) |
| Ngưỡng gia hạn mặc định | Fleetio: xe 3 tuần, liên hệ 4 tuần | Mỗi nhắc | Sửa được (`Chạy`) |
| Hạn mức xe gói dùng thử | Fleetio: 5 xe, xe Sample không tính | Tài khoản | "Your plan is limited to 5 vehicles" (`Chạy`) |
| Mục Meter Entry | Fleetio: 1 mỗi biểu mẫu | Biểu mẫu | Panel khoá (`Chạy`) |
| Hoãn mặc định | Fleetio: +7 ngày | Mỗi lần hoãn | Chỉnh tự do (`Chạy`) |

### 7.3 Wording samples (exact strings)

#### Error messages

| Tình huống | Wording | Code |
|---|---|---|
| Mục lỗi thiếu ghi chú | "must contain a remark on failure" | E-001 |
| Mục Đạt thiếu ghi chú | "must contain a remark on pass" | E-002 |
| Thiếu giá trị | "is required" | E-003 |
| Chưa có cấu hình trục | "Please select axle configuration before submitting the form" | E-004 |
| Chưa tick xác nhận | "This must be checked if there are no defects." | E-005 |
| Nộp phiếu lỗi | "Could not submit inspection form. Please fix any errors and try again." | E-006 |
| Nhắc thiếu chu kỳ | "Please provide a usage or a time interval" | E-008 |
| Ngưỡng ≥ chu kỳ | "Primary Meter Due Soon Threshold is too high (can't be equal to or greater than Primary Meter Interval)" | E-009 |
| Đồng hồ trái lịch sử | "must be less than 2,499 or marked as void" | E-013 |
| Thiếu số đồng hồ của mục | "requires a Odometer" | E-015 |

Mã đầy đủ có tiền tố `E-fleetio-reminders-inspection-`.

#### Info / neutral messages

| Tình huống | Wording |
|---|---|
| Không lấy được vị trí | "Fleetio was unable to detect your location from your web browser. Location data will not be saved on this inspection." |
| Tạm hoãn | "1 service reminder will be snoozed until the selected date and time. The reminder will return to its normal state after the snooze period is over." |
| Hoãn xong, kể cả ngày đã qua | "The Service Reminder was successfully updated." |
| Gán bộ lịch | "1 Vehicle will receive 2 Service Reminders based on the intervals below. Any conflicting individual Service Reminders will be replaced by the schedule from the Service Program." |
| Gỡ xe khỏi bộ lịch | "This will remove all service reminders on the vehicle from this service program." |
| Nộp phiếu | "Inspection form submitted." |
| Ghi nhận lỗi | "Successfully acknowledged failed inspection item." |

## 8. Assumptions

- `GĐ` Lái xe làm phiếu trên Delta Super App, có quyền camera và vị trí.
- `GĐ` GPS trên điện thoại đủ chính xác để phát hiện đứng yên một chỗ; xe tải, bãi lớn cần kiểm chứng.
- `GĐ` Fleetio Go có cùng luật phiếu với web. Phần xác nhận lại và vị trí từng mục có thể khác, xem Mục 14.

## 9. Risks

| Rủi ro | Mức | Giảm thiểu |
|---|---|---|
| Lái xe kiểm khống, tick nhanh cho xong | Cao | Vị trí, thời lượng, bắt ảnh ở mục quan trọng |
| Toạ độ gửi từ thiết bị bị giả, hệ thống tin hoàn toàn | Cao | Đối chiếu với GPS xe, chuyến đang chạy |
| Thêm phiếu làm chậm giờ xuất bến | Cao | Biểu mẫu ngắn, chỉ mục an toàn |
| Sửa chu kỳ, hoãn, ghi nhận lỗi không để lại lý do | Cao | Bắt lý do, ghi lịch sử |
| Quá nhiều thông báo khiến người dùng bỏ qua | Trung | Hồ sơ thông báo theo vai trò |
| Bắt buộc số km làm dữ liệu rác nếu nhập vội | Trung | Lấy từ GPS, nhập tay chỉ khi thiếu |
| Mooc không đồng hồ vướng luật bắt số đồng hồ khi xong lệnh | Trung | Tắt theo loại phương tiện; chưa kiểm được ở Fleetio |

## 10. Success Criteria (preliminary)

- Không có xe quá hạn giấy tờ mà không ai biết.
- Tỷ lệ nhắc xử lý đúng hạn đo được.
- Mục lỗi kiểm tra đều có sự cố hoặc ghi nhận kèm lý do, không có mục bỏ quên.

## 11. Open Questions

| ID | Câu hỏi | Nguồn khách |
|---|---|---|
| OQ-1 | Delta có yêu cầu kiểm tra xe trước chuyến không? Ai kiểm, bao lâu một lần? | Chưa có trong tài liệu khách gửi |
| OQ-2 | Chu kỳ bảo dưỡng của Delta theo km, theo tháng hay cả hai, theo từng dòng xe? | Chưa có trong tài liệu khách gửi |
| OQ-3 | Giấy tờ nào cần nhắc: đăng kiểm, bảo hiểm, bằng lái, phù hiệu? Báo trước bao lâu? | Chưa có trong tài liệu khách gửi |
| OQ-4 | Phiếu kiểm hỏng có cho xe chạy tiếp không, ai quyết? | Chưa có trong tài liệu khách gửi |
| OQ-5 | Mooc, máy phát có lịch riêng theo giờ chạy không? Liên quan `vehicle-management` OQ-4 | Đề xuất tiện ích GPS (25/9/2025), mục 3 |
| OQ-6 | Làm sớm hơn mốc thì Delta chấp nhận mất phần còn lại của chu kỳ, hay hợp đồng bảo dưỡng theo km đòi giữ mốc cũ? | Chưa có trong tài liệu khách gửi |

## 12. Next Steps

- Hỏi Delta OQ-1 trước khi quyết định lập feature kiểm tra xe.
- Khi đến lượt `/brainstorm reminders`, dùng Mục 4 và Mục 13 làm danh sách gợi ý.
- Mở lại lịch Daily trên `TEST-NHAC-PHIEU` sau một ngày để thấy Due Soon, Overdue, Skipped.
- Nếu được phép lưu trữ xe TEST không dùng: chạy mooc không đồng hồ, xe giờ máy, đồng hồ phụ, phiếu riêng đầu kéo và mooc.

## 13. Giải pháp đáng học và điểm yếu

### Đáng học

- **Trạng thái đổi ngay khi lưu số, theo trục xấu nhất:** không cần chờ job, hợp với số km GPS về liên tục.
- **Bảng đối chiếu khi gán bộ lịch** (Conflicting, Duplicate, New Interval): cho đầu kéo cùng dòng xe, thấy trước hệ quả rồi mới áp.
- **Resolve gom mọi nhắc của xe vào một lệnh:** vào xưởng làm luôn nhiều việc, giảm số lần dừng xe.
- **Lỗi lặp gộp vào sự cố đang mở nhưng vẫn giữ dòng lỗi và dòng thời gian:** tránh một lốp hỏng sinh hàng chục sự cố khi nhiều lái kiểm cùng đầu kéo hoặc mooc.
- **Phiên bản biểu mẫu "Past Version":** phiếu cũ không đổi khi sửa mẫu, cần cho kiểm toán và tranh chấp.
- **Đóng dấu Job vào phiếu kiểm:** liên kết kiểm trước chuyến với chuyến đang chạy, rất hợp Lệnh vận tải.
- **Khai trục và lắp lốp thiếu ngay trong phiếu:** phát hiện thiếu dữ liệu lúc kiểm, không bắt quay lại màn quản trị.
- **KPI đếm theo xe:** nói đúng câu hỏi điều phối.

### Điểm yếu, đề xuất Invlogis tách riêng

- **Nhắc mới chưa có lịch sử tính mốc từ 0:** đầu kéo đã chạy nhiều vừa khai báo là Overdue ngay. Đề xuất Invlogis: mặc định tính từ số hiện tại.
- **Đổi chu kỳ xoá trắng quá hạn, Acknowledge không cần lý do, Snooze không có lý do, ngày hoãn đã qua vẫn báo thành công:** lỗ hổng kiểm soát. Đề xuất Invlogis: bắt lý do, ghi lịch sử, chặn ngày đã qua.
- **Làm sớm mất phần còn lại của chu kỳ:** tốt cho an toàn, nhưng cần cân nhắc với hợp đồng bảo dưỡng theo km (OQ-6).
- **Gia hạn không có lịch sử, không có nút gia hạn:** giấy tờ đầu kéo, mooc, đăng kiểm cần giữ chứng từ qua từng kỳ. Đề xuất Invlogis: mỗi kỳ gia hạn là một bản ghi có chứng từ.
- **Lẫn giờ thiết bị và giờ tài khoản:** chặn sai số đồng hồ, lệch giờ mục Date/Time 13 giờ. Delta chỉ một múi giờ nhưng SaaS đa khách phải chốt một nguồn giờ.
- **Bắt số đồng hồ khi xong lệnh là cấu hình tài khoản:** mooc không đồng hồ sẽ vướng (`Suy`, chưa kiểm được vì không tạo được xe). Đề xuất Invlogis: cấu hình theo loại phương tiện.
- **Workflow không có action tạo lệnh:** muốn tự tạo lệnh phải qua Automations.
- **Rule, bộ lịch chạy ngầm, không có dấu hiệu rõ ở màn đang mở;** biểu mẫu chưa gán xe chỉ hiện danh sách rỗng.
- **Mở Edit rồi lưu làm Notifications từ Inactive thành Active:** đổi cài đặt mà người dùng không đụng tới.
- **Không có nháp phiếu, rời trang là mất:** đề xuất Invlogis cho lưu nháp trên app vì sóng ở bãi yếu.
- **Sự cố từ phiếu lốp không có trường vị trí lốp, mô tả có thể thiếu lỗi:** đề xuất Invlogis gắn vị trí thành dữ liệu.
- **Máy chủ tin toạ độ gửi lên, không so giữa các phiếu:** chống kiểm khống trên web không có tác dụng.

## 14. Câu hỏi đã có câu trả lời từ chạy thử

Mã theo [[docs/_research/fleetio/srs/fleetio-reminders-inspection-spec.md|SRS]] Mục 12.

| Mã SRS | Câu hỏi | Trả lời | Mức |
|---|---|---|---|
| OQ-8 | Lỗi lại khi sự cố còn mở thì trùng hay gộp? | Gộp vào sự cố đang mở, thêm mốc thời gian, mỗi lần lỗi vẫn là một dòng Item Failures; không báo cho người kiểm khi đang làm phiếu | `Chạy` |
| OQ-7 | Phiếu không vị trí có bị đánh dấu không? | Một phần: phiếu không vị trí vẫn nộp được; toạ độ giả không bị chặn; mọi phiếu web thử đều `location_exception` false; Fleetio Go chưa kiểm | `Chạy (vị trí giả lập)` |
| — | Có câu hỏi xác nhận lại sau khi sự cố Resolved không? | Trên web không thấy, lỗi lại thì sinh sự cố mới. Tài liệu hãng ghi có xác nhận; có thể chỉ ở Fleetio Go, chưa kiểm được | `Chạy`, `Docs` |
