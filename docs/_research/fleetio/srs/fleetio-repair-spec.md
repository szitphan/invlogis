---
type: research
feature: fleetio-repair
status: draft
status_changed: 2026-11-03
status_reason: "đã review upstream, không cần sửa"
updated: 2026-11-03
links:
  - docs/_research/fleetio/fleetio-repair.md
  - docs/_research/fleetio/run-notes/repair.md
  - docs/_product/saas-core-vs-tenant.md
---

# Sửa chữa: sự cố, lệnh sửa, lịch sử dịch vụ — SRS phân tích ngược từ Fleetio

> Tài liệu mô tả **Fleetio đang làm gì**, kèm đề xuất cho Invlogis. Chưa phải yêu cầu đã chốt với Delta. Không dùng làm baseline phát triển.

**Nhãn bằng chứng:** `Chạy` đã thao tác và thấy kết quả · `Xem` thấy trên giao diện · `Docs` tài liệu công khai của Fleetio · `Suy` suy ra · `GĐ` giả định của người viết.

**Dữ liệu chạy:** xe TEST-SUA-01 loại Car; Issue #33 đến #38, #45, #46; Work Order #103, #104, #106, #107; Service Entry 57856983, 57857945 (tự bị xoá khi mở lại), 57858956. Lượt 3: Issue #52, #53; Work Order #110; Service Entry 57902070; bảo hành 356513, 356515 và "TEST-SUA BH het han". Lượt 4: Issue #59, Service Entry 57903452 trên TEST-KHO-01; thử markup phụ tùng trên #107. Lượt 5: trạng thái "TEST-SUA Cho phu tung", "TEST-SUA Xong cho nghiem thu" qua #106, entry 57906551 (đã xoá khi mở lại); mẫu "TEST-SUA Mau bao hanh" sinh 2 bảo hành; đã đổi Cài đặt có chủ đích, phần không xoá được còn lại trong Settings. Lượt trước: Issue #30, #31, Work Order #99, #100. Tài khoản một người dùng, toàn quyền: mọi kết luận về phân quyền chưa kiểm chứng.

## 1. Scope

**Trong phạm vi:** vòng đời Issue, Work Order, Service Entry, Service Task, Fault, Warranty và các tính năng AI gắn với chúng; phần tồn kho, nhận hàng phát sinh từ dòng phụ tùng của lệnh.

**Ngoài phạm vi:** nhắc bảo dưỡng và kiểm tra xe (xem [[docs/_research/fleetio/srs/fleetio-reminders-inspection-spec.md|Nhắc, kiểm tra]]), vòng đời kho, đơn mua ngoài phần lệnh (xem [[docs/_research/fleetio/srs/fleetio-parts-purchasing-fuel-spec.md|Kho, mua]]), mạng lưới xưởng Maintenance Shop Network vì phụ thuộc đối tác Mỹ; chỉ ghi nhận cổng vào.

**Phân biệt bốn khái niệm** (`Docs`): Service Task và Issue mô tả việc **cần làm**; Service Entry và Work Order ghi việc **đã làm hoặc đang làm**.

| Khái niệm | Bản chất | Khi dùng |
|---|---|---|
| Service Task | Đầu việc trong danh mục, định kỳ hoặc một lần | Lập kế hoạch, gắn vào nhắc và lệnh |
| Issue | Sự cố một lần, ngoài dự kiến | Xe gặp vấn đề |
| Service Entry | Bản ghi nhanh việc đã xong | Sửa ngoài, chỉ cần lưu lịch sử |
| Work Order | Phiếu chi tiết từ lúc mở đến hoàn thành | Kiểm soát việc sửa nội bộ |

## 2. Actors & Stakeholders

| Actor | Loại | Mục tiêu | Trong scope? | Tương đương Invlogis |
|---|---|---|---|---|
| Operator | Người | Báo sự cố, xem việc của xe | Có | Lái xe |
| Technician | Người | Thực hiện lệnh, ghi công | Có | Nhân viên xưởng |
| Fleet Manager | Người | Xếp ưu tiên, lập và hoàn thành lệnh | Có | Quản lý phương tiện |
| Account Owner, Administrator | Người | Cấu hình trạng thái, luật | Có | Admin |
| AI Service Advisor | Hệ thống | Xếp ưu tiên, soạn lệnh, đánh giá, đóng sự cố | Có | Chưa có |
| Automation, Workflow | Hệ thống | Tạo và đổi bản ghi theo luật | Có | Chưa có |
| Telematics | Ngoài | Đẩy mã lỗi, số km | Có | EUP theo `vehicle-telematics` |

## 3. Functional Requirements (FR)

| ID | Title | Description | Priority | Tầng | Verify by | Source | Mức thực tế | Đề xuất Invlogis |
|---|---|---|---|---|---|---|---|---|
| FR-fleetio-repair-001 | Tạo sự cố | Người dùng tạo sự cố cho một xe với tóm tắt, ngày báo; hệ thống tự điền người báo và thời điểm. Hạn theo ngày, đồng hồ là tuỳ chọn. | P0 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` Issue #30, #33 đến #38 | `Chạy` | Lấy cho `incident-report`, thêm báo từ app |
| FR-fleetio-repair-002 | Nhiều nguồn sự cố | Sự cố đến từ nhập tay, phiếu kiểm tra hỏng, mã lỗi thiết bị, thu hồi; có trường Source liên kết về nguồn. Sự cố nhập tay có Source "—" (#52); sự cố từ mã lỗi liệt kê từng dòng Fault (#13 Sample). | P0 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` Issue #31, #52; `Xem` Faults, #13, menu Recall | `Chạy` một phần lượt 3: Tay, phiếu kiểm, đọc Source mã lỗi Sample; Recall không chạy | Lấy, bỏ thu hồi NHTSA |
| FR-fleetio-repair-003 | Năm cách xử lý | Menu Resolve trên sự cố mở: Add to Service Entry, Draft Work Order, Add to Work Order, Get Service at Shop, Resolve with Note. Khi sự cố đã gắn lệnh: Add to Service Entry, Add to Work Order, Resolve with Note xám có khoá; Draft Work Order lượt trước còn dùng được, lượt 3 trên #45 và lượt 5 trên #46 cũng xám (OQ-19); Get Service at Shop vẫn sáng. | P1 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` #35, #37, #45, #46, #52; `Xem` Shop | `Chạy` một phần lượt 3: 4/5 cách; Get Service at Shop chặn | Lấy, bỏ nhánh mạng lưới xưởng |
| FR-fleetio-repair-004 | Đóng sự cố không sửa | Menu ba chấm › Close mở hộp có ô Note tuỳ chọn; đóng ghi Closed Date, Closed By, Note; ghi chú thành một Comment; mất Edit, Resolve. Không tính vào thời gian xử lý (`Docs`). | P1 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` #36, #38; `Docs` Issues Overview | `Chạy` | Lấy; nên bắt buộc lý do đóng |
| FR-fleetio-repair-005 | Sự cố quá hạn | Sự cố có hạn theo ngày và số đồng hồ. Overdue là giá trị tính, không lưu: đọc lại mỗi lần theo ngày và đồng hồ hiện tại; hiện ở Issue Status, tab Overdue, vẫn thuộc nhóm Open. Không có nút, sự kiện chuyển. | P1 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` #33 đến #38 | `Chạy` | Lấy cách tính; ghi thêm thời điểm bắt đầu quá hạn |
| FR-fleetio-repair-006 | Tạo lệnh | Lệnh có xe, trạng thái, phân loại ưu tiên, ngày lập, người lập, người nhận việc, ngày dự kiến và thực tế, xưởng ngoài, hoá đơn, số đơn mua. Số lệnh trên form chỉ là số dự kiến, lưu thì tự nhảy nếu đã có lệnh khác. | P0 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` WO #99, #100, #103, #104 | `Chạy` | Lấy cho `repair-order` |
| FR-fleetio-repair-007 | Gắn sự cố vào lệnh | Form lệnh liệt kê sự cố của xe theo tab Open, Resolved, Closed; Overdue nằm trong tab Open; tick để gắn; gắn được với từng dòng việc qua Link Issues. Dòng đã ở lệnh khác có ổ khoá. Hộp Link Issues liệt kê sự cố của xe; sau Save sự cố tự được tick ở khối Issues, cột Linked Line Items hiện tên dòng, dòng việc đếm số sự cố; chi tiết lệnh hiện sự cố ở cả "Resolved Issues" và dưới dòng, kể cả khi lệnh còn Open. | P0 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` WO #100, #103, #104, #107 | `Chạy` lượt 3: Link Issues vào dòng; khoá sự cố ở lệnh khác | Lấy, phải báo khi tick không vào |
| FR-fleetio-repair-008 | Dòng việc | Dòng việc gồm đầu việc, công, phụ tùng, ghi chú, mã phân loại tự điền (Reason, Category, System, Assembly), Last Completed, Add Service Reminder; có tab Service Tasks, Labor, Parts. | P0 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` | `Chạy`; tiền hiển thị lệch, xem E-005 | Lấy, sửa lỗi tiền |
| FR-fleetio-repair-009 | Ghi công | Hộp Add Labor: Technician bắt buộc, Labor Hours mặc định 1 kèm nút chọn nhanh, Hourly Rate, Service Task, Note, Subtotal, "Save and Add Another", "Save". Chọn kỹ thuật viên lấy đơn giá mặc định của contact. Tài liệu hãng có bấm giờ bắt đầu, kết thúc; web không có nút Start, Stop ở form và chi tiết lệnh, chỉ nhập giờ tay và mốc thời gian (FR-fleetio-repair-045). Báo cáo `work_orders/labor_time_entries` chỉ lọc Contacts, Started at, Ended at. | P1 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` hộp Add Labor, #107; `Docs` bấm giờ | `Chạy` lượt 4: Nhập công; web không có nút bấm giờ | Lấy nếu Delta tính công |
| FR-fleetio-repair-010 | Tổng hợp chi phí | Tính tổng công, phụ tùng, markup công, markup phụ tùng, tín dụng bảo hành, giảm giá, thuế. Mỗi ô đổi được giữa phần trăm và số tiền. Thứ tự tính ở BR-fleetio-repair-035. Warranty Credits nhập tay, không nối với hồ sơ bảo hành. Xoá hết phụ tùng, markup phụ tùng cố định vẫn cộng, không cảnh báo. | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | test | `Chạy` #107 markup công, markup phụ tùng theo phần trăm và cố định, credit, giảm giá, thuế | `Chạy` lượt 4: Markup phụ tùng % và cố định, trả tồn | Lấy, hợp với sửa cho xe khách |
| FR-fleetio-repair-011 | Đổi trạng thái lệnh | Đổi trạng thái ngay trên đầu trang. Open và Pending đổi qua lại không hỏi; Pending sang Completed đi thẳng được; hệ thống kiểm điều kiện theo cấu hình; Completed về chưa xong có hộp xác nhận. | P0 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` #104 | `Chạy` | Lấy |
| FR-fleetio-repair-012 | Hoàn thành lệnh | Khi chuyển sang trạng thái loại Completed, hệ thống giải quyết sự cố đã chọn, ghi nhận đầu việc, tính Duration, tạo Service Entry, ghi Time to Resolve, Kilometers to Resolve, khoá Edit của lệnh, entry và Reopen của sự cố. Không ghi sổ kho. | P0 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` WO #99, #104; `Chạy` nhóm Nhắc #101 về nhắc | `Chạy` | Lấy, xem Mục 11 về ghi trùng số km |
| FR-fleetio-repair-013 | Mở lại lệnh | Đổi lệnh Completed về chưa xong qua hộp "Update Status". Service Entry bị xoá hẳn, URL ra Not Found; sự cố về Open, mất Resolution Details và dòng Timeline; đồng hồ và tồn giữ nguyên. Khôi phục dữ liệu archive chạy nền. | P0 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` #104; `Chạy` K15 ở WO #102 | `Chạy` | Lấy cơ chế khoá; giữ vết thay vì xoá hẳn |
| FR-fleetio-repair-014 | Ghi lịch sử trực tiếp | Tạo Service Entry không qua lệnh, bắt buộc Odometer và Completion Date, không cần dòng việc; lưu là giải quyết sự cố đã chọn. | P1 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` entry 57856983 từ #37; `Docs` phần tạo từ danh sách | `Chạy` | Lấy cho sửa ngoài; cảnh báo số đồng hồ thấp |
| FR-fleetio-repair-015 | Xem lệnh ba chế độ | Danh sách, lịch tháng, lịch tài nguyên theo xe hoặc kỹ thuật viên. | P1 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` chuyển chế độ | `Chạy` | Lấy lịch tài nguyên cho xưởng |
| FR-fleetio-repair-016 | Đầu việc | Danh mục đầu việc có mã phân loại mặc định, giờ công dự kiến, phụ tùng gắn kèm; 400 đầu việc có sẵn. Tab Active, Archived; Actions có Update Service Tasks, Archive; More Actions có Import, Export. | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | demo | `Chạy` | `Chạy` | Lấy cấu trúc, tự xây danh mục tiếng Việt |
| FR-fleetio-repair-017 | Tình trạng từng dòng | Tài liệu hãng: đánh dấu xong từng dòng, không kích hoạt hiệu ứng hoàn thành; cấu hình bắt buộc xong hết mới hoàn thành lệnh. Trên web với tài khoản hiện tại không thấy: menu dòng chỉ có Change Service Task, Add Service Reminder, View Change Log, View Service Task History, Delete; chi tiết lệnh không có ô hay nút đánh dấu. | P2 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | test | `Docs`; `Chạy` #107 không thấy trên web; không đổi Settings nên chưa kiểm luật | `Chạy` một phần lượt 3: Web không có ô đánh dấu dòng; cấu hình bị chặn | Cân nhắc |
| FR-fleetio-repair-018 | Sao chép, in, gửi | More Actions: Run Assessment, Print, Make a Copy, View Record History, Email PDF, Delete. Print mở PDF tab mới. Make a Copy mở form mới: xe trống, Status Open, Issue Date hiện tại; chọn xe xong mới có dòng việc, công; không chép sự cố, ngày, đồng hồ. Print ra tệp PDF 2 trang: thông tin lệnh và xe, Line Items, Description, Summary đủ từng khoản tiền. PDF theo múi giờ tài khoản, tiền dạng US, khác web (E-fleetio-repair-028). View Record History: FR-fleetio-repair-042. | P2 | [Cấu hình] | demo | `Chạy` Print #103, #107, Copy, Record History #107; `Xem` Email PDF, Delete | `Chạy` một phần lượt 4: Đọc được PDF; Email PDF chặn, Delete không làm | Lấy in và lịch sử |
| FR-fleetio-repair-019 | AI xếp ưu tiên | Với sự cố mới, AI tự gán hoặc gợi ý mức ưu tiên, hiện dấu sao và câu "Auto-assigned priority". Có sự cố vẫn để "No Priority". | P2 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` #33, #34, #35, #45, #46 | `Chạy` | Cân nhắc, cần thử nhiều hơn với tiếng Việt |
| FR-fleetio-repair-020 | AI soạn lệnh | Từ sự cố, AI soạn nháp chạy nền, đổi dòng chữ tiến độ; rời trang vẫn chạy. Hộp review: cảnh báo lệnh đang mở của xe, nhóm "Resolves this issue" và "Also recommended for this vehicle" gom sự cố khác cùng xe, đầu việc có tick, ước tính, phần tự điền; tạo lệnh mới hoặc thêm vào lệnh đang mở; hoặc Discard. Menu "Add to" chỉ nêu lệnh mở mới nhất dù xe có nhiều lệnh mở, không cho chọn lệnh khác. Sự cố khác đang ở lệnh không chuyển sang lệnh mới, nhưng đầu việc gợi ý của nó vẫn vào, thành dòng trùng. | P2 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` WO #99, #106, #110, sự cố #45, #46, #52, #53; `Chạy` nhóm Nhắc: mục này xám trên nhắc | `Chạy` lượt 3: Nhiều sự cố, tạo mới, thêm vào lệnh đang có | Cân nhắc; học gom việc cùng xe |
| FR-fleetio-repair-021 | AI đánh giá lệnh | Khi có đầu việc và chi phí, AI tự chạy trên lệnh, kiểm công và giá phụ tùng, kết luận Acceptable hoặc Needs Review, ghi nguồn; cho chạy lại khi lệnh đổi; soi cả lệnh khác cùng xe trùng đầu việc. | P2 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` WO #99, #103, #104 | `Chạy` | Chờ có dữ liệu giá Việt Nam; không dùng làm điều kiện duyệt |
| FR-fleetio-repair-022 | AI đóng sự cố | Tài liệu hãng: khi có Service Entry, AI đóng hoặc gợi ý đóng sự cố khớp nội dung. Với cấu hình hiện tại, entry 57902070 cùng đầu việc và nội dung với #52 không đóng, không gợi ý, ở cả form và trang chi tiết; đọc lại sau khoảng 1 đến 2 giờ vẫn vậy. Thử lại với #59 và entry 57903452, sau khoảng 15 phút cũng không. Mục Issue Resolution trong Settings chưa bấm vì có câu điều khoản, chưa biết trạng thái bật thật. | P2 | [Gói: Bảo dưỡng đội xe] | demo | `Docs`, `Xem` cấu hình, `Chạy` entry 57902070, 57903452 | `Chạy` một phần lượt 4: Đợi lâu hơn, không đóng; bật tính năng bị chặn | Cân nhắc, cần người duyệt |
| FR-fleetio-repair-023 | Mã lỗi thiết bị | Nhận mã lỗi, đánh dấu nghiêm trọng, gom các mã liên quan vào một sự cố; có trạng thái Open, Pending, Resolved, Ignored; menu dòng Create Issue, Ignore, View Fault Rule. Mã thuộc hai hệ OBD và SPN/FMI. Sự cố #13 gom ba mã, Reported By là AI Service Advisor, ưu tiên "Auto-assigned priority: High", Source liệt kê từng mã. Nhập mã qua tích hợp telematics. | P2 | [Gói: Bảo dưỡng đội xe] | demo | `Xem` Issue #13, #14, #15 gom nhiều mã; 16 dòng Sample; không bấm Create Issue, Ignore | `Xem` | Phụ thuộc thiết bị |
| FR-fleetio-repair-024 | Luật mã lỗi | Khai mã, mô tả và mức nghiêm trọng theo khách; có mẫu bỏ qua mã phiền. Hộp Add Fault Rule: Code bắt buộc, phải khớp chính xác mã đến; Name, Description ghi đè giá trị của mã đến; Priority Handling bắt buộc gồm Off, Ignore Code, Flag as Critical. Bảng trong Settings cột Code, Description. | P2 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | demo | `Xem` Fault Rules 11 dòng, hộp Add Fault Rule mở rồi Cancel, mẫu Automation | `Xem` | Phụ thuộc thiết bị |
| FR-fleetio-repair-025 | Bảo hành | Khai bảo hành theo ngày và số km, cho nhiều xe một lượt, mỗi xe một Start Date, Start Meter; Standard Warranty, Standard templates, Extended Warranty; tự tính End Date, End Meter; gắn mã phân loại. Có hai form: một xe (`warranties/new`) và nhiều xe (`multiple/warranties/new`). End Date, End Meter là ô xám tự tính khi gõ. Trang chi tiết hiện End Date sớm hơn form 1 ngày (E-fleetio-repair-023). Áp mẫu: FR-fleetio-repair-046. Ô Start Meter không cảnh báo khi lệch xa đồng hồ xe (E-fleetio-repair-032). | P2 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` nhóm Phương tiện, TEST Bao hanh dong co; `Chạy` 356513, 356515, "TEST-SUA BH het han" | `Chạy` lượt 5: Tạo mẫu, áp cho xe, sinh bảo hành | Hỏi Delta |
| FR-fleetio-repair-026 | Giải quyết kèm ghi chú | Resolve with Note mở hộp có Note bắt buộc, nút khoá khi trống. Sau lưu: Status Resolved, khối Resolution Details, nút Reopen, mất Edit. | P1 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` #35 | `Chạy` | Lấy |
| FR-fleetio-repair-027 | Mở lại sự cố | Nút Reopen trên sự cố Closed hoặc Resolved bằng ghi chú, bằng entry mở hộp xác nhận; sự cố Resolved bằng lệnh thì nút khoá, tooltip nêu số lệnh. | P1 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` #35, #37, #38 | `Chạy` | Lấy; ghi vết lần mở lại |
| FR-fleetio-repair-028 | Thêm vào Service Entry | Hộp "Add to Service Entry" liệt kê sự cố mở của xe, tick sẵn sự cố đang mở trang; chọn Add to New hoặc Add to Existing Service Entry, Continue sang form. Existing hiện thêm ô chọn chỉ có entry của đúng xe, Continue khoá tới khi chọn. Resolved Date lấy theo ngày entry đã chọn, không chặn entry cũ hơn lúc báo sự cố. Sửa entry, bỏ tick sự cố ở tab Resolved là gỡ sự cố về Open. Sự cố đang ở lệnh có ổ khoá, không tick hay bỏ tick được từ đây. | P1 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` New; `Chạy` Existing, bỏ tick với #52 và 57856983 | `Chạy` lượt 3: Add to Existing, bỏ tick sự cố trong entry | Lấy |
| FR-fleetio-repair-029 | Số đồng hồ trên lệnh | Start Odometer và tick "Use start odometer for completion meter" mặc định bật; bỏ tick hiện Completion Odometer. Lưu hai mốc tạo hai dòng Meter History nguồn lệnh. | P0 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` #104 | `Chạy` | Lấy |
| FR-fleetio-repair-030 | Phân loại ưu tiên lệnh | Repair Priority Class gồm Scheduled, Non-Scheduled, Emergency, ghi rõ VMRS Code Key 16; bật được bắt buộc. | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | demo | `Chạy` #106 chọn Emergency | `Chạy` | Lấy ba mức, bỏ mã VMRS |
| FR-fleetio-repair-031 | Khoá và gỡ sự cố khỏi lệnh | Sự cố đã gắn lệnh thì khoá lối khác kèm tooltip, gồm cả Close ("...already added to a Work Order. Remove it from all Work Orders to close"); Delete vẫn sáng, không bấm. Sửa lệnh, bỏ tick rồi lưu là gỡ; sự cố tự do trở lại, Timeline xoá dòng "added this issue". | P0 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` #45, #107 | `Chạy` | Lấy khoá; ghi vết lần gỡ |
| FR-fleetio-repair-032 | Tồn kho theo dòng phụ tùng | Hộp Add Part chọn kho, ghi "This will make an inventory adjustment" hoặc "None (No Inventory Adjustment)". Lưu lệnh trừ tồn ngay khi lệnh còn Open, có WO Current Qty riêng; sửa số lượng, xoá dòng ghi bù vào Inventory Activity nguồn số lệnh, xoá dòng trả lại đủ tồn. | P0 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` #103, #104, K10 đến K16 | `Chạy` | Lấy; cảnh báo khi vượt tồn |
| FR-fleetio-repair-033 | Giao việc, theo dõi | Sửa so với bản trước: Assigned To không chỉ người có nhãn Technician, danh sách có cả Employee, Operator, Account Owner và "Fleetio Automation"; lưu không hỏi. Người tạo lệnh, sự cố, kể cả lệnh từ nháp AI, tự thành người theo dõi. User được giao tự thành người theo dõi; liên hệ không đăng nhập thì không. Khung Watching liệt kê WATCHERS, ADD WATCHER tìm user; Watch, Unwatch đổi ngay, không hỏi lại. Xe không tự theo dõi. | P1 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` #106, #107, #110, TEST-SUA-01; user thứ hai: không chạy vì không mời người ngoài; email khi giao: không kiểm được | `Chạy` một phần lượt 4: Giao cho user tự theo dõi; user thứ hai chặn | Lấy; cần báo người nhận |
| FR-fleetio-repair-034 | Hoàn thành lại | Lệnh đã mở lại đổi Completed lần nữa: tạo entry mới số khác, dùng ngày và đồng hồ cũ của lệnh, không hỏi lại; Timeline sự cố lại có dòng giải quyết. Hai lượt thử không thấy giới hạn số lần. | P0 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` #104, entry 57858956 | `Chạy` | Hỏi lại ngày; không sinh dòng đồng hồ trùng |
| FR-fleetio-repair-035 | Cài đặt bảo dưỡng | Maintenance Settings: Enable Work Orders, Next Work Order Number, Require a Meter Reading kèm Excluded Vehicle Types, Require Inspections, Require Repair Priority Class, Reason for Repair, Category, hai mục chặn sửa mã mặc định. | P1 | [Cấu hình] | demo | `Xem`, không đổi | `Xem` | Lấy cách nhóm luật; tham số mới, chưa có mã |
| FR-fleetio-repair-036 | Danh mục trạng thái lệnh | Bảng trạng thái có Name kèm màu, Default, mô tả; Type; số lệnh; mặc định Open, Pending loại Incomplete, Completed loại Completed. Khách thêm trạng thái bằng form Name, Description, ô Completed, ô Default, Color. Loại chỉ có hai, chọn bằng một ô tick; không khai thứ tự chuyển, người được chuyển, hiệu ứng. Trạng thái mới có ngay ở menu trên lệnh, form lệnh, bộ lọc; không tự thêm tab trên danh sách lệnh. | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | demo | `Chạy` 2 trạng thái TEST qua #106; Delete, kéo sắp xếp không chạy | `Chạy` một phần lượt 5: Đủ vòng tuỳ biến; chưa kéo sắp xếp, chưa đo nhắc | Lấy hai nhóm |
| FR-fleetio-repair-037 | Nhận hàng đơn mua vào lệnh | Nhận đơn mua chọn nơi đến là lệnh có sẵn hoặc lệnh mới: cộng kho trước, trừ khi lưu lệnh, dòng ghi chú "From PO"; huỷ form hàng vẫn ở kho. | P1 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` D14, D15 ở nhóm Kho | `Chạy` | Lấy |
| FR-fleetio-repair-038 | Cơ hội bảo hành trên lệnh | Khối Warranty Opportunities luôn hiện trên lệnh: đếm active, expiring soon, total; Vehicle Coverage khớp đầu việc theo mã phân loại đúng từng mức (BR-fleetio-repair-036), chỉ với bảo hành Active (BR-fleetio-repair-037); có View Active Coverage, Complaint, Cause, Correction; Replaced Parts cho phụ tùng. Ba ô chữ là ghi chú trên lệnh, không có nút claim, trạng thái claim, gửi hãng; "View Active Coverage", "Total vehicle coverage breakdown" chỉ là liên kết sang tab bảo hành của xe. | P2 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` WO #100 nhóm Phương tiện; `Chạy` #103, #104, #106 khối trống; `Chạy` #107, #110 | `Chạy` lượt 3: Khớp theo mã, trạng thái; điền Complaint, Cause, Correction | Lấy khi có bảo hành |
| FR-fleetio-repair-039 | Đưa ra xưởng ngoài | Get Service at Shop mở hộp giới thiệu Shop Network, cần Enable Shop Network mới dùng. Mục vẫn sáng cả khi sự cố đang gắn lệnh. Bấm Enable chuyển sang trang thiết lập tài khoản thanh toán Fleetio Pay, tài khoản này gặp "Access Denied"; không thấy hộp điều khoản, phí; mở lại vẫn hộp giới thiệu, tức chưa bật. Chọn xưởng, gửi yêu cầu, duyệt báo giá, hoá đơn chưa chạy được. | P2 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` #46 tới Access Denied; phần sau không chạy | `Xem` | Không lấy mạng lưới Mỹ; có thể gửi yêu cầu cho nhà cung cấp dịch vụ của khách |
| FR-fleetio-repair-040 | Đơn giá công theo contact | Contact Technician có đơn giá mặc định; danh sách chọn và hộp Edit Labor hiện đơn giá đó. | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | test | `Chạy` TEST-SUA-KTV; số hiện lệch giữa màn, xem E-014 | `Chạy` | Lấy; đơn giá là dữ liệu của khách |
| FR-fleetio-repair-041 | Tạo, lưu trữ đầu việc | Form "New Custom Service Task" gồm 6 bước gập, Save khoá tới khi Continue hết. Archive không xoá khỏi Fleetio, cập nhật bản ghi liên quan chạy nền. Không thấy gộp đầu việc. | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | test | `Chạy` TEST-SUA-DV-A, TEST-SUA-DV-B | `Chạy` | Lấy Archive; nên có gộp khi trùng |
| FR-fleetio-repair-042 | Sổ thay đổi theo trường | Hộp Record History của lệnh: lọc "Select Date Range", cột Date, Changes By, Changes Made. Ghi từng trường tiền, phần trăm, dòng việc, dòng công và việc tạo lệnh. Khác Timeline của sự cố vốn không ghi đóng, mở lại. | P1 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` #107 | `Chạy` | Lấy; đủ để đối soát khi sửa lệnh đã tính chi phí |
| FR-fleetio-repair-043 | Mã phân loại, thành phần bảo hành | Hộp Add Maintenance Categorization có Bulk Mode, Column Mode, nhận mã System hoặc System–Assembly, phần thứ ba bị bỏ; menu "…" có Edit, Clear Codes. Add Component: Component Name bắt buộc, Description, để chia phạm vi trong một bảo hành. | P2 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` 356513; `Xem` Add Component mở rồi huỷ | `Chạy` một phần: mã chạy; Add Component chưa lưu | Lấy gắn mã; nên cho mã cha phủ mã con |
| FR-fleetio-repair-044 | Bảo hành theo xe, lưu liên tiếp | Tab Warranties của xe: Name, Manufacturer, Coverage Type, Start Date, End Date, Start Meter, Coverage Distance, End Meter, Status. "Save & Add Another" giữ phần lớn trường, có danh sách "Added Warranties" bên phải. Coverage Template bật khi đã chọn xe; "No options" khi chưa có mẫu đúng điều kiện (FR-fleetio-repair-046). | P2 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` TEST-SUA-01; template không chạy | `Chạy` một phần: tab, lưu liên tiếp; template không có | Lấy tab theo xe; xoá mã khi lưu liên tiếp |
| FR-fleetio-repair-045 | Mốc thời gian của dòng công | Tick "Set Labor Time Entry" hiện Start Date, End Date để tạo Time Entry; End tự bằng Start cộng số giờ, đổi nút giờ thì End đổi theo. | P1 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` #107 | `Chạy` | Lấy nếu Delta tính công theo ca |
| FR-fleetio-repair-046 | Mẫu bảo hành và áp thay đổi | Settings › Warranty Templates: mẫu có Name, Meter Unit, các coverage đủ trường như bảo hành thường; Save khoá tới khi có coverage. New Warranties chọn Standard templates, xem trước và sửa riêng từng dòng, lưu thì sinh các bảo hành riêng. Sửa mẫu đã dùng mở hộp "Template Change": chỉ áp tương lai (mặc định), hoặc áp cả quá khứ kèm số xe bị ảnh hưởng và cảnh báo ghi đè phần sửa riêng. Có thư viện mẫu OEM. Liên quan FR-fleetio-vehicle-039. | P2 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | test | `Chạy` mẫu TEST trên TEST-SUA-01, áp quá khứ; `Xem` OEM, không lưu; lựa chọn tương lai không chạy | `Chạy` một phần: mẫu riêng, áp quá khứ; chưa chạy áp tương lai | Lấy cơ chế tương lai hay quá khứ cho mọi mẫu; thêm so sánh trước sau; bỏ thư viện OEM Mỹ |

## 4. Non-Functional Requirements (NFR)

Fleetio không công bố số liệu; các số dưới là quan sát một lần, không phải cam kết.

| ID | Category | Requirement | Priority | Acceptance |
|---|---|---|---|---|
| NFR-fleetio-repair-001 | hiệu năng | AI soạn lệnh chạy nền, người dùng làm tiếp được. | P2 | Quan sát: nháp xong khoảng 30 đến 40 giây, có banner đổi chữ, có thông báo |
| NFR-fleetio-repair-002 | truy vết | Mọi đổi trạng thái có người và thời điểm, kể cả do workflow hay AI. | P0 | Quan sát: dòng thời gian ghi "by work order", "by workflow", "from an AI draft"; **không** ghi đổi Overdue, đóng, mở lại, gỡ khỏi lệnh, bỏ tick trong entry. Record History của lệnh ghi theo từng trường, Timeline của sự cố thì không |
| NFR-fleetio-repair-003 | trách nhiệm AI | Khách tự chịu trách nhiệm quyết định theo gợi ý AI; AI có nguồn và nút phản hồi. | P2 | Quan sát: điều khoản ở trang AI Service Advisor, "Was this helpful?" |
| NFR-fleetio-repair-004 | quyền | Sửa trạng thái cần quyền theo nhóm lệnh đã xong và chưa xong. | P1 | `Docs`: Edit và View Completed hoặc Incomplete Work Orders. Tài khoản một người, chưa kiểm |
| NFR-fleetio-repair-005 | hiệu năng | Thời gian phản hồi cho Invlogis: TBD — đội sản phẩm — khi chi tiết hoá `repair-order`. | P1 | TBD |
| NFR-fleetio-repair-006 | nhất quán dữ liệu | Mở lại lệnh chạy nền; trong vài giây trang vẫn hiện Completed. | P1 | Quan sát: toast "Restoring Work Order #104 data". Invlogis nên khoá thao tác cho tới khi xong |
| NFR-fleetio-repair-007 | tiền tệ | Tiền không có số lẻ phải hiện đúng ở mọi màn. | P0 | Quan sát Fleetio: lệch 100 lần với VND. Invlogis: lưu tiền theo số lẻ của từng loại tiền, không cứng 2 số lẻ; ca kiểm thử bắt buộc |
| NFR-fleetio-repair-008 | nhất quán thời gian | Một bản ghi phải hiện cùng ngày ở mọi kênh. | P1 | Quan sát Fleetio: PDF theo múi giờ tài khoản, web theo máy, một lệnh hiện 2 ngày khác nhau. Invlogis: ca kiểm thử web và bản in |

## 5. Business Rules

| ID | Rule | Tầng | Trigger | Implements FR | Source | Mức thực tế |
|---|---|---|---|---|---|---|
| BR-fleetio-repair-001 | Sự cố mới luôn ở trạng thái Open, kể cả khi hạn đã qua thì hiển thị Overdue. | [Gói: Bảo dưỡng đội xe] | Lưu sự cố | FR-fleetio-repair-001 | `Chạy` #33 | `Chạy` |
| BR-fleetio-repair-002 | Sự cố đã Resolved hoặc Closed không sửa được đến khi mở lại: nút Edit biến mất. | [Gói: Bảo dưỡng đội xe] | Sửa sự cố | FR-fleetio-repair-004 | `Chạy` #35, #36 | `Chạy` |
| BR-fleetio-repair-003 | Cách mở lại tuỳ nguồn: giải quyết bằng lệnh thì đổi lệnh về chưa xong; bằng ghi chú, bằng Service Entry hoặc đã đóng thì bấm Reopen. Sửa so với bản trước: nút Reopen của sự cố giải quyết bằng entry không khoá. Bỏ tick trong entry cũng mở lại, xem BR-fleetio-repair-040. | [Gói: Bảo dưỡng đội xe] | Mở lại | FR-fleetio-repair-027 | `Chạy` #35, #37, #38, #52, #104 | `Chạy` |
| BR-fleetio-repair-004 | Sự cố Closed không tính vào chênh lệch thời gian, số km xử lý. | [Gói: Bảo dưỡng đội xe] | Tính chỉ số | FR-fleetio-repair-004 | `Docs` | `Docs` |
| BR-fleetio-repair-005 | Chỉ một trạng thái lệnh là mặc định; trạng thái đang dùng không xoá được. | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Cấu hình | FR-fleetio-repair-036 | `Chạy` đổi Default; `Docs`, `Xem` phần xoá | `Chạy` Default; xoá `Xem` nút khoá |
| BR-fleetio-repair-006 | Có số đồng hồ đầu thì bắt buộc ngày bắt đầu thực tế. | [Gói: Bảo dưỡng đội xe] | Lưu lệnh | FR-fleetio-repair-006 | `Chạy` | `Chạy` |
| BR-fleetio-repair-007 | Hoàn thành cần số đồng hồ nếu bật luật Require a Meter Reading: áp cho cả lưu Service Entry và lệnh completed; loại trừ được theo loại xe. Dùng số đầu cho số cuối nếu giữ tick. | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Hoàn thành | FR-fleetio-repair-012 | `Chạy` #99, #104, `Xem` Excluded Vehicle Types | `Chạy` |
| BR-fleetio-repair-008 | Bật được bắt buộc: phân loại ưu tiên, lý do sửa, nhóm hệ thống, phiếu kiểm tra (`Xem`, đang tắt); kho phụ tùng, xong hết dòng, ba trường Triệu chứng, Nguyên nhân, Khắc phục (`Docs`). | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Hoàn thành | FR-fleetio-repair-012, FR-fleetio-repair-035 | `Xem`, `Docs` Maintenance Settings | `Xem`, `Docs` |
| BR-fleetio-repair-009 | Luật mã phân loại chỉ áp cho bản ghi tạo sau khi bật. | [Cấu hình] | Bật luật | FR-fleetio-repair-012 | `Docs` | `Docs` |
| BR-fleetio-repair-010 | Số lệnh tiếp theo không thấp hơn số cao nhất đã dùng. | [Cấu hình] | Cấu hình | FR-fleetio-repair-006 | `Docs`, `Xem` câu "The current highest number" | `Xem` |
| BR-fleetio-repair-011 | Lệnh đã xong khoá Edit, kéo theo khoá đồng hồ, dòng việc; mở lại lệnh thì xoá Service Entry. | [Gói: Bảo dưỡng đội xe] | Mở lại | FR-fleetio-repair-013 | `Chạy` #104 | `Chạy` |
| BR-fleetio-repair-012 | Assessment của lệnh chỉ chạy khi có đầu việc và có chi phí dòng; của entry cần có dòng việc. | [Gói: Bảo dưỡng đội xe] | Chạy đánh giá | FR-fleetio-repair-021 | `Chạy` #103, #106, #107, entry 57856983 | `Chạy` |
| BR-fleetio-repair-013 | AI tự gán ưu tiên áp cho sự cố từ phiếu kiểm tra, mã lỗi theo tài liệu; quan sát thấy cả sự cố nhập tay, nhưng không phải mọi sự cố. | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Tạo sự cố | FR-fleetio-repair-019 | `Docs`, `Chạy` | `Chạy` |
| BR-fleetio-repair-014 | Quá hạn khi ngày hiện tại đã qua Due Date, hoặc đồng hồ hiện tại lớn hơn hẳn Due Odometer. Đúng bằng hạn đồng hồ hoặc hạn ngày đúng hôm nay vẫn là Open. | [Gói: Bảo dưỡng đội xe] | Đọc sự cố | FR-fleetio-repair-005 | `Chạy` #34 đến #38 | `Chạy` |
| BR-fleetio-repair-015 | Không chặn, không cảnh báo khi hạn đã nằm trong quá khứ; Timeline không ghi đổi Overdue. | [Gói: Bảo dưỡng đội xe] | Lưu sự cố | FR-fleetio-repair-005 | `Chạy` #33 | `Chạy` |
| BR-fleetio-repair-016 | Close thì Note tuỳ chọn; Resolve with Note thì Note bắt buộc. Ghi chú đóng thành một Comment của người đóng, Comment còn sau khi mở lại. | [Gói: Bảo dưỡng đội xe] | Đóng, giải quyết | FR-fleetio-repair-004, FR-fleetio-repair-026 | `Chạy` | `Chạy` |
| BR-fleetio-repair-017 | Reopen không có điều kiện với sự cố đóng, giải quyết bằng ghi chú, bằng entry. Mở lại sự cố giải quyết bằng entry tháo liên kết, entry vẫn còn. | [Gói: Bảo dưỡng đội xe] | Mở lại | FR-fleetio-repair-027 | `Chạy` #37 | `Chạy` |
| BR-fleetio-repair-018 | Một sự cố chỉ ở một lệnh khi chọn từ form lệnh; phải gỡ khỏi lệnh cũ mới thêm được vào lệnh khác. Đã gắn lệnh thì khoá Add to Service Entry, Add to Work Order, Resolve with Note, Close. Draft Work Order không đưa được sự cố sang lệnh thứ hai: chính sự cố đó xám trên #45; sự cố khác cùng xe được AI gợi ý thì không chuyển lệnh. | [Gói: Bảo dưỡng đội xe] | Gắn sự cố | FR-fleetio-repair-031 | `Chạy` | `Chạy` |
| BR-fleetio-repair-019 | Service Entry bắt buộc Odometer, Completion Date, không cần dòng việc; số đồng hồ thấp hơn hiện tại vẫn lưu, không cảnh báo, không đổi số hiện tại. | [Gói: Bảo dưỡng đội xe] | Lưu entry | FR-fleetio-repair-014 | `Chạy` entry 57856983 | `Chạy` |
| BR-fleetio-repair-020 | Đổi Completed bắt buộc Started At trước, rồi đồng hồ đầu theo Require a Meter Reading; thiếu thì trạng thái giữ nguyên. | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Hoàn thành | FR-fleetio-repair-012 | `Chạy` #104, #101, WO #102 | `Chạy` |
| BR-fleetio-repair-021 | Có số cuối thì bắt buộc Actual Completion Date; số cuối phải lớn hơn hoặc bằng số đầu. Không so với số hiện tại của xe. Số đầu bị kiểm theo dòng đồng hồ cùng thời điểm, có lần chặn do lệch múi giờ. | [Gói: Bảo dưỡng đội xe] | Lưu lệnh | FR-fleetio-repair-029 | `Chạy` #104; `Chạy` nhóm Nhắc #101 | `Chạy` |
| BR-fleetio-repair-022 | Tồn trừ lúc lưu dòng có kho, không chờ hoàn thành. Hoàn thành và mở lại lệnh không ghi sổ kho. Sửa số lượng, xoá dòng ghi bù. Tồn âm được, không chặn. | [Gói: Bảo dưỡng đội xe] | Lưu lệnh | FR-fleetio-repair-032 | `Chạy` K10 đến K16, #103, #104 | `Chạy` |
| BR-fleetio-repair-023 | Mở lại lệnh: xoá entry, sự cố về Open, giữ đồng hồ, giữ tồn. Hộp xác nhận chỉ báo khôi phục dữ liệu archive. | [Gói: Bảo dưỡng đội xe] | Mở lại | FR-fleetio-repair-013 | `Chạy` #104 | `Chạy` |
| BR-fleetio-repair-024 | Hoàn thành lại giữ ngày và đồng hồ cũ của lệnh, nên Resolved Date và Time to Resolve không đổi. Có thể sinh dòng đồng hồ trùng nguồn entry. | [Gói: Bảo dưỡng đội xe] | Hoàn thành lại | FR-fleetio-repair-034 | `Chạy` #104 | `Chạy` |
| BR-fleetio-repair-025 | Entry sinh từ lệnh khoá Edit, phải bấm Run Assessment; entry tạo tay sửa được, lưu lại không đổi gì vẫn báo thành công. | [Gói: Bảo dưỡng đội xe] | Sửa entry | FR-fleetio-repair-012, FR-fleetio-repair-014 | `Chạy` | `Chạy` |
| BR-fleetio-repair-026 | Số lệnh trên form là số dự kiến; trùng khi lưu thì tự nhảy, không báo lỗi. | [Lõi] | Lưu lệnh | FR-fleetio-repair-006 | `Chạy` form 101, lưu #103 | `Chạy` |
| BR-fleetio-repair-027 | Contact mẫu không dùng được với xe không mẫu. Lúc tạo lệnh không chặn; mọi lần sửa về sau báo lỗi, lệnh kẹt. | [Gói: Bảo dưỡng đội xe] | Sửa lệnh | FR-fleetio-repair-009 | `Chạy` #103 | `Chạy` |
| BR-fleetio-repair-028 | Make a Copy chép dòng việc, dòng công sau khi chọn xe; không chép xe, sự cố, ngày, đồng hồ; chưa có số lệnh tới khi lưu. | [Gói: Bảo dưỡng đội xe] | Sao chép | FR-fleetio-repair-018 | `Chạy` | `Chạy` |
| BR-fleetio-repair-029 | Nháp AI: việc và sự cố bị bỏ tick không vào lệnh; việc đề xuất gom từ sự cố khác cùng xe; Discard mất ngay, không hỏi, không ghi Timeline. | [Gói: Bảo dưỡng đội xe] | Duyệt nháp | FR-fleetio-repair-020 | `Chạy` #45, #46, #106 | `Chạy` |
| BR-fleetio-repair-030 | Cơ hội bảo hành khớp theo mã phân loại của Service Task, không theo phụ tùng; không có bảo hành thì không có cơ hội. | [Gói: Bảo dưỡng đội xe] | Sửa lệnh | FR-fleetio-repair-038 | `Chạy` WO #100 | `Chạy` |
| BR-fleetio-repair-031 | Tên đầu việc không trùng; Archive giữ bản ghi nhưng không dùng được nữa. | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Tạo, lưu trữ | FR-fleetio-repair-041 | `Chạy` | `Chạy` |
| BR-fleetio-repair-032 | Assessment tự chạy trên lệnh khi đủ điều kiện; trên entry phải bấm. Menu đổi Run thành Rerun sau lần đầu. | [Gói: Bảo dưỡng đội xe] | Đánh giá | FR-fleetio-repair-021 | `Chạy` | `Chạy` |
| BR-fleetio-repair-033 | Nhận hàng vào lệnh đi qua kho: cộng kho trước, trừ khi lưu lệnh; huỷ form thì hàng ở lại kho, đơn vẫn Full. | [Gói: Bảo dưỡng đội xe] | Nhận hàng | FR-fleetio-repair-037 | `Chạy` D14, D15 | `Chạy` |
| BR-fleetio-repair-034 | Gỡ sự cố khỏi lệnh xoá luôn dòng "added this issue" trên Timeline, không để vết. | [Gói: Bảo dưỡng đội xe] | Sửa lệnh | FR-fleetio-repair-031 | `Chạy` #45, #107 | `Chạy` |
| BR-fleetio-repair-035 | Thứ tự tính tổng lệnh: Parts Markup phần trăm tính trên Parts; giảm giá phần trăm tính trên Subtotal (công cộng phụ tùng, chưa markup); thuế phần trăm tính trên Subtotal cộng markup, trừ credit, trừ giảm giá. Markup phụ tùng cố định cộng vào Total nhưng không vào cơ số thuế ở trang chi tiết, trong khi xem trước trên form có tính: E-fleetio-repair-026. Suy từ các bộ số, khớp cả 6 bộ đã đo. | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Lưu lệnh | FR-fleetio-repair-010 | `Chạy` #107, thứ tự là `Suy` | `Chạy`, thứ tự `Suy` |
| BR-fleetio-repair-036 | Khớp bảo hành đúng từng mức mã: mã hệ thống chỉ khớp dòng đúng mức hệ thống, không bao trùm assembly bên dưới; muốn khớp dòng có assembly phải khai đủ hai mức. Trái với cách đọc tự nhiên của "System code". | [Gói: Bảo dưỡng đội xe] | Tính cơ hội | FR-fleetio-repair-038 | `Chạy` #107, #110 | `Chạy` |
| BR-fleetio-repair-037 | Chỉ bảo hành Active sinh cơ hội. Expired không gợi ý; Expiring Soon vẫn hiệu lực cũng không gợi ý, một lần đo. | [Gói: Bảo dưỡng đội xe] | Tính cơ hội | FR-fleetio-repair-038 | `Chạy` #110, Expiring Soon một lần đo | `Chạy` |
| BR-fleetio-repair-038 | Cơ hội chỉ tính lại khi chính lệnh được mở form hoặc lưu lại: trang chi tiết giữ kết quả cũ, form hiện ngay, lưu thì chi tiết cập nhật. Bảo hành đổi không lan sang lệnh không sửa. | [Gói: Bảo dưỡng đội xe] | Sửa lệnh | FR-fleetio-repair-038 | `Chạy` #106, #110 | `Chạy` |
| BR-fleetio-repair-039 | Gắn sự cố vào entry có sẵn: Resolved Date, Resolved Meter Entry lấy theo entry, kể cả entry cũ hơn lúc báo sự cố. Không chặn, không cảnh báo, nên Time to Resolve có thể âm. | [Gói: Bảo dưỡng đội xe] | Lưu entry | FR-fleetio-repair-028 | `Chạy` #52, 57856983 | `Chạy` |
| BR-fleetio-repair-040 | Bỏ tick sự cố trong entry đưa sự cố về Open, không hỏi xác nhận, mất Resolution Details, Timeline chỉ còn "opened this issue". Sự cố đang ở lệnh khác có ổ khoá, không bỏ tick được từ entry. | [Gói: Bảo dưỡng đội xe] | Sửa entry | FR-fleetio-repair-028 | `Chạy` #52, #35, #37 | `Chạy` |
| BR-fleetio-repair-041 | Nháp AI thêm vào lệnh đang có chỉ nêu lệnh mở mới nhất. Sự cố khác cùng xe đang ở lệnh khác giữ nguyên lệnh đó; đầu việc gợi ý của nó vẫn vào lệnh mới, không hỏi khi tạo dòng trùng. | [Gói: Bảo dưỡng đội xe] | Duyệt nháp | FR-fleetio-repair-020 | `Chạy` #52, #53, #45, #107, #110 | `Chạy` |
| BR-fleetio-repair-042 | Người bấm tạo lệnh, kể cả từ nháp AI, thành người theo dõi. User được giao tự thành người theo dõi; liên hệ không đăng nhập thì không; xe không tự theo dõi. Danh sách thêm chỉ có các mục xám khoá vì tài khoản một người. | [Gói: Bảo dưỡng đội xe] | Tạo, giao | FR-fleetio-repair-033 | `Chạy` #106, #110, TEST-SUA-01 | `Chạy` |
| BR-fleetio-repair-043 | Luật mã lỗi áp khi Code khớp chính xác mã đến. Ignore Code bỏ qua mọi lần xuất hiện của mã với mọi xe; Flag as Critical đánh dấu Critical, nêu ở dashboard và trang xe; Off không xử lý đặc biệt. | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Nhận mã | FR-fleetio-repair-024 | `Xem` hộp Add Fault Rule, không lưu | `Xem` |
| BR-fleetio-repair-044 | Đếm trên khối bảo hành: Expired vẫn tính vào total. | [Gói: Bảo dưỡng đội xe] | Đọc lệnh | FR-fleetio-repair-038 | `Chạy` #110 | `Chạy` |
| BR-fleetio-repair-045 | "Save & Add Another" của bảo hành giữ xe, loại bảo hành, Start Date, Unlimited, mã Maintenance; chỉ xoá tên và thời hạn. | [Gói: Bảo dưỡng đội xe] | Lưu bảo hành | FR-fleetio-repair-044 | `Chạy` | `Chạy` |
| BR-fleetio-repair-046 | Dòng công: chọn kỹ thuật viên điền đơn giá theo contact; có Time Entry thì End bằng Start cộng số giờ. | [Gói: Bảo dưỡng đội xe] | Thêm công | FR-fleetio-repair-009, FR-fleetio-repair-045 | `Chạy` #107 | `Chạy` |
| BR-fleetio-repair-048 | Trạng thái tuỳ biến chỉ mang hai loại. Mọi trạng thái loại Completed có cùng điều kiện và hiệu ứng với Completed gốc: bắt buộc Started At, sinh Service Entry, khoá Edit; không có bước riêng như chờ nghiệm thu. | [Lõi] [Cấu hình] | Đổi trạng thái | FR-fleetio-repair-036, FR-fleetio-repair-012 | `Chạy` #106 | `Chạy` |
| BR-fleetio-repair-049 | Không ràng buộc thứ tự: Incomplete bất kỳ sang Incomplete hay Completed bất kỳ. Giữa hai trạng thái Completed không hỏi, giữ nguyên Service Entry. Completed sang Incomplete bất kỳ, kể cả tuỳ biến, qua hộp "Update Status" và xoá Service Entry; hộp không báo việc xoá. | [Gói: Bảo dưỡng đội xe] | Đổi trạng thái | FR-fleetio-repair-036, FR-fleetio-repair-013 | `Chạy` #106 | `Chạy` |
| BR-fleetio-repair-050 | Trạng thái đang có lệnh dùng không đổi được loại, không xoá được; hết lệnh thì ô tick trở lại. Trạng thái gốc sửa được tên, mô tả, màu. Mỗi lúc một Default, form lệnh mới chọn sẵn trạng thái đó. | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Cấu hình | FR-fleetio-repair-036 | `Chạy`; Delete `Xem` | `Chạy` |
| BR-fleetio-repair-051 | Áp mẫu sinh bảo hành riêng cho từng coverage, vẫn liên kết với mẫu; mã phân loại theo coverage khớp cơ hội trên lệnh như bảo hành thường. | [Gói: Bảo dưỡng đội xe] | Lưu bảo hành | FR-fleetio-repair-046 | `Chạy` | `Chạy` |
| BR-fleetio-repair-052 | Sửa mẫu đã dùng: lựa chọn tương lai là mặc định; lựa chọn quá khứ cập nhật mọi bảo hành đã sinh, nêu số xe bị ảnh hưởng và ghi đè phần sửa riêng theo câu cảnh báo. | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Sửa mẫu | FR-fleetio-repair-046 | `Chạy` áp quá khứ, End Date đổi; ghi đè là câu cảnh báo, chưa kiểm | `Chạy` một phần |
| BR-fleetio-repair-053 | Danh sách mẫu trên form bảo hành không lọc theo hãng xe: xe Freightliner vẫn thấy mẫu Ford. Xe mi thấy OEM mi, xe km thấy mẫu km: lọc theo đơn vị đồng hồ là suy từ 2 lần quan sát. "No options" trước đây do chưa có mẫu đúng điều kiện, không phải do thiếu Make. | [Gói: Bảo dưỡng đội xe] | Chọn mẫu | FR-fleetio-repair-046 | `Xem` BSA100TRNS, `Chạy` TEST-SUA-01; lọc đơn vị là `Suy` | `Chạy`, lọc đơn vị `Suy` |
| BR-fleetio-repair-054 | Bật Shop Network đi qua thiết lập tài khoản thanh toán Fleetio Pay. Vì sao bị từ chối chưa biết. | [Gói: Bảo dưỡng đội xe] | Bật tính năng | FR-fleetio-repair-039 | `Chạy` một lần bấm | `Chạy` |
| BR-fleetio-repair-047 | PDF của lệnh hiện giờ theo múi giờ tài khoản, tiền dạng US; web hiện giờ theo máy, tiền dạng Việt Nam. Số tiền hai bên khớp nhau trên lệnh chỉ có công. | [Gói: Bảo dưỡng đội xe] | In lệnh | FR-fleetio-repair-018 | `Chạy` #107 | `Chạy` |

**Tham số mới cần có nếu Invlogis lấy, chưa có mã:** bắt buộc số đồng hồ khi hoàn thành và loại xe được miễn; bắt buộc phân loại ưu tiên, lý do sửa, nhóm hệ thống; cho phép tồn âm; số lệnh tiếp theo. Fleetio: mặc định bật bắt buộc số đồng hồ, các mục còn lại tắt.

## 6. Error Matrix

Wording giữ nguyên tiếng Anh của Fleetio. Các lỗi có chữ "không báo" là lỗi im lặng do người chạy phát hiện, Fleetio không hiện thông báo nào.

| Error ID | Title | Trigger | Severity | Related FR | Screen state | Recovery | Mức |
|---|---|---|---|---|---|---|---|
| E-fleetio-repair-001 | Thiếu ngày bắt đầu khi có số đầu | Có số đồng hồ đầu, thiếu ngày: "Start Odometer is invalid", "can't be blank if an odometer value is entered" | major | FR-fleetio-repair-006 | Dải lỗi đầu form, viền đỏ, toast "Work Order could not be updated" | Nhập ngày | `Chạy` |
| E-fleetio-repair-002 | Thiếu số đồng hồ cuối | Hoàn thành thiếu số cuối: "Please edit and fix the following errors: Ending Meter Entry can't be blank (per your account settings)" | major | FR-fleetio-repair-012 | Toast, trạng thái giữ nguyên | Sửa lệnh | `Chạy` #99 |
| E-fleetio-repair-003 | Lưu form sự cố trống | "You are not authorized to perform this action." | minor | FR-fleetio-repair-001 | Toast, không chỉ trường | Điền đủ. Không nên học | `Chạy` một lần |
| E-fleetio-repair-004 | Không đủ điều kiện đánh giá | "Add a service task to run an assessment.", "Add line item costs to run an assessment.", trên entry "Add a line item to run an assessment." | minor | FR-fleetio-repair-021 | Khối Assessment | Bổ sung | `Chạy` |
| E-fleetio-repair-005 | Sai tiền phụ tùng | Giá phụ tùng lưu đúng trong form nhưng trang chi tiết lệnh và Service Entry hiện gấp 100 lần: 300.000 thành 30.000.000 ₫, 5 thành 500 ₫, 12,5 thành 1.250 ₫; tổng 2.550.000 thành 255.000.000 ₫. Sửa so với bản trước: hộp Add Part không sai. Đơn giá tự điền 100000.00 từ danh mục ra 10.000.000 ₫/cái, làm sai cả Total, thuế, giảm giá | critical | FR-fleetio-repair-008 | Không báo lỗi. Ô parts_cost của form sửa theo số sai, dòng vẫn số cũ | Sửa bản trước: có đường né, gõ đơn giá chia 100 (1000) thì chi tiết đúng 100.000 ₫, form lại sai; lỗi của Fleetio, xem Mục 11 | `Chạy` |
| E-fleetio-repair-006 | Thiếu Started At khi hoàn thành | "Please edit and fix the following errors: Started At can't be blank" | major | FR-fleetio-repair-012 | Toast, trạng thái giữ nguyên | Nhập ngày bắt đầu | `Chạy` |
| E-fleetio-repair-007 | Thiếu đồng hồ đầu khi hoàn thành | "Starting Meter Entry can't be blank (per your account settings)", "Odometer can't be blank (per your account settings)"; ở WO #102 "Start Odometer can't be blank (per your account settings)" | major | FR-fleetio-repair-012 | Toast, trạng thái giữ nguyên | Nhập số đầu | `Chạy` |
| E-fleetio-repair-008 | Có số cuối, thiếu ngày hoàn thành | Ô Actual Completion Date "can't be blank", toast "Work Order could not be updated" | major | FR-fleetio-repair-029 | Viền ô, toast | Nhập ngày | `Chạy` |
| E-fleetio-repair-009 | Số cuối nhỏ hơn đầu | "Completion Odometer must be greater than or equal to start meter entry." | major | FR-fleetio-repair-029 | Banner đầu form | Sửa số | `Chạy` |
| E-fleetio-repair-010 | Kỹ thuật viên mẫu trên xe thường | "Contact is a sample, and cannot be used with non sample vehicles" | major | FR-fleetio-repair-009 | Báo ở mọi lần sửa, không báo lúc tạo | Không gỡ được ở lần thử; chỉ xảy ra với dữ liệu Sample | `Chạy` #103 |
| E-fleetio-repair-011 | Đổi dòng công hoặc trạng thái khi dòng công lỗi | "Work Order Labor Line Items is invalid", toast "Work Order could not be updated" | major | FR-fleetio-repair-011 | Toast, trạng thái giữ nguyên | Không có ở lần thử; lệnh kẹt | `Chạy` #103 |
| E-fleetio-repair-012 | Service Entry thiếu ngày | Ô Completion Date chỉ có placeholder giờ hiện tại, lưu báo "can't be blank", toast "Service Entry could not be created" | minor | FR-fleetio-repair-014 | Viền ô, toast. Odometer không báo riêng tới khi gõ | Gõ lại ngày. Không nên học. Lặp lại ở entry 57902070 | `Chạy` |
| E-fleetio-repair-013 | Trùng tên đầu việc | "has already been taken", toast "Service Task could not be created" | minor | FR-fleetio-repair-041 | Viền ô, toast | Đổi tên | `Chạy` |
| E-fleetio-repair-014 | Sai tiền công giữa các màn | Contact nhập 100.000: danh sách ghi 10.000.000 ₫/hr, hộp Edit Labor "Current default labor rate is ₫100000.00". Kỹ thuật viên mẫu: danh sách 480.000 ₫/hr, vào dòng 4.800 ₫ | critical | FR-fleetio-repair-040 | Không báo lỗi | Công nhập tay qua hộp lưu đúng | `Chạy` |
| E-fleetio-repair-015 | Xuất phụ tùng quá tồn | Không báo; tồn về âm (K12 còn -10,5; #100 còn -2) | major | FR-fleetio-repair-032 | Hộp chỉ ghi "This will make an inventory adjustment" | Nhập kho, chỉnh tồn | `Chạy` |
| E-fleetio-repair-016 | Tick sự cố không vào lệnh | Không báo; #34 không ở Resolved Issues nhưng cột Work Orders vẫn ghi #103 và bị khoá ở lệnh mới | major | FR-fleetio-repair-007 | Không báo lỗi | Chưa rõ nguyên nhân, xem OQ-11 | `Chạy` một lần |
| E-fleetio-repair-017 | Nháp AI hứa mà không làm | Hộp ghi "Repair Priority Class Non-Scheduled" sẽ tự điền; lệnh tạo ra để trống | minor | FR-fleetio-repair-020 | Không báo lỗi | Điền tay | `Chạy` #99, #106, #110 |
| E-fleetio-repair-018 | Số đồng hồ đầu chặn do thời điểm | "must be less than 2,499 or marked as void" dù đồng hồ hiện cao hơn; ngày lệnh lệch múi giờ tài khoản nên xếp trước các dòng đồng hồ mới | major | FR-fleetio-repair-029 | Viền ô | Nhập số thấp hơn | `Chạy` nhóm Nhắc #101 |
| E-fleetio-repair-019 | Sai markup trên form sửa | Không báo; form sửa hiện Labor Markup 2.000.000 ₫, chi tiết và Total dùng 20.000 ₫; Parts Markup 20% hiện 4.000.000 ₫, chi tiết 40.000 ₫. Cùng họ lỗi với E-fleetio-repair-005 | major | FR-fleetio-repair-010 | Không báo lỗi | Total vẫn đúng; đọc số ở trang chi tiết | `Chạy` #107 |
| E-fleetio-repair-020 | Time to Resolve âm | Không báo; gắn sự cố vào entry cũ hơn lúc báo sự cố, Time to Resolve "-15 hrs 16 mins" | major | FR-fleetio-repair-028 | Không báo lỗi, số âm trong Resolution Details | Bỏ tick trong entry; làm hỏng số liệu nếu để nguyên | `Chạy` #52 |
| E-fleetio-repair-021 | Câu AI sai thực tế | Không báo; hộp nháp viết "Both leaks were recently flagged and have no existing open work orders covering transmission or engine leak work." khi #45 đang ở lệnh mở #107, và không tính entry vừa làm đúng việc đó | major | FR-fleetio-repair-020 | Không báo lỗi | Người duyệt tự đối chiếu | `Chạy` #52, #107, 57902070 |
| E-fleetio-repair-022 | Dòng việc trùng từ nháp AI | Không hỏi khi tạo dòng; #110 có Engine Leak Inspection trong khi sự cố #45 vẫn chỉ ở #107 | major | FR-fleetio-repair-020 | Không báo lỗi | Bỏ tick việc đó ở hộp review | `Chạy` #110 |
| E-fleetio-repair-023 | End Date bảo hành lệch 1 ngày | Không báo; trang hiện 01/14/2027, 12/31/2024, 11/04/2026 trong khi form hiện đủ năm; bảo hành của TEST-XE-01 lượt trước ghi đủ năm. Chưa rõ nguyên nhân, xem OQ-20 | minor | FR-fleetio-repair-025 | Không báo lỗi | Chưa có | `Chạy` |
| E-fleetio-repair-024 | Thiếu đơn vị trên dòng xe của bảo hành | Không báo; trang bảo hành ghi "2,350 undefined" | minor | FR-fleetio-repair-025 | Không báo lỗi | Không ảnh hưởng số | `Chạy` 356513 |
| E-fleetio-repair-025 | Tick nhanh trong Link Issues không vào | Không báo; bấm Save ngay sau tick thì hộp đóng mà không tick, làm lại thì được. Liên hệ với E-fleetio-repair-016 là `Suy`, xem OQ-11 | minor | FR-fleetio-repair-007 | Hộp đóng như bình thường | Mở lại, tick, đợi rồi Save | `Chạy` một lần |
| E-fleetio-repair-026 | Markup cố định không vào cơ số thuế | Không báo; Parts Markup Fixed 15.000, trang chi tiết thuế 37.000, xem trước trên form 38.500. Markup phần trăm thì có vào cơ số. Đo 2 lần. Chưa rõ hãng cố ý hay lỗi VND | major | FR-fleetio-repair-010 | Hai màn hai số thuế | Chưa có | `Chạy` #107 |
| E-fleetio-repair-027 | Markup cố định còn trên lệnh không có phụ tùng | Không báo; xoá hết dòng phụ tùng, Parts 0 ₫ vẫn cộng 15.000 | minor | FR-fleetio-repair-010 | Không báo lỗi | Đưa markup về 0 | `Chạy` #107 |
| E-fleetio-repair-028 | PDF lệch ngày so với web | Không báo; Issue Date PDF "Mon, Nov 2, 2026 12:32 PM", web 11/03/2026 1:32am: PDF theo múi giờ tài khoản, web theo máy | major | FR-fleetio-repair-018 | Không báo lỗi; web có banner lệch múi giờ, PDF không | Đặt múi giờ tài khoản trùng máy: `Suy`, chưa thử | `Chạy` #107 |
| E-fleetio-repair-029 | Trạng thái lệnh thiếu tên | "can't be blank", toast "Work Order Status could not be created" | minor | FR-fleetio-repair-036 | Viền ô, toast | Nhập tên | `Chạy` |
| E-fleetio-repair-030 | Trùng tên trạng thái lệnh | "has already been taken" | minor | FR-fleetio-repair-036 | Viền ô | Đổi tên | `Chạy` |
| E-fleetio-repair-031 | Đổi loại trạng thái đang dùng | "cannot be changed if work orders are assigned", toast "Work Order Status could not be updated" | major | FR-fleetio-repair-036 | Toast, loại giữ nguyên | Chuyển hết lệnh sang trạng thái khác | `Chạy` |
| E-fleetio-repair-032 | Start Meter bảo hành chỉ giữ ký tự đầu, nghi vấn | Gõ 2365 ở form New Warranties, ô chỉ giữ "2": lúc gõ ký tự đầu, dòng hiện thêm nút sao chép, ô mất tiêu điểm. Lưu ra Start Meter 2 km, End Meter 100.002 km. Lặp 2/2 lần bằng gõ tự động, chưa thử tay: **chưa kết luận lỗi của Fleetio hay của công cụ gõ**. Phần chắc chắn của Fleetio: không cảnh báo khi lệch xa đồng hồ xe 2.365 | major | FR-fleetio-repair-025, FR-fleetio-repair-046 | Không báo lỗi | Sửa lại số; xem OQ-26 | `Chạy` 2/2, nguyên nhân chưa rõ |
| E-fleetio-repair-033 | Bật Shop Network bị từ chối | Bấm Enable Shop Network sang `fleetio_pay/account_setup/new`: "Access Denied", "You do not have access to the requested URL." | major | FR-fleetio-repair-039 | Trang lỗi, không nêu lý do | Không có; xem OQ-25 | `Chạy` một lần |

## 7. Success Criteria

| ID | Outcome nghiệp vụ | Đo bằng | Mốc đạt |
|---|---|---|---|
| SC-fleetio-repair-01 | Mọi sự cố truy được đến cách xử lý | Tỷ lệ sự cố có lệnh, entry hoặc ghi chú | TBD |
| SC-fleetio-repair-02 | Thời gian xử lý đo tự động | Fleetio có Time to Resolve, Kilometers to Resolve | Có sẵn khi lưu |
| SC-fleetio-repair-03 | Không nhập lại khi hoàn thành lệnh | Đếm thao tác từ hoàn thành đến lịch sử | Một thao tác |

## 8. Data Entities (tóm tắt — chi tiết ở erd.md)

Issue, Work Order, Work Order Line Item, Labor Line, Time Entry, Part Line, Service Entry, Service Task, Fault, Fault Rule, Warranty, Warranty Code, Warranty Component, AI Draft, Assessment, Meter Entry, Inventory Activity, Contact, Work Order Status, Record History, Watcher. Chi tiết: [[docs/_research/fleetio/srs/fleetio-repair-erd.md|ERD]].

## 9. Flows (tóm tắt — chi tiết ở flows.md)

Sự cố đến hoàn thành lệnh; mở lại, hoàn thành lại; hạn và quá hạn; đóng, giải quyết bằng ghi chú, bằng entry; khoá và gỡ sự cố; dòng phụ tùng và tồn; AI soạn lệnh; AI đánh giá; sao chép; đầu việc; bảo hành; nhận hàng vào lệnh; ghi công; tính tổng; Link Issues; khớp bảo hành, hồ sơ bảo hành; gắn và bỏ sự cố ở entry; luật mã lỗi; người theo dõi. Chi tiết: [[docs/_research/fleetio/srs/fleetio-repair-flows.md|Flows]], [[docs/_research/fleetio/srs/fleetio-repair-states.md|States]], [[docs/_research/fleetio/srs/fleetio-repair-usecases.md|Use case]], [[docs/_research/fleetio/srs/fleetio-repair-userflow.md|User flow]].

## 10. Screens

Ảnh thật và bảng mô tả: [[docs/_research/fleetio/srs/fleetio-repair-screens.md|Màn hình]].

### Cấu hình UI Common Rules & Components

Không áp `CMP`, `GR`: tài liệu mô tả sản phẩm của bên khác. Khi chuyển sang Invlogis mới đối chiếu.

## 11. Constraints, Dependencies & Assumptions

**Giải pháp đáng học:**

| Điểm | Vì sao | Mức |
|---|---|---|
| Overdue là giá trị tính | Không cần tác vụ nền đổi trạng thái; đúng cho hạn theo km của đầu kéo vì đồng hồ đổi liên tục | `Chạy` |
| Một sự cố một lệnh, gắn lệnh thì khoá lối khác | Tránh hai xưởng cùng sửa một lỗi; tooltip nêu cách gỡ | `Chạy` |
| Trừ kho từ lúc lưu dòng, xoá dòng có bút toán đảo ghi nguồn | Phù hợp xưởng cấp phụ tùng trước khi sửa; dễ đối soát; WO Current Qty cho thấy hàng đã giữ cho lệnh đang sửa | `Chạy` |
| Tên trạng thái do khách đặt, nghiệp vụ gắn vào hai loại cố định | Đúng mô hình lõi cố định, tên theo cấu hình; khoá đổi loại khi đã có lệnh tránh lịch sử sai nghĩa | `Chạy` |
| Mẫu có lựa chọn tương lai hay cả quá khứ, nêu số xe bị ảnh hưởng | Áp được cho mẫu giá thuê, định mức, chính sách; áp mẫu cho nhiều xe, mỗi xe một mốc | `Chạy` |
| Giao cho user tự thành người theo dõi | Người nhận việc có thông báo mà không cần thao tác; liên hệ không đăng nhập thì không | `Chạy` |
| Nhận hàng vào lệnh qua kho hai bước | Hàng không mất khi huỷ form; hợp phụ tùng đặt riêng cho xe nằm xưởng | `Chạy` |
| AI nháp chạy nền, gom sự cố cùng xe, cảnh báo lệnh đang mở | Đỡ đưa xe vào xưởng hai lần, quý với đầu kéo | `Chạy` |
| Assessment soi lệnh khác cùng xe trùng đầu việc | Phát hiện hai lệnh làm cùng việc | `Chạy` |
| Bảo hành khớp theo mã đầu việc | Cơ hội hiện ngay trên lệnh; xưởng thấy việc đòi hãng khi lập lệnh | `Chạy` |
| Record History theo từng trường tiền | Đủ để đối soát khi sửa lệnh đã tính chi phí | `Chạy` |
| Tooltip khoá nói rõ cách gỡ | Người dùng biết phải gỡ khỏi lệnh nào trước khi đổi lối xử lý | `Chạy` |

**Điểm không nên học (`Chạy`):**

| Điểm | Thấy gì | Nên làm ở Invlogis |
|---|---|---|
| Ghi trùng số km | #99 đóng lệnh sinh 3 dòng: đầu, cuối từ lệnh và cuối từ Service Entry. #104 lần đầu 2 dòng, hoàn thành lại thêm dòng trùng nguồn entry | Ghi một lần cho mỗi lần hoàn thành |
| Nháp AI lệch | Ghi tự điền Non-Scheduled, lệnh tạo ra để trống | Điền đúng như hứa |
| Lệch tiền | Sửa lại: form đúng, trang chi tiết và entry gấp 100 lần với ₫; đơn giá công lệch theo chiều khác; đơn giá tự điền từ danh mục làm sai cả Total | Lưu tiền theo số lẻ của từng loại tiền, không cứng 2 số lẻ; ca kiểm thử định dạng tiền Việt ở mọi màn |
| PDF khác múi giờ web | Một lệnh hiện 2 ngày khác nhau | Một múi giờ cho mọi kênh, in kèm múi giờ |
| Markup cố định lệch thuế | Form tính thuế gồm markup cố định, chi tiết thì không; xoá hết phụ tùng vẫn cộng | Một công thức cho mọi màn; cảnh báo khi cơ số về 0 |
| Xoá Service Entry khi mở lại | `Chạy`: URL ra Not Found, không còn bản xem được | Giữ vết, ghi lần mở lại |
| Hộp mở lại thiếu hậu quả | Không nói entry bị xoá, sự cố mở lại; lặp lại với trạng thái tuỳ biến (#106) | Nêu rõ từng hậu quả trước khi xác nhận |
| Không khai được thứ tự chuyển, vai trò | Lệnh nhảy thẳng từ chờ phụ tùng sang Completed | Quy trình duyệt cần thứ tự chuyển hoặc phân quyền; xem OQ-28 |
| Nhiều trạng thái Completed giống nhau | "Chờ nghiệm thu" đã sinh Service Entry và khoá lệnh | Tách trạng thái chờ khỏi nhóm hoàn thành |
| Áp mẫu về quá khứ ghi đè phần sửa riêng | Chỉ có cảnh báo, không so sánh trước sau | Hiện trước sau từng xe, cho loại trừ |
| Thư viện OEM thuần xe con Mỹ | 14 mẫu Ford, Chevrolet; không có đầu kéo; không lọc theo hãng | Mẫu riêng của khách; không chép thư viện |
| Không chặn Start Meter lệch xa đồng hồ xe | Lưu 2 km khi xe 2.365 km | Cảnh báo khi lệch |
| Mở lại không đảo đồng hồ | Dòng 2.300, 2.350 còn nguyên | Huỷ dòng theo lần mở lại |
| Hoàn thành lại giữ ngày cũ | Time to Resolve 23 mins dù hoàn thành lại sau 41 phút | Hỏi lại ngày, tính lại chỉ số |
| Timeline thiếu | Không ghi Overdue, đóng, mở lại, gỡ; có chỗ xoá dòng cũ, có chỗ giữ dòng cũ | Ghi đủ, không xoá dòng |
| Tồn âm im lặng | Không cảnh báo | Cảnh báo; chặn hay không theo khách, tham số mới, chưa có mã |
| AI đánh giá sai | Giá 30 triệu vẫn Acceptable; nêu quá hạn đã không còn | Chỉ gợi ý, không làm điều kiện |
| Discard không hỏi | Mất nháp ngay | Xác nhận, ghi vết |
| Toast cũ nổi lại | "Issue #36 was closed." hiện ở trang #38 | Xoá toast khi rời trang |
| Khớp bảo hành đúng mức mã | Mã hệ thống không phủ assembly; khai "toàn hệ thống động cơ" sẽ trượt phần lớn dòng | Cho mã cha phủ mã con |
| Expiring Soon không gợi ý | Còn hiệu lực mà không gợi ý, đúng lúc cần đòi nhất; một lần đo | Gợi ý mọi bảo hành còn hiệu lực, nêu sắp hết |
| Không có quy trình claim | Ba ô chữ; Warranty Credits nhập tay; không theo dõi hãng đã trả chưa | Nếu Delta cần đòi hãng: có trạng thái, nối credit |
| Time to Resolve âm | Gắn sự cố vào entry cũ làm hỏng số liệu | Chặn, hoặc lấy mốc lúc gắn |
| AI nêu sai, sinh dòng trùng | Viết "no existing open work orders" khi đang có lệnh mở | Giữ bước người duyệt như hộp Review; cảnh báo dòng trùng |
| Lưu liên tiếp giữ mã | Dễ lưu nhầm mã của bảo hành trước | Xoá mã khi lưu liên tiếp, hoặc hỏi lại |

**Đầu kéo, mooc:** `Chạy` ở nhóm Lốp: mooc là một Vehicle độc lập, đồng hồ riêng. `Suy` cho nhóm này (lượt sửa chữa chỉ chạy xe Car): sự cố, lệnh gắn một Vehicle; hỏng cả đầu kéo và mooc phải tạo hai lệnh; hạn đồng hồ của sự cố trên mooc theo đồng hồ riêng của mooc, không tự cộng từ đầu kéo. Đề xuất Invlogis: lệnh gắn tổ hợp đầu kéo cùng mooc.

**Giả định:**

| Giả định | Invalidate nếu sai |
|---|---|
| `GĐ` Bước báo giá của Delta chen giữa sự cố và lệnh | UC-run-work-order phải đổi |
| `GĐ` Quyền trên tài khoản chủ không phản ánh vai trò thường | Nhánh chờ duyệt, phân quyền cần thử bằng user khác |

**Phụ thuộc:** AI Service Advisor, Fault cần tích hợp thiết bị hoặc gói của Fleetio.

## 12. Open Questions

* [ ] OQ-1: Delta có gom sự cố mọi nguồn về một bản ghi không? Phần Fleetio: có gom. — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-2: Một lệnh có giải quyết nhiều sự cố không? Phần Fleetio: có. — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-3: Ai được mở lại lệnh đã xong, xử lý chi phí thế nào? — Nguồn khách: chưa có trong tài liệu khách gửi
* [x] OQ-4: Fleetio có giới hạn số lần mở lại, có lưu lịch sử khi xoá Service Entry không? Trả lời: hai lượt không thấy giới hạn; entry bị xoá hẳn, URL ra Not Found, không có bản lưu xem được theo URL. `Chạy` — Nguồn khách: không áp dụng
* [x] OQ-5: Mở lại lệnh thì dòng đồng hồ đã ghi, nhắc đã reset, tỷ lệ tuân thủ, Time to Resolve xử lý thế nào? Trả lời một phần: đồng hồ giữ nguyên, có dòng trùng khi hoàn thành lại; Time to Resolve mất khi mở, hoàn thành lại lấy ngày cũ. Nhắc và tỷ lệ tuân thủ khi mở lại chưa kiểm, chuyển sang OQ-10. `Chạy` — Nguồn khách: không áp dụng
* [x] OQ-6: Xoá lệnh hoặc xoá dòng phụ tùng có hoàn kho và ghi sổ không? Trả lời một phần: xoá dòng hoàn kho và ghi Inventory Activity; tồn âm được. Xoá lệnh chưa chạy, chuyển sang OQ-12. `Chạy` — Nguồn khách: không áp dụng
* [ ] OQ-7: Sửa ngoài có cần lập lệnh hay chỉ ghi lịch sử? Phần Fleetio: chỉ ghi lịch sử được. — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-8: Thiết bị GPS của Delta có đọc được mã lỗi động cơ không? — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-9: Delta có theo dõi bảo hành xe, phụ tùng không? — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-10: Mở lại lệnh có hoàn nhắc đã reset và tỷ lệ tuân thủ không? Xe TEST-SUA không gắn nhắc. — Nguồn khách: không áp dụng
* [ ] OQ-11: Vì sao #34 tick vào #103 mà không ở Resolved Issues? Chạy một lần, chưa rõ. Lượt 3 thấy tick nhanh rồi Save trong Link Issues cũng rơi (E-fleetio-repair-025); chưa chứng minh là cùng nguyên nhân (`Suy`). — Nguồn khách: không áp dụng
* [ ] OQ-12: Xoá cả lệnh có hoàn kho, hoàn đồng hồ, mở lại sự cố không? Không chạy vì xoá vĩnh viễn. — Nguồn khách: không áp dụng
* [ ] OQ-13: Điều kiện nào sinh dòng đồng hồ trùng: #99 lần đầu có, #104 lần đầu không, lần 2 có? — Nguồn khách: không áp dụng
* [x] OQ-14: Draft Work Order từ sự cố đã gắn lệnh, chọn lệnh khác thì sự cố có ở hai lệnh không? Tooltip viết "all Work Orders". Chưa thử. Trả lời lượt 3: sự cố chỉ ở 1 lệnh; AI gợi ý đè lên thì sinh dòng việc trùng mà không gắn sự cố, viết sai "no existing open work orders" (`Chạy`) — Nguồn khách: không áp dụng
* [x] OQ-15: Close có dùng được khi sự cố đang gắn lệnh không? Chưa thử. Trả lời lượt 3: Close bị khoá khi sự cố đang gắn lệnh (`Chạy`) — Nguồn khách: không áp dụng
* [ ] OQ-16: Trạng thái tuỳ biến, phân quyền theo nhóm lệnh, Add to Existing Service Entry, bỏ tick sự cố trong entry, nút claim bảo hành chạy thế nào? Chưa thử. Một phần lượt 3: không có nút claim, chỉ 3 ô chữ; bỏ tick trong entry đưa sự cố về Open, không để lại vết; Add to Existing Service Entry chạy được, xem BR-fleetio-repair-039 (`Chạy`). Lượt 5: trạng thái tuỳ biến chạy được, xem BR-fleetio-repair-048 đến 050 (`Chạy`). Còn mở: phân quyền vì tài khoản một người. — Nguồn khách: không áp dụng
* [ ] OQ-17: Delta có cần lệnh gom cả đầu kéo và mooc không? — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-18: Xưởng Delta cấp phụ tùng lúc lập lệnh hay lúc xong việc? Quyết định thời điểm trừ kho. — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-19: Vì sao Draft Work Order xám trên #45 đang gắn #107, trong khi lượt trước còn dùng được trên sự cố đã gắn? Do lệnh, do #45 từng Discard, hay do hãng đổi. Lượt 5 cũng xám trên #46 đang gắn lệnh, nên không riêng #45. — Nguồn khách: không áp dụng
* [ ] OQ-20: Vì sao End Date trang chi tiết bảo hành sớm hơn form 1 ngày ở xe TEST-SUA-01, còn TEST-XE-01 ghi đủ năm? — Nguồn khách: không áp dụng
* [ ] OQ-21: Expiring Soon không gợi ý cơ hội có phải luật cố định không? Mới đo một lần, còn 1 ngày tới hạn; ngưỡng Expiring Soon chưa biết. — Nguồn khách: không áp dụng
* [ ] OQ-22: Bật Issue Resolution thì AI có đóng hoặc gợi ý đóng sự cố khi có Service Entry không, trễ bao lâu? Một phần lượt 4: với cấu hình hiện tại không đóng, không gợi ý sau khoảng 1 đến 2 giờ (#52) và 15 phút (#59) (`Chạy`). Còn mở: trạng thái bật thật, hành vi khi bật; không bấm vì có câu điều khoản. — Nguồn khách: không áp dụng
* [ ] OQ-23: Tình trạng từng dòng và luật bắt buộc xong hết dòng có bật được trong Settings không? Web chưa thấy ô đánh dấu. — Nguồn khách: không áp dụng
* [ ] OQ-24: Delta có cần quy trình đòi bảo hành có trạng thái, nối với khoản hãng trả không? Phần Fleetio: chỉ 3 ô chữ, credit nhập tay. — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-25: Vì sao bật Shop Network bị Access Denied: do gói dùng thử, vị trí hay quyền? Sau bước đó có điều khoản, phí không? Dừng vì là phần thanh toán. — Nguồn khách: không áp dụng
* [ ] OQ-26: Start Meter chỉ giữ ký tự đầu là lỗi Fleetio hay do gõ tự động? Lặp 2/2, chưa thử gõ tay. — Nguồn khách: không áp dụng
* [ ] OQ-27: Danh sách mẫu có lọc theo đơn vị đồng hồ không? Suy từ 2 lần quan sát, chưa thử mẫu Miles trên xe mi. — Nguồn khách: không áp dụng
* [ ] OQ-28: Delta có cần khống chế thứ tự chuyển trạng thái lệnh, người được chuyển, bước chờ nghiệm thu không? Phần Fleetio: không khai được. — Nguồn khách: chưa có trong tài liệu khách gửi

## 13. Ma trận case

Toàn bộ chạy trên tài khoản dùng thử. `Chạy` lượt 03/11 trên TEST-SUA-01 trừ khi ghi khác.

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| C01 Hạn ngày đã qua | Tạo #33 với hạn 11/01/2026 | Overdue ngay, không cảnh báo, không chặn | `Chạy` |
| C02 Hạn đúng hôm nay | #37 | Open | `Chạy` |
| C03 Đồng hồ đúng bằng hạn | #38: 2.200 trên 2.200 | Open | `Chạy` |
| C04 Đồng hồ dưới hạn 1 | #35: 2.200 trên 2.201 | Open | `Chạy` |
| C05 Đồng hồ vượt hạn | #36: 2.200 trên 2.199 | Overdue | `Chạy` |
| C06 Đồng hồ tăng qua hạn | Đồng hồ lên 2.350; #38, #35 | Tự thành Overdue, không ai thao tác | `Chạy` |
| C07 Đổi hạn sang tương lai | #33 sang 12/31/2026 | Về Open ngay, không có nút, không sự kiện | `Chạy` |
| C08 Tab Overdue | `state_scope=overdue` | 2 dòng #34, #36. Overdue vẫn thuộc nhóm Open, hiện chung tab Open ở form lệnh | `Chạy` |
| C09 Timeline khi đổi Overdue | C01, C05, C06, C07 | Không ghi | `Chạy` |
| C10 Đóng không ghi chú | #36 | Được; Closed Details gồm Closed Date, Closed By, Note; còn Unwatch, Reopen; mất Edit, Resolve | `Chạy` · issue-closed.jpg |
| C11 Đóng có ghi chú | #38 | Ghi chú thành một Comment của người đóng | `Chạy` |
| C12 Mở lại sự cố đã đóng | #38 | Hộp hỏi, về Open, Closed Details mất, Comment còn, Timeline chỉ có "opened this issue" | `Chạy` |
| C13 Toast cũ | Sang trang #38 sau khi đóng #36 | "Issue #36 was closed." nổi lại | `Chạy` |
| C14 Giải quyết ghi chú trống | Hộp Resolve Issue | Nút khoá | `Chạy` · issue-resolve-note-dialog.jpg |
| C15 Giải quyết có ghi chú | #35 | Resolved; Time to Resolve 5 mins; Kilometers to Resolve trống; mất Edit | `Chạy` · issue-resolved-note.jpg |
| C16 Mở lại sự cố giải quyết bằng ghi chú | #35 | Về Open, mất Resolution Details, comment giữ | `Chạy` |
| C17 Thêm vào entry mới | #37 | Tick sẵn, "1 Issue will be added", form entry, toast "1 Issue(s) were added to the form" | `Chạy` |
| C18 Thêm vào entry có sẵn | Hộp có lựa chọn | Lượt 2 chưa lưu; lượt 3 đã chạy, xem C144 đến C149 | `Xem` |
| C19 Entry không gõ ngày | Ô hiện giờ hiện tại | "can't be blank", "Service Entry could not be created"; Odometer không báo riêng tới khi gõ | `Chạy` |
| C20 Entry đồng hồ thấp | 2.100 khi xe 2.200 | Lưu, không cảnh báo; Meter History thêm dòng "100 km ago"; số hiện tại giữ 2.200 | `Chạy` |
| C21 Entry không có dòng việc | Entry 57856983 | Lưu được, vẫn giải quyết sự cố; "No line items to show." | `Chạy` |
| C22 Sự cố sau khi lưu entry | #37 | Resolved, Resolved Meter Entry 2,100 km, Timeline "Issue Resolved by service entry", Resolved By là người lưu | `Chạy` |
| C23 Mở lại sự cố giải quyết bằng entry | #37 | Nút **không** khoá; "Successfully reopened Issue."; entry còn nguyên nhưng "No issues to show"; Timeline vẫn giữ dòng cũ, không ghi mở lại | `Chạy` |
| C24 Sửa entry tạo tay | Lưu không đổi gì | Thành công | `Chạy` |
| C25 Đưa ra xưởng ngoài | Bấm Get Service at Shop | Hộp giới thiệu Shop Network; không bật. Lượt 5 đã bấm Enable, xem C268 | `Xem` · issue-shop-network.jpg |
| C26 Số lệnh dự kiến | Form hiện 101, hai lệnh khác lưu trước | Thành #103, không lỗi trùng | `Chạy` |
| C27 Phụ tùng giá lớn | 300.000 | Form 300.000,00 ₫; chi tiết 30.000.000 ₫; form sửa 300.000 | `Chạy` · wo-100x-after-save.jpg |
| C28 Phụ tùng giá nhỏ | 5 | Form 5,00 ₫; chi tiết 500 ₫; form sửa 5 | `Chạy` |
| C29 Phụ tùng số lẻ | 12,5 | Form 12,50 ₫; chi tiết 1.250 ₫; form sửa 12,5 | `Chạy` |
| C30 Tổng phụ tùng | Ba dòng trên | Form 300.017,50 ₫; chi tiết 30.001.750 ₫; ô parts_cost 30.001.750, dòng số cũ | `Chạy` |
| C31 Lặp lại lệch tiền ở lệnh khác | WO #102, PT-B | Đúng 50.000, hiện 5.000.000; tổng 2.550.000 hiện 255.000.000; entry theo số sai | `Chạy` nhóm Kho |
| C32 Lưu lại form không đổi | WO #102 | Số trên chi tiết không tăng thêm; chưa chắc lần lưu đã chạy | `Chạy` nhóm Kho |
| C33 Đơn giá kỹ thuật viên mẫu | Chọn vào dòng công | Danh sách 480.000 ₫/hr, dòng 4.800 ₫ | `Chạy` |
| C34 Đơn giá contact tự tạo | TEST-SUA-KTV 100.000 | Danh sách 10.000.000 ₫/hr; hộp Edit Labor ₫100000.00; dòng lệnh #104 100.000 ₫ | `Chạy` |
| C35 AI với giá sai | Lệnh phụ tùng 30 triệu | "Acceptable", nội dung không bàn giá | `Chạy` |
| C36 Kỹ thuật viên mẫu trên xe thường | Tạo #103 | Tạo được; mọi sửa về sau báo E-010 | `Chạy` |
| C37 Lệnh kẹt | Đổi tech, đổi trạng thái #103 | E-011; không đổi được status, không xoá được dòng công ở lần thử | `Chạy` |
| C38 Tick sự cố không vào | Tick #33, #34, #38 khi tạo #103 | Chỉ #38, #33 vào; #34 không vào, không báo | `Chạy` một phần |
| C39 Trừ kho khi lưu | #103 rồi #104, trạng thái Open | 4 thành 3, 3 thành 2, nguồn số lệnh | `Chạy` |
| C40 Không trừ kho | Chọn "None (No Inventory Adjustment)" | Không điều chỉnh | `Chạy`, K13 |
| C41 Sửa số lượng dòng | 5 thành 3 | Sổ +2, loại Work Order #102 | `Chạy` K11 |
| C42 Xuất quá tồn | PT-A 20, kho 9,5; dòng cũ #100 | Tồn -10,5; 4 thành -2; không cảnh báo | `Chạy` K12 |
| C43 Hoàn thành lệnh và kho | WO #102 | Sổ không có dòng mới | `Chạy` K14 |
| C44 Mở lại lệnh và kho | #104, WO #102 | Không có dòng nào, tồn giữ | `Chạy` K15 |
| C45 Xoá dòng phụ tùng | Trong form sửa | Hộp "Confirm Line Item Deletion", toast "Removed Part"; tồn cộng lại, có vết nguồn lệnh | `Chạy` K16 |
| C46 Xoá cả lệnh | Hộp "All data will be lost forever." | Không chạy: đã huỷ. Có hoàn kho không vẫn chưa biết | Không chạy, K21 |
| C47 Thay thế phụ tùng | Form phụ tùng | Không thấy trường; chỉ có Replaced Parts trong bảo hành ở lệnh | `Xem` K23 |
| C48 Open sang Pending | #104 | Không hỏi, toast "Work Order was successfully updated" | `Chạy` |
| C49 Pending sang Completed thẳng, thiếu ngày | #104 | E-006; trạng thái giữ | `Chạy` · wo-complete-errors.jpg |
| C50 Có ngày, thiếu đồng hồ | #104 | E-007; trạng thái giữ | `Chạy` |
| C51 Có số cuối, thiếu ngày xong | Form sửa #104 | E-008 | `Chạy` |
| C52 Số cuối nhỏ hơn đầu | 2.250 trên 2.300 | E-009 chặn; 2.350 mới lưu | `Chạy` |
| C53 Không so với số hiện tại | Số cuối 2.350 khi xe 2.200 | Không yêu cầu lớn hơn số hiện tại. Số đầu nhỏ hơn hiện tại chưa thử ở nhóm này | `Chạy` |
| C54 Số đầu chặn do thời điểm | WO #101, 3.100 khi đồng hồ 2.999 | "must be less than 2,499 or marked as void" | `Chạy` nhóm Nhắc |
| C55 Dùng số đầu làm số cuối | Giữ tick mặc định | Ẩn ô số cuối | `Chạy` |
| C56 Lần đầu hoàn thành | #104 | Status Completed, thêm Service Entry, Duration 2 minutes, Odometer, Completion Odometer; Edit khoá | `Chạy` · wo-completed.jpg |
| C57 Entry sinh từ lệnh | Entry 57857945 | Edit khoá; Odometer lấy số cuối; Run Assessment không tự chạy; tiền gấp 100 như lệnh; Resolved Issues #35, #37 | `Chạy` · se-from-wo.jpg |
| C58 Sự cố sau hoàn thành | #35 | Resolved Meter Entry 2,350 km; Time to Resolve 23 mins; Kilometers to Resolve 150 km; Timeline "Issue Resolved by work order" | `Chạy` |
| C59 Reopen khi giải quyết bằng lệnh | #35 | Khoá, tooltip "Reopen work order #104 to reopen this issue." | `Chạy` · issue-reopen-locked.jpg |
| C60 Nhiều sự cố một lệnh | #35, #37 | Cùng Resolved | `Chạy` |
| C61 Đồng hồ hai mốc | #104 | Hai dòng Meter History nguồn "Work Order #104": 2.300, 2.350 | `Chạy` |
| C62 Đồng hồ ba dòng lượt trước | WO #99 | 3 dòng, 2 dòng 1.010 km từ lệnh và entry. Khác #104; điều kiện chưa rõ | `Chạy` |
| C63 Nhắc khi hoàn thành | WO #101 | Nhắc tính lại Next Due, Last Completed | `Chạy` nhóm Nhắc |
| C64 Nhắc trên xe nhóm này | TEST-SUA không gắn nhắc | Không kiểm được "nhắc đã reset" khi hoàn thành lại, khi mở lại | Không chạy |
| C65 Hộp mở lại lệnh | Status › Open trên #104 | Chỉ nêu khôi phục archive; **không** báo entry bị xoá, sự cố mở lại | `Chạy` · wo-reopen-confirm.jpg |
| C66 Trễ sau mở lại | Confirm | Toast cập nhật, toast "Restoring Work Order #104 data"; vài giây trang vẫn Completed | `Chạy` |
| C67 Entry khi mở lại | URL 57857945 | Not Found, "the record may have been deleted" | `Chạy` · se-deleted-not-found.jpg |
| C68 Sự cố khi mở lại lệnh | #35 | Về Open, Edit và Resolve hiện lại, mất Resolution Details, xoá dòng "Issue Resolved by work order", còn "added this issue to a work order" | `Chạy` |
| C69 Đồng hồ khi mở lại lệnh | #104 | Hai dòng còn, số hiện tại vẫn 2.350 | `Chạy` |
| C70 Hoàn thành lần 2 | #104 sau khi mở lại | Entry mới 57858956; không hỏi lại ngày, đồng hồ; Resolved Date, Time to Resolve như lần đầu dù sau 41 phút | `Chạy` |
| C71 Dòng đồng hồ trùng | Hoàn thành lần 2 | Thêm "2,350 km · Service Entry" cạnh "2,350 km · Work Order #104" | `Chạy` |
| C72 Assessment lần 2 | #104 | Đổi "Needs Review": lệnh khác đang có Brake Pads Replacement | `Chạy` |
| C73 Giới hạn số lần mở lại | Hai lượt | Không thấy giới hạn | `Chạy`, hai lượt |
| C74 Một sự cố hai lệnh | Form lệnh mới, sự cố ở #103, #104 | Không có ô tick, có ổ khoá | `Chạy` |
| C75 Menu khi đã ở lệnh | Sự cố đã gắn | Draft Work Order, Get Service at Shop dùng được; ba mục còn lại xám có khoá, tooltip. Lượt 3 khác ở Draft Work Order và đã thử Close, xem C139 đến C143 | `Chạy` · issue-menu-locked-tooltip.jpg |
| C76 Add to Work Order | #45 chưa ở lệnh | Mở tab mới, xe và sự cố điền sẵn, lưu #107 | `Chạy` |
| C77 Gỡ sự cố | Bỏ tick #45 ở #107 | "No issues to show"; Timeline #45 xoá dòng, không vết; thao tác lại được | `Chạy` |
| C78 Sao chép lệnh | Make a Copy | Xe trống; Status Open; chép dòng việc, dòng công sau khi chọn xe; không chép sự cố, ngày, đồng hồ; chưa có số | `Chạy` · wo-make-copy.jpg |
| C79 AI ưu tiên, tiếng Anh | #45, #46 | High "Major functionality impaired"; Low "Minor Impact" | `Chạy` |
| C80 AI ưu tiên, tiếng Việt và trống | #34; #33, #35 | Medium "Does not impair function"; "No Priority" | `Chạy` |
| C81 Nháp chạy nền | #46 | Banner đổi chữ khoảng 40 giây, rời trang vẫn chạy | `Chạy` · issue-draft-running.jpg |
| C82 Nháp xong | #46 | "Work Order drafted", "Ready for your review.", Discard, Review draft | `Chạy` · issue-draft-ready.jpg |
| C83 Hộp review | Xe đang có #104 | Cảnh báo lệnh mở; gom Engine Leak Inspection từ #45 vào "Also recommended"; "No estimate available" | `Chạy` · wo-draft-review.jpg |
| C84 Bỏ tick trong nháp | "1/2 Service Tasks" | Việc và sự cố #45 không vào lệnh | `Chạy` |
| C85 Tạo từ nháp | Create new Work Order | #106; "Created from an AI draft from Issue #46"; đầu việc có mô tả và mã do AI | `Chạy` · wo-from-draft.jpg |
| C86 Hứa tự điền | "Repair Priority Class Non-Scheduled" | Lệnh trống "—" | `Chạy` |
| C87 Thêm nháp vào lệnh đang có | Menu "Add to Work Order #104" | Lượt 2 thấy, không bấm; lượt 3 đã chạy, xem C191 đến C193 | `Xem` · wo-draft-add-menu.jpg |
| C88 Bỏ nháp | Discard trên #45 | Mất ngay, không hỏi, không vết | `Chạy` |
| C89 Nháp từ nhắc | Nhắc D Upcoming | Mục xám có khoá, bấm không có gì | `Chạy` nhóm Nhắc |
| C90 Assessment chưa đủ | Chưa việc; việc không tiền; entry trống | Ba câu ở E-004 | `Chạy` |
| C91 Assessment tự chạy | Có tiền | Chữ tiến độ, "Acceptable", "Auto-assessed", số nguồn | `Chạy` |
| C92 Chạy lại đánh giá | #103 | Menu đổi Rerun; vẫn "Acceptable"; nêu "the open overdue-by-date issue" dù #33 đã hết quá hạn | `Chạy` |
| C93 In | #103 | PDF hai trang, tab mới; khung xem không hiện trong tab tự động | `Chạy` |
| C94 Gửi PDF | Menu | Không bấm | `Xem` |
| C95 Giao việc | #106, Emergency, TEST-SUA-KTV | Lưu, không hỏi; người nhận không email nên không ai bị báo | `Chạy` |
| C96 Theo dõi | Tạo lệnh, sự cố | Người tạo tự theo dõi. Người được giao là liên hệ: xem C199; là user: C200 | `Chạy` một phần |
| C97 Form đầu việc | New Custom Service Task | Save khoá tới khi Continue hết 6 bước | `Chạy` |
| C98 Gợi ý đầu việc | Tên tự đặt | "No Service Task Recommendation for ..." | `Chạy` |
| C99 Trùng tên đầu việc | Tên đã có | E-013 | `Chạy` |
| C100 Gộp đầu việc | Actions, More Actions | Không thấy Merge | `Xem` |
| C101 Lưu trữ đầu việc | TEST-SUA-DV-B | Hộp xác nhận; bản ghi liên quan cập nhật nền | `Chạy` |
| C102 Mã lỗi | 16 dòng Sample | Cột, tab, menu; xe TEST không có thiết bị; không thao tác | `Xem` |
| C103 Danh mục trạng thái | `work_order_statuses` | 3 mặc định; lượt 2 không thêm; lượt 5 đã thêm, xem C239 đến C253 | `Xem` |
| C104 Cài đặt bảo dưỡng | `account/maintenance_settings/edit` | Require a Meter Reading bật; các mục khác tắt; không đổi | `Xem` · maintenance-settings.jpg |
| C105 Xong hết dòng mới hoàn thành | Luật theo `Docs` | Không kiểm vì không đổi Settings | Không chạy |
| C106 Khối bảo hành khi xe không có | #103, #104, #106 | "No vehicle warranty opportunities to show.", 0 active | `Chạy` |
| C107 Có bảo hành, chưa khớp | WO #100, chỉ có phụ tùng má phanh | Phụ tùng đứng riêng không gợi ý | `Chạy` nhóm Phương tiện · wo-warranty-before.jpg |
| C108 Có bảo hành, khớp mã | Thêm đầu việc Brake Inspection | "Warranty Opportunities (1)"; View Active Coverage; Complaint, Cause, Correction trống | `Chạy` nhóm Phương tiện · wo-warranty-opportunity.jpg |
| C109 Tự tính hết hạn | 01/10/2026 + 1 Years | End Date 10/01/2027, Active | `Chạy` nhóm Phương tiện |
| C110 Số đồng hồ bảo hành | Nhập 1000, Coverage 50.000 | Danh sách ghi Start Meter 1 km, End Meter 50,001 km; chưa rõ do ô nhập hay định dạng. Lượt 3 không lặp lại, xem C152 | `Chạy` nhóm Phương tiện |
| C111 Mẫu bảo hành | Xe không có Make, Model | "No options"; lượt 5 trả lời: do chưa có mẫu đúng điều kiện, không phải do thiếu Make, xem C255 | `Xem` |
| C112 Nút claim | Trên cơ hội bảo hành | Lượt 2 chưa thử; lượt 3 xác nhận không có nút, xem C174 | Không chạy |
| C113 Đồng hồ xe khi tạo | Ô Current Reading gõ 10.000 | Không vào bản lưu; xe hiện 0 km | `Chạy` |
| C114 Xe thứ hai | TEST-SUA-02 | Save Vehicle khoá mãi, không báo lỗi. Nhóm Lốp thấy câu "maximum number of records" | `Chạy` |
| C115 Nhận hàng vào lệnh có sẵn | D14 | Sổ +5 trước, -5 khi lưu lệnh; dòng ghi chú "From PO #2" | `Chạy` nhóm Kho |
| C116 Nhận hàng vào lệnh mới, huỷ | D15 | Hàng ở kho, đơn Full, không có lệnh | `Chạy` nhóm Kho |
| C117 Lưu form sự cố trống | Lượt trước | E-003 | `Chạy` một lần |
| C118 Bỏ dở form | Lượt trước | Trình duyệt "Leave site?" | `Chạy` |
| C119 Đầu kéo, mooc | Sự cố, lệnh theo một Vehicle | Chỉ chạy Car; không có cách gom | `Suy` |
| C120 Hộp Add Labor | #107, dòng TEST-SUA-DV-A | Technician bắt buộc, Labor Hours mặc định 1, preset 15m đến 4h, Hourly Rate, "Set Labor Time Entry", Service Task, Note, Subtotal, "Save and Add Another", "Save" | `Chạy` |
| C121 Chọn kỹ thuật viên | TEST-SUA-KTV | Hourly Rate tự điền 100000.00 theo contact | `Chạy` |
| C122 Time Entry | Tick, bấm preset 2h | Hiện Start Date, End Date; End nhảy từ 5:17pm sang 6:17pm | `Chạy` |
| C123 Lưu dòng công | 2h, 100.000 | Dòng 200.000 ₫; chi tiết "( 2 hr ) x 100.000 ₫" | `Chạy` |
| C124 Bấm giờ Start, Stop | Form và chi tiết lệnh | **Không có** nút; chỉ giờ tay và mốc thời gian | `Chạy` |
| C125 Tổng, credit 30.000 | Công 200.000, markup 10%, giảm 5%, thuế 10% | Markup + 20.000; credit - 30.000; giảm - 10.000; thuế + 18.000; Total 198.000 | `Chạy` |
| C126 Tổng, credit 20.000 | Cùng số khác | Thuế 19.000; Total 209.000 | `Chạy` |
| C127 Thứ tự tính | So hai bộ số | Giảm giá trên Subtotal; thuế sau markup, credit, giảm giá | `Suy` |
| C128 Hiển thị markup | Form sửa #107 | Form 2.000.000 ₫, chi tiết 20.000 ₫, Total đúng; E-019 | `Chạy` |
| C129 Link Issues, sự cố tự do | Tick #45, Save | #45 tự được tick ở khối Issues; Linked Line Items hiện TEST-SUA-DV-A; dòng đếm 1 sự cố | `Chạy` |
| C130 Link Issues, sự cố ở lệnh khác | #33, #34, #38, #46 | Ổ khoá; tooltip "...to a Work Order. Remove it from ...orders to add it to another.", câu bị che một phần | `Chạy` |
| C131 Chi tiết lệnh sau Link | #107 | #45 hiện ở cả "Resolved Issues" và dưới dòng DV-A | `Chạy` |
| C132 Tên khối khi lệnh Open | #107 còn Open | Khối đã tên "Resolved Issues" dù chưa giải quyết | `Chạy` |
| C133 Tick rồi Save quá nhanh | Lần bấm đầu | Hộp đóng mà không tick, không báo; làm lại được; E-025 | `Chạy` một lần |
| C134 Menu dòng trên form | #107 | Change Service Task, Add Service Reminder, View Change Log, View Service Task History, Delete; **không** có đánh dấu xong. Customize chỉ có Line Item Appearance, New Line Item Method, New Line Item Position | `Chạy` |
| C135 Dòng ở chi tiết lệnh | #107 | Reason for Repair, Category / System / Assembly, kỹ thuật viên, giờ, tiền; **không** có ô, nút đánh dấu xong | `Chạy` |
| C136 Record History | #107 | Lọc ngày; cột Date, Changes By, Changes Made; ghi "Tax 1 changed from ₫0 to ₫18,000", "Labor Markup Percentage changed from 0.0 to 10.0", "Total Amount changed from ₫0 to ₫198,000", dòng việc, dòng công, tạo lệnh | `Chạy` |
| C137 So với Timeline sự cố | Lệnh và sự cố | Sổ theo trường; Timeline sự cố không ghi đóng, mở lại | `Chạy` |
| C138 Email PDF, Delete lệnh | Menu #107 | Không bấm: gửi email, xoá vĩnh viễn | Không chạy |
| C139 Close khi gắn lệnh | #45 gắn #107 | Xám, tooltip "...already added to a Work Order. Remove it from all Work Orders to close"; trả lời OQ-15 | `Chạy` |
| C140 Resolve khi gắn lệnh | #45 | Add to Service Entry, Draft Work Order, Add to Work Order, Resolve with Note xám có khoá, tooltip "Issue already added to a Work Order. Remove it from all Work Orders to add it to another." | `Chạy` |
| C141 Get Service at Shop khi gắn lệnh | #45 | Vẫn mở; bấm tiếp không chạy | `Chạy` một phần |
| C142 Delete sự cố khi gắn lệnh | #45 | Vẫn sáng, không bấm | `Xem` |
| C143 Draft khác lượt trước | #45 xám; lượt trước mở | Chưa rõ do lệnh, do #45 từng Discard, hay hãng đổi; OQ-19 | `Chạy`, một sự cố |
| C144 Chọn Add to Existing | #52 | Hiện ô chọn; Continue khoá tới khi chọn | `Chạy` |
| C145 Danh sách entry | TEST-SUA-01 | Chỉ entry của đúng xe, một dòng | `Chạy` |
| C146 Lưu entry có sẵn | Chọn 57856983, Continue, Save | Toast "1 Issue(s) were added to the form"; #52 Resolved; Timeline "Issue Resolved by service entry Service Entry #57856983" | `Chạy` · issue-resolved-negative-ttr.jpg |
| C147 Ngày giải quyết | Entry cũ | Resolved Date theo entry 11/03/2026 1:04am; Resolved Meter Entry 2,100 km | `Chạy` |
| C148 Sự cố báo sau entry | #52 báo sau lúc entry làm | Time to Resolve "-15 hrs 16 mins"; **không** cảnh báo, **không** chặn; E-020 | `Chạy` · issue-resolved-negative-ttr.jpg |
| C149 Sự cố đã gắn lệnh trong hộp | Hộp Add to Service Entry | Ổ khoá, không tick được | `Chạy` |
| C150 Hai form bảo hành | `warranties/new`, `multiple/warranties/new` | Khác nhau; form đơn có End Date, End Meter ô xám tự tính khi gõ | `Chạy` |
| C151 Tự tính End Meter | Start 1000, Coverage 50000 | 51000 | `Chạy` |
| C152 Start Meter | Nhập 1000 | Lưu đúng "1,000 km"; lỗi 1 km ở C110 **không** lặp lại | `Chạy` · vehicle-warranties-tab.jpg |
| C153 End Date | Ba bảo hành TEST-SUA | Trang hiện 01/14/2027, 12/31/2024, 11/04/2026, sớm hơn form 1 ngày; TEST-XE-01 ghi đủ năm; E-023, OQ-20 | `Chạy` · vehicle-warranties-tab.jpg |
| C154 Đơn vị dòng xe | Trang bảo hành | "2,350 undefined"; E-024 | `Chạy` |
| C155 Hộp mã bảo hành | Add Maintenance Categorization | Bulk Mode, Column Mode; "Enter either a System code (000) or a System–Assembly code (000-001)"; toast "VMRS codes have been updated" | `Chạy` |
| C156 Mã ba phần | Nhập đủ ba phần | Phần Component bị bỏ | `Chạy` |
| C157 Mã 999 | Nhập "999" | **Không** báo sai; ra "9 - Bulk Product Transfer, Handling & Storage Systems › 999 - Total Vehicle Assembly" | `Chạy` |
| C158 Menu mã | "…" | Edit, Clear Codes | `Xem` |
| C159 Add Component | Mở rồi huỷ | Component Name bắt buộc, Description, câu "Use a component to itemize coverage within the Warranty. Ex. Powertrain, Axles, etc." | `Xem` |
| C160 Khớp, bảo hành hết hạn | Expired; Engine Leak 4/045/020 trùng mã | **Không** gợi ý | `Chạy` |
| C161 Khớp, sắp hết hạn | Expiring Soon, còn 1 ngày; dòng 2/027 trùng mã | **Không** gợi ý dù còn hiệu lực; một lần đo, OQ-21 | `Chạy` |
| C162 Khớp, mã hệ thống, dòng cùng mức | Active, mã 027; Transmission Leak 2/027 | Gợi ý | `Chạy` |
| C163 Khớp, mã hệ thống, dòng sâu hơn | Active, mã 027; Filter 2/027/036 | **Không** gợi ý | `Chạy` |
| C164 Khớp, mã hệ thống, dòng sâu hơn | Active, mã 034; Headlamp 3/034/004 | **Không** gợi ý | `Chạy` |
| C165 Khớp, mã đủ hai mức | Active, mã 034-004; Headlamp 3/034/004 | Gợi ý, "Warranty Opportunities (2)" cùng Brake Inspection 1/013 | `Chạy` · wo-warranty-claim-fields.jpg |
| C166 Thời điểm tính | #110 sau khi thêm mã 027 | Chi tiết vẫn "No vehicle warranty opportunities to show."; mở form hiện "(1)"; lưu thì chi tiết cập nhật | `Chạy` |
| C167 Không lan sang lệnh khác | #106 có Headlamp, không sửa lệnh | Vẫn trống, đếm "1 active ... 1 total" | `Chạy` |
| C168 Đếm khối | Ba bảo hành | "1 active 1 expiring soon 3 total": Expired vẫn tính vào total | `Chạy` |
| C169 Save & Add Another | Bảo hành | Giữ xe, loại, Start Date, Unlimited, mã Maintenance; chỉ xoá tên, thời hạn; danh sách "Added Warranties" bên phải; suýt lưu nhầm mã | `Chạy` |
| C170 Coverage Template | TEST-SUA-01 | Ô bật khi đã chọn xe, "No options" | `Xem` |
| C171 Warranty Templates | Settings | Lượt 3 bảng rỗng, không tạo; lượt 5 đã tạo, xem C255 | Không chạy |
| C172 Điền hồ sơ bảo hành | #107, Brake Inspection | Lưu xong chi tiết hiện đúng ba nội dung; câu "Add complaint, cause, and correction details for claim processing." | `Chạy` · wo-warranty-claim-fields.jpg |
| C173 View Active Coverage | Khối bảo hành | Chỉ là liên kết sang `vehicles/5891232/warranties`, cùng "Total vehicle coverage breakdown" | `Chạy` |
| C174 Quy trình claim | #107 | **Không** có nút claim, trạng thái claim, gửi hãng | `Chạy` |
| C175 Warranty Credits | Sau khi điền hồ sơ | **Không** tự nối; vẫn nhập tay | `Chạy` |
| C176 Bỏ tick sự cố trong entry | #52, entry 57856983 | #52 về Open, mất Resolution Details; Timeline chỉ còn "opened this issue" | `Chạy` |
| C177 Xác nhận khi bỏ tick | Như trên | **Không** hỏi, **không** để vết đã từng Resolved | `Chạy` |
| C178 Sự cố ở lệnh khác trong entry | #37, #35 | Ổ khoá, không bỏ tick được từ entry | `Chạy` |
| C179 AI đóng sự cố | Entry 57902070 cùng đầu việc, ghi chú khớp #52, không tick | Entry "No issues to show."; #52 vẫn Open | `Chạy` |
| C180 AI gợi ý đóng | Form, trang chi tiết | **Không** gợi ý khi xem ngay sau lưu; đợi lâu hơn xem C234, C235 | `Chạy` |
| C181 Issue Resolution | Settings | Không bấm Manage vì có câu điều khoản; OQ-22 | Không chạy |
| C182 Entry mới không gõ ngày | Ô mờ hiện ngày hôm nay | "can't be blank", "Service Entry could not be created"; E-012 lặp lại. Có khối "Smart Upload" Beta | `Chạy` |
| C183 Menu "Add to" | #52, #107 đang mở | "Add to Work Order #107" kèm "Open · Updated 5 minutes ago", "Create new Work Order" | `Chạy` |
| C184 Hai nhóm việc | #52 | "Resolves this issue": Automatic Transmission Leak Inspection; "Also recommended": Engine Leak Inspection từ #45 đang gắn #107 | `Chạy` |
| C185 Tạo lệnh từ nháp | Create new Work Order | #110, toast "Created from an AI draft from Issue #52"; "Resolved Issues" CHỈ có #52 | `Chạy` |
| C186 Sự cố đang ở lệnh khác | #45 | **Không** vào #110; vẫn ở #107, Timeline không đổi; #110 vẫn có dòng Engine Leak Inspection; trả lời OQ-14 | `Chạy` |
| C187 Câu AI | Hộp review | Viết "no existing open work orders" khi #107 đang mở; E-021 | `Chạy` |
| C188 AI và entry vừa làm | Entry 57902070 cùng việc, vài phút trước | **Không** tính đến | `Chạy` |
| C189 Hứa tự điền, lần 2 | #110 | "Repair Priority Class Non-Scheduled" nhưng trường "—"; E-017 | `Chạy` |
| C190 Dòng trùng | #110 | **Không** hỏi xác nhận; E-022 | `Chạy` |
| C191 Thêm vào lệnh, chọn lệnh | #53, xe có 4 lệnh mở #103, #106, #107, #110 | Chỉ nêu "#110", không cho chọn lệnh khác | `Chạy` |
| C192 Thêm nháp vào #110 | "Add to Work Order #110" | Toast "Work Order successfully updated", "Updated from an AI draft from Issue #53"; thêm dòng Windshield Wiper Blade Replacement; "Resolved Issues" có #52, #53 | `Chạy` |
| C193 AI phân loại | #53 | Ưu tiên Low; mã 0 / 002 / 035 | `Chạy` |
| C194 Khung Watching | #110 | "You're watching this record, so you will receive all Watched Notifications."; "WATCHERS · 1"; "ADD WATCHER", ô "Search users" | `Chạy` |
| C195 Thêm người theo dõi | Danh sách | Chỉ "Fleetio Automation", "Service Advisor", xám có khoá; không chọn | `Xem` |
| C196 Unwatch, Watch | #110 | Avatar mất, nút đổi "Watch", không hỏi lại; bấm lại về "Unwatch" | `Chạy` |
| C197 Lệnh từ nháp AI | #110 | Người bấm thành người theo dõi | `Chạy` |
| C198 Xe | TEST-SUA-01 | **Không** tự theo dõi; hiện "Watch" | `Chạy` · vehicle-warranties-tab.jpg |
| C199 Giao cho liên hệ | #106, TEST-SUA-KTV | "1 watcher": liên hệ **không** thành người theo dõi | `Chạy` |
| C200 Giao cho user thứ hai | Không mời người ngoài | Không chạy được; giao cho chính tài khoản đăng nhập xem C227 | Không chạy |
| C201 Menu dòng mã lỗi | Dữ liệu Sample | Không chọn "Create Issue", "Ignore"; xe TEST không có thiết bị | `Xem` |
| C202 Fault Rules | "View Fault Rule" sang Settings | 11 dòng, cột Code, Description | `Xem` · fault-rules.jpg |
| C203 Add Fault Rule | Mở đọc rồi Cancel | Code, Name, Description, Priority Handling; "Off", "Ignore Code", "Flag as Critical"; không lưu vì là danh mục dùng chung | `Xem` |
| C204 Hai hệ mã | Fault Rules | OBD "P0401"; SPN/FMI "SPN 520672 FMI 1" có nhãn Critical | `Xem` · fault-rules.jpg |
| C205 Gom mã | Sự cố Sample #13 | "[Fault] Diesel Aftertreatment Restriction - DPF and EGR (P0401, P2002, P2459)"; Reported By "AI Service Advisor"; "Auto-assigned priority: High"; Source 3 dòng | `Xem` |
| C206 Nguồn mã lỗi | Đầu trang | "Integrate your telematics provider to automatically import Faults" | `Xem` |
| C207 Source sự cố nhập tay | #52 | "—" | `Chạy` · issue-resolved-negative-ttr.jpg |
| C208 Menu Recall | Dòng Sample | "Acknowledge", "Create Issue", "Check VIN"; không chọn | `Xem` |
| C209 Tab Recall | Cùng tab Needs Action, dữ liệu Sample | Hai số đều đúng ở thời điểm đo: 261 ở lượt đầu ("1 - 50 of 261" trong `recalls-list.jpg`, ảnh lưu 03/11 lúc 01:37, nhóm Nền tảng); 285 ở lượt 3 chiều 03/11, là số mới nhất. Tăng 24 dòng dù không ai đổi trạng thái; lý do chưa kiểm, nhập tự động từ NHTSA là `Suy`. Lượt 4 không đếm lại. Tab All, Needs Action, Open, Resolved, Acknowledged | `Xem` |
| C210 Recall trên xe TEST | Xe không có Make | **Không** phát sinh recall để thử | Không chạy |
| C211 Print lệnh, lượt 3 | `work_orders/107/pdf` | Tệp PDF 2 trang; khung xem trong tab tự động trắng, chưa đọc nội dung; không tải. Lượt 4 đã đọc, xem C230 | `Chạy` một phần |
| C212 Đổi Cài đặt | Enable Shop Network, trạng thái tuỳ biến, xong hết dòng, Warranty Templates | Lượt 3 không làm vì đổi Settings dùng chung. Lượt 5 đã chạy FR-036, mẫu bảo hành, bấm Enable Shop Network; phần cấu hình của FR-017 vẫn chưa kiểm | Không chạy |
| C213 Markup phụ tùng, lượt 3 | Hộp Add Part mở rồi huỷ | Không thêm vì kho TEST đang do nhóm khác đo tồn; lượt 4 đã chạy, xem C217 | Không chạy |
| C214 Dữ liệu không đụng | #103 kẹt, biểu mẫu #680174, TEST-XE-LOP, TEST-MOOC-LOP | Không thao tác; không tạo xe | Không chạy |
| C215 Tab đóng từ ngoài | Một lần đầu lượt 3 | Cả nhóm tab mất, form chưa lưu mất; làm lại trên tab mới. Do môi trường chạy thử, không phải hành vi Fleetio | `Chạy` |
| C216 Hộp Add Part, lượt 4 | Chọn TEST-KHO-PT-A | Hiện Part Location: "None (No Inventory Adjustment)" hoặc nhóm "PULL FROM INVENTORY" kèm tồn từng kho; chọn kho hiện "This will make an inventory adjustment"; Unit Cost tự điền từ danh mục | `Chạy` |
| C217 Parts Markup 20%, đơn giá tự điền | 2 x 100000.00 | Đơn giá lưu ra 10.000.000 ₫/cái; Parts 20.000.000 ₫, sai 100 lần; markup + 4.000.000; giảm - 1.010.000; thuế + 2.318.000; Total 25.498.000 ₫ | `Chạy` #107 |
| C218 Parts Markup 20%, gõ đơn giá 1000 | 2 x 1000 | Parts 200.000 ₫, đơn giá chi tiết 100.000 ₫; markup + 40.000; giảm - 20.000; thuế + 41.000; Total 451.000 ₫ | `Chạy` #107 |
| C219 Parts Markup Fixed | 15.000 | Parts 200.000 ₫; + 15.000; giảm - 20.000; thuế + 37.000; Total 422.000 ₫ | `Chạy` #107 |
| C220 Xoá dòng phụ tùng, Fixed còn | Parts 0 ₫ | + 15.000; giảm - 10.000; thuế + 18.000; Total 213.000 ₫; **không** cảnh báo | `Chạy` #107 |
| C221 Công thức thuế, markup phần trăm | C218 | Cơ số 410.000 gồm cả hai markup, trừ credit, giảm giá | `Suy` từ số thật |
| C222 Form sửa, Parts Markup | C218 | Form 4.000.000 ₫, chi tiết 40.000 ₫; dòng công không lệch | `Chạy` |
| C223 Thuế với Fixed | C219, C220 | Chi tiết 37.000, 18.000, cơ số **không** gồm 15.000; xem trước trên form 38.500 | `Chạy`, 2 lần đo |
| C224 Tồn theo lệnh Open | TEST-KHO-01 | Current Qty 121 trước; 119 và WO Current Qty 2 khi lưu lệnh Open; **không** đợi Completed | `Chạy` #107 |
| C225 Xoá dòng phụ tùng, tồn | Lưu lệnh | Current Qty về 121, WO Current Qty 0; hộp "Confirm Line Item Deletion" "Are you sure you want to permanently delete this line item?"; form **không** có dấu vết số đã trả | `Chạy` #107 |
| C226 Trả markup về 0 | Parts Markup #107 | Total về 198.000 ₫ như trước khi thử; loại markup vẫn Fixed | `Chạy` |
| C227 Giao cho user | #107 đã Unwatch, WATCHERS 0; giao chính tài khoản Account Owner | Lưu không hỏi; nút đổi từ "Watch" thành "Unwatch"; "WATCHERS · 1": user được giao tự thành người theo dõi | `Chạy` |
| C228 Danh sách Assigned To | Form lệnh | **Không** chỉ Technician: có Employee, Operator, Account Owner, "Fleetio Automation" | `Chạy` |
| C229 Email khi giao | Giao cho chính mình | Không kiểm được hộp thư, không biết có gửi | Không chạy |
| C230 Đọc PDF | `work_order_107.pdf`, 2 trang | Đầu trang tên, địa chỉ tài khoản; Work Order Number, Invoice Number, PO Number; "WORK ORDER DETAILS"; "LINE ITEMS"; trang 2 "DESCRIPTION", "SUMMARY"; chân trang "Powered by Fleetio", "Page 1 of 2" | `Chạy` · wo-print-pdf.jpg |
| C231 Ngày trên PDF | Issue Date | PDF "Mon, Nov 2, 2026 12:32 PM", web 11/03/2026 1:32am; lệch sang ngày khác; E-028 | `Chạy` · wo-print-pdf.jpg |
| C232 Tiền trên PDF | Summary | Dạng US ₫198,000, web 198.000 ₫; số khớp: Labor Markup + ₫20,000, Parts Markup + ₫0 (Fixed), Warranty Credits - ₫30,000, Discount - ₫10,000, Tax +₫18,000, Total ₫198,000 | `Chạy` |
| C233 Hồ sơ bảo hành trên PDF | Phần đọc được | **Không** in Complaint, Cause, Correction | `Chạy` |
| C234 AI đóng sự cố, đợi lâu | #52, khoảng 1 đến 2 giờ sau entry 57902070 | #52 vẫn Open | `Chạy` |
| C235 AI đóng sự cố, thử lại | #59 trên TEST-KHO-01, entry 57903452 khớp nội dung, không tick, khoảng 15 phút | #59 vẫn Open; AI xếp Priority High; entry "No issues to show.", "If this service entry resolves any issues, you can add them by editing the service entry."; **không** gợi ý | `Chạy` |
| C236 Form entry, sự cố mở | #59 | Liệt kê ở tab Open, "Select any issues that were resolved as part of this service", **không** tự tick | `Chạy` |
| C237 Báo cáo giờ công | `work_orders/labor_time_entries` | Chỉ lọc Contacts, Started at, Ended at; không phải nút bấm giờ | `Xem` |
| C238 Không chạy, lượt 4 | Recall và Fault tạo sự cố, Get Service at Shop, luật xong hết dòng, Warranty Templates, Email PDF, Delete | Đổi trạng thái Sample, cần thiết bị, đổi Settings, gửi email hoặc xoá | Không chạy |
| C239 Trạng thái, thiếu tên | Name trống | E-029 | `Chạy` |
| C240 Trạng thái, trùng tên | Name "Open" | E-030 | `Chạy` |
| C241 Tạo loại Incomplete | "TEST-SUA Cho phu tung", không màu | "Work Order Status was successfully created"; cuối bảng, ô tick thay cho khoá vì chưa dùng | `Chạy` · wo-status-custom-list.jpg |
| C242 Tạo loại Completed | "TEST-SUA Xong cho nghiem thu", tím | Cột Type "Completed" có dấu tick đen | `Chạy` · wo-status-custom-list.jpg |
| C243 Lan ra màn khác | Sau khi tạo | Có ngay ở menu trên lệnh, form lệnh, bộ lọc Status; loại Completed có huy hiệu riêng; **không** tự thêm tab trên danh sách lệnh | `Chạy` |
| C244 Sang Incomplete tuỳ biến | #106 Open | Cập nhật ngay; Status Updates ghi đổi; số lệnh Open 13 sang 12 | `Chạy` |
| C245 Sang Completed tuỳ biến, thiếu dữ liệu | #106 không Started At | Chặn như Completed gốc, E-006 | `Chạy` |
| C246 Sang Completed tuỳ biến, đủ dữ liệu | #106 đồng hồ 2.360, 2.365 | Sinh entry 57906551, Edit xám; **không** có bước riêng cho chờ nghiệm thu | `Chạy` |
| C247 Giữa hai trạng thái Completed | Tuỳ biến sang gốc | **Không** hộp thoại; vẫn entry cũ, **không** sinh thêm | `Chạy` |
| C248 Completed sang Incomplete tuỳ biến | #106 | Hộp "Update Status" cùng câu chữ; Confirm: entry mất, URL 404, toast "Complete: Restoring Work Order #106 data". Hộp **không** nói xoá entry | `Chạy` |
| C249 Đổi loại khi đang dùng | Tick Completed, trạng thái có 1 lệnh | E-031 | `Chạy` |
| C250 Đổi Default | Tick trên trạng thái tuỳ biến | Huy hiệu chuyển hẳn, Open mất Default; form lệnh mới chọn sẵn; đã trả về Open | `Chạy` |
| C251 Khoá theo số lệnh | Có lệnh dùng | Ổ khoá, tooltip "...that are being used cannot be deleted."; menu Edit, Delete xám có khoá | `Chạy` · wo-status-custom-list.jpg |
| C252 Trạng thái gốc | Open, Pending, Completed | Sửa được tên, mô tả, màu; có lệnh nên khoá Delete | `Chạy` |
| C253 Không kiểm, trạng thái | Kéo sắp xếp, nhắc khi Completed tuỳ biến, Delete | #106 không gắn nhắc; không xoá | Không chạy |
| C254 Sự cố sau mở lại | #46 | Về tab Open của Issues, trên lệnh vẫn ở khối "Resolved Issues" | `Chạy` |
| C255 Mẫu riêng trên xe km | TEST-SUA-01, mẫu Kilometers | Trước "No options", nay nhóm "CUSTOM TEMPLATES" có mẫu dù xe không có Make | `Chạy` · warranty-template-list.jpg |
| C256 Xem trước mẫu | Chọn mẫu | "Coverage preview" liệt kê coverage; từng dòng Edit, Edit Maintenance Codes, Delete, sửa riêng lần này | `Chạy` · warranty-template-preview.jpg |
| C257 Áp mẫu | Save Warranties | "Warranties have been successfully created"; sinh 2 bảo hành riêng, Standard 11/03/2026 đến 11/03/2028, Extended 11/03/2026 đến 05/03/2027 | `Chạy` |
| C258 Mã theo mẫu | Coverage có 034-004 | Form sửa #106 hiện thêm cơ hội "TEST-SUA BH mau co ban" | `Chạy` |
| C259 Xe Sample có Make | BSA100TRNS, Freightliner, đơn vị mi; không lưu | "OEM TEMPLATES" 14 mẫu xe con Ford, Chevrolet; **không** lọc theo Make; **không** có mẫu đầu kéo; không thấy mẫu km của khách | `Xem` |
| C260 Mẫu OEM | 2025 Ford F-150 | Bumper to Bumper 3 năm 36.000 mi, Powertrain 5 năm 60.000 mi, Safety Restraint System 5 năm 60.000 mi, Corrosion 5 năm Unlimited; còn dòng dưới, không đọc hết | `Xem` · warranty-oem-template-preview.jpg |
| C261 Xe km gặp OEM | TEST-SUA-01 | Không thấy nhóm OEM; lọc theo đơn vị đồng hồ là suy từ 2 lần quan sát; OQ-27 | `Suy` |
| C262 Sửa mẫu đã dùng | Coverage 2 năm thành 3 năm | Hộp "Template Change": "Apply to assets this template is added to in the future" mặc định; "Apply to all historical and future assets with this template" | `Chạy` · warranty-template-change.jpg |
| C263 Áp về quá khứ | Lựa chọn 2 | "1 asset with coverage ... applied will be updated. Please note that any coverage edits made to individual assets will be overwritten."; End Date đổi 11/03/2029: mẫu liên kết với bảo hành đã sinh | `Chạy` |
| C264 Start Meter khi gõ tự động | Form New Warranties, gõ 2365 | Ô giữ "2", lưu 2 km, End Meter 100.002 km; không cảnh báo lệch 2.365; 2/2 lần, **chưa kết luận** lỗi Fleetio hay công cụ; E-032, OQ-26 | `Chạy` |
| C265 Không chạy, mẫu | Áp tương lai, ghi đè phần sửa riêng, xoá mẫu | Ghi đè chỉ có câu cảnh báo; Delete mẫu không khoá dù đang dùng, không bấm | Không chạy |
| C266 Form mẫu | New Warranty Template | Name, Meter Unit (Miles, Kilometers, Hours); coverage đủ trường; "Create & Add Another", "Create Coverage"; Save xám tới khi có coverage; danh sách Name, Manufacturer, # Coverages; menu Edit, Duplicate, Delete | `Chạy` |
| C267 Hộp Shop Network | #46, Get Service at Shop | Ba bước, "Already included in your plan, there's no additional charge to use it."; "Learn more", "Enable Shop Network" | `Chạy` |
| C268 Bấm Enable | Một lần | Chuyển sang `fleetio_pay/account_setup/new`, E-033; **không** có hộp điều khoản, hợp đồng, phí | `Chạy` · shop-network-enable-denied.jpg |
| C269 Sau khi bị từ chối | Mở lại mục | Vẫn hộp giới thiệu, tức chưa bật | `Chạy` |
| C270 Draft trên #46 đang gắn lệnh | Menu Resolve | Draft Work Order xám; chỉ Get Service at Shop sáng; OQ-19 | `Chạy` |
| C271 Không chạy, Shop | Chọn xưởng, gửi yêu cầu, ghi tự động, duyệt báo giá, hoá đơn | Chặn tại Access Denied; dừng vì là phần thanh toán | Không chạy |

## Phát hiện lượt 3 (03/11)

Nguồn: `run-notes/repair.md`, mục Lượt 3.

- Khớp bảo hành theo đúng mức mã: mã hệ thống `027` khớp dòng 2/027, không khớp 2/027/036.
- Bảo hành Expiring Soon còn hiệu lực nhưng không gợi ý (1 lần đo); Expired cũng không. Trang chi tiết lệnh giữ kết quả cũ, chỉ cập nhật sau khi sửa và lưu chính lệnh đó.
- Không có quy trình claim: 3 ô chữ, Warranty Credits nhập tay.
- Gắn sự cố vào Service Entry cũ cho Time to Resolve âm "-15 hrs 16 mins", không cảnh báo.
- Công thức trên #107: giảm giá tính trên Subtotal, thuế tính sau markup, credit, giảm giá. Form sửa hiện Labor Markup 2.000.000 ₫, chi tiết đúng 20.000 ₫ (lệch 100 lần).
- Lượt 4: Parts Markup phần trăm tính trên Parts và vào cơ số thuế; markup cố định không vào cơ số thuế ở trang chi tiết (E-fleetio-repair-026). Đơn giá tự điền từ danh mục làm sai Total 100 lần. User được giao tự thành người theo dõi. PDF theo múi giờ tài khoản, lệch ngày với web (E-fleetio-repair-028). AI không đóng sự cố sau 1 đến 2 giờ.
- Lượt 5: trạng thái tuỳ biến chỉ hai loại, hiệu ứng như gốc; mẫu bảo hành có hộp Template Change áp tương lai hay quá khứ; Enable Shop Network sang Fleetio Pay, Access Denied; hộp mở lại không báo xoá Service Entry; Start Meter chỉ giữ ký tự đầu khi gõ tự động, chưa kết luận lỗi Fleetio hay công cụ.
- Chưa rõ nguyên nhân: Draft Work Order xám trên #45, #46 khác lượt trước; End Date trang chi tiết sớm hơn form 1 ngày.
