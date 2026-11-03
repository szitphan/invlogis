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

**Phép thử chính:** chạy ngày 02/11/2026 trên `TEST-XE-01`; chạy ngày 03/11/2026 trên `TEST-XE-LOP` (Semi Truck, đồng hồ đầu 5.000 km) và `TEST-MOOC-LOP` (Trailer).

## 1. Scope

**Trong phạm vi:** Vehicle (form, trang xe, trạng thái, Archive, hạn mức), mooc dưới dạng Vehicle riêng và Linked Vehicles, Vehicle Assignment, Meter Entry, Expense Entry, Cost of Ownership, Warranty và Warranty Opportunities, Replacement Analysis, Recall và Motor Pool ở mức đọc.

**Lốp:** sơ đồ trục, lắp, đảo, tháo, đọc gai nằm ở [[docs/_research/fleetio/srs/fleetio-tires-spec.md|SRS Lốp]]; nhóm này chỉ giữ FR-fleetio-vehicle-017 trỏ sang.

**Ngoài phạm vi:** tổ hợp đầu kéo, mooc, container; Fleetio không có đối tượng này (`Chạy`), Invlogis giữ theo `transport-dispatch` và `vehicle-management`. Bán, thanh lý xe chỉ là trường dữ liệu (Out-of-Service Date, Out-of-Service Odometer) và trạng thái Sold, không thấy nút hay luồng thanh lý (`Xem`).

## 2. Actors & Stakeholders

| Actor | Loại | Mục tiêu | Trong scope? | Tương đương Invlogis |
|---|---|---|---|---|
| Fleet Manager | Người | Quản lý hồ sơ, gán xe, bảo hành | Có | Quản lý phương tiện |
| Operator | Người | Được gán xe, báo số km | Có | Lái xe |
| Kế toán, Lãnh đạo | Người | Xem chi phí, phân tích thay xe | Có | Kế toán, Lãnh đạo |
| Kỹ thuật viên | Người | Thấy cơ hội bảo hành trên lệnh | Có | Kỹ thuật xưởng |
| Telematics, API | Ngoài | Đẩy số km; có thể là nguồn của lý do Out of Sequence (`Suy`) | Có | EUP |
| Automation | Hệ thống | Đổi trạng thái xe theo mẫu | Có, chi tiết ở nhóm Nền tảng | — |

## 3. Functional Requirements (FR)

| ID | Title | Description | Priority | Tầng | Verify by | Mức | Source | Đề xuất Invlogis |
|---|---|---|---|---|---|---|---|---|
| FR-fleetio-vehicle-001 | Tạo xe | Form 6 phần: Details (Identification, Classification, Additional Details), Maintenance (Service Program hoặc None), Lifecycle, Financial, Specifications (Dimensions, Weight, Performance, Fuel Economy, Engine 15 trường, Transmission 4, Wheels & Tires 11, Fuel, Oil Capacity), Settings (Primary Meter, Current Reading, Average Usage per Day, Add Secondary Meter, Fuel Unit, Measurement Units). Nút Cancel, Add Multiple Vehicles, Save & Add Another, Save Vehicle. | P0 | [Lõi] | demo | `Chạy` | Tạo `TEST-XE-LOP`, `TEST-MOOC-LOP`; đọc đủ trường ở `TEST-NEN-01` | Lấy cách chia phần, rút trường theo xe Việt Nam |
| FR-fleetio-vehicle-002 | Tạo nhiều xe | Add Multiple Vehicles từ form. | P1 | [Cấu hình] | demo | `Xem` | Thấy nút, không bấm vì đó là lách hạn mức gói | Lấy cho khởi tạo khách |
| FR-fleetio-vehicle-003 | Trang xe trung tâm | Đầu trang: số km, trạng thái, nhóm, người lái; tab Overview cùng khoảng 19 lịch sử; cột phải bình luận, ảnh, tài liệu; khối Linked Assets, Cost of Ownership. | P0 | [Lõi] | demo | `Chạy` | Trang `TEST-XE-01`, `TEST-XE-LOP` | Lấy, rút gọn trên mobile |
| FR-fleetio-vehicle-004 | Tạo bản ghi từ xe | Nút Add: Draft Work Order, Assignment, Fuel, Charging, Expense, Service Entry, Issue, Inspection, Work Order, Warranty, Service Reminder, Renewal, Meter. | P0 | [Lõi] | demo | `Chạy` | Đếm được 13 loại trên ảnh trang xe | Lấy |
| FR-fleetio-vehicle-005 | Overview có thể tuỳ biến | Khối Fields tìm được theo tên trường, có Customize Layout; các khối Last Known Location, Open Issues, Service Reminders và số đếm. | P1 | [Cấu hình] | demo | `Xem` | Trang xe | Lấy khối cần xử lý |
| FR-fleetio-vehicle-006 | Lịch sử trường | Status, Group có nút xem lịch sử đổi; menu có View Record History. | P1 | [Lõi] | demo | `Xem` | Trang xe, More Actions | Lấy |
| FR-fleetio-vehicle-007 | Giải mã số khung | Nút Decode cạnh VIN/SN điền thông số, gồm dung tích bình. | P2 | [Cấu hình] | demo | `Xem`, `Docs` | Form xe | Kiểm với xe Việt Nam |
| FR-fleetio-vehicle-008 | Liên kết xe | Linked Vehicles là trường chọn trong form sửa xe; kết quả hiện hai chiều ở khối "Linked Assets" › "Link Asset" › "VEHICLES" trên cả hai xe; gỡ, gắn lại từ một trong hai phía. Không có ngày, không có lịch sử ghép, không truyền số km, không gộp lốp. | P1 | [Lõi] | test | `Chạy` | `run-notes/vehicle.md`, `run-notes/tires.md` | Không đủ thay ghép tách mooc |
| FR-fleetio-vehicle-009 | Gán xe | Assigned Vehicle, Operator, Start Date/Time ("Leave blank if assignment has always existed."), End Date/Time ("Can be past or future."), comment; chọn đủ xe và người thì hiện thêm Starting Odometer, Ending Odometer; hộp Edit gợi ý Starting Odometer theo đồng hồ hiện tại. | P0 | [Lõi] | test | `Chạy` | Phân công 05/11 đến 07/11, 10/11 đến 12/11 | Lấy cho bàn giao, thu hồi |
| FR-fleetio-vehicle-010 | Chặn trùng gán | Không cho hai lần gán chồng thời gian trên **một xe**; không tự đóng phân công cũ. Không xét trùng theo người (BR-fleetio-vehicle-007). | P0 | [Lõi] | test | `Chạy` | E-fleetio-vehicle-001 | Lấy theo xe, thêm cảnh báo theo người |
| FR-fleetio-vehicle-011 | Chỉ Operator được gán | Ô chọn chỉ hiện liên hệ phân loại Operator ("Allow this Contact to be assigned to assets"); liên hệ khác bị chặn bằng câu dẫn trên trang liên hệ; có ngoại lệ từ workflow biểu mẫu. | P1 | [Lõi] | test | `Chạy`, `Docs` | `TEST-NEN-LH-01`; ngoại lệ là `Docs` | Lấy |
| FR-fleetio-vehicle-012 | Lịch gán | Mỗi xe một hàng, xem Day hoặc Week, thanh màu cam là tương lai, xanh là đang chạy, lịch tháng bên phải, gom theo xe hoặc người. | P1 | [Lõi] | demo | `Chạy` | Lịch tuần; gom theo người là `Xem` | Làm mẫu cho `transport-dispatch` |
| FR-fleetio-vehicle-013 | Sổ đồng hồ | Mỗi dòng có ngày, giá trị, loại Primary hoặc Secondary, Void, Source, Void Status, Auto-Void Reason; hiện số hiện tại và khoảng cách với hiện tại ("200 km ago"); lọc Void Status: All Voided, Manually Voided, Auto Voided, Not Voided. | P0 | [Lõi] | test | `Chạy` | 7 dòng trên `TEST-XE-01`, 5 dòng trên `TEST-XE-LOP` | Lấy |
| FR-fleetio-vehicle-014 | Tự huỷ số sai | Số vượt mức tối đa một ngày: lưu nhưng tự Void, lý do Exceeds Max. Daily Usage, popup có Last Meter Entry, Daily Usage, Max Daily Usage, Exceeds By, nút "Unvoid this Entry". Lý do Out of Sequence có trong tài liệu hãng, không tái hiện được khi nhập tay trên web. | P0 | [Lõi] [Cấu hình] | test | `Chạy`, `Docs` | Exceeds Max là `Chạy`; Out of Sequence là `Docs` | Lấy, ngưỡng là tham số mới, chưa có mã |
| FR-fleetio-vehicle-015 | Sửa xung đột | Dòng gây xung đột gắn cờ đỏ, Void Status "Conflict Source", popup "Conflicting Meter Entry" có số dòng ảnh hưởng và chênh lệch. Unvoid dòng con thì cờ tự mất. Theo tài liệu hãng: Void dòng gốc rồi bỏ Void từng dòng, không tự động. | P1 | [Lõi] | test | `Chạy`, `Docs` | Cờ và Unvoid là `Chạy`; Void dòng gốc là `Docs` | Lấy, nên tự bỏ Void, bắt buộc lý do |
| FR-fleetio-vehicle-016 | Đổi đồng hồ | Bulk Meter Management Void toàn bộ số của xe khi thay đồng hồ, kể cả số GPS. | P1 | [Lõi] | test | `Docs` | Chưa chạy | Lấy |
| FR-fleetio-vehicle-017 | Đọc lốp, quản lý lốp | Trục, lắp, đảo, tháo, đọc gai theo từng xe: xem [[docs/_research/fleetio/srs/fleetio-tires-spec.md|SRS Lốp]]. | P2 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` | `run-notes/vehicle.md`, `run-notes/tires.md` | Xem `fleetio-tires` |
| FR-fleetio-vehicle-018 | Chi phí khác | Vehicle, Expense Type (17 loại có sẵn), Vendor, Amount, Frequency: "Single Expense" hoặc "Recurring Expense" ("Repeats on a monthly or annual basis"), Notes; Recurring thêm Start Date, End Date, Frequency. Tab Past, Future. Tự sinh khoản vay, thuê mua nếu bật Auto Generate Loan / Lease Expenses. | P1 | [Cấu hình] | test | `Chạy` | Insurance định kỳ, Tolls đơn lẻ; tự sinh vay là `Xem` | Vẫn lấy `cost-catalog` làm gốc |
| FR-fleetio-vehicle-019 | Phân tích thay xe | Máy tính ước lượng **cấp tài khoản**: không có ô chọn xe, không đọc dữ liệu xe nào. Biểu đồ chi phí trên km theo tuổi xe từ giả định nhập tay: tuổi thọ, số km năm, tiêu hao, giá mua, thanh lý, phương pháp khấu hao, dịch vụ và nhiên liệu từng năm; chỉ ra Optimal Replacement, Estimated Replacement. | P2 | [Gói: Bảo dưỡng đội xe] | phân tích | `Chạy` | Chỉ đọc, không đổi số | Để sau; nếu làm thì đọc số thật của từng xe |
| FR-fleetio-vehicle-020 | Trạng thái xe | Status bắt buộc, mặc định Active. Danh mục 5 trạng thái có đếm xe, Add Vehicle Status. Đổi tự do qua trường hoặc automation, không thấy luật chuyển. Báo cáo Status Changes, Status Summary. | P0 | [Lõi] [Cấu hình] | test | `Xem` | Settings › Vehicle Statuses; không đổi vì xe thuộc nhóm khác | Khung trạng thái lõi, nhãn cấu hình |
| FR-fleetio-vehicle-021 | Archive xe | Nút Archive trong More Actions, đưa xe sang tab Archived; quyền `vehicles_archive_delete`. Restore chưa kiểm trên xe. | P1 | [Lõi] | test | `Xem` | Chưa bấm | Lấy, nêu rõ dữ liệu liên quan còn hay không |
| FR-fleetio-vehicle-022 | More Actions trên xe | Edit Vehicle Settings, Manage Inspection Forms, Manage Service Programs, Manage Integration Links, Attach Shared Document, Recalculate Fuel Entries, View Record History, Archive. | P1 | [Lõi] | demo | `Xem` | `images/vehicle-more-actions.jpg` | Lấy nhóm thao tác cấp xe |
| FR-fleetio-vehicle-023 | Hạn mức xe theo gói | Danh sách hiện "5 of 5", nút Add Vehicle có khoá; Save bị chặn. Account Usage đếm Vehicles. Xe Sample không tính. Quyền Create cảnh báo "Adding new Vehicles will result in additional charges to your account's subscription." | P1 | [Cấu hình] | test | `Chạy` | E-fleetio-vehicle-009 | Hạn mức là tham số mới, chưa có mã |
| FR-fleetio-vehicle-024 | Loại xe | Type bắt buộc, mặc định Car; Settings › Vehicle Types 25 loại. Loại xe được dùng ở Excluded Vehicle Types của Require a Meter Reading. | P1 | [Cấu hình] | demo | `Xem` | Settings | Danh mục theo khách |
| FR-fleetio-vehicle-025 | Nhóm xe | Group dạng cây nhiều cấp; "Require Group" bị khoá khi còn tài sản, liên hệ chưa có nhóm; Export Data. | P1 | [Lõi] [Cấu hình] | demo | `Xem` | Settings › Groups & Subgroups | Khớp Chi nhánh, xem nhóm Nền tảng |
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
| FR-fleetio-vehicle-044 | Đồng hồ phụ | Add Secondary Meter trong Settings của form xe; Primary Meter chỉ Miles, Kilometers, Hours, không bỏ được. | P1 | [Cấu hình] | demo | `Xem` | Form xe | Hợp máy phát điện, xe nâng; mooc cần chế độ không đồng hồ |
| FR-fleetio-vehicle-045 | Automation đổi trạng thái xe | Mẫu: In Shop khi sự cố từ kiểm tra; Active khi sự cố Resolved; đổi trạng thái khi tạo lệnh; Active khi lệnh Completed và Vehicle Incomplete Work Orders Count < 1. | P1 | [Cấu hình] | test | `Xem` | Đọc mẫu, không chạy vì sẽ sửa xe nhóm khác | Lấy dạng công tắc theo khách |
| FR-fleetio-vehicle-046 | Bắt buộc số đồng hồ theo loại xe | Maintenance Settings: Require a Meter Reading + Excluded Vehicle Types, "This requirement only applies to future Work Orders or Service Entries." | P1 | [Cấu hình] | demo | `Xem` | Settings, chỉ đọc | Mẫu cho loại xe không đồng hồ như mooc |

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
| BR-fleetio-vehicle-003 | Ô số km đầu, cuối hiện khi đã chọn đủ xe và người. Bản 02/11 ghi ô mở theo ngày; chưa thử riêng nên chưa loại trừ thêm ràng buộc theo ngày (OQ-12). | [Lõi] | Nhập form | FR-fleetio-vehicle-009 | `Chạy` | Sửa theo chạy 03/11 |
| BR-fleetio-vehicle-004 | Số hiện tại là số lớn nhất không bị Void. | [Lõi] | Lưu số km | FR-fleetio-vehicle-013 | `Chạy` | 5.300 sau 5.500 giữ 5.500; Void không tính; Unvoid 20.000 thành hiện tại |
| BR-fleetio-vehicle-005 | Số làm mức dùng một ngày vượt tối đa thì lưu và tự Void. Fleetio: 4.828 km một ngày; theo tài liệu hãng còn 3.000 dặm, 24 giờ. Invlogis: tham số mới, chưa có mã. | [Lõi] [Cấu hình] | Lưu số km | FR-fleetio-vehicle-014 | `Chạy`, `Docs` | Nhập 20.000 khi đang 5.500. Số 4.828 là `Chạy`; dặm, giờ là `Docs` |
| BR-fleetio-vehicle-006 | Giá trị cao có cảnh báo, bỏ qua được; quá cao phải sửa hoặc Void. | [Lõi] | Nhập trên app | FR-fleetio-vehicle-014 | `Docs` | Chưa có số; trên web chỉ thấy tự Void |
| BR-fleetio-vehicle-007 | Trùng gán chỉ xét theo xe. Một người được giữ nhiều xe cùng lúc, kể cả đang có phân công "No end date". | [Lõi] | Lưu gán | FR-fleetio-vehicle-010 | `Chạy` | `TEST-LAI-XE` giữ `TEST-XE-01` và `TEST-XE-LOP` |
| BR-fleetio-vehicle-008 | Gán mới chồng phân công cũ thì từ chối, không tự đóng phân công cũ. | [Lõi] | Lưu gán | FR-fleetio-vehicle-010 | `Chạy` | E-fleetio-vehicle-001 |
| BR-fleetio-vehicle-009 | Khi sửa phân công, xe khoá, Operator đổi được; bản ghi giữ nguyên mã. | [Lõi] | Sửa gán | FR-fleetio-vehicle-028 | `Chạy` | #12480917 |
| BR-fleetio-vehicle-010 | Số đồng hồ ngày cũ phải nhỏ hơn số ngày sau; số ngày mới phải lớn hơn số ngày trước; sai thì từ chối trừ khi tick Void. Lệch thứ tự theo ngày không tự Void. | [Lõi] | Lưu số km, phiếu dầu | FR-fleetio-vehicle-032 | `Chạy` | E-fleetio-vehicle-004, 005, 008 |
| BR-fleetio-vehicle-011 | Cùng ngày, số nhỏ hơn được lưu, không Void, không báo, không đổi số hiện tại. | [Lõi] | Lưu số km | FR-fleetio-vehicle-013 | `Chạy` | 5.300 sau 5.500; `TEST-XE-01` 900 sau 1.010; cùng hành vi ở Service Entry, Fuel Entry theo nhóm Sửa chữa, Kho |
| BR-fleetio-vehicle-012 | Dòng Void không bao giờ là số hiện tại, không kích hoạt nhắc bảo dưỡng hay thứ gì dựa trên số hiện tại. | [Lõi] | Tính số hiện tại | FR-fleetio-vehicle-030 | `Chạy` | Tooltip nguyên văn; 5.800 Manually Voided không đổi đồng hồ |
| BR-fleetio-vehicle-013 | Dòng làm dòng sau bị tự Void được gắn Conflict Source; hết xung đột thì cờ tự mất. | [Lõi] | Tự Void, Unvoid | FR-fleetio-vehicle-015 | `Chạy` | Dòng 5.500 |
| BR-fleetio-vehicle-014 | Unvoid không hỏi lý do, không kiểm lại mức tối đa; dòng được Unvoid thành số hiện tại ngay. | [Lõi] | Unvoid | FR-fleetio-vehicle-031 | `Chạy` | 5.500 lên 20.000 |
| BR-fleetio-vehicle-015 | Chi phí định kỳ sinh sẵn theo kỳ từ Start đến End. Cost of Ownership chỉ tính dòng đã đến ngày. | [Cấu hình] | Lưu chi phí | FR-fleetio-vehicle-033 | `Chạy` | Dòng 03/11 tính; 03/12, 03/01 chưa tính |
| BR-fleetio-vehicle-016 | Cost Per Meter = tổng chi phí chia km đã chạy trong kỳ, nên số đồng hồ sai làm sai chi phí/km. | [Lõi] | Xem Cost of Ownership | FR-fleetio-vehicle-034 | `Chạy`, `Suy` | 3.500.000 / 15.000 = 233 ₫/km; hệ quả là `Suy` |
| BR-fleetio-vehicle-017 | End Date = Start Date + Coverage Duration; End Meter = Start Meter + Coverage Distance. | [Lõi] | Lưu bảo hành | FR-fleetio-vehicle-036 | `Chạy` | Kiểm chứng trên `TEST-XE-01` |
| BR-fleetio-vehicle-018 | Cơ hội bảo hành xuất hiện khi Service Task trên lệnh có cùng mã bảo dưỡng với coverage còn hiệu lực. Phụ tùng đứng riêng không gợi ý. | [Gói: Bảo dưỡng đội xe] | Lưu lệnh | FR-fleetio-vehicle-038 | `Chạy` | Lệnh #100 |
| BR-fleetio-vehicle-019 | Liên kết xe không truyền số km, không gộp sơ đồ lốp; gỡ liên kết không đổi đồng hồ, lốp. | [Lõi] | Sửa xe | FR-fleetio-vehicle-008 | `Chạy` | `run-notes/vehicle.md`, `run-notes/tires.md` |
| BR-fleetio-vehicle-020 | Đổi trạng thái xe không có luật chuyển; đóng lệnh không tự đổi trạng thái nếu không có automation. | [Lõi] | Sửa xe | FR-fleetio-vehicle-020 | `Xem` | Không đổi thử trạng thái thật ở lượt 03/11 |
| BR-fleetio-vehicle-021 | Hạn mức xe chỉ đếm xe thật, xe Sample không tính. Hết hạn mức thì chặn cả khi dữ liệu hợp lệ. | [Cấu hình] | Lưu xe | FR-fleetio-vehicle-023 | `Chạy` | Fleetio: gói dùng thử 5 xe. Invlogis: tham số mới, chưa có mã |
| BR-fleetio-vehicle-022 | Chỉ liên hệ phân loại Operator mới gán được xe. | [Lõi] | Gán xe | FR-fleetio-vehicle-011 | `Chạy` | Câu dẫn trên trang liên hệ |
| BR-fleetio-vehicle-023 | Phân tích thay xe không đọc dữ liệu xe, tham số Lifecycle trên từng xe không ảnh hưởng theo những gì thấy. | [Gói: Bảo dưỡng đội xe] | Xem trang | FR-fleetio-vehicle-019 | `Chạy` | `TEST-XE-LOP` có chi phí nhưng trang không đổi |

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
| E-fleetio-vehicle-013 | Hộp nhập hiện số cũ | "Last updated: 5,000 km (Today)" khi xe đã 5.500 | minor | FR-fleetio-vehicle-013 | Thông tin gợi ý sai | Không nên học | `Chạy` |
| E-fleetio-vehicle-014 | Start Meter lệch khi hiển thị | Nhập 1000, danh sách bảo hành ghi 1 km, End Meter 50,001 km | major | FR-fleetio-vehicle-036 | Chưa rõ do ô nhập hay định dạng | OQ-10 | `Chạy` |
| E-fleetio-vehicle-015 | Unvoid nhầm ghim đồng hồ | Sau khi Unvoid 20.000 các số thật sẽ bị "must be greater than" | major | FR-fleetio-vehicle-031 | Đồng hồ xe 20.000 | Void lại dòng đó (`Suy`) | `Chạy`, `Suy` |
| E-fleetio-vehicle-016 | Không có mẫu bảo hành | Ô Coverage Template báo "No options" | minor | FR-fleetio-vehicle-039 | Ô chọn rỗng | Nhập tay Standard Warranty | `Chạy` |
| E-fleetio-vehicle-017 | Lệch múi giờ phân công | Ngày gửi đi theo múi giờ thiết bị trong khi tài khoản đặt America/Chicago | minor | FR-fleetio-vehicle-009 | Không có báo lỗi | OQ-13 | `Chạy` |
| E-fleetio-vehicle-018 | Dòng định kỳ đúng hôm nay ở tab Future | Tab Past trống sau khi lưu dù dòng 03/11 đúng hôm nay, còn Cost of Ownership đã tính dòng đó | minor | FR-fleetio-vehicle-033, FR-fleetio-vehicle-034 | Hai nơi nói khác nhau | Không nên học | `Chạy` |
| E-fleetio-vehicle-019 | Lý do Out of Sequence | Lý do tự Void trong tài liệu hãng; nhập tay trên web chỉ ra E-fleetio-vehicle-004, 005 | major | FR-fleetio-vehicle-014 | Chưa thấy dòng nào mang lý do này | OQ-8 | `Docs` |

## 7. Success Criteria

| ID | Outcome nghiệp vụ | Đo bằng | Mốc đạt |
|---|---|---|---|
| SC-fleetio-vehicle-01 | Mọi thứ của xe xem được một nơi | Số màn phải mở để xử lý | TBD |
| SC-fleetio-vehicle-02 | Biết ai giữ xe lúc nào | Không có khoảng trùng theo xe; người cũ còn trong lịch sử | 0 trùng; Fleetio chỉ đạt vế đầu |
| SC-fleetio-vehicle-03 | Số km tin cậy | Tỉ lệ dòng bị Void, dòng lùi | TBD |
| SC-fleetio-vehicle-04 | Chi phí/km đúng | Số dòng số km sai lọt vào phép tính | TBD |

## 8. Data Entities (tóm tắt — chi tiết ở erd.md)

Vehicle, Contact, Assignment, Meter Entry, Expense Entry, Warranty, Warranty Coverage Code, Recall, Motor Pool Reservation; Tire Reading thuộc nhóm Lốp. Xem [[docs/_research/fleetio/srs/fleetio-vehicle-erd.md|ERD]].

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
| `Chạy` Tài khoản dùng thử trần 5 xe, nên không chạy được bản ghi trùng tên xe, đổi trạng thái thật, Archive, Motor Pool | Cần một chỗ xe trống để kiểm |

## 12. Open Questions

* [x] OQ-1: Một xe nhiều người lái theo ca được không? — Trả lời (`Chạy`): theo Fleetio được, miễn các khoảng không chồng nhau trên xe; trùng theo người không bị chặn. Quyết định của Delta chuyển sang OQ-7. — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-2: GPS và đồng hồ lệch thì lấy số nào? Lượt chạy không có nguồn telematics. — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-3: Có đo gai lốp định kỳ không? Sự thật phía Fleetio đã ở `fleetio-tires`; phía Delta vẫn phải quyết định. — Nguồn khách: file sơ đồ lốp của Delta
* [x] OQ-4: Tab Tire Management chưa xem được vì xe chưa có lốp; cần cấu hình trục — Trả lời (`Chạy`): xem được; cấu hình trục khai ở tab này của từng xe, chi tiết ở `fleetio-tires`. — Nguồn khách: không áp dụng
* [x] OQ-5: "Out of Sequence" chính xác là gì? `Chạy` nhập 900 khi đang 1.010 cùng ngày không bị Void; ngưỡng "giá trị cao" chỉ áp trên app, chưa có số — Trả lời (`Chạy`): lệch thứ tự theo ngày bị từ chối ở trường, không Void; cùng ngày nhỏ hơn không bị gì; lý do Out of Sequence không tái hiện được trên web. Phần còn lại chuyển sang OQ-8, OQ-9. — Nguồn khách: không áp dụng
* [x] OQ-6: Số sai dưới ngưỡng ghim số hiện tại, hoặc Void toàn bộ thì xe không còn số hiện tại: xử lý thế nào? — Trả lời (`Chạy`): số sai dưới ngưỡng cùng ngày không ghim vì lấy số lớn nhất; số sai trên ngưỡng tự Void; Unvoid nhầm thì ghim số hiện tại. Trường hợp Void toàn bộ chưa chạy. — Nguồn khách: không áp dụng
* [ ] OQ-7: Delta có cho một xe nhiều người lái theo ca không, và có chặn một người giữ nhiều xe cùng lúc không? — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-8: Lý do Out of Sequence có chỉ xảy ra với nguồn không có người sửa (telematics, API) không? — Nguồn khách: không áp dụng
* [ ] OQ-9: Ngưỡng cảnh báo "giá trị cao" trên app là bao nhiêu? — Nguồn khách: không áp dụng
* [ ] OQ-10: Start Meter nhập 1000 mà hiện 1 km là do ô nhập hay định dạng? — Nguồn khách: không áp dụng
* [ ] OQ-11: Đổi trạng thái thật, Archive và Restore xe, bản ghi trùng tên xe, Motor Pool chạy ra sao? Cần một chỗ xe trống. — Nguồn khách: không áp dụng
* [ ] OQ-12: Ô Starting Odometer, Ending Odometer có thêm ràng buộc theo ngày không? Bản 02/11 và 03/11 ghi khác nhau. — Nguồn khách: không áp dụng
* [ ] OQ-13: Giờ phân công lưu theo múi giờ nào khi thiết bị và tài khoản khác nhau? — Nguồn khách: không áp dụng
* [ ] OQ-14: Sửa phân công đã qua, xoá phân công, nút claim bảo hành, Bulk Meter Management, điều kiện có Coverage Template chạy thế nào? — Nguồn khách: không áp dụng
* [ ] OQ-15: Replacement Analysis có tự lưu khi đổi số không? Công thức các năm sau, Sum of Years, Optimal Replacement tính thế nào? — Nguồn khách: không áp dụng
* [ ] OQ-16: Một mooc gắn được nhiều đầu kéo không? Không chạy do hết chỗ xe. — Nguồn khách: chưa có trong tài liệu khách gửi

## 13. Ma trận case

### 13.1 Tạo xe, hạn mức

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| Save rỗng | Form trống, đã hết hạn mức | "can't be blank" + "Your plan is limited to 5 vehicles" + toast "Vehicle could not be created" | `Chạy` |
| Có tên, hết hạn mức | Gõ `TEST-NEN-01`, Save | Vẫn "Your plan is limited to 5 vehicles" | `Chạy` |
| Lối phụ qua hạn mức | Add Multiple Vehicles, nhập tệp | Không thử vì đó là lách hạn mức gói | Không chạy |
| Xe Sample | 25 xe tính cả Sample, Usage "5 of 5" | Sample không tính vào hạn mức | `Chạy` |
| Mặc định form | Mở New Vehicle | Type Car, Status Active, Ownership Owned, Average Usage "Automatically calculate" | `Xem` |
| Trục trong form xe | Mở form Semi Truck | KHÔNG có trục; Wheels & Tires chỉ là trường chữ. Xem `fleetio-tires` | `Chạy` |
| Thanh lý | Tìm luồng bán, thanh lý | KHÔNG có nút; chỉ Out-of-Service Date, Odometer, trạng thái Sold | `Xem` |
| Đơn vị lẫn | Odometer phần Financial | Hiện "mi" trong khi Specifications hiện cm, kg, lít; chưa rõ lý do | `Xem` |
| Trùng tên xe | Tạo xe cùng tên | Không chạy được vì hạn mức | Không chạy |

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
| Một mooc nhiều đầu kéo | Ô chọn nhiều | Chưa biết | Không chạy |

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
| Out of Sequence | Mọi cách nhập tay | KHÔNG ra lý do này | `Chạy`; lý do là `Docs` |
| Void dòng gốc rồi Unvoid dòng con | | Chưa chạy | `Docs` |
| Bulk Meter Management | Thay đồng hồ | Chưa chạy | `Docs` |

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
| Đổi trạng thái | Xe thuộc nhóm khác | Không đổi; không thấy luật chuyển | `Xem` |
| Đóng lệnh | Không có automation | KHÔNG tự đổi trạng thái xe | `Xem` |
| Archive | Menu xe | Có nút, không bấm | `Xem`, `images/vehicle-more-actions.jpg` |
| Quyền Archive | Role Operator | Operator không có `vehicles_archive_delete`, có `vehicles_update_status` | `Xem` |
| Require Group | Settings | Khoá vì "all existing assets and contacts must be assigned a group" | `Xem` |
| Recall | 261 dòng Sample | Chỉ đọc, không đổi trạng thái | `Xem`, `images/recalls-list.jpg` |
| Motor Pool | Rỗng | Không chạy | `Xem`, `images/motor-pool-reservations.jpg` |
