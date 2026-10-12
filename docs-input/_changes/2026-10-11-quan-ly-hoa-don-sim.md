# Thay đổi: SOLUTIONS FOR INVOICE MANAGEMENT (SIM) — thay "Hóa đơn trả hộ"

> Bản cũ: nhận 2026-10-02 (`hoa-don-tra-ho-2026-10-01` — "Hóa đơn trả hộ", docx ngày 01/10/2026; bản gốc không lưu) · Bản mới: nhận 2026-10-11 (`SIM_Oct 10 2026.pdf`, ngày 10/10/2026) · Tài liệu: [quan-ly-hoa-don-sim.md](../sop/quan-ly-hoa-don-sim/quan-ly-hoa-don-sim.md)

## Tóm tắt nghiệp vụ

- **Phạm vi mở rộng từ 1 luồng thành cả hệ thống quản lý hóa đơn (SIM).** Toàn bộ "Hóa đơn trả hộ" cũ nay là **mục 3.1** (Trích xuất mã QR động & tĩnh để thanh toán), nội dung gần như giữ nguyên. Tài liệu đổi tên thư mục `sop/hoa-don-tra-ho-2026-10-01/` → `sop/quan-ly-hoa-don-sim/`.
- **Mới — AI01 quản lý hóa đơn đầu vào (mục 2.1):** nhân viên upload hoặc nhận từ Misa API gateway → AI01 quét trích thông tin định danh → Delta MIS kiểm trùng → vào danh mục (2 trạng thái: Chưa làm thanh toán / Đã làm thanh toán) → thông báo cho người upload. Yêu cầu thanh toán **phải lấy hóa đơn từ danh mục AI01**, không upload trực tiếp như hiện nay. Phân loại 2 bước (nhóm phí → JobID) theo phụ lục 5.1.
- **Mới — API Banking (mục 2.2):** 4 bước UNC (gửi YCTT → xác thực OTP → chuyển tiền → trả UNC) + sổ phụ điện tử dùng để lập báo cáo công nợ và **duyệt/từ chối JobID** (cảnh báo thanh toán của khách ngay khi tạo JobID). Lưu đồ 6 bước có "Duyệt tối cao" của chủ tài khoản/đồng chủ tài khoản trên môi trường ngân hàng. Triển khai trước cho chi phí trả hộ theo JobID (Quy trình 5.4), sau mở rộng sang nhà cung cấp; bắt buộc chuyển tiền về ngân hàng đầu tiên kết nối.
- **Mới — yêu cầu mở rộng:** đưa định danh lô hàng/khách lên nội dung UNC; phân công đồng chủ tài khoản duyệt theo **Mã phí** với hạn mức khác nhau; 1 gói API cho **3 pháp nhân** (Delta HN, Delta HCM, Delta Vận tải/Hải Phòng).
- **Mới — phát hành/điều chỉnh hóa đơn đầu ra qua Misa meInvoice (mục 3.2):** từ Bảng kê doanh thu dịch vụ / Doanh thu trả hộ, gửi theo **mã DK05**, ký bằng MISA eSign Cloud, cấp mã Cục thuế, đồng bộ MISA AMIS; luồng Thay thế / Điều chỉnh đổi trạng thái hóa đơn gốc thành "Bị thay thế"/"Bị điều chỉnh".
- **Mới — tự khớp hóa đơn đầu vào với giao dịch ngân hàng (mục 3.3):** khớp 1-1 khi tổng tiền = số tiền thực chi, MST/tên NCC ≈ tài khoản nhận, ngày lập trong ±3 ngày; kế thừa Mã nhân viên + JobID, tự ghi giảm **"Dư nợ tạm ứng 2"**. Kiểm trùng theo MST người bán + Ký hiệu + Số hóa đơn. Không khớp → danh mục **"Hóa đơn vô chủ"**, thêm bước duyệt của Kế toán tổng hợp.
- **Mới — rủi ro vận hành (mục IV):** hàng đợi ký số + thử lại 1/5/15 phút, sau 5 lần lỗi → trạng thái "Ký số lỗi" báo Kế toán; đồng bộ ngược sang MISA AMIS khi nhận webhook thành công, mã FT ghi vào Số chứng từ gốc.
- **Mới — phụ lục:** bảng phân loại hóa đơn theo nhóm phí (mã 01–05) và bảng chi phí API Banking của MB Bank, TP Bank, Techcombank (Vietcombank chờ báo giá). ⚠ Bảng phí có **Techcombank** nhưng mục 3.1 vẫn chỉ nêu 3 ngân hàng MB Bank, Vietcombank, TPBank — cần hỏi khách ngân hàng nào nằm trong phạm vi.
- **Sửa trong phần cũ (mục 3.1):**
  - Pháp nhân thứ ba: "Delta Hải Phòng" → "Delta Vận tải" (mục 2.2.2.2 ghi "Delta Vận tải/Hải Phòng").
  - Dữ liệu giải mã QR: "số tài khoản cảng" → "số tài khoản đối tác".
  - Thứ tự trên sơ đồ kiến trúc: "Quét mã QR … và tạo Yêu cầu thanh toán" → "**Tạo Yêu cầu thanh toán rồi** quét mã QR …" (tạo yêu cầu trước, quét sau — khớp Bước 1).
  - Bỏ câu "Delta cũng sẽ không thể đứng ngoài xu hướng chung."
- ⚠ Các chỗ bản gốc tự đánh dấu chưa xong, cần hỏi lại khách: "Định nghĩa đầy đủ về thông tin định danh của hóa đơn" (2.1.4.2), "Sẽ định nghĩa chi tiết các tiêu chí phân loại" (2.1.4.4), "Sẽ định nghĩa chi tiết sau" (2.1.4.5), "Mô tả chi tiết" bước xác thực OTP (2.2.1.1), "Cần lập danh mục" định danh khách hàng (2.2.1.2); mục 2.1.4.3 trỏ tới "Bước 2.1.4.6" không tồn tại; mục 4.1 chỉ có 1 câu.

## Tài liệu đang dùng nguồn này

- `docs/dispatch-coordination/brainstorms/dispatch-coordination.md` — chỉ trong `links:`; brainstorm loại "Thanh toán trả hộ" khỏi phạm vi Điều phối (dòng 45) → không đổi nghiệp vụ, nhưng phần mới về AI01 (YCTT lấy hóa đơn từ danh mục, nhiệm vụ thu hóa đơn GTGT giao người gần lái xe nhất) có thể chạm bàn giao dữ liệu JobID.
- `docs/meetings/decks/2026-10-06-oq-dispatch-coordination-deck.md` — `links:` + ghi chú nguồn OQ-17 (7.000 HĐ trả hộ/tháng, nay ở mục 3.1) và OQ-32 (UNC qua API MB/VCB/TPBank, nay ở mục 3.1 và 2.2).
- `docs/_shared/logistics-primer.html` — dòng nguồn mục trả hộ.

## Chi tiết

`diff.py` không ghép được mục vì bản cũ (chuyển từ docx) không có số mục — so theo câu giữa bản cũ và mục 3.1 bản mới:

| Bản cũ | Bản mới (mục 3.1) |
|---|---|
| Tiêu đề "HÓA ĐƠN TRẢ HỘ — Thanh toán bằng mã QR động, tĩnh và thông tin tài khoản qua API banking" | "3.1. Trích xuất mã QR động & tĩnh để thanh toán" |
| "Delta cũng sẽ không thể đứng ngoài xu hướng chung." | (bỏ) |
| Sơ đồ: "App / Web — Quét mã QR động hoặc nhập thông tin tài khoản của đối tác và tạo Yêu cầu thanh toán" | "App / Web — Tạo Yêu cầu thanh toán rồi quét mã QR động hoặc nhập thông tin tài khoản của đối tác" |
| "(Delta HN, Delta HCM, Delta Hải Phòng)" | "(Delta HN, Delta HCM, Delta Vận tải)" |
| "gồm số tài khoản cảng, tên ngân hàng hưởng, số tiền, nội dung" | "gồm số tài khoản đối tác, tên ngân hàng hưởng, số tiền, nội dung" |

Các câu còn lại của mục 3.1 trùng nguyên văn bản cũ. Mục I, II, 3.2, 3.3, IV, V hoàn toàn mới.
