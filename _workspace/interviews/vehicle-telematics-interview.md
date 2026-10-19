# Brainstorm VIS (dữ liệu vận hành xe): ghi chép phỏng vấn (2026-10-14 → 2026-10-15)

Nguồn: Vehicle Intelligent Service — VIS (08/10/2026, SRC-06); SIM & VIS — Công tác chuẩn bị (11/10/2026, SRC-24) mục 2.2, 3.3, 3.4; SRS cũ LG v2.0 (SRC-22) Module 5 Danh mục › Feature 04.01 Phương tiện (trang 2014–2430), Barem và sensor iGAS (trang 2505); SRS mobile (SRC-23) Epic 06 Phiếu cấp dầu.
Phỏng vấn qua trang trả lời https://claude.ai/artifact/GRtqWJ6Zwc7a3P4MuBoNhr (câu trả lời lưu trong trang, mã câu p1-… đến p7-…). @author `@szitphan`.

## Cách làm đã chốt
- Deep, đủ 7 phần, từng phần một; mỗi câu có "Theo nguồn" và "Đề xuất".
- Ghi kết quả theo nơi nhận (Phần 2 câu A, DEC-100): Lệnh vận tải (`transport-dispatch`), Quản lý phương tiện (`vehicle-management`), feature dùng chung mới `vehicle-telematics`; phần định mức, cấp dầu, lịch nhắc, hoá đơn VETC chuyển sang `fuel-allowance`, `fuel-issuing`, `reminders`, `invoice-management`.

## Kiểm tra phần phương tiện hiện có (SRS LG v2.0)
- Module 5 Danh mục › Feature 04.01 Phương tiện; đường vào "Dashboards › Quản lý tài sản › Phương tiện"; tác nhân "người dùng phần mềm xưởng".
- Hồ sơ xe 6 tab: Thông tin chung · Hàng hoá và thiết bị · Bàn giao/thu hồi · Sửa chữa · Định mức · Lịch nhắc (UC04.00.01–07).
- Trạng thái xe: lái xe giữ (Đang hoạt động · Đang sửa chữa · Đang tạm giữ); công ty giữ (Sẵn sàng hoạt động · Đang sửa chữa).
- Ô chờ dữ liệu ngoài: "Số vận hành hiện tại lấy theo API bên thứ 3"; thẻ "Dầu diesel tồn" chưa chốt nguồn.
- Bàn giao, thu hồi (UC04.01.01–10): yêu cầu → duyệt → ký biên bản; nhập tay "KMs bàn giao", "Mô tả nhiên liệu" bằng chữ. Liên quy trình: phiếu dGas4 xong → bàn giao; phiếu dGas5 xong → thu hồi, chạy định mức.
- Định mức nhiên liệu (UC04.01.11–21): kế hoạch chạy định mức → tiêu hao thực tế theo chặng → định mức khoán (tỷ lệ hao hụt %, 8 mức tải l/km: Đầu kéo không, Vỏ container rỗng, dưới 10T … trên 30T); áp riêng xe hoặc cả loại xe theo vận hành. Không có định mức l/giờ.
- iGAS đo bồn cây dầu nội bộ (khác cảm biến bình dầu xe của EUP). Phiếu cấp dầu: dGas1 cấp quản lý, dGas2 xưởng, dGas3 vận tải (chip "X L chờ nhận" = dầu tích luỹ từ Lệnh đã xong), dGas4 đổ đầy bình, dGas5 chốt dầu (kỳ tháng). Cây nội bộ (iGAS) bơm được dGas1–5; cây mua ngoài, hoá đơn lẻ chỉ dGas1, dGas3.

## Phần 1 — Tổng quan (chốt)
- Mô tả: phần mềm tự đọc dữ liệu GPS, cảm biến dầu của từng xe và giao dịch vé VETC, đổi thành sự việc có ý nghĩa gắn đúng Lệnh, đúng xe, để duyệt Lệnh, tính bù dầu, đối soát vé và dầu không nhập tay. Điều xe tự động để P2 (`transport-dispatch` F9).
- Lồng vào giải pháp có sẵn trước, chưa có chỗ mới sinh feature (→ DEC-100).
- Ranh giới, phân tầng SaaS: đồng ý đề xuất (sự kiện hành trình, đối soát vé [Lõi]; dầu tồn, hút dầu, đổ dầu [Gói: Giám sát nhiên liệu]; EUP, VETC là kết nối thay được; mọi ngưỡng qua mã P; tài khoản mẹ VETC + Vietcombank tự nạp [Riêng Delta], ngoài phần mềm).
- Vấn đề: cả 4 — (a) đối soát hoá đơn VETC bằng tay cuối tháng; (b) bù dầu kẹt xe theo lời lái xe kể; (c) hút dầu, đổ thiếu phát hiện muộn hoặc không phát hiện; (d) tránh trạm không ai biết.
- Giai đoạn: "Làm hết" → Phần 2: cả VIS vào giai đoạn 1 (30/03/2027).
- Feed thêm SRC-24 mục 2.2, 3.3, 3.4: đồng ý.
- Phương tiện: định mức l/giờ → hỏi khách; tìm vỏ dùng mức "Đầu kéo không"; thêm số thẻ ETC + mã thiết bị GPS vào hồ sơ xe; bàn giao đang có phiếu dGas 4/5 bắt buộc; chạy định mức lấy km, dầu từ GPS: có; cảnh báo xe chạy ngoài Lệnh: có; lịch nhắc theo km từ GPS: có (Phần 3) → `reminders`.
- Chỗ lệch: thời điểm gọi VETC → hỏi khách + [Mới] lấy danh mục trạm thu phí để dự toán vé; vé tránh trạm phải ghi nhận, đối soát và chốt theo từng Lệnh; dịch vụ bản đồ → hỏi khách, chọn bên nhiều dữ liệu (tắc đường, biển báo) vì là đầu vào điều chỉnh cung đường; định mức kẹt xe và nổ máy ngủ dùng chung một con số l/giờ.

## Phần 2 — Người dùng và quyền (chốt)
- Ghi theo nơi nhận (C), phần dùng chung sinh `vehicle-telematics`.
- Bàn giao dùng dGas4, thu hồi dùng dGas5 (câu hỏi mở xác nhận khách).
- Vé tránh trạm chốt theo Lệnh, người duyệt chọn tính lái xe hoặc chấp nhận kèm lý do; kết quả là nguồn bảng kê tránh trạm theo lái xe theo kỳ cho bộ phận lương. Cách xử lý khi VETC chưa trả dữ liệu → câu hỏi mở.
- Dự toán vé theo cung đường khi lập Lệnh: đưa vào.
- Vai trò, cảnh báo tức thời (hút dầu, chạy ngoài Lệnh → quản lý phương tiện chi nhánh khai thác; kẹt xe trễ mốc theo B6; lệch dầu → quản lý cây dầu; kênh thông báo web và app, không SMS, không email), chỗ xem (Lệnh, hồ sơ xe, bảng kê báo cáo, thông báo), phạm vi chi nhánh (chi nhánh khai thác xe lúc xảy ra; Lệnh theo chi nhánh Lệnh; VETC theo tài khoản mẹ, pháp nhân), bảng tần suất: đồng ý.
- Quy mô: chưa có số → câu hỏi mở.

## Phần 3 — Luồng chính (chốt)
- L1 Lệnh có dữ liệu GPS, L2 tìm vỏ J01, L5 hút dầu, L7 xe chạy ngoài Lệnh, L8 dự toán vé: đồng ý.
- L3: nhắc lái xe tắt máy → câu hỏi mở đề xuất với khách.
- L4: cảm biến xác nhận bình đầy thay cho chọn tay "đầy bình"; luồng L4 gắn vào phiếu dGas5 → BL-152.
- L6: dùng luồng liên quy trình sẵn có: phiếu dGas4 xong mới qua bàn giao, thu hồi tương tự dGas5; phiếu xong là phần dầu đã đạt, biên bản chỉ xem lại; làm biên bản trước hay phiếu trước đều được.
- L9: đã đối soát theo Lệnh thì cuối kỳ chỉ kiểm phát sinh (Phần 4 câu D).
- Quyết định: ③ cách ghép phiếu đồng ý, con số hỏi khách; ④ người duyệt sửa số lít bù, bắt lý do; ⑤ tìm vỏ chỉ dùng GPS, lái xe không báo; ② xếp hàng ở cảng có bù không, ⑥ trường hợp miễn cảnh báo chạy ngoài Lệnh → hỏi khách.

## Phần 4 — Chi tiết luồng (chốt)
- Phân loại (anh sửa lại, Phần 4 câu A): đứng yên hẳn, máy nổ, quá 10 phút = nổ máy ngủ (cả trong Lệnh, gắn Lệnh); nhích dưới 5 km/h, máy nổ, quá 10 phút = kẹt xe. Tai nạn, kẹt cứng → đề xuất (Phần 5 câu A) → hỏi khách.
- Đầy bình: dGas4, dGas5 làm ở cây dầu nội bộ, vòi bơm tự ngắt; lệch → đề xuất (Phần 5 câu B) → hỏi khách.
- Bàn giao, thu hồi theo luồng liên quy trình (câu C), cuối kỳ chỉ kiểm phát sinh (câu D): đồng ý.
- Thông tin lưu, điểm rẽ nhánh D1–D11, trạng thái trạm trên Lệnh, trạng thái đề xuất bù dầu (Đã duyệt → dầu chờ nhận dGas3), hai bảng tình huống: đồng ý.
- Sự việc cần xử lý: bỏ trạng thái "Đang xem".
- Mất tín hiệu GPS → câu hỏi mở, đề xuất chụp ảnh định vị theo mốc. Đổi xe giữa chặng chắc không xảy ra → hỏi khách. Lệnh mở lại sau khi duyệt: bỏ (Lệnh "Đã duyệt" là trạng thái cuối). 2 container 20 feet của 2 Lệnh trên 1 xe → hỏi khách.
- Sơ đồ vòng 1: thêm dầu định mức của Lệnh (theo cung đường ban đầu) vào dGas3; sơ đồ đổ dầu phải có dGas1, 2, 3, còn dGas4, 5 chỉ xét đầy bình.

## Phần 5 — Kiểm tra, giới hạn, câu chữ (chốt)
- Kẹt cứng, vòi bơm tự ngắt → câu hỏi mở cho khách.
- Lệnh trả lại: anh hỏi vì sao lái xe sửa giờ hoàn thành → Phần 6 câu A trả lời: không sửa.
- Lịch nhắc theo km → `reminders`.
- Sơ đồ vòng 2: anh hỏi sao không khớp VETC ngay khi qua trạm → Phần 6 câu B; dGas1, dGas3 bơm ngoài được, người ghi nhận nhập số lít thực bơm.
- Mọi ngưỡng `P-…` → câu hỏi mở cho khách chốt.
- Kiểm tra dữ liệu: đồng ý + số dầu cấp bù cộng số dầu định mức theo Lệnh không vượt dung tích bình; km không sửa tay.
- Câu lỗi, xác nhận, thông báo, nhãn: đồng ý. 17 câu hỏi mở: đủ.

## Phần 6 — Hệ thống (chốt)
- Lệnh trả lại giữ kết quả đối soát; khớp vé từng trạm khi VETC gửi về (câu hỏi mở nêu hệ quả từng đáp án); dGas3 mỗi lần không vượt chỗ trống trong bình, km chỉ từ GPS, mất GPS lấy lần đọc gần nhất: đồng ý.
- Sơ đồ vòng 3: chốt cả hai.
- Dịch vụ ngoài qua `vehicle-telematics`; danh mục trạm thu phí dùng chung mọi khách [Lõi] (DEC-101); việc chạy nền, tức thời, 8 báo cáo: đồng ý; kỳ báo cáo = tháng + chọn khoảng ngày tuỳ ý.

## Phần 7 — Ngoại lệ, rủi ro (chốt)
- Xe chưa gắn GPS, xe không có cảm biến, trạm chưa có trong danh mục, thẻ ETC gắn nhầm, VETC trừ trùng → hỏi khách. Xe thuê ngoài, xe nhà thầu: không quản lý (DEC-102). Hai người cùng xử lý: như đề xuất. Lệnh không hết chạy: xét bằng GPS, chỉ xử lý khi GPS hỏng.
- Dầu chờ nhận còn tồn khi thu hồi xe hoặc lái xe nghỉ: chốt để tính thưởng vào lương lái xe. Cách tính kỳ (qua nửa đêm, qua tháng; Lệnh theo ngày duyệt) → hỏi khách.
- Rủi ro: bỏ "cả VIS vào giai đoạn 1 với 3 đối tác"; phần còn lại đưa khách xem (câu hỏi mở).
- Giả định, chỉ số thành công, câu hỏi mở 18–23: đồng ý.

## Sơ đồ đã chốt: đổ dầu và đối soát phiếu (chờ feature `fuel-issuing`, BL-152)

```
 LÁI XE, CÂY DẦU         PHẦN MỀM                          CẢM BIẾN (EUP)
 Lập phiếu cấp dầu ────► Phiếu chờ bơm
                           dGas1, 2, 3: số lít cố định
                           Cây nội bộ (iGAS) bơm được dGas1–5;
                           cây mua ngoài, hoá đơn lẻ chỉ dGas1, dGas3
 Bơm dầu
   Cây nội bộ ─────────► Số lít thực bơm lấy từ iGAS
   Cây mua ngoài ──────► Nhân viên cây dầu nhập số lít thực bơm
   Hoá đơn lẻ ─────────► Lái xe nhập số lít thực bơm
                                                          Dầu tăng trên 20 lít
                         Ghi sự kiện đổ dầu ◄──────────── trong 10 phút, xe đứng
                         ◇ Ghép được phiếu cùng xe trong khung giờ?
                         ├─ Không ─► Nghi đổ ngoài luồng ─► Bảng kê nghi vấn
                         └─ Có ─► ◇ Loại phiếu?
                            ├─ dGas1, 2, 3 ─► So lít cảm biến với lít thực bơm
                            │                 ◇ Lệch trong dung sai?
                            │                 ├─ Có ─► Khớp
                            │                 └─ Không ─► Thiếu · Thừa ─► Bảng kê nghi vấn
                            └─ dGas4, 5 ─► Vòi tự ngắt, iGAS ghi số lít
                                           Chờ số đo ổn định
                                           ◇ Cảm biến thấy đã đầy?
                                           ├─ Có ─► Đã đầy (theo cảm biến)
                                           └─ Không ─► Nhắc bơm bồi một lần
                                                       ◇ Đã đầy?
                                                       ├─ Có ─► Đã đầy
                                                       └─ Không ─► Chốt theo số iGAS,
                                                          ghi thiếu x lít ─► Bảng kê nghi vấn
 QUẢN LÝ CÂY DẦU ◄──────────────── Cảnh báo lệch
 Xử lý: Vi phạm · Hợp lệ · Lỗi thiết bị
```

Bảng tình huống đổ dầu (đã chốt): có sự kiện + có phiếu + trong dung sai → Khớp; cảm biến ít hơn phiếu → nghi đổ thiếu hoặc cây dầu gian lận; cảm biến nhiều hơn phiếu → nghi đổ thêm ngoài phiếu; có sự kiện, không ghép được phiếu → nghi đổ ngoài luồng; không có sự kiện, phiếu đã bơm → nghi bơm sang chỗ khác hoặc cảm biến hỏng, báo quản lý cây dầu; không có sự kiện, phiếu chưa bơm → bình thường.

Đề xuất xử lý vòi bơm tự ngắt (chờ khách): căn cứ tính dầu là số iGAS; chờ cảm biến ổn định rồi đọc; chưa đầy thì nhắc bơm bồi một lần cùng phiếu; vẫn chưa đầy thì chốt theo số iGAS, ghi thiếu x lít, vào bảng kê nghi vấn, không chặn phiếu; một xe lệch lặp lại → nghi cảm biến xe, báo quản lý phương tiện hiệu chỉnh; một vòi lệch với nhiều xe → nghi vòi bơm, báo quản lý cây dầu.

## Câu hỏi mở: ghi ở đâu

| # | Câu | Ghi ở |
|---|---|---|
| 1 | Gọi VETC lúc vào vùng điểm cuối hay kết thúc Lệnh; VETC gửi giao dịch tức thời không (hệ quả mỗi đáp án) | `transport-dispatch` OQ-49 |
| 2 | Tránh trạm chốt theo Lệnh; "trả vào lương" trừ hay cộng | `transport-dispatch` OQ-50 |
| 3 | VETC chưa trả dữ liệu sau lượt lấy lại | `transport-dispatch` OQ-51 |
| 4 | Dịch vụ bản đồ | `vehicle-telematics` OQ-1 |
| 5 | Định mức l/giờ có chưa, ai đặt, dùng chung kẹt xe và nổ máy ngủ | `vehicle-telematics` OQ-12 (chuyển `fuel-allowance`) |
| 6 | Bàn giao dGas4, thu hồi dGas5 | `vehicle-management` OQ-1 |
| 7 | Nhắc lái xe tắt máy | `vehicle-telematics` OQ-5 |
| 8 | Xếp hàng chờ ở cảng, bãi, kho có bù dầu không | `transport-dispatch` OQ-52 |
| 9 | Khung ghép phiếu, dung sai dầu thực đổ, dung sai đầy bình | `vehicle-telematics` OQ-13 (chuyển `fuel-issuing`) |
| 10 | Xe chạy ngoài Lệnh: trường hợp miễn, ngưỡng | `vehicle-management` OQ-3 |
| 11 | Mất tín hiệu GPS: chụp ảnh định vị theo mốc | `transport-dispatch` OQ-54 |
| 12 | Đổi xe giữa chặng | `transport-dispatch` OQ-55 |
| 13 | 2 container 20 feet của 2 Lệnh trên 1 xe | `transport-dispatch` OQ-56 |
| 14 | Vòi bơm tự ngắt | `vehicle-telematics` OQ-14 (chuyển `fuel-issuing`) |
| 15 | Quy mô | `vehicle-telematics` OQ-8 |
| 16 | EUP: gửi tức thời, dữ liệu hút dầu, ngưỡng dùng chung | `vehicle-telematics` OQ-2 |
| 17 | Mục lục VIS thiếu 3.6 | `vehicle-telematics` OQ-11 |
| 18 | Kẹt cứng, tai nạn | `transport-dispatch` OQ-53 |
| 19 | Các ngưỡng | `transport-dispatch` OQ-57 (ngưỡng của Lệnh) · `vehicle-telematics` OQ-4 (ngưỡng còn lại) |
| 20 | VETC gửi tức thời | gộp vào `transport-dispatch` OQ-49 |
| 21 | Km khi ký biên bản mà không có GPS | `vehicle-management` OQ-2 |
| 22 | Dầu chờ nhận khi thu hồi | Đã chốt: tính thưởng vào lương lái xe (`vehicle-management` B5) |
| 23 | Quy chế cho tính tiền vào lương từ dữ liệu GPS | `transport-dispatch` OQ-50 · `vehicle-telematics` OQ-10 |
| 24 | Xe chưa gắn GPS, xe không cảm biến | `vehicle-telematics` OQ-6 |
| 25 | Trạm chưa có trong danh mục, thẻ ETC gắn nhầm, VETC trừ trùng | `vehicle-telematics` OQ-7 |
| 26 | Kỳ: qua nửa đêm, qua tháng, Lệnh theo ngày duyệt | `vehicle-telematics` OQ-9 |
| 27 | Khách xem các rủi ro | `vehicle-telematics` OQ-10 |
| 28 | VETC cung cấp danh mục trạm thu phí | `vehicle-telematics` OQ-3 |

## Review vòng 1 — trả lời 17–19/10/2026

Trang phỏng vấn VIS nhóm Phần 8 (https://claude.ai/artifact/GRtqWJ6Zwc7a3P4MuBoNhr). Áp vào brainstorm ngày 19/10.

| # | Vấn đề | Trả lời | Áp vào |
|---|---|---|---|
| r2 | Lệnh "hết chạy" theo GPS | Đồng ý | `transport-dispatch` I7, I8, I11 |
| r3 | Huỷ Lệnh khi xe đang chạy | Đồng ý | `transport-dispatch` I11, 6.3 |
| r4 | Dầu định mức của Lệnh | Sửa: đọc định mức theo tải ở SRS cũ; xe chưa có định mức thì cảnh báo, cho áp định mức xe cùng loại xe vận hành (tạm hoặc gán luôn); hiện 2 số dầu (cung đường ban đầu, thực tế); chưa hiểu km tìm vỏ âm; tính theo đoạn rỗng, có hàng đúng | `transport-dispatch` I5, I9 · vòng 2 v1–v3 |
| r5 | Lái xe được báo, xem, khiếu nại | Đồng ý; phải phân tích vì sao lái xe khiếu nại và luồng sau khiếu nại để anh đánh giá, rồi mới hỏi khách | `transport-dispatch` I14 · `vehicle-management` V1–V3 · vòng 2 v4 |
| r6 | Lệch dầu thực đổ: lỗi của ai | Đồng ý | `vehicle-telematics` X1, 5.3 |
| r7 | Chốt kỳ, bảng kê lương, vé xe ngoài Lệnh | Sửa: soát ngược từ Lệnh xem case nào lọt tới chốt kỳ rồi mới tính giải pháp | vòng 2 v5 |
| r8 | Thu hồi xe khi còn Lệnh chưa duyệt; thiết bị lỗi lúc bơm đầy | Sửa: thu hồi phải xong việc liên quan, duyệt trước rồi mới thu hồi; ý 2 đồng ý | `vehicle-management` B2, B3, B6 · vòng 2 v6 |
| r9 | Lệnh chờ duyệt quá lâu; hai người cùng duyệt | Đồng ý | `transport-dispatch` I13 |
| r10 | Thiết bị chưa khai; cả đội mất dữ liệu | Đồng ý | `vehicle-telematics` G6, G7 |
| r11 | Trạm đổi giữa chừng; giá vé theo tổ hợp xe; trả tiền mặt tại trạm | Ý 1, 2 đồng ý; ý 3 hỏi lại khách | `transport-dispatch` I7, I10, OQ-58 · `vehicle-telematics` T1 |
| r12 | Một gói hay hai gói nhiên liệu | Tách 2 gói | `saas-core-vs-tenant.md` 3.6 · DEC-195 |
| r13 | Thêm vấn đề (e) hao phí | Thêm | `vehicle-telematics` Mục 2, 10 |
