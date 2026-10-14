# UC-forgot-password — Quên mật khẩu

## a. Introduction

Người dùng quên mật khẩu chọn lấy lại qua IT hoặc tự reset bằng email. Mã UC gốc: Web UC01.02; Mobile UC01.01.02. ✅ [SRS Web tr.258 — UC01.02 Quên mật khẩu; SRS Mobile tr.52 — UC01.01.02 Quên mật khẩu]

## b. Actors & Objects

- Actor chính: Người dùng phần mềm Xưởng (Web); người dùng ứng dụng lái xe Delta (Mobile). ✅ [SRS Web tr.258 — UC01.02 Quên mật khẩu; SRS Mobile tr.52 — UC01.01.02 Quên mật khẩu]
- Bộ phận IT phần mềm ERP Delta; ERP và PMX; hệ thống gửi email. ✅ [SRS Web tr.260 — UC01.02 Quên mật khẩu; SRS Web tr.263 — UC01.02 Quên mật khẩu]
- Đối tượng: Tài khoản người dùng, Yêu cầu hỗ trợ đặt lại mật khẩu, Mã OTP (Mobile), Link reset (Web). ✅ [SRS Web tr.263 — UC01.02 Quên mật khẩu; SRS Mobile tr.57 — UC01.01.02 Quên mật khẩu]

## c. Pre-conditions

- Người dùng đã được cấp tài khoản; trạng thái tài khoản "Đang hoạt động"; tài khoản có quyền truy cập phần mềm Xưởng (Web) / ứng dụng lái xe Delta (Mobile). ✅ [SRS Web tr.258 — UC01.02 Quên mật khẩu; SRS Mobile tr.52 — UC01.01.02 Quên mật khẩu]

## d. Expected result

- Chọn Liên hệ IT: thông báo reset mật khẩu được gửi tới bộ phận IT phần mềm ERP Delta, hiển thị màn "Gửi tài khoản thành công". ✅ [SRS Web tr.258 — UC01.02 Quên mật khẩu; SRS Mobile tr.52 — UC01.01.02 Quên mật khẩu]
- Chọn Reset bằng email: Web gửi email kèm link tạo mật khẩu mới và hiện màn "Kiểm tra hòm thư"; Mobile gửi OTP qua email công ty và hiện màn Nhập OTP (điều kiện sau ghi "Kiểm tra hòm thư" — Conflict). ✅ (Web); 🟡 (Mobile) [SRS Web tr.258 — UC01.02 Quên mật khẩu; SRS Mobile tr.52 — UC01.01.02 Quên mật khẩu; SRS Mobile tr.57 — UC01.01.02 Quên mật khẩu]

## e. Activity diagram

Xem flows.md — Flow: Quên mật khẩu — Liên hệ IT; Flow: Quên mật khẩu — Reset bằng email (Web, gửi link); Flow: Quên mật khẩu — Reset bằng email (Mobile, mã OTP).

**Main Success Scenario**

1. Người dùng bấm "Quên mật khẩu" ở màn Đăng nhập; hệ thống hiện lựa chọn cách lấy lại mật khẩu. ✅ [SRS Web tr.259 — hình lưu đồ UC01.02 Quên mật khẩu; SRS Web tr.260 — UC01.02 Quên mật khẩu; SRS Mobile tr.53 — UC01.01.02 Quên mật khẩu]
2. Người dùng chọn "Liên hệ IT" hoặc "Reset mật khẩu"; hệ thống mở màn Nhập tên tài khoản tương ứng. ✅ [SRS Web tr.260 — UC01.02 Quên mật khẩu; SRS Mobile tr.53 — UC01.01.02 Quên mật khẩu]
3. Người dùng nhập tên tài khoản; hệ thống kiểm tra (Web sau 1 giây dừng gõ, Mobile sau "Kết thúc nhập") và hiện Họ tên + Tên tài khoản. ✅ [SRS Web tr.262 — UC01.02 Quên mật khẩu; SRS Mobile tr.54 — UC01.01.02 Quên mật khẩu]
4. Người dùng bấm "Xác nhận". ✅ [SRS Web tr.263 — UC01.02 Quên mật khẩu; SRS Mobile tr.55 — UC01.01.02 Quên mật khẩu]
5a. Liên hệ IT: hệ thống gửi email tự động tới IT Delta và hiện màn "Gửi tài khoản thành công"; người dùng bấm "Quay về đăng nhập" (Web) / "Quay lại" (Mobile). ✅ [SRS Web tr.263 — UC01.02 Quên mật khẩu; SRS Web tr.265 — UC01.02 Quên mật khẩu; SRS Mobile tr.57 — UC01.01.02 Quên mật khẩu]
5b. Reset bằng email (Web): hệ thống gửi email có link, hiện "Kiểm tra hòm thư", người dùng bấm link để sang Tạo mật khẩu mới (bước bấm link 🔵). ✅ [SRS Web tr.263 — UC01.02 Quên mật khẩu; SRS Web tr.264 — UC01.02 Quên mật khẩu]
5c. Reset bằng email (Mobile): hệ thống gửi OTP, hiện màn Nhập OTP; nhập đủ 6 số, đúng → Tạo mật khẩu mới. ✅ [SRS Mobile tr.56 — UC01.01.02 Quên mật khẩu; SRS Mobile tr.58 — UC01.01.02 Quên mật khẩu]
6. IT reset mật khẩu; ERP gọi API cho PMX cập nhật; trạng thái tài khoản chuyển sang "Cấp mới" (nhánh Liên hệ IT). ✅ [SRS Web tr.260 — UC01.02 Quên mật khẩu; SRS Mobile tr.53 — UC01.01.02 Quên mật khẩu]

**Extensions**

- 3a. Tên tài khoản sai → "Tên tài khoản không chính xác." (E-account-access-010). ✅ [SRS Web tr.262 — UC01.02 Quên mật khẩu; SRS Mobile tr.55 — UC01.01.02 Quên mật khẩu]
- 3b. Tài khoản không ở trạng thái Đang hoạt động → không được đổi mật khẩu; nguồn không có câu lỗi cho trường hợp này (`<!-- TBD -->`). ✅ (quy tắc) / 🟡 (câu lỗi) [SRS Web tr.262 — UC01.02 Quên mật khẩu]
- 4a. Gửi lần 2 trong vòng 1 phút → popup "Bạn chỉ có thể gửi yêu cầu quên mật khẩu tối đa 1 lần mỗi phút. Xin vui lòng thử lại sau." (E-account-access-011), nút "Trở về". ✅ [SRS Web tr.263 — UC01.02 Quên mật khẩu; SRS Mobile tr.55 — UC01.01.02 Quên mật khẩu]
- 5c-1. OTP sai hoặc hết hạn → "OTP không hợp lệ hoặc hết hạn. Vui lòng thử lại." (E-account-access-013). ✅ [SRS Mobile tr.58 — UC01.01.02 Quên mật khẩu]
- 5c-2. Sai 5 lần → "Bạn đã nhập sai mã OTP 5 lần. Vui lòng gửi lại mã OTP mới." (E-account-access-012). ✅ [SRS Mobile tr.58 — UC01.01.02 Quên mật khẩu]
- 5c-3. Bấm "Gửi lại mã [x]" khi đã bật (sau 5 phút): gửi OTP mới, email reply email OTP cũ. ✅ [SRS Mobile tr.58 — UC01.01.02 Quên mật khẩu; SRS Mobile tr.59 — UC01.01.02 Quên mật khẩu]
- 5c-4. Bấm "Back" → về màn Đăng nhập. ✅ [SRS Mobile tr.59 — UC01.01.02 Quên mật khẩu]

## f. Screens

Popup / màn Chọn cách lấy lại mật khẩu; Màn Nhập tên tài khoản (Liên hệ IT / Reset bằng email); Popup lỗi giới hạn 1 lần/phút; Màn Gửi tài khoản thành công; Màn Kiểm tra hòm thư (Web); Màn Nhập OTP (Mobile).

## g. Related FR

| Bước | FR | BR | Error | Nguồn |
|---|---|---|---|---|
| 1–2 | FR-account-access-019 | — | — | SRS Web tr.260 — UC01.02 Quên mật khẩu; SRS Mobile tr.53 — UC01.01.02 Quên mật khẩu |
| 3 | FR-account-access-020 | BR-account-access-017, BR-account-access-018, BR-account-access-041 | E-account-access-010 | SRS Web tr.262 — UC01.02 Quên mật khẩu; SRS Mobile tr.54 — UC01.01.02 Quên mật khẩu |
| 4 | FR-account-access-025 | BR-account-access-019 | E-account-access-011 | SRS Web tr.263 — UC01.02 Quên mật khẩu |
| 5a | FR-account-access-021, FR-account-access-028 | BR-account-access-020, BR-account-access-039 | — | SRS Web tr.263 — UC01.02 Quên mật khẩu |
| 5b | FR-account-access-023, FR-account-access-028 | BR-account-access-022, BR-account-access-039 | — | SRS Web tr.264 — UC01.02 Quên mật khẩu |
| 5c | FR-account-access-024, FR-account-access-026, FR-account-access-027 | BR-account-access-023, BR-account-access-024, BR-account-access-025 | E-account-access-012, E-account-access-013 | SRS Mobile tr.58 — UC01.01.02 Quên mật khẩu |
| 6 | FR-account-access-022 | BR-account-access-021 | — | SRS Web tr.260 — UC01.02 Quên mật khẩu |

## h. Open Questions

OQ-2, OQ-5, OQ-6, OQ-11, OQ-12, OQ-13.
