---
type: research
feature: fleetio
status: draft
status_changed: 2026-11-03
status_reason: "đã review upstream, không cần sửa"
updated: 2026-11-03
links:
  - docs/_research/fleetio/README.md
---

# Fleetio: danh sách chức năng và mức đã đi

Tổng 275 chức năng: Đã chạy 154 · Một phần 56 · Chỉ xem 54 · Tài liệu 6 · Chưa 0 · Không mở 5.

`Đã chạy` = tự thao tác, thấy kết quả. `Một phần` = đi được một nhánh. `Chỉ xem` = thấy giao diện, chưa thao tác. `Tài liệu` = chỉ đọc tài liệu hãng.

## Dashboard, tổng quan

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Trang đầu Needs Attention | Thẻ đếm dẫn tới danh sách đã lọc (đích từng thẻ ở Mục 13.6); "ROs Needing Approval" không có đích khi rỗng; mỗi thẻ tải riêng; lọc theo nhóm | Đã chạy | Đích từng thẻ |
| Khởi tạo khách | Dữ liệu mẫu có nhãn Sample, tắt được; Sample không tính vào hạn mức; Onboarding Tasks trỏ 7 đường dẫn; danh sách Get Started, mẫu số đổi giữ | Đã chạy | Chạy |
| Hướng dẫn tại chỗ | Khung Learn có mô tả, ảnh, More Info, Academy; đóng được. | Đã chạy | Chạy |

## Vehicles · Danh sách, hồ sơ xe

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Tạo xe | Form 6 phần: Details (Identification, Classification, Additional Details), Maintenance (Service Program hoặc None), Lifecycle, Financial, Sp | Đã chạy | Tạo xe; sau đó chạm trần 5 xe của gói thử |
| Tạo nhiều xe | Add Multiple Vehicles từ form. | Chỉ xem | Xem |
| Trang xe trung tâm | Đầu trang: số km, trạng thái, nhóm, người lái; tab Overview cùng khoảng 19 lịch sử; cột phải bình luận, ảnh, tài liệu; khối Linked Assets, C | Đã chạy | Chạy |
| Tạo bản ghi từ xe | Nút Add: Draft Work Order, Assignment, Fuel, Charging, Expense, Service Entry, Issue, Inspection, Work Order, Warranty, Service Reminder, Re | Đã chạy | Chạy |
| Overview có thể tuỳ biến | Khối Fields tìm được theo tên trường, có Customize Layout; các khối Last Known Location, Open Issues, Service Reminders và số đếm. | Chỉ xem | Xem |
| Lịch sử trường | Status, Group có nút xem lịch sử đổi; menu có View Record History. | Chỉ xem | Xem |
| Giải mã số khung | Nút Decode cạnh VIN/SN điền thông số, gồm dung tích bình. | Chỉ xem | Xem, Docs |
| Liên kết xe | Linked Vehicles là trường chọn trong form sửa xe; kết quả hiện hai chiều ở khối "Linked Assets" › "Link Asset" › "VEHICLES" trên cả hai xe;  | Đã chạy | Linked Vehicles đầu kéo và mooc |
| Trạng thái xe | Status bắt buộc, mặc định Active. Danh mục 5 trạng thái có đếm xe, Add Vehicle Status. Đổi tự do qua trường hoặc automation, không thấy luật | Chỉ xem | Xem |
| Archive xe | Nút Archive trong More Actions, đưa xe sang tab Archived; quyền `vehicles_archive_delete`. Restore chưa kiểm trên xe. | Chỉ xem | Xem |
| More Actions trên xe | Edit Vehicle Settings, Manage Inspection Forms, Manage Service Programs, Manage Integration Links, Attach Shared Document, Recalculate Fuel  | Chỉ xem | Xem |
| Hạn mức xe theo gói | Danh sách hiện "5 of 5", nút Add Vehicle có khoá; Save bị chặn. Account Usage đếm Vehicles. Xe Sample không tính. Quyền Create cảnh báo "Add | Đã chạy | Chạy |
| Loại xe | Type bắt buộc, mặc định Car; Settings › Vehicle Types 25 loại. Loại xe được dùng ở Excluded Vehicle Types của Require a Meter Reading. | Chỉ xem | Xem |
| Nhóm xe | Group dạng cây nhiều cấp; "Require Group" bị khoá khi còn tài sản, liên hệ chưa có nhóm; Export Data. | Chỉ xem | Xem |
| Mooc là một Vehicle | Mooc tạo với Type Trailer, có đồng hồ riêng (lưu trống thành "0 km"), sơ đồ lốp riêng, lịch sử lốp riêng; không có tổ hợp đầu kéo và mooc. Đ | Đã chạy | Chạy |
| Form xe sáu phần | Details, Maintenance, Lifecycle, Financial, Specifications, Settings; trường ở Mục 19. Out-of-Service chỉ là trường ngày và số km, không có  | Chỉ xem | Xem |

## Vehicles · Gán xe

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Gán xe | Assigned Vehicle, Operator, Start Date/Time ("Leave blank if assignment has always existed."), End Date/Time ("Can be past or future."), com | Đã chạy | Chạy |
| Chặn trùng gán | Không cho hai lần gán chồng thời gian trên **một xe**; không tự đóng phân công cũ. Không xét trùng theo người (BR-fleetio-vehicle-007). | Đã chạy | Chạy |
| Chỉ Operator được gán | Ô chọn chỉ hiện liên hệ phân loại Operator ("Allow this Contact to be assigned to assets"); liên hệ khác bị chặn bằng câu dẫn trên trang liê | Một phần | Trùng xe chặn, trùng người không chặn · SRS ghi: Chạy, Docs |
| Lịch gán | Mỗi xe một hàng, xem Day hoặc Week, thanh màu cam là tương lai, xanh là đang chạy, lịch tháng bên phải, gom theo xe hoặc người. | Đã chạy | Thêm, trùng, sửa đè người |
| Tạo gán từ ô lịch | Bấm ô trống mở "Add Vehicle Assignment For {xe}", xe khoá, ngày điền sẵn theo ô. | Đã chạy | Chạy |
| Sửa, thay người trên phân công | Edit đổi Operator đè lên phân công, xe khoá khi sửa. Không có hành động "thay người", trang chi tiết không còn dấu vết người cũ. | Đã chạy | Chạy |
| Chi tiết phân công | Trang "Vehicle Assignment #…": Operator, nhãn Future, Start, End, Duration, Start Meter, End Meter, Distance. Menu thanh lịch: View, Edit, D | Đã chạy | Chạy |

## Vehicles · Số đồng hồ

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Sổ đồng hồ | Mỗi dòng có ngày, giá trị, loại Primary hoặc Secondary, Void, Source, Void Status, Auto-Void Reason; hiện số hiện tại và khoảng cách với hiệ | Đã chạy | Lệch ngày bị từ chối |
| Tự huỷ số sai | Số vượt mức tối đa một ngày: lưu nhưng tự Void, lý do Exceeds Max. Daily Usage, popup có Last Meter Entry, Daily Usage, Max Daily Usage, Exc | Một phần | Exceeds Max chạy; Out of Sequence không tái hiện trên web |
| Sửa xung đột | Dòng gây xung đột gắn cờ đỏ, Void Status "Conflict Source", popup "Conflicting Meter Entry" có số dòng ảnh hưởng và chênh lệch. Unvoid dòng  | Một phần | Void, Unvoid, Conflict Source · SRS ghi: Chạy, Docs |
| Đổi đồng hồ | Bulk Meter Management Void toàn bộ số của xe khi thay đồng hồ, kể cả số GPS. | Tài liệu | Docs |
| Void tay khi nhập | Hộp nhập có ô Void; dòng thành "Manually Voided", không bao giờ là số hiện tại. | Đã chạy | Chạy |
| Unvoid | Hộp "This operation will attempt to unvoid the selected Meter Entry." rồi Confirm. Không hỏi lý do, không kiểm lại Max Daily Usage. | Đã chạy | Chạy |
| Chặn lệch thứ tự theo ngày | Số đồng hồ phải nằm giữa số ngày trước và số ngày sau; sai thì từ chối ở trường, trừ khi tick Void. Cùng luật cho Fuel Entry. | Đã chạy | Chạy |
| Đồng hồ phụ | Add Secondary Meter trong Settings của form xe; Primary Meter chỉ Miles, Kilometers, Hours, không bỏ được. | Chỉ xem | Xem |

## Vehicles · Lốp

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Khai cấu hình trục từng xe | Khai ở tab Tire Management. Form tạo xe không có trục, chỉ có trường chữ ở Specifications › Wheels & Tires. Chưa khai thì màn trống có nút " | Đã chạy | Chạy |
| Trình hướng dẫn | Asset Type (Vehicle, Trailer) → Wheel Positions (4, 6, 8, 10) → Axle Type. Trailer nhảy thẳng sang ô cấu hình, chỉ còn 7 dòng. | Đã chạy | Chạy |
| Danh sách cấu hình | "I know my axle configuration": 27 dòng, 20 xe, 7 mooc. Không tự tạo được. | Đã chạy | Chạy |
| Multi-Axle | Trên mooc hiện thêm "Number of Axles *" từ 2 đến 10; tiêu đề "4 Axle". | Đã chạy | Chạy |
| Vai trò trục | Xe: Steer, Drive, Dead, Lifted, Tag, Pusher, Other. Mooc: Dead, Lifted, Trailer, Other. Đổi được cả khi có lốp, không có dòng Activity riêng | Đã chạy | Chạy |
| Khoá cấu hình | Có lốp thì Edit khoá. Tháo hết thì mở lại, đổi được, Activity giữ nguyên. Đổi cấu hình làm mất vai trò đã đặt. | Đã chạy | Chạy |
| Màn lốp hai cột | Trái: sơ đồ, ô trống nút +, ô có lốp hiện gai, PSI, màu. Phải: "Installed Tires" có số đếm kiểu "12 + Spare", menu Rotate Tires, Remove All  | Đã chạy | Chạy |
| Lắp nhiều lốp | Position chọn nhiều, chip All, từng trục; bấm ô + điền sẵn vị trí. Một lần lắp tạo nhiều lốp cùng thông số. | Đã chạy | Chạy |
| Trường khi lắp | Position, Install Date, Tire Meter at Installation, Current Tread Depth, Current Pressure, Tire Model, Factory Tread Depth, Minimum Tread De | Đã chạy | Chạy |
| Mẫu lốp từ phụ tùng | Tire Model lấy từ Part có category lốp; tạo xong xuất hiện ngay. Chọn mẫu thì Factory, Min, Life tự điền và khoá. Chưa có thì "No options". | Đã chạy | Chạy |
| Spare | Add, chọn "Spare Tire". Activity `Spare Stowed`, Axle Type `N/A`, đầu mục "6 + Spare". Không có ô trên sơ đồ, chỉ có dòng ở Installed Tires. | Đã chạy | Chạy |
| Copy details | Menu dòng lốp. Tick trường cần chép, chọn đích. Ô trống thì tạo lốp mới `Installed`, ngày lắp hôm nay, gai trống. Không chép gai, áp suất. Đ | Đã chạy | Chạy |
| Đọc trên dòng, hộp Edit | Sửa gai, áp suất trên dòng lưu ngay khi rời ô, không có nút Lưu, tạo dòng đọc Method Manual. Hộp Edit thêm Current Tire Meter, Remove; sửa M | Đã chạy | Chạy |
| Đảo theo mẫu chuẩn | Rotation Pattern; "Standard 6x4" điền sẵn 10 dòng: LF↔RF, 2LO→3LI, 2LI→3LO, 2RI→3RO, 2RO→3RI, 3LO→2LI, 3LI→2LO, 3RI→2RO, 3RO→2RI. Sửa tay đư | Đã chạy | Chạy |
| Đảo tự do khép kín | Nút Rotate Tires chỉ bật khi sơ đồ khép kín. Ô trống cũng có dòng New Position và được làm đích. Thông báo đếm cả ô trống. | Đã chạy | Chạy |
| Lưu mẫu đảo tuỳ biến | Hiện "Save as a Custom Rotation Pattern" khi đã khép kín. Bỏ trống tên thì không đảo được. Lưu thật không thử vì mẫu nằm trong Settings. | Một phần | Chạy một phần |
| Undo Rotation | Chỉ ở màn kết quả. Lốp về chỗ cũ, quay lại form, mapping còn nguyên, Activity không còn dấu vết. Close thì mất nút. | Đã chạy | Chạy |
| Tháo | Remove từng lốp, Select All, Remove All. Không hỏi lý do, không chọn đích. Ô về nút +. Thêm dòng `Removal`. | Đã chạy | Chạy |
| Tire Activity | 1 dòng mỗi sự kiện từng lốp. Cột Tire Model, Date Recorded, Date Installed, Tire Meter, Activity, User, Method, Tire Pressure, Tread Depth,  | Đã chạy | Chạy |
| Tire Readings | 1 dòng mỗi vị trí đang có lốp, là lần đọc mới nhất. Cột Vehicle, Last Reading Date, Reading Method, Recorded By, Tread Depth, Pressure, Posi | Đã chạy | Chạy |
| Mức sức khoẻ gai | Ba mức theo Min của lốp, tính lại khi đổi Min. Áp suất không có mức theo lốp. | Đã chạy | Chạy, công thức Suy |
| Mục Tire Readings của biểu mẫu | Tick Tread Depth, Pressure; Minimum, Maximum cho từng cái; bắt ảnh hoặc nhận xét khi Pass, Fail. | Đã chạy | Chạy |
| Phiếu sinh ô theo trục | Tự sinh ô Tread Depth, Pressure theo cấu hình. Thứ tự đi vòng: bên trái từ trước ra sau, rồi bên phải từ sau ra trước. Xe chưa khai trục: hộ | Đã chạy | Chạy |
| Phiếu phát hiện thiếu lốp | "Install Missing Tires" kèm danh sách, nút Install Tires tạo lốp trống, không hỏi gì thêm. | Đã chạy | Chạy |
| Không đạt thành sự cố | Workflow "ANY Failed Inspection Item" → "Create an issue". Một sự cố cho nhiều lốp, Priority High, Source là phiếu. Kết quả từng vị trí có d | Đã chạy | Chạy |
| Số km lốp | Tự tính theo đồng hồ của chính xe chứa lốp, tính lại liên tục. Lùi ngày lắp thì tính từ các số đồng hồ sau ngày lắp. Nhập được Tire Meter at | Đã chạy | Chạy, quy tắc Suy |
| Liên kết xe | Linked Vehicles hai chiều, khối "Linked Assets". Gỡ và gắn từ phía nào cũng được. Không truyền lốp, không truyền số km. | Đã chạy | Chạy |
| Báo cáo | Standard Reports chỉ có "Tire Activity Report"; thêm màn Tire Readings. | Đã chạy | Chạy |
| Đọc áp suất tự động | "Automated tire pressure readings" khoá, chỉ 4x2 hoặc 4x4 có telematics; tài liệu hãng nói Geotab. | Một phần | Chạy phần đọc màn hình, Docs |
| Import lốp | Tài liệu hãng có mẫu import lốp, chưa chạy. | Tài liệu | Docs |
| Lốp là đối tượng độc lập, kho lốp | Fleetio không có | Đã chạy | Tháo xong chỉ còn lịch sử |

## Vehicles · Chi phí, thay xe

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Chi phí khác | Vehicle, Expense Type (17 loại có sẵn), Vendor, Amount, Frequency: "Single Expense" hoặc "Recurring Expense" ("Repeats on a monthly or annua | Đã chạy | Một lần, định kỳ |
| Phân tích thay xe | Máy tính ước lượng **cấp tài khoản**: không có ô chọn xe, không đọc dữ liệu xe nào. Biểu đồ chi phí trên km theo tuổi xe từ giả định nhập ta | Đã chạy | Máy tính tự nhập, chỉ đọc |
| Sinh chi phí định kỳ | Lưu thì xử lý nền ("Processing: Recurring expense save", "Complete: Recurring expense save"), sinh sẵn từng dòng theo kỳ trong tab Future. | Đã chạy | Chạy |
| Cost of Ownership | Khối trên trang xe: Total Costs, Cost Per Meter, Fuel & Energy Costs, Service Costs, Other Costs; mốc This Month, Last Month, This Year, Las | Đã chạy | Chạy |
| Công thức thay xe | Năm 1 tính khớp: nhiên liệu = giá lít / tiêu hao đổi ra km/lít; bảo dưỡng = chi phí năm / km năm; khấu hao Double Declining = giá mua × 2 /  | Đã chạy | Chạy, Suy |

## Fleet Map

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Bản đồ cạnh danh sách | Danh sách Nearby có tab Vehicles, Places, đếm kết quả, sắp theo Distance; dòng ghi tên xe, người lái ("Unassigned" nếu chưa gán), tuổi vị tr | Đã chạy | Vị trí giả lập: danh sách theo khoảng cách |
| Lớp bản đồ | Vehicles, Places, Vendors bật tắt; Shops theo tài liệu hãng. Trong panel xe, PLACES, VENDORS mặc định ẩn, có nút "Show Places", "Show Vendor | Một phần | Vị trí giả lập: bật tắt lớp · SRS ghi: Chạy (vị trí giả lập), Docs phần Shops |
| Tải theo khung nhìn | Lấy vị trí theo khung đang xem, gọi lại khi đổi khung. | Đã chạy | Chạy |
| Nguồn vị trí | Từ tích hợp (`Docs`), API (`Docs`), hoặc từ phiếu kiểm tra (`Chạy`). **Đã sửa:** phiếu dầu và phiếu dịch vụ trên web không có ô vị trí; trên | Một phần | Phiếu kiểm web tạo vị trí; phiếu dầu, phiếu dịch vụ không có ô vị trí · SRS ghi: Chạy, Docs |
| Tìm và lọc | Ô "Locate vehicles, places, vendors on map..." tìm và chọn được xe. Filters có Vehicle Type, Vehicle Group, Vehicle Status, Vehicle Operator | Một phần | Lọc chạy một phần |
| Chi tiết khi chọn xe | Bấm marker hoặc dòng: không popup, panel trái đổi sang xe, marker gắn nhãn tên. Tab Overview có Alerts (Open Issues, Service Reminders, Inco | Đã chạy | Vị trí giả lập: panel, Nearby, Quick Add |
| Quan hệ gần | Dòng Place trong Nearby có khoảng cách. Rê chuột vẽ đường thẳng nét đứt từ xe tới Place, marker xe đổi thành marker Place trong lúc rê. | Đã chạy | Vị trí giả lập: đường nét đứt |
| Tuỳ chọn bản đồ | **Đã sửa tên:** Default (không phải Standard), Satellite, Grayscale; Labels hiện tên Place; Set Label Options; lưu theo người dùng, tải lại  | Một phần | Satellite, Grayscale chạy; Street View không kéo được |
| Chú giải | **Đã sửa nghĩa:** Map Legend có Active, Idle, Stale là độ tươi vị trí, không phải xe chạy, nhàn rỗi; Place là tâm vùng; Preferred Shop, Prem | Đã chạy | Màu theo độ tươi: 30 phút, 1 giờ |
| Lịch sử vị trí | Tab Location History trên xe. | Chỉ xem | Xem sau khi có vị trí · SRS ghi: Xem |
| Vị trí từ phiếu kiểm web | Web app đọc vị trí trình duyệt một lần lúc khởi động app, giữ giá trị và gửi kèm phiếu khi nộp. Phiếu ghi Submission Source "Fleetio Web App | Đã chạy | Chạy |
| Location Entry | Mỗi lần ghi vị trí có asset, loại, contact, thời điểm, Entry Type. Địa chỉ ngược có sau khoảng 1 phút, lúc đầu rỗng. `initial_place` cho biế | Đã chạy | Chạy (vị trí giả lập) |
| Quick Add | Nút Add trên panel, 11 mục: Draft Work Order, Add Vehicle Assignment, Add Expense Entry, Add Service Entry, Add Issue, Add Inspection Submis | Đã chạy | Chạy (vị trí giả lập) |
| Độ tươi vị trí xe | Trạng thái Active, Idle, Stale hiện trên Status, tuổi vị trí trên dòng danh sách. Marker xe hình xe đen nhỏ; chú giải vẽ icon khác nhau cho  | Đã chạy | Chạy (vị trí giả lập) |
| Điểm mở bản đồ | Mở theo IP của máy, không tự thu về xe. Center on Default Location; Map Starting Location đổi được (`Xem`, không bấm vì đổi cài đặt người dù | Đã chạy | Chạy (vị trí giả lập) |
| Location Exception Tracking | Biểu mẫu có cờ Enabled. Trên web không tạo được cờ: mọi phiếu `location_exception` = false. Không so giữa các phiếu. | Đã chạy | Chạy (vị trí giả lập), Suy phần nguyên nhân |
| Gom cụm marker | Mới thử 2 xe | Một phần | Chưa đủ kết luận |

## Places, Geofence

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Địa điểm | Tên, mô tả, địa chỉ, toạ độ, bán kính. Gõ toạ độ thì Address tự điền theo địa chỉ ngược, bản đồ tự chuyển. Vòng tròn đổi ngay khi chọn bán k | Đã chạy | Vùng tròn, đa giác, sửa bán kính |
| Sự kiện vùng | Hai loại Entered, Exited, sinh khi vị trí mới đổi quan hệ với vùng. Dùng làm Record Type của Automation. Không có màn danh sách riêng. | Đã chạy | Vị trí giả lập: Entered, Exited, Automation TEST chạy 2 lần |
| Vùng đa giác | Bấm biểu tượng đa giác, bấm các đỉnh, bấm lại đỉnh đầu để đóng. Hệ thống thay toạ độ bằng tâm, đổi Address theo tâm, khoá Geofence Radius vớ | Đã chạy | Chạy |
| Danh sách, trang địa điểm | Danh sách cột Name, Description, Address; lọc nhanh Location Entry Type, Location Entry Date, Place Geofence Radius. Trang chi tiết: tab Ove | Đã chạy | Chạy, Chạy (vị trí giả lập) phần Location Entries |
| Cảnh báo vùng | Add Alert Policy trên Place: Trigger (Vehicle is within, outside geofence; Contact is within, outside geofence), Which Vehicles?, Which Grou | Chỉ xem | Xem |
| Automation theo sự kiện vùng | Record Type Geofence Event, Trigger Type Created (lựa chọn duy nhất). Điều kiện phổ biến: Geofence Event Type, Geofence Event Place, Vehicle | Đã chạy | Chạy (vị trí giả lập) |

## Jobs

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Gán xe vào việc | Tạo việc, gán xe, tính thời gian trên việc; tự tạo và kết thúc gán theo vùng. Chi tiết tách ở FR 014 đến 022. | Đã chạy | Tạo, gán, trùng, kết thúc, tự gán theo vùng |
| Bảng việc dạng cột | Cột Unassigned (toàn bộ xe) cộng mỗi việc đang chạy một cột, có số đếm. Thẻ xe ghi "On job: 0m". Tab Active, Completed. Lọc Job Name or Numb | Đã chạy | Chạy |
| Tạo việc | Form Add Job: Job Number, Job Name, Place, ô tự gán theo vùng. Nút giữa màn trống và nút góc phải mở cùng form; nút giữa chỉ có khi chưa có  | Đã chạy | Chạy |
| Gán tay | Tích xe trong cột, Actions, Assign. Hộp Add Job Assignments có Job, Start Date/Time. | Đã chạy | Chạy |
| Kết thúc gán tay | Actions, Unassign. Hộp Unassign from Job có End Date/Time. | Đã chạy | Chạy |
| Sửa, xoá lượt gán | Menu dòng xe: Edit, Delete. Edit Job Assignment khoá Job và Vehicle, chỉ sửa Start Date/Time. Delete chưa bấm (`Xem`). | Đã chạy | Chạy |
| Hoàn thành việc | Menu cột: Edit, Complete, Delete. Hộp Complete Job chỉ có End Date/Time; xe đang gán tự kết thúc cùng lúc. Edit, Delete của việc chưa bấm (` | Đã chạy | Chạy |
| Lịch sử gán | Job Assignment History: Job, Place, Vehicle, Time on Job, Start Date, End Date (Active khi đang gán), Added; lọc Status, Job Status, Job, Ve | Đã chạy | Chạy |
| Trang việc | Tab Overview, Job Assignments; Details gồm Job Number, Job Name, Status, Place, Auto-Tracking, Start Date/Time, End Date/Time; bản đồ vùng P | Đã chạy | Chạy |
| Tự gán, tự kết thúc theo vùng | Việc bật ô tự động, gắn Place: vào vùng thêm lượt gán Added = Geofence, thẻ xe có chip "Geofence"; ra vùng lượt có End Date, xe về Unassigne | Đã chạy | Chạy (vị trí giả lập) |

## Inspections

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Dựng biểu mẫu | Tạo trống, từ mẫu hệ thống, hoặc từ PDF, ảnh bằng Smart Upload (Beta); có màu, ngôn ngữ, Location Exception Tracking, Prevent Use of Stored  | Một phần | Dựng, phiên bản Past Version · SRS ghi: Chạy trống và mẫu; Xem Smart Upload |
| Loại mục kiểm tra | Date/Time, Dropdown, Free Text, Inventory Adjustment, Meter Entry, Number, Pass/Fail, Photo, Signature, Tire Readings, Section. Mọi loại trừ | Một phần | 11 loại đọc; 8 loại lưu |
| Luật từng mục | Bắt buộc, mô tả, hướng dẫn có định dạng, nhãn Đạt và Không đạt, N/A, bắt ảnh hoặc ghi chú; mục Số có khoảng, ngoài khoảng là Không đạt, biên | Đã chạy | Bắt buộc, ghi chú, E-001, E-003 |
| Workflow biểu mẫu | Trigger: If an item passes, If an item fails, If form is submitted; chọn "ANY Failed Inspection Item" hoặc từng mục Pass/Fail, Number, Dropd | Một phần | Workflow không tạo được lệnh; chưa lưu |
| Gán biểu mẫu | All Vehicles, By Vehicle Attribute, Specific Vehicle; lịch Daily đến Yearly, Set Delayed Start, Enable Reminder Notification; không đặt lịch | Một phần | Gán Daily; chưa qua ngày |
| Làm phiếu | Chọn biểu mẫu, xe; hệ thống ghi Started, Submitted, Duration, Submission Source, Submitted By, Job, vị trí; nộp xong ra trang phiếu có bản đ | Đã chạy | Không có nháp; lệch múi giờ |
| Vòng đời mục lỗi | Tab All, Needs Action, Open Issue, Acknowledged, Resolved; có Failure Timeline; Status trỏ sự cố, lệnh ("WO #100", "Resolved in Issue #49"). | Một phần | Gộp lỗi lặp, Acknowledge · SRS ghi: Chạy; Create Issue, Reopen Xem |
| Xác nhận lại sau sửa | Tài liệu hãng: sự cố đã giải quyết thì người kiểm tiếp theo được hỏi xác nhận, từ chối thì tạo sự cố mới. Trên web không thấy câu hỏi nào; l | Một phần | Web không có câu xác nhận |
| Chống kiểm khống | Tài liệu hãng: gắn Location Exception khi tỉ lệ mục cùng vị trí vượt ngưỡng, hoặc một mục lệch xa điểm trung tâm; bật theo biểu mẫu. Trên we | Một phần | Vị trí giả; cờ từng mục cần app |
| Cấm ảnh có sẵn | Chỉ cho đính ảnh chụp bằng camera, bật sẵn trên biểu mẫu mới. Chưa thử chụp hay đính ảnh. | Chỉ xem | Cấu hình |
| Ghi nhận lỗi | Acknowledge ở Needs Action mở hộp "Acknowledge Failure", Comments tuỳ chọn. Sau đó row menu chỉ còn "View Failure Timeline". | Đã chạy | Chạy |
| Gộp lỗi lặp | Mục lỗi lại khi sự cố còn mở: không tạo sự cố mới, thêm dòng Item Failures, thêm mốc Failure Timeline. Không báo gì cho người kiểm khi đang  | Đã chạy | Chạy |
| Phiếu ăn theo chuyến | Trường Job tự gắn việc đang gán cho xe lúc nộp, "Unassigned" khi không có; phiếu nộp đúng lúc rời vùng vẫn mang việc đang gán rồi việc mới k | Đã chạy | Chạy |
| Mục Meter Entry | Ghi số đồng hồ của xe từ phiếu, kiểm theo lịch sử đồng hồ; "Require Secondary Meter", "Require Photo Verification" bật sẵn; phiếu hiện dòng  | Một phần | Chạy; ảnh, đồng hồ phụ Xem |
| Phiên bản biểu mẫu | Sửa nhãn sau khi có phiếu: phiếu cũ giữ nhãn cũ, đầu phiếu có nhãn cam "Past Version". Phiếu đã nộp: "..." chỉ có Delete, có Print, không sử | Đã chạy | Chạy |

## Issues

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Tạo sự cố | Người dùng tạo sự cố cho một xe với tóm tắt, ngày báo; hệ thống tự điền người báo và thời điểm. Hạn theo ngày, đồng hồ là tuỳ chọn. | Đã chạy | Chạy |
| Nhiều nguồn sự cố | Sự cố đến từ nhập tay, phiếu kiểm tra hỏng, mã lỗi thiết bị, thu hồi; có trường Source liên kết về nguồn. | Một phần | Tay, từ phiếu kiểm, mã lỗi Sample · SRS ghi: Chạy nhập tay, phiếu; Xem mã lỗi |
| Năm cách xử lý | Menu Resolve trên sự cố mở: Add to Service Entry, Draft Work Order, Add to Work Order, Get Service at Shop, Resolve with Note. Khi sự cố đã  | Một phần | 4/5 cách; Get Service at Shop cần bật Shop Network |
| Đóng sự cố không sửa | Menu ba chấm › Close mở hộp có ô Note tuỳ chọn; đóng ghi Closed Date, Closed By, Note; ghi chú thành một Comment; mất Edit, Resolve. Không t | Đã chạy | Đóng, mở lại |
| Sự cố quá hạn | Sự cố có hạn theo ngày và số đồng hồ. Overdue là giá trị tính, không lưu: đọc lại mỗi lần theo ngày và đồng hồ hiện tại; hiện ở Issue Status | Đã chạy | Hạn, Overdue |
| AI xếp ưu tiên | Với sự cố mới, AI tự gán hoặc gợi ý mức ưu tiên, hiện dấu sao và câu "Auto-assigned priority". Có sự cố vẫn để "No Priority". | Đã chạy | Chạy |
| AI đóng sự cố | Khi có Service Entry, AI đóng hoặc gợi ý đóng sự cố khớp nội dung. | Tài liệu | Docs |
| Giải quyết kèm ghi chú | Resolve with Note mở hộp có Note bắt buộc, nút khoá khi trống. Sau lưu: Status Resolved, khối Resolution Details, nút Reopen, mất Edit. | Đã chạy | Chạy |
| Mở lại sự cố | Nút Reopen trên sự cố Closed hoặc Resolved bằng ghi chú, bằng entry mở hộp xác nhận; sự cố Resolved bằng lệnh thì nút khoá, tooltip nêu số l | Đã chạy | Chạy |
| Thêm vào Service Entry | Hộp "Add to Service Entry" liệt kê sự cố mở của xe, tick sẵn sự cố đang mở trang; chọn Add to New hoặc Add to Existing Service Entry, Contin | Một phần | Chạy New; Xem Existing |
| Recall | Danh sách từ NHTSA theo năm, hãng, đời; tab All, Needs Action, Open, Resolved, Acknowledged; cột Issued At, Status, Issue, Manufacturer Camp | Chỉ xem | Xem 261 dòng Sample, không đổi trạng thái |
| Mức ưu tiên tự động của Issue | Issue mới có Priority "Auto-assign"; #40, #42 tự thành High dù không nhập mức. | Đã chạy | Chạy |

## Faults

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Mã lỗi thiết bị | Nhận mã lỗi, đánh dấu nghiêm trọng, gom các mã liên quan vào một sự cố; có trạng thái Open, Pending, Resolved, Ignored; menu dòng Create Iss | Chỉ xem | Chỉ dữ liệu Sample |
| Luật mã lỗi | Khai mã, mô tả và mức nghiêm trọng theo khách; có mẫu bỏ qua mã phiền. | Chỉ xem | Xem |

## Service Reminders

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Tạo nhắc hai trục | Nhắc gắn xe và đầu việc, chu kỳ theo thời gian và đồng hồ, chỉ cần một trục, trục nào đến trước thì tính; ngưỡng Sắp đến hạn riêng từng trục | Đã chạy | Mốc từ 0, biên |
| Lấy lần gần nhất | Khi chọn xe và đầu việc, form hiện lần hoàn thành gần nhất, lấy từ lịch sử; chưa làm lần nào thì hiện "Never logged for this vehicle". | Đã chạy | Chạy |
| Xem trước lịch | Form hiện 5 kỳ tới với ngày và số km, kể cả kỳ đã qua ("1,000 km / 1,300 km ago"); lỗi ngưỡng báo ngay trong khối này. Form Edit không làm m | Đã chạy | Chạy |
| Tính trạng thái | Upcoming, Due Soon, Overdue đổi ngay khi lưu số đồng hồ từ bất kỳ nguồn nào, không chờ job đêm; lấy trục xấu nhất. Chuyển do thời gian trôi  | Đã chạy | Biên ngưỡng, Void |
| Reset khi xong | Đầu việc ghi nhận trên Service Entry hoặc lệnh Completed thì nhắc tính kỳ sau từ lần làm. Lệnh Open không đổi trạng thái. | Đã chạy | Đóng bằng lệnh, phiếu dịch vụ, sớm, lùi ngày |
| Tạm hoãn | Chọn ngày giờ hoãn, mặc định +7 ngày, giờ theo thiết bị, không có mức chọn sẵn, không có ô lý do. Status "Snoozed", Next Due vẫn đổi số nhưn | Một phần | Hết hạn, đồng hồ đổi, hoãn rồi hoàn thành · SRS ghi: Chạy, Docs |
| Xử lý từ nhắc | Resolve: Add to Work Order, Add to service history, Draft Work Order, Find a shop. Menu "...": Snooze hoặc Remove Snooze, Recalculate Compli | Một phần | Menu Resolve · SRS ghi: Chạy hai đường đầu; Xem phần còn lại |
| Tỷ lệ tuân thủ | Tỷ lệ việc đúng hạn trên việc đã xong; thẻ Completed, Late, On-Time Compliance theo nhắc; trung bình theo danh sách lọc (D 100%, F 100%, Bra | Một phần | Công thức khớp · SRS ghi: Chạy khi mỗi nhắc một lần; nhiều lần chưa kiểm |
| Dự báo ngày đến hạn | Ước tính ngày từ số km trung bình ngày; bật ở cấp tài khoản, nhóm theo tuần hoặc tháng. Thấy nút "Enable Forecasting", không bật vì là cài đ | Tài liệu | Không bật vì đổi Cài đặt |
| Giao nhắc cho người | Giao nhắc quá hạn cho người lái; nhận email hoặc tin nhắn, xác nhận được. Trang chi tiết lấy Operator từ phân công xe. | Chỉ xem | Docs, Xem |
| Chi tiết nhắc | Nút Unwatch, "...", Edit, Resolve; khối Details (Vehicle, Operator, Status, Service Task, Service Program, Next Due, Last Completed, Work Or | Đã chạy | Chạy |
| Đặt tay mốc kỳ tới | Tick "Manually set the due date and/or meter for the next reminder" mở Next Due Date, Next Due Primary Meter, mặc định hôm nay + chu kỳ và đ | Đã chạy | Chạy |
| Sửa nhắc | Edit khoá Vehicle, đổi chu kỳ thì tính lại ngay, không cảnh báo, không bắt lý do, không ghi History. Mở Edit rồi lưu làm Notifications từ In | Đã chạy | Chạy |
| Gộp nhắc vào lệnh | Resolve, Add to Work Order mở hộp liệt kê mọi nhắc của xe để tick thêm, chọn lệnh mới hoặc có sẵn. Lệnh Open: nhắc hiện "Work Order #101, Ad | Đã chạy | Chạy |
| Đóng nhắc bằng phiếu dịch vụ | Add to service history mở "Log completed service": nhập tay hoặc Smart uploads (mặc định). Hoặc New Service Entry, gõ đầu việc ở Line Items: | Một phần | Chạy; Smart uploads Xem |
| Ghi tuân thủ từng lần | Mỗi lần hoàn thành có dòng Due, Completed, nhãn On-Time hoặc Late, chênh trên từng trục ("3 weeks, 6 days ahead · 1,600 kilometers ahead").  | Đã chạy | Chạy |
| KPI danh sách nhắc | Thẻ Overdue Vehicles, Due Soon Vehicles, Snoozed Vehicles đếm xe, không đếm nhắc; Average Compliance; tab Due Soon, Overdue có số; cột Next  | Đã chạy | Chạy |

## Service Programs

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Bộ lịch | Một bộ gồm nhiều lịch cho nhiều xe, có mẫu, đồng hồ chính (Miles, Kilometers, Hours) và phụ; một dòng lịch chọn được nhiều đầu việc; sửa lịc | Một phần | Tạo, thêm đầu việc, gắn xe · SRS ghi: Chạy; đồng hồ phụ, mẫu Xem |
| Đối chiếu khi gán bộ lịch | Trước khi lưu có bảng Service Task, Conflicting, Duplicate, New Interval và câu cảnh báo chung. Lịch có "Set First Service". "Save as a Serv | Một phần | Chạy; Rule Xem |
| Gỡ xe khỏi bộ lịch | Row menu chỉ có Delete; hộp "Confirm Service Program Vehicle Deletion" nêu sẽ xoá mọi nhắc từ bộ này trên xe. Không bấm; hệ quả thực tế chưa | Chỉ xem | Xem |

## Renewals

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Gia hạn giấy tờ | Nhắc theo loại có sẵn, cho xe và liên hệ, có ngày đến hạn, ngưỡng báo, người theo dõi. Fleetio: loại xe Emission Test, Inspection, Insurance | Đã chạy | Gia hạn xe |
| Gia hạn bằng sửa tay | Chi tiết chỉ có Details, Comments, "...", Edit. Không có Resolve, History, không tải giấy tờ mới. Gia hạn là sửa Due Date, kỳ cũ không lưu.  | Đã chạy | Chạy |
| Gia hạn liên hệ |  | Một phần | Tạo, chưa mở chi tiết |

## Work Orders

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Tạo lệnh | Lệnh có xe, trạng thái, phân loại ưu tiên, ngày lập, người lập, người nhận việc, ngày dự kiến và thực tế, xưởng ngoài, hoá đơn, số đơn mua.  | Đã chạy | Form đủ trường, số lệnh |
| Gắn sự cố vào lệnh | Form lệnh liệt kê sự cố của xe theo tab Open, Resolved, Closed; Overdue nằm trong tab Open; tick để gắn; gắn được với từng dòng việc qua Lin | Một phần | Một sự cố ở 2 lệnh · SRS ghi: Chạy, trừ ca #34 chưa rõ |
| Dòng việc | Dòng việc gồm đầu việc, công, phụ tùng, ghi chú, mã phân loại tự điền (Reason, Category, System, Assembly), Last Completed, Add Service Remi | Đã chạy | Công, phụ tùng, lỗi tiền 100 lần |
| Ghi công | Ghi giờ công trực tiếp hoặc bấm giờ bắt đầu, kết thúc theo kỹ thuật viên; chọn kỹ thuật viên lấy đơn giá mặc định của contact. | Một phần | Thêm công, rate liên hệ · SRS ghi: Chạy nhập công; Docs bấm giờ |
| Tổng hợp chi phí | Tính tổng công, phụ tùng, markup công, markup phụ tùng, tín dụng bảo hành, giảm giá, thuế. | Một phần | Tổng, lệch tiền · SRS ghi: Chạy phần tổng; Xem phần còn lại |
| Đổi trạng thái lệnh | Đổi trạng thái ngay trên đầu trang. Open và Pending đổi qua lại không hỏi; Pending sang Completed đi thẳng được; hệ thống kiểm điều kiện the | Đã chạy | Open, Pending, điều kiện hoàn thành |
| Hoàn thành lệnh | Khi chuyển sang trạng thái loại Completed, hệ thống giải quyết sự cố đã chọn, ghi nhận đầu việc, tính Duration, tạo Service Entry, ghi Time  | Đã chạy | Điều kiện, số cuối nhỏ hơn đầu |
| Mở lại lệnh | Đổi lệnh Completed về chưa xong qua hộp "Update Status". Service Entry bị xoá hẳn, URL ra Not Found; sự cố về Open, mất Resolution Details v | Đã chạy | Mở lại lệnh đã Completed |
| Xem lệnh ba chế độ | Danh sách, lịch tháng, lịch tài nguyên theo xe hoặc kỹ thuật viên. | Đã chạy | Chạy |
| Tình trạng từng dòng | Đánh dấu xong từng dòng, không kích hoạt hiệu ứng hoàn thành; cấu hình bắt buộc xong hết mới hoàn thành lệnh. | Tài liệu | Docs |
| Sao chép, in, gửi | More Actions: Run Assessment, Print, Make a Copy, View Record History, Email PDF, Delete. Print mở PDF tab mới. Make a Copy mở form mới: xe  | Một phần | Copy chạy; Print chưa đọc được PDF |
| AI soạn lệnh | Từ sự cố, AI soạn nháp chạy nền, đổi dòng chữ tiến độ; rời trang vẫn chạy. Hộp review: cảnh báo lệnh đang mở của xe, nhóm "Resolves this iss | Một phần | Nhiều sự cố, Discard, bỏ việc · SRS ghi: Chạy tạo mới; Xem thêm vào lệnh đang có |
| AI đánh giá lệnh | Khi có đầu việc và chi phí, AI tự chạy trên lệnh, kiểm công và giá phụ tùng, kết luận Acceptable hoặc Needs Review, ghi nguồn; cho chạy lại  | Đã chạy | Đủ, thiếu, Rerun, sai số |
| Số đồng hồ trên lệnh | Start Odometer và tick "Use start odometer for completion meter" mặc định bật; bỏ tick hiện Completion Odometer. Lưu hai mốc tạo hai dòng Me | Đã chạy | Chạy |
| Phân loại ưu tiên lệnh | Repair Priority Class gồm Scheduled, Non-Scheduled, Emergency, ghi rõ VMRS Code Key 16; bật được bắt buộc. | Đã chạy | Chạy |
| Khoá và gỡ sự cố khỏi lệnh | Sự cố đã gắn lệnh thì khoá lối khác kèm tooltip. Sửa lệnh, bỏ tick rồi lưu là gỡ; sự cố tự do trở lại, Timeline xoá dòng "added this issue". | Đã chạy | Chạy |
| Tồn kho theo dòng phụ tùng | Hộp Add Part chọn kho, ghi "This will make an inventory adjustment" hoặc "None (No Inventory Adjustment)". Lưu lệnh trừ tồn; sửa số lượng, x | Đã chạy | Chạy |
| Giao việc, theo dõi | Assigned To chọn người có nhãn Technician, lưu không hỏi. Người tạo lệnh, sự cố tự thành người theo dõi. | Một phần | Chạy một phần |
| Hoàn thành lại | Lệnh đã mở lại đổi Completed lần nữa: tạo entry mới số khác, dùng ngày và đồng hồ cũ của lệnh, không hỏi lại; Timeline sự cố lại có dòng giả | Đã chạy | Chạy |
| Danh mục trạng thái lệnh | Bảng trạng thái có Name, Type, số lệnh; mặc định Open, Pending loại Incomplete, Completed loại Completed. | Chỉ xem | Xem |
| Đưa ra xưởng ngoài | Get Service at Shop mở hộp giới thiệu Shop Network, cần Enable Shop Network mới dùng. | Chỉ xem | Xem |
| Đơn giá công theo contact | Contact Technician có đơn giá mặc định; danh sách chọn và hộp Edit Labor hiện đơn giá đó. | Đã chạy | Chạy |

## Service History

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Ghi lịch sử trực tiếp | Tạo Service Entry không qua lệnh, bắt buộc Odometer và Completion Date, không cần dòng việc; lưu là giải quyết sự cố đã chọn. | Đã chạy | Entry tạo tay, sửa |

## Service Tasks

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Đầu việc | Danh mục đầu việc có mã phân loại mặc định, giờ công dự kiến, phụ tùng gắn kèm; 400 đầu việc có sẵn. Tab Active, Archived; Actions có Update | Đã chạy | Tạo, trùng, archive; không thấy Merge |
| Tạo, lưu trữ đầu việc | Form "New Custom Service Task" gồm 6 bước gập, Save khoá tới khi Continue hết. Archive không xoá khỏi Fleetio, cập nhật bản ghi liên quan ch | Đã chạy | Chạy |

## Warranties

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Bảo hành | Khai bảo hành theo ngày và số km, cho nhiều xe một lượt, mỗi xe một Start Date, Start Meter; Standard Warranty, Standard templates, Extended | Một phần | Tạo, Opportunity; xe TEST-SUA chưa dựng |
| Cơ hội bảo hành trên lệnh | Khối Warranty Opportunities luôn hiện trên lệnh: đếm active, expiring soon, total; Vehicle Coverage khớp đầu việc theo mã phân loại, có View | Một phần | Chạy; nút claim chưa thử |
| Tạo bảo hành nhiều xe | Form "New Warranties" 2 bước: Vehicles (nhiều xe, mỗi xe Start Date, Start Meter riêng) rồi Coverage Type: Standard Warranty, Standard templ | Đã chạy | Chạy |
| Tự tính hạn bảo hành | End Date = Start Date + Coverage Duration; End Meter = Start Meter + Coverage Distance; Status "Active". Danh sách có số active, expiring so | Đã chạy | Chạy |
| Gắn mã bảo dưỡng vào bảo hành | Maintenance Categorization nhập mã hệ thống (VMRS), có Bulk Mode, Column Mode. | Đã chạy | Chạy |
| Mẫu bảo hành | Coverage Template "contain a collection of coverages based on manufacturer guidelines"; Settings › Warranty Templates rỗng. Xe không có Make | Chỉ xem | Xem |

## Parts & Inventory

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Danh mục phụ tùng | Mã duy nhất, mô tả, nhóm, hãng, mã hãng, UPC, đơn giá, đơn vị, bảo hành, ảnh, tài liệu. Không thấy trường thay thế, tương thích xe (K23). Đơ | Một phần | Chạy; K23 Xem |
| Kho và hoạt động theo kho | Phụ tùng bật tại nhiều kho, mỗi kho có vị trí dãy, hàng, ô; số lượng; điểm đặt lại. Tên kho không trùng. Kho khai ở Settings; bật phụ tùng t | Đã chạy | Nhiều kho, tồn theo kho |
| Thẻ tồn | Theo kho: Current Qty, Reorder Point, Pending PO Qty, WO Current Qty; bốn nút điều chỉnh, chuyển kho, đặt mua, menu (Edit, View History). | Đã chạy | Chạy |
| Sổ kho | Mỗi biến động ghi ngày, kho, loại, chứng từ, lý do, nhà cung cấp, số biến động, số trước, số sau, người, ghi chú. Sáu loại: Initial, Manual, | Đã chạy | Chạy đủ sáu loại |
| Điều chỉnh tồn | Hộp theo một kho: Adjust Quantity và New Quantity liên động, lý do bắt buộc trong 11 giá trị, ghi chú, chấp nhận số lẻ. Không chặn giảm quá  | Đã chạy | Chỉnh âm không chặn |
| Chuyển kho | Nhập số chuyển, chọn kho đích, danh sách đích chỉ gồm kho còn lại kèm tồn. Nút khoá khi tồn từ 0 trở xuống. Nhập quá tồn thì cắt về tồn hiện | Đã chạy | Tự cắt số lượng |
| Cảnh báo tồn thấp | Nhãn theo từng kho: Low Stock khi tồn trên 0 và từ điểm đặt lại trở xuống, số màu cam; Out of Stock khi từ 0 trở xuống. Gửi email theo tài l | Một phần | Biên điểm đặt lại · SRS ghi: Chạy nhãn; Docs email |
| Tính giá tồn | Chọn một trong Average Cost, FIFO, LIFO, Static Pricing. Static: Unit Cost phụ tùng giữ theo danh mục dù đơn mua giá khác; Total Inventory V | Một phần | Static; FIFO, LIFO cần đổi Cài đặt |
| Xuất phụ tùng cho lệnh | Chọn phụ tùng thấy tồn từng kho; lấy từ kho hoặc None không trừ kho; gắn đầu việc. Trừ ngay khi lưu. Không cảnh báo khi vượt tồn. | Đã chạy | Chạy |
| Bulk Manage Parts | Tab theo kho; cột Aisle, Row, Bin, Active?, Track Inventory, Current Qty, Last Quantity Update; sửa ô là tự lưu, sổ loại Bulk Update, không  | Một phần | Chạy; Print Worksheet Xem |
| Nhiều nhà cung cấp, lịch sử giá | Thêm nhà cung cấp, giá trong Purchase History; đơn mua tự thêm dòng lịch sử; trang phụ tùng vẽ biểu đồ giá. | Đã chạy | Chạy |
| Sửa, xoá dòng phụ tùng trên lệnh | Sửa số lượng hoặc xoá dòng thì sổ ghi bù, loại Work Order kèm số lệnh; xoá có hộp xác nhận. | Đã chạy | Chạy |
| Tác động của hoàn thành, mở lại lệnh | Hoàn thành: sổ không có dòng mới, sinh Service Entry, Edit khoá; cần Started At, Start Odometer theo cài đặt. Mở lại: sổ không đổi, liên kết | Đã chạy | Chạy |

## Purchase Orders

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Lập đơn mua | Một nhà cung cấp, một kho rồi mới thêm dòng; chỉ hiện nhà cung cấp có Parts; đơn giá lấy từ danh mục, sửa được; giảm giá, phí vận chuyển, th | Đã chạy | Chạy |
| Duyệt đơn | Có quyền duyệt thì Save & Approve hoặc Approve, một cú bấm, không hộp xác nhận, duyệt được đơn của mình. Không có quyền thì Submit for Appro | Một phần | Tự duyệt; Pending, Rejected cần người thứ hai |
| Một nút chính mỗi bước | Approve, Mark as Purchased, Receive, Close; ghi người và thời điểm mỗi bước. | Đã chạy | Chạy |
| Nhận hàng | Bảng Item, Total Received, Total Ordered, Receive; nhận nhiều lần, lần sau gợi ý số còn lại. Không chặn nhận vượt. Trạng thái tính theo từng | Đã chạy | Chạy |
| Nơi đến khi nhận | Inventory, Existing work order, New work order. Hai nhánh lệnh đều nhập kho trước, trừ khi lưu lệnh, dòng ghi chú "From PO #n". `Docs`: chỉ  | Đã chạy | Vào kho, vào lệnh |
| Make Adjustment trên đơn | Có ở Full, Closed; bảng Item, Total Received, Total Ordered, Adjustment; số âm tới mức đã nhận; quá thì cắt không báo; ghi sổ; về Partial; " | Một phần | Chạy từ Full; từ Closed Xem nút |
| Đóng đơn | Close từ Partial, Full; hộp xác nhận; đóng được khi nhận thiếu, không ghi lý do; ghi Closed By. Không có nút mở lại. Không có trạng thái, nú | Đã chạy | Chạy |
| Sửa đơn theo trạng thái | Draft sửa mọi thứ; Approved đủ trường; Purchased có Edit; Partial khoá nhà cung cấp, kho, không thêm bớt dòng, sửa số và giá được; Full, Clo | Một phần | Chạy Approved, Partial, Closed; còn lại Xem |
| Lùi trạng thái đơn | Save as Draft từ Approved về Draft, mất dòng Approved By. Unmark as Purchased từ Purchased về Approved, một cú bấm. Make Adjustment từ Full  | Đã chạy | Chạy |
| Sao chép đơn | Make a Copy mở form mới điền sẵn, giữ giá đơn cũ, số tăng lên. | Đã chạy | Chạy |
| In và lịch sử bản ghi đơn | Print, View Record History trên đơn. | Chỉ xem | Xem |

## Vendors

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Nhà cung cấp | Tên, địa chỉ, thành phố, tỉnh, mã bưu chính, quốc gia bắt buộc; liên hệ; phân loại Charging, Fuel, Parts, Service, Vehicle không bắt buộc nh | Một phần | Chạy; đánh giá Xem |
| Tạo nhanh trong ô chọn | Gõ tên chưa có thì chọn Create, mở form với tên điền sẵn và phân loại theo ngữ cảnh. | Đã chạy | Chạy |
| Trang nhà cung cấp | Tab Overview, Fuel Entries, Purchase Orders theo phân loại; tab đơn liệt kê đơn của nhà cung cấp. "Network Status: Invite", "Find Shops" có  | Một phần | Chạy tab; Xem Network Status, Find Shops |

## Fuel

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Phiếu dầu | Xe, ngày, số đồng hồ, số lít, đơn giá, loại dầu, nơi đổ, tham chiếu, ảnh, tài liệu. Nơi đổ chỉ gồm nhà cung cấp có Fuel; có nhà cung cấp thì | Đã chạy | Chạy |
| Tính tiêu hao | Từ phiếu trước theo số đồng hồ: quãng đường, tiêu hao, chi phí trên km, chênh so với lần trước. Cộng dồn phiếu Partial. Tính đúng nhưng xe k | Đã chạy | Chạy |
| Cờ phiếu dầu | Personal vẫn tính tiêu hao và vào Cost of Ownership. Partial cộng dồn sang phiếu sau. Reset usage: phiếu đó không usage, phiếu sau Usage "N/ | Một phần | Capacity; Personal, Void |
| Thẻ tổng hợp dầu | Tổng tiền, tổng lượng, tiêu hao trung bình, chi phí trung bình theo bộ lọc. Trên VND sai 100 lần. | Đã chạy | Chạy |
| Cảnh báo sai vị trí | Vị trí xe khi đổ xa nhà cung cấp hơn bán kính đặt thì gắn Vendor Location Alert; tắt được. | Chỉ xem | Cần tích hợp |
| Cảnh báo vượt dung tích | Số lít lớn hơn dung tích bình đã khai thì gắn Capacity Alert và ghi Capacity Exception Volume, kể cả phiếu nhập tay. Bằng dung tích không cả | Đã chạy | Nhập tay có cảnh báo, biên 60 và 60,5 |
| Void phiếu dầu | Tick Void, số đồng hồ vẫn bắt buộc; lưu thì số gạch ngang, đồng hồ xe không đổi, không Usage; vẫn tính vào chi phí xe. | Đã chạy | Chạy |
| Bộ lọc phiếu dầu | Date, Vehicle, Vehicle Group, Vendor, Filters; mở bộ lọc theo xe có Add Filter, Add Filter Group. | Một phần | Chạy lọc xe; còn lại Xem |
| Thẻ dầu trên phiếu | Ô Fuel Card ghi "No"; cấu hình WEX chỉ đọc; không có màn gán thẻ thử được. | Chỉ xem | Xem |

## Reports, hỏi dữ liệu

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Báo cáo chuẩn | 49 báo cáo 13 nhóm; yêu thích, lưu, chia sẻ; dạng lưới, danh sách; nhãn "Upgrading soon" trên 4 báo cáo. Bảng nhóm ở Mục 18. | Một phần | 49 báo cáo; mở sâu 1; Share có link công khai |
| Hỏi dữ liệu | Nút Ask a data question trên đầu trang mở AI Data Analyst, khung nhúng từ ThoughtSpot; hỏi bằng lời ra bảng; Show work, chọn All data models | Đã chạy | Trả lời sai số |
| Trang báo cáo | Issues Report: biểu đồ Summary, Top Vehicles; Filters, Columns, phân trang; Save, Share, Export CSV (Export Visible Columns, Export All Colu | Đã chạy | Chạy 1/49 báo cáo |
| Chia sẻ báo cáo bằng link | Bấm Share sinh ngay link công khai, có hạn (Fleetio: 7 ngày); "this link allows anyone with access to view all data". Reports › Shared liệt  | Đã chạy | Chạy |

## Automations

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Tự động hoá | Trigger gồm loại bản ghi và kiểu sự kiện; điều kiện tuỳ chọn; hành động Update Field, Add Comment, Send Email, Create Record; có bật tắt, ph | Một phần | Tạo, bật, chạy, tắt, Archive · SRS ghi: Chạy Add Comment, Update Field, Create Record; Send Email chưa chạy |
| Loại bản ghi tự động hoá | Work Order, Service Entry, Fault, Issue, Purchase Order, Geofence Event, Vehicle. Kiểu sự kiện gồm Created, Updated, Created or Updated, Del | Một phần | Nhiều loại · SRS ghi: Chạy Issue; còn lại Xem |
| Mẫu tự động hoá | 18 mẫu: Faults 2, Issues 5, Purchase Orders 3, Service Entries 2, Work Orders 6; gợi ý đúng lúc ngay sau hành động liên quan. Bảng từng mẫu  | Đã chạy | Đọc đủ 18 mẫu |
| Danh sách tự động hoá | Cột Name, Status, Trigger Record, Total Runs, Successful Runs, Failed Runs, Created By, Last Run At, Current Version; tab All, Archived; lọc | Đã chạy | Chạy |
| Thư viện mẫu | Browse Templates: cột trái theo loại trigger, thẻ có sơ đồ trigger, số điều kiện, số hành động, nút Apply khi rê chuột. Apply mở trình dựng  | Đã chạy | Chạy |
| Bật tắt có xác nhận và phiên bản | Lưu xong ở trạng thái tắt; bật phải qua hộp xác nhận và lúc đó sinh phiên bản v.1, ghi Enabled At; tắt cũng có hộp xác nhận. | Một phần | Chạy; sửa khi đang bật để sinh v.2 chưa chạy |
| Archive và Restore automation | Archive không cần tắt trước, tắt ngay, ghi Disabled At; bản Archived chỉ đọc; Restore về Disabled, không tự bật. Nút Delete, Make a Copy, Vi | Một phần | Chạy một phần |
| Run History và Run Result | Mỗi lượt có kết quả, phiên bản, bản ghi kích hoạt, Triggered By, log JSON. | Đã chạy | Chạy; chỉ thấy SUCCESS |
| Trình dựng điều kiện | Với Issue: 59 trường, chia nhóm Issue, Tool, Vehicle, Vehicle or Tool; All of, Any of; nhóm điều kiện lồng. So khớp không phân biệt hoa thườ | Một phần | Chạy một phần |
| Hành động Create Record | Tạo Work Order từ Issue; chỉ có Status, Assigned To, Service Tasks; Status chỉ cho Open và Pending; WO sinh ra liên kết Issue ở cột Resolved | Đã chạy | Chạy |
| Thông báo của automation | Ô Failure Notification Email, Run Summary Email. | Chỉ xem | Xem |
| Automation đổi trạng thái xe | Mẫu: In Shop khi sự cố từ kiểm tra; Active khi sự cố Resolved; đổi trạng thái khi tạo lệnh; Active khi lệnh Completed và Vehicle Incomplete  | Chỉ xem | Xem |

## Settings, quyền

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Thiết lập chung | Khách chọn tiền tệ, định dạng ngày, múi giờ, 12 hay 24 giờ, đơn vị số đo, nhiên liệu, hệ đo, gọi Vehicle hay Asset, thuế. Là mặc định cho xe | Chỉ xem | Đọc đủ |
| Luật bật tắt có giải thích | Mỗi luật có ô tick, câu mô tả tác động, phạm vi; loại trừ theo loại xe (Require a Meter Reading kèm Excluded Vehicle Types). | Chỉ xem | Xem 3.800/3.965 ký tự trang |
| Danh mục theo khách | Trạng thái, loại, mã, lý do, đơn vị do khách sửa; có mục khoá của hệ thống, có bí danh, tắt được từng mục (Issue Priorities). Số mục ở Mục 1 | Chỉ xem | Xem |
| Tắt cả module | Ví dụ Enable Work Orders; tắt thì ẩn Work Orders, Parts. General Settings còn bật tắt Jobs, Motor Pool, Smart Uploads (Fuel Entry, Service E | Chỉ xem | Xem, chưa tắt thử |
| Role | Bốn vai có sẵn: Fleet Manager, Operator, Technician, Viewer; 30 module, mỗi module mức đủ, một phần, không; thêm vai mới; khoá vai mặc định. | Chỉ xem | Xem, chưa kiểm hiệu lực thật |
| Record Set | Phạm vi dữ liệu theo Vehicles, Contacts, Part Locations, Inspection Forms; mẫu Assigned Only, Full, No Access, Group Only, View Only; quyền  | Chỉ xem | Xem, chưa kiểm hiệu lực thật |
| Điều kiện theo trường tuỳ chỉnh | Record Set lọc được theo trường tuỳ chỉnh dạng chọn, tick. | Chỉ xem | Docs, Xem tên điều kiện |
| Giới hạn theo gói | Hiện đã dùng trên giới hạn: tài liệu, vai, xe, tự động hoá, bản ghi tự tạo (Fleetio: 250.0 GB, 30, 5, 75, 25). Hết hạn mức thì chặn tạo và k | Một phần | Chạm trần 5 xe · SRS ghi: Chạy với xe; còn lại Xem |
| Quyền con theo module | Vehicles có create, edit, view_all, view_details, view_financial_info, view_custom_fields, export_data, update_status, manage_vehicle_assign | Chỉ xem | Xem |
| Cảnh báo chi phí tại quyền | Ngay tại quyền Create của Vehicles: "Adding new Vehicles will result in additional charges to your account's subscription." | Chỉ xem | Xem |
| Điều kiện Record Set tự tạo | Vehicles có 8 điều kiện: All vehicles, Vehicles in this contact's group, Vehicles assigned to this contact, Specific vehicles, Vehicles in s | Chỉ xem | Xem, không lưu |
| Chính sách bảo mật | Minimum Length, Expiration, yêu cầu ký tự, Maximum invalid login attempts, Lockout, Reset All Passwords; giá trị ở Mục 14. | Chỉ xem | Xem |
| AI Service Advisor | Issue Prioritization, Issue Resolution, Fault Monitoring, Service Assessments, Service Writer, mỗi cái có Manage, có câu điều khoản. | Chỉ xem | Xem |
| Khung trạng thái theo khách | Work Order: Type cố định Incomplete, Completed; khách thêm tên. Purchase Order: 8 trạng thái cố định, không có Add. | Chỉ xem | Xem |
| Cài đặt bảo dưỡng | Maintenance Settings: Enable Work Orders, Next Work Order Number, Require a Meter Reading kèm Excluded Vehicle Types, Require Inspections, R | Chỉ xem | Xem |
| Quyền trên xe | Quyền con: create, edit, view_all, view_details, view_financial_info, view_custom_fields, export_data, update_status, manage_vehicle_assignm | Đã chạy | Chạy |
| Bắt buộc số đồng hồ theo loại xe | Maintenance Settings: Require a Meter Reading + Excluded Vehicle Types, "This requirement only applies to future Work Orders or Service Entr | Chỉ xem | Xem |

## Tính năng chung

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Danh sách chuẩn | Tab đếm số, lọc nhanh, Filters có nhóm điều kiện, sắp xếp, nhóm dòng, chọn cột, phân trang, chọn nhiều. | Chỉ xem | Xem |
| Chế độ xem đã lưu | Add Tab, Save View, Save Changes; My Saved Views, Saved Views dùng chung. | Chỉ xem | Xem |
| Xem nhanh bản ghi | Record peek mở ngay trên danh sách. | Chỉ xem | Xem |
| Theo dõi, bình luận | Watch; người tạo tự theo dõi; bình luận, nhắc tên; cột phải trên trang chi tiết. Automation bình luận với tác giả "Fleetio Automation". | Một phần | Theo dõi, comment · SRS ghi: Chạy một phần |
| Thông báo | Hồ sơ thông báo gán cho người (gán bulk từ Contacts), nhóm xe theo dõi có cột Direct Watchers, Total Watchers, cài đặt cá nhân; hộp Inbox, A | Chỉ xem | Xem, tài khoản có 0 hồ sơ |
| Tìm toàn cục | Tìm theo 15 loại bản ghi. | Chỉ xem | Xem |
| Lịch sử bản ghi | View Record History; lịch sử từng trường. Có trên xe và automation. | Chỉ xem | Xem đọc nút |
| Kho tài liệu | Danh sách file, thư mục, biết gắn bản ghi nào; tab All Documents và tab tên tài khoản; cột File Name, File Size, Location, Auto-Delete, Atta | Chỉ xem | Không tải tệp |
| Liên hệ một bảng | Một bảng Contact, phân vai bằng tick Operator, Employee, Technician; User Access: Enable Access to Fleetio hoặc No Access (mặc định). Người  | Một phần | Chạy No Access; Xem Enable Access, không mời người |
| Motor Pool | Đặt xe dùng chung: cột Motor Pool, Number, Operator, Vehicle Types, Vehicle, Pick Up, Drop Off, Status; Settings có Motor Pools, Reservation | Chỉ xem | Xem rỗng; chưa chạy |

## Tích hợp, API

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Webhook | Chọn một sự kiện mỗi webhook; hơn 50 sự kiện; ký xác thực; thất bại 3 lần liên tiếp thì tắt. Màn ghi "send a HTTP POST" dạng JSON. | Chỉ xem | Xem rỗng, không tạo |
| API, SAML, MCP | API key, đăng nhập SAML (có Metadata), máy chủ MCP: "Each connection respects the user's role permissions." Module Fleetio MCP mức không có  | Chỉ xem | Xem, không bật |
| Sandbox, xuất dữ liệu | Môi trường thử: Sample Copy, Production Copy có hạn mức riêng. Export Account Data: 13 loại dữ liệu, CSV hoặc XLS, gửi qua email, link hết h | Chỉ xem | Xem, không bấm |
| Kết nối ra ngoài | Integration Links (link sang hệ khác kèm biến), External Connections (FTP, SFTP, Amazon S3 cho báo cáo định kỳ). | Chỉ xem | Xem, không tạo |
| API vị trí | `POST /vehicles/:id/location_entries` tạo mới, bản tương tự cho Equipment, khuyên Bulk API khi nhiều. | Tài liệu | Docs |

## Ngoài phạm vi đợt này

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Tools | Không mở trial theo chọn của user | Không mở | Không mở trial theo chọn của user |
| Advanced Analytics | Không mở trial theo chọn của user | Không mở | Không mở trial theo chọn của user |
| Custom Records, trường tuỳ chỉnh | Không mở theo chọn của user; chỉ có tài liệu hãng | Không mở | Không mở theo chọn của user; chỉ có tài liệu hãng |
| App Fleetio Go | Chưa xem; cần điện thoại | Không mở | Chưa xem; cần điện thoại |
| Kết nối thật GPS, ERP, thanh toán | Không kết nối; cần tài khoản ngoài | Không mở | Không kết nối; cần tài khoản ngoài |
