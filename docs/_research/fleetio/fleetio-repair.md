---
type: research
keyword: "Fleetio: sự cố, lệnh sửa chữa, lịch sử dịch vụ, mã lỗi, bảo hành, AI"
status: draft
status_changed: 2026-11-03
status_reason: "đã review upstream, không cần sửa"
updated: 2026-11-03
links:
  - docs/_product/prd.md
  - docs/_product/saas-core-vs-tenant.md
  - docs/_research/2026-11-02-fleetio-app-teardown.md
  - docs/_research/fleetio/run-notes/repair.md
---

# Giải pháp tham khảo: Sửa chữa, từ sự cố đến lịch sử dịch vụ

> Khuyến nghị: **Nên tham khảo mạnh** cho `incident-report`, `repair-order`. Vòng đời đã chạy trọn trên Fleetio bằng dữ liệu TEST, gồm cả mở lại và hoàn thành lại. Phần "Đề xuất cho Invlogis" tách riêng; không phần nào là yêu cầu đã chốt với Delta.

## 1. Idea Seed

Mọi lỗi của xe, từ lái xe báo, phiếu kiểm tra hay thiết bị, đổ về **một loại bản ghi Sự cố**. Sự cố có năm lối xử lý: ghi chú, ghi lịch sử, lập lệnh bằng tay, AI soạn lệnh, đưa ra xưởng ngoài; hoặc đóng nếu không làm. Hoàn thành lệnh thì tự sinh Lịch sử dịch vụ, tự giải quyết sự cố, tự ghi số đồng hồ và cập nhật nhắc bảo dưỡng. Kho bị trừ ngay khi lưu dòng phụ tùng, không chờ hoàn thành. Muốn sửa lệnh đã xong thì phải mở lại: lịch sử dịch vụ bị xoá hẳn, sự cố mở lại, nhưng đồng hồ và kho giữ nguyên.

## 2. Context

**Feature Invlogis liên quan:** `incident-report` (Feature Map #15), `repair-quotation` (#16), `repair-order` (#17), đều chưa chi tiết hoá, thuộc Gói Bảo dưỡng đội xe. PRD ghi gói này chưa có mốc trong 6 tháng đầu, nên tài liệu này là đầu vào khi đến lượt, không phải việc của bản thí điểm Điều phối vận tải.

**Khác biệt cần giữ:** Delta có bước **chẩn đoán và báo giá** trước khi lập lệnh, Fleetio không có bước riêng. Fleetio chỉ có thông tin "Last Emailed Quote" trên lệnh, chưa thấy luồng duyệt báo giá.

**Nguồn và bằng chứng:**

- Lượt 1, 2026-11-02, tài khoản dùng thử: Issue #30, #31; Work Order #99, #100; Service Entry #57837459.
- Lượt 2, 2026-11-03, cùng tài khoản: xe TEST-SUA-01 (loại Car); Issue #33 đến #38, #45, #46; Work Order #103, #104, #106, #107; Service Entry 57856983, 57857945 (đã tự bị xoá), 57858956. Kho và đơn mua lấy từ lượt chạy nhóm Kho (WO #102, PO #2, PO #3). Bảo hành lấy từ lượt chạy nhóm Phương tiện (WO #100).
- Giới hạn chung: tài khoản một người dùng có toàn quyền, chạm trần số xe nên chỉ chạy trên xe Car. Xoá lệnh không chạy vì là xoá vĩnh viễn.

| Nhãn | Nghĩa |
|---|---|
| **Chạy** | Đã thao tác và thấy kết quả |
| **Xem** | Thấy trên giao diện, chưa thao tác hết |
| **Docs** | Đọc từ tài liệu công khai của Fleetio |
| **Suy** | Kết luận rút ra, chưa kiểm chứng |
| **GĐ** | Giả định của người viết |

## 3. User Types (preliminary)

| User Type | Pain Point | Primary Need |
|---|---|---|
| Lái xe | Báo lỗi qua điện thoại, dễ thất lạc | Báo nhanh, biết đã có người nhận |
| Nhân viên xưởng | Sự cố nằm rải rác, nhập lại nhiều lần | Một danh sách việc, lập lệnh từ sự cố |
| Quản lý phương tiện | Không biết xe nào đang hỏng gì | Nhìn trạng thái sự cố và chi phí theo xe |
| Kế toán | Chi phí sửa thiếu căn cứ | Chi phí tách công, phụ tùng, gắn đúng xe |

### 3.1 Tác vụ chính

| Vai trò | Tác vụ | Tần suất | Mức quan trọng | Ghi chú |
|---|---|---|---|---|
| Lái xe | Báo sự cố | Mỗi ngày | Cao | Báo sót thì xe chạy tiếp với lỗi |
| Nhân viên xưởng | Lập và đóng lệnh | Mỗi ngày | Cao | Đóng sai làm sai chi phí và lịch sử |
| Quản lý phương tiện | Xếp ưu tiên, giao việc | Mỗi ngày | Cao | Sai ưu tiên làm xe nằm lâu |
| Kế toán | Đối chiếu chi phí lệnh | Mỗi tuần | Trung | Sai số tiền ảnh hưởng thanh toán |

## 4. Capabilities Breakdown

### P0 — must have

- R1 [Mới] [Gói: Bảo dưỡng đội xe] **Một loại Sự cố cho mọi nguồn**, có cột Nguồn: lái xe, phiếu kiểm tra, thiết bị. Fleetio: `Chạy` (Issue #31 sinh từ phiếu kiểm tra, có liên kết về phiếu). Áp vào `incident-report`.
- R2 [Mới] [Gói: Bảo dưỡng đội xe] **Một lệnh giải quyết nhiều sự cố**, tick chọn ngay trên form lệnh; form tự liệt kê sự cố đang mở của xe. Fleetio: `Chạy` (#35 và #37 cùng Resolved khi #104 hoàn thành). Áp vào `repair-order`.
- R3 [Mới] [Gói: Bảo dưỡng đội xe] **Hoàn thành lệnh kéo theo dây chuyền:** sinh lịch sử dịch vụ, chuyển sự cố sang Resolved, ghi số đồng hồ (`Chạy` #99, #104); cập nhật nhắc (`Chạy` ở nhóm Nhắc, lệnh #101). Áp vào `repair-order`.
- R4 [Mới] [Gói: Bảo dưỡng đội xe] **Dòng việc tách công và phụ tùng**, cộng dồn lên đầu lệnh. Fleetio: `Chạy`, nhưng số tiền VND lệch (R24). Áp vào `repair-order`.
- R5 [Mới] [Gói: Bảo dưỡng đội xe] [Cấu hình] **Bắt buộc số đồng hồ khi hoàn thành lệnh**, bật tắt theo khách, loại trừ được theo loại xe. Fleetio: `Chạy` luật đang bật, `Xem` ô loại trừ. Tham số mới, chưa có mã.
- R6 [Mới] [Gói: Bảo dưỡng đội xe] **Khoá sửa sau khi hoàn thành**; muốn sửa phải đổi trạng thái có xác nhận. Fleetio: `Chạy` (nút Edit của lệnh và Service Entry bị khoá).
- R7 [Mới] [Lõi] **Dòng thời gian trên bản ghi:** ai làm gì, kể cả "do workflow" hay "từ bản nháp AI". Fleetio: `Chạy`, nhưng không ghi đóng, mở lại, gỡ khỏi lệnh (R27). Đề xuất Invlogis ghi đủ.
- R22 [Mới] [Gói: Bảo dưỡng đội xe] **Quá hạn là giá trị tính, không phải trạng thái lưu**: so ngày hoặc đồng hồ với hạn mỗi khi đọc. Đồng hồ tăng là tự sang Overdue, đổi hạn là tự về Open, không cần tác vụ nền. Fleetio: `Chạy`. Đáng học vì số km đầu kéo đổi liên tục.
- R23 [Mới] [Gói: Bảo dưỡng đội xe] **Một sự cố chỉ ở một lệnh**: dòng đã thuộc lệnh khác có ổ khoá, ba lối xử lý khác bị khoá kèm lý do. Fleetio: `Chạy`. Tránh hai xưởng cùng sửa một lỗi.
- R25 [Mới] [Gói: Bảo dưỡng đội xe] **Trừ kho khi lưu dòng phụ tùng, có bút toán đảo khi sửa, xoá dòng**, ghi nguồn là số lệnh; chọn được không trừ kho. Fleetio: `Chạy`. Hợp xưởng cấp phụ tùng trước khi sửa. Hoàn thành và mở lại lệnh không tạo dòng kho.

### P1 — should have

- R8 [Mới] [Gói: Bảo dưỡng đội xe] [Cấu hình] **Trạng thái lệnh do khách thêm**, mỗi trạng thái thuộc nhóm Chưa xong hoặc Hoàn thành. Fleetio: `Xem` bảng 3 trạng thái mặc định, chưa thêm thử.
- R9 [Mới] [Gói: Bảo dưỡng đội xe] **Năm cách xử lý sự cố:** thêm vào lịch sử, AI soạn lệnh, thêm vào lệnh, đưa ra xưởng ngoài, giải quyết kèm ghi chú. Fleetio: `Chạy` bốn nhánh; đưa ra xưởng ngoài chỉ `Xem` hộp giới thiệu, cần bật Shop Network. Áp vào `incident-report`.
- R10 [Mới] [Gói: Bảo dưỡng đội xe] **Xem lệnh theo danh sách, lịch, lịch tài nguyên.** Fleetio: `Chạy` chuyển chế độ.
- R11 [Mới] [Gói: Bảo dưỡng đội xe] [Cấu hình] **Khung Triệu chứng, Nguyên nhân, Cách khắc phục** cho từng dòng việc, bật được bắt buộc trước khi hoàn thành. Fleetio: `Docs` phần bắt buộc; `Chạy` thấy ba ô Complaint, Cause, Correction trên cơ hội bảo hành.
- R12 [Mới] [Gói: Bảo dưỡng đội xe] [Cấu hình] **Tổng hợp chi phí:** markup công, markup phụ tùng, tín dụng bảo hành, giảm giá, thuế. Fleetio: `Xem`. Hợp với `service-sales-payment` khi sửa cho khách ngoài.
- R13 [Mới] [Gói: Bảo dưỡng đội xe] **Ghi thẳng lịch sử dịch vụ** cho việc sửa ngoài, không cần lập lệnh; entry không cần dòng việc vẫn giải quyết được sự cố. Fleetio: `Chạy` (entry 57856983).
- R14 [Mới] [Gói: Bảo dưỡng đội xe] **Cảnh báo cơ hội bảo hành** ngay trên lệnh, khớp theo mã phân loại của đầu việc, không theo phụ tùng. Fleetio: `Chạy` (WO #100 hiện "Warranty Opportunities (1)" sau khi thêm đầu việc khớp mã).
- R15 [Mới] [Cấu hình] **Sao chép lệnh, in, gửi PDF.** Fleetio: `Chạy` sao chép, in; `Xem` gửi PDF.
- R26 [Mới] [Gói: Bảo dưỡng đội xe] **Giải quyết bằng ghi chú bắt buộc, đóng bằng ghi chú tuỳ chọn:** hai ý nghĩa khác nhau, có đã làm và không làm. Resolve bắt buộc ghi đã làm gì; Close không. Fleetio: `Chạy`.
- R28 [Mới] [Gói: Bảo dưỡng đội xe] **Phân loại Scheduled, Non-Scheduled, Emergency** trên lệnh. Fleetio: `Chạy`. Chỉ học ba mức, không chép hệ mã VMRS.
- R29 [Mới] [Gói: Bảo dưỡng đội xe] **Nhận hàng từ đơn mua thẳng vào lệnh qua hai bước kho:** cộng kho trước, trừ khi lưu lệnh; huỷ form thì hàng vẫn ở kho. Fleetio: `Chạy`. Hợp phụ tùng đặt riêng cho xe nằm xưởng.

### P2 — nice to have

- R16 [Mới] [Gói: Bảo dưỡng đội xe] **AI xếp ưu tiên sự cố** từ nội dung, ghi rõ "Auto-assigned". Fleetio: `Chạy` với câu tiếng Anh (High, Low) và một câu tiếng Việt (Medium); có sự cố vẫn "No Priority".
- R17 [Mới] [Gói: Bảo dưỡng đội xe] **AI soạn nháp lệnh chạy nền**, báo khi xong, người dùng duyệt từng việc rồi mới tạo; **gom sự cố khác cùng xe và cảnh báo xe đang có lệnh mở**. Fleetio: `Chạy`, mất khoảng 30 đến 40 giây. Gom việc đỡ đưa đầu kéo vào xưởng hai lần.
- R18 [Mới] [Gói: Bảo dưỡng đội xe] **AI đánh giá lệnh** (kiểm công, giá phụ tùng), kết luận, ghi nguồn, cho chạy lại khi lệnh đổi; phát hiện lệnh khác cùng xe trùng việc. Fleetio: `Chạy`. Giá trị thấp nếu không có dữ liệu giá Việt Nam: lệnh phụ tùng 30 triệu vẫn "Acceptable".
- R19 [Mới] [Gói: Bảo dưỡng đội xe] **Nhận mã lỗi từ thiết bị**, gom và tạo sự cố. Fleetio: `Xem` bảng mẫu, có menu Create Issue, Ignore, View Fault Rule. Áp vào `vehicle-telematics`, phụ thuộc thiết bị.
- R20 [Mới] [Gói: Bảo dưỡng đội xe] **Theo dõi bảo hành xe và phụ tùng** theo ngày và số km, có mẫu Standard, Extended; khai cho nhiều xe một lượt. Fleetio: `Chạy`.
- R21 [Mới] [Gói: Bảo dưỡng đội xe] **Danh mục đầu việc:** giờ công dự kiến, phụ tùng đi kèm, lưu trữ thay vì xoá. Fleetio: `Chạy` tạo và lưu trữ; không thấy gộp đầu việc. Chỉ học cấu trúc, không chép hệ mã VMRS của Mỹ. Áp vào `product-catalog`.

### Điểm yếu cần làm khác

- R24 [Mới] [Lõi] **Tiền không có số lẻ phải đúng ở mọi màn.** Fleetio: `Chạy` lệch 100 lần với VND giữa các màn (Mục 6.5). Invlogis cần ca kiểm thử riêng cho định dạng tiền Việt và tiền không có số lẻ.
- R27 [Mới] [Gói: Bảo dưỡng đội xe] **Mở lại phải giữ vết:** ai mở, vì sao, lần hoàn thành trước. Fleetio: `Chạy` xoá hẳn entry, xoá dòng trên Timeline, hộp xác nhận không báo. Đề xuất Invlogis không xoá, chuyển bản cũ sang trạng thái đã huỷ.
- R30 [Mới] [Gói: Bảo dưỡng đội xe] **Đảo đồng hồ khi mở lại, không ghi trùng khi hoàn thành lại.** Fleetio: `Chạy` giữ nguyên dòng cũ và thêm dòng trùng. Đề xuất Invlogis: một lần hoàn thành một dòng, huỷ theo lần mở lại.
- R31 [Mới] [Gói: Bảo dưỡng đội xe] [Cấu hình] **Không cho tồn âm âm thầm.** Fleetio: `Chạy` xuất quá tồn không cảnh báo. Đề xuất Invlogis cảnh báo, chặn hay không theo khách; tham số mới, chưa có mã.

## 5. Core Flows (Happy Path)

### 5.1 Từ sự cố đến lịch sử dịch vụ

`Chạy` với Issue #35, #37, Work Order #104, và lượt trước Issue #30, Work Order #99.

1. Người dùng tạo sự cố, chọn xe, ghi tóm tắt, có thể đặt hạn theo ngày hoặc đồng hồ. Hệ thống tự điền người báo, thời điểm, AI xếp ưu tiên.
2. Người dùng chọn cách xử lý. Nếu chọn AI, bản nháp chạy nền và báo khi xong.
3. Người dùng duyệt nháp, bỏ chọn việc không cần, tạo lệnh. Sự cố tự gắn vào "Resolved Issues" và bị khoá các lối xử lý khác.
4. Xưởng nhập công, phụ tùng. Lưu dòng phụ tùng có kho là tồn giảm ngay.
5. Xưởng đổi Open và Pending tuỳ ý. Đổi Completed cần Started At và số đồng hồ đầu theo cài đặt.
6. Hệ thống sinh lịch sử dịch vụ, chuyển sự cố sang Resolved, ghi đồng hồ, tính Time to Resolve, Kilometers to Resolve, khoá lệnh, entry và nút Reopen của sự cố.

```
Sự cố ──> [AI soạn nháp] ──> Duyệt nháp ──> Lệnh Open ── lưu dòng phụ tùng ──> Tồn giảm
                                              │
                                     Pending ⇄ Open
                                              │
                         Started At + đồng hồ đầu theo cài đặt
                                              │
                                         Completed
                 ┌───────────────┬────────────┴───┬──────────────┐
          Lịch sử dịch vụ   Sự cố Resolved   Số đồng hồ của xe   Nhắc bảo dưỡng
```

### 5.2 Từ phiếu kiểm tra hỏng đến lệnh

`Chạy` với Submission #125988723, Issue #31, Work Order #100.

1. Lái xe nộp phiếu, một mục Không đạt.
2. Workflow của biểu mẫu tạo sự cố, tiêu đề dạng "[Inspection Item] Brakes [Answer] Fail", có mô tả tự sinh và liên kết về phiếu.
3. Xưởng lập lệnh, tick sự cố vào lệnh.

```
Phiếu kiểm tra ── mục Không đạt ──> Sự cố (do workflow) ──> Lệnh sửa
```

### 5.3 Ba lối xử lý không qua lệnh

`Chạy` với #35, #36, #37, #38.

```
Sự cố ─ Resolve with Note (ghi chú bắt buộc) ─> Resolved ─ Reopen ─> Open
Sự cố ─ Add to Service Entry ─ lưu entry ─────> Resolved ─ Reopen ─> Open, entry còn
Sự cố ─ Close (ghi chú tuỳ chọn) ─────────────> Closed   ─ Reopen ─> Open
```

### 5.4 Mở lại và hoàn thành lại lệnh

`Chạy` với #104.

```
Completed ─ đổi về Open, xác nhận ─> Entry bị xoá, Sự cố Open; đồng hồ và tồn giữ nguyên
Open ─ sửa dòng ─> xoá dòng phụ tùng thì tồn tăng lại
Open ─ Completed lần 2 ─> Entry mới, ngày cũ giữ nguyên, thêm dòng đồng hồ trùng
```

### 5.5 Đề xuất cho Invlogis: chèn bước chẩn đoán, báo giá

Đề xuất, chưa đối chiếu với SOP Delta.

```
Sự cố ──> Chẩn đoán ──> Báo giá ──> Duyệt ──> Lệnh sửa ──> Hoàn thành
              (repair-quotation)                (repair-order)
```

### 5.6 Đầu kéo, mooc

`Chạy` ở nhóm Lốp: mooc là một Vehicle độc lập, đồng hồ riêng. `Suy` cho nhóm này vì lượt sửa chữa chỉ chạy trên xe Car: sự cố và lệnh gắn với một Vehicle duy nhất, nên hỏng cả đầu kéo và mooc phải tạo hai lệnh, không gom được. Đề xuất Invlogis: lệnh gắn được tổ hợp đầu kéo cùng mooc, số km theo từng thành phần. Tham khảo `lab-combo.html` khi thiết kế.

## 6. System Behavior Deep Dive

### 6.1 Decision Points

| ID | Flow | Khi nào | YES | NO |
|---|---|---|---|---|
| D1 | 5.1 | Sự cố có cần sửa không | Lập hoặc thêm vào lệnh | Close, ghi chú tuỳ chọn |
| D2 | 5.1 | Xe đã có lệnh đang mở | Nháp AI cảnh báo, cho thêm vào lệnh đó | Tạo lệnh mới |
| D3 | 5.1 | Sửa ở xưởng nhà | Lệnh sửa | Ghi Service Entry hoặc đưa ra xưởng ngoài |
| D4 | 5.1 | Đủ Started At và số đồng hồ đầu khi đổi Completed | Cho hoàn thành | Chặn, trạng thái giữ nguyên |
| D5 | 5.2 | Mục kiểm tra Không đạt | Tạo sự cố theo workflow | Không tạo |
| D6 | 5.1 | Sự cố đã nằm ở một lệnh | Khoá ba lối, ổ khoá ở form lệnh khác | Tự do chọn lối |
| D7 | 5.3 | Sự cố giải quyết bằng lệnh | Reopen khoá, phải mở lại lệnh | Reopen mở |
| D8 | 5.1 | Dòng phụ tùng có chọn kho | Trừ tồn khi lưu | "None" không trừ |

### 6.3 State Transitions

```
Sự cố: Open ──> Resolved ──> (Reopen, khoá nếu do lệnh)
          └───> Closed ──> (Reopen)
       Overdue là giá trị tính trên Open, không lưu
Lệnh:  Open ⇄ Pending ──> Completed ──> Open hoặc Pending (xác nhận)
```

| Entity | Từ | Sang | Trigger | Quay lại được? | Bằng chứng |
|---|---|---|---|---|---|
| Sự cố | Open | Resolved | Lệnh chứa nó hoàn thành | Nút Reopen khoá, phải mở lại lệnh | `Chạy` |
| Sự cố | Open | Resolved | Lưu Service Entry | Có, Reopen chạy được, entry còn, mất liên kết | `Chạy` |
| Sự cố | Open | Resolved | Resolve with Note | Có, Reopen | `Chạy` |
| Sự cố | Open | Closed | Close, ghi chú tuỳ chọn | Có, Reopen | `Chạy` |
| Lệnh | Open | Pending | Đổi trạng thái, không hỏi | Có | `Chạy` |
| Lệnh | Open, Pending | Completed | Đổi trạng thái, đủ điều kiện | Có; mở lại thì Service Entry bị xoá hẳn | `Chạy` |

Ma trận đủ: [[docs/_research/fleetio/srs/fleetio-repair-states.md|States]].

### 6.4 Interrupted Transactions

| Tình huống | Hệ thống còn lại gì | Resume | Cleanup |
|---|---|---|---|
| AI soạn nháp chưa xong, người dùng rời trang | Nháp vẫn chạy nền | Thông báo, dải "Review draft" trên sự cố | Nút Discard, mất ngay, không hỏi |
| Đổi sang Completed mà thiếu điều kiện | Lệnh giữ nguyên trạng thái | Sửa rồi đổi lại | Không có |
| Bỏ dở form có dữ liệu | Trình duyệt chặn "Leave site?" | Ở lại trang | Không có bản nháp tự lưu |
| Mở lại lệnh, tác vụ nền chưa xong | Trang vẫn hiện Completed vài giây, toast "Restoring Work Order #104 data" | Chờ rồi tải lại | Không có |
| Nhận hàng đơn mua vào lệnh mới rồi huỷ form | Hàng ở lại kho, đơn thành Full, không có lệnh | Lập lệnh sau, lấy từ kho | Không có |

### 6.5 Other Edge Cases

- **Điểm không nên học, nháp AI:** bản nháp ghi sẽ tự điền Repair Priority Class là Non-Scheduled, nhưng lệnh tạo ra để trống trường này (`Chạy` hai lần: #99, #106).
- **Điểm không nên học, trùng số đồng hồ:** #99 sinh 3 dòng gồm 2 dòng 1.010 km từ Work Order và Service Entry; #104 lần đầu chỉ 2 dòng nguồn lệnh, hoàn thành lần 2 mới có dòng 2.350 km trùng nguồn entry (`Chạy`). Điều kiện sinh dòng trùng chưa rõ. Invlogis nên ghi một lần.
- **Điểm không nên học, lưu form trống:** form Issue trống chỉ báo "You are not authorized to perform this action." thay vì chỉ trường thiếu (`Chạy`, một lần, chưa rõ nguyên nhân).
- **Điểm không nên học, lệch tiền (sửa lại so với bản trước):** hộp Add Part không lưu sai số. Form trước lưu và form sửa đều đúng; chỉ trang chi tiết lệnh và Service Entry hiện gấp 100 lần. `Chạy`: phụ tùng 300.000 hiện 30.000.000 ₫, 5 hiện 500 ₫, 12,5 hiện 1.250 ₫. Ở chiều ngược lại, kỹ thuật viên mẫu ghi 480.000 ₫/hr trong danh sách nhưng đưa vào dòng thành 4.800 ₫; contact nhập 100.000 thì danh sách ghi 10.000.000 ₫/hr. Mỗi màn nhân hoặc chia 100 khác nhau, không có cách sửa tay.
- **Điểm không nên học, mở lại không báo hậu quả:** hộp xác nhận chỉ nói khôi phục dữ liệu archive, không nói entry bị xoá, sự cố mở lại (`Chạy`).
- **Điểm không nên học, hoàn thành lại giữ ngày cũ:** Time to Resolve vẫn 23 mins dù hoàn thành lại sau 41 phút (`Chạy`).
- **Điểm không nên học, AI nêu sai:** Assessment vẫn "Acceptable" với phụ tùng 30 triệu, và ghi "the open overdue-by-date issue" khi #33 đã đổi hạn sang tương lai (`Chạy`).
- **Điểm không nên học, tick không vào:** tick #33, #34, #38 khi tạo #103, sau lưu chỉ có #38, #33; #34 không vào, không báo, nhưng cột Work Orders vẫn ghi #103 và bị khoá ở lệnh mới (`Chạy`, chưa rõ nguyên nhân).
- **Điểm không nên học, dữ liệu mẫu làm kẹt lệnh:** chọn kỹ thuật viên mẫu lúc tạo lệnh thì qua, về sau mọi lần sửa đều báo lỗi, lệnh #103 không đổi được trạng thái (`Chạy`).
- **Điểm không nên học, số đồng hồ thấp:** Service Entry 2.100 km khi xe đang 2.200 km vẫn lưu, không cảnh báo (`Chạy`).
- **Điểm không nên học, dấu vết thiếu:** Timeline không ghi đổi Overdue, đóng, mở lại, gỡ khỏi lệnh. Sau khi Reopen sự cố resolved bằng entry, Timeline vẫn giữ "Issue Resolved by service entry" như chưa mở lại (`Chạy`).
- **Assessment không chạy** khi chưa có đầu việc, chưa có chi phí dòng việc, hoặc entry chưa có dòng (`Chạy`).
- **Không xảy ra:** tạo sự cố với hạn đã qua không bị chặn; mở lại lệnh không hoàn đồng hồ, không hoàn kho; hoàn thành lệnh không ghi sổ kho; sao chép lệnh không chép sự cố, ngày, đồng hồ.

## 7. Validation, Limits & Wording

### 7.1 Validation rules

| Field | Rule | Bằng chứng |
|---|---|---|
| Sự cố | Bắt buộc xe, ngày báo, tóm tắt | `Xem` |
| Hạn sự cố | Quá hạn khi ngày qua Due Date hoặc đồng hồ vượt Due Odometer; đúng bằng không tính quá hạn; không chặn hạn trong quá khứ | `Chạy` |
| Lệnh | Bắt buộc xe, trạng thái, ngày lập | `Xem` |
| Số đồng hồ đầu | Có số thì bắt buộc ngày bắt đầu thực tế | `Chạy` |
| Hoàn thành lệnh | Bắt buộc Started At; số đồng hồ đầu theo cấu hình | `Chạy` |
| Số đồng hồ cuối | Có số thì bắt buộc Actual Completion Date; phải lớn hơn hoặc bằng số đầu | `Chạy` |
| Service Entry | Bắt buộc Odometer, Completion Date; không cần dòng việc; ô ngày hiện giờ hiện tại nhưng chỉ là placeholder | `Chạy` |
| Ghi chú | Resolve bắt buộc; Close tuỳ chọn | `Chạy` |
| Đầu việc | Tên không trùng; Save khoá tới khi Continue hết 6 bước | `Chạy` |
| Dòng công | Contact mẫu không dùng được với xe không mẫu khi sửa lệnh | `Chạy` |
| Cấu hình thêm | Bắt buộc phân loại ưu tiên, lý do sửa, nhóm hệ thống; bắt buộc nộp phiếu kiểm tra | `Xem`, đều đang tắt |

### 7.2 Limits & Quotas (exact values)

| Tham số | Giá trị | Window | Behavior khi vượt |
|---|---|---|---|
| Số lệnh tiếp theo | Khách tự đặt; ô trên form chỉ là số dự kiến | Toàn tài khoản | Trùng thì tự nhảy số, không lỗi (`Chạy`, form hiện 101, lưu thành #103) |
| Số lần mở lại lệnh | Không thấy giới hạn | Hai lượt thử | Chưa chạm trần |
| Số xe tài khoản dùng thử | Có trần | Toàn tài khoản | Nút Save Vehicle khoá, TEST-SUA-02 không tạo được |
| Danh mục đầu việc | Fleetio: 400 đầu việc chuẩn | Toàn tài khoản | Không áp dụng |

### 7.3 Wording samples (exact strings)

#### Error messages

| Tình huống | Wording | Code |
|---|---|---|
| Có số đồng hồ, thiếu ngày bắt đầu | "Start Odometer is invalid" và "can't be blank if an odometer value is entered" | E-fleetio-repair-001 |
| Lưu lệnh lỗi | "Work Order could not be updated" | E-fleetio-repair-001, 008, 011 |
| Hoàn thành thiếu số cuối | "Please edit and fix the following errors: Ending Meter Entry can't be blank (per your account settings)" | E-fleetio-repair-002 |
| Hoàn thành thiếu ngày bắt đầu | "Please edit and fix the following errors: Started At can't be blank" | E-fleetio-repair-006 |
| Hoàn thành thiếu đồng hồ đầu | "Starting Meter Entry can't be blank (per your account settings)", "Odometer can't be blank (per your account settings)" | E-fleetio-repair-007 |
| Số cuối nhỏ hơn đầu | "Completion Odometer must be greater than or equal to start meter entry." | E-fleetio-repair-009 |
| Kỹ thuật viên mẫu | "Contact is a sample, and cannot be used with non sample vehicles" | E-fleetio-repair-010 |
| Trùng tên đầu việc | "has already been taken", "Service Task could not be created" | E-fleetio-repair-013 |

#### Success messages

| Tình huống | Wording |
|---|---|
| Tạo lệnh từ nháp | "Work Order successfully created. Created from an AI draft from Issue #30" |
| Đổi trạng thái lệnh | "Work Order was successfully updated" |
| Đóng, giải quyết sự cố | "Issue #36 was closed.", "Issue #35 was resolved." |
| Mở lại sự cố | "Successfully reopened Issue." |
| Xoá dòng phụ tùng | "Removed Part: TEST-BRAKE-PAD-01" |

#### Info / neutral messages

| Tình huống | Wording |
|---|---|
| AI đang soạn | "Drafting service for this issue. No need to wait here — we'll notify you when the draft is ready." |
| Nháp xong | "Work Order drafted. Ready for your review." |
| Xe đang có lệnh mở | "A Work Order is already open for this vehicle" |
| Lệnh đổi sau đánh giá | "Rerun available. This work order has been updated since the assessment was run." |
| Sự cố đã ở lệnh | "Issue already added to a Work Order. Remove it from all Work Orders to add it to another." |
| Reopen khoá | "Reopen work order #104 to reopen this issue." |
| Mở lại lệnh | "Changing this completed Work Order to an incomplete Status will automatically restore any archived parts, part locations, and contacts associated with line items. Are you sure you wish to continue?" |

Câu "(per your account settings)" đáng học: nói rõ luật đến từ cấu hình của khách. Câu tooltip Reopen cũng đáng học: khoá kèm cách mở.

## 8. Assumptions

- `GĐ` Delta muốn gom sự cố về một nơi; chưa hỏi.
- `GĐ` Lái xe báo sự cố qua Delta Super App, không phải web.
- `GĐ` Chi phí lệnh sửa đi vào `cost-catalog`; cách ghi nhận cụ thể chưa thiết kế.

## 9. Risks

| Rủi ro | Mức | Giảm thiểu |
|---|---|---|
| Tự động hoá dây chuyền làm sai nhiều bản ghi cùng lúc khi đóng nhầm lệnh | Cao | Mở lại có kiểm soát, giữ vết, đảo đủ đồng hồ và lịch sử (R27, R30) |
| Trừ kho từ lúc lưu, lệnh Open nằm lâu làm tồn sổ thấp hơn thực tế; hoàn kho chỉ khi xoá dòng | Trung | Báo cáo tồn đã cấp cho lệnh chưa hoàn thành |
| Sai số tiền ở chi tiết lệnh làm sai chi phí theo xe | Cao | Ca kiểm thử tiền Việt ở mọi màn (R24) |
| AI xếp ưu tiên sai với chữ tiếng Việt, từ địa phương | Trung | Cho sửa tay, đo tỉ lệ sửa trước khi bật mặc định |
| AI đánh giá kết luận sai mà trông đáng tin | Trung | Không dùng kết luận làm điều kiện duyệt; chỉ gợi ý |
| Sao chép mô hình đội xe Mỹ, bỏ sót bước báo giá của Delta | Cao | Lấy SOP Delta làm gốc, Fleetio chỉ tham khảo |
| Mô hình một Vehicle không gom đầu kéo cùng mooc | Trung | Thiết kế lệnh theo tổ hợp (Mục 5.6) |

## 10. Success Criteria (preliminary)

- Mọi sự cố có nguồn và trạng thái rõ; không còn sự cố nằm ngoài hệ thống.
- Hoàn thành lệnh không phải nhập lại ở nơi khác.
- Chỉ số thời gian xử lý sự cố lấy được tự động (Fleetio có Time to Resolve, Kilometers to Resolve).
- Mọi lần mở lại đều truy được ai, khi nào, vì sao.

## 11. Open Questions

| ID | Câu hỏi | Trả lời hiện có | Nguồn khách |
|---|---|---|---|
| OQ-1 | Delta có muốn gom sự cố từ lái xe, kiểm tra, thiết bị về một loại bản ghi không? | Fleetio có gom. Quyết định của Delta còn mở | Chưa có trong tài liệu khách gửi |
| OQ-2 | Một lệnh có được giải quyết nhiều sự cố của cùng xe không? | Fleetio có. Quyết định của Delta còn mở | Chưa có trong tài liệu khách gửi |
| OQ-3 | Hoàn thành lệnh xong có được mở lại không, ai được làm? | Fleetio cho mở, tài khoản một người nên chưa thử phân quyền. Quyết định của Delta còn mở | Chưa có trong tài liệu khách gửi |
| OQ-4 | Sửa ngoài có cần lập lệnh hay chỉ ghi lịch sử? | Fleetio chạy được chỉ ghi lịch sử. Quyết định của Delta còn mở | Chưa có trong tài liệu khách gửi |
| OQ-5 | Thiết bị GPS của Delta có đọc được mã lỗi động cơ không? | Chưa có | Chưa có trong tài liệu khách gửi |
| OQ-6 | Delta có theo dõi bảo hành xe, phụ tùng không? | Chưa có | Chưa có trong tài liệu khách gửi |
| OQ-7 | Delta có cần lệnh gom cả đầu kéo và mooc không? | Fleetio không gom (`Suy`) | Chưa có trong tài liệu khách gửi |
| OQ-8 | Xưởng Delta cấp phụ tùng lúc lập lệnh hay lúc xong việc? Quyết định thời điểm trừ kho | Fleetio trừ khi lưu | Chưa có trong tài liệu khách gửi |

## 12. Next Steps

- Review cùng user, chọn ý đưa vào `/brainstorm incident-report` và `/brainstorm repair-order` khi đến lượt Gói Bảo dưỡng đội xe.
- Đối chiếu với bộ tài liệu cũ `docs-input/srs-cu/lg-srs-export.md` trước khi đề xuất với Delta.
