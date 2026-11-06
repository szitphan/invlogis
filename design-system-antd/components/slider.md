---
type: design-system-component
status: draft
updated: 2026-11-07
links:
  - design-system-antd/foundations/foundations.md
  - design-system-antd/token-mapping.md
  - design-system-antd/components/switch.md
  - design-system-antd/components/tooltip.md
  - design-system-antd/components/input.md
---

# Slider — `nz-slider`

> **Dựng tạm theo đề xuất 07/11 — chưa qua trang chọn biến thể, user duyệt sau.**
>
> Bộ thử AntD. Giao diện theo **shadcnuikit.com/components/slider** (13 ví dụ, registry `slider1…13`, đọc mã 07/11)
> và primitive shadcn v4 (`ui.shadcn.com/r/styles/new-york-v4/slider.json`): rãnh `h-1.5` (6) bo tròn nền `bg-muted`,
> đoạn chọn `bg-primary`, núm `size-4` (16) nền trắng viền 1px màu chính `shadow-sm`, rê/focus `ring-4 ring-ring/50`.
> Thuộc tính theo **API ng-zorro 22.x**; biến Less đọc từ `ng-zorro-antd/style/themes/default.less` + `slider/style/index.less`.
> Đồng bộ với component đã dựng: rãnh nền **giống rãnh Switch tắt** (`switch/track-bg`), tooltip giá trị dùng
> **instance Tooltip** (`67:3374`, Trên · Một dòng), ô số dùng **instance Input** (`47:442`, Nền xám · default · Đã nhập + Đơn vị ₫).
> Slider dùng khi người dùng **ước lượng** trong một dải (bán kính, tải trọng, khoảng giá) và thấy được vị trí trong dải.
> Cần con số chính xác → luôn kèm ô số (web-10) hoặc dùng Input số thay Slider.

## 0. Đề xuất Dùng / Không dùng (chờ user duyệt)

| Mã | Ví dụ (shadcnuikit) | ng-zorro | Đề xuất | Lý do / dùng ở Invlogis |
|---|---|---|---|---|
| web-01 | Thanh trượt cơ bản, 1 giá trị | `nz-slider` | **Dùng** (= set chính) | Kiểu Một giá trị của set `Slider`; không cần mẫu ghép riêng |
| web-02 | Nhãn tham chiếu dưới rãnh (5 GB · 20 GB · 35 GB) | `nz-slider` + chữ tự ghép | **Dùng** (gộp vào web-04) | Mốc 0 km · 25 km · 50 km dưới thanh bán kính; không dựng riêng |
| web-03 | Vạch mốc + nhãn cách quãng | `nzMarks` | **Dùng** | Tải trọng hàng 0–40 tấn, mốc chính mỗi 10 tấn — set phụ `Slider mốc` |
| web-04 | Thanh trượt + số giá trị bên cạnh | `nz-slider` + output | **Dùng** | Bán kính tìm xe quanh điểm nhận: số "30 km" ở đầu dòng |
| web-05 | Icon loa nhỏ/lớn hai đầu | `nz-slider` + icon | Không dùng | Trang trí kiểu trình phát nhạc; không có nghiệp vụ |
| web-06 | Nhãn Low/High + bước 10 | `nzStep` | Không dùng | Trùng web-02/03; nhãn chữ Thấp/Cao không nói được giá trị |
| web-07 | Đánh giá trải nghiệm bằng emoji hai đầu | — | Không dùng | Trang trí; đánh giá tài xế/khách nếu có dùng `nz-rate` |
| web-08 | Nút − / + hai bên thanh | `nz-slider` + nút | Không dùng | Ô số `nz-input-number` (web-10) đã cho chỉnh từng bước, khỏi thêm 2 nút |
| web-09 | Emoji đổi theo giá trị | — | Không dùng | Trang trí, trùng web-07 |
| web-10 | Khoảng giá 2 núm + nhãn "Từ … đến …" | `nzRange` | **Dùng** | Lọc lệnh/bảng giá theo khoảng cước; thêm 2 ô số để gõ chính xác (mẫu AntD "Slider + InputNumber") |
| web-11 | Thanh đứng 1 giá trị | `nzVertical` | Không dùng | Web điều phối và app tài xế không có chỗ cần thanh đứng |
| web-12 | Thanh đứng khoảng | `nzVertical nzRange` | Không dùng | Như web-11 |
| web-13 | Bộ chỉnh âm (equalizer) nhiều thanh đứng | `nzVertical` | Không dùng | Trang trí, không có nghiệp vụ |

## 1. Thuộc tính

| ng-zorro | Figma property | Giá trị dùng | Ghi chú |
|---|---|---|---|
| `nzRange` | `Kiểu` (variant) | Một giá trị · Khoảng | Khoảng: 2 núm, đoạn chọn (màu chính) nằm giữa |
| `ngModel` | — | | Vị trí núm cố định theo biến thể: Một giá trị 60 %, Khoảng 25–75 %. Mẫu ghép chọn số khớp vị trí đó (30/50 km, 24/40 tấn, 2,5–7,5 triệu/10 triệu) |
| `nzMin` · `nzMax` · `nzStep` | — | | Theo nghiệp vụ. Vd bán kính 0–50 km bước 1; cước bước 100.000 ₫ |
| `nzTooltipVisible` · `nzTipFormatter` | `Trạng thái` = Rê/Kéo · lớp `Tooltip giá trị` (instance Tooltip lồng, đã expose → sửa `Nhãn`) | `default` | Tooltip chỉ hiện khi rê/kéo núm, không hiện thường trực. `nzTipFormatter` định dạng số: "60", "7.500.000 ₫" |
| `nzDisabled` | `Trạng thái` = Đã tắt | | Cả thanh mờ 50 % |
| (focus bàn phím) | `Trạng thái` = Focus | | Vòng 3px quanh núm như Input; ←/→ đổi một bước |
| `nzMarks` · `nzDots` | Set `Slider mốc`: `Mức` (variant) · `Nhãn` (text) | Chính · Phụ | Vạch dưới rãnh (web-03). Chính: vạch 4 + nhãn; Phụ: vạch 2, nhãn ẩn |
| `nzVertical` | — | | Không dựng (web-11…13 Không dùng) |
| `nzReverse` · `nzIncluded` | — | | Giữ mặc định (tô từ đầu rãnh) |

## 2. Thanh trượt

| Phần | Giá trị | Token |
|---|---|---|
| Rãnh | Cao 6, bo tròn, rộng theo cha (set vẽ 240, mẫu ghép 320) | `slider/rail-height` · `slider/radius` = `radius/full` |
| Nền rãnh | Xám nhạt như rãnh Switch tắt (Dark: trắng 10 %) | `slider/rail-bg` → `switch/track-bg` (→ `color/border-base`) |
| Đoạn chọn | Màu chính, từ đầu rãnh tới núm (Khoảng: giữa 2 núm) | `slider/track-bg` → `color/primary` |
| Núm | Tròn 16, nền trắng (Dark: nền tối), viền 1px màu chính, bóng `shadow/xs` | `slider/handle-size` · `slider/handle-bg` → `color/body-bg` · `slider/handle-border` → `color/primary` · `slider/handle-border-width` |

| Trạng thái | Cách thể hiện | Token |
|---|---|---|
| Thường | như trên | |
| Rê/Kéo | Quầng 4px quanh núm đang kéo + tooltip giá trị phía trên núm (Tooltip Trên · Một dòng, mũi tên cách mép núm 4) | `slider/handle-ring-width` · `color/focus-ring` · `slider/tooltip-offset` = 4 |
| Focus | Vòng 3px quanh núm (lệch −3, rộng +6) | `focus/width` · `color/focus-ring` |
| Đã tắt | Mờ 50 % | `opacity/disabled` |

Kiểu Khoảng: quầng/focus/tooltip đặt ở **núm cuối** (núm đang thao tác). Không đổi màu rãnh khi hover (AntD đổi
sang `primary-4`) — một màu chính cho mọi trạng thái, giống Switch.

Figma: núm nằm trong khung `Nút` co giãn theo tỉ lệ (constraint Scale), núm và tooltip neo giữa khung → kéo
rộng instance thì núm vẫn đúng vị trí phần trăm và giữ cỡ 16.

## 3. Vạch mốc (`Slider mốc`)

| Phần | Giá trị | Token |
|---|---|---|
| Ô mốc | Rộng 16 (= cỡ núm) để tâm vạch đầu/cuối thẳng tâm núm ở 0 % / 100 % | `slider/handle-size` |
| Vạch | 1 × 4 (Phụ 1 × 2), màu chữ phụ 70 % | `slider/mark-color` → `color/text-secondary` |
| Nhãn | `text/sm/medium` 12, màu chữ phụ, cách vạch 8; Phụ giữ chỗ (ẩn) | `slider/mark-color` |
| Khoảng rãnh → hàng mốc | 12 | `slider/mark-gap` → `spacing/sm` |

Ghép: hàng ngang rộng bằng thanh, `space-between`, mốc đầu/cuối = min/max. AntD vẽ mốc bằng chấm tròn trên rãnh
(`@slider-dot-border-color`) + nhãn dưới — bộ thử theo shadcn (vạch dưới rãnh), dev ẩn chấm (`nzDots` = false) và
style lại `.ant-slider-mark`.

## 4. Mẫu ghép

| Mã | Ví dụ | ng-zorro | Dùng ở Invlogis |
|---|---|---|---|
| web-10 | Lọc khoảng cước kèm 2 ô số | `nz-slider nzRange` + 2 `nz-input-number` (đơn vị ₫) | Bộ lọc lệnh vận tải / bảng giá: "Khoảng cước 2,5 – 7,5 triệu ₫"; gõ ô số thì thanh nhảy theo và ngược lại |
| web-04 | Bán kính tìm xe quanh điểm | `nz-slider` + số đầu dòng + mốc tham chiếu | Điều phối tìm xe trống: "Bán kính tìm xe quanh điểm nhận — 30 km", mốc 0 · 25 · 50 km |
| web-03 | Tải trọng với vạch mốc | `nz-slider nzMarks` | Lọc xe theo tải trọng: "Tải trọng hàng — 24 tấn", mốc 0…40 tấn mỗi 5 (nhãn mỗi 10) |

Bố cục chung: dòng đầu (nhãn `text/base/medium` trái, giá trị `text/base/medium` phải), thanh, rồi phần dưới
(ô số / mốc), các khối cách 12 (`spacing/sm`). Hai ô số cách nhau 8 (`spacing/xs`) với gạch nối "–" ở giữa.

Giới hạn dải (min/max/bước) của từng mẫu là **ví dụ minh hoạ**, không phải tham số sản phẩm — khi đưa vào SRS
thì min/max/bước bán kính và tải trọng đi qua mã `P-…` theo `.claude/rules/saas-layer.md`.

## 5. Figma

File `ElvhTYV3unixPkXky2oKIY`, trang **Slider** (`71:6016`) — dựng 07/11, chờ duyệt:

| Khối | Node | Nội dung |
|---|---|---|
| Frame `Slider` (tài liệu) | `71:15785` | Đầu trang · Playground **Light** / **Dark** (Kiểu, 4 trạng thái × 2 kiểu, vạch mốc) · `Ví dụ` (3 thẻ) · `Mapping` (9 thuộc tính + 13 token) |
| Section Components | `71:6878` | Set `Slider` `71:6791` = Kiểu (2) × Trạng thái (4) = **8**, ma trận cột Trạng thái, hàng Kiểu · Set phụ `Slider mốc` `71:6892` (Mức Chính · Phụ, text `Nhãn`) |
| Section Mẫu ghép | `71:7675` | `Slider mẫu ghép/web-10 …` `71:7676` · `web-04 …` `71:7711` · `web-03 …` `71:7724` |
| Biến mới — color | `slider/rail-bg` · `track-bg` · `handle-bg` · `handle-border` · `mark-color` | `VariableID:71:6017…71:6021` (alias, Light/Dark) |
| Biến mới — size | `slider/rail-height` · `handle-size` · `handle-border-width` · `radius` · `handle-ring-width` · `mark-gap` · `tooltip-offset` | `VariableID:71:6022…71:6028` |

Chữ "tấn" hiển thị thiếu dấu trên Figma — lỗi dấu tiếng Việt của Geist trên Figma đã ghi nhận ở trang Button,
không phải lỗi nội dung.
