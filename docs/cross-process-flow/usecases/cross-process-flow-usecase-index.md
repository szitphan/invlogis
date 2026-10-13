---
type: usecase-index
feature: cross-process-flow
status: draft
updated: 2026-10-12
links:
  - docs/cross-process-flow/srs/cross-process-flow-spec.md
  - docs/cross-process-flow/cross-process-flow-object-map.md
---

# Liên quy trình — Use Cases Index

## Use cases

| # | Slug | Level | Status | Actor primary | Covers FR | Screens | Errors (E-*) | OQ ref | Priority | Updated |
|---|------|-------|--------|---------------|-----------|---------|--------------|--------|----------|---------|
| 1 | [uc-xem-quy-trinh-cua-ban-ghi](uc-xem-quy-trinh-cua-ban-ghi.md) | sea | draft | Người theo dõi quy trình · Lái xe | FR-cross-process-flow-005, -006, -007, -008, -009, -010, -011, -020, -021 | xem-quy-trinh [1]–[10] · xem-quy-trinh-mobile [19]–[29] · panel [6]–[9] cũng mở từ [15] | E-cross-process-flow-004, E-common-008, E-common-009, E-common-011 | — | P0 | 2026-10-12 |
| 2 | [uc-tao-nghiep-vu-tiep-theo](uc-tao-nghiep-vu-tiep-theo.md) | sea | draft | Người tạo bản ghi | FR-cross-process-flow-003, -012, -013 | [1] ban-ghi-dong-quy-trinh · tao-nghiep-vu-tiep-theo [16]–[17] | E-cross-process-flow-001, E-cross-process-flow-003, E-common-008, E-common-009 | — | P0 | 2026-10-12 |
| 3 | [uc-tra-cuu-quy-trinh](uc-tra-cuu-quy-trinh.md) | sea | draft | Người theo dõi quy trình | FR-cross-process-flow-015, -016, -017, -018, -019, -020, -022 | tra-cuu-quy-trinh [11]–[15] · panel [6]–[9] | E-common-008, E-common-011 | — | P0 | 2026-10-12 |
| 4 | [uc-cap-nhat-quy-trinh-theo-ban-ghi](uc-cap-nhat-quy-trinh-theo-ban-ghi.md) | sea | draft | Hệ thống | FR-cross-process-flow-001, -002, -003, -004, -014, -020 | [18] popup-da-co-buoc-con | E-cross-process-flow-001, E-cross-process-flow-002, E-cross-process-flow-003 | spec.md#OQ-1 | P0 | 2026-10-12 |

Không thành use case riêng: "Xem dòng quy trình" (bước 1–2 của uc-xem-quy-trinh-cua-ban-ghi) · "Cấp quyền menu Quy trình" (FR-cross-process-flow-019 — một bước trong luồng phân quyền chung của Admin, tiền điều kiện của uc-tra-cuu-quy-trinh).

## CRUD matrix

| UC \ Entity | QuyTrinh | BuocQuyTrinh | LienKetBuoc | BanGhiNghiepVu | BangCongNo |
|---|---|---|---|---|---|
| [uc-xem-quy-trinh-cua-ban-ghi](uc-xem-quy-trinh-cua-ban-ghi.md) | R | R | R | R | R |
| [uc-tao-nghiep-vu-tiep-theo](uc-tao-nghiep-vu-tiep-theo.md) | R | C | C | CR | — |
| [uc-tra-cuu-quy-trinh](uc-tra-cuu-quy-trinh.md) | R | R | R | R | — |
| [uc-cap-nhat-quy-trinh-theo-ban-ghi](uc-cap-nhat-quy-trinh-theo-ban-ghi.md) | CU | CU | C | R | R |

## Actors

| Actor | Loại | Mô tả | Nguồn |
|---|---|---|---|
| Người theo dõi quy trình | primary | Nhân viên nội bộ Delta xem quy trình (Kế toán thanh toán, Quản lý xưởng, Thủ kho, Người duyệt, Điều phối) | object map › Vai trò nghiệp vụ |
| Người tạo bản ghi | primary | Nhân viên nội bộ Delta tạo nghiệp vụ tiếp theo | object map › Vai trò nghiệp vụ |
| Lái xe | primary | Xem tiến độ trên Delta Super App, quyền theo FR-cross-process-flow-009 | brainstorm Mục 6.2 |
| Admin | secondary | Cấp quyền menu Quy trình theo module | object map › Vai trò nghiệp vụ |
| Hệ thống | system | Tạo quy trình, sinh mã, thêm bước, tính trạng thái | object map › Vai trò nghiệp vụ |

## Nguồn dữ liệu

- FR + Error Matrix: [[docs/cross-process-flow/srs/cross-process-flow-spec.md|SRS spec]]
- Open Questions: `srs/cross-process-flow-spec.md` Mục 12 (canonical)
