# Ghi chú chạy thử — nhóm Vị trí và Điều phối (2026-11-03)

Xe chạy thử: `TEST-XE-01`, `TEST-XE-LOP`. Ghi tăng dần, phần chưa làm ghi ở cuối file.

## Tạo và sửa Place, vùng tròn — Chạy
Các bước đã làm: Add Place → gõ tên `TEST-Cang-Cat-Lai`, gõ Latitude 10.7569, Longitude 106.7870 → chọn "200 meters" → Save Place. Mở Edit, gõ tay 350 ở Geofence Radius, Enter, lưu.
Kết quả thấy được:
- Thông báo "Place was successfully created", "Place was successfully updated". Id 254105.
- Gõ toạ độ thì ô Address tự điền theo địa chỉ ngược ("96A Thạnh Mỹ Lợi, Cát Lái, Hồ Chí Minh, Việt Nam"), bản đồ tự chuyển đến.
- Geofence Radius là ô chọn có sẵn "100 meters", "200 meters", "500 meters", "1000 meters", nhưng gõ số khác được: gõ 350 hiện lựa chọn "350 meters". Vòng tròn trên bản đồ đổi ngay khi chọn, chưa cần lưu.
- Trang chi tiết: tab "Overview", "Location Entries"; khối "Details" (Name, Address, Description, Geofence Radius), "Latest Location Entries", "Geofence Alert Policy", bản đồ.
- Danh sách Places: cột Name, Description, Address; lọc nhanh "Location Entry Type", "Location Entry Date", "Place Geofence Radius". "1 - 2 of 2".
Bất ngờ, lỗi, điểm khác tài liệu hãng: Form mở với bản đồ chưa đúng nơi (Việt Nam, gần Sóc Sơn, Hà Nội). Bấm một điểm trên bản đồ ở chế độ thường là đặt lại pin: Address và toạ độ đổi theo, Name giữ nguyên. Có một pin thứ hai màu đỏ giữ lại ở điểm cũ khi đổi toạ độ. Toast "Recurring expense save" treo sẵn từ việc khác, không liên quan.
Màn mới: place-new-form — ảnh images/place-new-form.jpg — Name, Description, khối "Adding a Location" (Address, Latitude, Longitude), Geofence Radius, bản đồ có công cụ tay, hình tròn, đa giác, Pegman, lớp bản đồ, zoom; câu "You can draw a geofence directly on the map by clicking the circle or polygon icon." place-detail-circle — ảnh images/place-detail-circle.jpg. places-list-data — ảnh images/places-list-data.jpg.
Dữ liệu TEST đã tạo: Place `TEST-Cang-Cat-Lai` (id 254105, 350 m).

## Vùng đa giác — Chạy
Các bước đã làm: Add Place `TEST-Bai-Xe`, gõ toạ độ 10.7700, 106.7600, bấm biểu tượng đa giác, bấm 4 đỉnh, bấm lại đỉnh đầu để đóng, lưu.
Kết quả thấy được:
- Đóng đa giác thì hệ thống tự thay Latitude, Longitude bằng tâm (10.77090641226091, 106.76003436580301), tự đổi Address theo tâm mới ("242 Trương Văn Bang, Cát Lái, Hồ Chí Minh, Việt Nam"), và Geofence Radius bị khoá xám với giá trị tự tính "465 meters".
- Trang chi tiết vẫn ghi "Geofence Radius 465 meters" dù vùng là đa giác; bản đồ vẽ đúng đa giác.
- Lần đầu có đa giác chỉ 2 đỉnh (thành một đoạn thẳng) vẫn được chấp nhận trên form: radius tự tính "431 meters", tức không chặn đa giác suy biến ở bước vẽ (chưa thử lưu, đã huỷ).
Bất ngờ, lỗi, điểm khác tài liệu hãng: Hộp "Leave site?" của trình duyệt xuất hiện khi rời form có thay đổi; tab kẹt, phải đóng tab.
Màn mới: place-new-polygon — ảnh images/place-new-polygon.jpg.
Dữ liệu TEST đã tạo: Place `TEST-Bai-Xe` (465 m, đa giác 4 đỉnh).

## Geofence Alert Policy (form, không lưu) — Một phần
Các bước đã làm: Mở "Add Alert Policy" trên Place, đọc, Cancel. Không lưu vì hành động duy nhất là gửi email.
Kết quả thấy được: Trigger có 4 giá trị: "Vehicle is within geofence", "Vehicle is outside geofence", "Contact is within geofence", "Contact is outside geofence". Trường "Which Vehicles?" (bắt buộc), "Which Groups?", Description, Enabled, Email Message, Recipients (bắt buộc, "Only users with an email address will be available for selection."), "Include Watchers", "Receive as Summary" ("By default, alerts are sent when detected. Enable this setting to receive a daily summary of the previous day's activity for the configured policy rules.").
Màn mới: place-geofence-alert-policy — ảnh images/place-geofence-alert-policy.jpg.

## Việc (Job): tạo, gán, kết thúc gán, gán trùng, hoàn thành — Chạy
Các bước đã làm: Add Job qua nút giữa màn trống (`TEST-Job-01`, số `TEST-01`, Place `TEST-Cang-Cat-Lai`, tắt tự động) và qua nút góc phải (`TEST-Job-02-Tu-dong`, số `TEST-02`, Place `TEST-Bai-Xe`, bật tự động). Tích xe trong cột → "Actions" → "Assign" / "Unassign". Thử: nộp form trống, gán xe đang có việc, gán trùng khoảng thời gian cũ, gán giờ tương lai, kéo thả xe sang cột việc khác, Complete.
Kết quả thấy được:
- Jobs là bảng cột: cột "Unassigned" (toàn bộ xe) + mỗi việc đang chạy 1 cột, có số đếm. Thẻ xe ghi "On job: 0m" (đếm thời gian). 2 tab "Active", "Completed". Lọc "Job Name or Number", "Vehicle Group", "Vehicle Type", "Filters".
- Form "Add Job": "Job Number" (bắt buộc, "can't be blank"), "Job Name" (bắt buộc), "Place", ô "Automatically assign and unassign assets when entering or leaving the selected Place's geofence boundary." Hai vị trí nút mở cùng một form. Nút giữa chỉ có khi chưa có việc nào.
- Toast: "Job created successfully", "Job assignments created successfully", "Vehicles successfully unassigned from Jobs", "Job completed successfully".
- Gán: hộp "Add Job Assignments" (Job, Start Date/Time, câu "Job assignments can only be created for the current or past date/time. Since they're meant to reflect real activity, future-dated assignments aren't supported at present."). Giờ tương lai: báo "cannot be in the future".
- Gán trùng: xe đang có việc thì "Assign" trong Actions bị mờ, chỉ còn "Unassign" (không chuyển thẳng sang việc khác, phải kết thúc gán trước). Gán lại giờ trùng khoảng cũ: "active Assignment overlaps with historical Assignment", kèm băng đỏ "TEST-XE-01 on TEST-01 TEST-Job-01 started at 11/03/2026 12:53 AM".
- Kết thúc gán: hộp "Unassign from Job" (End Date/Time, "When unassigning an asset from a job, the end time of the assignment must be set to the current time or a past date/time."). Ô giờ chỉ hiện chữ mờ 12:54am chứ chưa có giá trị; bấm Unassign ngay thì báo lỗi băng đỏ, không nói rõ lỗi gì; phải bấm vào ô giờ thì giờ hiện tại mới điền thật.
- Menu dòng xe trong cột: "Edit", "Delete". "Edit Job Assignment": Job và Vehicle khoá, chỉ sửa Start Date/Time.
- Menu cột việc: "Edit", "Complete", "Delete". Trang việc: tab "Overview", "Job Assignments"; Details gồm Job Number, Job Name, Status (Active / Completed), Place, "Auto-Tracking" (Off), Start Date/Time, End Date/Time; bản đồ vùng Place.
- "Job Assignment History" (menu Jobs): cột Job, Place, Vehicle, Time on Job, Start Date, End Date (Active khi đang gán), "Added" = "Manual"; lọc Status, Job Status, Job, Vehicle; "Group: None". 2 dòng thật: 2m 26s và 1m.
- Complete: hộp "Complete Job" chỉ có End Date/Time. Lỗi "must be after active assignment start date/time", "End date cannot be in the future". Xe đang gán tự được kết thúc cùng lúc (End 12:57am). Không có bước hỏi.
- Start Date/Time của việc tự lấy lúc tạo (12:51am), không nhập trên form.
Bất ngờ, lỗi, điểm khác tài liệu hãng: Kéo thả thẻ xe giữa các cột không hoạt động (thử bằng thao tác kéo chuột: chỉ bôi đen chữ); kết luận "không có kéo thả" ở mức quan sát qua công cụ. Ô tìm kiếm trên Jobs lọc theo tên xe và làm ẩn cột việc không có xe khớp. Giờ hiển thị theo giờ máy (Asia/Saigon) dù cài đặt người dùng là America/Chicago, có banner cảnh báo lệch múi giờ.
Màn mới: jobs-board — ảnh images/jobs-board.jpg; job-add-modal — images/job-add-modal.jpg; job-assign-modal — images/job-assign-modal.jpg; job-unassign-modal — images/job-unassign-modal.jpg; job-assign-overlap-error — images/job-assign-overlap-error.jpg; job-detail — images/job-detail.jpg; job-assignment-history — images/job-assignment-history.jpg; job-completed — images/job-completed.jpg.
Dữ liệu TEST đã tạo: Job `TEST-01 TEST-Job-01` (id 37280, Completed, 2 lượt gán của TEST-XE-01); Job `TEST-02 TEST-Job-02-Tu-dong` (id 37281, đã bật ô tự động gán, Place TEST-Bai-Xe).

## Vị trí không cần thiết bị: phiếu dầu, phiếu dịch vụ — Không có đường này
Các bước đã làm: Mở form New Fuel Entry, New Service Entry, đọc hết trường.
Kết quả thấy được: Không có ô vị trí nào trong cả 2 form trên web. Phiếu dầu chỉ có Vehicle, Fuel Entry Date, Odometer, Liters, Price/Liter, Fuel Type/Grade, Vendor Name, Reference, Flags, Photos, Documents, Comments. Phiếu dịch vụ: Vehicle, Repair Priority Class, Completion Date, Reference, Vendor, Labels, Issues, Line Items, Photos, Documents, Comments. Không tạo phiếu dầu TEST vì không có ô để thử.

## Phiếu kiểm web tự ghi vị trí trình duyệt — Chạy (không phải giả lập, phát hiện ngoài dự kiến)
Các bước đã làm: Nộp `TEST - Quick check` cho TEST-XE-01 trên web (#126053573). Bộ ghi đè chèn sau khi trang đã tải nên không có tác dụng.
Kết quả thấy được: Web app gọi `getCurrentPosition` đúng 1 lần lúc khởi động app (không phải lúc mở form, không phải lúc lưu), giữ giá trị đó và gửi `submitted_latitude`, `submitted_longitude` khi nộp. Phiếu có "Submission Source": "Fleetio Web App". Sinh Location Entry, xe lên marker ngay. Phiếu #125988723 nộp trước đó không có vị trí, lý do chưa rõ (có thể trình duyệt lúc đó chưa cấp quyền định vị).
Bất ngờ, lỗi, điểm khác tài liệu hãng: Câu "chỉ có điện thoại hoặc thiết bị mới có vị trí" là sai: chỉ cần trình duyệt desktop cho phép định vị. Toạ độ này là vị trí thật của máy chạy trình duyệt (khu vực Hà Nội, khác toạ độ của `/web_api/ip_geo_location`), không ghi số chính xác vào ghi chú; bản ghi còn trong tài khoản dùng thử.

## Giả lập vị trí và phiếu kiểm — Chạy (vị trí giả lập)
Các bước đã làm: Vì app đọc vị trí lúc khởi động, chèn sau tải không ăn. Cách chạy được: giữ trang Fleetio làm khung ngoài, tạo iframe cùng nguồn phủ kín màn hình, ghi đè `Geolocation.prototype` trong cửa sổ iframe ngay khi nó vừa chuyển trang, trước lúc script app chạy. Mỗi lần đổi toạ độ phải mở iframe mới.
Kết quả thấy được: #126053906 toạ độ 10.7569, 106.787; server lưu đúng, địa chỉ ngược "96A Thạnh Mỹ Lợi, Cát Lái, Hồ Chí Minh, Vietnam" (địa chỉ có sau khoảng 1 phút, lúc đầu `address` null). `location_entry.initial_place` = TEST-Cang-Cat-Lai. Trang phiếu có bản đồ nhỏ, chấm xanh tại vị trí.
Bất ngờ, lỗi, điểm khác tài liệu hãng: Máy chủ tin toạ độ do trình duyệt gửi, không có kiểm tra nào phát hiện toạ độ giả.
Dữ liệu TEST đã tạo: phiếu #126053573 (vị trí thật), #126053906, #126054089, #126054159 (giả lập) của TEST-XE-01.

## Tự gán và kết thúc gán theo vùng — Chạy (vị trí giả lập)
Các bước đã làm: Job TEST-02 bật ô tự động, Place TEST-Bai-Xe (đa giác). Nộp phiếu 10.7709, 106.7600 (trong đa giác), sau đó nộp phiếu 10.7569, 106.7870 (ngoài đa giác).
Kết quả thấy được: Phiếu trong vùng: Job Assignment History có dòng mới, "Added" = "Geofence", Start 1:06am, trạng thái Active; thẻ xe trên bảng Jobs có chip "Geofence". Phiếu ngoài vùng: dòng đó có End Date 1:07am, "Time on Job" 59s, xe về Unassigned.
Phiếu nộp ngoài vùng vẫn mang `job_assignment` là TEST-02 (phiếu ghi lại việc đang gán tại thời điểm nộp, rồi việc mới kết thúc).
Màn mới: jobs-board-geofence-chip — images/jobs-board-geofence-chip.jpg; job-history-auto-geofence — images/job-history-auto-geofence.jpg; place-detail-with-entries — images/place-detail-with-entries.jpg.

## Sự kiện vùng và Automation — Chạy (vị trí giả lập)
Các bước đã làm: Automation mới → Record Type "Geofence Event" → Trigger Type "Created" (lựa chọn duy nhất) → điều kiện Vehicle = TEST-XE-01 → hành động "Add Comment" trên Vehicle → đặt tên `TEST-Geofence vao vung them comment`, bật. Sau đó nộp phiếu ở TEST-XE-01 từ trong TEST-Cang-Cat-Lai sang trong TEST-Bai-Xe (#126055155).
Kết quả thấy được:
- Automation chạy 2 lần cùng lúc, "Total Runs" 2, "Successful" 2. Xe có 2 comment của "Fleetio Automation": "TEST - automation vung vao". Hai lần ứng với thoát Cát Lái và vào Bãi Xe (suy ra từ vị trí 2 vùng và số lần chạy; màn Run Result không ghi loại sự kiện hay Place).
- Geofence Event Type có đúng 2 giá trị: "Entered", "Exited". Điều kiện phổ biến: "Geofence Event Type", "Geofence Event Place", "Vehicle", "Vehicle Group". Hành động chỉ trên Vehicle: "Update Field", "Add Comment", "Send Email".
- Job tự gán cùng lúc: "Current Job" của xe thành TEST-02.
- Sự kiện vùng không có màn danh sách riêng. Không có cột Geofence Event ở Location Entries của Place (cột: Asset, Asset Type, Contact, Date, Entry Type; Manage Columns chỉ thêm Address, Created On, Updated On) cũng như danh sách Places. Chỉ thấy gián tiếp qua Automation và gán việc. Ngoài ra `location_entry.initial_place` cho biết lần ghi vị trí nằm trong Place nào.
- Run Result ghi "Records": "No records changed" dù comment đã thêm; log JSON có bước `ActionSet` trạng thái `DNF`, lý do "Automation Trigger has no action set" ở trace xem được, mà comment vẫn sinh. Coi là log không đáng tin, chưa rõ nguyên nhân.
Đã tắt Automation sau khi kiểm ("Automation disabled"), không gửi email nào.
Màn mới: automation-geofence-conditions — images/automation-geofence-conditions.jpg; automation-geofence-saved — images/automation-geofence-saved.jpg; automation-run-history — images/automation-run-history.jpg; vehicle-automation-comments — images/vehicle-automation-comments.jpg; place-location-entries — images/place-location-entries.jpg.
Dữ liệu TEST đã tạo: Automation id 96374 (đã tắt), 2 comment trên TEST-XE-01, phiếu #126055155.

## Location Exception và chống kiểm khống — Một phần (vị trí giả lập)
Các bước đã làm: Nộp `TEST - Pre-trip inspection` đủ mục (#126054432) và 6 phiếu `TEST - Quick check` ở các toạ độ cách nhau từ 1,4 km đến khoảng 1.100 km. Cả 2 biểu mẫu "Location Exception Tracking: Enabled". Soi gói tin gửi đi của phiếu Pre-trip.
Kết quả thấy được: Mọi phiếu `location_exception` = false. Gói tin chỉ có 1 cặp `submitted_latitude`, `submitted_longitude` cấp phiếu; mục kiểm không có toạ độ nào; `starting_latitude` null.
Kết luận đúng mức: trên web không có dữ liệu vị trí từng mục nên không tạo được Location Exception. Suy luận: luật này có lẽ cần dữ liệu từng mục từ Fleetio Go (chưa kiểm được). Không so giữa các phiếu với nhau: phiếu lệch xa phiếu trước vẫn không bị gắn cờ.
Bất ngờ: Không chặn được 1 phiếu có toạ độ giả. Đồng hồ có "must be less than 2,499 or marked as void" kiểm theo lịch sử đồng hồ dù dòng dưới ghi "Last updated: 2,999 km (Today)".
Màn mới: inspection-submission-location — images/inspection-submission-location.jpg; inspection-pretrip-simulated — images/inspection-pretrip-simulated.jpg.

## Location Exception trên Fleetio Go — Chạy một ca không vi phạm (03/11)
Các bước đã làm: User nộp `TEST - Pre-trip inspection` cho TEST-XE-01 trên app Fleetio Go (phiếu #126102722, 3m 36s, 21 mục, không mục lỗi). Đọc phản hồi của chính phiếu, chỉ lấy tên trường và khoảng cách tương đối, không chép toạ độ.
Kết quả thấy được: `submitted_from` = Fleetio Go. 21/21 mục có cặp `latitude`, `longitude` riêng, gồm 7 điểm khác nhau, cách nhau tối đa 37 m. `location_exception` = false, `are_items_too_close` = false, `items_completed_too_far_away_count` = 0. `starting_latitude` vẫn null dù phiếu có giờ bắt đầu.
Kết luận đúng mức: Fleetio Go ghi vị trí từng mục, đúng phần web không có; suy luận cũ có cơ sở. Phiếu có 2 chỉ báo riêng: mục quá gần nhau và số mục quá xa. Chưa có ca dương nên chưa biết ngưỡng, cũng chưa thấy cờ bật thật.
Bất ngờ: Số đồng hồ 3.100 km trên phiếu có icon lạ, xe vẫn hiện 2.999 km; chưa kiểm vì sao.
Không chụp ảnh màn này: bản đồ hiện tên đường thật, ảnh mục Interior Cleanliness chụp màn hình laptop của user. Phải rà trước khi đưa lên Figma hoặc commit.
Dữ liệu TEST đã tạo: phiếu #126102722 (user nộp).
Dữ liệu TEST đã tạo: phiếu #126054432; #126054560 cho TEST-XE-LOP (10.764, 106.776). TEST-XE-LOP đã được thêm vào biểu mẫu Quick check (Add Vehicles › Specific Vehicle).

## Fleet Map có marker — Chạy (vị trí giả lập), gom cụm Một phần
Các bước đã làm: Mở Fleet Map, tìm xe ở ô "Locate vehicles, places, vendors on map...", chọn xe, xem Overview, Nearby, bật Places, rê chuột, đổi Map Options, zoom, bấm marker, tắt/bật "Update list when map moves", thử Quick Add.
Kết quả thấy được:
- Marker xe: hình xe màu đen nhỏ. Bản đồ chú giải "Map Legend": "Active" ("Location updated within the last 30 minutes."), "Idle" ("Location updated within the last hour."), "Stale" ("No location updates for over an hour."), "Place" ("Center location for a configured Place geofence."), "Preferred Shop", "Premier Fleetio Vendor", "In-Network Shop", "Out-of-Network Shop", "Vendor". Trạng thái là độ tươi vị trí, không phải xe chạy hay dừng. Trang xe có lúc ghi "Idle" khi mới 25 giây trong lúc bản đồ vẫn "Active"; chưa rõ lý do.
- Mở đầu: `/web_api/ip_geo_location` theo IP (Hà Nội); "Map Starting Location" cho "Use Current Map Center" và "Reset to Default". Bản đồ không tự thu về xe; ngoài vùng thấy "No results found in this area".
- Danh sách Nearby: tab Vehicles, Places; "2 results"; sắp theo "Distance"; dòng ghi tên xe, người lái ("Unassigned" nếu chưa gán), tuổi vị trí "3m ago". Sắp theo khoảng cách với tâm bản đồ (không đo được công thức).
- Bấm marker hoặc dòng trong danh sách: không có popup, panel trái đổi sang xe đó, thân xe gắn nhãn tên. Panel: tab "Overview" (Alerts: Open Issues, Service Reminders, Incomplete Work Orders; "Last Known Location": Status, Last Updated, Where, Source "Inspection Submission #..."; Details), tab "Nearby" (PLACES, VENDORS, mặc định ẩn, nút "Show Places", "Show Vendors"; dòng Place có khoảng cách: "0", "3.33km", "1.44km", "1.91km").
- Rê chuột dòng Place trong Nearby: vẽ đường thẳng nét đứt từ xe tới Place, marker xe đổi thành marker Place trong lúc rê.
- Quick Add: nút "Add" trên panel, 11 mục: Draft Work Order, Add Vehicle Assignment, Add Expense Entry, Add Service Entry, Add Issue, Add Inspection Submission, Add Work Order, Add Warranty, Add Service Reminder, Add Vehicle Renewal Reminder, Add Meter Entry. "Add Issue" mở form New Issue điền sẵn xe, lưu xong về trang sự cố (rời bản đồ).
- "Update list when map moves": bỏ tích rồi di chuyển bản đồ, danh sách vẫn ra "No results found in this area" sau khi bấm "Center on Default Location"; không thấy khác biệt rõ khi bấm nút này, chưa thử kéo bản đồ tay.
- Map Options: "Default", "Satellite", "Grayscale", "Labels" (hiện tên Place, đè lên nhau khi gần), "Set Label Options". Tuỳ chọn được lưu theo người dùng: tải lại bản đồ vẫn giữ, đã trả về Default, Labels tắt.
- Filters: Vehicle Type, Vehicle Group, Vehicle Status, Vehicle Operator, Vehicle Assigned, còn thêm phía dưới.
- Đa giác hiển thị đúng hình trên Fleet Map; Place dùng marker tròn xanh ở tâm.
Bất ngờ, lỗi, điểm khác tài liệu hãng: Marker xe nằm trong vùng bị che bởi tâm Place khi trùng toạ độ. Gom cụm: zoom xa hết 2 xe + 2 Place không gom, marker đè nhau. Không đủ kết luận vì chỉ 2 xe; cần nhiều xe hơn để kết luận chắc.
Màn mới: fleet-map-vehicle-panel, fleet-map-vehicle-nearby-places, fleet-map-nearby-hover-dashed, fleet-map-legend, fleet-map-options, fleet-map-satellite, fleet-map-grayscale, fleet-map-labels-polygon, fleet-map-zoomed-out-no-cluster, fleet-map-nearby-list-2-vehicles (đều trong images/).
Trả lời câu hỏi mở nào: OQ-2 nhóm Vị trí (hình marker, màu theo độ tươi). OQ-1 trả lời một phần: chưa thấy gom cụm với 2 xe. OQ-3 không trả lời được phần pháp lý, nhưng ghi nhận: web gửi vị trí thật của trình duyệt lên máy chủ mà không báo gì trong form.
Dữ liệu TEST đã tạo: Issue #39 "TEST - su co tao tu Quick Add ban do".

## Câu hỏi còn lại về bản đồ
- Nhãn Zoom đảo: Còn. Nút hình "+" có `aria-label` "Zoom Out", nút hình "−" có "Zoom In". Hành vi đúng theo hình vẽ, chỉ nhãn trợ năng sai.
- Map Legend: Có, xem trên.
- Street View: Có Pegman trên bản đồ. Kéo Pegman bằng công cụ không ăn, không vào được chế độ Street View: Không chạy được.
- Satellite, Grayscale: Chạy.
- Điểm mở mặc định: theo IP, đổi được bằng "Use Current Map Center" (không bấm vì đổi cài đặt người dùng).

## API đẩy vị trí — chỉ đọc tài liệu
Tài liệu công khai developer.fleetio.com có `POST /vehicles/:id/location_entries` (tạo mới trả 201, 422 nếu không hợp lệ), bản tương tự cho Equipment; khuyên dùng Bulk API khi nhiều. Trang tóm tắt không lộ tên trường toạ độ. Không tạo key, không gọi thử.

## Việc chưa làm
- Fleetio Go trên điện thoại: đã kiểm vị trí từng mục (#126102722); còn thiếu ca Location Exception bật thật để biết ngưỡng.
- Chế độ Street View.
- Gom cụm với nhiều hơn 2 xe (không dùng dữ liệu Sample, không tạo thêm).
- Phiếu #126053573 và phiếu của agent khác (vd TEST-MOOC-LOP nhóm Phương tiện) mang vị trí thật của máy tại Hà Nội, không xoá theo quy định.

# Lượt 3 (03/11)

Gói xe 5/5, không tạo xe mới. Không lưu ảnh nào có vị trí hoặc địa chỉ thật; không ghi toạ độ, địa chỉ. Bản đồ mở theo IP cấp thành phố: Map Options ghi "MAP STARTING LOCATION: Hanoi, Hanoi". Các bước bản đồ chạy bằng đọc DOM; ảnh tạm chỉ chụp ở vùng dữ liệu Sample, không lưu.

## Nguồn vị trí: phiếu dầu có nhà cung cấp tạo vị trí xe — Chạy
Các bước đã làm: tab Location History (More, "Location History") của TEST-KHO-01; tạo 1 phiếu dầu cho TEST-DAUKEO-2 (trước đó chưa có vị trí) chọn TEST-KHO-NCC-02; mở lại tab của xe đó; mở Fleet Map.
Kết quả thấy được:
- Bộ lọc "Location Entry Type" có đúng 3 giá trị: "Fuel Entry", "Service Entry", "Inspection".
- TEST-KHO-01: 14 phiếu dầu nhưng chỉ 1 Location Entry "Fuel Entry", cùng giờ với phiếu chọn TEST-KHO-NCC-DAU (các phiếu nhìn thấy khác không có nhà cung cấp).
- TEST-DAUKEO-2: sau khi lưu phiếu #229944275, Location History có 1 dòng "Fuel Entry"; xe xuất hiện trên Fleet Map "5m ago".
- Panel xe TEST-KHO-01: "Last Known Location", Source "Fuel Entry #229915727", Status "Stale".
- TEST-XE-01: 12 dòng đều "Inspection". TEST-SUA-01: "No results found."
Bất ngờ: **sửa FR-004**. Form phiếu dầu không có ô vị trí, nhưng chọn nhà cung cấp là tạo vị trí xe tại nhà cung cấp, không cần thiết bị hay tích hợp. Không báo gì trên form. Xe hiện như đang ở cây dầu dù đó chỉ là địa chỉ khai. Địa chỉ nhà cung cấp TEST giả vẫn định vị được ra một điểm (không rõ cách quy đổi).
Service Entry: Không chạy được phần tạo. Form Service Entry chỉ cho chọn NCC có phân loại Service; NCC TEST đều không có, chọn "TEST" chỉ hiện "Create "TEST"". Không đổi NCC. Chỉ thấy loại ở bộ lọc.
Màn mới: vehicle-location-history (không lưu ảnh vì có địa chỉ; phần tử: ô Search, "Location Entry Date", "Location Entry Type", "Sort: Date - Newest First", danh sách trái icon loại + ngày + địa chỉ, bản đồ phải, "Page 1 of 1").
Dữ liệu TEST đã tạo: Fuel Entry #229944275 (TEST-DAUKEO-2), đồng hồ xe thành 100 km. Form Service Entry nháp của xe đó chưa lưu.

## Lịch sử vị trí — Chạy
Xem mục trên. Lọc theo loại mở được; không lưu lọc. Phân trang theo trang 30 dòng.

## Tìm và lọc Fleet Map — Chạy
Các bước đã làm: gõ "TEST" ở ô tìm; mở Filters; lọc Vehicle Type = Trailer; tải lại trang.
Kết quả thấy được:
- Ô tìm: "10 results available for search term TEST" gồm NCC, xe, Place; xếp NCC trước. Gõ "TEST-KHO-01" rồi Enter chọn nhầm NCC TEST-KHO-NCC-01 vì khớp mờ và NCC đứng đầu; phải đi xuống 4 dòng mới tới xe.
- Xe chưa có vị trí vẫn nằm trong kết quả (TEST-SUA-01).
- Filters đủ: VEHICLES: Vehicle Type, Vehicle Group, Vehicle Status, Vehicle Operator, Vehicle Assigned, Vehicle GPS Integration, Vehicle GPS Device Assigned, Vehicle Has Overdue Service Reminders. VENDORS: Classification. Nút Cancel, Apply.
- Lọc Trailer: còn 1 marker TEST-MOOC-LOP, huy hiệu "1" trên Filters.
- Tải lại trang: **bộ lọc mất**, quay về 2 kết quả (khác Map Options được giữ).

## Lớp bản đồ — Một phần
Bật Vendors: thêm marker NCC, danh sách có thêm tab Places, Vendors. Bấm nút Vehicles lần đó marker xe vẫn còn trong DOM: chưa kết luận lại được phần tắt xe (lượt trước đã thử bật tắt). Lớp Shops riêng: không thấy nút; chú giải có "Preferred Shop", "Premier Fleetio Vendor", "In-Network Shop", "Out-of-Network Shop", "Vendor". Giữ Docs phần Shops.

## "Update list when map moves" — Chạy (trả lời OQ-6 nhóm Vị trí)
Làm ở vùng dữ liệu Sample, chỉ đọc.
| Ô | Thao tác | Danh sách | Marker |
|---|---|---|---|
| Tick | Kéo bản đồ ra vùng không có gì | "0 results", "No results found in this area" | — |
| Bỏ tick | Kéo về vùng có 2 NCC | Vẫn "0 results", không đổi | Thấy trên bản đồ |
| Tick lại | Không kéo | Ra ngay 2 kết quả | Thấy |
| Bỏ tick | Chọn kết quả từ ô tìm | Danh sách vẫn đổi theo vùng mới | — |
Kết luận: ô chỉ chặn cập nhật khi kéo tay; chọn từ ô tìm vẫn cập nhật. Tick lại là áp ngay.

## Gom cụm marker — Chạy (chỉ đọc, trả lời OQ-1 nhóm Vị trí ở mức thấy được)
Các bước đã làm: zoom xa dần, đếm marker trong DOM.
Kết quả thấy được:
- Lớp Vendors (Sample): 2, 4, 6, 15 kết quả ứng với mỗi mức xa; 15 marker riêng, số marker dạng số = 0. Ở mức nhìn cả đông nam Mỹ, các marker trong một thành phố đè lên nhau, không gom.
- Lớp Vehicles: 4 xe TEST, zoom xa thêm 10 mức, luôn 4 marker tên riêng, không có marker dạng số.
Kết luận: tới 15 marker NCC và 4 xe, không gom. Không biết ngưỡng ở số lớn hơn. Không dùng Sample để sửa.

## Street View — Không chạy được
Kéo Pegman bằng công cụ lần nữa, ở vùng Sample, không vào chế độ phố. Giữ OQ-5.

## Tuỳ chọn bản đồ — Một phần
Menu đọc được: MAP TYPE (Default, Satellite, Grayscale), MAP DETAILS (Labels, Set Label Options), MAP STARTING LOCATION ("Use Current Map Center", "Reset to Default"). Không bấm 2 nút cuối vì đổi tuỳ chọn người dùng. Set Label Options: hộp có 1 ô "Vehicle Marker Label" (đang Name), chú thích "Select field to display for Vehicle map marker labels. Falls back to Vehicle Name if selected field value is empty/blank.", nút Cancel, Save; không lưu. Street View không chạy được.

## Cảnh báo vùng (Add Alert Policy) — Không chạy được: hành động duy nhất là gửi email, brief cấm tự động hoá gửi email. Giữ OQ-12.

## Việc Jobs
Function list không còn dòng part, view, docs cho Jobs: không có gì để chạy lượt này.

# Lượt 4 (03/11)

Không lưu ảnh bản đồ có vị trí, không ghi địa chỉ, tên nơi. NCC mới dùng địa chỉ giả TEST. Phiếu web lượt này gửi vị trí trình duyệt nên điểm mới nhất của TEST-DAUKEO-2 là vị trí máy chạy.

## Nguồn vị trí: phiếu dịch vụ có NCC Service tạo vị trí xe — Chạy
Các bước đã làm: Tạo NCC TEST-DV-NCC-01 (địa chỉ giả, phân loại Service). Lưu Service Entry #57903305 cho TEST-DAUKEO-2 chọn NCC đó. Mở tab Location History của xe.
Kết quả thấy được: Thêm 1 dòng loại "Service Entry" cùng giờ phiếu, đứng trên dòng "Fuel Entry" cũ. Form Service Entry không có ô vị trí và không báo gì. Cùng cơ chế với phiếu dầu, vậy đủ 3 loại của bộ lọc "Location Entry Type" đều đã thấy thật.
Bất ngờ:
- Địa chỉ giả "1 TEST Street, TEST City", nước Viet Nam vẫn được quy đổi ra một điểm, nhưng ở MỘT NƯỚC KHÁC, không báo độ tin cậy. Trang NCC thì vẫn ghi đúng chuỗi đã nhập. Hệ quả: khai sai địa chỉ NCC làm vị trí xe "nhảy" sang nơi không liên quan mà không cảnh báo.
- Enter trong ô Country của form New Vendor lưu luôn NCC, bỏ qua các phần dưới (Classification). Phải sửa lại để tick Service. Trang NCC có "Network Status", nút "Invite": không bấm.
Trả lời câu hỏi mở nào: FR-004: phần phiếu dịch vụ, không còn chưa thử.
Dữ liệu TEST đã tạo: Vendor #15001909 TEST-DV-NCC-01; Service Entry #57903305.

## Lớp bản đồ — Một phần (Shops vẫn Docs)
Các bước đã làm: Đọc DOM, không lưu ảnh. Bấm lần lượt Vehicles, Vendors, Places; tắt hết; tải lại trang.
Kết quả thấy được:
| Trạng thái | Danh sách trái | Marker đọc được |
|---|---|---|
| Vehicles bật (mặc định) | Tab "Vehicles", "3 results" | 3 |
| Vehicles tắt | Tab biến mất | 0 |
| Chỉ Vendors | Tab "Vendors" | Chỉ NCC |
| Vendors + Places | Tab "Places", "Vendors" | NCC, Place |
| Tắt hết | "No results found in this area" | 0 |
- **Trả lời phần lượt 3 chưa rõ:** tắt Vehicles có tác dụng thật: marker và cả tab danh sách biến mất. Nút có trạng thái aria-pressed.
- Tải lại trang: lớp về mặc định Vehicles bật, Places, Vendors tắt. Không lưu như Map Options.
- Xe trên bản đồ đang 3 (TEST-XE-01, TEST-MOOC-LOP, TEST-DAUKEO-2).
Không chạy được: Shops: không có nút lớp nào tên đó, chỉ thấy trong chú giải. Giữ Docs.

## Tuỳ chọn bản đồ: nhãn marker, vị trí mở đầu — Một phần (Street View còn lại)
Các bước đã làm: Set Label Options đổi sang VIN/SN, Save, đọc tiêu đề marker, tải lại, đổi về Name. "Use Current Map Center", xem, "Reset to Default".
Kết quả thấy được:
- Ô "Vehicle Marker Label" có 5 giá trị: Name, VIN/SN, Vehicle Type, License Plate, "Year, Make, Model".
- VIN/SN: TEST-DAUKEO-2 hiện số VIN; TEST-XE-01, TEST-MOOC-LOP không có VIN nên hiện tên, đúng câu "Falls back to Vehicle Name". Giữ sau tải lại, tức lưu theo người dùng.
- "Use Current Map Center": toast "Map Preferences Updated", dòng vị trí mở đầu đổi sang tên vùng đang xem (dạng tên, không phải toạ độ). "Reset to Default" đã bấm để trả lại.
- Đã trả nhãn về Name, marker hiện lại tên.
Không chạy được: Street View: công cụ không kéo được Pegman, lượt 3 đã thử 2 lần, không thử nữa. Giữ OQ-5.
Dữ liệu TEST đã tạo: không; tuỳ chọn người dùng đã trả lại.

## Gom cụm marker — Chặn
Lượt 3 đã đo: 15 NCC, 4 xe không gom. Muốn biết ngưỡng cần nhiều marker hơn; gói xe 5/5, NCC mới chỉ thêm 1. Không tạo hàng loạt bản ghi để đo. Giữ OQ-1 ở mức đã thấy.
