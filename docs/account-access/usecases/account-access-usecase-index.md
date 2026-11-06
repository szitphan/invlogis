---
type: usecase-index
feature: account-access
status: in-review
status_changed: 2026-11-06
status_reason: "đã review upstream, không cần sửa"
updated: 2026-10-15
links:
  - docs/account-access/srs/account-access-spec.md
  - docs/account-access/brainstorms/account-access.md
---

# Đăng nhập và tài khoản cá nhân — Use Cases Index

## Use cases

| # | Slug | Level | Status | Actor primary | Covers FR | Screens | Errors (E-*) | OQ ref | Priority | Updated |
|---|------|-------|--------|---------------|-----------|---------|--------------|--------|----------|---------|
| 1 | [uc-dang-nhap](uc-dang-nhap.md) | sea | draft | Người dùng nội bộ · Đối tác cây dầu | FR-account-access-001, -002, -003, -004, -005, -006, -007, -010, -011, -013, -014, -015, -025, -030, -031, -033 | sign-in [1.1]–[1.5] | E-account-access-001, -002, -003, -004, -005, -006, -017, E-common-001, E-common-008, E-common-009 | — | P0 | 2026-10-15 |
| 2 | [uc-kich-hoat-tai-khoan](uc-kich-hoat-tai-khoan.md) | sea | draft | Người dùng có mật khẩu tạm | FR-account-access-008, -009 | [1.3] → create-password [2.1] | E-account-access-001, -006, -008, -009, -010, E-common-008 | — | P0 | 2026-10-15 |
| 3 | [uc-tu-dat-lai-mat-khau](uc-tu-dat-lai-mat-khau.md) | sea | draft | Người dùng có email | FR-account-access-006, -009, -017, -018, -019, -020, -023, -032 | reset-password [3.1]–[3.5], [2.1] | E-account-access-008, -009, -010, -011, -012, -013, -014, -018 | — | P0 | 2026-10-15 |
| 4 | [uc-lien-he-it](uc-lien-he-it.md) | sea | draft | Người dùng không có email | FR-account-access-017, -020, -021 | contact-it [3.1], [4.1]–[4.2] | E-account-access-014, -015 | — | P0 | 2026-10-15 |
| 5 | [uc-doi-mat-khau](uc-doi-mat-khau.md) | sea | draft | Người dùng đã đăng nhập | FR-account-access-022, -023 | change-password [6.1], [5.1] | E-account-access-007, -008, -009, -010, E-common-008, E-common-009 | — | P0 | 2026-10-15 |
| 6 | [uc-doi-chi-nhanh](uc-doi-chi-nhanh.md) | sea | draft | Người dùng nội bộ ≥2 chi nhánh | FR-account-access-012 | switch-branch [1.5] | E-common-012 | — | P1 | 2026-10-15 |
| 7 | [uc-dang-xuat](uc-dang-xuat.md) | sea | draft | Người dùng đã đăng nhập | FR-account-access-024 | sign-out [8.1] | — | — | P0 | 2026-10-15 |
| 8 | [uc-xem-thong-tin-ca-nhan](uc-xem-thong-tin-ca-nhan.md) | sea | draft | Người dùng đã đăng nhập | FR-account-access-026, -027, -028, -029 | account-profile [5.1]–[5.3] | E-account-access-016, E-common-006, E-common-008 | — | P1 | 2026-10-15 |

Không thành use case riêng: FR-account-access-016 (kết thúc phiên khi tài khoản bị vô hiệu hoá, đặt lại mật khẩu hoặc đổi quyền) là quy tắc hệ thống áp lên mọi use case khi có phiên, kích hoạt từ thao tác ở `access-control`.

## CRUD matrix

| UC \ Entity | TaiKhoan | MatKhauTam | Phien | YeuCauDatLai | ChiNhanhGanNhat | LichSuHoatDong |
|---|---|---|---|---|---|---|
| [uc-dang-nhap](uc-dang-nhap.md) | RU | R | C | — | RU | C |
| [uc-kich-hoat-tai-khoan](uc-kich-hoat-tai-khoan.md) | RU | RU | — | — | — | C |
| [uc-tu-dat-lai-mat-khau](uc-tu-dat-lai-mat-khau.md) | RU | — | U | CRU | — | C |
| [uc-lien-he-it](uc-lien-he-it.md) | R | — | — | C | — | — |
| [uc-doi-mat-khau](uc-doi-mat-khau.md) | RU | — | U | — | — | C |
| [uc-doi-chi-nhanh](uc-doi-chi-nhanh.md) | R | — | U | — | CU | — |
| [uc-dang-xuat](uc-dang-xuat.md) | — | — | U | — | — | C |
| [uc-xem-thong-tin-ca-nhan](uc-xem-thong-tin-ca-nhan.md) | RU | — | — | — | — | R |
