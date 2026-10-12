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
   Code chạy đầy đủ: xem lượt figma_write 07/10 (đã chạy OK, ảnh đã soát). Màn còn lại vẽ tiếp theo lab-repair-detail.html.
   Lượt 3 (09/10) — 9 màn còn lại, hàng y=3379 (cùng cha với bản A), nhân từ bản A nghiệm thu rồi sửa:
     1 tab-chung 5457:92664 (x240, thêm Ghi chú của xưởng + Thẻ kỹ thuật viên) · 2 tien-trinh-mo 5457:92801 (x713)
     · 9 da-nghiem-thu 5457:92950 (x1186, toast) · 10 tu-choi-nghiem-thu 5457:93076 (x1659, dải lý do)
     · 3 lap-vao 5457:93202 (x2132) · 4 thay-ra 5457:93390 (x2605) · 5 dich-vu 5457:93562 (x3078)
     · 6 sheet-serial 5457:93711 (x3551) · 11 sheet-lich-su 5457:93874 (x4024).
   Lưu ý: đổi màu node đã gắn biến phải dùng applyVariable (modify fill:"$…" không thay biến cũ);
     node chèn vào frame auto-layout cần counterAxisSizingMode:"AUTO" (mặc định cao 100). layoutAudit 9/9 sạch.
   Lượt 4 (09/10) — DỰNG LẠI theo component. Lượt 3 dời vào Section "Bản cũ · chi tiết lệnh lượt 3 — không dùng, chờ xoá" 5457:94060 (tên lớp có tiền tố [cũ]).
   Text style Lab/H1 H2 H3 Title đã đổi sang Manrope (28/34 · 24/30 · 17/22 · 15/20, Bold/SemiBold, chữ -2%).
   Component (Section 5457:94301 "Lab · Component chi tiết lệnh sửa chữa"):
     Tab 2 mục 5457:94071 (Đang chọn=Chung|Chi tiết) · Thanh đầu 5457:94072 · Tiến trình gọn 5457:94104 · Đầu sheet 5457:94243
     · Chân màn 5457:94141 · Tiêu đề 5457:94103 (Trạng thái=Chờ nghiệm thu|Đã nghiệm thu|Từ chối nghiệm thu)
     · Tiêu đề nhóm 5457:94156 (Tính tiền=Có|Không) · Khối kết quả 5457:94140 (Kết quả=Đã nghiệm thu|Từ chối nghiệm thu)
     · Dòng lịch sử 5457:94300 (Có lý do=Không|Có) · Dòng hàng 5457:94242 (Loại=Lắp vào|Thay ra|Dịch vụ × Mở=Không|Có; Dịch vụ chỉ Không)
     · Sheet xác nhận 5457:94281 (Loại=Xác nhận|Từ chối (có lý do)) — CMP-03 Mobile phương án B.
     Ghi đè chữ khi dùng: overrides theo tên lớp ("Tên", "Mã và số lượng", "Giá trị", "Tên nhóm", "Tiền nhóm", "Tiêu đề sheet", "Hành động", "Thời điểm").
   Màn (Section 5457:95350 "Chi tiết lệnh sửa chữa · app lái xe · v2", hàng y=3300, cách 473):
     1 tab-chung · cho-nghiem-thu 5457:94302 (cao theo nội dung) · 2 sheet-tien-trinh 5457:94569 · 3 tab-chi-tiet 5457:94410 (cao theo nội dung)
     · 4 sheet-nghiem-thu 5457:94728 · 5 sheet-tu-choi-nghiem-thu 5457:94850 · 6 da-nghiem-thu 5457:95111 · 7 tu-choi-nghiem-thu 5457:95230
     · 8 sheet-lich-su 5457:94976.
   Bẫy thêm: cột "Mốc" trong Dòng lịch sử phải width cố định + primaryAxisSizingMode FIXED, nếu không đường nối giữ cao 100 mặc định và tràn.
   layoutAudit 8/8 sạch (trừ icon hệ thống thanh trạng thái, và nền bị khung cắt dưới sheet — đúng chủ ý).
   09/10 sau góp ý: Dòng lịch sử làm lại thành 5457:95404 (Hành động=Tạo lệnh|Chốt lệnh|Cập nhật chốt lệnh|Nghiệm thu|Từ chối nghiệm thu,
     icon tròn 28 thay chấm; việc của xưởng nền well, nghiệm thu nền done-bg, từ chối nền bad-bg + khối lý do). Bộ cũ 5457:94300 đã xoá; màn 8 đã thay.
   Bảng phương án Thẻ thông tin sửa chữa 5457:95425 (cấp trang, x14400 y3300): A lưới ô · B dòng có icon · C thẻ xưởng + mốc thời gian · D câu tóm tắt. */
