---
type: brainstorm
feature: invoice-management
status: stale
status_prev: draft
updated: 2026-10-21
links:
  - docs-input/sop/apas-thanh-toan-doi-soat/apas-thanh-toan-doi-soat.md
  - docs-input/sop/delta-3-0-master-plan/delta-3-0-master-plan.md
  - docs-input/sop/quan-ly-quy-thanh-toan/quan-ly-quy-thanh-toan.md
  - docs-input/sop/sop-cung-cap-dich-vu-tong-quat.md
  - docs-input/sop/vis-giam-sat-doi-xe/vis-giam-sat-doi-xe.md
  - docs-input/tich-hop/vis-sim-cong-tac-chuan-bi/vis-sim-cong-tac-chuan-bi.md
  - docs/_product/prd.md
  - docs/_product/tenant-parameters.md
  - docs/service-delivery/brainstorms/service-delivery.md
  - docs/payment-on-behalf/brainstorms/payment-on-behalf.md
  - docs/fund-payments/brainstorms/fund-payments.md
  - docs/cost-catalog/brainstorms/cost-catalog.md
  - docs/debt-management/brainstorms/debt-management.md
  - docs/transport-dispatch/brainstorms/transport-dispatch.md
---

# Hoá đơn đầu vào, đầu ra và kê khai thuế

> Tách khỏi `debt-management` ngày 2026-10-21 (DEC-251). Phỏng vấn ngày 2026-10-14 (phần hóa đơn, đồng bộ kế toán, thuế của SIM, 35 câu chung với `payment-on-behalf`), đối chiếu lại 2026-10-21 theo Phân hệ APAS 17/10. Số OQ-9 tới OQ-11 giữ như bản khung.

## 1. Idea Seed

Hóa đơn đầu vào tự về và tự khớp với tiền đã chi qua ngân hàng; kế toán chỉ xử lý phần máy không khớp được. Hóa đơn đầu ra phát hành từ bảng kê đã chốt bằng một nút. Mỗi khoản chi, mỗi hóa đơn tự sang phần mềm kế toán đủ JobID, nhân viên, mã FT để phần mềm kế toán lập tờ khai thuế. Delta gọi phần này là IIP (hóa đơn đầu vào), SII (phát hành hóa đơn), ATR (kê khai thuế) của APAS.

## 2. Context

Delta trả khoảng **7.000 hóa đơn trả hộ mỗi tháng** (local charges hãng tàu, phí facility, nâng hạ, lưu kho CFS, kho hàng không, vệ sinh, lưu bãi). Hôm nay kế toán khớp hóa đơn với tiền đã chi bằng tay, hạch toán chi tiết tay, theo dõi công nợ tay. Mục tiêu của Delta: bỏ thanh toán trùng, sổ kế toán khớp ngân hàng, dữ liệu thuế sạch trước ngày 15 hằng tháng.

Vì sao lúc này: Delta đã làm việc với MISA (meInvoice, AMIS, eSign) và ngân hàng. Với sản phẩm SaaS, kết nối hóa đơn điện tử và phần mềm kế toán là phần khách thứ hai nào cũng hỏi.

**Chữ nhóm:** giữ chữ của bản nháp SIM 14–15/10 để truy về câu trả lời phỏng vấn. Nhóm A (thanh toán trả hộ) đã sang `payment-on-behalf`.

**Phạm vi:**
- Gồm: (B) hóa đơn đầu vào: nhận, kiểm trùng, khớp với giao dịch ngân hàng, hóa đơn trả bằng tiền cá nhân, hóa đơn vô chủ, kiểm phát sinh VETC cuối kỳ; (C) hóa đơn đầu ra: phát hành, điều chỉnh, thay thế; (D) kết nối và đồng bộ sang phần mềm kế toán; (E) chuẩn bị dữ liệu thuế.
- Ranh giới:
  - `payment-on-behalf`: tạo, duyệt, chi Yêu cầu nợ hóa đơn; lưu cặp mã FT ↔ Yêu cầu thanh toán ↔ JobID (A12); Yêu cầu trả hóa đơn (B1–B3). Feature này dùng cặp mã FT để khớp và báo lại "đã khớp" để giảm dư nợ.
  - `debt-management`: lập, chốt bảng kê (bảng kê đã chốt là đầu vào của Nhóm C); công nợ phải thu, phải trả; nhận sổ phụ để gạch nợ phải thu.
  - `fund-payments`: sổ dư nợ tạm ứng của nhân viên (dư nợ tạm ứng 2), Yêu cầu thanh toán có hóa đơn (Quy trình 5.2), Phiếu chi, Phiếu thu.
  - `service-delivery`: JobID nhận chi phí từ hóa đơn đã duyệt và số hóa đơn đầu ra (trạng thái "Đã xuất hóa đơn"). Kết nối lấy hóa đơn từ cổng hóa đơn điện tử thuộc feature này (DEC-252); `service-delivery` A9 chỉ nhận hóa đơn đã lấy về.
  - `transport-dispatch`: khớp vé VETC từng trạm trên Lệnh (I7), trạng thái "Chờ VETC".
  - `cost-catalog`: nhóm phí, mã phí cấp 2 dùng cho định danh và phân loại.
  - DIS (khối đọc chứng từ dùng chung, chưa có feature): đọc ảnh, PDF, gửi gói dữ liệu hóa đơn sang đây.
- Ngoài phạm vi: lập tờ khai thuế, ký tờ khai, nộp Cục thuế (phần mềm kế toán, ký số từ xa, cổng T-VAN làm); thuế TNCN của lao động chính thức (phần mềm nhân sự đẩy bảng lương sang phần mềm kế toán); phát hành chứng từ khấu trừ TNCN; quét hóa đơn rủi ro theo dữ liệu Cục thuế; đối chiếu sổ cái với tờ khai; lập tờ khai bổ sung (kế toán trưởng duyệt nộp). Cổng khách tự tra hóa đơn: bỏ (phỏng vấn 14/10).
- Ứng dụng: web cho kế toán, CS, cán bộ quản lý; Delta Super App cho lái xe, hiện trường (tải hóa đơn, xem hóa đơn mình tải).

**Doanh thu và chi phí đều có hóa đơn, xử lý ở hai phía:**
- **Chi phí** (Delta trả đối tác) sinh **hóa đơn đầu vào**: đối tác xuất cho Delta, tự về qua cổng hóa đơn điện tử hoặc nhân viên tải lên, rồi khớp với khoản tiền đã chi (Nhóm B).
- **Doanh thu** (khách trả Delta) sinh **hóa đơn đầu ra**: Delta xuất cho khách từ bảng kê đã chốt (Nhóm C). Tiền khách trả về gạch nợ ở `debt-management`.
- **Trả hộ** đi cả hai phía: Delta chi trước cho cảng, hãng tàu (hóa đơn đầu vào, nhóm phí 03), rồi thu lại của khách trên bảng kê.

**Nguồn:** Phân hệ APAS (17/10/2026) mục 2.2.3 (Luồng xử lý Hóa đơn đầu vào), 3.2, 3.3, 3.4, IV, 5.1; Phần mềm Delta 3.0 (16/10/2026) mục 7.2; Quy trình cung cấp dịch vụ tổng quát mục 4.10; SIM & VIS – Công tác chuẩn bị (11/10/2026) mục 1.2, 2.3, 3.2; VIS – Giám sát đội xe mục 3.1.3 Bước 4; phỏng vấn ngày 14/10/2026.

**Nhãn:** [SOP to-be] = tài liệu khách đã yêu cầu · [SOP+] = khách có nêu, đề xuất làm sâu hơn · [Mới] = khách chưa nêu.

## 3. User Types (preliminary)

Phân quyền theo chức năng, không cố định vai trò.

| User Type | Pain Point | Primary Need |
|-----------|-----------|--------------|
| Người tải hóa đơn (CS, hiện trường, lái xe) | Không biết hóa đơn đã ai tải, đã khớp chưa | Tải một lần, thấy hóa đơn mình tải đang ở đâu |
| Kế toán viên | Khớp hóa đơn tay, hạch toán tay | Chỉ xử lý giao dịch máy không tự khớp, hóa đơn vô chủ |
| Kế toán (đầu ra) | Xuất hóa đơn tay trên trang nhà cung cấp | Phát hành từ bảng kê đã chốt, biết hóa đơn nào ký lỗi |
| Cán bộ quản lý, Ban giám đốc | Không thấy hóa đơn trả bằng tiền cá nhân | Duyệt hóa đơn tiền cá nhân có đủ JobID, nhóm phí |
| Kế toán trưởng | Sổ kế toán lệch sổ phụ; thiếu chứng từ khi lập tờ khai | Dữ liệu đã định danh sang phần mềm kế toán trước hạn |

### 3.1 Tác vụ chính

| Vai trò | Tác vụ | Tần suất | Mức quan trọng | Ghi chú |
|---------|--------|----------|----------------|---------|
| Người tải | Tải hóa đơn trên Lệnh, JobID, Yêu cầu thanh toán | Nhiều lần mỗi ngày | cao | Trễ hạn thì trễ dữ liệu thuế |
| Kế toán viên | Khớp gộp, tách; xử lý hàng chờ tra soát | Mỗi ngày | cao | Lệch 1 ₫ cũng vào hàng chờ |
| Kế toán viên | Tra soát hóa đơn vô chủ | Định kỳ | trung | Gán nhầm mã FT thì chi 2 lần |
| Cán bộ quản lý, kế toán, Ban giám đốc | Duyệt hóa đơn tiền cá nhân | Mỗi ngày | trung | Cố ý dài để dồn chi về ngân hàng |
| Kế toán | Phát hành, điều chỉnh, thay thế hóa đơn đầu ra | Mỗi ngày, dồn cuối tháng | cao | Cuối tháng dễ nghẽn ký số |
| Kế toán | Xử lý đồng bộ kế toán lỗi | Khi có lỗi | cao | Để lâu thì trả nhà cung cấp 2 lần |

## 4. Capabilities Breakdown

### P0 — must have

**Nhóm B — Hóa đơn đầu vào (IIP)**
- B1 [SOP to-be] [Lõi] [Cấu hình] Nhận hóa đơn từ 2 nguồn đã chuẩn hóa: tệp XML tự về từ cổng hóa đơn điện tử (kết nối đầu tiên: MISA meInvoice, nhận qua webhook hoặc kéo định kỳ) và gói dữ liệu hóa đơn từ DIS (ảnh, PDF nhân viên, lái xe tải lên; DIS tách mã số thuế người bán, ký hiệu, số hóa đơn, ngày lập, tiền trước thuế, tiền thuế, tổng tiền). Feature này không tự đọc ảnh. App chặn nút "Gửi" khi ảnh mờ, lóa (bộ chặn chất lượng ảnh của DIS). Mỗi hóa đơn tải lên tối đa `P-gioi-han-tep-hoa-don` (Delta: 50 MB, 5 tệp).
- B2 [SOP to-be] [Lõi] Kiểm trùng **trước** khi khớp, theo mã số thuế người bán + ký hiệu + số hóa đơn, so với toàn bộ hóa đơn đã có. Trùng thì từ chối, khóa dùng lại, đưa vào "Hóa đơn từ chối thanh toán"; không xóa.
- B2b [SOP+] [Lõi] Tách 3 trường hợp trùng (Mục 6.5): cùng hóa đơn về từ 2 nguồn (lái xe tải ảnh, sau đó XML tự về) thì **gộp**, giữ XML làm bản gốc, ảnh làm đính kèm, không từ chối; hai người cùng tải thì bản sau trỏ về bản đầu, báo người sau; hóa đơn đã dùng thanh toán hoặc đang chờ duyệt ở yêu cầu khác thì **từ chối** như B2. Nguồn chỉ ghi "trùng thì từ chối" (OQ-9).
- B3 [SOP+] [Lõi] Hóa đơn tải tay gắn ngay vào Lệnh, JobID hoặc Yêu cầu thanh toán đang mở (lái xe tải trên Lệnh, nối qua Yêu cầu thanh toán của Lệnh đó; đã chốt khi phỏng vấn), để máy khớp có thêm manh mối ngoài số tiền và ngày.
- B4 [SOP to-be] [Lõi] Mỗi hóa đơn mang **định danh hai lớp**: lớp 1 pháp lý (số hóa đơn, ký hiệu, mã số thuế người bán, ngày lập, tổng tiền); lớp 2 nội bộ (mã nhân viên lập Yêu cầu thanh toán, mã phí cấp 2 theo `cost-catalog`, JobID sẽ hạch toán). Thiếu lớp 2 thì chưa được đồng bộ sang phần mềm kế toán.
- B5 [SOP to-be] [Lõi] [Cấu hình] Tự khớp 1-1 với giao dịch thực chi (mã FT từ `payment-on-behalf`) khi đủ 3 điều kiện: tổng tiền hóa đơn bằng đúng số tiền chi; mã số thuế hoặc tên người bán trùng tài khoản nhận, tra qua **Bảng ánh xạ** mã số thuế/tên trên hóa đơn ↔ tên tài khoản ngân hàng thường dùng của đối tác (cho trường hợp tên không trùng 100% do chứng từ scan); ngày lập và ngày giao dịch lệch không quá `P-lech-ngay-khop-hoa-don` (Delta: 3 ngày). Ai lập, sửa Bảng ánh xạ: OQ-6.
- B6 [SOP to-be] [Lõi] [Cấu hình] Khớp cấu trúc phức tạp, tổng phải bằng đúng, không có sai số:
  - Gộp N-1 (nhiều giao dịch, 1 hóa đơn tổng của cảng, nhà cung cấp): kế toán chọn nhiều mã FT chưa đối soát; chỉ mở nút "Duyệt đối soát" khi tổng bằng đúng hóa đơn.
  - Tách 1-N (1 lệnh chuyển gộp, đối tác xuất nhiều hóa đơn theo JobID): máy gợi ý các tổ hợp hóa đơn của cùng nhà cung cấp có tổng bằng đúng số tiền chi; kế toán duyệt tổ hợp, mã FT gắn vào mọi hóa đơn trong tổ hợp. Chỉ khớp toàn phần, không có "Khớp một phần" (bản 12/10 có, bản 17/10 bỏ).
  - Lệch dù một đồng: cấm tự duyệt, cấm làm tròn; giao dịch vào **Hàng chờ tra soát** trong `P-han-tra-soat-giao-dich` (Delta: 24 giờ) cho kế toán xử lý tay; quá hạn thì cảnh báo kế toán, đưa lên đầu danh sách. Không tự tạo phiếu chi hoàn tiền khi quá hạn: `P-tu-hoan-tien-qua-han` (Delta: tắt; APAS 17/10 đã bỏ câu tự hoàn ở mục IIP, sơ đồ thuế 3.4.1 còn ghi, OQ-2).
- B7 [SOP to-be] [Lõi] Trường hợp 1 — khớp được mã FT: hóa đơn kế thừa mã nhân viên và JobID từ giao dịch, chuyển "Đã khớp" (đóng, khóa dùng lại), đưa lên JobID; báo khớp để sổ ở `fund-payments` ghi giảm dư nợ tạm ứng 2 của người tạo từng mã FT đúng bằng số tiền của mã FT đó (khớp gộp nhiều người thì giảm cho từng người; nhân viên không phải lập Yêu cầu trả hóa đơn, `payment-on-behalf` B3); đồng bộ sang phần mềm kế toán (D2).
- B8 [SOP to-be] [Lõi] [Cấu hình] Trường hợp 2 — hóa đơn nhân viên tải mà không tìm thấy giao dịch (nhân viên trả bằng tiền cá nhân): hóa đơn vào **Danh mục hóa đơn chờ thanh toán** trên mã nhân viên của người tải, chỉ người đó thấy, ẩn khỏi màn chung. Nhân viên kê JobID và nhóm phí (nhóm phí bắt buộc khi là JobID nghiệp vụ), gửi duyệt theo `P-cap-duyet-hoa-don-tien-ca-nhan` (Delta: 3 bước Cán bộ quản lý → Kế toán → Ban giám đốc; nguồn ghi cố ý dài để dồn khoản chi về ngân hàng). Duyệt xong:
  - JobID kế toán: phần mềm tự tạo Yêu cầu thanh toán có hóa đơn, chuyển Quy trình 5.2 ở `fund-payments` để chi ngay; hóa đơn đồng bộ sang phần mềm kế toán.
  - JobID nghiệp vụ: hóa đơn chuyển vào JobID đó, thanh toán từ JobID theo quy trình đã có.
  - SOP quỹ 06/10 mục 5.2 ghi duyệt 2 bước (OQ-10). Chi trả cho người tải hay người đã chi (OQ-8).
- B9 [SOP+] [Lõi] [Cấu hình] Chặn chi 2 lần: trước khi đưa hóa đơn vào Danh mục chờ thanh toán (B8), tìm giao dịch cùng nhân viên, cùng số tiền trong `P-cua-so-nghi-khop` (Delta: 7 ngày). Có thì kế toán chọn "Khớp với giao dịch" hoặc "Xác nhận chi cá nhân" rồi mới đi tiếp.
- B10 [SOP to-be] [Lõi] Trường hợp 3 — hóa đơn vô chủ (chỉ hóa đơn tự về từ cổng hóa đơn điện tử, không tìm thấy giao dịch), chia 2 nhóm:
  - Nhóm 1, lỗi đối soát (sai cú pháp, thiếu JobID, chuyển gộp lệch cấu trúc): kế toán tra soát (gợi ý giao dịch: B10b). Kế toán gán mã FT thì phần mềm định danh lớp 2 theo mã FT, chuyển hóa đơn về Danh mục chờ thanh toán của nhân viên đã chi qua ngân hàng để nhân viên lập Yêu cầu trả hóa đơn (`payment-on-behalf` B1). Chênh lệch tiền chi và trị giá hóa đơn: kế toán ghi đối ứng tay.
  - Nhóm 2, xuất nhầm mã số thuế hoặc giao dịch chưa định nghĩa: kế toán rà định kỳ, chọn **Từ chối** (loại khỏi báo cáo thuế, chuyển "Hóa đơn không rõ nguồn gốc") hoặc **Chấp nhận** kèm lý do (phần mềm tự tạo Yêu cầu thanh toán có hóa đơn theo JobID kế toán, duyệt theo quy định). Nguồn ghi "Quy trình 5.3" (OQ-3).
- B11 [SOP to-be] [Lõi] Danh mục hóa đơn đầu vào lọc theo trạng thái (Mục 6.3) trên web và app; khu riêng cho kế toán: Hàng chờ tra soát, Hóa đơn vô chủ, Hóa đơn từ chối thanh toán, Hóa đơn không rõ nguồn gốc. Người tải thấy hóa đơn mình tải và Danh mục chờ thanh toán của mình.
- B12 [SOP to-be] [Lõi] Kiểm phát sinh VETC cuối kỳ: khi nhận hóa đơn tổng của đơn vị thu phí, phần mềm quét các giao dịch trên hóa đơn chưa gắn Lệnh nào (**vé mồ côi**), tra lịch sử GPS lúc phát sinh, gợi ý xe, khung giờ, trạm để kế toán duyệt chi phí hợp lý hoặc chuyển xử lý sai phạm của lái xe (chạy ngoài lịch trình, việc riêng); khớp tổng hóa đơn với tổng vé đã ghi trên các Lệnh. Vé từng trạm khớp ngay trên Lệnh ở `transport-dispatch` I7; Lệnh còn trạm "Chờ VETC" chưa duyệt được (`transport-dispatch` OQ-51, khách đã chốt). Hóa đơn tổng VETC có đi qua B1–B7 như hóa đơn thường không, ai duyệt, gắn JobID nào: OQ-7.

**Nhóm C — Hóa đơn đầu ra (SII)**
- C1 [SOP to-be] [Lõi] Kế toán chọn bảng kê doanh thu dịch vụ hoặc doanh thu trả hộ đã chốt với khách, xem trước, bấm phát hành; phần mềm gửi dữ liệu người mua theo mã khách hàng và bảng kê sang cổng hóa đơn điện tử (kết nối đầu tiên: MISA meInvoice) để ký số từ xa và lấy mã Cục thuế, không nhập tay. Luồng chi tiết chờ khách (OQ-1).
- C2 [SOP to-be] [Lõi] Yêu cầu phát hành, điều chỉnh không gọi thẳng mà vào **Hàng đợi ký số** riêng, để cuối tháng nghẽn không làm treo màn kế toán. Nhận mã Cục thuế, PDF, XML; lưu, gửi khách qua email và link tra cứu. Cổng hóa đơn điện tử tự đồng bộ hóa đơn sang phần mềm kế toán.
- C3 [SOP to-be] [Lõi] Điều chỉnh hoặc thay thế: kế toán chọn hóa đơn sai, chọn "Điều chỉnh" hoặc "Thay thế", nhập lý do, chọn bảng kê mới. Phần mềm chỉ mở nút phát hành hóa đơn mới khi **Thông báo sai sót (Mẫu 04/SS-HĐĐT)** đã ký số và gửi Cục thuế thành công. Hóa đơn cũ sang "Bị thay thế" hoặc "Bị điều chỉnh", liên kết tới hóa đơn mới.
- C4 [SOP to-be] [Lõi] [Cấu hình] Lỗi kết nối hoặc hết thời gian chờ khi ký số: tự thử lại theo `P-ky-so-thu-lai` (Delta: sau 1, 5, 15 phút, tối đa 5 lần, OQ-11); vẫn lỗi thì "Ký số lỗi" và cảnh báo kế toán, kế toán bấm thử lại. Trước mỗi lần thử lại, hỏi trạng thái hóa đơn ở cổng hóa đơn điện tử để không phát hành 2 lần khi lần trước hết thời gian chờ mà Cục thuế đã cấp mã. Cục thuế quá tải cũng thử lại như lỗi kết nối. Cục thuế từ chối cấp mã vì sai dữ liệu (mã số thuế người mua, thuế suất): không thử lại, "Bị từ chối cấp mã", tạo việc cho kế toán sửa bảng kê (user chốt 14/10).

**Nhóm D — Kết nối và đồng bộ kế toán**
- D1 [SOP+] [Lõi] Lớp kết nối dùng chung cho hóa đơn điện tử, phần mềm kế toán, ngân hàng (phần nhận sổ phụ, dùng chung bộ nối ngân hàng của `payment-on-behalf` A16). Mỗi nhà cung cấp là một bộ nối thay được; MISA meInvoice, MISA AMIS là bộ nối đầu tiên.
- D2 [SOP to-be] [Lõi] [Cấu hình] Đồng bộ ngược sang phần mềm kế toán ngay khi có kết quả chi thành công kèm mã FT: lập chứng từ chi tiền (ủy nhiệm chi), khớp hóa đơn đầu vào với chứng từ đó khi hóa đơn đã khớp (B7), đổi công nợ nhà cung cấp sang "Đã thanh toán"; mã FT (mọi mã FT khi khớp gộp N-1) ghi vào trường "Số chứng từ gốc". Lỗi kết nối: dữ liệu vào hàng chờ cô lập, tự gửi lại theo `P-dong-bo-ke-toan-thu-lai` (Delta: mỗi 15 phút, tới khi thông); lỗi dữ liệu (mã nhà cung cấp chưa có, tài khoản kế toán chưa ánh xạ) hoặc còn tồn gần hạn `P-han-day-du-lieu-ke-toan` thì tạo việc cho kế toán. Dư nợ tạm ứng 2 không đồng bộ sang phần mềm kế toán (tài khoản trung gian, SOP quỹ mục 4.3.1). Chứng từ chi lúc "Đã chi" khi hóa đơn chưa về ghi nhận thế nào: OQ-17.
- D4 [SOP+] [Lõi] Sổ phụ chỉ nhận ở một nơi: phần mềm mình nhận sổ phụ từ ngân hàng (vì chỉ ở đây nối được mã FT với JobID, nhân viên, hóa đơn); phần mềm kế toán nhận chứng từ đã định danh từ mình (D2), không tự kéo sổ phụ, để một giao dịch không thành 2 chứng từ. Khách có đang bật kết nối ngân hàng trong phần mềm kế toán không: OQ-5.

**Nhóm E — Chuẩn bị dữ liệu thuế**
- E1 [SOP to-be] [Lõi] [Cấu hình] Đẩy hóa đơn đã định danh (định danh 2 lớp, mã FT) sang phần mềm kế toán trước `P-han-day-du-lieu-ke-toan` (Delta: ngày 15 hằng tháng). Mỗi hóa đơn mang mã nhóm thuế theo `P-nhom-phi` (Delta: đầu ra DT02 doanh thu dịch vụ và doanh thu xuất lại phí trả hộ; đầu vào CP01 quản lý chung, CP02 hàng bán, CP03 trả hộ, CP04 tài sản cố định và đầu tư, CP05 khác). Phân loại lần 2 theo APAS phụ lục 5.1: nhóm 03 và phần nhóm 02 xuất lại cho khách theo JobID nghiệp vụ; phần còn lại của nhóm 02 và nhóm 01, 04, 05 theo JobID kế toán. Hóa đơn trả hộ bắt buộc có JobID để phần mềm kế toán lập phụ lục bảng kê mua vào theo JobID. Mã CP0n có trùng nhóm phí 0n không: OQ-12.
- E2 [SOP to-be] [Lõi] [Cấu hình] Nhắc nhân viên, lái xe còn hóa đơn chưa tải trước `P-han-tai-hoa-don` (Delta: ngày 12 hằng tháng); nhắc sớm `P-nhac-truoc-han-tai-hoa-don` (Delta: 3 ngày, khách đổi được).
- E4 [SOP to-be] [Lõi] Hóa đơn CP04 (xe đầu kéo, container, kho bãi) có cờ "Dự án đầu tư mới" để phần mềm kế toán tách sang tờ khai 02/GTGT riêng. Ai gắn cờ, lúc nào: OQ-13.
- E5 [SOP to-be] [Lõi] [Cấu hình] Chi cho cá nhân không ký hợp đồng lao động (thù lao, mua dịch vụ cá nhân): người nhận trong danh mục đối tác có cờ "Cá nhân – khấu trừ TNCN"; khoản chi từ `P-nguong-khau-tru-tncn` (Delta: 2.000.000 ₫/lần) trở lên phải khấu trừ `P-ty-le-khau-tru-tncn` (Delta: 10%). Ai khấu trừ, ai gắn cờ: OQ-14.

### P1 — should have

- B10b [SOP to-be] [Lõi] Khi kế toán tra soát hóa đơn vô chủ, phần mềm gợi ý giao dịch có số tiền tương đương.
- E3 [SOP to-be] [Lõi] Gắn cờ "Thuế nhà thầu" cho hóa đơn thương mại (commercial invoice) của đại lý nước ngoài (nhóm CP05) theo quốc gia của đối tác trong danh mục, trước khi đồng bộ sang phần mềm kế toán. Đề xuất: phần mềm không tính số thuế, kế toán tính trên phần mềm kế toán; APAS 3.4.2.3 ghi phần mềm tự tính (OQ-4).
- D3 [Mới] [Lõi] Bảng đối chiếu cuối ngày: giao dịch có mã FT mà phần mềm kế toán chưa có chứng từ; mục tiêu cuối ngày bằng 0.

### P2 — nice to have

Chưa có.

## 5. Core Flows (Happy Path)

### 5.1 Hóa đơn đầu vào: nhận, kiểm trùng, khớp

1. Hóa đơn về: XML tự về từ cổng hóa đơn điện tử, hoặc người tải chụp, tải trên Lệnh, JobID, Yêu cầu thanh toán (DIS đọc, gửi gói dữ liệu).
2. (PM) Kiểm trùng (B2, B2b): gộp, trỏ về bản đầu, hoặc từ chối.
3. (PM) Tìm giao dịch khớp 1-1 (B5). Khớp: Trường hợp 1 (B7).
4. Không tự khớp nhưng có giao dịch gần: [Kế toán viên] khớp gộp hoặc tách (B6); lệch tiền vào Hàng chờ tra soát.
5. Không có giao dịch: hóa đơn nhân viên tải → Trường hợp 2 (5.2); hóa đơn tự về → Trường hợp 3, vô chủ (5.3).

```
XML tự về ─┐
           ├─► (PM) <Trùng?> ─Cùng hóa đơn 2 nguồn─► gộp, giữ XML
DIS (ảnh) ─┘        │        ─2 người tải─────────► trỏ về bản đầu
                    │        ─Đã dùng─────────────► Từ chối thanh toán
                    ▼Không
              <Khớp 1-1 mã FT?> ─Có─► TH1: Đã khớp · JobID · giảm dư nợ tạm ứng 2
                    │Không                · đồng bộ kế toán
              <Có giao dịch gần?> ─Có─► [Kế toán viên] gộp N-1 / tách 1-N
                    │Không                   │lệch tiền ─► Hàng chờ tra soát
                    ▼
              <Nguồn?> ─Nhân viên tải─► TH2: Danh mục chờ thanh toán (5.2)
                       ─Tự về────────► TH3: Hóa đơn vô chủ (5.3)
```

### 5.2 Hóa đơn trả bằng tiền cá nhân (Trường hợp 2)

1. (PM) Tìm giao dịch nghi khớp (B9); có thì [Kế toán viên] chọn "Khớp với giao dịch" hoặc "Xác nhận chi cá nhân".
2. (PM) Hóa đơn vào Danh mục chờ thanh toán trên mã nhân viên của người tải.
3. [Người tải] Kê JobID, nhóm phí, gửi duyệt.
4. [Cán bộ quản lý] → [Kế toán] → [Ban giám đốc] duyệt.
5. (PM) JobID kế toán: tạo Yêu cầu thanh toán có hóa đơn sang `fund-payments` Quy trình 5.2. JobID nghiệp vụ: chuyển hóa đơn vào JobID.

### 5.3 Hóa đơn vô chủ (Trường hợp 3)

1. (PM) Hóa đơn tự về không tìm thấy giao dịch: vào "Hóa đơn vô chủ", gợi ý giao dịch có số tiền tương đương.
2. Nhóm 1: [Kế toán viên] gán mã FT → (PM) định danh lớp 2, chuyển về Danh mục chờ thanh toán của nhân viên đã chi → [Nhân viên] lập Yêu cầu trả hóa đơn (`payment-on-behalf`).
3. Nhóm 2: [Kế toán viên] Từ chối (sang "Không rõ nguồn gốc", loại khỏi báo cáo thuế) hoặc Chấp nhận kèm lý do → (PM) tạo Yêu cầu thanh toán có hóa đơn theo JobID kế toán.

### 5.4 Hóa đơn đầu ra từ bảng kê

1. [Kế toán] Chọn bảng kê đã chốt với khách, xem trước hóa đơn, bấm phát hành.
2. (PM) Đưa vào Hàng đợi ký số; hóa đơn "Chờ ký".
3. (Cổng hóa đơn điện tử) Ký số, lấy mã Cục thuế, trả mã + PDF + XML.
4. (PM) "Đã cấp mã", gửi khách qua email và link tra cứu; "Đã gửi khách".
5. Sai: [Kế toán] chọn Điều chỉnh hoặc Thay thế, nhập lý do, chọn bảng kê mới → (PM) gửi Thông báo sai sót 04/SS-HĐĐT, chờ ký và gửi thành công → lặp bước 2–4; hóa đơn cũ đổi trạng thái.

```
[Kế toán] bảng kê đã chốt ─► phát hành ─► (PM) Hàng đợi ký số ─► Chờ ký
                                                     │
                     <Ký số, cấp mã?> ─Lỗi kết nối─► thử lại P-ky-so-thu-lai ─hết lượt─► Ký số lỗi
                             │         ─Cục thuế từ chối─► Bị từ chối cấp mã ─► việc cho kế toán
                             ▼Có
                     Đã cấp mã ─► Đã gửi khách
                                      │sai
[Kế toán] Điều chỉnh/Thay thế ─► (PM) 04/SS-HĐĐT ký + gửi thành công? ─Có─► phát hành hóa đơn mới
                                                                         └► cũ: Bị thay thế / Bị điều chỉnh
```

### 5.5 Kiểm phát sinh VETC cuối kỳ

1. (PM) Nhận hóa đơn tổng của đơn vị thu phí cuối kỳ.
2. (PM) Quét vé mồ côi, tra GPS, gợi ý xe, giờ, trạm (B12); khớp tổng hóa đơn với tổng vé trên Lệnh.
3. [Kế toán] Duyệt chi phí hợp lý, hoặc chuyển xử lý sai phạm của lái xe.

## 6. System Behavior Deep Dive

### 6.1 Decision Points

| ID | Flow | Khi nào | YES | NO |
|---|---|---|---|---|
| D1 | 5.1 | Trùng mã số thuế người bán + ký hiệu + số hóa đơn? | Gộp / trỏ về / từ chối (B2b) | Tìm giao dịch |
| D2 | 5.1 | Khớp 1-1 đủ 3 điều kiện (B5)? | Trường hợp 1 | Tìm giao dịch gần |
| D3 | 5.1 | Tổng gộp, tách bằng đúng (sai số 0 ₫)? | Mở nút "Duyệt đối soát" | Hàng chờ tra soát |
| D4 | 5.1 | Hóa đơn do nhân viên tải? | Trường hợp 2 | Trường hợp 3, vô chủ |
| D5 | 5.2 | Có giao dịch nghi khớp trong `P-cua-so-nghi-khop`? | Kế toán chọn | Vào Danh mục chờ thanh toán |
| D6 | 5.2 | JobID kế toán? | Yêu cầu thanh toán có hóa đơn (`fund-payments`) | Chuyển vào JobID nghiệp vụ |
| D7 | 5.3 | Kế toán tìm được mã FT? | Nhóm 1: gán FT | Nhóm 2: từ chối / chấp nhận |
| D8 | 5.4 | Ký số thành công? | Đã cấp mã | Lỗi kết nối: thử lại, hết lượt thì Ký số lỗi · Cục thuế từ chối: Bị từ chối cấp mã |
| D9 | 5.4 | Thông báo 04/SS-HĐĐT đã ký và gửi thành công? | Mở phát hành hóa đơn mới | Chặn |

### 6.2 Scenario Matrix — hóa đơn và giao dịch

| Tình huống | Phần mềm làm gì | Nguồn / phụ thuộc |
|---|---|---|
| 1 hóa đơn, 1 lệnh chi đúng tiền | Tự khớp 1-1 | B5 |
| Hóa đơn tổng của cảng = tổng nhiều lệnh chi lẻ | Kế toán chọn gộp N-1 | B6 |
| 1 lệnh chuyển gộp cho hãng tàu, hãng xuất nhiều hóa đơn theo JobID | Máy gợi ý tổ hợp, kế toán duyệt | B6 |
| Tổng lệch 1 ₫ | Hàng chờ tra soát, không làm tròn | B6 |
| Tên người bán trên ảnh scan sai chính tả | Tra Bảng ánh xạ | B5, OQ-6 |
| Nhân viên trả tiền túi, tải hóa đơn | Trường hợp 2, duyệt 3 bước | B8 |
| Nhân viên trả tiền túi nhưng thật ra đã có lệnh chi cùng số tiền | Chặn, kế toán chọn | B9 |
| Hóa đơn tự về, chưa ai tải, không thấy giao dịch | Vô chủ | B10 |
| Đối tác xuất nhầm mã số thuế Delta | Vô chủ nhóm 2 | B10 |
| Hóa đơn tự về trùng ảnh lái xe đã tải | Gộp, giữ XML | B2b |

### 6.3 State Transitions

```
Hóa đơn đầu vào: Mới → Đã khớp ─► Đã đồng bộ kế toán
                   ↘ Từ chối thanh toán (trùng)
                   ↘ Chờ thanh toán (mã nhân viên) → Chờ duyệt → Đã duyệt → (JobID kế toán) Đã tạo Yêu cầu thanh toán
                                                                         → (JobID nghiệp vụ) Đã chuyển JobID
                   ↘ Vô chủ → (gán FT) Chờ thanh toán (mã nhân viên)
                          → Không rõ nguồn gốc
                          → (chấp nhận) Đã tạo Yêu cầu thanh toán
Giao dịch ngân hàng: Chờ đối soát → Đã khớp
                          ↘ Chờ tra soát (lệch tiền) → Đã khớp (kế toán xử lý)
Hóa đơn đầu ra: Chờ phát hành → Chờ ký → Đã cấp mã → Đã gửi khách → Bị thay thế / Bị điều chỉnh
                         ↘ Ký số lỗi → ([Kế toán] thử lại) Chờ ký
                         ↘ Bị từ chối cấp mã → ([Kế toán] sửa bảng kê) Chờ phát hành
Đồng bộ kế toán: Chờ đồng bộ → Đã đồng bộ
                     ↘ Lỗi kết nối (tự gửi lại) → Đã đồng bộ
                     ↘ Lỗi dữ liệu → ([Kế toán] sửa) Chờ đồng bộ
```

| Entity | Từ | Sang | Trigger | Quay lại được? |
|--------|------|----|---------|-------------|
| Hóa đơn đầu vào | Mới | Đã khớp | Khớp 1-1, gộp, tách | có (kế toán gỡ khớp, ghi lý do) |
| Hóa đơn đầu vào | Mới | Từ chối thanh toán | Trùng, đã dùng | không (không xóa) |
| Hóa đơn đầu vào | Mới | Chờ thanh toán | Nhân viên tải, không có giao dịch | có (khớp khi giao dịch về) |
| Hóa đơn đầu vào | Mới | Vô chủ | Tự về, không có giao dịch | có (kế toán gán FT) |
| Hóa đơn đầu vào | Chờ duyệt | Đã duyệt | Ban giám đốc duyệt bước 3 | không |
| Giao dịch | Chờ đối soát | Chờ tra soát | Gộp, tách lệch tiền | có |
| Hóa đơn đầu ra | Chờ ký | Ký số lỗi | Hết lượt thử khi lỗi kết nối | có |
| Hóa đơn đầu ra | Chờ ký | Bị từ chối cấp mã | Cục thuế từ chối vì sai dữ liệu | có (sửa bảng kê) |
| Hóa đơn đầu ra | Đã gửi khách | Bị thay thế / Bị điều chỉnh | Hóa đơn mới đã cấp mã | không |
| Đồng bộ kế toán | Chờ đồng bộ | Lỗi dữ liệu | Mã nhà cung cấp, tài khoản chưa có | có |

### 6.4 Interrupted Transactions

| Tình huống | Hệ thống còn lại gì | Resume | Cleanup |
|---|---|---|---|
| App mất mạng khi tải hóa đơn | Nháp trên máy | Tự gửi khi có mạng | — |
| Cổng hóa đơn điện tử ngừng | Hóa đơn đầu ra "Chờ ký"; đầu vào chỉ còn nguồn tải tay | Tự gửi lại; XML về sau thì gộp với bản tải tay (B2b) | — |
| Phần mềm kế toán ngừng | "Chờ đồng bộ" trong hàng chờ cô lập | Tự gửi lại theo `P-dong-bo-ke-toan-thu-lai` | Bảng đối chiếu cuối ngày (D3) |
| Đồng bộ lỗi dữ liệu | "Lỗi dữ liệu" | Việc cho kế toán | — |
| Máy tự khớp và kế toán khớp tay cùng giao dịch | Bản đầu thắng | Người sau thấy "Giao dịch vừa được khớp", tải lại | — |
| Hai kế toán cùng khớp một giao dịch | Bản đầu thắng | Như trên | — |
| Hai người duyệt cùng hóa đơn tiền cá nhân | Lần duyệt đầu | Người sau thấy đã duyệt | — |
| Cuối tháng nghẽn ký số | Hàng đợi ký số | Thử lại theo `P-ky-so-thu-lai` | Ký số lỗi, kế toán thử lại |

### 6.5 Other Edge Cases

**Hóa đơn trùng xảy ra khi nào** (B2b, user đồng ý 14/10):
1. Cùng hóa đơn về từ 2 nguồn: lái xe tải ảnh, sau đó XML tự về. Không phải lỗi: gộp, giữ XML làm bản gốc, ảnh làm đính kèm.
2. Hai người cùng tải: CS và lái xe cùng tải hóa đơn của một khoản. Bản sau trỏ về bản đầu, báo người sau.
3. Dùng một hóa đơn hai lần: hóa đơn đã khớp lại được đưa vào yêu cầu khác (nhầm hoặc gian lận). Từ chối, vào "Hóa đơn từ chối thanh toán"; không xóa.

**Đồng bộ kế toán lỗi thì hậu quả là gì, ai xử lý** (phỏng vấn 14/10):
- Hậu quả nếu để lâu: phần mềm kế toán vẫn ghi công nợ nhà cung cấp "chưa thanh toán" nên có thể trả lần hai; số dư tiền gửi trên sổ lệch sổ phụ; tờ khai GTGT tháng thiếu chứng từ thanh toán không dùng tiền mặt nên có thể mất khấu trừ thuế đầu vào.
- Ai xử lý: lỗi kết nối tạm thời do hệ thống tự gửi lại. Lỗi dữ liệu và lỗi còn tồn gần hạn đẩy dữ liệu thì kế toán.

**Sổ phụ ngân hàng 2 nơi giữ** (D4): sổ phụ gốc do ngân hàng giữ. Phần mềm kế toán cũng có thể tự kéo sổ phụ nếu bật kết nối ngân hàng; đề xuất không bật để một giao dịch không thành 2 chứng từ (OQ-5).

**Thuế nhà thầu để làm gì** (E3): khi Delta trả đại lý nước ngoài không có cơ sở tại Việt Nam, Delta phải khấu trừ và nộp thay thuế nhà thầu (tờ khai 01/NTNN). Đại lý gửi commercial invoice, không phải hóa đơn điện tử Việt Nam, nên không tự về và dễ bị bỏ sót. Cờ giúp phần mềm kế toán gom đủ các khoản lên tờ khai tháng. Tỷ lệ phụ thuộc loại dịch vụ và hiệp định thuế (nguồn: thường 2% TNDN, 5% GTGT hoặc miễn với vận tải quốc tế).

## 7. Validation, Limits & Wording

### 7.1 Validation rules

| Field | Rule |
|---|---|
| Tệp hóa đơn | Ảnh, PDF hoặc XML; tối đa theo `P-gioi-han-tep-hoa-don`; ảnh mờ thì app chặn gửi |
| JobID (Trường hợp 2) | Bắt buộc khi gửi duyệt |
| Nhóm phí (Trường hợp 2) | Bắt buộc khi JobID nghiệp vụ; chọn từ danh mục `cost-catalog` |
| Hóa đơn nhóm trả hộ | Bắt buộc có JobID trước khi đồng bộ kế toán |
| Gộp N-1, tách 1-N | Tổng bằng đúng, sai số 0 ₫ |
| Lý do chấp nhận hóa đơn vô chủ nhóm 2 | Bắt buộc |
| Lý do điều chỉnh, thay thế hóa đơn đầu ra | Bắt buộc |

### 7.2 Limits & Quotas (exact values)

| Tham số | Giá trị | Window | Behavior khi vượt |
|---|---|---|---|
| `P-gioi-han-tep-hoa-don` | Delta: 50 MB, 5 tệp | Mỗi hóa đơn | Chặn tải |
| `P-lech-ngay-khop-hoa-don` | Delta: 3 ngày | Mỗi lần khớp | Không tự khớp |
| `P-han-tra-soat-giao-dich` | Delta: 24 giờ | Từ lúc vào Hàng chờ tra soát | Cảnh báo kế toán |
| `P-tu-hoan-tien-qua-han` | Delta: tắt | — | — |
| `P-cap-duyet-hoa-don-tien-ca-nhan` | Delta: 3 bước (Cán bộ quản lý → Kế toán → Ban giám đốc) | Mỗi hóa đơn | — |
| `P-cua-so-nghi-khop` | Delta: 7 ngày | Lúc vào Trường hợp 2 | Kế toán chọn |
| `P-ky-so-thu-lai` | Delta: 1, 5, 15 phút; tối đa 5 lần | Mỗi hóa đơn đầu ra | Ký số lỗi |
| `P-dong-bo-ke-toan-thu-lai` | Delta: mỗi 15 phút, tới khi thông | Mỗi dữ liệu đồng bộ | — |
| `P-han-tai-hoa-don` | Delta: ngày 12 hằng tháng | Tháng | Nhắc |
| `P-nhac-truoc-han-tai-hoa-don` | Delta: 3 ngày | Tháng | — |
| `P-han-day-du-lieu-ke-toan` | Delta: ngày 15 hằng tháng | Tháng | Cảnh báo kế toán |
| `P-nguong-khau-tru-tncn` | Delta: 2.000.000 ₫/lần | Mỗi khoản chi cho cá nhân | Gắn khấu trừ TNCN |
| `P-ty-le-khau-tru-tncn` | Delta: 10% | Mỗi khoản chi cho cá nhân | — |

### 7.3 Wording samples (exact strings)

#### Error messages

| Tình huống | Wording | Code |
|---|---|---|
| Hóa đơn đã dùng | "Hóa đơn {ký hiệu} {số} đã có trong hệ thống (JobID {mã}). Không tải lại." | E-? |
| Gộp, tách lệch tiền | "Tổng {n} giao dịch là {tổng}, lệch {chênh} so với hóa đơn. Chọn lại." | E-? |
| Chưa gửi được thông báo sai sót | "Chưa gửi được Thông báo sai sót 04/SS-HĐĐT. Chưa phát hành được hóa đơn mới." | E-? |
| Ảnh mờ | "Ảnh mờ hoặc lóa. Chụp lại rõ hơn." | E-? |
| Tệp quá lớn | "Dung lượng file tối đa {P-gioi-han-tep-hoa-don} MB." | E-? |
| Tệp sai định dạng | "File không đúng định dạng." | E-common-006 |
| Lỗi hệ thống | "Đã xảy ra lỗi. Thử lại sau." | E-common-008 |
| Mất mạng | "Mất kết nối. Kiểm tra mạng và thử lại." | E-common-009 |

E-common-007 đang ghi 250 MB; tệp hóa đơn dùng giới hạn riêng nên cần câu riêng (dòng "Tệp quá lớn").

#### Success messages

| Tình huống | Wording |
|---|---|
| Khớp hóa đơn | "Đã khớp hóa đơn với giao dịch {mã FT}." |
| Phát hành hóa đơn | "Đã phát hành hóa đơn {ký hiệu} {số}, mã Cục thuế {mã}." |
| Duyệt hóa đơn tiền cá nhân | "Đã duyệt hóa đơn {số} của {tên}." |

#### Info / neutral messages

| Tình huống | Wording |
|---|---|
| Vào Danh mục chờ thanh toán | "Chưa tìm thấy khoản chi cho hóa đơn này. Kê JobID và nhóm phí để gửi duyệt." |
| Vô chủ | "Hóa đơn chưa tìm thấy giao dịch, đang ở Hóa đơn vô chủ." |
| Chờ tra soát quá hạn | "Giao dịch chờ tra soát quá {P-han-tra-soat-giao-dich} giờ." |
| Đang ký số | "Hóa đơn đang chờ ký số (lần thử {n}/{tối đa})." |
| Nhắc tải hóa đơn | "Còn {n} hóa đơn chưa tải. Hạn ngày {P-han-tai-hoa-don}." |

### 7.4 Bối cảnh hệ thống (mức nghiệp vụ)

**Thông tin cần lưu:** hóa đơn đầu vào (định danh 2 lớp, tiền trước thuế, thuế, tổng, tệp gốc, nguồn, nhóm phí, mã nhóm thuế, cờ thuế nhà thầu, cờ dự án đầu tư mới, giá trị máy đọc và giá trị người sửa) · liên kết hóa đơn ↔ mã FT (1-1, N-1, 1-N) · Bảng ánh xạ mã số thuế/tên ↔ tài khoản đối tác · hóa đơn đầu ra (bảng kê, mã Cục thuế, PDF, XML, thông báo sai sót, liên kết thay thế, điều chỉnh) · nhật ký đồng bộ kế toán.

**Dịch vụ ngoài:**

| Dịch vụ | Mục đích | Ghi chú |
|---|---|---|
| MISA meInvoice | Phát hành hóa đơn đầu ra; gom hóa đơn đầu vào (XML) | Bộ nối đầu tiên; webhook hoặc kéo định kỳ |
| MISA eSign Cloud | Ký số hóa đơn từ xa | Qua meInvoice, gói doanh nghiệp |
| MISA AMIS | Phần mềm kế toán: chứng từ chi, công nợ, tờ khai | Bộ nối đầu tiên |
| Ngân hàng | Sổ phụ, biến động số dư | Dùng chung bộ nối với `payment-on-behalf`; gạch nợ ở `debt-management` |
| DIS | Đọc ảnh, PDF hóa đơn | Khối dùng chung, chưa có feature |

**Thông báo:** trong app và thông báo đẩy cho mọi việc; email cho khách (hóa đơn) và cho kế toán khi cảnh báo nặng (Ký số lỗi, đồng bộ lỗi gần hạn, chờ tra soát quá hạn).

**Việc chạy nền:** gom hóa đơn đầu vào mới · thử khớp lại hóa đơn chưa khớp khi có giao dịch mới · nhắc tải hóa đơn trước hạn · báo kế toán hóa đơn chưa định danh trước hạn đẩy dữ liệu · thử lại ký số, đồng bộ kế toán · bảng đối chiếu cuối ngày · kiểm phát sinh VETC cuối kỳ.

**Dùng chung:**

| Nhóm | Feature chung | Feature này cần | Trạng thái |
|---|---|---|---|
| Liên quy trình | `cross-process-flow` | Khớp FT → giảm dư nợ tạm ứng 2 (`fund-payments`, `payment-on-behalf`); hóa đơn tiền cá nhân → Yêu cầu thanh toán 5.2 (`fund-payments`) hoặc vào JobID (`service-delivery`); vé mồ côi → xử lý sai phạm lái xe | đề xuất |
| Thông báo | (chưa có feature) | Vào Danh mục chờ thanh toán, chờ duyệt, Ký số lỗi, Bị từ chối cấp mã, đồng bộ lỗi, nhắc tải hóa đơn | đề xuất |
| Lịch sử hoạt động | (chưa có feature) | Khớp, gỡ khớp, gán FT, từ chối, chấp nhận vô chủ, duyệt, phát hành, điều chỉnh, thay thế | đề xuất |
| Thao tác chung | `common-workspace` | Tải tệp, lưu nháp trên máy khi mất mạng | đề xuất |
| Quyền + danh mục | `access-control`, `organization`, `cost-catalog` | Quyền khớp, tra soát, duyệt 3 bước, phát hành; danh mục đối tác (quốc gia, cờ cá nhân); nhóm phí, mã phí cấp 2 | đề xuất |

## 8. Assumptions

- Cổng hóa đơn điện tử gom được đủ hóa đơn đầu vào của Delta (OQ-23 của `service-delivery`).
- Ngân hàng trả sổ phụ theo thời gian thực kèm mã FT.
- Pháp nhân thứ ba là Delta Vận tải (phỏng vấn 14/10; VIS-SIM ghi Delta Hải Phòng), cần khách xác nhận văn bản.
- Bảng kê do phần bảng kê, công nợ của feature này lập và chốt (chưa phỏng vấn); Nhóm C chỉ nhận bảng kê đã chốt với khách.
- 95% là quy tắc cứng; AI chỉ đọc ảnh ở DIS (SIM & VIS – Công tác chuẩn bị mục 1.2).

## 9. Risks

| Rủi ro | Khả năng | Hậu quả nghiệp vụ | Cách phòng |
|--------|----------|-------------------|-----------|
| Chi 2 lần cho một hóa đơn (gán nhầm mã FT, nhân viên kê tiền cá nhân cho khoản đã chi qua ngân hàng) | thỉnh thoảng | Mất tiền, kế toán mất lòng tin | Kiểm trùng trước khớp (B2); chặn nghi khớp (B9); lệch 1 ₫ không tự duyệt (B6) |
| Đồng bộ kế toán tồn đọng cuối tháng | thường | Trả nhà cung cấp 2 lần, mất khấu trừ thuế | Tự gửi lại; bảng đối chiếu cuối ngày (D3) |
| Nghẽn ký số cuối tháng | thường | Hóa đơn đầu ra trễ | Hàng đợi ký số, thử lại (C2, C4) |
| Nhân viên, lái xe không tải hóa đơn đúng hạn | thường | Kế toán vẫn làm tay, trễ hạn thuế | Nhắc tự động (E2) |
| Khách SaaS khác dùng nhà cung cấp hóa đơn, phần mềm kế toán khác | thường | Không bán được | Lớp kết nối thay được (D1) |

## 10. Success Criteria (preliminary)

- % hóa đơn đầu vào tự khớp, không cần kế toán khớp tay.
- Số giao dịch có mã FT mà phần mềm kế toán chưa có chứng từ, cuối mỗi ngày: mục tiêu 0.
- Số lần chi 2 lần cho một hóa đơn: mục tiêu 0.
- % hóa đơn tải trước hạn hằng tháng.
- Thời gian từ bảng kê chốt tới "Đã cấp mã"; tỷ lệ "Ký số lỗi".

Hiện trạng và mục tiêu số: chưa có (OQ-16).

## 11. Open Questions

| ID | Câu hỏi | Nguồn khách | Trạng thái |
|---|---|---|---|
| OQ-1 | Luồng xuất hóa đơn đầu ra: ai lập yêu cầu (CS hay kế toán); 1 hóa đơn cho cả bảng kê hay có khách tách theo JobID; bảng kê lập ở đâu? Quy trình cung cấp dịch vụ ghi hóa đơn ở Quy trình 5.4, APAS ghi 5.2 | Phân hệ APAS (17/10/2026), mục 3.2.3; Quy trình cung cấp dịch vụ tổng quát, mục 4.10 | Còn mở |
| OQ-2 | Mục IIP đã bỏ câu tự tạo phiếu chi hoàn tiền sau 24 giờ, sơ đồ thuế vẫn ghi "Xử lý hóa đơn vô chủ: Tạo Phiếu chi hoàn tiền". Xác nhận: không tự hoàn, chỉ cảnh báo? | Phân hệ APAS (17/10/2026), mục 3.3.2 Bước 3, 3.4.1 | Đã có hướng: không tự hoàn (user 14/10), cần khách xác nhận |
| OQ-3 | Chấp nhận hóa đơn vô chủ nhóm 2: nguồn ghi tạo "Yêu cầu thanh toán có hóa đơn (Quy trình 5.3)", nhưng SOP quỹ đánh 5.2 là có hóa đơn, 5.3 là không hóa đơn. Ý là quy trình nào? | Phân hệ APAS (17/10/2026), mục 3.3.3; Quy trình quản lý quỹ & Thanh toán (06/10/2026), mục 5.2, 5.3 | Còn mở, BL-214 |
| OQ-4 | Thuế nhà thầu: APAS ghi phần mềm tự tính 2% TNDN, 5% GTGT. Đề xuất chỉ gắn cờ, kế toán tính trên phần mềm kế toán. Chi cho đại lý nước ngoài (ngoại tệ) đi qua luồng ngân hàng của `payment-on-behalf` không; "phân hệ quản lý dịch vụ forwarding" là phần nào? | Phân hệ APAS (17/10/2026), mục 3.4.2.3 | Còn mở |
| OQ-5 | Delta có đang bật kết nối ngân hàng trong phần mềm kế toán MISA AMIS không? Đề xuất không bật để không trùng chứng từ | Chưa có trong tài liệu khách gửi | Còn mở |
| OQ-6 | Bảng ánh xạ mã số thuế/tên ↔ tài khoản đối tác: ai lập, ai sửa; có tự thêm dòng mỗi lần kế toán khớp tay không? | Phân hệ APAS (17/10/2026), mục 3.3.2 Bước 3 | Còn mở |
| OQ-7 | Điểm giao dữ liệu xe (VIS) ↔ hóa đơn (SIM): (1) hóa đơn tổng VETC cuối kỳ có đi qua nhận, khớp hóa đơn đầu vào như hóa đơn thường không, ai duyệt, gắn JobID nào; (2) hóa đơn dầu mua ngoài lái xe tải lên có đối chiếu với sự kiện đổ dầu từ cảm biến không; (3) chi phí đã duyệt trên Lệnh (vé, dầu bù, km tìm vỏ) có sang đây để ghép hóa đơn theo JobID không. Cùng câu với `transport-dispatch` OQ-47 | VIS – Giám sát đội xe, mục 3.1.3 Bước 4, 3.2; SIM & VIS – Công tác chuẩn bị (11/10/2026), mục 2.2 | Còn mở, BL-120, BL-164 |
| OQ-8 | Hóa đơn tiền cá nhân: chi trả cho người tải hóa đơn hay người đã chi? Khi CS tải hộ hóa đơn lái xe đã trả, ai nhận tiền? JobID nghiệp vụ "thanh toán từ JobID theo quy trình đã có" là quy trình nào? | Phân hệ APAS (17/10/2026), mục 3.3.4 Bước 2 | Còn mở |
| OQ-9 | Hóa đơn trùng: cùng hóa đơn về từ 2 nguồn (ảnh lái xe tải, sau đó XML tự về) thì gộp giữ XML thay vì từ chối; hai người cùng tải thì trỏ về bản đầu. Delta đồng ý? | Phân hệ APAS (17/10/2026), mục 3.3.2 Bước 2 | Còn mở |
| OQ-10 | Hóa đơn trả bằng tiền cá nhân duyệt 3 cấp (APAS) hay 2 bước (SOP quỹ mục 5.2: Cán bộ quản lý → Ban giám đốc)? Áp cho riêng hóa đơn tiền cá nhân hay cả thanh toán có hóa đơn? Duyệt 3 cấp xong lại sang Quy trình 5.2 (có duyệt riêng) thì có duyệt 2 lần không? | Phân hệ APAS (17/10/2026), mục 3.3.2 Bước 4, 3.3.4; Quy trình quản lý quỹ & Thanh toán (06/10/2026), mục 5.2 | Còn mở (nguồn lệch) |
| OQ-11 | Ký số thử lại sau 1, 5, 15 phút nhưng tối đa 5 lần: lần 4, 5 cách bao lâu? | Phân hệ APAS (17/10/2026), mục 4.2 | Còn mở |
| OQ-12 | Mã nhóm thuế CP01–CP05, DT02 có trùng nhóm phí 01–05 của phụ lục 5.1 không? DT01 và các mã DT khác là gì? SOP quỹ mục 4.4.2 có thêm nhóm công cụ dụng cụ, phụ lục 5.1 không có: xếp vào nhóm nào? | Phân hệ APAS (17/10/2026), mục 3.4.2.1, 5.1 | Còn mở |
| OQ-13 | Hóa đơn CP04: ai gắn cờ "Dự án đầu tư mới", lúc tải hóa đơn hay kế toán gắn sau? | Phân hệ APAS (17/10/2026), mục 3.4.2.1 | Còn mở |
| OQ-14 | Chi cho cá nhân không ký hợp đồng lao động từ ngưỡng: phần mềm chuyển thiếu số khấu trừ khi lập lệnh chi, hay chuyển đủ và phần mềm kế toán khấu trừ khi lập phiếu chi (APAS ghi kế toán lập phiếu chi thì tự khấu trừ)? Ai gắn cờ "cá nhân" cho người nhận? | Phân hệ APAS (17/10/2026), mục 3.4.2.2 | Còn mở |
| OQ-15 | Kết quả nộp tờ khai (thông báo tiếp nhận sau 15 phút, chấp nhận sau 1–2 ngày) chỉ lưu trên phần mềm kế toán hay cũng hiện trên phần mềm cho lãnh đạo xem? | Phân hệ APAS (17/10/2026), mục 3.4.3 Bước 3 | Còn mở |
| OQ-16 | Số hiện trạng: số hóa đơn đầu vào, đầu ra mỗi tháng ngoài trả hộ; % kế toán đang khớp tay | Chưa có trong tài liệu khách gửi | Còn mở |
| OQ-17 | Lúc khoản nợ hóa đơn "Đã chi" mà hóa đơn chưa về: chứng từ chi tiền sang phần mềm kế toán ghi nhận vào tài khoản nào, khi hóa đơn về thì khớp lại thế nào? (Dư nợ tạm ứng 2 không sang phần mềm kế toán) | Phân hệ APAS (17/10/2026), mục 4.3; Quy trình quản lý quỹ & Thanh toán (06/10/2026), mục 4.3.1 | Còn mở |

## 12. Next Steps

- Gửi Delta OQ-1 tới OQ-17 (gộp OQ-7 với `transport-dispatch` OQ-47 khi hỏi).
- Còn phải đọc, đối chiếu: Quy trình quản lý quỹ & Thanh toán, Đính kèm 01 (AI01, bản 20/06, đã được DIS + IIP thay); Phần mềm Delta 3.0 mục 2.1.2 (quy tắc chia sẻ dữ liệu với phần mềm kế toán).
- `/user-flow invoice-management`, rồi `/srs invoice-management`.
