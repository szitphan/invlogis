# UC-change-password — Đổi mật khẩu

## a. Introduction

Người dùng đã đăng nhập đổi mật khẩu của chính mình từ màn Thông tin cá nhân. Mã UC gốc: Web UC01.04; Mobile UC01.01.04. ✅ [SRS Web tr.269 — UC01.04 Đổi mật khẩu; SRS Mobile tr.62 — UC01.01.04 Đổi mật khẩu]

## b. Actors & Objects

- Actor chính: Người dùng phần mềm Xưởng (Web); người dùng ứng dụng Lái xe Delta (Mobile). ✅ [SRS Web tr.269 — UC01.04 Đổi mật khẩu; SRS Mobile tr.62 — UC01.01.04 Đổi mật khẩu]
- Hệ thống ERP Delta (nhận mật khẩu mới; nguồn không nhắc PMX ở use case này). ✅ [SRS Web tr.272 — UC01.04 Đổi mật khẩu; SRS Web tr.269 — hình lưu đồ UC01.04 Đổi mật khẩu]
- Đối tượng: Tài khoản người dùng (mật khẩu).

## c. Pre-conditions

- Người dùng đã đăng nhập. Đường dẫn UC: Thông tin cá nhân > nút Đổi mật khẩu; bảng mô tả đặt trong "Hành động" (Web) / menu ☰ (Mobile) — lối vào lệch nhau (OQ-23). ✅ [SRS Web tr.269 — UC01.04 Đổi mật khẩu; SRS Web tr.281 — UC01.06 Xem thông tin cá nhân; SRS Mobile tr.62 — UC01.01.04 Đổi mật khẩu]

## d. Expected result

- Mật khẩu mới được cập nhật cho tài khoản, hiển thị toast (Web) / popup message (Mobile) thành công, hiển thị lại màn Thông tin tài khoản. ✅ [SRS Web tr.269 — UC01.04 Đổi mật khẩu; SRS Mobile tr.62 — UC01.01.04 Đổi mật khẩu]

## e. Activity diagram

Xem flows.md — Flow: Đổi mật khẩu.

**Main Success Scenario**

1. Người dùng ở màn Thông tin cá nhân bấm Đổi mật khẩu (nút trên màn hoặc trong "Hành động"); hệ thống hiện popup Đổi mật khẩu (lời dẫn trên ảnh Web "Vui lòng nhập các thông tin tài khoản của bạn bên dưới."; Mobile "Vui lòng nhập mật khẩu cũ của bạn"). ✅ [SRS Web tr.269 — hình lưu đồ UC01.04 Đổi mật khẩu; SRS Web tr.270 — UC01.04 Đổi mật khẩu; SRS Mobile tr.62 — hình lưu đồ UC01.01.04 Đổi mật khẩu; SRS Mobile tr.63 — UC01.01.04 Đổi mật khẩu]
2. Người dùng nhập Mật khẩu cũ,  Mật khẩu mới, Xác nhận mật khẩu mới (đều bắt buộc). ✅ [SRS Web tr.270 — UC01.04 Đổi mật khẩu; SRS Web tr.271 — UC01.04 Đổi mật khẩu; SRS Mobile tr.63 — UC01.01.04 Đổi mật khẩu; SRS Mobile tr.64 — UC01.01.04 Đổi mật khẩu]
3. Người dùng bấm "Xác nhận"; hệ thống kiểm tra hợp lệ cả 3 ô. ✅ [SRS Web tr.272 — UC01.04 Đổi mật khẩu; SRS Mobile tr.64 — UC01.01.04 Đổi mật khẩu]
4. Hợp lệ: hệ thống cập nhật mật khẩu mới (cả qua hệ thống ERP Delta), báo "Đổi mật khẩu thành công", tắt popup, quay lại Thông tin tài khoản. ✅ [SRS Web tr.272 — UC01.04 Đổi mật khẩu; SRS Mobile tr.65 — UC01.01.04 Đổi mật khẩu]

**Extensions**

- 3a. Mật khẩu cũ sai → "Mật khẩu cũ không chính xác." (E-account-access-014). ✅ [SRS Web tr.270 — UC01.04 Đổi mật khẩu; SRS Mobile tr.63 — UC01.01.04 Đổi mật khẩu]
- 3b. Mật khẩu mới không đủ 8 ký tự gồm chữ cái, số, chữ hoa, ký tự đặc biệt → E-account-access-015. ✅ [SRS Web tr.271 — UC01.04 Đổi mật khẩu; SRS Mobile tr.64 — UC01.01.04 Đổi mật khẩu]
- 3c. Mật khẩu mới trùng mật khẩu hiện tại → "Mật khẩu trùng với mật khẩu cũ" (E-account-access-016). ✅ [SRS Web tr.271 — UC01.04 Đổi mật khẩu; SRS Mobile tr.64 — UC01.01.04 Đổi mật khẩu]
- 3d. Xác nhận không khớp → "Mật khẩu xác nhận không khớp." (E-account-access-017). ✅ [SRS Web tr.271 — UC01.04 Đổi mật khẩu; SRS Mobile tr.64 — UC01.01.04 Đổi mật khẩu]

## f. Screens

Popup Đổi mật khẩu; Web — Xem thông tin tài khoản; Mobile — Xem thông tin tài khoản nội bộ.

## g. Related FR

| Bước | FR | BR | Error | Nguồn |
|---|---|---|---|---|
| 1 | FR-account-access-031, FR-account-access-036 | — | — | SRS Web tr.270 — UC01.04 Đổi mật khẩu; SRS Web tr.281 — UC01.06 Xem thông tin cá nhân |
| 2 | FR-account-access-010, FR-account-access-031 | BR-account-access-030 | — | SRS Web tr.271 — UC01.04 Đổi mật khẩu |
| 3 | FR-account-access-031 | BR-account-access-026, BR-account-access-027, BR-account-access-029 | E-account-access-014 đến E-account-access-017 | SRS Web tr.270 — UC01.04 Đổi mật khẩu; SRS Web tr.271 — UC01.04 Đổi mật khẩu |
| 4 | FR-account-access-031 | BR-account-access-031 | — | SRS Web tr.272 — UC01.04 Đổi mật khẩu |

## h. Open Questions

OQ-13, OQ-23.
