---
type: srs-states
feature: account-access
updated: 2026-10-15
---

# account-access — State Diagrams

## Tài khoản

```mermaid
stateDiagram-v2
    [*] --> ChoKichHoat : Admin tạo tài khoản
    ChoKichHoat --> DangHoatDong : tạo mật khẩu mới
    ChoKichHoat --> TamKhoa : sai mật khẩu tạm đủ số lần
    DangHoatDong --> TamKhoa : sai mật khẩu đủ số lần
    TamKhoa --> DangHoatDong : hết khoá khi khoá từ Đang hoạt động, đặt lại qua email, hoặc Admin mở
    TamKhoa --> ChoKichHoat : Admin đặt lại mật khẩu, hoặc hết khoá khi khoá từ Chờ kích hoạt
    DangHoatDong --> ChoKichHoat : Admin đặt lại mật khẩu
    ChoKichHoat --> VoHieuHoa : Admin vô hiệu hoá
    DangHoatDong --> VoHieuHoa : Admin vô hiệu hoá
    TamKhoa --> VoHieuHoa : Admin vô hiệu hoá
    VoHieuHoa --> ChoKichHoat : Admin kích hoạt lại
```

| Trạng thái | Đăng nhập | Đặt lại qua email | Ghi chú |
|---|---|---|---|
| Chờ kích hoạt | Chỉ bằng mật khẩu tạm còn hạn, vào thẳng Tạo mật khẩu mới | Có | Mật khẩu tạm hạn `P-han-mat-khau-tam` |
| Đang hoạt động | Có | Có | |
| Tạm khoá | Không (E-account-access-002) | Có, thành công thì mở khoá | Tự mở sau `P-thoi-gian-tam-khoa` |
| Vô hiệu hoá | Không (E-account-access-003) | Không gửi | Chỉ Admin đổi, ở `access-control` |

Chuyển cấm: Vô hiệu hoá → Đang hoạt động (phải qua Chờ kích hoạt với mật khẩu tạm mới).

## Phiên đăng nhập

```mermaid
stateDiagram-v2
    [*] --> DangDung : đăng nhập thành công
    DangDung --> KetThuc : đăng xuất
    DangDung --> KetThuc : hết hạn
    DangDung --> KetThuc : đổi hoặc đặt lại mật khẩu ở thiết bị khác
    DangDung --> KetThuc : Admin đặt lại mật khẩu hoặc vô hiệu hoá
    DangDung --> KetThuc : huỷ chọn chi nhánh khi vừa đăng nhập
    KetThuc --> [*]
```

## Yêu cầu đặt lại mật khẩu (link, mã OTP)

```mermaid
stateDiagram-v2
    [*] --> ConHieuLuc : gửi email
    ConHieuLuc --> DangTaoMatKhau : mở link hoặc nhập đúng mã
    DangTaoMatKhau --> DaDung : lưu mật khẩu mới
    DangTaoMatKhau --> HetHieuLuc : quá thời gian tạo mật khẩu
    DangTaoMatKhau --> HetHieuLuc : đổi hoặc đặt lại mật khẩu, vô hiệu hoá
    ConHieuLuc --> HetHieuLuc : quá hạn
    ConHieuLuc --> HetHieuLuc : sai mã đủ số lần
    ConHieuLuc --> HetHieuLuc : gửi yêu cầu mới
    ConHieuLuc --> HetHieuLuc : đổi hoặc đặt lại mật khẩu, vô hiệu hoá
    DaDung --> [*]
    HetHieuLuc --> [*]
```
