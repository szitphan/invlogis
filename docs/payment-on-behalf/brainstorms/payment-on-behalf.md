---
type: brainstorm
feature: payment-on-behalf
status: stale
status_prev: draft
updated: 2026-10-21
links:
  - docs-input/sop/apas-thanh-toan-doi-soat/apas-thanh-toan-doi-soat.md
  - docs-input/sop/quan-ly-quy-thanh-toan/quan-ly-quy-thanh-toan.md
  - docs-input/sop/delta-3-0-master-plan/delta-3-0-master-plan.md
  - docs-input/tich-hop/vis-sim-cong-tac-chuan-bi/vis-sim-cong-tac-chuan-bi.md
  - docs/_product/prd.md
  - docs/_product/tenant-parameters.md
  - docs/service-delivery/brainstorms/service-delivery.md
  - docs/debt-management/brainstorms/debt-management.md
  - docs/invoice-management/brainstorms/invoice-management.md
  - docs/fund-payments/brainstorms/fund-payments.md
---

# Thanh toán trả hộ qua ngân hàng

> Phỏng vấn ngày 2026-10-14 (phần thanh toán của SIM, 35 câu chung với `invoice-management`), đối chiếu lại 2026-10-21 theo Phân hệ APAS 17/10 và Quy trình quản lý quỹ & Thanh toán 06/10. Quy trình nợ, trả hóa đơn (A12–A15) lấy từ SOP quỹ, chưa phỏng vấn.

## 1. Idea Seed

Nhân viên hiện trường, CS và lái xe trả phí cảng, bãi, hãng tàu ngay trên JobID hoặc Lệnh vận tải bằng tiền công ty qua ngân hàng: chụp mã QR hoặc chọn đối tác, cán bộ quản lý duyệt, chủ tài khoản bấm OTP trên app ngân hàng. Khoản chi thành dư nợ của người chi cho tới khi hóa đơn về. Không còn ứng tiền túi, không còn kế toán lập lệnh chuyển tiền tay.

## 2. Context

Delta trả khoảng **7.000 hóa đơn trả hộ mỗi tháng** (local charges hãng tàu, phí facility, nâng hạ, lưu kho CFS, kho hàng không, vệ sinh, lưu bãi), khoảng 300 khoản mỗi ngày làm việc. Hôm nay kế toán lập lệnh chuyển tiền tay trên ngân hàng điện tử, nhân viên hiện trường ứng tiền mặt rồi chờ hoàn. Mục tiêu của Delta: bỏ quỹ tiền mặt tạm ứng, bỏ sai sót nhập tay, giảm việc cho nhân viên nghiệp vụ, tuân thủ quy định dùng tiền mặt.

Vì sao lúc này: Delta đã tự đàm phán với ngân hàng (MB Bank, TP Bank đã báo giá; Vietcombank đồng ý cung cấp kết nối, chờ giá). Với sản phẩm SaaS, kết nối ngân hàng là phần khách thứ hai nào cũng hỏi.

**Phạm vi:**
- Gồm: Yêu cầu thanh toán nợ hóa đơn (tạo, đọc QR, duyệt, lập lệnh chi, nhận kết quả ngân hàng), Yêu cầu thanh toán trả hóa đơn (nộp hóa đơn hoặc trả lại tiền để xóa dư nợ), khóa quyền tạo khi quá hạn trả hóa đơn, báo cáo dư nợ nợ hóa đơn.
- Ranh giới:
  - `service-delivery`: nút Yêu cầu thanh toán trên JobID, ghi chi phí lên JobID, việc "Thu hóa đơn GTGT" (E2, E6). Feature này nhận yêu cầu từ JobID và trả trạng thái về.
  - `transport-dispatch`: màn Yêu cầu thanh toán của lái xe trên Lệnh.
  - `invoice-management`: thu và khớp hóa đơn đầu vào với giao dịch ngân hàng, hóa đơn vô chủ, hóa đơn trả bằng tiền cá nhân, đồng bộ sang phần mềm kế toán.
  - `debt-management`: bảng kê nợ phải thu, gạch nợ phải thu từ sổ phụ.
  - `fund-payments`: sổ dư nợ tạm ứng của nhân viên (kể cả dư nợ nợ hóa đơn, gọi là "dư nợ tạm ứng 2"), phiếu thu, phiếu chi, tạm ứng tiền mặt, thanh toán có và không hóa đơn, thanh toán nhà cung cấp.
- Ứng dụng: web cho CS, kế toán, cán bộ quản lý; Delta Super App cho lái xe, hiện trường.

**Nguồn:** Phân hệ APAS (17/10/2026) mục 2.1, 3.1, IV; Quy trình quản lý quỹ & Thanh toán (06/10/2026) mục 4.3, 4.5, 4.6, 5.4, 5.5; Phần mềm Delta 3.0 (16/10/2026) mục 7.1; SIM & VIS – Công tác chuẩn bị (11/10/2026) mục 2.3, 3.1; phỏng vấn ngày 14/10/2026.

**Nhãn:** [SOP to-be] = tài liệu khách đã yêu cầu · [SOP+] = khách có nêu, đề xuất làm sâu hơn · [Mới] = khách chưa nêu.

## 3. User Types (preliminary)

Phân quyền theo chức năng, không cố định vai trò.

| User Type | Pain Point | Primary Need |
|-----------|-----------|--------------|
| Người tạo yêu cầu (CS, hiện trường, lái xe) | Ứng tiền túi, chờ hoàn | Trả đối tác ngay tại chỗ bằng tiền công ty |
| Cán bộ quản lý | Duyệt chi qua tin nhắn, không thấy JobID | Duyệt yêu cầu trong "Việc của tôi", thấy QR còn bao lâu |
| Ban giám đốc, giám đốc chi nhánh | Khoản lớn không qua ai | Duyệt bước 2 khoản vượt giới hạn |
| Chủ tài khoản / đồng chủ tài khoản | Không biết lệnh nào gấp | Duyệt OTP trên app ngân hàng kịp trước khi QR hết hạn |
| Kế toán | Lập lệnh tay; không biết khoản nào chưa có hóa đơn | Duyệt Yêu cầu trả hóa đơn; xem dư nợ nợ hóa đơn từng người |

### 3.1 Tác vụ chính

| Vai trò | Tác vụ | Tần suất | Mức quan trọng | Ghi chú |
|---------|--------|----------|----------------|---------|
| Người tạo | Tạo Yêu cầu thanh toán nợ hóa đơn, tải ảnh QR | Nhiều lần mỗi ca (~300 khoản/ngày toàn Delta) | cao | Chi nhầm người nhận |
| Cán bộ quản lý | Duyệt bước 1 | Nhiều lần mỗi ngày | cao | Chậm thì QR hết hạn |
| Chủ tài khoản | Duyệt OTP trên app ngân hàng | Nhiều lần mỗi ngày | cao | Chậm thì QR hết hạn |
| Người tạo | Tạo Yêu cầu trả hóa đơn | Sau mỗi khoản chi, trong 3 ngày làm việc | trung | Quá hạn thì bị khóa quyền tạo |
| Kế toán | Duyệt Yêu cầu trả hóa đơn | Mỗi ngày | trung | Sai thì hạch toán nhầm JobID |

## 4. Capabilities Breakdown

### P0 — must have

**Nhóm A — Thanh toán nợ hóa đơn (chi trước, hóa đơn về sau)**
- A1 [SOP to-be] [Lõi] [Cấu hình] Tạo Yêu cầu thanh toán nợ hóa đơn từ JobID nghiệp vụ (CS, hiện trường, web hoặc app) hoặc từ Lệnh vận tải (lái xe, app); chi phí trên Lệnh chuyển lên JobID. Không tạo được từ chỗ khác. Lái xe chọn loại phí từ danh sách rút gọn `P-phi-lai-xe-tra-ho` (Delta: phí hạ hàng cho hàng xuất; phí hạ vỏ, vệ sinh, sửa chữa container cho hàng nhập) và tải chứng từ cảng bãi đưa.
- A2 [SOP to-be] [Lõi] Ba cách chọn người nhận: tải ảnh QR động, tải ảnh QR tĩnh, hoặc chọn đối tác từ danh mục (cảng, bãi, hãng tàu, đại lý, kho CFS, kho hàng không). Phần mềm đọc QR lấy tài khoản nhận, ngân hàng, số tiền, nội dung, hiệu lực còn lại; QR tĩnh và chọn từ danh mục thì người tạo nhập số tiền.
- A3 [SOP to-be] [Lõi] [Cấu hình] Lái xe chọn QR tĩnh hoặc chọn từ danh mục: phần mềm lấy vị trí lái xe, gợi ý `P-so-cang-bai-goi-y` (Delta: 3–5) cảng bãi gần nhất trong danh mục để chọn.
- A4 [SOP+] [Lõi] Chọn từ danh mục thì kiểm hai vòng: người tạo xác nhận lại tài khoản hiện từ danh mục, cán bộ quản lý duyệt thấy nhãn "Chọn từ danh mục". Tài khoản mới chưa có trong danh mục: tạo việc "Đăng ký tài khoản đối tác" cho kế toán duyệt trước, không nhập tay số tài khoản trên yêu cầu. Cách hiểu "hai vòng" chờ khách xác nhận (OQ-1).
- A5 [SOP to-be] [Lõi] Nội dung chuyển tiền tự ghép: mã nhân viên, số JobID, số Yêu cầu thanh toán, số vận đơn hoặc booking, tên chi phí, tên khách hàng.
- A6 [SOP to-be] [Lõi] [Cấu hình] Kiểm hiệu lực QR động: còn dưới `P-qr-hieu-luc-toi-thieu` (Delta: 3 phút) thì trả lại người tạo lấy mã mới; hiệu lực gốc dưới `P-qr-hieu-luc-goc-ngan` (Delta: 15 phút) thì cảnh báo ngay khi đọc QR và gợi ý 3 cách: xin đối tác QR tĩnh hoặc số tài khoản, nhờ quản lý duyệt nhanh, hoặc để đồng chủ tài khoản duyệt. Nguồn ghi 2 cách: mục 2.1.4 ghi "chặn đẩy lệnh", mục 3.1.4 cho đi tiếp theo 3 cách trên (OQ-2).
- A8 [SOP to-be] [Lõi] [Cấu hình] Duyệt bước 1: cán bộ quản lý. Trong giới hạn duyệt của người đó `P-han-muc-duyet-chi` (Delta: chưa chốt, OQ-3) và hạn mức duyệt còn lại trên ngân hàng của đồng chủ tài khoản `P-han-muc-dong-chu-tai-khoan` (Delta: cán bộ quản lý nghiệp vụ 15 triệu/lệnh, 50 triệu/ngày; cán bộ quản lý hiện trường 10 triệu/lệnh, 30 triệu/ngày) thì đi thẳng sang ngân hàng; vượt một trong hai thì chuyển duyệt bước 2. Cán bộ quản lý cũng tự chọn chuyển bước 2 được. Từ chối thì trả về người tạo.
- A9 [SOP to-be] [Lõi] Duyệt bước 2: ban giám đốc hoặc giám đốc chi nhánh. Từ chối thì trả về người tạo.
- A10 [SOP to-be] [Lõi] Lập lệnh chi (ủy nhiệm chi, UNC) và gửi ngân hàng từ tài khoản của pháp nhân chi nhánh. Mỗi site đã gắn một chi nhánh, mỗi chi nhánh thuộc một pháp nhân (Mục 8), nên người tạo không chọn pháp nhân. Pháp nhân có tài khoản ở nhiều ngân hàng thì chọn ngân hàng theo cam kết số lượng lệnh chi với từng ngân hàng — quy tắc chờ khách (OQ-4). JobID 2 chi nhánh cùng làm: chi từ pháp nhân nào (OQ-5).
- A11 [SOP to-be] [Lõi] Chủ tài khoản hoặc đồng chủ tài khoản duyệt OTP trên app ngân hàng (MBBank Biz, VCB DigiBiz, TPBank Biz); phần mềm không giữ quyền trích tiền. Ngân hàng trả UNC điện tử kèm mã giao dịch (mã FT): yêu cầu "Đã chi", UNC gắn lên JobID, chi phí ghi lên JobID và Lệnh; ghi tăng dư nợ tạm ứng 2 của người tạo (sổ ở `fund-payments`); tạo việc "Thu hóa đơn GTGT" (E6 của `service-delivery`).
- A12 [SOP to-be] [Lõi] Lưu cặp mã FT ↔ Yêu cầu thanh toán ↔ JobID, vì nội dung QR động không chèn thêm được. `invoice-management` dùng cặp này để khớp hóa đơn đầu vào.

**Nhóm B — Trả hóa đơn và dư nợ nợ hóa đơn**
- B1 [SOP to-be] [Lõi] [Cấu hình] Trong `P-han-tra-hoa-don` (Delta: 3 ngày làm việc kể từ ngày duyệt Yêu cầu nợ hóa đơn) người tạo phải lập Yêu cầu thanh toán trả hóa đơn, tạo thẳng từ Yêu cầu nợ hóa đơn đó để giữ liên kết, chọn 1 trong 2 hoặc cả 2:
  - Trả hóa đơn: chọn một hoặc nhiều hóa đơn trả hộ mình đã tải lên (danh sách lấy từ `invoice-management`). Tổng hóa đơn nhỏ hơn số đã chi thì kê thêm phần trả tiền cho đủ; tổng hóa đơn lớn hơn số đã chi: OQ-17. Dư nợ tạm ứng 2 không được âm.
  - Trả tiền: đối tác hoàn tiền (kê số tiền, tải UNC hoặc báo có của đối tác; kế toán duyệt ở B2) hoặc nhân viên nộp lại (kê số tiền; phần mềm tạo ngay Phiếu thu "Trả lại tiền tạm ứng thanh toán nợ hóa đơn" chuyển thủ quỹ thu theo Quy trình 5.8 ở `fund-payments`, không qua B2).
- B2 [SOP to-be] [Lõi] Kế toán duyệt Yêu cầu trả hóa đơn (bảng phân quyền mục 6.4.1 ghi thêm bước 2 Ban giám đốc, OQ-18): kiểm hóa đơn khớp mã phí trả hộ và JobID, hoặc kiểm tiền đối tác hoàn đã về tài khoản. Duyệt thì ghi giảm dư nợ tạm ứng 2 của người tạo và đưa hóa đơn vào bảng kê nợ phải thu của khách (`debt-management`); từ chối thì trả về người tạo. Nguồn ghi 2 cách ở bước ghi sổ khi duyệt: "ghi tăng nợ phải thu từ khách hàng" (mục 5.5.2) và "ghi tăng nợ phải trả cho mã khách hàng" (mục 5.5.2.5) (OQ-7).
- B3 [SOP+] [Lõi] Hóa đơn mà `invoice-management` đã tự khớp với mã FT của yêu cầu (khớp 1-1 hoặc khớp gộp, tách) thì tự coi là đã trả hóa đơn: `invoice-management` báo khớp, sổ ở `fund-payments` ghi giảm dư nợ tạm ứng 2 của người tạo từng mã FT đúng bằng số tiền của mã FT đó (khớp gộp nhiều người thì giảm cho từng người), người tạo không phải lập Yêu cầu trả hóa đơn. Yêu cầu trả hóa đơn chỉ còn cho phần máy không tự khớp được và cho trường hợp trả tiền. APAS ghi khớp FT thì tự ghi giảm dư nợ; SOP quỹ ghi luôn qua kế toán duyệt (OQ-8).
- B4 [SOP to-be] [Lõi] [Cấu hình] Yêu cầu nợ hóa đơn đã chi mà quá `P-han-tra-hoa-don` chưa trả hóa đơn thì phần mềm tạm dừng quyền tạo Yêu cầu nợ hóa đơn của người đó. Yêu cầu được duyệt trong `P-khoa-cuoi-thang` (Delta: 2 ngày cuối tháng) thì tạm dừng từ ngày làm việc đầu tháng sau; nguồn không ghi "nếu chưa trả hóa đơn", bản nháp thêm điều kiện này (OQ-9). Mở lại quyền khi nào, ai mở: OQ-9.
- B5 [SOP to-be] [Lõi] Dư nợ tạm ứng 2 là tài khoản trung gian, không sang phần mềm kế toán (SOP quỹ mục 4.3.1). Báo cáo dư nợ tạm ứng 2 của từng nhân viên tháng trước, gửi kế toán và nhân sự liên quan ngày đầu tháng.
- B6 [SOP+] [Lõi] Báo cáo B5 tự lọc khoản bất thường để kế toán chỉ làm việc với các khoản đó: quá hạn trả hóa đơn, đã có hóa đơn nhưng lệch tiền, đối tác báo hoàn mà tiền chưa về. Bộ tiêu chí chờ khách (OQ-10).

### P1 — should have

- A7 [SOP+] [Lõi] Đồng hồ đếm ngược hiệu lực QR hiện trên yêu cầu cho người duyệt và chủ tài khoản thấy việc gấp.
- A13 [SOP to-be] [Lõi] Mỗi lệnh chi do đồng chủ tài khoản duyệt được nhắn tin cho chủ tài khoản chính sau khi thực hiện (ngân hàng hay phần mềm gửi: OQ-6), kèm báo cáo tháng các lệnh này.
- A14 [Mới] [Lõi] [Cấu hình] Chờ OTP quá `P-thoi-gian-cho-otp` (Delta: chưa chốt, đề xuất 30 phút) thì nhắc chủ tài khoản qua SMS.
- A15 [SOP to-be] [Lõi] [Cấu hình] Ngân hàng ngừng kết nối quá `P-thoi-gian-cho-ngan-hang` (Delta: chưa chốt, đề xuất 2 giờ): phần mềm xuất lệnh chi đã duyệt ra tệp theo mẫu của từng ngân hàng (Excel hoặc XML), kế toán tải lên Internet Banking duyệt tay; hoặc người tạo chuyển cách trả sang tạm ứng (E2 của `service-delivery`).
- A16 [SOP+] [Lõi] Lớp kết nối ngân hàng dùng chung: mỗi ngân hàng là một bộ nối thay được (gửi lệnh chi, nhận kết quả, nhận sổ phụ). MB Bank, Vietcombank, TP Bank là 3 bộ nối đầu tiên.

### P2 — nice to have

Chưa có.

## 5. Core Flows (Happy Path)

### 5.1 Thanh toán nợ hóa đơn

1. [Người tạo] Mở JobID (hoặc Lệnh trên app), bấm Yêu cầu thanh toán, chọn loại chi phí, chọn cách: QR động, QR tĩnh, hoặc đối tác từ danh mục (lái xe được gợi ý cảng bãi gần).
2. (PM) Đọc QR, điền tài khoản nhận, số tiền, nội dung; QR tĩnh hoặc danh mục thì người tạo nhập số tiền. Phần mềm tự ghép nội dung chuyển tiền (A5).
3. (PM) Kiểm hiệu lực QR động (A6); đủ thì chuyển duyệt bước 1.
4. [Cán bộ quản lý] Duyệt bước 1; thấy đồng hồ đếm ngược QR. Vượt giới hạn thì sang [Ban giám đốc] duyệt bước 2.
5. (PM) Lập lệnh chi gửi ngân hàng từ tài khoản pháp nhân của chi nhánh; yêu cầu sang "Chờ ngân hàng".
6. [Chủ tài khoản / đồng chủ tài khoản] Duyệt OTP trên app ngân hàng.
7. (Ngân hàng) Trích tiền, trả UNC điện tử + mã FT.
8. (PM) Yêu cầu "Đã chi"; UNC lên JobID; chi phí ghi lên JobID, Lệnh; ghi tăng dư nợ tạm ứng 2 của người tạo; tạo việc "Thu hóa đơn GTGT". Người tạo nhận thông báo "Đã chi" kèm mã FT.

```
[Người tạo]   Yêu cầu nợ hóa đơn ── cách? ─QR động/tĩnh─► (PM) đọc QR ──┐
                                   └─Danh mục─► chọn đối tác (gợi ý   │
                                               cảng bãi gần) ─────────┤
                                                                      ▼
                              (PM) <QR động còn ≥ P-qr-hieu-luc-toi-thieu?>
                                   │Không → trả lại người tạo
                                   ▼Có
[Cán bộ quản lý]              Duyệt bước 1 ──Từ chối──► Bị trả lại
                                   │
                              <Trong giới hạn duyệt và hạn mức ngân hàng còn đủ?>
                                   │Không
                                   ├──────► [Ban giám đốc] Duyệt bước 2 ──Từ chối──► Bị trả lại
                                   ▼Có                    │
                              (PM) lập lệnh chi → Ngân hàng ◄──┘   [Chờ ngân hàng]
[Chủ tài khoản]               OTP trên app ngân hàng ──Không kịp──► Thất bại
                                   ▼
(Ngân hàng)                   Trích tiền, trả UNC + mã FT
                                   ▼
(PM)                          Đã chi · UNC lên JobID · tăng dư nợ tạm ứng 2
                              · việc "Thu hóa đơn GTGT"
```

### 5.2 Trả hóa đơn

1. (invoice-management) Hóa đơn về và tự khớp với mã FT của yêu cầu: dư nợ tạm ứng 2 tự giảm, xong (B3).
2. Không tự khớp: [Người tạo] trong `P-han-tra-hoa-don` lập Yêu cầu trả hóa đơn, chọn hóa đơn đã tải lên hoặc chọn trả tiền.
3. Nhân viên nộp lại tiền: (PM) tạo Phiếu thu chuyển thủ quỹ (`fund-payments`), thu xong thì dư nợ giảm.
4. [Kế toán] Duyệt: hóa đơn khớp mã phí trả hộ và JobID, hoặc tiền đối tác hoàn đã về.
5. (PM) Ghi giảm dư nợ tạm ứng 2; hóa đơn vào bảng kê nợ phải thu của khách.

```
(PM) mã FT khớp hóa đơn? ─Có─► tự giảm dư nợ tạm ứng 2 ─► xong
        │Không
        ▼
[Người tạo] Yêu cầu trả hóa đơn ─ chọn ─┬─ Hóa đơn ───────────┐
   (trong 3 ngày làm việc)              ├─ Đối tác hoàn tiền ─┤
                                        └─ Nộp lại tiền ──► Phiếu thu (fund-payments)
                                                              ▼
[Kế toán]                          Duyệt ──Từ chối──► trả về người tạo
                                     ▼
(PM)                     Giảm dư nợ tạm ứng 2 · hóa đơn vào bảng kê nợ phải thu

Quá hạn chưa trả ─► (PM) tạm dừng quyền tạo Yêu cầu nợ hóa đơn (B4)
```

## 6. System Behavior Deep Dive

### 6.1 Decision Points

| ID | Flow | Khi nào | YES | NO |
|---|---|---|---|---|
| D1 | 5.1 | Có ảnh QR? | Đọc QR | Chọn đối tác từ danh mục, kiểm hai vòng |
| D2 | 5.1 | QR đọc được và là QR chuyển khoản ngân hàng? | Điền thông tin | Báo lỗi, chọn từ danh mục |
| D3 | 5.1 | QR có số tiền? | Lấy số tiền QR | Người tạo nhập số tiền |
| D4 | 5.1 | QR động còn ≥ `P-qr-hieu-luc-toi-thieu`? | Chuyển duyệt bước 1 | Trả lại người tạo |
| D5 | 5.1 | Trong `P-han-muc-duyet-chi` và hạn mức ngân hàng của đồng chủ tài khoản còn đủ? | Gửi ngân hàng | Duyệt bước 2 |
| D6 | 5.1 | Ngân hàng trả thành công? | Đã chi | Thất bại, người tạo tạo yêu cầu mới |
| D7 | 5.2 | Hóa đơn tự khớp mã FT? | Tự giảm dư nợ | Yêu cầu trả hóa đơn |
| D8 | 5.2 | Quá `P-han-tra-hoa-don`? | Tạm dừng quyền tạo yêu cầu nợ hóa đơn | — |

### 6.2 Scenario Matrix — các giả định về QR

Các phụ thuộc phải kiểm với ngân hàng và đối tác trước khi viết SRS.

| Tình huống QR | Phần mềm làm gì | Giả định / phụ thuộc |
|---|---|---|
| QR động đủ số tiền và nội dung | Lấy nguyên, không sửa số tiền | Nội dung QR động không chèn thêm được, nên dùng cặp mã FT ↔ JobID (A12) |
| QR tĩnh: chỉ có tài khoản | Người tạo nhập số tiền; phần mềm tự ghép nội dung theo A5 | Số tiền nhập tay = điểm dễ sai, cán bộ quản lý thấy nhãn "Số tiền nhập tay" |
| QR có số tiền khác chi phí đã kê trên JobID | Cảnh báo chênh, người duyệt quyết | Chưa có trong nguồn (OQ-11) |
| QR không có thời hạn hiển thị | Coi như QR tĩnh | Cần ngân hàng xác nhận cách nhận biết hiệu lực QR động (OQ-11) |
| QR ví điện tử, không theo chuẩn chuyển khoản liên ngân hàng | Báo không dùng được, chọn từ danh mục | — |
| Tài khoản trên QR khác tài khoản đối tác trong danh mục | Cảnh báo, người duyệt quyết | Rủi ro đổi tài khoản lừa đảo |
| Một QR cho nhiều JobID (cảng gộp phí) | Một yêu cầu gắn nhiều JobID, chia tiền theo JobID | Chưa có trong nguồn (OQ-11) |
| Nhiều QR cho một JobID | Mỗi QR một yêu cầu | — |
| Ảnh QR mờ, chụp lệch | Báo chụp lại hoặc chọn từ danh mục | Dịch vụ đọc QR: tự làm hay thuê ngoài (OQ-12) |

### 6.3 State Transitions

```
Yêu cầu nợ hóa đơn: Nháp → Chờ duyệt → (Chờ duyệt bước 2) → Chờ ngân hàng → Đã chi
                              ↘ Bị trả lại → (sửa) → Chờ duyệt      (cả từ Chờ duyệt bước 2)
                              ↘ Thu hồi
                                    Chờ ngân hàng ↘ Thất bại
                                    Chờ ngân hàng ↘ Chờ xác nhận ngân hàng → (kế toán tra soát) Đã chi
                                    Đã chi (+ cờ "Đối tác cần hạch toán tay" khi QR hết hạn bị động)
Yêu cầu trả hóa đơn: Nháp → Chờ kế toán duyệt → Đã duyệt
                              ↘ Bị trả lại → (sửa) → Chờ kế toán duyệt
                     Nháp → (nhân viên nộp lại tiền) Chờ thủ quỹ thu → Đã thu
Quyền tạo yêu cầu nợ hóa đơn của nhân viên: Được tạo ⇄ Tạm dừng
```

| Entity | Từ | Sang | Trigger | Quay lại được? |
|--------|------|----|---------|-------------|
| Yêu cầu nợ hóa đơn | Chờ duyệt / Chờ duyệt bước 2 | Bị trả lại | QR dưới hạn (lúc gửi duyệt hoặc lúc duyệt xong, ngay trước khi gửi ngân hàng), người duyệt bước 1 hoặc 2 từ chối | có (sửa, gửi lại) |
| Yêu cầu nợ hóa đơn | Chờ duyệt | Chờ duyệt bước 2 | Vượt giới hạn duyệt hoặc hạn mức ngân hàng, hoặc cán bộ quản lý tự chuyển | không |
| Yêu cầu nợ hóa đơn | Chờ duyệt | Thu hồi | Người tạo rút | không |
| Yêu cầu nợ hóa đơn | Chờ ngân hàng | Thất bại | Ngân hàng từ chối, QR hết hạn trước OTP | không (tạo yêu cầu mới) |
| Yêu cầu nợ hóa đơn | Chờ ngân hàng | Đã chi | Ngân hàng trả mã FT | không (khóa) |
| Yêu cầu nợ hóa đơn | Chờ ngân hàng | Chờ xác nhận ngân hàng | Ngân hàng báo thành công mà không trả kết quả | có (kế toán tra soát, nhập mã FT) |
| Yêu cầu trả hóa đơn | Nháp | Chờ thủ quỹ thu | Nhân viên chọn nộp lại tiền | không |
| Yêu cầu trả hóa đơn | Chờ kế toán duyệt | Đã duyệt | Kế toán duyệt | không |
| Quyền tạo | Được tạo | Tạm dừng | Quá `P-han-tra-hoa-don` | có (OQ-9) |

Trạng thái lỗi của giao dịch ngân hàng (từ chối, treo, hoàn) cần kiểm lại khi có tài liệu kết nối của từng ngân hàng (OQ-13).

### 6.4 Interrupted Transactions

| Tình huống | Hệ thống còn lại gì | Resume | Cleanup |
|---|---|---|---|
| App mất mạng khi tạo yêu cầu | Nháp lưu trên máy | Tự gửi khi có mạng; QR động kiểm lại hiệu lực khi gửi | — |
| QR động hết hạn khi yêu cầu còn chờ duyệt | "Chờ duyệt" | Phần mềm kiểm lại `P-qr-hieu-luc-toi-thieu` ngay trước khi gửi ngân hàng; không đủ thì tự trả lại người tạo | Người tạo lấy QR mới |
| Không ai duyệt OTP | "Chờ ngân hàng" | Quá `P-thoi-gian-cho-otp` nhắc chủ tài khoản qua SMS; QR hết hạn thì "Thất bại" | Người tạo tạo yêu cầu mới |
| Ngân hàng báo thành công nhưng không trả kết quả về | "Chờ xác nhận ngân hàng" | Kế toán bấm "Tra soát", nhập mã FT tay | — |
| QR hết hạn sau khi tiền đã trích (hết hạn bị động) | "Đã chi" + cờ "Đối tác cần hạch toán tay" | Việc cho người tạo gửi UNC cho đối tác | Không chi lại |
| Ngân hàng ngừng kết nối | Yêu cầu "Chờ ngân hàng", xếp hàng | Tự gửi lại; quá `P-thoi-gian-cho-ngan-hang` thì xuất tệp lệnh chi cho kế toán duyệt tay hoặc chuyển cách trả (A15) | Lệnh đã xuất tệp không tự gửi lại nữa |
| Hai người duyệt cùng yêu cầu | Lần duyệt đầu | Người sau thấy đã duyệt | — |

### 6.5 Other Edge Cases

**Ngân hàng từ chối lệnh chi đến từ đâu:** sau khi phần mềm gửi lệnh chi, ngân hàng có thể trả về từ chối vì: số dư không đủ; tài khoản nhận sai, đã đóng hoặc ngân hàng nhận không hỗ trợ; vượt hạn mức giao dịch ngân hàng đặt cho tài khoản hoặc người duyệt; chủ tài khoản từ chối hoặc không duyệt OTP trong hạn; lệnh trùng. Danh sách lý do thật lấy từ tài liệu kết nối của từng ngân hàng (OQ-13).

**Khoản chi không bao giờ có hóa đơn** (phí được miễn sau khi đã trả, đối tác không xuất): người tạo chọn "trả tiền" ở Yêu cầu trả hóa đơn — đối tác hoàn hoặc tự nộp lại. Nếu là chi phí hợp lý mà không có hóa đơn, làm thế nào để xóa dư nợ: chờ khách (OQ-14); nội dung "thanh toán không hóa đơn để nhận lại số tiền này" đã bị Delta bỏ (comment 09/10).

## 7. Validation, Limits & Wording

### 7.1 Validation rules

| Field | Rule |
|---|---|
| JobID hoặc Lệnh | Bắt buộc; JobID chưa kê khai đủ thì khóa thanh toán (E-shipment-coordination-003) |
| Loại chi phí | Bắt buộc, chọn từ danh mục khoản mục chi phí (`cost-catalog`); lái xe chọn trong `P-phi-lai-xe-tra-ho` |
| Số tiền | Bắt buộc, lớn hơn 0; lấy từ QR động thì không sửa |
| Người nhận | Bắt buộc: từ QR hoặc từ danh mục đối tác |
| Ảnh QR | Bắt buộc nếu chọn cách trả QR |
| Chứng từ cảng bãi | Lái xe tải theo hướng dẫn của Quy trình điều phối cho từng loại JobID |
| Có / không hóa đơn GTGT | Bắt buộc |
| Yêu cầu trả hóa đơn | Chọn ít nhất 1 hóa đơn hoặc kê số tiền trả lại; đối tác hoàn thì bắt buộc tải UNC hoặc báo có |

### 7.2 Limits & Quotas (exact values)

| Tham số | Giá trị | Window | Behavior khi vượt |
|---|---|---|---|
| `P-qr-hieu-luc-toi-thieu` | Delta: 3 phút | Lúc gửi duyệt, ngay trước khi gửi ngân hàng | Trả lại người tạo |
| `P-qr-hieu-luc-goc-ngan` | Delta: 15 phút | Lúc đọc QR | Cảnh báo, gợi ý 3 cách |
| `P-han-muc-duyet-chi` | Delta: chưa chốt (OQ-3) | Mỗi lệnh | Duyệt bước 2 |
| `P-han-muc-dong-chu-tai-khoan` | Delta: 15 triệu/lệnh, 50 triệu/ngày (quản lý nghiệp vụ); 10 triệu/lệnh, 30 triệu/ngày (quản lý hiện trường) | Mỗi lệnh, mỗi ngày | Duyệt bước 2 |
| `P-so-cang-bai-goi-y` | Delta: 3–5 | Mỗi lần lái xe chọn | — |
| `P-han-tra-hoa-don` | Delta: 3 ngày làm việc | Từ ngày duyệt yêu cầu nợ hóa đơn | Tạm dừng quyền tạo |
| `P-khoa-cuoi-thang` | Delta: 2 ngày cuối tháng | Tháng | Tạm dừng từ ngày làm việc đầu tháng sau |
| `P-thoi-gian-cho-otp` | Delta: chưa chốt, đề xuất 30 phút | Từ lúc gửi ngân hàng | Nhắc qua SMS |
| `P-thoi-gian-cho-ngan-hang` | Delta: chưa chốt, đề xuất 2 giờ | Từ lúc ngân hàng ngừng | Xuất tệp lệnh chi, cho chuyển cách trả |

### 7.3 Wording samples (exact strings)

#### Error messages

| Tình huống | Wording | Code |
|---|---|---|
| QR sắp hết hạn | "Mã QR còn dưới {P-qr-hieu-luc-toi-thieu} phút. Tạo mã mới rồi gửi lại." | E-? |
| QR không đọc được | "Không đọc được mã QR. Chụp lại rõ hơn hoặc chọn người nhận từ danh mục." | E-? |
| Vượt giới hạn duyệt | "Khoản chi vượt hạn mức {số tiền}/lệnh của bạn. Đã chuyển duyệt bước 2." | E-? |
| Ngân hàng từ chối | "Ngân hàng từ chối lệnh chi: {lý do ngân hàng}. Tạo yêu cầu mới." | E-? |
| Bị tạm dừng quyền tạo | "Bạn còn {n} khoản quá hạn trả hóa đơn. Trả hóa đơn để tạo yêu cầu mới." | E-? |
| Bỏ trống trường bắt buộc | "Nhập [tên trường]." / "Chọn [tên trường]." | E-common-001 |
| Lỗi hệ thống | "Đã xảy ra lỗi. Thử lại sau." | E-common-008 |
| Mất mạng | "Mất kết nối. Kiểm tra mạng và thử lại." | E-common-009 |

#### Success messages

| Tình huống | Wording |
|---|---|
| Gửi ngân hàng | "Đã gửi lệnh chi sang ngân hàng. Chờ chủ tài khoản duyệt OTP." |
| Đã chi | "Đã chi {số tiền}. Mã FT {mã}." |
| Trả hóa đơn | "Đã trả hóa đơn cho khoản {mã FT}. Dư nợ còn {số tiền}." |

#### Info / neutral messages

| Tình huống | Wording |
|---|---|
| Hạn trả hóa đơn | "Còn {n} ngày để trả hóa đơn cho khoản {mã FT}." |
| Chờ OTP lâu | "Lệnh chi chờ OTP {n} phút. QR còn {m} phút." |

### 7.4 Bối cảnh hệ thống (mức nghiệp vụ)

**Thông tin cần lưu:** Yêu cầu nợ hóa đơn (người tạo, pháp nhân, tài khoản nguồn, người nhận, ảnh QR, chứng từ, lịch sử duyệt) · giao dịch ngân hàng (mã FT, UNC, ngày, số tiền, nội dung, trạng thái) · Yêu cầu trả hóa đơn (hóa đơn đã chọn hoặc số tiền trả lại, chứng từ hoàn tiền, người duyệt) · quyền tạo yêu cầu của từng nhân viên.

**Dịch vụ ngoài:**

| Dịch vụ | Mục đích | Ghi chú |
|---|---|---|
| Ngân hàng: MB Bank, Vietcombank, TP Bank | Gửi lệnh chi, nhận UNC, nhận sổ phụ | Có cần làm cả 3 không, thứ tự nào (OQ-12) |
| Đọc QR | Lấy tài khoản, số tiền, nội dung từ ảnh | Tự làm bằng thư viện mã nguồn mở hay dùng dịch vụ ngoài (VietQR.io), chi phí (OQ-12) |
| Bản đồ | Vị trí lái xe để gợi ý cảng bãi gần (A3) | Dùng chung với `transport-dispatch` |

**Thông báo:** trong app và thông báo đẩy cho mọi việc. SMS chỉ cho cảnh báo nặng, gồm nhắc chủ tài khoản duyệt OTP (chủ tài khoản có thể không có mạng).

**Việc chạy nền:** nhắc hạn trả hóa đơn · tạm dừng quyền tạo khi quá hạn · báo cáo dư nợ tạm ứng 2 đầu tháng · gửi lại lệnh chi khi ngân hàng có lại.

**Dùng chung:**

| Nhóm | Feature chung | Feature này cần | Trạng thái |
|---|---|---|---|
| Liên quy trình | `cross-process-flow` | Yêu cầu nợ hóa đơn từ JobID/Lệnh → Đã chi trả về JobID; Đã chi tạo việc "Thu hóa đơn GTGT"; Hóa đơn khớp FT → giảm dư nợ (`invoice-management`, `fund-payments`); Yêu cầu trả hóa đơn đã duyệt → bảng kê nợ phải thu (`debt-management`); nộp lại tiền → Phiếu thu (`fund-payments`) | đề xuất |
| Thông báo | (chưa có feature) | Đã chi, Bị trả lại, chờ duyệt bước 1/2, nhắc OTP qua SMS, nhắc hạn trả hóa đơn, tạm dừng quyền tạo | đề xuất |
| Lịch sử hoạt động | (chưa có feature) | Tạo, duyệt, từ chối, thu hồi yêu cầu; tạm dừng và mở quyền tạo | đề xuất |
| Thao tác chung | `common-workspace` | Lưu nháp trên máy khi mất mạng; mã Yêu cầu thanh toán | đề xuất |
| Quyền + danh mục | `access-control`, `organization` | Chỉ đọc danh mục đối tác và tài khoản; quyền duyệt bước 1, bước 2; pháp nhân của chi nhánh | đề xuất |

## 8. Assumptions

- Ngân hàng cho phần mềm gửi lệnh chi, còn duyệt OTP vẫn trên app ngân hàng; phần mềm không giữ quyền trích tiền.
- Ngân hàng trả kết quả theo thời gian thực kèm mã FT.
- Phần mềm biết hạn mức duyệt còn lại trong ngày của từng đồng chủ tài khoản (tự cộng các lệnh đã gửi, hoặc hỏi ngân hàng).
- Mỗi chi nhánh thuộc một pháp nhân, có tài khoản riêng; mỗi site đã gắn một chi nhánh. Delta có 3 pháp nhân: Delta HN (Delta Quốc tế, công ty mẹ), Delta Vận tải, Delta HCM (phỏng vấn 14/10; SIM & VIS ghi Delta Hải Phòng, cần khách xác nhận văn bản).
- Danh mục đối tác có vị trí của cảng bãi để gợi ý theo vị trí lái xe.

## 9. Risks

| Rủi ro | Khả năng | Hậu quả nghiệp vụ | Cách phòng |
|--------|----------|-------------------|-----------|
| Ngân hàng rút hoặc trì hoãn kết nối (tài liệu khách: ngân hàng bỏ ngay nếu có rủi ro an ninh, Delta là khách nhỏ) | thỉnh thoảng | Không bỏ được quỹ tạm ứng | Làm một ngân hàng trước; giữ luồng tạm ứng và xuất tệp lệnh chi làm đường lùi (A15) |
| Nhân viên bị tạm dừng quyền tạo giữa ca vì chưa trả hóa đơn | thường | Hàng kẹt ở cảng | Nhắc trước hạn; báo trước trên app khi sắp bị dừng (OQ-9) |
| Khách SaaS khác dùng ngân hàng khác | thường | Không bán được | Lớp kết nối ngân hàng thay được (A16) |

## 10. Success Criteria (preliminary)

- % khoản trả hộ đi qua ngân hàng thay vì tạm ứng tiền mặt.
- % yêu cầu "Thất bại" vì QR hết hạn; thời gian từ lúc tạo yêu cầu tới "Đã chi".
- % khoản chi tự trả hóa đơn nhờ khớp mã FT, không cần Yêu cầu trả hóa đơn.
- Số nhân viên bị tạm dừng quyền tạo mỗi tháng.

Hiện trạng và mục tiêu số: chưa có (OQ-15).

## 11. Open Questions

| ID | Câu hỏi | Nguồn khách | Trạng thái |
|---|---|---|---|
| OQ-1 | "Kiểm tra hai vòng" khi chọn người nhận từ danh mục là ai với ai? Có cho nhập tay số tài khoản không? | Phân hệ APAS (17/10/2026), mục 3.1.3 Bước 1 | Còn mở |
| OQ-2 | QR có hiệu lực gốc dưới 15 phút: mục 2.1.4 ghi chặn đẩy lệnh và cho chuyển QR tĩnh/số tài khoản hoặc nhờ quản lý duyệt nhanh; mục 3.1.4 thêm cách để đồng chủ tài khoản duyệt. Xác nhận dùng đủ 3 cách của mục 3.1.4 | Phân hệ APAS (17/10/2026), mục 2.1.4 và 3.1.4 | Đã có hướng: 3 cách, cần khách xác nhận |
| OQ-3 | Giới hạn duyệt bước 1 của từng cán bộ quản lý là bao nhiêu (phụ lục phân quyền chưa gửi)? Ai là người duyệt bước 2 ở từng chi nhánh? | Quy trình quản lý quỹ & Thanh toán (06/10/2026), mục 5.4.2.3, 5.4.2.4 | Còn mở |
| OQ-4 | Pháp nhân có tài khoản ở nhiều ngân hàng: phần mềm chọn ngân hàng nào cho từng lệnh chi (theo cam kết số lượng lệnh chi, theo số dư, theo ngân hàng người nhận)? | Quy trình quản lý quỹ & Thanh toán (06/10/2026), mục 5.4.2.5; Phân hệ APAS (17/10/2026), mục 5.2 | Còn mở |
| OQ-5 | JobID 2 chi nhánh cùng làm: chi từ tài khoản pháp nhân nào? | Chưa có trong tài liệu khách gửi | Còn mở |
| OQ-6 | Tin nhắn báo chủ tài khoản chính khi đồng chủ tài khoản duyệt: ngân hàng gửi hay phần mềm gửi? | Phân hệ APAS (17/10/2026), mục 2.1.4 | Còn mở |
| OQ-7 | Duyệt Yêu cầu trả hóa đơn thì ghi tăng nợ phải thu của khách (mục 5.5.2) hay nợ phải trả cho mã DK05 (mục 5.5.2.5)? | Quy trình quản lý quỹ & Thanh toán (06/10/2026), mục 5.5.2, 5.5.2.5 | Còn mở (nguồn tự lệch) |
| OQ-8 | Hóa đơn đã tự khớp mã FT: dư nợ tạm ứng 2 tự giảm luôn (APAS), hay vẫn cần nhân viên lập Yêu cầu trả hóa đơn và kế toán duyệt (SOP quỹ)? Đề xuất: tự giảm, Yêu cầu trả hóa đơn chỉ cho phần không tự khớp | Phân hệ APAS (17/10/2026), mục 3.3.2 Bước 4; Quy trình quản lý quỹ & Thanh toán (06/10/2026), mục 4.6, 5.5 | Còn mở |
| OQ-9 | Quyền tạo bị tạm dừng: tự mở lại khi trả đủ hóa đơn quá hạn, hay cần kế toán hoặc cán bộ quản lý mở? Có cho mở tạm khi đang kẹt hàng không? Yêu cầu duyệt trong 2 ngày cuối tháng mà đã trả hóa đơn kịp thì có bị tạm dừng đầu tháng sau không (nguồn không ghi điều kiện)? | Quy trình quản lý quỹ & Thanh toán (06/10/2026), mục 4.5 | Còn mở |
| OQ-10 | Tiêu chí "khoản bất thường" trong báo cáo dư nợ đầu tháng | Quy trình quản lý quỹ & Thanh toán (06/10/2026), mục 4.6 | Còn mở |
| OQ-11 | QR: số tiền QR khác chi phí đã kê; nhận biết hiệu lực QR động; một QR cho nhiều JobID | Phân hệ APAS (17/10/2026), mục 3.1.3, 3.1.4 | Còn mở |
| OQ-12 | Làm cả 3 ngân hàng hay một trước, thứ tự nào? (MB và TP Bank đã có giá, Vietcombank chưa.) Đọc QR tự làm hay dùng dịch vụ ngoài, chi phí? | Phân hệ APAS (17/10/2026), mục 3.1.2, 5.2; SIM & VIS – Công tác chuẩn bị (11/10/2026), mục III | Còn mở |
| OQ-13 | Trạng thái lỗi và lý do từ chối của giao dịch ngân hàng | Chưa có trong tài liệu khách gửi (chờ tài liệu kết nối ngân hàng) | Còn mở |
| OQ-14 | Khoản đã chi qua nợ hóa đơn, là chi phí hợp lý nhưng không có hóa đơn: xóa dư nợ tạm ứng 2 bằng cách nào? | Quy trình quản lý quỹ & Thanh toán (06/10/2026), mục 4.6 (đoạn đã bỏ theo comment 09/10) | Còn mở |
| OQ-15 | Số hiện trạng: % chi bằng tiền mặt, số người đang ứng tiền túi | Chưa có trong tài liệu khách gửi | Còn mở |
| OQ-16 | Trả hộ ngoài giờ hành chính: SOP quỹ còn cho tạm ứng tiền mặt cho hóa đơn dưới 5 triệu ngoài giờ, APAS muốn bỏ quỹ tạm ứng. Ngoài giờ ai duyệt bước 1 và bấm OTP; có giữ đường tạm ứng tiền mặt không? | Quy trình quản lý quỹ & Thanh toán (06/10/2026), mục 4.2; Phân hệ APAS (17/10/2026), mục I | Còn mở |
| OQ-17 | Tổng hóa đơn trả lớn hơn số đã chi qua nợ hóa đơn: phần chênh xử lý thế nào (chi bổ sung, Yêu cầu thanh toán mới)? | Quy trình quản lý quỹ & Thanh toán (06/10/2026), mục 4.3.1, 4.11 | Còn mở |
| OQ-18 | Yêu cầu trả hóa đơn: chỉ kế toán duyệt (mục 5.5.2.4) hay thêm bước 2 Ban giám đốc (bảng phân quyền mục 6.4.1, bản gốc tự ghi dự thảo)? | Quy trình quản lý quỹ & Thanh toán (06/10/2026), mục 5.5.2.4, 6.4.1 | Còn mở (nguồn lệch) |

## 12. Next Steps

- Gửi Delta OQ-1 tới OQ-18.
- `/api-assess payment-on-behalf` — so sánh tự làm và thuê ngoài cho đọc QR, chọn ngân hàng làm trước.
- `/user-flow payment-on-behalf`, rồi `/srs payment-on-behalf`.
