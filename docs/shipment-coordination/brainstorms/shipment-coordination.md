---
type: brainstorm
feature: shipment-coordination
status: draft
updated: 2026-10-21
links:
  - docs-input/sop/sop-dieu-phoi.md
  - docs-input/sop/sop-cung-cap-dich-vu-tong-quat.md
  - docs-input/sop/giao-nhan-hang-hoa/giao-nhan-hang-hoa.md
  - docs-input/sop/apas-thanh-toan-doi-soat/apas-thanh-toan-doi-soat.md
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
  - docs/fund-payments/brainstorms/fund-payments.md
  - docs/location-catalog/brainstorms/location-catalog.md
---

# Điều phối — từ JobID tới Yêu cầu vận tải, theo 6 luồng hàng

> Phỏng vấn xong đủ 7 phần ngày 2026-10-07: tổng quan, người dùng, luồng chính, trạng thái và tình huống, kiểm tra dữ liệu và câu thông báo, bối cảnh hệ thống, rủi ro và tiêu chí thành công.
> Cập nhật 2026-10-12 theo trả lời của Delta cho bộ câu hỏi vòng 1 (biên bản 2026-10-10).
> Tách ngày 2026-10-12 theo SOP: Quy trình cung cấp dịch vụ tổng quát ([[docs/service-delivery/brainstorms/service-delivery.md|service-delivery]]) · Quy trình điều phối (feature này) · Quy trình điều vận ([[docs/transport-dispatch/brainstorms/transport-dispatch.md|transport-dispatch]]). Mã ý tưởng (A1, B7…), DP-nn và OQ-n giữ nguyên số của bản gộp.
> Cập nhật 2026-10-21 theo nguồn mới: phạm vi dịch vụ, số container thực nhận, việc phát sinh (service-delivery 20/10); thu hoá đơn GTGT, danh mục lô hàng (Phân hệ APAS 17/10/2026); chọn thiếu vỏ FCL xuất (Quy trình điều phối mục 4.6); định mức và Quyết định phân công (Quy trình cung cấp dịch vụ tổng quát mục 4.6).

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
| e | Khách gọi thêm việc giữa chừng nhưng không ghi lên JobID, đến bảng kê cuối tháng mới xử lý |
| f | Số container thực làm khác chứng từ (chọn thiếu vỏ, khách chia Booking Note) nên doanh thu, YCVT lệch |
| g | Lô đã có chứng từ nhưng chưa ai mở JobID, bị sót tới sát cut-off |

**Phạm vi:**
- Gồm: Điều phối 6 luồng (FCL, LCL/CFS, air × xuất, nhập): danh mục lô hàng (lô đã có chứng từ, chưa thành JobID), nhận JobID, kê khai và phân luồng theo phạm vi dịch vụ, việc ePort, giao việc hiện trường (kể cả trực ngoài giờ, việc phát sinh, thu hoá đơn GTGT), lấy định mức khi giao việc, việc hiện trường trên mobile (chụp chứng từ, AI đọc), chọn vỏ và chốt số container thực nhận, sinh YCVT.
- Ranh giới với 2 feature cùng chuỗi:
  - Cung cấp dịch vụ tổng quát (`service-delivery`): tạo và duyệt JobID, hoàn thành dịch vụ, quy tắc thanh toán chi phí, giao dịch nội bộ (B7). Feature này nhận JobID ở trạng thái "Chờ xử lý".
  - Điều vận (`transport-dispatch`): nhận YCVT, lập và chạy Lệnh, cảnh báo quá mốc. Mốc do feature này ghi khi kê khai.
  - Quỹ và thanh toán (`fund-payments`): cách trả, dư nợ tạm ứng, sinh Quyết định phân công công việc hằng tháng. Feature này tạo việc và là căn cứ phân công.
  - Danh mục địa điểm (`location-catalog`): cảng, bãi, kho, hãng tàu, thuộc tính phân luồng (B1) và định mức theo địa điểm. Feature này chỉ đọc.
- CBT và đường sắt không có giao nhận tại cảng (CBT thuê ngoài toàn bộ) nên không đi qua Điều phối (Delta, 10/10/2026); đi thẳng từ JobID sang Điều vận.
- Không gồm: quản lý danh mục cảng/bãi (`location-catalog`); phần đọc chứng từ (DIS, khối dùng chung, chỉ đẩy dữ liệu vào danh mục lô hàng); tạo, duyệt JobID, ghi doanh thu (`service-delivery`); sinh Quyết định phân công, dư nợ tạm ứng, khớp tiền (`fund-payments`); phạm vi xem dữ liệu chi nhánh khác (feature Phân quyền).
- Ngoài giai đoạn 1: quản lý vỏ container.
- Ứng dụng: Delta Super App; web cho CS, cán bộ quản lý; mobile cho nhân viên hiện trường và lái xe khi được giao việc hiện trường.

**Nguồn:** Quy trình điều phối (mục 4, 5.1–5.6), Giao nhận hàng hoá 18/9/2026, Quy trình cung cấp dịch vụ tổng quát 24/9/2026 (mục 4.6, 5.1), Phân hệ APAS 17/10/2026 (mục 2.2, 3.1.2), 3 báo cáo điều tra trong `docs/_research/` (mốc container, ePort, đọc chứng từ hiện trường).

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
| Kế toán | Phát sinh và giảm container tới cuối tháng mới biết | Thấy việc phát sinh, số container thực nhận ngay trên JobID |
| Trợ lý AI | — | Đọc chứng từ, gợi ý người nhận việc |

Mọi vai trò có màn "Việc của tôi" kèm thông báo đẩy mở thẳng vào việc. Mặc định chỉ thấy JobID của chi nhánh mình.

### 3.1 Tác vụ chính

Tần suất chưa đo được, ghi định tính. Dòng có ★ là tác vụ phải tối ưu cho thao tác nhanh nhất.

| Vai trò | Tác vụ | Tần suất | Mức quan trọng | Ghi chú |
|---------|--------|----------|----------------|---------|
| CS | ★ Kê khai JobID, quét QR tờ khai, đưa D/O, eDO, booking; việc ePort; chuyển việc cho hiện trường | Nhiều lần mỗi ngày | cao | Xe đi nhầm kho hoặc đi khi hàng chưa sẵn sàng |
| CS | Xem danh mục lô hàng; thêm việc phát sinh; chọn "Chọn tiếp" hoặc "Chốt số" khi chọn thiếu vỏ | Hằng ngày | cao | Lô bị sót không thành JobID; doanh thu tính sai số container |
| Nhân viên hiện trường | ★ Chụp: phiếu cân ra VGM, EIR, mã vạch gốc; nhận việc được gợi ý; thu hoá đơn GTGT | Vài lần mỗi ngày | cao | Trễ VGM nên lỡ tàu; mất chứng từ gốc |
| Cán bộ quản lý | ★ Việc của tôi: giao việc hiện trường, giao người trực ngoài giờ | Vài lần mỗi ngày | trung | Việc hiện trường không có người nhận |
| Cán bộ quản lý | Duyệt việc phát sinh, duyệt chốt số container | Vài lần mỗi tuần | trung | Phát sinh không hạch toán kịp; giảm container không ai biết |
| Kế toán | Xem việc phát sinh, số container thực nhận trên JobID khi lập bảng kê | Hằng tháng | trung | Bảng kê sai số container, sót phát sinh |

## 4. Capabilities Breakdown

### P0 — must have

P0 là phần chuỗi JobID → YCVT cần để chạy ở giai đoạn 1.

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
- B1 [SOP+] [Lõi] Danh mục cảng/bãi có 3 thuộc tính: có ePort, có xe mới chọn được vỏ, thanh lý tờ khai online hay tại bãi; phần mềm phân luồng theo 3 thuộc tính này. Danh mục và người cập nhật thuộc `location-catalog`.
- B2 [SOP to-be] [Lõi] [Cấu hình] Nút "Chuyển việc" thay "Từ chối", bắt buộc chọn lý do trong `P-ly-do-chuyen-viec` (Delta: "Hết giờ làm việc" · "Khác" tự ghi); quyền thanh toán tự chuyển sang hiện trường.
- B3a [SOP+] [Lõi] [Cấu hình] Gợi ý `P-so-nguoi-goi-y-nhan-viec` (Delta: 2–3) người nhận việc (gần cảng/bãi, số việc đang ôm, trong ca trực); quản lý vẫn bấm chọn. Dùng chung quy tắc "người gần lái xe nhất".
- B3b [SOP to-be] [Lõi] [Cấu hình] Cán bộ quản lý hiện trường giao người trực ngoài giờ theo `P-ca-truc-ngoai-gio` (Delta: 17h30–8h); người trực có quyền tự giao việc trong ca, hết ca thu quyền. [Mới] Đầu ca và cuối ca có bước bàn giao việc đang dở giữa người trực và người làm giờ hành chính, theo `P-ban-giao-ca-truc` (Delta: bật).
- B4 [SOP+] [Cấu hình] Lệnh hạ vỏ rỗng (chỉ hàng nhập FCL): JobID có 1 container thì gộp giao việc theo vận đơn + nơi hạ theo `P-gop-giao-viec-ha-vo` (Delta: bật); JobID nhiều container thì giao từng container, vì khách nhận hàng khác ngày.
- Giao việc cho người chi nhánh khác tuyến thì phần mềm tự ghi giao dịch nội bộ — xem B7 ở `service-delivery`.
- B15 [SOP to-be] [Lõi] Phạm vi dịch vụ quyết định bước: mục giao nhận tại cảng đã chọn trên JobID (lấy lệnh giao hàng, nâng container hàng, nâng container rỗng, cược vỏ, chọn vỏ — `service-delivery` B9) quyết định Điều phối có bước nào. Có chọn thì hiện bước, có kê khai, giao việc, ghi định mức, cấp quyền thanh toán; không chọn thì bỏ bước và không đếm mốc của bước đó. "Kê khai đủ" ở DP-03 = đủ trường bắt buộc của các mục đã chọn. Thứ tự bước trong từng luồng giữ như Mục 5.2–5.7.
- B16 [SOP to-be] [Lõi] [Cấu hình] Chọn thiếu vỏ (FCL xuất): hiện trường hoặc lái xe chọn được ít vỏ đạt chuẩn hơn số container thực nhận thì phần mềm sinh YCVT ngay cho các container đã chụp và ghi số (mỗi container chỉ một YCVT), rồi báo CS. CS hỏi khách và chọn: "Chọn tiếp" (quay lại bãi chọn phần còn lại, chọn được container nào sinh thêm YCVT cho container đó) hoặc "Chốt số" (ngừng chọn vỏ, ghi số container thực nhận mới lên JobID). Chốt số cần cán bộ quản lý hiện trường duyệt theo `P-duyet-chot-so-container` (Delta: bật, chờ xác nhận OQ-71). Tới cut-off trên Booking Note mà chưa chọn đủ thì phần mềm nhắc CS chốt số. Khi "Chọn tiếp", phần mềm ghi mốc bắt đầu và kết thúc chờ chọn vỏ trên JobID và báo Điều vận để tính thời gian lưu xe (Quy trình điều phối mục 4.6). Duyệt chốt số xong, phần mềm huỷ Yêu cầu thanh toán chưa trả, thu quyền thanh toán và tính lại định mức cho phần container bị bỏ; phí đã trả theo B17. Số thực nhận được tăng lại sau khi chốt: như B21, cấp lại quyền thanh toán, định mức; phí nâng không dùng còn hạn lệnh nâng thì dùng lại. Khi chọn vỏ còn ở "Chọn tiếp" hoặc "Chờ duyệt chốt số", JobID không lên "Đã thực hiện Lệnh vận tải" (xác nhận với Delta: OQ-75). Cut-off là trường bắt buộc khi kê khai FCL xuất; AI không đọc ra thì CS nhập tay. Nhắc chốt số khi tới cut-off: trong giờ gửi CS, ngoài giờ gửi người trực (B3b). Chốt số chờ duyệt quá `P-han-duyet-dieu-phoi` (Delta: chưa chốt, OQ-77) thì nhắc lại cán bộ quản lý hiện trường, ngoài giờ gửi người trực. Nguồn: Quy trình điều phối mục 4.6, đoạn "Xác định số lượng container xuất FCL trên JobID".
- B17 [SOP to-be] [Lõi] Phí nâng không dùng: phí nâng đã trả cho vỏ không nâng được (sau "Chốt số", hoặc lệnh nâng hết hạn khi chưa chọn đủ) được đánh dấu "Phí nâng không dùng" trên JobID; không tính vào chi phí JobID, không thu khách. Tiền ở nguyên dư nợ tạm ứng 2 của người đã trả, việc đòi hoàn với bãi xử lý ngoài phần mềm; phần mềm không theo dõi khoản chờ hoàn (Delta, 10/10/2026, OQ-28). Khi "Chọn tiếp", phí dư giữ trạng thái "Đã trả, chưa dùng" để dùng tiếp trong hạn lệnh nâng.
- B18 [SOP+] [Lõi] Việc phát sinh: phạm vi gốc khoá khi JobID đã vào Điều phối (`service-delivery` Mục 6.3, OQ-66). Khách cần thêm việc thì CS thêm "Việc phát sinh" vào JobID (chọn từ cùng danh sách phạm vi, ghi lý do); cán bộ quản lý hiện trường duyệt. Duyệt xong việc vào luồng giao việc như thường và hạch toán lên JobID ngay, không chờ tới bảng kê cuối tháng: Điều phối ghi chi phí định mức, quyền thanh toán; khoản thu thêm ghi lên JobID ngay lúc duyệt theo quy tắc doanh thu của `service-delivery` E16. Việc phát sinh hiện riêng với báo giá gốc để kế toán thấy khi lập bảng kê. Thêm được tới trước khi JobID "Hoàn thành dịch vụ"; khách báo thêm việc sau mốc đó thì xử lý thế nào: OQ-76. Chờ duyệt quá `P-han-duyet-dieu-phoi` (Delta: chưa chốt, OQ-77) thì nhắc lại cán bộ quản lý hiện trường, ngoài giờ gửi người trực.
- B20 [SOP to-be] [Lõi] Định mức chi phí hiện trường và Quyết định phân công: giao việc thì phần mềm lấy định mức theo địa điểm làm việc (cảng, bãi, kho) × loại việc (chọn vỏ, thanh lý tờ khai, kiểm hoá…) từ `location-catalog`; người được giao không gõ số tiền. Địa điểm chưa có định mức thì cảnh báo, cán bộ quản lý hiện trường nhập tạm kèm lý do. Quyết định phân công công việc chỉ sinh khi JobID có công tác phí: mỗi người một Quyết định mỗi tháng, kèm bảng kê các JobID có công tác phí và số tiền, cùng nhịp với quyết định giao Lệnh hằng tháng của lái xe; phần mềm sinh ở `fund-payments`. Người ký: OQ-74. Nguồn: Quy trình cung cấp dịch vụ tổng quát (24/9/2026), mục 4.6.
- B21 [SOP to-be] [Lõi] Đếm theo số container thực nhận (`service-delivery` B10): số YCVT, số vỏ cần chọn, DP-14 (gộp hạ vỏ khi thực nhận 1 container) đều dùng số thực nhận, không dùng số trên Booking Note hoặc vận đơn. Số thực nhận đổi sau khi đã có YCVT (chọn thiếu vỏ rồi chốt số, khách đổi Booking Note): tăng thì sinh thêm YCVT cho phần tăng và báo điều vận; giảm thì như Mục 6.4 dòng 6.

**Nhóm D — từ SOP Giao nhận hàng hoá**
- D4 [SOP+] [Lõi] Nơi nhận trên Lệnh lấy thẳng từ D/O, không nhập tay; D/O đổi kho thì Lệnh cập nhật theo, xe đã giao thì báo điều vận.

### P1 — should have

Làm sau phần P0 trong giai đoạn 1 (cách phân mức như `service-delivery`, DEC-229).

- A12 [SOP to-be] [Lõi] Danh mục lô hàng: mỗi chứng từ vận tải (B/L, Booking Note) phần đọc chứng từ nhận được qua các kênh thành một dòng lô hàng, kèm khách, loại chứng từ, kênh nhận và JobID nháp tạo cùng lần đọc. CS thấy ngay lô nào đã có chứng từ mà chưa thành JobID, mở JobID nháp để kiểm và chuyển duyệt (`service-delivery` A11). Chứng từ không nhận ra khách thì dòng hiện "Chờ tra soát", không có JobID nháp (theo `service-delivery` A11). Trường hiển thị, lọc, ai được xem: OQ-73. Nguồn: Phân hệ APAS (17/10/2026), mục 2.2.1–2.2.4.
- B19 [SOP to-be] [Lõi] Thu hoá đơn GTGT theo "người gần lái xe nhất": khi lái xe tạo Yêu cầu thanh toán trên Lệnh, phần mềm giao việc "Thu hoá đơn GTGT" theo phân công việc của JobID chứa Lệnh đó, lần lượt: (1) nhân viên hiện trường đang giữ việc của JobID tại cùng cảng, bãi, kho nơi phát sinh khoản; (2) nhân viên hiện trường làm việc gần nhất của JobID; (3) CS của JobID. Việc vào "Việc của tôi" kèm Lệnh, khoản, số tiền; người nhận "Chuyển việc" được như B2, việc đi tới người kế tiếp trong thứ tự, hết người thì về cán bộ quản lý hiện trường. CS hoặc nhân viên hiện trường tự tạo Yêu cầu thanh toán từ JobID thì người tạo tự thu hoá đơn. Quy tắc chọn người đặt ở đây; `service-delivery` E6 trỏ sang. Hạn thu hoá đơn: OQ-72. Nguồn: Phân hệ APAS (17/10/2026), mục 3.1.2; `service-delivery` E6.

### P2 — nice to have

Chưa có.

## 5. Core Flows (Happy Path)

### 5.1 Luồng tổng (xương sống chung của 3 feature)

0. **Tạo và duyệt JobID** — `service-delivery`.
1. **Nhận JobID vào Điều phối** — phần mềm đưa vào danh sách của CS, bắt đầu đếm mốc của các mục phạm vi đã chọn (B15). Lô đã có chứng từ mà chưa có JobID hiện ở danh mục lô hàng (A12).
2. **Hoàn thiện dữ liệu và phân luồng** — CS kê khai, đưa chứng từ; nơi nhận lấy từ D/O; chưa kê khai đủ trường bắt buộc của các mục phạm vi đã chọn thì khoá thanh toán trên JobID.
3. **Giao việc hiện trường** — cán bộ quản lý hiện trường chọn người (phần mềm gợi ý `P-so-nguoi-goi-y-nhan-viec` (Delta: 2–3) người); phần mềm ghi chi phí định mức, cấp quyền thanh toán. Định mức lấy theo địa điểm làm việc × loại việc trong danh mục địa điểm (`location-catalog`, B20); định mức hải quan (mở tờ khai, kiểm hoá, thanh lý tờ khai) theo `service-delivery` E14; con số chờ phụ lục định mức (OQ-3). Quyết định phân công công việc chỉ sinh khi JobID có công tác phí: mỗi người một Quyết định mỗi tháng kèm bảng kê JobID và số tiền, sinh ở `fund-payments`; việc giao ở bước này là căn cứ của Quyết định (SOP tổng quát 4.6). Tiền chọn vỏ: OQ-48. Giao cho người chi nhánh khác thì tự ghi giao dịch nội bộ (B7). Khách thêm việc giữa chừng thì CS thêm việc phát sinh, cán bộ quản lý hiện trường duyệt, rồi việc vào bước này như thường (B18).
4. **Sinh YCVT** — mỗi container thực nhận một YCVT (B21). FCL: sau khi hiện trường xong việc tại cảng/bãi; chọn thiếu vỏ thì sinh YCVT dần theo container đã chọn (B16). Hàng lẻ, CFS, air: ngay khi giao việc, việc hiện trường chạy song song với Lệnh.
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
   <Chọn đủ số container thực nhận?> --Đủ--> đi tiếp
   | Thiếu (B16)
   v
(PM) Báo CS: "Chọn được 3/5 vỏ"
[CS] hỏi khách, chọn:
   +-- "Chọn tiếp": HT hoặc lái xe quay lại bãi; chọn được cái nào
   |     (PM) sinh thêm 1 YCVT; phí nâng dư "Đã trả, chưa dùng"
   |     tới cut-off chưa đủ --> (PM) nhắc CS chốt số
   +-- "Chốt số": [Cán bộ QL] duyệt (P-duyet-chot-so-container)
         (PM) ghi số thực nhận mới lên JobID
         (PM) huỷ thanh toán chưa trả, thu quyền, tính lại định mức phần bỏ
         (PM) phí nâng dư --> đánh dấu "Phí nâng không dùng" (B17)
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

### 5.8 Việc phát sinh (B18)

```
JobID đang ở Điều phối (phạm vi gốc đã khoá)
   |
   v
[CS] Thêm "Việc phát sinh": chọn từ danh sách phạm vi, ghi lý do
   |
   v
<[Cán bộ QL hiện trường] duyệt?>
   +-- Từ chối (bắt ghi lý do) --> báo CS; JobID giữ nguyên
   +-- Duyệt --> (PM) hạch toán ngay lên JobID: định mức, quyền thanh toán,
                 khoản thu thêm; hiện riêng với báo giá gốc
                 --> vào bước 3 Giao việc (5.1) như việc thường
```

### 5.9 Thu hoá đơn GTGT (B19)

```
[Lái xe] Tạo Yêu cầu thanh toán trên Lệnh (khoản có hoá đơn)
   |
   v
(PM) Tìm người nhận việc "Thu hoá đơn GTGT" theo phân công việc của JobID:
   1. HT đang giữ việc của JobID tại cùng cảng, bãi, kho  --không có-->
   2. HT làm việc gần nhất của JobID                     --không có-->
   3. CS của JobID
   |
   v
[Người nhận] Thu hoá đơn, chụp đưa lên JobID   (hoặc "Chuyển việc" như B2)
```

## 6. System Behavior Deep Dive

### 6.1 Decision Points

| ID | Flow | Khi nào | YES (nhánh đồng ý) | NO (nhánh từ chối) |
|---|---|---|---|---|
| DP-03 | Hoàn thiện dữ liệu | CS kê khai đủ trường bắt buộc của các mục phạm vi đã chọn | Mở thanh toán trên JobID | Khoá thanh toán |
| DP-22 | Mọi luồng | Mục phạm vi của bước có được chọn trên JobID (B15) | Hiện bước, kê khai, giao việc, đếm mốc | Bỏ bước, không đếm mốc |
| DP-04 | FCL xuất, nhập | Bãi có ePort và CS tự làm lệnh nâng | Sinh YCVT (bỏ qua giao việc, trừ FCL xuất chọn vỏ trước) | Giao việc hiện trường |
| DP-05 | FCL xuất | Bãi phải có xe mới chọn được vỏ | Lệnh nâng khống hoặc lái xe tự chọn vỏ | Chọn vỏ trước khi xe đến |
| DP-06 | Giao việc | Loại hàng FCL | Hiện trường xong việc mới sinh YCVT | Sinh YCVT ngay, hiện trường song song |
| DP-10 | Hạ hàng / hạ vỏ | Cảng/bãi hạ có ePort | CS làm lệnh hạ | Lái xe làm lệnh hạ |
| DP-14 | Giao việc hạ vỏ (FCL nhập) | JobID thực nhận 1 container | Gộp theo vận đơn + nơi hạ | Giao từng container |
| DP-23 | FCL xuất, chọn vỏ | Chọn đủ số container thực nhận | Đi tiếp | Báo CS chọn "Chọn tiếp" hoặc "Chốt số" (B16) |
| DP-24 | Chọn thiếu vỏ | CS chọn "Chọn tiếp" | Chọn tiếp tới cut-off, chọn được thì sinh thêm YCVT | "Chốt số": cán bộ quản lý duyệt, ghi số thực nhận mới |
| DP-25 | Việc phát sinh | Cán bộ quản lý hiện trường duyệt | Hạch toán ngay lên JobID, vào luồng giao việc | Báo CS kèm lý do, JobID giữ nguyên |

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
| Chọn vỏ (FCL xuất) | Đang chọn | Chọn tiếp | CS | Chọn thiếu vỏ, khách chờ được | Sinh YCVT cho container đã chọn; tới cut-off nhắc chốt |
| Chọn vỏ (FCL xuất) | Đang chọn, Chọn tiếp | Chờ duyệt chốt số | CS | Khách chốt số đã chọn | Cán bộ quản lý hiện trường nhận việc duyệt |
| Chọn vỏ (FCL xuất) | Chờ duyệt chốt số | Đã chốt | Cán bộ quản lý hiện trường | Duyệt | Số thực nhận mới lên JobID; huỷ thanh toán chưa trả, thu quyền, tính lại định mức phần bỏ; phí dư đánh dấu không dùng |
| Chọn vỏ (FCL xuất) | Chờ duyệt chốt số | Chọn tiếp | Cán bộ quản lý hiện trường | Từ chối, bắt ghi lý do | CS nhận lại việc |
| Chọn vỏ (FCL xuất) | Đang chọn, Chọn tiếp | Đã chốt | CS | `P-duyet-chot-so-container` tắt | Như dòng "Đã chốt" ở trên, không qua duyệt |
| Chọn vỏ (FCL xuất) | Đang chọn, Chọn tiếp | Đã chọn đủ | Phần mềm | Số container đã chọn bằng số thực nhận | Ngừng nhắc; ghi mốc kết thúc chờ |
| Việc phát sinh | — | Chờ duyệt | CS | Có lý do, mục thuộc danh sách phạm vi | Cán bộ quản lý hiện trường nhận việc duyệt |
| Việc phát sinh | Chờ duyệt | Đã duyệt / Từ chối | Cán bộ quản lý hiện trường | Từ chối bắt ghi lý do | Duyệt: hạch toán ngay lên JobID |

### 6.3 State Transitions

**Yêu cầu vận tải (YCVT)** — định nghĩa ở Quy trình điều phối mục 4.3. Feature này tạo YCVT; Điều vận lập Lệnh từ YCVT.

```
Đã được tạo --> Đã lập Lệnh vận tải --> Đã thực hiện Lệnh vận tải
```

- Điều vận khai số xe cần; mỗi lần lập Lệnh phần mềm trừ dần tới hết; không khai thì chỉ lập được 1 Lệnh. YCVT hiện "đã lập x/n Lệnh".
- Nhiều YCVT hàng lẻ được gộp vào 1 Lệnh nếu đủ một xe.

Vòng đời JobID xem `service-delivery` Mục 6.3; feature này đổi JobID từ "Chờ xử lý" sang "Đã tạo YCVT".

**Chọn vỏ (FCL xuất, khi chọn thiếu)**

```
Đang chọn --> Chọn tiếp --> (đủ) Đã chọn đủ
    |             |
    +-------------+--> Chờ duyệt chốt số --duyệt--> Đã chốt
                             |
                             +--từ chối--> Chọn tiếp
```

**Việc phát sinh:** `Chờ duyệt --> Đã duyệt | Từ chối`. Đã duyệt thì thành việc hiện trường thường.

### 6.4 Interrupted Transactions

| # | Tình huống | Xử lý |
|---|---|---|
| 1 | Mất sóng hoặc tắt app khi hiện trường đang chụp chứng từ | Lưu trên máy, tự đồng bộ khi có sóng. Giờ và vị trí lấy theo lúc chụp, không phải lúc gửi. Việc hiện nhãn "Chờ đồng bộ" |
| 2 | AI không đọc được chứng từ (ảnh mờ, mẫu lạ) | Chuyển sang nhập tay, ảnh hiện bên cạnh. Đánh dấu "nhập thủ công" để thống kê |
| 3 | Hai người cùng nhận một việc | Ai bấm "Nhận xử lý" trước giữ việc; người sau thấy tên người đang giữ (E-shipment-coordination-002) |
| 4 | Người được giao từ chối hoặc quá lâu không nhận việc | Việc quay về cán bộ quản lý giao lại. Thời gian "quá lâu": OQ-41 |
| 5 | D/O đổi kho khi xe đang chạy | Lệnh cập nhật nơi nhận, báo điều vận và lái xe (D4) |
| 6 | Sửa JobID (đổi Booking Note, giảm container, chốt số khi chọn thiếu vỏ) khi đã có YCVT, Lệnh | YCVT, Lệnh dư chưa giao lái xe thì tự huỷ; đã giao thì báo điều vận xử lý tay |
| 7 | Số container thực nhận tăng khi đã có YCVT | Sinh thêm YCVT cho phần tăng, báo điều vận (B21) |
| 8 | Tới cut-off mà vẫn "Chọn tiếp", chưa đủ vỏ | Nhắc CS chốt số; container đã có YCVT vẫn chạy |
| 9 | Lệnh nâng hết hạn khi chưa chọn đủ | Phí dư đánh dấu "Phí nâng không dùng" (B17) |
| 10 | CS chốt số trong lúc lái xe đang ở bãi chọn tiếp | Container đã chụp và ghi số trước lúc duyệt chốt vẫn có YCVT; số thực nhận tính cả container đó |

### 6.5 Other Edge Cases

- D/O đổi kho sau khi đã có Lệnh: Lệnh cập nhật theo; xe đã giao thì báo điều vận.
- CS bấm "Chuyển việc": bắt chọn lý do ("Hết giờ làm việc" hoặc "Khác" tự ghi); quyền thanh toán chuyển theo.
- Đầu ca, cuối ca trực ngoài giờ: bàn giao việc đang dở giữa người trực và người làm giờ hành chính (B3b).
- Nhân viên hiện trường từ chối chọn vỏ: JobID quay về cán bộ quản lý giao lại.
- Việc phát sinh trùng một mục phạm vi đã có trên JobID: chặn, báo CS mục đã có (E-shipment-coordination-004).
- Không tìm được ai cho việc "Thu hoá đơn GTGT" theo thứ tự B19 (JobID không có CS phụ trách): việc về cán bộ quản lý hiện trường.
- Nhắc chốt số, chờ duyệt rơi vào ngoài giờ: gửi người trực ngoài giờ (B3b).
- Địa điểm làm việc chưa có định mức: cảnh báo, cán bộ quản lý hiện trường nhập tạm kèm lý do (B20).

## 7. Validation, Limits & Wording

### 7.1 Validation rules

Quy tắc chung (bắt buộc, độ dài, ngày, email, số điện thoại) theo GR và E-common, không viết lại.

| Field | Rule |
|---|---|
| Số container | 4 chữ cái + 7 số, đúng chữ số kiểm tra ISO 6346; không trùng container đã có YCVT trong cùng JobID (mỗi container một YCVT) |
| Số tờ khai | 12 chữ số |
| Cut-off (FCL xuất) | Bắt buộc khi kê khai; AI không đọc ra thì CS nhập tay |
| VGM, số kiện, CBM, kg | Lớn hơn 0; AI đọc ra thì người chụp bắt buộc bấm xác nhận |
| Nơi nhận trên Lệnh | Lấy từ D/O, không nhập tay |
| Lý do bắt buộc | Chuyển việc · từ chối việc được giao · thêm việc phát sinh · từ chối việc phát sinh, chốt số · nhập tạm định mức |
| Việc phát sinh | Mục chọn từ danh sách phạm vi theo loại JobID; không trùng mục đã có trên JobID |
| Số container thực nhận khi chốt số | Lớn hơn 0, không lớn hơn số đang ghi trên JobID; không nhỏ hơn số container đã có YCVT |
| Lý do Chuyển việc (`P-ly-do-chuyen-viec`) | Delta: chọn 1 trong "Hết giờ làm việc" · "Khác" (bắt ghi nội dung) |

### 7.2 Limits & Quotas (exact values)

| Tham số | Giá trị | Window | Behavior khi vượt |
|---|---|---|---|
| Số người gợi ý nhận việc (`P-so-nguoi-goi-y-nhan-viec`) | Delta: 2–3 | mỗi việc | Quản lý vẫn bấm chọn |
| Ca trực ngoài giờ (`P-ca-truc-ngoai-gio`, `P-ban-giao-ca-truc`) | Delta: 17h30–8h; bàn giao bật | mỗi ngày | Cán bộ quản lý hiện trường giao người trực; người trực tự giao việc trong ca; bàn giao việc đầu ca, cuối ca |
| Gộp giao việc hạ vỏ (`P-gop-giao-viec-ha-vo`) | Delta: bật | mỗi JobID 1 container | Gộp theo vận đơn + nơi hạ |
| Thời gian chờ người nhận việc (`P-thoi-gian-cho-nhan-viec`) | Chưa có số (OQ-41) | mỗi việc được giao | Việc quay về cán bộ quản lý |
| Duyệt chốt số container (`P-duyet-chot-so-container`) | Delta: bật (chờ xác nhận OQ-71) | mỗi lần chốt số | Tắt thì CS chốt số là xong |
| Hạn chọn tiếp vỏ | Cut-off trên Booking Note | mỗi JobID FCL xuất | Nhắc CS chốt số |
| Hạn chờ duyệt chốt số, việc phát sinh (`P-han-duyet-dieu-phoi`) | Delta: chưa chốt (OQ-77) | mỗi lần chờ duyệt | Nhắc lại cán bộ quản lý hiện trường; ngoài giờ gửi người trực |
| Quyết định phân công công việc | 1 / người / tháng | tháng | Chỉ người có công tác phí trong tháng |

### 7.3 Wording samples (exact strings)

Ngôi "bạn", câu ngắn, không "Vui lòng" (theo design.md). Loại hiển thị theo GR-15: Inline dưới trường, Popup chặn giữa màn, Toast góc màn.

#### Error messages

| Mã | Loại | Tình huống | Câu |
|---|---|---|---|
| E-shipment-coordination-001 | Inline | Số container sai chữ số kiểm tra | "Số container không đúng. Kiểm tra lại chữ số cuối." |
| E-shipment-coordination-002 | Popup | Nhận việc đã có người nhận | **Việc đã có người nhận** · "[Tên] đã nhận xử lý lúc 14:05." |
| E-shipment-coordination-003 | Popup | Thanh toán khi JobID chưa kê khai đủ | **Chưa thanh toán được** · "Kê khai đủ thông tin JobID trước khi thanh toán chi phí." |
| E-shipment-coordination-004 | Inline | Việc phát sinh trùng mục đã có | "JobID đã có [mục phạm vi]. Chọn mục khác." |
| E-shipment-coordination-005 | Inline | Chốt số nhỏ hơn số container đã có YCVT | "Đã có [n] container có YCVT. Số chốt không nhỏ hơn [n]." |
| E-shipment-coordination-006 | Inline | Số container đã có YCVT trong JobID | "Container [số] đã có YCVT. Chụp container khác." |
| E-common-009 | Toast | Mất mạng | Dùng câu chung |
| E-common-008 | Toast | Lỗi hệ thống | Dùng câu chung |

#### Success messages

- "Đã giao việc cho [tên]" · "Đã chuyển việc"
- "Đã gửi việc phát sinh chờ duyệt" · "Đã duyệt việc phát sinh"
- "Đã chốt [n] container"

#### Info / neutral messages

| Tình huống | Câu |
|---|---|
| Mất sóng | "Chờ đồng bộ. Ảnh sẽ gửi khi có mạng." |
| AI không đọc được | "Không đọc được chứng từ. Nhập tay theo ảnh bên cạnh." |
| Chọn thiếu vỏ (báo CS) | "Chọn được [3]/[5] vỏ. Hỏi khách để chọn tiếp hoặc chốt số." |
| Tới cut-off chưa đủ vỏ | "JobID [mã] tới cut-off còn thiếu [2] vỏ. Chốt số để kết thúc chọn vỏ." |
| Chờ duyệt quá hạn | "JobID [mã] có [chốt số / việc phát sinh] chờ duyệt quá [n] giờ." |
| Địa điểm chưa có định mức | "[Địa điểm] chưa có định mức cho [loại việc]. Nhập tạm và ghi lý do." |

### 7.4 Bối cảnh hệ thống (mức nghiệp vụ)

**Thông tin cần lưu**
- Trên JobID: chứng từ vận hành (tờ khai + QR, D/O, eDO, booking, thông báo hãng tàu); các mốc (cut-off, hạn eDO, hạn trả vỏ); người giữ quyền thanh toán; số ngày miễn phí lưu container, lưu vỏ.
- Trên việc hiện trường: người được giao, chi phí định mức, quyền thanh toán, ảnh chứng từ, số AI đọc và người xác nhận.
- Việc phát sinh: mục phạm vi, lý do, người thêm, người duyệt, lúc duyệt, khoản hạch toán.
- Chọn vỏ: số đã chọn / số thực nhận, lựa chọn của CS, người duyệt chốt số, số thực nhận trước và sau.
- Danh mục lô hàng: chứng từ gốc, kênh nhận, khách, JobID nháp đi kèm.
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
| CS | Chọn thiếu vỏ; tới cut-off chưa đủ vỏ; việc phát sinh bị từ chối | Thông báo đẩy + "Việc của tôi" |
| Cán bộ quản lý hiện trường | Việc phát sinh, chốt số chờ duyệt; chờ duyệt quá hạn | Thông báo đẩy + "Việc của tôi" |
| Người nhận việc thu hoá đơn GTGT | Lái xe tạo Yêu cầu thanh toán có hoá đơn | Thông báo đẩy + "Việc của tôi" |
| Điều vận | Số container thực nhận đổi khi đã có YCVT; bắt đầu, kết thúc chờ chọn vỏ (tính lưu xe) | Thông báo đẩy |
| Kế toán | Việc phát sinh được duyệt; số container thực nhận đổi | "Việc của tôi" |

**Việc phần mềm tự chạy theo giờ:** bắt đầu đếm mốc khi JobID vào Điều phối (cảnh báo quá mốc ở Điều vận) · nhắc bàn giao đầu ca, cuối ca (`P-ban-giao-ca-truc`) · thu việc quá lâu không ai nhận (OQ-41) · nhắc chốt số khi tới cut-off · nhắc chờ duyệt quá `P-han-duyet-dieu-phoi`.

**Cần gần như tức thời:** giao việc mới.

## 8. Assumptions

- SOP của Delta là thiết kế to-be của khách, không phải cách đang làm.
- SOP Quy trình điều phối mục 5.4.2.4 ghi "nhân viên CS upload đủ Lệnh nâng hàng" trong bước của hiện trường; hiểu là nhân viên hiện trường upload (chờ xác nhận, OQ-40).
- Lệnh nâng vỏ còn hạn thì phí nâng đã trả dùng tiếp được cho lần chọn sau, không phải hoàn (B17).
- "Người gần lái xe nhất" ở Phân hệ APAS mục 3.1.2 hiểu theo phân công việc của JobID, không theo vị trí điện thoại (B19).
- Khoản thu thêm của việc phát sinh lấy theo báo giá hoặc hợp đồng của JobID; mục chưa có đơn giá thì đi theo cờ "chưa có đơn giá" của `service-delivery`.

## 9. Risks

| Rủi ro | Khả năng | Hậu quả nghiệp vụ | Cách phòng |
|--------|----------|-------------------|-----------|
| Hiện trường vẫn gửi ảnh và chứng từ qua Zalo, không dùng app | thường | Mất bằng chứng; chi phí không lên JobID | App chạy khi mất sóng; thao tác chính làm được bằng một tay |
| Thiếu dữ liệu nền: thuộc tính cảng/bãi, định mức chi phí | thường | Phân luồng sai | Chốt danh mục trước khi chạy thật; người có quyền cập nhật; bám OQ-3 |
| AI đọc sai chứng từ (VGM, số container, tên kho) | thỉnh thoảng | VGM sai thì lỡ tàu, bị phạt; đi nhầm kho | Người chụp bắt buộc xác nhận; kiểm chữ số container |
| Phí nâng đã trả mà không nâng được vỏ bị tính vào chi phí JobID | thỉnh thoảng | Giá vốn JobID sai, bảng kê sai | Chốt số thì đánh dấu "Phí nâng không dùng"; đòi hoàn xử lý ngoài phần mềm theo OQ-28 |
| Khách gọi thêm việc nhưng không ghi lên JobID | thường | Làm mà không thu được tiền; chi phí lệch | Việc phát sinh hạch toán ngay khi duyệt; chưa có việc phát sinh thì không cấp quyền thanh toán |

## 10. Success Criteria (preliminary)

Mỗi tiêu chí gắn một vấn đề ban đầu. Số hiện trạng và mục tiêu chờ khách (OQ-44, ở `service-delivery`).

| Vấn đề | Tiêu chí | Mục tiêu |
|---|---|---|
| a. Nhập lại nhiều lần | Tỉ lệ trường tự điền (AI đọc hoặc kế thừa từ JobID) trên tổng trường phải nhập khi kê khai và ở việc hiện trường | ? |
| b. Giao việc qua Zalo | Tỉ lệ việc hiện trường được giao và nhận trên app | ? |
| c. Bị phạt vì quá mốc | Tỉ lệ JobID có đủ mốc cut-off, lưu container, lưu vỏ ngay sau kê khai | ? |
| e. Phát sinh không lên JobID | Thời gian từ lúc khách yêu cầu thêm việc tới lúc việc phát sinh được duyệt và hạch toán lên JobID | ? |
| f. Số container lệch | Tỉ lệ JobID FCL xuất có số container thực nhận khớp số YCVT khi chốt Lệnh | ? |
| g. Lô bị sót | Số lô trong danh mục lô hàng chưa thành JobID khi còn dưới 24 giờ tới cut-off | ? |

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
| OQ-48 | Tiền chọn vỏ container (nhân viên hiện trường trả cho quản lý bãi để lấy vỏ tốt) có áp định mức theo từng bãi và phần mềm tự ghi lên JobID khi giao việc chọn vỏ, giống định mức hải quan không? Hay hiện trường kê số thực chi khi thanh toán? SOP xếp khoản này vào nhóm Vận tải (công tác phí), nhưng câu "xây dựng định mức theo địa điểm… tự áp lên JobID" chỉ đứng sau 3 khoản hải quan. | Quy trình cung cấp dịch vụ tổng quát (24/9/2026), mục 4.6 | Chưa hỏi Delta |
| OQ-71 | Khi chọn thiếu vỏ, nháp giao CS hỏi khách rồi bấm "Chọn tiếp" hoặc "Chốt số" (SOP chỉ ghi "thỏa thuận với khách hàng", và hiện trường, lái xe ghi số container ngược về JobID). Delta đồng ý CS là người bấm không? "Chốt số" có cần cán bộ quản lý hiện trường duyệt không (vì làm giảm doanh thu JobID)? Tạm ghi là có (B16) | Quy trình điều phối, mục 4.6 "Xác định số lượng container xuất FCL trên JobID" | Chưa hỏi Delta |
| OQ-72 | Việc "Thu hoá đơn GTGT" có hạn bao lâu kể từ khi lái xe tạo Yêu cầu thanh toán? Quá hạn thì nhắc ai? | Phân hệ APAS (17/10/2026), mục 3.1.2 | Chưa hỏi Delta |
| OQ-73 | Danh mục lô hàng cần hiện những thông tin gì (tàu, chuyến, ETA/ETD, cut-off, số container…), lọc theo gì, ai được xem (CS chi nhánh, cán bộ quản lý)? | Phân hệ APAS (17/10/2026), mục 2.2.1 | Chưa hỏi Delta |
| OQ-74 | Ai ký Quyết định phân công công việc hằng tháng cho CS và nhân viên hiện trường? | Quy trình cung cấp dịch vụ tổng quát (24/9/2026), mục 4.6 | Chưa hỏi Delta |
| OQ-75 | Khi chọn vỏ FCL xuất còn dở (đang "Chọn tiếp" hoặc chờ duyệt chốt số), JobID không được lên "Đã thực hiện Lệnh vận tải" dù các Lệnh đã có đều duyệt. Delta đồng ý không? | Quy trình điều phối, mục 4.6 "Xác định số lượng container xuất FCL trên JobID" | Chưa hỏi Delta |
| OQ-76 | Khách báo thêm việc sau khi JobID đã "Hoàn thành dịch vụ" (hoặc đã xuất hoá đơn): mở lại JobID có duyệt, hay ghi vào JobID mới? | Quy trình cung cấp dịch vụ tổng quát (24/9/2026), mục 5.1.2 | Chưa hỏi Delta |
| OQ-77 | Chốt số container và việc phát sinh chờ cán bộ quản lý hiện trường duyệt bao lâu thì nhắc lại (`P-han-duyet-dieu-phoi`)? | Chưa có trong tài liệu khách gửi | Chưa hỏi Delta |

## 12. Next Steps

Đã tách từ brainstorm Điều phối gộp ngày 2026-10-12. Tiếp theo:
- Hỏi lại Delta các câu còn mở ở Mục 11 (BL-041)
- Hỏi Delta OQ-71 đến OQ-77 (cùng đợt BL-041)
- `/user-flow shipment-coordination` — chạy lại; userflow tách máy từ bản nháp ngày 07/10, còn nội dung cũ (Chuyển cho hiện trường), chưa có danh mục lô hàng, việc phát sinh, chọn thiếu vỏ, khoản chờ hoàn
- `/srs shipment-coordination` — đặc tả FR, BR, Error Matrix
