---
type: project-profile
status: draft
updated: 2026-10-05
links:
  - docs-input/srs-cu/lg-srs-export.md
  - docs/_shared/system-overview.md
  - docs/_shared/definitions.md
  - docs/_shared/operating-environment.md
---

# Project Profile

## Domain

Hệ thống quản lý vận hành nội bộ cho Delta — doanh nghiệp vận tải có đội xe đầu kéo, xe tải và sơ mi-rơ mooc. Hệ thống phủ các mảng: xưởng sửa chữa phương tiện, kho phụ tùng, mua hàng hoá dịch vụ, thanh toán và công nợ, quản lý phương tiện và định mức nhiên liệu, nghiệp vụ cây dầu. Dữ liệu tổ chức theo Công ty → Chi nhánh → Cơ sở (xem [[docs/_shared/system-overview.md|System Overview]]). (2026-10-01)

## Người dùng & thuật ngữ

| Nhóm user | Gọi là gì trong doc | Ghi chú | Ngày |
|---|---|---|---|
| Nhân viên Delta dùng Website | Nhân viên nội bộ Delta | Làm được gì tuỳ phân quyền (nhóm quyền, nền tảng, phạm vi chi nhánh/cơ sở) | 2026-10-01 |
| Nhân viên Delta dùng Delta Super App | Lái xe | Vẫn là nhân viên nội bộ Delta, quyền theo phân quyền. Delta Super App là tên mới của App Lái xe | 2026-10-05 |
| Quản trị hệ thống | Admin | Toàn quyền | 2026-10-01 |
| Nhân viên của đối tác cây dầu | Nhân viên đối tác cây dầu | Dùng Delta Super App (Partner Portal cũ đã gộp vào, hiện chỉ có mobile), nghiệp vụ Cấp dầu | 2026-10-05 |

Danh sách tác nhân chuẩn kèm tên gọi cần tránh: [[docs/_shared/definitions.md|Definitions]] › Actor Registry.

## Thị trường & ngôn ngữ

- Vận hành tại Việt Nam, nhiều chi nhánh (vd Hà Nội, TP.HCM). (2026-10-01)
- Giao diện: Tiếng Việt (mặc định) và Tiếng Anh. Không hỗ trợ Tiếng Nhật. (2026-10-01)
- Câu chữ giao diện theo `design/design.md` (Copy động), không dùng "Vui lòng". (2026-10-01)

## Ghi chú khác

| Câu hỏi | Trả lời | Ngày | Skill hỏi |
|---|---|---|---|
| "DK05" trong "Khách hàng DK05" nghĩa là gì? | Tạm thời chưa giải thích; dùng nguyên tên | 2026-10-01 | /update-overview |
| Gọi hành động rút lại yêu cầu chờ duyệt là gì? | Thống nhất "Thu hồi" mọi luồng (không dùng "Huỷ đề xuất") | 2026-10-01 | /update-overview |
| Tài liệu nguồn của dự án? | SRS LG — `docs-input/srs-cu/lg-srs-export.md` (bản v2.0; mục `[not done]` chưa chốt) | 2026-10-01 | /update-overview |
