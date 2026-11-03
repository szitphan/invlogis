---
type: research
feature: fleetio
status: draft
updated: 2026-11-03
links:
  - docs/_research/fleetio/README.md
---

# Fleetio: danh sách chức năng và mức đã đi

Tổng 327 chức năng: Đã chạy 216 · Một phần 67 · Chỉ xem 38 · Tài liệu 2 · Chưa 0 · Không mở 4.

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
| Tạo nhiều xe | Add Multiple Vehicles từ form hoặc menu Vehicle List, 2 bước. Bước 1 dán tối đa 200 xe, mỗi dòng {Vehicle Name}, {VIN}, {Group}; VIN, Group  | Một phần | Chặn: Add Multiple khoá khi gói 5/5 |
| Trang xe trung tâm | Đầu trang: số km, trạng thái, nhóm, người lái; tab Overview cùng khoảng 19 lịch sử; cột phải bình luận, ảnh, tài liệu; khối Linked Assets, C | Đã chạy | Chạy |
| Tạo bản ghi từ xe | Nút Add: Draft Work Order, Assignment, Fuel, Charging, Expense, Service Entry, Issue, Inspection, Work Order, Warranty, Service Reminder, Re | Đã chạy | Chạy |
| Overview có thể tuỳ biến | Khối Fields tìm được theo tên trường (gõ "tire" lọc còn nhóm Specifications, "4 results for "tire"", có "Clear search"), có Customize Layout | Một phần | Chặn: Sửa layout nằm trong Settings |
| Lịch sử trường | Status, Group có nút xem lịch sử đổi; menu có View Record History. Hộp "Status Updates" mỗi lần một dòng: ai đổi, từ trạng thái nào sang trạ | Đã chạy | Status Updates, Record History ghi từng thay đổi |
| Giải mã số khung | Nút Decode cạnh VIN/SN điền thông số, gồm dung tích bình. VIN ngắn thì nút khoá, không giải thích (E-fleetio-vehicle-026). VIN 17 ký tự: "De | Đã chạy | VIN ngắn khoá; VIN đúng ra bảng so sánh |
| Liên kết xe | Linked Vehicles là trường chọn trong form sửa xe; kết quả hiện hai chiều ở khối "Linked Assets" › "Link Asset" › "VEHICLES" trên cả hai xe;  | Đã chạy | Linked Vehicles đầu kéo và mooc |
| Trạng thái xe | Status bắt buộc, mặc định Active. Danh mục 5 trạng thái có đếm xe, Add Vehicle Status. Đổi tự do qua form hoặc automation, không có luật chu | Đã chạy | Đổi đủ 5 trạng thái, không ràng buộc |
| Archive xe | Nút Archive trong More Actions, hộp "Confirm Vehicle Archive", nút "Archive Vehicle", đưa xe sang tab Archived; quyền `vehicles_archive_dele | Một phần | Chặn: Chưa có đặt chỗ, chờ user quyết Operator |
| More Actions trên xe | Edit Vehicle Settings (mở thẳng phần Settings của form), Manage Inspection Forms (thẻ từng biểu mẫu nhãn "Disabled", menu "…", "View Submiss | Một phần | Mở thêm 2 mục; Integration Links bị chặn |
| Hạn mức xe theo gói | Danh sách hiện "5 of 5", nút Add Vehicle có khoá; Save bị chặn. Account Usage đếm Vehicles. Xe Sample không tính. Quyền Create cảnh báo "Add | Đã chạy | Chạy |
| Loại xe | Type bắt buộc, mặc định Car; Settings › Vehicle Types 25 loại. Đổi loại tự do, không hỏi, dòng phụ đầu trang đổi theo, Status giữ nguyên, có | Đã chạy | Đổi Car sang Semi Truck tự do |
| Nhóm xe | Group dạng cây nhiều cấp, ô chọn hiện cha / con, tìm tên chưa có thì có dòng "Create "…""; "Require Group" bị khoá khi còn tài sản, liên hệ  | Một phần | Chặn: Tạo nhóm, Export Data |
| Mooc là một Vehicle | Mooc tạo với Type Trailer, có đồng hồ riêng (lưu trống thành "0 km"), sơ đồ lốp riêng, lịch sử lốp riêng; không có tổ hợp đầu kéo và mooc. Đ | Đã chạy | Chạy |
| Form xe sáu phần | Details, Maintenance, Lifecycle, Financial, Specifications, Settings; trường ở Mục 19. Out-of-Service chỉ là trường ngày và số km, không có  | Đã chạy | Lưu ngày, số Out-of-Service; Status không đổi |
| Restore xe | Nút Restore trên xe Archived, bấm là chạy, không hỏi: "Record successfully restored!". Giữ trạng thái, đồng hồ, cấu hình trục; KHÔNG trả lại | Đã chạy | Chạy |
| Hiệu ứng của Archive | Archive thành công: liên kết với xe, công cụ mất ở cả hai phía; phân công đang chạy bị đóng ngay; phân công tương lai bị xoá hẳn; xe rời lịc | Đã chạy | Chạy |
| Tên xe, VIN không trùng | Form đơn báo Vehicle Name và VIN "has already been taken", "Vehicle could not be created". Trùng VIN xét cả xe Sample. Tên của xe đã Archive | Một phần | Chạy một phần: tên xe Archived chỉ thấy không báo, chưa lưu vì VIN vẫn trùng |
| Ẩn hiện thẻ cá nhân | Personalize › Manage Overview Layout: Available Cards 15, lọc thẻ, Visible Cards chia Left Column, Right Column, Restore defaults, Apply Cha | Một phần | Chạy phần ẩn hiện, Restore; kéo đổi thứ tự, Manage Tab Menu chưa thử |
| Layout form theo tài khoản | Customize Layout đưa vào Settings › Standard Records › Vehicle › Layout: "System Default", 4 Sections, 104 Fields, All (25) loại xe, nút Add | Chỉ xem | Xem |
| Bộ lịch bảo dưỡng trên xe | More Actions › Manage Service Programs đi tới `vehicles/{id}/service_programs`. Xe chưa có bộ lịch: trang rỗng dạng quảng bá "Efficiently sc | Một phần | Chạy phần mở, nút Create chưa bấm |
| Đính tài liệu dùng chung | More Actions › Attach Shared Document, ô "Select Document" chỉ liệt kê tài liệu dùng chung (tên, loại, thời điểm sửa), nút khoá tới khi chọn | Đã chạy | Chạy |
| Áp và sửa mẫu bảo hành | Áp mẫu sinh mỗi coverage một bảo hành riêng; dòng preview có Edit, Edit Maintenance Codes, Delete để sửa riêng lần này; mã bảo dưỡng của mẫu | Một phần | Chạy phần áp, áp về quá khứ; lựa chọn "future", ghi đè phần sửa riêng chưa thử |
| Cấu hình Motor Pool | Settings › Motor Pools › Add: Name, Groups, Vehicle Types, Vehicle Statuses (mặc định Active) bắt buộc; "Automatically calculate charges"; ' | Một phần | Chạy phần tạo pool; Auto Approvals, Rates, Flat Fees Xem |
| Form đặt xe | Operator, Motor Pool, Reason for Trip, Pick Up, Drop Off; chọn pool thì thêm Vehicle Types chỉ gồm loại của pool. Người đặt chọn loại xe, kh | Một phần | Chạy một phần: kiểm tra form, chưa tạo được đặt xe |

## Vehicles · Gán xe

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Gán xe | Assigned Vehicle, Operator, Start Date/Time ("Leave blank if assignment has always existed."), End Date/Time ("Can be past or future."), com | Đã chạy | Chạy |
| Chặn trùng gán | Không cho hai lần gán chồng thời gian trên **một xe**; không tự đóng phân công cũ. Không xét trùng theo người (BR-fleetio-vehicle-007). | Đã chạy | Chạy |
| Chỉ Operator được gán | Ô chọn chỉ hiện liên hệ phân loại Operator ("Allow this Contact to be assigned to assets"); liên hệ khác bị chặn bằng câu dẫn trên trang liê | Đã chạy | Liên hệ chỉ Technician không có trong ô chọn |
| Lịch gán | Mỗi xe một hàng, xem Day hoặc Week, thanh màu cam là tương lai, xanh là đang chạy, lịch tháng bên phải, gom theo xe hoặc người. | Đã chạy | Thêm, trùng, sửa đè người |
| Tạo gán từ ô lịch | Bấm ô trống mở "Add Vehicle Assignment For {xe}", xe khoá, ngày điền sẵn theo ô. | Đã chạy | Chạy |
| Sửa, thay người trên phân công | Edit đổi Operator đè lên phân công, xe khoá khi sửa. Không có hành động "thay người", trang chi tiết không còn dấu vết người cũ. | Đã chạy | Chạy |
| Chi tiết phân công | Trang "Vehicle Assignment #…": Operator, nhãn Future, Start, End, Duration, Start Meter, End Meter, Distance. Menu thanh lịch: View, Edit, D | Đã chạy | Chạy |

## Vehicles · Số đồng hồ

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Sổ đồng hồ | Mỗi dòng có ngày, giá trị, loại Primary hoặc Secondary, Void, Source, Void Status, Auto-Void Reason; hiện số hiện tại và khoảng cách với hiệ | Đã chạy | Lệch ngày bị từ chối |
| Tự huỷ số sai | Số vượt mức tối đa một ngày: lưu nhưng tự Void, lý do Exceeds Max. Daily Usage, popup có Last Meter Entry, Daily Usage, Max Daily Usage, Exc | Đã chạy | Biên 4.828 nhận, 4.829 Void; Out of Sequence có thật |
| Sửa xung đột | Dòng gây xung đột gắn cờ đỏ, Void Status "Conflict Source", popup "Conflicting Meter Entry" có số dòng ảnh hưởng và chênh lệch (ca Fleetio G | Đã chạy | Thêm hai popup xung đột từ ca Fleetio Go |
| Đổi đồng hồ | Không có bước khai báo "thay đồng hồ", không lưu lý do. Cách đã chạy: Void hàng loạt toàn bộ số của xe (FR-fleetio-vehicle-047), xe về "0 km | Một phần | Chặn: Số GPS cần tích hợp |
| Void tay khi nhập | Hộp nhập có ô Void; dòng thành "Manually Voided", không bao giờ là số hiện tại. | Đã chạy | Chạy |
| Unvoid | Hộp "This operation will attempt to unvoid the selected Meter Entry." rồi Confirm. Không hỏi lý do, không kiểm lại Max Daily Usage. | Đã chạy | Chạy |
| Chặn lệch thứ tự theo ngày | Số đồng hồ phải nằm giữa số ngày trước và số ngày sau; sai thì từ chối ở trường, trừ khi tick Void. Cùng luật cho Fuel Entry. | Đã chạy | Chạy |
| Đồng hồ phụ | Add Secondary Meter trong Settings của form xe ("Track an additional meter, such as a concrete mixer, street sweeper, cleaning equipment, et | Đã chạy | Thêm đồng hồ phụ, nhập riêng, chuỗi riêng |
| Void, Unvoid, Delete hàng loạt | Meter History tick nhiều dòng, mở Actions: Void, Unvoid, Delete. Chọn lẫn dòng đã Void và chưa Void thì Void, Unvoid đều khoá. Hộp "Void Met | Một phần | Chạy phần Void; Unvoid, Delete hàng loạt Xem |

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
| Lưu mẫu đảo tuỳ biến | Hiện "Save as a Custom Rotation Pattern" khi đã khép kín. Bỏ trống tên thì không đảo được. Mẫu thuộc cấp tài khoản, nằm ở Settings › Tire Ma | Một phần | Chặn: Mẫu đảo lưu trong Settings |
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
| Liên kết xe | Linked Vehicles hai chiều, khối "Linked Assets". Gỡ và gắn từ phía nào cũng được. Không truyền lốp, không truyền số km. Một mooc nối được nh | Đã chạy | Chạy |
| Báo cáo | Standard Reports chỉ có "Tire Activity Report"; thêm màn Tire Readings. | Đã chạy | Chạy |
| Đọc áp suất tự động | Công tắc "Automated tire pressure readings" ở Settings › Tire Management Settings › General, đang tắt, có icon khoá: "When enabled, Fleetio  | Một phần | Chặn: Công tắc Settings, cần telematics |
| Import lốp | Tài liệu hãng có mẫu import lốp, chưa chạy. Không thấy lối vào: Tire Readings không có menu "…"; menu Vehicle List có Add Multiple Vehicles, | Tài liệu | Chặn: Không thấy lối Import lốp ở nơi đã xem |
| Danh mục mẫu đảo ở Settings | Khối "Tire Rotation Patterns" có "Add Tire Rotation Pattern", cột Name, Type, Created, Axle Configuration. 8 mẫu đọc được đều Type Standard, | Chỉ xem | Xem |
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
| Lớp bản đồ | Vehicles, Places, Vendors bật tắt. Bật Vendors thêm marker nhà cung cấp và tab Places, Vendors ở danh sách. Tắt Vehicles có tác dụng thật: m | Một phần | Tắt Vehicles chạy; Shops không có nút, giữ Docs |
| Tải theo khung nhìn | Lấy vị trí theo khung đang xem, gọi lại khi đổi khung. | Đã chạy | Chạy |
| Nguồn vị trí | Từ tích hợp (`Docs`), API (`Docs`), từ phiếu kiểm tra (`Chạy`), từ phiếu dầu có chọn nhà cung cấp (`Chạy`, chi tiết ở FR-fleetio-location-di | Một phần | Phiếu dầu, phiếu dịch vụ tạo vị trí; tích hợp, API giữ Docs |
| Tìm và lọc | Ô "Locate vehicles, places, vendors on map..." tìm cả nhà cung cấp, xe, Place ("10 results available for search term TEST"), xếp nhà cung cấ | Đã chạy | Đủ 9 bộ lọc; tải lại thì mất lọc |
| Chi tiết khi chọn xe | Bấm marker hoặc dòng: không popup, panel trái đổi sang xe, marker gắn nhãn tên. Tab Overview có Alerts (Open Issues, Service Reminders, Inco | Đã chạy | Vị trí giả lập: panel, Nearby, Quick Add |
| Quan hệ gần | Dòng Place trong Nearby có khoảng cách. Rê chuột vẽ đường thẳng nét đứt từ xe tới Place, marker xe đổi thành marker Place trong lúc rê. | Đã chạy | Vị trí giả lập: đường nét đứt |
| Tuỳ chọn bản đồ | **Đã sửa tên:** Default (không phải Standard), Satellite, Grayscale; Labels hiện tên Place; Set Label Options (FR-fleetio-location-dispatch- | Một phần | Nhãn, vị trí mở đầu chạy; Street View không kéo được |
| Chú giải | **Đã sửa nghĩa:** Map Legend có Active, Idle, Stale là độ tươi vị trí, không phải xe chạy, nhàn rỗi; Place là tâm vùng; Preferred Shop, Prem | Đã chạy | Màu theo độ tươi: 30 phút, 1 giờ |
| Lịch sử vị trí | Tab Location History trên xe, mở từ More. Có ô Search, "Location Entry Date", "Location Entry Type" (Fuel Entry, Service Entry, Inspection), | Đã chạy | Tab, 3 loại nguồn, bộ lọc |
| Vị trí từ phiếu kiểm web | Web app đọc vị trí trình duyệt một lần lúc khởi động app, giữ giá trị và gửi kèm phiếu khi nộp. Phiếu ghi Submission Source "Fleetio Web App | Đã chạy | Chạy |
| Location Entry | Mỗi lần ghi vị trí có asset, loại, contact, thời điểm, Entry Type. Địa chỉ ngược có sau khoảng 1 phút, lúc đầu rỗng. `initial_place` cho biế | Đã chạy | Chạy (vị trí giả lập) |
| Quick Add | Nút Add trên panel, 11 mục: Draft Work Order, Add Vehicle Assignment, Add Expense Entry, Add Service Entry, Add Issue, Add Inspection Submis | Đã chạy | Chạy (vị trí giả lập) |
| Độ tươi vị trí xe | Trạng thái Active, Idle, Stale hiện trên Status, tuổi vị trí trên dòng danh sách. Marker xe hình xe đen nhỏ; chú giải vẽ icon khác nhau cho  | Đã chạy | Chạy (vị trí giả lập) |
| Điểm mở bản đồ | Mở theo IP của máy, không tự thu về xe. Center on Default Location; Map Starting Location đổi được bằng Use Current Map Center, trả lại bằng | Đã chạy | Chạy (vị trí giả lập) |
| Location Exception Tracking | Biểu mẫu có cờ Enabled. Trên web không tạo được cờ: mọi phiếu `location_exception` = false. Không so giữa các phiếu. Fleetio Go ghi toạ độ t | Đã chạy | Chạy (vị trí giả lập), Chạy (Fleetio Go) ca không vi phạm |
| Vị trí từ phiếu dầu có nhà cung cấp | Chọn nhà cung cấp trên phiếu dầu thì sinh Location Entry loại Fuel Entry tại địa chỉ nhà cung cấp, cùng giờ với phiếu. Source của Last Known | Đã chạy | Chạy |
| Nhãn marker xe | Set Label Options mở hộp một ô "Vehicle Marker Label" (đang Name), chú thích "Select field to display for Vehicle map marker labels. Falls b | Đã chạy | Đổi nhãn, trả về Name |
| Marker không gom cụm | Marker hiện riêng từng điểm ở mọi mức zoom đã thử, đè nhau khi gần; không có marker dạng số. Đã đếm tới 15 nhà cung cấp và 4 xe. | Một phần | Chạy một phần: 15 nhà cung cấp, 4 xe; chưa biết ngưỡng lớn hơn |
| Vị trí từ phiếu dịch vụ có nhà cung cấp | Chọn nhà cung cấp phân loại Service trên phiếu dịch vụ thì sinh Location Entry loại Service Entry, cùng giờ phiếu, tại vị trí quy từ địa chỉ | Đã chạy | Chạy |

## Places, Geofence

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Địa điểm | Tên, mô tả, địa chỉ, toạ độ, bán kính. Gõ toạ độ thì Address tự điền theo địa chỉ ngược, bản đồ tự chuyển. Vòng tròn đổi ngay khi chọn bán k | Đã chạy | Vùng tròn, đa giác, sửa bán kính |
| Sự kiện vùng | Hai loại Entered, Exited, sinh khi vị trí mới đổi quan hệ với vùng. Dùng làm Record Type của Automation. Không có màn danh sách riêng. | Đã chạy | Vị trí giả lập: Entered, Exited, Automation TEST chạy 2 lần |
| Vùng đa giác | Bấm biểu tượng đa giác, bấm các đỉnh, bấm lại đỉnh đầu để đóng. Hệ thống thay toạ độ bằng tâm, đổi Address theo tâm, khoá Geofence Radius vớ | Đã chạy | Chạy |
| Danh sách, trang địa điểm | Danh sách cột Name, Description, Address; lọc nhanh Location Entry Type, Location Entry Date, Place Geofence Radius. Trang chi tiết: tab Ove | Đã chạy | Chạy, Chạy (vị trí giả lập) phần Location Entries |
| Cảnh báo vùng | Add Alert Policy trên Place: Trigger (Vehicle is within, outside geofence; Contact is within, outside geofence), Which Vehicles?, Which Grou | Chỉ xem | Chặn: Hành động duy nhất là gửi email |
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
| Dựng biểu mẫu | Tạo trống, từ mẫu hệ thống, hoặc từ PDF, ảnh bằng Smart Upload (Beta); có màu, ngôn ngữ, Location Exception Tracking, Prevent Use of Stored  | Đã chạy | Smart Upload ra bản dựng dưới 30 giây |
| Loại mục kiểm tra | Date/Time, Dropdown, Free Text, Inventory Adjustment, Meter Entry, Number, Pass/Fail, Photo, Signature, Tire Readings, Section. Mọi loại trừ | Đã chạy | Inventory Adjustment trừ kho thật, 10 còn 7 |
| Luật từng mục | Bắt buộc, mô tả, hướng dẫn có định dạng, nhãn Đạt và Không đạt, N/A, bắt ảnh hoặc ghi chú; mục Số có khoảng, ngoài khoảng là Không đạt, biên | Đã chạy | Bắt buộc, ghi chú, E-001, E-003 |
| Workflow biểu mẫu | Trigger: If an item passes, If an item fails, If form is submitted; chọn "ANY Failed Inspection Item" hoặc từng mục Pass/Fail, Number, Dropd | Một phần | Pass, Fail chạy; email, gán người bị chặn |
| Gán biểu mẫu | All Vehicles, By Vehicle Attribute, Specific Vehicle; lịch Daily đến Yearly, Set Delayed Start, Enable Reminder Notification; không đặt lịch | Một phần | Chặn: Hạn luôn ở tương lai, Overdue phải chờ |
| Làm phiếu | Start Inspection mở Select Inspection Form, nhóm MOST USED và ALL. Mở từ xe thì chỉ liệt kê biểu mẫu đã gán cho xe đó. Chưa chọn xe thì form | Đã chạy | Không có nháp; lệch múi giờ |
| Vòng đời mục lỗi | Tab All, Needs Action, Open Issue, Acknowledged, Resolved; có Failure Timeline; Status trỏ sự cố, lệnh ("WO #100", "Resolved in Issue #49"). | Đã chạy | Create Issue, Reopen đã bấm |
| Xác nhận lại sau sửa | Tài liệu hãng: sự cố đã giải quyết thì người kiểm tiếp theo được hỏi xác nhận, từ chối thì tạo sự cố mới. Trên web không thấy câu hỏi nào; l | Một phần | Chặn: Cần Fleetio Go; web nối mục đạt với sự cố |
| Chống kiểm khống | Tài liệu hãng: gắn Location Exception khi tỉ lệ mục cùng vị trí vượt ngưỡng, hoặc một mục lệch xa điểm trung tâm; bật theo biểu mẫu. Trên we | Một phần | Chặn: Ca dương cần giả vị trí |
| Cấm ảnh có sẵn | Cờ "Prevent Use of Stored Photos", bật sẵn trên biểu mẫu mới. Bật: Pick File mở thẳng hộp chụp webcam, không có đường chọn file; máy không c | Một phần | Chặn: Cần cấp camera, chưa chụp |
| Ghi nhận lỗi | Acknowledge ở Needs Action mở hộp "Acknowledge Failure", Comments tuỳ chọn. Sau đó row menu chỉ còn "View Failure Timeline". | Đã chạy | Chạy |
| Gộp lỗi lặp | Mục lỗi lại khi sự cố còn mở: không tạo sự cố mới, thêm dòng Item Failures, thêm mốc Failure Timeline. Không báo gì cho người kiểm khi đang  | Đã chạy | Chạy |
| Phiếu ăn theo chuyến | Trường Job tự gắn việc đang gán cho xe lúc nộp, "Unassigned" khi không có; phiếu nộp đúng lúc rời vùng vẫn mang việc đang gán rồi việc mới k | Đã chạy | Chạy |
| Mục Meter Entry | Ghi số đồng hồ của xe từ phiếu, kiểm theo lịch sử đồng hồ; "Require Secondary Meter", "Require Photo Verification" bật sẵn; phiếu hiện dòng  | Một phần | Đồng hồ phụ chạy; ảnh webcam chưa |
| Phiên bản biểu mẫu | Sửa nhãn sau khi có phiếu: phiếu cũ giữ nhãn cũ, đầu phiếu có nhãn cam "Past Version". Phiếu đã nộp: "..." chỉ có Delete, có Print, không sử | Đã chạy | Chạy |
| Mục Inventory Adjustment | Trên phiếu: Part Location liệt kê kho; chọn kho mới hiện ô Parts "Search and add parts...", danh sách chỉ gồm phụ tùng có ở kho đó kèm tồn.  | Đã chạy | Trừ kho thật, 10 còn 7 |
| Vị trí từng mục trên Fleetio Go | Phiếu nộp từ Fleetio Go ghi cặp toạ độ riêng cho từng mục, phần web không có; gói phiếu có thêm `are_items_too_close`, `items_completed_too_ | Một phần | Chạy một phần lượt 3: Một phiếu không vi phạm, chưa có ca dương |
| Phiếu từ app Fleetio Go | User nộp trên điện thoại | Một phần | Phiếu #126102722; Chặn: thao tác trên app do user làm |

## Issues

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Tạo sự cố | Người dùng tạo sự cố cho một xe với tóm tắt, ngày báo; hệ thống tự điền người báo và thời điểm. Hạn theo ngày, đồng hồ là tuỳ chọn. | Đã chạy | Chạy |
| Nhiều nguồn sự cố | Sự cố đến từ nhập tay, phiếu kiểm tra hỏng, mã lỗi thiết bị, thu hồi; có trường Source liên kết về nguồn. Sự cố nhập tay có Source "—" (#52) | Một phần | Chặn: Recall là Sample, Fault cần thiết bị |
| Năm cách xử lý | Menu Resolve trên sự cố mở: Add to Service Entry, Draft Work Order, Add to Work Order, Get Service at Shop, Resolve with Note. Khi sự cố đã  | Một phần | Chặn: Enable sang Fleetio Pay, Access Denied |
| Đóng sự cố không sửa | Menu ba chấm › Close mở hộp có ô Note tuỳ chọn; đóng ghi Closed Date, Closed By, Note; ghi chú thành một Comment; mất Edit, Resolve. Không t | Đã chạy | Đóng, mở lại |
| Sự cố quá hạn | Sự cố có hạn theo ngày và số đồng hồ. Overdue là giá trị tính, không lưu: đọc lại mỗi lần theo ngày và đồng hồ hiện tại; hiện ở Issue Status | Đã chạy | Hạn, Overdue |
| AI xếp ưu tiên | Với sự cố mới, AI tự gán hoặc gợi ý mức ưu tiên, hiện dấu sao và câu "Auto-assigned priority". Có sự cố vẫn để "No Priority". | Đã chạy | Chạy |
| AI đóng sự cố | Tài liệu hãng: khi có Service Entry, AI đóng hoặc gợi ý đóng sự cố khớp nội dung. Với cấu hình hiện tại, entry 57902070 cùng đầu việc và nội | Một phần | Đợi lâu hơn, không đóng; bật tính năng bị chặn |
| Giải quyết kèm ghi chú | Resolve with Note mở hộp có Note bắt buộc, nút khoá khi trống. Sau lưu: Status Resolved, khối Resolution Details, nút Reopen, mất Edit. | Đã chạy | Chạy |
| Mở lại sự cố | Nút Reopen trên sự cố Closed hoặc Resolved bằng ghi chú, bằng entry mở hộp xác nhận; sự cố Resolved bằng lệnh thì nút khoá, tooltip nêu số l | Đã chạy | Chạy |
| Thêm vào Service Entry | Hộp "Add to Service Entry" liệt kê sự cố mở của xe, tick sẵn sự cố đang mở trang; chọn Add to New hoặc Add to Existing Service Entry, Contin | Đã chạy | Add to Existing, bỏ tick sự cố trong entry |
| Recall | Danh sách từ NHTSA theo năm, hãng, đời; tab All, Needs Action, Open, Resolved, Acknowledged; cột Issued At, Status, Issue, Manufacturer Camp | Chỉ xem | Chặn: Đọc menu Recall, không đổi Sample |
| Mức ưu tiên tự động của Issue | Issue mới có Priority "Auto-assign"; #40, #42 tự thành High dù không nhập mức. Xếp mức chạy nền: #55 lúc mới tạo hiện "Prioritizing", Record | Đã chạy | Chạy |

## Faults

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Mã lỗi thiết bị | Nhận mã lỗi, đánh dấu nghiêm trọng, gom các mã liên quan vào một sự cố; có trạng thái Open, Pending, Resolved, Ignored; menu dòng Create Iss | Chỉ xem | Chặn: Menu, sự cố gom 3 mã; chỉ Sample |
| Luật mã lỗi | Khai mã, mô tả và mức nghiêm trọng theo khách; có mẫu bỏ qua mã phiền. Hộp Add Fault Rule: Code bắt buộc, phải khớp chính xác mã đến; Name,  | Chỉ xem | Chặn: Đọc hộp Add Fault Rule, huỷ, không lưu |

## Service Reminders

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Tạo nhắc hai trục | Nhắc gắn xe và đầu việc, chu kỳ theo thời gian và đồng hồ, chỉ cần một trục, trục nào đến trước thì tính; ngưỡng Sắp đến hạn riêng từng trục | Đã chạy | Mốc từ 0, biên |
| Lấy lần gần nhất | Khi chọn xe và đầu việc, form hiện lần hoàn thành gần nhất, lấy từ lịch sử; chưa làm lần nào thì hiện "Never logged for this vehicle". | Đã chạy | Chạy |
| Xem trước lịch | Form hiện 5 kỳ tới với ngày và số km, kể cả kỳ đã qua ("1,000 km / 1,300 km ago"); lỗi ngưỡng báo ngay trong khối này. Form Edit không làm m | Đã chạy | Chạy |
| Tính trạng thái | Upcoming, Due Soon, Overdue đổi ngay khi lưu số đồng hồ từ bất kỳ nguồn nào, không chờ job đêm; lấy trục xấu nhất. Chuyển do thời gian trôi  | Đã chạy | Biên ngưỡng, Void |
| Reset khi xong | Đầu việc ghi nhận trên Service Entry hoặc lệnh Completed thì nhắc tính kỳ sau từ lần làm. Lệnh Open không đổi trạng thái. | Đã chạy | Đóng bằng lệnh, phiếu dịch vụ, sớm, lùi ngày |
| Tạm hoãn | Hộp "Snooze Service Reminders" (số nhiều vì dùng chung với thao tác hàng loạt): ô "Snooze Until" ngày và giờ, mặc định +7 ngày, giờ theo thi | Đã chạy | Hoãn và huỷ hoãn trên Upcoming |
| Xử lý từ nhắc | Resolve chia 2 nhóm: GET SERVICE có Draft Work Order, Add to Work Order, Find a shop; LOG COMPLETED SERVICE có Add to service history. Menu  | Một phần | Chặn: Assign gửi email, SMS |
| Tỷ lệ tuân thủ | Tỷ lệ việc đúng hạn trên việc đã xong; thẻ Completed, Late, On-Time Compliance theo nhắc; trung bình theo danh sách lọc (D 100%, F 100%, Bra | Đã chạy | Biên km: +100 Late, +99 On-Time |
| Dự báo ngày đến hạn | Ước tính ngày đến hạn từ số km trung bình ngày cho từng thuộc tính của nhắc; thuộc tính đến trước có cờ ưu tiên. Bật bằng ô "Forecasting" ở  | Một phần | Đo công thức, trạng thái, nhóm; thiếu số km tự tính |
| Giao nhắc cho người | Tài liệu hãng: giao nhắc quá hạn cho người lái; nhận email hoặc tin nhắn, xác nhận được. Trên web có cột Assignee, Assigned At nhưng chưa th | Chỉ xem | Chặn: Không thấy lối giao; không gửi thông báo |
| Chi tiết nhắc | Nút Unwatch, "...", Edit, Resolve; khối Details (Vehicle, Operator, Status, Service Task, Service Program, Next Due, Last Completed, Work Or | Đã chạy | Chạy |
| Đặt tay mốc kỳ tới | Tick "Manually set the due date and/or meter for the next reminder" mở Next Due Date, Next Due Primary Meter, mặc định hôm nay + chu kỳ và đ | Đã chạy | Chạy |
| Sửa nhắc | Edit khoá Vehicle, đổi chu kỳ thì tính lại ngay, không cảnh báo, không bắt lý do, không hiện ở tab History; có ghi ở Record History (FR-flee | Đã chạy | Chạy |
| Gộp nhắc vào lệnh | Resolve, Add to Work Order mở hộp liệt kê mọi nhắc của xe để tick thêm, chọn lệnh mới hoặc có sẵn. Lệnh Open: nhắc hiện "Work Order #101, Ad | Đã chạy | Chạy |
| Đóng nhắc bằng phiếu dịch vụ | Add to service history mở "Log completed service": nhập tay hoặc Smart uploads (mặc định). Hoặc New Service Entry, gõ đầu việc ở Line Items: | Đã chạy | Smart uploads chạy trọn đến phiếu lưu |
| Ghi tuân thủ từng lần | Mỗi lần hoàn thành có dòng Due, Completed, nhãn On-Time hoặc Late, chênh trên từng trục ("3 weeks, 6 days ahead · 1,600 kilometers ahead").  | Đã chạy | Chạy |
| KPI danh sách nhắc | Thẻ Overdue Vehicles, Due Soon Vehicles, Snoozed Vehicles đếm xe, không đếm nhắc; Average Compliance; tab Due Soon, Overdue có số; cột Next  | Đã chạy | Chạy |
| Bản nháp lệnh bằng AI | Resolve › Draft Work Order, chỉ mở khi nhắc Due Soon hoặc Overdue: toast "Drafting service", "No need to wait here — we'll notify you when t | Một phần | Chạy trên Overdue; Add to chưa bấm |
| Nhật ký thay đổi bản ghi | Menu "..." › View Record History mở hộp có lọc khoảng ngày, cột Date, Changes By, Changes Made; ghi tên trường kỹ thuật và giá trị trước, sa | Đã chạy | Chạy |
| Thao tác hàng loạt trên nhắc | Tick dòng, mở "Actions": GET SERVICE có Add to Work Order, Find a shop; LOG COMPLETED SERVICE có Add to service history; OTHER có Snooze Ser | Chỉ xem | Xem |
| Smart Upload phiếu dịch vụ | Hộp toàn màn: trái trình xem tài liệu, phải "Review Service Entry", "Review and edit for accuracy before adding the service entry."; các ô h | Đã chạy | Chạy |
| Đánh giá phiếu dịch vụ bằng AI | Sau lưu, phiếu có khối "Assessment": "Reviewing this service", "Checking service history"; không có giá thì "Add line item costs to run an a | Một phần | Chạy một phần lượt 4: Đọc kết quả; chưa thêm rule |
| Giao dịch vụ thuê ngoài từ nhắc | Resolve › Find a shop mở hộp "Assign outsourced service", 3 bước Service Details, Suggest Shop, Confirm. Service Details: Assign to, Vehicle | Một phần | Chạy một phần lượt 4: Đến Confirm; không bấm Assign vì gửi email, SMS thật; không thấy danh sách cửa hàng |
| Giải trình phép tính dự báo | Popover "Next Due" trên danh sách, chi tiết: từng thuộc tính (Scheduled Date, Primary Meter) kèm cờ ưu tiên. Popover "Meter Forecast" bày từ | Đã chạy | Chạy |
| Nhóm nhắc theo tuần, tháng | Menu Group có thêm Week, Month khi bật Forecasting; khi tắt chỉ còn None, Vehicle. Tiêu đề nhóm theo dải ngày, "This Week", "Next Week", "Th | Đã chạy | Chạy |

## Service Programs

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Bộ lịch | Một bộ gồm nhiều lịch cho nhiều xe, có mẫu, đồng hồ chính (Miles, Kilometers, Hours) và phụ; một dòng lịch chọn được nhiều đầu việc; sửa lịc | Đã chạy | Đã gắn xe, sinh 2 nhắc |
| Đối chiếu khi gán bộ lịch | Trước khi lưu có bảng Service Task, Conflicting, Duplicate, New Interval và câu cảnh báo chung. Lịch có "Set First Service". "Save as a Serv | Một phần | Chặn: Rule khoá khi còn Sample Data |
| Gỡ xe khỏi bộ lịch | Row menu chỉ có Delete, không có đường gỡ khác; hộp "Confirm Service Program Vehicle Deletion" nêu sẽ xoá mọi nhắc từ bộ này trên xe. Không  | Chỉ xem | Chặn: Chỉ có Delete, không xoá |
| Mẫu bộ lịch hệ thống | New Service Program có Fleetio: 14 mẫu (Basic Vehicle Maintenance, Light Duty Truck Maintenance, Heavy Duty Truck Short Haul, Long Haul, 10  | Đã chạy | Chạy |
| Lịch theo đồng hồ phụ | Bộ lịch bật Secondary Meter = Hours: form lịch mở 3 trục Time, Primary Meter, Secondary Meter; "Secondary Meter Due Soon Threshold" tự điền  | Một phần | Chạy một phần lượt 3: Lưu lịch; chưa sinh nhắc trên xe thật |
| Điều kiện gán bộ lịch | New Service Program Vehicles: By Vehicle Attribute, All Vehicles, Specific Vehicles; điều kiện đầu khoá sẵn "Primary Meter is equal to Kilom | Một phần | Chặn: Rule khoá khi còn Sample Data |

## Renewals

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Gia hạn giấy tờ | Nhắc theo loại có sẵn, cho xe và liên hệ, có ngày đến hạn, ngưỡng báo, người theo dõi. Fleetio: loại xe Emission Test, Inspection, Insurance | Đã chạy | Gia hạn xe |
| Gia hạn bằng sửa tay | Bấm dòng mở panel phải "Contact Renewal #..." có Edit, "...": View, Send Notifications, View Record History, Delete. Trang chi tiết chỉ có D | Đã chạy | Chạy |
| Gia hạn liên hệ |  | Đã chạy | Mở chi tiết, sửa hạn, đọc Record History |

## Work Orders

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Tạo lệnh | Lệnh có xe, trạng thái, phân loại ưu tiên, ngày lập, người lập, người nhận việc, ngày dự kiến và thực tế, xưởng ngoài, hoá đơn, số đơn mua.  | Đã chạy | Form đủ trường, số lệnh |
| Gắn sự cố vào lệnh | Form lệnh liệt kê sự cố của xe theo tab Open, Resolved, Closed; Overdue nằm trong tab Open; tick để gắn; gắn được với từng dòng việc qua Lin | Đã chạy | Link Issues vào dòng; khoá sự cố ở lệnh khác |
| Dòng việc | Dòng việc gồm đầu việc, công, phụ tùng, ghi chú, mã phân loại tự điền (Reason, Category, System, Assembly), Last Completed, Add Service Remi | Đã chạy | Công, phụ tùng, lỗi tiền 100 lần |
| Ghi công | Hộp Add Labor: Technician bắt buộc, Labor Hours mặc định 1 kèm nút chọn nhanh, Hourly Rate, Service Task, Note, Subtotal, "Save and Add Anot | Đã chạy | Nhập công; web không có nút bấm giờ |
| Tổng hợp chi phí | Tính tổng công, phụ tùng, markup công, markup phụ tùng, tín dụng bảo hành, giảm giá, thuế. Mỗi ô đổi được giữa phần trăm và số tiền. Thứ tự  | Đã chạy | Markup phụ tùng % và cố định, trả tồn |
| Đổi trạng thái lệnh | Đổi trạng thái ngay trên đầu trang. Open và Pending đổi qua lại không hỏi; Pending sang Completed đi thẳng được; hệ thống kiểm điều kiện the | Đã chạy | Open, Pending, điều kiện hoàn thành |
| Hoàn thành lệnh | Khi chuyển sang trạng thái loại Completed, hệ thống giải quyết sự cố đã chọn, ghi nhận đầu việc, tính Duration, tạo Service Entry, ghi Time  | Đã chạy | Điều kiện, số cuối nhỏ hơn đầu |
| Mở lại lệnh | Đổi lệnh Completed về chưa xong qua hộp "Update Status". Service Entry bị xoá hẳn, URL ra Not Found; sự cố về Open, mất Resolution Details v | Đã chạy | Mở lại lệnh đã Completed |
| Xem lệnh ba chế độ | Danh sách, lịch tháng, lịch tài nguyên theo xe hoặc kỹ thuật viên. | Đã chạy | Chạy |
| Tình trạng từng dòng | Tài liệu hãng: đánh dấu xong từng dòng, không kích hoạt hiệu ứng hoàn thành; cấu hình bắt buộc xong hết mới hoàn thành lệnh. Trên web với tà | Một phần | Chặn: Web không có ô dòng, cấu hình ở Settings |
| Sao chép, in, gửi | More Actions: Run Assessment, Print, Make a Copy, View Record History, Email PDF, Delete. Print mở PDF tab mới. Make a Copy mở form mới: xe  | Một phần | Đọc được PDF; Email PDF chặn, Delete không làm |
| AI soạn lệnh | Từ sự cố, AI soạn nháp chạy nền, đổi dòng chữ tiến độ; rời trang vẫn chạy. Hộp review: cảnh báo lệnh đang mở của xe, nhóm "Resolves this iss | Đã chạy | Nhiều sự cố, tạo mới, thêm vào lệnh đang có |
| AI đánh giá lệnh | Khi có đầu việc và chi phí, AI tự chạy trên lệnh, kiểm công và giá phụ tùng, kết luận Acceptable hoặc Needs Review, ghi nguồn; cho chạy lại  | Đã chạy | Đủ, thiếu, Rerun, sai số |
| Số đồng hồ trên lệnh | Start Odometer và tick "Use start odometer for completion meter" mặc định bật; bỏ tick hiện Completion Odometer. Lưu hai mốc tạo hai dòng Me | Đã chạy | Chạy |
| Phân loại ưu tiên lệnh | Repair Priority Class gồm Scheduled, Non-Scheduled, Emergency, ghi rõ VMRS Code Key 16; bật được bắt buộc. | Đã chạy | Chạy |
| Khoá và gỡ sự cố khỏi lệnh | Sự cố đã gắn lệnh thì khoá lối khác kèm tooltip, gồm cả Close ("...already added to a Work Order. Remove it from all Work Orders to close"); | Đã chạy | Chạy |
| Tồn kho theo dòng phụ tùng | Hộp Add Part chọn kho, ghi "This will make an inventory adjustment" hoặc "None (No Inventory Adjustment)". Lưu lệnh trừ tồn ngay khi lệnh cò | Đã chạy | Chạy |
| Giao việc, theo dõi | Sửa so với bản trước: Assigned To không chỉ người có nhãn Technician, danh sách có cả Employee, Operator, Account Owner và "Fleetio Automati | Một phần | Giao cho user tự theo dõi; user thứ hai chặn |
| Hoàn thành lại | Lệnh đã mở lại đổi Completed lần nữa: tạo entry mới số khác, dùng ngày và đồng hồ cũ của lệnh, không hỏi lại; Timeline sự cố lại có dòng giả | Đã chạy | Chạy |
| Danh mục trạng thái lệnh | Bảng trạng thái có Name kèm màu, Default, mô tả; Type; số lệnh; mặc định Open, Pending loại Incomplete, Completed loại Completed. Khách thêm | Một phần | Đủ vòng tuỳ biến; chưa kéo sắp xếp, chưa đo nhắc |
| Đưa ra xưởng ngoài | Get Service at Shop mở hộp giới thiệu Shop Network, cần Enable Shop Network mới dùng. Mục vẫn sáng cả khi sự cố đang gắn lệnh. Bấm Enable ch | Chỉ xem | Chặn: Enable sang Fleetio Pay, Access Denied |
| Đơn giá công theo contact | Contact Technician có đơn giá mặc định; danh sách chọn và hộp Edit Labor hiện đơn giá đó. | Đã chạy | Chạy |
| Sổ thay đổi theo trường | Hộp Record History của lệnh: lọc "Select Date Range", cột Date, Changes By, Changes Made. Ghi từng trường tiền, phần trăm, dòng việc, dòng c | Đã chạy | Chạy |
| Mốc thời gian của dòng công | Tick "Set Labor Time Entry" hiện Start Date, End Date để tạo Time Entry; End tự bằng Start cộng số giờ, đổi nút giờ thì End đổi theo. | Đã chạy | Chạy |

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
| Bảo hành | Khai bảo hành theo ngày và số km, cho nhiều xe một lượt, mỗi xe một Start Date, Start Meter; Standard Warranty, Standard templates, Extended | Đã chạy | Tạo mẫu, áp cho xe, sinh bảo hành |
| Cơ hội bảo hành trên lệnh | Khối Warranty Opportunities luôn hiện trên lệnh: đếm active, expiring soon, total; Vehicle Coverage khớp đầu việc theo mã phân loại đúng từn | Đã chạy | Khớp theo mã, trạng thái; điền Complaint, Cause, Correction |
| Tạo bảo hành nhiều xe | Form "New Warranties" 2 bước: Vehicles (nhiều xe, mỗi xe Start Date, Start Meter riêng) rồi Coverage Type: Standard Warranty, Standard templ | Đã chạy | Chạy |
| Tự tính hạn bảo hành | End Date = Start Date + Coverage Duration; End Meter = Start Meter + Coverage Distance; Status "Active". Danh sách có số active, expiring so | Đã chạy | Chạy |
| Gắn mã bảo dưỡng vào bảo hành | Maintenance Categorization nhập mã hệ thống (VMRS), có Bulk Mode, Column Mode. | Đã chạy | Chạy |
| Mẫu bảo hành | Coverage Template "contain a collection of coverages based on manufacturer guidelines". Settings › Warranty Templates: Add, form Name, Meter | Một phần | Mẫu riêng, OEM đọc được; lựa chọn future chưa chạy |
| Mã phân loại, thành phần bảo hành | Hộp Add Maintenance Categorization có Bulk Mode, Column Mode, nhận mã System hoặc System–Assembly, phần thứ ba bị bỏ; menu "…" có Edit, Clea | Một phần | Chạy một phần: mã chạy; Add Component chưa lưu |
| Bảo hành theo xe, lưu liên tiếp | Tab Warranties của xe: Name, Manufacturer, Coverage Type, Start Date, End Date, Start Meter, Coverage Distance, End Meter, Status. "Save & A | Một phần | Chạy một phần: tab, lưu liên tiếp; template không có |
| Mẫu bảo hành và áp thay đổi | Settings › Warranty Templates: mẫu có Name, Meter Unit, các coverage đủ trường như bảo hành thường; Save khoá tới khi có coverage. New Warra | Một phần | Chạy một phần: mẫu riêng, áp quá khứ; chưa chạy áp tương lai |

## Parts & Inventory

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Danh mục phụ tùng | Mã duy nhất, mô tả, nhóm, hãng, mã hãng, UPC, đơn giá, đơn vị, bảo hành, ảnh, tài liệu. Không có trường thay thế, tương thích xe trong form, | Đã chạy | Form không có thay thế, tương thích |
| Kho và hoạt động theo kho | Phụ tùng bật tại nhiều kho, mỗi kho có vị trí dãy, hàng, ô; số lượng; điểm đặt lại. Tên kho không trùng. Kho khai ở Settings; bật phụ tùng t | Đã chạy | Nhiều kho, tồn theo kho |
| Thẻ tồn | Theo kho: Current Qty, Reorder Point, Pending PO Qty, WO Current Qty; bốn nút điều chỉnh, chuyển kho, đặt mua, menu (Edit, View History). Cá | Đã chạy | Chạy |
| Sổ kho | Mỗi biến động ghi ngày, kho, loại, chứng từ, lý do, nhà cung cấp, số biến động, số trước, số sau, người, ghi chú. Sáu loại: Initial, Manual, | Đã chạy | Chạy đủ sáu loại |
| Điều chỉnh tồn | Hộp theo một kho: Adjust Quantity và New Quantity liên động, lý do bắt buộc trong 11 giá trị, ghi chú, chấp nhận số lẻ. Không chặn giảm quá  | Đã chạy | Chỉnh âm không chặn |
| Chuyển kho | Nhập số chuyển, chọn kho đích, danh sách đích chỉ gồm kho còn lại kèm tồn. Nút khoá khi tồn từ 0 trở xuống. Nhập quá tồn thì cắt về tồn hiện | Đã chạy | Tự cắt số lượng |
| Cảnh báo tồn thấp | Nhãn theo từng kho: Low Stock khi tồn trên 0 và từ điểm đặt lại trở xuống, số màu cam; Out of Stock khi từ 0 trở xuống. Điểm đặt lại 0: tồn  | Một phần | Chặn: Email tồn thấp |
| Tính giá tồn | Chọn một trong Average Cost, FIFO, LIFO, Static Pricing. Static: Unit Cost phụ tùng giữ theo danh mục dù đơn mua giá khác; Total Inventory V | Một phần | Chặn: Đổi một chiều, chờ user quyết; đọc cảnh báo |
| Xuất phụ tùng cho lệnh | Chọn phụ tùng thấy tồn từng kho; lấy từ kho hoặc None không trừ kho; gắn đầu việc. Trừ ngay khi lưu. Không cảnh báo khi vượt tồn. | Đã chạy | Chạy |
| Bulk Manage Parts | Tab theo kho; cột Aisle, Row, Bin, Active?, Track Inventory, Current Qty, Last Quantity Update; sửa ô là tự lưu, sổ loại Bulk Update, không  | Đã chạy | Print Worksheet tự tải PDF |
| Nhiều nhà cung cấp, lịch sử giá | Thêm nhà cung cấp, giá trong Purchase History; đơn mua tự thêm dòng lịch sử; trang phụ tùng vẽ biểu đồ giá. | Đã chạy | Chạy |
| Sửa, xoá dòng phụ tùng trên lệnh | Sửa số lượng hoặc xoá dòng thì sổ ghi bù, loại Work Order kèm số lệnh; xoá có hộp xác nhận. | Đã chạy | Chạy |
| Tác động của hoàn thành, mở lại lệnh | Hoàn thành: sổ không có dòng mới, sinh Service Entry, Edit khoá; cần Started At, Start Odometer theo cài đặt. Mở lại: sổ không đổi, liên kết | Đã chạy | Chạy |
| Phiếu kiểm kê in | Print Worksheet ở Bulk Manage: một cú bấm, không mở tab, tự tải PDF theo kho đang chọn. PDF một trang: tên, địa chỉ tài khoản; Part, Categor | Đã chạy | Chạy |
| Menu trang phụ tùng | "Update Quantity", "Archive" (mờ với PT-A), "View Record History". | Chỉ xem | Xem |
| Đổi phương pháp tính giá tồn | Settings › Parts & Inventory › Inventory Valuation Method: 4 radio có mô tả, không có nút Save. Chọn radio khác mới hiện khối cảnh báo, ô tí | Chỉ xem | Xem câu chữ; chưa bấm Activate, chưa đo giá |

## Purchase Orders

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Lập đơn mua | Một nhà cung cấp, một kho rồi mới thêm dòng; chỉ hiện nhà cung cấp có Parts; đơn giá lấy từ danh mục, sửa được; giảm giá, phí vận chuyển, th | Đã chạy | Chạy |
| Duyệt đơn | Có quyền duyệt thì Save & Approve hoặc Approve, một cú bấm, không hộp xác nhận, duyệt được đơn của mình. Không có quyền thì Submit for Appro | Một phần | Chặn: Cần người thứ hai |
| Một nút chính mỗi bước | Approve, Mark as Purchased, Receive, Close; ghi người và thời điểm mỗi bước. | Đã chạy | Chạy |
| Nhận hàng | Bảng Item, Total Received, Total Ordered, Receive; nhận nhiều lần, lần sau gợi ý số còn lại. Không chặn nhận vượt. Trạng thái tính theo từng | Đã chạy | Chạy |
| Nơi đến khi nhận | Inventory, Existing work order, New work order. Hai nhánh lệnh đều nhập kho trước, trừ khi lưu lệnh, dòng ghi chú "From PO #n". `Docs`: chỉ  | Đã chạy | Vào kho, vào lệnh |
| Make Adjustment trên đơn | Có ở Full, Closed; không có ở Partial, Purchased. Tick từng dòng rồi nhập; bảng Item, Total Received, Total Ordered, Adjustment; nút Make Ad | Đã chạy | Từ Closed: giảm 1, vẫn Closed |
| Đóng đơn | Close từ Partial, Full; hộp xác nhận; đóng được khi nhận thiếu, không ghi lý do; ghi Closed By. Không có nút mở lại. Không có trạng thái, nú | Đã chạy | Chạy |
| Sửa đơn theo trạng thái | Draft: nhà cung cấp, kho mở, có Add Line Item, nút xoá dòng, "Save as Draft", "Save & Approve". Approved: đủ trường, thêm bớt dòng được, "Sa | Đã chạy | Draft, Full lưu thật |
| Lùi trạng thái đơn | Save as Draft từ Approved về Draft, nằm trong form Edit, không có trong menu; mất dòng Approved By. Unmark as Purchased từ Purchased về Appr | Đã chạy | Chạy |
| Sao chép đơn | Make a Copy mở form mới điền sẵn nhà cung cấp, kho, dòng, số đặt, giá đơn cũ, chiết khấu; số tăng lên; không chép số đã nhận; lưu ra Draft.  | Đã chạy | Chạy |
| In và lịch sử bản ghi đơn | Print: mở tab "Preparing your PDF...", ra `purchase_order_{số}.pdf` một trang gồm thông tin đơn, người và ngày từng bước, dòng hàng, Subtota | Đã chạy | PDF, Record History, thêm Make a Copy |
| Số đang về theo trạng thái đơn | Đơn chưa Edit: Draft, Approved không tính, tính từ Purchased. Đơn Draft đã Edit và lưu: số vào Pending ngay dù chưa duyệt, theo số mới mỗi l | Một phần | Đo PO #4, #5; Approved đã Edit chưa đo |

## Vendors

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Nhà cung cấp | Tên, địa chỉ, thành phố, tỉnh, mã bưu chính, quốc gia bắt buộc; liên hệ; phân loại Charging, Fuel, Parts, Service, Vehicle không bắt buộc nh | Một phần | Rating là số; nguồn điểm chưa rõ |
| Tạo nhanh trong ô chọn | Gõ tên chưa có thì chọn Create, mở form với tên điền sẵn và phân loại theo ngữ cảnh. | Đã chạy | Chạy |
| Trang nhà cung cấp | Tab Overview, Fuel Entries, Purchase Orders theo phân loại; tab đơn liệt kê đơn của nhà cung cấp. "Network Status: Invite" không bấm vì mời  | Một phần | Chặn: Invite là mời người ngoài |
| Tìm xưởng (Find Shops) | Hộp "Select service shops and easily save them to your vendors list", ô "Enter address, city or ZIP/postal code", ô "Shop type", "Let's Go". | Đã chạy | Chạy tới bước tick; Add Vendor không bấm |

## Fuel

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Phiếu dầu | Xe, ngày, số đồng hồ, số lít, đơn giá, loại dầu, nơi đổ, tham chiếu, ảnh, tài liệu. Nơi đổ chỉ gồm nhà cung cấp có Fuel; có nhà cung cấp thì | Đã chạy | Chạy |
| Tính tiêu hao | Từ phiếu trước theo số đồng hồ: quãng đường, tiêu hao, chi phí trên km, chênh so với lần trước. Cộng dồn phiếu Partial. Tính đúng nhưng xe k | Đã chạy | Chạy |
| Cờ phiếu dầu | Personal vẫn tính tiêu hao, vào Cost of Ownership và cộng vào thẻ tổng Fuel History (F22). Partial cộng dồn sang phiếu sau. Reset usage: phi | Đã chạy | Void, Personal vẫn cộng thẻ tổng |
| Thẻ tổng hợp dầu | Tổng tiền, tổng lượng, tiêu hao trung bình, chi phí trung bình theo bộ lọc, tính lại khi đổi lọc. Tính cả phiếu Void, Personal (F22). Trên V | Đã chạy | Chạy |
| Cảnh báo sai vị trí | Vị trí xe khi đổ xa nhà cung cấp hơn bán kính đặt thì gắn Vendor Location Alert; tắt được. Chỉ thấy tên loại ở bộ lọc (F18); không chạy được | Chỉ xem | Chặn: Cần tích hợp; chỉ thấy tên loại |
| Cảnh báo vượt dung tích | Số lít lớn hơn dung tích bình đã khai thì gắn Capacity Alert và ghi Capacity Exception Volume, kể cả phiếu nhập tay. Bằng dung tích không cả | Đã chạy | Nhập tay có cảnh báo, biên 60 và 60,5 |
| Void phiếu dầu | Tick Void, số đồng hồ vẫn bắt buộc; lưu thì số gạch ngang, đồng hồ xe không đổi, không Usage; vẫn tính vào chi phí xe và vẫn cộng vào Total  | Đã chạy | Chạy |
| Bộ lọc phiếu dầu | Date, Vehicle, Vehicle Group, Vendor, Filters; panel có Add Filter, Add Filter Group, Fleetio: tối đa 3 nhóm OR. Date mặc định 30 ngày gần n | Đã chạy | Vendor, Alert Type, Personal chạy |
| Thẻ dầu trên phiếu | Ô Fuel Card ghi "No"; cấu hình WEX chỉ đọc; không có màn gán thẻ thử được. Dữ liệu thẻ gắn ở mức phiếu: bộ lọc có Transaction Card Number, T | Chỉ xem | Chặn: Chỉ thấy trường Transaction ở bộ lọc |
| Loại cảnh báo dầu | Fuel Alert Type có đúng 3 giá trị: "Vendor Location Alert", "Fuel Capacity Alert", "Missing GPS Location Alert". Lọc được theo loại. | Một phần | Chạy lọc Fuel Capacity Alert; hai loại còn lại Xem tên |

## Reports, hỏi dữ liệu

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Báo cáo chuẩn | 49 báo cáo 13 nhóm; yêu thích, lưu, chia sẻ; dạng lưới, danh sách; nhãn "Upgrading soon" trên 4 báo cáo. Bảng nhóm ở Mục 18; đủ tên, đường d | Một phần | Đọc bộ lọc 47 báo cáo, lọc thật 1; expense_entries lỗi 500 |
| Hỏi dữ liệu | Nút Ask a data question trên đầu trang mở AI Data Analyst, khung nhúng từ ThoughtSpot; hỏi bằng lời ra bảng; Show work, chọn All data models | Đã chạy | Trả lời sai số |
| Trang báo cáo | Issues Report: biểu đồ Summary, Top Vehicles; Filters, Columns, phân trang; Save, Share, Export CSV (Export Visible Columns, Export All Colu | Một phần | Đọc 48/49, lọc thật 1 |
| Chia sẻ báo cáo bằng link | Bấm Share sinh ngay link công khai, có hạn (Fleetio: 7 ngày); "this link allows anyone with access to view all data". Reports › Shared liệt  | Đã chạy | Chạy |
| Hai thế hệ báo cáo, khối cột xe | Thế hệ mới (34 báo cáo) có Save, Share, Export CSV, Print, Filters, Columns, nhiều cái có biểu đồ; thế hệ cũ (15 báo cáo) chỉ thấy Save, Fil | Đã chạy | Chạy chỉ đọc 48/49; expense_entries lỗi 500 |
| Báo cáo đã lưu | Hộp New Saved Report: Name *, Description, Visibility Public hoặc Private (mặc định Private), Email Schedule. Reports › Saved cột Name, Desc | Một phần | Chạy một phần: Private; Public, Email Schedule không chạy |
| Ba kiểu bộ lọc báo cáo | Kiểu A: panel ô cố định, nút Search, đa số báo cáo mới. Kiểu B: filter builder "No filters applied.", Add Filter, Popular Filters như danh s | Một phần | Chạy một phần: Đọc nhãn, lọc thật 1 báo cáo; expense_entries lỗi 500 |

## Automations

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Tự động hoá | Trigger gồm loại bản ghi và kiểu sự kiện; điều kiện tuỳ chọn; hành động Update Field, Add Comment, Send Email, Create Record; có bật tắt, ph | Một phần | Chặn: Send Email; Update, Comment đã có |
| Loại bản ghi tự động hoá | Work Order, Service Entry, Fault, Issue, Purchase Order, Geofence Event, Vehicle. Kiểu sự kiện gồm Created, Updated, Created or Updated, Del | Một phần | SE, PO chạy thật; Fault chỉ lưu, không phát sinh |
| Mẫu tự động hoá | 18 mẫu: Faults 2, Issues 5, Purchase Orders 3, Service Entries 2, Work Orders 6; gợi ý đúng lúc ngay sau hành động liên quan. Bảng từng mẫu  | Đã chạy | 18/18 mẫu đọc đủ |
| Danh sách tự động hoá | Cột Name, Status, Trigger Record, Total Runs, Successful Runs, Failed Runs, Created By, Last Run At, Current Version; tab All, Archived; lọc | Đã chạy | Chạy |
| Thư viện mẫu | Browse Templates: cột trái theo loại trigger, thẻ có sơ đồ trigger, số điều kiện, số hành động, nút Apply khi rê chuột. Apply mở trình dựng  | Đã chạy | Chạy |
| Bật tắt có xác nhận và phiên bản | Lưu xong ở trạng thái tắt; bật phải qua hộp xác nhận và lúc đó sinh phiên bản v.1, ghi Enabled At; tắt cũng có hộp xác nhận. Tắt rồi bật lại | Đã chạy | Sửa khi bật lên v.2, chạy theo v.2 |
| Archive và Restore automation | Archive không cần tắt trước, tắt ngay, ghi Disabled At; bản Archived chỉ đọc; Restore về Disabled, không tự bật. Khi chưa Archive, menu More | Đã chạy | Archive khi bật, Restore về Disabled |
| Run History và Run Result | Mỗi lượt có kết quả, phiên bản, Processed At, Records, bản ghi kích hoạt, Trigger Type, Triggered At, Triggered By, View Full Log dạng JSON  | Đã chạy | Có cả lượt FAILURE |
| Trình dựng điều kiện | Với Issue: 59 trường, chia nhóm Issue, Tool, Vehicle, Vehicle or Tool; All of, Any of; nhóm điều kiện lồng, hiện "And", "Or" ở khung trái. S | Đã chạy | Nhóm lồng All of + Any of, khớp đúng |
| Hành động Create Record | Tạo Work Order từ Issue; chỉ có Status, Assigned To, Service Tasks; Status chỉ cho Open và Pending; WO sinh ra liên kết Issue ở cột Resolved | Đã chạy | Chạy |
| Thông báo của automation | Failure Notification Email: "Send an email whenever this automation fails." Run Summary Email: "Receive a summary email of successful automa | Chỉ xem | Chặn: Đọc câu chữ; không bật email |
| Automation đổi trạng thái xe | Mẫu: In Shop khi sự cố từ kiểm tra; Active khi sự cố Resolved; đổi trạng thái khi tạo lệnh; Active khi lệnh Completed và Vehicle Incomplete  | Đã chạy | Automation tự đổi trạng thái xe, lật thao tác tay |
| Sửa automation đang bật | Sửa mà chưa lưu: băng cảnh báo "You have unsaved changes on this enabled automation", nút Save thành menu Save Automation, Discard Unsaved C | Đã chạy | Chạy |
| Lịch sử phiên bản automation | Version History liệt kê v.2 Current Version và v.1, kèm Created At, Created By; mở một bản ra Step Summary gồm Trigger, Conditions, Actions. | Đã chạy | Chạy 1 lần sửa nội dung action |
| Make a Copy automation | Mở trình dựng `copy_from`, chưa lưu gì, tên thêm " (copy)", Disabled; rời trang không để lại bản rác. | Đã chạy | Chạy |
| Lượt automation thất bại | Run Result có băng đỏ nguyên văn lỗi, Status FAILURE, Records "No records changed"; danh sách đếm Failed; log từng bước state DNF, status FA | Một phần | Chạy một phần: Failure Notification Email không bật |

## Settings, quyền

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Thiết lập chung | Khách chọn tiền tệ, định dạng ngày, múi giờ, 12 hay 24 giờ, đơn vị số đo, nhiên liệu, hệ đo, gọi Vehicle hay Asset, thuế. Là mặc định cho xe | Chỉ xem | Chặn: Đọc thêm, không lưu |
| Luật bật tắt có giải thích | Mỗi luật có ô tick, câu mô tả tác động, phạm vi; loại trừ theo loại xe (Require a Meter Reading kèm Excluded Vehicle Types). Lượt 3 đọc đủ M | Chỉ xem | Chặn: Đọc đủ, không lưu |
| Danh mục theo khách | Trạng thái, loại, mã, lý do, đơn vị do khách sửa; có mục khoá của hệ thống, có bí danh, tắt được từng mục (Issue Priorities). Số mục ở Mục 1 | Chỉ xem | Chặn: Đọc thêm, không lưu |
| Tắt cả module | Ví dụ Enable Work Orders; tắt thì ẩn Work Orders, Parts. General Settings còn bật tắt Jobs, Motor Pool, Smart Uploads (Fuel Entry, Service E | Chỉ xem | Chặn: Không tắt module |
| Role | Bốn vai có sẵn: Fleet Manager, Operator, Technician, Viewer; 30 module, mỗi module mức đủ, một phần, không; thêm vai mới; khoá vai mặc định. | Chỉ xem | Chặn: Hiệu lực cần người dùng thứ hai |
| Record Set | Phạm vi dữ liệu theo Vehicles, Contacts, Part Locations, Inspection Forms; mẫu Assigned Only, Full, No Access, Group Only, View Only; quyền  | Chỉ xem | Chặn: Hiệu lực cần người dùng thứ hai |
| Điều kiện theo trường tuỳ chỉnh | Record Set lọc được theo trường tuỳ chỉnh dạng chọn, tick. | Chỉ xem | Chặn: Hiệu lực cần người dùng thứ hai |
| Giới hạn theo gói | Hiện đã dùng trên giới hạn: tài liệu, vai, xe, tự động hoá, bản ghi tự tạo (Fleetio: 250.0 GB, 30, 5, 75, 25). Hết hạn mức thì chặn tạo và k | Một phần | Đếm 1 of 75; chặn hạn mức chưa thử |
| Quyền con theo module | Vehicles có create, edit, view_all, view_details, view_financial_info, view_custom_fields, export_data, update_status, manage_vehicle_assign | Chỉ xem | Chặn: Hiệu lực cần người dùng thứ hai |
| Cảnh báo chi phí tại quyền | Ngay tại quyền Create của Vehicles: "Adding new Vehicles will result in additional charges to your account's subscription." | Chỉ xem | Chặn: Hiệu lực cần người dùng thứ hai |
| Điều kiện Record Set tự tạo | Vehicles có 8 điều kiện: All vehicles, Vehicles in this contact's group, Vehicles assigned to this contact, Specific vehicles, Vehicles in s | Chỉ xem | Chặn: Hiệu lực cần người dùng thứ hai |
| Chính sách bảo mật | Minimum Length, Expiration, yêu cầu ký tự, Maximum invalid login attempts, Lockout, Reset All Passwords; Session Timeout tách Fleetio Go và  | Chỉ xem | Chặn: Thêm Session Timeout |
| AI Service Advisor | Issue Prioritization, Issue Resolution, Fault Monitoring, Service Assessments, Service Writer, mỗi cái có Manage, có câu điều khoản. Câu mô  | Chỉ xem | Chặn: Đọc AI Advisor |
| Khung trạng thái theo khách | Work Order: Type cố định Incomplete, Completed; khách thêm tên. Purchase Order: 8 trạng thái cố định, không có Add. | Chỉ xem | Chặn: Đọc thêm, không lưu |
| Cài đặt bảo dưỡng | Maintenance Settings: Enable Work Orders, Next Work Order Number, Require a Meter Reading kèm Excluded Vehicle Types, Require Inspections, R | Chỉ xem | Chặn: Maintenance Settings đọc đủ |
| Quyền trên xe | Quyền con: create, edit, view_all, view_details, view_financial_info, view_custom_fields, export_data, update_status, manage_vehicle_assignm | Đã chạy | Chạy |
| Bắt buộc số đồng hồ theo loại xe | Maintenance Settings: Require a Meter Reading + Excluded Vehicle Types, "This requirement only applies to future Work Orders or Service Entr | Chỉ xem | Chặn: Maintenance Settings đọc đủ |

## Tính năng chung

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Danh sách chuẩn | Tab đếm số, lọc nhanh, Filters có nhóm điều kiện, sắp xếp, nhóm dòng, chọn cột, phân trang, chọn nhiều. Trên Issues: Group có None, Priority | Đã chạy | Tìm, nhóm, cột |
| Chế độ xem đã lưu | Add Tab, Save View, Save Changes; My Saved Views, Saved Views dùng chung. Có thay đổi thì nút thành Save Changes có chấm cam. "Fleetio Stand | Đã chạy | Lưu view Private |
| Xem nhanh bản ghi | Record peek mở ngay trên danh sách. Lượt 3: bấm dòng trên Issues sang thẳng trang chi tiết, không mở khung xem nhanh; chưa thử màn khác (OQ- | Chỉ xem | Chặn: Không thấy peek ở Issues |
| Theo dõi, bình luận | Watch; người tạo tự theo dõi; bình luận, nhắc tên; cột phải trên trang chi tiết. Automation bình luận với tác giả "Fleetio Automation". Unwa | Đã chạy | Comment, Watch; @ không khớp dấu, gạch nối |
| Thông báo | Hồ sơ thông báo gán cho người (gán bulk từ Contacts), nhóm xe theo dõi có cột Direct Watchers, Total Watchers, cài đặt cá nhân (FR-061); hộp | Một phần | Chặn: Tạo hồ sơ là đổi Settings |
| Tìm toàn cục | Bản trước ghi 15 loại bản ghi; lượt 3 đếm ô chọn loại có 16 mục (chưa tách mục "All"). Kết quả theo nhóm VEHICLES, CONTACTS, SERVICE ENTRIES | Đã chạy | Tìm theo nhóm, tách theo từ |
| Lịch sử bản ghi | View Record History; lịch sử từng trường. Có trên xe, automation, Issue. Cột Date, Changes By, Changes Made, lọc theo khoảng ngày. Comment,  | Đã chạy | Đọc lịch sử Issue, xe |
| Kho tài liệu | Danh sách file, thư mục, biết gắn bản ghi nào; tab All Documents và tab tên tài khoản; cột File Name, File Size, Location, Auto-Delete, Atta | Đã chạy | Tải tệp TEST, gắn xe |
| Liên hệ một bảng | Một bảng Contact, phân vai bằng tick Operator, Employee, Technician; User Access: Enable Access to Fleetio hoặc No Access (mặc định). Người  | Một phần | Chặn: Enable Access có thể gửi mời |
| Motor Pool | Đặt xe dùng chung: cột Motor Pool, Number, Operator, Vehicle Types, Vehicle, Pick Up, Drop Off, Status; Settings có Motor Pools, Reservation | Một phần | Tạo pool; đặt xe không có Operator |
| Cài đặt thông báo cá nhân | Email, Mobile App bật tắt chung; 18 nhóm sự kiện, mỗi sự kiện cột Email, Push; "You are watching 20 vehicles"; tự theo dõi xe mới, bản ghi m | Chỉ xem | Xem, không lưu |
| Gắn tài liệu vào xe | Select Vehicles mở "Attach Document to Vehicles": tìm, Attached Vehicles, All Vehicles, Vehicle Types, Groups; gắn xong nút thành "Attached" | Một phần | Chạy một phần: Gắn 1 xe |
| Mở truy cập từ liên hệ | Chọn Enable Access: "This Contact will be enabled as a User...", Login Information gồm Email, Delay email invitation, Message; Role * mặc đị | Chỉ xem | Xem, không lưu |
| Tạo Motor Pool | Form Add Motor Pool: Name *, Groups *, Vehicle Types *, Vehicle Statuses * (mặc định Active), "Automatically calculate charges", 'Require "R | Một phần | Chạy một phần: Tạo pool; Auto Approvals, Rates, Fees chỉ đọc |
| Đặt xe theo loại xe | Form Vehicle Reservation: Operator *, Motor Pool *, Reason for Trip, Pick Up *, Drop Off *. Chọn pool thì hiện Vehicle Types * chỉ gồm loại  | Một phần | Chạy một phần: Submit thiếu dữ liệu; chưa tạo được đặt xe |

## Tích hợp, API

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Webhook | Chọn một sự kiện mỗi webhook; hơn 50 sự kiện; ký xác thực; thất bại 3 lần liên tiếp thì tắt. Màn ghi "send a HTTP POST" dạng JSON. | Chỉ xem | Chặn: Đọc sâu, không tạo |
| API, SAML, MCP | API key, đăng nhập SAML (có Metadata), máy chủ MCP: "Each connection respects the user's role permissions." Module Fleetio MCP mức không có  | Chỉ xem | Chặn: Đọc sâu, không tạo |
| Sandbox, xuất dữ liệu | Môi trường thử: Sample Copy, Production Copy có hạn mức riêng. Export Account Data: 13 loại dữ liệu (Vehicles, Vehicle Assignments, Meter En | Chỉ xem | Chặn: Đọc sâu, không tạo |
| Kết nối ra ngoài | Integration Links (link sang hệ khác kèm biến; cột Label, Record, Status), External Connections (FTP, SFTP, Amazon S3 cho báo cáo định kỳ; c | Chỉ xem | Chặn: Đọc sâu, không tạo |
| API vị trí | `POST /vehicles/:id/location_entries` tạo mới, bản tương tự cho Equipment, khuyên Bulk API khi nhiều. | Tài liệu | Chặn: Không tạo key, không gọi thử |
| Danh mục tích hợp | Trang `integrations/my-integrations`: Data Connectors 6, Fuel Cards 9, Fuel Management 5, Key Management 1, Operations 1, Telematics 43, Tir | Chỉ xem | Xem |

## Ngoài phạm vi đợt này

| Chức năng | Mô tả | Mức | Đã đi tới đâu |
|---|---|---|---|
| Tools | Đã tắt theo yêu cầu user, còn tới 16/11; không dùng | Không mở | Đã tắt theo yêu cầu user, còn tới 16/11; không dùng |
| Advanced Analytics | Không mở trial theo chọn của user | Không mở | Không mở trial theo chọn của user |
| Custom Records, trường tuỳ chỉnh | Không mở theo chọn của user; chỉ có tài liệu hãng | Không mở | Không mở theo chọn của user; chỉ có tài liệu hãng |
| Kết nối thật GPS, ERP, thanh toán | Không kết nối; cần tài khoản ngoài | Không mở | Không kết nối; cần tài khoản ngoài |
