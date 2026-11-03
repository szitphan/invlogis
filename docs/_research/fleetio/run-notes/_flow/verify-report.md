# Kiểm tra độc lập trang Figma `Research · Fleetio` (chỉ đọc)

File `FifpyOMpZk9OP8qyNzbRVJ`, trang 7214:221223, ngày 2026-11-03. Phạm vi: 16 section, 171 frame màn cấp một (bỏ `Ảnh gốc Fleetio…` và hậu tố ` · 1280/1024/393`). Reaction ON_CLICK + NAVIGATE của mọi node con (kể cả trong instance), đích tra lên frame cấp một.

## 1-2. Đường nối thật so với 218 dòng links
- Cặp (nguồn, đích) duy nhất trong Figma: 1193. Trong đó 125 cặp có trong links.
- Links có 218 dòng, 216 cặp duy nhất (2 dòng trùng). Số dòng links đã nối: **126/218** (125 cặp duy nhất).

| Nhóm | Đã nối / dòng links |
|---|---|
| repair | 41/63 |
| reminders-inspection | 8/12 |
| parts-purchasing-fuel | 12/16 |
| vehicle | 11/32 |
| saas-platform | 12/23 |
| location-dispatch | 27/44 |
| tires | 15/28 |
| Tổng | 126/218 |

- Cặp có trong Figma, không có trong links: 1068 = 1014 cặp menu (6 đích menu: reports, jobs-board, places-list-data, contact-no-access, vendors, fuel-list) + 54 cặp khác (menu bổ sung: Calendar/Scheduler, chuyển sang meter-history từ 17 frame lốp + 3 frame xe khác, quay về issue-resolved/wo-detail/wo-edit, v.v.).
- 92 dòng links chưa nối (danh sách đầy đủ lấy bằng chạy lại script; vd vehicle-detail>vehicle-more-actions, vehicle-detail>cost-of-ownership, jobs-board>job-assign/unassign/history/geofence-chip, dashboard>recalls/motor-pool/documents/more-actions, wo-detail>make-copy/100x, issue-open>close-dialog/menu-locked-tooltip).

## 3. Reaction trỏ node không tồn tại
0. NAVIGATE thiếu destinationId: 0.

## 4. Đường vào/ra (không tính điểm bắt đầu flow)
- Tính mọi reaction (kể cả menu): 0 frame không vào lẫn ra; 58 frame không có đường vào.
- Không tính 6 đích menu, không tính tự trỏ: **31 frame không vào không ra**: 5.1 service-tasks, 2.2 vendors, 2.1 place-new, 5.4 tire-readings-boundary, 3.2 se-from-wo, 3.3 se-deleted-not-found, 1.5 fleet-map-nearby-hover-dashed, 3.4 job-assign-modal, 3.5 job-assign-overlap-error, 3.6 job-unassign-modal, 3.8 job-assignment-history, 3.9 job-completed, 3.10 jobs-board-geofence-chip, 3.11 job-history-auto-geofence, 5.2 inspection-pretrip-simulated, 2.3 assignment-week, 2.4 assignment-overlap, 3.4 meter-history-conflict, 6.2 replacement-params, 2.2 report-issues, 2.3 ai-analyst-issues, 3.7 automation-self-trigger-runs, 5.1 contact-no-access, 5.3 recalls-list, 5.4 motor-pool-reservations, 5.5 documents-empty, 2.7 po-make-adjustment, 3.4 fuel-entry-odometer-backdate-error, 2.7 inspection-tire-axle-error, 2.8 inspection-tire-remark-required, 2.13 item-failure-needs-action. (2.2 vendors và 5.1 contact-no-access vẫn vào được qua menu.)
- Có đường ra, không có đường vào (không tính menu): 30 frame.
- Theo links (không đo Figma): 10 frame không xuất hiện trong links (service-tasks, wo-list Calendar, wo-list Resource Scheduler, vendors, place-new, job-completed, inspection-pretrip-simulated, fuel-entry-odometer-backdate-error, inspection-tire-axle-error, inspection-tire-remark-required).

## 5. Flow bắt đầu
45 điểm bắt đầu: 38 trỏ vào frame màn, 7 trỏ vào frame `Userflow · Fleetio · …`. Không trùng tên, không có tên dạng `Flow N`.

## 6. Vị trí
- Mỗi frame màn có nhóm `Ảnh gốc Fleetio · <slug>` cùng slug: 171/171 (2 frame Calendar, Resource Scheduler dùng slug `wo-calendar`, `wo-scheduler`). Không có nhóm trùng.
- Cùng x, cách frame 0 đến 80, rộng 1920: 171/171 đạt, 0 lệch. Lưu ý kiểu node: 7 section cũ dùng GROUP, 9 section mới dùng FRAME.
- Đè nhau cấp một cùng section: **1 cặp**, section `Sửa chữa · Hoàn thành, phiếu, bảo hành`: frame `6.5 · web · warranty-new-standard` (y 3080) đè `Ảnh gốc Fleetio · wo-make-copy` (x 4080, y 2181, cao 1051, tới y 3232).
- Section đè section: 0.

## 7. Bỏ qua (không đo).

## 8. Chữ `Nhập nội dung`, `Label`, `Lorem`
Quét TEXT của 171 frame màn (so khớp phân biệt hoa thường), bỏ node ẩn và node trong Sidebar/Header: 0 node hiển thị.
