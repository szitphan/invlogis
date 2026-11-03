---
type: research
feature: fleetio-tires
updated: 2026-11-03
---

# Quản lý lốp — Use cases

## Use cases

| UC | Tên | Actor | FR | Màn | Lỗi | OQ |
|---|---|---|---|---|---|---|
| UC-axle-config | Khai cấu hình trục | Quản trị | 001–006 | 1.1–1.7 | E-002, E-016, E-017 | OQ-4 |
| UC-install-tire | Lắp lốp | Kỹ thuật | 007–011 | 2.1, 2.2, 2.4 | E-006, E-013, E-015 | OQ-1 |
| UC-copy-details | Chép thông số | Kỹ thuật | 012 | 2.3 | E-008, E-009 | — |
| UC-read-tire | Đọc lốp, theo dõi mức | Kỹ thuật, Quản trị | 013, 020, 021, 029, 030 | 2.3, 5.1–5.4 | — | OQ-2, OQ-9, OQ-13 |
| UC-rotate-tire | Đảo lốp | Kỹ thuật | 014–017, 031 | 3.1–3.3 | E-003, E-004, E-010, E-014 | OQ-7 |
| UC-remove-tire | Tháo, thay lốp | Kỹ thuật | 018 | 4.1 | — | OQ-6 |
| UC-inspect-tire | Đọc lốp qua phiếu kiểm | Lái xe | 022–025 | Màn liên quan ở Mục 2 của user flow | E-001, E-005, E-007, E-011 | OQ-5 |
| UC-trailer-tire | Quản lý lốp mooc và liên kết đầu kéo | Quản trị, Kỹ thuật | 026, 027 | 1.7, 2.4 | E-012, E-014 | OQ-3, OQ-8, OQ-12 |
| UC-tire-history | Xem lịch sử, báo cáo | Quản trị | 019, 028 | 5.5 | — | — |

Số FR, lỗi viết tắt, đầy đủ có tiền tố `fleetio-tires`.

## UC-axle-config — Khai cấu hình trục

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Mở tab Tire Management của xe | Màn trống, nút "Set up axle configuration" |
| 2 | Chọn Asset Type | Vehicle: hỏi Wheel Positions. Trailer: nhảy sang ô 7 cấu hình |
| 3 | Chọn cấu hình, hoặc đi đường "I know my axle configuration" | Danh sách 27 dòng |
| 4 | Lưu | Vẽ sơ đồ, mỗi ô trống có nút + |
| 5 | Đổi vai trò từng trục | Ghi nhận, không đổi số cầu kéo |

**Nhánh:** xe có lốp thì Edit khoá (E-002). Tháo hết thì mở lại. Xe Archived: xem được, Edit khoá (E-017); Restore giữ nguyên cấu hình.

## UC-install-tire — Lắp lốp

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Bấm ô + hoặc Add | Mở form, ô + điền sẵn vị trí |
| 2 | Chọn vị trí, chip trục | Ô có lốp xám, chip đầy biến mất (E-006) |
| 3 | Chọn Tire Model | Factory, Min, Life tự điền, khoá; danh mục rỗng thì "No options" (E-013) |
| 4 | Nhập ngày, km, gai, áp suất, mã lốp, có thể bỏ trống | Không kiểm trùng mã (E-015) |
| 5 | Lưu | Mỗi vị trí một dòng `Installed`; không trừ kho, không vào chi phí |

**Nhánh:** chọn "Spare Tire" thì dòng `Spare Stowed`, không có ô trên sơ đồ.

## UC-copy-details — Chép thông số

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Menu dòng lốp, Copy details to... | Danh sách trường, gai và áp suất không chép được (E-008) |
| 2 | Tick trường, chọn đích | Đích trống: tạo lốp mới. Đích có lốp: sửa, không có dòng lịch sử |
| 3 | Xác nhận | "Details copied to 2 tire positions."; có thể xoá trắng Factory, Life của đích (E-009) |

## UC-read-tire — Đọc lốp, theo dõi mức

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Sửa gai, áp suất trên dòng hoặc hộp Edit | Rời ô là lưu, thêm dòng đọc Manual, không có ô ngày |
| 2 | Xem sơ đồ | Màu theo mức gai; không có sự cố, không có thông báo |
| 3 | Mở Vehicles › Tire Readings, lọc | 1 dòng mỗi vị trí đang có lốp, lần đọc mới nhất |

## UC-rotate-tire — Đảo lốp

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Menu Rotate Tires | Form, mỗi vị trí một dòng, không có Spare |
| 2 | Chọn mẫu hoặc tự ghép | Mẫu chuẩn điền sẵn; mooc "No options" (E-014) |
| 3 | Kiểm tra sơ đồ | Chưa khép kín thì nút tắt (E-003) |
| 4 | Tick lưu mẫu nếu muốn | Trống tên thì lỗi (E-004) |
| 5 | Rotate Tires | "Successfully Rotated 10 tires", gai, áp suất, số km theo lốp |
| 6 | Undo Rotation hoặc Close | Undo: về chỗ cũ, lịch sử sạch (E-010). Close: mất Undo |

## UC-remove-tire — Tháo, thay lốp

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Remove, Remove All | Hộp "Remove Tires", chọn nhiều, Select All |
| 2 | Xác nhận | Ô về nút +, dòng `Removal`, mất khỏi Tire Readings |
| 3 | Lắp mới | Là một lần lắp mới, không nối lịch sử |

**Không có:** lý do, đích đến, kho, lệnh sửa chữa.

## UC-inspect-tire — Đọc lốp qua phiếu kiểm

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Start Inspection, chọn biểu mẫu | Xe chưa gán: "No inspection forms exist yet" (E-007) |
| 2 | Vào mục Tire Readings | Chưa khai trục: "More info needed"; thiếu lốp: "Install Missing Tires" |
| 3 | Nhập từng vị trí | Thứ tự đi vòng, không có Spare, biên tính là đạt |
| 4 | Nộp | Fail thiếu nhận xét: E-005; ghi về lốp, Method "Inspection #…" |
| 5 | Xem kết quả | Fail và có workflow: tạo sự cố High, vị trí nằm trong chữ |

## UC-trailer-tire — Quản lý lốp mooc và liên kết đầu kéo

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Tạo xe loại Trailer | Đồng hồ riêng, trống thành "0 km" |
| 2 | Khai 1 trong 7 cấu hình | Sơ đồ mooc, trục mặc định Trailer |
| 3 | Lắp lốp | Như xe, số km theo đồng hồ mooc; thiếu mốc thì "—" (E-012) |
| 4 | Sửa Linked Vehicles ở đầu kéo hoặc mooc | Hai bên đều có "Linked Assets" |
| 5 | Xem tab lốp đầu kéo | Không có lốp mooc |
| 6 | Gỡ, đổi mooc | Lốp, đồng hồ không đổi, không có lịch sử ghép |
| 7 | Nối thêm xe thứ hai vào cùng mooc | Lưu được, không kiểm loại xe, không ngày hiệu lực; không biết đang kéo bởi đầu nào |

## UC-tire-history — Xem lịch sử, báo cáo

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Mở tab Tire Activity | 1 dòng mỗi sự kiện từng lốp, cả lốp đã tháo |
| 2 | Mở Standard Reports | Chỉ có "Tire Activity Report" |
