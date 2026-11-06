# Use Case: Tự đặt lại mật khẩu qua email

> Scope: account-access · Level: sea

## Primary Actor

Người dùng có email đăng ký (web: link · app: mã OTP)

## Stakeholders & Interests

| Stakeholder | Interest |
|-------------|----------|
| Khách (doanh nghiệp) | Người ngoài không dò được tài khoản, không chiếm được tài khoản qua email |

## Trigger

Người dùng bấm Quên mật khẩu ở màn đăng nhập, chọn "Đặt lại qua email".

## Preconditions

- Không có.

## Guarantees

- **Minimal Guarantee:** Màn kết quả giống nhau dù tài khoản có tồn tại, có email hay không; số lần gửi bị giới hạn theo BR-account-access-010.
- **Success Guarantee:** Tài khoản có mật khẩu mới, Đang hoạt động (mở khoá nếu đang Tạm khoá); mọi phiên khác bị kết thúc.

## Main Success Scenario

1. Người dùng nhập tên tài khoản, bấm Xác nhận.
2. Hệ thống kiểm tra giới hạn gửi; tài khoản đủ điều kiện theo BR-account-access-007 thì gửi email (web: link hạn `P-han-link-dat-lai`; app: mã OTP 6 số hạn `P-han-ma-otp`) và làm link, mã cũ hết hiệu lực.
3. Hệ thống hiện màn "Kiểm tra email" (web) hoặc "Nhập mã xác thực" (app).
4. Web: người dùng mở link. App: người dùng nhập đủ 6 số, hệ thống tự kiểm tra.
5. Hệ thống mở màn Tạo mật khẩu mới (có `P-han-tao-mat-khau` để lưu); người dùng nhập mật khẩu mới, nhập lại, bấm Xác nhận.
6. Hệ thống kiểm tra theo BR-account-access-006, lưu, đánh dấu link hoặc mã đã dùng, mở khoá nếu cần, kết thúc phiên khác, huỷ link/mã/mật khẩu tạm khác, báo thành công, về màn đăng nhập.

## Extensions

**2a. Chưa đủ `P-cho-gui-lai-ma` từ lần gửi trước:**
- 2a1. Nút Gửi lại hiện đếm ngược, chưa gửi.

**2b. Vượt `P-so-lan-gui-ma-moi-gio` lần trong giờ:**
- 2b1. Hệ thống báo E-account-access-014. Use case kết thúc.

**2c. Tài khoản không tồn tại, Vô hiệu hoá hoặc không có email:**
- 2c1. Hệ thống không gửi gì, vẫn hiện màn ở bước 3. Người dùng không nhận được email thì dùng uc-lien-he-it.

**4a. App: mã sai, còn lượt:**
- 4a1. Hệ thống báo E-account-access-011, xoá mã đã nhập; quay lại bước 4.

**4b. App: mã sai đủ `P-so-lan-sai-otp` lần hoặc hết hạn:**
- 4b1. Hệ thống báo E-account-access-012, khoá ô nhập; người dùng gửi mã mới (quay lại bước 2).

**4c. Web: link hết hạn hoặc đã dùng:**
- 4c1. Hệ thống báo E-account-access-013, có nút Gửi lại link.

**6b. Quá `P-han-tao-mat-khau`:**
- 6b1. Hệ thống báo E-account-access-018; người dùng gửi lại yêu cầu (quay lại bước 1).

**6a. Mật khẩu mới không hợp lệ:**
- 6a1. Hệ thống báo E-account-access-008 / 009 / 010; quay lại bước 5.

## Related Requirements

FR-account-access-006, 009, 017, 018, 019, 020, 023 · BR-account-access-006, 007, 008, 009, 010, 011, 012
