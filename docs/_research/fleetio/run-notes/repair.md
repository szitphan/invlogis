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
