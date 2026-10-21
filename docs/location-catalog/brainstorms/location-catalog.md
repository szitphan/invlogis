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
  - docs-input/danh-muc/danh-muc-dia-diem-hang-tau.md
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
| SRC-08 | Danh mục cảng, bãi, kho CFS, kho hàng không, hãng tàu (15/9/2026) | 1. Danh mục cảng | 36 cảng, 25 có ePort; cột "xe chọn vỏ" là danh sách hãng tàu yêu cầu (Hapag Lloyd, Maersk, ZIM, "hãng nào yêu cầu"), không phải cờ có/không; MST, tỉnh, địa chỉ giao nhận, link bản đồ |
| SRC-08 | Danh mục cảng, bãi, kho CFS, kho hàng không, hãng tàu (15/9/2026) | 2. Danh mục depot / bãi container (CY) | 88 bãi, 14 có ePort, cùng cột như cảng |
| SRC-08 | Danh mục cảng, bãi, kho CFS, kho hàng không, hãng tàu (15/9/2026) | 3. Danh mục kho CFS | không nơi nào có ePort |
| SRC-08 | Danh mục cảng, bãi, kho CFS, kho hàng không, hãng tàu (15/9/2026) | 4. Danh mục kho hàng không | cột Sân bay thay Tỉnh/TP |
| SRC-08 | Danh mục cảng, bãi, kho CFS, kho hàng không, hãng tàu (15/9/2026) | 5. Danh mục hãng tàu | 24 hãng: tên, MST, tỉnh, địa chỉ; dữ liệu ban đầu [Riêng Delta] |
| SRC-13 | Lệnh giao vỏ không màu (mẫu thực tế) | Toàn bộ chứng từ | thuộc tính bãi: bắt đăng ký thanh toán trước trên web của bãi (Greating Fortune, từ 1/6/2026), cho 3 ngày sửa thông tin hoá đơn (`shipment-coordination` A6, OQ-81) |
| SRC-12 | Lệnh giao vỏ có màu (mẫu thực tế) | Toàn bộ chứng từ | có sơ đồ đường nội bộ nhà máy, bãi (khu, cổng, khu sửa chữa): cân nhắc lưu sơ đồ theo địa điểm |

## 4. Open Questions

Chưa có — sinh khi phỏng vấn.

## 5. Next Steps

- `/brainstorm location-catalog` — phỏng vấn đầy đủ từ các mục nguồn ở Mục 3
