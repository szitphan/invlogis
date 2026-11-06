# Use Case: Đổi mật khẩu

> Scope: account-access · Level: sea

## Primary Actor

Người dùng đã đăng nhập (nội bộ, đối tác)

## Trigger

Người dùng mở Thông tin cá nhân (hoặc Tài khoản trên app) và chọn Đổi mật khẩu.

## Preconditions

- Người dùng có phiên hợp lệ.

## Guarantees

- **Minimal Guarantee:** Mật khẩu cũ giữ nguyên khi có lỗi.
- **Success Guarantee:** Mật khẩu mới có hiệu lực; mọi phiên khác bị kết thúc; phiên hiện tại giữ nguyên.

## Main Success Scenario

1. Người dùng nhập mật khẩu cũ, mật khẩu mới, nhập lại, bấm Xác nhận.
2. Hệ thống kiểm tra theo BR-account-access-006.
3. Hệ thống lưu, kết thúc các phiên khác, báo toast "Đã đổi mật khẩu. Các thiết bị khác đã được đăng xuất.", đóng cửa sổ, ở lại màn Thông tin cá nhân.

## Extensions

**2a. Mật khẩu cũ sai:**
- 2a1. Hệ thống báo E-account-access-007; quay lại bước 1.

**2b. Mật khẩu mới không đúng chính sách / trùng mật khẩu đang dùng / nhập lại không khớp:**
- 2b1. Hệ thống báo E-account-access-008 / 009 / 010; quay lại bước 1.

**3a. Lỗi hệ thống hoặc mất mạng:**
- 3a1. Hệ thống báo E-common-008 / 009; mật khẩu cũ giữ nguyên.

## Related Requirements

FR-account-access-022, 023 · BR-account-access-006, 012
