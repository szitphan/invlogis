# UC-change-language — Thay đổi ngôn ngữ (Web)

## a. Introduction

Người dùng đổi ngôn ngữ giao diện từ menu Avatar. Mã UC gốc: Web UC02.03.01. ✅ [SRS Web tr.160 — UC02.03.01 Thay đổi ngôn ngữ]

## b. Actors & Objects

- Actor chính: Người dùng phần mềm xưởng. ✅ [SRS Web tr.160 — UC02.03.01 Thay đổi ngôn ngữ]
- Đối tượng: Ngôn ngữ giao diện.

## c. Pre-conditions

- Người dùng đã đăng nhập. Đường dẫn: icon Avatar (góc trên bên phải) > nút "Ngôn ngữ". ✅ [SRS Web tr.160 — UC02.03.01 Thay đổi ngôn ngữ]

## d. Expected result

- Hệ thống đổi ngôn ngữ thành công, hiển thị giao diện theo ngôn ngữ mới. ✅ [SRS Web tr.160 — UC02.03.01 Thay đổi ngôn ngữ]

## e. Activity diagram

Xem flows.md — Flow: Đổi ngôn ngữ (Web).

**Main Success Scenario**

1. Người dùng bấm icon Avatar; hệ thống hiện dropdown Tài khoản. ✅ [SRS Web tr.160 — hình lưu đồ UC02.03.01 Thay đổi ngôn ngữ; SRS Web tr.161 — UC02.03.01 Thay đổi ngôn ngữ]
2. Người dùng chọn "Ngôn ngữ"; hệ thống hiện dropdown Tiếng Anh, Tiếng Việt, Tiếng Nhật. ✅ [SRS Web tr.161 — hình UC02.03.01 Thay đổi ngôn ngữ; SRS Web tr.162 — UC02.03.01 Thay đổi ngôn ngữ]
3. Người dùng chọn 1 ngôn ngữ (chỉ chọn 1). ✅ [SRS Web tr.162 — UC02.03.01 Thay đổi ngôn ngữ]
4. Hệ thống tải lại giao diện theo ngôn ngữ mới và báo toast thành công. ✅ [SRS Web tr.162 — UC02.03.01 Thay đổi ngôn ngữ]

**Extensions**

Nguồn không mô tả nhánh lỗi (ví dụ tải ngôn ngữ thất bại) cho use case này. 🟡 [SRS Web tr.162 — UC02.03.01 Thay đổi ngôn ngữ]

## f. Screens

Menu Avatar (Web); Web — Ngôn ngữ.

## g. Related FR

| Bước | FR | BR | Error | Nguồn |
|---|---|---|---|---|
| 1–4 | FR-account-access-037 | BR-account-access-034 | — | SRS Web tr.162 — UC02.03.01 Thay đổi ngôn ngữ |

## h. Open Questions

OQ-16.
