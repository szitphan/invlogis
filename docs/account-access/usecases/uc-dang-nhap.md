# Use Case: Đăng nhập và chọn chi nhánh

> Scope: account-access · Level: sea

## Primary Actor

Người dùng nội bộ (web, app) · Nhân viên đối tác cây dầu (app)

## Trigger

Người dùng mở đường dẫn đăng nhập của khách trên web, hoặc mở app.

## Preconditions

- Tài khoản đã được tạo ở `access-control`.
- Người dùng dùng đúng đường dẫn đăng nhập của khách (FR-account-access-002).

## Guarantees

- **Minimal Guarantee:** Không ai vào được khi thông tin sai; mỗi lần sai được đếm theo BR-account-access-003; không câu báo nào cho biết tài khoản có tồn tại hay không.
- **Success Guarantee:** Người dùng ở Home của đúng chi nhánh (hoặc công ty mẹ, hoặc Home đối tác); phiên được giữ theo FR-account-access-013, 014; chi nhánh được nhớ cho lần sau.

## Main Success Scenario

1. Hệ thống kiểm tra phiên trên thiết bị; chưa có phiên thì hiện màn đăng nhập (app: Splash, lần đầu cài thì Onboarding).
2. Người dùng nhập tên tài khoản (hoặc email), mật khẩu; trên web có thể chọn Ghi nhớ đăng nhập; bấm Đăng nhập.
3. Hệ thống kiểm tra ô trống, khoá nút trong lúc gửi, rồi kiểm tra theo thứ tự BR-account-access-022 (khách → tạm khoá → mật khẩu → trạng thái, chi nhánh, quyền kênh).
4. Thông tin hợp lệ, tài khoản Đang hoạt động: hệ thống đưa bộ đếm sai về 0.
5. Tài khoản nội bộ có từ 2 chi nhánh, chưa có chi nhánh lần trước: hệ thống mở cửa sổ chọn chi nhánh.
6. Người dùng tìm và chọn công ty mẹ hoặc một chi nhánh, bấm Chọn.
7. Hệ thống lưu chi nhánh dùng lần trước, mở Home của chi nhánh đã chọn.

## Extensions

**1a. Đã có phiên hợp lệ:**
- 1a1. Hệ thống bỏ qua màn đăng nhập, đi tiếp bước 5 theo FR-account-access-010.

**3a. Còn ô trống:**
- 3a1. Hệ thống báo E-common-001 tại ô, không gửi.

**3b. Sai tên tài khoản hoặc mật khẩu, còn lượt:**
- 3b1. Hệ thống tăng bộ đếm, báo E-account-access-001 kèm số lần thử còn lại, xoá mật khẩu đã nhập; quay lại bước 2.

**3c. Sai đủ `P-so-lan-sai-mat-khau` lần, hoặc tài khoản đang Tạm khoá:**
- 3c1. Hệ thống chuyển tài khoản sang Tạm khoá (nếu chưa), báo E-account-access-002 kèm giờ mở khoá. Use case kết thúc.

**3d. Mật khẩu đúng nhưng tài khoản Vô hiệu hoá / chưa có chi nhánh / không có quyền dùng kênh này:**
- 3d1. Hệ thống báo E-account-access-003 / 004 / 005. Use case kết thúc.

**3e. Đăng nhập bằng mật khẩu tạm:**
- 3e1. Còn hạn → chuyển sang uc-kich-hoat-tai-khoan. Hết hạn → báo E-account-access-006. Use case kết thúc.

**3f. Lỗi hệ thống hoặc mất mạng:**
- 3f1. Hệ thống báo E-common-008 hoặc E-common-009, giữ nguyên dữ liệu đã nhập.

**1b. App mở lần đầu hoặc vừa chọn Đổi doanh nghiệp:**
- 1b1. Người dùng nhập mã doanh nghiệp; sai thì E-account-access-017 (FR-account-access-002).

**1c. App có phiên nhưng mất mạng:**
- 1c1. Vào Home ở chế độ mất mạng (GR-25).

**5a. Tài khoản đối tác:**
- 5a1. Hệ thống mở Home đối tác, không qua chọn chi nhánh. Use case kết thúc.

**5b. Tài khoản nội bộ chỉ có 1 chi nhánh, hoặc chi nhánh lần trước còn quyền:**
- 5b1. Hệ thống mở thẳng Home của chi nhánh đó. Use case kết thúc.

**6a. Tìm không ra chi nhánh:**
- 6a1. Hệ thống hiện trạng thái rỗng theo GR-12.

**6b. Người dùng bấm Huỷ:**
- 6b1. Hệ thống đăng xuất, xoá phiên ghi nhớ, về màn đăng nhập (BR-account-access-014).

## Related Requirements

FR-account-access-001, 002, 003, 004, 005, 006, 007, 010, 011, 013, 014, 015, 025, 030, 031 · BR-account-access-001, 002, 003, 004, 013, 014, 015, 016
