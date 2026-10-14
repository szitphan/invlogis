# UC-create-new-password — Tạo mật khẩu mới

## a. Introduction

Người dùng tạo mật khẩu mới khi đăng nhập lần đầu, sau khi IT reset thành mật khẩu mặc định, hoặc từ link/luồng reset bằng email. Mã UC gốc: Web UC01.05; Mobile UC01.01.05. ✅ [SRS Web tr.273 — UC01.05 Tạo mật khẩu mới; SRS Mobile tr.66 — UC01.01.05 Tạo mật khẩu mới]

## b. Actors & Objects

- Actor chính: Người dùng phần mềm Xưởng (Web); người dùng ứng dụng lái xe Delta (Mobile). ✅ [SRS Web tr.273 — UC01.05 Tạo mật khẩu mới; SRS Mobile tr.66 — UC01.01.05 Tạo mật khẩu mới]
- ERP Delta và PMX (theo lưu đồ "Update mật khẩu (ERP + PMX)"). ✅ [SRS Web tr.274 — hình lưu đồ UC01.05 Tạo mật khẩu mới]
- Đối tượng: Tài khoản người dùng (mật khẩu mặc định, mật khẩu mới).

## c. Pre-conditions

- TH1 và TH2: tài khoản đang dùng mật khẩu mặc định. TH3: email tài khoản nhận được link reset gửi từ luồng Quên mật khẩu - Reset bằng email. ✅ [SRS Web tr.273 — UC01.05 Tạo mật khẩu mới; SRS Mobile tr.66 — UC01.01.05 Tạo mật khẩu mới]

## d. Expected result

- Mật khẩu mới được cập nhật; hiển thị toast (Web) / popup message (Mobile) thành công; hiển thị màn Đăng nhập để đăng nhập bằng mật khẩu mới. ✅ [SRS Web tr.273 — UC01.05 Tạo mật khẩu mới; SRS Mobile tr.66 — UC01.01.05 Tạo mật khẩu mới] (nút "Đổi mật khẩu" nói tự đăng nhập vào trang chủ — Conflict, 🟡)

## e. Activity diagram

Xem flows.md — Flow: Tạo mật khẩu mới.

**Main Success Scenario**

1. Vào màn Tạo mật khẩu mới qua TH1 (đăng nhập lần đầu), TH2 (đăng nhập sau khi IT reset thành mật khẩu mặc định) hoặc TH3 (link reset trong email). ✅ [SRS Web tr.273 — UC01.05 Tạo mật khẩu mới; SRS Mobile tr.66 — UC01.01.05 Tạo mật khẩu mới]
2. Hệ thống hiện màn Tạo mật khẩu mới với khung Tài khoản (Web ảnh: khung hiện sẵn; Mobile ảnh: ô nhập "Tên tài khoản*" — OQ-24). ✅ [SRS Web tr.275 — UC01.05 Tạo mật khẩu mới; SRS Mobile tr.68 — UC01.01.05 Tạo mật khẩu mới]
3. Người dùng nhập Mật khẩu mới và Nhập lại mật khẩu mới (bắt buộc). ✅ [SRS Web tr.275 — UC01.05 Tạo mật khẩu mới; SRS Web tr.276 — UC01.05 Tạo mật khẩu mới]
4. Người dùng bấm "Xác nhận" (bảng còn nút "Đổi mật khẩu", ảnh Web chỉ có "Xác nhận"); hệ thống kiểm tra hợp lệ. ✅ [SRS Web tr.276 — UC01.05 Tạo mật khẩu mới; SRS Web tr.277 — UC01.05 Tạo mật khẩu mới]
5. Hợp lệ: cập nhật mật khẩu mới (ERP + PMX), toast "Đổi mật khẩu thành công", hiện màn Đăng nhập. ✅ [SRS Web tr.274 — hình lưu đồ UC01.05 Tạo mật khẩu mới; SRS Web tr.277 — UC01.05 Tạo mật khẩu mới]

**Extensions**

- 4a. Mật khẩu không đủ độ mạnh → E-account-access-015. ✅ [SRS Web tr.275 — UC01.05 Tạo mật khẩu mới; SRS Mobile tr.68 — UC01.01.05 Tạo mật khẩu mới]
- 4b. Mật khẩu trùng mật khẩu mặc định → "Mật khẩu trùng với mật khẩu mặc định" (E-account-access-018). ✅ [SRS Web tr.275 — UC01.05 Tạo mật khẩu mới; SRS Mobile tr.68 — UC01.01.05 Tạo mật khẩu mới]
- 4c. Nhập lại không khớp → "Mật khẩu xác nhận không khớp." (E-account-access-017). ✅ [SRS Web tr.276 — UC01.05 Tạo mật khẩu mới; SRS Mobile tr.69 — UC01.01.05 Tạo mật khẩu mới]
- 4d. Cập nhật thất bại → "Đã có lỗi xảy ra, vui lòng thử lại." (E-account-access-019). ✅ [SRS Web tr.276 — UC01.05 Tạo mật khẩu mới; SRS Mobile tr.69 — UC01.01.05 Tạo mật khẩu mới]
- 5a. Nút "Đổi mật khẩu": thành công thì tự đăng nhập vào trang chủ Delta (mô tả nút). 🟡 [SRS Web tr.276 — UC01.05 Tạo mật khẩu mới; SRS Mobile tr.69 — UC01.01.05 Tạo mật khẩu mới]

## f. Screens

Màn Tạo mật khẩu mới; Web — Đăng nhập; Mobile — Đăng nhập.

## g. Related FR

| Bước | FR | BR | Error | Nguồn |
|---|---|---|---|---|
| 1 | FR-account-access-011, FR-account-access-032 | BR-account-access-007, BR-account-access-021, BR-account-access-032 | — | SRS Web tr.273 — UC01.05 Tạo mật khẩu mới |
| 3 | FR-account-access-010, FR-account-access-032 | BR-account-access-030 | — | SRS Web tr.275 — UC01.05 Tạo mật khẩu mới |
| 4 | FR-account-access-032 | BR-account-access-026, BR-account-access-028, BR-account-access-029 | E-account-access-015, E-account-access-017, E-account-access-018, E-account-access-019 | SRS Web tr.275 — UC01.05 Tạo mật khẩu mới; SRS Web tr.276 — UC01.05 Tạo mật khẩu mới |
| 5 | FR-account-access-032 | BR-account-access-031 | — | SRS Web tr.277 — UC01.05 Tạo mật khẩu mới |

## h. Open Questions

OQ-2, OQ-4, OQ-13, OQ-19, OQ-24.
