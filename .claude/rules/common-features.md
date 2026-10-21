---
paths:
  - "docs/*/brainstorms/**"
  - "docs/*/srs/**"
  - ".claude/skills/brainstorm/**"
  - ".claude/skills/srs/**"
  - ".claude/skills/prd-epic/**"
---

# Common Features — feature nào cũng rà phần dùng chung

> Rule chung cho `/brainstorm`, `/prd-epic`, `/srs`. Feature nghiệp vụ hay quên phần dùng chung (liên
> quy trình, thông báo, lịch sử, thao tác chung, quyền, danh mục), rồi mỗi feature tự làm một kiểu hoặc
> feature chung không biết có ai cần. Rule này bắt ghi nhu cầu ngay khi làm feature. User chốt 2026-10-21.

## 1. Danh sách feature chung — đọc từ PRD, không viết cứng

Nguồn: `docs/_product/prd.md` Feature Map, theme **"Nền tảng"** + nhóm **danh mục cấp doanh nghiệp**
(vd `cross-process-flow`, `common-workspace`, `access-control`, `help-center`, `organization`,
`product-catalog`, `location-catalog`, `cost-catalog`). User thêm feature chung vào PRD dần; rule tự áp.

## 2. Năm nhóm phải rà

| Nhóm | Feature có khi | Ghi gì |
|---|---|---|
| Liên quy trình (`cross-process-flow`) | Có quy tắc liên feature: tạo, chờ hoặc đổi trạng thái bản ghi ở module khác | Các bước của feature trong luồng + bước trước/sau. **Luôn đề xuất đăng ký, không hỏi lại** |
| Thông báo | Gửi, nhắc, cảnh báo, chờ duyệt | Sự kiện · người nhận · kênh |
| Lịch sử hoạt động / thay đổi | Bản ghi sửa, duyệt, huỷ được | Hành động cần lưu · ai xem |
| Thao tác chung (`common-workspace`) | Lưu nháp, xuất, nhập, thao tác hàng loạt, mã bản ghi | Dùng khuôn chung; chỉ ghi phần khác |
| Quyền + danh mục | Đọc danh mục, cần quyền riêng | "chỉ đọc {danh mục}" · quyền cần thêm |

Nhóm chưa có feature chủ trong PRD (vd thông báo — PRD OQ-18; lịch sử hoạt động) → vẫn ghi nhu cầu,
đánh dấu `(chưa có feature)`. KHÔNG bỏ qua vì chưa có chủ.

## 3. Ghi ở đâu

- Brainstorm Mục 7.4 (Bối cảnh hệ thống) / SRS mục tích hợp: bảng **"Dùng chung"** — `Nhóm | Feature chung | Feature này cần | Trạng thái` (`đã có ở {feature}` / `đề xuất`).
- Mỗi dòng `đề xuất` → 1 task backlog "Đưa {nhu cầu} của {feature} vào {feature chung}", Xong khi
  `grep:docs/{feature chung}/…:{feature}`; `(chưa có feature)` → task "Xếp chủ cho {nhu cầu}", `manual`.
- Đang ở worktree `feat/*`: KHÔNG sửa doc của feature chung (rule `worktree.md`) — chỉ ghi bảng + task.

## Tóm tắt 1 dòng

> **Rà 5 nhóm dùng chung theo danh sách PRD · ghi bảng "Dùng chung" · liên feature thì luôn đề xuất
> `cross-process-flow` · nhu cầu chưa có chủ vẫn ghi + task backlog.**
