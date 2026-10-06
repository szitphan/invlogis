---
type: meeting-deck
meeting: open-questions
title: Rà soát câu hỏi mở — Hoàn tiền đơn hàng
client: Khách hàng mẫu
date: 2026-10-08
duration: 45
status: draft
updated: 2026-10-06
links:
  - docs/refund/srs/refund-spec.md
---

<!-- layout: title -->
# Rà soát câu hỏi mở — Hoàn tiền đơn hàng
Chốt 3 điểm còn treo để đội làm tiếp đặc tả

::: notes
Mở đầu 2 phút. Nhắc khách: hôm nay cần quyết, không cần trình bày lại cả tính năng.
:::

---

<!-- layout: goal -->
## Mục tiêu buổi họp
- Chốt **3 câu hỏi** đang chặn đặc tả hoàn tiền
- Câu nào chưa chốt được: thống nhất ai trả lời và hạn
- Thời lượng: 45 phút, khoảng 10 phút mỗi câu

---

<!-- layout: oq; id: OQ-1; src: docs/refund/srs/refund-spec.md; recommend: C; group: Phê duyệt; time: 10 -->
## Hoàn tiền trên bao nhiêu thì cần quản lý duyệt?

> Hiện mọi yêu cầu hoàn tiền đều qua quản lý. Giờ cao điểm có ngày tồn hơn 40 yêu cầu chờ duyệt.

### A. Duyệt tất cả
+ Kiểm soát chặt
- Khách chờ lâu giờ cao điểm

### B. Không cần duyệt
+ Hoàn ngay cho khách
- Rủi ro gian lận

### C. Duyệt khi trên ngưỡng
Ngưỡng do khách đề xuất
+ Cân bằng tốc độ và kiểm soát
- Cần chốt con số ngưỡng

**Ảnh hưởng:** màn duyệt, quy tắc phân quyền, thông báo cho khách

::: notes
- Nguồn: FR-refund-004, BR-refund-002
- Nếu chọn C: hỏi luôn con số ngưỡng (gợi ý 2 triệu theo số liệu tháng 9)
:::

---

<!-- layout: oq; id: OQ-2; src: docs/refund/srs/refund-spec.md; group: Thông báo; time: 5 -->
## Khách có cần nhận thông báo khi yêu cầu hoàn tiền bị từ chối không, qua kênh nào?

::: notes
Câu mở — chưa có phương án, để khách tự trả lời.
:::

---

<!-- layout: recap -->
## Tổng kết quyết định

---

<!-- layout: bullets -->
## Bước tiếp theo
- Cập nhật đặc tả theo quyết định hôm nay
- Gửi biên bản cho khách trong 1 ngày làm việc
- Câu hoãn: hẹn trả lời trước buổi họp tuần sau

---

<!-- layout: end -->
# Cảm ơn anh chị
