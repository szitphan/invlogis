---
type: research
feature: fleetio-reminders-inspection
status: draft
updated: 2026-11-03
links:
  - docs/_research/fleetio/fleetio-reminders-inspection.md
  - docs/_research/fleetio/srs/fleetio-repair-spec.md
  - docs/_research/fleetio/run-notes/reminders-inspection.md
  - docs/_research/fleetio/run-notes/tires.md
  - docs/_research/fleetio/run-notes/location-dispatch.md
---

# Nhắc bảo dưỡng và kiểm tra xe — SRS phân tích ngược từ Fleetio

> Mô tả **Fleetio đang làm gì**, kèm đề xuất cho Invlogis. Chưa phải yêu cầu đã chốt với Delta.

**Nhãn bằng chứng:** `Chạy` đã thao tác · `Chạy (vị trí giả lập)` thao tác với toạ độ giả · `Xem` thấy trên giao diện · `Docs` tài liệu công khai · `Suy` suy ra · `GĐ` giả định.

## 1. Scope

**Trong phạm vi:** Service Reminder, Service Program, Vehicle và Contact Renewal, Inspection Form, Inspection Workflow, Schedule, Submission, Item Failure.

**Ngoài phạm vi:** app Fleetio Go chưa xem; lệnh sửa xem [[docs/_research/fleetio/srs/fleetio-repair-spec.md|Sửa chữa]]; quản lý lốp ngoài phiếu xem nhóm Phương tiện; vị trí và bản đồ xem nhóm Vị trí và điều phối.

**Giới hạn đợt chạy:** gói dùng thử chặn ở 5 xe, nên mooc không đồng hồ, xe giờ máy, đồng hồ phụ, phiếu riêng đầu kéo và mooc chưa chạy (OQ-10). Lịch kiểm cần qua ngày thật nên trạng thái lịch chưa thấy (OQ-11).

## 2. Actors & Stakeholders

| Actor | Loại | Mục tiêu | Trong scope? | Tương đương Invlogis |
|---|---|---|---|---|
| Operator | Người | Làm phiếu kiểm tra, nhận việc nhắc | Có | Lái xe |
| Fleet Manager | Người | Theo dõi nhắc, xử lý lỗi kiểm tra | Có | Quản lý phương tiện |
| Technician | Người | Thực hiện việc đến hạn | Có | Nhân viên xưởng |
| Administrator | Người | Dựng biểu mẫu, bộ lịch, ngưỡng | Có | Admin |
| Hệ thống | Hệ thống | Tính trạng thái, gửi thông báo, chạy workflow, xử lý ngầm | Có | — |

## 3. Functional Requirements (FR)

| ID | Title | Description | Priority | Tầng | Verify by | Source | Mức | Đề xuất Invlogis |
|---|---|---|---|---|---|---|---|---|
| FR-fleetio-reminders-inspection-001 | Tạo nhắc hai trục | Nhắc gắn xe và đầu việc, chu kỳ theo thời gian và đồng hồ, chỉ cần một trục, trục nào đến trước thì tính; ngưỡng Sắp đến hạn riêng từng trục, có đơn vị riêng. Fleetio: ngưỡng điền sẵn 2 tuần, 500 km. Lưu xong về trang chi tiết, người tạo tự là Watcher, chưa bật Notifications thì ghi "Inactive". | P0 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | test | #17071869, #17071895 | `Chạy` | Lấy cho `reminders`; chu kỳ, ngưỡng là tham số mới, chưa có mã |
| FR-fleetio-reminders-inspection-002 | Lấy lần gần nhất | Khi chọn xe và đầu việc, form hiện lần hoàn thành gần nhất, lấy từ lịch sử; chưa làm lần nào thì hiện "Never logged for this vehicle". | P0 | [Gói: Bảo dưỡng đội xe] | demo | Task C | `Chạy` | Lấy |
| FR-fleetio-reminders-inspection-003 | Xem trước lịch | Form hiện 5 kỳ tới với ngày và số km, kể cả kỳ đã qua ("1,000 km / 1,300 km ago"); lỗi ngưỡng báo ngay trong khối này. Form Edit không làm mới theo số mới. | P1 | [Gói: Bảo dưỡng đội xe] | demo | Task C | `Chạy` | Lấy, rẻ mà giảm sai; sửa điểm không làm mới |
| FR-fleetio-reminders-inspection-004 | Tính trạng thái | Upcoming, Due Soon, Overdue đổi ngay khi lưu số đồng hồ từ bất kỳ nguồn nào, không chờ job đêm; lấy trục xấu nhất. Chuyển do thời gian trôi chưa quan sát trực tiếp, biên ngày đo bằng cách sửa ngày. | P0 | [Gói: Bảo dưỡng đội xe] | test | 1.010 → 1.600 → 2.200 km; 2.300 → 3.001 km | `Chạy` | Lấy |
| FR-fleetio-reminders-inspection-005 | Reset khi xong | Đầu việc ghi nhận trên Service Entry hoặc lệnh Completed thì nhắc tính kỳ sau từ lần làm. Lệnh Open không đổi trạng thái. | P0 | [Gói: Bảo dưỡng đội xe] | test | Lệnh #101, #57857350, #57857463, #57857573 | `Chạy` | Lấy |
| FR-fleetio-reminders-inspection-006 | Tạm hoãn | Chọn ngày giờ hoãn, mặc định +7 ngày, giờ theo thiết bị, không có mức chọn sẵn, không có ô lý do. Status "Snoozed", Next Due vẫn đổi số nhưng xám. Hết hạn tự về trạng thái thường; Remove Snooze về ngay, không hỏi; hoàn thành xoá hoãn. Ẩn thông báo không nghiêm trọng là `Docs`. | P1 | [Gói: Bảo dưỡng đội xe] | test | Nhắc C, G | `Chạy`, `Docs` | Lấy, nên bắt ghi lý do, chặn ngày đã qua |
| FR-fleetio-reminders-inspection-007 | Xử lý từ nhắc | Resolve: Add to Work Order, Add to service history, Draft Work Order, Find a shop. Menu "...": Snooze hoặc Remove Snooze, Recalculate Compliance, Send Notifications. Draft Work Order xám, có icon khoá trên nhắc Upcoming, bấm không phản hồi. | P1 | [Gói: Bảo dưỡng đội xe] | demo | Nhắc D, E | `Chạy` hai đường đầu; `Xem` phần còn lại | Lấy |
| FR-fleetio-reminders-inspection-008 | Tỷ lệ tuân thủ | Tỷ lệ việc đúng hạn trên việc đã xong; thẻ Completed, Late, On-Time Compliance theo nhắc; trung bình theo danh sách lọc (D 100%, F 100%, Brake 100%, E 0%, G 0% ra 60%). Báo cáo là `Docs`. | P1 | [Gói: Bảo dưỡng đội xe] | phân tích | Danh sách lọc TEST-XE-01 | `Chạy` khi mỗi nhắc một lần; nhiều lần chưa kiểm | Lấy |
| FR-fleetio-reminders-inspection-009 | Dự báo ngày đến hạn | Ước tính ngày từ số km trung bình ngày; bật ở cấp tài khoản, nhóm theo tuần hoặc tháng. Thấy nút "Enable Forecasting", không bật vì là cài đặt tài khoản. | P2 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | phân tích | Nút trên danh sách, form Vehicle | `Xem`, `Docs` | Lấy khi số km tin cậy |
| FR-fleetio-reminders-inspection-010 | Giao nhắc cho người | Giao nhắc quá hạn cho người lái; nhận email hoặc tin nhắn, xác nhận được. Trang chi tiết lấy Operator từ phân công xe. | P2 | [Gói: Bảo dưỡng đội xe] | demo | Cột Assignee, Assigned At | `Docs`, `Xem` | Cân nhắc |
| FR-fleetio-reminders-inspection-011 | Bộ lịch | Một bộ gồm nhiều lịch cho nhiều xe, có mẫu, đồng hồ chính (Miles, Kilometers, Hours) và phụ; một dòng lịch chọn được nhiều đầu việc; sửa lịch trên bộ thì nhắc đang chạy đổi theo sau xử lý ngầm. | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | test | #590923 | `Chạy`; đồng hồ phụ, mẫu `Xem` | Lấy |
| FR-fleetio-reminders-inspection-012 | Gia hạn giấy tờ | Nhắc theo loại có sẵn, cho xe và liên hệ, có ngày đến hạn, ngưỡng báo, người theo dõi. Fleetio: loại xe Emission Test, Inspection, Insurance, Registration; loại liên hệ Certification, License Renewal; ngưỡng mặc định xe 3 tuần, liên hệ 4 tuần. Thêm loại mới chưa thử. | P0 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | test | #3531389, TEST-NHAC-LX | `Chạy` | Lấy; danh sách loại, ngưỡng là tham số mới, chưa có mã |
| FR-fleetio-reminders-inspection-013 | Dựng biểu mẫu | Tạo trống, từ mẫu hệ thống, hoặc từ PDF, ảnh bằng Smart Upload (Beta); có màu, ngôn ngữ, Location Exception Tracking, Prevent Use of Stored Photos. | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | demo | #679228 | `Chạy` trống và mẫu; `Xem` Smart Upload | Lấy cho feature mới `vehicle-inspection` nếu Delta cần |
| FR-fleetio-reminders-inspection-014 | Loại mục kiểm tra | Date/Time, Dropdown, Free Text, Inventory Adjustment, Meter Entry, Number, Pass/Fail, Photo, Signature, Tire Readings, Section. Mọi loại trừ Section có Label, Required (mặc định bật), Short Description. Meter Entry chỉ một mục. | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | demo | #679228 | `Chạy` cấu hình; Inventory Adjustment, Photo chưa làm trên phiếu | Lấy dần |
| FR-fleetio-reminders-inspection-015 | Luật từng mục | Bắt buộc, mô tả, hướng dẫn có định dạng, nhãn Đạt và Không đạt, N/A, bắt ảnh hoặc ghi chú; mục Số có khoảng, ngoài khoảng là Không đạt, biên tính là đạt; Dropdown có "Fail item if chosen"; Date/Time chọn "Date Only" hoặc "Date and Time". | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | test | #126056430, phiếu lốp | `Chạy` | Lấy |
| FR-fleetio-reminders-inspection-016 | Workflow biểu mẫu | Trigger: If an item passes, If an item fails, If form is submitted; chọn "ANY Failed Inspection Item" hoặc từng mục Pass/Fail, Number, Dropdown. Action: Change vehicle status, Send an email, Create an issue, Assign user to vehicle, Unassign user from vehicle. Không có action tạo lệnh. "..." có Edit, Disable, Delete. | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | test | Issue #47 đến #50; Disable ở TEST-NHAC-PHIEU | `Chạy` tạo sự cố và Disable; `Xem` phần còn lại | Lấy |
| FR-fleetio-reminders-inspection-017 | Gán biểu mẫu | All Vehicles, By Vehicle Attribute, Specific Vehicle; lịch Daily đến Yearly, Set Delayed Start, Enable Reminder Notification; không đặt lịch là "as needed". Xử lý ngầm. Không thấy lịch theo số đồng hồ trong form; chưa mở hết danh sách Frequency. | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | demo | Add Via "Manual", Daily | `Chạy` xe cụ thể; `Xem` còn lại | Lấy |
| FR-fleetio-reminders-inspection-018 | Làm phiếu | Chọn biểu mẫu, xe; hệ thống ghi Started, Submitted, Duration, Submission Source, Submitted By, Job, vị trí; nộp xong ra trang phiếu có bản đồ và Print. Phiếu không có nháp. | P1 | [Gói: Bảo dưỡng đội xe] | test | #126056430 | `Chạy` | Làm trên Delta Super App |
| FR-fleetio-reminders-inspection-019 | Vòng đời mục lỗi | Tab All, Needs Action, Open Issue, Acknowledged, Resolved; có Failure Timeline; Status trỏ sự cố, lệnh ("WO #100", "Resolved in Issue #49"). Needs Action chỉ ra khi workflow tắt. | P1 | [Gói: Bảo dưỡng đội xe] | test | #126056570, #126057076 | `Chạy`; Create Issue, Reopen `Xem` | Lấy |
| FR-fleetio-reminders-inspection-020 | Xác nhận lại sau sửa | Tài liệu hãng: sự cố đã giải quyết thì người kiểm tiếp theo được hỏi xác nhận, từ chối thì tạo sự cố mới. Trên web không thấy câu hỏi nào; lỗi lại sau Resolved sinh sự cố mới. | P1 | [Gói: Bảo dưỡng đội xe] | test | Issue #49 → #50 | `Docs`; `Chạy` trên web không có | Rất đáng lấy cho Super App; kiểm trên Fleetio Go trước (OQ-14) |
| FR-fleetio-reminders-inspection-021 | Chống kiểm khống | Tài liệu hãng: gắn Location Exception khi tỉ lệ mục cùng vị trí vượt ngưỡng, hoặc một mục lệch xa điểm trung tâm; bật theo biểu mẫu. Trên web không kích hoạt được: gói tin chỉ có một cặp toạ độ cấp phiếu, mọi phiếu `location_exception` false, không so giữa các phiếu. | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | test | #126054432 và 6 phiếu Quick check | `Xem` cấu hình; `Docs` luật; `Chạy (vị trí giả lập)` không kích hoạt | Lấy, thử với bãi xe lớn; kết hợp GPS xe, chuyến |
| FR-fleetio-reminders-inspection-022 | Cấm ảnh có sẵn | Chỉ cho đính ảnh chụp bằng camera, bật sẵn trên biểu mẫu mới. Chưa thử chụp hay đính ảnh. | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | test | Form biểu mẫu | `Xem` | Lấy |
| FR-fleetio-reminders-inspection-023 | Chi tiết nhắc | Nút Unwatch, "...", Edit, Resolve; khối Details (Vehicle, Operator, Status, Service Task, Service Program, Next Due, Last Completed, Work Order, Time Interval, Meter Interval, Manually Set Next Due, Notifications); khối Next Due; khối và tab History; bảng Due, Completed, Compliance. | P1 | [Gói: Bảo dưỡng đội xe] | demo | Nhắc D | `Chạy` | Lấy |
| FR-fleetio-reminders-inspection-024 | Đặt tay mốc kỳ tới | Tick "Manually set the due date and/or meter for the next reminder" mở Next Due Date, Next Due Primary Meter, mặc định hôm nay + chu kỳ và đồng hồ hiện tại + chu kỳ. Kỳ sau tính từ mốc đặt; tự về "No" sau một lần hoàn thành. | P0 | [Gói: Bảo dưỡng đội xe] | test | #17071903, #17071906 | `Chạy` | Lấy; đề xuất làm mặc định cho xe đã chạy |
| FR-fleetio-reminders-inspection-025 | Sửa nhắc | Edit khoá Vehicle, đổi chu kỳ thì tính lại ngay, không cảnh báo, không bắt lý do, không ghi History. Mở Edit rồi lưu làm Notifications từ Inactive thành Active. | P1 | [Gói: Bảo dưỡng đội xe] | test | Nhắc C, H | `Chạy` | Lấy cơ chế, thêm lý do và lịch sử |
| FR-fleetio-reminders-inspection-026 | Gộp nhắc vào lệnh | Resolve, Add to Work Order mở hộp liệt kê mọi nhắc của xe để tick thêm, chọn lệnh mới hoặc có sẵn. Lệnh Open: nhắc hiện "Work Order #101, Added ..." và dải "This Service Task was added to Work Order #101 ...". Completed xong hết dải, sinh Service Entry. | P0 | [Gói: Bảo dưỡng đội xe] | test | Lệnh #101 | `Chạy` | Lấy |
| FR-fleetio-reminders-inspection-027 | Đóng nhắc bằng phiếu dịch vụ | Add to service history mở "Log completed service": nhập tay hoặc Smart uploads (mặc định). Hoặc New Service Entry, gõ đầu việc ở Line Items: nhắc tự nhận, form hiện "Last Completed", "Next Due" ngay. Line Items có nút "View Service Reminders" kèm số. | P0 | [Gói: Bảo dưỡng đội xe] | test | #57857463, #57857573 | `Chạy`; Smart uploads `Xem` | Lấy |
| FR-fleetio-reminders-inspection-028 | Ghi tuân thủ từng lần | Mỗi lần hoàn thành có dòng Due, Completed, nhãn On-Time hoặc Late, chênh trên từng trục ("3 weeks, 6 days ahead · 1,600 kilometers ahead"). Recalculate Compliance chỉ bật khi đã có lịch sử; tính ngầm sau mọi thay đổi. | P1 | [Gói: Bảo dưỡng đội xe] | test | Nhắc D, E | `Chạy` | Lấy |
| FR-fleetio-reminders-inspection-029 | Đối chiếu khi gán bộ lịch | Trước khi lưu có bảng Service Task, Conflicting, Duplicate, New Interval và câu cảnh báo chung. Lịch có "Set First Service". "Save as a Service Program Rule" giữ đồng bộ theo thuộc tính, mờ khi chọn Specific Vehicles. | P1 | [Gói: Bảo dưỡng đội xe] | test | #590923 | `Chạy`; Rule `Xem` | Lấy, rất hợp đầu kéo cùng dòng |
| FR-fleetio-reminders-inspection-030 | Gỡ xe khỏi bộ lịch | Row menu chỉ có Delete; hộp "Confirm Service Program Vehicle Deletion" nêu sẽ xoá mọi nhắc từ bộ này trên xe. Không bấm; hệ quả thực tế chưa kiểm chứng (OQ-12). | P1 | [Gói: Bảo dưỡng đội xe] | demo | Hộp xác nhận | `Xem` | Đề xuất giữ lịch sử khi gỡ |
| FR-fleetio-reminders-inspection-031 | Gia hạn bằng sửa tay | Chi tiết chỉ có Details, Comments, "...", Edit. Không có Resolve, History, không tải giấy tờ mới. Gia hạn là sửa Due Date, kỳ cũ không lưu. Edit khoá Vehicle và Renewal Type. Lưu xong về danh sách. | P0 | [Gói: Bảo dưỡng đội xe] | test | #3531389; liên hệ chưa mở chi tiết | `Chạy` | Không học phần này; đề xuất mỗi kỳ một bản ghi có chứng từ |
| FR-fleetio-reminders-inspection-032 | Ghi nhận lỗi | Acknowledge ở Needs Action mở hộp "Acknowledge Failure", Comments tuỳ chọn. Sau đó row menu chỉ còn "View Failure Timeline". | P1 | [Gói: Bảo dưỡng đội xe] | test | #126057076 | `Chạy` | Lấy cơ chế, bắt lý do |
| FR-fleetio-reminders-inspection-033 | Gộp lỗi lặp | Mục lỗi lại khi sự cố còn mở: không tạo sự cố mới, thêm dòng Item Failures, thêm mốc Failure Timeline. Không báo gì cho người kiểm khi đang làm phiếu. | P1 | [Gói: Bảo dưỡng đội xe] | test | #126056570 vào Issue #31 | `Chạy` | Lấy |
| FR-fleetio-reminders-inspection-034 | Phiếu ăn theo chuyến | Trường Job tự gắn việc đang gán cho xe lúc nộp, "Unassigned" khi không có; phiếu nộp đúng lúc rời vùng vẫn mang việc đang gán rồi việc mới kết thúc. | P1 | [Gói: Bảo dưỡng đội xe] | test | #126056430 | `Chạy` | Rất đáng lấy cho Lệnh vận tải |
| FR-fleetio-reminders-inspection-035 | Vị trí nộp phiếu | Web gọi định vị một lần lúc khởi động app, giữ giá trị và gửi khi nộp; không cần điện thoại. Sinh Location Entry, xe lên bản đồ, gán Place, kích hoạt vùng; địa chỉ ngược có sau khoảng 1 phút. Máy chủ tin toạ độ gửi lên. | P1 | [Gói: Bảo dưỡng đội xe] | test | #126053906 | `Chạy (vị trí giả lập)` | Lấy, nhưng đối chiếu GPS xe |
| FR-fleetio-reminders-inspection-036 | Mục Meter Entry | Ghi số đồng hồ của xe từ phiếu, kiểm theo lịch sử đồng hồ; "Require Secondary Meter", "Require Photo Verification" bật sẵn; phiếu hiện dòng Odometer Reading. | P1 | [Gói: Bảo dưỡng đội xe] | test | #126056430, #126054432 | `Chạy`; ảnh, đồng hồ phụ `Xem` | Lấy, ưu tiên GPS |
| FR-fleetio-reminders-inspection-037 | Mục Tire Readings | Tự sinh ô gai và áp suất theo cấu hình trục, đi vòng bên trái từ trước ra sau rồi bên phải từ sau ra trước. Khai trục, lắp lốp thiếu ngay trong phiếu. Ghi về Tire Readings, Method "Inspection #...". Dòng tổng một chữ "Fail", mở ra từng vị trí. Spare không có trong phiếu. | P1 | [Gói: Bảo dưỡng đội xe] | test | #126051306, #126055120 | `Chạy` | Lấy, thêm trường vị trí trên sự cố |
| FR-fleetio-reminders-inspection-038 | Phiên bản biểu mẫu | Sửa nhãn sau khi có phiếu: phiếu cũ giữ nhãn cũ, đầu phiếu có nhãn cam "Past Version". Phiếu đã nộp: "..." chỉ có Delete, có Print, không sửa. | P1 | [Gói: Bảo dưỡng đội xe] | test | #126056430 | `Chạy` | Lấy |
| FR-fleetio-reminders-inspection-039 | KPI danh sách nhắc | Thẻ Overdue Vehicles, Due Soon Vehicles, Snoozed Vehicles đếm xe, không đếm nhắc; Average Compliance; tab Due Soon, Overdue có số; cột Next Due tô đỏ trục gây quá hạn; Resolve mở ngay trên dòng. | P1 | [Gói: Bảo dưỡng đội xe] | demo | Ảnh `reminder-list-compliance` | `Chạy` | Lấy |

## 4. Non-Functional Requirements (NFR)

| ID | Category | Requirement | Priority | Acceptance |
|---|---|---|---|---|
| NFR-fleetio-reminders-inspection-001 | thông báo | Fleetio: gửi lúc 7 giờ sáng khi đến hạn, sau đó mỗi tuần đến khi xử lý. | P1 | `Xem` mô tả trên form |
| NFR-fleetio-reminders-inspection-002 | tính toán nền | Tuân thủ, bộ lịch, gán biểu mẫu chạy ngầm, báo "Processing" rồi "Complete"; gán biểu mẫu hơn 1 phút, không tự báo ở tab đang mở. | P2 | `Chạy` "Calculating Service Reminders Compliance in the background", "Syncing Vehicles to Service Programs", "Adding Rule in the background" |
| NFR-fleetio-reminders-inspection-003 | trạng thái có vị trí | Không có quyền vị trí vẫn làm được phiếu, có cảnh báo trước và sau. | P1 | `Chạy` |
| NFR-fleetio-reminders-inspection-004 | khả dụng ngoại tuyến | Kiểm tra trên app khi mất mạng ở bãi: TBD — đội sản phẩm — khi lập `vehicle-inspection`. | P1 | TBD, chưa xem Fleetio Go |
| NFR-fleetio-reminders-inspection-005 | múi giờ | Fleetio dùng lẫn giờ thiết bị (Snooze, mốc đến hạn) và giờ tài khoản (thứ tự đồng hồ, thông báo). Lệch múi giờ gây chặn sai số đồng hồ và lệch mục Date/Time 13 giờ, có dải cảnh báo đầu trang. | P1 | `Chạy`. Đề xuất Invlogis: chốt một nguồn giờ theo khách, tham số mới, chưa có mã |

## 5. Business Rules

| ID | Rule | Tầng | Trigger | Implements FR | Source | Mức |
|---|---|---|---|---|---|---|
| BR-fleetio-reminders-inspection-001 | Đến hạn khi chạm mốc thời gian hoặc số km trước. | [Gói: Bảo dưỡng đội xe] | Số km, thời gian đổi | FR-fleetio-reminders-inspection-004 | Nhắc C | `Chạy` |
| BR-fleetio-reminders-inspection-002 | Một việc tính trễ nếu hoàn thành quá 10% chu kỳ ngày hoặc đồng hồ (Fleetio: 10%). Thấy Late ở mức vượt rõ; biên 10% chưa đo. | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Tính tuân thủ | FR-fleetio-reminders-inspection-008 | Tham số mới, chưa có mã | `Docs` |
| BR-fleetio-reminders-inspection-003 | Tuân thủ cần ít nhất một lịch sử khớp; chưa có thì Recalculate xám. | [Gói: Bảo dưỡng đội xe] | Tính tuân thủ | FR-fleetio-reminders-inspection-008 | Menu "..." | `Chạy`, `Docs` |
| BR-fleetio-reminders-inspection-004 | Áp bộ lịch: nhắc thêm tay trùng đầu việc bị thay, giữ nguyên mã, không hỏi từng nhắc; đầu việc chưa có nhắc thì sinh mới. Nhân đôi nhắc từ bộ khác và không hoàn tác được là `Docs`. | [Gói: Bảo dưỡng đội xe] | Gán bộ lịch | FR-fleetio-reminders-inspection-011 | Nhắc B giữ #17071895 | `Chạy`, `Docs` |
| BR-fleetio-reminders-inspection-005 | Biểu mẫu mới mặc định có workflow "mục lỗi thì tạo sự cố". | [Gói: Bảo dưỡng đội xe] | Tạo biểu mẫu | FR-fleetio-reminders-inspection-016 | #679228 | `Chạy` |
| BR-fleetio-reminders-inspection-006 | Tiêu đề sự cố từ phiếu theo loại mục: Pass/Fail "[Inspection Item] {mục} [Answer] Fail [Remark] {ghi chú}"; Tire Readings "[Inspection] {nhận xét}" hoặc "[Inspection] Tire Readings". Mô tả ghi người nộp, giờ; Source trỏ phiếu. | [Gói: Bảo dưỡng đội xe] | Tạo sự cố | FR-fleetio-reminders-inspection-016 | Issue #47, #32, #41 | `Chạy` |
| BR-fleetio-reminders-inspection-007 | Mỗi workflow một trigger, nhiều action; mỗi biểu mẫu một workflow gán hoặc bỏ gán. Đã có workflow ANY tạo sự cố thì action Create an issue hiện "Not Available". | [Gói: Bảo dưỡng đội xe] | Cấu hình | FR-fleetio-reminders-inspection-016 | Màn Add Workflow | `Docs`, `Xem` |
| BR-fleetio-reminders-inspection-008 | Không có lịch thì không bao giờ đến hạn, quá hạn; biểu mẫu vẫn dùng "as needed". | [Gói: Bảo dưỡng đội xe] | Gán xe | FR-fleetio-reminders-inspection-017 | Form Add Vehicles | `Docs`, `Xem` |
| BR-fleetio-reminders-inspection-009 | Fleetio: ngưỡng cùng vị trí 50–100%, mặc định 80%; ngưỡng lệch mặc định 100 m, đo theo đường thẳng tới điểm trung tâm. | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Nộp phiếu | FR-fleetio-reminders-inspection-021 | Tham số mới, chưa có mã; trên web không kích hoạt được | `Docs` |
| BR-fleetio-reminders-inspection-010 | Due Soon khi số còn lại nhỏ hơn hoặc bằng ngưỡng; biên thuộc Due Soon. | [Gói: Bảo dưỡng đội xe] | Lưu đồng hồ | FR-fleetio-reminders-inspection-004 | Nhắc B: 501 Upcoming, 500 Due Soon | `Chạy` |
| BR-fleetio-reminders-inspection-011 | Overdue khi đồng hồ lớn hơn hoặc bằng mốc; đúng mốc đã Overdue dù chữ ghi "0 kilometers remaining". | [Gói: Bảo dưỡng đội xe] | Lưu đồng hồ | FR-fleetio-reminders-inspection-004 | Nhắc B ở 3.000 | `Chạy` |
| BR-fleetio-reminders-inspection-012 | Trạng thái lấy trục xấu nhất: "3 months from now" kèm "1,300 kilometers overdue" vẫn là Overdue. | [Gói: Bảo dưỡng đội xe] | Tính trạng thái | FR-fleetio-reminders-inspection-004 | Nhắc C | `Chạy` |
| BR-fleetio-reminders-inspection-013 | Nhắc chưa có lịch sử, không đặt tay: mốc đồng hồ là bội số chu kỳ tính từ 0; mốc thời gian tính từ hôm nay. | [Gói: Bảo dưỡng đội xe] | Tạo nhắc | FR-fleetio-reminders-inspection-001 | Xe 2.300, chu kỳ 1.000: Overdue ngay | `Chạy` |
| BR-fleetio-reminders-inspection-014 | Phải có ít nhất một chu kỳ; ngưỡng nhỏ hơn chu kỳ, bằng cũng chặn, so đúng khi khác đơn vị. | [Gói: Bảo dưỡng đội xe] | Lưu nhắc | FR-fleetio-reminders-inspection-001 | 20 tuần so với 3 tháng | `Chạy` |
| BR-fleetio-reminders-inspection-015 | Nhắc bảo dưỡng: ngày đến hạn lấy mốc 00:00 giờ thiết bị, đến hạn hôm nay đã Overdue từ đầu ngày. Gia hạn: đến hạn hôm nay còn Due Soon ("19 hours from now"). | [Gói: Bảo dưỡng đội xe] | Tính trạng thái | FR-fleetio-reminders-inspection-004, FR-fleetio-reminders-inspection-012 | Nhắc H, #3531389 | `Chạy` |
| BR-fleetio-reminders-inspection-016 | Kỳ sau tính từ ngày và số đồng hồ của lần hoàn thành, không từ mốc dự kiến, kể cả khi số đó thấp hơn đồng hồ hiện tại. | [Gói: Bảo dưỡng đội xe] | Hoàn thành | FR-fleetio-reminders-inspection-005 | Nhắc D ra 7.400 km | `Chạy` |
| BR-fleetio-reminders-inspection-017 | Tính Late theo từng trục: ngày sớm nhưng km vượt vẫn Late. | [Gói: Bảo dưỡng đội xe] | Tính tuân thủ | FR-fleetio-reminders-inspection-028 | Nhắc E | `Chạy` |
| BR-fleetio-reminders-inspection-018 | Hoàn thành xoá hoãn, không hỏi; vẫn tính Late nếu quá hạn. | [Gói: Bảo dưỡng đội xe] | Hoàn thành khi hoãn | FR-fleetio-reminders-inspection-006 | Nhắc G | `Chạy` |
| BR-fleetio-reminders-inspection-019 | Hoãn ngày đã qua không bị chặn, báo thành công, trạng thái không đổi. Hết hạn hoãn về trạng thái thường, chênh dưới 2 phút. Đồng hồ tăng khi hoãn: số quá hạn vẫn đổi, Status vẫn Snoozed. | [Gói: Bảo dưỡng đội xe] | Hoãn | FR-fleetio-reminders-inspection-006 | Nhắc C | `Chạy` |
| BR-fleetio-reminders-inspection-020 | Đặt tay mốc tự tắt sau một lần hoàn thành. | [Gói: Bảo dưỡng đội xe] | Hoàn thành | FR-fleetio-reminders-inspection-024 | Nhắc D | `Chạy` |
| BR-fleetio-reminders-inspection-021 | Lệnh Open không đổi trạng thái nhắc. Completed cần Started At; số đồng hồ bắt buộc theo Cài đặt tài khoản. Xong thì khoá Edit lệnh. | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Đóng lệnh | FR-fleetio-reminders-inspection-026 | Lệnh #101 | `Chạy` |
| BR-fleetio-reminders-inspection-022 | Số đồng hồ phải khớp lịch sử theo thời điểm ghi, hoặc đánh Void. Void không hỏi lý do, ghi "Manually Voided", trạng thái nhắc lùi ngay. | [Gói: Bảo dưỡng đội xe] | Lưu đồng hồ | FR-fleetio-reminders-inspection-004, FR-fleetio-reminders-inspection-036 | 3.001, 3.000 | `Chạy` |
| BR-fleetio-reminders-inspection-023 | Sửa bộ lịch đổi nhắc đang chạy và trạng thái của nó, không hỏi. | [Gói: Bảo dưỡng đội xe] | Sửa bộ | FR-fleetio-reminders-inspection-011 | Nhắc B: Upcoming sang Due Soon | `Chạy` |
| BR-fleetio-reminders-inspection-024 | Bộ lịch chỉ gắn xe cùng đơn vị đồng hồ; ô chọn xe loại xe khác đơn vị. | [Gói: Bảo dưỡng đội xe] | Gán bộ | FR-fleetio-reminders-inspection-011 | "Primary Meter is equal to Kilometers" | `Chạy` |
| BR-fleetio-reminders-inspection-025 | Sự cố còn mở: lỗi lại gộp, đạt lại không tự đóng sự cố (phiếu hiện "✓ Pass" kèm liên kết sự cố). Sự cố đã Resolved: lỗi lại sinh sự cố mới, không mở lại. | [Gói: Bảo dưỡng đội xe] | Nộp phiếu | FR-fleetio-reminders-inspection-033 | #47, #48, #49 → #50 | `Chạy` |
| BR-fleetio-reminders-inspection-026 | Workflow tắt là đường duy nhất ra Needs Action. Acknowledged là trạng thái cuối. | [Gói: Bảo dưỡng đội xe] | Nộp phiếu | FR-fleetio-reminders-inspection-019 | #126057076 | `Chạy` |
| BR-fleetio-reminders-inspection-027 | Phiếu đã nộp không sửa được, chỉ xoá hoặc in; phiếu giữ nội dung phiên bản lúc nộp. | [Gói: Bảo dưỡng đội xe] | Sửa biểu mẫu | FR-fleetio-reminders-inspection-038 | #126056430 | `Chạy` |
| BR-fleetio-reminders-inspection-028 | Biểu mẫu chưa gán xe thì không làm phiếu được; danh sách xe rỗng, không nêu lý do. | [Gói: Bảo dưỡng đội xe] | Làm phiếu | FR-fleetio-reminders-inspection-017 | TEST-NHAC-PHIEU; mooc lốp | `Chạy` |
| BR-fleetio-reminders-inspection-029 | Mỗi xe một nhắc cho mỗi loại gia hạn; loại đã có hiện xám "the selected vehicle already has a reminder of this type". | [Gói: Bảo dưỡng đội xe] | Tạo gia hạn | FR-fleetio-reminders-inspection-012 | Registration | `Chạy` |
| BR-fleetio-reminders-inspection-030 | Mỗi biểu mẫu tối đa một mục Meter Entry (Fleetio: 1). | [Gói: Bảo dưỡng đội xe] | Dựng biểu mẫu | FR-fleetio-reminders-inspection-014 | Panel khoá | `Chạy` |
| BR-fleetio-reminders-inspection-031 | Phiếu ghi Job đang gán tại thời điểm nộp. | [Gói: Bảo dưỡng đội xe] | Nộp phiếu | FR-fleetio-reminders-inspection-034 | Trong và ngoài vùng | `Chạy (vị trí giả lập)` |
| BR-fleetio-reminders-inspection-032 | Vị trí phiếu là một cặp toạ độ cấp phiếu; không có toạ độ từng mục trên web; không kiểm toạ độ giả, không so giữa các phiếu. | [Gói: Bảo dưỡng đội xe] | Nộp phiếu | FR-fleetio-reminders-inspection-035 | Gói tin phiếu Pre-trip | `Chạy (vị trí giả lập)` |
| BR-fleetio-reminders-inspection-033 | Mục số: biên tính là đạt. | [Gói: Bảo dưỡng đội xe] | Nộp phiếu | FR-fleetio-reminders-inspection-015 | Gai Min 5: 5 Pass, 4.9 Fail | `Chạy` |
| BR-fleetio-reminders-inspection-034 | Ưu tiên sự cố tự sinh khác theo loại mục: Pass/Fail "High", Tire Readings "High", Dropdown "No Priority". | [Gói: Bảo dưỡng đội xe] | Tạo sự cố | FR-fleetio-reminders-inspection-016 | #47, #41, #49 | `Chạy` |
| BR-fleetio-reminders-inspection-035 | Mức tối thiểu của mục biểu mẫu tách khỏi mức của lốp: cùng số đọc có thể Pass ở phiếu mà Low ở lốp, hoặc Fail ở phiếu mà chỉ Warning ở lốp. Chỉ đường phiếu mới ra sự cố. | [Gói: Bảo dưỡng đội xe] | Nộp phiếu | FR-fleetio-reminders-inspection-037 | 1LO gai 5 | `Chạy` |
| BR-fleetio-reminders-inspection-036 | Một sự cố cho nhiều lốp; vị trí chỉ nằm trong chữ mô tả, không có trường riêng; mô tả có thể thiếu lỗi. | [Gói: Bảo dưỡng đội xe] | Tạo sự cố | FR-fleetio-reminders-inspection-037 | Issue #41 | `Chạy` |
| BR-fleetio-reminders-inspection-037 | Resolve with Note bắt buộc Note. Acknowledge không bắt buộc Comments. | [Gói: Bảo dưỡng đội xe] | Xử lý lỗi | FR-fleetio-reminders-inspection-019, FR-fleetio-reminders-inspection-032 | Issue #49 | `Chạy` |

## 6. Error Matrix

| Error ID | Title | Trigger | Severity | Related FR | Screen state | Recovery | Mức |
|---|---|---|---|---|---|---|---|
| E-fleetio-reminders-inspection-001 | Thiếu ghi chú khi lỗi | "must contain a remark on failure" | major | FR-fleetio-reminders-inspection-015 | Chữ đỏ ở mục, toast nộp lỗi | Add Remark, gõ vào ô Comment hoặc thêm ảnh | `Chạy` |
| E-fleetio-reminders-inspection-002 | Thiếu ghi chú khi đạt | "must contain a remark on pass" | major | FR-fleetio-reminders-inspection-015 | Như trên | Thêm | `Chạy` đợt 1 |
| E-fleetio-reminders-inspection-003 | Thiếu giá trị | "is required" | major | FR-fleetio-reminders-inspection-015 | Ở nhãn và ô | Nhập; gợi ý ngày trên ô Date chưa tính là đã nhập | `Chạy` |
| E-fleetio-reminders-inspection-004 | Thiếu cấu hình trục | "Please select axle configuration before submitting the form" | major | FR-fleetio-reminders-inspection-037 | Hộp "More info needed" ở mục lốp | Chọn Axle Configuration ngay trong phiếu, Done, hệ thống tự sinh lốp | `Chạy` |
| E-fleetio-reminders-inspection-005 | Chưa xác nhận | "This must be checked if there are no defects." | major | FR-fleetio-reminders-inspection-018 | Ở mục ký của biểu mẫu có ô này; kiểu Signature mặc định không có | Tick | `Chạy` đợt 1 |
| E-fleetio-reminders-inspection-006 | Nộp lỗi | "Could not submit inspection form. Please fix any errors and try again." | major | FR-fleetio-reminders-inspection-018 | Toast | Xem từng mục | `Chạy` |
| E-fleetio-reminders-inspection-007 | Không có vị trí | "Fleetio was unable to detect your location from your web browser. Location data will not be saved on this inspection."; trang phiếu ghi "Location permission was not enabled on this device when the inspection was submitted." | minor | FR-fleetio-reminders-inspection-035 | Dải cảnh báo | Bật vị trí, hoặc nộp không vị trí | `Chạy` đợt 1 |
| E-fleetio-reminders-inspection-008 | Nhắc thiếu chu kỳ | "Please provide a usage or a time interval"; toast "Service Reminder could not be created" | major | FR-fleetio-reminders-inspection-001 | Chữ đỏ ở cả hai ô | Nhập ít nhất một trục | `Chạy` |
| E-fleetio-reminders-inspection-009 | Ngưỡng km quá cao | "Primary Meter Due Soon Threshold is too high (can't be equal to or greater than Primary Meter Interval)" | major | FR-fleetio-reminders-inspection-001 | Trong Schedule Preview | Giảm ngưỡng | `Chạy` |
| E-fleetio-reminders-inspection-010 | Ngưỡng thời gian quá cao | "Time Due Soon Threshold is too high (can't be equal to or greater than Time Interval)" | major | FR-fleetio-reminders-inspection-001 | Trong Schedule Preview | Giảm ngưỡng | `Chạy` |
| E-fleetio-reminders-inspection-011 | Lệnh thiếu giờ bắt đầu | "Please edit and fix the following errors: Started At can't be blank" | major | FR-fleetio-reminders-inspection-026 | Khi đặt Completed | Nhập Started At | `Chạy` |
| E-fleetio-reminders-inspection-012 | Lệnh thiếu đồng hồ | "Starting Meter Entry can't be blank (per your account settings)"; "Odometer can't be blank (per your account settings)" | major | FR-fleetio-reminders-inspection-026 | Sau E-011 | Nhập số; sinh từ Cài đặt tài khoản | `Chạy` |
| E-fleetio-reminders-inspection-013 | Đồng hồ trái lịch sử | "must be less than 2,499 or marked as void"; "must be between 800 and 2,499 or marked as void" | major | FR-fleetio-reminders-inspection-036 | Ở ô đồng hồ; dòng dưới vẫn hiện số mới nhất | Nhập số hợp lệ hoặc Void; hay do lệch múi giờ | `Chạy` |
| E-fleetio-reminders-inspection-014 | Thiếu ngày hoàn thành | "can't be blank" | major | FR-fleetio-reminders-inspection-027 | Completion Date có gợi ý hôm nay nhưng chưa nhập | Nhập | `Chạy` |
| E-fleetio-reminders-inspection-015 | Thiếu đồng hồ trên phiếu | "requires a Odometer" | major | FR-fleetio-reminders-inspection-036 | Ở mục đồng hồ | Nhập | `Chạy` |
| E-fleetio-reminders-inspection-016 | Vượt hạn mức xe | "Your plan is limited to 5 vehicles"; toast "Vehicle could not be created" | major | FR-fleetio-reminders-inspection-001 | Form New Vehicle | Nâng gói, lưu trữ xe; xe Sample không tính | `Chạy` |
| E-fleetio-reminders-inspection-017 | Biểu mẫu chưa gán | "No options", "No results for ..." ở ô chọn xe; "No inspection forms exist yet" ở mooc chưa gán | major | FR-fleetio-reminders-inspection-017 | Danh sách rỗng, câu chữ gây hiểu nhầm | Gán xe, chờ xử lý ngầm | `Chạy` |
| E-fleetio-reminders-inspection-018 | Thiếu Note khi giải quyết | Note bắt buộc, gợi ý "Describe what work was performed to resolve the issue."; câu lỗi chưa ghi lại | minor | FR-fleetio-reminders-inspection-019 | Hộp Resolve with Note | Nhập Note | `Chạy` |
| E-fleetio-reminders-inspection-019 | Rời phiếu đang làm | "Leave site?" của trình duyệt | major | FR-fleetio-reminders-inspection-018 | Hộp trình duyệt | Ở lại; rời là mất phiếu, không có nháp | `Chạy` |

## 7. Success Criteria

| ID | Outcome nghiệp vụ | Đo bằng | Mốc đạt |
|---|---|---|---|
| SC-fleetio-reminders-inspection-01 | Không xe nào quá hạn mà không ai biết | Số xe Overdue chưa có người, lệnh xử lý | TBD |
| SC-fleetio-reminders-inspection-02 | Lỗi kiểm tra đều có đường xử lý | Số mục ở Needs Action quá lâu | TBD |
| SC-fleetio-reminders-inspection-03 | Giảm kiểm khống | Tỉ lệ phiếu Location Exception, thời lượng phiếu | TBD |

## 8. Data Entities (tóm tắt — chi tiết ở erd.md)

Service Reminder, Service Task, Compliance Record, Service Program, Program Schedule, Program Vehicle, Renewal Reminder, Renewal Type, Inspection Form, Form Version, Inspection Item, Workflow, Schedule Rule, Submission, Submitted Item, Item Failure, Meter Entry, Location Entry. Xem [[docs/_research/fleetio/srs/fleetio-reminders-inspection-erd.md|ERD]].

## 9. Flows (tóm tắt — chi tiết ở flows.md)

Xem [[docs/_research/fleetio/srs/fleetio-reminders-inspection-flows.md|Flows]], [[docs/_research/fleetio/srs/fleetio-reminders-inspection-states.md|States]], [[docs/_research/fleetio/srs/fleetio-reminders-inspection-usecases.md|Use case]], [[docs/_research/fleetio/srs/fleetio-reminders-inspection-userflow.md|User flow]].

## 10. Screens

Ảnh thật và bảng mô tả: [[docs/_research/fleetio/srs/fleetio-reminders-inspection-screens.md|Màn hình]]. Không áp `CMP`, `GR` vì mô tả sản phẩm của bên khác.

## 11. Constraints, Dependencies & Assumptions

| Giả định | Invalidate nếu sai |
|---|---|
| `GĐ` Fleetio Go có cùng luật phiếu với web | Phần làm phiếu trên app phải viết lại; đã biết xác nhận lại và vị trí từng mục không thấy trên web |
| `GĐ` GPS điện thoại đủ tốt ở bãi | Ngưỡng chống kiểm khống vô tác dụng |

**Không nên học:**

- Mốc đồng hồ tính từ 0 cho nhắc chưa có lịch sử: đầu kéo đã chạy nhiều bị Overdue ngay.
- Sửa chu kỳ xoá trắng quá hạn, Snooze và Acknowledge không có lý do, ngày hoãn đã qua vẫn báo thành công.
- Gia hạn không giữ lịch sử, không có chứng từ theo kỳ.
- Dùng lẫn giờ thiết bị và giờ tài khoản.
- Tin toạ độ gửi lên mà không đối chiếu.
- Mở Edit rồi lưu làm Notifications tự bật.

Bản trước ghi "mục lốp chặn nộp phiếu chỉ vì xe chưa khai trục, lái xe không tự sửa được". Đã sửa: người kiểm khai trục được ngay trong phiếu (E-fleetio-reminders-inspection-004).

## 12. Open Questions

* [ ] OQ-1: Delta có kiểm tra xe trước chuyến không? — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-2: Chu kỳ bảo dưỡng theo km, tháng hay cả hai, theo dòng xe? — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-3: Giấy tờ nào cần nhắc, báo trước bao lâu? — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-4: Phiếu kiểm hỏng có cho xe chạy tiếp không? — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-5: Mooc, máy phát có lịch riêng theo giờ chạy không? — Nguồn khách: Đề xuất tiện ích GPS (25/9/2025), mục 3
* [ ] OQ-6: Thay đồng hồ thì mốc km của nhắc xử lý thế nào? Chưa thử Meter Replacement. Đã biết Void số đồng hồ làm trạng thái lùi ngay — Nguồn khách: không áp dụng
* [ ] OQ-7: Phiếu không có vị trí có bị đánh dấu ngoại lệ không? Tắt vị trí có lách được chống kiểm khống không? Một phần: phiếu không vị trí vẫn nộp được (E-fleetio-reminders-inspection-007); toạ độ giả không bị chặn; mọi phiếu web thử đều `location_exception` false kể cả lệch khoảng 1.100 km giữa các phiếu; trên web không có vị trí từng mục. Còn Fleetio Go chưa kiểm (`Chạy (vị trí giả lập)`) — Nguồn khách: không áp dụng
* [x] OQ-8: Lần kiểm sau lỗi lại khi sự cố còn mở thì trùng hay gộp? Trả lời: gộp vào sự cố đang mở, thêm một mốc Failure Timeline, mỗi lần lỗi vẫn là một dòng Item Failures; không báo gì cho người kiểm khi đang làm phiếu (`Chạy`, #126056570 vào Issue #31) — Nguồn khách: không áp dụng
* [ ] OQ-9: Lưu vị trí lái xe, ảnh, chữ ký cần thông báo, đồng ý, thời hạn lưu thế nào theo quy định dữ liệu cá nhân? Cần pháp chế xác nhận — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-10: Mooc không đồng hồ, xe giờ máy, đồng hồ phụ, phiếu riêng đầu kéo và mooc chạy thế nào? Bị chặn bởi hạn mức 5 xe; cần được phép lưu trữ xe TEST không dùng — Nguồn khách: không áp dụng
* [ ] OQ-11: Lịch kiểm Due Soon, Overdue, Skipped đi thế nào? Cần qua ngày thật; lịch Daily đã gán trên `TEST-NHAC-PHIEU` — Nguồn khách: không áp dụng
* [ ] OQ-12: Gỡ xe khỏi bộ lịch thực tế xoá gì, có lịch sử tuân thủ không? Dừng ở hộp xác nhận — Nguồn khách: không áp dụng
* [ ] OQ-13: Create Issue từ Needs Action và Reopen sự cố đi đâu? Chưa bấm — Nguồn khách: không áp dụng
* [ ] OQ-14: Fleetio Go có hỏi xác nhận lại sau khi sự cố đã giải quyết, có vị trí từng mục, có làm phiếu ngoại tuyến không? — Nguồn khách: không áp dụng
* [ ] OQ-15: Inventory Adjustment, Photo trên phiếu và các trigger, action còn lại của workflow chạy thế nào? Chưa chạy — Nguồn khách: không áp dụng
* [ ] OQ-16: Lưu biểu mẫu không đổi gì có sinh phiên bản mới không? Biên 10% của Late, tuân thủ khi một nhắc có nhiều lần tính ra sao? Draft Work Order có khoá theo gói không? Chưa kiểm — Nguồn khách: không áp dụng
* [ ] OQ-17: Làm sớm hơn mốc thì Delta chấp nhận mất phần còn lại của chu kỳ, hay hợp đồng bảo dưỡng theo km đòi giữ mốc cũ? — Nguồn khách: chưa có trong tài liệu khách gửi

## 13. Ma trận case

Gồm cả điều KHÔNG xảy ra. Mã E trong bảng viết tắt, đầy đủ có tiền tố `E-fleetio-reminders-inspection-`. Dữ liệu thử ghi ở [[docs/_research/fleetio/run-notes/reminders-inspection.md|ghi chú chạy]].

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| C01 Đường chính nhắc | 3 tháng, 1.000 km trên xe 2.300 km | "3 months from now" kèm "1,300 kilometers overdue" vẫn là Overdue: theo trục xấu nhất | `Chạy`, `reminder-list-compliance.jpg` |
| C02 Nhắc chưa có lịch sử | Đồng hồ 2.300, chu kỳ 1.000 | Overdue ngay, "1,300 kilometers overdue"; preview hiện kỳ 1.000, 2.000 đã qua | `Chạy` |
| C03 Thời gian của nhắc mới | Chu kỳ 3 tháng | Tính từ hôm nay, "3 months from now" | `Chạy` |
| C04 Thiếu chu kỳ | Bỏ trống cả hai | E-008; chỉ cần một trục | `Chạy` |
| C05 Ngưỡng bằng chu kỳ | 1.000 và 1.000 | E-009; bằng cũng chặn | `Chạy` |
| C06 Ngưỡng thời gian khác đơn vị | 20 tuần so với 3 tháng | E-010, so đúng | `Chạy` |
| C07 Biên km 501 | Mốc 3.000, đồng hồ 2.499 | Upcoming, "501 kilometers remaining" | `Chạy` |
| C08 Biên km 500 | Đồng hồ 2.500 | Due Soon, "500 kilometers remaining" | `Chạy` |
| C09 Biên km 1 | Đồng hồ 2.999 | Due Soon, "1 kilometers remaining" (sai ngữ pháp số ít) | `Chạy` |
| C10 Đúng mốc | Đồng hồ 3.000 | Overdue, "0 kilometers remaining" | `Chạy` |
| C11 Quá mốc | Đồng hồ 3.001 | Overdue, "1 kilometers overdue" | `Chạy` |
| C12 Biên ngày 15 ngày | Ngưỡng 2 tuần, đến hạn 18/11 | Upcoming, "2 weeks from now" | `Chạy` |
| C13 Biên ngày 14 ngày | Đến hạn 17/11 | Due Soon, vẫn "2 weeks from now" | `Chạy` |
| C14 Đến hạn hôm nay | Đến hạn 03/11 | Overdue từ đầu ngày, "1 hour ago" | `Chạy` |
| C15 Đổi trạng thái có chờ job không | Lưu đồng hồ | Đổi ngay, KHÔNG chờ job đêm | `Chạy` |
| C16 Snooze ngày đã qua | 01/11 | KHÔNG chặn, toast thành công, vẫn Overdue | `Chạy` |
| C17 Snooze hợp lệ | Hôm nay 01:06 | "Snoozed until 11/03/2026", Next Due xám, menu đổi thành Remove Snooze, Resolve vẫn dùng được | `Chạy` |
| C18 Snooze hết hạn | Mốc 01:06 | 01:04:30 còn Snoozed, 01:07:06 đã Overdue | `Chạy` |
| C19 Đồng hồ tăng khi hoãn | Tăng trong lúc Snoozed | Số quá hạn đổi 1.300 → 2.000, Status vẫn Snoozed | `Chạy` |
| C20 Hoàn thành khi hoãn | G hoãn đến 11/10, Service Entry 2.460 km | Hết Snoozed, Due Soon còn 461 km, không hỏi; vẫn Late | `Chạy` |
| C21 Remove Snooze | G đang hoãn | Không hỏi, về Due Soon | `Chạy` |
| C22 Snooze có lý do, có mức chọn sẵn không | Mở hộp | KHÔNG có ô lý do, KHÔNG có mức chọn sẵn | `Chạy` |
| C23 Snooze từ Upcoming, Due Soon | | Chưa bấm | Chưa chạy |
| C24 Void số cao nhất | Void 3.001 | Đồng hồ 3.000, B vẫn Overdue | `Chạy` |
| C25 Void tiếp | Void 3.000 | Đồng hồ 2.999, B về Due Soon; không hỏi lý do | `Chạy` |
| C26 Đổi chu kỳ khi quá hạn | 1.000 → 5.000 km | Overdue → Upcoming, "2,001 kilometers remaining"; KHÔNG cảnh báo, KHÔNG ghi History | `Chạy` |
| C27 Mở Edit rồi lưu | Notifications đang Inactive | Thành Active dù không đụng ô | `Chạy` |
| C28 Đặt tay mốc | Nhắc D 30/11, 4.000 km | Mốc đúng như đặt; kỳ sau tính từ mốc đặt | `Chạy` |
| C29 Đặt tay sau hoàn thành | D xong | "Manually Set Next Due" về No | `Chạy` |
| C30 Thêm vào lệnh, lệnh Open | D, lệnh #101 Open | Vẫn Upcoming, có dải "added to Work Order" | `Chạy` |
| C31 Lệnh Completed thiếu dữ liệu | Thiếu giờ, đồng hồ | E-011 rồi E-012 | `Chạy` |
| C32 Lệnh lệch múi giờ | 01:09 giờ máy là 02/11 giờ tài khoản, đồng hồ 3.100 | E-013, phải nhập 2.400 | `Chạy` |
| C33 Lệnh Completed | D | Sinh #57857350, khoá Edit lệnh; Next Due 02/02/2027, 7.400 km | `Chạy`, `reminder-after-work-order.jpg` |
| C34 Làm sớm 4 tuần | Dự kiến 30/11, 4.000 km; làm 03/11, 2.400 km | Kỳ sau từ lần làm, mất phần còn lại; On-Time "3 weeks, 6 days ahead · 1,600 kilometers ahead" | `Chạy` |
| C35 Làm trễ km | E mốc 1.000, làm 2.450 km | Late dù ngày sớm; kỳ sau 3.450, Due Soon còn 451 km (KHÔNG về Upcoming) | `Chạy` |
| C36 Ghi Service Entry ngược ngày | 01/11, đồng hồ 1.500 | E-013 "must be less than 900 or marked as void" | `Chạy` |
| C37 Thiếu Completion Date | Chỉ có gợi ý hôm nay | E-014 | `Chạy` |
| C38 Ghi lùi không đi từ nhắc | F, 01/11, 800 km | Nhắc tự nhận; mốc 9.800, 30/04/2027, On-Time | `Chạy` |
| C39 Draft Work Order | D Upcoming | Xám, có icon khoá, bấm KHÔNG phản hồi | `Chạy` |
| C40 Tuân thủ lọc theo xe | 5 nhắc đã làm | 60%, trung bình đều | `Chạy` |
| C41 KPI theo xe | 2 nhắc Overdue, 1 xe | "Overdue Vehicles 1" | `Chạy`, `reminder-list-compliance.jpg` |
| C42 Recalculate | Nhắc chưa làm | Xám | `Chạy` |
| C43 Gán bộ lịch trùng nhắc tay | B đã có | Giữ mã #17071895, thay chu kỳ, Due Soon → Upcoming; KHÔNG hỏi từng nhắc | `Chạy` |
| C44 Gán bộ, đầu việc mới | A | Sinh nhắc Upcoming | `Chạy` |
| C45 Bộ lịch khác đơn vị | Xe Sample dùng mi | Không có trong ô chọn | `Chạy` |
| C46 Trong lúc đồng bộ bộ lịch | Khoảng 1 phút | Nhắc B chưa đổi | `Chạy` |
| C47 Sửa bộ lịch | 4.000 → 3.000, lần đầu 4.500 → 3.200 | B thành Due Soon, 201 km, sau xử lý ngầm; KHÔNG hỏi | `Chạy` |
| C48 Gỡ xe khỏi bộ | Hộp xác nhận | Không bấm, hệ quả chưa kiểm | `Xem` |
| C49 Gia hạn đến hạn hôm nay | Registration, ngưỡng 3 tuần | Due Soon, "19 hours from now" (khác nhắc bảo dưỡng) | `Chạy` |
| C50 Gia hạn ngày đã qua | 01/10 | Overdue, "1 month ago" | `Chạy` |
| C51 Gia hạn xử lý thế nào | Mở chi tiết | KHÔNG có Resolve, History, tải giấy tờ; chỉ sửa Due Date | `Chạy` |
| C52 Trùng gia hạn | Cùng xe, cùng loại | Dòng xám, không chọn được | `Chạy` |
| C53 Gia hạn liên hệ | License Renewal, ngưỡng 4 | Due Soon, "18 hours from now", 1 watcher | `Chạy` |
| C54 Liên hệ không mời | Tick Operator, User Access No Access | Không gửi gì | `Chạy` |
| C55 Biểu mẫu chưa gán xe | Làm phiếu | Danh sách xe rỗng, KHÔNG nêu lý do; E-017 | `Chạy` |
| C56 Mooc chưa gán | Mở phiếu từ mooc | "No inspection forms exist yet" dù tài khoản có | `Chạy` |
| C57 Đang gán ngầm | Hơn 1 phút | Tab rỗng, ô xe "No options", toast KHÔNG tự báo ở tab đang mở | `Chạy` |
| C58 Thêm Meter Entry lần hai | Đã có một mục | Panel khoá, xám | `Chạy` |
| C59 Tự tạo lệnh qua workflow | Xem Add Workflow | KHÔNG có action này | `Xem` |
| C60 Phiếu rỗng | Lưu trống | E-006, E-003, E-015 | `Chạy` |
| C61 Fail không ghi chú | Có luật | E-001 | `Chạy` |
| C62 Số ngoài khoảng | 25, khoảng 10 đến 20 | Fail tự động, "X 25", bắt ghi chú, sinh sự cố | `Chạy` |
| C63 Dropdown Fail | TEST Hong | Sinh sự cố, không cần ghi chú, No Priority | `Chạy` |
| C64 Ô Date chỉ có gợi ý | Chưa nhập | E-003 | `Chạy` |
| C65 Có ô xác nhận không | Signature mặc định | KHÔNG có "This must be checked", chỉ gõ tên | `Chạy` |
| C66 Lưu nháp | Tìm nút | KHÔNG có; rời trang "Leave site?", phiếu mất | `Chạy` |
| C67 Phiếu đạt có Job | Xe đang có Job chạy | Job tự gắn; lúc khác "Unassigned" | `Chạy` |
| C68 Mục Date/Time lệch giờ | Nhập 1:40am | Hiện 2:40pm, lệch 13 giờ, KHÔNG báo | `Chạy` |
| C69 Đồng hồ trên phiếu lệch giờ | 3.050 | "must be between 800 and 2,499 or marked as void" | `Chạy` |
| C70 Lỗi lại khi sự cố mở | Brakes, Issue #31 ở WO #100 | Gộp, "WO #100", thêm dòng; KHÔNG tạo sự cố mới, KHÔNG báo người kiểm | `Chạy` |
| C71 Đạt lại khi sự cố mở | Phanh, Áp suất | "✓ Pass" kèm liên kết sự cố; sự cố KHÔNG tự đóng | `Chạy` |
| C72 Lỗi lại sau Resolved | Dropdown, #49 đã Resolved | Issue mới #50, KHÔNG mở lại #49 | `Chạy` |
| C73 Hỏi xác nhận sau Resolved | Làm lại phiếu trên web | KHÔNG thấy prompt; tài liệu hãng ghi có | `Chạy`, `Docs` |
| C74 Workflow tắt | Disable rồi nộp lỗi | Needs Action, hai nút Acknowledge, Create Issue | `Chạy`, `item-failure-needs-action.jpg` |
| C75 Acknowledge không ghi chú | Lưu rỗng | Được; Acknowledged, không quay lại, không tạo sự cố được nữa | `Chạy` |
| C76 Resolve with Note | Issue #49 | Note bắt buộc; "Resolved in Issue #49" trên phiếu cũ, nút Reopen | `Chạy` |
| C77 Ưu tiên sự cố tự sinh | Theo loại mục | Pass/Fail High, Dropdown No Priority | `Chạy` |
| C78 Sửa biểu mẫu có phiếu | Đổi nhãn | "Past Version", phiếu cũ giữ nhãn cũ | `Chạy` |
| C79 Sửa phiếu đã nộp | Menu "..." | KHÔNG có sửa, chỉ Delete, có Print | `Chạy` |
| C80 Xe chưa khai trục, mục lốp | Chọn trong phiếu | "More info needed", Done, tự sinh lốp | `Chạy` |
| C81 Xe thiếu lốp khi mở phiếu | Tri-Axle thiếu 2 | "Install Missing Tires", "2 tires were successfully installed" | `Chạy` |
| C82 Biên gai và áp suất | Min 5, áp 80 đến 120 | 5 Pass, 4.9 Fail; 80 Pass, 79.9 Fail; 120 Pass, 120.1 Fail | `Chạy`, `inspection-tire-fail-detail.jpg` |
| C83 Hai mức tối thiểu | 1LO gai 5, biểu mẫu Min 5, lốp Min 8 | Phiếu Pass, Tire Readings Low | `Chạy` |
| C84 Lốp Fail | Nhiều vị trí | 1 sự cố, Issue #41, High; vị trí chỉ trong chữ, mô tả thiếu áp suất 2LI | `Chạy`, `inspection-tire-fail-summary.jpg` |
| C85 Spare trong phiếu | Xe có Spare | KHÔNG có ô | `Chạy` |
| C86 Phiếu trên web có vị trí không | Trình duyệt cho phép | Có; định vị lúc khởi động app, không cần điện thoại | `Chạy`, `inspection-submission-location.jpg` |
| C87 Phiếu không vị trí | #125988723 | Nộp được, E-007 | `Chạy` |
| C88 Toạ độ giả | Ghi đè định vị | Máy chủ lưu đúng toạ độ giả, sinh Location Entry; KHÔNG phát hiện | `Chạy (vị trí giả lập)` |
| C89 Location Exception, nhiều phiếu lệch | 6 phiếu cách nhau đến khoảng 1.100 km | Mọi phiếu false; KHÔNG so giữa các phiếu | `Chạy (vị trí giả lập)` |
| C90 Location Exception, phiếu đủ mục | Pre-trip, biểu mẫu bật | False; mục không có toạ độ; `starting_latitude` null | `Chạy (vị trí giả lập)`, `inspection-pretrip-simulated.jpg` |
| C91 Nộp trong, ngoài vùng khi có Job tự động | Hai phiếu liên tiếp | Thêm rồi kết thúc gán việc; phiếu ngoài vùng vẫn mang việc đang gán | `Chạy (vị trí giả lập)` |
| C92 Tạo xe riêng để thử | Đã có 5 xe | E-016; các case mooc, giờ máy bị chặn | `Chạy` |
