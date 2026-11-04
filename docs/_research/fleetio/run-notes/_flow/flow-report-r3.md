# Nối flow 59 màn mới Fleetio (lượt 3-5)

Ngày 2026-11-03. File `FifpyOMpZk9OP8qyNzbRVJ`, trang `Research · Fleetio` (7214:221223). Nguồn: Mục 1, 2, 3 của `srs/fleetio-<nhóm>-userflow.md`, `run-notes/*.md`.

Cách nối: Plugin API `setReactionsAsync`, đọc reaction hiện có rồi thêm 1 ON_CLICK NAVIGATE, `transition: null`. Không dùng `setReactions` của reqwise. Mỗi lần ghi đều đối chiếu lại: reaction cũ giữ nguyên, số lượng tăng đúng 1. Không ghi đè click nào.

## Kết quả kiểm bằng máy

| Mục | Trước | Sau |
|---|---|---|
| Tổng reaction, 239 frame màn | 8210 | 8301 (+91, đúng số đường đã nối) |
| Frame cũ (180) | 6578 | 6614 (+36, không giảm) |
| Frame mới (59) | 1632 | 1687 (+55) |
| Reaction trỏ node không tồn tại | | 0 (kiểm 191 đích) |
| Lỗi ghi, lỗi đối chiếu | | 0/91 |
| Điểm bắt đầu flow | 64 | 64 (không đổi) |

Số "Trước" của frame cũ và frame mới tính từ bản quét đầu lượt. Hover, press của 91 node đã ghi được đối chiếu từng node. Chưa bấm thử Present.

Đường vào, đường ra dưới đây không tính menu bên, Menu bổ sung và đường tự trỏ. Trong 59 frame: 39 có đường vào, 41 có đường ra, 7 không có cả hai.

## Đường đã nối: 91


### Phương tiện

| Từ | Đến | Nút | Kết quả |
|---|---|---|---|
| 1.1 vehicle-detail | 1.5 vehicle-status-history | Trạng thái Đang dùng (2 huy hiệu) | Đã nối. Tài liệu không nói nút cụ thể, chọn huy hiệu trạng thái |
| 1.5 vehicle-status-history | 1.1 vehicle-detail | Đóng | Đã nối |
| 1.1 vehicle-detail | 1.9 vehicle-manage-overview-layout | Tuỳ chỉnh bố cục | Đã nối |
| 1.9 vehicle-manage-overview-layout | 1.1 vehicle-detail | Áp dụng thay đổi; Huỷ | Đã nối 2 |
| 1.3 vehicle-cost-of-ownership | 1.7 trailer-linked-two-vehicles | Chữ TEST-MOOC-LOP, khối Xe liên kết | Đã nối |
| 1.7 trailer-linked-two-vehicles | 1.1 vehicle-detail | Dòng TEST-XE-01 | Đã nối. Dòng TEST-XE-LOP không nối vì màn đích là TEST-XE-01 |
| 1.2 vehicle-more-actions | 1.10 vehicle-service-programs-empty | Mục Quản lý bộ lịch bảo dưỡng | Đã nối |
| 1.2 vehicle-more-actions | 1.11 vehicle-attach-shared-document | Mục Đính kèm tài liệu dùng chung | Đã nối |
| 1.2 vehicle-more-actions | 1.6 vehicle-archive-confirm | Mục Lưu trữ | Đã nối |
| 1.10 vehicle-service-programs-empty | 1.1 vehicle-detail | Tab Tổng quan | Đã nối |
| 1.11 vehicle-attach-shared-document | 1.1 vehicle-detail | Huỷ; Đính tài liệu dùng chung | Đã nối 2 |
| 1.6 vehicle-archive-confirm | 1.1 vehicle-detail | Huỷ | Đã nối |
| 3.1 meter-history | 3.6 meter-bulk-void-secondary | Thao tác khác | Đã nối |
| 3.6 meter-bulk-void-secondary | 3.1 meter-history | Thêm số đồng hồ | Đã nối ("Nhập số mới") |
| 3.6 meter-bulk-void-secondary | 3.5 meter-out-of-sequence-autovoid | Trạng thái Tự vô hiệu (2 dòng) | Suy luận, user đã duyệt giữ. Tài liệu ghi nguồn là 3.1, nhưng 3.1 không có huy hiệu này; nối theo quy tắc hộp thoại mở từ màn nền |

### Nhắc, kiểm tra

| Từ | Đến | Nút | Kết quả |
|---|---|---|---|
| 1.1 reminders-list | 1.5 reminder-detail-overdue | Dòng đầu (layer tên "Header row" nhưng chứa dữ liệu) | Đã nối |
| 1.1 reminders-list | 1.9 reminder-resolve | Xử lý ở dòng đầu | Đã nối |
| 1.5 reminder-detail-overdue | 1.9 reminder-resolve | Xử lý | Đã nối |
| 1.5 reminder-detail-overdue | 1.14 reminder-compliance-multi | Tab Lịch sử | Đã nối |
| 1.8 reminder-snooze | 1.5 reminder-detail-overdue | Huỷ; Đóng | Đã nối 2 |
| 1.9 reminder-resolve | 1.12 reminder-draft-work-order | Mục Soạn nháp lệnh sửa chữa | Đã nối |
| 1.9 reminder-resolve | 3.1 service-entry | Mục Thêm vào lịch sử dịch vụ | Đã nối |
| 1.12 reminder-draft-work-order | 1.5 reminder-detail-overdue | Bỏ nháp; Đóng | Đã nối 2 |
| 1.13 reminder-record-history | 1.5 reminder-detail-overdue | Đóng | Đã nối |
| 1.2 program-new | 1.10 program-vehicles-add | Lưu bộ lịch bảo dưỡng (2 nút) | Đã nối |
| 1.3 renewals-list | 1.11 renewal-new | Thêm nhắc gia hạn xe | Đã nối |
| 1.11 renewal-new | 1.3 renewals-list | Lưu nhắc gia hạn xe | Đã nối |
| 2.19 inspection-form-smart-upload-review | 2.1 inspection-form | Tạo biểu mẫu kiểm tra | Đã nối |
| 2.1 inspection-form | 2.14 inspection-workflow-add | Tab Quy trình | Đã nối |
| 2.1 inspection-form | 2.15 inspection-form-vehicles | Tab Xe và lịch | Đã nối |
| 2.14 inspection-workflow-add | 2.1 inspection-form | Huỷ | Đã nối |
| 2.5 inspection-schedules | 2.6 inspection-submit-form | Bắt đầu kiểm tra | Đã nối |
| 2.16 inspection-schedule-due-soon | 2.6 inspection-submit-form | Bắt đầu kiểm tra | Đã nối |
| 2.6 inspection-submit-form | 2.17 inspection-photo-webcam-only | Chọn tệp | Đã nối |
| 2.17 inspection-photo-webcam-only | 2.6 inspection-submit-form | Đóng | Đã nối |
| 2.6 inspection-submit-form | 2.3 inspection-submission | Lưu phiếu kiểm tra | Đã nối, nhánh Đạt |
| 2.7 inspection-tire-axle-error | 2.6 inspection-submit-form | Xong | Đã nối |
| 2.8 inspection-tire-remark-required | 2.6 inspection-submit-form | Thêm nhận xét (3 mục) | Đã nối |
| 2.3 inspection-submission | 2.20 inspection-workflow-fail-issues | Chữ TEST-XE-01 | Đã nối ("xem trên xe") |
| 2.20 inspection-workflow-fail-issues | 2.4 item-failures | Dòng đầu | Đã nối |
| 1.19 reminder-forecast-next-due-popover | 1.20 reminder-forecast-meter-popover | Dòng TEST-NHAC-B | Đã nối |
| 1.19 reminder-forecast-next-due-popover | 1.21 reminder-forecast-group-week | Nhóm: Không | Đã nối |
| 1.21 reminder-forecast-group-week | 1.19 reminder-forecast-next-due-popover | Nhóm: Tuần | Đã nối |
| 1.16 service-smart-upload-review | 3.1 service-entry | Đóng; Huỷ bỏ | Đã nối 2 |

### Kho, sửa chữa

| Từ | Đến | Nút | Kết quả |
|---|---|---|---|
| 2.8 po-closed-partial | 2.9 po-adjust-closed | Thêm | Đã nối. Menu chưa vẽ, chỉ một đích có tài liệu trên màn này |
| 2.9 po-adjust-closed | 2.8 po-closed-partial | Đóng hộp; Đóng; Thực hiện điều chỉnh | Đã nối 3 |
| 2.10 po-record-history | 2.1 po-detail | Đóng hộp | Đã nối |
| 3.2 fuel-list | 3.5 fuel-filter-alert-type | Bộ lọc (1) | Đã nối |
| 3.5 fuel-filter-alert-type | 3.2 fuel-list | Đóng | Đã nối |
| 3.5 fuel-filter-alert-type | 3.1 fuel-entry | Dòng đầu | Đã nối |
| 6.9 warranty-template-list | 1.8 settings-valuation-fifo-permanent-warning | Mục Phương pháp tính giá tồn | Đã nối. 4.1 maintenance-settings không có mục này |
| 1.8 issue-shop-network | 1.15 shop-network-enable-denied | Bật Shop Network | Đã nối |
| 2.17 wo-warranty-opportunity | 2.18 wo-warranty-claim-fields | Ô Nguyên nhân | Suy luận, user đã duyệt giữ. Tài liệu ghi "Điền ba ô chữ", nút Sửa đang trỏ 2.2 wo-edit nên đi qua ô Nguyên nhân |
| 2.17 wo-warranty-opportunity | 6.8 vehicle-warranties-tab | Xem bảo hành đang dùng | Đã nối |
| 4.1 maintenance-settings | 4.2 fault-rules | Mục Quy tắc mã lỗi | Đã nối |
| 4.1 maintenance-settings | 6.9 warranty-template-list | Mục Mẫu bảo hành | Đã nối |
| 4.1 maintenance-settings | 7.2 wo-status-custom-list | Mục Trạng thái lệnh sửa chữa | Đã nối |
| 6.4 warranty-new-template | 6.10 warranty-template-preview | Ô chọn Mẫu phạm vi bảo hành | Đã nối, happy path Mục 3 |
| 6.10 warranty-template-preview | 6.7 warranty-list | Lưu bảo hành (2 nút) | Đã nối |
| 6.11 warranty-oem-template-preview | 6.4 warranty-new-template | Huỷ (2 nút) | Đã nối |
| 6.9 warranty-template-list | 6.12 warranty-template-change | Dòng mẫu | Đã nối |
| 6.12 warranty-template-change | 6.9 warranty-template-list | Đồng ý; Huỷ; Đóng | Đã nối 3 |

### Nền tảng

| Từ | Đến | Nút | Kết quả |
|---|---|---|---|
| 2.1 reports | 2.6 report-expense-entries-500 | Thẻ Chi phí theo xe | Đã nối |
| 2.6 report-expense-entries-500 | 2.1 reports | Chữ Quay lại | Đã nối |
| 2.3 ai-analyst-issues | 2.7 ai-analyst-vehicle-not-exist | Gửi | Đã nối |
| 3.4 automation-detail | 3.10 automation-version-v1-lech | Khối Phiên bản hiện tại | Suy luận, user đã duyệt giữ. Tài liệu không nói nút cụ thể |
| 3.10 automation-version-v1-lech | 3.4 automation-detail | Quay lại | Đã nối |
| 3.11 automation-run-failure | 3.5 automation-run-history | Quay lại | Đã nối |
| 3.12 automation-vehicle-status-flip | 1.1 vehicle-detail | Đóng | Đã nối theo quy tắc hộp thoại về màn nền |
| 5.6 record-history-issue | 1.2 issue-open | Đóng | Đã nối |
| 1.1 dashboard | 5.7 notifications-inbox | Chuông (Notifications) | Đã nối |
| 5.5 documents-empty | 5.8 documents-list-file | Tải tài liệu lên (2 nút) | Đã nối |
| 5.13 reservation-validation | 5.4 motor-pool-reservations | Huỷ; Đóng | Đã nối 2 |

## Đường nối theo suy luận (user đã duyệt giữ)

Ba đường này không có nút ghi rõ trong tài liệu:

- 3.6 meter-bulk-void-secondary → 3.5 meter-out-of-sequence-autovoid, qua huy hiệu Tự vô hiệu.
- 2.17 wo-warranty-opportunity → 2.18 wo-warranty-claim-fields, qua ô Nguyên nhân.
- 3.4 automation-detail → 3.10 automation-version-v1-lech, qua khối Phiên bản hiện tại.

## Đã có sẵn, không ghi

- 2.18 wo-warranty-claim-fields, Lưu lệnh sửa chữa → 2.3 wo-detail.
- 2.11 po-edit-purchased, Lưu và duyệt → 2.1 po-detail.

## Đường không nối được

### Xung đột với click có sẵn: đã xử lý

Nút Sửa (7226:251708) của 2.1 po-detail từng trỏ 2.6 po-edit-received-partial, tài liệu cần 2.11 po-edit-purchased. User duyệt đổi đích sang 2.11. Sau khi ghi, nút vẫn có 3 reaction, hover và press không đổi, click trỏ 7332:440965. Tổng reaction vẫn 8301, không có reaction hỏng. 2.6 còn đường vào từ nút Sửa của 2.9 và 2.10.

### Màn đích hoặc màn nguồn chưa có

| Đường trong tài liệu | Màn chưa có |
|---|---|
| Danh sách xe → 1.8 vehicle-add-multiple-step1, chiều về (Lưu), và Huỷ | Danh sách xe |
| 1.8 vehicle-add-multiple-step1 ↔ E-025 | E-025 |
| Form thêm xe ↔ 1.4 vin-decode-review | Form thêm xe |
| 1.6 vehicle-archive-confirm → E-021, E-022; → Xe đã lưu trữ | Cả hai màn |
| 1.9 reminder-resolve → Tìm xưởng 1.18 reminder-find-shop, chiều về | 1.18 |
| Cài đặt nhắc 1.23 reminder-settings-forecasting → 1.19 | 1.23 |
| 1.15 contact-renewal-panel → 1.13 reminder-record-history | 1.15 contact-renewal-panel |
| 2.18 inspection-smart-upload → 2.19; Đóng, Huỷ bỏ của 2.19 về màn nền | 2.18 |
| 2.6 → E-017 → 2.15; 2.6 ↔ E-007; E-006 → 2.6 | Các màn lỗi E |
| Hộp thêm vào phiếu dịch vụ → 1.14 issue-resolved-negative-ttr | Hộp này |
| 2.7 ai-analyst-vehicle-not-exist, 5.7 notifications-inbox → Chi tiết bản ghi | Node chung, không có frame |
| 5.8 documents-list-file ↔ document-detail | document-detail |
| Danh sách nhóm xe → 5.12 motor-pool-add; Lưu, Huỷ, Đóng về nền | Danh sách nhóm xe, 4.1 maintenance-settings không có mục này |
| vehicle-reservation-form → 5.13 reservation-validation | Form đặt xe |

### Đích không xác định

| Đường | Lý do |
|---|---|
| 1.9 Thêm vào lệnh sửa chữa → Lệnh sửa chữa | Node `wo` chung; ghi chú nói mở hộp chọn lệnh mới hoặc lệnh có sẵn, hộp chưa vẽ |
| 1.12 Thêm vào → Lệnh sửa chữa | Như trên, tài liệu ghi chưa bấm |

### Một nút nhiều đích (menu chưa vẽ)

| Màn | Nút | Các đích |
|---|---|---|
| 1.5 reminder-detail-overdue | Thêm | 1.8 reminder-snooze, 1.13 reminder-record-history |
| 2.1 po-detail | Thêm | 2.10 po-record-history, 2.12 po-print-pdf |
| 2.3 wo-detail | Thêm | 2.19 wo-print-pdf, cùng các mục cũ chưa nối |
| 1.2 issue-open | Thêm | 5.6 record-history-issue, cùng các mục cũ chưa nối |
| 6.4 warranty-new-template | Ô chọn mẫu | 6.10 (đã nối), 6.11 warranty-oem-template-preview (phụ thuộc xe, không nối) |

### Không có control trên màn

| Đường | Lý do |
|---|---|
| 3.1 meter-history → 3.5 | 3.1 không có huy hiệu Tự vô hiệu |
| 3.5 meter-out-of-sequence-autovoid → 3.1 (Đóng) | Popup không vẽ nút đóng |
| 2.15 inspection-form-vehicles → 2.5 (Lưu) | Màn không có nút Lưu |
| 2.14 inspection-workflow-add → 2.1 (Lưu) | Bước 1 chỉ có Huỷ, Tiếp tục. Huỷ đã nối |
| 1.19 → 1.22 (chọn nhắc usage 0) | Bảng 1.19 không có dòng TEST-NHAC-G |
| 1.20, 1.22 → 1.19 (Quay lại) | Không có nút quay lại |
| 3.1 service-entry → 1.16 (Tải hoá đơn) | Màn không có nút tải |
| 1.15 shop-network-enable-denied → 1.8 | Màn chỉ có thông báo |
| 1.14 issue-resolved-negative-ttr → 1.2 | Thao tác nằm trong phiếu dịch vụ, không có control |
| 3.5 automation-run-history → 3.11 | Bảng chỉ có dòng Thành công |
| 3.3 automation-list-data → 3.12; 3.12 → 1.2 | Không có control tương ứng |
| 4.1 faults → 4.2 (View Fault Rule) | Không có nút. 4.2 đã có đường vào từ menu cài đặt |
| 2.19 wo-print-pdf → 2.3; 2.12 po-print-pdf | Trang PDF, không có control |

### Hệ thống tự chuyển, không có nút

- 2.5 → 2.16 (sang ngày tài khoản).
- 2.6 → 2.7, 2.8 (điều kiện dữ liệu).
- 2.3 → 2.21 (có chọn phụ tùng thì trừ kho).
- 3.1 service-entry → 1.14, 1.17 (lần hoàn thành tiếp theo).
- 1.14, 1.17 → 1.1 reminders-list (kỳ mới).

## Frame không có đường vào: 20

1.22 reminder-forecast-not-available · 6.11 warranty-oem-template-preview · 5.12 motor-pool-add · 5.13 reservation-validation · 2.19 inspection-form-smart-upload-review · 2.21 inspection-inventory-adjustment-deduct · 2.16 inspection-schedule-due-soon · 1.17 reminder-compliance-km-boundary · 1.13 reminder-record-history · 1.8 reminder-snooze · 1.16 service-smart-upload-review · 3.11 automation-run-failure · 3.12 automation-vehicle-status-flip · 5.6 record-history-issue · 1.8 vehicle-add-multiple-step1 · 1.4 vin-decode-review · 2.12 po-print-pdf · 2.10 po-record-history · 1.14 issue-resolved-negative-ttr · 2.19 wo-print-pdf

## Frame không có đường ra: 18

1.8 settings-valuation-fifo-permanent-warning · 1.20 reminder-forecast-meter-popover · 1.22 reminder-forecast-not-available · 1.15 shop-network-enable-denied · 7.2 wo-status-custom-list · 5.12 motor-pool-add · 2.15 inspection-form-vehicles · 2.21 inspection-inventory-adjustment-deduct · 1.10 program-vehicles-add · 1.17 reminder-compliance-km-boundary · 1.14 reminder-compliance-multi · 2.7 ai-analyst-vehicle-not-exist · 5.8 documents-list-file · 3.5 meter-out-of-sequence-autovoid · 1.8 vehicle-add-multiple-step1 · 2.12 po-print-pdf · 4.2 fault-rules · 2.19 wo-print-pdf

Không vào, không ra (7): 1.22 reminder-forecast-not-available, 5.12 motor-pool-add, 2.21 inspection-inventory-adjustment-deduct, 1.17 reminder-compliance-km-boundary, 1.8 vehicle-add-multiple-step1, 2.12 po-print-pdf, 2.19 wo-print-pdf.

## Frame userflow

Không đụng. Spec của 7 frame userflow chưa có hộp màn mới, còn thêm hộp rồi chạy `linkScreens` là vẽ lại frame và từng khớp nhầm (2.1 wo-list sang Calendar). Không chứng minh được an toàn với liên kết cũ nên bỏ theo brief.

---

# Đợt bổ sung: 7 màn đặt xe (lượt 6)

Ngày 2026-11-04. Section `Đặt xe · lượt 6` (7386:470002). Nguồn: Mục 1, 2 của `srs/fleetio-saas-platform-userflow.md` (file này không có Mục 3), Flow 25-27 của `srs/fleetio-saas-platform-flows.md`, `run-notes/platform.md` Lượt 6. Cách nối như đợt trên.

## Kết quả kiểm bằng máy

| Mục | Trước | Sau |
|---|---|---|
| Tổng reaction, 246 frame màn | 8397 | 8408 (+11, đúng số đường đã nối) |
| Reaction trỏ node không tồn tại | 0 | 0 |
| Lỗi ghi, lỗi đối chiếu, xung đột click | | 0/11 |

Mốc 8397 đo đầu đợt này, sau khi có 7 frame mới, nên không so trực tiếp với 8301 của đợt trên. Hover, press của 11 node đã đối chiếu từng node. Chưa bấm thử Present.

## Đường đã nối: 11

| Từ | Đến | Nút | Kết quả |
|---|---|---|---|
| 5.13 reservation-validation | 5.14 reservation-detail-requested | Gửi yêu cầu đặt xe | Đã nối theo Flow 25, nhánh sửa xong thì tạo được, Requested |
| 5.14 reservation-detail-requested | 5.15 reservation-approve-dialog | Thêm | Suy luận về nút: màn không có nút Duyệt, menu chưa vẽ, chỉ một đích là frame |
| 5.15 reservation-approve-dialog | 5.16 reservation-detail-approved | Duyệt đặt xe | Đã nối |
| 5.15 reservation-approve-dialog | 5.14 reservation-detail-requested | Huỷ; Đóng | Đã nối 2 |
| 5.15 reservation-approve-dialog | 5.19 reservation-vehicle-overlap | Ô Xe | Đã nối theo Flow 26, ô Vehicle khi xe trùng lịch. Hai màn khác bản ghi (#1, #4) |
| 5.19 reservation-vehicle-overlap | 5.14 reservation-detail-requested | Huỷ; Đóng | Đã nối 2. Đích là #1, màn nền là #4 |
| 5.16 reservation-detail-approved | 5.20 reservation-completed | Thêm | Suy luận về nút: Giao xe, hoàn tất nằm trong menu chưa vẽ. Hai màn khác bản ghi (#1, #3) |
| 5.17 reservation-auto-approved-charges | 5.18 reservation-charges-flat-fee | Sửa | Đã nối |
| 5.18 reservation-charges-flat-fee | 5.20 reservation-completed | Thêm | Suy luận về nút, như 5.16 |

## Đường không nối được

| Đường | Lý do |
|---|---|
| 5.4 motor-pool-reservations → 5.11 vehicle-reservation-form (Thêm đặt xe), chiều Huỷ | 5.11 chưa có frame, tài liệu ghi không có ảnh |
| 5.11 → 5.13, 5.11 → 5.14, 5.11 → 5.17 | Như trên. Vì vậy 5.13 và 5.17 không có đường vào |
| 5.13 Gửi → 5.17 (đủ điều kiện tự duyệt) | Tài liệu chỉ ghi nguồn là 5.11, và nút Gửi đã trỏ 5.14 |
| 5.14 → Kết thúc (từ chối hoặc huỷ); 5.20 → Kết thúc | Không có màn đích |
| Check Out, Complete, Denied, Canceled | Có trong Flow 26, 27 nhưng chưa có màn |

## Đường vào, ra của 7 màn

Không tính menu bên, Menu bổ sung và đường tự trỏ. Số là số frame khác nhau.

| Màn | Vào | Ra |
|---|---|---|
| 5.14 reservation-detail-requested | 3 | 1 |
| 5.15 reservation-approve-dialog | 1 | 3 |
| 5.16 reservation-detail-approved | 1 | 1 |
| 5.17 reservation-auto-approved-charges | 0 | 1 |
| 5.18 reservation-charges-flat-fee | 1 | 1 |
| 5.19 reservation-vehicle-overlap | 1 | 1 |
| 5.20 reservation-completed | 2 | 0 |

Màn 5.13 reservation-validation: vào 0, ra 2. Do đó chuỗi 5.14 trở đi chưa đi tới được từ màn nào đang có đường vào. Muốn đi xuyên từ 5.4 thì cần frame 5.11.
