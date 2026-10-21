---
type: meeting-deck
meeting: open-questions
delivery: async
density: compact
title: Câu hỏi cần xác nhận — vòng 3
client: Delta
date: 2026-10-21
reply_to: Tín Phan (tinpb.work@gmail.com)
footer: Câu hỏi cần xác nhận — vòng 3
brand: innvie-v1
status: draft
updated: 2026-10-21
links:
  - docs/transport-dispatch/brainstorms/transport-dispatch.md
  - docs/shipment-coordination/brainstorms/shipment-coordination.md
  - docs/service-delivery/brainstorms/service-delivery.md
  - docs/vehicle-telematics/brainstorms/vehicle-telematics.md
  - docs/vehicle-management/brainstorms/vehicle-management.md
  - docs/meetings/2026-10-21-oq-vis.md
  - docs/meetings/2026-10-10-oq-dispatch-coordination.md
  - docs-input/sop/giao-nhan-hang-hoa/giao-nhan-hang-hoa.md
  - docs-input/sop/sop-dieu-phoi.md
  - docs-input/sop/sop-cung-cap-dich-vu-tong-quat.md
  - docs-input/sop/apas-thanh-toan-doi-soat/apas-thanh-toan-doi-soat.md
  - docs-input/sop/delta-3-0-master-plan/delta-3-0-master-plan.md
  - docs-input/tich-hop/camera-ai-quay-cat-de-xuat-2026-08-11/camera-ai-quay-cat-de-xuat-2026-08-11.md
  - docs-input/tich-hop/gps-tien-ich-de-xuat-2025-09-25/gps-tien-ich-de-xuat-2025-09-25.md
  - docs-input/tich-hop/vetc-api-cong-van-2026-09-02/vetc-api-cong-van-2026-09-02.md
  - docs-input/tich-hop/ecus-api-yeu-cau-2025-10-26/ecus-api-yeu-cau-2025-10-26.md
  - docs-input/du-lieu-mau/thong-ke-chi-phi-chung-tu-cbt.md
---

<!-- layout: title -->
# Câu hỏi cần xác nhận — vòng 3
41 nội dung nhờ Delta trả lời để hoàn thiện Lệnh vận tải, quay cắt, dữ liệu xe, Điều phối hiện trường và Cung cấp dịch vụ

::: notes
- Bản gửi khách tự trả lời (async, compact) — ghi chú KHÔNG có trong file HTML gửi đi.
- Phạm vi: mọi OQ "Chưa hỏi Delta" (nội bộ) trên dashboard 21/10, trừ cross-process-flow. 39 câu − td OQ-46 (user trả lời 21/10: có) − vt OQ-19 (đã trả lời qua deck VIS 21/10) = 37 câu; tách 4 câu hai ý (td-65, vm-4, sd-68, sd-70) → 41 slide.
- id tiền tố feature: td transport-dispatch · sc shipment-coordination · sd service-delivery · vt vehicle-telematics · vm vehicle-management.
- Đã so với 3 deck trước (06/10 ×2, 15/10): không trùng nguyên câu; td-60, vt-16, sc-48 có bối cảnh nhắc câu đã hỏi.
:::

---

<!-- layout: goal -->
## Vì sao cần anh/chị trả lời
- **41 câu hỏi** còn treo sau các buổi trao đổi và các tài liệu Delta gửi gần đây, đang chặn phần thiết kế chi tiết
- Mỗi câu có bối cảnh và câu trích từ tài liệu Delta (Giao nhận hàng hoá, Quy trình điều phối, Quy trình cung cấp dịch vụ, APAS, Delta 3.0, Camera AI, công văn VETC…) để tiện đọc lại
- Một số câu đã có đề xuất của đội, chỉ cần Delta xác nhận hoặc sửa
- Mất khoảng 90–100 phút; có thể làm nhiều lần, câu trả lời tự lưu
- Câu chưa rõ hoặc cần hỏi bộ phận khác: bấm **Cần trao đổi thêm**

---

<!-- layout: agenda -->
## Nội dung
1. **Lệnh vận tải** — hàng lạnh, đường sắt, thông báo khách, chi phí CBT, trạm thu phí, duyệt và khiếu nại (10 câu)
2. **Quay cắt** — cách tính lượt, đơn giá, phân công (3 câu)
3. **Dữ liệu xe, hồ sơ xe** — thiết bị GPS mooc và máy phát, VETC, máy phát, danh mục xe (8 câu)
4. **Điều phối hiện trường** — ePort, giao việc, chọn vỏ, việc phát sinh, hoá đơn, lô hàng (11 câu)
5. **Cung cấp dịch vụ, công nợ** — mã khách cấp 2, nợ quá hạn, tạm ứng, Ecus, dịch vụ mới (9 câu)

---

<!-- layout: section -->
## Lệnh vận tải

---

<!-- layout: oq; id: td-OQ-35; src: docs/transport-dispatch/brainstorms/transport-dispatch.md; group: Lệnh vận tải -->
## Kế hoạch chạy hàng ngày của Ratraco có mẫu cố định không? Nhờ gửi giúp một mẫu thật

> Ratraco gửi kế hoạch chạy hàng ngày n vào ngày n-1; từ đó điều vận lập Lệnh cho từng lô. Đội thiết kế cho điều vận nhập file kế hoạch để phần mềm sinh Lệnh hàng loạt, thay vì lập từng Lệnh. Muốn đọc tự động được thì cần biết file có mẫu cố định không (Excel, PDF, tin nhắn) và các cột gồm gì.

**Tài liệu:** Giao nhận hàng hoá (18/9/2026), mục 3.5 Hàng đường sắt Ratraco
**Trích dẫn:** "Kế hoạch chạy hàng ngày n sẽ được Ratraco thông báo cho Delta ở ngày n-1. Từ kế hoạch chạy hàng này, nhân viên điều vận của Delta sẽ lập Lệnh kế hoạch" — Giao nhận hàng hoá, mục 3.5

**Cách trả lời:** ghi dạng file và cách Ratraco gửi; gửi kèm một file mẫu (đã che thông tin nhạy cảm nếu cần) qua email người nhận câu trả lời
**Ảnh hưởng:** nhập kế hoạch Ratraco và sinh Lệnh hàng loạt cho hàng đường sắt

::: notes
- Nguồn: transport-dispatch OQ-35, ý D6. GNHH dòng 875.
:::

---

<!-- layout: oq; id: td-OQ-37; src: docs/transport-dispatch/brainstorms/transport-dispatch.md; group: Lệnh vận tải -->
## Lái xe chỉnh nhiệt độ theo yêu cầu của khách hàng có bắt buộc chụp ảnh làm bằng chứng không?

> Yêu cầu chỉnh nhiệt độ, cửa gió đến từ khách hàng hoặc đại lý, qua điều vận tới lái xe. SOP ghi mọi yêu cầu chỉnh phải lưu bằng hình ảnh. Đội đang thiết kế: yêu cầu vẫn nhắn qua kênh hiện nay, lái xe bấm "Đã chỉnh" trên Lệnh kèm lý do, không bắt chụp ảnh. Cần Delta chọn mức chặt.

**Tài liệu:** Giao nhận hàng hoá (18/9/2026), mục 3.4.3.2 Vận chuyển
**Trích dẫn:** "Mọi yêu cầu điều chỉnh nhiệt độ bắt buộc phải được ghi nhận lại bằng hình ảnh giao dịch cụ thể & được lưu lại làm bằng chứng đối chiếu khi cần thiết." — Giao nhận hàng hoá, mục 3.4.3.2

### A. Bắt buộc chụp ảnh như SOP
Không có ảnh thì không ghi nhận được lần chỉnh
+ Có bằng chứng khi khách hàng khiếu nại hàng hỏng
- Lái xe thêm thao tác, khó làm khi đang chạy

### B. Bấm "Đã chỉnh" kèm lý do, ảnh tuỳ chọn
+ Nhanh cho lái xe
- Bằng chứng yếu hơn khi có tranh chấp

**Ảnh hưởng:** nhật ký nhiệt độ hàng lạnh trên app lái xe

::: notes
- Nguồn: transport-dispatch OQ-37, ý D2 (đang ghi "không bắt ảnh"). GNHH dòng 757. Không đề xuất: SOP và thiết kế ngược nhau, để Delta chọn.
:::

---

<!-- layout: oq; id: td-OQ-43; src: docs/transport-dispatch/brainstorms/transport-dispatch.md; group: Lệnh vận tải -->
## Phần mềm nhắc lái xe ghi nhiệt độ bao lâu một lần, cho từng loại hàng lạnh?

> Phần mềm sẽ nhắc lái xe ghi nhiệt độ theo chu kỳ, quá giờ chưa ghi thì báo điều vận; điều vận chỉnh được chu kỳ trên từng Lệnh. SOP có hai mức: hàng sầu riêng 3–4 giờ một lần, mục khác ghi ít nhất 3–4 lần một ngày. Cần chu kỳ mặc định cho từng loại hàng Delta đang chở.

**Tài liệu:** Giao nhận hàng hoá (18/9/2026), mục 3.4.3.2 và 3.4.4.2 Vận chuyển
**Trích dẫn:** "Việc cập nhật nhiệt độ được thực hiện ít nhất 3-4 lần/ngày" — Giao nhận hàng hoá, mục 3.4.3.2
**Trích dẫn:** "Sau khi xuất phát, lái xe phải cập nhật nhiệt độ 3-4 giờ/lần" — Giao nhận hàng hoá, mục 3.4.4.2

**Cách trả lời:** mỗi loại hàng một dòng, vd "Sầu riêng: 3 giờ · Hàng đông lạnh: 6 giờ"
**Ảnh hưởng:** nhắc ghi nhiệt độ trên app lái xe, cảnh báo cho điều vận

::: notes
- Nguồn: transport-dispatch OQ-43, ý D2, tham số P-chu-ky-nhac-nhiet.
:::

---

<!-- layout: oq; id: td-OQ-38; src: docs/transport-dispatch/brainstorms/transport-dispatch.md; group: Lệnh vận tải -->
## Khách hàng của Delta có cần nhận thông báo tự động ở mốc nào của chuyến hàng không?

> Phần mềm đã ghi được các mốc của Lệnh nhờ GPS và thao tác của lái xe. Có thể gửi thông báo cho khách hàng (email hoặc tin nhắn) ở một số mốc, ví dụ: xe đã đến điểm nhận, đã nhận hàng, đã giao xong, xe trễ so với giờ hẹn. Tài liệu Delta chưa nói tới việc này.

**Tài liệu:** chưa có trong tài liệu Delta gửi

**Cách trả lời:** ghi các mốc cần gửi; khách hàng nào cần (mọi khách hay chỉ một số khách); hoặc ghi "không cần"
**Ảnh hưởng:** thông báo cho khách hàng của Delta

::: notes
- Nguồn: transport-dispatch OQ-38 (Mục 7 bảng thông báo: "Khách | Các mốc giao nhận khác | Chờ OQ-38").
:::

---

<!-- layout: oq; id: td-OQ-65.1; src: docs/transport-dispatch/brainstorms/transport-dispatch.md; group: Lệnh vận tải -->
## Chi phí ở cửa khẩu Trung Quốc lái xe trả bằng tiền gì?

> Bảng chi phí CBT liệt kê các khoản lái xe trả ở cửa khẩu Trung Quốc (bàn cân, bãi kiểm hoá, bãi cắm điện, dẫn xe…) và ghi số tiền bằng đồng. Lái xe kê các khoản này trên Lệnh. Nếu thực tế lái xe trả bằng nhân dân tệ thì phần mềm cần ghi tiền gốc và quy đổi.

**Tài liệu:** Thống kê chi phí chứng từ CBT (03/9/2026), nhóm II.b Chi phí tại cửa khẩu Trung Quốc / Campuchia

### A. Nhân dân tệ
Phần mềm ghi tiền gốc và quy đổi ra đồng
+ Đúng số lái xe thực trả
- Cần quy tắc tỷ giá

### B. Tiền đồng
+ Đơn giản, như bảng chi phí hiện nay
- Lệch nếu lái xe đổi tiền theo giá khác

### C. Cả hai, tuỳ khoản

**Nếu chọn A hoặc C:** ghi ở Ý kiến thêm tỷ giá lấy theo đâu (ngân hàng nào, ngày lái xe chi hay ngày duyệt Lệnh)
**Ảnh hưởng:** kê chi phí CBT trên Lệnh, bảng kê chi phí lái xe

::: notes
- Nguồn: transport-dispatch OQ-65 (ý 1), ý E11. Bảng CBT ghi số VND (vd bàn cân 200.000). Không đề xuất: câu hỏi sự thật.
:::

---

<!-- layout: oq; id: td-OQ-65.2; src: docs/transport-dispatch/brainstorms/transport-dispatch.md; group: Lệnh vận tải -->
## Phí bãi xe Viettel: khi nào lái xe trả, khi nào kế toán trả?

> Bảng chi phí CBT ghi phí bãi xe Viettel ở hai nhóm: nhóm Delta trả nhà cung cấp (sầu riêng Thái Lan) và nhóm ghi trên Lệnh trả cho lái xe (sầu riêng Việt Nam, hàng Campuchia). Cả hai chỗ đều ghi "thanh toán sau theo hợp đồng và hoá đơn của Viettel". Đội cần biết khoản này có lúc nào lái xe trả tại chỗ không, để không ghi hai lần.

**Tài liệu:** Thống kê chi phí chứng từ CBT (03/9/2026), nhóm I dòng 5 và nhóm II.a dòng 4 Phí bãi xe Viettel
**Trích dẫn:** "Đơn giá phí bãi 1 ngày, có thể kéo dài nhiều hơn 1 ngày. Thanh toán sau theo hợp đồng và hóa đơn của Viettel" — Thống kê chi phí chứng từ CBT

**Cách trả lời:** nêu trường hợp lái xe trả, trường hợp kế toán trả theo hoá đơn Viettel
**Ảnh hưởng:** danh mục chi phí CBT trên Lệnh, đối chiếu hoá đơn Viettel

::: notes
- Nguồn: transport-dispatch OQ-65 (ý 2), ý E11.
:::

---

<!-- layout: oq; id: td-OQ-58; src: docs/transport-dispatch/brainstorms/transport-dispatch.md; recommend: A; group: Lệnh vận tải -->
## Lái xe phải trả tiền mặt tại trạm thu phí: ghi nhận theo đề xuất dưới đây được không?

> Khi tài khoản giao thông hết tiền hoặc trạm không thu tự động được, lái xe phải trả tiền mặt. Lúc đó VETC không có giao dịch, phần mềm có thể hiểu nhầm là lái xe tránh trạm. Đội đề xuất: lái xe ghi khoản chi hộ trên Lệnh kèm tên trạm và ảnh biên lai; trạm đó tính là "Đã qua", không chờ giao dịch VETC.

**Tài liệu:** chưa có trong tài liệu Delta gửi

### A. Đồng ý cách làm trên
+ Lái xe không bị tính tránh trạm oan
+ Có biên lai làm chứng từ chi hộ
- Lái xe thêm một thao tác khi xảy ra

### B. Xử lý cách khác
Nhờ ghi cách Delta muốn ở Ý kiến thêm

**Nếu không có trường hợp này:** ghi "không xảy ra" ở Ý kiến thêm
**Ảnh hưởng:** vé cầu đường trên Lệnh, bảng kê tránh trạm
**Vì sao đề xuất A:** không có biên lai thì chỉ còn dữ liệu VETC, và khoản trả tiền mặt sẽ bị xếp thành tránh trạm

::: notes
- Nguồn: transport-dispatch OQ-58, review VIS r11 (19/10). Liên quan I7 (khớp vé từng trạm).
:::

---

<!-- layout: oq; id: td-OQ-59; src: docs/transport-dispatch/brainstorms/transport-dispatch.md; group: Lệnh vận tải -->
## Lệnh đã chạy xong mà chưa ai duyệt sau bao lâu thì phần mềm nhắc người duyệt và báo trưởng điều vận?

> Dầu chờ nhận, vé, bù dầu của lái xe chỉ chốt khi Lệnh được duyệt. Lệnh để lâu không duyệt thì các khoản của lái xe bị treo. Đội thiết kế: quá một số giờ sau khi Lệnh chạy xong thì nhắc người duyệt, đồng thời báo trưởng điều vận. Cần Delta cho số giờ.

**Tài liệu:** chưa có trong tài liệu Delta gửi

**Cách trả lời:** ghi số giờ, vd "24 giờ"; có khác giữa hàng nội địa và CBT không
**Ảnh hưởng:** nhắc duyệt Lệnh, dầu chờ nhận của lái xe

::: notes
- Nguồn: transport-dispatch OQ-59, ý I13, tham số P-han-duyet-lenh. Review VIS r9.
:::

---

<!-- layout: oq; id: td-OQ-60; src: docs/transport-dispatch/brainstorms/transport-dispatch.md; group: Lệnh vận tải -->
## Lái xe không đồng ý khoản bị tính vào lương: có cần luồng khiếu nại trên phần mềm không?

> Ngày 21/10 Delta trả lời câu "lái xe phản đối khi bị ghi vi phạm" là việc ngoài phạm vi phần mềm. Thiết kế hiện có một luồng khiếu nại cho các khoản tính vào lương: vé tránh trạm, đi ngoài cung đường, bù dầu bị giảm, dầu định mức. Lái xe khiếu nại trong hạn, khoản tạm rút khỏi bảng kê lương, người đã quyết định xem lại (Giữ, Huỷ, Sửa số), bị giữ thì được đề nghị trưởng bộ phận xem lại một lần. Cần Delta chốt giữ hay bỏ.

**Tài liệu:** chưa có trong tài liệu Delta gửi (trả lời của Delta ngày 21/10 cho bộ câu hỏi dữ liệu vận hành xe, câu Rủi ro ý 3)

### A. Bỏ, xử lý ngoài phần mềm
Lái xe phản ánh trực tiếp với điều vận như hiện nay
+ Phần mềm gọn hơn
- Không có dấu vết ai sửa khoản nào, vì sao

### B. Giữ luồng khiếu nại như mô tả
+ Lái xe thấy được kết quả, ít tranh cãi khi chốt lương
- Thêm việc xem lại cho người duyệt

**Nếu chọn B:** ghi ở Ý kiến thêm hạn khiếu nại bao nhiêu ngày, và quy chế có cho khiếu nại khoản của kỳ lương đã chốt không
**Ảnh hưởng:** màn "Số liệu của tôi" của lái xe, bảng kê lương

::: notes
- Nguồn: transport-dispatch OQ-60, ý I14, tham số P-han-khieu-nai. Biên bản docs/meetings/2026-10-21-oq-vis.md dòng 59: vt OQ-10 ý 3 "phản đối vi phạm ngoài phạm vi phần mềm" ⚠ mâu thuẫn I14. Không đề xuất (user chốt 21/10).
:::

---

<!-- layout: oq; id: td-OQ-64; src: docs/transport-dispatch/brainstorms/transport-dispatch.md; group: Lệnh vận tải -->
## Các mooc Delta để lại nhà máy (mô hình cắt mooc) đã gắn thiết bị GPS chưa?

> Thư đề xuất GPS năm 2025 có đề nghị lắp thiết bị GPS cho mooc. Nếu mooc có thiết bị, phần mềm tự ghi lượt quay cắt khi đầu kéo ghép rồi tách mooc trong nhà máy. Nếu chưa, lái xe quay cắt phải tự bấm "Quay cắt" trên app và chụp số container cho từng lượt, tới khi lắp xong.

**Tài liệu:** Đề xuất tiện ích GPS (25/9/2025), mục 2 Sơ mi-rơ mooc
**Trích dẫn:** "Lắp thiết bị GPS để quản lý mooc… Lập báo cáo chi tiết theo thời gian các đầu kéo đã sử dụng một mooc cụ thể." — Đề xuất tiện ích GPS, mục 2

### A. Đã gắn
Nhờ ghi số mooc đã gắn ở Ý kiến thêm
+ Lượt quay cắt tự ghi, lái xe không phải bấm

### B. Chưa gắn
Nhờ ghi dự kiến khi nào lắp ở Ý kiến thêm
- Mọi lượt quay cắt do lái xe bấm trên app

**Ảnh hưởng:** cách ghi lượt quay cắt, lương quay cắt của lái xe

::: notes
- Nguồn: transport-dispatch OQ-64, ý Q2, Q4. Câu cùng chủ đề vt OQ-17 (slide Dữ liệu xe) hỏi tổng số thiết bị.
:::

---

<!-- layout: section -->
## Quay cắt

---

<!-- layout: oq; id: td-OQ-61; src: docs/transport-dispatch/brainstorms/transport-dispatch.md; group: Quay cắt -->
## Một lượt quay cắt được tính thế nào?

> Lái xe quay cắt kéo container từ chỗ chờ vào cửa kho để đóng, dỡ hàng, rồi kéo ra chỗ chờ. Ngày 14/10 Delta bỏ phương án camera, nên phần mềm sẽ ghi lượt bằng GPS: đầu kéo ghép rồi tách khỏi một mooc trong vùng nhà máy. Cần biết một lượt để trả lương, cấp dầu là một chiều hay cả vào lẫn ra.

**Tài liệu:** Camera AI — đếm tự động số lần quay cắt (11/8/2026), mục 1 Vấn đề
**Trích dẫn:** "phải đưa container A từ địa điểm chờ vào cửa kho theo yêu cầu để đóng/dỡ hàng. Sau khi đóng/dỡ hàng hoàn tất thì phải đưa container A này ra khỏi cửa kho, vào vị trí chờ kéo đi" — Camera AI, mục 1

### A. Mỗi lần kéo vào hoặc kéo ra là một lượt
Một container thường có 2 lượt

### B. Kéo vào và kéo ra tính chung một lượt

**Xin thêm ở Ý kiến thêm:** chỉnh vị trí liên tiếp trong bao nhiêu phút thì gộp thành một lượt; mooc di chuyển dưới bao nhiêu mét thì không tính (móc thử)
**Ảnh hưởng:** đếm lượt quay cắt, lương và dầu theo lượt, bảng kê thu tiền đơn vị thuê

::: notes
- Nguồn: transport-dispatch OQ-61, ý Q2, Q6; tham số P-gop-luot-quay-cat, P-quang-toi-thieu-quay-cat. Không đề xuất.
:::

---

<!-- layout: oq; id: td-OQ-62; src: docs/transport-dispatch/brainstorms/transport-dispatch.md; group: Quay cắt -->
## Đơn giá lương và định mức dầu cho mỗi lượt quay cắt khác nhau theo những gì?

> Lái xe quay cắt hưởng lương và nhận dầu theo định mức cho mỗi lượt. Quay cắt cho đơn vị khác cùng làm ở nhà máy thì Delta có doanh thu. Đội cần biết bảng đơn giá chia theo gì để dựng danh mục.

**Tài liệu:** Camera AI — đếm tự động số lần quay cắt (11/8/2026), mục 1 Vấn đề và mục 3 Yêu cầu
**Trích dẫn:** "Lái xe quay cắt sẽ hưởng lương và nhận dầu diesel theo định mức cho mỗi lần quay cắt. Nếu việc quay cắt này là phục vụ cho một nhà cung cấp khác cùng làm việc tại nhà máy đó thì sẽ phát sinh doanh thu cho công ty." — Camera AI, mục 1

### A. Một mức chung cho mọi nhà máy

### B. Theo từng nhà máy

### C. Theo nhà máy và cỡ container (20 hay 40 feet)

**Xin thêm ở Ý kiến thêm:** đơn giá thu của đơn vị thuê quay cắt theo hợp đồng nào; ai lập bảng kê thu tiền, theo kỳ nào
**Ảnh hưởng:** lương quay cắt, dầu chờ nhận, bảng kê thu tiền đơn vị thuê

::: notes
- Nguồn: transport-dispatch OQ-62, ý Q5; tham số P-don-gia-luong-quay-cat, P-dinh-muc-dau-quay-cat. Không đề xuất.
:::

---

<!-- layout: oq; id: td-OQ-63; src: docs/transport-dispatch/brainstorms/transport-dispatch.md; group: Quay cắt -->
## Đầu kéo quay cắt cố định ở một nhà máy hay xoay giữa các nhà máy? Ai phân công, nhà máy nào đang có quay cắt?

> Phần mềm sẽ khai mỗi nhà máy có quay cắt trong danh mục địa điểm (vùng nhà máy và các đầu kéo được phân công). Đầu kéo quay cắt trong vùng nhà máy được phân công thì không bị cảnh báo "chạy ngoài Lệnh". Cần biết cách Delta đang bố trí để danh mục đúng thực tế.

**Tài liệu:** Camera AI — đếm tự động số lần quay cắt (11/8/2026), mục 1 Vấn đề

**Cách trả lời:** danh sách nhà máy đang có quay cắt; mỗi nhà máy mấy đầu kéo; đầu kéo cố định hay xoay; lái xe đổi ca thế nào; ai phân công
**Ảnh hưởng:** danh mục nhà máy quay cắt, cảnh báo chạy ngoài Lệnh

::: notes
- Nguồn: transport-dispatch OQ-63, ý Q1.
:::

---

<!-- layout: section -->
## Dữ liệu xe, hồ sơ xe

---

<!-- layout: oq; id: vt-OQ-16; src: docs/vehicle-telematics/brainstorms/vehicle-telematics.md; group: Dữ liệu xe, hồ sơ xe -->
## Hai mốc thời gian về dữ liệu thiết bị: nhờ Delta cho số

> Câu số liệu ở bộ câu hỏi trước, Delta trả lời "đã giải quyết trong VIS 18/10", nhưng bản đó chưa có hai số dưới đây. (1) Thiết bị đã gửi dữ liệu mà chưa khai trên hồ sơ xe nào (mới lắp, chuyển xe chưa duyệt): phần mềm giữ dữ liệu chờ khai bao lâu rồi xoá? (2) Cả đội xe cùng không có dữ liệu bao nhiêu phút thì coi là nhà cung cấp GPS ngừng gửi và báo quản trị, thay vì báo lỗi từng xe?

**Tài liệu:** chưa có trong tài liệu Delta gửi

**Cách trả lời:** ghi 2 số, vd "(1) 7 ngày · (2) 30 phút"
**Ảnh hưởng:** xử lý thiết bị mới lắp, cảnh báo mất dữ liệu cả đội xe

::: notes
- Nguồn: vehicle-telematics OQ-16, ý G6, G7; tham số P-giu-du-lieu-chua-khai, P-mat-du-lieu-ca-doi. Review VIS r10. Deck VIS vt-OQ-4 Delta trả "đã giải quyết trong VIS 18/10".
:::

---

<!-- layout: oq; id: vt-OQ-17; src: docs/vehicle-telematics/brainstorms/vehicle-telematics.md; group: Dữ liệu xe, hồ sơ xe -->
## Thiết bị GPS cho mooc và máy phát điện Delta đã lắp chưa?

> Thư đề xuất năm 2025 có đề nghị lắp GPS cho mooc và máy phát, kèm báo cáo giờ chạy máy phát. Phần mềm nhận dữ liệu các thiết bị này qua cùng nhà cung cấp GPS. Giờ chạy máy phát chỉ tính được nếu thiết bị gửi tín hiệu máy chạy, tắt.

**Tài liệu:** Đề xuất tiện ích GPS (25/9/2025), mục 2 Sơ mi-rơ mooc và mục 3 Máy phát điện
**Trích dẫn:** "Lập báo cáo chi tiết theo giời gian số giờ hoạt động của máy phát điện." — Đề xuất tiện ích GPS, mục 3

**Cách trả lời:** đã lắp chưa; bao nhiêu mooc, bao nhiêu máy phát; nhà cung cấp nào; thiết bị máy phát có gửi tín hiệu máy chạy, tắt không
**Ảnh hưởng:** vị trí mooc, máy phát trên bản đồ; giờ chạy máy phát

::: notes
- Nguồn: vehicle-telematics OQ-17, ý M1, M3.
:::

---

<!-- layout: oq; id: vt-OQ-18; src: docs/vehicle-telematics/brainstorms/vehicle-telematics.md; group: Dữ liệu xe, hồ sơ xe -->
## Mooc chưa gắn thiết bị thì lịch sử chỉ có theo Lệnh: Delta chấp nhận được không?

> Mooc không có thiết bị thì phần mềm chỉ biết đầu kéo nào kéo mooc đó qua Lệnh vận tải. Mooc bị kéo ngoài Lệnh (dời bãi, kéo đi sửa) sẽ không có lịch sử. Muốn đủ lịch sử thì mooc cần gắn thiết bị.

**Tài liệu:** chưa có trong tài liệu Delta gửi

### A. Chấp nhận lịch sử theo Lệnh
+ Không phát sinh chi phí thiết bị
- Mất dấu mooc khi bị kéo ngoài Lệnh

### B. Không chấp nhận
Nhờ ghi cách Delta muốn ở Ý kiến thêm (vd gắn thiết bị cho mọi mooc, hoặc bắt khai khi kéo ngoài Lệnh)

**Ảnh hưởng:** lịch sử sử dụng mooc, quản lý tài sản mooc

::: notes
- Nguồn: vehicle-telematics OQ-18, ý M1.
:::

---

<!-- layout: oq; id: vt-OQ-20; src: docs/vehicle-telematics/brainstorms/vehicle-telematics.md; group: Dữ liệu xe, hồ sơ xe -->
## Trạm thu phí tính tiền theo loại xe đăng ký trên thẻ hay theo tổ hợp thực tế lúc qua trạm?

> Danh mục xe gửi VETC ghi "Loại phí xe" trên từng thẻ (Loại 1 đến 5, đầu kéo phần lớn Loại 5). Phần mềm đang tính tiền vé dự kiến trên Lệnh theo tổ hợp thực tế (kéo container 20 hay 40 feet, kéo mooc rỗng). Nếu trạm thu theo loại trên thẻ, đội đề xuất lấy loại trên thẻ làm giá dự kiến và cảnh báo khi tiền trừ lệch.

**Tài liệu:** Công văn 20260902/CV gửi VETC (21/9/2026), 4 danh mục xe đính kèm, cột "Loại phí xe"

### A. Theo loại đăng ký trên thẻ
Giá vé dự kiến lấy theo loại trên thẻ; tiền trừ lệch thì cảnh báo

### B. Theo tổ hợp thực tế khi qua trạm
Giá vé dự kiến theo tổ hợp trên Lệnh

**Ảnh hưởng:** giá vé dự kiến trên Lệnh, cảnh báo lệch tiền vé

::: notes
- Nguồn: vehicle-telematics OQ-20. Không đề xuất: câu hỏi sự thật (Delta 21/10: VETC chia giá theo 5 nhóm xe, khớp A nhưng chưa nói rõ).
:::

---

<!-- layout: oq; id: vt-OQ-21; src: docs/vehicle-telematics/brainstorms/vehicle-telematics.md; group: Dữ liệu xe, hồ sơ xe -->
## Xe của pháp nhân này chạy Lệnh cho JobID của pháp nhân kia: tiền vé hạch toán cho bên nào?

> 4 tài khoản giao thông thuộc 2 pháp nhân: 1 tài khoản của Chi nhánh Công ty CP Quốc tế Delta tại HCM (49 xe), 3 tài khoản của Công ty TNHH MTV Vận tải Delta (70, 108, 27 xe). Một xe có thể chạy cho JobID của pháp nhân khác. Khi đó tiền vé bị trừ ở tài khoản của chủ xe nhưng phục vụ JobID của bên kia.

**Tài liệu:** Công văn 20260902/CV gửi VETC (21/9/2026), bảng 4 tài khoản giao thông
**Trích dẫn:** "quan trọng nhất là phân bổ chi phí vé vào từng Lệnh vận tải để hạch toán kế toán" — Công văn gửi VETC

### A. Pháp nhân chủ tài khoản bị trừ tiền
+ Khớp hoá đơn VETC cấp cho tài khoản đó
- Chi phí JobID của pháp nhân kia thiếu tiền vé

### B. Pháp nhân của JobID, kèm giao dịch nội bộ giữa hai pháp nhân
+ Chi phí JobID đầy đủ
- Phát sinh giao dịch nội bộ phải đối chiếu

**Ảnh hưởng:** hạch toán tiền vé, giao dịch nội bộ giữa hai pháp nhân

::: notes
- Nguồn: vehicle-telematics OQ-21, ý K4; service-delivery ý B7 (giao dịch nội bộ). Không đề xuất.
:::

---

<!-- layout: oq; id: vm-OQ-4.1; src: docs/vehicle-management/brainstorms/vehicle-management.md; group: Dữ liệu xe, hồ sơ xe -->
## Máy phát điện tháo ra lắp sang mooc khác thì ai khai trên phần mềm?

> Đội thiết kế máy phát là thiết bị gắn theo mooc: hồ sơ mooc ghi máy phát nào đang gắn, ngày gắn; tháo sang mooc khác thì ghi lần gắn mới và giữ lịch sử. Máy phát nằm xa mooc đang khai thì phần mềm báo lệch. Cần biết ai là người khai khi tháo lắp.

**Tài liệu:** Đề xuất tiện ích GPS (25/9/2025), mục 3 Máy phát điện

### A. Quản lý phương tiện khai trên web

### B. Lái xe khai trên app khi tháo lắp
Quản lý phương tiện duyệt

**Nếu máy phát hầu như không tháo lắp:** ghi ở Ý kiến thêm
**Ảnh hưởng:** hồ sơ mooc, cảnh báo máy phát lệch mooc

::: notes
- Nguồn: vehicle-management OQ-4 (ý 1), ý H8; vehicle-telematics ý M3.
:::

---

<!-- layout: oq; id: vm-OQ-4.2; src: docs/vehicle-management/brainstorms/vehicle-management.md; group: Dữ liệu xe, hồ sơ xe -->
## Có cần phần mềm nhắc bảo dưỡng máy phát điện theo số giờ chạy không?

> Phần mềm đã có nhắc bảo dưỡng xe theo km, theo ngày. Nếu thiết bị máy phát gửi được giờ chạy, phần mềm có thể nhắc bảo dưỡng máy phát theo số giờ (vd mỗi 500 giờ).

**Tài liệu:** Đề xuất tiện ích GPS (25/9/2025), mục 3 Máy phát điện

### A. Có
Nhờ ghi chu kỳ bảo dưỡng ở Ý kiến thêm

### B. Không cần

**Ảnh hưởng:** nhắc bảo dưỡng cho quản lý phương tiện

::: notes
- Nguồn: vehicle-management OQ-4 (ý 3), feature reminders. Phụ thuộc vt-OQ-17 (thiết bị có gửi giờ chạy). "500 giờ" chỉ là ví dụ minh hoạ.
:::

---

<!-- layout: oq; id: vm-OQ-5; src: docs/vehicle-management/brainstorms/vehicle-management.md; group: Dữ liệu xe, hồ sơ xe -->
## Delta có file Excel danh mục xe và thẻ thu phí để nhập ban đầu vào hồ sơ xe không?

> Công văn gửi VETC có 4 danh mục 254 xe (biển số, số thẻ, loại phí, trạng thái thẻ), nhưng bản đội nhận là ảnh chụp. Có file Excel gốc thì đội nhập thẳng vào hồ sơ xe khi đưa phần mềm vào dùng, tránh gõ lại.

**Tài liệu:** Công văn 20260902/CV gửi VETC (21/9/2026), 4 danh mục xe đính kèm

### A. Có, gửi kèm
Nhờ gửi file qua email người nhận câu trả lời

### B. Không có file Excel

**Ảnh hưởng:** nhập dữ liệu hồ sơ xe ban đầu

::: notes
- Nguồn: vehicle-management OQ-5. Công văn VETC là PDF scan (chữ gõ lại từ ảnh).
:::

---

<!-- layout: section -->
## Điều phối hiện trường

---

<!-- layout: oq; id: sc-OQ-39; src: docs/shipment-coordination/brainstorms/shipment-coordination.md; group: Điều phối hiện trường -->
## Những cảng, bãi nào có ePort nhưng nhân viên hiện trường vẫn phải xuống thanh lý tờ khai?

> Hàng nhập FCL ở cảng có ePort: CS đổi lệnh giao hàng sang Lệnh nâng hàng trên ePort. Quy trình ghi "ở một số cảng bãi" hiện trường vẫn phải xuống làm thủ tục thanh lý tờ khai, nên trường hợp này tách hai. Phần mềm cần biết cảng nào thuộc loại phải xuống để tự sinh việc cho hiện trường.

**Tài liệu:** Quy trình điều phối, mục 5.4.2.2
**Trích dẫn:** "“Ở một số cảng bãi” nhân viên hiện trường vẫn phải xuống cảng bãi để làm thủ tục thanh lý tờ khai sau khi nhân viên CS đã thực hiện việc đổi Lệnh giao hàng sang Lệnh nâng hàng trên ePort." — Quy trình điều phối, mục 5.4.2.2

**Cách trả lời:** danh sách cảng, bãi (tên như Delta đang gọi); nếu danh sách hay đổi thì ghi ai cập nhật
**Ảnh hưởng:** danh mục cảng, bãi; giao việc hiện trường hàng nhập FCL

::: notes
- Nguồn: shipment-coordination OQ-39 (Mục 5 sơ đồ dòng 251). Điều phối dòng 1480.
:::

---

<!-- layout: oq; id: sc-OQ-40; src: docs/shipment-coordination/brainstorms/shipment-coordination.md; recommend: A; group: Điều phối hiện trường -->
## Hàng nhập FCL: ai tải Lệnh nâng hàng lên JobID, nhân viên hiện trường hay CS?

> Ở bước nhân viên hiện trường lấy Lệnh nâng container hàng, quy trình liệt kê việc của hiện trường gồm tải Lệnh nâng hàng lên JobID, nhưng câu ngay sau lại ghi "nhân viên CS upload đủ". Đội hiểu là hiện trường tải lên, cần Delta xác nhận.

**Tài liệu:** Quy trình điều phối, mục 5.4.2.4 Lệnh nâng container hàng
**Trích dẫn:** "Upload Lệnh nâng hàng cho tất cả số container có trên vận đơn lên JobID." — việc của nhân viên hiện trường, mục 5.4.2.4
**Trích dẫn:** "Sau khi nhân viên CS upload đủ Lệnh nâng hàng lên JobID thì phần mềm tự động chuyển JobID thành Yêu cầu vận tải" — mục 5.4.2.4

### A. Nhân viên hiện trường tải lên
+ Người cầm lệnh tải luôn, không chuyển tay

### B. CS tải lên
Hiện trường gửi lệnh cho CS
- Thêm một bước chuyển tay

**Ảnh hưởng:** việc của hiện trường, thời điểm sinh Yêu cầu vận tải
**Vì sao đề xuất A:** hiện trường là người lấy Lệnh nâng tại cảng, tải lên ngay thì Yêu cầu vận tải sinh sớm hơn

::: notes
- Nguồn: shipment-coordination OQ-40 (Mục 9 giả định dòng 563). Điều phối dòng 1514–1518.
:::

---

<!-- layout: oq; id: sc-OQ-41; src: docs/shipment-coordination/brainstorms/shipment-coordination.md; group: Điều phối hiện trường -->
## Việc giao cho nhân viên hiện trường quá bao lâu chưa bấm nhận thì tự quay về cán bộ quản lý giao lại?

> Cán bộ quản lý hiện trường giao việc, người được giao bấm nhận. Người đó không nhận (bận, quên, không có sóng) thì việc cần quay về để giao người khác, tránh trễ mốc của JobID. Cần Delta cho số phút.

**Tài liệu:** chưa có trong tài liệu Delta gửi

**Cách trả lời:** ghi số phút, vd "30 phút"; trong giờ và ngoài giờ có khác không
**Ảnh hưởng:** giao việc hiện trường, việc chờ cán bộ quản lý giao lại

::: notes
- Nguồn: shipment-coordination OQ-41; tham số P-thoi-gian-cho-nhan-viec.
:::

---

<!-- layout: oq; id: sc-OQ-48; src: docs/shipment-coordination/brainstorms/shipment-coordination.md; recommend: A; group: Điều phối hiện trường -->
## Tiền chọn vỏ container có áp định mức theo từng bãi và tự ghi lên JobID không?

> Tiền chọn vỏ là khoản hiện trường trả quản lý bãi để lấy vỏ tốt, hạch toán vào công tác phí. Quy trình nói xây định mức theo địa điểm để tự áp lên JobID, nhưng câu đó đứng sau 3 khoản hải quan. Delta đang làm bảng loại phí theo địa điểm (bộ câu hỏi 06/10); câu này chỉ hỏi riêng tiền chọn vỏ.

**Tài liệu:** Quy trình cung cấp dịch vụ tổng quát (24/9/2026), mục 4.6
**Trích dẫn:** "Tiền chọn vỏ container tại cảng. Chi phí này do nhân viên hiện trường chi trả cho quản lý bãi container để nhận vỏ container tốt." — mục 4.6
**Trích dẫn:** "Các chi phí định mức này sẽ được xây dựng theo địa điểm làm thủ tục hải quan và đưa lên phần mềm để tự động áp lên JobID." — mục 4.6

### A. Định mức theo bãi, phần mềm tự ghi lên JobID khi giao việc chọn vỏ
+ Hiện trường không phải kê số tiền
+ Kiểm soát được chi phí từng bãi
- Phải lập và cập nhật định mức từng bãi

### B. Hiện trường kê số thực chi khi thanh toán
+ Không cần bảng định mức
- Khó kiểm soát, dễ lệch giữa người

**Ảnh hưởng:** giao việc chọn vỏ, chi phí hiện trường trên JobID
**Vì sao đề xuất A:** cùng cách với các khoản hải quan, và chọn vỏ cũng là khoản không hoá đơn cần định mức để hạch toán công tác phí

::: notes
- Nguồn: shipment-coordination OQ-48, ý B20 (định mức theo địa điểm × loại việc, location-catalog). CCDV dòng 934, mục 4.6 đoạn bôi vàng. Deck 06/10 OQ-31 (Delta: sẽ làm rõ bảng loại phí theo địa điểm, chưa hẹn).
:::

---

<!-- layout: oq; id: sc-OQ-71; src: docs/shipment-coordination/brainstorms/shipment-coordination.md; recommend: A; group: Điều phối hiện trường -->
## Hàng xuất FCL chọn thiếu vỏ: CS quyết "Chọn tiếp" hay "Chốt số", và chốt số cần cán bộ quản lý hiện trường duyệt?

> Hiện trường hoặc lái xe chọn được ít vỏ đạt chuẩn hơn số container: phần mềm sinh Yêu cầu vận tải cho các container đã chọn, rồi báo CS. CS hỏi khách hàng và bấm "Chọn tiếp" (quay lại bãi chọn nốt) hoặc "Chốt số" (dừng chọn, ghi số container thực mới lên JobID). Chốt số làm giảm doanh thu JobID nên đội đề xuất cán bộ quản lý hiện trường duyệt.

**Tài liệu:** Quy trình điều phối, mục 4.6, đoạn "Xác định số lượng container xuất FCL trên JobID"
**Trích dẫn:** "Chọn không đủ số lượng container trên JobID: Thỏa thuận với khách hàng để kéo dài thời gian chọn vỏ hoặc chốt số lượng container trên JobID tại bước này." — Quy trình điều phối, mục 4.6

### A. CS bấm, chốt số cần cán bộ quản lý hiện trường duyệt
+ Có người kiểm soát khi giảm doanh thu

### B. CS bấm, chốt số không cần duyệt
+ Nhanh hơn
- Không ai kiểm soát việc giảm số container

### C. Người khác bấm
Nhờ ghi là ai ở Ý kiến thêm

**Ảnh hưởng:** chọn vỏ hàng xuất FCL, số container và doanh thu trên JobID
**Vì sao đề xuất A:** CS là người làm việc với khách hàng; chốt số làm giảm doanh thu nên cần người duyệt

::: notes
- Nguồn: shipment-coordination OQ-71, ý B16; tham số P-duyet-chot-so-container (Delta: bật, chờ xác nhận). Điều phối dòng 609–620.
:::

---

<!-- layout: oq; id: sc-OQ-75; src: docs/shipment-coordination/brainstorms/shipment-coordination.md; recommend: A; group: Điều phối hiện trường -->
## Khi chọn vỏ hàng xuất FCL còn dở, JobID chưa được chuyển sang "Đã thực hiện Lệnh vận tải": Delta đồng ý không?

> Trong lúc đang "Chọn tiếp" hoặc chờ duyệt chốt số, một số Lệnh của JobID có thể đã chạy xong và được duyệt. Đội đề xuất JobID chỉ sang "Đã thực hiện Lệnh vận tải" khi việc chọn vỏ đã xong, vì số container còn có thể đổi.

**Tài liệu:** Quy trình điều phối, mục 4.6, đoạn "Xác định số lượng container xuất FCL trên JobID"

### A. Đồng ý, chờ chọn vỏ xong
+ Không ghi nhận JobID xong khi còn container chưa chạy

### B. Cho sang ngay khi các Lệnh đã có đều được duyệt
- Phải mở lại JobID khi chọn thêm được vỏ

**Ảnh hưởng:** trạng thái JobID, thời điểm ghi nhận doanh thu, chi phí
**Vì sao đề xuất A:** số container chưa chốt thì doanh thu, chi phí JobID chưa đủ

::: notes
- Nguồn: shipment-coordination OQ-75, ý B16; service-delivery Mục 6 (dòng 294).
:::

---

<!-- layout: oq; id: sc-OQ-77; src: docs/shipment-coordination/brainstorms/shipment-coordination.md; group: Điều phối hiện trường -->
## Chốt số container và việc phát sinh chờ cán bộ quản lý hiện trường duyệt quá bao lâu thì phần mềm nhắc lại?

> Hai việc cần cán bộ quản lý hiện trường duyệt: chốt số container (chọn thiếu vỏ) và việc phát sinh khách hàng báo thêm vào JobID. Chờ quá lâu thì JobID bị chậm. Ngoài giờ, nhắc gửi người trực.

**Tài liệu:** chưa có trong tài liệu Delta gửi

**Cách trả lời:** ghi số phút hoặc giờ, vd "1 giờ"
**Ảnh hưởng:** nhắc duyệt cho cán bộ quản lý hiện trường

::: notes
- Nguồn: shipment-coordination OQ-77; tham số P-han-duyet-dieu-phoi; ý B16, B18.
:::

---

<!-- layout: oq; id: sc-OQ-76; src: docs/shipment-coordination/brainstorms/shipment-coordination.md; group: Điều phối hiện trường -->
## Khách hàng báo thêm việc sau khi JobID đã "Hoàn thành dịch vụ" (hoặc đã xuất hoá đơn) thì xử lý thế nào?

> Trước mốc "Hoàn thành dịch vụ", CS thêm "Việc phát sinh" vào JobID, cán bộ quản lý hiện trường duyệt, chi phí và khoản thu ghi lên JobID ngay. Sau mốc này phần mềm đã ghi nhận doanh thu, chi phí vào kỳ báo cáo, nên thêm việc vào JobID cũ sẽ làm đổi số của kỳ đã chốt.

**Tài liệu:** Quy trình cung cấp dịch vụ tổng quát (24/9/2026), mục 5.1.2
**Trích dẫn:** "Để phần mềm có thể thực hiện việc ghi nhận doanh thu và chi phí trong kỳ báo cáo thì JobID bắt buộc phải có một trạng thái là hoàn thành dịch vụ." — Quy trình cung cấp dịch vụ tổng quát

### A. Mở lại JobID cũ, có duyệt
+ Giữ một JobID cho một lô hàng
- Đổi số liệu kỳ đã ghi nhận

### B. Ghi vào một JobID mới
+ Không đụng kỳ đã chốt
- Một lô hàng có hai JobID

**Ảnh hưởng:** việc phát sinh, ghi nhận doanh thu, bảng kê

::: notes
- Nguồn: shipment-coordination OQ-76, ý B18; service-delivery Mục 6 (dòng 294). CCDV dòng 888. Không đề xuất.
:::

---

<!-- layout: oq; id: sc-OQ-72; src: docs/shipment-coordination/brainstorms/shipment-coordination.md; group: Điều phối hiện trường -->
## Việc "Thu hoá đơn GTGT" có hạn bao lâu từ khi lái xe tạo Yêu cầu thanh toán? Quá hạn thì nhắc ai?

> Lái xe tạo Yêu cầu thanh toán trên Lệnh (khoản trả hộ). Phần mềm giao việc thu hoá đơn GTGT cho người gần lái xe nhất theo phân công của JobID: hiện trường cùng cảng, bãi, rồi hiện trường gần nhất, rồi CS. Cần hạn hoàn thành và người nhận nhắc khi quá hạn.

**Tài liệu:** Phân hệ APAS (17/10/2026), mục 3.1.2 Các thành phần hệ thống và kết nối ngoại vi
**Trích dẫn:** "Phần mềm sẽ giao nhiệm vụ này cho nhân viên CS hoặc hiện trường theo nguyên tắc giao cho người gần lái xe nhất theo luồng phân công công việc của Lệnh vận tải đó." — APAS, mục 3.1.2

**Cách trả lời:** ghi số ngày, vd "3 ngày"; quá hạn nhắc ai (cán bộ quản lý hiện trường, kế toán…)
**Ảnh hưởng:** việc thu hoá đơn GTGT trong "Việc của tôi", nhắc quá hạn

::: notes
- Nguồn: shipment-coordination OQ-72, ý B19; service-delivery ý E6.
:::

---

<!-- layout: oq; id: sc-OQ-73; src: docs/shipment-coordination/brainstorms/shipment-coordination.md; group: Điều phối hiện trường -->
## Danh mục lô hàng cần hiện những thông tin gì, lọc theo gì, và ai được xem?

> Mỗi chứng từ vận tải (vận đơn, Booking Note) phần mềm đọc được sẽ thành một dòng trong danh mục lô hàng, kèm JobID nháp. CS thấy lô nào đã có chứng từ mà chưa thành JobID. APAS chỉ nêu danh mục này là một kết quả, chưa nói nội dung.

**Tài liệu:** Phân hệ APAS (17/10/2026), mục 2.2.1 Giới hạn phạm vi thông tin
**Trích dẫn:** "Kết quả 1: Danh mục lô hàng (Shipment List) cho phòng nghiệp vụ." — APAS, mục 2.2.1

**Cách trả lời:** các cột cần (vd tàu, chuyến, ngày tàu đến/đi, cut-off, số container, khách hàng); lọc theo gì; ai xem (CS từng chi nhánh, cán bộ quản lý…)
**Ảnh hưởng:** màn danh mục lô hàng của CS

::: notes
- Nguồn: shipment-coordination OQ-73, ý A12; service-delivery ý A11.
:::

---

<!-- layout: oq; id: sc-OQ-74; src: docs/shipment-coordination/brainstorms/shipment-coordination.md; group: Điều phối hiện trường -->
## Ai ký Quyết định phân công công việc hằng tháng cho CS và nhân viên hiện trường?

> Quyết định phân công kèm bảng kê JobID và số tiền là chứng từ để hạch toán chi phí hiện trường là công tác phí. Phần mềm tự sinh mỗi người một Quyết định mỗi tháng. Với lái xe, quy trình ghi rõ lái xe ký online khi nhận bảng lương; với CS và hiện trường chưa nói ai ký.

**Tài liệu:** Quy trình cung cấp dịch vụ tổng quát (24/9/2026), mục 4.6, phần Giải pháp
**Trích dẫn:** "Soạn mẫu quyết định gồm … (2) Mẫu quyết định phân công công việc cho nhân viên CS và nhân viên hiện trường và bảng kê đính kèm (JobID và số tiền tương ứng)." — mục 4.6

**Cách trả lời:** người ký (vd trưởng phòng, giám đốc chi nhánh); người nhận có ký xác nhận không; ký online hay giấy
**Ảnh hưởng:** Quyết định phân công hằng tháng, hồ sơ công tác phí

::: notes
- Nguồn: shipment-coordination OQ-74, ý B20; feature fund-payments sinh Quyết định.
:::

---

<!-- layout: section -->
## Cung cấp dịch vụ, công nợ

---

<!-- layout: oq; id: sd-OQ-36; src: docs/service-delivery/brainstorms/service-delivery.md; group: Cung cấp dịch vụ, công nợ -->
## Khách hàng CBT đổi pháp nhân thanh toán sang bên mới: ai duyệt mã khách cấp 2?

> Khách hàng CBT có thể đổi pháp nhân thanh toán sau khi đã tạo JobID, kể cả sang bên thứ ba Delta chưa có hợp đồng. Quy trình mới: tạo mã khách cấp 2 từ mã chính, tải thoả thuận thanh toán ba bên, rồi duyệt mã. Quy trình chưa nói ai duyệt.

**Tài liệu:** Giao nhận hàng hoá (18/9/2026), mục 3.4.1.1 Doanh thu
**Trích dẫn:** "Đăng ký thông tin bên thứ 3 bằng cách tạo mã DK05 cấp 2 từ mã DK05 chính và phê duyệt mã này." — Giao nhận hàng hoá, mục 3.4.1.1

**Cách trả lời:** người tạo và người duyệt (vd CS tạo, kế toán công nợ duyệt); có cần duyệt hai cấp không
**Ảnh hưởng:** danh mục khách hàng, xuất hoá đơn cho bên thứ ba

::: notes
- Nguồn: service-delivery OQ-36.
:::

---

<!-- layout: oq; id: sd-OQ-42; src: docs/service-delivery/brainstorms/service-delivery.md; group: Cung cấp dịch vụ, công nợ -->
## JobID bị dừng vì khách nợ quá hạn hoặc vượt hạn mức: có cần nhắc CS sau một số ngày không?

> Khách có nợ quá hạn hoặc vượt hạn mức thì JobID dừng ở "Chờ khách thanh toán", không tự huỷ, cho tới khi khách trả hoặc gia hạn nợ được duyệt. JobID có thể nằm đó lâu mà không ai để ý.

**Tài liệu:** chưa có trong tài liệu Delta gửi

### A. Có nhắc
Nhờ ghi ở Ý kiến thêm: sau bao nhiêu ngày, nhắc ai (CS, sales, cán bộ quản lý)

### B. Không cần nhắc

**Ảnh hưởng:** JobID dừng vì công nợ, việc nhắc CS

::: notes
- Nguồn: service-delivery OQ-42 (Mục 6.4 dòng 310, Mục 8 việc chạy theo giờ).
:::

---

<!-- layout: oq; id: sd-OQ-67; src: docs/service-delivery/brainstorms/service-delivery.md; group: Cung cấp dịch vụ, công nợ -->
## Một lần gia hạn nợ quá hạn được tối đa bao nhiêu ngày? Có giới hạn số lần gia hạn không?

> Khách có nợ quá hạn mà vẫn cần làm hàng thì CS hoặc sales tạo yêu cầu gia hạn theo hoá đơn, bảng kê quá hạn; cán bộ quản lý duyệt bước 1, Ban giám đốc duyệt bước 2. Quy trình chưa nêu giới hạn.

**Tài liệu:** Quy trình cung cấp dịch vụ tổng quát (24/9/2026), mục 4.9.4 Nợ quá hạn
**Trích dẫn:** "Nếu mã DK05 có nợ quá hạn nhưng vẫn cần cung cấp dịch vụ thì cần phải gia hạn nợ để phần mềm duyệt JobID." — mục 4.9.4

**Cách trả lời:** số ngày tối đa mỗi lần; số lần tối đa cho một hoá đơn, bảng kê (hoặc "không giới hạn")
**Ảnh hưởng:** yêu cầu gia hạn nợ, duyệt JobID khi khách nợ quá hạn

::: notes
- Nguồn: service-delivery OQ-67, ý B13; tham số P-so-ngay-gia-han-no-toi-da (feature debt-management).
:::

---

<!-- layout: oq; id: sd-OQ-68.1; src: docs/service-delivery/brainstorms/service-delivery.md; group: Cung cấp dịch vụ, công nợ -->
## "Dư nợ tạm ứng 2" trong tài liệu APAS là gì?

> Khi nhân viên trả chi phí từ tài khoản công ty qua ngân hàng và hoá đơn về khớp giao dịch, APAS ghi giảm "Dư nợ tạm ứng 2" của nhân viên. Đội hiểu đây là tài khoản tạm ứng riêng cho khoản chi qua ngân hàng, khác tạm ứng tiền mặt, nhưng tài liệu chưa định nghĩa.

**Tài liệu:** Phân hệ APAS (17/10/2026), mục 3.3.2 Bước 4
**Trích dẫn:** "IIP ghi giảm “Dư nợ tạm ứng 2” của nhân viên thực hiện" — APAS, mục 3.3.2

**Cách trả lời:** giải thích ngắn; "Dư nợ tạm ứng 1" (nếu có) là gì; hai loại có hạch toán tài khoản riêng không
**Ảnh hưởng:** dư nợ tạm ứng của nhân viên, đối chiếu hoá đơn với giao dịch ngân hàng

::: notes
- Nguồn: service-delivery OQ-68 (ý 1), ý E2.
:::

---

<!-- layout: oq; id: sd-OQ-68.2; src: docs/service-delivery/brainstorms/service-delivery.md; group: Cung cấp dịch vụ, công nợ -->
## Mức 5 triệu đồng có còn là ngưỡng nhân viên được trả chi phí bằng tiền cá nhân không?

> Cách trả mặc định là nhân viên quét QR, trả từ tài khoản công ty qua ngân hàng. Trả bằng tiền cá nhân là ngoại lệ, đội đang để dưới 5 triệu đồng theo hạn mức chi tiền mặt trong quy trình.

**Tài liệu:** Quy trình cung cấp dịch vụ tổng quát (24/9/2026), mục 4.6, bảng điều kiện hạch toán công tác phí
**Trích dẫn:** "Tuân thủ hạn mức chi tiền mặt là 5 triệu đồng, vượt quá phải thanh toán không dùng tiền mặt." — mục 4.6

### A. Đúng, vẫn là 5 triệu đồng

### B. Ngưỡng khác
Nhờ ghi số ở Ý kiến thêm

**Ảnh hưởng:** chi phí nhân viên trả bằng tiền cá nhân, luồng thanh toán hoá đơn sau

::: notes
- Nguồn: service-delivery OQ-68 (ý 2), ý E2; tham số P-nguong-tam-ung (Delta: 5.000.000 ₫).
:::

---

<!-- layout: oq; id: sd-OQ-45; src: docs/service-delivery/brainstorms/service-delivery.md; group: Cung cấp dịch vụ, công nợ -->
## Kho dữ liệu Ecus "VT" có phải là điểm khai hải quan Hải Phòng không?

> Tài liệu Ecus ghi Delta khai tập trung ở Hà Nội, Hải Phòng, TP.HCM, nhưng sơ đồ có 3 kho dữ liệu HN, HCM, VT. Trước đó Delta cho biết không có chi nhánh Hải Phòng. Đội cần biết VT (Vận tải Delta) có phải điểm khai Hải Phòng không, để gắn JobID hải quan đúng chi nhánh.

**Tài liệu:** Kết nối API với Ecus (26/10/2025), mục 1 Mục đích và sơ đồ mục 3.1
**Trích dẫn:** "khai báo hải quan tập trung tại Hà Nội, Hải Phòng và Hồ Chí Minh" — Kết nối API với Ecus, mục 1

### A. Đúng, VT là điểm khai Hải Phòng

### B. Không phải
Nhờ ghi VT là gì ở Ý kiến thêm

**Xin thêm ở Ý kiến thêm:** JobID hải quan khai ở Hải Phòng gắn chi nhánh nào
**Ảnh hưởng:** kết nối Ecus, chi nhánh của JobID hải quan

::: notes
- Nguồn: service-delivery OQ-45 (OQ-17 cũ: "không có chi nhánh Hải Phòng"), ý A10, H1–H5. Không đề xuất.
:::

---

<!-- layout: oq; id: sd-OQ-46; src: docs/service-delivery/brainstorms/service-delivery.md; group: Cung cấp dịch vụ, công nợ -->
## Kết nối Ecus: Delta đã làm việc với bên cung cấp Ecus chưa, và khách khai thuê hiện chia nhóm thế nào?

> Tài liệu yêu cầu kết nối Ecus viết từ 10/2025. Delta khai thuê cho 137 khách, chia 2 nhóm: khai trên máy Delta (nhóm 1) và khai trên máy của khách (nhóm 2). Nhóm 2 có thể cài EcusAuto để đồng bộ, hoặc xuất file làm tay. Số khách mỗi cách quyết định phần nào cần làm trước.

**Tài liệu:** Kết nối API với Ecus (26/10/2025), mục 2.2 Khách hàng của Delta và mục 3.2
**Trích dẫn:** "Delta đang cung cấp dịch vụ khai thuê hải quan cho 137 khách hàng, khai báo tất cả các loại hình tờ khai và phân làm hai nhóm" — mục 2.2

**Cách trả lời:** đã làm việc với bên Ecus chưa, kết quả; số khách nhóm 2; trong đó bao nhiêu khách dùng EcusAuto, bao nhiêu làm tay
**Ảnh hưởng:** thứ tự làm kết nối Ecus, tờ khai tự vào JobID

::: notes
- Nguồn: service-delivery OQ-46, ý H2.
:::

---

<!-- layout: oq; id: sd-OQ-70.1; src: docs/service-delivery/brainstorms/service-delivery.md; group: Cung cấp dịch vụ, công nợ -->
## Cước vận tải quốc tế (đường biển, hàng không) dùng loại JobID nào, nhận diện bằng chứng từ gì?

> Tài liệu Delta 3.0 đưa cước quốc tế vào phạm vi phần mềm giai đoạn 1, nhưng bảng 12 loại JobID hiện có chưa có loại nào cho dịch vụ này. Mỗi loại JobID cần chứng từ định danh (vd vận đơn, Booking Note) để phần mềm đọc và tạo JobID nháp.

**Tài liệu:** Phần mềm Delta 3.0 — Thiết kế kiến trúc và lộ trình (16/10/2026), mục 3.1.3 Nghiệp vụ
**Trích dẫn:** "Vận tải quốc tế (sea & air freight) và các dịch vụ giá trị gia tăng." — Delta 3.0, mục 3.1.3

**Cách trả lời:** dùng loại JobID có sẵn nào hay cần loại mới; chứng từ định danh (vận đơn biển, vận đơn hàng không…)
**Ảnh hưởng:** danh mục loại JobID, tạo JobID cho cước quốc tế

::: notes
- Nguồn: service-delivery OQ-70 (ý 1), ý B9 (P-loai-jobid).
:::

---

<!-- layout: oq; id: sd-OQ-70.2; src: docs/service-delivery/brainstorms/service-delivery.md; group: Cung cấp dịch vụ, công nợ -->
## Dịch vụ cho thuê kho có tạo JobID trên phần mềm không?

> Delta 3.0 chia việc: phần mềm quản lý kho lo vận hành và lập bảng kê phí dịch vụ; Delta MIS lo hợp đồng, hạn mức công nợ và xuất hoá đơn. Chưa rõ phần cho thuê kho có đi qua JobID như các dịch vụ khác không.

**Tài liệu:** Phần mềm Delta 3.0 — Thiết kế kiến trúc và lộ trình (16/10/2026), mục 3.1.3 Nghiệp vụ
**Trích dẫn:** "WMS (Vận hành - tính cước)… Tập hợp số liệu và lập bảng kê phí dịch vụ." — Delta 3.0, mục 3.1.3

### A. Có, mỗi hợp đồng hoặc kỳ thuê là một JobID
+ Doanh thu, chi phí kho nằm chung báo cáo theo JobID

### B. Không, chỉ nhận bảng kê phí từ phần mềm kho để xuất hoá đơn
+ Gọn, không trùng việc với phần mềm kho
- Không theo dõi chi phí kho theo JobID

**Ảnh hưởng:** phạm vi tạo JobID, kết nối với phần mềm quản lý kho

::: notes
- Nguồn: service-delivery OQ-70 (ý 2). Không đề xuất.
:::

---

<!-- layout: recap -->
## Tổng kết câu trả lời

---

<!-- layout: end -->
# Cảm ơn anh/chị
Đội sẽ cập nhật thiết kế theo câu trả lời và hẹn trao đổi riêng những câu cần bàn thêm
