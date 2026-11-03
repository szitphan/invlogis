---
type: research
feature: fleetio-saas-platform
updated: 2026-11-03
---

# Nền tảng SaaS — Màn hình thật

Ảnh chụp từ tài khoản dùng thử ngày 02/11/2026 và 03/11/2026, dùng nội bộ để phân tích. Bảng các màn thêm ngày 03/11 viết theo ghi chú chạy; ô "Chưa ghi" là phần ghi chú không nêu. Màn 2.4 Hộp chia sẻ báo cáo và 2.5 Báo cáo đã chia sẻ không có ảnh, mô tả ở Mục 13.7 của spec.

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
| 5 | Save | Nút | — | Lưu báo cáo; chưa bấm |
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
| 4 | Total Runs, Successful Runs, Failed Runs | Cột | Số | Lượt không khớp không được tính; Failed Runs luôn 0 trong lượt chạy |
| 5 | Created By, Last Run At, Current Version | Cột | Chữ, ngày | Truy vết người tạo, phiên bản |

## 3.4 Chi tiết tự động hoá

![Chi tiết tự động hoá](images/automation-detail.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Công tắc bật tắt | Bật tắt | — | Có hộp xác nhận cả hai chiều; bật sinh version v.1, ghi Enabled At |
| 2 | Archive | Nút | — | Không cần tắt trước; có hộp xác nhận |
| 3 | More Actions | Menu | — | Make a Copy, View Record History; chưa bấm |
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
| 1 | All, Needs Action, Open, Resolved, Acknowledged | Tab | — | 261 dòng Sample; chỉ đọc |
| 2 | Issued At, Status, Issue | Cột | Ngày, chữ | Không đổi trạng thái |
| 3 | Manufacturer Campaign Number, NHTSA Campaign Number | Cột | Chữ | Khung Learn ghi nhập tự động theo năm, hãng, đời từ NHTSA |

## 5.4 Đặt xe dùng chung

![Đặt xe dùng chung](images/motor-pool-reservations.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Add Vehicle Reservation | Nút | — | Phải có Motor Pool trong Settings; không chạy |
| 2 | Motor Pool, Number, Operator, Vehicle Types, Vehicle, Pick Up, Drop Off, Status | Cột | Chữ, ngày | Danh sách rỗng |

## 5.5 Kho tài liệu

![Kho tài liệu](images/documents-empty.jpg)

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | All Documents, tab tên tài khoản | Tab | — | Đang rỗng |
| 2 | File Name, File Size, Location, Auto-Delete, Attached To, Labels | Cột | Chữ, số | Không tải tệp |
| 3 | Document File Type, Document Location Type | Lọc | — | Chưa thử |
