# Use Case: Liên hệ IT để đặt lại mật khẩu

> Scope: account-access · Level: sea

## Primary Actor

Người dùng không có email hoặc không nhận được email đặt lại

## Stakeholders & Interests

| Stakeholder | Interest |
|-------------|----------|
| Bộ phận hỗ trợ của khách | Nhận đủ thông tin để đặt lại đúng người; không bị gửi trùng liên tục |

## Trigger

Người dùng bấm Quên mật khẩu, chọn "Liên hệ IT".

## Preconditions

- Khách đã khai `P-email-ho-tro-mat-khau` (Delta: it@delta.com.vn).

## Guarantees

- **Minimal Guarantee:** Màn kết quả không cho biết tài khoản có tồn tại; số lần gửi bị giới hạn chung với đặt lại qua email.
- **Success Guarantee:** Bộ phận hỗ trợ nhận email gồm tên tài khoản, họ tên, chi nhánh, thời gian, kênh gửi.

## Main Success Scenario

1. Người dùng nhập tên tài khoản, bấm Xác nhận.
2. Hệ thống kiểm tra giới hạn gửi; tài khoản tồn tại thì gửi email tới `P-email-ho-tro-mat-khau`.
3. Hệ thống hiện màn "Đã gửi yêu cầu".
4. Bộ phận hỗ trợ đặt lại mật khẩu ở `access-control`; người dùng nhận mật khẩu tạm (qua email, hoặc người đặt lại gửi ngoài phần mềm) và tiếp tục ở uc-kich-hoat-tai-khoan.

## Extensions

**2a. Chưa đủ thời gian chờ hoặc vượt số lần mỗi giờ:**
- 2a1. Như uc-tu-dat-lai-mat-khau 2a, 2b (E-account-access-014).

**2b. Dịch vụ email lỗi:**
- 2b1. Hệ thống báo E-account-access-015, giữ màn nhập, không tự gửi lại; người dùng gửi lại theo giới hạn.

**2c. Tài khoản không tồn tại:**
- 2c1. Hệ thống không gửi gì, vẫn hiện màn ở bước 3.

## Related Requirements

FR-account-access-017, 020, 021 · BR-account-access-010, 021
