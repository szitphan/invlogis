---
type: backlog
status: draft
updated: 2026-10-06
links:
  - docs-input/README.md
---

# Backlog

> Task tự đóng khi điều kiện cột **Xong khi** thoả (`_scripts/intake-sync.py`, chạy qua hook). Nguồn mới trong `docs-input/` tự sinh task feed. Task `manual` đóng bằng cách đổi Trạng thái thành ✅. Cú pháp điều kiện: `exists:<glob>` · `grep:<glob>:<regex>` · `fed:<nguồn>` · `!` phủ định · `&&` nối.

## Đang mở

| ID | Việc | Nguồn | Xong khi | Trạng thái | Tạo | Xong | Bằng chứng |
|---|---|---|---|---|---|---|---|
| BL-002 | Cài skill `/reverse-doc` + `/reverse-preview` từ kit ai4ba | `srs-cu/` | `exists:.claude/skills/reverse-doc/SKILL.md` | ⬜ | 2026-10-02 |  |  |
| BL-003 | Reverse SRS cũ LG sang bộ SRS chuẩn (`/reverse-doc`) | `srs-cu/` | `grep:docs/_reverse/*/*-reverse-spec.md:lg-srs-export` | ⬜ | 2026-10-02 |  |  |
| BL-004 | Tạo SRS mới từ bộ reverse LG (`/srs`) | `srs-cu/` | `grep:docs/*/srs/*-spec.md:docs/_reverse/` | ⬜ | 2026-10-02 |  |  |
| BL-005 | Chốt brainstorm điều phối (đang chờ trả lời vòng 1) | `sop/` | `exists:docs/dispatch-coordination/brainstorms/*.md` | ⬜ | 2026-10-02 |  |  |
| BL-006 | Gõ lại chữ công văn VETC từ ảnh scan 7 trang | `tich-hop/vetc-api-cong-van-2026-09-02/` | `!grep:docs-input/tich-hop/vetc-api-cong-van-2026-09-02/*.md:Không trích xuất được` | ⬜ | 2026-10-02 |  |  |
| BL-007 | Đối chiếu EUP (19/09) với Dữ liệu vận hành xe (30/09): bản sau thay thế hay bổ sung | `sop/eup-dieu-van-2026-09-19/` | `manual` | ⬜ | 2026-10-02 |  |  |
| BL-008 | Ghi bối cảnh điều vận + vai trò + đối thủ vào project-profile (từ 4 báo cáo discover) | — | `grep:docs/_shared/project-profile.md:Terminal49` | ⬜ | 2026-10-02 |  |  |
| BL-009 | Đọc và feed SRC-05 vào brainstorm/feature | `sop/eup-dieu-van-2026-09-19/eup-dieu-van-2026-09-19.md` | `fed:sop/eup-dieu-van-2026-09-19/eup-dieu-van-2026-09-19.md` | ⬜ | 2026-10-02 |  |  |
| BL-012 | Đọc và feed SRC-08 vào brainstorm/feature | `danh-muc/danh-muc-dia-diem-hang-tau.md` | `fed:danh-muc/danh-muc-dia-diem-hang-tau.md` | ⬜ | 2026-10-02 |  |  |
| BL-013 | Đọc và feed SRC-09 vào brainstorm/feature | `tich-hop/vetc-api-cong-van-2026-09-02/vetc-api-cong-van-2026-09-02.md` | `fed:tich-hop/vetc-api-cong-van-2026-09-02/vetc-api-cong-van-2026-09-02.md` | ⬜ | 2026-10-02 |  |  |
| BL-014 | Đọc và feed SRC-10 vào brainstorm/feature | `tich-hop/ecus-api-yeu-cau-2025-10-26/ecus-api-yeu-cau-2025-10-26.md` | `fed:tich-hop/ecus-api-yeu-cau-2025-10-26/ecus-api-yeu-cau-2025-10-26.md` | ⬜ | 2026-10-02 |  |  |
| BL-015 | Đọc và feed SRC-11 vào brainstorm/feature | `tich-hop/eport-qr-thanh-toan-2026-09-16/eport-qr-thanh-toan-2026-09-16.md` | `fed:tich-hop/eport-qr-thanh-toan-2026-09-16/eport-qr-thanh-toan-2026-09-16.md` | ⬜ | 2026-10-02 |  |  |
| BL-016 | Đọc và feed SRC-12 vào brainstorm/feature | `chung-tu-mau/lenh-giao-vo-mau-thuc-te.jpg` | `fed:chung-tu-mau/lenh-giao-vo-mau-thuc-te.jpg` | ⬜ | 2026-10-02 |  |  |
| BL-017 | Đọc và feed SRC-13 vào brainstorm/feature | `chung-tu-mau/lenh-giao-vo-khong-mau-thuc-te.pdf` | `fed:chung-tu-mau/lenh-giao-vo-khong-mau-thuc-te.pdf` | ⬜ | 2026-10-02 |  |  |
| BL-018 | Đọc và feed SRC-14 vào brainstorm/feature | `chung-tu-mau/phieu-eeir-mau-thuc-te.pdf` | `fed:chung-tu-mau/phieu-eeir-mau-thuc-te.pdf` | ⬜ | 2026-10-02 |  |  |
| BL-019 | Đọc và feed SRC-15 vào brainstorm/feature | `chung-tu-mau/bien-ban-bat-thuong-hang-nhap.pdf` | `fed:chung-tu-mau/bien-ban-bat-thuong-hang-nhap.pdf` | ⬜ | 2026-10-02 |  |  |
| BL-020 | Đọc và feed SRC-16 vào brainstorm/feature | `chung-tu-mau/ma-vach-hang-nhap.pdf` | `fed:chung-tu-mau/ma-vach-hang-nhap.pdf` | ⬜ | 2026-10-02 |  |  |
| BL-021 | Đọc và feed SRC-17 vào brainstorm/feature | `chung-tu-mau/ma-vach-hang-xuat.pdf` | `fed:chung-tu-mau/ma-vach-hang-xuat.pdf` | ⬜ | 2026-10-02 |  |  |
| BL-022 | Đọc và feed SRC-18 vào brainstorm/feature | `du-lieu-mau/thong-ke-chi-phi-chung-tu-cbt.md` | `fed:du-lieu-mau/thong-ke-chi-phi-chung-tu-cbt.md` | ⬜ | 2026-10-02 |  |  |
| BL-023 | Đọc và feed SRC-19 vào brainstorm/feature | `du-lieu-mau/eport-cargo-tracking-vi-du.md` | `fed:du-lieu-mau/eport-cargo-tracking-vi-du.md` | ⬜ | 2026-10-02 |  |  |
| BL-025 | Rà lại `docs/_research/2026-10-02-container-deadline-alerts.md` theo thay đổi SRC-01 (SOP giao nhận bản 18/9: số mục mới, nội dung đổi) | `sop/giao-nhan-hang-hoa/giao-nhan-hang-hoa.md` | `grep:docs/_research/2026-10-02-container-deadline-alerts.md:_changes/2026-10-02-giao-nhan-hang-hoa` | ⬜ | 2026-10-02 |  |  |
| BL-026 | Rà lại `docs/_research/2026-10-02-electronic-delivery-record.md` theo thay đổi SRC-01 (SOP giao nhận bản 18/9: số mục mới, nội dung đổi) | `sop/giao-nhan-hang-hoa/giao-nhan-hang-hoa.md` | `grep:docs/_research/2026-10-02-electronic-delivery-record.md:_changes/2026-10-02-giao-nhan-hang-hoa` | ⬜ | 2026-10-02 |  |  |
| BL-027 | Rà lại `docs/_research/2026-10-02-eport-integration.md` theo thay đổi SRC-01 (SOP giao nhận bản 18/9: số mục mới, nội dung đổi) | `sop/giao-nhan-hang-hoa/giao-nhan-hang-hoa.md` | `grep:docs/_research/2026-10-02-eport-integration.md:_changes/2026-10-02-giao-nhan-hang-hoa` | ⬜ | 2026-10-02 |  |  |
| BL-028 | Rà lại `docs/_research/2026-10-02-field-document-reading.md` theo thay đổi SRC-01 (SOP giao nhận bản 18/9: số mục mới, nội dung đổi) | `sop/giao-nhan-hang-hoa/giao-nhan-hang-hoa.md` | `grep:docs/_research/2026-10-02-field-document-reading.md:_changes/2026-10-02-giao-nhan-hang-hoa` | ⬜ | 2026-10-02 |  |  |
| BL-029 | Chạy thử `/prototype-html <feature> <link Figma>` trên 1 flow thật, sửa skill theo kết quả (khớp artboard 3b, lệch Figma↔tài liệu, đối chiếu ảnh 26b) | `.claude/skills/prototype-html/` | `grep:docs/*/html-design/*-prototype.html:data-figma-node` | ⬜ | 2026-10-04 |  |  |
| BL-030 | Chạy thử luồng usability AI trên 1 feature thật: `/brainstorm` (bảng 3.1) → `/user-flow` (Mục 3.6) → `/figma-screen` gọi `@usability-reviewer`; sửa skill/agent theo kết quả | `.claude/agents/usability-reviewer.md` | `grep:docs/*/srs/*-userflow.md:^## 3\.6\. Tác vụ chính` | ⬜ | 2026-10-04 |  |  |
| BL-031 | Đưa 4 đề xuất thẻ dùng chung (Mục 5 bản đồ đối tượng: Phương tiện, Nhà cung cấp, dòng mặt hàng, thẻ chứng từ) thành CMP qua `/update-overview patterns`, làm khi bắt đầu vẽ màn | `docs/_shared/object-map.md` | `grep:design/ui-common/screen-patterns.md:Ô chọn Nhà cung cấp` | ⬜ | 2026-10-05 |  |  |
| BL-032 | Sửa fixture KG (`skills/kg/engine/test-fixtures/`) cho khớp engine hiện tại — đang 112 pass / 25 fail, hỏng sẵn cả ở kit | `_guides/pipeline.md` P-28 | `manual` | ⬜ | 2026-10-05 |  |  |
| BL-033 | Reverse SRS mobile (feature cũ đang phát triển) sang bộ SRS chuẩn (`/reverse-doc`) | `srs-cu/srs-mobile/srs-mobile.md` | `grep:docs/_reverse/*/*-reverse-spec.md:srs-mobile` | ⬜ | 2026-10-05 |  |  |

## Đã xong

| ID | Việc | Nguồn | Xong khi | Trạng thái | Tạo | Xong | Bằng chứng |
|---|---|---|---|---|---|---|---|
| BL-010 | Đọc và feed SRC-06 vào brainstorm/feature | `sop/du-lieu-van-hanh-xe-2026-09-30/du-lieu-van-hanh-xe-2026-09-30.md` | `fed:sop/du-lieu-van-hanh-xe-2026-09-30/du-lieu-van-hanh-xe-2026-09-30.md` | ✅ | 2026-10-02 | 2026-10-06 | sổ nguồn: sop/du-lieu-van-hanh-xe-2026-09-30/du-lieu-van-hanh-xe-2026-09-30.md ✅ |
| BL-011 | Đọc và feed SRC-07 vào brainstorm/feature | `sop/hoa-don-tra-ho-2026-10-01/hoa-don-tra-ho-2026-10-01.md` | `fed:sop/hoa-don-tra-ho-2026-10-01/hoa-don-tra-ho-2026-10-01.md` | ✅ | 2026-10-02 | 2026-10-06 | sổ nguồn: sop/hoa-don-tra-ho-2026-10-01/hoa-don-tra-ho-2026-10-01.md ✅ |
| BL-001 | Chuyển app common rules (MSC-01…11 + 18 quy tắc) sang CMP/GR mobile qua `/update-overview` | `ui-common/app/` | `grep:design/ui-common/screen-patterns.md:MSC-11` | ✅ | 2026-10-02 | 2026-10-04 | `design/ui-common/screen-patterns.md` |
| BL-024 | Xếp nhóm + đặt tên, rồi đọc và feed SRC-23 vào brainstorm/feature | `sop/giao-nhan-hang-hoa/giao-nhan-hang-hoa.md` | `fed:sop/giao-nhan-hang-hoa/giao-nhan-hang-hoa.md` | ✅ | 2026-10-02 | 2026-10-02 | bản cập nhật, đã gộp vào SRC-01 (`sop/giao-nhan-hang-hoa/giao-nhan-hang-hoa.md`) |
