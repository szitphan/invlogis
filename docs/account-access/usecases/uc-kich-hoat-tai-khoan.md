# Use Case: Kích hoạt tài khoản bằng mật khẩu tạm

> Scope: account-access · Level: sea

## Primary Actor

Người dùng có tài khoản mới hoặc vừa được đặt lại mật khẩu

## Trigger

Người dùng đăng nhập bằng mật khẩu tạm nhận qua email hoặc từ người đặt lại.

## Preconditions

- Tài khoản ở trạng thái Chờ kích hoạt với mật khẩu tạm còn hạn (FR-account-access-008, BR-account-access-005).

## Guarantees

- **Minimal Guarantee:** Mật khẩu tạm không mở được màn nào ngoài Tạo mật khẩu mới.
- **Success Guarantee:** Tài khoản sang Đang hoạt động với mật khẩu mới đúng chính sách; mật khẩu tạm hết hiệu lực.

## Main Success Scenario

1. Người dùng đăng nhập bằng tên tài khoản và mật khẩu tạm (uc-dang-nhap bước 2–3).
2. Hệ thống mở màn Tạo mật khẩu mới.
3. Người dùng nhập mật khẩu mới, nhập lại, bấm Xác nhận.
4. Hệ thống kiểm tra theo BR-account-access-006, lưu, chuyển tài khoản sang Đang hoạt động, mở khoá nếu đang Tạm khoá.
5. Hệ thống báo "Đã đặt mật khẩu mới. Đăng nhập lại bằng mật khẩu này." và về màn đăng nhập.

## Extensions

**1a. Mật khẩu tạm hết hạn:**
- 1a1. Hệ thống báo E-account-access-006. Use case kết thúc; người dùng dùng uc-tu-dat-lai-mat-khau hoặc uc-lien-he-it.

**1b. Đã có lần đặt lại mới hơn:**
- 1b1. Mật khẩu tạm cũ không còn hiệu lực, xử lý như sai mật khẩu (E-account-access-001).

**4a. Mật khẩu mới không đúng chính sách / trùng mật khẩu tạm / nhập lại không khớp:**
- 4a1. Hệ thống báo E-account-access-008 / 009 / 010 tại ô; quay lại bước 3.

**4b. Lỗi hệ thống:**
- 4b1. Hệ thống báo E-common-008, giữ màn; tài khoản vẫn Chờ kích hoạt.

## Related Requirements

FR-account-access-008, 009 · BR-account-access-005, 006, 011
