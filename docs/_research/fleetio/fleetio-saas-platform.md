---
type: research
keyword: "Fleetio: cấu hình theo khách, tự động hoá, quyền, danh sách, báo cáo, onboarding, tích hợp"
status: draft
status_changed: 2026-11-03
status_reason: "đã review upstream, không cần sửa"
updated: 2026-11-03
links:
  - docs/_product/prd.md
  - docs/_product/saas-core-vs-tenant.md
  - docs/_product/tenant-parameters.md
  - docs/_research/2026-11-02-fleetio-app-teardown.md
  - docs/_research/fleetio/run-notes/platform.md
  - docs/_research/fleetio/srs/fleetio-saas-platform-spec.md
---

# Giải pháp tham khảo: Nền tảng SaaS và thao tác chung

> Khuyến nghị: **Nên tham khảo mạnh** cho phần cấu hình theo khách (OQ-7 của PRD), mô hình quyền và khung tự động hoá. Đây là phần có ích cho Invlogis sớm nhất vì không phụ thuộc Gói Bảo dưỡng đội xe. Lượt chạy 03/11/2026 đã tạo, bật, chạy, tắt, lưu trữ tự động hoá thật và thử chia sẻ báo cáo, hỏi dữ liệu bằng lời; hai chỗ sau lộ điểm yếu nặng (Mục 4 "Điểm yếu cần làm khác"). Phần "Đề xuất cho Invlogis" tách riêng; không phần nào là yêu cầu đã chốt.

## 1. Idea Seed

Luật nghiệp vụ là thứ khách tự bật tắt, không phải code riêng. Quyền tách làm hai lớp: làm được gì (Role) và trên dữ liệu nào (Record Set), trong Record Set lại tách quyền sửa (Manage) và quyền xem (View). Tự động hoá theo mẫu Trigger, Điều kiện, Hành động: lưu xong ở trạng thái tắt, bật phải xác nhận, mỗi lượt chạy có nhật ký. Lái xe, thợ, kế toán chung một hồ sơ Liên hệ; người dùng chỉ là liên hệ được bật truy cập. Khách mới có dữ liệu mẫu không tính vào hạn mức gói và hướng dẫn ngay trên từng trang.

## 2. Context

**Feature Invlogis liên quan:** OQ-7 của PRD (cấu hình và khởi tạo khách mới chưa thành feature), `access-control` (#5), `organization` (#6), `common-workspace` (#2), `help-center` (#4), `workshop-reports`, `account-access` (#1), `cross-process-flow` (#3).

**Nguồn và bằng chứng:**

- Lượt 1, 2026-11-02, tài khoản dùng thử: xem trang đầu, báo cáo, trình dựng tự động hoá, khoảng 20 trang Settings, Record Sets.
- Lượt 2, 2026-11-03, cùng tài khoản, tiền tố dữ liệu `TEST-NEN`: automation 96373 `TEST-NEN-AUTO-01`, 96375 `TEST-NEN-AUTO-02`, 96376 `TEST-NEN-AUTO-03` (đều đang tắt); Issue #40, #42, #43, #44 trên xe dùng chung TEST-XE-01; Work Order #105 sinh từ automation; hai liên hệ `TEST-NEN-LH-01`. Đọc 56 tên trang Settings, mở Edit Role cả 4 vai (bấm Cancel), đọc 18 mẫu tự động hoá, 49 tên báo cáo. Chi tiết từng case ở [[docs/_research/fleetio/srs/fleetio-saas-platform-spec.md|SRS]] Mục 13.
- Giới hạn chung: tài khoản một người dùng có toàn quyền nên chưa kiểm hiệu lực quyền thật; hạn mức xe "5 of 5" đã đầy bởi xe TEST của các nhóm khác nên không tạo được xe riêng; không đổi Settings, không bấm nút gửi email, không mở trial. Custom Records, Tools chỉ theo tài liệu hãng.

| Nhãn | Nghĩa |
|---|---|
| **Chạy** | Đã thao tác và thấy kết quả |
| **Xem** | Thấy trên giao diện, mở màn nhưng không lưu |
| **Docs** | Đọc từ tài liệu công khai của Fleetio |
| **Suy** | Kết luận rút ra, chưa kiểm chứng |
| **GĐ** | Giả định của người viết |

## 3. User Types (preliminary)

| User Type | Pain Point | Primary Need |
|---|---|---|
| Admin của khách | Muốn đổi luật mà phải nhờ nhà cung cấp | Tự cấu hình, thử an toàn trước khi bật |
| Đội sản phẩm | Mỗi khách một yêu cầu làm riêng | Khách tự đáp ứng phần lớn nhu cầu |
| Đội hỗ trợ | Khách hỏi "sao bản ghi tự đổi" | Tra được lượt chạy nào, phiên bản nào gây ra |
| Quản lý | Mở app không biết việc gì gấp | Trang đầu chỉ rõ việc cần xử lý |
| Người dùng mới | Không biết bắt đầu từ đâu | Dữ liệu mẫu, hướng dẫn tại chỗ |

### 3.1 Tác vụ chính

| Vai trò | Tác vụ | Tần suất | Mức quan trọng | Ghi chú |
|---|---|---|---|---|
| Admin của khách | Cấu hình danh mục, luật | Hiếm | Cao | Sai làm chặn nghiệp vụ hàng loạt |
| Admin của khách | Phân quyền người dùng | Mỗi tuần | Cao | Lộ dữ liệu chi nhánh khác |
| Admin của khách | Tạo, bật, tắt tự động hoá | Hiếm | Cao | Chuỗi thay đổi khó truy nếu thiếu nhật ký |
| Người dùng | Lọc, lưu chế độ xem | Mỗi ngày | Trung | |
| Quản lý | Xem trang đầu, báo cáo, chia sẻ báo cáo | Mỗi ngày | Cao | Chia sẻ ra ngoài có rủi ro lộ dữ liệu |

## 4. Capabilities Breakdown

### P0 — must have

- P1 [Mới] [Lõi] [Cấu hình] **Quyền hai lớp:** Role cho hành động (4 vai có sẵn, 30 module, mỗi module mức đủ, một phần, không, có quyền con như `update_status`, `archive_delete`, PO `approve` tách `receive`); Record Set cho phạm vi dữ liệu trên Xe, Liên hệ, Kho phụ tùng, Biểu mẫu kiểm tra, tách Manage và View. Fleetio: `Xem` mở Edit Role cả 4 vai và Record Set, chưa kiểm hiệu lực thật vì không mời người. Sát với quyền theo chi nhánh của `access-control`.
- P2 [Mới] [Lõi] [Cấu hình] **Thiết lập chung theo khách:** tiền tệ, định dạng ngày, múi giờ, 12 hoặc 24 giờ, đơn vị số đo, đơn vị nhiên liệu, hệ đo lường, gọi đối tượng là Vehicle hay Asset, thuế, bật tắt module Jobs, Motor Pool, Smart Uploads. Fleetio: `Xem` đủ trang. Đơn vị và định dạng là tham số mới, chưa có mã.
- P3 [Mới] [Lõi] [Cấu hình] **Luật bật tắt có giải thích ngay dưới ô:** ví dụ bắt số km khi đóng lệnh kèm danh sách loại xe được miễn. Fleetio: `Xem`. Câu mô tả ghi rõ tác động và phạm vi ("This requirement only applies to future Work Orders or Service Entries."). Require Meter kèm Excluded Vehicle Types là mẫu đúng cho mooc không có đồng hồ.
- P4 [Mới] [Lõi] **Trang đầu "Needs Attention":** thẻ đếm dẫn thẳng tới danh sách đã lọc; mỗi thẻ tải riêng, có "0 minutes ago", Refresh, lọc All groups. Fleetio: `Chạy` bấm từng thẻ, ghi đích (SRS Mục 13.6). Áp vào `common-workspace`.
- P5 [Mới] [Lõi] **Danh sách chuẩn:** tab đếm số, lọc nhanh, nhóm điều kiện, chọn cột, lưu chế độ xem, tab tự tạo, xem nhanh bản ghi. Fleetio: `Xem`. Áp vào `common-workspace`.
- P6 [Mới] [Lõi] **Khởi tạo khách mới:** danh sách Get Started, dữ liệu mẫu có nhãn Sample, tắt được một nút; xe Sample không tính vào hạn mức gói. Fleetio: `Chạy` (bộ đếm đổi khi tạo xe; 25 xe tính cả Sample nhưng hạn mức chỉ đếm 5 xe TEST). Áp vào OQ-7.
- P23 [Mới] [Lõi] **Một bảng Liên hệ, phân vai bằng tick:** Operator ("Allow this Contact to be assigned to assets"), Employee, Technician ("Allow this Contact to be selected in labor line items on work orders"); Người dùng là liên hệ được bật Enable Access to Fleetio, mặc định No Access. Fleetio: `Chạy`. Lái xe, thợ, kế toán chung một hồ sơ; chỉ liên hệ có tick Operator mới gán được xe. Áp vào `organization`, `account-access`.
- P24 [Mới] [Lõi] [Cấu hình] **Nhóm nhiều cấp làm khung phạm vi:** Groups & Subgroups dạng cây; Record Set có điều kiện "Vehicles in this contact's group"; Require Group chỉ mở khi mọi tài sản và liên hệ đã có nhóm, màn liệt kê số còn thiếu ("5 Vehicles", "3 Contacts"). Fleetio: `Xem`. Dùng được cho cấp Chi nhánh; Công ty, Cơ sở phải tự xếp thành cây.
- P25 [Mới] [Lõi] [Cấu hình] **Khung trạng thái cố định, nhãn theo khách:** Work Order có Type cố định Incomplete, Completed, khách thêm tên trạng thái; Purchase Order 8 trạng thái cố định, không có Add. Fleetio: `Xem`. Khớp đúng "Lõi khung trạng thái + Cấu hình nhãn" của `saas-core-vs-tenant.md`.

### P1 — should have

- P7 [Mới] [Cấu hình] **Tự động hoá Trigger, Điều kiện, Hành động** với 18 mẫu: Work Orders 6, Issues 5, Purchase Orders 3, Faults 2, Service Entries 2. Loại bản ghi trigger: Work Order, Service Entry, Fault, Issue, Purchase Order, Geofence Event, Vehicle; kiểu sự kiện Created, Updated, Created or Updated, Deleted. Hành động với Issue: Update Field, Add Comment, Send Email; Create Record tạo Work Order. Điều kiện cho Issue có 59 trường, All of, Any of, nhóm lồng, không phân biệt hoa thường. Fleetio: `Chạy` tạo 3 automation, chạy Add Comment, Update Field, Create Record (trước đây chỉ `Xem` mẫu).
- P8 [Mới] [Cấu hình] **Gợi ý tự động hoá đúng ngữ cảnh:** vừa tạo sự cố xong bật hộp gợi ý mẫu "tạo lệnh khi có sự cố". Fleetio: `Chạy`. Cách bán tính năng rất tự nhiên, nhưng dễ gây phiền nếu lặp.
- P9 [Mới] [Lõi] **Theo dõi, bình luận, nhắc tên** trên mọi bản ghi; người tạo tự thành người theo dõi; bình luận do automation ghi tác giả "Fleetio Automation". Fleetio: `Chạy` tự theo dõi và comment do automation.
- P10 [Mới] [Cấu hình] **Hồ sơ thông báo** gán cho người (gán hàng loạt từ Contacts), nhóm xe theo dõi có cột Direct Watchers, Total Watchers. Fleetio: `Xem` 0 hồ sơ, 11 nhóm theo dõi.
- P11 [Mới] [Gói: Bảo dưỡng đội xe] **49 báo cáo trong 13 nhóm** (Vehicles 14, Vehicle Assignments 2, Inspections 4, Issues 2, Service 8, Warranties 2, Work Orders 5, Contacts 2, Parts 4, Fuel 3, Tools 1, Jobs 1, Motor Pools 1), có yêu thích, lưu, chia sẻ; 4 báo cáo gắn "Upgrading soon". Trang báo cáo có biểu đồ, Filters, Columns, Export CSV (cột đang hiện hoặc mọi cột), Print. Fleetio: `Xem` 49 tên, `Chạy` mở sâu Issues Report. Bản 02/11 ghi 48 báo cáo 12 nhóm là sai. Dùng làm danh mục để chọn cho `workshop-reports`.
- P12 [Mới] [Lõi] **Tìm kiếm toàn cục** theo 15 loại bản ghi. Fleetio: `Xem`.
- P13 [Mới] [Lõi] **Lịch sử bản ghi** (View Record History) và lịch sử đổi của từng trường như trạng thái; có trên xe và trên automation. Fleetio: `Xem` nút.
- P14 [Mới] [Cấu hình] **Kho tài liệu chung,** biết file gắn với bản ghi nào: cột File Name, File Size, Location, Auto-Delete, Attached To, Labels. Fleetio: `Xem` khung rỗng, không tải tệp.
- P15 [Mới] [Lõi] [Cấu hình] **Giới hạn theo gói hiển thị rõ và chặn thật:** Account Usage hiện đã dùng trên giới hạn (Fleetio: Documents 250.0 GB, Roles 30, Vehicles 5, Automations 75, Custom Records 25); hết hạn mức thì Save báo "Your plan is limited to 5 vehicles" kể cả khi đủ trường, danh sách xe hiện "5 of 5", nút Add Vehicle có khoá. Fleetio: `Chạy` bị chặn thật. Bản 02/11 đọc Roles là 50 từ ảnh mờ, đúng là 30. Áp vào phần bán gói; giá trị theo hợp đồng là tham số mới, chưa có mã.
- P16 [Mới] [Lõi] **Câu hỏi dữ liệu bằng ngôn ngữ tự nhiên** (Ask a data question): mở AI Data Analyst, khung nhúng từ ThoughtSpot, có Show work, lưu My Conversations. Fleetio: `Chạy` 2 câu, cả 2 trả số sai so với trang xe (Điểm yếu W2).
- P26 [Mới] [Cấu hình] **Lưu ở trạng thái tắt, bật phải xác nhận, lúc bật mới sinh phiên bản:** hộp "When you enable this automation ... actions will run when you set the trigger and conditions are met."; bật sinh v.1 và ghi Enabled At; bật không chạy bù cho bản ghi đã có. Fleetio: `Chạy`. Khách thử luật an toàn, không sợ luật vừa lưu đã chạy trên dữ liệu thật.
- P27 [Mới] [Cấu hình] **Nhật ký từng lượt chạy:** danh sách có Total Runs, Successful Runs, Failed Runs, Last Run At, Current Version; mỗi lượt có Run Result ghi phiên bản, bản ghi kích hoạt, Triggered By, log JSON; lượt không khớp điều kiện không được đếm. Fleetio: `Chạy`. Đội hỗ trợ tra được vì sao bản ghi tự đổi.
- P28 [Mới] [Cấu hình] **Lưu trữ thay cho xoá:** Archive tắt ngay không cần tắt trước, bản lưu trữ chỉ đọc, Restore về trạng thái tắt, không tự bật lại. Fleetio: `Chạy`.
- P29 [Mới] [Cấu hình] **Hành động tạo lệnh bị giới hạn trạng thái chưa xong:** Create Record chỉ cho Open, Pending, không có Completed; Work Order sinh ra nối ngược về sự cố ở cột Resolved Issues. Fleetio: `Chạy` Issue #44 sinh WO #105. Tránh lối tắt bỏ qua kiểm số km khi hoàn tất.
- P30 [Mới] [Cấu hình] **Mẫu "lệnh xong và xe không còn lệnh mở thì xe về Active":** điều kiện đếm Vehicle Incomplete Work Orders Count nhỏ hơn 1. Fleetio: `Chạy` đọc định nghĩa mẫu, chưa bật vì sẽ sửa xe của nhóm khác. Với đầu kéo có nhiều lệnh sửa song song, điều kiện đếm này rất đáng lấy.
- P31 [Mới] [Lõi] [Cấu hình] **Chính sách mật khẩu theo khách:** độ dài tối thiểu, hạn đổi, yêu cầu ký tự, số lần sai, thời gian khoá, đặt lại mọi mật khẩu; không áp cho đăng nhập SAML. Fleetio: `Xem` (lựa chọn đọc được: độ dài 8, 15, 30, 50; hạn None, 30, 60, 90 ngày; sai 5 hoặc 10 lần; khoá 5, 10, 30 phút). Đối chiếu `account-access`.
- P32 [Mới] [Lõi] **Cảnh báo chi phí ngay tại quyền:** quyền Create của Vehicles có câu "Adding new Vehicles will result in additional charges to your account's subscription." Fleetio: `Xem`. Lấy nếu tính tiền theo xe.

### P2 — nice to have

- P17 [Mới] [Gói: Khách lớn, chưa có trong danh sách gói] **Bản ghi tự tạo:** loại bản ghi, trường, liên kết, bố cục kéo thả, trang danh sách, trang chi tiết. Fleetio: `Docs` (Early Access, gói Premium); không mở theo lựa chọn của user.
- P18 [Mới] [Cấu hình] **Trường tuỳ chỉnh:** nhãn duy nhất theo loại bản ghi, không đổi được kiểu dữ liệu sau khi lưu; chỉ trường chọn và tick dùng được cho Record Set. Fleetio: `Docs`, `Xem` Standard Records liệt kê 15 loại bản ghi, đều 0 trường.
- P19 [Mới] [Gói: Khách lớn, chưa có trong danh sách gói] **API key, Webhook, SAML, kết nối ngoài** (Integration Links kèm biến; External Connections FTP, SFTP, Amazon S3 cho báo cáo định kỳ). Fleetio: `Xem` trang rỗng, không tạo. Áp vào `account-access`.
- P20 [Mới] [Gói: Khách lớn, chưa có trong danh sách gói] **Máy chủ MCP** để nối trợ lý AI: "Each connection respects the user's role permissions."; module Fleetio MCP mức không có ở cả 4 vai mặc định. Fleetio: `Xem`, tắt mặc định, không bật.
- P21 [Mới] [Gói: Khách lớn, chưa có trong danh sách gói] **Sandbox và xuất toàn bộ dữ liệu:** Sample Copy, Production Copy có hạn mức riêng (tài khoản: 0/2 và 0/0); Export Account Data 13 loại dữ liệu, CSV hoặc XLS, gửi qua email, link hết hạn (Fleetio: 7 ngày). Fleetio: `Xem`, không bấm.
- P22 [Mới] [Cấu hình] **Widget tuỳ chỉnh cho trang đầu.** Fleetio: `Xem` trang rỗng.
- P33 [Mới] [Gói: Bảo dưỡng đội xe] **Thu hồi của hãng (Recall):** nhập tự động theo năm, hãng, đời xe từ nguồn công khai của Mỹ; tab All, Needs Action, Open, Resolved, Acknowledged; một mẫu tự động hoá nâng sự cố lên Critical khi nguồn là Recall. Fleetio: `Xem` 261 dòng Sample. Ở Việt Nam chưa thấy nguồn tương đương (`Suy`).
- P34 [Mới] [Gói: Khách lớn, chưa có trong danh sách gói] **Đặt xe dùng chung (Motor Pool):** danh sách đặt xe, bảng giá đặt xe, phí cố định, quyền nhận xe, trả xe, huỷ. Fleetio: `Xem` danh sách rỗng, không chạy vì cần tạo Motor Pool trong Settings.
- P35 [Mới] [Cấu hình] **Trợ lý AI cho bảo dưỡng:** Issue Prioritization, Issue Resolution, Fault Monitoring, Service Assessments, Service Writer, mỗi cái bật riêng, có câu điều khoản. Sự cố mới có mức ưu tiên "Auto-assign" và tự thành High dù không nhập (Issue #40, #42). Fleetio: `Chạy` phần thấy được; nguyên nhân là AI Issue Prioritization là `Suy`. Đối chiếu NFR-006 của SRS.
- P36 [Mới] [Lõi] **Chia sẻ báo cáo bằng link có hạn, có danh sách thu hồi:** Reports › Shared liệt kê link, Unshare có hộp xác nhận, thu hồi xong mở lại không còn dữ liệu. Fleetio: `Chạy`. Chỉ học hạn và danh sách thu hồi, KHÔNG học cách sinh link (Điểm yếu W1).

### Điểm yếu cần làm khác

- W1 [Mới] [Lõi] **Chia sẻ ra ngoài phải là hành động chủ động.** Fleetio: `Chạy` bấm Share là sinh NGAY link công khai, không hỏi, "this link allows anyone with access to view all data"; lối "click here to unshare" trong hộp không có tác dụng, bấm lại trả 404, link vẫn sống; chỉ Reports › Shared › Unshare mới thu hồi được. Đề xuất Invlogis: mở hộp không sinh link, có bước bấm tạo, nói rõ phạm vi dữ liệu, thu hồi có hiệu lực ở mọi lối, ghi nhật ký tạo, mở, thu hồi.
- W2 [Mới] [Lõi] **Số do AI trả phải ghi dữ liệu đến thời điểm nào.** Fleetio: `Chạy` hỏi số sự cố mở của TEST-XE-01, AI trả "currently has 2 open issues" khi trang xe có 7; hỏi km mới nhất, AI trả 1.700 khi thật là 2.999 km; không cảnh báo, không ghi độ trễ. Khả năng kho phân tích trễ là `Suy`. Đề xuất Invlogis: mọi số AI trả kèm "dữ liệu đến thời điểm" và lối mở bản ghi gốc.
- W3 [Mới] [Cấu hình] **Lượt do máy gây ra phải ghi máy là nguồn.** Fleetio: `Chạy` lượt Update do automation tự gây ra vẫn ghi "Triggered By" là người tạo sự cố. Đề xuất Invlogis ghi rõ automation nào, phiên bản nào.
- W4 [Mới] [Cấu hình] **Kết quả lượt chạy phải phản ánh đúng việc đã làm.** Fleetio: `Chạy` lượt thêm comment ghi "Records: No records changed".
- W5 [Mới] [Lõi] [Cấu hình] **Có trần lượt chạy theo khách.** Fleetio: `Chạy` automation tự kích hoạt lại chính nó 2 lượt rồi dừng vì giá trị không đổi; tài liệu hãng không nêu chống vòng lặp, giới hạn lượt, hành vi khi hành động lỗi; vòng lặp chéo hai automation chưa thử. Đề xuất Invlogis: trần lượt chạy theo khách, tham số mới, chưa có mã.
- W6 [Mới] [Lõi] **Chặn hoặc cảnh báo trùng người.** Fleetio: `Chạy` tạo lại liên hệ cùng tên, không email, lưu được, không cảnh báo.
- W7 [Mới] [Lõi] **Bộ đếm khởi tạo phải nhất quán.** Fleetio: `Chạy` "Get Started" hiện 3/5 ở trang này, 3/6 ở trang khác.
- W8 [Mới] [Lõi] **Thông báo nền không che nội dung.** Fleetio: `Chạy` toast "Calculating Service Reminders Compliance" lặp nhiều lượt và che màn.

## 5. Core Flows (Happy Path)

### 5.1 Khách mới vào hệ thống

`Chạy` một phần ở tài khoản dùng thử.

1. Đăng ký, có sẵn dữ liệu mẫu có nhãn Sample; xe Sample không tính vào hạn mức gói.
2. Làm theo danh sách Get Started (Onboarding Tasks trỏ 7 đường dẫn); bộ đếm tăng khi hoàn thành.
3. Mỗi trang có khung Learn giải thích, có thể đóng.
4. Tạo dữ liệu thật đến khi chạm hạn mức gói thì bị chặn ở bước lưu.
5. Tắt dữ liệu mẫu khi sẵn sàng.

```
Đăng ký ─> Dữ liệu mẫu + Get Started ─> Tạo dữ liệu thật ─┬─> Tắt Sample
                                                          └─> Hết hạn mức ─> "Your plan is limited to 5 vehicles"
```

### 5.2 Cấp quyền người dùng

`Xem` cấu hình, chưa mời người nên chưa kiểm hiệu lực.

```
Liên hệ ─┬─ Phân vai: Operator (gán xe) · Technician (ghi công) · Employee
         ├─ Truy cập: No Access (mặc định) | Enable Access ─> thành Người dùng
         ├─ Role: được làm gì (Fleet Manager, Operator, Technician, Viewer)
         └─ Record Set: trên dữ liệu nào, Manage và View riêng
                        (xe được giao, nhóm của người dùng, xe cụ thể, theo trạng thái, theo trường tuỳ chỉnh)
```

### 5.3 Tự động hoá

`Chạy` trọn vòng tạo, bật, chạy, tắt, lưu trữ, khôi phục.

```
Mẫu hoặc trống ─> Trigger + Điều kiện + Hành động ─> Lưu (tắt)
   ─> Bật (xác nhận, sinh v.1) ─> Sự kiện khớp ─> Hành động ─> Lượt chạy ghi SUCCESS
                                └─ Không khớp ─> Không ghi lượt
   ─> Tắt (xác nhận) | Archive (tắt ngay, chỉ đọc) ─> Restore (về tắt)
```

Kết quả thật: Issue #40 tạo lúc automation tắt không có comment, bật lên cũng không chạy bù; Issue #42 tạo lúc bật có comment trong khoảng 6 giây; Issue #43 khớp hai automation thì cả hai chạy; Issue #44 sinh Work Order #105 trạng thái Open. Ví dụ mẫu có sẵn: tự duyệt đơn mua dưới ngưỡng (Fleetio: 10.000 ₫), đổi xe sang In Shop khi sự cố đến từ kiểm tra hỏng, email khi lịch sử dịch vụ vượt số tiền (Fleetio: 100.000 ₫), tạo lệnh theo dõi sau khi thay lốp, bỏ qua mã lỗi phiền, nâng sự cố lên Critical khi có áp suất dầu thấp. Bảng đủ 18 mẫu ở SRS Mục 17.

### 5.4 Chia sẻ báo cáo

`Chạy`, link đã thu hồi.

```
Mở báo cáo ─> Share ─> Link công khai có ngay (hết hạn 7 ngày)
   ─> "click here to unshare" ─> không tác dụng, link vẫn sống
   ─> Reports › Shared › Unshare ─> xác nhận ─> link chết
```

### 5.5 Hỏi dữ liệu bằng lời

`Chạy` 2 câu.

```
Ask a data question ─> AI Data Analyst ─> gõ câu hỏi ─> bảng + câu trả lời (40 đến 50 giây)
   ─> Show work xem cách tính ─> đối chiếu tay mới biết số sai
```

## 6. System Behavior Deep Dive

### 6.1 Decision Points

| ID | Flow | Khi nào | YES | NO |
|---|---|---|---|---|
| D1 | 5.2 | Người dùng là lái xe | Record Set chỉ xe được giao | Theo nhóm hoặc toàn bộ |
| D2 | 5.3 | Automation đang bật và điều kiện đúng | Chạy hành động, ghi lượt | Bỏ qua, không ghi lượt |
| D3 | 5.3 | Hành động đổi chính bản ghi và trigger gồm Updated | Kích hoạt lại; dừng khi giá trị không đổi | Dừng |
| D4 | 5.1 | Đã chạm hạn mức gói | Chặn lưu, khoá nút | Lưu |
| D5 | 5.2 | Liên hệ có tick Operator | Gán được xe | Câu dẫn "Contact must have operator classification to be assigned to vehicles" |
| D6 | 5.4 | Thu hồi qua lối nào | Reports › Shared: link chết | Trong hộp: link vẫn sống |

### 6.3 State Transitions

Automation (`Chạy`):

| Từ | Hành động | Sang | Ghi chú |
|---|---|---|---|
| Chưa lưu | Save Automation | Disabled | Save mờ cho tới khi có trigger, hành động; rời trang không để lại bản rác |
| Disabled | Bật, xác nhận | Enabled | Sinh v.1, ghi Enabled At |
| Enabled | Tắt, xác nhận | Disabled | "it will stop working and prevent any actions from running." |
| Enabled hoặc Disabled | Archive | Archived | Tắt ngay, ghi Disabled At |
| Archived | Restore | Disabled | Không tự bật lại; "Record successfully restored" |
| Archived | Delete | — | Có nút, không bấm |

Xe có 5 trạng thái danh mục Active (Default), In Shop, Inactive, Out of Service, Sold, đổi tự do không có luật chuyển (`Xem`). Đủ sơ đồ và ma trận ở [[docs/_research/fleetio/srs/fleetio-saas-platform-states.md|States]].

### 6.5 Other Edge Cases

- **Banner múi giờ:** đầu trang cảnh báo khi múi giờ thiết bị khác cài đặt (`Xem`), đề xuất giữ cho khách nhiều chi nhánh, nhưng cần nút tắt hẳn.
- **Luật chỉ áp về sau:** nhiều luật ghi "only applies to future" (`Xem`). Invlogis nên nói rõ tương tự để tránh tưởng dữ liệu cũ sai.
- **Tự động hoá không chạy bù:** bật luật sau khi bản ghi đã có thì bản ghi cũ không được xử lý (`Chạy`). Invlogis cần nói rõ trong hộp bật, hoặc có nút chạy cho dữ liệu cũ.
- **Toast nổi trùng lặp:** thông báo nền lặp nhiều lượt và che nội dung (`Chạy`). Không nên học.
- **Nút đi nơi khác:** "Manage Users" trỏ sang danh sách người dùng ngoài Settings, "Integrations Directory" mở trang ngoài (`Xem`).
- **Thanh lý xe chỉ là trường dữ liệu:** Out-of-Service là ngày và số km, không có nút thanh lý (`Xem`).
- **Đơn vị lẫn trên form xe:** Odometer trong Financial hiện "mi" khi Specifications hiện cm, kg, lít (`Xem`, chưa rõ lý do).
- **Trial bật ngoài ý muốn:** cuối lượt chạy, add-on Tools đổi sang "Trialing", "14 days left in trial" mà nhóm này không bấm (`Xem`). Invlogis cần nhật ký thay đổi gói.

## 7. Validation, Limits & Wording

### 7.1 Validation rules

| Trường | Luật | Câu báo | Mức |
|---|---|---|---|
| Vehicle Name | Bắt buộc | "can't be blank" + toast "Vehicle could not be created" | `Chạy` |
| Liên hệ | Chỉ cần First Name, email không bắt buộc, trùng tên không chặn | — | `Chạy` |
| Gán xe cho liên hệ | Phải có tick Operator | "Contact must have operator classification to be assigned to vehicles" | `Chạy` |
| Record Type của Record Set | Không đổi sau khi tạo | "can't be changed after creation" | `Xem` |
| Require Group | Mọi tài sản, liên hệ phải có nhóm | "all existing assets and contacts must be assigned a group" | `Xem` |
| Save automation | Phải có trigger và hành động | Nút Save mờ | `Chạy` |

### 7.2 Limits & Quotas (exact values)

| Tham số | Giá trị | Window | Behavior khi vượt |
|---|---|---|---|
| Xe | Fleetio: 5, gói đang dùng; Sample không tính | Theo gói | Chặn lưu, "Your plan is limited to 5 vehicles", nút Add Vehicle khoá (`Chạy`) |
| Vai trò | Fleetio: 30, đang dùng 4 | Theo gói | Chưa thử |
| Tự động hoá | Fleetio: 75, đang dùng 0 lúc đọc | Theo gói | Chưa thử |
| Bản ghi tự tạo | Fleetio: 25 | Theo gói | Chưa thử |
| Tài liệu | Fleetio: 250.0 GB | Theo gói | Chưa thử |
| Sandbox | Fleetio: Sample Copy 2, Production Copy 0 | Theo gói | Chưa thử |
| Link chia sẻ báo cáo | Fleetio: 7 ngày | Mỗi link | Chưa chờ hết hạn |
| Link xuất toàn bộ dữ liệu | Fleetio: 7 ngày | Mỗi lần xuất | Chưa thử |
| Lượt tự kích hoạt | Thấy dừng sau 2 lượt khi giá trị không đổi; trần không công bố | Mỗi sự kiện | Chưa biết |

### 7.3 Wording samples (exact strings)

#### Error messages

| Tình huống | Wording |
|---|---|
| Hết hạn mức xe | "Your plan is limited to 5 vehicles" |
| Không có quyền | "You are not authorized to perform this action." |
| Sửa bản đã lưu trữ | "Archived records are read-only and cannot be updated." |

#### Info / neutral messages

| Tình huống | Wording |
|---|---|
| Bật automation | "When you enable this automation ... actions will run when you set the trigger and conditions are met." |
| Tắt automation | "When you disable this automation ... it will stop working and prevent any actions from running." |
| Archive automation | "This will disable the automation and it will stop working immediately. It can be restored at any time." |
| Liên hệ không truy cập | "This Contact will not have access to your Fleetio account and will not receive any notifications." |
| Chia sẻ báo cáo | "Link expires in 7 days", "this link allows anyone with access to view all data" |
| Thu hồi chia sẻ | "Are you sure you want to unshare this report?" |
| Thêm xe tốn tiền | "Adding new Vehicles will result in additional charges to your account's subscription." |
| Trách nhiệm khi dùng AI | Khách hàng tự chịu trách nhiệm xem xét và quyết định theo gợi ý AI (tóm tắt nội dung trang AI Service Advisor) |
| Dữ liệu mẫu | "Vehicles and other records labeled as Sample are available to help you explore how Fleetio works during your trial." |

## 8. Assumptions

- Invlogis đi theo hướng khách tự cấu hình trong `tenant-parameters.md`, không làm riêng.
- `GĐ` Giai đoạn đầu chỉ cần luật có tham số, chưa cần công cụ tự động hoá tổng quát. Lượt chạy củng cố: mẫu đủ dùng với luật đơn giản, nhưng không thấy chống vòng lặp nên công cụ tổng quát có rủi ro.
- `GĐ` Mô hình Role và Record Set dùng được cho cấp Chi nhánh qua nhóm nhiều cấp; cấp Công ty, Cơ sở và quyền theo ca cần thêm một lớp phạm vi.

## 9. Risks

| Rủi ro | Mức | Giảm thiểu |
|---|---|---|
| Quá nhiều tuỳ chọn làm admin khách rối | Trung | Giá trị mặc định tốt, mô tả rõ tác động |
| Tự động hoá gây chuỗi thay đổi khó truy | Cao | Nhật ký lượt chạy ghi đúng nguồn, trần lượt chạy, lưu ở trạng thái tắt |
| Chia sẻ báo cáo làm lộ dữ liệu ra ngoài | Cao | Tạo link chủ động, thu hồi ở mọi lối, nhật ký |
| AI trả số sai mà người dùng tin | Cao | Ghi thời điểm dữ liệu, lối đối chiếu bản ghi gốc |
| Làm bản ghi tự tạo quá sớm tốn công lớn | Cao | Để sau, chỉ làm khi có khách cần |

## 10. Success Criteria (preliminary)

- Khách thứ hai chạy được mà không sửa lõi; đây cũng là mục tiêu OQ-7 của PRD.
- Người dùng mới làm được bản ghi đầu tiên không cần đào tạo.
- Mọi thay đổi do tự động hoá truy được về luật và phiên bản gây ra.

## 11. Open Questions

| ID | Câu hỏi | Trả lời hiện có | Nguồn khách |
|---|---|---|---|
| OQ-1 | Mô hình Role và Record Set có khớp với quyền theo Công ty, Chi nhánh, Cơ sở không? | Đã trả lời (`Xem`): khớp Chi nhánh bằng nhóm nhiều cấp và điều kiện "Vehicles in this contact's group"; Công ty, Cơ sở phải tự xếp thành cây nhóm; không có quyền theo thời hạn hay ca trực. Hiệu lực thật xem OQ-8 | Câu hỏi nội bộ |
| OQ-2 | Giai đoạn đầu có cần công cụ tự động hoá tổng quát không, hay chỉ các luật có tham số? | Thông tin mới (`Chạy`): mẫu đủ dùng với luật đơn giản, không thấy chống vòng lặp. Quyết định của đội sản phẩm còn mở | Câu hỏi nội bộ |
| OQ-3 | Dữ liệu mẫu cho khách mới của Invlogis lấy từ đâu mà không lộ dữ liệu Delta? | Fleetio dùng bộ Sample riêng, không tính hạn mức. Quyết định của Invlogis còn mở | Câu hỏi nội bộ |
| OQ-4 | Tên gói cho API, SAML, sandbox của Invlogis? | Fleetio tách Sandbox, MCP theo hạn mức gói (`Xem`). Tên gói của Invlogis còn mở | Câu hỏi nội bộ |
| OQ-5 | Hai automation lật giá trị của nhau có bị chặn không, trần bao nhiêu lượt? | Chưa chạy; tài liệu hãng không nêu | Câu hỏi nội bộ |
| OQ-6 | Lượt automation thất bại trông thế nào, có thử lại không? | Không tái hiện được; Failed Runs luôn 0 | Câu hỏi nội bộ |
| OQ-7 | Sửa automation đang bật có sinh v.2 không; Make a Copy, Delete, trigger Vehicle, Send Email chạy ra sao? | Chưa chạy | Câu hỏi nội bộ |
| OQ-8 | Role và Record Set có chặn đúng như khai không? | Chưa kiểm; cần mời người dùng thử theo từng vai | Câu hỏi nội bộ |
| OQ-9 | Technician có quyền gì với Fuel Entries? | Ma trận ghi "không", ghi chú cùng lượt ghi "chỉ có ô xem"; cần mở lại | Câu hỏi nội bộ |
| OQ-10 | Settings có bao nhiêu trang? | Bản 02/11 ghi khoảng 65, lượt chạy kê 56 tên trang; chưa đếm lại trên menu | Câu hỏi nội bộ |
| OQ-11 | Cột và lọc của 48 báo cáo chưa mở, Saved Reports là gì? | Chỉ mở sâu Issues Report | Câu hỏi nội bộ |
| OQ-12 | Đổi trạng thái xe thật, lưu trữ xe, xe trùng tên, đặt xe dùng chung chạy thế nào? | Chưa chạy vì hạn mức xe đã đầy | Câu hỏi nội bộ |
| OQ-13 | AI Data Analyst sai vì kho phân tích trễ hay vì cách đếm? | Mới là `Suy` | Câu hỏi nội bộ |

Danh sách câu hỏi mở đầy đủ, kể cả OQ-14, OQ-15 về mẫu email và đơn vị trên form xe, ở SRS Mục 12.

## 12. Next Steps

- Đưa P1, P2, P3, P6, P23, P24, P25 vào phần chốt OQ-7 của PRD khi review.
- Đưa W1, W2, W3, W5 vào yêu cầu phi chức năng chung của Invlogis (chia sẻ ra ngoài, AI, nhật ký, trần tự động hoá).
- Đối chiếu P5 với mẫu danh sách trong design system.
