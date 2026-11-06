---
type: design-foundations
status: approved
updated: 2026-11-06
links:
  - design-system-antd/token-mapping.md
  - design-system-antd/README.md
---

# Foundations đã chốt — bộ thử shadcn → Ant Design

> Duyệt 06/11 trên trang claude.ai/artifact/XV5xq5YFK21sKFLWHtGTGb (9/9 mục). Cập nhật 06/11 chiều theo trang so sánh
> claude.ai/artifact/Qj8jL1PeqzTCJC2tU9SKWr: lấy **shadcnuikit Figma kit** (`uSGI07mEcItaHEVre2RwFq`) làm chuẩn, có trộn (Mục 8). Đây là **spec dựng Figma**:
> danh sách biến theo collection, giá trị cuối. Cột biến Less, mặc định AntD, trường hợp → [[design-system-antd/token-mapping|bảng mapping]].

## 1. Collection và mode trên Figma

| Collection | Mode | Chứa |
|---|---|---|
| `color` | Light · Dark | Mọi màu (Mục 2) |
| `size` | 1 mode | Bo góc, khoảng cách, chiều cao, padding, độ mờ, focus (Mục 4–6) |
| `type` | 1 mode | Font, cỡ, dòng, độ đậm (Mục 3) — kèm text style |
| Effect styles | — | `shadow/xs`, `shadow/base`, `focus/ring`, `focus/error-ring` (Mục 6) |

Tên biến theo biến Less của ng-zorro (README nguyên tắc 1). Mọi component chỉ dùng biến — không số thô.

## 2. Màu (`color`)

| Biến | Light | Dark |
|---|---|---|
| `color/primary` | #171717 | #e5e5e5 |
| `color/primary-foreground` | #fafafa | #171717 |
| `color/primary-hover` | #2e2e2e (= primary + trắng 10%) | #cfcfcf |
| `color/text` | #0a0a0a | #fafafa |
| `color/heading` | #0a0a0a | #fafafa |
| `color/text-secondary` | #737373 | #a1a1a1 |
| `color/input-placeholder` | #737373 | #a1a1a1 |
| `color/link` | #171717 | #e5e5e5 |
| `color/body-bg` | #ffffff | #0a0a0a |
| `color/layout-body-bg` | #ffffff | #0a0a0a |
| `color/layout-header-bg` | #ffffff | #0a0a0a |
| `color/component-bg` | #ffffff | #171717 |
| `color/popover-bg` | #ffffff | #171717 |
| `color/bg-base` | #f5f5f5 | #262626 |
| `color/item-hover-bg` | #f5f5f5 | #262626 |
| `color/item-active-bg` | #f5f5f5 | #262626 |
| `color/accent-foreground` | #171717 | #fafafa |
| `color/secondary-foreground` | #171717 | #fafafa |
| `color/sider-bg` | #fafafa | #171717 |
| `color/border-base` | #e5e5e5 | #ffffff 10% |
| `color/border-split` | #e5e5e5 | #ffffff 10% |
| `color/input-border` | trong suốt | trong suốt |
| `color/input-hover-border` | #a1a1a1 | #ffffff 30% |
| `color/input-bg` | #f2f2f2 | #ffffff 4.5% |
| `color/ring` | #a1a1a1 | #737373 |
| `color/error` | #e7000b | #ff6467 |
| `color/error-foreground` | #ffffff | #ffffff |
| `color/error-bg` | #e7000b 10% | #ff6467 20% |
| `color/error-bg-hover` | #e7000b 20% | #ff6467 30% |
| `color/success` | #52c41a | #49aa19 |
| `color/warning` | #faad14 | #d89614 |
| `color/info` | #155dfc | #2b7fff |
| `color/focus-ring` | #a1a1a1 50% | #737373 50% |
| `color/focus-error-ring` | #e7000b 20% | #ff6467 40% |
| `color/chart-1` … `chart-5` | #f54900 · #009689 · #104e64 · #ffb900 · #fe9a00 | #1447e6 · #00bc7d · #fe9a00 · #ad46ff · #ff2056 |

Ô nhập không viền: nhận diện bằng nền xám `color/input-bg` (kiểu shadcnuikit web). `color/input-hover-border` giữ cho control khác còn viền (select viền, checkbox).
Nhấn nút không dùng màu riêng: cả nút mờ `opacity/pressed` (Mục 5, Mục 7).

## 3. Chữ (`type`)

| Biến | Giá trị |
|---|---|
| `font/family` | **Geist** |
| `font/heading-family` | Cal Sans (display + heading) |
| `font/code-family` | Geist Mono |
| `font-weight/regular` · `medium` · `semibold` | 400 · 500 · 600 (Geist: Regular · Medium · SemiBold) |
| `font-weight/button` | 500 |
| `font-weight/title` | 400 (Cal Sans chỉ có 1 độ đậm) |
| `btn/letter-spacing` | −0.25px (Figma ≈ −1.8% ở cỡ 14) |

Chữ hiển thị **antialiased** (`-webkit-font-smoothing: antialiased`) — thiếu dòng này chữ nút trông đậm hơn thiết kế.
Geist, Geist Mono, Cal Sans đủ 74/75 ký tự tiếng Việt, chỉ thiếu **₫** (trình duyệt lấy font dự phòng). Trên Figma ghi tiền bằng "đ" hoặc "VNĐ".

> ⚠ **Lỗi dấu tiếng Việt trên Figma (06/11):** Geist do Figma cung cấp là bản cũ: mất dấu sắc / huyền / ngã khi
> chồng lên mũ hoặc trăng (ấ ầ ẫ · ắ ằ ẵ · ế ề ễ · ố ồ ỗ — "Tiếp" thành "Tiêp"). Bản web (Google Fonts) và bản
> **Geist v1.9.2** (github.com/vercel/geist-font) đúng hết, có cả ₫. Cách dùng: **cài Geist + Geist Mono v1.9.2 vào máy**
> (`~/Library/Fonts`) rồi mở lại Figma desktop. Máy chưa cài (dev, khách, Figma trên trình duyệt) vẫn thấy lỗi —
> khi gửi file Figma cho người khác phải nhắc cài font. Code dev không bị ảnh hưởng (dùng Google Fonts hoặc gói `geist`).

**Text style** (cỡ / dòng):

| Text style | Font | Cỡ / dòng | Biến ng-zorro |
|---|---|---|---|
| `display/2` | Cal Sans | 60 / 60 | — |
| `display/1` | Cal Sans | 48 / 48 | — |
| `heading/1` | Cal Sans | 36 / 40 | `@heading-1-size` |
| `heading/2` | Cal Sans | 30 / 36 | `@heading-2-size` |
| `heading/3` | Cal Sans | 24 / 32 | `@heading-3-size` |
| `heading/4` | Cal Sans | 20 / 28 | `@heading-4-size` |
| `heading/5` | Cal Sans | 16 / 24 | `@heading-5-size` |
| `text/xl` | Geist | 18 / 28 | — |
| `text/lg` | Geist | 16 / 24 | `@font-size-lg` |
| `text/base` | Geist | 14 / 20 | `@font-size-base`, `@line-height-base` 1.4286 |
| `text/sm` | Geist | 12 / 16 | `@font-size-sm` |
| `code/base` | Geist Mono | 14 / 20 | `@code-family` |

Mỗi text style Geist có biến thể độ đậm Regular / Medium / SemiBold (4 × 3 = 12 style).

## 4. Bo góc (`size`)

| Biến | Giá trị |
|---|---|
| `radius/xs` | 2 |
| `radius/checkbox` | 4 |
| `radius/sm` | 6 |
| `radius/base` | 8 |
| `radius/lg` | 10 |
| `radius/xl` · `2xl` · `3xl` · `4xl` | 14 · 18 · 22 · 26 |
| `radius/full` | 9999 |

| Dùng ở | Bo |
|---|---|
| Nút (mọi cỡ) | `radius/base` 8 |
| Ô nhập (`input/radius`) | `radius/lg` 10 — bo theo kit (chốt 07/11, bỏ pill) |
| Card (`card/radius`) | `radius/xl` 14 |
| Tag, badge (`tag/radius`) | `radius/full` — pill |
| Mục trong menu | `radius/sm` 6 |
| Checkbox | `radius/checkbox` 4 |

## 5. Khoảng cách, chiều cao, padding (`size`)

| Biến | Giá trị |
|---|---|
| `spacing/2` · `xss` · `6` · `xs` · `sm` · `md` · `20` · `lg` · `32` · `40` · `48` | 2 · 4 · 6 · 8 · 12 · 16 · 20 · 24 · 32 · 40 · 48 |
| `height/xs` · `sm` · `base` · `lg` | 24 · 32 · 36 · 40 |
| `btn/padding-x/sm` · `base` · `lg` | 10 · 12 · 16 (dev nhập 9 · 11 · 15) |
| `btn/padding-x-icon/sm` · `base` · `lg` | 10 · 12 · 16 — đo lại khi dựng Button |
| `btn/gap` · `btn/gap-xs` | 6 · 4 |
| `input/padding-x` · `input/padding-y` | 12 (không viền nên dev nhập 12) · 4 |
| `card/padding` | 24 |
| `tag/height` | 20 |
| `opacity/disabled` | 0.5 (trên Figma nhập 50 — biến độ mờ của Figma tính theo %) |
| `opacity/pressed` | 0.6 (Figma 60) |
| `focus/width` | 3 |

## 6. Đổ bóng, focus (Effect styles)

| Style | Giá trị |
|---|---|
| `shadow/xs` | 0 1 2 0 · #000 5% |
| `shadow/base` | 0 4 6 −1 · #000 10% + 0 2 4 −2 · #000 10% |
| `focus/ring` | spread 3 · `color/ring` 50% |
| `focus/error-ring` | spread 3 · `color/error` 20% (Dark 40%) |

Nút (mọi kiểu), ô nhập, card: **không đổ bóng**. Checkbox: `shadow/xs`. Menu xổ, popover: `shadow/base`.

## 7. Trạng thái tương tác

| Trạng thái | Quy tắc |
|---|---|
| Hover nút chính | `color/primary-hover` |
| Nhấn nút (mọi kiểu) | cả nút `opacity/pressed` 0.6 (kit shadcnuikit) |
| Hover nút viền, nút text | nền `color/item-hover-bg` |
| Hover ô nhập | không đổi (ô nhập không viền) |
| Nút xoá | nền `color/error-bg`, chữ `color/error`; hover nền `color/error-bg-hover` |
| Focus | viền `color/ring` + `focus/ring` |
| Lỗi | viền `color/error` + `focus/error-ring` |
| Tắt | cả control `opacity/disabled` 0.5, không nhận thao tác |
| Mục đang chọn trong menu | nền `color/item-active-bg` + dấu ✓ bên phải |

## 8. Đổi 06/11 chiều — theo shadcnuikit Figma kit

Chốt trên trang so sánh claude.ai/artifact/Qj8jL1PeqzTCJC2tU9SKWr + trang font claude.ai/artifact/WTpcYA2VQsNsdjS9xRuf17.

| Mục | Chốt |
|---|---|
| Nền tảng | **B — shadcnuikit Figma kit**, trộn các dòng dưới |
| Chữ thường | **Geist** (thay Inter); tiêu đề Cal Sans; mã/số Geist Mono |
| Nút | bo 8, cao 36 · 32 · 40, padding ngang 12 (sm 10, lg 16), gap 6, chữ −0.25px |
| Hover / nhấn nút chính | primary + trắng 10% (#2e2e2e) / cả nút mờ 60% (bỏ màu nhấn #454545) |
| Nút viền, ô nhập | không đổ bóng |
| Ô nhập | kiểu shadcnuikit web: nền #f2f2f2, không viền, bo pill |
| Nút xoá | đỏ nhạt: nền 10%, chữ đỏ, hover 20% |
| Card · tag | đo trong kit: card bo 14, pad 24, không bóng · tag pill cao 20 |
