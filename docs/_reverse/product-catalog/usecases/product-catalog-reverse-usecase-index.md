---
type: reverse-usecase-index
feature: product-catalog
status: draft
updated: 2026-10-15
links:
  - docs/_reverse/product-catalog/product-catalog-reverse-spec.md
---

# Danh mục hàng hoá và dịch vụ kỹ thuật (`product-catalog`) — Use Case Index (reverse)

## Use cases

| Slug | Title | Primary Actor | Related FR | Screens | Errors | OQ | Nguồn | Nhãn |
|------|-------|---------------|-----------|---------|--------|-----|-------|------|
| [uc-view-catalog-list](./uc-view-catalog-list.md) | Xem danh sách danh mục (5 danh mục) | Người dùng phần mềm xưởng | FR-product-catalog-001..004 | Danh sách DVKT / PTVT / CCDC / lốp / ắc quy | — | OQ-11, OQ-12, OQ-17, OQ-18 | SRS Web tr.288, 325, 361, 394, 427 — Xem danh mục (UC03.01.01, UC03.03.01, UC03.04.01, UC03.05.01, UC03.06.01) | ✅ |
| [uc-view-catalog-detail](./uc-view-catalog-detail.md) | Xem thông tin bản ghi danh mục (gồm Xoá / Tạo mới yêu cầu) | Người dùng phần mềm xưởng | FR-product-catalog-005..008, FR-product-catalog-018, FR-product-catalog-019, FR-product-catalog-021, FR-product-catalog-022 | Thông tin DVKT / PTVT / CCDC / lốp / ắc quy; popup Xác nhận xoá; popup Lịch sử hoạt động | — | OQ-3, OQ-4, OQ-10, OQ-16 | SRS Web tr.293, 329, 365, 399, 432 — Xem thông tin (UC03.01.02, UC03.03.02, UC03.04.02, UC03.05.02, UC03.06.02) | ✅ |
| [uc-create-catalog-request](./uc-create-catalog-request.md) | Tạo đề xuất tạo mới bản ghi danh mục | Người dùng phần mềm xưởng | FR-product-catalog-009..011, FR-product-catalog-020, FR-product-catalog-021 | Tạo mới DVKT / PTVT / CCDC / lốp / ắc quy; hộp thoại xác nhận huỷ tạo mới | E-product-catalog-001..002, E-product-catalog-005 | OQ-1, OQ-5, OQ-7, OQ-9, OQ-13, OQ-15, OQ-20, OQ-22, OQ-24, OQ-25, OQ-26 | SRS Web tr.298, 334, 370, 404, 437 — Tạo đề xuất tạo mới (UC03.01.03, UC03.03.03, UC03.04.03, UC03.05.03, UC03.06.03) | ✅ |
| [uc-cancel-catalog-request](./uc-cancel-catalog-request.md) | Huỷ đề xuất cấp mới | Người dùng phần mềm xưởng | FR-product-catalog-012, FR-product-catalog-016, FR-product-catalog-020, FR-product-catalog-021 | Popup Xác nhận huỷ yêu cầu; Thông tin trạng thái Đã huỷ | — | OQ-2, OQ-3, OQ-16, OQ-23 | SRS Web tr.308, 344, 377, 412, 444 — Huỷ đề xuất cấp mới (UC03.01.04, UC03.03.04, UC03.04.04, UC03.05.04, UC03.06.04) | ✅ |
| [uc-approve-reject-catalog-request](./uc-approve-reject-catalog-request.md) | Phê duyệt / Từ chối đề xuất cấp mới | Người dùng phần mềm xưởng (có quyền Phê duyệt/Từ chối) | FR-product-catalog-013..017, FR-product-catalog-020, FR-product-catalog-021 | Popup Xác nhận phê duyệt; popup Xác nhận từ chối; popup lỗi Tải lại trang; Thông tin trạng thái Đã từ chối / Đã phê duyệt | E-product-catalog-003..004 | OQ-3, OQ-5..8, OQ-14, OQ-19, OQ-23 | SRS Web tr.313, 349, 382, 417, 449 — Phê duyệt/Từ chối đề xuất cấp mới (UC03.01.05, UC03.03.05, UC03.04.05, UC03.05.05, UC03.06.05) | ✅ |

## Actors

| Actor |
|---|
| Người dùng phần mềm xưởng |
| Người dùng phần mềm xưởng (có quyền Phê duyệt/Từ chối) |

## Ghi chú

* Use case **tái lập chưa duyệt** từ SRS cũ — mỗi mệnh đề mang nhãn ✅/🔵/🟡. Chạy `/usecase product-catalog` (downstream) sau khi có SRS chính thức để điền truy vết đầy đủ.
* Nhóm mục con cùng khuôn (vd các danh mục) viết 1 use case cho cả khuôn; khác biệt từng mục con ở bảng "Khác biệt theo …" trong spec Mục 3.
