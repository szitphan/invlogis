# Use Case: Đăng xuất

> Scope: account-access · Level: sea

## Primary Actor

Người dùng đã đăng nhập (nội bộ, đối tác)

## Trigger

Người dùng bấm Đăng xuất ở menu ảnh đại diện (web) hoặc tab Tài khoản (app).

## Preconditions

- Người dùng có phiên hợp lệ.

## Guarantees

- **Minimal Guarantee:** Huỷ ở hộp xác nhận thì không đổi gì.
- **Success Guarantee:** Phiên trên thiết bị này kết thúc; các thiết bị khác giữ phiên.

## Main Success Scenario

1. Hệ thống hiện hộp xác nhận "Đăng xuất?" (CMP-03).
2. Người dùng bấm Đăng xuất.
3. Hệ thống kết thúc phiên trên thiết bị này, về màn đăng nhập.

## Extensions

**2a. Người dùng bấm Ở lại:**
- 2a1. Đóng hộp, giữ màn đang xem.

**3a. Mất mạng:**
- 3a1. Hệ thống vẫn xoá phiên trên thiết bị, về màn đăng nhập; phiên phía hệ thống hết theo thời hạn.

## Related Requirements

FR-account-access-024
