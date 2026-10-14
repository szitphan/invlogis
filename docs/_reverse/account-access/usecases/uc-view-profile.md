# UC-view-profile — Xem thông tin cá nhân (nội bộ)

## a. Introduction

Người dùng nội bộ xem thông tin tài khoản của mình (chỉ đọc), mở lịch sử hoạt động và đổi mật khẩu. Mã UC gốc: Web UC01.06; Mobile UC01.01.06 (Tài khoản nội bộ). ✅ [SRS Web tr.278 — UC01.06 Xem thông tin cá nhân; SRS Mobile tr.71 — UC01.01.06 Xem thông tin cá nhân - Tài khoản nội bộ]

## b. Actors & Objects

- Actor chính: Người dùng phần mềm Xưởng (Web); người dùng ứng dụng Delta Super App (Mobile). ✅ [SRS Web tr.278 — UC01.06 Xem thông tin cá nhân; SRS Mobile tr.71 — UC01.01.06 Xem thông tin cá nhân - Tài khoản nội bộ]
- Đối tượng: Tài khoản người dùng, Hồ sơ nhân viên, Lịch sử hoạt động.

## c. Pre-conditions

- Người dùng đã đăng nhập. Đường dẫn: Web — màn bất kỳ > icon Avatar > nút "Thông tin tài khoản"; Mobile — màn bất kỳ > icon Avatar > màn Thông tin tài khoản, hoặc icon Tài khoản trên Navigation Bar. ✅ [SRS Web tr.278 — UC01.06 Xem thông tin cá nhân; SRS Mobile tr.71 — UC01.01.06 Xem thông tin cá nhân - Tài khoản nội bộ]

## d. Expected result

- Người dùng xem được thông tin tài khoản của mình đang đăng nhập. ✅ [SRS Web tr.278 — UC01.06 Xem thông tin cá nhân; SRS Mobile tr.71 — UC01.01.06 Xem thông tin cá nhân - Tài khoản nội bộ]

## e. Activity diagram

Xem flows.md — Flow: Xem thông tin cá nhân.

**Main Success Scenario**

1. Người dùng bấm icon Avatar và chọn "Thông tin tài khoản" (Mobile còn icon Tài khoản trên Navigation Bar). ✅ [SRS Web tr.278 — hình lưu đồ UC01.06 Xem thông tin cá nhân; SRS Mobile tr.71 — UC01.01.06 Xem thông tin cá nhân - Tài khoản nội bộ]
2. Hệ thống hiện thông tin chỉ đọc: Họ và tên & Tên tài khoản, Trạng thái, ID nhân viên, (Web: Tên tài khoản), Chức vụ, Phòng ban, Xưởng, Ngày sinh, Giới tính, Email, SĐT, MST, Địa chỉ, Ghi chú. ✅ [SRS Web tr.279 — UC01.06 Xem thông tin cá nhân; SRS Web tr.280 — UC01.06 Xem thông tin cá nhân; SRS Mobile tr.72 — UC01.01.06 Xem thông tin cá nhân - Tài khoản nội bộ; SRS Mobile tr.73 — UC01.01.06 Xem thông tin cá nhân - Tài khoản nội bộ]

**Extensions**

- 2a. Trường không có dữ liệu (Chức vụ, Phòng ban, Xưởng, Ngày sinh, Giới tính, Email, SĐT, MST, Địa chỉ, Ghi chú) → để trống. ✅ [SRS Web tr.279 — UC01.06 Xem thông tin cá nhân; SRS Web tr.280 — UC01.06 Xem thông tin cá nhân]
- 2b. Bấm "Lịch sử hoạt động" → popup/màn Lịch sử hoạt động của nhân viên đó (hình mẫu Mobile: danh sách người thực hiện, ngày, mô tả hành động; Web không có hình). ✅ (mở màn); 🟡 (nội dung) [SRS Web tr.280 — UC01.06 Xem thông tin cá nhân; SRS Mobile tr.73 — UC01.01.06 Xem thông tin cá nhân - Tài khoản nội bộ]
- 2c. Bấm "Hành động" (Web) / menu ☰ (Mobile) → Đổi mật khẩu (mở popup, UC Đổi mật khẩu); Mobile thêm Lịch sử hoạt động và Đăng xuất (UC Đăng xuất, chữ đỏ). ✅ [SRS Web tr.281 — UC01.06 Xem thông tin cá nhân; SRS Mobile tr.74 — UC01.01.06 Xem thông tin cá nhân - Tài khoản nội bộ]

## f. Screens

Web — Xem thông tin tài khoản; Mobile — Xem thông tin tài khoản nội bộ; Menu Avatar; Popup Đổi mật khẩu.

## g. Related FR

| Bước | FR | BR | Error | Nguồn |
|---|---|---|---|---|
| 1 | FR-account-access-033, FR-account-access-034 | — | — | SRS Web tr.278 — UC01.06 Xem thông tin cá nhân; SRS Mobile tr.71 — UC01.01.06 Xem thông tin cá nhân - Tài khoản nội bộ |
| 2 | FR-account-access-033, FR-account-access-034 | BR-account-access-033 | — | SRS Web tr.279 — UC01.06 Xem thông tin cá nhân |
| 2b | FR-account-access-035 | — | — | SRS Web tr.280 — UC01.06 Xem thông tin cá nhân |
| 2c | FR-account-access-036 | — | — | SRS Web tr.281 — UC01.06 Xem thông tin cá nhân |

## h. Open Questions

OQ-15, OQ-20, OQ-23, OQ-25.
