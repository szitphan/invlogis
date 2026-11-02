---
type: brainstorm
feature: transport-dispatch
status: stale
status_prev: draft
updated: 2026-10-21
links:
  - docs-input/sop/giao-nhan-hang-hoa/giao-nhan-hang-hoa.md
  - docs-input/sop/sop-dieu-phoi.md
  - docs-input/sop/apas-thanh-toan-doi-soat/apas-thanh-toan-doi-soat.md
  - docs-input/sop/vis-giam-sat-doi-xe/vis-giam-sat-doi-xe.md
  - docs-input/tich-hop/vis-sim-cong-tac-chuan-bi/vis-sim-cong-tac-chuan-bi.md
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
  - docs-input/tich-hop/camera-ai-quay-cat-de-xuat-2026-08-11/camera-ai-quay-cat-de-xuat-2026-08-11.md
  - docs-input/tich-hop/gps-tien-ich-de-xuat-2025-09-25/gps-tien-ich-de-xuat-2025-09-25.md
  - docs-input/du-lieu-mau/thong-ke-chi-phi-chung-tu-cbt.md
---

# Điều vận — Lệnh vận tải từ YCVT đến khi duyệt

> Phỏng vấn xong đủ 7 phần ngày 2026-10-07 (chung với Điều phối và Cung cấp dịch vụ), cập nhật 2026-10-12 theo trả lời của Delta cho bộ câu hỏi vòng 1 (biên bản 2026-10-10) và trao đổi với khách 09/10.
> Cập nhật 2026-10-15: thêm Nhóm I, dữ liệu vận hành xe trên Lệnh, theo VIS (08/10/2026) và phỏng vấn 14–15/10. Phần dùng chung ở [[docs/vehicle-telematics/brainstorms/vehicle-telematics.md|vehicle-telematics]], phần theo xe ở [[docs/vehicle-management/brainstorms/vehicle-management.md|vehicle-management]].
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
- Không gồm (feature riêng): Bảng kê đường sắt (màn riêng); ghi nhận và bù dầu ngoài Lệnh (module Vận tải / Cấp dầu); quản lý danh mục điểm chụp ảnh, loại phí.
- Dữ liệu xe (VIS): feature này giữ phần hiện và dùng trên Lệnh (Nhóm I). Kết nối EUP, VETC, dịch vụ bản đồ, phát hiện sự việc và danh mục trạm thu phí dùng chung ở `vehicle-telematics`; km, dầu tồn, hút dầu, xe chạy ngoài Lệnh ở `vehicle-management`; định mức l/giờ ở `fuel-allowance`; nhận dầu chờ nhận ở `fuel-issuing`.
- Ngoài giai đoạn 1: quản lý vỏ container (chi phí sửa vỏ vẫn ghi trên Lệnh).
- Xử lý ngoài phần mềm: tiền hoàn nâng vỏ; quá mốc do kẹt xe, sự cố đường.
- Ứng dụng: Delta Super App, dùng chung cho nhân viên Delta và nhân viên đối tác/khách; web cho điều vận, mobile cho lái xe.

**Nguồn:** Giao nhận hàng hoá 18/9/2026, Quy trình điều phối (các mục dẫn chiếu Lệnh vận tải), tài liệu Hoá đơn trả hộ 01/10/2026, Vehicle Intelligent Service — VIS 08/10/2026 (thay bản Dữ liệu vận hành xe 30/9/2026), SIM & VIS — Công tác chuẩn bị 11/10/2026, EUP điều vận 19/9/2026, trao đổi với khách 09/10/2026, 2 báo cáo điều tra trong `docs/_research/`.

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
| Cán bộ quản lý | Khi duyệt Lệnh: duyệt bù dầu, xử lý trạm tránh | Khoảng 300 Lệnh mỗi ngày (110.000 Lệnh mỗi năm) | cao | Bù sai dầu, lái xe khiếu nại; thất thoát tiền vé |
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
- D7 [SOP+] [Gói: Đường sắt] [Cấu hình] Lệnh đường sắt hoàn tất tự vào Bảng kê đường sắt đúng kỳ `P-ky-chot-duong-sat` (Delta: ngày 25 / cuối tháng). Màn Bảng kê đường sắt là feature riêng.
- D8 [Mới] [Gói: CBT] Gợi ý hàng chiều về cho xe CBT sắp trả hàng ở miền Nam, miền Trung.

**Nhóm E — chi phí trên Lệnh (vấn đề e)**
- E3 [SOP+] [Gói: Đường sắt] [Cấu hình] Đơn giá đường sắt lấy theo `P-nguon-don-gia-duong-sat` (Delta: giai đoạn 1 CS nhập tay, giai đoạn 2 báo giá Sales). Nhập tay qua việc "Xác định giá"; Lệnh chưa có giá mang cờ "Chưa có đơn giá", còn cờ thì chặn chốt kỳ.
- E4 [SOP to-be] [Lõi] Lái xe ghi chi hộ (vd Ratraco), cân xe ngay trên Lệnh (loại phí, số tiền, ảnh); phần mềm gom bảng kê chi phí cho điều vận xác nhận, gắn nhãn "chi hộ — phải thu lại"; cân xe chọn "khách trả trực tiếp" hoặc "công ty trả".
- E5 [SOP to-be] [Lõi] [Cấu hình] [Riêng Delta] Danh mục loại phí có cách hạch toán theo địa điểm; lái xe chỉ chọn loại phí, phần mềm tự xếp và tự điền định mức từ danh mục định mức của khách (dữ liệu Riêng Delta: 150.000 ₫ Nam Khánh, 160.000 ₫ Phú Lợi).
- E7 [SOP to-be] [Lõi] Hiện trên Lệnh dữ liệu GPS: giờ đến thật, vé trạm, cờ tránh trạm, thời gian kẹt xe; dữ liệu kẹt xe gắn làm bằng chứng vào cảnh báo quá mốc. Chi tiết ở Nhóm I.
- E8 [SOP+] [Gói: CBT] [Cấu hình] Phí lưu ca xe CBT ghi nhận lên Lệnh. Đề xuất đồng hồ từ giờ đến tới giờ khởi hành, quá `P-gio-mien-phi-luu-xe` (Delta: 72 giờ) tự đề xuất dòng phí, CS xác nhận; chờ khách trả lời có cần phần mềm tự tính không (OQ-33). Phí chạy máy phát chờ giải pháp của khách.
- E9 [SOP to-be] [Lõi] Mỗi trạm vé trong danh mục được vẽ bằng hình đa giác bao trọn đoạn đường xe bắt buộc phải đi qua khi qua trạm, không dùng tâm + bán kính tròn. Lý do: vòng tròn nhỏ dễ lọt giữa hai lần GPS gửi vị trí nên bắt hụt; vòng tròn to thì trùm cả đường song song, đường gom bên cạnh nên bắt nhầm. Xe vào đa giác thì Lệnh ghi ngay "Đã qua". Trạm thu một chiều hoặc có làn vào/ra riêng được vẽ đa giác riêng cho từng chiều. Hình dạng đa giác thuộc danh mục trạm thu phí dùng chung mọi khách do đội sản phẩm duy trì (DEC-101, `vehicle-telematics` T1), không cần mã P.
- E10 [SOP+] [Lõi] [Cấu hình] Ngoài việc xét từng điểm GPS có nằm trong đa giác không, phần mềm xét thêm đoạn thẳng nối hai điểm GPS liền nhau có cắt đa giác không, để bắt được xe chạy nhanh qua trạm giữa hai lần gửi vị trí. Nếu hai điểm cách nhau quá `P-khoang-gps-toi-da` (Delta: chưa chốt, OQ-48) thì không kết luận "Tránh trạm vé": trạm đó mang cờ "Thiếu dữ liệu GPS" và chờ đối soát VETC.
- E11 [SOP+] [Gói: CBT] [Cấu hình] Danh mục loại phí CBT ghi trên Lệnh, theo bảng thống kê chi phí chứng từ CBT của Delta (03/9/2026, khoảng 35 loại), chia 2 nhóm: chi ở cửa khẩu Việt Nam; chi ở cửa khẩu Trung Quốc hoặc Campuchia. Mỗi loại có đơn vị tính (lần, ngày, đêm, lượt đi), cờ "chỉ khi phát sinh" hay luôn có, chứng từ đi kèm (hoá đơn VAT, phiếu thu, không có chứng từ). Đơn giá theo tuyến hàng (sầu riêng Thái Lan, sầu riêng Việt Nam, hàng nóng Campuchia) là dữ liệu [Riêng Delta] trong danh mục định mức (E5): lập Lệnh CBT thì tự điền các khoản luôn có thành chi phí dự kiến; lái xe thêm khoản phát sinh; khoản tính theo ngày ghi số ngày, gợi ý từ giờ vào, ra vùng bãi theo GPS (như E8). Khoản không có chứng từ thì bắt ảnh hoặc ghi chú. Chi phí Delta trả thẳng nhà cung cấp (hạ tầng cửa khẩu, dịch vụ khai báo, bãi và cân Viettel) không qua Lệnh, ghi về JobID (`service-delivery`). Tiền tệ chi ở Trung Quốc chờ khách (OQ-65).
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
- F10 [Mới] [Lõi] [Cấu hình] Xếp tổ hợp đầu kéo – mooc – container kiểm theo `P-quy-tac-ghep-mooc` (Delta: chưa chốt, OQ-66, OQ-67): mức Chặn thì không cho chọn; dữ liệu nhập từ nguồn khác (AI đọc chứng từ, sửa Lệnh) ra cấu hình Chặn thì báo đỏ, không giao lái xe; Cảnh báo, Cần hỏi có dấu. Số container kiểm chữ số cuối ISO 6346. Nguồn lab-combo, `design-system/foundations/vehicle.md` mục 5 (DEC-267).
- F11 [Mới] [Lõi] Mỗi vị trí container trên tổ hợp có trạng thái riêng, độc lập trạng thái Lệnh: Chưa có số · Vỏ rỗng · Đang đóng (chưa niêm chì) · Có hàng · Đang đổi vỏ · Kiểm hoá · Đã hạ; container lạnh thêm nhiệt độ cài và nguồn điện.

**Nhóm I — dữ liệu vận hành xe trên Lệnh (VIS 08/10/2026, phỏng vấn 14–15/10)**
- I1 [SOP to-be] [Lõi] [Cấu hình] ETA: xe rời vùng điểm đi thì tính ETA gốc và quãng đường theo cung đường ban đầu qua dịch vụ bản đồ. Trên đường, ETA tính theo quãng còn lại và vận tốc trung bình tuyến; chỉ gọi lại dịch vụ bản đồ khi kẹt xe, khi lệch cung đường quá `P-lech-cung-duong-eta` (chưa chốt; VIS ghi "x%"), hoặc mỗi `P-chu-ky-eta-cung-dai` (Delta: 30 phút) với cung dài hơn `P-cung-dai-eta` (Delta: 300 km). Dịch vụ bản đồ lỗi thì ghi "ETA ước tính". CS xem ETA để báo khách khi sắp trễ mốc.
- I2 [SOP to-be] [Lõi] Giờ đến thật tự ghi khi xe vào vùng từng điểm giao nhận; sắp trễ hoặc trễ mốc thì cảnh báo như B6.
- I3 [SOP to-be] [Lõi] [Cấu hình] Kẹt xe trong Lệnh: máy nổ, xe nhích dưới `P-van-toc-ket-xe` (Delta: 5 km/h), quá `P-thoi-gian-ket-xe` (Delta: 10 phút). Xe đứng yên hẳn là nổ máy ngủ, gắn vào Lệnh, không bù; đứng yên có dấu hiệu kẹt cứng thì vẫn tính kẹt xe (cách phân loại: `vehicle-telematics` S2–S4; chờ khách, OQ-53). Thời gian kẹt xe làm bằng chứng cho cảnh báo quá mốc.
- I4 [SOP to-be] [Gói: Nhiên liệu] Đề xuất bù dầu kẹt xe = số phút kẹt × định mức nổ máy không chạy (l/giờ) của xe, hiện "Đề xuất bù dầu do kẹt xe: [x] lít" trên Lệnh. Định mức l/giờ ở `fuel-allowance` (chờ khách, `vehicle-telematics` OQ-12). Xếp hàng chờ trong vùng cảng, bãi, kho có được bù không theo `P-bu-dau-xep-hang` (chờ khách, OQ-52).
- I5 [SOP to-be] [Lõi] [Cấu hình] Tìm vỏ rỗng qua nhiều bãi, chỉ áp Lệnh thuộc JobID hàng xuất FCL: xe rời bãi nhận vỏ trên Lệnh, chưa tới nơi đóng hàng mà ở bãi khác trong danh mục quá `P-thoi-gian-o-bai-tim-vo` (Delta: 10 phút) thì ghi bãi vào lịch trình phụ. Km phát sinh = km GPS thực tế từ bãi nhận vỏ tới nơi đóng hàng trừ km cung đường trên Lệnh. Chỉ dùng GPS, lái xe không phải báo. Km phát sinh ra số âm (bãi vỏ khác gần nơi đóng hàng hơn, đi đường tắt) thì tính 0: không bù, không trừ (review v1).
- I6 [SOP to-be] [Gói: Nhiên liệu] Dầu bù tìm vỏ = km phát sinh × định mức mức tải "Đầu kéo không" của xe (`fuel-allowance`), hiện "Đề nghị cấp bù dầu do chọn container rỗng ở nhiều bãi: [x] lít" kèm bảng lịch trình phụ (Bãi A → B → C, km phát sinh, số lít).
- I7 [SOP+] [Lõi] [Cấu hình] Khớp vé từng trạm: giao dịch thu phí về tới đâu thì ghép với lượt "Đã qua" trạm đó của Lệnh tới đó, ghi tiền vé lên Lệnh ngay. Trạm xét theo bản danh mục có hiệu lực lúc xe qua trạm, không theo bản sửa sau đó. Lệnh hết chạy khi xe đã qua các điểm giao nhận theo thứ tự rồi mới vào vùng điểm cuối; chạm vùng điểm cuối trước đó (điểm cuối trùng điểm đi, xe đi ngang) không tính. Lệnh hết chạy thì chốt các trạm còn lại: trạm trên cung đường mà GPS không qua, không có giao dịch là tránh trạm; đã qua mà chưa có giao dịch thì tra lại sau `P-quet-lai-vetc` (Delta: 120 phút), vẫn chưa có thì "Chờ VETC", kiểm nốt cuối kỳ; có giao dịch ở trạm không nằm trên cung đường là "Ngoài cung đường". Đơn vị thu phí không gửi giao dịch ngay thì chỉ tra một lần lúc Lệnh hết chạy (OQ-49, OQ-51). Lái xe trả tiền mặt tại trạm (hết tiền tài khoản giao thông, trạm không thu tự động): đề xuất lái xe ghi khoản chi hộ (E4), chọn trạm, chụp biên lai; trạm đó thành "Đã qua", không chờ giao dịch VETC (OQ-58).
- I8 [SOP+] [Lõi] [Cấu hình] Tránh trạm và ngoài cung đường chốt theo từng Lệnh. [Lõi]: phát hiện, ghi nhận, người duyệt Lệnh xem. [Cấu hình] `P-tinh-tien-tranh-tram` (Delta: bật): người duyệt chọn "Tính cho lái xe" hoặc "Chấp nhận" kèm lý do (đổi cung đường đã duyệt, đường cấm…); `P-chan-duyet-khi-con-tram` (Delta: bật): còn trạm chưa xử lý thì chưa duyệt được Lệnh (review r14). Lệnh chưa hết chạy thì chưa duyệt được; trạm "Chờ VETC" không chặn duyệt. Lệnh đã duyệt có khối "Điều chỉnh sau duyệt": mỗi dòng ghi khoản, số cũ → số mới, lý do, nguồn (vé VETC về muộn, khiếu nại, xem lại sự việc), người, ngày; không sửa số gốc. Chi phí đổi thì JobID cập nhật, báo kế toán (cùng OQ-51); dầu đổi thì cộng, trừ dầu chờ nhận; khoản lái xe đổi thì sửa bảng kê (kỳ chưa chốt sửa ngay, đã chốt vào kỳ sau). Trạm đã "Tính cho lái xe" mà vé VETC về muộn: xe không tránh trạm, tự huỷ khoản qua một dòng điều chỉnh, báo lái xe (review v4b, v5). Kết quả là nguồn bảng kê tránh trạm theo lái xe theo kỳ cho bộ phận lương (OQ-50).
- I9 [Mới] [Gói: Nhiên liệu] Người duyệt Lệnh sửa được số lít bù, bắt ghi lý do; Lệnh giữ cả số đề xuất và số được duyệt. Dầu định mức của Lệnh tính theo từng đoạn: đoạn rỗng dùng mức "Đầu kéo không" hoặc "Vỏ container rỗng", đoạn có hàng dùng mức theo trọng lượng hàng (8 mức tải của định mức khoán, `fuel-allowance`). Lệnh hiện 2 số: dầu theo cung đường ban đầu (km cung đường trên Lệnh) và dầu theo cung đường thực tế (km GPS); dầu chờ nhận theo cung đường trên Lệnh (đổi cung đã duyệt thì theo cung mới, F3); số theo GPS chỉ để so, lệch quá `P-lech-km-gps-lenh` (chưa chốt) thì báo người duyệt Lệnh. Không cấp theo GPS vì km tìm vỏ đã bù riêng ở I6 sẽ bị tính 2 lần, và mất GPS thì cấp thiếu (review v2). Xe chưa có định mức: vẫn lập được Lệnh, phần mềm cảnh báo và cho 2 lựa chọn độc lập với một xe cùng loại xe theo vận hành: dùng tạm định mức đó cho Lệnh này (có/không), và gửi yêu cầu cập nhật thông tin phương tiện – định mức nhiên liệu để áp luôn cho xe (có/không); yêu cầu duyệt như sửa hồ sơ xe (`vehicle-management` H1; SRS LG UC04.01.19, UC04.01.21) (review v3). Duyệt Lệnh thì dầu định mức của Lệnh cộng dầu bù đã duyệt vào "dầu chờ nhận" của lái xe, nhận qua phiếu cấp dầu vận tải (Delta: dGas3); mỗi lần nhận không vượt chỗ trống trong bình theo cảm biến (xe không có cảm biến: không vượt dung tích bình), phần còn lại để lần sau (`fuel-issuing`).
- I10 [Mới] [Lõi] Dự toán vé: lập Lệnh thì dò các trạm thu phí trên cung đường từ danh mục dùng chung (`vehicle-telematics` T1), tính tiền vé theo nhóm xe của tổ hợp đầu kéo, mooc, container (20 hay 40 feet) trên Lệnh, cộng vào chi phí dự kiến của Lệnh. Chạy xong so dự toán với vé thật, chỉ ra trạm lệch.
- I11 [SOP+] [Lõi] Dữ liệu GPS khi Lệnh thay đổi: Lệnh bị trả lại giữ nguyên kết quả đối soát và không nhận sự việc GPS mới, sự việc mới gắn Lệnh đang chạy kế tiếp của xe; đổi cung đường thì tính lại trạm dự toán, trạm của cung cũ không bị coi là tránh trạm; không huỷ được Lệnh đang thực hiện: khách huỷ giữa chặng thì lái xe báo vấn đề (F1), Lệnh kết thúc sớm, vẫn chốt và duyệt như thường, dầu định mức, bù dầu, vé tính theo phần đường đã chạy; GPS hỏng không vào được vùng điểm cuối thì lái xe bấm hoàn thành, Lệnh ghi "Kết thúc theo lái xe"; cả Lệnh không có dữ liệu GPS thì không đề xuất bù kẹt xe, vé theo giao dịch thu phí.
- I12 [SOP to-be] [Lõi] Báo cáo theo kỳ (tháng, hoặc khoảng ngày tuỳ ý): km GPS so với km trên Lệnh theo Lệnh, xe, lái xe; bảng kê tránh trạm theo lái xe; bù dầu đề xuất so với được duyệt theo Lệnh, lái xe, người duyệt.
- I13 [Mới] [Lõi] [Cấu hình] Lệnh hết chạy quá `P-han-duyet-lenh` (chưa chốt, OQ-59) chưa duyệt: nhắc người duyệt, báo trưởng điều vận, để dầu chờ nhận của lái xe không bị treo. Hai người cùng duyệt bù dầu hoặc cùng xử lý một trạm: người lưu sau thấy ai đã làm lúc nào, không ghi đè.
- I14 [Mới] [Lõi] [Cấu hình] Lái xe nhận thông báo trên app khi bị tính tiền tránh trạm, ngoài cung đường hoặc bị ghi vi phạm; màn "Số liệu của tôi" theo tháng: vé, bù dầu, nổ máy ngủ, vi phạm, dầu chờ nhận. Khiếu nại: khoản khiếu nại được là tránh trạm, ngoài cung đường, hút dầu Vi phạm, chạy ngoài Lệnh, lệch dầu Lỗi lái xe, bù dầu kẹt xe bị giảm hoặc Không bù, dầu định mức sai, nổ máy ngủ. Lái xe bấm Khiếu nại (lý do theo loại khoản, ghi chú, ảnh) trong `P-han-khieu-nai` ngày (chưa chốt); kỳ đã chốt vẫn khiếu nại được trong hạn. Khoản thành "Đang khiếu nại", rút khỏi bảng kê lương tới khi có kết quả. Khoản trên Lệnh (tránh trạm, ngoài cung đường, bù dầu, dầu định mức): người ra quyết định gốc chọn Giữ · Huỷ · Sửa số kèm lý do. Sự việc (hút dầu, chạy ngoài Lệnh, lệch dầu thực đổ): đi theo cơ chế xem lại của `vehicle-telematics` X1 (Giữ kết quả · Đổi kết quả). Phần mềm báo lái xe kết quả; bị Giữ thì lái xe được leo thang 1 lần lên trưởng bộ phận. Mỗi khoản khiếu nại 1 lần; quá hạn xem lại thì nhắc, rồi báo cấp trên. Chấp nhận thì ghi một dòng "Điều chỉnh sau duyệt" trên Lệnh (I8); kỳ đã chốt thì điều chỉnh vào kỳ sau. Chờ khách chốt luồng (OQ-60).

**Nhóm Q — quay cắt container tại nhà máy (Camera AI 11/8/2026 mục 1, 3; ghi nhận bằng GPS thay Camera AI, chốt 20/10)**
- Q1 [SOP+] [Lõi] [Cấu hình] Quay cắt là việc đầu kéo đặt sẵn tại nhà máy kéo container (đang trên mooc) vào cửa kho để đóng, dỡ hàng và kéo ra vị trí chờ, để xe đường dài để mooc lại mà không phải chờ (cắt mooc). Nhà máy có quay cắt khai trong danh mục địa điểm: vùng nhà máy (đa giác), các đầu kéo quay cắt được phân công. Bật/tắt theo `P-quay-cat` (Delta: bật). Đầu kéo quay cắt làm việc không theo Lệnh: còn trong vùng nhà máy được phân công thì không bị cảnh báo chạy ngoài Lệnh (`vehicle-telematics` S8).
- Q2 [Mới] [Lõi] [Cấu hình] Tự ghi lượt quay cắt bằng GPS: đầu kéo quay cắt ghép với một mooc trong vùng nhà máy rồi tách khỏi mooc đó vẫn trong vùng (`vehicle-telematics` M2) là một lượt. Lượt ghi đầu kéo, lái xe đang giữ xe (lịch sử bàn giao), mooc, container trên mooc (theo Lệnh đang gắn mooc), giờ ghép, giờ tách. Mooc đi chưa tới `P-quang-toi-thieu-quay-cat` (chưa chốt, OQ-61) thì không tính (móc thử). Một lượt là một chiều hay khứ hồi: chờ khách (OQ-61).
- Q3 [SOP+] [Lõi] Container của lượt thuộc Lệnh đang mở của mình (cắt mooc: lượt đi đã để mooc tại nhà máy) thì lượt tự ghi vào Lệnh chính đó làm chi phí quay cắt, không ai phải bấm.
- Q4 [SOP+] [Lõi] Container không do mình phục vụ: mooc của đơn vị khác không có thiết bị GPS nên GPS chỉ thấy đầu kéo. Lái xe bấm "Quay cắt" trên App: chụp số container (phần mềm đọc số), chọn đơn vị thuê quay cắt từ danh mục đối tác (chưa có thì nhập tên, chờ CS tạo đối tác). Phần mềm đối chiếu trong khoảng lái xe bấm đầu kéo có di chuyển trong vùng nhà máy không: khớp thì lượt hợp lệ, không khớp thì cờ "Chờ xác nhận" cho trưởng điều vận. Mooc của mình mà mất tín hiệu GPS cũng đi đường này. Lượt cho đơn vị khác là doanh thu: gom theo đơn vị và kỳ thành bảng kê quay cắt để lập chứng từ thanh toán với bên thuê (`debt-management`).
- Q5 [SOP+] [Lõi] [Cấu hình] Lương và dầu theo lượt: lượt hợp lệ vào bảng kê lương lái xe theo `P-don-gia-luong-quay-cat` (chưa chốt, OQ-62); khi bật Gói Nhiên liệu, cộng dầu theo `P-dinh-muc-dau-quay-cat` (chưa chốt, OQ-62) vào dầu chờ nhận của lái xe (`fuel-allowance`). Đơn giá thu của đơn vị thuê theo hợp đồng với từng đơn vị (dữ liệu khách). Lái xe thấy lượt của mình trong "Số liệu của tôi", lượt bị loại thì khiếu nại theo I14.
- Q6 [Mới] [Lõi] [Cấu hình] Trường hợp đặc biệt: (a) cùng mooc ghép, tách liên tiếp trong `P-gop-luot-quay-cat` (chưa chốt, OQ-61) do chỉnh vị trí thì gộp một lượt; (b) đầu kéo quay cắt kéo mooc ra khỏi vùng nhà máy thì không còn là quay cắt: lượt dừng, báo điều vận (chuyến kéo cần Lệnh); (c) cùng mooc, cùng khoảng giờ có cả lượt GPS và lượt lái xe bấm: giữ lượt GPS, bỏ bản bấm tay; (d) lượt GPS không xác định được container (mooc chưa gắn Lệnh nào): cờ "Thiếu container", lái xe bổ sung trên App như Q4; (e) đổi ca giữa ngày: lượt thuộc lái xe đang giữ xe lúc ghép; (f) dữ liệu về muộn: tính theo giờ thật (`vehicle-telematics` G1).
- Q7 [SOP+] [Lõi] Báo cáo theo kỳ: lượt theo lái xe, nhà máy, đơn vị thuê, Lệnh chính; lượt "Chờ xác nhận", "Thiếu container" còn treo; tổng lương, dầu, doanh thu quay cắt.

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
--> Chốt Lệnh --> (PM) vào Bảng kê đường sắt kỳ 25 / cuối tháng
                  còn cờ "Chưa có đơn giá" --> chặn chốt kỳ
```

### 5.5 Lệnh chạy có dữ liệu GPS và đối soát vé

1. Lái xe nhận Lệnh. Xe rời vùng điểm đi: ghi giờ khởi hành, tính ETA gốc và quãng đường theo cung đường ban đầu; dầu định mức của Lệnh = km từng đoạn × mức tải của đoạn đó (I9).
2. Trên đường: kẹt xe cộng đề xuất bù dầu; đứng yên hẳn là nổ máy ngủ (trừ khi có dấu hiệu kẹt cứng); ETA tính lại (I1, I3).
3. Xe qua trạm: ghi "Đã qua"; giao dịch thu phí về thì khớp, ghi tiền vé lên Lệnh (I7).
4. Xe vào vùng từng điểm giao nhận: ghi giờ đến thật; trễ mốc thì cảnh báo (I2, B6).
5. Xe đã qua đủ các điểm giao nhận theo thứ tự rồi vào vùng điểm cuối: Lệnh hết chạy, chốt danh sách trạm: tránh trạm, ngoài cung đường, chờ VETC (I7).
6. Người duyệt Lệnh xem khối "Dữ liệu hành trình": duyệt bù dầu (sửa được, ghi lý do), xử lý trạm tránh, rồi duyệt Lệnh (I8, I9).
7. Duyệt Lệnh: dầu định mức của Lệnh và dầu bù đã duyệt vào dầu chờ nhận của lái xe; lái xe nhận qua phiếu cấp dầu vận tải.

```
 LÁI XE, XE              PHẦN MỀM                            VETC
 ──────────              ────────                            ────
 Nhận Lệnh
 Rời vùng điểm đi ─────► Ghi giờ khởi hành
                         Tính ETA gốc, quãng đường theo cung đường ban đầu
                         Dầu định mức = km từng đoạn × mức tải của đoạn
 Chạy trên đường ──────► Nhận vị trí, tốc độ, máy (EUP)
                         ◇ Máy nổ quá 10 phút, xe nhích dưới 5 km/h?
                         ├─ Có ─► Kẹt xe: cộng đề xuất bù dầu, tính lại ETA
                         └─ Không ─► ◇ Máy nổ quá 10 phút, đứng yên hẳn?
                                     ├─ Có ─► ◇ Kẹt cứng?
                                     │        ├─ Có ─► Kẹt xe
                                     │        └─ Không ─► Nổ máy ngủ (gắn Lệnh)
                                     └─ Không ─► ETA theo vận tốc trung bình
 Qua trạm ─────────────► Trạm: Dự toán ─► Đã qua
                         ◄──────────────────────────────── Giao dịch trừ tiền (gửi về ngay)
                         ◇ Có giao dịch của xe ở trạm này?
                         ├─ Có ─► Khớp, ghi tiền vé lên Lệnh
                         └─ Chưa ─► Để chốt khi Lệnh hết chạy
 Vào vùng điểm giao ───► Ghi giờ đến thật
                         ◇ Trễ mốc? ─ Có ─► Cảnh báo quá mốc (B6)
 Vào vùng điểm cuối ───► ◇ Đã qua đủ điểm giao nhận theo thứ tự?
 (sau điểm giao cuối)    └─ Có ─► Lệnh hết chạy: chốt danh sách trạm
                         Trạm chưa khớp ──────────────────► Tra theo khung giờ Lệnh
                         ◇ GPS đã qua mà VETC vẫn chưa có?
                         ├─ Có ─► Chờ 120 phút, tra lại
                         │        vẫn chưa có ─► Chờ VETC (kiểm cuối kỳ)
                         └─ Không ─► Tránh trạm · Ngoài cung đường
                         Bù dầu: Đang ghi ─► Chờ duyệt
 NGƯỜI DUYỆT LỆNH
 Xem Dữ liệu hành trình ◄── Đề xuất bù dầu, danh sách trạm
 Duyệt bù dầu (sửa được, ghi lý do)
 Xử lý trạm tránh: tính lái xe · chấp nhận
 Duyệt Lệnh ───────────► Dầu chờ nhận của lái xe (phiếu cấp dầu vận tải)
                         = dầu định mức của Lệnh + dầu bù đã duyệt
 Lái xe nhận dầu ◄───── Mỗi lần không vượt chỗ trống trong bình
```

### 5.6 Tìm vỏ rỗng qua nhiều bãi (Lệnh hàng xuất FCL)

1. Xe vào vùng bãi nhận vỏ ghi trên Lệnh: ghi giờ đến.
2. Lấy được vỏ ngay: không có km phát sinh.
3. Xe rời bãi đó, chưa tới nơi đóng hàng mà ở bãi khác trong danh mục quá 10 phút: ghi bãi vào lịch trình phụ.
4. Xe tới nơi đóng hàng: tính km phát sinh, dầu bù theo mức "Đầu kéo không" (I5, I6).
5. Lịch trình phụ (Bãi A → B → C, km, lít) hiện trên Lệnh; người duyệt duyệt cùng Lệnh.

### 5.7 Dự toán vé khi lập Lệnh

1. Điều vận chọn cung đường và xe cho Lệnh.
2. Phần mềm dò các trạm thu phí trên cung đường, tính tiền vé theo loại xe; Lệnh hiện tiền vé dự toán trong chi phí dự kiến.
3. Chạy xong: so dự toán với vé thật, chỉ ra trạm lệch (đi trạm khác, tránh trạm, giá đổi).

## 6. System Behavior Deep Dive

### 6.1 Decision Points

| ID | Flow | Khi nào | YES (nhánh đồng ý) | NO (nhánh từ chối) |
|---|---|---|---|---|
| DP-07 | Air nhập | Đã về đủ kiện | Giao xe | Chặn giao xe tới khi CS chọn cách xử lý |
| DP-08 | CFS nhập | Kho xác nhận hàng sẵn sàng | Giao xe | Cảnh báo, vẫn giao xe được |
| DP-09 | Chạy Lệnh | Đủ ảnh tại điểm bắt buộc | Qua bước tiếp | Chặn bước tiếp |
| DP-11 | Chốt Lệnh | Đủ việc, chứng từ, chi phí | Chờ duyệt | Chặn chốt, chỉ ra phần thiếu |
| DP-12 | Đường sắt | Lệnh có đơn giá | Vào kỳ chốt | Cờ "Chưa có đơn giá", chặn chốt kỳ |
| DP-13 | Chạy Lệnh | Máy nổ quá 10 phút, xe nhích dưới 5 km/h | Kẹt xe, cộng đề xuất bù dầu | Đứng yên hẳn: xét kẹt cứng, không có thì nổ máy ngủ gắn Lệnh |
| DP-14 | Chạy Lệnh | Có giao dịch thu phí của xe ở trạm vừa qua | Khớp, ghi tiền vé | Để chốt khi Lệnh hết chạy |
| DP-15 | Lệnh hết chạy | Trạm trên cung đường mà GPS không qua, không có giao dịch | Tránh trạm, người duyệt xử lý | — |
| DP-16 | Lệnh hết chạy | GPS đã qua mà chưa có giao dịch | Tra lại sau 120 phút; vẫn chưa có thì "Chờ VETC" | Khớp |
| DP-17 | Duyệt Lệnh | Lệnh chưa hết chạy, còn trạm tránh, ngoài cung đường chưa xử lý, hoặc bù dầu chưa duyệt (trạm "Chờ VETC" không chặn) | Chặn duyệt, chỉ ra phần còn thiếu | Duyệt được |
| DP-18 | Duyệt Lệnh | Người duyệt sửa số lít bù | Bắt ghi lý do | Duyệt số đề xuất |
| DP-19 | Tìm vỏ | Lệnh hàng xuất FCL, xe ở bãi khác quá 10 phút trước nơi đóng hàng | Ghi lịch trình phụ, tính km phát sinh | Không có km phát sinh |

### 6.2 Scenario Matrix

Ai được đổi trạng thái gì, ở trạng thái nào.

| Đối tượng | Từ | Sang | Ai làm | Điều kiện | Kết quả |
|---|---|---|---|---|---|
| YCVT | Đã được tạo | Đã lập Lệnh vận tải | Điều vận | Lập đủ số Lệnh đã khai | Hiện "đã lập x/n Lệnh" tới khi đủ |
| Lệnh | Đã lập | Huỷ | Điều vận | Lái xe chưa nhận | Trả số xe lại cho YCVT |
| Lệnh | Đã giao lái xe | Đã lập | Lái xe | Từ chối, bắt chọn lý do | Báo điều vận giao lại |
| Lệnh | Lái xe đã nhận | Đang thực hiện | Phần mềm hoặc lái xe | GPS ghi nhận xe khởi hành; không có GPS thì lái xe bấm "Bắt đầu" | Bắt đầu theo dõi mốc |
| Lệnh | Đang thực hiện | Lái xe đã chốt | Lái xe | Đủ ảnh, chứng từ, chi phí | Chờ duyệt |
| Lệnh | Đang thực hiện | Lái xe đã chốt (kết thúc sớm) | Lái xe | Khách huỷ giữa chặng, lái xe báo vấn đề (F1); không huỷ được Lệnh đang thực hiện | Chốt, duyệt như thường; dầu, vé theo phần đường đã chạy |
| Lệnh | Lái xe đã chốt | Đã duyệt | Điều vận hoặc cán bộ quản lý (1 người là đủ) | — | Chi phí chuyển lên JobID |
| Lệnh | Lái xe đã chốt | Đang thực hiện | Điều vận hoặc cán bộ quản lý | Trả lại, bắt ghi lý do | Lái xe bổ sung |
| JobID | Đã tạo YCVT | Đã thực hiện Lệnh vận tải | Phần mềm | Mọi Lệnh của JobID đã duyệt | Sang `service-delivery` để hoàn thành dịch vụ |
| Cảnh báo | Mới | Đã có người nhận | Điều vận hoặc CS | Ai bấm "Nhận xử lý" trước giữ việc | Hiện tên người giữ |
| Cảnh báo | Đã có người nhận | Đã xử lý | Người giữ cảnh báo | Bắt chọn nhóm nguyên nhân | Đóng cảnh báo |
| Cảnh báo | Mới / Đã có người nhận | Đã leo thang | Phần mềm | Quá hạn chưa xử lý | Báo trưởng điều vận |

Phân loại trạm trên Lệnh (VIS mục 3.1.3 bước 3, bổ sung đủ tổ hợp):

| Trạm trên cung đường? | GPS | Giao dịch thu phí | Kết quả |
|---|---|---|---|
| Có | Qua | Có | Khớp, ghi tiền vé lên Lệnh |
| Có | Qua | Chưa có | Tra lại sau 120 phút, rồi Khớp hoặc "Chờ VETC" |
| Có | Không qua | Không có | Tránh trạm, người duyệt xử lý |
| Có | Không qua | Có | Khớp theo giao dịch, ghi "GPS không bắt được trạm" |
| Có | Mất dữ liệu | Không có | "Không đủ dữ liệu", người duyệt xem |
| Không | Qua | Có | Ngoài cung đường, người duyệt chấp nhận hoặc tính lái xe |
| Không | — | Có, ngoài khung giờ mọi Lệnh | Vé mồ côi, kiểm phát sinh cuối kỳ (`invoice-management`) |

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

**Trạm trên Lệnh**

```
Dự toán --> Đã qua --> Khớp
   |           |
   |           +--> Chờ VETC (tra lại sau 120 phút) --> Khớp, hoặc kiểm nốt cuối kỳ
   |
   +--> Tránh trạm (Lệnh hết chạy, không qua, không có giao dịch) --> Tính cho lái xe / Chấp nhận (có lý do)
Ngoài cung đường (có giao dịch, trạm không trên cung đường) --> Tính cho lái xe / Chấp nhận (có lý do)
```

Xử lý trạm tránh, ngoài cung đường mở lại được trước khi duyệt Lệnh. Đổi cung đường thì danh sách dự toán tính lại. Giao dịch về sau khi Lệnh đã duyệt: một dòng "Điều chỉnh sau duyệt" (I8).

**Đề xuất bù dầu**

```
Đang ghi --> Chờ duyệt (Lệnh hết chạy) --> Đã duyệt (giữ hoặc sửa số, có lý do) --> Chờ nhận (Lệnh được duyệt)
                                    \--> Không bù (có lý do)
```

Đã duyệt, Không bù mở lại được trước khi duyệt Lệnh.

Vòng đời YCVT xem `shipment-coordination` Mục 6.3; feature này đổi YCVT sang "Đã lập Lệnh vận tải" và "Đã thực hiện Lệnh vận tải".

### 6.4 Interrupted Transactions

| # | Tình huống | Xử lý |
|---|---|---|
| 1 | Mất sóng hoặc tắt app khi lái xe đang chụp ảnh, ghi biên bản, nhập nhiệt độ | Lưu trên máy, tự đồng bộ khi có sóng. Giờ và vị trí lấy theo lúc chụp, không phải lúc gửi. Lệnh hiện nhãn "Chờ đồng bộ" |
| 2 | GPS mất tín hiệu | Không tự đánh dấu "đã đến"; lái xe bấm tay kèm ảnh định vị. Hết dữ liệu GPS cho Lệnh thì báo điều vận. Đề xuất lái xe chụp ảnh định vị tại từng mốc (OQ-54) |
| 3 | Hai điều vận cùng lập Lệnh từ 1 YCVT khi chỉ còn 1 xe | Người lưu trước được; người sau nhận E-transport-dispatch-004 |
| 4 | Hai người cùng xử lý một cảnh báo | Ai bấm "Nhận xử lý" trước giữ việc; người sau thấy tên người đang giữ (E-transport-dispatch-005) |
| 5 | D/O đổi kho khi xe đang chạy | Lệnh cập nhật nơi nhận, báo điều vận và lái xe (D4 ở `shipment-coordination`) |
| 6 | Sửa JobID (đổi Booking Note, giảm container) khi đã có Lệnh | Lệnh dư chưa giao lái xe thì tự huỷ; đã giao thì báo điều vận xử lý tay |
| 7 | Mất dữ liệu GPS đúng đoạn qua trạm | Có giao dịch thu phí: coi là Khớp (VETC là nguồn chuẩn, F8). Không có: "Không đủ dữ liệu", không kết luận tránh trạm, người duyệt xem (cùng cờ "Thiếu dữ liệu GPS" ở E10) |
| 8 | Cả Lệnh không có dữ liệu GPS (thiết bị hỏng) | "Không có dữ liệu GPS", không đề xuất bù kẹt xe, vé theo giao dịch thu phí; báo quản lý phương tiện kiểm tra thiết bị |
| 9 | Đơn vị thu phí lỗi, chậm | Tra lại sau 120 phút; vẫn lỗi thì "Chờ VETC", Lệnh vẫn duyệt được, kiểm nốt cuối kỳ (OQ-51) |
| 10 | Dịch vụ bản đồ lỗi | ETA theo vận tốc trung bình tuyến, ghi "ETA ước tính" |
| 11 | Lệnh bị trả lại cho lái xe bổ sung | Giữ nguyên kết quả đối soát vé, bù dầu; không tra lại giao dịch; không nhận sự việc GPS mới, sự việc mới gắn Lệnh đang chạy kế tiếp của xe |
| 12 | Đổi cung đường, khách huỷ giữa chặng (Lệnh kết thúc sớm), GPS hỏng không vào được vùng điểm cuối | Như I11 |
| 13 | Danh mục trạm sửa (trạm ngừng thu, sửa vùng) trong lúc Lệnh đang chạy | Trạm xét theo bản có hiệu lực lúc xe qua trạm (I7) |

### 6.5 Other Edge Cases

- Air nhập tách chuyến bay: mỗi đợt hàng về là 1 Lệnh mới dưới cùng JobID.
- Mất sóng tại điểm giao: biên bản giao hàng vẫn ghi được, đồng bộ sau.
- Thay đổi giữa chặng (cung đường, giờ giao, điểm giao, khách huỷ, thiếu hàng): ghi trên Lệnh, báo điều vận và quản lý, kéo theo chi phí, dầu, chứng từ (F1–F3).
- Hàng quay cắt: xử lý ở Nhóm Q (Q1–Q7); còn chờ OQ-61 đến OQ-64.
- Xếp hàng chờ ở cổng cảng, bãi, kho mà máy vẫn nổ: có bù dầu như kẹt xe không (OQ-52).
- Tai nạn, kẹt cứng không nhích được: đứng yên hẳn vẫn tính kẹt xe khi có dấu hiệu ở `vehicle-telematics` S4 (OQ-53).
- Đổi xe giữa chặng: chắc không xảy ra; nếu có, sự việc trước lúc đổi gắn xe cũ, sau đó gắn xe mới, vé tra theo khung giờ từng xe (OQ-55).
- 2 container 20 feet của 2 Lệnh trên cùng một xe: kẹt xe, vé trong khoảng chạy chung chia đều cho 2 Lệnh; dầu bù tìm vỏ chỉ tính cho Lệnh có bãi nhận vỏ đó (OQ-56).

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
| Vùng trạm vé (danh mục) | Đa giác khép kín, ít nhất 3 đỉnh, không tự cắt; mỗi trạm có ít nhất 1 đa giác |
| Số lít bù được duyệt | Số không âm; khác số đề xuất thì bắt lý do |
| Lý do chấp nhận trạm tránh, ngoài cung đường | Bắt buộc, tối đa 1000 ký tự |
| Nhận dầu chờ nhận | Mỗi lần không vượt chỗ trống trong bình theo cảm biến (xe không có cảm biến: dung tích bình) |

### 7.2 Limits & Quotas (exact values)

| Tham số | Giá trị | Window | Behavior khi vượt |
|---|---|---|---|
| Lưu xe CBT miễn phí (`P-gio-mien-phi-luu-xe`) | Delta: 72 giờ | từ giờ đến tới giờ khởi hành | Đề xuất dòng phí, CS xác nhận (chờ OQ-33) |
| Kỳ chốt đường sắt (`P-ky-chot-duong-sat`) | Delta: ngày 25 và cuối tháng | tháng | Còn cờ "Chưa có đơn giá" thì chặn chốt kỳ |
| Định mức depot đường sắt (danh mục định mức, dữ liệu Riêng Delta) | 150.000 ₫ Nam Khánh; 160.000 ₫ Phú Lợi | mỗi lượt | Tự điền khi lái xe chọn loại phí |
| Chu kỳ nhắc nhật ký nhiệt (`P-chu-ky-nhac-nhiet`) | Chưa có số (OQ-43) | theo loại hàng, chỉnh được trên từng Lệnh | Nhắc lái xe; quá giờ chưa nhập thì báo điều vận |
| Khoảng hở GPS tối đa (`P-khoang-gps-toi-da`) | Chưa có số (OQ-48) | giữa 2 điểm GPS liền nhau | Không kết luận tránh trạm; gắn cờ "Thiếu dữ liệu GPS", chờ đối soát VETC |
| Kẹt xe (`P-van-toc-ket-xe`, `P-thoi-gian-ket-xe`) | Delta: dưới 5 km/h, quá 10 phút (chờ xác nhận, OQ-57) | liên tục | Ghi kẹt xe, đề xuất bù dầu |
| Đứng yên giữa 2 đoạn kẹt (`P-khoang-dung-giua-ket-xe`) | Chưa có số (OQ-57) | giữa 2 đoạn kẹt | Vẫn tính kẹt xe |
| Tra lại giao dịch thu phí (`P-quet-lai-vetc`) | Delta: 120 phút | sau khi Lệnh hết chạy | "Chờ VETC" |
| Ở bãi khác khi tìm vỏ (`P-thoi-gian-o-bai-tim-vo`) | Delta: 10 phút | mỗi bãi | Ghi vào lịch trình phụ |
| Tính lại ETA cung dài (`P-cung-dai-eta`, `P-chu-ky-eta-cung-dai`) | Delta: cung trên 300 km, mỗi 30 phút | — | Gọi lại dịch vụ bản đồ |
| Lệch cung đường (`P-lech-cung-duong-eta`) | Chưa có số; VIS ghi "x%" (OQ-57) | — | Gọi lại dịch vụ bản đồ |
| Bù dầu khi xếp hàng chờ (`P-bu-dau-xep-hang`) | Chờ khách (OQ-52) | — | Bật thì bù như kẹt xe |

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
| E-transport-dispatch-008 | Popup | Duyệt Lệnh khi còn trạm tránh, ngoài cung đường chưa xử lý | **Chưa duyệt được Lệnh** · "Còn [n] trạm tránh chưa xử lý. Chọn cách xử lý từng trạm rồi duyệt Lệnh." |
| E-transport-dispatch-009 | Popup | Duyệt Lệnh khi đề xuất bù dầu chưa duyệt | **Chưa duyệt được Lệnh** · "Đề xuất bù dầu chưa được duyệt. Duyệt hoặc bỏ đề xuất rồi duyệt Lệnh." |
| E-transport-dispatch-010 | Inline | Số lít bù âm | "Số lít bù không được âm." |
| E-transport-dispatch-011 | Inline | Nhận dầu vượt chỗ trống trong bình | "Tối đa [x] lít, theo dung tích bình còn trống." |
| E-common-001 | Inline | Bỏ trống lý do (sửa số lít bù, chấp nhận trạm tránh) | "Nhập lý do." |
| E-common-009 | Toast | Mất mạng | Dùng câu chung |
| E-common-008 | Toast | Lỗi hệ thống | Dùng câu chung |

#### Success messages

- "Đã lập Lệnh [mã]" · "Đã chốt Lệnh" · "Đã duyệt Lệnh" · "Đã gửi biên bản cho CS và khách"
- "Đã duyệt bù dầu [x] lít" · "Đã bỏ đề xuất bù dầu" · "Đã xử lý trạm [tên trạm]"

Xác nhận (Xem CMP-03):

| Tình huống | Tiêu đề · nội dung | Nút |
|---|---|---|
| Huỷ Lệnh | **Huỷ Lệnh [mã]?** · "Số xe sẽ trả lại cho YCVT [mã]." | [Huỷ Lệnh] [Quay lại] |

#### Info / neutral messages

| Tình huống | Câu |
|---|---|
| Mất sóng | "Chờ đồng bộ. Ảnh sẽ gửi khi có mạng." |
| Kho CFS chưa sẵn sàng | "Kho chưa xác nhận hàng sẵn sàng. Xe có thể phải chờ." |
| Nhãn dữ liệu hành trình trên Lệnh | "Đề xuất bù dầu do kẹt xe: [x] lít" · "Đề nghị cấp bù dầu do chọn container rỗng ở nhiều bãi: [x] lít" · "ETA ước tính" · "Chờ VETC" · "Không có dữ liệu GPS" · "Không đủ dữ liệu" · "Kết thúc theo lái xe" |

### 7.4 Bối cảnh hệ thống (mức nghiệp vụ)

**Thông tin cần lưu**
- Trên Lệnh: xe, mooc, lái xe, cung đường (kế hoạch và thực tế); ảnh định vị theo điểm; nhật ký nhiệt; chi hộ, chi phí sửa vỏ container, phí lưu ca xe, cấp dầu; biên bản giao hàng (điện tử hoặc ảnh bản giấy); giờ đến thật, vé trạm, thời gian kẹt xe (từ GPS); thay đổi giữa chặng; lý do từ chối, trả lại; hạn chuẩn bị giấy tờ.
- Lịch sử: ai lập, giao, duyệt Lệnh; ai đổi trạng thái.
- Danh mục: điểm chụp ảnh theo loại hàng; chu kỳ nhắc nhiệt theo loại hàng; loại phí kèm cách hạch toán theo địa điểm; đơn giá đường sắt.

**Dịch vụ bên ngoài**

| Dịch vụ | Mục đích | Tình trạng |
|---|---|---|
| GPS và cảm biến dầu EUP | Giờ đến, khởi hành, kẹt xe, vé trạm cho Lệnh | Có tài liệu khách (VIS 08/10); nối qua `vehicle-telematics` |
| Dịch vụ bản đồ | Cung đường, quãng đường, giờ đến dự kiến | Chờ khách chọn nhà cung cấp (`vehicle-telematics` OQ-1) |
| VETC | Nguồn chuẩn toạ độ, chi phí đường bộ (F8); giao dịch trừ tiền theo xe để khớp vé (I7) | Có tài liệu khách; nối qua `vehicle-telematics` |
| Email | Gửi văn bản cảnh báo, kế hoạch xe cho trưởng ga, biên bản giao hàng cho CS và khách | Trong phạm vi |

**Thông báo**

| Ai nhận | Khi nào | Kênh |
|---|---|---|
| Điều vận | Quá mốc, lái xe từ chối Lệnh, quá giờ chưa nhập nhiệt, D/O đổi kho khi xe đang chạy, lái xe báo thay đổi giữa chặng | Thông báo đẩy |
| Trưởng điều vận | Cảnh báo quá hạn chưa xử lý | Thông báo đẩy |
| CS | Air chưa đủ kiện | Thông báo đẩy |
| CS và khách | Lái xe xác nhận biên bản giao hàng khách đã ký | Email kèm biên bản |
| Lái xe | Lệnh mới, tới giờ nhập nhiệt, Lệnh bị trả lại | Thông báo đẩy |
| Người duyệt Lệnh | Lệnh hết chạy có đề xuất bù dầu, trạm tránh, ngoài cung đường | Thông báo đẩy |
| Khách | Các mốc giao nhận khác | Chờ OQ-38 |

**Việc phần mềm tự chạy theo giờ:** đếm mốc và bắn cảnh báo quá mốc, leo thang · nhắc nhiệt độ theo chu kỳ · đồng hồ lưu xe theo `P-gio-mien-phi-luu-xe` (Delta: 72 giờ, chờ OQ-33) · sinh Bảng kê đường sắt nháp tới kỳ `P-ky-chot-duong-sat` (Delta: ngày 25 và cuối tháng).

**Cần gần như tức thời:** giờ đến theo GPS, cảnh báo quá mốc, giao Lệnh mới, vé khớp khi đơn vị thu phí gửi về. Còn lại (Bảng kê đường sắt, thống kê) chậm vài phút được.

## 8. Assumptions

- SOP của Delta là thiết kế to-be của khách, không phải cách đang làm.
- Delta chưa gửi Quy trình điều vận (OQ-1); trạng thái Lệnh và thứ tự bước CBT, đường sắt là đề xuất dựa trên SOP Giao nhận hàng hoá.
- Gợi ý ghép hàng (D5) và hàng chiều về (D8) cần có sẵn dữ liệu tải xe, khoảng cách giữa các kho và yêu cầu vận tải nội địa trên phần mềm.
- EUP gửi dữ liệu theo xe gần như tức thời; VETC cho tra giao dịch trừ tiền theo xe (VIS 08/10/2026).
- Định mức nổ máy không chạy (l/giờ) sẽ có trong định mức nhiên liệu của từng xe (`fuel-allowance`).

## 9. Risks

| Rủi ro | Khả năng | Hậu quả nghiệp vụ | Cách phòng |
|--------|----------|-------------------|-----------|
| Lái xe vẫn gửi ảnh và chi phí qua Zalo, không dùng app | thường | Mất bằng chứng; chi phí không lên JobID; vấn đề cũ quay lại | Thiếu ảnh thì chặn bước; app chạy khi mất sóng; thao tác chính làm được bằng một tay |
| Thiếu dữ liệu nền: tải xe, khoảng cách kho, giá đường sắt, định mức | thường | Gợi ý ghép hàng (D5), hàng chiều về (D8) sai | Chốt danh mục trước khi chạy thật; người có quyền cập nhật |
| Thiếu tài liệu khách: quy trình điều vận | thường | Luồng CBT, đường sắt và trạng thái Lệnh sai | Bám OQ-1 |
| GPS EUP gián đoạn | thỉnh thoảng | Mốc và giờ đến sai, cảnh báo sai | Lái xe bấm tay kèm ảnh định vị |
| VETC không gửi giao dịch tức thời hoặc không cho tra theo xe | thỉnh thoảng | Tránh trạm phát hiện muộn, đối soát dồn cuối kỳ | Chạy được cả hai cách (I7); bám OQ-49 |
| Lái xe phản đối khi bị tính tiền tránh trạm | thường | Tranh chấp, mất lái xe | Người duyệt chấp nhận được kèm lý do; lái xe được báo và xem số liệu của mình (I14); khách xác nhận quy chế trước khi tính vào lương (OQ-50) |
| Vùng trạm vẽ sai, thiếu | thỉnh thoảng | Báo tránh trạm sai, lái xe bị tính oan | Giao dịch thu phí là nguồn chuẩn khi có; danh mục dùng chung do đội sản phẩm duy trì |

## 10. Success Criteria (preliminary)

Mỗi tiêu chí gắn một vấn đề ban đầu. Số hiện trạng và mục tiêu chờ khách (OQ-44, ở `service-delivery`).

| Vấn đề | Tiêu chí | Mục tiêu |
|---|---|---|
| c. Bị phạt vì quá mốc | Số lần, số tiền phạt lưu container, lưu vỏ, lưu xe mỗi tháng so với trước | giảm ?% |
| d. Chứng từ về chậm | Thời gian từ khi xe xong việc tới khi Lệnh được duyệt | ≤ ? ngày |
| e. Chi phí thiếu | Tỉ lệ Lệnh được duyệt mà đủ chi phí | ? |
| Đối soát vé bằng tay | % giao dịch thu phí tự khớp vào Lệnh không cần người | ? |
| Bù dầu theo lời kể | % lít bù dầu có bằng chứng GPS; độ lệch giữa số đề xuất và số được duyệt | ? |
| Tránh trạm không ai biết | Số trạm tránh trên 100 Lệnh, theo tháng | ? |

## 11. Open Questions

Nguồn khách: tên tài liệu khách gửi và mục. Cột Trả lời theo biên bản [[docs/meetings/2026-10-10-oq-dispatch-coordination.md|Delta trả lời vòng 1]] (anh Nghĩa, 10/10/2026) và 2 điểm xác nhận lại ngày 12/10/2026; OQ-47–57 theo [[docs/meetings/2026-10-21-oq-vis.md|Delta trả lời deck VIS]] (anh Nghĩa, 21/10/2026).

| Mã | Câu hỏi | Nguồn khách | Trả lời |
|---|---|---|---|
| OQ-1 | Chưa có tài liệu Quy trình điều vận (QTĐV); luồng CBT, đường sắt và bước lập Lệnh đang dựa vào đâu? | Quy trình điều phối, các mục "Lệnh vận tải" (dẫn chiếu QTĐV) | Còn mở: Delta đang hoàn thiện, gửi dần |
| OQ-8 | 4 quy trình chờ Trasas; Trasas là ai? | Giao nhận hàng hoá (18/9/2026) | Đóng: ý kiến Trasas không làm thay đổi SOP |
| OQ-10 | Thuế với khoản chi hộ Ratraco không có hoá đơn đầu vào | Giao nhận hàng hoá (18/9/2026) | Còn mở: làm rõ khi viết SOP điều vận |
| OQ-12 | CBT và đường sắt thuộc QTĐV chưa có | Giao nhận hàng hoá (18/9/2026) | Đã chốt: CBT, đường sắt không đi qua Điều phối; mỗi loại JobID có giao diện, Yêu cầu vận tải, Lệnh riêng. Chi tiết chờ Quy trình điều vận |
| OQ-13 | Ai nhập đơn giá đường sắt khi thiếu phụ lục hợp đồng? | Giao nhận hàng hoá (18/9/2026) | Đã chốt (cùng OQ-30): giai đoạn 1 CS nhập đơn giá tay |
| OQ-18 | Quản lý vỏ container swap (vỏ Delta/khách, sửa chữa vỏ) có thuộc Điều phối không? | Chưa có trong tài liệu khách gửi | Đã chốt: ngoài giai đoạn 1; chi phí sửa vỏ ghi trên Lệnh (phần Điều vận) |
| OQ-20 | Người ký biên bản giao hàng phía khách là ai? Có khách bắt buộc đóng dấu không? | Chưa có trong tài liệu khách gửi | Một phần: làm cả ký điện tử lẫn biên bản giấy (xác nhận 12/10); tự email biên bản cho CS và khách khi lái xe xác nhận (A7). Còn thiếu: ai ký phía khách, khách nào bắt đóng dấu |
| OQ-28 | Ai bấm xác nhận "đã nhận tiền hoàn" tiền nâng vỏ? Quá 7 ngày chưa về thì báo ai? | Giao nhận hàng hoá (18/9/2026) | Đã chốt: ngoài phần mềm: khoản nằm trong dư nợ tạm ứng; bỏ theo dõi khoản chờ hoàn (B5) |
| OQ-30 | Đường sắt: giá xác định lần đầu lưu vào bảng giá cho các chuyến sau, hay chỉ dùng cho chuyến đó? Khi nào áp cách nào, ai quyết? | Giao nhận hàng hoá (18/9/2026) | Đã chốt: giai đoạn 1 CS làm đơn giá tay; giai đoạn 2 báo giá trên phân hệ Sales (E3) |
| OQ-32 | Bước 5 chi hộ Ratraco (thủ quỹ chuyển tiền trả lái xe) giữ thủ công hay chuyển khoản tự động? | Giao nhận hàng hoá (18/9/2026) | Còn mở: giải quyết trong Quy trình điều vận |
| OQ-33 | Phí lưu xe quá 72 giờ và phí máy phát CBT: có muốn phần mềm tự đề xuất doanh thu không; đơn giá, đơn vị tính; giờ bắt đầu lấy từ GPS hay ảnh định vị? | Giao nhận hàng hoá (18/9/2026) | Một phần: phí lưu ca xe ghi lên Lệnh; phí máy phát Delta sẽ có giải pháp. Còn thiếu: phần mềm có tự tính phí lưu ca không (E8) |
| OQ-34 | Quá mốc vì kẹt xe, sự cố đường: có thêm nhóm nguyên nhân thứ 4 "khách quan" không? | Chưa có trong tài liệu khách gửi | Đã chốt: ngoài phần mềm; không thêm nhóm nguyên nhân (B6) |
| OQ-35 | Kế hoạch ngày Ratraco gửi ngày n-1 có mẫu cố định không? Xin một mẫu thật | Giao nhận hàng hoá (18/9/2026) | Chưa hỏi Delta (ngoài deck vòng 1) |
| OQ-37 | Lái xe chỉnh nhiệt theo yêu cầu khách có bắt buộc chụp ảnh làm bằng chứng không? | Giao nhận hàng hoá (18/9/2026) | Chưa hỏi Delta (ngoài deck vòng 1) |
| OQ-38 | Khách có cần nhận thông báo ở mốc nào không: xe đã đến, đã nhận hàng, đã giao xong, quá mốc? | Chưa có trong tài liệu khách gửi | Chưa hỏi Delta (ngoài deck vòng 1) |
| OQ-43 | Chu kỳ nhắc nhập nhật ký nhiệt độ mặc định cho từng loại hàng lạnh là bao nhiêu? (SOP chỉ có sầu riêng 3–4 giờ/lần, hàng lạnh khác 3–4 lần/ngày) | Giao nhận hàng hoá (18/9/2026) | Chưa hỏi Delta (ngoài deck vòng 1) |
| OQ-45 | "Hàng quay cắt" trong thực tế là tình huống nào? Khi đó xe và hàng được xử lý ra sao? | Chưa có trong tài liệu khách gửi (trao đổi trực tiếp 09/10/2026) | Đã chốt: trả lời qua tài liệu Camera AI (11/8/2026) mục 1, 3: quay cắt là kéo container vào, ra cửa kho tại nhà máy cho mô hình cắt mooc; lái xe quay cắt hưởng lương, dầu theo lượt; làm cho đơn vị khác thì có doanh thu. Camera AI đã loại 14/10, ghi nhận bằng GPS (chốt 20/10). Xem Q1–Q7 |
| OQ-46 | Có cần làm luồng tạm ứng dầu cho xe CBT không? (Đợt trước khách nói bỏ phần xử lý bên ngoài) | Chưa có trong tài liệu khách gửi (trao đổi trực tiếp 09/10/2026) | Đã chốt (BA 21/10, theo Delta): có — cần luồng tạm ứng dầu cho xe CBT |
| OQ-47 | Dữ liệu xe (VIS) và hóa đơn, thanh toán (SIM) nối nhau ở đâu? (1) Hóa đơn tổng VETC cuối kỳ, sau khi đối chiếu với GPS, có đi qua IIP/MISA như hóa đơn đầu vào thường không, ai duyệt, gắn JobID nào? (2) Hóa đơn dầu mua ngoài mà lái xe tải lên IIP có ghép với đối soát sensor dầu không? (3) Chi phí đã duyệt trên Lệnh (vé, dầu bù, km tìm vỏ J01) có chuyển sang SIM để ghép hóa đơn theo JobID không? | VIS (08/10/2026) mục 3.1.3 Bước 4, 3.6; SIM & VIS Công tác chuẩn bị (11/10/2026) mục 2.2–2.3 | Một phần (Delta 21/10): (1) Hoá đơn tổng VETC đi qua phần thu thập hoá đơn đầu vào; hoá đơn cấp cho 2 tài khoản mẹ Delta VT, Delta HCM; phần mềm chạy đối soát định kỳ tìm vé chưa gắn Lệnh, lập danh mục vé mồ côi để xử lý. (2) Có: hoá đơn dầu mua ngoài đối chiếu với số lít cảm biến (dữ liệu xét "Nhà vô địch đổ dầu xuống cống" hằng tháng). Còn thiếu: (3) chi phí đã duyệt trên Lệnh có sang SIM ghép hoá đơn theo JobID không (chưa hỏi); brainstorm SIM nhận lại (BL-120) |
| OQ-48 | Thiết bị EUP gửi vị trí bao nhiêu giây một lần khi xe chạy? Hai điểm GPS cách nhau tối đa bao lâu (hoặc bao xa) thì còn tin được để kết luận xe tránh trạm? | VIS (08/10/2026) mục 2.2.6 | Đã chốt (Delta 21/10): có GPS dự phòng và VETC gửi giao dịch ngay thì gần như không xảy ra; nếu xảy ra thì gắn cờ Lệnh để người duyệt xem kỹ, không kết luận tránh trạm. Delta không cho số giây, khoảng cách |
| OQ-49 | Phần mềm gọi VETC đối soát lúc xe vào vùng điểm cuối hay lúc kết thúc Lệnh (2 mục ghi khác nhau)? VETC có gửi giao dịch ngay khi trừ tiền không? Nếu có: khớp vé từng trạm lúc xe đang chạy, điều vận thấy vé trên Lệnh ngay. Nếu không: chỉ khớp một lần khi Lệnh hết chạy, tránh trạm biết muộn hơn. | VIS (08/10/2026), mục 2.2.6 Giám sát lộ trình và ghi nhận tránh trạm vé, mục 3.1.1 Sơ đồ kiến trúc và luồng dữ liệu, mục 3.1.3 Bước 2 | Đã chốt (Delta 21/10): A — VETC trừ tiền ngay trên tài khoản mẹ của Delta (Cục Đường bộ không cho nợ vé) nên có dữ liệu đối soát ngay; khớp vé từng trạm khi xe đang chạy. Dữ liệu đôi khi trễ: phần mềm quét lại liên tục tới khi có vé để gán vào Lệnh |
| OQ-50 | Vé tránh trạm chốt theo từng Lệnh, người duyệt chọn "Tính cho lái xe" hoặc "Chấp nhận" kèm lý do: đúng ý khách không? Sơ đồ ghi "vé tránh trạm, trả vào lương lái xe": trừ lương hay cộng lương, tự động hay sau khi duyệt? Quy chế nội bộ đã cho phép tính khoản này vào lương chưa? | VIS (08/10/2026), mục 3.1.1 Sơ đồ kiến trúc và luồng dữ liệu | Đã chốt (Delta 21/10): (1) VIS ghi trạm tránh lên Lệnh theo thời gian thực; lái xe, điều vận, cán bộ quản lý chốt Lệnh; Lệnh đủ chi phí mới được chốt — quy tắc cứng, chốt chặn an toàn (fail-safe) chống dữ liệu rác. (2) Tiền vé trạm tránh trừ vào lương lái xe; là căn cứ duyệt Lệnh ở cả hai cấp. Còn thiếu: quy chế nội bộ đã cho tính khoản này vào lương chưa (vehicle-telematics OQ-10) |
| OQ-51 | VETC vẫn chưa trả dữ liệu sau lượt tra lại 120 phút: cho duyệt Lệnh, trạm ghi "Chờ VETC" và đối soát nốt cuối kỳ được không? | VIS (08/10/2026), mục 3.1.3 Bước 3 | Đã chốt (Delta 21/10): B, ngược đề xuất — Lệnh chưa đủ dữ liệu VETC thì chưa cho duyệt; quy tắc cứng, chốt chặn an toàn. Delta cho rằng thực tế không xảy ra; nếu có, Delta khiếu nại VETC |
| OQ-52 | Xe xếp hàng chờ ở cổng cảng, bãi, kho quá 10 phút mà máy vẫn nổ: có bù dầu như kẹt xe không? | VIS (08/10/2026), mục 3.2 Bước 1 | Đã chốt (Delta 21/10): A — bù dầu khi kẹt xe ở bất kỳ đâu, kể cả xếp hàng ở cổng cảng, bãi, kho; phân biệt kẹt xe với nổ máy ngủ. Trước khi đề xuất bù dầu trên Lệnh, phần mềm gọi Google Maps ghi tình trạng giao thông làm ngữ cảnh cho người duyệt (chống gian lận) |
| OQ-53 | Tai nạn, kẹt cứng không nhích được: xe đứng yên hẳn được tính là kẹt xe (có bù) khi đứng giữa hai đoạn kẹt, khi lái xe báo vấn đề giữa chặng, hoặc khi bản đồ báo tắc tại đó. Khách đồng ý không? | VIS (08/10/2026), mục 2.2.3, mục 2.2.4 | Đã chốt (Delta 21/10): không tính kẹt xe, không bù dầu — VIS đã loại tình huống xe kẹt cứng, đứng yên hẳn (xe không vận hành) |
| OQ-54 | Mất tín hiệu GPS: đề xuất lái xe chụp ảnh định vị tại từng mốc để ghi giờ đến. Khách đồng ý không? | Chưa có trong tài liệu khách gửi | Còn mở — khách cần trao đổi thêm (Delta 21/10): Delta không lấy dữ liệu từ lái xe để quản lý vận hành xe; VIS 18/10 đã có nguồn dữ liệu dự phòng khi mất GPS. Cần đối chiếu nguồn dự phòng trong VIS 18/10, bỏ đề xuất chụp ảnh định vị |
| OQ-55 | Có trường hợp đổi xe giữa chặng không? | Chưa có trong tài liệu khách gửi | Còn mở — khách cần trao đổi thêm (Delta 21/10): Delta hướng tạo Lệnh phụ cho xe kéo tiếp. Cần làm rõ Lệnh phụ: chi phí, lương, vé chia giữa Lệnh gốc và Lệnh phụ |
| OQ-56 | Có trường hợp 2 container 20 feet của 2 Lệnh trên cùng một xe không? Nếu có: kẹt xe, vé trong khoảng chạy chung chia đều cho 2 Lệnh được không? | Chưa có trong tài liệu khách gửi | Đã chốt (Delta 21/10): có trường hợp một xe chở 2 container 20 feet, nhưng không được tách thành 2 Lệnh trên cùng chuyến; Delta sẽ định nghĩa Lệnh vận tải để loại bỏ cách ghép này. ⚠ Phiếu chọn B "chia đều" nhưng ý kiến thêm ngược lại; ghi theo ý kiến thêm, xác nhận lại khi Delta gửi định nghĩa Lệnh |
| OQ-57 | Xác nhận các ngưỡng đã ghi (kẹt xe dưới 5 km/h quá 10 phút; tra lại VETC sau 120 phút; tính lại ETA mỗi 30 phút với cung trên 300 km; ở bãi khác quá 10 phút khi tìm vỏ) và cho số các ngưỡng còn trống (lệch cung đường "x%", đứng yên tối đa giữa 2 đoạn kẹt). | VIS (08/10/2026), mục 2.2.1, 2.2.3, 3.1.3, 3.3 | Đã chốt (Delta 21/10): 4 số đã có không đổi. Lệch cung đường không dùng %, quy ra thời gian đến muộn dự kiến: dưới 30 phút bình thường, từ 30 phút thông báo, từ 90 phút xử lý theo quy trình đặc biệt. Thời gian kẹt xe cộng dồn theo từng Lệnh, trạng thái kẹt theo định nghĩa VIS (không cần ngưỡng đứng yên giữa hai đoạn kẹt) |
| OQ-58 | Lái xe trả tiền mặt tại trạm thu phí (tài khoản giao thông hết tiền, trạm không thu tự động): đề xuất lái xe ghi khoản chi hộ kèm trạm và ảnh biên lai, trạm đó tính "Đã qua", không chờ giao dịch VETC. Delta có trường hợp này không, đồng ý cách làm không? | Chưa có trong tài liệu khách gửi | Chưa hỏi Delta (review VIS r11, 19/10) |
| OQ-59 | Lệnh hết chạy bao lâu chưa duyệt thì nhắc người duyệt và báo trưởng điều vận (`P-han-duyet-lenh`)? | Chưa có trong tài liệu khách gửi | Chưa hỏi Delta (review VIS r9, 19/10) |
| OQ-60 | Luồng khiếu nại của lái xe (I14): lái xe khiếu nại trong hạn, khoản rút khỏi bảng kê lương, người ra quyết định gốc xem lại (Giữ · Huỷ · Sửa số), bị Giữ thì leo thang 1 lần lên trưởng bộ phận: khách đồng ý không? Hạn khiếu nại bao nhiêu ngày (`P-han-khieu-nai`)? Quy chế có cho khiếu nại khoản đã chốt kỳ không? | Chưa có trong tài liệu khách gửi | Chưa hỏi Delta (review VIS v4, 20/10) |
| OQ-61 | Một lượt quay cắt tính thế nào: mỗi lần kéo vào hoặc ra cửa kho là một lượt, hay vào và ra là một lượt? Chỉnh vị trí liên tiếp trong bao nhiêu phút thì gộp (`P-gop-luot-quay-cat`), mooc đi dưới bao nhiêu mét thì không tính (`P-quang-toi-thieu-quay-cat`)? | Camera AI (11/8/2026), mục 1 | Chưa hỏi Delta |
| OQ-62 | Đơn giá lương và định mức dầu cho mỗi lượt quay cắt (`P-don-gia-luong-quay-cat`, `P-dinh-muc-dau-quay-cat`): một số chung hay khác theo nhà máy, theo container 20 hay 40 feet? Đơn giá thu của đơn vị thuê quay cắt theo hợp đồng nào, ai lập bảng kê, kỳ nào? | Camera AI (11/8/2026), mục 1, 3 | Chưa hỏi Delta |
| OQ-63 | Đầu kéo quay cắt cố định tại một nhà máy hay xoay giữa các nhà máy, lái xe xoay ca thế nào? Ai phân công? Nhà máy nào đang có quay cắt? | Camera AI (11/8/2026), mục 1 | Chưa hỏi Delta |
| OQ-64 | Mooc của Delta để lại nhà máy đã gắn thiết bị GPS mooc chưa (đề xuất 25/9/2025)? Nếu chưa, mọi lượt quay cắt đi đường lái xe bấm trên App (Q4) tới khi lắp. | Đề xuất tiện ích GPS (25/9/2025), mục 2 | Chưa hỏi Delta |
| OQ-65 | Chi ở cửa khẩu Trung Quốc lái xe trả bằng nhân dân tệ hay đồng? Nếu ngoại tệ thì quy đổi theo tỷ giá nào, ngày nào? Phí bãi xe Viettel nằm ở cả nhóm Delta trả nhà cung cấp và nhóm ghi trên Lệnh: khi nào lái xe trả, khi nào kế toán trả? | Thống kê chi phí chứng từ CBT (03/9/2026) | Chưa hỏi Delta |
| OQ-66 | Mooc 40ft 2 giàn có khoá giữa để chở 1 container 20ft không? (quy tắc ghép F10) | Chưa có trong tài liệu khách gửi (lab-combo 11/10/2026 mục 10) | Chưa hỏi Delta |
| OQ-67 | Mooc 45ft có khoá cho container 20ft, 40ft không, chở được 2×20 không? | Chưa có trong tài liệu khách gửi (lab-combo mục 10) | Chưa hỏi Delta |
| OQ-68 | Tải trọng từng mooc là bao nhiêu, để cảnh báo 2×20 có hàng vượt tải? Danh mục mooc hiện chưa có trường tải. | Chưa có trong tài liệu khách gửi (lab-combo mục 10) | Chưa hỏi Delta |
| OQ-69 | Container lạnh chạy điện bằng máy phát gắn rời (mã PT 35–37, `vehicle-management` H8) hay máy phát tích hợp khi đi đường sắt? Máy phát có là một thành phần của tổ hợp không? | Chưa có trong tài liệu khách gửi (lab-combo mục 10) | Chưa hỏi Delta |
| OQ-70 | Hai container 20ft trên một mooc có được thuộc 2 Lệnh khác nhau (ghép hàng) không, hay một tổ hợp luôn thuộc một Lệnh? | Chưa có trong tài liệu khách gửi (lab-combo mục 10) | Chưa hỏi Delta |
| OQ-71 | Container của Delta (mã PT 33–34) có theo dõi trên tổ hợp như phương tiện, hay chỉ ghi số như vỏ hãng tàu (liên quan OQ-18)? | Chưa có trong tài liệu khách gửi (lab-combo mục 10) | Chưa hỏi Delta |
| OQ-72 | Đầu kéo chạy một mình (đi lấy mooc, về bãi sau khi bỏ mooc) có lập Lệnh không? | Chưa có trong tài liệu khách gửi (lab-combo mục 10) | Chưa hỏi Delta |


## 12. Next Steps

Đã tách từ brainstorm Điều phối gộp ngày 2026-10-12. Tiếp theo:
- Chờ Delta gửi Quy trình điều vận (OQ-1), rồi rà lại Mục 5–6
- Hỏi lại Delta các câu còn mở ở Mục 11 (BL-041)
- `/user-flow transport-dispatch` — chạy lại; userflow tách máy từ bản nháp ngày 07/10, còn nội dung cũ (hạ vỏ "x/n", tiền hoàn nâng vỏ, duyệt chi ngoài định mức, CBT và đường sắt)
- `/srs transport-dispatch` — đặc tả FR, BR, Error Matrix
- Hỏi Delta OQ-49–60 cùng lượt với câu hỏi mở của `vehicle-telematics`, `vehicle-management`
