---
type: design-system-component
status: draft
updated: 2026-11-07
links:
  - design-system-antd/foundations/foundations.md
  - design-system-antd/token-mapping.md
---

# Button — `nz-button`

> Bộ thử AntD. Giao diện theo **shadcnuikit Figma kit** (lưới biến thể) + **shadcnuikit.com/components/button**
> (mẫu ghép); thuộc tính theo **API ng-zorro 22.x**. Mọi con số là token trong `token-mapping.md` Mục 7.1.
> Lựa chọn giữ/bỏ: trang claude.ai/artifact/3eRLKXBhZLRfpBS1rcJ6Bx (db `answers`, đọc 06/11).

## 1. Thuộc tính

| ng-zorro | Figma property | Giá trị dùng | Ghi chú |
|---|---|---|---|
| `nzType` + class `secondary` | `Kiểu` (variant) | primary · secondary · default · text · link | `secondary` không có trong ng-zorro → dev thêm class riêng |
| `nzDanger` | `Kiểu` = danger | true | Gộp vào prop Kiểu trên Figma cho gọn |
| `nzSize` + class `xs` | `Cỡ` (variant) | xs · sm · default · lg (+ 4 cỡ chỉ icon) | `xs` không có trong ng-zorro → class riêng |
| chỉ icon | `Cỡ` = icon-xs · icon-sm · icon · icon-lg | — | Vuông, cạnh = chiều cao cỡ. **Luôn kèm `nz-tooltip`** |
| `nzLoading` | `Trạng thái` = Loading | true | Spinner trước chữ, nút mờ 50%, tắt bấm |
| `disabled` | `Trạng thái` = disabled | true | |
| `nzBlock` | — | true | Rộng hết khung; Figma kéo giãn, không cần biến thể |
| — | `Icon trái` · `Icon phải` (boolean + instance swap) | | Theo kit `Show Left Icon` · `Show Right Icon` |
| — | `Chữ` (text) | | Theo kit `Button Text` |
| — | `Số đếm` (boolean) + `Số đếm · chữ` (text) | | Số trong ô viền nhỏ sau nhãn (user chốt 07/11) |
| — | `Phím tắt` (boolean) | | Instance Kbd, như `Show KbdGroup` của kit |
| — | `Avatar` (boolean) | | Component `button/avatar` 22px đầu nút; nút vẫn bo 8 (bỏ pill, user chốt 07/11) |

**Không dùng** (không vẽ Figma, dev không làm): `nzType="dashed"`, `nzGhost`, `nzShape="circle"` / `round`.

## 2. Kiểu

| Kiểu | ng-zorro | Nền · chữ · viền | Hover | Dùng khi |
|---|---|---|---|---|
| Default (nền đen) | `nzType="primary"` | `color/primary` · `color/primary-foreground` | `color/primary-hover` (#2e2e2e) | Hành động chính, mỗi màn 1 nút (Lưu, Giao lệnh) |
| Secondary (nền xám) | class `secondary` | `color/bg-base` #f5f5f5 · `color/secondary-foreground` | đo lại khi dựng (kit `secondary/80`) | Nút phụ quan trọng hơn nút viền (Lưu nháp, Huỷ trong hộp thoại) |
| Outline | `nzType="default"` | `color/body-bg` · `color/text` · viền `color/border-base`, **không bóng** | `color/item-hover-bg` #f5f5f5 | Nút phụ cạnh nút chính |
| Ghost | `nzType="text"` | trong suốt · `color/text` | `color/item-hover-bg` | Trong bảng, thanh công cụ |
| Link | `nzType="link"` | trong suốt · `color/text`, gạch chân khi hover | gạch chân | Đi tới trang khác trong câu, ô bảng |
| Destructive (đỏ nhạt) | `nzDanger` | `color/error-bg` (đỏ 10%) · `color/error` | `color/error-bg-hover` (đỏ 20%) | Xoá, huỷ lệnh |

## 3. Cỡ

| Cỡ | ng-zorro | Cao | Padding ngang | Gap icon–chữ | Chữ | Nút chỉ icon |
|---|---|---|---|---|---|---|
| xs | class `xs` | `height/xs` 24 | 8 | `btn/gap-xs` 4 | 12 | 24 × 24 (icon-xs) |
| sm | `nzSize="small"` | `btn/height/sm` 32 | `btn/padding-x/sm` 10 | `btn/gap` 6 | 14 | 32 × 32 (icon-sm) |
| default | `nzSize="default"` | `btn/height/base` 36 | `btn/padding-x/base` 12 | `btn/gap` 6 | 14 | 36 × 36 (icon) |
| lg | `nzSize="large"` | `btn/height/lg` 40 | `btn/padding-x/lg` 16 | `btn/gap` 6 | 14 | 40 × 40 (icon-lg) |

Chung mọi cỡ: bo `btn/radius` 8 · icon `btn/icon-size` 16 · chữ Geist 500, `btn/letter-spacing` −0.25px.
Web dùng default 36; mobile dùng lg 40 cho nút chính; sm trong bảng, bộ lọc; xs trong ô bảng dày.

## 4. Trạng thái

| Trạng thái | Cách thể hiện | Token |
|---|---|---|
| Default | — | |
| Hover | Theo từng kiểu (Mục 2) | `color/primary-hover`, `color/item-hover-bg`, `color/error-bg-hover` |
| Focus | Vòng 3px quanh nút (`:focus-visible`) | `focus/width` 3 · `focus/color` #a3a3a3 50% |
| Pressed | Cả nút mờ 60% (`:active`), không màu riêng | `opacity/pressed` 0.6 |
| Loading | Spinner thay icon trái, nút tắt bấm. Biến thể "giữ độ rộng": chữ ẩn, spinner đè giữa | `nzLoading` |
| Disabled | Cả nút mờ 50% | `opacity/disabled` 0.5 |

## 5. Ví dụ đã chốt — mẫu ghép xếp theo 4 nhóm

Từ 07/11 mẫu ghép **không còn là component riêng** (duyệt trên trang claude.ai/artifact/EW8eQ5m7gzVLTRPysdmo1X, db `answers`).
Mỗi mẫu vào 1 trong 4 nhóm:

| Nhóm | Nghĩa | Trên Figma |
|---|---|---|
| 1 · Thuộc tính | Chỉ thêm một phần nhỏ vào nút | Thuộc tính bật tắt / chữ trên set Button, **không thêm trục biến thể** |
| 2 · Component riêng | Có cấu trúc riêng | Set riêng có biến thể (Mục 5.1) |
| 3 · Cách dùng | Ghép nhiều component | Chỉ là ví dụ trong khung tài liệu (instance thường hoặc detach) |
| 4 · Đã có sẵn | Trùng biến thể/thuộc tính có sẵn | Bỏ mẫu, thẻ ví dụ dùng instance set Button |

| # | Mẫu | Nhóm | Đi đâu | Dùng khi |
|---|---|---|---|---|
| web-01 | Nút chính | 4 | `Kiểu=Default` | Nút chính |
| web-02 | Đang tải | 4 | `Trạng thái=Loading` | Đang gửi lệnh |
| web-03 | Xoá | 4 | `Kiểu=Destructive` + icon trái | Xoá |
| web-04 | Spinner đè, giữ độ rộng | 4 | `Trạng thái=Loading` (dev: `nzLoading` + CSS giữ độ rộng) | Nút trong hàng không được nhảy độ rộng |
| web-05 | Huỷ / Lưu | 3 | 2 instance Secondary + Default | Footer form, hộp thoại |
| web-06 | Số đếm | 1 | `Số đếm` (ô viền) | Số mục chờ xử lý |
| web-07 | Phím tắt ⌘P | 1 | `Phím tắt` | Web, người dùng văn phòng |
| web-08 | Có avatar | 1 | `Avatar`, bo 8 | Đổi người đang chọn |
| web-09 | Icon trái | 4 | `Icon trái` | Thêm lệnh; mobile chỉ còn icon |
| web-11 | Chuông + badge | 3 | Button chỉ icon bọc `nz-badge` (chờ Badge) | Thông báo trên header |
| web-12 | Đổi sáng/tối | 2 | `Nút đổi icon`, Loại=Sáng tối | Header |
| web-13 | Chép → dấu tích | 2 | `Nút đổi icon`, Loại=Chép (tự về sau 1,5 s) | Chép mã lệnh, biển số |
| web-14 | + / − dọc | 2 | `Button group`, Hướng=Dọc | Phóng to/thu nhỏ bản đồ |
| web-16 | Split viền | 2 | `Split button`, Kiểu=Viền | Hành động chính + lựa chọn phụ |
| web-17 | Bước tăng giảm | 3 | Thuộc về Input number (`nz-input-number`, chưa dựng) | Số kiện, số chuyến |
| web-18 | Split nền đậm | 2 | `Split button`, Kiểu=Nền đậm | Như web-16, khi là hành động chính |
| web-19 · web-20 | Trước / Sau | 2 | `Button group`, Kiểu=Viền, 2 nút có icon | Lật bản ghi ở màn chi tiết |
| web-21 | Sao + số | 1 | `Số đếm` + icon trái | |
| web-22 | Thích + số | 1 | `Số đếm` + icon trái (bỏ vạch ngăn) | |
| web-24 · web-25 | Đăng nhập MXH | 2 | `Nút đăng nhập MXH` | Màn đăng nhập (màu hãng không phải token) |
| web-26 | Icon + tooltip | 3 | Button chỉ icon + `nz-tooltip` | Bắt buộc với mọi nút chỉ icon |
| web-27 | Trái \| Giữa \| Phải | 2 | `Button group`, Kiểu=Phân đoạn, 3 nút | Chuyển Ngày / Tuần / Tháng |

**Không dùng:** web-10 icon tròn (đã có icon vuông) · web-23 đăng nhập chỉ icon · web-15 ô nhập + nút tìm rời → **chuyển sang Input**: icon tìm nằm trong ô (`nzSuffix`),
không còn nút rời (user chốt 06/11: ô pill đứng cạnh nút bo 8 lệch góc).

### 5.1 Component tách từ mẫu ghép

| Component | ng-zorro | Biến thể | Ghi chú |
|---|---|---|---|
| `Split button` | `nz-button-group` + `nz-dropdown` | Kiểu Viền · Nền đậm × Trạng thái Default · Disabled = 4 | |
| `Button group` | `nz-button-group` | Kiểu Viền · Phân đoạn × Hướng Ngang · Dọc × Số nút 2 · 3 = 8 | Nút con là instance Button, sửa chữ/icon ngay trên instance |
| `Nút đổi icon` | Button chỉ icon + đổi icon theo trạng thái | Loại Sáng tối · Chép × Trạng thái Trước · Sau = 4 | Prototype bấm để đổi; Chép tự về sau 1,5 s |
| `Nút đăng nhập MXH` | Button outline/fill màu hãng + logo | Hãng (Google · X · Facebook · GitHub) × Kiểu Viền · Nền màu hãng = 8 | Rộng cố định 280 (user chốt 07/11); màn mobile đặt giãn khi vẽ màn |

## 6. Nút trượt xác nhận — component riêng `slide-confirm`

Không có trong ng-zorro → dev dựng component mới (Angular CDK drag). Dùng trên mobile khi tài xế xác nhận
giao hàng, nhận lệnh — tránh bấm nhầm.

| Phần | Giá trị | Token |
|---|---|---|
| Rãnh | rộng tối đa 280, cao 56, **bo 18** | `slide/height` 56 · `slide/radius` = `radius/2xl` 18 |
| Đệm rãnh | 4 | `slide/padding` 4 |
| Nút kéo | 48 × 48, **bo 14 = 18 − 4** (đồng tâm với rãnh) | `slide/grip-size` 48 · `slide/grip-radius` = `radius/xl` 14 |
| Màu | rãnh `color/bg-base` · nút `color/primary` · mũi tên `color/primary-foreground` · chữ gợi ý `color/text-secondary` | Light #f5f5f5 / #171717 · Dark #262626 / #e5e5e5 — cùng biến, đổi theo mode |

Giữ 3 biến thể nền: **Sáng**, **Sáng có viền** (rãnh nền trắng `color/body-bg` + viền 1px `color/border-base`, user giữ 06/11 tối) và **Tối** (mode Dark).

Hành vi (khớp bencho.dev/?c=slide-confirm, user chốt 06/11): kéo tới đâu, **khối cùng màu nút kéo phủ từ đầu rãnh tới đó**;
chữ gợi ý mờ dần (hết ở 55% quãng), mũi tên mờ ở 40% cuối. Chỉ xác nhận khi kéo tới cuối; thả giữa chừng thì lò xo về
(chạm mép nén 8%). Xác nhận: nút kéo **giãn sang trái lấp kín rãnh, mép phải đứng yên** → cụm **✓ + "Đã xác nhận"** (nằm giữa
nút) **trượt từ phải vào giữa**, rõ dần, phóng 70% → 100%; giữ 1,5 giây rồi nút thu về cỡ 48 ở đầu rãnh. Phím Enter/Space
trên nút kéo = xác nhận.

## 7. Figma

File `ElvhTYV3unixPkXky2oKIY`, trang **Button** (`14:9`) — bố cục theo shadcn UI Kit (user chốt 06/11: bảng master dạng ma trận + playground như kit):

| Khối | Node | Nội dung |
|---|---|---|
| Frame `Button` (tài liệu) | `13:1714` | Rộng 1536: đầu trang · Playground **Light** (trên) và **Dark** (dưới), nút xếp dọc giữa theo nhóm cỡ default → sm → lg → xs, rồi 4 hàng chỉ icon |
| Section Components | `13:432` | Set `Button` `15:2459` = **1 set 288 tổ hợp** như kit: Kiểu (6) × Cỡ (8: xs · sm · default · lg · icon-xs · icon-sm · icon · icon-lg) × Trạng thái (6: Default · Hover · Focus · Loading · Disabled · Pressed). Ma trận: cột = trạng thái, hàng 2 cấp Kiểu → Cỡ, lưới nét đứt tím |
| Section Component tách từ mẫu ghép | `80:1641` | `Split button` `80:1800` · `Button group` `80:2079` · `Nút đổi icon` `80:2121` · `Nút đăng nhập MXH` `80:2288` (Mục 5.1). Section mẫu ghép cũ `13:3312` đã xoá 07/11 |
| Khối `Ví dụ đã chốt` (trong `13:1714`) | `13:2703` | Lưới 3 cột, mỗi thẻ là instance set Button / set Mục 5.1; web-05, 11, 17, 26 là ví dụ cách dùng (detach) |
| Khối `Mapping` (trong `13:1714`) | `13:3152` | Bảng thuộc tính ng-zorro ↔ Figma + bảng token Figma variable ↔ biến Less |
| Section Icons (lucide) | `14:10` | 21 icon lucide + 4 logo hãng (`brand/google` · `x` · `facebook` · `github`), 16px, nét theo màu chữ nút |

Thuộc tính: `Chữ` (text) · `Icon trái` · `Icon phải` (boolean) · `Icon trái · chọn` · `Icon phải · chọn` (instance swap) · `Số đếm` (boolean) + `Số đếm · chữ` (text) · `Phím tắt` (boolean) · `Avatar` (boolean, component `button/avatar` `78:1275` trong Icons). 3 thuộc tính sau chỉ có ở 144 biến thể có chữ.
Số đếm: khung `Số đếm` cao `kbd/height` 20, bo `kbd/radius`, đệm ngang 6, viền 1px cùng màu chữ nút 25%; chữ `font-size/sm` 12, mờ 60%.
Cỡ `icon-*` chỉ có icon (instance swap qua `Icon trái · chọn`), luôn kèm tooltip khi dùng.
Loading là một **trạng thái** (như kit): spinner hiện, nút mờ `opacity/disabled`.
Focus: lớp `Focus ring` viền 3px ngoài nút, bo 11 (= `btn/radius` 8 + `focus/width` 3), màu `color/focus-ring`
(Destructive: `color/focus-error-ring`); Outline focus đổi viền sang `color/ring`. Không dùng effect bóng vì
nút không nền (Ghost, Link) không hiện bóng. Text style: `button/base` (14/20), `button/xs` (12/16), Geist Medium −0.25px.
Bộ 288 biến thể tạo bằng Figma MCP vì reqwise giới hạn 50 tổ hợp/set; bảng, nhãn, playground dựng bằng reqwise.

Section Slide confirm `13:4056`: set `Slide confirm` `13:4117` — Nền (Sáng · Sáng có viền · Tối, mode Dark gắn trên biến thể) × Trạng thái (Nghỉ · Đang kéo · Đã xác nhận) = 9; gắn `slide/height` · `slide/grip-size` · `slide/radius` · `slide/grip-radius`; thuộc tính `Chữ gợi ý` (text). Prototype: Nghỉ —On drag→ Đã xác nhận (Smart animate, Gentle 0,45 s) —After delay 1,5 s→ Nghỉ; các lớp đổi bằng opacity/vị trí (không ẩn/hiện) để Smart animate chạy; khối phủ cùng màu nút, trạng thái Đã xác nhận nút kéo phủ kín rãnh, cụm `Xong` (✓ + chữ) đặt sát phải mờ 0 ở Nghỉ/Đang kéo → giữa rõ 100% ở Đã xác nhận nên trượt từ phải vào. **Figma Motion (keyframe)** gắn trên biến thể Nghỉ (Sáng, Sáng có viền, Tối) — instance tự chạy, số liệu lấy từ code bencho (SlideConfirm, speed 50):
0,1–0,9 s kéo (nút 0 → 224, khối phủ 48 → 272, chữ gợi ý mờ hết ở 55%, mũi tên mờ 40% cuối) ·
0,9–1,2 s xác nhận: nút giãn trái + cụm `Xong` trượt từ phải (−85,5 px) theo **lò xo giảm chấn tới hạn**
(stiffness 580, mass 0,9, damping 45,7 → `CUSTOM_SPRING` bounce 0: ra nhanh, chậm dần, 95% sau ≈ 0,19 s) ·
cụm `Xong` mờ → rõ + 70% → 100% trong 0,16 s, cubic (0.33, 0.55, 0.2, 1) ·
**nhịp nhấn sau khi tới nơi**: khung `Rãnh` 1,0 → 1,26 → 1,42 s co 100% → 97,4% → 100%, cubic như trên ·
sau đó giữ trạng thái xác nhận. Không có bước thu về: component trong set chỉ chạy 2 s đầu (set không có timeline riêng).
Figma không cho keyframe trên chính component nên nhịp nhấn đặt trên khung con `Rãnh`. Frame chứa instance cần timeline ≥ 2 s. Giới hạn Figma: kéo bất kỳ đoạn nào cũng hoàn tất, không có ngưỡng cuối rãnh và lò xo trả về — hành vi đúng xem trên trang artifact.
