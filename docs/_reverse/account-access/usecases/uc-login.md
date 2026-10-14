# UC-login — Đăng nhập (kèm chọn tổ chức/chi nhánh)

## a. Introduction

Người dùng chưa đăng nhập vào hệ thống bằng tên tài khoản và mật khẩu; sau đó vào Module Menu (Web) / Home (Mobile) của tổ chức/chi nhánh, hoặc được chuyển sang Tạo mật khẩu mới. Mã UC gốc: Web UC01.01; Mobile UC01.01.01. ✅ [SRS Web tr.248 — UC01.01 Đăng nhập; SRS Mobile tr.43 — UC01.01.01 Đăng nhập]

## b. Actors & Objects

- Actor chính: Người dùng chưa đăng nhập (mọi role) — Web; người dùng Delta Super App / Delta Partner Portal (mọi role) — Mobile. ✅ [SRS Web tr.248 — UC01.01 Đăng nhập; SRS Mobile tr.43 — UC01.01.01 Đăng nhập]
- Hệ thống xác thực; Admin (được nhắc trong thông báo lỗi). ✅ [SRS Web tr.257 — UC01.01 Đăng nhập]
- Đối tượng: Tài khoản người dùng, Phiên đăng nhập, Tổ chức/Chi nhánh, Quyền truy cập tổ chức/chi nhánh, Tài khoản đối tác (Cây dầu). ✅ [SRS Mobile tr.44 — UC01.01.01 Đăng nhập]

## c. Pre-conditions

- Tài khoản đang hoạt động (Mobile: "Đang hoạt động/Hoạt động"); tài khoản có quyền truy cập website / ứng dụng; người dùng chưa đăng nhập hoặc phiên đã hết hạn (Web); người dùng đã được cấp tài khoản (Mobile). ✅ [SRS Web tr.248 — UC01.01 Đăng nhập; SRS Mobile tr.43 — UC01.01.01 Đăng nhập]

## d. Expected result

- Tài khoản không dùng mật khẩu mặc định: đăng nhập thành công và vào Module Menu (Web) / Home nội bộ (Mobile) của tổ chức/chi nhánh đã chọn (hoặc chi nhánh duy nhất); phiên lưu theo tuỳ chọn "Ghi nhớ đăng nhập". ✅ [SRS Web tr.248 — UC01.01 Đăng nhập]
- Tài khoản đang dùng mật khẩu mặc định: vào màn Tạo mật khẩu mới để đổi mật khẩu lần đầu. ✅ [SRS Web tr.248 — UC01.01 Đăng nhập; SRS Mobile tr.43 — UC01.01.01 Đăng nhập]
- Tài khoản đối tác: vào thẳng Home theo loại tài khoản, không qua chọn tổ chức. ✅ [SRS Mobile tr.43 — UC01.01.01 Đăng nhập]

## e. Activity diagram

Xem flows.md — Flow: Đăng nhập; Flow: Chọn tổ chức/chi nhánh sau đăng nhập.

**Main Success Scenario**

1. (Mobile) Mở app → Splash 3 giây → kiểm tra phiên; (Web) vào hệ thống, chưa có phiên thì tự về trang đăng nhập. ✅ [SRS Mobile tr.43 — UC01.01.01 Đăng nhập; SRS Web tr.248 — UC01.01 Đăng nhập]
2. (Mobile, lần đầu hoặc sau khi xoá dữ liệu) Onboarding, bấm "Đăng nhập". ✅ [SRS Mobile tr.43 — UC01.01.01 Đăng nhập; SRS Mobile tr.46 — UC01.01.01 Đăng nhập]
3. Người dùng nhập Tên tài khoản (Web: hoặc email) và Mật khẩu, tuỳ chọn Ghi nhớ đăng nhập, bấm "Đăng nhập". ✅ [SRS Web tr.248 — UC01.01 Đăng nhập; SRS Web tr.250 — UC01.01 Đăng nhập; SRS Mobile tr.43 — UC01.01.01 Đăng nhập]
4. Hệ thống kiểm tra ô trống phía màn hình (Web), rồi gọi xác thực; nút Đăng nhập hiện spinner và khoá khi đang gọi. ✅ [SRS Web tr.248 — UC01.01 Đăng nhập; SRS Web tr.253 — UC01.01 Đăng nhập]
5. Xác thực đúng và không dùng mật khẩu mặc định: hệ thống kiểm tra số tổ chức/chi nhánh. ✅ [SRS Web tr.248 — UC01.01 Đăng nhập; SRS Mobile tr.44 — UC01.01.01 Đăng nhập]
6. Chỉ 1 chi nhánh: tự chọn, vào thẳng Module Menu / Home nội bộ. ✅ [SRS Web tr.248 — UC01.01 Đăng nhập; SRS Mobile tr.44 — UC01.01.01 Đăng nhập]
7. Từ 2 chi nhánh hoặc 2 tổ chức: hiện Modal / Bottom Sheet Chọn tổ chức; người dùng chọn công ty mẹ hoặc 1 chi nhánh (có thể tìm kiếm), bấm "Chọn" / "Xác nhận"; vào Module Menu / Home của phạm vi đã chọn. ✅ [SRS Web tr.254 — UC01.01 Đăng nhập; SRS Web tr.256 — UC01.01 Đăng nhập; SRS Mobile tr.44 — UC01.01.01 Đăng nhập; SRS Mobile tr.51 — UC01.01.01 Đăng nhập]

**Extensions**

- 1a. (Web) Có phiên hợp lệ mà vào URL đăng nhập → vào thẳng Module Menu. ✅ [SRS Web tr.257 — UC01.01 Đăng nhập]
- 1b. (Mobile) Có phiên hợp lệ → bỏ qua Onboarding và Đăng nhập, kiểm tra tổ chức. ✅ [SRS Mobile tr.43 — UC01.01.01 Đăng nhập]
- 1c. (Web) Phiên hết hạn khi đang dùng → về trang đăng nhập, banner "Phiên làm việc đã hết hạn. Vui lòng đăng nhập lại." (E-account-access-006). ✅ [SRS Web tr.257 — UC01.01 Đăng nhập]
- 4a. Có trường trống (Web) → lỗi inline, không gọi API (E-account-access-020, 🟡 chưa có câu chữ). ✅ [SRS Web tr.248 — UC01.01 Đăng nhập]
- 4b. Lỗi 5xx → toast "Đã xảy ra lỗi. Vui lòng thử lại." (E-account-access-007); mất mạng → toast "Mất kết nối. Vui lòng kiểm tra mạng." (E-account-access-008) (Web). ✅ [SRS Web tr.257 — UC01.01 Đăng nhập]
- 5a. Sai thông tin → lỗi inline, trừ 1 lần thử, xoá mật khẩu (E-account-access-001); Mobile ảnh còn lỗi theo ô "Tài khoản không hợp lệ" / "Mật khẩu không đúng" (E-account-access-021, E-account-access-022). ✅ [SRS Web tr.253 — UC01.01 Đăng nhập; SRS Mobile tr.44 — UC01.01.01 Đăng nhập]
- 5b. Sai quá ngưỡng (Web 5, Mobile 10) → khoá tài khoản; đăng nhập lại báo (E-account-access-002, E-account-access-003). ✅ [SRS Web tr.251 — UC01.01 Đăng nhập; SRS Mobile tr.44 — UC01.01.01 Đăng nhập; SRS Mobile tr.47 — UC01.01.01 Đăng nhập] (ngưỡng lệch: 🟡 OQ-1)
- 5c. Tài khoản bị khoá / vô hiệu hoá → lỗi dưới ô Mật khẩu (E-account-access-003). ✅ [SRS Web tr.257 — UC01.01 Đăng nhập]
- 5d. Không có quyền truy cập chi nhánh nào → lỗi dưới ô Mật khẩu (E-account-access-004). ✅ [SRS Web tr.257 — UC01.01 Đăng nhập]
- 5e. Không có quyền truy cập phần mềm xưởng → màn lỗi (E-account-access-005) với nút "Quay về đăng nhập". ✅ [SRS Web tr.253 — UC01.01 Đăng nhập; SRS Web tr.254 — hình lỗi UC01.01 Đăng nhập] (Mobile 🟡: hình trống)
- 5f. Đúng nhưng dùng mật khẩu mặc định → màn Tạo mật khẩu mới. ✅ [SRS Web tr.248 — UC01.01 Đăng nhập; SRS Mobile tr.44 — UC01.01.01 Đăng nhập]
- 5g. (Mobile) Tài khoản đối tác → bỏ qua chọn tổ chức, vào Home theo loại (Cây dầu → Home Partner Portal UC-PP.01). ✅ [SRS Mobile tr.43 — UC01.01.01 Đăng nhập; SRS Mobile tr.44 — UC01.01.01 Đăng nhập]
- 7a. Tìm kiếm không có kết quả → "Không tìm thấy chi nhánh phù hợp." (E-account-access-009). ✅ [SRS Web tr.256 — UC01.01 Đăng nhập; SRS Mobile tr.51 — UC01.01.01 Đăng nhập]
- 7b. Bấm Huỷ (hoặc ✕ Web) → đăng xuất, về màn Đăng nhập. ✅ [SRS Web tr.255 — UC01.01 Đăng nhập; SRS Web tr.256 — UC01.01 Đăng nhập; SRS Mobile tr.44 — UC01.01.01 Đăng nhập; SRS Mobile tr.51 — UC01.01.01 Đăng nhập]
- 7c. (Mobile) Lần đăng nhập sau, nếu còn quyền, bỏ qua Bottom Sheet theo lựa chọn đã lưu. ✅ [SRS Mobile tr.51 — UC01.01.01 Đăng nhập]
- 3a. Bấm "Quên mật khẩu" → UC Quên mật khẩu. ✅ [SRS Web tr.249 — UC01.01 Đăng nhập; SRS Mobile tr.47 — UC01.01.01 Đăng nhập]

## f. Screens

Web — Đăng nhập; Web — Modal Chọn tổ chức; Web — Màn lỗi không có quyền đăng nhập; Web — Banner phiên hết hạn trên trang Đăng nhập; Mobile — Splash; Mobile — Onboarding; Mobile — Đăng nhập; Mobile — Bottom Sheet Chọn tổ chức.

## g. Related FR

| Bước | FR | BR | Error | Nguồn |
|---|---|---|---|---|
| 1 | FR-account-access-002, FR-account-access-003, FR-account-access-017 | BR-account-access-016 | — | SRS Web tr.248 — UC01.01 Đăng nhập; SRS Mobile tr.43 — UC01.01.01 Đăng nhập |
| 2 | FR-account-access-004 | — | — | SRS Mobile tr.46 — UC01.01.01 Đăng nhập |
| 3 | FR-account-access-001, FR-account-access-005, FR-account-access-010 | BR-account-access-001, BR-account-access-002, BR-account-access-003, BR-account-access-006, BR-account-access-040 | — | SRS Web tr.250 — UC01.01 Đăng nhập; SRS Web tr.251 — UC01.01 Đăng nhập |
| 4 | FR-account-access-009, FR-account-access-018 | — | E-account-access-007, E-account-access-008, E-account-access-020 | SRS Web tr.253 — UC01.01 Đăng nhập; SRS Web tr.257 — UC01.01 Đăng nhập |
| 5 (rẽ nhánh lỗi) | FR-account-access-006, FR-account-access-007, FR-account-access-008, FR-account-access-011 | BR-account-access-004, BR-account-access-005, BR-account-access-007 | E-account-access-001 đến E-account-access-005, E-account-access-021, E-account-access-022 | SRS Web tr.253 — UC01.01 Đăng nhập; SRS Web tr.257 — UC01.01 Đăng nhập |
| 6–7 | FR-account-access-012, FR-account-access-013, FR-account-access-014, FR-account-access-015 | BR-account-access-008 đến BR-account-access-015 | E-account-access-009 | SRS Web tr.254 — UC01.01 Đăng nhập; SRS Mobile tr.49 — UC01.01.01 Đăng nhập |
| 1c | FR-account-access-016 | — | E-account-access-006 | SRS Web tr.257 — UC01.01 Đăng nhập |

## h. Open Questions

OQ-1, OQ-3, OQ-6, OQ-7, OQ-8, OQ-9, OQ-10, OQ-17, OQ-19, OQ-21, OQ-22.
