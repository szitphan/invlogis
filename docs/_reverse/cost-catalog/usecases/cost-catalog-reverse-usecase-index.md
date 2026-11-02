---
type: reverse-usecase-index
feature: cost-catalog
status: draft
updated: 2026-10-20
links:
  - docs/_reverse/cost-catalog/cost-catalog-reverse-spec.md
---

# Khoản mục chi phí cấp 1–3 (`cost-catalog`) — Use Case Index (reverse)

## Use cases

| Slug | Title | Primary Actor | Related FR | Screens | Errors | OQ | Nguồn | Nhãn |
|------|-------|---------------|-----------|---------|--------|-----|-------|------|
| [uc-view-cost-list](./uc-view-cost-list.md) | Xem danh mục chi phí cấp 1, 2, 3 | Người dùng phần mềm xưởng | FR-cost-catalog-001..004 | Danh sách chi phí cấp 1, 2, 3 | — | OQ-6, OQ-7 | SRS Web tr.581, 614, 648 — UC03.10.01, UC03.11.01, UC03.12.01 Xem danh mục chi phí cấp 1, 2, 3 | ✅ |
| [uc-view-cost-detail](./uc-view-cost-detail.md) | Xem thông tin chi phí cấp 1, 2, 3 | Người dùng phần mềm xưởng | FR-cost-catalog-005..008, FR-cost-catalog-021 | Thông tin chi phí cấp 1, 2, 3; popup Lịch sử hoạt động | — | — | SRS Web tr.585, 618, 652 — UC03.10.02, UC03.11.02, UC03.12.02 Xem thông tin chi phí cấp 1, 2, 3 | ✅ |
| [uc-create-cost-proposal](./uc-create-cost-proposal.md) | Tạo đề xuất tạo mới chi phí cấp 1, 2, 3 | Người dùng phần mềm xưởng | FR-cost-catalog-009..012, FR-cost-catalog-022..024 | Tạo mới chi phí cấp 1, 2, 3; popup Huỷ tạo mới | E-cost-catalog-001, E-cost-catalog-003..005 | OQ-1, OQ-9, OQ-10 | SRS Web tr.591, 625, 657 — UC03.10.03, UC03.11.03, UC03.12.03 Tạo đề xuất tạo mới chi phí cấp 1, 2, 3 | ✅ |
| [uc-cancel-cost-proposal](./uc-cancel-cost-proposal.md) | Huỷ đề xuất cấp mới chi phí cấp 1, 2, 3 | Người dùng phần mềm xưởng | FR-cost-catalog-013, FR-cost-catalog-014 | Popup Huỷ đề xuất tạo mới; Thông tin chi phí (Đã huỷ) | — | OQ-11 | SRS Web tr.598, 632, 666 — UC03.10.04, UC03.11.04, UC03.12.04 Huỷ đề xuất cấp mới chi phí cấp 1, 2, 3 | ✅ |
| [uc-approve-reject-cost-proposal](./uc-approve-reject-cost-proposal.md) | Phê duyệt/Từ chối đề xuất cấp mới chi phí cấp 1, 2, 3 | Người dùng phần mềm xưởng (có quyền phê duyệt) | FR-cost-catalog-015..018 | Popup Phê duyệt, Từ chối, Lỗi; Thông tin chi phí (Đã phê duyệt / Đã từ chối) | E-cost-catalog-002 | OQ-2, OQ-5, OQ-12, OQ-14 | SRS Web tr.603, 637, 671 — UC03.10.05, UC03.11.05, UC03.12.05 Phê duyệt/Từ chối đề xuất cấp mới chi phí cấp 1, 2, 3 | ✅ |
| [uc-delete-or-recreate-cost-request](./uc-delete-or-recreate-cost-request.md) | Xoá yêu cầu / Tạo mới yêu cầu từ bản đã huỷ hoặc đã từ chối | Người dùng phần mềm xưởng | FR-cost-catalog-019, FR-cost-catalog-020 | Thông tin chi phí (Đã huỷ / Đã từ chối); popup Xoá yêu cầu | — | OQ-4, OQ-13 | SRS Web tr.589–590, 601–602, 607–608, 623–624, 635–636, 641–642, 655–656, 669–670, 675–676 — UC03.10.02, UC03.10.04, UC03.10.05 (và cấp 2, 3; mô tả trong màn trạng thái Đã huỷ/Đã từ chối) | ✅ |

## Actors

| Actor |
|---|
| Người dùng phần mềm xưởng |
| Người dùng phần mềm xưởng (có quyền phê duyệt) |

## Ghi chú

* Use case **tái lập chưa duyệt** từ SRS cũ — mỗi mệnh đề mang nhãn ✅/🔵/🟡. Chạy `/usecase cost-catalog` (downstream) sau khi có SRS chính thức để điền truy vết đầy đủ.
* Nhóm mục con cùng khuôn (vd các danh mục) viết 1 use case cho cả khuôn; khác biệt từng mục con ở bảng "Khác biệt theo …" trong spec Mục 3.
