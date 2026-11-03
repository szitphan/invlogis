# Chạy thử: Nhắc và Kiểm tra xe (phân tích ngược lần 2)

Tiền tố dữ liệu: `TEST-NHAC`. Ghi tăng dần, phần chưa làm ghi ở cuối file.

## Chặn đầu vào: không tạo được xe riêng — Không chạy được (giới hạn gói)
Các bước đã làm: New Vehicle, tên TEST-NHAC-01, đồng hồ 1000 km, Save Vehicle.
Kết quả thấy được: "Your plan is limited to 5 vehicles", toast "Vehicle could not be created". Ngay lúc đó có đúng 5 xe không phải Sample: TEST-XE-01, TEST-XE-LOP, TEST-MOOC-LOP (nhóm lốp), TEST-SUA-01, TEST-KHO-01 (hai xe sau do agent song song vừa tạo). Xe Sample không tính vào hạn mức.
Cách xử lý: KHÔNG lưu trữ xe nhóm khác, KHÔNG thử đường khác (Add Multiple Vehicles) để lách hạn mức. Dùng `TEST-XE-01` (tải dùng chung trong brief, chính xe chạy nhắc ở lần 1) làm xe thử. KHÔNG đổi cài đặt xe (loại, đơn vị đồng hồ, đồng hồ phụ).
Hệ quả: các case cần xe riêng (mooc không đồng hồ, xe dùng giờ máy, đồng hồ phụ, phiếu riêng đầu kéo và mooc) bị chặn, xem cuối file.

## Nhắc bảo dưỡng: tạo và kiểm tra form — Chạy
Các bước đã làm: Tạo 8 Service Task `TEST-NHAC-A..H`. New Service Reminder trên TEST-XE-01 (đồng hồ 2.300), task C. Lưu khi chưa có chu kỳ, rồi nhập ngưỡng lớn hơn và bằng chu kỳ.
Kết quả thấy được:
- Không chu kỳ: chữ đỏ ở cả hai ô "Please provide a usage or a time interval", toast "Service Reminder could not be created". Chỉ cần một trong hai trục.
- Ngưỡng ≥ chu kỳ: Schedule Preview báo "Primary Meter Due Soon Threshold is too high (can't be equal to or greater than Primary Meter Interval)"; tương tự "Time Due Soon Threshold is too high (can't be equal to or greater than Time Interval)". Bằng cũng bị chặn. Đổi đơn vị vẫn so đúng (20 tuần so với 3 tháng).
- Mặc định ngưỡng 2 tuần, 500 km. Đơn vị thời gian chọn được; ngưỡng có đơn vị riêng.
- Task chưa từng làm: dưới ô hiện "Never logged for this vehicle".
- BẤT NGỜ: mốc đồng hồ của nhắc CHƯA có lịch sử tính từ 0 theo bội số chu kỳ, không tính từ số hiện tại. Chu kỳ 1.000 km trên xe 2.300 km: preview ghi "1,000 km / 1,300 km ago", "2,000 km / 300 km ago", "3,000 km / 700 km from now". Lưu xong trạng thái Overdue ngay, Next Due "1,300 kilometers overdue". Thời gian thì tính từ hôm nay ("3 months from now").
- Trạng thái lấy trục xấu nhất: "3 months from now" kèm "1,300 kilometers overdue" vẫn là Overdue.
- Tạo nhắc chưa bật Notifications thì trang chi tiết ghi Notifications "Inactive". Watchers tự có người tạo.
Màn mới: reminder-detail-overdue (nút Unwatch, ..., Edit, Resolve; khối Details: Vehicle, Operator lấy từ phân công xe, Status, Service Task, Service Program, Next Due, Last Completed, Work Order, Time Interval, Meter Interval, Manually Set Next Due, Notifications; khối Next Due; tab History).
Dữ liệu TEST đã tạo: Service Task TEST-NHAC-A thoi gian, B dong ho, C ca hai, D lenh sua, E phieu dich vu, F hoan thanh som, G hoan roi xong, H manual due. Nhắc #17071869 (C: 3 tháng / 1.000 km), #17071895 (B: 3.000 km).

## Ngưỡng đồng hồ, biên — Chạy
Các bước đã làm: Nhắc B, mốc 3.000, ngưỡng 500, nhập đồng hồ từng bước qua Add Meter Entry (bấm số đồng hồ ở đầu trang xe).
| Đồng hồ | Còn lại | Trạng thái | Câu chữ |
|---|---|---|---|
| 2.300 | 700 | Upcoming | "700 kilometers remaining" |
| 2.499 | 501 | Upcoming | "501 kilometers remaining" |
| 2.500 | 500, đúng ngưỡng | Due Soon | "500 kilometers remaining" |
| 2.999 | 1 | Due Soon | "1 kilometers remaining" |
| 3.000 | 0, đúng mốc | Overdue | "0 kilometers remaining" |
| 3.001 | -1 | Overdue | "1 kilometers overdue" |
Kết luận: Due Soon khi còn lại ≤ ngưỡng (biên thuộc Due Soon). Overdue khi đồng hồ ≥ mốc (đúng mốc đã là Overdue dù chữ vẫn ghi "0 kilometers remaining"). Trạng thái đổi ngay khi lưu đồng hồ, không chờ job đêm.
Bất ngờ: chữ số ít sai ngữ pháp "1 kilometers".
Dữ liệu TEST đã tạo: đồng hồ TEST-XE-01 2.499, 2.500, 2.999, 3.000, 3.001.

## Snooze: form và ngày quá khứ — Chạy
Các bước đã làm: Nhắc C Overdue, menu "...", Snooze Service Reminder. Lần 1 chọn ngày đã qua 01/11/2026. Lần 2 chọn hôm nay 01:06 sáng theo giờ máy.
Kết quả thấy được:
- Hộp: "1 service reminder will be snoozed until the selected date and time. The reminder will return to its normal state after the snooze period is over." Mặc định +7 ngày (11/10/2026), giờ mặc định theo giờ thiết bị (Asia/Saigon), không phải giờ tài khoản (America/Chicago). Không có ô lý do. Không có mức chọn sẵn (1 tuần, 1 tháng): chỉ ngày và giờ tự do.
- Ngày quá khứ: KHÔNG chặn, toast "The Service Reminder was successfully updated.", trạng thái vẫn Overdue (thao tác vô hiệu, không báo).
- Hoãn hợp lệ: Status "Snoozed", dòng phụ "Snoozed until 11/03/2026". Next Due vẫn hiện "1,300 kilometers overdue" nhưng đổi sang màu xám. Menu "..." đổi "Snooze Service Reminder" thành "Remove Snooze". Resolve vẫn dùng được.

## Snooze: hết hạn, đồng hồ đổi trong lúc hoãn, hoãn rồi hoàn thành — Chạy
- Hết hạn: hoãn đến 01:06 (giờ máy). 01:04:30 vẫn "Snoozed". 01:07:06 đã về "Overdue" (không thấy trễ theo job đêm, chênh dưới 2 phút).
- Trong lúc hoãn đồng hồ tăng: số "kilometers overdue" vẫn đổi theo (1.300 → 2.000), trạng thái vẫn Snoozed.
- Hoãn rồi hoàn thành: nhắc G Snoozed đến 11/10, ghi Service Entry 2.460 km → hết Snoozed, về "Due Soon" (3.460 mốc mới, còn 461 km). Hoàn thành xoá hoãn, không hỏi. Vẫn bị tính "Late 1".
- Chưa bấm thử "Remove Snooze" đến lúc này (xem phần sau nếu có).

## Đồng hồ lùi, Void — Chạy
Các bước đã làm: Nhắc B (mốc 3.000) đang Overdue ở 3.001. Row menu đồng hồ: Edit, Void, View Record History, Delete. Void 3.001 rồi 3.000. Hộp: "This operation will attempt to void the selected Meter Entry."
Kết quả thấy được: "Successfully voided Meter Entry", dòng gạch ngang, Void Status "Manually Voided". Void 3.001 → đồng hồ xe 3.000 → B vẫn Overdue "0 kilometers remaining". Void 3.000 → đồng hồ 2.999 → B về "Due Soon" "1 kilometers remaining". Trạng thái lùi ngay, không hỏi lý do Void.
Đồng hồ hiện của xe sau bài này: 2.999.

## Đổi chu kỳ khi đang quá hạn — Chạy
Các bước đã làm: Nhắc C Overdue theo mốc 1.000, sửa chu kỳ 1.000 → 5.000 km.
Kết quả thấy được: lưu xong Status "Upcoming", "2,001 kilometers remaining". KHÔNG cảnh báo, không bắt lý do, không ghi vào History. Một lần sửa xoá trắng tình trạng quá hạn (lỗ hổng kiểm soát).
Bất ngờ: Schedule Preview trong form Edit không làm mới theo số mới ngay (vẫn hiện 1.000, 2.000, 3.000 sau 2 giây). Vehicle khoá khi Edit. Breadcrumb ghi "TEST-NHAC-C Ca Hai Reminder".
BẤT NGỜ: form Edit luôn hiện Notifications tick lại: nhắc đang "Inactive", mở Edit rồi lưu mà không đụng ô đó → thành "Active" (đã thấy ở cả C và H).

## Manually set due — Chạy
Các bước đã làm: Tick "Manually set the due date and/or meter for the next reminder". Nhắc H (3 tháng, ngưỡng 2 tuần), đổi ngày liên tục để đo biên; nhắc D (3 tháng, 5.000 km) đặt 11/30/2026 và 4.000 km.
Kết quả thấy được:
- Ô mở ra "Next Due Date" và "Next Due Primary Meter" ("At"), mặc định = hôm nay + chu kỳ, = đồng hồ hiện tại + chu kỳ (7.999), khác với bội số từ 0 khi KHÔNG tick. Đây là cách đúng để nhắc mới không bị quá hạn ngay.
- Preview sau khi lưu: kỳ sau tính từ ngày đặt tay (Nov 17 → Feb 17 → May 16).
- Biên thời gian, hôm nay 03/11 giờ máy, ngưỡng 2 tuần: 18/11 → Upcoming; 17/11 → Due Soon (cả hai đều ghi "2 weeks from now"); 03/11 → Overdue "1 hour ago". Ngày đến hạn lấy mốc 00:00 giờ máy: đến hạn hôm nay đã Overdue ngay từ đầu ngày.
- Sau khi hoàn thành một lần, "Manually Set Next Due" tự về "No".
Dữ liệu TEST đã tạo: nhắc #17071903 (H), #17071906 (D).

## Đóng nhắc bằng lệnh sửa chữa — Chạy
Các bước đã làm: Nhắc D Upcoming, Resolve, "Add to Work Order". Hộp liệt kê mọi nhắc của xe để tick thêm ("1 Service Reminder will be added", "Show 1 more"), chọn "Add to New Work Order" hoặc "Add to Existing Work Order". Lưu lệnh #101 Open. Đặt Completed.
Kết quả thấy được:
- Khi lệnh Open: nhắc vẫn "Upcoming"; Work Order "Work Order #101, Added 1 minute, 16 seconds ago"; dải "This Service Task was added to Work Order #101 3 minutes ago". Lệnh không đổi trạng thái nhắc.
- Completed bị chặn lần lượt: "Please edit and fix the following errors: Started At can't be blank"; rồi "Starting Meter Entry can't be blank (per your account settings)", "Odometer can't be blank (per your account settings)". Sinh ra từ Cài đặt tài khoản.
- Lệch múi giờ: Start Odometer 3.100 bị chặn "must be less than 2,499 or marked as void" dù đồng hồ hiện 2.999. Ngày lệnh 03/11 01:09 giờ máy là 02/11 giờ tài khoản, nên bị xếp trước các dòng đồng hồ ghi 03/11. Phải nhập 2.400.
- Completed xong: Sinh Service Entry #57857350, nút Edit của lệnh khoá. Nhắc: Next Due 02/02/2027 và 7.400 km; Last Completed 11/03/2026 2.400 km; hết dải Work Order.
- **Chu kỳ tính từ lần HOÀN THÀNH, không từ ngày dự kiến**: dự kiến 30/11 + 4.000 km, làm 03/11 + 2.400 km → kỳ sau = 03/11 + 3 tháng, 2.400 + 5.000 = 7.400. Làm sớm là mất phần còn lại của chu kỳ. Đồng thời ghi số đồng hồ của lần làm, kể cả thấp hơn đồng hồ hiện tại.
- Tuân thủ: Due "Nov 30, 2026 / 4,000 km", Completed "11/03/2026 / 2,400 km", "On-Time", "3 weeks, 6 days ahead · 1,600 kilometers ahead". Thẻ: Completed 1, Late 0, On-Time Compliance 100%.
Bất ngờ: "Draft Work Order" trong Resolve xám, có icon khoá, bấm không có gì xảy ra (trên D Upcoming; có vẻ là tính năng AI Service Advisor khóa gói, chưa kiểm chứng). Tuỳ chọn thay thế "Add to Work Order" dùng được.
Dữ liệu TEST đã tạo: Lệnh #101 Completed, Service Entry #57857350, đồng hồ 2.400.

## Đóng nhắc bằng phiếu dịch vụ, trễ — Chạy
Các bước đã làm: Nhắc E (1 tháng, 1.000 km, Overdue ngay). Resolve, "Add to service history". Hộp "Log completed service": "Manually add to service entry" / "Smart uploads - Import one or more invoices for Fleetio to scan." (mặc định chọn Smart uploads). Chọn tay, hộp "Add to Service Entry", New hoặc Existing. Form có khối Smart Upload (Beta), Odometer, Completion Date bắt buộc.
Kết quả thấy được:
- Ngày phiếu 01/11, đồng hồ 1.500: "must be less than 900 or marked as void".
- Completion Date hiện placeholder ngày hôm nay nhưng chưa nhập: lỗi "can't be blank".
- 03/11, 2.450 km: Service Entry #57857463. E: Next Due 12/02/2026, 3.450 km (2.450 + 1.000), Status "Due Soon" còn 451 km. Compliance "Late", "4 weeks, 1 day ahead · 1,450 kilometers behind", Due ghi "Dec 2, 2026 / 1,000 km". Late 1, On-Time 0%.
- Tính trễ trên trục nào trễ: ngày sớm nhưng km vượt vẫn Late.

## Hoàn thành sớm, ghi lùi ngày — Chạy
Các bước đã làm: Nhắc F (6 tháng, 9.000 km, Upcoming). New Service Entry không đi từ nhắc: gõ task F ở Line Items. Ngày 01/11, 800 km.
Kết quả thấy được: Dòng hiện ngay "Last Completed: Never", "Next Due: 6 months from now · 6,001 kilometers remaining" trên form. Lưu #57857573: F tự nhận là đã làm, không cần tick nhắc. Next Due 04/30/2027, 9.800 km (800 + 9.000), On-Time.
Bất ngờ: Line Items có nút "View Service Reminders" kèm số đỏ (7).

## Service Program: tạo, thêm đầu việc, gắn xe — Chạy
Các bước đã làm: New Service Program TEST-NHAC-BO-LICH (id 590923). Form: Name, Template, Photo, Primary Meter (Miles, Kilometers, Hours), Secondary Meter ("Turn on to utilize an additional meter on the service program. This is useful for tracking service for vehicle engine hours or attached vehicle equipment (concrete mixer, welder, trailer, etc.)"). Add Service Schedule: Service Tasks chọn NHIỀU task một dòng, Time Interval, Time Due Soon Threshold, Primary Meter Interval, Threshold, "Set First Service" (Time Due "At" N tháng, Primary Meter Due "At" N km). Add Vehicles: By Vehicle Attribute, All Vehicles, Specific Vehicles.
Kết quả thấy được:
- Ngưỡng tự điền 2 tuần, 500 km khi nhập chu kỳ. Dòng lịch hiện "1st service at 5 month(s) or 4,500 kilometers, then every 6 month(s) or 4,000 kilometers". Đầu chương trình ghi "Schedule Behavior: Standard".
- Điều kiện khoá sẵn "Primary Meter is equal to Kilometers": bộ lịch chỉ gắn xe cùng đơn vị đồng hồ. Ô chọn xe KHÔNG có xe Sample (đơn vị mi), chỉ có xe km.
- Trước khi lưu có bảng đối chiếu: "1 Vehicle will receive 2 Service Reminders based on the intervals below. Any conflicting individual Service Reminders will be replaced by the schedule from the Service Program." Cột Service Task, Conflicting ("1 Service Reminder" với task B đã có nhắc tay), Duplicate, New Interval.
- "Create a Service Program Rule" / "Save as a Service Program Rule": "Fleetio will keep all of your vehicles in sync with this Service Program based on the vehicle attributes you've selected above." (chỉ tick được với tiêu chí thuộc tính; mờ khi Specific Vehicles).
- Lưu: "Service Program Vehicles was successfully created", xử lý ngầm "Processing: Syncing Vehicles to Service Programs" rồi "Complete: Syncing Vehicles to Service Programs". Mất khoảng 1 phút; trong lúc đó nhắc B cũ chưa đổi.
Dữ liệu TEST đã tạo: chương trình #590923, TEST-XE-01 được gắn vào.

## Gia hạn xe — Chạy
Các bước đã làm: New Vehicle Renewal Reminder, TEST-XE-01, Registration, Due Date mặc định hôm nay, Threshold mặc định 3 tuần. Sửa ngày về 01/10/2026, rồi 01/11/2027. Tạo lại cùng loại.
Kết quả thấy được:
- Loại có sẵn: Emission Test, Inspection, Insurance, Registration. Chọn xe xong Watchers tự điền Bảo Tín. Lưu xong về danh sách (khác Service Reminder về chi tiết).
- Due hôm nay: "Due Soon", "19 hours from now" (khác Service Reminder: đến hạn hôm nay đã Overdue).
- Sửa ngày 01/10: "Overdue", "1 month ago". Không có hành động nào khác: chi tiết chỉ có Details, Comments, "...", Edit. KHÔNG có Resolve, KHÔNG có History, không tải giấy tờ mới: gia hạn = sửa tay Due Date, không giữ lịch sử.
- Edit khoá Vehicle và Renewal Type.
- Trùng: trong danh sách loại, dòng xám "Registration - the selected vehicle already has a reminder of this type". Mỗi xe một nhắc cho mỗi loại.
- Tab Due Soon, Overdue ở danh sách; bộ lọc Vehicle, Type, Due Date, Watcher. Tạo xong hiện đúng dòng có thẻ tuần tự.
Dữ liệu TEST đã tạo: Vehicle Renewal #3531389 (TEST-XE-01, Registration, hiện 01/11/2027).

## Liên hệ TEST — Chạy
New Contact TEST-NHAC-LX, không email, tick Operator, User Access để "No Access" (mặc định): không mời ai, không gửi gì. Contact Renewal loại có sẵn: Certification, License Renewal.

## Service Program: đồng bộ, nhắc tay bị thay, sửa lịch, gỡ xe — Một phần (gỡ xe dừng ở hộp xác nhận)
- Nhắc tay trùng task: nhắc B giữ NGUYÊN mã #17071895, đổi sang lịch bộ: Service Program "TEST-NHAC-BO-LICH", Time Interval từ trống thành "Every 6 months", Meter Interval từ 3.000 thành 4.000, mốc theo "Set First Service" (4.500, "1,501 kilometers remaining"), Status từ Due Soon về Upcoming. KHÔNG hỏi riêng từng nhắc, chỉ có câu cảnh báo chung ở bước Add Vehicles.
- Task A chưa có nhắc: tự sinh nhắc mới, Upcoming.
- Sửa lịch trên bộ (đổi 4.000 → 3.000, lần đầu 4.500 → 3.200): "Service Schedule was successfully updated", "Processing: Updating vehicle reminders in the background", xong "Complete". Nhắc B theo: "Every 3,000 kilometers", "201 kilometers remaining", Status từ Upcoming sang Due Soon. Sửa bộ đổi trạng thái nhắc đang chạy, không hỏi.
- Gỡ xe: row menu chỉ có "Delete". Hộp "Confirm Service Program Vehicle Deletion": "Are you sure you want to remove the selected vehicle from this service program? This will remove all service reminders on the vehicle from this service program." Nút đỏ "Delete Service Program Vehicle". TÔI KHÔNG BẤM (quy tắc không xoá vĩnh viễn; hộp đã nêu rõ hệ quả xoá nhắc). Hoàn tác không có. Hệ quả thực tế chưa kiểm chứng.
- Row menu của dòng lịch: Edit, Delete. Form Edit có đủ ô như New.

## Biểu mẫu: dựng đủ loại mục — Chạy
Các bước đã làm: New Inspection Form TEST-NHAC-PHIEU (#679228): Smart Upload (Beta) chỉ xem ("Have a paper inspection form? Upload a PDF or photo..."), Title, Description, Copy from Template, Color, "Enable Location Exception Tracking" (bật sẵn), "Prevent Use of Stored Photos" (bật sẵn, "Users will only be able to attach photos by taking them with the device's built-in camera"). Lưu chuyển sang Add items. Thêm 11 loại.
Kết quả thấy được, cấu hình từng loại (mọi loại có Label, Required mặc định bật, Short Description):
| Loại | Ô riêng | Ghi chú |
|---|---|---|
| Section | Label | Không có bắt buộc, gom mục |
| Pass / Fail | Instructions có định dạng, Pass Label, Fail Label, "Enable N/A option", N/A Label, Require photo or comment cho "Pass" và "Fail" | Nhãn đổi được |
| Number | Instructions, Passing Range Minimum/Maximum ("No Minimum", "No Maximum"), Require photo or comment cho Pass, Fail | Ngoài khoảng là Fail |
| Free Text | Instructions | Không có đạt/lỗi |
| Dropdown | Instructions, Choices, "Fail item if chosen" từng lựa chọn, "Add Choice", Require photo or comment | Lựa chọn gắn lỗi |
| Date / Time | Instructions, "Date Only" / "Date and Time" (mặc định) | |
| Meter Entry | "Require Secondary Meter", "Require Photo Verification" (hai ô bật sẵn) | CHỈ một mục trên biểu mẫu: panel khoá sau khi thêm (icon khoá, xám) |
| Photo | Instructions | |
| Signature | | |
| Inventory Adjustment | Instructions; "During an inspection, users can select parts and quantity that were used. After submission, an automatic adjustment is made to update your inventory." | Label mặc định |
| Tire Readings | Instructions; "During an inspection, the correct number of form fields for tread depth and tire pressure will be automatically generated based on the vehicle's axle configuration and number of tires."; Tread Depth, Pressure (min/max mỗi loại), Require photo or comment | Label mặc định "Tire Readings" |
Bất ngờ: Biểu mẫu mới có 8 mục lưu xong, tab Workflows 1 sẵn: "If an item fails — ANY Failed Inspection Item → Create an issue — Create issues automatically". Có thể thêm mục qua bấm panel: ô label tự focus.
Màn Add Workflow: Bước 1 "When do you want to trigger this workflow?": If an item passes, If an item fails, If form is submitted. Sau đó "Which inspection item(s)?": "ANY Failed Inspection Item" hoặc từng mục (chỉ mục đánh giá được: Pass/Fail, Number, Dropdown). Bước 2 action: Change vehicle status, Send an email, Create an issue (có nhãn "Not Available" vì đã có workflow ANY tạo sự cố), Assign user to vehicle, Unassign user from vehicle. Description, "Enable Workflow". KHÔNG có action tạo lệnh sửa chữa: tự tạo lệnh trong Workflow là không có. Dừng, không lưu workflow email.
Dữ liệu TEST đã tạo: biểu mẫu #679228 TEST-NHAC-PHIEU, 8 mục.

## Vehicles & Schedules: gán xe, lịch — Một phần
Các bước đã làm: Add Vehicles trên biểu mẫu: All Vehicles / By Vehicle Attribute / Specific Vehicle (manual override). Tick Set Schedule: Frequency mặc định Daily, Every 1 Day; Advanced: Set Delayed Start, Enable Reminder Notification ("Send a reminder notification to the currently assigned vehicle operator ahead of the inspection's due date. Notifications are sent in the Account timezone."). Chỉ thấy tần suất theo thời gian (Daily đến Yearly), KHÔNG có lịch theo số đồng hồ trong form.
Kết quả thấy được: "If unchecked, the form will still be available to these Vehicles on an "as needed" basis." Lưu: "Adding Rule in the background. You'll be notified when it's complete." Mất hơn 1 phút (toast không tự báo trong tab đang mở): trong lúc đó tab Vehicles & Schedules rỗng và ô chọn xe của phiếu báo "No options" / "No results for 'TEST-XE-01'". Sau đó: Vehicle TEST-XE-01, Add Via "Manual", Form Status "Enabled", Schedule "Daily with no reminder currently set", Frequency Daily.
Bất ngờ: biểu mẫu chưa gán xe thì không làm phiếu được (không báo lý do, chỉ danh sách rỗng).
Chưa làm: Skipped, Overdue, Due Soon của lịch cần chờ qua ngày: kiểm lại sau 1 ngày trên TEST-XE-01, xem "Việc chưa làm" cuối file.

## Làm phiếu: thiếu dữ liệu từng lỗi — Chạy
Các bước đã làm: New Vehicle Inspection TEST-NHAC-PHIEU, TEST-XE-01. Lưu trống. Điền từng phần lưu lại.
Kết quả thấy được:
- Lưu trống: toast "Could not submit inspection form. Please fix any errors and try again." (E-006). Từng mục "is required" (E-003) ở cả nhãn và ô; mục đồng hồ "requires a Odometer"; Chữ ký "is required".
- Phanh Fail, Áp suất 25 (khoảng 10 đến 20): "must contain a remark on failure" (E-001) cả hai. 25 hiện chữ đỏ "X 25".
- Đồng hồ 3.050: "must be between 800 and 2,499 or marked as void", vì lệch múi giờ (cùng hiện tượng WO): giờ phiếu tính theo Chicago là 02/11.
- Chữ ký: nhập text "Type your name", vẽ thành nét chữ, không có ô "This must be checked" (E-005 chỉ thấy ở mẫu có ô xác nhận, không có trong kiểu Signature mặc định).
- Dropdown: khi chọn TEST Hong (Fail if chosen) cũng tính lỗi. Date mặc định hiện gợi ý ngày, giờ nhưng chưa nhập thì lỗi "is required".
- Add Remark: "Add Comment", "Add Photo". Lớp ghi chú chỉ lưu khi gõ vào ô Comment.
- Không có nút lưu nháp: chỉ Save Inspection, Cancel. Rời trang: hộp "Leave site?", phiếu mất. Không có bản nháp ở Inspection History.
- Đạt: Submission #126056430, toast "Inspection form submitted.". Đầu phiếu: Vehicle, Inspection Form, Work Order, Started, Submitted, Duration 2m 17s, Submission Source "Fleetio Web App", Submitted By, Job. Bản đồ vị trí, Print.
- BẤT NGỜ: trường Job tự gắn "TEST-02 TEST-Job-02-Tu-dong" do xe đang có Job chạy (phiếu #126056570 lúc khác là "Unassigned"): phiếu ăn theo chuyến đang chạy của xe.
- BẤT NGỜ: mục Date/Time nhập 1:40am, phiếu hiện "11/03/2026 2:40pm". Lệch 13 giờ, không báo. Vấn đề khi thiết bị khác múi giờ tài khoản.
- Vị trí lần này ghi được: bản đồ hiện vị trí máy thật (Việt Nam). E-007 không hiện ở lần này do trình duyệt đã có quyền vị trí; lần 1 đã ghi. Ảnh không lưu lại vì có vị trí thật.
Dữ liệu TEST đã tạo: Submission #126056430 (sự cố #47, #48, #49), đồng hồ 2.470.

## Mục lỗi: lỗi lại khi sự cố còn mở, Failure Timeline — Chạy
Các bước đã làm: "TEST - Quick check", Brakes Fail lần 2, khi Issue #31 còn mở và đã ở WO #100.
Kết quả thấy được: KHÔNG tạo sự cố mới. Submission #126056570, cột trạng thái trên phiếu hiện "WO #100". Danh sách Item Failures có thêm dòng riêng, cũng "WO #100". Failure Timeline của dòng này gộp cùng dòng thời gian sự cố cũ: "Bảo Tín submitted an inspection with a failed item, Inspection Submission #126056570, Brakes Fail" (Now); "Bảo Tín added this issue to a work order, Work Order 100"; "Workflow opened this issue"; "submitted an inspection with a failed item #125988723".
Trả lời: OQ-8 của nhóm reminders-inspection: GỘP vào sự cố đang mở, thêm một mốc vào dòng thời gian, mỗi lần lỗi vẫn là một dòng Item Failures. Không báo gì cho người kiểm khi đang làm phiếu.
Tab Item Failures: All, Needs Action, Open Issue, Acknowledged, Resolved. Cột: Submitted At, Submission, Vehicle, Item, Inspection Form, Failure Timeline, Status.
Dữ liệu TEST đã tạo: Submission #126056570 (dùng biểu mẫu tải chung TEST - Quick check).

## Gia hạn liên hệ — Chạy
New Contact Renewal Reminder: TEST-NHAC-LX, License Renewal, Due mặc định hôm nay. Ngưỡng mặc định 4 (tuần), khác xe là 3. Watchers tự điền Bảo Tín (người dùng tài khoản). Lưu về danh sách: "Due Soon", 11/03/2026, "18 hours from now", 1 watcher. Cùng mô hình gia hạn xe, không có Resolve (chưa mở chi tiết để xác nhận lần nữa).
Dữ liệu TEST đã tạo: liên hệ TEST-NHAC-LX, Contact Renewal License Renewal.

## Mục lỗi: Needs Action, Acknowledged, Resolved; lỗi lại sau khi đã sửa — Chạy
Các bước đã làm: Workflow "..." có Edit, Disable, Delete. Disable: "Are you sure you want to disable this workflow? This will prevent any actions from running." → nhãn "Disabled", "Inspection Workflow was successfully updated". Nộp phiếu có Dropdown TEST Hong.
Kết quả thấy được:
- Không workflow: Status đỏ "Needs Action" (đây là cách duy nhất ra trạng thái này), trên phiếu hiện hai nút "Acknowledge", "Create Issue". Ảnh images/item-failure-needs-action.jpg.
- Row menu Needs Action: Acknowledge, Create Issue, View Failure Timeline.
- Acknowledge: hộp "Acknowledge Failure", Comments KHÔNG bắt buộc (lưu rỗng được). "Successfully acknowledged failed inspection item." Status "Acknowledged", row menu chỉ còn "View Failure Timeline": là trạng thái cuối, KHÔNG có nút quay lại, không tạo sự cố được nữa. Bỏ qua lỗi không cần lý do.
- Resolved: Sự cố từ phiếu: Resolve menu "Add to Service Entry, Draft Work Order, Add to Work Order, Get Service at Shop, Resolve with Note". Resolve with Note: Note bắt buộc ("Describe what work was performed to resolve the issue."). Status "Resolved", nút đổi thành "Reopen". Trên phiếu cũ cột trạng thái thành "Resolved in Issue #49"; tab Resolved của Item Failures có dòng.
- Lỗi lại sau khi đã Resolved: Dropdown TEST Hong lần sau → Issue MỚI #50, KHÔNG mở lại #49.
- KHÔNG có câu hỏi xác nhận: làm lại phiếu trên web sau khi đã Resolved không thấy prompt nào, chỉ các ô như thường. Tài liệu hãng ghi có xác nhận lại; trên web tôi không thấy (có thể chỉ trên Fleetio Go, chưa kiểm được). Không thử được "từ chối xác nhận".
- Đạt lại khi sự cố còn mở: Phanh từng Fail #47 nay Pass: phiếu hiện "✓ Pass" kèm link "Issue #47", sự cố vẫn Open, không tự đóng; Tương tự Áp suất #48. Mục đạt sau không ảnh hưởng.
- Sự cố tự sinh: tiêu đề "[Inspection Item] TEST-NHAC Phanh [Answer] Fail [Remark] TEST-NHAC phanh mon", mô tả "Generated by the failed inspection item ... submitted by Bảo Tín on Nov 2, 2026 at 12:35 PM CST", Source "Inspection Submission #126056430", Timeline "Issue Opened by workflow". Priority: Pass/Fail "High" (Auto-assigned priority: High, Major functionality impaired), Dropdown "No Priority". Khác nhau theo loại mục.
Dữ liệu TEST đã tạo: Submission #126056886 (Issue #50), #126057076 (Needs Action rồi Acknowledged). Workflow mặc định của TEST-NHAC-PHIEU đang Disabled.

## Phiên bản biểu mẫu — Chạy
Các bước đã làm: Sửa nhãn "TEST-NHAC Phanh" thành "TEST-NHAC Phanh MOI" sau khi đã có phiếu.
Kết quả thấy được: Phiếu cũ #126056430 vẫn giữ "TEST-NHAC Phanh", đầu phiếu có nhãn cam "Past Version" cạnh tên biểu mẫu. Biểu mẫu mới mang nhãn mới. Phiếu đã nộp: menu "..." chỉ có "Delete", KHÔNG có sửa; có Print.
Bất ngờ: Lưu biểu mẫu kể cả khi không đổi gì cũng ghi "Inspection Form was successfully updated" (có sinh phiên bản hay không: chưa kiểm).

## Hoãn: huỷ hoãn; Tuân thủ; Forecasting — Chạy / Một phần
- Remove Snooze: nhắc G đang Snoozed đến 11/10, bấm "Remove Snooze" → không hỏi, "The Service Reminder was successfully updated.", về "Due Soon".
- Tuân thủ: mỗi nhắc 1 lần hoàn thành: D 100%, F 100%, Brake 100%, E 0%, G 0%. Danh sách lọc TEST-XE-01 "Average Compliance 60% on-time" = trung bình đều, khớp số liệu nhỏ này (chưa kiểm khi một nhắc có nhiều lần). "Recalculate Compliance" trong menu "..." chỉ bật khi đã có lịch sử (xám ở nhắc chưa làm). Chạy ngầm "Processing: Calculating Service Reminders Compliance in the background" sau mọi thay đổi.
- KPI đầu danh sách đếm XE, không đếm nhắc: 2 nhắc Overdue trên 1 xe → "Overdue Vehicles 1". Ảnh images/reminder-list-compliance.jpg. Tab Due Soon, Overdue, Snoozed có số. Cột: Vehicle, Service Task, Status, Next Due, Incomplete Work Order, Last Completed, Compliance, Watchers, Assignee, Assigned At, và nút Resolve mở ngay trên dòng.
- Forecasting: thấy nút "Enable Forecasting" trên danh sách, và "Improve compliance with Forecasting" + Learn More ở trang chi tiết. KHÔNG bấm vì là bật cấp tài khoản (brief cấm đổi Cài đặt). Kết quả dự báo: Docs, không thấy. Form Vehicle có mô tả "Average Usage per Day is used to forecast Service Reminders..." và ô "Automatically calculate".
- Smart Upload: chỉ xem ở New Inspection Form và New Service Entry (Beta), chưa tải gì.

---

# Bảng tổng hợp theo yêu cầu độ sâu

## 1. Ma trận trạng thái: Nhắc bảo dưỡng (Service Reminder)
| Trạng thái | Hành động làm được | Sang trạng thái | Điều kiện, người làm | Hiệu ứng lên đối tượng khác | Câu chữ nguyên văn | Mức |
|---|---|---|---|---|---|---|
| (tạo mới) | Lưu form | Upcoming / Due Soon / Overdue | Theo mốc so với hiện tại. Chưa có lịch sử: mốc km bội số từ 0 | Thêm dòng danh sách; KPI theo xe | "Service Reminder was successfully created" | Chạy |
| Upcoming | Đồng hồ tăng | Due Soon | Còn ≤ ngưỡng | | "500 kilometers remaining" | Chạy |
| Upcoming | Đồng hồ vượt mốc nhảy cóc | Overdue | ≥ mốc | | | Chạy (lần 1), cùng công thức |
| Due Soon | Đồng hồ ≥ mốc | Overdue | Đúng bằng mốc cũng Overdue | | "0 kilometers remaining" | Chạy |
| Overdue | Void đồng hồ, lùi | Due Soon | Theo số hiện tại | | "Successfully voided Meter Entry" | Chạy (Due Soon về Upcoming bằng Void chưa bấm) |
| Bất kỳ | Edit chu kỳ | Tính lại ngay | Không hỏi, không ghi lịch sử | | | Chạy |
| Bất kỳ | Manually set | Tính theo ngày, số đặt | Tự tắt sau hoàn thành | Kỳ sau tính từ mốc đặt | "Manually Set Next Due: Yes" | Chạy |
| Overdue, Due Soon, Upcoming | Snooze | Snoozed | Ngày tương lai; ngày đã qua lưu được nhưng vô hiệu | Next Due xám | "Snoozed until 11/03/2026" | Chạy trên Overdue; Upcoming chưa bấm thử |
| Snoozed | Hết hạn | Trạng thái thường | Dưới 2 phút sau mốc | | | Chạy |
| Snoozed | Remove Snooze | Trạng thái thường | Không hỏi | | "Remove Snooze" | Chạy |
| Snoozed | Hoàn thành | Tính kỳ mới, xoá hoãn | Tự động | Late nếu quá | | Chạy |
| Bất kỳ | Add to Work Order | Không đổi trạng thái | Lệnh Open: gắn dải | "Work Order #101" | "This Service Task was added to Work Order #101" | Chạy |
| Bất kỳ | Lệnh Completed | Kỳ mới từ lần làm | Bắt Started At, Odometer | Sinh Service Entry | "On-Time" / "Late" | Chạy |
| Bất kỳ | Add to service history / Service Entry | Kỳ mới từ lần làm | Task khớp là nhận | Compliance | | Chạy |
| Bất kỳ | Gắn Service Program | Lịch bộ, giữ mã nhắc | Task trùng | Đổi trạng thái | "Any conflicting individual Service Reminders will be replaced..." | Chạy |
| Bất kỳ | Delete | | Không bấm | | | Không làm |
| Bất kỳ | Find a shop / Send Notifications | | Không bấm (không gửi ra ngoài) | | | Xem |

## 2. Ma trận trạng thái: Lịch kiểm (Schedule)
| Trạng thái | Hành động | Sang | Điều kiện | Hiệu ứng | Câu chữ | Mức |
|---|---|---|---|---|---|---|
| Enabled, chưa đến hạn | Set Schedule Daily | | Gán xe qua Rule hoặc Manual | "Daily with no reminder currently set" | Add Via "Manual", Form Status "Enabled" | Chạy |
| Due Soon, Overdue, Skipped | | | Cần qua ngày thật | | | Không chạy được trong phiên (chờ 1 ngày) |

## 3. Ma trận trạng thái: Mục lỗi (Item Failure)
| Trạng thái | Hành động làm được | Sang | Điều kiện | Hiệu ứng | Câu chữ | Mức |
|---|---|---|---|---|---|---|
| Needs Action | Acknowledge | Acknowledged | Comment tuỳ chọn | Hết hàng việc | "Successfully acknowledged failed inspection item." | Chạy |
| Needs Action | Create Issue | Open Issue | | Sinh sự cố | "Create Issue" | Xem, chưa bấm |
| (workflow bật) | Fail | Issue #n | Tự động | Sinh sự cố "[Inspection Item] ..." | "Issue Opened by workflow" | Chạy |
| Open Issue | Lỗi lại | Giữ sự cố | Gộp timeline | Thêm dòng Item Failures | "submitted an inspection with a failed item" | Chạy |
| Open Issue | Đạt lại | Giữ sự cố | Không tự đóng | | "✓ Pass", "Issue #47" | Chạy |
| Open Issue | Resolve with Note | Resolved | Note bắt buộc | "Resolved in Issue #49" | | Chạy |
| Open Issue | Add to Work Order | WO #n | | Status "WO #100" | | Chạy lần 1, thấy ở #31 |
| Resolved | Lỗi lại | Sự cố MỚI | Không mở lại | Issue #50 | | Chạy |
| Resolved | Reopen ở sự cố | | Chưa bấm | | "Reopen" | Xem |
| Acknowledged | Chỉ xem | Cuối | Không có đường quay lại | | "View Failure Timeline" | Chạy |

## 4. Bảng case
| Case | Điều kiện | Kết quả thật | Ảnh |
|---|---|---|---|
| Đường chính nhắc | 3 tháng, 3.000 km | Trạng thái đúng theo trục xấu nhất | reminder-list-compliance.jpg |
| Xe mới gắn nhắc chưa có lịch sử | Đồng hồ 2.300, chu kỳ 1.000 | Overdue ngay "1,300 kilometers overdue" | |
| Thiếu chu kỳ | Bỏ trống cả hai | "Please provide a usage or a time interval" | |
| Ngưỡng = chu kỳ | 1.000 / 1.000 | "too high (can't be equal to or greater than...)" | |
| Biên km | 501, 500, 1, 0, -1 | Upcoming, Due Soon, Due Soon, Overdue, Overdue | |
| Biên ngày | 15, 14, 0 ngày | Upcoming, Due Soon, Overdue | |
| Snooze ngày quá khứ | 01/11 | Không chặn, vô hiệu, vẫn báo thành công | |
| Đổi chu kỳ khi quá hạn | 1.000 → 5.000 | Overdue → Upcoming, không dấu vết | |
| Làm sớm 4 tuần | Dự kiến 30/11, làm 03/11 | Kỳ sau tính từ 03/11, mất phần còn lại | reminder-after-work-order.jpg |
| Làm trễ km | Mốc 1.000, làm 2.450 | Late, kỳ sau 3.450, Due Soon ngay | |
| Ghi lùi | Ngày 01/11, 800 km | Mốc 9.800, 30/04/2027 | |
| Đồng hồ ngược ngày | 1.500 ngày 01/11 | "must be less than 900 or marked as void" | |
| Lệch múi giờ | Lệnh 01:09 sáng VN | Bị xếp 02/11 Chicago, chặn 3.100 | |
| Trùng gia hạn | Cùng xe, cùng loại | Dòng xám trong danh sách | |
| Gán bộ lịch trùng nhắc tay | B đã có | Giữ mã, thay chu kỳ | |
| Sửa bộ lịch | 4.000 → 3.000 | Nhắc đổi trạng thái sau xử lý ngầm | |
| Phiếu rỗng | Không điền | E-003, E-006, "requires a Odometer" | |
| Fail không ghi chú | Có luật | E-001 | |
| Số ngoài khoảng | 25, khoảng 10 đến 20 | Fail tự động, sinh sự cố, cần ghi chú | |
| Dropdown Fail | TEST Hong | Sinh sự cố, không cần ghi chú | |
| Lỗi lại khi mở | Brakes | Gộp | |
| Lỗi lại sau Resolved | Dropdown | Sự cố mới | |
| Không workflow | Disable | Needs Action | item-failure-needs-action.jpg |
| Biểu mẫu chưa gán xe | Làm phiếu | Danh sách xe rỗng, không báo | |
| Sửa biểu mẫu có phiếu | Đổi nhãn | "Past Version", phiếu cũ giữ nhãn cũ | |

## 5. Luồng nghiệp vụ
**Nhắc:** Admin dựng Service Task → gắn nhắc lẻ hoặc Service Program cho xe (cùng đơn vị đồng hồ) → hệ thống tính trạng thái mỗi khi đồng hồ, thời gian đổi → Quản lý thấy Due Soon/Overdue ở danh sách + KPI xe. Rẽ: Hoãn (Snooze) rồi về; hoặc Resolve: Add to Work Order (lệnh Open không đổi trạng thái, Completed mới tính) / Add to service history (tính ngay) → kỳ mới từ lần làm, Compliance ghi On-Time/Late. Kết thúc: vòng lặp; không có trạng thái Đóng.
**Gia hạn:** Admin tạo nhắc theo loại → Due Soon → Overdue → người phụ trách sửa tay Due Date sang kỳ mới. Không lịch sử.
**Kiểm tra:** Admin dựng biểu mẫu → gán xe (Rule/Manual, có lịch hoặc as needed; xử lý ngầm) → Lái xe chọn biểu mẫu, xe, làm phiếu một lần xong (không nháp) → đạt: hết; lỗi: workflow bật → Sự cố (gộp nếu đang mở) → Lệnh hoặc Resolve with Note → Resolved; workflow tắt → Needs Action → Acknowledge (hết) hoặc Create Issue.

## 6. Giải pháp đáng học, điểm yếu
**Đáng học**
- Trạng thái tính tại lúc đọc, theo trục xấu nhất, đổi ngay khi lưu đồng hồ: rẻ và không cần job, hợp với số km GPS về liên tục.
- Bảng đối chiếu khi gán bộ lịch (Conflicting, Duplicate, New Interval): cho đầu kéo cùng dòng xe, thấy trước hệ quả rồi mới áp.
- Resolve mở hộp liệt kê mọi nhắc của xe để gộp vào một lệnh: vào xưởng làm luôn nhiều việc, giảm số lần dừng xe.
- Lỗi lặp gộp vào sự cố đang mở, nhưng vẫn giữ dòng lỗi và dòng thời gian: tránh một lốp hỏng sinh hàng chục sự cố khi nhiều lái kiểm cùng đầu kéo hoặc mooc.
- Phiên bản biểu mẫu "Past Version": phiếu cũ không đổi khi sửa mẫu, cần cho kiểm toán và tranh chấp.
- Đóng dấu Job vào phiếu kiểm tự động: liên kết kiểm trước chuyến với chuyến đang chạy, rất hợp Lệnh vận tải.
**Điểm yếu**
- Nhắc mới chưa có lịch sử tính mốc từ 0: đầu kéo đã chạy 300.000 km vừa khai báo là Overdue ngay, phải dùng Manually set hoặc nhập lịch sử trước. Invlogis nên mặc định tính từ số hiện tại.
- Đổi chu kỳ xoá trắng quá hạn, Acknowledge không cần lý do, Snooze không có lý do: lỗ hổng kiểm soát. Invlogis nên bắt lý do và ghi lịch sử.
- Làm sớm mất phần còn lại của chu kỳ: tốt cho an toàn, nhưng cần cân nhắc với hợp đồng bảo dưỡng theo km.
- Gia hạn không có lịch sử, không có nút gia hạn: giấy tờ đầu kéo, mooc, đăng kiểm cần giữ chứng từ qua từng kỳ.
- Múi giờ: dùng lẫn giờ thiết bị và giờ tài khoản, gây chặn sai số đồng hồ và lệch giờ mục Date/Time 13 giờ. Delta chỉ một múi giờ nhưng SaaS đa khách phải chốt một nguồn giờ.
- Đóng phiếu dữ liệu đồng hồ: bắt buộc Odometer khi xong lệnh là cấu hình tài khoản; mooc không đồng hồ sẽ vướng (chưa kiểm được vì không tạo được xe).
- Workflow không có action "tạo lệnh": muốn tự tạo lệnh phải qua Automations (nhóm khác đang thử).
- Tạo Rule, Service Program chạy ngầm, trong lúc đó không có dấu hiệu rõ ở màn đang mở.

# Trả lời câu hỏi mở (Mục 12 spec reminders-inspection)
- OQ-8: Trả lời được: gộp vào sự cố đang mở, mỗi lần lỗi một dòng Item Failures.
- OQ-7: Một phần: phiếu ghi được vị trí khi trình duyệt cấp quyền, phiếu lần 1 không vị trí vẫn nộp được (E-007). Cờ Location Exception chưa thấy (cần nhiều vị trí khác nhau, web không giả được).
- OQ-6: Chưa thử thay đồng hồ (Meter Replacement), không có trong phạm vi bước này.
- OQ-1 đến OQ-5, OQ-9: câu của khách, không trả lời bằng chạy thử.

# Việc chưa làm và vì sao
- Mooc không đồng hồ, xe giờ máy, đồng hồ phụ, phiếu riêng đầu kéo và mooc: BỊ CHẶN bởi "Your plan is limited to 5 vehicles", không có xe riêng; không sửa dữ liệu xe nhóm khác. Giải pháp: user cho phép lưu trữ xe TEST không dùng, hoặc chia lại xe.
- Lịch kiểm Due Soon, Overdue, Skipped: cần qua ngày thật. Lịch Daily đã gán trên TEST-NHAC-PHIEU: mở lại sau 1 ngày sẽ thấy.
- Theo số đồng hồ của lịch kiểm: form không có (chỉ thấy Daily đến Yearly); chưa mở hết danh sách Frequency để liệt kê đúng.
- E-002 Thiếu ghi chú khi đạt, E-004 thiếu cấu hình trục (TEST-XE-01 đã khai trục), E-005 (không có ô này ở biểu mẫu tự dựng): không làm lại; câu chữ từ lần 1.
- Inventory Adjustment, Tire Readings, Photo trên phiếu: đã xem cấu hình nhưng bản biểu mẫu lưu cuối không chứa ba loại này (tab bị mất lúc nhóm tab reset). Không tải ảnh thật; tồn kho chưa chạy.
- Workflow 3 trigger: đã xem, không lưu workflow email, Change vehicle status không lưu vì TEST-XE-01 dùng chung.
- Gỡ xe khỏi Service Program: dừng ở hộp xác nhận vì quy tắc không xoá vĩnh viễn.
- "Create Issue" ở Needs Action, "Reopen" sự cố: chưa bấm (hết thời lượng hợp lý).
- Forecasting: không bật. Bấm "Draft Work Order": xám, có icon khoá, bấm không có phản hồi (chỉ thử ở nhắc Upcoming).

# Ghi chú vận hành, rủi ro
- Dùng TEST-XE-01 dùng chung: đồng hồ hiện 2.999 (đã thêm 2.499, 2.500, 2.999, void 3.000, 3.001, cùng các số 2.400, 2.450, 2.460, 2.470, 2.480, 2.490, 800 có dòng ghi trước). Xe có thêm 8 nhắc TEST-NHAC (A đến H), 1 gia hạn, 1 biểu mẫu gán (TEST-NHAC-PHIEU), 1 bộ lịch. Biểu mẫu thứ hai TEST-NHAC-NHANH #679262 (1 mục) đã tạo nhưng Rule gán xe không thấy lưu, không dùng. Ba phiếu TEST-NHAC-PHIEU và một phiếu Quick check có lưu vị trí thật của máy chạy (Việt Nam) trên bản đồ. Có thể lẫn với nhóm khác dùng cùng xe.
- Chrome dùng chung: nhóm tab bị reset 3 lần giữa chừng (tab của tôi biến mất), zoom toàn trang thay đổi do agent khác. Một ảnh chụp hiện Issue #34 của nhóm SUA tại tab của tôi trong lúc bấm: đã kiểm lại, WO #101 chưa bị đổi; Issue #34 vẫn nguyên trên ảnh.
