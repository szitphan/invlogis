---
type: research
feature: fleetio-vehicle
status: draft
status_changed: 2026-11-03
status_reason: "đã review upstream, không cần sửa"
updated: 2026-11-03
links:
  - docs/_research/fleetio/fleetio-vehicle.md
  - docs/_research/fleetio/run-notes/vehicle.md
  - docs/_research/fleetio/run-notes/platform.md
  - docs/_research/fleetio/fleetio-tires.md
  - docs/vehicle-management/brainstorms/vehicle-management.md
---

# Hồ sơ và vòng đời phương tiện — SRS phân tích ngược từ Fleetio

> Mô tả **Fleetio đang làm gì**, kèm đề xuất cho Invlogis ở cột riêng. Chưa phải yêu cầu đã chốt với Delta.

**Nhãn bằng chứng:** `Chạy` đã thao tác · `Xem` thấy trên giao diện, chưa bấm · `Docs` tài liệu công khai · `Suy` suy ra · `GĐ` giả định.

**Phép thử chính:** chạy ngày 02/11/2026 trên `TEST-XE-01`; chạy ngày 03/11/2026 trên `TEST-XE-LOP` (Semi Truck, đồng hồ đầu 5.000 km) và `TEST-MOOC-LOP` (Trailer); lượt 3 ngày 03/11/2026 chạy tiếp trên `TEST-XE-LOP`, `TEST-MOOC-LOP`, xe mới `TEST-DAUKEO-2` và đọc kết quả phiếu Fleetio Go có sẵn trên `TEST-XE-01`.

## 1. Scope

**Trong phạm vi:** Vehicle (form, trang xe, trạng thái, Archive, hạn mức), mooc dưới dạng Vehicle riêng và Linked Vehicles, Vehicle Assignment, Meter Entry, Expense Entry, Cost of Ownership, Warranty và Warranty Opportunities, Replacement Analysis, Recall và Motor Pool ở mức đọc.

**Lốp:** sơ đồ trục, lắp, đảo, tháo, đọc gai nằm ở [[docs/_research/fleetio/srs/fleetio-tires-spec.md|SRS Lốp]]; nhóm này chỉ giữ FR-fleetio-vehicle-017 trỏ sang.

**Ngoài phạm vi:** tổ hợp đầu kéo, mooc, container; Fleetio không có đối tượng này (`Chạy`), Invlogis giữ theo `transport-dispatch` và `vehicle-management`. Bán, thanh lý xe chỉ là trường dữ liệu (Out-of-Service Date, Out-of-Service Odometer) và trạng thái Sold, không thấy nút hay luồng thanh lý (`Xem`); nhập hai trường đó không đổi Status, không tạo dòng đồng hồ (`Chạy`).

## 2. Actors & Stakeholders

| Actor | Loại | Mục tiêu | Trong scope? | Tương đương Invlogis |
|---|---|---|---|---|
| Fleet Manager | Người | Quản lý hồ sơ, gán xe, bảo hành | Có | Quản lý phương tiện |
| Operator | Người | Được gán xe, báo số km | Có | Lái xe |
| Kế toán, Lãnh đạo | Người | Xem chi phí, phân tích thay xe | Có | Kế toán, Lãnh đạo |
| Kỹ thuật viên | Người | Thấy cơ hội bảo hành trên lệnh | Có | Kỹ thuật xưởng |
| Telematics, API | Ngoài | Đẩy số km. Lý do Out of Sequence đã thấy từ phiếu Fleetio Go (`Chạy`, một ca); nguồn telematics, API chưa thử | Có | EUP |
| Automation | Hệ thống | Đổi trạng thái xe theo mẫu | Có, chi tiết ở nhóm Nền tảng | — |

## 3. Functional Requirements (FR)

| ID | Title | Description | Priority | Tầng | Verify by | Mức | Source | Đề xuất Invlogis |
|---|---|---|---|---|---|---|---|---|
| FR-fleetio-vehicle-001 | Tạo xe | Form 6 phần: Details (Identification, Classification, Additional Details), Maintenance (Service Program hoặc None), Lifecycle, Financial, Specifications (Dimensions, Weight, Performance, Fuel Economy, Engine 15 trường, Transmission 4, Wheels & Tires 11, Fuel, Oil Capacity), Settings (Primary Meter, Current Reading, Average Usage per Day, Add Secondary Meter, Fuel Unit, Measurement Units). Nút Cancel, Add Multiple Vehicles, Save & Add Another, Save Vehicle. | P0 | [Lõi] | demo | `Chạy` | Tạo `TEST-XE-LOP`, `TEST-MOOC-LOP`; đọc đủ trường ở `TEST-NEN-01` | Lấy cách chia phần, rút trường theo xe Việt Nam |
| FR-fleetio-vehicle-002 | Tạo nhiều xe | Add Multiple Vehicles từ form hoặc menu Vehicle List, 2 bước. Bước 1 dán tối đa 200 xe, mỗi dòng {Vehicle Name}, {VIN}, {Group}; VIN, Group tuỳ chọn; Group chưa có thì tự tạo, kể cả cấp cha. Bước 2 chỉ hiện lại bảng, không kiểm trùng. Lưu chạy nền ("Processing", "Complete: Add Multiple Vehicles"); xe mới Active, tự giải mã VIN, mặc định Car nếu VIN không ra loại. Dòng lỗi chỉ báo qua email (E-fleetio-vehicle-025). Gói đầy thì mục trong menu "..." xám, có khoá, bấm không mở form (E-fleetio-vehicle-032); Import Vehicles, Import Meter Entries không khoá. | P1 | [Cấu hình] | demo | `Chạy` một phần lượt 3: 1 dòng lỗi, 1 dòng thành công; chưa dán nhiều dòng | `images/vehicle-add-multiple-step1.jpg`, `TEST-DAUKEO-2`; dán nhiều dòng, Group mới không thử vì vượt gói, tạo danh mục dùng chung | Lấy cho khởi tạo khách, báo lỗi ngay trên màn từng dòng |
| FR-fleetio-vehicle-003 | Trang xe trung tâm | Đầu trang: số km, trạng thái, nhóm, người lái; tab Overview cùng khoảng 19 lịch sử; cột phải bình luận, ảnh, tài liệu; khối Linked Assets, Cost of Ownership. | P0 | [Lõi] | demo | `Chạy` | Trang `TEST-XE-01`, `TEST-XE-LOP` | Lấy, rút gọn trên mobile |
| FR-fleetio-vehicle-004 | Tạo bản ghi từ xe | Nút Add: Draft Work Order, Assignment, Fuel, Charging, Expense, Service Entry, Issue, Inspection, Work Order, Warranty, Service Reminder, Renewal, Meter. Menu đổi theo xe: xe Gasoline ẩn Add Charging Entry, xe chưa có Fuel Type thì có; trạng thái xe không làm bớt mục nào (`Chạy` lượt 3). | P0 | [Lõi] | demo | `Chạy` | Đếm được 13 loại trên ảnh trang xe | Lấy |
| FR-fleetio-vehicle-005 | Overview có thể tuỳ biến | Khối Fields tìm được theo tên trường (gõ "tire" lọc còn nhóm Specifications, "4 results for "tire"", có "Clear search"), có Customize Layout; các khối Last Known Location, Open Issues, Service Reminders và số đếm. Ẩn hiện thẻ cá nhân ở FR-fleetio-vehicle-051; layout tài khoản ở FR-fleetio-vehicle-052. | P1 | [Cấu hình] | demo | `Chạy` một phần lượt 3: Tìm trường, ẩn hiện thẻ cá nhân; layout tài khoản chỉ đọc | Trang xe | Lấy khối cần xử lý |
| FR-fleetio-vehicle-006 | Lịch sử trường | Status, Group có nút xem lịch sử đổi; menu có View Record History. Hộp "Status Updates" mỗi lần một dòng: ai đổi, từ trạng thái nào sang trạng thái nào, ngày giờ, thời lượng. Record History ghi "Type changed from Car to Semi Truck", "Out Of Service Date changed from (empty) to …", "Out Of Service Meter changed from (empty) to 10.0", "Archived At changed from … to …", "Axle config created", "Vehicle created"; lọc theo khoảng ngày. KHÔNG ghi việc ngắt liên kết, KHÔNG ghi đổi đồng hồ. Lịch sử đổi nhóm chưa xem được. | P1 | [Lõi] | demo | `Chạy` lượt 3: Status Updates, Record History ghi từng thay đổi | Trang xe, More Actions, `images/vehicle-status-history.jpg` | Lấy, ghi thêm thao tác lên liên kết và đồng hồ |
| FR-fleetio-vehicle-007 | Giải mã số khung | Nút Decode cạnh VIN/SN điền thông số, gồm dung tích bình. VIN ngắn thì nút khoá, không giải thích (E-fleetio-vehicle-026). VIN 17 ký tự: "Decoding VIN...", rồi hộp "Add New Vehicle Data" với bảng Attribute, Current Data, Decoded Data, nhãn New hoặc Different. Dòng New tick sẵn, dòng Different KHÔNG tick. "Save Data to Vehicle" chỉ điền vào form, xe chưa đổi cho tới khi Save Vehicle. Add Multiple tự giải mã không qua hộp này: thấy Front, Rear Tire Type từ VIN, nhưng MSRP vẫn 0, khác bảng giải mã tay. | P2 | [Cấu hình] | demo | `Chạy` lượt 3: VIN ngắn khoá; VIN đúng ra bảng so sánh | Form xe, `images/vin-decode-review.jpg` | Kiểm với xe Việt Nam; lấy cách so sánh trước khi ghi đè |
| FR-fleetio-vehicle-008 | Liên kết xe | Linked Vehicles là trường chọn trong form sửa xe; kết quả hiện hai chiều ở khối "Linked Assets" › "Link Asset" › "VEHICLES" trên cả hai xe; gỡ, gắn lại từ một trong hai phía. Không có ngày, không có lịch sử ghép, không truyền số km, không gộp lốp. Một mooc nối được nhiều xe cùng lúc, không cảnh báo, không kiểm loại xe (nối được với Car); xe đã nối không còn trong ô chọn. Khối còn có mục TOOLS. Archive xe ngắt liên kết, kể cả khi Archive bị từ chối (E-fleetio-vehicle-022). | P1 | [Lõi] | test | `Chạy` | `run-notes/vehicle.md`, `run-notes/tires.md` | Không đủ thay ghép tách mooc |
| FR-fleetio-vehicle-009 | Gán xe | Assigned Vehicle, Operator, Start Date/Time ("Leave blank if assignment has always existed."), End Date/Time ("Can be past or future."), comment; chọn đủ xe và người thì hiện thêm Starting Odometer, Ending Odometer; hộp Edit gợi ý Starting Odometer theo đồng hồ hiện tại. Xe đang Out of Service, Inactive vẫn gán được, không cảnh báo. | P0 | [Lõi] | test | `Chạy` | Phân công 05/11 đến 07/11, 10/11 đến 12/11 | Lấy cho bàn giao, thu hồi |
| FR-fleetio-vehicle-010 | Chặn trùng gán | Không cho hai lần gán chồng thời gian trên **một xe**; không tự đóng phân công cũ. Không xét trùng theo người (BR-fleetio-vehicle-007). | P0 | [Lõi] | test | `Chạy` | E-fleetio-vehicle-001 | Lấy theo xe, thêm cảnh báo theo người |
| FR-fleetio-vehicle-011 | Chỉ Operator được gán | Ô chọn chỉ hiện liên hệ phân loại Operator ("Allow this Contact to be assigned to assets"); liên hệ khác bị chặn bằng câu dẫn trên trang liên hệ; có ngoại lệ từ workflow biểu mẫu. Gõ tên liên hệ chỉ phân loại Technician: không có trong kết quả, chỉ có dòng "Create "…"", không báo lý do (E-fleetio-vehicle-030). | P1 | [Lõi] | test | `Chạy` lượt 3: Liên hệ chỉ Technician không có trong ô chọn | `TEST-NEN-LH-01`; ngoại lệ là `Docs` | Lấy |
| FR-fleetio-vehicle-012 | Lịch gán | Mỗi xe một hàng, xem Day hoặc Week, thanh màu cam là tương lai, xanh là đang chạy, lịch tháng bên phải, gom theo xe hoặc người. | P1 | [Lõi] | demo | `Chạy` | Lịch tuần; gom theo người là `Xem` | Làm mẫu cho `transport-dispatch` |
| FR-fleetio-vehicle-013 | Sổ đồng hồ | Mỗi dòng có ngày, giá trị, loại Primary hoặc Secondary, Void, Source, Void Status, Auto-Void Reason; hiện số hiện tại và khoảng cách với hiện tại ("200 km ago"); lọc Void Status: All Voided, Manually Voided, Auto Voided, Not Voided. Đồng hồ phụ là chuỗi riêng trên cùng danh sách, Meter Type "Secondary", nhãn "Current hours". Chọn nhiều dòng có Actions: FR-fleetio-vehicle-047. | P0 | [Lõi] | test | `Chạy` | 7 dòng trên `TEST-XE-01`, 5 dòng trên `TEST-XE-LOP` | Lấy |
| FR-fleetio-vehicle-014 | Tự huỷ số sai | Số vượt mức tối đa một ngày: lưu nhưng tự Void, lý do Exceeds Max. Daily Usage, popup có Last Meter Entry, Daily Usage, Max Daily Usage, Exceeds By, nút "Unvoid this Entry". Biên Fleetio: đúng +4.828 km vẫn nhận, +4.829 km tự Void. Lý do Out of Sequence có thật: dòng 3.100 km từ phiếu Fleetio Go tự Void, popup "Auto-Voided Meter Entry" có This Entry, Conflicting Entry, Conflict Status. Nhập tay trên web không ra lý do này mà bị từ chối ở trường (FR-fleetio-vehicle-032). | P0 | [Lõi] [Cấu hình] | test | `Chạy` lượt 3: Biên 4.828 nhận, 4.829 Void; Out of Sequence có thật | Exceeds Max là `Chạy`; Out of Sequence là `Chạy` một ca từ Fleetio Go, telematics, API chưa thử; `images/meter-out-of-sequence-autovoid.jpg` | Lấy, ngưỡng là tham số mới, chưa có mã |
| FR-fleetio-vehicle-015 | Sửa xung đột | Dòng gây xung đột gắn cờ đỏ, Void Status "Conflict Source", popup "Conflicting Meter Entry" có số dòng ảnh hưởng và chênh lệch (ca Fleetio Go: Conflicts With 1 Entry, "601 kilometers over 1 day"). Unvoid dòng con thì cờ tự mất. Theo tài liệu hãng: Void dòng gốc rồi bỏ Void từng dòng, không tự động. | P1 | [Lõi] | test | `Chạy` lượt 3: Thêm hai popup xung đột từ ca Fleetio Go | Cờ và Unvoid là `Chạy`; Void dòng gốc là `Docs` | Lấy, nên tự bỏ Void, bắt buộc lý do |
| FR-fleetio-vehicle-016 | Đổi đồng hồ | Không có bước khai báo "thay đồng hồ", không lưu lý do. Cách đã chạy: Void hàng loạt toàn bộ số của xe (FR-fleetio-vehicle-047), xe về "0 km", nhập lại từ số nhỏ, lịch sử số cũ còn nguyên. Tài liệu hãng gọi Bulk Meter Management, kể cả số GPS (`Docs`); không thấy mục tên đó ở các menu đã mở, chưa đối chiếu có cùng tính năng không. | P1 | [Lõi] | test | `Chạy` một phần lượt 3: Void hàng loạt, nhập lại từ 100 km; chưa có GPS | `TEST-XE-LOP`, `images/meter-bulk-void-secondary.jpg` | Lấy cách giữ lịch sử; thêm bước khai báo thay đồng hồ, có lý do |
| FR-fleetio-vehicle-017 | Đọc lốp, quản lý lốp | Trục, lắp, đảo, tháo, đọc gai theo từng xe: xem [[docs/_research/fleetio/srs/fleetio-tires-spec.md|SRS Lốp]]. | P2 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` | `run-notes/vehicle.md`, `run-notes/tires.md` | Xem `fleetio-tires` |
| FR-fleetio-vehicle-018 | Chi phí khác | Vehicle, Expense Type (17 loại có sẵn), Vendor, Amount, Frequency: "Single Expense" hoặc "Recurring Expense" ("Repeats on a monthly or annual basis"), Notes; Recurring thêm Start Date, End Date, Frequency. Tab Past, Future. Tự sinh khoản vay, thuê mua nếu bật Auto Generate Loan / Lease Expenses. | P1 | [Cấu hình] | test | `Chạy` | Insurance định kỳ, Tolls đơn lẻ; tự sinh vay là `Xem` | Vẫn lấy `cost-catalog` làm gốc |
| FR-fleetio-vehicle-019 | Phân tích thay xe | Máy tính ước lượng **cấp tài khoản**: không có ô chọn xe, không đọc dữ liệu xe nào. Biểu đồ chi phí trên km theo tuổi xe từ giả định nhập tay: tuổi thọ, số km năm, tiêu hao, giá mua, thanh lý, phương pháp khấu hao, dịch vụ và nhiên liệu từng năm; chỉ ra Optimal Replacement, Estimated Replacement. | P2 | [Gói: Bảo dưỡng đội xe] | phân tích | `Chạy` | Chỉ đọc, không đổi số | Để sau; nếu làm thì đọc số thật của từng xe |
| FR-fleetio-vehicle-020 | Trạng thái xe | Status bắt buộc, mặc định Active. Danh mục 5 trạng thái có đếm xe, Add Vehicle Status. Đổi tự do qua form hoặc automation, không có luật chuyển, không hỏi lý do, toast "Vehicle was successfully updated". Trạng thái không ràng buộc nghiệp vụ nào: xe Out of Service, Inactive vẫn gán tài xế; xe Sold vẫn mở Lệnh, nhập đồng hồ. In Shop không tự sinh Lệnh; mở, đóng Lệnh không đổi trạng thái khi không có automation. Báo cáo Status Changes, Status Summary. | P0 | [Lõi] [Cấu hình] | test | `Chạy` lượt 3: Đổi đủ 5 trạng thái, không ràng buộc | Settings › Vehicle Statuses; đổi thật trên `TEST-XE-LOP`, `images/vehicle-status-history.jpg` | Khung trạng thái lõi, nhãn cấu hình; cân nhắc luật chặn theo trạng thái (OQ-17) |
| FR-fleetio-vehicle-021 | Archive xe | Nút Archive trong More Actions, hộp "Confirm Vehicle Archive", nút "Archive Vehicle", đưa xe sang tab Archived; quyền `vehicles_archive_delete`. Archive không đổi trường Status: xe Archived vẫn hiện Active hoặc Inactive. Chặn khi còn Lệnh chưa xong; câu trong hộp nêu thêm Motor Pool đang đặt. Xe Archived vẫn xem được đồng hồ, cấu hình trục, Edit trục khoá. Hiệu ứng ở FR-fleetio-vehicle-049, Restore ở FR-fleetio-vehicle-048. | P1 | [Lõi] | test | `Chạy` một phần lượt 3: Restore, Archive, chặn lệnh mở; Motor Pool chỉ đọc câu chữ | `TEST-XE-LOP`, `images/vehicle-archive-confirm.jpg`; Motor Pool chưa tạo đặt xe | Lấy, nêu rõ dữ liệu liên quan còn hay không |
| FR-fleetio-vehicle-022 | More Actions trên xe | Edit Vehicle Settings (mở thẳng phần Settings của form), Manage Inspection Forms (thẻ từng biểu mẫu nhãn "Disabled", menu "…", "View Submissions"), Manage Service Programs, Manage Integration Links, Attach Shared Document, Recalculate Fuel Entries, View Record History, Archive. Recalculate Fuel Entries lượt 3 không thấy trên 2 xe TEST đã mở, cả 2 không có Fuel Entry; lượt 4 thấy đủ 8 mục trên `TEST-DAUKEO-2`, điều kiện hiện mục này chưa rõ (OQ-20). Service Programs ở FR-fleetio-vehicle-053, Shared Document ở FR-fleetio-vehicle-054. | P1 | [Lõi] | demo | `Chạy` một phần lượt 4: Mở thêm 2 mục; Integration Links bị chặn | `images/vehicle-more-actions.jpg`; lượt 4 đã mở Service Programs, Shared Document; Integration Links không mở vì là tích hợp | Lấy nhóm thao tác cấp xe |
| FR-fleetio-vehicle-023 | Hạn mức xe theo gói | Danh sách hiện "5 of 5", nút Add Vehicle có khoá; Save bị chặn. Account Usage đếm Vehicles. Xe Sample không tính. Quyền Create cảnh báo "Adding new Vehicles will result in additional charges to your account's subscription." | P1 | [Cấu hình] | test | `Chạy` | E-fleetio-vehicle-009 | Hạn mức là tham số mới, chưa có mã |
| FR-fleetio-vehicle-024 | Loại xe | Type bắt buộc, mặc định Car; Settings › Vehicle Types 25 loại. Đổi loại tự do, không hỏi, dòng phụ đầu trang đổi theo, Status giữ nguyên, có dòng Record History. Loại xe được dùng ở Excluded Vehicle Types của Require a Meter Reading. | P1 | [Cấu hình] | demo | `Chạy` lượt 3: Đổi Car sang Semi Truck tự do | Settings | Danh mục theo khách |
| FR-fleetio-vehicle-025 | Nhóm xe | Group dạng cây nhiều cấp, ô chọn hiện cha / con, tìm tên chưa có thì có dòng "Create "…""; "Require Group" bị khoá khi còn tài sản, liên hệ chưa có nhóm; Export Data. Xe thật không dùng được nhóm Sample (E-fleetio-vehicle-028). Gán nhóm thật, lịch sử đổi nhóm chưa xem được. | P1 | [Lõi] [Cấu hình] | demo | `Chạy` một phần lượt 3: Nhóm Sample bị từ chối; không tạo nhóm mới | Settings › Groups & Subgroups, `TEST-DAUKEO-2` | Khớp Chi nhánh, xem nhóm Nền tảng |
| FR-fleetio-vehicle-026 | Mooc là một Vehicle | Mooc tạo với Type Trailer, có đồng hồ riêng (lưu trống thành "0 km"), sơ đồ lốp riêng, lịch sử lốp riêng; không có tổ hợp đầu kéo và mooc. Đầu kéo tăng km thì mooc giữ nguyên. | P1 | [Lõi] | test | `Chạy` | `TEST-MOOC-LOP` | Không đủ cho nghiệp vụ ghép tách; giữ mô hình tổ hợp |
| FR-fleetio-vehicle-027 | Tạo gán từ ô lịch | Bấm ô trống mở "Add Vehicle Assignment For {xe}", xe khoá, ngày điền sẵn theo ô. | P1 | [Lõi] | demo | `Chạy` | Lịch tuần | Lấy cho điều vận |
| FR-fleetio-vehicle-028 | Sửa, thay người trên phân công | Edit đổi Operator đè lên phân công, xe khoá khi sửa. Không có hành động "thay người", trang chi tiết không còn dấu vết người cũ. | P0 | [Lõi] | test | `Chạy` | Phân công #12480917 | Không nên học; cần hành động bàn giao có lịch sử |
| FR-fleetio-vehicle-029 | Chi tiết phân công | Trang "Vehicle Assignment #…": Operator, nhãn Future, Start, End, Duration, Start Meter, End Meter, Distance. Menu thanh lịch: View, Edit, Delete. | P1 | [Lõi] | demo | `Chạy` | Delete là `Xem` | Lấy, thêm số km bàn giao bắt buộc |
| FR-fleetio-vehicle-030 | Void tay khi nhập | Hộp nhập có ô Void; dòng thành "Manually Voided", không bao giờ là số hiện tại. | P0 | [Lõi] | test | `Chạy` | 5.800 ngày 01/11 | Lấy, bắt buộc lý do |
| FR-fleetio-vehicle-031 | Unvoid | Hộp "This operation will attempt to unvoid the selected Meter Entry." rồi Confirm. Không hỏi lý do, không kiểm lại Max Daily Usage. | P1 | [Lõi] | test | `Chạy` | Dòng 20.000 | Lấy, thêm lý do và kiểm lại ngưỡng |
| FR-fleetio-vehicle-032 | Chặn lệch thứ tự theo ngày | Số đồng hồ phải nằm giữa số ngày trước và số ngày sau; sai thì từ chối ở trường, trừ khi tick Void. Cùng luật cho Fuel Entry. | P0 | [Lõi] | test | `Chạy` | E-fleetio-vehicle-004, 005, 008 | Lấy |
| FR-fleetio-vehicle-033 | Sinh chi phí định kỳ | Lưu thì xử lý nền ("Processing: Recurring expense save", "Complete: Recurring expense save"), sinh sẵn từng dòng theo kỳ trong tab Future. | P1 | [Cấu hình] | test | `Chạy` | 3 dòng Insurance | Lấy, báo rõ khi xong không cần tải lại |
| FR-fleetio-vehicle-034 | Cost of Ownership | Khối trên trang xe: Total Costs, Cost Per Meter, Fuel & Energy Costs, Service Costs, Other Costs; mốc This Month, Last Month, This Year, Last 12 Months, Last Year, All Time. Dòng Future chưa tính. | P0 | [Lõi] | test | `Chạy` | `images/vehicle-cost-of-ownership.jpg` | Lấy, chặn số km sai làm sai chi phí/km |
| FR-fleetio-vehicle-035 | Tạo bảo hành nhiều xe | Form "New Warranties" 2 bước: Vehicles (nhiều xe, mỗi xe Start Date, Start Meter riêng) rồi Coverage Type: Standard Warranty, Standard templates, Extended Warranty. Trường: Warranty Name, Description, Manufacturer, Warranty Vendor, Contract ID, Vendor Link, Coverage Duration, Coverage Distance hoặc Unlimited. | P1 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` | "TEST Bao hanh dong co" trên `TEST-XE-01` | Lấy |
| FR-fleetio-vehicle-036 | Tự tính hạn bảo hành | End Date = Start Date + Coverage Duration; End Meter = Start Meter + Coverage Distance; Status "Active". Danh sách có số active, expiring soon, total. | P1 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` | Start 1 km, Coverage 50,000 km, End 50,001 km | Lấy |
| FR-fleetio-vehicle-037 | Gắn mã bảo dưỡng vào bảo hành | Maintenance Categorization nhập mã hệ thống (VMRS), có Bulk Mode, Column Mode. | P1 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` | Nhập 013 hiện "1 - Chassis" › "013 - Brakes" | Lấy nguyên tắc, danh mục mã theo khách |
| FR-fleetio-vehicle-038 | Cơ hội bảo hành trên lệnh | Khối "Warranty Opportunities" luôn hiện trên lệnh; Service Task trùng mã với coverage thì hiện "View Active Coverage" kèm Complaint, Cause, Correction. Khớp theo mã Service Task, không theo phụ tùng. | P1 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` | Lệnh #100 trước và sau "Brake Inspection"; nút claim chưa thử | Lấy, đáng học nhất nhóm này |
| FR-fleetio-vehicle-039 | Mẫu bảo hành | Coverage Template "contain a collection of coverages based on manufacturer guidelines"; Settings › Warranty Templates rỗng. Xe không có Make, Model thì ô báo "No options"; quan hệ nhân quả chưa kiểm chứng. | P2 | [Cấu hình] | demo | `Xem` | `TEST-XE-01` | Để sau |
| FR-fleetio-vehicle-040 | Công thức thay xe | Năm 1 tính khớp: nhiên liệu = giá lít / tiêu hao đổi ra km/lít; bảo dưỡng = chi phí năm / km năm; khấu hao Double Declining = giá mua × 2 / số năm / km năm. Phương pháp khác: Sum of Years. | P2 | [Gói: Bảo dưỡng đội xe] | phân tích | `Chạy`, `Suy` | Đối chiếu dữ liệu biểu đồ; các năm sau chưa kiểm | Để sau |
| FR-fleetio-vehicle-041 | Recall | Danh sách tab All, Needs Action, Open, Resolved, Acknowledged; cột Issued At, Status, Issue, Manufacturer Campaign Number, NHTSA Campaign Number; khung Learn ghi nhập tự động từ NHTSA theo năm, hãng, đời. | P2 | [Gói: Bảo dưỡng đội xe] | demo | `Xem` | 261 dòng Sample, không đổi trạng thái | Nguồn NHTSA không áp được cho xe Việt Nam (`Suy`) |
| FR-fleetio-vehicle-042 | Motor Pool | `motor_pool_reservations` rỗng, Add Vehicle Reservation; cột Motor Pool, Number, Operator, Vehicle Types, Vehicle, Pick Up, Drop Off, Status; quyền check_out, return, cancel. Phải tạo Motor Pool trong Settings trước. | P2 | [Gói: Bảo dưỡng đội xe] | demo | `Xem` | Không chạy: cấm đổi Settings, không có xe của nhóm | Để sau |
| FR-fleetio-vehicle-043 | Quyền trên xe | Quyền con: create, edit, view_all, view_details, view_financial_info, view_custom_fields, export_data, update_status, manage_vehicle_assignment, archive_delete, view_documents, manage_documents, manage_photos. Record Set Vehicles: Assigned Vehicles Only, Full Access, No Access, User's Group Only, View Only. | P0 | [Lõi] | kiểm tra | `Chạy` | Chỉ đọc màn Role, xem chi tiết ở nhóm Nền tảng | Lấy cách tách quyền đổi trạng thái, xem tài chính |
| FR-fleetio-vehicle-044 | Đồng hồ phụ | Add Secondary Meter trong Settings của form xe ("Track an additional meter, such as a concrete mixer, street sweeper, cleaning equipment, etc."), mặc định Hours, có Current Reading; Primary Meter chỉ Miles, Kilometers, Hours, không bỏ được. Bật xong đầu trang hiện 2 số, Overview thêm "Secondary Meter"; Add Meter Entry có 2 ô, mỗi ô có Void, "Last updated" riêng; bỏ trống Primary vẫn lưu được. Bật trên xe đang có số: số phụ bắt đầu "0 hr", đồng hồ chính không đổi; nhập từ phiếu kiểm ở `run-notes/reminders-inspection.md`. | P1 | [Cấu hình] | demo | `Chạy` lượt 3: Thêm đồng hồ phụ, nhập riêng, chuỗi riêng | Form xe, `TEST-XE-LOP`, `images/meter-bulk-void-secondary.jpg` | Hợp máy phát điện, xe nâng; mooc cần chế độ không đồng hồ |
| FR-fleetio-vehicle-045 | Automation đổi trạng thái xe | Mẫu: In Shop khi sự cố từ kiểm tra; Active khi sự cố Resolved; đổi trạng thái khi tạo lệnh; Active khi lệnh Completed và Vehicle Incomplete Work Orders Count < 1. Đã chạy automation tự tạo trên `TEST-DAUKEO-2`: sửa trường bất kỳ cũng kích hoạt; Status Updates ghi "Fleetio Automation updated status from Active to Inactive"; người đổi ngược lưu được, khoảng 1 giây sau bị đổi lại, màn hình không báo. | P1 | [Cấu hình] | test | `Chạy` lượt 3: Automation tự đổi trạng thái xe, lật thao tác tay | Mẫu là `Xem`; lượt chạy ở `run-notes/platform.md`, chi tiết ở nhóm Nền tảng | Lấy dạng công tắc theo khách; báo khi luật ghi đè thao tác tay |
| FR-fleetio-vehicle-046 | Bắt buộc số đồng hồ theo loại xe | Maintenance Settings: Require a Meter Reading + Excluded Vehicle Types, "This requirement only applies to future Work Orders or Service Entries." | P1 | [Cấu hình] | demo | `Xem` | Settings, chỉ đọc | Mẫu cho loại xe không đồng hồ như mooc |
| FR-fleetio-vehicle-047 | Void, Unvoid, Delete hàng loạt | Meter History tick nhiều dòng, mở Actions: Void, Unvoid, Delete. Chọn lẫn dòng đã Void và chưa Void thì Void, Unvoid đều khoá. Hộp "Void Meter Entries" đòi gõ VOID in hoa, Confirm khoá tới khi gõ đúng; toast "Successfully voided Meter Entries". | P1 | [Lõi] | test | `Chạy` phần Void; Unvoid, Delete hàng loạt `Xem` | 5 dòng trên `TEST-XE-LOP`, `images/meter-bulk-void-secondary.jpg` | Lấy cách gõ xác nhận, thêm lý do |
| FR-fleetio-vehicle-048 | Restore xe | Nút Restore trên xe Archived, bấm là chạy, không hỏi: "Record successfully restored!". Giữ trạng thái, đồng hồ, cấu hình trục; KHÔNG trả lại liên kết, phân công đã mất. Gói đầy thì nút khoá, không giải thích (E-fleetio-vehicle-023). | P1 | [Lõi] | test | `Chạy` | `TEST-XE-LOP` | Lấy, báo trước phần không trả lại được |
| FR-fleetio-vehicle-049 | Hiệu ứng của Archive | Archive thành công: liên kết với xe, công cụ mất ở cả hai phía; phân công đang chạy bị đóng ngay; phân công tương lai bị xoá hẳn; xe rời lịch phân công; lịch sử liên hệ giữ dòng đã đóng, nhãn "Archived". Hộp xác nhận báo trước đủ các hiệu ứng này. Toast nói bản ghi liên quan cập nhật ở nền (chữ nhỏ, chưa đọc được nguyên văn). | P1 | [Lõi] | test | `Chạy` | `TEST-XE-LOP`, `TEST-LAI-XE-02` | Lấy cách báo trước; thao tác phải trọn vẹn hoặc không có gì, xem E-fleetio-vehicle-022 |
| FR-fleetio-vehicle-050 | Tên xe, VIN không trùng | Form đơn báo Vehicle Name và VIN "has already been taken", "Vehicle could not be created". Trùng VIN xét cả xe Sample. Tên của xe đã Archive không báo trùng. | P1 | [Lõi] | test | `Chạy` một phần: tên xe Archived chỉ thấy không báo, chưa lưu vì VIN vẫn trùng | Form xe, `run-notes/vehicle.md` | Lấy; biển số, số khung Việt Nam cần xét riêng |
| FR-fleetio-vehicle-051 | Ẩn hiện thẻ cá nhân | Personalize › Manage Overview Layout: Available Cards 15, lọc thẻ, Visible Cards chia Left Column, Right Column, Restore defaults, Apply Changes. Bỏ tick thẻ thì thẻ mất ở trang xe, Restore defaults thì quay lại; câu dẫn nói kéo thả để đổi thứ tự. Personalize còn Manage Tab Menu. | P2 | [Cấu hình] | demo | `Chạy` phần ẩn hiện, Restore; kéo đổi thứ tự, Manage Tab Menu chưa thử | `images/vehicle-manage-overview-layout.jpg` | Lấy cho trang xe nhiều vai trò |
| FR-fleetio-vehicle-052 | Layout form theo tài khoản | Customize Layout đưa vào Settings › Standard Records › Vehicle › Layout: "System Default", 4 Sections, 104 Fields, All (25) loại xe, nút Add Layout. | P2 | [Cấu hình] | demo | `Xem` | Chỉ đọc; Add Layout là cài đặt cấp tài khoản, không thử | Cân nhắc layout theo loại xe |
| FR-fleetio-vehicle-053 | Bộ lịch bảo dưỡng trên xe | More Actions › Manage Service Programs đi tới `vehicles/{id}/service_programs`. Xe chưa có bộ lịch: trang rỗng dạng quảng bá "Efficiently schedule and manage service needs for multiple vehicles", 4 gạch đầu dòng, nút "Create Service Program". Tab xe KHÔNG có nút gán bộ lịch sẵn có. | P2 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` phần mở, nút Create chưa bấm | `TEST-DAUKEO-2`, `images/vehicle-service-programs-empty.jpg` | Cho gán bộ lịch có sẵn ngay trên xe |
| FR-fleetio-vehicle-054 | Đính tài liệu dùng chung | More Actions › Attach Shared Document, ô "Select Document" chỉ liệt kê tài liệu dùng chung (tên, loại, thời điểm sửa), nút khoá tới khi chọn; toast "Successfully attached shared document to vehicle." Panel Documents hiện thẻ tệp nhãn "Shared", ô kéo thả riêng cho tệp của xe. | P2 | [Lõi] | test | `Chạy` | `TEST-DAUKEO-2`, `images/vehicle-attach-shared-document.jpg` | Lấy cho giấy tờ dùng chung nhiều xe |

## 4. Non-Functional Requirements (NFR)

| ID | Category | Requirement | Priority | Acceptance |
|---|---|---|---|---|
| NFR-fleetio-vehicle-001 | đơn vị | Đơn vị số km, nhiên liệu chọn theo xe và tài khoản. | P0 | `Chạy` km, lít; Fleetio vẫn hiện mpg ở Replacement Analysis, "mi" ở Odometer của phần Financial nên chưa đạt |
| NFR-fleetio-vehicle-002 | truy vết | Mỗi số km truy được nguồn. | P0 | `Chạy` cột Source; Unvoid và đổi người trên phân công thì không có lý do, người cũ không còn trên trang nên chưa đạt phần lịch sử |
| NFR-fleetio-vehicle-003 | hiệu năng | Trang xe trên điện thoại ở bãi: TBD — đội sản phẩm — khi chi tiết hoá. | P1 | TBD |
| NFR-fleetio-vehicle-004 | múi giờ | Giờ phân công lưu và hiện theo một múi giờ rõ ràng. | P1 | `Chạy`: trường ngày gửi đi theo múi giờ thiết bị trong khi tài khoản đặt múi giờ khác, nên chưa đạt |
| NFR-fleetio-vehicle-005 | phản hồi nền | Việc xử lý nền phải báo xong mà không cần tải lại. | P2 | `Chạy`: "You may have to refresh your browser to see the changes." nên chưa đạt |

## 5. Business Rules

| ID | Rule | Tầng | Trigger | Implements FR | Mức | Source |
|---|---|---|---|---|---|---|
| BR-fleetio-vehicle-001 | Bắt buộc tên, loại, trạng thái, sở hữu, đồng hồ chính, đơn vị nhiên liệu, đơn vị đo. | [Lõi] | Lưu xe | FR-fleetio-vehicle-001 | `Chạy` | Form đánh dấu sao; Save rỗng báo "can't be blank" |
| BR-fleetio-vehicle-002 | Thời gian gán không chồng nhau trên một xe. | [Lõi] | Lưu gán | FR-fleetio-vehicle-010 | `Chạy` | Start 04/11 không End đè lên 05/11 |
| BR-fleetio-vehicle-003 | Ô số km đầu, cuối hiện khi đã chọn đủ xe và người. Lượt 3 thấy thêm: Starting Odometer xám khi Start bằng thời điểm hiện tại lúc chưa chọn đủ, mở khi chọn ngày, có lần tự điền số hiện tại; quy luật chưa tách rõ (OQ-12). | [Lõi] | Nhập form | FR-fleetio-vehicle-009 | `Chạy` | Sửa theo chạy 03/11 |
| BR-fleetio-vehicle-004 | Số hiện tại là số lớn nhất không bị Void. | [Lõi] | Lưu số km | FR-fleetio-vehicle-013 | `Chạy` | 5.300 sau 5.500 giữ 5.500; Void không tính; Unvoid 20.000 thành hiện tại |
| BR-fleetio-vehicle-005 | Số làm mức dùng một ngày vượt tối đa thì lưu và tự Void; đúng bằng mức thì vẫn nhận. Fleetio: 4.828 km một ngày; theo tài liệu hãng còn 3.000 dặm, 24 giờ. Invlogis: tham số mới, chưa có mã. | [Lõi] [Cấu hình] | Lưu số km | FR-fleetio-vehicle-014 | `Chạy`, `Docs` | Nhập 20.000 khi đang 5.500; từ 100 nhập 4.928 (+4.828) nhận, 9.757 (+4.829) tự Void. Số 4.828 là `Chạy`; dặm, giờ là `Docs` |
| BR-fleetio-vehicle-006 | Giá trị cao có cảnh báo, bỏ qua được; quá cao phải sửa hoặc Void. | [Lõi] | Nhập trên app | FR-fleetio-vehicle-014 | `Docs` | Chưa có số; trên web chỉ thấy tự Void |
| BR-fleetio-vehicle-007 | Trùng gán chỉ xét theo xe. Một người được giữ nhiều xe cùng lúc, kể cả đang có phân công "No end date". | [Lõi] | Lưu gán | FR-fleetio-vehicle-010 | `Chạy` | `TEST-LAI-XE` giữ `TEST-XE-01` và `TEST-XE-LOP` |
| BR-fleetio-vehicle-008 | Gán mới chồng phân công cũ thì từ chối, không tự đóng phân công cũ. | [Lõi] | Lưu gán | FR-fleetio-vehicle-010 | `Chạy` | E-fleetio-vehicle-001 |
| BR-fleetio-vehicle-009 | Khi sửa phân công, xe khoá, Operator đổi được; bản ghi giữ nguyên mã. | [Lõi] | Sửa gán | FR-fleetio-vehicle-028 | `Chạy` | #12480917 |
| BR-fleetio-vehicle-010 | Số đồng hồ ngày cũ phải nhỏ hơn số ngày sau; số ngày mới phải lớn hơn số ngày trước; sai thì từ chối trừ khi tick Void. Với nhập tay trên web, lệch thứ tự theo ngày không tự Void; phiếu từ Fleetio Go xem BR-fleetio-vehicle-024. Cùng luật áp cho Start Odometer khi đóng Lệnh (E-fleetio-vehicle-029). | [Lõi] | Lưu số km, phiếu dầu | FR-fleetio-vehicle-032 | `Chạy` | E-fleetio-vehicle-004, 005, 008 |
| BR-fleetio-vehicle-011 | Cùng ngày, số nhỏ hơn được lưu, không Void, không báo, không đổi số hiện tại. | [Lõi] | Lưu số km | FR-fleetio-vehicle-013 | `Chạy` | 5.300 sau 5.500; `TEST-XE-01` 900 sau 1.010; cùng hành vi ở Service Entry, Fuel Entry theo nhóm Sửa chữa, Kho |
| BR-fleetio-vehicle-012 | Dòng Void không bao giờ là số hiện tại, không kích hoạt nhắc bảo dưỡng hay thứ gì dựa trên số hiện tại. | [Lõi] | Tính số hiện tại | FR-fleetio-vehicle-030 | `Chạy` | Tooltip nguyên văn; 5.800 Manually Voided không đổi đồng hồ |
| BR-fleetio-vehicle-013 | Dòng làm dòng sau bị tự Void được gắn Conflict Source; hết xung đột thì cờ tự mất. | [Lõi] | Tự Void, Unvoid | FR-fleetio-vehicle-015 | `Chạy` | Dòng 5.500 |
| BR-fleetio-vehicle-014 | Unvoid không hỏi lý do, không kiểm lại mức tối đa; dòng được Unvoid thành số hiện tại ngay. | [Lõi] | Unvoid | FR-fleetio-vehicle-031 | `Chạy` | 5.500 lên 20.000 |
| BR-fleetio-vehicle-015 | Chi phí định kỳ sinh sẵn theo kỳ từ Start đến End. Cost of Ownership chỉ tính dòng đã đến ngày. | [Cấu hình] | Lưu chi phí | FR-fleetio-vehicle-033 | `Chạy` | Dòng 03/11 tính; 03/12, 03/01 chưa tính |
| BR-fleetio-vehicle-016 | Cost Per Meter = tổng chi phí chia km đã chạy trong kỳ, nên số đồng hồ sai làm sai chi phí/km. | [Lõi] | Xem Cost of Ownership | FR-fleetio-vehicle-034 | `Chạy`, `Suy` | 3.500.000 / 15.000 = 233 ₫/km; hệ quả là `Suy` |
| BR-fleetio-vehicle-017 | End Date = Start Date + Coverage Duration; End Meter = Start Meter + Coverage Distance. | [Lõi] | Lưu bảo hành | FR-fleetio-vehicle-036 | `Chạy` | Kiểm chứng trên `TEST-XE-01` |
| BR-fleetio-vehicle-018 | Cơ hội bảo hành xuất hiện khi Service Task trên lệnh có cùng mã bảo dưỡng với coverage còn hiệu lực. Phụ tùng đứng riêng không gợi ý. | [Gói: Bảo dưỡng đội xe] | Lưu lệnh | FR-fleetio-vehicle-038 | `Chạy` | Lệnh #100 |
| BR-fleetio-vehicle-019 | Liên kết xe không truyền số km, không gộp sơ đồ lốp; gỡ liên kết không đổi đồng hồ, lốp. | [Lõi] | Sửa xe | FR-fleetio-vehicle-008 | `Chạy` | `run-notes/vehicle.md`, `run-notes/tires.md` |
| BR-fleetio-vehicle-020 | Đổi trạng thái xe không có luật chuyển, không hỏi lý do, không chặn thao tác nào; mở, đóng lệnh không tự đổi trạng thái nếu không có automation; In Shop không tự sinh lệnh. | [Lõi] | Sửa xe | FR-fleetio-vehicle-020 | `Chạy` | Lượt 3: Active, Out of Service, Sold, In Shop, Sold, Inactive; xe Sold giữ Sold khi mở, đóng Lệnh #108, #109 |
| BR-fleetio-vehicle-021 | Hạn mức xe chỉ đếm xe thật, xe Sample không tính. Hết hạn mức thì chặn cả khi dữ liệu hợp lệ. | [Cấu hình] | Lưu xe | FR-fleetio-vehicle-023 | `Chạy` | Fleetio: gói dùng thử 5 xe. Invlogis: tham số mới, chưa có mã |
| BR-fleetio-vehicle-022 | Chỉ liên hệ phân loại Operator mới gán được xe. | [Lõi] | Gán xe | FR-fleetio-vehicle-011 | `Chạy` | Câu dẫn trên trang liên hệ |
| BR-fleetio-vehicle-023 | Phân tích thay xe không đọc dữ liệu xe, tham số Lifecycle trên từng xe không ảnh hưởng theo những gì thấy. | [Gói: Bảo dưỡng đội xe] | Xem trang | FR-fleetio-vehicle-019 | `Chạy` | `TEST-XE-LOP` có chi phí nhưng trang không đổi |
| BR-fleetio-vehicle-024 | Số lệch thứ tự xử lý khác nhau theo nguồn: nhập tay trên web bị từ chối ở trường, phiếu Fleetio Go được lưu rồi tự Void với lý do Out of Sequence; số đã Void không làm số hiện tại; dòng còn lại gắn Conflict Source. | [Lõi] | Lưu số km | FR-fleetio-vehicle-014, FR-fleetio-vehicle-032 | `Chạy` một ca | Dòng 3.100 km, xe giữ 2.999 km. Telematics, API chưa thử (OQ-8) |
| BR-fleetio-vehicle-025 | Void toàn bộ số thì xe hiện "0 km", hộp nhập "Last updated: No meter history", số kế tiếp nhận bất kỳ, không so với số cũ đã Void. | [Lõi] | Void, lưu số km | FR-fleetio-vehicle-016 | `Chạy` | Nhập 100 km ngay sau Void 5 dòng |
| BR-fleetio-vehicle-026 | Void hàng loạt chỉ mở khi mọi dòng chọn đều chưa Void, phải gõ đúng VOID. Dòng từng Auto-Voided đã Unvoid, Void lại thì về "Auto-Voided" với lý do cũ, không thành Manually Voided. | [Lõi] | Void hàng loạt | FR-fleetio-vehicle-047 | `Chạy` | Dòng 20.000 về "Exceeds Max. Daily Usage"; 4 dòng còn lại Manually Voided |
| BR-fleetio-vehicle-027 | Đồng hồ phụ là chuỗi riêng: số hiện tại, Void, "Last updated" tách khỏi đồng hồ chính; một phiếu chỉ có số phụ vẫn lưu được. | [Cấu hình] | Lưu số km | FR-fleetio-vehicle-044 | `Chạy` | 50, 60 hr trên `TEST-XE-LOP`, đồng hồ chính giữ 4.928 |
| BR-fleetio-vehicle-028 | Archive không đổi trường Status; Restore giữ nguyên trạng thái, đồng hồ, cấu hình trục. | [Lõi] | Archive, Restore | FR-fleetio-vehicle-021, FR-fleetio-vehicle-048 | `Chạy` | Xe Archived hiện Active hoặc Inactive |
| BR-fleetio-vehicle-029 | Archive thành công: ngắt mọi liên kết ở cả hai phía, đóng phân công đang chạy ngay lúc đó, xoá hẳn phân công tương lai. Restore không trả lại các thứ này. | [Lõi] | Archive, Restore | FR-fleetio-vehicle-049 | `Chạy` | Kết thúc 10/11 đổi thành lúc Archive, Duration 1m; phân công 20/11 không còn dòng nào |
| BR-fleetio-vehicle-030 | Không Archive được khi xe còn Lệnh chưa xong; câu trong hộp nêu thêm Motor Pool đang đặt. | [Lõi] | Archive | FR-fleetio-vehicle-021 | `Chạy` phần Lệnh, `Xem` phần Motor Pool | Thử 2 lần có đối chứng; đóng Lệnh xong thì Archive được |
| BR-fleetio-vehicle-031 | Restore khoá khi gói đã đầy, xe Archived không chiếm chỗ trong hạn mức. | [Cấu hình] | Restore | FR-fleetio-vehicle-048, FR-fleetio-vehicle-023 | `Chạy`, phần không chiếm chỗ `Suy` | Tạo được xe thứ 5 khi `TEST-XE-LOP` đang Archived; sau đó nút khoá, bấm không có gì |
| BR-fleetio-vehicle-032 | Tên xe, VIN không được trùng; trùng VIN xét cả xe Sample; tên của xe đã Archive không tính trùng. | [Lõi] | Lưu xe | FR-fleetio-vehicle-050 | `Chạy` một phần | Tên xe Archived chỉ thấy không báo lỗi, chưa lưu thành công. VIN của xe Archived chưa thử |
| BR-fleetio-vehicle-033 | Add Multiple không kiểm trùng ở bước xem lại; dòng lỗi không tạo xe, báo qua email người đang đăng nhập; Group chưa có thì tự tạo cả cấp cha. | [Cấu hình] | Add Multiple | FR-fleetio-vehicle-002 | `Chạy`, `Xem` phần tự tạo Group | Câu trên màn "Any group (including parents) that do not exist will be created." |
| BR-fleetio-vehicle-034 | Giải mã VIN không tự ghi đè: dòng Different mặc định không tick, chỉ ghi vào xe khi Save Vehicle. | [Cấu hình] | Giải mã VIN | FR-fleetio-vehicle-007 | `Chạy` | Vehicle Type Semi Truck với Car không tick |
| BR-fleetio-vehicle-035 | Liên kết không kiểm loại xe, không giới hạn số xe nối với một mooc. | [Lõi] | Sửa liên kết | FR-fleetio-vehicle-008 | `Chạy` | `TEST-MOOC-LOP` nối `TEST-XE-LOP` và `TEST-XE-01` (Car) |
| BR-fleetio-vehicle-036 | Out-of-Service Date, Out-of-Service Odometer chỉ là trường dữ liệu: không đổi Status, không tạo dòng đồng hồ, có ghi Record History. | [Lõi] | Sửa xe | FR-fleetio-vehicle-006 | `Chạy` | Nhập ngày 03/11, Odometer 10; xe vẫn Active, 0 km |
| BR-fleetio-vehicle-037 | Xe thật không dùng được nhóm Sample; lỗi một trường làm cả form bị từ chối, các thay đổi khác cũng không áp dụng. | [Lõi] | Sửa xe | FR-fleetio-vehicle-025 | `Chạy` | Lưu In Shop kèm nhóm Sample: xe vẫn Sold, No Group |
| BR-fleetio-vehicle-038 | Đóng Lệnh bắt Started At, và theo cài đặt tài khoản bắt Starting Meter Entry, Odometer; đóng Lệnh tự sinh Service Entry. | [Cấu hình] | Đóng Lệnh | FR-fleetio-vehicle-021 | `Chạy` | "per your account settings"; chi tiết ở nhóm Sửa chữa |
| BR-fleetio-vehicle-039 | Hộp đính chỉ nhận tài liệu dùng chung có sẵn, một tài liệu đính được vào số xe bất kỳ; tệp riêng của xe đi qua ô kéo thả ở panel Documents. | [Lõi] | Đính tài liệu | FR-fleetio-vehicle-054 | `Chạy` | "You may attach a shared document to any number of vehicles." Số xe nhiều chỉ là câu chữ |
| BR-fleetio-vehicle-040 | Thêm đồng hồ phụ trên xe đang có số không đổi đồng hồ chính; số phụ bắt đầu từ 0 nếu không nhập Current Reading. | [Cấu hình] | Lưu xe | FR-fleetio-vehicle-044 | `Chạy` | `TEST-DAUKEO-2`, "Secondary Meter 0 hr" |

## 6. Error Matrix

| Error ID | Title | Trigger | Severity | Related FR | Screen state | Recovery | Mức |
|---|---|---|---|---|---|---|---|
| E-fleetio-vehicle-001 | Trùng gán | "can't overlap existing assignments", toast "Vehicle Assignment could not be created" | major | FR-fleetio-vehicle-010 | Viền đỏ cả hai ô ngày | Đổi thời gian; tự đóng phân công cũ nếu cần | `Chạy` |
| E-fleetio-vehicle-002 | Số nhỏ hơn cùng ngày không báo | Nhập 900 khi đang 1.010, 5.300 khi đang 5.500, cùng ngày | minor | FR-fleetio-vehicle-013 | Lưu, hiện "110 km ago", "200 km ago" | Không nên học. Khác ngày thì xem E-fleetio-vehicle-004, 005 | `Chạy` |
| E-fleetio-vehicle-003 | Tạo liên hệ ngoài ý muốn | Enter khi tên chưa có | minor | FR-fleetio-vehicle-011 | Mở Add Contact, dữ liệu gõ sau rơi sai ô | Không nên học | `Chạy` |
| E-fleetio-vehicle-004 | Số lớn hơn số ngày sau | Lùi ngày, nhập 5.800 ngày 01/11: "must be less than 5,000 or marked as void", "Meter Entry could not be created" | major | FR-fleetio-vehicle-032 | Lỗi ở trường, không lưu | Sửa số hoặc tick Void. Số so sánh là dòng đầu ngày sau, không phải số hiện tại | `Chạy` |
| E-fleetio-vehicle-005 | Số nhỏ hơn số ngày trước | Nhập 5.400 ngày 04/11: "must be greater than 5,500 or marked as void" | major | FR-fleetio-vehicle-032 | Lỗi ở trường, không lưu | Sửa số hoặc tick Void | `Chạy` |
| E-fleetio-vehicle-006 | Vượt mức một ngày | "Meter Entry was successfully created. However, it was automatically voided because it exceeds maximum possible for day"; popup "Automatically voided because it exceeds the maximum daily usage of 4,828 kilometers by 9,672 kilometers" | major | FR-fleetio-vehicle-014 | Lưu, Void Status "Auto-Voided", Auto-Void Reason "Exceeds Max. Daily Usage" | "Unvoid this Entry" hoặc nhập lại số đúng | `Chạy` |
| E-fleetio-vehicle-007 | Dòng gây xung đột | "This entry was flagged because it has caused one or more successive entries to be auto-voided", Conflicts With 1 Entry, Difference 14,500 kilometers over 0 days | minor | FR-fleetio-vehicle-015 | Cờ đỏ, Void Status "Conflict Source" | Sửa dòng gốc hoặc Unvoid dòng con | `Chạy` |
| E-fleetio-vehicle-008 | Phiếu dầu lệch thứ tự | Fuel Entry odometer 21.000 ngày 01/11: "must be less than 5,000 or marked as void", "Fuel Entry could not be created" | major | FR-fleetio-vehicle-032 | Lỗi ở trường, không lưu | Sửa số hoặc tick Void | `Chạy` |
| E-fleetio-vehicle-009 | Hết hạn mức xe | "Your plan is limited to 5 vehicles", "Vehicle could not be created"; ở lượt khác nút Save Vehicle khoá, "You've reached the maximum number of records allowed on your account." | major | FR-fleetio-vehicle-023 | Nút khoá, "5 of 5" | Nâng gói hoặc lưu trữ xe | `Chạy` |
| E-fleetio-vehicle-010 | Tên xe trống | "can't be blank" | major | FR-fleetio-vehicle-001 | Lỗi ở trường, kèm lỗi hạn mức nếu đã hết | Nhập tên | `Chạy` |
| E-fleetio-vehicle-011 | Ngày giả điền sẵn | Start Date của chi phí định kỳ, bảo hành hiện chữ xám là placeholder, lưu báo "can't be blank" | minor | FR-fleetio-vehicle-018, FR-fleetio-vehicle-035 | Trông như đã điền | Gõ ngày. Không nên học | `Chạy` |
| E-fleetio-vehicle-012 | Không phải Operator | "Contact must have operator classification to be assigned to vehicles" | minor | FR-fleetio-vehicle-011 | Câu dẫn ở khối xe trên trang liên hệ | Bật phân loại Operator | `Chạy` |
| E-fleetio-vehicle-013 | Hộp nhập hiện số cũ | "Last updated: 5,000 km (Today)" khi xe đã 5.500; hộp "Save and Add Another" vẫn "No meter history" sau khi vừa lưu 100 km | minor | FR-fleetio-vehicle-013 | Thông tin gợi ý sai | Không nên học | `Chạy` |
| E-fleetio-vehicle-014 | Start Meter lệch khi hiển thị | Nhập 1000, danh sách bảo hành ghi 1 km, End Meter 50,001 km | major | FR-fleetio-vehicle-036 | Chưa rõ do ô nhập hay định dạng | OQ-10 | `Chạy` |
| E-fleetio-vehicle-015 | Unvoid nhầm ghim đồng hồ | Sau khi Unvoid 20.000 các số thật sẽ bị "must be greater than" | major | FR-fleetio-vehicle-031 | Đồng hồ xe 20.000 | Void lại dòng đó (`Suy`) | `Chạy`, `Suy` |
| E-fleetio-vehicle-016 | Không có mẫu bảo hành | Ô Coverage Template báo "No options" | minor | FR-fleetio-vehicle-039 | Ô chọn rỗng | Nhập tay Standard Warranty | `Chạy` |
| E-fleetio-vehicle-017 | Lệch múi giờ phân công | Ngày gửi đi theo múi giờ thiết bị trong khi tài khoản đặt America/Chicago. Ngày đồng hồ cũng có thể lệch: dòng phiếu Fleetio Go ghi 11/02 so với giờ Việt Nam (`Suy`) | minor | FR-fleetio-vehicle-009 | Không báo trên ô ngày; đầu trang có dải "Your local timezone on your device (Asia/Saigon) does not match your user settings timezone in Fleetio (America/Chicago)." | OQ-13 | `Chạy` |
| E-fleetio-vehicle-018 | Dòng định kỳ đúng hôm nay ở tab Future | Tab Past trống sau khi lưu dù dòng 03/11 đúng hôm nay, còn Cost of Ownership đã tính dòng đó | minor | FR-fleetio-vehicle-033, FR-fleetio-vehicle-034 | Hai nơi nói khác nhau | Không nên học | `Chạy` |
| E-fleetio-vehicle-019 | Lý do Out of Sequence | Phiếu Fleetio Go 3.100 km: "Automatically voided because it is out of sequence and ahead of the conflicting meter by 601 kilometers"; nhập tay trên web cùng tình huống chỉ ra E-fleetio-vehicle-004, 005 | major | FR-fleetio-vehicle-014 | Void Status "Auto-Voided", Conflicting Entry 2.499 km, Conflict Status "601 kilometers ahead of"; dòng 2.499 km cờ đỏ; xe vẫn 2.999 km | Menu dòng có Edit, Unvoid, View Record History, Delete (chưa bấm). OQ-8 | `Chạy` |
| E-fleetio-vehicle-020 | Chọn lẫn dòng khi Void hàng loạt | Tick cả dòng đã Void và chưa Void, mở Actions | minor | FR-fleetio-vehicle-047 | Void, Unvoid đều khoá, không có câu giải thích | Bỏ tick dòng đã Void | `Chạy` |
| E-fleetio-vehicle-021 | Archive khi còn Lệnh mở | Toast "Vehicle could not be archived." không nêu lý do | major | FR-fleetio-vehicle-021 | Xe không Archive; câu lý do chỉ có trong hộp xác nhận trước đó | Đóng Lệnh rồi Archive lại | `Chạy` |
| E-fleetio-vehicle-022 | Archive bị từ chối vẫn ngắt liên kết | Lần Archive của E-fleetio-vehicle-021 vẫn xoá liên kết với mooc ở cả hai phía; phân công tương lai còn nguyên. Đối chứng: lưu Sold, In Shop liên kết còn; Archive bị từ chối thì mất. Thấy 2/2 lần | critical | FR-fleetio-vehicle-008, FR-fleetio-vehicle-021 | Không báo, Record History không có dòng nào | Nối lại bằng tay. Không nên học: thao tác phải trọn vẹn hoặc không có gì | `Chạy` |
| E-fleetio-vehicle-023 | Restore khoá khi đầy gói | Vehicles 5 of 5, xe Archived | minor | FR-fleetio-vehicle-048 | Nút khoá, bấm không có gì, không có câu giải thích | Giải phóng chỗ hoặc nâng gói. Không nên học | `Chạy` |
| E-fleetio-vehicle-024 | Trùng tên, trùng VIN | "has already been taken" ở Vehicle Name, VIN; toast "Vehicle could not be created" | major | FR-fleetio-vehicle-050 | Lỗi ở trường | Đổi tên, VIN | `Chạy` |
| E-fleetio-vehicle-025 | Add Multiple lỗi chỉ báo qua email | "Process warning: Add Multiple Vehicles", "Please check your email for detailed information about records that failed to create." | major | FR-fleetio-vehicle-002 | Không tạo xe, màn không nêu dòng nào sai, lý do gì | Mở email, sửa, dán lại. Không nên học. Nội dung email chưa kiểm | `Chạy` |
| E-fleetio-vehicle-026 | Decode khoá với VIN ngắn | VIN `ABC123` | minor | FR-fleetio-vehicle-007 | Nút khoá, rê chuột không có câu giải thích | Nhập đủ 17 ký tự | `Chạy` |
| E-fleetio-vehicle-027 | Kẹt hộp rời trang | Thoát form có thay đổi chưa lưu | minor | FR-fleetio-vehicle-007 | Tab kẹt hộp rời trang | Mở tab mới | `Chạy` |
| E-fleetio-vehicle-028 | Nhóm Sample trên xe thật | "Selected group is a sample, and cannot be used with non-sample records.", toast "Vehicle could not be updated" | minor | FR-fleetio-vehicle-025 | Lỗi ở trường, dấu đỏ ở mục Details dù đang đứng ở Lifecycle; mọi thay đổi khác trong form cũng không lưu | Bỏ nhóm | `Chạy` |
| E-fleetio-vehicle-029 | Đóng Lệnh thiếu thông tin, số lệch | "Started At can't be blank", "Starting Meter Entry can't be blank (per your account settings)", "Odometer can't be blank (per your account settings)"; Start Odometer 4.928: "must be less than 100 or marked as void" | major | FR-fleetio-vehicle-032 | Lỗi ở trường, Lệnh chưa đóng | Nhập đủ, sửa số. Thử 90 thì qua | `Chạy` |
| E-fleetio-vehicle-030 | Liên hệ không phải Operator trong ô gán | Gõ tên liên hệ chỉ phân loại Technician | minor | FR-fleetio-vehicle-011 | Chỉ có dòng "Create "…"", không báo lý do | Bật phân loại Operator ở liên hệ. Dễ tạo trùng liên hệ, không nên học | `Chạy` |
| E-fleetio-vehicle-031 | Start Meter trống sau khi lưu | Form phân công đã điền sẵn 4.928, cột Start Meter sau đó trống | minor | FR-fleetio-vehicle-009, FR-fleetio-vehicle-029 | Không báo | Nguyên nhân chưa tách riêng | `Chạy` |
| E-fleetio-vehicle-032 | Add Multiple khoá theo gói | Gói 5 of 5, tooltip cuối câu "...to add more Vehicles." (ghi chú không chép đủ câu) | minor | FR-fleetio-vehicle-002, FR-fleetio-vehicle-023 | Mục xám có khoá, bấm không mở form, không điều hướng | Nâng gói hoặc giải phóng chỗ | `Chạy` |

## 7. Success Criteria

| ID | Outcome nghiệp vụ | Đo bằng | Mốc đạt |
|---|---|---|---|
| SC-fleetio-vehicle-01 | Mọi thứ của xe xem được một nơi | Số màn phải mở để xử lý | TBD |
| SC-fleetio-vehicle-02 | Biết ai giữ xe lúc nào | Không có khoảng trùng theo xe; người cũ còn trong lịch sử | 0 trùng; Fleetio chỉ đạt vế đầu |
| SC-fleetio-vehicle-03 | Số km tin cậy | Tỉ lệ dòng bị Void, dòng lùi | TBD |
| SC-fleetio-vehicle-04 | Chi phí/km đúng | Số dòng số km sai lọt vào phép tính | TBD |

## 8. Data Entities (tóm tắt — chi tiết ở erd.md)

Vehicle, Contact, Assignment, Meter Entry, Status Update, Record History, Expense Entry, Warranty, Warranty Coverage Code, Recall, Motor Pool Reservation; Tire Reading thuộc nhóm Lốp. Xem [[docs/_research/fleetio/srs/fleetio-vehicle-erd.md|ERD]].

## 9. Flows (tóm tắt — chi tiết ở flows.md)

Xem [[docs/_research/fleetio/srs/fleetio-vehicle-flows.md|Flows]], [[docs/_research/fleetio/srs/fleetio-vehicle-states.md|States]], [[docs/_research/fleetio/srs/fleetio-vehicle-usecases.md|Use case]], [[docs/_research/fleetio/srs/fleetio-vehicle-userflow.md|User flow]].

## 10. Screens

Ảnh thật và bảng mô tả: [[docs/_research/fleetio/srs/fleetio-vehicle-screens.md|Màn hình]]. Không áp `CMP`, `GR` vì mô tả sản phẩm của bên khác.

## 11. Constraints, Dependencies & Assumptions

| Giả định | Invalidate nếu sai |
|---|---|
| `GĐ` Số km của Delta chủ yếu từ GPS | Luật tự Void phải đổi cho nhập tay |
| `GĐ` Một thời điểm xe chỉ có một người lái chính | BR-fleetio-vehicle-002 phải nới cho lái ca |
| `Chạy` Linked Vehicles chỉ là đường dẫn hai chiều, không có ngày, không truyền km, không gộp lốp; không thay được nghiệp vụ ghép tách mooc | Nếu Delta chỉ cần biết mooc nào hay đi với đầu kéo nào thì đủ |
| `Chạy` Tài khoản dùng thử trần 5 xe; lượt 3 đã chạy trùng tên xe, đổi trạng thái thật, Archive, Restore. Còn Motor Pool, dán nhiều dòng vượt hạn mức chưa chạy | Cần một chỗ xe trống để kiểm; hiện 5 of 5, `TEST-XE-LOP` đang Archived |

## 12. Open Questions

* [x] OQ-1: Một xe nhiều người lái theo ca được không? — Trả lời (`Chạy`): theo Fleetio được, miễn các khoảng không chồng nhau trên xe; trùng theo người không bị chặn. Quyết định của Delta chuyển sang OQ-7. — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-2: GPS và đồng hồ lệch thì lấy số nào? Lượt chạy không có nguồn telematics. — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-3: Có đo gai lốp định kỳ không? Sự thật phía Fleetio đã ở `fleetio-tires`; phía Delta vẫn phải quyết định. — Nguồn khách: file sơ đồ lốp của Delta
* [x] OQ-4: Tab Tire Management chưa xem được vì xe chưa có lốp; cần cấu hình trục — Trả lời (`Chạy`): xem được; cấu hình trục khai ở tab này của từng xe, chi tiết ở `fleetio-tires`. — Nguồn khách: không áp dụng
* [x] OQ-5: "Out of Sequence" chính xác là gì? `Chạy` nhập 900 khi đang 1.010 cùng ngày không bị Void; ngưỡng "giá trị cao" chỉ áp trên app, chưa có số — Trả lời (`Chạy`): lệch thứ tự theo ngày bị từ chối ở trường, không Void; cùng ngày nhỏ hơn không bị gì; lý do Out of Sequence không tái hiện được trên web. Phần còn lại chuyển sang OQ-8, OQ-9. — Nguồn khách: không áp dụng
* [x] OQ-6: Số sai dưới ngưỡng ghim số hiện tại, hoặc Void toàn bộ thì xe không còn số hiện tại: xử lý thế nào? — Trả lời (`Chạy`): số sai dưới ngưỡng cùng ngày không ghim vì lấy số lớn nhất; số sai trên ngưỡng tự Void; Unvoid nhầm thì ghim số hiện tại. Void toàn bộ: xe về "0 km", hộp nhập "No meter history", nhận số bất kỳ (`Chạy` lượt 3). — Nguồn khách: không áp dụng
* [ ] OQ-7: Delta có cho một xe nhiều người lái theo ca không, và có chặn một người giữ nhiều xe cùng lúc không? — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-8: Lý do Out of Sequence có chỉ xảy ra với nguồn không có người sửa (telematics, API) không? Một phần: phiếu Fleetio Go 3.100 km bị Auto-Voided Out of Sequence, lệch 601 km; nhập tay web bị chặn ở trường, app lưu rồi tự Void. Mới một ca, chưa thử telematics, API (`Chạy`). Thứ tự sự kiện chưa rõ: dòng xung đột 2.499 km ghi ngày sau dòng 3.100 km, nên chưa biết phiếu bị Void ngay lúc lưu hay lúc có số 2.499 km — Nguồn khách: không áp dụng
* [ ] OQ-9: Ngưỡng cảnh báo "giá trị cao" trên app là bao nhiêu? — Nguồn khách: không áp dụng
* [ ] OQ-10: Start Meter nhập 1000 mà hiện 1 km là do ô nhập hay định dạng? — Nguồn khách: không áp dụng
* [ ] OQ-11: Đổi trạng thái thật, Archive và Restore xe, bản ghi trùng tên xe, Motor Pool chạy ra sao? Một phần (`Chạy` lượt 3): đổi trạng thái tự do, không ràng buộc; Archive, Restore xem Mục 13.10; trùng tên, VIN báo "has already been taken". Còn mở: Motor Pool đang đặt có chặn Archive thật không, mới có câu trong hộp thoại. — Nguồn khách: không áp dụng
* [ ] OQ-12: Ô Starting Odometer, Ending Odometer có thêm ràng buộc theo ngày không? Bản 02/11 và 03/11 ghi khác nhau. Lượt 3: ô xám khi Start bằng thời điểm hiện tại lúc chưa chọn đủ, mở khi chọn ngày, có lần tự điền số hiện tại; chưa tách được quy luật. — Nguồn khách: không áp dụng
* [ ] OQ-13: Giờ phân công lưu theo múi giờ nào khi thiết bị và tài khoản khác nhau? Lượt 3: dòng đồng hồ phiếu Fleetio Go cũng ghi lệch ngày so với giờ Việt Nam (`Suy`, chưa tách riêng). — Nguồn khách: không áp dụng
* [ ] OQ-14: Sửa phân công đã qua, xoá phân công, nút claim bảo hành, Bulk Meter Management, điều kiện có Coverage Template chạy thế nào? Phần Bulk một phần: Void hàng loạt trên danh sách đã chạy, chưa đối chiếu có đúng tính năng hãng gọi tên đó, chưa có số GPS. Các phần khác còn mở. — Nguồn khách: không áp dụng
* [ ] OQ-15: Replacement Analysis có tự lưu khi đổi số không? Công thức các năm sau, Sum of Years, Optimal Replacement tính thế nào? — Nguồn khách: không áp dụng
* [x] OQ-16: Một mooc gắn được nhiều đầu kéo không? Không chạy do hết chỗ xe. Trả lời: một mooc nối được nhiều xe, không có ngày hiệu lực, không chặn, không kiểm loại xe (`Chạy`) — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-17: Delta có cần chặn gán tài xế, mở lệnh, nhập đồng hồ khi xe Sold, Out of Service không? Fleetio không chặn gì (`Chạy`). — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-18: Khi thay đồng hồ, Delta có cần khai báo riêng kèm lý do và số chốt của đồng hồ cũ không? Fleetio không có bước này (`Chạy`). — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-19: Add Multiple: email lỗi ghi gì, dán nhiều dòng vượt hạn mức thì sao, nhập Group mới thì sao? Chưa kiểm hộp thư, chưa thử vì vượt gói và tạo danh mục dùng chung. Lượt 4: gói đầy thì lối vào khoá từ menu, chưa từng thấy form dán nhiều dòng trong gói đầy; vẫn chưa chạy. — Nguồn khách: không áp dụng
* [ ] OQ-22: Huy hiệu "(1)" trên icon Documents đếm gì? Trước khi đính, xe không có tài liệu nào trong panel; sau khi đính có đúng 1 thẻ và huy hiệu tắt. — Nguồn khách: không áp dụng
* [ ] OQ-20: Manage Tab Menu, kéo đổi thứ tự thẻ, Add Layout chạy ra sao? Manage Service Programs, Attach Shared Document đã chạy ở lượt 4. Recalculate Fuel Entries hiện theo điều kiện gì: lượt 3 không thấy trên 2 xe không có Fuel Entry, lượt 4 thấy trên `TEST-DAUKEO-2`, chưa đối chiếu xe này có Fuel Entry không. Gán nhóm thật có lịch sử đổi nhóm thế nào? — Nguồn khách: không áp dụng
* [ ] OQ-21: Cột thời lượng của Status Updates là thời gian ở trạng thái nào? Ghi chú chạy thử ghi "trạng thái trước"; ảnh `vehicle-status-history` khớp thời gian ở trạng thái đích, tính tới lần đổi kế tiếp (`Suy`). — Nguồn khách: không áp dụng

## 13. Ma trận case

### 13.1 Tạo xe, hạn mức

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| Save rỗng | Form trống, đã hết hạn mức | "can't be blank" + "Your plan is limited to 5 vehicles" + toast "Vehicle could not be created" | `Chạy` |
| Có tên, hết hạn mức | Gõ `TEST-NEN-01`, Save | Vẫn "Your plan is limited to 5 vehicles" | `Chạy` |
| Lối phụ qua hạn mức | Dán nhiều dòng vượt hạn mức, nhập tệp | Không thử vì vượt gói | Không chạy |
| Add Multiple, dòng trùng | 1 dòng trùng tên và trùng VIN xe mẫu | Bước 2 chỉ hiện lại bảng, không kiểm trùng. "Process warning: Add Multiple Vehicles", "Please check your email…"; không tạo xe, màn không nêu lý do | `Chạy` |
| Add Multiple, dòng hợp lệ | 1 dòng | "Processing", rồi "Complete: Add Multiple Vehicles"; xe mới Active, Car, 0 km, VIN giải mã ra Honda, Accord, 2003 | `Chạy`, `images/vehicle-add-multiple-step1.jpg` |
| Add Multiple, trường từ VIN | Xe vừa tạo | Có Front, Rear Tire Type từ VIN; MSRP vẫn 0, khác bảng giải mã tay ($26,360.00) | `Chạy` |
| Add Multiple, Group mới | Câu trên màn nói tự tạo cả cấp cha | Không thử vì tạo danh mục dùng chung | `Xem`, Không chạy |
| Lên đầy gói | Sau xe thứ 5 | Thanh đỏ, Add Vehicle khoá, Add Multiple khoá | `Chạy` |
| Xe Sample | 25 xe tính cả Sample, Usage "5 of 5" | Sample không tính vào hạn mức | `Chạy` |
| Mặc định form | Mở New Vehicle | Type Car, Status Active, Ownership Owned, Average Usage "Automatically calculate" | `Xem` |
| Trục trong form xe | Mở form Semi Truck | KHÔNG có trục; Wheels & Tires chỉ là trường chữ. Xem `fleetio-tires` | `Chạy` |
| Thanh lý | Tìm luồng bán, thanh lý | KHÔNG có nút; chỉ Out-of-Service Date, Odometer, trạng thái Sold | `Xem` |
| Nhập Out-of-Service | Date 03/11, Odometer 10 trên `TEST-DAUKEO-2` | KHÔNG đổi Status, KHÔNG tạo dòng đồng hồ, xe vẫn 0 km; Record History có 2 dòng | `Chạy` |
| Đổi loại xe | Car sang Semi Truck | Đổi tự do, không hỏi; dòng phụ đổi theo, Status giữ Active | `Chạy` |
| Đơn vị lẫn | Odometer phần Financial | Hiện "mi" trong khi Specifications hiện cm, kg, lít; chưa rõ lý do | `Xem` |
| Trùng tên, VIN, form đơn | Cùng dữ liệu xe đã có | Vehicle Name, VIN đều "has already been taken", "Vehicle could not be created" | `Chạy` |
| Trùng VIN với xe Sample | VIN của xe mẫu | Vẫn báo trùng | `Chạy` |
| Tên của xe đã Archive | VIN vẫn trùng để không lưu | KHÔNG báo trùng tên, chỉ VIN báo lỗi; chưa lưu thành công | `Chạy` một phần |

### 13.2 Mooc, Linked Vehicles

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| Tạo mooc | Type Trailer, đồng hồ để trống | Lưu thành "0 km"; là Vehicle riêng | `Chạy` |
| Tổ hợp | Tìm đối tượng đầu kéo + mooc | KHÔNG có | `Chạy` |
| Liên kết | Thêm mooc vào Linked Vehicles của đầu kéo | Đầu kéo có Linked Assets › VEHICLES › mooc; mooc cũng hiện đầu kéo | `Chạy`, `images/vehicle-cost-of-ownership.jpg` |
| Gộp lốp | Xem Tire Management đầu kéo sau liên kết | KHÔNG thêm lốp mooc, vẫn 3 trục | `Chạy` |
| Truyền km | Đầu kéo tăng km | Mooc KHÔNG đổi, giữ 3.500 | `Chạy`, `run-notes/tires.md` |
| Gỡ liên kết | Xoá chip ở đầu kéo | Mooc "There are no linked Assets for this Vehicle"; đồng hồ, lốp không đổi | `Chạy`, `run-notes/tires.md` |
| Gắn lại phía mooc | Thêm từ mooc | Đầu kéo hiện lại mooc | `Chạy`, `run-notes/tires.md` |
| Đổi mooc | Gỡ rồi gắn | KHÔNG có lịch sử ghép, KHÔNG có ngày | `Suy` |
| Một mooc nhiều xe | `TEST-MOOC-LOP` nối `TEST-XE-LOP`, thêm `TEST-XE-01` (Car) | Lưu được cả hai, "Linked Assets have been updated", KHÔNG cảnh báo, KHÔNG kiểm loại xe, hiện ở cả hai phía | `Chạy`, `images/trailer-linked-two-vehicles.jpg` |
| Ô chọn khi đã nối | Xe đã nối | Không còn trong ô chọn; form xe có trường "Linked Vehicles" cùng dữ liệu | `Chạy` |
| Biết đang kéo bởi đầu nào | Mooc nối 2 xe | KHÔNG có ngày hiệu lực, KHÔNG biết xe nào đang kéo | `Chạy` |
| Một xe nối bị Archive | `TEST-XE-LOP` Archive | Mooc chỉ còn `TEST-XE-01` | `Chạy` |
| Lưu Sold, In Shop | Xe có liên kết | Liên kết còn nguyên | `Chạy` |

### 13.3 Gán xe

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| Tạo thường | `TEST-XE-LOP` + `TEST-LAI-XE-02`, 05/11 đến 07/11 | Tạo được, thanh cam trên lịch | `Chạy`, `images/assignment-add.jpg` |
| Bấm ô trống | Lịch tuần | "Add Vehicle Assignment For TEST-XE-LOP", xe khoá, ngày điền theo ô | `Chạy`, `images/assignment-week.jpg` |
| Trùng xe | Start 04/11 không End đè 05/11 | "can't overlap existing assignments" ở cả Start, End; KHÔNG tự đóng cũ | `Chạy`, `images/assignment-overlap.jpg` |
| Trùng xe, ngày 02/11 | Lượt đầu trên `TEST-XE-01` | Cùng lỗi, viền đỏ hai ô ngày | `Chạy` |
| Trùng người | `TEST-LAI-XE` giữ `TEST-XE-01` "No end date", gán thêm `TEST-XE-LOP` | KHÔNG chặn: "successfully updated", "successfully created" | `Chạy` |
| Một xe nhiều người theo khoảng | Hai khoảng 05–07/11, 10–12/11 | Được | `Chạy` |
| Thay người | Edit Operator phân công tương lai | Lưu đè; xe khoá; KHÔNG còn dấu vết người cũ trên trang | `Chạy`, `images/assignment-edit.jpg`, `images/assignment-detail.jpg` |
| Hành động "thay người" riêng | Tìm trong menu | KHÔNG có. Phải tự đóng cũ, tạo mới | `Chạy` |
| Gợi ý số km | Mở Edit | Starting Odometer 20000.0 lấy theo đồng hồ hiện tại | `Chạy` |
| Không phải Operator | Khối xe trên liên hệ | Bị chặn bằng câu dẫn | `Chạy`, `images/contact-no-access.jpg` |
| Tên chưa có | Enter ở ô chọn | Mở Add Contact, dữ liệu rơi sai ô | `Chạy` |
| Múi giờ | Ngày gửi đi | Theo múi giờ thiết bị dù tài khoản đặt múi giờ khác | `Chạy` |
| Xoá | Menu thanh | Có Delete, không bấm | `Xem` |
| Sửa phân công đã qua | | Chưa thử | Không chạy |
| Gõ liên hệ chỉ Technician | `TEST-SUA-KTV`, gõ "TEST-SUA" | Không có trong kết quả, chỉ có dòng "Create "TEST-SUA"", KHÔNG báo lý do; không bấm | `Chạy` |
| Trùng xe, trùng người, lượt 3 | Trên `TEST-DAUKEO-2` | Trùng xe chặn, trùng người KHÔNG chặn: như lượt trước | `Chạy` |
| Ô Starting Odometer | Start bằng thời điểm hiện tại, chưa chọn đủ | Xám; chọn ngày thì mở; có lần tự điền số hiện tại | `Chạy`, quy luật chưa tách |
| Gán khi Out of Service | Xe Out of Service, Inactive | Lưu được, KHÔNG cảnh báo | `Chạy` |
| Start Meter sau khi lưu | Form điền sẵn 4.928 | Cột Start Meter trống | `Chạy` |

### 13.4 Số đồng hồ

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| Hợp lệ tăng | 5.500 hôm nay khi đang 5.000 | Lưu, lên số hiện tại | `Chạy` |
| Lùi ngày, số cao | 5.800 ngày 01/11 | TỪ CHỐI, "must be less than 5,000 or marked as void"; KHÔNG tự Void | `Chạy`, `images/meter-reject-backdate.jpg` |
| Ngày tương lai, số thấp | 5.400 ngày 04/11 | TỪ CHỐI, "must be greater than 5,500 or marked as void" | `Chạy`, `images/meter-reject-forward.jpg` |
| Lùi ngày, tick Void | 5.800 ngày 01/11, Void | Lưu, "Manually Voided", đồng hồ không đổi | `Chạy` |
| Cùng ngày, số nhỏ | 5.300 khi đang 5.500 | Lưu, KHÔNG Void, KHÔNG báo; đồng hồ giữ 5.500; "200 km ago" | `Chạy` |
| Cùng ngày, số nhỏ, 02/11 | 900 khi đang 1.010 | Như trên, "110 km ago" | `Chạy` |
| Trùng giá trị | Hai dòng 1.010 trên `TEST-XE-01` | KHÔNG gộp, KHÔNG báo | `Chạy` |
| Nhảy quá ngưỡng | 20.000 hôm nay khi 5.500 | Lưu + tự Void, "Exceeds Max. Daily Usage", vượt 9.672 km | `Chạy`, `images/meter-history-conflict.jpg` |
| Dòng gốc | 5.500 sau khi có 20.000 | Cờ đỏ, "Conflict Source", Difference 14,500 km over 0 days | `Chạy` |
| Unvoid | Dòng 20.000 | Confirm, KHÔNG hỏi lý do, KHÔNG kiểm lại ngưỡng; đồng hồ lên 20.000; cờ của 5.500 tự mất | `Chạy` |
| Phiếu dầu cùng luật | Odometer 21.000 ngày 01/11 | "must be less than 5,000 or marked as void" | `Chạy` |
| Số so sánh trong lỗi | Lỗi 5.800 | So với 5.000 là dòng đầu ngày 03/11, không phải số hiện tại 5.500 | `Chạy` |
| Gợi ý số cũ | Hộp nhập khi xe 5.500 | "Last updated: 5,000 km (Today)" | `Chạy` |
| Out of Sequence, nhập tay | Mọi cách nhập tay trên web | KHÔNG ra lý do này, bị chặn ở trường | `Chạy` |
| Out of Sequence, phiếu Fleetio Go | Dòng 3.100 km ngày 11/02 trên `TEST-XE-01` | Lưu rồi "Auto-Voided", Auto-Void Reason "Out of Sequence"; "ahead of the conflicting meter by 601 kilometers" | `Chạy`, `images/meter-out-of-sequence-autovoid.jpg` |
| Dòng xung đột của ca trên | 2.499 km ngày 11/03, nguồn Manual | Cờ đỏ, "Conflict Source", Conflicts With 1 Entry, "601 kilometers over 1 day" | `Chạy` |
| Icon lạ ở số 3.100 km | Cột Meter Value | Là dấu đã Void; số gạch ngang | `Chạy` |
| Số hiện tại ca trên | Có dòng 3.100 km Void | Xe vẫn 2.999 km | `Chạy` |
| Out of Sequence, telematics, API | Không có nguồn | Chưa thử | Không chạy |
| Biên ngưỡng ngày, đúng mức | Từ 100 nhập 4.928 (+4.828) | Lưu bình thường, thành số hiện tại | `Chạy` |
| Biên ngưỡng ngày, vượt 1 km | Nhập 9.757 (+4.829) | Auto-Voided, "Exceeds Max. Daily Usage"; dòng 4.928 thành "Conflict Source"; đồng hồ giữ 4.928 | `Chạy` |
| Void dòng gốc rồi Unvoid dòng con | | Chưa chạy | `Docs` |
| Void hàng loạt, chọn lẫn | Có cả dòng đã Void và chưa Void | Void, Unvoid đều khoá | `Chạy` |
| Void hàng loạt, chỉ dòng chưa Void | 5 dòng | Void mở; hộp đòi gõ VOID, Confirm khoá tới khi đúng; "Successfully voided Meter Entries" | `Chạy` |
| Void lại dòng từng Auto-Voided | Dòng 20.000 đã Unvoid | Về "Auto-Voided", "Exceeds Max. Daily Usage", KHÔNG thành Manually Voided; 4 dòng khác "Manually Voided" | `Chạy`, `images/meter-bulk-void-secondary.jpg` |
| Void toàn bộ | Mọi số của xe | Xe "0 km", "Last updated: No meter history" | `Chạy` |
| Nhập lại từ số nhỏ | 100 km sau Void toàn bộ | Nhận ngay, KHÔNG báo nhỏ hơn số cũ; lịch sử số cũ còn | `Chạy` |
| Khai báo thay đồng hồ | Tìm bước riêng | KHÔNG có, KHÔNG lưu lý do | `Chạy` |
| Mục tên Bulk Meter Management | Các menu đã mở; menu "…" chỉ có Import Meter Entries, Export Data | KHÔNG thấy; chưa đối chiếu với tài liệu hãng | `Chạy`; tên là `Docs` |
| Void số GPS | Không có nguồn GPS | Chưa chạy | `Docs` |
| Hộp sau lưu | "Save and Add Another" sau khi lưu 100 km | Vẫn "No meter history" | `Chạy` |
| Đồng hồ khi xe Sold | Nhập số trên xe Sold | Lưu được, KHÔNG cảnh báo | `Chạy` |

### 13.5 Chi phí, Cost of Ownership

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| Định kỳ | Insurance 1.500.000 ₫, 03/11/2026 đến 31/01/2027, hàng tháng | Xử lý nền, sinh 03/11, 03/12, 03/01 trong Future | `Chạy`, `images/expense-recurring.jpg`, `images/expense-future.jpg` |
| Dòng đúng hôm nay | 03/11 | Vẫn ở Future, Past trống; nhưng Cost of Ownership đã tính | `Chạy` |
| Đơn lẻ | Tolls 2.000.000 ₫ ngày 15/10/2026 | Lưu, Expense Entry riêng | `Chạy` |
| This Month | Sau hai khoản | Total 1.500.000 ₫, 100 ₫/km, Fuel 0, Service 0, Other 1.500.000 | `Chạy`, `images/vehicle-cost-of-ownership.jpg` |
| All Time | | 3.500.000 ₫, 233 ₫/km; 03/12, 03/01 KHÔNG tính | `Chạy` |
| Số km sai | Mẫu số 15.000 đến từ số đã Unvoid | Một số đồng hồ sai làm sai chi phí/km | `Chạy`, `Suy` |
| Start Date giả | Lưu khi ô chữ xám | "can't be blank" | `Chạy` |

### 13.6 Bảo hành

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| Tạo | `TEST-XE-01`, 01/10/2026, 1 Years, 50000, mã 013 | "Warranties have been successfully created", Status "Active", End Date 10/01/2027 (giao diện ghi tháng trước) | `Chạy`, `images/warranty-list.jpg` |
| End Meter | Start 1 km + 50,000 km | 50,001 km | `Chạy` |
| Nhập 1000 hiện 1 km | Start Meter | Chưa rõ nguyên nhân | `Chạy` |
| Mẫu | Xe không Make, Model | "No options" | `Chạy`, `images/warranty-new-template.jpg` |
| Mã hệ thống | Nhập 000, 000-001, 013 | Nhận; 013 ra "013 - Brakes" | `Chạy`, `images/warranty-maintenance-codes.jpg` |
| Lệnh có phụ tùng phanh, không có task | Lệnh #100 | KHÔNG gợi ý: "No vehicle warranty opportunities to show.", "No part warranty opportunities to show." | `Chạy`, `images/wo-warranty-before.jpg` |
| Thêm task khớp mã | "Brake Inspection" | "Warranty Opportunities (1)", "View Active Coverage" | `Chạy`, `images/wo-warranty-opportunity.jpg` |
| Claim | Nút claim | Chưa thử | Không chạy |

### 13.7 Phân tích thay xe

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| Chọn xe | Mở trang | KHÔNG có ô chọn xe | `Chạy` |
| Dữ liệu thật | `TEST-XE-LOP` đã có chi phí | Trang KHÔNG đổi | `Chạy` |
| Mốc | Tham số mặc định | Optimal Replacement năm 7, Estimated Replacement năm 8 | `Chạy` |
| Năm 1 | Tính tay | Nhiên liệu 0,2352 + bảo dưỡng 0,075 + khấu hao 0,625 = 0,935/km, khớp biểu đồ | `Chạy` |
| Tiền | Đơn vị | Ghi ₫ nhưng số mặc định kiểu đô la (Purchase Price 50000) | `Chạy` |
| Lưu | Tìm nút | KHÔNG có nút Lưu; không đổi số nên chưa biết có tự lưu | `Chạy` |
| Tham số trên xe | Form xe tab Lifecycle | Trang này không dùng theo những gì thấy | `Chạy` |

### 13.8 Trạng thái, Archive, quyền

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| Danh mục | Settings › Vehicle Statuses | Active 22, In Shop 2, Inactive 1, Out of Service 0, Sold 0 lúc đọc | `Xem` |
| Đổi trạng thái | `TEST-XE-LOP` qua form: Out of Service, Sold, In Shop, Sold, Inactive | Đổi tự do, "Vehicle was successfully updated", KHÔNG hỏi lý do | `Chạy`, `images/vehicle-status-history.jpg` |
| Xe Out of Service | Add Vehicle Assignment, nhập đồng hồ | Lưu được, KHÔNG cảnh báo; menu Add đủ mục | `Chạy` |
| Xe Sold | Tạo Lệnh sửa, nhập đồng hồ | Lưu được, KHÔNG cảnh báo; liên kết mooc còn nguyên | `Chạy` |
| Xe In Shop | Lưu trạng thái | KHÔNG tự sinh Lệnh; liên kết còn nguyên | `Chạy` |
| Xe Inactive | Thêm đồng hồ phụ, phân công | Lưu được | `Chạy` |
| Mở, đóng Lệnh | Không có automation | KHÔNG đổi trạng thái xe, xe Sold vẫn Sold | `Chạy` |
| Status Updates | Sau mỗi lần đổi | Dạng "{người dùng} updated status from Sold to Inactive", ngày giờ, thời lượng | `Chạy` |
| Thời lượng trong Status Updates | So ngày giờ các dòng trên ảnh | Khớp thời gian ở trạng thái đích tính tới lần đổi kế tiếp; run-notes ghi "trạng thái trước" (OQ-21) | `Suy` |
| Lưu In Shop kèm nhóm Sample | Một lần | Cả form bị từ chối, xe vẫn Sold, No Group | `Chạy` |
| Automation đổi ngược | Bật `TEST-NEN-AUTO-05` | Người đổi về Active lưu được, khoảng 1 giây sau automation đổi lại, màn KHÔNG báo. Chi tiết ở nhóm Nền tảng | `Chạy` |
| Quyền Archive | Role Operator | Operator không có `vehicles_archive_delete`, có `vehicles_update_status` | `Xem` |
| Require Group | Settings | Khoá vì "all existing assets and contacts must be assigned a group" | `Xem` |
| Recall | 261 dòng Sample | Chỉ đọc, không đổi trạng thái | `Xem`, `images/recalls-list.jpg` |
| Motor Pool | Rỗng | Không chạy | `Xem`, `images/motor-pool-reservations.jpg` |

### 13.9 Đồng hồ phụ, giải mã VIN

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| Bật đồng hồ phụ | Settings, tick "Add Secondary Meter", Hours, Current Reading 50 | Đầu trang 2 số (4.928 km, 50 hr), Overview thêm "Secondary Meter" | `Chạy` |
| Nhập chỉ số phụ | Secondary 60, Primary trống | Lưu được; Meter Type "Secondary", "Current hours", chuỗi riêng | `Chạy`, `images/meter-bulk-void-secondary.jpg` |
| Hộp nhập khi có 2 đồng hồ | Add Meter Entry | 2 ô, mỗi ô Void riêng, "Last updated" riêng | `Chạy` |
| VIN ngắn | `ABC123` | Decode khoá, KHÔNG có câu giải thích khi rê chuột | `Chạy` |
| VIN 17 ký tự | VIN ví dụ công khai | "Decoding VIN...", hộp "Add New Vehicle Data" | `Chạy`, `images/vin-decode-review.jpg` |
| Dòng Different | Vehicle Type Semi Truck với Car | KHÔNG tick sẵn | `Chạy` |
| Dòng New | Fuel Type, Year, Make, Model, Trim, Body Type, MSRP, EPA, động cơ, hộp số, bánh | Tick sẵn | `Chạy` |
| Save Data to Vehicle | Bấm trong hộp | Chỉ điền vào form, xe chưa đổi tới khi Save Vehicle: "We've successfully decoded your VIN and have downloaded the vehicle specifications." | `Chạy` |
| Thoát form có thay đổi | Không lưu | Tab kẹt hộp rời trang, phải mở tab mới | `Chạy` |

### 13.10 Archive, Restore

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| Hộp xác nhận | Bấm Archive | "Confirm Vehicle Archive": báo trước ngắt liên kết, đóng phân công đang chạy, xoá phân công tương lai; 2 câu chặn Lệnh chưa xong, Motor Pool đang đặt | `Chạy`, `images/vehicle-archive-confirm.jpg` |
| Archive khi có Lệnh Open | Thử 2 lần | "Vehicle could not be archived." KHÔNG nêu lý do, xe không Archive | `Chạy` |
| Archive bị từ chối, liên kết | Lệnh mở, có mooc | Liên kết VẪN mất ở cả hai phía, 2/2 lần; KHÔNG có dòng lịch sử | `Chạy` |
| Archive bị từ chối, phân công | Có phân công tương lai | Phân công tương lai còn nguyên | `Chạy` |
| Đối chứng | Nối lại, lưu Sold, In Shop | Liên kết còn; chỉ lần Archive bị từ chối mới làm mất | `Chạy` |
| Đóng Lệnh để Archive | Lệnh #108, #109 | Đòi Started At, Starting Meter Entry, Odometer; đóng được; tự sinh Service Entry | `Chạy` |
| Start Odometer khi đóng Lệnh | 4.928, Actual Start 12:28am | "must be less than 100 or marked as void"; nhập 90 thì qua, dòng ghi ngày 11/02 | `Chạy`, `images/meter-bulk-void-secondary.jpg` |
| Archive thành công, liên kết | Có mooc | Liên kết mất | `Chạy` |
| Archive thành công, phân công đang chạy | Kết thúc dự kiến 10/11 | Bị đóng ngay, End đổi thành lúc Archive, Duration 1m | `Chạy` |
| Archive thành công, phân công tương lai | Ngày 20/11 | Xoá hẳn, KHÔNG còn dòng nào; phân công 05/11, 10/11 của lượt trước cũng mất theo cách này | `Chạy` |
| Sau Archive, lịch sử liên hệ | `TEST-LAI-XE-02` | Dòng đã đóng có nhãn "Archived"; cột Start Meter trống | `Chạy` |
| Sau Archive, lịch phân công | Lịch | Xe rời khỏi lịch | `Chạy` |
| Archive, trường Status | Xe Archived | KHÔNG đổi, vẫn hiện Active hoặc Inactive | `Chạy` |
| Archive, Record History | Xem | Chỉ "Archived At changed from … to …"; KHÔNG ghi ngắt liên kết, KHÔNG ghi đổi đồng hồ | `Chạy` |
| Xe Archived, lốp, đồng hồ | Xem | Cấu hình trục, đồng hồ vẫn xem được, Edit trục khoá | `Chạy` |
| Restore | Bấm | Chạy ngay, KHÔNG hỏi, "Record successfully restored!" | `Chạy` |
| Sau Restore | Xem xe | Trạng thái, đồng hồ, cấu hình trục giữ nguyên; liên kết, phân công đã mất KHÔNG quay lại | `Chạy` |
| Restore khi đầy gói | 5 of 5 | Nút khoá, bấm không có gì, KHÔNG có câu giải thích | `Chạy` |
| Motor Pool chặn Archive | Chưa tạo đặt xe | Chỉ có câu trong hộp | `Xem` |

### 13.11 Overview, More Actions, nhóm xe

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| Tìm trường | Gõ "tire" | Còn nhóm Specifications, "4 results for "tire"", "Clear search" | `Chạy` |
| Ẩn thẻ | Bỏ tick Recalls, Apply | Thẻ mất ở trang xe | `Chạy`, `images/vehicle-manage-overview-layout.jpg` |
| Restore defaults | Apply | Thẻ Recalls hiện lại | `Chạy` |
| Kéo đổi thứ tự thẻ, Manage Tab Menu | | Chưa thử | Không chạy |
| Customize Layout | Đọc, không sửa | Settings › Standard Records › Vehicle › Layout, "System Default", 4 Sections, 104 Fields, All (25), Add Layout | `Xem` |
| Edit Vehicle Settings | More Actions | Mở thẳng phần Settings của form | `Chạy` |
| Manage Inspection Forms | More Actions | Thẻ từng biểu mẫu nhãn "Disabled", menu "…", "View Submissions" | `Chạy` |
| Manage Integration Links | | Chưa mở, là tích hợp | Không chạy |
| Manage Service Programs, xe chưa có bộ lịch | `TEST-DAUKEO-2` | Trang rỗng dạng quảng bá, nút "Create Service Program"; KHÔNG có nút gán bộ lịch sẵn có | `Chạy`, `images/vehicle-service-programs-empty.jpg` |
| Attach Shared Document, chưa chọn | Mở hộp | Nút Attach khoá; ô chỉ liệt kê tài liệu dùng chung | `Chạy`, `images/vehicle-attach-shared-document.jpg` |
| Attach Shared Document, đã chọn | Tài liệu có sẵn | "Successfully attached shared document to vehicle.", panel có thẻ nhãn "Shared" | `Chạy` |
| Huy hiệu Documents | Trước và sau khi đính | Trước có "(1)" mà panel chưa có tài liệu của xe; sau có 1 thẻ, huy hiệu tắt; chưa rõ đếm gì | `Chạy` |
| Menu More Actions, lượt 4 | `TEST-DAUKEO-2` | Đủ 8 mục, có Recalculate Fuel Entries | `Chạy` |
| Add Multiple khi gói đầy | Menu "...", 5 of 5 | Mục xám có khoá, bấm không mở form, không điều hướng; KHÔNG vào thẳng URL | `Chạy` |
| Import Vehicles, Import Meter Entries khi gói đầy | Menu "..." | Không khoá, chưa bấm | `Xem` |
| Đồng hồ phụ trên xe đang có số | `TEST-DAUKEO-2` 2.199 km | Mặc định Hours, "Secondary Meter 0 hr", đầu trang 2 số | `Chạy` |
| Sửa layout tài khoản, tạo Group, Export Data | Lượt 4 | Không làm: Settings, danh mục dùng chung, xuất dữ liệu | Không chạy |
| Archive khi có đặt Motor Pool, số GPS khi đổi đồng hồ | Lượt 4 | Vẫn chặn: phải tạo Motor Pool trong Settings, cần tích hợp GPS | Không chạy |
| Menu Add theo nhiên liệu | Xe Gasoline, xe chưa có Fuel Type | Gasoline ẩn "Add Charging Entry"; chưa có Fuel Type thì có | `Chạy` |
| Recalculate Fuel Entries, lượt 3 | 2 xe TEST không có Fuel Entry | KHÔNG có trong menu; lượt 4 thấy trên xe khác, xem OQ-20 | `Chạy` |
| Chọn nhóm Sample | Georgia / Atlanta cho `TEST-DAUKEO-2` | "Selected group is a sample, and cannot be used with non-sample records.", "Vehicle could not be updated"; dấu đỏ ở mục Details dù đang đứng ở Lifecycle | `Chạy` |
| Tìm nhóm chưa có | Gõ "TEST" | Chỉ có "Create "TEST"", không bấm | `Chạy` |
| Gán nhóm thật, lịch sử đổi nhóm | Không có nhóm ngoài Sample | Chưa chạy | Không chạy |

## Phát hiện lượt 3 (03/11)

- Archive bị từ chối vì còn lệnh mở (toast "Vehicle could not be archived.") vẫn ngắt liên kết với mooc ở cả hai phía, không ghi lịch sử; lặp lại 2/2 lần.
- Archive thành công: liên kết mất, phân công đang chạy bị đóng ngay, phân công tương lai bị xoá hẳn; Restore không trả lại gì. Restore bị khoá khi gói xe đầy.
- Trùng tên, trùng VIN báo "has already been taken", xét cả xe Sample; tên của xe đã Archive dùng lại được.
- Void toàn bộ đồng hồ: xe về 0 km, nhận số mới bất kỳ. Chưa khẳng định đây là Bulk Meter Management trong tài liệu hãng.
- Xe Sold, Out of Service vẫn gán tài xế (thử khi Out of Service), mở lệnh (thử khi Sold), nhập đồng hồ; không cảnh báo.
- Out of Sequence có thật: phiếu Fleetio Go được lưu rồi tự Void, cùng tình huống nhập tay trên web bị chặn ở trường. Một ca.
- Một mooc nối được nhiều xe, không ngày hiệu lực, không kiểm loại xe.
- Lỗi Add Multiple chỉ gửi qua email; Restore khoá khi đầy gói không có lý do.

Đã đưa vào: FR-fleetio-vehicle-002, 008, 014, 016, 020, 021, 047 đến 052; BR-fleetio-vehicle-024 đến 038; E-fleetio-vehicle-019 đến 031; Mục 13.

## Phát hiện lượt 4 (03/11)

- Manage Service Programs chỉ có trang quảng bá khi xe chưa có bộ lịch, không gán được bộ lịch sẵn có từ tab xe.
- Attach Shared Document chạy được, tài liệu mang nhãn "Shared".
- Add Multiple khoá ngay từ menu khi gói đầy; dán nhiều dòng vẫn chưa chạy. Motor Pool chặn Archive, số GPS, Group mới, layout tài khoản vẫn bị chặn.

Đã đưa vào: FR-fleetio-vehicle-002, 022, 044, 053, 054; BR-fleetio-vehicle-039, 040; E-fleetio-vehicle-032; OQ-19, 20, 22; Mục 13.11.
