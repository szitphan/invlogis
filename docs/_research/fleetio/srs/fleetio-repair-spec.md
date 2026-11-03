---
type: research
feature: fleetio-repair
status: draft
updated: 2026-11-03
links:
  - docs/_research/fleetio/fleetio-repair.md
  - docs/_research/fleetio/run-notes/repair.md
  - docs/_product/saas-core-vs-tenant.md
---

# Sửa chữa: sự cố, lệnh sửa, lịch sử dịch vụ — SRS phân tích ngược từ Fleetio

> Tài liệu mô tả **Fleetio đang làm gì**, kèm đề xuất cho Invlogis. Chưa phải yêu cầu đã chốt với Delta. Không dùng làm baseline phát triển.

**Nhãn bằng chứng:** `Chạy` đã thao tác và thấy kết quả · `Xem` thấy trên giao diện · `Docs` tài liệu công khai của Fleetio · `Suy` suy ra · `GĐ` giả định của người viết.

**Dữ liệu chạy:** xe TEST-SUA-01 loại Car; Issue #33 đến #38, #45, #46; Work Order #103, #104, #106, #107; Service Entry 57856983, 57857945 (tự bị xoá khi mở lại), 57858956. Lượt trước: Issue #30, #31, Work Order #99, #100. Tài khoản một người dùng, toàn quyền: mọi kết luận về phân quyền chưa kiểm chứng.

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
| FR-fleetio-repair-002 | Nhiều nguồn sự cố | Sự cố đến từ nhập tay, phiếu kiểm tra hỏng, mã lỗi thiết bị, thu hồi; có trường Source liên kết về nguồn. | P0 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` Issue #31, `Xem` Faults | `Chạy` nhập tay, phiếu; `Xem` mã lỗi | Lấy, bỏ thu hồi NHTSA |
| FR-fleetio-repair-003 | Năm cách xử lý | Menu Resolve trên sự cố mở: Add to Service Entry, Draft Work Order, Add to Work Order, Get Service at Shop, Resolve with Note. Khi sự cố đã gắn lệnh, ba mục Add to Service Entry, Add to Work Order, Resolve with Note khoá. | P1 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` #35, #37, #45, #46; `Xem` Shop | `Chạy` bốn nhánh; `Xem` Shop | Lấy, bỏ nhánh mạng lưới xưởng |
| FR-fleetio-repair-004 | Đóng sự cố không sửa | Menu ba chấm › Close mở hộp có ô Note tuỳ chọn; đóng ghi Closed Date, Closed By, Note; ghi chú thành một Comment; mất Edit, Resolve. Không tính vào thời gian xử lý (`Docs`). | P1 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` #36, #38; `Docs` Issues Overview | `Chạy` | Lấy; nên bắt buộc lý do đóng |
| FR-fleetio-repair-005 | Sự cố quá hạn | Sự cố có hạn theo ngày và số đồng hồ. Overdue là giá trị tính, không lưu: đọc lại mỗi lần theo ngày và đồng hồ hiện tại; hiện ở Issue Status, tab Overdue, vẫn thuộc nhóm Open. Không có nút, sự kiện chuyển. | P1 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` #33 đến #38 | `Chạy` | Lấy cách tính; ghi thêm thời điểm bắt đầu quá hạn |
| FR-fleetio-repair-006 | Tạo lệnh | Lệnh có xe, trạng thái, phân loại ưu tiên, ngày lập, người lập, người nhận việc, ngày dự kiến và thực tế, xưởng ngoài, hoá đơn, số đơn mua. Số lệnh trên form chỉ là số dự kiến, lưu thì tự nhảy nếu đã có lệnh khác. | P0 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` WO #99, #100, #103, #104 | `Chạy` | Lấy cho `repair-order` |
| FR-fleetio-repair-007 | Gắn sự cố vào lệnh | Form lệnh liệt kê sự cố của xe theo tab Open, Resolved, Closed; Overdue nằm trong tab Open; tick để gắn; gắn được với từng dòng việc qua Link Issues. Dòng đã ở lệnh khác có ổ khoá. | P0 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` WO #100, #103, #104 | `Chạy`, trừ ca #34 chưa rõ | Lấy, phải báo khi tick không vào |
| FR-fleetio-repair-008 | Dòng việc | Dòng việc gồm đầu việc, công, phụ tùng, ghi chú, mã phân loại tự điền (Reason, Category, System, Assembly), Last Completed, Add Service Reminder; có tab Service Tasks, Labor, Parts. | P0 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` | `Chạy`; tiền hiển thị lệch, xem E-005 | Lấy, sửa lỗi tiền |
| FR-fleetio-repair-009 | Ghi công | Ghi giờ công trực tiếp hoặc bấm giờ bắt đầu, kết thúc theo kỹ thuật viên; chọn kỹ thuật viên lấy đơn giá mặc định của contact. | P1 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` hộp Add Labor; `Docs` bấm giờ | `Chạy` nhập công; `Docs` bấm giờ | Lấy nếu Delta tính công |
| FR-fleetio-repair-010 | Tổng hợp chi phí | Tính tổng công, phụ tùng, markup công, markup phụ tùng, tín dụng bảo hành, giảm giá, thuế. | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | test | `Chạy` phần tổng, `Xem` các ô khác | `Chạy` phần tổng; `Xem` phần còn lại | Lấy, hợp với sửa cho xe khách |
| FR-fleetio-repair-011 | Đổi trạng thái lệnh | Đổi trạng thái ngay trên đầu trang. Open và Pending đổi qua lại không hỏi; Pending sang Completed đi thẳng được; hệ thống kiểm điều kiện theo cấu hình; Completed về chưa xong có hộp xác nhận. | P0 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` #104 | `Chạy` | Lấy |
| FR-fleetio-repair-012 | Hoàn thành lệnh | Khi chuyển sang trạng thái loại Completed, hệ thống giải quyết sự cố đã chọn, ghi nhận đầu việc, tính Duration, tạo Service Entry, ghi Time to Resolve, Kilometers to Resolve, khoá Edit của lệnh, entry và Reopen của sự cố. Không ghi sổ kho. | P0 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` WO #99, #104; `Chạy` nhóm Nhắc #101 về nhắc | `Chạy` | Lấy, xem Mục 11 về ghi trùng số km |
| FR-fleetio-repair-013 | Mở lại lệnh | Đổi lệnh Completed về chưa xong qua hộp "Update Status". Service Entry bị xoá hẳn, URL ra Not Found; sự cố về Open, mất Resolution Details và dòng Timeline; đồng hồ và tồn giữ nguyên. Khôi phục dữ liệu archive chạy nền. | P0 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` #104; `Chạy` K15 ở WO #102 | `Chạy` | Lấy cơ chế khoá; giữ vết thay vì xoá hẳn |
| FR-fleetio-repair-014 | Ghi lịch sử trực tiếp | Tạo Service Entry không qua lệnh, bắt buộc Odometer và Completion Date, không cần dòng việc; lưu là giải quyết sự cố đã chọn. | P1 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` entry 57856983 từ #37; `Docs` phần tạo từ danh sách | `Chạy` | Lấy cho sửa ngoài; cảnh báo số đồng hồ thấp |
| FR-fleetio-repair-015 | Xem lệnh ba chế độ | Danh sách, lịch tháng, lịch tài nguyên theo xe hoặc kỹ thuật viên. | P1 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` chuyển chế độ | `Chạy` | Lấy lịch tài nguyên cho xưởng |
| FR-fleetio-repair-016 | Đầu việc | Danh mục đầu việc có mã phân loại mặc định, giờ công dự kiến, phụ tùng gắn kèm; 400 đầu việc có sẵn. Tab Active, Archived; Actions có Update Service Tasks, Archive; More Actions có Import, Export. | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | demo | `Chạy` | `Chạy` | Lấy cấu trúc, tự xây danh mục tiếng Việt |
| FR-fleetio-repair-017 | Tình trạng từng dòng | Đánh dấu xong từng dòng, không kích hoạt hiệu ứng hoàn thành; cấu hình bắt buộc xong hết mới hoàn thành lệnh. | P2 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | test | `Docs`; không đổi Settings nên chưa kiểm | `Docs` | Cân nhắc |
| FR-fleetio-repair-018 | Sao chép, in, gửi | More Actions: Run Assessment, Print, Make a Copy, View Record History, Email PDF, Delete. Print mở PDF tab mới. Make a Copy mở form mới: xe trống, Status Open, Issue Date hiện tại; chọn xe xong mới có dòng việc, công; không chép sự cố, ngày, đồng hồ. | P2 | [Cấu hình] | demo | `Chạy` Print, Copy; `Xem` Email PDF, Delete | `Chạy` Print, Copy; `Xem` còn lại | Lấy in và lịch sử |
| FR-fleetio-repair-019 | AI xếp ưu tiên | Với sự cố mới, AI tự gán hoặc gợi ý mức ưu tiên, hiện dấu sao và câu "Auto-assigned priority". Có sự cố vẫn để "No Priority". | P2 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` #33, #34, #35, #45, #46 | `Chạy` | Cân nhắc, cần thử nhiều hơn với tiếng Việt |
| FR-fleetio-repair-020 | AI soạn lệnh | Từ sự cố, AI soạn nháp chạy nền, đổi dòng chữ tiến độ; rời trang vẫn chạy. Hộp review: cảnh báo lệnh đang mở của xe, nhóm "Resolves this issue" và "Also recommended for this vehicle" gom sự cố khác cùng xe, đầu việc có tick, ước tính, phần tự điền; tạo lệnh mới hoặc thêm vào lệnh đang mở; hoặc Discard. | P2 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` WO #99, #106, sự cố #45, #46; `Chạy` nhóm Nhắc: mục này xám trên nhắc | `Chạy` tạo mới; `Xem` thêm vào lệnh đang có | Cân nhắc; học gom việc cùng xe |
| FR-fleetio-repair-021 | AI đánh giá lệnh | Khi có đầu việc và chi phí, AI tự chạy trên lệnh, kiểm công và giá phụ tùng, kết luận Acceptable hoặc Needs Review, ghi nguồn; cho chạy lại khi lệnh đổi; soi cả lệnh khác cùng xe trùng đầu việc. | P2 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` WO #99, #103, #104 | `Chạy` | Chờ có dữ liệu giá Việt Nam; không dùng làm điều kiện duyệt |
| FR-fleetio-repair-022 | AI đóng sự cố | Khi có Service Entry, AI đóng hoặc gợi ý đóng sự cố khớp nội dung. | P2 | [Gói: Bảo dưỡng đội xe] | demo | `Docs`, `Xem` cấu hình | `Docs` | Cân nhắc, cần người duyệt |
| FR-fleetio-repair-023 | Mã lỗi thiết bị | Nhận mã lỗi, đánh dấu nghiêm trọng, gom các mã liên quan vào một sự cố; có trạng thái Open, Pending, Resolved, Ignored; menu dòng Create Issue, Ignore, View Fault Rule. | P2 | [Gói: Bảo dưỡng đội xe] | demo | `Xem` Issue #13, #14, #15 gom nhiều mã; 16 dòng Sample | `Xem` | Phụ thuộc thiết bị |
| FR-fleetio-repair-024 | Luật mã lỗi | Khai mã, mô tả và mức nghiêm trọng theo khách; có mẫu bỏ qua mã phiền. | P2 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | demo | `Xem` Fault Rules, mẫu Automation | `Xem` | Phụ thuộc thiết bị |
| FR-fleetio-repair-025 | Bảo hành | Khai bảo hành theo ngày và số km, cho nhiều xe một lượt, mỗi xe một Start Date, Start Meter; Standard Warranty, Standard templates, Extended Warranty; tự tính End Date, End Meter; gắn mã phân loại. | P2 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` nhóm Phương tiện, TEST Bao hanh dong co | `Chạy` | Hỏi Delta |
| FR-fleetio-repair-026 | Giải quyết kèm ghi chú | Resolve with Note mở hộp có Note bắt buộc, nút khoá khi trống. Sau lưu: Status Resolved, khối Resolution Details, nút Reopen, mất Edit. | P1 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` #35 | `Chạy` | Lấy |
| FR-fleetio-repair-027 | Mở lại sự cố | Nút Reopen trên sự cố Closed hoặc Resolved bằng ghi chú, bằng entry mở hộp xác nhận; sự cố Resolved bằng lệnh thì nút khoá, tooltip nêu số lệnh. | P1 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` #35, #37, #38 | `Chạy` | Lấy; ghi vết lần mở lại |
| FR-fleetio-repair-028 | Thêm vào Service Entry | Hộp "Add to Service Entry" liệt kê sự cố mở của xe, tick sẵn sự cố đang mở trang; chọn Add to New hoặc Add to Existing Service Entry, Continue sang form. | P1 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` New; `Xem` Existing | `Chạy` New; `Xem` Existing | Lấy |
| FR-fleetio-repair-029 | Số đồng hồ trên lệnh | Start Odometer và tick "Use start odometer for completion meter" mặc định bật; bỏ tick hiện Completion Odometer. Lưu hai mốc tạo hai dòng Meter History nguồn lệnh. | P0 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` #104 | `Chạy` | Lấy |
| FR-fleetio-repair-030 | Phân loại ưu tiên lệnh | Repair Priority Class gồm Scheduled, Non-Scheduled, Emergency, ghi rõ VMRS Code Key 16; bật được bắt buộc. | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | demo | `Chạy` #106 chọn Emergency | `Chạy` | Lấy ba mức, bỏ mã VMRS |
| FR-fleetio-repair-031 | Khoá và gỡ sự cố khỏi lệnh | Sự cố đã gắn lệnh thì khoá lối khác kèm tooltip. Sửa lệnh, bỏ tick rồi lưu là gỡ; sự cố tự do trở lại, Timeline xoá dòng "added this issue". | P0 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` #45, #107 | `Chạy` | Lấy khoá; ghi vết lần gỡ |
| FR-fleetio-repair-032 | Tồn kho theo dòng phụ tùng | Hộp Add Part chọn kho, ghi "This will make an inventory adjustment" hoặc "None (No Inventory Adjustment)". Lưu lệnh trừ tồn; sửa số lượng, xoá dòng ghi bù vào Inventory Activity nguồn số lệnh. | P0 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` #103, #104, K10 đến K16 | `Chạy` | Lấy; cảnh báo khi vượt tồn |
| FR-fleetio-repair-033 | Giao việc, theo dõi | Assigned To chọn người có nhãn Technician, lưu không hỏi. Người tạo lệnh, sự cố tự thành người theo dõi. | P1 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` #106; người được giao có tự theo dõi không: chưa kiểm được | `Chạy` một phần | Lấy; cần báo người nhận |
| FR-fleetio-repair-034 | Hoàn thành lại | Lệnh đã mở lại đổi Completed lần nữa: tạo entry mới số khác, dùng ngày và đồng hồ cũ của lệnh, không hỏi lại; Timeline sự cố lại có dòng giải quyết. Hai lượt thử không thấy giới hạn số lần. | P0 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` #104, entry 57858956 | `Chạy` | Hỏi lại ngày; không sinh dòng đồng hồ trùng |
| FR-fleetio-repair-035 | Cài đặt bảo dưỡng | Maintenance Settings: Enable Work Orders, Next Work Order Number, Require a Meter Reading kèm Excluded Vehicle Types, Require Inspections, Require Repair Priority Class, Reason for Repair, Category, hai mục chặn sửa mã mặc định. | P1 | [Cấu hình] | demo | `Xem`, không đổi | `Xem` | Lấy cách nhóm luật; tham số mới, chưa có mã |
| FR-fleetio-repair-036 | Danh mục trạng thái lệnh | Bảng trạng thái có Name, Type, số lệnh; mặc định Open, Pending loại Incomplete, Completed loại Completed. | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | demo | `Xem`, không thêm thử; `Docs` phần thêm | `Xem` | Lấy hai nhóm |
| FR-fleetio-repair-037 | Nhận hàng đơn mua vào lệnh | Nhận đơn mua chọn nơi đến là lệnh có sẵn hoặc lệnh mới: cộng kho trước, trừ khi lưu lệnh, dòng ghi chú "From PO"; huỷ form hàng vẫn ở kho. | P1 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` D14, D15 ở nhóm Kho | `Chạy` | Lấy |
| FR-fleetio-repair-038 | Cơ hội bảo hành trên lệnh | Khối Warranty Opportunities luôn hiện trên lệnh: đếm active, expiring soon, total; Vehicle Coverage khớp đầu việc theo mã phân loại, có View Active Coverage, Complaint, Cause, Correction; Replaced Parts cho phụ tùng. | P2 | [Gói: Bảo dưỡng đội xe] | test | `Chạy` WO #100 nhóm Phương tiện; `Chạy` #103, #104, #106 khối trống | `Chạy`; nút claim chưa thử | Lấy khi có bảo hành |
| FR-fleetio-repair-039 | Đưa ra xưởng ngoài | Get Service at Shop mở hộp giới thiệu Shop Network, cần Enable Shop Network mới dùng. | P2 | [Gói: Bảo dưỡng đội xe] | demo | `Xem`, không bật | `Xem` | Không lấy mạng lưới Mỹ; có thể gửi yêu cầu cho nhà cung cấp dịch vụ của khách |
| FR-fleetio-repair-040 | Đơn giá công theo contact | Contact Technician có đơn giá mặc định; danh sách chọn và hộp Edit Labor hiện đơn giá đó. | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | test | `Chạy` TEST-SUA-KTV; số hiện lệch giữa màn, xem E-014 | `Chạy` | Lấy; đơn giá là dữ liệu của khách |
| FR-fleetio-repair-041 | Tạo, lưu trữ đầu việc | Form "New Custom Service Task" gồm 6 bước gập, Save khoá tới khi Continue hết. Archive không xoá khỏi Fleetio, cập nhật bản ghi liên quan chạy nền. Không thấy gộp đầu việc. | P1 | [Gói: Bảo dưỡng đội xe] [Cấu hình] | test | `Chạy` TEST-SUA-DV-A, TEST-SUA-DV-B | `Chạy` | Lấy Archive; nên có gộp khi trùng |

## 4. Non-Functional Requirements (NFR)

Fleetio không công bố số liệu; các số dưới là quan sát một lần, không phải cam kết.

| ID | Category | Requirement | Priority | Acceptance |
|---|---|---|---|---|
| NFR-fleetio-repair-001 | hiệu năng | AI soạn lệnh chạy nền, người dùng làm tiếp được. | P2 | Quan sát: nháp xong khoảng 30 đến 40 giây, có banner đổi chữ, có thông báo |
| NFR-fleetio-repair-002 | truy vết | Mọi đổi trạng thái có người và thời điểm, kể cả do workflow hay AI. | P0 | Quan sát: dòng thời gian ghi "by work order", "by workflow", "from an AI draft"; **không** ghi đổi Overdue, đóng, mở lại, gỡ khỏi lệnh |
| NFR-fleetio-repair-003 | trách nhiệm AI | Khách tự chịu trách nhiệm quyết định theo gợi ý AI; AI có nguồn và nút phản hồi. | P2 | Quan sát: điều khoản ở trang AI Service Advisor, "Was this helpful?" |
| NFR-fleetio-repair-004 | quyền | Sửa trạng thái cần quyền theo nhóm lệnh đã xong và chưa xong. | P1 | `Docs`: Edit và View Completed hoặc Incomplete Work Orders. Tài khoản một người, chưa kiểm |
| NFR-fleetio-repair-005 | hiệu năng | Thời gian phản hồi cho Invlogis: TBD — đội sản phẩm — khi chi tiết hoá `repair-order`. | P1 | TBD |
| NFR-fleetio-repair-006 | nhất quán dữ liệu | Mở lại lệnh chạy nền; trong vài giây trang vẫn hiện Completed. | P1 | Quan sát: toast "Restoring Work Order #104 data". Invlogis nên khoá thao tác cho tới khi xong |
| NFR-fleetio-repair-007 | tiền tệ | Tiền không có số lẻ phải hiện đúng ở mọi màn. | P0 | Quan sát Fleetio: lệch 100 lần với VND. Invlogis: ca kiểm thử bắt buộc |

## 5. Business Rules

| ID | Rule | Tầng | Trigger | Implements FR | Source | Mức thực tế |
|---|---|---|---|---|---|---|
| BR-fleetio-repair-001 | Sự cố mới luôn ở trạng thái Open, kể cả khi hạn đã qua thì hiển thị Overdue. | [Gói: Bảo dưỡng đội xe] | Lưu sự cố | FR-fleetio-repair-001 | `Chạy` #33 | `Chạy` |
| BR-fleetio-repair-002 | Sự cố đã Resolved hoặc Closed không sửa được đến khi mở lại: nút Edit biến mất. | [Gói: Bảo dưỡng đội xe] | Sửa sự cố | FR-fleetio-repair-004 | `Chạy` #35, #36 | `Chạy` |
| BR-fleetio-repair-003 | Cách mở lại tuỳ nguồn: giải quyết bằng lệnh thì đổi lệnh về chưa xong; bằng ghi chú, bằng Service Entry hoặc đã đóng thì bấm Reopen. Sửa so với bản trước: nút Reopen của sự cố giải quyết bằng entry không khoá. Bỏ tick trong entry là `Docs`, chưa thử. | [Gói: Bảo dưỡng đội xe] | Mở lại | FR-fleetio-repair-027 | `Chạy` #35, #37, #38, #104; `Docs` bỏ tick | `Chạy` |
| BR-fleetio-repair-004 | Sự cố Closed không tính vào chênh lệch thời gian, số km xử lý. | [Gói: Bảo dưỡng đội xe] | Tính chỉ số | FR-fleetio-repair-004 | `Docs` | `Docs` |
| BR-fleetio-repair-005 | Chỉ một trạng thái lệnh là mặc định; trạng thái đang dùng không xoá được. | [Gói: Bảo dưỡng đội xe] [Cấu hình] | Cấu hình | FR-fleetio-repair-036 | `Docs`, `Xem` nhãn Default ở Open | `Docs` |
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
| BR-fleetio-repair-018 | Một sự cố chỉ ở một lệnh khi chọn từ form lệnh; phải gỡ khỏi lệnh cũ mới thêm được vào lệnh khác. Đã gắn lệnh thì khoá Add to Service Entry, Add to Work Order, Resolve with Note. | [Gói: Bảo dưỡng đội xe] | Gắn sự cố | FR-fleetio-repair-031 | `Chạy` | `Chạy` |
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

**Tham số mới cần có nếu Invlogis lấy, chưa có mã:** bắt buộc số đồng hồ khi hoàn thành và loại xe được miễn; bắt buộc phân loại ưu tiên, lý do sửa, nhóm hệ thống; cho phép tồn âm; số lệnh tiếp theo. Fleetio: mặc định bật bắt buộc số đồng hồ, các mục còn lại tắt.

## 6. Error Matrix

Wording giữ nguyên tiếng Anh của Fleetio. Các lỗi có chữ "không báo" là lỗi im lặng do người chạy phát hiện, Fleetio không hiện thông báo nào.

| Error ID | Title | Trigger | Severity | Related FR | Screen state | Recovery | Mức |
|---|---|---|---|---|---|---|---|
| E-fleetio-repair-001 | Thiếu ngày bắt đầu khi có số đầu | Có số đồng hồ đầu, thiếu ngày: "Start Odometer is invalid", "can't be blank if an odometer value is entered" | major | FR-fleetio-repair-006 | Dải lỗi đầu form, viền đỏ, toast "Work Order could not be updated" | Nhập ngày | `Chạy` |
| E-fleetio-repair-002 | Thiếu số đồng hồ cuối | Hoàn thành thiếu số cuối: "Please edit and fix the following errors: Ending Meter Entry can't be blank (per your account settings)" | major | FR-fleetio-repair-012 | Toast, trạng thái giữ nguyên | Sửa lệnh | `Chạy` #99 |
| E-fleetio-repair-003 | Lưu form sự cố trống | "You are not authorized to perform this action." | minor | FR-fleetio-repair-001 | Toast, không chỉ trường | Điền đủ. Không nên học | `Chạy` một lần |
| E-fleetio-repair-004 | Không đủ điều kiện đánh giá | "Add a service task to run an assessment.", "Add line item costs to run an assessment.", trên entry "Add a line item to run an assessment." | minor | FR-fleetio-repair-021 | Khối Assessment | Bổ sung | `Chạy` |
| E-fleetio-repair-005 | Sai tiền phụ tùng | Giá phụ tùng lưu đúng trong form nhưng trang chi tiết lệnh và Service Entry hiện gấp 100 lần: 300.000 thành 30.000.000 ₫, 5 thành 500 ₫, 12,5 thành 1.250 ₫; tổng 2.550.000 thành 255.000.000 ₫. Sửa so với bản trước: hộp Add Part không sai | critical | FR-fleetio-repair-008 | Không báo lỗi. Ô parts_cost của form sửa theo số sai, dòng vẫn số cũ | Không có cách sửa tay; lỗi của Fleetio, xem Mục 11 | `Chạy` |
| E-fleetio-repair-006 | Thiếu Started At khi hoàn thành | "Please edit and fix the following errors: Started At can't be blank" | major | FR-fleetio-repair-012 | Toast, trạng thái giữ nguyên | Nhập ngày bắt đầu | `Chạy` |
| E-fleetio-repair-007 | Thiếu đồng hồ đầu khi hoàn thành | "Starting Meter Entry can't be blank (per your account settings)", "Odometer can't be blank (per your account settings)"; ở WO #102 "Start Odometer can't be blank (per your account settings)" | major | FR-fleetio-repair-012 | Toast, trạng thái giữ nguyên | Nhập số đầu | `Chạy` |
| E-fleetio-repair-008 | Có số cuối, thiếu ngày hoàn thành | Ô Actual Completion Date "can't be blank", toast "Work Order could not be updated" | major | FR-fleetio-repair-029 | Viền ô, toast | Nhập ngày | `Chạy` |
| E-fleetio-repair-009 | Số cuối nhỏ hơn đầu | "Completion Odometer must be greater than or equal to start meter entry." | major | FR-fleetio-repair-029 | Banner đầu form | Sửa số | `Chạy` |
| E-fleetio-repair-010 | Kỹ thuật viên mẫu trên xe thường | "Contact is a sample, and cannot be used with non sample vehicles" | major | FR-fleetio-repair-009 | Báo ở mọi lần sửa, không báo lúc tạo | Không gỡ được ở lần thử; chỉ xảy ra với dữ liệu Sample | `Chạy` #103 |
| E-fleetio-repair-011 | Đổi dòng công hoặc trạng thái khi dòng công lỗi | "Work Order Labor Line Items is invalid", toast "Work Order could not be updated" | major | FR-fleetio-repair-011 | Toast, trạng thái giữ nguyên | Không có ở lần thử; lệnh kẹt | `Chạy` #103 |
| E-fleetio-repair-012 | Service Entry thiếu ngày | Ô Completion Date chỉ có placeholder giờ hiện tại, lưu báo "can't be blank", toast "Service Entry could not be created" | minor | FR-fleetio-repair-014 | Viền ô, toast. Odometer không báo riêng tới khi gõ | Gõ lại ngày. Không nên học | `Chạy` |
| E-fleetio-repair-013 | Trùng tên đầu việc | "has already been taken", toast "Service Task could not be created" | minor | FR-fleetio-repair-041 | Viền ô, toast | Đổi tên | `Chạy` |
| E-fleetio-repair-014 | Sai tiền công giữa các màn | Contact nhập 100.000: danh sách ghi 10.000.000 ₫/hr, hộp Edit Labor "Current default labor rate is ₫100000.00". Kỹ thuật viên mẫu: danh sách 480.000 ₫/hr, vào dòng 4.800 ₫ | critical | FR-fleetio-repair-040 | Không báo lỗi | Công nhập tay qua hộp lưu đúng | `Chạy` |
| E-fleetio-repair-015 | Xuất phụ tùng quá tồn | Không báo; tồn về âm (K12 còn -10,5; #100 còn -2) | major | FR-fleetio-repair-032 | Hộp chỉ ghi "This will make an inventory adjustment" | Nhập kho, chỉnh tồn | `Chạy` |
| E-fleetio-repair-016 | Tick sự cố không vào lệnh | Không báo; #34 không ở Resolved Issues nhưng cột Work Orders vẫn ghi #103 và bị khoá ở lệnh mới | major | FR-fleetio-repair-007 | Không báo lỗi | Chưa rõ nguyên nhân, xem OQ-11 | `Chạy` một lần |
| E-fleetio-repair-017 | Nháp AI hứa mà không làm | Hộp ghi "Repair Priority Class Non-Scheduled" sẽ tự điền; lệnh tạo ra để trống | minor | FR-fleetio-repair-020 | Không báo lỗi | Điền tay | `Chạy` #99, #106 |
| E-fleetio-repair-018 | Số đồng hồ đầu chặn do thời điểm | "must be less than 2,499 or marked as void" dù đồng hồ hiện cao hơn; ngày lệnh lệch múi giờ tài khoản nên xếp trước các dòng đồng hồ mới | major | FR-fleetio-repair-029 | Viền ô | Nhập số thấp hơn | `Chạy` nhóm Nhắc #101 |

## 7. Success Criteria

| ID | Outcome nghiệp vụ | Đo bằng | Mốc đạt |
|---|---|---|---|
| SC-fleetio-repair-01 | Mọi sự cố truy được đến cách xử lý | Tỷ lệ sự cố có lệnh, entry hoặc ghi chú | TBD |
| SC-fleetio-repair-02 | Thời gian xử lý đo tự động | Fleetio có Time to Resolve, Kilometers to Resolve | Có sẵn khi lưu |
| SC-fleetio-repair-03 | Không nhập lại khi hoàn thành lệnh | Đếm thao tác từ hoàn thành đến lịch sử | Một thao tác |

## 8. Data Entities (tóm tắt — chi tiết ở erd.md)

Issue, Work Order, Work Order Line Item, Labor Line, Part Line, Service Entry, Service Task, Fault, Warranty, AI Draft, Assessment, Meter Entry, Inventory Activity, Contact, Work Order Status. Chi tiết: [[docs/_research/fleetio/srs/fleetio-repair-erd.md|ERD]].

## 9. Flows (tóm tắt — chi tiết ở flows.md)

Sự cố đến hoàn thành lệnh; mở lại, hoàn thành lại; hạn và quá hạn; đóng, giải quyết bằng ghi chú, bằng entry; khoá và gỡ sự cố; dòng phụ tùng và tồn; AI soạn lệnh; AI đánh giá; sao chép; đầu việc; bảo hành; nhận hàng vào lệnh. Chi tiết: [[docs/_research/fleetio/srs/fleetio-repair-flows.md|Flows]], [[docs/_research/fleetio/srs/fleetio-repair-states.md|States]], [[docs/_research/fleetio/srs/fleetio-repair-usecases.md|Use case]], [[docs/_research/fleetio/srs/fleetio-repair-userflow.md|User flow]].

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
| Trừ kho từ lúc lưu dòng, xoá dòng có bút toán đảo ghi nguồn | Phù hợp xưởng cấp phụ tùng trước khi sửa; dễ đối soát | `Chạy` |
| Nhận hàng vào lệnh qua kho hai bước | Hàng không mất khi huỷ form; hợp phụ tùng đặt riêng cho xe nằm xưởng | `Chạy` |
| AI nháp chạy nền, gom sự cố cùng xe, cảnh báo lệnh đang mở | Đỡ đưa xe vào xưởng hai lần, quý với đầu kéo | `Chạy` |
| Assessment soi lệnh khác cùng xe trùng đầu việc | Phát hiện hai lệnh làm cùng việc | `Chạy` |
| Bảo hành khớp theo mã đầu việc | Cơ hội hiện ngay trên lệnh | `Chạy` |

**Điểm không nên học (`Chạy`):**

| Điểm | Thấy gì | Nên làm ở Invlogis |
|---|---|---|
| Ghi trùng số km | #99 đóng lệnh sinh 3 dòng: đầu, cuối từ lệnh và cuối từ Service Entry. #104 lần đầu 2 dòng, hoàn thành lại thêm dòng trùng nguồn entry | Ghi một lần cho mỗi lần hoàn thành |
| Nháp AI lệch | Ghi tự điền Non-Scheduled, lệnh tạo ra để trống | Điền đúng như hứa |
| Lệch tiền | Sửa lại: form đúng, trang chi tiết và entry gấp 100 lần với ₫; đơn giá công lệch theo chiều khác | Ca kiểm thử định dạng tiền Việt ở mọi màn |
| Xoá Service Entry khi mở lại | `Chạy`: URL ra Not Found, không còn bản xem được | Giữ vết, ghi lần mở lại |
| Hộp mở lại thiếu hậu quả | Không nói entry bị xoá, sự cố mở lại | Nêu rõ từng hậu quả trước khi xác nhận |
| Mở lại không đảo đồng hồ | Dòng 2.300, 2.350 còn nguyên | Huỷ dòng theo lần mở lại |
| Hoàn thành lại giữ ngày cũ | Time to Resolve 23 mins dù hoàn thành lại sau 41 phút | Hỏi lại ngày, tính lại chỉ số |
| Timeline thiếu | Không ghi Overdue, đóng, mở lại, gỡ; có chỗ xoá dòng cũ, có chỗ giữ dòng cũ | Ghi đủ, không xoá dòng |
| Tồn âm im lặng | Không cảnh báo | Cảnh báo; chặn hay không theo khách, tham số mới, chưa có mã |
| AI đánh giá sai | Giá 30 triệu vẫn Acceptable; nêu quá hạn đã không còn | Chỉ gợi ý, không làm điều kiện |
| Discard không hỏi | Mất nháp ngay | Xác nhận, ghi vết |
| Toast cũ nổi lại | "Issue #36 was closed." hiện ở trang #38 | Xoá toast khi rời trang |

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
* [ ] OQ-11: Vì sao #34 tick vào #103 mà không ở Resolved Issues? Chạy một lần, chưa rõ. — Nguồn khách: không áp dụng
* [ ] OQ-12: Xoá cả lệnh có hoàn kho, hoàn đồng hồ, mở lại sự cố không? Không chạy vì xoá vĩnh viễn. — Nguồn khách: không áp dụng
* [ ] OQ-13: Điều kiện nào sinh dòng đồng hồ trùng: #99 lần đầu có, #104 lần đầu không, lần 2 có? — Nguồn khách: không áp dụng
* [ ] OQ-14: Draft Work Order từ sự cố đã gắn lệnh, chọn lệnh khác thì sự cố có ở hai lệnh không? Tooltip viết "all Work Orders". Chưa thử. — Nguồn khách: không áp dụng
* [ ] OQ-15: Close có dùng được khi sự cố đang gắn lệnh không? Chưa thử. — Nguồn khách: không áp dụng
* [ ] OQ-16: Trạng thái tuỳ biến, phân quyền theo nhóm lệnh, Add to Existing Service Entry, bỏ tick sự cố trong entry, nút claim bảo hành chạy thế nào? Chưa thử. — Nguồn khách: không áp dụng
* [ ] OQ-17: Delta có cần lệnh gom cả đầu kéo và mooc không? — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-18: Xưởng Delta cấp phụ tùng lúc lập lệnh hay lúc xong việc? Quyết định thời điểm trừ kho. — Nguồn khách: chưa có trong tài liệu khách gửi

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
| C18 Thêm vào entry có sẵn | Hộp có lựa chọn | Chưa lưu | `Xem` |
| C19 Entry không gõ ngày | Ô hiện giờ hiện tại | "can't be blank", "Service Entry could not be created"; Odometer không báo riêng tới khi gõ | `Chạy` |
| C20 Entry đồng hồ thấp | 2.100 khi xe 2.200 | Lưu, không cảnh báo; Meter History thêm dòng "100 km ago"; số hiện tại giữ 2.200 | `Chạy` |
| C21 Entry không có dòng việc | Entry 57856983 | Lưu được, vẫn giải quyết sự cố; "No line items to show." | `Chạy` |
| C22 Sự cố sau khi lưu entry | #37 | Resolved, Resolved Meter Entry 2,100 km, Timeline "Issue Resolved by service entry", Resolved By là người lưu | `Chạy` |
| C23 Mở lại sự cố giải quyết bằng entry | #37 | Nút **không** khoá; "Successfully reopened Issue."; entry còn nguyên nhưng "No issues to show"; Timeline vẫn giữ dòng cũ, không ghi mở lại | `Chạy` |
| C24 Sửa entry tạo tay | Lưu không đổi gì | Thành công | `Chạy` |
| C25 Đưa ra xưởng ngoài | Bấm Get Service at Shop | Hộp giới thiệu Shop Network; không bật | `Xem` · issue-shop-network.jpg |
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
| C75 Menu khi đã ở lệnh | Sự cố đã gắn | Draft Work Order, Get Service at Shop dùng được; ba mục còn lại xám có khoá, tooltip. Close chưa thử | `Chạy` · issue-menu-locked-tooltip.jpg |
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
| C87 Thêm nháp vào lệnh đang có | Menu "Add to Work Order #104" | Thấy, không bấm | `Xem` · wo-draft-add-menu.jpg |
| C88 Bỏ nháp | Discard trên #45 | Mất ngay, không hỏi, không vết | `Chạy` |
| C89 Nháp từ nhắc | Nhắc D Upcoming | Mục xám có khoá, bấm không có gì | `Chạy` nhóm Nhắc |
| C90 Assessment chưa đủ | Chưa việc; việc không tiền; entry trống | Ba câu ở E-004 | `Chạy` |
| C91 Assessment tự chạy | Có tiền | Chữ tiến độ, "Acceptable", "Auto-assessed", số nguồn | `Chạy` |
| C92 Chạy lại đánh giá | #103 | Menu đổi Rerun; vẫn "Acceptable"; nêu "the open overdue-by-date issue" dù #33 đã hết quá hạn | `Chạy` |
| C93 In | #103 | PDF hai trang, tab mới; khung xem không hiện trong tab tự động | `Chạy` |
| C94 Gửi PDF | Menu | Không bấm | `Xem` |
| C95 Giao việc | #106, Emergency, TEST-SUA-KTV | Lưu, không hỏi; người nhận không email nên không ai bị báo | `Chạy` |
| C96 Theo dõi | Tạo lệnh, sự cố | Người tạo tự theo dõi. Người được giao chưa kiểm được | `Chạy` một phần |
| C97 Form đầu việc | New Custom Service Task | Save khoá tới khi Continue hết 6 bước | `Chạy` |
| C98 Gợi ý đầu việc | Tên tự đặt | "No Service Task Recommendation for ..." | `Chạy` |
| C99 Trùng tên đầu việc | Tên đã có | E-013 | `Chạy` |
| C100 Gộp đầu việc | Actions, More Actions | Không thấy Merge | `Xem` |
| C101 Lưu trữ đầu việc | TEST-SUA-DV-B | Hộp xác nhận; bản ghi liên quan cập nhật nền | `Chạy` |
| C102 Mã lỗi | 16 dòng Sample | Cột, tab, menu; xe TEST không có thiết bị; không thao tác | `Xem` |
| C103 Danh mục trạng thái | `work_order_statuses` | 3 mặc định; không thêm | `Xem` |
| C104 Cài đặt bảo dưỡng | `account/maintenance_settings/edit` | Require a Meter Reading bật; các mục khác tắt; không đổi | `Xem` · maintenance-settings.jpg |
| C105 Xong hết dòng mới hoàn thành | Luật theo `Docs` | Không kiểm vì không đổi Settings | Không chạy |
| C106 Khối bảo hành khi xe không có | #103, #104, #106 | "No vehicle warranty opportunities to show.", 0 active | `Chạy` |
| C107 Có bảo hành, chưa khớp | WO #100, chỉ có phụ tùng má phanh | Phụ tùng đứng riêng không gợi ý | `Chạy` nhóm Phương tiện · wo-warranty-before.jpg |
| C108 Có bảo hành, khớp mã | Thêm đầu việc Brake Inspection | "Warranty Opportunities (1)"; View Active Coverage; Complaint, Cause, Correction trống | `Chạy` nhóm Phương tiện · wo-warranty-opportunity.jpg |
| C109 Tự tính hết hạn | 01/10/2026 + 1 Years | End Date 10/01/2027, Active | `Chạy` nhóm Phương tiện |
| C110 Số đồng hồ bảo hành | Nhập 1000, Coverage 50.000 | Danh sách ghi Start Meter 1 km, End Meter 50,001 km; chưa rõ do ô nhập hay định dạng | `Chạy` nhóm Phương tiện |
| C111 Mẫu bảo hành | Xe không có Make, Model | "No options"; lý do chưa kiểm | `Xem` |
| C112 Nút claim | Trên cơ hội bảo hành | Chưa thử | Không chạy |
| C113 Đồng hồ xe khi tạo | Ô Current Reading gõ 10.000 | Không vào bản lưu; xe hiện 0 km | `Chạy` |
| C114 Xe thứ hai | TEST-SUA-02 | Save Vehicle khoá mãi, không báo lỗi. Nhóm Lốp thấy câu "maximum number of records" | `Chạy` |
| C115 Nhận hàng vào lệnh có sẵn | D14 | Sổ +5 trước, -5 khi lưu lệnh; dòng ghi chú "From PO #2" | `Chạy` nhóm Kho |
| C116 Nhận hàng vào lệnh mới, huỷ | D15 | Hàng ở kho, đơn Full, không có lệnh | `Chạy` nhóm Kho |
| C117 Lưu form sự cố trống | Lượt trước | E-003 | `Chạy` một lần |
| C118 Bỏ dở form | Lượt trước | Trình duyệt "Leave site?" | `Chạy` |
| C119 Đầu kéo, mooc | Sự cố, lệnh theo một Vehicle | Chỉ chạy Car; không có cách gom | `Suy` |
