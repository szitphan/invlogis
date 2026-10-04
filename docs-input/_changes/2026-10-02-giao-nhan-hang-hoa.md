# Thay đổi: Giao nhận hàng hóa (thay SOP Giao nhận container)

> Bản cũ: nhận 2026-10-01 (`sop/sop-giao-nhan-container.md`, tài liệu ngày 21/8/2026, chuyển tay, không còn bản gốc Word) · Bản mới: nhận 2026-10-02 (`Giao nhận hàng hóa_Sep 18 2026.docx`, tài liệu ngày 18/9/2026) · Tài liệu: [giao-nhan-hang-hoa.md](../sop/giao-nhan-hang-hoa/giao-nhan-hang-hoa.md)

## Tóm tắt nghiệp vụ

- **Phạm vi mở rộng từ container sang mọi loại hàng, toàn quốc.** Tên đổi "Giao nhận container" thành "Giao nhận hàng hóa — Quy trình vận tải thực tế tại Delta". Bản cũ chỉ nói container tại Hải Phòng, HCM; bản mới có 5 loại hàng: container (2.2, 3.1), hàng lẻ CFS/LCL (2.3, 3.2), hàng không (2.4, 3.3), hàng CBT xuyên biên giới (2.5, 3.4), hàng đường sắt Ratraco (2.6, 3.5), cộng mục IV Danh mục. Phần container chỉ là ~1/5 tài liệu mới.
- **Khái niệm chung mới (2.1):** Lệnh giao hàng D/O/eDO, vận đơn MB/L–HB/L, "lệnh nối" (hàng qua NVOCC cần 2 lệnh), 3 cách cấp lệnh hàng air nhập ở Nội Bài (lệnh giấy / eDO cấp cho khách / eDO gửi thẳng kho) — yêu cầu quy trình phải phủ cả 3. Thêm nguyên tắc chung về thanh toán chi phí (local charges + phí cảng/bãi/cửa khẩu, do nhân viên nghiệp vụ hoặc lái xe trả theo "Quy trình quản ký quỹ và thanh toán").
- **Container — điều kiện Lệnh nâng container hàng nhập: 3 → 4 điều kiện.** Thêm "vượt qua đánh giá HSE của cảng (giấy phép vận chuyển hàng DG, hóa chất, quá khổ quá tải…)"; giải thích "thanh lý" = cho phép đưa hàng khỏi khu vực giám sát hải quan.
- **Container — Lệnh hạ container rỗng:** điều kiện "email nơi hạ vỏ của hãng tàu" mở rộng thành "email … **hoặc một văn bản chỉ định nơi hạ vỏ**".
- **Container — Biên bản giao hàng với khách:** thêm yêu cầu **ảnh chụp 4 mặt container khi đến và khi rời nhà máy**.
- **Container — 2 tình huống bất thường mới (3.1.4):** (1) khách giao Booking Note n container nhưng chỉ thuê Delta n-1 container (thường khi khách chỉ dùng vận tải + thanh lý tờ khai xuất tại cảng); (2) hãng tàu không đủ vỏ đạt chuẩn — lái xe có thể phải quay lại bãi lần 2 (đã hoặc chưa trả phí nâng vỏ), khách chọn 1 trong 3 cách: chốt số container đã chọn / đổi Booking Note / chờ chọn đủ vỏ (đổi ưu tiên, đổi bãi nhận vỏ).
- ⚠ **4 quy trình "cần bổ sung theo ý kiến của Trasas" — chưa có nội dung:** đóng/rút hàng tại cảng sang xe tải nhỏ và ngược lại; đảo chuyển vỏ tại depot tư nhân; reused container; cược container hàng nhập. Cần hỏi khách khi nào có mô tả, và Trasas là bên nào (lần đầu xuất hiện trong nguồn).
- ⚠ **Ghi chú "Cái này không cần." đã bị bỏ**, nhưng câu "Cần lập và duy trì bảng số ngày miễn phí DEM và DET theo từng hãng tàu…" vẫn giữ nguyên. Báo cáo `container-deadline-alerts` đang để câu hỏi mở đúng chỗ này — bản mới nghiêng về **giữ yêu cầu**, nhưng nên hỏi khách xác nhận.
- **Container — Thanh toán chi phí (3.1.5):** bỏ đoạn mở đầu liệt kê 3 loại phí (nâng hạ; vệ sinh sửa chữa; lưu container, lưu bãi) và câu "quy trình thanh toán khác nhau giữa các cảng, bãi". Ngưỡng **5 triệu đồng** (dưới: tạm ứng tiền mặt; trên: tạm ứng chuyển khoản/thanh toán nợ) và cách lái xe đổi phiếu thu thành hóa đơn **giữ nguyên**.
- **Bỏ giới hạn địa lý ở depot:** "Một số depot tại Hải Phòng đã ký hợp đồng shipside" → "Một số depot đã ký…".
- **Mẫu chứng từ đính kèm đổi:** bản cũ nhúng 4 mẫu container (Lệnh giao vỏ, phiếu thu nâng vỏ khống, Phiếu eEIR, Cargo Tracking — đã có ở `chung-tu-mau/`, `du-lieu-mau/`); bản mới không nhúng lại 4 mẫu này (chỉ còn câu "chi tiết xe file chèn bên dưới" và "bao gồm Cargo Tracking Details và Phiếu eEIR"), thay vào đó đính kèm 5 file khác: mã vạch hàng nhập air, mã vạch hàng xuất air, biên bản bất thường hàng nhập air, thống kê chi phí CBT, danh mục cảng/bãi/kho/hãng tàu — cả 5 trùng với tài liệu đã có trong docs-input.
- Phần khác của container (Phiếu EIR, cấp chì, VGM, Lệnh cấp container khống, ePort, Lệnh hạ hàng xuất, Lệnh nâng rỗng, 4 mốc SI–CY–DEM–DET và mức cảnh báo 24 giờ / 12 giờ / 2 ngày, 9 tình huống bất thường cũ) **giữ nguyên câu chữ** (chỉ sửa lỗi gõ).

## Đổi số mục

| Mục cũ | Mục mới |
|---|---|
| (mở đầu) Giao nhận container tại Hải Phòng, HCM | I. MỤC TIÊU (mọi loại hàng) + 3.1 (lời dẫn hàng container) |
| 1. Khái niệm chung | 2.2. Hàng container |
| 2. Giao nhận container với cảng bãi | 3.1.1 |
| 3. Giao nhận container với khách hàng | 3.1.2 |
| 4. Giao nhận container với hãng tàu | 3.1.3 |
| 5. Các vấn đề liên quan | 3.1.4 |
| 6. Thanh toán chi phí | 3.1.5 |

## Tài liệu đang dùng nguồn này

- `docs/_research/2026-10-02-container-deadline-alerts.md` — trích "Mục 4" → nay 3.1.3; câu hỏi mở về "Cái này không cần" (bản mới bỏ ghi chú, giữ yêu cầu bảng DEM/DET); có thể bổ sung tình huống hãng tàu thiếu vỏ đạt chuẩn ảnh hưởng mốc CY.
- `docs/_research/2026-10-02-electronic-delivery-record.md` — trích "Mục 3 và Mục 5" → 3.1.2 và 3.1.4; Biên bản giao hàng nay thêm ảnh 4 mặt container; hàng lẻ/air/CBT/đường sắt có yêu cầu biên bản riêng (nhiệt độ hàng lạnh, CD13, chữ ký người nhận Trung Quốc, chứng từ trả về ga Ratraco).
- `docs/_research/2026-10-02-eport-integration.md` — trích "Mục 1–2" → 2.2 và 3.1.1; điều kiện HSE mới cho lệnh nâng hàng nhập; nơi hạ vỏ có thể theo văn bản chỉ định.
- `docs/_research/2026-10-02-field-document-reading.md` — trích "Mục 1, 3, 6" → 2.2, 3.1.2, 3.1.5; thêm nhiều chứng từ hiện trường mới (D/O kho CFS, phiếu xuất kho/nhập kho, tally sheet, mã vạch KVGS, phiếu cân air, biên bản bất thường kho hàng không, ảnh định vị CBT).

## Chi tiết

`diff.py` không ghép được mục vì bản cũ không có heading (chuyển tay, đánh số 1–6 dạng danh sách) và bản mới đổi cả cấu trúc — báo "Thêm mới 56 mục / Bỏ 1 mục" là do cách chuyển, không phải thay đổi thật. Đã so theo câu giữa 6 mục cũ và phần container mới (2.2 + 3.1.1–3.1.5); kết quả ở Tóm tắt nghiệp vụ. Không còn bản gốc Word cũ để chuyển lại bằng `convert.py`.

Các phần chỉ có ở bản mới (không có bản cũ để so): 2.1, 2.3–2.6, 3.2–3.5, IV và 5 đính kèm — đọc trực tiếp trong tài liệu.
