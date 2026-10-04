# Sổ đăng ký nguồn — docs-input

> Tài liệu khách gửi (SOP, giải pháp, chứng từ mẫu, SRS cũ). Cột *tự động* do `_scripts/intake-sync.py` ghi lại mỗi lần chạy (hook) — các cột khác sửa tay được. Việc cần làm với từng nguồn ở [[_workspace/backlog.md|Backlog]].
>
> **Feed brainstorm:** ✅ đã đọc vào brainstorm/feature · ⬜ chưa · ➖ không phải nguồn brainstorm (xử lý qua task riêng). Doc trong `docs/{feature}/` trỏ tới nguồn ⬜ → script tự nâng thành ✅.
>
> **Quy ước sắp xếp:** tên kebab-case không dấu; tài liệu có ảnh nằm trong folder riêng cùng tên, ảnh ở `images/`. Thả file mới vào gốc `docs-input/` cũng được — script tự đăng ký (nhóm "Chưa phân loại") và tạo task xếp chỗ.

| Mã | File | Nhóm | Feed brainstorm | Dùng ở (tự động) | Việc mở (tự động) | Ngày nhận | Ghi chú |
|---|---|---|---|---|---|---|---|
| SRC-01 | `sop/giao-nhan-hang-hoa/giao-nhan-hang-hoa.md` | SOP & giải pháp | ✅ đã feed | `docs/_research/2026-10-02-container-deadline-alerts.md`<br>`docs/_research/2026-10-02-electronic-delivery-record.md`<br>`docs/_research/2026-10-02-eport-integration.md`<br>`docs/_research/2026-10-02-field-document-reading.md` | BL-005, BL-025, BL-026, BL-027, BL-028 | 2026-10-01 | Brainstorm điều phối Phase A + 4 báo cáo discover · 2026-10-02 thay bằng bản 18/9 "Giao nhận hàng hóa" (docx 19 trang, 5 đính kèm trùng tài liệu đã có, 9 trang scan đã đọc lại) — xem `_changes/2026-10-02-giao-nhan-hang-hoa.md` |
| SRC-02 | `sop/sop-dieu-phoi.md` | SOP & giải pháp | ✅ đã feed | `docs/_research/2026-10-02-container-deadline-alerts.md`<br>`docs/_research/2026-10-02-electronic-delivery-record.md`<br>`docs/_research/2026-10-02-eport-integration.md`<br>`docs/_research/2026-10-02-field-document-reading.md` | BL-005 | 2026-10-01 | Brainstorm điều phối Phase A + 4 báo cáo discover · 2026-10-02 thay bằng bản 18/9 "Giao nhận hàng hóa" (docx 19 trang, 5 đính kèm trùng tài liệu đã có, 9 trang scan đã đọc lại) — xem `_changes/2026-10-02-giao-nhan-hang-hoa.md` |
| SRC-03 | `sop/sop-cung-cap-dich-vu-tong-quat.md` | SOP & giải pháp | ✅ đã feed | `docs/_research/2026-10-02-container-deadline-alerts.md`<br>`docs/_research/2026-10-02-field-document-reading.md` | BL-005 | 2026-10-01 | Brainstorm điều phối Phase A + 2 báo cáo discover |
| SRC-04 | `sop/sop-ban-do-kien-thuc.md` | SOP & giải pháp | ✅ đã feed | `docs/_research/2026-10-02-electronic-delivery-record.md`<br>`docs/_research/2026-10-02-eport-integration.md` | BL-005 | 2026-09-26 | Bản tổng hợp 3 SOP do BA viết (không phải tài liệu khách) |
| SRC-05 | `sop/eup-dieu-van-2026-09-19/eup-dieu-van-2026-09-19.md` | SOP & giải pháp | ⬜ chưa feed | — | BL-005, BL-007, BL-009 | 2026-10-02 | Bản trước của SRC-06 (cùng chủ đề EUP) — tạm giữ cả 2 |
| SRC-06 | `sop/du-lieu-van-hanh-xe-2026-09-30/du-lieu-van-hanh-xe-2026-09-30.md` | SOP & giải pháp | ⬜ chưa feed | — | BL-005, BL-010 | 2026-10-02 | Sơ đồ kiến trúc dựng lại từ docx (ảnh gốc mất chữ) |
| SRC-07 | `sop/hoa-don-tra-ho-2026-10-01/hoa-don-tra-ho-2026-10-01.md` | SOP & giải pháp | ⬜ chưa feed | — | BL-005, BL-011 | 2026-10-02 | Sơ đồ kiến trúc dựng lại từ docx (ảnh gốc mất chữ) |
| SRC-08 | `danh-muc/danh-muc-dia-diem-hang-tau.md` | Danh mục | ⬜ chưa feed | `docs/_research/2026-10-02-eport-integration.md` | BL-012 | 2026-10-01 | Mới dùng ở 1 báo cáo discover (ePort) |
| SRC-09 | `tich-hop/vetc-api-cong-van-2026-09-02/vetc-api-cong-van-2026-09-02.md` | Tích hợp ngoài | ⬜ chưa feed | — | BL-006, BL-013 | 2026-10-02 | Bản scan 7 trang, chưa có chữ — chỉ ảnh trang |
| SRC-10 | `tich-hop/ecus-api-yeu-cau-2025-10-26/ecus-api-yeu-cau-2025-10-26.md` | Tích hợp ngoài | ⬜ chưa feed | — | BL-014 | 2026-10-02 |  |
| SRC-11 | `tich-hop/eport-qr-thanh-toan-2026-09-16/eport-qr-thanh-toan-2026-09-16.md` | Tích hợp ngoài | ⬜ chưa feed | — | BL-015 | 2026-10-02 |  |
| SRC-12 | `chung-tu-mau/lenh-giao-vo-mau-thuc-te.jpg` | Chứng từ mẫu | ⬜ chưa feed | — | BL-016 | 2026-10-01 | Lệnh giao vỏ điện tử có QR |
| SRC-13 | `chung-tu-mau/lenh-giao-vo-khong-mau-thuc-te.pdf` | Chứng từ mẫu | ⬜ chưa feed | — | BL-017 | 2026-10-01 | Lệnh giao vỏ khống — bản scan |
| SRC-14 | `chung-tu-mau/phieu-eeir-mau-thuc-te.pdf` | Chứng từ mẫu | ⬜ chưa feed | — | BL-018 | 2026-10-01 | Bản scan |
| SRC-15 | `chung-tu-mau/bien-ban-bat-thuong-hang-nhap.pdf` | Chứng từ mẫu | ⬜ chưa feed | — | BL-019 | 2026-10-01 | Bản scan |
| SRC-16 | `chung-tu-mau/ma-vach-hang-nhap.pdf` | Chứng từ mẫu | ⬜ chưa feed | — | BL-020 | 2026-10-01 | Bản scan 5 trang |
| SRC-17 | `chung-tu-mau/ma-vach-hang-xuat.pdf` | Chứng từ mẫu | ⬜ chưa feed | — | BL-021 | 2026-10-01 | Bản scan 3 trang |
| SRC-18 | `du-lieu-mau/thong-ke-chi-phi-chung-tu-cbt.md` | Dữ liệu mẫu | ⬜ chưa feed | — | BL-022 | 2026-10-01 | Chuyển từ xlsx (đã xoá bản gốc, còn trong git) |
| SRC-19 | `du-lieu-mau/eport-cargo-tracking-vi-du.md` | Dữ liệu mẫu | ⬜ chưa feed | — | BL-023 | 2026-10-01 | Chuyển từ xlsx (đã xoá bản gốc, còn trong git) |
| SRC-20 | `ui-common/web/web-common-rules.md` | UI common | ➖ | `design/ui-common/conventions.md`<br>`design/ui-common/screen-patterns.md` | — | 2026-10-01 | Đã chuyển đủ: SC-01…11 → CMP-01…11, mục 2.1…2.20 → GR-01…20. 40 ảnh (21 đang dùng) |
| SRC-21 | `ui-common/app/app-common-rules.md` | UI common | ➖ | `design/ui-common/conventions.md`<br>`design/ui-common/screen-patterns.md` | — | 2026-10-01 | Chưa chuyển (MSC-01…11 + 18 quy tắc). 21 ảnh (18 đang dùng) |
| SRC-22 | `srs-cu/lg-srs-export.md` | SRS cũ | ➖ | `docs/_shared/definitions.md`<br>`docs/_shared/operating-environment.md`<br>`docs/_shared/project-profile.md`<br>`docs/_shared/system-overview.md` | BL-002, BL-003, BL-004 | 2026-10-01 | SRS cũ LG, 2.610 trang. Mới trích một phần vào `_shared`; chưa reverse |

