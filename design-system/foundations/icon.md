---
type: design-icons
status: approved
updated: 2026-11-03
links:
  - design-system/foundations/README.md
  - design-system/architecture.md
  - design-system/tokens.json
  - _workspace/decisions.md
---

# Foundations · Icon

> Một phần của [[design-system/foundations/README.md|Foundations]] (DEC-317). Tóm tắt mục 11 cũ ngay dưới; chi tiết ở các mục sau.

## 11. Icon (DEC-141…156)

Luật icon ở `icon.md (file này)`: Lucide 1.58.0 cho web và app; nét 2 trên khung 24, riêng icon cỡ 16 trở xuống nét 2,25, kể cả icon trong chip (DEC-329 ic01,
thay một phần DEC-300, bỏ ngoại lệ Badge của DEC-309); một bộ cỡ cho web và app `icon/size/xs · sm · md · lg · chip` 12 · 14 · 16 · 20 · 14 (DEC-329 ic02, thay DEC-143); bản tô chỉ cho cảnh báo, lỗi và trạng thái bật;
tab đang chọn (app) và mục menu đang chọn (web) giữ icon viền; 7 icon nghiệp vụ tự vẽ, chỉ bản viền; bảng icon theo nghĩa chia 6 nhóm như trang Figma.

**Cấu trúc lớp trên Figma (DEC-202):** mỗi icon mỗi cỡ là **một lớp nét tên `Vector`** (bản tô thêm một lớp `Hình tô`).
Component tô màu icon bằng cách đè màu lớp `Vector`; nhờ cùng một lớp cùng tên nên đổi icon qua thuộc tính vẫn giữ màu. Icon mới
phải gộp nét thành một lớp trước khi đưa vào thư viện. Lớp `Hình tô` không theo màu khi đổi icon: trong component dùng bản viền,
cần bản tô thì gán màu lớp tô trên instance.


> Kết quả vòng 3/6, chốt 17/10/2026 trên trang phỏng vấn https://claude.ai/artifact/D5KS1PPdUih9dsajBo48vU
> (tab 3 và 3b, DEC-141…156). Trên Figma: trang `DS · Foundations`, khung `Foundations / Icons` — các nhóm icon theo cách A
> (component set `icon/<tên>` nằm ngay trong ô tài liệu, nghĩa ghi dưới tên; DEC-262 thêm 53 icon; user chốt giữ cách A cho icon, 27/10).
> Kho nguồn 1694 icon ở khung `Foundations / Icons / Resources`. Bộ cũ giữ tới vòng 6 rồi xoá.

## 1. Bộ nền (DEC-141, DEC-156)

- **Lucide** cho cả web và app, bản **1.58.0** (giấy phép ISC). Bản này giữ tên đang dùng trên màn đã duyệt
  (`funnel`, `circle-question-mark`); `history`, `trash-2` vẫn có dưới dạng tên phụ.
- Không dùng SF Symbols (theo điều khoản của Apple, chỉ dùng trong app chạy trên thiết bị Apple), không trộn Material Symbols (DEC-141).
- Thiếu icon nghiệp vụ khác thì đề xuất vẽ theo cách của DEC-145 (lưới 24, nét Lucide, mục 6), duyệt bằng ảnh trước khi dùng; không mượn bộ khác.

## 2. Độ dày nét (DEC-329 ic01, thay một phần DEC-300)

| Cỡ | 12 | 14 | 16 | 20 | 24 |
|---|---|---|---|---|---|
| Nét trên khung 24 | 2.25 | 2.25 | 2.25 | 2 | 2 |
| Nét thật (px) | 1.13 | 1.31 | 1.5 | 1.67 | 2.0 |

Code (lucide-react): `strokeWidth={size <= 16 ? 2.25 : 2}`; để `absoluteStrokeWidth` mặc định (tắt) thì nét tự co theo cỡ như bảng trên.

Không còn ngoại lệ: icon trong Badge cỡ 14 dùng nét 2,25 như mọi icon cỡ này. Nét 2.5 của DEC-309 đã bỏ.

## 3. Cỡ (DEC-329 ic02…ic05, thay DEC-143, DEC-306)

Một bộ cho web và app, không đổi theo Platform.

| Token | Trỏ thang | Cỡ | Dùng cho |
|---|---|---|---|
| `icon/size/xs` | `size/lg` | 12 | Xoá trong tag, dấu tick, dấu ngăn, mũi tên bước số, nút đổi ảnh Avatar nhỏ (ic03) |
| `icon/size/sm` | `size/14` | 14 | Nút SM, ô nhập, ô tìm, mũi tên tuyến, chevron |
| `icon/size/chip` | `size/14` | 14 | Icon trong Badge (DEC-310) |
| `icon/size/md` | `size/xl` | 16 | Nút MD, menu, hàng bảng, hàng danh sách, nút icon |
| `icon/size/lg` | `size/2xl` | 20 | Nút LG, thanh tab app, icon đứng riêng cần nổi, Upload Compact, lớp Thử lại trên ảnh |

- **Vì sao một bộ:** lý do tách của DEC-143 là chữ đọc app to hơn web, DEC-322 đã đưa chữ app về 14/20 nên lý do đó hết hiệu lực. User chọn gộp về 14 · 16 · 20: icon app nhỏ đi 2–4 so với trước, thanh tab còn 20.
- **Bỏ cỡ 18:** `icon/size/ml` đã xoá (ic04, thay DEC-306); chỗ từng dùng 18 chuyển sang 20.
- **Bậc 14 lệch thang Untitled, do user chọn (ic05):** thang `size/*` theo Untitled không có 14, nên thêm primitive `space/14` và `size/14` riêng cho icon. Không thêm bậc 18 vì 18 đã bỏ. Token cỡ icon đều trỏ thang, không còn số trần.
- Trên Figma chọn biến thể `Size` theo bảng này; biến thể không gắn được biến. Code đọc token.

### Ghép cỡ icon với cỡ chữ (DEC-329 ic06)

**Luật: icon không cao hơn dòng chữ cạnh nó**, để icon không đẩy hàng cao lên. Canh giữa icon theo dòng chữ.

| Chữ | Cỡ / dòng | Icon đi cùng | Ghi chú |
|---|---|---|---|
| `type/hint`, `type/chip-sm` | 12 / 18 | `xs` 12, `sm` 14 | `md` 16 vẫn không đội dòng, dùng khi là icon chính của hàng |
| `type/caption` | 12 / 16 | `xs` 12, `sm` 14 | Dòng 16 nên `md` 16 là trần, `lg` 20 sẽ đội dòng |
| `type/body` | 14 / 20 | `sm` 14, `md` 16 | `lg` 20 bằng đúng dòng, chỉ dùng cho nút lớn và icon đứng đầu hàng |
| `type/title-3` | 18 / 28 | `md` 16, `lg` 20 | Đầu khối, đầu sheet |

### 3.1 Nhấn mạnh bằng Featured icon, không phóng icon (DEC-258, DEC-329 ic10, ic11)

1. Không phóng icon quá `icon/size/lg` 20 ngoài các cỡ Featured trong [icon-sets.md](icon-sets.md): nét sẽ dày và thô khi phóng (Untitled UI cùng luật).
2. Cần nhấn mạnh (màn trống, màn kết quả, đầu dialog xác nhận, ô tải lên) thì đặt icon trong **Featured icon**.

Bảng cỡ, kiểu, tương phản của Featured icon: [icon-sets.md](icon-sets.md) (DEC-332).

## 4. Bản tô (DEC-141, DEC-144, DEC-329 ic07, ic08)

- Dùng bản tô (`Fill=On`) cho: **cảnh báo, lỗi cần chú ý** và **trạng thái bật, đã chọn** (yêu thích, ghim, đánh dấu).
- **Tab đang chọn (app) và mục menu đang chọn (web) không dùng bản tô**: giữ icon viền, nhận ra bằng khối nền và màu icon chính (DEC-144).
- Cảnh báo, lỗi: file `triangle-alert-fill.svg`, `circle-alert-fill.svg` trong `design-system/icons/`. Bản tô cắt chi tiết thành lỗ thật, một màu, nên đổi màu chỉ cần đổi một token.
- Yêu thích, ghim, đánh dấu: `star`, `pin`, `flag` bật bằng **fill trên chính path Lucide**, không vẽ hình mới và không thêm file. Code: `fill="currentColor"` trên icon Lucide. Không chỉ đổi màu, vì người mù màu và ảnh đen trắng không phân biệt được bật với tắt.
- Icon nghiệp vụ tự vẽ không có bản tô (DEC-262, đã xoá 7 file ở DEC-329 ic07).

## 5. Màu (DEC-320, DEC-329 ic12)

- Mặc định `color/fg/secondary`.
- **Icon phụ mang nghĩa** (chevron ô chọn, mũi tên tuyến, icon trong ô tìm, Help, nút xoá) dùng `color/fg/tertiary` (Sáng 7,81:1, Tối 6,97:1 trên `color/bg/primary`).
- `color/fg/quaternary` (2,52:1 và 2,25:1, dưới ngưỡng 3:1) **chỉ cho icon trang trí và disabled**: dấu ngăn, chấm ngăn, tay nắm kéo, khoá ô chỉ đọc.
- Icon đi cùng chữ thì theo màu chữ cạnh nó; icon trong chip dùng màu chữ chip `color/utility/{sắc}/*` (DEC-320), xem `design-system/components/base/badge.md`.
- Trên Figma màu nét đã gắn `color/fg/secondary`; chỗ dùng gắn token khác thay vì chọn mã màu.

## 6. Icon nghiệp vụ tự vẽ (DEC-145, DEC-149…155)

| Icon | Nghĩa | Quyết định |
|---|---|---|
| `icon/tractor-unit` | Đầu kéo | DEC-150 |
| `icon/semi-trailer` | Mooc | DEC-151 |
| `icon/container-truck` | Xe container | DEC-152 |
| `icon/container-seal` | Seal | DEC-149 |
| `icon/toll-booth` | Trạm thu phí | DEC-153 |
| `icon/container-ship` | Cảng | DEC-154 |
| `icon/eir` | Phiếu EIR | DEC-155 |

Lưới 24, nét 2, đầu và góc nét bo tròn, chừa ít nhất 1 quanh mép như hướng dẫn của Lucide; code đặt nét theo cỡ như mục 2. File SVG
ở `design-system/icons/`, chỉ bản viền.

`tractor-unit` và `container-truck` vẽ lại bớt chi tiết (DEC-329 ic09, 8 và 10 phần tử còn 5, như `truck` của Lucide) để đọc được ở cỡ 14, đã render kiểm ở 14, 16, 24. Hai file này lưu nét 2.25 vì vẽ cho cỡ nhỏ; ở cỡ 20, 24 code vẫn đặt 2.


```svg
tractor-unit:
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.25" stroke-linecap="round" stroke-linejoin="round"><path d="M13 18V6a1 1 0 0 1 1-1h3.52a1 1 0 0 1 .78.38l3.48 4.35a1 1 0 0 1 .22.62V17a1 1 0 0 1-1 1h-1"/><path d="M15 18H8"/><path d="M13 13H2v4a1 1 0 0 0 1 1h1"/><circle cx="6" cy="18" r="2"/><circle cx="17" cy="18" r="2"/></svg>

semi-trailer:
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 13h20"/><path d="M2 10v3"/><path d="M22 10v3"/><path d="M17 13v5"/><path d="M15.5 18h3"/><circle cx="5" cy="17" r="2"/><circle cx="10" cy="17" r="2"/></svg>

container-truck:
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.25" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="12" height="9" rx="1"/><path d="M8 3v9"/><path d="M8 18h6v-8h4.52a1 1 0 0 1 .78.38l2.48 3.1a1 1 0 0 1 .22.62V17a1 1 0 0 1-1 1h-1"/><circle cx="6" cy="18" r="2"/><circle cx="17" cy="18" r="2"/></svg>

container-seal:
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="2" width="7" height="5" rx="1"/><path d="M6.5 7v12"/><path d="m5.5 19 1 2 1-2"/><rect x="13" y="9" width="8" height="13" rx="2"/><path d="M17 9v2.5"/><path d="M15.5 15h3"/><path d="M15.5 18h3"/></svg>

toll-booth:
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21V9l3-3 3 3v12"/><path d="M5 12h2"/><path d="M2 21h20"/><rect x="9" y="13" width="13" height="2.5" rx="1.25"/><path d="M13 13v2.5"/><path d="M17 13v2.5"/></svg>

container-ship:
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 15h20l-2.5 5h-15z"/><rect x="4.5" y="10.5" width="4.5" height="4.5" rx=".5"/><rect x="9" y="10.5" width="4.5" height="4.5" rx=".5"/><rect x="9" y="6" width="4.5" height="4.5" rx=".5"/><path d="M16 15V8h3v7"/></svg>

eir:
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 22H6a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8l6 6v5"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M8 9h2"/><path d="M8 13h4"/><rect x="12" y="15" width="10" height="7" rx="1"/><path d="M15.5 15v7"/><path d="M18.5 15v7"/></svg>
```

## 7. Bảng nghĩa (DEC-146, DEC-329 ic13, ic14)

Mỗi nghĩa đúng một icon, mọi feature dùng chung. AI và người vẽ tra bảng, không tự chọn. Thêm nghĩa mới thì thêm
dòng ở đây và dòng nghĩa trong ô icon ở khung `Foundations / Icons` cùng lượt. Sáu nhóm và thứ tự theo đúng khung `Bộ icon theo nhóm` trên Figma (DEC-262, đọc ngày 02/11).


### Điều hướng và bố cục

| Nghĩa | Icon |
|---|---|
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
| Nhóm | `icon/rows-3` |
| Đăng xuất | `icon/log-out` |
| Tách, rẽ nhánh | `icon/git-branch` |
| Trang chủ | `icon/house` |
| Mở menu | `icon/menu` |
| Tiếp theo | `icon/arrow-right` |
| Đăng nhập | `icon/log-in` |

### Hành động

| Nghĩa | Icon |
|---|---|
| Lập, thêm | `icon/plus` |
| Sửa | `icon/pencil` |
| Xoá | `icon/trash-2` |
| Sao chép | `icon/copy` |
| Tải lên | `icon/upload` |
| Xuất file | `icon/file-output` |
| Tải xuống | `icon/download` |
| In | `icon/printer` |
| Gửi | `icon/send` |
| Bộ lọc | `icon/list-filter` |
| Xoá bộ lọc | `icon/funnel-x` |
| Tuỳ chỉnh cột | `icon/sliders-vertical` |
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
| Bớt, giảm số lượng | `icon/minus` |
| Bắt đầu | `icon/play` |
| Cài đặt | `icon/settings` |
| Kéo để đổi thứ tự | `icon/grip` |
| Lưu | `icon/save` |
| Hoàn tác | `icon/undo-2` |
| Ghim | `icon/pin` · có bản tô (fill trên path Lucide) |
| Yêu thích | `icon/star` · có bản tô (fill trên path Lucide) |
| Chia sẻ | `icon/share-2` |
| Liên kết | `icon/link` |
| Lưu trữ | `icon/archive` |
| Nhập file | `icon/import` |
| Mã QR | `icon/qr-code` |
| Mã vạch | `icon/barcode` |
| Đổi mật khẩu | `icon/key-round` |
| Đổi ngôn ngữ | `icon/languages` |

### Trạng thái và phản hồi

| Nghĩa | Icon |
|---|---|
| Đã duyệt | `icon/check-check` |
| Hoàn thành, thành công | `icon/circle-check` |
| Huỷ | `icon/circle-x` |
| Chưa bắt đầu, nháp | `icon/circle-dashed` |
| Đã lập | `icon/file-pen` |
| Lái xe đã nhận | `icon/user-check` |
| Tạm dừng | `icon/circle-pause` |
| Chờ duyệt | `icon/clock` |
| Thông tin | `icon/info` |
| Cảnh báo | `icon/triangle-alert` · có bản tô |
| Lỗi | `icon/circle-alert` · có bản tô |
| Trợ giúp | `icon/circle-question-mark` |
| Không được phép, bị chặn | `icon/ban` |
| Không có kết quả tìm | `icon/search-x` |
| Mất kết nối | `icon/wifi-off` |
| Khoá, bảo mật | `icon/lock` |
| Quyền truy cập, bảo vệ | `icon/shield` |
| Thông báo | `icon/bell` |
| Chưa có dữ liệu (màn trống) | `icon/inbox` |
| Đang tải | `icon/loader-circle` |
| Đang chờ xử lý | `icon/hourglass` |
| Đang xử lý | `icon/circle-dot` |
| Đã xác minh | `icon/badge-check` |
| An toàn | `icon/shield-check` |
| Tắt thông báo | `icon/bell-off` |
| Đánh dấu | `icon/flag` · có bản tô (fill trên path Lucide) |

### Tệp và chứng từ

| Nghĩa | Icon |
|---|---|
| Chứng từ | `icon/file-text` |
| Phiếu EIR | `icon/eir` · tự vẽ |
| Lệnh vận tải | `icon/clipboard-list` |
| Chi phí | `icon/receipt` |
| Thư, email | `icon/mail` |
| Báo cáo, biểu đồ | `icon/chart-column` |
| Hàng hoá | `icon/package` |
| Thêm hàng hoá | `icon/package-plus` |
| Lập chứng từ | `icon/file-plus` |
| Chứng từ đã duyệt | `icon/file-check` |
| Bảng tính (Excel) | `icon/file-spreadsheet` |
| Đã kiểm tra | `icon/clipboard-check` |
| Thư mục | `icon/folder` |
| Dấu xác nhận | `icon/stamp` |
| Hoá đơn | `icon/receipt-text` |

### Vận tải và địa điểm

| Nghĩa | Icon |
|---|---|
| Đã giao lái xe | `icon/truck` |
| Đầu kéo | `icon/tractor-unit` · tự vẽ |
| Mooc | `icon/semi-trailer` · tự vẽ |
| Xe container | `icon/container-truck` · tự vẽ |
| Hành trình, tuyến | `icon/route` |
| Đang thực hiện | `icon/navigation` |
| Địa điểm | `icon/map-pin` |
| Container | `icon/container` |
| Seal | `icon/container-seal` · tự vẽ |
| Cảng | `icon/container-ship` · tự vẽ |
| Kho, cơ sở | `icon/warehouse` |
| Trạm dầu | `icon/fuel` |
| Trạm thu phí | `icon/toll-booth` · tự vẽ |
| Công ty | `icon/building` |
| Lịch | `icon/calendar` |
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

### Người, tài chính và khác

| Nghĩa | Icon |
|---|---|
| Lái xe | `icon/user-round` |
| Hỗ trợ, tổng đài | `icon/headset` |
| Tiền mặt, thanh toán | `icon/banknote` |
| Mua sắm, vật tư | `icon/shopping-cart` |
| Sửa chữa, bảo dưỡng | `icon/wrench` |
| Nhóm, đội | `icon/users` |
| Thêm người dùng | `icon/user-plus` |
| Giấy phép lái xe, CCCD | `icon/id-card` |
| Ví, quỹ | `icon/wallet` |
| Thẻ | `icon/credit-card` |
| Tạm ứng | `icon/hand-coins` |
| Đối soát, tính toán | `icon/calculator` |
| Ngân hàng | `icon/landmark` |
| Thuế, chiết khấu | `icon/percent` |
| Đối tác | `icon/handshake` |


Icon `pen-line`, `funnel` còn trong khung Figma nhưng không có nghĩa: đó là hai icon lệch ở mục 8, chờ gộp ở vòng 6.

## 8. Icon đang dùng trên màn đã duyệt

Quét trang `00 · Chung` ngày 17/10 (5 trang màn khác chưa có icon) ra 34 icon ngoài bảng nghĩa, đã đưa vào thư viện (DEC-148).
Ngày 27/10 (DEC-262) các icon này đã có nghĩa chuẩn ở mục 7, trừ hai icon đang lệch dưới đây.

Lệch cần thống nhất ở vòng 6 (khi đổi instance sang bộ mới): màn dùng `funnel` cho lọc trong khi bảng nghĩa
là `list-filter`; `pen-line` và `pencil` cùng dùng cho sửa; nút Tuỳ chỉnh cột dùng `columns-3` thay `sliders-vertical`.
`/figma-audit` kiểm icon ngoài bảng nghĩa (DEC-329 ic15), màn cũ sửa khi dựng lại ở vòng 6.

## 9. Trên Figma (DEC-147)

- Mỗi icon là component set `icon/<tên>` với biến thể `Size=12 · 14 · 16 · 20 · 24`, nét đặt sẵn đúng cỡ theo mục 2. Không có Size=18 (DEC-329 ic04).
  Icon có bản tô thêm `Fill=Off · On`: `triangle-alert`, `circle-alert`, `star`, `pin`, `flag`.
- Component dùng icon mở thuộc tính đổi icon (Instance swap) và chọn Size; không resize tay, không sửa nét.
- Icon trong chip trạng thái dùng cùng nét như mọi icon cùng cỡ (mục 2); người vẽ không sửa nét.
- Kho nguồn để chọn icon thêm: khung `Foundations / Icons / Resources` cạnh khung tài liệu trên trang `DS · Foundations` (node `6679:68629`, link ở mô tả đầu trang Foundations · Icons); chưa phân nhóm.
- Thêm icon mới: `python3 _scripts/ds-v2-icons.py figma <tên>...` tải SVG Lucide 1.58.0 và in mã dựng 5 biến thể, chạy qua `use_figma` (file, trang, khung thư viện ghi trong script); icon tự vẽ lấy SVG ở `design-system/icons/`.

## 10. Còn mở

- Gộp `funnel` → `list-filter`, `pen-line` → `pencil`, `columns-3` → `sliders-vertical` trên màn cũ ở vòng 6.
- Figma chưa có biến thể icon cỡ 28: `Featured icon` Size 56 phóng từ icon `Size=24`, nét 2,33.

Đã đóng ở DEC-329: bản tô trạng thái bật (ic08); màu icon ở chế độ Tối, `color/fg/*` đã có giá trị Tối; nét icon trong chip (ic01).

## 12. Bộ phụ: Payment và Social (DEC-329 ic16)

Chuyển sang [icon-sets.md](icon-sets.md) (DEC-332).

## 13. Nhãn và trình đọc màn hình (DEC-329 ic17)

1. Mặc định icon đi kèm nhãn chữ.
2. Nút chỉ có icon phải có tên truy cập (`aria-label`) và `Tooltip` (`design-system/components/base/tooltip.md`).
3. Icon trang trí đặt `aria-hidden="true"`.
