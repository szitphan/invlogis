---
type: brainstorm
feature: dispatch-coordination
status: draft
updated: 2026-10-07
links:
  - docs-input/sop/sop-dieu-phoi.md
  - docs-input/sop/sop-cung-cap-dich-vu-tong-quat.md
  - docs-input/sop/giao-nhan-hang-hoa/giao-nhan-hang-hoa.md
  - docs-input/sop/hoa-don-tra-ho-2026-10-01/hoa-don-tra-ho-2026-10-01.md
  - docs-input/sop/du-lieu-van-hanh-xe-2026-09-30/du-lieu-van-hanh-xe-2026-09-30.md
  - docs-input/sop/eup-dieu-van-2026-09-19/eup-dieu-van-2026-09-19.md
  - docs-input/sop/sop-ban-do-kien-thuc.md
  - docs/_research/2026-10-02-container-deadline-alerts.md
  - docs/_research/2026-10-02-electronic-delivery-record.md
  - docs/_research/2026-10-02-eport-integration.md
  - docs/_research/2026-10-02-field-document-reading.md
  - docs/_shared/project-profile.md
  - docs/meetings/decks/2026-10-06-oq-dispatch-coordination-deck.md
---

# Điều phối — JobID, Yêu cầu vận tải, Lệnh vận tải liền mạch

> Bản checkpoint 2026-10-07. Đã phỏng vấn: tổng quan, người dùng, luồng chính, vòng rà đề xuất A/B/D/E. Chưa phỏng vấn: điểm rẽ nhánh chi tiết, trạng thái, kiểm tra dữ liệu và câu thông báo, rủi ro, tiêu chí thành công.

## 1. Idea Seed

Dữ liệu đi liền mạch từ JobID sang Yêu cầu vận tải (YCVT) sang Lệnh vận tải và chiều ngược lại, gồm cả Quy trình cung cấp dịch vụ tổng quát. Mỗi việc làm trên JobID hoặc Lệnh phải kéo theo đủ chi phí, để khi dịch vụ hoàn thành thì doanh thu và chi phí đã nằm đúng JobID.

## 2. Context

**5 vấn đề hiện tại (khách xác nhận cả 5):**

| Mã | Vấn đề |
|---|---|
| a | Nhập lại cùng một dữ liệu nhiều lần |
| b | Giao việc qua điện thoại, Zalo; không truy được ai đang giữ việc |
| c | Không thấy trước mốc cắt máng, cut-off, lưu container, lưu vỏ nên bị phạt |
| d | Chứng từ giấy về chậm nên chốt Lệnh và tính chi phí chậm |
| e | Chi phí chưa được hạch toán rõ ràng, đầy đủ |

**Phạm vi:**
- Gồm: Điều phối 6 luồng (FCL, LCL/CFS, air × xuất, nhập), CBT và đường sắt ở mức Lệnh + chi phí; tạo và duyệt JobID (có AI đọc chứng từ); ghi nhận chi phí, doanh thu lên JobID và Lệnh.
- Không gồm (feature riêng, Điều phối chỉ đảm bảo dữ liệu đủ và đúng JobID): màn bảng kê, công nợ, kết nối MISA; "Thanh toán trả hộ" (duyệt hạn mức, QR, UNC, API ngân hàng); ghi nhận và bù dầu (module Vận tải / Cấp dầu); phạm vi xem dữ liệu chi nhánh khác (feature Phân quyền).
- Ứng dụng: Delta Super App, dùng chung cho nhân viên Delta và nhân viên đối tác/khách; làm cả web và mobile.

**Nguồn:** 3 SOP của Delta (Quy trình điều phối, Quy trình cung cấp dịch vụ tổng quát, Giao nhận hàng hoá 18/9/2026), tài liệu Hoá đơn trả hộ 01/10/2026, Dữ liệu vận hành xe 30/9/2026, 4 báo cáo điều tra trong `docs/_research/`.

**Nhãn đề xuất:** [SOP to-be] = SOP đã yêu cầu, phần mềm làm theo · [SOP+] = SOP có nêu, đề xuất làm thêm · [Mới] = SOP chưa có. Chỉ [SOP+] và [Mới] tính là điểm khác biệt.

## 3. User Types (preliminary)

Phân quyền theo chức năng ("quyền lái xe", "quyền hiện trường"…), không cố định vai trò. Luồng và sơ đồ vẫn ghi theo vai trò nghiệp vụ.

| User Type | Pain Point | Primary Need |
|-----------|-----------|--------------|
| CS | Nhập lại chứng từ; xe đi nhầm kho; không biết JobID đang kẹt ở đâu | Theo dõi và xử lý mọi nghiệp vụ trong một JobID |
| Điều vận | Xếp xe bằng bảng tính + Zalo; không thấy trước mốc phạt | Màn theo dõi xếp xe có đủ dữ liệu để quyết định |
| Lái xe | Gửi ảnh, nhiệt độ, chi phí qua Zalo; phải nhớ điểm cần chụp | Nhận Lệnh, chụp ảnh, thao tác nhanh trên Lệnh |
| Nhân viên hiện trường | Nhận việc qua điện thoại; chứng từ gốc dễ thất lạc | Chụp chứng từ và xác nhận ngay tại chỗ |
| Cán bộ quản lý | Giao việc, duyệt bằng tin nhắn | "Việc của tôi" để duyệt |
| Kế toán | Chi phí về muộn, thiếu, không gắn JobID | Chi phí đã gắn đúng Lệnh, JobID |
| Đại diện khách hàng | Phải gọi CS hỏi tình trạng | Theo dõi lô, nhận file xuất |
| Trợ lý AI | — | Đọc chứng từ, gợi ý người nhận việc, ghép hàng, hàng chiều về |

Mọi vai trò có màn "Việc của tôi" kèm thông báo đẩy mở thẳng vào việc; mỗi feature có màn danh sách riêng. Mặc định chỉ thấy JobID của chi nhánh mình.

### 3.1 Tác vụ chính

Tần suất chưa đo được, ghi định tính. Cột Ghi chú nêu hậu quả khi làm sai hoặc chậm; dòng có ★ là tác vụ phải tối ưu cho thao tác nhanh nhất.

| Vai trò | Tác vụ | Tần suất | Mức quan trọng | Ghi chú |
|---------|--------|----------|----------------|---------|
| CS | ★ Theo dõi và xử lý nghiệp vụ trong JobID: tạo JobID từ chứng từ, xử lý air chưa đủ kiện, xác nhận doanh thu phát sinh, giao chứng từ gốc | Nhiều lần mỗi ngày | cao | Xe đi nhầm kho hoặc đi khi hàng chưa sẵn sàng; thiếu doanh thu; khách chưa nhận căn cứ thanh toán |
| Điều vận | ★ Màn theo dõi xếp xe: tạo Lệnh, xếp xe và lái xe, Lệnh đường sắt hàng loạt, ghép hàng lẻ, duyệt chi ngoài định mức, xử lý cảnh báo quá mốc | Liên tục trong ca | cao | Trễ cut-off; xe chạy rỗng chiều về; chi phí mất kiểm soát |
| Lái xe | ★ Nhận Lệnh, chụp ảnh, thao tác nhanh trên Lệnh (nhật ký nhiệt, chi hộ, chuyển bước) | Nhiều lần mỗi chuyến | cao | Thiếu bằng chứng khi tranh chấp; hỏng hàng lạnh không truy được trách nhiệm |
| Nhân viên hiện trường | ★ Chụp: phiếu cân ra VGM, EIR, mã vạch gốc; nhận việc được gợi ý; thu hoá đơn GTGT | Vài lần mỗi ngày | cao | Trễ VGM nên lỡ tàu; mất chứng từ gốc |
| Cán bộ quản lý | ★ Việc của tôi (duyệt): giao việc hiện trường, duyệt thông tin viết hoá đơn bất thường, xem cảnh báo | Vài lần mỗi ngày | trung | Xuất sai hoá đơn; việc hiện trường không có người nhận |
| Kế toán | Nhận chi phí đã gắn Lệnh/JobID; thanh toán khoản trên 5 triệu | Hằng ngày, dồn vào kỳ chốt | trung | Chốt kỳ trễ; hạch toán sai |
| Đại diện khách hàng | Theo dõi tình trạng lô; nhận file xuất | Thỉnh thoảng | thấp | Gọi hỏi CS nhiều |
| Trợ lý AI | Đọc chứng từ; gợi ý người nhận việc, ghép hàng, hàng chiều về | Tự động | trung | Gợi ý sai thì người dùng phải sửa tay |

## 4. Capabilities Breakdown

### P0 — must have

**Luồng lõi:** tạo, duyệt JobID → hoàn thiện dữ liệu và phân luồng → giao việc hiện trường → sinh YCVT → lập Lệnh → chạy Lệnh → chốt, duyệt Lệnh → hoàn thành dịch vụ (Mục 5).

**Nhóm A — giảm nhập liệu**
- A1 [SOP+] AI đọc Booking Note, eDO để điền mốc cắt máng, cut-off, lưu container, lưu vỏ.
- A2 [SOP+] Quét QR tờ khai hải quan; lưu cả ảnh QR lẫn thông tin bóc từ QR.
- A3 [SOP+] Kiểm số container theo chữ số kiểm tra ISO 6346, bắt sai ngay khi nhập hoặc AI đọc.
- A4 [SOP+] Chụp EIR để tự điền giờ, số container, số chì; giờ EIR nhận hàng là mốc tính lưu vỏ.
- A5 [SOP+] Hỗ trợ CS danh sách việc ePort theo cảng, lưu lệnh và EIR về Lệnh (không kết nối máy với ePort).
- A6 [SOP+] Quét QR Lệnh giao vỏ điện tử (mức nhẹ).
- A7 [SOP+] Biên bản giao hàng có cấu trúc trên app, tự điền từ Lệnh, bắt ghi có/không bất thường + ảnh trước khi rời điểm, chạy được khi mất sóng; khách ký trên máy lái xe chạy thử với khách đồng ý. Mẫu theo 5 loại hàng.
- A8 [SOP+] AI đọc phiếu cân ra VGM; người chụp bắt buộc xác nhận trước khi lưu.
- A9 [SOP+] Hoá đơn điện tử lấy qua MISA; không khớp thì chụp + nhập tay, gắn cờ "Chưa khớp hoá đơn điện tử".

**Nhóm B — quy trình**
- B1 [SOP+] Danh mục cảng/bãi có 3 thuộc tính: có ePort, có xe mới chọn được vỏ, thanh lý tờ khai online hay tại bãi; phần mềm phân luồng theo 3 thuộc tính này. Người có quyền (theo Phân quyền) cập nhật.
- B2 [SOP to-be] Nút "Chuyển cho hiện trường" thay "Từ chối", bắt chọn lý do; quyền thanh toán tự chuyển sang hiện trường.
- B3a [SOP+] Gợi ý 2–3 người nhận việc (gần cảng/bãi, số việc đang ôm, trong ca trực); quản lý vẫn bấm chọn. Dùng chung quy tắc "người gần lái xe nhất".
- B3b [SOP to-be] Phân công trực ngoài giờ 17h30–8h theo ngày; người trực có quyền tự giao việc trong ca, hết ca thu quyền.
- B4 [SOP+] Gộp giao việc Lệnh hạ vỏ theo vận đơn + nơi hạ; mỗi container vẫn 1 Lệnh hạ; theo dõi "đã làm x/n".
- B5 [SOP+] Khoản tiền nâng vỏ chờ hoàn gắn Lệnh/JobID, hạn 7 ngày, cảnh báo quá hạn; phí đổi vỏ ghi chi phí phát sinh của Lệnh.
- B6 [SOP+] Cảnh báo quá mốc: bắt chọn nhóm nguyên nhân (thêm nhóm "do nhà vận tải"), văn bản soạn sẵn báo khách/hãng tàu, mỗi cảnh báo có người phụ trách + trạng thái "đã xử lý"; gửi qua email, copy nội dung hoặc xuất file. Leo thang lên trưởng điều vận.

**Nhóm D — từ SOP Giao nhận hàng hoá**
- D1 [SOP+] Danh sách điểm chụp ảnh định vị bắt buộc theo loại hàng; ảnh tự gắn vị trí, giờ vào Lệnh; thiếu ảnh thì chặn bước tiếp. Trưởng điều vận duy trì danh sách.
- D2 [SOP+] Nhật ký nhiệt độ hàng lạnh: chu kỳ nhắc mặc định theo loại hàng, chỉnh được trên từng Lệnh; quá giờ chưa nhập thì cảnh báo điều vận; khách nhận qua file xuất. Yêu cầu chỉnh nhiệt vẫn nhắn qua kênh ngoài; lái xe ghi "đã chỉnh" + lý do, không bắt ảnh.
- D3 [SOP+] Air nhập chưa về đủ kiện thì chặn giao xe tới khi CS chọn "Khai theo số kiện đã về" hoặc "Chờ đủ hàng"; lô tách chuyến thành nhiều Lệnh dưới 1 JobID. Kho CFS chưa xác nhận hàng sẵn sàng thì chỉ cảnh báo.
- D4 [SOP+] Nơi nhận trên Lệnh lấy thẳng từ D/O, không nhập tay; D/O đổi kho thì Lệnh cập nhật theo, xe đã giao thì báo điều vận.
- D5 [SOP+] Gợi ý ghép hàng lẻ và hàng air chung xe (cùng kho/kho gần, giờ cut-off, CBM/trọng lượng so với tải xe); điều vận bấm chọn.
- D6 [SOP+] Đường sắt: nhập kế hoạch Ratraco ngày n (nhận ngày n-1), sinh Lệnh hàng loạt; xuất "Kế hoạch xe theo ga" gửi trưởng ga (chỉ nhận file); gợi ý nơi lấy vỏ theo thứ tự ưu tiên SOP.
- D7 [SOP+] Lệnh đường sắt hoàn tất tự vào shipment list đúng kỳ (ngày 25 / cuối tháng). Màn shipment list, bảng kê là feature riêng.
- D8 [Mới] Gợi ý hàng chiều về cho xe CBT sắp trả hàng ở miền Nam, miền Trung.
- D9 [SOP+] Theo dõi mã vạch gốc air: Đang ở hiện trường → CS đã nhận → Đã giao khách; đánh dấu "cần chuyển mã vạch gốc" trên từng JobID; chưa giao khách thì JobID có cờ ở bước ghi nhận doanh thu.
- D10 [SOP to-be] CBT đổi bên xuất hoá đơn trên JobID tới trước khi xuất hoá đơn, không phải huỷ Lệnh; bên thứ ba chưa có mã thì tạo việc "Đăng ký bên thanh toán" kèm thoả thuận ba bên.

**Nhóm E — chi phí (vấn đề e)**
- E1 [SOP to-be] Xin duyệt chi ngoài định mức trên app trước khi chi, gắn Lệnh, áp mọi loại hàng; điều vận duyệt là đủ; chưa duyệt thì chặn hoàn tiền.
- E2 [SOP to-be] Phần mềm đề xuất cách trả theo ngưỡng 5 triệu (dưới: tạm ứng; trên: tạo việc cho CS phụ trách + kế toán), bắt chọn có/không hoá đơn.
- E3 [SOP+] Bảng giá phụ lục hợp đồng đường sắt; Lệnh tự áp giá; thiếu giá thì cờ "Chưa có đơn giá" + việc "Xác định giá"; còn cờ thì chặn chốt kỳ.
- E4 [SOP to-be] Lái xe ghi chi hộ Ratraco, cân xe ngay trên Lệnh (loại phí, số tiền, ảnh); phần mềm gom bảng kê chi phí cho điều vận xác nhận, gắn nhãn "chi hộ — phải thu lại"; cân xe chọn "khách trả trực tiếp" hoặc "Delta trả".
- E5 [SOP to-be] Danh mục loại phí có cách hạch toán theo địa điểm; lái xe chỉ chọn loại phí, phần mềm tự xếp và tự điền định mức (150.000 ₫ Nam Khánh, 160.000 ₫ Phú Lợi).
- E6 [SOP to-be] Nút tạo Yêu cầu thanh toán trên Lệnh/JobID, gắn chi phí đúng Lệnh/JobID; việc "Thu hoá đơn GTGT" giao người gần lái xe nhất; hiện trạng thái thanh toán. Phần duyệt, QR, UNC, API ngân hàng thuộc feature "Thanh toán trả hộ".
- E7 [SOP to-be] Hiện trên Lệnh dữ liệu GPS: giờ đến thật, vé trạm, cờ tránh trạm, thời gian kẹt xe; dữ liệu kẹt xe gắn làm bằng chứng vào cảnh báo quá mốc.
- E8 [SOP+] Đồng hồ lưu xe CBT từ giờ đến tới giờ khởi hành; quá 72 giờ tự đề xuất dòng doanh thu trên JobID, CS xác nhận; máy phát tương tự. Làm khi khách xác nhận (OQ-33).

### P1 — should have

Chưa phân mức: mọi đề xuất đã chốt ở trên đều làm ngay giai đoạn này.

### P2 — nice to have

Chưa phân mức.

## 5. Core Flows (Happy Path)

### 5.1 Luồng tổng (xương sống chung)

0. **Tạo và duyệt JobID** — CS hoặc điều vận đưa chứng từ khách, khai phạm vi dịch vụ; AI đọc chứng từ, người tạo xác nhận. Không đạt điều kiện nợ quá hạn, hạn mức thì dừng hẳn, chờ khách thanh toán. JobID không có thủ tục giao nhận (CBT, đường sắt, không làm hiện trường) đi thẳng sang lập Lệnh.
1. **Nhận JobID vào Điều phối** — phần mềm đưa vào danh sách của CS, bắt đầu đếm mốc.
2. **Hoàn thiện dữ liệu và phân luồng** — CS kê khai, đưa chứng từ; nơi nhận lấy từ D/O; chưa kê khai đủ thì khoá thanh toán trên JobID.
3. **Giao việc hiện trường** — cán bộ quản lý hiện trường chọn người (phần mềm gợi ý 2–3 người); phần mềm ghi chi phí định mức, cấp quyền thanh toán.
4. **Sinh YCVT** — FCL: sau khi hiện trường xong việc tại cảng/bãi. Hàng lẻ, CFS, air: ngay khi giao việc, việc hiện trường chạy song song với Lệnh.
5. **Lập Lệnh vận tải** — điều vận gán xe, lái xe, cung đường.
6. **Chạy Lệnh** — lái xe nhận Lệnh, chụp ảnh điểm bắt buộc, nhật ký nhiệt, ghi chi hộ; GPS tự đánh dấu "đã đến"; quá mốc thì cảnh báo, leo thang.
7. **Chốt và duyệt Lệnh** — thiếu việc, chứng từ, chi phí thì chặn chốt; duyệt xong chi phí lên JobID.
8. **Hoàn thành dịch vụ** — CS xác nhận doanh thu phát sinh, giao chứng từ gốc; JobID ghi doanh thu, chi phí vào kỳ.

Ký hiệu: `[Vai trò]` người làm · `(PM)` phần mềm tự làm · `<…?>` điểm rẽ nhánh.

```
1. TẠO JOBID
[CS/Điều vận] Đưa chứng từ khách, khai phạm vi dịch vụ
   |
   v
(PM) AI đọc chứng từ --> [Người tạo] xác nhận / sửa (chỗ sửa lưu lại để AI học)
   |
   v
<Đạt điều kiện nợ quá hạn, hạn mức?> --Không--> DỪNG, chờ khách thanh toán
   | Có                                          (khách thanh toán xong -> đi tiếp)
   v
<Có thủ tục giao nhận tại cảng / kho / sân bay?>
   | Có                                   | Không (CBT, đường sắt, không làm hiện trường)
   v                                      +---------------------------------------+
2. HOÀN THIỆN DỮ LIỆU                                                            |
[CS] Kê khai giờ nhận/trả, nơi hạ, tờ khai + QR, đưa D/O, booking                 |
(PM) Nơi nhận lấy thẳng từ D/O; bắt đầu đếm mốc cut-off / lưu cont / lưu vỏ       |
(PM) Chưa kê khai đủ --> khoá thanh toán trên JobID                               |
[CS] Hàng nhập: trả phí lấy eDO, cược vỏ                                         |
   |                                                                              |
   v                                                                              |
<FCL đi thẳng ra YCVT được không? (xem 5.2, 5.3)>                                 |
   | Có ------------------------------------------------------------+             |
   | Không / CS chuyển cho hiện trường (chọn lý do)                 |             |
   v                                                                |             |
3. GIAO VIỆC                                                        |             |
(PM) Gợi ý 2-3 người gần nhất                                       |             |
[Cán bộ QL hiện trường] Chọn nhân viên hiện trường hoặc lái xe       |             |
(PM) Ghi chi phí định mức, cấp quyền thanh toán cho người được giao  |             |
   |                                                                |             |
   v                                                                |             |
<Loại hàng?>                                                        |             |
   | FCL                              | LCL / CFS / air             |             |
   v                                  v                             |             |
4. [Hiện trường] chọn vỏ,            (PM) Sinh YCVT ngay;           |             |
   lấy lệnh nâng, chụp EIR,          việc hiện trường chạy song     |             |
   phiếu cân -> VGM                  song ở bước 6 ----------+      |             |
   (giao cho lái xe: bỏ qua)                                 |      |             |
   |                                                         |      |             |
   v                                                         |      |             |
(PM) Sinh YCVT, 1 YCVT / container <-------------------------+------+             |
   |                                                                              |
   v                                                                              |
5. LẬP LỆNH VẬN TẢI <----------------------------------------------------------+
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
[Hiện trường] Hàng lẻ / air: phiếu nhập kho, phiếu cân, phiếu xuất kho
              -> số kiện, CBM, kg thay số trên Booking Note
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
8. HOÀN THÀNH DỊCH VỤ
[CS] Xác nhận doanh thu phát sinh; giao chứng từ gốc nếu JobID có đánh dấu
(PM) JobID "Hoàn thành dịch vụ" --> ghi doanh thu, chi phí vào kỳ
(PM) Đường sắt --> tự vào bảng kê kỳ ngày 25 / cuối tháng
```

### 5.2 FCL xuất

Theo Quy trình điều phối mục 5.1.

```
[CS] Kê khai: giờ đóng hàng, giờ nhận vỏ, cảng hạ hàng, thông báo hãng tàu, tờ khai + QR
(PM) Cấp quyền trả phí nâng vỏ cho CS
   |
   v
<Bãi cấp vỏ phải có xe mới chọn được vỏ? Bãi có ePort?>
   +-- Có xe mới chọn, có ePort ---- [CS] làm lệnh nâng khống ------------------> (A)
   |                                 CS chuyển cho HT --> [Cán bộ QL] giao HT --> (A)
   +-- Có xe mới chọn, không ePort - lái xe tự chọn vỏ, làm lệnh nâng tại bãi -> (A)
   +-- Chọn trước được, có ePort --- [CS] làm lệnh nâng vỏ, hoặc chuyển HT -----> (B)
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
(PM) Chưa kê khai đủ --> khoá thanh toán trên JobID
[CS] Trả hãng tàu lấy eDO; ghi hạn eDO, hạn trả vỏ; trả phí gia hạn nếu có; cược vỏ
   |
   v
<Cảng nhận hàng có ePort?>
   +-- Có:    [CS] đổi eDO lấy lệnh nâng hàng cho đủ container trên vận đơn --> (A)
   |          (cảng phải thanh lý tờ khai tại bãi: HT vẫn xuống cảng - OQ-39)
   |          CS chuyển cho hiện trường --> (B)
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
- <Đã về đủ kiện?> --Chưa--> CHẶN giao xe --> [CS] "Khai theo số đã về" / "Chờ đủ"
- Lô tách chuyến: mỗi đợt hàng về = 1 Lệnh mới dưới cùng JobID
- JobID có đánh dấu mã vạch gốc --> theo dõi: hiện trường -> CS đã nhận -> đã giao khách
```

### 5.8 CBT

Theo SOP Giao nhận hàng hoá. Thứ tự bước giữa chưa có quy trình điều vận của khách làm căn cứ (OQ-1).

```
(PM) JobID J07 --> YCVT ngay (bỏ qua bước 1-4)
[Điều vận] Lập Lệnh
[Lái xe] đến vựa: chụp đầu + đuôi xe --> đóng hàng --> nhật ký nhiệt theo chu kỳ của loại hàng
   --> đến cửa khẩu: chụp ảnh --> giao hàng
(PM) Đồng hồ lưu xe từ giờ đến tới giờ khởi hành; quá 72h --> đề xuất dòng doanh thu, CS xác nhận
[Lái xe] Chi ngoài định mức --> [Điều vận] duyệt
(PM) Xe sắp trả hàng ở miền Nam / Trung --> gợi ý hàng chiều về
--> Chốt Lệnh
```

### 5.9 Đường sắt

Theo SOP Giao nhận hàng hoá. Thứ tự bước giữa chưa có quy trình điều vận của khách làm căn cứ (OQ-1).

```
[Điều vận] Nhập kế hoạch Ratraco ngày n (nhận từ ngày n-1) --> (PM) sinh Lệnh hàng loạt
[Điều vận] Xếp xe, lái xe
   (PM) gợi ý nơi lấy vỏ: theo kế hoạch Ratraco -> tồn vỏ tại ga -> vị trí xe đang đậu
(PM) Xuất "Kế hoạch xe theo ga" --> gửi trưởng ga (email / copy / file)
[Lái xe] Chạy Lệnh, ghi chi hộ Ratraco / cân xe (loại phí, số tiền, ảnh)
(PM) Áp giá theo phụ lục hợp đồng; chưa có giá --> cờ "Chưa có đơn giá" + việc "Xác định giá"
--> Chốt Lệnh --> (PM) vào shipment list kỳ 25 / cuối tháng
                  còn cờ "Chưa có đơn giá" --> chặn chốt kỳ
```

## 6. System Behavior Deep Dive

### 6.1 Decision Points

Mới rút từ sơ đồ luồng chính; chưa phỏng vấn chi tiết.

| ID | Flow | Khi nào | YES (nhánh đồng ý) | NO (nhánh từ chối) |
|---|---|---|---|---|
| DP-01 | Tạo JobID | Đạt điều kiện nợ quá hạn, hạn mức | Đi tiếp | Dừng, chờ khách thanh toán |
| DP-02 | Tạo JobID | Có thủ tục giao nhận tại cảng/kho/sân bay | Vào Điều phối (bước 1) | Thành YCVT, sang lập Lệnh |
| DP-03 | Hoàn thiện dữ liệu | CS kê khai đủ | Mở thanh toán trên JobID | Khoá thanh toán |
| DP-04 | FCL xuất, nhập | Bãi có ePort và CS tự làm lệnh nâng | Sinh YCVT (bỏ qua giao việc, trừ FCL xuất chọn vỏ trước) | Giao việc hiện trường |
| DP-05 | FCL xuất | Bãi phải có xe mới chọn được vỏ | Lệnh nâng khống hoặc lái xe tự chọn vỏ | Chọn vỏ trước khi xe đến |
| DP-06 | Giao việc | Loại hàng FCL | Hiện trường xong việc mới sinh YCVT | Sinh YCVT ngay, hiện trường song song |
| DP-07 | Air nhập | Đã về đủ kiện | Giao xe | Chặn giao xe tới khi CS chọn cách xử lý |
| DP-08 | CFS nhập | Kho xác nhận hàng sẵn sàng | Giao xe | Cảnh báo, vẫn giao xe được |
| DP-09 | Chạy Lệnh | Đủ ảnh tại điểm bắt buộc | Qua bước tiếp | Chặn bước tiếp |
| DP-10 | Hạ hàng / hạ vỏ | Cảng/bãi hạ có ePort | CS làm lệnh hạ | Lái xe làm lệnh hạ |
| DP-11 | Chốt Lệnh | Đủ việc, chứng từ, chi phí | Chờ duyệt | Chặn chốt, chỉ ra phần thiếu |
| DP-12 | Đường sắt | Lệnh có đơn giá | Vào kỳ chốt | Cờ "Chưa có đơn giá", chặn chốt kỳ |

### 6.2 Scenario Matrix (nếu `has_multi_role` / ≥2 input states)

Chưa phỏng vấn.

### 6.3 State Transitions (nếu `has_state_machine`)

Chưa phỏng vấn. Thực thể cần làm: JobID, YCVT, Lệnh vận tải, cảnh báo mốc, chứng từ gốc phải chuyển (D9 đã có 3 trạng thái: Đang ở hiện trường → CS đã nhận → Đã giao khách).

### 6.4 Interrupted Transactions (nếu `has_external_redirect` / `has_async_flow`)

Chưa phỏng vấn.

### 6.5 Other Edge Cases

- Air nhập tách chuyến bay: mỗi đợt hàng về là 1 Lệnh mới dưới cùng JobID.
- D/O đổi kho sau khi đã có Lệnh: Lệnh cập nhật theo; xe đã giao thì báo điều vận.
- CS chuyển việc cho hiện trường: bắt chọn lý do; quyền thanh toán chuyển theo.
- Nhân viên hiện trường từ chối chọn vỏ: JobID quay về cán bộ quản lý giao lại.
- Mất sóng tại điểm giao: biên bản giao hàng vẫn ghi được, đồng bộ sau.
- Tiền nâng vỏ chờ hoàn quá 7 ngày chưa về: cảnh báo.

## 7. Validation, Limits & Wording

### 7.1 Validation rules

Chưa phỏng vấn. Đã có:

| Field | Rule |
|---|---|
| Số container | Kiểm chữ số kiểm tra theo ISO 6346 |
| Nơi nhận trên Lệnh | Lấy từ D/O, không nhập tay |
| VGM | AI đọc từ phiếu cân, người chụp bắt buộc xác nhận |

### 7.2 Limits & Quotas (exact values)

| Tham số | Giá trị | Window | Behavior khi vượt |
|---|---|---|---|
| Ngưỡng cách trả chi phí | 5.000.000 ₫ | mỗi khoản | Dưới: tạm ứng; trên: tạo việc cho CS phụ trách + kế toán |
| Hạn hoàn tiền nâng vỏ | 7 ngày | từ khi từ chối vỏ | Cảnh báo quá hạn |
| Lưu xe CBT miễn phí | 72 giờ | từ giờ đến tới giờ khởi hành | Đề xuất dòng doanh thu, CS xác nhận |
| Ca trực ngoài giờ | 17h30–8h | mỗi ngày | Người trực có quyền tự giao việc |
| Kỳ chốt đường sắt | ngày 25 và cuối tháng | tháng | Còn cờ "Chưa có đơn giá" thì chặn chốt kỳ |
| Định mức depot đường sắt | 150.000 ₫ Nam Khánh; 160.000 ₫ Phú Lợi | mỗi lượt | Tự điền khi lái xe chọn loại phí |

### 7.3 Wording samples (exact strings)

Chưa phỏng vấn.

#### Error messages

Chưa phỏng vấn.

#### Success messages

Chưa phỏng vấn.

#### Info / neutral messages

Chưa phỏng vấn.

## 8. Assumptions

- SOP của Delta là thiết kế to-be của khách, không phải cách đang làm.
- JobID dừng vì nợ quá hạn, hạn mức: khách thanh toán xong thì JobID đi tiếp.
- SOP Quy trình điều phối mục 5.4.2.4 ghi "nhân viên CS upload đủ Lệnh nâng hàng" trong bước của hiện trường; hiểu là nhân viên hiện trường upload (chờ xác nhận, OQ-40).
- Luồng CBT và đường sắt dựa trên SOP Giao nhận hàng hoá, chưa có quy trình điều vận riêng.
- Gợi ý ghép hàng (D5) và hàng chiều về (D8) cần có sẵn dữ liệu tải xe, khoảng cách giữa các kho và yêu cầu vận tải nội địa trên phần mềm.

## 9. Risks

Chưa phỏng vấn. Đã thấy:

| Rủi ro | Khả năng | Hậu quả nghiệp vụ | Cách phòng |
|--------|----------|-------------------|-----------|
| Thiếu dữ liệu tải xe, khoảng cách kho, YCVT nội địa khi làm D5, D8 | thường | Gợi ý sai, người dùng bỏ qua tính năng | Chốt nguồn dữ liệu trước khi làm SRS |
| Chưa có quy trình điều vận (QTĐV) | thường | Luồng CBT, đường sắt có thể sai thứ tự | OQ-1, xin khách tài liệu |

## 10. Success Criteria (preliminary)

Chưa phỏng vấn.

## 11. Open Questions

Nguồn khách: tên tài liệu khách gửi và mục. Quy trình điều phối và Quy trình cung cấp dịch vụ tổng quát chưa có ngày bản trong sổ nguồn.

| Mã | Câu hỏi | Nguồn khách |
|---|---|---|
| OQ-1 | Chưa có tài liệu Quy trình điều vận (QTĐV); luồng CBT, đường sắt và bước lập Lệnh đang dựa vào đâu? | Quy trình điều phối, các mục "Lệnh vận tải" (dẫn chiếu QTĐV) |
| OQ-3 | Phụ lục Bảng thông tin JobID và Định mức chi phí còn trống | Quy trình điều phối, mục 6.1–6.2 |
| OQ-4 | Cách phân chia lợi nhuận nội bộ giữa các chi nhánh chưa chốt | Quy trình cung cấp dịch vụ tổng quát |
| OQ-5 | Phụ lục bảng kê doanh thu, chi phí còn trống | Quy trình cung cấp dịch vụ tổng quát, phụ lục |
| OQ-6 | Chưa có cách xử lý bồi thường nội bộ khi khách từ chối trả hộ do lỗi nhân viên | Quy trình cung cấp dịch vụ tổng quát, mục 5.3–5.5 |
| OQ-7 | Quy trình quản lý quỹ và thanh toán chưa phát triển | Quy trình cung cấp dịch vụ tổng quát |
| OQ-8 | 4 quy trình chờ Trasas; Trasas là ai? | Giao nhận hàng hoá (18/9/2026) |
| OQ-9 | Định danh JobID đường sắt thế nào? | Giao nhận hàng hoá (18/9/2026) |
| OQ-10 | Thuế với khoản chi hộ Ratraco không có hoá đơn đầu vào | Giao nhận hàng hoá (18/9/2026) |
| OQ-11 | Lệch báo cáo quản trị và báo cáo thuế ở hàng CBT, cần kế toán xác nhận | Giao nhận hàng hoá (18/9/2026) |
| OQ-12 | CBT và đường sắt thuộc QTĐV chưa có | Giao nhận hàng hoá (18/9/2026) |
| OQ-13 | Ai nhập đơn giá đường sắt khi thiếu phụ lục hợp đồng? | Giao nhận hàng hoá (18/9/2026) |
| OQ-16 | JobID có được chia sẻ hoặc chuyển sang chi nhánh khác không, thao tác ra sao? | Quy trình cung cấp dịch vụ tổng quát, mục 5.5 |
| OQ-17 | Quy mô: JobID mỗi ngày, số lái xe, nhân viên hiện trường, CS, điều vận theo chi nhánh (Hà Nội, Hải Phòng, TP.HCM, Lạng Sơn) | Chưa có trong tài liệu khách gửi |
| OQ-18 | Quản lý vỏ container swap (vỏ Delta/khách, sửa chữa vỏ) có thuộc Điều phối không? | Chưa có trong tài liệu khách gửi |
| OQ-19 | Khách có cung cấp số booking, tàu, chuyến (xuất) hoặc free time lưu container, lưu vỏ (nhập) ngay khi đặt xe không? | Giao nhận hàng hoá (18/9/2026) |
| OQ-20 | Người ký biên bản giao hàng phía khách là ai? Có khách bắt buộc đóng dấu không? | Chưa có trong tài liệu khách gửi |
| OQ-21 | Các cảng, depot Delta làm nhiều nhất? | Chưa có trong tài liệu khách gửi |
| OQ-22 | QR trên tờ khai hải quan chứa những trường nào? Xin mẫu thật | Quy trình điều phối, các mục "Phân luồng công việc" |
| OQ-23 | Gói MISA có lấy đủ hoá đơn đầu vào không? Hoá đơn trả hộ ghi mã số thuế của ai? | Quy trình cung cấp dịch vụ tổng quát |
| OQ-24 | QR trên Lệnh giao vỏ điện tử chứa gì, bãi nào phát hành? | Mẫu Lệnh giao vỏ điện tử khách gửi |
| OQ-25 | Danh sách lý do khi CS bấm "Chuyển cho hiện trường": bãi yêu cầu có xe mới chọn vỏ · ngoài giờ · ePort lỗi · khác (ghi chú) — khách duyệt, thêm, bớt | Quy trình điều phối, mục 5.1.2.2 |
| OQ-26 | Ca trực ngoài giờ: xếp lịch theo vòng hay từng ngày; ngày không có người trực thì sao; việc dở lúc 8h chuyển cho ai; có trực cuối tuần, lễ không; một chi nhánh mấy người trực? | Quy trình điều phối, mục 4 Định nghĩa |
| OQ-27 | Gộp giao việc Lệnh hạ vỏ theo vận đơn + nơi hạ có đúng thực tế không? | Chưa có trong tài liệu khách gửi |
| OQ-28 | Ai bấm xác nhận "đã nhận tiền hoàn" tiền nâng vỏ? Quá 7 ngày chưa về thì báo ai? | Giao nhận hàng hoá (18/9/2026) |
| OQ-29 | Lưu bằng chứng khách đồng ý khoản chi ngoài định mức bằng cách nào: khách bấm trên app, ảnh tin nhắn/email, link xác nhận, hay ghi chú đã gọi? | Giao nhận hàng hoá (18/9/2026) |
| OQ-30 | Đường sắt: giá xác định lần đầu lưu vào bảng giá cho các chuyến sau, hay chỉ dùng cho chuyến đó? Khi nào áp cách nào, ai quyết? | Giao nhận hàng hoá (18/9/2026) |
| OQ-31 | Bảng loại phí × địa điểm → cách hạch toán (thu nhập chịu thuế lái xe / chi hộ / trả hộ / chi phí vận hành) cho các tuyến ngoài đường sắt | Giao nhận hàng hoá (18/9/2026) |
| OQ-32 | Bước 5 chi hộ Ratraco (thủ quỹ chuyển tiền trả lái xe) giữ thủ công hay chuyển khoản tự động? | Giao nhận hàng hoá (18/9/2026) |
| OQ-33 | Phí lưu xe quá 72 giờ và phí máy phát CBT: có muốn phần mềm tự đề xuất doanh thu không; đơn giá, đơn vị tính; giờ bắt đầu lấy từ GPS hay ảnh định vị? | Giao nhận hàng hoá (18/9/2026) |
| OQ-34 | Quá mốc vì kẹt xe, sự cố đường: có thêm nhóm nguyên nhân thứ 4 "khách quan" không? | Chưa có trong tài liệu khách gửi |
| OQ-35 | Kế hoạch ngày Ratraco gửi ngày n-1 có mẫu cố định không? Xin một mẫu thật | Giao nhận hàng hoá (18/9/2026) |
| OQ-36 | Ai duyệt mã khách DK05 cấp 2 khi CBT đổi pháp nhân thanh toán sang bên mới? | Giao nhận hàng hoá (18/9/2026) |
| OQ-37 | Lái xe chỉnh nhiệt theo yêu cầu khách có bắt buộc chụp ảnh làm bằng chứng không? | Giao nhận hàng hoá (18/9/2026) |
| OQ-38 | Khách có cần nhận thông báo ở mốc nào không: xe đã đến, đã nhận hàng, đã giao xong, quá mốc? | Chưa có trong tài liệu khách gửi |
| OQ-39 | Cảng có ePort nhưng hiện trường vẫn phải thanh lý tờ khai tại bãi: những cảng nào? | Quy trình điều phối, mục 5.4.2.2 |
| OQ-40 | Bước lấy Lệnh nâng hàng của hiện trường (FCL nhập) ghi "nhân viên CS upload": là hiện trường upload hay CS phải upload lại? | Quy trình điều phối, mục 5.4.2.4 |

## 12. Next Steps

Hoàn tất phỏng vấn phần còn lại (Mục 6.2–6.4, 7, 9, 10), duyệt sơ đồ luồng, rồi:
- `/user-flow dispatch-coordination` — user flow tổng và chia flow
- `/wireframe-ascii dispatch-coordination` hoặc `/wireframe-html dispatch-coordination`
- `/srs dispatch-coordination` — đặc tả FR, BR, Error Matrix
