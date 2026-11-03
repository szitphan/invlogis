---
type: research
feature: fleetio-reminders-inspection
updated: 2026-11-03
---

# Nhắc và kiểm tra — Màn hình thật

Ảnh chụp từ tài khoản dùng thử ngày 02/11/2026 và 03/11/2026, dùng nội bộ để phân tích. Màn không có ảnh ghi rõ "Chưa có ảnh", bảng lấy từ ghi chú chạy.

## 1.1 Danh sách nhắc bảo dưỡng

![Danh sách nhắc](images/reminders-list.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Tab All, Due Soon, Overdue, Snoozed | Tab | Số | Due Soon, Overdue có số; All, Snoozed không |
| 2 | Thẻ Overdue Vehicles, Due Soon Vehicles, Snoozed Vehicles, Average Compliance | Thẻ | Số, % | Đếm theo xe, không theo nhắc |
| 3 | Vehicle, Service Task | Cột | Chữ | Dưới đầu việc ghi chu kỳ "Every 1 month(s) or 4,000 miles" |
| 4 | Status | Cột | Badge | Overdue đỏ, Due Soon cam, thanh màu mép dòng |
| 5 | Next Due | Cột | 2 dòng | Thời gian và số km còn hoặc quá; phần đang gây quá hạn tô đỏ |
| 6 | Incomplete Work Order | Cột | Liên kết | Lệnh đang xử lý nhắc |
| 7 | Last Completed, Compliance | Cột | Ngày, % | — |
| 8 | Watchers, Assignee, Assigned At | Cột | Người, ngày | Giao cho người |
| 8b | Add Service Reminder | Nút | — | Góc phải trên |
| 9 | Resolve | Menu dòng | — | Mở các cách xử lý ngay trên dòng |
| 10 | Enable Forecasting, Group | Nút | — | Bật dự báo, nhóm theo xe |

## 1.4 Form nhắc

![Form nhắc](images/reminder-new.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Dải gợi ý | Chữ | — | Nhiều xe cùng lịch thì dùng Service Program |
| 2 | Vehicle, Service Task | Chọn | Bắt buộc | Chọn xong hiện lần hoàn thành gần nhất |
| 3 | Time Interval, Time Due Soon Threshold | Số, đơn vị | — | Mặc định ngưỡng 2 tuần |
| 4 | Primary Meter Interval, Due Soon Threshold | Số | — | Mặc định ngưỡng 500; đơn vị theo xe |
| 5 | Manually set the due date and/or meter | Tick | — | Đặt tay kỳ tới |
| 6 | Notifications, Watchers | Tick, chọn | — | 7 giờ sáng rồi mỗi tuần |
| 7 | Schedule Preview | Bảng | Ngày, số | 5 kỳ tới, khi đủ dữ liệu |

## 1.2 Form bộ lịch

![Form bộ lịch](images/program-new.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Name | Chữ | Bắt buộc | Tên tuỳ biến theo ngôn ngữ |
| 2 | Template | Chọn | — | Mẫu có sẵn |
| 3 | Photo | Tải | Ảnh | — |
| 4 | Primary Meter | Chọn một | Bắt buộc | Miles, Kilometers, Hours |
| 5 | Secondary Meter | Bật tắt | — | Theo dõi thêm giờ máy, thiết bị kèm |

## 1.3 Danh sách gia hạn

![Gia hạn](images/renewals-list.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Tab All, Due Soon, Overdue | Tab đếm | Số | — |
| 2 | Vehicle, Renewal Type | Cột | Chữ | Loại có sẵn: Emission Test, Inspection, Insurance, Registration; thêm loại mới chưa thử |
| 3 | Status, Due Date | Cột | Badge, ngày | Kèm "3 weeks from now", "1 month ago" |
| 4 | Watchers | Cột | Người | — |

## 2.1 Chi tiết biểu mẫu

![Biểu mẫu](images/inspection-form.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Đầu trang | Chữ | — | Description, Location Exception Tracking, Prevent Use of Stored Photos |
| 2 | Tab Inspection Items, Workflows, Vehicles & Schedules | Tab đếm | Số | — |
| 3 | Thẻ từng mục | Khối | — | Đọc được luật: nhãn, N/A, bắt ảnh hoặc ghi chú |

## 2.2 Dựng mục

![Dựng mục](images/inspection-items-edit.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Danh sách mục | Kéo thả | — | Mở rộng để sửa; nhân bản, xoá; có nhóm |
| 2 | Thanh phải | Nút | — | 10 loại mục và Section; Meter Entry khoá khi đã có; bấm panel thêm mục, ô label tự focus |
| 3 | Ngôn ngữ | Nhãn | — | Sửa theo ngôn ngữ đang chọn |

## 2.3 Trang phiếu

![Phiếu](images/inspection-submission.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Inspection Details | Khối | — | Xe, biểu mẫu, Work Order, Started, Submitted, Duration, Source, Submitted By, Job |
| 2 | Cảnh báo vị trí | Dải | — | "Location permission was not enabled on this device when the inspection was submitted." |
| 3 | Inspection Items | Khối | — | Kết quả, liên kết lệnh hoặc sự cố |
| 4 | Print | Nút | — | In phiếu |

## 2.4 Item Failures

![Mục lỗi](images/item-failures.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Tab All, Needs Action, Open Issue, Acknowledged, Resolved | Tab | — | — |
| 2 | Cột | Bảng | — | Submitted At, Submission, Vehicle, Item, Form, Failure Timeline, Status |
| 3 | Status | Liên kết | — | Trỏ sự cố hoặc lệnh hiện tại |

## 2.5 Lịch kiểm tra

![Lịch kiểm tra](images/inspection-schedules.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Tab All, Due Soon, Overdue, Skipped | Tab | — | — |
| 2 | Cột | Bảng | — | Vehicle, Form, Status, Next Due, Last Inspected, Schedule, Frequency, Manually Overridden |
| 3 | Start Inspection | Nút | — | Bắt đầu phiếu |

## 1.5 Chi tiết nhắc

Chưa có ảnh trạng thái quá hạn; bố cục giống ảnh ở 1.6.

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Unwatch, "...", Edit, Resolve | Nút | — | "..." có Snooze hoặc Remove Snooze, Recalculate Compliance; Resolve mở các cách xử lý |
| 2 | Details | Khối | — | Vehicle, Operator lấy từ phân công xe, Status, Service Task, Service Program, Next Due, Last Completed, Work Order, Time Interval, Meter Interval, Manually Set Next Due, Notifications |
| 3 | Next Due | Khối | Ngày, số | "3 months from now" kèm "1,300 kilometers overdue" |
| 4 | Tab History | Tab | — | Lịch sử hoàn thành; sửa chu kỳ không ghi vào đây |

## 1.6 Chi tiết nhắc sau khi hoàn thành

![Chi tiết nhắc sau lệnh](images/reminder-after-work-order.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Tab Overview, History | Tab | — | Overview mặc định |
| 2 | Details | Khối | — | Status Upcoming, Next Due "3 months from now", "4,401 kilometers remaining", Last Completed 11/03/2026 và 2.400 km, Work Order trống, Time Interval kèm ngưỡng |
| 3 | Next Due | Khối | Ngày, số | Scheduled Date 02/02/2027, Primary Meter 7.400 km; liên kết "Improve compliance with Forecasting" |
| 4 | History | Thẻ | Số, % | Completed 1, Late 0, On-Time Compliance 100%; liên kết View History |
| 5 | Dòng lịch sử | Bảng | — | Due Nov 30, 2026 / 4.000 km; Completed 11/03/2026 / 2.400 km; nhãn On-Time; "3 weeks, 6 days ahead · 1,600 kilometers ahead" |
| 6 | Toast | Chữ | — | "Complete: Calculating Service Reminders Compliance in the background" kèm gợi ý tải lại trang |
| 7 | Dải đầu trang | Dải | — | Cảnh báo múi giờ thiết bị khác múi giờ tài khoản, có Fix, Dismiss |

## 1.7 Danh sách nhắc kèm tuân thủ

![Danh sách có tuân thủ](images/reminder-list-compliance.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Tab All, Due Soon 4, Overdue 2, Snoozed | Tab | Số | Tab có số |
| 2 | Lọc Vehicle, Service Task, Vehicle Group, Watcher, Filters | Bộ lọc | — | Đang lọc một xe; Group: None |
| 3 | Thẻ KPI | Thẻ | Số, % | Overdue Vehicles 1, Due Soon Vehicles 1, Snoozed Vehicles 0, Average Compliance 60% on-time; đếm xe, không đếm nhắc |
| 4 | Next Due | Cột | 2 dòng | Trục gây quá hạn đỏ, trục Due Soon cam |
| 5 | Compliance | Cột | % | 100%, 0%; chưa làm thì trống |
| 6 | Resolve | Nút dòng | — | Mở ngay trên dòng |

## 1.8 Hộp tạm hoãn

Chưa có ảnh.

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Câu mô tả | Chữ | — | "1 service reminder will be snoozed until the selected date and time. The reminder will return to its normal state after the snooze period is over." |
| 2 | Ngày, giờ | Chọn | Ngày giờ | Mặc định +7 ngày, giờ theo thiết bị; không có mức chọn sẵn; ngày đã qua không bị chặn |
| 3 | Lý do | — | — | Không có ô này |

## 1.9 Hộp giải quyết nhắc

Chưa có ảnh.

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Add to Work Order | Hộp | — | Liệt kê mọi nhắc của xe để tick thêm: "1 Service Reminder will be added", "Show 1 more"; "Add to New Work Order" hoặc "Add to Existing Work Order" |
| 2 | Add to service history | Hộp | — | "Log completed service": "Manually add to service entry" hoặc "Smart uploads" (mặc định); sau đó New hoặc Existing |
| 3 | Draft Work Order | Mục | — | Xám, icon khoá, bấm không phản hồi trên nhắc Upcoming |
| 4 | Find a shop | Mục | — | Không bấm |

## 1.10 Gán xe vào bộ lịch

Chưa có ảnh.

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | By Vehicle Attribute, All Vehicles, Specific Vehicles | Chọn một | — | Khoá sẵn "Primary Meter is equal to Kilometers"; ô chọn xe loại xe khác đơn vị |
| 2 | Câu tóm tắt | Chữ | — | "1 Vehicle will receive 2 Service Reminders based on the intervals below. Any conflicting individual Service Reminders will be replaced by the schedule from the Service Program." |
| 3 | Bảng đối chiếu | Bảng | — | Service Task, Conflicting, Duplicate, New Interval |
| 4 | Save as a Service Program Rule | Tick | — | Chỉ tick được với tiêu chí thuộc tính; mờ khi Specific Vehicles |

## 1.11 Thêm nhắc gia hạn

Chưa có ảnh.

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Vehicle hoặc Contact | Chọn | Bắt buộc | Chọn xe xong Watchers tự điền; Edit khoá |
| 2 | Renewal Type | Chọn | Bắt buộc | Loại đã có hiện xám "the selected vehicle already has a reminder of this type"; Edit khoá |
| 3 | Due Date | Ngày | Bắt buộc | Mặc định hôm nay |
| 4 | Threshold | Số | — | Fleetio: xe 3 tuần, liên hệ 4 tuần |

## 2.6 Form làm phiếu

Chưa có ảnh trạng thái đầy đủ; ảnh trạng thái lỗi lốp ở 2.7, 2.8.

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Chọn biểu mẫu, xe | Chọn | Bắt buộc | Biểu mẫu chưa gán xe: "No options", E-fleetio-reminders-inspection-017 |
| 2 | Các mục | Theo loại | — | Lỗi ở nhãn và ô: E-fleetio-reminders-inspection-001, 002, 003, 015 |
| 3 | Add Remark | Nút | — | "Add Comment", "Add Photo"; chỉ lưu khi gõ vào ô Comment |
| 4 | Chữ ký | Chữ | — | Nhập text "Type your name", vẽ thành nét chữ |
| 5 | Save Inspection, Cancel | Nút | — | Không có lưu nháp; toast E-fleetio-reminders-inspection-006; rời trang E-fleetio-reminders-inspection-019 |

## 2.7 Phiếu thiếu cấu hình trục

![Thiếu cấu hình trục](images/inspection-tire-axle-error.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Hộp lỗi đỏ | Chữ | — | "Please select axle configuration before submitting the form", kèm E-fleetio-reminders-inspection-006 |
| 2 | More info needed | Khối | — | "To display the correct number of tires below, please provide the following:" |
| 3 | Axle Configuration, Done | Chọn, nút | — | Khai ngay trong phiếu; Done sinh ô gai, áp suất và lốp cho từng vị trí |

## 2.8 Phiếu lốp bắt nhận xét

![Bắt nhận xét](images/inspection-tire-remark-required.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Ô gai từng vị trí | Số | Bắt buộc | Theo cấu hình trục |
| 2 | Lỗi | Chữ | — | "must contain a remark on failure" khi dưới mức của biểu mẫu |

## 2.9 Phiếu lốp không đạt, tổng

![Lốp không đạt](images/inspection-tire-fail-summary.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Submission | Khối | — | Thông tin phiếu |
| 2 | Dòng Tire Readings | Dòng | — | Một chữ "Fail", không tách vị trí ở dòng tổng |
| 3 | Issue #41 | Liên kết | — | Một sự cố cho nhiều lốp; "Added to Issue #41 (1 time reported)" |

## 2.10 Phiếu lốp không đạt, từng vị trí

![Từng vị trí](images/inspection-tire-fail-detail.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Dòng từng vị trí | Mở rộng | — | Dấu tích hoặc X cho gai, áp suất; đi vòng trái rồi phải; không có Spare |

## 2.11 Phiếu có bản đồ vị trí

![Bản đồ phiếu](images/inspection-submission-location.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Submitted, Duration, Submission Source, Submitted By, Job | Khối | — | "Fleetio Web App"; Job "Unassigned" khi xe không có việc |
| 2 | Bản đồ nhỏ | Bản đồ | — | Chấm xanh tại vị trí; ảnh dùng toạ độ giả lập |
| 3 | "...", Print | Nút | — | "..." chỉ có Delete |

## 2.12 Phiếu đủ mục, vị trí giả lập

![Phiếu đủ mục](images/inspection-pretrip-simulated.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Inspection Details | Khối | — | Vehicle, Inspection Form, Work Order, Started, Submitted, Duration, Submission Source, Submitted By, Job |
| 2 | Inspection Items | Khối | — | Odometer Reading, Item Checklist với kết quả Pass, số, nhãn lựa chọn |
| 3 | Location Exception | — | — | Không hiện cờ; `location_exception` false dù biểu mẫu bật |

## 2.13 Mục lỗi cần xử lý

![Needs Action](images/item-failure-needs-action.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Tab All, Needs Action, Open Issue, Acknowledged, Resolved | Tab | — | Đang ở Needs Action |
| 2 | Lọc Submitted Inspection Form, Submitted Inspection Item, Filters | Bộ lọc | — | — |
| 3 | Cột | Bảng | — | Submitted At, Submission, Vehicle, Item, Inspection Form, Failure Timeline (View), Status |
| 4 | Status | Nhãn | — | "Needs Action" đỏ; chỉ ra khi workflow tắt |
| 5 | Row menu "..." | Menu | — | Acknowledge, Create Issue, View Failure Timeline |

## 2.14 Thêm workflow

Chưa có ảnh.

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Bước 1 trigger | Chọn một | — | If an item passes, If an item fails, If form is submitted |
| 2 | Which inspection item(s)? | Chọn | — | "ANY Failed Inspection Item" hoặc từng mục Pass/Fail, Number, Dropdown |
| 3 | Bước 2 action | Chọn | — | Change vehicle status, Send an email, Create an issue ("Not Available" khi đã có workflow ANY), Assign user to vehicle, Unassign user from vehicle; không có tạo lệnh |
| 4 | Description, Enable Workflow | Chữ, bật tắt | — | — |

## 2.15 Xe và lịch của biểu mẫu

Chưa có ảnh.

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | All Vehicles, By Vehicle Attribute, Specific Vehicle | Chọn một | — | "manual override" với xe cụ thể |
| 2 | Set Schedule | Tick | — | Mặc định Daily, Every 1 Day; bỏ tick là "as needed" |
| 3 | Advanced | Khối | — | Set Delayed Start, Enable Reminder Notification, gửi theo múi giờ tài khoản |
| 4 | Bảng xe | Bảng | — | Vehicle, Add Via "Manual", Form Status "Enabled", Schedule, Frequency; rỗng trong lúc xử lý ngầm hơn 1 phút |
