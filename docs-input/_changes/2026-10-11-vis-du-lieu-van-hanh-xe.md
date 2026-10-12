# Thay đổi: VEHICLE INTELLIGENT SERVICE (VIS) — trước là "Dữ liệu vận hành xe"

> Bản cũ: nhận 2026-10-02 (docx "Dữ liệu vận hành xe", ngày 30/09/2026 — bản gốc không lưu trong repo) · Bản mới: nhận 2026-10-11 (`VIS_Oct 8 2026_Update.pdf`, ngày 08/10/2026) · Tài liệu: [vis-du-lieu-van-hanh-xe.md](../sop/vis-du-lieu-van-hanh-xe/vis-du-lieu-van-hanh-xe.md)

## Tóm tắt nghiệp vụ

- **Đổi tên và cấu trúc.** "Dữ liệu vận hành xe" thành "Vehicle Intelligent Service (VIS) — Giải pháp số hóa toàn diện dữ liệu vận hành đội xe Delta". Tài liệu có số mục và mục lục, chia 2 phần: II Giải pháp kỹ thuật (7 chức năng 2.2.1–2.2.7) và III Giải pháp nghiệp vụ (quy trình 3.1–3.6). Mục lục không liệt kê mục 3.6 (đối soát dầu thực đổ) dù thân tài liệu có mục này.
- **Thứ tự mục tiêu đổi.** Bản cũ đặt "điều xe tự động" là mục tiêu (1). Bản mới đặt (1) cập nhật và duyệt Lệnh vận tải tự động theo thời gian thực, (2) ghi nhận vé cầu đường hoặc báo cáo tránh trạm lên Lệnh vận tải, (3) điều xe tự động. Kết nối VETC từ phần "khi kết hợp" nay thành một phần chính của giải pháp.
- **Mới: thanh toán vé cầu đường tập trung (mục 3.1.2).**
  - Master Account VETC do Delta VT và Delta HCM đăng ký. Mọi xe trực thuộc tài khoản này, thẻ RFID trừ thẳng vào quỹ chung.
  - Vietcombank tự nạp tiền (Auto-topup): khi số dư xuống dưới **15 triệu (Delta VT) / 5 triệu (Delta HCM)** thì nạp để số dư về **150 triệu / 50 triệu**. Lý do nêu trong tài liệu: tránh phí quản lý hạn mức **3%** của ví trả sau.
- **Mới: sơ đồ 4 bên (Delta MIS, EUP, VETC, Vietcombank) ở mục 3.1.1**, phân 3 loại vé:
  - vé qua trạm: ghi lên Lệnh vận tải;
  - vé tránh trạm: **trả vào lương lái xe**;
  - vé mồ côi: không ghi vào đâu, chuyển Kế toán Delta.
  - ⚠ Cách xử lý vé tránh trạm qua lương lái xe chỉ có trong sơ đồ, phần chữ không nói. Cần hỏi khách: "trả vào lương" là trừ lương hay cộng lương, áp dụng tự động hay sau khi duyệt.
- **Quy trình đối soát vé (trước là "đối soát tự động vé VETC", nay là mục 3.1.3) viết gọn lại:**
  - Mục tiêu (3) đổi từ "vé phát sinh mà hệ thống chưa ghi nhận trên Lệnh vận tải" thành "vé phát sinh ngoài lộ trình, không ghi nhận vào đâu, chuyển kế toán xử lý".
  - Bước 1 bỏ chi tiết "chốt giờ Bắt đầu/Kết thúc khi Geofence của địa điểm lấy từ Danh mục cảng/bãi hoặc DK05", chỉ còn "khung thời gian theo Geofence các địa điểm giao nhận".
  - Bước 2 gọi VETC khi "xe kết thúc Lệnh vận tải". Bản cũ ghi "khi xe kích hoạt Geofence điểm đích"; mục 2.2.6 bản mới vẫn giữ cách ghi cũ.
  - Bước 4 bỏ câu so hóa đơn tổng với tổng vé đã duyệt và bỏ câu gợi ý mẫu ("Giao dịch này thuộc xe A… tại trạm X"). Cách xử lý đổi từ "phê duyệt chi phí phát sinh hợp lý vào Lệnh vận tải" thành "phê duyệt chi phí hợp lý". Bản mới không còn nói chi phí đã duyệt có đưa vào Lệnh vận tải hay không.
  - Bỏ chữ "BOT".
- **Không đổi nghiệp vụ:** các chức năng kỹ thuật ETA, Geofencing, Traffic jam, Idling, Diesel, tránh trạm, Mileage (2.2.1–2.2.7) và các quy trình 3.2–3.6 giữ nguyên số liệu: dưới 5 km/h liên tục hơn 10 phút; idling hơn 10 phút; quét 30 phút khi tắt máy; hút dầu giảm quá 5 lít trong dưới 3 phút; đổ dầu tăng trên 20 lít trong 10 phút; quét lại VETC sau 120 phút; tìm vỏ ở mỗi bãi trên 10 phút; chỉ áp dụng JobID J01. Mục 3.6 Bước 1 chỉ sửa câu: "lượng dầu thực tế nạp vào bình" được gộp vào danh sách thông số chốt.

## Đổi số mục

Bản cũ không có số mục (Word dùng số tự động hiển thị "1."). Bảng dưới để sửa các tài liệu đang dẫn theo tên mục:

| Bản cũ (tên mục) | Bản mới |
|---|---|
| (mở đầu, mục tiêu) | I. Đặt vấn đề |
| Kiến trúc hệ thống | 2.1 |
| Quy trình xử lý chi tiết, 7 chức năng | 2.2, 2.2.1–2.2.7 |
| Quy trình nghiệp vụ đối soát tài chính & vận tải | III. Giải pháp nghiệp vụ |
| — | 3.1 Hệ thống quản lý tự động vé cầu đường; 3.1.1 Sơ đồ; 3.1.2 Quản lý chi phí tập trung *(mới)* |
| Quy trình đối soát tự động vé VETC | 3.1.3 Quy trình đối soát và quản lý chi phí trên Delta MIS |
| Quy trình xác định lượng dầu hao phí do tắc đường | 3.2 |
| … khi chọn container rỗng | 3.3 |
| … do "Nổ máy ngủ" | 3.4 |
| Quy trình giám sát dầu tồn và lập báo cáo hút dầu bất thường | 3.5 |
| Quy trình đối soát lượng dầu thực đổ | 3.6 |

## Tài liệu đang dùng nguồn này

- `docs/dispatch-coordination/brainstorms/dispatch-coordination.md`: link ở frontmatter; ý E7 (dữ liệu GPS trên Lệnh: vé trạm, cờ tránh trạm, kẹt xe) và F8 (VETC là nguồn chuẩn chi phí đường bộ). Cần rà theo cách phân loại vé mới (tránh trạm thì trả lương, vé mồ côi chuyển kế toán) và theo master account.
- `docs/meetings/decks/2026-10-06-oq-dispatch-coordination-deck.md`: link ở frontmatter. Rà các câu hỏi mở về VETC và tránh trạm, xem bản mới đã trả lời câu nào.
- `docs/_shared/logistics-primer.html` (dòng 722): dòng nguồn dẫn tên file cũ.

## Chi tiết

`diff.py` không ghép được mục vì bản cũ không có heading đánh số. Phần trên đã so theo từng đoạn và từng ý. Ngoài các điểm đã nêu, chữ của 2.1, 2.2.1–2.2.7, 3.2–3.5 trùng với bản cũ, chỉ khác định dạng: danh sách ✓ và cấp heading. Sơ đồ kiến trúc 2.1 vẫn như bản cũ. Bản cũ đã dựng sơ đồ này thành mermaid; bản mới dùng ảnh gốc kèm danh sách chữ trong sơ đồ.
