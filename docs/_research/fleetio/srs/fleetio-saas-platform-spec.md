---
type: research
feature: fleetio-saas-platform
status: draft
updated: 2026-11-03
links:
  - docs/_research/fleetio/fleetio-saas-platform.md
  - docs/_research/fleetio/run-notes/platform.md
  - docs/_product/saas-core-vs-tenant.md
  - docs/_product/tenant-parameters.md
---

# Nền tảng SaaS và thao tác chung — SRS phân tích ngược từ Fleetio

> Mô tả **Fleetio đang làm gì**, kèm đề xuất cho Invlogis. Phần có ích sớm nhất vì không phụ thuộc Gói Bảo dưỡng đội xe. Chưa phải yêu cầu đã chốt. Bản này cập nhật theo lượt chạy thật ngày 03/11/2026; khi mâu thuẫn với bản 02/11, kết quả chạy được ưu tiên.

**Nhãn bằng chứng:** `Chạy` đã thao tác · `Xem` thấy trên giao diện, mở màn nhưng không lưu · `Docs` tài liệu công khai · `Suy` suy ra · `GĐ` giả định. Số chính sách của Fleetio ghi "Fleetio: x". Tham số Invlogis nếu cần ghi "tham số mới, chưa có mã".

## 1. Scope

**Trong phạm vi:** cấu hình theo khách, quyền, tự động hoá, trang đầu, danh sách chuẩn, báo cáo, dữ liệu mẫu, thông báo, tài liệu, bản ghi tự tạo, tích hợp, sandbox, liên hệ và người dùng, nhóm xe, hạn mức gói, hỏi dữ liệu bằng lời.

**Ngoài phạm vi:** thanh toán gói, Advanced Analytics ngoài AI Data Analyst (user không chọn). Custom Records, Tools chỉ theo tài liệu.

**Giới hạn của lượt chạy:** tài khoản dùng thử đã hết hạn mức xe nên nhóm này không có xe riêng; không mời người, không đổi Settings, không dùng bản ghi Sample để đổi trạng thái. Chi tiết việc chưa chạy ở Mục 13.9 và Mục 12.

## 2. Actors & Stakeholders

| Actor | Loại | Mục tiêu | Trong scope? | Tương đương Invlogis |
|---|---|---|---|---|
| Account Owner | Người | Sở hữu tài khoản | Có | Admin của khách |
| Administrator | Người | Cấu hình, phân quyền | Có | Admin của khách |
| Người dùng theo Role | Người | Làm việc trong phạm vi quyền | Có | Nhân viên nội bộ |
| Liên hệ không truy cập | Người | Có hồ sơ để gán xe, ghi công, không đăng nhập | Có | Lái xe, thợ chưa có tài khoản |
| Người nhận link chia sẻ báo cáo | Người ngoài | Xem báo cáo qua link, không cần đăng nhập | Có | Chưa có |
| Fleetio Automation | Hệ thống | Tác giả các comment do automation tạo | Có | Chưa có |
| Đội sản phẩm | Người | Không phải sửa lõi cho từng khách | Có | innvie |
| Hệ thống ngoài | Ngoài | API, Webhook, SAML, MCP, FTP, SFTP, Amazon S3, ThoughtSpot, NHTSA | Có | EUP, ngân hàng, hải quan |

## 3. Functional Requirements (FR)

| ID | Title | Description | Priority | Tầng | Verify by | Source | Mức thực tế | Đề xuất Invlogis |
|---|---|---|---|---|---|---|---|---|
| FR-fleetio-saas-platform-001 | Thiết lập chung | Khách chọn tiền tệ, định dạng ngày, múi giờ, 12 hay 24 giờ, đơn vị số đo, nhiên liệu, hệ đo, gọi Vehicle hay Asset, thuế. Là mặc định cho xe mới; đổi tên gọi thì đổi toàn hệ thống. | P0 | [Lõi] [Cấu hình] | demo | `Xem` | `Xem` đủ trang, không Save | Lấy cho OQ-7 của PRD; Vehicle hay Asset ứng với từ điển thuật ngữ theo khách |
| FR-fleetio-saas-platform-002 | Luật bật tắt có giải thích | Mỗi luật có ô tick, câu mô tả tác động, phạm vi; loại trừ theo loại xe (Require a Meter Reading kèm Excluded Vehicle Types). | P0 | [Cấu hình] | demo | `Xem`, `Docs` 17 cài đặt Maintenance | `Xem` 3.800/3.965 ký tự trang | Lấy cách trình bày; mẫu cho loại xe không đồng hồ như mooc |
| FR-fleetio-saas-platform-003 | Danh mục theo khách | Trạng thái, loại, mã, lý do, đơn vị do khách sửa; có mục khoá của hệ thống, có bí danh, tắt được từng mục (Issue Priorities). Số mục ở Mục 14. | P0 | [Cấu hình] | demo | `Xem` | `Xem` | Lấy |
| FR-fleetio-saas-platform-004 | Tắt cả module | Ví dụ Enable Work Orders; tắt thì ẩn Work Orders, Parts. General Settings còn bật tắt Jobs, Motor Pool, Smart Uploads (Fuel Entry, Service Entry, Inspection Form). Đề xuất: khách chỉ tắt trong phạm vi đã mua. | P0 | [Lõi] | test | `Xem` | `Xem`, chưa tắt thử | Lấy cho bật gói |
| FR-fleetio-saas-platform-005 | Role | Bốn vai có sẵn: Fleet Manager, Operator, Technician, Viewer; 30 module, mỗi module mức đủ, một phần, không; thêm vai mới; khoá vai mặc định. Ma trận ở Mục 15. | P0 | [Lõi] [Cấu hình] | demo | `Xem` mở Edit Role cả 4 vai, bấm Cancel | `Xem`, chưa kiểm hiệu lực thật | Đối chiếu `access-control` |
| FR-fleetio-saas-platform-006 | Record Set | Phạm vi dữ liệu theo Vehicles, Contacts, Part Locations, Inspection Forms; mẫu Assigned Only, Full, No Access, Group Only, View Only; quyền Manage và View riêng. Bảng ở Mục 16. | P0 | [Lõi] [Cấu hình] | test | `Xem`, `Docs` | `Xem`, chưa kiểm hiệu lực thật | Rất đáng lấy; "theo xe được gán" hợp lái xe đầu kéo; thêm phạm vi Chi nhánh |
| FR-fleetio-saas-platform-007 | Điều kiện theo trường tuỳ chỉnh | Record Set lọc được theo trường tuỳ chỉnh dạng chọn, tick. | P2 | [Cấu hình] | test | `Docs`; `Xem` có điều kiện "Vehicles with specific custom field values" | `Docs`, `Xem` tên điều kiện | Cân nhắc |
| FR-fleetio-saas-platform-008 | Trang đầu Needs Attention | Thẻ đếm dẫn tới danh sách đã lọc (đích từng thẻ ở Mục 13.6); "ROs Needing Approval" không có đích khi rỗng; mỗi thẻ tải riêng; lọc theo nhóm; tuỳ biến, nhiều dashboard; phía dưới có Cost, Inspections, Recent Activity. | P0 | [Lõi] [Cấu hình] | demo | `Chạy` | `Chạy` | Lấy cho `common-workspace` |
| FR-fleetio-saas-platform-009 | Danh sách chuẩn | Tab đếm số, lọc nhanh, Filters có nhóm điều kiện, sắp xếp, nhóm dòng, chọn cột, phân trang, chọn nhiều. | P0 | [Lõi] | demo | `Xem` | `Xem` | Lấy |
| FR-fleetio-saas-platform-010 | Chế độ xem đã lưu | Add Tab, Save View, Save Changes; My Saved Views, Saved Views dùng chung. | P1 | [Lõi] | demo | `Xem` | `Xem` | Lấy |
| FR-fleetio-saas-platform-011 | Xem nhanh bản ghi | Record peek mở ngay trên danh sách. | P1 | [Lõi] | demo | `Xem` nút đóng | `Xem` | Lấy nếu rẻ |
| FR-fleetio-saas-platform-012 | Tự động hoá | Trigger gồm loại bản ghi và kiểu sự kiện; điều kiện tuỳ chọn; hành động Update Field, Add Comment, Send Email, Create Record; có bật tắt, phiên bản, đếm lần chạy. Đã tạo, bật, chạy, tắt, Archive, Restore. | P1 | [Cấu hình] | demo | `Chạy`, `Docs` | `Chạy` Add Comment, Update Field, Create Record; Send Email chưa chạy | Làm sau; trước mắt dùng luật có tham số |
| FR-fleetio-saas-platform-013 | Loại bản ghi tự động hoá | Work Order, Service Entry, Fault, Issue, Purchase Order, Geofence Event, Vehicle. Kiểu sự kiện gồm Created, Updated, Created or Updated, Deleted. Bản ghi hành động chọn được với Issue: Issue, Vehicle, Work Order. | P1 | [Cấu hình] | demo | `Xem` | `Chạy` Issue; còn lại `Xem` | Tham khảo |
| FR-fleetio-saas-platform-014 | Mẫu tự động hoá | 18 mẫu: Faults 2, Issues 5, Purchase Orders 3, Service Entries 2, Work Orders 6; gợi ý đúng lúc ngay sau hành động liên quan. Bảng từng mẫu ở Mục 17. | P1 | [Cấu hình] | demo | `Chạy` Apply từng mẫu, không lưu | `Chạy` 17/18 mẫu đọc đủ | Lấy gợi ý đúng lúc; lấy mẫu "WO xong và xe không còn WO mở thì xe về Active" |
| FR-fleetio-saas-platform-015 | Khởi tạo khách | Dữ liệu mẫu có nhãn Sample, tắt được; Sample không tính vào hạn mức; Onboarding Tasks trỏ 7 đường dẫn; danh sách Get Started, mẫu số đổi giữa các trang (3/5 và 3/6). | P0 | [Lõi] | demo | `Chạy` bộ đếm đổi | `Chạy` | Lấy; dữ liệu mẫu không lấy từ khách thật; bộ đếm phải nhất quán |
| FR-fleetio-saas-platform-016 | Hướng dẫn tại chỗ | Khung Learn có mô tả, ảnh, More Info, Academy; đóng được. | P1 | [Lõi] | demo | `Chạy` | `Chạy` | Lấy cho `help-center` |
| FR-fleetio-saas-platform-017 | Theo dõi, bình luận | Watch; người tạo tự theo dõi; bình luận, nhắc tên; cột phải trên trang chi tiết. Automation bình luận với tác giả "Fleetio Automation". | P1 | [Lõi] | demo | `Chạy` tự theo dõi, comment do automation | `Chạy` một phần | Lấy |
| FR-fleetio-saas-platform-018 | Thông báo | Hồ sơ thông báo gán cho người (gán bulk từ Contacts), nhóm xe theo dõi có cột Direct Watchers, Total Watchers, cài đặt cá nhân; hộp Inbox, Archived, All Activity, Comments, Mentions. | P1 | [Cấu hình] | demo | `Xem` | `Xem`, tài khoản có 0 hồ sơ | Lấy |
| FR-fleetio-saas-platform-019 | Báo cáo chuẩn | 49 báo cáo 13 nhóm; yêu thích, lưu, chia sẻ; dạng lưới, danh sách; nhãn "Upgrading soon" trên 4 báo cáo. Bảng nhóm ở Mục 18. | P1 | [Gói: Bảo dưỡng đội xe] | demo | `Xem` | `Xem` tên, `Chạy` mở sâu 1 báo cáo | Chọn khoảng 10 |
| FR-fleetio-saas-platform-020 | Hỏi dữ liệu | Nút Ask a data question trên đầu trang mở AI Data Analyst, khung nhúng từ ThoughtSpot; hỏi bằng lời ra bảng; Show work, chọn All data models, lưu My Conversations. Đã thử 2 câu, cả 2 sai số so với trang xe. | P2 | [Lõi] | demo | `Chạy` 2 câu | `Chạy` | Cân nhắc; nếu làm phải ghi "dữ liệu đến thời điểm" |
| FR-fleetio-saas-platform-021 | Tìm toàn cục | Tìm theo 15 loại bản ghi. | P1 | [Lõi] | demo | `Xem` | `Xem` | Lấy |
| FR-fleetio-saas-platform-022 | Lịch sử bản ghi | View Record History; lịch sử từng trường. Có trên xe và automation. | P0 | [Lõi] | demo | `Xem` | `Xem` đọc nút | Lấy |
| FR-fleetio-saas-platform-023 | Giới hạn theo gói | Hiện đã dùng trên giới hạn: tài liệu, vai, xe, tự động hoá, bản ghi tự tạo (Fleetio: 250.0 GB, 30, 5, 75, 25). Hết hạn mức thì chặn tạo và khoá nút; danh sách xe hiện "5 of 5". Giá trị theo hợp đồng, khách không tự nâng. | P1 | [Lõi] | demo | `Chạy` bị chặn thật | `Chạy` với xe; còn lại `Xem` | Lấy khi bán gói |
| FR-fleetio-saas-platform-024 | Kho tài liệu | Danh sách file, thư mục, biết gắn bản ghi nào; tab All Documents và tab tên tài khoản; cột File Name, File Size, Location, Auto-Delete, Attached To, Labels; lọc Document File Type, Document Location Type. | P2 | [Cấu hình] | demo | `Xem` khung rỗng | `Xem`, không tải tệp | Cân nhắc |
| FR-fleetio-saas-platform-025 | Bản ghi tự tạo | Khai loại, trường, liên kết, bố cục kéo thả; trang danh sách, chi tiết; hiện theo tab trên bản ghi liên kết. | P2 | [Gói: Khách lớn, chưa có trong danh sách gói] | demo | `Docs`, không mở | `Docs` | Để sau |
| FR-fleetio-saas-platform-026 | Trường tuỳ chỉnh | Nhãn duy nhất theo loại; không đổi kiểu sau khi lưu; xoá thì mất ở mọi bản ghi. Standard Records liệt kê 15 loại bản ghi có trường tuỳ chỉnh, đều 0. | P1 | [Cấu hình] | test | `Docs`, `Xem` Standard Records | `Docs`, `Xem` | Lấy |
| FR-fleetio-saas-platform-027 | Webhook | Chọn một sự kiện mỗi webhook; hơn 50 sự kiện; ký xác thực; thất bại 3 lần liên tiếp thì tắt. Màn ghi "send a HTTP POST" dạng JSON. | P2 | [Gói: Khách lớn, chưa có trong danh sách gói] | test | `Xem`, `Docs` | `Xem` rỗng, không tạo | Để sau |
| FR-fleetio-saas-platform-028 | API, SAML, MCP | API key, đăng nhập SAML (có Metadata), máy chủ MCP: "Each connection respects the user's role permissions." Module Fleetio MCP mức không có ở cả 4 vai mặc định. | P2 | [Gói: Khách lớn, chưa có trong danh sách gói] | demo | `Xem` | `Xem`, không bật | Để sau |
| FR-fleetio-saas-platform-029 | Sandbox, xuất dữ liệu | Môi trường thử: Sample Copy, Production Copy có hạn mức riêng. Export Account Data: 13 loại dữ liệu, CSV hoặc XLS, gửi qua email, link hết hạn (Fleetio: 7 ngày). | P2 | [Gói: Khách lớn, chưa có trong danh sách gói] | demo | `Xem` | `Xem`, không bấm | Để sau |
| FR-fleetio-saas-platform-030 | Danh sách tự động hoá | Cột Name, Status, Trigger Record, Total Runs, Successful Runs, Failed Runs, Created By, Last Run At, Current Version; tab All, Archived; lọc Created By, Trigger Record, Status, Filters. | P1 | [Cấu hình] | demo | `Chạy`, ảnh `automation-list-data.jpg` | `Chạy` | Lấy cột đếm lượt |
| FR-fleetio-saas-platform-031 | Thư viện mẫu | Browse Templates: cột trái theo loại trigger, thẻ có sơ đồ trigger, số điều kiện, số hành động, nút Apply khi rê chuột. Apply mở trình dựng đã điền sẵn, chưa lưu gì. | P1 | [Cấu hình] | demo | `Chạy`, ảnh `automation-templates.jpg` | `Chạy` | Lấy |
| FR-fleetio-saas-platform-032 | Bật tắt có xác nhận và phiên bản | Lưu xong ở trạng thái tắt; bật phải qua hộp xác nhận và lúc đó sinh phiên bản v.1, ghi Enabled At; tắt cũng có hộp xác nhận. | P1 | [Cấu hình] | test | `Chạy` | `Chạy`; sửa khi đang bật để sinh v.2 chưa chạy | Lấy: khách thử an toàn |
| FR-fleetio-saas-platform-033 | Archive và Restore automation | Archive không cần tắt trước, tắt ngay, ghi Disabled At; bản Archived chỉ đọc; Restore về Disabled, không tự bật. Nút Delete, Make a Copy, View Record History có trong menu. | P1 | [Cấu hình] | test | `Chạy` Archive, Restore; `Xem` các nút còn lại | `Chạy` một phần | Lấy |
| FR-fleetio-saas-platform-034 | Run History và Run Result | Mỗi lượt có kết quả, phiên bản, bản ghi kích hoạt, Triggered By, log JSON. | P1 | [Cấu hình] | test | `Chạy`, ảnh `automation-run-history.jpg`, `automation-run-result.jpg` | `Chạy`; chỉ thấy SUCCESS | Lấy; sửa "Triggered By" và "No records changed" (xem BR-012, BR-013) |
| FR-fleetio-saas-platform-035 | Trình dựng điều kiện | Với Issue: 59 trường, chia nhóm Issue, Tool, Vehicle, Vehicle or Tool; All of, Any of; nhóm điều kiện lồng. So khớp không phân biệt hoa thường. | P1 | [Cấu hình] | test | `Chạy` điều kiện contains; `Xem` phần còn lại | `Chạy` một phần | Tham khảo |
| FR-fleetio-saas-platform-036 | Hành động Create Record | Tạo Work Order từ Issue; chỉ có Status, Assigned To, Service Tasks; Status chỉ cho Open và Pending; WO sinh ra liên kết Issue ở cột Resolved Issues. | P1 | [Cấu hình] | test | `Chạy` | `Chạy` | Lấy: tránh bỏ qua kiểm tra km khi hoàn tất |
| FR-fleetio-saas-platform-037 | Thông báo của automation | Ô Failure Notification Email, Run Summary Email. | P2 | [Cấu hình] | demo | `Xem`, không bật vì gửi email | `Xem` | Lấy |
| FR-fleetio-saas-platform-038 | Liên hệ một bảng | Một bảng Contact, phân vai bằng tick Operator, Employee, Technician; User Access: Enable Access to Fleetio hoặc No Access (mặc định). Người dùng là liên hệ được bật truy cập. Không email vẫn lưu được; không chặn trùng tên. | P0 | [Lõi] | test | `Chạy`, ảnh `contact-no-access.jpg` | `Chạy` No Access; `Xem` Enable Access, không mời người | Lấy; thêm cảnh báo trùng người |
| FR-fleetio-saas-platform-039 | Form xe sáu phần | Details, Maintenance, Lifecycle, Financial, Specifications, Settings; trường ở Mục 19. Out-of-Service chỉ là trường ngày và số km, không có nút thanh lý. | P1 | [Lõi] [Cấu hình] | demo | `Xem` đọc đủ form, không lưu được | `Xem` | Đối chiếu nhóm Phương tiện |
| FR-fleetio-saas-platform-040 | Nhóm nhiều cấp | Groups & Subgroups dạng cây; Require Group chỉ mở khi mọi tài sản và liên hệ đã có nhóm, màn liệt kê số còn thiếu; Export Data. | P0 | [Lõi] [Cấu hình] | test | `Xem` | `Xem`, không đổi | Lấy làm khung Công ty, Chi nhánh, Cơ sở |
| FR-fleetio-saas-platform-041 | Trạng thái xe theo danh mục | Active (Default), In Shop, Inactive, Out of Service, Sold có đếm xe, Add Vehicle Status; không thấy luật chuyển; có lịch sử trạng thái, báo cáo Status Changes, Status Summary. | P1 | [Lõi] [Cấu hình] | test | `Xem` | `Xem`, chưa đổi thật | Đối chiếu nhóm Phương tiện |
| FR-fleetio-saas-platform-042 | Recall | Danh sách từ NHTSA theo năm, hãng, đời; tab All, Needs Action, Open, Resolved, Acknowledged; cột Issued At, Status, Issue, Manufacturer Campaign Number, NHTSA Campaign Number. Một mẫu tự nâng Critical khi nguồn là Recall. | P2 | [Gói: Bảo dưỡng đội xe] | demo | `Xem`, ảnh `recalls-list.jpg` | `Xem` 261 dòng Sample, không đổi trạng thái | Nguồn thu hồi của Việt Nam chưa biết; để sau |
| FR-fleetio-saas-platform-043 | Motor Pool | Đặt xe dùng chung: cột Motor Pool, Number, Operator, Vehicle Types, Vehicle, Pick Up, Drop Off, Status; Settings có Motor Pools, Reservation Rates, Flat Fees; quyền check_out, return, cancel. | P2 | [Gói: Khách lớn, chưa có trong danh sách gói] | demo | `Xem`, ảnh `motor-pool-reservations.jpg` | `Xem` rỗng; chưa chạy | Để sau |
| FR-fleetio-saas-platform-044 | Quyền con theo module | Vehicles có create, edit, view_all, view_details, view_financial_info, view_custom_fields, export_data, update_status, manage_vehicle_assignment, archive_delete, view_documents, manage_documents, manage_photos. Work Orders, Purchase Orders, Motor Pool có quyền con ở Mục 15. | P0 | [Lõi] | test | `Xem` | `Xem` | Lấy cách tách xem tài chính, duyệt, nhận hàng |
| FR-fleetio-saas-platform-045 | Cảnh báo chi phí tại quyền | Ngay tại quyền Create của Vehicles: "Adding new Vehicles will result in additional charges to your account's subscription." | P2 | [Lõi] | demo | `Xem` | `Xem` | Lấy nếu tính tiền theo xe |
| FR-fleetio-saas-platform-046 | Điều kiện Record Set tự tạo | Vehicles có 8 điều kiện: All vehicles, Vehicles in this contact's group, Vehicles assigned to this contact, Specific vehicles, Vehicles in specific groups, Vehicles with specific status(es), Vehicles with specific custom field values, No vehicles. Manage và View khai riêng. | P0 | [Lõi] [Cấu hình] | test | `Xem`, ảnh `record-set-conditions.jpg` | `Xem`, không lưu | Lấy; thiếu điều kiện theo thời gian |
| FR-fleetio-saas-platform-047 | Chính sách bảo mật | Minimum Length, Expiration, yêu cầu ký tự, Maximum invalid login attempts, Lockout, Reset All Passwords; giá trị ở Mục 14. | P1 | [Lõi] [Cấu hình] | test | `Xem`, không bấm | `Xem` | Đối chiếu `account-access` |
| FR-fleetio-saas-platform-048 | AI Service Advisor | Issue Prioritization, Issue Resolution, Fault Monitoring, Service Assessments, Service Writer, mỗi cái có Manage, có câu điều khoản. | P2 | [Cấu hình] | demo | `Xem`, không bấm | `Xem` | Đối chiếu NFR-006 |
| FR-fleetio-saas-platform-049 | Kết nối ra ngoài | Integration Links (link sang hệ khác kèm biến), External Connections (FTP, SFTP, Amazon S3 cho báo cáo định kỳ). | P2 | [Gói: Khách lớn, chưa có trong danh sách gói] | demo | `Xem` rỗng | `Xem`, không tạo | Để sau |
| FR-fleetio-saas-platform-050 | Khung trạng thái theo khách | Work Order: Type cố định Incomplete, Completed; khách thêm tên. Purchase Order: 8 trạng thái cố định, không có Add. | P0 | [Lõi] [Cấu hình] | test | `Xem` | `Xem` | Khớp "Lõi khung trạng thái + Cấu hình nhãn" |
| FR-fleetio-saas-platform-051 | Trang báo cáo | Issues Report: biểu đồ Summary, Top Vehicles; Filters, Columns, phân trang; Save, Share, Export CSV (Export Visible Columns, Export All Columns), Print. | P1 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy`, ảnh `report-issues.jpg` | `Chạy` 1/49 báo cáo | Lấy khung cho `workshop-reports` |
| FR-fleetio-saas-platform-052 | Chia sẻ báo cáo bằng link | Bấm Share sinh ngay link công khai, có hạn (Fleetio: 7 ngày); "this link allows anyone with access to view all data". Reports › Shared liệt kê link và cho Unshare. | P2 | [Cấu hình] | test | `Chạy`, link đã thu hồi | `Chạy` | Học hạn và danh sách thu hồi; KHÔNG học sinh link ngay. Phải bấm tạo mới có link, ghi nhật ký |
| FR-fleetio-saas-platform-053 | Mức ưu tiên tự động của Issue | Issue mới có Priority "Auto-assign"; #40, #42 tự thành High dù không nhập mức. | P2 | [Cấu hình] | test | `Chạy` phần thấy được; nguyên nhân AI Issue Prioritization là `Suy` | `Chạy` | Đối chiếu NFR-006; phải ghi nguồn gán |

## 4. Non-Functional Requirements (NFR)

| ID | Category | Requirement | Priority | Acceptance |
|---|---|---|---|---|
| NFR-fleetio-saas-platform-001 | phân quyền | Không thao tác hàng loạt nếu thiếu quyền Manage trên Record Set. | P0 | `Docs` |
| NFR-fleetio-saas-platform-002 | hiệu năng trang đầu | Mỗi thẻ tải độc lập, thẻ chậm không chặn thẻ khác. | P1 | `Chạy` API `async_stats/*_job`, có "0 minutes ago", Refresh |
| NFR-fleetio-saas-platform-003 | múi giờ | Cảnh báo khi múi giờ thiết bị khác tài khoản. | P1 | `Xem` |
| NFR-fleetio-saas-platform-004 | chống làm phiền | Thông báo nền không che màn. | P2 | Fleetio không đạt: toast lặp lại |
| NFR-fleetio-saas-platform-005 | cách ly dữ liệu giữa khách | Đề xuất Invlogis: mọi đọc, ghi, tìm kiếm, báo cáo, xuất, tác vụ nền, thông báo chỉ chạm dữ liệu của đúng một khách; dữ liệu từng khách tách riêng theo PRD. Fleetio không công bố cách làm. | P0 | Ca kiểm thử hai khách, 100% đạt |
| NFR-fleetio-saas-platform-006 | dữ liệu gửi cho AI | Đề xuất Invlogis: có cờ bật tắt từng tính năng; khai rõ trường được gửi, thời gian lưu; không huấn luyện chéo giữa khách; AI chỉ thấy dữ liệu người gọi được thấy; AI lỗi thì làm tay được. Đối chiếu việc 2 ở `saas-core-vs-tenant.md`. | P0 | TBD — đội sản phẩm — trước khi bật AI |
| NFR-fleetio-saas-platform-007 | đường đọc gộp | Đề xuất Invlogis: số đếm, tìm kiếm, báo cáo, in, xuất, thông báo áp cùng phạm vi quyền của người xem. | P0 | Ca kiểm thử theo vai |
| NFR-fleetio-saas-platform-008 | giới hạn vòng lặp tự động hoá | Đề xuất Invlogis: đặt trần lượt chạy theo khách (tham số mới, chưa có mã). Fleetio không nêu giới hạn; lượt chạy chỉ thấy dừng khi giá trị không đổi. | P1 | Ca hai automation lật giá trị phải dừng ở trần |
| NFR-fleetio-saas-platform-009 | truy vết nguồn gây ra | Đề xuất Invlogis: lượt do automation gây ra phải ghi automation là nguồn, không ghi người thật; kết quả phải phản ánh cả comment đã thêm. Fleetio không đạt. | P1 | Đọc lịch sử phân biệt được người và máy |
| NFR-fleetio-saas-platform-010 | chia sẻ ra ngoài | Đề xuất Invlogis: mở hộp không sinh link; có bước tạo chủ động, nói rõ phạm vi dữ liệu; thu hồi có hiệu lực ngay ở mọi lối; ghi nhật ký tạo, mở, thu hồi. Fleetio không đạt. | P0 | Mở hộp rồi đóng không tồn tại link nào; thu hồi xong mở lại không còn dữ liệu |
| NFR-fleetio-saas-platform-011 | độ tin của câu trả lời AI | Đề xuất Invlogis: mọi số do AI trả phải ghi "dữ liệu đến thời điểm" và lối đối chiếu về bản ghi gốc. Fleetio không đạt: khẳng định "currently" với số lệch. | P0 | Câu trả lời số luôn có thời điểm dữ liệu |

## 5. Business Rules

| ID | Rule | Tầng | Trigger | Implements FR | Source | Mức thực tế |
|---|---|---|---|---|---|---|
| BR-fleetio-saas-platform-001 | Quyền hiệu lực là giao của Role và Record Set. | [Lõi] | Thao tác | FR-fleetio-saas-platform-006 | `Suy` từ `Docs` | `Suy`, chưa kiểm được vì không mời người |
| BR-fleetio-saas-platform-002 | Chỉ trường dạng chọn, tick dùng làm điều kiện Record Set. | [Cấu hình] | Khai Record Set | FR-fleetio-saas-platform-007 | `Docs` | `Docs` |
| BR-fleetio-saas-platform-003 | Luật mới thường chỉ áp cho bản ghi về sau: "This requirement only applies to future Work Orders or Service Entries." | [Cấu hình] | Bật luật | FR-fleetio-saas-platform-002 | `Docs`, `Xem` câu trên màn | `Xem` |
| BR-fleetio-saas-platform-004 | Mỗi webhook một sự kiện; 3 lần lỗi liên tiếp thì tắt. | [Gói: Khách lớn, chưa có trong danh sách gói] | Gửi webhook | FR-fleetio-saas-platform-027 | `Docs` | `Docs` |
| BR-fleetio-saas-platform-005 | Tính năng có phân gói: tạo trạng thái lệnh, kiểm dòng, Custom Records chỉ ở Premium. | [Gói: Khách lớn, chưa có trong danh sách gói] | Dùng tính năng | FR-fleetio-saas-platform-023 | `Docs` | `Docs` |
| BR-fleetio-saas-platform-006 | Tên bản ghi tự động hoá sinh theo thời điểm; chỉ lưu khi đủ trigger, hành động. | [Cấu hình] | Tạo Automation | FR-fleetio-saas-platform-012 | `Chạy`, không để lại bản rác | `Chạy` |
| BR-fleetio-saas-platform-007 | Automation mới lưu ở trạng thái tắt; khi tắt không chạy. | [Cấu hình] | Lưu | FR-fleetio-saas-platform-032 | `Chạy` Issue #40 không có comment | `Chạy` |
| BR-fleetio-saas-platform-008 | Bật automation không chạy bù cho bản ghi đã có. | [Cấu hình] | Bật | FR-fleetio-saas-platform-032 | `Chạy` #40 vẫn không có comment | `Chạy` |
| BR-fleetio-saas-platform-009 | Lượt không khớp điều kiện không được đếm. | [Cấu hình] | Sự kiện | FR-fleetio-saas-platform-034 | `Chạy` Total Runs vẫn 1 | `Chạy` |
| BR-fleetio-saas-platform-010 | Nhiều automation cùng sự kiện đều chạy. | [Cấu hình] | Sự kiện | FR-fleetio-saas-platform-012 | `Chạy` #43; thứ tự chạy chưa biết | `Chạy` |
| BR-fleetio-saas-platform-011 | Automation tự kích hoạt lại khi chính nó đổi bản ghi, rồi dừng khi giá trị không đổi. | [Cấu hình] | Created or Updated | FR-fleetio-saas-platform-034 | `Chạy` 2 lượt; giới hạn vòng lặp chéo chưa biết | `Chạy` |
| BR-fleetio-saas-platform-012 | "Triggered By" ghi người tạo bản ghi, kể cả lượt do automation gây ra. | [Cấu hình] | Ghi lượt chạy | FR-fleetio-saas-platform-034 | `Chạy`, ảnh `automation-self-trigger-runs.jpg` | `Chạy` |
| BR-fleetio-saas-platform-013 | Lượt chỉ thêm comment ghi "Records: No records changed". | [Cấu hình] | Ghi lượt chạy | FR-fleetio-saas-platform-034 | `Chạy`, ảnh `automation-run-result.jpg` | `Chạy` |
| BR-fleetio-saas-platform-014 | Hành động tạo Work Order không có Status Completed. | [Cấu hình] | Create Record | FR-fleetio-saas-platform-036 | `Chạy` hộp chỉ có Open, Pending | `Chạy` |
| BR-fleetio-saas-platform-015 | Archive tắt automation ngay, không cần tắt trước. Restore về Disabled, không tự bật. Bản Archived chỉ đọc. | [Cấu hình] | Archive, Restore | FR-fleetio-saas-platform-033 | `Chạy` | `Chạy` |
| BR-fleetio-saas-platform-016 | Hết hạn mức xe thì không tạo được, kể cả khi đủ trường bắt buộc; bản ghi Sample không tính vào hạn mức. | [Lõi] [Cấu hình] | Lưu xe | FR-fleetio-saas-platform-023 | `Chạy` | `Chạy` |
| BR-fleetio-saas-platform-017 | Chỉ liên hệ có tick Operator mới gán được xe; chỉ Technician mới được chọn ở dòng công lệnh sửa. | [Lõi] | Gán xe, ghi công | FR-fleetio-saas-platform-038 | `Chạy` khối gán xe chặn; Technician theo câu trên màn là `Xem` | `Chạy` Operator, `Xem` Technician |
| BR-fleetio-saas-platform-018 | Liên hệ chỉ cần First Name; trùng tên vẫn lưu, không cảnh báo. No Access thì không vào hệ thống, không nhận thông báo. | [Lõi] | Lưu liên hệ | FR-fleetio-saas-platform-038 | `Chạy` | `Chạy` |
| BR-fleetio-saas-platform-019 | Record Type của Record Set không đổi sau khi tạo; bản mặc định bị khoá sửa. | [Lõi] | Sửa Record Set | FR-fleetio-saas-platform-046 | `Xem` | `Xem` |
| BR-fleetio-saas-platform-020 | Record Set không có điều kiện theo thời gian (ca trực, thời hạn). | [Lõi] | Khai Record Set | FR-fleetio-saas-platform-046 | `Xem` danh sách 8 điều kiện | `Xem` |
| BR-fleetio-saas-platform-021 | Require Group chỉ mở khi mọi tài sản và liên hệ đã gán nhóm. | [Cấu hình] | Bật Require Group | FR-fleetio-saas-platform-040 | `Xem` khoá, liệt kê số thiếu | `Xem` |
| BR-fleetio-saas-platform-022 | Trạng thái xe đổi tự do bằng trường Status hoặc automation, không có luật chuyển; cần quyền `vehicles_update_status`. | [Lõi] [Cấu hình] | Đổi trạng thái | FR-fleetio-saas-platform-041 | `Xem` | `Xem` |
| BR-fleetio-saas-platform-023 | Work Order về Type Completed thì cập nhật nhắc bảo dưỡng và giải quyết Issue liên quan. | [Lõi] | Hoàn tất lệnh | FR-fleetio-saas-platform-050 | `Xem` câu trên màn; hành vi thật xem nhóm Sửa chữa | `Xem` |
| BR-fleetio-saas-platform-024 | Trạng thái Purchase Order cố định, khách không thêm. | [Lõi] | Cấu hình | FR-fleetio-saas-platform-050 | `Xem` không có nút Add | `Xem` |
| BR-fleetio-saas-platform-025 | Chính sách mật khẩu áp khi tạo hoặc đặt lại mật khẩu, không áp SAML. | [Lõi] [Cấu hình] | Đổi mật khẩu | FR-fleetio-saas-platform-047 | `Xem` | `Xem` |
| BR-fleetio-saas-platform-026 | Bản xuất toàn bộ gửi qua email; link hết hạn (Fleetio: 7 ngày). | [Gói: Khách lớn, chưa có trong danh sách gói] | Export Account Data | FR-fleetio-saas-platform-029 | `Xem` câu trên màn | `Xem` |
| BR-fleetio-saas-platform-027 | Mở hộp Share là sinh link công khai, không hỏi trước; ai có link xem được dữ liệu; hết hạn (Fleetio: 7 ngày). | [Cấu hình] | Bấm Share | FR-fleetio-saas-platform-052 | `Chạy` | `Chạy`; hết hạn thật chưa chờ |
| BR-fleetio-saas-platform-028 | Chỉ Unshare ở Reports › Shared mới thu hồi được; lối "click here to unshare" trong hộp không có tác dụng. | [Cấu hình] | Thu hồi | FR-fleetio-saas-platform-052 | `Chạy` | `Chạy` |
| BR-fleetio-saas-platform-029 | AI Data Analyst khẳng định số mà không ghi dữ liệu tính đến lúc nào. | [Lõi] | Hỏi dữ liệu | FR-fleetio-saas-platform-020 | `Chạy`; nguyên nhân kho phân tích trễ là `Suy` | `Chạy` |
| BR-fleetio-saas-platform-030 | Cảnh báo Location Exception bật khi phiếu nộp từ một chỗ theo ngưỡng (Fleetio: 80%, 100 m). | [Cấu hình] | Nộp phiếu | FR-fleetio-saas-platform-003 | `Xem` Inspection Settings | `Xem` |
| BR-fleetio-saas-platform-031 | Thiếu giá trị trong mẫu thì trình dựng hiện "Missing Value" hoặc để trống; người dùng phải chọn trước khi lưu. | [Cấu hình] | Apply mẫu | FR-fleetio-saas-platform-031 | `Chạy` hiện; không lưu để kiểm chặn | `Chạy` phần hiện |

## 6. Error Matrix

| Error ID | Title | Trigger | Severity | Related FR | Screen state | Recovery | Mức thực tế |
|---|---|---|---|---|---|---|---|
| E-fleetio-saas-platform-001 | Không có quyền | "You are not authorized to perform this action." | major | FR-fleetio-saas-platform-005 | Toast | Xin quyền; Fleetio dùng lẫn cho form trống | Theo bản 02/11, lượt 03/11 không gặp lại |
| E-fleetio-saas-platform-002 | Không có dữ liệu | "No results to show." kèm hướng dẫn | minor | FR-fleetio-saas-platform-009 | Trạng thái rỗng có nút tạo | Tạo mới, bỏ lọc | `Xem` |
| E-fleetio-saas-platform-003 | Hết hạn mức xe | "Your plan is limited to 5 vehicles" | major | FR-fleetio-saas-platform-023 | Dưới form; danh sách "5 of 5", nút Add Vehicle có khoá | Nâng gói, Explore Plans; không có lối khác đã thử | `Chạy` |
| E-fleetio-saas-platform-004 | Thiếu tên xe | "can't be blank" và toast "Vehicle could not be created" | minor | FR-fleetio-saas-platform-039 | Dưới trường | Nhập tên | `Chạy` |
| E-fleetio-saas-platform-005 | Bản ghi đã Archive | "Archived records are read-only and cannot be updated." | minor | FR-fleetio-saas-platform-033 | Banner, chỉ đọc | Restore | `Chạy` |
| E-fleetio-saas-platform-006 | Liên hệ chưa là Operator | "Contact must have operator classification to be assigned to vehicles" | minor | FR-fleetio-saas-platform-038 | Câu dẫn trong khối xe | Tick Operator | `Chạy` |
| E-fleetio-saas-platform-007 | Chưa bật được Require Group | "all existing assets and contacts must be assigned a group" | minor | FR-fleetio-saas-platform-040 | Ô khoá, liệt kê số thiếu | Gán nhóm cho đủ | `Xem` |
| E-fleetio-saas-platform-008 | Không đổi loại Record Set | "can't be changed after creation" | minor | FR-fleetio-saas-platform-046 | Trường khoá | Tạo Record Set mới | `Xem` |
| E-fleetio-saas-platform-009 | Mẫu thiếu giá trị | "Missing Value" trên mẫu Add Label khi tài khoản chưa có nhãn; mẫu Update Vehicle Status để trống | minor | FR-fleetio-saas-platform-031 | Trong khối Action | Chọn giá trị | `Chạy` phần hiện |
| E-fleetio-saas-platform-010 | Lối thu hồi trong hộp Share hỏng | Bấm "click here to unshare": không có tác dụng, bấm lại trả 404, link vẫn sống | critical | FR-fleetio-saas-platform-052 | Hộp Share | Reports › Shared › Unshare | `Chạy` |
| E-fleetio-saas-platform-011 | Lượt automation thất bại | Chưa tái hiện được; Failed Runs luôn 0 | major | FR-fleetio-saas-platform-034 | Cột Failed Runs, ô Failure Notification Email | Chưa biết | `Xem` |
| E-fleetio-saas-platform-012 | AI trả số sai, không báo lỗi | Trả "currently has 2 open issues" khi thật là 7; "1,700.0" khi thật là 2.999 km | critical | FR-fleetio-saas-platform-020 | Câu trả lời bình thường, không có cảnh báo | Đối chiếu tay trên trang xe; có Show work | `Chạy` |
| E-fleetio-saas-platform-013 | Link công khai sinh ngoài ý muốn | Bấm Share là có link, không có bước xác nhận | critical | FR-fleetio-saas-platform-052 | Hộp Share có sẵn link | Thu hồi ở Reports › Shared | `Chạy` |

## 7. Success Criteria

| ID | Outcome nghiệp vụ | Đo bằng | Mốc đạt |
|---|---|---|---|
| SC-fleetio-saas-platform-01 | Khách thứ hai chạy không sửa lõi | Số yêu cầu phải sửa code | 0 cho luật có tham số |
| SC-fleetio-saas-platform-02 | Người mới tự làm được | Thời gian tới bản ghi đầu tiên | TBD |
| SC-fleetio-saas-platform-03 | Không lộ dữ liệu ngoài phạm vi | Ca kiểm thử Role và Record Set | 100% đạt |

## 8. Data Entities (tóm tắt — chi tiết ở erd.md)

Account, Plan Limit, Contact, User, Group, Role, Role Permission, Record Set, Saved View, Automation, Automation Version, Automation Run, Automation Template, Dashboard, Custom Field, Custom Record Type, Webhook, Report, Report Share Link, AI Conversation, Recall, Motor Pool, Reservation, Document. Xem [[docs/_research/fleetio/srs/fleetio-saas-platform-erd.md|ERD]].

## 9. Flows (tóm tắt — chi tiết ở flows.md)

Xem [[docs/_research/fleetio/srs/fleetio-saas-platform-flows.md|Flows]], [[docs/_research/fleetio/srs/fleetio-saas-platform-states.md|States]], [[docs/_research/fleetio/srs/fleetio-saas-platform-usecases.md|Use case]], [[docs/_research/fleetio/srs/fleetio-saas-platform-userflow.md|User flow]].

## 10. Screens

Ảnh thật và bảng mô tả: [[docs/_research/fleetio/srs/fleetio-saas-platform-screens.md|Màn hình]]. Không áp `CMP`, `GR` vì mô tả sản phẩm của bên khác.

## 11. Constraints, Dependencies & Assumptions

| Giả định | Invalidate nếu sai |
|---|---|
| `GĐ` Role, Record Set của Fleetio chưa đủ cấp Công ty, Chi nhánh, Cơ sở, và chưa có quyền có thời hạn theo việc, ca trực. Lượt chạy thấy (`Xem`): cấp Chi nhánh dùng được qua Group nhiều cấp; Công ty, Cơ sở phải tự xếp thành cây Group; không có điều kiện theo thời gian | Cần thêm một lớp phạm vi |
| `GĐ` Giai đoạn đầu chỉ cần luật có tham số, chưa cần công cụ tự động hoá. Lượt chạy thấy (`Chạy`): mẫu đủ dùng với luật đơn giản, không thấy chống vòng lặp nên công cụ tổng quát có rủi ro | Phải đưa FR-012 lên P0 |

**Ghi chú nhãn:** "Gói: Khách lớn" là tên tạm do người viết đặt, cần chốt khi review.

**Giới hạn bằng chứng về quyền:** ma trận Mục 15, Mục 16 đọc từ màn cấu hình; chưa đăng nhập bằng vai khác nên chưa biết hệ thống có chặn đúng như khai không.

**Nối với `docs/_product/saas-core-vs-tenant.md`:** Vehicle hay Asset ứng với từ điển thuật ngữ theo khách; Work Order Statuses (khung Type cố định, khách thêm tên) khớp đúng "Lõi khung trạng thái + Cấu hình nhãn"; Require Meter + Excluded Vehicle Types là mẫu cho loại xe không đồng hồ như mooc; PO Statuses cố định là ví dụ phần không cho khách đổi.

## 12. Open Questions

* [x] OQ-1: Role và Record Set có khớp Công ty, Chi nhánh, Cơ sở không? Trả lời (`Xem`): khớp Chi nhánh bằng Group nhiều cấp + "Vehicles in this contact's group"; Công ty, Cơ sở phải tự xếp thành cây Group; không có quyền theo thời hạn. Hiệu lực thật chuyển sang OQ-8. — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-2: Có cần công cụ tự động hoá tổng quát giai đoạn đầu không? Thông tin mới (`Chạy`): mẫu đủ dùng với luật đơn giản, không thấy chống vòng lặp nên công cụ tổng quát có rủi ro; đây là quyết định của đội sản phẩm. — Nguồn khách: câu hỏi nội bộ
* [ ] OQ-3: Dữ liệu mẫu cho khách mới lấy từ đâu mà không lộ dữ liệu Delta? — Nguồn khách: câu hỏi nội bộ
* [ ] OQ-4: Tên gói cho API, SAML, sandbox? Thông tin mới (`Xem`): Fleetio tách Sandbox, MCP theo hạn mức gói; tên gói của Invlogis vẫn phải chốt. — Nguồn khách: câu hỏi nội bộ
* [ ] OQ-5: Hai automation lật giá trị của nhau có bị chặn không, giới hạn bao nhiêu lượt? Tài liệu hãng không nêu, chưa chạy. — Nguồn khách: câu hỏi nội bộ
* [ ] OQ-6: Lượt automation thất bại trông thế nào, có thử lại không, Failure Notification Email gửi gì? Không tái hiện được. — Nguồn khách: câu hỏi nội bộ
* [ ] OQ-7: Sửa automation đang bật có sinh v.2 không; Make a Copy, Delete, trigger Vehicle, hành động Update Vehicle Status, Run Summary Email, Send Email chạy ra sao? — Nguồn khách: câu hỏi nội bộ
* [ ] OQ-8: Role và Record Set có chặn đúng như khai không? Cần mời người dùng thử theo từng vai. — Nguồn khách: câu hỏi nội bộ
* [ ] OQ-9: Technician có quyền gì với Fuel Entries? Ma trận ghi "không", ghi chú cùng lượt ghi "chỉ có ô xem". Cần mở lại Edit Role để chốt. — Nguồn khách: câu hỏi nội bộ
* [ ] OQ-10: Settings có bao nhiêu trang? Bản 02/11 ghi khoảng 65, tiêu đề ghi chú chạy ghi khoảng 45, bảng chạy kê 56 tên trang. Mục 14 theo bảng chạy; chưa đếm lại trên menu. — Nguồn khách: câu hỏi nội bộ
* [ ] OQ-11: Cột và lọc của 48 báo cáo còn lại, Saved Reports là gì? Ghi chú chạy chỉ giữ số theo nhóm và 5 tên, chưa giữ 49 tên. — Nguồn khách: câu hỏi nội bộ
* [ ] OQ-12: Đổi trạng thái xe thật, Archive xe, Restore xe, xe trùng tên, Motor Pool chạy thế nào? Cần một chỗ xe (đang 5 of 5). — Nguồn khách: câu hỏi nội bộ
* [ ] OQ-13: AI Data Analyst sai vì kho phân tích trễ hay vì cách đếm? Mới là `Suy`; 1.700 và 2 không rõ lấy từ thời điểm nào. — Nguồn khách: câu hỏi nội bộ
* [ ] OQ-14: Mẫu Send Email When A Work Order Total Exceeds Amount có trigger, điều kiện gì? Chỉ thấy tên, 1 điều kiện, 1 hành động. — Nguồn khách: câu hỏi nội bộ
* [ ] OQ-15: Vì sao Odometer trong Financial của form xe hiện "mi" khi Specifications hiện cm, kg, lít? Chưa rõ. — Nguồn khách: câu hỏi nội bộ

## 13. Ma trận case

### 13.1 Hạn mức, form xe

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| C-01 Lưu xe trống | Hết hạn mức, Vehicle Name trống | "can't be blank" + "Your plan is limited to 5 vehicles" + toast "Vehicle could not be created" | `Chạy` |
| C-02 Lưu xe đủ tên | Hết hạn mức, tên `TEST-NEN-01` | Vẫn "Your plan is limited to 5 vehicles", không tạo xe | `Chạy` |
| C-03 Sample và hạn mức | 25 xe tính cả Sample, 5 xe TEST | Đếm "5 of 5": Sample không tính | `Chạy` |
| C-04 Lách qua Add Multiple, nhập tệp | Có nút Add Multiple Vehicles | KHÔNG thử vì là lách hạn mức gói | Không chạy |
| C-05 Xe trùng tên | Cần chỗ xe | Không chạy được vì hạn mức | Không chạy |
| C-06 Thanh lý xe | Tìm nút thanh lý | KHÔNG có nút; Out-of-Service chỉ là trường ngày và số km | `Xem` |
| C-07 Đơn vị trên form | Mở Financial, Specifications | Odometer hiện "mi", Specifications hiện cm, kg, lít, chưa rõ lý do | `Xem` |

### 13.2 Tự động hoá: trình dựng và mẫu

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| C-08 Apply mẫu | Bấm Apply | Mở trình dựng theo mẫu, chưa lưu gì | `Chạy` |
| C-09 Rời trang | Chưa bấm Save | Không để lại bản rác | `Chạy` |
| C-10 Save khi chưa đủ | Chưa có trigger, hành động | Save mờ | `Chạy` |
| C-11 Mẫu cần nhãn | Tài khoản chưa có nhãn, mẫu Add Label | Hiện "Missing Value" | `Chạy` |
| C-12 Mẫu cần chọn giá trị | Mẫu Update Vehicle Status when a Work Order is Created | Trường trạng thái để trống, phải chọn | `Chạy` |
| C-13 Mẫu tự gán người | Mẫu Automatically Assign Employee | Tự điền người đang đăng nhập vào Assigned To | `Chạy` |
| C-14 Mẫu chưa đọc | Send Email When A Work Order Total Exceeds Amount | Chỉ thấy tên, 1 điều kiện, 1 hành động | `Xem` |

### 13.3 Tự động hoá: chạy

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| C-15 Đang tắt | Issue #40 tạo khi `TEST-NEN-AUTO-01` tắt | Không có comment, không có lượt chạy | `Chạy` |
| C-16 Không chạy bù | Bật AUTO-01 sau khi #40 đã có | #40 vẫn không có comment | `Chạy` |
| C-17 Bật, khớp | Issue #42 | Trong vòng 6 giây có comment, tác giả "Fleetio Automation"; Run History 1 SUCCESS | `Chạy`, `automation-comment-result.jpg` |
| C-18 Không khớp | Issue #41 của nhóm khác tạo trong lúc bật | Total Runs vẫn 1: lượt không khớp không được tính | `Chạy` |
| C-19 Hai automation | Issue #43 khớp AUTO-01 và AUTO-02 | Cả hai chạy: có comment và lên Critical | `Chạy` |
| C-20 Hoa thường | Description "low engine oil pressure", điều kiện "Low Engine Oil Pressure" | Vẫn khớp, Priority Critical | `Chạy` |
| C-21 Tự kích hoạt | AUTO-02 Created or Updated tự đổi Priority của chính Issue | 2 lượt Create rồi Update, sau đó dừng vì giá trị không đổi | `Chạy`, `automation-self-trigger-runs.jpg` |
| C-22 Người gây ra | Lượt Update do automation gây ra | "Triggered By" vẫn ghi người tạo Issue, không ghi automation | `Chạy`, `automation-self-trigger-runs.jpg` |
| C-23 Kết quả chạy | Lượt thêm comment | "Records: No records changed" dù đã thêm comment | `Chạy`, `automation-run-result.jpg` |
| C-24 Tạo bản ghi | Issue #44 khớp AUTO-03 | Work Order #105 trạng thái Open trên `TEST-XE-01`, Resolved Issues trỏ #44 | `Chạy` |
| C-25 Tạo WO đã xong | Chọn Completed trong hành động | KHÔNG có lựa chọn này; hộp chỉ có Open, Pending | `Chạy` |
| C-26 Vòng lặp tự thân | AUTO-02, giá trị không đổi | Dừng sau 2 lượt | `Chạy` |
| C-27 Vòng lặp chéo | Hai automation lật giá trị của nhau | KHÔNG chạy: tài liệu hãng không nêu giới hạn. Kết quả chưa biết | Không chạy |
| C-28 Lượt thất bại | Thử bằng WO Completed bị giao diện chặn | KHÔNG tái hiện được; Failed Runs luôn 0 | `Xem` |
| C-29 Priority mặc định | Issue mới không nhập mức | Priority "Auto-assign"; #40, #42 tự thành High. Nguyên nhân AI Issue Prioritization là `Suy` | `Chạy` |

### 13.4 Tự động hoá: vòng đời

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| C-30 Bật | Gạt công tắc | Hộp xác nhận; sinh v.1; ghi Enabled At | `Chạy`, `automation-detail.jpg` |
| C-31 Tắt | Gạt công tắc | Hộp "When you disable this automation ... it will stop working and prevent any actions from running." | `Chạy` |
| C-32 Archive khi đang bật | Không tắt trước | Hộp xác nhận, tắt ngay, ghi Disabled At | `Chạy`, `automation-archived.jpg` |
| C-33 Sửa bản Archived | Đang Archived | "Archived records are read-only and cannot be updated." | `Chạy` |
| C-34 Restore | Đang Archived | "Record successfully restored", về Disabled, KHÔNG tự bật lại | `Chạy` |
| C-35 Delete | Nút có trên bản Archived | KHÔNG bấm theo ràng buộc | Không chạy |
| C-36 Sửa khi đang bật, Make a Copy | Muốn xem v.2 | Chưa làm | Không chạy |
| C-37 Trigger Vehicle, Update Vehicle Status | Sẽ sửa xe của nhóm khác | KHÔNG chạy | Không chạy |
| C-38 Run Summary Email | Sẽ gửi email | KHÔNG bật | Không chạy |

### 13.5 Liên hệ, quyền, nhóm, xe

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| C-39 Chỉ tên | Không email, không phân loại | Lưu được; "This Contact doesn't have user access." | `Chạy`, `contact-no-access.jpg` |
| C-40 Trùng tên | Tạo lại cùng First Name | Lưu được, KHÔNG cảnh báo trùng | `Chạy` |
| C-41 Gán xe khi không phải Operator | Xem khối gán xe | Bị chặn bằng câu dẫn | `Chạy`, `contact-no-access.jpg` |
| C-42 Mở Role | Edit Role cả 4 vai | Đọc được 30 module; bấm Cancel, không đổi | `Xem` |
| C-43 Hiệu lực quyền | Cần đăng nhập vai khác | KHÔNG kiểm được vì không mời người | Không chạy |
| C-44 Record Set mặc định | Mở bản mặc định | Bị khoá sửa | `Xem` |
| C-45 Require Group | Còn 5 xe, 3 liên hệ thiếu nhóm | Ô khoá, "all existing assets and contacts must be assigned a group" | `Xem` |
| C-46 Đổi trạng thái xe | Chỉ có xe nhóm khác và Sample | KHÔNG đổi | Không chạy |
| C-47 Archive xe | Nút trong menu More Actions | KHÔNG bấm; Restore chưa kiểm | `Xem`, `vehicle-more-actions.jpg` |
| C-48 Recall | 261 dòng Sample | Chỉ đọc, không đổi trạng thái | `Xem`, `recalls-list.jpg` |
| C-49 Motor Pool | Cần tạo Motor Pool trong Settings, cần xe của nhóm | KHÔNG chạy; danh sách rỗng | `Xem`, `motor-pool-reservations.jpg` |
| C-50 Documents | Rỗng | Không tải tệp | `Xem`, `documents-empty.jpg` |

### 13.6 Trang đầu

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| C-51 Thẻ Open Issues | Bấm Open, Overdue | `issues/state/opened`, `issues/state/overdue` | `Chạy` |
| C-52 Thẻ Service Reminders | Bấm Overdue, Due Soon | `service_reminders/status/*` | `Chạy` |
| C-53 Thẻ Overdue Inspections | Bấm số, % | `inspection_schedules/status/overdue`, `.../all` | `Chạy` |
| C-54 Thẻ Faults | Critical; Open, Pending | `faults`; `faults/state/*` | `Chạy` |
| C-55 Thẻ Renewal | Vehicle, Contact Renewal, Overdue, Due Soon | `.../status/*` | `Chạy` |
| C-56 ROs Needing Approval rỗng | Không có dữ liệu | KHÔNG có đích | `Chạy` |
| C-57 Get Started | Đi qua các trang | Bộ đếm đổi giữa 3/5 và 3/6 | `Chạy` |

### 13.7 Báo cáo và chia sẻ

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| C-58 Bấm Share | Không có bước xác nhận | Link công khai sinh NGAY; "Link expires in 7 days", "this link allows anyone with access to view all data" | `Chạy` |
| C-59 Mở link | Mở thử trong khoảng 5 phút | Xem được dữ liệu Issues | `Chạy` |
| C-60 Thu hồi trong hộp | Bấm "click here to unshare" | Không có tác dụng, bấm lại trả 404, link vẫn sống | `Chạy` |
| C-61 Thu hồi đúng lối | Reports › Shared › Unshare, hộp "Are you sure you want to unshare this report?" | Shared về 0, mở lại không còn báo cáo | `Chạy` |
| C-62 Hết hạn | Chờ hết hạn | KHÔNG chờ; chỉ có câu trên hộp | `Xem` |
| C-63 Mở 48 báo cáo còn lại | | KHÔNG mở sâu; chưa có bảng cột, lọc | Không chạy |
| C-64 Saved Reports | | KHÔNG đọc do lỗi đợt | Không chạy |

### 13.8 Hỏi dữ liệu

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| C-65 Đếm sự cố mở | "How many open issues does vehicle TEST-XE-01 have?" | "currently has 2 open issues", bảng Total Count Issue Id = 2; trang xe thật Open 7; khoảng 40 giây | `Chạy`, `ai-analyst-issues.jpg` |
| C-66 Đọc km mới nhất | "What is the latest meter reading of TEST-XE-01 and when was it recorded?" | "1,700.0 (primary meter), recorded in November 2026"; trang xe thật 2.999 km; khoảng 50 giây | `Chạy` |
| C-67 Cảnh báo độ trễ | Cả 2 câu | KHÔNG ghi dữ liệu tính đến lúc nào | `Chạy` |
| C-68 Màn mở trial | Bấm Ask a data question | Không có màn mở trial | `Chạy` |

### 13.9 Điều KHÔNG làm trong lượt chạy

Đổi trạng thái thật và Archive xe, bản ghi trùng tên xe, Motor Pool chạy thật (cần một chỗ xe); vòng lặp chéo, lượt thất bại, version v.2; cột và lọc của 48 báo cáo; Saved Reports; mẫu Send Email Work Order; hiệu lực quyền thật. Tools, Tool Management, Custom Records, Advanced Analytics ngoài AI Data Analyst không mở theo ràng buộc.

## 14. Bảng Settings từng trang

Mọi dòng là `Xem`: mở trang, đọc, không Save. Giá trị là của tài khoản dùng thử lúc đọc; chỉ dòng ghi "(Default)" hoặc "mặc định" là mặc định sản phẩm đọc được trên màn. "Chưa ghi" nghĩa là ghi chú chạy không nêu. Bảng kê 56 tên trang, chưa kể Account Usage nằm trong General (xem OQ-10).

| Trang | Tham số | Mặc định hoặc giá trị đọc được | Ảnh hưởng theo câu trên màn | Mức đọc |
|---|---|---|---|---|
| General Settings | Công ty, địa chỉ, ngành; tiền tệ; định dạng ngày; múi giờ; 12 hay 24 giờ; đơn vị, lít, hệ đo; Vehicle hay Asset; thuế; bật tắt Jobs, Motor Pool, Smart Uploads (Fuel Entry, Service Entry, Inspection Form) | VND; MM/DD/YYYY; CST; các module đều On | Mặc định cho xe mới; đổi tên gọi toàn hệ thống | Đủ |
| Account Usage (trong General) | Documents, Roles, Vehicles, Automations, Custom Records | 0 B of 250.0 GB; 4 of 30; 5 of 5; 0 of 75; 0 of 25 | Hết hạn mức thì chặn tạo | Đủ |
| Billing & Subscriptions | Gói, Add-On, Account Cancellation | Fleetio Manage - Premium 5 Annual; Trialing; Add-On Tool Management | Không bấm Buy, Start Free Trial | Chỉ đọc |
| Export Account Data | 13 loại dữ liệu; CSV hoặc XLS | Chưa ghi | Gửi email; "the download link in the email expires after 7 days" | Đủ, không bấm |
| Sandboxes | Sample Copy; Production Copy | 0/2; 0/0 | Môi trường thử | Đủ |
| Notification Profiles | Hồ sơ; gán bulk từ Contacts | 0 hồ sơ | Quy định ai nhận gì | Đủ |
| Watched Vehicle Groups | Cột Direct Watchers, Total Watchers | 11 nhóm | Quy định xe nào được báo | Đủ |
| Manage Users | Trỏ sang `contacts/users` ngoài Settings | Không áp dụng | Chưa ghi | Mở |
| Security | Minimum Length 8, 15, 30, 50; Expiration None, 30, 60, 90 ngày; chữ hoa thường, số, ký tự; Maximum invalid login attempts 5, 10; Lockout 5, 10, 30 phút; Reset All Passwords | Giá trị đang chọn chưa ghi | Áp khi tạo hoặc đặt lại mật khẩu, không áp SAML | Không bấm |
| Roles | Xem Mục 15 | 4 vai có sẵn | Xem Mục 15 | Đủ |
| Record Sets | Xem Mục 16 | Full Access (Default) | Xem Mục 16 | Đủ |
| AI Service Advisor | Issue Prioritization, Issue Resolution, Fault Monitoring, Service Assessments, Service Writer, mỗi cái có Manage | Trạng thái bật chưa ghi | Có câu điều khoản | Đủ, không bấm |
| Integrations Directory | Chỉ thấy link | Không áp dụng | Chưa ghi | Không mở |
| Integration Links | Link sang hệ khác kèm biến | Rỗng | Chưa ghi | Đủ |
| Webhooks | Webhook | Rỗng | "send a HTTP POST" dạng JSON | Không tạo |
| External Connections | FTP, SFTP, Amazon S3 | Rỗng | Dùng cho báo cáo định kỳ | Không tạo |
| SAML Connectors | Connector, Metadata | Rỗng | Chưa ghi | Không tạo |
| Fleetio MCP | Kết nối | Chưa bật | "Each connection respects the user's role permissions." | Không bật |
| Standard Records | 15 loại bản ghi có trường tuỳ chỉnh | Đều 0 | Chưa ghi | Đủ |
| Custom Records | Add Custom Record | Rỗng | Chưa ghi | Không mở |
| Groups & Subgroups | Cây nhóm; Require Group; Export Data | Sample có Alabama, Florida, Georgia, South Carolina, Tennessee; Require Group khoá | "all existing assets and contacts must be assigned a group" | Đủ |
| Saved Views | Chế độ xem | Rỗng | Chưa ghi | Đủ |
| Labels | Nhãn | Rỗng | Chưa ghi | Đủ |
| Custom Widgets | Widget | Rỗng | Chưa ghi | Đủ |
| External Vehicle IDs | Mã ngoài | Rỗng | Chưa ghi | Đủ |
| Vehicle Statuses | 5 trạng thái có đếm xe; Add Vehicle Status | Active (Default); đếm Active 22, In Shop 2, Inactive 1, Out of Service 0, Sold 0 | Chưa ghi | Đủ |
| Vehicle Types | 25 loại | Car mặc định | Chưa ghi | Đủ |
| Expense Types | 17 loại | Chưa ghi | Chưa ghi | Đủ |
| Expense Settings | Auto Generate Loan / Lease Expenses | Chưa ghi | Tự sinh chi phí trả góp | Đủ |
| Tire Management Settings | Automated tire pressure readings; Tire Rotation Patterns theo cấu hình trục, thêm được mẫu | Đo tự động chỉ 4x2, 4x4 có telematics | Chưa ghi | Một phần danh sách mẫu |
| Motor Pools | Motor Pool | Rỗng | Chưa ghi | Đủ |
| Reservation Rates | Bảng giá đặt xe | Rỗng | Bảng giá đặt xe | Đủ |
| Flat Fees | Phí cố định | Rỗng | Phí cố định | Đủ |
| Inspection Settings | Proximity Threshold; Distance Threshold | Fleetio: 80%; 100 m | Bật cảnh báo Location Exception khi phiếu nộp từ một chỗ | Đủ |
| Issue Priorities | No Priority, Low, Medium, High, Critical; alias; tắt được | No Priority (Default) | Chưa ghi | Đủ |
| Fault Rules | Mã | 11 mã | Chưa ghi | Một phần |
| Service Reminder Settings | Recalculate; Forecasting | Forecasting tắt | Dự báo ngày đến hạn theo km ngày | Đủ |
| Vehicle Renewal Types | Emission Test, Inspection, Insurance, Registration | Chưa ghi | Chưa ghi | Đủ |
| Contact Renewal Types | Certification, License Renewal | Chưa ghi | Chưa ghi | Đủ |
| Maintenance Settings | Enable Work Orders, Next Work Order Number, Require a Meter Reading + Excluded Vehicle Types, Require inspections, Repair Priority Class, Reason for Repair, Category, khoá sửa mã, Inventory Location, Expected Labor Hours, Complaint/Cause/Correction, Markups | Giá trị chưa ghi | "This requirement only applies to future Work Orders or Service Entries." | 3.800/3.965 ký tự |
| Work Order Statuses | Open, Pending, Completed; Type Incomplete, Completed; Add | Open (Default) | Completed "corresponding service reminders updated and issues resolved" | Đủ |
| Reason For Repair Codes | Mã | 59 mã | Chưa ghi | Một phần |
| Repair Priority Class Codes | Scheduled, Non-Scheduled, Emergency | Chưa ghi | Chưa ghi | Một phần |
| System/Assembly/Component Codes | Cây VMRS | 10 nhóm | Chưa ghi | Một phần |
| Warranty Templates | Mẫu bảo hành | Rỗng | Chưa ghi | Đủ |
| Part Settings | Enable Inventory Tracking By Default | Chưa ghi | Chưa ghi | Đủ |
| Part Locations | Kho; Active, Archived | `TEST-KHO-01`, `TEST-KHO-02` | Chưa ghi | Đủ |
| Part Categories | Loại | 8 loại | Chưa ghi | Một phần |
| Part Manufacturers | Hãng | Rỗng | Chưa ghi | Đủ |
| Inventory Adjustment Reasons | Lý do | 11 lý do | Chưa ghi | Đủ |
| Inventory Valuation Method | Average Cost, FIFO, LIFO, Static Pricing | Giá trị đang chọn chưa ghi | Giá xuất kho | Một phần |
| Measurement Units | Đơn vị | 8 đơn vị | Chưa ghi | Đủ |
| Purchase Order Settings | Next Purchase Order Number; Automatically Close Fully Received POs | Chưa ghi | Chưa ghi | Đủ |
| Purchase Order Statuses | Draft, Pending Approval, Rejected, Approved, Purchased, Received Partial, Received Full, Closed; không có Add | Cố định | Cố định, khác Work Order | Đủ |
| Fuel & Energy Settings | WEX auto-assign; Fuel Vendor Location Alert Radius | Chưa ghi | Chưa ghi | Đủ |
| Fuel Types | Loại | 11 loại | Chưa ghi | Một phần |
| Saved Reports | Chưa đọc do lỗi đợt | Chưa ghi | Chưa ghi | Không |

## 15. Ma trận quyền Role

Mở Edit Role cả 4 vai, đọc 30 module, đóng bằng Cancel (`Xem`). F đủ, S một phần, N không. Chưa kiểm hiệu lực thật (OQ-8).

| Module | Fleet Manager | Operator | Technician | Viewer |
|---|---|---|---|---|
| Vehicles | F | S | S | S |
| Meter Entries | F | S | S | S |
| Issues | F | S | S | S |
| Jobs | F | S | S | S |
| Service Entries | F | S | S | S |
| Warranties | F | S | S | S |
| Work Orders | F | S | S | S |
| Inspections | F | S | S | S |
| Service Reminders | F | S | S | S |
| Service Programs | F | S | S | S |
| Vehicle Renewal | F | S | S | S |
| Vendors | F | S | S | S |
| Places | F | S | S | S |
| Location Entries | F | S | S | S |
| Fuel Entries | F | S | N (ghi chú nói "chỉ có ô xem", xem OQ-9) | S |
| Faults | F | N | S | S |
| Recalls | F | N | S | S |
| Service Task Management | F | N | F | N |
| Contacts | F | S | N (xem Basic Info trong dữ liệu ô đánh dấu) | S |
| Contact Renewal | F | S | N (xem Basic Info trong dữ liệu ô đánh dấu) | S |
| Parts | F | N | S | S |
| Purchase Orders | F | N | S | S |
| Standard Reports | F | N | N | N |
| Motor Pool | F | S | N | N |
| Expense Entries | F | N | N | S |
| Dashboards | F | N | N | N |
| Documents | F | S | N | S |
| Advanced Analytics | N | N | N | N |
| Integrations | N | N | N | N |
| Fleetio MCP | N | N | N | N |

**Quyền con đọc được:**

| Module | Quyền con |
|---|---|
| Vehicles | create, edit, view_all, view_details, view_financial_info, view_custom_fields, export_data, update_status, manage_vehicle_assignment, archive_delete, view_documents, manage_documents, manage_photos |
| Work Orders | edit_all, edit, manage_labor_time_entries, edit_number, view_incomplete, view_completed, view_update_cost_information |
| Purchase Orders | có approve và receive tách riêng |
| Motor Pool | check_out, return, cancel |

**Vai mặc định làm được:** Operator: tạo meter, fuel, issue, nộp phiếu, đổi trạng thái xe, gán xe, đặt và trả xe. Technician: tạo và sửa Work Order, chấm công, tạo sửa Issue, sửa tồn kho, nhận hàng Purchase Order.

## 16. Record Set

`Xem`: đọc 4 loại, mở một bản mặc định và form Add Record Set, không lưu.

| Loại | Bản ghi mặc định | Manage | View |
|---|---|---|---|
| Vehicles | Assigned Vehicles Only | Some | Some |
| Vehicles | Full Access (Default) | All | All |
| Vehicles | No Access | None | None |
| Vehicles | User's Group Only | Some | Some |
| Vehicles | View Only | None | All |
| Contacts | Full Access (Default) | All | All |
| Contacts | No Access | None | None |
| Contacts | User's Group Only | Some | Some |
| Contacts | View Only | None | All |
| Part Locations | Full Access (Default) | All | Không có cột |
| Part Locations | No Access | None | Không có cột |
| Inspection Forms | Full Access (Default) | All | Không có cột |
| Inspection Forms | No Access | None | Không có cột |

## 17. 18 mẫu tự động hoá

`Chạy`: Apply từng mẫu để đọc định nghĩa, rời trang không lưu. 17/18 đọc đủ. Số trong mẫu là ví dụ khách sửa được trước khi bật.

| Bản ghi | Tên mẫu | Trigger | Điều kiện | Hành động |
|---|---|---|---|---|
| Fault | Create An Issue When A Critical Fault Is Created | Created | Critical = Yes và Status = Open | Create Issue |
| Fault | Ignore Nuisance Codes | Created | Code = P0456 | Update Fault Status to Ignored |
| Issue | Update Vehicle Status To Active When Issue Status Is Resolved | Updated | Status is Resolved | Update Vehicle Status to Active |
| Issue | Update Vehicle Status To In Shop When Issue Source Is Inspection Failure | Created or Updated | Status Open và Source Inspection Failure | Update Vehicle Status to In Shop |
| Issue | Create A Work Order When An Issue Is Created | Created | Không có | Create Work Order, Status Open |
| Issue | Update Issue To Critical When Issue Contains Low Engine Oil Pressure | Created or Updated | Status Open và Description contains | Update Issue Priority to Critical |
| Issue | Update Issue To Critical When Open Issue Source Is Recall | Created | Source is Recall | Update Issue Priority to Critical |
| Purchase Order | Automatically Approve New Purchase Orders Less Than Or Equal To Amount | Created | Status Pending Approval và Total ≤ 10.000 ₫ | Update PO Status to Approved |
| Purchase Order | Add Comment For Review When a Purchase Order Is Created | Created | Status Pending Approval | Add Comment, có "Prevent duplicate comments" |
| Purchase Order | Add Label For New Purchase Orders Created With Brakes Category | Created | Part Category Brakes | Add to Labels list ("Missing Value" vì tài khoản chưa có nhãn) |
| Service Entry | Send Email When A Service Entry Total Exceeds Amount | Created or Updated | Total ≥ 100.000 ₫ | Send Email, nội dung có biến `{{ service_entry.id }}`, `{{ asset.name }}` |
| Service Entry | Set Repair Priority Class to Scheduled for Engine Oil & Replacement | Created or Updated | Service Tasks is any of Engine Oil & Filter Replacement | Đặt Repair Priority Class |
| Work Order | Update Vehicle Status when a Work Order is Created | Created | Status Type = Incomplete | Update Vehicle Status (để trống, phải chọn) |
| Work Order | Update Vehicle Status to Active when Work Orders are Completed | Updated | Status Type Completed và Vehicle Incomplete Work Orders Count < 1 | Update Vehicle Status to Active |
| Work Order | Send Email When A Work Order Total Exceeds Amount | Chưa đọc | 1 điều kiện | 1 hành động |
| Work Order | Set Repair Priority Class to Scheduled for Preventative Maintenance Work Orders | Created or Updated | Line Item Reason for Repair is any of 08 | Update Repair Priority Class to Scheduled |
| Work Order | Automatically Assign Employee To Newly Created Work Orders | Created | Assigned To is blank | Update Assigned To (tự điền người đang đăng nhập) |
| Work Order | Create Follow-Up Work Order After Tire Replacement | Updated | Service Tasks any of Tire Replacement và Status Type Completed | Create Work Order, Status Open, Service Tasks Wheel Lug Nut Torque |

## 18. 49 báo cáo chuẩn

Đọc đủ 49 tên trên màn (`Xem`), nhưng ghi chú chạy chỉ giữ số theo nhóm và các tên dưới đây; danh sách 49 tên chưa có trong tài liệu này (OQ-11). Mở sâu 1 báo cáo (`Chạy`). Bản 02/11 ghi 48 báo cáo, 12 nhóm là sai.

| Nhóm | Số báo cáo |
|---|---|
| Vehicles | 14 |
| Vehicle Assignments | 2 |
| Inspections | 4 |
| Issues | 2 |
| Service | 8 |
| Warranties | 2 |
| Work Orders | 5 |
| Contacts | 2 |
| Parts | 4 |
| Fuel | 3 |
| Tools | 1 |
| Jobs | 1 |
| Motor Pools | 1 |
| **13 nhóm** | **49** |

**Tên đã ghi:** Issues Report (đã mở); Status Changes, Status Summary (nêu ở Vehicle Statuses); "Upgrading soon" trên Cost/Meter Trend, Expense Summary, Operating Costs Summary, Service History by Vehicle.

## 19. Form xe, từng trường

`Xem`: đọc đủ form, không lưu được vì hết hạn mức. Nút: Cancel, Add Multiple Vehicles, Save & Add Another, Save Vehicle.

| Phần | Trường |
|---|---|
| Details › Identification | Vehicle Name * ("Enter a nickname to distinguish this vehicle in Fleetio."), VIN/SN (nút Decode), License Plate, Type * (mặc định Car), Fuel Type, Year, Make, Model, Trim, Registration State/Province, Labels, Photo |
| Details › Classification | Status * (mặc định Active), Group, Operator, Ownership * (mặc định Owned) |
| Details › Additional Details | Color, Body Type, Body Subtype, MSRP (₫), Linked Vehicles |
| Maintenance | "Choose a Service Program": None ("No Service Reminders will be created") hoặc "Choose an existing Service Program" |
| Lifecycle | In-Service Date, In-Service Odometer, Estimated Service Life in Months, Estimated Service Life in Meter, Estimated Resale Value, Out-of-Service Date, Out-of-Service Odometer |
| Financial | Purchase Vendor, Purchase Date, Purchase Price, Odometer, Notes; Loan/Lease: Loan, Lease, None |
| Specifications | Dimensions (Width, Height, Length, Interior Volume, Passenger Volume, Cargo Volume, Ground Clearance, Bed Length), Weight (Curb Weight, Gross Vehicle Weight Rating), Performance (Towing Capacity, Max Payload), Fuel Economy (EPA City, Highway, Combined), Engine (15 trường), Transmission (4), Wheels & Tires (11), Fuel (Quality, Tank 1, Tank 2), Oil Capacity |
| Settings | Primary Meter * (Miles, Kilometers, Hours), Current Reading, Average Usage per Day (mặc định "Automatically calculate"), Add Secondary Meter; Fuel Unit *, Measurement Units * |

## 20. Trải nghiệm rủi ro

**Share báo cáo sinh link công khai ngay.** Trong lượt chạy, người chạy thử bấm Share trên Issues Report để xem hộp thoại; link công khai đã sinh ngay, không hỏi trước. Mở thử trong khoảng 5 phút xem được dữ liệu Issues. Lối "click here to unshare" trong hộp không có tác dụng và link vẫn sống. Đã thu hồi đúng qua Reports › Shared › Unshare; Shared về 0, mở lại không còn báo cáo. Link không gửi cho ai và không được ghi lại ở bất kỳ tài liệu nào. Bài học: chỉ cần mở hộp là dữ liệu đã có đường ra ngoài (E-fleetio-saas-platform-013, E-fleetio-saas-platform-010).

**AI hỏi dữ liệu trả sai số.** Cả 2 câu hỏi về `TEST-XE-01` đều lệch với trang xe: 2 so với 7 sự cố mở, 1.700 so với 2.999 km. Câu trả lời khẳng định "currently", không có cảnh báo, không ghi dữ liệu tính đến lúc nào. Khả năng do kho phân tích trễ so với dữ liệu giao dịch là `Suy`, chưa kiểm (OQ-13). Người dùng không có cách nhận ra nếu không đối chiếu tay (E-fleetio-saas-platform-012).

**Trial Tools đã bị bật, không rõ ai bật.** Đầu lượt, Billing ghi Tool Management "Start Free Trial", thanh bên có nhãn "Try". Cuối lượt, Billing ghi "Tools - Monthly 25", "Trialing", "14 days left in trial", "Tools 0 of 25", có "Disable Add-On". Nhóm chạy này không bấm nút đó, không xác định được ai bật, và không tắt vì đây là thay đổi cài đặt tài khoản ngoài phần được giao. Cần chủ tài khoản quyết định.

**Dữ liệu thử còn trên tài khoản:** automation `TEST-NEN-AUTO-01`, `TEST-NEN-AUTO-02`, `TEST-NEN-AUTO-03` (đều đang tắt); Issue #40, #42, #43, #44 và Work Order #105 trên xe dùng chung `TEST-XE-01`; hai liên hệ `TEST-NEN-LH-01` không email.
