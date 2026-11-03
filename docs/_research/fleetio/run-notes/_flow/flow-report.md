# Báo cáo nối flow Fleetio (đợt 2)

File Figma `[innvie] invlogis v0.3.4`, trang `Research · Fleetio`. Chưa bấm thử Present, chỉ kiểm bằng máy.

## 1. Hộp userflow tới màn (linkScreens)
Đã bật cho cả 7 frame userflow. Không có id nào không khớp. Cảnh báo "khớp nhiều frame" chỉ ở nhóm repair (1.1 issues-list, 2.1 wo-list, 2.3 wo-detail, 2.2 wo-edit), đọc lại đích đều đúng frame gốc (7218:222540, 7218:223490, 7221:227136, 7221:228404), không phải sửa tay. Nhóm parts: node `wo` đổi thành `continuation`, nhãn "Sửa chữa · Lệnh sửa chữa". Đáy 6 frame vẫn y=1900. Phụ: patch ở reminders, vehicle, saas, map, tires có đặt `subtitle: null` (phụ đề userflow bị bỏ).

## 2. Nối prototype: 106/218 đường

| Nhóm | Nối | Tổng |
|---|---|---|
| location-dispatch | 24 | 44 |
| parts-purchasing-fuel | 11 | 16 |
| reminders-inspection | 6 | 12 |
| repair | 38 | 63 |
| saas-platform | 10 | 23 |
| tires | 11 | 28 |
| vehicle | 6 | 32 |

Cách nối: đọc reaction hiện có của node, giữ nguyên hover/press, chỉ thêm ON_CLICK → NAVIGATE (transition null) bằng Plugin API chính thức (`setReactionsAsync`), không dùng `setReactions` của reqwise vì nó thay toàn bộ và làm mất hover/press. 13 đường đã có sẵn đúng đích (bỏ qua). Thêm 1 đường ngoài file: 2.3 wo-detail → 3.1 service-entry qua badge "Status Completed" 7221:227635 (7221:227663 chưa nối). Đường 1.2 issue-open → 1.13 issue-resolve-menu (nút Xử lý 7221:226461) đã có sẵn một ON_CLICK trỏ 1.3 issue-resolved; đã thay bằng 1.13 theo brief (đích cũ 7221:226558, báo để biết). Trang đầu → Báo cáo: không thấy control (menu bên bị bỏ qua), chưa nối.

### Đường chưa nối, theo lý do (số = thứ tự dòng trong gộp links-*.json, đếm từ 0 theo thứ tự nhóm location, parts, reminders, repair, saas, tires, vehicle)
- Hover/rời chuột, không phải click: 14, 15.
- Hệ thống tự chuyển hoặc kết quả sau khi lưu, không có control: 22, 30, 31, 41, 78, 85, 93, 121, 125, 204, 205.
- Nhiều control hợp lý hoặc cùng một control dẫn tới 2 đích, không đoán: 44 (Lưu nháp hay Lưu và duyệt), 45, 69 và 70 (cùng chip "Không đạt", 2 đích), 74 và 95 (issue-open: nút Xử lý/Đóng), 99, 163 và 165 (cùng nút Lưu, đích 6x4 hay mooc), 168 và 169 (cùng nút Lưu của tire-install), 186 và 190 (cùng nút "Thêm" của vehicle-detail), 188, 211, 212, 129, 131, 159.
- Khớp nhầm, bỏ: 63 ("Bỏ lọc" trùng chữ không dấu với "Bộ lọc").
- Control đã có liên kết khác ý, không ghi đè: 127 và 210 (nút "Thêm bảo hành" 7261:346491 đang trỏ 2.2 wo-edit 7221:228404, cần chủ màn xem lại).
- Không có control bấm được trên ảnh (đóng panel, đổi lại, quay lại, mở menu ẩn, nút trong hộp thoại bị cắt, kéo vẽ trên bản đồ, tab/nút tiếng Anh gốc không có trên màn): 0, 2, 7, 8, 9, 28, 29, 33, 36, 37, 38, 39, 42, 43, 49, 51, 58, 62, 64, 71, 76, 100, 104, 108, 109, 111, 114, 115, 117, 118, 119, 120, 122, 126, 135, 136, 137, 144, 147, 149, 150, 151, 153 đến 157, 173 đến 176, 178 đến 185, 187, 189, 191 đến 196, 198 đến 201, 208, 209, 213, 214, 216, 217.

### Control chọn kèm suy diễn (không chắc, nên soát)
- 5 "Xám" → mục "Thang xám" 7261:294095; 10 "Zoom xa" → nút "Thu nhỏ"; 11 "Zoom gần" → "Phóng to".
- 24 "Thêm cảnh báo" → "+ Thêm chính sách" 7261:327196; 23 "Tab lần ghi" → tab "Lượt ghi vị trí".
- 21, 35, 57, 59, 72, 101 "Mở dòng/Mở việc" → ô đầu của dòng bảng đầu tiên (chữ trong dòng, không phải node Row).
- 32 "Lưu" → nút "Gán"; 34 "Lưu" → nút "Bỏ gán"; 88 "Lưu" → "Xử lý sự cố"; 128 "Chọn xe" → "Tiếp tục".
- 46 → "Lệnh sửa chữa có sẵn"; 82 → "Tạo lệnh sửa chữa mới"; 83 → "Thêm vào Lệnh sửa chữa #104"; 91 "Xưởng ngoài" → "Nhờ xưởng sửa chữa".
- 116 "Khối bảo hành" → tiêu đề "Cơ hội bảo hành"; 130 → "Bảo hành tiêu chuẩn".
- 158 → "Khai báo cấu hình trục"; 160 → "Tôi đã biết cấu hình trục"; 161 → "Loại tài sản"; 166/167 → ô "+" đầu; 170/171 → lốp "LF"/"1LO"; 177 "Đảo" → "Đảo lốp".
- 206 "Chọn định kỳ" → "Chi phí định kỳ".
- Nhiều nút lưu có 2 bản (đầu và cuối form): chỉ nối bản đầu tiên tìm thấy.
- Nút bị tắt trong ảnh: không gặp trường hợp cần ghi chú.

## 3. Flow bắt đầu (38 flow tên theo tác vụ + 7 flow Userflow giữ nguyên)
Đã đặt lại toàn bộ danh sách (`replace`), danh sách cũ có 70 mục trùng tên (24 flow "Xe · Trang xe", 8 flow "Sửa chữa · Hoàn thành"...). Mỗi frame chỉ được là điểm bắt đầu của 1 flow, nên các dòng Mục 3 cùng màn đầu được gộp tên:
- Sửa chữa: Báo và xử lý (1.1) · Xử lý bằng ghi chú, đóng và ghi lịch sử (1.2, gộp 3 dòng) · Thực hiện lệnh (2.1) · Hoàn thành và sao chép (2.3, gộp 2 dòng) · Mở lại (2.11) · Bảo hành (6.7) · Cấu hình (7.1, frame tên 4.1 maintenance-settings).
- Nhắc và kiểm tra: Nhắc và tuân thủ (1.1, gộp) · Bộ lịch (1.2) · Gia hạn (1.3) · Biểu mẫu (2.1) · Kiểm tra (2.5) · Lốp (2.9, vì 2.6 chưa vẽ) · Lỗi (2.3).
- Phụ tùng và dầu: Mua (2.3 po-new) · Nhận, trả, đóng và sửa sau nhận (2.1, gộp 3) · Tồn, chỉnh và chuyển (1.1, gộp) · Kiểm kê (1.6) · Dầu (3.2).
- Xe (tự đặt theo cụm số): Trang xe 1.1 · Gán xe 2.1 · Số đồng hồ 3.1 · Số đọc lốp 4.1 · Chi phí 5.1 · Thay xe 6.1.
- Nền tảng: Trang đầu 1.1 · Báo cáo 2.1 · Tự động hoá 3.3 · Tập bản ghi 4.2. Cụm 5.x (liên hệ, thu hồi, đặt xe, tài liệu) không flow vì không có liên kết nào tới.
- Bản đồ: Bản đồ đội xe 1.1 · Địa điểm 2.4 · Việc 3.1 · Tự động hoá vùng 4.1.
- Lốp: Khai báo trục 1.1 · Lắp lốp 2.1 · Đảo lốp 3.1 · Tháo lốp 4.1 · Số đọc lốp 5.2.
Không còn tên "Flow N".

## 4. Kiểm bằng máy (309 frame trong 16 section)
- Reaction trỏ tới node không tồn tại: 0.
- Hover/press: nút Chú giải 7226:263878 đã bị mất hover/press ở lần thử đầu của lượt này (do `setReactions` của reqwise), đã dựng lại. Quét sau cùng thấy 88 instance có ON_CLICK mà thiếu hover/press (Button 76, _Tab chip 6, Radio label 5, Checkbox label 1; gồm cả nút lần trước làm mất); đã thêm ON_HOVER/ON_PRESS CHANGE_TO tới biến thể State=Hover/Pressed cùng bộ (SMART_ANIMATE, 0,3 giây; thời lượng gốc không đọc lại được). Badge "Status Completed" không có biến thể State, bỏ qua.
- Frame không có đường vào lẫn ra (bỏ qua frame "Ảnh gốc Fleetio", biến thể, userflow, frame là điểm bắt đầu flow): 7261:354030 report-issues, 7265:361946 ai-analyst-issues, 7265:372278 automation-self-trigger-runs, 7265:377978 contact-no-access, 7265:379764 recalls-list, 7270:382171 motor-pool-reservations, 7270:382767 documents-empty, 7226:265244 place-new, 7226:256601 vendors, 7221:225010 service-tasks, 7261:359286 tire-readings-filter-warning, 7265:360608 tire-readings-boundary, 7261:287973 fleet-map-nearby-hover-dashed, 7261:282839 assignment-week, 7261:292133 assignment-overlap, 7261:325107 meter-history-conflict, 7261:337747 replacement-params, 7261:298885 se-from-wo, 7261:306779 se-deleted-not-found, 7261:356511 và 7261:357102 inspection-tire (2.7, 2.8), 7261:358755 item-failure-needs-action, 7265:372934 parts-bulk-manage, 7270:381577 po-make-adjustment, 7271:385928 fuel-entry-odometer-backdate-error, 7261:317426 job-assign-overlap-error, 7261:344549, 7261:341285, 7261:350727, 7261:348989 (job 3.8 đến 3.11), 7265:364137, 7265:364668 (inspection 5.1, 5.2).
- Chưa bấm Present thử.

---

# Lượt 2 (thay các mục trên khi mâu thuẫn)

## Tổng mới: 118/218
| Nhóm | Nối | Tổng |
|---|---|---|
| location-dispatch | 24 | 44 |
| parts-purchasing-fuel | 12 | 16 |
| reminders-inspection | 8 | 12 |
| repair | 40 | 63 |
| saas-platform | 10 | 23 |
| tires | 15 | 28 |
| vehicle | 9 | 32 |

Cách làm như lượt 1 (`use_figma`, đọc reaction rồi thêm ON_CLICK, transition null, giữ hover/press). Không còn reaction trỏ node không tồn tại (quét lại: 0). 182 reaction NAVIGATE trên 309 frame.

## Đã xử lý trong lượt 2
- 44 (po-new, Lưu nháp / Lưu và duyệt, cả bản đầu và cuối form): 4 nút đã có sẵn liên kết tới po-detail, tính là nối.
- 69 chip "Không đạt" 7226:265207 → 2.4 item-failures (Happy path Lỗi: 2.3 → 2.4). 70 (cùng chip, đích 2.13): nhánh, chưa nối vì Figma chỉ có 1 đích mỗi control.
- 99 nút "Mở lại" 7221:227019 trên 1.3 issue-resolved → 1.11 issue-reopen-locked (Happy path Hoàn thành: 1.3 → 1.11); đích cũ 1.2 là đường 94, nay thành nhánh, chưa nối.
- 127 và 210: "Thêm bảo hành" 7261:346491 bỏ đích wo-edit, nối 6.3 warranty-new-vehicles. Hai đường trùng from/to nên cả hai tính nối.
- 163 nút Lưu cấu hình trục 7261:318740 → 1.6 tire-management-6x4; 165 (đích mooc, cùng nút): nhánh, chưa nối.
- 168 nút Lưu tire-install 7261:327189 → 2.2 tire-management-installed (đích xuất hiện trước trong links); 169 (đích mooc): nhánh, chưa nối.
- 129 "Mẫu phạm vi bảo hành" (6.1) → 6.4; 211 "Loại phạm vi bảo hành" (6.3) → 6.4 (Mục 3: 6.4 hoặc 6.5, chọn 6.4); 212 (→ 6.5, cùng control): nhánh, chưa nối.
- 159 "Tiếp tục" 7261:311643 (1.2 axle-setup-step1) → 1.3 axle-setup-axle-type.
- 63 "Bỏ lọc" → nút "Xoá tất cả" 7265:367193 → 1.1 reminders-list. 184 "Lọc Tread Depth Health" → cột "Sức khoẻ độ sâu gai" 7261:352519 → 5.3 (suy diễn nhãn).
- 190 và 186: nút "Thêm" 7224:249241 của vehicle-detail đã trỏ sẵn tới 3.1 meter-history (tính 190 đã nối). Trên 1.1 không có menu mục con "Lịch sử số đồng hồ"; 186 (→ 1.2 vehicle-more-actions) giữ chưa nối, vì cùng nút đã có liên kết khác ý, không ghi đè. Cần chủ màn chỉ ra nút "Thêm" nào là More Actions (còn nút "Thêm" thứ hai 7224:249303).
- 188 "Overview" → cost-of-ownership: giữ chưa nối (tab "Tổng quan" 7224:249263 không rõ dẫn tới 1.3).

## Đường vẫn chưa nối (100)
0, 2, 7, 8, 9, 14, 15, 22, 28, 29, 30, 31, 33, 36, 37, 38, 39, 41, 42, 43, 45, 49, 51, 58, 62, 64, 70, 71, 74, 76, 78, 85, 93, 94, 95, 100, 104, 108, 109, 111, 114, 115, 117, 118, 119, 120, 121, 122, 125, 126, 131, 135, 136, 137, 144, 147, 149, 150, 151, 153, 154, 155, 156, 157, 165, 169, 173 đến 176, 178 đến 183, 185, 186 đến 189, 191 đến 196, 198 đến 201, 204, 205, 208, 209, 212, 213, 214, 216, 217.
Lý do còn lại:
- Nhánh, một control chỉ có 1 đích: 70, 74, 94, 165, 169, 212.
- Control không có trên màn (nút trong hộp thoại bị cắt, panel đóng, menu ẩn, kéo vẽ, tab tiếng Anh gốc): phần lớn các số còn lại.
- Hệ thống tự chuyển hoặc kết quả sau lưu: 22, 30, 31, 41, 78, 85, 93, 121, 125, 204, 205.
- Hover (giữ chưa nối vì lượt này chỉ dùng click): 14, 15.
- 135 Trang đầu → Báo cáo: sidebar của frame dashboard không có mục "Báo cáo" (13 mục menu: Trang đầu, Bản đồ, Phương tiện, Kiểm tra, Dịch vụ, Lệnh, Lịch sử dịch vụ, Đầu việc, Sự cố, Nhắc việc, Phụ tùng và kho, Cài đặt). 153 đến 157 cũng vậy (không có mục riêng).
- 45, 49, 51, 95, 99-nhánh...: control không rõ hoặc không có.

## Frame cô lập còn lại (30, đã loại frame là điểm bắt đầu flow)
Có đường trong links nhưng control không có trên màn: report-issues (136), ai-analyst-issues (137), automation-self-trigger-runs (147), contact-no-access (153), recalls-list (155), motor-pool-reservations (156), documents-empty (157), tire-readings-boundary (185), fleet-map-nearby-hover-dashed (14, 15 hover), assignment-week (198 đến 201), assignment-overlap (204, 205), meter-history-conflict (195, 196), replacement-params (209), se-from-wo (120, 121), se-deleted-not-found (125), item-failure-needs-action (70, 71), po-make-adjustment (49), job-assign-overlap-error (30, 31), job-assignment-history (36), jobs-board-geofence-chip (38), job-history-auto-geofence (39), inspection-submission-location (43).
Userflow không có đường tới (không có dòng nào trong links): place-new (2.1), vendors (2.2), service-tasks (5.1), inspection-tire-axle-error (2.7), inspection-tire-remark-required (2.8), fuel-entry-odometer-backdate-error (3.4), job-completed (3.9), inspection-pretrip-simulated (5.2).

## Lượt 3: nhóm "Menu bổ sung" và nối theo menu
Ngày 2026-11-03. Chưa bấm thử Present, chỉ kiểm bằng máy và chụp màn.

**Đã thêm.** Frame `Menu bổ sung` (con của frame màn, ABSOLUTE, x16 y659, rộng 207, cao 226, gap 2) trên 171 frame `<số> · web · <slug>` của 16 section (kể cả `wo-list · Calendar` và `· Resource Scheduler`; bỏ các biến thể 1280, 1024, 393 và nhóm "Ảnh gốc"). 6 mục theo thứ tự: Báo cáo, Việc, Địa điểm, Liên hệ, Nhà cung cấp, Dầu; mỗi mục là instance `_Nav item` (Type=Link, Open=False, State Default hoặc Current) cùng component với Sidebar, icon Lucide của kho icon (chart-column, briefcase, map-pin, contact, store, fuel). Vùng trống của Nav từ y643 đến y898 trong Sidebar, đủ chỗ cho cả 6 mục (kết thúc y885, không đè Footer items và thẻ tài khoản), nên không phải giảm còn 3 mục. Không sửa component chính, không detach Sidebar. Thứ tự lớp: chèn ngay sau Sidebar, dưới Main, Lớp phủ, hộp thoại, toast; hộp thoại vẫn che menu (đã chụp issue-close-dialog).

**Mục đang chọn.** Màn thuộc mục nào thì mục đó State Current và mọi ô Current trong Sidebar chuyển Default: reports, report-issues, ai-analyst-issues (Báo cáo); jobs, jobs-board, job-* (Việc); place-new, place-*, places-list-data (Địa điểm); contact-no-access (Liên hệ); vendors (Nhà cung cấp); fuel-* (Dầu). Màn khác giữ nguyên Sidebar.

**Nối.** Mỗi mục menu ON_CLICK NAVIGATE (transition null), nối thêm vào reaction đang có bằng `setReactionsAsync`. Đích: Báo cáo 2.1 reports (7224:247155); Việc 3.2 jobs-board (7261:292905); Địa điểm 2.4 places-list-data (7261:315685); Liên hệ 5.1 contact-no-access (7265:377978); Nhà cung cấp 2.2 vendors (7226:256601); Dầu 3.2 fuel-list (7226:265743). Mục trỏ chính màn đang đứng thì bỏ qua (không tự nối). Tra bằng id nên không nhầm 3.2 jobs-board với 3.2 meter-reject-backdate. Cả 6 đích là màn mới thiết kế, không phải màn hiện trạng khác hẳn.

**Duyệt lại đường thiếu control.** 135 Trang đầu → Báo cáo và 153 Trang đầu → Liên hệ: nối nhờ menu (mọi màn, kể cả dashboard). 43 inspection-submission-location → map: nối qua ô "Bản đồ đội xe" có sẵn của Sidebar trên màn đó (control thật, đích đúng 1.1 map). Còn lại không có control thật nên giữ nguyên, không thêm control: 154 (Xe → vehicle-more-actions, không có mục), 155 Thu hồi hãng, 156 Đặt xe, 157 Tài liệu (menu bổ sung không có mục này), 136, 137, 147, 185, 198 đến 201, 204, 205, 195, 196, 209, 120, 121, 125, 70, 71, 49, 30, 31, 36, 38, 39 (quét chữ nhãn trên màn nguồn, không có control tương ứng; 14, 15 là hover).

**11 đường hệ thống tự chuyển** (22, 30, 31, 41, 78, 85, 93, 121, 125, 204, 205) bỏ theo quyết định của user, không nối và không tính vào mục tiêu.

**Kết quả.** Nối 126/218 (trước đợt này 106, lượt 2 tính cả đường có sẵn; kiểm lại bằng máy thì 125 trước khi nối 43). Không có reaction trỏ tới node không tồn tại (kiểm 171 frame). Đường còn chưa nối (92): 0, 2, 7, 8, 9, 14, 15, 22, 29, 30, 31, 33, 36, 38, 39, 41, 42, 45, 49, 51, 58, 62, 64, 70, 71, 74, 76, 78, 85, 93, 94, 95, 100, 104, 108, 109, 111, 114, 115, 117, 118, 119, 120, 121, 122, 125, 131, 136, 137, 144, 147, 149, 150, 151, 154, 155, 156, 157, 165, 169, 173, 174, 175, 176, 178, 179, 180, 181, 182, 183, 185, 186, 187, 188, 189, 191, 193, 195, 196, 198, 199, 200, 201, 204, 205, 208, 209, 212, 213, 214, 216, 217.
Nhóm lý do còn lại: (a) hệ thống tự chuyển, 11 đường, bỏ theo user; (b) hover, 14 và 15; (c) nhánh một control nhiều đích: 70, 74, 94, 165, 169, 212; (d) control không có trên màn (hộp thoại bị cắt, panel đóng, menu ẩn, tab, kéo vẽ, màn nguồn không có nút tương ứng): phần còn lại.

**Frame cô lập (không có đường vào, không phải điểm bắt đầu flow): 58.** 4.1 faults, 5.1 service-tasks, 2.1 place-new, 2.4 tire-management-trailer-12-spare, 3.3 tire-rotate-name-required, 5.4 tire-readings-boundary, 5.5 tire-activity, 1.4 issue-close-dialog, 1.10 issue-draft-ready, 1.12 issue-menu-locked-tooltip, 2.12 wo-reopen-confirm, 2.13 wo-make-copy, 2.14 wo-complete-errors, 2.15 wo-100x-after-save, 2.17 wo-warranty-opportunity, 3.2 se-from-wo, 3.3 se-deleted-not-found, 6.2 warranty-form, 6.6 warranty-maintenance-codes, 1.2 fleet-map-nearby-list-2-vehicles, 1.5 fleet-map-nearby-hover-dashed, 2.6 place-detail-with-entries, 3.4 job-assign-modal, 3.5 job-assign-overlap-error, 3.6 job-unassign-modal, 3.8 job-assignment-history, 3.9 job-completed, 3.10 jobs-board-geofence-chip, 3.11 job-history-auto-geofence, 4.4 vehicle-automation-comments, 5.1 inspection-submission-location, 5.2 inspection-pretrip-simulated, 1.2 vehicle-more-actions, 1.3 vehicle-cost-of-ownership, 2.3 assignment-week, 2.4 assignment-overlap, 2.5 assignment-edit, 3.2 meter-reject-backdate, 3.3 meter-reject-forward, 3.4 meter-history-conflict, 6.2 replacement-params, 2.2 report-issues, 2.3 ai-analyst-issues, 3.7 automation-self-trigger-runs, 3.8 automation-archived, 3.9 automation-comment-result, 5.3 recalls-list, 5.4 motor-pool-reservations, 5.5 documents-empty, 2.4 po-receive-dialog, 2.7 po-make-adjustment, 3.3 fuel-history-capacity-alert, 3.4 fuel-entry-odometer-backdate-error, 1.6 reminder-after-work-order, 1.7 reminder-list-compliance, 2.7 inspection-tire-axle-error, 2.8 inspection-tire-remark-required, 2.13 item-failure-needs-action. (contact-no-access đã hết cô lập nhờ menu.) Con số 58 tính theo "không có đường vào nào"; lượt 2 đếm 30 theo "có dòng trong links mà thiếu control". Một số frame trong 58 (vd menu bay, hộp thoại con) là đích của đường hover hoặc hệ thống tự chuyển.
