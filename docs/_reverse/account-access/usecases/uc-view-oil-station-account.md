# UC-view-oil-station-account — Xem thông tin tài khoản cây dầu (Mobile)

## a. Introduction

Nhân viên cây dầu mua ngoài xem thông tin tài khoản của chính mình trên app Delta Partner Portal (chỉ đọc) và đăng xuất. Mã UC gốc: UC01.01.07. ✅ [SRS Mobile tr.75 — UC01.01.07 Xem thông tin tài khoản cây dầu]

## b. Actors & Objects

- Actor chính: Nhân viên cây dầu mua ngoài đã đăng nhập. ✅ [SRS Mobile tr.75 — UC01.01.07 Xem thông tin tài khoản cây dầu]
- Đối tượng: Tài khoản cây dầu, Nhà cung cấp HHDV, Người đại diện, Hạn mức tháng, Hợp đồng. ✅ [SRS Mobile tr.77 — UC01.01.07 Xem thông tin tài khoản cây dầu; SRS Mobile tr.78 — UC01.01.07 Xem thông tin tài khoản cây dầu]

## c. Pre-conditions

- Đã đăng nhập, loại tài khoản = Cây dầu. Đường dẫn: app Delta Partner Portal — Bottom Navigation > tab Tài khoản (tab cuối) hoặc tap Avatar trên Trang chủ. ✅ [SRS Mobile tr.75 — UC01.01.07 Xem thông tin tài khoản cây dầu]

## d. Expected result

- Hiển thị thông tin đầy đủ của cây dầu; đăng xuất nếu người dùng chọn. ✅ [SRS Mobile tr.75 — UC01.01.07 Xem thông tin tài khoản cây dầu]

## e. Activity diagram

Xem flows.md — Flow: Xem thông tin tài khoản cây dầu (Mobile).

**Main Success Scenario**

1. Người dùng tap tab Tài khoản hoặc Avatar trên Trang chủ. ✅ [SRS Mobile tr.75 — UC01.01.07 Xem thông tin tài khoản cây dầu]
2. Hệ thống tải thông tin tài khoản cây dầu, hiện skeleton loader khi tải. ✅ [SRS Mobile tr.75 — UC01.01.07 Xem thông tin tài khoản cây dầu]
3. Người dùng xem thông tin (chỉ đọc): avatar, tên cây dầu, mã đối tác, nhà cung cấp HHDV, người đại diện, địa chỉ, ghi chú; hạn mức tháng hiện tại; loại hợp đồng, số tiền đặt cọc (nếu Đặt cọc). ✅ [SRS Mobile tr.76 — UC01.01.07 Xem thông tin tài khoản cây dầu; SRS Mobile tr.77 — UC01.01.07 Xem thông tin tài khoản cây dầu; SRS Mobile tr.78 — UC01.01.07 Xem thông tin tài khoản cây dầu]
4. Người dùng tap "Đăng xuất" → hộp xác nhận "Bạn có chắc muốn đăng xuất?" → "Đăng xuất" → về màn đăng nhập. ✅ [SRS Mobile tr.75 — UC01.01.07 Xem thông tin tài khoản cây dầu; SRS Mobile tr.79 — UC01.01.07 Xem thông tin tài khoản cây dầu]

**Extensions**

- 3a. Cây dầu không có ảnh → icon no data. Ghi chú không có giá trị → ẩn hoàn toàn. ✅ [SRS Mobile tr.76 — UC01.01.07 Xem thông tin tài khoản cây dầu; SRS Mobile tr.77 — UC01.01.07 Xem thông tin tài khoản cây dầu]
- 3b. Loại hợp đồng "Tín chấp" → ẩn "Số tiền đặt cọc"; mục Hợp đồng ẩn hoàn toàn. ✅ (số tiền đặt cọc); 🟡 (Hợp đồng — bảng cắt) [SRS Mobile tr.78 — UC01.01.07 Xem thông tin tài khoản cây dầu; SRS Mobile tr.79 — UC01.01.07 Xem thông tin tài khoản cây dầu]
- 4a. Tap "Ở lại" ở hộp xác nhận → ở lại màn Tài khoản. 🔵 [SRS Mobile tr.79 — UC01.01.07 Xem thông tin tài khoản cây dầu]
- 3c. Muốn sửa thông tin cây dầu → không sửa trên app; thực hiện qua CBQL trên Delta ERP (UC12.04.06). ✅ [SRS Mobile tr.79 — UC01.01.07 Xem thông tin tài khoản cây dầu]

## f. Screens

Mobile — Tài khoản cây dầu; Mobile — Hộp xác nhận đăng xuất (cây dầu).

## g. Related FR

| Bước | FR | BR | Error | Nguồn |
|---|---|---|---|---|
| 1–2 | FR-account-access-038 | BR-account-access-035 | — | SRS Mobile tr.75 — UC01.01.07 Xem thông tin tài khoản cây dầu |
| 3 | FR-account-access-038, FR-account-access-039, FR-account-access-040, FR-account-access-041 | BR-account-access-036, BR-account-access-037 | — | SRS Mobile tr.77 — UC01.01.07 Xem thông tin tài khoản cây dầu; SRS Mobile tr.78 — UC01.01.07 Xem thông tin tài khoản cây dầu |
| 4 | FR-account-access-030 | BR-account-access-038 | — | SRS Mobile tr.79 — UC01.01.07 Xem thông tin tài khoản cây dầu |

## h. Open Questions

OQ-17, OQ-18.
