---
type: research
keyword: "Fleetio: cấu hình trục, lắp, đảo, tháo, đọc lốp, lốp đầu kéo và lốp mooc"
status: draft
updated: 2026-11-03
links:
  - docs/_research/fleetio/run-notes/tires.md
  - docs/_research/fleetio/run-notes/vehicle.md
  - docs/_research/fleetio/run-notes/reminders-inspection.md
  - docs/vehicle-management/brainstorms/vehicle-management.md
  - design-system/components/application/tyre-layout.md
  - design-system/foundations/vehicle.md
  - docs/_product/saas-core-vs-tenant.md
---

# Giải pháp tham khảo: Quản lý lốp

> Khuyến nghị: **Học thao tác, không học mô hình dữ liệu.** Fleetio lắp nhanh, đảo gọn, đọc gai rõ, nhưng không có đối tượng "quả lốp": lốp là dữ liệu của một vị trí trên một xe. Nhu cầu Delta (serial, kho, lệnh sửa chữa, phân bổ chi phí, mooc đi theo đầu kéo) cần mô hình khác, trình bày riêng ở Phụ lục A.

**Nhãn bằng chứng:** `Chạy` đã thao tác và thấy kết quả · `Chạy một phần` mới đi được một đoạn · `Xem` thấy trên giao diện · `Docs` tài liệu hãng · `Suy` rút từ số liệu, chưa tách riêng để chứng minh · `GĐ` giả định · `Không chạy` chưa thử, có nêu lý do.

## 1. Idea Seed

Mỗi xe và mỗi mooc có sơ đồ trục riêng. Người dùng khai cấu hình trục, bấm vào ô để lắp, đọc gai và áp suất ngay trên dòng, đảo theo sơ đồ khép kín, tháo là ô trở lại trống. Lịch sử sống ở Tire Activity, số đọc mới nhất ở Tire Readings. Lái xe đọc lốp qua phiếu kiểm tra, phiếu không đạt thì thành sự cố.

### 1.1 Trả lời trực tiếp: mỗi trạng thái lốp đi thế nào

Fleetio chỉ có 3 trạng thái thật: **vị trí trống, có lốp, Spare**. "Đã tháo" chỉ còn là dòng lịch sử. Không có trạng thái trong kho, chờ xử lý, đi đắp hay phế.

| Trạng thái | Làm được gì | Sang đâu |
|---|---|---|
| Xe chưa khai trục | Set up ở tab Tire Management, hoặc chọn cấu hình ngay trong phiếu kiểm | Có trục, mọi ô trống. Khai trong phiếu thì tự sinh lốp cho mọi ô |
| Vị trí trống | Bấm ô +, Add, chip trục, Copy details, Install Tires trong phiếu kiểm, làm đích khi đảo | Có lốp |
| Có lốp | Sửa gai, áp suất, thông số; đọc qua phiếu; đảo; Undo ngay sau đảo; Remove, Remove All | Giữ nguyên, sang vị trí khác cùng xe, hoặc về trống |
| Spare | Add chọn "Spare Tire"; sửa, đọc tay | Giữ nguyên. Không đảo được, không có trong phiếu kiểm, không có ô trên sơ đồ |
| Đã tháo | Chỉ xem dòng `Removal` ở Tire Activity | Không có nút lắp lại. Muốn dùng lại phải lắp mới, gõ lại mã lốp, số km về 0 nếu không nhập tay |

**Tháo xong lốp đi đâu: không đi đâu cả.** Bảng đủ từng ô: [[docs/_research/fleetio/srs/fleetio-tires-states.md|States]].

### 1.2 Trả lời trực tiếp: gắn lốp theo đầu kéo ra sao

1. Tạo xe loại Semi Truck. Form tạo xe không có trục.
2. Tab Tire Management, khai 6x4 (10 vị trí + Spare) hoặc 4x2 RWD (Dually) (6 vị trí + Spare).
3. Bấm ô + hoặc chip trục để lắp, mỗi trục có vai trò Steer, Drive, Dead, Lifted, Tag, Pusher, Other.
4. Số km lốp tự tăng theo đồng hồ của chính đầu kéo.
5. Tab lốp của đầu kéo chỉ có lốp của đầu kéo, kể cả khi đã liên kết mooc.

### 1.3 Trả lời trực tiếp: gắn lốp theo mooc ra sao

1. Mooc là một Vehicle riêng, loại Trailer, có đồng hồ riêng, lốp riêng, lịch sử riêng. Không có "tổ hợp".
2. Asset Type chọn Trailer thì chỉ còn 7 cấu hình: Single, Tandem, Tri-Axle, Multi-Axle theo 2 hoặc 4 lốp mỗi trục. Tri-Axle 4 lốp mỗi trục là 12 ô + Spare. Vai trò trục: Trailer, Dead, Lifted, Other.
3. Lắp như đầu kéo, nhưng Rotation Pattern báo "No options": không có mẫu đảo chuẩn cho mooc, phải tự ghép.
4. Số km lốp mooc tính theo **đồng hồ của mooc**, không theo đầu kéo. Không bỏ được đồng hồ (chỉ có Miles, Kilometers, Hours). Đã chạy: đầu kéo tăng lên 20.500 km, mooc vẫn 3.500 km. Lắp khi mooc chưa có số đồng hồ nào trước ngày lắp thì số km lốp đứng ở "—".
5. Liên kết mooc qua trường Linked Vehicles: hai chiều, chỉ là đường dẫn. Gỡ hoặc gắn lại không đổi lốp, không đổi đồng hồ, không có lịch sử ghép, không có ngày.
6. Đổi lốp giữa đầu kéo và mooc, hai đầu kéo, hai mooc: **không có thao tác**. Tháo bên A, lắp mới bên B, gõ lại mã lốp, gai, áp suất, số km; hai lịch sử không nối nhau (cơ chế `Chạy` trên một xe, giữa hai xe là `Suy` vì tài khoản đã chạm trần số xe).

## 2. Context

**Feature Invlogis liên quan:** `vehicle-management` (sơ đồ lốp), `repair-order` (thay lốp theo lệnh), `stock-movement` (lốp theo serial), kiểm tra xe (đề xuất mới), `transport-dispatch` (tổ hợp đầu kéo, mooc, container).

**Nguồn và bằng chứng:** chạy thật ngày 03/11/2026 trên `TEST-XE-LOP` (đầu kéo) và `TEST-MOOC-LOP` (mooc), `TEST-XE-01` cho phiếu kiểm. Không tạo được xe thứ ba trở đi vì tài khoản đã chạm trần. Chi tiết: [[docs/_research/fleetio/run-notes/tires.md|ghi chú lốp]], [[docs/_research/fleetio/run-notes/vehicle.md|ghi chú phương tiện]].

## 3. User Types (preliminary)

| User Type | Pain Point | Primary Need |
|---|---|---|
| Kỹ thuật, xưởng | Lắp 10 đến 12 lốp mỗi xe mất thời gian | Lắp theo trục, điền sẵn vị trí |
| Quản lý phương tiện | Không biết lốp nào sắp mòn | Danh sách đọc mới nhất, có mức sức khoẻ |
| Lái xe | Kiểm lốp trước chuyến | Phiếu tự sinh ô theo xe |
| Kế toán | Cần chi phí từng lốp | Fleetio không đáp ứng, xem Phụ lục A |

### 3.1 Tác vụ chính

Tần suất là `GĐ`, chưa khảo sát.

| Vai trò | Tác vụ | Tần suất | Mức quan trọng | Ghi chú |
|---|---|---|---|---|
| Quản trị | Khai cấu hình trục | Khi có xe mới | Cao | Khoá khi đã có lốp |
| Kỹ thuật | Lắp, thay lốp | Mỗi tuần | Cao | Không nối lệnh sửa chữa |
| Kỹ thuật | Đảo lốp | Theo kỳ | Trung | Chỉ trong một xe |
| Lái xe | Đọc lốp qua phiếu | Theo biểu mẫu khách gán | Trung | Không có Spare |
| Quản lý phương tiện | Xem lốp cần thay | Mỗi tuần | Cao | Không có cảnh báo chủ động |

## 4. Capabilities Breakdown

### P0 — must have

- L1 [Mới] [Gói: Bảo dưỡng đội xe] **Sơ đồ theo cấu hình trục, khai riêng từng xe.** Fleetio: `Chạy`, 27 cấu hình (20 xe, 7 mooc). Áp vào `vehicle-management`.
- L2 [Mới] [Gói: Bảo dưỡng đội xe] **Lắp theo ô hoặc chip trục, nhiều lốp một lần.** Fleetio: `Chạy`. Hợp đầu kéo 10 lốp, mooc 12 lốp.
- L3 [Mới] [Gói: Bảo dưỡng đội xe] **Khoá cấu hình trục khi đã có lốp.** Fleetio: `Chạy`, tháo hết thì mở lại, lịch sử giữ nguyên.
- L4 [Mới] [Gói: Bảo dưỡng đội xe] **Lịch sử theo sự kiện từng lốp.** Fleetio: `Chạy`, gồm Installed, Tire Rotation, Tread Depth Reading, Pressure Reading, Removal, Spare Stowed. Không học phần Undo xoá dấu vết.
- L5 [Mới] [Gói: Bảo dưỡng đội xe] **Đảo là sơ đồ khép kín, cho ô trống tham gia.** Fleetio: `Chạy`.

### P1 — should have

- L6 [Mới] [Gói: Bảo dưỡng đội xe] [Cấu hình] **Ba mức gai theo mức tối thiểu của lốp.** Fleetio: `Suy` từ hai mức tối thiểu, Low khi gai ≤ Min, Warning khi Min < gai ≤ Min + 2, còn lại Normal. Khoảng đệm là tham số mới, chưa có mã.
- L7 [Mới] [Gói: Bảo dưỡng đội xe] **Phiếu kiểm tự sinh ô theo cấu hình trục, báo thiếu lốp ngay trong phiếu.** Fleetio: `Chạy`.
- L8 [Mới] [Gói: Bảo dưỡng đội xe] **Tách vai trò trục khỏi hình dạng trục.** Fleetio: `Chạy`, đổi được kể cả khi có lốp, ghi vào cột Axle Type của lịch sử.
- L9 [Mới] [Gói: Bảo dưỡng đội xe] **Danh mục mẫu lốp lấy từ phụ tùng nhóm lốp, tự điền thông số.** Fleetio: `Chạy`, chọn mẫu thì Factory, Min, Life tự điền và khoá.
- L10 [Mới] [Gói: Bảo dưỡng đội xe] **Undo ngay sau đảo.** Fleetio: `Chạy`. Nên giữ dấu vết.

### P2 — nice to have

- L11 [Mới] [Gói: Bảo dưỡng đội xe] **Mẫu đảo chuẩn và mẫu đảo tuỳ biến.** Fleetio: `Chạy` mẫu chuẩn; lưu mẫu tuỳ biến `Không chạy`. Settings có 8 mẫu chuẩn, không mẫu nào cho mooc.
- L12 [Mới] [Gói: Bảo dưỡng đội xe] **Chép thông số sang vị trí khác.** Fleetio: `Chạy`, có lỗi xoá trắng dữ liệu đích, xem Mục 6.5.
- L13 [Mới] [Gói: Bảo dưỡng đội xe] **Đọc áp suất tự động từ thiết bị.** Fleetio: `Chạy` phần đọc màn hình và `Docs`, bị khoá, chỉ 4x2 hoặc 4x4 có telematics. Không dùng được cho đầu kéo 6x4.

## 5. Core Flows (Happy Path)

### 5.1 Khai cấu hình trục, lắp lốp

1. Quản trị tạo xe, mở tab Tire Management, chọn Vehicle hoặc Trailer, chọn cấu hình.
2. Tuỳ chọn tạo phụ tùng nhóm lốp để có Tire Model.
3. Kỹ thuật bấm ô + hoặc chip trục, nhập mã lốp, gai, áp suất, mức tối thiểu. Chỉ vị trí và ngày là cần có.

```
Tạo xe ─> Khai trục ─> Lắp theo ô hoặc chip ─> Sơ đồ có gai, PSI, màu
```

### 5.2 Đọc định kỳ

1. Lái xe làm phiếu kiểm, hoặc kỹ thuật sửa trực tiếp trên dòng.
2. Phiếu không đạt thì workflow của biểu mẫu tạo sự cố. Sửa trực tiếp dưới mức chỉ đổi màu.

```
Phiếu kiểm ─┬─ Đạt ─> Ghi về Tire Readings
            └─ Không đạt ─> Ghi về Tire Readings + Sự cố
Sửa trên dòng ─> Ghi về Tire Readings, chỉ đổi màu
```

### 5.3 Đảo, thay, đổi mooc

1. Đảo: chọn mẫu hoặc tự ghép khép kín, xong có Undo tức thì, đóng rồi thì thôi.
2. Thay lốp: Remove rồi lắp mới. Không nối lệnh sửa chữa, không trừ kho, không có chi phí, không có lý do.
3. Đổi mooc: sửa Linked Vehicles. Lốp và đồng hồ đứng yên.

```
Rotate ─> Kết quả ─┬─ Undo ─> Về chỗ cũ, lịch sử sạch
                   └─ Close ─> Không còn Undo
Remove ─> Ô trống ─> Lắp mới, gõ lại mã lốp
```

## 6. System Behavior Deep Dive

### 6.1 Decision Points

| ID | Flow | Khi nào | YES | NO |
|---|---|---|---|---|
| D1 | 5.1 | Xe đã có lốp | Khoá Edit cấu hình trục | Đổi được |
| D2 | 5.1 | Chọn Tire Model | Factory, Min, Life tự điền, khoá | Nhập tay hoặc bỏ trống |
| D3 | 5.2 | Biểu mẫu có workflow "ANY Failed Inspection Item" | Tạo sự cố | Không tạo |
| D4 | 5.3 | Sơ đồ đảo khép kín | Bật Rotate Tires | Nút tắt |
| D5 | 5.3 | Tick lưu mẫu tuỳ biến mà trống tên | Báo lỗi, không đảo | Đảo |
| D6 | 5.1 | Có số đồng hồ trước ngày lắp | Số km lốp tính được | Đứng ở "—" |

### 6.2 Scenario Matrix

| From State | To State | Rule | Action | Result | Bằng chứng |
|---|---|---|---|---|---|
| Min 4, gai 3.9 hoặc 4.0 | Low | Gai ≤ Min | Đọc | Đỏ | `Chạy` |
| Min 4, gai 4.5, 5, 6.0 | Warning | Min < gai ≤ Min + 2 | Đọc | Vàng | `Chạy` |
| Min 4, gai 6.1, 6.9, 7, 8 | Normal | Còn lại | Đọc | Xám | `Chạy` |
| Min 8, gai 9, 10 | Warning | Như trên | Đọc | Vàng | `Chạy` |
| Min 8, gai 10.5, 11, 12 | Normal | Như trên | Đọc | Xám | `Chạy` |
| Form Min 5, áp 80 đến 120 | Pass | Biên tính là đạt | Nộp phiếu | 5 Pass, 4.9 Fail; 80 Pass, 79.9 Fail; 120 Pass, 120.1 Fail | `Chạy` |
| Gai 5, form Min 5, lốp Min 8 | Pass và Low | Hai mức tách rời | Nộp phiếu | Phiếu Pass, Tire Readings Low | `Chạy` |

Ma trận đầy đủ: [[docs/_research/fleetio/srs/fleetio-tires-spec.md|Spec]] Mục 13.

### 6.3 State Transitions

Xem Mục 1.1 và [[docs/_research/fleetio/srs/fleetio-tires-states.md|States]].

### 6.4 Interrupted Transactions

| Tình huống | Hệ thống còn lại gì | Resume | Cleanup |
|---|---|---|---|
| Đóng màn kết quả đảo | Lốp ở vị trí mới, có dòng Tire Rotation | Không còn Undo | Đảo ngược lại bằng một lần đảo mới |
| Undo ngay sau đảo | Lốp về chỗ cũ, quay lại form, mapping còn nguyên | Đảo lại được | Tire Activity không còn dấu vết lần đảo |
| Khai trục trong phiếu rồi không nộp | Chưa thử | Chưa rõ | `Không chạy` |

### 6.5 Other Edge Cases

- **Mã lốp không phải định danh:** lắp 4 lốp một lần thì cả 4 chung một mã, trùng vị trí khác không cảnh báo (`Chạy`).
- **Copy details xoá dữ liệu đích:** chỉ tick mã lốp, chép sang 1LI và 1LO thì Factory 16 và Life 100.000 của đích bị xoá trắng. Lặp lại hai lần đều vậy (`Chạy`).
- **Undo xoá dấu vết:** không biết đã từng đảo (`Chạy`).
- **Số km lốp mooc im lặng:** lắp khi chưa có số đồng hồ trước ngày lắp thì đứng "—", hộp Edit và Rotate hiện 0 (`Chạy`).
- **Hai mức tối thiểu tách rời:** phiếu Pass nhưng Tire Readings Low với cùng số đọc (`Chạy`).
- **Sự cố không có trường vị trí:** vị trí chỉ nằm trong chữ mô tả; mô tả có lúc thiếu lỗi: 2LI áp 120.1 có dấu X ở phiếu nhưng mô tả không nhắc (`Chạy`).
- **Dưới mức khi sửa trực tiếp:** chỉ đổi màu, không sự cố, không thông báo (`Chạy`).
- **Lốp đã tháo biến khỏi Tire Readings,** chỉ còn ở Tire Activity (`Chạy`).
- **Đơn vị cố định:** gai /32 in, áp suất PSI dù xe đặt Metric; không thấy chỗ đổi (`Chạy`).
- **Không có cách đọc nhiều lốp trên màn lốp:** Copy details không chép gai, áp suất; cách duy nhất là phiếu kiểm (`Chạy`).
- **Không vào chi phí, không trừ kho:** phụ tùng giá 3.000.000 ₫ lắp bằng Tire Model không sinh Inventory Activity, Total Costs của xe không đổi theo giá lốp (`Chạy`).

## 7. Validation, Limits & Wording

### 7.1 Validation rules

| Field | Rule | Bằng chứng |
|---|---|---|
| Vị trí | Chỉ vị trí trống; ô có lốp xám, chip trục đầy biến mất | `Chạy` |
| Mã lốp, gai, áp suất | Không bắt buộc; sơ đồ hiện "–/32"", dòng "Unknown Tire" | `Chạy` |
| Ngày lắp | Cho lùi ngày | `Chạy` |
| Số thập phân | Lịch sử giữ 12.5; ô nhập làm tròn 13; 4.5 trên sơ đồ hiện 5/32"; 79.9 PSI hiện 79PSI ở bảng | `Chạy` |
| Mẫu đảo mới | Bắt buộc tên khi tick lưu | `Chạy` |
| Multi-Axle | Number of Axles từ 2 đến 10 | `Chạy` |

### 7.2 Limits & Quotas (exact values)

| Tham số | Giá trị | Window | Behavior khi vượt |
|---|---|---|---|
| Cấu hình trục | 27 dòng, không tự tạo | Cố định | Không có lựa chọn |
| Wheel Positions của trình hướng dẫn | 4, 6, 8, 10 | Cố định | 12x4, 12x6 chỉ có ở danh sách "I know" |
| Số xe của gói dùng thử | Fleetio: 5 xe không tính xe mẫu | Theo gói | Không lưu được xe |

### 7.3 Wording samples (exact strings)

#### Error messages

| Tình huống | Wording | Code |
|---|---|---|
| Nộp phiếu chưa khai trục | "Please select axle configuration before submitting the form" | E-fleetio-tires-001 |
| Sửa cấu hình khi có lốp | "Axle Configuration cannot be edited for this Vehicle because it has installed Tires" | E-fleetio-tires-002 |
| Tick lưu mẫu trống tên | "Could not rotate tires.", "can't be blank" | E-fleetio-tires-004 |
| Phiếu Fail chưa nhận xét | "must contain a remark on failure" | E-fleetio-tires-005 |

#### Success messages

| Tình huống | Wording |
|---|---|
| Khai trục | "Vehicle's Axle Configuration successfully updated" |
| Lắp | "4 tires were installed on this vehicle." |
| Lắp Spare | "1 spare tire was installed on this vehicle." |
| Sửa | "Tire updated successfully." |
| Đảo | "Successfully Rotated 2 tires" |
| Tháo | "1 tire was removed from this asset." |
| Chép | "Details copied to 2 tire positions." |

## 8. Assumptions

- Mô hình vị trí của Fleetio chỉ hợp đội xe không quản lý lốp theo serial (`Suy`).
- Thao tác lắp, đảo, đọc của Fleetio dùng lại được trên nền mô hình quả lốp độc lập (`GĐ`).

## 9. Risks

| Rủi ro | Mức | Giảm thiểu |
|---|---|---|
| Chép màn Fleetio làm mất serial, kho, chi phí | Cao | Lấy mô hình theo Phụ lục A, chỉ học thao tác |
| Số km lốp mooc sai vì mooc không có đồng hồ | Cao | Tính theo tổ hợp, xem DX-03 |
| Hai mức tối thiểu gây tranh cãi | Trung | Một nguồn mức tối thiểu |
| Mở rộng sang đi đắp, trả về kho trước khi Delta chốt | Trung | Hỏi Delta trước, OQ-5 |

## 10. Success Criteria (preliminary)

- Truy được một lốp theo serial qua mọi xe, mọi lần lắp.
- Số km lốp mooc khớp quãng đường của các tổ hợp đã ghép.
- Mọi lần tháo có lý do và đích đến.

## 11. Open Questions

| ID | Câu hỏi | Nguồn khách |
|---|---|---|
| OQ-1 | Quy luật mức tối thiểu tự hiện 4/32" khi để trống ở một số lốp, và ngưỡng mặc định khi không có Min, là gì? | Không áp dụng |
| OQ-2 | Số 3.502 km trên mooc từ đâu ra, khi số nhập cuối là 3.500? | Không áp dụng |
| OQ-3 | Hình 6x2, 8x4, 10x, 12x của Fleetio có khớp `truck-6x2`, `truck-8x4`, `truck-5ax` không? | Không áp dụng |
| OQ-4 | Delta có đo gai định kỳ không, hay chỉ quản lý vị trí và serial? | File sơ đồ lốp của Delta |
| OQ-5 | Lốp tháo ra có những đích nào: kho, xưởng, rác thải, đi đắp, chuyển xe khác? | Phân hệ FIAM (25/10/2026), mục Chốt chặn Sơ đồ lốp và Bình ắc quy |
| OQ-6 | Số km lốp mooc tính theo GPS đầu kéo trong thời gian ghép có được Delta chấp nhận không? | Chưa có trong tài liệu khách gửi |

## 12. Next Steps

- Đối chiếu Phụ lục A với `docs/vehicle-management/brainstorms/vehicle-management.md` và `repair-order`, chỉ đưa ý chưa có.
- Hỏi Delta OQ-4, OQ-5, OQ-6 khi chi tiết hoá sơ đồ lốp.
- Bộ SRS: [[docs/_research/fleetio/srs/fleetio-tires-spec.md|Spec]].

## Phụ lục A. So với nhu cầu Delta và đề xuất Invlogis

> Phần này **không mô tả Fleetio.** Là đề xuất để cân nhắc, chưa chốt với Delta. Tầng đề xuất theo `docs/_product/saas-core-vs-tenant.md`.

### A.1 Fleetio so với nhu cầu Delta

Nguồn phía Delta: `design-system/components/application/tyre-layout.md`, `design-system/foundations/vehicle.md`, `design/_lab/tyre-mapping.html`, SRS cũ UC03.05 và UC05.06.05, `docs-input/sop/fiam-ke-toan-quan-tri/fiam-ke-toan-quan-tri.md`. File xlsx sơ đồ lốp gốc không có trong `docs-input`, chỉ có bản dựng lại ở lab.

| Yêu cầu Delta | Fleetio | Đáp ứng |
|---|---|---|
| `tractor-6x4` 10 + 1 | 6x4 + Spare | Có, `Chạy` |
| `tractor-4x2` 6 + 1 | 4x2 RWD (Dually) + Spare | Có, `Chạy`; Spare chưa thử riêng trên cấu hình này |
| `trailer-2ax` 8 + 1, `trailer-3ax` 12 + 1 | Tandem, Tri-Axle 4 lốp mỗi trục + Spare | 3 giàn `Chạy`, 2 giàn theo danh sách |
| `truck-4x2`, `truck-6x4` | Cùng cấu hình trên | Có |
| `truck-6x2` 8 + 1 | 6x2 có trong danh sách, chưa xem hình | Chưa kiểm |
| `truck-8x4` 12 + 1, `truck-5ax` 16 + 1 | 8x4, 10x có trong danh sách, chưa xem hình | Chưa kiểm |
| `forklift-diesel` 4 | 4x2 thường | Có về số lốp, theo danh sách |
| `forklift-elec` 3 lốp | Không có cấu hình 3 lốp | Không |
| Container, máy phát: không lốp | Xe để chưa khai trục | Được, không có loại riêng |
| Tổ hợp đầu kéo + mooc + container | Chỉ Linked Vehicles, không vẽ chung | Không |
| Số thứ tự vị trí theo file, bên lái, bên phụ | Mã 2LO, 2RI, không đổi tên, không đánh số | Không |
| Warning: đến hạn km, ngày, mòn | Chỉ theo gai. Life Expectancy không tạo cảnh báo nào trong các case đã chạy | Một phần |
| Error: hỏng, cần thay | Không có trạng thái hỏng trên vị trí | Không |
| Serial từng lốp; Tháo ra, Lắp vào, Đổi vị trí, Thay thế theo lệnh sửa chữa | Mã lốp không duy nhất, tách khỏi lệnh | Không |
| Ngày lắp lấy theo ngày chốt lệnh | Nhập tay | Không |
| Chốt lệnh cập nhật tồn kho, tồn xưởng, rác thải | Không trừ kho, không có đích tháo | Không |
| Thẻ phân bổ `LOP_BiểnSố_Series`, kèm series, vị trí, km lúc lắp | Không chi phí, không thẻ | Không |
| Chặn tạo lệnh sửa chữa khi sơ đồ lốp trống | Không chặn, chỉ nhắc trong phiếu kiểm | Không |
| Danh mục lốp có đề xuất, phê duyệt | Phụ tùng không qua duyệt | Không |

### A.2 Đề xuất Invlogis

| Mã | Đề xuất | Tầng đề xuất | Học từ Fleetio hay khác |
|---|---|---|---|
| DX-01 | **Quả lốp là đối tượng độc lập,** định danh bằng serial duy nhất; nhóm Lốp trong `P-nhom-hang` (Delta: bắt buộc serial) đã có cờ này | [Gói: Bảo dưỡng đội xe] | Khác: Fleetio không có |
| DX-02 | **Mỗi lần lắp là một đoạn:** lốp, xe, vị trí, từ ngày và km, đến ngày và km, lệnh sửa chữa. Số km lốp là tổng các đoạn. Chuyển xe là đóng đoạn cũ, mở đoạn mới, lịch sử không đứt | [Gói: Bảo dưỡng đội xe] | Khác |
| DX-03 | **Lốp mooc lấy km theo tổ hợp:** tổ hợp là 1 đầu kéo + 0 hoặc 1 mooc + 0–2 container, một Lệnh gắn một tổ hợp (DEC-267). Km lốp mooc = km đầu kéo trong thời gian mooc nằm trong tổ hợp, mooc không cần đồng hồ riêng. Container không có lốp | [Lõi] phần tổ hợp · [Gói: Bảo dưỡng đội xe] phần tính km | Khác: Fleetio bắt nhập đồng hồ mooc |
| DX-04 | **Xem chung sơ đồ tổ hợp:** từ Lệnh hoặc xe thấy cả lốp đầu kéo và mooc đang ghép, dùng `Tyre Layout`. Ghép mooc không trộn lốp hai xe về mặt dữ liệu | [Gói: Bảo dưỡng đội xe] | Khác |
| DX-05 | **Vòng đời lốp:** Trong kho, Đang lắp, Dự phòng trên xe, Tồn xưởng, Rác thải; đi đắp chờ OQ-5 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Khác |
| DX-06 | **Tháo bắt buộc lý do và đích đến.** Danh sách lý do là tham số mới, chưa có mã | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Khác |
| DX-07 | **Thay lốp đi qua lệnh sửa chữa:** chốt lệnh thì đổi vị trí, ngày lắp theo ngày chốt, cập nhật tồn kho, tồn xưởng, rác thải | [Gói: Bảo dưỡng đội xe] | Khác |
| DX-08 | **Chi phí và phân bổ từng lốp:** thẻ phân bổ theo xe và series; kỳ phân bổ là tham số mới, chưa có mã (Delta: 36 tháng) | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Khác |
| DX-09 | **Lắp nhanh theo ô và trục, phiếu tự sinh ô, đảo khép kín:** giữ nguyên cách Fleetio làm, thêm Spare vào đảo và phiếu; thêm đảo giữa hai xe bằng phiếu chuyển | [Gói: Bảo dưỡng đội xe] | Học, mở rộng |
| DX-10 | **Một nguồn mức tối thiểu:** mức theo mẫu lốp, phiếu kiểm dùng lại. Khoảng đệm Warning, đơn vị mm hoặc /32 in, bar hoặc PSI là tham số mới, chưa có mã | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Học, sửa điểm yếu |
| DX-11 | **Dưới mức tạo việc ở mọi đường đọc,** sự cố có trường vị trí và số serial, thống kê được theo vị trí, theo mẫu lốp | [Gói: Bảo dưỡng đội xe] | Sửa điểm yếu |
| DX-12 | **Trạng thái trên vị trí:** Warning theo km, ngày, mòn; Error hỏng, cần thay; có báo hỏng từ app lái xe, đúng biến thể `Tyre Slot` đã có | [Gói: Bảo dưỡng đội xe] | Khác |
| DX-13 | **Mẫu sơ đồ theo nhóm hình dùng chung, đổi riêng từng dòng xe:** 11 sơ đồ, kể cả xe nâng 3 lốp; số thứ tự vị trí, bên lái, bên phụ. Bảng gán tên xe là dữ liệu của khách | [Lõi] phần sơ đồ · [Riêng Delta] phần bảng gán | Khác |
| DX-14 | **Chặn tạo lệnh sửa chữa khi sơ đồ lốp trống:** bật tắt theo khách, tham số mới, chưa có mã | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Khác |
| DX-15 | **Danh mục lốp qua đề xuất, phê duyệt:** bật tắt theo khách, tham số mới, chưa có mã | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Khác |
| DX-16 | **Không học:** Undo xoá dấu vết, Copy details xoá trắng đích, mã lốp trùng không báo, đồng hồ bắt buộc cho mooc | Không áp dụng | Tránh |
