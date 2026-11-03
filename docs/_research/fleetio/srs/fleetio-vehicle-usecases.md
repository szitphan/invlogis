---
type: research
feature: fleetio-vehicle
updated: 2026-11-03
---

# Phương tiện — Use cases

## Use cases

| UC | Tên | Actor | FR | Màn | Lỗi | OQ |
|---|---|---|---|---|---|---|
| UC-manage-vehicle | Quản lý hồ sơ xe | Fleet Manager | 001–008, 020, 022–026, 043, 050–054 | 1.1–1.5, 1.7–1.11 | E-009, E-010, E-024–E-028, E-032 | OQ-16, OQ-17, OQ-19, OQ-20, OQ-21, OQ-22 |
| UC-archive-vehicle | Lưu trữ, khôi phục xe | Fleet Manager | 021, 048, 049 | 1.2, 1.6 | E-021, E-022, E-023, E-029 | OQ-11 |
| UC-assign-vehicle | Gán, thay người, thu hồi xe | Fleet Manager | 009–012, 027–029 | 2.1–2.6 | E-001, E-003, E-012, E-017, E-030, E-031 | OQ-1, OQ-7, OQ-12, OQ-13, OQ-14 |
| UC-log-meter | Ghi và sửa số đồng hồ | Fleet Manager, Operator | 013–016, 030–032, 044, 046, 047 | 3.1–3.6 | E-002, E-004–E-008, E-013, E-015, E-019, E-020 | OQ-2, OQ-8, OQ-9, OQ-14, OQ-18 |
| UC-tire | Đọc lốp | Technician | 017 | 4.1 | Xem `fleetio-tires` | OQ-3 |
| UC-expense | Ghi chi phí khác, xem chi phí trên km | Kế toán | 018, 033, 034 | 1.3, 5.1–5.3 | E-011, E-018 | — |
| UC-replacement | Phân tích thay xe | Lãnh đạo | 019, 040 | 6.1, 6.2 | — | OQ-15 |
| UC-warranty | Khai bảo hành, thấy cơ hội trên lệnh | Fleet Manager, Kỹ thuật viên | 035–039, 055 | 7.1–7.7 | E-011, E-014, E-016 | OQ-10, OQ-14 |
| UC-recall-pool | Xem Recall, đặt xe chung | Fleet Manager | 041, 042, 056, 057 | Thuộc nhóm Nền tảng | E-033, E-034 | OQ-11 |

Số FR, lỗi viết tắt, đầy đủ có tiền tố `fleetio-vehicle`. FR-045 (automation đổi trạng thái) xem nhóm Nền tảng. FR-044 đã chuyển sang UC-log-meter vì đồng hồ phụ được nhập, xem ở sổ đồng hồ; khai báo vẫn ở form xe.

## UC-manage-vehicle — Quản lý hồ sơ xe

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Tạo xe: tên, loại | Điền sẵn trạng thái, đơn vị |
| 2 | Lưu | Mở trang xe, khối trống có nút thêm |
| 3 | Bổ sung thông số qua Edit, giải mã số khung | Hộp so sánh, dòng New tick sẵn, dòng Different không tick; chỉ ghi vào xe khi Save Vehicle |
| 4 | Dùng Add để tạo bản ghi | Xe điền sẵn; menu đổi theo nhiên liệu của xe |
| 5 | Đổi trạng thái, loại xe, thao tác trong More Actions | Đổi tự do, không hỏi; ghi Status Updates, Record History (`Chạy`) |
| 6 | Với mooc: Type Trailer, thêm vào Linked Vehicles của đầu kéo | Hai xe hiện Linked Assets, không gộp gì khác; một mooc nối được nhiều xe |
| 7 | Tuỳ biến: tìm trường, ẩn hiện thẻ cá nhân | Áp dụng cho riêng người này; layout chung ở Settings |

**Nhánh:** 1a Nhiều xe: Add Multiple, tối đa 200 dòng, lỗi chỉ qua email (E-025). 2a Hết hạn mức: E-009. 2b Trống tên: E-010. 2c Trùng tên, VIN: E-024. 3a VIN ngắn: Decode khoá (E-026). 3b Thoát form chưa lưu: E-027. 5a Nhóm Sample: E-028, cả form bị từ chối. 5b Nhập Out-of-Service: không đổi Status, không tạo dòng đồng hồ. 5c Manage Service Programs: xe chưa có bộ lịch thì chỉ có trang quảng bá, không gán bộ lịch có sẵn. 5d Attach Shared Document: chỉ chọn tài liệu dùng chung, thẻ nhãn "Shared". 1b Gói đầy: Add Multiple khoá từ menu (E-032).

## UC-archive-vehicle — Lưu trữ, khôi phục xe

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | More Actions, Archive | Hộp "Confirm Vehicle Archive" báo trước hiệu ứng, nêu 2 điều kiện chặn |
| 2 | Bấm Archive Vehicle | Kiểm Lệnh chưa xong, Motor Pool đang đặt (`Xem` phần Motor Pool) |
| 3 | — | Ngắt liên kết, đóng phân công đang chạy, xoá phân công tương lai, đưa xe sang tab Archived; Status giữ nguyên |
| 4 | Mở xe Archived, bấm Restore | Chạy ngay, không hỏi; giữ trạng thái, đồng hồ, cấu hình trục |

**Nhánh:** 2a Còn Lệnh mở: E-021, xe không Archive nhưng liên kết vẫn mất (E-022), phân công tương lai còn. Phải đóng Lệnh (E-029) rồi làm lại. 4a Gói đầy: Restore khoá, không giải thích (E-023). **Không đảo ngược được:** liên kết, phân công đã mất không quay lại sau Restore, phải làm lại bằng tay.

## UC-assign-vehicle — Gán, thay người, thu hồi xe

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Mở lịch gán, Add Assignment hoặc bấm ô trống | Form có ô xe, người, thời gian; bấm ô thì xe khoá, ngày điền sẵn |
| 2 | Chọn xe, người | Chỉ hiện Operator; đủ hai ô thì hiện số km |
| 3 | Nhập thời gian, số km | Gợi ý số đầu theo đồng hồ hiện tại |
| 4 | Lưu | Kiểm trùng theo xe; đầu trang xe đổi người lái khi đang trong khoảng |
| 5 | Thu hồi: nhập ngày, số km kết thúc | Kết thúc lần gán (`Suy`) |

**Nhánh:** 2a Tên chưa có: mở Add Contact (E-003). 2b Không phải Operator: E-012; trong ô chọn chỉ có dòng Create, không báo lý do (E-030). 2c Xe Out of Service, Inactive: vẫn gán được, không cảnh báo. 4c Xe bị Archive: phân công đang chạy bị đóng, tương lai bị xoá, xem UC-archive-vehicle. 4a Trùng xe: E-001, không đóng lần cũ. 4b Người đang giữ xe khác: vẫn lưu. 6 Thay người: Edit đổi Operator, xe khoá, mất dấu người cũ trên trang chi tiết; muốn giữ lịch sử phải tự đóng và tạo mới.

## UC-log-meter — Ghi và sửa số đồng hồ

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Add Meter Entry, chọn xe | Hiện số gần nhất (có thể cũ, E-013) |
| 2 | Nhập số, ngày, có thể tick Void, lưu | Kiểm thứ tự ngày, mức một ngày, ghi nguồn Manual |
| 3 | Xem lịch sử, lọc Void Status | Số hiện tại, khoảng cách từng dòng, nguồn |

**Nhánh:** 2a Lệch ngày: E-004, E-005, từ chối. 2b Vượt mức: E-006, tự Void, dòng gốc gắn cờ E-007. 2c Cùng ngày nhỏ hơn: lưu im lặng, E-002. 3a Unvoid: Confirm, không hỏi lý do. 3b Sửa theo tài liệu hãng: Void dòng gốc, bỏ Void dòng sau (`Docs`). 3c Thay đồng hồ: chọn dòng, Actions, Void, gõ VOID; Void toàn bộ thì xe 0 km, nhập lại số bất kỳ (`Chạy`); chọn lẫn thì khoá (E-020); tên Bulk Meter Management, số GPS là `Docs`. 2d Phiếu Fleetio Go lệch thứ tự: lưu rồi tự Void Out of Sequence (E-019, một ca). 2e Xe có đồng hồ phụ: 2 ô riêng, bỏ trống Primary vẫn lưu.

## UC-tire — Đọc lốp

Đã chạy. Toàn bộ ở [[docs/_research/fleetio/srs/fleetio-tires-usecases.md|Use case Lốp]].

## UC-expense — Ghi chi phí khác, xem chi phí trên km

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Chọn xe, loại, nhà cung cấp, số tiền | — |
| 2 | Chọn một lần hoặc định kỳ, ngày, ghi chú | Định kỳ xử lý nền, sinh các khoản trong tab Future (`Chạy`) |
| 3 | Mở trang xe, chọn mốc thời gian | Cost of Ownership tính phần đã đến ngày, chia km đã chạy |

**Nhánh:** 2a Start Date chữ xám: E-011. 3a Dòng đúng hôm nay: đã tính nhưng vẫn ở tab Future, E-018.

## UC-replacement — Phân tích thay xe

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Mở trang | Hiện giả định mẫu, biểu đồ; không có ô chọn xe, không đọc dữ liệu xe (`Chạy`) |
| 2 | Sửa giả định | Vẽ lại, chỉ Minimum Cost of Ownership, Optimal Replacement (`Suy`, chưa đổi số) |

## UC-warranty — Khai bảo hành, thấy cơ hội trên lệnh

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Add Warranty, chọn một hoặc nhiều xe, Start Date, Start Meter riêng | Hiện Year, Make, Model từng xe |
| 2 | Chọn Coverage Type: Standard Warranty, Standard templates, Extended Warranty | Mở trường tương ứng |
| 3 | Nhập tên, thời hạn, quãng đường, gắn mã bảo dưỡng | Tra được mã, vd 013 ra "013 - Brakes" |
| 4 | Lưu | Tính End Date, End Meter, Status Active |
| 5 | Mở lệnh sửa của xe đó, thêm Service Task cùng mã | Warranty Opportunities (1), View Active Coverage |

**Nhánh:** 2a Chưa có mẫu đúng điều kiện: Coverage Template "No options", E-016; không phải do thiếu Make. 2b Có mẫu: Coverage preview, mỗi coverage một bảo hành. 4a Sửa mẫu đã dùng: chọn tương lai hay cả quá khứ. 3a Start Date chữ xám: E-011. 5a Phụ tùng cùng loại nhưng không có Service Task: không gợi ý. 5b Claim: chưa thử.
