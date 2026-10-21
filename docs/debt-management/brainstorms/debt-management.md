---
type: brainstorm
feature: debt-management
status: draft
updated: 2026-10-21
links:
  - docs-input/sop/quan-ly-quy-thanh-toan/quan-ly-quy-thanh-toan.md
  - docs-input/sop/sop-cung-cap-dich-vu-tong-quat.md
  - docs/_product/prd.md
  - docs/service-delivery/brainstorms/service-delivery.md
  - docs/invoice-management/brainstorms/invoice-management.md
---

# Công nợ và bảng kê

> Brainstorm khung lập 2026-10-20 để nhận các mục nguồn đã giao cho feature này (DEC-230). Chưa phỏng vấn.

## 1. Idea Seed

Quản lý bảng kê và công nợ phải thu, phải trả theo JobID; duyệt doanh thu; mua ngoài dịch vụ và thanh toán nhà cung cấp; lệch kỳ thanh toán và kỳ hạch toán. Cung cấp kết quả kiểm nợ quá hạn, hạn mức tín dụng và gia hạn nợ cho bước duyệt JobID của `service-delivery`.

## 2. Context

Feature chưa có trong Feature Map của PRD sản phẩm (PRD OQ-6, OQ-17).

Ranh giới với `service-delivery`: JobID là nơi ghi chi phí, doanh thu; feature này sở hữu quy trình riêng và trả kết quả về JobID.

Ranh giới với `invoice-management` (DEC-251): hoá đơn đầu vào, hoá đơn đầu ra, hoá đơn vô chủ, kê khai thuế và kết nối MISA thuộc `invoice-management`. Feature này lập, chốt bảng kê; bảng kê đã chốt là đầu vào để `invoice-management` phát hành hoá đơn. Tiền khách trả về gạch nợ phải thu ở đây.

## 3. Mục nguồn đã giao

| Nguồn | Tài liệu | Mục | Ghi chú sổ đối chiếu |
|---|---|---|---|
| SRC-31 | Quy trình quản lý quỹ & Thanh toán | 4.10 Thanh toán nhà cung cấp | nhận dữ liệu từ Quy trình quản lý nợ phải trả (SRC-03 5.3); chặn thanh toán NCC qua quy trình khác; hạn trả sau tính theo cách 1/cách 2, lưu trên danh mục NCC; comment 08–09/10 về lý do tách 6 quy trình |
| SRC-31 | Quy trình quản lý quỹ & Thanh toán | 5.7 Quy trình thanh toán nhà cung cấp |  |
| SRC-03 | Quy trình cung cấp dịch vụ tổng quát | 4.3 Mua ngoài dịch vụ | nhà cung cấp, phân loại, quy trình mua ngoài; kê khai trên JobID (4.2.7) ở lại service-delivery |
| SRC-03 | Quy trình cung cấp dịch vụ tổng quát | 4.3.5 Phương thức thanh toán chi phí mua ngoài (mã phí 02xx) | nhóm mã phí 02xx/0201/03xx |
| SRC-03 | Quy trình cung cấp dịch vụ tổng quát | 4.5 Lệch pha giữa kỳ thanh toán và kỳ hạch toán | kỳ ghi chi phí về muộn |
| SRC-03 | Quy trình cung cấp dịch vụ tổng quát | 4.5.3 Ghi nhận doanh thu và chi phí |  |
| SRC-03 | Quy trình cung cấp dịch vụ tổng quát | 5.3 Quy trình quản lý nợ phải trả |  |
| SRC-03 | Quy trình cung cấp dịch vụ tổng quát | 5.4 Quy trình quản lý nợ phải thu |  |

## 4. Open Questions

Chưa có — sinh khi phỏng vấn.

## 5. Next Steps

- `/brainstorm debt-management` — phỏng vấn đầy đủ từ các mục nguồn ở Mục 3
