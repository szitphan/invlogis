---
type: research
feature: fleetio-location-dispatch
status: draft
status_changed: 2026-11-03
status_reason: "đã review upstream, không cần sửa"
updated: 2026-11-03
links:
  - docs/_research/fleetio/fleetio-location-dispatch.md
  - docs/_research/fleetio/run-notes/location-dispatch.md
  - docs/vehicle-telematics/brainstorms/vehicle-telematics.md
---

# Bản đồ, địa điểm, gán việc — SRS phân tích ngược từ Fleetio

> Mô tả **Fleetio đang làm gì**, kèm đề xuất cho Invlogis chưa chốt. **Không làm mẫu điều vận.** Mọi kết quả về xe trên bản đồ, marker và sự kiện vùng dùng vị trí giả lập gửi qua phiếu kiểm tra web, chưa kiểm với thiết bị thật hay Fleetio Go.

**Nhãn bằng chứng:** `Chạy` đã thao tác, không phụ thuộc vị trí giả lập · `Chạy (vị trí giả lập)` đã thao tác, dữ liệu vị trí là giả lập · `Xem` thấy trên giao diện · `Docs` tài liệu công khai · `Suy` suy ra · `GĐ` giả định.

## 1. Scope

**Trong phạm vi:** Fleet Map, Places, Geofence, Geofence Alert Policy, sự kiện vùng và Automation theo sự kiện vùng, Location Entry từ phiếu kiểm, Location Exception, Jobs, Job Assignment.

**Ngoài phạm vi:** mạng lưới xưởng Mỹ; Lệnh vận tải của Invlogis; Fleetio Go trên điện thoại (chưa kiểm); thiết bị định vị thật (tài khoản dùng thử không có).

## 2. Actors & Stakeholders

| Actor | Loại | Mục tiêu | Trong scope? | Tương đương Invlogis |
|---|---|---|---|---|
| Fleet Manager | Người | Xem xe, tìm nơi gần xe, gán việc | Có | Điều vận, Quản lý phương tiện |
| Administrator | Người | Khai địa điểm, vùng, Automation, cảnh báo | Có | Admin |
| Người kiểm tra xe | Người | Nộp phiếu, vô tình gửi vị trí | Có | Lái xe |
| Telematics | Ngoài | Đẩy vị trí | Có, chỉ `Docs` | EUP |
| Hệ thống ngoài qua API | Ngoài | Tạo Location Entry | Có, chỉ `Docs` | Lớp kết nối GPS |

## 3. Functional Requirements (FR)

| ID | Title | Description | Priority | Tầng | Verify by | Source | Mức | Đề xuất Invlogis |
|---|---|---|---|---|---|---|---|---|
| FR-fleetio-location-dispatch-001 | Bản đồ cạnh danh sách | Danh sách Nearby có tab Vehicles, Places, đếm kết quả, sắp theo Distance; dòng ghi tên xe, người lái ("Unassigned" nếu chưa gán), tuổi vị trí ("3m ago"); ô "Update list when map moves". Mốc khoảng cách là tâm bản đồ (`Suy`, không đo được công thức). | P0 | [Lõi] | demo | Run-notes Fleet Map | `Chạy (vị trí giả lập)` | Lấy cho `vehicle-telematics` |
| FR-fleetio-location-dispatch-002 | Lớp bản đồ | Vehicles, Places, Vendors bật tắt; Shops theo tài liệu hãng. Trong panel xe, PLACES, VENDORS mặc định ẩn, có nút "Show Places", "Show Vendors". | P0 | [Lõi] | demo | Run-notes Fleet Map, tài liệu hãng | `Chạy (vị trí giả lập)`, `Docs` phần Shops | Lấy, thay Shops bằng cây dầu, cảng |
| FR-fleetio-location-dispatch-003 | Tải theo khung nhìn | Lấy vị trí theo khung đang xem, gọi lại khi đổi khung. | P0 | [Lõi] | test | Lần xem trực tiếp đầu | `Chạy` | Lấy |
| FR-fleetio-location-dispatch-004 | Nguồn vị trí | Từ tích hợp (`Docs`), API (`Docs`), hoặc từ phiếu kiểm tra (`Chạy`). **Đã sửa:** phiếu dầu và phiếu dịch vụ trên web không có ô vị trí; trên Fleetio Go chưa kiểm. | P1 | [Lõi] | demo | Run-notes Vị trí không cần thiết bị | `Chạy`, `Docs` | Lấy làm dự phòng khi mất GPS |
| FR-fleetio-location-dispatch-005 | Tìm và lọc | Ô "Locate vehicles, places, vendors on map..." tìm và chọn được xe. Filters có Vehicle Type, Vehicle Group, Vehicle Status, Vehicle Operator, Vehicle Assigned, còn thêm phía dưới. | P0 | [Lõi] | demo | Run-notes Fleet Map | `Chạy (vị trí giả lập)` | Lấy |
| FR-fleetio-location-dispatch-006 | Chi tiết khi chọn xe | Bấm marker hoặc dòng: không popup, panel trái đổi sang xe, marker gắn nhãn tên. Tab Overview có Alerts (Open Issues, Service Reminders, Incomplete Work Orders), Last Known Location (Status, Last Updated, Where, Source), Details; tab Nearby. Căn giữa xe: `Docs`. | P1 | [Lõi] | demo | Run-notes Fleet Map | `Chạy (vị trí giả lập)` | Lấy |
| FR-fleetio-location-dispatch-007 | Quan hệ gần | Dòng Place trong Nearby có khoảng cách. Rê chuột vẽ đường thẳng nét đứt từ xe tới Place, marker xe đổi thành marker Place trong lúc rê. | P2 | [Lõi] | demo | Run-notes Fleet Map | `Chạy (vị trí giả lập)` | Cân nhắc; không lấy việc đổi marker xe |
| FR-fleetio-location-dispatch-008 | Tuỳ chọn bản đồ | **Đã sửa tên:** Default (không phải Standard), Satellite, Grayscale; Labels hiện tên Place; Set Label Options; lưu theo người dùng, tải lại vẫn giữ. Map Starting Location có Use Current Map Center, Reset to Default (`Xem`). Street View: có Pegman, không vào được chế độ này (`Xem`). | P1 | [Cấu hình] | demo | Run-notes Fleet Map | `Chạy (vị trí giả lập)` | Lấy |
| FR-fleetio-location-dispatch-009 | Chú giải | **Đã sửa nghĩa:** Map Legend có Active, Idle, Stale là độ tươi vị trí, không phải xe chạy, nhàn rỗi; Place là tâm vùng; Preferred Shop, Premier Fleetio Vendor, In-Network Shop, Out-of-Network Shop, Vendor. | P1 | [Lõi] | demo | Run-notes Fleet Map | `Chạy (vị trí giả lập)` | Lấy cách làm chú giải; BL-382 cần bộ riêng có chạy, dừng |
| FR-fleetio-location-dispatch-010 | Địa điểm | Tên, mô tả, địa chỉ, toạ độ, bán kính. Gõ toạ độ thì Address tự điền theo địa chỉ ngược, bản đồ tự chuyển. Vòng tròn đổi ngay khi chọn bán kính, chưa cần lưu. Bấm bản đồ ở chế độ thường đặt lại pin. | P1 | [Cấu hình] | demo | Run-notes Tạo Place | `Chạy` | Lấy cho `location-catalog`; bỏ việc bấm bản đồ đổi pin ngoài ý muốn |
| FR-fleetio-location-dispatch-011 | Sự kiện vùng | Hai loại Entered, Exited, sinh khi vị trí mới đổi quan hệ với vùng. Dùng làm Record Type của Automation. Không có màn danh sách riêng. | P1 | [Cấu hình] | test | Run-notes Sự kiện vùng | `Chạy (vị trí giả lập)` | Đối chiếu `vehicle-telematics`; thêm nhật ký vào, ra vùng |
| FR-fleetio-location-dispatch-012 | Gán xe vào việc | Tạo việc, gán xe, tính thời gian trên việc; tự tạo và kết thúc gán theo vùng. Chi tiết tách ở FR 014 đến 022. | P2 | [Cấu hình] | demo | Run-notes Việc | `Chạy`, `Chạy (vị trí giả lập)` phần tự gán | Không lấy cho điều vận |
| FR-fleetio-location-dispatch-013 | Lịch sử vị trí | Tab Location History trên xe. | P1 | [Lõi] | demo | Lần xem trực tiếp đầu, chưa mở lại | `Xem` | Lấy |
| FR-fleetio-location-dispatch-014 | Bảng việc dạng cột | Cột Unassigned (toàn bộ xe) cộng mỗi việc đang chạy một cột, có số đếm. Thẻ xe ghi "On job: 0m". Tab Active, Completed. Lọc Job Name or Number, Vehicle Group, Vehicle Type, Filters. Ô tìm lọc theo tên xe, ẩn cột việc không có xe khớp. | P2 | [Cấu hình] | demo | Run-notes Việc | `Chạy` | Không lấy cho điều vận |
| FR-fleetio-location-dispatch-015 | Tạo việc | Form Add Job: Job Number, Job Name, Place, ô tự gán theo vùng. Nút giữa màn trống và nút góc phải mở cùng form; nút giữa chỉ có khi chưa có việc. Start Date/Time tự lấy lúc tạo. | P2 | [Cấu hình] | demo | Run-notes Việc | `Chạy` | Không lấy |
| FR-fleetio-location-dispatch-016 | Gán tay | Tích xe trong cột, Actions, Assign. Hộp Add Job Assignments có Job, Start Date/Time. | P2 | [Cấu hình] | demo | Run-notes Việc | `Chạy` | Không lấy; học nguyên tắc cấm giờ tương lai |
| FR-fleetio-location-dispatch-017 | Kết thúc gán tay | Actions, Unassign. Hộp Unassign from Job có End Date/Time. | P2 | [Cấu hình] | demo | Run-notes Việc | `Chạy` | Không lấy; điền sẵn giờ |
| FR-fleetio-location-dispatch-018 | Sửa, xoá lượt gán | Menu dòng xe: Edit, Delete. Edit Job Assignment khoá Job và Vehicle, chỉ sửa Start Date/Time. Delete chưa bấm (`Xem`). | P2 | [Cấu hình] | demo | Run-notes Việc | `Chạy` | Không lấy |
| FR-fleetio-location-dispatch-019 | Hoàn thành việc | Menu cột: Edit, Complete, Delete. Hộp Complete Job chỉ có End Date/Time; xe đang gán tự kết thúc cùng lúc. Edit, Delete của việc chưa bấm (`Xem`). | P2 | [Cấu hình] | demo | Run-notes Việc | `Chạy` | Không lấy; hỏi lại khi còn xe |
| FR-fleetio-location-dispatch-020 | Lịch sử gán | Job Assignment History: Job, Place, Vehicle, Time on Job, Start Date, End Date (Active khi đang gán), Added; lọc Status, Job Status, Job, Vehicle; Group: None. | P2 | [Cấu hình] | demo | Run-notes Việc | `Chạy` | Lấy mẫu cột Added ghi nguồn |
| FR-fleetio-location-dispatch-021 | Trang việc | Tab Overview, Job Assignments; Details gồm Job Number, Job Name, Status, Place, Auto-Tracking, Start Date/Time, End Date/Time; bản đồ vùng Place. | P2 | [Cấu hình] | demo | Run-notes Việc | `Chạy` | Không lấy |
| FR-fleetio-location-dispatch-022 | Tự gán, tự kết thúc theo vùng | Việc bật ô tự động, gắn Place: vào vùng thêm lượt gán Added = Geofence, thẻ xe có chip "Geofence"; ra vùng lượt có End Date, xe về Unassigned. | P2 | [Cấu hình] | test | Run-notes Tự gán | `Chạy (vị trí giả lập)` | Không lấy cho điều vận; học chip nguồn |
| FR-fleetio-location-dispatch-023 | Vị trí từ phiếu kiểm web | Web app đọc vị trí trình duyệt một lần lúc khởi động app, giữ giá trị và gửi kèm phiếu khi nộp. Phiếu ghi Submission Source "Fleetio Web App", có bản đồ nhỏ chấm tại vị trí. Sinh Location Entry, xe lên marker ngay. | P1 | [Lõi] | test | Run-notes Phiếu kiểm web | `Chạy` | Lấy ý tưởng; đọc lúc nộp, báo người dùng |
| FR-fleetio-location-dispatch-024 | Location Entry | Mỗi lần ghi vị trí có asset, loại, contact, thời điểm, Entry Type. Địa chỉ ngược có sau khoảng 1 phút, lúc đầu rỗng. `initial_place` cho biết lần ghi nằm trong Place nào. | P1 | [Lõi] | test | Run-notes Giả lập vị trí | `Chạy (vị trí giả lập)` | Lấy |
| FR-fleetio-location-dispatch-025 | Vùng đa giác | Bấm biểu tượng đa giác, bấm các đỉnh, bấm lại đỉnh đầu để đóng. Hệ thống thay toạ độ bằng tâm, đổi Address theo tâm, khoá Geofence Radius với giá trị tự tính. Fleet Map vẽ đúng hình. | P1 | [Cấu hình] | demo | Run-notes Vùng đa giác | `Chạy` | Lấy cho `location-catalog`; không hiện bán kính với đa giác |
| FR-fleetio-location-dispatch-026 | Danh sách, trang địa điểm | Danh sách cột Name, Description, Address; lọc nhanh Location Entry Type, Location Entry Date, Place Geofence Radius. Trang chi tiết: tab Overview, Location Entries; khối Details, Latest Location Entries, Geofence Alert Policy, bản đồ. Location Entries có cột Asset, Asset Type, Contact, Date, Entry Type; Manage Columns thêm Address, Created On, Updated On. | P1 | [Cấu hình] | demo | Run-notes Tạo Place, Sự kiện vùng | `Chạy`, `Chạy (vị trí giả lập)` phần Location Entries | Lấy |
| FR-fleetio-location-dispatch-027 | Cảnh báo vùng | Add Alert Policy trên Place: Trigger (Vehicle is within, outside geofence; Contact is within, outside geofence), Which Vehicles?, Which Groups?, Description, Enabled, Email Message, Recipients, Include Watchers, Receive as Summary. Chưa lưu. | P1 | [Cấu hình] | test | Run-notes Geofence Alert Policy | `Xem` | Đối chiếu `vehicle-telematics` |
| FR-fleetio-location-dispatch-028 | Automation theo sự kiện vùng | Record Type Geofence Event, Trigger Type Created (lựa chọn duy nhất). Điều kiện phổ biến: Geofence Event Type, Geofence Event Place, Vehicle, Vehicle Group. Hành động trên Vehicle: Update Field, Add Comment, Send Email. Đã chạy Add Comment; có Total Runs, Successful. | P1 | [Cấu hình] | test | Run-notes Sự kiện vùng | `Chạy (vị trí giả lập)` | Lấy; buộc chọn loại sự kiện |
| FR-fleetio-location-dispatch-029 | Quick Add | Nút Add trên panel, 11 mục: Draft Work Order, Add Vehicle Assignment, Add Expense Entry, Add Service Entry, Add Issue, Add Inspection Submission, Add Work Order, Add Warranty, Add Service Reminder, Add Vehicle Renewal Reminder, Add Meter Entry. Add Issue mở form điền sẵn xe, lưu xong về trang sự cố. Các mục còn lại chưa mở (`Xem`). | P1 | [Lõi] | demo | Run-notes Fleet Map | `Chạy (vị trí giả lập)` | Lấy; quay lại bản đồ sau khi lưu |
| FR-fleetio-location-dispatch-030 | Độ tươi vị trí xe | Trạng thái Active, Idle, Stale hiện trên Status, tuổi vị trí trên dòng danh sách. Marker xe hình xe đen nhỏ; chú giải vẽ icon khác nhau cho 3 mức. | P0 | [Lõi] [Cấu hình] | demo | Run-notes Fleet Map | `Chạy (vị trí giả lập)` | Lấy mô hình; tách khỏi chạy, dừng. Ngưỡng là tham số mới, chưa có mã |
| FR-fleetio-location-dispatch-031 | Điểm mở bản đồ | Mở theo IP của máy, không tự thu về xe. Center on Default Location; Map Starting Location đổi được (`Xem`, không bấm vì đổi cài đặt người dùng). | P1 | [Cấu hình] | demo | Run-notes Câu hỏi còn lại | `Chạy (vị trí giả lập)` | Mở theo khung có xe |
| FR-fleetio-location-dispatch-032 | Location Exception Tracking | Biểu mẫu có cờ Enabled. Trên web không tạo được cờ: mọi phiếu `location_exception` = false. Không so giữa các phiếu. | P1 | [Cấu hình] | test | Run-notes Location Exception | `Chạy (vị trí giả lập)`, `Suy` phần nguyên nhân | Không dựa vào cách này để chống kiểm khống |
| FR-fleetio-location-dispatch-033 | API vị trí | `POST /vehicles/:id/location_entries` tạo mới, bản tương tự cho Equipment, khuyên Bulk API khi nhiều. | P2 | [Lõi] | test | developer.fleetio.com | `Docs` | Đọc khi thiết kế lớp kết nối GPS |

## 4. Non-Functional Requirements (NFR)

| ID | Category | Requirement | Priority | Acceptance |
|---|---|---|---|---|
| NFR-fleetio-location-dispatch-001 | độ tươi | Gần thời gian thực với 5 nhà cung cấp; nguồn khác hiện theo lần ghi đã có. | P1 | `Docs` |
| NFR-fleetio-location-dispatch-002 | trợ năng | Nhãn nút zoom phải đúng chức năng. | P1 | Fleetio không đạt: nút "+" có `aria-label` "Zoom Out", nút "−" có "Zoom In"; hành vi đúng theo hình (`Chạy`) |
| NFR-fleetio-location-dispatch-003 | độ trễ vị trí cho Invlogis | TBD — đội sản phẩm — khi chốt với EUP. | P1 | TBD |
| NFR-fleetio-location-dispatch-004 | minh bạch vị trí | Người dùng biết khi vị trí của họ được ghi. | P1 | Fleetio web không báo gì trong form (`Chạy`); yêu cầu quyền của trình duyệt chưa ghi nhận |
| NFR-fleetio-location-dispatch-005 | tin cậy log | Log chạy phải khớp kết quả thật. | P2 | Fleetio không đạt: E-fleetio-location-dispatch-011 (`Chạy (vị trí giả lập)`) |

## 5. Business Rules

| ID | Rule | Tầng | Trigger | Implements FR | Source |
|---|---|---|---|---|---|
| BR-fleetio-location-dispatch-001 | Xe chỉ hiện sau một hoạt động có vị trí hoặc khi có dữ liệu từ nguồn tích hợp. Bổ sung: phiếu kiểm trên web đủ làm xe lên marker. | [Lõi] | Có vị trí | FR-fleetio-location-dispatch-004, FR-fleetio-location-dispatch-023 | `Chạy` |
| BR-fleetio-location-dispatch-002 | App Fleetio Go chỉ hiện xe. | [Lõi] | Mở app | FR-fleetio-location-dispatch-002 | `Docs` |
| BR-fleetio-location-dispatch-003 | Vùng dùng để gắn lượt vị trí với địa điểm (`initial_place`) và làm căn cứ sự kiện, tự gán, cảnh báo. | [Cấu hình] | Có lượt vị trí | FR-fleetio-location-dispatch-010, FR-fleetio-location-dispatch-024 | `Chạy (vị trí giả lập)` |
| BR-fleetio-location-dispatch-004 | Ra khỏi vùng thì tự kết thúc lượt gán nếu việc bật ô tự động; nâng từ `Docs` lên chạy thật. | [Cấu hình] | Sự kiện vùng | FR-fleetio-location-dispatch-022 | `Chạy (vị trí giả lập)` |
| BR-fleetio-location-dispatch-005 | Xe đang có việc không gán thêm được: Assign mờ, chỉ còn Unassign. Không chuyển thẳng sang việc khác. | [Cấu hình] | Chọn xe đang gán | FR-fleetio-location-dispatch-016 | `Chạy` |
| BR-fleetio-location-dispatch-006 | Khoảng gán của một xe không được chồng khoảng cũ. | [Cấu hình] | Lưu lượt gán | FR-fleetio-location-dispatch-016 | `Chạy` |
| BR-fleetio-location-dispatch-007 | Giờ bắt đầu, kết thúc gán chỉ được là hiện tại hoặc quá khứ, vì lượt gán phản ánh việc thật. | [Cấu hình] | Lưu lượt gán | FR-fleetio-location-dispatch-016, FR-fleetio-location-dispatch-017 | `Chạy` |
| BR-fleetio-location-dispatch-008 | Giờ hoàn thành việc phải sau giờ bắt đầu của lượt đang chạy và không ở tương lai. | [Cấu hình] | Complete | FR-fleetio-location-dispatch-019 | `Chạy` |
| BR-fleetio-location-dispatch-009 | Hoàn thành việc tự kết thúc mọi lượt đang chạy cùng giờ, không có bước hỏi. | [Cấu hình] | Complete | FR-fleetio-location-dispatch-019 | `Chạy` |
| BR-fleetio-location-dispatch-010 | Độ tươi vị trí theo tuổi lần ghi gần nhất. Fleetio: Active trong 30 phút, Idle trong 1 giờ, Stale quá 1 giờ (tham số mới, chưa có mã). | [Lõi] [Cấu hình] | Hiện marker | FR-fleetio-location-dispatch-030 | `Chạy (vị trí giả lập)` |
| BR-fleetio-location-dispatch-011 | Đóng đa giác thì toạ độ thành tâm, Address đổi theo tâm, bán kính khoá với giá trị tự tính. | [Cấu hình] | Đóng đa giác | FR-fleetio-location-dispatch-025 | `Chạy` |
| BR-fleetio-location-dispatch-012 | Bán kính có danh sách gợi ý, nhận số khác. Fleetio: 100, 200, 500, 1000 m (tham số mới, chưa có mã). | [Cấu hình] | Chọn bán kính | FR-fleetio-location-dispatch-010 | `Chạy` |
| BR-fleetio-location-dispatch-013 | Máy chủ tin toạ độ trình duyệt gửi, không có kiểm tra phát hiện toạ độ giả. | [Lõi] | Nộp phiếu | FR-fleetio-location-dispatch-023 | `Chạy (vị trí giả lập)` |
| BR-fleetio-location-dispatch-014 | Location Exception không so giữa các phiếu: phiếu lệch xa phiếu trước vẫn không bị gắn cờ. | [Cấu hình] | Nộp phiếu | FR-fleetio-location-dispatch-032 | `Chạy (vị trí giả lập)` |
| BR-fleetio-location-dispatch-015 | Một lần ghi có thể sinh nhiều sự kiện: đi từ vùng A sang vùng B làm Automation chạy 2 lần. Hai lần ứng với ra A, vào B là `Suy`. | [Cấu hình] | Lần ghi vị trí | FR-fleetio-location-dispatch-011, FR-fleetio-location-dispatch-028 | `Chạy (vị trí giả lập)` |
| BR-fleetio-location-dispatch-016 | Phiếu ghi lại việc đang gán tại thời điểm nộp, sau đó mới xử lý kết thúc theo vùng: phiếu nộp ngoài vùng vẫn mang `job_assignment` của việc đó. | [Cấu hình] | Nộp phiếu | FR-fleetio-location-dispatch-022, FR-fleetio-location-dispatch-023 | `Chạy (vị trí giả lập)` |
| BR-fleetio-location-dispatch-017 | Alert Policy bắt buộc Which Vehicles, Recipients; chỉ người dùng có email được chọn. Mặc định gửi khi phát hiện, bật Receive as Summary để nhận tổng hợp hằng ngày của ngày trước. | [Cấu hình] | Lưu cảnh báo | FR-fleetio-location-dispatch-027 | `Xem` |
| BR-fleetio-location-dispatch-018 | Việc mới luôn Active, Start Date/Time tự lấy lúc tạo, không nhập trên form. | [Cấu hình] | Tạo việc | FR-fleetio-location-dispatch-015 | `Chạy` |
| BR-fleetio-location-dispatch-019 | Automation Geofence Event chỉ có trigger Created, chỉ hành động trên Vehicle. Không có điều kiện loại sự kiện thì chạy cả khi vào lẫn ra (`Suy`). | [Cấu hình] | Sự kiện vùng | FR-fleetio-location-dispatch-028 | `Chạy (vị trí giả lập)` |
| BR-fleetio-location-dispatch-020 | Web đọc vị trí một lần lúc khởi động app, không phải lúc mở form hay lúc lưu. Form không báo gì khi gửi. | [Lõi] | Khởi động app | FR-fleetio-location-dispatch-023 | `Chạy` |
| BR-fleetio-location-dispatch-021 | Đồng hồ trên phiếu kiểm theo lịch sử đồng hồ: báo phải nhỏ hơn số trong lịch sử dù dòng dưới ghi số cập nhật cuối lớn hơn. | [Cấu hình] | Nộp phiếu | FR-fleetio-location-dispatch-023 | `Chạy (vị trí giả lập)` |

## 6. Error Matrix

| Error ID | Title | Trigger | Severity | Related FR | Screen state | Recovery | Mức |
|---|---|---|---|---|---|---|---|
| E-fleetio-location-dispatch-001 | Không có kết quả | "No results found in this area. Try updating your filter criteria or moving the map to re-do your search." | minor | FR-fleetio-location-dispatch-001, FR-fleetio-location-dispatch-031 | Trạng thái rỗng | Đổi vùng, lọc, tìm ở ô Locate | `Chạy (vị trí giả lập)` |
| E-fleetio-location-dispatch-002 | Xe chưa có vị trí | "No current location information available for this Vehicle" | minor | FR-fleetio-location-dispatch-004 | Khối trên trang xe | Nộp phiếu có vị trí, hoặc chờ dữ liệu | `Xem` |
| E-fleetio-location-dispatch-003 | Bỏ trống trường bắt buộc của việc | Job Number: "can't be blank". Job Name cũng bắt buộc, câu chữ không ghi riêng | minor | FR-fleetio-location-dispatch-015 | Lỗi tại trường | Điền đủ | `Chạy` |
| E-fleetio-location-dispatch-004 | Giờ gán ở tương lai | "cannot be in the future" | minor | FR-fleetio-location-dispatch-016 | Lỗi trong hộp gán | Chọn giờ hiện tại hoặc quá khứ | `Chạy` |
| E-fleetio-location-dispatch-005 | Gán trùng khoảng cũ | "active Assignment overlaps with historical Assignment", kèm băng đỏ "TEST-XE-01 on TEST-01 TEST-Job-01 started at 11/03/2026 12:53 AM" | major | FR-fleetio-location-dispatch-016 | Băng đỏ trong hộp gán | Đổi giờ không chồng | `Chạy` |
| E-fleetio-location-dispatch-006 | Unassign khi ô giờ chưa có giá trị | Băng đỏ, không nói rõ lỗi gì (câu chữ không ghi lại) | major | FR-fleetio-location-dispatch-017 | Băng đỏ trong hộp | Bấm vào ô giờ để điền giờ hiện tại, bấm lại | `Chạy` |
| E-fleetio-location-dispatch-007 | Giờ hoàn thành trước giờ bắt đầu | "must be after active assignment start date/time" | minor | FR-fleetio-location-dispatch-019 | Lỗi trong hộp Complete | Chọn giờ sau | `Chạy` |
| E-fleetio-location-dispatch-008 | Giờ hoàn thành ở tương lai | "End date cannot be in the future" | minor | FR-fleetio-location-dispatch-019 | Lỗi trong hộp Complete | Chọn giờ hiện tại hoặc quá khứ | `Chạy` |
| E-fleetio-location-dispatch-009 | Xe đang có việc | Không có câu báo: Assign bị mờ | minor | FR-fleetio-location-dispatch-016 | Mục Actions mờ | Unassign trước rồi gán lại | `Chạy` |
| E-fleetio-location-dispatch-010 | Rời form địa điểm có thay đổi | Hộp "Leave site?" của trình duyệt; tab kẹt, phải đóng tab | minor | FR-fleetio-location-dispatch-010 | Hộp trình duyệt | Đóng tab | `Chạy` |
| E-fleetio-location-dispatch-011 | Log Automation mâu thuẫn | Run Result "No records changed"; bước `ActionSet` trạng thái `DNF`, "Automation Trigger has no action set", trong khi comment vẫn sinh | major | FR-fleetio-location-dispatch-028 | Màn Run Result | Chưa rõ; không tin log, kiểm bản ghi đích | `Chạy (vị trí giả lập)` |
| E-fleetio-location-dispatch-012 | Đồng hồ bị chặn trên phiếu | "must be less than 2,499 or marked as void" dù dòng dưới ghi "Last updated: 2,999 km (Today)" | major | FR-fleetio-location-dispatch-023 | Lỗi tại trường đồng hồ | Nhập số thấp hơn hoặc đánh dấu void | `Chạy (vị trí giả lập)` |

## 7. Success Criteria

| ID | Outcome nghiệp vụ | Đo bằng | Mốc đạt |
|---|---|---|---|
| SC-fleetio-location-dispatch-01 | Tìm được xe nhanh | Số thao tác từ mở bản đồ | TBD |
| SC-fleetio-location-dispatch-02 | Biết xe đang gần nơi nào | Có danh sách gần | Có sẵn |
| SC-fleetio-location-dispatch-03 | Biết vị trí còn tươi không | Tuổi vị trí trên dòng danh sách | Có sẵn |

## 8. Data Entities (tóm tắt — chi tiết ở erd.md)

Location Entry, Inspection Submission, Place, Geofence Event, Geofence Alert Policy, Automation, Job, Job Assignment. Xem [[docs/_research/fleetio/srs/fleetio-location-dispatch-erd.md|ERD]].

## 9. Flows (tóm tắt — chi tiết ở flows.md)

Xem [[docs/_research/fleetio/srs/fleetio-location-dispatch-flows.md|Flows]], [[docs/_research/fleetio/srs/fleetio-location-dispatch-states.md|States]], [[docs/_research/fleetio/srs/fleetio-location-dispatch-usecases.md|Use case]], [[docs/_research/fleetio/srs/fleetio-location-dispatch-userflow.md|User flow]].

## 10. Screens

Ảnh thật và bảng mô tả: [[docs/_research/fleetio/srs/fleetio-location-dispatch-screens.md|Màn hình]]. Không áp `CMP`, `GR` vì mô tả sản phẩm của bên khác.

## 11. Constraints, Dependencies & Assumptions

| Ràng buộc | Source / Owner |
|---|---|
| Tài khoản dùng thử không có thiết bị; xe có vị trí nhờ phiếu kiểm web, phần lớn là vị trí giả lập | Chạy thử 03/11/2026 |
| Chỉ có 2 xe TEST nên không kết luận được gom cụm | Chạy thử 03/11/2026 |
| Chưa kiểm Fleetio Go | Chạy thử 03/11/2026 |
| Kéo thả, Street View kết luận ở mức quan sát qua công cụ | Chạy thử 03/11/2026 |

| Giả định | Invalidate nếu sai |
|---|---|
| `GĐ` Invlogis dùng lớp kết nối nhà cung cấp GPS, EUP là kết nối đầu tiên | Phần nguồn vị trí phải viết lại |
| `GĐ` Sự kiện vùng với vị trí từ thiết bị hoạt động như với vị trí từ phiếu | Phần sự kiện vùng phải kiểm lại |

## 12. Open Questions

* [ ] OQ-1: Fleetio có gom cụm marker không? Trả lời một phần: zoom xa hết với 2 xe và 2 Place không gom, marker đè nhau; chưa đủ kết luận, cần nhiều xe hơn — Nguồn khách: không áp dụng
* [x] OQ-2: Hình dạng, màu marker theo trạng thái; cần tài khoản có thiết bị. Trả lời: marker hình xe đen nhỏ; chú giải có 3 icon theo độ tươi Active, Idle, Stale, không phải chạy hay dừng (`Chạy (vị trí giả lập)`) — Nguồn khách: không áp dụng
* [ ] OQ-3: Lịch sử vị trí xe, vị trí điện thoại lái xe: thời hạn lưu, ai được xem, thông báo thế nào? Cần pháp chế xác nhận. Ghi nhận: web gửi vị trí thật của trình duyệt lên máy chủ mà không báo gì trong form (`Chạy`) — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-4: Fleetio Go có ghi vị trí từng mục kiểm và tạo Location Exception thật không? — Nguồn khách: không áp dụng
* [ ] OQ-5: Street View hoạt động thế nào? Kéo Pegman bằng công cụ không ăn — Nguồn khách: không áp dụng
* [ ] OQ-6: "Update list when map moves" khác gì khi kéo bản đồ tay? Chưa thử — Nguồn khách: không áp dụng
* [ ] OQ-7: Vì sao trang xe ghi "Idle" khi vị trí mới 25 giây trong lúc bản đồ "Active"? — Nguồn khách: không áp dụng
* [ ] OQ-8: Có chống nhiễu ở mép vùng không, sự kiện vùng dựa vào lần ghi nào, có áp cho vị trí từ thiết bị như vậy không? — Nguồn khách: không áp dụng
* [ ] OQ-9: Tự gán xử lý thế nào khi xe đang có việc khác, khi xe đã ở trong vùng lúc bật ô, khi việc đã hoàn thành? — Nguồn khách: không áp dụng
* [ ] OQ-10: Đa giác 2 đỉnh có lưu được không? — Nguồn khách: không áp dụng
* [ ] OQ-11: Vì sao log Automation ghi `DNF` trong khi hành động vẫn chạy? — Nguồn khách: không áp dụng
* [ ] OQ-12: Geofence Alert Policy gửi thật ra sao, có lặp lại khi xe ở trong vùng lâu không? Chưa lưu vì chỉ có hành động gửi email — Nguồn khách: không áp dụng
* [ ] OQ-13: Phiếu #125988723 không có vị trí vì sao; Delete lượt gán, Edit, Delete việc có hệ quả gì; việc Completed có mở lại được không? — Nguồn khách: không áp dụng

## 13. Ma trận case

Mọi case lấy từ [[docs/_research/fleetio/run-notes/location-dispatch.md|ghi chú chạy thử]]. In đậm là điều **không** xảy ra.

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| Tạo Place vùng tròn | Add Place, gõ tên, toạ độ, chọn "200 meters", Save Place | "Place was successfully created" | `Chạy` |
| Gõ toạ độ trên form | Nhập Latitude, Longitude | Address tự điền theo địa chỉ ngược, bản đồ tự chuyển đến | `Chạy` |
| Gõ bán kính không có trong danh sách | Edit, gõ 350, Enter, lưu | Hiện lựa chọn "350 meters", lưu được, "Place was successfully updated" | `Chạy` |
| Đổi bán kính chưa lưu | Chọn giá trị khác trên form | Vòng tròn đổi ngay | `Chạy` |
| Bấm điểm trên bản đồ ở chế độ thường | Form địa điểm, không chọn công cụ vẽ | Đặt lại pin; Address, toạ độ đổi theo; Name giữ nguyên | `Chạy` |
| Đổi toạ độ sau khi đã có pin | Form địa điểm | Một pin thứ hai màu đỏ còn lại ở điểm cũ | `Chạy` |
| Mở form địa điểm mới | Chưa nhập gì | Bản đồ mở chưa đúng nơi cần khai | `Chạy` |
| Đóng đa giác 4 đỉnh | Bấm đa giác, 4 đỉnh, bấm lại đỉnh đầu | Toạ độ thay bằng tâm, Address đổi theo tâm, Radius khoá xám "465 meters"; lưu được | `Chạy` |
| Xem Place đa giác | Trang chi tiết | Vẫn ghi "Geofence Radius 465 meters"; bản đồ vẽ đúng đa giác | `Chạy` |
| Đa giác 2 đỉnh | Vẽ thành đoạn thẳng | Form **không chặn**, radius tự tính "431 meters". Chưa thử lưu, đã huỷ | `Chạy` |
| Rời form có thay đổi | Đổi trang | Hộp "Leave site?", tab kẹt (E-010) | `Chạy` |
| Mở Add Alert Policy | Đọc rồi Cancel | Thấy 4 giá trị Trigger, các trường; không lưu, **không gửi email nào** | `Xem` |
| Add Job khi chưa có việc | Màn trống | Có nút giữa và nút góc phải, cùng mở một form; nút giữa mất khi đã có việc | `Chạy` |
| Nộp form việc trống | Add Job | "can't be blank" (E-003) | `Chạy` |
| Tạo việc, tắt tự động | Job Number, Job Name, Place | "Job created successfully"; Start Date/Time tự lấy lúc tạo; Auto-Tracking Off | `Chạy` |
| Tạo việc, bật tự động | Thêm tick ô tự động | Tạo được; hoạt động xem các case vùng bên dưới | `Chạy` |
| Gán xe hiện tại | Tích xe, Actions, Assign | "Job assignments created successfully"; thẻ xe "On job: 0m", số đếm cột đổi | `Chạy` |
| Gán giờ tương lai | Hộp Add Job Assignments | "cannot be in the future" (E-004) | `Chạy` |
| Gán xe đang có việc | Tích xe đang gán | Assign mờ, chỉ còn Unassign (E-009). **Không có** chuyển thẳng sang việc khác | `Chạy` |
| Gán lại giờ trùng khoảng cũ | Sau khi đã kết thúc lượt | "active Assignment overlaps with historical Assignment" kèm băng đỏ (E-005) | `Chạy` |
| Kéo thẻ xe sang cột khác | Thao tác kéo chuột | **Không hoạt động**, chỉ bôi đen chữ. Kết luận ở mức quan sát qua công cụ | `Chạy` |
| Unassign, không bấm ô giờ | Ô hiện chữ mờ, chưa có giá trị | Băng đỏ, không rõ lỗi (E-006) | `Chạy` |
| Unassign, đã bấm ô giờ | Giờ hiện tại được điền thật | "Vehicles successfully unassigned from Jobs"; xe về Unassigned | `Chạy` |
| Edit lượt gán | Menu dòng xe | Job, Vehicle khoá; chỉ sửa Start Date/Time | `Chạy` |
| Delete lượt gán; Edit, Delete việc | Menu dòng xe, menu cột | Thấy mục menu, **chưa bấm** | `Xem` |
| Complete khi còn xe đang gán | Hộp Complete Job | "Job completed successfully"; xe tự kết thúc cùng giờ (End 12:57am). **Không có** bước hỏi | `Chạy` |
| Complete, giờ trước khi bắt đầu | Hộp Complete Job | "must be after active assignment start date/time" (E-007) | `Chạy` |
| Complete, giờ tương lai | Hộp Complete Job | "End date cannot be in the future" (E-008) | `Chạy` |
| Tìm trên bảng việc | Gõ tên xe | Lọc theo tên xe, ẩn cột việc không có xe khớp | `Chạy` |
| Múi giờ máy khác cài đặt | Máy khác múi giờ tài khoản | Giờ hiển thị theo máy, có banner cảnh báo lệch | `Chạy` |
| Xem lịch sử gán thủ công | Job Assignment History | 2 dòng thật 2m 26s và 1m, Added = "Manual" | `Chạy` |
| Phiếu dầu, phiếu dịch vụ | Đọc hết trường trên form web | **Không có ô vị trí** ở cả hai; không có đường sinh vị trí trên web | `Chạy` |
| Nộp phiếu kiểm web, trình duyệt có quyền định vị | Phiếu #126053573 | Gửi vị trí thật của máy, Source "Fleetio Web App", sinh Location Entry, xe lên marker ngay. Câu "chỉ có điện thoại hoặc thiết bị mới có vị trí" là sai | `Chạy` |
| Phiếu kiểm không có vị trí | Phiếu #125988723 | Không sinh vị trí. Lý do chưa rõ, có thể trình duyệt chưa cấp quyền (`Suy`) | `Chạy` |
| Thời điểm đọc vị trí | Theo dõi lệnh gọi định vị | Đúng 1 lần lúc khởi động app, **không** lúc mở form, **không** lúc lưu | `Chạy` |
| Form có báo đang gửi vị trí không | Nộp phiếu kiểm web | **Không báo gì** trong form | `Chạy` |
| Nộp phiếu với toạ độ giả | Phiếu #126053906 | Máy chủ lưu đúng toạ độ gửi lên, **không có** kiểm tra nào phát hiện | `Chạy (vị trí giả lập)` |
| Địa chỉ của Location Entry | Ngay sau khi nộp | Lúc đầu `address` rỗng, có địa chỉ sau khoảng 1 phút | `Chạy (vị trí giả lập)` |
| Lần ghi trong vùng Place | Phiếu trong TEST-Cang-Cat-Lai | `location_entry.initial_place` = Place đó; trang phiếu có bản đồ nhỏ, chấm xanh | `Chạy (vị trí giả lập)` |
| Vào vùng, việc bật tự động | Phiếu trong đa giác TEST-Bai-Xe | Lịch sử có dòng mới Added = "Geofence", Active; thẻ xe có chip "Geofence" | `Chạy (vị trí giả lập)` |
| Ra vùng, lượt tự gán đang chạy | Phiếu ngoài đa giác | Dòng đó có End Date, Time on Job 59s, xe về Unassigned | `Chạy (vị trí giả lập)` |
| Phiếu nộp ngoài vùng | Phiếu làm kết thúc lượt gán | Phiếu vẫn mang `job_assignment` là việc đó | `Chạy (vị trí giả lập)` |
| Đi từ vùng A sang vùng B | Phiếu #126055155 | Automation chạy 2 lần, Total Runs 2, Successful 2, 2 comment. Ứng với ra A, vào B là `Suy`; "Current Job" thành TEST-02 | `Chạy (vị trí giả lập)` |
| Chọn Record Type Geofence Event | Automation mới | Trigger Type chỉ có "Created"; Event Type đúng 2 giá trị Entered, Exited | `Chạy (vị trí giả lập)` |
| Hành động trên Automation vùng | Chọn hành động | Chỉ trên Vehicle: Update Field, Add Comment, Send Email. Chỉ chạy Add Comment, **không gửi email** | `Chạy (vị trí giả lập)` |
| Xem Run Result sau khi chạy | Automation đã chạy | "No records changed", bước `ActionSet` `DNF` dù comment đã thêm (E-011) | `Chạy (vị trí giả lập)` |
| Run Result có ghi loại sự kiện, Place không | Màn Run Result | **Không ghi** | `Chạy (vị trí giả lập)` |
| Tìm danh sách sự kiện vùng | Location Entries của Place, danh sách Places, Manage Columns | **Không có** màn riêng, không có cột Geofence Event | `Chạy (vị trí giả lập)` |
| Tắt Automation | Sau khi kiểm | "Automation disabled" | `Chạy` |
| Pre-trip đủ mục, biểu mẫu bật Location Exception | Phiếu #126054432 | `location_exception` = false; gói tin chỉ 1 cặp toạ độ cấp phiếu, mục kiểm không có toạ độ, `starting_latitude` rỗng | `Chạy (vị trí giả lập)` |
| 6 phiếu Quick check cách xa nhau | Cách từ 1,4 km đến khoảng 1.100 km | Mọi phiếu `location_exception` = false, **không so** giữa các phiếu | `Chạy (vị trí giả lập)` |
| Chặn phiếu toạ độ giả | Nộp phiếu | **Không chặn được**. Chỉ đồng hồ báo lỗi (E-012), không liên quan vị trí | `Chạy (vị trí giả lập)` |
| Mở Fleet Map | Xe ở xa điểm mở | Tâm theo IP, không tự thu về xe, "No results found in this area" | `Chạy (vị trí giả lập)` |
| Khung có 2 xe | Tab Vehicles | "2 results", sắp Distance, dòng có người lái hoặc "Unassigned", tuổi "3m ago" | `Chạy (vị trí giả lập)` |
| Bấm marker hoặc dòng | Chọn xe | **Không có popup**; panel trái đổi sang xe, marker gắn nhãn tên | `Chạy (vị trí giả lập)` |
| Tab Nearby của xe | Mở tab | PLACES, VENDORS mặc định ẩn; Show Places hiện dòng có khoảng cách: 0, 3.33km, 1.44km, 1.91km | `Chạy (vị trí giả lập)` |
| Rê chuột dòng Place | Tab Nearby | Đường thẳng nét đứt từ xe tới Place, marker xe đổi thành marker Place trong lúc rê | `Chạy (vị trí giả lập)` |
| Quick Add, Add Issue | Nút Add trên panel | Form điền sẵn xe, tạo Issue #39, lưu xong về trang sự cố, **rời bản đồ** | `Chạy (vị trí giả lập)` |
| Bỏ tích Update list when map moves | Bấm Center on Default Location | Danh sách vẫn ra "No results found in this area"; **không thấy khác biệt rõ**; chưa thử kéo tay | `Chạy (vị trí giả lập)` |
| Đổi Map Options | Satellite, Grayscale, Labels | Chạy được; tải lại vẫn giữ, lưu theo người dùng; Labels đè nhau khi Place gần | `Chạy (vị trí giả lập)` |
| Place đa giác trên Fleet Map | Bật Places | Đúng hình; tâm là marker tròn xanh | `Chạy (vị trí giả lập)` |
| Xe trùng toạ độ tâm Place | Xe trong vùng | Tâm Place che marker xe | `Chạy (vị trí giả lập)` |
| Zoom xa hết | 2 xe, 2 Place | **Không gom cụm**, marker đè nhau. Không đủ kết luận với 2 xe | `Chạy (vị trí giả lập)` |
| Độ tươi trên trang xe | Vị trí mới 25 giây | Trang xe có lúc ghi "Idle", bản đồ vẫn "Active". Chưa rõ lý do | `Chạy (vị trí giả lập)` |
| Mở Map Legend | Nút chú giải | Active, Idle, Stale, Place và 5 loại cửa hàng, nhà cung cấp | `Chạy (vị trí giả lập)` |
| Nút zoom | Đọc nhãn trợ năng, bấm | "+" có nhãn "Zoom Out", "−" có "Zoom In"; hành vi đúng theo hình | `Chạy` |
| Street View | Kéo Pegman bằng công cụ | Không ăn, **không vào được** chế độ này | `Xem` |
| Map Starting Location | Thấy 2 lựa chọn | Không bấm vì đổi cài đặt người dùng | `Xem` |
| API tạo vị trí | Đọc tài liệu | 201 khi tạo mới, 422 nếu không hợp lệ; tên trường toạ độ không lộ ở trang tóm tắt; **không gọi thử** | `Docs` |
