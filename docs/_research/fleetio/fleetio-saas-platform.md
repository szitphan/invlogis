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

> Khuyến nghị: **Nên tham khảo mạnh** cho phần cấu hình theo khách (OQ-7 của PRD), mô hình quyền và khung tự động hoá. Đây là phần có ích cho Invlogis sớm nhất vì không phụ thuộc Gói Bảo dưỡng đội xe. Lượt chạy 03/11/2026 đã tạo, bật, chạy, tắt, lưu trữ tự động hoá thật và thử chia sẻ báo cáo, hỏi dữ liệu bằng lời; hai chỗ sau lộ điểm yếu nặng (Mục 4 "Điểm yếu cần làm khác"). Lượt 3 tái hiện được lượt automation thất bại, đo sửa khi đang bật và luật ghi đè thao tác tay, đọc cột 48/49 báo cáo: khung tự động hoá đáng học nhưng lỗi, xung đột với người dùng và phiên bản còn hở. Phần "Đề xuất cho Invlogis" tách riêng; không phần nào là yêu cầu đã chốt.

## 1. Idea Seed

Luật nghiệp vụ là thứ khách tự bật tắt, không phải code riêng. Quyền tách làm hai lớp: làm được gì (Role) và trên dữ liệu nào (Record Set), trong Record Set lại tách quyền sửa (Manage) và quyền xem (View). Tự động hoá theo mẫu Trigger, Điều kiện, Hành động: lưu xong ở trạng thái tắt, bật phải xác nhận, mỗi lượt chạy có nhật ký. Lái xe, thợ, kế toán chung một hồ sơ Liên hệ; người dùng chỉ là liên hệ được bật truy cập. Khách mới có dữ liệu mẫu không tính vào hạn mức gói và hướng dẫn ngay trên từng trang.

## 2. Context

**Feature Invlogis liên quan:** OQ-7 của PRD (cấu hình và khởi tạo khách mới chưa thành feature), `access-control` (#5), `organization` (#6), `common-workspace` (#2), `help-center` (#4), `workshop-reports`, `account-access` (#1), `cross-process-flow` (#3).

**Nguồn và bằng chứng:**

- Lượt 1, 2026-11-02, tài khoản dùng thử: xem trang đầu, báo cáo, trình dựng tự động hoá, khoảng 20 trang Settings, Record Sets.
- Lượt 2, 2026-11-03, cùng tài khoản, tiền tố dữ liệu `TEST-NEN`: automation 96373 `TEST-NEN-AUTO-01`, 96375 `TEST-NEN-AUTO-02`, 96376 `TEST-NEN-AUTO-03` (đều đang tắt); Issue #40, #42, #43, #44 trên xe dùng chung TEST-XE-01; Work Order #105 sinh từ automation; hai liên hệ `TEST-NEN-LH-01`. Đọc 56 tên trang Settings, mở Edit Role cả 4 vai (bấm Cancel), đọc 18 mẫu tự động hoá, 49 tên báo cáo. Chi tiết từng case ở [[docs/_research/fleetio/srs/fleetio-saas-platform-spec.md|SRS]] Mục 13.
- Lượt 4, 2026-11-03: automation `TEST-NEN-AUTO-07` trên Service Entry, `TEST-NEN-AUTO-08` trên Purchase Order, `TEST-NEN-AUTO-09` trên Fault (đều đã tắt), đo Archive, Restore, hạn mức khi đang bật; đọc nhãn bộ lọc 48 báo cáo, lọc thật `purchase_orders`.
- Lượt 3, 2026-11-03, cùng tiền tố: automation `TEST-NEN-AUTO-04` đến `06` (đều đã tắt), AUTO-01 lên v.2; Issue #54, #55, Work Order #111, tệp `TEST-NEN-tailieu.txt` trên TEST-DAUKEO-2; báo cáo Private `TEST-NEN-BC-01`, view Private `TEST-NEN-VIEW-01`. Mở từng báo cáo chỉ đọc, đếm menu Settings, đọc thêm các trang chỉ đọc. Đủ 49 tên, cột ở SRS Mục 21.
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

- P1 [Mới] [Lõi] [Cấu hình] **Quyền hai lớp:** Role cho hành động (4 vai có sẵn, 30 module, mỗi module mức đủ, một phần, không, có quyền con như `update_status`, `archive_delete`, PO `approve` tách `receive`); Record Set cho phạm vi dữ liệu trên Xe, Liên hệ, Kho phụ tùng, Biểu mẫu kiểm tra, tách Manage và View. Fleetio: `Xem` mở Edit Role cả 4 vai và Record Set, chưa kiểm hiệu lực thật vì không mời người, lượt 3 vẫn vậy. Lượt 3 chốt Technician với Fuel Entries là None, không có ô con. Sát với quyền theo chi nhánh của `access-control`.
- P2 [Mới] [Lõi] [Cấu hình] **Thiết lập chung theo khách:** tiền tệ, định dạng ngày, múi giờ, 12 hoặc 24 giờ, đơn vị số đo, đơn vị nhiên liệu, hệ đo lường, gọi đối tượng là Vehicle hay Asset, thuế, bật tắt module Jobs, Motor Pool, Smart Uploads. Fleetio: `Xem` đủ trang. Đơn vị và định dạng là tham số mới, chưa có mã.
- P3 [Mới] [Lõi] [Cấu hình] **Luật bật tắt có giải thích ngay dưới ô:** ví dụ bắt số km khi đóng lệnh kèm danh sách loại xe được miễn. Fleetio: `Xem`. Câu mô tả ghi rõ tác động và phạm vi ("This requirement only applies to future Work Orders or Service Entries."). Require Meter kèm Excluded Vehicle Types là mẫu đúng cho mooc không có đồng hồ.
- P4 [Mới] [Lõi] **Trang đầu "Needs Attention":** thẻ đếm dẫn thẳng tới danh sách đã lọc; mỗi thẻ tải riêng, có "0 minutes ago", Refresh, lọc All groups. Fleetio: `Chạy` bấm từng thẻ, ghi đích (SRS Mục 13.6). Áp vào `common-workspace`.
- P5 [Mới] [Lõi] **Danh sách chuẩn:** tab đếm số, lọc nhanh, nhóm điều kiện, nhóm dòng, chọn cột kéo đổi thứ tự có Restore defaults, số dòng 50, 100, 200, mật độ Default, Compact, tab tự tạo, trang nhớ tab dùng lần trước, menu dòng theo nghiệp vụ (Add to Work Order, Resolve with Note...). Fleetio: `Chạy` lượt 3 trên Issues. Xem nhanh bản ghi: bấm dòng trên Issues sang thẳng trang chi tiết, không thấy peek. Áp vào `common-workspace`.
- P6 [Mới] [Lõi] **Khởi tạo khách mới:** danh sách Get Started, dữ liệu mẫu có nhãn Sample, tắt được một nút; xe Sample không tính vào hạn mức gói. Fleetio: `Chạy` (bộ đếm đổi khi tạo xe; 25 xe tính cả Sample nhưng hạn mức chỉ đếm 5 xe TEST). Áp vào OQ-7.
- P23 [Mới] [Lõi] **Một bảng Liên hệ, phân vai bằng tick:** Operator ("Allow this Contact to be assigned to assets"), Employee, Technician ("Allow this Contact to be selected in labor line items on work orders"); Người dùng là liên hệ được bật Enable Access to Fleetio, mặc định No Access. Fleetio: `Chạy`. Lái xe, thợ, kế toán chung một hồ sơ; chỉ liên hệ có tick Operator mới gán được xe. Áp vào `organization`, `account-access`.
- P24 [Mới] [Lõi] [Cấu hình] **Nhóm nhiều cấp làm khung phạm vi:** Groups & Subgroups dạng cây; Record Set có điều kiện "Vehicles in this contact's group"; Require Group chỉ mở khi mọi tài sản và liên hệ đã có nhóm, màn liệt kê số còn thiếu ("5 Vehicles", "3 Contacts"). Fleetio: `Xem`. Dùng được cho cấp Chi nhánh; Công ty, Cơ sở phải tự xếp thành cây.
- P25 [Mới] [Lõi] [Cấu hình] **Khung trạng thái cố định, nhãn theo khách:** Work Order có Type cố định Incomplete, Completed, khách thêm tên trạng thái; Purchase Order 8 trạng thái cố định, không có Add. Fleetio: `Xem`. Khớp đúng "Lõi khung trạng thái + Cấu hình nhãn" của `saas-core-vs-tenant.md`.

### P1 — should have

- P7 [Mới] [Cấu hình] **Tự động hoá Trigger, Điều kiện, Hành động** với 18 mẫu: Work Orders 6, Issues 5, Purchase Orders 3, Faults 2, Service Entries 2. Loại bản ghi trigger: Work Order, Service Entry, Fault, Issue, Purchase Order, Geofence Event, Vehicle; kiểu sự kiện Created, Updated, Created or Updated, Deleted. Hành động với Issue: Update Field, Add Comment, Send Email; Create Record tạo Work Order. Điều kiện cho Issue có 59 trường, All of, Any of, nhóm lồng, không phân biệt hoa thường. Fleetio: `Chạy` tạo 9 automation, chạy Add Comment, Update Field, Create Record trên Issue, Vehicle, Work Order, Add Comment trên Service Entry, Purchase Order (trước đây chỉ `Xem` mẫu); Fault lưu được, chưa có lượt thật vì cần thiết bị telematics. Trigger Vehicle, Purchase Order không có Deleted; Fault chỉ có Created.
- P8 [Mới] [Cấu hình] **Gợi ý tự động hoá đúng ngữ cảnh:** vừa tạo sự cố xong bật hộp gợi ý mẫu "tạo lệnh khi có sự cố". Fleetio: `Chạy`. Cách bán tính năng rất tự nhiên, nhưng dễ gây phiền nếu lặp.
- P9 [Mới] [Lõi] **Theo dõi, bình luận, nhắc tên** trên mọi bản ghi; người tạo tự thành người theo dõi; bình luận do automation ghi tác giả "Fleetio Automation". Fleetio: `Chạy` tự theo dõi, Unwatch, Watch lại, comment tay và comment do automation. Ô @ yếu với tiếng Việt, xem W17.
- P10 [Mới] [Cấu hình] **Hồ sơ thông báo** gán cho người (gán hàng loạt từ Contacts), nhóm xe theo dõi có cột Direct Watchers, Total Watchers; cài đặt cá nhân 18 nhóm sự kiện, mỗi sự kiện chọn Email, Push; hộp Inbox, Archived, lọc All Activity, Comments Only, @ Mentions. Fleetio: `Xem` 0 hồ sơ, 11 nhóm theo dõi; `Chạy` Inbox. Điểm đáng học: có 0 hồ sơ thì người theo dõi vẫn nhận in-app, khách mới không bị im lặng hoàn toàn.
- P11 [Mới] [Gói: Bảo dưỡng đội xe] **49 báo cáo trong 13 nhóm** (Vehicles 14, Vehicle Assignments 2, Inspections 4, Issues 2, Service 8, Warranties 2, Work Orders 5, Contacts 2, Parts 4, Fuel 3, Tools 1, Jobs 1, Motor Pools 1), có yêu thích, lưu, chia sẻ; 4 báo cáo gắn "Upgrading soon". Trang báo cáo có biểu đồ, Filters, Columns, Export CSV (cột đang hiện hoặc mọi cột), Print. Fleetio: `Chạy` đọc 49 tên, mở từng báo cáo đọc cột 48/49 (chỉ đọc), lọc và lưu Issues Report. Đủ tên, cột ở SRS Mục 21. Bản 02/11 ghi 48 báo cáo 12 nhóm là sai; `expense_entries` lỗi 500 nên chưa đọc được cột. Dùng làm danh mục để chọn cho `workshop-reports`.
- P12 [Mới] [Lõi] **Tìm kiếm toàn cục** theo nhiều loại bản ghi (bản trước ghi 15, lượt 3 đếm ô chọn có 16 mục, chưa tách mục "All"); kết quả theo nhóm, mỗi nhóm 3 dòng và More; tách theo từ, không đòi khớp cả cụm. Fleetio: `Chạy`.
- P13 [Mới] [Lõi] **Lịch sử bản ghi** (View Record History) và lịch sử đổi của từng trường như trạng thái; có trên xe, automation, Issue; cột Date, Changes By, Changes Made, lọc khoảng ngày. Comment, Watch không vào lịch sử. Fleetio: `Chạy`.
- P14 [Mới] [Cấu hình] **Kho tài liệu chung,** biết file gắn với bản ghi nào: cột File Name, File Size, Location, Auto-Delete, Attached To, Labels; gắn vào xe, hộp gắn còn có theo loại xe, nhóm, hợp với giấy tờ chung cả đội đầu kéo. Fleetio: `Chạy` tải 1 tệp, gắn 1 xe; gắn theo nhóm, loại chưa bấm.
- P15 [Mới] [Lõi] [Cấu hình] **Giới hạn theo gói hiển thị rõ và chặn thật:** Account Usage hiện đã dùng trên giới hạn (Fleetio: Documents 250.0 GB, Roles 30, Vehicles 5, Automations 75, Custom Records 25); hết hạn mức thì Save báo "Your plan is limited to 5 vehicles" kể cả khi đủ trường, danh sách xe hiện "5 of 5", nút Add Vehicle có khoá. Fleetio: `Chạy` bị chặn thật. Bản 02/11 đọc Roles là 50 từ ảnh mờ, đúng là 30. Automations chỉ đếm bản đang bật (`Chạy` lượt 4: 1 of 75 khi lưu 10 bản, bật 1): khách lưu nháp không tốn hạn mức, đáng học. Áp vào phần bán gói; giá trị theo hợp đồng là tham số mới, chưa có mã.
- P16 [Mới] [Lõi] **Câu hỏi dữ liệu bằng ngôn ngữ tự nhiên** (Ask a data question): mở AI Data Analyst, khung nhúng từ ThoughtSpot, có Show work, lưu My Conversations. Fleetio: `Chạy` 4 câu qua 2 lượt, không câu nào khớp trang xe (Điểm yếu W2, W14).
- P26 [Mới] [Cấu hình] **Lưu ở trạng thái tắt, bật phải xác nhận, lúc bật mới sinh phiên bản:** hộp "When you enable this automation ... actions will run when you set the trigger and conditions are met."; bật sinh v.1 và ghi Enabled At; bật không chạy bù cho bản ghi đã có; tắt rồi bật lại không sinh phiên bản mới. Fleetio: `Chạy`. Khách thử luật an toàn, không sợ luật vừa lưu đã chạy trên dữ liệu thật. Sửa khi đang bật thì không có lớp an toàn này, xem P39.
- P27 [Mới] [Cấu hình] **Nhật ký từng lượt chạy:** danh sách có Total Runs, Successful Runs, Failed Runs, Last Run At, Current Version; mỗi lượt có Run Result ghi phiên bản, bản ghi kích hoạt, Triggered By, log JSON; lượt không khớp điều kiện không được đếm. Lượt lỗi có băng đỏ nguyên văn lỗi nghiệp vụ, log từng bước có caused_by, thrown_by. Fleetio: `Chạy` cả SUCCESS và FAILURE. Đội hỗ trợ tra được vì sao bản ghi tự đổi hoặc không đổi.
- P28 [Mới] [Cấu hình] **Lưu trữ thay cho xoá:** Archive tắt ngay không cần tắt trước, bản lưu trữ chỉ đọc, Restore về trạng thái tắt, không tự bật lại. Fleetio: `Chạy`.
- P29 [Mới] [Cấu hình] **Hành động tạo lệnh bị giới hạn trạng thái chưa xong:** Create Record chỉ cho Open, Pending, không có Completed; Work Order sinh ra nối ngược về sự cố ở cột Resolved Issues. Fleetio: `Chạy` Issue #44 sinh WO #105. Tránh lối tắt bỏ qua kiểm số km khi hoàn tất. Update Field thì có Completed, nhưng vẫn qua kiểm tra như form tay: WO thiếu Start Date làm lượt thất bại, bản ghi giữ nguyên (`Chạy`). Automation không lách được ràng buộc nghiệp vụ.
- P30 [Mới] [Cấu hình] **Mẫu "lệnh xong và xe không còn lệnh mở thì xe về Active":** điều kiện đếm Vehicle Incomplete Work Orders Count nhỏ hơn 1. Fleetio: `Chạy` đọc định nghĩa mẫu, chưa bật mẫu này. Với đầu kéo có nhiều lệnh sửa song song, điều kiện đếm này rất đáng lấy.
- P37 [Mới] [Gói: Bảo dưỡng đội xe] **Khối cột đối tượng gắn sẵn trong báo cáo:** 22 báo cáo kèm khoảng 110 cột thông tin xe chọn trong Columns, nên người dùng tự ghép bảng rộng thay vì cần nhiều báo cáo riêng. Fleetio: `Chạy` chỉ đọc. Hợp với `workshop-reports` khi báo cáo cần thêm hãng, đời, nhóm xe.
- P38 [Mới] [Gói: Bảo dưỡng đội xe] **Báo cáo đã lưu:** lưu bộ lọc và cột của báo cáo chuẩn, mặc định Private, có lịch gửi email, yêu thích, mở lại giữ bộ lọc, bộ lọc nằm trên đường dẫn nên gửi được cho đồng nghiệp có quyền (`Suy`). Fleetio: `Chạy` Private; Public, Email Schedule không chạy.
- P39 [Mới] [Cấu hình] **Báo rõ đang sửa luật đang chạy:** băng "You have unsaved changes on this enabled automation", menu Save Automation, Discard Unsaved Changes; lưu lên phiên bản mới, lượt sau ghi đúng phiên bản. Fleetio: `Chạy`. Đề xuất Invlogis thêm xác nhận trước khi lưu.
- P40 [Mới] [Cấu hình] **Điều kiện tự động hoá theo dữ liệu xe:** 71 trường, có cảm biến Fuel Level, Engine Oil Pressure, Engine Coolant Temp, Battery Voltage, Tire Pressure, Ignition Status, Installed Tires Count, Axle Configuration, Incomplete Work Orders Count. Fleetio: `Xem` trường, `Chạy` điều kiện theo xe. Đủ để dựng luật theo dữ liệu GPS của đầu kéo (`Suy`).
- P41 [Mới] [Lõi] **Lịch sử trạng thái ghi rõ nguồn và thời lượng:** Status Updates ghi "Fleetio Automation" hay tên người, kèm thời gian ở mỗi trạng thái. Fleetio: `Chạy`. Tốt hơn "Triggered By" (W3), đủ để tính thời gian xe nằm xưởng.
- P42 [Mới] [Lõi] **Chế độ xem chia sẻ theo phạm vi:** Shared with Private, Admins Only, Specific Roles, Specific Users, Everyone; bản chuẩn có khoá, muốn đổi phải lưu bản mới. Fleetio: `Chạy` Private, các mức khác chỉ đọc. Áp vào `common-workspace`.
- P44 [Mới] [Lõi] [Cấu hình] **Hãng buộc điều kiện với hành động nhạy:** tự động đổi đơn mua sang Approved bắt buộc có điều kiện Status là Pending Approval, cảnh báo ngay trong panel, lưu thì chặn. Tự động chỉ xử lý đơn đã nộp duyệt, không bỏ qua bước nộp được. Fleetio: `Chạy` phần chặn; nhánh duyệt thật cần người thứ hai. Đáng lấy cho mọi luật tự duyệt.
- P43 [Mới] [Cấu hình] **Nói rõ loại thông báo không tắt được:** tắt email chung vẫn không tắt essential communications, Saved Reports, Inspection Workflows, Automation Alerts, Notification Profiles. Fleetio: `Xem`.
- P31 [Mới] [Lõi] [Cấu hình] **Chính sách mật khẩu theo khách:** độ dài tối thiểu, hạn đổi, yêu cầu ký tự, số lần sai, thời gian khoá, đặt lại mọi mật khẩu; không áp cho đăng nhập SAML. Fleetio: `Xem` (lựa chọn đọc được: độ dài 8, 15, 30, 50; hạn None, 30, 60, 90 ngày; sai 5 hoặc 10 lần; khoá 5, 10, 30 phút; Session Timeout tách app và web, chỉ app có Never). Hết phiên tách theo thiết bị là ý đáng học cho app lái xe. Đối chiếu `account-access`.
- P32 [Mới] [Lõi] **Cảnh báo chi phí ngay tại quyền:** quyền Create của Vehicles có câu "Adding new Vehicles will result in additional charges to your account's subscription." Fleetio: `Xem`. Lấy nếu tính tiền theo xe.

### P2 — nice to have

- P17 [Mới] [Gói: Khách lớn, chưa có trong danh sách gói] **Bản ghi tự tạo:** loại bản ghi, trường, liên kết, bố cục kéo thả, trang danh sách, trang chi tiết. Fleetio: `Docs` (Early Access, gói Premium); không mở theo lựa chọn của user.
- P18 [Mới] [Cấu hình] **Trường tuỳ chỉnh:** nhãn duy nhất theo loại bản ghi, không đổi được kiểu dữ liệu sau khi lưu; chỉ trường chọn và tick dùng được cho Record Set. Fleetio: `Docs`, `Xem` Standard Records liệt kê 15 loại bản ghi, đều 0 trường.
- P19 [Mới] [Gói: Khách lớn, chưa có trong danh sách gói] **API key, Webhook, SAML, kết nối ngoài** (Integration Links kèm biến; External Connections FTP, SFTP, Amazon S3 cho báo cáo định kỳ; Account Tokens có Rate Limit, Fleetio: 250 requests/minute; khoá thu hồi không kích hoạt lại). Danh mục tích hợp đếm Telematics 43, Fuel Cards 9, Data Connectors 6, Fuel Management 5, Tolls & Citations 2, còn lại mỗi nhóm 1. Fleetio: `Xem` trang rỗng, không tạo. Áp vào `account-access`.
- P20 [Mới] [Gói: Khách lớn, chưa có trong danh sách gói] **Máy chủ MCP** để nối trợ lý AI: "Each connection respects the user's role permissions."; module Fleetio MCP mức không có ở cả 4 vai mặc định. Fleetio: `Xem`, tắt mặc định, không bật.
- P21 [Mới] [Gói: Khách lớn, chưa có trong danh sách gói] **Sandbox và xuất toàn bộ dữ liệu:** Sample Copy, Production Copy có hạn mức riêng (tài khoản: 0/2 và 0/0); Export Account Data 13 loại dữ liệu, CSV hoặc XLS, gửi qua email, link hết hạn (Fleetio: 7 ngày). Fleetio: `Xem`, không bấm.
- P22 [Mới] [Cấu hình] **Widget tuỳ chỉnh cho trang đầu.** Fleetio: `Xem` trang rỗng.
- P33 [Mới] [Gói: Bảo dưỡng đội xe] **Thu hồi của hãng (Recall):** nhập tự động theo năm, hãng, đời xe từ nguồn công khai của Mỹ; tab All, Needs Action, Open, Resolved, Acknowledged; một mẫu tự động hoá nâng sự cố lên Critical khi nguồn là Recall. Fleetio: `Xem` tab Needs Action 261 dòng Sample lúc chụp ảnh, 285 ở lần đọc sau của nhóm Sửa chữa (OQ-21). Ở Việt Nam chưa thấy nguồn tương đương (`Suy`).
- P34 [Mới] [Gói: Khách lớn, chưa có trong danh sách gói] **Đặt xe dùng chung (Motor Pool):** danh sách đặt xe, bảng giá đặt xe, phí cố định, quyền nhận xe, trả xe, huỷ. Form đặt xe có Operator *, Motor Pool *, Reason for Trip, Pick Up *, Drop Off *. Fleetio: `Xem` danh sách rỗng, form mở được, không chạy vì cần tạo Motor Pool trong Settings.
- P35 [Mới] [Cấu hình] **Trợ lý AI cho bảo dưỡng:** Issue Prioritization, Issue Resolution, Fault Monitoring, Service Assessments, Service Writer, mỗi cái bật riêng, có câu điều khoản. Sự cố mới có mức ưu tiên "Auto-assign" và tự thành High dù không nhập (Issue #40, #42). Fleetio: `Chạy` phần thấy được; nguyên nhân là AI Issue Prioritization là `Suy`. Có lần AI thất bại im lặng (W15). Đối chiếu NFR-006 của SRS.
- P36 [Mới] [Lõi] **Chia sẻ báo cáo bằng link có hạn, có danh sách thu hồi:** Reports › Shared liệt kê link, Unshare có hộp xác nhận, thu hồi xong mở lại không còn dữ liệu. Fleetio: `Chạy`. Chỉ học hạn và danh sách thu hồi, KHÔNG học cách sinh link (Điểm yếu W1).

### Điểm yếu cần làm khác

- W1 [Mới] [Lõi] **Chia sẻ ra ngoài phải là hành động chủ động.** Fleetio: `Chạy` bấm Share là sinh NGAY link công khai, không hỏi, "this link allows anyone with access to view all data"; lối "click here to unshare" trong hộp không có tác dụng, bấm lại trả 404, link vẫn sống; chỉ Reports › Shared › Unshare mới thu hồi được. Đề xuất Invlogis: mở hộp không sinh link, có bước bấm tạo, nói rõ phạm vi dữ liệu, thu hồi có hiệu lực ở mọi lối, ghi nhật ký tạo, mở, thu hồi.
- W2 [Mới] [Lõi] **Số do AI trả phải ghi dữ liệu đến thời điểm nào.** Fleetio: `Chạy` hỏi số sự cố mở của TEST-XE-01, AI trả "currently has 2 open issues" khi trang xe có 7; hỏi km mới nhất, AI trả 1.700 khi thật là 2.999 km; không cảnh báo, không ghi độ trễ. Lượt 3 trả 10 khi thật là 12, hỏi trực tiếp ngày dữ liệu thì trả lời bộ dữ liệu không có trường này. Khả năng kho phân tích trễ là `Suy`. Đề xuất Invlogis: mọi số AI trả kèm "dữ liệu đến thời điểm" và lối mở bản ghi gốc.
- W3 [Mới] [Cấu hình] **Lượt do máy gây ra phải ghi máy là nguồn, và ghi giống nhau mọi nơi.** Fleetio: `Chạy` lượt Update do automation tự gây ra vẫn ghi "Triggered By" là người tạo sự cố, trong khi Status Updates của xe và tác giả comment lại ghi đúng "Fleetio Automation". Đề xuất Invlogis ghi rõ automation nào, phiên bản nào.
- W4 [Mới] [Cấu hình] **Kết quả lượt chạy phải phản ánh đúng việc đã làm.** Fleetio: `Chạy` "Records: No records changed" hiện ở lượt thêm comment, lượt đã đổi Status xe và lượt thất bại; chỉ ở lượt thất bại câu này mới đúng sự thật. Lượt đổi xe là theo ghi chép, không có ảnh Run Result.
- W5 [Mới] [Lõi] [Cấu hình] **Có trần lượt chạy theo khách.** Fleetio: `Chạy` automation trên Issue tự kích hoạt lại chính nó 2 lượt rồi dừng vì giá trị không đổi, trên Vehicle thì không sinh lượt mới; tài liệu hãng không nêu chống vòng lặp, giới hạn lượt; vòng lặp chéo hai automation không chạy vì không rõ giới hạn trên hệ thống thật. Đề xuất Invlogis: trần lượt chạy theo khách, tham số mới, chưa có mã.
- W6 [Mới] [Lõi] **Chặn hoặc cảnh báo trùng người.** Fleetio: `Chạy` tạo lại liên hệ cùng tên, không email, lưu được, không cảnh báo.
- W7 [Mới] [Lõi] **Bộ đếm khởi tạo phải nhất quán.** Fleetio: `Chạy` "Get Started" hiện 3/5 ở trang này, 3/6 ở trang khác.
- W8 [Mới] [Lõi] **Thông báo nền không che nội dung.** Fleetio: `Chạy` toast "Calculating Service Reminders Compliance" lặp nhiều lượt và che màn.
- W9 [Mới] [Cấu hình] **Lỗi tự động hoá phải báo tới người liên quan.** Fleetio: `Chạy` lượt lỗi không thấy trên trang bản ghi, chuông không có dòng nào, không thử lại trong khoảng 5 phút, không tự tắt, không có màn gom lỗi ngoài cột Failed Runs. Đề xuất Invlogis: báo trong app không cần cấu hình thêm.
- W10 [Mới] [Cấu hình] **Luật không được lật thao tác tay trong im lặng.** Fleetio: `Chạy` người đổi Status về Active, 1 giây sau automation đổi lại Inactive, màn người dùng không báo gì. Đề xuất Invlogis: báo ngay, nêu tên luật.
- W11 [Mới] [Cấu hình] **Trigger phải lọc được theo trường đổi.** Fleetio: `Chạy` sửa Color cũng kích hoạt luật đổi Status, dễ chạy thừa. Đề xuất Invlogis: "chỉ khi Status đổi".
- W12 [Mới] [Cấu hình] **Lịch sử phiên bản phải đúng nội dung từng bản.** Fleetio: `Chạy` mở v.1 hiện chữ của v.2, thấy 1 lần trên sửa nội dung action (OQ-16); lưu bản sửa khi đang bật không hỏi xác nhận.
- W13 [Mới] [Lõi] **Mặc định quyền thấp nhất khi mở người dùng.** Fleetio: `Xem` form Enable Access mặc định Role Fleet Manager, Record Sets đều Full Access. Đề xuất Invlogis đảo mặc định.
- W14 [Mới] [Lõi] **AI không được nói bản ghi "không tồn tại" khi chỉ là chưa có trong kho.** Fleetio: `Chạy` "Vehicle TEST-DAUKEO-2 does not exist" khi xe có từ cùng ngày, có 2 sự cố. Đề xuất Invlogis: nói rõ "chưa có dữ liệu đến thời điểm...".
- W15 [Mới] [Lõi] **AI chạy nền thất bại phải lộ ra.** Fleetio: `Chạy` AI Issue Prioritization từ pending sang failed, chỉ có một dòng Record History, ghi Changes By là người tạo; Issue về "No Priority".
- W16 [Mới] [Cấu hình] **Chữ trong mẫu phải lấy từ biến.** Fleetio: `Chạy` mở mẫu đổi ngưỡng theo tiền tệ khách (100.000 ₫) nhưng câu email viết cứng ">$1,000.00".
- W17 [Mới] [Lõi] **Nhắc tên, tìm tên phải chịu tiếng Việt.** Fleetio: `Chạy` gõ @ không dấu hoặc có gạch nối không ra người, đăng thành chữ thường không báo. Với khách Việt Nam đây là lỗi hằng ngày.
- W18 [Mới] [Lõi] **Một sản phẩm, một kiểu giao diện báo cáo.** Fleetio: `Chạy` chỉ đọc 34 báo cáo thế hệ mới, 15 thế hệ cũ; bản cũ không thấy Share, Export CSV, người dùng không đoán được báo cáo nào xuất được.
- W21 [Mới] [Cấu hình] **Báo lỗi cấu hình luật ngay lúc chọn, nói được lý do.** Fleetio: `Chạy` Update Field Repair Priority Class = Emergency trên Service Entry cho chọn và Apply, tới Save mới báo "action is missing", "is invalid", không nêu vì sao; chỉ thử 1 giá trị. Cùng màn với cảnh báo tốt ở P44 nên không nhất quán.
- W22 [Mới] [Cấu hình] **Hành động phục hồi cũng cần rõ hệ quả.** Fleetio: `Chạy` Restore một cú bấm, không hộp xác nhận, về Disabled dù trước đó Enabled; chỉ nói "Record successfully restored!", người dùng dễ tưởng luật đã chạy lại.
- W23 [Mới] [Lõi] **Một kiểu bộ lọc cho mọi báo cáo.** Fleetio: `Chạy` đọc 3 kiểu: panel ô cố định, filter builder, thanh lọc trên báo cáo; người dùng phải học lại từng báo cáo; tên ô lúc Vehicle lúc Asset, một ô sai chính tả "Subotal amount"; một báo cáo không lọc được.
- W24 [Mới] [Gói: Bảo dưỡng đội xe] **Số tổng không được gộp bản nháp mà không nói.** Fleetio: `Chạy` báo cáo đơn mua cộng cả Draft vào Total Amount; biểu đồ trục chỉ 20k khi tổng 3,5 triệu ở VND, tức thang biểu đồ lệch với tiền tệ lớn. Đề xuất Invlogis: mặc định loại nháp, nói rõ phạm vi cộng.
- W19 [Mới] [Cấu hình] **Danh sách phải cập nhật sau khi tải.** Fleetio: `Chạy` vừa báo "Document was successfully added." danh sách vẫn "No results to show"; tệp .txt mở khung xem PDF 0 trang.
- W20 [Mới] [Lõi] **Lỗi trang phải có lối phục hồi rõ.** Fleetio: `Chạy` `expense_entries` Error 500 cả 3 lần, qua 2 lượt, nên khó còn là sự cố thoáng qua (`Suy`), trang lỗi có Go back, contact us, status page; có thể sự cố tạm của hãng. Điểm đáng học là trang lỗi nói trạng thái dịch vụ "Partially Degraded Service".

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
Mẫu, Make a Copy hoặc trống ─> Trigger + Điều kiện + Hành động ─> Lưu (tắt)
   ─> Bật (xác nhận, sinh v.1) ─> Sự kiện khớp ─> Hành động ─┬─> Lượt SUCCESS
                                │                            └─> Lượt FAILURE, bản ghi giữ nguyên, không báo
                                └─ Không khớp ─> Không ghi lượt
   ─> Sửa khi đang bật (băng cảnh báo) ─> Lưu lên v.2, hiệu lực ngay | Discard
   ─> Tắt (xác nhận) | Archive (tắt ngay, chỉ đọc) ─> Restore (về tắt)
```

Kết quả thật: Issue #40 tạo lúc automation tắt không có comment, bật lên cũng không chạy bù; Issue #42 tạo lúc bật có comment trong khoảng 6 giây; Issue #43 khớp hai automation thì cả hai chạy; Issue #44 sinh Work Order #105 trạng thái Open. Lượt 3: Work Order #111 thiếu Start Date làm lượt FAILURE, WO vẫn Open; sửa AUTO-01 khi đang bật lên v.2, Issue #55 chạy theo v.2; AUTO-05 đổi xe sang Inactive, người đổi về Active bị đổi lại sau 1 giây. Ví dụ mẫu có sẵn: tự duyệt đơn mua dưới ngưỡng (Fleetio: 10.000 ₫), đổi xe sang In Shop khi sự cố đến từ kiểm tra hỏng, email khi lịch sử dịch vụ vượt số tiền (Fleetio: 100.000 ₫), tạo lệnh theo dõi sau khi thay lốp, bỏ qua mã lỗi phiền, nâng sự cố lên Critical khi có áp suất dầu thấp. Bảng đủ 18 mẫu ở SRS Mục 17.

### 5.4 Chia sẻ báo cáo

`Chạy`, link đã thu hồi.

```
Mở báo cáo ─> Share ─> Link công khai có ngay (hết hạn 7 ngày)
   ─> "click here to unshare" ─> không tác dụng, link vẫn sống
   ─> Reports › Shared › Unshare ─> xác nhận ─> link chết
```

### 5.5 Hỏi dữ liệu bằng lời

`Chạy` 4 câu qua 2 lượt.

```
Ask a data question ─> AI Data Analyst ─> gõ câu hỏi ─> bảng + câu trả lời (40 đến 90 giây)
   ─> Show work xem cách tính ─> đối chiếu tay mới biết số sai
   ─> Xe mới tạo ─> "does not exist", hỏi lại có gõ đúng tên không
```

### 5.6 Lưu báo cáo, lưu chế độ xem

`Chạy` Private.

```
Báo cáo ─> Filters ─> Save (mặc định Private) ─> Reports › Saved ─> sao ─> Favorites
Danh sách ─> đổi cột, nhóm ─> Save Changes ─> bản chuẩn có khoá ─> Save as New View ─> Shared with ─> tab mới
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
| D7 | 5.3 | Hành động qua kiểm tra nghiệp vụ | Lượt SUCCESS | Lượt FAILURE, bản ghi giữ nguyên, không báo trong app |
| D8 | 5.3 | Đang sửa bản đang bật | Save: lên phiên bản mới, hiệu lực ngay | Discard: giữ bản hiện tại |
| D9 | 5.3 | Automation đang bật và người sửa ngược giá trị | Automation đổi lại sau 1 giây, không báo | Giữ giá trị người sửa |
| D10 | 5.6 | Đang ở view chuẩn | Chỉ Save as New View | Save Changes vào view đó |

### 6.3 State Transitions

Automation (`Chạy`):

| Từ | Hành động | Sang | Ghi chú |
|---|---|---|---|
| Chưa lưu | Save Automation | Disabled | Save mờ cho tới khi có trigger, hành động; rời trang không để lại bản rác |
| Disabled | Bật, xác nhận | Enabled | Lần đầu sinh v.1, ghi Enabled At; bật lại giữ phiên bản |
| Enabled | Tắt, xác nhận | Disabled | "it will stop working and prevent any actions from running." |
| Enabled | Sửa, Save Automation | Enabled | Lên v.2, không hỏi lại, hiệu lực ngay |
| Enabled hoặc Disabled | Archive | Archived | Tắt ngay, ghi Disabled At |
| Archived | Restore | Disabled | Không tự bật lại; "Record successfully restored" |
| Archived | Delete | — | Có nút, không bấm |

Xe có 5 trạng thái danh mục Active (Default), In Shop, Inactive, Out of Service, Sold, đổi tự do không có luật chuyển (`Xem`); lượt 3 đổi thật Active, Inactive bằng automation và bằng tay (`Chạy`). Đủ sơ đồ và ma trận ở [[docs/_research/fleetio/srs/fleetio-saas-platform-states.md|States]].

### 6.5 Other Edge Cases

- **Banner múi giờ:** đầu trang cảnh báo khi múi giờ thiết bị khác cài đặt (`Xem`), đề xuất giữ cho khách nhiều chi nhánh, nhưng cần nút tắt hẳn.
- **Luật chỉ áp về sau:** nhiều luật ghi "only applies to future" (`Xem`). Invlogis nên nói rõ tương tự để tránh tưởng dữ liệu cũ sai.
- **Tự động hoá không chạy bù:** bật luật sau khi bản ghi đã có thì bản ghi cũ không được xử lý (`Chạy`). Invlogis cần nói rõ trong hộp bật, hoặc có nút chạy cho dữ liệu cũ.
- **Toast nổi trùng lặp:** thông báo nền lặp nhiều lượt và che nội dung (`Chạy`). Không nên học.
- **Nút đi nơi khác:** "Manage Users" trỏ sang danh sách người dùng ngoài Settings, "Integrations Directory" mở trang ngoài (`Xem`).
- **Thanh lý xe chỉ là trường dữ liệu:** Out-of-Service là ngày và số km, không có nút thanh lý (`Xem`).
- **Đơn vị lẫn trên form xe:** Odometer trong Financial hiện "mi" khi Specifications hiện cm, kg, lít (`Xem`, chưa rõ lý do).
- **Trial bật ngoài ý muốn:** cuối lượt chạy, add-on Tools đổi sang "Trialing", "14 days left in trial" mà nhóm này không bấm (`Xem`). Invlogis cần nhật ký thay đổi gói.
- **Hai automation cùng khớp:** ra 2 comment giống hệt nếu không tick Prevent duplicate comments (`Chạy`). Invlogis nên mặc định chống trùng.
- **Trường thứ 2 trong nhóm điều kiện:** toán tử mặc định "does not contain", Enter đóng panel như Apply (`Chạy`); dễ đặt sai luật. Invlogis nên giữ cùng toán tử với dòng trước.
- **Trường điều kiện thiếu:** Work Order không có Description, Vehicle không có Name; phải khoanh vùng bằng Invoice Number, "Vehicle is any of" (`Chạy`).
- **Tên nhà cung cấp lộ ra:** hộp tải tài liệu hiện Filestack và các nguồn Facebook, Instagram, GitHub (`Chạy`). Nên tắt nguồn không hợp với giấy tờ công ty.
- **Bộ lọc tên sai nghĩa:** ô "Issue Summary" tìm cả mô tả (`Chạy`).

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
| Automation đổi Work Order sang Completed | Qua kiểm tra như form tay, Start Date bắt buộc | "Automation Action failed: Start Date can't be blank" | `Chạy` |
| New Saved Report | Name bắt buộc | Chưa thử để trống | `Xem` |
| Automation Service Entry, Update Field Repair Priority Class = Emergency | Từ chối lúc lưu | "Automation could not be created. Please resolve any errors try again." | `Chạy` |
| Automation đổi đơn mua sang Approved | Phải có điều kiện Status Pending Approval | "Purchase Order Status "Pending Approval" is required" | `Chạy` |

### 7.2 Limits & Quotas (exact values)

| Tham số | Giá trị | Window | Behavior khi vượt |
|---|---|---|---|
| Xe | Fleetio: 5, gói đang dùng; Sample không tính | Theo gói | Chặn lưu, "Your plan is limited to 5 vehicles", nút Add Vehicle khoá (`Chạy`) |
| Vai trò | Fleetio: 30, đang dùng 4 | Theo gói | Chưa thử |
| Tự động hoá | Fleetio: 75, chỉ đếm bản đang bật (`Chạy` đọc 1 khi lưu 10 bản, bật 1) | Theo gói | Chưa thử, cần 75 bản bật |
| API Account Tokens | Fleetio: 250 requests/minute | Mỗi phút | Chưa thử (`Xem`) |
| Thời gian hết phiên | Fleetio: Go có Never, Web từ 15 phút đến 2 tuần | Theo khách | Chưa thử (`Xem`) |
| Bản ghi tự tạo | Fleetio: 25 | Theo gói | Chưa thử |
| Tài liệu | Fleetio: 250.0 GB | Theo gói | Chưa thử |
| Sandbox | Fleetio: Sample Copy 2, Production Copy 0 | Theo gói | Chưa thử |
| Link chia sẻ báo cáo | Fleetio: 7 ngày | Mỗi link | Chưa chờ hết hạn |
| Link xuất toàn bộ dữ liệu | Fleetio: 7 ngày | Mỗi lần xuất | Chưa thử |
| Lượt tự kích hoạt | Issue thấy dừng sau 2 lượt khi giá trị không đổi; Vehicle không sinh lượt mới; trần không công bố | Mỗi sự kiện | Chưa biết |

### 7.3 Wording samples (exact strings)

#### Error messages

| Tình huống | Wording |
|---|---|
| Hết hạn mức xe | "Your plan is limited to 5 vehicles" |
| Không có quyền | "You are not authorized to perform this action." |
| Sửa bản đã lưu trữ | "Archived records are read-only and cannot be updated." |
| Lượt automation lỗi | "Automation Action failed: Start Date can't be blank" |
| Báo cáo lỗi máy chủ | "We're sorry, but something went wrong." |
| AI nói xe không có | "Vehicle TEST-DAUKEO-2 does not exist in the issues dataset with that exact name" |
| Lịch sử AI xếp mức | "Issue Priority Status changed from pending to failed" |

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
| Sửa automation đang bật | "You have unsaved changes on this enabled automation" · "Save to update, or discard to keep the current settings." |
| Báo cáo Private | "Private Saved Reports are visible only to you, but can be emailed to anyone with access to the source report." |
| Trạng thái do automation | "Fleetio Automation updated status from Active to Inactive" |
| View chuẩn | "Save as a new view to keep your changes" |
| Chat cũ | "This data may have changed since the last time you had a chat." |
| Mở truy cập | "An email invitation with instructions to create a password will be sent immediately." |

## 8. Assumptions

- Invlogis đi theo hướng khách tự cấu hình trong `tenant-parameters.md`, không làm riêng.
- `GĐ` Giai đoạn đầu chỉ cần luật có tham số, chưa cần công cụ tự động hoá tổng quát. Lượt chạy củng cố: mẫu đủ dùng với luật đơn giản, nhưng không thấy chống vòng lặp, luật lật thao tác tay không báo, lỗi im lặng nếu không bật email, nên công cụ tổng quát có rủi ro.
- `GĐ` Mô hình Role và Record Set dùng được cho cấp Chi nhánh qua nhóm nhiều cấp; cấp Công ty, Cơ sở và quyền theo ca cần thêm một lớp phạm vi.

## 9. Risks

| Rủi ro | Mức | Giảm thiểu |
|---|---|---|
| Quá nhiều tuỳ chọn làm admin khách rối | Trung | Giá trị mặc định tốt, mô tả rõ tác động |
| Tự động hoá gây chuỗi thay đổi khó truy | Cao | Nhật ký lượt chạy ghi đúng nguồn, trần lượt chạy, lưu ở trạng thái tắt |
| Chia sẻ báo cáo làm lộ dữ liệu ra ngoài | Cao | Tạo link chủ động, thu hồi ở mọi lối, nhật ký |
| AI trả số sai mà người dùng tin | Cao | Ghi thời điểm dữ liệu, lối đối chiếu bản ghi gốc |
| Luật tự động và người dùng giằng nhau, không ai biết | Cao | Báo ngay khi luật ghi đè, nêu tên luật, trigger lọc theo trường |
| Mở người dùng mới với quyền cao nhất mặc định | Cao | Mặc định quyền thấp nhất |
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
| OQ-5 | Hai automation lật giá trị của nhau có bị chặn không, trần bao nhiêu lượt? | Còn mở. Lượt 3 không chạy vì có thể lặp không biết giới hạn trên hệ thống thật; lượt do AUTO-05 đổi xe không sinh lượt mới (`Chạy`) | Câu hỏi nội bộ |
| OQ-6 | Lượt automation thất bại trông thế nào, có thử lại không? | Đã trả lời phần lớn (`Chạy`): câu lỗi nghiệp vụ nguyên văn, log từng bước, không thử lại trong khoảng 5 phút, không tự tắt, không báo trong app. Còn mở: nội dung Failure Notification Email | Câu hỏi nội bộ |
| OQ-7 | Sửa automation đang bật có sinh v.2 không; Make a Copy, Delete, trigger Vehicle, Send Email chạy ra sao? | Đã trả lời một phần (`Chạy`): sửa khi bật lên v.2, chạy theo v.2; Make a Copy mở bản chưa lưu; trigger Vehicle, Update Vehicle Status chạy. Còn mở: Delete, Run Summary Email, Send Email | Câu hỏi nội bộ |
| OQ-8 | Role và Record Set có chặn đúng như khai không? | Chưa kiểm; cần người dùng thứ hai, không mời người | Câu hỏi nội bộ |
| OQ-9 | Technician có quyền gì với Fuel Entries? | Đã trả lời (`Xem`): chọn None, không có ô con; ghi chú cũ "chỉ có ô xem" sai | Câu hỏi nội bộ |
| OQ-10 | Settings có bao nhiêu trang? | Đã trả lời (`Xem`): menu 67 link = 59 trang cấp tài khoản + 7 trang cá nhân + Log Out | Câu hỏi nội bộ |
| OQ-11 | Cột và lọc của 48 báo cáo chưa mở, Saved Reports là gì? | Đã trả lời một phần (`Chạy`): đủ 49 tên, cột 48 báo cáo ở SRS Mục 21; Saved Reports là bộ lọc và cột lưu lại kèm Private hoặc Public, lịch email. Lượt 4: nhãn bộ lọc 48 báo cáo, 3 kiểu, ở SRS Mục 21.3. Còn mở: `expense_entries` lỗi 500 lần 3 | Câu hỏi nội bộ |
| OQ-12 | Đổi trạng thái xe thật, lưu trữ xe, xe trùng tên, đặt xe dùng chung chạy thế nào? | Một phần (`Chạy`): đổi Status thật Active, Inactive. Còn mở: lưu trữ xe, xe trùng tên vì hạn mức xe đã đầy; đặt xe cần tạo Motor Pool trong Settings | Câu hỏi nội bộ |
| OQ-13 | AI Data Analyst sai vì kho phân tích trễ hay vì cách đếm? | `Suy` nghiêng về kho trễ: 2/7 rồi 10/12 sau khoảng 15 giờ, xe mới "does not exist". Chưa giải thích được #49, #51 | Câu hỏi nội bộ |
| OQ-14 | Mẫu Send Email When A Work Order Total Exceeds Amount có trigger, điều kiện gì? | Đã trả lời (`Chạy` mở mẫu): Work Order Created or Updated, Total Cost ≥ 100.000 ₫, câu email viết cứng ">$1,000.00" | Câu hỏi nội bộ |
| OQ-16 | Version History hiện nội dung v.2 khi mở v.1 là lỗi chung không? | Thấy 1 lần, chưa thử sửa điều kiện | Câu hỏi nội bộ |
| OQ-17 | Vì sao automation đổi Issue sinh thêm lượt còn đổi Vehicle thì không? | `Chạy` thấy khác biệt, chưa biết cơ chế | Câu hỏi nội bộ |
| OQ-18 | Record peek, thao tác hàng loạt chạy ở màn nào? | Issues không thấy peek; ô chọn nhiều chưa bấm | Câu hỏi nội bộ |
| OQ-19 | Hạn mức Automations có đúng chỉ đếm bản đang bật không? | Đã trả lời (`Chạy`): đúng, 1 of 75 khi lưu 10 bản, bật 1 | Câu hỏi nội bộ |
| OQ-21 | Vì sao tab Needs Action của Recall từ 261 lên 285 dòng? | Cùng tab, khác thời điểm; có thể do nhập tự động (`Suy`) | Câu hỏi nội bộ |
| OQ-20 | AI Issue Prioritization thất bại vì sao, có thử lại không? | Chưa biết điều kiện | Câu hỏi nội bộ |

Danh sách câu hỏi mở đầy đủ, kể cả OQ-15 về đơn vị trên form xe, ở SRS Mục 12.

## 12. Next Steps

- Đưa P1, P2, P3, P6, P23, P24, P25 vào phần chốt OQ-7 của PRD khi review.
- Đưa W1, W2, W3, W5, W9, W10, W13, W14, W17 vào yêu cầu phi chức năng chung của Invlogis (chia sẻ ra ngoài, AI, nhật ký, trần và báo lỗi tự động hoá, quyền mặc định, tìm tiếng Việt) khi review.
- Chọn báo cáo cho `workshop-reports` từ SRS Mục 21.
- Đối chiếu P5 với mẫu danh sách trong design system.
