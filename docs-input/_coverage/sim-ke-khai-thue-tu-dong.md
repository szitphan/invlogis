# Sổ đối chiếu: SIM — Lập và nộp báo cáo thuế tự động qua Misa AMIS Online (SRC-25)

> Nguồn: `sop/sim-ke-khai-thue-tu-dong/sim-ke-khai-thue-tu-dong.md`
> Bản: 12/10/2026 (nhận 2026-10-14)

Cả nguồn giao `debt-management` = phần của brainstorm SIM đang chạy (chưa ghi file, chia feature sau).
Brainstorm ghi file → đổi từng dòng ➡ sang ✅ kèm đường dẫn + mã B/OQ; chia feature → đổi ➡ theo slug mới.

| Mục | Kết quả | Ở đâu | Ghi chú |
|---|---|---|---|
| Giải pháp (mở đầu) | ➡ debt-management | | định danh 2 lớp (pháp lý + mã nhân viên/JobID); khớp FT tự gạch nợ; Pending Queue 24h rồi tự tạo phiếu chi hoàn tiền — lệch SRC-07 3.3 (hoàn tiền qua duyệt tay), chờ BL-111 |
| 1. Luồng dữ liệu đối soát & Kết nối thuế toàn diện | ➡ debt-management | | IIP gắn mã DT/CP + mã nhân viên + JobID → background job sang AMIS, đồng bộ ngược; hóa đơn vô chủ → phiếu chi hoàn tiền |
| 2.1 Thuế GTGT - Tờ khai mẫu 01/GTGT | ➡ debt-management | | phần Delta MIS: gắn nhóm mã DT02, CP01–CP04 (đối chiếu SRC-07 5.1 nhóm 02xx/03xx); CP03 trả hộ theo JobID; lập tờ khai do MISA |
| 2.2 Thuế TNCN - Tờ khai mẫu 05/KK-TNCN | ➡ debt-management | | phần lớn MISA AMIS + Delta HR tính; brainstorm chốt ranh giới (khấu trừ 10% khi chi cá nhân ≥2.000.000 ₫/lần) |
| 2.3 Thuế FCT - Tờ khai mẫu 01/NTNN | ➡ debt-management | | cờ thuế nhà thầu theo cấu hình quốc gia, nhóm CP05; chi phí đại lý nước ngoài xử lý ở "phân hệ forwarding" — Feature Map chưa có |
| 3. Quy trình nộp tờ khai thuế tự động lên Cục thuế | ➡ debt-management | | đối chiếu sổ cái, ký số eSign, nộp T-VAN làm trên MISA; brainstorm chốt Delta MIS có hiện trạng thái nộp không |
| 4. Kế hoạch triển khai | ➡ debt-management | | việc chuẩn bị với MISA; hạn chốt: upload hóa đơn + chốt lương trước ngày 12, IIP đẩy AMIS trước ngày 15 → mã tham số P-… |
