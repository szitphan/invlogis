---
type: brainstorm
feature: fund-payments
status: draft
updated: 2026-10-21
links:
  - docs-input/sop/quan-ly-quy-thanh-toan/quan-ly-quy-thanh-toan.md
  - docs/_product/prd.md
  - docs/service-delivery/brainstorms/service-delivery.md
---

# Quỹ, tạm ứng và thanh toán

> Brainstorm khung lập 2026-10-20 để nhận các mục nguồn đã giao cho feature này (DEC-230). Chưa phỏng vấn.

## 1. Idea Seed

Quản lý quỹ tiền mặt, tạm ứng và dư nợ tạm ứng của nhân viên, thanh toán có và không hoá đơn, tiền đặt cọc (cược vỏ container), phiếu chi, phiếu thu, số âm trong thanh toán, hạn mức tạm ứng và phân quyền duyệt.

## 2. Context

Feature chưa có trong Feature Map của PRD sản phẩm (PRD OQ-6, OQ-17).

Ranh giới với `service-delivery`: JobID là nơi ghi chi phí, doanh thu; feature này sở hữu quy trình riêng và trả kết quả về JobID.

## 3. Mục nguồn đã giao

| Nguồn | Tài liệu | Mục | Ghi chú sổ đối chiếu |
|---|---|---|---|
| SRC-31 | Quy trình quản lý quỹ & Thanh toán | 4.1 Các khái niệm chung | JobID; đơn vị nhận tiền trả hộ (hãng tàu, cảng, bãi) không phải nhà cung cấp; cấm số âm trên Yêu cầu thanh toán, Đề nghị tạm ứng, phiếu thu/chi |
| SRC-31 | Quy trình quản lý quỹ & Thanh toán | 4.2 Tạm ứng tiền mặt | bỏ "tạm ứng chuyển khoản"; tạm ứng hóa đơn trả hộ < 5 triệu; hạn 7 ngày từ ngày duyệt Phiếu chi, cảnh báo còn 2 ngày, quá hạn khóa tạm ứng mới; gia hạn rút gọn 3 bước; 2 tiêu chí phân loại; hạn mức theo mã nhân viên; 5 trạng thái; "Dư nợ tạm ứng 1" |
| SRC-31 | Quy trình quản lý quỹ & Thanh toán | 4.3 Dư nợ tạm ứng của nhân viên | 3 loại dư nợ; dư nợ 2 (TTNHĐ) là tài khoản trung gian, không sang Misa, không hạn mức; dư nợ 3 (đặt cọc) là TK 244; chuyển giao khi nghỉ việc/chuyển việc |
| SRC-31 | Quy trình quản lý quỹ & Thanh toán | 4.4 Thanh toán & Thanh toán có hóa đơn | phân loại theo nhóm phí (JobID kế toán/nghiệp vụ) và theo 6 mục đích; không đối ứng tạm ứng, dư nợ 1 chuyển sang module nhân sự; 4 trạng thái Yêu cầu thanh toán |
| SRC-31 | Quy trình quản lý quỹ & Thanh toán | 4.7 Thanh toán không hóa đơn | chi phí quản lý chung không chứng từ; chi phí định mức (COGS) ghi lên Mã nhân viên; hoa hồng khách hàng qua Mã DK05; comment 09/10: tạm ứng không hạn chế, quản lý ở module nhân sự; ⚠ chốt ranh giới với `employee-records` (BL-215) |
| SRC-31 | Quy trình quản lý quỹ & Thanh toán | 4.8 Quản lý tiền đặt cọc | 5 trường hợp đặt cọc; TK 244, dư nợ 3 không hạn mức; hoàn trả nhiều lần; không đòi được thì ghi TK 811 / TK 1388 |
| SRC-31 | Quy trình quản lý quỹ & Thanh toán | 4.9 Phiếu chi và Phiếu thu | phần mềm tự tạo phiếu từ Yêu cầu thanh toán/Đề nghị tạm ứng; thủ quỹ tạo tay chỉ ở tình huống đặc biệt |
| SRC-31 | Quy trình quản lý quỹ & Thanh toán | 4.11 Hướng dẫn thực hiện các quy trình | bảng 8 quy trình; tạm ứng hóa đơn trả hộ < 5 triệu hoặc tổng < 5 triệu/ngày |
| SRC-31 | Quy trình quản lý quỹ & Thanh toán | 4.12 Số âm trong thanh toán và tạm ứng | 15 trường hợp ở Đính kèm 04 |
| SRC-31 | Quy trình quản lý quỹ & Thanh toán | 5.1 Quy trình tạm ứng tiền mặt | duyệt 2 bước; chủ tài khoản chính duyệt trên ngân hàng; webhook lấy UNC; ⚠ đồng chủ tài khoản lệch APAS 3.1 (BL-215) |
| SRC-31 | Quy trình quản lý quỹ & Thanh toán | 5.2 Quy trình thanh toán có hóa đơn | chọn hóa đơn từ AI01 cùng nhóm phí, tổng tiền tự cộng; comment 09/10: biên lai cũng dùng quy trình này, duyệt xong là trả tiền; ⚠ 2 bước duyệt, APAS 3.3 là 3 cấp (BL-215) |
| SRC-31 | Quy trình quản lý quỹ & Thanh toán | 5.3 Quy trình thanh toán không hóa đơn |  |
| SRC-31 | Quy trình quản lý quỹ & Thanh toán | 5.6 Quy trình quản lý tiền đặt cọc |  |
| SRC-31 | Quy trình quản lý quỹ & Thanh toán | 5.8 Quy trình Phiếu chi |  |
| SRC-31 | Quy trình quản lý quỹ & Thanh toán | 5.9 Quy trình Phiếu thu |  |
| SRC-31 | Quy trình quản lý quỹ & Thanh toán | 5.10 Quy trình quản lý quỹ tiền mặt | bổ sung quỹ bằng séc hoặc API Banking |
| SRC-31 | Quy trình quản lý quỹ & Thanh toán | 6.1 Quy tắc ghi chép đối ứng | ghi 1 lần, khóa sau khi ghi; sửa sai bằng phiếu thu/chi, không dùng số âm; không dùng khái niệm "Hoàn ứng" |
| SRC-31 | Quy trình quản lý quỹ & Thanh toán | 6.2 Hạn mức tạm ứng | 5 mức theo chức danh (CS, hiện trường, sales, thanh tra: 0–60 triệu; CBQL 30–120 triệu; BGĐ 100–500 triệu); lái xe không có hạn mức; khi viết brainstorm cần đưa qua mã tham số P-… |
| SRC-31 | Quy trình quản lý quỹ & Thanh toán | 6.4 Phân quyền duyệt tạm ứng & thanh toán | bảng quy trình × nhóm phí, bản gốc tự ghi "dự thảo, có thể chưa nhất quán"; bảng gọi Phiếu chi/Phiếu thu là 5.7/5.8 trong khi thân bài là 5.8/5.9; 6.4.2 hạn mức duyệt còn trống (BL-215) |
| SRC-31 | Quy trình quản lý quỹ & Thanh toán | 6.5 Báo cáo | 6 mẫu báo cáo (tạm ứng, có HĐ, không HĐ, TTNHĐ & TTTHĐ, đặt cọc, quỹ tiền mặt) |
| SRC-31 | Quy trình quản lý quỹ & Thanh toán | Đính kèm 04 Thanh toán âm | 15 trường hợp + giải pháp đề xuất |
| SRC-31 | Quy trình quản lý quỹ & Thanh toán | Đính kèm 07 Bảng phân quyền duyệt (xlsx) | bản Excel của 6.4.1, thêm mã nhóm phí 03xx |

## 4. Ghi nhận trước phỏng vấn

Từ phỏng vấn SIM 14/10/2026:

- S1 [SOP+] [Lõi] [Cấu hình] Dư nợ tạm ứng của từng nhân viên (dư nợ tạm ứng 1, 2, 3) hiện trên phần mềm cho nhân viên và người duyệt. Có Đề nghị tạm ứng mới mà dư nợ cũ vượt `P-han-muc-du-no-tam-ung` (Delta: chưa chốt, OQ-1) hoặc còn khoản quá hạn thì cảnh báo người duyệt. Dư nợ tạm ứng 2 tăng khi `payment-on-behalf` chi, giảm khi `invoice-management` khớp hóa đơn với mã FT (B7) hoặc kế toán duyệt Yêu cầu trả hóa đơn; không sang phần mềm kế toán. Mức: P1 (DEC-253).

## 5. Open Questions

| ID | Câu hỏi | Nguồn khách | Trạng thái |
|---|---|---|---|
| OQ-1 | Cảnh báo dư nợ khi tạm ứng mới dùng chính hạn mức tạm ứng theo chức danh (mục 6.2) hay một ngưỡng riêng? Dư nợ tạm ứng 2, 3 không có hạn mức (mục 4.3) thì có cảnh báo không? | Quy trình quản lý quỹ & Thanh toán (06/10/2026), mục 4.3, 6.2 | Còn mở |

## 6. Next Steps

- `/brainstorm fund-payments` — phỏng vấn đầy đủ từ các mục nguồn ở Mục 3
