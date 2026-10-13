---
type: figma-audit-report
feature: cross-process-flow
figma: "[innvie] invlogis v0.3" · trang "00 · Chung"
updated: 2026-10-13
---

# Figma audit — cross-process-flow (lớp 1, máy đo)

Màn đã đọc: 41 · bỏ qua (tên không theo quy ước): 0

**Cao 1 · Trung 20 · Thấp 14**

## Mức Cao

| Mã | Sai lệch | Ở đâu |
|---|---|---|
| K4 | `icon/list` cỡ 13px — cho phép [12, 14, 16, 18, 20, 24] | `1.6 · web · debt-step` › Icon công nợ (I5587:123905;5578:110271) |

## Mức Trung

| Mã | Sai lệch | Ở đâu |
|---|---|---|
| K2 | [web] Khối "Đầu trang" khác nhau giữa các màn — bo None gap 16 pad (0, 0, 0, 0): 18 màn · bo None gap 8 pad (0, 0, 0, 0): 9 màn | 1.1 · web · record-detail, 1.1 · web · record-detail · Load error, 1.1 · web · record-detail · Loading, 1.2 · web · process-diagram, 1.2 · web · process-diagram · Condition tooltip, 1.2 · web · process-diagram · History load error, 1.2 · web · process-diagram · Load error, 1.2 · web · process-diagra |
| K2 | [web] Khối "Tiêu đề" khác nhau giữa các màn — bo None gap 0 pad (0, 0, 0, 0): 14 màn · bo None gap 2 pad (0, 0, 0, 0): 9 màn | 1.2 · web · process-diagram, 1.2 · web · process-diagram · Condition tooltip, 1.2 · web · process-diagram · History load error, 1.2 · web · process-diagram · Load error, 1.2 · web · process-diagram · Loading, 1.2 · web · process-diagram · Update banner, 1.3 · web · step-not-created, 1.4 · web · bran |
| K2 | [web] Khối "Hàng tiêu đề" khác nhau giữa các màn — bo None gap 12 pad (0, 0, 0, 0): 14 màn · bo None gap 0 pad (0, 0, 0, 0): 8 màn | 1.2 · web · process-diagram, 1.2 · web · process-diagram · Condition tooltip, 1.2 · web · process-diagram · History load error, 1.2 · web · process-diagram · Load error, 1.2 · web · process-diagram · Loading, 1.2 · web · process-diagram · Update banner, 1.3 · web · step-not-created, 1.4 · web · bran |
| K2 | [web] Khối "Vùng trạng thái" khác nhau giữa các màn — bo None gap 0 pad (0, 0, 64, 64): 4 màn · bo None gap 0 pad (0, 0, 120, 0): 1 màn | 2.1 · web · process-list · Empty, 2.1 · web · process-list · Load error, 2.1 · web · process-list · No filter results, 2.1 · web · process-list · No permission, 2.1 · web · process-list · No search results |
| K3 | Nút "mở màn hình chi tiết" khác biến thể/cỡ giữa các màn — Primary/MD: 1.2 · web · process-diagram, 1.2 · web · process-diagram · Condition tooltip, 1.2 · web · process-diagram · History load error, 1.2 · web · process-diagram · Update banner, 1.7 · web · step-previous-records, 1.8 · web · open-denied, 1.9 · web · record-deleted · Primary/LG: 4.1 · mob · step-sheet |  |
| K3 | Nút "đóng" khác biến thể/cỡ giữa các màn — Primary/MD: 1.8 · web · open-denied, 3.2 · web · step-already-requested, 3.4 · web · has-child-step · Secondary/MD: 1.9 · web · record-deleted |  |
| K4 | Vector tự vẽ, không phải instance `icon/<tên>` (bỏ qua nếu là logo/hình minh hoạ) | `1.2 · web · process-diagram` › Đường bg→lsc (5587:119622) |
| K4 | Icon mặc định của thư viện `icon/circle-dashed` đang hiện — xác nhận là có chủ ý (vd trạng thái Chưa tạo) | `1.2 · web · process-diagram` › Icon trạng thái (I5587:119638;5578:112350;5578:109820) |
| K4 | `icon/search` màu nét không gắn token | `2.1 · web · process-list · Empty` › Icon (I5600:144992;84:148824;82:153) |
| K4 | Nút "Tuỳ chỉnh cột" dùng `icon/columns-3`, design.md quy định `icon/sliders-vertical` | `2.1 · web · process-list · Empty` › Icon (I5600:144994;86:194844) |
| K4 | 52 icon 12px để nét 1, cần ≈ 0.9 — 2 loại: `icon/arrow-up-down`, `icon/x` | `2.1 · web · process-list · Loading` › Sort Icon (I5600:137740;2389:14354); `2.1 · web · process-list · Loading` › Sort Icon (I5600:137741;2389:14354); `2.1 · web · process-list · Loading` › Sort Icon (I5600:137742;2389:14354) … |
| K4 | 62 icon 12px để nét 1.2, cần ≈ 0.9 — 3 loại: `icon/check`, `icon/git-branch`, `icon/map-pin` | `1.2 · web · process-diagram` › Icon (I5587:119632;5584:117129;5578:109858); `1.2 · web · process-diagram` › Icon (I5587:119635;5578:110102;5578:109860); `1.2 · web · process-diagram` › Icon (I5587:119636;5578:110102;5578:109860) … |
| K4 | 244 icon 14px để nét 1.2, cần ≈ 1.05 — 12 loại: `icon/check`, `icon/check-check`, `icon/chevron-down`, `icon/chevron-right`, `icon/circle-dashed`, `icon/clock`, `icon/git-branch`, `icon/list` … | `1.1 · web · record-detail` › icon/map-pin (I5596:130329;5596:129426;5596:129271); `1.1 · web · record-detail` › icon/chevron-down (I5596:130329;5596:129426;5596:129273); `1.1 · web · record-detail` › icon/chevron-right (I5596:130452;5596:129540) … |
| K4 | 4 icon 16px để nét 1.33, cần ≈ 1.2 — 1 loại: `icon/search` | `2.1 · web · process-list · Empty` › Icon (I5600:144992;84:148824;82:153); `2.1 · web · process-list · No search results` › Icon (I5600:147413;84:148824;82:153); `2.1 · web · process-list · No filter results` › Icon (I5600:149834;84:148824;82:153) … |
| K4 | 106 icon 18px để nét 1.2, cần ≈ 1.35 — 11 loại: `icon/banknote`, `icon/circle-question-mark`, `icon/git-branch`, `icon/package`, `icon/package-plus`, `icon/receipt`, `icon/search`, `icon/shield` … | `1.2 · web · process-diagram` › icon/search (I5587:119631;5578:110095); `1.2 · web · process-diagram` › Icon nghiệp vụ (I5587:119632;5578:110125); `1.2 · web · process-diagram` › Icon nghiệp vụ (I5587:119633;5578:110095) … |
| K4 | 30 icon 20px để nét 1.2, cần ≈ 1.5 — 3 loại: `icon/chevron-right`, `icon/git-branch`, `icon/wifi-off` | `1.1 · web · record-detail` › icon/git-branch (I5587:118196;5570:106914); `1.2 · web · process-diagram` › icon/git-branch (I5587:119306;5570:106914); `1.2 · web · process-diagram · Loading` › icon/git-branch (I5587:120046;5570:106914) … |
| K4 | 4 icon 20px để nét 1.67, cần ≈ 1.5 — 2 loại: `icon/circle-x`, `icon/info` | `1.1 · web · record-detail · Load error` › Icon (I5587:118910;5570:106971;86:308486;82:156); `1.2 · web · process-diagram · Update banner` › Icon (I5587:122288;86:286681;82:156); `1.1 · mob · record-detail · Load error` › Icon (I5600:160683;5371:3073;5600:160696;5570:106998;86:308486;82:156) … |
| K4 | 5 icon 24px để nét 1.2, cần ≈ 1.8 — 3 loại: `icon/funnel-x`, `icon/lock`, `icon/search-x` | `1.5 · web · step-no-permission` › icon/lock (I5587:123171;5578:110811); `2.1 · web · process-list · No search results` › icon/search-x (I5600:157129;2282:17800;5600:157803); `2.1 · web · process-list · No filter results` › icon/funnel-x (I5600:157164;2282:17800;5600:157809) … |
| K4 | 1 icon 24px để nét 2, cần ≈ 1.8 — 1 loại: `icon/inbox` | `2.1 · web · process-list · Empty` › Icon (I5600:157107;2282:17768;82:159) |
| K5 | Khung tự dựng tên "BottomSheet" trùng tên component đang dùng — nghi tách rời hoặc dựng lại | `1.2 · mob · process-diagram · Update banner` › BottomSheet (5600:162176); `1.2 · mob · process-diagram` › BottomSheet (5600:161278); `1.3 · mob · step-not-created` › BottomSheet (5600:163099) |

## Mức Thấp

| Mã | Sai lệch | Ở đâu |
|---|---|---|
| K1 | khoảng cách `8` không gắn token — 196 chỗ / 34 màn | `1.1 · web · record-detail` › Tiêu đề và meta (5587:118098); `1.1 · web · record-detail` › Vùng hành động (5587:118102); `1.1 · web · record-detail` › Rail phải (5587:118508); `1.1 · web · record-detail · Loading` › Tiêu đề và meta (5587:118536) … |
| K1 | khoảng cách `16` không gắn token — 101 chỗ / 29 màn | `1.1 · web · record-detail` › Nội dung (5587:117898); `1.1 · web · record-detail` › Trang chi tiết (5587:118096); `1.1 · web · record-detail` › Đầu trang (5587:118097); `1.1 · web · record-detail` › Thân trang (5587:118506) … |
| K1 | padding `(12, 12, 0, 0)` không gắn token — 80 chỗ / 1 màn | `2.1 · web · process-list · Loading` › Ô · Mã quy trình (5600:157265); `2.1 · web · process-list · Loading` › Ô · Luồng (5600:157267); `2.1 · web · process-list · Loading` › Ô · Bản ghi gốc (5600:157269); `2.1 · web · process-list · Loading` › Ô · Phương tiện / khách hàng (5600:157271) … |
| K1 | khoảng cách `12` không gắn token — 53 chỗ / 26 màn | `1.1 · web · record-detail` › Hàng meta (5587:118100); `1.1 · web · record-detail · Loading` › Hàng meta (5587:118538); `1.1 · web · record-detail · Load error` › Hàng meta (5587:118902); `1.2 · web · process-diagram` › Hàng meta (5587:119298) … |
| K1 | padding `(16, 16, 16, 16)` không gắn token — 50 chỗ / 19 màn | `1.1 · web · record-detail` › Cột chính (5587:118507); `1.1 · web · record-detail` › Rail phải (5587:118508); `1.1 · web · record-detail · Loading` › Cột chính (5587:118549); `1.1 · web · record-detail · Loading` › Rail phải (5587:118551) … |
| K1 | padding `(24, 24, 24, 24)` không gắn token — 29 chỗ / 29 màn | `1.1 · web · record-detail` › Nội dung (5587:117898); `1.1 · web · record-detail · Loading` › Nội dung (5587:118532); `1.1 · web · record-detail · Load error` › Nội dung (5587:118896); `1.2 · web · process-diagram` › Nội dung (5587:119292) … |
| K1 | khoảng cách `2` không gắn token — 16 chỗ / 16 màn | `2.1 · web · process-list · Loading` › Tiêu đề (5600:137723); `2.1 · web · process-list` › Tiêu đề (5600:132888); `2.1 · web · process-list · Update banner` › Tiêu đề (5600:140144); `2.2 · web · list-process-diagram` › Tiêu đề (5600:142565) … |
| K1 | padding `(16, 8, 4, 8)` không gắn token — 7 chỗ / 7 màn | `1.2 · mob · process-diagram` › Header (5600:161517); `1.2 · mob · process-diagram · Update banner` › Header (5600:162180); `4.1 · mob · step-sheet` › Header (5600:162607); `1.3 · mob · step-not-created` › Header (5600:163103) … |
| K1 | padding `(16, 16, 4, 42)` không gắn token — 7 chỗ / 7 màn | `1.2 · mob · process-diagram` › Thân (5600:161522); `1.2 · mob · process-diagram · Update banner` › Thân (5600:162185); `4.1 · mob · step-sheet` › Thân (5600:162612); `1.3 · mob · step-not-created` › Thân (5600:163108) … |
| K1 | padding `(0, 0, 64, 64)` không gắn token — 4 chỗ / 4 màn | `2.1 · web · process-list · Empty` › Vùng trạng thái (5600:157106); `2.1 · web · process-list · No search results` › Vùng trạng thái (5600:157128); `2.1 · web · process-list · No filter results` › Vùng trạng thái (5600:157163); `2.1 · web · process-list · Load error` › Vùng trạng thái (5600:157209) |
| K1 | padding `(0, 0, 120, 0)` không gắn token — 1 chỗ / 1 màn | `2.1 · web · process-list · No permission` › Vùng trạng thái (5600:157234) |
| K6 | Flow view-process: `PXK-0433` chỉ có ở 1 màn, các màn khác dùng `PXK-0410`, `PXK-0415` — soát dữ liệu mẫu có cùng một bản ghi không | 1.5 · mob · step-no-permission |
| K6 | Flow view-process: `YC-BT-0029` chỉ có ở 1 màn, các màn khác dùng `YC-BT-0034` — soát dữ liệu mẫu có cùng một bản ghi không | 1.7 · web · step-previous-records |
| K6 | Flow search-process: `PXK-9999` chỉ có ở 1 màn, các màn khác dùng `PXK-0410`, `PXK-0415` — soát dữ liệu mẫu có cùng một bản ghi không | 2.1 · web · process-list · No search results |

## Icon đang dùng

| Icon | Số màn |
|---|---|
| `icon/chevron-right` | 34 |
| `icon/wrench` | 32 |
| `icon/search` | 32 |
| `icon/git-branch` | 31 |
| `icon/map-pin` | 31 |
| `icon/history` | 30 |
| `icon/x` | 29 |
| `icon/package` | 28 |
| `icon/chevron-down` | 27 |
| `icon/play` | 26 |
| `icon/bell` | 24 |
| `icon/check-check` | 22 |
| `icon/shield` | 21 |
| `icon/chart-column` | 20 |
| `icon/plus` | 19 |
| `icon/pen-line` | 13 |
| `icon/file-text` | 12 |
| `icon/circle-dashed` | 12 |
| `icon/check` | 12 |
| `icon/minus` | 12 |
| `icon/chevron-left` | 12 |
| `icon/inbox` | 11 |
| `icon/package-plus` | 11 |
| `icon/banknote` | 11 |
| `icon/panel-left` | 10 |
| `icon/layout-dashboard` | 10 |
| `icon/external-link` | 9 |
| `icon/circle-check` | 8 |
| `icon/circle-question-mark` | 8 |
| `icon/triangle-alert` | 7 |
| `icon/shopping-cart` | 7 |
| `icon/truck` | 7 |
| `icon/receipt` | 7 |
| `icon/arrow-up-down` | 5 |
| `icon/wifi-off` | 4 |
| `icon/download` | 4 |
| `icon/list-filter` | 4 |
| `icon/columns-3` | 4 |
| `icon/lock` | 3 |
| `icon/circle-x` | 2 |
| `icon/info` | 2 |
| `icon/list` | 2 |
| `icon/clock` | 2 |
| `icon/search-x` | 1 |
| `icon/funnel-x` | 1 |

Máy KHÔNG kiểm: nghiệp vụ/nhãn đúng sai, thẩm mỹ, thứ bậc thị giác — xem lớp 2 (reviewer).
