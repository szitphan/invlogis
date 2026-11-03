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
| UC-handle-reminder | Xử lý nhắc đến hạn | Fleet Manager | 004–008, 010, 023, 025, 026, 027, 028, 039, 041, 042 | 1.1, 1.5, 1.6, 1.7, 1.8, 1.9, 1.13, 1.14 | E-011, E-012, E-013, E-014 | OQ-16, OQ-17 |
| UC-draft-work-order | Soạn nháp lệnh bằng AI | Fleet Manager | 040 | 1.9, 1.12 | E-030 | — |
| UC-outsource-service | Giao dịch vụ thuê ngoài | Fleet Manager | 050 | 1.9, 1.18 | E-031 | OQ-26 |
| UC-forecast | Dự báo ngày đến hạn | Administrator, Fleet Manager | 009, 051, 052 | 1.19, 1.20, 1.21, 1.22, 1.23 | E-032 | OQ-28, OQ-29, OQ-30, OQ-31, OQ-32 |
| UC-import-invoice | Nhập hoá đơn bằng Smart Upload | Fleet Manager | 027, 048, 049 | 1.16 | E-014 | OQ-27 |
| UC-apply-program | Áp bộ lịch | Administrator | 011, 029, 030, 043, 044, 045 | 1.2, 1.10 | E-024, E-025, E-026, E-029 | OQ-2, OQ-10, OQ-12, OQ-20, OQ-21 |
| UC-renewal | Nhắc giấy tờ | Fleet Manager | 012, 031, 041 | 1.3, 1.11, 1.13, 1.15 | — | OQ-3 |
| UC-build-form | Dựng biểu mẫu | Administrator | 013–017, 021, 022, 038 | 2.1, 2.2, 2.14, 2.15, 2.16, 2.5, 2.18, 2.19 | E-017, E-023, E-027 | OQ-1, OQ-11, OQ-15, OQ-16 |
| UC-submit-inspection | Làm phiếu kiểm tra | Operator | 018, 021, 022, 034, 035, 036, 037, 046, 047 | 2.3, 2.6, 2.7, 2.8, 2.9, 2.10, 2.11, 2.12, 2.17, 2.21 | E-001 đến E-007, E-013, E-015, E-017, E-019, E-020, E-021, E-022, E-028 | OQ-1, OQ-4, OQ-7, OQ-14, OQ-23, OQ-24 |
| UC-handle-failure | Xử lý mục lỗi | Fleet Manager | 019, 020, 032, 033 | 2.3, 2.4, 2.13, 2.20 | E-018 | OQ-4, OQ-14, OQ-18, OQ-22, OQ-25 |

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

**Nhánh:** 2a Tạm hoãn đến ngày chọn, từ Overdue hoặc Upcoming; ngày đã qua vẫn báo thành công, không có tác dụng. 2b Remove Snooze về ngay. 2c Add to service history: nhập tay hoặc Smart uploads. 2d Giao người lái (`Docs`), chưa thấy lối trên web. 2e Gửi thông báo (`Xem`). 2f Thao tác hàng loạt qua Actions (`Xem`). 2g Sửa chu kỳ: tính lại ngay, không hiện ở tab History, có ở Record History. 2h Void số đồng hồ sai: trạng thái lùi. 2i View Record History: ai đổi trường nào, từ giá trị nào. 2j Draft Work Order: xem UC-draft-work-order. 4a Thiếu dữ liệu: E-011, E-012, E-013. 4b Lần làm trễ trên một trục: Late, có thể Due Soon ngay. 5a Trễ trong dung sai: On-Time, chữ "behind" đỏ. 5b Ghi lùi ngày: nhận, kỳ sau từ lần làm.

## UC-draft-work-order — Soạn nháp lệnh bằng AI

- **Tiền điều kiện:** xe có nhắc đến hạn hoặc sự cố đang mở.
- **Kết quả:** bản nháp gắn với xe, người dùng chọn việc rồi thêm vào lệnh hoặc bỏ. Chưa bấm Add to.

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Resolve, Draft Work Order | Toast "Drafting service", chạy nền |
| 2 | Làm việc khác | Xong dưới 2 phút, dải "Work Order drafted" trên nhắc của xe |
| 3 | Review draft | Tóm tắt AI, nhóm Resolves, nhóm Due for maintenance, tick sẵn hết, Est. Subtotal, báo lệnh đang mở |
| 4 | Add to lệnh đang mở hoặc lệnh mới | Tự điền Repair Priority Class, Issue Date, WO Status (`Xem`) |

**Nhánh:** 1a Nhắc Upcoming: xám, E-030, khoá theo trạng thái, không theo gói. 3a Clear all, bỏ tick từng dòng. 3b Discard: không sinh lệnh. 3c Việc còn xa được tick sẵn: thêm vào lệnh rồi hoàn thành mất phần còn lại của chu kỳ (`Suy`).

## UC-outsource-service — Giao dịch vụ thuê ngoài

- **Kết quả:** gửi yêu cầu cho người được chọn. Chưa bấm Assign vì gửi email, SMS thật.

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Resolve, Find a shop | Hộp 3 bước, tick nhắc đang mở, có Assign all |
| 2 | Chọn người, When, Continue | Notification Methods tick sẵn; sang Suggest Shop rồi Confirm |
| 3 | Assign | Chưa chạy |

**Nhánh:** 2a Liên hệ không có đăng nhập: E-031. 2b Bấm ASAP: Continue khoá (OQ-26). 2c Không hiện cửa hàng ở tài khoản này.

## UC-forecast — Dự báo ngày đến hạn

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Bấm Enable Forecasting | Sang Service Reminder Settings |
| 2 | Tích Forecasting, lưu | Không hỏi xác nhận; danh sách sắp theo ngày dự báo |
| 3 | Đọc danh sách, chi tiết, popover | Ngày theo từng thuộc tính, cờ ưu tiên, phép tính từng bước |
| 4 | Nhóm theo Week, Month | Group Week ẩn cột Next Due |

**Nhánh:** 2a Số km ngày vào ngưỡng: nhắc sang Due Soon. 3a Số km ngày bằng 0: E-032. 3b Nhập tay số km ngày trên xe. 4a Nhắc không dự báo rơi vào "This Week". 5a Tắt: về nguyên trạng.

## UC-import-invoice — Nhập hoá đơn bằng Smart Upload

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | New Service Entry, tải hoá đơn | Hộp cạnh tài liệu, các ô hiện dần, dưới 30 giây |
| 2 | Rà, thêm đầu việc của nhắc nếu cần | Gộp dòng thành đầu việc hệ thống; "Add to Service Entry" khoá khi dòng mới chưa chọn đầu việc |
| 3 | Add to Service Entry, Save | Đổ vào form; lưu mới tạo phiếu, đóng nhắc nếu có đúng đầu việc |
| 4 | — | Khối Assessment chạy nền, ra "Acceptable" hoặc cần sửa |

**Nhánh:** 1a Đi từ Resolve không qua Smart Upload: thiếu ngày E-014. 3a Không có đầu việc của nhắc: nhắc không đóng. 4a Không có giá: "Add line item costs to run an assessment".

## UC-apply-program — Áp bộ lịch

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Tạo bộ: tên, mẫu, đồng hồ chính, phụ | Lưu bộ. Chọn mẫu: hiện "11 Service Reminders will be created", ẩn đồng hồ, Primary Meter "Miles" cố định |
| 2 | Thêm lịch: nhiều đầu việc, chu kỳ trên Time, Primary, Secondary, Set First Service | Tự điền ngưỡng, hiện "1st service at ..., then every ..."; chỉ đồng hồ phụ vẫn lưu được |
| 3 | Add Vehicles | Chỉ xe cùng đơn vị; hiện bảng Conflicting, Duplicate, New Interval |
| 4 | Lưu | Xử lý ngầm; sinh nhắc mới, thay nhắc tay trùng và giữ mã (BR-004) |
| 5 | Sửa lịch trên bộ | Nhắc đang chạy đổi, kể cả trạng thái, không hỏi (BR-023) |

**Nhánh:** 3a Theo thuộc tính: 28 thuộc tính; gán một lần chạy thật; Save as a Service Program Rule khoá khi còn Sample Data (E-029). 3b Current Operator: E-025, không lưu thành Rule. 3c Không khớp xe: E-026. 3d Sau gán: đầu việc của bộ xám ở form nhắc lẻ. 5a Gỡ xe: chỉ có Delete, hộp xác nhận nêu xoá nhắc từ bộ, chưa bấm.

## UC-renewal — Nhắc giấy tờ

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Chọn xe hoặc liên hệ, loại, ngày đến hạn, ngưỡng | Loại đã có hiện xám; Watcher tự điền; lưu về danh sách |
| 2 | — | Trong ngưỡng là Due Soon, qua ngày là Overdue |
| 3 | Gia hạn | Sửa tay Due Date; Status "Upcoming"; Record History ghi Next Due At, Due Soon At; không có kỳ, không có Resolve, không tải giấy tờ |

**Nhánh:** 1a Bấm dòng: panel phải xem nhanh, có Edit, "...". 3a Edit khoá Vehicle hoặc Contact và Renewal Type.

## UC-build-form — Dựng biểu mẫu

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Nhập tên, chọn mẫu hoặc tải phiếu giấy, bật theo dõi vị trí, cấm ảnh có sẵn | Sinh mục; hai ô bật sẵn |
| 2 | Thêm mục từ thanh phải, đặt luật | Hiện cấu hình theo loại; Meter Entry khoá khi đã có |
| 3 | Lưu | Có workflow mặc định "ANY Failed Inspection Item → Create an issue" |
| 4 | Gán xe, đặt lịch | Xử lý ngầm; hiện tóm tắt "Daily with no reminder currently set" |

**Nhánh:** 1a Smart Upload: hộp Processing khoá form, Review rồi Create Inspection Form; số, ô chọn, đồng hồ, ảnh thành Free Text, phải sửa tay; cờ cấm ảnh lưu lệch; treo thì E-027, Restart hoặc Discard. 2a Sửa mẫu đã có phiếu: phiếu cũ mang "Past Version". 2b Mục kho thiếu nhãn: E-023. 3a Thêm workflow: chọn trigger, mục, action; không có action tạo lệnh; Create an issue "Not Available" khi đã có workflow ANY. 3b Tắt workflow: mục lỗi sau đó vào Needs Action. 3c Trigger form submitted đổi trạng thái xe ngay khi nộp. 4a Không đặt lịch: "as needed", Schedule "Off", không vào Inspection Schedules.

## UC-submit-inspection — Làm phiếu kiểm tra

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Start Inspection, chọn biểu mẫu được gán (nhóm MOST USED, ALL) | Đã có vị trí từ lúc khởi động app; ghi giờ bắt đầu; chỉ có ô Vehicle, Save Inspection khoá |
| 2 | Chọn xe | Hiện các mục, số km gần nhất; mục lốp tự sinh ô theo trục |
| 3 | Trả lời, ghi chú, chụp ảnh, ký, chọn kho nếu có | Kiểm khi nộp |
| 4 | Nộp | Sinh phiếu, gắn Job, sinh Location Entry, ghi đồng hồ, đọc lốp, chạy workflow |

**Nhánh:** 1a Không có vị trí: vẫn làm, E-007. 1b Biểu mẫu chưa gán: E-017. 2a Xe chưa khai trục: E-004, khai trong phiếu. 2b Xe thiếu lốp: "Install Tires" trong phiếu. 2c Xe không có đồng hồ phụ: tuỳ chọn phụ bị bỏ qua; xe có: 2 ô, thiếu thì E-028. 3a Thiếu dữ liệu: lỗi ngay tại mục, kèm E-006. 3b Rời trang: E-019, phiếu mất. 3c Cờ cấm ảnh bật, không có camera: E-021, không nộp được. 3d Cờ tắt: chọn file; nộp khi đang tải: E-022. 3e Ảnh đồng hồ: luôn webcam, thiếu: E-020, Void không gỡ. 3f Kho để trống: "No parts used"; chọn phụ tùng: nộp là trừ kho ngay, không duyệt. 4a Vị trí bất thường: `Docs` gắn Location Exception; trên web không kích hoạt được (`Chạy (vị trí giả lập)`); Fleetio Go có toạ độ từng mục, ca lệch tối đa 37 m không gắn cờ (`Chạy (Fleetio Go)`). 4b Workflow form submitted, trigger đạt, trigger lỗi: xe đổi trạng thái ngay, không hỏi; mục đạt cũng kích được.

## UC-handle-failure — Xử lý mục lỗi

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Mở Item Failures, lọc theo tab | Hiện phiếu, xe, mục, biểu mẫu, dòng thời gian, Status |
| 2 | Workflow tắt: Acknowledge hoặc Create Issue | Đổi trạng thái; Acknowledged là điểm cuối |
| 3 | Workflow bật: sự cố tự sinh, thêm vào lệnh hoặc Resolve with Note | Status "WO #n", "Resolved in Issue #n" |
| 4 | Lần kiểm sau lỗi lại | Sự cố còn mở: gộp. Đã Resolved: sự cố mới, không hỏi xác nhận trên web |

**Nhánh:** 2a Create Issue: một cú bấm, không form, sang trang sự cố, người bấm là người mở. 3a Thiếu Note: E-018. 3b Reopen: không hỏi lý do, Resolution Details biến mất, Timeline không thêm dòng, dòng lỗi về Open Issue. 3c Một phiếu nhiều mục lỗi: mỗi mục một sự cố, ưu tiên khác nhau (OQ-25). 4a Đạt lại khi sự cố mở: phiếu nối với sự cố, sự cố không tự đóng. 4b Xác nhận lại theo tài liệu hãng (`Docs`), chưa thấy trên web (OQ-14).
