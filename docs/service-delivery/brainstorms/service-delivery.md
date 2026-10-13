---
type: brainstorm
feature: service-delivery
status: draft
updated: 2026-10-12
links:
  - docs-input/sop/sop-cung-cap-dich-vu-tong-quat.md
  - docs-input/sop/sop-dieu-phoi.md
  - docs-input/sop/giao-nhan-hang-hoa/giao-nhan-hang-hoa.md
  - docs-input/sop/quan-ly-hoa-don-sim/quan-ly-hoa-don-sim.md
  - docs-input/sop/sop-ban-do-kien-thuc.md
  - docs/_research/2026-10-02-field-document-reading.md
  - docs/_shared/project-profile.md
  - docs/meetings/decks/2026-10-06-oq-dispatch-coordination-deck.md
  - docs/meetings/2026-10-10-oq-dispatch-coordination.md
  - docs/shipment-coordination/brainstorms/shipment-coordination.md
  - docs/transport-dispatch/brainstorms/transport-dispatch.md
---

# Cung cấp dịch vụ tổng quát — JobID từ lúc tạo đến khi hoàn thành dịch vụ

> Phỏng vấn xong đủ 7 phần ngày 2026-10-07 (chung với Điều phối và Điều vận), cập nhật 2026-10-12 theo trả lời của Delta cho bộ câu hỏi vòng 1 (biên bản 2026-10-10).
> Tách ngày 2026-10-12 theo SOP: Quy trình cung cấp dịch vụ tổng quát (feature này) · Quy trình điều phối ([[docs/shipment-coordination/brainstorms/shipment-coordination.md|shipment-coordination]]) · Quy trình điều vận ([[docs/transport-dispatch/brainstorms/transport-dispatch.md|transport-dispatch]]). Mã ý tưởng (A1, B7…), DP-nn và OQ-n giữ nguyên số của bản gộp.

## 1. Idea Seed

JobID là xương sống của mọi dịch vụ Delta cung cấp (hải quan, vận tải, thủ tục chuyên ngành, giá trị gia tăng). Tạo và duyệt JobID một lần từ chứng từ khách. Sau đó mọi việc làm ở Điều phối và Điều vận đều kéo chi phí, doanh thu về đúng JobID. Khi dịch vụ hoàn thành, doanh thu và chi phí đã sẵn sàng cho bảng kê, công nợ và hạch toán nội bộ.

## 2. Context

**Vấn đề hiện tại feature này xử lý (khách xác nhận):**

| Mã | Vấn đề |
|---|---|
| a | Nhập lại cùng một dữ liệu nhiều lần (tạo JobID từ chứng từ khách) |
| e | Chi phí chưa được hạch toán rõ ràng, đầy đủ |

Vấn đề b, c, d (giao việc qua Zalo, quá mốc bị phạt, chứng từ giấy về chậm) nằm ở Điều phối và Điều vận.

**Phạm vi:**
- Gồm: tạo và duyệt JobID (có AI đọc chứng từ, kiểm nợ quá hạn và hạn mức); phân JobID sang Điều phối (có thủ tục giao nhận) hoặc thẳng sang Điều vận (CBT, đường sắt, không làm hiện trường); quy tắc ghi nhận chi phí, doanh thu lên JobID; hoàn thành dịch vụ; tự ghi nhận giao dịch nội bộ khi làm trái tuyến (B7); hoá đơn trả hộ, hoá đơn điện tử, đổi bên xuất hoá đơn.
- Ranh giới với 2 feature cùng chuỗi:
  - Điều phối (`shipment-coordination`): nhận JobID "Chờ xử lý", kê khai, giao việc hiện trường, sinh YCVT. Màn Chi tiết JobID dùng chung cho cả 3 feature, thuộc feature này; Điều phối, Điều vận thêm phần kê khai, YCVT/Lệnh lên màn đó.
  - Điều vận (`transport-dispatch`): từ YCVT lập, chạy, chốt và duyệt Lệnh. Lệnh duyệt xong thì chi phí chuyển về JobID.
- Không gồm (feature riêng, chỉ đảm bảo dữ liệu đủ và đúng JobID): màn bảng kê, công nợ, kết nối MISA (ngoài phần lấy hoá đơn điện tử); "Thanh toán trả hộ" (duyệt hạn mức, QR, UNC, API ngân hàng); phạm vi xem dữ liệu chi nhánh khác (feature Phân quyền).
- Xử lý ngoài phần mềm: thoả thuận với khách về khoản chi ngoài định mức.
- Ứng dụng: Delta Super App, web cho CS, kế toán, cán bộ quản lý.

**Nguồn:** Quy trình cung cấp dịch vụ tổng quát (mục 4, 5.1–5.5), Quy trình điều phối (mục 4.2 Job ID nghiệp vụ), tài liệu Hoá đơn trả hộ 01/10/2026, báo cáo điều tra `docs/_research/2026-10-02-field-document-reading.md`.

**Nhãn đề xuất:** [SOP to-be] = SOP đã yêu cầu, phần mềm làm theo · [SOP+] = SOP có nêu, đề xuất làm thêm · [Mới] = SOP chưa có. Chỉ [SOP+] và [Mới] tính là điểm khác biệt.

## 3. User Types (preliminary)

Phân quyền theo chức năng, không cố định vai trò. Luồng và sơ đồ vẫn ghi theo vai trò nghiệp vụ.

| User Type | Pain Point | Primary Need |
|-----------|-----------|--------------|
| CS | Nhập lại chứng từ khi tạo JobID; không biết JobID đang kẹt ở đâu | Tạo JobID từ chứng từ, theo dõi tới khi hoàn thành dịch vụ |
| Điều vận | Tạo JobID cho CBT, đường sắt | Tạo JobID nhanh, đi thẳng sang lập Lệnh |
| Cán bộ quản lý | Duyệt bằng tin nhắn | Duyệt thông tin viết hoá đơn bất thường trong "Việc của tôi" |
| Kế toán | Chi phí về muộn, thiếu, không gắn JobID | Doanh thu, chi phí đã gắn đúng JobID khi dịch vụ hoàn thành |
| Đại diện khách hàng | Phải gọi CS hỏi tình trạng | Theo dõi lô, nhận file xuất |
| Trợ lý AI | — | Đọc chứng từ khách khi tạo JobID |

Mọi vai trò có màn "Việc của tôi" kèm thông báo đẩy mở thẳng vào việc. Mặc định chỉ thấy JobID của chi nhánh mình.

### 3.1 Tác vụ chính

| Vai trò | Tác vụ | Tần suất | Mức quan trọng | Ghi chú |
|---------|--------|----------|----------------|---------|
| CS | ★ Tạo JobID từ chứng từ; xác nhận doanh thu phát sinh; giao chứng từ gốc; hoàn thành dịch vụ | Nhiều lần mỗi ngày | cao | Thiếu doanh thu; khách chưa nhận căn cứ thanh toán |
| Cán bộ quản lý | Duyệt thông tin viết hoá đơn bất thường | Vài lần mỗi ngày | trung | Xuất sai hoá đơn |
| Kế toán | Nhận chi phí đã gắn Lệnh/JobID; thanh toán khoản từ `P-nguong-tam-ung` (Delta: 5.000.000 ₫) trở lên | Hằng ngày, dồn vào kỳ chốt | trung | Chốt kỳ trễ; hạch toán sai |
| Đại diện khách hàng | Theo dõi tình trạng lô; nhận file xuất | Thỉnh thoảng | thấp | Gọi hỏi CS nhiều |

## 4. Capabilities Breakdown

### P0 — must have

**Luồng lõi:** tạo, duyệt JobID → phân sang Điều phối hoặc Điều vận → (Điều phối, Điều vận làm việc, ghi chi phí lên Lệnh và JobID) → hoàn thành dịch vụ (Mục 5).

**Nhóm A — giảm nhập liệu**
- A9 [SOP+] [Lõi] Hoá đơn điện tử lấy qua kết nối nhà cung cấp hoá đơn điện tử (kết nối đầu tiên: MISA); không khớp thì chụp + nhập tay, gắn cờ "Chưa khớp hoá đơn điện tử".

**Nhóm B — quy trình**
- B7 [SOP+] [Gói: Đa chi nhánh] [Cấu hình] Giao dịch nội bộ theo 2 trường hợp trong SOP: tạo JobID trái tuyến (TH1) hoặc giao việc trái tuyến (TH2, phát sinh ở bước giao việc của Điều phối). Phần mềm lấy 2 dấu hiệu này để tự ghi nhận giao dịch nội bộ và tự hạch toán. Lợi nhuận chia theo `P-ty-le-chia-lai-noi-bo` (Delta: 50/50 lãi gộp, chỉ hạch toán sau khi đã chốt bảng kê công nợ phải thu, phải trả).

**Nhóm D — từ SOP Giao nhận hàng hoá**
- D9 [SOP+] [Lõi] Theo dõi mã vạch gốc air: Đang ở hiện trường → CS đã nhận → Đã giao khách; đánh dấu "cần chuyển mã vạch gốc" trên từng JobID; chưa giao khách thì JobID có cờ ở bước ghi nhận doanh thu.
- D10 [SOP to-be] [Lõi] CBT đổi bên xuất hoá đơn trên JobID tới trước khi xuất hoá đơn, không phải huỷ Lệnh; bên thứ ba chưa có mã thì tạo việc "Đăng ký bên thanh toán" kèm thoả thuận ba bên.

**Nhóm E — chi phí (vấn đề e)**
- E1 [SOP to-be] [Riêng Delta] Chi ngoài định mức: không làm luồng xin duyệt riêng trên app. Thoả thuận với khách giải quyết ngoài phần mềm; khoản chi ghi nhận và chi trả qua Quy trình cung cấp dịch vụ (chi phí mua ngoài) hoặc thanh toán không hoá đơn (Quy trình quản lý quỹ và thanh toán).
- E2 [SOP to-be] [Lõi] [Cấu hình] Phần mềm đề xuất cách trả theo ngưỡng `P-nguong-tam-ung` (Delta: 5.000.000 ₫) (dưới: tạm ứng; trên: tạo việc cho CS phụ trách + kế toán), bắt chọn có/không hoá đơn.
- E6 [SOP to-be] [Lõi] Nút tạo Yêu cầu thanh toán trên Lệnh/JobID, gắn chi phí đúng Lệnh/JobID; việc "Thu hoá đơn GTGT" giao người gần lái xe nhất; hiện trạng thái thanh toán. Màn Yêu cầu thanh toán của lái xe vẽ ở Điều vận (`payment-request`). Phần duyệt, QR, UNC, API ngân hàng thuộc feature "Thanh toán trả hộ".
- E9 [SOP+] [Lõi] Hoá đơn trả hộ ghi trên JobID. Khi lập bảng kê nợ phải thu, phần mềm đánh dấu hoá đơn trả hộ mà khách không xác nhận thanh toán. Cách xử lý tiếp chờ khách trả lời (OQ-6).

### P1 — should have

Chưa phân mức: mọi đề xuất đã chốt ở trên đều làm ngay giai đoạn này.

### P2 — nice to have

Chưa có.

## 5. Core Flows (Happy Path)

### 5.1 Luồng tổng (xương sống chung của 3 feature)

0. **Tạo và duyệt JobID** (feature này) — CS hoặc điều vận đưa chứng từ khách, khai phạm vi dịch vụ; AI đọc chứng từ, người tạo xác nhận. Không đạt điều kiện nợ quá hạn, hạn mức thì dừng hẳn, chờ khách thanh toán. JobID không có thủ tục giao nhận (CBT, đường sắt, không làm hiện trường) đi thẳng sang lập Lệnh. Tạo JobID trái tuyến thì phần mềm tự ghi giao dịch nội bộ (B7).
1–4. **Điều phối** (`shipment-coordination`) — nhận JobID, hoàn thiện dữ liệu và phân luồng, giao việc hiện trường, sinh YCVT.
5–7. **Điều vận** (`transport-dispatch`) — lập Lệnh, chạy Lệnh, chốt và duyệt Lệnh; duyệt xong chi phí lên JobID.
8. **Hoàn thành dịch vụ** (feature này) — CS xác nhận doanh thu phát sinh, giao chứng từ gốc; JobID ghi doanh thu, chi phí vào kỳ.

Ký hiệu: `[Vai trò]` người làm · `(PM)` phần mềm tự làm · `<…?>` điểm rẽ nhánh.

```
0. TẠO JOBID
[CS/Điều vận] Đưa chứng từ khách, khai phạm vi dịch vụ
   |
   v
(PM) AI đọc chứng từ --> [Người tạo] xác nhận / sửa (chỗ sửa lưu lại để AI học)
   |
   v
<Đạt điều kiện nợ quá hạn, hạn mức?> --Không--> DỪNG, chờ khách thanh toán
   | Có                                          (khách thanh toán xong -> đi tiếp)
   v
(PM) Tạo JobID trái tuyến? --Có--> tự ghi giao dịch nội bộ (B7)
   |
   v
<Có thủ tục giao nhận tại cảng / kho / sân bay?>
   | Có                                   | Không (CBT, đường sắt, không làm hiện trường)
   v                                      v
ĐIỀU PHỐI (bước 1-4)                     ĐIỀU VẬN: sinh YCVT, lập Lệnh (bước 5)
   |                                      |
   +-------------> ĐIỀU VẬN (5-7) <-------+
                        |
                        v  (PM) Lệnh duyệt xong: chi phí trên Lệnh chuyển lên JobID
8. HOÀN THÀNH DỊCH VỤ
[CS] Xác nhận doanh thu phát sinh; đổi bên xuất hoá đơn (CBT, D10); giao chứng từ gốc nếu JobID có đánh dấu (D9)
<Mọi Lệnh đã duyệt, doanh thu đã xác nhận?> --Không--> chỉ ra phần thiếu
   | Có
   v
(PM) JobID "Hoàn thành dịch vụ" --> ghi doanh thu, chi phí vào kỳ
(PM) Đường sắt --> tự vào bảng kê kỳ `P-ky-chot-duong-sat` (xem Điều vận D7)
```

### 5.2 Thanh toán chi phí trên JobID

```
[CS / Lái xe / Hiện trường] Tạo Yêu cầu thanh toán gắn Lệnh hoặc JobID
(PM) Chưa kê khai đủ JobID --> khoá thanh toán (Điều phối, DP-03)
(PM) Đề xuất cách trả theo `P-nguong-tam-ung`:
   +-- dưới ngưỡng: tạm ứng
   +-- từ ngưỡng trở lên: tạo việc cho CS phụ trách + kế toán
[Người tạo] Bắt chọn có / không hoá đơn
<Có hoá đơn?> --Có--> (PM) lấy hoá đơn điện tử từ MISA (A9) --Không khớp--> chụp, nhập tay, cờ "Chưa khớp hoá đơn điện tử"
(PM) Chi phí gắn đúng Lệnh / JobID; hiện trạng thái thanh toán
```

## 6. System Behavior Deep Dive

### 6.1 Decision Points

| ID | Flow | Khi nào | YES (nhánh đồng ý) | NO (nhánh từ chối) |
|---|---|---|---|---|
| DP-01 | Tạo JobID | Đạt điều kiện nợ quá hạn, hạn mức | Đi tiếp | Dừng, chờ khách thanh toán |
| DP-02 | Tạo JobID | Có thủ tục giao nhận tại cảng/kho/sân bay | Vào Điều phối (bước 1) | Thành YCVT, sang lập Lệnh (Điều vận) |
| DP-13 | Tạo JobID, giao việc | Người tạo JobID hoặc người nhận việc thuộc chi nhánh khác tuyến | Tự ghi giao dịch nội bộ, chia lãi gộp 50/50 sau khi chốt bảng kê | Không ghi |

### 6.2 Scenario Matrix

Ai được đổi trạng thái gì, ở trạng thái nào.

| Đối tượng | Từ | Sang | Ai làm | Điều kiện | Kết quả |
|---|---|---|---|---|---|
| JobID | Chờ duyệt | Chờ xử lý | Phần mềm (hoặc người tạo, khi chưa có dữ liệu công nợ) | Đạt nợ quá hạn, hạn mức | Vào danh sách của CS, bắt đầu đếm mốc |
| JobID | Chờ duyệt | Dừng - chờ khách thanh toán | Phần mềm | Không đạt | Báo CS |
| JobID | Dừng - chờ khách thanh toán | Chờ xử lý | Phần mềm | Khách thanh toán xong | Vào danh sách của CS |
| JobID | Chờ xử lý | Huỷ | CS | Chưa phân luồng | Đóng JobID |
| JobID | Đã thực hiện Lệnh vận tải | Hoàn thành dịch vụ | CS | Mọi Lệnh đã duyệt; đã xác nhận doanh thu phát sinh | Ghi doanh thu, chi phí vào kỳ |
| Chứng từ gốc | Đang ở hiện trường | CS đã nhận | CS | — | Ghi người và giờ |
| Chứng từ gốc | CS đã nhận | Đã giao khách | CS | — | Gỡ cờ trên JobID |

### 6.3 State Transitions

**JobID** — SOP Điều phối có 3 trạng thái giữa; "Hoàn thành dịch vụ" theo Quy trình cung cấp dịch vụ tổng quát; "Chờ duyệt" và "Dừng - chờ khách thanh toán" là đề xuất đã chốt. "Đã tạo YCVT" do Điều phối (hoặc Điều vận với JobID không có thủ tục giao nhận) đổi; "Đã thực hiện Lệnh vận tải" do Điều vận đổi khi mọi Lệnh đã duyệt.

```
Chờ duyệt --Không đạt nợ, hạn mức--> Dừng - chờ khách thanh toán
   |                                     | khách thanh toán xong
   v Đạt                                 v
Chờ xử lý --> Đã tạo YCVT --> Đã thực hiện Lệnh vận tải --> Hoàn thành dịch vụ
```

- Chờ xử lý: CS đang hoàn thiện. Đã tạo YCVT: có ít nhất 1 YCVT. Đã thực hiện Lệnh vận tải: mọi Lệnh của JobID đã duyệt. Hoàn thành dịch vụ: CS xác nhận doanh thu; doanh thu, chi phí ghi vào kỳ.
- Huỷ chỉ khi còn "Chờ duyệt" hoặc "Chờ xử lý" mà chưa phân luồng. Sau mốc đó chỉ được sửa (đổi Booking Note, giảm số container — ở Điều phối).
- Dừng vì công nợ không có duyệt ngoại lệ; ở nguyên trạng thái tới khi khách trả, không tự huỷ.

**Chứng từ gốc phải chuyển (D9)**

```
Đang ở hiện trường --> CS đã nhận --> Đã giao khách
```

### 6.4 Interrupted Transactions

| # | Tình huống | Xử lý |
|---|---|---|
| 1 | AI không đọc được chứng từ (ảnh mờ, mẫu lạ) | Chuyển sang nhập tay, ảnh hiện bên cạnh. Đánh dấu "nhập thủ công" để thống kê |
| 2 | MISA chưa trả hoá đơn | Cờ "Chưa khớp hoá đơn điện tử", chụp và nhập tay (A9) |
| 3 | JobID dừng vì công nợ quá lâu | Ở nguyên "Dừng - chờ khách thanh toán", không tự huỷ. Nhắc CS sau bao lâu: OQ-42 |

### 6.5 Other Edge Cases

- CBT đổi bên xuất hoá đơn sau khi đã có Lệnh: đổi trên JobID, không huỷ Lệnh; bên thứ ba chưa có mã thì tạo việc "Đăng ký bên thanh toán" (D10).
- Hoàn thành dịch vụ khi còn Lệnh chưa duyệt hoặc doanh thu chưa xác nhận: chặn, chỉ ra phần thiếu.
- JobID có đánh dấu cần chuyển mã vạch gốc mà chưa giao khách: cờ ở bước ghi nhận doanh thu (D9).

## 7. Validation, Limits & Wording

### 7.1 Validation rules

Quy tắc chung (bắt buộc, độ dài, ngày, email, số điện thoại) theo GR và E-common, không viết lại.

| Field | Rule |
|---|---|
| Số container (khi tạo JobID) | 4 chữ cái + 7 số, đúng chữ số kiểm tra ISO 6346 |
| Cách trả chi phí | Bắt chọn có/không hoá đơn |

### 7.2 Limits & Quotas (exact values)

| Tham số | Giá trị | Window | Behavior khi vượt |
|---|---|---|---|
| Ngưỡng cách trả chi phí (`P-nguong-tam-ung`) | Delta: 5.000.000 ₫ | mỗi khoản | Dưới: tạm ứng; trên: tạo việc cho CS phụ trách + kế toán |
| Chia lãi giao dịch nội bộ (`P-ty-le-chia-lai-noi-bo`) | Delta: 50/50 lãi gộp | mỗi JobID trái tuyến | Chỉ hạch toán sau khi chốt bảng kê công nợ phải thu, phải trả |

### 7.3 Wording samples (exact strings)

Ngôi "bạn", câu ngắn, không "Vui lòng" (theo design.md). Loại hiển thị theo GR-15: Inline dưới trường, Popup chặn giữa màn, Toast góc màn.

#### Error messages

| Mã | Loại | Tình huống | Câu |
|---|---|---|---|
| E-service-delivery-001 | Inline | Số container sai chữ số kiểm tra khi tạo JobID | "Số container không đúng. Kiểm tra lại chữ số cuối." |
| E-common-009 | Toast | Mất mạng | Dùng câu chung |
| E-common-008 | Toast | Lỗi hệ thống | Dùng câu chung |

#### Success messages

- "Đã tạo JobID [mã]" · "Đã hoàn thành dịch vụ"

Xác nhận (Xem CMP-03):

| Tình huống | Tiêu đề · nội dung | Nút |
|---|---|---|
| Huỷ JobID | **Huỷ JobID [mã]?** · "JobID sẽ đóng, không thể hoàn tác." | [Huỷ JobID] [Quay lại] |

#### Info / neutral messages

| Tình huống | Câu |
|---|---|
| AI không đọc được | "Không đọc được chứng từ. Nhập tay theo ảnh bên cạnh." |
| JobID dừng | "Đang dừng: chờ khách thanh toán nợ quá hạn." |

### 7.4 Bối cảnh hệ thống (mức nghiệp vụ)

**Thông tin cần lưu**
- Trên JobID: chứng từ khách; phạm vi dịch vụ; chi phí, doanh thu (kéo về từ Lệnh và việc hiện trường); giao dịch nội bộ (chi nhánh nào làm phần nào); hoá đơn trả hộ; bên xuất hoá đơn; cờ (chưa khớp hoá đơn điện tử, chưa có đơn giá, cần chuyển mã vạch gốc, hoá đơn trả hộ khách không xác nhận). Mốc, chứng từ vận hành và người giữ quyền thanh toán do Điều phối ghi.
- Lịch sử: ai tạo, ai đổi trạng thái; chỗ AI đọc sai đã được người sửa; số lần phải nhập thủ công.

**Dịch vụ bên ngoài**

| Dịch vụ | Mục đích | Tình trạng |
|---|---|---|
| MISA | Lấy hoá đơn điện tử | Chưa rõ lấy được hoá đơn đầu vào (OQ-23) |
| AI đọc chứng từ | Đọc chứng từ khách khi tạo JobID | Trong phạm vi |
| Ngân hàng (API, QR) | Thanh toán trả hộ | Feature riêng |

**Thông báo**

| Ai nhận | Khi nào | Kênh |
|---|---|---|
| CS | JobID dừng vì công nợ; có việc "Đăng ký bên thanh toán" | Thông báo đẩy + "Việc của tôi" |
| CS phụ trách, kế toán | Khoản chi từ `P-nguong-tam-ung` trở lên | Thông báo đẩy + "Việc của tôi" |

**Việc phần mềm tự chạy theo giờ:** kiểm lại JobID đang dừng khi khách thanh toán · nhắc CS JobID dừng quá lâu (OQ-42).

## 8. Assumptions

- SOP của Delta là thiết kế to-be của khách, không phải cách đang làm.
- Bảng kê, công nợ và kết nối MISA (ngoài lấy hoá đơn) là feature riêng; feature này chỉ đảm bảo doanh thu, chi phí đủ và đúng JobID.

## 9. Risks

| Rủi ro | Khả năng | Hậu quả nghiệp vụ | Cách phòng |
|--------|----------|-------------------|-----------|
| AI đọc sai chứng từ khi tạo JobID (số container, tên kho) | thỉnh thoảng | Đi nhầm kho; dữ liệu sai lan sang Điều phối, Điều vận | Người tạo bắt buộc xác nhận; kiểm chữ số container |
| Thiếu tài liệu khách: phụ lục bảng kê doanh thu, chi phí; quy trình quản lý quỹ và thanh toán | thường | Ghi nhận chi phí, doanh thu sai cấu trúc bảng kê | Bám OQ-5, OQ-7 |
| Chưa lấy được hoá đơn đầu vào từ MISA | thỉnh thoảng | Nhập tay hoá đơn nhiều, dễ sai | Cờ "Chưa khớp hoá đơn điện tử" (A9); chờ OQ-23 |

## 10. Success Criteria (preliminary)

Mỗi tiêu chí gắn một vấn đề ban đầu. Số hiện trạng và mục tiêu chờ khách (OQ-44).

| Vấn đề | Tiêu chí | Mục tiêu |
|---|---|---|
| a. Nhập lại nhiều lần | Tỉ lệ trường tự điền khi tạo JobID (AI đọc) trên tổng trường phải nhập | ? |
| e. Chi phí thiếu | Tỉ lệ JobID lập bảng kê không bị thiếu chi phí | ? |

## 11. Open Questions

Nguồn khách: tên tài liệu khách gửi và mục. Cột Trả lời theo biên bản [[docs/meetings/2026-10-10-oq-dispatch-coordination.md|Delta trả lời vòng 1]] (anh Nghĩa, 10/10/2026) và 2 điểm xác nhận lại ngày 12/10/2026.

| Mã | Câu hỏi | Nguồn khách | Trả lời |
|---|---|---|---|
| OQ-4 | Cách phân chia lợi nhuận nội bộ giữa các chi nhánh chưa chốt | Quy trình cung cấp dịch vụ tổng quát | Đã chốt: chia theo lãi gộp 50/50, sau khi chốt bảng kê công nợ phải thu, phải trả (B7) |
| OQ-5 | Phụ lục bảng kê doanh thu, chi phí còn trống | Quy trình cung cấp dịch vụ tổng quát, phụ lục | Còn mở: Delta gửi dần phụ lục |
| OQ-6 | Chưa có cách xử lý bồi thường nội bộ khi khách từ chối trả hộ do lỗi nhân viên | Quy trình cung cấp dịch vụ tổng quát, mục 5.3–5.5 | Một phần: khi lập bảng kê, phần mềm đánh dấu hoá đơn trả hộ khách không xác nhận thanh toán (E9). Quy trình xử lý Delta sẽ phát triển |
| OQ-7 | Quy trình quản lý quỹ và thanh toán chưa phát triển | Quy trình cung cấp dịch vụ tổng quát | Còn mở: Delta đang hoàn thiện |
| OQ-9 | Định danh JobID đường sắt thế nào? | Giao nhận hàng hoá (18/9/2026) | Còn mở: Delta làm rõ trong tài liệu JobID |
| OQ-11 | Lệch báo cáo quản trị và báo cáo thuế ở hàng CBT, cần kế toán xác nhận | Giao nhận hàng hoá (18/9/2026) | Đã chốt: chấp nhận lệch về hình thức; báo cáo quản trị phản ánh đúng thực tế giao dịch |
| OQ-16 | JobID có được chia sẻ hoặc chuyển sang chi nhánh khác không, thao tác ra sao? | Quy trình cung cấp dịch vụ tổng quát, mục 5.5 | Đã chốt: theo 2 trường hợp giao dịch nội bộ trong SOP; JobID trái tuyến hoặc giao việc trái tuyến thì phần mềm tự ghi nhận, tự hạch toán (B7) |
| OQ-17 | Quy mô: JobID mỗi ngày, số lái xe, nhân viên hiện trường, CS, điều vận theo chi nhánh | Chưa có trong tài liệu khách gửi | Một phần: ~110.000 lô hàng/năm (= số Lệnh vận tải), ~50.000 tờ khai/năm (= số JobID J01–J06), tăng 2 con số mỗi năm. Chi nhánh Hà Nội, Vận Tải (VT), Bắc Ninh (BN), Hải Dương (HD, sẽ giải thể do sáp nhập tỉnh) gấp 3–4 lần TP.HCM về sản lượng, doanh thu; không có chi nhánh Hải Phòng. Còn thiếu: số người theo chi nhánh |
| OQ-23 | Gói MISA có lấy đủ hoá đơn đầu vào không? Hoá đơn trả hộ ghi mã số thuế của ai? | Quy trình cung cấp dịch vụ tổng quát | Còn mở: Delta đánh giá cao hướng lấy hoá đơn từ MISA, đang xem xét |
| OQ-29 | Lưu bằng chứng khách đồng ý khoản chi ngoài định mức bằng cách nào: khách bấm trên app, ảnh tin nhắn/email, link xác nhận, hay ghi chú đã gọi? | Giao nhận hàng hoá (18/9/2026) | Ngoài phần mềm: ghi nhận, chi trả qua Quy trình cung cấp dịch vụ hoặc thanh toán không hoá đơn (E1) |
| OQ-31 | Bảng loại phí × địa điểm → cách hạch toán (thu nhập chịu thuế lái xe / chi hộ / trả hộ / chi phí vận hành) cho các tuyến ngoài đường sắt | Giao nhận hàng hoá (18/9/2026) | Còn mở: Delta làm rõ luồng dữ liệu Cung cấp dịch vụ, Điều phối, Điều vận và bút toán đối ứng |
| OQ-36 | Ai duyệt mã khách DK05 cấp 2 khi CBT đổi pháp nhân thanh toán sang bên mới? | Giao nhận hàng hoá (18/9/2026) | Chưa hỏi Delta (ngoài deck vòng 1) |
| OQ-42 | JobID dừng vì nợ quá hạn, vượt hạn mức có cần nhắc CS sau một số ngày không? Bao nhiêu ngày, nhắc ai? | Chưa có trong tài liệu khách gửi | Chưa hỏi Delta (ngoài deck vòng 1) |
| OQ-44 | Số hiện trạng và mục tiêu cho các tiêu chí thành công của 3 feature: tỉ lệ trường tự điền; tỉ lệ việc hiện trường giao, nhận trên app; số lần và tiền phạt lưu container, lưu vỏ, lưu xe mỗi tháng; thời gian từ xe xong việc tới duyệt Lệnh; tỉ lệ Lệnh duyệt đủ chi phí | Chưa có trong tài liệu khách gửi | Chưa hỏi Delta (ngoài deck vòng 1) |

## 12. Next Steps

Đã tách từ brainstorm Điều phối gộp ngày 2026-10-12. Tiếp theo:
- Hỏi lại Delta các câu còn mở ở Mục 11 (BL-041)
- `/user-flow service-delivery` — chạy lại; userflow tách máy từ bản nháp ngày 07/10, còn nội dung cũ
- `/srs service-delivery` — đặc tả FR, BR, Error Matrix
