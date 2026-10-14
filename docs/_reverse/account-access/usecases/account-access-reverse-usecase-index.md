---
type: reverse-usecase-index
feature: account-access
status: draft
updated: 2026-10-15
links:
  - docs/_reverse/account-access/account-access-reverse-spec.md
---

# Đăng nhập và tài khoản cá nhân (`account-access`) — Use Case Index (reverse)

## Use cases

| Slug | Title | Primary Actor | Related FR | Screens | Errors | OQ | Nguồn | Nhãn |
|------|-------|---------------|-----------|---------|--------|-----|-------|------|
| [uc-login](./uc-login.md) | Đăng nhập (kèm chọn tổ chức/chi nhánh) | Người dùng chưa đăng nhập (mọi role) | FR-account-access-001..018 | Web — Đăng nhập; Web — Modal Chọn tổ chức; Web — Màn lỗi không có quyền; Mobile — Splash, Onboarding, Đăng nhập, Bottom Sheet Chọn tổ chức | E-account-access-001..009, E-account-access-020..022 | OQ-1, OQ-3, OQ-6..10, OQ-17, OQ-19, OQ-21, OQ-22 | SRS Web tr.248 — UC01.01 Đăng nhập; SRS Mobile tr.43 — UC01.01.01 Đăng nhập | ✅ |
| [uc-forgot-password](./uc-forgot-password.md) | Quên mật khẩu (Liên hệ IT / Reset bằng email) | Người dùng phần mềm Xưởng / ứng dụng Delta | FR-account-access-019..028 | Chọn cách lấy lại mật khẩu; Nhập tên tài khoản; Gửi tài khoản thành công; Kiểm tra hòm thư; Nhập OTP; Popup lỗi 1 lần/phút | E-account-access-010..013 | OQ-2, OQ-5, OQ-6, OQ-11..13 | SRS Web tr.258 — UC01.02 Quên mật khẩu; SRS Mobile tr.52 — UC01.01.02 Quên mật khẩu | ✅ (Web); 🔵 (Mobile) |
| [uc-logout](./uc-logout.md) | Đăng xuất | Người dùng đã đăng nhập (Web, Mobile nội bộ, Mobile cây dầu) | FR-account-access-029, FR-account-access-030 | Menu Avatar; Hộp xác nhận đăng xuất (cây dầu) | — | OQ-14 | SRS Web tr.267 — UC01.03 Đăng xuất; SRS Mobile tr.60 — UC01.01.03 Đăng xuất | ✅ |
| [uc-change-password](./uc-change-password.md) | Đổi mật khẩu | Người dùng đã đăng nhập | FR-account-access-031, FR-account-access-036 | Popup Đổi mật khẩu | E-account-access-014..017 | OQ-13, OQ-23 | SRS Web tr.269 — UC01.04 Đổi mật khẩu; SRS Mobile tr.62 — UC01.01.04 Đổi mật khẩu | ✅ |
| [uc-create-new-password](./uc-create-new-password.md) | Tạo mật khẩu mới | Người dùng (mật khẩu mặc định hoặc link/OTP reset) | FR-account-access-011, FR-account-access-032 | Màn Tạo mật khẩu mới | E-account-access-015, E-account-access-017..019 | OQ-2, OQ-4, OQ-13, OQ-19, OQ-24 | SRS Web tr.273 — UC01.05 Tạo mật khẩu mới; SRS Mobile tr.66 — UC01.01.05 Tạo mật khẩu mới | ✅ (phần chung); 🟡 (kết thúc) |
| [uc-view-profile](./uc-view-profile.md) | Xem thông tin cá nhân (nội bộ) | Người dùng đã đăng nhập | FR-account-access-033..036 | Web — Xem thông tin tài khoản; Mobile — Xem thông tin tài khoản nội bộ | — | OQ-15, OQ-20, OQ-23, OQ-25 | SRS Web tr.278 — UC01.06 Xem thông tin cá nhân; SRS Mobile tr.71 — UC01.01.06 Xem thông tin cá nhân - Tài khoản nội bộ | ✅ |
| [uc-view-oil-station-account](./uc-view-oil-station-account.md) | Xem thông tin tài khoản cây dầu (Mobile) | Nhân viên cây dầu mua ngoài | FR-account-access-030, FR-account-access-038..041 | Mobile — Tài khoản cây dầu; Hộp xác nhận đăng xuất | — | OQ-17, OQ-18 | SRS Mobile tr.75 — UC01.01.07 Xem thông tin tài khoản cây dầu | ✅ |
| [uc-change-language](./uc-change-language.md) | Thay đổi ngôn ngữ (Web) | Người dùng phần mềm xưởng | FR-account-access-037 | Menu Avatar; Web — Ngôn ngữ | — | OQ-16 | SRS Web tr.160 — UC02.03.01 Thay đổi ngôn ngữ | ✅ |

## Actors

| Actor |
|---|
| Người dùng (mật khẩu mặc định hoặc link/OTP reset) |
| Người dùng chưa đăng nhập (mọi role) |
| Người dùng phần mềm Xưởng / ứng dụng Delta |
| Người dùng phần mềm xưởng |
| Người dùng đã đăng nhập |
| Người dùng đã đăng nhập (Web, Mobile nội bộ, Mobile cây dầu) |
| Nhân viên cây dầu mua ngoài |

## Ghi chú

* Use case **tái lập chưa duyệt** từ SRS cũ — mỗi mệnh đề mang nhãn ✅/🔵/🟡. Chạy `/usecase account-access` (downstream) sau khi có SRS chính thức để điền truy vết đầy đủ.
* Nhóm mục con cùng khuôn (vd các danh mục) viết 1 use case cho cả khuôn; khác biệt từng mục con ở bảng "Khác biệt theo …" trong spec Mục 3.
