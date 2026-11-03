---
type: research
keyword: "Fleetio: nhắc bảo dưỡng, bộ lịch, gia hạn giấy tờ, kiểm tra xe"
status: draft
status_changed: 2026-11-03
status_reason: "đã review upstream, không cần sửa"
updated: 2026-11-03
links:
  - docs/_product/prd.md
  - docs/_research/fleetio/fleetio-repair.md
  - docs/_research/2026-11-02-fleetio-app-teardown.md
  - docs/_research/fleetio/run-notes/reminders-inspection.md
  - docs/_research/fleetio/run-notes/tires.md
  - docs/_research/fleetio/run-notes/location-dispatch.md
---

# Giải pháp tham khảo: Nhắc bảo dưỡng và kiểm tra xe

> Khuyến nghị: **Nên tham khảo mạnh** cho `reminders`. **Kiểm tra xe chưa có feature ở Invlogis**, có thể là tính năng mới đáng cân nhắc, cần hỏi Delta. Tài liệu mô tả Fleetio đang làm gì; đề xuất cho Invlogis tách riêng, chưa phải yêu cầu đã chốt.

## 1. Idea Seed

Xe được nhắc bảo dưỡng theo thời gian hoặc số km, trục nào đến trước thì tính trục đó. Số km đến từ mọi nguồn nên trạng thái nhắc tự đổi ngay khi lưu. Hoàn thành qua lệnh hoặc phiếu dịch vụ thì kỳ sau tính từ lần làm thật. Giấy tờ là loại nhắc riêng, gia hạn bằng cách sửa tay ngày. Lái xe làm phiếu kiểm tra trên biểu mẫu tự dựng; mục Không đạt tự thành sự cố, lỗi lặp gộp vào sự cố đang mở; phiếu tự gắn chuyến đang chạy và vị trí nộp.

## 2. Context

**Feature Invlogis liên quan:** `reminders` (#18), chưa chi tiết hoá, thuộc Gói Bảo dưỡng đội xe. Kiểm tra xe: tìm "kiểm tra xe", "checklist" trong brainstorm Phương tiện và Lệnh vận tải không ra kết quả; chưa chắc tài liệu khách không có.

**Nguồn và bằng chứng:** chạy thật hai đợt trên tài khoản dùng thử. Đợt 02/11/2026: nhắc "Brake Pads Replacement" trên `TEST-XE-01`; biểu mẫu `TEST - Pre-trip inspection`, `TEST - Quick check`; phiếu #125988723. Đợt 03/11/2026: 8 đầu việc `TEST-NHAC-A..H`, bộ lịch `TEST-NHAC-BO-LICH`, gia hạn xe và liên hệ, biểu mẫu `TEST-NHAC-PHIEU`, lệnh #101, các phiếu dịch vụ, phiếu kiểm và sự cố #47 đến #50, cộng phiếu kiểm lốp (`TEST-LOP kiem lop`) và phiếu có vị trí giả lập. Lượt 3 (03/11/2026): biểu mẫu `TEST-NHAC-R3` #680174, phiếu #126108655, sự cố #51 và mở lại #49, bộ lịch #591701, #591702, gia hạn liên hệ #1596560, bản nháp lệnh đã Discard; thêm một phiếu trên Fleetio Go #126102722 để kiểm vị trí từng mục. Chi tiết ở [[docs/_research/fleetio/run-notes/reminders-inspection.md|ghi chú chạy]].

**Nhãn bằng chứng:** `Chạy` đã thao tác · `Chạy (vị trí giả lập)` thao tác với toạ độ giả · `Xem` thấy trên giao diện · `Docs` tài liệu hãng · `Suy` suy ra · `GĐ` giả định.

**Giới hạn đợt chạy:** gói dùng thử chặn ở 5 xe ("Your plan is limited to 5 vehicles"), nên không có xe riêng để thử mooc không đồng hồ, xe giờ máy, đồng hồ phụ trên xe thật, phiếu riêng đầu kéo và mooc. Lịch kiểm đã thấy Due Soon; Overdue, Skipped cần qua hạn thật. App Fleetio Go mới có một phiếu không vi phạm. Không làm việc có thể gửi ra ngoài hoặc xoá dữ liệu, không đổi Cài đặt tài khoản.

## 3. User Types (preliminary)

| User Type | Pain Point | Primary Need |
|---|---|---|
| Quản lý phương tiện | Xe quá hạn bảo dưỡng mới biết | Danh sách sắp đến hạn, quá hạn |
| Nhân viên xưởng | Đặt lịch từng xe rất tốn công | Bộ lịch theo dòng xe |
| Lái xe | Phiếu giấy mất thời gian | Kiểm nhanh trên điện thoại |
| Admin của khách | Mỗi khách một mẫu phiếu | Tự dựng biểu mẫu, không cần lập trình |

### 3.1 Tác vụ chính

| Vai trò | Tác vụ | Tần suất | Mức quan trọng | Ghi chú |
|---|---|---|---|---|
| Quản lý phương tiện | Rà nhắc đến hạn | Mỗi ngày | Cao | Bỏ sót làm hỏng xe, trễ đăng kiểm |
| Nhân viên xưởng | Xử lý nhắc thành lệnh | Mỗi ngày | Cao | |
| Lái xe | Nộp phiếu kiểm tra | Mỗi ca | Cao | Kiểm khống làm mất giá trị dữ liệu |
| Admin của khách | Dựng biểu mẫu, gán xe | Hiếm | Trung | |

## 4. Capabilities Breakdown

### P0 — must have

- N1 [Mới] [Gói: Bảo dưỡng đội xe] [Cấu hình] **Nhắc theo hai trục:** thời gian và số km, trục nào đến trước, mỗi trục có ngưỡng Sắp đến hạn riêng; chỉ cần một trục, thiếu cả hai bị chặn; ngưỡng phải nhỏ hơn chu kỳ. `Chạy`. Fleetio: ngưỡng điền sẵn 2 tuần, 500 km. Chu kỳ, ngưỡng là tham số mới, chưa có mã.
- N2 [Mới] [Gói: Bảo dưỡng đội xe] **Trạng thái tự đổi ngay khi lưu số km, từ bất kỳ nguồn nào, không chờ job đêm.** `Chạy`: đo đủ biên còn 501, 500, 1, 0, -1 km ra Upcoming, Due Soon, Due Soon, Overdue, Overdue. Đúng mốc đã Overdue dù chữ vẫn ghi "0 kilometers remaining". Lấy theo trục xấu nhất.
- N3 [Mới] [Gói: Bảo dưỡng đội xe] **Tự lấy lần hoàn thành gần nhất** từ lịch sử khi tạo nhắc; chưa từng làm thì hiện "Never logged for this vehicle". `Chạy`.
- N4 [Mới] [Gói: Bảo dưỡng đội xe] **Xem trước lịch:** form hiện 5 kỳ tới và báo lỗi ngưỡng ngay trong khối xem trước. `Chạy`. Điểm yếu: form Edit không làm mới theo số mới.
- N5 [Mới] [Gói: Bảo dưỡng đội xe] [Cấu hình] **Nhắc giấy tờ xe, người** theo loại, mỗi xe một nhắc cho mỗi loại, có ngày đến hạn và ngưỡng báo trước. `Chạy`. Fleetio: loại xe là Emission Test, Inspection, Insurance, Registration; loại liên hệ là Certification, License Renewal; ngưỡng mặc định xe 3 tuần, liên hệ 3 tuần. Thêm loại mới chưa thử. Danh sách loại, ngưỡng là tham số mới, chưa có mã.
- N6 [Mới] [Gói: Bảo dưỡng đội xe] **Từ nhắc đi thẳng sang xử lý:** nút Resolve trên từng dòng: Add to Work Order (mới hoặc có sẵn), Add to service history; menu: tạm hoãn, Recalculate Compliance, Record History. `Chạy`. Draft Work Order khoá theo trạng thái nhắc, không theo gói: mở khi Due Soon hoặc Overdue, xem N31. Find a shop đi đến bước Confirm, không bấm Assign vì gửi email, SMS thật, xem N35. Send Notifications chỉ `Xem`.
- N19 [Mới] [Gói: Bảo dưỡng đội xe] **Kỳ sau tính từ lần làm thật:** ngày và số đồng hồ của lần hoàn thành, không từ mốc dự kiến; làm sớm là mất phần còn lại của chu kỳ. `Chạy`.
- N20 [Mới] [Gói: Bảo dưỡng đội xe] **Lệnh chưa xong không đổi trạng thái nhắc:** lệnh Open chỉ gắn dải "This Service Task was added to Work Order"; Completed mới tính kỳ mới và sinh Service Entry. `Chạy`.
- N21 [Mới] [Gói: Bảo dưỡng đội xe] **Đầu việc khớp là nhận:** ghi Service Entry có đúng đầu việc thì nhắc tự coi là đã làm, không cần đi từ nhắc. `Chạy`.
- N22 [Mới] [Gói: Bảo dưỡng đội xe] **Đặt tay mốc kỳ tới:** mặc định hôm nay + chu kỳ, đồng hồ hiện tại + chu kỳ; tự tắt sau một lần hoàn thành. `Chạy`. Đây là đường đúng để xe đã chạy lâu không bị quá hạn ngay.

### P1 — should have

- N7 [Mới] [Gói: Bảo dưỡng đội xe] [Cấu hình] **Biểu mẫu kiểm tra tự dựng** với 10 loại mục và Section: Pass/Fail, Number, Free Text, Dropdown, Date/Time, Meter Entry, Photo, Signature, Inventory Adjustment, Tire Readings. `Chạy`: lưu đủ 11 loại, Photo và mục kho đã nộp trên phiếu; nộp là trừ kho ngay, không bước duyệt, tồn 10 sang 7 ở Inventory Activity. Meter Entry chỉ một mục mỗi biểu mẫu; xe có đồng hồ phụ thì hiện 2 ô, bắt nhập cả hai. Áp cho feature mới, đề xuất tên `vehicle-inspection`.
- N8 [Mới] [Gói: Bảo dưỡng đội xe] [Cấu hình] **Luật theo mục:** đổi nhãn Đạt/Không đạt, cho N/A, bắt ảnh hoặc ghi chú khi Đạt, khi Không đạt; Number có khoảng, ngoài khoảng tự Fail, biên tính là đạt; Dropdown gắn "Fail item if chosen". `Chạy`.
- N9 [Mới] [Gói: Bảo dưỡng đội xe] **Workflow theo biểu mẫu:** ba trigger (mục đạt, mục lỗi, nộp phiếu); action đổi trạng thái xe, gửi email, tạo sự cố, gán và bỏ gán người với xe. Biểu mẫu mới có sẵn một workflow "ANY Failed Inspection Item → Create an issue". `Chạy` tạo sự cố, tắt workflow, và "If form is submitted" đổi xe sang In Shop ngay khi nộp, không hỏi, không phân biệt đạt hay lỗi. Trigger từng mục cũng chạy: mục đạt đổi xe sang Inactive, mục lỗi đổi sang Out of Service, không hỏi. Mỗi mục lỗi sinh một sự cố. Gửi email, gán người chưa chạy vì có thể phát thông báo. Không có action tạo lệnh sửa chữa.
- N10 [Mới] [Gói: Bảo dưỡng đội xe] **Vòng đời mục lỗi:** Needs Action, Open Issue, Acknowledged, Resolved, có Failure Timeline. `Chạy`. Needs Action chỉ ra khi workflow tắt; Acknowledged là điểm cuối, không quay lại. Create Issue một cú bấm, không form. Reopen đưa dòng lỗi từ Resolved về Open Issue. Áp vào `incident-report`.
- N11 [Mới] [Gói: Bảo dưỡng đội xe] [Cấu hình] **Gán biểu mẫu theo luật:** mọi xe, theo thuộc tính xe, hoặc xe cụ thể; lịch Daily đến Yearly, bắt đầu trễ, nhắc người lái; không đặt lịch thì dùng "as needed". `Chạy` phần gán xe cụ thể, có lịch Daily và không lịch. Không lịch thì không vào Inspection Schedules. Tần suất chỉ Daily, Weekly, Monthly, Yearly, không có lịch theo số đồng hồ.
- N12 [Mới] [Gói: Bảo dưỡng đội xe] **Bộ lịch theo dòng xe:** một bộ nhiều đầu việc nhiều xe, đồng hồ chính và phụ; chỉ gắn xe cùng đơn vị đồng hồ; có "Set First Service". `Chạy`. Sửa lịch trên bộ làm nhắc đang chạy đổi trạng thái sau xử lý ngầm. Có 14 mẫu hệ thống (Fleetio); chọn mẫu hiện ngay số nhắc sẽ tạo, nhưng cố định Miles lúc tạo. Một dòng lịch chỉ theo đồng hồ phụ vẫn lưu được ("Every 200 hours"); chưa sinh nhắc theo giờ trên xe. Gán theo 28 thuộc tính xe chạy thật một lần; mốc lần đầu tính tuyệt đối theo đồng hồ; sau gán, đầu việc của bộ xám ở form nhắc lẻ. Ô Rule khoá khi tài khoản còn Sample Data nên chưa lưu được (bản trước ghi dùng được là sai).
- N13 [Mới] [Gói: Bảo dưỡng đội xe] **Tỷ lệ tuân thủ** theo lịch sử đúng hạn, trễ, ghi từng lần ("3 weeks, 6 days ahead · 1,600 kilometers ahead"). `Chạy`. Ngày sớm nhưng km vượt vẫn Late. Mức trễ Fleetio: dưới 10% chu kỳ mới On-Time, đúng bằng 10% đã Late (chu kỳ 1.000 km: 99 km On-Time, 100 km Late; chu kỳ 3 tháng: 9 ngày On-Time, 10 ngày Late). Một nhắc nhiều lần: số lần đúng hạn trên số lần làm; trung bình danh sách khớp theo lần (một điểm đo). Là tham số mới, chưa có mã.
- N14 [Mới] [Gói: Bảo dưỡng đội xe] [Cấu hình] **Chống kiểm khống bằng vị trí:** cảnh báo khi một tỉ lệ mục được kiểm từ cùng vị trí, hoặc một mục lệch xa các mục khác. `Xem` cấu hình; `Docs` Fleetio: Proximity Threshold 50–100%, mặc định 80%, Distance Threshold mặc định 100 m. `Chạy (vị trí giả lập)`: trên web không kích hoạt được, mọi phiếu `location_exception` false, gói tin chỉ có một cặp toạ độ cấp phiếu. `Chạy (Fleetio Go)`: một phiếu có toạ độ riêng 21/21 mục, lệch tối đa 37 m, không bị gắn cờ, có hai chỉ báo mục quá gần, số mục quá xa; chưa có ca dương nên chưa đo được ngưỡng. Ngưỡng là tham số mới, chưa có mã.
- N15 [Mới] [Gói: Bảo dưỡng đội xe] [Cấu hình] **Cấm dùng ảnh có sẵn:** bật thì Pick File mở thẳng webcam, không có đường chọn file; tắt thì nhận file. `Chạy`, bật mặc định, chưa chụp thật. Ảnh xác minh đồng hồ luôn phải chụp webcam, không theo cờ này, tick Void không gỡ được. Rất hợp với thói quen gửi lại ảnh cũ; cần đường dự phòng khi máy không có camera.
- N23 [Mới] [Gói: Bảo dưỡng đội xe] **Bảng đối chiếu trước khi gán bộ lịch:** cột Service Task, Conflicting, Duplicate, New Interval, kèm câu cảnh báo chung. `Chạy`. Nhắc tay trùng đầu việc giữ nguyên mã, đổi sang lịch bộ.
- N24 [Mới] [Gói: Bảo dưỡng đội xe] **Gộp nhiều nhắc vào một lệnh:** hộp Resolve liệt kê mọi nhắc của xe để tick thêm. `Chạy`. Vào xưởng làm luôn nhiều việc.
- N25 [Mới] [Gói: Bảo dưỡng đội xe] **Gộp lỗi lặp:** mục lỗi lại khi sự cố còn mở không sinh sự cố mới, chỉ thêm dòng Item Failures và mốc Failure Timeline; sau Resolved thì sinh sự cố mới. `Chạy`.
- N26 [Mới] [Gói: Bảo dưỡng đội xe] **Phiếu ăn theo chuyến đang chạy:** trường Job tự gắn việc đang gán cho xe lúc nộp. `Chạy`. Liên kết kiểm trước chuyến với Lệnh vận tải.
- N27 [Mới] [Gói: Bảo dưỡng đội xe] **Phiên bản biểu mẫu:** sửa mẫu không đổi phiếu cũ, phiếu cũ mang nhãn "Past Version"; phiếu đã nộp không sửa được. `Chạy`.
- N28 [Mới] [Gói: Bảo dưỡng đội xe] **Đọc lốp từ phiếu:** tự sinh ô theo cấu hình trục, khai trục và lắp lốp thiếu ngay trong phiếu, ghi về Tire Readings. `Chạy`. Spare không vào phiếu; mức tối thiểu của biểu mẫu tách khỏi mức của lốp.
- N29 [Mới] [Gói: Bảo dưỡng đội xe] **Vị trí nộp phiếu thành vị trí xe:** phiếu ghi vị trí trình duyệt, sinh Location Entry, xe lên bản đồ. `Chạy (vị trí giả lập)`. Máy chủ tin toạ độ gửi lên, không phát hiện toạ độ giả.
- N32 [Mới] [Gói: Bảo dưỡng đội xe] **Nhật ký thay đổi bản ghi:** Record History ghi ai đổi trường nào, từ giá trị nào sang giá trị nào, có lọc khoảng ngày, trên nhắc và gia hạn. `Chạy`. Dạng trường kỹ thuật, không có lý do, không hiện ở History nghiệp vụ.
- N33 [Mới] [Gói: Bảo dưỡng đội xe] **Thao tác hàng loạt trên nhắc:** menu Actions có thêm vào lệnh, ghi lịch sử, hoãn, bỏ hoãn, thêm và bỏ người theo dõi, xoá. `Xem`, chỉ đọc menu. Không có mục giao nhắc.

### P2 — nice to have

- N16 [Mới] [Gói: Bảo dưỡng đội xe] **Chuyển phiếu giấy thành biểu mẫu số** từ PDF hoặc ảnh bằng AI. `Chạy` hai lần: lần đầu treo khoảng 6 phút, lần sau dưới 30 giây có bản dựng, nên là lỗi lúc đó. Đoán đúng Pass/Fail, Signature; số, ô chọn, đồng hồ, ảnh đều thành Free Text; mọi mục bắt buộc; cờ cấm ảnh tick trên màn nhưng lưu Disabled. Hợp với khách đang dùng phiếu giấy, nhưng phải rà lại.
- N31 [Mới] [Gói: Bảo dưỡng đội xe] **Bản nháp lệnh bằng AI:** bấm từ một nhắc, AI gom toàn xe, ghép sự cố đang mở với đầu việc, liệt kê việc đến hạn, tạm tính từ lịch sử, báo lệnh đang mở; xong dưới 2 phút, chạy nền. Chỉ mở khi nhắc Due Soon hoặc Overdue. `Chạy` đến Review và Discard, chưa bấm Add to. Điểm yếu: tick sẵn cả việc còn 3 tháng.
- N34 [Mới] [Gói: Bảo dưỡng đội xe] **Đọc hoá đơn thành phiếu dịch vụ bằng AI:** màn đối chiếu cạnh tài liệu, dưới 30 giây đọc đúng đồng hồ, ngày, số hoá đơn, nhà cung cấp, thuế, tổng; gộp dòng thành đầu việc hệ thống. `Chạy`. Điểm yếu: đầu việc gợi ý không gắn với nhắc đang chờ, phải tự thêm mới đóng nhắc.
- N35 [Mới] [Gói: Bảo dưỡng đội xe] **Giao dịch vụ thuê ngoài từ nhắc:** hộp 3 bước, gom nhắc của xe, chọn người, cách báo. `Chạy` đến Confirm; chưa thấy danh sách cửa hàng.
- N36 [Mới] [Gói: Bảo dưỡng đội xe] **AI đánh giá phiếu dịch vụ:** sau lưu ra "Acceptable" kèm nhận xét, cần phiếu có giá; có chỗ dạy luật riêng của đội xe. `Chạy` đọc kết quả, chưa thêm luật.
- N17 [Mới] [Gói: Bảo dưỡng đội xe] **Dự đoán ngày đến hạn** từ số km trung bình ngày, theo từng thuộc tính của nhắc. `Chạy`: bật bằng ô tích ở Settings, không hỏi xác nhận, tắt là về nguyên trạng. Dự báo đổi trạng thái thật: còn 700 km trên ngưỡng 500 km vẫn sang Due Soon khi ngày dự báo vào ngưỡng 2 tuần (Fleetio). Popover bày đủ phép tính; Group Week, Month chỉ có khi bật. Số km tự tính thật, đồng hồ phụ, thông báo chưa đo.
- N18 [Mới] [Gói: Bảo dưỡng đội xe] **Thời lượng làm phiếu và nguồn nộp** ghi tự động. `Chạy`: "Duration 2m 17s", "Fleetio Web App". Thời lượng quá ngắn là dấu hiệu kiểm khống (`Suy`).
- N30 [Mới] [Gói: Bảo dưỡng đội xe] **KPI đếm theo xe:** 2 nhắc Overdue trên 1 xe vẫn là "Overdue Vehicles 1". `Chạy`. Hợp câu hỏi "bao nhiêu xe cần vào xưởng".

## 5. Core Flows (Happy Path)

### 5.1 Vòng đời một nhắc bảo dưỡng

Đã chạy trọn vòng, kể cả đóng nhắc bằng lệnh và bằng phiếu dịch vụ.

1. Dựng đầu việc, tạo nhắc lẻ hoặc gán bộ lịch. Nhắc chưa có lịch sử: mốc km là bội số chu kỳ tính từ 0, mốc thời gian tính từ hôm nay; muốn tính từ số hiện tại thì đặt tay.
2. Số km tăng từ lệnh, phiếu đổ dầu, phiếu kiểm, nhập tay hay thiết bị.
3. Hệ thống đổi trạng thái ngay khi lưu, theo trục xấu nhất.
4. Người dùng xử lý từ Resolve hoặc tạm hoãn.
5. Lệnh Open chưa đổi gì; lệnh Completed hoặc Service Entry mới tính kỳ mới từ lần làm và ghi On-Time hoặc Late.
6. Không có trạng thái Đóng: nhắc lặp vòng.

```
Upcoming ── còn ≤ ngưỡng ──> Due Soon ── đồng hồ ≥ mốc ──> Overdue
    ▲                           ▲                            │
    │                           └── void đồng hồ, lùi ───────┤
    └────── hoàn thành: kỳ mới từ lần làm, ra trạng thái theo mốc mới ─┘
              Tạm hoãn: về trạng thái thường khi hết hạn hoặc Remove Snooze
```

### 5.2 Gia hạn giấy tờ

1. Tạo nhắc theo loại, chọn xe hoặc liên hệ, ngày đến hạn, ngưỡng.
2. Trạng thái Due Soon, Overdue theo ngày.
3. Gia hạn: sửa tay Due Date sang kỳ mới, Status về "Upcoming". Không có Resolve, không có kỳ, không tải giấy tờ mới; Record History ghi ai đổi hạn từ ngày nào sang ngày nào.

### 5.3 Kiểm tra xe

1. Admin dựng biểu mẫu, từ trống, từ mẫu có sẵn hoặc từ phiếu giấy (`Chạy` một lần, không ra bản dựng).
2. Admin gán xe, đặt lịch nếu cần; xử lý ngầm hơn 1 phút, trong lúc đó ô chọn xe rỗng.
3. Lái xe chọn biểu mẫu và xe, làm phiếu một lần xong, không có nháp. Hệ thống ghi giờ bắt đầu, vị trí, chuyến đang chạy.
4. Nộp phiếu: mục lỗi có workflow tự thành sự cố (gộp nếu đang mở); workflow tắt thì Needs Action. Xem tiếp [[docs/_research/fleetio/fleetio-repair.md|Sửa chữa]] Mục 5.2.

```
Dựng biểu mẫu ─> Gán xe, lịch ─> Làm phiếu ─> Nộp ─┬─ Đạt hết: lưu lịch sử
                                                   ├─ Lỗi, workflow bật: Sự cố ─> Lệnh hoặc Resolve with Note
                                                   └─ Lỗi, workflow tắt: Needs Action ─> Acknowledge hoặc Create Issue
```

## 6. System Behavior Deep Dive

### 6.1 Decision Points

| ID | Flow | Khi nào | YES | NO |
|---|---|---|---|---|
| D1 | 5.1 | Nhiều xe cùng lịch | Dùng bộ lịch | Nhắc riêng từng xe |
| D2 | 5.1 | Nhắc đến hạn, chưa sửa được | Tạm hoãn đến ngày chọn | Xử lý ngay |
| D3 | 5.3 | Biểu mẫu có lịch | Theo dõi đến hạn, quá hạn | Làm khi cần, không bao giờ quá hạn (`Docs`) |
| D4 | 5.3 | Vị trí các mục gần như trùng nhau | Gắn Location Exception (`Docs`) | Bình thường; trên web luôn rơi vào nhánh này; phiếu Fleetio Go lệch tối đa 37 m cũng rơi vào nhánh này |
| D5 | 5.1 | Nhắc chưa có lịch sử, xe đã chạy nhiều | Đặt tay mốc kỳ tới | Quá hạn ngay vì mốc tính từ 0 |
| D6 | 5.3 | Workflow "mục lỗi tạo sự cố" đang bật | Sinh hoặc gộp sự cố | Needs Action |
| D7 | 5.3 | Sự cố của mục đó còn mở | Gộp, thêm mốc thời gian | Sự cố mới, không mở lại sự cố cũ; chỉ Reopen tay mới mở lại |
| D8 | 5.1 | Cần gom việc của xe nhanh, nhắc đã Due Soon hoặc Overdue | Draft Work Order, AI gom toàn xe, phải rà bỏ việc còn xa | Add to Work Order, tự tick từng nhắc |
| D9 | 5.3 | Biểu mẫu cấm ảnh có sẵn | Chỉ webcam, không camera thì không nộp được | Chọn file từ máy; ảnh đồng hồ vẫn chỉ webcam |
| D10 | 5.3 | Có workflow đổi trạng thái (form submitted, mục đạt, mục lỗi) | Xe đổi ngay, không hỏi, kể cả phiếu đạt hết | Xe giữ nguyên |
| D11 | 5.1 | Trễ so với hạn | Dưới 10% chu kỳ (Fleetio): On-Time, chữ đỏ; từ 10%: Late | On-Time |
| D12 | 5.3 | Mục kho có chọn phụ tùng | Nộp là trừ kho ngay, không duyệt | "No parts used" |
| D13 | 5.1 | Forecasting bật, ngày dự báo vào ngưỡng thời gian | Due Soon, kể cả còn trên ngưỡng km | Theo mốc thường |

### 6.2 Cases đã chạy

Đủ ở [[docs/_research/fleetio/srs/fleetio-reminders-inspection-spec.md|SRS]] Mục 13, gồm cả điều không xảy ra.

### 6.3 State Transitions

| Entity | Từ | Sang | Trigger | Quay lại được? | Bằng chứng |
|---|---|---|---|---|---|
| Nhắc | Upcoming | Due Soon | Còn ≤ ngưỡng | Có khi mốc đổi | `Chạy` |
| Nhắc | Due Soon | Overdue | Đồng hồ ≥ mốc, hoặc đến ngày | Có: Void đồng hồ, hoàn thành, sửa chu kỳ | `Chạy` |
| Nhắc | Overdue | Due Soon | Void đồng hồ, hoặc hoàn thành khi mốc mới gần | Có | `Chạy` |
| Nhắc | Overdue | Upcoming | Sửa chu kỳ, có Record History, không bắt lý do | Có | `Chạy` |
| Nhắc | Overdue | Snoozed | Chọn ngày hoãn ở tương lai | Tự về dưới 2 phút sau mốc, hoặc Remove Snooze, hoặc hoàn thành | `Chạy` |
| Nhắc | Upcoming | Snoozed | Chọn ngày hoãn; Next Due giữ nguyên | Remove Snooze về Upcoming | `Chạy` |
| Nhắc | Upcoming | Overdue | Đặt tay hạn cũ hơn hôm nay, không bị chặn | Có, hoàn thành | `Chạy` |
| Gia hạn | Due Soon | Overdue | Sửa ngày về quá khứ | Có, sửa ngày | `Chạy` |
| Gia hạn | Due Soon | Upcoming | Sửa ngày sang kỳ mới, Record History ghi | Có, sửa ngày | `Chạy` |
| Lịch kiểm | Upcoming | Due Soon | Thời gian trôi, hạn không đổi; mốc theo ngày tài khoản là `Suy` | Nộp phiếu (`Suy`) | `Chạy` |
| Mục lỗi | (nộp phiếu) | Issue #n | Workflow bật | Không | `Chạy` |
| Mục lỗi | (nộp phiếu) | Needs Action | Workflow tắt | Không | `Chạy` |
| Mục lỗi | Needs Action | Acknowledged | Acknowledge, ghi chú tuỳ chọn | Không, trạng thái cuối | `Chạy` |
| Mục lỗi | Needs Action | Open Issue | Create Issue, một cú bấm, không form | Không có đường quay về Needs Action trên giao diện đã thấy | `Chạy` |
| Mục lỗi | Open Issue | Resolved | Resolve with Note | Có: Reopen | `Chạy` |
| Mục lỗi | Resolved | Open Issue | Reopen sự cố, không hỏi lý do; Resolution Details biến mất, Timeline không thêm dòng | Có: Resolve lại | `Chạy` |
| Bản nháp lệnh | Drafting | Ready | Xử lý nền, dưới 2 phút | Discard | `Chạy` |
| Xe | Active | In Shop | Workflow "If form is submitted" | Sửa tay bằng Edit Vehicle | `Chạy` |

### 6.4 Interrupted Transactions

| Tình huống | Hệ thống còn lại gì | Resume | Cleanup |
|---|---|---|---|
| Không có quyền vị trí | Vẫn làm được phiếu, có cảnh báo | Phiếu ghi "Location permission was not enabled" | Không có |
| Rời form phiếu đang làm | Trình duyệt chặn "Leave site?", phiếu mất | Không có nháp ở Inspection History (`Chạy`) | Không có |
| Đổi biểu mẫu sau khi đã có phiếu | Phiếu cũ giữ nhãn cũ, nhãn "Past Version" (`Chạy`) | Không cần | Không có |
| Đang xử lý ngầm gán xe vào biểu mẫu | Tab xe rỗng, ô chọn xe "No options" hơn 1 phút (`Chạy`) | Tự xong, không báo ở tab đang mở | Không có |
| Đang đồng bộ bộ lịch | Nhắc cũ chưa đổi khoảng 1 phút (`Chạy`) | Thông báo "Complete" | Không có |
| Smart Upload treo | Form khoá bằng hộp, không báo lỗi, không có thời hạn (`Chạy` lần đầu; lần sau chạy được) | Restart Processing | Đóng, xác nhận Discard |
| Bản nháp AI đang soạn | Chạy nền, có thể rời trang (`Chạy`) | Dải "Ready for your review." trên nhắc của xe | Discard |
| Nộp khi ảnh đang tải | Báo "is required" dù xem trước đã hiện (`Chạy`) | Chờ "File uploaded", bấm lại | Không có |

### 6.5 Other Edge Cases

- **Xe không có GPS, không có số km mới:** nhắc theo số km đứng yên, chỉ trục thời gian còn tác dụng (`Suy`).
- **Số km bất thường** có thể đẩy sai trạng thái nhắc; xem [[docs/_research/fleetio/fleetio-vehicle.md|Phương tiện]] Mục 6.5. Void số sai thì trạng thái lùi ngay (`Chạy`).
- **Mục Đọc lốp, xe chưa khai trục:** nộp phiếu thì báo lỗi, nhưng mục hiện hộp "More info needed" cho người kiểm khai trục ngay trong phiếu, Done xong tự sinh lốp (`Chạy`). Bản trước ghi là chặn cứng, lái xe không tự sửa được: sai.
- **Mục Đọc lốp, xe thiếu lốp:** hộp "Install Missing Tires" lắp ngay trong phiếu, không hỏi gì thêm (`Chạy`).
- **Mooc chưa gán biểu mẫu:** "No inspection forms exist yet" dù tài khoản có biểu mẫu; câu chữ gây hiểu nhầm (`Chạy`).
- **Tài khoản chưa có phân loại** khi gán biểu mẫu: chưa thử.
- **Lệch múi giờ thiết bị và tài khoản:** số đồng hồ bị chặn sai, mục Date/Time lệch 13 giờ, không báo (`Chạy`). Cột Submitted At ở Item Failures cũng lệch đầu phiếu, chưa rõ vì sao.
- **Máy không có camera:** mục Photo khi bật cờ cấm ảnh và ảnh đồng hồ đều không qua được, phiếu không nộp được (`Chạy`).
- **Đồng hồ phụ bật trên xe không có:** tuỳ chọn bị bỏ qua, không báo; xe có thì bắt nhập, tắt Photo Verification các dòng ảnh vẫn hiện (`Chạy`).
- **Làm phiếu khi xe Inactive:** được, workflow vẫn chạy (`Chạy`).
- **Đồng hồ bằng đúng số hiện tại:** nhận, không báo trùng (`Chạy`).
- **Bộ từ mẫu:** cố định Miles lúc tạo, đổi ở Edit chưa biết có quy đổi số không (`Chạy` phần tạo).
- **Bấm Current Operator làm điều kiện Rule:** lọc được, không lưu thành Rule (`Chạy`). Mọi thuộc tính khác cũng chưa lưu được khi tài khoản còn Sample Data.

## 7. Validation, Limits & Wording

### 7.1 Validation rules

| Field | Rule | Bằng chứng |
|---|---|---|
| Nhắc | Bắt buộc xe, đầu việc; có ít nhất một trục | `Chạy` |
| Ngưỡng nhắc | Nhỏ hơn chu kỳ; bằng cũng bị chặn; so đúng khi khác đơn vị | `Chạy` |
| Ngày hoãn | Không chặn ngày đã qua; không có ô lý do | `Chạy` |
| Mục Không đạt | Bắt ghi chú nếu cấu hình; lớp ghi chú chỉ lưu khi gõ vào ô Comment | `Chạy` |
| Mục Đạt | Một số mục bắt ghi chú | `Chạy` |
| Xác nhận cuối | Phải tick ở biểu mẫu có ô này; không có trong kiểu Signature mặc định | `Chạy` |
| Số đồng hồ | Phải khớp lịch sử theo thời điểm, hoặc Void | `Chạy` |
| Hoàn thành lệnh | Bắt Started At, số đồng hồ, theo Cài đặt tài khoản | `Chạy` |
| Giấy tờ | Bắt buộc xe, loại, ngày đến hạn; mỗi xe một nhắc cho mỗi loại | `Chạy` |
| Resolve with Note | Note bắt buộc | `Chạy` |
| Acknowledge | Comments không bắt buộc | `Chạy` |

### 7.2 Limits & Quotas (exact values)

| Tham số | Giá trị | Window | Behavior khi vượt |
|---|---|---|---|
| Thông báo nhắc | Fleetio: 7 giờ sáng khi đến hạn, sau đó mỗi tuần | Đến khi xử lý | Theo cài đặt thông báo của từng người (`Xem`) |
| Ngưỡng nhắc mặc định | Fleetio: 2 tuần, 500 km | Mỗi nhắc | Sửa được (`Chạy`) |
| Ngưỡng gia hạn mặc định | Fleetio: xe 3 tuần, liên hệ 3 tuần | Mỗi nhắc | Sửa được (`Chạy`) |
| Hạn mức xe gói dùng thử | Fleetio: 5 xe, xe Sample không tính | Tài khoản | "Your plan is limited to 5 vehicles" (`Chạy`) |
| Mục Meter Entry | Fleetio: 1 mỗi biểu mẫu | Biểu mẫu | Panel khoá (`Chạy`) |
| Hoãn mặc định | Fleetio: +7 ngày | Mỗi lần hoãn | Chỉnh tự do (`Chạy`) |

### 7.3 Wording samples (exact strings)

#### Error messages

| Tình huống | Wording | Code |
|---|---|---|
| Mục lỗi thiếu ghi chú | "must contain a remark on failure" | E-001 |
| Mục Đạt thiếu ghi chú | "must contain a remark on pass" | E-002 |
| Thiếu giá trị | "is required" | E-003 |
| Chưa có cấu hình trục | "Please select axle configuration before submitting the form" | E-004 |
| Chưa tick xác nhận | "This must be checked if there are no defects." | E-005 |
| Nộp phiếu lỗi | "Could not submit inspection form. Please fix any errors and try again." | E-006 |
| Nhắc thiếu chu kỳ | "Please provide a usage or a time interval" | E-008 |
| Ngưỡng ≥ chu kỳ | "Primary Meter Due Soon Threshold is too high (can't be equal to or greater than Primary Meter Interval)" | E-009 |
| Đồng hồ trái lịch sử | "must be less than 2,499 or marked as void" | E-013 |
| Thiếu số đồng hồ của mục | "requires a Odometer" | E-015 |
| Thiếu ảnh đồng hồ | "must attach an odometer image" | E-020 |
| Không có camera | "Webcam Disabled", "Please enable your webcam to take a photo." | E-021 |
| Mục kho thiếu nhãn | "can't be blank" | E-023 |
| Hết hạn mức bản ghi | "You've reached the maximum number of records allowed on your account." | E-024 |
| Rule không tự động hoá được | "We are unable to automate this program because the following attribute has been selected. Current Operator" | E-025 |
| Không khớp xe | "No Vehicles have been found" | E-026 |
| Smart Upload treo | "Taking longer than usual..." | E-027 |
| Thiếu đồng hồ phụ | "requires a Secondary Meter" | E-028 |
| Rule khi còn Sample Data | "...while sample data is turned on" | E-029 |
| Draft Work Order chưa mở | "Available when this reminder is due soon or overdue." | E-030 |

Mã đầy đủ có tiền tố `E-fleetio-reminders-inspection-`.

#### Info / neutral messages

| Tình huống | Wording |
|---|---|
| Không lấy được vị trí | "Fleetio was unable to detect your location from your web browser. Location data will not be saved on this inspection." |
| Tạm hoãn | "1 service reminder will be snoozed until the selected date and time. The reminder will return to its normal state after the snooze period is over." |
| Hoãn xong, kể cả ngày đã qua | "The Service Reminder was successfully updated." |
| Gán bộ lịch | "1 Vehicle will receive 2 Service Reminders based on the intervals below. Any conflicting individual Service Reminders will be replaced by the schedule from the Service Program." |
| Gỡ xe khỏi bộ lịch | "This will remove all service reminders on the vehicle from this service program." |
| Nộp phiếu | "Inspection form submitted." |
| Ghi nhận lỗi | "Successfully acknowledged failed inspection item." |
| Soạn bản nháp lệnh | "Drafting service", "No need to wait here — we'll notify you when the draft is ready." |
| Xe có lệnh đang mở | "A Work Order is already open for this vehicle" |
| Tạo sự cố từ mục lỗi | "Inspection Item was linked to an Issue." |
| Mở lại sự cố | "Successfully reopened Issue." |
| Gán biểu mẫu mọi xe | "This Rule enables the inspection form for ALL vehicles. The form will also be enabled for any new vehicles added to the account." |

## 8. Assumptions

- `GĐ` Lái xe làm phiếu trên Delta Super App, có quyền camera và vị trí.
- `GĐ` GPS trên điện thoại đủ chính xác để phát hiện đứng yên một chỗ; xe tải, bãi lớn cần kiểm chứng.
- `GĐ` Fleetio Go có cùng luật phiếu với web. Đã biết vị trí từng mục khác (`Chạy (Fleetio Go)`); xác nhận lại, ngoại tuyến, ảnh webcam trên app chưa kiểm, xem Mục 14.

## 9. Risks

| Rủi ro | Mức | Giảm thiểu |
|---|---|---|
| Lái xe kiểm khống, tick nhanh cho xong | Cao | Vị trí, thời lượng, bắt ảnh ở mục quan trọng |
| Toạ độ gửi từ thiết bị bị giả, hệ thống tin hoàn toàn | Cao | Đối chiếu với GPS xe, chuyến đang chạy |
| Thêm phiếu làm chậm giờ xuất bến | Cao | Biểu mẫu ngắn, chỉ mục an toàn |
| Sửa chu kỳ, hoãn, ghi nhận lỗi, mở lại sự cố không để lại lý do | Cao | Bắt lý do, đưa thay đổi lên lịch sử nghiệp vụ |
| Bản nháp AI tick sẵn việc còn xa, bấm nhanh là làm sớm | Trung | Không tick sẵn việc chưa tới ngưỡng |
| Bắt chụp trực tiếp mà thiết bị không có camera, phiếu kẹt lại | Trung | Đường dự phòng có ghi nhận ngoại lệ; lái xe dùng app điện thoại nên ít gặp hơn web (`Suy`) |
| Workflow đổi trạng thái xe không phân biệt đạt, lỗi | Trung | Chỉ cho đổi trạng thái khi có mục lỗi, hỏi xác nhận |
| Phiếu trừ kho ngay, không duyệt, không lý do; lái xe gõ sai là lệch tồn | Trung | Đề xuất có bước duyệt hoặc giới hạn số lượng |
| Số km ngày nhập sai làm dự báo kéo nhiều nhắc sang Due Soon | Trung | Báo rõ nhắc đổi vì dự báo, kiểm số km ngày bất thường |
| AI đoán sai loại mục, người dùng bấm tạo luôn | Trung | Bắt rà trước khi tạo, không mặc định bắt buộc mọi mục |
| Quá nhiều thông báo khiến người dùng bỏ qua | Trung | Hồ sơ thông báo theo vai trò |
| Bắt buộc số km làm dữ liệu rác nếu nhập vội | Trung | Lấy từ GPS, nhập tay chỉ khi thiếu |
| Mooc không đồng hồ vướng luật bắt số đồng hồ khi xong lệnh | Trung | Tắt theo loại phương tiện; chưa kiểm được ở Fleetio |

## 10. Success Criteria (preliminary)

- Không có xe quá hạn giấy tờ mà không ai biết.
- Tỷ lệ nhắc xử lý đúng hạn đo được.
- Mục lỗi kiểm tra đều có sự cố hoặc ghi nhận kèm lý do, không có mục bỏ quên.

## 11. Open Questions

| ID | Câu hỏi | Nguồn khách |
|---|---|---|
| OQ-1 | Delta có yêu cầu kiểm tra xe trước chuyến không? Ai kiểm, bao lâu một lần? | Chưa có trong tài liệu khách gửi |
| OQ-2 | Chu kỳ bảo dưỡng của Delta theo km, theo tháng hay cả hai, theo từng dòng xe? | Chưa có trong tài liệu khách gửi |
| OQ-3 | Giấy tờ nào cần nhắc: đăng kiểm, bảo hiểm, bằng lái, phù hiệu? Báo trước bao lâu? | Chưa có trong tài liệu khách gửi |
| OQ-4 | Phiếu kiểm hỏng có cho xe chạy tiếp không, ai quyết? | Chưa có trong tài liệu khách gửi |
| OQ-5 | Mooc, máy phát có lịch riêng theo giờ chạy không? Liên quan `vehicle-management` OQ-4 | Đề xuất tiện ích GPS (25/9/2025), mục 3 |
| OQ-6 | Làm sớm hơn mốc thì Delta chấp nhận mất phần còn lại của chu kỳ, hay hợp đồng bảo dưỡng theo km đòi giữ mốc cũ? | Chưa có trong tài liệu khách gửi |
| OQ-7 | Ảnh kiểm tra bắt chụp trực tiếp hay cho tải file? Thiết bị không có camera thì sao? | Chưa có trong tài liệu khách gửi |
| OQ-8 | Phiếu kiểm nộp xong có được tự đổi trạng thái xe không, ai duyệt? Liên quan OQ-4 | Chưa có trong tài liệu khách gửi |

## 12. Next Steps

- Hỏi Delta OQ-1 trước khi quyết định lập feature kiểm tra xe.
- Khi đến lượt `/brainstorm reminders`, dùng Mục 4 và Mục 13 làm danh sách gợi ý.
- Mở lại lịch Daily trên `TEST-NHAC-PHIEU` sau hạn để thấy Overdue, Skipped.
- Nếu được phép lưu trữ xe TEST không dùng: chạy mooc không đồng hồ, xe giờ máy, đồng hồ phụ, phiếu riêng đầu kéo và mooc, xe mới tự vào Rule.
- Nếu được Disable Sample Data: lưu Rule bộ lịch, xem xe mới có tự vào không.
- Trên Fleetio Go: dựng một ca Location Exception dương để đo ngưỡng, kiểm xác nhận lại sau sửa, làm phiếu ngoại tuyến.

## 13. Giải pháp đáng học và điểm yếu

### Đáng học

- **Trạng thái đổi ngay khi lưu số, theo trục xấu nhất:** không cần chờ job, hợp với số km GPS về liên tục.
- **Bảng đối chiếu khi gán bộ lịch** (Conflicting, Duplicate, New Interval): cho đầu kéo cùng dòng xe, thấy trước hệ quả rồi mới áp.
- **Resolve gom mọi nhắc của xe vào một lệnh:** vào xưởng làm luôn nhiều việc, giảm số lần dừng xe.
- **Lỗi lặp gộp vào sự cố đang mở nhưng vẫn giữ dòng lỗi và dòng thời gian:** tránh một lốp hỏng sinh hàng chục sự cố khi nhiều lái kiểm cùng đầu kéo hoặc mooc.
- **Phiên bản biểu mẫu "Past Version":** phiếu cũ không đổi khi sửa mẫu, cần cho kiểm toán và tranh chấp.
- **Đóng dấu Job vào phiếu kiểm:** liên kết kiểm trước chuyến với chuyến đang chạy, rất hợp Lệnh vận tải.
- **Khai trục và lắp lốp thiếu ngay trong phiếu:** phát hiện thiếu dữ liệu lúc kiểm, không bắt quay lại màn quản trị.
- **KPI đếm theo xe:** nói đúng câu hỏi điều phối.
- **Bản nháp lệnh gom cả xe:** ghép sự cố đang mở với đầu việc, liệt kê việc đến hạn, tạm tính từ lịch sử, biết lệnh đang mở; xong dưới 2 phút, chạy nền nên không chặn người dùng.
- **Record History:** dấu vết đủ ai, lúc nào, từ giá trị nào sang giá trị nào, trên cả nhắc và gia hạn.
- **Bộ lịch có trục đồng hồ phụ riêng:** một dòng chỉ theo giờ máy vẫn lưu được, hợp máy phát trên xe chạy km.
- **Mẫu bộ lịch hiện ngay số nhắc sẽ tạo:** thấy hệ quả trước khi lưu.
- **Vị trí từng mục trên app, hai chỉ báo tách riêng:** mục quá gần nhau và số mục quá xa là hai dấu hiệu kiểm khống khác nhau.
- **Create Issue một cú bấm từ dòng lỗi:** quản lý không phải nhập lại, tiêu đề tự sinh từ mục.
- **Rule không nhận thuộc tính đổi liên tục:** cảnh báo ngay Current Operator thay vì lưu một Rule chạy sai.
- **Popover bày đủ phép tính dự báo từng bước:** người dùng tự kiểm được vì sao ra ngày đó, đáng học cho đầu kéo, mooc khi dự báo theo km.
- **Bật một công tắc, tắt lại không mất dữ liệu:** thử an toàn. Cho nhập tay số km ngày cho xe mới chưa đủ đồng hồ.
- **Draft Work Order khoá theo trạng thái nhắc, có câu giải thích:** không cho soạn nháp khi chưa tới ngưỡng, nói rõ khi nào mở.
- **Màn Smart Upload đặt tài liệu cạnh các ô đọc được:** rà nhanh, sửa ngay trước khi đổ vào form.
- **Sau khi gán bộ lịch, đầu việc của bộ xám ở form nhắc lẻ:** chặn trùng ngay từ đầu.
- **Inventory Activity ghi số phiếu, tồn trước, tồn sau:** truy được từng lần trừ về đúng phiếu kiểm.

### Điểm yếu, đề xuất Invlogis tách riêng

- **Nhắc mới chưa có lịch sử tính mốc từ 0:** đầu kéo đã chạy nhiều vừa khai báo là Overdue ngay. Đề xuất Invlogis: mặc định tính từ số hiện tại.
- **Đổi chu kỳ xoá trắng quá hạn, Acknowledge không cần lý do, Snooze không có lý do, ngày hoãn đã qua vẫn báo thành công:** lỗ hổng kiểm soát. Có dấu vết ở Record History dạng trường kỹ thuật (bản trước ghi không có dấu vết là sai), nhưng không bắt lý do, không cảnh báo, không hiện ở History nghiệp vụ. Đề xuất Invlogis: bắt lý do, đưa lên lịch sử nghiệp vụ, chặn ngày đã qua.
- **Làm sớm mất phần còn lại của chu kỳ:** tốt cho an toàn, nhưng cần cân nhắc với hợp đồng bảo dưỡng theo km (OQ-6).
- **Gia hạn không có khái niệm kỳ, không có chứng từ, không có nút gia hạn:** tra được ai đổi hạn qua Record History (bản trước ghi không có lịch sử là sai), nhưng giấy tờ đầu kéo, mooc, đăng kiểm cần giữ chứng từ qua từng kỳ. Đề xuất Invlogis: mỗi kỳ gia hạn là một bản ghi có chứng từ.
- **Lẫn giờ thiết bị và giờ tài khoản:** chặn sai số đồng hồ, lệch giờ mục Date/Time 13 giờ. Delta chỉ một múi giờ nhưng SaaS đa khách phải chốt một nguồn giờ.
- **Bắt số đồng hồ khi xong lệnh là cấu hình tài khoản:** mooc không đồng hồ sẽ vướng (`Suy`, chưa kiểm được vì không tạo được xe). Đề xuất Invlogis: cấu hình theo loại phương tiện.
- **Workflow không có action tạo lệnh:** muốn tự tạo lệnh phải qua Automations.
- **Rule, bộ lịch chạy ngầm, không có dấu hiệu rõ ở màn đang mở;** biểu mẫu chưa gán xe chỉ hiện danh sách rỗng.
- **Mở Edit rồi lưu làm Notifications từ Inactive thành Active:** đổi cài đặt mà người dùng không đụng tới.
- **Không có nháp phiếu, rời trang là mất:** đề xuất Invlogis cho lưu nháp trên app vì sóng ở bãi yếu.
- **Sự cố từ phiếu lốp không có trường vị trí lốp, mô tả có thể thiếu lỗi:** đề xuất Invlogis gắn vị trí thành dữ liệu.
- **Máy chủ tin toạ độ gửi lên, không so giữa các phiếu:** chống kiểm khống trên web không có tác dụng; muốn có tác dụng phải làm phiếu trên app.
- **Bản nháp AI tick sẵn cả việc còn 3 tháng:** bấm nhanh là làm sớm, mất phần còn lại của chu kỳ. Đề xuất Invlogis: chỉ tick sẵn việc đã tới ngưỡng, việc còn xa để người dùng chủ động thêm.
- **Bắt webcam không có đường dự phòng, cờ cấm ảnh và ảnh đồng hồ theo hai luật khác nhau, Void không gỡ được:** máy không có camera thì phiếu kẹt. Đề xuất Invlogis: một luật chung cho ảnh, có ngoại lệ ghi nhận lý do.
- **Workflow nộp phiếu đổi trạng thái xe không phân biệt đạt, lỗi:** phiếu đạt hết cũng đưa xe vào xưởng. Đề xuất Invlogis: đổi trạng thái chỉ khi có mục lỗi đúng mức, có người xác nhận.
- **Reopen không hỏi lý do, Resolution Details biến mất, Timeline không thêm dòng:** mất ngữ cảnh lần giải quyết trước. Đề xuất Invlogis: giữ lịch sử giải quyết, bắt lý do mở lại.
- **Bộ từ mẫu cố định Miles:** không hợp khách dùng km. Đề xuất Invlogis: chọn đơn vị lúc tạo, mẫu theo dòng xe là dữ liệu cấu hình.
- **Smart Upload khoá form, không có thời hạn, không báo lỗi:** khi treo người dùng kẹt trong hộp. Đề xuất Invlogis: chạy nền như bản nháp lệnh, có thời hạn.
- **Smart Upload biểu mẫu đoán nhầm số, ô chọn, đồng hồ, ảnh thành Free Text, mục nào cũng bắt buộc, cờ cấm ảnh lưu lệch màn Review:** tạo xong phải sửa tay. Đề xuất Invlogis: hiện rõ loại đoán, cho đổi ngay trên màn rà.
- **Hoá đơn không gắn được nhắc đang chờ:** nhập xong mà nhắc vẫn mở. Đề xuất Invlogis: gợi ý đầu việc từ nhắc của xe trước.
- **Mục đạt cũng đổi trạng thái xe, không hỏi, không báo trên phiếu:** lái xe không biết vừa làm xe dừng. Đề xuất Invlogis: báo ngay trên phiếu, có người xác nhận.
- **Trừ kho từ phiếu không duyệt, không lý do; phiếu đếm dòng không đếm số lượng:** đề xuất Invlogis duyệt theo ngưỡng, hiện đúng số lượng.
- **Ưu tiên sự cố tự gán không có câu giải thích:** cùng phiếu có Critical và No Priority. Đề xuất Invlogis: ghi lý do gán, cho sửa.
- **Rule bộ lịch bị khoá chỉ vì còn dữ liệu mẫu:** khách dùng thử không thử được tính năng này. Đề xuất Invlogis: dữ liệu mẫu tách khỏi luật thật.
- **Bấm ASAP làm Continue khoá, không báo gì:** có thể là lỗi, chưa rõ.
- **Dự báo âm thầm đổi Due Soon:** số km ngày nhập sai có thể làm đầy hàng việc. Đề xuất Invlogis: ghi rõ nhắc đổi vì dự báo.
- **Nhóm "This Week" chứa nhắc không có ngày, Group Week ẩn cột Next Due:** dễ đọc nhầm. Đề xuất Invlogis: nhóm riêng "không có dự báo".
- **Form Vehicle và nhắc nói khác nhau về số km ngày; phép tính "1 day ago × 10" ra 0; 700 km ÷ 100 hiện 6 ngày:** chưa giải thích được, xem SRS OQ-28 đến OQ-31.
- **Chữ lỗi sai ngữ cảnh:** "is required" khi ảnh còn đang tải; "behind" đỏ trên dòng On-Time.

## 14. Câu hỏi đã có câu trả lời từ chạy thử

Mã theo [[docs/_research/fleetio/srs/fleetio-reminders-inspection-spec.md|SRS]] Mục 12.

| Mã SRS | Câu hỏi | Trả lời | Mức |
|---|---|---|---|
| OQ-8 | Lỗi lại khi sự cố còn mở thì trùng hay gộp? | Gộp vào sự cố đang mở, thêm mốc thời gian, mỗi lần lỗi vẫn là một dòng Item Failures; không báo cho người kiểm khi đang làm phiếu | `Chạy` |
| OQ-7 | Phiếu không vị trí có bị đánh dấu không? | Một phần: phiếu không vị trí vẫn nộp được; toạ độ giả không bị chặn; mọi phiếu web thử đều `location_exception` false; Fleetio Go có vị trí từng mục, ca lệch tối đa 37 m vẫn false; chưa thử tắt định vị trên app, chưa có ca dương | `Chạy (vị trí giả lập)`, `Chạy (Fleetio Go)` |
| — | Có câu hỏi xác nhận lại sau khi sự cố Resolved không? | Trên web không thấy, lỗi lại thì sinh sự cố mới. Tài liệu hãng ghi có xác nhận; có thể chỉ ở Fleetio Go, chưa kiểm được | `Chạy`, `Docs` |
| OQ-13 | Create Issue và Reopen đi đâu? | Create Issue một cú bấm, sang sự cố mới, dòng lỗi sang Open Issue. Reopen không hỏi lý do, sự cố về Open, dòng lỗi về Open Issue, Resolution Details biến mất | `Chạy` |
| OQ-11 | Lịch kiểm đi thế nào? | Một phần: có Due Soon thật; Overdue, Skipped còn chờ qua hạn | `Chạy` |
| OQ-14 | Fleetio Go có vị trí từng mục không? | Có, 21/21 mục; xác nhận lại, ngoại tuyến chưa kiểm | `Chạy (Fleetio Go)` |
| OQ-15 | Photo, các trigger, đổi trạng thái, trừ kho? | Đã chạy; Send an email, Assign user còn mở | `Chạy` |
| OQ-16 | Biên 10%, nhiều lần? | Dưới 10% mới On-Time: 99 km On-Time, 100 km Late trên 1.000 km; 9 ngày On-Time, 10 ngày Late trên 92 ngày; nhiều lần tính theo lần | `Chạy` |
| FR-009 | Forecast chạy thế nào? | Bật bằng ô tích, đổi trạng thái thật, popover phép tính, Group Week, Month; 4 điểm lệch còn mở OQ-28 đến OQ-31 | `Chạy` |
| OQ-19 | Draft Work Order khoá vì gì? | Theo trạng thái nhắc, không theo gói: "Available when this reminder is due soon or overdue." | `Chạy` |
| OQ-21 | Rule bộ lịch có tự thêm xe mới không? | Chưa biết; ô Rule khoá khi còn Sample Data, phải tắt ở cấp tài khoản | `Chạy` phần khoá |
