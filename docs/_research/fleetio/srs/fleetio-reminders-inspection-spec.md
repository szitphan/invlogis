---
type: research
feature: fleetio-reminders-inspection
status: draft
status_changed: 2026-11-03
status_reason: "đã review upstream, không cần sửa"
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

**Ngoài phạm vi:** phần còn lại của app Fleetio Go (mới đọc một phiếu #126102722 để kiểm vị trí từng mục); lệnh sửa xem [[docs/_research/fleetio/srs/fleetio-repair-spec.md|Sửa chữa]]; quản lý lốp ngoài phiếu xem nhóm Phương tiện; vị trí và bản đồ xem nhóm Vị trí và điều phối.

**Giới hạn đợt chạy:** gói dùng thử chặn ở 5 xe, nên mooc không đồng hồ, xe giờ máy, đồng hồ phụ trên xe thật, phiếu riêng đầu kéo và mooc chưa chạy (OQ-10). Lịch kiểm đã thấy Upcoming, Due Soon; Overdue, Skipped cần qua hạn thật (OQ-11). Không làm các việc có thể gửi ra ngoài hoặc xoá dữ liệu: Send Notifications, Send an email, Assign user, Delete, gỡ xe khỏi bộ lịch; không đổi Cài đặt cấp tài khoản nên Forecasting chưa bật.

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
| FR-fleetio-reminders-inspection-006 | Tạm hoãn | Hộp "Snooze Service Reminders" (số nhiều vì dùng chung với thao tác hàng loạt): ô "Snooze Until" ngày và giờ, mặc định +7 ngày, giờ theo thiết bị, không có mức chọn sẵn, không có ô lý do. Hoãn được nhắc Overdue và Upcoming; Upcoming giữ Next Due "3 months from now", Remove Snooze về Upcoming. Status "Snoozed", Next Due vẫn đổi số nhưng xám. Mỗi lần hoãn, bỏ hoãn ghi vào Record History. Hết hạn tự về trạng thái thường; Remove Snooze về ngay, không hỏi; hoàn thành xoá hoãn. Ẩn thông báo không nghiêm trọng là `Docs`. | P1 | [Gói: Bảo dưỡng đội xe] | test | Nhắc C, G | `Chạy` lượt 3: Hoãn và huỷ hoãn trên Upcoming | Lấy, nên bắt ghi lý do, chặn ngày đã qua |
| FR-fleetio-reminders-inspection-007 | Xử lý từ nhắc | Resolve chia 2 nhóm: GET SERVICE có Draft Work Order, Add to Work Order, Find a shop; LOG COMPLETED SERVICE có Add to service history. Menu "...": Snooze hoặc Remove Snooze, Send Notifications, View Record History, Recalculate Compliance, Delete. Draft Work Order khoá theo trạng thái nhắc, không theo gói: nhắc Upcoming xám, có icon khoá, tooltip "Available when this reminder is due soon or overdue."; nhắc Overdue chạy được, xem FR-fleetio-reminders-inspection-040. Find a shop xem FR-fleetio-reminders-inspection-050. | P1 | [Gói: Bảo dưỡng đội xe] | demo | Nhắc D, E | `Chạy` một phần lượt 4: Assign gửi email, SMS, dừng trước khi bấm | Lấy |
| FR-fleetio-reminders-inspection-008 | Tỷ lệ tuân thủ | Tỷ lệ việc đúng hạn trên việc đã xong; thẻ Completed, Late, On-Time Compliance theo nhắc; trung bình theo danh sách lọc (D 100%, F 100%, Brake 100%, E 0%, G 0% ra 60%). Một nhắc nhiều lần: thẻ nhắc H Completed 2, Late 1, 50%. Thêm H 50% thì danh sách ra "57% on-time", khớp 4 đúng hạn trên 7 lần (57,1%), không khớp trung bình theo nhắc (58,3%); mới một điểm đo. Báo cáo là `Docs`. | P1 | [Gói: Bảo dưỡng đội xe] | phân tích | Danh sách lọc TEST-XE-01 | `Chạy` lượt 4: Biên km: +100 Late, +99 On-Time | Lấy |
| FR-fleetio-reminders-inspection-009 | Dự báo ngày đến hạn | Ước tính ngày từ số km trung bình ngày; bật ở cấp tài khoản, nhóm theo tuần hoặc tháng. Thấy nút "Enable Forecasting", không bật vì là cài đặt tài khoản. | P2 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | phân tích | Nút trên danh sách, form Vehicle | `Xem`, `Docs` | Lấy khi số km tin cậy |
| FR-fleetio-reminders-inspection-010 | Giao nhắc cho người | Tài liệu hãng: giao nhắc quá hạn cho người lái; nhận email hoặc tin nhắn, xác nhận được. Trên web có cột Assignee, Assigned At nhưng chưa thấy nút giao ở các chỗ đã mở; menu Actions không có mục giao. Trang chi tiết lấy Operator từ phân công xe. | P2 | [Gói: Bảo dưỡng đội xe] | demo | Cột Assignee, Assigned At | `Docs`, `Xem` | Cân nhắc |
| FR-fleetio-reminders-inspection-011 | Bộ lịch | Một bộ gồm nhiều lịch cho nhiều xe, có mẫu, đồng hồ chính (Miles, Kilometers, Hours) và phụ; một dòng lịch chọn được nhiều đầu việc; sửa lịch trên bộ thì nhắc đang chạy đổi theo sau xử lý ngầm. Mẫu hệ thống xem FR-fleetio-reminders-inspection-043; lịch theo đồng hồ phụ xem FR-fleetio-reminders-inspection-044. Gắn xe theo thuộc tính sinh nhắc Upcoming trên xe, cột Service Program; tab Service Programs của xe có thẻ bộ lịch. Sau khi gán, đầu việc của bộ xám kèm khoá ở form New Service Reminder của xe đó. | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | test | #590923, TEST-DAUKEO-2 | `Chạy` lượt 4: Đã gắn xe, sinh 2 nhắc | Lấy |
| FR-fleetio-reminders-inspection-012 | Gia hạn giấy tờ | Nhắc theo loại có sẵn, cho xe và liên hệ, có ngày đến hạn, ngưỡng báo, người theo dõi. Fleetio: loại xe Emission Test, Inspection, Insurance, Registration; loại liên hệ Certification, License Renewal; ngưỡng mặc định xe 3 tuần, liên hệ 3 tuần. Thêm loại mới chưa thử. | P0 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | test | #3531389, TEST-NHAC-LX | `Chạy` | Lấy; danh sách loại, ngưỡng là tham số mới, chưa có mã |
| FR-fleetio-reminders-inspection-013 | Dựng biểu mẫu | Tạo trống, từ mẫu hệ thống, hoặc từ PDF, ảnh bằng Smart Upload (Beta); có màu, ngôn ngữ, Location Exception Tracking, Prevent Use of Stored Photos. Smart Upload nhận file xong khoá toàn bộ form bằng hộp "Processing Your Inspection Form"; khoảng 4 phút sau đổi "Taking longer than usual..." kèm "Restart Processing"; không có thời hạn, không báo lỗi. Lần đầu treo khoảng 6 phút, không ra bản dựng; lần thử lại dưới 30 giây có bản dựng, nên là lỗi lúc đó, không phải tính năng hỏng. Hộp "Review and Create Inspection Form": trái tài liệu, phải Title lấy từ ảnh, Description, Color, hai ô tick sẵn, danh sách mục có icon loại, Discard, Create Inspection Form. Nhận đúng Pass/Fail, Signature, Free Text; Number, Dropdown, Meter Entry, Photo đều thành Free Text (BR-fleetio-reminders-inspection-064). Đóng hộp hỏi "Are you sure you'd like to discard this smart upload?". | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | demo | #679228 | `Chạy` lượt 4: Smart Upload ra bản dựng dưới 30 giây | Lấy cho feature mới `vehicle-inspection` nếu Delta cần |
| FR-fleetio-reminders-inspection-014 | Loại mục kiểm tra | Date/Time, Dropdown, Free Text, Inventory Adjustment, Meter Entry, Number, Pass/Fail, Photo, Signature, Tire Readings, Section. Mọi loại trừ Section có Label, Required (mặc định bật), Short Description. Meter Entry chỉ một mục. Tire Readings tự có nhãn và mô tả "Tire Readings for all tire positions"; Inventory Adjustment không có nhãn mặc định, bỏ trống báo E-fleetio-reminders-inspection-023. | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | demo | #679228 | `Chạy` lượt 4: Inventory Adjustment trừ kho thật, 10 còn 7 | Lấy dần |
| FR-fleetio-reminders-inspection-015 | Luật từng mục | Bắt buộc, mô tả, hướng dẫn có định dạng, nhãn Đạt và Không đạt, N/A, bắt ảnh hoặc ghi chú; mục Số có khoảng, ngoài khoảng là Không đạt, biên tính là đạt; Dropdown có "Fail item if chosen"; Date/Time chọn "Date Only" hoặc "Date and Time". | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | test | #126056430, phiếu lốp | `Chạy` | Lấy |
| FR-fleetio-reminders-inspection-016 | Workflow biểu mẫu | Trigger: If an item passes, If an item fails, If form is submitted; chọn "ANY Failed Inspection Item" hoặc từng mục Pass/Fail, Number, Dropdown. Action: Change vehicle status, Send an email, Create an issue, Assign user to vehicle, Unassign user from vehicle. Không có action tạo lệnh. "..." có Edit, Disable, Delete. Change vehicle status có Active, In Shop, Inactive, Out of Service, Sold. "If form is submitted" đổi trạng thái xe ngay khi nộp, không hỏi, không phân biệt đạt hay lỗi. Description tự điền theo trigger và action. Danh sách chia nhóm Enabled, Disabled. Trigger đạt, lỗi theo từng mục chạy thật: mục đạt đổi được trạng thái xe, chọn được nhiều mục; trigger lỗi có thêm ANY ở đầu, trigger đạt không có. | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | test | Issue #47 đến #50; Disable ở TEST-NHAC-PHIEU; #680174, #126108655; #680309, #126116461, #126116614, #126116970 | `Chạy` một phần lượt 4: Pass, Fail chạy; email, gán người bị chặn | Lấy |
| FR-fleetio-reminders-inspection-017 | Gán biểu mẫu | All Vehicles, By Vehicle Attribute, Specific Vehicle; lịch Daily đến Yearly, Set Delayed Start, Enable Reminder Notification; không đặt lịch là "as needed": dòng gán có Schedule "Off", Frequency trống, không vào danh sách Inspection Schedules. Xử lý ngầm. Bộ lọc Frequency chỉ có Daily, Weekly, Monthly, Yearly, không có lịch theo số đồng hồ. Set Delayed Start: "The next due date will always be in the future.", không đặt được hạn quá khứ. | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | demo | Add Via "Manual", Daily; #680174 | `Chạy` một phần lượt 3: As needed; lịch sang Due Soon; Overdue chưa | Lấy |
| FR-fleetio-reminders-inspection-018 | Làm phiếu | Start Inspection mở Select Inspection Form, nhóm MOST USED và ALL. Mở từ xe thì chỉ liệt kê biểu mẫu đã gán cho xe đó. Chưa chọn xe thì form chỉ có ô Vehicle, nút Save Inspection khoá; chọn xe mới bung các mục. Trạng thái xe không chặn làm phiếu (xe Inactive vẫn làm được). Hệ thống ghi Started, Submitted, Duration, Submission Source, Submitted By, Job, vị trí; nộp xong ra trang phiếu có bản đồ và Print. Phiếu không có nháp. | P1 | [Gói: Bảo dưỡng đội xe] | test | #126056430 | `Chạy` | Làm trên Delta Super App |
| FR-fleetio-reminders-inspection-019 | Vòng đời mục lỗi | Tab All, Needs Action, Open Issue, Acknowledged, Resolved; có Failure Timeline; Status trỏ sự cố, lệnh ("WO #100", "Resolved in Issue #49"). Needs Action chỉ ra khi workflow tắt. Create Issue một cú bấm, không mở form, chuyển sang trang sự cố mới, dòng lỗi sang tab Open Issue. Reopen sự cố đưa dòng lỗi từ Resolved về Open Issue, không hỏi lý do. | P1 | [Gói: Bảo dưỡng đội xe] | test | #126056570, #126057076; #126108655 → Issue #51; #126056430, Issue #49 | `Chạy` lượt 3: Create Issue, Reopen đã bấm | Lấy |
| FR-fleetio-reminders-inspection-020 | Xác nhận lại sau sửa | Tài liệu hãng: sự cố đã giải quyết thì người kiểm tiếp theo được hỏi xác nhận, từ chối thì tạo sự cố mới. Trên web không thấy câu hỏi nào; lỗi lại sau Resolved sinh sự cố mới. Mục đạt khi sự cố còn mở: web chỉ nối mục với sự cố đó ("Issue #57" cạnh câu trả lời đạt), không có bước xác nhận, sự cố không tự đóng. | P1 | [Gói: Bảo dưỡng đội xe] | test | Issue #49 → #50 | `Docs`; `Chạy` trên web không có | Rất đáng lấy cho Super App; kiểm trên Fleetio Go trước (OQ-14) |
| FR-fleetio-reminders-inspection-021 | Chống kiểm khống | Tài liệu hãng: gắn Location Exception khi tỉ lệ mục cùng vị trí vượt ngưỡng, hoặc một mục lệch xa điểm trung tâm; bật theo biểu mẫu. Trên web không kích hoạt được: gói tin chỉ có một cặp toạ độ cấp phiếu, mọi phiếu `location_exception` false, không so giữa các phiếu. Fleetio Go ghi toạ độ từng mục và có hai chỉ báo `are_items_too_close`, `items_completed_too_far_away_count`; ca thử lệch tối đa 37 m không bị gắn cờ, chưa có ca dương. | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | test | #126054432, 6 phiếu Quick check, #126102722 | `Chạy` một phần lượt 3: Phiếu Fleetio Go 21/21 mục có toạ độ; chưa có ca dương | Lấy, thử với bãi xe lớn; kết hợp GPS xe, chuyến |
| FR-fleetio-reminders-inspection-022 | Cấm ảnh có sẵn | Cờ "Prevent Use of Stored Photos", bật sẵn trên biểu mẫu mới. Bật: Pick File mở thẳng hộp chụp webcam, không có đường chọn file; máy không có hoặc chặn camera thì mục Photo bắt buộc làm phiếu không nộp được. Tắt: mục Photo đổi thành "Pick File", "Or drop file here", nhận ảnh từ máy, hiện xem trước, "File uploaded: ...". Chưa chụp webcam thật. | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | test | Form biểu mẫu; #680174, #126108655 | `Chạy` một phần lượt 3: Chỉ mở webcam; tắt cờ thì nhận file; chưa chụp | Lấy |
| FR-fleetio-reminders-inspection-023 | Chi tiết nhắc | Nút Unwatch, "...", Edit, Resolve; khối Details (Vehicle, Operator, Status, Service Task, Service Program, Next Due, Last Completed, Work Order, Time Interval, Meter Interval, Manually Set Next Due, Notifications); khối Next Due; khối và tab History; bảng Due, Completed, Compliance. | P1 | [Gói: Bảo dưỡng đội xe] | demo | Nhắc D | `Chạy` | Lấy |
| FR-fleetio-reminders-inspection-024 | Đặt tay mốc kỳ tới | Tick "Manually set the due date and/or meter for the next reminder" mở Next Due Date, Next Due Primary Meter, mặc định hôm nay + chu kỳ và đồng hồ hiện tại + chu kỳ. Kỳ sau tính từ mốc đặt; tự về "No" sau một lần hoàn thành. | P0 | [Gói: Bảo dưỡng đội xe] | test | #17071903, #17071906 | `Chạy` | Lấy; đề xuất làm mặc định cho xe đã chạy |
| FR-fleetio-reminders-inspection-025 | Sửa nhắc | Edit khoá Vehicle, đổi chu kỳ thì tính lại ngay, không cảnh báo, không bắt lý do, không hiện ở tab History; có ghi ở Record History (FR-fleetio-reminders-inspection-041). Mở Edit rồi lưu làm Notifications từ Inactive thành Active, Record History ghi "Active changed from false to true". | P1 | [Gói: Bảo dưỡng đội xe] | test | Nhắc C, H | `Chạy` | Lấy cơ chế, thêm lý do và đưa lên lịch sử nghiệp vụ |
| FR-fleetio-reminders-inspection-026 | Gộp nhắc vào lệnh | Resolve, Add to Work Order mở hộp liệt kê mọi nhắc của xe để tick thêm, chọn lệnh mới hoặc có sẵn. Lệnh Open: nhắc hiện "Work Order #101, Added ..." và dải "This Service Task was added to Work Order #101 ...". Completed xong hết dải, sinh Service Entry. | P0 | [Gói: Bảo dưỡng đội xe] | test | Lệnh #101 | `Chạy` | Lấy |
| FR-fleetio-reminders-inspection-027 | Đóng nhắc bằng phiếu dịch vụ | Add to service history mở "Log completed service": nhập tay hoặc Smart uploads (mặc định). Hoặc New Service Entry, gõ đầu việc ở Line Items: nhắc tự nhận, form hiện "Last Completed", "Next Due" ngay. Line Items có nút "View Service Reminders" kèm số. New Service Entry có khối "Smart Upload" Beta: "Upload an invoice or receipt and Fleetio will automatically fill in the service entry for you."; luồng chạy thật xem FR-fleetio-reminders-inspection-048. | P0 | [Gói: Bảo dưỡng đội xe] | test | #57857463, #57857573 | `Chạy` lượt 4: Smart uploads chạy trọn đến phiếu lưu | Lấy |
| FR-fleetio-reminders-inspection-028 | Ghi tuân thủ từng lần | Mỗi lần hoàn thành có dòng Due, Completed, nhãn On-Time hoặc Late, chênh trên từng trục ("3 weeks, 6 days ahead · 1,600 kilometers ahead"). Recalculate Compliance chỉ bật khi đã có lịch sử; tính ngầm sau mọi thay đổi. | P1 | [Gói: Bảo dưỡng đội xe] | test | Nhắc D, E | `Chạy` | Lấy |
| FR-fleetio-reminders-inspection-029 | Đối chiếu khi gán bộ lịch | Trước khi lưu có bảng Service Task, Conflicting, Duplicate, New Interval và câu cảnh báo chung. Lịch có "Set First Service". "Save as a Service Program Rule" giữ đồng bộ theo thuộc tính, mờ khi chọn Specific Vehicles, khoá khi còn Sample Data (E-fleetio-reminders-inspection-029). Không có Rule thì lần gán chỉ là gán một lần theo kết quả lọc. Điều kiện Rule xem FR-fleetio-reminders-inspection-045. | P1 | [Gói: Bảo dưỡng đội xe] | test | #590923 | `Chạy` một phần lượt 3: Rule đọc điều kiện; chưa lưu Rule | Lấy, rất hợp đầu kéo cùng dòng |
| FR-fleetio-reminders-inspection-030 | Gỡ xe khỏi bộ lịch | Row menu chỉ có Delete, không có đường gỡ khác; hộp "Confirm Service Program Vehicle Deletion" nêu sẽ xoá mọi nhắc từ bộ này trên xe. Không bấm vì brief cấm xoá; hệ quả thực tế chưa kiểm chứng (OQ-12). | P1 | [Gói: Bảo dưỡng đội xe] | demo | Hộp xác nhận | `Xem` | Đề xuất giữ lịch sử khi gỡ |
| FR-fleetio-reminders-inspection-031 | Gia hạn bằng sửa tay | Bấm dòng mở panel phải "Contact Renewal #..." có Edit, "...": View, Send Notifications, View Record History, Delete. Trang chi tiết chỉ có Details, Comments, "...", Edit; xe và liên hệ giống nhau. Không có Resolve, tab History, không tải giấy tờ mới. Gia hạn là sửa Due Date; không có khái niệm kỳ, không có chứng từ, nhưng Record History ghi "Next Due At", "Due Soon At" từ giá trị nào sang giá trị nào, ai đổi lúc nào. Edit khoá Vehicle hoặc Contact và Renewal Type. Sửa xong Status tính lại ("Upcoming", "1 year from now"). | P0 | [Gói: Bảo dưỡng đội xe] | test | #3531389, #1596560 | `Chạy` | Không học phần này; đề xuất mỗi kỳ một bản ghi có chứng từ |
| FR-fleetio-reminders-inspection-032 | Ghi nhận lỗi | Acknowledge ở Needs Action mở hộp "Acknowledge Failure", Comments tuỳ chọn. Sau đó row menu chỉ còn "View Failure Timeline". | P1 | [Gói: Bảo dưỡng đội xe] | test | #126057076 | `Chạy` | Lấy cơ chế, bắt lý do |
| FR-fleetio-reminders-inspection-033 | Gộp lỗi lặp | Mục lỗi lại khi sự cố còn mở: không tạo sự cố mới, thêm dòng Item Failures, thêm mốc Failure Timeline. Không báo gì cho người kiểm khi đang làm phiếu. | P1 | [Gói: Bảo dưỡng đội xe] | test | #126056570 vào Issue #31 | `Chạy` | Lấy |
| FR-fleetio-reminders-inspection-034 | Phiếu ăn theo chuyến | Trường Job tự gắn việc đang gán cho xe lúc nộp, "Unassigned" khi không có; phiếu nộp đúng lúc rời vùng vẫn mang việc đang gán rồi việc mới kết thúc. | P1 | [Gói: Bảo dưỡng đội xe] | test | #126056430 | `Chạy` | Rất đáng lấy cho Lệnh vận tải |
| FR-fleetio-reminders-inspection-035 | Vị trí nộp phiếu | Web gọi định vị một lần lúc khởi động app, giữ giá trị và gửi khi nộp; không cần điện thoại. Sinh Location Entry, xe lên bản đồ, gán Place, kích hoạt vùng; địa chỉ ngược có sau khoảng 1 phút. Máy chủ tin toạ độ gửi lên. | P1 | [Gói: Bảo dưỡng đội xe] | test | #126053906 | `Chạy (vị trí giả lập)` | Lấy, nhưng đối chiếu GPS xe |
| FR-fleetio-reminders-inspection-036 | Mục Meter Entry | Ghi số đồng hồ của xe từ phiếu, kiểm theo lịch sử đồng hồ; "Require Secondary Meter", "Require Photo Verification" bật sẵn; phiếu hiện dòng Odometer Reading. Xe không có đồng hồ phụ: tuỳ chọn phụ bị bỏ qua, không báo. Xe có đồng hồ phụ: 2 ô "Primary Meter", "Secondary Meter", mỗi ô một Void; để trống phụ báo E-fleetio-reminders-inspection-028; phiếu hiện cả hai số ở cùng mục. Require Photo Verification tạo dòng bắt buộc "Meter Entry Photo Verification" (thêm "Secondary Meter Entry Photo Verification" nếu có đồng hồ phụ); tắt đi các dòng vẫn hiện, chỉ bỏ dấu bắt buộc. Ảnh đồng hồ luôn chỉ mở webcam, không theo cờ cấm ảnh có sẵn; tick Void không gỡ được yêu cầu (E-fleetio-reminders-inspection-020). Số bằng đúng số hiện tại được nhận, không báo trùng. | P1 | [Gói: Bảo dưỡng đội xe] | test | #126056430, #126054432 | `Chạy` một phần lượt 4: Đồng hồ phụ chạy; ảnh webcam chưa | Lấy, ưu tiên GPS |
| FR-fleetio-reminders-inspection-037 | Mục Tire Readings | Tự sinh ô gai và áp suất theo cấu hình trục, đi vòng bên trái từ trước ra sau rồi bên phải từ sau ra trước (xe 4 lốp: LF, LR, RR, RF; mỗi vị trí Tread Depth /32 in, Pressure PSI, đều bắt buộc). Khai trục, lắp lốp thiếu ngay trong phiếu. Ghi về Tire Readings, Method "Inspection #...". Dòng tổng một chữ "Fail", mở ra từng vị trí. Spare không có trong phiếu. | P1 | [Gói: Bảo dưỡng đội xe] | test | #126051306, #126055120 | `Chạy` | Lấy, thêm trường vị trí trên sự cố |
| FR-fleetio-reminders-inspection-038 | Phiên bản biểu mẫu | Sửa nhãn sau khi có phiếu: phiếu cũ giữ nhãn cũ, đầu phiếu có nhãn cam "Past Version". Phiếu đã nộp: "..." chỉ có Delete, có Print, không sửa. | P1 | [Gói: Bảo dưỡng đội xe] | test | #126056430 | `Chạy` | Lấy |
| FR-fleetio-reminders-inspection-039 | KPI danh sách nhắc | Thẻ Overdue Vehicles, Due Soon Vehicles, Snoozed Vehicles đếm xe, không đếm nhắc; Average Compliance; tab Due Soon, Overdue có số; cột Next Due tô đỏ trục gây quá hạn; Resolve mở ngay trên dòng. | P1 | [Gói: Bảo dưỡng đội xe] | demo | Ảnh `reminder-list-compliance` | `Chạy` | Lấy |
| FR-fleetio-reminders-inspection-040 | Bản nháp lệnh bằng AI | Resolve › Draft Work Order, chỉ mở khi nhắc Due Soon hoặc Overdue: toast "Drafting service", "No need to wait here — we'll notify you when the draft is ready."; dải "Work Order drafted", "Ready for your review." với Discard, Review draft; xong dưới 2 phút. Bản nháp gom toàn xe ("Drafted from vehicle profile", "13/13 Service Tasks"), không chỉ nhắc đang bấm: nhóm "Resolves ..." ghép sự cố đang mở với đầu việc do AI chọn; nhóm "Due for maintenance" gồm Overdue, Due Soon, Upcoming, tick sẵn hết. Có "Est. Subtotal (1 of 13 estimated)" từ lịch sử, báo lệnh đang mở và cho "Add to" lệnh đó hoặc lệnh mới; "Will auto-fill when created" gồm Repair Priority Class, Issue Date, WO Status; "Generated by AI just now. Was this helpful?". | P2 | [Gói: Bảo dưỡng đội xe] | demo | Nhắc H, C; Work Order #105; đã Discard | `Chạy` một phần lượt 4: Chạy trên Overdue; Add to chưa bấm | Đáng học việc gom cả xe; đề xuất không tick sẵn việc còn xa |
| FR-fleetio-reminders-inspection-041 | Nhật ký thay đổi bản ghi | Menu "..." › View Record History mở hộp có lọc khoảng ngày, cột Date, Changes By, Changes Made; ghi tên trường kỹ thuật và giá trị trước, sau (Primary Meter Interval, Due Soon Meter Value, Next Due Meter, Snooze Until, Active, Skip Automatic Watchers Callbacks, Current Service Occurrence). Có trên nhắc bảo dưỡng và gia hạn. Không hiện ở tab History nghiệp vụ, không có lý do. | P1 | [Gói: Bảo dưỡng đội xe] | demo | Nhắc C; #1596560 | `Chạy` | Lấy; đề xuất viết bằng ngôn ngữ nghiệp vụ, thêm lý do |
| FR-fleetio-reminders-inspection-042 | Thao tác hàng loạt trên nhắc | Tick dòng, mở "Actions": GET SERVICE có Add to Work Order, Find a shop; LOG COMPLETED SERVICE có Add to service history; OTHER có Snooze Service Reminder, Remove Snooze, Add Watchers, Remove Watchers, Delete. Không có mục giao nhắc; khác menu Resolve một dòng ở chỗ không có Draft Work Order. | P1 | [Gói: Bảo dưỡng đội xe] | demo | Danh sách nhắc; chỉ đọc menu | `Xem` | Lấy |
| FR-fleetio-reminders-inspection-043 | Mẫu bộ lịch hệ thống | New Service Program có Fleetio: 14 mẫu (Basic Vehicle Maintenance, Light Duty Truck Maintenance, Heavy Duty Truck Short Haul, Long Haul, 10 loại máy công trình); bộ tự tạo cũng hiện làm mẫu. Chọn mẫu: hiện ngay "11 Service Reminders will be created" và bảng Intervals, Service Task, ẩn lựa chọn đồng hồ. Mẫu ghi được "1st service at ..., then every ..." và "Every 3 years or 500,000 miles". | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | test | #591701 | `Chạy` | Lấy ý tưởng bộ mẫu theo dòng xe; danh sách mẫu là dữ liệu theo khách, đơn vị phải chọn được |
| FR-fleetio-reminders-inspection-044 | Lịch theo đồng hồ phụ | Bộ lịch bật Secondary Meter = Hours: form lịch mở 3 trục Time, Primary Meter, Secondary Meter; "Secondary Meter Due Soon Threshold" tự điền (Fleetio: 50 hr). Chỉ nhập đồng hồ phụ vẫn lưu được ("Every 200 hours"). Chưa gắn được xe có đồng hồ phụ vì hết hạn mức xe. | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | test | #591702 | `Chạy` một phần lượt 3: Lưu lịch; chưa sinh nhắc trên xe thật | Rất đáng lấy cho máy phát, xe giờ máy |
| FR-fleetio-reminders-inspection-045 | Điều kiện gán bộ lịch | New Service Program Vehicles: By Vehicle Attribute, All Vehicles, Specific Vehicles; điều kiện đầu khoá sẵn "Primary Meter is equal to Kilometers"; thêm điều kiện theo 28 thuộc tính xe, nối AND. Giá trị chỉ liệt kê cái đang có. Thuộc tính đổi liên tục như Current Operator lọc được nhưng không lưu thành Rule (E-fleetio-reminders-inspection-025). Không khớp xe thì nút lưu khoá (E-fleetio-reminders-inspection-026). Ô Rule khoá toàn bộ khi còn Sample Data, kể cả với Make (E-fleetio-reminders-inspection-029). Link "1 Vehicle" mở tab mới có danh sách xe khớp, đọc được tiêu chí lọc. | P1 | [Gói: Bảo dưỡng đội xe] | demo | #590923; gán Make, Type lên TEST-DAUKEO-2 | `Chạy` một phần lượt 3: Đọc điều kiện; chưa lưu Rule, chưa thấy xe mới tự vào | Lấy, rất hợp đầu kéo cùng dòng |
| FR-fleetio-reminders-inspection-046 | Mục Inventory Adjustment | Trên phiếu: Part Location liệt kê kho; chọn kho mới hiện ô Parts "Search and add parts...", danh sách chỉ gồm phụ tùng có ở kho đó kèm tồn. Để trống phiếu ghi "No parts used". Màn Edit items có dấu đỏ, trang xem và form phiếu không có; phiếu trống vẫn nộp được nên thực tế không bắt buộc. Có chọn phụ tùng: số lượng mặc định 1, có đơn vị, nút xoá dòng; nộp phiếu là trừ kho ngay, không bước duyệt; Inventory Activity ghi "Inspection Submission #...", số lượng, tồn trước, tồn sau, người làm; Reason trống. Phiếu hiện "{kho} • 1 parts", đếm dòng, không đếm số lượng. | P1 | [Gói: Bảo dưỡng đội xe] | test | #680174, #126108655; #126116970, Part #9427430 | `Chạy` lượt 4: Trừ kho thật, 10 còn 7 | Cân nhắc; bổ sung một đường ghi nhận phụ tùng dùng ngay lúc kiểm |
| FR-fleetio-reminders-inspection-047 | Vị trí từng mục trên Fleetio Go | Phiếu nộp từ Fleetio Go ghi cặp toạ độ riêng cho từng mục, phần web không có; gói phiếu có thêm `are_items_too_close`, `items_completed_too_far_away_count`. `starting_latitude` vẫn null dù phiếu có giờ bắt đầu. | P1 | [Gói: Bảo dưỡng đội xe] | test | #126102722 | `Chạy` một phần lượt 3: Một phiếu không vi phạm, chưa có ca dương | Lấy làm dữ liệu nền cho chống kiểm khống trên Delta Super App |
| FR-fleetio-reminders-inspection-048 | Smart Upload phiếu dịch vụ | Hộp toàn màn: trái trình xem tài liệu, phải "Review Service Entry", "Review and edit for accuracy before adding the service entry."; các ô hiện dần, dưới 30 giây đủ. Đọc Primary Meter, Completion Date, Reference, Vendor (khớp bản ghi có sẵn), Tax, Total. Gộp dòng hoá đơn thành một Service Task hệ thống, tách Labor, Parts, ghi mô tả. "Add to Service Entry" khoá khi dòng mới chưa chọn đầu việc, chỉ đổ vào form, phải Save lần nữa. Có Discard, Give Feedback, "Show More" gồm Labor, Parts, Labor Markup, Parts Markup, Warranty Credits, Discount, Tax. | P1 | [Gói: Bảo dưỡng đội xe] | test | #57903305 | `Chạy` | Đáng học màn đối chiếu cạnh tài liệu; đề xuất gợi ý đầu việc theo nhắc đang chờ của xe |
| FR-fleetio-reminders-inspection-049 | Đánh giá phiếu dịch vụ bằng AI | Sau lưu, phiếu có khối "Assessment": "Reviewing this service", "Checking service history"; không có giá thì "Add line item costs to run an assessment"; có giá thì ra "Acceptable", tiêu đề, đoạn nhận xét, "Auto-assessed ...", số nguồn, "Was this helpful?". Khối "Teach assessments your fleet's policies" có "Add a rule", dòng gợi ý và kết quả xem trước "Needs Review". | P2 | [Gói: Bảo dưỡng đội xe] | demo | #57903305, #57903349 | `Chạy` một phần lượt 4: Đọc kết quả; chưa thêm rule | Cân nhắc sau, cần lịch sử giá đủ dày |
| FR-fleetio-reminders-inspection-050 | Giao dịch vụ thuê ngoài từ nhắc | Resolve › Find a shop mở hộp "Assign outsourced service", 3 bước Service Details, Suggest Shop, Confirm. Service Details: Assign to, Vehicle, Service Reminders ("Assign all service reminders (3)"), When + ASAP, Continue. Assign to chỉ có người dùng và nhãn Fleetio Automation, không lấy được liên hệ không có đăng nhập. Notification Methods Email, Text Message tick sẵn. Confirm: "Service Assignment", "Ready to assign", Back, Assign. | P2 | [Gói: Bảo dưỡng đội xe] | demo | Nhắc TEST-NHAC-E, đóng ở Confirm | `Chạy` một phần lượt 4: Đến Confirm; không bấm Assign vì gửi email, SMS thật; không thấy danh sách cửa hàng | Cân nhắc khi Delta có xưởng ngoài |

## 4. Non-Functional Requirements (NFR)

| ID | Category | Requirement | Priority | Acceptance |
|---|---|---|---|---|
| NFR-fleetio-reminders-inspection-001 | thông báo | Fleetio: gửi lúc 7 giờ sáng khi đến hạn, sau đó mỗi tuần đến khi xử lý. | P1 | `Xem` mô tả trên form |
| NFR-fleetio-reminders-inspection-002 | tính toán nền | Tuân thủ, bộ lịch, gán biểu mẫu chạy ngầm, báo "Processing" rồi "Complete"; gán biểu mẫu hơn 1 phút, không tự báo ở tab đang mở. | P2 | `Chạy` "Calculating Service Reminders Compliance in the background", "Syncing Vehicles to Service Programs", "Adding Rule in the background" |
| NFR-fleetio-reminders-inspection-003 | trạng thái có vị trí | Không có quyền vị trí vẫn làm được phiếu, có cảnh báo trước và sau. | P1 | `Chạy` |
| NFR-fleetio-reminders-inspection-004 | khả dụng ngoại tuyến | Kiểm tra trên app khi mất mạng ở bãi: TBD — đội sản phẩm — khi lập `vehicle-inspection`. | P1 | TBD, chưa xem Fleetio Go |
| NFR-fleetio-reminders-inspection-005 | múi giờ | Fleetio dùng lẫn giờ thiết bị (Snooze, mốc đến hạn) và giờ tài khoản (thứ tự đồng hồ, thông báo). Lệch múi giờ gây chặn sai số đồng hồ và lệch mục Date/Time 13 giờ, có dải cảnh báo đầu trang. | P1 | `Chạy`. Đề xuất Invlogis: chốt một nguồn giờ theo khách, tham số mới, chưa có mã |
| NFR-fleetio-reminders-inspection-006 | xử lý AI nền | Draft Work Order chạy nền, báo khi xong (dưới 2 phút); Smart Upload biểu mẫu khoá form bằng hộp, không có thời hạn (lần đầu treo khoảng 6 phút, lần thử lại dưới 30 giây); Smart Upload phiếu dịch vụ dưới 30 giây; Assessment hơn 5 phút mới ra kết quả. | P2 | `Chạy`, ít lần thử, chưa đủ để kết luận độ tin cậy |

## 5. Business Rules

| ID | Rule | Tầng | Trigger | Implements FR | Source | Mức |
|---|---|---|---|---|---|---|
| BR-fleetio-reminders-inspection-001 | Đến hạn khi chạm mốc thời gian hoặc số km trước. | [Gói: Bảo dưỡng đội xe] | Số km, thời gian đổi | FR-fleetio-reminders-inspection-004 | Nhắc C | `Chạy` |
| BR-fleetio-reminders-inspection-002 | Một việc tính trễ nếu hoàn thành quá 10% chu kỳ ngày hoặc đồng hồ (Fleetio: 10%). Dung sai là dưới 10%: trục đồng hồ chu kỳ 1.000 km, trễ đúng 100 km Late, trễ 99 km On-Time. Trục ngày: chu kỳ 3 tháng khoảng 92 ngày, trễ 9 ngày On-Time, trễ 10 ngày Late; ca đúng bằng 10% không đo được vì không tròn ngày. | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Tính tuân thủ | FR-fleetio-reminders-inspection-008 | Tham số mới, chưa có mã | `Chạy` |
| BR-fleetio-reminders-inspection-003 | Tuân thủ cần ít nhất một lịch sử khớp; chưa có thì Recalculate xám. | [Gói: Bảo dưỡng đội xe] | Tính tuân thủ | FR-fleetio-reminders-inspection-008 | Menu "..." | `Chạy`, `Docs` |
| BR-fleetio-reminders-inspection-004 | Áp bộ lịch: nhắc thêm tay trùng đầu việc bị thay, giữ nguyên mã, không hỏi từng nhắc; đầu việc chưa có nhắc thì sinh mới. Nhân đôi nhắc từ bộ khác và không hoàn tác được là `Docs`. | [Gói: Bảo dưỡng đội xe] | Gán bộ lịch | FR-fleetio-reminders-inspection-011 | Nhắc B giữ #17071895 | `Chạy`, `Docs` |
| BR-fleetio-reminders-inspection-005 | Biểu mẫu mới mặc định có workflow "mục lỗi thì tạo sự cố". | [Gói: Bảo dưỡng đội xe] | Tạo biểu mẫu | FR-fleetio-reminders-inspection-016 | #679228 | `Chạy` |
| BR-fleetio-reminders-inspection-006 | Tiêu đề sự cố từ phiếu theo loại mục: Pass/Fail "[Inspection Item] {mục} [Answer] Fail [Remark] {ghi chú}"; Tire Readings "[Inspection] {nhận xét}" hoặc "[Inspection] Tire Readings". Mô tả ghi người nộp, giờ; Source trỏ phiếu. | [Gói: Bảo dưỡng đội xe] | Tạo sự cố | FR-fleetio-reminders-inspection-016 | Issue #47, #32, #41 | `Chạy` |
| BR-fleetio-reminders-inspection-007 | Mỗi workflow một trigger, nhiều action; mỗi biểu mẫu một workflow gán hoặc bỏ gán. Đã có workflow ANY tạo sự cố thì action Create an issue hiện "Not Available", kể cả với trigger form submitted. | [Gói: Bảo dưỡng đội xe] | Cấu hình | FR-fleetio-reminders-inspection-016 | Màn Add Workflow, #680174 | `Docs`; `Chạy` phần Not Available |
| BR-fleetio-reminders-inspection-008 | Không có lịch thì không bao giờ đến hạn, quá hạn; biểu mẫu vẫn dùng "as needed". | [Gói: Bảo dưỡng đội xe] | Gán xe | FR-fleetio-reminders-inspection-017 | Form Add Vehicles | `Docs`, `Xem` |
| BR-fleetio-reminders-inspection-009 | Fleetio: ngưỡng cùng vị trí 50–100%, mặc định 80%; ngưỡng lệch mặc định 100 m, đo theo đường thẳng tới điểm trung tâm. | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Nộp phiếu | FR-fleetio-reminders-inspection-021 | Tham số mới, chưa có mã; trên web không kích hoạt được; Fleetio Go có dữ liệu từng mục nhưng chưa có ca dương nên chưa đo được ngưỡng | `Docs` |
| BR-fleetio-reminders-inspection-010 | Due Soon khi số còn lại nhỏ hơn hoặc bằng ngưỡng; biên thuộc Due Soon. | [Gói: Bảo dưỡng đội xe] | Lưu đồng hồ | FR-fleetio-reminders-inspection-004 | Nhắc B: 501 Upcoming, 500 Due Soon | `Chạy` |
| BR-fleetio-reminders-inspection-011 | Overdue khi đồng hồ lớn hơn hoặc bằng mốc; đúng mốc đã Overdue dù chữ ghi "0 kilometers remaining". | [Gói: Bảo dưỡng đội xe] | Lưu đồng hồ | FR-fleetio-reminders-inspection-004 | Nhắc B ở 3.000 | `Chạy` |
| BR-fleetio-reminders-inspection-012 | Trạng thái lấy trục xấu nhất: "3 months from now" kèm "1,300 kilometers overdue" vẫn là Overdue. | [Gói: Bảo dưỡng đội xe] | Tính trạng thái | FR-fleetio-reminders-inspection-004 | Nhắc C | `Chạy` |
| BR-fleetio-reminders-inspection-013 | Nhắc chưa có lịch sử, không đặt tay: mốc đồng hồ là bội số chu kỳ tính từ 0; mốc thời gian tính từ hôm nay. Xe 100 km, chu kỳ 1.000: preview 1.000, 2.000, 3.000. | [Gói: Bảo dưỡng đội xe] | Tạo nhắc | FR-fleetio-reminders-inspection-001 | Xe 2.300, chu kỳ 1.000: Overdue ngay; #17077733 | `Chạy` |
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
| BR-fleetio-reminders-inspection-032 | Phiếu nộp trên web có một cặp toạ độ cấp phiếu; không có toạ độ từng mục; không kiểm toạ độ giả, không so giữa các phiếu. Phiếu Fleetio Go xem BR-fleetio-reminders-inspection-057. | [Gói: Bảo dưỡng đội xe] | Nộp phiếu | FR-fleetio-reminders-inspection-035 | Gói tin phiếu Pre-trip | `Chạy (vị trí giả lập)` |
| BR-fleetio-reminders-inspection-033 | Mục số: biên tính là đạt. | [Gói: Bảo dưỡng đội xe] | Nộp phiếu | FR-fleetio-reminders-inspection-015 | Gai Min 5: 5 Pass, 4.9 Fail | `Chạy` |
| BR-fleetio-reminders-inspection-034 | Ưu tiên sự cố tự sinh khác nhau, chưa rõ luật: lượt trước Pass/Fail "High", Tire Readings "High", Dropdown "No Priority"; lượt 4 Pass/Fail Brakes "Critical", Number và Dropdown "No Priority", cùng phiếu, cùng người. Theo nội dung mục là `Suy`, bản trước ghi theo loại mục chưa đủ. | [Gói: Bảo dưỡng đội xe] | Tạo sự cố | FR-fleetio-reminders-inspection-016 | #47, #41, #49; #56, #57, #58 | `Chạy` |
| BR-fleetio-reminders-inspection-035 | Mức tối thiểu của mục biểu mẫu tách khỏi mức của lốp: cùng số đọc có thể Pass ở phiếu mà Low ở lốp, hoặc Fail ở phiếu mà chỉ Warning ở lốp. Chỉ đường phiếu mới ra sự cố. | [Gói: Bảo dưỡng đội xe] | Nộp phiếu | FR-fleetio-reminders-inspection-037 | 1LO gai 5 | `Chạy` |
| BR-fleetio-reminders-inspection-036 | Một sự cố cho nhiều lốp; vị trí chỉ nằm trong chữ mô tả, không có trường riêng; mô tả có thể thiếu lỗi. | [Gói: Bảo dưỡng đội xe] | Tạo sự cố | FR-fleetio-reminders-inspection-037 | Issue #41 | `Chạy` |
| BR-fleetio-reminders-inspection-037 | Resolve with Note bắt buộc Note. Acknowledge không bắt buộc Comments. | [Gói: Bảo dưỡng đội xe] | Xử lý lỗi | FR-fleetio-reminders-inspection-019, FR-fleetio-reminders-inspection-032 | Issue #49 | `Chạy` |
| BR-fleetio-reminders-inspection-038 | Trễ trong dung sai vẫn tính On-Time nhưng chữ "behind" vẫn đỏ. | [Gói: Bảo dưỡng đội xe] | Tính tuân thủ | FR-fleetio-reminders-inspection-028 | Nhắc H lần 2 | `Chạy` |
| BR-fleetio-reminders-inspection-039 | Tỷ lệ một nhắc là số lần đúng hạn trên số lần làm; trung bình danh sách khớp cách tính theo lần, không theo nhắc (một điểm đo). | [Gói: Bảo dưỡng đội xe] | Tính tuân thủ | FR-fleetio-reminders-inspection-008 | Nhắc H 50%, danh sách 57% | `Chạy` |
| BR-fleetio-reminders-inspection-040 | Ghi Service Entry lùi ngày được chấp nhận, kỳ sau tính từ lần làm đó. Đặt tay hạn cũ hơn hôm nay không bị chặn, Overdue ngay. | [Gói: Bảo dưỡng đội xe] | Hoàn thành, đặt tay | FR-fleetio-reminders-inspection-005, FR-fleetio-reminders-inspection-024 | #57888299, #57888341 | `Chạy` |
| BR-fleetio-reminders-inspection-041 | Bản nháp lệnh gắn với xe, không với nhắc: bấm ở một nhắc, dải hiện trên nhắc khác của cùng xe. | [Gói: Bảo dưỡng đội xe] | Draft Work Order | FR-fleetio-reminders-inspection-040 | Bấm ở H, thấy ở C | `Chạy` |
| BR-fleetio-reminders-inspection-042 | Bản nháp tick sẵn mọi việc của xe, kể cả nhắc Upcoming còn xa; thêm vào lệnh rồi hoàn thành thì mất phần còn lại của chu kỳ (`Suy` từ BR-fleetio-reminders-inspection-016). | [Gói: Bảo dưỡng đội xe] | Draft Work Order | FR-fleetio-reminders-inspection-040 | Nhắc Upcoming 3 tháng được tick | `Chạy` phần tick sẵn |
| BR-fleetio-reminders-inspection-043 | Đổi chu kỳ, hoãn, đổi hạn gia hạn đều ghi Record History, không bắt lý do, không cảnh báo, không hiện ở History nghiệp vụ. | [Gói: Bảo dưỡng đội xe] | Sửa bản ghi | FR-fleetio-reminders-inspection-041 | Nhắc C, #1596560 | `Chạy` |
| BR-fleetio-reminders-inspection-044 | Bộ từ mẫu hệ thống có Primary Meter "Miles" cố định lúc tạo, không chọn được đơn vị; Edit sau đó có Miles, Kilometers, Hours. Chưa biết số có quy đổi khi đổi không. | [Gói: Bảo dưỡng đội xe] | Tạo bộ từ mẫu | FR-fleetio-reminders-inspection-043 | #591701 | `Chạy` |
| BR-fleetio-reminders-inspection-045 | Nhắc riêng theo đồng hồ phụ được phép ở mức bộ lịch: một dòng lịch chỉ cần một trong 3 trục. | [Gói: Bảo dưỡng đội xe] | Thêm lịch | FR-fleetio-reminders-inspection-044 | #591702 | `Chạy` |
| BR-fleetio-reminders-inspection-046 | Rule theo thuộc tính không lưu được với Current Operator; lọc vẫn dùng được. Lý do giá trị đổi liên tục là `Suy`. Ngoài ra ô Rule khoá khi còn Sample Data, xem BR-fleetio-reminders-inspection-059. | [Gói: Bảo dưỡng đội xe] | Gán bộ | FR-fleetio-reminders-inspection-045 | #590923 | `Chạy` |
| BR-fleetio-reminders-inspection-047 | Gán biểu mẫu không đặt lịch thì không vào Inspection Schedules; Schedule "Off", vẫn làm phiếu được. Rule All Vehicles áp cả xe mới; Specific Vehicle là "manual override" bỏ qua mọi Rule (câu chữ trên form, chưa lưu Rule). | [Gói: Bảo dưỡng đội xe] | Gán xe | FR-fleetio-reminders-inspection-017 | #680174 | `Chạy` phần gán xe cụ thể; `Xem` phần Rule |
| BR-fleetio-reminders-inspection-048 | Lịch Daily đổi Upcoming sang Due Soon khi chưa tới hạn: cùng hạn 11/04, 12:17 giờ máy Upcoming, 14:42 giờ máy Due Soon. Mốc đổi có lẽ theo ngày tài khoản; lịch Daily có lẽ Due Soon gần như cả ngày. | [Gói: Bảo dưỡng đội xe] | Thời gian trôi | FR-fleetio-reminders-inspection-017 | Inspection Schedules | `Chạy` phần đổi; `Suy` phần mốc |
| BR-fleetio-reminders-inspection-049 | Cờ cấm ảnh có sẵn chỉ áp cho mục Photo. Ảnh xác minh đồng hồ luôn phải chụp webcam, dù cờ tắt. | [Gói: Bảo dưỡng đội xe] | Nộp phiếu | FR-fleetio-reminders-inspection-022, FR-fleetio-reminders-inspection-036 | #680174 | `Chạy` |
| BR-fleetio-reminders-inspection-050 | Tick Void ở mục đồng hồ không gỡ yêu cầu ảnh xác minh. | [Gói: Bảo dưỡng đội xe] | Nộp phiếu | FR-fleetio-reminders-inspection-036 | #680174 | `Chạy` |
| BR-fleetio-reminders-inspection-051 | Số đồng hồ trên phiếu bằng đúng số hiện tại được nhận, không báo trùng. | [Gói: Bảo dưỡng đội xe] | Nộp phiếu | FR-fleetio-reminders-inspection-036 | #126108655 | `Chạy` |
| BR-fleetio-reminders-inspection-052 | Workflow "If form is submitted" chạy ngay khi nộp, không hỏi, không phân biệt đạt hay lỗi: phiếu có mục Fail vẫn nộp và xe vẫn đổi trạng thái. | [Gói: Bảo dưỡng đội xe] | Nộp phiếu | FR-fleetio-reminders-inspection-016 | #126108655, Active sang In Shop | `Chạy` |
| BR-fleetio-reminders-inspection-053 | Workflow tắt và có mục lỗi: không tạo sự cố, phiếu hiện "Fail" kèm Acknowledge, Create Issue. | [Gói: Bảo dưỡng đội xe] | Nộp phiếu | FR-fleetio-reminders-inspection-019 | #126108655 | `Chạy` |
| BR-fleetio-reminders-inspection-054 | Create Issue từ Needs Action ghi người bấm là người mở ("opened this issue", không phải "by workflow"); Priority "Prioritizing" lúc đầu, chờ hệ thống gán. | [Gói: Bảo dưỡng đội xe] | Create Issue | FR-fleetio-reminders-inspection-019 | Issue #51 | `Chạy` |
| BR-fleetio-reminders-inspection-055 | Reopen không hỏi lý do; khối Resolution Details biến mất khỏi trang, Timeline không thêm dòng, chỉ Comment cũ còn; dòng lỗi quay lại tab Open Issue. Đây là chiều ngược của BR-fleetio-reminders-inspection-025: lỗi lại sau Resolved sinh sự cố mới, chỉ Reopen tay mới mở lại. | [Gói: Bảo dưỡng đội xe] | Reopen | FR-fleetio-reminders-inspection-019 | Issue #49 | `Chạy` |
| BR-fleetio-reminders-inspection-056 | Chưa chọn xe thì không có mục nào để trả lời và không lưu được; Tire Readings, Meter Entry sinh theo xe vừa chọn. | [Gói: Bảo dưỡng đội xe] | Làm phiếu | FR-fleetio-reminders-inspection-018 | #680174 | `Chạy` |
| BR-fleetio-reminders-inspection-057 | Phiếu Fleetio Go có toạ độ từng mục; ca lệch tối đa 37 m có `location_exception` false, `are_items_too_close` false, `items_completed_too_far_away_count` 0. Ngưỡng thật chưa đo vì chưa có ca dương. | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Nộp phiếu | FR-fleetio-reminders-inspection-021, FR-fleetio-reminders-inspection-047 | #126102722 | `Chạy (Fleetio Go)` |
| BR-fleetio-reminders-inspection-058 | Draft Work Order chỉ mở khi nhắc Due Soon hoặc Overdue; khoá theo trạng thái nhắc, không theo gói. | [Gói: Bảo dưỡng đội xe] | Resolve | FR-fleetio-reminders-inspection-040 | TEST-NHAC-E Upcoming, nhắc H Overdue | `Chạy` |
| BR-fleetio-reminders-inspection-059 | Ô "Save as a Service Program Rule" khoá khi tài khoản còn bật Sample Data, bấm không tick. Muốn thử phải Disable Sample Data, là thao tác cấp tài khoản. | [Gói: Bảo dưỡng đội xe] | Gán bộ | FR-fleetio-reminders-inspection-029, FR-fleetio-reminders-inspection-045 | Bộ #590923 | `Chạy` |
| BR-fleetio-reminders-inspection-060 | Gán bộ theo thuộc tính không lưu Rule là gán một lần theo kết quả lọc; xe mới không tự vào (`Suy`). | [Gói: Bảo dưỡng đội xe] | Gán bộ | FR-fleetio-reminders-inspection-029 | TEST-DAUKEO-2, tab Vehicles thành 2 | `Chạy` phần gán |
| BR-fleetio-reminders-inspection-061 | Set First Service là mốc tuyệt đối theo đồng hồ: "1st service at 5 month(s) or 3,200 kilometers", xe 100 km còn 3.100 km, không cộng từ số hiện tại. | [Gói: Bảo dưỡng đội xe] | Gán bộ | FR-fleetio-reminders-inspection-011 | TEST-DAUKEO-2 | `Chạy` |
| BR-fleetio-reminders-inspection-062 | Xe đã gán bộ: đầu việc của bộ xám kèm khoá ở form nhắc lẻ, chặn tạo trùng từ đầu. | [Gói: Bảo dưỡng đội xe] | Tạo nhắc | FR-fleetio-reminders-inspection-011 | TEST-DAUKEO-2 | `Chạy` |
| BR-fleetio-reminders-inspection-063 | Đầu việc Smart Upload gợi ý không gắn với nhắc đang chờ của xe: phiếu chỉ đóng nhắc nếu người dùng tự thêm đúng đầu việc. Dòng thêm tay giá 0 không đổi Total. | [Gói: Bảo dưỡng đội xe] | Nhập hoá đơn | FR-fleetio-reminders-inspection-048 | #57903305 | `Chạy` |
| BR-fleetio-reminders-inspection-064 | Smart Upload biểu mẫu đặt mọi mục bắt buộc; ô chọn, số, đồng hồ, ảnh trên giấy đều thành Free Text; nhãn dính cả chữ phụ trên giấy. | [Gói: Bảo dưỡng đội xe] | Tạo biểu mẫu | FR-fleetio-reminders-inspection-013 | #680309 | `Chạy` |
| BR-fleetio-reminders-inspection-065 | Màn Review tick "Prevent Use of Stored Photos" nhưng biểu mẫu tạo ra ghi Disabled; Location Exception Tracking vẫn Enabled. Là lệch giữa màn và kết quả, một lần đo. | [Gói: Bảo dưỡng đội xe] | Tạo biểu mẫu | FR-fleetio-reminders-inspection-013, FR-fleetio-reminders-inspection-022 | #680309 | `Chạy` |
| BR-fleetio-reminders-inspection-066 | Mục đạt cũng kích workflow: trigger đạt đổi trạng thái xe, không hỏi, không báo trên phiếu. Number ngoài dải và Dropdown "Fail item if chosen" tính là lỗi, kích trigger lỗi. | [Gói: Bảo dưỡng đội xe] | Nộp phiếu | FR-fleetio-reminders-inspection-016 | #126116461, #126116614 | `Chạy` |
| BR-fleetio-reminders-inspection-067 | Workflow ANY sinh mỗi mục lỗi một sự cố, nguồn trỏ phiếu. | [Gói: Bảo dưỡng đội xe] | Nộp phiếu | FR-fleetio-reminders-inspection-016 | #126116614: #56, #57, #58 | `Chạy` |
| BR-fleetio-reminders-inspection-068 | Mục đạt khi sự cố của mục còn mở vẫn được nối với sự cố đó, không hỏi xác nhận, không tự đóng. | [Gói: Bảo dưỡng đội xe] | Nộp phiếu | FR-fleetio-reminders-inspection-020, FR-fleetio-reminders-inspection-033 | #126116970 | `Chạy` |
| BR-fleetio-reminders-inspection-069 | Nộp phiếu trừ kho ngay, không bước duyệt; dòng từ phiếu không có Reason. | [Gói: Bảo dưỡng đội xe] | Nộp phiếu | FR-fleetio-reminders-inspection-046 | #126116970: 10 sang 7 | `Chạy` |
| BR-fleetio-reminders-inspection-070 | Assign to của Find a shop chỉ nhận người dùng và nhãn Fleetio Automation, không nhận liên hệ không có đăng nhập. | [Gói: Bảo dưỡng đội xe] | Giao ngoài | FR-fleetio-reminders-inspection-050 | Tìm TEST | `Chạy` |

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
| E-fleetio-reminders-inspection-014 | Thiếu ngày hoàn thành | "can't be blank", "Service Entry could not be created" | major | FR-fleetio-reminders-inspection-027 | Completion Date có gợi ý hôm nay nhưng chưa nhập | Nhập | `Chạy` |
| E-fleetio-reminders-inspection-015 | Thiếu đồng hồ trên phiếu | "requires a Odometer" | major | FR-fleetio-reminders-inspection-036 | Ở mục đồng hồ | Nhập | `Chạy` |
| E-fleetio-reminders-inspection-016 | Vượt hạn mức xe | "Your plan is limited to 5 vehicles"; toast "Vehicle could not be created" | major | FR-fleetio-reminders-inspection-001 | Form New Vehicle | Nâng gói, lưu trữ xe; xe Sample không tính | `Chạy` |
| E-fleetio-reminders-inspection-017 | Biểu mẫu chưa gán | "No options", "No results for ..." ở ô chọn xe; "No inspection forms exist yet" ở mooc chưa gán | major | FR-fleetio-reminders-inspection-017 | Danh sách rỗng, câu chữ gây hiểu nhầm | Gán xe, chờ xử lý ngầm | `Chạy` |
| E-fleetio-reminders-inspection-018 | Thiếu Note khi giải quyết | Note bắt buộc, gợi ý "Describe what work was performed to resolve the issue."; câu lỗi chưa ghi lại | minor | FR-fleetio-reminders-inspection-019 | Hộp Resolve with Note | Nhập Note | `Chạy` |
| E-fleetio-reminders-inspection-019 | Rời phiếu đang làm | "Leave site?" của trình duyệt | major | FR-fleetio-reminders-inspection-018 | Hộp trình duyệt | Ở lại; rời là mất phiếu, không có nháp | `Chạy` |
| E-fleetio-reminders-inspection-020 | Thiếu ảnh đồng hồ | "must attach an odometer image"; toast E-fleetio-reminders-inspection-006 | major | FR-fleetio-reminders-inspection-036 | Ở mục Meter Entry Photo Verification; Void không gỡ được | Chụp bằng webcam; hoặc admin tắt Require Photo Verification trên biểu mẫu | `Chạy` |
| E-fleetio-reminders-inspection-021 | Không có camera | "Webcam Disabled", "Please enable your webcam to take a photo." | major | FR-fleetio-reminders-inspection-022, FR-fleetio-reminders-inspection-036 | Hộp chụp ảnh, không có đường chọn file; mục bắt buộc thì không nộp được phiếu | Bật camera; riêng mục Photo: admin tắt cờ cấm ảnh có sẵn | `Chạy` |
| E-fleetio-reminders-inspection-022 | Nộp khi ảnh đang tải | "is required" dù ảnh xem trước đã hiện | minor | FR-fleetio-reminders-inspection-022 | Ở mục Photo, chữ sai ngữ cảnh | Chờ "File uploaded: ...", bấm lại | `Chạy` |
| E-fleetio-reminders-inspection-023 | Mục kho thiếu nhãn | "can't be blank"; toast "Inspection Form could not be updated" | major | FR-fleetio-reminders-inspection-014 | Ở ô nhãn mục Inventory Adjustment khi dựng biểu mẫu | Nhập nhãn | `Chạy` |
| E-fleetio-reminders-inspection-024 | Hết hạn mức bản ghi | Nút "Save Vehicle", "Add Multiple Vehicles" khoá sẵn, tooltip "You've reached the maximum number of records allowed on your account." | major | FR-fleetio-reminders-inspection-001 | Form New Vehicle, trước khi bấm; khác E-fleetio-reminders-inspection-016 báo sau khi bấm | Nâng gói, lưu trữ xe | `Chạy` |
| E-fleetio-reminders-inspection-025 | Thuộc tính không tự động hoá được | Cảnh báo vàng "We are unable to automate this program because the following attribute has been selected. Current Operator" | minor | FR-fleetio-reminders-inspection-045 | Trên màn Add Vehicles; lọc vẫn dùng được, Rule không lưu | Đổi thuộc tính | `Chạy` |
| E-fleetio-reminders-inspection-026 | Không khớp xe | Nút "Add Service Program Vehicles" khoá, tooltip "No Vehicles have been found" | minor | FR-fleetio-reminders-inspection-045 | Hai nút lưu có icon khoá | Đổi điều kiện | `Chạy` |
| E-fleetio-reminders-inspection-027 | Smart Upload treo | "Taking longer than usual...", "Our system might be spinning its wheels here. You can wait, or restart the processing to get things moving again." | minor | FR-fleetio-reminders-inspection-013 | Hộp khoá toàn form | Chờ, Restart Processing, hoặc đóng và xác nhận Discard; lần thử lại sau đó chạy được | `Chạy` |
| E-fleetio-reminders-inspection-028 | Thiếu đồng hồ phụ | "requires a Secondary Meter"; toast E-fleetio-reminders-inspection-006 | major | FR-fleetio-reminders-inspection-036 | Ở ô Secondary Meter, xe có đồng hồ phụ | Nhập số | `Chạy` |
| E-fleetio-reminders-inspection-029 | Rule bị khoá khi còn Sample Data | Tooltip kết thúc bằng "...while sample data is turned on"; bấm không tick | minor | FR-fleetio-reminders-inspection-029, FR-fleetio-reminders-inspection-045 | Ô Save as a Service Program Rule | Disable Sample Data, thao tác cấp tài khoản, chưa làm | `Chạy` |
| E-fleetio-reminders-inspection-030 | Draft Work Order chưa mở | Tooltip "Available when this reminder is due soon or overdue." | minor | FR-fleetio-reminders-inspection-040 | Mục xám, icon khoá trên nhắc Upcoming | Chờ tới ngưỡng | `Chạy` |
| E-fleetio-reminders-inspection-031 | Không tìm được người nhận | "No results for 'TEST'" ở ô Assign to | minor | FR-fleetio-reminders-inspection-050 | Hộp Assign outsourced service | Chọn người dùng có đăng nhập | `Chạy` |

## 7. Success Criteria

| ID | Outcome nghiệp vụ | Đo bằng | Mốc đạt |
|---|---|---|---|
| SC-fleetio-reminders-inspection-01 | Không xe nào quá hạn mà không ai biết | Số xe Overdue chưa có người, lệnh xử lý | TBD |
| SC-fleetio-reminders-inspection-02 | Lỗi kiểm tra đều có đường xử lý | Số mục ở Needs Action quá lâu | TBD |
| SC-fleetio-reminders-inspection-03 | Giảm kiểm khống | Tỉ lệ phiếu Location Exception, thời lượng phiếu | TBD |

## 8. Data Entities (tóm tắt — chi tiết ở erd.md)

Service Reminder, Service Task, Compliance Record, Service Program, Program Schedule, Program Vehicle, Program Rule, Renewal Reminder, Renewal Type, Inspection Form, Form Version, Inspection Item, Workflow, Schedule Rule, Submission, Submitted Item, Item Failure, Meter Entry, Location Entry, Work Order Draft, Record History Entry. Xem [[docs/_research/fleetio/srs/fleetio-reminders-inspection-erd.md|ERD]].

## 9. Flows (tóm tắt — chi tiết ở flows.md)

Xem [[docs/_research/fleetio/srs/fleetio-reminders-inspection-flows.md|Flows]], [[docs/_research/fleetio/srs/fleetio-reminders-inspection-states.md|States]], [[docs/_research/fleetio/srs/fleetio-reminders-inspection-usecases.md|Use case]], [[docs/_research/fleetio/srs/fleetio-reminders-inspection-userflow.md|User flow]].

## 10. Screens

Ảnh thật và bảng mô tả: [[docs/_research/fleetio/srs/fleetio-reminders-inspection-screens.md|Màn hình]]. Không áp `CMP`, `GR` vì mô tả sản phẩm của bên khác.

## 11. Constraints, Dependencies & Assumptions

| Giả định | Invalidate nếu sai |
|---|---|
| `GĐ` Fleetio Go có cùng luật phiếu với web | Đã biết một điểm khác: vị trí từng mục chỉ có trên Fleetio Go (`Chạy (Fleetio Go)`). Xác nhận lại sau sửa, ngoại tuyến, ảnh webcam trên app chưa kiểm |
| `GĐ` GPS điện thoại đủ tốt ở bãi | Ngưỡng chống kiểm khống vô tác dụng |

**Không nên học:**

- Mốc đồng hồ tính từ 0 cho nhắc chưa có lịch sử: đầu kéo đã chạy nhiều bị Overdue ngay.
- Sửa chu kỳ xoá trắng quá hạn, Snooze và Acknowledge không có lý do, ngày hoãn đã qua vẫn báo thành công.
- Gia hạn: Record History ghi đổi hạn; không có chứng từ theo kỳ, không bắt lý do.
- Dùng lẫn giờ thiết bị và giờ tài khoản.
- Tin toạ độ gửi lên mà không đối chiếu.
- Mở Edit rồi lưu làm Notifications tự bật.
- Bản nháp AI tick sẵn cả việc còn xa: bấm nhanh là làm sớm và mất phần còn lại của chu kỳ.
- Bắt webcam mà không có đường dự phòng: máy không có camera thì phiếu không nộp được; cờ cấm ảnh và ảnh đồng hồ theo hai luật khác nhau.
- Workflow nộp phiếu đổi trạng thái xe không phân biệt đạt, lỗi và không hỏi: một phiếu đạt cũng đưa xe vào xưởng.
- Reopen làm mất khối Resolution Details và không để lại dòng Timeline.
- Mục đạt cũng đổi được trạng thái xe mà không hỏi, không báo trên phiếu.
- Trừ kho từ phiếu không có bước duyệt, không có lý do.
- Màn Review Smart Upload tick một cờ mà kết quả lưu cờ khác; đoán nhầm mọi loại mục đặc biệt thành Free Text.
- Bộ lịch từ mẫu cố định Miles, không chọn được km lúc tạo.
- Chữ lỗi "is required" khi ảnh còn đang tải; chữ "behind" đỏ trên dòng On-Time.

Bản trước ghi "mục lốp chặn nộp phiếu chỉ vì xe chưa khai trục, lái xe không tự sửa được". Đã sửa: người kiểm khai trục được ngay trong phiếu (E-fleetio-reminders-inspection-004).

## 12. Open Questions

* [ ] OQ-1: Delta có kiểm tra xe trước chuyến không? — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-2: Chu kỳ bảo dưỡng theo km, tháng hay cả hai, theo dòng xe? — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-3: Giấy tờ nào cần nhắc, báo trước bao lâu? — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-4: Phiếu kiểm hỏng có cho xe chạy tiếp không? — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-5: Mooc, máy phát có lịch riêng theo giờ chạy không? — Nguồn khách: Đề xuất tiện ích GPS (25/9/2025), mục 3
* [ ] OQ-6: Thay đồng hồ thì mốc km của nhắc xử lý thế nào? Chưa thử Meter Replacement. Đã biết Void số đồng hồ làm trạng thái lùi ngay — Nguồn khách: không áp dụng
* [ ] OQ-7: Phiếu không có vị trí có bị đánh dấu ngoại lệ không? Tắt vị trí có lách được chống kiểm khống không? Một phần: phiếu không vị trí vẫn nộp được (E-fleetio-reminders-inspection-007); toạ độ giả không bị chặn; mọi phiếu web thử đều `location_exception` false kể cả lệch khoảng 1.100 km giữa các phiếu; trên web không có vị trí từng mục. Fleetio Go có vị trí từng mục, ca lệch tối đa 37 m vẫn false; chưa thử tắt định vị trên app và chưa có ca dương (`Chạy (vị trí giả lập)`, `Chạy (Fleetio Go)`) — Nguồn khách: không áp dụng
* [x] OQ-8: Lần kiểm sau lỗi lại khi sự cố còn mở thì trùng hay gộp? Trả lời: gộp vào sự cố đang mở, thêm một mốc Failure Timeline, mỗi lần lỗi vẫn là một dòng Item Failures; không báo gì cho người kiểm khi đang làm phiếu (`Chạy`, #126056570 vào Issue #31) — Nguồn khách: không áp dụng
* [ ] OQ-9: Lưu vị trí lái xe, ảnh, chữ ký cần thông báo, đồng ý, thời hạn lưu thế nào theo quy định dữ liệu cá nhân? Cần pháp chế xác nhận — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-10: Mooc không đồng hồ, xe giờ máy, đồng hồ phụ, phiếu riêng đầu kéo và mooc chạy thế nào? Bị chặn bởi hạn mức 5 xe, thử 3 lần trong lượt 3 đều khoá (E-fleetio-reminders-inspection-024); cần được phép lưu trữ xe TEST không dùng. Một phần: lịch chỉ theo đồng hồ phụ lưu được ở mức bộ lịch; Require Secondary Meter bị bỏ qua êm trên xe không có đồng hồ phụ, xe có thì bắt nhập (#126116461). Nhắc theo giờ máy trên xe thật, mooc không đồng hồ, phiếu riêng đầu kéo và mooc chưa chạy — Nguồn khách: không áp dụng
* [ ] OQ-11: Lịch kiểm Overdue, Skipped đi thế nào? Cần qua hạn thật; Set Delayed Start không đặt được hạn quá khứ nên không rút ngắn được. Một phần: Due Soon đã thấy thật, cùng hạn 11/04 đổi từ Upcoming sang Due Soon, "22 hours from now" (`Chạy`); mốc đổi theo ngày tài khoản là `Suy` — Nguồn khách: không áp dụng
* [ ] OQ-12: Gỡ xe khỏi bộ lịch thực tế xoá gì, có lịch sử tuân thủ không? Dừng ở hộp xác nhận; nút duy nhất là Delete, không bấm vì brief cấm xoá — Nguồn khách: không áp dụng
* [x] OQ-13: Create Issue từ Needs Action và Reopen sự cố đi đâu? Trả lời: Create Issue một cú bấm, không form, sang trang sự cố mới, dòng lỗi sang Open Issue (Issue #51). Reopen hỏi xác nhận không hỏi lý do, sự cố về Open, Resolution Details biến mất, Timeline không thêm dòng, dòng lỗi về Open Issue (Issue #49). Phần Record History của sự cố tách ra OQ-18 (`Chạy`) — Nguồn khách: không áp dụng
* [ ] OQ-14: Fleetio Go có hỏi xác nhận lại sau khi sự cố đã giải quyết, có làm phiếu ngoại tuyến không? Một phần: Fleetio Go có vị trí từng mục, 21/21 mục của phiếu #126102722 (`Chạy (Fleetio Go)`); xác nhận lại, ngoại tuyến chưa kiểm; trên web mục đạt chỉ nối với sự cố đang mở, không hỏi xác nhận — Nguồn khách: không áp dụng
* [ ] OQ-15: Send an email, Assign user, Unassign user của workflow chạy thế nào? Chưa chạy vì có thể gửi ra ngoài. Một phần: Photo, trigger form submitted, trigger đạt và lỗi từng mục, đổi trạng thái, Inventory Adjustment trừ kho đã chạy (`Chạy`) — Nguồn khách: không áp dụng
* [ ] OQ-16: Lưu biểu mẫu không đổi gì có sinh phiên bản mới không? Một phần: dung sai dưới 10%, trục đồng hồ trễ đúng 100 trên 1.000 km Late, 99 km On-Time; trục ngày trễ 9 ngày On-Time, 10 ngày Late; nhiều lần trên một nhắc là số lần đúng hạn trên số lần làm; Draft Work Order khoá theo trạng thái nhắc, không theo gói (`Chạy`) — Nguồn khách: không áp dụng
* [ ] OQ-17: Làm sớm hơn mốc thì Delta chấp nhận mất phần còn lại của chu kỳ, hay hợp đồng bảo dưỡng theo km đòi giữ mốc cũ? — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-18: Reopen có lưu vết ở Record History của sự cố không? Chưa mở — Nguồn khách: không áp dụng
* [x] OQ-19: Draft Work Order xám trên nhắc Upcoming là khoá theo trạng thái hay do lúc đó? Trả lời: khoá theo trạng thái, tooltip "Available when this reminder is due soon or overdue." (`Chạy`) — Nguồn khách: không áp dụng
* [ ] OQ-20: Bộ từ mẫu đổi Miles sang Kilometers ở Edit thì số trong lịch có quy đổi không? Chưa thử — Nguồn khách: không áp dụng
* [ ] OQ-21: Lưu Rule theo thuộc tính thì xe mới có tự vào bộ lịch không? Bị chặn: ô Rule khoá khi còn Sample Data, phải Disable Sample Data ở cấp tài khoản — Nguồn khách: không áp dụng
* [ ] OQ-22: Cột Submitted At ở Item Failures lệch đầu phiếu (3:41pm so với 3:49pm, Started 3:40pm) vì sao? Có thể lấy mốc lần nộp hỏng đầu (`Suy`) — Nguồn khách: không áp dụng
* [ ] OQ-23: Số đồng hồ 3.100 km trên phiếu Fleetio Go có icon lạ, xe vẫn hiện 2.999 km: đây là số bị từ chối hay chờ duyệt? Chưa kiểm — Nguồn khách: không áp dụng
* [ ] OQ-24: Delta muốn ảnh kiểm tra bắt chụp trực tiếp hay cho tải file, thiết bị không có camera thì sao? Câu hỏi đề xuất từ kết quả Fleetio — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-25: Mức ưu tiên sự cố tự sinh theo luật nào? Brakes "Critical", Number và Dropdown "No Priority" trên cùng phiếu, chưa có câu giải thích — Nguồn khách: không áp dụng
* [ ] OQ-26: Bấm ASAP ở Find a shop làm Continue khoá, không gọi máy chủ: lỗi hay cần thao tác khác? Danh sách cửa hàng ở bước Suggest Shop không hiện ở tài khoản này — Nguồn khách: không áp dụng
* [ ] OQ-27: Dòng "Always require a review when ..." trong khối Assessment là gợi ý mẫu hay do người khác tạo? Chưa rõ, không thêm rule — Nguồn khách: không áp dụng

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
| C23 Snooze từ Due Soon | | Chưa bấm trực tiếp; từ Upcoming xem C103. Nhắc G bỏ hoãn về Due Soon nhưng không ghi trạng thái lúc hoãn | Chưa chạy |
| C24 Void số cao nhất | Void 3.001 | Đồng hồ 3.000, B vẫn Overdue | `Chạy` |
| C25 Void tiếp | Void 3.000 | Đồng hồ 2.999, B về Due Soon; không hỏi lý do | `Chạy` |
| C26 Đổi chu kỳ khi quá hạn | 1.000 → 5.000 km | Overdue → Upcoming, "2,001 kilometers remaining"; KHÔNG cảnh báo, KHÔNG bắt lý do, KHÔNG hiện ở tab History; có ghi ở Record History (C105) | `Chạy` |
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
| C39 Draft Work Order | D Upcoming | Xám, có icon khoá, bấm KHÔNG phản hồi; khoá theo trạng thái (C196); trên Overdue chạy được (C95) | `Chạy` |
| C40 Tuân thủ lọc theo xe | 5 nhắc đã làm | 60%, trung bình đều | `Chạy` |
| C41 KPI theo xe | 2 nhắc Overdue, 1 xe | "Overdue Vehicles 1" | `Chạy`, `reminder-list-compliance.jpg` |
| C42 Recalculate | Nhắc chưa làm | Xám | `Chạy` |
| C43 Gán bộ lịch trùng nhắc tay | B đã có | Giữ mã #17071895, thay chu kỳ, Due Soon → Upcoming; KHÔNG hỏi từng nhắc | `Chạy` |
| C44 Gán bộ, đầu việc mới | A | Sinh nhắc Upcoming | `Chạy` |
| C45 Bộ lịch khác đơn vị | Xe Sample dùng mi | Không có trong ô chọn | `Chạy` |
| C46 Trong lúc đồng bộ bộ lịch | Khoảng 1 phút | Nhắc B chưa đổi | `Chạy` |
| C47 Sửa bộ lịch | 4.000 → 3.000, lần đầu 4.500 → 3.200 | B thành Due Soon, 201 km, sau xử lý ngầm; KHÔNG hỏi | `Chạy` |
| C48 Gỡ xe khỏi bộ | Hộp xác nhận | Không bấm vì brief cấm xoá, hệ quả chưa kiểm; nút duy nhất là Delete | `Xem` |
| C49 Gia hạn đến hạn hôm nay | Registration, ngưỡng 3 tuần | Due Soon, "19 hours from now" (khác nhắc bảo dưỡng) | `Chạy` |
| C50 Gia hạn ngày đã qua | 01/10 | Overdue, "1 month ago" | `Chạy` |
| C51 Gia hạn xử lý thế nào | Mở chi tiết | KHÔNG có Resolve, tab History, tải giấy tờ; chỉ sửa Due Date; dấu vết ở Record History (C138) | `Chạy` |
| C52 Trùng gia hạn | Cùng xe, cùng loại | Dòng xám, không chọn được | `Chạy` |
| C53 Gia hạn liên hệ | License Renewal, ngưỡng thật 3 tuần (ghi chú đầu ghi 4 tuần là sai) | Due Soon, "18 hours from now", 1 watcher | `Chạy` |
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
| C77 Ưu tiên sự cố tự sinh | Lượt trước | Pass/Fail High, Dropdown No Priority; lượt 4 khác, xem C218 | `Chạy` |
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
| C93 Location Exception, phiếu từ Fleetio Go | #126102722, 21 mục, lệch tối đa 37 m | False; 21/21 mục có toạ độ riêng, 7 điểm khác nhau; `are_items_too_close` false, `items_completed_too_far_away_count` 0 | `Chạy (Fleetio Go)` |
| C94 Menu Resolve | Nhắc H Overdue | 2 nhóm GET SERVICE, LOG COMPLETED SERVICE; Find a shop không bấm | `Chạy`, `reminder-resolve.jpg` |
| C95 Draft Work Order trên Overdue | Nhắc H | KHÔNG khoá theo gói; toast "Drafting service"; xong dưới 2 phút, dải "Work Order drafted" | `Chạy` |
| C96 Phạm vi bản nháp | Bấm từ một nhắc | Gom toàn xe, "13/13 Service Tasks", KHÔNG chỉ nhắc đang bấm | `Chạy`, `reminder-draft-work-order.jpg` |
| C97 Ghép sự cố với đầu việc | Xe có sự cố đang mở | Nhóm "Resolves ...": sự cố áp suất thành Tire & Wheel Assembly Inspect, sự cố gai thấp thành Tire Replacement, do AI chọn | `Chạy`, `reminder-draft-work-order.jpg` |
| C98 Nhắc còn xa trong bản nháp | Upcoming 3 tháng | Vẫn tick sẵn trong nhóm "Due for maintenance" | `Chạy` |
| C99 Ước tính tiền | Lịch sử chỉ có một đầu việc | "Est. Subtotal (1 of 13 estimated)" 9.000 ₫, dòng khác "No estimate available" | `Chạy`, `reminder-draft-work-order.jpg` |
| C100 Xe đang có lệnh mở | Work Order #105 | "A Work Order is already open for this vehicle", "Add to" có 2 lựa chọn; "Will auto-fill when created": Non-Scheduled, Today, Open | `Chạy`, `reminder-draft-work-order.jpg` phần trên |
| C101 Bản nháp gắn với đâu | Bấm ở H | Dải hiện trên trang C cùng xe | `Chạy` |
| C102 Discard bản nháp | Review draft rồi Discard | KHÔNG sinh lệnh | `Chạy` |
| C103 Snooze Upcoming | Nhắc C, mặc định | Status "Snoozed", Next Due giữ "3 months from now", "2,001 kilometers remaining" | `Chạy` |
| C104 Remove Snooze trên Upcoming | Nhắc C | Về "Upcoming", không hỏi | `Chạy` |
| C105 Record History đổi chu kỳ | Đổi 1.000 → 5.000 | Ghi "Primary Meter Interval changed from 1000.0 to 5000.0", "Due Soon Meter Value changed from 500.0 to 4500.0", "Next Due Meter changed from 1000.0 to 5000.0", kèm ngày giờ và người | `Chạy`, `reminder-record-history.jpg` |
| C106 Record History khi hoãn | Hoãn, bỏ hoãn | Ghi "Snooze Until changed from (empty) to ..." và chiều ngược | `Chạy`, `reminder-record-history.jpg` |
| C107 Menu Actions hàng loạt | Tick một dòng, chỉ đọc | Có Add to Work Order, Find a shop, Add to service history, Snooze, Remove Snooze, Add Watchers, Remove Watchers, Delete; KHÔNG có Draft Work Order, KHÔNG có giao nhắc | `Xem` |
| C108 Giao nhắc | Tìm lối vào trên web | Có cột Assignee, Assigned At; KHÔNG thấy nút giao ở chỗ đã mở; Send Notifications không bấm | `Xem` |
| C109 Trễ 10 ngày | H chu kỳ 3 tháng, hạn 01/10, làm 10/10 | "1 week, 3 days behind", Late | `Chạy`, `reminder-compliance-multi.jpg` |
| C110 Trễ 9 ngày | Hạn 11/10, làm 19/10 | "1 week, 2 days behind", On-Time, chữ "behind" vẫn đỏ | `Chạy`, `reminder-compliance-multi.jpg` |
| C111 Tỷ lệ nhiều lần | 2 lần trên H | Completed 2, Late 1, 50% | `Chạy`, `reminder-compliance-multi.jpg` |
| C112 Trung bình danh sách | Lọc TEST-XE-01 sau C111 | 60% thành "57% on-time"; khớp theo lần 4/7, KHÔNG khớp theo nhắc 58,3% | `Chạy`, một điểm đo |
| C113 Ghi lùi ngày | Service Entry ngày quá khứ, đồng hồ quá khứ | Nhận; kỳ sau từ lần làm, 01/19/2027; KHÔNG đổi đồng hồ hiện tại 2.999 | `Chạy` |
| C114 Đặt tay hạn cũ | Hạn cũ hơn hôm nay | KHÔNG chặn, Overdue ngay; hoàn thành đưa Manually Set Next Due về No | `Chạy` |
| C115 Biên Late trục đồng hồ | | Đã đo ở lượt 4, xem C189, C190 | `Chạy` |
| C116 Forecasting | Enable Forecasting | Không bật vì là Cài đặt cấp tài khoản | `Docs` |
| C117 Smart uploads trên phiếu dịch vụ | Khối Beta trên New Service Entry | Lượt 3 chưa tải; lượt 4 chạy, xem C184 | `Xem` |
| C118 Danh sách mẫu bộ lịch | New Service Program | 14 mẫu hệ thống; bộ tự tạo cũng hiện làm mẫu | `Chạy` |
| C119 Chọn mẫu | Heavy Duty Truck Long Haul | Hiện ngay "11 Service Reminders will be created", bảng Intervals, Service Task; ẩn lựa chọn đồng hồ | `Chạy` |
| C120 Đơn vị bộ từ mẫu | Tạo từ mẫu | Primary Meter "Miles" cố định, KHÔNG chọn được km lúc tạo; đổi ở Edit chưa thử (OQ-20) | `Chạy` |
| C121 Gom đầu việc | Mẫu 11 đầu việc | Thành 6 dòng lịch | `Chạy` |
| C122 Lịch chỉ đồng hồ phụ | Kilometers, phụ Hours, nhập 200 giờ | Lưu được "Every 200 hours"; ngưỡng tự điền 50 hr | `Chạy` |
| C123 Gắn xe có đồng hồ phụ | Cần xe riêng | Không tạo được xe; chưa sinh nhắc | Chưa chạy |
| C124 Rule theo Current Operator | Chọn thuộc tính | E-025; lọc được, KHÔNG lưu thành Rule | `Chạy` |
| C125 Rule theo Make | Chọn thuộc tính | KHÔNG cảnh báo; giá trị chỉ liệt kê cái đang có. Ghi "ô Rule dùng được" ở lượt 3 là sai: ô khoá khi còn Sample Data (C180) | `Chạy` |
| C126 Không khớp xe | Điều kiện rỗng kết quả | E-026, nút lưu khoá | `Chạy`, `program-vehicles-add.jpg` trạng thái khoá |
| C127 Xe mới tự vào Rule | | Chặn: Rule khoá khi còn Sample Data; chưa biết (OQ-21) | Chưa chạy |
| C128 Gỡ xe khỏi bộ lịch lượt 3 | Nút duy nhất là Delete | Không bấm, OQ-12 vẫn mở | Chưa chạy |
| C129 Tạo xe khi đủ 5/5 | TEST-NHAC-02, thử 3 lần, lần cuối sau gần 4 giờ | E-024, nút khoá sẵn; khác C92 báo sau khi bấm. Không có lựa chọn "không đồng hồ" trên form | `Chạy` |
| C130 Gán biểu mẫu không lịch | #680174, Specific Vehicle | Add Via "Manual", Form Status "Enabled", Schedule "Off", Frequency trống; KHÔNG vào Inspection Schedules | `Chạy` |
| C131 Lịch Daily sang Due Soon | Hạn 11/04 không đổi, 12:17 rồi 14:42 giờ máy | Upcoming "1 day from now" thành Due Soon "22 hours from now", tab Due Soon (2) | `Chạy`, `inspection-schedule-due-soon.jpg` |
| C132 Lịch Overdue, Skipped | | Tab rỗng, cần qua hạn thật (OQ-11) | Chưa chạy |
| C133 Tần suất lịch | Bộ lọc Frequency | Chỉ Daily, Weekly, Monthly, Yearly; KHÔNG có lịch theo số đồng hồ | `Chạy` |
| C134 Mở gia hạn liên hệ | Bấm dòng TEST-NHAC-LX | Panel phải "Contact Renewal #1596560", có Edit, "..." gồm View, Send Notifications, View Record History, Delete | `Chạy` |
| C135 Trang chi tiết gia hạn liên hệ | Mở trang | Chỉ Details, Comments; KHÔNG Resolve, KHÔNG tab History, giống gia hạn xe | `Chạy` |
| C136 Edit gia hạn liên hệ | Mở Edit | Khoá Contact, Contact Renewal Type | `Chạy` |
| C137 Sửa ngày gia hạn | Sang 11/01/2027 | Status "Upcoming", "1 year from now" | `Chạy` |
| C138 Record History gia hạn | Sau khi sửa | Ghi "Next Due At changed from ... to ...", "Due Soon At changed from ... to ..."; KHÔNG có chứng từ, KHÔNG có khái niệm kỳ | `Chạy` |
| C139 Smart Upload biểu mẫu | Ảnh phiếu giấy TEST 9 dòng, chờ khoảng 4 phút, Restart một lần, chờ thêm khoảng 2 phút | E-027; KHÔNG ra bản dựng, form khoá, KHÔNG báo lỗi; thử lại chạy được (C202), nên là lỗi lúc đó | `Chạy` |
| C140 Đóng Smart Upload | Đóng hộp | Hỏi "Are you sure you'd like to discard this smart upload?" | `Chạy` |
| C141 Inventory Adjustment thiếu nhãn | Bỏ trống | E-023 | `Chạy` |
| C142 Nhãn Tire Readings | Thêm mục | Tự có nhãn và mô tả | `Chạy` |
| C143 Dấu bắt buộc mục kho | So 3 màn | Edit items có dấu đỏ; trang xem, form phiếu KHÔNG có; nộp trống được | `Chạy` |
| C144 Đủ 11 loại mục | #680174, cộng 8 loại lượt trước | Lưu được đủ; sau khi có Meter Entry ô panel khoá; tab Workflows tự có 1, Vehicles 0 | `Chạy` |
| C145 Workflow form submitted | "If form is submitted", Change vehicle status In Shop | Lưu được; Description tự điền; "Inspection Workflow was successfully updated" | `Chạy` |
| C146 Create an issue khi đã có workflow ANY | Mọi trigger | "Not Available", kể cả form submitted | `Chạy` |
| C147 Disable workflow | Hộp xác nhận | Danh sách chia Enabled, Disabled, dòng tắt có nhãn "Disabled"; menu dòng Edit, Disable, Delete | `Chạy`, `inspection-workflow-add.jpg` chỉ bước 1 |
| C148 Action còn lại | Send an email, Assign user | Không lưu vì có thể gửi đi; vẫn KHÔNG có action tạo lệnh | Chưa chạy |
| C149 Form chưa chọn xe | Start Inspection, chọn biểu mẫu | Chỉ có ô Vehicle, Save Inspection khoá; chọn xe mới bung mục | `Chạy` |
| C150 Lốp trên xe 4 vị trí | Chọn TEST-XE-01 | LF, LR, RR, RF; Tread Depth, Pressure đều bắt buộc | `Chạy` |
| C151 Require Secondary Meter trên xe không có | Bật trên biểu mẫu | Chỉ hiện Primary Meter, KHÔNG báo lỗi, KHÔNG chặn | `Chạy` |
| C152 Require Photo Verification | Bật | Thêm dòng bắt buộc "Meter Entry Photo Verification" | `Chạy` |
| C153 Chọn kho trên phiếu | Part Location | Hiện ô Parts, chỉ phụ tùng có ở kho đó kèm tồn; chọn thử rồi xoá | `Chạy` |
| C154 Cấm ảnh có sẵn bật | Pick File, không cấp camera | Hộp "Webcam Disabled", KHÔNG có đường chọn file; E-021; mục bắt buộc nên KHÔNG nộp được | `Chạy`, `inspection-photo-webcam-only.jpg` |
| C155 Cấm ảnh có sẵn tắt | Sửa biểu mẫu | "Pick File", "Or drop file here", nhận file, "File uploaded: test-photo.jpg" | `Chạy` |
| C156 Ảnh đồng hồ khi cờ đã tắt | Thiếu ảnh | Vẫn chỉ webcam, KHÔNG có "Or drop file here"; E-020 | `Chạy` |
| C157 Void đồng hồ để né ảnh | Tick Void | KHÔNG gỡ được, vẫn chặn | `Chạy` |
| C158 Nộp khi ảnh đang tải | Xem trước đã hiện | E-022 "is required"; bấm lại sau "File uploaded" thì qua | `Chạy` |
| C159 Đồng hồ bằng số hiện tại | 2.999 | Nhận, KHÔNG báo trùng, phiếu hiện "2,999 km" | `Chạy` |
| C160 Kho bỏ trống | Nộp | Phiếu ghi "No parts used" | `Chạy` |
| C161 Trừ kho | Lượt 3 | KHÔNG chạy: kho và phụ tùng TEST là của nhóm KHO; lượt 4 dùng phụ tùng riêng, xem C222 | Chưa chạy |
| C162 Lốp trong khoảng | 10/32, 100 PSI | "Pass" | `Chạy` |
| C163 Lỗi khi workflow lỗi tắt | Phanh Fail, chỉ có workflow form submitted | "Fail" kèm Acknowledge, Create Issue; KHÔNG tạo sự cố | `Chạy` |
| C164 Workflow đổi trạng thái xe | Nộp #126108655 | Active sang "In Shop" ngay, KHÔNG có hộp hỏi | `Chạy` |
| C165 Phiếu có Fail, trigger form submitted | Như trên | Vẫn nộp, vẫn đổi trạng thái; KHÔNG phân biệt đạt hay lỗi | `Chạy` |
| C166 Đầu phiếu | #126108655 | Duration 8m 58s tính cả lúc mở form; Job "Unassigned"; "Fleetio Web App" | `Chạy` |
| C167 Create Issue từ Needs Action | Row menu | Một cú bấm, KHÔNG mở form; "Inspection Item was linked to an Issue."; Issue #51 Open; dòng lỗi sang Open Issue | `Chạy` |
| C168 Người mở, ưu tiên | Issue #51 | "opened this issue", KHÔNG phải "by workflow"; Priority "Prioritizing" | `Chạy` |
| C169 Reopen | Issue #49 Resolved | Hộp "Reopen Issue(s)", KHÔNG hỏi lý do; "Successfully reopened Issue."; nút lại thành Resolve | `Chạy` |
| C170 Dấu vết sau Reopen | Issue #49 | Resolution Details biến mất, Timeline KHÔNG thêm dòng, chỉ Comment cũ còn; Record History chưa mở (OQ-18) | `Chạy` |
| C171 Dòng lỗi sau Reopen | #126056430 | Quay lại tab Open Issue với "Issue #49" | `Chạy` |
| C172 Giờ trên danh sách lỗi | #126108655 | Submitted At 3:41pm, đầu phiếu Submitted 3:49pm, Started 3:40pm: lệch, chưa rõ (OQ-22) | `Chạy` |
| C173 Xác nhận lại sau sửa trên Fleetio Go | | Không thử được trên web, chưa làm trên app (OQ-14) | Chưa chạy |
| C174 Toạ độ cấp phiếu trên Fleetio Go | #126102722 | `starting_latitude` vẫn null dù phiếu có giờ bắt đầu | `Chạy (Fleetio Go)` |
| C175 Đồng hồ trên phiếu Fleetio Go | 3.100 km | Có icon lạ, xe vẫn 2.999 km; chưa kiểm vì sao (OQ-23) | `Chạy (Fleetio Go)` |
| C176 Location Exception bật thật | | Chưa có ca dương, chưa biết ngưỡng (OQ-7) | Chưa chạy |
| C177 Trạng thái xe sau trả lại | Edit Vehicle về Active | Trang xe Active; xe ở In Shop khoảng 10 đến 15 phút | `Chạy` |
| C178 Gán bộ theo thuộc tính | Make Honda, Type Semi Truck | "1 Vehicle will receive 2 Service Reminders ..."; Conflicting, Duplicate trống; New Interval "Every 6 month(s) or 3,000 kilometers" | `Chạy` |
| C179 Link "1 Vehicle" | Bấm | Mở tab mới lọc danh sách xe, đúng xe khớp; đọc được tiêu chí | `Chạy` |
| C180 Ô Rule khi còn Sample Data | Rê, bấm | E-029; bấm KHÔNG tick; không thử tắt Sample vì là cấp tài khoản | `Chạy` |
| C181 Lưu gán không Rule | Add Service Program Vehicles | "Service Program Vehicles was successfully created", tab Vehicles thành 2, có Date Added; vẫn hiện quảng bá Create a Service Program Rule | `Chạy` |
| C182 Nhắc sinh ra trên xe | Xe 100 km | 2 nhắc Upcoming, cột Service Program; "1st service at 5 month(s) or 3,200 kilometers" còn 3.100 km: mốc tuyệt đối | `Chạy` |
| C183 Tạo nhắc lẻ trùng sau gán | Form New Service Reminder | 2 đầu việc của bộ xám kèm khoá, KHÔNG chọn được | `Chạy` |
| C184 Smart Upload hoá đơn | Ảnh hoá đơn TEST | Dưới 30 giây đủ; đọc đúng đồng hồ 1100, ngày, Reference, Vendor khớp bản ghi, Tax 15, Total 165 | `Chạy`, `service-smart-upload-review.jpg` |
| C185 Dòng hoá đơn | "Oil change labor", "Oil filter" | Gộp thành 1 Service Task hệ thống, Labor 100, Parts 50; KHÔNG đoán đúng đầu việc TEST | `Chạy`, `service-smart-upload-review.jpg` |
| C186 Thêm dòng tay | Giá 0; dòng chưa chọn đầu việc | Total vẫn 165; "Add to Service Entry" khoá khi chưa chọn | `Chạy` |
| C187 Bấm Add to Service Entry | | Chỉ đổ vào form, KHÔNG lưu; phải Save; icon tài liệu trên xe tăng số | `Chạy` |
| C188 Nhắc đang chờ khi nhập hoá đơn | Đầu việc máy gợi ý | KHÔNG gắn với nhắc; phải tự thêm đúng đầu việc mới đóng nhắc | `Chạy` |
| C189 Trễ đúng 10% trục đồng hồ | Hạn 1.000, làm 1.100 | "100 kilometers behind", Late | `Chạy`, `reminder-compliance-km-boundary.jpg` |
| C190 Trễ dưới 10% trục đồng hồ | Hạn 2.100, làm 2.199 | "99 kilometers behind", On-Time, chữ vẫn đỏ; thẻ Completed 2, Late 1, 50% | `Chạy`, `reminder-compliance-km-boundary.jpg` |
| C191 Preview trên xe đã chạy | Xe 100 km, chu kỳ 1.000 | 1.000, 2.000, ... ("900 km from now"): bội số từ 0, KHÔNG phải 100 + 1.000 | `Chạy` |
| C192 Kỳ sau lần làm đầu | Làm 1.100 | Hạn 2.100, KHÔNG quay về 2.000 | `Chạy` |
| C193 Completion Date từ Resolve | Không gõ, gợi ý mờ | E-014; phiếu Smart Upload thì tự điền | `Chạy` |
| C194 Assessment, phiếu không giá | | "Add line item costs to run an assessment" | `Chạy` |
| C195 Assessment, phiếu có giá | #57903305 | "Assessing" hơn 5 phút, sau đó "Acceptable", "Auto-assessed ...", "6 sources"; không thêm rule | `Chạy` |
| C196 Draft Work Order trên Upcoming | TEST-NHAC-E, rê vào | E-030; khoá theo trạng thái, KHÔNG theo gói | `Chạy` |
| C197 Find a shop | Bấm trên Upcoming | Hộp "Assign outsourced service", 3 bước; mục Assign all thấy nhắc khác của xe | `Chạy` |
| C198 Assign to là liên hệ | Tìm TEST | E-031; chỉ người dùng, "Fleetio Automation", "Service Advisor" | `Chạy` |
| C199 Chọn người | | Cột Notification Methods, Email, Text Message tick sẵn | `Chạy` |
| C200 Bấm ASAP | | Continue khoá, KHÔNG gọi máy chủ; bỏ ASAP thì chạy (OQ-26) | `Chạy` |
| C201 Bước Suggest Shop, Assign | | Tích xanh, KHÔNG hiện cửa hàng; Confirm "Ready to assign"; KHÔNG bấm Assign vì gửi email, SMS thật | `Chạy` đến Confirm |
| C202 Smart Upload biểu mẫu, thử lại | Ảnh checklist TEST 8 mục | Dưới 30 giây có bản dựng; tạo #680309 | `Chạy`, `inspection-form-smart-upload-review.jpg` |
| C203 Loại mục máy chọn | 8 mục | Pass/Fail, Signature, Notes đúng; số, ô chọn, đồng hồ, ảnh thành Free Text | `Chạy` |
| C204 Bắt buộc, nhãn | | Cả 8 mục bắt buộc; nhãn dính chữ phụ như "Odometer reading km" | `Chạy` |
| C205 Cờ cấm ảnh qua Smart Upload | Review tick | Biểu mẫu tạo ra ghi Disabled; Location Exception Enabled | `Chạy` |
| C206 Sau khi tạo | #680309 | Có sẵn workflow lỗi tạo sự cố ANY; Vehicles & Schedules rỗng | `Chạy` |
| C207 Xe có đồng hồ phụ | Add Secondary Meter Hours | Form 2 ô km, hr, "Last updated: No meter history", mỗi ô một Void | `Chạy` |
| C208 Photo Verification hai đồng hồ | Bật rồi tắt | Bật: 2 dòng bắt buộc. Tắt: 2 dòng VẪN HIỆN, chỉ bỏ dấu bắt buộc; nộp được không ảnh | `Chạy` |
| C209 Trống đồng hồ phụ | Nộp | E-028, E-006 | `Chạy` |
| C210 Điền đồng hồ phụ | 10 | Phiếu #126116461 hiện "2,300 km", "10 hr" cùng mục | `Chạy` |
| C211 Thêm Meter Entry lần hai | Đã có một mục | Nút bên phải xám có khoá; nút nhân bản dòng cũng khoá | `Chạy` |
| C212 Chọn biểu mẫu từ xe | Hộp Select Inspection Form | Chỉ liệt kê biểu mẫu đã gán cho xe | `Chạy` |
| C213 Dựng lịch Overdue | Set Delayed Start | "The next due date will always be in the future."; KHÔNG đặt được hạn quá khứ; phải chờ thời gian thật | `Chạy` phần chặn |
| C214 Ô chọn mục của trigger | Lỗi và đạt | Chỉ Pass/Fail, Number, Dropdown; lỗi có ANY, đạt KHÔNG có; chọn được nhiều | `Chạy` |
| C215 Phiếu đạt, trigger đạt | #126116461, Brakes Pass | Xe sang Inactive ngay, KHÔNG hỏi, KHÔNG báo; KHÔNG sự cố | `Chạy` |
| C216 Phiếu nhiều mục lỗi | #126116614 | Xe sang Out of Service; 3 sự cố #56, #57, #58, mỗi mục một sự cố | `Chạy`, `inspection-workflow-fail-issues.jpg` |
| C217 Phiếu lỗi lại một mục | #126116970, Brakes Fail | KHÔNG đổi trạng thái; KHÔNG sự cố mới, gắn lại #56 | `Chạy` |
| C218 Ưu tiên cùng phiếu | #126116614 | #56 Critical; #57, #58 No Priority; chưa có câu giải thích (OQ-25) | `Chạy`, `inspection-workflow-fail-issues.jpg` |
| C219 Mục đạt khi sự cố mở | Number 15, Cao | Vẫn hiện "Issue #57", "Issue #58"; KHÔNG hỏi xác nhận, KHÔNG tự đóng | `Chạy` |
| C220 Làm phiếu khi xe Inactive | | Được; workflow vẫn chạy. Xe đã trả về Active bằng ô trạng thái đầu trang | `Chạy` |
| C221 Send an email, Assign, Unassign | | Không chạy vì có thể gửi ra ngoài (OQ-15) | Chưa chạy |
| C222 Trừ kho từ phiếu | #126116970, TEST-KHO-02, số lượng 3 | Inventory Activity -3.0, 10.0 sang 7.0, KHÔNG duyệt, Reason trống | `Chạy`, `inspection-inventory-adjustment-deduct.jpg` |
| C223 Phiếu hiển thị phụ tùng | Số lượng 3 | "TEST-KHO-02 • 1 parts": đếm dòng, KHÔNG đếm số lượng | `Chạy` |
| C224 Tìm phụ tùng trên phiếu | | Hiện tồn 10 ngay trong ô, số lượng mặc định 1, có đơn vị, nút xoá | `Chạy` |

## Phát hiện lượt 3 (03/11)

Nguồn: `run-notes/reminders-inspection.md`, mục Lượt 3.

- SỬA kết luận cũ: đổi chu kỳ và gia hạn CÓ dấu vết. Menu "..." có View Record History, ghi ai đổi trường nào, từ giá trị nào sang giá trị nào, kể cả chu kỳ, hoãn, hạn gia hạn. Điểm yếu thật là không bắt lý do, không cảnh báo.
- SỬA: ngưỡng mặc định gia hạn liên hệ là 3 tuần, không phải 4.
- Biên Late trên trục ngày: chu kỳ 3 tháng, trễ 9 ngày vẫn On-Time, 10 ngày là Late.
- Trung bình tuân thủ ở danh sách 57%, khớp cách tính theo lần (4/7), không theo nhắc (58%); mới một điểm đo.
- "Require Photo Verification" chỉ mở webcam dù đã tắt cờ cấm ảnh có sẵn; tick Void không gỡ được; máy không có camera thì không nộp được phiếu.
- Reopen sự cố từ mục lỗi không hỏi lý do, Resolution Details biến mất, Timeline không thêm dòng.
- Draft Work Order không khoá theo gói trên nhắc Overdue; AI gom mọi sự cố và nhắc của xe, tick sẵn cả việc còn 3 tháng.
- Smart Upload treo khoảng 6 phút, không ra bản dựng. Bộ lịch từ mẫu hệ thống tạo đồng hồ Miles.
- Fleetio Go: 21/21 mục có toạ độ riêng, lệch tối đa 37 m, `location_exception` false; chưa có ca dương.
- Workflow "If form is submitted" đổi xe sang In Shop ngay khi nộp, không phân biệt đạt, lỗi. Create Issue một cú bấm, ghi người bấm là người mở.
- Lịch kiểm có Due Soon thật; gán biểu mẫu không lịch thì không vào Inspection Schedules.

Đã đưa vào FR-fleetio-reminders-inspection-040 đến 047, BR-fleetio-reminders-inspection-038 đến 057, E-fleetio-reminders-inspection-020 đến 027, C94 đến C177.

## Phát hiện lượt 4 (03/11)

Nguồn: `run-notes/reminders-inspection.md`, mục Lượt 4.

- SỬA kết luận lượt 3: ô Rule của bộ lịch khoá khi còn Sample Data, ghi "dùng được" là sai.
- SỬA kết luận lượt 3: Draft Work Order khoá theo trạng thái nhắc, không theo gói; mở khi Due Soon hoặc Overdue.
- Dung sai Late là dưới 10%: đúng bằng 10% đã Late.
- Smart Upload chạy được cả hoá đơn và biểu mẫu, dưới 30 giây; lần treo 6 phút là lỗi lúc đó. Biểu mẫu đoán nhầm 4 loại mục thành Free Text, cờ cấm ảnh lưu lệch với màn Review.
- Mục đạt cũng đổi trạng thái xe; mỗi mục lỗi một sự cố; trừ kho từ phiếu không có bước duyệt.

Đã đưa vào FR-fleetio-reminders-inspection-048 đến 050, BR-fleetio-reminders-inspection-058 đến 070, E-fleetio-reminders-inspection-028 đến 031, C178 đến C224.
