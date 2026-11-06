# Use Case: Đổi chi nhánh trong phiên

> Scope: account-access · Level: sea

## Primary Actor

Người dùng nội bộ có từ 2 chi nhánh

## Trigger

Người dùng bấm tên chi nhánh đang dùng ở thanh đầu trang.

## Preconditions

- Người dùng có phiên hợp lệ và quyền ở từ 2 chi nhánh (hoặc công ty mẹ).

## Guarantees

- **Minimal Guarantee:** Không mất dữ liệu chưa lưu mà người dùng chưa đồng ý bỏ.
- **Success Guarantee:** Home của chi nhánh mới được mở; chi nhánh mới được nhớ cho lần đăng nhập sau.

## Main Success Scenario

1. Hệ thống mở cửa sổ chọn chi nhánh, chọn sẵn chi nhánh đang dùng.
2. Người dùng chọn chi nhánh khác, bấm Chọn.
3. Hệ thống lưu chi nhánh dùng lần trước, tải lại Home của chi nhánh mới.

## Extensions

**1a. Đang có dữ liệu chưa lưu:**
- 1a1. Hệ thống hỏi xác nhận rời trang theo GR-13. Người dùng huỷ thì ở lại màn; đồng ý thì bỏ dữ liệu và đi tiếp bước 1.

**2a. Người dùng bấm Huỷ:**
- 2a1. Đóng cửa sổ, giữ chi nhánh đang dùng (khác uc-dang-nhap 6b: không đăng xuất).

**3a. Mất quyền chi nhánh vừa chọn trong lúc chọn:**
- 3a1. Hệ thống báo E-common-012, tải lại danh sách chi nhánh.

## Related Requirements

FR-account-access-012 · BR-account-access-015
