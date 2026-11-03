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

> Mô tả **Fleetio đang làm gì**, kèm đề xuất cho Invlogis chưa chốt. **Không làm mẫu điều vận.** Kết quả về marker và sự kiện vùng phần lớn dùng vị trí giả lập gửi qua phiếu kiểm tra web; vị trí từ phiếu dầu, phiếu dịch vụ có nhà cung cấp là dữ liệu chạy thật; Fleetio Go mới kiểm một phiếu không vi phạm; chưa kiểm với thiết bị thật.

**Nhãn bằng chứng:** `Chạy` đã thao tác, không phụ thuộc vị trí giả lập · `Chạy (vị trí giả lập)` đã thao tác, dữ liệu vị trí là giả lập · `Chạy (Fleetio Go)` phiếu nộp thật trên app, chỉ đọc kết quả của chính phiếu · `Xem` thấy trên giao diện · `Docs` tài liệu công khai · `Suy` suy ra · `GĐ` giả định.

## 1. Scope

**Trong phạm vi:** Fleet Map, Places, Geofence, Geofence Alert Policy, sự kiện vùng và Automation theo sự kiện vùng, Location Entry từ phiếu kiểm và phiếu dầu, Location History của xe, Location Exception, Jobs, Job Assignment.

**Ngoài phạm vi:** mạng lưới xưởng Mỹ; Lệnh vận tải của Invlogis; thiết bị định vị thật (tài khoản dùng thử không có). Fleetio Go chỉ trong phạm vi vị trí từng mục của phiếu kiểm, phần còn lại của app chưa kiểm.

## 2. Actors & Stakeholders

| Actor | Loại | Mục tiêu | Trong scope? | Tương đương Invlogis |
|---|---|---|---|---|
| Fleet Manager | Người | Xem xe, tìm nơi gần xe, gán việc | Có | Điều vận, Quản lý phương tiện |
| Administrator | Người | Khai địa điểm, vùng, Automation, cảnh báo | Có | Admin |
| Người kiểm tra xe | Người | Nộp phiếu, vô tình gửi vị trí | Có | Lái xe |
| Người nhập phiếu dầu | Người | Ghi đổ dầu, vô tình tạo vị trí xe khi chọn nhà cung cấp | Có | Lái xe, Kế toán đội xe |
| Telematics | Ngoài | Đẩy vị trí | Có, chỉ `Docs` | EUP |
| Hệ thống ngoài qua API | Ngoài | Tạo Location Entry | Có, chỉ `Docs` | Lớp kết nối GPS |

## 3. Functional Requirements (FR)

| ID | Title | Description | Priority | Tầng | Verify by | Source | Mức | Đề xuất Invlogis |
|---|---|---|---|---|---|---|---|---|
| FR-fleetio-location-dispatch-001 | Bản đồ cạnh danh sách | Danh sách Nearby có tab Vehicles, Places, đếm kết quả, sắp theo Distance; dòng ghi tên xe, người lái ("Unassigned" nếu chưa gán), tuổi vị trí ("3m ago"); ô "Update list when map moves" chỉ chặn cập nhật khi kéo tay, chọn từ ô tìm vẫn cập nhật, tick lại là áp ngay. Mốc khoảng cách là tâm bản đồ (`Suy`, không đo được công thức). | P0 | [Lõi] | demo | Run-notes Fleet Map | `Chạy (vị trí giả lập)` | Lấy cho `vehicle-telematics` |
| FR-fleetio-location-dispatch-002 | Lớp bản đồ | Vehicles, Places, Vendors bật tắt. Bật Vendors thêm marker nhà cung cấp và tab Places, Vendors ở danh sách. Tắt Vehicles có tác dụng thật: marker và cả tab danh sách biến mất; tắt hết còn "No results found in this area". Tải lại trang thì lớp về mặc định: Vehicles bật, Places, Vendors tắt. Không thấy nút Shops riêng; chú giải có Preferred Shop, Premier Fleetio Vendor, In-Network Shop, Out-of-Network Shop, Vendor; phần Shops giữ theo tài liệu hãng. Trong panel xe, PLACES, VENDORS mặc định ẩn, có nút "Show Places", "Show Vendors". | P0 | [Lõi] | demo | Run-notes Fleet Map, tài liệu hãng | `Chạy` một phần lượt 4: Tắt Vehicles chạy; Shops không có nút, giữ Docs | Lấy, thay Shops bằng cây dầu, cảng |
| FR-fleetio-location-dispatch-003 | Tải theo khung nhìn | Lấy vị trí theo khung đang xem, gọi lại khi đổi khung. | P0 | [Lõi] | test | Lần xem trực tiếp đầu | `Chạy` | Lấy |
| FR-fleetio-location-dispatch-004 | Nguồn vị trí | Từ tích hợp (`Docs`), API (`Docs`), từ phiếu kiểm tra (`Chạy`), từ phiếu dầu có chọn nhà cung cấp (`Chạy`, chi tiết ở FR-fleetio-location-dispatch-034). **Đã sửa lượt 3:** phiếu dầu và phiếu dịch vụ không có ô vị trí, nhưng chọn nhà cung cấp trên phiếu dầu tạo vị trí xe tại địa chỉ nhà cung cấp, không cần thiết bị hay tích hợp, form không báo. Bộ lọc Location Entry Type có đúng Fuel Entry, Service Entry, Inspection. **Đã sửa lượt 4:** phiếu dịch vụ có nhà cung cấp phân loại Service cũng sinh vị trí theo cùng cơ chế (`Chạy`, chi tiết ở FR-fleetio-location-dispatch-038), đủ 3 loại của bộ lọc đều đã thấy thật. | P1 | [Lõi] | demo | Run-notes Vị trí không cần thiết bị; Lượt 3, Lượt 4 Nguồn vị trí | `Chạy` một phần lượt 4: Phiếu dầu, phiếu dịch vụ tạo vị trí; tích hợp, API giữ Docs | Lấy làm dự phòng khi mất GPS, ghi rõ nguồn là địa chỉ khai |
| FR-fleetio-location-dispatch-005 | Tìm và lọc | Ô "Locate vehicles, places, vendors on map..." tìm cả nhà cung cấp, xe, Place ("10 results available for search term TEST"), xếp nhà cung cấp trước, khớp mờ; xe chưa có vị trí vẫn nằm trong kết quả. Filters có VEHICLES: Vehicle Type, Vehicle Group, Vehicle Status, Vehicle Operator, Vehicle Assigned, Vehicle GPS Integration, Vehicle GPS Device Assigned, Vehicle Has Overdue Service Reminders; VENDORS: Classification; nút Cancel, Apply; huy hiệu số bộ lọc trên nút. Bộ lọc mất khi tải lại trang. | P0 | [Lõi] | demo | Run-notes Fleet Map; Lượt 3 Tìm và lọc | `Chạy` lượt 3: Đủ 9 bộ lọc; tải lại thì mất lọc | Lấy; giữ bộ lọc khi tải lại, tên khớp đúng lên đầu kết quả |
| FR-fleetio-location-dispatch-006 | Chi tiết khi chọn xe | Bấm marker hoặc dòng: không popup, panel trái đổi sang xe, marker gắn nhãn tên. Tab Overview có Alerts (Open Issues, Service Reminders, Incomplete Work Orders), Last Known Location (Status, Last Updated, Where, Source trỏ về bản ghi sinh vị trí: "Inspection Submission #...", "Fuel Entry #..."), Details; tab Nearby. Căn giữa xe: `Docs`. | P1 | [Lõi] | demo | Run-notes Fleet Map | `Chạy (vị trí giả lập)` | Lấy |
| FR-fleetio-location-dispatch-007 | Quan hệ gần | Dòng Place trong Nearby có khoảng cách. Rê chuột vẽ đường thẳng nét đứt từ xe tới Place, marker xe đổi thành marker Place trong lúc rê. | P2 | [Lõi] | demo | Run-notes Fleet Map | `Chạy (vị trí giả lập)` | Cân nhắc; không lấy việc đổi marker xe |
| FR-fleetio-location-dispatch-008 | Tuỳ chọn bản đồ | **Đã sửa tên:** Default (không phải Standard), Satellite, Grayscale; Labels hiện tên Place; Set Label Options (FR-fleetio-location-dispatch-035); lưu theo người dùng, tải lại vẫn giữ. Menu chia 3 nhóm MAP TYPE, MAP DETAILS, MAP STARTING LOCATION. Map Starting Location ghi tên nơi mở đầu, mặc định là thành phố theo IP. Use Current Map Center: toast "Map Preferences Updated", dòng này đổi sang tên vùng đang xem; Reset to Default trả lại (`Chạy`). Street View: có Pegman, kéo bằng công cụ 2 lượt đều không vào được chế độ này, không thử nữa (`Xem`). | P1 | [Cấu hình] | demo | Run-notes Fleet Map | `Chạy` một phần lượt 4: Nhãn, vị trí mở đầu chạy; Street View không kéo được | Lấy |
| FR-fleetio-location-dispatch-009 | Chú giải | **Đã sửa nghĩa:** Map Legend có Active, Idle, Stale là độ tươi vị trí, không phải xe chạy, nhàn rỗi; Place là tâm vùng; Preferred Shop, Premier Fleetio Vendor, In-Network Shop, Out-of-Network Shop, Vendor. | P1 | [Lõi] | demo | Run-notes Fleet Map | `Chạy (vị trí giả lập)` | Lấy cách làm chú giải; BL-382 cần bộ riêng có chạy, dừng |
| FR-fleetio-location-dispatch-010 | Địa điểm | Tên, mô tả, địa chỉ, toạ độ, bán kính. Gõ toạ độ thì Address tự điền theo địa chỉ ngược, bản đồ tự chuyển. Vòng tròn đổi ngay khi chọn bán kính, chưa cần lưu. Bấm bản đồ ở chế độ thường đặt lại pin. | P1 | [Cấu hình] | demo | Run-notes Tạo Place | `Chạy` | Lấy cho `location-catalog`; bỏ việc bấm bản đồ đổi pin ngoài ý muốn |
| FR-fleetio-location-dispatch-011 | Sự kiện vùng | Hai loại Entered, Exited, sinh khi vị trí mới đổi quan hệ với vùng. Dùng làm Record Type của Automation. Không có màn danh sách riêng. | P1 | [Cấu hình] | test | Run-notes Sự kiện vùng | `Chạy (vị trí giả lập)` | Đối chiếu `vehicle-telematics`; thêm nhật ký vào, ra vùng |
| FR-fleetio-location-dispatch-012 | Gán xe vào việc | Tạo việc, gán xe, tính thời gian trên việc; tự tạo và kết thúc gán theo vùng. Chi tiết tách ở FR 014 đến 022. | P2 | [Cấu hình] | demo | Run-notes Việc | `Chạy`, `Chạy (vị trí giả lập)` phần tự gán | Không lấy cho điều vận |
| FR-fleetio-location-dispatch-013 | Lịch sử vị trí | Tab Location History trên xe, mở từ More. Có ô Search, "Location Entry Date", "Location Entry Type" (Fuel Entry, Service Entry, Inspection), "Sort: Date - Newest First"; danh sách trái gồm icon loại, ngày, địa chỉ; bản đồ phải; phân trang "Page 1 of 1", Fleetio: 30 dòng mỗi trang. Xe chưa có vị trí: "No results found." | P1 | [Lõi] | demo | Lần xem trực tiếp đầu; Lượt 3 Lịch sử vị trí | `Chạy` lượt 3: Tab, 3 loại nguồn, bộ lọc | Lấy |
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
| FR-fleetio-location-dispatch-030 | Độ tươi vị trí xe | Trạng thái Active, Idle, Stale hiện trên Status, tuổi vị trí trên dòng danh sách. Marker xe hình xe đen nhỏ; chú giải vẽ icon khác nhau cho 3 mức. Panel một xe có vị trí từ phiếu dầu đã ghi Status "Stale" (`Chạy`). | P0 | [Lõi] [Cấu hình] | demo | Run-notes Fleet Map | `Chạy (vị trí giả lập)` | Lấy mô hình; tách khỏi chạy, dừng. Ngưỡng là tham số mới, chưa có mã |
| FR-fleetio-location-dispatch-031 | Điểm mở bản đồ | Mở theo IP của máy, không tự thu về xe. Center on Default Location; Map Starting Location đổi được bằng Use Current Map Center, trả lại bằng Reset to Default (`Chạy`, đã trả lại). | P1 | [Cấu hình] | demo | Run-notes Câu hỏi còn lại | `Chạy (vị trí giả lập)` | Mở theo khung có xe |
| FR-fleetio-location-dispatch-032 | Location Exception Tracking | Biểu mẫu có cờ Enabled. Trên web không tạo được cờ: mọi phiếu `location_exception` = false. Không so giữa các phiếu. Fleetio Go ghi toạ độ từng mục; ca lệch tối đa 37 m không bị gắn cờ, chưa có ca dương (FR-fleetio-location-dispatch-037). | P1 | [Cấu hình] | test | Run-notes Location Exception, #126102722 | `Chạy (vị trí giả lập)`, `Chạy (Fleetio Go)` ca không vi phạm | Không dựa vào cách này để chống kiểm khống |
| FR-fleetio-location-dispatch-033 | API vị trí | `POST /vehicles/:id/location_entries` tạo mới, bản tương tự cho Equipment, khuyên Bulk API khi nhiều. | P2 | [Lõi] | test | developer.fleetio.com | `Docs` | Đọc khi thiết kế lớp kết nối GPS |
| FR-fleetio-location-dispatch-034 | Vị trí từ phiếu dầu có nhà cung cấp | Chọn nhà cung cấp trên phiếu dầu thì sinh Location Entry loại Fuel Entry tại địa chỉ nhà cung cấp, cùng giờ với phiếu. Source của Last Known Location trỏ về phiếu, xe lên Fleet Map. Form không có ô vị trí, không báo gì. Phiếu không có nhà cung cấp không thấy sinh vị trí (`Suy`). Địa chỉ nhà cung cấp giả vẫn quy được ra một điểm, có thể ở nước khác, không báo độ tin cậy. | P1 | [Lõi] | test | Run-notes Lượt 3 Nguồn vị trí | `Chạy` | Cân nhắc làm dự phòng khi mất GPS; ghi rõ "vị trí khai", không coi là vị trí xe thật |
| FR-fleetio-location-dispatch-035 | Nhãn marker xe | Set Label Options mở hộp một ô "Vehicle Marker Label" (đang Name), chú thích "Select field to display for Vehicle map marker labels. Falls back to Vehicle Name if selected field value is empty/blank.", nút Cancel, Save. 5 giá trị: Name, VIN/SN, Vehicle Type, License Plate, "Year, Make, Model". Lưu VIN/SN: xe có VIN hiện số VIN, xe không có hiện tên; tải lại vẫn giữ, tức lưu theo người dùng (`Chạy` lượt 4, đã trả về Name). | P2 | [Cấu hình] | demo | Run-notes Lượt 3, Lượt 4 Tuỳ chọn bản đồ | `Chạy` lượt 4: Đổi nhãn, trả về Name | Lấy cho `vehicle-telematics`; nhãn chọn được theo trường của xe |
| FR-fleetio-location-dispatch-036 | Marker không gom cụm | Marker hiện riêng từng điểm ở mọi mức zoom đã thử, đè nhau khi gần; không có marker dạng số. Đã đếm tới 15 nhà cung cấp và 4 xe. | P1 | [Lõi] | demo | Run-notes Lượt 3 Gom cụm marker | `Chạy` một phần: 15 nhà cung cấp, 4 xe; chưa biết ngưỡng lớn hơn | Đội xe lớn cần gom cụm; không học theo mức đã đo |
| FR-fleetio-location-dispatch-037 | Vị trí từng mục từ Fleetio Go | Phiếu nộp trên app có `submitted_from` = Fleetio Go; mỗi mục kiểm có cặp `latitude`, `longitude` riêng (21/21 mục, 7 điểm, cách nhau tối đa 37 m); phiếu có 2 chỉ báo `are_items_too_close`, `items_completed_too_far_away_count`. `starting_latitude` vẫn rỗng dù phiếu có giờ bắt đầu. | P1 | [Cấu hình] | test | Run-notes Location Exception trên Fleetio Go | `Chạy (Fleetio Go)` ca không vi phạm | Học mức dữ liệu theo từng mục; cần ca dương trước khi rút ngưỡng |
| FR-fleetio-location-dispatch-038 | Vị trí từ phiếu dịch vụ có nhà cung cấp | Chọn nhà cung cấp phân loại Service trên phiếu dịch vụ thì sinh Location Entry loại Service Entry, cùng giờ phiếu, tại vị trí quy từ địa chỉ nhà cung cấp; đứng trên dòng Fuel Entry cũ ở Location History. Form không có ô vị trí, không báo gì. Cùng cơ chế với phiếu dầu. | P1 | [Lõi] | test | Run-notes Lượt 4 Nguồn vị trí | `Chạy` | Như FR-fleetio-location-dispatch-034; kiểm địa chỉ trước khi dùng làm vị trí xe |

## 4. Non-Functional Requirements (NFR)

| ID | Category | Requirement | Priority | Acceptance |
|---|---|---|---|---|
| NFR-fleetio-location-dispatch-001 | độ tươi | Gần thời gian thực với 5 nhà cung cấp; nguồn khác hiện theo lần ghi đã có. | P1 | `Docs` |
| NFR-fleetio-location-dispatch-002 | trợ năng | Nhãn nút zoom phải đúng chức năng. | P1 | Fleetio không đạt: nút "+" có `aria-label` "Zoom Out", nút "−" có "Zoom In"; hành vi đúng theo hình (`Chạy`) |
| NFR-fleetio-location-dispatch-003 | độ trễ vị trí cho Invlogis | TBD — đội sản phẩm — khi chốt với EUP. | P1 | TBD |
| NFR-fleetio-location-dispatch-004 | minh bạch vị trí | Người dùng biết khi vị trí của họ được ghi. | P1 | Fleetio web không báo gì trong form phiếu kiểm và phiếu dầu có nhà cung cấp (`Chạy`); yêu cầu quyền của trình duyệt chưa ghi nhận |
| NFR-fleetio-location-dispatch-005 | tin cậy log | Log chạy phải khớp kết quả thật. | P2 | Fleetio không đạt: E-fleetio-location-dispatch-011 (`Chạy (vị trí giả lập)`) |

## 5. Business Rules

| ID | Rule | Tầng | Trigger | Implements FR | Source |
|---|---|---|---|---|---|
| BR-fleetio-location-dispatch-001 | Xe chỉ hiện sau một hoạt động có vị trí hoặc khi có dữ liệu từ nguồn tích hợp. Bổ sung: phiếu kiểm trên web, phiếu dầu có nhà cung cấp đều đủ làm xe lên marker. | [Lõi] | Có vị trí | FR-fleetio-location-dispatch-004, FR-fleetio-location-dispatch-023, FR-fleetio-location-dispatch-034 | `Chạy` |
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
| BR-fleetio-location-dispatch-022 | Chọn nhà cung cấp trên phiếu dầu là sinh vị trí xe tại địa chỉ nhà cung cấp, không hỏi, không báo. Phiếu không có nhà cung cấp không sinh: 14 phiếu dầu của một xe chỉ có 1 lần ghi, cùng giờ phiếu có nhà cung cấp (phần không sinh là `Suy`). | [Lõi] | Lưu phiếu dầu | FR-fleetio-location-dispatch-004, FR-fleetio-location-dispatch-034 | `Chạy` |
| BR-fleetio-location-dispatch-023 | Vị trí khai từ nhà cung cấp được đối xử như mọi lần ghi khác: thành Last Known Location, xe hiện như đang ở đó, không có dấu phân biệt ngoài Source và loại. | [Lõi] | Có lần ghi Fuel Entry | FR-fleetio-location-dispatch-034 | `Chạy` |
| BR-fleetio-location-dispatch-024 | Form Service Entry chỉ cho chọn nhà cung cấp có phân loại Service; tên không khớp chỉ có lựa chọn tạo mới. | [Cấu hình] | Chọn nhà cung cấp | FR-fleetio-location-dispatch-004 | `Chạy` |
| BR-fleetio-location-dispatch-025 | Ô "Update list when map moves" chỉ chặn cập nhật khi kéo tay. Chọn từ ô tìm vẫn cập nhật danh sách theo vùng mới; tick lại là áp ngay, không cần kéo. | [Lõi] | Đổi khung nhìn | FR-fleetio-location-dispatch-001 | `Chạy` |
| BR-fleetio-location-dispatch-026 | Bộ lọc Fleet Map không giữ qua tải lại trang, trong khi Map Options giữ theo người dùng. | [Lõi] | Tải lại trang | FR-fleetio-location-dispatch-005, FR-fleetio-location-dispatch-008 | `Chạy` |
| BR-fleetio-location-dispatch-027 | Ô tìm bản đồ khớp mờ, xếp nhà cung cấp trước xe; Enter chọn dòng đầu. | [Lõi] | Tìm trên bản đồ | FR-fleetio-location-dispatch-005 | `Chạy` |
| BR-fleetio-location-dispatch-028 | Xe chưa có vị trí vẫn nằm trong kết quả tìm của bản đồ. | [Lõi] | Tìm trên bản đồ | FR-fleetio-location-dispatch-005 | `Chạy` |
| BR-fleetio-location-dispatch-029 | Nhãn marker xe rơi về Vehicle Name khi trường đã chọn trống; lựa chọn lưu theo người dùng. | [Cấu hình] | Hiện nhãn marker | FR-fleetio-location-dispatch-035 | `Chạy` |
| BR-fleetio-location-dispatch-030 | Bộ lọc Location Entry Type có đúng 3 loại: Fuel Entry, Service Entry, Inspection, cả 3 đã thấy thật, đo trên tài khoản không có thiết bị. | [Lõi] | Lọc lịch sử vị trí | FR-fleetio-location-dispatch-013 | `Chạy` |
| BR-fleetio-location-dispatch-031 | Mỗi mục kiểm trên Fleetio Go mang toạ độ riêng; web chỉ có 1 cặp cấp phiếu. | [Cấu hình] | Nộp phiếu | FR-fleetio-location-dispatch-032, FR-fleetio-location-dispatch-037 | `Chạy (Fleetio Go)` |
| BR-fleetio-location-dispatch-032 | Chọn nhà cung cấp phân loại Service trên phiếu dịch vụ là sinh vị trí xe, không hỏi, không báo. | [Lõi] | Lưu phiếu dịch vụ | FR-fleetio-location-dispatch-004, FR-fleetio-location-dispatch-038 | `Chạy` |
| BR-fleetio-location-dispatch-033 | Địa chỉ nhà cung cấp được quy ra một điểm không kèm độ tin cậy, không cảnh báo; trang nhà cung cấp vẫn ghi đúng chuỗi đã nhập. Khai sai địa chỉ làm vị trí xe nhảy sang nơi không liên quan. | [Lõi] | Sinh vị trí từ phiếu | FR-fleetio-location-dispatch-034, FR-fleetio-location-dispatch-038 | `Chạy` |
| BR-fleetio-location-dispatch-034 | Lớp bản đồ không giữ qua tải lại trang, về mặc định Vehicles bật, Places, Vendors tắt. Nhãn marker và vị trí mở đầu thì lưu theo người dùng. | [Lõi] | Tải lại trang | FR-fleetio-location-dispatch-002, FR-fleetio-location-dispatch-008 | `Chạy` |

## 6. Error Matrix

| Error ID | Title | Trigger | Severity | Related FR | Screen state | Recovery | Mức |
|---|---|---|---|---|---|---|---|
| E-fleetio-location-dispatch-001 | Không có kết quả | "No results found in this area. Try updating your filter criteria or moving the map to re-do your search." | minor | FR-fleetio-location-dispatch-001, FR-fleetio-location-dispatch-031 | Trạng thái rỗng | Đổi vùng, lọc, tìm ở ô Locate | `Chạy (vị trí giả lập)` |
| E-fleetio-location-dispatch-002 | Xe chưa có vị trí | "No current location information available for this Vehicle" | minor | FR-fleetio-location-dispatch-004 | Khối trên trang xe | Nộp phiếu kiểm có vị trí, phiếu dầu có nhà cung cấp, hoặc chờ dữ liệu | `Xem` |
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
| E-fleetio-location-dispatch-013 | Nhà cung cấp không có phân loại Service | Form Service Entry, gõ "TEST" chỉ hiện `Create "TEST"`, không có dòng nhà cung cấp TEST | minor | FR-fleetio-location-dispatch-004 | Danh sách ô Vendor | Phân loại lại nhà cung cấp hoặc tạo mới; chưa thử | `Chạy` |
| E-fleetio-location-dispatch-014 | Enter ở ô tìm chọn nhầm đối tượng | Không có câu báo: gõ tên xe, Enter, chọn nhà cung cấp có tên gần giống vì khớp mờ và nhà cung cấp đứng đầu | minor | FR-fleetio-location-dispatch-005 | Bản đồ chuyển sang nhà cung cấp | Đi xuống trong danh sách kết quả tới dòng xe (đo được 4 dòng) | `Chạy` |
| E-fleetio-location-dispatch-015 | Mất bộ lọc khi tải lại | Không có câu báo: quay về toàn bộ kết quả | minor | FR-fleetio-location-dispatch-005 | Danh sách, bản đồ không lọc | Lọc lại | `Chạy` |
| E-fleetio-location-dispatch-016 | Danh sách lệch bản đồ khi bỏ tick | Bỏ tick "Update list when map moves", kéo về vùng có nhà cung cấp: danh sách vẫn "0 results", bản đồ thấy marker | minor | FR-fleetio-location-dispatch-001 | Danh sách cũ, bản đồ mới | Tick lại, danh sách áp ngay | `Chạy` |
| E-fleetio-location-dispatch-017 | Xe chưa có lịch sử vị trí | "No results found." | minor | FR-fleetio-location-dispatch-013 | Tab Location History rỗng | Nộp phiếu kiểm có vị trí, phiếu dầu hoặc phiếu dịch vụ có nhà cung cấp | `Chạy` |
| E-fleetio-location-dispatch-018 | Enter ở ô Country lưu luôn nhà cung cấp | Không có câu báo: form New Vendor lưu ngay, bỏ qua các phần dưới như Classification | minor | FR-fleetio-location-dispatch-038 | Trang nhà cung cấp thiếu phân loại | Sửa lại, tick Service | `Chạy` |
| E-fleetio-location-dispatch-019 | Vị trí xe nhảy theo địa chỉ khai sai | Không có câu báo: địa chỉ giả được quy ra một điểm ở nước khác, không có độ tin cậy | major | FR-fleetio-location-dispatch-034, FR-fleetio-location-dispatch-038 | Location History, Fleet Map hiện điểm sai | Sửa địa chỉ nhà cung cấp (hiệu lực với lần ghi cũ chưa thử), đối chiếu Source | `Chạy` |

## 7. Success Criteria

| ID | Outcome nghiệp vụ | Đo bằng | Mốc đạt |
|---|---|---|---|
| SC-fleetio-location-dispatch-01 | Tìm được xe nhanh | Số thao tác từ mở bản đồ | TBD |
| SC-fleetio-location-dispatch-02 | Biết xe đang gần nơi nào | Có danh sách gần | Có sẵn |
| SC-fleetio-location-dispatch-03 | Biết vị trí còn tươi không | Tuổi vị trí trên dòng danh sách | Có sẵn |

## 8. Data Entities (tóm tắt — chi tiết ở erd.md)

Location Entry, Inspection Submission, mục kiểm trên Fleetio Go, Fuel Entry, Service Entry, nhà cung cấp, Place, Geofence Event, Geofence Alert Policy, Automation, Job, Job Assignment. Xem [[docs/_research/fleetio/srs/fleetio-location-dispatch-erd.md|ERD]].

## 9. Flows (tóm tắt — chi tiết ở flows.md)

Xem [[docs/_research/fleetio/srs/fleetio-location-dispatch-flows.md|Flows]], [[docs/_research/fleetio/srs/fleetio-location-dispatch-states.md|States]], [[docs/_research/fleetio/srs/fleetio-location-dispatch-usecases.md|Use case]], [[docs/_research/fleetio/srs/fleetio-location-dispatch-userflow.md|User flow]].

## 10. Screens

Ảnh thật và bảng mô tả: [[docs/_research/fleetio/srs/fleetio-location-dispatch-screens.md|Màn hình]]. Không áp `CMP`, `GR` vì mô tả sản phẩm của bên khác.

## 11. Constraints, Dependencies & Assumptions

| Ràng buộc | Source / Owner |
|---|---|
| Tài khoản dùng thử không có thiết bị; xe có vị trí nhờ phiếu kiểm web, phần lớn là vị trí giả lập, và phiếu dầu, phiếu dịch vụ có nhà cung cấp | Chạy thử 03/11/2026 |
| Gói thử 5 xe, đã đầy: đo gom cụm mới tới 4 xe và 15 nhà cung cấp, chưa biết ngưỡng lớn hơn | Chạy thử 03/11/2026 |
| Fleetio Go mới có một phiếu không vi phạm, chưa có ca Location Exception dương | Chạy thử 03/11/2026 |
| Kéo thả, Street View kết luận ở mức quan sát qua công cụ | Chạy thử 03/11/2026 |
| Lượt 3, lượt 4 đọc bản đồ qua DOM, không lưu ảnh có vị trí hoặc địa chỉ thật, nên một số màn không có ảnh | Chạy thử 03/11/2026 |
| Không tạo hàng loạt bản ghi để đo ngưỡng gom cụm | Chạy thử 03/11/2026 |
| Cảnh báo vùng chỉ có hành động gửi email, chưa được phép tự động gửi | Chạy thử 03/11/2026 |

| Giả định | Invalidate nếu sai |
|---|---|
| `GĐ` Invlogis dùng lớp kết nối nhà cung cấp GPS, EUP là kết nối đầu tiên | Phần nguồn vị trí phải viết lại |
| `GĐ` Sự kiện vùng với vị trí từ thiết bị hoạt động như với vị trí từ phiếu | Phần sự kiện vùng phải kiểm lại |

## 12. Open Questions

* [ ] OQ-1: Fleetio có gom cụm marker không? Trả lời một phần: zoom xa hết với 2 xe và 2 Place không gom, marker đè nhau. Lượt 3: 15 nhà cung cấp, 4 xe vẫn không gom, không có marker dạng số; chưa biết ngưỡng ở số lớn hơn (`Chạy` chỉ đọc). Lượt 4 không đo thêm vì gói xe đã đầy và không tạo hàng loạt bản ghi — Nguồn khách: không áp dụng
* [x] OQ-2: Hình dạng, màu marker theo trạng thái; cần tài khoản có thiết bị. Trả lời: marker hình xe đen nhỏ; chú giải có 3 icon theo độ tươi Active, Idle, Stale, không phải chạy hay dừng (`Chạy (vị trí giả lập)`) — Nguồn khách: không áp dụng
* [ ] OQ-3: Lịch sử vị trí xe, vị trí điện thoại lái xe: thời hạn lưu, ai được xem, thông báo thế nào? Cần pháp chế xác nhận. Ghi nhận: web gửi vị trí thật của trình duyệt lên máy chủ mà không báo gì trong form (`Chạy`) — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-4: Fleetio Go có ghi vị trí từng mục kiểm và tạo Location Exception thật không? Một phần: có ghi vị trí từng mục (#126102722, 21/21 mục); chưa có ca dương nên chưa thấy cờ bật và chưa biết ngưỡng (`Chạy (Fleetio Go)`) — Nguồn khách: không áp dụng
* [ ] OQ-5: Street View hoạt động thế nào? Kéo Pegman bằng công cụ 2 lượt đều không ăn, lần sau ở vùng Sample; lượt 4 không thử nữa — Nguồn khách: không áp dụng
* [x] OQ-6: "Update list when map moves" khác gì khi kéo bản đồ tay? Trả lời lượt 3: ô chỉ chặn cập nhật khi kéo tay; chọn từ ô tìm vẫn cập nhật; tick lại là áp ngay (`Chạy`) — Nguồn khách: không áp dụng
* [ ] OQ-7: Vì sao trang xe ghi "Idle" khi vị trí mới 25 giây trong lúc bản đồ "Active"? — Nguồn khách: không áp dụng
* [ ] OQ-8: Có chống nhiễu ở mép vùng không, sự kiện vùng dựa vào lần ghi nào, có áp cho vị trí từ thiết bị như vậy không? — Nguồn khách: không áp dụng
* [ ] OQ-9: Tự gán xử lý thế nào khi xe đang có việc khác, khi xe đã ở trong vùng lúc bật ô, khi việc đã hoàn thành? — Nguồn khách: không áp dụng
* [ ] OQ-10: Đa giác 2 đỉnh có lưu được không? — Nguồn khách: không áp dụng
* [ ] OQ-11: Vì sao log Automation ghi `DNF` trong khi hành động vẫn chạy? — Nguồn khách: không áp dụng
* [ ] OQ-12: Geofence Alert Policy gửi thật ra sao, có lặp lại khi xe ở trong vùng lâu không? Chưa lưu vì chỉ có hành động gửi email; lượt 3 vẫn không chạy vì lý do này — Nguồn khách: không áp dụng
* [ ] OQ-13: Phiếu #125988723 không có vị trí vì sao; Delete lượt gán, Edit, Delete việc có hệ quả gì; việc Completed có mở lại được không? — Nguồn khách: không áp dụng
* [x] OQ-14: Phiếu dịch vụ có nhà cung cấp có sinh Location Entry loại Service Entry như phiếu dầu không? Trả lời lượt 4: có, Service Entry #57903305 sinh 1 dòng cùng giờ phiếu, form không báo (`Chạy`) — Nguồn khách: không áp dụng
* [x] OQ-15: Địa chỉ nhà cung cấp giả được quy ra một điểm bằng cách nào? Trả lời lượt 4: địa chỉ giả vẫn được quy đổi ra một điểm, ở một nước khác với nước đã khai, không báo độ tin cậy; trang nhà cung cấp vẫn ghi đúng chuỗi đã nhập (`Chạy`). Dịch vụ quy đổi cụ thể không nhìn thấy được. Phần địa chỉ không quy được chuyển sang OQ-19 — Nguồn khách: không áp dụng
* [x] OQ-16: Tắt lớp Vehicles có ẩn marker xe không? Trả lời lượt 4: có, marker về 0 và tab Vehicles biến mất; nút có trạng thái `aria-pressed` (`Chạy`) — Nguồn khách: không áp dụng
* [ ] OQ-17: Số đồng hồ 3.100 km trên phiếu Fleetio Go có icon lạ, xe vẫn hiện 2.999 km: vì sao? — Nguồn khách: không áp dụng
* [ ] OQ-18: Khi có thiết bị hoặc API, bộ lọc Location Entry Type có thêm loại khác ngoài 3 loại đã thấy không? — Nguồn khách: không áp dụng
* [ ] OQ-19: Địa chỉ nhà cung cấp hoàn toàn không quy được thì phiếu có sinh vị trí không; sửa địa chỉ nhà cung cấp có đổi các lần ghi cũ không? — Nguồn khách: không áp dụng

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
| Phiếu dầu, phiếu dịch vụ | Đọc hết trường trên form web | **Không có ô vị trí** ở cả hai. Phiếu dầu có nhà cung cấp vẫn sinh vị trí: xem case cuối Mục này | `Chạy` |
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
| Phiếu từ Fleetio Go, các mục ở gần nhau | #126102722, lệch tối đa 37 m | `location_exception` = false; 21/21 mục có toạ độ riêng; hai chỉ báo quá gần, quá xa đều không bật | `Chạy (Fleetio Go)` |
| Chặn phiếu toạ độ giả | Nộp phiếu | **Không chặn được**. Chỉ đồng hồ báo lỗi (E-012), không liên quan vị trí | `Chạy (vị trí giả lập)` |
| Mở Fleet Map | Xe ở xa điểm mở | Tâm theo IP, không tự thu về xe, "No results found in this area" | `Chạy (vị trí giả lập)` |
| Khung có 2 xe | Tab Vehicles | "2 results", sắp Distance, dòng có người lái hoặc "Unassigned", tuổi "3m ago" | `Chạy (vị trí giả lập)` |
| Bấm marker hoặc dòng | Chọn xe | **Không có popup**; panel trái đổi sang xe, marker gắn nhãn tên | `Chạy (vị trí giả lập)` |
| Tab Nearby của xe | Mở tab | PLACES, VENDORS mặc định ẩn; Show Places hiện dòng có khoảng cách: 0, 3.33km, 1.44km, 1.91km | `Chạy (vị trí giả lập)` |
| Rê chuột dòng Place | Tab Nearby | Đường thẳng nét đứt từ xe tới Place, marker xe đổi thành marker Place trong lúc rê | `Chạy (vị trí giả lập)` |
| Quick Add, Add Issue | Nút Add trên panel | Form điền sẵn xe, tạo Issue #39, lưu xong về trang sự cố, **rời bản đồ** | `Chạy (vị trí giả lập)` |
| Bỏ tích Update list when map moves | Bấm Center on Default Location | Danh sách vẫn ra "No results found in this area"; **không thấy khác biệt rõ** với nút này; phần kéo tay xem các case "Update list" lượt 3 | `Chạy (vị trí giả lập)` |
| Đổi Map Options | Satellite, Grayscale, Labels | Chạy được; tải lại vẫn giữ, lưu theo người dùng; Labels đè nhau khi Place gần | `Chạy (vị trí giả lập)` |
| Place đa giác trên Fleet Map | Bật Places | Đúng hình; tâm là marker tròn xanh | `Chạy (vị trí giả lập)` |
| Xe trùng toạ độ tâm Place | Xe trong vùng | Tâm Place che marker xe | `Chạy (vị trí giả lập)` |
| Zoom xa hết | 2 xe, 2 Place | **Không gom cụm**, marker đè nhau. Không đủ kết luận với 2 xe; đo rộng hơn ở case gom cụm lượt 3 | `Chạy (vị trí giả lập)` |
| Độ tươi trên trang xe | Vị trí mới 25 giây | Trang xe có lúc ghi "Idle", bản đồ vẫn "Active". Chưa rõ lý do | `Chạy (vị trí giả lập)` |
| Mở Map Legend | Nút chú giải | Active, Idle, Stale, Place và 5 loại cửa hàng, nhà cung cấp | `Chạy (vị trí giả lập)` |
| Nút zoom | Đọc nhãn trợ năng, bấm | "+" có nhãn "Zoom Out", "−" có "Zoom In"; hành vi đúng theo hình | `Chạy` |
| Street View | Kéo Pegman bằng công cụ | Không ăn, **không vào được** chế độ này | `Xem` |
| Map Starting Location | Thấy 2 lựa chọn | Không bấm vì đổi cài đặt người dùng | `Xem` |
| API tạo vị trí | Đọc tài liệu | 201 khi tạo mới, 422 nếu không hợp lệ; tên trường toạ độ không lộ ở trang tóm tắt; **không gọi thử** | `Docs` |
| Phiếu dầu có nhà cung cấp, xe chưa có vị trí | Phiếu #229944275 của TEST-DAUKEO-2 | Location History có 1 dòng "Fuel Entry"; xe xuất hiện trên Fleet Map "5m ago"; đồng hồ xe thành 100 km | `Chạy` |
| 14 phiếu dầu, chỉ 1 phiếu có nhà cung cấp | TEST-KHO-01 | Chỉ 1 Location Entry "Fuel Entry", cùng giờ phiếu có nhà cung cấp. Các phiếu nhìn thấy khác không có nhà cung cấp **không sinh** dòng nào | `Chạy` |
| Form phiếu dầu có báo tạo vị trí không | Chọn nhà cung cấp, lưu | **Không báo gì** | `Chạy` |
| Xe có vị trí từ phiếu dầu trên panel | TEST-KHO-01 | Last Known Location, Source "Fuel Entry #229915727", Status "Stale"; xe hiện như đang ở cây dầu dù đó chỉ là địa chỉ khai, **không có dấu phân biệt** | `Chạy` |
| Địa chỉ nhà cung cấp TEST là giả | Phiếu dầu chọn nhà cung cấp TEST | Vẫn định vị được ra một điểm, không rõ cách quy đổi | `Chạy` |
| Mở bộ lọc Location Entry Type | Tab Location History | Đúng 3 giá trị: "Fuel Entry", "Service Entry", "Inspection" | `Chạy` |
| Xe chỉ có phiếu kiểm | TEST-XE-01, Location History | 12 dòng đều "Inspection" | `Chạy` |
| Xe chưa có vị trí | TEST-SUA-01, Location History | "No results found." (E-017) | `Chạy` |
| Lọc, phân trang Location History | Mở lọc theo loại | Mở được, **không lưu lọc**; Fleetio: 30 dòng mỗi trang | `Chạy` |
| Tạo Service Entry với nhà cung cấp TEST | Gõ "TEST" ở ô Vendor | Chỉ hiện `Create "TEST"` (E-013); **không tạo được**, không đổi nhà cung cấp, nháp chưa lưu; phần sinh vị trí xem case lượt 4 | `Chạy` |
| Gõ "TEST" ở ô tìm Fleet Map | Có nhà cung cấp, xe, Place cùng tên | "10 results available for search term TEST", nhà cung cấp xếp trước | `Chạy` |
| Gõ tên xe rồi Enter | "TEST-KHO-01" | Chọn nhầm TEST-KHO-NCC-01 vì khớp mờ, nhà cung cấp đứng đầu (E-014); phải đi xuống 4 dòng mới tới xe | `Chạy` |
| Tìm xe chưa có vị trí | TEST-SUA-01 | Vẫn nằm trong kết quả | `Chạy` |
| Mở Filters | Fleet Map | VEHICLES 8 bộ lọc, VENDORS: Classification; nút Cancel, Apply | `Chạy` |
| Lọc Vehicle Type = Trailer | Filters, Apply | Còn 1 marker TEST-MOOC-LOP, huy hiệu "1" trên Filters | `Chạy` |
| Tải lại trang khi đang lọc | Đã lọc Trailer | **Bộ lọc mất**, về 2 kết quả (E-015); Map Options thì được giữ | `Chạy` |
| Bật lớp Vendors | Nút Vendors | Thêm marker nhà cung cấp; danh sách có thêm tab Places, Vendors | `Chạy` |
| Bấm nút Vehicles lượt 3 | Sau khi bật Vendors | Marker xe **vẫn còn trong DOM**; lượt này chưa kết luận, lượt 4 đã đo lại (xem case Lớp bản đồ) | `Chạy` |
| Tìm lớp Shops riêng | Thanh lớp bản đồ | **Không thấy nút**; chú giải có 5 loại cửa hàng, nhà cung cấp | `Chạy`, chức năng Shops vẫn `Docs` |
| Update list: tick, kéo ra vùng trống | Vùng Sample, kéo tay | "0 results", "No results found in this area" | `Chạy` |
| Update list: bỏ tick, kéo về vùng có 2 nhà cung cấp | Vùng Sample, kéo tay | Vẫn "0 results", **không đổi**, bản đồ thấy marker (E-016) | `Chạy` |
| Update list: tick lại, không kéo | Vùng Sample | Ra ngay 2 kết quả, thấy marker | `Chạy` |
| Update list: bỏ tick, chọn từ ô tìm | Vùng Sample | Danh sách **vẫn đổi** theo vùng mới | `Chạy` |
| Gom cụm lớp Vendors | Vùng Sample, zoom xa dần, đếm DOM | 2, 4, 6, 15 kết quả theo từng mức; 15 marker riêng, 0 marker dạng số; ở mức nhìn cả đông nam Mỹ marker trong một thành phố đè nhau, **không gom** | `Chạy` |
| Gom cụm lớp Vehicles | 4 xe TEST, zoom xa thêm 10 mức | Luôn 4 marker tên riêng, **không có** marker dạng số. Không biết ngưỡng ở số lớn hơn | `Chạy` |
| Street View lần 2 | Kéo Pegman bằng công cụ, vùng Sample | **Không vào được** chế độ phố (OQ-5) | `Xem` |
| Đọc menu Map Options | Mở menu | MAP TYPE, MAP DETAILS, MAP STARTING LOCATION ghi thành phố theo IP. "Use Current Map Center", "Reset to Default" **không bấm** vì đổi tuỳ chọn người dùng | `Xem` |
| Mở Set Label Options | Map Options | Hộp 1 ô "Vehicle Marker Label" (đang Name), Cancel, Save; **không lưu** | `Xem` |
| Lưu cảnh báo vùng lượt 3 | Add Alert Policy | **Không chạy** vì hành động duy nhất là gửi email (OQ-12) | `Xem` |
| Jobs lượt 3 | Function list không còn dòng một phần, xem, tài liệu | **Không chạy thêm**, kết quả Jobs giữ nguyên | Không có thao tác mới |
| Phiếu Fleetio Go: toạ độ đầu phiếu | #126102722 có giờ bắt đầu | `starting_latitude` **vẫn rỗng** | `Chạy (Fleetio Go)` |
| Phiếu Fleetio Go: đồng hồ | Số 3.100 km trên phiếu | Có icon lạ, xe vẫn hiện 2.999 km; chưa kiểm vì sao (OQ-17) | `Chạy (Fleetio Go)` |
| Phiếu dịch vụ có nhà cung cấp phân loại Service | Service Entry #57903305, TEST-DAUKEO-2 | Thêm 1 dòng "Service Entry" cùng giờ phiếu, đứng trên dòng "Fuel Entry" cũ | `Chạy` |
| Form phiếu dịch vụ có báo tạo vị trí không | Chọn nhà cung cấp, lưu | **Không có ô vị trí, không báo gì** | `Chạy` |
| Địa chỉ nhà cung cấp giả, có nước | TEST-DV-NCC-01 | Quy đổi ra một điểm ở **nước khác**, **không báo độ tin cậy** (E-019); trang nhà cung cấp ghi đúng chuỗi đã nhập | `Chạy` |
| Enter ở ô Country của New Vendor | Chưa điền phần dưới | Lưu luôn, **bỏ qua** Classification (E-018); phải sửa lại để tick Service | `Chạy` |
| Trang nhà cung cấp | Network Status, nút Invite | Thấy, **không bấm** | `Xem` |
| Phiếu kiểm web sau các phiếu trên | TEST-DAUKEO-2 | Phiếu gửi vị trí trình duyệt nên điểm mới nhất của xe là vị trí máy chạy | `Chạy` |
| Lớp bản đồ: Vehicles bật, mặc định | Fleet Map | Tab "Vehicles", "3 results", 3 marker | `Chạy` |
| Lớp bản đồ: Vehicles tắt | Bấm nút | Tab **biến mất**, 0 marker; nút có `aria-pressed` | `Chạy` |
| Lớp bản đồ: chỉ Vendors | Bấm nút | Tab "Vendors", chỉ marker nhà cung cấp | `Chạy` |
| Lớp bản đồ: Vendors và Places | Bấm nút | Tab "Places", "Vendors"; marker nhà cung cấp, Place | `Chạy` |
| Lớp bản đồ: tắt hết | Bấm nút | "No results found in this area", 0 marker | `Chạy` |
| Tải lại trang sau khi đổi lớp | Fleet Map | Lớp về mặc định Vehicles bật, Places, Vendors tắt, **không lưu** như Map Options | `Chạy` |
| Tìm lớp Shops lượt 4 | Thanh lớp bản đồ | **Không có nút** tên đó, chỉ thấy trong chú giải | `Chạy`, chức năng Shops vẫn `Docs` |
| Ô Vehicle Marker Label | Set Label Options | 5 giá trị: Name, VIN/SN, Vehicle Type, License Plate, "Year, Make, Model" | `Chạy` |
| Nhãn marker = VIN/SN, xe có VIN | Save | TEST-DAUKEO-2 hiện số VIN | `Chạy` |
| Nhãn marker = VIN/SN, xe không có VIN | Save | TEST-XE-01, TEST-MOOC-LOP hiện tên, đúng câu "Falls back to Vehicle Name" | `Chạy` |
| Tải lại trang sau khi lưu nhãn | Fleet Map | Nhãn được giữ, lưu theo người dùng; đã trả về Name | `Chạy` |
| Use Current Map Center | Map Options | Toast "Map Preferences Updated", dòng vị trí mở đầu đổi sang tên vùng đang xem | `Chạy` |
| Reset to Default | Map Options | Đã bấm để trả lại | `Chạy` |
| Street View lượt 4 | Công cụ không kéo được Pegman | **Không thử nữa** (OQ-5) | Không có thao tác mới |
| Đo ngưỡng gom cụm lượt 4 | Gói xe 5/5 | **Chặn**, không tạo hàng loạt bản ghi; OQ-1 giữ ở mức đã thấy | Không có thao tác mới |

## Phát hiện lượt 3 (03/11)

Nguồn: `run-notes/location-dispatch.md`, mục Lượt 3.

- SỬA FR-fleetio-location-dispatch-004: chọn nhà cung cấp trên phiếu dầu tạo vị trí xe tại địa chỉ nhà cung cấp, không cần thiết bị, form không báo. Xe lên Fleet Map sau 1 phiếu. Location Entry Type có 3 loại: Fuel Entry, Service Entry, Inspection; phiếu dịch vụ chưa thử.
- Bộ lọc Fleet Map mất khi tải lại trang.
- Cảnh báo vùng có hành động duy nhất là gửi email nên không chạy.
- Đã đưa vào đúng chỗ: FR-fleetio-location-dispatch-034 đến 037, BR-fleetio-location-dispatch-022 đến 031, E-fleetio-location-dispatch-013 đến 017, OQ-14 đến OQ-18, các case cuối Mục 13. OQ-6 đã trả lời; OQ-1 vẫn mở ở mức 15 nhà cung cấp, 4 xe.

## Phát hiện lượt 4 (03/11)

Nguồn: `run-notes/location-dispatch.md`, mục Lượt 4.

- Phiếu dịch vụ có nhà cung cấp phân loại Service cũng tạo vị trí xe, form không báo: FR-fleetio-location-dispatch-038, BR-fleetio-location-dispatch-032.
- Địa chỉ giả được quy ra điểm ở nước khác, không báo độ tin cậy, vị trí xe nhảy mà không cảnh báo: BR-fleetio-location-dispatch-033, E-fleetio-location-dispatch-019.
- Tắt Vehicles có tác dụng thật; lớp không giữ qua tải lại: BR-fleetio-location-dispatch-034.
- Nhãn marker có 5 giá trị, lưu theo người dùng; Use Current Map Center chạy được.
- OQ-14, OQ-15, OQ-16 đã trả lời; thêm OQ-19. OQ-1, OQ-5 giữ nguyên, không đo thêm.
