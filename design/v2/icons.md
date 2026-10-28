---
type: design-icons
status: draft
updated: 2026-10-26
links:
  - design/v2/foundations.md
  - design/v2/architecture.md
  - design/v2/tokens.json
  - _workspace/decisions.md
---

# Design System v2 — icon

> Kết quả vòng 3/6, chốt 17/10/2026 trên trang phỏng vấn https://claude.ai/artifact/D5KS1PPdUih9dsajBo48vU
> (tab 3 và 3b, DEC-141…156). Trên Figma: trang `DS · Foundations`, khung `Foundations / Icons` — các nhóm icon theo cách A
> (component set `icon/<tên>` nằm ngay trong ô tài liệu, nghĩa ghi dưới tên; DEC-262 thêm 53 icon; user chốt giữ cách A cho icon, 27/10).
> Kho nguồn 1694 icon ở khung `Foundations / Icons / Resources`. Bộ cũ giữ tới vòng 6 rồi xoá.

## 1. Bộ nền (DEC-141, DEC-156)

- **Lucide** cho cả web và app, bản **1.58.0** (giấy phép ISC). Bản này giữ tên đang dùng trên màn đã duyệt
  (`funnel`, `circle-question-mark`); `history`, `trash-2` vẫn có dưới dạng tên phụ.
- Không dùng SF Symbols (theo điều khoản của Apple, chỉ dùng trong app chạy trên thiết bị Apple), không trộn Material Symbols (DEC-141).
- Thiếu icon nghiệp vụ khác thì đề xuất vẽ theo cách của DEC-145 (lưới 24, nét Lucide, mục 6), duyệt bằng ảnh trước khi dùng; không mượn bộ khác.

## 2. Độ dày nét (DEC-300, thay DEC-142)

| Cỡ | 12 | 14 | 16 | 20 | 24 |
|---|---|---|---|---|---|
| Nét (2 trên khung 24, mọi icon kể cả trong chip) | 1.0 | 1.17 | 1.33 | 1.67 | 2.0 |

Code (lucide-react): `strokeWidth={2}` (mặc định Lucide) cho mọi icon; để
`absoluteStrokeWidth` mặc định (tắt) thì nét tự co theo cỡ như bảng trên.

## 3. Cỡ theo nền tảng (DEC-143)

| Token (Platform) | Web | App | Dùng cho |
|---|---|---|---|
| `icon/size/sm` | 14 | 16 | Trong nút có chữ, ô nhập, ô tìm, mũi tên tuyến, chevron |
| `icon/size/md` | 16 | 20 | Menu, hàng bảng, hàng danh sách, nút icon |
| `icon/size/lg` | 20 | 24 | Thanh tab app, icon đứng riêng cần nổi |
| `icon/size/chip` | 14 | 14 | Chip trạng thái |

Trên Figma chọn biến thể `Size` theo bảng này: biến thể không gắn được biến, nên đổi chế độ Platform của khung màn **không** tự đổi cỡ icon. Code đọc token. Cỡ 12 để dự phòng cho chỗ rất dày, chưa có token.

### 3.1 Nhấn mạnh bằng Featured icon, không phóng icon (DEC-258)

1. Không phóng icon quá 24 (app) / 20 (web): nét 2 trên khung 24 sẽ dày và thô khi phóng (Untitled UI cùng luật).
2. Cần nhấn mạnh (màn trống, màn kết quả, đầu dialog xác nhận) thì đặt icon 24 trong **Featured icon** 48: khối tròn (app,
   màn trống, màn kết quả) hoặc vuông bo 14; nền `color/status/*-bg-strong` hoặc `color/bg/muted`, icon `color/status/*-icon`
   hoặc `color/icon/primary`.
3. `Base / Featured Icon` vào danh sách L1 đợt 2 (cùng Stepper, BL-241).

## 4. Bản tô (DEC-141, DEC-144)

- Dùng bản tô (`Fill=On`) cho: **cảnh báo, lỗi cần chú ý** và **trạng thái bật, đã chọn** (yêu thích, ghim, đánh dấu).
  Chỗ khác chốt khi vẽ từng màn.
- **Tab đang chọn (app) và mục menu đang chọn (web) không dùng bản tô**: giữ icon viền, nhận ra bằng khối nền và màu icon chính (DEC-144).
- Đã có bản tô: `tractor-unit`, `semi-trailer`, `container-truck`, `container-seal`, `toll-booth`, `container-ship`, `eir`, `triangle-alert`, `circle-alert`. Bản tô cắt chi tiết thành lỗ thật, một màu,
  nên đổi màu chỉ cần đổi một token. Icon khác cần bản tô thì vẽ thêm khi có màn dùng.

## 5. Màu

Giữ như bộ cũ (`design/design.md` › Iconography), đổi tên token sang bộ mới:


- Mặc định `color/icon/primary`; icon phụ (chevron, mũi tên tuyến, icon trong ô tìm) dùng `color/icon/secondary`.
- Icon đi cùng chữ thì theo màu chữ cạnh nó; icon trong chip dùng `color/chip/{sắc}/fg`.
- Trên Figma màu nét đã gắn `color/icon/primary`; chỗ dùng gắn token khác thay vì chọn mã màu.

## 6. Icon nghiệp vụ tự vẽ (DEC-145, DEC-149…155)

| Icon | Nghĩa | Quyết định | Có bản tô |
|---|---|---|---|
| `icon/tractor-unit` | Đầu kéo | DEC-150 | có |
| `icon/semi-trailer` | Mooc | DEC-151 | có |
| `icon/container-truck` | Xe container | DEC-152 | có |
| `icon/container-seal` | Seal | DEC-149 | có |
| `icon/toll-booth` | Trạm thu phí | DEC-153 | có |
| `icon/container-ship` | Cảng | DEC-154 | có |
| `icon/eir` | Phiếu EIR | DEC-155 | có |

Lưới 24, nét 2, đầu và góc nét bo tròn, chừa ít nhất 1 quanh mép như hướng dẫn của Lucide. File SVG
(bản viền và bản tô) ở `design/v2/icons/`. Mã bản viền dưới đây để nét 2 như Lucide gốc, code giữ `strokeWidth={2}`:

```svg
tractor-unit:
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 18V7a1 1 0 0 1 1-1h4.4a1 1 0 0 1 .84.46l2.6 4.08a1 1 0 0 1 .16.54V17a1 1 0 0 1-1 1h-1"/><path d="M16 6v4h5.2"/><path d="M2 18h2"/><path d="M8 18h7"/><path d="M3 14h6"/><path d="M6 14v2"/><circle cx="6" cy="18" r="2"/><circle cx="17" cy="18" r="2"/></svg>

semi-trailer:
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 13h20"/><path d="M2 10v3"/><path d="M22 10v3"/><path d="M17 13v5"/><path d="M15.5 18h3"/><circle cx="5" cy="17" r="2"/><circle cx="10" cy="17" r="2"/></svg>

container-truck:
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="5" width="13" height="10" rx="1"/><path d="M5 8v4"/><path d="M8.5 8v4"/><path d="M12 8v4"/><path d="M15 18V9a1 1 0 0 1 1-1h2.6a1 1 0 0 1 .8.4l2.4 3.2a1 1 0 0 1 .2.6V17a1 1 0 0 1-1 1h-.5"/><path d="M17 8v3h3.6"/><path d="M2 18h2"/><path d="M8 18h8.5"/><circle cx="6" cy="18" r="2"/><circle cx="18.5" cy="18" r="2"/></svg>

container-seal:
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="2" width="7" height="5" rx="1"/><path d="M6.5 7v12"/><path d="m5.5 19 1 2 1-2"/><rect x="13" y="9" width="8" height="13" rx="2"/><path d="M17 9v2.5"/><path d="M15.5 15h3"/><path d="M15.5 18h3"/></svg>

toll-booth:
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21V9l3-3 3 3v12"/><path d="M5 12h2"/><path d="M2 21h20"/><rect x="9" y="13" width="13" height="2.5" rx="1.25"/><path d="M13 13v2.5"/><path d="M17 13v2.5"/></svg>

container-ship:
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 15h20l-2.5 5h-15z"/><rect x="4.5" y="10.5" width="4.5" height="4.5" rx=".5"/><rect x="9" y="10.5" width="4.5" height="4.5" rx=".5"/><rect x="9" y="6" width="4.5" height="4.5" rx=".5"/><path d="M16 15V8h3v7"/></svg>

eir:
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 22H6a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8l6 6v5"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M8 9h2"/><path d="M8 13h4"/><rect x="12" y="15" width="10" height="7" rx="1"/><path d="M15.5 15v7"/><path d="M18.5 15v7"/></svg>
```

## 7. Bảng nghĩa (DEC-146)

Mỗi nghĩa đúng một icon, mọi feature dùng chung. AI và người vẽ tra bảng, không tự chọn. Thêm nghĩa mới thì thêm
dòng ở đây và dòng nghĩa trong ô icon ở khung `Foundations / Icons` cùng lượt (khung "Bảng nghĩa icon" cũ không còn).

### Hành động

| Nghĩa | Icon |
|---|---|
| Lập, thêm | `icon/plus` |
| Sửa | `icon/pencil` |
| Xoá | `icon/trash-2` |
| Sao chép | `icon/copy` |
| Xuất file | `icon/upload` |
| Tải xuống | `icon/download` |
| In | `icon/printer` |
| Gửi | `icon/send` |
| Bộ lọc | `icon/list-filter` |
| Tuỳ chỉnh cột | `icon/sliders-vertical` |
| Nhóm | `icon/rows-3` |
| Lịch sử | `icon/history` |
| Giao lại | `icon/refresh-cw` |
| Theo dõi | `icon/eye` |
| Duyệt | `icon/check` |
| Gọi lái xe | `icon/phone` |
| Chụp ảnh | `icon/camera` |
| Đính kèm | `icon/paperclip` |
| Quét mã | `icon/scan-line` |
| Thêm thao tác | `icon/ellipsis` |
| Đóng, xoá chip | `icon/x` |
| Tìm | `icon/search` |
| Thông báo | `icon/bell` |
| Quay lại màn trước | `icon/arrow-left` |
| Sắp xếp cột | `icon/arrow-up-down` |
| Mở rộng | `icon/chevron-down` |
| Thu gọn | `icon/chevron-up` |
| Trang trước | `icon/chevron-left` |
| Trang sau, vào chi tiết hàng | `icon/chevron-right` |
| Mở trang ngoài | `icon/external-link` |
| Trang tổng quan | `icon/layout-dashboard` |
| Thu/mở thanh menu bên | `icon/panel-left` |
| Xem dạng danh sách | `icon/list` |
| Xem dạng cột | `icon/columns-3` |
| Đăng xuất | `icon/log-out` |
| Tách, rẽ nhánh | `icon/git-branch` |
| Trang chủ | `icon/house` |
| Mở menu | `icon/menu` |
| Tiếp theo | `icon/arrow-right` |
| Đăng nhập | `icon/log-in` |
| Xoá bộ lọc | `icon/funnel-x` |
| Bớt, giảm số lượng | `icon/minus` |
| Bắt đầu | `icon/play` |
| Cài đặt | `icon/settings` |
| Kéo để đổi thứ tự | `icon/grip` |
| Lưu | `icon/save` |
| Hoàn tác | `icon/undo-2` |
| Ghim | `icon/pin` |
| Yêu thích | `icon/star` |
| Chia sẻ | `icon/share-2` |
| Liên kết | `icon/link` |
| Lưu trữ | `icon/archive` |
| Nhập file | `icon/import` |
| Mã QR | `icon/qr-code` |
| Mã vạch | `icon/barcode` |
| Đổi mật khẩu | `icon/key-round` |
| Đổi ngôn ngữ | `icon/languages` |


### Đối tượng

| Nghĩa | Icon |
|---|---|
| Lệnh vận tải | `icon/clipboard-list` |
| Lái xe | `icon/user-round` |
| Đầu kéo | `icon/tractor-unit` · tự vẽ · có bản tô |
| Mooc | `icon/semi-trailer` · tự vẽ · có bản tô |
| Container | `icon/container` |
| Seal | `icon/container-seal` · tự vẽ · có bản tô |
| Xe container | `icon/container-truck` · tự vẽ · có bản tô |
| Chứng từ | `icon/file-text` |
| Phiếu EIR | `icon/eir` · tự vẽ · có bản tô |
| Chi phí | `icon/receipt` |
| Hành trình, tuyến | `icon/route` |
| Địa điểm | `icon/map-pin` |
| Cảng | `icon/container-ship` · tự vẽ · có bản tô |
| Kho, cơ sở | `icon/warehouse` |
| Trạm dầu | `icon/fuel` |
| Trạm thu phí | `icon/toll-booth` · tự vẽ · có bản tô |
| Lịch | `icon/calendar` |
| Thư, email | `icon/mail` |
| Báo cáo, biểu đồ | `icon/chart-column` |
| Hàng hoá | `icon/package` |
| Thêm hàng hoá | `icon/package-plus` |
| Công ty, đối tác | `icon/building` |
| Hỗ trợ, tổng đài | `icon/headset` |
| Tiền mặt, thanh toán | `icon/banknote` |
| Mua sắm, vật tư | `icon/shopping-cart` |
| Sửa chữa, bảo dưỡng | `icon/wrench` |
| Lập chứng từ | `icon/file-plus` |
| Chứng từ đã duyệt | `icon/file-check` |
| Bảng tính (Excel) | `icon/file-spreadsheet` |
| Đã kiểm tra | `icon/clipboard-check` |
| Thư mục | `icon/folder` |
| Dấu xác nhận | `icon/stamp` |
| Hoá đơn | `icon/receipt-text` |
| Xe nâng | `icon/forklift` |
| Tàu | `icon/ship` |
| Đường sắt | `icon/train-front` |
| Hàng không | `icon/plane` |
| Công tơ mét, số km | `icon/gauge` |
| Đường | `icon/road` |
| Bản đồ | `icon/map` |
| Vị trí hiện tại | `icon/locate-fixed` |
| Nhà máy, xưởng | `icon/factory` |
| Cửa hàng | `icon/store` |
| Hàng nhiều kiện | `icon/boxes` |
| Đã giao nhận | `icon/package-check` |
| Điểm dừng | `icon/waypoints` |
| Nhóm, đội | `icon/users` |
| Thêm người dùng | `icon/user-plus` |
| Giấy phép lái xe, CCCD | `icon/id-card` |
| Ví, quỹ | `icon/wallet` |
| Thẻ | `icon/credit-card` |
| Tạm ứng | `icon/hand-coins` |
| Đối soát, tính toán | `icon/calculator` |
| Ngân hàng | `icon/landmark` |
| Thuế, chiết khấu | `icon/percent` |
| Đối tác, hợp đồng | `icon/handshake` |


### Trạng thái (chip, DEC-029)

| Nghĩa | Icon |
|---|---|
| Đã lập | `icon/pencil` |
| Đã giao lái xe | `icon/truck` |
| Lái xe đã nhận | `icon/check` |
| Đang thực hiện | `icon/navigation` |
| Chờ duyệt | `icon/clock` |
| Đã duyệt | `icon/check-check` |
| Huỷ | `icon/circle-x` |
| Cảnh báo | `icon/triangle-alert` · có bản tô |
| Lỗi | `icon/circle-alert` · có bản tô |
| Thông tin | `icon/info` |
| Hoàn thành, thành công | `icon/circle-check` |
| Chưa bắt đầu, nháp | `icon/circle-dashed` |
| Tạm dừng | `icon/circle-pause` |
| Trợ giúp | `icon/circle-question-mark` |
| Không được phép, bị chặn | `icon/ban` |
| Không có kết quả tìm | `icon/search-x` |
| Mất kết nối | `icon/wifi-off` |
| Khoá, bảo mật | `icon/lock` |
| Quyền truy cập, bảo vệ | `icon/shield` |
| Chưa có dữ liệu (màn trống) | `icon/inbox` |
| Đang tải | `icon/loader-circle` |
| Đang chờ xử lý | `icon/hourglass` |
| Đang xử lý | `icon/circle-dot` |
| Đã xác minh | `icon/badge-check` |
| An toàn | `icon/shield-check` |
| Tắt thông báo | `icon/bell-off` |
| Đánh dấu | `icon/flag` |


## 8. Icon đang dùng trên màn đã duyệt

Quét trang `00 · Chung` ngày 17/10 (5 trang màn khác chưa có icon) ra 34 icon ngoài bảng nghĩa, đã đưa vào thư viện (DEC-148).
Ngày 27/10 (DEC-262) các icon này đã có nghĩa chuẩn ở mục 7, trừ hai icon đang lệch dưới đây.

Lệch cần thống nhất ở vòng 6 (khi đổi instance sang bộ mới): màn dùng `funnel` cho lọc trong khi bảng nghĩa
là `list-filter`; `pen-line` và `pencil` cùng dùng cho sửa.

## 9. Trên Figma (DEC-147)

- Mỗi icon là component set `icon/<tên>` với biến thể `Size=12 · 14 · 16 · 20 · 24`, nét đặt sẵn đúng cỡ.
  Icon có bản tô thêm `Fill=Off · On`.
- Component dùng icon mở thuộc tính đổi icon (Instance swap) và chọn Size; không resize tay, không sửa nét.
- Icon trong chip trạng thái dùng cùng nét 2 trên khung 24 như mọi icon (mục 2, DEC-300); người vẽ không sửa nét.
- Kho nguồn để chọn icon thêm: khung `Foundations / Icons / Resources` cạnh khung tài liệu trên trang `DS · Foundations` (node `6679:68629`, link ở mô tả đầu trang Foundations · Icons); chưa phân nhóm.
- Thêm icon mới: `python3 _scripts/ds-v2-icons.py figma <tên>...` tải SVG Lucide 1.58.0 và in mã dựng 5 biến thể, chạy qua `use_figma` (file, trang, khung thư viện ghi trong script); icon tự vẽ lấy SVG ở `design/v2/icons/`.

## 10. Còn mở

- Bản tô cho icon trạng thái bật (yêu thích, ghim, đánh dấu) — chưa có trong bảng nghĩa; thêm khi có màn cần.
- Màu icon ở chế độ Dark (theo DEC-116).
- Gộp `funnel` → `list-filter`, `pen-line` → `pencil` trên màn cũ ở vòng 6.
- Nét 2 cho icon trong chip: đặt trong component Chip ở vòng 4.
