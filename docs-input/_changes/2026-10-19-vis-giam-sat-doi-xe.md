# Thay đổi: Phân hệ VIS — Hệ thống giám sát phương tiện & Quản trị đội xe

> Bản cũ: nhận 2026-10-11 (`VIS_Oct 8 2026_Update.pdf`, 9 trang, tên "Vehicle Intelligent Service (VIS)") · Bản mới: nhận 2026-10-19 (`Phân hệ VIS_October 18 2026.pdf`, 34 trang) · Tài liệu: [vis-giam-sat-doi-xe.md](../sop/vis-giam-sat-doi-xe/vis-giam-sat-doi-xe.md)

## Tóm tắt nghiệp vụ

- **Tài liệu dài gấp gần 4 lần, chia thành 3 khối:**
  - Quản lý chi phí vận hành (III).
  - Quản lý vận hành và hiệu suất tài xế (IV).
  - Trung tâm dữ liệu cho Thanh tra vận tải (V).
  - Thêm mục VI là yêu cầu gửi EUP.
- **App Delta trên điện thoại lái xe trở thành nguồn GPS dự phòng (2.1, 2.2.3):**
  - Khi hộp đen EUP mất kết nối liên tục quá **15 phút**, km được bù bằng GPS của App (Tổng km thực tế = km EUP + km App bù).
  - Có bộ lọc chặn giả lập tọa độ (Fake GPS).
  - Số liệu có dùng nguồn dự phòng được đánh dấu `*` trên báo cáo.
- **2.2.2 Geofence thêm phân nhánh theo loại xe:** xe đầu kéo chạy thuật toán ghép cặp PUR để gắn mooc và container. Xe tải thùng thì ẩn trường Mooc/Container, ghi "Không áp dụng".
- **2.2.5 Cảm biến dầu:** quét tần suất cao khi nổ máy, 30 phút/lần khi tắt máy, bắt biến cố thể tích tăng hoặc giảm đột ngột. Bản 08/10 không nói tần suất này.
- **Đổi số mục, nội dung giữ nguyên:**
  - Tắc đường và nổ máy ngủ gộp vào 2.2.4.
  - Km GPS chuyển từ 2.2.7 sang 2.2.3.
  - Đối soát dầu thực đổ chuyển từ 3.6 lên 3.2.
  - Dầu bù do tắc đường và do tìm vỏ chuyển từ 3.2, 3.3 xuống 3.3.1, 3.3.2.
  - Các ngưỡng không đổi: dưới 5 km/h quá 10 phút; 0 km/h quá 10 phút; quét lại VETC sau 120 phút; tự nạp VETC (tài khoản Delta VT 15/150 triệu, Delta HCM 5/50 triệu).
- **4.1 và 4.2 gộp nguyên giải pháp PUR (SRC-29, bản 14/10) và D&H (SRC-28, bản 15/10)** vào VIS.
- **4.3 mới — VETS, dự báo ETA và gửi email cho khách:**
  - Tính ETA gốc khi xe **check-out khỏi Geofence nơi xuất phát** chứ không còn tính từ lúc bắt đầu Lệnh.
  - Tính lại ETA cơ học mỗi 5 phút. Lệch quá **10%** cung chuẩn, kẹt xe, hoặc định kỳ 30 phút với tuyến trên 300 km thì mới gọi lại API bản đồ.
  - Gửi 3 mốc email: lúc rời điểm xuất phát; khi còn 30 phút tới đích; cảnh báo nội bộ khi ETA vượt "giờ Closing Time − 2 tiếng".
  - Danh sách người nhận lấy theo DK05 đích, CC CS phụ trách và đội trưởng đội xe.
  - Có mẫu email.
- **4.3.2 mới — DMS, quản lý thời gian lưu xe tại kho khách:**
  - Check-in khi vào Geofence DK05. Check-out khi ra xa quá 100 m với vận tốc ≥5 km/h.
  - Tách thời gian nổ máy chờ và tắt máy chờ.
  - Báo cáo nhật ký lưu bãi và email Excel ký số gửi khách đúng **24:00** hằng ngày. Xe còn nằm bãi thì cộng dồn sang ngày sau.
- **5.1 mới — MATG, đối soát km tháng:**
  - Chạy ngày 01 hằng tháng, khung thời gian động theo từng xe: từ check-out của Lệnh đầu tiên đến check-in của Lệnh cuối cùng.
  - Ngưỡng ±2%. Thiếu km (< −2%) kèm vé mồ côi VETC thì chuyển Nhân sự phạt chạy việc riêng. Thừa km (> 2%) kèm lịch sử bỏ điểm Geofence thì chuyển Thanh tra phạt chạy tắt.
- **5.2 mới — DMS lái xe:**
  - Ngày làm việc tính từ Engine ON đầu tiên đến Engine OFF cuối cùng trong bãi.
  - Thời gian lái thực tế = Engine ON − (kẹt xe + nổ máy chờ).
  - Đếm **4 giờ lái liên tục**: cảnh báo ở phút 210, vi phạm ở phút 240. Bộ đếm về 0 khi dừng hoặc tắt máy ≥15 phút, hoặc đổi thẻ RFID.
  - Lệnh vận tải gắn theo cặp [đầu kéo + thẻ RFID tài xế].
  - Có 6 tình huống: đèn đỏ, kẹt xe, nghỉ đúng, đổi ca, quên thẻ (gán tay và hồi tố), hỏng đầu đọc (giữ phiên tối đa 60 phút).
  - ⚠ **Thẻ RFID tài xế** là thiết bị mới, chưa có trong tài liệu nào.
- **5.3 mới — HDS, chẩn đoán thiết bị:**
  - Phát hiện hộp đen ngoại tuyến quá 15 phút trong khi App vẫn chạy và xe > 5 km/h.
  - Phát hiện tọa độ nhảy cóc vượt 80 km/h, và sensor dầu mất tín hiệu.
  - Phân 3 màu Xanh/Vàng/Đỏ. Lỗi được xác nhận thì tự tạo lệnh sửa chữa sang Xưởng.
- **5.4 mới — VPS, điểm đỗ:**
  - Vùng đỗ hợp lệ đổi theo chặng có hàng hay không. Chặng có hàng tính theo mã JobID: J01–J03 xuất, J04–J06 nhập.
  - Ban ngày được đỗ dọc đường dưới 60 phút. Ban đêm tối đa 200 phút: nhắc ở phút 21–60, vi phạm khi quá 60 phút.
  - Vùng đệm 500 m quanh kho. Hoãn thủ công khi có sự cố.
  - Mức Đỏ (đang chở hàng) đẩy ngay ở phút 31, kèm chứng từ gốc lấy từ DIS. Mức Cam gom lúc 24:00.
  - ⚠ Trong tình huống 4 ghi "giới nghiêm 22:00–04:00, 30 phút", lệch với khung "ban đêm 18:00–06:00, 60 phút" của tình huống 1. Cần hỏi khách.
- **5.5 mới — TAMS, mooc mồ côi:**
  - Lấy 3 điều kiện tách cặp của PUR, thêm điều kiện thứ 4: vị trí cuối của mooc nằm ngoài danh mục "Vùng cắt mooc hợp lệ" (bãi Delta, chi nhánh, nhà máy D&H).
  - Báo động Đỏ ngay. Thanh tra điều xe kéo về, hoặc chuyển Nhân sự phạt.
- **VI mới — yêu cầu gửi EUP:**
  - Webhook cho các sự kiện máy, thẻ RFID và vị trí: 5 phút/lần khi chạy đều; ngay lập tức (<1 giây) khi bẻ lái ≥30° hoặc đổi trạng thái dừng/chạy.
  - Dầu 30 phút/lần khi tắt máy.
  - Xin EUP ngưỡng nhận diện đổ dầu, hút dầu, và API tra km theo khoảng thời gian.
  - Đường truyền TLS 1.3, chữ ký HMAC-SHA256.
  - Trả lời một phần câu hỏi mở về ngưỡng dầu ở `vehicle-telematics`.

## Đổi số mục

| Mục cũ (08/10) | Mục mới (18/10) |
|---|---|
| II. Giải pháp kỹ thuật | II. Hạ tầng xử lý dữ liệu & Công nghệ lõi |
| 2.1 Kiến trúc hệ thống | 2.1 Kiến trúc hệ thống và Luồng thu thập dữ liệu |
| 2.2.1 Thời gian xe sẽ đến (ETA) | 2.2.1 Dự báo thời gian phân tầng (Hybrid ETA Engine) |
| 2.2.2 Thời gian xe đã đến (Geofencing) | 2.2.2 Địa giới ảo & Phân luồng cấu hình xe |
| 2.2.3 Traffic jam; 2.2.4 Idling | 2.2.4 Phân tích biến cố chuyển động và trạng thái máy |
| 2.2.5 Dầu diesel tồn và bất thường | 2.2.5 Giám sát nhiên liệu và Điện áp xung lực |
| 2.2.7 Tổng số km (Mileage) | 2.2.3 Làm sạch & Ghép dữ liệu hành trình |
| III. Giải pháp nghiệp vụ | III. Quản lý chi phí vận hành |
| 3.1 Hệ thống quản lý tự động vé cầu đường | 3.1 Quản lý tự động vé cầu đường (Toll fee) |
| 3.6 Đối soát lượng dầu thực đổ | 3.2 Quản lý cấp đổ và đối soát dầu thực tế |
| 3.2 Dầu hao phí do tắc đường | 3.3.1 |
| 3.3 Dầu hao phí khi chọn container rỗng | 3.3.2 |
| 3.4, 3.5 | 3.4, 3.5 (giữ số) |

## Tài liệu đang dùng nguồn này

- `docs/vehicle-telematics/brainstorms/vehicle-telematics.md` — K1–K4, S2–S10, T1, X1 theo số mục cũ; thêm App Delta GPS dự phòng, 5.2–5.5, VI.
- `docs/transport-dispatch/brainstorms/transport-dispatch.md` — I1 (ETA: nay tính từ check-out điểm xuất phát, email 3 mốc), I2–I12, E7, F8; thêm lưu bãi 4.3.2, MATG 5.1.
- `docs/vehicle-management/brainstorms/vehicle-management.md` — V1–V5, H4, H5; thêm HDS tạo lệnh sửa chữa (5.3.3 bước 3).
- `docs/meetings/decks/2026-10-06-oq-dispatch-coordination-deck.md`, `docs/meetings/decks/2026-10-15-oq-vis-deck.md` — trích SRC-06: rà câu nào bản mới đã trả lời (ngưỡng EUP, ETA).
- `docs-input/_coverage/vis-pur-ghep-tach-mooc.md` (SRC-29), `docs-input/_coverage/vis-dh-cat-keo.md` (SRC-28) — nội dung nay là mục 4.1, 4.2.

## Chi tiết

Theo `diff.py`. Phần lớn mục bị đếm "thêm mới/bỏ" là do đổi tên và đổi số. Các mục còn nội dung giống bản cũ đã ghi ở bảng Đổi số mục. Thay đổi thật đã tóm ở trên.

## Tổng quan thay đổi

| Loại | Số mục | Mục |
|---|---|---|
| Thêm mới | 14 | 4.1. Tự động ghép/tách cặp giữa mooc và đầu kéo/số container (PUR); 4.2. Tự động hóa Lệnh vận tải phụ cho mô hình cắt kéo container (D&H); 4.3.1. Tính toán ETA của xe và phát thông báo; 4.3.2. Quản lý thời gian lưu xe; 5.1. Đối soát kms hàng tháng theo chu kỳ vận hành động (MATG); 5.2. Quản lý thời gian làm việc của lái xe và Lệnh vận tải đã thực hiện; 5.3. Giám sát hoạt động của thiết bị & chống gian lận (HDS); 5.4. Quy trình kiểm soát và cảnh báo vi phạm điểm đỗ quy định (VPS); 5.5. Quy trình kiểm soát và cảnh báo rơ mooc mồ côi sai quy định (TAMS); 6.1. Yêu cầu kết nối & luồng dữ liệu đẩy (Webhook); 6.2. Yêu cầu cung cấp thông số cấu hình mặc định; 6.3. Tiêu chuẩn an ninh & đường truyền bảo mật; V. Thanh tra vận tải; VI. Kết nối với EUP |
| Bỏ | 0 | |
| Sửa | 4 | 2.1. Kiến trúc hệ thống và Luồng thu thập dữ liệu (Data Ingestion); 2.2.2. Địa giới ảo & Phân luồng cấu hình xe (Geofencing Polygon Engine); 2.2.3. Làm sạch & Ghép dữ liệu hành trình (Mileage & Data Stitching Engine); 2.2.5. Giám sát nhiên liệu và Điện áp xung lực (Fuel Sensor Engine) |
| Giữ nguyên | 13 | I; 2.2.1; 2.2.4; 2.2.6; 3.1; 3.1.2; 3.1.3; 3.2; 3.3.1; 3.3.2; 3.4; 3.5; (đổi số theo bảng trên) |
