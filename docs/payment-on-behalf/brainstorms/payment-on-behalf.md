---
type: brainstorm
feature: payment-on-behalf
status: draft
updated: 2026-10-20
links:
  - docs-input/sop/apas-thanh-toan-doi-soat/apas-thanh-toan-doi-soat.md
  - docs-input/sop/delta-3-0-master-plan/delta-3-0-master-plan.md
  - docs-input/sop/quan-ly-quy-thanh-toan/quan-ly-quy-thanh-toan.md
  - docs-input/tich-hop/vis-sim-cong-tac-chuan-bi/vis-sim-cong-tac-chuan-bi.md
  - docs/_product/prd.md
  - docs/service-delivery/brainstorms/service-delivery.md
---

# Thanh toán trả hộ qua ngân hàng

> Brainstorm khung lập 2026-10-20 để nhận các mục nguồn đã giao cho feature này (DEC-230). Chưa phỏng vấn.

## 1. Idea Seed

Yêu cầu thanh toán tạo từ JobID hoặc Lệnh vận tải, quét QR động hoặc tĩnh, duyệt nội bộ, lập uỷ nhiệm chi và đẩy lệnh qua API ngân hàng, thanh toán nợ hoá đơn và trả hoá đơn; xử lý QR hết hạn và khi ngân hàng lỗi.

## 2. Context

Feature chưa có trong Feature Map của PRD sản phẩm (PRD OQ-6, OQ-17).

Ranh giới với `service-delivery`: JobID là nơi ghi chi phí, doanh thu; feature này sở hữu quy trình riêng và trả kết quả về JobID.

## 3. Mục nguồn đã giao

| Nguồn | Tài liệu | Mục | Ghi chú sổ đối chiếu |
|---|---|---|---|
| SRC-07 | Phân hệ APAS — Hệ thống tự động hóa thanh toán & Đối soát công nợ | 2.1 Luồng thanh toán tự động qua API Banking | không đổi so với bản 12/10 |
| SRC-07 | Phân hệ APAS — Hệ thống tự động hóa thanh toán & Đối soát công nợ | 3.1 Thanh toán qua luồng API Banking (PAB) | trước là 3.1 Trích xuất mã QR; QR ≥3 phút hiệu lực, QR gốc <15 phút chặn, đồng chủ tài khoản 15tr/50tr, 10tr/30tr (không đổi) |
| SRC-07 | Phân hệ APAS — Hệ thống tự động hóa thanh toán & Đối soát công nợ | 4.1 Rủi ro xử lý mã QR động |  |
| SRC-30 | Phần mềm Delta 3.0 — Thiết kế kiến trúc & Lộ trình phát triển | 3.1.4 Kế toán | quản lý quỹ và thanh toán (kể cả trả hộ, cược vỏ container FCL); API ngân hàng MB, TP Bank, Vietcombank — duyệt lần 2 trên ngân hàng; sổ phụ sang quản lý công nợ để CS cấp dữ liệu cho duyệt JobID tự động; tài sản/khấu hao, CCDC/phân bổ, chi phí không hóa đơn, đồng bộ danh mục với Misa (`debt-management`) |
| SRC-30 | Phần mềm Delta 3.0 — Thiết kế kiến trúc & Lộ trình phát triển | 7.1 API Ngân hàng gặp sự cố | xuất lệnh chi ra file chuẩn (Excel/XML theo ngân hàng) để kế toán tải lên Internet Banking duyệt tay |
| SRC-31 | Quy trình quản lý quỹ & Thanh toán | 4.5 Thanh toán nợ hóa đơn | hạn trả hóa đơn 3 ngày làm việc, quá hạn khóa quyền tạo TTNHĐ; duyệt trong 2 ngày cuối tháng thì khóa từ ngày làm việc đầu tháng sau; tạo từ JobID (CS, hiện trường) và Lệnh vận tải (lái xe) |
| SRC-31 | Quy trình quản lý quỹ & Thanh toán | 4.6 Thanh toán trả hóa đơn | báo cáo dư nợ 2 đầu tháng, thu hồi bằng Phiếu thu; comment 09/10: anh Nghĩa bỏ đoạn "thanh toán không hóa đơn để nhận lại số tiền này" |
| SRC-31 | Quy trình quản lý quỹ & Thanh toán | 5.4 Quy trình thanh toán nợ hóa đơn | QR động (≥ 3 phút), QR tĩnh, tài khoản đối tác; gợi ý 3–5 cảng bãi gần lái xe; duyệt bước 1 theo giới hạn duyệt và hạn mức trên ngân hàng |
| SRC-31 | Quy trình quản lý quỹ & Thanh toán | 5.5 Quy trình thanh toán trả hóa đơn |  |
| SRC-31 | Quy trình quản lý quỹ & Thanh toán | Đính kèm 02 API Banking | bản 03/03; UNC, sổ phụ điện tử, lưu đồ dự kiến; bảng phí ngân hàng là báo giá, không phải yêu cầu (như SRC-07 5.2) |
| SRC-24 | Tích hợp hệ thống VIS & SIM — Công tác chuẩn bị | 2.3 Phân hệ SIM — Trục Tích hợp Kết nối Ngân hàng (API Banking) | lệnh chi outbound MB/TPBank/VCB, webhook sổ phụ inbound |
| SRC-24 | Tích hợp hệ thống VIS & SIM — Công tác chuẩn bị | 3.1 Ngân hàng (MB, VCB, TPBank) | 1 gói API cho 3 pháp nhân HN/HCM/Hải Phòng (BL-048 hỏi còn giữ không); lưu vết mã FT ↔ JobID; báo giá VCB, Auto-topup |

## 4. Open Questions

Chưa có — sinh khi phỏng vấn.

## 5. Next Steps

- `/brainstorm payment-on-behalf` — phỏng vấn đầy đủ từ các mục nguồn ở Mục 3
