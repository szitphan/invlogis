---
type: research
feature: fleetio-saas-platform
updated: 2026-11-03
---

# Nền tảng SaaS — Use cases

## Use cases

| UC | Tên | Actor | FR | Màn | Lỗi | OQ |
|---|---|---|---|---|---|---|
| UC-configure-tenant | Cấu hình theo khách | Administrator | 001–004, 023, 040, 047, 050 | 4.1 | E-003, E-007 | OQ-4, OQ-10 |
| UC-grant-access | Phân quyền | Administrator | 005–007, 044, 045, 046 | 4.2, 4.3 | E-001, E-008 | OQ-1, OQ-8, OQ-9 |
| UC-automate | Tạo tự động hoá | Administrator | 012–014, 030–037 | 3.1–3.9 | E-005, E-009, E-011 | OQ-2, OQ-5, OQ-6, OQ-7, OQ-14 |
| UC-work-list | Làm việc trên danh sách | Mọi người dùng | 009–011 | Mọi danh sách | E-002 | — |
| UC-start-tenant | Bắt đầu dùng | Admin của khách | 015, 016 | 1.1 | — | OQ-3 |
| UC-see-attention | Xem việc cần xử lý | Quản lý | 008 | 1.1 | E-002 | — |
| UC-reports | Xem báo cáo | Quản lý | 019, 051 | 2.1, 2.2 | E-002 | OQ-11 |
| UC-share-report | Chia sẻ báo cáo | Quản lý | 052 | 2.2, 2.4, 2.5 | E-010, E-013 | — |
| UC-ask-data | Hỏi dữ liệu bằng lời | Quản lý | 020 | 2.3 | E-012 | OQ-13 |
| UC-manage-contact | Quản lý liên hệ | Administrator | 038 | 5.1 | E-006 | OQ-8 |
| UC-add-vehicle | Thêm xe trong hạn mức | Administrator | 023, 039, 041 | 5.2 | E-003, E-004 | OQ-12, OQ-15 |

Số FR, lỗi viết tắt, đầy đủ có tiền tố `fleetio-saas-platform`.

## UC-configure-tenant — Cấu hình theo khách

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Mở Settings, tìm mục hoặc duyệt theo nhóm | Hiện các trang chia nhóm, bảng 56 tên ở Mục 14 của spec (số trang xem OQ-10) |
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

Manage Users trỏ sang `contacts/users` ngoài Settings; không mời người trong lượt chạy.

## UC-automate — Tạo tự động hoá

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Add Automation hoặc Browse Templates | Trình dựng 3 khối, tên theo thời điểm; Apply mẫu điền sẵn, chưa lưu |
| 2 | Chọn loại bản ghi, kiểu sự kiện | Thanh phải |
| 3 | Thêm điều kiện, hành động | Save mở khi đủ |
| 4 | Save | Lưu ở Disabled |
| 5 | Gạt bật, xác nhận | Enabled, sinh v.1; bản ghi cũ không chạy bù |
| 6 | Xem danh sách, Run History, Run Result | Đếm lượt, phiên bản, log JSON |

**Nhánh:** 1a Rời trang: không có bản rác. 3a Mẫu thiếu giá trị: "Missing Value". 5a Archive: tắt ngay, chỉ đọc; Restore về Disabled. 6a Lượt thất bại: chưa tái hiện.

Đã lưu 3 automation, xem Mục 13 và Mục 20 của spec.

## UC-work-list — Làm việc trên danh sách

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Chọn tab, lọc nhanh | Đổi kết quả, URL giữ điều kiện |
| 2 | Thêm điều kiện, chọn cột, nhóm | Bảng đổi |
| 3 | Save View hoặc Add Tab | Lưu thành tab |
| 4 | Tick nhiều dòng | Hiện thao tác hàng loạt nếu có quyền |

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
| 2 | Mở, lọc | Biểu đồ Summary, Top Vehicles; Filters, Columns, phân trang (`Chạy` Issues Report; 48 báo cáo còn lại chưa mở) |
| 3 | Lưu, yêu thích | Vào Favorites, Saved |
| 4 | Export CSV, Print | Export Visible Columns, Export All Columns (`Xem`) |

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
| 2 | Gõ câu hỏi | Khoảng 40 đến 50 giây sau trả câu trả lời và bảng |
| 3 | Show work, chọn data model | Xem cách làm; lưu My Conversations |

**Nhánh:** 2a Số sai so với dữ liệu thật, không báo lỗi (E-012); `Chạy` 2/2 câu.

## UC-manage-contact — Quản lý liên hệ

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Tạo liên hệ, nhập First Name | Không cần email |
| 2 | Tick Operator, Employee, Technician | Quyết định gán xe, ghi công |
| 3 | Chọn User Access | No Access mặc định; Enable Access không chạy |
| 4 | Lưu | Có hồ sơ; "This Contact doesn't have user access." |

**Nhánh:** 1a Trùng tên: vẫn lưu, không cảnh báo. 2a Chưa tick Operator mà gán xe: bị chặn (E-006).

## UC-add-vehicle — Thêm xe trong hạn mức

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Mở New Vehicle | Form 6 phần, trường ở Mục 19 của spec |
| 2 | Nhập, bấm Save Vehicle | Kiểm trường bắt buộc, kiểm hạn mức |
| 3 | Xe được tạo | Chưa kiểm, tài khoản đã 5 of 5 |

**Nhánh:** 2a Thiếu tên: E-004. 2b Hết hạn mức: E-003, kể cả khi đủ tên.
