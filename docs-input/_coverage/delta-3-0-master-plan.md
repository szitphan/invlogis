# Sổ đối chiếu: Phần mềm Delta 3.0 — Thiết kế kiến trúc & Lộ trình phát triển (SRC-30)

> Nguồn: `sop/delta-3-0-master-plan/delta-3-0-master-plan.md`
> Bản: 16/10/2026 (nhận 2026-10-19)

Tài liệu định hướng cấp dự án của Delta (kiến trúc 3 giai đoạn, 6 phân hệ, lộ trình, nguyên tắc AI, mã nguồn, quản trị dữ liệu, rủi ro API). Mục có yêu cầu chức năng thì giao feature. Mục cấp dự án (kiến trúc, lộ trình, AI) để ⬜ chờ đưa vào `docs/_shared/system-overview.md`, `docs/_product/prd.md`, roadmap. Quy chế nội bộ của Delta thì ➖.

| Mục | Kết quả | Ở đâu | Ghi chú |
|---|---|---|---|
| I. Mục tiêu | ➖ | | giới thiệu; "Phần mềm Delta 3.0" = Delta 3.0 + Delta MIS + công cụ AI |
| II. Cấu trúc Delta 3.0 | ✅ | `docs/_shared/system-overview.md` Architecture; `docs/_product/prd.md` Mục 9 | 3 giai đoạn: GĐ1 MIS cơ bản (vận tải, hải quan, thủ tục chuyên ngành, dịch vụ GTGT), GĐ2 các phân hệ còn lại, GĐ3 chuyển sang Genetic AI platform — đưa vào `docs/_shared/system-overview.md` |
| 2.1 Delta 3.0 với node AI & workflow AI | ✅ | `docs/_shared/system-overview.md` External Integrations, Architecture | kiến trúc 3 lớp (Database · Delta MIS + node AI · Mobile App) + kết nối API ngân hàng, Misa, EUP, Google Maps, Việt MAP — đưa vào `system-overview` |
| 2.1.2 Liên kết ngoại vi | ➡ invoice-management | | Delta MIS đẩy bút toán từng giao dịch sang Misa qua API để Misa lập tờ khai thuế, BCTC; "cần xác định quy tắc chia sẻ dữ liệu giữa Delta MIS và Misa để hạn chế việc chỉnh sửa" (câu hỏi mở) |
| 2.2 Delta 3.0 với Genetic AI platform | ➖ | | Giai đoạn 3 (sau GĐ2, kết thúc 31/12/2027, ước 6 tháng): AI Agent (Quick Desktop, Copilot) làm việc qua MCP Server; ngoài phạm vi hiện tại, ghi nhận khi lập roadmap |
| 2.2.1 Thiết lập ranh giới dữ liệu sạch (Data Validation Gateway) chống Rác AI | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` A11 | kiểm dữ liệu AI đọc chứng từ; phần hoá đơn đầu vào cùng quy tắc ở invoice-management |
| 2.2.3 Kiến trúc bảo mật đa tầng (Multi-Layer Security) | ✅ | `docs/_product/prd.md` Mục 9.1 | kiểm dữ liệu ở tầng API, quyền theo người dùng thật đằng sau AI Agent, phân quyền theo hàng dữ liệu (RLS) — NFR cấp sản phẩm (`prd`), liên quan `access-control`, `organization` |
| 3.1 Phân hệ và chức năng | ✅ | `docs/_product/prd.md` Mục 7 | 6 phân hệ đã giao feature ở các dòng 3.1.1–3.1.6 |
| 3.1.1 Hệ thống | ➡ access-control | | người dùng, phân quyền, danh mục |
| 3.1.2 Xưởng sửa chữa | ➡ vehicle-management | | phương tiện + trang thiết bị, chi phí sửa chữa + tồn kho phụ tùng (`repair-order`, `stock-movement`), dầu diesel theo mã iGas (`fuel-issuing`, `fuel-stations`); tích hợp phần mềm cây dầu iGas (Delta đã mua bản quyền); cấp tài khoản cho nhà cung cấp dầu để nhận yêu cầu cấp dầu, chốt bảng kê, gửi hóa đơn (`fuel-payment`) |
| 3.1.3 Nghiệp vụ | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` Mục 2 Phạm vi, E14, E20, E21, OQ-70 | cước quốc tế, cho thuê kho chưa có loại JobID (OQ-70); WMS giai đoạn 2; API bản đồ, tài khoản nhà cung cấp vận tải ➡ transport-dispatch; lập, chốt bảng kê, công nợ ➡ debt-management |
| 3.1.4 Kế toán | ➡ payment-on-behalf | | quản lý quỹ và thanh toán (kể cả trả hộ, cược vỏ container FCL); API ngân hàng MB, TP Bank, Vietcombank — duyệt lần 2 trên ngân hàng; sổ phụ sang quản lý công nợ để CS cấp dữ liệu cho duyệt JobID tự động; tài sản/khấu hao, CCDC/phân bổ, chi phí không hóa đơn, đồng bộ danh mục với Misa (`debt-management`) |
| 3.1.5 Sales | ✅ | `docs/_product/prd.md` OQ-16 | Sales giai đoạn 2, chưa có feature |
| 3.1.6 Nhân sự | ➡ employee-records | | lương thưởng từ Module điều vận, BHXH, nợ cá nhân, quỹ hỗ trợ lái xe, sales fund, phạt; thanh tra vận tải và sự cố nghề nghiệp, bảo hiểm phương tiện |
| 3.2 Sơ đồ phân hệ Delta MIS | ➖ | | sơ đồ tóm tắt 3.1 (Nghiệp vụ gồm Cung cấp dịch vụ tổng quát, Điều phối, Điều vận, Forwarding, Cho thuê kho) |
| 3.3 Lộ trình phát triển | ✅ | `docs/_product/prd.md` Mục 9 | GĐ1 01/9/2026–31/3/2027, GĐ2 01/4–31/12/2027; Xưởng đã hoàn thiện, đang hiệu chỉnh và go live; dầu go live 15/10/2026; Kế toán quỹ + thanh toán go live trên Delta 2.0 trước 31/12/2026 — đưa vào roadmap (`docs/_product/`) |
| IV. Ứng dụng AI | ✅ | `docs/_product/prd.md` Mục 9.1 | AI ở lớp 2 (node trong quy trình, nhận dữ liệu rời rạc) và lớp 3 (quy trình độc lập trả kết quả qua API); sẵn sàng cho kiểm toán bảo mật dữ liệu của khách (Second-Party Audit) — NFR cấp sản phẩm (`prd`) |
| 4.2 Nguyên tắc sử dụng AI | ➖ | | quy định nội bộ cho nhân viên Delta (có trách nhiệm, đề xuất TGĐ duyệt, không lưu dữ liệu trung gian trên Google Docs/Sheets) |
| 4.3 Phương pháp sử dụng AI | ✅ | `docs/_product/prd.md` Mục 9.1 | nhúng AI vào quy trình, kích hoạt theo hành động trên Delta MIS (không copy-paste ra AI ngoài) — cùng nhóm NFR AI |
| 4.4 Chi phí sử dụng AI | ✅ | `docs/_product/prd.md` Mục 9.1 | Delta MIS phải đo được query/token phát sinh theo từng quy trình nghiệp vụ — yêu cầu đo lường dùng AI theo khách (SaaS: theo tenant) |
| V. Mã nguồn & Vận hành liên tục | ➖ | | quy chế nội bộ Delta: quyền sở hữu mã nguồn, GitHub/GitLab do Ban giám đốc giữ, duyệt mã, sao lưu hằng ngày, ký gửi mã nguồn (Viettel Cyber Security hoặc FPT), thu hồi quyền khi nghỉ, hotfix bổ sung duyệt trong 12 giờ; ⚠ đụng hợp đồng SaaS (quyền sở hữu mã nguồn, escrow) — báo user, không phải yêu cầu chức năng |
| VI. Quản trị dữ liệu (Data Governance) | ✅ | `docs/_product/prd.md` Mục 9.1 | chuẩn bị kiểm toán bảo mật dữ liệu — NFR cấp sản phẩm |
| 6.1 Phân loại và dịnh danh dữ liệu (Data classification) | ✅ | `docs/_product/prd.md` Mục 9.1 | 4 cấp: pháp lý (mã hóa, lưu biệt lập), quản trị/tài chính (P/L Jobsheet, công nợ, hợp đồng, bảng lương — chỉ người được phân quyền), vận hành, công cộng |
| 6.2 Nguyên tắc lưu trữ dữ liệu (Data lifecycle) | ✅ | `docs/_product/prd.md` Mục 9.1 | thời hạn thành P-thoi-gian-luu-chung-tu, P-thoi-gian-luu-log |
| 6.3 Quyền truy cập dữ liệu (Access control) | ➡ organization | | phân quyền theo hàng dữ liệu theo chi nhánh, đội xe, luồng AI — khớp "phân vùng dữ liệu theo chi nhánh" của `organization` |
| 6.4 Sao lưu cơ sở dữ liệu (Database backup) | ➖ | | phương án sao lưu sẽ phát triển trước GĐ3, việc hạ tầng |
| VII. Rủi ro vận hành | ✅ | `docs/_product/prd.md` Mục 9.1 | mục con giao riêng ở 7.1–7.5 |
| 7.1 API Ngân hàng gặp sự cố | ✅ | `docs/payment-on-behalf/brainstorms/payment-on-behalf.md` A15 | xuất lệnh chi ra file chuẩn (Excel/XML theo ngân hàng) để kế toán tải lên Internet Banking duyệt tay |
| 7.2 API Phần mềm kế toán Misa gặp sự cố | ✅ | `docs/invoice-management/brainstorms/invoice-management.md` D2 | hàng chờ cô lập + tự gửi lại mỗi 15 phút đến khi thông |
| 7.3 API Bản đồ (Google Maps / Việt MAP) gặp sự cố | ➡ transport-dispatch | | điều vận nhập tay km cung đường + phí trạm vé, Lệnh vẫn phát hành, số liệu đánh dấu cho thanh tra rà lại |
| 7.4 Quản lý chi phí Token | ➖ | | thử nghiệm LLM nội bộ (Llama 3, Qwen) trên cloud riêng — quyết định hạ tầng |
| 7.5 Xử lý vòng lặp vô hạn (Infinite Loop / Token Bleeding) | ✅ | `docs/_product/prd.md` Mục 9.1 | ngưỡng thành P-gioi-han-luot-goi-ai, P-gioi-han-thoi-gian-tac-vu-ai |
