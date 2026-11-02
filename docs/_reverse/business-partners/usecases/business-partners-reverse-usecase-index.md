---
type: reverse-usecase-index
feature: business-partners
status: draft
updated: 2026-10-20
links:
  - docs/_reverse/business-partners/business-partners-reverse-spec.md
---

# Đối tác: nhà cung cấp, khách hàng, xe của khách (`business-partners`) — Use Case Index (reverse)

## Use cases

| Slug | Title | Primary Actor | Related FR | Screens | Errors | OQ | Nguồn | Nhãn |
|------|-------|---------------|-----------|---------|--------|-----|-------|------|
| [uc-view-partner-list](./uc-view-partner-list.md) | Xem danh mục nhà cung cấp HHDV / khách hàng DK05 / xe của khách hàng | Người dùng phần mềm xưởng | FR-business-partners-001..011 | Danh sách NCC; Danh sách KH DK05; Danh sách xe khách hàng | — | OQ-10, OQ-12 | SRS Web tr.461 — UC03.07.01; SRS Web tr.505 — UC03.08.01; SRS Web tr.545 — UC03.09.01 | ✅ |
| [uc-view-partner-detail](./uc-view-partner-detail.md) | Xem thông tin nhà cung cấp HHDV / khách hàng DK05 / xe của khách hàng | Người dùng phần mềm xưởng | FR-business-partners-012..018, FR-business-partners-041, FR-business-partners-045 | Thông tin NCC; Thông tin KH DK05; Thông tin xe khách hàng | — | OQ-9, OQ-13 | SRS Web tr.467 — UC03.07.02; SRS Web tr.510 — UC03.08.02; SRS Web tr.549 — UC03.09.02 | ✅ |
| [uc-create-partner-request](./uc-create-partner-request.md) | Tạo đề xuất tạo mới nhà cung cấp HHDV / khách hàng DK05 / xe của khách hàng | Người dùng phần mềm xưởng | FR-business-partners-019..022, FR-business-partners-032, FR-business-partners-037, FR-business-partners-041..044 | Tạo mới NCC; Tạo mới KH DK05; Tạo mới xe khách hàng; popup Huỷ tạo mới | E-business-partners-001..007, E-business-partners-010 | OQ-4, OQ-5, OQ-6, OQ-9, OQ-13 | SRS Web tr.474 — UC03.07.03; SRS Web tr.517 — UC03.08.03; SRS Web tr.554 — UC03.09.03 | ✅ |
| [uc-cancel-partner-request](./uc-cancel-partner-request.md) | Huỷ đề xuất cấp mới nhà cung cấp HHDV / khách hàng DK05 / xe của khách hàng | Người dùng phần mềm xưởng | FR-business-partners-023..025, FR-business-partners-033 | Thông tin (Chờ phê duyệt, Đã huỷ); popup Xác nhận huỷ | E-business-partners-008, E-business-partners-009 | OQ-11, OQ-15 | SRS Web tr.488 — UC03.07.04; SRS Web tr.528 — UC03.08.04; SRS Web tr.565 — UC03.09.04 | ✅ |
| [uc-approve-reject-partner-request](./uc-approve-reject-partner-request.md) | Phê duyệt / Từ chối đề xuất cấp mới nhà cung cấp HHDV / khách hàng DK05 / xe của khách hàng | Người dùng phần mềm xưởng (có quyền phê duyệt/từ chối) | FR-business-partners-026..029, FR-business-partners-034..036, FR-business-partners-038, FR-business-partners-039 | Thông tin (Chờ phê duyệt, Đã từ chối, Đã phê duyệt); popup phê duyệt/từ chối/lỗi | E-business-partners-008, E-business-partners-009 | OQ-7, OQ-8, OQ-11, OQ-14, OQ-15 | SRS Web tr.493 — UC03.07.05; SRS Web tr.533 — UC03.08.05; SRS Web tr.570 — UC03.09.05 | ✅ |
| [uc-delete-or-recreate-closed-request](./uc-delete-or-recreate-closed-request.md) | Xoá yêu cầu / Tạo mới yêu cầu từ yêu cầu đã huỷ hoặc đã từ chối | Người dùng phần mềm xưởng | FR-business-partners-015, FR-business-partners-030, FR-business-partners-031 | Thông tin (Đã huỷ, Đã từ chối); popup Xác nhận xoá | — | OQ-3, OQ-4 | SRS Web tr.472 — UC03.07.02; SRS Web tr.492 — UC03.07.04; SRS Web tr.497 — UC03.07.05 | 🔵 |

## Actors

| Actor |
|---|
| Người dùng phần mềm xưởng |
| Người dùng phần mềm xưởng (có quyền phê duyệt/từ chối) |

## Ghi chú

* Use case **tái lập chưa duyệt** từ SRS cũ — mỗi mệnh đề mang nhãn ✅/🔵/🟡. Chạy `/usecase business-partners` (downstream) sau khi có SRS chính thức để điền truy vết đầy đủ.
* Nhóm mục con cùng khuôn (vd các danh mục) viết 1 use case cho cả khuôn; khác biệt từng mục con ở bảng "Khác biệt theo …" trong spec Mục 3.
