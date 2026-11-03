# Ghi chú chạy thử — nhóm Phương tiện (2026-11-03)

Xe chạy thử: `TEST-XE-LOP` (id 5890753, Semi Truck, đồng hồ đầu 5.000 km).

## Sơ đồ lốp, cấu hình trục — Chạy
Các bước đã làm: Tạo xe `TEST-XE-LOP`, loại "Semi Truck". Xem hết form New Vehicle. Mở tab Tire Management, bấm "Set up axle configuration", đi cả 2 đường: trình hướng dẫn 3 bước và "I know my axle configuration". Lưu 6x4.
Kết quả thấy được:
- Form New Vehicle KHÔNG có trục. Mục Specifications › Wheels & Tires chỉ có trường chữ thông số (Drive Type, Rear Axle, Front/Rear Tire Type, Front/Rear Tire PSI...), không liên quan sơ đồ.
- Cấu hình trục khai ở tab Tire Management của từng xe. Chưa khai thì màn trống ghi "Set up this vehicle's axle configuration to begin managing tires."
- Trình hướng dẫn: "Asset Type" (Vehicle | Trailer) → "Wheel Positions" (4, 6, 8, 10) → "Axle Type" (vd 6 → 6x2, 6x4, 6x6). Xong "Vehicle's Axle Configuration successfully updated".
- Danh sách "I know my axle configuration" có đúng 27 dòng: 20 cho xe (4x2 FWD, 4x2 RWD, 4x2 RWD (Dually), 4x2 AWD, 4x2 AWD (Dually), 4x4, 4x4 (Dually), 6x2, 6x4, 6x6, 8x2, 8x4, 8x6, 8x8, 10x4, 10x6, 10x8, 10x10, 12x4, 12x6) và 7 cho mooc (Single Axle, Tandem Axle (2 Tires per Axle), Tandem Axle (4 Tires per Axle), Tri-Axle (2 Tires per Axle), Tri-Axle (4 Tires per Axle), Multi-Axle (2 Tires per Axle), Multi-Axle (4 Tires per Axle)).
- Không có dòng tự tạo cấu hình tuỳ biến trong danh sách. Chỉ đổi được vai trò từng trục qua menu trên sơ đồ: Steer, Drive, Dead, Lifted, Tag, Pusher, Other.
- 6x4 vẽ: Front Axle (LF, RF, đơn) + Axle 2 và Axle 3 (mỗi bên 2 lốp đôi: 2LO, 2LI, 2RI, 2RO, 3LO, 3LI, 3RI, 3RO) = 10 vị trí, cộng "Spare Tire" trong danh sách Position. Nhãn lại ghi "6 wheel positions, 4 driven": "wheel position" là đầu trục, không phải số lốp. Chưa thử 12x.
- Khoá cấu hình: có lốp rồi thì Edit bị khoá, tooltip "Axle Configuration cannot be edited for this Vehicle because it has installed Tires".
Bất ngờ, lỗi, điểm khác tài liệu hãng: Trình hướng dẫn chỉ cho 4, 6, 8, 10 vị trí, 12x4 và 12x6 chỉ có trong danh sách "I know". Đơn vị gai "/32 in" và áp suất "PSI" cố định dù xe đặt Metric.
Màn mới: tire-management-empty — ảnh images/tire-management-empty.jpg — hình minh hoạ, câu dẫn, nút "Set up axle configuration", ô Learn More. axle-setup-step1 — ảnh images/axle-setup-step1.jpg — 3 khối gập (Asset Type, Wheel Positions, Axle Type), Cancel, Continue, Save Axle Configuration. axle-config-options — images/axle-config-options.jpg, axle-setup-known.jpg — ô chọn có nhóm "VEHICLE AXLES". axle-setup-axle-type — images/axle-setup-axle-type.jpg. tire-management-6x4 — images/tire-management-6x4.jpg — trái: sơ đồ, mỗi vị trí trống nút +, menu vai trò trục; phải: "Installed Tires" nút ... (Rotate Tires, Remove All) và Add.
Trả lời câu hỏi mở nào: OQ-4 nhóm Phương tiện (tab Tire Management xem được, cấu hình trục ở từng xe).
Dữ liệu TEST đã tạo: xe `TEST-XE-LOP`.

## Đầu kéo và mooc — Chạy
Các bước đã làm: Tạo `TEST-MOOC-LOP` loại Trailer. Tab Tire Management → Asset Type "Trailer" → nhảy thẳng sang ô "Axle Configuration" chỉ còn 7 dòng mooc → lưu "Tri-Axle (4 Tires per Axle)". Liên kết mooc vào đầu kéo qua trường "Linked Vehicles" trong form sửa xe.
Kết quả thấy được:
- Mooc là một Vehicle riêng: có đồng hồ riêng (lưu trống thành "0 km"), sơ đồ lốp riêng, lịch sử lốp riêng. Không có "tổ hợp" đầu kéo + mooc.
- "Tri-Axle" ghi "6 wheel positions", vẽ Trailer Axle 1, 2, 3, mỗi trục 4 lốp = 12 vị trí. Vai trò trục mặc định "Trailer".
- Sau liên kết, trang xe đầu kéo có khối "Linked Assets" › "Link Asset" › "VEHICLES" › TEST-MOOC-LOP. Tab Tire Management của đầu kéo KHÔNG thêm lốp mooc, vẫn chỉ 3 trục của đầu kéo.
Bất ngờ, lỗi, điểm khác tài liệu hãng: Lốp mooc tính km theo đồng hồ của mooc. Mooc thường không có đồng hồ nên Tire Meter dễ đứng yên (suy luận từ "The tire meter will update automatically based on the vehicle's meter readings"; chưa chạy riêng cho mooc).
Màn mới: tire-management-trailer — ảnh images/tire-management-trailer.jpg — sơ đồ 3 trục mooc.
Trả lời câu hỏi mở nào: bổ sung Mục Assumptions của spec nhóm Phương tiện về `Linked Vehicles` không thay được nghiệp vụ ghép tách mooc.
Dữ liệu TEST đã tạo: xe `TEST-MOOC-LOP` (id 5890758), liên kết với TEST-XE-LOP.

## Lắp, sửa, đảo, tháo lốp và Tire Activity — Chạy
Các bước đã làm: Add ở "Installed Tires": lắp theo chip vị trí Front Axle (2 lốp), Axle 2 (4 lốp), Axle 3 (4 lốp). Bấm lốp trên sơ đồ để sửa. Sửa nhanh gai và áp suất ngay trên dòng. Rotate Tires với "Standard 6x4". Remove lốp LF. Đọc Tire Activity.
Kết quả thấy được:
- Form "Install Tires": Position (chọn nhiều, chip All, Front Axle, Axle 2, Axle 3; vị trí đã có lốp thì mất khỏi chip), Install Date ("If backdating, the tire meter will be automatically calculated based on vehicle odometer readings since install."), Tire Meter at Installation, Current Tread Depth, Current Pressure, Tire Model, Factory Tread Depth, Minimum Tread Depth, Life Expectancy, Tire Identification Number. Thông báo "2 tires were installed on this vehicle."
- Lốp không phải bản ghi riêng có mã: lắp 4 lốp một lần thì cả 4 dùng chung TIN (`TEST-TIN-A2`), hệ thống không kiểm trùng. Dòng tên là "Unknown Tire" khi chưa có Tire Model.
- "Tire Model" báo "No options" trên tài khoản này, form không có nút tạo model. Không xác định được nguồn danh mục này.
- Rotate Tires: "Rotation Pattern" có "Standard 6x4" và ghi "Use a Standard or previously saved custom Rotation Pattern". Chọn mẫu thì tự điền New Position: LF↔RF, 2LO→3LI, 2LI→3LO, 2RI→3RO, 2RO→3RI, 3LO→2LI, 3LI→2LO, 3RI→2RO, 3RO→2RI. Sửa tay từng dòng được. Gai và áp suất đi theo lốp sang vị trí mới. Màn kết quả có "Undo Rotation" và Close (chưa bấm Undo).
- Remove: hộp "Remove Tires" ghi "Are you sure you would like to permanently remove tires from this asset?", cho chọn nhiều lốp, "Select All", thông báo "1 tire was removed from this asset." Vị trí trở lại nút +. Không hỏi lý do, không có đích đến.
- KHÔNG có chuyển kho: menu dòng lốp chỉ có "Edit", "Copy details to...", "Remove"; menu chung chỉ có "Rotate Tires", "Remove All". Không có khái niệm kho lốp, tháo là mất khỏi xe.
- Tire Activity: 1 dòng cho mỗi sự kiện từng lốp. Cột Tire Model, Date Recorded, Date Installed, Tire Meter, Activity, User, Method, Tire Pressure, Tread Depth, Position, Axle Type, Tire Identification Number. Activity gặp được: "Installed", "Tire Rotation", "Tread Depth Reading", "Pressure Reading", "Removal". Đảo 10 lốp sinh 10 dòng dạng "Left Front (LF) > Right Front (RF)", "Steer > Steer". Sau khi tháo, lịch sử lốp vẫn còn.
Bất ngờ, lỗi, điểm khác tài liệu hãng: Sửa gai áp suất trên dòng lưu ngay khi rời ô, không có nút Lưu, tạo dòng Reading ngay. Sửa trong hộp Edit cũng tạo "Tread Depth Reading". Vì không có định danh lốp thật, không theo được một lốp qua nhiều xe.
Màn mới: tire-install — images/tire-install.jpg. tire-edit — images/tire-edit.jpg — thêm "Current Tire Meter", "Remove". tire-management-installed — images/tire-management-installed.jpg — mỗi ô lốp hiện gai và PSI, gai dưới mức đỏ. tire-rotate — images/tire-rotate.jpg. tire-rotate-result-undo — images/tire-rotate-result-undo.jpg. tire-remove — images/tire-remove.jpg. tire-activity — images/tire-activity.jpg.
Trả lời câu hỏi mở nào: OQ-4 nhóm Phương tiện (phần lốp).
Dữ liệu TEST đã tạo: 10 lốp TEST trên TEST-XE-LOP (TIN `TEST-TIN-F`, `TEST-TIN-A2`, `TEST-TIN-A3`); đã Remove 1 lốp LF (thao tác "tháo" được giao, bản ghi TEST) nên còn 9.

## Số đồng hồ: Void, Exceeds Max, Out of Sequence — Chạy (Out of Sequence: Một phần)
Các bước đã làm: Trên TEST-XE-LOP đang 5.000 km, nhập lần lượt: 5.500 hôm nay; 5.800 lùi ngày 01/11; 5.800 lùi ngày có tick Void; 5.300 hôm nay; 20.000 hôm nay; 5.400 ngày mai 04/11; Unvoid dòng 20.000; thử Fuel Entry odometer 21.000 lùi ngày 01/11 (không lưu được, không tạo).
Kết quả thấy được:
- 5.800 ngày 01/11 (lớn hơn số ngày sau): BỊ TỪ CHỐI, "must be less than 5,000 or marked as void", "Meter Entry could not be created". Không tự Void.
- 5.400 ngày 04/11 (nhỏ hơn số trước đó): BỊ TỪ CHỐI, "must be greater than 5,500 or marked as void".
- Tick Void thì lưu được; Void Status "Manually Voided". Tooltip: "A voided meter entry is never considered a vehicle's "current meter" even if it's the most recent. Hence, a voided meter entry will never trigger a service reminder or anything else that depends on a vehicle's current meter value."
- 5.300 cùng ngày với 5.500: lưu được, không Void, không báo gì. Đồng hồ xe vẫn 5.500; dòng ghi "200 km ago".
- 20.000 hôm nay (nhảy 14.500): "Meter Entry was successfully created. However, it was automatically voided because it exceeds maximum possible for day". Dòng: Void Status "Auto-Voided", Auto-Void Reason "Exceeds Max. Daily Usage". Popup: "Automatically voided because it exceeds the maximum daily usage of 4,828 kilometers by 9,672 kilometers", Last Meter Entry 5.500, Daily Usage 14.500, Max Daily Usage 4.828, Exceeds By 9.672, nút "Unvoid this Entry".
- Dòng 5.500 được gắn cờ đỏ, Void Status "Conflict Source". Popup "Conflicting Meter Entry": "This entry was flagged because it has caused one or more successive entries to be auto-voided", Conflicts With 1 Entry, Difference 14,500 kilometers over 0 days.
- Unvoid: hộp "This operation will attempt to unvoid the selected Meter Entry." → Confirm → "Successfully unvoided Meter Entry". Không hỏi lý do. Đồng hồ xe nhảy thành 20.000 ("Current odometer"), cờ Conflict Source của 5.500 tự mất.
- Fuel Entry cùng luật: odometer 21.000 ngày 01/11 báo "must be less than 5,000 or marked as void", "Fuel Entry could not be created".
- Void Status lọc: All Voided, Manually Voided, Auto Voided, Not Voided.
Bất ngờ, lỗi, điểm khác tài liệu hãng: Dòng "Last updated: 5,000 km (Today)" trong hộp nhập hiện số cũ dù xe đã 5.500. Số so sánh "5,000" trong lỗi là dòng đầu cùng ngày 03/11, không phải số hiện tại 5.500. Nhập tay trên web không ra lý do "Out of Sequence": số lệch thứ tự ngày bị chặn ngay bằng lỗi trường. Chưa thấy dòng nào mang lý do đó; có thể chỉ xảy ra với nguồn không có người sửa (telematics, API), chưa kiểm chứng.
Một Unvoid không kiểm lại Max Daily Usage: 1 thao tác đẩy đồng hồ lên 20.000, sau đó các số thật sẽ bị lỗi "must be greater than".
Màn mới: meter-reject-backdate — images/meter-reject-backdate.jpg. meter-reject-forward — images/meter-reject-forward.jpg. meter-history-conflict — images/meter-history-conflict.jpg — cột Void Status, Auto-Void Reason, cờ đỏ.
Trả lời câu hỏi mở nào: OQ-5 nhóm Phương tiện: lệch thứ tự theo NGÀY bị từ chối, không Void; cùng ngày nhỏ hơn không bị gì; lý do "Out of Sequence" không tái hiện được trên web. OQ-6: số sai dưới ngưỡng cùng ngày không ghim vì lấy số lớn nhất; số sai trên ngưỡng tự Void; Unvoid nhầm thì ghim số hiện tại.
Dữ liệu TEST đã tạo: 5 dòng đồng hồ trên TEST-XE-LOP (5.000, 5.500, 5.300, 20.000 đã Unvoid, 5.800 Manually Voided). Đồng hồ xe hiện 20.000.

## Đọc lốp, Tire Readings, cảnh báo gai — Chạy
Các bước đã làm: Sửa gai và áp suất từng vị trí trên TEST-XE-LOP, đặt 3 (dưới mức tối thiểu 4), 5, 6, 8, 12, 14. Mở Vehicles › Tire Readings, lọc Tread Depth Health. Kiểm tra Issues và Notifications của xe.
Kết quả thấy được:
- Tire Readings có 1 dòng cho mỗi vị trí, hiện lần đọc mới nhất (không phải toàn bộ lịch sử). Cột Vehicle, Last Reading Date, Reading Method, Recorded By, Tread Depth, Pressure, Position, Tire Model, Tire Meter, Install Date, Life Expectancy, Minimum Tread Depth, Factory Tread Depth, Tire Identification Number. Có Group: None.
- Lọc Tread Depth Health: Low, Warning, Normal, Unknown. Lọc Reading Method: Manual, Inspection, Telematics, API, Import.
- Dữ liệu thật với mức tối thiểu 4/32: 3/32 = Low (đỏ, 4 dòng); 5/32 và 6/32 = Warning (vàng, 2 dòng); 8, 12, 14/32 = Normal (xám, 3 dòng). Chưa thử đúng 4 và 7 nên chưa biết biên Warning.
- Dưới mức tối thiểu từ màn Tire Management: chỉ đổi màu. KHÔNG tạo sự cố (Issues Open của xe trống, trang xe "There are no Open Issues for this Vehicle"), KHÔNG có thông báo mới. Không thấy nhắc lịch nào.
- Áp suất không có mức Low trên màn này: 60 PSI hiển thị xám.
Bất ngờ, lỗi, điểm khác tài liệu hãng: Tire Readings của lốp đã tháo (LF) biến mất khỏi danh sách, chỉ còn ở Tire Activity.
Màn mới: tire-readings-data — images/tire-readings-data.jpg. tire-readings-filter-warning — images/tire-readings-filter-warning.jpg.
Trả lời câu hỏi mở nào: thông tin cho OQ-3 nhóm Phương tiện (phía Delta vẫn phải quyết định có đo gai không).
Dữ liệu TEST đã tạo: các lần đọc trên TEST-XE-LOP.

## Tire Readings trong phiếu kiểm tra — Chạy
Các bước đã làm: Start Inspection, biểu mẫu "TEST - Pre-trip inspection", chỉ chọn được TEST-XE-01 (xe chưa có cấu hình trục; TEST-XE-LOP không có trong danh sách vì chưa gán vào biểu mẫu). Bấm Save khi chưa khai trục. Chọn 4x2 RWD ngay trong phiếu, Done. Nhập LF, RF 10/32 100 PSI; LR, RR 3/32 60 PSI. Nộp.
Kết quả thấy được:
- Kiểm chứng đúng lỗi: "Please select axle configuration before submitting the form" kèm "Could not submit inspection form. Please fix any errors and try again."
- Mục Tires hiện hộp "More info needed", "To display the correct number of tires below, please provide the following:", ô "Axle Configuration" và "Done". Tức là người kiểm tra được khai cấu hình trục ngay trong phiếu. Done xong hiện ô Tread Depth và Pressure bắt buộc cho từng vị trí.
- Khi Done, hệ thống sinh tire_id cho từng vị trí (thấy trong tên trường form, vd tire_id_822197), nên xe tự có 4 lốp. Date Installed là lúc khai, 11/03/2026 12:30am.
- Biểu mẫu đặt mức riêng cho mục Tire Readings: "Require Tread Depth" Yes, Minimum 5/32 in, Maximum -, "Require Pressure" Yes, Minimum 15 PSI, Maximum -, "Require photo or comment for "Fail"" Yes.
- 3/32 dưới mức 5/32 của biểu mẫu: báo "must contain a remark on failure", phải có nhận xét mới nộp được.
- Nộp xong #126051306: Tires "Fail" cả mục (không tách từng vị trí ở dòng tổng), trạng thái "Creating Issue" rồi "Issue #32". Sự cố #32: "[Inspection] TEST gai thap" (lấy từ nhận xét), Priority High, Source "Inspection Submission #126051306". Xuất hiện trong Item Failures tab Open Issue.
- Việc tạo sự cố đến từ workflow của biểu mẫu: "If an item fails", "ANY Failed Inspection Item" → "Create an issue", mô tả "Create issues automatically". Không do lốp.
- Tire Readings thêm 4 dòng Reading Method "Inspection #126051306", Tire Meter 100 km (đồng hồ 2.300 − 2.200). 3/32 hiện Low đỏ dù Minimum Tread Depth của lốp để trống.
Bất ngờ, lỗi, điểm khác tài liệu hãng: Có 2 mức tối thiểu tách rời: Minimum Tread Depth của lốp (4/32 trên LOP) và Minimum của mục trong biểu mẫu (5/32). Cùng số đọc có thể Fail ở phiếu mà chỉ Warning ở lốp. Chỉ đường phiếu kiểm tra mới ra sự cố. Nhãn "Lighting Devices and Reflectors" đòi "must contain a remark on pass" do cấu hình mục đó.
Màn mới: inspection-tire-axle-error — images/inspection-tire-axle-error.jpg — hộp lỗi đỏ + More info needed. inspection-tire-remark-required — images/inspection-tire-remark-required.jpg — ô gai từng vị trí và lỗi bắt nhận xét.
Trả lời câu hỏi mở nào: câu hỏi "cảnh báo dưới mức có tạo sự cố không" trong giao việc: chỉ qua phiếu + workflow.
Dữ liệu TEST đã tạo: phiếu #126051306, sự cố #32, cấu hình 4x2 RWD + 4 vị trí lốp trên TEST-XE-01, đồng hồ TEST-XE-01 2.300 km.

## Chi phí, Expense Entry — Chạy
Các bước đã làm: Tạo Expense Entry trên TEST-XE-LOP: định kỳ Insurance 1.500.000 ₫ từ 03/11/2026 đến 31/01/2027 hàng tháng; đơn lẻ Tolls 2.000.000 ₫ ngày 15/10/2026. Xem Expense Entries và khối Cost of Ownership.
Kết quả thấy được:
- Form: Vehicle, Expense Type, Vendor, Amount, Frequency ("Single Expense" hoặc "Recurring Expense", "Repeats on a monthly or annual basis"), Notes. Recurring thêm Start Date, End Date, Frequency.
- Expense Type có sẵn: Annual Inspection Fees, Depreciation, Down Payment, Fines, Insurance, Lease, Legal/Court Costs, Loan, Loan Payment, Miscellaneous, Moving Violations, Safety Technology, Telematics Device, Tolls, Tool, Vehicle Disposal Costs, Vehicle Registration and Taxes.
- Định kỳ xử lý nền: "Processing: Recurring expense save" rồi "Complete: Recurring expense save", "You may have to refresh your browser to see the changes." Sinh ngay 3 dòng 03/11, 03/12, 03/01 trong tab "Future". Tab "Past" của xe trống ngay sau khi lưu, kể cả dòng 03/11 đúng hôm nay.
- Cost of Ownership "This Month": Total Costs 1.500.000 ₫, Cost Per Meter 100 ₫ / km, Fuel & Energy Costs 0, Service Costs 0, Other Costs 1.500.000. "All Time": 3.500.000 ₫, 233 ₫ / km (2.000.000 + 1.500.000; dòng 03/12 và 03/01 chưa tính). Mốc chọn: This Month, Last Month, This Year, Last 12 Months, Last Year, All Time.
- Cost Per Meter = tổng chi phí chia km đã chạy trong kỳ: 3.500.000 / 15.000 = 233 (đồng hồ 5.000 → 20.000). Số 15.000 là số đã Unvoid ở luồng đồng hồ, nên 1 số đồng hồ sai làm sai luôn chi phí/km (suy từ phép tính).
Bất ngờ, lỗi, điểm khác tài liệu hãng: Ô Start Date hiện chữ xám 11/03/2026 trông như đã điền nhưng là placeholder, lưu báo "can't be blank". Cùng kiểu ở Start Date của bảo hành.
Màn mới: expense-recurring — images/expense-recurring.jpg. expense-future — images/expense-future.jpg — tab Past, Future. vehicle-cost-of-ownership — images/vehicle-cost-of-ownership.jpg (kèm khối Linked Assets).
Dữ liệu TEST đã tạo: Expense Entry #24243307 (Tolls), 3 dòng Insurance định kỳ trên TEST-XE-LOP.

## Bảo hành, Warranty Opportunities — Chạy
Các bước đã làm: Add Warranty, chọn TEST-XE-01, Start Date 01/10/2026, Start Meter nhập 1000. Xem Standard templates. Chọn Standard Warranty, Coverage Duration 1 Years, Coverage Distance 50000, mã bảo dưỡng 013. Lưu. Xem Lệnh #100 trước và sau khi thêm Service Task "Brake Inspection" (task mẫu có sẵn, không sửa task).
Kết quả thấy được:
- Form "New Warranties" 2 bước: "Vehicles" (chọn nhiều xe, mỗi xe một Start Date, Start Meter riêng, hiện Year, Make, Model) → "Coverage Type": "Standard Warranty" ("Manually add OEM coverages"), "Standard templates" ("Add a template of coverages by OEM"), "Extended Warranty" ("Manually add aftermarket coverages"). Trường: Warranty Name, Description, Manufacturer, Warranty Vendor, Contract ID, Vendor Link, Coverage Duration + đơn vị, Coverage Distance + "Unlimited".
- Kiểm chứng ngày hết hạn tự tính: 01/10/2026 + 1 Years = End Date 10/01/2027; Status "Active"; "Warranties have been successfully created".
- End Meter = Start Meter + Coverage Distance: Start Meter 1 km, Coverage 50,000 km, End Meter 50,001 km. Lưu ý: tôi nhập 1000 mà danh sách ghi 1 km. Chưa rõ do ô nhập hay định dạng, chưa thử lại.
- Coverage Template: tooltip "Coverage templates contain a collection of coverages based on manufacturer guidelines"; trên TEST-XE-01 ô báo "No options" (xe không có Make, Model; chưa kiểm chứng đó có phải lý do).
- "Maintenance Categorization": "Applying Maintenance Categorization to this Vehicle's coverage will surface claim opportunities when a Work Order form includes a Service Task with the same code". Nhập mã hệ thống 000, 000-001; nhập 013 hiện "1 - Chassis" › "013 - Brakes". Có Bulk Mode, Column Mode.
- Trước khi có task khớp, Lệnh #100 (có sẵn phụ tùng má phanh nhưng không gắn Service Task): khối "Warranty Opportunities", "Total vehicle coverage breakdown", 1 active, 0 expiring soon, 1 total; "Vehicle Coverage" "No vehicle warranty opportunities to show."; "Replaced Parts" "No part warranty opportunities to show."
- Sau khi thêm Service Task "Brake Inspection" (task mang sẵn 1 - Chassis, 013 - Brakes) và lưu: "Warranty Opportunities (1)", Vehicle Coverage › Service Task "Brake Inspection" › "View Active Coverage" › "TEST Bao hanh dong co" với Complaint, Cause, Correction trống.
Bất ngờ, lỗi, điểm khác tài liệu hãng: Khớp theo mã VMRS của Service Task, không theo phụ tùng. Phụ tùng phanh đứng riêng không gợi ý gì. Không có bảo hành thì không có cơ hội; khối hiển thị luôn trên lệnh. Chưa thử nút claim.
Màn mới: warranty-new-vehicles — images/warranty-new-vehicles.jpg. warranty-new-template — images/warranty-new-template.jpg. warranty-new-standard — images/warranty-new-standard.jpg. warranty-maintenance-codes — images/warranty-maintenance-codes.jpg. warranty-list — images/warranty-list.jpg. wo-warranty-before — images/wo-warranty-before.jpg. wo-warranty-opportunity — images/wo-warranty-opportunity.jpg.
Dữ liệu TEST đã tạo: Warranty "TEST Bao hanh dong co" trên TEST-XE-01. Sửa Lệnh #100: thêm Service Task "Brake Inspection".

## Phân tích thay xe, Replacement Analysis — Chạy (chỉ đọc)
Các bước đã làm: Mở Vehicles › Replacement Analysis, đọc biểu đồ và tham số, không đổi số nào, không lưu. Tính tay năm 1 đối chiếu dữ liệu biểu đồ.
Kết quả thấy được:
- Trang KHÔNG có ô chọn xe. Không lấy dữ liệu của xe nào: TEST-XE-LOP đã có chi phí nhưng trang không đổi, không có danh sách xe. Đây là máy tính ước lượng cấp tài khoản, người dùng tự nhập số. Tiền ghi ₫ nhưng số mặc định là kiểu đô la (Purchase Price 50000).
- Tham số đổi được, giá trị đang có: Lifecycle Estimates: Estimated Vehicle Life 96 months, Estimated Annual Usage 20000 kilometers, Estimated Fuel Efficiency 15 mpg (US). Acquisition: Purchase Price 50000. Disposal: Estimated Disposal Cost 1000, Estimated Salvage Value 20 % of purchase price, Method of Depreciation "Double Declining" (đang chọn) hoặc "Sum of Years". Service Cost Estimates Year 1 đến 8: 1500, 1500, 1500, 300, 1350, 2500, 2000, 10000. Fuel Cost Estimates Year 1 đến 8: 1.5, 1.6, 1.75, 1.9, 2, 2.1, 2.3, 2.5 / liters.
- Biểu đồ: trục Vehicle Age 1 đến 8, Annual Cost per Kilometer, các lớp chồng, đường "Minimum Cost of Ownership", mốc "Optimal Replacement" tại năm 7, "Estimated Replacement" tại năm 8.
- Công thức, phần kiểm được bằng phép tính năm 1 (đối chiếu dữ liệu biểu đồ 0.23518899626183 và đỉnh khoảng 0.935): nhiên liệu = 1,5 / (15 mpg đổi ra 6,377 km/lít) = 0,2352/km. Bảo dưỡng = 1500 / 20000 = 0,075/km. Khấu hao Double Declining = 50000 × 2/8 / 20000 = 0,625/km. Tổng 0,935/km. Các năm sau chưa kiểm được; Optimal Replacement khớp điểm thấp nhất đường tổng trên hình.
Bất ngờ, lỗi, điểm khác tài liệu hãng: Không có nút Lưu trên trang; không thử đổi số nên chưa biết có tự lưu không. Tham số ước tính trên từng xe nằm ở form xe tab Lifecycle (Estimated Service Life in Months, Estimated Service Life in Meter, Estimated Resale Value), nhưng trang này không dùng chúng theo những gì thấy.
Màn mới: replacement-params — images/replacement-params.jpg — toàn bộ ô tham số (đã có images/replacement.jpg cho biểu đồ).
Trả lời câu hỏi mở nào: OQ-4 trong `fleetio-vehicle.md` (lãnh đạo có cần phân tích thay xe không) vẫn là câu của Delta; bổ sung sự thật: Fleetio chỉ là máy tính chung, không theo xe.
Dữ liệu TEST đã tạo: không.

## Lịch gán xe: gán, sửa, trùng, thay người — Chạy
Các bước đã làm: Add Assignment TEST-XE-LOP + TEST-LAI-XE-02 từ 05/11 đến 07/11. Bấm ô trống trên lịch tuần. Thử mở kết thúc từ 04/11 (đè lên phân công có sẵn). Tạo TEST-XE-LOP + TEST-LAI-XE 10/11 đến 12/11, trong khi TEST-LAI-XE đang giữ TEST-XE-01 không có ngày kết thúc. Edit đổi Operator phân công 05/11 sang TEST-LAI-XE. Xem chi tiết.
Kết quả thấy được:
- Add Assignment: Assigned Vehicle, Operator, Start Date/Time ("When assignment starts. Leave blank if assignment has always existed."), End Date/Time ("When does this assignment end? Can be past or future."), comment. Chọn đủ xe và người thì hiện thêm Starting Odometer, Ending Odometer.
- Lịch: trục Vehicle, xem Day, Week, thanh phân công màu cam (tương lai) và xanh (đang chạy), lịch tháng bên phải. Bấm ô trống mở "Add Vehicle Assignment For TEST-XE-LOP", xe khoá, ngày điền sẵn theo ô (11/04/2026 12:00am).
- TRÙNG XE: chặn. Start 04/11 không có End đè lên 05/11: "can't overlap existing assignments" ở cả Start và End, "Vehicle Assignment could not be created". Không tự đóng phân công cũ.
- TRÙNG NGƯỜI: KHÔNG chặn. TEST-LAI-XE giữ TEST-XE-01 "No end date", vẫn được gán TEST-XE-LOP cả 05/11 đến 07/11 và 10/11 đến 12/11: "Vehicle Assignment was successfully updated", "...successfully created". Một người lái 2 xe cùng lúc hợp lệ.
- THAY NGƯỜI: chỉ có cách sửa đè Operator trên phân công (xe khoá khi sửa). Không có hành động "thay người" riêng. Trang "Vehicle Assignment #12480917" chỉ hiện Operator mới kèm nhãn "Future", Start, End, Duration 2 days, Start Meter, End Meter, Distance; không còn dấu vết người cũ (không thấy lịch sử đổi trên trang). Sửa phân công đã qua thì chưa thử.
- Menu thanh phân công: View, Edit, Delete (không bấm Delete).
- Hộp Edit gợi ý Starting Odometer 20000.0 (đồng hồ hiện tại của xe).
Bất ngờ, lỗi, điểm khác tài liệu hãng: Trường ngày gửi đi có múi giờ thiết bị (2026-11-05 00:40+07:00) trong khi tài khoản đặt America/Chicago. Muốn đổi người giữa chừng phải tự đóng phân công cũ rồi tạo mới; Fleetio không làm thay.
Màn mới: assignment-add — images/assignment-add.jpg. assignment-week — images/assignment-week.jpg. assignment-overlap — images/assignment-overlap.jpg. assignment-edit — images/assignment-edit.jpg. assignment-detail — images/assignment-detail.jpg.
Trả lời câu hỏi mở nào: OQ-1 nhóm Phương tiện (một xe nhiều người theo ca): theo Fleetio được, miễn các khoảng không chồng nhau; quyết định của Delta vẫn mở. Làm rõ dòng "không trùng thời gian" ở spec 7.1: chỉ tính theo xe, không tính theo người.
Dữ liệu TEST đã tạo: phân công #12480917 TEST-XE-LOP + TEST-LAI-XE 05/11 đến 07/11 (đã đổi từ TEST-LAI-XE-02), phân công TEST-XE-LOP + TEST-LAI-XE 10/11 đến 12/11.

## Chưa làm trong lượt này
- Biên chính xác giữa Low, Warning, Normal (chưa thử gai đúng 4 và 7).
- Bấm "Undo Rotation", "Copy details to...", lưu mẫu đảo tuỳ biến, lắp vị trí Spare Tire.
- Lốp trên mooc. Tire Meter tăng theo đồng hồ mới thấy ở lốp qua phiếu (100 km), chưa kiểm lại trên lốp lắp tay.
- Nguồn danh mục Tire Model ("No options") và điều kiện có Coverage Template.
- Lý do Auto-Void "Out of Sequence": không tái hiện được bằng nhập tay web; nguồn telematics không có.
- Form "New Fuel Entry" bỏ dở bị kẹt hộp "Leave site?": không có Fuel Entry nào được lưu.

# Lượt 3 (03/11)

## Lý do Out of Sequence, icon lạ của số 3.100 km — Chạy (đọc kết quả phiếu Fleetio Go có sẵn)
Các bước đã làm: Mở Meter History lọc TEST-XE-01, bấm huy hiệu của từng dòng. Không mở phiếu, không mở bản đồ.
Kết quả thấy được:
- Dòng 3.100 km từ phiếu Fleetio Go: Void Status "Auto-Voided", Auto-Void Reason "Out of Sequence", ngày đồng hồ 11/02/2026. Icon lạ chính là dấu đã Void.
- Popup "Auto-Voided Meter Entry": "Automatically voided because it is out of sequence and ahead of the conflicting meter by 601 kilometers". Conflicting Entry 2.499 km ngày 11/03/2026, nguồn Manual. Conflict Status "601 kilometers ahead of", 3,100 km - 2,499 km.
- Dòng 2.499 km gắn cờ đỏ "Conflict Source". Popup "Conflicting Meter Entry": "This entry was flagged because it has caused one or more successive entries to be auto-voided", Conflicts With 1 Entry, Difference "601 kilometers over 1 day".
- Xe vẫn 2.999 km vì số đã Void không làm số hiện tại. Menu dòng có Edit, Unvoid, View Record History, Delete (không bấm).
Bất ngờ: Cùng tình huống, nhập tay trên web bị chặn ở trường ("must be less than … or marked as void"), còn phiếu từ app được lưu rồi tự Void. Một ca thấy thật, chưa thử nguồn khác (telematics, API). Ngày 11/02 lệch so với giờ VN vì tài khoản theo America/Chicago (suy luận từ múi giờ tài khoản, chưa tách riêng để chứng minh).
Màn mới: meter-out-of-sequence-autovoid — images/meter-out-of-sequence-autovoid.jpg — popup Auto-Voided; mã phiếu đã được che trong ảnh.
Trả lời câu hỏi mở nào: OQ-8 nhóm Phương tiện: Một phần, có ca từ Fleetio Go; chưa thử telematics, API.
Dữ liệu TEST đã tạo: không.

## Biên Max Daily Usage — Chạy
Các bước đã làm: Trên TEST-XE-LOP sau khi Void hết số, nhập 100, 4.928 (đúng +4.828), rồi 9.757 (+4.829).
Kết quả thấy được: +4.828 lưu bình thường. +4.829 Auto-Voided, "Exceeds Max. Daily Usage", toast "Meter Entry was successfully created. However, it was automatically voided because it exceeds maximum possible for day". Dòng 4.928 thành "Conflict Source", đồng hồ xe giữ 4.928.
Trả lời câu hỏi mở nào: biên ngưỡng ngày của FR-fleetio-vehicle-014: đúng bằng 4.828 km vẫn nhận.

## Đổi đồng hồ: Void hàng loạt rồi nhập lại từ số nhỏ — Chạy
Các bước đã làm: Meter History lọc TEST-XE-LOP, tick cả danh sách, mở Actions. Bỏ tick dòng đã Void, chọn Void, gõ VOID, Confirm 5 dòng. Nhập số mới 100 km.
Kết quả thấy được:
- Actions gồm Void, Unvoid, Delete. Chọn lẫn dòng đã Void và chưa Void thì Void, Unvoid đều khoá; chỉ chọn dòng chưa Void thì Void mở.
- Hộp "Void Meter Entries": "This operation will attempt to void all 5 selected Meter Entries. Please type VOID in all caps to confirm…", Confirm khoá tới khi gõ đúng. Toast "Successfully voided Meter Entries".
- Dòng trước đó Unvoid (20.000) quay về "Auto-Voided", "Exceeds Max. Daily Usage", không thành Manually Voided. 4 dòng còn lại "Manually Voided".
- Void toàn bộ: xe hiện "0 km", hộp nhập ghi "Last updated: No meter history". Số 100 km nhận ngay, không báo nhỏ hơn số cũ.
Bất ngờ: Không thấy mục tên "Bulk Meter Management" ở các menu đã mở (menu "…" của Meter History chỉ có Import Meter Entries, Export Data; không bấm). Đây là thao tác Void hàng loạt trên danh sách; chưa đối chiếu nó có đúng là tính năng tài liệu hãng gọi tên đó. Không có nguồn GPS nên phần "kể cả số GPS" vẫn là Docs. Không có bước khai báo "thay đồng hồ", không lưu lý do.
Hộp "Save and Add Another" vẫn ghi "No meter history" sau khi vừa lưu 100 km (số cũ trên hộp).
Màn mới: meter-bulk-void-secondary — images/meter-bulk-void-secondary.jpg — danh sách sau Void hàng loạt, có cả dòng Secondary.
Trả lời câu hỏi mở nào: OQ-6 phần còn lại (Void toàn bộ): xe về 0 km, nhận số bất kỳ. OQ-14 phần Bulk: như trên.
Dữ liệu TEST đã tạo: TEST-XE-LOP thêm 100, 4.928, 9.757 (Auto-Voided); 5 dòng cũ đã Void.

## Đồng hồ phụ — Chạy
Các bước đã làm: Form xe, Settings, tick "Add Secondary Meter" ("Track an additional meter, such as a concrete mixer, street sweeper, cleaning equipment, etc."). Mặc định Hours, nhập Current Reading 50, lưu. Nhập phiếu chỉ có Secondary 60.
Kết quả thấy được: Đầu trang xe hiện 2 số (4.928 km, 50 hr), Overview thêm "Secondary Meter". Add Meter Entry có 2 ô, mỗi ô có Void riêng, "Last updated" riêng. Bỏ trống Primary vẫn lưu được. Danh sách có Meter Type "Secondary", "Current hours", chuỗi riêng với Primary.
Dữ liệu TEST đã tạo: Secondary 50, 60 hr trên TEST-XE-LOP.

## Giải mã VIN — Chạy
Các bước đã làm: Form sửa TEST-XE-LOP. Gõ VIN ngắn ABC123, rồi VIN ví dụ công khai 17 ký tự, bấm Decode. Áp vào form, không lưu.
Kết quả thấy được:
- VIN ngắn: Decode khoá (icon khoá), không có câu giải thích khi rê chuột.
- 17 ký tự: "Decoding VIN...", rồi hộp "Add New Vehicle Data": "Select any data attributes you would like to save to this vehicle. Saving will overwrite any existing data for those attributes." Bảng Attribute, Current Data, Decoded Data, nhãn New hoặc Different. Vehicle Type Semi Truck với Car nhãn "Different", mặc định KHÔNG tick; các dòng New tick sẵn (Fuel Type, Year, Make, Model, Trim, Body Type, MSRP, EPA, động cơ, hộp số, bánh…).
- "Save Data to Vehicle" chỉ điền vào form, xe chưa đổi cho tới khi Save Vehicle: "We've successfully decoded your VIN and have downloaded the vehicle specifications."
- Thoát form có thay đổi: tab kẹt hộp rời trang, phải mở tab mới.
Màn mới: vin-decode-review — images/vin-decode-review.jpg — bảng so sánh thuộc tính.

## Trạng thái xe — Chạy
Các bước đã làm: Trên TEST-XE-LOP đổi qua form: Out of Service, Sold, In Shop, Sold, Inactive. Khi Out of Service tạo phân công; khi Sold tạo Lệnh #108, #109; xem menu Add.
Kết quả thấy được: Danh sách chọn có Active, In Shop, Inactive, Out of Service, Sold. Đổi tự do giữa mọi cặp đã thử, toast "Vehicle was successfully updated".
| Trạng thái | Thao tác đã thử | Kết quả |
|---|---|---|
| Out of Service | Add Vehicle Assignment, nhập đồng hồ | Lưu được, không cảnh báo; menu Add đủ mục |
| Sold | Tạo Lệnh sửa, nhập đồng hồ | Lưu được, không cảnh báo; Liên kết mooc còn nguyên |
| In Shop | Lưu trạng thái | Không tự sinh Lệnh; liên kết còn nguyên |
| Inactive | Thêm đồng hồ phụ, phân công | Lưu được |
Điều KHÔNG xảy ra: Mở hoặc đóng Lệnh không đổi trạng thái xe (xe Sold vẫn Sold). Không hỏi lý do đổi trạng thái.
Bất ngờ: Một lần lưu In Shop kèm nhóm mẫu Georgia / Atlanta không áp dụng (xe vẫn Sold, No Group). Lỗi thấy rõ ở mục Nhóm xe bên dưới: cả form bị từ chối vì nhóm Sample.
Status Updates ghi đủ từng lần: "Bảo Tín updated status from Sold to Inactive", ngày giờ, thời gian ở trạng thái trước (vd "1 minute, 50 seconds").
Màn mới: vehicle-status-history — images/vehicle-status-history.jpg — chỉ chụp phần hộp.
Trả lời câu hỏi mở nào: OQ-11 phần đổi trạng thái.

## Archive, Restore, liên kết — Chạy
Các bước đã làm: Restore TEST-XE-LOP, đọc Record History, nối lại mooc, thử Archive khi có Lệnh mở (2 lần, có đối chứng), đóng Lệnh, tạo phân công đang chạy và tương lai, Archive thật, thử Restore khi gói đầy.
Kết quả thấy được:
- Restore bấm là chạy ngay, không hỏi: "Record successfully restored!". Liên kết, phân công đã mất KHÔNG quay lại. Trạng thái, đồng hồ, cấu hình trục giữ nguyên. Archive không đổi trường Status: xe Archived vẫn hiện Active hoặc Inactive.
- Record History chỉ có "Archived At changed from … to …", "Axle config created", "Vehicle created". Không ghi việc ngắt liên kết, không ghi đổi đồng hồ.
- Hộp "Confirm Vehicle Archive": "Archiving this vehicle will end any associations with linked assets (vehicles and tools), end any current vehicle assignments, and remove any future-dated vehicle assignments." kèm 2 câu chặn Lệnh chưa xong, Motor Pool đang đặt.
- Có Lệnh Open: toast "Vehicle could not be archived." không nêu lý do. Xe không Archive.
- LỖI ĐÁNG GHI: lần Archive bị từ chối đó VẪN ngắt liên kết với mooc, ở cả hai phía; phân công tương lai thì còn. Đối chứng: nối lại, lưu Sold và In Shop liên kết vẫn còn; tạo Lệnh #109, Archive bị từ chối, liên kết lại mất. Thấy 2/2 lần.
- Archive thành công: liên kết mất; phân công đang chạy bị đóng ngay (kết thúc 10/11 đổi thành 11/03/2026 12:35pm, Duration 1m); phân công 20/11 bị xoá hẳn, không còn dòng nào. Lịch sử liên hệ TEST-LAI-XE-02 hiện nhãn "Archived". Cột Start Meter trống dù form đã điền sẵn 4.928. Xe rời khỏi lịch phân công. Toast thành công có câu báo các bản ghi liên quan cập nhật ở nền (chụp nhỏ, không đọc được nguyên văn).
- Phân công 05/11 và 10/11 của lượt trước đã mất do lần Archive ở phiên chính, khớp câu trên.
- Đóng Lệnh: "Started At can't be blank"; sau đó "Starting Meter Entry can't be blank (per your account settings)", "Odometer can't be blank (per your account settings)". Start Odometer 4.928 bị chặn "must be less than 100 or marked as void" vì Actual Start ghi 12:28am sớm hơn số 100 lúc trưa; nhập 90 thì qua. Đóng Lệnh tự sinh Service Entry.
- Gói đầy: sau khi tạo xe thứ 5, nút Restore của TEST-XE-LOP khoá, bấm không có gì, không có câu giải thích.
Màn mới: vehicle-archive-confirm — images/vehicle-archive-confirm.jpg — hộp xác nhận, chỉ chụp phần hộp.
Không chạy được: Motor Pool đang đặt chặn Archive: chưa tạo đặt xe, chỉ có câu trong hộp thoại.
Trả lời câu hỏi mở nào: OQ-11 phần Archive, Restore.
Dữ liệu TEST đã tạo: Lệnh #108, #109 (Completed, Service Entry tự sinh), phân công TEST-LAI-XE-02 (đã đóng, một dòng đã bị xoá). TEST-XE-LOP đang Archived, Inactive, 4.928 km.

## Liên kết một mooc với nhiều xe — Chạy
Các bước đã làm: TEST-MOOC-LOP nối TEST-XE-LOP, rồi nối thêm TEST-XE-01 (Car).
Kết quả thấy được: Lưu được cả hai, "Linked Assets have been updated", không cảnh báo, không kiểm loại xe. Hiện ở cả hai phía. Xe đã nối không còn trong ô chọn. Form xe có trường "Linked Vehicles" cùng dữ liệu. Sau khi TEST-XE-LOP Archive, mooc chỉ còn TEST-XE-01.
Màn mới: trailer-linked-two-vehicles — images/trailer-linked-two-vehicles.jpg.
Trả lời câu hỏi mở nào: OQ-16 nhóm Phương tiện: một mooc nối được nhiều xe, không có ngày hiệu lực, không chặn.
Dữ liệu TEST đã tạo: liên kết TEST-MOOC-LOP với TEST-XE-01 (còn hiệu lực).

## Tạo nhiều xe, trùng tên, trùng VIN — Chạy
Các bước đã làm: Add Multiple Vehicles với 1 dòng trùng tên và trùng VIN mẫu; form đơn cùng dữ liệu; form đơn đổi sang tên xe đã Archive (VIN vẫn trùng để không lưu); Add Multiple 1 dòng hợp lệ.
Kết quả thấy được:
- Bước 1 ô dán tối đa 200 xe, mỗi dòng {Vehicle Name}, {VIN}, {Group}; "Any group (including parents) that do not exist will be created." Bước 2 chỉ hiện lại bảng, không kiểm trùng.
- Dòng trùng: "Process warning: Add Multiple Vehicles", "Please check your email for detailed information about records that failed to create." Không tạo xe, trên màn không nêu lý do; lỗi gửi qua email của người dùng đang đăng nhập.
- Form đơn: Vehicle Name và VIN đều "has already been taken", "Vehicle could not be created".
- Tên của xe đã Archive: không báo trùng tên, tức dùng lại được; chỉ VIN báo lỗi. Trùng VIN xét cả xe Sample.
- Dòng hợp lệ: chạy nền "Processing", rồi "Complete: Add Multiple Vehicles". Xe mới Active, Car, 0 km, tự giải mã VIN ra Honda, Accord, 2003.
- Gói lên 5 of 5: thanh đỏ, Add Vehicle khoá.
Màn mới: vehicle-add-multiple-step1 — images/vehicle-add-multiple-step1.jpg.
Không chạy được: Dán nhiều dòng vượt hạn mức, nhập Group mới: không thử vì vượt gói và tạo danh mục dùng chung.
Trả lời câu hỏi mở nào: OQ-11 phần trùng tên.
Dữ liệu TEST đã tạo: xe TEST-DAUKEO-2 (id 5892778). Thử dòng lỗi có thể đã sinh 1 email tới chính tài khoản người dùng, chưa kiểm hộp thư.

## Chỉ Operator được gán — Chạy
Các bước đã làm: Add Vehicle Assignment trên TEST-DAUKEO-2, gõ "TEST-SUA" vào ô Operator (liên hệ TEST-SUA-KTV chỉ phân loại Technician).
Kết quả thấy được: Không có liên hệ đó trong kết quả, chỉ có dòng "Create "TEST-SUA"" (không bấm). Không báo lý do. Trùng xe chặn, trùng người không chặn: như lượt trước.
Điều tra thêm: Ô Starting Odometer xám khi Start bằng thời điểm hiện tại lúc chưa chọn đủ, mở khi chọn ngày; có lần tự điền số hiện tại.

## Overview tuỳ biến — Một phần
Các bước đã làm: Ô tìm trường gõ "tire". Personalize, Manage Overview Layout, bỏ tick Recalls, Apply, kiểm thẻ, Restore defaults, Apply. Đọc trang Customize Layout, không sửa.
Kết quả thấy được: Tìm "tire" lọc còn nhóm Specifications, "4 results for "tire"", có "Clear search". Hộp layout: "Select which cards are visible for you. To change the card order between the two columns, drag and drop the visible cards." 15 thẻ. Bỏ Recalls thì thẻ mất ở trang xe, Restore defaults thì thẻ quay lại. Personalize còn Manage Tab Menu (không mở).
Customize Layout đưa vào Settings › Standard Records › Vehicle › Layout: "System Default", 4 Sections, 104 Fields, All (25) loại xe, nút Add Layout.
Không chạy được: Add Layout, sửa layout tài khoản: Cài đặt cấp tài khoản, brief cấm. Kéo đổi thứ tự thẻ: chưa thử.
Màn mới: vehicle-manage-overview-layout — images/vehicle-manage-overview-layout.jpg. Hộp thoại này che nền, thẻ vị trí chỉ hiện tên.
Dữ liệu TEST đã tạo: không; layout cá nhân đã về mặc định, đã kiểm thẻ Recalls hiện lại.

## Lịch sử trường, More Actions, loại xe, form 6 phần — Chạy (More Actions: Một phần)
Các bước đã làm: Trên TEST-DAUKEO-2 đổi Type Car sang Semi Truck, nhập Out-of-Service Date 03/11, Odometer 10. Xem View Record History. Mở Edit Vehicle Settings, Manage Inspection Forms.
Kết quả thấy được:
- Đổi loại xe tự do, không hỏi. Dòng phụ đầu trang đổi theo, trạng thái vẫn Active.
- Out-of-Service Date và Odometer KHÔNG đổi Status, KHÔNG tạo dòng đồng hồ (xe vẫn 0 km).
- Record History: "Type changed from Car to Semi Truck", "Out Of Service Date changed from (empty) to 2026-11-03", "Out Of Service Meter changed from (empty) to 10.0". Có lọc theo khoảng ngày. Xe mới có sẵn "Axle config created".
- Edit Vehicle Settings mở thẳng phần Settings của form. Manage Inspection Forms: thẻ từng biểu mẫu mang nhãn "Disabled", có menu "…", "View Submissions".
- Menu Add ẩn "Add Charging Entry" với xe Gasoline, xe chưa có Fuel Type thì có.
- Menu không có Recalculate Fuel trên 2 xe TEST đã mở (cả 2 không có Fuel Entry); chưa kiểm xe có Fuel Entry.
- Xe tạo qua Add Multiple: tìm trường thấy Front, Rear Tire Type P215/50R17 từ VIN; MSRP vẫn 0, khác bảng giải mã tay ($26,360.00).
Không chạy được: Manage Integration Links: tích hợp, brief cấm. Manage Service Programs, Attach Shared Document: chưa mở.

## Nhóm xe — Một phần
Các bước đã làm: Chọn nhóm Georgia / Atlanta (Sample) cho TEST-DAUKEO-2, lưu.
Kết quả thấy được: Ô chọn hiện cây cha / con. Lưu bị từ chối, toast "Vehicle could not be updated", dưới trường: "Selected group is a sample, and cannot be used with non-sample records." Dấu đỏ hiện ở mục Details dù đang đứng ở Lifecycle. Tìm "TEST" chỉ có "Create "TEST"" (không bấm).
Không chạy được: Gán nhóm thật, xem lịch sử đổi nhóm: tài khoản không có nhóm ngoài Sample; tạo nhóm là danh mục dùng chung, brief cấm.
Dữ liệu TEST đã tạo: không.

## Giải pháp đáng học, điểm yếu (lượt 3)
- Đáng học: Void hàng loạt phải gõ VOID, giữ nguyên lịch sử số cũ khi thay đồng hồ. Với đầu kéo thay đồng hồ, cách này hợp hơn xoá số.
- Đáng học: Archive có hiệu ứng rõ trên phân công: đóng cái đang chạy, xoá cái tương lai; có câu báo trước.
- Điểm yếu, không nên chép: Archive bị từ chối mà vẫn ngắt liên kết. Với cặp đầu kéo, mooc, người dùng mất quan hệ ghép mà không có dòng lịch sử nào. Thao tác phải trọn vẹn hoặc không có gì.
- Điểm yếu: Trạng thái xe không ràng buộc gì: xe Sold, Out of Service vẫn gán tài xế, mở lệnh. Delta cần luật chặn ở đây (đề xuất, chưa có quyết định).
- Điểm yếu: Mooc nối nhiều xe không có ngày hiệu lực, không biết đang kéo bởi đầu nào. Không đủ cho ghép đầu kéo, mooc theo chuyến.
- Điểm yếu: Lỗi tạo hàng loạt chỉ gửi email, màn hình không nói dòng nào sai; Restore khoá khi đầy gói không có lý do.

## Trạng thái cuối trên Fleetio (đã kiểm lại)
Vehicles 5 of 5, Add Vehicle khoá. TEST-XE-LOP đang Archived, Restore khoá vì đầy gói. Cấu hình trục, đồng hồ của xe Archived vẫn xem được, Edit trục khoá.

# Lượt 4 (03/11)

Gói xe 5/5, không tạo xe, không Restore. Xe dùng: TEST-DAUKEO-2 (brief chỉ giới hạn đổi trạng thái TEST-SUA-01, TEST-XE-01). Không lưu ảnh nào có bản đồ vị trí.
Liên kết với nhóm khác: xe này có Issue #54, #55 (TEST-NEN) của nhóm khác, không sửa. Trong lúc thử workflow xe đã qua Inactive, Out of Service vài phút rồi trả về Active; các automation TEST-NEN đang chạy song song có thể đã thấy những lần đổi đó.

## Add Multiple khi gói đầy — Không chạy được: mục khoá theo gói
Các bước đã làm: Danh sách xe, menu "...", rê chuột rồi bấm "Add Multiple Vehicles".
Kết quả thấy được: 5 of 5, mục xám có icon khoá, tooltip cuối câu "...to add more Vehicles.", bấm không mở form, không điều hướng. "Import Vehicles", "Import Meter Entries" không khoá. Chưa bấm các mục này.
Bất ngờ: Lối vào khoá ngay từ menu, nên chưa từng thấy form dán nhiều dòng trong gói đầy; không vào thẳng URL vì lock theo gói là điểm dừng của brief. Phần "dán nhiều dòng" vẫn chưa chạy.
Trả lời câu hỏi mở nào: không.
Dữ liệu TEST đã tạo: không.

## More Actions: Manage Service Programs, Attach Shared Document — Chạy
Các bước đã làm: TEST-DAUKEO-2, More Actions, Manage Service Programs; More Actions, Attach Shared Document, chọn TEST-NEN-tailieu.txt (tài liệu nhóm khác đã có), bấm Attach; mở panel Documents.
Kết quả thấy được:
- Menu đủ 8 mục: Edit Vehicle Settings, Manage Inspection Forms, Manage Service Programs, Manage Integration Links, Attach Shared Document, Recalculate Fuel Entries, View Record History, Archive.
- Manage Service Programs đi tới tab `vehicles/{id}/service_programs`. Xe chưa có bộ lịch: trang rỗng dạng quảng bá "Efficiently schedule and manage service needs for multiple vehicles", 4 gạch đầu dòng, nút "Create Service Program". Ở tab xe KHÔNG có nút gán bộ lịch sẵn có vào xe.
- Hộp "Attach Shared Document": "Performing this action will attach a shared document to 1 selected vehicle(s). View documents.", ô "Select Document" chỉ liệt kê tài liệu dùng chung (tên, loại, thời điểm sửa), "You may attach a shared document to any number of vehicles." Nút khoá tới khi chọn.
- Toast "Successfully attached shared document to vehicle." Panel Documents có thẻ tệp nhãn "Shared", ô kéo thả riêng cho tệp của xe.
Bất ngờ: Số "(1)" trên icon Documents trước đó không phải tài liệu của xe: sau khi đính panel mới có đúng 1 thẻ và huy hiệu đã tắt; chưa rõ huy hiệu ban đầu đếm gì.
Màn mới: vehicle-service-programs-empty — images/vehicle-service-programs-empty.jpg; vehicle-attach-shared-document — images/vehicle-attach-shared-document.jpg (Select Document, Cancel, Attach Shared Document).
Dữ liệu TEST đã tạo: Liên kết TEST-NEN-tailieu.txt với TEST-DAUKEO-2. Tài liệu dùng chung của nhóm khác, chỉ đính, không sửa.

## Đồng hồ phụ trên xe đang có số — Chạy
Các bước đã làm: TEST-DAUKEO-2 (đang 2.199 km), Edit Vehicle, Settings, "Add Secondary Meter". Lưu.
Kết quả thấy được: Mặc định Hours, xe hiện "Secondary Meter 0 hr" ở Fields, đầu trang "… km … hr". Nhập từ phiếu kiểm: chi tiết ở run-notes/reminders-inspection.md (Lượt 4).
Dữ liệu TEST đã tạo: TEST-DAUKEO-2 có đồng hồ phụ; hiện 2.500 km, 30 hr; trạng thái Active.

## Các dòng còn lại của nhóm xe — Chặn
- Overview, layout tài khoản (FR-005): sửa Customize Layout là Settings › Standard Records. Không sửa.
- Archive khi có đặt Motor Pool (FR-021): cần tạo Motor Pool trong Settings; gói đầy nên cũng không có xe riêng để thử. Câu chặn vẫn chỉ đọc.
- Nhóm mới (FR-025): tạo Group là danh mục dùng chung; Export Data thuộc xuất dữ liệu. Không làm.
- "Kể cả số GPS" khi đổi đồng hồ (FR-016): cần tích hợp GPS, brief cấm.
