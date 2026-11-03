---
type: research
feature: fleetio-vehicle
updated: 2026-11-03
---

# Phương tiện — Use cases

## Use cases

| UC | Tên | Actor | FR | Màn | Lỗi | OQ |
|---|---|---|---|---|---|---|
| UC-manage-vehicle | Quản lý hồ sơ xe | Fleet Manager | 001–008, 020–026, 043, 044 | 1.1, 1.2, 1.3 | E-009, E-010 | OQ-11, OQ-16 |
| UC-assign-vehicle | Gán, thay người, thu hồi xe | Fleet Manager | 009–012, 027–029 | 2.1–2.6 | E-001, E-003, E-012, E-017 | OQ-1, OQ-7, OQ-12, OQ-13, OQ-14 |
| UC-log-meter | Ghi và sửa số đồng hồ | Fleet Manager, Operator | 013–016, 030–032, 046 | 3.1–3.4 | E-002, E-004–E-008, E-013, E-015, E-019 | OQ-2, OQ-8, OQ-9, OQ-14 |
| UC-tire | Đọc lốp | Technician | 017 | 4.1 | Xem `fleetio-tires` | OQ-3 |
| UC-expense | Ghi chi phí khác, xem chi phí trên km | Kế toán | 018, 033, 034 | 1.3, 5.1–5.3 | E-011, E-018 | — |
| UC-replacement | Phân tích thay xe | Lãnh đạo | 019, 040 | 6.1, 6.2 | — | OQ-15 |
| UC-warranty | Khai bảo hành, thấy cơ hội trên lệnh | Fleet Manager, Kỹ thuật viên | 035–039 | 7.1–7.7 | E-011, E-014, E-016 | OQ-10, OQ-14 |
| UC-recall-pool | Xem Recall, đặt xe chung | Fleet Manager | 041, 042 | Thuộc nhóm Nền tảng | — | OQ-11 |

Số FR, lỗi viết tắt, đầy đủ có tiền tố `fleetio-vehicle`. FR-045 (automation đổi trạng thái) xem nhóm Nền tảng.

## UC-manage-vehicle — Quản lý hồ sơ xe

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Tạo xe: tên, loại | Điền sẵn trạng thái, đơn vị |
| 2 | Lưu | Mở trang xe, khối trống có nút thêm |
| 3 | Bổ sung thông số qua Edit, giải mã số khung | Điền thông số |
| 4 | Dùng Add để tạo bản ghi | Xe điền sẵn |
| 5 | Đổi trạng thái, thao tác trong More Actions | Lưu lịch sử trường (`Xem`) |
| 6 | Với mooc: Type Trailer, thêm vào Linked Vehicles của đầu kéo | Hai xe hiện Linked Assets, không gộp gì khác |

**Nhánh:** 2a Hết hạn mức: E-009. 2b Trống tên: E-010. 5a Archive: tab Archived (`Xem`, chưa chạy).

## UC-assign-vehicle — Gán, thay người, thu hồi xe

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Mở lịch gán, Add Assignment hoặc bấm ô trống | Form có ô xe, người, thời gian; bấm ô thì xe khoá, ngày điền sẵn |
| 2 | Chọn xe, người | Chỉ hiện Operator; đủ hai ô thì hiện số km |
| 3 | Nhập thời gian, số km | Gợi ý số đầu theo đồng hồ hiện tại |
| 4 | Lưu | Kiểm trùng theo xe; đầu trang xe đổi người lái khi đang trong khoảng |
| 5 | Thu hồi: nhập ngày, số km kết thúc | Kết thúc lần gán (`Suy`) |

**Nhánh:** 2a Tên chưa có: mở Add Contact (E-003). 2b Không phải Operator: E-012. 4a Trùng xe: E-001, không đóng lần cũ. 4b Người đang giữ xe khác: vẫn lưu. 6 Thay người: Edit đổi Operator, xe khoá, mất dấu người cũ trên trang chi tiết; muốn giữ lịch sử phải tự đóng và tạo mới.

## UC-log-meter — Ghi và sửa số đồng hồ

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Add Meter Entry, chọn xe | Hiện số gần nhất (có thể cũ, E-013) |
| 2 | Nhập số, ngày, có thể tick Void, lưu | Kiểm thứ tự ngày, mức một ngày, ghi nguồn Manual |
| 3 | Xem lịch sử, lọc Void Status | Số hiện tại, khoảng cách từng dòng, nguồn |

**Nhánh:** 2a Lệch ngày: E-004, E-005, từ chối. 2b Vượt mức: E-006, tự Void, dòng gốc gắn cờ E-007. 2c Cùng ngày nhỏ hơn: lưu im lặng, E-002. 3a Unvoid: Confirm, không hỏi lý do. 3b Sửa theo tài liệu hãng: Void dòng gốc, bỏ Void dòng sau (`Docs`). 3c Thay đồng hồ: Bulk Meter Management (`Docs`).

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

**Nhánh:** 2a Xe không Make, Model: Coverage Template "No options", E-016 (nhân quả chưa kiểm chứng). 3a Start Date chữ xám: E-011. 5a Phụ tùng cùng loại nhưng không có Service Task: không gợi ý. 5b Claim: chưa thử.
