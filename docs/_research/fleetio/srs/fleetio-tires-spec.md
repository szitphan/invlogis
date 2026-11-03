---
type: research
feature: fleetio-tires
status: draft
updated: 2026-11-03
links:
  - docs/_research/fleetio/fleetio-tires.md
  - docs/_research/fleetio/run-notes/tires.md
  - docs/vehicle-management/brainstorms/vehicle-management.md
---

# Quản lý lốp — SRS phân tích ngược từ Fleetio

> Mô tả **Fleetio đang làm gì**. Đề xuất cho Invlogis nằm riêng ở Mục 14. Chưa phải yêu cầu đã chốt với Delta.

**Nhãn bằng chứng:** `Chạy` đã thao tác · `Chạy một phần` mới đi được một đoạn · `Xem` thấy trên giao diện · `Docs` tài liệu công khai · `Suy` suy ra · `GĐ` giả định · `Không chạy` chưa thử, có lý do.

## 1. Scope

**Trong phạm vi:** Axle Configuration, Tire Management, Install Tires, Copy details, Rotate Tires, Remove Tires, Tire Activity, Tire Readings, mục Tire Readings của phiếu kiểm tra, số km lốp, Linked Vehicles ở góc nhìn lốp.

**Ngoài phạm vi:** quản lý xe, số đồng hồ nói chung, sự cố nói chung (xem bộ `fleetio-vehicle`, `fleetio-repair`, `fleetio-reminders-inspection`).

### 1.1 Trả lời trực tiếp

- **Mỗi trạng thái:** chỉ có vị trí trống, có lốp, Spare. "Đã tháo" chỉ là dòng lịch sử, không có nút lắp lại. Bảng đủ từng ô: [[docs/_research/fleetio/srs/fleetio-tires-states.md|States]].
- **Theo đầu kéo:** khai cấu hình ở tab lốp của đầu kéo, lắp theo ô hoặc chip trục, số km lốp theo đồng hồ đầu kéo. Tab đầu kéo không hiện lốp mooc đã liên kết.
- **Theo mooc:** mooc là một Vehicle riêng, 7 cấu hình riêng, đồng hồ riêng bắt buộc, không có mẫu đảo chuẩn. Liên kết với đầu kéo chỉ là đường dẫn, không truyền số km.
- **Giữa các xe:** không có thao tác chuyển lốp, phải tháo rồi lắp mới, hai lịch sử không nối.

## 2. Actors & Stakeholders

| Actor | Loại | Mục tiêu | Trong scope? | Tương đương Invlogis |
|---|---|---|---|---|
| Quản trị (Fleet Manager) | Người | Khai trục, tạo mẫu lốp, gán biểu mẫu | Có | Quản lý phương tiện |
| Kỹ thuật (Technician) | Người | Lắp, đảo, tháo, đọc | Có | Kỹ thuật xưởng |
| Lái xe (Operator) | Người | Đọc lốp qua phiếu | Có | Lái xe |
| Telematics | Ngoài | Đọc áp suất tự động, bị khoá trên tài khoản thử | Có | EUP |

## 3. Functional Requirements (FR)

Cột Tầng là đề xuất nếu Invlogis lấy chức năng này. Cột cuối chỉ ghi lấy hay không; đề xuất đầy đủ ở Mục 14.

| ID | Title | Description | Priority | Tầng | Verify by | Source | Đề xuất Invlogis |
|---|---|---|---|---|---|---|---|
| FR-fleetio-tires-001 | Khai cấu hình trục từng xe | Khai ở tab Tire Management. Form tạo xe không có trục, chỉ có trường chữ ở Specifications › Wheels & Tires. Chưa khai thì màn trống có nút "Set up axle configuration". | P0 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` | Lấy, xem DX-13 |
| FR-fleetio-tires-002 | Trình hướng dẫn | Asset Type (Vehicle, Trailer) → Wheel Positions (4, 6, 8, 10) → Axle Type. Trailer nhảy thẳng sang ô cấu hình, chỉ còn 7 dòng. | P1 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` | Lấy cách dẫn |
| FR-fleetio-tires-003 | Danh sách cấu hình | "I know my axle configuration": 27 dòng, 20 xe, 7 mooc. Không tự tạo được. | P0 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` | Thay bằng 11 sơ đồ, DX-13 |
| FR-fleetio-tires-004 | Multi-Axle | Trên mooc hiện thêm "Number of Axles *" từ 2 đến 10; tiêu đề "4 Axle". | P2 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` | Cân nhắc |
| FR-fleetio-tires-005 | Vai trò trục | Xe: Steer, Drive, Dead, Lifted, Tag, Pusher, Other. Mooc: Dead, Lifted, Trailer, Other. Đổi được cả khi có lốp, không có dòng Activity riêng, không đổi số cầu kéo, được ghi vào Axle Type của dòng lịch sử sau đó. | P1 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` | Lấy, có ghi lịch sử |
| FR-fleetio-tires-006 | Khoá cấu hình | Có lốp thì Edit khoá. Tháo hết thì mở lại, đổi được, Activity giữ nguyên. Đổi cấu hình làm mất vai trò đã đặt. | P0 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` | Lấy |
| FR-fleetio-tires-007 | Màn lốp hai cột | Trái: sơ đồ, ô trống nút +, ô có lốp hiện gai, PSI, màu. Phải: "Installed Tires" có số đếm kiểu "12 + Spare", menu Rotate Tires, Remove All và Add. | P0 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` | Lấy |
| FR-fleetio-tires-008 | Lắp nhiều lốp | Position chọn nhiều, chip All, từng trục; bấm ô + điền sẵn vị trí. Một lần lắp tạo nhiều lốp cùng thông số. | P0 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` | Lấy, nhập serial từng lốp |
| FR-fleetio-tires-009 | Trường khi lắp | Position, Install Date, Tire Meter at Installation, Current Tread Depth, Current Pressure, Tire Model, Factory Tread Depth, Minimum Tread Depth, Life Expectancy, Tire Identification Number. Không có ô tiền. | P0 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` | Lấy, thêm serial, chi phí, DX-07, DX-08 |
| FR-fleetio-tires-010 | Mẫu lốp từ phụ tùng | Tire Model lấy từ Part có category lốp; tạo xong xuất hiện ngay. Chọn mẫu thì Factory, Min, Life tự điền và khoá. Chưa có thì "No options". | P1 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` | Lấy |
| FR-fleetio-tires-011 | Spare | Add, chọn "Spare Tire". Activity `Spare Stowed`, Axle Type `N/A`, đầu mục "6 + Spare". Không có ô trên sơ đồ, chỉ có dòng ở Installed Tires. | P1 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` | Lấy, thêm vào đảo và phiếu |
| FR-fleetio-tires-012 | Copy details | Menu dòng lốp. Tick trường cần chép, chọn đích. Ô trống thì tạo lốp mới `Installed`, ngày lắp hôm nay, gai trống. Không chép gai, áp suất. Đích có lốp thì không có dòng Activity. | P2 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` | Không lấy nguyên trạng, E-009 |
| FR-fleetio-tires-013 | Đọc trên dòng, hộp Edit | Sửa gai, áp suất trên dòng lưu ngay khi rời ô, không có nút Lưu, tạo dòng đọc Method Manual. Hộp Edit thêm Current Tire Meter, Remove; sửa Model, Factory, Min, Life, mã lốp không có dòng Activity riêng. Không có ô ngày đọc. | P0 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` | Lấy, thêm ngày đọc |
| FR-fleetio-tires-014 | Đảo theo mẫu chuẩn | Rotation Pattern; "Standard 6x4" điền sẵn 10 dòng: LF↔RF, 2LO→3LI, 2LI→3LO, 2RI→3RO, 2RO→3RI, 3LO→2LI, 3LI→2LO, 3RI→2RO, 3RO→2RI. Sửa tay được. Settings có 8 mẫu chuẩn, không mẫu nào cho mooc. | P1 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` | Lấy, thêm mẫu cho mooc |
| FR-fleetio-tires-015 | Đảo tự do khép kín | Nút Rotate Tires chỉ bật khi sơ đồ khép kín. Ô trống cũng có dòng New Position và được làm đích. Thông báo đếm cả ô trống. | P0 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` | Lấy |
| FR-fleetio-tires-016 | Lưu mẫu đảo tuỳ biến | Hiện "Save as a Custom Rotation Pattern" khi đã khép kín. Bỏ trống tên thì không đảo được. Lưu thật không thử vì mẫu nằm trong Settings. | P2 | [Gói: Bảo dưỡng đội xe] | test | `Chạy một phần` | Cân nhắc |
| FR-fleetio-tires-017 | Undo Rotation | Chỉ ở màn kết quả. Lốp về chỗ cũ, quay lại form, mapping còn nguyên, Activity không còn dấu vết. Close thì mất nút. | P1 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` | Lấy, giữ dấu vết |
| FR-fleetio-tires-018 | Tháo | Remove từng lốp, Select All, Remove All. Không hỏi lý do, không chọn đích. Ô về nút +. Thêm dòng `Removal`. | P0 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` | Lấy thao tác, thêm lý do, đích, DX-06 |
| FR-fleetio-tires-019 | Tire Activity | 1 dòng mỗi sự kiện từng lốp. Cột Tire Model, Date Recorded, Date Installed, Tire Meter, Activity, User, Method, Tire Pressure, Tread Depth, Position, Axle Type, Tire Identification Number. Đảo 10 lốp sinh 10 dòng dạng "Left Front (LF) > Right Front (RF)", "Steer > Steer". Còn sau khi tháo. | P0 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` | Lấy |
| FR-fleetio-tires-020 | Tire Readings | 1 dòng mỗi vị trí đang có lốp, là lần đọc mới nhất. Cột Vehicle, Last Reading Date, Reading Method, Recorded By, Tread Depth, Pressure, Position, Tire Model, Tire Meter, Install Date, Life Expectancy, Minimum, Factory, mã lốp. Lọc Tread Depth Health (Low, Warning, Normal, Unknown), Reading Method (Manual, Inspection, Telematics, API, Import); Group. | P1 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` | Lấy |
| FR-fleetio-tires-021 | Mức sức khoẻ gai | Ba mức theo Min của lốp, tính lại khi đổi Min. Áp suất không có mức theo lốp. | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | test | `Chạy`, công thức `Suy` | Lấy, ngưỡng là tham số mới, chưa có mã |
| FR-fleetio-tires-022 | Mục Tire Readings của biểu mẫu | Tick Tread Depth, Pressure; Minimum, Maximum cho từng cái; bắt ảnh hoặc nhận xét khi Pass, Fail. | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | test | `Chạy` | Lấy |
| FR-fleetio-tires-023 | Phiếu sinh ô theo trục | Tự sinh ô Tread Depth, Pressure theo cấu hình. Thứ tự đi vòng: bên trái từ trước ra sau, rồi bên phải từ sau ra trước. Xe chưa khai trục: hộp "More info needed" cho khai ngay, Done xong sinh lốp cho mọi vị trí. | P1 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` | Lấy |
| FR-fleetio-tires-024 | Phiếu phát hiện thiếu lốp | "Install Missing Tires" kèm danh sách, nút Install Tires tạo lốp trống, không hỏi gì thêm. | P1 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` | Lấy, cần serial |
| FR-fleetio-tires-025 | Không đạt thành sự cố | Workflow "ANY Failed Inspection Item" → "Create an issue". Một sự cố cho nhiều lốp, Priority High, Source là phiếu. Kết quả từng vị trí có dấu tích hoặc X, dòng tổng một chữ "Fail". Ghi về Tire Readings, Method "Inspection #…". | P1 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` | Lấy, thêm trường vị trí, DX-11 |
| FR-fleetio-tires-026 | Số km lốp | Tự tính theo đồng hồ của chính xe chứa lốp, tính lại liên tục. Lùi ngày lắp thì tính từ các số đồng hồ sau ngày lắp. Nhập được Tire Meter at Installation. | P1 | [Gói: Bảo dưỡng đội xe] | test | `Chạy`, quy tắc `Suy` | Đổi cho mooc, DX-03 |
| FR-fleetio-tires-027 | Liên kết xe | Linked Vehicles hai chiều, khối "Linked Assets". Gỡ và gắn từ phía nào cũng được. Không truyền lốp, không truyền số km. | P1 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` | Không đủ, thay bằng tổ hợp, DX-03 |
| FR-fleetio-tires-028 | Báo cáo | Standard Reports chỉ có "Tire Activity Report"; thêm màn Tire Readings. | P2 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` | Mở rộng |
| FR-fleetio-tires-029 | Đọc áp suất tự động | "Automated tire pressure readings" khoá, chỉ 4x2 hoặc 4x4 có telematics; tài liệu hãng nói Geotab. | P2 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` phần đọc màn hình, `Docs` | Để sau |
| FR-fleetio-tires-030 | Import lốp | Tài liệu hãng có mẫu import lốp, chưa chạy. | P2 | [Cấu hình] | demo | `Docs` | Lấy khi khởi tạo khách |

## 4. Non-Functional Requirements (NFR)

| ID | Category | Requirement | Priority | Acceptance |
|---|---|---|---|---|
| NFR-fleetio-tires-001 | đơn vị | Gai /32 in và áp suất PSI cố định dù xe đặt Metric. | P1 | `Chạy`, không đạt với Việt Nam |
| NFR-fleetio-tires-002 | truy vết | Mọi lần lắp, đảo, đọc, tháo có dòng lịch sử; Undo và Copy details là ngoại lệ. | P0 | `Chạy` |
| NFR-fleetio-tires-003 | độ chính xác | Lịch sử giữ số thập phân, màn hình làm tròn không nhất quán: 12.5 thành 13, 4.5 thành 5, 79.9 thành 79. | P2 | `Chạy` |

## 5. Business Rules

| ID | Rule | Tầng | Trigger | Implements FR | Source |
|---|---|---|---|---|---|
| BR-fleetio-tires-001 | Chỉ lắp vào vị trí trống: ô có lốp xám trong Position, chip trục đầy biến mất, Save tắt. | [Gói: Bảo dưỡng đội xe] | Lắp | FR-fleetio-tires-008 | `Chạy` |
| BR-fleetio-tires-002 | Có lốp thì không đổi cấu hình trục. | [Gói: Bảo dưỡng đội xe] | Sửa cấu hình | FR-fleetio-tires-006 | `Chạy` |
| BR-fleetio-tires-003 | Low: gai ≤ Min. Warning: Min < gai ≤ Min + 2. Normal: còn lại. Fleetio: khoảng đệm 2/32 in. | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Đọc, đổi Min | FR-fleetio-tires-021 | `Suy` từ hai mức Min |
| BR-fleetio-tires-004 | Chọn Tire Model thì Factory, Min, Life theo mẫu và khoá. | [Gói: Bảo dưỡng đội xe] | Lắp | FR-fleetio-tires-010 | `Chạy` |
| BR-fleetio-tires-005 | Đảo phải khép kín và trong cùng một xe. | [Gói: Bảo dưỡng đội xe] | Đảo | FR-fleetio-tires-015 | `Chạy` |
| BR-fleetio-tires-006 | Khi đảo, gai, áp suất, số km đi theo lốp. | [Gói: Bảo dưỡng đội xe] | Đảo | FR-fleetio-tires-014 | `Chạy` |
| BR-fleetio-tires-007 | Copy details không chép gai, áp suất. | [Gói: Bảo dưỡng đội xe] | Chép | FR-fleetio-tires-012 | `Chạy` |
| BR-fleetio-tires-008 | Trên phiếu, biên tính là đạt: dưới Min hoặc ngoài khoảng Min đến Max mới Fail. | [Gói: Bảo dưỡng đội xe] | Nộp phiếu | FR-fleetio-tires-022 | `Chạy` |
| BR-fleetio-tires-009 | Mức của biểu mẫu và Min của lốp độc lập nhau. | [Gói: Bảo dưỡng đội xe] | Đọc | FR-fleetio-tires-021, FR-fleetio-tires-022 | `Chạy` |
| BR-fleetio-tires-010 | Chỉ phiếu kèm workflow mới tạo sự cố, đọc trên màn lốp chỉ đổi màu. | [Gói: Bảo dưỡng đội xe] | Đọc | FR-fleetio-tires-025 | `Chạy` |
| BR-fleetio-tires-011 | Phiếu có Tire Readings mà xe chưa khai trục thì không nộp được. | [Gói: Bảo dưỡng đội xe] | Nộp phiếu | FR-fleetio-tires-023 | `Chạy` |
| BR-fleetio-tires-012 | Số km lốp = số đồng hồ mới nhất − số đồng hồ gần nhất trước ngày lắp; số cùng ngày lắp không làm mốc; không có mốc thì không tính. | [Gói: Bảo dưỡng đội xe] | Thêm số đồng hồ | FR-fleetio-tires-026 | `Chạy`, quy tắc `Suy` |
| BR-fleetio-tires-013 | Mã lốp không duy nhất, không kiểm trùng. | [Gói: Bảo dưỡng đội xe] | Lắp, sửa | FR-fleetio-tires-009 | `Chạy` |
| BR-fleetio-tires-014 | Phiếu đòi nhận xét hoặc ảnh theo cấu hình mục. | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Nộp phiếu | FR-fleetio-tires-022 | `Chạy` |
| BR-fleetio-tires-015 | Xe nào cũng phải có đồng hồ Miles, Kilometers hoặc Hours, kể cả mooc. | [Gói: Bảo dưỡng đội xe] | Tạo xe | FR-fleetio-tires-026 | `Chạy` |
| BR-fleetio-tires-016 | Spare nằm ngoài đảo và ngoài phiếu kiểm. | [Gói: Bảo dưỡng đội xe] | Đảo, phiếu | FR-fleetio-tires-011 | `Chạy` |
| BR-fleetio-tires-017 | Tháo không có lý do, không có đích, không có kho. | [Gói: Bảo dưỡng đội xe] | Tháo | FR-fleetio-tires-018 | `Chạy` |
| BR-fleetio-tires-018 | Liên kết xe không truyền số km, không đổi lốp. | [Gói: Bảo dưỡng đội xe] | Sửa Linked Vehicles | FR-fleetio-tires-027 | `Chạy` |
| BR-fleetio-tires-019 | Vai trò trục là nhãn: dòng phụ vẫn "4 wheel positions, 2 driven (rear)" khi trục sau là Tag. "Wheel position" đếm đầu trục, lốp kép tính 1. | [Gói: Bảo dưỡng đội xe] | Đổi vai trò | FR-fleetio-tires-005 | `Chạy` |
| BR-fleetio-tires-020 | Lắp bằng Tire Model không sinh Inventory Activity, không trừ kho, không vào chi phí xe. | [Gói: Bảo dưỡng đội xe] | Lắp | FR-fleetio-tires-010 | `Chạy` |
| BR-fleetio-tires-021 | Lốp đơn hay kép đi theo cấu hình có sẵn, không chỉnh từng trục. | [Gói: Bảo dưỡng đội xe] | Khai trục | FR-fleetio-tires-003 | `Chạy` |

## 6. Error Matrix

| Error ID | Title | Trigger | Severity | Related FR | Screen state | Recovery |
|---|---|---|---|---|---|---|
| E-fleetio-tires-001 | Phiếu thiếu cấu hình trục | "Please select axle configuration before submitting the form" kèm "Could not submit inspection form. Please fix any errors and try again." | major | FR-fleetio-tires-023 | Hộp đỏ, "More info needed" | Khai trục trong phiếu, Done |
| E-fleetio-tires-002 | Sửa cấu hình khi có lốp | "Axle Configuration cannot be edited for this Vehicle because it has installed Tires" | minor | FR-fleetio-tires-006 | Edit khoá, tooltip | Remove All |
| E-fleetio-tires-003 | Đảo chưa khép kín | Chỉ có 1LO → 3LO, không có câu báo | minor | FR-fleetio-tires-015 | Nút Rotate Tires tắt | Thêm 3LO → 1LO |
| E-fleetio-tires-004 | Mẫu đảo thiếu tên | "Could not rotate tires.", "can't be blank" nằm cuối form | minor | FR-fleetio-tires-016 | Lỗi đầu form, chi tiết cuối form | Nhập tên, hoặc bỏ tick |
| E-fleetio-tires-005 | Thiếu nhận xét khi Fail | "must contain a remark on failure" | major | FR-fleetio-tires-022 | Lỗi tại ô | Nhập nhận xét, ảnh |
| E-fleetio-tires-006 | Lắp đè | Không có câu báo | minor | FR-fleetio-tires-008 | Ô xám, Save tắt | Tháo trước |
| E-fleetio-tires-007 | Không thấy biểu mẫu | "No inspection forms exist yet" dù tài khoản có form, do xe chưa được gán | minor | FR-fleetio-tires-022 | Trạng thái rỗng | Gán biểu mẫu; câu chữ gây hiểu nhầm, không nên học |
| E-fleetio-tires-008 | Chép gai, áp suất | "For data accuracy, current tread depth and pressure cannot be copied." | minor | FR-fleetio-tires-012 | Ô rỗng khoá tick | Nhập tay |
| E-fleetio-tires-009 | Copy details xoá trắng đích | Chỉ tick mã lốp, chép sang 1LI, 1LO: Factory 16, Life 100.000 bị xoá. Chỉ tick Factory thì mã lốp đích không đổi | critical | FR-fleetio-tires-012 | Lưu, không báo | Nhập lại; không nên học |
| E-fleetio-tires-010 | Undo xoá dấu vết | Undo Rotation | major | FR-fleetio-tires-017 | Activity sạch | Không có; không nên học |
| E-fleetio-tires-011 | Sự cố thiếu lỗi | 2LI áp 120.1 có X ở phiếu, mô tả sự cố không nhắc áp suất 2LI | major | FR-fleetio-tires-025 | Sự cố thiếu nội dung | Mở phiếu đọc lại |
| E-fleetio-tires-012 | Số km lốp đứng yên | Mooc không có số đồng hồ trước ngày lắp: Tire Meter "—", Edit và Rotate hiện 0 | major | FR-fleetio-tires-026 | Không báo | Nhập Tire Meter tay |
| E-fleetio-tires-013 | Danh mục rỗng | Tire Model "No options", form không có nút tạo | minor | FR-fleetio-tires-010 | Ô chọn rỗng | Tạo Part category lốp |
| E-fleetio-tires-014 | Không có mẫu đảo mooc | Rotation Pattern "No options" trên mooc | minor | FR-fleetio-tires-014 | Ô chọn rỗng | Tự ghép |
| E-fleetio-tires-015 | Mã lốp trùng không báo | Cùng xe, sang vị trí khác; tháo rồi lắp lại cũng không báo | major | FR-fleetio-tires-009 | Lưu | Không nên học |
| E-fleetio-tires-016 | Chạm trần số xe | "You've reached the maximum number of records allowed on your account." Save Vehicle khoá; nơi khác "Your plan is limited to 5 vehicles", "Vehicle could not be created" | major | FR-fleetio-tires-001 | Nút khoá | Nâng gói |

## 7. Success Criteria

| ID | Outcome nghiệp vụ | Đo bằng | Mốc đạt |
|---|---|---|---|
| SC-fleetio-tires-01 | Lắp đủ một xe nhanh | Số thao tác để lắp 10 lốp | Fleetio: 3 chip trục trên 6x4 khi đã chạy |
| SC-fleetio-tires-02 | Biết lốp cần thay | Lọc Low, Warning | `Chạy` |
| SC-fleetio-tires-03 | Truy được một lốp qua nhiều xe | Có định danh thật | Fleetio: không đạt |

## 8. Data Entities (tóm tắt — chi tiết ở erd.md)

Vehicle, Axle Configuration, Axle, Tire (vị trí), Tire Model (Part), Tire Activity, Rotation Pattern, Meter Entry, Linked Vehicles, Inspection Submission, Issue. Xem [[docs/_research/fleetio/srs/fleetio-tires-erd.md|ERD]].

## 9. Flows (tóm tắt — chi tiết ở flows.md)

Xem [[docs/_research/fleetio/srs/fleetio-tires-flows.md|Flows]], [[docs/_research/fleetio/srs/fleetio-tires-states.md|States]], [[docs/_research/fleetio/srs/fleetio-tires-usecases.md|Use case]], [[docs/_research/fleetio/srs/fleetio-tires-userflow.md|User flow]].

## 10. Screens

Ảnh thật và bảng mô tả: [[docs/_research/fleetio/srs/fleetio-tires-screens.md|Màn hình]]. Không áp `CMP`, `GR` vì mô tả sản phẩm của bên khác.

## 11. Constraints, Dependencies & Assumptions

| Giả định | Invalidate nếu sai |
|---|---|
| `GĐ` Case giữa hai xe suy từ cơ chế trên một xe | Chạy được xe thứ ba thì kiểm lại các dòng `Suy` ở Mục 13 |
| Tài khoản dùng thử có thể khác gói trả phí | Các tính năng bị khoá phải xem lại |

## 12. Open Questions

* [ ] OQ-1: Quy luật Minimum tự hiện 4/32": trục 3 mooc để trống lại hiện 4/32", LO trên đầu kéo để trống thì trống, lắp từ phiếu thì trống — Nguồn khách: không áp dụng
* [ ] OQ-2: Ngưỡng mặc định khi không có Min: 3/32" vẫn Low, 10/32" Normal, chưa biết biên — Nguồn khách: không áp dụng
* [ ] OQ-3: Mooc hiện 3.502 km, số nhập cuối là 3.500, chưa kiểm nguồn — Nguồn khách: không áp dụng
* [ ] OQ-4: Hình 6x2, 8x4, 10x, 12x chưa xem; Semi Truck có lưu được cấu hình mooc không (danh sách vẫn liệt kê, chưa lưu thử) — Nguồn khách: không áp dụng
* [ ] OQ-5: Phiếu Fail lần 2 có gộp vào sự cố cũ không: thấy "Added to Issue #41 (1 time reported)", chưa nộp lần 2 — Nguồn khách: không áp dụng
* [ ] OQ-6: Lệnh sửa chữa có phụ tùng lốp thì lốp có đổi khi đóng lệnh không: form lệnh không có trường lốp, chưa thêm phụ tùng lốp vào lệnh — Nguồn khách: không áp dụng
* [ ] OQ-7: Lưu mẫu đảo tuỳ biến, điều kiện có Coverage Template, Spare trên 4x2 RWD (Dually), tháo Spare — Nguồn khách: không áp dụng
* [ ] OQ-8: Đổi lốp thật giữa hai xe, một mooc gắn hai đầu kéo: cần tài khoản hết trần số xe — Nguồn khách: không áp dụng
* [ ] OQ-9: Nhắc theo độ mòn: không thấy ở Tire Management, tài liệu hãng không nói tới; chưa kiểm trong form nhắc lịch — Nguồn khách: không áp dụng
* [ ] OQ-10: Delta có đo gai định kỳ không, hay chỉ quản lý vị trí và serial? — Nguồn khách: file sơ đồ lốp của Delta
* [ ] OQ-11: Lốp tháo ra có những đích nào: kho, xưởng, rác thải, đi đắp, chuyển xe khác? — Nguồn khách: Phân hệ FIAM (25/10/2026), mục Chốt chặn Sơ đồ lốp và Bình ắc quy
* [ ] OQ-12: Số km lốp mooc tính theo GPS đầu kéo trong thời gian ghép có được chấp nhận không? — Nguồn khách: chưa có trong tài liệu khách gửi

OQ-4 của bộ `fleetio-vehicle` (tab Tire Management) đã trả lời bằng bộ tài liệu này.

## 13. Ma trận case

### 13.1 Cấu hình trục

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| Form tạo xe có trục không | New Vehicle | Không. Chỉ có trường chữ ở Wheels & Tires | `Chạy` |
| Trình hướng dẫn | Vehicle → 6 → Axle Type | 6x2, 6x4, 6x6 | `Chạy` |
| Trình hướng dẫn, 12x | | Chỉ 4, 6, 8, 10; 12x4, 12x6 chỉ ở danh sách "I know" | `Chạy` |
| Chọn Trailer | Asset Type | Nhảy sang ô cấu hình, chỉ 7 dòng mooc | `Chạy` |
| Tạo cấu hình tuỳ biến | Danh sách | Không có | `Chạy` |
| Vai trò trên mooc | Menu trục | Dead, Lifted, Trailer, Other | `Chạy` |
| Vai trò trên xe | Menu trục | Steer, Drive, Dead, Lifted, Tag, Pusher, Other | `Chạy` |
| Đổi vai trò khi chưa lốp | Trailer → Lifted | "Trailer Axle 1 updated successfully", còn sau khi tải lại | `Chạy` |
| Đổi vai trò khi có lốp | Drive → Tag, Edit trục đang khoá | Đổi được, không có dòng Activity | `Chạy` |
| Vai trò đổi số cầu kéo không | Trục sau thành Tag | Dòng phụ vẫn "4 wheel positions, 2 driven (rear)" | `Chạy` |
| Vai trò ghi vào lịch sử | Lắp lốp trên trục Tag | Axle Type của dòng là `Tag` | `Chạy` |
| Đổi cấu hình khi có lốp | | Edit khoá, có tooltip | `Chạy` |
| Tháo hết rồi đổi | Remove All 9 lốp | Edit mở lại, 6x4 → 4x2 RWD (Dually) được; Activity giữ nguyên | `Chạy` |
| Đổi cấu hình mất vai trò | Tri-Axle có Lifted → Multi → Tri-Axle | Trục về "Trailer" | `Chạy` |
| Multi-Axle | Trên mooc | Thêm "Number of Axles *" 2 đến 10, tiêu đề "4 Axle" | `Chạy` |
| Loại xe ràng buộc cấu hình không | Semi Truck, ô Edit lọc "Axle" | Vẫn liệt kê 7 cấu hình mooc, chưa lưu thử | `Chạy một phần` |
| Số vị trí | Tri-Axle "6 wheel positions", 12 ô; 6x4 "6 wheel positions, 4 driven", 10 ô | Đếm đầu trục, lốp kép tính 1 | `Chạy` |
| Lốp đơn, kép từng trục | | Không chỉnh được | `Chạy` |
| 4x2 kép | 4x2 RWD (Dually) | Trước 2, sau 4 (LO, LI, RI, RO), đúng đầu kéo 4x2 | `Chạy` |
| 12x, 8x4, 10x | | Chỉ thấy trong danh sách | `Không chạy` |
| Khai trong phiếu | Xe chưa có trục | Chọn trong phiếu, Done, tự sinh lốp cho mọi vị trí | `Chạy` |

### 13.2 Lắp

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| Nhiều lốp một lần | Chip "Axle 1" | 4 lốp cùng thông số, cùng mã | `Chạy` |
| Bấm ô + | Vị trí trống | Form điền sẵn vị trí | `Chạy` |
| Thiếu mã, gai, áp suất | Để trống | Lưu được. Sơ đồ "–/32"", dòng "Unknown Tire" | `Chạy` |
| Lắp đè | Ô đã có lốp | Ô xám, chip đầy biến mất, Save tắt | `Chạy` |
| Mã lốp trùng | Cùng xe, vị trí khác | Không cảnh báo | `Chạy` |
| Số thập phân | Gai 12.5, áp 95.5 | Activity giữ 12.5; ô nhập hiện 13; 4.5 trên sơ đồ hiện 5/32"; 79.9 PSI hiện 79PSI ở bảng | `Chạy` |
| Danh mục mẫu lốp | Chưa có Part category lốp | "No options" | `Chạy` |
| Nguồn danh mục | Tạo Part `TEST-LOP-MODEL-01` category Tires | Xuất hiện ngay | `Chạy` |
| Chọn Tire Model | Factory 20, Min 6, Life 120.000 | 3 ô tự điền, có biểu tượng ổ khoá | `Chạy` |
| Không có chi phí | Form lắp, Part giá 3.000.000 ₫ | Không có ô tiền, "There is no Inventory Activity for this part"; Total Costs tháng này 1.500.000 ₫ nên không cộng giá lốp | `Chạy` |
| Ngày lắp quá khứ | 10/20, 10/24 | Lưu được | `Chạy` |
| Tire Meter at Installation | 12.000 | "12,000 kilometers" | `Chạy` |
| Minimum để trống | Trục 3 mooc | Bảng hiện 4/32"; LO đầu kéo để trống thì trống; lắp từ phiếu thì trống. Chưa rõ quy luật | `Chạy`, chưa giải thích được |
| Lắp Spare | Add, "Spare Tire" | `Spare Stowed`, Axle Type `N/A`, "6 + Spare" | `Chạy` |
| Copy details, trường | | Không chép gai, áp suất; ô rỗng khoá tick | `Chạy` |
| Copy details, lỗi | Chỉ tick mã lốp, sang 1LI, 1LO | Mã đổi, Factory 16, Life 100.000 của đích xoá trắng. Hai lần đều vậy. Chỉ tick Factory thì mã đích không đổi | `Chạy` |
| Copy details, ô trống | Đích trống | Tạo lốp mới, `Installed`, ngày hôm nay, gai trống | `Chạy` |
| Copy details, lịch sử | Đích có lốp | Không có dòng Activity | `Chạy` |
| Trong phiếu kiểm | Xe thiếu 2 lốp | Install Tires tạo lốp trống | `Chạy` |

### 13.3 Đảo

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| Mẫu trên mooc | Rotation Pattern | "No options". Settings có 8 mẫu chuẩn, không cho mooc | `Chạy` |
| Mẫu trên 6x4 | "Standard 6x4" | Điền sẵn 10 dòng, kể cả ô trống LF | `Chạy` |
| Đảo khi có ô trống | LF trống, Standard 6x4 | RF sang LF, RF trống. "Successfully Rotated 10 tires" đếm cả ô trống | `Chạy` |
| Tự do, chưa khép kín | Chỉ 1LO → 3LO | Nút tắt | `Chạy` |
| Tự do, khép kín | Thêm 3LO → 1LO | Nút bật, hiện "Save as a Custom Rotation Pattern" | `Chạy` |
| Tick lưu mẫu, trống tên | | "Could not rotate tires.", "can't be blank" | `Chạy` |
| Dữ liệu theo lốp | Sau đảo | Gai, áp suất, số km đi theo lốp | `Chạy` |
| Lịch sử | Đảo 10 lốp | 10 dòng "Left Front (LF) > Right Front (RF)", "Steer > Steer" | `Chạy` |
| Undo | Ngay sau đảo | Về chỗ cũ, quay lại form, mapping còn. Activity sạch | `Chạy` |
| Undo sau khi đóng | Close | Không còn nút | `Chạy` |
| Đảo sang xe khác | | New Position chỉ có vị trí của xe đó | `Chạy` |
| Đảo Spare | | Không có dòng, không có trong New Position | `Chạy` |
| Lưu mẫu tuỳ biến | | Không lưu vì mẫu nằm trong Settings, quy định Settings chỉ đọc. Form Settings cho chọn cả nhóm mooc | `Không chạy` |

### 13.4 Tháo

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| Tháo một lốp | LF | "1 tire was removed from this asset.", ô về + | `Chạy` |
| Tháo nhiều | Select All, Remove All | Tháo được, xác nhận "permanently remove" | `Chạy` |
| Lý do, đích | | Không hỏi, không có kho, không có chuyển kho | `Chạy` |
| Menu dòng lốp | | Chỉ Edit, Copy details to..., Remove | `Chạy` |
| Sau tháo, Tire Readings | | Dòng biến mất | `Chạy` |
| Sau tháo, Tire Activity | | Dòng `Removal`, lịch sử còn | `Chạy` |
| Lắp lại | Gõ lại mã `TEST-TIN-A2` | Không báo, không nối lịch sử; km về 0 nếu không nhập tay | `Chạy` |
| Tháo Spare | | Chưa ghi nhận | `Không chạy` |

### 13.5 Đọc

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| Biên, Min 4 | 3.9, 4.0 | Low đỏ | `Chạy` |
| Biên, Min 4 | 4.5, 5, 6.0 | Warning vàng | `Chạy` |
| Biên, Min 4 | 6.1, 6.9, 7, 8 | Normal | `Chạy` |
| Biên, Min 8 | 9, 10 | Warning | `Chạy` |
| Biên, Min 8 | 10.5, 11, 12 | Normal | `Chạy` |
| Quy tắc | | Low ≤ Min, Warning ≤ Min + 2, còn lại Normal | `Suy` |
| Không có Min | TEST-XE-01 | 3/32" Low, 10/32" Normal; ngưỡng mặc định chưa xác định | `Chạy` |
| Đổi Min | 5 → Min 8 | Mức tính lại | `Chạy` |
| Áp suất | 60 PSI | Không có mức theo lốp | `Chạy` |
| Đơn vị | Xe đặt Metric | Vẫn /32 in, PSI | `Chạy` |
| Đọc lùi ngày | | Không có ô ngày ở dòng và hộp Edit | `Chạy` |
| Đọc nhiều lốp | | Màn lốp không có, chỉ phiếu kiểm | `Chạy` |
| Lưu khi rời ô | Sửa trên dòng | Lưu ngay, tạo dòng đọc | `Chạy` |
| Dưới mức trên màn lốp | Gai 3, Min 4 | Chỉ đổi màu; **không** sự cố, **không** thông báo, **không** nhắc | `Chạy` |
| Import | Tài liệu hãng có mẫu | Chưa chạy | `Docs` |
| Tự động | Khoá, chỉ 4x2, 4x4 | Không dùng được cho đầu kéo 6x4 | `Chạy` đọc màn hình, `Docs` |

### 13.6 Đồng hồ, số km lốp

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| Bỏ đồng hồ | Primary Meter | Không được, chỉ Miles, Kilometers, Hours | `Chạy` |
| Mooc tạo mới | Để trống | Thành "0 km" | `Chạy` |
| Mooc không có số trước ngày lắp | Lắp 10/20, 10/24, sau nhập 1.000 (10/25), 3.000, 3.500 | Tire Meter vẫn "—", Edit và Rotate hiện 0 | `Chạy` |
| Mooc có số trước ngày lắp | Lắp 11/03, có 1.000 ngày 10/25, 3.000 cùng ngày 11/03, tiếp 3.500 | 2.500 = 3.500 − 1.000; số cùng ngày không làm mốc | `Chạy`, quy tắc `Suy` |
| Tính lại liên tục | TEST-XE-01 | 100 → 800 → 799 km khi đồng hồ đổi | `Chạy` |
| Lốp qua phiếu | Đồng hồ 2.200 → 2.300 | Tire Meter 100 km | `Chạy` |
| Đầu kéo tăng km | TEST-XE-LOP lên 20.500 | Mooc giữ 3.500 | `Chạy` |
| Số lạ | Trang lốp mooc | Hiện 3.502 km, không nhập số này | `Chạy`, chưa kiểm nguồn |

### 13.7 Liên kết đầu kéo, mooc

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| Hai chiều | Liên kết từ đầu kéo | Mooc cũng có "Linked Assets" › TEST-XE-LOP | `Chạy` |
| Tab lốp đầu kéo | Đã liên kết | **Không** thêm lốp mooc, vẫn 3 trục | `Chạy` |
| Gỡ | Xoá chip ở đầu kéo | "There are no linked Assets for this Vehicle"; lốp 12 + Spare, đồng hồ không đổi | `Chạy` |
| Gắn lại từ mooc | | Đầu kéo hiện lại mooc | `Chạy` |
| Đổi mooc | | Là gỡ rồi gắn. Không có lịch sử ghép, không có ngày | `Suy` |
| Một mooc nhiều đầu kéo | Ô chọn nhiều | Xe còn lại của nhóm khác | `Không chạy` |

### 13.8 Đổi lốp giữa các xe

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| Đầu kéo ↔ mooc, hai đầu kéo, hai mooc | | **Không có thao tác.** Tháo bên A, lắp mới bên B, gõ lại mã, gai, áp suất, km. Hai lịch sử không nối | Cơ chế `Chạy` trên một xe, giữa hai xe `Suy` |
| Cùng xe, không qua đảo | Remove rồi lắp, mã `TEST-TIN-A2` | Không báo gì | `Chạy` |

### 13.9 Phiếu kiểm

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| Xe không thấy biểu mẫu | Mooc chưa gán form | "No inspection forms exist yet" dù có form | `Chạy` |
| Mục Tire Readings | Khi tạo form | Tick Tread Depth, Pressure; Min, Max; bắt ảnh hoặc nhận xét | `Chạy` |
| Xe chưa khai trục | Bấm Save | E-fleetio-tires-001, cho khai ngay trong phiếu | `Chạy` |
| Thiếu lốp | Tri-Axle, thiếu 2 | "Install Missing Tires", "2 tires were successfully installed" | `Chạy` |
| Thứ tự ô | 12 vị trí | Đi vòng trái trước ra sau, phải sau ra trước | `Chạy` |
| Spare | Phiếu 12 vị trí | **Không có** | `Chạy` |
| Biên | Min 5, áp 80 đến 120 | 5 Pass, 4.9 Fail; 80 Pass, 79.9 Fail; 120 Pass, 120.1 Fail | `Chạy` |
| Dưới mức biểu mẫu | 3/32, Min 5 | "must contain a remark on failure" | `Chạy` |
| Kết quả từng vị trí | Mở rộng mục | Dấu tích hoặc X; dòng tổng một chữ "Fail" | `Chạy` |
| Ghi về lốp | | Có, Method "Inspection #…" | `Chạy` |
| Hai mức tối thiểu | 1LO gai 5, form Min 5, lốp Min 8 | Phiếu Pass, Tire Readings Low | `Chạy` |
| Fail tạo sự cố | | #41 "[Inspection] Tire Readings", High, một sự cố nhiều lốp | `Chạy` |
| Tiêu đề từ nhận xét | Phiếu #126051306 | #32 "[Inspection] TEST gai thap" | `Chạy` |
| Nguồn tạo sự cố | | Workflow của biểu mẫu, không do lốp | `Chạy` |
| Sự cố gắn vị trí | | Chỉ trong chữ mô tả, **không** có trường vị trí | `Chạy` |
| Mô tả thiếu lỗi | 2LI áp 120.1 | Không nhắc áp suất 2LI | `Chạy` |
| Fail lần 2 | | "Added to Issue #41 (1 time reported)" gợi ý gộp, chưa nộp | `Không chạy` |

### 13.10 Liên hệ sang chức năng khác

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| Lệnh sửa chữa | Form Work Order | Không có trường lốp. Lốp không đổi khi đóng lệnh là suy luận | `Chạy một phần` |
| Phụ tùng từ kho | Lắp bằng Tire Model | **Không** sinh Inventory Activity, **không** trừ kho | `Chạy` |
| Nhắc theo độ mòn | | Không thấy ở Tire Management, tài liệu hãng không nói tới | `Chạy một phần` |
| Chi phí | | **Không** vào chi phí xe | `Chạy` |
| Báo cáo | Standard Reports | Chỉ "Tire Activity Report" | `Chạy` |
| Life Expectancy | | Không tạo cảnh báo nào trong các case đã chạy | `Chạy` |

## 14. So với nhu cầu Delta và đề xuất Invlogis

> Phần này không mô tả Fleetio, là đề xuất để cân nhắc, chưa chốt với Delta. Bảng so sánh: [[docs/_research/fleetio/fleetio-tires.md|Brainstorm]] Phụ lục A.1.

| Mã | Đề xuất | Tầng đề xuất | Thay cho |
|---|---|---|---|
| DX-01 | Quả lốp là đối tượng độc lập, serial duy nhất; nhóm Lốp trong `P-nhom-hang` (Delta: bắt buộc serial) | [Gói: Bảo dưỡng đội xe] | BR-fleetio-tires-013 |
| DX-02 | Mỗi lần lắp là một đoạn: lốp, xe, vị trí, từ ngày và km, đến ngày và km, lệnh. Km lốp là tổng các đoạn. Chuyển xe không đứt lịch sử | [Gói: Bảo dưỡng đội xe] | Mục 13.8 |
| DX-03 | Lốp mooc lấy km theo tổ hợp: 1 đầu kéo + 0 hoặc 1 mooc + 0–2 container, một Lệnh một tổ hợp (DEC-267). Mooc không cần đồng hồ riêng | [Lõi] phần tổ hợp · [Gói: Bảo dưỡng đội xe] phần tính km | BR-fleetio-tires-015, BR-fleetio-tires-018 |
| DX-04 | Xem chung sơ đồ tổ hợp bằng `Tyre Layout`, dữ liệu lốp hai xe vẫn tách | [Gói: Bảo dưỡng đội xe] | FR-fleetio-tires-027 |
| DX-05 | Vòng đời lốp: Trong kho, Đang lắp, Dự phòng trên xe, Tồn xưởng, Rác thải; đi đắp chờ OQ-11 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | BR-fleetio-tires-017 |
| DX-06 | Tháo bắt buộc lý do và đích. Danh sách lý do: tham số mới, chưa có mã | [Gói: Bảo dưỡng đội xe] [Cấu hình] | FR-fleetio-tires-018 |
| DX-07 | Thay lốp qua lệnh sửa chữa: chốt lệnh đổi vị trí, ngày lắp theo ngày chốt, cập nhật tồn kho, tồn xưởng, rác thải | [Gói: Bảo dưỡng đội xe] | BR-fleetio-tires-020 |
| DX-08 | Chi phí, phân bổ từng lốp. Kỳ phân bổ: tham số mới, chưa có mã (Delta: 36 tháng) | [Gói: Bảo dưỡng đội xe] [Cấu hình] | BR-fleetio-tires-020 |
| DX-09 | Giữ lắp theo ô, phiếu tự sinh ô, đảo khép kín; thêm Spare vào đảo và phiếu; thêm đảo giữa hai xe bằng phiếu chuyển | [Gói: Bảo dưỡng đội xe] | BR-fleetio-tires-005, BR-fleetio-tires-016 |
| DX-10 | Một nguồn mức tối thiểu; khoảng đệm, đơn vị mm hoặc /32 in, bar hoặc PSI: tham số mới, chưa có mã | [Gói: Bảo dưỡng đội xe] [Cấu hình] | BR-fleetio-tires-009, NFR-fleetio-tires-001 |
| DX-11 | Dưới mức tạo việc ở mọi đường đọc; sự cố có trường vị trí, serial | [Gói: Bảo dưỡng đội xe] | BR-fleetio-tires-010 |
| DX-12 | Trạng thái vị trí Warning theo km, ngày, mòn; Error hỏng, cần thay; báo hỏng từ app lái xe | [Gói: Bảo dưỡng đội xe] | FR-fleetio-tires-021 |
| DX-13 | Sơ đồ theo nhóm hình dùng chung, đổi riêng từng dòng xe; 11 sơ đồ; số thứ tự, bên lái, bên phụ. Bảng gán tên xe là dữ liệu của khách | [Lõi] phần sơ đồ · [Riêng Delta] phần bảng gán | FR-fleetio-tires-003 |
| DX-14 | Chặn tạo lệnh sửa chữa khi sơ đồ lốp trống: bật tắt, tham số mới, chưa có mã | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Fleetio không có |
| DX-15 | Danh mục lốp qua đề xuất, phê duyệt: bật tắt, tham số mới, chưa có mã | [Gói: Bảo dưỡng đội xe] [Cấu hình] | FR-fleetio-tires-010 |
| DX-16 | Không học: Undo xoá dấu vết, Copy details xoá trắng đích, mã lốp trùng không báo, đồng hồ bắt buộc cho mooc | Không áp dụng | E-fleetio-tires-009, E-fleetio-tires-010, E-fleetio-tires-015 |

Tham số sẵn có liên quan ghép mooc: `P-quy-tac-ghep-mooc`.
