---
type: srs-flows
feature: account-access
updated: 2026-10-15
---

# Đăng nhập và tài khoản cá nhân — Flows

## Flow: Đăng nhập
__Trigger__: Người dùng bấm Đăng nhập · __Related__: FR-account-access-001, 005, 007, 010

```mermaid
sequenceDiagram
    actor ND as Người dùng
    participant HT as Hệ thống
    ND->>HT: Tên tài khoản, mật khẩu, đường dẫn khách
    HT->>HT: Kiểm tra ô trống, khoá nút
    alt Thông tin sai, còn lượt
        HT-->>ND: E-account-access-001 kèm số lần còn lại
    else Sai đủ số lần hoặc đang Tạm khoá
        HT->>HT: Chuyển Tạm khoá
        HT-->>ND: E-account-access-002 kèm giờ mở khoá
    else Vô hiệu hoá hoặc không có chi nhánh hoặc không có quyền kênh
        HT-->>ND: E-account-access-003, 004 hoặc 005
    else Mật khẩu tạm còn hạn
        HT-->>ND: Màn Tạo mật khẩu mới
    else Hợp lệ
        HT->>HT: Bộ đếm về 0, tạo phiên
        alt Đối tác
            HT-->>ND: Home đối tác
        else Nội bộ 1 chi nhánh hoặc có chi nhánh lần trước
            HT-->>ND: Home chi nhánh
        else Nội bộ từ 2 chi nhánh
            HT-->>ND: Cửa sổ chọn chi nhánh
            ND->>HT: Chọn chi nhánh
            HT-->>ND: Home chi nhánh đã chọn
        end
    end
```

## Flow: Tự đặt lại mật khẩu (web link, app mã OTP)
__Trigger__: Người dùng xác nhận Đặt lại qua email · __Related__: FR-account-access-018, 019, 020

```mermaid
sequenceDiagram
    actor ND as Người dùng
    participant HT as Hệ thống
    participant EM as Dịch vụ email
    ND->>HT: Tên tài khoản
    alt Vượt giới hạn gửi
        HT-->>ND: E-account-access-014
    else Trong giới hạn
        opt Tài khoản đủ điều kiện và có email
            HT->>HT: Huỷ link hoặc mã cũ, tạo mới
            HT->>EM: Gửi link (web) hoặc mã OTP (app)
        end
        HT-->>ND: Màn Kiểm tra email (giống nhau mọi trường hợp)
        ND->>HT: Mở link hoặc nhập mã
        alt Mã sai, còn lượt
            HT-->>ND: E-account-access-011
        else Hết hạn, đã dùng hoặc sai đủ lần
            HT-->>ND: E-account-access-012 hoặc 013
        else Hợp lệ
            HT-->>ND: Màn Tạo mật khẩu mới
            ND->>HT: Mật khẩu mới, nhập lại
            HT->>HT: Lưu, mở khoá, kết thúc phiên khác
            HT-->>ND: Thành công, về màn đăng nhập
        end
    end
```

## Flow: Liên hệ IT
__Trigger__: Người dùng xác nhận Liên hệ IT · __Related__: FR-account-access-020, 021

```mermaid
sequenceDiagram
    actor ND as Người dùng
    participant HT as Hệ thống
    participant EM as Dịch vụ email
    actor IT as Bộ phận hỗ trợ
    ND->>HT: Tên tài khoản
    alt Vượt giới hạn gửi
        HT-->>ND: E-account-access-014
    else Tài khoản tồn tại
        HT->>EM: Yêu cầu đặt lại tới địa chỉ hỗ trợ của khách
        alt Gửi lỗi
            HT-->>ND: E-account-access-015
        else Gửi được
            EM-->>IT: Email yêu cầu
            HT-->>ND: Màn Đã gửi yêu cầu
        end
    else Tài khoản không tồn tại
        HT-->>ND: Màn Đã gửi yêu cầu
    end
    Note over IT: Đặt lại ở access-control, cấp mật khẩu tạm
```

## Flow: Cấp mật khẩu tạm và kích hoạt
__Trigger__: Admin tạo tài khoản hoặc đặt lại mật khẩu · __Related__: FR-account-access-008, 009, 016

```mermaid
sequenceDiagram
    actor AD as Admin hoặc Nhân sự
    participant HT as Hệ thống
    participant EM as Dịch vụ email
    actor ND as Người dùng
    AD->>HT: Tạo tài khoản hoặc đặt lại mật khẩu
    HT->>HT: Sinh mật khẩu tạm, chuyển Chờ kích hoạt, kết thúc mọi phiên
    alt Tài khoản có email
        HT->>EM: Gửi mật khẩu tạm
        EM-->>ND: Email mật khẩu tạm
    else Không có email
        HT-->>AD: Hiện mật khẩu tạm một lần
        AD-->>ND: Gửi ngoài phần mềm
    end
    ND->>HT: Đăng nhập bằng mật khẩu tạm
    alt Hết hạn
        HT-->>ND: E-account-access-006
    else Còn hạn
        HT-->>ND: Màn Tạo mật khẩu mới
        ND->>HT: Mật khẩu mới, nhập lại
        HT->>HT: Chuyển Đang hoạt động
        HT-->>ND: Thành công, về màn đăng nhập
    end
```
