---
type: brainstorm
feature: transport-dispatch
status: draft
updated: 2026-10-12
links:
  - docs-input/sop/giao-nhan-hang-hoa/giao-nhan-hang-hoa.md
  - docs-input/sop/sop-dieu-phoi.md
  - docs-input/sop/quan-ly-hoa-don-sim/quan-ly-hoa-don-sim.md
  - docs-input/sop/vis-du-lieu-van-hanh-xe/vis-du-lieu-van-hanh-xe.md
  - docs-input/sop/eup-dieu-van-2026-09-19/eup-dieu-van-2026-09-19.md
  - docs-input/sop/sop-ban-do-kien-thuc.md
  - docs/_research/2026-10-02-container-deadline-alerts.md
  - docs/_research/2026-10-02-electronic-delivery-record.md
  - docs/_shared/project-profile.md
  - docs/meetings/decks/2026-10-06-oq-dispatch-coordination-deck.md
  - docs/meetings/2026-10-09-client-dispatch-field-issues.md
  - docs/meetings/2026-10-10-oq-dispatch-coordination.md
  - docs/service-delivery/brainstorms/service-delivery.md
  - docs/shipment-coordination/brainstorms/shipment-coordination.md
---

# Điều vận — Lệnh vận tải từ YCVT đến khi duyệt

> Phỏng vấn xong đủ 7 phần ngày 2026-10-07 (chung với Điều phối và Cung cấp dịch vụ), cập nhật 2026-10-12 theo trả lời của Delta cho bộ câu hỏi vòng 1 (biên bản 2026-10-10) và trao đổi với khách 09/10.
> Tách ngày 2026-10-12 theo SOP: Quy trình cung cấp dịch vụ tổng quát ([[docs/service-delivery/brainstorms/service-delivery.md|service-delivery]]) · Quy trình điều phối ([[docs/shipment-coordination/brainstorms/shipment-coordination.md|shipment-coordination]]) · Quy trình điều vận (feature này, Delta chưa gửi SOP — OQ-1). Mã ý tưởng (A1, B7…), DP-nn và OQ-n giữ nguyên số của bản gộp.

## 1. Idea Seed

Điều vận nhận YCVT đủ dữ liệu từ Điều phối (hoặc thẳng từ JobID với CBT, đường sắt), lập Lệnh trên một màn theo dõi xếp xe, lái xe chạy Lệnh trên app: chụp ảnh tại điểm, nhật ký nhiệt, ghi chi phí, biên bản giao hàng. Lệnh lưu cả kế hoạch và thực tế; quá mốc thì cảnh báo, leo thang. Lệnh duyệt xong thì chi phí đã nằm đúng JobID.

## 2. Context

**Vấn đề hiện tại feature này xử lý (khách xác nhận):**

| Mã | Vấn đề |
|---|---|
| b | Giao việc qua điện thoại, Zalo; không truy được ai đang giữ việc (giao Lệnh, báo vấn đề giữa chặng) |
| c | Không thấy trước mốc cắt máng, cut-off, lưu container, lưu vỏ nên bị phạt |
| d | Chứng từ giấy về chậm nên chốt Lệnh và tính chi phí chậm |
| e | Chi phí chưa được hạch toán rõ ràng, đầy đủ (chi phí trên Lệnh) |

**Phạm vi:**
- Gồm: Màn theo dõi xếp xe, lập Lệnh, gợi ý ghép hàng và hàng chiều về; lái xe chạy Lệnh (ảnh định vị, nhật ký nhiệt, chi hộ, cân xe, biên bản giao hàng); thay đổi giữa chặng, mooc, nhiên liệu; chốt và duyệt Lệnh; cảnh báo quá mốc; CBT và đường sắt (Lệnh hàng loạt).
- Ranh giới với 2 feature cùng chuỗi:
  - Điều phối (`shipment-coordination`): sinh YCVT, ghi mốc, nơi nhận lấy từ D/O. Màn "Việc của tôi" (web, mobile) vẽ đầy đủ ở đó, feature này dùng chung.
  - Cung cấp dịch vụ tổng quát (`service-delivery`): tạo JobID (CBT, đường sắt đi thẳng sang đây), quy tắc thanh toán chi phí và Yêu cầu thanh toán (E2, E6), hoàn thành dịch vụ.
- CBT và đường sắt không đi qua Điều phối (Delta, 10/10/2026). Mỗi loại JobID có giao diện riêng, kéo theo Yêu cầu vận tải và Lệnh riêng. Chi tiết chờ Quy trình điều vận (OQ-1). Mục 5.3, 5.4 và D6–D8, E3, E4, E8 dựa trên SOP Giao nhận hàng hoá.
- Không gồm (feature riêng): shipment list, bảng kê đường sắt; ghi nhận và bù dầu ngoài Lệnh (module Vận tải / Cấp dầu); quản lý danh mục điểm chụp ảnh, loại phí.
- Ngoài giai đoạn 1: quản lý vỏ container (chi phí sửa vỏ vẫn ghi trên Lệnh).
- Xử lý ngoài phần mềm: tiền hoàn nâng vỏ; quá mốc do kẹt xe, sự cố đường.
- Ứng dụng: Delta Super App, dùng chung cho nhân viên Delta và nhân viên đối tác/khách; web cho điều vận, mobile cho lái xe.

**Nguồn:** Giao nhận hàng hoá 18/9/2026, Quy trình điều phối (các mục dẫn chiếu Lệnh vận tải), tài liệu Hoá đơn trả hộ 01/10/2026, Dữ liệu vận hành xe 30/9/2026, EUP điều vận 19/9/2026, trao đổi với khách 09/10/2026, 2 báo cáo điều tra trong `docs/_research/`.

**Nhãn đề xuất:** [SOP to-be] = SOP đã yêu cầu, phần mềm làm theo · [SOP+] = SOP có nêu, đề xuất làm thêm · [Mới] = SOP chưa có. Chỉ [SOP+] và [Mới] tính là điểm khác biệt.

## 3. User Types (preliminary)

Phân quyền theo chức năng ("quyền lái xe"…), không cố định vai trò. Luồng và sơ đồ vẫn ghi theo vai trò nghiệp vụ.

| User Type | Pain Point | Primary Need |
|-----------|-----------|--------------|
| Điều vận | Xếp xe bằng bảng tính + Zalo; không thấy trước mốc phạt | Màn theo dõi xếp xe có đủ dữ liệu để quyết định |
| Trưởng điều vận | Không biết cảnh báo nào bị bỏ sót | Nhận cảnh báo leo thang; duy trì danh sách điểm chụp ảnh |
| Lái xe | Gửi ảnh, nhiệt độ, chi phí qua Zalo; phải nhớ điểm cần chụp | Nhận Lệnh, chụp ảnh, thao tác nhanh trên Lệnh |
| Cán bộ quản lý | Duyệt bằng tin nhắn | "Việc của tôi" để duyệt Lệnh |
| CS | Xe đi khi hàng air chưa đủ kiện | Quyết định "khai theo số đã về" hoặc "chờ đủ"; nhập đơn giá đường sắt |
| Kế toán | Chi phí về muộn, thiếu, không gắn JobID | Chi phí đã gắn đúng Lệnh |
| Đại diện khách hàng | Phải gọi CS hỏi tình trạng | Theo dõi lô, nhận biên bản giao hàng, file nhật ký nhiệt |
| Trợ lý AI | — | Gợi ý ghép hàng, hàng chiều về, xe phù hợp |

### 3.1 Tác vụ chính

Tần suất chưa đo được, ghi định tính. Dòng có ★ là tác vụ phải tối ưu cho thao tác nhanh nhất.

| Vai trò | Tác vụ | Tần suất | Mức quan trọng | Ghi chú |
|---------|--------|----------|----------------|---------|
| Điều vận | ★ Màn theo dõi xếp xe: tạo Lệnh, xếp xe và lái xe, Lệnh đường sắt hàng loạt, ghép hàng lẻ, xử lý cảnh báo quá mốc | Liên tục trong ca | cao | Trễ cut-off; xe chạy rỗng chiều về; chi phí mất kiểm soát |
| Lái xe | ★ Nhận Lệnh, chụp ảnh, thao tác nhanh trên Lệnh (nhật ký nhiệt, chi hộ, chuyển bước) | Nhiều lần mỗi chuyến | cao | Thiếu bằng chứng khi tranh chấp; hỏng hàng lạnh không truy được trách nhiệm |
| Cán bộ quản lý | ★ Việc của tôi: duyệt Lệnh, xem cảnh báo | Vài lần mỗi ngày | trung | Lệnh duyệt chậm thì chi phí lên JobID chậm |
| CS | Xử lý air chưa đủ kiện; nhập đơn giá đường sắt | Vài lần mỗi ngày | trung | Xe đi khi hàng chưa sẵn sàng; chặn chốt kỳ |

## 4. Capabilities Breakdown

### P0 — must have

**Luồng lõi:** nhận YCVT → lập Lệnh → chạy Lệnh → chốt, duyệt Lệnh → chi phí lên JobID (Mục 5).

**Nhóm A — giảm nhập liệu**
- A7 [SOP+] [Lõi] [Cấu hình] Biên bản giao hàng có cấu trúc trên app, tự điền từ Lệnh, bắt ghi có/không bất thường + ảnh trước khi rời điểm, chạy được khi mất sóng. Mẫu theo 5 loại hàng. Hình thức ký theo `P-hinh-thuc-ky-bien-ban` (Delta: ký điện tử trên máy lái xe + biên bản giấy, để khách chuyển đổi dần). [Mới] Lái xe xác nhận biên bản khách đã ký thì phần mềm tự email biên bản cho CS và khách ngay, chống giao lận — theo `P-email-bien-ban-giao-hang` (Delta: bật).

**Nhóm B — quy trình**
- B5 [SOP+] [Lõi] [Cấu hình] Phí đổi vỏ ghi chi phí phát sinh của Lệnh. Theo dõi tiền nâng vỏ chờ hoàn, cảnh báo sau `P-han-hoan-tien-nang-vo` (Delta: không dùng), bật/tắt theo `P-theo-doi-tien-hoan-nang-vo` (mặc định sản phẩm bật; Delta: tắt — khoản này đã nằm trong dư nợ tạm ứng của nhân viên nghiệp vụ, lái xe; cá nhân tự xử lý).
- B6 [SOP+] [Lõi] Cảnh báo quá mốc: bắt chọn nhóm nguyên nhân (thêm nhóm "do nhà vận tải"), văn bản soạn sẵn báo khách/hãng tàu, mỗi cảnh báo có người phụ trách + trạng thái "đã xử lý"; gửi qua email, copy nội dung hoặc xuất file. Leo thang lên trưởng điều vận. Quá mốc do kẹt xe, sự cố đường xử lý ngoài phần mềm, không thêm nhóm nguyên nhân.

**Nhóm D — từ SOP Giao nhận hàng hoá**
- D1 [SOP+] [Lõi] [Cấu hình] Danh sách điểm chụp ảnh định vị bắt buộc theo loại hàng; ảnh tự gắn vị trí, giờ vào Lệnh; thiếu ảnh thì chặn bước tiếp. Trưởng điều vận duy trì danh sách.
- D2 [SOP+] [Gói: Hàng lạnh] [Cấu hình] Nhật ký nhiệt độ hàng lạnh: chu kỳ nhắc theo `P-chu-ky-nhac-nhiet` (Delta: chưa chốt, OQ-43) theo loại hàng, chỉnh được trên từng Lệnh; quá giờ chưa nhập thì cảnh báo điều vận; khách nhận qua file xuất. Yêu cầu chỉnh nhiệt vẫn nhắn qua kênh ngoài; lái xe ghi "đã chỉnh" + lý do, không bắt ảnh.
- D3 [SOP+] [Lõi] Air nhập chưa về đủ kiện thì chặn giao xe tới khi CS chọn "Khai theo số kiện đã về" hoặc "Chờ đủ hàng"; lô tách chuyến thành nhiều Lệnh dưới 1 JobID. Kho CFS chưa xác nhận hàng sẵn sàng thì chỉ cảnh báo.
- D5 [SOP+] [Lõi] Gợi ý ghép hàng lẻ và hàng air chung xe (cùng kho/kho gần, giờ cut-off, CBM/trọng lượng so với tải xe); điều vận bấm chọn.
- D6 [SOP+] [Gói: Đường sắt] Đường sắt: nhập kế hoạch nhà ga theo mẫu file (mẫu đầu tiên: Ratraco) ngày n (nhận ngày n-1), sinh Lệnh hàng loạt; xuất "Kế hoạch xe theo ga" gửi trưởng ga (chỉ nhận file); gợi ý nơi lấy vỏ theo thứ tự ưu tiên SOP.
- D7 [SOP+] [Gói: Đường sắt] [Cấu hình] Lệnh đường sắt hoàn tất tự vào shipment list đúng kỳ `P-ky-chot-duong-sat` (Delta: ngày 25 / cuối tháng). Màn shipment list, bảng kê là feature riêng.
- D8 [Mới] [Gói: CBT] Gợi ý hàng chiều về cho xe CBT sắp trả hàng ở miền Nam, miền Trung.

**Nhóm E — chi phí trên Lệnh (vấn đề e)**
- E3 [SOP+] [Gói: Đường sắt] [Cấu hình] Đơn giá đường sắt lấy theo `P-nguon-don-gia-duong-sat` (Delta: giai đoạn 1 CS nhập tay, giai đoạn 2 báo giá Sales). Nhập tay qua việc "Xác định giá"; Lệnh chưa có giá mang cờ "Chưa có đơn giá", còn cờ thì chặn chốt kỳ.
- E4 [SOP to-be] [Lõi] Lái xe ghi chi hộ (vd Ratraco), cân xe ngay trên Lệnh (loại phí, số tiền, ảnh); phần mềm gom bảng kê chi phí cho điều vận xác nhận, gắn nhãn "chi hộ — phải thu lại"; cân xe chọn "khách trả trực tiếp" hoặc "công ty trả".
- E5 [SOP to-be] [Lõi] [Cấu hình] [Riêng Delta] Danh mục loại phí có cách hạch toán theo địa điểm; lái xe chỉ chọn loại phí, phần mềm tự xếp và tự điền định mức từ danh mục định mức của khách (dữ liệu Riêng Delta: 150.000 ₫ Nam Khánh, 160.000 ₫ Phú Lợi).
- E7 [SOP to-be] [Lõi] Hiện trên Lệnh dữ liệu GPS: giờ đến thật, vé trạm, cờ tránh trạm, thời gian kẹt xe; dữ liệu kẹt xe gắn làm bằng chứng vào cảnh báo quá mốc.
- E8 [SOP+] [Gói: CBT] [Cấu hình] Phí lưu ca xe CBT ghi nhận lên Lệnh. Đề xuất đồng hồ từ giờ đến tới giờ khởi hành, quá `P-gio-mien-phi-luu-xe` (Delta: 72 giờ) tự đề xuất dòng phí, CS xác nhận; chờ khách trả lời có cần phần mềm tự tính không (OQ-33). Phí chạy máy phát chờ giải pháp của khách.
- Cách trả chi phí theo ngưỡng (E2) và nút Yêu cầu thanh toán (E6) xem `service-delivery`; màn Yêu cầu thanh toán của lái xe vẽ ở feature này.

**Nhóm F — thay đổi giữa chặng, mooc, nhiên liệu (trao đổi với khách 09/10)**
- F1 [Mới] [Lõi] [Cấu hình] Lái xe báo vấn đề hoặc chỗ lệch kế hoạch ngay giữa chặng trên app, thay cho báo qua kênh ngoài. Thay đổi cần ghi: cung đường, thời gian giao, đi công suất, khách muốn đi cao tốc, sự cố đường về, khách báo thiếu hàng, khách huỷ vì hàng chưa sẵn sàng, đổi điểm giao.
- F2 [Mới] [Lõi] Mọi thay đổi so với kế hoạch và mọi vấn đề phát sinh đều báo tới điều vận và quản lý. Lệnh lưu cả kế hoạch và thực tế.
- F3 [Mới] [Lõi] Đổi cung đường: chi phí phát sinh công ty chịu, lượng dầu cấp cho Lệnh điều chỉnh theo.
- F4 [Mới] [Lõi] Mooc trên Lệnh được khác mooc đang móc trên xe; đổi mooc thì ghép hàng – xe đổi theo.
- F5 [Mới] [Lõi] Bỏ mooc giữa đường (hi hữu): điều xe khác ra kéo tiếp.
- F6 [Mới] [Lõi] [Gói: Nhiên liệu] Cấp dầu trên Lệnh gắn với định mức phương tiện; vượt định mức đi phiếu cấp nhiên liệu riêng như hiện có (loại phiếu theo danh mục của khách). [Gói: Nhiên liệu] Dầu mua ngoài theo hoá đơn lẻ: lưu lượng dầu dư làm căn cứ tạo phiếu cấp bù (hiện chưa lưu).
- F7 [Mới] [Lõi] Hạn chuẩn bị giấy tờ đặt theo từng Lệnh.
- F8 [Mới] [Lõi] Toạ độ và chi phí đường bộ lấy VETC làm nguồn chuẩn khi lệch với Vietmap.

### P1 — should have

Chưa phân mức: mọi đề xuất đã chốt ở trên đều làm ngay giai đoạn này.

### P2 — nice to have

- F9 [Mới] [Lõi] Điều phối Lệnh có AI hỗ trợ, kiểu ứng dụng gọi xe: phần mềm đề xuất xe phù hợp, điều vận chốt.

## 5. Core Flows (Happy Path)

### 5.1 Luồng tổng (xương sống chung của 3 feature)

0. **Tạo và duyệt JobID** — `service-delivery`. JobID không có thủ tục giao nhận (CBT, đường sắt, không làm hiện trường) đi thẳng sang bước 5.
1–4. **Điều phối** — `shipment-coordination`: hoàn thiện dữ liệu, giao việc hiện trường, sinh YCVT.
5. **Lập Lệnh vận tải** — điều vận gán xe, lái xe, cung đường.
6. **Chạy Lệnh** — lái xe nhận Lệnh, chụp ảnh điểm bắt buộc, nhật ký nhiệt, ghi chi hộ; GPS tự đánh dấu "đã đến"; quá mốc thì cảnh báo, leo thang.
7. **Chốt và duyệt Lệnh** — thiếu việc, chứng từ, chi phí thì chặn chốt; duyệt xong chi phí lên JobID.
8. **Hoàn thành dịch vụ** — `service-delivery`.

Ký hiệu: `[Vai trò]` người làm · `(PM)` phần mềm tự làm · `<…?>` điểm rẽ nhánh.

```
YCVT (từ shipment-coordination, hoặc thẳng từ JobID CBT / đường sắt)
   |
   v
5. LẬP LỆNH VẬN TẢI
   (đường sắt: sinh Lệnh hàng loạt từ kế hoạch Ratraco ngày n-1)
[Điều vận] Màn theo dõi xếp xe: gán xe, lái xe, cung đường
(PM) Gợi ý ghép hàng lẻ, gợi ý hàng chiều về cho xe CBT
<Air nhập chưa về đủ kiện?> --Có--> chặn giao xe --> [CS] "Khai theo số đã về" / "Chờ đủ"
<Kho CFS chưa sẵn sàng?>    --Có--> cảnh báo, vẫn giao xe được
   |
   v
6. CHẠY LỆNH
[Lái xe] Nhận Lệnh -> chụp ảnh tại từng điểm bắt buộc (thiếu ảnh: không qua bước tiếp)
         -> nhật ký nhiệt (hàng lạnh) -> ghi chi hộ / tạo yêu cầu thanh toán
(PM) GPS tự đánh dấu "đã đến", hiện vé trạm
(PM) Quá mốc --> cảnh báo điều vận --> chưa xử lý --> leo thang trưởng điều vận
[Lái xe] Lệch kế hoạch giữa chặng --> báo trên app --> (PM) báo điều vận, quản lý (F1, F2)
[Hiện trường] Hàng lẻ / air: phiếu nhập kho, phiếu cân, phiếu xuất kho (shipment-coordination)
[CS hoặc Lái xe] Lệnh hạ hàng / hạ vỏ (cảng có ePort: CS; không có: lái xe)
   |
   v
7. CHỐT LỆNH
[Lái xe] Chốt --> <Thiếu việc / chứng từ / chi phí?> --Có--> chặn, chỉ ra phần thiếu
   | Không
   v
[Điều vận / Cán bộ QL] Duyệt Lệnh --> (PM) chi phí trên Lệnh chuyển lên JobID
   |
   v
Mọi Lệnh của JobID đã duyệt --> JobID "Đã thực hiện Lệnh vận tải" --> service-delivery (bước 8)
```

### 5.2 Lệnh theo loại hàng FCL, LCL, CFS, air

Thứ tự việc của lái xe theo từng loại hàng vẽ ở `shipment-coordination` Mục 5.2–5.7 (theo SOP điều phối). Feature này dùng các điểm đó làm danh sách điểm chụp ảnh bắt buộc (D1) và mẫu biên bản giao hàng (A7).

### 5.3 CBT

Không đi qua Điều phối (Delta, 10/10/2026). Thứ tự bước giữa chờ Quy trình điều vận (OQ-1).

```
(PM) JobID J07 --> YCVT ngay (bỏ qua bước 1-4)
[Điều vận] Lập Lệnh
[Lái xe] đến vựa: chụp đầu + đuôi xe --> đóng hàng --> nhật ký nhiệt theo chu kỳ của loại hàng
   --> đến cửa khẩu: chụp ảnh --> giao hàng
(PM) Phí lưu ca xe ghi lên Lệnh (tự tính quá 72h: chờ OQ-33)
(PM) Xe sắp trả hàng ở miền Nam / Trung --> gợi ý hàng chiều về
--> Chốt Lệnh
```

### 5.4 Đường sắt

Không đi qua Điều phối (Delta, 10/10/2026). Thứ tự bước giữa chờ Quy trình điều vận (OQ-1).

```
[Điều vận] Nhập kế hoạch Ratraco ngày n (nhận từ ngày n-1) --> (PM) sinh Lệnh hàng loạt
[Điều vận] Xếp xe, lái xe
   (PM) gợi ý nơi lấy vỏ: theo kế hoạch Ratraco -> tồn vỏ tại ga -> vị trí xe đang đậu
(PM) Xuất "Kế hoạch xe theo ga" --> gửi trưởng ga (email / copy / file)
[Lái xe] Chạy Lệnh, ghi chi hộ Ratraco / cân xe (loại phí, số tiền, ảnh)
Chưa có giá --> cờ "Chưa có đơn giá" + việc "Xác định giá" --> [CS] nhập đơn giá tay (giai đoạn 1)
--> Chốt Lệnh --> (PM) vào shipment list kỳ 25 / cuối tháng
                  còn cờ "Chưa có đơn giá" --> chặn chốt kỳ
```

## 6. System Behavior Deep Dive

### 6.1 Decision Points

| ID | Flow | Khi nào | YES (nhánh đồng ý) | NO (nhánh từ chối) |
|---|---|---|---|---|
| DP-07 | Air nhập | Đã về đủ kiện | Giao xe | Chặn giao xe tới khi CS chọn cách xử lý |
| DP-08 | CFS nhập | Kho xác nhận hàng sẵn sàng | Giao xe | Cảnh báo, vẫn giao xe được |
| DP-09 | Chạy Lệnh | Đủ ảnh tại điểm bắt buộc | Qua bước tiếp | Chặn bước tiếp |
| DP-11 | Chốt Lệnh | Đủ việc, chứng từ, chi phí | Chờ duyệt | Chặn chốt, chỉ ra phần thiếu |
| DP-12 | Đường sắt | Lệnh có đơn giá | Vào kỳ chốt | Cờ "Chưa có đơn giá", chặn chốt kỳ |

### 6.2 Scenario Matrix

Ai được đổi trạng thái gì, ở trạng thái nào.

| Đối tượng | Từ | Sang | Ai làm | Điều kiện | Kết quả |
|---|---|---|---|---|---|
| YCVT | Đã được tạo | Đã lập Lệnh vận tải | Điều vận | Lập đủ số Lệnh đã khai | Hiện "đã lập x/n Lệnh" tới khi đủ |
| Lệnh | Đã lập | Huỷ | Điều vận | Lái xe chưa nhận | Trả số xe lại cho YCVT |
| Lệnh | Đã giao lái xe | Đã lập | Lái xe | Từ chối, bắt chọn lý do | Báo điều vận giao lại |
| Lệnh | Lái xe đã nhận | Đang thực hiện | Phần mềm hoặc lái xe | GPS ghi nhận xe khởi hành; không có GPS thì lái xe bấm "Bắt đầu" | Bắt đầu theo dõi mốc |
| Lệnh | Đang thực hiện | Lái xe đã chốt | Lái xe | Đủ ảnh, chứng từ, chi phí | Chờ duyệt |
| Lệnh | Lái xe đã chốt | Đã duyệt | Điều vận hoặc cán bộ quản lý (1 người là đủ) | — | Chi phí chuyển lên JobID |
| Lệnh | Lái xe đã chốt | Đang thực hiện | Điều vận hoặc cán bộ quản lý | Trả lại, bắt ghi lý do | Lái xe bổ sung |
| JobID | Đã tạo YCVT | Đã thực hiện Lệnh vận tải | Phần mềm | Mọi Lệnh của JobID đã duyệt | Sang `service-delivery` để hoàn thành dịch vụ |
| Cảnh báo | Mới | Đã có người nhận | Điều vận hoặc CS | Ai bấm "Nhận xử lý" trước giữ việc | Hiện tên người giữ |
| Cảnh báo | Đã có người nhận | Đã xử lý | Người giữ cảnh báo | Bắt chọn nhóm nguyên nhân | Đóng cảnh báo |
| Cảnh báo | Mới / Đã có người nhận | Đã leo thang | Phần mềm | Quá hạn chưa xử lý | Báo trưởng điều vận |

### 6.3 State Transitions

**Lệnh vận tải** — SOP chưa định nghĩa (OQ-1), toàn bộ là đề xuất đã chốt.

```
Đã lập --> Đã giao lái xe --> Lái xe đã nhận --> Đang thực hiện --> Lái xe đã chốt --> Đã duyệt
  |              |                                                       |
  v              v                                                       | Duyệt trả lại (ghi lý do)
 Huỷ        Lái xe từ chối --> về "Đã lập"                                v
(trước khi lái xe nhận)                                            Đang thực hiện
```

**Cảnh báo mốc**

```
Mới --> Đã có người nhận --> Đã xử lý (bắt chọn nhóm nguyên nhân)
  |            |
  +------------+-- Quá hạn chưa xử lý --> Đã leo thang (trưởng điều vận)
```

Vòng đời YCVT xem `shipment-coordination` Mục 6.3; feature này đổi YCVT sang "Đã lập Lệnh vận tải" và "Đã thực hiện Lệnh vận tải".

### 6.4 Interrupted Transactions

| # | Tình huống | Xử lý |
|---|---|---|
| 1 | Mất sóng hoặc tắt app khi lái xe đang chụp ảnh, ghi biên bản, nhập nhiệt độ | Lưu trên máy, tự đồng bộ khi có sóng. Giờ và vị trí lấy theo lúc chụp, không phải lúc gửi. Lệnh hiện nhãn "Chờ đồng bộ" |
| 2 | GPS mất tín hiệu | Không tự đánh dấu "đã đến"; lái xe bấm tay kèm ảnh định vị. Hết dữ liệu GPS cho Lệnh thì báo điều vận |
| 3 | Hai điều vận cùng lập Lệnh từ 1 YCVT khi chỉ còn 1 xe | Người lưu trước được; người sau nhận E-transport-dispatch-004 |
| 4 | Hai người cùng xử lý một cảnh báo | Ai bấm "Nhận xử lý" trước giữ việc; người sau thấy tên người đang giữ (E-transport-dispatch-005) |
| 5 | D/O đổi kho khi xe đang chạy | Lệnh cập nhật nơi nhận, báo điều vận và lái xe (D4 ở `shipment-coordination`) |
| 6 | Sửa JobID (đổi Booking Note, giảm container) khi đã có Lệnh | Lệnh dư chưa giao lái xe thì tự huỷ; đã giao thì báo điều vận xử lý tay |

### 6.5 Other Edge Cases

- Air nhập tách chuyến bay: mỗi đợt hàng về là 1 Lệnh mới dưới cùng JobID.
- Mất sóng tại điểm giao: biên bản giao hàng vẫn ghi được, đồng bộ sau.
- Thay đổi giữa chặng (cung đường, giờ giao, điểm giao, khách huỷ, thiếu hàng): ghi trên Lệnh, báo điều vận và quản lý, kéo theo chi phí, dầu, chứng từ (F1–F3).
- Hàng quay cắt: chưa rõ tình huống và cách xử lý xe, hàng (OQ-45).

## 7. Validation, Limits & Wording

### 7.1 Validation rules

Quy tắc chung (bắt buộc, độ dài, ngày, email, số điện thoại) theo GR và E-common, không viết lại.

| Field | Rule |
|---|---|
| Số kiện đã về | Số nguyên, không lớn hơn tổng số kiện |
| Nhiệt độ | Số thập phân 1 chữ số, cho phép số âm |
| Khoản chi trên Lệnh | Bắt buộc loại phí, số tiền lớn hơn 0, ảnh chứng từ; bắt chọn có/không hoá đơn |
| Số xe trên YCVT | Số nguyên ≥ 1 |
| Nơi nhận trên Lệnh | Lấy từ D/O, không nhập tay |
| Lý do bắt buộc | Lái xe từ chối Lệnh · trả lại Lệnh · nguyên nhân quá mốc |

### 7.2 Limits & Quotas (exact values)

| Tham số | Giá trị | Window | Behavior khi vượt |
|---|---|---|---|
| Lưu xe CBT miễn phí (`P-gio-mien-phi-luu-xe`) | Delta: 72 giờ | từ giờ đến tới giờ khởi hành | Đề xuất dòng phí, CS xác nhận (chờ OQ-33) |
| Kỳ chốt đường sắt (`P-ky-chot-duong-sat`) | Delta: ngày 25 và cuối tháng | tháng | Còn cờ "Chưa có đơn giá" thì chặn chốt kỳ |
| Định mức depot đường sắt (danh mục định mức, dữ liệu Riêng Delta) | 150.000 ₫ Nam Khánh; 160.000 ₫ Phú Lợi | mỗi lượt | Tự điền khi lái xe chọn loại phí |
| Chu kỳ nhắc nhật ký nhiệt (`P-chu-ky-nhac-nhiet`) | Chưa có số (OQ-43) | theo loại hàng, chỉnh được trên từng Lệnh | Nhắc lái xe; quá giờ chưa nhập thì báo điều vận |

### 7.3 Wording samples (exact strings)

Ngôi "bạn", câu ngắn, không "Vui lòng" (theo design.md). Loại hiển thị theo GR-15: Inline dưới trường, Popup chặn giữa màn, Toast góc màn.

#### Error messages

| Mã | Loại | Tình huống | Câu |
|---|---|---|---|
| E-transport-dispatch-001 | Popup | Giao xe khi air chưa về đủ kiện | **Hàng chưa về đủ kiện** · "Đã về 8/10 kiện. Chọn khai theo số đã về hoặc chờ đủ hàng trước khi giao xe." |
| E-transport-dispatch-002 | Popup | Sang bước khi thiếu ảnh bắt buộc | **Chưa chụp đủ ảnh** · "Còn thiếu ảnh tại: Đến vựa (đuôi xe)." |
| E-transport-dispatch-003 | Popup | Chốt Lệnh khi còn thiếu việc | **Chưa chốt được Lệnh** · "Còn thiếu: biên bản giao hàng, chi phí nâng hạ." |
| E-transport-dispatch-004 | Popup | Lập Lệnh khi YCVT đã đủ số | **YCVT đã đủ số Lệnh** · "YCVT [mã] đã lập 3/3 Lệnh. Tăng số xe trên YCVT nếu cần lập thêm." |
| E-transport-dispatch-005 | Popup | Nhận cảnh báo hoặc duyệt Lệnh đã có người làm | **Việc đã có người nhận** · "[Tên] đã nhận xử lý lúc 14:05." |
| E-transport-dispatch-006 | Popup | Chốt kỳ đường sắt khi còn Lệnh chưa có giá | **Chưa chốt được kỳ** · "Còn 2 Lệnh chưa có đơn giá." |
| E-transport-dispatch-007 | — | Bỏ ngày 10/10: không còn luồng duyệt chi ngoài định mức (wireframe còn dùng, sửa khi chạy lại `/user-flow`) | — |
| E-common-009 | Toast | Mất mạng | Dùng câu chung |
| E-common-008 | Toast | Lỗi hệ thống | Dùng câu chung |

#### Success messages

- "Đã lập Lệnh [mã]" · "Đã chốt Lệnh" · "Đã duyệt Lệnh" · "Đã gửi biên bản cho CS và khách"

Xác nhận (Xem CMP-03):

| Tình huống | Tiêu đề · nội dung | Nút |
|---|---|---|
| Huỷ Lệnh | **Huỷ Lệnh [mã]?** · "Số xe sẽ trả lại cho YCVT [mã]." | [Huỷ Lệnh] [Quay lại] |

#### Info / neutral messages

| Tình huống | Câu |
|---|---|
| Mất sóng | "Chờ đồng bộ. Ảnh sẽ gửi khi có mạng." |
| Kho CFS chưa sẵn sàng | "Kho chưa xác nhận hàng sẵn sàng. Xe có thể phải chờ." |

### 7.4 Bối cảnh hệ thống (mức nghiệp vụ)

**Thông tin cần lưu**
- Trên Lệnh: xe, mooc, lái xe, cung đường (kế hoạch và thực tế); ảnh định vị theo điểm; nhật ký nhiệt; chi hộ, chi phí sửa vỏ container, phí lưu ca xe, cấp dầu; biên bản giao hàng (điện tử hoặc ảnh bản giấy); giờ đến thật, vé trạm, thời gian kẹt xe (từ GPS); thay đổi giữa chặng; lý do từ chối, trả lại; hạn chuẩn bị giấy tờ.
- Lịch sử: ai lập, giao, duyệt Lệnh; ai đổi trạng thái.
- Danh mục: điểm chụp ảnh theo loại hàng; chu kỳ nhắc nhiệt theo loại hàng; loại phí kèm cách hạch toán theo địa điểm; đơn giá đường sắt.

**Dịch vụ bên ngoài**

| Dịch vụ | Mục đích | Tình trạng |
|---|---|---|
| GPS và cảm biến dầu EUP | Giờ đến, khởi hành, kẹt xe, vé trạm cho Lệnh | Có tài liệu khách (30/9) |
| Google Maps | Cung đường, giờ đến dự kiến | Có tài liệu khách |
| VETC | Nguồn chuẩn toạ độ, chi phí đường bộ (F8) | Có tài liệu khách |
| Email | Gửi văn bản cảnh báo, kế hoạch xe cho trưởng ga, biên bản giao hàng cho CS và khách | Trong phạm vi |

**Thông báo**

| Ai nhận | Khi nào | Kênh |
|---|---|---|
| Điều vận | Quá mốc, lái xe từ chối Lệnh, quá giờ chưa nhập nhiệt, D/O đổi kho khi xe đang chạy, lái xe báo thay đổi giữa chặng | Thông báo đẩy |
| Trưởng điều vận | Cảnh báo quá hạn chưa xử lý | Thông báo đẩy |
| CS | Air chưa đủ kiện | Thông báo đẩy |
| CS và khách | Lái xe xác nhận biên bản giao hàng khách đã ký | Email kèm biên bản |
| Lái xe | Lệnh mới, tới giờ nhập nhiệt, Lệnh bị trả lại | Thông báo đẩy |
| Khách | Các mốc giao nhận khác | Chờ OQ-38 |

**Việc phần mềm tự chạy theo giờ:** đếm mốc và bắn cảnh báo quá mốc, leo thang · nhắc nhiệt độ theo chu kỳ · đồng hồ lưu xe theo `P-gio-mien-phi-luu-xe` (Delta: 72 giờ, chờ OQ-33) · sinh shipment list nháp tới kỳ `P-ky-chot-duong-sat` (Delta: ngày 25 và cuối tháng).

**Cần gần như tức thời:** giờ đến theo GPS, cảnh báo quá mốc, giao Lệnh mới. Còn lại (shipment list, thống kê) chậm vài phút được.

## 8. Assumptions

- SOP của Delta là thiết kế to-be của khách, không phải cách đang làm.
- Delta chưa gửi Quy trình điều vận (OQ-1); trạng thái Lệnh và thứ tự bước CBT, đường sắt là đề xuất dựa trên SOP Giao nhận hàng hoá.
- Gợi ý ghép hàng (D5) và hàng chiều về (D8) cần có sẵn dữ liệu tải xe, khoảng cách giữa các kho và yêu cầu vận tải nội địa trên phần mềm.

## 9. Risks

| Rủi ro | Khả năng | Hậu quả nghiệp vụ | Cách phòng |
|--------|----------|-------------------|-----------|
| Lái xe vẫn gửi ảnh và chi phí qua Zalo, không dùng app | thường | Mất bằng chứng; chi phí không lên JobID; vấn đề cũ quay lại | Thiếu ảnh thì chặn bước; app chạy khi mất sóng; thao tác chính làm được bằng một tay |
| Thiếu dữ liệu nền: tải xe, khoảng cách kho, giá đường sắt, định mức | thường | Gợi ý ghép hàng (D5), hàng chiều về (D8) sai | Chốt danh mục trước khi chạy thật; người có quyền cập nhật |
| Thiếu tài liệu khách: quy trình điều vận | thường | Luồng CBT, đường sắt và trạng thái Lệnh sai | Bám OQ-1 |
| GPS EUP gián đoạn | thỉnh thoảng | Mốc và giờ đến sai, cảnh báo sai | Lái xe bấm tay kèm ảnh định vị |

## 10. Success Criteria (preliminary)

Mỗi tiêu chí gắn một vấn đề ban đầu. Số hiện trạng và mục tiêu chờ khách (OQ-44, ở `service-delivery`).

| Vấn đề | Tiêu chí | Mục tiêu |
|---|---|---|
| c. Bị phạt vì quá mốc | Số lần, số tiền phạt lưu container, lưu vỏ, lưu xe mỗi tháng so với trước | giảm ?% |
| d. Chứng từ về chậm | Thời gian từ khi xe xong việc tới khi Lệnh được duyệt | ≤ ? ngày |
| e. Chi phí thiếu | Tỉ lệ Lệnh được duyệt mà đủ chi phí | ? |

## 11. Open Questions

Nguồn khách: tên tài liệu khách gửi và mục. Cột Trả lời theo biên bản [[docs/meetings/2026-10-10-oq-dispatch-coordination.md|Delta trả lời vòng 1]] (anh Nghĩa, 10/10/2026) và 2 điểm xác nhận lại ngày 12/10/2026.

| Mã | Câu hỏi | Nguồn khách | Trả lời |
|---|---|---|---|
| OQ-1 | Chưa có tài liệu Quy trình điều vận (QTĐV); luồng CBT, đường sắt và bước lập Lệnh đang dựa vào đâu? | Quy trình điều phối, các mục "Lệnh vận tải" (dẫn chiếu QTĐV) | Còn mở: Delta đang hoàn thiện, gửi dần |
| OQ-8 | 4 quy trình chờ Trasas; Trasas là ai? | Giao nhận hàng hoá (18/9/2026) | Đóng: ý kiến Trasas không làm thay đổi SOP |
| OQ-10 | Thuế với khoản chi hộ Ratraco không có hoá đơn đầu vào | Giao nhận hàng hoá (18/9/2026) | Còn mở: làm rõ khi viết SOP điều vận |
| OQ-12 | CBT và đường sắt thuộc QTĐV chưa có | Giao nhận hàng hoá (18/9/2026) | Đã chốt: CBT, đường sắt không đi qua Điều phối; mỗi loại JobID có giao diện, Yêu cầu vận tải, Lệnh riêng. Chi tiết chờ Quy trình điều vận |
| OQ-13 | Ai nhập đơn giá đường sắt khi thiếu phụ lục hợp đồng? | Giao nhận hàng hoá (18/9/2026) | Đã chốt (cùng OQ-30): giai đoạn 1 CS nhập đơn giá tay |
| OQ-18 | Quản lý vỏ container swap (vỏ Delta/khách, sửa chữa vỏ) có thuộc Điều phối không? | Chưa có trong tài liệu khách gửi | Ngoài giai đoạn 1; chi phí sửa vỏ ghi trên Lệnh (phần Điều vận) |
| OQ-20 | Người ký biên bản giao hàng phía khách là ai? Có khách bắt buộc đóng dấu không? | Chưa có trong tài liệu khách gửi | Một phần: làm cả ký điện tử lẫn biên bản giấy (xác nhận 12/10); tự email biên bản cho CS và khách khi lái xe xác nhận (A7). Còn thiếu: ai ký phía khách, khách nào bắt đóng dấu |
| OQ-28 | Ai bấm xác nhận "đã nhận tiền hoàn" tiền nâng vỏ? Quá 7 ngày chưa về thì báo ai? | Giao nhận hàng hoá (18/9/2026) | Ngoài phần mềm: khoản nằm trong dư nợ tạm ứng; bỏ theo dõi khoản chờ hoàn (B5) |
| OQ-30 | Đường sắt: giá xác định lần đầu lưu vào bảng giá cho các chuyến sau, hay chỉ dùng cho chuyến đó? Khi nào áp cách nào, ai quyết? | Giao nhận hàng hoá (18/9/2026) | Đã chốt: giai đoạn 1 CS làm đơn giá tay; giai đoạn 2 báo giá trên phân hệ Sales (E3) |
| OQ-32 | Bước 5 chi hộ Ratraco (thủ quỹ chuyển tiền trả lái xe) giữ thủ công hay chuyển khoản tự động? | Giao nhận hàng hoá (18/9/2026) | Còn mở: giải quyết trong Quy trình điều vận |
| OQ-33 | Phí lưu xe quá 72 giờ và phí máy phát CBT: có muốn phần mềm tự đề xuất doanh thu không; đơn giá, đơn vị tính; giờ bắt đầu lấy từ GPS hay ảnh định vị? | Giao nhận hàng hoá (18/9/2026) | Một phần: phí lưu ca xe ghi lên Lệnh; phí máy phát Delta sẽ có giải pháp. Còn thiếu: phần mềm có tự tính phí lưu ca không (E8) |
| OQ-34 | Quá mốc vì kẹt xe, sự cố đường: có thêm nhóm nguyên nhân thứ 4 "khách quan" không? | Chưa có trong tài liệu khách gửi | Ngoài phần mềm; không thêm nhóm nguyên nhân (B6) |
| OQ-35 | Kế hoạch ngày Ratraco gửi ngày n-1 có mẫu cố định không? Xin một mẫu thật | Giao nhận hàng hoá (18/9/2026) | Chưa hỏi Delta (ngoài deck vòng 1) |
| OQ-37 | Lái xe chỉnh nhiệt theo yêu cầu khách có bắt buộc chụp ảnh làm bằng chứng không? | Giao nhận hàng hoá (18/9/2026) | Chưa hỏi Delta (ngoài deck vòng 1) |
| OQ-38 | Khách có cần nhận thông báo ở mốc nào không: xe đã đến, đã nhận hàng, đã giao xong, quá mốc? | Chưa có trong tài liệu khách gửi | Chưa hỏi Delta (ngoài deck vòng 1) |
| OQ-43 | Chu kỳ nhắc nhập nhật ký nhiệt độ mặc định cho từng loại hàng lạnh là bao nhiêu? (SOP chỉ có sầu riêng 3–4 giờ/lần, hàng lạnh khác 3–4 lần/ngày) | Giao nhận hàng hoá (18/9/2026) | Chưa hỏi Delta (ngoài deck vòng 1) |
| OQ-45 | "Hàng quay cắt" trong thực tế là tình huống nào? Khi đó xe và hàng được xử lý ra sao? | Chưa có trong tài liệu khách gửi (trao đổi trực tiếp 09/10/2026) | Chưa hỏi Delta (ngoài deck vòng 1) |
| OQ-46 | Có cần làm luồng tạm ứng dầu cho xe CBT không? (Đợt trước khách nói bỏ phần xử lý bên ngoài) | Chưa có trong tài liệu khách gửi (trao đổi trực tiếp 09/10/2026) | Chưa hỏi Delta (ngoài deck vòng 1) |

## 12. Next Steps

Đã tách từ brainstorm Điều phối gộp ngày 2026-10-12. Tiếp theo:
- Chờ Delta gửi Quy trình điều vận (OQ-1), rồi rà lại Mục 5–6
- Hỏi lại Delta các câu còn mở ở Mục 11 (BL-041)
- `/user-flow transport-dispatch` — chạy lại; userflow tách máy từ bản nháp ngày 07/10, còn nội dung cũ (hạ vỏ "x/n", tiền hoàn nâng vỏ, duyệt chi ngoài định mức, CBT và đường sắt)
- `/srs transport-dispatch` — đặc tả FR, BR, Error Matrix
