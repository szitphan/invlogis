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
