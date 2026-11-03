---
type: research
feature: fleetio-saas-platform
updated: 2026-11-03
---

# Nền tảng SaaS — Use cases

## Use cases

| UC | Tên | Actor | FR | Màn | Lỗi | OQ |
|---|---|---|---|---|---|---|
| UC-configure-tenant | Cấu hình theo khách | Administrator | 001–004, 023, 040, 047, 050, 064 | 4.1 | E-003, E-007 | OQ-4, OQ-10 |
| UC-grant-access | Phân quyền | Administrator | 005–007, 044, 045, 046, 063 | 4.2, 4.3, 5.10 | E-001, E-008 | OQ-1, OQ-8, OQ-9 |
| UC-automate | Tạo tự động hoá | Administrator | 012–014, 030–037, 058 | 3.1–3.9 | E-005, E-009, E-011, E-019, E-021, E-024, E-025, E-026 | OQ-2, OQ-5, OQ-6, OQ-7, OQ-14 |
| UC-edit-automation | Sửa automation đang bật | Administrator | 032, 056, 057 | 3.4, 3.10 | E-018 | OQ-7, OQ-16 |
| UC-investigate-run | Tra lượt automation thất bại | Administrator, đội hỗ trợ | 034, 060 | 3.5, 3.6, 3.11 | E-011, E-021 | OQ-6 |
| UC-automate-vehicle | Luật đổi trạng thái xe | Administrator | 041, 059 | 3.12 | E-017 | OQ-5, OQ-17 |
| UC-work-list | Làm việc trên danh sách | Mọi người dùng | 009–011 | Mọi danh sách | E-002 | OQ-18 |
| UC-follow-record | Theo dõi, bình luận, nhận thông báo | Mọi người dùng | 017, 018, 022, 053, 061 | 4.4, 5.6, 5.7 | E-016, E-020 | OQ-20 |
| UC-manage-document | Tải và gắn tài liệu | Mọi người dùng có quyền | 024, 062 | 5.5, 5.8, 5.9 | E-022, E-023 | — |
| UC-start-tenant | Bắt đầu dùng | Admin của khách | 015, 016 | 1.1 | — | OQ-3 |
| UC-see-attention | Xem việc cần xử lý | Quản lý | 008 | 1.1 | E-002 | — |
| UC-reports | Xem báo cáo | Quản lý | 019, 051, 054, 065 | 2.1, 2.2, 2.6, 2.10 | E-002, E-014, E-027 | OQ-11 |
| UC-save-report | Lưu, yêu thích báo cáo | Quản lý | 055 | 2.8, 2.9 | — | OQ-11 |
| UC-share-report | Chia sẻ báo cáo | Quản lý | 052 | 2.2, 2.4, 2.5 | E-010, E-013 | — |
| UC-ask-data | Hỏi dữ liệu bằng lời | Quản lý | 020 | 2.3, 2.7 | E-012, E-015 | OQ-13 |
| UC-manage-contact | Quản lý liên hệ | Administrator | 038, 063 | 5.1, 5.10 | E-006, E-024 | OQ-8 |
| UC-book-vehicle | Đặt xe dùng chung | Administrator, Operator | 043, 066, 067 | 5.4, 5.11, 5.12, 5.13 | E-028, E-029 | OQ-12 |
| UC-add-vehicle | Thêm xe trong hạn mức | Administrator | 023, 039, 041 | 5.2 | E-003, E-004 | OQ-12, OQ-15 |

Số FR, lỗi viết tắt, đầy đủ có tiền tố `fleetio-saas-platform`.

## UC-configure-tenant — Cấu hình theo khách

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Mở Settings, tìm mục hoặc duyệt theo nhóm | Hiện các trang chia nhóm: 59 trang cấp tài khoản, 7 trang cá nhân (OQ-10); bảng các trang đã đọc ở Mục 14 của spec |
| 2 | Đổi tuỳ chọn, đọc mô tả | Hiện phạm vi tác động |
| 3 | Lưu | Áp dụng; nhiều luật chỉ áp về sau |

**Nhánh:** 2a Tắt module: ẩn menu. 2b Vượt giới hạn gói: chặn tạo, Explore Plans (`Chạy` với xe). 2c Require Group khi còn thiếu nhóm: ô khoá, liệt kê số thiếu (`Xem`). Lượt chạy không Save trang nào.

## UC-grant-access — Phân quyền

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Chọn hoặc tạo Role | 30 module, mỗi module có quyền con (`Xem`) |
| 2 | Chọn Record Set theo xe, liên hệ, kho, biểu mẫu | Mẫu sẵn hoặc điều kiện; Manage và View khai riêng (`Xem`) |
| 3 | Gán cho người dùng | Dữ liệu ngoài phạm vi không hiện (`Suy`, chưa kiểm) |

**Nhánh:** 1a Vai mặc định khoá. 2a Bản mặc định khoá sửa. 2b Đổi Record Type sau khi tạo: không được.

Manage Users trỏ sang `contacts/users` ngoài Settings; không mời người trong lượt chạy. Mở truy cập từ form liên hệ: Role mặc định Fleet Manager, Record Sets đều Full Access (`Xem`, không lưu).

## UC-automate — Tạo tự động hoá

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Add Automation hoặc Browse Templates | Trình dựng 3 khối, tên theo thời điểm; Apply mẫu điền sẵn, chưa lưu |
| 2 | Chọn loại bản ghi, kiểu sự kiện | Thanh phải |
| 3 | Thêm điều kiện, hành động | Save mở khi đủ |
| 4 | Save | Lưu ở Disabled |
| 5 | Gạt bật, xác nhận | Enabled, sinh v.1; bản ghi cũ không chạy bù |
| 6 | Xem danh sách, Run History, Run Result | Đếm lượt, phiên bản, log JSON |

**Nhánh:** 1a Rời trang: không có bản rác. 1b Make a Copy: mở bản chưa lưu, tên thêm " (copy)". 3a Mẫu thiếu giá trị: "Missing Value". 3b Mẫu Send Email có câu cứng ">$1,000.00": sửa tay trước khi lưu (E-019). 5a Archive: tắt ngay, chỉ đọc; Restore về Disabled. 5b Tắt rồi bật lại: vẫn phiên bản cũ. 6a Lượt thất bại: xem UC-investigate-run. 4a Service Entry, Update Field Repair Priority Class: Save bị từ chối (E-025). 4b Tự duyệt đơn mua thiếu điều kiện Pending Approval: Save bị chặn (E-026). 5c Restore: không có hộp xác nhận, không tự bật.

Nhóm này đã lưu 9 automation, đều đã tắt; xem Mục 13 và Mục 20 của spec.

## UC-edit-automation — Sửa automation đang bật

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Edit, đổi nội dung | Băng "You have unsaved changes on this enabled automation" |
| 2 | Save Automation | Lên phiên bản mới, vẫn Enabled, không hỏi lại, hiệu lực ngay |
| 3 | Tạo bản ghi khớp | Lượt ghi phiên bản mới, hành động theo nội dung mới |
| 4 | Mở Version History | Danh sách phiên bản, Created At, Created By |

**Nhánh:** 2a Discard Unsaved Changes: giữ bản hiện tại (`Xem`). 4a Mở bản cũ: hiện nội dung bản mới (E-018), thấy 1 lần.

## UC-investigate-run — Tra lượt automation thất bại

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Mở danh sách hoặc Run History | Cột Failed Runs, nhãn FAILURE đỏ |
| 2 | Mở lượt | Băng đỏ lỗi nguyên văn, Version, Processed At, Records, Trigger Record, Trigger Type, Triggered At, Triggered By |
| 3 | View Full Log | JSON từng bước, caused_by, thrown_by |
| 4 | Sửa dữ liệu hoặc tắt automation | Lượt lỗi không tự chạy lại trong khoảng 5 phút đã đo |

**Nhánh:** 1a Không vào Run History: không có kênh báo trong app nào khác. 1b Bật Failure Notification Email: không chạy.

## UC-automate-vehicle — Luật đổi trạng thái xe

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Chọn trigger Vehicle Updated | Không có Deleted; 71 trường điều kiện |
| 2 | Chọn xe, hành động Update Vehicle Status | Update Field chỉ có 5 trường |
| 3 | Bật, sửa một trường bất kỳ của xe | Status đổi trong vài giây, Status Updates ghi "Fleetio Automation" |

**Nhánh:** 3a Người đổi ngược: lưu được, 1 giây sau bị đổi lại, không báo (E-017). 3b Lượt do automation đổi xe: không sinh lượt mới. Đảo ngược: tắt automation rồi đổi tay.

## UC-work-list — Làm việc trên danh sách

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Chọn tab, lọc nhanh | Đổi kết quả, URL giữ điều kiện |
| 2 | Thêm điều kiện, chọn cột, nhóm | Bảng đổi |
| 3 | Save View hoặc Add Tab | Lưu thành tab; Shared with Private, Admins Only, Specific Roles, Specific Users, Everyone |
| 4 | Tick nhiều dòng | Hiện thao tác hàng loạt nếu có quyền (`Suy`, chưa bấm) |

**Nhánh:** 3a Đang ở "Fleetio Standard View": có khoá, chỉ Save as New View hoặc Clear Unsaved Changes. 1a Mở lại trang: về đúng tab dùng lần trước. Bấm dòng trên Issues sang trang chi tiết, không có xem nhanh.

## UC-follow-record — Theo dõi, bình luận, nhận thông báo

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Mở bản ghi, Watch hoặc Unwatch | Đổi cụm người theo dõi, không ghi lịch sử |
| 2 | Viết comment, gõ @ | Danh sách liên hệ kèm biểu tượng khoá |
| 3 | Mở chuông | Inbox, Archived; All Activity, Comments Only, @ Mentions |
| 4 | Mở Record History | Date, Changes By, Changes Made, lọc khoảng ngày |

**Nhánh:** 2a Gõ không dấu, có gạch nối: không ra người (E-020). 3a 0 hồ sơ thông báo: Inbox vẫn có thông báo. 4a AI xếp mức thất bại: chỉ thấy ở đây (E-016).

## UC-manage-document — Tải và gắn tài liệu

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Upload Document | Hộp Filestack; "Document was successfully added." |
| 2 | Tải lại danh sách | Dòng tệp có File Size, Location |
| 3 | Select Vehicles, gắn xe | "Attached"; trang tệp ghi "1 Vehicle" |
| 4 | Mở trang tệp | Khung xem, Type, Auto-Delete, Comments |

**Nhánh:** 2a Chưa tải lại: "No results to show" (E-022). 3a Gắn theo loại, nhóm: chưa bấm. 4a Tệp không phải PDF: khung xem 0 trang (E-023).

## UC-start-tenant — Bắt đầu dùng

Xem Flow 3. Bộ đếm Get Started đổi theo việc đã làm và có khi đổi mẫu số (`Chạy` 1/6, 1/5, 2/6, 3/6); lượt 03/11 thấy 3/5 và 3/6 giữa các trang.

## UC-see-attention — Xem việc cần xử lý

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Mở Dashboard | Từng thẻ tải riêng; "0 minutes ago", Refresh data, All groups |
| 2 | Bấm số trên thẻ | Mở danh sách đúng bộ lọc; đích từng thẻ ở Mục 13.6 của spec |
| 3 | Lọc nhóm, tuỳ biến, thêm widget | Lưu dashboard |

**Nhánh:** 2a "ROs Needing Approval" rỗng: không có đích.

## UC-reports — Xem báo cáo

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Chọn nhóm hoặc tìm | Thẻ báo cáo có mô tả, nhóm; 49 báo cáo, 13 nhóm |
| 2 | Mở, lọc | Biểu đồ Summary, Top Vehicles; Filters, Columns, phân trang (`Chạy` Issues Report; lượt 3 đọc cột 48/49, bộ lọc chỉ ở Issues) |
| 3 | Lưu, yêu thích | Vào Favorites, Saved, xem UC-save-report |
| 4 | Export CSV, Print | Export Visible Columns, Export All Columns (`Xem`), chỉ giao diện mới |

**Nhánh:** 2a `expense_entries` lỗi 500 (E-014). 2b Giao diện cũ: không thấy Share, Export CSV. 2c Ba kiểu bộ lọc khác nhau theo báo cáo; `job_assignments_summary_by_job` không lọc được (Flow 24). 2d `purchase_orders` cộng cả Draft (E-027).

## UC-save-report — Lưu, yêu thích báo cáo

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Lọc báo cáo, bấm Save | Hộp New Saved Report, Visibility mặc định Private |
| 2 | Nhập Name, lưu | Vào Reports › Saved |
| 3 | Bấm sao | Favorites tăng |
| 4 | Mở báo cáo đã lưu | Tab mới, giữ bộ lọc |

**Nhánh:** 1a Public, Email Schedule: không chạy. 2a Private vẫn gửi email được cho người có quyền báo cáo gốc (câu trên hộp, `Xem`).

## UC-share-report — Chia sẻ báo cáo

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Bấm Share trên báo cáo | Sinh ngay link công khai, hạn (Fleetio: 7 ngày), không hỏi trước |
| 2 | Gửi link cho người ngoài | Ai có link xem được dữ liệu |
| 3 | Vào Reports › Shared, bấm Unshare, xác nhận | Shared giảm, link không còn báo cáo |

**Nhánh:** 3a Bấm "click here to unshare" trong hộp: không có tác dụng, link vẫn sống (E-010). Đề xuất Invlogis ở NFR-fleetio-saas-platform-010.

## UC-ask-data — Hỏi dữ liệu bằng lời

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Bấm Ask a data question | Mở AI Data Analyst, khung nhúng từ ThoughtSpot |
| 2 | Gõ câu hỏi | Khoảng 40 đến 90 giây sau trả câu trả lời và bảng |
| 3 | Show work, chọn data model | Xem cách làm; lưu My Conversations |

**Nhánh:** 2a Số sai so với dữ liệu thật, không báo lỗi (E-012); `Chạy` lượt 2 đủ 2 câu, lượt 3 sai 10/12. 2b Xe mới tạo: "does not exist" (E-015). 2c Hỏi ngày dữ liệu: "does not expose". 3a Mở lại chat cũ: banner dữ liệu có thể đã đổi.

## UC-manage-contact — Quản lý liên hệ

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Tạo liên hệ, nhập First Name | Không cần email |
| 2 | Tick Operator, Employee, Technician | Quyết định gán xe, ghi công |
| 3 | Chọn User Access | No Access mặc định; Enable Access mở form Role, Record Sets (`Xem`, không lưu) |
| 4 | Lưu | Có hồ sơ; "This Contact doesn't have user access." |

**Nhánh:** 1a Trùng tên: vẫn lưu, không cảnh báo. 2a Chưa tick Operator mà gán xe: bị chặn (E-006).

## UC-book-vehicle — Đặt xe dùng chung

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Administrator tạo Motor Pool | Name, Groups, Vehicle Types, Vehicle Statuses; tuỳ chọn tính phí, bắt buộc lý do, tự duyệt |
| 2 | Add Vehicle Reservation, chọn pool | Hiện Vehicle Types của pool, không chọn xe cụ thể |
| 3 | Chọn Operator, nhập lý do, Pick Up, Drop Off | Chỉ liệt kê liên hệ có đăng nhập và là Operator |
| 4 | Submit Reservation | Chưa kiểm: chưa tạo được đặt xe nào |

**Nhánh:** 3a Không có Operator hợp lệ: "No options" (E-028). 4a Thiếu dữ liệu: "Failed to create Reservation" (E-029). Duyệt, gán xe, tính phí, tự duyệt chưa chạy.

## UC-add-vehicle — Thêm xe trong hạn mức

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Mở New Vehicle | Form 6 phần, trường ở Mục 19 của spec |
| 2 | Nhập, bấm Save Vehicle | Kiểm trường bắt buộc, kiểm hạn mức |
| 3 | Xe được tạo | Chưa kiểm, tài khoản đã 5 of 5 |

**Nhánh:** 2a Thiếu tên: E-004. 2b Hết hạn mức: E-003, kể cả khi đủ tên.
