/* Chi tiết lệnh sửa chữa (app lái xe) — từ lab-repair-detail.html. 07/10.
   Lượt 1: 1 artboard "5.1-mob · chi-tiet-lenh · sheet-tu-choi-nghiem-thu" 5453:44227, rel (80, 3359) trong Section 5446:15413.
   Helper: như figma-form-v2.js (P/K/ic/T/TW/H/V/sp/gap/kẻ/S/G/R/BD/circ/icc/ib/statusBar/homeInd/screen) +:
     btn(label,"pri"|"sec"|"bad") — sec = nền well + viền rule; bad = nền $lab/st/bad.
     card(name,ch,gap) — nền card, viền rule, bo lab/r/card, đệm lab/sp/16.
   Thân màn (tab Chung, Chờ nghiệm thu): Thanh đầu (back + lịch sử, nút tròn viền) · Tiêu đề (LSC H1 + pill accept, phụ Small)
     · Thẻ tiến trình đang đóng (nhãn bước + thanh 4 đoạn, đoạn 4 = ink-3) · Tab Chung/Chi tiết (segmented)
     · Thẻ phương tiện (thẻ con xe + chip odo nền card cao 32, mô tả sự cố, link BCSC) · Thẻ thông tin sửa chữa (kv + kẻ).
   Chân màn: nền card, Tổng giá trị (Lab/Title) + Từ chối (sec) / Nghiệm thu (pri).
   Sheet từ chối: góc trên 28, icon tròn 52 bad-bg, tiêu đề Lab/H2, giải thích Meta, ô lý do (well, bo inner, đếm 38/500), Huỷ bỏ (sec) / Từ chối (bad).
   Hậu kỳ: Chân màn + Sheet → absolute, y = 852 - h; Nền mờ (0,0); Home indicator (129.5, 839).
   Lượt 2 (07/10) — trong Section "Duyệt" 5453:44355, hàng y=1630:
     A từ chối 5453:44227 (x240) · A nghiệm thu 5453:44356 (x713, clone A từ chối: icon check nền #e8f5ec, nút Xác nhận primary, bỏ ô lý do)
     · B nghiệm thu 5453:44486 (x1186) · B từ chối 5453:44649 (x1659).
   Bản B = kiểu sheet-chon-xe 5446:20103: sheet nổi x8 w377 bo 36 + bóng, đáy cách 8; Đầu sheet (Lab/H3 + nút X 38 nền well);
     1 nút chính full ngang, huỷ bằng X. B nghiệm thu: khối Tóm tắt (well, 4 cặp Lệnh/Phương tiện/Xưởng/Tổng) + dòng lưu ý alert.
     B từ chối: giải thích Meta + ô lý do (clone từ A) + nút "Gửi từ chối" nền lab/st/bad.
   Code chạy đầy đủ: xem lượt figma_write 07/10 (đã chạy OK, ảnh đã soát). Màn còn lại vẽ tiếp theo lab-repair-detail.html. */
