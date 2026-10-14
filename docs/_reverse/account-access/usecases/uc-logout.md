# UC-logout — Đăng xuất

## a. Introduction

Người dùng đăng xuất khỏi hệ thống từ menu Avatar. Mã UC gốc: Web UC01.03; Mobile UC01.01.03 (nội bộ); tài khoản cây dầu có nhánh xác nhận riêng ở UC01.01.07. ✅ [SRS Web tr.267 — UC01.03 Đăng xuất; SRS Mobile tr.60 — UC01.01.03 Đăng xuất; SRS Mobile tr.75 — UC01.01.07 Xem thông tin tài khoản cây dầu]

## b. Actors & Objects

- Actor chính: Người dùng phần mềm Xưởng (Web); người dùng ứng dụng Lái xe Delta (Mobile); nhân viên cây dầu (Mobile Partner Portal). ✅ [SRS Web tr.267 — UC01.03 Đăng xuất; SRS Mobile tr.60 — UC01.01.03 Đăng xuất; SRS Mobile tr.75 — UC01.01.07 Xem thông tin tài khoản cây dầu]
- Đối tượng: Phiên đăng nhập.

## c. Pre-conditions

- Người dùng đã đăng nhập. ✅ [SRS Web tr.267 — UC01.03 Đăng xuất; SRS Mobile tr.60 — UC01.01.03 Đăng xuất]

## d. Expected result

- Tài khoản đã đăng xuất, hiển thị màn Đăng nhập. ✅ [SRS Web tr.267 — UC01.03 Đăng xuất; SRS Mobile tr.60 — UC01.01.03 Đăng xuất]

## e. Activity diagram

Xem flows.md — Flow: Đăng xuất.

**Main Success Scenario**

1. Người dùng bấm icon Avatar (góc trên bên phải); hệ thống hiện dropdown Tài khoản. ✅ [SRS Web tr.267 — hình lưu đồ UC01.03 Đăng xuất; SRS Web tr.268 — UC01.03 Đăng xuất; SRS Mobile tr.61 — UC01.01.03 Đăng xuất]
2. Người dùng chọn "Đăng xuất". ✅ [SRS Web tr.268 — UC01.03 Đăng xuất]
3. Hệ thống đăng xuất và hiện màn Đăng nhập. ✅ [SRS Web tr.268 — UC01.03 Đăng xuất; SRS Mobile tr.61 — UC01.01.03 Đăng xuất]

**Extensions**

- 1a. Đường vào riêng của tài khoản cây dầu (Mobile): không qua dropdown Avatar; ở màn Tài khoản bấm nút "Đăng xuất" → hộp xác nhận "Bạn có chắc muốn đăng xuất?" với nút "Ở lại" và "Đăng xuất" (đỏ); "Đăng xuất" → đăng xuất, redirect màn đăng nhập. ✅ [SRS Mobile tr.75 — UC01.01.07 Xem thông tin tài khoản cây dầu; SRS Mobile tr.79 — UC01.01.07 Xem thông tin tài khoản cây dầu]
- 2b. Đăng xuất cũng được gọi từ menu ☰ ("Hành động") ở màn Thông tin cá nhân (Mobile nội bộ). ✅ (chữ trên ảnh) [SRS Mobile tr.72 — hình màn Thông tin tài khoản UC01.01.06 Xem thông tin cá nhân - Tài khoản nội bộ; SRS Mobile tr.74 — UC01.01.06 Xem thông tin cá nhân - Tài khoản nội bộ]

## f. Screens

Menu Avatar (Web); Mobile — Hộp xác nhận đăng xuất (cây dầu); Mobile — Tài khoản cây dầu.

## g. Related FR

| Bước | FR | BR | Error | Nguồn |
|---|---|---|---|---|
| 1–3 | FR-account-access-029 | — | — | SRS Web tr.267 — UC01.03 Đăng xuất; SRS Mobile tr.60 — UC01.01.03 Đăng xuất |
| 1a | FR-account-access-030 | BR-account-access-038 | — | SRS Mobile tr.79 — UC01.01.07 Xem thông tin tài khoản cây dầu |

## h. Open Questions

OQ-14.
