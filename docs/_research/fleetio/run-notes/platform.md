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

# Lượt 3 (03/11)

Tiền tố dữ liệu nhóm: `TEST-NEN`. Mức ghi đúng theo thao tác của lượt này.

## 49 tên báo cáo chuẩn — Chạy (đọc từ danh sách Standard Reports, OQ-11)
| Nhóm | Số | Tên (đường dẫn sau `reports/`) |
|---|---|---|
| Vehicles | 14 | Cost Comparison by Year in Service (`vehicles/cost_comparison_by_year_in_service`), Cost/Meter Trend (`vehicles/cpm_trend`), Expense Summary (`vehicles/expense_summary`), Expenses by Vehicle (`expense_entries`), Group Changes (`vehicle_group_changes`), Operating Costs Summary (`vehicles/operating_cost_summary`), Status Changes (`vehicle_status_changes`), Status Summary (`vehicle_status_summaries`), Tire Activity Report (`tire_activities`), Total Cost Trend (`vehicles_total_cost_trend`), Utilization Summary (`vehicles_utilization_summary`), Vehicle Details (`vehicles/details`), Vehicle Renewal Reminders (`vehicle_renewal_reminders`), Vehicles Report (`vehicles`) |
| Vehicle Assignments | 2 | Vehicle Assignment Log (`vehicle_assignments`), Vehicle Assignments Summary (`vehicle_assignments/summary`) |
| Inspections | 4 | Inspection Failures List (`inspections/failures`), Inspection Schedules (`inspections/schedules`), Inspection Submission List (`inspections`), Inspection Submissions Summary (`inspections_summary`) |
| Issues | 2 | Faults Summary (`faults/summary`), Issues List (`issues`) |
| Service | 8 | Maintenance Categorization Summary (`vmrs_system_assembly_components/summary`), Repair Priority Class Summary (`repair_priority_classes/summary`), Service Entries Summary (`service_entries/summary`), Service History by Vehicle (`service_entries`), Service Reminder Compliance (`service_reminder_compliance`), Service Reminders (`service_reminders`), Service Task Summary (`service_tasks/summary`), Vehicles Without Service (`vehicles_without_service`) |
| Warranties | 2 | Part Warranty Opportunities (`part_warranty_opportunities`), Vehicle Warranty Opportunities (`vehicle_warranty_opportunities`) |
| Work Orders | 5 | Labor Time Entries List (`work_orders/labor_time_entries`), Technician Labor Summary (`work_orders/technician_summary`), Work Order Status Summary (`work_order_status_changes/summary`), Work Orders by Vehicle (`work_orders/by_vehicle`), Work Orders List (`work_orders`) |
| Contacts | 2 | Contact Renewal Reminders (`contact_renewal_reminders`), Contacts List (`contacts`) |
| Parts | 4 | Parts Activity Report (`inventory_journal_entries`), Parts by Location (`part_locations`), Parts by Vehicle (`parts/by_vehicle`), Purchase Orders List (`purchase_orders`) |
| Fuel | 3 | Fuel Entries by Vehicle (`fuel_entries`), Fuel Summary (`fuel_summary`), Fuel Summary by Location (`fuel_entries/by_location`) |
| Tools | 1 | Tool Service Entries Summary (`tool_service_entries_summary`) |
| Jobs | 1 | Job Assignments Summary by Job (`job_assignments_summary_by_job`) |
| Motor Pools | 1 | Motor Pool Reservations Summary (`motor_pool_reservations_summary`) |
Nhãn "Upgrading soon" đúng 4: Cost/Meter Trend, Expense Summary, Operating Costs Summary, Service History by Vehicle.
Tab đầu: Favorites 0, Saved 0, Shared 0. Thanh bên còn ghi "Tool List 13 days left".

## 49 báo cáo: mở từng cái, cột thật — Chạy 48/49 (chỉ đọc, không bấm Share)
Các bước đã làm: Nạp lần lượt 49 đường dẫn, đọc tiêu đề cột và nút trên màn. Không bấm gì trong báo cáo. Giá trị lọc chưa mở từng cái, xem mục sau.
Hai thế hệ giao diện: **M** (mới, có Save, Share, Export CSV, Print, Filters, Columns, nhiều cái có biểu đồ) và **C** (cũ, chỉ thấy Save, Filters, Add Filter; không thấy nút Share, Export CSV dạng nút trên màn). "+Xe" = kèm khối khoảng 110 cột thông tin xe chọn được trong Columns (Group, Make, Model, chi phí trọn đời, thông số kỹ thuật...). "Dòng" là số dòng lúc đọc, có TEST lẫn Sample.
| Đường dẫn | Kiểu | Dòng | +Xe | Tổng cột | Cột riêng của báo cáo | Chiều nhóm trên màn |
|---|---|---|---|---|---|---|
| contact_renewal_reminders | M | 81 | | 31 | Status, Renewal Type, Due Date, Contact, Subscribers + khối liên hệ | |
| contacts | C | 55 | | 10 | Full Name, Group, Email, Employee Number, Job Title, Start Date, Leave Date, License Number, License State, License Class | |
| vehicles/cost_comparison_by_year_in_service | M | 20 | có | 112 | Year 1..8, Avg. Cost / Meter | |
| vehicles/cpm_trend | M | 25 | có | 115 | Theo tháng; biểu đồ | |
| vehicles/expense_summary | M | 2 | | 14 | Expense Type, Transactions, Vehicles, Cost, Total | Group: Expense Type |
| expense_entries | C | ? | | ? | **Không đọc được: trang không tải xong trong 12 giây, chưa mở lại** | |
| faults/summary | M | 11 | | 20 | Code, Name, Description, Priority Handling, Vehicle Count, Open, Pending, Ignored, Resolved, Total, First Occurred, Last Occurred | All statuses; Group: Fault Only |
| fuel_entries | M | 59 | có | 129 | Date, Occurred at, Vendor, Vendor region, Odometer, Void, Usage, Price/Gallon, Fuel Economy, Cost, Partial, Reset, Reference, Vehicle Exception Alert | |
| fuel_summary | C | 23 | | 8 | Name, Usage, Gallons, Economy, Cost/Usage, Total Fuel Cost, Cost/Gallon, Last Fuel Date | |
| fuel_entries/by_location | M | 0 | | 13 | Fuel Vendor Location, Transactions, Gallons, Cost | Group: Location Only |
| vehicle_group_changes | M | 0 | có | 116 | From, To, User, Date, Duration | |
| inspections/failures | M | 10 | có | 129 | Date, Submission, Form, Form Version, Submission Source, Submitted By, Duration, Item, Stage, Issue, Acknowledged By, Acknowledged At, Acknowledged Comment; biểu đồ | Count |
| inspections/schedules | M | 5 | có | 117 | Operator, Inspection Form, Due Date, Last Inspected, Schedule, Overdue | |
| inspections | M | 16 | có | 148 | Date, Inspection Form, Form Version, Started at, Submitted at, Submission Source, Duration, Failed Items + khối người; biểu đồ | By Day |
| inspections_summary | C | 25 | | 5 | Name, Submissions Count, Forms Count, Average Duration, Group; biểu đồ | Submissions by Vehicle, by User |
| issues | M | 53 | có | 133 | Issue, Status, Priority, Summary, Reported Date, Reported By, Assigned, Due Date, Due Meter, Closed, Resolved, Resolved with, Reopened, Resolved Meter Variance, Time to Resolve in Days, Asset Record Type | |
| job_assignments_summary_by_job | C | 0 | | 8 | Vehicle, Vehicle Type, Assignments Count, Days On Job, Usage, Meter Unit, Avg/Day, Job | |
| work_orders/labor_time_entries | M | 0 | | 9 | Technician, Work Order, Vehicle, Service Task, Expected Labor Hours, Notes, Started At, Ended At, Duration | |
| vmrs_system_assembly_components/summary | M | 5 | | 15 | Category Code, Line Item Usage, Latest Usage, Labor Costs, Parts Costs, Subtotal; biểu đồ | Group: Category Code |
| motor_pool_reservations_summary | C | 0 | | 15 | Number, Motor Pool, Reservation Status, Reason for Trip, Pick Up, Drop Off, Approved At, Completed At, Meter/Duration/Flat Fees Subtotal, Total Amount, Assigned Vehicle Name, Group, Operator Name | |
| vehicles/operating_cost_summary | M | 8 | có | 116 | Service, Fuel, Other, Total Cost, Cost/Meter (Filtered); biểu đồ | Group: Vehicle Group |
| part_warranty_opportunities | C | 0 | | 6 | Replacement Work Order Number, Vehicle Name, Vehicle Group, Part Number, Part Description, Original Work Order Number | |
| inventory_journal_entries | M | 31 | có | 156 | Created at, Previous/Adjustment/New Quantity, Associated Work Order, Associated Inspection, Adjustment Unit Cost, Adjustment Type, Inventory Adjustment Reason, Vendor, Part..., Part Location, Contact | |
| part_locations | M | 4 | | 15 | Part Location, Total Inventory Value, Part, Category, Unit Cost, Aisle / Row / Bin, Current Quantity, Work Order Current Quantity, Purchase Order Current Quantity, Reorder Point | Sort: Number |
| parts/by_vehicle | M | 5 | có | 137 | Part..., Work Order, Part Location, Vendor, Assigned to, Issue Date, Invoice Number, PO Number, Part unit price, quantity, subtotal, Total | |
| purchase_orders | M | 4 | | 38 | PO, Description, Part Location, Vendor; người + ngày cho từng bước Submitted, Rejected, Approved, Purchased, Partially Received, Received In Full, Closed; Line Items, Subtotal, Shipping, Discount, Tax, Tax 2, Total Amount; biểu đồ | Layout: Group by Purchase Order |
| repair_priority_classes/summary | M | 15 | có | 127 | Last Service Date, # Service Entries, # Service Tasks, Duration, Labor, Labor markup, Parts, Parts markup, Subtotal, Tax, Warranty Credits, Total, # Scheduled, # Non-Scheduled, # Emergency; biểu đồ | |
| service_entries/summary | M | 15 | có | 127 | Giống dòng trên, không biểu đồ | |
| service_entries | M | 107 | có | 153 | Service Entry, Repair Priority Class, Actual Start, Completion, Reference, External ID, Invoice Number, Invoice Date, nhiều cột Auto Integrate RO, Vendor, Minority Owned (MBE), Women Owned (WBE), Work Order Number, Service Tasks, Resolved Issue Numbers, Total Labor, Total Parts, Tax, Fees | Layout: Group by Service Entry |
| service_reminder_compliance | M | 168 | có | 121 | Due At, Completed At, On-Time Status, Service Task, Expected Labor Hours, Due/Completed Meter Value; biểu đồ | Group: Individual Service Reminders |
| service_reminders | C | 0 đọc được | | 12 | Status, Service Task, Subtasks, Incomplete Work Orders, Meter Interval, Due Meter, Meter Variance, Time Interval, Due Date, Time Variance, Vehicle, Group | |
| service_tasks/summary | M | 27 | | 21 | Default Category, Default System, Service Task, Expected Labor Hours, Usage, # Vehicles, Last Service Date, Labor, Parts, Subtotal; biểu đồ | Group: Service Task Only |
| vehicle_status_changes | M | 27 | có | 115 | From, To, User, Date | |
| vehicle_status_summaries | M | 25 | có | 117 | Chưa tách được cột riêng (dùng làm mốc khối xe) | |
| work_orders/technician_summary | M | 9 | | 43 | Technician + khối liên hệ, Average Hourly Rate, Work Orders, Line Items, Hours/Line Item, Total Hours, Cost/Line Item, Total Labor Cost | Layout: Group by Technician |
| tire_activities | C | 96 | | 13 | Vehicle, Date Installed, Date Recorded, Tire Model, Tire Meter, Activity, Method, User, Pressure, Tread Depth, Position, Axle Type, Tire Identification Number | |
| tool_service_entries_summary | C | 0 | | 10 | Name, Brand, Model, Serial Number, Service Entries Count, Total Labor Subtotal, Aggregated Subtotal, Total Tax 1, Tax 2, Aggregated Total | |
| vehicles_total_cost_trend | C | 25 | | 4 | Name, 3 tháng gần nhất | |
| vehicles_utilization_summary | C | 25 | | 9 | Name, Group, Min Value, Min Date, Max Value, Max Date, Usage, Avg/Day, Meter Unit | |
| vehicle_assignments | M | 0 đọc được | có | 142 | Operator + khối liên hệ, Start Date/Time, End Date/Time, Duration, Start Meter, End Meter, Distance | |
| vehicle_assignments/summary | M | 25 | có | 115 | # Assignments, # Operators, % Assigned; biểu đồ | Group: Vehicle |
| vehicles/details | M | 25 (10 mỗi trang) | | 54 | Dạng hồ sơ từng xe, không phải bảng: thông số, Purchase, Lifecycle, Loan/Lease, Recent Comments, Images, Service Reminders, Vehicle Renewal Reminders. Không có Export CSV | |
| vehicle_renewal_reminders | M | 21 | có | 114 | Status, Renewal Type, Due Date, Vehicle, Subscribers | |
| vehicle_warranty_opportunities | C | 4 | | 8 | Warranty Name, Work Order Number, Service Task, Vehicle Name, Vehicle Group, Complaint, Cause, Correction | |
| vehicles | C | 25 | | 12 | Name, Group, Year, Make, Model, Type, Status, Operator, VIN/SN, License Plate, Cost Per Meter Unit (Lifetime), Service Programs | |
| vehicles_without_service | M | 3 | có | 111 | Khối xe | |
| work_order_status_changes/summary | M | 3 | | 14 | Status, Entered, Left, Start to End, Net Change. Không có Export CSV | |
| work_orders/by_vehicle | M | 108 | có | 141 | Work Order, Repair Priority Class, Vendor, Invoice Number, PO Number, Assigned To, Issue, Start, Completion Date, Duration, Line Item Count, Service Tasks, Resolved Issues, Labor Hours, Parts Quantity, Labor, Parts Subtotal + Markup, Tax, Discount, Total Amount | |
| work_orders | C | 0 đọc được | | 9 | Number, Status, Repair Priority Class, Resolved Issues, Issue Date, Scheduled Start Date, Expected Completion Date, Assigned To, Total Cost | |
Kết luận đọc được: 22 báo cáo thế hệ mới có khoảng 110 cột xe gắn sẵn, nên người dùng tự ghép bảng rộng thay vì nhiều báo cáo riêng. Báo cáo Sample Issues có 53 dòng, `vehicles` 25 xe: đếm cả Sample.
Trả lời câu hỏi mở: OQ-11 phần 49 tên và cột, trừ `expense_entries`. Giá trị lọc: xem mục dưới.
Không kiểm: "0" ở vài báo cáo có thể do chưa kịp tải khi đọc (đánh "0 đọc được"); không ngắt lấy lại từng cái.

## Báo cáo: lọc, lưu, yêu thích, lưới và danh sách — Chạy
Các bước đã làm: Mở Issues Report, Filters, lọc Issue Summary TEST-NEN, Search. Save ở chế độ Private. Sang Reports › Saved, đổi List display, bấm sao, mở báo cáo đã lưu. Mở lại `expense_entries`.
Kết quả thấy được:
- Bộ lọc Issues Report 26 ô: Issue Summary, Issue Source, Reported Date, Time to Resolve in Days, Due Date, Resolved Date, Closed Date, Status, Labels, Reported By, Resolved By, Assigned to, Priority, Vehicles, Vehicle Types, Vehicle Groups, Status (xe), Vehicle Year, Make, Model, Trim, Current Operator, VIN/SN, License Plate, Registration State/Province, Include archived vehicles.
- Bộ lọc nằm trên đường dẫn (`q[summary_or_description_cont]`): tìm cả tiêu đề lẫn mô tả dù nhãn ghi "Issue Summary". Biểu đồ và thẻ đếm tính lại: Open 6, Overdue 0.
- Hộp "New Saved Report": Name *, Description, Visibility Public | Private (mặc định Private), Email Schedule (ô tick, không tick). Câu giải thích: "Private Saved Reports are visible only to you, but can be emailed to anyone with access to the source report."
- Reports › Saved: cột Name, Description, Report Type, Schedule. Menu dòng: View Source Report, View Record History, Edit, Make a Copy, Delete. Bấm sao: Favorites từ 0 lên 1. Mở báo cáo đã lưu sang tab mới, đường dẫn thêm `saved_report_id=484032` và giữ bộ lọc.
- **`reports/expense_entries` (Expenses by Vehicle) trả Error 500 "We're sorry, but something went wrong.", chân trang ghi "Partially Degraded Service".** 2 lần mở cùng lỗi. Có thể sự cố tạm của hãng, chưa thử lại sau. Ảnh images/report-expense-entries-500.jpg.
Không chạy: Share (brief cấm), Public, Email Schedule (gửi email).
Trả lời câu hỏi mở: OQ-11 Saved Reports là bộ lọc + cột của báo cáo chuẩn lưu lại kèm Private hoặc Public và lịch gửi email.
Dữ liệu TEST đã tạo: báo cáo Private `TEST-NEN-BC-01 Issue loc TEST` (id 484032), đang yêu thích.

## Danh sách, chế độ xem, xem nhanh — Chạy
Các bước đã làm: Trên Issues, tab All, gõ TEST-NEN; mở Group, View Settings, Manage Columns (Cancel); Save as New View ở Private; hover dòng, mở menu dòng; bấm dòng.
| Case | Điều kiện | Kết quả thật |
|---|---|---|
| Tìm trên danh sách | Gõ TEST-NEN | Ra 6 dòng, nút Save View đổi thành Save Changes có chấm cam |
| Nhóm dòng | Group | None, Priority, Vehicle or Tool, Group |
| Cài đặt xem | View Settings | Manage Columns (có nhãn "1 New"), Items Per Page 50, 100, 200, Density Default, Compact |
| Chọn cột | Manage Columns | Available 27 (ISSUE 9/21, VEHICLE/TOOL 2/6), Visible 11, kéo đổi thứ tự, Restore defaults |
| Sửa bản chuẩn | Menu Save Changes ở All | "Fleetio Standard View" có khoá, "Save as a new view to keep your changes"; chỉ có Save as New View, Clear Unsaved Changes |
| Lưu view | Name, Description, Shared with | Shared with: Private ("Visible only to you"), Admins Only, Specific Roles, Specific Users, Everyone. Lưu xong thành tab mới cạnh All, Open... và có `saved_view_id` riêng |
| Trang nhớ tab | Mở lại /issues | Mở đúng tab đang dùng lần trước (lúc vào là Closed) |
| Menu dòng | Hover dòng | View, Edit, Add to Service Entry, Add to Work Order, Get Service at Shop, Resolve with Note, Check service history (khoá), Close, Delete |
| Bấm dòng | Issues | Sang trang chi tiết, **không mở khung xem nhanh**. Không thấy Record peek ở màn này |
Trạng thái FR-saas-platform-011 vẫn là Xem: chưa thấy peek trên Issues, chưa thử màn khác.
Dữ liệu TEST đã tạo: view Private `TEST-NEN-VIEW-01` (id 30798100) trên Issues.

## Theo dõi, bình luận, lịch sử, thông báo — Chạy
Các bước đã làm: Trên Issue #55: gõ comment có @, đăng, Unwatch, xem Record History, Watch lại. Mở chuông.
- @ hiện danh sách liên hệ kèm biểu tượng khoá (không có quyền truy cập). Gõ "@Bao" không ra "Bảo Tín" (không bỏ dấu), gõ "@TEST-NEN" không ra `TEST-NEN-LH-01` (không khớp có gạch nối); đăng thành chữ thường, không tạo mention. Không nhắc ai thật.
- Unwatch: avatar mất khỏi cụm người theo dõi, nút thành Watch. Watch lại được. Comment, Watch không vào Record History.
- **Record History #55 có dòng "Issue Priority Status changed from pending to failed"**: AI Issue Prioritization chạy nền, thất bại im lặng, Issue về "No Priority". Lỗi này không báo ra đâu khác. Ảnh images/record-history-issue.jpg.
- Bộ lọc Record History: chọn khoảng ngày. Cột Date, Changes By, Changes Made.
- Chuông: Notifications, tab Inbox, Archived; lọc All Activity, Comments Only, @ Mentions; Archive all; từng dòng có Reply, View All Comments; menu Notification Settings. Người theo dõi nhận thông báo in-app khi automation bình luận ("Fleetio Automation commented on an issue").
- **Tài khoản có 0 hồ sơ thông báo nhưng Inbox vẫn có "Fuel Capacity Alert / Fuel Entry #... / TEST-KHO-01"**: thông báo in-app của người theo dõi chạy kể cả khi chưa có hồ sơ. Ảnh images/notifications-inbox.jpg.
- Tìm toàn cục TEST-NEN: danh sách trả về theo nhóm: VEHICLES, CONTACTS, SERVICE ENTRIES, VENDORS, PARTS, ISSUES..., mỗi nhóm 3 dòng và More; ô chọn loại có 16 mục. Kết quả có cả TEST-XE-01, TEST-KHO-NCC-02: không đòi khớp cả cụm, tách theo từ "TEST", "NEN".
Dữ liệu TEST đã tạo: 1 comment trên Issue #55.

## Kho tài liệu — Chạy
Các bước đã làm: Upload Document từ tệp `TEST-NEN-tailieu.txt` một dòng, 26 Bytes. Xem danh sách, menu dòng, Select Vehicles, gắn TEST-DAUKEO-2, mở trang tệp.
Kết quả thấy được:
- Hộp tải là Filestack: từ máy, Facebook, GitHub, tìm web, link, camera, Instagram, Box. Tên nhà cung cấp lộ ra; chỉ dùng từ máy. "Document was successfully added."
- Danh sách cập nhật chậm: ngay sau tải vẫn "No results to show", tải lại mới có.
- Dòng: File Name, File Size, Location, Auto-Delete, Attached To, Labels. Menu: View, Rename, Replace, Download, Delete.
- Select Vehicles mở "Attach Document to Vehicles": tìm, Attached Vehicles, All Vehicles 25, Vehicle Types 25, Groups 11. Gắn xong nút thành "Attached". **Gắn được theo nhóm và loại** (chưa bấm), hợp với giấy tờ chung cả đội đầu kéo.
- Trang tệp: khung xem PDF hiển thị 0 trang với .txt (không xem trước được); Location, Attached to "1 Vehicle", Labels, Type Text File, File Size, Auto-Delete có câu giải thích (xoá cuối ngày đã chọn), Last Modified, Uploaded, Add Description, Comments.
- Account Usage: Documents "26 B of 250.0 GB". Ảnh images/documents-list-file.jpg.
Dữ liệu TEST đã tạo: tệp `TEST-NEN-tailieu.txt` (id 17765168), gắn TEST-DAUKEO-2.

## Giới hạn theo gói — Xem thêm
Account Usage lúc đọc: Documents 26 B of 250.0 GB, Roles 4 of 30, Vehicles 5 of 5, Tools 0 of 25, **Automations 0 of 75 dù có 7 automation lưu trên tài khoản, đều đang tắt: hạn mức chỉ đếm bản đang bật** (`Suy` từ số đọc, chưa đọc lúc đang bật), Custom Records 0 of 25.

## Lượt automation thất bại — Chạy (OQ-6)
Các bước đã làm: Tạo `TEST-NEN-AUTO-06` (96509): Work Order Created, Invoice Number contains TEST-NEN-F, Update Work Order Status to Completed. Bật. Tạo WO #111 trên TEST-DAUKEO-2, Invoice Number TEST-NEN-F1, không có Start Date. Đọc Run History sau khoảng 5 phút. Tắt.
| Case | Kết quả thật |
|---|---|
| Điều khiển Completed được chọn | Khác Create Record (chỉ Open, Pending): Update Field Status có đủ Open, Pending, Completed |
| Lượt chạy | Failed 1, Successful 0, nhãn FAILURE đỏ |
| Câu lỗi | Băng đỏ trong Run Result: "Automation Action failed: Start Date can't be blank" |
| Log | Workflow, Trigger, ConditionSet đều state DNF, status FAILURE, cùng reason, có caused_by, thrown_by trỏ bước gây lỗi |
| Bản ghi | WO #111 vẫn Open, không đổi. "Records: No records changed" lần này đúng |
| Thử lại | Sau khoảng 5 phút, Total Runs vẫn 1: không thấy tự thử lại trong khoảng đó |
| Tự tắt | Automation vẫn Enabled sau lượt lỗi, không tự tắt |
| Báo người dùng | Người tạo WO không thấy lỗi trên trang WO; chuông không có dòng nào; ô Failure Notification Email đang tắt nên chỉ biết khi vào Run History |
Không chạy: Failure Notification Email (gửi email, brief cấm), nên chưa biết nội dung email.
Ảnh images/automation-run-failure.jpg.
Trả lời câu hỏi mở: OQ-6 trừ nội dung email. Phát hiện kèm: luật "WO Completed" có kiểm tra giống form tay (Start Date bắt buộc), tức automation không lách được ràng buộc nghiệp vụ.
Giải pháp đáng học, điểm yếu: câu lỗi nghiệp vụ nguyên văn, có log từng bước. Điểm yếu: lỗi im lặng nếu không bật email; không có màn gom lỗi toàn bộ automation ngoài cột Failed Runs.
Dữ liệu TEST đã tạo: automation 96509 (đã tắt); WO #111 Open trên TEST-DAUKEO-2.

## Loại bản ghi, trigger — Một phần (FR-saas-platform-013)
| Bản ghi | Kiểu sự kiện đọc được | Mức |
|---|---|---|
| Issue | Created, Updated, Created or Updated, Deleted | Chạy Created, Created or Updated |
| Vehicle | Created, Updated, Created or Updated (không Deleted) | Chạy Updated |
| Work Order | Created, Updated, Created or Updated, Deleted | Chạy Created |
| Service Entry | Created, Updated, Created or Updated, Deleted | Xem |
| Geofence Event | Đã có `TEST-Geofence` của nhóm khác, 2 lượt | Không do nhóm này |
| Fault, Purchase Order | Có trong danh sách; chưa đọc kiểu sự kiện | Xem |
Trường điều kiện: Work Order 61 mục (nhóm WORK ORDER, VEHICLE; không có Description, phải dùng Invoice Number để khoanh vùng); Vehicle 71 mục. Update Field của Work Order: Status, Repair Priority Class, Issued By, Assigned To, Vendor, Labels. Hành động của Work Order: Update Field, Add Comment, Send Email, Create Record.
Hai automation lật giá trị nhau (OQ-5): **Không chạy**: AUTO-05 đã cho thấy một lượt do automation đổi xe không sinh lượt mới, nhưng thử chéo có thể lặp không biết giới hạn trên hệ thống thật. Giữ OQ-5, nhóm chưa có căn cứ an toàn để thử.

## Thông báo của automation — Xem thêm (FR-saas-platform-037)
Run Summary Email: "Receive a summary email of successful automations. Select from Daily at 6:00 am, or Weekly on Mondays at 6:00 am." Failure Notification Email: "Send an email whenever this automation fails." Mention trong comment: "Notifications for mentions in comments are delivered based on users' permissions and notification settings." Có ô Prevent duplicate comments. Không bật: gửi email.

## AI hỏi dữ liệu, chỉ TEST — Chạy (OQ-13)
| Câu hỏi | AI trả lời nguyên văn | Thật | Thời gian |
|---|---|---|---|
| "How many open issues does vehicle TEST-XE-01 have, and what is the data as-of date? List the issue numbers." | "Vehicle TEST-XE-01 has 10 open issues." Số: 31, 32, 39, 40, 42, 43, 44, 47, 48, 50 | 12 mở: thêm #49, #51 | Khoảng 60 giây |
| Cùng câu, phần ngày dữ liệu | "The dataset does not expose a specific "data as-of date" field for when the data was last refreshed." rồi đẩy sang "your system's data pipeline or integration settings" | Không có ngày dữ liệu nào trên màn | |
| "List open issues of vehicle TEST-DAUKEO-2 with issue number, summary and priority." | "no issues were found for vehicle TEST-DAUKEO-2" · "Vehicle TEST-DAUKEO-2 does not exist in the issues dataset with that exact name" · "No issues have been recorded for this vehicle" | Xe có từ 12:39 cùng ngày, Issue #54, #55 tạo 25 phút trước | Khoảng 90 giây |
Kết luận: `Suy` mạnh hơn lần trước về kho trễ: lượt trước, khoảng 15 giờ trước, trả 2 (thật 7), lượt này 10 (thật 12); xe tạo trong ngày chưa có trong kho, AI lại khẳng định "does not exist". **Chưa giải thích được:** #50 có mà #49 không, nên không phải cắt theo thời điểm đơn giản; #51 có Priority High nên cũng không do thiếu mức ưu tiên. Mở lại chat cũ hiện banner "This data may have changed since the last time you had a chat." Ảnh images/ai-analyst-vehicle-not-exist.jpg.
Giữ OQ-13 mở phần nguyên nhân #49, #51.

## Động cơ quyền, liên hệ — Chạy đọc thêm
OQ-9 chốt: mở lại Edit Role Technician, **Fuel Entries chọn None**, không có ô con; ghi chú cũ "chỉ có ô xem" sai. Cancel, không lưu.
Form Contact khi chọn Enable Access (không lưu): "This Contact will be enabled as a User...", Login Information: Email ("An email invitation with instructions to create a password will be sent immediately."), Delay email invitation, Message; Role * mặc định **Fleet Manager**; Notification Profile; Watched Vehicle Groups; Record Sets: Vehicles, Tools, Contacts, Part Locations, Inspection Forms đều mặc định **Full Access**. Điểm yếu: mở người dùng mới mặc định quyền cao nhất, nên Invlogis đảo mặc định.
Kiểm hiệu lực Role, Record Set: **Không chạy được**: cần người dùng thứ hai, không mời người.
Motor Pool: "Vehicle Reservation" có Operator *, Motor Pool *, Reason for Trip, Pick Up *, Drop Off *, Submit Reservation. Motor Pool * lấy từ Settings, đang rỗng; **Không chạy được** vì tạo Motor Pool là Settings bị cấm. Đã Cancel bằng cách rời trang.

## Settings: đọc thêm, đếm trang — Chạy (chỉ đọc, không Save, OQ-10)
**OQ-10 chốt: menu có 67 link = 59 trang cấp tài khoản + 7 trang cá nhân + Log Out.** Cấp tài khoản theo nhóm: tài khoản 4, Notification 2, User Access 4, Intelligence 1, Integrations 5, Developer 1 (Fleetio MCP nhãn New), Data Management 5, Dashboard 1, Vehicles 6, Motor Pool 3, Tools 3 (không mở), Inspections 1, Issues 2, Reminders 3, Service 5, Warranties 1, Parts & Inventory 9, Fuel & Energy 2, Reports 1. Cá nhân: User Profile, Notification Settings, Custom Dashboards, My Saved Views, Login & Password, Appearance & Theme, Manage API Keys.
| Trang | Đọc được thêm | Mức |
|---|---|---|
| Notification Settings (cá nhân) | Email, Mobile App bật tắt chung; 18 nhóm: Collaboration, Vehicles, Tools, Inspections, Issues, Work Orders, Service Entries, Service Reminders, Vehicle Reminders, Contact Reminders, Fuel Entries, Charging Entries, Motor Pool Reservations, Parts, Vendors, Purchase Orders, Expense Entries, Integrations. "You are watching 20 vehicles"; Automatically watch new vehicles, new records, existing reminders; mỗi sự kiện cột Email, Push (Vehicle Status Changed, Vehicle Fault, Vehicle Recall, Voided Fuel Entries...). Email tắt chung vẫn không tắt "essential communications, Saved Reports, Inspection Workflows, Automation Alerts or Notification Profiles" | Xem |
| Notification Profiles | Cột Name, Description, Users Assigned, Users Personalized, Status; "Assign Notification Profiles and manage Watched Vehicle Groups in bulk from the Contacts page." 0 hồ sơ, không tạo | Xem |
| Watched Vehicle Groups | Name, Total Groups, Direct Vehicles, Subgroup Vehicles, Total Vehicles, Direct Watchers, Total Watchers | Xem |
| Security | Thêm phần đã thiếu: Session Timeout, Fleetio Go: Never, 15, 30 phút, 1, 12, 24 giờ, 2 tuần; Fleetio Web: 15 phút đến 2 tuần (không có Never) | Xem |
| Manage API Keys | Cột Label, Token, API Version, Date Added, Status; Account Tokens có Rate Limit 250 requests/minute; "Keys can be regenerated and revoked. Once a key has been revoked it cannot be reactivated." Không tạo khoá. Không ghi token | Xem |
| Webhooks | Tab Webhooks, Webhook Events; cột URL, # Events, Status. Không tạo | Xem |
| External Connections | Cột Name, Type; "upload scheduled reports to your company's FTP, SFTP, and Amazon S3". Không tạo | Xem |
| Integration Links | Cột Label, Record, Status | Xem |
| SAML Connectors | Metadata; cột IdP Entity Id, SSO URL | Xem |
| Fleetio MCP | "Let users on this account connect Fleetio to Claude, Codex or another MCP client. Each connection respects the user's role permissions." | Xem |
| Integrations Directory | Trang `integrations/my-integrations`: Data Connectors 6, Fuel Cards 9, Fuel Management 5, Key Management 1, Operations 1, Telematics 43, Tire Management 1, Tolls & Citations 2 | Xem |
| Sandboxes | Cột Name, URL, Type, Status, Date Created, Last Data Refresh | Xem |
| Export Account Data | 13 loại: Vehicles, Vehicle Assignments, Meter Entries, Issues, Service Entries, Work Orders, Work Order Line Items, Work Order Sub Line Items, Contacts, Vendors, Parts, Purchase Order, Fuel Entries. Không bấm | Xem |
| AI Service Advisor | Issue Prioritization "Prioritizes issues when they're created."; Issue Resolution "Match and resolve issues from completed service."; Fault Monitoring; Service Assessments; Service Writer "Drafts Work Orders from open issues and service reminders."; câu khách tự chịu trách nhiệm | Xem |
| Maintenance Settings | Đọc đủ 5.534 ký tự: phần thiếu là Disable Editing Default Reason, Category codes; Require an Inventory Location; Display Expected Labor Hours; Complaint, Cause, Correction và Require service documentation; Labor, Parts Markup kèm % hoặc giá trị | Xem (FR-repair-035, FR-vehicle-046) |
| Standard Records | 15 loại, mỗi loại đếm Custom Fields, đều 0 | Xem |
| Custom Dashboards | "My Dashboards", "Shared With Me"; Title, Visibility, Last Updated; riêng theo vai, người | Xem |
| Saved Reports | Name, Description, Owner, Visibility, Email Schedule, Created On, Updated On | Xem |
| Reservation Rates, Flat Fees, Motor Pools | Name, Status, Usage; Amount, Vehicle Types; # Groups. Đều rỗng | Xem |
| Work Order Statuses | Open 13, Pending 1, Completed 97 "(2 from 1 archived vehicle)" | Xem |
| Issue Priorities | No Priority 8, Low 4, Medium 12, High 27, Critical 4; cột Alias, Enabled | Xem |
Không bấm: Add Role, Add Record Set, Add API Key, Add Webhook, Add SAML, Add Sandbox, Export Data, Add Notification Profile, Enable module, Upgrade. Không tắt module (FR-004 vẫn Xem).
Dòng Tools (3 trang): không mở theo brief.

## Chưa làm trong lượt 3
Chạy thật automation Service Entry, Fault, PO; OQ-5 vòng lặp chéo; hiệu lực Role, Record Set; Failure Notification Email; Motor Pool đặt xe; Record peek (chưa thấy ở Issues); thao tác hàng loạt trên danh sách (có ô chọn ở tab Open, Closed, chưa bấm); bộ lọc từng báo cáo ngoài Issues; `expense_entries` chưa đọc được do lỗi 500.
Tab trình duyệt: tab New Contact đang kẹt hộp "Leave site?" nên chưa đóng được (form chưa lưu, không có dữ liệu).

## Automation: sửa khi đang bật, phiên bản, Make a Copy, nhóm Any of — Chạy
Các bước đã làm: Bật lại AUTO-01 (96373), sửa nội dung comment thêm " v2", lưu. Xem Version History. More Actions, Make a Copy. Từ bản sao dựng nhóm lồng, lưu thành `TEST-NEN-AUTO-04` (96475), bật. Tạo Issue #54, #55 trên TEST-DAUKEO-2. Tắt 01 và 04.
| Case | Điều kiện | Kết quả thật | Mức |
|---|---|---|---|
| Bật lại bản đã có v.1 | Tắt rồi bật, không sửa | Vẫn v.1, Enabled At đổi: bật lại không sinh phiên bản mới | Chạy |
| Sửa khi đang bật | Đổi nội dung vào form, chưa lưu | Băng cảnh báo "You have unsaved changes on this enabled automation" · "Save to update, or discard to keep the current settings."; nút Save đổi thành menu Save Automation, Discard Unsaved Changes | Chạy |
| Lưu bản sửa | Automation đang bật | Lên v.2, vẫn Enabled, không hỏi xác nhận lại; hiệu lực ngay | Chạy |
| Lượt chạy sau sửa | Issue #55 | Comment mang chữ "v2"; Run Result ghi Version v.2 | Chạy |
| Xem Version History | Mở v.1 | **Lệch: màn ghi "Step Summary v.1" nhưng hiện chữ "comment tu dong v2" của bản mới.** Danh sách có v.2 Current Version và v.1, kèm Created At, Created By. Chỉ thấy trên 1 lần sửa nội dung action, chưa thử với sửa điều kiện | Chạy (ảnh automation-version-v1-lech.jpg) |
| Make a Copy | Bản đang bật | Mở `automations/new?copy_from=96373`, chưa lưu gì, tên thêm " (copy)", Disabled. Rời trang không để lại bản rác. Bản đã lưu: Current Version "—" cho tới khi bật lần đầu | Chạy |
| Menu More Actions khi chưa Archive | | Make a Copy, Archive, View Record History. Delete chỉ hiện ở bản Archived (lượt trước) | Chạy |
| Nhóm lồng | All of [Summary contains TEST-NEN, Any of (contains NHOMA, contains NHOMB)] | Hiện đúng "And" và "Or" ở khung trái | Chạy |
| Khớp nhóm | #54 "TEST-NEN-D1 NHOMA" | AUTO-04 và AUTO-01 cùng chạy: 2 comment giống hệt nhau (không tick Prevent duplicate comments) | Chạy |
| Không khớp nhóm | #55 "TEST-NEN-D2 khong khop nhom" | Chỉ AUTO-01 chạy, 1 comment | Chạy |
| Trường thứ 2 thêm vào nhóm | Thêm điều kiện cùng trường | Toán tử mặc định "does not contain", phải đổi tay; Enter trong ô giá trị đóng luôn panel như Apply | Chạy |
Bất ngờ: Run Result của lượt thêm comment vẫn "Records: No records changed". #54 Priority "No Priority", #55 lúc mới tạo hiện "Prioritizing": AI xếp mức chạy nền, kết quả khác nhau giữa 2 Issue.
Trả lời câu hỏi mở: OQ-7 phần v.2 và Make a Copy.
Dữ liệu TEST đã tạo: automation 96475 `TEST-NEN-AUTO-04` (đã tắt); 96373 lên v.2 (đã tắt); Issue #54, #55 trên TEST-DAUKEO-2.

## Mẫu Send Email When A Work Order Total Exceeds Amount — Chạy (mở mẫu, không lưu, OQ-14)
Đường dẫn `automations/new?template=send_email_from_work_order`. Trigger Work Order Created or Updated. Điều kiện Work Order Total Cost ≥ 100.000 ₫. Hành động Send Email: Recipient(s) tự điền người đang đăng nhập; Subject "Action Needed: Review high WO cost {{ work_order.number }}"; nội dung "Work Order {{ work_order.number }} for {{ asset.name }} was flagged for high cost (>$1,000.00). Please review the planned work below: {{ work_order.service_tasks }}".
**Bất ngờ:** mẫu đổi ngưỡng theo tiền tệ khách (100.000 ₫) nhưng câu email vẫn viết cứng ">$1,000.00": sửa ngưỡng không sửa câu. Invlogis: chữ trong mẫu phải lấy từ biến.
Gửi Email thật: Không chạy được, brief cấm hành động gửi email. Rời trang mẫu bằng Cancel làm tab kẹt hộp "Leave site?", phải đóng tab.

## Automation trigger Vehicle, Update Vehicle Status — Chạy
Các bước đã làm: Tạo `TEST-NEN-AUTO-05` (96476): Vehicle Updated, Vehicle is any of TEST-DAUKEO-2, Update Vehicle Status to Inactive. Bật. Sửa Color xe thành TEST, lưu. Rồi người dùng đổi Status về Active. Xem Status Updates. Tắt.
Kết quả thấy được:
- Trigger của Vehicle chỉ có Created, Updated, Created or Updated; khác Issue không có Deleted.
- Điều kiện Vehicle 71 mục, không có trường "Name", phải dùng "Vehicle is any of". Có trường cảm biến: Fuel Level, Engine Oil Pressure, Engine Coolant Temp, Battery Voltage, Tire Pressure, Ignition Status, Installed Tires Count, Axle Configuration, Incomplete Work Orders Count. Đủ để dựng luật theo dữ liệu GPS.
- Hành động trên Vehicle: Update Field, Add Comment, Send Email. Update Field chỉ có 5 trường: Status, Type, Group, Labels, Axle Configuration.
- Sửa trường không liên quan (Color) đã kích hoạt: trigger Updated chạy trên MỌI thay đổi, không chọn được "khi trường X đổi".
| Case | Điều kiện | Kết quả thật | Ảnh |
|---|---|---|---|
| Đổi trạng thái tự động | Sửa Color | Status Active sang Inactive trong vài giây; Status Updates ghi "Fleetio Automation updated status from Active to Inactive" | automation-vehicle-status-flip.jpg |
| Người sửa ngược automation | Người đổi về Active khi automation bật | Lưu được, không cảnh báo; 1 giây sau automation đổi lại Inactive. Màn người dùng không báo gì | automation-vehicle-status-flip.jpg |
| Tự kích hoạt chính mình | Update Vehicle Status gây Vehicle Updated | Total Runs 2 cho đúng 2 lần người sửa: lượt do automation đổi xe không sinh lượt mới (khác AUTO-02 trên Issue đã sinh 2 lượt) | — |
| Kết quả chạy | Lượt thật đã đổi xe | Run Result vẫn "Records: No records changed" dù đã đổi Status: nhãn này không đáng tin | — |
| Log đầy đủ | View Full Log | JSON từng bước: Workflow, Trigger, ActionSet (có bước NOOP "Automation Trigger has no action set"), ConditionSet, ScoopMatcher, Database; có runtime từng bước | — |
Trả lời câu hỏi mở: OQ-7 phần trigger Vehicle, Update Vehicle Status. Thông tin cho FR-fleetio-vehicle-045.
Giải pháp đáng học, điểm yếu: lịch sử trạng thái ghi rõ nguồn "Fleetio Automation" (tốt hơn "Triggered By" ghi người). Điểm yếu: người sửa bị lật lại không có thông báo; trigger không lọc theo trường đổi, dễ chạy thừa. Với đầu kéo: nên có "chỉ khi Status đổi" và báo khi luật ghi đè thao tác tay.
Dữ liệu TEST đã tạo: automation 96476 `TEST-NEN-AUTO-05` (đã tắt); TEST-DAUKEO-2 Color = TEST, Status trả về Active sau khi đo.

# Lượt 4 (03/11)

Tiền tố `TEST-NEN`. Vẫn không gửi email, không đổi Cài đặt, không mời người. Mọi automation tắt lại sau khi đo.

## Automation Service Entry — Chạy (FR-012, FR-013)
Các bước đã làm: Tạo `TEST-NEN-AUTO-07 SE tao doi Priority` (96542): Service Entry Created; Vehicle is any of TEST-KHO-01. Thử Update Field trước, rồi đổi Add Comment. Bật, tạo entry #57903356 trên TEST-KHO-01 (5.310 km, Brake Inspection, Reference TEST-NEN-SE-1). Tắt.
Kết quả thấy được:
| Case | Điều kiện | Kết quả thật |
|---|---|---|
| Kiểu sự kiện | Mở danh sách | Created, Updated, Created or Updated, Deleted |
| Bản ghi của hành động | Trigger Service Entry | Chọn được Service Entry hoặc Vehicle |
| Hành động trên Service Entry | | Update Field, Add Comment, Send Email. Update Field chỉ có Repair Priority Class, Labels |
| Popular Conditions | | Service Entry Created By, Service Entry Completion Date, Vehicle, Vehicle Status |
| **Update Field Repair Priority Class = Emergency** | Save Automation | **Từ chối**: "Automation could not be created. Please resolve any errors try again.", khối Actions "action is missing" · "is invalid", nút "Fix Errors". Giao diện cho chọn và Apply bình thường, chỉ báo lúc lưu. Chỉ thử 1 giá trị, lý do hãng không nêu |
| Add Comment | Tạo entry đúng xe | Comment hiện ngay, tác giả "Fleetio Automation": "TEST-NEN comment tu dong tren SE" |
| Khoanh vùng theo xe | Agent khác đang tạo entry trên TEST-DAUKEO-2 cùng lúc | Total Runs 1, Successful 1: entry xe khác không tính lượt |
| Bật | Toggle | Hộp "Do you want to enable this automation?"; v.1 sinh lúc bật đầu tiên, Activity ghi "Enabled changed from false to true", "Version changed from [empty] to 1" |
Bất ngờ: ô Completion Date của form entry hiện chữ mờ ngày hiện tại nhưng là placeholder, bấm lưu báo "can't be blank", phải gõ. Toàn bộ chọn trên form không báo.
Dữ liệu TEST đã tạo: automation 96542 (đã tắt); Service Entry #57903356.

## Automation Purchase Order — Chạy (FR-012, FR-013)
Các bước đã làm: Tạo `TEST-NEN-AUTO-08 PO sua tu duyet` (96543): Purchase Order Updated; Vendor is any of TEST-NCC-01. Thử Update Field Status = Approved, rồi đổi Add Comment. Bật, lưu lại PO #5 không đổi gì, rồi bấm Approve.
| Case | Điều kiện | Kết quả thật |
|---|---|---|
| Kiểu sự kiện | | Created, Updated, Created or Updated. **Không có Deleted** |
| Bản ghi của hành động | | Chỉ Purchase Order |
| Hành động | | Update Field, Add Comment, Send Email. Update Field: Labels, Status |
| Giá trị Status của Update Field | | Chỉ "Rejected", "Approved" |
| Popular Conditions | | Purchase Order Parts, Vendor, Part Locations, Labels, Status |
| Tự duyệt không có điều kiện | Chọn Approved | Cảnh báo cam ngay trong panel: "This Trigger and Action set requires a specific Condition. To ensure a successful automation, add a Condition on Purchase Order Status for Pending Approval." |
| Vẫn lưu | Save | Chặn: "Purchase Order Status "Pending Approval" is required", có nút "Resolve error" |
| Lưu lại đơn không đổi gì | Edit #5, Save as Draft | **0 lượt**: không đổi gì thì không tính Updated |
| Bấm Approve | Draft sang Approved | 1 lượt, comment "Fleetio Automation" trên #5. Comment không kích lại automation |
Trả lời: duyệt, từ chối đơn tự động là có thật, nhưng hãng buộc điều kiện Pending Approval: tự động chỉ xử lý đơn đã nộp duyệt, không bỏ qua bước nộp được. Chạy thật nhánh này: Chặn, tài khoản có quyền duyệt không tạo được đơn Pending, cần người thứ hai.
Dữ liệu TEST đã tạo: automation 96543 (đang Disabled); comment trên PO #5.

## Archive và Restore automation — Chạy (FR-033)
Các bước đã làm: AUTO-08 đang Enabled, More Actions, Archive, xác nhận. Sửa PO #5 số 7 thành 6, Save as Draft trong lúc Archived. Restore.
| Bước | Kết quả thật |
|---|---|
| Menu khi chưa Archive | "Make a Copy", "Archive", "View Record History" (không có Delete) |
| Xác nhận | "Confirm Automation Archive": "This will disable the automation and it will stop working immediately. It can be restored at any time." |
| Sau Archive | Băng "This record is archived." · "Archived records are read-only and cannot be updated."; nút "Restore", "Delete". Mất toggle, mất Edit, mất menu "...". Status Disabled, có Disabled At |
| Đang Archived mà bản ghi khớp đổi | PO #5 đổi số: Total Runs vẫn 1, không comment mới |
| Restore | Một cú bấm, không hộp xác nhận: "Record successfully restored!". Về **Disabled**, có toggle, Edit; không tự bật lại dù trước đó Enabled. Giữ v.1, giữ Run History 1, giữ Disabled At. Activity ghi "Archived At changed from ..." |
Không bấm Delete (không xoá bản ghi).

## Automation Fault — Một phần (FR-013)
Các bước đã làm: Tạo `TEST-NEN-AUTO-09 Fault tao Issue` (96544): Fault Created, không điều kiện, Create Record Issue. Lưu Disabled, không bật.
Kết quả thấy được: Kiểu sự kiện của Fault **chỉ có Created**. Popular Conditions: Fault Code, Fault Status. Bản ghi của hành động: Issue, Fault, Vehicle. Trên Issue chỉ có "Create Record", 2 ô Assigned to, Priority; không có ô Summary. Trên Fault: Update Field, Send Email; Update Field chỉ có Status; giá trị chỉ "Ignored". Lưu được: "Automation ... was successfully created", Step Summary "Fault is created" · "Create Issue".
Chưa chạy lượt thật: Chặn: Fault chỉ sinh từ thiết bị telematics, xe TEST không có thiết bị, không có cách tạo tay; Sample không đụng; không kết nối tích hợp.
Dữ liệu TEST đã tạo: automation 96544 (Disabled, chưa bật lần nào).

## Giới hạn theo gói: đếm khi đang bật — Chạy phần đọc (FR-023)
Các bước đã làm: Bật AUTO-07, mở Settings › General › Account Usage (chỉ đọc), tắt lại.
Kết quả thấy được: "Documents 82.7 kB of 250.0 GB", "Roles 4 of 30", "Vehicles 5 of 5", "Tools 0 of 25", **"Automations 1 of 75"**, "Custom Records 0 of 25". Lúc này tài khoản lưu 10 automation, 1 đang bật. Xác nhận: **hạn mức Automations chỉ đếm bản đang bật** (lượt 3 mới là suy).
Chặn: hết hạn mức Automations thì sao: cần 75 bản bật, không làm. Xe đã thấy chặn ở 5 of 5.

## Bộ lọc báo cáo ngoài Issues — Chạy (FR-019, chỉ đọc, 1 lần lọc thật)
Các bước đã làm: Mở nền 48 báo cáo, bấm Filters, đọc nhãn, không Apply. Lọc thật `purchase_orders` theo Vendor TEST-NCC-01, không Save, không Share.
Có **3 kiểu bộ lọc**:
| Kiểu | Hình | Báo cáo |
|---|---|---|
| A. Panel ô cố định, nút Search | Ô dựng sẵn, gồm khối Vehicle 11 ô | Đa số báo cáo mới |
| B. Filter builder | "No filters applied.", Add Filter, Popular Filters (như danh sách thường) | contacts, motor_pool_reservations_summary, part_warranty_opportunities, service_reminders, tire_activities, tool_service_entries_summary, vehicle_warranty_opportunities, vehicles, work_orders |
| C. Thanh lọc ngay trên báo cáo, Add Filter, Apply | Nút "1 Filters", mỗi chiều 1 nút | fuel_summary (Fuel Entry Date), inspections_summary (Inspection Submitted, Failed Items, Form, User), vehicles_utilization_summary (Meter Type, Meter Entry Meter Date; "2 Filters"), vehicles_total_cost_trend (Time Frame) |
Không lọc được: job_assignments_summary_by_job (chỉ có Save). Lỗi: `expense_entries` vẫn Error 500 lần 3, lượt này mở lại vẫn hỏng.
Ô riêng của từng báo cáo kiểu A ([XE] = khối 11 ô Vehicle Types, Groups, Status, Year, Make, Model, Trim, Current Operator, VIN/SN, License Plate, Registration State/Province):
| Báo cáo | Ô riêng |
|---|---|
| contact_renewal_reminders | Status, Renewal Type, Time Frame, Contacts, Contact Group |
| faults/summary | Fault Code, Fault Details, Critical Codes Only, Time Frame, Total Occurrences (Equals, Less than, Greater than...), [XE] |
| fuel_entries, fuel_entries/by_location | Time Frame, Vendors, Fuel Type, Reference, Fuel Alerts, [XE], Void Status, đơn vị Miles, Kilometers, Gallons (US), Gallons (UK), Liters |
| inspections | Time Frame, Inspection Form, Duration (minutes), Users, User Groups, User Roles, [XE] |
| inspections/failures | Inspection Form, Inspection Items, Stage, Time Frame, Submitted By User, [XE] |
| inspections/schedules | Due Date, Last Inspected, Inspection Form, Schedule Type, Schedule Status, [XE] |
| inventory_journal_entries | Time Frame, Previous quantity, Adjustment quantity, Current quantity, Adjustment Type, Part Locations, Part, Part Number, Part Description, Part Category, Part Manufacturer, Part Vendors, [XE] |
| part_locations | Part Location, Inventory status, Current Quantity, Work Orders Current Quantity, Purchase Order Current Quantity, Reorder Point, Part, Part Number, Part Description, Part Category, Part Manufacturer, Part Vendors, Aisle, Row, Bin, Include archived parts |
| parts/by_vehicle | Work Order Status, Completion Date, Quantity Subtotal, Subotal amount (nguyên văn sai chính tả), [XE], các ô Part, Part Locations |
| purchase_orders | Description, Labels, Part Locations, Status, Vendor, người + ngày từng bước (Created, Approved, Purchase, Received In Full, Closed), Total, các ô Part |
| repair_priority_classes/summary | Repair Priority Class, Service Tasks, Duration (hours), Time Frame, Vendors, [XE] |
| service_entries | Repair Priority Class, Created by, Service Tasks, Reason for Repair, Category, System, Assembly, Component, External ID, Time Frame, Duration (hours), Vendors, Minority/Women Owned, Labels, Reference, Work Order Number, Generated by work order, [XE] |
| service_entries/summary | Repair Priority Class, Service Tasks, Duration (hours), Time Frame, Vendors, khối Asset thay Vehicle |
| service_reminder_compliance | Completion Date, Became Due Date, On-Time Status, Service Tasks, [XE] |
| service_tasks/summary | Service Entry Status, Time Frame, Repair Priority Class, Service Tasks, Exclude archived tasks, Default Category, Default System, Labels, Vendors, Number of Uses, Service Task Part Cost, Service Task Labor Cost, Total Cost, [XE] |
| vehicle_assignments | Time Frame, Show Assignments from Past, Current, Future; Operator, Operator Group, khối xe, Vehicle Loan/Lease Vendors, Vehicle Ownership |
| vehicle_assignments/summary | Time Frame, Assignments Count, % Assigned, % Assigned Range, Operator, Operator Group, khối Asset |
| vehicle_group_changes | Time Frame, From Group, To Group, [XE], Loan/Lease Vendors, Ownership |
| vehicle_renewal_reminders | Status, Renewal Type, Time Frame, khối xe, Loan/Lease Vendors, Ownership |
| vehicle_status_changes | Time Frame, From status, To status, [XE], Loan/Lease Vendors, Ownership |
| vehicle_status_summaries | Time Frame, # Changes, Duration in Status, [XE] |
| vehicles/cost_comparison_by_year_in_service | Expense Type, Meter Type, [XE], Current Meter |
| vehicles/cpm_trend | Time Frame, Expense Type, [XE], Current Meter |
| vehicles/details | [XE], Loan/Lease Vendors, Purchase Vendors, Ownership, Current Meter |
| vehicles/expense_summary | Time Frame, Include Future Expenses, Only Include TCO Expenses, Expense Type, Vendor, khối Asset |
| vehicles/operating_cost_summary | Time Frame, Expense Type, khối Asset, Current Meter |
| vehicles_without_service | Time Frame, Service Task, [XE] |
| vmrs_system_assembly_components/summary | Service Entry Status, Time Frame, Category, System, Reason for Repair, Repair Priority Class, Service Tasks, Labels, Vendors, [XE] |
| work_order_status_changes/summary | Time Frame |
| work_orders/by_vehicle | Status, Repair Priority Class, Vendor, Service Tasks, Labels, Created by, Assigned to, Issue Date, Scheduled Start Date, Start Date, Completion Date, Duration (hours), Parts Subtotal, Parts Markup, Labor Subtotal, Labor Markup, Subtotal, Total, khối xe |
| work_orders/labor_time_entries | Contacts, Started at, Ended at |
| work_orders/technician_summary | Issue Date, Labor Timeframe, Status, Service Task, Technician, Scheduled Start Date, Start Date, Completion Date, Labels, khối Asset |
Popular Filters kiểu B: work_orders: Vehicle, Vehicle Group, Work Order Service Tasks, Watcher, Assignee Group, Work Order Labels, Work Order Repair Priority Class, Vehicle Current Job. vehicles: Vehicle, Vehicle Group, Vehicle Status, Vehicle Type, Vehicle Current Job. service_reminders: Service Task, Service Reminder Service Programs, Service Reminder Manually Set Next Due, Vehicle, Vehicle Group. contacts: Role, Unconfirmed Email, Classification, Group, Full Name, Email, City, State/Province/Region, Currently Assigned Vehicle, Currently Assigned Tools. part_warranty_opportunities: Replacement Work Order Completed At, Vehicle, Vehicle Group, Vehicle Current Job, Part Manufacturer Part Number, Part Manufacturer, Part Category, Part Vendor. vehicle_warranty_opportunities: Vehicle Warranty Name, Work Order Completed At, Vehicle Group, Vehicle Current Job, Service Task. motor_pool_reservations_summary: Vehicle Reservation Motor Pool, Vehicle Reservation Operator, Status, Vehicle. tool_service_entries_summary: Tool Brand, Tool Model, Tool, Tool Status, Tool Group, Tool Current Assignee. tire_activities: không có Popular Filters.
Lọc thật: `purchase_orders`, Vendor TEST-NCC-01, Search: "1 filter applied", "Clear all", 2 dòng #1 và #5. Đường dẫn thêm `q[vendor_id_in_s]`. **Total Amount ₫3,574,040 gồm cả đơn Draft #5 (₫574,040)**: báo cáo cộng đơn nháp. Biểu đồ "Total by Vendor" trục chỉ 20k trong khi tổng 3,5 triệu: lệch thang ở VND.
Bất ngờ: tên ô nói "Vehicle" hoặc "Asset" khác nhau giữa báo cáo cùng nội dung. Ô "Subotal amount" sai chính tả.
Không làm: Share (lượt 3 đã biết Share sinh link công khai ngay), Save.

## Không chạy được (lượt 4)
- FR-012 Send Email: gửi email.
- FR-018 hồ sơ thông báo, FR-038 Enable Access: tạo hồ sơ là đổi Settings; Enable Access có thể gửi email mời, không lưu.
- FR-023 chặn khi hết hạn mức Automations: cần 75 bản bật.

## Giải pháp đáng học, điểm yếu (lượt 4)
- Đáng học: hãng buộc điều kiện Pending Approval khi tự duyệt đơn, chặn ngay lúc lưu kèm nút "Resolve error". Rule tự động có hậu quả tiền nên có ràng buộc cứng như vậy.
- Đáng học: hạn mức chỉ đếm automation đang bật, Archive tắt ngay, Restore không tự bật.
- Điểm yếu: Update Field của Service Entry vẫn cho chọn và Apply, chỉ báo "action is missing" lúc lưu, câu lỗi không chỉ cách sửa.
- Điểm yếu: 3 kiểu bộ lọc, người dùng phải học lại từng báo cáo.
- Điểm yếu: báo cáo đơn mua cộng cả Draft vào Total Amount, không phân biệt mặc định.

## Dữ liệu TEST lượt 4 (nhóm nền tảng)
Automation 96542 AUTO-07, 96543 AUTO-08, 96544 AUTO-09, đều Disabled. Service Entry #57903356 trên TEST-KHO-01. Comment tự động trên #57903356 và PO #5.

# Lượt 5 (03/11)

Giá trị Cài đặt trước khi đổi: Motor Pools rỗng, Reservation Rates rỗng, Flat Fees rỗng. TEST-DAUKEO-2: Active, No Group, Unassigned, 2.500 km, 30 hr, "There are no linked Assets for this Vehicle", Lệnh #111 đang Open.

## Motor Pool: tạo nhóm xe dùng chung — Chạy; đặt xe — Không chạy được (không có Operator hợp lệ)
Các bước đã làm: Settings › Motor Pools › Add; tạo TEST-NEN-POOL-01; Add Vehicle Reservation; bấm Submit khi thiếu Operator để đọc kiểm tra; huỷ.

Form "Add Motor Pool": Name *, Groups *, Vehicle Types *, Vehicle Statuses * (mặc định Active), "Automatically calculate charges", 'Require "Reason for Trip" field', "Auto Approvals" kèm "How it works". Bật Auto Approvals: Time zone * ("Used only for auto-approval window checks. It does not affect reservation times."), Days *, Start Time *, End Time *, Full day, Add Window. Đã xem, không lưu.

| Case | Điều kiện | Kết quả thật | Ảnh |
|---|---|---|---|
| Tạo pool | Group 11/05/2026, Semi Truck, Active, bắt buộc Reason | "Motor Pool was successfully created"; danh sách Name, # Groups | motor-pool-add |
| Bắt buộc lý do | Tick ô | Cảnh báo "This field will be required on all reservations. Users with access will be unable to create new or save edits to existing reservations until a valid value is entered for this field." | motor-pool-add |
| Form đặt xe trước khi chọn pool | | Operator *, Motor Pool *, Reason for Trip, Pick Up *, Drop Off * | |
| Chọn pool | | Hiện thêm Vehicle Types * chỉ gồm loại của pool (Semi Truck); Reason for Trip có dấu *. **Người đặt chọn loại xe, không chọn xe cụ thể** | reservation-validation |
| Operator | Gõ "TEST" | "No results for 'TEST'"; xoá tìm kiếm: "No options". Tooltip: "...contacts with login access and operator classification are shown." | |
| Đối chiếu Contacts | | TEST-LAI-XE, TEST-LAI-XE-02, TEST-NHAC-LX có Operator nhưng "No Access"; Bảo Tín có đăng nhập nhưng không có Classification. **Không ai thoả cả 2 điều kiện** | |
| Submit thiếu dữ liệu | Không Operator, Reason, ngày | "must exist", "is required for this motor pool", "can't be blank" 2 lần, toast "Failed to create Reservation". Không tạo bản ghi | reservation-validation |
| Reservation Rates | Chỉ xem | "Reservation Rates are configurable pricing tables used to automatically calculate reservation costs."; Add Rate Table; cột Name, Status, Usage, Last Updated | |
| Flat Fees | Chỉ xem | "Preset fees that can be optionally added to individual reservations."; Add Flat Fee; cột Name, Status, Amount, Vehicle Types | |

Không chạy được, vì sao: muốn có Operator phải (a) tick Operator trên contact Bảo Tín: bản ghi thật, không phải TEST, ngoài phạm vi được phép; hoặc (b) cho contact TEST đăng nhập: mời người, bị cấm. Đã dừng, báo về để user quyết. Hệ quả chưa chạy: duyệt, gán xe cụ thể, trạng thái đặt xe, xe trong pool (chưa đổi Group của TEST-DAUKEO-2), tính phí, Auto Approvals.
Trả lời câu hỏi mở nào: OQ-12 nhóm Nền tảng, OQ-11 nhóm Xe: một phần, chỉ phần cấu hình pool và điều kiện Operator.
Màn mới: motor-pool-add, reservation-validation — ảnh cùng tên trong images/.
Dữ liệu TEST đã tạo: Motor Pool TEST-NEN-POOL-01 (dùng nhóm "11/05/2026" có sẵn, không phải Sample, không thấy xe TEST nào trong nhóm; tên nhóm giống ngày gõ nhầm, chưa rõ ai tạo). Không xoá được theo ràng buộc.

## Archive xe có đặt chỗ đang hiệu lực — Không chạy (FR-vehicle-021)
Không bấm Archive trên TEST-DAUKEO-2 vì không tạo được đặt chỗ. Bấm lúc này không đo được gì: xe không có đặt chỗ, và Lệnh #111 đang Open sẽ tự làm Archive bị từ chối; lần từ chối đó lại ngắt liên kết (lượt 3). Khi chạy lại phải đóng #111 trước, nếu không không tách được nguyên nhân. Đọc lại cuối lượt: Active, No Group, Unassigned, 2.500 km, 30 hr: không đổi.

Giải pháp đáng học, điểm yếu:
- Đáng học: đặt theo loại xe, không theo xe cụ thể; hợp với điều xe đầu kéo khi người đặt chỉ cần "1 đầu kéo", điều độ mới gán xe.
- Đáng học: tự duyệt theo cửa sổ thời gian, có múi giờ riêng cho việc duyệt.
- Điểm yếu: người lái không đăng nhập không đặt được, cũng không được đặt hộ. Lái xe logistics thường không có tài khoản nên điều độ không đặt thay được.
- Điểm yếu: form Add Motor Pool bắt buộc Groups, nên tài khoản không dùng nhóm xe không tạo được pool.

# Lượt 6 (03/11)

User duyệt tick Operator trên Bảo Tín, cho TEST-DAUKEO-2 vào nhóm của pool. Trước khi đổi: Bảo Tín Classifications trống ("Contact must have operator classification to be assigned to vehicles" ở thẻ Current Vehicle Assignments); TEST-DAUKEO-2 Active, No Group, Unassigned, 2.500 km, 30 hr.

## Đặt xe: tạo, duyệt, gán xe — Chạy
Các bước đã làm: tick Operator (toast "Contact was successfully updated"; thẻ phân công đổi thành "No currently active vehicle assignments", hiện thêm tab Vehicle Assignments, Tool Assignments); xe vào nhóm 11/05/2026 ("Vehicle was successfully updated"); Add Vehicle Reservation; Approve.

| Case | Điều kiện | Kết quả thật | Ảnh |
|---|---|---|---|
| Ô Operator sau khi tick | Chủ tài khoản có đăng nhập + Operator | Danh sách có đúng 1 dòng Bảo Tín, nhãn "Account Owner", "Operator". Xác nhận điều kiện kép của tooltip | |
| Tạo đặt xe | Pool, Semi Truck, Reason, 11/10 đến 11/12 | "Reservation was created successfully"; số #1; "Requested"; Vehicle trống; Line Items trống | reservation-detail-requested |
| Menu khi Requested | | Approve, Deny, Cancel, View Record History; thêm nút Edit | |
| Form Edit khi Requested | | Status chỉ đọc; sửa được Operator, Pool, Vehicle Types, Reason, Pick Up, Drop Off | |
| Hộp Approve | | "Approve Reservation #1": Operator, Pool khoá, Vehicle Types chỉ đọc, **Vehicle * bắt buộc**, sửa được Reason, ngày | reservation-approve-dialog |
| Ô Vehicle khi duyệt | Nhóm chỉ có 1 xe Semi Truck | Tiêu đề "REQUESTED TYPES", chỉ TEST-DAUKEO-2; không có xe Sample cùng loại khác nhóm. Lọc theo nhóm của pool là thật | |
| Duyệt | Chọn xe | "Reservation was approved successfully"; "Approved"; Vehicle = TEST-DAUKEO-2; chưa đổi Start Meter, End Meter | reservation-detail-approved |
| Menu khi Approved | | Check Out, Email Invoice, Print, Cancel, View Record History (không bấm Email Invoice, Print) | |
Không thấy hộp hay câu nào báo gửi email khi tạo, duyệt. Chuông thông báo của chủ tài khoản vẫn số 5 ngay sau duyệt.

## Bảng giá, phí cố định, tự duyệt — Chạy
Các bước đã làm: tạo TEST-NEN-RATE-01 (Semi Truck: giờ 10.000, ngày 100.000, tuần 500.000, km 1.000), TEST-FEE-VE-SINH (50.000, mọi loại xe); pool bật tính phí + Auto Approvals, cửa sổ Thứ Hai 8:00am đến 5:00pm.

Câu chữ form: Add Rate Table: Name, Enabled, dòng Rates (Name, Vehicle Types, Hourly, Daily, Weekly, Monthly, Mileage). Bánh răng: "Hourly threshold" 4, 8, 12, 24 ("Max hours to charge each day before rounding up."), "Once reservation exceeds threshold, ignore hourly billing for entire reservation.". Rate duration: "Hourly: 60-minute period, for reservations under the table's hourly threshold", "Daily: 24-hour period", "Weekly: 7-day period", "Monthly: 30-day period". "Reservations are priced from the largest defined duration to the smallest. Undefined durations are skipped. Any remaining time that does not fit evenly into a duration is rounded up to the next defined duration." Form pool khi bật tính phí: chọn bảng giá, "If greater than N days" + bảng giá thứ hai, "Manage Rates". Add Flat Fee: Name, Enabled, Amount ("Leave empty to allow the amount to be entered on the reservation."), Vehicle Types ("Leave empty to allow this fee on any vehicle type.").
Auto Approvals, How it works: "the reservation pickup time falls within any qualifying window", "the reservation drop-off time falls within any qualifying window", "the request does not overlap with existing assignments on vehicle"; "If multiple vehicles qualify, selection is based on: order of requested vehicle types, lowest current meter reading".

| Case | Điều kiện | Kết quả thật | Ảnh |
|---|---|---|---|
| Bật tính phí sau khi đã có đặt xe | #1 đã Approved trước đó | Line Items của #1 vẫn trống; **không tính lại** | |
| Trong cửa sổ, múi giờ cửa sổ Central | #2, Thứ Hai 16/11 9:00am đến 4:00pm, cửa sổ múi giờ tài khoản | Vẫn **"Requested"**, Vehicle trống, không phí, không báo lý do | |
| Trong cửa sổ, đổi đúng 1 biến: múi giờ cửa sổ sang Hanoi | #3, Thứ Hai 23/11 9:00am đến 4:00pm | **Tự "Approved"**, tự gán TEST-DAUKEO-2, toast vẫn "Reservation was created successfully" không nói đã tự duyệt | reservation-auto-approved-charges |
| Tính phí ngắn hơn 1 ngày | #3, 7 giờ | Hours 10.000 ₫ / hour × 7 = 70.000 ₫; Meter 1.000 ₫ / km × 0 = 0; Total 70.000 ₫ | reservation-auto-approved-charges |
| Sửa đặt xe đã duyệt | Form Edit #3 thêm: Vehicle, Start Meter và End Meter kèm Void, "Last updated: 2,500 km (Today)", khối Charges "Calculated from:", "View Line Items", "Add Flat Fee" (Custom hoặc phí có sẵn) | |
| Tính phí nhiều ngày | Đổi Drop Off 25/11 12:00pm (2 ngày 3 giờ) | Báo ngay "Charges have been recalculated based on updates to the reservation. Saving will replace the previously saved values."; Days 2 × 100.000 + Hours 3 × 10.000 = 230.000 ₫ | reservation-charges-flat-fee |
| Phí cố định | Chọn TEST-FEE-VE-SINH | Dòng 50.000 ₫, sửa được số tiền ngay trên đặt xe; Total 280.000 ₫; "Reservation was edited successfully" | reservation-charges-flat-fee |
| Trùng lịch, trong cửa sổ | #4, 23/11 10:00am đến 3:00pm, trùng #3 trên xe duy nhất | Không tự duyệt, "Requested" | reservation-vehicle-overlap |
| Duyệt tay khi trùng | Hộp Approve #4 | Xe xám, không chọn được, icon lịch, tooltip "Requested dates overlap an existing assignment from 11/23/2026 9:00am to 11/25/2026 12:00pm" | reservation-vehicle-overlap |
| Trả xe ngoài cửa sổ | #5, Thứ Hai 30/11 9:00am đến Thứ Ba 1/12 9:00am | Không tự duyệt, "Requested" | |
| Deny | #4 | Hộp "Denied Reason *" bắt buộc; "Denied"; hiện Denied Reason; mất nút Edit | |
| Cancel khi Requested | #5 | Hộp "Canceled Reason *" bắt buộc; "Reservation was canceled successfully"; "Canceled"; mất Edit; menu chỉ còn View Record History | |
| Duyệt sinh phân công | #1, #3 Approved | Trang liên hệ có 2 dòng Vehicle Assignments gắn nhãn "Future". **Đặt xe là phân công thật**, nên lịch trùng được chặn từ đây | |
| Check Out sớm hơn ngày hẹn | #3 hẹn 23/11, Check Out 3/11 Start Meter 2510 | Hộp nói "Checking out confirms the operator has picked up the vehicle. The reservation moves to Checked Out, from where it can be returned or completed once the trip ends."; "Reservation was checked out successfully"; "Checked Out At 11/03/2026 9:01pm"; Pick Up vẫn 23/11. Phân công vẫn nhãn "Future", có Start Meter 2.510 | |
| LỖI: số đồng hồ đề ngày tương lai | Sau Check Out đó | "Last updated: 2,510 km (in 19 days)": số đồng hồ lấy ngày Pick Up hẹn, không phải giờ lấy xe thật | |
| Return khi ngày hẹn còn ở tương lai | #3 Checked Out, có End Meter 2560, rồi bỏ trống End Meter | Cả 3 lần "Failed to return Reservation", PATCH `/motor_pool_reservations/3/status` 422, **không nêu lý do**. Lấy xe sớm mà không trả được | |
| Sửa ngày về 8:00am cùng ngày | Edit #3 | "must be less than 100 or marked as void" ở Start Meter, "Failed to edit Reservation". Con số 100 trong câu không rõ nghĩa. Đổi Pick Up 8:45pm, sau số đồng hồ của Lệnh #111 lúc 8:30pm thì qua | |
| Làm tròn giờ | 15 phút | 1 hour, 10.000 ₫: làm tròn lên | |
| Quá giờ hẹn | Drop Off đã qua, menu Checked Out | Mục đầu đổi thành Complete (hộp "Complete Reservation #3"), bước thẳng không qua Returned ở ca này. Đây là chênh lệch so với hộp Return "From Returned, the reservation can only be moved to Completed." | |
| Complete, phí km | End Meter 2560 | Charges báo tính lại trước khi lưu; "Reservation was completed successfully"; Hours 1 × 10.000, Meter 50 km × 1.000 = 50.000, phí 50.000, Total 110.000 ₫. Drop Off tự đổi thành 9:04pm, thêm "Returned At 11/03/2026 9:04pm", tiền giờ không tính lại. Completed vẫn còn nút Edit | reservation-completed |

Suy luận, không phải câu chữ hãng: ô giờ trong form đặt xe nhận theo múi giờ trình duyệt (Asia/Saigon, mặc định hiện đúng giờ máy), không theo múi giờ người dùng Fleetio (America/Chicago). 9:00am Saigon rơi ngoài Thứ Hai Central nên #2 không tự duyệt.
Suy luận, chưa kiểm: Return 422 do ngày Pick Up còn ở tương lai. Sau khi dời Pick Up, Drop Off về quá khứ, mục đầu menu là Complete, nên KHÔNG thử lại Return; lý do 422 chưa xác nhận và trạng thái Returned chưa từng đạt được.

Sửa ý ở bảng trên: "tiền giờ không tính lại" không chứng minh được vì 15 phút và 19 phút đều làm tròn 1 giờ. Chỉ thấy: Drop Off đổi 9:04pm, tiền giờ vẫn 1 giờ.

Không bấm Email Invoice, Print. Không thấy câu nào báo gửi email. Mở chuông cuối lượt: vẫn 5 mục (nhắc dịch vụ, bình luận tự động), không thấy mục nào về đặt xe trong phần hiển thị; hộp thư ngoài không kiểm.

### Ma trận trạng thái đặt xe
| Trạng thái | Hành động làm được | Sang | Điều kiện | Hiệu ứng lên đối tượng khác | Mức |
|---|---|---|---|---|---|
| Requested | Approve, Deny, Cancel, Edit, View Record History | Approved, Denied, Canceled | Approve bắt buộc chọn xe; Deny, Cancel bắt buộc lý do | Không phân công. Không chặn Archive | Chạy |
| Approved | Check Out, Email Invoice, Print, Cancel, Edit, View Record History | Checked Out, Canceled | | Sinh phân công Future; xe bị xám ở đặt khác trùng giờ; chặn Archive. Cancel xoá phân công | Chạy, trừ Email Invoice, Print |
| Checked Out | Return, Email Invoice, Print, Cancel, Edit, View Record History; khi quá giờ hẹn mục đầu là Complete | Completed (đã chạy); Returned (lỗi 422) | | Start Meter ghi vào đồng hồ theo ngày Pick Up | Một phần: Return, Cancel chưa thành |
| Returned | Không đạt tới | | Câu hộp: "From Returned, the reservation can only be moved to Completed." | | Không chạy được |
| Completed | Edit; menu "..." | | | Phân công thành lịch sử có Start, End Meter; đồng hồ xe lên 2.560; hết chặn Archive | Một phần: chưa đọc menu |
| Denied | Menu "..." (chưa đọc), mất Edit | | | Không hiệu ứng | Chạy |
| Canceled | Chỉ View Record History | | | Xoá phân công nếu đã Approved | Chạy |

### Luồng nghiệp vụ
Người đặt chọn pool, loại xe, lý do, giờ. Nếu đủ 3 điều kiện cửa sổ và không trùng lịch thì hệ thống tự duyệt và chọn xe; nếu không thì chờ quản lý duyệt, chọn xe cụ thể. Giao xe (Check Out) ghi Start Meter. Nhận xe ghi End Meter, tính tiền, đóng.

Giải pháp đáng học, điểm yếu:
- Đáng học: bảng giá theo loại xe, giờ, ngày, tuần, tháng, km; bảng khác khi thuê trên N ngày; làm tròn từ đơn vị lớn xuống. Hợp tính phí nội bộ đầu kéo theo chuyến và km.
- Đáng học: đặt xe sinh phân công thật, nên trùng lịch được chặn ngay trong ô chọn xe kèm giờ trùng.
- Đáng học: báo "Charges have been recalculated" trước khi lưu.
- Điểm yếu: múi giờ form và múi giờ cửa sổ lệch thì không tự duyệt mà không báo gì. Với Delta nên hiện rõ lý do không tự duyệt.
- Điểm yếu: lấy xe sớm hơn hẹn thì đồng hồ đề ngày tương lai và Return lỗi không lý do.
- Điểm yếu: bật tính phí không áp cho đặt xe đang có.
Trả lời câu hỏi mở nào: OQ-12 nhóm Nền tảng, OQ-11 nhóm Xe phần đặt xe, phí, tự duyệt. Còn mở: Returned, Cancel khi Checked Out, Hourly threshold khác 24, bảng giá thứ hai.
Màn mới: reservation-detail-requested, reservation-approve-dialog, reservation-detail-approved, reservation-auto-approved-charges, reservation-charges-flat-fee, reservation-vehicle-overlap, reservation-completed.
Dữ liệu TEST đã tạo: đặt xe #1, #2, #5 Canceled, #3 Completed, #4 Denied; TEST-NEN-RATE-01; TEST-FEE-VE-SINH. Pool TEST-NEN-POOL-01 hiện bật tính phí, tự duyệt Thứ Hai 8:00am đến 5:00pm múi giờ Hanoi; để nguyên vì là bản ghi TEST.
Trạng thái cuối: Bảo Tín bỏ tick Operator, đọc lại "Operator: No", thẻ phân công về "Contact must have operator classification to be assigned to vehicles"; lịch sử phân công #3 vẫn trong dữ liệu nhưng tab đã ẩn. TEST-DAUKEO-2 No Group, không Archive.
