---
type: meeting-deck
meeting: open-questions
delivery: async
density: compact
title: Câu hỏi cần xác nhận — Dữ liệu vận hành xe (VIS)
client: Delta
date: 2026-10-15
footer: Câu hỏi cần xác nhận — Dữ liệu vận hành xe (VIS)
brand: innvie-v1
status: stale
status_prev: draft
updated: 2026-10-15
links:
  - docs/transport-dispatch/brainstorms/transport-dispatch.md
  - docs/meetings/2026-10-09-client-dispatch-field-issues.md
  - docs/meetings/2026-10-10-oq-dispatch-coordination.md
  - _workspace/backlog.md
  - docs-input/sop/vis-giam-sat-doi-xe/vis-giam-sat-doi-xe.md
  - docs-input/tich-hop/vis-sim-cong-tac-chuan-bi/vis-sim-cong-tac-chuan-bi.md
  - docs-input/tich-hop/gps-tien-ich-de-xuat-2025-09-25/gps-tien-ich-de-xuat-2025-09-25.md
  - docs-input/sop/apas-thanh-toan-doi-soat/apas-thanh-toan-doi-soat.md
  - docs-input/srs-cu/lg-srs-export.md
---

<!-- layout: title -->
# Câu hỏi cần xác nhận — Dữ liệu vận hành xe (VIS)
30 nội dung nhờ Delta trả lời để hoàn thiện phần vé cầu đường, bù dầu, đối soát dầu và cảnh báo xe

::: notes
- Bản gửi khách tự trả lời (delivery: async, density: compact) — ghi chú KHÔNG có trong file HTML gửi đi.
- Nguồn câu hỏi: Mục 11 của 3 bản nháp brainstorm VIS (CHƯA ghi repo) ở ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/vis/: transport-dispatch.md OQ-49..57 (id `td-…`), vehicle-telematics.md OQ-1..14 (id `vt-…`), vehicle-management.md OQ-1..3 (id `vm-…`); + 3 câu đã có trong repo docs/transport-dispatch/brainstorms/transport-dispatch.md (OQ-47 tách 47.1/47.2, OQ-48); + review VIS r1 "Hỏi khách" (hút/đổ dầu khi tắt máy) gộp vào câu EUP.
- OQ-50 tách 2 slide (td-OQ-50.1 cơ chế chốt, td-OQ-50.2 lương). OQ-55 viết lại theo lời Delta 09/10 (bỏ mooc giữa đường, điều xe khác kéo tiếp).
- Khi import: câu trả lời ghi vào cột Trả lời Mục 11 của bản nháp tương ứng (rồi theo bản nháp vào repo khi ghi brainstorm VIS); 3 câu repo ghi vào transport-dispatch.md Mục 11. Review r2–r12 chưa trả lời — có thể sinh thêm câu.
- Không ghi reply_to / reply_by theo lựa chọn của user 15/10. Brand innvie-v1 (memory client-deck-old-style).
:::

---

<!-- layout: goal -->
## Vì sao cần anh/chị trả lời
- **30 câu hỏi** về dữ liệu vận hành xe (VIS) đang chặn phần thiết kế vé cầu đường, bù dầu kẹt xe, đối soát dầu và cảnh báo xe
- Mỗi câu có bối cảnh và câu trích từ tài liệu Delta đã gửi (VIS 08/10, Công tác chuẩn bị 11/10, thư đề xuất GPS 25/9/2025) để tiện đọc lại
- Nhiều câu đã có đề xuất của đội, chỉ cần Delta xác nhận hoặc sửa
- Mất khoảng 75–90 phút; có thể làm nhiều lần, câu trả lời tự lưu
- Câu liên quan EUP, VETC có thể cần hỏi đối tác: chưa rõ thì bấm **Cần trao đổi thêm**

---

<!-- layout: agenda -->
## Nội dung
1. **Vé cầu đường, VETC** — giao dịch VETC, tránh trạm, danh mục trạm, hoá đơn tổng (7 câu)
2. **Kẹt xe, nổ máy, bù dầu** — xếp hàng ở cảng, kẹt cứng, nhắc tắt máy, định mức (4 câu)
3. **Dầu, cảm biến** — dữ liệu EUP, đối soát dầu thực đổ, vòi tự ngắt, bàn giao xe (6 câu)
4. **GPS và Lệnh** — mất GPS, đổi xe, ghép container, km, xe chạy ngoài Lệnh, bản đồ (8 câu)
5. **Ngưỡng, quy mô, kỳ, rủi ro** — các con số, quy mô đội xe, kỳ báo cáo, rủi ro (5 câu)

---

<!-- layout: section -->
## Vé cầu đường, VETC

---

<!-- layout: oq; id: td-OQ-49; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/vis/transport-dispatch.md; group: Vé cầu đường, VETC -->
## VETC có gửi từng giao dịch trừ tiền về ngay khi xe qua trạm không?

> Ba chỗ trong tài liệu cùng một ý: phần mềm gọi VETC một lần khi xe vào vùng điểm đích, tức lúc kết thúc Lệnh, để lấy các giao dịch trong khung giờ của Lệnh. Còn chưa rõ VETC có tự gửi từng giao dịch về ngay khi trừ tiền không. Công văn VETC ngày 02/09/2026 là ảnh chụp, đội chưa đọc được nội dung. Đội thiết kế chạy được cả hai cách; câu trả lời quyết định lúc nào điều vận thấy tiền vé và biết lái xe tránh trạm.

**Tài liệu:** VIS (08/10/2026), mục 2.2.6 Giám sát lộ trình và ghi nhận tránh trạm vé, mục 3.1.3 Bước 2; SIM & VIS — Công tác chuẩn bị (11/10/2026), mục 3.4 Thu phí tự động VETC
**Trích dẫn:** "Tại thời điểm xe kết thúc Lệnh vận tải, Delta MIS tự động gọi API sang hệ thống VETC để thu thập toàn bộ danh sách giao dịch trừ tiền phát sinh của phương tiện đó trong đúng khung thời gian thực hiện Lệnh vận tải" — VIS, mục 3.1.3 Bước 2
**Trích dẫn:** "gọi API VETC ngay tại thời điểm xe kích hoạt Geofence điểm đích (kết thúc Lệnh vận tải)" — Công tác chuẩn bị, mục 3.4

### A. Có, VETC gửi ngay khi trừ tiền
Phần mềm khớp vé từng trạm lúc xe đang chạy; tránh trạm vẫn chốt khi Lệnh hết chạy
+ Điều vận thấy tiền vé trên Lệnh ngay
+ Biết sớm xe đã qua trạm nào
- Phụ thuộc VETC gửi đều, đúng giờ

### B. Không, chỉ tra được theo xe trong một khung giờ
Phần mềm khớp một lần khi xe vào vùng điểm cuối
+ Đúng như tài liệu VIS mô tả
- Tiền vé và tránh trạm chỉ hiện sau khi xe chạy xong

**Nếu chưa rõ:** bấm Cần trao đổi thêm, đội cùng Delta hỏi VETC
**Ảnh hưởng:** lúc nào tiền vé hiện trên Lệnh; lúc nào biết lái xe tránh trạm

::: notes
- Nguồn: bản nháp transport-dispatch OQ-49 + I7. VIS 2.2.6 ý 3 ("Khi xe kích hoạt Geofence điểm đích…") và 3.1.3 Bước 2; Công tác chuẩn bị 3.4 đồng nhất "Geofence điểm đích (kết thúc Lệnh vận tải)".
- Công văn VETC 02/09/2026: docs-input/tich-hop/vetc-api-cong-van-2026-09-02/ (ảnh scan, BL-006 chưa gõ lại chữ).
- User yêu cầu: câu VETC tức thời phải nêu hệ quả từng đáp án. Không đề xuất: câu hỏi sự thật.
:::

---

<!-- layout: oq; id: td-OQ-50.1; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/vis/transport-dispatch.md; recommend: A; group: Vé cầu đường, VETC -->
## Trạm lái xe tránh có được xử lý ngay khi duyệt từng Lệnh không?

> VIS nói phần mềm tự ghi lái xe "Tránh trạm vé / Sai lộ trình" và đưa vào bảng kê, chưa nói ai xem lại và khi nào. Có lúc xe đi đường khác vì lý do chính đáng: điều vận đã cho đổi cung đường, đường cấm, tai nạn. Đội đề xuất: khi duyệt Lệnh, người duyệt xử lý từng trạm bị ghi tránh hoặc ngoài cung đường bằng "Tính cho lái xe" hoặc "Chấp nhận" kèm lý do; còn trạm chưa xử lý thì chưa duyệt được Lệnh. Kết quả thành bảng kê tránh trạm theo lái xe mỗi kỳ cho bộ phận lương.

**Tài liệu:** VIS (08/10/2026), mục 3.1.3 Bước 3 Phân loại dữ liệu và lập Bảng kê "Lái xe tránh trạm vé"
**Trích dẫn:** "Hệ thống tự động ghi nhận lái xe "Tránh trạm vé / Sai lộ trình", đồng thời đẩy thông tin vào Bảng kê tránh trạm vé." — VIS, mục 3.1.3 Bước 3

### A. Chốt theo từng Lệnh khi duyệt
+ Xử lý khi chuyến còn mới, dễ hỏi lại lái xe
+ Bảng kê cuối kỳ đã có lý do từng trạm
- Người duyệt Lệnh thêm một bước

### B. Chốt cuối kỳ theo bảng kê
+ Duyệt Lệnh nhanh hơn
- Dồn việc cuối kỳ, khó nhớ lý do từng chuyến

**Ảnh hưởng:** màn duyệt Lệnh, bảng kê tránh trạm gửi bộ phận lương
**Vì sao đề xuất A:** chỉ người duyệt Lệnh biết đã cho đổi cung đường hay chưa; xử lý dồn cuối kỳ dễ tính oan cho lái xe

::: notes
- Nguồn: bản nháp transport-dispatch OQ-50 (ý 1) + I8. Review VIS r14 (đồng ý): phần chặn duyệt Lệnh khi còn trạm chưa xử lý cân nhắc thành cấu hình.
:::

---

<!-- layout: oq; id: td-OQ-50.2; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/vis/transport-dispatch.md; group: Vé cầu đường, VETC -->
## Tiền vé của trạm lái xe tránh được tính thế nào với lương lái xe?

> Sơ đồ VIS ghi "vé tránh trạm, trả vào lương lái xe" nhưng chưa rõ là trừ hay cộng. Thư đề xuất GPS năm 2025 cho thấy hiện nay vé lái xe trốn được ghi vào thu nhập chịu thuế của lái xe. Nay vé trừ tự động vào tài khoản VETC của công ty, lái xe không cầm tiền vé, nên cần chốt lại cách tính.

**Tài liệu:** VIS (08/10/2026), mục 3.1.1 Sơ đồ kiến trúc và luồng dữ liệu; Đề xuất phát triển tiện ích mới cho thiết bị GPS (25/9/2025), mục 1 Đầu kéo và Xe tải
**Trích dẫn:** "Vé tránh trạm, trả vào lương lái xe." — VIS, ghi chú sơ đồ mục 3.1.1
**Trích dẫn:** "việc lái xe trốn vé cầu đường và công ty phải ghi nhận những vé không phải trả để đưa vào thu nhập chịu thuế hàng tháng của lái xe" — Đề xuất tiện ích GPS, mục 1

### A. Trừ vào lương lái xe
Coi là vi phạm sai lộ trình
+ Răn đe việc tránh trạm
- Cần quy chế nội bộ cho phép trừ lương

### B. Cộng vào lương, tính thu nhập chịu thuế
Như cách đang làm theo thư 2025
+ Giữ cách hạch toán hiện nay
- Có thể khuyến khích lái xe tránh trạm

### C. Không tính tiền, chỉ ghi vi phạm
+ Đơn giản, không động tới lương
- Không có chế tài

**Ảnh hưởng:** bảng kê tránh trạm gửi bộ phận lương, quy chế lương lái xe

::: notes
- Nguồn: bản nháp transport-dispatch OQ-50 (ý 2). Thư GPS 25/9/2025 = SRC-26. Quy chế cho phép tính tiền vào lương: hỏi chung ở câu rủi ro (vt-OQ-10).
- Không đề xuất: chính sách lương của Delta.
:::

---

<!-- layout: oq; id: td-OQ-51; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/vis/transport-dispatch.md; recommend: A; group: Vé cầu đường, VETC -->
## VETC vẫn chưa trả dữ liệu sau lần tra lại 120 phút: có cho duyệt Lệnh không?

> VIS nêu: xe đã qua trạm theo GPS mà VETC chưa trả giao dịch thì 120 phút sau tra lại. Tài liệu chưa nói tra lại vẫn chưa có thì làm gì. Đội đề xuất vẫn cho duyệt Lệnh, trạm đó ghi "Chờ VETC" và được kiểm nốt khi đối soát hoá đơn tổng VETC cuối kỳ.

**Tài liệu:** VIS (08/10/2026), mục 3.1.3 Bước 3 và Bước 4 Đối soát hóa đơn cuối kỳ
**Trích dẫn:** "Thiết lập cơ chế tự động quét lại sau 120 phút đối với các trường hợp GPS báo "Đã qua" nhưng VETC chưa trả về dữ liệu giao dịch để loại trừ độ trễ đồng bộ của bên thứ ba." — VIS, mục 3.1.3 Bước 3

### A. Cho duyệt, trạm ghi "Chờ VETC"
Kiểm nốt khi đối soát hoá đơn tổng cuối kỳ
+ Lệnh, chi phí lên JobID không bị treo vì lỗi bên ngoài
- Vài vé lên Lệnh muộn, sau đối soát cuối kỳ

### B. Chưa cho duyệt tới khi VETC trả dữ liệu
+ Lệnh đã duyệt là đủ tiền vé
- Lệnh có thể treo không rõ bao lâu

**Ảnh hưởng:** duyệt Lệnh, đối soát hoá đơn VETC cuối kỳ
**Vì sao đề xuất A:** chậm trễ là của VETC, không nên giữ Lệnh và chi phí của cả chuyến; cuối kỳ vẫn kiểm lại đủ

::: notes
- Nguồn: bản nháp transport-dispatch OQ-51 + I7 (tham số tra lại 120 phút).
:::

---

<!-- layout: oq; id: vt-OQ-3; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/vis/vehicle-telematics.md; group: Vé cầu đường, VETC -->
## VETC có cung cấp được danh mục trạm thu phí (toạ độ, giá vé theo loại xe) không?

> Để biết xe qua trạm hay tránh trạm, mỗi trạm cần toạ độ chuẩn, vùng bao đoạn đường phải qua theo từng chiều và giá vé theo loại xe. Đội đề xuất làm một danh mục trạm dùng chung, đội sản phẩm duy trì, Delta không phải tự vẽ. Ngày 09/10 Delta đã chọn VETC là nguồn chuẩn về toạ độ và chi phí đường bộ, nên VETC là nguồn ban đầu tốt nhất.

**Tài liệu:** VIS (08/10/2026), mục 2.2.6 Giám sát lộ trình và ghi nhận tránh trạm vé; trao đổi với Delta ngày 09/10/2026, mục 4 Dữ liệu và chứng từ
**Trích dẫn:** "cần xác định tọa độ chuẩn của trạm vé lên danh mục trạm vé để thực hiện nhiệm vụ này" — VIS, mục 2.2.6
**Trích dẫn:** "Dữ liệu từ Vietmap và VETC đang lệch nhau về toạ độ và chi phí, cần thống nhất nguồn chuẩn -> VETC." — bản tổng hợp trao đổi 09/10/2026

### A. VETC cung cấp được
Delta xin VETC danh sách trạm, toạ độ, giá theo loại xe
+ Đúng nguồn chuẩn Delta đã chọn
- Cần Delta làm việc với VETC

### B. VETC không cung cấp
Đội sản phẩm tự dựng danh mục, Delta kiểm các trạm hay đi
+ Không phải chờ VETC
- Delta mất thời gian kiểm danh mục

**Ảnh hưởng:** danh mục trạm thu phí, phát hiện tránh trạm, dự toán vé khi lập Lệnh

::: notes
- Nguồn: bản nháp vehicle-telematics OQ-3 + T1 (danh mục dùng chung, DEC-101). Biên bản docs/meetings/2026-10-09-client-dispatch-field-issues.md mục 4.
- Không đề xuất: câu hỏi sự thật.
:::

---

<!-- layout: oq; id: vt-OQ-7; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/vis/vehicle-telematics.md; recommend: A; group: Vé cầu đường, VETC -->
## Ba trường hợp vé bất thường dưới đây xử lý theo đề xuất của đội được không?

> VIS mới nói vé không gắn được vào Lệnh nào thì chuyển kế toán xử lý. Ba trường hợp sau chưa có trong tài liệu; đội đề xuất phần mềm tự nhận ra và xử lý như sau:

**Tài liệu:** VIS (08/10/2026), mục 3.1.3 Quy trình đối soát và quản lý chi phí trên Delta MIS; ba trường hợp chưa có trong tài liệu Delta gửi
**Trích dẫn:** "Lập báo cáo các vé phát sinh ngoài lộ trình, hệ thống không ghi nhận vào đâu, để chuyển cho kế toán xử lý." — VIS, mục 3.1.3

- Trạm chưa có trong danh mục: vẫn ghi tiền theo giao dịch, đánh dấu "Trạm chưa có trong danh mục", báo bổ sung danh mục
- Thẻ thu phí gắn nhầm xe: lúc trừ tiền, GPS của xe ở nơi khác thì không ghi vào Lệnh, cảnh báo "nghi gắn nhầm thẻ"
- Trừ trùng: hai giao dịch cùng xe, cùng trạm cách vài phút thì ghi một lượt, lượt kia đánh dấu "nghi trừ trùng" để kế toán khiếu nại

### A. Đồng ý cả 3 đề xuất
+ Vé lạ không thành vé không rõ chủ cuối kỳ
+ Có căn cứ khiếu nại VETC
- Thêm danh sách cảnh báo cho kế toán

### B. Không phân loại, chuyển hết cho kế toán
+ Đơn giản
- Kế toán tự dò từng giao dịch

**Ảnh hưởng:** đối soát vé, danh sách việc của kế toán
**Vì sao đề xuất A:** phần mềm đã có GPS và danh mục trạm nên nhận ra được 3 trường hợp này; kế toán chỉ cần xử lý chỗ bị đánh dấu

::: notes
- Nguồn: bản nháp vehicle-telematics OQ-7 + T2, G3, G4 (đều [Mới]; review r17 đánh dấu "hoãn được nếu trễ go-live").
:::

---

<!-- layout: oq; id: td-OQ-47.1; src: docs/transport-dispatch/brainstorms/transport-dispatch.md; group: Vé cầu đường, VETC -->
## Hoá đơn tổng VETC cuối kỳ có đi qua phần thu thập hoá đơn đầu vào như hoá đơn thường không?

> Cuối kỳ phần mềm đối soát hoá đơn tổng VETC với GPS, gợi ý cho kế toán giao dịch nào phát sinh ngoài Lệnh để duyệt hoặc xử lý lái xe. Tài liệu SIM có phần thu thập hoá đơn đầu vào (đọc, định danh, gắn vào JobID). Chưa rõ hoá đơn tổng VETC có đi qua phần đó không, và ai duyệt các giao dịch ngoài Lệnh.

**Tài liệu:** VIS (08/10/2026), mục 3.1.3 Bước 4 Đối soát hóa đơn cuối kỳ; SIM (12/10/2026), mục 3.3 Thu thập & định danh hóa đơn đầu vào (IIP); Đề xuất tiện ích GPS (25/9/2025), mục 1
**Trích dẫn:** "Hệ thống tự động đưa ra gợi ý xử lý cho kế toán xác định chính xác giao dịch đó thuộc xe nào, phát sinh ngoài lệnh trong khung giờ nào, tại trạm nào để phê duyệt chi phí hợp lý hoặc xử lý sai phạm của lái xe" — VIS, mục 3.1.3 Bước 4
**Trích dẫn:** "Hàng tháng Delta đang phải hạch toán hàng ngàn vé xe vào các Lệnh vận chuyển cho gần 200 đầu xe." — Đề xuất tiện ích GPS, mục 1

### A. Có, qua phần thu thập hoá đơn đầu vào
Ghép hoá đơn tổng với vé đã ghi trên từng Lệnh
+ Một nơi quản lý mọi hoá đơn đầu vào, đối chiếu theo JobID
- Hoá đơn tổng gồm hàng ngàn vé của gần 200 đầu xe

### B. Không, kế toán xử lý riêng
Dùng bảng đối soát của VIS
+ Kế toán làm như hiện nay
- Hoá đơn VETC nằm ngoài luồng hoá đơn đầu vào chung

**Ghi thêm:** ai duyệt các giao dịch phát sinh ngoài Lệnh
**Ảnh hưởng:** việc của kế toán cuối kỳ, chi phí vé trên JobID

::: notes
- Nguồn: repo transport-dispatch.md Mục 11 OQ-47 ý (1) (BL-120). Ý (3) chi phí trên Lệnh chuyển sang SIM: đội tự quyết, không hỏi khách.
- Không đề xuất.
:::

---

<!-- layout: section -->
## Kẹt xe, nổ máy, bù dầu

---

<!-- layout: oq; id: td-OQ-52; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/vis/transport-dispatch.md; group: Kẹt xe, nổ máy, bù dầu -->
## Xe xếp hàng chờ ở cổng cảng, bãi, kho quá 10 phút mà máy vẫn nổ: có bù dầu như kẹt xe không?

> VIS dùng ngưỡng 10 phút để bỏ qua dừng đèn đỏ và check-in ở cổng cảng. Thực tế xe có thể xếp hàng ở cổng cảng, bãi, kho lâu hơn 10 phút mà máy vẫn nổ, nhích dưới 5 km/h. Theo cách tính của VIS, khoảng đó sẽ thành kẹt xe và được đề xuất bù dầu; cần Delta chốt có bù cho trường hợp này không.

**Tài liệu:** VIS (08/10/2026), mục 3.2 Bước 1 Ghi nhận sự kiện kích hoạt trạng thái "Traffic jam"
**Trích dẫn:** "Trạng thái này phải duy trì liên tục trên 10 phút để hệ thống tự động loại trừ các biến cố dừng đèn đỏ hoặc dừng check-in tại cổng cảng." — VIS, mục 3.2 Bước 1

### A. Có, bù như kẹt xe
+ Lái xe không chịu thiệt khi cảng ùn
- Số lít bù tăng, nhất là ở cảng hay ùn

### B. Không bù khi xe ở trong vùng cảng, bãi, kho
+ Đúng ý loại trừ dừng ở cổng cảng của VIS
- Lái xe chịu phần dầu khi cảng ùn lâu

**Ảnh hưởng:** đề xuất bù dầu kẹt xe trên Lệnh

::: notes
- Nguồn: bản nháp transport-dispatch OQ-52 + I4 (bật/tắt bù dầu xếp hàng theo khách). Không đề xuất.
:::

---

<!-- layout: oq; id: td-OQ-53; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/vis/transport-dispatch.md; recommend: A; group: Kẹt xe, nổ máy, bù dầu -->
## Tai nạn, kẹt cứng làm xe đứng yên hẳn: có tính là kẹt xe (được bù dầu) không?

> Theo VIS, xe nhích dưới 5 km/h là kẹt xe (được bù dầu), còn đứng yên hẳn khi máy nổ là nổ máy ngủ (không bù). Khi tai nạn hay kẹt cứng, xe đứng yên hẳn dù lái xe không có lỗi. Đội đề xuất: khoảng đứng yên vẫn tính là kẹt xe khi có ít nhất 1 dấu hiệu — nằm giữa hai đoạn kẹt xe gần nhau; lái xe đã báo sự cố giữa chặng trên app; hoặc bản đồ báo tắc, sự cố tại đó. Trạm dừng nghỉ, cây xăng không xét.

**Tài liệu:** VIS (08/10/2026), mục 2.2.3 Thời gian xe di chuyển dưới 5 km/h và mục 2.2.4 Thời gian nổ máy không di chuyển
**Trích dẫn:** "Điều kiện kích hoạt: Khi nhận Event vận tốc < 5 km/h từ EUP và trạng thái máy hoạt động." — VIS, mục 2.2.3
**Trích dẫn:** "Điều kiện Idling là Nổ máy và Speed = 0 trong thời gian quá 10 phút." — VIS, mục 2.2.4

### A. Tính kẹt xe khi có 1 trong 3 dấu hiệu
+ Lái xe không chịu thiệt khi kẹt cứng
+ Vẫn có căn cứ, không tính tràn lan
- Cần chốt khoảng tối đa giữa hai đoạn kẹt (câu 26)

### B. Theo đúng VIS
Đứng yên hẳn là nổ máy ngủ, không bù
+ Đơn giản
- Lái xe chịu dầu khi tai nạn, kẹt cứng

**Ảnh hưởng:** phân loại kẹt xe và nổ máy ngủ, đề xuất bù dầu trên Lệnh
**Vì sao đề xuất A:** kẹt cứng là lúc lái xe thiệt nhất mà không có lỗi; 3 dấu hiệu đều có dữ liệu kiểm được

::: notes
- Nguồn: bản nháp transport-dispatch OQ-53 + vehicle-telematics S4.
:::

---

<!-- layout: oq; id: vt-OQ-5; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/vis/vehicle-telematics.md; group: Kẹt xe, nổ máy, bù dầu -->
## Có muốn phần mềm nhắc lái xe tắt máy trên app khi xe nổ máy đứng yên quá 10 phút không?

> VIS ghi nhận thời gian nổ máy không di chuyển (ví dụ bật điều hoà ngủ) và tổng hợp theo lái xe cuối kỳ. Đội có thể nhắc ngay trên app để lái xe tắt máy trước khi thành hao phí. Đây là đề xuất mới, không có trong VIS.

**Tài liệu:** VIS (08/10/2026), mục 2.2.4 Thời gian nổ máy không di chuyển và mục 3.4 Bước 3
**Trích dẫn:** "ghi nhận thời gian nổ máy không di chuyển để quản trị hao phí nhiên liệu vô ích (Tài xế dừng chờ bật điều hòa ngủ, không tắt máy xe)" — VIS, mục 2.2.4
**Trích dẫn:** "Dữ liệu được tổng hợp vào bảng tổng hợp Idling cuối kỳ theo từng lái xe." — VIS, mục 3.4 Bước 3

### A. Có, nhắc trên app
+ Giảm dầu đốt vô ích ngay lúc đó
- Lái xe có thể thấy phiền khi đang chờ bốc hàng

### B. Không, chỉ báo cáo cuối kỳ
+ Đúng như VIS mô tả
- Chỉ biết sau khi dầu đã tốn

**Ảnh hưởng:** thông báo trên app lái xe

::: notes
- Nguồn: bản nháp vehicle-telematics OQ-5 + S10 ([Mới], review r17 hoãn được). Không đề xuất.
:::

---

<!-- layout: oq; id: vt-OQ-12; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/vis/vehicle-telematics.md; group: Kẹt xe, nổ máy, bù dầu -->
## Định mức dầu khi máy nổ mà xe không chạy (lít/giờ): dùng chung cho kẹt xe và nổ máy ngủ được không?

> Hai mục của VIS dùng hai tên định mức: "khi nổ máy chờ" để tính dầu bù kẹt xe và "Idling" để tính dầu hao phí nổ máy ngủ, cùng đơn vị lít/giờ theo loại xe. Chưa rõ định mức này đã có số chưa và bộ phận nào đặt.

**Tài liệu:** VIS (08/10/2026), mục 3.2 Bước 3 và mục 3.4 Bước 3
**Trích dẫn:** "Delta MIS gọi bảng Định mức tiêu hao khi nổ máy chờ của loại xe đó trong danh mục để tính ra số lít dầu" — VIS, mục 3.2 Bước 3
**Trích dẫn:** "Delta MIS gọi Định mức tiêu hao dầu Idling (lít/giờ) tương ứng với từng loại xe trong danh mục hệ thống" — VIS, mục 3.4 Bước 3

### A. Dùng chung một định mức
Cho cả kẹt xe và nổ máy ngủ
+ Một bảng, dễ duy trì
- Nhích chậm có thể tốn dầu hơn đứng yên

### B. Hai định mức riêng
+ Sát thực tế hơn
- Thêm một bảng phải duy trì

**Ghi thêm:** định mức đã có số chưa, bộ phận nào đặt
**Ảnh hưởng:** dầu bù kẹt xe trên Lệnh, báo cáo dầu nổ máy ngủ

::: notes
- Nguồn: bản nháp vehicle-telematics OQ-12 (chuyển fuel-allowance khi lập feature). Không đề xuất.
:::

---

<!-- layout: section -->
## Dầu, cảm biến

---

<!-- layout: oq; id: vt-OQ-2; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/vis/vehicle-telematics.md; group: Dầu, cảm biến -->
## Dữ liệu từ EUP: nhờ Delta (hoặc EUP) trả lời 4 ý dưới đây

> Khi xe tắt máy, phần mềm chỉ đọc mức dầu 30–60 phút một lần, nên ngưỡng "giảm 5 lít trong dưới 3 phút" không kiểm được: hút dầu lúc xe đậu bãi tắt máy có thể lọt. Lái xe thường tắt máy khi đổ dầu nên cũng có thể không bắt được sự kiện đổ dầu. Nếu EUP không báo các sự kiện này khi xe tắt máy, đội sẽ so hai lần đọc liền nhau: giảm quá ngưỡng thì nghi hút dầu, tăng quá ngưỡng thì ghi đổ dầu.

**Tài liệu:** VIS (08/10/2026), mục 2.2 Quy trình xử lý chi tiết, mục 3.5 Bước 1–2; SIM & VIS — Công tác chuẩn bị (11/10/2026), mục 3.3 Giám sát hành trình EUP
**Trích dẫn:** "Delta MIS chỉ chủ động quét (polling) với tần suất thấp (30-60 phút) khi xe tắt máy để kiểm tra dầu tồn." — VIS, mục 2.2
**Trích dẫn:** "Nếu EUP có thể cung cấp đầy đủ dữ liệu để Delta MIS cảnh báo hành vi hút dầu … thì dùng trực tiếp dữ liệu của EUP." — VIS, mục 3.5

1. Khi trạng thái xe đổi, EUP có gửi sự kiện ngay không? Khi xe chạy, mấy giây gửi vị trí một lần?
2. Khi xe tắt máy, EUP có gửi sự kiện hút dầu, đổ dầu không?
3. EUP có sẵn cảnh báo hút dầu và báo cáo lượng dầu bị hút để dùng thẳng không?
4. Ngưỡng hút dầu 5 lít trong 3 phút, đổ dầu 20 lít trong 10 phút đã thống nhất với EUP chưa?

**Ảnh hưởng:** cách phát hiện hút dầu, đổ dầu; cảnh báo đến sớm hay muộn

::: notes
- Nguồn: bản nháp vehicle-telematics OQ-2 + K1, S6, S7; review VIS r1 (chọn "Hỏi khách"): hút/đổ dầu khi xe tắt máy, đề xuất so 2 lần đọc (tham số ngưỡng hút/đổ khi tắt máy chưa chốt).
- Ý 1 gần với repo OQ-48 (câu khoảng hở GPS ở nhóm 4).
:::

---

<!-- layout: oq; id: vt-OQ-11; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/vis/vehicle-telematics.md; group: Dầu, cảm biến -->
## Mục 3.6 Đối soát lượng dầu thực đổ có thuộc phạm vi giai đoạn 1 không?

> Mục lục tài liệu VIS dừng ở mục 3.5, nhưng thân tài liệu có thêm mục 3.6: so số lít trên phiếu cấp dầu với số lít cảm biến ghi nhận thực đổ vào bình, lệch thì đưa vào bảng kê nghi vấn. Đội đang đưa mục này vào giai đoạn 1.

**Tài liệu:** VIS (08/10/2026), mục lục và mục 3.6 Quy trình đối soát lượng dầu thực đổ
**Trích dẫn:** "Mục tiêu của quy trình này là tự động so khớp chéo giữa lượng dầu cấp cho xe bằng phiếu cấp dầu với lượng dầu thực tế đổ vào bình do sensor dầu EUP ghi nhận" — VIS, mục 3.6

### A. Có, thuộc giai đoạn 1
+ Phát hiện đổ thiếu, gian lận phiếu dầu ngay từ đầu
- Cần cảm biến đo chuẩn và các dung sai (câu 14)

### B. Để giai đoạn sau
+ Giai đoạn 1 gọn hơn
- Chưa đối soát được dầu thực đổ

**Ảnh hưởng:** phạm vi giai đoạn 1, báo cáo đối soát nhiên liệu

::: notes
- Nguồn: bản nháp vehicle-telematics OQ-11 (= BL-045 ý c). Không đề xuất.
:::

---

<!-- layout: oq; id: vt-OQ-13; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/vis/vehicle-telematics.md; group: Dầu, cảm biến -->
## Đối soát dầu thực đổ: nhờ cho 4 con số dưới đây

> VIS nói phần mềm so phiếu cấp dầu với số lít cảm biến ngay khi đổ dầu xong, nhưng chưa nêu lệch bao nhiêu thì vẫn coi là khớp. Thiếu các số này, phần mềm sẽ báo lệch cả những lần đổ bình thường. Số ước lượng cũng được, đội ghi là số tạm.

**Tài liệu:** VIS (08/10/2026), mục 3.6 Bước 1 và Bước 3
**Trích dẫn:** "Ngay khi sự kiện đổ dầu kết thúc, Delta MIS thực hiện lệnh so khớp tự động giữa dữ liệu cấp dầu hệ thống (Bước 2) và dữ liệu thực đổ từ sensor (Bước 1)" — VIS, mục 3.6 Bước 3

1. Sự kiện đổ dầu cách giờ phiếu cấp dầu tối đa bao lâu thì ghép với nhau?
2. Lệch bao nhiêu lít (hoặc %) giữa phiếu và cảm biến vẫn coi là khớp?
3. Thiếu bao nhiêu lít so với dung tích bình vẫn coi là đầy bình?
4. Chờ bao lâu sau khi đổ để cảm biến ổn định rồi mới đọc?

**Ảnh hưởng:** bảng kê nghi vấn lệch dầu, tranh chấp với cây dầu và lái xe

::: notes
- Nguồn: bản nháp vehicle-telematics OQ-13 (chuyển fuel-issuing khi lập feature).
:::

---

<!-- layout: oq; id: vt-OQ-14; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/vis/vehicle-telematics.md; recommend: A; group: Dầu, cảm biến -->
## Cây dầu nội bộ dừng bơm khi vòi tự ngắt, số lít lệch với cảm biến: xử lý theo đề xuất được không?

> Phiếu đổ đầy bình (dGas4) và phiếu chốt dầu (dGas5) ở cây dầu nội bộ thường dừng khi vòi tự ngắt, nên số lít có thể lệch với cảm biến. Đội đề xuất: lấy số lít trên iGAS làm căn cứ; chờ cảm biến ổn định; cảm biến cho thấy chưa đầy bình thì nhắc bơm bồi một lần; vẫn chưa đầy thì chốt theo số iGAS và ghi số lít còn thiếu.

**Tài liệu:** VIS (08/10/2026), mục 3.6 Bước 2; cách xử lý vòi tự ngắt chưa có trong tài liệu Delta gửi
**Trích dẫn:** "Delta MIS lấy dữ liệu từ phiếu cấp dầu điện tử hoặc dữ liệu cấp dầu của module xưởng bao gồm (1) số lít dầu được cấp theo định mức/kế hoạch (2) thời gian cấp và tên cây dầu cấp." — VIS, mục 3.6 Bước 2

### A. Đồng ý đề xuất
+ Không tranh cãi số lít khi vòi tự ngắt
+ Vẫn biết số lít còn thiếu để theo dõi
- Thêm một lần bơm bồi khi chưa đầy

### B. Lấy số cảm biến làm căn cứ
+ Đúng số dầu vào bình
- Cảm biến dao động ngay sau khi đổ, dễ lệch với cây dầu

**Ảnh hưởng:** phiếu đổ đầy bình, phiếu chốt dầu, đối soát dầu thực đổ
**Vì sao đề xuất A:** số iGAS là số cây dầu đã bơm thật, cảm biến cần thời gian ổn định; nhắc bơm bồi giữ được mục tiêu đầy bình

::: notes
- Nguồn: bản nháp vehicle-telematics OQ-14 (chuyển fuel-issuing; BL-152). iGAS: hệ thống cây dầu trong SRS ERP Delta 3.0 ("xin cấp mã Igas, ghi nhận bơm dầu").
:::

---

<!-- layout: oq; id: td-OQ-47.2; src: docs/transport-dispatch/brainstorms/transport-dispatch.md; recommend: A; group: Dầu, cảm biến -->
## Hoá đơn dầu lái xe mua ngoài có cần đối chiếu với số lít cảm biến dầu ghi nhận không?

> VIS mục 3.6 chỉ lấy dữ liệu từ phiếu cấp dầu để so với cảm biến, và cảnh báo khi dầu thực đổ nhiều hơn dầu được cấp. Dầu lái xe mua ngoài theo hoá đơn lẻ chưa nằm trong phần đối soát này. Ngày 09/10 Delta muốn lưu lượng dầu dư của dầu mua ngoài để làm căn cứ cấp bù.

**Tài liệu:** VIS (08/10/2026), mục 3.6 Bước 2–3; trao đổi với Delta ngày 09/10/2026, mục 3 Nhiên liệu
**Trích dẫn:** "Nếu dầu thực đổ (Sensor) > Dầu được cấp: Cảnh báo lái xe không dùng phiếu dầu để đổ hoặc có sự cố gian lận hóa đơn cấp dầu ngoài luồng." — VIS, mục 3.6 Bước 3
**Trích dẫn:** "Dầu mua ngoài theo hoá đơn lẻ: tính lượng dầu dư để làm căn cứ cấp bù" — bản tổng hợp trao đổi 09/10/2026

### A. Có, đối chiếu với cảm biến
So số lít trên hoá đơn với lần đổ dầu cảm biến ghi nhận
+ Phát hiện hoá đơn không khớp dầu thực đổ
+ Có số lít thật để tính dầu dư, cấp bù
- Hoá đơn không khớp lần đổ nào thì kế toán xử lý tay

### B. Không
Chỉ đối soát phiếu cấp dầu
+ Đối soát đơn giản hơn
- Dầu mua ngoài chỉ kiểm bằng hoá đơn

**Ảnh hưởng:** báo cáo đối soát dầu, căn cứ cấp bù dầu
**Vì sao đề xuất A:** dầu mua ngoài là chỗ dễ lệch nhất; cần số lít thật để tính dầu dư làm căn cứ cấp bù như Delta đã nêu

::: notes
- Nguồn: repo transport-dispatch.md Mục 11 OQ-47 ý (2). Biên bản 09/10 quyết định #5; brainstorm F6.
:::

---

<!-- layout: oq; id: vm-OQ-1; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/vis/vehicle-management.md; group: Dầu, cảm biến -->
## Bàn giao xe kèm phiếu đổ đầy bình, thu hồi xe kèm phiếu chốt dầu: thứ tự làm như đề xuất được không?

> Theo SRS hiện tại, phiếu đổ đầy bình (dGas4) hoàn thành thì mới tạo được bàn giao xe; phiếu chốt dầu (dGas5) hoàn thành thì mới tạo được thu hồi xe. Đội đề xuất giữ cặp phiếu – biên bản này, nhưng cho làm phiếu trước hay biên bản trước đều được; biên bản chỉ ký xong khi phiếu đi kèm đã xong.

**Tài liệu:** Tài liệu SRS - ERP Delta 3.0 (Web) (30/9/2026), bảng liên quy trình (Bàn giao phương tiện, Thu hồi phương tiện)
**Trích dẫn:** "Phiếu dGas 4 trường hợp Bàn giao PT — Phiếu cấp dầu được hoàn thành — Tạo bàn giao phương tiện với phương tiện tương ứng" — SRS ERP Delta 3.0, bảng liên quy trình

### A. Làm trước sau đều được, ký xong khi phiếu xong
+ Không phải chờ cây dầu mới lập được biên bản
+ Vẫn đủ phiếu trước khi giao xe
- Biên bản có thể nằm chờ phiếu

### B. Giữ như SRS hiện tại
Phiếu xong mới tạo được biên bản
+ Một thứ tự rõ ràng
- Không lập biên bản trước được

**Ghi thêm:** cách làm này có làm chậm việc giao xe không
**Ảnh hưởng:** màn bàn giao, thu hồi xe; phiếu đổ đầy bình, chốt dầu

::: notes
- Nguồn: bản nháp vehicle-management OQ-1 + B2. SRS lg-srs-export.md:1182-1190, 1383-1384 (bảng liên quy trình). Không đề xuất.
:::

---

<!-- layout: section -->
## GPS và Lệnh

---

<!-- layout: oq; id: td-OQ-54; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/vis/transport-dispatch.md; recommend: A; group: GPS và Lệnh -->
## Khi xe mất tín hiệu GPS, lái xe có phải chụp ảnh định vị tại từng mốc giao nhận không?

> Giờ đến thật tại cảng, bãi, kho dùng để tính quá mốc và phạt lưu container, lưu vỏ. Khi mất GPS, phần mềm không tự ghi được giờ đến. Đội đề xuất lái xe chụp ảnh định vị ngay tại từng mốc; ảnh tự mang giờ và vị trí, dùng thay cho giờ GPS.

**Tài liệu:** VIS (08/10/2026), mục 2.2.2 Thời gian xe đã đến (Geofencing); cách xử lý khi mất GPS chưa có trong tài liệu Delta gửi
**Trích dẫn:** "Chức năng này xác định thời gian xe đến các địa điểm giao nhận theo Lệnh vận tải và ghi nhận lên Lệnh vận tải." — VIS, mục 2.2.2

### A. Bắt chụp ảnh định vị tại từng mốc
+ Có giờ, vị trí làm bằng chứng như GPS
- Thêm thao tác cho lái xe khi mất sóng

### B. Lái xe chỉ bấm "đã đến"
+ Nhanh
- Không có bằng chứng giờ đến khi tranh chấp

**Ảnh hưởng:** giờ đến trên Lệnh, cảnh báo quá mốc
**Vì sao đề xuất A:** giờ đến là căn cứ tính phạt quá mốc; ảnh định vị cho bằng chứng tương đương GPS

::: notes
- Nguồn: bản nháp transport-dispatch OQ-54 (6.4 dòng 2).
:::

---

<!-- layout: oq; id: td-OQ-55; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/vis/transport-dispatch.md; group: GPS và Lệnh -->
## Bỏ mooc giữa đường rồi điều xe khác ra kéo tiếp: phần còn lại chạy trên cùng Lệnh hay Lệnh mới?

> Ngày 09/10 Delta cho biết trường hợp hiếm phải bỏ mooc giữa đường thì điều xe khác ra kéo tiếp. Từ lúc đó, GPS, vé cầu đường, kẹt xe thuộc đầu kéo mới. Đội cần biết phần còn lại thuộc Lệnh nào để gắn đúng dữ liệu và chi phí. Nếu còn trường hợp đổi xe giữa chặng khác, nhờ ghi vào ô ý kiến.

**Tài liệu:** chưa có trong tài liệu Delta gửi (trao đổi ngày 09/10/2026, mục 2 Mooc)
**Trích dẫn:** "Trường hợp hiếm phải bỏ mooc giữa đường: điều xe khác ra kéo tiếp." — bản tổng hợp trao đổi 09/10/2026

### A. Cùng Lệnh, đổi xe giữa chặng
Trước giờ đổi gắn xe cũ, sau giờ đổi gắn xe mới; vé tra theo khung giờ từng xe
+ Một chuyến hàng một Lệnh, chi phí không bị tách
- Một Lệnh có hai xe, hai lái xe

### B. Lệnh mới cho xe kéo tiếp
+ Mỗi Lệnh một xe, dễ theo dõi
- Một chuyến hàng tách thành hai Lệnh

**Ảnh hưởng:** Lệnh vận tải, dữ liệu GPS và chi phí theo xe

::: notes
- Nguồn: bản nháp transport-dispatch OQ-55 ("Có trường hợp đổi xe giữa chặng không?") — viết lại theo F5 biên bản 09/10 (Delta đã nói có, hi hữu). Đề xuất xử lý trong bản nháp 6.5 = phương án A. Không đề xuất.
:::

---

<!-- layout: oq; id: td-OQ-56; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/vis/transport-dispatch.md; group: GPS và Lệnh -->
## Có trường hợp một xe chở 2 container 20 feet thuộc 2 Lệnh khác nhau không?

> Nếu có, khoảng đường hai Lệnh chạy chung sinh kẹt xe, vé cầu đường cho cả hai. Đội đề xuất chia đều kẹt xe và vé trong khoảng chạy chung cho 2 Lệnh; dầu bù đi tìm vỏ chỉ tính cho Lệnh có bãi nhận vỏ đó.

**Tài liệu:** chưa có trong tài liệu Delta gửi

### A. Không có trường hợp này

### B. Có, chia đều như đề xuất
+ Đơn giản, công bằng giữa 2 Lệnh
- Có thể chưa sát nếu 2 Lệnh khác quãng đường

**Ghi thêm:** nếu có mà muốn chia cách khác, ghi cách chia
**Ảnh hưởng:** kẹt xe, vé, dầu bù trên từng Lệnh

::: notes
- Nguồn: bản nháp transport-dispatch OQ-56 (6.5). Không đề xuất: câu hỏi sự thật.
:::

---

<!-- layout: oq; id: td-OQ-48; src: docs/transport-dispatch/brainstorms/transport-dispatch.md; group: GPS và Lệnh -->
## Hai lần ghi vị trí của xe cách nhau quá bao lâu thì coi là thiếu dữ liệu, không kết luận lái xe tránh trạm?

> Thiết bị trên xe gửi vị trí theo từng khoảng thời gian. Phần mềm xét cả điểm GPS lẫn đoạn nối hai điểm liền nhau có cắt vùng trạm không, để bắt xe chạy nhanh qua trạm. Nếu khoảng hở quá dài, xe có thể đi đường khác mà phần mềm không biết. Khi đó trạm mang cờ "Thiếu dữ liệu GPS" và chờ đối soát VETC, thay vì ghi lỗi cho lái xe. Nhờ ghi số phút (hoặc số km).

**Tài liệu:** VIS (08/10/2026), mục 2.2.6 Giám sát lộ trình và ghi nhận tránh trạm vé
**Trích dẫn:** "Trạm vé trên danh mục phải được vẽ dưới dạng hình đa giác (Polygon geofence) bao trọn đoạn đường phải qua của trạm, thay vì bán kính tròn (Radius) để tránh bắt hụt sự kiện." — VIS, mục 2.2.6

**Ảnh hưởng:** kết luận tránh trạm, bảng kê tránh trạm

::: notes
- Nguồn: repo transport-dispatch.md Mục 11 OQ-48 + E10 (tham số khoảng GPS tối đa).
:::

---

<!-- layout: oq; id: vm-OQ-2; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/vis/vehicle-management.md; recommend: A; group: GPS và Lệnh -->
## Ký biên bản bàn giao, thu hồi xe mà GPS không có dữ liệu lúc đó: lấy số km nào?

> Hiện biên bản thu hồi cho người dùng tự nhập số km của xe. Đội đề xuất km trên biên bản bàn giao, thu hồi lấy từ GPS lúc ký, không sửa tay, để không khai sai km. Cần chốt trường hợp lúc ký GPS không có dữ liệu.

**Tài liệu:** Tài liệu SRS - ERP Delta 3.0 (Web) (30/9/2026), phần Thu hồi phương tiện (ô KMs thu hồi)
**Trích dẫn:** "Cho phép người dùng nhập số kms hiện tại của phương tiện thu hồi. Chỉ cho phép nhập số dương" — SRS ERP Delta 3.0, ô KMs thu hồi

### A. Lấy lần đọc GPS gần nhất, ghi kèm giờ đọc
+ Km không sửa tay được
+ Giờ đọc cho biết số liệu cũ bao lâu
- Có thể lệch vài km nếu xe đã chạy sau lần đọc đó

### B. Cho người bàn giao nhập tay km đồng hồ
+ Đúng số trên đồng hồ xe
- Quay lại nhập tay, khó kiểm

**Ảnh hưởng:** biên bản bàn giao, thu hồi; km của xe dùng cho định mức
**Vì sao đề xuất A:** giữ nguyên tắc km chỉ lấy từ GPS; giờ đọc đi kèm giúp người ký biết số km cũ đến đâu

::: notes
- Nguồn: bản nháp vehicle-management OQ-2 + B4. SRS lg-srs-export.md:34432.
:::

---

<!-- layout: oq; id: vm-OQ-3; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/vis/vehicle-management.md; recommend: A; group: GPS và Lệnh -->
## Xe không có Lệnh mà vẫn di chuyển: những trường hợp nào không cần cảnh báo?

> VIS nhắc xe chạy ngoài lịch trình, việc riêng. Đội đề xuất cảnh báo ngay khi xe không có Lệnh mà di chuyển quá một ngưỡng, trừ 5 trường hợp đã có chứng từ:

**Tài liệu:** VIS (08/10/2026), mục 3.1.3 Bước 4 Đối soát hóa đơn cuối kỳ
**Trích dẫn:** "phê duyệt chi phí hợp lý hoặc xử lý sai phạm của lái xe (chạy xe ngoài lịch trình, việc riêng)" — VIS, mục 3.1.3 Bước 4

- (1) Lệnh đã nhận, xe đang tới điểm đầu · (2) Về bãi sau khi xong Lệnh · (3) Đi đổ dầu khi có phiếu cấp dầu đang mở
- (4) Đi xưởng khi có lệnh sửa chữa đang mở · (5) Đang bàn giao xe giữa các chi nhánh

### A. Miễn cả 5 trường hợp
+ Chỉ cảnh báo xe đi không có lý do
- Phiếu, lệnh phải được mở đúng lúc

### B. Chỉ miễn một số
Ghi số thứ tự các trường hợp được miễn vào ô ý kiến

**Ghi thêm:** đi bao xa (km) hoặc bao lâu (phút) thì cảnh báo
**Ảnh hưởng:** cảnh báo xe chạy ngoài Lệnh cho quản lý phương tiện
**Vì sao đề xuất A:** cả 5 trường hợp đều có chứng từ chứng minh lý do di chuyển

::: notes
- Nguồn: bản nháp vehicle-management OQ-3 + V2; vehicle-telematics S8 (ngưỡng chạy ngoài Lệnh chưa chốt).
:::

---

<!-- layout: oq; id: vt-OQ-6; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/vis/vehicle-telematics.md; group: GPS và Lệnh -->
## Delta còn xe chưa gắn GPS, hoặc có GPS mà chưa có cảm biến dầu không?

> Đội đề xuất: xe chưa gắn GPS vẫn chạy Lệnh như hiện nay, lái xe bấm đến nơi kèm ảnh định vị, không có kẹt xe và bù dầu tự động, vé lấy theo giao dịch thu phí. Xe có GPS mà chưa có cảm biến dầu thì không có cảnh báo hút dầu, đổ dầu; phiếu đầy bình chọn tay.

**Tài liệu:** chưa có trong tài liệu Delta gửi

### A. Còn, xử lý như đề xuất
Nhờ ghi số xe chưa gắn GPS, chưa có cảm biến

### B. Mọi xe sẽ gắn đủ GPS và cảm biến dầu trước khi dùng phần mềm

**Ảnh hưởng:** Lệnh của xe thiếu thiết bị, cảnh báo dầu

::: notes
- Nguồn: bản nháp vehicle-telematics OQ-6 + Mục 6.5. Xe thuê ngoài không quản lý (DEC-102). Không đề xuất.
:::

---

<!-- layout: oq; id: vt-OQ-1; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/vis/vehicle-telematics.md; group: GPS và Lệnh -->
## Delta đang dùng dịch vụ bản đồ nào để tính cung đường và giờ đến dự kiến?

> Tài liệu nhắc ba nguồn bản đồ khác nhau. Bản đồ dùng để tính cung đường, quãng đường, giờ đến dự kiến; nếu có dữ liệu tắc đường, sự cố thì dùng thêm để nhận biết kẹt cứng. Đội đề xuất chọn bên có nhiều dữ liệu giao thông hơn. Toạ độ trạm và phí đường bộ vẫn lấy VETC làm chuẩn như Delta đã chọn ngày 09/10.

**Tài liệu:** VIS (08/10/2026), mục 2.2.1 Thời gian xe sẽ đến (ETA), mục 2.2.6; trao đổi với Delta ngày 09/10/2026, mục 4
**Trích dẫn:** "thì không gọi Google Maps API mà tính ETA cơ học (Khoảng cách / Vận tốc trung bình tuyến)" — VIS, mục 2.2.1
**Trích dẫn:** "Chức năng Map API trên phần mềm Delta 2.0 đã ghi nhận các trạm vé mà xe phải qua trên Lệnh vận tải" — VIS, mục 2.2.6

### A. Google Maps

### B. Vietmap

### C. Bản đồ của phần mềm Delta 2.0

**Ghi thêm:** bên đang dùng có dữ liệu tắc đường, đường cấm xe tải không
**Ảnh hưởng:** cung đường, giờ đến dự kiến, nhận biết kẹt cứng

::: notes
- Nguồn: bản nháp vehicle-telematics OQ-1 + K3. Biên bản 09/10 mục 4 (Vietmap lệch VETC → VETC chuẩn). Không đề xuất: câu hỏi sự thật.
:::

---

<!-- layout: section -->
## Ngưỡng, quy mô, kỳ, rủi ro

---

<!-- layout: oq; id: td-OQ-57; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/vis/transport-dispatch.md; group: Ngưỡng, quy mô, kỳ, rủi ro -->
## Các con số trên Lệnh vận tải: nhờ xác nhận 4 số đã có và cho 2 số còn trống

> Các số dưới đây lấy từ VIS; mỗi khách đặt số riêng được. Số nào muốn khác thì ghi số mới vào ô trả lời, số còn trống nhờ cho số.

**Tài liệu:** VIS (08/10/2026), mục 2.2.1, 2.2.3, 3.1.3, 3.3
**Trích dẫn:** "Nếu khoảng cách không lệch quá x% so với cung đường trên Lệnh vận tải thì không gọi Google Maps API" — VIS, mục 2.2.1

- Kẹt xe: xe nhích dưới 5 km/h, liên tục quá 10 phút
- Tra lại VETC sau 120 phút khi chưa có giao dịch
- Tính lại giờ đến dự kiến mỗi 30 phút với cung đường dài trên 300 km
- Đi tìm vỏ: ở bãi khác quá 10 phút thì tính là bãi đi tìm vỏ
- Còn trống: lệch cung đường bao nhiêu % thì tính lại giờ đến (VIS ghi "x%")
- Còn trống: đứng yên tối đa bao lâu giữa hai đoạn kẹt xe vẫn tính là kẹt (câu 9)

**Ảnh hưởng:** kẹt xe, bù dầu, giờ đến dự kiến trên Lệnh

::: notes
- Nguồn: bản nháp transport-dispatch OQ-57 (tham số Lệnh: vận tốc/thời gian kẹt xe, tra lại VETC, chu kỳ ETA cung dài, thời gian ở bãi tìm vỏ, lệch cung đường ETA, khoảng đứng giữa kẹt xe).
:::

---

<!-- layout: oq; id: vt-OQ-4; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/vis/vehicle-telematics.md; group: Ngưỡng, quy mô, kỳ, rủi ro -->
## Các con số về dầu và cảnh báo xe: nhờ xác nhận 4 số đã có và cho các số còn trống

> Các số đã có lấy từ VIS và Công tác chuẩn bị; riêng chu kỳ đọc dầu khi tắt máy VIS ghi hai số khác nhau. Số nào muốn khác thì ghi số mới.

**Tài liệu:** VIS (08/10/2026), mục 2.2, 2.2.4, 3.5, 3.6; SIM & VIS — Công tác chuẩn bị (11/10/2026), mục 3.3
**Trích dẫn:** "Khi xe tắt máy, hệ thống tự động chuyển sang chế độ quét định kỳ tần suất thấp (30 phút/lần)" — VIS, mục 3.5 Bước 1 (mục 2.2 ghi 30–60 phút)

- Đọc mức dầu khi xe tắt máy: 30 phút một lần
- Nổ máy ngủ: máy nổ, xe đứng yên quá 10 phút
- Hút dầu: giảm quá 5 lít trong dưới 3 phút; đổ dầu: tăng trên 20 lít trong 10 phút khi xe dừng
- Còn trống: hạn xử lý một sự việc (hút dầu, chạy ngoài Lệnh, lệch dầu) trước khi báo trưởng bộ phận
- Còn trống: thiết bị báo lỗi bao nhiêu lần trong tháng thì báo kiểm tra; giữ dữ liệu GPS chi tiết bao lâu
- Còn trống: Lệnh quá giờ kết thúc dự kiến bao lâu khi GPS hỏng thì nhắc lái xe, điều vận

**Ảnh hưởng:** cảnh báo hút dầu, nổ máy ngủ; nhắc xử lý sự việc

::: notes
- Nguồn: bản nháp vehicle-telematics OQ-4 + Mục 7.2 (ngưỡng chạy ngoài Lệnh hỏi ở câu vm-OQ-3, không lặp ở đây).
:::

---

<!-- layout: oq; id: vt-OQ-8; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/vis/vehicle-telematics.md; group: Ngưỡng, quy mô, kỳ, rủi ro -->
## Quy mô đội xe và việc đối soát hiện nay là bao nhiêu?

> Đội dùng các số này để ước khối lượng dữ liệu, số cảnh báo mỗi ngày và chi phí kết nối. Số ước lượng cũng được. Đội đã có: khoảng 110.000 lô hàng mỗi năm (Delta trả lời ngày 10/10) và gần 200 đầu xe (thư đề xuất GPS năm 2025).

**Tài liệu:** chưa có trong tài liệu Delta gửi; Đề xuất tiện ích GPS (25/9/2025), mục 1
**Trích dẫn:** "Hàng tháng Delta đang phải hạch toán hàng ngàn vé xe vào các Lệnh vận chuyển cho gần 200 đầu xe." — Đề xuất tiện ích GPS, mục 1

- Số xe đã gắn GPS; số xe có cảm biến dầu
- Số trạm thu phí xe hay đi qua
- Số giao dịch VETC mỗi tháng
- Số người: quản lý phương tiện, kế toán đối soát, quản lý cây dầu

**Ảnh hưởng:** thiết kế danh sách cảnh báo, tốc độ phần mềm, chi phí kết nối

::: notes
- Nguồn: bản nháp vehicle-telematics OQ-8. 110.000 lô/năm: biên bản docs/meetings/2026-10-10-oq-dispatch-coordination.md (OQ-17).
:::

---

<!-- layout: oq; id: vt-OQ-9; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/vis/vehicle-telematics.md; recommend: A; group: Ngưỡng, quy mô, kỳ, rủi ro -->
## Số liệu dữ liệu xe tính vào kỳ báo cáo (tháng) theo cách đề xuất được không?

> Báo cáo dữ liệu xe tính theo tháng, khớp kỳ chốt dầu. Đội đề xuất: một sự việc (kẹt xe, nổ máy ngủ…) kéo qua nửa đêm hay qua tháng thì tính vào ngày, tháng bắt đầu; số liệu gắn với Lệnh (vé, dầu bù) tính vào kỳ theo ngày duyệt Lệnh.

**Tài liệu:** chưa có trong tài liệu Delta gửi

### A. Đồng ý đề xuất
+ Mỗi sự việc chỉ thuộc một kỳ, không bị cắt đôi
+ Số của Lệnh vào kỳ khi đã chốt xong
- Lệnh duyệt muộn thì số liệu sang kỳ sau

### B. Số liệu của Lệnh tính theo ngày xe chạy xong
+ Đúng ngày phát sinh
- Lệnh chưa duyệt thì số chưa chắc, kỳ có thể phải sửa

**Ảnh hưởng:** báo cáo tháng, kỳ chốt dầu, bảng kê tránh trạm
**Vì sao đề xuất A:** vé và dầu bù chỉ chắc chắn khi Lệnh đã duyệt; tính theo ngày duyệt thì kỳ đã chốt không phải sửa

::: notes
- Nguồn: bản nháp vehicle-telematics OQ-9 + R1.
:::

---

<!-- layout: oq; id: vt-OQ-10; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/vis/vehicle-telematics.md; group: Ngưỡng, quy mô, kỳ, rủi ro -->
## Rủi ro khi dùng dữ liệu xe để tính tiền: nhờ Delta cho ý kiến từng ý, nhất là ý 1 và 2

> Đây là những rủi ro đội thấy khi dữ liệu GPS, cảm biến được dùng để tính tiền cho lái xe. Ý 3–6 đã có cách phòng trong thiết kế; nhờ Delta xác nhận hoặc bổ sung.

**Tài liệu:** VIS (08/10/2026), mục 3.1.1 và mục 3.5 Bước 3
**Trích dẫn:** "hiển thị trực quan vị trí hút dầu trên bản đồ để làm bằng chứng làm việc với lái xe" — VIS, mục 3.5 Bước 3

1. Quy chế nội bộ đã cho phép tính tiền vào lương từ dữ liệu GPS (tránh trạm, nổ máy ngủ, hút dầu) chưa?
2. Lái xe xem số liệu của mình thế nào? Đề xuất: xem trên app; tháng đầu chỉ ghi nhận, chưa tính tiền
3. Lái xe phản đối khi bị ghi vi phạm: người duyệt chấp nhận được, kèm lý do
4. Cảm biến dầu lệch, nhiễu: có kết quả "Lỗi thiết bị", báo hiệu chỉnh khi lệch lặp lại
5. Vùng trạm vẽ sai: giao dịch VETC là nguồn chuẩn khi có
6. EUP, VETC không gửi dữ liệu ngay: cảnh báo trễ, đối soát dồn cuối kỳ

**Ảnh hưởng:** thời điểm bật tính tiền, quyền xem của lái xe trên app

::: notes
- Nguồn: bản nháp vehicle-telematics OQ-10 + Mục 9 Risks (user yêu cầu đưa rủi ro cho khách xem).
:::

---

<!-- layout: recap -->
## Tổng kết câu trả lời

---

<!-- layout: end -->
# Cảm ơn anh/chị
Đội sẽ cập nhật thiết kế theo câu trả lời và hẹn trao đổi riêng những câu cần bàn thêm
