---
type: meeting-deck
meeting: open-questions
delivery: async
feature: dispatch-coordination
title: Câu hỏi cần xác nhận — Điều phối
client: Delta
date: 2026-10-06
footer: Câu hỏi cần xác nhận — Điều phối
brand: innvie
status: shipped
updated: 2026-10-10
links:
  - docs-input/sop/sop-cung-cap-dich-vu-tong-quat.md
  - docs-input/sop/sop-dieu-phoi.md
  - docs-input/sop/sop-ban-do-kien-thuc.md
  - docs-input/sop/giao-nhan-hang-hoa/giao-nhan-hang-hoa.md
  - docs-input/sop/quan-ly-hoa-don-sim/quan-ly-hoa-don-sim.md
  - docs-input/sop/vis-du-lieu-van-hanh-xe/vis-du-lieu-van-hanh-xe.md
  - docs/_shared/project-profile.md
---

<!-- layout: title -->
# Câu hỏi cần xác nhận
24 nội dung cần Delta phản hồi để hoàn thiện thiết kế phần Điều phối

::: notes
- Bản gửi khách tự trả lời (delivery: async) — ghi chú KHÔNG có trong file HTML gửi đi.
- Nguồn câu hỏi: brainstorm Điều phối (chưa ghi vào vault) — ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/brainstorm-dispatch-interview.md mục "Câu hỏi mở" (OQ-1…OQ-34).
- Bỏ: OQ-2 (đã đóng), OQ-14 (gộp OQ-18), OQ-15 (SOP 18/9 đã có link bản đồ 4 ga, GNHH:308-312).
- Khi import: đưa câu trả lời vào file brainstorm lúc viết `docs/dispatch-coordination/brainstorms/`.
- Chưa có reply_to / reply_by — user chưa cung cấp.
:::

---

<!-- layout: goal -->
## Vì sao cần anh/chị trả lời
- **24 câu hỏi** đang chặn phần đặc tả Điều phối: JobID, giao việc hiện trường, chi phí trên Lệnh
- Nhiều câu đã có hướng đề xuất theo SOP, chỉ cần Delta xác nhận
- Mất khoảng 50–60 phút; có thể làm nhiều lần, câu trả lời tự lưu
- Nhóm **Kế toán** có thể nhờ phòng kế toán trả lời
- Câu nào chưa quyết được: bấm **Cần trao đổi thêm**, đội sẽ hẹn trao đổi riêng

---

<!-- layout: agenda -->
## Nội dung
1. **Phạm vi và tổ chức** — chi nhánh, lợi nhuận nội bộ, quy mô (7 câu)
2. **Hiện trường và giao việc** — ca trực, Lệnh hạ vỏ, ký nhận hàng (6 câu)
3. **Chi phí và thanh toán** — chi ngoài định mức, tiền hoàn, lưu xe (6 câu)
4. **Kế toán và tài liệu** — hoá đơn đầu vào, hạch toán, tài liệu cần gửi (5 câu)

---

<!-- layout: section -->
## Phạm vi và tổ chức

---

<!-- layout: oq; id: OQ-16; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/brainstorm-dispatch-interview.md; recommend: A; group: Phạm vi và tổ chức -->
## Khi chi nhánh khác làm việc cho một JobID, phần mềm ghi nhận thế nào?

> Quy trình cung cấp dịch vụ đã nêu 2 trường hợp giao dịch nội bộ giữa chi nhánh nhưng chưa nói thao tác trên phần mềm.

**Tài liệu:** Quy trình cung cấp dịch vụ tổng quát, mục 4.4 Hạch toán nội bộ

### A. Theo quy trình cung cấp dịch vụ
Làm toàn bộ: chi nhánh đó tự tạo JobID. Làm một phần: nhận giao phần việc trên JobID
+ Rõ chi nhánh nào làm việc nào
- Phải tạo JobID mới khi nhận toàn bộ

### B. Chuyển nguyên JobID
+ Thao tác nhanh, không tạo lại
- Khó tách doanh thu, chi phí từng chi nhánh

**Ảnh hưởng:** báo cáo giao dịch nội bộ, ai được xem JobID
**Vì sao đề xuất A:** đúng nguyên tắc Delta đã đặt trong quy trình, tách bạch hạch toán nội bộ

::: notes
- Nguồn: OQ-16; QTCCDV sop-cung-cap-dich-vu-tong-quat.md:708-730 (TH1, TH2; "cung cấp toàn bộ thì chi nhánh A phải tạo JobID").
- Phạm vi xem chi nhánh khác: feature Phân quyền quyết (Phần 2 câu 3).
:::

---

<!-- layout: oq; id: OQ-4; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/brainstorm-dispatch-interview.md; group: Phạm vi và tổ chức -->
## Chia lợi nhuận giữa các chi nhánh theo cách nào?

> Quy trình cung cấp dịch vụ nêu 3 cách, chọn tuỳ dữ liệu phần mềm đáp ứng, nhưng chưa chọn cách nào.

**Tài liệu:** Quy trình cung cấp dịch vụ tổng quát, mục 4.4 Hạch toán nội bộ

### A. Cộng lãi định mức vào chi phí
Chi nhánh làm dịch vụ nhận chi phí + một khoản lãi định mức
+ Đơn giản, dễ tính
- Lãi không đổi theo kết quả lô hàng

### B. Trừ lãi định mức trên doanh thu
Chi nhánh ghi doanh thu trả cho chi nhánh làm dịch vụ
+ Bám theo doanh thu thực tế
- Cần định mức cho từng loại dịch vụ

### C. Chia theo tỷ lệ lãi gộp
+ Công bằng theo kết quả từng JobID
- Cần đủ doanh thu, chi phí mới chia được

**Ảnh hưởng:** báo cáo giao dịch nội bộ, hoá đơn bù trừ cuối tháng

::: notes
- Nguồn: OQ-4; sop-cung-cap-dich-vu-tong-quat.md:736-746 (Cost plus / Revenue minus / Profit share).
- Không đề xuất: quyết định tài chính của lãnh đạo.
:::

---

<!-- layout: oq; id: OQ-12; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/brainstorm-dispatch-interview.md; recommend: A; group: Phạm vi và tổ chức -->
## Hàng CBT và đường sắt: dùng tạm SOP Giao nhận hàng hoá 18/9 trong lúc chờ quy trình điều vận?

> Hàng CBT và đường sắt đi thẳng từ yêu cầu vận tải sang Lệnh. Phần này thuộc quy trình điều vận, Delta chưa gửi tài liệu.

**Tài liệu:** Giao nhận hàng hoá (18/9/2026), mục 3.4 Hàng CBT và 3.5 Hàng đường sắt Ratraco

### A. Dùng tạm SOP 18/9
Bổ sung khi có quy trình điều vận
+ Không phải chờ, thiết kế vẫn bám SOP
- Có thể phải chỉnh lại khi có quy trình mới

### B. Chờ quy trình điều vận
+ Thiết kế một lần, ít sửa
- Phần CBT và đường sắt bị dừng

**Ảnh hưởng:** Lệnh và chi phí của hàng CBT, đường sắt
**Vì sao đề xuất A:** SOP 18/9 đã mô tả đủ các bước giao nhận và chi phí của 2 loại hàng này

::: notes
- Nguồn: OQ-12 + OQ-1 (chưa có QTĐV). GNHH 3.4 (CBT) + 3.5 (rail).
- User đã chốt 05/10: CBT + rail vào brainstorm ở mức Lệnh + chi phí.
:::

---

<!-- layout: oq; id: OQ-9; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/brainstorm-dispatch-interview.md; group: Phạm vi và tổ chức -->
## JobID hàng đường sắt cần những thông tin nhận diện nào?

> SOP ghi giao nhận tại ga đơn giản hơn cảng, không theo dõi giờ lấy/trả vỏ, nên "cần xem xét lại thông tin định danh" của JobID này. Nhờ liệt kê thông tin cần có, ví dụ: số kế hoạch Ratraco, số container, ga, khách.

**Tài liệu:** Giao nhận hàng hoá (18/9/2026), mục 3.5.1 Quy trình giao nhận container hàng ga Đông Anh

**Ảnh hưởng:** cách tạo JobID và Lệnh cho hàng đường sắt

::: notes
- Nguồn: OQ-9; GNHH:871. Kế hoạch chạy hàng ngày n do Ratraco gửi ngày n-1 (GNHH:875).
:::

---

<!-- layout: oq; id: OQ-18; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/brainstorm-dispatch-interview.md; group: Phạm vi và tổ chức -->
## Quản lý vỏ container (vỏ của Delta hoặc của khách, sửa chữa vỏ) có thuộc phần Điều phối không?

> Vỏ container đổi qua lại giữa Delta, khách và bãi, có khi phải sửa. Chưa rõ phần nào của phần mềm theo dõi việc này.

**Tài liệu:** chưa có trong tài liệu Delta gửi

### A. Trong Điều phối
+ Theo dõi vỏ ngay trên JobID và Lệnh
- Phần Điều phối lớn hơn, lâu xong hơn

### B. Tách thành phần riêng
Điều phối chỉ ghi số vỏ trên Lệnh
+ Điều phối gọn, ra sớm
- Cần thêm một phần quản lý vỏ sau

**Ảnh hưởng:** phạm vi phần Điều phối, theo dõi tồn vỏ

::: notes
- Nguồn: OQ-18 (= OQ-14 cũ). User chốt để OQ, không có căn cứ đề xuất.
:::

---

<!-- layout: oq; id: OQ-17; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/brainstorm-dispatch-interview.md; group: Phạm vi và tổ chức -->
## Quy mô từng chi nhánh hiện nay là bao nhiêu?

> Nhờ ghi cho Hà Nội, Hải Phòng, TP.HCM, Lạng Sơn: số JobID mỗi ngày, số lái xe, nhân viên hiện trường, CS, điều vận. Số đội đã biết: khoảng 7.000 hoá đơn trả hộ mỗi tháng; TP.HCM có khoảng 16 xe chạy hàng đường sắt.

**Tài liệu:** Hoá đơn trả hộ (01/10/2026), phần mở đầu; Giao nhận hàng hoá (18/9/2026), mục 3.5.2

**Ảnh hưởng:** thiết kế danh sách việc, cảnh báo và tốc độ phần mềm

::: notes
- Nguồn: OQ-17. 7.000 HĐ trả hộ/tháng: quan-ly-hoa-don-sim.md; 16 xe rail HCM (Bình Thung 5 + Trảng Bom 11): GNHH 3.5.2.
:::

---

<!-- layout: oq; id: OQ-21; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/brainstorm-dispatch-interview.md; group: Phạm vi và tổ chức -->
## Delta làm nhiều nhất ở những cảng và depot nào?

> Nhờ ghi 5–10 cảng/depot làm nhiều nhất, nếu được thì kèm số lượt mỗi tháng. Đội dùng danh sách này để ưu tiên danh sách việc theo cảng cho CS.

**Tài liệu:** chưa có trong tài liệu Delta gửi

**Ảnh hưởng:** danh sách việc theo cảng, thứ tự cảng làm trước

::: notes
- Nguồn: OQ-21. Báo cáo eport-integration: 36 cảng (25 có ePort), 88 depot (14 có).
:::

---

<!-- layout: section -->
## Hiện trường và giao việc

---

<!-- layout: oq; id: OQ-25; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/brainstorm-dispatch-interview.md; recommend: A; group: Hiện trường và giao việc -->
## CS chuyển việc làm Lệnh nâng vỏ cho hiện trường: danh sách lý do dưới đây đã đủ chưa?

> Thay nút "Từ chối" bằng "Chuyển cho hiện trường", quyền thanh toán tự chuyển theo.

**Tài liệu:** Quy trình điều phối, mục 5.1 Quy trình điều phối hàng FCL xuất khẩu, trường hợp 2 và 5

### A. Bắt chọn 1 trong 4 lý do
Bãi yêu cầu có xe mới chọn vỏ · Ngoài giờ làm việc · ePort lỗi · Khác (ghi chú)
+ Thống kê được vì sao CS chuyển việc
- Thêm một bước khi chuyển

### B. Không bắt chọn lý do
+ Chuyển nhanh
- Không biết vì sao việc bị chuyển

**Ảnh hưởng:** màn giao việc của CS và nhân viên hiện trường
**Vì sao đề xuất A:** biết nguyên nhân thì cải thiện được, ví dụ cảng nào ePort hay lỗi
**Nếu chọn A:** ghi thêm lý do cần bổ sung, nếu có

::: notes
- Nguồn: OQ-25; B2. SOP sop-dieu-phoi.md:787 (TH2), :815 (TH5), :790 quyền thanh toán.
:::

---

<!-- layout: oq; id: OQ-26; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/brainstorm-dispatch-interview.md; group: Hiện trường và giao việc -->
## Lịch trực ngoài giờ (17h30–8h) xếp theo cách nào?

> SOP: quản lý phân công nhân viên hiện trường trực theo ngày; người trực được tự giao việc làm Lệnh nâng hạ.

**Tài liệu:** Quy trình điều phối, mục 4.1 Thông tin chung, phần "Nhân viên hiện trường trực làm ngoài giờ hành chính"

### A. Quản lý chọn người trực từng ngày
+ Linh hoạt theo tình hình
- Quên chọn thì không có người trực

### B. Lịch xoay vòng theo tuần
Phần mềm tự xếp, quản lý chỉnh khi cần
+ Không sót ngày
- Cần lập danh sách người trực trước

**Ảnh hưởng:** ca trực, quyền tự giao việc ngoài giờ
**Nhờ ghi thêm:** ngày không có người trực thì báo ai; việc dở lúc 8h giao cho ai; có trực cuối tuần, ngày lễ không; mỗi chi nhánh 1 hay nhiều người trực

::: notes
- Nguồn: OQ-26; B3b. sop-dieu-phoi.md:417-421. A = SOP to-be, B = SOP+.
:::

---

<!-- layout: oq; id: OQ-27; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/brainstorm-dispatch-interview.md; recommend: A; group: Hiện trường và giao việc -->
## Gộp giao việc làm Lệnh hạ vỏ rỗng theo vận đơn và nơi hạ được không?

> SOP làm Lệnh hạ vỏ cho từng container vì một vận đơn có thể hạ nhiều bãi và khách nhận hàng nhiều ngày.

**Tài liệu:** Giao nhận hàng hoá (18/9/2026), mục 3.1.1 Giao nhận container với cảng bãi

### A. Gộp theo vận đơn + nơi hạ
Mỗi container vẫn 1 Lệnh hạ; theo dõi đã làm mấy/tổng số
+ Một người lo trọn, ít giao việc lặp
- Không giao lẻ từng container được

### B. Giao từng container như hiện nay
+ Linh hoạt từng container
- Giao việc nhiều lần cho cùng vận đơn

**Ảnh hưởng:** giao việc cho CS và hiện trường
**Vì sao đề xuất A:** vẫn giữ đúng lý do SOP tách từng container, chỉ gom phần giao việc
**Nhờ ghi thêm:** có khi nào cùng vận đơn, cùng nơi hạ nhưng phải giao cho người khác không

::: notes
- Nguồn: OQ-27; B4. GNHH:355-366.
:::

---

<!-- layout: oq; id: OQ-19; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/brainstorm-dispatch-interview.md; group: Hiện trường và giao việc -->
## Khi đặt xe, khách có báo trước số booking, tàu hoặc số ngày miễn phí lưu container không?

> Hiện các mốc hạn chỉ ghi khi có Booking Note (hàng xuất) hoặc Lệnh giao hàng (hàng nhập). Có sớm hơn thì cảnh báo được sớm hơn.

**Tài liệu:** Giao nhận hàng hoá (18/9/2026), mục 3.1.3 Giao nhận container với hãng tàu

### A. Thường có
Ghi mốc ngay lúc đặt xe, xác nhận lại khi có chứng từ
+ Cảnh báo sớm, ít bị phạt
- CS phải xác nhận lại

### B. Thường không có
Mốc chỉ ghi khi có chứng từ
+ Mốc luôn đúng chứng từ
- Cảnh báo muộn hơn

**Ảnh hưởng:** cảnh báo hạn nộp chi tiết lô hàng, hạ hàng, lưu container

::: notes
- Nguồn: OQ-19; GNHH:400-418 (mốc SI/CY/DEM/DET lấy từ Booking Note, Lệnh giao hàng).
- Báo cáo deadline: mốc "dự kiến"/"đã xác nhận".
:::

---

<!-- layout: oq; id: OQ-20; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/brainstorm-dispatch-interview.md; recommend: B; group: Hiện trường và giao việc -->
## Khách có chấp nhận ký nhận hàng trên điện thoại của lái xe không?
**Tài liệu:** chưa có trong tài liệu Delta gửi

### A. Thay hẳn biên bản giấy
+ Biên bản về ngay, không chờ giấy
- Có khách chưa quen

### B. Ký điện tử kèm biên bản giấy
Chạy thử với khách đồng ý
+ Thử được mà không rủi ro
- Giai đoạn đầu vẫn có giấy

### C. Chỉ giấy, lái xe chụp ảnh
+ Không đổi thói quen khách
- Vẫn chờ giấy để chốt Lệnh

**Ảnh hưởng:** biên bản giao hàng, chốt Lệnh và tính chi phí
**Vì sao đề xuất B:** thử với vài khách trước, giấy vẫn là căn cứ trong lúc chạy thử
**Nhờ ghi thêm:** phía khách thường ai ký (thủ kho, bảo vệ, đại diện); khách nào bắt đóng dấu

::: notes
- Nguồn: OQ-20 + "khách có chấp nhận ký điện tử" (còn lại từ trước). Quyết định 05/10: biên bản A + B (B chạy thử).
:::

---

<!-- layout: oq; id: OQ-34; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/brainstorm-dispatch-interview.md; recommend: A; group: Hiện trường và giao việc -->
## Container quá hạn vì kẹt xe hoặc sự cố đường thì xếp vào nguyên nhân nào?

> SOP có 3 nhóm nguyên nhân quá hạn: khách giao chậm, Delta điều xe chậm hoặc xe hỏng, bên thứ ba. Hàng air có thêm nhóm khách quan.

**Tài liệu:** Giao nhận hàng hoá (18/9/2026), mục 3.1.3 (container) và 3.3.3 (hàng air)

### A. Giữ 3 nhóm
Dữ liệu kẹt xe từ GPS gắn làm bằng chứng
+ Không đổi cách quy trách nhiệm phí
- Kẹt xe vẫn tính vào nhóm Delta

### B. Thêm nhóm "khách quan"
+ Tách được lỗi không do ai
- Phải thống nhất lại cách chia phí với khách

**Ảnh hưởng:** cảnh báo quá hạn, quy trách nhiệm phí
**Vì sao đề xuất A:** giữ đúng SOP; có bằng chứng GPS để thương lượng khi cần

::: notes
- Nguồn: OQ-34; sop-ban-do-kien-thuc.md:188; GNHH:414 (3 nhóm). E7 câu 2 user chốt (a).
:::

---

<!-- layout: section -->
## Chi phí và thanh toán

---

<!-- layout: oq; id: OQ-29; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/brainstorm-dispatch-interview.md; group: Chi phí và thanh toán -->
## Khi khách đồng ý khoản chi ngoài định mức, lưu bằng chứng bằng cách nào?

> Lái xe phải xin điều vận trước khi chi; điều vận xác nhận với khách. Cách này sẽ áp cho mọi loại hàng.

**Tài liệu:** Giao nhận hàng hoá (18/9/2026), mục 3.4.3.3, 3.4.4.3, 3.4.5.3

### A. Khách bấm đồng ý trên app
+ Có bằng chứng ngay, rõ ai đồng ý
- Khách phải có tài khoản

### B. Đính kèm ảnh tin nhắn hoặc email
+ Khách không phải đổi thói quen
- Điều vận phải chụp và gắn tay

### C. Gửi link xác nhận cho khách
+ Khách không cần tài khoản
- Khách có thể không bấm kịp

### D. Ghi "đã gọi khách" kèm giờ
+ Nhanh nhất
- Khó làm căn cứ khi khách từ chối trả

**Ảnh hưởng:** duyệt chi phí ngoài định mức trên Lệnh

::: notes
- Nguồn: OQ-29; E1. GNHH:778, 823, 852.
:::

---

<!-- layout: oq; id: OQ-28; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/brainstorm-dispatch-interview.md; recommend: A; group: Chi phí và thanh toán -->
## Từ chối nhận vỏ đã trả tiền nâng: ai xác nhận đã nhận tiền hoàn?

> Bãi hoàn tiền nâng sau 7 ngày, về tài khoản người làm Lệnh nâng vỏ. Phần mềm sẽ theo dõi khoản chờ hoàn và cảnh báo khi quá hạn.

**Tài liệu:** Giao nhận hàng hoá (18/9/2026), mục 3.1.4 Các vấn đề liên quan

### A. Người làm Lệnh nâng vỏ
+ Tiền về tài khoản họ, biết đầu tiên
- Phải nhớ vào xác nhận

### B. Kế toán
+ Kiểm soát tập trung
- Kế toán phải đối chiếu tài khoản cá nhân

**Ảnh hưởng:** khoản chờ hoàn trên Lệnh và JobID
**Vì sao đề xuất A:** tiền về tài khoản người đó, họ thấy đầu tiên
**Nhờ ghi thêm:** quá 7 ngày chưa nhận thì báo ai

::: notes
- Nguồn: OQ-28; B5. GNHH:462; sop-ban-do-kien-thuc.md:233.
:::

---

<!-- layout: oq; id: OQ-30; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/brainstorm-dispatch-interview.md; recommend: C; group: Chi phí và thanh toán -->
## Đường sắt: chuyến chưa có đơn giá, giá xác định lần đầu dùng thế nào?

> Chuyến chưa có giá trong phụ lục hợp đồng thì người ghi nhận hỏi người phụ trách giá. Phần mềm sẽ gắn cờ "Chưa có đơn giá".

**Tài liệu:** Giao nhận hàng hoá (18/9/2026), mục 3.5.4 Quy trình ghi nhận doanh thu

### A. Lưu cho các chuyến sau
Chờ ký phụ lục mới
+ Không hỏi lại mỗi chuyến
- Dễ dùng giá chưa được ký

### B. Chỉ dùng cho chuyến đó
+ Chặt chẽ theo phụ lục
- Hỏi giá lại nhiều lần

### C. Người xác định giá chọn từng lần
+ Hợp cả 2 trường hợp thực tế
- Thêm một lựa chọn khi nhập giá

**Ảnh hưởng:** bảng giá đường sắt, chốt bảng kê kỳ 25 và cuối tháng
**Vì sao đề xuất C:** thực tế có cả giá dùng một lần và giá dùng lâu dài
**Nhờ ghi thêm:** ai được xác định giá

::: notes
- Nguồn: OQ-30 + OQ-13; E3. GNHH:1000 ("hỏi lại anh Vũ").
:::

---

<!-- layout: oq; id: OQ-32; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/brainstorm-dispatch-interview.md; recommend: B; group: Chi phí và thanh toán -->
## Khoản chi hộ Ratraco: bước trả tiền lại cho lái xe làm thế nào?

> Hiện có 5 bước: lái xe chi, điều vận lập bảng kê, CS làm thanh toán, quản lý duyệt, thủ quỹ trả lái xe.

**Tài liệu:** Giao nhận hàng hoá (18/9/2026), mục 3.5.3; Hoá đơn trả hộ (01/10/2026)

### A. Thủ quỹ trả như hiện nay
+ Không đổi quy trình
- Vẫn dùng tiền mặt

### B. Chuyển khoản tự động
Theo cách thanh toán trả hộ qua ngân hàng
+ Bỏ được quỹ tiền mặt
- Phụ thuộc phần thanh toán trả hộ xong trước

**Ảnh hưởng:** chi hộ trên Lệnh đường sắt, quỹ tiền mặt
**Vì sao đề xuất B:** khớp mục tiêu bỏ quỹ tiền mặt trong tài liệu hoá đơn trả hộ 01/10

::: notes
- Nguồn: OQ-32; E4. GNHH:984-987; SRC-07 quan-ly-hoa-don-sim.md (UNC qua API MB/VCB/TPBank).
:::

---

<!-- layout: oq; id: OQ-33; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/brainstorm-dispatch-interview.md; recommend: A; group: Chi phí và thanh toán -->
## Phí lưu xe quá 72 giờ và phí chạy máy phát: phần mềm có tự tính không?

> Hàng CBT miễn phí 72 giờ lưu xe khi đóng hàng và khi trả hàng ở cửa khẩu; máy phát chạy lạnh thu theo thời gian thực tế.

**Tài liệu:** Giao nhận hàng hoá (18/9/2026), mục 3.4.4.1 Thông báo

### A. Phần mềm tự tính
Đề xuất dòng doanh thu trên JobID, CS xác nhận
+ Không sót khoản thu
- Cần đơn giá rõ trong hợp đồng

### B. CS tự tính như hiện nay
+ Không cần thiết lập trước
- Dễ sót hoặc tính muộn

**Ảnh hưởng:** doanh thu hàng CBT
**Vì sao đề xuất A:** giờ xe đến và rời đã có từ định vị nên tính được chính xác
**Nhờ ghi thêm:** đơn giá theo hợp đồng khách nào; tính theo giờ, ngày hay ca

::: notes
- Nguồn: OQ-33; E8. GNHH:789-793, 734.
- Hỏi tiếp: giờ bắt đầu lấy từ geofence hay ảnh định vị check-in.
:::

---

<!-- layout: oq; id: OQ-6; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/brainstorm-dispatch-interview.md; group: Chi phí và thanh toán -->
## Khách từ chối trả khoản trả hộ do lỗi nhân viên Delta: xử lý thế nào?

> Quy trình cung cấp dịch vụ ghi tăng chi phí trên JobID và nêu có thể phát sinh bồi thường nội bộ, nhưng chưa có cách ghi nhận.

**Tài liệu:** Quy trình cung cấp dịch vụ tổng quát, mục 5.4 Quy trình quản lý nợ phải thu

### A. Chỉ ghi tăng chi phí JobID
+ Đơn giản, đúng quy trình hiện có
- Không truy được người gây lỗi

### B. Ghi tăng chi phí + lập khoản bồi thường
Quản lý duyệt khoản bồi thường cho người gây lỗi
+ Rõ trách nhiệm
- Thêm bước duyệt, cần quy định mức bồi thường

**Ảnh hưởng:** chi phí JobID, theo dõi trách nhiệm nhân viên

::: notes
- Nguồn: OQ-6; sop-cung-cap-dich-vu-tong-quat.md:1836-1842, :1870.
:::

---

<!-- layout: section -->
## Kế toán và tài liệu

---

<!-- layout: oq; id: OQ-23; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/brainstorm-dispatch-interview.md; group: Kế toán và tài liệu -->
## Phần mềm MISA của Delta có lấy được hoá đơn đầu vào không?

> Đội định lấy hoá đơn điện tử từ MISA thay vì đọc ảnh; không khớp thì chụp và nhập tay.

**Tài liệu:** Quy trình cung cấp dịch vụ tổng quát, mục 4.10 Giải pháp phát hành hoá đơn

### A. Lấy được đầy đủ
### B. Lấy được một phần
### C. Không lấy được

**Ảnh hưởng:** gắn hoá đơn chi phí vào Lệnh và JobID
**Nhờ ghi thêm:** hoá đơn trả hộ ghi mã số thuế của ai (Delta hay khách)

::: notes
- Nguồn: OQ-23 + "HĐ lái xe trả hộ mang MST của ai". QTCCDV:1132-1152 chỉ có chiều phát hành. A9.
:::

---

<!-- layout: oq; id: OQ-31; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/brainstorm-dispatch-interview.md; group: Kế toán và tài liệu -->
## Các loại phí hiện trường được hạch toán thế nào theo từng địa điểm?

> Với đường sắt, SOP đã có: thu nhập chịu thuế lái xe (trả kỳ lương), chi hộ (thu lại khách), trả hộ, chi phí vận hành. Nhờ bổ sung quy tắc cho các tuyến và loại hàng khác.

**Tài liệu:** Giao nhận hàng hoá (18/9/2026), mục 3.5.3 Quy trình thanh toán chi phí

**Ảnh hưởng:** lái xe chỉ chọn loại phí, phần mềm tự xếp cách hạch toán

::: notes
- Nguồn: OQ-31; E5. GNHH:956, 976-982 (150k Nam Khánh / 160k Phú Lợi; tài 2, bốc xếp).
:::

---

<!-- layout: oq; id: OQ-10; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/brainstorm-dispatch-interview.md; group: Kế toán và tài liệu -->
## Khoản chi hộ bốc xếp cho Ratraco không có hoá đơn đầu vào được hạch toán thế nào?

> Delta không có hoá đơn đầu vào nhưng phải xuất hoá đơn cho Ratraco. SOP ghi cần làm việc với Ratraco về thuế nếu khoản này phát sinh nhiều.

**Tài liệu:** Giao nhận hàng hoá (18/9/2026), mục 3.5.4 Quy trình ghi nhận doanh thu

**Ảnh hưởng:** bảng kê doanh thu Ratraco, thuế thu nhập doanh nghiệp

::: notes
- Nguồn: OQ-10; GNHH:998-999.
:::

---

<!-- layout: oq; id: OQ-11; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/brainstorm-dispatch-interview.md; recommend: A; group: Kế toán và tài liệu -->
## Hàng CBT xuất hoá đơn cho bên thứ ba được uỷ quyền: chấp nhận lệch giữa báo cáo quản trị và báo cáo thuế?

> Doanh thu quản trị ghi theo khách chính, hoá đơn xuất cho bên thanh toán được uỷ quyền.

**Tài liệu:** Giao nhận hàng hoá (18/9/2026), mục 3.4.1.1 Doanh thu

### A. Chấp nhận lệch
+ Báo cáo quản trị đúng khách chính
- Phải giải trình khi đối chiếu thuế

### B. Không chấp nhận
+ Hai báo cáo khớp nhau
- Doanh thu quản trị ghi sai khách

**Ảnh hưởng:** chọn bên xuất hoá đơn sau khi hoàn thành Lệnh CBT
**Vì sao đề xuất A:** SOP 18/9 đã nêu cần chấp nhận sai lệch hình thức này

::: notes
- Nguồn: OQ-11; GNHH:700-703 (DK05 cấp 2, "Cần chấp nhận sự sai lệch về hình thức này").
:::

---

<!-- layout: oq; id: OQ-3; src: ~/.claude/handoff/Users-szit-Desktop-szit-AI-Projects-invlogis/drafts/brainstorm-dispatch-interview.md; group: Kế toán và tài liệu -->
## Anh/chị gửi giúp các tài liệu sau được không, dự kiến khi nào?
**Tài liệu:** Giao nhận hàng hoá (18/9/2026), mục 3.1.4 (phần ý kiến Trasas)

- Quy trình điều vận
- Phụ lục thông tin JobID, định mức chi phí và bảng kê doanh thu, chi phí
- Quy trình quản lý quỹ và thanh toán
- 4 quy trình bổ sung theo ý kiến Trasas, và Trasas là đơn vị nào
- Mẫu QR trên tờ khai hải quan và trên lệnh giao vỏ điện tử (bãi nào phát hành)

::: notes
- Gộp: OQ-1 (QTĐV), OQ-3 + OQ-5 (phụ lục trống), OQ-7 (QT 5.10), OQ-8 (Trasas, GNHH:484-489), OQ-22 (QR tờ khai), OQ-24 (QR lệnh giao vỏ SRC-12).
:::

---

<!-- layout: recap -->
## Tổng kết câu trả lời

---

<!-- layout: bullets -->
## Sau khi nhận câu trả lời
- Đội cập nhật thiết kế phần Điều phối theo câu trả lời của Delta
- Câu chọn **Cần trao đổi thêm**: đội hẹn một buổi ngắn để chốt
- Tài liệu Delta gửi thêm: đội đọc và bổ sung vào thiết kế

---

<!-- layout: end -->
# Cảm ơn anh/chị
