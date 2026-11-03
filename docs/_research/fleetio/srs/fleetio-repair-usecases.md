---
type: research
feature: fleetio-repair
updated: 2026-11-03
---

# Sửa chữa — Use cases

## Use cases

| UC | Tên | Actor | FR | Màn | Lỗi | OQ |
|---|---|---|---|---|---|---|
| UC-report-issue | Báo sự cố | Operator, Fleet Manager | 001, 002, 005, 019 | 1.1, 1.2 | E-003 | OQ-1 |
| UC-resolve-issue | Xử lý sự cố | Fleet Manager | 003, 004, 026, 027, 028, 031, 039 | 1.2, 1.3, 1.4 đến 1.8, 1.11, 1.12, 1.13 | E-012 | OQ-1, OQ-15 |
| UC-ai-draft | AI soạn lệnh | Fleet Manager | 020 | 1.9, 1.10, 2.8, 2.9, 2.10 | E-017 | OQ-14 |
| UC-run-work-order | Thực hiện lệnh | Technician, Fleet Manager | 006–011, 015, 017, 029, 030, 032, 033, 037, 038, 040 | 2.1–2.7, 2.15 đến 2.17 | E-001, E-005, E-008, E-009, E-010, E-011, E-014, E-015, E-016, E-018 | OQ-2, OQ-11, OQ-18 |
| UC-complete-work-order | Hoàn thành lệnh | Fleet Manager | 012, 021 | 2.3, 2.11, 2.14, 3.1, 3.2 | E-002, E-004, E-006, E-007 | OQ-13 |
| UC-reopen-work-order | Mở lại lệnh | Fleet Manager | 013, 034 | 2.3, 2.11, 2.12, 3.3 | — | OQ-3, OQ-10, OQ-13 |
| UC-log-service | Ghi lịch sử trực tiếp | Fleet Manager | 014, 022, 028 | 3.1, 3.2 | E-012 | OQ-7 |
| UC-copy-work-order | Sao chép, in lệnh | Fleet Manager | 018 | 2.13 | — | — |
| UC-manage-service-task | Quản lý đầu việc | Administrator | 016, 041 | 5.1 | E-013 | — |
| UC-track-warranty | Theo dõi bảo hành | Fleet Manager | 025, 038 | 6.1 đến 6.7, 2.16, 2.17 | — | OQ-9, OQ-16 |
| UC-configure-maintenance | Cấu hình bảo dưỡng | Administrator | 035, 036 | 7.1 | — | OQ-16 |

Số FR, lỗi viết tắt, đầy đủ là `FR-fleetio-repair-NNN`, `E-fleetio-repair-NNN`.

## UC-report-issue — Báo sự cố

- **Mục tiêu:** ghi nhận vấn đề của xe.
- **Tiền điều kiện:** có xe; người dùng có quyền tạo sự cố.
- **Kết quả:** sự cố Open, có người báo, thời điểm, ưu tiên nếu AI gán.

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Mở form từ danh sách, trang xe hoặc nút tạo nhanh | Điền người báo, giờ hiện tại; ưu tiên Auto-assign |
| 2 | Chọn xe, nhập tóm tắt, mô tả, nhãn, người nhận, hạn ngày, hạn đồng hồ | Tìm xe theo tên, hiện trạng thái |
| 3 | Lưu | Tạo sự cố Open, số tăng dần, AI gán ưu tiên, người tạo thành người theo dõi |

**Nhánh:** 2a Chọn mức ưu tiên tay thì AI không gán (`Suy`). 2b Hạn đã qua: lưu được, hiện Overdue, không cảnh báo (`Chạy`). 3a Lần đầu hiện gợi ý mẫu "Create A Work Order When An Issue Is Created". 3b Thiếu dữ liệu: E-fleetio-repair-003. 3c AI có thể để "No Priority" (`Chạy`). 3d Sau khi lưu, đồng hồ vượt hạn thì tự hiện Overdue, không ai thao tác (`Chạy`).

## UC-resolve-issue — Xử lý sự cố

- **Tiền điều kiện:** sự cố Open hoặc Overdue.
- **Kết quả:** sự cố có đường xử lý, hoặc đã đóng.

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Mở sự cố, chọn Resolve | Hiện 5 cách; sự cố đã gắn lệnh thì 3 cách khoá kèm tooltip |
| 2 | Chọn cách | Mở hộp hoặc form tương ứng, điền sẵn xe, sự cố |
| 3 | Hoàn tất | Cập nhật Timeline, Resolution Details khi đã giải quyết |

**Nhánh:**

- 2a Resolve with Note: Note bắt buộc, nút khoá khi trống; ghi chú vào Resolution Details (`Chạy`).
- 2b Close từ menu ba chấm: Note tuỳ chọn, ghi chú thành Comment; không tính vào chỉ số (`Chạy`, chỉ số `Docs`).
- 2c Bulk: chọn nhiều sự cố thêm vào một lệnh (`Xem`). Trên hộp Add to Service Entry cũng chọn được nhiều sự cố (`Chạy`).
- 2d Add to Service Entry: chuyển sang UC-log-service (`Chạy`).
- 2e Add to Work Order: mở tab mới, điền sẵn xe, sự cố (`Chạy`).
- 2f Get Service at Shop: hộp giới thiệu, cần bật Shop Network (`Xem`).
- 4a Reopen: chạy được với sự cố đóng, giải quyết bằng ghi chú, bằng entry; khoá với sự cố giải quyết bằng lệnh (`Chạy`).

## UC-ai-draft — AI soạn lệnh

- **Tiền điều kiện:** có sự cố mở; AI bật. Trên nhắc mục này xám ở tài khoản dùng thử (`Chạy` nhóm Nhắc).
- **Kết quả:** lệnh Open với đầu việc do người dùng chọn.

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Chọn Draft Work Order | Hiện dải "Drafting service for this issue", đổi chữ tiến độ |
| 2 | Làm việc khác | Chạy nền khoảng 40 giây, báo "Work Order drafted" |
| 3 | Review draft | Hiện cảnh báo lệnh đang mở, lý do, đầu việc có tick, gom sự cố cùng xe, ước tính, phần tự điền |
| 4 | Bỏ tick việc thừa, Create new Work Order | Tạo lệnh, gắn sự cố được chọn, tự xếp mã phân loại, thông báo kèm nút phản hồi |

**Nhánh:** 4a Discard: mất ngay, không hỏi, không vết. 3a Không có ước tính: "No estimate available". 4b Add to Work Order đang mở: thấy menu, chưa bấm (`Xem`). 4c Bỏ tick việc của sự cố khác: sự cố đó không vào lệnh (`Chạy`). 4d Phân loại ưu tiên hứa tự điền nhưng trống: E-fleetio-repair-017.

## UC-run-work-order — Thực hiện lệnh

- **Tiền điều kiện:** lệnh chưa hoàn thành.

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Mở sửa lệnh | Hiện sự cố của xe, dòng việc, nhắc liên quan; số lệnh là số dự kiến |
| 2 | Thêm đầu việc, công, phụ tùng | Đề xuất phụ tùng kèm tồn từng kho; đơn giá công theo contact; cộng tiền |
| 3 | Nhập số đồng hồ, ngày | Kiểm chéo |
| 4 | Lưu | Trừ kho nếu chọn kho; ghi sổ đồng hồ; số lệnh tự nhảy nếu đã có người lưu trước |

**Nhánh:** 3a Có số đầu, thiếu ngày: E-fleetio-repair-001. 3b Có số cuối, thiếu ngày hoàn thành: E-fleetio-repair-008. 3c Số cuối nhỏ hơn đầu: E-fleetio-repair-009. 3d Số đầu xếp sau dòng đồng hồ cùng thời điểm: E-fleetio-repair-018. 2a Phụ tùng không qua kho: chọn "None". 2b Vượt tồn: không báo, E-fleetio-repair-015. 2c Xoá dòng phụ tùng: xác nhận, hoàn tồn có sổ. 2d Contact mẫu trên xe thường: lưu được lần đầu, về sau E-fleetio-repair-010, E-fleetio-repair-011. 2e Tick sự cố không vào: E-fleetio-repair-016. 2f Tick lại sự cố đã ở lệnh khác: có ổ khoá, phải gỡ trước. 2g Hàng nhận từ đơn mua vào lệnh: cộng kho rồi trừ khi lưu. 4a Đổi Pending khi chờ hàng, không hỏi. 4b Sau lưu, chi tiết lệnh hiện tiền phụ tùng gấp 100 lần: E-fleetio-repair-005. 4c Có bảo hành khớp mã đầu việc: khối Warranty Opportunities hiện cơ hội. 4d Giao việc: lưu không hỏi, không kiểm được có báo người nhận không.

## UC-complete-work-order — Hoàn thành lệnh

- **Tiền điều kiện:** đủ luật cấu hình.
- **Kết quả:** lệnh khoá; Service Entry mới; sự cố Resolved; nhắc tính lại; không ghi sổ kho.

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Nhập số cuối, ngày xong, hoặc giữ tick dùng số đầu | Tính thời lượng |
| 2 | Đổi trạng thái Completed, từ Open hoặc thẳng từ Pending | Kiểm luật |
| 3 | — | Sinh Service Entry, giải quyết sự cố, ghi đồng hồ, khoá sửa, khoá Reopen của sự cố |

**Nhánh:** 2a Thiếu Started At: E-fleetio-repair-006. 2b Thiếu đồng hồ đầu: E-fleetio-repair-007. 2c Thiếu số cuối: E-fleetio-repair-002. 3a Chạy Assessment: có kết quả, có nguồn; đổi lệnh sau đó thì hiện "Rerun available"; thiếu điều kiện: E-fleetio-repair-004. 3b Service Entry phải bấm Run Assessment, không tự chạy.

## UC-reopen-work-order — Mở lại lệnh

`Chạy` #104.

- **Tiền điều kiện:** lệnh Completed.
- **Kết quả:** lệnh chưa xong, Service Entry bị xoá, sự cố Open; đồng hồ, tồn giữ nguyên.

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Đổi về Open hoặc Pending | Hộp "Update Status" chỉ nêu khôi phục dữ liệu archive |
| 2 | Confirm | Xoá Service Entry; sự cố về Open, xoá dòng Timeline; khôi phục chạy nền, vài giây trang vẫn Completed |
| 3 | Sửa lệnh | Sửa, xoá dòng phụ tùng ghi bù kho |
| 4 | Hoàn thành lại | Sinh Service Entry mới số khác; dùng ngày, đồng hồ cũ; thêm dòng đồng hồ trùng |

**Nhánh:** 1a Cancel: giữ Completed (`Suy`, nút có trên hộp). 4a Hai lượt không thấy giới hạn số lần.

## UC-log-service — Ghi lịch sử trực tiếp

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Tạo Service Entry, chọn sự cố mở, hoặc đi từ sự cố | Hiện nhắc liên quan; từ sự cố thì tick sẵn, toast "1 Issue(s) were added to the form" |
| 2 | Nhập Odometer, Completion Date, đầu việc, chi phí, xưởng, tải chứng từ bằng Smart Upload | Đọc chứng từ (`Xem` nút, chưa chạy) |
| 3 | Lưu | Sự cố Resolved; nhắc cập nhật (`Docs`); AI có thể đóng sự cố khớp (`Docs`) |

**Nhánh:** 2a Không gõ ngày: E-fleetio-repair-012. 2b Số đồng hồ thấp hơn hiện tại: lưu, không cảnh báo, số hiện tại không đổi (`Chạy`). 2c Không có dòng việc: vẫn lưu, vẫn giải quyết sự cố (`Chạy`). 3a Sau đó Reopen sự cố: entry còn, mất liên kết (`Chạy`). 1a Add to Existing Service Entry: thấy, chưa lưu (`Xem`).

## UC-copy-work-order — Sao chép, in lệnh

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | More Actions, Make a Copy | Form mới, xe trống, Open, Issue Date hiện tại |
| 2 | Chọn xe | Chép dòng việc, dòng công; không chép sự cố, ngày, đồng hồ |
| 3 | Lưu | Có số lệnh mới |

**Nhánh:** 1a Print: PDF tab mới (`Chạy`). 1b Email PDF: chưa bấm (`Xem`).

## UC-manage-service-task — Quản lý đầu việc

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Tạo đầu việc | Form 6 bước gập; Save khoá tới khi Continue hết |
| 2 | Nhập tên, mã, giờ công, phụ tùng | Gợi ý Fleetio Recommendations; tên lạ thì "No Service Task Recommendation" |
| 3 | Lưu | Đầu việc Active |

**Nhánh:** 3a Trùng tên: E-fleetio-repair-013. 4 Archive: hộp xác nhận, cập nhật nền. Gộp đầu việc: không thấy (`Xem`).

## UC-track-warranty — Theo dõi bảo hành

`Chạy` ở nhóm Phương tiện.

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Add Warranty, chọn nhiều xe, mỗi xe một Start Date, Start Meter | Hiện Year, Make, Model |
| 2 | Chọn Standard, Standard templates hoặc Extended; nhập thời hạn, số km, mã phân loại | Tự tính End Date, End Meter |
| 3 | Lưu | "Warranties have been successfully created", Status Active |
| 4 | Thêm đầu việc cùng mã vào lệnh | "Warranty Opportunities (1)" |

**Nhánh:** 2a Xe không có Make, Model: Coverage Template "No options" (`Xem`, lý do chưa kiểm). 4a Chỉ có phụ tùng cùng hệ thống: không có cơ hội. 4b Nút claim: chưa thử.

## UC-configure-maintenance — Cấu hình bảo dưỡng

`Xem`, không đổi cài đặt.

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Mở Maintenance Settings | Enable Work Orders, Next Work Order Number, Require a Meter Reading, các luật bắt buộc |
| 2 | Mở Work Order Statuses | Open, Pending, Completed với Name, Type, số lệnh |
