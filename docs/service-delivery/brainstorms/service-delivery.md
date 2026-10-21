---
type: brainstorm
feature: service-delivery
status: draft
status_changed: 2026-10-20
status_reason: "đã review upstream, không cần sửa"
updated: 2026-10-20
links:
  - docs-input/tich-hop/ecus-api-yeu-cau-2025-10-26/ecus-api-yeu-cau-2025-10-26.md
  - docs-input/sop/sop-cung-cap-dich-vu-tong-quat.md
  - docs-input/sop/sop-dieu-phoi.md
  - docs-input/sop/giao-nhan-hang-hoa/giao-nhan-hang-hoa.md
  - docs-input/sop/apas-thanh-toan-doi-soat/apas-thanh-toan-doi-soat.md
  - docs-input/sop/sop-ban-do-kien-thuc.md
  - docs-input/sop/delta-3-0-master-plan/delta-3-0-master-plan.md
  - docs-input/sop/quan-ly-quy-thanh-toan/quan-ly-quy-thanh-toan.md
  - docs-input/du-lieu-mau/thong-ke-chi-phi-chung-tu-cbt.md
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
> Cập nhật 2026-10-20 theo sổ đối chiếu nguồn: Quy trình cung cấp dịch vụ tổng quát (24/9/2026), Phân hệ APAS (17/10/2026), Giao nhận hàng hoá (18/9/2026), Phần mềm Delta 3.0 (16/10/2026) mục 3.1.3, Quy trình quản lý quỹ và thanh toán Đính kèm 05 Job ID (26/7/2026), Thống kê chi phí chứng từ CBT (3/9/2026).

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
- Gồm: tạo và duyệt JobID (JobID nháp từ chứng từ đọc tự động, loại JobID, danh sách phạm vi dịch vụ, kê khai mua ngoài, thông tin viết hoá đơn trả hộ, kiểm nợ quá hạn và hạn mức, gia hạn nợ); phân JobID sang Điều phối (có thủ tục giao nhận), thẳng sang Điều vận (CBT, đường sắt, không làm hiện trường) hoặc thẳng sang ghi doanh thu (không có vận tải); quy tắc ghi nhận chi phí, doanh thu lên JobID; hoàn thành dịch vụ; tự ghi nhận giao dịch nội bộ khi làm trái tuyến (B7); hoá đơn trả hộ, hoá đơn điện tử, đổi bên xuất hoá đơn; khai tờ khai hải quan nháp và kết nối phần mềm khai hải quan (Ecus là bên đầu tiên).
- Ranh giới với 2 feature cùng chuỗi:
  - Điều phối (`shipment-coordination`): nhận JobID "Chờ xử lý", kê khai, giao việc hiện trường, sinh YCVT. Màn Chi tiết JobID dùng chung cho cả 3 feature, thuộc feature này; Điều phối, Điều vận thêm phần kê khai, YCVT/Lệnh lên màn đó.
  - Điều vận (`transport-dispatch`): từ YCVT lập, chạy, chốt và duyệt Lệnh. Lệnh duyệt xong thì chi phí chuyển về JobID.
- Không gồm (feature riêng, chỉ đảm bảo dữ liệu đủ và đúng JobID): màn bảng kê, công nợ (`debt-management`: duyệt doanh thu, mua ngoài, nợ phải thu, phải trả, đối soát hoá đơn đầu vào, lệch kỳ báo cáo và kỳ thanh toán), kết nối MISA (ngoài phần lấy hoá đơn điện tử); quỹ, tạm ứng, thanh toán (`fund-payments`); thanh toán trả hộ qua ngân hàng — duyệt, QR, uỷ nhiệm chi, API ngân hàng (`payment-on-behalf`); phạm vi xem dữ liệu chi nhánh khác (feature Phân quyền); danh mục lô hàng (`shipment-coordination`) và dashboard tổng mọi chi nhánh (màn riêng); danh mục địa điểm (`location-catalog`); JobID kế toán (`cost-catalog`), JobID xưởng (phân hệ xưởng); cho thuê kho làm trên phần mềm quản lý kho riêng nối với hệ thống, giai đoạn 2. Cước quốc tế (đường biển, hàng không) và cho thuê kho có trong phạm vi phân hệ nhưng chưa có loại JobID (OQ-70).
- Xử lý ngoài phần mềm: thoả thuận với khách về khoản chi ngoài định mức.
- Ứng dụng: Delta Super App, web cho CS, kế toán, cán bộ quản lý.

**Nguồn:** Quy trình cung cấp dịch vụ tổng quát (mục 4, 5.1–5.5), Quy trình điều phối (mục 4.2 Job ID nghiệp vụ), Phân hệ APAS (17/10/2026, mục 2.2 DIS, 3.3), tài liệu Hoá đơn trả hộ 01/10/2026, báo cáo điều tra `docs/_research/2026-10-02-field-document-reading.md`.

**Nhãn đề xuất:** [SOP to-be] = SOP đã yêu cầu, phần mềm làm theo · [SOP+] = SOP có nêu, đề xuất làm thêm · [Mới] = SOP chưa có. Chỉ [SOP+] và [Mới] tính là điểm khác biệt.

## 3. User Types (preliminary)

Phân quyền theo chức năng, không cố định vai trò. Luồng và sơ đồ vẫn ghi theo vai trò nghiệp vụ.

| User Type | Pain Point | Primary Need |
|-----------|-----------|--------------|
| CS | Nhập lại chứng từ khi tạo JobID; không biết JobID đang kẹt ở đâu | Tạo JobID từ chứng từ, theo dõi tới khi hoàn thành dịch vụ |
| Điều vận | Tạo JobID cho CBT, đường sắt | Tạo JobID nhanh, đi thẳng sang lập Lệnh |
| Sales | Khách nợ quá hạn mà vẫn cần làm hàng | Tạo yêu cầu gia hạn nợ để JobID được duyệt |
| Cán bộ quản lý | Duyệt bằng tin nhắn | Duyệt thông tin viết hoá đơn bất thường, gia hạn nợ trong "Việc của tôi" |
| Ban giám đốc | Duyệt gia hạn nợ bằng tin nhắn | Duyệt bước cuối gia hạn nợ trong "Việc của tôi" |
| Kế toán | Chi phí về muộn, thiếu, không gắn JobID | Doanh thu, chi phí đã gắn đúng JobID khi dịch vụ hoàn thành |
| Đại diện khách hàng | Phải gọi CS hỏi tình trạng | Theo dõi lô, nhận file xuất |
| Trợ lý AI | — | Đọc chứng từ khách khi tạo JobID |

Mọi vai trò có màn "Việc của tôi" kèm thông báo đẩy mở thẳng vào việc. Mặc định chỉ thấy JobID của chi nhánh mình.

### 3.1 Tác vụ chính

| Vai trò | Tác vụ | Tần suất | Mức quan trọng | Ghi chú |
|---------|--------|----------|----------------|---------|
| CS | ★ Tạo JobID từ chứng từ (kiểm JobID nháp, khai phạm vi, mua ngoài, xác nhận thông tin viết hoá đơn trả hộ); ghi doanh thu; giao chứng từ gốc; hoàn thành dịch vụ | Nhiều lần mỗi ngày | cao | Thiếu doanh thu; khách chưa nhận căn cứ thanh toán |
| CS, Sales | Tạo yêu cầu gia hạn nợ quá hạn | Thỉnh thoảng | trung | JobID dừng, không làm được hàng |
| Cán bộ quản lý | Duyệt thông tin viết hoá đơn bất thường; duyệt gia hạn nợ bước 1 | Vài lần mỗi ngày | trung | Xuất sai hoá đơn |
| Ban giám đốc | Duyệt gia hạn nợ bước 2 | Thỉnh thoảng | trung | Cho khách mất khả năng trả nợ làm tiếp |
| Kế toán | Nhận chi phí đã gắn Lệnh/JobID | Hằng ngày, dồn vào kỳ chốt | trung | Chốt kỳ trễ; hạch toán sai |
| Đại diện khách hàng | Theo dõi tình trạng lô; nhận file xuất | Thỉnh thoảng | thấp | Gọi hỏi CS nhiều |

## 4. Capabilities Breakdown

### P0 — must have

Mục nào không ghi ở P1, P2 dưới đây là P0 (DEC-229). DP-01 ở P0 do người tạo duyệt tay, đúng SOP tổng quát mục 4.2.3 cho giai đoạn trước khi xong giai đoạn 1.

**Luồng lõi:** tạo, duyệt JobID → phân sang Điều phối, Điều vận hoặc thẳng sang ghi doanh thu → (Điều phối, Điều vận làm việc, ghi chi phí lên Lệnh và JobID) → ghi doanh thu → hoàn thành dịch vụ (Mục 5).

**Nhóm A — giảm nhập liệu**
- A9 [SOP+] [Lõi] Hoá đơn điện tử lấy qua kết nối nhà cung cấp hoá đơn điện tử (kết nối đầu tiên: MISA); không khớp thì chụp + nhập tay, gắn cờ "Chưa khớp hoá đơn điện tử".
- A10 [SOP+] [Lõi] Tờ khai hải quan do chính doanh nghiệp khai qua phần mềm khai hải quan có kết nối (Ecus là bên đầu tiên, Nhóm H): sau khi khai chính thức, số tờ khai, ngày tờ khai, phân luồng, mã vạch lô hàng hoặc container và chứng từ đã đính kèm tờ khai tự bổ sung vào bộ chứng từ của JobID; CS không phải quét QR hay tải lại. Tờ khai khách tự khai thì vẫn quét QR (`shipment-coordination` A2). Nguồn: Kết nối API với Ecus (26/10/2025), mục 3.1.
- A11 [SOP to-be] [Lõi] [Cấu hình] JobID nháp từ chứng từ đọc tự động: phần mềm nhận chứng từ khách qua các kênh `P-kenh-nhan-chung-tu` (Delta: Zalo OA, Telegram, WeChat, Gmail, tải lên app hoặc web), đọc mỗi chứng từ một lần rồi tạo JobID ở trạng thái Nháp, điền sẵn phần lớn trường; tự gán mã khách theo người gửi và số báo giá hoặc hợp đồng còn hiệu lực; kiểm số container theo ISO 6346. Dữ liệu đọc ra bị từ chối nếu sai kiểu, số âm, ngày sai định dạng, hoặc thiếu mã số thuế, số hoá đơn, tổng tiền; mã số thuế phải đủ 10 hoặc 13 số; tiền trước thuế cộng VAT phải bằng tổng (Phần mềm Delta 3.0, 16/10/2026, mục 2.2.1). CS hoặc điều vận kiểm, sửa rồi chuyển duyệt; chỗ người sửa so với bản đọc được lưu lại. Chứng từ không nhận ra khách thì vào hàng đợi tra soát thủ công, không tạo JobID. App chặn ảnh mờ (khoá nút "Gửi", bắt chụp lại). Vẫn có luồng tạo JobID thủ công khi đọc lỗi hoặc loại JobID không có chứng từ định danh. Phần đọc chứng từ (DIS) là một khối riêng dùng chung; tạo JobID nháp là một ứng dụng của nó, cùng lần đọc ra danh mục lô hàng (`shipment-coordination` A12) và dữ liệu hoá đơn đầu vào (`debt-management`) (DEC-230). Nguồn: Phân hệ APAS (17/10/2026), mục 2.2–2.2.4.

**Nhóm B — quy trình**
- B7 [SOP+] [Gói: Đa chi nhánh] [Cấu hình] Giao dịch nội bộ theo 2 trường hợp trong SOP: tạo JobID trái tuyến (TH1) hoặc giao việc trái tuyến (TH2, phát sinh ở bước giao việc của Điều phối). Chi nhánh làm toàn bộ dịch vụ cho JobID do chi nhánh khác tạo thì phải tự tạo JobID (thành TH1). Phần mềm lấy 2 dấu hiệu này để tự ghi nhận giao dịch nội bộ và tự hạch toán. Lợi nhuận chia theo `P-ty-le-chia-lai-noi-bo` (Delta: 50/50 lãi gộp, chỉ hạch toán sau khi đã chốt bảng kê công nợ phải thu, phải trả).
- B8 [SOP to-be] [Lõi] [Cấu hình] Loại JobID: mỗi JobID có một loại, quyết định chứng từ định danh, ai được tạo và mục phạm vi nào được chọn. Bộ loại là `P-loai-jobid` (Delta: J01–J12, bảng ở Mục 5.3; bảng mã cần Delta xác nhận, OQ-69). Xe thuê bao: mỗi ngày một JobID, nhiều Lệnh. Mỗi loại có 3 nhóm trường: định danh (bắt buộc để tạo, giữ vĩnh viễn), nghiệp vụ (phát sinh khi làm, giữ tới khi thanh toán xong với khách), hoàn thiện (khối lượng dịch vụ đã làm, mất hàng, hỏng hàng, bồi thường, khiếu nại; giữ vĩnh viễn). Danh sách trường từng loại theo Quy trình quản lý quỹ và thanh toán, Đính kèm 05 phụ lục 4.1.
- B9 [SOP to-be] [Lõi] [Cấu hình] Danh sách phạm vi dịch vụ ghi ngay khi tạo JobID: thủ tục hải quan (khai báo gồm kiểm hoá, thanh lý tờ khai); thủ tục chuyên ngành (chọn từ danh mục thủ tục chuyên ngành của khách); vận tải nội địa; giao nhận tại cảng (lấy lệnh giao hàng, nâng container hàng, nâng container rỗng, cược vỏ, chọn vỏ — mục nào hiện tuỳ loại JobID); yêu cầu khác. Mục hải quan và chuyên ngành chỉ hiện với loại JobID có thủ tục hải quan `P-loai-jobid` (Delta: J01–J07). Đường sắt không có thủ tục hải quan, không nâng hạ ở ga nên khoá 2 mục này. Thủ tục chuyên ngành chọn "tự làm" (chi phí định mức) hoặc "mua ngoài". Đổi phạm vi được tới trước khi JobID vào Điều phối (mốc với JobID không qua Điều phối và "một bước" của luồng thủ công: OQ-66).
- B10 [SOP to-be] [Lõi] Trường thêm ở bước tạo và duyệt JobID: số báo giá hoặc hợp đồng cung cấp dịch vụ; số container thực nhận khi chỉ làm một phần số container trên Booking Note hoặc vận đơn (hàng xuất, nhập nguyên container: mỗi container một YCVT); thoả thuận khác và yêu cầu đặc biệt của khách, hiện cho nhân viên nghiệp vụ và lái xe.
- B11 [SOP to-be] [Lõi] Xác nhận thông tin viết hoá đơn trả hộ khi tạo JobID: phần mềm hiện thông tin viết hoá đơn ghi trên mã khách, CS xác nhận. Lô hàng cần thông tin khác mã khách (khách lẻ của 3PL chưa có mã khách riêng) thì CS nhập thông tin cho lô, cán bộ quản lý duyệt. Thông tin đi theo JobID sang YCVT và Lệnh.
- B12 [SOP to-be] [Lõi] JobID không có vận tải (chỉ thủ tục hải quan, chuyên ngành, giá trị gia tăng) không vào Điều phối, Điều vận: ghi chi phí mua ngoài nếu có, rồi ghi doanh thu và hoàn thành dịch vụ.
- B13 [SOP to-be] [Lõi] Gia hạn nợ quá hạn: khách có nợ quá hạn mà vẫn cần làm hàng thì JobID được duyệt khi có gia hạn nợ đã duyệt (DEC-227). Luồng tạo, duyệt yêu cầu gia hạn (`P-cap-duyet-gia-han-no`, `P-so-ngay-gia-han-no-toi-da`) và cách tính hạn mức thuộc `debt-management`; feature này chỉ dùng kết quả ở DP-01 (DEC-230).

- B14 [SOP to-be] [Lõi] JobID không doanh thu: JobID tạo để làm việc không thu tiền (làm từ thiện, hỗ trợ khách hàng, đối tác, chạy bù chuyến xe tuyến bị hỏng). Khách trên JobID là chính doanh nghiệp hoặc chi nhánh; toàn bộ chi phí ghi vào chi phí quản lý; có báo cáo định kỳ tháng, quý, năm các chi phí này. Nguồn: Quy trình quản lý quỹ và thanh toán, Đính kèm 05 mục 2.1.3.
**Nhóm D — từ SOP Giao nhận hàng hoá**
- D9 [SOP+] [Lõi] Theo dõi mã vạch gốc air: Đang ở hiện trường → CS đã nhận → Đã giao khách; đánh dấu "cần chuyển mã vạch gốc" trên từng JobID; chưa giao khách thì JobID có cờ ở bước ghi nhận doanh thu.
- D10 [SOP to-be] [Lõi] CBT đổi bên xuất hoá đơn trên JobID tới trước khi xuất hoá đơn, không phải huỷ Lệnh; bên thứ ba chưa có mã thì tạo việc "Đăng ký bên thanh toán" kèm thoả thuận ba bên. JobID CBT luôn tạo theo mã khách chính; bên xuất hoá đơn (mã khách cấp 2 hoặc bên thứ ba được uỷ quyền) chọn được cả sau khi hoàn thành Lệnh. CBT có thủ tục hải quan thì thủ tục giao nhận tại cửa khẩu làm sau khi lập Lệnh (ghi ở `transport-dispatch`).
- D11 [SOP to-be] [Gói: CBT] [Cấu hình] Thanh toán phí dịch vụ bằng chuyển khoản, tiền tệ theo `P-tien-te-thanh-toan` (Delta: VND, USD); nhận tiền mặt cho phí dịch vụ theo `P-nhan-tien-mat-phi-dich-vu` (Delta: tắt). Nguồn: Giao nhận hàng hoá (18/9/2026), mục 3.4.1.1.

**Nhóm E — chi phí, doanh thu (vấn đề e)**
- E1 [SOP to-be] [Riêng Delta] Chi ngoài định mức: không làm luồng xin duyệt riêng trên app. Thoả thuận với khách giải quyết ngoài phần mềm; khoản chi ghi nhận và chi trả qua Quy trình cung cấp dịch vụ (chi phí mua ngoài) hoặc thanh toán không hoá đơn (Quy trình quản lý quỹ và thanh toán).
- E2 [SOP to-be] [Lõi] [Cấu hình] Cách trả chi phí mặc định: nhân viên quét QR hoặc nhập tài khoản đối tác, trả từ tài khoản công ty qua ngân hàng; khoản chi ghi vào dư nợ tạm ứng của nhân viên và tự giảm khi hoá đơn về khớp giao dịch. Trả bằng tiền cá nhân là ngoại lệ, chỉ dưới `P-nguong-tam-ung` (Delta: 5.000.000 ₫, hạn mức chi tiền mặt theo quy định thuế); hoá đơn đó đi luồng thanh toán hoá đơn không có mã giao dịch ngân hàng, duyệt ở `debt-management`. Quy trình trả, dư nợ tạm ứng, duyệt chi thuộc `fund-payments` và `payment-on-behalf`; feature này giữ quy tắc khoản chi gắn đúng JobID (DEC-230). Bắt chọn có/không hoá đơn. Nguồn: Phân hệ APAS (17/10/2026), mục 3.3; Quy trình cung cấp dịch vụ tổng quát, mục 4.6 điều kiện 5. Nghĩa của "Dư nợ tạm ứng 2": OQ-68.
- E6 [SOP to-be] [Lõi] Nút tạo Yêu cầu thanh toán trên Lệnh/JobID, gắn chi phí đúng Lệnh/JobID; việc "Thu hoá đơn GTGT" giao người gần lái xe nhất, quy tắc chọn người ở Điều phối B19; hiện trạng thái thanh toán. Màn Yêu cầu thanh toán của lái xe vẽ ở Điều vận (`payment-request`). Phần duyệt, QR, uỷ nhiệm chi, API ngân hàng thuộc `payment-on-behalf`.
- E9 [SOP+] [Lõi] Hoá đơn trả hộ ghi trên JobID. Khi lập bảng kê nợ phải thu, phần mềm đánh dấu hoá đơn trả hộ mà khách không xác nhận thanh toán. Cách xử lý tiếp chờ khách trả lời (OQ-6).
- E12 [SOP to-be] [Lõi] Kê khai nhu cầu mua ngoài ngay khi tạo JobID, theo cùng danh sách phạm vi (B9). Ghi chi phí mua ngoài lên JobID 3 bước: tạo bản ghi, kê loại dịch vụ mua ngoài (theo danh mục), nhà cung cấp, đơn giá, tổng chi phí, cách thanh toán (bảng kê chi phí trả hộ tách riêng), chuyển duyệt. Duyệt và thanh toán nhà cung cấp thuộc `debt-management`.
- E13 [SOP to-be] [Lõi] JobID không có thủ tục hải quan trong phạm vi thì chặn ngay lúc kê: không tạo được mua ngoài dịch vụ hải quan, không thanh toán được chi phí định mức hải quan. Câu báo: "JobID này không có thủ tục hải quan trong phạm vi. Đổi phạm vi trước nếu cần."
- E14 [SOP to-be] [Lõi] Chi phí định mức hải quan (tiền mở tờ khai, kiểm hoá, thanh lý tờ khai): phần mềm tự áp theo định mức của địa điểm làm thủ tục, nhân viên không tự gõ số tiền. Định mức từng địa điểm là dữ liệu của khách, sống trong danh mục địa điểm (`location-catalog`). Khi JobID có công tác phí, phần mềm sinh mỗi người một Quyết định phân công công việc mỗi tháng, kèm bảng kê JobID, ở `fund-payments` (Điều phối B20); Quyết định giao Lệnh hằng tháng cho lái xe ở `transport-dispatch`.
- E15 [SOP to-be] [Lõi] Chi phí từ hoá đơn chưa gắn được khoản chi (hoá đơn vô chủ) lên JobID sau khi duyệt xong. Quy trình duyệt và việc đưa chi phí lên JobID do `debt-management` thực hiện.
- E16 [SOP to-be] [Lõi] Ghi doanh thu dịch vụ lên JobID 3 bước: tạo bản ghi, kê loại dịch vụ đã cung cấp theo danh sách phạm vi, đơn giá, tổng phí, chuyển duyệt. Cán bộ quản lý duyệt doanh thu ở Quy trình quản lý nợ phải thu (`debt-management`). JobID chỉ sang "Hoàn thành dịch vụ" khi doanh thu đã duyệt.
- E17 [SOP to-be] [Lõi] Lập bảng kê bị chặn khi JobID thiếu chi phí hoặc doanh thu so với danh sách phạm vi, hoặc có Lệnh nâng, hạ container mà chưa có chi phí nâng, hạ. Chặn ở bước lập bảng kê, không chặn bước Hoàn thành dịch vụ. Feature này định nghĩa điều kiện dữ liệu; `debt-management` thực hiện việc chặn (DEC-230).
- E18 [SOP to-be] [Lõi] [Cấu hình] Doanh thu, chi phí của JobID vào kỳ báo cáo chứa ngày JobID chuyển "Hoàn thành dịch vụ". Độ dài kỳ `P-ky-bao-cao` (Delta: tháng, từ 00:00 ngày đầu tới 24:00 ngày cuối tháng). Lệch giữa kỳ báo cáo và kỳ thanh toán với khách xử lý ở `debt-management`.

- E19 [SOP+] [Gói: CBT] Chi phí CBT trả nhà cung cấp ghi thẳng lên JobID, không qua Lệnh, chỉ phát sinh khi doanh nghiệp làm thủ tục hải quan cho lô. Hai cách trả: kế toán chuyển thẳng (phí hạ tầng cửa khẩu); trả sau theo hợp đồng và hoá đơn (dịch vụ khai báo thủ tục tại cửa khẩu — tính là mua ngoài, E12; phí bãi, cân xe). Danh mục loại phí và đơn giá là dữ liệu [Riêng Delta] (cửa khẩu Chalo, Hữu Nghị; bãi, cân Viettel). Chi phí trả cho lái xe ghi trên Lệnh (`transport-dispatch` E11). Nguồn: Thống kê chi phí chứng từ CBT (3/9/2026), mục I.
- E20 [SOP to-be] [Lõi] Hoa hồng trả cho khách hàng: nhóm phí riêng trong danh mục khoản mục chi phí (`cost-catalog`), ghi trên JobID nghiệp vụ, thanh toán theo mã khách ở `fund-payments`. Nguồn: Phần mềm Delta 3.0 (16/10/2026) mục 3.1.3; Đính kèm 05 phụ lục 4.2.
- E21 [SOP to-be] [Lõi] P/L Jobsheet: mỗi JobID có bảng khoản mục, chi phí, doanh thu, lãi gộp (doanh thu trừ chi phí) hoặc lỗ; gồm chi phí trực tiếp, mua ngoài, định mức, hoa hồng; chi phí trả hộ ghi từ Quy trình quản lý quỹ và thanh toán. Mẫu khoản mục chờ Delta (OQ-5). Nguồn: Đính kèm 05 mục 2.1.6, phụ lục 4.5; Phần mềm Delta 3.0 mục 3.1.3.
**Nhóm H — khai thuê hải quan (Kết nối API với Ecus, 26/10/2025)**
- H1 [SOP to-be] [Gói: Khai thuê hải quan] Trên JobID hải quan, CS khai tờ khai nháp ngay trên phần mềm: tờ khai xuất, tờ khai nhập, tờ khai sửa AMA. Danh mục chuẩn VNACCS/VCIS chọn sẵn. Tờ khai đính kèm các chứng từ đã có trên JobID (Hợp đồng, Invoice, Packing List…), không phải tải lại. Không gồm: nguyên phụ liệu, thanh khoản, kiểm tra sau thông quan.
- H2 [SOP to-be] [Gói: Khai thuê hải quan] [Cấu hình] Mỗi khách khai thuê chọn 1 trong 3 cách truyền tờ khai: (a) khai trên phần mềm khai hải quan của doanh nghiệp (Delta: Ecus Delta, dữ liệu riêng từng điểm khai); (b) khai trên phần mềm của khách có công cụ đồng bộ (EcusAuto); (c) khai trên phần mềm của khách không đồng bộ: phần mềm xuất file XML, nhân viên đưa lên bằng tay qua Ultraview.
- H3 [SOP to-be] [Gói: Khai thuê hải quan] Với cách (a) và (b): phần mềm đẩy tờ khai nháp kèm chứng từ sang phần mềm khai hải quan; nhân viên đăng nhập phần mềm đó để khai chính thức.
- H4 [SOP to-be] [Gói: Khai thuê hải quan] Phần mềm nhận về: số tiếp nhận của từng chứng từ đã tải lên (để kiểm hồ sơ đủ); trạng thái tờ khai (Đã truyền · Đã phân luồng · Có thông báo thuế với hàng nhập có thuế · Đã thông quan); số và ngày tờ khai; mã vạch lô hàng hoặc container. Sau khi khai chính thức thì đồng bộ lại toàn bộ dữ liệu và chứng từ để khớp với hải quan (bổ sung chứng từ JobID: A10).
- H5 [SOP+] [Gói: Khai thuê hải quan] Cách (c) không nhận được dữ liệu về: nhân viên nhập tay số tờ khai, phân luồng, thông quan, hoặc quét QR tờ khai (`shipment-coordination` A2). JobID gắn cờ "Tờ khai ngoài kết nối".

### P1 — should have

Làm trong giai đoạn 1, có cách làm tay tạm hoặc phụ thuộc feature khác (DEC-229):
- DP-01 duyệt tự động theo hạn mức — cần số liệu nợ từ `debt-management`.
- B7 giao dịch nội bộ · B14 JobID không doanh thu · D9 mã vạch gốc air · D11 tiền tệ CBT.
- E9 hoá đơn trả hộ khách không xác nhận (chờ OQ-6) · E15 hoá đơn vô chủ · E19 chi phí CBT trả nhà cung cấp · E20 hoa hồng · E21 P/L Jobsheet (mẫu chờ OQ-5).
- A9 hoá đơn điện tử qua MISA (chờ OQ-23).

### P2 — nice to have

Chờ khách hoặc gói bán riêng (DEC-229):
- A10, H1–H5 khai thuê hải quan và kết nối Ecus (Gói Khai thuê hải quan; chờ OQ-45, OQ-46).

## 5. Core Flows (Happy Path)

### 5.1 Luồng tổng (xương sống chung của 3 feature)

0. **Tạo và duyệt JobID** (feature này) — chứng từ khách vào qua kênh nhận hoặc tải lên; phần mềm đọc, tạo JobID nháp; CS hoặc điều vận kiểm, chọn loại JobID, báo giá, khai phạm vi dịch vụ, nhu cầu mua ngoài, xác nhận thông tin viết hoá đơn trả hộ, chuyển duyệt. Không đạt điều kiện nợ quá hạn, hạn mức thì dừng, chờ khách thanh toán hoặc gia hạn nợ được duyệt. Duyệt xong thì ghi số container thực nhận. JobID không có thủ tục giao nhận (CBT, đường sắt, không làm hiện trường) đi thẳng sang lập Lệnh; JobID không có vận tải đi thẳng sang ghi doanh thu. Tạo JobID trái tuyến thì phần mềm tự ghi giao dịch nội bộ (B7).
1–4. **Điều phối** (`shipment-coordination`) — nhận JobID, hoàn thiện dữ liệu và phân luồng, giao việc hiện trường, sinh YCVT.
5–7. **Điều vận** (`transport-dispatch`) — lập Lệnh, chạy Lệnh, chốt và duyệt Lệnh; duyệt xong chi phí lên JobID.
8. **Hoàn thành dịch vụ** (feature này) — CS ghi doanh thu và chuyển duyệt, giao chứng từ gốc; doanh thu được duyệt thì JobID hoàn thành, ghi doanh thu, chi phí vào kỳ báo cáo.

Ký hiệu: `[Vai trò]` người làm · `(PM)` phần mềm tự làm · `<…?>` điểm rẽ nhánh.

```
0. TẠO JOBID
[Khách] Gửi chứng từ (Zalo OA, Telegram, WeChat, Gmail) / [CS, Điều vận] tải lên
   |
   v
(PM) Đọc chứng từ, nhận ra khách? --Không--> hàng đợi tra soát thủ công (không tạo JobID)
   | Có                              (đọc lỗi / loại không có chứng từ -> [CS] tạo thủ công)
   v
(PM) Tạo JobID NHÁP: gán DK05, báo giá/hợp đồng, kiểm số container
   |
   v
[CS/Điều vận] Kiểm, sửa (chỗ sửa lưu lại); chọn loại JobID; khai phạm vi + mua ngoài;
              xác nhận thông tin viết hoá đơn trả hộ --Khác DK05--> [Cán bộ quản lý] duyệt
   |
   v  chuyển duyệt
<Đạt hạn mức, không nợ quá hạn?> --Không--> DỪNG, chờ khách thanh toán
   | Có                                     hoặc [CS/Sales] xin gia hạn nợ -> [CBQL] -> [BGĐ] duyệt
   v                                        (khách trả xong / gia hạn duyệt -> đi tiếp)
[Người tạo] Ghi số container thực nhận (nếu ít hơn chứng từ)
(PM) Tạo JobID trái tuyến? --Có--> tự ghi giao dịch nội bộ (B7)
   |
   v
<Có vận tải? Có thủ tục giao nhận tại cảng / kho / sân bay?>
   | Có giao nhận            | Có vận tải, không giao nhận       | Không có vận tải
   v                         v (CBT, đường sắt, không hiện trường) v
ĐIỀU PHỐI (bước 1-4)       ĐIỀU VẬN: sinh YCVT, lập Lệnh (bước 5)  [CS] Ghi chi phí mua ngoài (nếu có)
   |                         |                                    |
   +--> ĐIỀU VẬN (5-7) <-----+                                    |
             |                                                    |
             v  (PM) Lệnh duyệt xong: chi phí trên Lệnh chuyển lên JobID
8. HOÀN THÀNH DỊCH VỤ  <------------------------------------------+
[CS] Ghi doanh thu (theo danh sách phạm vi), chuyển duyệt; đổi bên xuất hoá đơn (CBT, D10);
     giao chứng từ gốc nếu JobID có đánh dấu (D9)
[Cán bộ quản lý] Duyệt doanh thu (Quy trình quản lý nợ phải thu, debt-management)
<Mọi Lệnh đã duyệt, doanh thu đã duyệt?> --Không--> chỉ ra phần thiếu
   | Có
   v
(PM) JobID "Hoàn thành dịch vụ" --> ghi doanh thu, chi phí vào kỳ báo cáo chứa ngày này (E18)
(PM) Đường sắt --> tự vào bảng kê kỳ `P-ky-chot-duong-sat` (xem Điều vận D7)
```

### 5.2 Thanh toán chi phí trên JobID

```
[CS / Lái xe / Hiện trường] Tạo Yêu cầu thanh toán gắn Lệnh hoặc JobID
(PM) Chưa kê khai đủ JobID --> khoá thanh toán (Điều phối, DP-03)
(PM) Khoản hải quan mà JobID không có hải quan trong phạm vi --> chặn (E13)
(PM) Cách trả mặc định: QR / tài khoản đối tác, trả từ tài khoản công ty (E2)
   +-- ghi dư nợ tạm ứng của nhân viên; hoá đơn về khớp giao dịch --> tự giảm
   +-- ngoại lệ trả tiền cá nhân: chỉ dưới `P-nguong-tam-ung`; duyệt ở debt-management
[Người tạo] Bắt chọn có / không hoá đơn
<Có hoá đơn?> --Có--> (PM) lấy hoá đơn điện tử từ MISA (A9) --Không khớp--> chụp, nhập tay, cờ "Chưa khớp hoá đơn điện tử"
             --Không--> định mức hải quan tự áp (E14); có công tác phí thì vào Quyết định phân công tháng (`fund-payments`)
(PM) Chi phí gắn đúng Lệnh / JobID; hiện trạng thái thanh toán
```

### 5.3 Loại JobID (Delta, `P-loai-jobid`)

Nguồn: Quy trình cung cấp dịch vụ tổng quát, mục 4.2.1, 4.9.1–4.9.2, 5.1.2.1; cột "Một JobID là" theo Quy trình quản lý quỹ và thanh toán, Đính kèm 05 mục 1.2.1.

| Mã | Loại | Một JobID là | Chứng từ định danh | Ai tạo | Hải quan + chuyên ngành |
|---|---|---|---|---|---|
| J01 | Hàng xuất nguyên container | Một Booking Note | Booking Note | CS | Có |
| J02 | Hàng xuất lẻ (gom container) | Một Booking Note | Booking Note | CS | Có |
| J03 | Hàng xuất hàng không | Một Booking Note | Booking Note | CS | Có |
| J04 | Hàng nhập nguyên container | Một vận đơn | Vận đơn + Giấy báo hàng đến | CS | Có |
| J05 | Hàng nhập lẻ | Một vận đơn | Vận đơn + Giấy báo hàng đến | CS | Có |
| J06 | Hàng nhập hàng không | Một vận đơn | Vận đơn + Giấy báo hàng đến | CS | Có |
| J07 | Hàng CBT | Một container | Biên bản giao nhận khi nhận hàng | CS hoặc điều vận | Có |
| J08 | Đóng hàng đường sắt | Một container | Kế hoạch chạy hàng của khách | Điều vận | Không |
| J09 | Trả hàng đường sắt | Một container | Kế hoạch chạy hàng của khách | Điều vận | Không |
| J10 | Vận tải gom hàng theo vòng (milkrun) | Một chuyến | Kế hoạch chạy hàng của khách | Điều vận | Không |
| J11 | Xe thuê bao (mỗi ngày một JobID, nhiều Lệnh) | Một ngày làm việc | Biên bản giao nhận | Điều vận | Không |
| J12 | Dịch vụ giá trị gia tăng | Chưa có định nghĩa | Không có (tạo thủ công) | CS | Không |

Mục giao nhận tại cảng theo loại: nâng container hàng và cược vỏ với J04; nâng container rỗng và chọn vỏ với J01.

## 6. System Behavior Deep Dive

### 6.1 Decision Points

| ID | Flow | Khi nào | YES (nhánh đồng ý) | NO (nhánh từ chối) |
|---|---|---|---|---|
| DP-01 | Tạo JobID | Không có nợ quá hạn (hoặc có gia hạn đã duyệt) và Hạn mức tín dụng > Nợ trong hạn + Chi phí dở dang | Đi tiếp | Dừng, chờ khách thanh toán hoặc gia hạn nợ |
| DP-02 | Tạo JobID | Có vận tải; có thủ tục giao nhận tại cảng/kho/sân bay | Vào Điều phối (bước 1) | Có vận tải, không giao nhận: thành YCVT, sang lập Lệnh (Điều vận). Không có vận tải: sang ghi doanh thu (B12) |
| DP-13 | Tạo JobID, giao việc | Người tạo JobID hoặc người nhận việc thuộc chi nhánh khác tuyến | Tự ghi giao dịch nội bộ, chia lãi gộp 50/50 sau khi chốt bảng kê | Không ghi |
| DP-20 | Tạo JobID | Thông tin viết hoá đơn trả hộ của lô khớp DK05 | Đi tiếp | CS nhập thông tin riêng, cán bộ quản lý duyệt (B11) |
| DP-21 | Kê chi phí | Khoản mua ngoài hải quan hoặc định mức hải quan trên JobID có hải quan trong phạm vi | Cho kê | Chặn, báo đổi phạm vi (E13) |

Cách tính DP-01 [Lõi] [Cấu hình] (Quy trình cung cấp dịch vụ tổng quát, mục 4.9.4–4.9.6):
- Nợ trong hạn: tổng các bảng kê lập ở Quy trình quản lý nợ phải thu không cần khách xác nhận, chưa tới hạn.
- Chi phí dở dang: doanh thu ghi ở Quy trình quản lý nợ phải thu trên mọi JobID trong kỳ báo cáo không cần khách xác nhận, cộng tổng chi phí trả hộ công ty đã chi.
- Khách có nợ quá hạn thì áp hạn mức ngay: bình quân (doanh thu dịch vụ + phí trả hộ) `P-so-thang-binh-quan-han-muc` (Delta: 6) tháng gần nhất × (1 + kỳ thanh toán tính theo tháng). Kỳ thanh toán ghi theo ngày hoặc tháng; quy đổi 1 tháng = 30 ngày.
- Mã DK05 không có hạn mức thì bỏ qua kiểm hạn mức. Số liệu nợ lấy từ `debt-management`; feature này chỉ dùng kết quả.

### 6.2 Scenario Matrix

Ai được đổi trạng thái gì, ở trạng thái nào.

| Đối tượng | Từ | Sang | Ai làm | Điều kiện | Kết quả |
|---|---|---|---|---|---|
| JobID | Nháp | Chờ duyệt | CS, điều vận | Đã kiểm trường đọc tự động, đủ loại JobID, phạm vi, thông tin viết hoá đơn | Chạy kiểm nợ, hạn mức |
| JobID | Chờ duyệt | Chờ xử lý | Phần mềm (hoặc người tạo, khi chưa có dữ liệu công nợ) | Đạt DP-01 | Vào danh sách của CS, bắt đầu đếm mốc |
| JobID | Chờ duyệt | Dừng - chờ khách thanh toán | Phần mềm | Không đạt | Báo CS |
| JobID | Dừng - chờ khách thanh toán | Chờ xử lý | Phần mềm | Khách thanh toán xong, hoặc gia hạn nợ được duyệt | Vào danh sách của CS |
| JobID | Nháp, Chờ xử lý | Huỷ | CS | Chưa phân luồng | Đóng JobID |
| JobID | Đã thực hiện Lệnh vận tải (hoặc Chờ xử lý với JobID không có vận tải) | Hoàn thành dịch vụ | CS | Mọi Lệnh đã duyệt; doanh thu đã duyệt | Ghi doanh thu, chi phí vào kỳ báo cáo |
| JobID | Hoàn thành dịch vụ | Đã xuất hoá đơn | Kế toán, phần mềm (`debt-management`) | Bảng kê phí dịch vụ đã chốt với khách, đã xuất hoá đơn (`debt-management`) | Ghi số hoá đơn lên JobID |
| JobID | Đã xuất hoá đơn | Đã đóng | Phần mềm (`debt-management`) | Đã chốt công nợ phải thu của JobID | Khoá JobID, không ghi thêm chi phí, doanh thu |
| Yêu cầu gia hạn nợ | Chờ duyệt bước 1 | Chờ duyệt bước 2 | Cán bộ quản lý | Đồng ý | Chuyển Ban giám đốc |
| Yêu cầu gia hạn nợ | Chờ duyệt bước 2 | Đã duyệt | Ban giám đốc | Đồng ý | JobID của khách được duyệt lại |
| Yêu cầu gia hạn nợ | Chờ duyệt bước 1, 2 | Từ chối | Cán bộ quản lý, Ban giám đốc | Không đồng ý | JobID giữ "Dừng" |
| Doanh thu dịch vụ | Nháp | Chờ duyệt | CS | Đã kê theo danh sách phạm vi | Sang cán bộ quản lý (debt-management) |
| Doanh thu dịch vụ | Chờ duyệt | Đã duyệt | Cán bộ quản lý | — | Cho JobID hoàn thành dịch vụ |
| Chứng từ gốc | Đang ở hiện trường | CS đã nhận | CS | — | Ghi người và giờ |
| Chứng từ gốc | CS đã nhận | Đã giao khách | CS | — | Gỡ cờ trên JobID |

### 6.3 State Transitions

**JobID** — SOP Điều phối có 3 trạng thái giữa; "Hoàn thành dịch vụ" theo Quy trình cung cấp dịch vụ tổng quát; "Nháp" theo Phân hệ APAS (17/10/2026) mục 2.2; "Đã xuất hoá đơn" và "Đã đóng" theo Quy trình quản lý quỹ và thanh toán, Đính kèm 05 mục 2.1.5 (DEC-228); "Chờ duyệt" và "Dừng - chờ khách thanh toán" là đề xuất đã chốt. "Đã tạo YCVT" do Điều phối (hoặc Điều vận với JobID không có thủ tục giao nhận) đổi; "Đã thực hiện Lệnh vận tải" do Điều vận đổi khi mọi Lệnh đã duyệt.

```
Nháp --> Chờ duyệt --Không đạt nợ, hạn mức--> Dừng - chờ khách thanh toán
            |                                     | khách thanh toán xong / gia hạn được duyệt
            v Đạt                                 v
         Chờ xử lý --> Đã tạo YCVT --> Đã thực hiện Lệnh vận tải --> Hoàn thành dịch vụ --> Đã xuất hoá đơn --> Đã đóng
            |                                                              ^
            +------------ không có vận tải (B12) --------------------------+
```

- Nháp: phần mềm vừa tạo từ chứng từ đọc tự động, hoặc người tạo đang nhập tay; chưa hiện với bộ phận khác. Chờ xử lý: CS đang hoàn thiện. Đã tạo YCVT: có ít nhất 1 YCVT. Đã thực hiện Lệnh vận tải: mọi Lệnh của JobID đã duyệt. Hoàn thành dịch vụ: doanh thu đã duyệt; doanh thu, chi phí ghi vào kỳ báo cáo. Đã xuất hoá đơn: bảng kê phí dịch vụ đã chốt với khách và đã xuất hoá đơn (`debt-management`). Đã đóng: đã chốt công nợ phải thu; JobID bị khoá, không ghi thêm chi phí, doanh thu.
- Huỷ chỉ khi còn "Nháp", "Chờ duyệt" hoặc "Chờ xử lý" mà chưa phân luồng. Sau mốc đó chỉ được sửa (đổi Booking Note, giảm số container — ở Điều phối). Ngoại lệ: khách cần thêm việc thì thêm "Việc phát sinh" có duyệt tới trước "Hoàn thành dịch vụ" (Điều phối B18, OQ-76). JobID không lên "Đã thực hiện Lệnh vận tải" khi chọn vỏ còn dở (Điều phối B16, OQ-75).
- Dừng vì công nợ chặn JobID, trừ khi có gia hạn nợ đã duyệt (B13); ở nguyên trạng thái tới khi khách trả hoặc gia hạn được duyệt, không tự huỷ.

**Chứng từ gốc phải chuyển (D9)**

```
Đang ở hiện trường --> CS đã nhận --> Đã giao khách
```

### 6.4 Interrupted Transactions

| # | Tình huống | Xử lý |
|---|---|---|
| 1 | Không đọc được chứng từ (ảnh mờ, mẫu lạ) | App chặn ảnh mờ trước khi gửi. Đọc lỗi thì chuyển sang nhập tay, ảnh hiện bên cạnh. Đánh dấu "nhập thủ công" để thống kê |
| 2 | Chứng từ không nhận ra khách | Vào hàng đợi tra soát thủ công, không tạo JobID (A11) |
| 3 | MISA chưa trả hoá đơn | Cờ "Chưa khớp hoá đơn điện tử", chụp và nhập tay (A9) |
| 4 | JobID dừng vì công nợ quá lâu | Ở nguyên "Dừng - chờ khách thanh toán", không tự huỷ. Nhắc CS sau bao lâu: OQ-42 |

### 6.5 Other Edge Cases

- CBT đổi bên xuất hoá đơn sau khi đã có Lệnh: đổi trên JobID, không huỷ Lệnh; bên thứ ba chưa có mã thì tạo việc "Đăng ký bên thanh toán" (D10).
- Hoàn thành dịch vụ khi còn Lệnh chưa duyệt hoặc doanh thu chưa duyệt: chặn, chỉ ra phần thiếu.
- JobID có đánh dấu cần chuyển mã vạch gốc mà chưa giao khách: cờ ở bước ghi nhận doanh thu (D9).
- Delta chỉ làm một phần số container trên chứng từ: người tạo ghi số container thực nhận; số YCVT theo số thực nhận (B10).
- Đổi phạm vi sau khi JobID đã vào Điều phối: không cho đổi (mốc chính xác: OQ-66).

## 7. Validation, Limits & Wording

### 7.1 Validation rules

Quy tắc chung (bắt buộc, độ dài, ngày, email, số điện thoại) theo GR và E-common, không viết lại.

| Field | Rule |
|---|---|
| Số container (khi tạo JobID) | 4 chữ cái + 7 số, đúng chữ số kiểm tra ISO 6346 |
| Số container thực nhận | Không lớn hơn số container trên Booking Note hoặc vận đơn |
| Phạm vi dịch vụ | Chỉ các mục loại JobID cho phép (Mục 5.3) |
| Cách trả chi phí | Bắt chọn có/không hoá đơn; tiền cá nhân chỉ dưới `P-nguong-tam-ung` |

### 7.2 Limits & Quotas (exact values)

| Tham số | Giá trị | Window | Behavior khi vượt |
|---|---|---|---|
| Hạn mức chi tiền mặt (`P-nguong-tam-ung`) | Delta: 5.000.000 ₫ | mỗi khoản | Từ ngưỡng trở lên không trả bằng tiền cá nhân |
| Chia lãi giao dịch nội bộ (`P-ty-le-chia-lai-noi-bo`) | Delta: 50/50 lãi gộp | mỗi JobID trái tuyến | Chỉ hạch toán sau khi chốt bảng kê công nợ phải thu, phải trả |
| Số tháng bình quân tính hạn mức (`P-so-thang-binh-quan-han-muc`) | Delta: 6 | mỗi khách có nợ quá hạn | Hạn mức tính lại theo công thức DP-01 |
| Gia hạn nợ tối đa (`P-so-ngay-gia-han-no-toi-da`) | Delta: chưa chốt (OQ-67) | mỗi yêu cầu | — |
| Kỳ báo cáo (`P-ky-bao-cao`) | Delta: tháng | — | — |

### 7.3 Wording samples (exact strings)

Ngôi "bạn", câu ngắn, không "Vui lòng" (theo design.md). Loại hiển thị theo GR-15: Inline dưới trường, Popup chặn giữa màn, Toast góc màn.

#### Error messages

| Mã | Loại | Tình huống | Câu |
|---|---|---|---|
| E-service-delivery-001 | Inline | Số container sai chữ số kiểm tra khi tạo JobID | "Số container không đúng. Kiểm tra lại chữ số cuối." |
| E-service-delivery-002 | Popup | Kê mua ngoài hoặc định mức hải quan trên JobID không có hải quan trong phạm vi | "JobID này không có thủ tục hải quan trong phạm vi. Đổi phạm vi trước nếu cần." |
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
- Trên JobID: loại JobID; chứng từ khách; số báo giá hoặc hợp đồng; phạm vi dịch vụ; nhu cầu mua ngoài; số container thực nhận; thoả thuận khác; thông tin viết hoá đơn trả hộ (và người duyệt nếu khác DK05); chi phí, doanh thu (kéo về từ Lệnh và việc hiện trường); giao dịch nội bộ (chi nhánh nào làm phần nào); hoá đơn trả hộ; bên xuất hoá đơn; cờ (chưa khớp hoá đơn điện tử, chưa có đơn giá, cần chuyển mã vạch gốc, hoá đơn trả hộ khách không xác nhận). Mốc, chứng từ vận hành và người giữ quyền thanh toán do Điều phối ghi.
- Yêu cầu gia hạn nợ: khách, hoá đơn hoặc bảng kê quá hạn, người tạo, người duyệt từng bước.
- Lịch sử: ai tạo, ai đổi trạng thái; chỗ AI đọc sai đã được người sửa; số lần phải nhập thủ công.

**Dịch vụ bên ngoài**

| Dịch vụ | Mục đích | Tình trạng |
|---|---|---|
| MISA | Lấy hoá đơn điện tử | Chưa rõ lấy được hoá đơn đầu vào (OQ-23) |
| AI đọc chứng từ (Google Document AI) | Đọc chứng từ khách khi tạo JobID | Trong phạm vi; hạn mức gọi theo ngày do IT khách cấu hình |
| Zalo OA, Telegram, WeChat, Gmail | Nhận chứng từ khách gửi | Trong phạm vi (A11) |
| Ngân hàng (API, QR) | Thanh toán trả hộ | Feature riêng |

**Thông báo**

| Ai nhận | Khi nào | Kênh |
|---|---|---|
| CS | JobID dừng vì công nợ; có việc "Đăng ký bên thanh toán"; JobID nháp mới từ chứng từ khách | Thông báo đẩy + "Việc của tôi" |
| Cán bộ quản lý | Thông tin viết hoá đơn khác DK05 chờ duyệt; yêu cầu gia hạn nợ bước 1 | Thông báo đẩy + "Việc của tôi" |
| Ban giám đốc | Yêu cầu gia hạn nợ bước 2 | Thông báo đẩy + "Việc của tôi" |

**Việc phần mềm tự chạy theo giờ:** kiểm lại JobID đang dừng khi khách thanh toán hoặc gia hạn được duyệt · nhắc CS JobID dừng quá lâu (OQ-42).

## 8. Assumptions

- SOP của Delta là thiết kế to-be của khách, không phải cách đang làm.
- Bảng kê, công nợ và kết nối MISA (ngoài lấy hoá đơn) là feature riêng; feature này chỉ đảm bảo doanh thu, chi phí đủ và đúng JobID.
- Phân hệ APAS (17/10/2026) thay bản "Giải pháp quản lý hoá đơn SIM" 12/10; yêu cầu thời gian xử lý, chặn đọc lặp và hạn mức gọi AI theo ngày của bản cũ không còn ở bản mới nên không ghi.

## 9. Risks

| Rủi ro | Khả năng | Hậu quả nghiệp vụ | Cách phòng |
|--------|----------|-------------------|-----------|
| AI đọc sai chứng từ khi tạo JobID (số container, tên kho) | thỉnh thoảng | Đi nhầm kho; dữ liệu sai lan sang Điều phối, Điều vận | JobID nháp, người tạo bắt buộc kiểm; kiểm chữ số container |
| Thiếu tài liệu khách: phụ lục bảng kê doanh thu, chi phí; quy trình quản lý quỹ và thanh toán | thường | Ghi nhận chi phí, doanh thu sai cấu trúc bảng kê | Bám OQ-5, OQ-7 |
| Chưa lấy được hoá đơn đầu vào từ MISA | thỉnh thoảng | Nhập tay hoá đơn nhiều, dễ sai | Cờ "Chưa khớp hoá đơn điện tử" (A9); chờ OQ-23 |

## 10. Success Criteria (preliminary)

Mỗi tiêu chí gắn một vấn đề ban đầu. Mục tiêu nội bộ tự đặt, đo sau 3 tháng chạy thật (DEC-229); số hiện trạng để so chờ khách (OQ-44).

| Vấn đề | Tiêu chí | Mục tiêu |
|---|---|---|
| a. Nhập lại nhiều lần | Trường định danh tự điền đúng, người tạo không phải sửa | ≥ 90% |
| a. Nhập lại nhiều lần | JobID phải tạo tay vì đọc lỗi | ≤ 10% |
| a. Nhập lại nhiều lần | Thời gian từ nhận chứng từ đến JobID chờ duyệt | ≤ 5 phút |
| e. Chi phí thiếu | JobID lập bảng kê lần đầu không bị chặn vì thiếu chi phí, doanh thu (E17) | ≥ 95% |
| e. Chi phí thiếu | Khoản chi gắn đúng JobID hoặc Lệnh khi ghi nhận | 100% |
| e. Chi phí thiếu | JobID từ "Hoàn thành dịch vụ" tới "Đã xuất hoá đơn" trong kỳ báo cáo chứa ngày hoàn thành | 100% |

## 11. Open Questions

Nguồn khách: tên tài liệu khách gửi và mục. Cột Trả lời theo biên bản [[docs/meetings/2026-10-10-oq-dispatch-coordination.md|Delta trả lời vòng 1]] (anh Nghĩa, 10/10/2026) và 2 điểm xác nhận lại ngày 12/10/2026.

| Mã | Câu hỏi | Nguồn khách | Trả lời |
|---|---|---|---|
| OQ-4 | Cách phân chia lợi nhuận nội bộ giữa các chi nhánh chưa chốt | Quy trình cung cấp dịch vụ tổng quát | Đã chốt: chia theo lãi gộp 50/50, sau khi chốt bảng kê công nợ phải thu, phải trả (B7) |
| OQ-5 | Phụ lục bảng kê doanh thu, chi phí còn trống | Quy trình cung cấp dịch vụ tổng quát, phụ lục | Còn mở: Delta gửi dần phụ lục |
| OQ-6 | Chưa có cách xử lý bồi thường nội bộ khi khách từ chối trả hộ do lỗi nhân viên | Quy trình cung cấp dịch vụ tổng quát, mục 5.3–5.5 | Một phần: khi lập bảng kê, phần mềm đánh dấu hoá đơn trả hộ khách không xác nhận thanh toán (E9). Quy trình xử lý Delta sẽ phát triển |
| OQ-7 | Quy trình quản lý quỹ và thanh toán chưa phát triển | Quy trình cung cấp dịch vụ tổng quát | Còn mở: Delta đang hoàn thiện |
| OQ-9 | Định danh JobID đường sắt thế nào? | Giao nhận hàng hoá (18/9/2026) | Một phần: SOP tổng quát mục 4.2.1 có J08 Đóng hàng đường sắt, J09 Trả hàng đường sắt, định danh theo kế hoạch chạy hàng của khách (Mục 5.3). Còn mở: số JobID ghi thế nào |
| OQ-11 | Lệch báo cáo quản trị và báo cáo thuế ở hàng CBT, cần kế toán xác nhận | Giao nhận hàng hoá (18/9/2026) | Đã chốt: chấp nhận lệch về hình thức; báo cáo quản trị phản ánh đúng thực tế giao dịch |
| OQ-16 | JobID có được chia sẻ hoặc chuyển sang chi nhánh khác không, thao tác ra sao? | Quy trình cung cấp dịch vụ tổng quát, mục 5.5 | Đã chốt: theo 2 trường hợp giao dịch nội bộ trong SOP; JobID trái tuyến hoặc giao việc trái tuyến thì phần mềm tự ghi nhận, tự hạch toán (B7) |
| OQ-17 | Quy mô: JobID mỗi ngày, số lái xe, nhân viên hiện trường, CS, điều vận theo chi nhánh | Chưa có trong tài liệu khách gửi | Một phần: ~110.000 lô hàng/năm (= số Lệnh vận tải), ~50.000 tờ khai/năm (= số JobID J01–J06), tăng 2 con số mỗi năm. Chi nhánh Hà Nội, Vận Tải (VT), Bắc Ninh (BN), Hải Dương (HD, sẽ giải thể do sáp nhập tỉnh) gấp 3–4 lần TP.HCM về sản lượng, doanh thu; không có chi nhánh Hải Phòng. Còn thiếu: số người theo chi nhánh |
| OQ-23 | Gói MISA có lấy đủ hoá đơn đầu vào không? Hoá đơn trả hộ ghi mã số thuế của ai? | Quy trình cung cấp dịch vụ tổng quát | Còn mở: Delta đánh giá cao hướng lấy hoá đơn từ MISA, đang xem xét |
| OQ-29 | Lưu bằng chứng khách đồng ý khoản chi ngoài định mức bằng cách nào: khách bấm trên app, ảnh tin nhắn/email, link xác nhận, hay ghi chú đã gọi? | Giao nhận hàng hoá (18/9/2026) | Ngoài phần mềm: ghi nhận, chi trả qua Quy trình cung cấp dịch vụ hoặc thanh toán không hoá đơn (E1) |
| OQ-31 | Bảng loại phí × địa điểm → cách hạch toán (thu nhập chịu thuế lái xe / chi hộ / trả hộ / chi phí vận hành) cho các tuyến ngoài đường sắt | Giao nhận hàng hoá (18/9/2026) | Còn mở: Delta làm rõ luồng dữ liệu Cung cấp dịch vụ, Điều phối, Điều vận và bút toán đối ứng |
| OQ-36 | Ai duyệt mã khách DK05 cấp 2 khi CBT đổi pháp nhân thanh toán sang bên mới? | Giao nhận hàng hoá (18/9/2026) | Chưa hỏi Delta (ngoài deck vòng 1) |
| OQ-42 | JobID dừng vì nợ quá hạn, vượt hạn mức có cần nhắc CS sau một số ngày không? Bao nhiêu ngày, nhắc ai? | Chưa có trong tài liệu khách gửi | Chưa hỏi Delta (ngoài deck vòng 1) |
| OQ-44 | Số hiện trạng cho các tiêu chí thành công của 3 feature (để so với mục tiêu): tỉ lệ trường tự điền; tỉ lệ việc hiện trường giao, nhận trên app; số lần và tiền phạt lưu container, lưu vỏ, lưu xe mỗi tháng; thời gian từ xe xong việc tới duyệt Lệnh; tỉ lệ Lệnh duyệt đủ chi phí | Chưa có trong tài liệu khách gửi | Một phần: mục tiêu service-delivery đã chốt nội bộ (Mục 10, DEC-229); còn xin số hiện trạng |
| OQ-45 | Tài liệu Ecus ghi khai tập trung ở Hà Nội, Hải Phòng, TP.HCM, sơ đồ có 3 kho dữ liệu Ecus HN, HCM, VT; OQ-17 ghi "không có chi nhánh Hải Phòng". VT (Vận tải Delta) có phải điểm khai Hải Phòng không? JobID hải quan gắn chi nhánh nào? | Kết nối API với Ecus (26/10/2025), mục 1, mục 2.1, sơ đồ mục 3.1 | Còn mở: chưa hỏi Delta |
| OQ-46 | Tài liệu từ 10/2025: Delta đã làm việc với bên cung cấp Ecus chưa? Trong 137 khách, bao nhiêu khách thuộc nhóm 2, và bao nhiêu khách chọn EcusAuto hay làm tay? | Kết nối API với Ecus (26/10/2025), mục 2.2, 3.2 | Còn mở: chưa hỏi Delta |
| OQ-66 | Phạm vi dịch vụ đổi được tới mốc nào? SOP ghi 2 kiểu: JobID tạo bằng quét chứng từ đổi được "trước khi thực hiện quy trình điều phối"; JobID tạo thủ công đổi được "tại một bước trong toàn bộ quy trình" — bước nào? JobID không qua Điều phối (CBT, đường sắt, không có vận tải) thì khoá phạm vi ở mốc nào? | Quy trình cung cấp dịch vụ tổng quát (24/9/2026), mục 5.1.2.1, 5.1.2.4 | Còn mở: đề xuất một quy tắc chung, đổi được tới trước khi vào Điều phối (B9) |
| OQ-67 | Một lần gia hạn nợ quá hạn được tối đa bao nhiêu ngày? Có giới hạn số lần gia hạn cho một hoá đơn, bảng kê không? | Quy trình cung cấp dịch vụ tổng quát (24/9/2026), mục 4.9.4 Nợ quá hạn | Còn mở: chưa hỏi Delta (B13) |
| OQ-68 | "Dư nợ tạm ứng 2" là gì: tài khoản tạm ứng riêng cho khoản chi qua ngân hàng, khác tạm ứng tiền mặt? Ngưỡng 5 triệu đồng (hạn mức chi tiền mặt) có còn là ngưỡng cho nhân viên trả bằng tiền cá nhân không? | Phân hệ APAS (17/10/2026), mục 3.3.2 Bước 4; Quy trình cung cấp dịch vụ tổng quát, mục 4.6 | Còn mở: chưa hỏi Delta (E2) |
| OQ-69 | Bảng mã JobID lệch giữa các tài liệu: SOP tổng quát (24/9) ghi J07 hàng CBT, J12 dịch vụ giá trị gia tăng; Đính kèm 05 (26/7) mục 2.1.4 ghi ngược lại (J07 giá trị gia tăng, J12 CBT); phụ lục 4.1 cùng tài liệu lại xếp J08 milkrun, J09 xe thuê bao, J10–J11 đường sắt. Bảng của SOP tổng quát 24/9 có phải bảng chuẩn? | Quy trình cung cấp dịch vụ tổng quát (24/9/2026), mục 4.2.1; Quy trình quản lý quỹ và thanh toán, Đính kèm 05 Job ID (26/7/2026), mục 2.1.4 và phụ lục 4.1 | Còn mở: brainstorm ghi theo SOP tổng quát 24/9 (bản mới hơn) |
| OQ-70 | Phần mềm Delta 3.0 đưa cước quốc tế (đường biển, hàng không) và cho thuê kho vào phạm vi phân hệ nghiệp vụ, nhưng bảng 12 loại JobID chưa có loại nào cho 2 dịch vụ này. Cước quốc tế dùng loại JobID nào, chứng từ định danh gì? Cho thuê kho có tạo JobID trên hệ thống hay chỉ nhận bảng kê phí từ phần mềm quản lý kho? | Phần mềm Delta 3.0 — Thiết kế kiến trúc và lộ trình (16/10/2026), mục 3.1.3 Nghiệp vụ | Còn mở: chưa hỏi Delta |

## 12. Next Steps

Đã tách từ brainstorm Điều phối gộp ngày 2026-10-12. Tiếp theo:
- Hỏi lại Delta các câu còn mở ở Mục 11 (BL-041)
- `/user-flow service-delivery` — chạy lại; userflow tách máy từ bản nháp ngày 07/10, còn nội dung cũ
- `/srs service-delivery` — đặc tả FR, BR, Error Matrix
