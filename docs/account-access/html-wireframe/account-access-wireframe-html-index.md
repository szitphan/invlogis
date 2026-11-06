---
type: wireframe-html-index
feature: account-access
status: in-review
status_changed: 2026-11-06
status_reason: "đã review upstream, không cần sửa"
updated: 2026-10-15
links:
  - docs/account-access/srs/account-access-userflow.md
  - docs/account-access/srs/account-access-spec.md
---

# account-access — HTML Wireframes

> Wireframe HTML đen trắng, mỗi file = 1 flow, mỗi màn vẽ đúng thiết bị của nó (web: khung desktop 1920 · app: khung mobile 375). Mở `account-access-wireframe.html` để xem có mục lục. Nguồn: `srs/account-access-userflow.md` (chia flow) + SRS, use case (element, lỗi, quy tắc). Prototype chạy được (web + app): [account-access-prototype.html](../html-design/account-access-prototype.html).

## Flows

| # | Flow | File | HTML prototype | Screens (theo thứ tự) | Figma | Status | Updated |
|---|------|------|----------------|-----------------------|-------|--------|---------|
| 1 | Đăng nhập và chọn chi nhánh | [sign-in.html](sign-in.html) | [prototype#sign-in](../html-design/account-access-prototype.html#sign-in) | splash → onboarding → company-code → sign-in → channel-denied → branch-picker | [1.3 · web](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5758-133038) · [1.4 · web](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5758-133235) · [1.5 · web](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5758-134429) · [1.1 · mob](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5758-138738) · [1.2 · mob](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5758-138805) · [1.6 · mob](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5758-138908) · [1.3 · mob](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5758-139070) · [1.4 · mob](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5758-139485) · [1.5 · mob](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5758-139400) | draft | 2026-10-15 |
| 2 | Kích hoạt bằng mật khẩu tạm | [activate-account.html](activate-account.html) | [prototype#sign-in](../html-design/account-access-prototype.html#sign-in) | sign-in → create-password → sign-in | [2.1 · web](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5758-133345) · [2.1 · mob](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5758-139672) | draft | 2026-10-15 |
| 3 | Tự đặt lại mật khẩu | [reset-password.html](reset-password.html) | [prototype#forgot-options](../html-design/account-access-prototype.html#forgot-options) | forgot-options → reset-request → check-email (web) / otp-entry (app) / reset-link-expired → create-password | [3.1 · web](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5758-133676) · [3.2 · web](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5758-133778) · [3.3 · web](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5758-133924) · [3.5 · web](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5758-134039) · [3.1 · mob](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5758-139748) · [3.2 · mob](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5758-139872) · [3.4 · mob](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5758-139961) | draft | 2026-10-15 |
| 4 | Liên hệ IT | [contact-it.html](contact-it.html) | [prototype#forgot-options](../html-design/account-access-prototype.html#forgot-options) | forgot-options → contact-it → contact-it-sent | [4.1 · web](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5758-134172) · [4.2 · web](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5758-134319) · [4.1 · mob](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5758-140086) · [4.2 · mob](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5758-140150) | draft | 2026-10-15 |
| 5 | Thông tin cá nhân, lịch sử, ngôn ngữ | [account-profile.html](account-profile.html) | [prototype#account-info](../html-design/account-access-prototype.html#account-info) | account-info → activity-history; oil-station-account (đối tác) | [5.1 · web](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5758-134713) · [5.2 · web](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5758-137389) · [5.1 · mob](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5758-140340) · [5.2 · mob](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5758-140774) · [5.3 · mob](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5758-140973) | draft | 2026-10-15 |
| 6 | Đổi mật khẩu | [change-password.html](change-password.html) | [prototype#change-password](../html-design/account-access-prototype.html#change-password) | change-password → account-info | [6.1 · web](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5758-137786) · [6.1 · mob](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5758-141253) | draft | 2026-10-15 |
| 7 | Đổi chi nhánh trong phiên | [switch-branch.html](switch-branch.html) | [prototype#home](../html-design/account-access-prototype.html#home) | Home → branch-picker → Home |  | draft | 2026-10-15 |
| 8 | Đăng xuất | [sign-out.html](sign-out.html) | [prototype#sign-out-confirm](../html-design/account-access-prototype.html#sign-out-confirm) | menu ảnh đại diện → sign-out-confirm | [8.1 · web](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5758-138113) · [8.1 · mob](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=5758-140596) | draft | 2026-10-15 |

Trạng thái Đang gửi và Mất mạng vẽ 1 khung đại diện ở màn Đăng nhập (flow 1); các form khác cùng hành vi, ghi ở bảng mô tả.

## Quyết định khi vẽ (chưa có trong SRS)

- Mã doanh nghiệp [1.6]: chữ không dấu và số, không phân biệt hoa thường, tối đa 20 ký tự; ký tự khác không nhập được.
- Giới thiệu lần đầu [1.2]: 3 trang (Nhận lệnh vận chuyển · Cập nhật hành trình · Báo cáo chi phí) + Bỏ qua; câu chữ từng trang chưa chốt.
- Lịch sử hoạt động [5.2]: lọc khoảng ngày trong 90 ngày, chặn trên lịch; cuộn tự tải 20 mốc trên cả web và app; tải lỗi dùng câu của Activity Log.
- Web, quyền chi nhánh vừa đổi (E-common-012): modal chặn như app — Override GR-26.
- Web, đường dẫn đăng nhập sai (E-account-access-017): trạng thái Tenant not found của [1.3], không có nút.

## Links upstream

- [[docs/account-access/srs/account-access-userflow.md|User Flow]]
- [[docs/account-access/brainstorms/account-access.md|Brainstorm]]
- [[docs/account-access/srs/account-access-spec.md|SRS Spec]]
