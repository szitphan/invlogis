---
type: brainstorm
feature: cost-catalog
status: draft
updated: 2026-10-20
links:
  - docs-input/sop/quan-ly-quy-thanh-toan/quan-ly-quy-thanh-toan.md
  - docs-input/srs-cu/lg-srs-export.md
  - docs/_product/prd.md
  - docs/service-delivery/brainstorms/service-delivery.md
  - docs/_reverse/cost-catalog/cost-catalog-reverse-spec.md
---

# Khoản mục chi phí cấp 1–3

> Brainstorm khung lập 2026-10-20 để nhận các mục nguồn đã giao cho feature này (DEC-230). Chưa phỏng vấn.

## 1. Idea Seed

Danh mục khoản mục chi phí cấp 1–3 có đề xuất và duyệt; JobID kế toán theo nhóm phí cấp 1; nhóm phí hoa hồng trả khách (`service-delivery` E20). Bộ tái lập từ SRS cũ: `docs/_reverse/cost-catalog/`.

## 2. Context

Feature có trong PRD sản phẩm, Mục 7.9 ([[docs/_product/prd.md|PRD]]).

Ranh giới với `service-delivery`: JobID là nơi ghi chi phí, doanh thu; feature này sở hữu quy trình riêng và trả kết quả về JobID.

## 3. Mục nguồn đã giao

| Nguồn | Tài liệu | Mục | Ghi chú sổ đối chiếu |
|---|---|---|---|
| SRC-22 | SRS cũ LG (lg-export) | Feature 03.10 - Chi phí cấp 1 | tr. 578 |
| SRC-22 | SRS cũ LG (lg-export) | 03.10 - Thông báo & Lịch sử hoạt động | tr. 579 |
| SRC-22 | SRS cũ LG (lg-export) | UC03.10.01 - Xem danh mục chi phí cấp 1 | tr. 581 |
| SRC-22 | SRS cũ LG (lg-export) | UC03.10.02 - Xem thông tin chi phí cấp 1 | tr. 585 |
| SRC-22 | SRS cũ LG (lg-export) | UC03.10.03 - Tạo đề xuất tạo mới chi phí cấp 1 | tr. 591 |
| SRC-22 | SRS cũ LG (lg-export) | UC03.10.04 - Huỷ đề xuất cấp mới chi phí cấp 1 | tr. 598 |
| SRC-22 | SRS cũ LG (lg-export) | UC03.10.05 - Phê duyệt/Từ chối đề xuất cấp mới chi phí cấp 1 | tr. 603 |
| SRC-22 | SRS cũ LG (lg-export) | Feature 03.11 - Chi phí cấp 2 | tr. 611 |
| SRC-22 | SRS cũ LG (lg-export) | 03.11 - Thông báo & Lịch sử hoạt động | tr. 612 |
| SRC-22 | SRS cũ LG (lg-export) | UC03.11.01 - Xem danh mục chi phí cấp 2 | tr. 614 |
| SRC-22 | SRS cũ LG (lg-export) | UC03.11.02 - Xem thông tin chi phí cấp 2 | tr. 618 |
| SRC-22 | SRS cũ LG (lg-export) | UC03.11.03 - Tạo đề xuất tạo mới chi phí cấp 2 | tr. 625 |
| SRC-22 | SRS cũ LG (lg-export) | UC03.11.04 - Huỷ đề xuất cấp mới chi phí cấp 2 | tr. 632 |
| SRC-22 | SRS cũ LG (lg-export) | UC03.11.05 - Phê duyệt/Từ chối đề xuất cấp mới chi phí cấp 2 | tr. 637 |
| SRC-22 | SRS cũ LG (lg-export) | Feature 03.12 - Chi phí cấp 3 | tr. 645 |
| SRC-22 | SRS cũ LG (lg-export) | 03.12 - Thông báo & Lịch sử hoạt động | tr. 646 |
| SRC-22 | SRS cũ LG (lg-export) | UC03.12.01 - Xem danh mục chi phí cấp 3 | tr. 648 |
| SRC-22 | SRS cũ LG (lg-export) | UC03.12.02 - Xem thông tin chi phí cấp 3 | tr. 652 |
| SRC-22 | SRS cũ LG (lg-export) | UC03.12.03 - Tạo đề xuất tạo mới chi phí cấp 3 | tr. 657 |
| SRC-22 | SRS cũ LG (lg-export) | UC03.12.04 - Huỷ đề xuất cấp mới chi phí cấp 3 | tr. 666 |
| SRC-22 | SRS cũ LG (lg-export) | UC03.12.05 - Phê duyệt/Từ chối đề xuất cấp mới chi phí cấp 3 | tr. 671 |
| SRC-31 | Quy trình quản lý quỹ & Thanh toán | Đính kèm 05 — JobID kế toán (2.2, 3.2, Phụ lục 4.2, 4.4) | K01–K07 theo nhóm phí cấp 1/cấp 2 |

## 4. Open Questions

Chưa có — sinh khi phỏng vấn.

## 5. Next Steps

- `/brainstorm cost-catalog` — phỏng vấn đầy đủ từ các mục nguồn ở Mục 3
