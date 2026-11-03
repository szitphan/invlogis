---
type: research
feature: fleetio-saas-platform
updated: 2026-11-03
---

# Nền tảng SaaS — Màn hình thật

Ảnh chụp từ tài khoản dùng thử ngày 02/11/2026 và 03/11/2026, dùng nội bộ để phân tích. Bảng các màn thêm ngày 03/11 viết theo ghi chú chạy; ô "Chưa ghi" là phần ghi chú không nêu. Màn 2.4 Hộp chia sẻ báo cáo và 2.5 Báo cáo đã chia sẻ không có ảnh, mô tả ở Mục 13.7 của spec. Màn lượt 3 không có ảnh: 2.8 Hộp lưu báo cáo, 2.9 Báo cáo đã lưu ở Mục 13.11; 2.10 Bộ lọc báo cáo (lượt 4) ở Mục 21.3; 4.4 Cài đặt thông báo cá nhân ở Mục 14; 5.9 Trang tệp ở Mục 13.14; 5.10 Form bật truy cập, 5.11 Form đặt xe ở Mục 13.21. Bảng các ảnh lượt 3 viết sau khi mở ảnh đối chiếu; phần ảnh không thấy được ghi rõ trong bảng.

## 1.1 Trang đầu

![Trang đầu](images/dashboard.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Fleet Overview | Chọn | — | Đổi dashboard |
| 2 | Refresh, nhóm, More, Add, toàn màn | Nút | — | "0 minutes ago"; lọc All groups |
| 3 | Onboarding Tasks | Khối | Danh sách | Thanh tiến độ, thời gian ước tính, việc đã xong gạch ngang |
| 4 | Needs Attention | Lưới thẻ | Số | Open Issues, Service Reminders, ROs Needing Approval, Overdue Inspections, Critical Faults, All Faults, Renewals; số dẫn tới danh sách lọc |

## 2.1 Báo cáo chuẩn

![Báo cáo](images/reports.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Tìm báo cáo | Tìm | Chữ | — |
| 2 | Standard Reports, Favorites, Saved, Shared | Menu | Số | — |
| 3 | Report Types | Menu | Số | 13 nhóm kèm số lượng, tổng 49 báo cáo (bản 02/11 ghi 12 nhóm là sai) |
| 4 | Thẻ báo cáo | Thẻ | — | Tên, mô tả, nhóm, nhãn "Upgrading soon" |
| 5 | Sắp xếp, lưới, danh sách | Nút | — | — |

## 2.2 Báo cáo Sự cố

![Báo cáo Sự cố](images/report-issues.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Summary | Biểu đồ | Số | Đếm theo Open, Overdue, Closed, Resolved |
| 2 | Top Vehicles | Biểu đồ | Số | Xe có nhiều sự cố nhất |
| 3 | Filters, Columns | Nút | — | Lọc và chọn cột; có phân trang |
| 4 | Bảng sự cố | Bảng | Danh sách | Cột Issue, Status, Summary, Reported By, Assigned, Due Date, Due Meter, Asset Record Type, Name/Tool Name |
| 5 | Save | Nút | — | Lưu báo cáo; lượt 3 đã bấm, xem màn 2.8 |
| 6 | Share | Nút | — | Sinh ngay link công khai, không hỏi trước (E-fleetio-saas-platform-013) |
| 7 | Export CSV | Menu | — | Export Visible Columns, Export All Columns; chưa bấm |
| 8 | Print | Nút | — | Chưa bấm |

## 2.3 Hỏi dữ liệu

![Hỏi dữ liệu](images/ai-analyst-issues.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | AI Data Analyst | Khung nhúng | — | Nhúng từ ThoughtSpot, mở từ nút Ask a data question trên đầu trang |
| 2 | Ô hỏi | Chữ | Câu hỏi | Trả lời sau khoảng 40 đến 50 giây |
| 3 | Câu trả lời, bảng | Chữ, bảng | Số | "currently has 2 open issues", bảng Total Count Issue Id = 2; thật là 7 (E-fleetio-saas-platform-012) |
| 4 | Show work | Nút | — | Xem cách làm |
| 5 | All data models | Chọn | — | Chọn nguồn dữ liệu |
| 6 | My Conversations | Danh sách | — | Lưu hội thoại |

## 3.1 Trình dựng tự động hoá

![Tự động hoá](images/automation-builder.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Tên | Chữ | — | Mặc định theo thời điểm, sửa được |
| 2 | Disabled, Save | Bật tắt, nút | — | Save khoá đến khi đủ |
| 3 | Trigger, Conditions, Actions | Khối | — | "Start when", "Check if", "Do this" |
| 4 | Browse Templates | Nút | — | 18 mẫu |
| 5 | Record Type | Chọn | Bắt buộc | Work Order, Service Entry, Fault, Issue, Purchase Order, Geofence Event, Vehicle |
| 6 | Give Feedback | Liên kết | — | "Don't see a trigger you'd like?" |

## 3.2 Thư viện mẫu tự động hoá

![Thư viện mẫu](images/automation-templates.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Cột trái theo loại trigger | Menu | Số | Faults 2, Issues 5, Purchase Orders 3, Service Entries 2, Work Orders 6 |
| 2 | Thẻ mẫu | Thẻ | — | Tên, sơ đồ trigger, số điều kiện, số hành động |
| 3 | Apply | Nút | — | Hiện khi rê chuột; mở trình dựng theo mẫu, chưa lưu gì |

## 3.3 Danh sách tự động hoá

![Danh sách tự động hoá](images/automation-list-data.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | All, Archived | Tab | — | Tách bản đã lưu trữ |
| 2 | Created By, Trigger Record, Status, Filters | Lọc | — | Lọc nhanh |
| 3 | Name, Status, Trigger Record | Cột | Chữ | Định danh và trạng thái |
| 4 | Total Runs, Successful Runs, Failed Runs | Cột | Số | Lượt không khớp không được tính; ảnh này Failed Runs 0, lượt 3 có lượt thất bại ở màn 3.11 |
| 5 | Created By, Last Run At, Current Version | Cột | Chữ, ngày | Truy vết người tạo, phiên bản |

## 3.4 Chi tiết tự động hoá

![Chi tiết tự động hoá](images/automation-detail.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Công tắc bật tắt | Bật tắt | — | Có hộp xác nhận cả hai chiều; bật sinh version v.1, ghi Enabled At |
| 2 | Archive | Nút | — | Không cần tắt trước; có hộp xác nhận |
| 3 | More Actions | Menu | — | Make a Copy, Archive, View Record History; lượt 3 đã chạy Make a Copy; Delete chỉ ở bản Archived |
| 4 | Failure Notification Email, Run Summary Email | Ô nhập | Chưa ghi | Không bật vì gửi email |
| 5 | Bố cục còn lại | Chưa ghi | Chưa ghi | Ghi chú chạy không mô tả từng khối |

## 3.5 Lịch sử lượt chạy

![Lịch sử lượt chạy](images/automation-run-history.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Danh sách lượt | Bảng | Danh sách | Kết quả SUCCESS; lượt không khớp không hiện |
| 2 | Cột cụ thể | Chưa ghi | Chưa ghi | Ghi chú chạy không liệt kê tên cột; mở một dòng ra màn 3.6 |

## 3.6 Kết quả một lượt chạy

![Kết quả lượt chạy](images/automation-run-result.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Phiên bản | Chữ | — | Phiên bản automation đã chạy |
| 2 | Bản ghi kích hoạt | Liên kết | — | Bản ghi gây ra lượt chạy |
| 3 | Records | Chữ | — | "Records: No records changed" dù đã thêm comment, điểm yếu |
| 4 | Log | Khối | JSON | Đội hỗ trợ tra được vì sao chạy |

## 3.7 Lượt chạy tự kích hoạt

![Lượt tự kích hoạt](images/automation-self-trigger-runs.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Hai lượt liên tiếp | Bảng | Danh sách | Create rồi Update; sau đó dừng vì giá trị không đổi |
| 2 | Triggered By | Cột | Chữ | Vẫn ghi người tạo Issue, không ghi automation; điểm yếu |

## 3.8 Tự động hoá đã lưu trữ

![Tự động hoá đã lưu trữ](images/automation-archived.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Thông báo chỉ đọc | Chữ | — | "Archived records are read-only and cannot be updated." (E-fleetio-saas-platform-005) |
| 2 | Restore | Nút | — | Về Disabled, không tự bật; "Record successfully restored" |
| 3 | Delete | Nút | — | Không bấm theo ràng buộc; hành vi chưa biết |

## 3.9 Comment do tự động hoá tạo

![Comment của tự động hoá](images/automation-comment-result.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Comment trên Issue | Khối | Chữ | Xuất hiện trong vòng 6 giây sau khi tạo Issue khớp điều kiện |
| 2 | Tác giả | Chữ | — | "Fleetio Automation" |

## 4.1 Maintenance Settings

![Cấu hình bảo dưỡng](images/maintenance-settings.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Enable Work Orders | Tick | — | Tắt thì ẩn Work Orders, Parts |
| 2 | Next Work Order Number | Số | Bắt buộc | Hiện số cao nhất đã dùng |
| 3 | Require a Meter Reading | Tick | — | Có Excluded Vehicle Types |
| 4 | Service Task Inspections | Tick | — | Bắt nộp phiếu gắn việc |
| 5 | Maintenance Categorization | Tick | — | Bắt phân loại, lý do, nhóm; khoá sửa mã mặc định |
| 6 | Complaint, Cause, Correction; Markups | Tick, số | — | Xem thêm khi cuộn |
| 7 | Thanh trái Settings | Menu | — | Tìm được, chia nhóm |

## 4.2 Record Sets

![Record Sets](images/record-sets.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Vehicles, Contacts, Part Locations, Inspection Forms | Tab | — | Đối tượng áp phạm vi |
| 2 | Name | Cột | Chữ | Assigned Vehicles Only, Full Access (mặc định), No Access, User's Group Only, View Only; biểu tượng hệ thống |
| 3 | Manage, View | Cột | All, Some, None | Tách quyền sửa và xem |
| 4 | Users | Cột | Số | Số người đang dùng |
| 5 | Add Record Set | Nút | — | Tạo tập theo điều kiện |

## 4.3 Điều kiện tập bản ghi

![Điều kiện tập bản ghi](images/record-set-conditions.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Record Type | Chọn | — | "can't be changed after creation" (E-fleetio-saas-platform-008) |
| 2 | Manage, View | Khối | — | Khai riêng hai quyền |
| 3 | Điều kiện Vehicles | Chọn | — | All vehicles, Vehicles in this contact's group, Vehicles assigned to this contact, Specific vehicles, Vehicles in specific groups, Vehicles with specific status(es), Vehicles with specific custom field values, No vehicles; không có điều kiện theo thời gian |

## 5.1 Liên hệ không truy cập

![Liên hệ không truy cập](images/contact-no-access.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Trạng thái truy cập | Chữ | — | "This Contact doesn't have user access." |
| 2 | Khối xe | Khối | — | "Contact must have operator classification to be assigned to vehicles" (E-fleetio-saas-platform-006) |
| 3 | Bố cục còn lại | Chưa ghi | Chưa ghi | Ghi chú chạy chỉ mô tả form tạo: Basic Details, Classifications, User Access, Contact Information |

## 5.2 Menu thao tác xe

![Menu thao tác xe](images/vehicle-more-actions.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Edit Vehicle Settings, Manage Inspection Forms, Manage Service Programs, Manage Integration Links | Mục menu | — | Không bấm |
| 2 | Attach Shared Document, Recalculate Fuel Entries, View Record History | Mục menu | — | Không bấm |
| 3 | Archive | Mục menu | — | Cần quyền `vehicles_archive_delete`, Operator không có; không bấm |

## 5.3 Danh sách thu hồi hãng

![Danh sách Recall](images/recalls-list.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | All, Needs Action, Open, Resolved, Acknowledged | Tab | — | Ảnh ở tab Needs Action, "1 - 50 of 261" (chữ nhỏ), dòng Sample; chỉ đọc. Nhóm Sửa chữa đọc cùng tab về sau: 285 (OQ-21) |
| 2 | Issued At, Status, Issue | Cột | Ngày, chữ | Không đổi trạng thái |
| 3 | Manufacturer Campaign Number, NHTSA Campaign Number | Cột | Chữ | Khung Learn ghi nhập tự động theo năm, hãng, đời từ NHTSA |

## 5.4 Đặt xe dùng chung

![Đặt xe dùng chung](images/motor-pool-reservations.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Add Vehicle Reservation | Nút | — | Phải có Motor Pool trong Settings; lượt 5 đã mở, xem màn 5.13 |
| 2 | Motor Pool, Number, Operator, Vehicle Types, Vehicle, Pick Up, Drop Off, Status | Cột | Chữ, ngày | Danh sách rỗng |

## 5.5 Kho tài liệu

![Kho tài liệu](images/documents-empty.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | All Documents, tab tên tài khoản | Tab | — | Đang rỗng |
| 2 | File Name, File Size, Location, Auto-Delete, Attached To, Labels | Cột | Chữ, số | Không tải tệp |
| 3 | Document File Type, Document Location Type | Lọc | — | Chưa thử |

## 2.6 Lỗi báo cáo

![Lỗi báo cáo Expenses by Vehicle](images/report-expense-entries-500.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Logo Fleetio | Hình | — | Trang lỗi riêng, không có menu trái, đầu trang |
| 2 | "We're sorry, but something went wrong." | Chữ | — | E-fleetio-saas-platform-014, mở `reports/expense_entries` 2 lần cùng lỗi; câu phụ "We've been notified about this issue and we'll take a look at it shortly." |
| 3 | Go back, contact us | Liên kết | — | "Go back and try again or contact us to report an issue." |
| 4 | Partially Degraded Service | Chữ, chấm vàng | — | Trạng thái dịch vụ lúc đọc; có thể sự cố tạm của hãng, chưa thử lại sau |
| 5 | Status page | Liên kết | — | "For detailed status information, please visit our status page"; chưa bấm |

## 2.7 Hỏi dữ liệu: xe không tồn tại

![AI nói xe không tồn tại](images/ai-analyst-vehicle-not-exist.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | My Conversations | Danh sách | — | New chat, nhóm Chats, 3 hội thoại; tên bị cắt |
| 2 | Câu hỏi | Chữ | — | "List open issues of vehicle TEST-DAUKEO-2 with issue number, summary and priority."; có giờ gửi, menu ba chấm |
| 3 | Show work | Nút mở | — | Chưa mở trong ảnh |
| 4 | Câu trả lời | Chữ | — | "no issues were found for vehicle TEST-DAUKEO-2"; hai truy vấn đã làm; "Vehicle TEST-DAUKEO-2 does not exist in the issues dataset with that exact name", "No issues have been recorded for this vehicle" (E-fleetio-saas-platform-015). Một dòng mở đầu danh sách bị khung gợi ý che, chỉ đọc được "Both queri..." |
| 5 | Khung gợi ý nổi | Tooltip | — | "Provides data on service, parts, and labor costs based on service entries."; do con trỏ rê đúng lúc chụp; chưa rõ gắn với mục nào |
| 6 | Câu hỏi lại người dùng | Chữ | — | Hỏi có gõ đúng tên không, có muốn tìm tên gần giống không |
| 7 | Is this useful? | Nút thích, không thích | — | Chưa bấm |
| 8 | Ô hỏi, All data models | Chữ, chọn | Câu hỏi | "Enter your question"; có thêm tệp, gửi |

## 3.10 Lịch sử phiên bản

![Phiên bản v.1 hiện nội dung v.2](images/automation-version-v1-lech.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Version History | Hộp | — | Mở trên trang chi tiết automation; đang ở bước xem một bản, chưa thấy danh sách phiên bản trong ảnh |
| 2 | Step Summary, nhãn v.1 | Chữ | — | Bản đang xem |
| 3 | Trigger | Khối | — | "Issue is created", có biểu tượng cảnh báo cạnh nhãn; chưa rõ cảnh báo gì |
| 4 | Conditions | Khối | Số | 1 điều kiện, "Issue Summary contains TEST-NEN" |
| 5 | Actions | Khối | Số | Add Issue Comment; nội dung "TEST-NEN-AUTO comment tu dong v2" dù đang xem v.1 (E-fleetio-saas-platform-018); Prevent duplicate comments: — |
| 6 | Back | Nút | — | Quay về danh sách phiên bản |
| 7 | Nền trang | Chữ | Số | Mờ một phần: Enabled, Total Runs 3, Successful 3, Failed 0, Run Summary Email Off, Failure Notification Email Off; khối bị hộp che không đọc được |

## 3.11 Lượt chạy thất bại

![Lượt automation thất bại](images/automation-run-failure.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Băng đỏ | Thông báo | — | "Automation Action failed: Start Date can't be blank" (E-fleetio-saas-platform-011) |
| 2 | Status | Nhãn | — | FAILURE đỏ |
| 3 | Version | Nhãn, liên kết | — | v.1, có View |
| 4 | Processed At | Ngày giờ | — | Thời điểm xử lý |
| 5 | Records | Chữ | — | "No records changed"; lần này đúng, WO #111 giữ nguyên |
| 6 | Trigger Record | Liên kết | — | Work Order - #111 |
| 7 | Trigger Type | Chữ | — | Create |
| 8 | Triggered At | Ngày giờ | — | Trùng phút với Processed At |
| 9 | Triggered By | Liên kết | — | Ghi người tạo WO |
| 10 | Back, View Full Log | Nút | — | Log JSON từng bước; nội dung log không có trong ảnh |
| 11 | Nền trang | Chữ | Số | Mờ một phần: Enabled, Successful 0, Failed 1, Run Summary Email Off, Failure Notification Email Off, Activity "Enabled changed from false to true" |

## 3.12 Luật đổi trạng thái xe

![Automation lật trạng thái xe](images/automation-vehicle-status-flip.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Status Updates | Hộp | Danh sách | Mở từ biểu tượng lịch sử cạnh trường Status; mới nhất ở trên |
| 2 | Dòng do automation | Dòng | — | "Fleetio Automation updated status from Active to Inactive" (E-fleetio-saas-platform-017) |
| 3 | Dòng do người | Dòng | — | Tên người "updated status from Inactive to Active"; dòng tiếp theo cùng phút là automation đổi lại |
| 4 | Ngày giờ | Chữ gạch chân | — | Từng dòng; không có cột nguồn riêng, nguồn nằm trong câu |
| 5 | Thời lượng | Chữ | — | Thời gian ở trạng thái đó: 12 seconds, 1 second, 1 minute 3 seconds, 4 hours 16 minutes |
| 6 | Close | Nút | — | Đóng hộp |
| 7 | Nền trang | Chữ | — | Trang xe: Status Inactive, Group No Group, Operator Unassigned, Type Semi Truck; có biểu tượng lịch sử ở Status, Group; tên xe bị hộp che một phần |

## 5.6 Lịch sử bản ghi sự cố

![Record History của Issue](images/record-history-issue.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Select Date Range, nút tìm | Chọn ngày | Ngày | Lọc lịch sử; chưa đổi trong ảnh |
| 2 | Date, Changes By, Changes Made | Cột | Ngày, chữ | 2 dòng cùng phút |
| 3 | "Issue created" | Dòng | — | Tạo Issue |
| 4 | "Issue Priority Status changed from pending to failed" | Dòng | — | Giá trị `pending`, `failed` tô đỏ; AI xếp mức thất bại, chỉ thấy ở đây (E-fleetio-saas-platform-016). Changes By ghi người tạo, không ghi máy |
| 5 | Close | Nút | — | Đóng hộp. Ảnh không có dòng Comment, Watch, đúng BR-fleetio-saas-platform-040; số Issue bị hộp che, theo ghi chú chạy là #55 |

## 5.7 Hộp thông báo

![Notifications](images/notifications-inbox.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Notifications, số 3 | Tiêu đề, nhãn đếm | Số | 3 chưa đọc; ngăn kéo bên phải đè lên trang Issue #55 |
| 2 | Inbox, Archived | Tab | — | Đang ở Inbox |
| 3 | All Activity, Comments Only, @ Mentions | Lọc | — | Đang thấy cả ba sáng |
| 4 | Archive all, ba chấm, đóng | Nút | — | Chưa bấm; menu ba chấm trong ảnh chưa mở, ghi chú chạy ghi có Notification Settings |
| 5 | Dòng comment của automation | Dòng | — | "Fleetio Automation commented on an issue"; Issue #54, #55, #54 trên TEST-DAUKEO-2, trích nội dung; 2 dòng #54 là 2 automation cùng chạy (C-155) |
| 6 | Reply, View All Comments | Nút, liên kết | — | Từng dòng; chưa bấm |
| 7 | Fuel Capacity Alert | Dòng | — | Fuel Entry trên TEST-KHO-01; có trong khi 0 hồ sơ thông báo (BR-fleetio-saas-platform-042). Ảnh bị cắt ở dòng này, dòng sau không đọc được |
| 8 | Nền trang Issue #55 | Chữ | — | Status Open, Priority "No Priority" (biểu tượng chờ), Timeline "opened this issue" |

## 5.8 Kho tài liệu có tệp

![Kho tài liệu có tệp](images/documents-list-file.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Upload Document | Nút | — | Mở hộp Filestack (không có trong ảnh) |
| 2 | Learn | Nhãn | — | Khung hướng dẫn tại chỗ |
| 3 | All Documents, tab tên tài khoản | Tab | — | Đang ở All Documents |
| 4 | Search, Document File Type, Document Location Type, Filters | Lọc | — | Chưa thử; có phân trang "1 - 1 of 1", biểu tượng cài đặt xem |
| 5 | File Name | Cột | Chữ | TEST-NEN-tailieu.txt, biểu tượng tệp |
| 6 | File Size | Cột | Số | 26 Bytes |
| 7 | Location | Cột | Chữ | Tên tài khoản |
| 8 | Auto-Delete | Cột | Ngày | — , chưa đặt |
| 9 | Attached To | Cột, liên kết | — | "Select Vehicles": ảnh chụp trước khi gắn; trạng thái "Attached" không có trong ảnh, theo ghi chú chạy |
| 10 | Labels | Cột | — | — |
| 11 | Menu dòng | Nút ba chấm | — | Chưa mở trong ảnh; ghi chú chạy ghi View, Rename, Replace, Download, Delete |

## 5.12 Thêm nhóm xe dùng chung

![Add Motor Pool](images/motor-pool-add.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Name * | Ô nhập | Chữ | Tên pool, `TEST-NEN-POOL-01` |
| 2 | Groups * | Chọn nhiều | Nhãn | Bắt buộc; ảnh chữ nhỏ, ghi chú chạy ghi một nhóm có sẵn tên giống ngày |
| 3 | Vehicle Types * | Chọn nhiều | Nhãn | Semi Truck; quyết định loại xe chọn được khi đặt (màn 5.13) |
| 4 | Vehicle Statuses * | Chọn nhiều | Nhãn | Active, mặc định theo ghi chú chạy |
| 5 | Automatically calculate charges | Tick | — | Không tick; tính phí chưa chạy |
| 6 | Require "Reason for Trip" field | Tick | — | Đang tick; hiện cảnh báo cam áp cho mọi đặt xe, cả sửa đặt xe cũ (BR-fleetio-saas-platform-059) |
| 7 | Auto Approvals, How it works | Bật tắt, nhãn | — | Đang tắt trong ảnh; các ô Time zone, Days, Start Time, End Time, Full day, Add Window theo ghi chú chạy, không có trong ảnh |
| 8 | Cancel, Save | Nút | — | Save báo "Motor Pool was successfully created" (không có trong ảnh) |
| 9 | Nền trang | Menu | — | Settings mờ, nhóm Motor Pool có Motor Pools, Reservation Rates, Flat Fees. Toast "Complete: Restoring Work Order #106 data" là việc ngoài luồng này, ghi chú chạy không nêu |

## 5.13 Lỗi form đặt xe

![Vehicle Reservation báo lỗi](images/reservation-validation.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Operator * | Chọn, có biểu tượng trợ giúp | Liên hệ | Viền đỏ, "must exist" (E-fleetio-saas-platform-029). Chỉ liệt kê liên hệ có đăng nhập và là Operator; "No options" (E-fleetio-saas-platform-028, không có trong ảnh) |
| 2 | Motor Pool * | Chọn, có trợ giúp | Pool | `TEST-NEN-POOL-01` |
| 3 | Vehicle Types * | Chọn nhiều, có trợ giúp | Nhãn | Semi Truck; chỉ hiện sau khi chọn pool. Không có ô chọn xe cụ thể |
| 4 | Reason for Trip * | Ô nhập | Chữ | Viền đỏ, "is required for this motor pool" vì pool bắt buộc |
| 5 | Pick Up *, Drop Off * | Ngày, giờ | Ngày giờ | Viền đỏ, "can't be blank" dù ô hiện chữ mờ ngày giờ hiện tại: đó là placeholder |
| 6 | Cancel, Submit Reservation | Nút | — | Submit không tạo bản ghi |
| 7 | Toast đỏ | Thông báo | — | "Failed to create Reservation". Toast xanh "Complete: Restoring Work Order #106 data" là việc ngoài luồng này, ghi chú chạy không nêu |
| 8 | Nền trang Reservations | Bảng | — | Cột Motor Pool, Number, Pick Up, Drop Off, Status; danh sách rỗng; khung Learn "Reservations Overview" bị hộp che một phần |
