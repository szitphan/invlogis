---
type: research
feature: fleetio-saas-platform
status: draft
status_changed: 2026-11-03
status_reason: "đã review upstream, không cần sửa"
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

**Giới hạn của lượt chạy:** tài khoản dùng thử đã hết hạn mức xe nên nhóm này không tạo được xe riêng; không mời người, không đổi Settings, không dùng bản ghi Sample để đổi trạng thái, không bấm hành động gửi email. Lượt 3 đo automation trên xe `TEST-DAUKEO-2` rồi trả Status về Active. Chi tiết việc chưa chạy ở Mục 13.9 và Mục 12.

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
| FR-fleetio-saas-platform-002 | Luật bật tắt có giải thích | Mỗi luật có ô tick, câu mô tả tác động, phạm vi; loại trừ theo loại xe (Require a Meter Reading kèm Excluded Vehicle Types). Lượt 3 đọc đủ Maintenance Settings 5.534 ký tự, phần còn thiếu ở Mục 14. | P0 | [Cấu hình] | demo | `Xem`, `Docs` 17 cài đặt Maintenance | `Xem` đọc đủ | Lấy cách trình bày; mẫu cho loại xe không đồng hồ như mooc |
| FR-fleetio-saas-platform-003 | Danh mục theo khách | Trạng thái, loại, mã, lý do, đơn vị do khách sửa; có mục khoá của hệ thống, có bí danh, tắt được từng mục (Issue Priorities). Số mục ở Mục 14. | P0 | [Cấu hình] | demo | `Xem` | `Xem` | Lấy |
| FR-fleetio-saas-platform-004 | Tắt cả module | Ví dụ Enable Work Orders; tắt thì ẩn Work Orders, Parts. General Settings còn bật tắt Jobs, Motor Pool, Smart Uploads (Fuel Entry, Service Entry, Inspection Form). Đề xuất: khách chỉ tắt trong phạm vi đã mua. | P0 | [Lõi] | test | `Xem` | `Xem`, chưa tắt thử | Lấy cho bật gói |
| FR-fleetio-saas-platform-005 | Role | Bốn vai có sẵn: Fleet Manager, Operator, Technician, Viewer; 30 module, mỗi module mức đủ, một phần, không; thêm vai mới; khoá vai mặc định. Ma trận ở Mục 15. | P0 | [Lõi] [Cấu hình] | demo | `Xem` mở Edit Role cả 4 vai, bấm Cancel | `Xem`, chưa kiểm hiệu lực thật | Đối chiếu `access-control` |
| FR-fleetio-saas-platform-006 | Record Set | Phạm vi dữ liệu theo Vehicles, Contacts, Part Locations, Inspection Forms; mẫu Assigned Only, Full, No Access, Group Only, View Only; quyền Manage và View riêng. Bảng ở Mục 16. | P0 | [Lõi] [Cấu hình] | test | `Xem`, `Docs` | `Xem`, chưa kiểm hiệu lực thật | Rất đáng lấy; "theo xe được gán" hợp lái xe đầu kéo; thêm phạm vi Chi nhánh |
| FR-fleetio-saas-platform-007 | Điều kiện theo trường tuỳ chỉnh | Record Set lọc được theo trường tuỳ chỉnh dạng chọn, tick. | P2 | [Cấu hình] | test | `Docs`; `Xem` có điều kiện "Vehicles with specific custom field values" | `Docs`, `Xem` tên điều kiện | Cân nhắc |
| FR-fleetio-saas-platform-008 | Trang đầu Needs Attention | Thẻ đếm dẫn tới danh sách đã lọc (đích từng thẻ ở Mục 13.6); "ROs Needing Approval" không có đích khi rỗng; mỗi thẻ tải riêng; lọc theo nhóm; tuỳ biến, nhiều dashboard; phía dưới có Cost, Inspections, Recent Activity. Custom Dashboards có My Dashboards, Shared With Me, cột Title, Visibility, Last Updated, riêng theo vai và người (`Xem`). | P0 | [Lõi] [Cấu hình] | demo | `Chạy` | `Chạy` | Lấy cho `common-workspace` |
| FR-fleetio-saas-platform-009 | Danh sách chuẩn | Tab đếm số, lọc nhanh, Filters có nhóm điều kiện, sắp xếp, nhóm dòng, chọn cột, phân trang, chọn nhiều. Trên Issues: Group có None, Priority, Vehicle or Tool, Group; View Settings có Manage Columns, Items Per Page 50, 100, 200, Density Default, Compact; Manage Columns kéo đổi thứ tự, Restore defaults; trang mở lại đúng tab dùng lần trước; menu dòng View, Edit, Add to Service Entry, Add to Work Order, Get Service at Shop, Resolve with Note, Check service history (khoá), Close, Delete. Bấm dòng sang trang chi tiết. Ô chọn nhiều có ở tab Open, Closed, chưa bấm. | P0 | [Lõi] | demo | `Xem` | `Chạy` lượt 3: Tìm, nhóm, cột | Lấy |
| FR-fleetio-saas-platform-010 | Chế độ xem đã lưu | Add Tab, Save View, Save Changes; My Saved Views, Saved Views dùng chung. Có thay đổi thì nút thành Save Changes có chấm cam. "Fleetio Standard View" có khoá, chỉ có Save as New View, Clear Unsaved Changes. Hộp lưu: Name, Description, Shared with (Private, Admins Only, Specific Roles, Specific Users, Everyone); lưu xong thành tab mới cạnh All, Open. | P1 | [Lõi] | demo | `Xem` | `Chạy` lượt 3: Lưu view Private | Lấy |
| FR-fleetio-saas-platform-011 | Xem nhanh bản ghi | Record peek mở ngay trên danh sách. Lượt 3: bấm dòng trên Issues sang thẳng trang chi tiết, không mở khung xem nhanh; chưa thử màn khác (OQ-18). | P1 | [Lõi] | demo | `Xem` nút đóng | `Xem` | Lấy nếu rẻ |
| FR-fleetio-saas-platform-012 | Tự động hoá | Trigger gồm loại bản ghi và kiểu sự kiện; điều kiện tuỳ chọn; hành động Update Field, Add Comment, Send Email, Create Record; có bật tắt, phiên bản, đếm lần chạy. Đã tạo, bật, chạy, tắt, Archive, Restore, sửa khi đang bật, Make a Copy; có lượt thất bại thật (FR-060). | P1 | [Cấu hình] | demo | `Chạy`, `Docs` | `Chạy` một phần lượt 3: Đủ Update, Comment; Send Email không chạy | Làm sau; trước mắt dùng luật có tham số |
| FR-fleetio-saas-platform-013 | Loại bản ghi tự động hoá | Work Order, Service Entry, Fault, Issue, Purchase Order, Geofence Event, Vehicle. Kiểu sự kiện gồm Created, Updated, Created or Updated, Deleted; Vehicle không có Deleted. Bản ghi hành động chọn được với Issue: Issue, Vehicle, Work Order. Work Order: 61 trường điều kiện (nhóm WORK ORDER, VEHICLE, không có Description); Update Field gồm Status, Repair Priority Class, Issued By, Assigned To, Vendor, Labels; hành động Update Field, Add Comment, Send Email, Create Record. Service Entry (lượt 4 `Chạy`): Created, Updated, Created or Updated, Deleted; bản ghi hành động Service Entry hoặc Vehicle; Update Field chỉ Repair Priority Class, Labels. Purchase Order (lượt 4 `Chạy`): Created, Updated, Created or Updated, không có Deleted; bản ghi hành động chỉ Purchase Order; Update Field Labels, Status (chỉ Rejected, Approved). Fault (lượt 4, lưu Disabled, chưa có lượt thật): chỉ Created; bản ghi hành động Issue, Fault, Vehicle; trên Issue chỉ Create Record với Assigned to, Priority, không có ô Summary; trên Fault Update Field chỉ Status, giá trị chỉ Ignored. | P1 | [Cấu hình] | demo | `Xem` | `Chạy` một phần lượt 4: SE, PO chạy thật; Fault chỉ lưu, không phát sinh | Tham khảo |
| FR-fleetio-saas-platform-014 | Mẫu tự động hoá | 18 mẫu: Faults 2, Issues 5, Purchase Orders 3, Service Entries 2, Work Orders 6; gợi ý đúng lúc ngay sau hành động liên quan. Bảng từng mẫu ở Mục 17, lượt 3 đọc nốt mẫu thứ 18. Mẫu đổi ngưỡng theo tiền tệ khách nhưng câu email vẫn viết cứng (BR-047). | P1 | [Cấu hình] | demo | `Chạy` Apply từng mẫu, không lưu | `Chạy` lượt 4: 18/18 mẫu đọc đủ | Lấy gợi ý đúng lúc; lấy mẫu "WO xong và xe không còn WO mở thì xe về Active" |
| FR-fleetio-saas-platform-015 | Khởi tạo khách | Dữ liệu mẫu có nhãn Sample, tắt được; Sample không tính vào hạn mức; Onboarding Tasks trỏ 7 đường dẫn; danh sách Get Started, mẫu số đổi giữa các trang (3/5 và 3/6). | P0 | [Lõi] | demo | `Chạy` bộ đếm đổi | `Chạy` | Lấy; dữ liệu mẫu không lấy từ khách thật; bộ đếm phải nhất quán |
| FR-fleetio-saas-platform-016 | Hướng dẫn tại chỗ | Khung Learn có mô tả, ảnh, More Info, Academy; đóng được. | P1 | [Lõi] | demo | `Chạy` | `Chạy` | Lấy cho `help-center` |
| FR-fleetio-saas-platform-017 | Theo dõi, bình luận | Watch; người tạo tự theo dõi; bình luận, nhắc tên; cột phải trên trang chi tiết. Automation bình luận với tác giả "Fleetio Automation". Unwatch làm avatar mất khỏi cụm người theo dõi, Watch lại được. Ô @ hiện liên hệ kèm biểu tượng khoá nếu không có quyền truy cập; không khớp khi gõ không dấu hoặc có gạch nối (E-020). | P1 | [Lõi] | demo | `Chạy` tự theo dõi, comment do automation | `Chạy` lượt 3: Comment, Watch; @ không khớp dấu, gạch nối | Lấy |
| FR-fleetio-saas-platform-018 | Thông báo | Hồ sơ thông báo gán cho người (gán bulk từ Contacts), nhóm xe theo dõi có cột Direct Watchers, Total Watchers, cài đặt cá nhân (FR-061); hộp Inbox, Archived, All Activity, Comments Only, @ Mentions, Archive all; từng dòng có Reply, View All Comments. Người theo dõi nhận thông báo in-app kể cả khi tài khoản có 0 hồ sơ thông báo (BR-042). Notification Profiles cột Name, Description, Users Assigned, Users Personalized, Status. | P1 | [Cấu hình] | demo | `Xem` | `Chạy` một phần lượt 3: Inbox, cài đặt cá nhân; 0 hồ sơ | Lấy |
| FR-fleetio-saas-platform-019 | Báo cáo chuẩn | 49 báo cáo 13 nhóm; yêu thích, lưu, chia sẻ; dạng lưới, danh sách; nhãn "Upgrading soon" trên 4 báo cáo. Bảng nhóm ở Mục 18; đủ tên, đường dẫn, cột ở Phụ lục báo cáo chuẩn. Hai thế hệ giao diện ở FR-054. | P1 | [Gói: Bảo dưỡng đội xe] | demo | `Xem` | `Chạy` một phần lượt 4: Đọc bộ lọc 47 báo cáo, lọc thật 1; expense_entries lỗi 500 | Chọn khoảng 10 |
| FR-fleetio-saas-platform-020 | Hỏi dữ liệu | Nút Ask a data question trên đầu trang mở AI Data Analyst, khung nhúng từ ThoughtSpot; hỏi bằng lời ra bảng; Show work, chọn All data models, lưu My Conversations; mở lại chat cũ có banner "This data may have changed since the last time you had a chat." Đã thử 4 câu qua 2 lượt, không câu nào khớp trang xe; lượt 3 trả 10/12 sự cố và nói xe mới tạo "does not exist" (E-012, E-015). | P2 | [Lõi] | demo | `Chạy` 2 câu | `Chạy` | Cân nhắc; nếu làm phải ghi "dữ liệu đến thời điểm" |
| FR-fleetio-saas-platform-021 | Tìm toàn cục | Bản trước ghi 15 loại bản ghi; lượt 3 đếm ô chọn loại có 16 mục (chưa tách mục "All"). Kết quả theo nhóm VEHICLES, CONTACTS, SERVICE ENTRIES, VENDORS, PARTS, ISSUES..., mỗi nhóm 3 dòng và More. Không đòi khớp cả cụm: gõ TEST-NEN ra cả bản ghi chỉ chứa "TEST". | P1 | [Lõi] | demo | `Xem` | `Chạy` lượt 3: Tìm theo nhóm, tách theo từ | Lấy |
| FR-fleetio-saas-platform-022 | Lịch sử bản ghi | View Record History; lịch sử từng trường. Có trên xe, automation, Issue. Cột Date, Changes By, Changes Made, lọc theo khoảng ngày. Comment, Watch không vào lịch sử (BR-040). Lịch sử trạng thái xe ghi nguồn và thời gian ở mỗi trạng thái (FR-059). | P0 | [Lõi] | demo | `Xem` | `Chạy` lượt 3: Đọc lịch sử Issue, xe | Lấy |
| FR-fleetio-saas-platform-023 | Giới hạn theo gói | Hiện đã dùng trên giới hạn: tài liệu, vai, xe, tự động hoá, bản ghi tự tạo (Fleetio: 250.0 GB, 30, 5, 75, 25). Hết hạn mức thì chặn tạo và khoá nút; danh sách xe hiện "5 of 5". Giá trị theo hợp đồng, khách không tự nâng. Automations chỉ đếm bản đang bật: 0 of 75 khi 7 bản đều tắt, 1 of 75 khi lưu 10 bản, bật 1 (BR-037). Chặn khi hết hạn mức Automations chưa đo: cần 75 bản bật. | P1 | [Lõi] | demo | `Chạy` bị chặn thật | `Chạy` một phần lượt 4: Đếm 1 of 75; chặn hạn mức chưa thử | Lấy khi bán gói |
| FR-fleetio-saas-platform-024 | Kho tài liệu | Danh sách file, thư mục, biết gắn bản ghi nào; tab All Documents và tab tên tài khoản; cột File Name, File Size, Location, Auto-Delete, Attached To, Labels; lọc Document File Type, Document Location Type. Upload Document qua hộp Filestack; menu dòng View, Rename, Replace, Download, Delete; trang tệp có khung xem, Type, Auto-Delete, Add Description, Comments. Gắn xe ở FR-062. | P2 | [Cấu hình] | demo | `Xem` khung rỗng | `Chạy` lượt 3: Tải tệp TEST, gắn xe | Cân nhắc |
| FR-fleetio-saas-platform-025 | Bản ghi tự tạo | Khai loại, trường, liên kết, bố cục kéo thả; trang danh sách, chi tiết; hiện theo tab trên bản ghi liên kết. | P2 | [Gói: Khách lớn, chưa có trong danh sách gói] | demo | `Docs`, không mở | `Docs` | Để sau |
| FR-fleetio-saas-platform-026 | Trường tuỳ chỉnh | Nhãn duy nhất theo loại; không đổi kiểu sau khi lưu; xoá thì mất ở mọi bản ghi. Standard Records liệt kê 15 loại bản ghi có trường tuỳ chỉnh, đều 0. | P1 | [Cấu hình] | test | `Docs`, `Xem` Standard Records | `Docs`, `Xem` | Lấy |
| FR-fleetio-saas-platform-027 | Webhook | Chọn một sự kiện mỗi webhook; hơn 50 sự kiện; ký xác thực; thất bại 3 lần liên tiếp thì tắt. Màn ghi "send a HTTP POST" dạng JSON. | P2 | [Gói: Khách lớn, chưa có trong danh sách gói] | test | `Xem`, `Docs` | `Xem` rỗng, không tạo | Để sau |
| FR-fleetio-saas-platform-028 | API, SAML, MCP | API key, đăng nhập SAML (có Metadata), máy chủ MCP: "Each connection respects the user's role permissions." Module Fleetio MCP mức không có ở cả 4 vai mặc định; nối được Claude, Codex hoặc MCP client khác. Manage API Keys: cột Label, Token, API Version, Date Added, Status; Account Tokens có Rate Limit (Fleetio: 250 requests/minute); khoá đã thu hồi không kích hoạt lại. SAML: Metadata, IdP Entity Id, SSO URL. | P2 | [Gói: Khách lớn, chưa có trong danh sách gói] | demo | `Xem` | `Xem`, không bật | Để sau |
| FR-fleetio-saas-platform-029 | Sandbox, xuất dữ liệu | Môi trường thử: Sample Copy, Production Copy có hạn mức riêng. Export Account Data: 13 loại dữ liệu (Vehicles, Vehicle Assignments, Meter Entries, Issues, Service Entries, Work Orders, Work Order Line Items, Work Order Sub Line Items, Contacts, Vendors, Parts, Purchase Order, Fuel Entries), CSV hoặc XLS, gửi qua email, link hết hạn (Fleetio: 7 ngày). Sandboxes cột Name, URL, Type, Status, Date Created, Last Data Refresh. | P2 | [Gói: Khách lớn, chưa có trong danh sách gói] | demo | `Xem` | `Xem`, không bấm | Để sau |
| FR-fleetio-saas-platform-030 | Danh sách tự động hoá | Cột Name, Status, Trigger Record, Total Runs, Successful Runs, Failed Runs, Created By, Last Run At, Current Version; tab All, Archived; lọc Created By, Trigger Record, Status, Filters. | P1 | [Cấu hình] | demo | `Chạy`, ảnh `automation-list-data.jpg` | `Chạy` | Lấy cột đếm lượt |
| FR-fleetio-saas-platform-031 | Thư viện mẫu | Browse Templates: cột trái theo loại trigger, thẻ có sơ đồ trigger, số điều kiện, số hành động, nút Apply khi rê chuột. Apply mở trình dựng đã điền sẵn, chưa lưu gì. | P1 | [Cấu hình] | demo | `Chạy`, ảnh `automation-templates.jpg` | `Chạy` | Lấy |
| FR-fleetio-saas-platform-032 | Bật tắt có xác nhận và phiên bản | Lưu xong ở trạng thái tắt; bật phải qua hộp xác nhận và lúc đó sinh phiên bản v.1, ghi Enabled At; tắt cũng có hộp xác nhận. Tắt rồi bật lại không sinh phiên bản mới, chỉ đổi Enabled At. Trước khi bật lần đầu, Current Version là "—". | P1 | [Cấu hình] | test | `Chạy` | `Chạy` lượt 3: Sửa khi bật lên v.2, chạy theo v.2 | Lấy: khách thử an toàn |
| FR-fleetio-saas-platform-033 | Archive và Restore automation | Archive không cần tắt trước, tắt ngay, ghi Disabled At; bản Archived chỉ đọc; Restore về Disabled, không tự bật. Khi chưa Archive, menu More Actions có Make a Copy, Archive, View Record History; Delete chỉ hiện ở bản Archived. Bản Archived mất công tắc, Edit, menu; bản ghi khớp đổi không sinh lượt. Restore một cú bấm, không hộp xác nhận, giữ phiên bản, Run History, Disabled At. | P1 | [Cấu hình] | test | `Chạy` Archive, Restore; `Xem` các nút còn lại | `Chạy` lượt 4: Archive khi bật, Restore về Disabled | Lấy |
| FR-fleetio-saas-platform-034 | Run History và Run Result | Mỗi lượt có kết quả, phiên bản, Processed At, Records, bản ghi kích hoạt, Trigger Type, Triggered At, Triggered By, View Full Log dạng JSON từng bước (Workflow, Trigger, ActionSet, ConditionSet, ScoopMatcher, Database, có runtime). Lượt 3 đã thấy cả FAILURE (FR-060). | P1 | [Cấu hình] | test | `Chạy`, ảnh `automation-run-history.jpg`, `automation-run-result.jpg` | `Chạy` lượt 4: Có cả lượt FAILURE | Lấy; sửa "Triggered By" và "No records changed" (xem BR-012, BR-013) |
| FR-fleetio-saas-platform-035 | Trình dựng điều kiện | Với Issue: 59 trường, chia nhóm Issue, Tool, Vehicle, Vehicle or Tool; All of, Any of; nhóm điều kiện lồng, hiện "And", "Or" ở khung trái. So khớp không phân biệt hoa thường. Trường thứ 2 thêm vào cùng nhóm có toán tử mặc định "does not contain"; Enter trong ô giá trị đóng panel như Apply. | P1 | [Cấu hình] | test | `Chạy` điều kiện contains; `Xem` phần còn lại | `Chạy` lượt 3: Nhóm lồng All of + Any of, khớp đúng | Tham khảo |
| FR-fleetio-saas-platform-036 | Hành động Create Record | Tạo Work Order từ Issue; chỉ có Status, Assigned To, Service Tasks; Status chỉ cho Open và Pending; WO sinh ra liên kết Issue ở cột Resolved Issues. Khác Update Field, nơi Status có đủ Open, Pending, Completed (BR-036). | P1 | [Cấu hình] | test | `Chạy` | `Chạy` | Lấy: tránh bỏ qua kiểm tra km khi hoàn tất |
| FR-fleetio-saas-platform-037 | Thông báo của automation | Failure Notification Email: "Send an email whenever this automation fails." Run Summary Email: "Receive a summary email of successful automations. Select from Daily at 6:00 am, or Weekly on Mondays at 6:00 am." Mention trong comment: "Notifications for mentions in comments are delivered based on users' permissions and notification settings." Có ô Prevent duplicate comments. | P2 | [Cấu hình] | demo | `Xem`, không bật vì gửi email | `Xem` | Lấy |
| FR-fleetio-saas-platform-038 | Liên hệ một bảng | Một bảng Contact, phân vai bằng tick Operator, Employee, Technician; User Access: Enable Access to Fleetio hoặc No Access (mặc định). Người dùng là liên hệ được bật truy cập. Không email vẫn lưu được; không chặn trùng tên. Mở truy cập ở FR-063. | P0 | [Lõi] | test | `Chạy`, ảnh `contact-no-access.jpg` | `Chạy` một phần lượt 3: Đọc form Enable Access, không lưu | Lấy; thêm cảnh báo trùng người |
| FR-fleetio-saas-platform-039 | Form xe sáu phần | Details, Maintenance, Lifecycle, Financial, Specifications, Settings; trường ở Mục 19. Out-of-Service chỉ là trường ngày và số km, không có nút thanh lý. | P1 | [Lõi] [Cấu hình] | demo | `Xem` đọc đủ form, không lưu được | `Chạy` lượt 3: Lưu ngày, số Out-of-Service; Status không đổi | Đối chiếu nhóm Phương tiện |
| FR-fleetio-saas-platform-040 | Nhóm nhiều cấp | Groups & Subgroups dạng cây; Require Group chỉ mở khi mọi tài sản và liên hệ đã có nhóm, màn liệt kê số còn thiếu; Export Data. | P0 | [Lõi] [Cấu hình] | test | `Xem` | `Xem`, không đổi | Lấy làm khung Công ty, Chi nhánh, Cơ sở |
| FR-fleetio-saas-platform-041 | Trạng thái xe theo danh mục | Active (Default), In Shop, Inactive, Out of Service, Sold có đếm xe, Add Vehicle Status; không thấy luật chuyển; có lịch sử trạng thái, báo cáo Status Changes, Status Summary. | P1 | [Lõi] [Cấu hình] | test | `Xem` | `Xem`, chưa đổi thật | Đối chiếu nhóm Phương tiện |
| FR-fleetio-saas-platform-042 | Recall | Danh sách từ NHTSA theo năm, hãng, đời; tab All, Needs Action, Open, Resolved, Acknowledged; cột Issued At, Status, Issue, Manufacturer Campaign Number, NHTSA Campaign Number. Một mẫu tự nâng Critical khi nguồn là Recall. Số dòng đổi theo thời điểm: tab Needs Action đọc 261 ở ảnh `recalls-list.jpg`, 285 ở lượt của nhóm Sửa chữa (C-223). Menu dòng theo nhóm Sửa chữa: Acknowledge, Create Issue, Check VIN. | P2 | [Gói: Bảo dưỡng đội xe] | demo | `Xem`, ảnh `recalls-list.jpg` | `Xem` 285 dòng Sample (261 ở lần đo trước), không đổi trạng thái | Nguồn thu hồi của Việt Nam chưa biết; để sau |
| FR-fleetio-saas-platform-043 | Motor Pool | Đặt xe dùng chung: cột Motor Pool, Number, Operator, Vehicle Types, Vehicle, Pick Up, Drop Off, Status; Settings có Motor Pools, Reservation Rates, Flat Fees; quyền check_out, return, cancel. Form Vehicle Reservation: Operator *, Motor Pool *, Reason for Trip, Pick Up *, Drop Off *, Submit Reservation; Motor Pool * lấy từ Settings, đang rỗng nên không đặt được. | P2 | [Gói: Khách lớn, chưa có trong danh sách gói] | demo | `Xem`, ảnh `motor-pool-reservations.jpg` | `Xem` rỗng; chưa chạy | Để sau |
| FR-fleetio-saas-platform-044 | Quyền con theo module | Vehicles có create, edit, view_all, view_details, view_financial_info, view_custom_fields, export_data, update_status, manage_vehicle_assignment, archive_delete, view_documents, manage_documents, manage_photos. Work Orders, Purchase Orders, Motor Pool có quyền con ở Mục 15. | P0 | [Lõi] | test | `Xem` | `Xem` | Lấy cách tách xem tài chính, duyệt, nhận hàng |
| FR-fleetio-saas-platform-045 | Cảnh báo chi phí tại quyền | Ngay tại quyền Create của Vehicles: "Adding new Vehicles will result in additional charges to your account's subscription." | P2 | [Lõi] | demo | `Xem` | `Xem` | Lấy nếu tính tiền theo xe |
| FR-fleetio-saas-platform-046 | Điều kiện Record Set tự tạo | Vehicles có 8 điều kiện: All vehicles, Vehicles in this contact's group, Vehicles assigned to this contact, Specific vehicles, Vehicles in specific groups, Vehicles with specific status(es), Vehicles with specific custom field values, No vehicles. Manage và View khai riêng. | P0 | [Lõi] [Cấu hình] | test | `Xem`, ảnh `record-set-conditions.jpg` | `Xem`, không lưu | Lấy; thiếu điều kiện theo thời gian |
| FR-fleetio-saas-platform-047 | Chính sách bảo mật | Minimum Length, Expiration, yêu cầu ký tự, Maximum invalid login attempts, Lockout, Reset All Passwords; Session Timeout tách Fleetio Go và Fleetio Web; giá trị ở Mục 14. | P1 | [Lõi] [Cấu hình] | test | `Xem`, không bấm | `Xem` | Đối chiếu `account-access` |
| FR-fleetio-saas-platform-048 | AI Service Advisor | Issue Prioritization, Issue Resolution, Fault Monitoring, Service Assessments, Service Writer, mỗi cái có Manage, có câu điều khoản. Câu mô tả: Issue Prioritization "Prioritizes issues when they're created."; Issue Resolution "Match and resolve issues from completed service."; Service Writer "Drafts Work Orders from open issues and service reminders." | P2 | [Cấu hình] | demo | `Xem`, không bấm | `Xem` | Đối chiếu NFR-006 |
| FR-fleetio-saas-platform-049 | Kết nối ra ngoài | Integration Links (link sang hệ khác kèm biến; cột Label, Record, Status), External Connections (FTP, SFTP, Amazon S3 cho báo cáo định kỳ; cột Name, Type). | P2 | [Gói: Khách lớn, chưa có trong danh sách gói] | demo | `Xem` rỗng | `Xem`, không tạo | Để sau |
| FR-fleetio-saas-platform-050 | Khung trạng thái theo khách | Work Order: Type cố định Incomplete, Completed; khách thêm tên. Purchase Order: 8 trạng thái cố định, không có Add. | P0 | [Lõi] [Cấu hình] | test | `Xem` | `Xem` | Khớp "Lõi khung trạng thái + Cấu hình nhãn" |
| FR-fleetio-saas-platform-051 | Trang báo cáo | Issues Report: biểu đồ Summary, Top Vehicles; Filters, Columns, phân trang; Save, Share, Export CSV (Export Visible Columns, Export All Columns), Print. Bộ lọc 26 ô, nằm trên đường dẫn; ô "Issue Summary" tìm cả tiêu đề lẫn mô tả; biểu đồ và thẻ đếm tính lại theo lọc. Lượt 3 đọc cột thêm 47 báo cáo; lượt 4 đọc nhãn bộ lọc 48 báo cáo, lọc thật 1 báo cáo (FR-065). | P1 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy`, ảnh `report-issues.jpg` | `Chạy` một phần lượt 4: Đọc 48/49, lọc thật 1 | Lấy khung cho `workshop-reports` |
| FR-fleetio-saas-platform-052 | Chia sẻ báo cáo bằng link | Bấm Share sinh ngay link công khai, có hạn (Fleetio: 7 ngày); "this link allows anyone with access to view all data". Reports › Shared liệt kê link và cho Unshare. | P2 | [Cấu hình] | test | `Chạy`, link đã thu hồi | `Chạy` | Học hạn và danh sách thu hồi; KHÔNG học sinh link ngay. Phải bấm tạo mới có link, ghi nhật ký |
| FR-fleetio-saas-platform-053 | Mức ưu tiên tự động của Issue | Issue mới có Priority "Auto-assign"; #40, #42 tự thành High dù không nhập mức. Xếp mức chạy nền: #55 lúc mới tạo hiện "Prioritizing", Record History ghi "Issue Priority Status changed from pending to failed", Issue về "No Priority", không báo ở đâu khác (E-016). | P2 | [Cấu hình] | test | `Chạy` phần thấy được; nguyên nhân AI Issue Prioritization là `Suy` | `Chạy` | Đối chiếu NFR-006; phải ghi nguồn gán |
| FR-fleetio-saas-platform-054 | Hai thế hệ báo cáo, khối cột xe | Thế hệ mới (34 báo cáo) có Save, Share, Export CSV, Print, Filters, Columns, nhiều cái có biểu đồ; thế hệ cũ (15 báo cáo) chỉ thấy Save, Filters, Add Filter. 22 báo cáo thế hệ mới kèm khoảng 110 cột thông tin xe chọn trong Columns, nên người dùng tự ghép bảng rộng. Ngoại lệ không Export CSV: `vehicles/details`, `work_order_status_changes/summary`. | P1 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` mở, đọc 48/49, không bấm trong báo cáo | `Chạy` chỉ đọc 48/49; `expense_entries` lỗi 500 | Lấy khối cột đối tượng gắn sẵn; không để hai thế hệ giao diện |
| FR-fleetio-saas-platform-055 | Báo cáo đã lưu | Hộp New Saved Report: Name *, Description, Visibility Public hoặc Private (mặc định Private), Email Schedule. Reports › Saved cột Name, Description, Report Type, Schedule; menu dòng View Source Report, View Record History, Edit, Make a Copy, Delete; bấm sao vào Favorites. Mở báo cáo đã lưu sang tab mới, giữ bộ lọc. Settings › Saved Reports cột Name, Description, Owner, Visibility, Email Schedule, Created On, Updated On. | P1 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` lưu Private, yêu thích, mở lại; `Xem` trang Settings | `Chạy` một phần: Private; Public, Email Schedule không chạy | Lấy; thêm rõ ai nhận email được gì |
| FR-fleetio-saas-platform-056 | Sửa automation đang bật | Sửa mà chưa lưu: băng cảnh báo "You have unsaved changes on this enabled automation", nút Save thành menu Save Automation, Discard Unsaved Changes. Lưu thì lên phiên bản mới, vẫn Enabled, không hỏi xác nhận lại, hiệu lực ngay; lượt sau ghi Version v.2. | P1 | [Cấu hình] | test | `Chạy` | `Chạy` | Lấy băng cảnh báo; thêm xác nhận vì luật đang chạy trên dữ liệu thật |
| FR-fleetio-saas-platform-057 | Lịch sử phiên bản automation | Version History liệt kê v.2 Current Version và v.1, kèm Created At, Created By; mở một bản ra Step Summary gồm Trigger, Conditions, Actions. Mở v.1 lại hiện nội dung của v.2 (E-018). | P1 | [Cấu hình] | test | `Chạy`, ảnh `automation-version-v1-lech.jpg` | `Chạy` 1 lần sửa nội dung action | Lấy; phải khoá đúng nội dung từng bản |
| FR-fleetio-saas-platform-058 | Make a Copy automation | Mở trình dựng `copy_from`, chưa lưu gì, tên thêm " (copy)", Disabled; rời trang không để lại bản rác. | P1 | [Cấu hình] | demo | `Chạy` | `Chạy` | Lấy |
| FR-fleetio-saas-platform-059 | Automation trên Vehicle | Trigger Created, Updated, Created or Updated; 71 trường điều kiện, không có "Name" nên dùng "Vehicle is any of"; có trường cảm biến Fuel Level, Engine Oil Pressure, Engine Coolant Temp, Battery Voltage, Tire Pressure, Ignition Status, Installed Tires Count, Axle Configuration, Incomplete Work Orders Count. Hành động Update Field (Status, Type, Group, Labels, Axle Configuration), Add Comment, Send Email. Status Updates của xe ghi nguồn "Fleetio Automation" và thời gian ở mỗi trạng thái. | P1 | [Cấu hình] | test | `Chạy` Update Vehicle Status; `Xem` danh sách trường | `Chạy` | Lấy cách ghi nguồn; thêm điều kiện "chỉ khi trường X đổi", báo khi luật ghi đè thao tác tay |
| FR-fleetio-saas-platform-060 | Lượt automation thất bại | Run Result có băng đỏ nguyên văn lỗi, Status FAILURE, Records "No records changed"; danh sách đếm Failed; log từng bước state DNF, status FAILURE, cùng reason, caused_by, thrown_by. Bản ghi không đổi, automation vẫn Enabled, không thấy tự thử lại trong khoảng 5 phút, không báo trên trang bản ghi, chuông (E-011). | P1 | [Cấu hình] | test | `Chạy`, ảnh `automation-run-failure.jpg` | `Chạy` một phần: Failure Notification Email không bật | Lấy câu lỗi nguyên văn, log; thêm màn gom lỗi và báo người tạo |
| FR-fleetio-saas-platform-061 | Cài đặt thông báo cá nhân | Email, Mobile App bật tắt chung; 18 nhóm sự kiện, mỗi sự kiện cột Email, Push; "You are watching 20 vehicles"; tự theo dõi xe mới, bản ghi mới, nhắc có sẵn. Email tắt chung vẫn không tắt "essential communications, Saved Reports, Inspection Workflows, Automation Alerts or Notification Profiles". | P1 | [Cấu hình] | demo | `Xem` | `Xem`, không lưu | Lấy; nói rõ loại không tắt được |
| FR-fleetio-saas-platform-062 | Gắn tài liệu vào xe | Select Vehicles mở "Attach Document to Vehicles": tìm, Attached Vehicles, All Vehicles, Vehicle Types, Groups; gắn xong nút thành "Attached", trang tệp ghi Attached to "1 Vehicle". Gắn theo loại, nhóm có trên hộp, chưa bấm. | P2 | [Cấu hình] | demo | `Chạy` gắn 1 xe; `Xem` loại, nhóm | `Chạy` một phần: Gắn 1 xe | Lấy cho giấy tờ chung của cả đội đầu kéo |
| FR-fleetio-saas-platform-063 | Mở truy cập từ liên hệ | Chọn Enable Access: "This Contact will be enabled as a User...", Login Information gồm Email, Delay email invitation, Message; Role * mặc định Fleet Manager; Notification Profile; Watched Vehicle Groups; Record Sets cho Vehicles, Tools, Contacts, Part Locations, Inspection Forms đều mặc định Full Access. | P0 | [Lõi] [Cấu hình] | test | `Xem` form, không lưu | `Xem`, không lưu | Lấy luồng; đảo mặc định về quyền thấp nhất (NFR-014) |
| FR-fleetio-saas-platform-064 | Danh mục tích hợp | Trang `integrations/my-integrations`: Data Connectors 6, Fuel Cards 9, Fuel Management 5, Key Management 1, Operations 1, Telematics 43, Tire Management 1, Tolls & Citations 2. | P2 | [Gói: Khách lớn, chưa có trong danh sách gói] | demo | `Xem` | `Xem` | Tham khảo độ phủ telematics |
| FR-fleetio-saas-platform-065 | Ba kiểu bộ lọc báo cáo | Kiểu A: panel ô cố định, nút Search, đa số báo cáo mới. Kiểu B: filter builder "No filters applied.", Add Filter, Popular Filters như danh sách thường, 9 báo cáo. Kiểu C: thanh lọc ngay trên báo cáo, Add Filter, Apply, 4 báo cáo. `job_assignments_summary_by_job` không lọc được, chỉ có Save. Từng báo cáo ở Mục 21.3. | P1 | [Gói: Bảo dưỡng đội xe] | demo | `Chạy` đọc nhãn, lọc thật `purchase_orders` | `Chạy` một phần: Đọc nhãn, lọc thật 1 báo cáo; `expense_entries` lỗi 500 | Lấy khối ô xe dùng chung; chỉ giữ một kiểu bộ lọc |

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
| NFR-fleetio-saas-platform-008 | giới hạn vòng lặp tự động hoá | Đề xuất Invlogis: đặt trần lượt chạy theo khách (tham số mới, chưa có mã). Fleetio không nêu giới hạn; Issue thấy dừng khi giá trị không đổi, Vehicle không sinh lượt mới do chính automation đổi xe; vòng lặp chéo chưa chạy (OQ-5). | P1 | Ca hai automation lật giá trị phải dừng ở trần |
| NFR-fleetio-saas-platform-009 | truy vết nguồn gây ra | Đề xuất Invlogis: lượt do automation gây ra phải ghi automation là nguồn, không ghi người thật; kết quả phải phản ánh cả comment đã thêm. Fleetio không đạt. | P1 | Đọc lịch sử phân biệt được người và máy |
| NFR-fleetio-saas-platform-010 | chia sẻ ra ngoài | Đề xuất Invlogis: mở hộp không sinh link; có bước tạo chủ động, nói rõ phạm vi dữ liệu; thu hồi có hiệu lực ngay ở mọi lối; ghi nhật ký tạo, mở, thu hồi. Fleetio không đạt. | P0 | Mở hộp rồi đóng không tồn tại link nào; thu hồi xong mở lại không còn dữ liệu |
| NFR-fleetio-saas-platform-011 | độ tin của câu trả lời AI | Đề xuất Invlogis: mọi số do AI trả phải ghi "dữ liệu đến thời điểm" và lối đối chiếu về bản ghi gốc. Fleetio không đạt: khẳng định "currently" với số lệch, khẳng định xe "does not exist" khi xe có thật, đẩy câu hỏi ngày dữ liệu sang "your system's data pipeline or integration settings". | P0 | Câu trả lời số luôn có thời điểm dữ liệu; bản ghi chưa vào kho thì nói "chưa có dữ liệu", không nói "không tồn tại" |
| NFR-fleetio-saas-platform-012 | báo lỗi tự động hoá | Đề xuất Invlogis: lượt thất bại phải báo tới người tạo luật và hiện trên bản ghi liên quan, có màn gom lỗi toàn bộ luật. Fleetio không đạt nếu chưa bật email. | P1 | Lượt lỗi có thông báo trong app mà không cần cấu hình thêm |
| NFR-fleetio-saas-platform-013 | luật ghi đè thao tác tay | Đề xuất Invlogis: luật đổi lại giá trị người vừa sửa phải báo ngay cho người đó, nêu luật nào. Fleetio không đạt: lật lại sau 1 giây, màn người dùng không báo gì. | P1 | Người sửa thấy thông báo nêu tên luật |
| NFR-fleetio-saas-platform-014 | quyền mặc định khi mở truy cập | Đề xuất Invlogis: mở người dùng mới mặc định vai và phạm vi thấp nhất, nâng lên phải chọn. Fleetio không đạt: mặc định Fleet Manager, Full Access. | P0 | Người dùng mới không chọn gì thì không thấy dữ liệu ngoài phạm vi |
| NFR-fleetio-saas-platform-015 | tìm và nhắc tên tiếng Việt | Đề xuất Invlogis: tìm, nhắc tên khớp cả khi gõ không dấu, có gạch nối. Fleetio không đạt ở ô @. | P1 | Gõ không dấu ra đúng người có dấu |

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
| BR-fleetio-saas-platform-011 | Trên Issue, automation tự kích hoạt lại khi chính nó đổi bản ghi, rồi dừng khi giá trị không đổi. Trên Vehicle, lượt do automation đổi xe không sinh lượt mới; khác biệt chưa giải thích được (OQ-17). | [Cấu hình] | Created or Updated, Updated | FR-fleetio-saas-platform-034 | `Chạy` Issue 2 lượt, Vehicle Total Runs 2 cho đúng 2 lần người sửa; giới hạn vòng lặp chéo chưa biết | `Chạy` |
| BR-fleetio-saas-platform-012 | "Triggered By" ghi người tạo bản ghi, kể cả lượt do automation gây ra. | [Cấu hình] | Ghi lượt chạy | FR-fleetio-saas-platform-034 | `Chạy`, ảnh `automation-self-trigger-runs.jpg` | `Chạy` |
| BR-fleetio-saas-platform-013 | Run Result ghi "Records: No records changed" ở cả ba loại lượt đã đo: lượt thêm comment, lượt đã đổi Status xe thật, lượt thất bại. Câu này chỉ khớp sự thật ở lượt thất bại (WO giữ nguyên), nên nhãn không đáng tin (E-021). Lượt đổi xe là theo run-notes; ảnh `automation-vehicle-status-flip.jpg` chỉ chụp Status Updates, không chụp Run Result. | [Cấu hình] | Ghi lượt chạy | FR-fleetio-saas-platform-034 | `Chạy`, ảnh `automation-run-result.jpg`, `automation-run-failure.jpg` | `Chạy` |
| BR-fleetio-saas-platform-014 | Hành động tạo Work Order không có Status Completed. | [Cấu hình] | Create Record | FR-fleetio-saas-platform-036 | `Chạy` hộp chỉ có Open, Pending | `Chạy` |
| BR-fleetio-saas-platform-015 | Archive tắt automation ngay, không cần tắt trước. Restore về Disabled, không tự bật. Bản Archived chỉ đọc. | [Cấu hình] | Archive, Restore | FR-fleetio-saas-platform-033 | `Chạy` | `Chạy` |
| BR-fleetio-saas-platform-016 | Hết hạn mức xe thì không tạo được, kể cả khi đủ trường bắt buộc; bản ghi Sample không tính vào hạn mức. | [Lõi] [Cấu hình] | Lưu xe | FR-fleetio-saas-platform-023 | `Chạy` | `Chạy` |
| BR-fleetio-saas-platform-017 | Chỉ liên hệ có tick Operator mới gán được xe; chỉ Technician mới được chọn ở dòng công lệnh sửa. | [Lõi] | Gán xe, ghi công | FR-fleetio-saas-platform-038 | `Chạy` khối gán xe chặn; Technician theo câu trên màn là `Xem` | `Chạy` Operator, `Xem` Technician |
| BR-fleetio-saas-platform-018 | Liên hệ chỉ cần First Name; trùng tên vẫn lưu, không cảnh báo. No Access thì không vào hệ thống, không nhận thông báo. | [Lõi] | Lưu liên hệ | FR-fleetio-saas-platform-038 | `Chạy` | `Chạy` |
| BR-fleetio-saas-platform-019 | Record Type của Record Set không đổi sau khi tạo; bản mặc định bị khoá sửa. | [Lõi] | Sửa Record Set | FR-fleetio-saas-platform-046 | `Xem` | `Xem` |
| BR-fleetio-saas-platform-020 | Record Set không có điều kiện theo thời gian (ca trực, thời hạn). | [Lõi] | Khai Record Set | FR-fleetio-saas-platform-046 | `Xem` danh sách 8 điều kiện | `Xem` |
| BR-fleetio-saas-platform-021 | Require Group chỉ mở khi mọi tài sản và liên hệ đã gán nhóm. | [Cấu hình] | Bật Require Group | FR-fleetio-saas-platform-040 | `Xem` khoá, liệt kê số thiếu | `Xem` |
| BR-fleetio-saas-platform-022 | Trạng thái xe đổi tự do bằng trường Status hoặc automation, không có luật chuyển; cần quyền `vehicles_update_status`. Lượt 3 đã đổi thật Active sang Inactive và ngược lại. | [Lõi] [Cấu hình] | Đổi trạng thái | FR-fleetio-saas-platform-041 | `Chạy` trên TEST-DAUKEO-2; quyền và không có luật chuyển là `Xem` | `Chạy` Active, Inactive; `Xem` phần còn lại |
| BR-fleetio-saas-platform-023 | Work Order về Type Completed thì cập nhật nhắc bảo dưỡng và giải quyết Issue liên quan. | [Lõi] | Hoàn tất lệnh | FR-fleetio-saas-platform-050 | `Xem` câu trên màn; hành vi thật xem nhóm Sửa chữa | `Xem` |
| BR-fleetio-saas-platform-024 | Trạng thái Purchase Order cố định, khách không thêm. | [Lõi] | Cấu hình | FR-fleetio-saas-platform-050 | `Xem` không có nút Add | `Xem` |
| BR-fleetio-saas-platform-025 | Chính sách mật khẩu áp khi tạo hoặc đặt lại mật khẩu, không áp SAML. | [Lõi] [Cấu hình] | Đổi mật khẩu | FR-fleetio-saas-platform-047 | `Xem` | `Xem` |
| BR-fleetio-saas-platform-026 | Bản xuất toàn bộ gửi qua email; link hết hạn (Fleetio: 7 ngày). | [Gói: Khách lớn, chưa có trong danh sách gói] | Export Account Data | FR-fleetio-saas-platform-029 | `Xem` câu trên màn | `Xem` |
| BR-fleetio-saas-platform-027 | Mở hộp Share là sinh link công khai, không hỏi trước; ai có link xem được dữ liệu; hết hạn (Fleetio: 7 ngày). | [Cấu hình] | Bấm Share | FR-fleetio-saas-platform-052 | `Chạy` | `Chạy`; hết hạn thật chưa chờ |
| BR-fleetio-saas-platform-028 | Chỉ Unshare ở Reports › Shared mới thu hồi được; lối "click here to unshare" trong hộp không có tác dụng. | [Cấu hình] | Thu hồi | FR-fleetio-saas-platform-052 | `Chạy` | `Chạy` |
| BR-fleetio-saas-platform-029 | AI Data Analyst khẳng định số mà không ghi dữ liệu tính đến lúc nào; hỏi trực tiếp thì trả lời bộ dữ liệu không có trường ngày làm mới. Bản ghi chưa vào kho bị nói là "does not exist". | [Lõi] | Hỏi dữ liệu | FR-fleetio-saas-platform-020 | `Chạy`; nguyên nhân kho phân tích trễ là `Suy`, chưa giải thích #49, #51 | `Chạy` |
| BR-fleetio-saas-platform-030 | Cảnh báo Location Exception bật khi phiếu nộp từ một chỗ theo ngưỡng (Fleetio: 80%, 100 m). | [Cấu hình] | Nộp phiếu | FR-fleetio-saas-platform-003 | `Xem` Inspection Settings | `Xem` |
| BR-fleetio-saas-platform-031 | Thiếu giá trị trong mẫu thì trình dựng hiện "Missing Value" hoặc để trống; người dùng phải chọn trước khi lưu. | [Cấu hình] | Apply mẫu | FR-fleetio-saas-platform-031 | `Chạy` hiện; không lưu để kiểm chặn | `Chạy` phần hiện |
| BR-fleetio-saas-platform-032 | Lưu bản sửa của automation đang bật thì lên phiên bản mới, vẫn Enabled, không hỏi xác nhận lại, hiệu lực ngay. | [Cấu hình] | Lưu bản sửa | FR-fleetio-saas-platform-056 | `Chạy` Issue #55 chạy theo v.2 | `Chạy` |
| BR-fleetio-saas-platform-033 | Tắt rồi bật lại mà không sửa thì giữ phiên bản, chỉ đổi Enabled At. | [Cấu hình] | Bật lại | FR-fleetio-saas-platform-032 | `Chạy` vẫn v.1 | `Chạy` |
| BR-fleetio-saas-platform-034 | Trigger Updated chạy trên MỌI thay đổi của bản ghi, không chọn được "khi trường X đổi". | [Cấu hình] | Sửa bản ghi | FR-fleetio-saas-platform-059 | `Chạy` sửa Color cũng kích hoạt | `Chạy` |
| BR-fleetio-saas-platform-035 | Automation đang bật được ghi đè thao tác tay ngay sau đó; người sửa không nhận cảnh báo nào. | [Cấu hình] | Người sửa bản ghi | FR-fleetio-saas-platform-059 | `Chạy` 1 giây sau đổi lại, ảnh `automation-vehicle-status-flip.jpg` | `Chạy` |
| BR-fleetio-saas-platform-036 | Hành động automation chịu cùng kiểm tra nghiệp vụ như form tay: Update Field Status cho chọn Completed, nhưng WO thiếu Start Date thì lượt thất bại, bản ghi giữ nguyên. | [Lõi] [Cấu hình] | Hành động đổi trạng thái | FR-fleetio-saas-platform-060 | `Chạy` WO #111 | `Chạy` |
| BR-fleetio-saas-platform-037 | Hạn mức Automations chỉ đếm bản đang bật. | [Lõi] [Cấu hình] | Đếm hạn mức | FR-fleetio-saas-platform-023 | `Chạy` lượt 4 bật AUTO-07, đọc 1 of 75 khi lưu 10 bản; lượt 3 đọc 0 of 75 khi 7 bản đều tắt | `Chạy` |
| BR-fleetio-saas-platform-038 | Lượt thất bại không thấy tự thử lại trong khoảng 5 phút, không làm automation tự tắt, không báo trong app; biết lỗi qua Run History hoặc email nếu đã bật. | [Cấu hình] | Hành động lỗi | FR-fleetio-saas-platform-060 | `Chạy`; email không bật | `Chạy` |
| BR-fleetio-saas-platform-039 | Ô @ chỉ khớp đúng ký tự: không khớp khi bỏ dấu hoặc có gạch nối; không khớp thì đăng thành chữ thường, không tạo mention. | [Lõi] | Viết comment | FR-fleetio-saas-platform-017 | `Chạy` | `Chạy` |
| BR-fleetio-saas-platform-040 | Comment, Watch không ghi vào Record History. | [Lõi] | Comment, Watch | FR-fleetio-saas-platform-022 | `Chạy` | `Chạy` |
| BR-fleetio-saas-platform-041 | View chuẩn "Fleetio Standard View" bị khoá; muốn giữ thay đổi phải Save as New View. | [Lõi] | Lưu view | FR-fleetio-saas-platform-010 | `Chạy` | `Chạy` |
| BR-fleetio-saas-platform-042 | Thông báo in-app của người theo dõi chạy kể cả khi tài khoản có 0 hồ sơ thông báo. Tắt email chung không tắt essential communications, Saved Reports, Inspection Workflows, Automation Alerts, Notification Profiles. | [Cấu hình] | Có sự kiện | FR-fleetio-saas-platform-018 | `Chạy` Inbox có Fuel Capacity Alert, ảnh `notifications-inbox.jpg`; câu về email là `Xem` | `Chạy` in-app, `Xem` email |
| BR-fleetio-saas-platform-043 | Mở truy cập cho liên hệ mặc định Role Fleet Manager, Record Sets đều Full Access, gửi email mời ngay trừ khi chọn Delay email invitation. | [Lõi] [Cấu hình] | Enable Access | FR-fleetio-saas-platform-063 | `Xem` form, không lưu | `Xem` |
| BR-fleetio-saas-platform-044 | Saved Report Private chỉ người tạo thấy, nhưng gửi email được cho bất kỳ ai có quyền với báo cáo gốc: "Private Saved Reports are visible only to you, but can be emailed to anyone with access to the source report." | [Cấu hình] | Lưu báo cáo | FR-fleetio-saas-platform-055 | `Xem` câu trên hộp, Private `Chạy`; không gửi email | `Xem` |
| BR-fleetio-saas-platform-045 | Session Timeout: Fleetio Go có Never, Fleetio Web không có Never (Fleetio: Go Never, 15, 30 phút, 1, 12, 24 giờ, 2 tuần; Web 15 phút đến 2 tuần). | [Lõi] [Cấu hình] | Hết phiên | FR-fleetio-saas-platform-047 | `Xem` | `Xem` |
| BR-fleetio-saas-platform-046 | API key thu hồi rồi không kích hoạt lại được; Account Tokens có Rate Limit (Fleetio: 250 requests/minute). | [Gói: Khách lớn, chưa có trong danh sách gói] | Quản lý khoá | FR-fleetio-saas-platform-028 | `Xem` câu trên màn, không tạo khoá | `Xem` |
| BR-fleetio-saas-platform-047 | Mẫu automation đổi ngưỡng theo tiền tệ khách nhưng câu email giữ số cứng (Fleetio: ngưỡng 100.000 ₫, câu ghi ">$1,000.00"), sửa ngưỡng không sửa câu. | [Cấu hình] | Apply mẫu | FR-fleetio-saas-platform-014 | `Chạy` mở mẫu, không lưu | `Chạy` mở mẫu |
| BR-fleetio-saas-platform-048 | AI xếp mức thất bại thì Issue về "No Priority", dòng lịch sử ghi Changes By là người tạo Issue, không phải máy. | [Cấu hình] | Xếp mức nền | FR-fleetio-saas-platform-053 | `Chạy` Issue #55, ảnh `record-history-issue.jpg`; nguyên nhân lỗi chưa biết | `Chạy` |
| BR-fleetio-saas-platform-049 | Tệp có Auto-Delete thì xoá cuối ngày đã chọn. | [Cấu hình] | Đặt Auto-Delete | FR-fleetio-saas-platform-024 | `Xem` câu giải thích, không đặt | `Xem` |
| BR-fleetio-saas-platform-050 | Lưu lại bản ghi không đổi gì thì không tính Updated, không sinh lượt. | [Cấu hình] | Lưu bản ghi | FR-fleetio-saas-platform-013 | `Chạy` Purchase Order #5, 0 lượt | `Chạy` |
| BR-fleetio-saas-platform-051 | Automation đổi Status đơn mua sang Approved bắt buộc có điều kiện Purchase Order Status là Pending Approval: tự động chỉ xử lý đơn đã nộp duyệt, không bỏ qua bước nộp được. | [Lõi] [Cấu hình] | Lưu automation | FR-fleetio-saas-platform-013 | `Chạy` bị chặn lúc lưu; nhánh duyệt tự động thật cần người thứ hai, chưa chạy | `Chạy` phần chặn |
| BR-fleetio-saas-platform-052 | Comment do automation thêm không kích lại automation đó. | [Cấu hình] | Add Comment | FR-fleetio-saas-platform-034 | `Chạy` Purchase Order #5, Total Runs 1 | `Chạy` |
| BR-fleetio-saas-platform-053 | Bản Archived không chạy khi bản ghi khớp đổi; Restore không tự bật lại dù trước đó Enabled, giữ v.1 và Run History. | [Cấu hình] | Archive, Restore | FR-fleetio-saas-platform-033 | `Chạy` AUTO-08 | `Chạy` |
| BR-fleetio-saas-platform-054 | Update Field Repair Priority Class của Service Entry chọn và Apply được nhưng bị từ chối lúc lưu; chỉ thử 1 giá trị Emergency, hãng không nêu lý do. | [Cấu hình] | Lưu automation | FR-fleetio-saas-platform-013 | `Chạy` | `Chạy` |
| BR-fleetio-saas-platform-055 | Automation trên Fault chỉ có sự kiện Created; Fault sinh từ thiết bị telematics, không tạo tay được. | [Cấu hình] | Tạo automation | FR-fleetio-saas-platform-013 | `Chạy` lưu AUTO-09 Disabled; lượt thật bị chặn vì xe TEST không có thiết bị | `Chạy` phần lưu |
| BR-fleetio-saas-platform-056 | Báo cáo đơn mua cộng cả đơn Draft vào Total Amount, không phân biệt mặc định. | [Gói: Bảo dưỡng đội xe] | Xem báo cáo | FR-fleetio-saas-platform-065 | `Chạy` lọc Vendor `TEST-NCC-01`, 2 dòng gồm Draft #5 | `Chạy` |

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
| E-fleetio-saas-platform-011 | Lượt automation thất bại | "Automation Action failed: Start Date can't be blank" khi WO thiếu Start Date bị đổi sang Completed. Lượt 2 không tái hiện được, lượt 3 có | major | FR-fleetio-saas-platform-060 | Băng đỏ trong Run Result, nhãn FAILURE, Failed 1; trang bản ghi và chuông không có gì | Vào Run History đọc lỗi, sửa dữ liệu; lượt không tự chạy lại | `Chạy`, email không bật |
| E-fleetio-saas-platform-012 | AI trả số sai, không báo lỗi | Trả "currently has 2 open issues" khi thật là 7; "1,700.0" khi thật là 2.999 km; lượt 3 "has 10 open issues" khi thật là 12 | critical | FR-fleetio-saas-platform-020 | Câu trả lời bình thường, không có cảnh báo | Đối chiếu tay trên trang xe; có Show work | `Chạy` |
| E-fleetio-saas-platform-013 | Link công khai sinh ngoài ý muốn | Bấm Share là có link, không có bước xác nhận | critical | FR-fleetio-saas-platform-052 | Hộp Share có sẵn link | Thu hồi ở Reports › Shared | `Chạy` |
| E-fleetio-saas-platform-014 | Báo cáo lỗi máy chủ | "We're sorry, but something went wrong." ở `reports/expense_entries`, lượt 3 mở 2 lần, lượt 4 vẫn lỗi; chân trang "Partially Degraded Service"; có thể sự cố tạm của hãng, chưa thử lại sau | major | FR-fleetio-saas-platform-019 | Trang lỗi 500 riêng, có Go back, contact us, status page | Quay lại, thử lại sau | `Chạy` |
| E-fleetio-saas-platform-015 | AI khẳng định xe không tồn tại | "Vehicle TEST-DAUKEO-2 does not exist in the issues dataset with that exact name" · "No issues have been recorded for this vehicle" khi xe và Issue #54, #55 có thật | critical | FR-fleetio-saas-platform-020 | Câu trả lời bình thường, hỏi lại có gõ đúng tên không | Đối chiếu tay trên trang xe | `Chạy` |
| E-fleetio-saas-platform-016 | AI xếp mức thất bại im lặng | "Issue Priority Status changed from pending to failed", Issue về "No Priority" | major | FR-fleetio-saas-platform-053 | Chỉ một dòng trong Record History, không báo ra đâu khác | Tự chọn mức tay; không có lối thử lại đã thấy | `Chạy` |
| E-fleetio-saas-platform-017 | Luật lật ngược thao tác tay | Người đổi Status về Active, 1 giây sau automation đổi lại Inactive | major | FR-fleetio-saas-platform-059 | Màn người dùng không báo gì; chỉ thấy trong Status Updates | Tắt hoặc sửa automation | `Chạy` |
| E-fleetio-saas-platform-018 | Lịch sử phiên bản hiện sai nội dung | Mở v.1 trong Version History, màn ghi "Step Summary v.1" nhưng hiện chữ của v.2 | major | FR-fleetio-saas-platform-057 | Hộp Version History | Chưa có; thấy 1 lần, chưa thử sửa điều kiện (OQ-16) | `Chạy` |
| E-fleetio-saas-platform-019 | Mẫu email sai số tiền | Câu email cố định ">$1,000.00" trong khi điều kiện là 100.000 ₫ | minor | FR-fleetio-saas-platform-014 | Khối Send Email của mẫu | Sửa tay nội dung trước khi lưu | `Chạy` mở mẫu, không lưu |
| E-fleetio-saas-platform-020 | Nhắc tên không ra người | Gõ @ không dấu hoặc có gạch nối không ra liên hệ; đăng thành chữ thường, không báo | minor | FR-fleetio-saas-platform-017 | Danh sách @ không có dòng khớp | Gõ đúng dấu | `Chạy` |
| E-fleetio-saas-platform-021 | Kết quả lượt chạy ghi sai | "Records: No records changed" khi đã thêm comment hoặc đã đổi Status xe | major | FR-fleetio-saas-platform-034 | Run Result, trạng thái thành công | Xem View Full Log hoặc lịch sử bản ghi | `Chạy` |
| E-fleetio-saas-platform-022 | Tài liệu vừa tải chưa hiện | Sau "Document was successfully added." danh sách vẫn "No results to show" | minor | FR-fleetio-saas-platform-024 | Danh sách Documents | Tải lại trang | `Chạy` |
| E-fleetio-saas-platform-023 | Tệp không xem trước được | Khung xem PDF hiện 0 trang với tệp .txt, không có câu giải thích | minor | FR-fleetio-saas-platform-024 | Trang tệp | Download | `Chạy` |
| E-fleetio-saas-platform-025 | Automation không lưu được | "Automation could not be created. Please resolve any errors try again.", khối Actions "action is missing" · "is invalid" khi Update Field Repair Priority Class = Emergency trên Service Entry | major | FR-fleetio-saas-platform-013 | Sau bấm Save, nút "Fix Errors"; lúc chọn không báo | Đổi hành động | `Chạy` |
| E-fleetio-saas-platform-026 | Tự duyệt đơn mua thiếu điều kiện | Cảnh báo cam "This Trigger and Action set requires a specific Condition. To ensure a successful automation, add a Condition on Purchase Order Status for Pending Approval."; lưu vẫn chặn "Purchase Order Status "Pending Approval" is required" | minor | FR-fleetio-saas-platform-013 | Ngay trong panel và lúc Save, nút "Resolve error" | Thêm điều kiện | `Chạy` |
| E-fleetio-saas-platform-027 | Báo cáo đơn mua sai số gộp, lệch thang | Total Amount gồm cả đơn Draft; biểu đồ "Total by Vendor" trục chỉ 20k trong khi tổng 3,5 triệu ở VND | major | FR-fleetio-saas-platform-065 | Trang `purchase_orders` sau khi lọc, không có cảnh báo | Thêm lọc Status, đọc bảng thay biểu đồ (`Suy`) | `Chạy` |
| E-fleetio-saas-platform-024 | Tab kẹt khi rời form chưa lưu | Rời mẫu automation hoặc form New Contact bằng Cancel, hộp "Leave site?" làm tab kẹt | minor | FR-fleetio-saas-platform-031 | Hộp của trình duyệt | Đóng tab; lượt 3 còn một tab không đóng được, nguyên nhân có thể do công cụ chạy thử | `Chạy` |

## 7. Success Criteria

| ID | Outcome nghiệp vụ | Đo bằng | Mốc đạt |
|---|---|---|---|
| SC-fleetio-saas-platform-01 | Khách thứ hai chạy không sửa lõi | Số yêu cầu phải sửa code | 0 cho luật có tham số |
| SC-fleetio-saas-platform-02 | Người mới tự làm được | Thời gian tới bản ghi đầu tiên | TBD |
| SC-fleetio-saas-platform-03 | Không lộ dữ liệu ngoài phạm vi | Ca kiểm thử Role và Record Set | 100% đạt |

## 8. Data Entities (tóm tắt — chi tiết ở erd.md)

Account, Plan Limit, Contact, User, Group, Role, Role Permission, Record Set, Saved View, Automation, Automation Version, Automation Run, Automation Template, Dashboard, Custom Field, Custom Record Type, Webhook, Report, Saved Report, Report Share Link, AI Conversation, Recall, Motor Pool, Reservation, Document, Document Attachment, Notification, Notification Profile, Watch, Comment, API Key. Xem [[docs/_research/fleetio/srs/fleetio-saas-platform-erd.md|ERD]].

## 9. Flows (tóm tắt — chi tiết ở flows.md)

Xem [[docs/_research/fleetio/srs/fleetio-saas-platform-flows.md|Flows]], [[docs/_research/fleetio/srs/fleetio-saas-platform-states.md|States]], [[docs/_research/fleetio/srs/fleetio-saas-platform-usecases.md|Use case]], [[docs/_research/fleetio/srs/fleetio-saas-platform-userflow.md|User flow]].

## 10. Screens

Ảnh thật và bảng mô tả: [[docs/_research/fleetio/srs/fleetio-saas-platform-screens.md|Màn hình]]. Không áp `CMP`, `GR` vì mô tả sản phẩm của bên khác.

## 11. Constraints, Dependencies & Assumptions

| Giả định | Invalidate nếu sai |
|---|---|
| `GĐ` Role, Record Set của Fleetio chưa đủ cấp Công ty, Chi nhánh, Cơ sở, và chưa có quyền có thời hạn theo việc, ca trực. Lượt chạy thấy (`Xem`): cấp Chi nhánh dùng được qua Group nhiều cấp; Công ty, Cơ sở phải tự xếp thành cây Group; không có điều kiện theo thời gian | Cần thêm một lớp phạm vi |
| `GĐ` Giai đoạn đầu chỉ cần luật có tham số, chưa cần công cụ tự động hoá. Lượt chạy thấy (`Chạy`): mẫu đủ dùng với luật đơn giản, không thấy chống vòng lặp, luật ghi đè thao tác tay không báo, lỗi im lặng nếu không bật email, nên công cụ tổng quát có rủi ro | Phải đưa FR-012 lên P0 |

**Ghi chú nhãn:** "Gói: Khách lớn" là tên tạm do người viết đặt, cần chốt khi review.

**Giới hạn bằng chứng về quyền:** ma trận Mục 15, Mục 16 đọc từ màn cấu hình; chưa đăng nhập bằng vai khác nên chưa biết hệ thống có chặn đúng như khai không.

**Nối với `docs/_product/saas-core-vs-tenant.md`:** Vehicle hay Asset ứng với từ điển thuật ngữ theo khách; Work Order Statuses (khung Type cố định, khách thêm tên) khớp đúng "Lõi khung trạng thái + Cấu hình nhãn"; Require Meter + Excluded Vehicle Types là mẫu cho loại xe không đồng hồ như mooc; PO Statuses cố định là ví dụ phần không cho khách đổi.

## 12. Open Questions

* [x] OQ-1: Role và Record Set có khớp Công ty, Chi nhánh, Cơ sở không? Trả lời (`Xem`): khớp Chi nhánh bằng Group nhiều cấp + "Vehicles in this contact's group"; Công ty, Cơ sở phải tự xếp thành cây Group; không có quyền theo thời hạn. Hiệu lực thật chuyển sang OQ-8. — Nguồn khách: chưa có trong tài liệu khách gửi
* [ ] OQ-2: Có cần công cụ tự động hoá tổng quát giai đoạn đầu không? Thông tin mới (`Chạy`): mẫu đủ dùng với luật đơn giản, không thấy chống vòng lặp nên công cụ tổng quát có rủi ro; đây là quyết định của đội sản phẩm. — Nguồn khách: câu hỏi nội bộ
* [ ] OQ-3: Dữ liệu mẫu cho khách mới lấy từ đâu mà không lộ dữ liệu Delta? — Nguồn khách: câu hỏi nội bộ
* [ ] OQ-4: Tên gói cho API, SAML, sandbox? Thông tin mới (`Xem`): Fleetio tách Sandbox, MCP theo hạn mức gói; tên gói của Invlogis vẫn phải chốt. — Nguồn khách: câu hỏi nội bộ
* [ ] OQ-5: Hai automation lật giá trị của nhau có bị chặn không, giới hạn bao nhiêu lượt? Tài liệu hãng không nêu, chưa chạy. Lượt 3 KHÔNG chạy: thử chéo có thể lặp không biết giới hạn trên hệ thống thật; thông tin liên quan: lượt do AUTO-05 đổi xe không sinh lượt mới (`Chạy`). — Nguồn khách: câu hỏi nội bộ
* [ ] OQ-6: Lượt automation thất bại trông thế nào, có thử lại không, Failure Notification Email gửi gì? Một phần lượt 3: lỗi "Automation Action failed: Start Date can't be blank", log từng bước, không thử lại trong khoảng 5 phút, không tự tắt, không báo trong app (`Chạy`). Còn mở: nội dung email vì không gửi email. — Nguồn khách: câu hỏi nội bộ
* [ ] OQ-7: Sửa automation đang bật có sinh v.2 không; Make a Copy, Delete, trigger Vehicle, hành động Update Vehicle Status, Run Summary Email, Send Email chạy ra sao? Một phần lượt 3: sửa khi bật lên v.2, chạy theo v.2, Make a Copy mở bản chưa lưu, trigger Vehicle và Update Vehicle Status chạy (`Chạy`); Run Summary Email chỉ đọc câu mô tả (`Xem`). Còn mở: Delete, Run Summary Email, Send Email. — Nguồn khách: câu hỏi nội bộ
* [ ] OQ-8: Role và Record Set có chặn đúng như khai không? Cần mời người dùng thử theo từng vai. Lượt 3 không chạy được: cần người dùng thứ hai, không mời người. — Nguồn khách: câu hỏi nội bộ
* [x] OQ-9: Technician có quyền gì với Fuel Entries? Ma trận ghi "không", ghi chú cùng lượt ghi "chỉ có ô xem". Cần mở lại Edit Role để chốt. Trả lời lượt 3: Role Technician có Fuel Entries chọn None, không có ô con; ghi chú cũ "chỉ có ô xem" sai (`Xem`, không lưu) — Nguồn khách: câu hỏi nội bộ
* [x] OQ-10: Settings có bao nhiêu trang? Bản 02/11 ghi khoảng 65, tiêu đề ghi chú chạy ghi khoảng 45, bảng chạy kê 56 tên trang. Mục 14 theo bảng chạy; chưa đếm lại trên menu. Trả lời lượt 3: menu có 67 link = 59 trang cấp tài khoản + 7 trang cá nhân + Log Out (`Xem`) — Nguồn khách: câu hỏi nội bộ
* [ ] OQ-11: Cột và lọc của 48 báo cáo còn lại, Saved Reports là gì? Một phần lượt 3: đủ 49 tên, cột 48 báo cáo ở Phụ lục báo cáo chuẩn; Saved Reports là bộ lọc và cột của báo cáo chuẩn lưu lại, kèm Private hoặc Public và lịch gửi email (`Chạy`). Lượt 4: nhãn bộ lọc 48 báo cáo ở Mục 21.3, 3 kiểu (`Chạy` đọc, lọc thật `purchase_orders`). Còn mở: `expense_entries` lỗi 500 lần 3 nên chưa có cột, bộ lọc; 3 báo cáo đọc "0 dòng" có thể chưa kịp tải. — Nguồn khách: câu hỏi nội bộ
* [ ] OQ-12: Đổi trạng thái xe thật, Archive xe, Restore xe, xe trùng tên, Motor Pool chạy thế nào? Một phần lượt 3: đổi Status thật Active, Inactive trên `TEST-DAUKEO-2` (`Chạy`). Còn mở: Archive, Restore, xe trùng tên cần một chỗ xe (đang 5 of 5); Motor Pool cần tạo trong Settings, ngoài phạm vi. — Nguồn khách: câu hỏi nội bộ
* [ ] OQ-13: AI Data Analyst sai vì kho phân tích trễ hay vì cách đếm? Mới là `Suy`, mạnh hơn sau lượt 3: lượt trước khoảng 15 giờ trước trả 2 (thật 7), lượt này 10 (thật 12); xe tạo trong ngày chưa có trong kho. Chưa giải thích được: #50 có mà #49 không nên không phải cắt theo thời điểm đơn giản; #51 có Priority High nên không do thiếu mức ưu tiên. — Nguồn khách: câu hỏi nội bộ
* [x] OQ-14: Mẫu Send Email When A Work Order Total Exceeds Amount có trigger, điều kiện gì? Trả lời lượt 3: trigger Work Order Created or Updated; điều kiện Work Order Total Cost ≥ 100.000 ₫; Send Email, Recipient(s) tự điền người đang đăng nhập; mẫu viết cứng ">$1,000.00" (`Chạy` mở mẫu, không lưu) — Nguồn khách: câu hỏi nội bộ
* [ ] OQ-15: Vì sao Odometer trong Financial của form xe hiện "mi" khi Specifications hiện cm, kg, lít? Chưa rõ. — Nguồn khách: câu hỏi nội bộ
* [ ] OQ-16: Version History hiện nội dung v.2 khi mở v.1 là lỗi chung hay chỉ khi sửa nội dung action? Mới thấy 1 lần, chưa thử sửa điều kiện. — Nguồn khách: câu hỏi nội bộ
* [ ] OQ-17: Vì sao automation đổi Issue sinh thêm lượt còn automation đổi Vehicle thì không? `Chạy` thấy khác biệt, chưa biết cơ chế. — Nguồn khách: câu hỏi nội bộ
* [ ] OQ-18: Record peek, thao tác hàng loạt chạy ở màn nào? Issues không thấy peek; ô chọn nhiều ở tab Open, Closed chưa bấm. — Nguồn khách: câu hỏi nội bộ
* [x] OQ-19: Hạn mức Automations có đúng chỉ đếm bản đang bật không? Trả lời lượt 4: đúng, "Automations 1 of 75" khi lưu 10 bản, bật 1 (`Chạy`). Hết hạn mức thì sao vẫn chưa đo. — Nguồn khách: câu hỏi nội bộ
* [ ] OQ-21: Vì sao tab Needs Action của Recall từ 261 lên 285 dòng? Cùng tab, khác thời điểm; có thể do nhập tự động từ NHTSA (`Suy`), chưa kiểm. — Nguồn khách: câu hỏi nội bộ
* [ ] OQ-20: AI Issue Prioritization thất bại vì sao, có thử lại không? #55 từ "Prioritizing" sang failed, #40, #42 lại thành High. Chưa biết điều kiện. — Nguồn khách: câu hỏi nội bộ

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
| C-14 Mẫu chưa đọc | Send Email When A Work Order Total Exceeds Amount | Lượt 2 chỉ thấy tên, 1 điều kiện, 1 hành động; lượt 3 đọc đủ, xem C-168 | `Xem` |

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
| C-28 Lượt thất bại | Thử bằng WO Completed bị giao diện chặn | Lượt 2 KHÔNG tái hiện được; lượt 3 tái hiện bằng WO thiếu Start Date, xem C-125 trở đi | `Xem` |
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
| C-36 Sửa khi đang bật, Make a Copy | Muốn xem v.2 | Lượt 2 chưa làm; lượt 3 đã làm, xem C-146 đến C-153 | Không chạy ở lượt 2 |
| C-37 Trigger Vehicle, Update Vehicle Status | Sẽ sửa xe của nhóm khác | Lượt 2 KHÔNG chạy; lượt 3 đã làm trên `TEST-DAUKEO-2`, xem C-159 đến C-167 | Không chạy ở lượt 2 |
| C-38 Run Summary Email | Sẽ gửi email | KHÔNG bật, cả lượt 3 | Không chạy |

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
| C-46 Đổi trạng thái xe | Chỉ có xe nhóm khác và Sample | Lượt 2 KHÔNG đổi; lượt 3 đổi trên `TEST-DAUKEO-2`, xem C-163, C-164 | Không chạy ở lượt 2 |
| C-47 Archive xe | Nút trong menu More Actions | KHÔNG bấm; Restore chưa kiểm | `Xem`, `vehicle-more-actions.jpg` |
| C-48 Recall | 261 dòng Sample, tab Needs Action theo ảnh | Chỉ đọc, không đổi trạng thái; số về sau đổi, xem C-223 | `Xem`, `recalls-list.jpg` |
| C-49 Motor Pool | Cần tạo Motor Pool trong Settings, cần xe của nhóm | KHÔNG chạy; danh sách rỗng; lượt 3 đọc form, xem C-186 | `Xem`, `motor-pool-reservations.jpg` |
| C-50 Documents | Rỗng | Lượt 2 không tải tệp; lượt 3 đã tải, xem C-117 trở đi | `Xem`, `documents-empty.jpg` |

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
| C-63 Mở 48 báo cáo còn lại | | Lượt 2 KHÔNG mở sâu; lượt 3 đọc cột, xem C-72 và Phụ lục báo cáo chuẩn | Không chạy ở lượt 2 |
| C-64 Saved Reports | | Lượt 2 KHÔNG đọc do lỗi đợt; lượt 3 đã lưu, xem C-85 đến C-90 | Không chạy ở lượt 2 |

### 13.8 Hỏi dữ liệu

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| C-65 Đếm sự cố mở | "How many open issues does vehicle TEST-XE-01 have?" | "currently has 2 open issues", bảng Total Count Issue Id = 2; trang xe thật Open 7; khoảng 40 giây | `Chạy`, `ai-analyst-issues.jpg` |
| C-66 Đọc km mới nhất | "What is the latest meter reading of TEST-XE-01 and when was it recorded?" | "1,700.0 (primary meter), recorded in November 2026"; trang xe thật 2.999 km; khoảng 50 giây | `Chạy` |
| C-67 Cảnh báo độ trễ | Cả 2 câu | KHÔNG ghi dữ liệu tính đến lúc nào | `Chạy` |
| C-68 Màn mở trial | Bấm Ask a data question | Không có màn mở trial | `Chạy` |

### 13.9 Điều KHÔNG làm trong lượt chạy

Sau lượt 3 còn: Archive, Restore xe, xe trùng tên (cần một chỗ xe); Motor Pool chạy thật (cần tạo trong Settings); vòng lặp chéo; lượt thật automation Fault (cần thiết bị telematics), nhánh tự duyệt đơn Pending (cần người thứ hai); Delete automation; chặn khi hết hạn mức Automations (cần 75 bản bật); hiệu lực quyền thật; Failure Notification Email, Run Summary Email, Send Email, Email Schedule của báo cáo; hồ sơ thông báo; lưu Enable Access; Share lại, Saved Report Public; Record peek; thao tác hàng loạt; `expense_entries` chưa đọc được do lỗi 500. Tools, Tool Management, Custom Records, Advanced Analytics ngoài AI Data Analyst không mở theo ràng buộc.

### 13.10 Báo cáo: danh mục và cột (lượt 3)

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| C-69 Tab đầu trang | Mở Reports | Favorites 0, Saved 0, Shared 0; thanh bên ghi "Tool List 13 days left" | `Chạy` |
| C-70 Đủ tên | Đọc danh sách Standard Reports | 49 tên, 13 nhóm, đường dẫn từng báo cáo ở Phụ lục | `Chạy` |
| C-71 Nhãn sắp nâng cấp | Đọc thẻ | "Upgrading soon" đúng 4: Cost/Meter Trend, Expense Summary, Operating Costs Summary, Service History by Vehicle | `Chạy` |
| C-72 Mở từng báo cáo | Nạp 49 đường dẫn, không bấm gì trong báo cáo, không bấm Share | Đọc được tiêu đề cột 48/49 | `Chạy` chỉ đọc |
| C-73 Thế hệ mới | 34 báo cáo | Có Save, Share, Export CSV, Print, Filters, Columns, nhiều cái có biểu đồ | `Chạy` chỉ đọc |
| C-74 Thế hệ cũ | 15 báo cáo | Chỉ thấy Save, Filters, Add Filter; KHÔNG thấy nút Share, Export CSV trên màn | `Chạy` chỉ đọc |
| C-75 Khối cột xe | 22 báo cáo thế hệ mới | Kèm khoảng 110 cột thông tin xe chọn trong Columns (Group, Make, Model, chi phí trọn đời, thông số kỹ thuật) | `Chạy` chỉ đọc |
| C-76 Báo cáo dạng hồ sơ | `vehicles/details` | Hồ sơ từng xe, không phải bảng, 10 mỗi trang; KHÔNG có Export CSV | `Chạy` chỉ đọc |
| C-77 Tóm tắt không xuất | `work_order_status_changes/summary` | KHÔNG có Export CSV | `Chạy` chỉ đọc |
| C-78 Số 0 lúc đọc | `service_reminders`, `vehicle_assignments`, `work_orders` | "0 đọc được"; có thể chưa kịp tải, không lấy lại từng cái | `Chạy`, chưa chắc |
| C-79 Số dòng | Báo cáo Issues, `vehicles` | 53 dòng, 25 xe: đếm cả Sample | `Chạy` |
| C-80 Báo cáo lỗi | `reports/expense_entries` | Lần đầu không tải xong trong 12 giây; mở lại Error 500 "We're sorry, but something went wrong." 2 lần, chân trang "Partially Degraded Service" | `Chạy`, `report-expense-entries-500.jpg` |
| C-81 Cột `vehicle_status_summaries` | Đọc cột | Chưa tách được cột riêng, dùng làm mốc khối xe | `Chạy` chỉ đọc |

### 13.11 Báo cáo: lọc, lưu, yêu thích (lượt 3)

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| C-82 Bộ lọc | Mở Filters trên Issues Report | 26 ô, từ Issue Summary đến Include archived vehicles; danh sách ở Mục 18 | `Chạy` |
| C-83 Lọc theo tên | Lọc Issue Summary TEST-NEN | Bộ lọc nằm trên đường dẫn `q[summary_or_description_cont]`: tìm cả tiêu đề lẫn mô tả dù nhãn ghi "Issue Summary" | `Chạy` |
| C-84 Tính lại | Search | Biểu đồ và thẻ đếm tính lại: Open 6, Overdue 0 | `Chạy` |
| C-85 Hộp lưu | Bấm Save | "New Saved Report": Name *, Description, Visibility Public hoặc Private (mặc định Private), Email Schedule (không tick) | `Chạy` |
| C-86 Lưu Private | Lưu `TEST-NEN-BC-01` | Vào Reports › Saved; câu "Private Saved Reports are visible only to you, but can be emailed to anyone with access to the source report." | `Chạy` |
| C-87 Danh sách đã lưu | Đổi List display | Cột Name, Description, Report Type, Schedule | `Chạy` |
| C-88 Menu dòng | Mở menu | View Source Report, View Record History, Edit, Make a Copy, Delete | `Chạy` đọc menu |
| C-89 Yêu thích | Bấm sao | Favorites từ 0 lên 1 | `Chạy` |
| C-90 Mở báo cáo đã lưu | Bấm tên | Sang tab mới, đường dẫn thêm `saved_report_id`, giữ bộ lọc | `Chạy` |
| C-91 Share, Public, Email Schedule | Sẽ tạo link hoặc gửi email | KHÔNG chạy | Không chạy |
| C-92 Bộ lọc báo cáo khác | 48 báo cáo còn lại | Lượt 3 KHÔNG mở; lượt 4 đã đọc, xem C-218 đến C-222 | Không chạy ở lượt 3 |

### 13.12 Danh sách, chế độ xem (lượt 3)

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| C-93 Tìm trên danh sách | Issues, tab All, gõ TEST-NEN | Ra 6 dòng, nút Save View đổi thành Save Changes có chấm cam | `Chạy` |
| C-94 Nhóm dòng | Mở Group | None, Priority, Vehicle or Tool, Group | `Chạy` |
| C-95 Cài đặt xem | Mở View Settings | Manage Columns (nhãn "1 New"), Items Per Page 50, 100, 200, Density Default, Compact | `Chạy` |
| C-96 Chọn cột | Manage Columns, rồi Cancel | Available 27 (ISSUE 9/21, VEHICLE/TOOL 2/6), Visible 11, kéo đổi thứ tự, Restore defaults | `Chạy` |
| C-97 Sửa bản chuẩn | Menu Save Changes ở All | "Fleetio Standard View" có khoá, "Save as a new view to keep your changes"; chỉ có Save as New View, Clear Unsaved Changes | `Chạy` |
| C-98 Lưu view | Name, Description, Shared with | Shared with: Private ("Visible only to you"), Admins Only, Specific Roles, Specific Users, Everyone. Lưu thành tab mới cạnh All, Open, có `saved_view_id` riêng | `Chạy` Private |
| C-99 Trang nhớ tab | Mở lại /issues | Mở đúng tab đang dùng lần trước (lúc vào là Closed) | `Chạy` |
| C-100 Menu dòng | Hover dòng | View, Edit, Add to Service Entry, Add to Work Order, Get Service at Shop, Resolve with Note, Check service history (khoá), Close, Delete | `Chạy` đọc menu |
| C-101 Bấm dòng | Issues | Sang trang chi tiết, KHÔNG mở khung xem nhanh, không thấy Record peek ở màn này | `Chạy` |
| C-102 Thao tác hàng loạt | Có ô chọn ở tab Open, Closed | KHÔNG bấm | Không chạy |

### 13.13 Theo dõi, bình luận, lịch sử, thông báo, tìm toàn cục (lượt 3)

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| C-103 Danh sách @ | Gõ @ trên Issue #55 | Hiện liên hệ kèm biểu tượng khoá nếu không có quyền truy cập | `Chạy` |
| C-104 @ không dấu | Gõ tên không dấu của liên hệ có dấu | KHÔNG ra | `Chạy` |
| C-105 @ có gạch nối | Gõ "@TEST-NEN" | KHÔNG ra `TEST-NEN-LH-01` | `Chạy` |
| C-106 Đăng không khớp | Đăng comment | Thành chữ thường, KHÔNG tạo mention, không nhắc ai | `Chạy` |
| C-107 Unwatch | Bấm Unwatch | Avatar mất khỏi cụm người theo dõi, nút thành Watch | `Chạy` |
| C-108 Watch lại | Bấm Watch | Theo dõi lại được | `Chạy` |
| C-109 Lịch sử | Comment, Watch rồi mở Record History | KHÔNG có dòng nào của Comment, Watch | `Chạy` |
| C-110 AI xếp mức thất bại | Issue #55, Record History | "Issue Priority Status changed from pending to failed", Issue về "No Priority"; Changes By ghi người tạo; không báo ra đâu khác | `Chạy`, `record-history-issue.jpg` |
| C-111 AI xếp mức nền | #54, #55 lúc mới tạo | #54 "No Priority", #55 hiện "Prioritizing"; kết quả khác nhau giữa 2 Issue | `Chạy` |
| C-112 Lọc lịch sử | Record History | Chọn khoảng ngày; cột Date, Changes By, Changes Made | `Chạy` |
| C-113 Chuông | Mở Notifications | Tab Inbox, Archived; lọc All Activity, Comments Only, @ Mentions; Archive all; từng dòng Reply, View All Comments; menu Notification Settings | `Chạy` |
| C-114 Người theo dõi | Automation bình luận | Nhận in-app "Fleetio Automation commented on an issue" | `Chạy`, `notifications-inbox.jpg` |
| C-115 0 hồ sơ thông báo | Tài khoản có 0 hồ sơ | Inbox vẫn có "Fuel Capacity Alert", Fuel Entry trên `TEST-KHO-01` | `Chạy`, `notifications-inbox.jpg` |
| C-116 Tìm toàn cục | Gõ TEST-NEN | Theo nhóm, mỗi nhóm 3 dòng và More; ô chọn loại 16 mục; có cả TEST-XE-01, TEST-KHO-NCC-02: tách theo từ, không đòi khớp cả cụm | `Chạy` |

### 13.14 Kho tài liệu (lượt 3)

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| C-117 Hộp tải | Upload Document | Hộp Filestack: từ máy, Facebook, GitHub, tìm web, link, camera, Instagram, Box; tên nhà cung cấp lộ ra; chỉ dùng từ máy. "Document was successfully added." | `Chạy` |
| C-118 Hiện chậm | Ngay sau tải | Vẫn "No results to show", tải lại mới có | `Chạy` |
| C-119 Dòng | Đọc danh sách, mở menu | File Name, File Size, Location, Auto-Delete, Attached To, Labels; View, Rename, Replace, Download, Delete | `Chạy`, `documents-list-file.jpg` |
| C-120 Gắn xe | Select Vehicles, gắn `TEST-DAUKEO-2` | "Attach Document to Vehicles": tìm, Attached Vehicles, All Vehicles 25, Vehicle Types 25, Groups 11; gắn xong nút thành "Attached" | `Chạy` |
| C-121 Gắn theo nhóm, loại | Có trên hộp | KHÔNG bấm | `Xem` |
| C-122 Xem trước | Mở tệp .txt | Khung xem PDF 0 trang, không xem trước được | `Chạy` |
| C-123 Trang tệp | Đọc | Location, Attached to "1 Vehicle", Labels, Type Text File, File Size, Auto-Delete có câu giải thích, Last Modified, Uploaded, Add Description, Comments | `Chạy` |
| C-124 Dung lượng | Account Usage | Documents "26 B of 250.0 GB" | `Chạy` |

### 13.15 Lượt automation thất bại (lượt 3)

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| C-125 Chọn Completed | Update Field Status của Work Order | Có đủ Open, Pending, Completed; khác Create Record chỉ Open, Pending | `Chạy` |
| C-126 Lượt chạy | `TEST-NEN-AUTO-06`, WO #111 thiếu Start Date | Failed 1, Successful 0, nhãn FAILURE đỏ | `Chạy`, `automation-run-failure.jpg` |
| C-127 Câu lỗi | Run Result | Băng đỏ "Automation Action failed: Start Date can't be blank" | `Chạy`, `automation-run-failure.jpg` |
| C-128 Log | View Full Log | Workflow, Trigger, ConditionSet đều state DNF, status FAILURE, cùng reason, có caused_by, thrown_by trỏ bước gây lỗi | `Chạy` |
| C-129 Bản ghi | Sau lượt lỗi | WO #111 vẫn Open; "Records: No records changed" lần này đúng | `Chạy` |
| C-130 Thử lại | Sau khoảng 5 phút | Total Runs vẫn 1: không thấy tự thử lại trong khoảng đó | `Chạy` |
| C-131 Tự tắt | Sau lượt lỗi | Vẫn Enabled, KHÔNG tự tắt | `Chạy` |
| C-132 Báo người dùng | Ô Failure Notification Email tắt | Trang WO không thấy lỗi; chuông không có dòng nào; chỉ biết khi vào Run History | `Chạy` |
| C-133 Email báo lỗi | Sẽ gửi email | KHÔNG chạy, chưa biết nội dung | Không chạy |
| C-134 Không lách ràng buộc | Luật "WO Completed" | Có kiểm tra giống form tay, Start Date bắt buộc | `Chạy` |

### 13.16 Loại bản ghi, trigger, hạn mức (lượt 3)

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| C-135 Issue | Kiểu sự kiện | Created, Updated, Created or Updated, Deleted; đã chạy Created, Created or Updated | `Chạy` 2 kiểu |
| C-136 Vehicle | Kiểu sự kiện | Created, Updated, Created or Updated, KHÔNG có Deleted; đã chạy Updated | `Chạy` Updated |
| C-137 Work Order | Kiểu sự kiện | Created, Updated, Created or Updated, Deleted; đã chạy Created | `Chạy` Created |
| C-138 Service Entry | Kiểu sự kiện | Created, Updated, Created or Updated, Deleted | `Xem` |
| C-139 Geofence Event | Có `TEST-Geofence` của nhóm khác, 2 lượt | Không do nhóm này chạy | Không chạy |
| C-140 Fault, Purchase Order | Có trong danh sách | Chưa đọc kiểu sự kiện | `Xem` |
| C-141 Điều kiện Work Order | Mở danh sách trường | 61 mục, nhóm WORK ORDER, VEHICLE; không có Description, phải dùng Invoice Number để khoanh vùng | `Chạy` |
| C-142 Update Field Work Order | Mở danh sách | Status, Repair Priority Class, Issued By, Assigned To, Vendor, Labels | `Chạy` |
| C-143 Hành động Work Order | Mở danh sách | Update Field, Add Comment, Send Email, Create Record | `Chạy` |
| C-144 Hai automation lật nhau | OQ-5 | KHÔNG chạy: thử chéo có thể lặp không biết giới hạn trên hệ thống thật | Không chạy |
| C-145 Hạn mức Automations | 7 automation đã lưu, đều tắt | 0 of 75; lượt 4 xác nhận chỉ đếm bản đang bật, xem C-217 | `Chạy` đọc số |

### 13.17 Automation: sửa khi bật, phiên bản, nhóm điều kiện (lượt 3)

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| C-146 Bật lại | Tắt rồi bật, không sửa | Vẫn v.1, Enabled At đổi | `Chạy` |
| C-147 Sửa khi bật, chưa lưu | Đổi nội dung vào form | Băng "You have unsaved changes on this enabled automation" · "Save to update, or discard to keep the current settings."; nút Save thành menu Save Automation, Discard Unsaved Changes | `Chạy` |
| C-148 Lưu bản sửa | Đang bật | Lên v.2, vẫn Enabled, KHÔNG hỏi xác nhận lại, hiệu lực ngay | `Chạy` |
| C-149 Lượt sau sửa | Issue #55 | Comment mang chữ "v2"; Run Result ghi Version v.2 | `Chạy` |
| C-150 Xem bản cũ | Version History, mở v.1 | Màn ghi "Step Summary v.1" nhưng hiện chữ của v.2; danh sách có v.2 Current Version và v.1, kèm Created At, Created By. Chỉ thấy trên 1 lần sửa nội dung action | `Chạy`, `automation-version-v1-lech.jpg` |
| C-151 Make a Copy | Bản đang bật | Mở `automations/new?copy_from=`, chưa lưu gì, tên thêm " (copy)", Disabled; rời trang không để lại bản rác | `Chạy` |
| C-152 Bản đã lưu chưa bật | Đọc Current Version | "—" cho tới khi bật lần đầu | `Chạy` |
| C-153 Menu khi chưa Archive | More Actions | Make a Copy, Archive, View Record History; KHÔNG có Delete | `Chạy` |
| C-154 Nhóm lồng | All of [Summary contains TEST-NEN, Any of (NHOMA, NHOMB)] | Hiện đúng "And", "Or" ở khung trái | `Chạy` |
| C-155 Khớp nhóm | #54 "TEST-NEN-D1 NHOMA" | AUTO-04 và AUTO-01 cùng chạy: 2 comment giống hệt (không tick Prevent duplicate comments) | `Chạy` |
| C-156 Không khớp nhóm | #55 "TEST-NEN-D2 khong khop nhom" | Chỉ AUTO-01 chạy, 1 comment | `Chạy` |
| C-157 Trường thứ 2 | Thêm điều kiện cùng trường | Toán tử mặc định "does not contain", phải đổi tay; Enter trong ô giá trị đóng panel như Apply | `Chạy` |
| C-158 Lượt thêm comment | Run Result | Vẫn "Records: No records changed" | `Chạy` |

### 13.18 Automation trên Vehicle (lượt 3)

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| C-159 Điều kiện Vehicle | Mở danh sách | 71 mục, KHÔNG có "Name", dùng "Vehicle is any of"; có trường cảm biến ở FR-059 | `Chạy` |
| C-160 Hành động Vehicle | Mở danh sách | Update Field, Add Comment, Send Email | `Chạy` |
| C-161 Update Field Vehicle | Mở danh sách | Chỉ 5 trường: Status, Type, Group, Labels, Axle Configuration | `Chạy` |
| C-162 Sửa trường không liên quan | Sửa Color | Trigger Updated vẫn chạy: chạy trên MỌI thay đổi | `Chạy` |
| C-163 Đổi trạng thái tự động | `TEST-NEN-AUTO-05`, sửa Color | Active sang Inactive trong vài giây; Status Updates ghi "Fleetio Automation updated status from Active to Inactive" | `Chạy`, `automation-vehicle-status-flip.jpg` |
| C-164 Người sửa ngược | Đổi về Active khi automation bật | Lưu được, không cảnh báo; 1 giây sau automation đổi lại Inactive; màn người dùng không báo gì | `Chạy`, `automation-vehicle-status-flip.jpg` |
| C-165 Tự kích hoạt | Update Vehicle Status gây Vehicle Updated | Total Runs 2 cho đúng 2 lần người sửa: lượt do automation đổi xe KHÔNG sinh lượt mới, khác Issue | `Chạy` |
| C-166 Kết quả chạy | Lượt đã đổi xe thật | Vẫn "Records: No records changed" dù đã đổi Status; ghi trong run-notes, không có ảnh Run Result của lượt này | `Chạy` |
| C-167 Log đầy đủ | View Full Log | JSON từng bước Workflow, Trigger, ActionSet (có bước NOOP "Automation Trigger has no action set"), ConditionSet, ScoopMatcher, Database; có runtime từng bước | `Chạy` |

### 13.19 Mẫu email, thông báo automation (lượt 3)

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| C-168 Mẫu Send Email WO | Mở `automations/new?template=send_email_from_work_order`, không lưu | Trigger Work Order Created or Updated; Total Cost ≥ 100.000 ₫; Recipient(s) tự điền người đang đăng nhập; Subject, nội dung dùng biến | `Chạy` mở mẫu |
| C-169 Câu cứng | Đọc nội dung mẫu | Ngưỡng đổi theo tiền tệ khách (100.000 ₫) nhưng câu email vẫn viết ">$1,000.00" | `Chạy` mở mẫu |
| C-170 Gửi email thật | Sẽ gửi email | KHÔNG chạy | Không chạy |
| C-171 Rời mẫu | Bấm Cancel | Tab kẹt hộp "Leave site?", phải đóng tab | `Chạy` |
| C-172 Run Summary Email | Đọc câu mô tả | "Daily at 6:00 am, or Weekly on Mondays at 6:00 am"; không bật | `Xem` |
| C-173 Failure Notification Email | Đọc câu mô tả | "Send an email whenever this automation fails."; không bật | `Xem` |
| C-174 Mention trong comment | Đọc câu mô tả | "Notifications for mentions in comments are delivered based on users' permissions and notification settings." | `Xem` |
| C-175 Chống trùng comment | Ô Prevent duplicate comments | Có ô; không tick thì 2 comment trùng (C-155); tick chưa thử | `Chạy` phần không tick |

### 13.20 AI hỏi dữ liệu (lượt 3)

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| C-176 Đếm sự cố | Số sự cố mở của TEST-XE-01 | "has 10 open issues", liệt kê 10 số; thật 12, thiếu #49, #51; khoảng 60 giây | `Chạy` |
| C-177 Ngày dữ liệu | Hỏi cùng câu | "The dataset does not expose a specific "data as-of date" field", đẩy sang "your system's data pipeline or integration settings"; không có ngày dữ liệu trên màn | `Chạy` |
| C-178 Xe mới tạo | Sự cố mở của TEST-DAUKEO-2 | "does not exist", "No issues have been recorded"; xe có từ cùng ngày, Issue #54, #55 tạo 25 phút trước; khoảng 90 giây | `Chạy`, `ai-analyst-vehicle-not-exist.jpg` |
| C-179 So với lượt trước | Khoảng 15 giờ trước trả 2 (thật 7), lượt này 10 (thật 12) | Củng cố khả năng kho trễ | `Suy` |
| C-180 Chưa giải thích | #50 có mà #49 không; #51 có Priority High | Không phải cắt theo thời điểm đơn giản, không do thiếu mức ưu tiên | `Chạy` thấy, nguyên nhân chưa biết |
| C-181 Mở lại chat cũ | Vào chat đã có | Banner "This data may have changed since the last time you had a chat." | `Chạy` |

### 13.21 Quyền, liên hệ, Motor Pool (lượt 3)

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| C-182 Technician, Fuel Entries | Mở Edit Role, Cancel | Chọn None, không có ô con; ghi chú cũ "chỉ có ô xem" sai | `Xem` |
| C-183 Form Enable Access | Chọn, không lưu | "This Contact will be enabled as a User..."; Email ("An email invitation with instructions to create a password will be sent immediately."), Delay email invitation, Message | `Xem` |
| C-184 Mặc định quyền | Đọc form | Role * mặc định Fleet Manager; Record Sets Vehicles, Tools, Contacts, Part Locations, Inspection Forms đều Full Access | `Xem` |
| C-185 Hiệu lực Role, Record Set | Cần người dùng thứ hai | KHÔNG chạy được, không mời người | Không chạy |
| C-186 Form đặt xe | Mở Vehicle Reservation | Operator *, Motor Pool *, Reason for Trip, Pick Up *, Drop Off *, Submit Reservation; rời trang để huỷ | `Xem` |
| C-187 Đặt xe thật | Motor Pool * lấy từ Settings, đang rỗng | KHÔNG chạy được, tạo Motor Pool là Settings bị cấm | Không chạy |
| C-188 Rời form liên hệ | New Contact chưa lưu | Tab kẹt hộp "Leave site?", không đóng được; form chưa lưu, không có dữ liệu | `Chạy` |

### 13.22 Settings (lượt 3)

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| C-189 Đếm trang | Đếm menu | 67 link = 59 trang cấp tài khoản + 7 trang cá nhân + Log Out | `Xem` |
| C-190 Nhóm cấp tài khoản | Đếm theo nhóm | Tài khoản 4, Notification 2, User Access 4, Intelligence 1, Integrations 5, Developer 1, Data Management 5, Dashboard 1, Vehicles 6, Motor Pool 3, Tools 3, Inspections 1, Issues 2, Reminders 3, Service 5, Warranties 1, Parts & Inventory 9, Fuel & Energy 2, Reports 1 | `Xem` |
| C-191 Nút tạo, gửi | Add Role, Add Record Set, Add API Key, Add Webhook, Add SAML, Add Sandbox, Export Data, Add Notification Profile, Enable module, Upgrade | KHÔNG bấm; FR-004 vẫn chưa tắt thử module | Không chạy |
| C-192 Nhóm Tools | 3 trang | KHÔNG mở theo ràng buộc | Không chạy |

### 13.23 Automation Service Entry, Purchase Order, Archive (lượt 4)

| Case | Điều kiện | Kết quả thật | Bằng chứng |
|---|---|---|---|
| C-193 Service Entry: kiểu sự kiện | Mở danh sách | Created, Updated, Created or Updated, Deleted | `Chạy` |
| C-194 Service Entry: bản ghi hành động | Trigger Service Entry | Chọn được Service Entry hoặc Vehicle | `Chạy` |
| C-195 Service Entry: hành động | Mở danh sách | Update Field, Add Comment, Send Email; Update Field chỉ Repair Priority Class, Labels | `Chạy` |
| C-196 Service Entry: Popular Conditions | Mở danh sách | Service Entry Created By, Service Entry Completion Date, Vehicle, Vehicle Status | `Chạy` |
| C-197 Update Field bị từ chối | Repair Priority Class = Emergency, Save | "Automation could not be created. Please resolve any errors try again.", "action is missing" · "is invalid", nút "Fix Errors"; giao diện cho chọn và Apply bình thường, chỉ báo lúc lưu. Chỉ thử 1 giá trị | `Chạy` |
| C-198 Add Comment | Tạo entry đúng xe | Comment hiện ngay, tác giả "Fleetio Automation" | `Chạy` |
| C-199 Khoanh vùng theo xe | Entry xe khác tạo cùng lúc | Total Runs 1, Successful 1: entry xe khác không tính lượt | `Chạy` |
| C-200 Bật | Toggle | Hộp "Do you want to enable this automation?"; v.1 sinh lúc bật đầu tiên; Activity "Enabled changed from false to true", "Version changed from [empty] to 1" | `Chạy` |
| C-201 Ngày hoàn tất trên form entry | Completion Date hiện chữ mờ ngày hiện tại | Là placeholder, bấm lưu báo "can't be blank", phải gõ | `Chạy` |
| C-202 Purchase Order: kiểu sự kiện | Mở danh sách | Created, Updated, Created or Updated; KHÔNG có Deleted | `Chạy` |
| C-203 Purchase Order: bản ghi hành động | Mở danh sách | Chỉ Purchase Order | `Chạy` |
| C-204 Purchase Order: hành động | Mở danh sách | Update Field, Add Comment, Send Email; Update Field Labels, Status; Status chỉ "Rejected", "Approved" | `Chạy` |
| C-205 Purchase Order: Popular Conditions | Mở danh sách | Purchase Order Parts, Vendor, Part Locations, Labels, Status | `Chạy` |
| C-206 Tự duyệt không điều kiện | Chọn Approved | Cảnh báo cam ngay trong panel, yêu cầu điều kiện Status Pending Approval | `Chạy` |
| C-207 Vẫn lưu | Save | Chặn: "Purchase Order Status "Pending Approval" is required", nút "Resolve error" | `Chạy` |
| C-208 Lưu không đổi gì | Edit PO #5, Save as Draft | 0 lượt: không đổi gì thì không tính Updated | `Chạy` |
| C-209 Bấm Approve | Draft sang Approved | 1 lượt, comment "Fleetio Automation" trên #5; comment không kích lại automation | `Chạy` |
| C-210 Tự duyệt đơn Pending thật | Tài khoản có quyền duyệt không tạo được đơn Pending | KHÔNG chạy được, cần người thứ hai | Không chạy |
| C-211 Archive đang bật | More Actions, Archive | "Confirm Automation Archive", băng "This record is archived."; nút Restore, Delete; mất công tắc, Edit, menu; Status Disabled, có Disabled At | `Chạy` |
| C-212 Đang Archived, bản ghi khớp đổi | PO #5 đổi số | Total Runs vẫn 1, không comment mới | `Chạy` |
| C-213 Restore | Một cú bấm | KHÔNG có hộp xác nhận; "Record successfully restored!"; về Disabled dù trước đó Enabled; giữ v.1, Run History 1, Disabled At; Activity ghi Archived At đổi | `Chạy` |
| C-214 Delete | Nút có ở bản Archived | KHÔNG bấm | Không chạy |
| C-215 Fault: trigger | Tạo `TEST-NEN-AUTO-09` | Kiểu sự kiện chỉ có Created; Popular Conditions Fault Code, Fault Status; bản ghi hành động Issue, Fault, Vehicle | `Chạy` |
| C-216 Fault: hành động | Create Record Issue, không điều kiện, Save | Trên Issue chỉ Create Record, ô Assigned to, Priority, không có Summary; trên Fault Update Field chỉ Status, giá trị chỉ Ignored. Lưu được, Disabled. Lượt thật bị chặn: Fault chỉ sinh từ thiết bị telematics | `Chạy` phần lưu |
| C-217 Hạn mức khi đang bật | Bật AUTO-07, đọc Account Usage, tắt lại | "Automations 1 of 75" khi lưu 10 bản, 1 đang bật; "Documents 82.7 kB of 250.0 GB" | `Chạy` đọc số |
| C-218 Bộ lọc kiểu A | Đa số báo cáo mới | Panel ô cố định, nút Search, thường kèm khối Vehicle 11 ô | `Chạy` đọc, không Apply |
| C-219 Bộ lọc kiểu B | 9 báo cáo | "No filters applied.", Add Filter, Popular Filters; `tire_activities` không có Popular Filters | `Chạy` đọc |
| C-220 Bộ lọc kiểu C | `fuel_summary`, `inspections_summary`, `vehicles_utilization_summary`, `vehicles_total_cost_trend` | Thanh lọc trên báo cáo, nút "1 Filters" hoặc "2 Filters", Add Filter, Apply | `Chạy` đọc |
| C-221 Không lọc được | `job_assignments_summary_by_job` | Chỉ có Save; `expense_entries` vẫn Error 500 lần 3 | `Chạy` |
| C-222 Lọc thật | `purchase_orders`, Vendor `TEST-NCC-01` | "1 filter applied", "Clear all", 2 dòng #1, #5; đường dẫn thêm `q[vendor_id_in_s]`; Total Amount gồm cả Draft #5; biểu đồ trục chỉ 20k khi tổng 3,5 triệu. Tên ô nói Vehicle hoặc Asset khác nhau; ô "Subotal amount" sai chính tả | `Chạy` |
| C-223 Recall đổi số | Tab Needs Action, hai lần đọc | `recalls-list.jpg` hiện 261 dòng, ảnh ghi Premium Plan 14 Days Left; run-notes nhóm Sửa chữa ghi 285 dòng. Cùng tab, khác thời điểm, không phải mâu thuẫn ghi chép; vì sao tăng chưa biết (OQ-21) | `Xem` |

## 14. Bảng Settings từng trang

Mọi dòng là `Xem`: mở trang, đọc, không Save. Giá trị là của tài khoản dùng thử lúc đọc; chỉ dòng ghi "(Default)" hoặc "mặc định" là mặc định sản phẩm đọc được trên màn. "Chưa ghi" nghĩa là ghi chú chạy không nêu. Menu có 59 trang cấp tài khoản và 7 trang cá nhân (OQ-10, C-189); bảng dưới kê các trang đã đọc, chưa đủ hết, kèm Account Usage nằm trong General. Tools (3 trang) không mở.

| Trang | Tham số | Mặc định hoặc giá trị đọc được | Ảnh hưởng theo câu trên màn | Mức đọc |
|---|---|---|---|---|
| General Settings | Công ty, địa chỉ, ngành; tiền tệ; định dạng ngày; múi giờ; 12 hay 24 giờ; đơn vị, lít, hệ đo; Vehicle hay Asset; thuế; bật tắt Jobs, Motor Pool, Smart Uploads (Fuel Entry, Service Entry, Inspection Form) | VND; MM/DD/YYYY; CST; các module đều On | Mặc định cho xe mới; đổi tên gọi toàn hệ thống | Đủ |
| Account Usage (trong General) | Documents, Roles, Vehicles, Tools, Automations, Custom Records | Lượt 4: 82.7 kB of 250.0 GB; 4 of 30; 5 of 5; Tools 0 of 25; 1 of 75 khi lưu 10 bản, bật 1; 0 of 25 | Hết hạn mức thì chặn tạo | Đủ |
| Billing & Subscriptions | Gói, Add-On, Account Cancellation | Fleetio Manage - Premium 5 Annual; Trialing; Add-On Tool Management | Không bấm Buy, Start Free Trial | Chỉ đọc |
| Export Account Data | 13 loại dữ liệu; CSV hoặc XLS | Chưa ghi | Gửi email; "the download link in the email expires after 7 days" | Đủ, không bấm |
| Sandboxes | Sample Copy; Production Copy; cột Name, URL, Type, Status, Date Created, Last Data Refresh | 0/2; 0/0 | Môi trường thử | Đủ, không tạo |
| Notification Settings (cá nhân) | Email, Mobile App bật tắt chung; 18 nhóm: Collaboration, Vehicles, Tools, Inspections, Issues, Work Orders, Service Entries, Service Reminders, Vehicle Reminders, Contact Reminders, Fuel Entries, Charging Entries, Motor Pool Reservations, Parts, Vendors, Purchase Orders, Expense Entries, Integrations; mỗi sự kiện cột Email, Push; tự theo dõi xe mới, bản ghi mới, nhắc có sẵn | "You are watching 20 vehicles" | Email tắt chung không tắt "essential communications, Saved Reports, Inspection Workflows, Automation Alerts or Notification Profiles" | Đủ |
| Notification Profiles | Cột Name, Description, Users Assigned, Users Personalized, Status; gán bulk từ Contacts | 0 hồ sơ | "Assign Notification Profiles and manage Watched Vehicle Groups in bulk from the Contacts page." | Đủ, không tạo |
| Watched Vehicle Groups | Cột Name, Total Groups, Direct Vehicles, Subgroup Vehicles, Total Vehicles, Direct Watchers, Total Watchers | 11 nhóm | Quy định xe nào được báo | Đủ |
| Manage Users | Trỏ sang `contacts/users` ngoài Settings | Không áp dụng | Chưa ghi | Mở |
| Security | Minimum Length 8, 15, 30, 50; Expiration None, 30, 60, 90 ngày; chữ hoa thường, số, ký tự; Maximum invalid login attempts 5, 10; Lockout 5, 10, 30 phút; Reset All Passwords; Session Timeout, Fleetio Go: Never, 15, 30 phút, 1, 12, 24 giờ, 2 tuần; Fleetio Web: 15 phút đến 2 tuần, không có Never | Giá trị đang chọn chưa ghi | Áp khi tạo hoặc đặt lại mật khẩu, không áp SAML | Không bấm |
| Manage API Keys (cá nhân) | Cột Label, Token, API Version, Date Added, Status; Account Tokens | Rate Limit (Fleetio: 250 requests/minute) | "Keys can be regenerated and revoked. Once a key has been revoked it cannot be reactivated." | Đủ, không tạo khoá, không ghi token |
| Custom Dashboards (cá nhân) | My Dashboards, Shared With Me; Title, Visibility, Last Updated | Chưa ghi | Riêng theo vai, người | Đủ |
| Roles | Xem Mục 15 | 4 vai có sẵn | Xem Mục 15 | Đủ |
| Record Sets | Xem Mục 16 | Full Access (Default) | Xem Mục 16 | Đủ |
| AI Service Advisor | Issue Prioritization, Issue Resolution, Fault Monitoring, Service Assessments, Service Writer, mỗi cái có Manage | Trạng thái bật chưa ghi | "Prioritizes issues when they're created." · "Match and resolve issues from completed service." · "Drafts Work Orders from open issues and service reminders."; có câu khách tự chịu trách nhiệm | Đủ, không bấm |
| Integrations Directory | Trang `integrations/my-integrations`: Data Connectors 6, Fuel Cards 9, Fuel Management 5, Key Management 1, Operations 1, Telematics 43, Tire Management 1, Tolls & Citations 2 | Không áp dụng | Chưa ghi | Đủ |
| Integration Links | Link sang hệ khác kèm biến; cột Label, Record, Status | Rỗng | Chưa ghi | Đủ |
| Webhooks | Tab Webhooks, Webhook Events; cột URL, # Events, Status | Rỗng | "send a HTTP POST" dạng JSON | Không tạo |
| External Connections | FTP, SFTP, Amazon S3; cột Name, Type | Rỗng | "upload scheduled reports to your company's FTP, SFTP, and Amazon S3" | Không tạo |
| SAML Connectors | Metadata; cột IdP Entity Id, SSO URL | Rỗng | Chưa ghi | Không tạo |
| Fleetio MCP | Kết nối; nhãn New, nhóm Developer | Chưa bật | "Let users on this account connect Fleetio to Claude, Codex or another MCP client. Each connection respects the user's role permissions." | Không bật |
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
| Motor Pools | Motor Pool; cột # Groups | Rỗng | Chưa ghi | Đủ |
| Reservation Rates | Bảng giá đặt xe; cột Name, Status, Usage | Rỗng | Bảng giá đặt xe | Đủ |
| Flat Fees | Phí cố định; cột Amount, Vehicle Types | Rỗng | Phí cố định | Đủ |
| Inspection Settings | Proximity Threshold; Distance Threshold | Fleetio: 80%; 100 m | Bật cảnh báo Location Exception khi phiếu nộp từ một chỗ | Đủ |
| Issue Priorities | No Priority, Low, Medium, High, Critical; cột Alias, Enabled | No Priority (Default); đếm No Priority 8, Low 4, Medium 12, High 27, Critical 4 | Chưa ghi | Đủ |
| Fault Rules | Mã | 11 mã | Chưa ghi | Một phần |
| Service Reminder Settings | Recalculate; Forecasting | Forecasting tắt | Dự báo ngày đến hạn theo km ngày | Đủ |
| Vehicle Renewal Types | Emission Test, Inspection, Insurance, Registration | Chưa ghi | Chưa ghi | Đủ |
| Contact Renewal Types | Certification, License Renewal | Chưa ghi | Chưa ghi | Đủ |
| Maintenance Settings | Enable Work Orders, Next Work Order Number, Require a Meter Reading + Excluded Vehicle Types, Require inspections, Repair Priority Class, Reason for Repair, Category, khoá sửa mã, Inventory Location, Expected Labor Hours, Complaint/Cause/Correction, Markups. Lượt 3 thêm: Disable Editing Default Reason, Category codes; Require an Inventory Location; Display Expected Labor Hours; Require service documentation; Labor, Parts Markup kèm % hoặc giá trị | Giá trị chưa ghi | "This requirement only applies to future Work Orders or Service Entries." | Đủ, lượt 3 đọc 5.534 ký tự (bản trước 3.800/3.965) |
| Work Order Statuses | Open, Pending, Completed; Type Incomplete, Completed; Add | Open (Default); đếm Open 13, Pending 1, Completed 97 "(2 from 1 archived vehicle)" | Completed "corresponding service reminders updated and issues resolved" | Đủ |
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
| Saved Reports | Cột Name, Description, Owner, Visibility, Email Schedule, Created On, Updated On | Lượt 3 có `TEST-NEN-BC-01` Private | Chưa ghi | Đủ |

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
| Fuel Entries | F | S | N (lượt 3 chốt: chọn None, không có ô con, OQ-9) | S |
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

`Chạy`: Apply từng mẫu để đọc định nghĩa, rời trang không lưu. 18/18 đọc đủ sau lượt 3. Số trong mẫu là ví dụ khách sửa được trước khi bật.

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
| Work Order | Send Email When A Work Order Total Exceeds Amount | Created or Updated | Work Order Total Cost ≥ 100.000 ₫ | Send Email: Recipient(s) tự điền người đang đăng nhập; Subject "Action Needed: Review high WO cost {{ work_order.number }}"; nội dung có biến `{{ work_order.number }}`, `{{ asset.name }}`, `{{ work_order.service_tasks }}` và câu cứng ">$1,000.00" (E-019) |
| Work Order | Set Repair Priority Class to Scheduled for Preventative Maintenance Work Orders | Created or Updated | Line Item Reason for Repair is any of 08 | Update Repair Priority Class to Scheduled |
| Work Order | Automatically Assign Employee To Newly Created Work Orders | Created | Assigned To is blank | Update Assigned To (tự điền người đang đăng nhập) |
| Work Order | Create Follow-Up Work Order After Tire Replacement | Updated | Service Tasks any of Tire Replacement và Status Type Completed | Create Work Order, Status Open, Service Tasks Wheel Lug Nut Torque |

## 18. 49 báo cáo chuẩn

Đọc đủ 49 tên (`Chạy`), mở từng báo cáo đọc cột 48/49, chỉ đọc (`Chạy`). Đủ tên, đường dẫn, cột ở Phụ lục báo cáo chuẩn. Bản 02/11 ghi 48 báo cáo, 12 nhóm là sai.

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

**"Upgrading soon":** Cost/Meter Trend, Expense Summary, Operating Costs Summary, Service History by Vehicle.

**Bộ lọc Issues Report, 26 ô (`Chạy`):** Issue Summary, Issue Source, Reported Date, Time to Resolve in Days, Due Date, Resolved Date, Closed Date, Status, Labels, Reported By, Resolved By, Assigned to, Priority, Vehicles, Vehicle Types, Vehicle Groups, Status (xe), Vehicle Year, Make, Model, Trim, Current Operator, VIN/SN, License Plate, Registration State/Province, Include archived vehicles. Bộ lọc các báo cáo khác ở Mục 21.3.

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

**Dữ liệu thử còn trên tài khoản:** automation `TEST-NEN-AUTO-01` (đã lên v.2), `TEST-NEN-AUTO-02`, `TEST-NEN-AUTO-03`, `TEST-NEN-AUTO-04`, `TEST-NEN-AUTO-05`, `TEST-NEN-AUTO-06`, `TEST-NEN-AUTO-07`, `TEST-NEN-AUTO-08`, `TEST-NEN-AUTO-09` (đều đang tắt, 09 chưa bật lần nào); Service Entry #57903356 trên `TEST-KHO-01`; comment và số đã sửa trên Purchase Order #5; Issue #40, #42, #43, #44 và Work Order #105 trên xe dùng chung `TEST-XE-01`; Issue #54, #55, 1 comment trên #55, Work Order #111 Open và tệp `TEST-NEN-tailieu.txt` trên `TEST-DAUKEO-2` (Color = TEST, Status đã trả về Active); báo cáo Private `TEST-NEN-BC-01` đang yêu thích; view Private `TEST-NEN-VIEW-01` trên Issues; hai liên hệ `TEST-NEN-LH-01` không email.

## 21. Phụ lục báo cáo chuẩn

### 21.1 Đủ 49 tên theo nhóm

`Chạy`: đọc từ danh sách Standard Reports. Đường dẫn ghi phần sau `reports/`. Dấu `*` là báo cáo gắn "Upgrading soon".

| Nhóm | Số | Tên | Đường dẫn |
|---|---|---|---|
| Vehicles | 14 | Cost Comparison by Year in Service | `vehicles/cost_comparison_by_year_in_service` |
| Vehicles | | Cost/Meter Trend * | `vehicles/cpm_trend` |
| Vehicles | | Expense Summary * | `vehicles/expense_summary` |
| Vehicles | | Expenses by Vehicle | `expense_entries` |
| Vehicles | | Group Changes | `vehicle_group_changes` |
| Vehicles | | Operating Costs Summary * | `vehicles/operating_cost_summary` |
| Vehicles | | Status Changes | `vehicle_status_changes` |
| Vehicles | | Status Summary | `vehicle_status_summaries` |
| Vehicles | | Tire Activity Report | `tire_activities` |
| Vehicles | | Total Cost Trend | `vehicles_total_cost_trend` |
| Vehicles | | Utilization Summary | `vehicles_utilization_summary` |
| Vehicles | | Vehicle Details | `vehicles/details` |
| Vehicles | | Vehicle Renewal Reminders | `vehicle_renewal_reminders` |
| Vehicles | | Vehicles Report | `vehicles` |
| Vehicle Assignments | 2 | Vehicle Assignment Log | `vehicle_assignments` |
| Vehicle Assignments | | Vehicle Assignments Summary | `vehicle_assignments/summary` |
| Inspections | 4 | Inspection Failures List | `inspections/failures` |
| Inspections | | Inspection Schedules | `inspections/schedules` |
| Inspections | | Inspection Submission List | `inspections` |
| Inspections | | Inspection Submissions Summary | `inspections_summary` |
| Issues | 2 | Faults Summary | `faults/summary` |
| Issues | | Issues List | `issues` |
| Service | 8 | Maintenance Categorization Summary | `vmrs_system_assembly_components/summary` |
| Service | | Repair Priority Class Summary | `repair_priority_classes/summary` |
| Service | | Service Entries Summary | `service_entries/summary` |
| Service | | Service History by Vehicle * | `service_entries` |
| Service | | Service Reminder Compliance | `service_reminder_compliance` |
| Service | | Service Reminders | `service_reminders` |
| Service | | Service Task Summary | `service_tasks/summary` |
| Service | | Vehicles Without Service | `vehicles_without_service` |
| Warranties | 2 | Part Warranty Opportunities | `part_warranty_opportunities` |
| Warranties | | Vehicle Warranty Opportunities | `vehicle_warranty_opportunities` |
| Work Orders | 5 | Labor Time Entries List | `work_orders/labor_time_entries` |
| Work Orders | | Technician Labor Summary | `work_orders/technician_summary` |
| Work Orders | | Work Order Status Summary | `work_order_status_changes/summary` |
| Work Orders | | Work Orders by Vehicle | `work_orders/by_vehicle` |
| Work Orders | | Work Orders List | `work_orders` |
| Contacts | 2 | Contact Renewal Reminders | `contact_renewal_reminders` |
| Contacts | | Contacts List | `contacts` |
| Parts | 4 | Parts Activity Report | `inventory_journal_entries` |
| Parts | | Parts by Location | `part_locations` |
| Parts | | Parts by Vehicle | `parts/by_vehicle` |
| Parts | | Purchase Orders List | `purchase_orders` |
| Fuel | 3 | Fuel Entries by Vehicle | `fuel_entries` |
| Fuel | | Fuel Summary | `fuel_summary` |
| Fuel | | Fuel Summary by Location | `fuel_entries/by_location` |
| Tools | 1 | Tool Service Entries Summary | `tool_service_entries_summary` |
| Jobs | 1 | Job Assignments Summary by Job | `job_assignments_summary_by_job` |
| Motor Pools | 1 | Motor Pool Reservations Summary | `motor_pool_reservations_summary` |

### 21.2 Cột thật từng báo cáo

`Chạy` 48/49, chỉ đọc, không bấm trong báo cáo. Kiểu **M** là giao diện mới, **C** là giao diện cũ (FR-054). Cột "+Xe" là báo cáo kèm khoảng 110 cột xe chọn trong Columns. "Dòng" là số dòng lúc đọc, có TEST lẫn Sample; "0 đọc được" có thể do chưa kịp tải.

| Đường dẫn | Kiểu | Dòng | +Xe | Tổng cột | Cột riêng của báo cáo | Chiều nhóm trên màn |
|---|---|---|---|---|---|---|
| contact_renewal_reminders | M | 81 | | 31 | Status, Renewal Type, Due Date, Contact, Subscribers + khối liên hệ | |
| contacts | C | 55 | | 10 | Full Name, Group, Email, Employee Number, Job Title, Start Date, Leave Date, License Number, License State, License Class | |
| vehicles/cost_comparison_by_year_in_service | M | 20 | có | 112 | Year 1..8, Avg. Cost / Meter | |
| vehicles/cpm_trend | M | 25 | có | 115 | Theo tháng; biểu đồ | |
| vehicles/expense_summary | M | 2 | | 14 | Expense Type, Transactions, Vehicles, Cost, Total | Group: Expense Type |
| expense_entries | C | ? | | ? | Không đọc được: Error 500 (E-014) | |
| faults/summary | M | 11 | | 20 | Code, Name, Description, Priority Handling, Vehicle Count, Open, Pending, Ignored, Resolved, Total, First Occurred, Last Occurred | All statuses; Group: Fault Only |
| fuel_entries | M | 59 | có | 129 | Date, Occurred at, Vendor, Vendor region, Odometer, Void, Usage, Price/Gallon, Fuel Economy, Cost, Partial, Reset, Reference, Vehicle Exception Alert | |
| fuel_summary | C | 23 | | 8 | Name, Usage, Gallons, Economy, Cost/Usage, Total Fuel Cost, Cost/Gallon, Last Fuel Date | |
| fuel_entries/by_location | M | 0 | | 13 | Fuel Vendor Location, Transactions, Gallons, Cost | Group: Location Only |
| vehicle_group_changes | M | 0 | có | 116 | From, To, User, Date, Duration | |
| inspections/failures | M | 10 | có | 129 | Date, Submission, Form, Form Version, Submission Source, Submitted By, Duration, Item, Stage, Issue, Acknowledged By, Acknowledged At, Acknowledged Comment; biểu đồ | Count |
| inspections/schedules | M | 5 | có | 117 | Operator, Inspection Form, Due Date, Last Inspected, Schedule, Overdue | |
| inspections | M | 16 | có | 148 | Date, Inspection Form, Form Version, Started at, Submitted at, Submission Source, Duration, Failed Items + khối người; biểu đồ | By Day |
| inspections_summary | C | 25 | | 5 | Name, Submissions Count, Forms Count, Average Duration, Group; biểu đồ | Submissions by Vehicle, by User |
| issues | M | 53 | có | 133 | Issue, Status, Priority, Summary, Reported Date, Reported By, Assigned, Due Date, Due Meter, Closed, Resolved, Resolved with, Reopened, Resolved Meter Variance, Time to Resolve in Days, Asset Record Type | |
| job_assignments_summary_by_job | C | 0 | | 8 | Vehicle, Vehicle Type, Assignments Count, Days On Job, Usage, Meter Unit, Avg/Day, Job | |
| work_orders/labor_time_entries | M | 0 | | 9 | Technician, Work Order, Vehicle, Service Task, Expected Labor Hours, Notes, Started At, Ended At, Duration | |
| vmrs_system_assembly_components/summary | M | 5 | | 15 | Category Code, Line Item Usage, Latest Usage, Labor Costs, Parts Costs, Subtotal; biểu đồ | Group: Category Code |
| motor_pool_reservations_summary | C | 0 | | 15 | Number, Motor Pool, Reservation Status, Reason for Trip, Pick Up, Drop Off, Approved At, Completed At, Meter/Duration/Flat Fees Subtotal, Total Amount, Assigned Vehicle Name, Group, Operator Name | |
| vehicles/operating_cost_summary | M | 8 | có | 116 | Service, Fuel, Other, Total Cost, Cost/Meter (Filtered); biểu đồ | Group: Vehicle Group |
| part_warranty_opportunities | C | 0 | | 6 | Replacement Work Order Number, Vehicle Name, Vehicle Group, Part Number, Part Description, Original Work Order Number | |
| inventory_journal_entries | M | 31 | có | 156 | Created at, Previous/Adjustment/New Quantity, Associated Work Order, Associated Inspection, Adjustment Unit Cost, Adjustment Type, Inventory Adjustment Reason, Vendor, Part..., Part Location, Contact | |
| part_locations | M | 4 | | 15 | Part Location, Total Inventory Value, Part, Category, Unit Cost, Aisle / Row / Bin, Current Quantity, Work Order Current Quantity, Purchase Order Current Quantity, Reorder Point | Sort: Number |
| parts/by_vehicle | M | 5 | có | 137 | Part..., Work Order, Part Location, Vendor, Assigned to, Issue Date, Invoice Number, PO Number, Part unit price, quantity, subtotal, Total | |
| purchase_orders | M | 4 | | 38 | PO, Description, Part Location, Vendor; người + ngày cho từng bước Submitted, Rejected, Approved, Purchased, Partially Received, Received In Full, Closed; Line Items, Subtotal, Shipping, Discount, Tax, Tax 2, Total Amount; biểu đồ | Layout: Group by Purchase Order |
| repair_priority_classes/summary | M | 15 | có | 127 | Last Service Date, # Service Entries, # Service Tasks, Duration, Labor, Labor markup, Parts, Parts markup, Subtotal, Tax, Warranty Credits, Total, # Scheduled, # Non-Scheduled, # Emergency; biểu đồ | |
| service_entries/summary | M | 15 | có | 127 | Giống dòng trên, không biểu đồ | |
| service_entries | M | 107 | có | 153 | Service Entry, Repair Priority Class, Actual Start, Completion, Reference, External ID, Invoice Number, Invoice Date, nhiều cột Auto Integrate RO, Vendor, Minority Owned (MBE), Women Owned (WBE), Work Order Number, Service Tasks, Resolved Issue Numbers, Total Labor, Total Parts, Tax, Fees | Layout: Group by Service Entry |
| service_reminder_compliance | M | 168 | có | 121 | Due At, Completed At, On-Time Status, Service Task, Expected Labor Hours, Due/Completed Meter Value; biểu đồ | Group: Individual Service Reminders |
| service_reminders | C | 0 đọc được | | 12 | Status, Service Task, Subtasks, Incomplete Work Orders, Meter Interval, Due Meter, Meter Variance, Time Interval, Due Date, Time Variance, Vehicle, Group | |
| service_tasks/summary | M | 27 | | 21 | Default Category, Default System, Service Task, Expected Labor Hours, Usage, # Vehicles, Last Service Date, Labor, Parts, Subtotal; biểu đồ | Group: Service Task Only |
| vehicle_status_changes | M | 27 | có | 115 | From, To, User, Date | |
| vehicle_status_summaries | M | 25 | có | 117 | Chưa tách được cột riêng (dùng làm mốc khối xe) | |
| work_orders/technician_summary | M | 9 | | 43 | Technician + khối liên hệ, Average Hourly Rate, Work Orders, Line Items, Hours/Line Item, Total Hours, Cost/Line Item, Total Labor Cost | Layout: Group by Technician |
| tire_activities | C | 96 | | 13 | Vehicle, Date Installed, Date Recorded, Tire Model, Tire Meter, Activity, Method, User, Pressure, Tread Depth, Position, Axle Type, Tire Identification Number | |
| tool_service_entries_summary | C | 0 | | 10 | Name, Brand, Model, Serial Number, Service Entries Count, Total Labor Subtotal, Aggregated Subtotal, Total Tax 1, Tax 2, Aggregated Total | |
| vehicles_total_cost_trend | C | 25 | | 4 | Name, 3 tháng gần nhất | |
| vehicles_utilization_summary | C | 25 | | 9 | Name, Group, Min Value, Min Date, Max Value, Max Date, Usage, Avg/Day, Meter Unit | |
| vehicle_assignments | M | 0 đọc được | có | 142 | Operator + khối liên hệ, Start Date/Time, End Date/Time, Duration, Start Meter, End Meter, Distance | |
| vehicle_assignments/summary | M | 25 | có | 115 | # Assignments, # Operators, % Assigned; biểu đồ | Group: Vehicle |
| vehicles/details | M | 25 (10 mỗi trang) | | 54 | Dạng hồ sơ từng xe, không phải bảng: thông số, Purchase, Lifecycle, Loan/Lease, Recent Comments, Images, Service Reminders, Vehicle Renewal Reminders. Không có Export CSV | |
| vehicle_renewal_reminders | M | 21 | có | 114 | Status, Renewal Type, Due Date, Vehicle, Subscribers | |
| vehicle_warranty_opportunities | C | 4 | | 8 | Warranty Name, Work Order Number, Service Task, Vehicle Name, Vehicle Group, Complaint, Cause, Correction | |
| vehicles | C | 25 | | 12 | Name, Group, Year, Make, Model, Type, Status, Operator, VIN/SN, License Plate, Cost Per Meter Unit (Lifetime), Service Programs | |
| vehicles_without_service | M | 3 | có | 111 | Khối xe | |
| work_order_status_changes/summary | M | 3 | | 14 | Status, Entered, Left, Start to End, Net Change. Không có Export CSV | |
| work_orders/by_vehicle | M | 108 | có | 141 | Work Order, Repair Priority Class, Vendor, Invoice Number, PO Number, Assigned To, Issue, Start, Completion Date, Duration, Line Item Count, Service Tasks, Resolved Issues, Labor Hours, Parts Quantity, Labor, Parts Subtotal + Markup, Tax, Discount, Total Amount | |
| work_orders | C | 0 đọc được | | 9 | Number, Status, Repair Priority Class, Resolved Issues, Issue Date, Scheduled Start Date, Expected Completion Date, Assigned To, Total Cost | |

### 21.3 Bộ lọc từng báo cáo

`Chạy` lượt 4: mở Filters, đọc nhãn, không Apply; chỉ lọc thật `purchase_orders`. **[XE]** là khối 11 ô Vehicle Types, Groups, Status, Year, Make, Model, Trim, Current Operator, VIN/SN, License Plate, Registration State/Province.

| Báo cáo | Kiểu | Ô lọc |
|---|---|---|
| contact_renewal_reminders | A | Status, Renewal Type, Time Frame, Contacts, Contact Group |
| faults/summary | A | Fault Code, Fault Details, Critical Codes Only, Time Frame, Total Occurrences (Equals, Less than, Greater than...), [XE] |
| fuel_entries, fuel_entries/by_location | A | Time Frame, Vendors, Fuel Type, Reference, Fuel Alerts, [XE], Void Status, đơn vị Miles, Kilometers, Gallons (US), Gallons (UK), Liters |
| inspections | A | Time Frame, Inspection Form, Duration (minutes), Users, User Groups, User Roles, [XE] |
| inspections/failures | A | Inspection Form, Inspection Items, Stage, Time Frame, Submitted By User, [XE] |
| inspections/schedules | A | Due Date, Last Inspected, Inspection Form, Schedule Type, Schedule Status, [XE] |
| issues | A | 26 ô, xem Mục 18 |
| inventory_journal_entries | A | Time Frame, Previous quantity, Adjustment quantity, Current quantity, Adjustment Type, Part Locations, Part, Part Number, Part Description, Part Category, Part Manufacturer, Part Vendors, [XE] |
| part_locations | A | Part Location, Inventory status, Current Quantity, Work Orders Current Quantity, Purchase Order Current Quantity, Reorder Point, Part, Part Number, Part Description, Part Category, Part Manufacturer, Part Vendors, Aisle, Row, Bin, Include archived parts |
| parts/by_vehicle | A | Work Order Status, Completion Date, Quantity Subtotal, Subotal amount (nguyên văn sai chính tả), [XE], các ô Part, Part Locations |
| purchase_orders | A | Description, Labels, Part Locations, Status, Vendor, người + ngày từng bước (Created, Approved, Purchase, Received In Full, Closed), Total, các ô Part |
| repair_priority_classes/summary | A | Repair Priority Class, Service Tasks, Duration (hours), Time Frame, Vendors, [XE] |
| service_entries | A | Repair Priority Class, Created by, Service Tasks, Reason for Repair, Category, System, Assembly, Component, External ID, Time Frame, Duration (hours), Vendors, Minority/Women Owned, Labels, Reference, Work Order Number, Generated by work order, [XE] |
| service_entries/summary | A | Repair Priority Class, Service Tasks, Duration (hours), Time Frame, Vendors, khối Asset thay Vehicle |
| service_reminder_compliance | A | Completion Date, Became Due Date, On-Time Status, Service Tasks, [XE] |
| service_tasks/summary | A | Service Entry Status, Time Frame, Repair Priority Class, Service Tasks, Exclude archived tasks, Default Category, Default System, Labels, Vendors, Number of Uses, Service Task Part Cost, Service Task Labor Cost, Total Cost, [XE] |
| vehicle_assignments | A | Time Frame, Show Assignments from Past, Current, Future; Operator, Operator Group, khối xe, Vehicle Loan/Lease Vendors, Vehicle Ownership |
| vehicle_assignments/summary | A | Time Frame, Assignments Count, % Assigned, % Assigned Range, Operator, Operator Group, khối Asset |
| vehicle_group_changes | A | Time Frame, From Group, To Group, [XE], Loan/Lease Vendors, Ownership |
| vehicle_renewal_reminders | A | Status, Renewal Type, Time Frame, khối xe, Loan/Lease Vendors, Ownership |
| vehicle_status_changes | A | Time Frame, From status, To status, [XE], Loan/Lease Vendors, Ownership |
| vehicle_status_summaries | A | Time Frame, # Changes, Duration in Status, [XE] |
| vehicles/cost_comparison_by_year_in_service | A | Expense Type, Meter Type, [XE], Current Meter |
| vehicles/cpm_trend | A | Time Frame, Expense Type, [XE], Current Meter |
| vehicles/details | A | [XE], Loan/Lease Vendors, Purchase Vendors, Ownership, Current Meter |
| vehicles/expense_summary | A | Time Frame, Include Future Expenses, Only Include TCO Expenses, Expense Type, Vendor, khối Asset |
| vehicles/operating_cost_summary | A | Time Frame, Expense Type, khối Asset, Current Meter |
| vehicles_without_service | A | Time Frame, Service Task, [XE] |
| vmrs_system_assembly_components/summary | A | Service Entry Status, Time Frame, Category, System, Reason for Repair, Repair Priority Class, Service Tasks, Labels, Vendors, [XE] |
| work_order_status_changes/summary | A | Time Frame |
| work_orders/by_vehicle | A | Status, Repair Priority Class, Vendor, Service Tasks, Labels, Created by, Assigned to, Issue Date, Scheduled Start Date, Start Date, Completion Date, Duration (hours), Parts Subtotal, Parts Markup, Labor Subtotal, Labor Markup, Subtotal, Total, khối xe |
| work_orders/labor_time_entries | A | Contacts, Started at, Ended at |
| work_orders/technician_summary | A | Issue Date, Labor Timeframe, Status, Service Task, Technician, Scheduled Start Date, Start Date, Completion Date, Labels, khối Asset |
| work_orders | B | Vehicle, Vehicle Group, Work Order Service Tasks, Watcher, Assignee Group, Work Order Labels, Work Order Repair Priority Class, Vehicle Current Job |
| vehicles | B | Vehicle, Vehicle Group, Vehicle Status, Vehicle Type, Vehicle Current Job |
| service_reminders | B | Service Task, Service Reminder Service Programs, Service Reminder Manually Set Next Due, Vehicle, Vehicle Group |
| contacts | B | Role, Unconfirmed Email, Classification, Group, Full Name, Email, City, State/Province/Region, Currently Assigned Vehicle, Currently Assigned Tools |
| part_warranty_opportunities | B | Replacement Work Order Completed At, Vehicle, Vehicle Group, Vehicle Current Job, Part Manufacturer Part Number, Part Manufacturer, Part Category, Part Vendor |
| vehicle_warranty_opportunities | B | Vehicle Warranty Name, Work Order Completed At, Vehicle Group, Vehicle Current Job, Service Task |
| motor_pool_reservations_summary | B | Vehicle Reservation Motor Pool, Vehicle Reservation Operator, Status, Vehicle |
| tool_service_entries_summary | B | Tool Brand, Tool Model, Tool, Tool Status, Tool Group, Tool Current Assignee |
| tire_activities | B | Không có Popular Filters |
| fuel_summary | C | Fuel Entry Date |
| inspections_summary | C | Inspection Submitted, Failed Items, Form, User |
| vehicles_utilization_summary | C | Meter Type, Meter Entry Meter Date; "2 Filters" |
| vehicles_total_cost_trend | C | Time Frame |
| job_assignments_summary_by_job | Không | Chỉ có Save |
| expense_entries | ? | Không đọc được: Error 500 lần 3 (E-014) |

Bảng kiểu B ghi Popular Filters, không phải toàn bộ trường Add Filter.

## Phát hiện lượt 3 (03/11)

Nguồn: `run-notes/platform.md`, mục Lượt 3.

- Lượt automation thất bại không thử lại trong khoảng 5 phút, không tự tắt, không báo trong app.
- Automation lật ngược thao tác tay sau 1 giây, không cảnh báo. "No records changed" hiện cả khi đã đổi xe.
- AI hỏi dữ liệu nói TEST-DAUKEO-2 "does not exist", đếm 10/12 sự cố của TEST-XE-01, thiếu #49, #51. Nghiêng về kho trễ (`Suy`), chưa giải thích được 2 sự cố đó.
- AI Prioritization thất bại im lặng, chỉ thấy trong Record History. Có Inbox dù 0 hồ sơ thông báo.
- "No records changed" hiện ở cả lượt comment, lượt đổi xe, lượt lỗi; chỉ lượt lỗi là đúng sự thật.
- Lượt 4: hạn mức Automations chỉ đếm bản bật (1 of 75 khi lưu 10); tự duyệt đơn mua bị buộc Pending Approval; Fault chỉ có Created; báo cáo có 3 kiểu bộ lọc.
- Hiệu lực Role, Record Set cần người dùng thứ hai; Motor Pool cần tạo trong Settings; vòng lặp chéo automation không chạy vì không rõ giới hạn trên hệ thống thật.
