---
type: brainstorm
feature: shipment-coordination
status: draft
updated: 2026-10-12
links:
  - docs-input/sop/sop-dieu-phoi.md
  - docs-input/sop/sop-cung-cap-dich-vu-tong-quat.md
  - docs-input/sop/giao-nhan-hang-hoa/giao-nhan-hang-hoa.md
  - docs-input/sop/sop-ban-do-kien-thuc.md
  - docs/_research/2026-10-02-container-deadline-alerts.md
  - docs/_research/2026-10-02-eport-integration.md
  - docs/_research/2026-10-02-field-document-reading.md
  - docs/_shared/project-profile.md
  - docs/meetings/decks/2026-10-06-oq-dispatch-coordination-deck.md
  - docs/meetings/2026-10-09-client-dispatch-field-issues.md
  - docs/meetings/2026-10-10-oq-dispatch-coordination.md
  - docs/service-delivery/brainstorms/service-delivery.md
  - docs/transport-dispatch/brainstorms/transport-dispatch.md
---

# Điều phối — từ JobID tới Yêu cầu vận tải, theo 6 luồng hàng

> Phỏng vấn xong đủ 7 phần ngày 2026-10-07: tổng quan, người dùng, luồng chính, trạng thái và tình huống, kiểm tra dữ liệu và câu thông báo, bối cảnh hệ thống, rủi ro và tiêu chí thành công.
> Cập nhật 2026-10-12 theo trả lời của Delta cho bộ câu hỏi vòng 1 (biên bản 2026-10-10).
> Tách ngày 2026-10-12 theo SOP: Quy trình cung cấp dịch vụ tổng quát ([[docs/service-delivery/brainstorms/service-delivery.md|service-delivery]]) · Quy trình điều phối (feature này) · Quy trình điều vận ([[docs/transport-dispatch/brainstorms/transport-dispatch.md|transport-dispatch]]). Mã ý tưởng (A1, B7…), DP-nn và OQ-n giữ nguyên số của bản gộp.

## 1. Idea Seed

Dữ liệu đi liền mạch từ JobID sang Yêu cầu vận tải (YCVT), không nhập lại. CS kê khai một lần, phần mềm phân luồng theo loại hàng và thuộc tính cảng/bãi: CS tự làm trên ePort, giao việc cho hiện trường, hoặc sinh YCVT ngay. Việc hiện trường được giao, nhận, chụp chứng từ trên app. Mỗi việc kéo theo chi phí định mức và quyền thanh toán đúng người, đúng JobID.

## 2. Context

**Vấn đề hiện tại feature này xử lý (khách xác nhận):**

| Mã | Vấn đề |
|---|---|
| a | Nhập lại cùng một dữ liệu nhiều lần |
| b | Giao việc qua điện thoại, Zalo; không truy được ai đang giữ việc |
| c | Không thấy trước mốc cắt máng, cut-off, lưu container, lưu vỏ nên bị phạt (Điều phối ghi mốc, Điều vận cảnh báo) |
| d | Chứng từ giấy về chậm nên chốt Lệnh và tính chi phí chậm (phần chứng từ hiện trường) |

**Phạm vi:**
- Gồm: Điều phối 6 luồng (FCL, LCL/CFS, air × xuất, nhập): nhận JobID, kê khai và phân luồng, việc ePort, giao việc hiện trường (kể cả trực ngoài giờ), việc hiện trường trên mobile (chụp chứng từ, AI đọc), sinh YCVT.
- Ranh giới với 2 feature cùng chuỗi:
  - Cung cấp dịch vụ tổng quát (`service-delivery`): tạo và duyệt JobID, hoàn thành dịch vụ, quy tắc thanh toán chi phí, giao dịch nội bộ (B7). Feature này nhận JobID ở trạng thái "Chờ xử lý".
  - Điều vận (`transport-dispatch`): nhận YCVT, lập và chạy Lệnh, cảnh báo quá mốc. Mốc do feature này ghi khi kê khai.
- CBT và đường sắt không có giao nhận tại cảng (CBT thuê ngoài toàn bộ) nên không đi qua Điều phối (Delta, 10/10/2026); đi thẳng từ JobID sang Điều vận.
- Không gồm: quản lý danh mục cảng/bãi (feature quản lý danh mục, OQ-47 ở userflow); phạm vi xem dữ liệu chi nhánh khác (feature Phân quyền).
- Ngoài giai đoạn 1: quản lý vỏ container.
- Ứng dụng: Delta Super App; web cho CS, cán bộ quản lý; mobile cho nhân viên hiện trường và lái xe khi được giao việc hiện trường.

**Nguồn:** Quy trình điều phối (mục 4, 5.1–5.6), Giao nhận hàng hoá 18/9/2026, 3 báo cáo điều tra trong `docs/_research/` (mốc container, ePort, đọc chứng từ hiện trường).

**Nhãn đề xuất:** [SOP to-be] = SOP đã yêu cầu, phần mềm làm theo · [SOP+] = SOP có nêu, đề xuất làm thêm · [Mới] = SOP chưa có. Chỉ [SOP+] và [Mới] tính là điểm khác biệt.

## 3. User Types (preliminary)

Phân quyền theo chức năng ("quyền hiện trường"…), không cố định vai trò. Luồng và sơ đồ vẫn ghi theo vai trò nghiệp vụ.

| User Type | Pain Point | Primary Need |
|-----------|-----------|--------------|
| CS | Nhập lại chứng từ; xe đi nhầm kho; không biết JobID đang kẹt ở đâu | Kê khai một lần, phân luồng đúng, theo dõi việc hiện trường |
| Nhân viên hiện trường | Nhận việc qua điện thoại; chứng từ gốc dễ thất lạc | Chụp chứng từ và xác nhận ngay tại chỗ |
| Cán bộ quản lý hiện trường | Giao việc bằng tin nhắn | Giao việc trong "Việc của tôi" theo người được gợi ý; xếp người trực |
| Lái xe | Được giao việc hiện trường (chọn vỏ) qua Zalo | Nhận việc hiện trường ngay trên app |
| Điều vận | Không biết YCVT nào sắp có | Nhận YCVT đủ dữ liệu để lập Lệnh |
| Trợ lý AI | — | Đọc chứng từ, gợi ý người nhận việc |

Mọi vai trò có màn "Việc của tôi" kèm thông báo đẩy mở thẳng vào việc. Mặc định chỉ thấy JobID của chi nhánh mình.

### 3.1 Tác vụ chính

Tần suất chưa đo được, ghi định tính. Dòng có ★ là tác vụ phải tối ưu cho thao tác nhanh nhất.

| Vai trò | Tác vụ | Tần suất | Mức quan trọng | Ghi chú |
|---------|--------|----------|----------------|---------|
| CS | ★ Kê khai JobID, quét QR tờ khai, đưa D/O, eDO, booking; việc ePort; chuyển việc cho hiện trường | Nhiều lần mỗi ngày | cao | Xe đi nhầm kho hoặc đi khi hàng chưa sẵn sàng |
| Nhân viên hiện trường | ★ Chụp: phiếu cân ra VGM, EIR, mã vạch gốc; nhận việc được gợi ý; thu hoá đơn GTGT | Vài lần mỗi ngày | cao | Trễ VGM nên lỡ tàu; mất chứng từ gốc |
| Cán bộ quản lý | ★ Việc của tôi: giao việc hiện trường, giao người trực ngoài giờ | Vài lần mỗi ngày | trung | Việc hiện trường không có người nhận |

## 4. Capabilities Breakdown

### P0 — must have

**Luồng lõi:** nhận JobID → hoàn thiện dữ liệu và phân luồng → giao việc hiện trường → sinh YCVT (Mục 5).

**Nhóm A — giảm nhập liệu**
- A1 [SOP+] [Lõi] [Cấu hình] AI đọc Booking Note, eDO để điền mốc cắt máng, cut-off, lưu container, lưu vỏ. Hàng nhập: số ngày miễn phí lưu container lấy từ Giấy báo hàng đến. Hàng xuất: CS nhập thời gian miễn phí lưu vỏ để đóng hàng (đã bổ sung vào SOP to-be).
- A2 [SOP+] [Lõi] Quét QR tờ khai hải quan; lưu cả ảnh QR lẫn thông tin bóc từ QR.
- A3 [SOP+] [Lõi] Kiểm số container theo chữ số kiểm tra ISO 6346, bắt sai ngay khi nhập hoặc AI đọc.
- A4 [SOP+] [Lõi] Chụp EIR để tự điền giờ, số container, số chì; giờ EIR nhận hàng là mốc tính lưu vỏ.
- A5 [SOP+] [Lõi] Hỗ trợ CS danh sách việc ePort theo cảng, lưu lệnh và EIR về Lệnh (không kết nối máy với ePort).
- A6 [SOP+] [Lõi] Quét QR Lệnh giao vỏ điện tử (mức nhẹ).
- A8 [SOP+] [Lõi] AI đọc phiếu cân ra VGM; người chụp bắt buộc xác nhận trước khi lưu.

**Nhóm B — quy trình**
- B1 [SOP+] [Lõi] Danh mục cảng/bãi có 3 thuộc tính: có ePort, có xe mới chọn được vỏ, thanh lý tờ khai online hay tại bãi; phần mềm phân luồng theo 3 thuộc tính này. Người có quyền (theo Phân quyền) cập nhật.
- B2 [SOP to-be] [Lõi] [Cấu hình] Nút "Chuyển việc" thay "Từ chối", bắt buộc chọn lý do trong `P-ly-do-chuyen-viec` (Delta: "Hết giờ làm việc" · "Khác" tự ghi); quyền thanh toán tự chuyển sang hiện trường.
- B3a [SOP+] [Lõi] [Cấu hình] Gợi ý `P-so-nguoi-goi-y-nhan-viec` (Delta: 2–3) người nhận việc (gần cảng/bãi, số việc đang ôm, trong ca trực); quản lý vẫn bấm chọn. Dùng chung quy tắc "người gần lái xe nhất".
- B3b [SOP to-be] [Lõi] [Cấu hình] Cán bộ quản lý hiện trường giao người trực ngoài giờ theo `P-ca-truc-ngoai-gio` (Delta: 17h30–8h); người trực có quyền tự giao việc trong ca, hết ca thu quyền. [Mới] Đầu ca và cuối ca có bước bàn giao việc đang dở giữa người trực và người làm giờ hành chính, theo `P-ban-giao-ca-truc` (Delta: bật).
- B4 [SOP+] [Cấu hình] Lệnh hạ vỏ rỗng (chỉ hàng nhập FCL): JobID có 1 container thì gộp giao việc theo vận đơn + nơi hạ theo `P-gop-giao-viec-ha-vo` (Delta: bật); JobID nhiều container thì giao từng container, vì khách nhận hàng khác ngày.
- Giao việc cho người chi nhánh khác tuyến thì phần mềm tự ghi giao dịch nội bộ — xem B7 ở `service-delivery`.

**Nhóm D — từ SOP Giao nhận hàng hoá**
- D4 [SOP+] [Lõi] Nơi nhận trên Lệnh lấy thẳng từ D/O, không nhập tay; D/O đổi kho thì Lệnh cập nhật theo, xe đã giao thì báo điều vận.

### P1 — should have

Chưa phân mức: mọi đề xuất đã chốt ở trên đều làm ngay giai đoạn này.

### P2 — nice to have

Chưa có.

## 5. Core Flows (Happy Path)

### 5.1 Luồng tổng (xương sống chung của 3 feature)

0. **Tạo và duyệt JobID** — `service-delivery`.
1. **Nhận JobID vào Điều phối** — phần mềm đưa vào danh sách của CS, bắt đầu đếm mốc.
2. **Hoàn thiện dữ liệu và phân luồng** — CS kê khai, đưa chứng từ; nơi nhận lấy từ D/O; chưa kê khai đủ thì khoá thanh toán trên JobID.
3. **Giao việc hiện trường** — cán bộ quản lý hiện trường chọn người (phần mềm gợi ý `P-so-nguoi-goi-y-nhan-viec` (Delta: 2–3) người); phần mềm ghi chi phí định mức, cấp quyền thanh toán. Giao cho người chi nhánh khác thì tự ghi giao dịch nội bộ (B7).
4. **Sinh YCVT** — FCL: sau khi hiện trường xong việc tại cảng/bãi. Hàng lẻ, CFS, air: ngay khi giao việc, việc hiện trường chạy song song với Lệnh.
5–7. **Lập, chạy, chốt và duyệt Lệnh** — `transport-dispatch`.
8. **Hoàn thành dịch vụ** — `service-delivery`.

Ký hiệu: `[Vai trò]` người làm · `(PM)` phần mềm tự làm · `<…?>` điểm rẽ nhánh.

```
JobID "Chờ xử lý" (từ service-delivery, có thủ tục giao nhận)
   |
   v
1-2. HOÀN THIỆN DỮ LIỆU
[CS] Kê khai giờ nhận/trả, nơi hạ, tờ khai + QR, đưa D/O, booking
(PM) Nơi nhận lấy thẳng từ D/O; bắt đầu đếm mốc cut-off / lưu cont / lưu vỏ
(PM) Chưa kê khai đủ --> khoá thanh toán trên JobID
[CS] Hàng nhập: trả phí lấy eDO, cược vỏ
   |
   v
<FCL đi thẳng ra YCVT được không? (xem 5.2, 5.3)>
   | Có ------------------------------------------------------------+
   | Không / CS bấm "Chuyển việc" (chọn lý do)                      |
   v                                                                |
3. GIAO VIỆC                                                        |
(PM) Gợi ý 2-3 người gần nhất                                       |
[Cán bộ QL hiện trường] Chọn nhân viên hiện trường hoặc lái xe       |
(PM) Ghi chi phí định mức, cấp quyền thanh toán cho người được giao  |
   |                                                                |
   v                                                                |
<Loại hàng?>                                                        |
   | FCL                              | LCL / CFS / air             |
   v                                  v                             |
[Hiện trường] chọn vỏ,               (PM) Sinh YCVT ngay;           |
   lấy lệnh nâng, chụp EIR,          việc hiện trường chạy song     |
   phiếu cân -> VGM                  song với Lệnh                  |
   (giao cho lái xe: bỏ qua)                 |                      |
   |                                         |                      |
   v                                         v                      v
4. (PM) Sinh YCVT, 1 YCVT / container  --> sang ĐIỀU VẬN (transport-dispatch)
```

Mục 5.2–5.7 vẽ trọn từng luồng theo SOP để thấy chỗ nối; các bước sau khi sinh YCVT (lập Lệnh, lái xe chạy, chốt Lệnh) thuộc `transport-dispatch`.

### 5.2 FCL xuất

Theo Quy trình điều phối mục 5.1.

```
[CS] Kê khai: giờ đóng hàng, giờ nhận vỏ, cảng hạ hàng, thông báo hãng tàu, tờ khai + QR,
     thời gian miễn phí lưu vỏ để đóng hàng
(PM) Cấp quyền trả phí nâng vỏ cho CS
   |
   v
<Bãi cấp vỏ phải có xe mới chọn được vỏ? Bãi có ePort?>
   +-- Có xe mới chọn, có ePort ---- [CS] làm lệnh nâng khống ------------------> (A)
   |                                 CS Chuyển việc --> [Cán bộ QL] giao HT ----> (A)
   +-- Có xe mới chọn, không ePort - lái xe tự chọn vỏ, làm lệnh nâng tại bãi -> (A)
   +-- Chọn trước được, có ePort --- [CS] làm lệnh nâng vỏ, hoặc Chuyển việc ---> (B)
   +-- Chọn trước được, không ePort  phải chọn vỏ trước rồi mới làm lệnh nâng --> (B)

(B) [Cán bộ QL] giao việc chọn vỏ
   +-- Giao lái xe ------------------------------------------------------------> (A)
   +-- Giao hiện trường: chọn vỏ, xác nhận số container (từ chối -> giao lại) --> (A)

(A) (PM) Sinh YCVT, 1 YCVT / container đã chọn
   |
   v
[Điều vận] Lập Lệnh --> [Lái xe] lấy vỏ, chụp EIR --> đóng hàng tại kho khách
   --> chụp phiếu cân --> (PM) AI ra VGM, người chụp xác nhận
   |
   v
<Cảng hạ hàng có ePort?>
   +-- Có:    [CS] khai VGM, làm lệnh hạ hàng (hoặc giao hiện trường)
   +-- Không: [Lái xe] làm lệnh hạ hàng theo nơi hạ đã kê khai
   |
   v
[Lái xe] Hạ container tại cảng --> chốt Lệnh
```

### 5.3 FCL nhập

Theo Quy trình điều phối mục 5.4.

```
[CS] Kê khai: giờ nhận cont tại cảng, hạn trả vỏ, bãi hạ vỏ, thông báo hãng tàu, tờ khai + QR
(PM) Số ngày miễn phí lưu container đọc từ Giấy báo hàng đến
(PM) Chưa kê khai đủ --> khoá thanh toán trên JobID
[CS] Trả hãng tàu lấy eDO; ghi hạn eDO, hạn trả vỏ; trả phí gia hạn nếu có; cược vỏ
   |
   v
<Cảng nhận hàng có ePort?>
   +-- Có:    [CS] đổi eDO lấy lệnh nâng hàng cho đủ container trên vận đơn --> (A)
   |          (cảng phải thanh lý tờ khai tại bãi: HT vẫn xuống cảng - OQ-39)
   |          CS bấm "Chuyển việc" --> (B)
   +-- Không: --> (B)

(B) [Cán bộ QL] giao hiện trường (PM: cấp quyền trả phí nâng, ghi định mức, tên + SĐT)
   --> [HT] trả phí nâng, xuất trình eDO + chứng từ cược + QR, lấy lệnh nâng hàng --> (A)

(A) (PM) Sinh YCVT, 1 YCVT / container
   |
   v
[Điều vận] Lập Lệnh --> [Lái xe] nhận cont tại cảng, chụp EIR
   --> giao kho khách, chụp biên bản giao hàng
   |
   v
<Bãi hạ vỏ có ePort?>
   +-- Có:    [CS] làm lệnh hạ vỏ từ EIR + lệnh giao hàng + email nơi hạ vỏ
   +-- Không: [Lái xe] làm lệnh hạ vỏ theo nơi hạ đã kê khai
   |
   v
[Lái xe] Trả vỏ rỗng --> chốt Lệnh        (PM) Đếm hạn trả vỏ, cảnh báo lưu vỏ
(Giao việc hạ vỏ: JobID 1 container gộp theo vận đơn + nơi hạ; nhiều container giao từng cái)
```

### 5.4 LCL xuất

Theo Quy trình điều phối mục 5.2.

```
[CS] Kê khai: giờ nhận hàng, Packing List, kho CFS giao, tờ khai + QR,
     truck sheet (riêng kho Pan Hải An)
[Cán bộ QL] Giao hiện trường --> (PM) ghi định mức, tên + SĐT; SINH YCVT NGAY
   |                                              |
   v                                              v
[Điều vận] Lập Lệnh (gợi ý ghép lô)          [HT] thanh lý tờ khai, kiểm hoá nếu có,
[Lái xe] lấy hàng tại kho khách,                  xuất trình Booking Note co-loader + PL
  chụp phiếu xuất kho của khách,             --> lập Phiếu nhập kho + phiếu kiểm đếm
  chụp thùng xe niêm phong (nếu khách cần)   --> nhập số kiện, CBM, kg
  --> giao vào kho CFS trước cut-off kho          (PM) thay số trên Booking Note
   |                                              |
   +----------------------+-----------------------+
                          v
                      Chốt Lệnh
```

### 5.5 Air xuất

Theo Quy trình điều phối mục 5.3. Giống LCL xuất, khác 4 chỗ:

```
- Kê khai Commercial Invoice thay Packing List; giao vào kho hàng không, hạn là closing time
- [HT] lập Phiếu cân thay Phiếu nhập kho
- Nhập số kiện + kích thước từng kiện + trọng lượng
- (PM) tự tính CBM và chargeable weight, thay số trên Booking Note
```

### 5.6 CFS nhập

Theo Quy trình điều phối mục 5.5.

```
[CS] Kê khai: giờ trả hàng, kho CFS nhận, tờ khai + QR
[CS] Trả đại lý lấy eDO, đưa eDO lên JobID
[Cán bộ QL] Giao hiện trường --> (PM) cấp quyền trả phí kho, ghi định mức; SINH YCVT NGAY
[Điều vận] Lập Lệnh (gợi ý ghép lô)
   <Kho CFS đã xác nhận hàng sẵn sàng?> --Chưa--> cảnh báo, vẫn giao xe được
   |
   v
Tại kho, 3 bên cùng lúc (kho giao - hiện trường làm thủ tục - lái xe nhận):
   [HT] chụp ảnh hàng; xuất trình eDO + QR để thanh lý tờ khai;
        trả phí facility, lưu kho; lấy Phiếu xuất kho
   [Lái xe] nhận hàng --> giao kho khách, chụp biên bản giao hàng
   |
   v
Chốt Lệnh
```

### 5.7 Air nhập

Theo Quy trình điều phối mục 5.6. Giống CFS nhập, khác 3 chỗ:

```
- <Đã về đủ kiện?> --Chưa--> CHẶN giao xe --> [CS] "Khai theo số đã về" / "Chờ đủ" (Điều vận D3)
- Lô tách chuyến: mỗi đợt hàng về = 1 Lệnh mới dưới cùng JobID
- JobID có đánh dấu mã vạch gốc --> theo dõi: hiện trường -> CS đã nhận -> đã giao khách (service-delivery D9)
```

## 6. System Behavior Deep Dive

### 6.1 Decision Points

| ID | Flow | Khi nào | YES (nhánh đồng ý) | NO (nhánh từ chối) |
|---|---|---|---|---|
| DP-03 | Hoàn thiện dữ liệu | CS kê khai đủ | Mở thanh toán trên JobID | Khoá thanh toán |
| DP-04 | FCL xuất, nhập | Bãi có ePort và CS tự làm lệnh nâng | Sinh YCVT (bỏ qua giao việc, trừ FCL xuất chọn vỏ trước) | Giao việc hiện trường |
| DP-05 | FCL xuất | Bãi phải có xe mới chọn được vỏ | Lệnh nâng khống hoặc lái xe tự chọn vỏ | Chọn vỏ trước khi xe đến |
| DP-06 | Giao việc | Loại hàng FCL | Hiện trường xong việc mới sinh YCVT | Sinh YCVT ngay, hiện trường song song |
| DP-10 | Hạ hàng / hạ vỏ | Cảng/bãi hạ có ePort | CS làm lệnh hạ | Lái xe làm lệnh hạ |
| DP-14 | Giao việc hạ vỏ (FCL nhập) | JobID có 1 container | Gộp theo vận đơn + nơi hạ | Giao từng container |

DP-13 (giao việc trái tuyến thì ghi giao dịch nội bộ) xem `service-delivery`.

### 6.2 Scenario Matrix

Ai được đổi trạng thái gì, ở trạng thái nào.

| Đối tượng | Từ | Sang | Ai làm | Điều kiện | Kết quả |
|---|---|---|---|---|---|
| JobID | Chờ xử lý | Đã tạo YCVT | Phần mềm | Đủ điều kiện sinh YCVT theo luồng | Sinh YCVT, sang Điều vận |
| Việc hiện trường | Đã giao | Đã nhận | Người được giao | — | Hiện tên người giữ việc |
| Việc hiện trường | Đã giao | Về cán bộ quản lý | Người được giao | Từ chối, bắt chọn lý do | Cán bộ quản lý giao lại |
| Việc hiện trường | Đã giao | Về cán bộ quản lý | Phần mềm | Quá `P-thoi-gian-cho-nhan-viec` chưa nhận (OQ-41) | Cán bộ quản lý giao lại |
| Việc ePort | CS giữ | Hiện trường giữ | CS | Bấm "Chuyển việc", bắt chọn lý do | Quyền thanh toán chuyển theo |
| YCVT | — | Đã được tạo | Phần mềm | FCL: hiện trường xong việc; hàng lẻ, CFS, air: ngay khi giao việc | Hiện trên Màn theo dõi xếp xe của Điều vận |

### 6.3 State Transitions

**Yêu cầu vận tải (YCVT)** — định nghĩa ở Quy trình điều phối mục 4.3. Feature này tạo YCVT; Điều vận lập Lệnh từ YCVT.

```
Đã được tạo --> Đã lập Lệnh vận tải --> Đã thực hiện Lệnh vận tải
```

- Điều vận khai số xe cần; mỗi lần lập Lệnh phần mềm trừ dần tới hết; không khai thì chỉ lập được 1 Lệnh. YCVT hiện "đã lập x/n Lệnh".
- Nhiều YCVT hàng lẻ được gộp vào 1 Lệnh nếu đủ một xe.

Vòng đời JobID xem `service-delivery` Mục 6.3; feature này đổi JobID từ "Chờ xử lý" sang "Đã tạo YCVT".

### 6.4 Interrupted Transactions

| # | Tình huống | Xử lý |
|---|---|---|
| 1 | Mất sóng hoặc tắt app khi hiện trường đang chụp chứng từ | Lưu trên máy, tự đồng bộ khi có sóng. Giờ và vị trí lấy theo lúc chụp, không phải lúc gửi. Việc hiện nhãn "Chờ đồng bộ" |
| 2 | AI không đọc được chứng từ (ảnh mờ, mẫu lạ) | Chuyển sang nhập tay, ảnh hiện bên cạnh. Đánh dấu "nhập thủ công" để thống kê |
| 3 | Hai người cùng nhận một việc | Ai bấm "Nhận xử lý" trước giữ việc; người sau thấy tên người đang giữ (E-shipment-coordination-002) |
| 4 | Người được giao từ chối hoặc quá lâu không nhận việc | Việc quay về cán bộ quản lý giao lại. Thời gian "quá lâu": OQ-41 |
| 5 | D/O đổi kho khi xe đang chạy | Lệnh cập nhật nơi nhận, báo điều vận và lái xe (D4) |
| 6 | Sửa JobID (đổi Booking Note, giảm container) khi đã có YCVT, Lệnh | YCVT, Lệnh dư chưa giao lái xe thì tự huỷ; đã giao thì báo điều vận xử lý tay |

### 6.5 Other Edge Cases

- D/O đổi kho sau khi đã có Lệnh: Lệnh cập nhật theo; xe đã giao thì báo điều vận.
- CS bấm "Chuyển việc": bắt chọn lý do ("Hết giờ làm việc" hoặc "Khác" tự ghi); quyền thanh toán chuyển theo.
- Đầu ca, cuối ca trực ngoài giờ: bàn giao việc đang dở giữa người trực và người làm giờ hành chính (B3b).
- Nhân viên hiện trường từ chối chọn vỏ: JobID quay về cán bộ quản lý giao lại.

## 7. Validation, Limits & Wording

### 7.1 Validation rules

Quy tắc chung (bắt buộc, độ dài, ngày, email, số điện thoại) theo GR và E-common, không viết lại.

| Field | Rule |
|---|---|
| Số container | 4 chữ cái + 7 số, đúng chữ số kiểm tra ISO 6346 |
| Số tờ khai | 12 chữ số |
| VGM, số kiện, CBM, kg | Lớn hơn 0; AI đọc ra thì người chụp bắt buộc bấm xác nhận |
| Nơi nhận trên Lệnh | Lấy từ D/O, không nhập tay |
| Lý do bắt buộc | Chuyển việc · từ chối việc được giao |
| Lý do Chuyển việc (`P-ly-do-chuyen-viec`) | Delta: chọn 1 trong "Hết giờ làm việc" · "Khác" (bắt ghi nội dung) |

### 7.2 Limits & Quotas (exact values)

| Tham số | Giá trị | Window | Behavior khi vượt |
|---|---|---|---|
| Số người gợi ý nhận việc (`P-so-nguoi-goi-y-nhan-viec`) | Delta: 2–3 | mỗi việc | Quản lý vẫn bấm chọn |
| Ca trực ngoài giờ (`P-ca-truc-ngoai-gio`, `P-ban-giao-ca-truc`) | Delta: 17h30–8h; bàn giao bật | mỗi ngày | Cán bộ quản lý hiện trường giao người trực; người trực tự giao việc trong ca; bàn giao việc đầu ca, cuối ca |
| Gộp giao việc hạ vỏ (`P-gop-giao-viec-ha-vo`) | Delta: bật | mỗi JobID 1 container | Gộp theo vận đơn + nơi hạ |
| Thời gian chờ người nhận việc (`P-thoi-gian-cho-nhan-viec`) | Chưa có số (OQ-41) | mỗi việc được giao | Việc quay về cán bộ quản lý |

### 7.3 Wording samples (exact strings)

Ngôi "bạn", câu ngắn, không "Vui lòng" (theo design.md). Loại hiển thị theo GR-15: Inline dưới trường, Popup chặn giữa màn, Toast góc màn.

#### Error messages

| Mã | Loại | Tình huống | Câu |
|---|---|---|---|
| E-shipment-coordination-001 | Inline | Số container sai chữ số kiểm tra | "Số container không đúng. Kiểm tra lại chữ số cuối." |
| E-shipment-coordination-002 | Popup | Nhận việc đã có người nhận | **Việc đã có người nhận** · "[Tên] đã nhận xử lý lúc 14:05." |
| E-shipment-coordination-003 | Popup | Thanh toán khi JobID chưa kê khai đủ | **Chưa thanh toán được** · "Kê khai đủ thông tin JobID trước khi thanh toán chi phí." |
| E-common-009 | Toast | Mất mạng | Dùng câu chung |
| E-common-008 | Toast | Lỗi hệ thống | Dùng câu chung |

#### Success messages

- "Đã giao việc cho [tên]" · "Đã chuyển việc"

#### Info / neutral messages

| Tình huống | Câu |
|---|---|
| Mất sóng | "Chờ đồng bộ. Ảnh sẽ gửi khi có mạng." |
| AI không đọc được | "Không đọc được chứng từ. Nhập tay theo ảnh bên cạnh." |

### 7.4 Bối cảnh hệ thống (mức nghiệp vụ)

**Thông tin cần lưu**
- Trên JobID: chứng từ vận hành (tờ khai + QR, D/O, eDO, booking, thông báo hãng tàu); các mốc (cut-off, hạn eDO, hạn trả vỏ); người giữ quyền thanh toán; số ngày miễn phí lưu container, lưu vỏ.
- Trên việc hiện trường: người được giao, chi phí định mức, quyền thanh toán, ảnh chứng từ, số AI đọc và người xác nhận.
- Lịch sử: ai giao việc cho ai, lúc nào; ai đổi trạng thái; chỗ AI đọc sai đã được người sửa; số lần phải nhập thủ công.
- Danh mục: thuộc tính cảng/bãi (ePort, có xe mới chọn vỏ, cách thanh lý); phân công trực ngoài giờ.

**Dịch vụ bên ngoài**

| Dịch vụ | Mục đích | Tình trạng |
|---|---|---|
| AI đọc chứng từ | Đọc D/O, eDO, EIR, phiếu cân, mã vạch, tờ khai | Trong phạm vi |
| ePort | Không kết nối; chỉ lưu lệnh, EIR về Lệnh | Đã chốt |

**Thông báo**

| Ai nhận | Khi nào | Kênh |
|---|---|---|
| Người được giao việc | Có việc mới, việc bị trả lại | Thông báo đẩy + "Việc của tôi" |
| Cán bộ quản lý hiện trường | Việc bị từ chối, quá lâu không ai nhận | Thông báo đẩy + "Việc của tôi" |
| Người trực, người làm giờ hành chính | Đầu ca, cuối ca trực | Thông báo đẩy + "Việc của tôi" (bàn giao việc) |
| Điều vận, lái xe | D/O đổi kho khi xe đang chạy | Thông báo đẩy |

**Việc phần mềm tự chạy theo giờ:** bắt đầu đếm mốc khi JobID vào Điều phối (cảnh báo quá mốc ở Điều vận) · nhắc bàn giao đầu ca, cuối ca (`P-ban-giao-ca-truc`) · thu việc quá lâu không ai nhận (OQ-41).

**Cần gần như tức thời:** giao việc mới.

## 8. Assumptions

- SOP của Delta là thiết kế to-be của khách, không phải cách đang làm.
- SOP Quy trình điều phối mục 5.4.2.4 ghi "nhân viên CS upload đủ Lệnh nâng hàng" trong bước của hiện trường; hiểu là nhân viên hiện trường upload (chờ xác nhận, OQ-40).

## 9. Risks

| Rủi ro | Khả năng | Hậu quả nghiệp vụ | Cách phòng |
|--------|----------|-------------------|-----------|
| Hiện trường vẫn gửi ảnh và chứng từ qua Zalo, không dùng app | thường | Mất bằng chứng; chi phí không lên JobID | App chạy khi mất sóng; thao tác chính làm được bằng một tay |
| Thiếu dữ liệu nền: thuộc tính cảng/bãi, định mức chi phí | thường | Phân luồng sai | Chốt danh mục trước khi chạy thật; người có quyền cập nhật; bám OQ-3 |
| AI đọc sai chứng từ (VGM, số container, tên kho) | thỉnh thoảng | VGM sai thì lỡ tàu, bị phạt; đi nhầm kho | Người chụp bắt buộc xác nhận; kiểm chữ số container |

## 10. Success Criteria (preliminary)

Mỗi tiêu chí gắn một vấn đề ban đầu. Số hiện trạng và mục tiêu chờ khách (OQ-44, ở `service-delivery`).

| Vấn đề | Tiêu chí | Mục tiêu |
|---|---|---|
| a. Nhập lại nhiều lần | Tỉ lệ trường tự điền (AI đọc hoặc kế thừa từ JobID) trên tổng trường phải nhập khi kê khai và ở việc hiện trường | ? |
| b. Giao việc qua Zalo | Tỉ lệ việc hiện trường được giao và nhận trên app | ? |
| c. Bị phạt vì quá mốc | Tỉ lệ JobID có đủ mốc cut-off, lưu container, lưu vỏ ngay sau kê khai | ? |

## 11. Open Questions

Nguồn khách: tên tài liệu khách gửi và mục. Quy trình điều phối chưa có ngày bản trong sổ nguồn. Cột Trả lời theo biên bản [[docs/meetings/2026-10-10-oq-dispatch-coordination.md|Delta trả lời vòng 1]] (anh Nghĩa, 10/10/2026) và 2 điểm xác nhận lại ngày 12/10/2026.

| Mã | Câu hỏi | Nguồn khách | Trả lời |
|---|---|---|---|
| OQ-3 | Phụ lục Bảng thông tin JobID và Định mức chi phí còn trống | Quy trình điều phối, mục 6.1–6.2 | Còn mở: Delta gửi dần phụ lục |
| OQ-19 | Khách có cung cấp số booking, tàu, chuyến (xuất) hoặc free time lưu container, lưu vỏ (nhập) ngay khi đặt xe không? | Giao nhận hàng hoá (18/9/2026) | Một phần: hàng nhập lấy số ngày miễn phí từ Giấy báo hàng đến; hàng xuất CS nhập thời gian miễn phí lưu vỏ (đã bổ sung SOP). Còn thiếu: số booking, tàu khi đặt xe; bản SOP mới |
| OQ-21 | Các cảng, depot Delta làm nhiều nhất? | Chưa có trong tài liệu khách gửi | Bỏ: không thống kê được; lấy số thật khi phần mềm chạy, không cài sẵn thứ tự ưu tiên |
| OQ-22 | QR trên tờ khai hải quan chứa những trường nào? Xin mẫu thật | Quy trình điều phối, các mục "Phân luồng công việc" | Còn mở: QR tĩnh và động theo một chuẩn; chờ mẫu |
| OQ-24 | QR trên Lệnh giao vỏ điện tử chứa gì, bãi nào phát hành? | Mẫu Lệnh giao vỏ điện tử khách gửi | Còn mở: như OQ-22; chờ mẫu và danh sách bãi |
| OQ-25 | Danh sách lý do khi CS bấm "Chuyển cho hiện trường": bãi yêu cầu có xe mới chọn vỏ · ngoài giờ · ePort lỗi · khác (ghi chú) — khách duyệt, thêm, bớt | Quy trình điều phối, mục 5.1.2.2 | Đã chốt: nút "Chuyển việc", 2 lý do "Hết giờ làm việc" / "Khác" (tự ghi), bắt buộc (B2) |
| OQ-26 | Ca trực ngoài giờ: xếp lịch theo vòng hay từng ngày; ngày không có người trực thì sao; việc dở lúc 8h chuyển cho ai; có trực cuối tuần, lễ không; một chi nhánh mấy người trực? | Quy trình điều phối, mục 4 Định nghĩa | Đã chốt: cán bộ quản lý hiện trường giao người trực; thêm bàn giao việc đầu ca, cuối ca (B3b) |
| OQ-27 | Gộp giao việc Lệnh hạ vỏ theo vận đơn + nơi hạ có đúng thực tế không? | Chưa có trong tài liệu khách gửi | Đã chốt: chỉ hàng nhập FCL; gộp khi JobID có 1 container, nhiều container làm từng container (B4) |
| OQ-39 | Cảng có ePort nhưng hiện trường vẫn phải thanh lý tờ khai tại bãi: những cảng nào? | Quy trình điều phối, mục 5.4.2.2 | Chưa hỏi Delta (ngoài deck vòng 1) |
| OQ-40 | Bước lấy Lệnh nâng hàng của hiện trường (FCL nhập) ghi "nhân viên CS upload": là hiện trường upload hay CS phải upload lại? | Quy trình điều phối, mục 5.4.2.4 | Chưa hỏi Delta (ngoài deck vòng 1) |
| OQ-41 | Người được giao việc hiện trường bao lâu không bấm nhận thì việc tự quay về cán bộ quản lý giao lại? | Chưa có trong tài liệu khách gửi | Chưa hỏi Delta (ngoài deck vòng 1) |

## 12. Next Steps

Đã tách từ brainstorm Điều phối gộp ngày 2026-10-12. Tiếp theo:
- Hỏi lại Delta các câu còn mở ở Mục 11 (BL-041)
- `/user-flow shipment-coordination` — chạy lại; userflow tách máy từ bản nháp ngày 07/10, còn nội dung cũ (Chuyển cho hiện trường)
- `/srs shipment-coordination` — đặc tả FR, BR, Error Matrix
