# Sổ đối chiếu: Công văn 20260902/CV — Cung cấp dữ liệu chi phí vé cầu đường qua giao thức kết nối API (SRC-09)

> Nguồn: `tich-hop/vetc-api-cong-van-2026-09-02/vetc-api-cong-van-2026-09-02.md`
> Bản: 21/9/2026 (nhận 2026-10-02)

Bản scan không có tiêu đề mục; dòng theo đoạn của công văn và 4 danh mục đính kèm.

| Mục | Kết quả | Ở đâu | Ghi chú |
|---|---|---|---|
| Đầu công văn, kính gửi, lời chào | ➖ | | thủ tục hành chính, không có yêu cầu |
| Đội xe 254 chiếc, 4 tài khoản giao thông (bảng) | ✅ | `docs/vehicle-telematics/brainstorms/vehicle-telematics.md` K4, Mục 8 Assumptions, OQ-8, OQ-19, OQ-21; `docs/_shared/project-profile.md` | 2 pháp nhân: Chi nhánh CP Quốc tế Delta tại HCM (1 tài khoản, 49 xe), TNHH MTV Vận tải Delta (3 tài khoản: 70, 108, 27 xe) — khớp tài khoản mẹ Delta VT + Delta HCM ở Công tác chuẩn bị mục 3.4 |
| Lý do: trên 10.000 lượt vé/tháng, phân bổ chi phí vé vào từng Lệnh để hạch toán | ✅ | `docs/vehicle-telematics/brainstorms/vehicle-telematics.md` Mục 2 vấn đề a, OQ-8, OQ-21; `docs/transport-dispatch/brainstorms/transport-dispatch.md` I7 | khớp vé từng trạm vào Lệnh đã có ở I7 |
| Đề nghị VETC chia sẻ dữ liệu thu phí qua API | ✅ | `docs/vehicle-telematics/brainstorms/vehicle-telematics.md` K2, Mục 9 Risks, OQ-19 | chưa có phản hồi VETC; cách gửi dữ liệu (tức thời hay tra lại) còn ở `transport-dispatch` OQ-49 |
| Đính kèm: 4 danh mục xe (biển số, số eTag, loại phí, trạng thái thẻ, mô tả) | ✅ | `docs/vehicle-management/brainstorms/vehicle-management.md` H3, OQ-5; `docs/vehicle-telematics/brainstorms/vehicle-telematics.md` G8, OQ-20 | 9 thẻ Tạm khóa; cùng số biển 15C-274.30 có 2 thẻ (biển trắng Tạm khóa, biển vàng Đang hoạt động) → ghép theo số thẻ, không theo biển số |
