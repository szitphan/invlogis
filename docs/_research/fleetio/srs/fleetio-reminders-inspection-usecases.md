---
type: research
feature: fleetio-reminders-inspection
updated: 2026-11-03
---

# Nhắc và kiểm tra — Use cases

## Use cases

| UC | Tên | Actor | FR | Màn | Lỗi | OQ |
|---|---|---|---|---|---|---|
| UC-create-reminder | Tạo nhắc bảo dưỡng | Fleet Manager | 001, 002, 003, 024 | 1.1, 1.4, 1.5 | E-008, E-009, E-010 | OQ-2 |
| UC-handle-reminder | Xử lý nhắc đến hạn | Fleet Manager | 004–008, 010, 023, 025, 026, 027, 028, 039 | 1.1, 1.5, 1.6, 1.7, 1.8, 1.9 | E-011, E-012, E-013, E-014 | OQ-16, OQ-17 |
| UC-apply-program | Áp bộ lịch | Administrator | 011, 029, 030 | 1.2, 1.10 | — | OQ-2, OQ-10, OQ-12 |
| UC-renewal | Nhắc giấy tờ | Fleet Manager | 012, 031 | 1.3, 1.11 | — | OQ-3 |
| UC-build-form | Dựng biểu mẫu | Administrator | 013–017, 021, 022, 038 | 2.1, 2.2, 2.14, 2.15, 2.5 | E-017 | OQ-1, OQ-11, OQ-15, OQ-16 |
| UC-submit-inspection | Làm phiếu kiểm tra | Operator | 018, 021, 034, 035, 036, 037 | 2.3, 2.6, 2.7, 2.8, 2.9, 2.10, 2.11, 2.12 | E-001 đến E-007, E-013, E-015, E-017, E-019 | OQ-1, OQ-4, OQ-7, OQ-14 |
| UC-handle-failure | Xử lý mục lỗi | Fleet Manager | 019, 020, 032, 033 | 2.3, 2.4, 2.13 | E-018 | OQ-4, OQ-13, OQ-14 |

Số FR, lỗi viết tắt, đầy đủ có tiền tố `fleetio-reminders-inspection`.

## UC-create-reminder — Tạo nhắc bảo dưỡng

- **Tiền điều kiện:** có xe, đầu việc.
- **Kết quả:** nhắc có trạng thái theo mốc so với hiện tại. Chưa có lịch sử và không đặt tay thì mốc km là bội số chu kỳ từ 0, có thể Overdue ngay.

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Mở form | Gợi ý dùng bộ lịch nếu nhiều xe giống nhau |
| 2 | Chọn xe, đầu việc | Hiện lần hoàn thành gần nhất, hoặc "Never logged for this vehicle" |
| 3 | Nhập chu kỳ, ngưỡng | Điền ngưỡng mặc định, hiện 5 kỳ tới, báo lỗi ngưỡng trong khối xem trước |
| 4 | Chọn thông báo, người theo dõi, lưu | Tạo nhắc, về trang chi tiết; tính tuân thủ ngầm |

**Nhánh:** 3a Đặt tay ngày hoặc số km kỳ tới: mặc định hôm nay + chu kỳ, đồng hồ hiện tại + chu kỳ. 3b Thiếu cả hai trục: E-008. 3c Ngưỡng lớn hơn hoặc bằng chu kỳ: E-009, E-010. 4a Save & Add Another.

## UC-handle-reminder — Xử lý nhắc đến hạn

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Mở danh sách, xem thẻ Overdue, Due Soon, Snoozed, tuân thủ | Đếm theo xe; sắp theo độ gấp |
| 2 | Bấm Resolve trên dòng | Mở các cách xử lý |
| 3 | Add to Work Order, tick thêm nhắc của xe | Gắn dải lệnh, trạng thái không đổi |
| 4 | Đặt lệnh Completed | Bắt Started At, số đồng hồ; sinh Service Entry |
| 5 | — | Kỳ mới từ lần làm; ghi On-Time hoặc Late |

**Nhánh:** 2a Tạm hoãn đến ngày chọn; ngày đã qua vẫn báo thành công, không có tác dụng. 2b Remove Snooze về ngay. 2c Add to service history: nhập tay hoặc Smart uploads. 2d Giao người lái (`Docs`). 2e Gửi thông báo (`Xem`). 2f Thao tác hàng loạt khi nhóm theo xe (`Docs`). 2g Sửa chu kỳ: tính lại ngay, không ghi lịch sử. 2h Void số đồng hồ sai: trạng thái lùi. 4a Thiếu dữ liệu: E-011, E-012, E-013. 4b Lần làm trễ trên một trục: Late, có thể Due Soon ngay.

## UC-apply-program — Áp bộ lịch

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Tạo bộ: tên, mẫu, đồng hồ chính, phụ | Lưu bộ |
| 2 | Thêm lịch: nhiều đầu việc, chu kỳ, Set First Service | Tự điền ngưỡng, hiện "1st service at ..., then every ..." |
| 3 | Add Vehicles | Chỉ xe cùng đơn vị; hiện bảng Conflicting, Duplicate, New Interval |
| 4 | Lưu | Xử lý ngầm; sinh nhắc mới, thay nhắc tay trùng và giữ mã (BR-004) |
| 5 | Sửa lịch trên bộ | Nhắc đang chạy đổi, kể cả trạng thái, không hỏi (BR-023) |

**Nhánh:** 3a Theo thuộc tính: Save as a Service Program Rule (`Xem`). 5a Gỡ xe: hộp xác nhận nêu xoá nhắc từ bộ, chưa bấm.

## UC-renewal — Nhắc giấy tờ

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Chọn xe hoặc liên hệ, loại, ngày đến hạn, ngưỡng | Loại đã có hiện xám; Watcher tự điền; lưu về danh sách |
| 2 | — | Trong ngưỡng là Due Soon, qua ngày là Overdue |
| 3 | Gia hạn | Sửa tay Due Date; kỳ cũ không lưu, không có Resolve, không tải giấy tờ |

## UC-build-form — Dựng biểu mẫu

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Nhập tên, chọn mẫu hoặc tải phiếu giấy, bật theo dõi vị trí, cấm ảnh có sẵn | Sinh mục; hai ô bật sẵn |
| 2 | Thêm mục từ thanh phải, đặt luật | Hiện cấu hình theo loại; Meter Entry khoá khi đã có |
| 3 | Lưu | Có workflow mặc định "ANY Failed Inspection Item → Create an issue" |
| 4 | Gán xe, đặt lịch | Xử lý ngầm; hiện tóm tắt "Daily with no reminder currently set" |

**Nhánh:** 2a Sửa mẫu đã có phiếu: phiếu cũ mang "Past Version". 3a Thêm workflow: chọn trigger, mục, action; không có action tạo lệnh. 3b Tắt workflow: mục lỗi sau đó vào Needs Action. 4a Không đặt lịch: dùng "as needed".

## UC-submit-inspection — Làm phiếu kiểm tra

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Start Inspection, chọn biểu mẫu được gán | Đã có vị trí từ lúc khởi động app; ghi giờ bắt đầu |
| 2 | Chọn xe | Hiện các mục, số km gần nhất; mục lốp tự sinh ô theo trục |
| 3 | Trả lời, ghi chú, chụp ảnh, ký | Kiểm khi nộp |
| 4 | Nộp | Sinh phiếu, gắn Job, sinh Location Entry, ghi đồng hồ, đọc lốp, chạy workflow |

**Nhánh:** 1a Không có vị trí: vẫn làm, E-007. 1b Biểu mẫu chưa gán: E-017. 2a Xe chưa khai trục: E-004, khai trong phiếu. 2b Xe thiếu lốp: "Install Tires" trong phiếu. 3a Thiếu dữ liệu: lỗi ngay tại mục, kèm E-006. 3b Rời trang: E-019, phiếu mất. 4a Vị trí bất thường: `Docs` gắn Location Exception; trên web không kích hoạt được (`Chạy (vị trí giả lập)`).

## UC-handle-failure — Xử lý mục lỗi

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Mở Item Failures, lọc theo tab | Hiện phiếu, xe, mục, biểu mẫu, dòng thời gian, Status |
| 2 | Workflow tắt: Acknowledge hoặc Create Issue | Đổi trạng thái; Acknowledged là điểm cuối |
| 3 | Workflow bật: sự cố tự sinh, thêm vào lệnh hoặc Resolve with Note | Status "WO #n", "Resolved in Issue #n" |
| 4 | Lần kiểm sau lỗi lại | Sự cố còn mở: gộp. Đã Resolved: sự cố mới, không hỏi xác nhận trên web |

**Nhánh:** 3a Thiếu Note: E-018. 4a Đạt lại khi sự cố mở: sự cố không tự đóng. 4b Xác nhận lại theo tài liệu hãng (`Docs`), chưa thấy trên web (OQ-14). 4c Reopen, Create Issue chưa bấm (OQ-13).
