# Sổ đối chiếu: Tích hợp hệ thống VIS & SIM — Công tác chuẩn bị (SRC-24)

> Nguồn: `tich-hop/vis-sim-cong-tac-chuan-bi/vis-sim-cong-tac-chuan-bi.md`
> Bản: 11/10/2026 (nhận 2026-10-12)

Dòng ➡ `payment-on-behalf` / ➡ `debt-management` = phần của brainstorm SIM đang chạy (chưa ghi file,
chia feature sau). Brainstorm ghi file → đổi sang ✅ kèm đường dẫn + mã B/OQ; chia feature → đổi ➡ theo
slug mới.

| Mục | Kết quả | Ở đâu | Ghi chú |
|---|---|---|---|
| 1.1 Dự án bao gồm hai phân hệ chính | ➖ | | giới thiệu VIS/SIM |
| 1.2 Định vị vai trò kỹ thuật | ⬜ | | AI01 = OCR mục "Ghi chú/Nội dung" hóa đơn — lệch SRC-07 2.2 (AI01 = tạo JobID); câu hỏi trong BL-048 |
| II. Khối lượng công việc phát triển | ➖ | | ước tính nhân sự, không phải yêu cầu |
| 2.1 Trục nền tảng trung tâm & API gateway | ➖ | | kiến trúc kỹ thuật (Message Queue, mTLS, Signing Queue, retry), việc của SRS/dev |
| 2.2 Phân hệ VIS - Quản lý đội xe | ✅ | `docs/vehicle-telematics/brainstorms/vehicle-telematics.md` S2–S8; `docs/transport-dispatch/brainstorms/transport-dispatch.md` I3, I5, I6 | đối soát dầu thực đổ với phiếu cấp dầu ➡ `fuel-issuing` (BL-152) |
| 2.3 Phân hệ SIM — Engine Quét & Đọc Hóa Đơn (AI01) | ⬜ | | XML Parser + ghép 1-1 hóa đơn ↔ giao dịch bank (tiền, nhà cung cấp, ngày lập ±3 ngày); thuộc IIP (SRC-07 3.3) |
| 2.3 Phân hệ SIM — Trục Tích hợp Kết nối Ngân hàng (API Banking) | ➡ payment-on-behalf | | lệnh chi outbound MB/TPBank/VCB, webhook sổ phụ inbound |
| 2.3 Phân hệ SIM — Tích hợp Open API MISA meInvoice & AMIS | ➡ debt-management | | ký số Cloud HSM, đồng bộ ngược tạo chứng từ chi |
| 2.3 Phân hệ SIM — Giao diện ứng dụng | ⬜ | | tải ảnh QR, danh mục hóa đơn theo trạng thái, Hóa đơn vô chủ |
| III. Làm việc với đối tác | ➖ | | giới thiệu mục |
| 3.1 Ngân hàng (MB, VCB, TPBank) | ➡ payment-on-behalf | | 1 gói API cho 3 pháp nhân HN/HCM/Hải Phòng (BL-048 hỏi còn giữ không); lưu vết mã FT ↔ JobID; báo giá VCB, Auto-topup |
| 3.2 MISA (meInvoice, AMIS, eSign Cloud) | ➡ debt-management | | Open API meInvoice, eSign Cloud, webhook/pull hóa đơn đầu vào, đồng bộ ngược AMIS ghi mã FT vào số chứng từ gốc |
| 3.3 Giám sát hành trình EUP | ✅ | `docs/vehicle-telematics/brainstorms/vehicle-telematics.md` K1, OQ-2, OQ-4 | |
| 3.4 Thu phí tự động VETC | ✅ | `docs/transport-dispatch/brainstorms/transport-dispatch.md` I7, OQ-49; `docs/vehicle-telematics/brainstorms/vehicle-telematics.md` K2 | tài khoản mẹ Delta VT + Delta HCM (mục 3.1 ghi HN/HCM/Hải Phòng, BL-048); cấu hình ở ngân hàng, ngoài phần mềm |
