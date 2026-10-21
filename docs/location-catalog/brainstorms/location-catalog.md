---
type: brainstorm
feature: location-catalog
status: draft
updated: 2026-10-21
links:
  - docs-input/sop/sop-dieu-phoi.md
  - docs/_product/prd.md
  - docs/service-delivery/brainstorms/service-delivery.md
  - docs/shipment-coordination/brainstorms/shipment-coordination.md
---

# Danh mục địa điểm

> Brainstorm khung lập 2026-10-20 dưới tên `master-data` (DEC-230), đổi tên 2026-10-21 (DEC-249). Chưa phỏng vấn.

## 1. Idea Seed

Danh mục địa điểm giao nhận (cảng, bãi, kho, sân bay, cửa khẩu, ga), gồm:

- Thuộc tính phân luồng của cảng/bãi: có ePort, có xe mới chọn được vỏ, thanh lý tờ khai online hay tại bãi (`shipment-coordination` B1).
- Hãng tàu.
- Định mức chi phí theo địa điểm × loại việc: định mức hải quan (`service-delivery` E14), định mức chi phí hiện trường khi giao việc (`shipment-coordination` B20).

## 2. Context

Feature chưa có trong Feature Map của PRD sản phẩm (PRD OQ-6, OQ-17).

Ranh giới: `service-delivery` và `shipment-coordination` chỉ đọc danh mục; JobID là nơi ghi chi phí, doanh thu. Feature này sở hữu việc thêm, sửa danh mục và ai được sửa (trước ghi là OQ-47 ở userflow Điều phối).

## 3. Mục nguồn đã giao

| Nguồn | Tài liệu | Mục | Ghi chú sổ đối chiếu |
|---|---|---|---|
| SRC-02 | Quy trình điều phối | 6.3 Danh mục địa điểm giao nhận | danh mục địa điểm giao nhận, có ở SRC-08 |

## 4. Open Questions

Chưa có — sinh khi phỏng vấn.

## 5. Next Steps

- `/brainstorm location-catalog` — phỏng vấn đầy đủ từ các mục nguồn ở Mục 3
