# Ghi chú chạy thử — nhóm Sửa chữa (2026-11-03)

Xe: `TEST-SUA-01` (id 5891232, Car, tạo trống đồng hồ nên hiện "0 km"; ô Current Reading ở mục Settings gõ 10000 không vào được bản lưu). Đồng hồ đẩy dần qua sự cố lên 2.200 km.

## Sự cố: hạn, Overdue — Chạy
Các bước đã làm: Tạo #33 hạn ngày 11/01/2026; #34 đồng hồ 2000, hạn 2000; #35 đồng hồ 2200, hạn 2201; #36 hạn 2199; #37 hạn ngày đúng hôm nay; #38 hạn 2200 (đúng bằng số hiện tại). Sửa #33 sang hạn 12/31/2026.
Kết quả thấy được:
- Nhãn trên form: "Considered overdue after this date", "Considered overdue above this value".
- Cột "Issue Status" và trường Status hiện "Overdue" như một trạng thái, nhưng là giá trị tính: đổi Due Date của #33 sang tương lai thì Status về "Open" ngay, không có nút hay sự kiện chuyển trạng thái.
- Biên: đúng bằng ngưỡng đồng hồ (#38: 2200/2200) = Open; dưới ngưỡng 1 (#35: 2200/2201) = Open; vượt ngưỡng (#36: 2200/2199) = Overdue. Hạn ngày đúng hôm nay (#37) = Open.
- Tab Overdue lọc `q[state_scope]=overdue` còn 2 dòng (#34, #36).
Bất ngờ: Không có cảnh báo gì khi tạo sự cố đã quá hạn ngay từ đầu, không chặn hạn nằm trong quá khứ. Timeline không ghi sự kiện đổi Overdue.
Trả lời: FR-005 của nhóm Sửa chữa: Overdue là trạng thái hiển thị tính toán, không lưu.

## Sự cố: đóng, mở lại — Chạy
Các bước đã làm: More Actions (…) gồm "Close", "View Record History", "Delete". Close #36 không ghi chú; Close #38 có ghi chú; Reopen #38.
Kết quả thấy được:
- Hộp "Close Issue #36": Vehicle, Summary, Description, ô "Note" (không bắt buộc), "Describe why you're closing the issue.", nút "Close Issue".
- Sau đóng: Status "Closed", khối "Closed Details" gồm Closed Date, Closed By, Note. Đầu trang còn Unwatch, …, "Reopen"; mất Edit, mất Resolve.
- Ghi chú đóng cũng thành một Comment của người đóng.
- Reopen: hộp "Reopen Issue(s)": "Are you sure you want to reopen the selected issue(s)?", nút "Reopen Issue(s)". Sau đó về "Open", khối Closed Details biến mất, Comment vẫn còn, Timeline chỉ có "opened this issue" (không ghi đóng, mở lại).
- Toast "Issue #36 was closed." còn hiện khi đang ở trang #38: thông báo cũ nổi lại sang trang khác.
Màn mới: issue-close-dialog, issue-closed — ảnh images/issue-close-dialog.jpg, images/issue-closed.jpg.

## Sự cố: Resolve with Note — Chạy
Các bước đã làm: Resolve › "Resolve with Note" trên #35.
Kết quả thấy được: Hộp "Resolve Issue #35", "Note" bắt buộc (nút "Resolve Issue" khoá khi trống), gợi ý "Describe what work was performed to resolve the issue.". Sau khi lưu: Status "Resolved", khối "Resolution Details": Resolved Date, Resolved By, Note, "Time to Resolve" 5 mins, "Kilometers to Resolve" trống. Đầu trang còn "Reopen", mất Edit. Toast "Issue #35 was resolved.".
Khác nhau đáng chú ý: Close thì Note tuỳ chọn, Resolve with Note thì Note bắt buộc.
Màn mới: issue-resolve-note-dialog, issue-resolved-note — ảnh images/issue-resolve-note-dialog.jpg, images/issue-resolved-note.jpg.

## Sự cố: Add to Service Entry, Reopen sự cố đã resolved bằng entry — Chạy
Các bước đã làm: Resolve › "Add to Service Entry" trên #37; lưu entry 57856983 với Odometer 2100 (nhỏ hơn 2200 hiện tại); Reopen #37.
Kết quả thấy được:
- Hộp "Add to Service Entry": danh sách sự cố mở của xe, tick sẵn sự cố đang mở trang ("1 Issue will be added"), "Add to New Service Entry" | "Add to Existing Service Entry", "Continue". Sang form `service_entries/new?issue_ids=...`, toast "1 Issue(s) were added to the form".
- Form Service Entry: Odometer bắt buộc, Completion Date bắt buộc: ô hiện sẵn giờ hiện tại nhưng chỉ là placeholder, lưu không gõ thì báo "can't be blank", toast "Service Entry could not be created". Lúc đó Odometer không báo lỗi riêng cho tới khi gõ.
- Số 2100 nhỏ hơn 2200: lưu được, KHÔNG cảnh báo. Meter History thêm dòng "2,100 km · 100 km ago · Service Entry #57856983", đồng hồ hiện tại vẫn 2200.
- Entry không cần dòng việc nào: "No line items to show." Lưu vẫn resolve sự cố. "Assessment: Add a line item to run an assessment."
- Sự cố sau khi lưu: Status "Resolved", "Resolved Meter Entry" 2,100 km, Timeline "Issue Resolved by service entry" + link. Resolved By là người lưu.
- Reopen sự cố resolved bằng entry: nút KHÔNG khoá, chạy được ("Successfully reopened Issue."). Sự cố về Open, mục "Resolved Issues" của entry thành "No issues to show", entry vẫn còn nguyên. Timeline của sự cố vẫn giữ dòng "Issue Resolved by service entry" và không ghi lần mở lại.
Trả lời: khác SRS (states ghi "nút Reopen khoá"): khoá chỉ có thể với lệnh, entry thì không. Xem phần lệnh.
Dữ liệu TEST: Service Entry 57856983.

## Sự cố: Get Service at Shop — Không chạy được (cần bật Shop Network)
Kết quả thấy được: Bấm mở hộp "Streamline your outsourced maintenance with Shop Network": "Already included in your plan, there's no additional charge to use it.", "Nearly 100,000 vetted and trusted national and independant shops are in our network.", nút "Learn more", "Enable Shop Network". Dừng ở đây, không bật. Ảnh images/issue-shop-network.jpg.

## Form Work Order: trường, trạng thái, Priority Class, số lệnh — Chạy
Kết quả thấy được:
- Status mặc định 3 giá trị: "Open", "Pending", "Completed" (có dấu chốt). Repair Priority Class: "Scheduled", "Non-Scheduled", "Emergency", ghi chú "Repair Priority Class (VMRS Code Key 16) is a simple way to classify whether a service or repair was scheduled, non-scheduled, or an emergency."
- Có ô đồng hồ "Start Odometer" và tick "Use start odometer for completion meter" ("Uncheck if meter usage has increased since work order start date").
- Mục Issues: 3 tab Open, Resolved, Closed, cảnh báo "Select any issues that were resolved as part of this service"; cột Priority, Issue, Summary, Linked Line Items, Status, Labels, Assigned, Work Orders, Due Date, Due Meter. Overdue hiện chung tab Open.
- Mục Line Items: tab Service Tasks, Labor, Parts; "No Service Reminders"; dòng việc có Last Completed, Add Service Reminder, Add Labor, Add Part, Link Issues, MAINTENANCE CATEGORIZATION (Reason for Repair, Category / System / Assembly tự điền 1 Chassis, 013 Brakes, 017 Brake Parts).
- Số lệnh: ô hiện "101" là số dự kiến. Hai lệnh do agent khác lưu trước thì lệnh của tôi tự thành #103, không lỗi trùng.
Màn mới: wo-form-issues-lines, wo-add-part, wo-add-labor, wo-link-issues (ảnh tương ứng).

## Dòng phụ tùng: lỗi lệch tiền 100 lần (VND) — Chạy
Các bước đã làm: Add Part giá mặc định 300000; giá 5; sửa trong dòng giá 12.5. Add Labor chọn kỹ thuật viên mẫu rate; tạo TEST-SUA-KTV rate 100000.
Kết quả thấy được (đối chiếu từng màn):
| Nhập | Form trước lưu | Trang chi tiết sau lưu | Form sửa lại |
|---|---|---|---|
| Part 300.000 | 300.000,00 ₫ | 30.000.000 ₫ | 300.000 |
| Part 5 | 5,00 ₫ | 500 ₫ | 5 |
| Part 12,5 | 12,50 ₫ | 1.250 ₫ | 12,5 |
| Tổng Parts | 300.017,50 ₫ | 30.001.750 ₫ | ô parts_cost 30.001.750 nhưng dòng vẫn số cũ |
- Công: danh sách Technician ghi "480.000 ₫/hr" của Abraham McGlynn, chọn xong đưa vào dòng 4.800 ₫. Contact TEST nhập 100000 thì danh sách ghi "10.000.000 ₫/hr", hộp Edit Labor ghi "Current default labor rate is ₫100000.00".
- Kết luận chỉ từ quan sát: với VND không có số lẻ, mỗi màn nhân hoặc chia 100 khác nhau. Sau lưu Phần Parts bị ×100 ở cả số nhỏ, số thập phân; Công nhập tay qua hộp thì lưu đúng 4.800 (xem lại ở lệnh có TEST-SUA-KTV).
- Assessment AI cho lệnh giá 30 triệu vẫn "Acceptable" và nội dung chỉ bàn về sự cố, không bàn về giá.
Trả lời: xác nhận lỗi tiền 100 lần (bổ sung E-matrix).

## Kỹ thuật viên mẫu trên xe không mẫu — Chạy
Kết quả thấy được: Lúc tạo lệnh chọn contact Sample vào dòng công thì lưu được. Sau đó mọi lần sửa báo "Contact is a sample, and cannot be used with non sample vehicles"; đổi sang tech khác trong dòng cũ báo 422 `work_order_labor_line_items: is invalid`, toast "Work Order could not be updated". Đổi trạng thái: "Please edit and fix the following errors: Work Order Labor Line Items is invalid". Lệnh #103 kẹt, không đổi được status (không xoá được dòng công qua nút bút chì ở lần thử này).
Completed khi chưa có ngày bắt đầu: "Started At can't be blank" (hiện cùng lỗi trên).
Dữ liệu TEST: Contact TEST-SUA-KTV (id 3789401, không email, không user access, Technician, rate 100000). Lệnh #103 (Open, kẹt do dữ liệu mẫu).

## Sự cố tại form lệnh: tick không vào lệnh — Một phần
Tick #33, #34, #38 khi tạo #103; sau lưu "Resolved Issues" chỉ có #38, #33. #34 (Overdue, ưu tiên Medium) không vào, không báo gì. Chưa rõ nguyên nhân (kiểm lại ở lệnh sau).

## Sự cố cho tồn kho — Một phần
Lưu lệnh Open với dòng phụ tùng chọn location: form sửa hiện "TEST-KHO-01 (3)" từ 4. Tồn trừ ngay khi lưu, chưa cần Completed. Hộp Add Part ghi "This will make an inventory adjustment"; chọn "None (No Inventory Adjustment)" thì không.

## Lệnh: Open ↔ Pending, điều kiện hoàn thành, số đồng hồ — Chạy
Lệnh #104 (xe TEST-SUA-01, sự cố #35, #37, 1 dòng công TEST-SUA-KTV 100.000 ₫, 1 phụ tùng kho TEST-KHO-01).
Kết quả thấy được:
- Open → Pending: đổi trên đầu trang, toast "Work Order was successfully updated", không hỏi.
- Pending → Completed (thẳng, không qua Open) khi thiếu dữ liệu, lần lượt:
  1. Chưa có ngày bắt đầu: "Please edit and fix the following errors: Started At can't be blank".
  2. Có ngày bắt đầu, chưa có đồng hồ: "Starting Meter Entry can't be blank (per your account settings)", "Odometer can't be blank (per your account settings)". Trạng thái giữ nguyên.
- Form sửa, bỏ tick "Use start odometer" hiện "Completion Odometer". Gõ đồng hồ cuối mà chưa có "Actual Completion Date": ô ngày báo "can't be blank", toast "Work Order could not be updated".
- Số cuối nhỏ hơn đầu (2250 < 2300): banner "Completion Odometer must be greater than or equal to start meter entry.", API `ending_meter_entry: must be greater than or equal to start meter entry.`. Sửa thành 2350 mới lưu.
- Lưu 2 mốc đồng hồ tạo 2 dòng Meter History, nguồn "Work Order #104": 2.300 và 2.350. Không bắt buộc số cuối phải lớn hơn số hiện tại 2.200.
Sau khi Completed:
- Trang lệnh: Status "Completed", thêm trường "Service Entry #57857945", "Duration 2 minutes", "Odometer 2,300 km", "Completion Odometer 2,350 km", nút Edit khoá.
- Service Entry tạo tự động: Edit khoá, "Work Order #104", "Start Date", "Duration 2 mins", Odometer lấy số cuối 2.350, "Run Assessment" (khác lệnh là tự chạy), đủ Line Items và cột tiền ×100 như lệnh, "Resolved Issues" #35, #37.
- Sự cố #35: "Resolved", "Resolved Meter Entry" 2,350 km, "Time to Resolve" 23 mins, "Kilometers to Resolve" 150 km. Timeline "Issue Resolved by work order" + "added this issue to a work order". Nút Reopen khoá, tooltip "Reopen work order #104 to reopen this issue."
Màn mới: wo-completed — images/wo-completed.jpg; se-from-wo — images/se-from-wo.jpg; issue-reopen-locked — images/issue-reopen-locked.jpg.

## Lệnh: mở lại lệnh đã Completed — Chạy (OQ-4, OQ-5 nhóm Sửa chữa)
Các bước đã làm: Status › Open trên #104.
Kết quả thấy được:
- Hộp "Update Status": "Changing this completed Work Order to an incomplete Status will automatically restore any archived parts, part locations, and contacts associated with line items. Are you sure you wish to continue?" nút Cancel, Confirm. Câu hỏi KHÔNG báo Service Entry sẽ bị xoá và sự cố sẽ mở lại.
- Sau Confirm: toast "Work Order was successfully updated", rồi toast nền "Restoring Work Order #104 data". Trong vài giây, trang lệnh vẫn còn hiện Completed, phải chờ nền xong.
- Service Entry 57857945: mở lại URL ra "Not Found" ("the record may have been deleted"). XOÁ hẳn, không còn lịch sử xem được theo URL.
- Sự cố #35: về "Open", Edit + Resolve hiện lại, khối Resolution Details mất; Timeline xoá dòng "Issue Resolved by work order" (khác trường hợp entry: dòng cũ vẫn còn), còn dòng "added this issue to a work order". Time to Resolve mất cùng khối.
- Đồng hồ: 2 dòng 2.300 và 2.350 nguồn "Work Order #104" VẪN CÒN, số hiện tại vẫn 2.350. Mở lại không hoàn đồng hồ.
So với tài liệu hãng: khớp "entry bị xoá, sự cố mở lại". Tài liệu không nói đồng hồ, thực tế giữ nguyên.
Màn mới: wo-reopen-confirm — images/wo-reopen-confirm.jpg; se-deleted-not-found — images/se-deleted-not-found.jpg.
Dữ liệu TEST: lệnh #104; entry 57857945 tự bị xoá do thao tác mở lại (đúng quy định "ghi rõ").

## Bộ chọn sự cố trên lệnh: một sự cố ở 2 lệnh — Chạy
Form lệnh hiện mọi sự cố mở của xe, cột "Work Orders" ghi lệnh đang giữ (#103, #104). Dòng đã nằm ở lệnh khác KHÔNG có ô tick, thay bằng biểu tượng ổ khoá. Vậy từ form lệnh, một sự cố chỉ ở 1 lệnh. Ngay cả #34: trang #103 không ghi ở "Resolved Issues", nhưng cột Work Orders vẫn ghi #103 và bị khoá ở lệnh mới.
Sự cố tự sang Overdue khi đồng hồ tăng: #38 (hạn 2200), #35 (hạn 2201) sau khi đồng hồ lên 2350 đều hiện "Overdue", không ai thao tác.

## Tồn kho khi sửa, xoá, mở lại lệnh — Chạy (OQ-6)
Part TEST-BRAKE-PAD-01 (id 9420032), trang Inventory Activity:
| Thời điểm | Sự kiện | Điều chỉnh | Trước → sau |
|---|---|---|---|
| 1:10am | Lưu lệnh #103 (Open) có dòng chọn kho | -1 | 4 → 3 |
| 1:18am | Lưu lệnh #104 (Open) có dòng chọn kho | -1 | 3 → 2 |
| Mở lại #104 từ Completed | KHÔNG có dòng nào | 0 | 2 |
| 1:26am | Xoá dòng phụ tùng trong form sửa #104 rồi lưu | +1 | 2 → 3 |
- Tồn trừ lúc LƯU lệnh, không phải lúc Completed. Xoá dòng hoàn kho và có vết ghi nguồn "Work Order #104". Hộp xác nhận "Confirm Line Item Deletion": "Are you sure you want to permanently delete this line item?", nút "Delete Line Item". Toast "Removed Part: TEST-BRAKE-PAD-01".
- Tồn âm được: dòng cũ của #100 đưa 4 → -2, không chặn.

## Make a Copy — Chạy
Menu More Actions của lệnh: "Run Assessment", "Print", "Make a Copy", "View Record History", "Email PDF", "Delete". Make a Copy mở `work_orders/new?id=<id nội bộ>`, form trống Vehicle (phải chọn lại), Status Open, Issue Date = hiện tại, không chép ngày bắt đầu, hoàn thành, đồng hồ; chọn xe xong dòng việc và dòng công được chép (Labor 100.000), sự cố KHÔNG được chép. Không có số lệnh mới cho tới khi lưu. Ảnh images/wo-make-copy.jpg. Không bấm Email PDF.

## Draft Work Order bằng AI — Chạy
Các bước đã làm: Tạo #45 "engine oil leak near oil pan", #46 "left headlight not working". Resolve › Draft Work Order trên #46; xem nháp; bỏ tick một việc; Create new Work Order. Lần 2 trên #45: Discard.
Kết quả thấy được:
- AI tự gán ưu tiên từ câu tiếng Anh: #45 "High" ("Major functionality impaired"), #46 "Low" ("Minor Impact"). #34 câu tiếng Việt "Medium" ("Does not impair function"), #33/#35 "No Priority".
- Banner trên sự cố, chạy nền, đổi chữ: "Drafting service for this issue" › "Gathering vehicle details" › "Reviewing this issue" khoảng 40 giây; rời trang vẫn chạy. Xong: "Work Order drafted", "Ready for your review.", nút "Discard", "Review draft".
- Hộp "Review Work Order draft": cảnh báo "A Work Order is already open for this vehicle / Selected services can be added to Work Order #104, or to a new Work Order."; "Drafted from #46"; câu tóm tắt; "2/2 Service Tasks" + "Clear all"; "Est. Subtotal (0 of 2 estimated)" "No estimate available"; nhóm "Resolves this issue": Headlamp Bulb Replacement; nhóm "Also recommended for this vehicle": Engine Leak Inspection "Resolves TEST-SUA engine oil leak near oil pan" (AI tự gom sự cố khác cùng xe); "Will auto-fill when created": Repair Priority Class Non-Scheduled, Issue Date Today, WO Status Open; "Generated by AI just now. Was this helpful?"; nút Discard, "Add to" (menu "Add to Work Order #104", "Create new Work Order").
- Bỏ tick: "1/2 Service Tasks", nút đổi thành "Select all".
- Tạo: lệnh #106, toast "Work Order successfully created", "Created from an AI draft from Issue #46". Có việc Headlamp Bulb Replacement (kèm mô tả AI "Replace the left headlight bulb to restore front lighting.", phân loại 2 Electrical / 034 Lighting System / 004 Bulbs, Fuses & Wiring). Sự cố #46 vào lệnh, timeline "added this issue to a work order from an AI draft". Sự cố #45 bị bỏ tick KHÔNG vào.
- Sai với lời hứa: hộp ghi "Repair Priority Class Non-Scheduled" nhưng lệnh #106 trường đó trống "—".
- Discard trên #45: bấm là mất ngay, KHÔNG hỏi lại, không có ghi vết trên timeline.
Trả lời: FR-020 thêm chi tiết; state "Ready › Created/Discarded" đúng.
Màn mới: issue-draft-running, issue-draft-ready, wo-draft-review, wo-draft-add-menu, wo-from-draft (ảnh tương ứng).
Dữ liệu TEST: #45, #46, lệnh #106.

## Issue › Add to Work Order, gỡ sự cố — Chạy
- Trên #45 (chưa ở lệnh): mục menu mở TAB MỚI `work_orders/new?issue=...&vehicle=...`, Vehicle điền sẵn, sự cố tick sẵn. Lưu thành lệnh #107.
- Sự cố đã ở lệnh: menu Resolve còn dùng được "Draft Work Order", "Get Service at Shop"; 3 mục kia xám có khoá. Tooltip "Add to Work Order": "Issue already added to a Work Order. Remove it from all Work Orders to add it to another."
- Sửa #107 bỏ tick #45 rồi lưu: "Resolved Issues" về "No issues to show. If this work order resolves any issues, you can add them by editing the work order.". Timeline #45 cũng xoá dòng "added this issue", không để lại vết gỡ. #45 tự do thao tác lại.
Assessment theo điều kiện lệnh: chưa có việc "Add a service task to run an assessment."; có việc không có tiền "Add line item costs to run an assessment."; entry trống "Add a line item to run an assessment."; có tiền: tự chạy ("Reviewing this service", "Checking labor rates and times", "Reviewing parts and pricing", "Still working. Larger records can take a moment."), kết quả "Acceptable" + "Auto-assessed 3 minutes ago" + "6 sources" + "Was this helpful?".
Dữ liệu TEST: lệnh #107.

## Faults — Xem (chỉ dữ liệu Sample, không sửa)
Trang "Faults", "Fault Monitoring is on", tab All, Open, Pending, Resolved, Ignored; 16 dòng Sample. Cột: Vehicle, Code, Critical, Name, Description, Last Occurred Date, Status, Issue. Menu dòng: "Create Issue", "Ignore", "View Fault Rule". Xe TEST không có thiết bị nên không có mã lỗi. Không chạy hành động trên dữ liệu Sample.

## Work Order Statuses và Maintenance Settings — Xem, không đổi
- Statuses (`work_order_statuses`): Name, Type, # Work Orders. "Open" Default "Active and in progress" Incomplete; "Pending" "Active but waiting on parts or something else preventing completion" Incomplete; "Completed" "Finished - corresponding service reminders updated and issues resolved" Completed.
- Maintenance Settings (`account/maintenance_settings/edit`): "Enable Work Orders" bật; "Next Work Order Number" "Sets the next Work Order number. The current highest number is 105"; "Require a Meter Reading" bật ("If enabled, a meter reading (primary or secondary) must be present to save a Service Entry or completed Work Order"), có "Excluded Vehicle Types"; "Require Inspections to be submitted" (tắt); "Require a Repair Priority Class", "Require a Reason for Repair on Line Items", "Require Category on Line Items", 2 mục disable sửa mã mặc định: đều tắt. Ảnh images/maintenance-settings.jpg.
Điều kiện hoàn thành "Started At" và đồng hồ đầu nằm dưới "Require a Meter Reading". Vì không đổi Settings nên không kiểm mức "hoàn thành hết dòng".

## Hoàn thành lại lệnh đã mở lại — Chạy (OQ-4, OQ-5)
Các bước đã làm: #104 đang Open (đã từng Completed), bấm Completed lần 2.
Kết quả thấy được:
- Không giới hạn số lần ở 2 lần thử. Entry MỚI #57858956 (id khác entry đã xoá 57857945).
- Ngày, đồng hồ của lệnh được giữ từ lần trước, không hỏi lại, nên sự cố #35 hiện "Resolved Date 11/03/2026 at 1:21am", "Time to Resolve 23 mins" y như lần đầu, dù 41 phút sau mới hoàn thành lại. Timeline lại có "Issue Resolved by work order".
- Đồng hồ: thêm một dòng TRÙNG "2,350 km · Service Entry #57858956" bên cạnh dòng "2,350 km · Work Order #104". Lần đầu không có dòng nguồn entry. Vậy Completed nhiều lần có thể đẻ dòng đồng hồ trùng.
- Assessment đổi kết luận: "Needs Review", "Another open work order already includes Brake Pads Replacement. Confirm which one covers the job and close or merge the other." (AI soi lệnh khác cùng xe, cùng đầu việc).
Nhắc: nhóm Nhắc kiểm riêng, xe TEST-SUA không gắn nhắc nên case này KHÔNG kiểm được "nhắc đã reset".

## Print, Rerun Assessment, người được giao — Chạy
- Print là link `work_orders/103/pdf` mở tab mới, PDF `work_order_103.pdf` 2 trang (khung xem không render được trong tab tự động, chỉ thấy tên và số trang). Không bấm Email PDF.
- Menu đổi tên "Run Assessment" thành "Rerun Assessment" sau lần đầu; chạy lại ra "Assessed a few seconds ago". Lệnh #103 vẫn "Acceptable" với phụ tùng 30 triệu; câu ghi "the open overdue-by-date issue" trong khi #33 đã đổi hạn sang 12/31/2026, tức AI nêu sai thực tế.
- #106: Repair Priority Class chọn "Emergency", Assigned To chọn TEST-SUA-KTV (dropdown có nhãn "Technician"). Lưu được, không hỏi gì, người nhận không email nên không ai bị báo.
- Watch: người tạo lệnh, sự cố tự Unwatch (đã theo dõi). Người được giao không kiểm được có tự theo dõi không vì tài khoản không user.

## Đầu việc (Service Task) — Chạy, gộp: không có
- Tạo: form "New Custom Service Task" dạng 6 bước gập: Details, Fleetio Recommendations, Parts, Inspections, Expected Labor Hours, Maintenance Categorization. Nút "Save Service Task" KHOÁ cho tới khi bấm "Continue" hết các bước. Trùng tên: "has already been taken", toast "Service Task could not be created". Tạo được TEST-SUA-DV-A (51374091), TEST-SUA-DV-B (51374092).
- "Fleetio Recommendations" với tên tự đặt: "No Service Task Recommendation for ..."
- Danh sách: tab Active, Archived; 408 dòng (400 chuẩn + tự tạo). Chọn dòng: Actions có "Update Service Tasks", "Archive". More Actions có "Import Service Tasks", "Export Data...". KHÔNG thấy "Merge" ở các chỗ này.
- Archive DV-B: hộp "Confirm Service Task Archive": "Are you sure you want to archive this record? Archiving a record does not remove it from Fleetio, but it will no longer be usable." Toast "Successfully archived TEST-SUA-DV-B. Associated records will be updated in the background so allow a few minutes for your account to reflect these changes."
Dữ liệu TEST: 2 đầu việc trên (DV-B đã archive theo yêu cầu kiểm).

## Bảo hành trên lệnh — Một phần
Form New Warranty ghi rõ khi nào gợi ý: "Applying Maintenance Categorization to this Vehicle's coverage will surface claim opportunities when a Work Order form includes a Service Task with the same code". Trường: Vehicle, Coverage Template, Standard Warranty ("Typically provided by an OEM") | Extended Warranty ("Aftermarket coverage"), Warranty Name, Description, Manufacturer, Warranty Vendor, Contract ID, Vendor Link, Start Date, Coverage Duration (Years, Months), End Date, Start Meter, Coverage Distance (Unlimited), End Meter, Maintenance Categorization, Components. Trên #103, #104, #106 (xe không bảo hành): "No vehicle warranty opportunities to show.", "No part warranty opportunities to show.", "0 active 0 expiring soon 0 total". Không dựng thêm bảo hành cho TEST-SUA; ảnh gợi ý thật đã có từ lượt trước (images/wo-warranty-opportunity.jpg). Ảnh form: images/warranty-form.jpg.

## Xe TEST-SUA-02 — Không chạy được
Hai lần nhập tên, bấm Save Vehicle: nút khoá mãi, không về trang xe, không báo lỗi; danh sách vẫn chỉ TEST-SUA-01. Lần đầu tạo TEST-SUA-01 thành công cũng cùng cách. Không rõ nguyên nhân, có thể tài khoản đã chạm giới hạn xe. Toàn bộ case chạy trên TEST-SUA-01.

## Ma trận trạng thái: Sự cố (đo được)
| Trạng thái | Hành động làm được | Sang | Điều kiện, người làm | Hiệu ứng | Câu chữ nguyên văn | Mức |
|---|---|---|---|---|---|---|
| Open | Edit, Resolve menu (5 mục), Close, History, Delete | Resolved/Closed | Admin | Note đóng thành comment | "Close Issue" | Chạy |
| Overdue | Y hệt Open | | Ngày > Due Date hoặc đồng hồ > Due Odometer; tính tự động, không lưu | Hiện Issue Status, tab Overdue, vẫn thuộc nhóm Open (`state_scope=opened`) | "Considered overdue above this value" | Chạy |
| Open, đã gắn lệnh | Edit, Close?, Draft Work Order, Get Service at Shop; khoá Add to Service Entry, Add to Work Order, Resolve with Note | | Một lệnh giữ sự cố | | "Issue already added to a Work Order. Remove it from all Work Orders to add it to another." | Chạy |
| Resolved bằng ghi chú | Reopen, History | Open | Không điều kiện | Mất Resolution Details, comment giữ | "Reopen Issue(s)" | Chạy |
| Resolved bằng entry | Reopen (mở) | Open | Không điều kiện | Entry còn, mất liên kết; Timeline giữ dòng cũ | "Successfully reopened Issue." | Chạy |
| Resolved bằng lệnh | Reopen khoá | | Phải mở lại lệnh | | "Reopen work order #104 to reopen this issue." | Chạy |
| Closed | Reopen, History | Open | Không điều kiện | Closed Details mất, comment còn | "Are you sure you want to reopen the selected issue(s)?" | Chạy |

## Ma trận trạng thái: Lệnh sửa
| Trạng thái | Hành động | Sang | Điều kiện | Hiệu ứng | Câu chữ | Mức |
|---|---|---|---|---|---|---|
| Open | Edit, đổi status, Rerun, Print, Copy, Email PDF, History, Delete | Pending, Completed | Completed cần Started At + đồng hồ đầu | Tồn trừ khi lưu dòng kho | "Started At can't be blank" | Chạy |
| Pending | Như Open | Open, Completed | Như trên, không phải quay qua Open | Không có | "Work Order was successfully updated" | Chạy |
| Completed | Edit KHOÁ, đổi status mở | Open/Pending | Hộp xác nhận | Xoá entry, sự cố mở lại, đồng hồ GIỮ, tồn GIỮ | "Changing this completed Work Order to an incomplete Status..." | Chạy |
Trạng thái tuỳ biến: bảng ở `work_order_statuses` có 3 mặc định, chỉ đọc, không thêm.

## Ma trận trạng thái: Service Entry
| Nguồn | Sửa | Xoá khi | Liên kết sự cố | Mức |
|---|---|---|---|---|
| Tạo tay, từ sự cố | Edit được; lưu lại không đổi gì vẫn thành công | Không tự xoá | Reopen sự cố tháo liên kết | Chạy |
| Từ lệnh | Edit KHOÁ, "Run Assessment" | Mở lại lệnh, URL ra "Not Found" | Giữ tới khi mở lại | Chạy |

## Bảng case
| Case | Điều kiện | Kết quả thật | Ảnh |
|---|---|---|---|
| Hạn ngày đã qua | Tạo sự cố | Overdue ngay, không cảnh báo | — |
| Hạn đúng hôm nay | | Open | — |
| Hạn đồng hồ đúng bằng / trên 1 / dưới 1 | 2200 | Open / Open / Overdue | — |
| Đồng hồ tăng qua hạn | 2350 > 2201 | Tự thành Overdue | — |
| Đóng không note | | Được | issue-closed.jpg |
| Resolve note trống | | Nút khoá | issue-resolve-note-dialog.jpg |
| Reopen Closed | | Mở lại, không dấu vết timeline | — |
| Reopen resolved lệnh | | Khoá | issue-reopen-locked.jpg |
| Entry đồng hồ nhỏ hơn hiện tại | 2100 < 2200 | Lưu, không cảnh báo | — |
| Lệnh đồng hồ cuối < đầu | 2250 < 2300 | Chặn | — |
| Lệnh đồng hồ đầu < hiện tại? | Không chặn: 2300 > 2200 thật; chưa thử đầu < hiện tại | — | — |
| Thiếu ngày hoàn thành khi có số cuối | | "can't be blank" | — |
| Hoàn thành thiếu Started At | | Chặn | wo-complete-errors.jpg |
| Dùng start odometer | Tick mặc định | Ẩn ô số cuối | — |
| Part ×100 | Mọi cỡ số | Lưu xong hiển thị ×100 | wo-100x-after-save.jpg |
| Giá công qua contact | 100000 | Dropdown ghi 10.000.000 ₫/hr | — |
| Tech mẫu trên xe không mẫu | | Tạo được, mọi sửa về sau lỗi | — |
| Xoá dòng phụ tùng | | Tồn +1 có log | — |
| Mở lại lệnh | | Entry xoá, sự cố mở, đồng hồ + tồn giữ | wo-reopen-confirm.jpg, se-deleted-not-found.jpg |
| Hoàn thành lại | | Entry mới, ngày cũ, đồng hồ trùng dòng | — |
| Sự cố ở 2 lệnh | | Không được: ổ khoá, tooltip | issue-menu-locked-tooltip.jpg |
| Gỡ sự cố khỏi lệnh | | Được, không vết | — |
| Nhiều sự cố một lệnh | #35, #37 | Cùng resolved | wo-completed.jpg |
| Draft AI nhiều sự cố | | Gom thêm sự cố cùng xe | wo-draft-review.jpg |
| Bỏ chọn việc trong nháp | | Việc và sự cố đó không vào | — |
| Discard | | Mất ngay, không hỏi | — |
| Make a Copy | | Xe trống; chép dòng việc, không chép sự cố, ngày | wo-make-copy.jpg |
| Trùng tên đầu việc | | "has already been taken" | — |

## Luồng nghiệp vụ đo được
1. Lái xe/quản lý tạo sự cố (AI gán ưu tiên ngay). Hạn tuỳ chọn; đến hạn tự Overdue.
2. Ba rẽ nhánh chính từ menu Resolve: ghi chú (kết thúc ngay) | Service Entry (đóng sau khi lưu) | Work Order (tay hoặc AI). Hoặc Close nếu không làm.
3. Lập lệnh: thêm việc, công, phụ tùng. Lưu là tồn trừ, dù chưa làm.
4. Open ↔ Pending tuỳ ý. Completed cần Started At + đồng hồ theo cài đặt.
5. Completed sinh entry, resolve sự cố, khoá lệnh + entry + Reopen sự cố.
6. Sửa: mở lại lệnh (xoá entry, mở sự cố, giữ đồng hồ, tồn) → sửa → Completed lại (entry mới, dấu vết cũ mất).

## Giải pháp đáng học, điểm yếu
- Học: Overdue là giá trị tính, không phải trạng thái lưu: không có job đổi trạng thái, đúng cho hạn theo km của đầu kéo vì đồng hồ đổi liên tục.
- Học: một sự cố chỉ ở một lệnh, gắn lệnh thì khoá lối khác: tránh 2 xưởng cùng sửa một lỗi.
- Học: trừ kho từ lúc lưu dòng, xoá dòng có bút toán đảo ghi nguồn. Phù hợp xưởng cấp phụ tùng trước khi sửa.
- Học: AI nháp chạy nền + gom sự cố cùng xe + cảnh báo lệnh đang mở: đỡ đưa xe vào xưởng hai lần, quý với đầu kéo.
- Yếu: mở lại lệnh xoá hẳn entry, timeline sự cố mất dấu vết; Invlogis cần giữ vết (lịch sử, ai mở lại, vì sao).
- Yếu: mở lại không hoàn đồng hồ, hoàn thành lại tạo dòng đồng hồ trùng; Reopen giữ ngày cũ làm Time to Resolve sai với thực tế.
- Yếu: hộp xác nhận mở lại không nói entry sẽ bị xoá.
- Yếu: tiền lệch 100 lần với VND ngay trong màn chính: tiền tệ không có số lẻ phải test riêng khi bán đa quốc gia.
- Yếu: AI "Will auto-fill Non-Scheduled" không thật, Assessment bỏ qua giá 30 triệu và nêu sai "overdue-by-date".
- Mooc, đầu kéo: sự cố gắn với "Vehicle" đơn lẻ; mooc phải là một bản ghi xe riêng, lệnh không gom đầu kéo + mooc.

## Trả lời câu hỏi mở (nhóm Sửa chữa)
- OQ-4: không thấy giới hạn số lần mở lại ở 2 lượt; entry bị xoá thật, không có bản lưu xem được (Not Found).
- OQ-5: đồng hồ giữ nguyên, có dòng trùng khi hoàn thành lại; Time to Resolve mất khi mở, khi hoàn thành lại lấy ngày cũ của lệnh. Nhắc và tỷ lệ tuân thủ: chưa kiểm (xe không gắn nhắc).
- OQ-6: xoá dòng phụ tùng hoàn kho +1 và ghi Inventory Activity. Xoá lệnh: không làm (quy định). Tồn âm được.
- OQ-1,2,3,7,8,9: câu hỏi cho Delta, phần Fleetio: gom nguồn, một lệnh nhiều sự cố: có.

## Sai sót và bị chặn
- Tôi điều hướng nhầm 1 lần sang tab agent khác (961321018, đang ở `work_orders/101/edit`, nhóm Nhắc), đã back về `work_orders/101`; nếu họ có dữ liệu chưa lưu trên form thì có thể mất. Không ghi dữ liệu nào lên #101.
- Nhóm tab bị đóng khoảng 4 lần từ ngoài trong lúc chạy, mất form đang mở, phải làm lại.
- Khung nhìn đổi kích thước giữa chừng (1512 ↔ 2016 px), bấm toạ độ trật 1 lần (không ghi gì).
- Faults, Shop Network, trạng thái tuỳ biến: không chạy hành động; #103 kẹt do chọn contact Sample.
- Chưa làm: Add to Existing Service Entry (thấy ở hộp, chưa lưu), dựng bảo hành TEST-SUA, tick sự cố vào entry tay, biến thể xe (chỉ chạy Car).

# Lượt 3 (03/11)

Tab bị đóng từ ngoài 1 lần đầu lượt (cả nhóm tab mất, form chưa lưu mất), làm lại trên tab mới. Dữ liệu chỉ trên TEST-SUA-01.

## Ghi công: thêm công, Time Entry — Một phần (FR-009)
Các bước đã làm: Lệnh #107, thêm đầu việc TEST-SUA-DV-A, Add Labor: chọn TEST-SUA-KTV, tick "Set Labor Time Entry", bấm preset 2h, Save; lưu lệnh.
Kết quả thấy được: Hộp "Add Labor": Technician (bắt buộc), Labor Hours (mặc định 1, preset 15m 30m 45m 1h 2h 3h 4h), Hourly Rate, "Set Labor Time Entry" ("Set a specific date and time when this labor was performed to create a Time Entry"), Service Task ("Recommended for precise maintenance cost reporting."), Note, Subtotal, "Save and Add Another", "Save". Chọn kỹ thuật viên thì Hourly Rate tự điền 100000.00 theo contact. Tick Time Entry hiện Start Date, End Date; End = Start + số giờ, đổi preset 2h thì End nhảy từ 5:17pm sang 6:17pm. Lưu: dòng 200.000 ₫, chi tiết lệnh "( 2 hr ) x 100.000 ₫".
Bất ngờ: Form lệnh không có nút bấm giờ Start/Stop, chỉ nhập giờ tay và mốc thời gian. Bấm giờ thật như tài liệu hãng ghi: không thấy trên web ở form này.
Dữ liệu TEST đã tạo: dòng DV-A + công 2h trên #107.

## Tổng chi phí: markup, tín dụng bảo hành, giảm giá, thuế — Chạy (FR-010)
Các bước đã làm: #107 công 200.000, Labor Markup 10%, Warranty Credits cố định 20.000 rồi 30.000, Discount 5%, Tax 10%; lưu; đối chiếu trang chi tiết.
Kết quả thấy được: Chi tiết lệnh: Subtotal 200.000; "Labor Markup (10.0%)" + 20.000; "Warranty Credits (Fixed)" - 30.000; "Discount (5.0%)" - 10.000; "Tax (10.0%)" + 18.000; Total 198.000. Với credit 20.000: thuế 19.000, Total 209.000.
Thứ tự tính suy từ 2 bộ số: Discount tính trên Subtotal (5% của 200.000, không gồm markup); Tax tính trên 200.000 + 20.000 - credit - discount. Mỗi ô đổi được % hoặc số tiền.
Bất ngờ, lỗi: Trên form sửa, dòng Labor Markup hiện 2.000.000 ₫ trong khi Total và trang chi tiết dùng 20.000 ₫: lệch hiển thị 100 lần, cùng họ lỗi VND đã ghi ở dòng phụ tùng, nhưng Total vẫn đúng.

## Link Issues trên dòng việc — Chạy (FR-007)
Các bước đã làm: Dòng DV-A › "Link Issues", tick #45 (chưa gắn lệnh nào), Save.
Kết quả thấy được: Hộp "Link Issues" liệt kê sự cố của xe; #33, #34, #38, #46 hiện ổ khoá vì đã ở lệnh khác, tooltip "...to a Work Order. Remove it from ...orders to add it to another." (câu bị che một phần). Sau Save: #45 tự được tick ở khối Issues, cột Linked Line Items hiện TEST-SUA-DV-A, dòng việc có đếm 1 sự cố; chi tiết lệnh hiện #45 dưới cả "Resolved Issues" và dưới dòng DV-A.
Bất ngờ: Lệnh còn Open mà khối đã tên "Resolved Issues". Lần bấm đầu hộp đóng mà không tick vì bấm Save ngay sau tick quá nhanh, phải làm lại.
Dữ liệu TEST đã tạo: #45 gắn #107.

## Tình trạng từng dòng — Một phần (FR-017)
Form lệnh: menu dòng chỉ có "Change Service Task", "Add Service Reminder", "View Change Log", "View Service Task History", "Delete". Customize chỉ có Line Item Appearance, New Line Item Method, New Line Item Position. Trang chi tiết lệnh: dòng chỉ hiện Reason for Repair, Category / System / Assembly, kỹ thuật viên, giờ, tiền; KHÔNG có ô hay nút đánh dấu xong dòng. Tức trên web, tài khoản hiện tại không thấy tính năng này; không đổi Settings nên không biết có bật ở đó không. Giữ mức Docs cho phần "cấu hình bắt buộc xong hết".

## View Record History của lệnh — Chạy (FR-018)
Hộp "Record History": lọc "Select Date Range"; cột Date, Changes By, Changes Made. #107 ghi cả từng trường tiền ("Tax 1 changed from ₫0 to ₫18,000", "Labor Markup Percentage changed from 0.0 to 10.0", "Total Amount changed from ₫0 to ₫198,000"), "Service Line Item TEST-SUA-DV-A: Created", "Labor Sub Line Item TEST-SUA-KTV: Created", "Work Order created". Giữ sổ theo trường, khác Timeline của sự cố vốn không ghi đóng, mở lại. Không bấm Email PDF (gửi email). Không bấm Delete.

## Khoá trên sự cố đang gắn lệnh — Chạy (trả lời OQ-14, OQ-15 nhóm Sửa chữa)
Các bước đã làm: Trên #45 đang gắn #107: mở menu Resolve và More Actions, hover từng mục.
Kết quả thấy được: "Close" xám, tooltip "...already added to a Work Order. Remove it from all Work Orders to close". Resolve: "Add to Service Entry", "Draft Work Order", "Add to Work Order", "Resolve with Note" đều xám có khoá, tooltip "Issue already added to a Work Order. Remove it from all Work Orders to add it to another."; chỉ "Get Service at Shop" còn mở. "Delete" vẫn sáng (không bấm).
OQ-15: Close KHÔNG dùng được khi đang gắn lệnh. OQ-14: trên #45 Draft Work Order bị khoá nên không tạo được tình huống hai lệnh.
Điểm khác ghi chú lượt trước: lượt trước ghi "Draft Work Order" còn dùng được khi đã ở lệnh; lần này trên #45 nó xám. Chưa biết do lệnh, do #45 từng Discard, hay do hãng đổi; chỉ thấy trên #45.

## Add to Existing Service Entry — Chạy (FR-028, một phần OQ-16)
Các bước đã làm: Tạo #52, Resolve › Add to Service Entry › "Add to Existing Service Entry", chọn #57856983, Continue, Save Service Entry.
Kết quả thấy được: Chọn Existing hiện thêm ô chọn, nút Continue khoá tới khi chọn. Danh sách chỉ có entry của đúng xe (1 dòng "#57856983 11/03/2026"). Sang form sửa entry, toast "1 Issue(s) were added to the form". Lưu: #52 "Resolved", Timeline "Issue Resolved by service entry Service Entry #57856983". Resolved Date lấy theo ngày entry cũ 11/03/2026 1:04am, Resolved Meter Entry 2,100 km.
Bất ngờ, lỗi: "Time to Resolve" ra số âm "-15 hrs 16 mins" vì entry cũ hơn lúc báo sự cố. Không có cảnh báo, không chặn gắn sự cố báo sau vào entry đã làm trước đó. Trong hộp, sự cố đã gắn lệnh hiện ổ khoá, không tick được.
Màn mới: issue-resolved-negative-ttr — ảnh images/issue-resolved-negative-ttr.jpg — Resolution Details có Time to Resolve âm.
Dữ liệu TEST đã tạo: #52, gắn entry #57856983.

## Bảo hành dựng trên xe TEST-SUA, khớp đầu việc — Chạy (FR-025, FR-038)
Các bước đã làm: `warranties/new`: TEST-SUA-01, "TEST-SUA Bao hanh den", Start 01/15/2026, 1 Years, Start Meter 1000, Coverage 50000, Maintenance Categorization "034", "999". Lưu. Sửa mã thành "013", "034-004". Thêm Headlamp Bulb Replacement rồi Brake Inspection vào #107, lưu từng lần; xem #106 (đã có Headlamp từ trước).
Kết quả thấy được:
- Form đơn (`warranties/new`) khác form nhiều xe (`multiple/warranties/new`). End Date, End Meter ô xám tự tính khi gõ: 51000. Start Meter 1000 lưu đúng "1,000 km" (lỗi 1 km lượt trước không lặp lại).
- Trang bảo hành: End Date "01/14/2027" trong khi form hiện 01/15/2027, lệch 1 ngày. Dòng xe ghi "2,350 undefined" (lỗi đơn vị).
- Hộp "Add Maintenance Categorization": Bulk Mode, Column Mode; "Enter either a System code (000) or a System–Assembly code (000-001)"; 3 phần thì phần Component bị bỏ. Toast "VMRS codes have been updated". 999 không báo sai: ra "9 - Bulk Product Transfer, Handling & Storage Systems › 999 - Total Vehicle Assembly". Menu "…": "Edit", "Clear Codes".
- "Add Component": Component Name (bắt buộc), Description, "Use a component to itemize coverage within the Warranty. Ex. Powertrain, Axles, etc.". Đã mở, huỷ.
- Mã "034": #107 có Headlamp (3 / 034 / 004) vẫn "No vehicle warranty opportunities found.". Đổi sang "034-004" và "013", thêm Brake Inspection (1 / 013), lưu: "Warranty Opportunities (2)", cả Brake Inspection và Headlamp. Khả năng: mã hệ thống trần không khớp dòng có Assembly, hoặc do chưa lưu lại lệnh; 1 lần đo, chưa tách được.
- Tính lại theo lệnh: #106 có cùng Headlamp, không sửa lệnh, vẫn "No vehicle warranty opportunities to show." và "1 active ... 1 total". Tức cơ hội chỉ tính lại khi chính lệnh được sửa, không lan khi bảo hành đổi.
Bất ngờ: Form sửa ghi "Add complaint, cause, and correction details for claim processing.". Không có nút claim riêng ở chi tiết lệnh, chỉ "View Active Coverage" và 3 ô.
Dữ liệu TEST đã tạo: Warranty 356513; #107 thêm 2 dòng Headlamp, Brake Inspection.

## Điền hồ sơ bảo hành trên lệnh — Chạy (FR-038, OQ-16 phần claim)
Các bước đã làm: Sửa #107, khối Warranty Opportunities (2), điền Complaint, Cause, Correction cho Brake Inspection, lưu.
Kết quả thấy được: Form: "Add complaint, cause, and correction details for claim processing.", mỗi đầu việc khớp có "View Active Coverage", tên bảo hành, 3 ô chữ. Lưu xong chi tiết hiện đúng 3 nội dung. "View Active Coverage" và "Total vehicle coverage breakdown" chỉ là link sang `vehicles/5891232/warranties`.
Không có: nút "claim", trạng thái claim, gửi hãng, liên kết tự sang Warranty Credits. Đây là ghi chú trên lệnh, không phải quy trình claim. Warranty Credits vẫn nhập tay.
Màn mới: wo-warranty-claim-fields — ảnh images/wo-warranty-claim-fields.jpg — Warranty Opportunities (n), Vehicle Coverage, đầu việc, View Active Coverage, tên bảo hành, Complaint, Cause, Correction.
Dữ liệu TEST đã tạo: 3 ô chữ TEST trên dòng Brake Inspection của #107.

## Bỏ tick sự cố trong Service Entry — Chạy (OQ-16 phần entry)
Các bước đã làm: Sửa entry #57856983, tab Resolved trong khối Issues, bỏ tick #52, lưu.
Kết quả thấy được: #52 về "Open", mất Resolution Details, Timeline chỉ còn "opened this issue": không để lại vết đã từng resolved. Không hỏi xác nhận. #37, #35 trong entry có ổ khoá vì đang ở lệnh khác, không bỏ tick được từ đây.

## AI đóng sự cố khi có Service Entry — Một phần (FR-022)
Các bước đã làm: Tạo entry #57902070 cho TEST-SUA-01, đồng hồ 2350, dòng "Automatic Transmission Leak Inspection", ghi chú "TEST replaced rear seal, fixed transmission fluid leak", KHÔNG tick #52 "TEST-SUA transmission fluid leak at rear seal". Xem #52 ngay sau đó.
Kết quả thấy được: Entry "Resolved Issues": "No issues to show."; #52 vẫn Open, không gợi ý ở form hay trang chi tiết. Tính năng "Issue Resolution" có Manage trong Settings theo ghi chú nhóm nền tảng; không bấm vì có câu điều khoản.
Bất ngờ: Form entry mới không tự điền Completion Date dù ô mờ hiện ngày hôm nay: lưu báo "can't be blank", toast "Service Entry could not be created". Có khối "Smart Upload" Beta ở đầu form.
Dữ liệu TEST đã tạo: Service Entry #57902070.

## AI Draft khi một sự cố khác của xe đang ở lệnh — Chạy (FR-020, trả lời OQ-14)
Các bước đã làm: #52 Open (không gắn lệnh), Resolve › Draft Work Order. Xem hộp, "Add to" › "Create new Work Order". Xem lệnh mới và #45.
Kết quả thấy được:
- Menu "Add to": "Add to Work Order #107" ("Open · Updated 5 minutes ago") và "Create new Work Order".
- Nhóm "Resolves this issue": Automatic Transmission Leak Inspection. Nhóm "Also recommended for this vehicle": Engine Leak Inspection "Resolves TEST-SUA engine oil leak near oil pan" (#45, đang gắn #107).
- Tạo ra lệnh #110, toast "Created from an AI draft from Issue #52". "Resolved Issues" của #110 CHỈ có #52. #110 có cả dòng Engine Leak Inspection nhưng #45 không vào; #45 vẫn chỉ ở #107, Timeline không đổi.
OQ-14: Một sự cố vẫn chỉ ở 1 lệnh; AI gợi ý đè lên thì sinh dòng việc trùng mà không gắn sự cố.
Bất ngờ, lỗi: Câu AI "Both leaks were recently flagged and have no existing open work orders covering transmission or engine leak work." sai: #45 đang gắn lệnh mở #107. AI cũng không tính entry #57902070 vừa làm đúng việc "Automatic Transmission Leak Inspection" cách đó vài phút. Hộp hứa "Repair Priority Class Non-Scheduled" nhưng #110 trường đó "—" (lặp lại lần 2, lần đầu ở #106). Không hỏi xác nhận khi tạo dòng trùng.
Dữ liệu TEST đã tạo: lệnh #110, #52 gắn #110.

## AI Draft thêm vào lệnh đang có — Chạy (FR-020)
Các bước đã làm: Tạo #53 "TEST-SUA windshield wiper not working", Draft Work Order, Review draft, "Add to" › "Add to Work Order #110".
Kết quả thấy được: AI gán "Low". Xe đang có 4 lệnh mở (#103, #106, #107, #110) nhưng hộp chỉ nêu lệnh mới nhất "#110", không cho chọn lệnh khác. Toast "Work Order successfully updated", "Updated from an AI draft from Issue #53". #110 có thêm dòng Windshield Wiper Blade Replacement (mô tả AI), "Resolved Issues" có #52, #53. Phân loại AI: 0 / 002 / 035.
Dữ liệu TEST đã tạo: #53, gắn #110.

## Quy tắc khớp bảo hành theo mã và trạng thái — Chạy (FR-038, FR-025)
Các bước đã làm: Thêm 2 bảo hành Extended cho TEST-SUA-01: "TEST-SUA BH het han" (01/01/2024, 1 năm, Unlimited, mã 045-020), "TEST-SUA BH sap het" (11/05/2025, 1 năm, Unlimited, mã 027). Thêm dòng Automatic Transmission Filter Replacement vào #110, lưu. Rồi thêm mã 027 vào bảo hành Active 356513, xem #110 ở trang chi tiết, mở form, lưu.
Kết quả thấy được:
| Case | Điều kiện | Kết quả thật |
|---|---|---|
| Hết hạn | Status "Expired", dòng Engine Leak 4/045/020 trùng mã | Không gợi ý |
| Sắp hết hạn | Status "Expiring Soon" (hết 11/04/2026, còn 1 ngày), dòng 2/027 trùng mã | Không gợi ý, dù bảo hành còn hiệu lực |
| Active, mã hệ thống, dòng cùng mức | Mã 027, dòng Transmission Leak 2/027 | Gợi ý |
| Active, mã hệ thống, dòng sâu hơn | Mã 027, dòng Filter 2/027/036 | KHÔNG gợi ý |
| Active, mã hệ thống, dòng sâu hơn | Mã 034, dòng Headlamp 3/034/004 | KHÔNG gợi ý (lần đo trước) |
| Active, mã đủ 2 mức | Mã 034-004, dòng Headlamp 3/034/004 | Gợi ý |
Tức khớp đúng từng mức: mã hệ thống không bao trùm các assembly bên dưới, trái với cách đọc tự nhiên của "System code". Sắp hết hạn không gợi ý: 1 lần đo.
- Thời điểm tính: trang chi tiết lệnh giữ kết quả cũ ("No vehicle warranty opportunities to show."), mở form sửa thì hiện ngay "(1)", lưu thì chi tiết cập nhật. #106 không sửa nên vẫn trống. Đính chính mục trên: lý do Headlamp lần đầu không khớp là mã 034 trần, không phải chưa lưu.
- Đếm "1 active 1 expiring soon 3 total": Expired vẫn tính vào total.
- "Save & Add Another": giữ Vehicle, loại bảo hành, Start Date, Unlimited và cả mã Maintenance; chỉ xoá tên, thời hạn. Dễ lưu nhầm mã của bảo hành trước (tôi suýt lưu nhầm). Danh sách "Added Warranties" bên phải.
- Coverage Template trên TEST-SUA-01: "No options"; ô bật khi đã chọn xe. Bảng Warranty Templates trong Settings rỗng; không tạo ở Settings vì cấm. Không chạy được template.
- End Date: trang chi tiết đều trừ 1 ngày so với form (01/14/2027, 12/31/2024, 11/04/2026), trong khi bảo hành của TEST-XE-01 lượt trước ghi đủ năm 10/01/2026 đến 10/01/2027. Chưa rõ nguyên nhân.
Dữ liệu TEST đã tạo: Warranty "TEST-SUA BH het han", "TEST-SUA BH sap het" (356515); 356513 mã 013, 034-004, 027; #110 thêm dòng Filter.
Màn mới: vehicle-warranties-tab — ảnh images/vehicle-warranties-tab.jpg — tab Warranties của xe: Name, Manufacturer, Coverage Type, Start Date, End Date, Start Meter, Coverage Distance, End Meter, Status.

## Người theo dõi — Chạy (FR-033)
Các bước đã làm: #110 bấm biểu tượng người theo dõi, mở danh sách thêm, không chọn; bấm Unwatch rồi Watch.
Kết quả thấy được: Khung "Watching": "You're watching this record, so you will receive all Watched Notifications."; "WATCHERS · 1" Bảo Tín; "ADD WATCHER" ô "Search users", chỉ có "Fleetio Automation", "Service Advisor", cả hai xám có khoá. Unwatch: avatar biến mất, nút thành "Watch", không hỏi lại; Watch đổi lại "Unwatch". Lệnh tạo từ AI draft vẫn đặt người bấm thành người theo dõi. Xe không tự theo dõi: TEST-SUA-01 hiện "Watch".
#106 giao cho TEST-SUA-KTV (liên hệ, không phải user) vẫn "1 watcher": người được giao là liên hệ không thành người theo dõi. Người được giao là user thật: không chạy được vì không mời người ngoài.

## Mã lỗi, luật mã lỗi — Xem (FR-023, FR-024), chỉ dữ liệu Sample
Các bước đã làm: Mở menu dòng Faults, không chọn "Create Issue", "Ignore". Bấm "View Fault Rule" sang Settings › Fault Rules (11 dòng). Mở "Add Fault Rule" đọc trường rồi Cancel, không lưu. Đọc sự cố Sample #13.
Kết quả thấy được:
- Hộp "Add Fault Rule": Code (bắt buộc) "The Code value of an incoming Fault must precisely match this Code to trigger this Fault Rule."; Name, Description "This will overwrite any existing ... value for the incoming Fault."; Priority Handling (bắt buộc): "Off", "Ignore Code" ("Fleetio will automatically Ignore every occurrence of this Code for all Vehicles"), "Flag as Critical" ("...mark every incoming occurrence of this Code as Critical, and they will be given special attention on the account dashboard and vehicle profiles").
- Mã 2 hệ: OBD ("P0401") và SPN/FMI ("SPN 520672 FMI 1" có nhãn "Critical").
- Gom mã thành sự cố: #13 Sample "[Fault] Diesel Aftertreatment Restriction - DPF and EGR (P0401, P2002, P2459)", Reported By "AI Service Advisor", "Auto-assigned priority: High", Source liệt kê 3 dòng "Fault ...", tức 3 mã về 1 sự cố do AI lập. Đầu trang nêu Learn: "Integrate your telematics provider to automatically import Faults".
Không chạy được: "Create Issue", "Ignore" trên mã lỗi vì dữ liệu Sample và xe TEST không có thiết bị; lưu Fault Rule vì là danh mục dùng chung trong Settings.
Màn mới: fault-rules — ảnh images/fault-rules.jpg — menu Settings › Issues › Fault Rules, ô Search, cột Code, Description, nút Add Fault Rule.

## Nguồn sự cố — Một phần (FR-002)
Đã có: nhập tay, từ phiếu kiểm (lượt trước), đọc Source mã lỗi Sample (#13). Recall: chỉ đọc menu, không đổi. #52 tự nhập: Source "—".

## Recall — Xem (saas-platform-042), không đổi trạng thái Sample
Mở menu dòng, không chọn: "Acknowledge", "Create Issue", "Check VIN" (mở ngoài). Tab Needs Action 285 dòng (SRS ghi 261), tab All, Needs Action, Open, Resolved, Acknowledged. Learn: "Recalls are automatically imported from the NHTSA by year, make and model". Xe TEST không có Make nên không phát sinh recall để thử thật.

## Print lệnh — Một phần (FR-018)
`work_orders/107/pdf` mở `work_order_107.pdf` 2 trang, khung xem trong tab tự động vẫn trắng, không đọc được nội dung; không tải file. URL có token xuất: không ghi lại. Email PDF: không chạy, là gửi email.

## Không chạy được (lượt 3)
- FR-039, dòng Get Service at Shop của FR-003: cần Enable Shop Network, đổi Cài đặt. Vẫn thấy mục này sáng cả khi sự cố đang gắn lệnh.
- FR-036: tạo trạng thái lệnh tuỳ biến là danh mục dùng chung trong Settings.
- FR-017 phần cấu hình bắt buộc xong hết dòng: đổi Settings; web không có ô đánh dấu dòng.
- FR-022 phần bật Issue Resolution: Settings có câu điều khoản. Với cấu hình hiện tại, entry không đóng cũng không gợi ý đóng #52 (xem ngay sau khi lưu, chưa đợi lâu; #52 sau đó gắn #110).
- vehicle-039: Settings › Warranty Templates rỗng, tạo mẫu là đổi Settings; TEST-SUA-01 không có Make.
- FR-009 phần bấm giờ: không có nút Start/Stop trên web ở form lệnh và chi tiết lệnh.
- FR-010 Parts Markup với phụ tùng thật: không thêm phụ tùng vì kho TEST đang do nhóm khác đo tồn. Hộp Add Part đã mở, huỷ.
- Lệnh #103 kẹt: không đụng. Biểu mẫu #680174: không nộp. Không đổi trạng thái TEST-XE-LOP, TEST-MOOC-LOP; không tạo xe.

## Giải pháp đáng học, điểm yếu (lượt 3)
- Đáng học: khoá cứng sự cố đang ở lệnh, chỉ 1 lệnh giữ 1 sự cố, tooltip nói rõ cách gỡ. Với đầu kéo, mooc thì tránh hai tổ cùng sửa một lỗi.
- Đáng học: Record History theo từng trường tiền, đủ để đối soát khi Delta sửa lệnh đã tính chi phí.
- Đáng học: bảo hành gắn mã VMRS với đầu việc; xưởng thấy ngay cơ hội đòi hãng khi lập lệnh.
- Điểm yếu: khớp theo đúng mức mã, mã hệ thống không phủ assembly: khai bảo hành "toàn hệ thống động cơ" sẽ trượt phần lớn dòng. Nếu làm, nên cho mã cha phủ mã con.
- Điểm yếu: bảo hành Expiring Soon vẫn hiệu lực mà không gợi ý, đúng lúc cần đòi nhất.
- Điểm yếu: không có quy trình claim: Complaint, Cause, Correction chỉ là chữ, Warranty Credits nhập tay, không theo dõi hãng đã trả chưa.
- Điểm yếu: gắn sự cố vào entry cũ ra Time to Resolve âm, làm hỏng số liệu; nên chặn hoặc lấy mốc lúc gắn.
- Điểm yếu: AI nêu sai thực tế và sinh dòng trùng với lệnh đang mở, nên cần người duyệt như hộp Review đang làm.

# Lượt 4 (03/11)

Vẫn không đổi Cài đặt, không gửi email, không có người thứ hai. Không đổi trạng thái TEST-SUA-01.

## Markup phụ tùng với phụ tùng TEST — Chạy (FR-010)
Các bước đã làm: Lệnh #107 (đã có công 200.000, Labor Markup 10%, Warranty Credits cố định 30.000, Discount 5%, Tax 10%). Dòng TEST-SUA-DV-A › Add Part, TEST-KHO-PT-A, Part Location TEST-KHO-01, số 2. Đặt Parts Markup 20%, lưu; sửa đơn giá; đổi Parts Markup sang Fixed 15.000, lưu; xoá dòng phụ tùng, lưu.
Hộp Add Part: chọn phụ tùng mới hiện Part Location, chọn trong "None (No Inventory Adjustment)" hoặc nhóm "PULL FROM INVENTORY" kèm tồn từng kho ("TEST-KHO-01 (121)"); chọn kho hiện câu "This will make an inventory adjustment"; Unit Cost tự điền từ danh mục.
| Case | Parts | Parts Markup | Discount | Tax | Total trang chi tiết |
|---|---|---|---|---|---|
| 2 x đơn giá tự điền 100000.00, Markup 20% | 20.000.000 ₫ (sai 100 lần) | + 4.000.000 | - 1.010.000 | + 2.318.000 | 25.498.000 ₫ |
| Sửa ô đơn giá thành 1000, Markup 20% | 200.000 ₫ (đơn giá chi tiết 100.000 ₫) | + 40.000 | - 20.000 | + 41.000 | 451.000 ₫ |
| Markup Fixed 15.000 | 200.000 ₫ | + 15.000 | - 20.000 | + 37.000 | 422.000 ₫ |
| Xoá dòng phụ tùng, Fixed vẫn giữ | 0 ₫ | + 15.000 | - 10.000 | + 18.000 | 213.000 ₫ |
Công thức đối chiếu số thật: Parts Markup % tính trên Parts. Discount % tính trên Subtotal (công + phụ tùng, chưa markup). Tax % với markup %: (Subtotal + 2 markup - credit - discount) x 10%: 410.000 x 10% = 41.000.
Bất ngờ, lỗi:
- **Lỗi tiền phụ tùng 100 lần có hậu quả thật**: đơn giá tự điền 100000.00 lưu xong ra 10.000.000 ₫/cái ở trang chi tiết, làm sai cả Total. Phải nhập 1000 thì chi tiết mới 100.000 ₫. Form sửa và trang chi tiết đang lệch nhau đúng 100 lần với dòng phụ tùng; dòng công không lệch.
- Form sửa hiện Parts Markup 20% là 4.000.000 ₫ trong khi chi tiết 40.000 ₫ (lệch hiển thị như Labor Markup).
- **Markup cố định không vào cơ số thuế ở trang chi tiết**: Fixed 15.000: thuế 37.000 (= 370.000 x 10%, không gồm 15.000), trong khi xem trước trên form là 38.500. Markup % thì có vào cơ số. Đo 2 lần: 37.000 và 18.000, đều ra không gồm 15.000. Không biết hãng cố ý hay lỗi VND.
- Xoá hết phụ tùng, markup cố định vẫn cộng 15.000 trên Parts 0 ₫, không cảnh báo.
Hiệu ứng tồn kho:
| Thời điểm | Current Qty TEST-KHO-01 | WO Current Qty |
|---|---|---|
| Trước | 121 | 0 |
| Lệnh Open có 2 cái | **119** | 2 |
| Xoá dòng, lưu lệnh | **121** | 0 |
Tức trừ tồn ngay khi lưu lệnh Open, không đợi Completed; xoá dòng thì trả lại. Xoá dòng có hộp "Confirm Line Item Deletion": "Are you sure you want to permanently delete this line item?". Không có dấu vết trên form về số đã trả.
Dữ liệu TEST: dòng phụ tùng trên #107 đã xoá, tồn trả về 121 (thao tác tự xoá bản ghi TEST của mình). Parts Markup Fixed 15.000 còn trên #107, sẽ trả 0 ở bước sau.
Sau đó: Parts Markup của #107 đã đặt lại 0. Lệnh về Total 198.000 ₫ như trước khi thử. Loại markup vẫn Fixed.

## Giao lệnh cho user, người theo dõi — Chạy (FR-033)
Các bước đã làm: #107 Unwatch trước (WATCHERS còn 0). Edit, Assigned To, chọn chính tài khoản đang đăng nhập (user Account Owner), Save.
Kết quả thấy được: Lưu không hỏi. Chi tiết "Assigned To" = Bảo Tín; đầu trang nút đổi từ "Watch" thành "Unwatch"; khung "Watching" "WATCHERS · 1". Tức **user được giao tự thành người theo dõi**. So sánh lượt 3: giao cho liên hệ TEST-SUA-KTV không có quyền đăng nhập thì không thành người theo dõi.
Sửa mô tả FR-033: danh sách Assigned To **không chỉ người có nhãn Technician**: có cả Employee, Operator, Account Owner, cả "Fleetio Automation".
Chưa thử: người được giao là user thứ hai (chặn: không mời). Không kiểm được hộp thư nên không biết có email tự gửi cho chính tài khoản khi giao hay không.

## Print lệnh: đọc được PDF — Chạy (FR-018)
Các bước đã làm: Mở `work_orders/107/pdf` trong tab, không tải về máy; xem 2 trang.
Kết quả thấy được: `work_order_107.pdf`, 2 trang. Đầu trang tên, địa chỉ tài khoản; góc phải Work Order Number, Invoice Number, PO Number. Khối "WORK ORDER DETAILS": Issue Date, Scheduled Start Date, Actual Start Date, Expected Completion Date, Actual Completion Date, Duration, Repair Priority Class, Status, Issued By, Assigned to, Vendor, Labels; bên phải tên xe, VIN/SN, License Plate, Operator, Type, Group, Odometer. "LINE ITEMS": Item, Labor, Parts, Subtotal; dòng công "TEST-SUA-KTV (Contact)" 2 hrs ₫100,000; dòng sự cố "#45 · ...". Trang 2 "DESCRIPTION", "SUMMARY": Subtotal, Labor, Parts, Labor Markup + ₫20,000 (10.0%), Parts Markup + ₫0 (Fixed), Warranty Credits - ₫30,000 (Fixed), Discount - ₫10,000 (5.0%), Tax +₫18,000 (10.0%), Total ₫198,000. Chân trang "Powered by Fleetio", "Page 1 of 2".
Bất ngờ: Issue Date PDF "Mon, Nov 2, 2026 12:32 PM" trong khi web hiện 11/03/2026 1:32am: PDF theo múi giờ tài khoản (America/Chicago), web theo máy (Asia/Saigon), lệch sang cả ngày khác. Tiền PDF dạng US (₫198,000), web dạng 198.000 ₫. Không in Complaint, Cause, Correction của bảo hành trong phần đọc được.
Màn mới: wo-print-pdf — ảnh images/wo-print-pdf.jpg (cắt bỏ phần đầu có địa chỉ tài khoản) — bố cục như trên.
Không chạy: Email PDF (gửi email). Delete (không xoá). FR-018 còn đúng 2 mục đó.

## AI đóng sự cố: thử lại, đợi lâu hơn — Một phần (FR-022)
Các bước đã làm: (a) Đọc lại #52 khoảng 1 đến 2 giờ sau entry #57902070 nội dung khớp. (b) Tạo #59 "TEST-KHO brake pads squealing, needs brake inspection" trên TEST-KHO-01, rồi entry #57903452 (dòng Brake Inspection, ghi chú "TEST replaced brake pads, fixed the squealing"), KHÔNG tick #59. Đọc lại sau khoảng 15 phút.
Kết quả thấy được: #52 vẫn Open. #59 vẫn Open; AI xếp Priority "High". Entry #57903452: "Resolved Issues" · "No issues to show." · "If this service entry resolves any issues, you can add them by editing the service entry."; không có gợi ý. Form entry liệt kê #59 ở tab Open với "Select any issues that were resolved as part of this service", không tự tick.
Trả lời: với cấu hình hiện tại, sau chừng ấy thời gian AI không đóng, không gợi ý đóng. Chặn phần còn lại: bật Issue Resolution là đổi Settings, có câu điều khoản; chưa biết trạng thái bật thật của tài khoản này.
Dữ liệu TEST đã tạo: Issue #59; Service Entry #57903452 (TEST-KHO-01, 5.320 km). AUTO-07 lúc này đã tắt nên không comment trên entry này.

## Không chạy được (lượt 4)
- FR-002 Recall: đổi trạng thái Sample, xe TEST không có Make. Fault tạo sự cố: cần thiết bị.
- FR-003 Get Service at Shop: cần Enable Shop Network, đổi Cài đặt.
- FR-017: web không có ô đánh dấu dòng; cấu hình bắt buộc xong hết dòng là đổi Settings.
- FR-025 Warranty Templates: Settings rỗng, tạo mẫu là đổi Settings.
- FR-009 bấm giờ: web không có nút Start/Stop; báo cáo `work_orders/labor_time_entries` chỉ lọc Contacts, Started at, Ended at.

## Giải pháp đáng học, điểm yếu (lượt 4)
- Đáng học: trừ tồn ngay khi lưu lệnh Open và có WO Current Qty riêng; xoá dòng trả lại. Xưởng thấy ngay hàng đã giữ cho lệnh đang sửa.
- Đáng học: giao việc cho user tự thành người theo dõi; liên hệ không đăng nhập thì không.
- Điểm yếu nặng: đơn giá phụ tùng lệch 100 lần giữa form và chi tiết với VND. Invlogis phải lưu tiền theo số lẻ của từng loại tiền, không cứng 2 số lẻ.
- Điểm yếu: markup cố định và markup % xử lý cơ số thuế khác nhau; xem trước trên form ra 38.500, sau khi lưu ra 37.000.
- Điểm yếu: PDF theo múi giờ tài khoản, web theo máy: một lệnh hiện 2 ngày khác nhau.

# Lượt 5 (03/11)

Giá trị Cài đặt trước khi đổi: Work Order Statuses: Open (Default, xanh ngọc, Incomplete, 13 lệnh), Pending (cam, Incomplete, 1), Completed (xanh lá, Completed, 97). Warranty Templates: rỗng. Shop Network: chưa bật.

## Trạng thái lệnh tuỳ biến — Chạy (FR-036, OQ-16 phần trạng thái tuỳ biến)
Các bước đã làm: Add Work Order Status: để trống, trùng tên, tạo 2 trạng thái; đưa #106 qua từng trạng thái; thử đổi loại khi đang dùng; đổi Default rồi trả về.

Form "Add Work Order Status": Name *, Description, ô "Completed", ô "Default", Color (17 màu + không màu). Ghi chú "Custom names are created the same in all languages. Future edits will only affect the current language". Không có ô cấu hình hiệu ứng, thứ tự chuyển, người được chuyển: **loại chỉ có 2, chọn bằng 1 ô tick**.

| Case | Điều kiện | Kết quả thật | Ảnh |
|---|---|---|---|
| Thiếu tên | Name trống | "can't be blank", toast "Work Order Status could not be created" | |
| Trùng tên | Name "Open" | "has already been taken" | |
| Tạo loại Incomplete | "TEST-SUA Cho phu tung", không màu | "Work Order Status was successfully created"; cuối bảng, ô tick thay cho khoá vì chưa dùng | wo-status-custom-list |
| Tạo loại Completed | "TEST-SUA Xong cho nghiem thu", tím | Cột Type "Completed" có dấu tick đen | wo-status-custom-list |
| Lan ra màn khác | | Có ngay trong menu trạng thái trên lệnh, form lệnh, bộ lọc Status; loại Completed có huy hiệu riêng. **KHÔNG tự thêm tab** trên danh sách lệnh (vẫn All, Open, Pending, Completed) | |
| Sang Incomplete tuỳ biến | #106 Open | Cập nhật ngay, Status Updates ghi "updated status from Open to TEST-SUA Cho phu tu..."; số lệnh Open 13 sang 12 | |
| Sang Completed tuỳ biến, thiếu dữ liệu | #106 không Started At | Bị chặn như Completed gốc: "Please edit and fix the following errors: Started At can't be blank" | |
| Sang Completed tuỳ biến, đủ dữ liệu | #106 có ngày, đồng hồ 2.360, 2.365 | Hiệu ứng y Completed gốc: sinh Service Entry #57906551, Edit xám. Không có bước riêng nào cho "chờ nghiệm thu" | |
| Giữa 2 trạng thái Completed | Tuỳ biến sang Completed gốc | Không hộp thoại, **vẫn Service Entry cũ** #57906551, không sinh thêm | |
| Completed sang Incomplete tuỳ biến | | Hộp "Update Status": "Changing this completed Work Order to an incomplete Status will automatically restore any archived parts, part locations, and contacts associated with line items. Are you sure you wish to continue?"; Confirm: Service Entry biến mất (URL 404), toast "Complete: Restoring Work Order #106 data". Hộp không nói sẽ xoá Service Entry | |
| Đổi loại khi đang dùng | Tick Completed trên trạng thái có 1 lệnh | "cannot be changed if work orders are assigned", toast "Work Order Status could not be updated" | |
| Đổi Default | Tick Default trên TEST-SUA Cho phu tung | Huy hiệu Default chuyển hẳn sang, Open mất Default (mỗi lúc 1). Form New Work Order chọn sẵn trạng thái mới. **Đã trả Open về Default** | |
| Khoá theo số lệnh | Có lệnh dùng | Ô tick thành ổ khoá, tooltip "...that are being used cannot be deleted."; menu "..." có Edit, Delete xám có khoá | wo-status-custom-list |
| Trạng thái gốc | Open, Pending, Completed | Sửa được tên, mô tả, màu; đang có lệnh nên khoá Delete | |

Không kiểm: kéo sắp xếp (nút "Drag to reorder" có sẵn); Service Reminder cập nhật khi Completed tuỳ biến (lệnh #106 không gắn nhắc); hành vi Delete (cấm xoá).

| Trạng thái | Hành động làm được | Sang trạng thái | Điều kiện, người làm | Hiệu ứng lên đối tượng khác | Câu chữ nguyên văn | Mức |
|---|---|---|---|---|---|---|
| Incomplete bất kỳ (gốc, tuỳ biến) | Đổi trạng thái | Incomplete bất kỳ | Không ràng buộc thứ tự | Chỉ ghi Status Updates | "Work Order was successfully updated" | Chạy |
| Incomplete bất kỳ | Đổi trạng thái | Completed bất kỳ | Đủ Started At, đồng hồ | Sinh Service Entry, khoá Edit, sự cố gắn lệnh coi là đã xử lý | "Started At can't be blank" | Chạy |
| Completed bất kỳ | Đổi trạng thái | Completed khác | Không hỏi | Giữ Service Entry | | Chạy |
| Completed bất kỳ | Đổi trạng thái, Confirm | Incomplete bất kỳ | Có hộp xác nhận | Xoá Service Entry, khôi phục bản ghi lưu trữ | "Changing this completed Work Order..." | Chạy |

Màn mới: wo-status-custom-list — ảnh images/wo-status-custom-list.jpg — Add Work Order Status, ô tìm, Name kèm chấm màu + huy hiệu Default + mô tả, Type, # Work Orders (link theo trạng thái, kèm số lệnh xe đã Archive), ô tick hoặc khoá, Drag to reorder, menu Edit, Delete.
Trả lời câu hỏi mở nào: OQ-16 phần trạng thái tuỳ biến của nhóm Sửa chữa.
Dữ liệu TEST đã tạo: trạng thái "TEST-SUA Cho phu tung" (Incomplete, 0 lệnh sau khi trả), "TEST-SUA Xong cho nghiem thu" (Completed, 0 lệnh). KHÔNG xoá được theo ràng buộc, còn lại trong danh sách trạng thái, xuất hiện ở mọi menu trạng thái lệnh. #106 trả về Open, nhưng nay có Actual Start, Actual Completion Date, đồng hồ 2.360, 2.365.
Trả lại Cài đặt: đọc lại cuối lượt: Open Default, 13 lệnh; Pending 1; Completed 97; 2 trạng thái TEST 0 lệnh, đã về ô tick (hết khoá).

Giải pháp đáng học, điểm yếu:
- Đáng học: tên trạng thái do khách đặt, nghiệp vụ gắn vào 2 loại cố định; đúng mô hình "Lõi khung + Cấu hình tên". Khớp `docs/_product/saas-core-vs-tenant.md`.
- Đáng học: khoá đổi loại và xoá khi đã có lệnh dùng, tránh lịch sử sai nghĩa.
- Điểm yếu: không khai được thứ tự chuyển hay vai trò; lệnh có thể nhảy thẳng từ "Chờ phụ tùng" sang Completed. Logistics cần quy trình duyệt thì phải làm ở phân quyền hay tự động hoá khác.
- Điểm yếu: nhiều trạng thái loại Completed không khác gì nhau về hiệu ứng, "chờ nghiệm thu" đã sinh Service Entry và khoá lệnh.
- Điểm yếu: hộp mở lại không báo xoá Service Entry.
- Sau khi mở lại, sự cố #46 quay về tab Open của Issues, trên lệnh vẫn nằm ở khối "Resolved Issues".

## Mẫu bảo hành (Warranty Templates) — Chạy (FR-025, vehicle-039)
Các bước đã làm: Settings › Warranty Templates › Add; tạo mẫu 2 coverage; New Warranties chọn Standard templates trên TEST-SUA-01; mở thử trên xe Sample không lưu; sửa mẫu rồi áp lại về bảo hành đã tạo.

Form "New Warranty Template": Name *, Meter Unit * (Miles, Kilometers, Hours). Coverage Details có đủ trường như bảo hành thường: Warranty Name *, Coverage Type (Standard, Extended), Description, Coverage Duration * (Years, Months), Coverage Distance * hoặc Unlimited, Manufacturer, Warranty Vendor, Contract ID, Vendor Link, Maintenance Categorization. Nút "Create & Add Another", "Create Coverage". "Save Warranty Template" xám tới khi có ít nhất 1 coverage. Danh sách: Name, Manufacturer, # Coverages; menu Edit, Duplicate, Delete (Delete không khoá dù mẫu đang dùng; không bấm).

| Case | Điều kiện | Kết quả thật | Ảnh |
|---|---|---|---|
| Mẫu riêng trên xe km | TEST-SUA-01, mẫu Kilometers | Trước đây "No options", nay nhóm "CUSTOM TEMPLATES" có mẫu. Không còn phụ thuộc Make vì xe không có Make | warranty-template-list |
| Xem trước | Chọn mẫu | "Coverage preview" liệt kê coverage; mỗi dòng có Edit, Edit Maintenance Codes, Delete, sửa riêng lần này được | warranty-template-preview |
| Áp mẫu | Save Warranties | "Warranties have been successfully created"; **sinh 2 bảo hành riêng**: Standard 11/03/2026–11/03/2028, Extended 11/03/2026–05/03/2027, Unlimited km | |
| Mã bảo dưỡng theo mẫu | Coverage có 034-004 | Form sửa #106 hiện thêm cơ hội "TEST-SUA BH mau co ban" cạnh "TEST-SUA Bao hanh den" | |
| Xe Sample có Make | BSA100TRNS, Freightliner Cascadia, mi; không lưu | "OEM TEMPLATES" 14 mẫu xe con (Ford F-150, Transit, F-250, F-350, F-550; Chevrolet Silverado 1500, 2500HD). **Không lọc theo Make**, xe Freightliner vẫn thấy Ford. **Không có mẫu đầu kéo**. Không thấy mẫu km riêng của mình | warranty-oem-template-preview |
| Mẫu OEM | 2025 Ford F-150 | Bumper to Bumper 3 năm 36.000 mi, Powertrain 5 năm 60.000 mi, Safety Restraint System 5 năm 60.000 mi, Corrosion 5 năm Unlimited,... (có thêm dòng dưới, không đọc hết) | warranty-oem-template-preview |
| Xe km gặp OEM | TEST-SUA-01 | Không thấy nhóm OEM. Suy ra lọc theo đơn vị đồng hồ (xe mi thấy OEM mi, xe km thấy mẫu km); **suy luận từ 2 lần quan sát**, chưa thử mẫu Miles trên xe mi | |
| Sửa mẫu đã dùng | Coverage 2 năm thành 3 năm | Hộp "Template Change": "Apply to assets this template is added to in the future" (mặc định) · "Apply to all historical and future assets with this template" | warranty-template-change |
| Áp về quá khứ | Chọn lựa chọn 2 | Cảnh báo "1 asset with coverage "TEST-SUA BH mau co ban" applied will be updated. Please note that any coverage edits made to individual assets will be overwritten."; lưu mẫu: End Date đổi thành 11/03/2029. **Mẫu liên kết với bảo hành đã sinh** | |
| Lỗi nhập Start Meter | Form New Warranties, gõ 2365 | Ô chỉ giữ "2": lúc gõ ký tự đầu, dòng hiện thêm nút sao chép, ô mất tiêu điểm. Lưu ra Start Meter 2 km, End Meter 100.002 km, Fleetio không cảnh báo lệch với đồng hồ xe 2.365. Có thể do gõ tự động nhanh; chưa thử tay. Lặp 2/2 lần | |

Chưa làm: lựa chọn 1 "future" (không đổi mẫu thêm); ghi đè bảo hành đã sửa riêng ở lựa chọn 2 (chỉ có câu cảnh báo); xoá mẫu (cấm).

Màn mới: warranty-template-list, warranty-template-preview, warranty-oem-template-preview, warranty-template-change — ảnh cùng tên trong images/.
Trả lời câu hỏi mở nào: Coverage Template "No options" ở lượt 4: do chưa có mẫu đúng điều kiện, không phải do thiếu Make.
Dữ liệu TEST đã tạo: mẫu "TEST-SUA Mau bao hanh" (id 10246, Kilometers, 2 coverage, Standard hiện 3 năm), bảo hành "TEST-SUA BH mau co ban", "TEST-SUA BH mau mo rong" trên TEST-SUA-01 (Start Meter sai 2 km, giữ nguyên làm bằng chứng). Không xoá được theo ràng buộc; mẫu còn trong Settings.
Trả lại Cài đặt: không trả về rỗng được vì cấm xoá; đã báo.

Giải pháp đáng học, điểm yếu:
- Đáng học: mẫu bảo hành có lựa chọn tương lai hay cả quá khứ, kèm số xe bị ảnh hưởng trước khi áp. Áp được cho mẫu giá thuê, định mức, chính sách của Invlogis.
- Đáng học: áp mẫu cho nhiều xe một lượt, mỗi xe một ngày và đồng hồ bắt đầu.
- Điểm yếu: áp về quá khứ ghi đè cả phần sửa riêng từng xe; chỉ có cảnh báo, không so sánh trước sau.
- Điểm yếu: thư viện OEM thuần xe con Mỹ, vô dụng với đầu kéo, mooc Việt Nam; mẫu riêng của khách mới có giá trị.
- Điểm yếu: không chặn Start Meter lệch xa đồng hồ xe.

## Shop Network: bật — Không chạy được (Access Denied ở bước thiết lập Fleetio Pay)
Các bước đã làm: Sự cố #46, Resolve, Get Service at Shop, bấm "Enable Shop Network" 1 lần. Không thử URL khác, không thử lại.
Kết quả thấy được:
- Hộp giới thiệu: "Shop Network features a suite of automations designed to make outsourced maintenance easy. Choose a shop from the directory and leave approval, data entry, and invoicing to us."; 3 bước "Choose an in-network shop", "Service automatically logged", "Review, approve, and resolve"; "Already included in your plan, there's no additional charge to use it."; "Nearly 100,000 vetted and trusted national and independent shops are in our network."; nút "Learn more", "Enable Shop Network".
- Bấm Enable: **chuyển sang `fleetio_pay/account_setup/new`**, trang "Access Denied" · "You do not have access to the requested URL.". Không có hộp điều khoản, hợp đồng, phí nào hiện ra.
- Trạng thái sau: mở lại Get Service at Shop vẫn hộp giới thiệu, nghĩa là **chưa bật**. Không có gì phải trả về.
- Phát hiện: bật Shop Network đi qua thiết lập tài khoản thanh toán Fleetio Pay. Đây là thanh toán, thuộc phần cấm, nên dừng. Vì sao bị từ chối (gói dùng thử, vị trí, quyền) chưa biết.
- Khác lượt trước: trên #46 đang gắn lệnh, menu Resolve nay khoá cả "Draft Work Order"; chỉ "Get Service at Shop" sáng.
Không chạy được: chọn cửa hàng, gửi yêu cầu, ghi service tự động, duyệt báo giá, hoá đơn (FR-003 dòng Get Service, FR-039). Find a shop trên nhắc (reminders-inspection-007): Shop Network chưa bật nên không có gì mới so với lượt 4, không mở lại; bước cuối Assign gửi email, SMS thật.
Màn mới: shop-network-enable-denied — ảnh images/shop-network-enable-denied.jpg.
Dữ liệu TEST đã tạo: không.
