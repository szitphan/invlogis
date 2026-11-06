# Use Case: Xem thông tin cá nhân, lịch sử và đổi ngôn ngữ

> Scope: account-access · Level: sea

## Primary Actor

Người dùng đã đăng nhập (nội bộ, đối tác cây dầu)

## Trigger

Người dùng mở Thông tin tài khoản (web: menu ảnh đại diện · app: tab Tài khoản).

## Preconditions

- Người dùng có phiên hợp lệ.

## Guarantees

- **Minimal Guarantee:** Thông tin hồ sơ không bị sửa ở màn này.
- **Success Guarantee:** Người dùng thấy đúng hồ sơ của mình; ảnh đại diện, ngôn ngữ mới được lưu theo tài khoản.

## Main Success Scenario

1. Hệ thống hiện thông tin hồ sơ chỉ đọc lấy từ `employee-records` (trường trống theo GR-10).
2. Người dùng đổi ảnh đại diện: chọn ảnh JPG hoặc PNG; hệ thống lưu, báo "Đã cập nhật ảnh đại diện.".
3. Người dùng mở Lịch sử hoạt động: hệ thống hiện thao tác của chính người đó trong `P-so-ngay-lich-su-hoat-dong` (CMP-08).
4. Người dùng chọn ngôn ngữ: hệ thống lưu theo tài khoản, tải lại giao diện, báo "Đã đổi ngôn ngữ.".

## Extensions

**1a. Tài khoản đối tác cây dầu (app):**
- 1a1. Hệ thống hiện màn Tài khoản cây dầu theo FR-account-access-026 và BR-account-access-020 thay cho hồ sơ nhân viên.

**1b. Đang tải / tải lỗi:**
- 1b1. Hiện khung đang tải theo GR-12; lỗi thì E-common-008 kèm Thử lại.

**2a. Ảnh sai định dạng / quá 5 MB:**
- 2a1. Hệ thống báo E-common-006 / E-account-access-016, giữ ảnh cũ.

**3a. Chưa có thao tác nào:**
- 3a1. Trạng thái rỗng theo GR-12.

## Related Requirements

FR-account-access-026, 027, 028, 029 · BR-account-access-017, 018, 019, 020
