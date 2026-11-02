# Khoản mục chi phí cấp 1–3 (`cost-catalog`) — Gaps & Open Questions

## 1. Open Questions

- [ ] OQ-1: Tên chi phí phải unique trong phạm vi nào — toàn cấp, trong cùng cấp cha, hay có tính cả bản ghi Đã huỷ/Đã từ chối? — liên quan: Mục 5 BR-cost-catalog-003, Mục 6 E-cost-catalog-001 · cần: PO/BA quyết — Nguồn nội bộ: `docs-input/srs-cu/lg-srs-export.md` trang 592, 626, 658 — Nguồn khách: Tài liệu SRS - ERP Delta 3.0 (Web) (bản 30/9/2026), UC03.10.03 / UC03.11.03 / UC03.12.03 Tạo đề xuất tạo mới chi phí cấp 1 / 2 / 3, trang 592, 626, 658
- [ ] OQ-2: Người tạo đề xuất có được tự phê duyệt đề xuất của chính mình không (nguồn chỉ nói "người dùng có quyền phê duyệt/từ chối")? — liên quan: Mục 3 FR-cost-catalog-015, Mục 5 BR-cost-catalog-010 · cần: PO/khách quyết — Nguồn nội bộ: `docs-input/srs-cu/lg-srs-export.md` trang 580, 603 — Nguồn khách: Tài liệu SRS - ERP Delta 3.0 (Web) (bản 30/9/2026), Thông báo & Lịch sử hoạt động Chi phí cấp 1, trang 580; UC03.10.05 Phê duyệt/Từ chối đề xuất cấp mới chi phí cấp 1, trang 603
- [ ] OQ-3: Khoản mục đã Phê duyệt có được sửa tên/tên tiếng Anh/ghi chú, đổi cấp cha, ngừng dùng hoặc xoá không? Hiện chỉ có tạo mới. — liên quan: Mục 3 bảng vòng đời danh mục · cần: PO/khách quyết — Nguồn nội bộ: `docs-input/srs-cu/lg-srs-export.md` trang 284, 610 — Nguồn khách: Tài liệu SRS - ERP Delta 3.0 (Web) (bản 30/9/2026), Lưu đồ trạng thái chung cho danh mục, trang 284; UC03.10.05 mục 3.4 Đã phê duyệt, trang 610
- [ ] OQ-4: "Xoá yêu cầu" xoá hẳn bản ghi hay chỉ ẩn? Lịch sử hoạt động và mã đề xuất còn lưu không? — liên quan: Mục 3 FR-cost-catalog-019 · cần: PO/BA quyết — Nguồn nội bộ: `docs-input/srs-cu/lg-srs-export.md` trang 589, 601 — Nguồn khách: Tài liệu SRS - ERP Delta 3.0 (Web) (bản 30/9/2026), UC03.10.02 Xem thông tin chi phí cấp 1, trang 589; UC03.10.04, trang 601
- [ ] OQ-5: Mã chi phí vượt giới hạn thì xử lý thế nào — cấp 1 quá 99, cấp 2 quá 99 trong một cấp 1, cấp 3 quá 999 trong một cặp cấp 1-cấp 2? — liên quan: Mục 5 BR-cost-catalog-014 · cần: PO/BA quyết — Nguồn nội bộ: `docs-input/srs-cu/lg-srs-export.md` trang 609, 643, 677 — Nguồn khách: Tài liệu SRS - ERP Delta 3.0 (Web) (bản 30/9/2026), UC03.10.05 / UC03.11.05 / UC03.12.05 Phê duyệt/Từ chối đề xuất cấp mới chi phí cấp 1 / 2 / 3, trang 609, 643, 677
- [ ] OQ-6: Import danh mục có phải qua phê duyệt đề xuất không? Quy tắc kiểm tra trùng tên, mã, cấp cha khi nhập? (nguồn chỉ trỏ "Common Rules") — liên quan: Mục 3 FR-cost-catalog-002 · cần: PO/BA quyết — Nguồn nội bộ: `docs-input/srs-cu/lg-srs-export.md` trang 583, 616, 650 — Nguồn khách: Tài liệu SRS - ERP Delta 3.0 (Web) (bản 30/9/2026), UC03.10.01 / UC03.11.01 / UC03.12.01 Xem danh mục chi phí cấp 1 / 2 / 3, trang 583, 616, 650
- [ ] OQ-7: Ma trận phân quyền chi tiết cho từng cấp và từng hành động (Xem, Tạo đề xuất, Huỷ đề xuất, Phê duyệt/Từ chối)? — liên quan: Mục 5 BR-cost-catalog-010 · cần: PO/BA quyết — Nguồn nội bộ: `docs-input/srs-cu/lg-srs-export.md` trang 581, 585, 591, 598, 603 — Nguồn khách: Tài liệu SRS - ERP Delta 3.0 (Web) (bản 30/9/2026), điều kiện trước UC03.10.01 đến UC03.10.05, trang 581, 585, 591, 598, 603
- [ ] OQ-8: CHG-20 — chờ Delta gửi bảng "loại phí × địa điểm → cách hạch toán, định mức" cho các tuyến ngoài đường sắt (OQ-31 đã có ở sổ dự án); lái xe chọn loại phí ở cấp nào (cấp 3?) — liên quan: Mục 0.3 · cần: khách (Delta) trả lời — Nguồn nội bộ: `docs/_product/srs-v2-change-log.md` dòng CHG-20 — Nguồn khách: Brainstorm Điều phối E5 (nội bộ, chưa có tài liệu khách riêng)
- [ ] OQ-9: Cấp 3 "Tên dịch vụ" có phải unique không (nguồn chỉ nói unique cho tên chi phí)? — liên quan: Mục 3 FR-cost-catalog-023 · cần: PO/BA quyết — Nguồn nội bộ: `docs-input/srs-cu/lg-srs-export.md` trang 659 — Nguồn khách: Tài liệu SRS - ERP Delta 3.0 (Web) (bản 30/9/2026), UC03.12.03 Tạo đề xuất tạo mới chi phí cấp 3, trang 659
- [ ] OQ-10: Khi "Ghi nhận chi phí qua PO" = Không, hệ thống lưu "Dịch vụ liên quan tới phương tiện" là Không hay để trống? — liên quan: Mục 3 FR-cost-catalog-024 · cần: BA quyết — Nguồn nội bộ: `docs-input/srs-cu/lg-srs-export.md` trang 660 — Nguồn khách: Tài liệu SRS - ERP Delta 3.0 (Web) (bản 30/9/2026), UC03.12.03, trang 660
- [ ] OQ-11: Người huỷ đề xuất không phải người tạo thì người tạo có được thông báo không? (thông báo "đã bị huỷ" chỉ gửi người có quyền phê duyệt) — liên quan: Mục 3 FR-cost-catalog-014 · cần: PO/BA quyết — Nguồn nội bộ: `docs-input/srs-cu/lg-srs-export.md` trang 580, 600 — Nguồn khách: Tài liệu SRS - ERP Delta 3.0 (Web) (bản 30/9/2026), Thông báo & Lịch sử hoạt động Chi phí cấp 1, trang 580; UC03.10.04 Huỷ đề xuất cấp mới chi phí cấp 1, trang 600
- [ ] OQ-12: Hai người cùng phê duyệt/từ chối một đề xuất, hoặc Huỷ bấm sau khi đã phê duyệt/từ chối: hệ thống phản ứng thế nào? (Nguồn đã trả lời trường hợp huỷ trước, duyệt/từ chối sau: ưu tiên Huỷ, popup lỗi.) — liên quan: Mục 3 FR-cost-catalog-018 · cần: BA quyết — Nguồn nội bộ: `docs-input/srs-cu/lg-srs-export.md` trang 606, 609 — Nguồn khách: Tài liệu SRS - ERP Delta 3.0 (Web) (bản 30/9/2026), UC03.10.05 Phê duyệt/Từ chối đề xuất cấp mới chi phí cấp 1, trang 606, 609
- [ ] OQ-13: Tạo lại yêu cầu từ bản đã huỷ/từ chối (nguồn đã nói: cập nhật cùng bản ghi, về Chờ phê duyệt): sửa được những trường nào, giữ hay đổi người tạo, ghi lịch sử và gửi thông báo ra sao? — liên quan: Mục 3 FR-cost-catalog-020 · cần: PO/BA quyết — Nguồn nội bộ: `docs-input/srs-cu/lg-srs-export.md` trang 602, 608 — Nguồn khách: Tài liệu SRS - ERP Delta 3.0 (Web) (bản 30/9/2026), UC03.10.04 mục 3.2, trang 602; UC03.10.05 mục 3.2, trang 608
- [ ] OQ-14: Hộp thoại từ chối có câu "Vui lòng nhập lý do từ chối." nhưng ô lý do không bắt buộc — có bắt buộc nhập lý do khi từ chối không? — liên quan: Mục 5 BR-cost-catalog-011 · cần: PO/BA quyết — Nguồn nội bộ: `docs-input/srs-cu/lg-srs-export.md` trang 604–605 — Nguồn khách: Tài liệu SRS - ERP Delta 3.0 (Web) (bản 30/9/2026), UC03.10.05 mục 3.1, trang 604–605

## 2. Gaps (nguồn thiếu hẳn)

| Mục spec | Thiếu gì | Hệ quả nếu không bổ sung | Cần ai bổ sung |
|---|---|---|---|
| Ngõ cụt — Khoản mục chi phí: Đã phê duyệt | Không có sửa, ngừng dùng, xoá; sơ đồ trạng thái chung kết thúc ở Đã phê duyệt không có đường ra | Tên sai/chọn nhầm cấp cha đã duyệt không sửa được; khoản mục lỗi thời vẫn hiện trong danh sách chọn | PO/khách |
| Ngõ cụt — Khoản mục chi phí: Chờ phê duyệt | Không sửa được đề xuất đang chờ; chỉ có huỷ rồi Tạo mới yêu cầu | Nhập sai phải huỷ + tạo lại, tốn thao tác và để lại lịch sử huỷ | BA |
| Ngõ cụt — Khoản mục chi phí: Đã huỷ / Đã từ chối | Đường ra có (Xoá yêu cầu, Tạo mới yêu cầu) nhưng "Xoá yêu cầu" không có trong sơ đồ trạng thái và nguồn không nói xoá hẳn hay ẩn; chứng từ/lịch sử đã sinh phía sau (thông báo, lịch sử hoạt động) xử lý thế nào khi xoá | Mất vết kiểm soát nếu xoá hẳn; người đọc không biết lịch sử còn hay mất | BA |
| Ngõ cụt — Chi phí cấp 1/2: Đã phê duyệt có con | Khoản mục cha đã có con đã duyệt, nguồn không nói điều gì xảy ra khi cần đổi/ngừng cha | Cây khoản mục lệch không sửa được | PO |
| Vòng đời danh mục — Chi phí cấp 1 | Thiếu Sửa, Ngừng dùng; chỉ Xoá yêu cầu cho bản ghi chưa duyệt | Danh mục chỉ tăng, không dọn được | PO |
| Vòng đời danh mục — Chi phí cấp 2 | Thiếu Sửa (gồm đổi cấp cha), Ngừng dùng | Như trên | PO |
| Vòng đời danh mục — Chi phí cấp 3 | Thiếu Sửa (gồm đổi cờ PO, dịch vụ, liên quan phương tiện), Ngừng dùng; cấp 3 đã dùng ở PO (xử lý sau) mà đổi được không | Dữ liệu PO có thể mâu thuẫn danh mục | PO |
| Mục 3 FR-cost-catalog-018 | Chỉ phủ trường hợp "huỷ trước, duyệt/từ chối sau"; thiếu hai người cùng duyệt/từ chối, hoặc huỷ sau duyệt | Hành vi không xác định khi xung đột khác | BA |
| Mục 3 FR-cost-catalog-002 | Quy tắc Import (mẫu file, trùng, có qua phê duyệt không) | Có thể nhập danh mục bỏ qua kiểm soát đề xuất | BA |
| Mục 5 BR-cost-catalog-014 | Giới hạn mã (99/99/999) không có hướng xử lý khi đầy | Không tạo thêm được mã | BA |
| Mục 6 Error Matrix | Câu chữ lỗi cho trường bắt buộc để trống, cấp cha trống, trường PO trống (chỉ nói "in-line error msg") | Giao diện báo lỗi không thống nhất | BA/UX |
| Mục 3 FR-cost-catalog-006 | Tab con ở chi tiết cấp 1, 2 có nhóm/lọc theo Trạng thái dù chỉ liệt kê bản ghi đã phê duyệt (SRS Web tr.588, 621) | Bộ lọc/nhóm trạng thái vô nghĩa, giao diện thừa | BA/UX |
| Mục 3 FR-cost-catalog-019 | Danh sách có "…" ở mọi dòng (ảnh) nhưng nguồn không nói dòng Chờ phê duyệt/Đã phê duyệt hiện hành động gì sau "…" ngoài các nút trong cột Hành động (SRS Web tr.582–583, 589–590) | Không rõ hành vi ở danh sách | BA |
| Mục 3 FR-cost-catalog-011 đến FR-cost-catalog-017 | Thông báo/lịch sử cho "Xoá yêu cầu" và "Tạo mới yêu cầu" không có dòng nào | Không truy vết được việc xoá/tạo lại | BA |
| Mục 5 BR-cost-catalog-010 | Ma trận phân quyền theo vai trò (nguồn chỉ nói "được phân quyền") | Không biết ai duyệt được gì | PO |
| Mục 0.3 CHG-20 | Bảng loại phí × địa điểm → cách hạch toán, định mức cho tuyến ngoài đường sắt | Chưa đủ dữ liệu để cấu hình | Khách (Delta) |
| Mục 10 Báo cáo cố định — Danh sách khoản mục | Danh sách chỉ có Export/Import; không có báo cáo/dashboard khoản mục chi phí trong lát (Export theo Common Rules, nguồn ngoài lát) | Không có báo cáo theo cây chi phí | BA |
| Mục 10 popup Lịch sử hoạt động | Không có ảnh/mô tả layout popup Lịch sử hoạt động (nút mở có trong mô tả) | Khó dựng lại màn | BA |
| Mục 5 BR-cost-catalog-026 | Luồng PO và liên quan phương tiện ghi "(Xử lý sau)" | Chưa biết dịch vụ cấp 3 tác động PO thế nào | PO |

## 3. Conflicts (nguồn mâu thuẫn)

| Điểm | Nguồn A nói | Nguồn B nói | Ghi chú |
|---|---|---|---|
| Mã CP ở dòng Chờ phê duyệt | Mô tả: cột Mã CP "chỉ có khi ở trạng thái phê duyệt" (SRS Web tr.583, 616, 650 — UC03.10.01, UC03.11.01, UC03.12.01) | Ảnh danh sách có mã hiển thị ở dòng Chờ phê duyệt (SRS Web tr.582, 615, 649 — hình mockup UC03.10.01, UC03.11.01, UC03.12.01) | 🟡 Ảnh dùng các dạng mã khác nhau ("BG00001", "CP020101", "CP02020001") nên nhiều khả năng là dữ liệu mẫu; giữ theo mô tả, nhãn BR-cost-catalog-015 🟡 |
| Định dạng ID đã phê duyệt cấp 1 và cấp 2 | Quy tắc: cấp 1 "aa" (01–99), cấp 2 "xxaa" (SRS Web tr.609, 643 — UC03.10.05, UC03.11.05) | Ảnh chi tiết đã phê duyệt cấp 1 và cấp 2: "ID: CP02020001" (SRS Web tr.610, 644 — hình mockup mục 3.4) | Ảnh cấp 3 "ID: 0101001" khớp xxaabbb (tr.678). Theo quy tắc chữ; ảnh cấp 1, 2 là mockup lẫn dữ liệu cũ 🟡 |
| Lý do từ chối bắt buộc hay không | Bảng trường: Lý do từ chối, Bắt buộc = Không (SRS Web tr.605, 639, 673 — UC03.10.05, UC03.11.05, UC03.12.05) | Ảnh popup: "Vui lòng nhập lý do từ chối." (SRS Web tr.604, 638, 672 — hình mockup) | Không tự chọn; BR-cost-catalog-011 🟡 |
| Tạo mới là popup hay màn hình | Lưu đồ ảnh: "Hiển thị popup Tạo mới Chi phí cấp N" (SRS Web tr.591, 625, 657 — hình lưu đồ UC03.10.03, UC03.11.03, UC03.12.03) | Bảng mô tả: "Màn hình Tạo mới chi phí cấp N" (SRS Web tr.592, 626, 658 — mục 3.1); ảnh mockup là khung trượt bên phải | Mức thấp; tài liệu này dùng "form Tạo mới" |

## 4. Inferred assumptions (suy đoán cần verify)

- Các UC xem/tạo/huỷ/duyệt của ba cấp có cùng hành vi (chỉ khác trường) — validate: đối chiếu lưu đồ và mô tả từng cấp (đã làm, giống nhau) · nếu sai: tách UC theo cấp.
- "Người dùng đã tạo yêu cầu cấp mới" là người bấm Tạo mới lần gần nhất — validate: hỏi khách (OQ-13) · nếu sai: thông báo gửi nhầm người.
- Các lỗi chép nguồn (không ảnh hưởng nghiệp vụ, xử lý như nhiễu): UC03.10.02 mục 3.1 ghi "Màn hình Thông tin chi phí cấp 2" nhưng ảnh tr.586 là "Thông tin chi phí cấp 1"; UC03.10.04 mục 3.2 (tr.601–602) nhắc "cấp 2" trong UC cấp 1; tên UC03.12.03 "…chi phí CPcấp 3 cấp 2" (tr.657) trong khi tiêu đề và đường dẫn là cấp 3; mục Đã từ chối ghi "trạng thái (từ Đã huỷ về Chờ phê duyệt)" (tr.608, 642, 676) nhưng bản ghi đang Đã từ chối; toast "Phê duyệt đề xuất tạochi phí cấp N thành công" thiếu dấu cách (tr.609, 643, 677, giữ nguyên văn); ảnh nền form Tạo mới dùng mã "CP020101" và tiêu đề "Chi phí CP02 - cấp 1" (tr.592, 658) là mockup bản cũ — validate: hỏi khách khi họp · nếu sai: từng chỗ có thể là yêu cầu thật.
- Thuật ngữ cùng một trường nhưng gọi khác nhau: "Liên quan tới phương tiện" (cột danh sách tr.651) / "Dịch vụ liên quan tới phương tiện" (nhóm, lọc, form tr.649–650, 659–660) / "Liên quan đến phương tiện" (chi tiết tr.654); "Ghi nhận PO" (danh sách) / "Ghi nhận chi phí qua PO" (form, chi tiết) — validate: hỏi khách tên chuẩn · nếu sai: hai trường khác nhau.
- Biểu tượng "…" của tab con (cấp 1, 2) luôn ẩn vì tab chỉ liệt kê bản ghi đã phê duyệt; "…" ở đầu màn chi tiết là cái dùng cho Xoá yêu cầu/Tạo mới yêu cầu (ảnh tr.601, 607) — validate: đối chiếu ảnh tr.588–589, 601 · nếu sai: hành động Xoá/Tạo lại áp cho dòng con.
- Chữ "CP02" trong tên UC và màn là dấu vết bản cũ, không có nghĩa nghiệp vụ — validate: hỏi khách · nếu sai: có thể là nhóm chi phí CP02.

## 5. Ứng viên tham số (cho /srs)

| Tên đề xuất | Loại | Giá trị Delta | Dùng ở | Nguồn |
|---|---|---|---|---|
| so-cap-khoan-muc-chi-phi | con số | 3 cấp | BR-cost-catalog-001 | SRS Web tr.627, 660 — UC03.11.03, UC03.12.03 |
| dinh-dang-ma-chi-phi-cap-1 | con số | aa, 01 đến 99 | BR-cost-catalog-014 | SRS Web tr.609 — UC03.10.05 |
| dinh-dang-ma-chi-phi-cap-2 | con số | xxaa, aa 01 đến 99 | BR-cost-catalog-014 | SRS Web tr.643 — UC03.11.05 |
| dinh-dang-ma-chi-phi-cap-3 | con số | xxaabbb, bbb 001 đến 999 | BR-cost-catalog-014 | SRS Web tr.677 — UC03.12.05 |
| so-ban-ghi-moi-trang-mac-dinh | con số | 50 (theo ảnh) | NFR-cost-catalog-003 | SRS Web tr.582 — hình mockup UC03.10.01 |
| quy-trinh-phe-duyet-de-xuat-danh-muc | bật-tắt | bật (có phê duyệt) | BR-cost-catalog-002, BR-cost-catalog-009 | SRS Web tr.284 — Lưu đồ trạng thái chung |
| ly-do-tu-choi-bat-buoc | bật-tắt | tắt (không bắt buộc) | BR-cost-catalog-011 | SRS Web tr.605 — UC03.10.05 |
| cho-phep-tao-lai-yeu-cau-da-huy-tu-choi | bật-tắt | bật | FR-cost-catalog-020, BR-cost-catalog-023 | SRS Web tr.602, 608 — UC03.10.04, UC03.10.05 |
| ghi-nhan-chi-phi-qua-po | bật-tắt | bật (cấp 3 có lựa chọn) | FR-cost-catalog-023, BR-cost-catalog-007 | SRS Web tr.659 — UC03.12.03 |
| dich-vu-lien-quan-phuong-tien | bật-tắt | bật | FR-cost-catalog-024, BR-cost-catalog-008 | SRS Web tr.660 — UC03.12.03 |
| danh-sach-trang-thai-de-xuat-khoan-muc | danh sách | Chờ phê duyệt, Đã huỷ, Đã từ chối, Đã phê duyệt | FR-cost-catalog-021 | SRS Web tr.284 — Lưu đồ trạng thái chung |
| danh-sach-cach-hach-toan-chi-phi | danh sách | thu nhập chịu thuế của lái xe, chi hộ, trả hộ, chi phí vận hành | CHG-20 (Mục 0.3) | Thay đổi CHG-20 (loại phí hạch toán theo địa điểm) |
| dinh-muc-chi-phi-theo-dia-diem | con số | 150.000 đ depot đường sắt Nam Khánh; 160.000 đ Phú Lợi | CHG-20 (Mục 0.3) | Thay đổi CHG-20 (loại phí hạch toán theo địa điểm) |
| ten-dia-diem-depot-duong-sat | tên riêng | Nam Khánh, Phú Lợi | CHG-20 (Mục 0.3) | Thay đổi CHG-20 (loại phí hạch toán theo địa điểm) |

## 6. Vấn đề đội đã ghi nhận

> Chép từ [`docs/_product/legacy-issues.md`](../../_product/legacy-issues.md). Mỗi vấn đề cần quyết định trong brainstorm của feature.

| Mã | Vấn đề | Xử lý ở | Trạng thái |
|---|---|---|---|
| ISS-04 | Danh mục không ngừng dùng hay xoá được (khách tạo sai phải nhờ đội xoá); cân nhắc luồng cập nhật danh mục | brainstorm (khuôn chung ở `common-workspace`) | 🟡 khuôn đề xuất – duyệt – ngừng dùng – xoá viết ở product-catalog (18/10), chờ nâng lên common-workspace; còn các danh mục khác |
| ISS-14 | Giao diện làm lại theo design system mới | `/figma-screen` | ⬜ |
| ISS-15 | Onboarding trực tiếp hoặc hướng dẫn sử dụng gắn với từng chức năng (trừ feature đơn giản) | brainstorm (đánh dấu feature đơn giản) + `/userguide` | 🟡 account-access, product-catalog, technical-services: feature đơn giản, không cần hướng dẫn riêng (15/10); còn các feature khác |
