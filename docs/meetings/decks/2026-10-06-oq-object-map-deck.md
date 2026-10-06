---
type: meeting-deck
meeting: open-questions
delivery: async
title: Câu hỏi cần xác nhận — Phân quyền, Xưởng và Cây dầu
client: Delta
date: 2026-10-06
footer: Câu hỏi cần xác nhận
brand: innvie
status: draft
updated: 2026-10-06
links:
  - docs/_shared/object-map.md
  - docs-input/srs-cu/lg-srs-export.md
  - docs/_shared/project-profile.md
---

<!-- layout: title -->
# Câu hỏi cần xác nhận
9 nội dung cần Delta phản hồi để hoàn thiện đặc tả phân quyền, xưởng và cây dầu

::: notes
- Bản gửi khách tự trả lời (delivery: async) — ghi chú này KHÔNG có trong file HTML gửi đi.
- Nguồn câu hỏi: docs/_shared/object-map.md Mục 6 (OQ-1…OQ-9).
- Thứ tự đã chốt với BA: 2 → 1 → 6 → 3 → 4 → 7 → 8 → 5 → 9.
:::

---

<!-- layout: goal -->
## Vì sao cần anh/chị trả lời
- **9 câu hỏi** đang chặn phần đặc tả phân quyền, xưởng và cây dầu
- Nhiều câu đã có hướng trong thiết kế hiện tại, chỉ cần Delta xác nhận
- Mất khoảng 20–25 phút; có thể làm nhiều lần, câu trả lời tự lưu
- Câu nào chưa quyết được: bấm **Cần trao đổi thêm**, đội sẽ hẹn trao đổi riêng

::: notes
- 5/9 câu (1 phần câu 1, câu 3, 4, 5, 6) SRS cũ đã có hướng — khách chỉ cần xác nhận.
:::

---

<!-- layout: agenda -->
## Nội dung
1. **Phân quyền** — vai trò mẫu, duyệt nhân sự, tài khoản (3 câu)
2. **Xưởng và mua hàng** — xuất phụ tùng, sửa ở xưởng ngoài, xác nhận báo giá (3 câu)
3. **Phương tiện và cây dầu** — biên bản giao xe, nhà cung cấp dầu, phiếu nhập dầu (3 câu)

---

<!-- layout: section -->
## Phân quyền

---

<!-- layout: oq; id: OQ-2; src: docs/_shared/object-map.md; recommend: A; group: Phân quyền -->
## Bộ 5 vai trò mẫu có dùng làm điểm khởi đầu được không?

> Thiết kế đang có 5 vai trò mẫu: Lái xe, Giám đốc xưởng, Cố vấn dịch vụ, Kế toán tổng hợp, IT. Bảng này chưa được Delta xác nhận.

### A. Dùng làm khởi đầu
Delta rà bảng quyền rồi chỉnh trong quá trình triển khai
+ Có sẵn phân quyền để chạy thử sớm
- Delta cần dành thời gian rà từng quyền

### B. Làm lại theo chức danh thực tế
Delta gửi danh sách chức danh, đội dựng lại bảng quyền
+ Sát cơ cấu tổ chức hiện nay
- Chậm hơn, cần thêm một vòng xác nhận

**Ảnh hưởng:** ai thấy và làm được gì trên Website và Super App
**Vì sao đề xuất A:** bảng đã chi tiết tới từng chức năng, chỉnh nhanh hơn dựng lại từ đầu
**Nếu chọn B:** ghi thêm ai bên Delta gửi danh sách chức danh

::: notes
- Nguồn: lg-srs-export.md:3046-3075 (bảng "Seed dữ liệu khởi đầu", đang đánh dấu [not done]); ma trận quyền :3076-3540.
- Số quyền mỗi vai trò: Lái xe 15 · Giám đốc xưởng 85 · Cố vấn dịch vụ 92 · Kế toán tổng hợp 91 · IT 12.
:::

---

<!-- layout: oq; id: OQ-1; src: docs/_shared/object-map.md; recommend: B; group: Phân quyền -->
## Ai duyệt đề xuất thêm nhân viên mới và yêu cầu nghỉ việc?

> Các danh mục khác (xưởng, nhà cung cấp, phụ tùng, lốp, ắc quy, chi phí…) đều do Giám đốc xưởng duyệt. Riêng nhân viên mới và nghỉ việc chưa giao cho ai.

### A. Giám đốc xưởng
+ Một người duyệt mọi đề xuất, dễ nhớ
- Giám đốc xưởng gánh thêm việc nhân sự

### B. Bộ phận nhân sự
Thêm vai trò riêng cho nhân sự
+ Đúng người, đúng chuyên môn
- Thêm một vai trò cần quản lý

**Ảnh hưởng:** hồ sơ nhân viên, cấp và khoá tài khoản khi nghỉ việc
**Vì sao đề xuất B:** tài liệu cũ đã cố ý tách việc duyệt nhân sự khỏi Giám đốc xưởng
**Nếu chọn B:** ghi thêm ai giữ vai trò này, theo chi nhánh hay toàn công ty

::: notes
- Câu gốc OQ-1 đọc nhầm: ma trận quyền (lg-srs-export.md:3105-3170, :3515-3532) ĐÃ tick Giám đốc xưởng duyệt mọi danh mục. Câu "trừ đề xuất cấp mới và xin nghỉ của Nhân sự" (:3059) chỉ loại phần nhân sự.
- Module Nhân sự (:3496-3504): quyền Phê duyệt/Từ chối cấp mới và xin nghỉ — không vai trò nào được tick.
- Luồng tài khoản ghi "nhân viên nghỉ việc (HR trigger)" (:26334) → có vai trò nhân sự.
:::

---

<!-- layout: oq; id: OQ-6; src: docs/_shared/object-map.md; recommend: A; group: Phân quyền -->
## Mỗi nhân viên có đúng một tài khoản, dùng chung cho Website và Super App?

> Thiết kế hiện tại tạo tài khoản từ hồ sơ nhân viên, chỉ chọn được nhân viên chưa có tài khoản. Email đăng nhập lấy từ hồ sơ.

### A. Một nhân viên, một tài khoản
Dùng cho cả Website và Super App
+ Một mật khẩu, dễ khoá khi nghỉ việc
- Muốn tách quyền theo nơi làm thì phải chỉnh nhóm quyền

### B. Cho phép nhiều tài khoản
+ Tách riêng theo nơi làm hoặc chi nhánh
- Khó kiểm soát, dễ sót khi khoá tài khoản

**Ảnh hưởng:** tạo tài khoản, đăng nhập, khoá tài khoản khi nghỉ việc
**Vì sao đề xuất A:** đúng thiết kế hiện tại; khi nhân viên nghỉ việc chỉ cần khoá một chỗ

::: notes
- Nguồn: UC13.01.02 Tạo tài khoản — lg-srs-export.md:26441-26460 ("Nhân viên đã có hồ sơ và chưa có tài khoản"; "Danh sách chỉ hiển thị nhân viên chưa có tài khoản").
- Danh sách tài khoản có lọc theo Nền tảng (:26379) → 1 tài khoản có thể gắn nhiều nền tảng.
:::

---

<!-- layout: section -->
## Xưởng và mua hàng

---

<!-- layout: oq; id: OQ-3; src: docs/_shared/object-map.md; recommend: A; group: Xưởng và mua hàng -->
## Một lệnh sửa chữa có được xuất phụ tùng nhiều lần không?

> Lệnh sửa xe, thay lốp, thay ắc quy đều xuất phụ tùng từ kho trong lúc sửa. Sau nghiệm thu, phần dư được nhập lại kho.

### A. Nhiều lần
Xuất bổ sung khi phát sinh hư hỏng mới
+ Đúng thực tế sửa chữa hay phát sinh thêm
- Một lệnh có nhiều phiếu, kế toán cần đối chiếu

### B. Một lần duy nhất
Lập đủ phụ tùng ngay từ đầu
+ Gọn chứng từ, dễ đối chiếu
- Phát sinh thêm thì phải lập lệnh mới

**Ảnh hưởng:** màn lệnh sửa chữa, xuất kho, đối chiếu chi phí sửa chữa
**Vì sao đề xuất A:** thiết kế hiện tại không giới hạn số lần xuất trong lúc đang sửa

::: notes
- Ý thứ nhất của OQ-3 ("lệnh có sinh phiếu xuất kho không") SRS đã trả lời: CÓ — trạng thái Đang sửa chữa có hành động Xuất kho cho sửa xe/thay lốp/thay ắc quy (lg-srs-export.md:16980); loại phiếu xuất "Sửa chữa xe" (:16168).
- Đã nghiệm thu → Nhập kho phần dư (:16982) → thiết kế linh hoạt về khối lượng.
- Phiếu xuất kho duyệt 2 lần (:16182) → nhiều phiếu = nhiều lượt duyệt; nếu khách chọn A, xác nhận lại khi trao đổi.
:::

---

<!-- layout: oq; id: OQ-4; src: docs/_shared/object-map.md; recommend: A; group: Xưởng và mua hàng -->
## Báo giá chọn sửa ở xưởng ngoài thì tự tạo đơn mua dịch vụ sửa ngoài?

> Thiết kế hiện tại: báo giá sửa xe Delta tại xưởng ngoài, sau khi được duyệt, sẽ tạo đơn mua dịch vụ sửa chữa ngoài.

### A. Có, tự tạo
+ Không nhập lại thông tin, không sót đơn
- Báo giá phải đủ thông tin xưởng ngoài trước khi duyệt

### B. Bộ phận mua hàng tự lập
+ Mua hàng chủ động chọn và thương lượng
- Nhập hai lần, dễ lệch với báo giá

**Ảnh hưởng:** báo giá, đơn mua dịch vụ, nghiệm thu sửa ngoài của Lái xe
**Vì sao đề xuất A:** đúng thiết kế hiện tại, chỉ cần Delta xác nhận

::: notes
- Nguồn: lưu đồ báo giá, trạng thái Đã phê duyệt → "Tạo đơn mua HHDV (trường hợp sửa xe Delta – Đã có yêu cầu – tại xưởng ngoài)" (lg-srs-export.md:14260).
- Đơn mua loại "Mua dịch vụ sửa chữa xe ngoài" → Chờ nghiệm thu → Lái xe nghiệm thu trên app (:13164, :13181).
:::

---

<!-- layout: oq; id: OQ-7; src: docs/_shared/object-map.md; recommend: A; group: Xưởng và mua hàng -->
## Ai ghi nhận khách hàng đã đồng ý báo giá trên hệ thống?

> Báo giá sửa xe khách hàng và bán phụ tùng phải qua bước khách xác nhận. Thiết kế hiện tại cho nhân viên bấm xác nhận thay khách, nhưng chưa giao quyền này cho vai trò nào.

### A. Cố vấn dịch vụ
Người làm việc trực tiếp với khách, ghi nhận thay khách
+ Nhanh, đúng người nắm trao đổi với khách
- Cần quy định bằng chứng khách đã đồng ý

### B. Giám đốc xưởng
+ Kiểm soát chặt giá bán
- Thêm một bước chờ, chậm phản hồi khách

**Ảnh hưởng:** báo giá, thanh toán trước/sau, lệnh sửa chữa xe khách hàng
**Vì sao đề xuất A:** Cố vấn dịch vụ đã lập, chỉnh báo giá và trao đổi trực tiếp với khách
**Ghi thêm:** có cần đính kèm bằng chứng (ảnh, email, chữ ký khách) không

::: notes
- Nguồn: lưu đồ báo giá (lg-srs-export.md:14250 Chờ xác nhận → Xác nhận/Từ chối xác nhận); lịch sử hoạt động ghi "Đã đại diện khách hàng xác nhận báo giá" (:15419).
- Ma trận quyền: "Xác nhận/từ chối từ khách hàng" (:3315) — chưa tick vai trò nào.
- Khách từ chối → báo giá bị khoá (:14262).
:::

---

<!-- layout: section -->
## Phương tiện và cây dầu

---

<!-- layout: oq; id: OQ-8; src: docs/_shared/object-map.md; group: Phương tiện và cây dầu -->
## Biên bản bàn giao và thu hồi xe ký thế nào, ai ký?

> Thiết kế hiện tại: sau khi yêu cầu được duyệt, biên bản ký trên giấy, nhân viên tải bản scan lên để hoàn tất. Bên nhận có thể là Lái xe hoặc Chi nhánh.

### A. Ký giấy, tải bản scan
Hai bên ký giấy, nhân viên nội bộ tải lên
+ Giữ đúng cách làm quen thuộc
- Phụ thuộc giấy tờ, dễ chậm tải lên

### B. Xác nhận trên Super App
Lái xe xác nhận nhận/trả xe trên app, người giao ký trên Website
+ Có ngay thời điểm và người xác nhận
- Cần thống nhất giá trị pháp lý của xác nhận trên app

**Ảnh hưởng:** bàn giao và thu hồi xe, trách nhiệm khi xe có hư hỏng
**Ghi thêm:** khi Chi nhánh nhận xe thì ai đại diện ký

::: notes
- Nguồn: lưu đồ bàn giao (lg-srs-export.md:29893-29900) và thu hồi (:31059-31066): Đã phê duyệt → Ký biên bản → Đã hoàn thành; UC04.01.05 Ký biên bản = upload file JPG/PNG/PDF (:30936-30990). Bên nhận: Lái xe hoặc Chi nhánh (:30304).
- SRS còn ghi chú "Ký biên bản (common) → check vs anh Toàn" (:3043) → chưa chốt nội bộ, nên KHÔNG đề xuất.
- Phương án B là đề xuất mới của BA (Super App có Lái xe), chưa có trong SRS/SOP.
:::

---

<!-- layout: oq; id: OQ-5; src: docs/_shared/object-map.md; recommend: A; group: Phương tiện và cây dầu -->
## Nhà cung cấp dầu có dùng chung danh sách nhà cung cấp hàng hoá dịch vụ không?

> Thiết kế hiện tại: kế hoạch mua dầu chọn nhà cung cấp từ danh sách nhà cung cấp hàng hoá dịch vụ chung.

### A. Dùng chung
+ Một nơi quản lý thông tin, công nợ nhà cung cấp
- Danh sách dài, cần lọc theo loại hàng

### B. Danh sách riêng cho dầu
+ Gọn khi lập kế hoạch mua dầu
- Một nhà cung cấp có thể phải khai hai lần

**Ảnh hưởng:** kế hoạch mua dầu, đơn mua dầu, thanh toán nhà cung cấp
**Vì sao đề xuất A:** đúng thiết kế hiện tại, chỉ cần Delta xác nhận

::: notes
- Nguồn: UC12.01.02 Tạo kế hoạch mua dầu — điều kiện trước "Nhà cung cấp HHDV đã tồn tại trong hệ thống" (lg-srs-export.md:23658).
- Nếu chọn A: có cần đánh dấu "nhà cung cấp dầu" để lọc không? — hỏi khi trao đổi.
:::

---

<!-- layout: oq; id: OQ-9; src: docs/_shared/object-map.md; recommend: A; group: Phương tiện và cây dầu -->
## Phiếu nhập dầu đã tạo có được rút lại hoặc huỷ không?

> Thiết kế hiện tại: phiếu nhập dầu chờ duyệt rồi được duyệt hoặc từ chối. Duyệt xong tồn bể dầu cập nhật ngay. Chưa có bước rút lại hay huỷ.

### A. Rút lại khi còn chờ duyệt
Giống phiếu xuất kho và đơn mua hàng
+ Người tạo tự sửa sai trước khi duyệt
- Phiếu đã duyệt mà sai vẫn cần cách xử lý riêng

### B. Thêm huỷ phiếu đã duyệt
Huỷ thì trả lại tồn bể dầu
+ Sửa được cả sai sót phát hiện muộn
- Tồn kho thay đổi ngược, khó kiểm soát

### C. Giữ như hiện tại
Sai thì người duyệt từ chối, lập phiếu mới
+ Đơn giản, ít trạng thái
- Người tạo phải chờ người duyệt mới sửa được

**Ảnh hưởng:** nhập dầu, tồn bể dầu, đối chiếu đơn mua dầu
**Vì sao đề xuất A:** giống các chứng từ khác, không phải đảo ngược tồn bể dầu

::: notes
- Nguồn: UC12.02.05 Phê duyệt phiếu nhập dầu (lg-srs-export.md:24962-25018): pending → approved/rejected; duyệt thì tồn bể += delta, nhập từ phương tiện thì tồn phương tiện −= delta.
- Phiếu xuất kho có "Thu hồi yêu cầu" khi Chờ phê duyệt (:16182) → căn cứ phương án A.
- Nếu chọn A: phiếu đã duyệt mà sai thì xử lý thế nào (phiếu điều chỉnh?) — hỏi tiếp.
:::

---

<!-- layout: recap -->
## Tổng kết câu trả lời

---

<!-- layout: bullets -->
## Sau khi nhận câu trả lời
- Đội cập nhật đặc tả phân quyền, xưởng và cây dầu theo câu trả lời của Delta
- Câu chọn **Cần trao đổi thêm**: đội hẹn một buổi ngắn để chốt
- Nếu dùng 5 vai trò mẫu làm khởi đầu: đội gửi bảng quyền để Delta rà

---

<!-- layout: end -->
# Cảm ơn anh/chị
