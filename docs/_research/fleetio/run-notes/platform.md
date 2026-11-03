# Ghi chú chạy thử — nhóm Nền tảng (2026-11-03)

Tiền tố dữ liệu: `TEST-NEN`. File đang viết dần trong lượt chạy.

## Hạn mức xe chặn việc tạo `TEST-NEN-01` — Không chạy được (hạn mức gói)
Các bước đã làm: Mở New Vehicle, bấm Save khi trống, rồi gõ `TEST-NEN-01`, bấm Save.
Kết quả thấy được: Trống: "can't be blank" + "Your plan is limited to 5 vehicles" + toast "Vehicle could not be created". Có tên: vẫn "Your plan is limited to 5 vehicles". Danh sách xe hiện "5 of 5", nút Add Vehicle có khoá. Settings › Account Usage: "Vehicles 5 of 5", "Roles 4 of 30", "Automations 0 of 75", "Custom Records 0 of 25", "Documents 0 B of 250.0 GB".
Bất ngờ, lỗi, điểm khác tài liệu hãng: 5 xe đã dùng đều là TEST của các nhóm khác: TEST-KHO-01, TEST-MOOC-LOP, TEST-SUA-01, TEST-XE-01, TEST-XE-LOP. Xe Sample không tính vào hạn mức (tài khoản có 25 xe tính cả Sample, theo số đếm ở Vehicle Statuses). Không chuyển qua Add Multiple Vehicles hay nhập tệp vì đó là lách hạn mức gói.
Dữ liệu TEST đã tạo: không có xe nào.

## Form xe 6 phần, từng trường — Một phần (đọc đủ form; không lưu được vì hết hạn mức)
Các bước đã làm: Mở New Vehicle, bấm từng phần, đọc nhãn và câu giải thích, bấm Save rỗng.
Kết quả thấy được:
| Phần | Trường |
|---|---|
| Details › Identification | Vehicle Name * ("Enter a nickname to distinguish this vehicle in Fleetio."), VIN/SN (nút Decode), License Plate, Type * (mặc định Car), Fuel Type, Year, Make, Model, Trim, Registration State/Province, Labels, Photo |
| Details › Classification | Status * (mặc định Active), Group, Operator, Ownership * (mặc định Owned) |
| Details › Additional Details | Color, Body Type, Body Subtype, MSRP (₫), Linked Vehicles |
| Maintenance | "Choose a Service Program": None ("No Service Reminders will be created") hoặc "Choose an existing Service Program" |
| Lifecycle | In-Service Date, In-Service Odometer, Estimated Service Life in Months, Estimated Service Life in Meter, Estimated Resale Value, Out-of-Service Date, Out-of-Service Odometer |
| Financial | Purchase Vendor, Purchase Date, Purchase Price, Odometer, Notes; Loan/Lease: Loan, Lease, None |
| Specifications | Dimensions (Width, Height, Length, Interior Volume, Passenger Volume, Cargo Volume, Ground Clearance, Bed Length), Weight (Curb Weight, Gross Vehicle Weight Rating), Performance (Towing Capacity, Max Payload), Fuel Economy (EPA City, Highway, Combined), Engine (15 trường), Transmission (4), Wheels & Tires (11), Fuel (Quality, Tank 1, Tank 2), Oil Capacity |
| Settings | Primary Meter * (Miles, Kilometers, Hours), Current Reading, Average Usage per Day (mặc định "Automatically calculate"), Add Secondary Meter; Fuel Unit *, Measurement Units * |
Nút: Cancel, Add Multiple Vehicles, Save & Add Another, Save Vehicle.
Bất ngờ: Odometer trong Financial hiện đơn vị "mi" trong khi Specifications hiện cm, kg, lít (chưa rõ lý do). Out-of-Service chỉ là trường ngày và số km, không thấy nút thanh lý.
Trả lời câu hỏi mở nào: bổ sung Scope nhóm Phương tiện (bán, thanh lý chỉ là trường dữ liệu).

## Tự động hoá: 18 mẫu — Chạy (đọc từng mẫu, không lưu mẫu)
Các bước đã làm: Automations › Browse Templates; Apply từng mẫu để đọc định nghĩa; rời trang không lưu.
Kết quả thấy được: Apply mở `automations/new?template=<slug>`, chưa lưu gì. 17/18 mẫu đọc đủ, mẫu "Send Email When A Work Order Total Exceeds Amount" chỉ thấy tên và số 1 điều kiện, 1 hành động.
| Bản ghi | Tên mẫu | Trigger | Điều kiện | Hành động |
|---|---|---|---|---|
| Fault | Create An Issue When A Critical Fault Is Created | Created | Critical = Yes và Status = Open | Create Issue |
| Fault | Ignore Nuisance Codes | Created | Code = P0456 | Update Fault Status to Ignored |
| Issue | Update Vehicle Status To Active When Issue Status Is Resolved | Updated | Status is Resolved | Update Vehicle Status to Active |
| Issue | Update Vehicle Status To In Shop When Issue Source Is Inspection Failure | Created or Updated | Status Open và Source Inspection Failure | Update Vehicle Status to In Shop |
| Issue | Create A Work Order When An Issue Is Created | Created | không có | Create Work Order, Status Open |
| Issue | Update Issue To Critical When Issue Contains Low Engine Oil Pressure | Created or Updated | Status Open và Description contains | Update Issue Priority to Critical |
| Issue | Update Issue To Critical When Open Issue Source Is Recall | Created | Source is Recall | Update Issue Priority to Critical |
| PO | Automatically Approve New Purchase Orders Less Than Or Equal To Amount | Created | Status Pending Approval và Total ≤ 10.000 ₫ | Update PO Status to Approved |
| PO | Add Comment For Review When a Purchase Order Is Created | Created | Status Pending Approval | Add Comment, có "Prevent duplicate comments" |
| PO | Add Label For New Purchase Orders Created With Brakes Category | Created | Part Category Brakes | Add to Labels list ("Missing Value" vì tài khoản chưa có nhãn) |
| Service Entry | Send Email When A Service Entry Total Exceeds Amount | Created or Updated | Total ≥ 100.000 ₫ | Send Email, nội dung có biến `{{ service_entry.id }}`, `{{ asset.name }}` |
| Service Entry | Set Repair Priority Class to Scheduled for Engine Oil & Replacement | Created or Updated | Service Tasks is any of Engine Oil & Filter Replacement | Đặt Repair Priority Class |
| Work Order | Update Vehicle Status when a Work Order is Created | Created | Status Type = Incomplete | Update Vehicle Status (để trống, phải chọn) |
| Work Order | Update Vehicle Status to Active when Work Orders are Completed | Updated | Status Type Completed và Vehicle Incomplete Work Orders Count < 1 | Update Vehicle Status to Active |
| Work Order | Send Email When A Work Order Total Exceeds Amount | chưa đọc | 1 | 1 |
| Work Order | Set Repair Priority Class to Scheduled for Preventative Maintenance Work Orders | Created or Updated | Line Item Reason for Repair is any of 08 | Update Repair Priority Class to Scheduled |
| Work Order | Automatically Assign Employee To Newly Created Work Orders | Created | Assigned To is blank | Update Assigned To (tự điền người đang đăng nhập) |
| Work Order | Create Follow-Up Work Order After Tire Replacement | Updated | Service Tasks any of Tire Replacement và Status Type Completed | Create Work Order, Status Open, Service Tasks Wheel Lug Nut Torque |
Màn mới: automation-templates — ảnh images/automation-templates.jpg — cột trái theo loại trigger (Faults 2, Issues 5, Purchase Orders 3, Service Entries 2, Work Orders 6), thẻ có sơ đồ trigger → số điều kiện → số hành động, nút Apply khi rê chuột.
Giải pháp đáng học: mẫu "WO xong và xe không còn WO mở thì xe về Active" nối đúng nhánh mà tài liệu hay bỏ sót; mẫu nào cũng là con số của khách có thể sửa trước khi bật. Với đầu kéo có nhiều lệnh sửa song song, điều kiện đếm này rất đáng lấy.

## Tự động hoá: tạo, bật, chạy, tắt, Archive — Chạy
Các bước đã làm: Tạo `TEST-NEN-AUTO-01` (Issue Created, Summary contains TEST-NEN, Add Comment) và `TEST-NEN-AUTO-02` (từ mẫu Low Engine Oil Pressure). Lưu ở trạng thái tắt, tạo Issue, bật, tạo Issue, đọc Run History, Archive, Restore.
Ma trận trạng thái Automation:
| Trạng thái | Hành động làm được | Sang trạng thái | Điều kiện, người làm | Hiệu ứng | Câu chữ nguyên văn | Mức |
|---|---|---|---|---|---|---|
| Chưa lưu | Save Automation | Disabled | Save mờ cho tới khi có trigger, hành động | Không để lại bản rác nếu rời trang | "Automation ... was successfully created" | Chạy |
| Disabled | Gạt công tắc, xác nhận | Enabled | Hộp xác nhận | Sinh version v.1; Enabled At | "When you enable this automation ... actions will run when you set the trigger and conditions are met." | Chạy |
| Enabled | Archive | Archived | Không cần tắt trước | Tắt ngay, ghi Disabled At | "This will disable the automation and it will stop working immediately. It can be restored at any time." | Chạy |
| Archived | Restore | Disabled | Không tự bật lại | Hết chỉ đọc | "Archived records are read-only and cannot be updated." · "Record successfully restored" | Chạy |
| Archived | Delete | — | Không bấm theo ràng buộc | — | nút "Delete" | Không chạy |
| Mọi trạng thái | Make a Copy, View Record History | — | Menu More Actions | — | — | Một phần (đọc nút) |
Bảng case:
| Case | Điều kiện | Kết quả thật | Ảnh |
|---|---|---|---|
| Đang tắt | Issue #40 tạo khi AUTO-01 tắt | Không có comment, không có lượt chạy | — |
| Không chạy bù | Bật AUTO-01 sau khi #40 đã có | #40 vẫn không có comment | — |
| Đang bật, khớp | Issue #42 | Trong vòng 6 giây có comment, tác giả "Fleetio Automation"; Run History 1 SUCCESS | automation-comment-result.jpg |
| Không khớp điều kiện | Issue #41 của nhóm khác tạo trong lúc bật | Total Runs vẫn 1: lượt không khớp không được tính | — |
| Hai automation cùng sự kiện | Issue #43 khớp cả 01 và 02 | Cả hai chạy: có comment và lên Critical | — |
| Không phân biệt hoa thường | Description "low engine oil pressure", điều kiện "Low Engine Oil Pressure" | Vẫn khớp, Priority Critical | — |
| Tự kích hoạt mình | AUTO-02 Created or Updated tự đổi Priority của chính Issue | 2 lượt: Create rồi Update, sau đó dừng vì giá trị không đổi | automation-self-trigger-runs.jpg |
| Người gây ra | Lượt Update do automation gây ra | "Triggered By" vẫn ghi người tạo Issue, không ghi automation | automation-self-trigger-runs.jpg |
| Kết quả chạy | Lượt thêm comment | "Records: No records changed" dù đã thêm comment | automation-run-result.jpg |
Bất ngờ, lỗi, điểm khác tài liệu hãng: Issue mới có Priority mặc định "Auto-assign", #40 và #42 tự thành High dù không nhập mức; đây là AI Issue Prioritization. Tài liệu hãng không nói về chống vòng lặp, giới hạn lượt chạy, hành vi khi hành động lỗi. Hành động theo loại bản ghi Issue: Update Field, Add Comment, Send Email; bản ghi hành động chọn được: Issue, Vehicle, Work Order. Trigger Deleted có thật. Điều kiện: 59 trường cho Issue, chia nhóm Issue, Tool, Vehicle, Vehicle or Tool; All of / Any of; nhóm điều kiện lồng.
Màn mới: automation-detail, automation-run-history, automation-run-result, automation-archived — ảnh cùng tên trong images/.
Dữ liệu TEST đã tạo: automation 96373 `TEST-NEN-AUTO-01`, 96375 `TEST-NEN-AUTO-02` (đã Archive rồi Restore, đang tắt); Issue #40, #42, #43 trên xe dùng chung TEST-XE-01 (không sửa xe).

## Tự động hoá: Create Record, tắt, vòng lặp, thất bại — Một phần
Các bước đã làm: Tạo `TEST-NEN-AUTO-03` từ mẫu Create A Work Order, thêm điều kiện Summary contains TEST-NEN-C. Tạo Issue #44, xem Work Order sinh ra. Tắt 01 và 03.
Kết quả thấy được: Issue #44 "TEST-NEN-C1 tu tao lenh sua" sinh Work Order #105 trạng thái Open trên TEST-XE-01, cột Resolved Issues trỏ #44, tức WO xong sẽ đóng được sự cố. Hành động Create Record chỉ có Status, Assigned To, Service Tasks. Hộp Status chỉ cho Open và Pending, không có Completed. Tắt có hộp "When you disable this automation ... it will stop working and prevent any actions from running."
| Case | Điều kiện | Kết quả thật |
|---|---|---|
| Tạo bản ghi | Issue khớp | WO #105 Open, liên kết Issue |
| Tạo WO đã xong | Chọn Completed trong hành động | Không có lựa chọn này (chặn từ giao diện) |
| Vòng lặp tự thân, giá trị không đổi | AUTO-02 | Dừng sau 2 lượt |
| Vòng lặp chéo hai automation lật giá trị | Không chạy: tài liệu hãng không nêu giới hạn, brief yêu cầu chỉ thử khi có giới hạn rõ | Chưa biết |
| Lượt thất bại | Không tái hiện được; cách thử bằng WO Completed bị giao diện chặn | Failed Runs luôn 0, chỉ thấy có cột Failed Runs và ô "Failure Notification Email" |
Chưa làm: sửa automation đang bật để xem version v.2, Make a Copy, Run Summary Email (không bật vì gửi email), trigger Vehicle và hành động Update Vehicle Status (sẽ sửa xe của nhóm khác).
Màn mới: automation-list-data — images/automation-list-data.jpg — cột Name, Status, Trigger Record, Total Runs, Successful Runs, Failed Runs, Created By, Last Run At, Current Version; tab All, Archived; lọc Created By, Trigger Record, Status, Filters.
Trả lời câu hỏi mở nào: thông tin cho OQ-2 nhóm Nền tảng: mẫu có sẵn đủ dùng với luật đơn giản, nhưng không thấy chống vòng lặp nên công cụ tổng quát có rủi ro.
Giải pháp đáng học, điểm yếu:
- Lưu ở trạng thái tắt, bật phải xác nhận và lúc đó mới sinh phiên bản: khách thử an toàn.
- Mỗi lượt có Run Result ghi phiên bản, bản ghi kích hoạt, log JSON: đội hỗ trợ tra được vì sao chạy.
- Hành động tạo lệnh sửa bị giới hạn trạng thái chưa xong, tránh bỏ qua kiểm tra km khi hoàn tất.
- Điểm yếu: "Triggered By" ghi người thật dù lượt do automation gây ra; "No records changed" khi đã thêm comment; không nêu giới hạn vòng lặp. Invlogis nên ghi rõ nguồn gây ra và đặt trần lượt chạy theo khách.
Dữ liệu TEST đã tạo: automation 96376 `TEST-NEN-AUTO-03` (đang tắt); Issue #44; WO #105 trên TEST-XE-01. 96373 đang tắt.

## Trạng thái xe, Archive xe, Group, Linked Vehicles — Một phần (chỉ đọc; không có xe của nhóm do hạn mức)
Các bước đã làm: Đọc Settings › Vehicle Statuses, Groups & Subgroups, menu More Actions trên TEST-XE-01 (không bấm), đối chiếu nhóm Phương tiện. Không đổi trạng thái xe của nhóm khác, không đổi xe Sample.
Ma trận trạng thái xe:
| Trạng thái | Hành động làm được | Sang trạng thái | Điều kiện, người làm | Hiệu ứng | Câu chữ nguyên văn | Mức |
|---|---|---|---|---|---|---|
| Active (Default), In Shop, Inactive, Out of Service, Sold | Đổi tự do qua trường Status, hoặc automation | Bất kỳ, không thấy luật chuyển | Quyền `vehicles_update_status`, Operator có sẵn | Có lịch sử trạng thái, báo cáo Status Changes, Status Summary | Số xe lúc đọc: Active 22, In Shop 2, Inactive 1, Out of Service 0, Sold 0 | Xem |
| Mọi trạng thái | Archive | Tab Archived của xe | Quyền `vehicles_archive_delete`; Operator không có | Chưa chạy; có Restore hay không chưa kiểm trên xe | Nút "Archive" | Xem |
Menu xe: Edit Vehicle Settings, Manage Inspection Forms, Manage Service Programs, Manage Integration Links, Attach Shared Document, Recalculate Fuel Entries, View Record History, Archive.
Group: cây nhiều cấp, Sample có Alabama, Florida, Georgia, South Carolina, Tennessee. "Require Group" đang khoá vì "all existing assets and contacts must be assigned a group", liệt kê "5 Vehicles", "3 Contacts" còn thiếu. Có Export Data. Thấy nhóm "11/05/2026" do nhóm khác tạo.
Linked Vehicles: trường trong form xe, xem kết quả ở `vehicle.md`.
Bản ghi trùng tên xe: Không chạy được vì hạn mức.
Màn mới: vehicle-more-actions — images/vehicle-more-actions.jpg.

## Liên hệ, người dùng so với liên hệ — Chạy
Các bước đã làm: Tạo `TEST-NEN-LH-01` chỉ có First Name, không email, No Access; tạo lần hai cùng tên.
Kết quả thấy được: Form có Basic Details, Classifications (Operator: "Allow this Contact to be assigned to assets"; Employee; Technician: "Allow this Contact to be selected in labor line items on work orders"), User Access (Enable Access to Fleetio | No Access mặc định: "This Contact will not have access to your Fleetio account and will not receive any notifications."), Contact Information. Trang liên hệ ghi "This Contact doesn't have user access."; khối xe ghi "Contact must have operator classification to be assigned to vehicles".
| Case | Điều kiện | Kết quả thật | Ảnh |
|---|---|---|---|
| Chỉ tên | Không email, không phân loại | Lưu được | contact-no-access.jpg |
| Trùng tên | Tạo lại cùng First Name | Lưu được, không cảnh báo trùng | — |
| Gán xe khi không phải Operator | Xem khối gán xe | Bị chặn bằng câu dẫn | contact-no-access.jpg |
Giải pháp đáng học: một bảng Contact, phân vai bằng tick; Người dùng chỉ là Contact được bật truy cập. Lái xe, thợ, kế toán chung một hồ sơ. Điểm yếu: không chặn trùng người.
Dữ liệu TEST đã tạo: hai liên hệ `TEST-NEN-LH-01` (không email).

## Recall, Motor Pool, Documents — Một phần
Recall: danh sách 261 dòng Sample, tab All, Needs Action, Open, Resolved, Acknowledged, cột Issued At, Status, Issue, Manufacturer Campaign Number, NHTSA Campaign Number. Khung Learn ghi nhập tự động theo năm, hãng, đời từ NHTSA. Chỉ đọc, không đổi trạng thái vì đều là Sample. Ảnh images/recalls-list.jpg.
Motor Pool: `motor_pool_reservations` rỗng, có Add Vehicle Reservation, cột Motor Pool, Number, Operator, Vehicle Types, Vehicle, Pick Up, Drop Off, Status. Muốn đặt xe phải tạo Motor Pool trong Settings; brief cấm đổi Settings và không có xe của nhóm nên KHÔNG chạy. Ảnh images/motor-pool-reservations.jpg.
Documents: rỗng, tab All Documents và tab tên tài khoản, cột File Name, File Size, Location, Auto-Delete, Attached To, Labels, lọc Document File Type, Document Location Type. Không tải tệp. Ảnh images/documents-empty.jpg.

## Quyền: Role và Record Set — Chạy (chỉ đọc, bấm Cancel, không mời người)
Các bước đã làm: Mở Edit Role cả 4 vai, đọc 30 module, đóng bằng Cancel. Đọc 4 loại Record Set, mở một Record Set mặc định và form Add Record Set (không lưu).
Ma trận Role (F đủ, S một phần, N không):
| Module | Fleet Manager | Operator | Technician | Viewer |
|---|---|---|---|---|
| Vehicles, Meter Entries, Issues, Jobs, Service Entries, Warranties, Work Orders, Inspections, Service Reminders, Service Programs, Vehicle Renewal, Vendors, Places, Location Entries | F | S | S | S |
| Fuel Entries | F | S | N | S |
| Faults, Recalls | F | N | S | S |
| Service Task Management | F | N | F | N |
| Contacts, Contact Renewal | F | S | N (Technician xem Basic Info trong dữ liệu ô đánh dấu) | S |
| Parts, Purchase Orders | F | N | S | S |
| Standard Reports | F | N | N | N |
| Motor Pool | F | S | N | N |
| Expense Entries | F | N | N | S |
| Dashboards | F | N | N | N |
| Documents | F | S | N | S |
| Advanced Analytics, Integrations, Fleetio MCP | N | N | N | N |
Quyền con theo module, ví dụ Vehicles: create, edit, view_all, view_details, view_financial_info, view_custom_fields, export_data, update_status, manage_vehicle_assignment, archive_delete, view_documents, manage_documents, manage_photos. Work Orders có edit_all, edit, manage_labor_time_entries, edit_number, view_incomplete, view_completed, view_update_cost_information. Purchase Orders có approve và receive tách riêng. Motor Pool có check_out, return, cancel.
Operator được: tạo meter, fuel, issue, nộp phiếu, đổi trạng thái xe, gán xe, đặt và trả xe. Technician: tạo và sửa WO, chấm công, tạo sửa Issue, sửa tồn kho, nhận hàng PO; Fuel chỉ có ô xem.
Câu cảnh báo tiền: "Adding new Vehicles will result in additional charges to your account's subscription." ngay tại quyền Create.
Record Set:
| Loại | Bản ghi mặc định | Manage | View |
|---|---|---|---|
| Vehicles | Assigned Vehicles Only / Full Access (Default) / No Access / User's Group Only / View Only | Some / All / None / Some / None | Some / All / None / Some / All |
| Contacts | Full Access (Default) / No Access / User's Group Only / View Only | All / None / Some / None | All / None / Some / All |
| Part Locations | Full Access (Default) / No Access | All / None | — |
| Inspection Forms | Full Access (Default) / No Access | All / None | — |
Điều kiện khi tự tạo (Vehicles): All vehicles, Vehicles in this contact's group, Vehicles assigned to this contact, Specific vehicles, Vehicles in specific groups, Vehicles with specific status(es), Vehicles with specific custom field values, No vehicles. Manage và View khai riêng. Record Type "can't be changed after creation". Bản mặc định bị khoá sửa.
Màn mới: record-set-conditions — images/record-set-conditions.jpg.
Trả lời câu hỏi mở nào: OQ-1 nhóm Nền tảng: khớp Chi nhánh bằng Group nhiều cấp + "Vehicles in this contact's group"; Công ty, Cơ sở phải tự xếp thành cây Group. Không có quyền theo thời hạn (ca trực).
Không kiểm được hiệu lực thật vì không được mời người. Giải pháp đáng học: Role cho hành động, Record Set cho phạm vi, tách Manage và View; đã có "theo xe được gán" rất hợp lái xe đầu kéo. Điểm yếu: không có điều kiện theo thời gian.

## Settings: khoảng 45 trang — Chạy (chỉ đọc, không Save)
| Trang | Tham số, giá trị đọc được | Đổi rồi ảnh hưởng gì (theo câu trên màn) | Mức đọc |
|---|---|---|---|
| General Settings | Công ty, địa chỉ, ngành; tiền VND; MM/DD/YYYY; múi giờ CST; 12 hay 24 giờ; đơn vị, lít, hệ đo; Vehicle hay Asset; thuế; bật tắt module Jobs, Motor Pool, Smart Uploads (Fuel Entry, Service Entry, Inspection Form) đều On | Mặc định cho xe mới; đổi tên gọi toàn hệ thống | Đủ |
| Account Usage (trong General) | Documents 0 B of 250.0 GB; Roles 4 of 30; Vehicles 5 of 5; Automations 0 of 75; Custom Records 0 of 25 | Hết hạn mức thì chặn tạo | Đủ |
| Billing & Subscriptions | Fleetio Manage - Premium 5 Annual; Trialing; Add-On Tool Management; Account Cancellation | Không bấm Buy, Start Free Trial | Chỉ đọc |
| Export Account Data | 13 loại dữ liệu, CSV hoặc XLS; "the download link in the email expires after 7 days" | Gửi email, không bấm | Đủ |
| Sandboxes | Sample Copy 0/2; Production Copy 0/0 | Môi trường thử | Đủ |
| Notification Profiles | 0 hồ sơ; gán bulk từ Contacts | Quy định ai nhận gì | Đủ |
| Watched Vehicle Groups | 11 nhóm, cột Direct Watchers, Total Watchers | Quy định xe nào được báo | Đủ |
| Manage Users | Trỏ sang `contacts/users` ngoài Settings | — | Mở |
| Security | Minimum Length 8, 15, 30, 50; Expiration None, 30, 60, 90 ngày; chữ hoa thường, số, ký tự; Maximum invalid login attempts 5, 10; Lockout 5, 10, 30 phút; Reset All Passwords | Áp khi tạo hoặc đặt lại mật khẩu, không áp SAML | Không bấm |
| Roles, Record Sets | Xem mục Quyền | | Đủ |
| AI Service Advisor | Issue Prioritization, Issue Resolution, Fault Monitoring, Service Assessments, Service Writer, mỗi cái có Manage | Có câu điều khoản; không bấm | Đủ |
| Integrations Directory | Chỉ thấy link, không mở | | Không mở |
| Integration Links | Rỗng; link sang hệ khác kèm biến | | Đủ |
| Webhooks | Rỗng; "send a HTTP POST" dạng JSON | | Không tạo |
| External Connections | Rỗng; FTP, SFTP, Amazon S3 cho báo cáo định kỳ | | Không tạo |
| SAML Connectors | Rỗng, có Metadata | | Không tạo |
| Fleetio MCP | "Each connection respects the user's role permissions." | | Không bật |
| Standard Records | 15 loại bản ghi có trường tuỳ chỉnh, đều 0 | | Đủ |
| Custom Records | Rỗng, Add Custom Record | | Không mở |
| Groups & Subgroups | Xem trên; Require Group | | Đủ |
| Saved Views, Labels, Custom Widgets, External Vehicle IDs | Rỗng | | Đủ |
| Vehicle Statuses | 5 trạng thái có đếm xe, Add Vehicle Status | | Đủ |
| Vehicle Types | 25 loại, Car mặc định | | Đủ |
| Expense Types | 17 loại | | Đủ |
| Expense Settings | Auto Generate Loan / Lease Expenses | Tự sinh chi phí trả góp | Đủ |
| Tire Management Settings | Automated tire pressure readings (chỉ 4x2, 4x4 có telematics); Tire Rotation Patterns theo cấu hình trục, thêm được mẫu | | Một phần danh sách mẫu |
| Motor Pools, Reservation Rates, Flat Fees | Rỗng | Bảng giá đặt xe, phí cố định | Đủ |
| Inspection Settings | Proximity Threshold 80%, Distance Threshold 100 m | Bật cảnh báo Location Exception khi phiếu nộp từ một chỗ | Đủ |
| Issue Priorities | No Priority (Default), Low, Medium, High, Critical; có alias; tắt được | | Đủ |
| Fault Rules | 11 mã | | Một phần |
| Service Reminder Settings | Recalculate; Forecasting tắt | Dự báo ngày đến hạn theo km ngày | Đủ |
| Vehicle Renewal Types | Emission Test, Inspection, Insurance, Registration | | Đủ |
| Contact Renewal Types | Certification, License Renewal | | Đủ |
| Maintenance Settings | Enable Work Orders, Next Work Order Number, Require a Meter Reading + Excluded Vehicle Types, Require inspections, Repair Priority Class, Reason for Repair, Category, khoá sửa mã, Inventory Location, Expected Labor Hours, Complaint/Cause/Correction, Markups | "This requirement only applies to future Work Orders or Service Entries." | 3.800/3.965 ký tự |
| Work Order Statuses | Open (Default), Pending, Completed; Type Incomplete, Completed; Add | Completed "corresponding service reminders updated and issues resolved" | Đủ |
| Reason For Repair Codes | 59 mã | | Một phần |
| Repair Priority Class Codes | Scheduled, Non-Scheduled, Emergency | | Một phần |
| System/Assembly/Component Codes | Cây VMRS 10 nhóm | | Một phần |
| Warranty Templates | Rỗng | | Đủ |
| Part Settings | Enable Inventory Tracking By Default | | Đủ |
| Part Locations | TEST-KHO-01, 02; Active, Archived | | Đủ |
| Part Categories | 8 loại | | Một phần |
| Part Manufacturers | Rỗng | | Đủ |
| Inventory Adjustment Reasons | 11 lý do | | Đủ |
| Inventory Valuation Method | Average Cost, FIFO, LIFO, Static Pricing | Giá xuất kho | Một phần |
| Measurement Units | 8 đơn vị | | Đủ |
| Purchase Order Settings | Next Purchase Order Number; Automatically Close Fully Received POs | | Đủ |
| Purchase Order Statuses | Draft, Pending Approval, Rejected, Approved, Purchased, Received Partial, Received Full, Closed; không có Add | Cố định, khác WO | Đủ |
| Fuel & Energy Settings | WEX auto-assign; Fuel Vendor Location Alert Radius | | Đủ |
| Fuel Types | 11 loại | | Một phần |
| Saved Reports | Chưa đọc do lỗi đợt | | Không |
Nối với `docs/_product/saas-core-vs-tenant.md`: Vehicle hay Asset ứng với từ điển thuật ngữ theo khách; Work Order Statuses (khung Type cố định, khách thêm tên) khớp đúng "Lõi khung trạng thái + Cấu hình nhãn"; Require Meter + Excluded Vehicle Types là mẫu cho loại xe không đồng hồ như mooc; PO Statuses cố định là ví dụ phần không cho khách đổi.
Trả lời câu hỏi mở nào: OQ-4 nhóm Nền tảng: Fleetio tách Sandbox, MCP theo hạn mức gói; còn tên gói của Invlogis vẫn phải chốt.

## Trang đầu — Chạy
Đích từng thẻ: Open Issues Open `issues/state/opened`, Overdue `issues/state/overdue`; Service Reminders Overdue, Due Soon `service_reminders/status/*`; Overdue Inspections `inspection_schedules/status/overdue`, % `.../all`; Critical Faults `faults`, Open, Pending `faults/state/*`; Vehicle Renewal và Contact Renewal Overdue, Due Soon `.../status/*`. Không có đích: "ROs Needing Approval" khi rỗng. Onboarding Tasks trỏ 7 đường `onboarding/*`, `getting_started/*`. Số thật: Open 38, Overdue 3, xe quá hạn nhắc 8. Có "0 minutes ago", Refresh data, All groups. Dưới có Cost, Inspections, Recent Activity.
Bất ngờ: "Get Started" đổi 3/5 và 3/6 giữa các trang.

## Báo cáo chuẩn — Một phần (đọc 49 tên; mở sâu 1 báo cáo)
Nhóm và số: Vehicles 14, Vehicle Assignments 2, Inspections 4, Issues 2, Service 8, Warranties 2, Work Orders 5, Contacts 2, Parts 4, Fuel 3, Tools 1, Jobs 1, Motor Pools 1 = 49 báo cáo, 13 nhóm (SRS cũ ghi 48, 12). "Upgrading soon" trên Cost/Meter Trend, Expense Summary, Operating Costs Summary, Service History by Vehicle.
Issues Report: biểu đồ Summary, Top Vehicles; Filters, Columns, phân trang; Save, Share, Export CSV (Export Visible Columns | Export All Columns), Print. Ảnh images/report-issues.jpg. Chưa mở 48 báo cáo còn lại nên không có bảng cột, lọc của từng cái.
**Sự cố do tôi gây, đã khắc phục:** bấm Share SINH NGAY liên kết công khai, không hỏi trước, "Link expires in 7 days", "this link allows anyone with access to view all data". Mở thử trong khoảng 5 phút thấy xem được dữ liệu Issues. Link "click here to unshare" trong hộp bấm không có tác dụng (bấm lại trả 404) và tôi mở kiểm thì link vẫn sống. Thu hồi đúng qua Reports › Shared › ... › Unshare, hộp "Are you sure you want to unshare this report?"; Shared về 0, mở lại không còn báo cáo. Không gửi link cho ai, không ghi mã link vào đây.
Giải pháp đáng học, điểm yếu: có hạn 7 ngày và danh sách Shared để thu hồi tốt. Điểm yếu nặng: sinh link công khai ngay khi mở hộp; lối thu hồi trong hộp lỗi. Invlogis: phải bấm tạo mới có link, và ghi nhật ký.

## Ask a data question — Chạy (2 câu, kết quả sai so với dữ liệu thật)
Các bước đã làm: Bấm nút trên đầu trang. Vào `advanced_analytics/agent` "AI Data Analyst", khung nhúng từ ThoughtSpot. Không có màn mở trial, không bấm gì liên quan trial. Hỏi 2 câu về TEST-XE-01.
| Câu hỏi | AI trả lời | Dữ liệu thật trên trang xe | Thời gian |
|---|---|---|---|
| "How many open issues does vehicle TEST-XE-01 have?" | "currently has 2 open issues", bảng Total Count Issue Id = 2 | Open 7 | Khoảng 40 giây |
| "What is the latest meter reading of TEST-XE-01 and when was it recorded?" | "1,700.0 (primary meter), recorded in November 2026" | 2.999 km | Khoảng 50 giây |
Bất ngờ: Câu trả lời khẳng định "currently" nhưng số cũ, không ghi dữ liệu tính đến lúc nào. Khả năng do kho phân tích trễ so với dữ liệu giao dịch (suy luận, chưa kiểm). Có "Show work", chọn "All data models", lưu "My Conversations". Ảnh images/ai-analyst-issues.jpg.
Giải pháp đáng học, điểm yếu: hỏi bằng lời ra bảng, xem được cách làm. Điểm yếu: số sai im lặng, không ghi độ trễ. Invlogis nếu làm phải ghi "dữ liệu đến thời điểm".

## Màn bị chặn
| Màn | Vì sao | Xử lý |
|---|---|---|
| Add Vehicle | "Your plan is limited to 5 vehicles" | Dừng, không dùng Add Multiple hay nhập tệp |
| Tools, Tool Management | Brief cấm; xem mục Trial Tools bên dưới | Không mở |
| Custom Records | Brief cấm thiết lập; chỉ đọc màn rỗng | Không mở |
| Advanced Analytics (ngoài AI Data Analyst) | Brief cấm mở trial; chưa thấy màn chặn | Không mở |
| Motor Pool thử đặt xe | Cần tạo Motor Pool trong Settings, cần xe của nhóm | Không chạy |

## Trial Tools đã bị bật, không do nhóm này
Lúc đầu lượt, Billing ghi Tool Management "Start Free Trial" và thanh bên có nhãn "Try". Cuối lượt, Billing ghi "Tools - Monthly 25", "Trialing", "14 days left in trial", "Tools 0 of 25", có "Disable Add-On". Nhóm này không bấm nút đó; không xác định được ai bật. Không tắt vì đây là thay đổi cài đặt tài khoản ngoài phần được giao.

## Chưa làm trong lượt này
Đổi trạng thái thật và Archive xe, bản ghi trùng tên xe, Motor Pool chạy thật: cần một chỗ xe (5 of 5). Vòng lặp chéo, lượt thất bại, version v.2. Cột và lọc của 48 báo cáo. Saved Reports. Mẫu Send Email WO. Hiệu lực quyền thật.
