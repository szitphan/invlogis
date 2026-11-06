---
type: design-mapping
status: draft
updated: 2026-11-06
links:
  - design-system-antd/README.md
---

# Bảng mapping token — shadcn → Figma variable → ng-zorro (Ant Design)

> Bảng **duy nhất** cho bộ thử. Mỗi token mới phát sinh khi dựng foundations hay component đều thêm vào đây.
> Nguồn và nguyên tắc: [[design-system-antd/README|README]]. Spec đã chốt: [[design-system-antd/foundations/foundations|Foundations]].
> Từ 06/11 chiều, giá trị component theo **shadcnuikit Figma kit** (`uSGI07mEcItaHEVre2RwFq`), trộn theo Mục 8.2. Cột "shadcn" ghi class/biến của kit.

## 0. Cách đọc

| Cột | Nghĩa |
|---|---|
| shadcn | Tên biến/class gốc ở shadcn v4 (theme neutral) — chỉ để tham khảo |
| Figma variable | Tên biến trên file Figma bộ thử — **đặt theo biến Less của ng-zorro** |
| Giá trị | Giá trị chốt (lấy từ shadcn). Màu có 2 mode **Light / Dark** |
| Biến ng-zorro | Biến Less dev sửa (`ng-zorro-antd` 22.2.0, `default.less`) |
| Mặc định AntD | Giá trị gốc của biến đó |
| TH | **1:1** = không làm gì · **Ghi đè** = dev đổi giá trị biến · **Thêm mới** = AntD không có, dev thêm vào theme / biến CSS · **Chưa chốt** |

**Quy tắc chung cho dev:**

1. **Padding trừ viền.** AntD tính padding *không gồm* viền 1px (`@btn-padding-horizontal-base` = 16 − 1 = 15). Figma đo từ mép ngoài. Cột "Giá trị" ghi số Figma, ô dev ghi rõ `N − 1`.
2. **Nền tối.** ng-zorro không có biến cho nền tối — nền tối là file riêng `ng-zorro-antd.dark.css`/`dark.less`. Dev ghi đè 2 lần: theme mặc định (cột Light) và theme tối (cột Dark).
3. **Màu quy đổi.** shadcn khai màu bằng `oklch`, Less cần hex. Hex trong bảng là quy đổi (≈), giá trị gốc ghi kèm.
4. **Tắt (disabled).** Chốt 06/11: mờ cả control 50% như shadcn → dev viết CSS riêng, không dùng `@disabled-color`/`@disabled-bg`.

## 1. Màu

### 1.1 Màu chính và trạng thái

| shadcn | Figma variable | Light | Dark | Biến ng-zorro | Mặc định AntD | TH |
|---|---|---|---|---|---|---|
| `--primary` oklch(0.205 0 0) / dark 0.922 | `color/primary` | #171717 | #e5e5e5 | `@primary-color` | #1890ff | **Ghi đè** (chốt 06/11: đen shadcn) |
| `--primary-foreground` 0.985 / dark 0.205 | `color/primary-foreground` | #fafafa | #171717 | `@btn-primary-color` | #fff | Ghi đè |
| State Hover (kit): primary + trắng 10% | `color/primary-hover` | #2e2e2e | #cfcfcf | `@primary-color-hover` | colorPalette(primary, 5) | Ghi đè — AntD tự sinh từ dải 10 màu, với màu đen sẽ ra xám nhạt; phải ghi tay |
| State Pressed (kit): cả nút `opacity-60` | `opacity/pressed` (không còn `color/primary-active`) | 0.6 → quy đổi #747474 | 0.6 → #8d8d8d | `@primary-color-active` | colorPalette(primary, 7) | Ghi đè — dev nhập màu quy đổi cho `@primary-color-active`, hoặc CSS `:active{opacity:.6}` cho mọi kiểu nút (chốt 06/11 chiều, thay #454545) |
| `--destructive` oklch(0.577 0.245 27.3) / dark (0.704 0.191 22.2) | `color/error` | #e7000b ≈ | #ff6467 ≈ | `@error-color` | #ff4d4f | Ghi đè |
| `destructive-foreground` (kit) / `text-white` | `color/error-foreground` | #ffffff | #ffffff | `@btn-danger-color` | #fff | 1:1 |
| `bg-destructive/10` · `dark:bg-destructive/20` (nút xoá nhạt) | `color/error-bg` | #e7000b 10% | #ff6467 20% | `@btn-danger-bg` | = error-color | **Ghi đè** — nút xoá đỏ nhạt, chữ `@btn-danger-color` = `color/error` |
| `hover:bg-destructive/20` · `dark:/30` | `color/error-bg-hover` | #e7000b 20% | #ff6467 30% | — (AntD tự sinh hover) | — | Thêm mới — CSS hover riêng cho `nzDanger` |
| — (shadcn không có) | `color/success` | #52c41a | #49aa19 | `@success-color` | #52c41a | 1:1 — giữ AntD (Dark theo `dark.less`, chốt 06/11) |
| `--warning` (chỉ là ví dụ token tự thêm trong docs) | `color/warning` | #faad14 | #d89614 | `@warning-color` | #faad14 | 1:1 — giữ AntD (Dark theo `dark.less`, chốt 06/11) |
| — (Tailwind blue-600 / blue-500) | `color/info` | #155dfc | #2b7fff | `@info-color` · `@processing-color` | = primary | Ghi đè (chốt 06/11: tách xanh khỏi màu chính đen) |
| `--ring` 0.708 / dark 0.556 | `color/ring` | #a1a1a1 | #737373 | `@primary-color-outline` | fade(primary, 20%) | **Thêm mới** + ghi đè — shadcn dùng màu ring riêng, không theo màu chính |

### 1.2 Chữ

| shadcn | Figma variable | Light | Dark | Biến ng-zorro | Mặc định AntD | TH |
|---|---|---|---|---|---|---|
| `--foreground` 0.145 / dark 0.985 | `color/text` | #0a0a0a | #fafafa | `@text-color` | đen 85% | Ghi đè |
| `--foreground` | `color/heading` | #0a0a0a | #fafafa | `@heading-color` | đen 85% | Ghi đè |
| `--muted-foreground` 0.556 / dark 0.708 | `color/text-secondary` | #737373 | #a1a1a1 | `@text-color-secondary` | đen 45% | Ghi đè |
| `placeholder:text-muted-foreground` | `color/input-placeholder` | #737373 | #a1a1a1 | `@input-placeholder-color` | #bfbfbf | Ghi đè |
| `opacity-50` | `opacity/disabled` | 0.5 (cả control) | 0.5 | — (`@disabled-color`, `@disabled-bg` không dùng) | đen 25% · #f5f5f5 | **Thêm mới** (chốt 06/11: mờ 50% như shadcn) — dev viết CSS `opacity:.5` + `pointer-events:none` cho từng component ng-zorro có trạng thái tắt |
| `text-primary` (nút link) | `color/link` | #171717 | #e5e5e5 | `@link-color` | = primary | 1:1 (theo primary) |

### 1.3 Nền

| shadcn | Figma variable | Light | Dark | Biến ng-zorro | Mặc định AntD | TH |
|---|---|---|---|---|---|---|
| `--background` 1 / dark 0.145 | `color/body-bg` | #ffffff | #0a0a0a | `@body-background` | #fff | 1:1 (Light) |
| `--card` 1 / dark 0.205 | `color/component-bg` | #ffffff | #171717 | `@component-background` | #fff | 1:1 (Light) |
| `--popover` 1 / dark 0.205 | `color/popover-bg` | #ffffff | #171717 | `@popover-background` | = component-bg | 1:1 |
| `--secondary` / `--muted` 0.97 / dark 0.269 | `color/bg-base` | #f5f5f5 | #262626 | `@background-color-base` | #f5f5f5 | 1:1 (Light) |
| `--accent` 0.97 / dark 0.269 | `color/item-hover-bg` | #f5f5f5 | #262626 | `@item-hover-bg` | #f5f5f5 | 1:1 (Light) |
| `--accent-foreground` 0.205 / dark 0.985 | `color/accent-foreground` | #171717 | #fafafa | — | — | Thêm mới |
| `--accent` (mục đang chọn) | `color/item-active-bg` | #f5f5f5 | #262626 | `@item-active-bg` | primary-1 (#e6f7ff) | Ghi đè — dải màu của đen không dùng được |
| `--secondary-foreground` | `color/secondary-foreground` | #171717 | #fafafa | — | — | Thêm mới (nút secondary — Mục 7.1) |
| `--sidebar` 0.985 / dark 0.205 | `color/sider-bg` | #fafafa | #171717 | `@layout-sider-background-light` | #fff | Ghi đè |
| `--background` | `color/layout-body-bg` | #ffffff | #0a0a0a | `@layout-body-background` | #f0f2f5 | Ghi đè (chốt 06/11: trắng như shadcn) |
| `--background` + `border-b` | `color/layout-header-bg` | #ffffff (viền dưới `color/border-base`) | #0a0a0a | `@layout-header-background` | #001529 | Ghi đè (chốt 06/11) |

### 1.4 Viền

| shadcn | Figma variable | Light | Dark | Biến ng-zorro | Mặc định AntD | TH |
|---|---|---|---|---|---|---|
| `--border` 0.922 / dark trắng 10% | `color/border-base` | #e5e5e5 | #ffffff 10% | `@border-color-base` | #d9d9d9 | Ghi đè |
| `--border` | `color/border-split` | #e5e5e5 | #ffffff 10% | `@border-color-split` | #f0f0f0 | Ghi đè (shadcn dùng 1 màu viền) |
| Ô nhập không viền (shadcnuikit web) | `color/input-border` | trong suốt | trong suốt | `@input-border-color` | = border-base | **Ghi đè** (chốt 06/11 chiều) |
| — | `color/input-hover-border` | #a1a1a1 | #ffffff 30% | `@input-hover-border-color` | primary-5 | Ghi đè — ô nhập không còn viền; giữ cho select viền, checkbox |

### 1.5 Biểu đồ, sidebar (AntD không có)

| shadcn | Figma variable | Light | Dark | TH |
|---|---|---|---|---|
| `--chart-1` | `color/chart-1` | #f54900 ≈ oklch(0.646 0.222 41.1) | #1447e6 ≈ oklch(0.488 0.243 264.4) | Thêm mới |
| `--chart-2` | `color/chart-2` | #009689 ≈ oklch(0.6 0.118 184.7) | #00bc7d ≈ oklch(0.696 0.17 162.5) | Thêm mới |
| `--chart-3` | `color/chart-3` | #104e64 ≈ oklch(0.398 0.07 227.4) | #fe9a00 ≈ oklch(0.769 0.188 70.1) | Thêm mới |
| `--chart-4` | `color/chart-4` | #ffb900 ≈ oklch(0.828 0.189 84.4) | #ad46ff ≈ oklch(0.627 0.265 303.9) | Thêm mới |
| `--chart-5` | `color/chart-5` | #fe9a00 ≈ oklch(0.769 0.188 70.1) | #ff2056 ≈ oklch(0.645 0.246 16.4) | Thêm mới |
| `--sidebar-foreground` · `-primary` · `-accent` · `-border` · `-ring` | `color/sider-*` | theo `--foreground`, `--primary`, `--accent`, `--border`, `--ring` | Spartan khác shadcn ở `-primary` nền tối (Spartan #fafafa, shadcn #1447e6) | Thêm mới — chốt khi dựng Sidebar |

## 2. Chữ

| shadcn | Figma variable | Giá trị | Biến ng-zorro | Mặc định AntD | TH |
|---|---|---|---|---|---|
| `font/font-sans` (kit: Geist) | `font/family` | **Geist** (chốt 06/11 chiều, thay Inter) | `@font-family` | system font stack | Ghi đè — thiếu ký tự ₫, trình duyệt lấy font dự phòng |
| `tracking` chữ nút (shadcnuikit web) | `btn/letter-spacing` | −0.25px | — | 0 | Thêm mới — kèm `-webkit-font-smoothing: antialiased` toàn trang |
| — | `font/heading-family` | **Cal Sans** — display + heading 1–5 (chốt 06/11) | — (AntD không có font riêng cho tiêu đề) | = `@font-family` | Thêm mới — dev gắn cho `h1–h5`, `nz-typography` tiêu đề |
| `font-mono` | `font/code-family` | Geist Mono | `@code-family` | SFMono-Regular… | Ghi đè |
| `text-xs` 12/16 | `font-size/sm` · `line-height/sm` | 12 / 16 | `@font-size-sm` | 12 | 1:1 (cỡ) · dòng: Thêm mới |
| `text-sm` 14/20 | `font-size/base` | 14 | `@font-size-base` | 14 | 1:1 |
| `text-sm` dòng 20 | `line-height/base` | 20 (1.4286) | `@line-height-base` | 1.5715 (22) | **Ghi đè** |
| `text-base` 16/24 | `font-size/lg` | 16 / 24 | `@font-size-lg` | 16 | 1:1 (cỡ) |
| `text-lg` 18/28 | `font-size/xl` | 18 / 28 | — | — | Thêm mới |
| `text-xl` 20/28 | `heading/4` | 20 / 28 | `@heading-4-size` | 20 | 1:1 |
| `text-2xl` 24/32 | `heading/3` | 24 / 32 | `@heading-3-size` | 24 | 1:1 |
| `text-3xl` 30/36 | `heading/2` | 30 / 36 | `@heading-2-size` | 30 | 1:1 |
| `text-4xl` 36/40 | `heading/1` | 36 / 40 | `@heading-1-size` | 38 | Ghi đè |
| `text-5xl` 48/48 | `display/1` | 48 / 48 (Cal Sans) | — | — | Thêm mới |
| `text-6xl` 60/60 | `display/2` | 60 / 60 (Cal Sans) | — | — | Thêm mới |
| `text-base` | `heading/5` | 16 / 24 | `@heading-5-size` | 16 | 1:1 |
| `font-semibold` 600 | `font-weight/title` | **400** (Cal Sans chỉ có 1 độ đậm — để 600 trình duyệt làm đậm giả) | `@typography-title-font-weight` | 600 | Ghi đè |
| `font-medium` 500 (nút) | `font-weight/button` | 500 | `@btn-font-weight` | 400 | Ghi đè |

## 3. Bo góc

shadcn: `--radius` 10px; các cấp suy ra (`sm` = ×0.6, `md` = ×0.8, `xl` = ×1.4…). Khớp với trang Style Guide của kit.

| shadcn | Figma variable | Giá trị | Biến ng-zorro | Mặc định AntD | TH |
|---|---|---|---|---|---|
| `rounded-md` (nút, ô nhập, select) | `radius/base` | 8 | `@border-radius-base` | 2 | **Ghi đè** |
| `rounded-sm` (mục trong menu) | `radius/sm` | 6 | `@border-radius-sm` | 2 | Ghi đè |
| `rounded-lg` (card, dialog) | `radius/lg` | 10 | `@border-radius-lg` | 4 | Ghi đè |
| `rounded-xs` | `radius/xs` | 2 | — | — | Thêm mới |
| `rounded-[4px]` (checkbox) | `radius/checkbox` | 4 | biến bo góc checkbox — tên cần kiểm trong `default.less` | = border-radius-base | Ghi đè |
| `rounded-xl` · `2xl` · `3xl` · `4xl` | `radius/xl` · `2xl` · `3xl` · `4xl` | 14 · 18 · 22 · 26 | — | — | Thêm mới |
| `rounded-full` | `radius/full` | 9999 | — | — | Thêm mới |
| Ô nhập bo kit (chốt 07/11, bỏ pill) | `input/radius` | `radius/lg` 10 | `@input-border-radius` — tên cần kiểm (mặc định theo `@border-radius-base`) | 2 | Thêm mới |
| Card `border-radius/rounded-xl` (đo kit) | `card/radius` | `radius/xl` 14 | `@card-radius` | 2 | Ghi đè |
| Tag bo nhỏ (user chốt 07/11, bỏ pill) | `tag/radius` | `radius/sm` 6 | `@tag-border-radius` — tên cần kiểm | 2 | Ghi đè |

## 4. Khoảng cách

Lưới 4px của shadcn (Tailwind `1` = 4px) trùng thang padding/margin của AntD.

| shadcn | Figma variable | Giá trị | Biến ng-zorro | Mặc định AntD | TH |
|---|---|---|---|---|---|
| `1` | `spacing/xss` | 4 | `@padding-xss` · `@margin-xss` | 4 | 1:1 |
| `2` | `spacing/xs` | 8 | `@padding-xs` · `@margin-xs` | 8 | 1:1 |
| `3` | `spacing/sm` | 12 | `@padding-sm` · `@margin-sm` | 12 | 1:1 |
| `4` | `spacing/md` | 16 | `@padding-md` · `@margin-md` | 16 | 1:1 |
| `6` | `spacing/lg` | 24 | `@padding-lg` · `@margin-lg` | 24 | 1:1 |
| `0.5` · `1.5` · `5` · `8` · `10` · `12` | `spacing/2` · `6` · `20` · `32` · `40` · `48` | 2 · 6 · 20 · 32 · 40 · 48 | — | — | Thêm mới |

## 5. Chiều cao control

| shadcn | Figma variable | Giá trị | Biến ng-zorro | Mặc định AntD | TH |
|---|---|---|---|---|---|
| `h-9` (mặc định) | `height/base` | 36 | `@height-base` | 32 | **Ghi đè** |
| `h-8` (sm) | `height/sm` | 32 | `@height-sm` | 24 | Ghi đè |
| `h-10` (lg) | `height/lg` | 40 | `@height-lg` | 40 | 1:1 |
| `h-6` (xs) | `height/xs` | 24 | — | — | Thêm mới — ng-zorro chỉ có 3 cỡ, xem Mục 7.1 |
| Badge cao 20 (đo kit) | `tag/height` | 20 | `@tag-line-height` (20) | 20 | 1:1 |
| Card `Top/Left 24px` (đo kit) | `card/padding` | 24 | `@card-padding-base` | 24 | 1:1 |

## 6. Đổ bóng, focus

| shadcn | Figma variable | Giá trị | Biến ng-zorro | Mặc định AntD | TH |
|---|---|---|---|---|---|
| `shadow-xs` (checkbox) | `shadow/xs` | 0 1px 2px 0 rgb(0 0 0 / 5%) | — | — | Thêm mới — chỉ checkbox |
| Kit: nút viền, ô nhập, card không bóng | `shadow/btn` | none | `@btn-shadow` | 0 2px 0 rgba(0,0,0,.015) | Ghi đè (chốt 06/11 chiều) |
| `shadow-md` (dropdown, popover) | `shadow/base` | 0 4px 6px -1px rgb(0 0 0 / 10%), 0 2px 4px -2px rgb(0 0 0 / 10%) | `@box-shadow-base` | 3 lớp `@shadow-2` | Ghi đè |
| — | `shadow/btn-primary` | none | `@btn-primary-shadow` | 0 2px 0 rgba(0,0,0,.045) | Ghi đè |
| — | `shadow/btn-text` | none | `@btn-text-shadow` | 0 -1px 0 rgba(0,0,0,.12) | Ghi đè |
| `ring-[3px]` | `focus/width` | 3 | `@outline-width` | 2 | Ghi đè |
| `ring-ring/50` | `focus/color` | `color/ring` 50% | `@outline-fade` | 20% (trên màu chính) | Ghi đè |
| `aria-invalid:ring-destructive/20` | `focus/error-color` | `color/error` 20% (Dark 40%) | `@error-color-outline` | fade(error, 20%) | 1:1 (Light) |

## 7. Component

### 7.1 Button — `nz-button`

**Biến thể** (bám ng-zorro; shadcn chỉ quyết giao diện):

| shadcn variant | ng-zorro | TH |
|---|---|---|
| `default` | `nzType="primary"` | 1:1 |
| `outline` | `nzType="default"` (có viền) | 1:1 |
| `ghost` | `nzType="text"` | 1:1 |
| `link` | `nzType="link"` | 1:1 |
| `destructive` | `nzDanger` (kèm `primary`) | 1:1 |
| `secondary` | **không có** → class `secondary`, nền `color/bg-base` | Thêm mới (chốt 06/11) |
| — | `nzType="dashed"` | Không dùng (chốt 06/11) |
| size `sm` · `default` · `lg` | `nzSize="small"` · `default` · `large` | 1:1 |
| size `xs`, `icon-xs` | **không có** → class `xs` | Thêm mới (chốt 06/11) |
| `icon` · `icon-sm` · `icon-lg` | nút chỉ icon (`nzShape` mặc định, chỉ có icon) | 1:1 |
| — | `nzBlock` · `nzLoading` | Dùng (chốt 06/11) |
| — | `nzShape="circle"` · `"round"` · `nzGhost` | Không dùng (chốt 06/11) |

**Token:**

| shadcn | Figma variable | Giá trị | Biến ng-zorro | Mặc định AntD | TH |
|---|---|---|---|---|---|
| `h-9` / `h-8` / `h-10` | `btn/height/base·sm·lg` | 36 / 32 / 40 | `@btn-height-base·sm·lg` | 32 / 24 / 40 | Theo `height/*` |
| `px-3` (chốt 06/11 chiều; kit h-8 dùng `spacing/2-5`) | `btn/padding-x/base` | 12 | `@btn-padding-horizontal-base` | 15 | Ghi đè — dev nhập 11 |
| `spacing/2-5` (sm) | `btn/padding-x/sm` | 10 | `@btn-padding-horizontal-sm` | 7 | Ghi đè — dev nhập 9 |
| `px-4` (lg) | `btn/padding-x/lg` | 16 | `@btn-padding-horizontal-lg` | 15 | 1:1 (dev nhập 15) |
| `has-[>svg]` | `btn/padding-x-icon/base·sm·lg` | 12 / 10 / 16 | — | — | Thêm mới — đo lại khi dựng Button |
| `spacing/1-5` · xs `spacing/1` (đo kit) | `btn/gap` · `btn/gap-xs` | 6 / 4 | — (AntD: lề icon 8px, không có biến) | 8 | Ghi đè (CSS) |
| `text-sm` mọi cỡ | `btn/font-size/base·sm·lg` | 14 / 14 / 14 | `@btn-font-size-sm` · `@btn-font-size-lg` | 14 / 16 | 1:1 sm · Ghi đè lg |
| `border-radius/rounded-md` (đo kit) | `btn/radius` | `radius/base` 8 | `@btn-border-radius-base` · `-sm` | 2 / 2 | Ghi đè |
| `size-4` icon | `btn/icon-size` | 16 | `@btn-square-only-icon-size` | 16 | 1:1 |
| State Hover | `color/primary-hover` | Mục 1.1 | `@primary-color-hover` | — | Ghi đè |
| State Pressed | `opacity/pressed` | 0.6 | `@primary-color-active` (quy đổi) | — | Ghi đè |
| `hover:bg-accent` (outline, ghost) | `color/item-hover-bg` | #f5f5f5 | `@btn-text-hover-bg` | đen 1.8% | Ghi đè |
| `bg-background` + `border` | `color/body-bg`, `color/border-base` | — | `@btn-default-bg` · `@btn-default-border` | — | Theo màu |

**Nút trượt xác nhận** (`slide-confirm`, component mới — ng-zorro không có; spec `components/button.md` Mục 6):

| Nguồn | Figma variable | Giá trị | Biến ng-zorro | Mặc định AntD | TH |
|---|---|---|---|---|---|
| bencho.dev (rãnh) | `slide/height` | 56 | — | — | Thêm mới |
| — | `slide/padding` | 4 | — | — | Thêm mới |
| — | `slide/grip-size` | 48 (= 56 − 2 × 4) | — | — | Thêm mới |
| Bo rãnh (chốt 06/11) | `slide/radius` | `radius/2xl` 18 | — | — | Thêm mới |
| Đồng tâm | `slide/grip-radius` | `radius/xl` 14 (= `slide/radius` − `slide/padding`) | — | — | Thêm mới |

### 7.2 Input — `nz-input`

| shadcn | Figma variable | Giá trị | Biến ng-zorro | Mặc định AntD | TH |
|---|---|---|---|---|---|
| `h-9` | `input/height/base` (sm, lg theo `height/*`) | 36 | `@input-height-base·sm·lg` | 32 / 24 / 40 | Theo `height/*` |
| `px-3` | `input/padding-x` | 12 | `@input-padding-horizontal-base` | 11 | Ghi đè — không viền nên dev nhập 12 |
| `py-1` | `input/padding-y` | 4 | `@input-padding-vertical-base` | 4 (tự tính từ chiều cao) | Ghi đè — cao 36 + dòng 20 → AntD tự tính ra 7, cần ghi tay nếu muốn khớp |
| `text-base` (< 768px) · `md:text-sm` | `input/font-size` | 16 mobile / 14 web | `@font-size-base` | 14 | Thêm mới (mobile 16 để iOS không tự zoom) |
| Không bóng | — | — | — | — | 1:1 (AntD ô nhập không bóng) |
| Không viền | `color/input-border` | trong suốt | `@input-border-color` | — | Ghi đè |
| Nền xám (shadcnuikit web) | `color/input-bg` | Light #f2f2f2 · Dark trắng 4.5% | `@input-bg` | = component-bg | Ghi đè |
| Bo kit | `input/radius` | `radius/lg` 10 | Mục 3 | 2 | Thêm mới |
| `rounded-lg` (ô nhiều dòng, kit) | `textarea/radius` | `radius/lg` 10 | `@textarea-border-radius` — tên cần kiểm | 2 | Thêm mới (chốt 06/11 tối) |
| Ô hợp lệ web-05: nền trắng, viền xanh | `color/input-success-border` | = `color/success` (Light/Dark) · nền `color/body-bg` | `@success-color` qua class `success` | — | Thêm mới — ng-zorro không có `nzStatus="success"` |

### 7.3 Select — `nz-select`

| shadcn | Figma variable | Giá trị | Biến ng-zorro | TH |
|---|---|---|---|---|
| Trigger: `h-9` · sm `h-8`, `px-3`, `gap-2`, `rounded-md`, `shadow-xs` | theo Input | 36 / 32, 12, 8, 8 | `@select-*` + `@input-*` — tên cần kiểm | Theo Input |
| Mũi tên `size-4 opacity-50` | `select/arrow-size` · `select/arrow-opacity` | 16 · 50% | — | Thêm mới (độ mờ) |
| Menu: `rounded-md border shadow-md`, `p-1`, rộng tối thiểu 128 | `select/dropdown-padding` | 4 | `@select-dropdown-*` — tên cần kiểm | Ghi đè / Thêm mới |
| Menu bo `rounded-md` · rộng tối thiểu `min-w-[8rem]` | `select/dropdown-radius` · `select/dropdown-min-width` | `radius/base` 8 · 128 | — | Thêm mới (chốt 07/11) |
| Mục: `py-1.5 pl-2 pr-8 rounded-sm text-sm` | `select/item-padding-y·x` | 6 · 8 (phải 32 chừa dấu ✓) | `@select-dropdown-vertical-padding` … — tên cần kiểm | Ghi đè |
| Mục `pr-8` · `rounded-sm` | `select/item-padding-right` · `select/item-radius` | 32 · `radius/sm` 6 | — | Thêm mới (chốt 07/11) |
| Mục chọn: `focus:bg-accent`, dấu ✓ bên phải | `color/item-hover-bg` | #f5f5f5 | `@select-item-selected-bg` | Ghi đè (AntD nền xanh nhạt, không có ✓) |

### 7.4 Checkbox — `nz-checkbox`

| shadcn | Figma variable | Giá trị | Biến ng-zorro | Mặc định AntD | TH |
|---|---|---|---|---|---|
| `size-4` | `checkbox/size` | 16 | `@checkbox-size` | 16 | 1:1 |
| `rounded-[4px]` | `radius/checkbox` | 4 | `@checkbox-border-radius` | = `@border-radius-sm` 2 | Ghi đè |
| `checked: bg-primary border-primary` | `color/primary` | #171717 | `@checkbox-check-bg` / theo primary | — | 1:1 (theo primary) |
| Dấu ✓ `size-3.5` | `checkbox/check-size` | 14 | — | — | Thêm mới |
| `shadow-xs` | `shadow/xs` | Mục 6 | — | — | Thêm mới |
| `text-primary-foreground` (dấu ✓) | `color/primary-foreground` | #fafafa | `@checkbox-check-color` | #fff | 1:1 |
| `border-input` (ô chưa chọn) | `color/border-base` · `color/body-bg` | #e5e5e5 · #fff | `@border-color-base` | #d9d9d9 | Ghi đè — không dùng `color/input-border` vì biến đó trong suốt (ô nhập không viền) |
| gạch "một phần" (Radix `MinusIcon` / CSS 8×2) | `checkbox/indeterminate-width` · `checkbox/indeterminate-height` | 8 × 2 | — (AntD ô vuông 8×8) | 8 × 8 | Ghi đè |
| `gap-2` ô ↔ nhãn | `checkbox/gap` → `spacing/xs` | 8 | `@checkbox-group-item-margin-right` | 8 | 1:1 (nhóm ngang dùng 16) |
| `pl-6` mục con / ô mở thêm | `checkbox/indent` → `spacing/lg` | 24 | — | — | Thêm mới |
| thẻ chọn `p-3` `rounded-lg` | `checkbox/card-padding` → `spacing/sm` · `radius/lg` | 12 · 10 | — | — | Thêm mới — đã chọn viền 2px `color/primary` |
| `focus-visible:ring-[3px]` · `aria-invalid:ring-destructive/20` | `focus/width` · `color/focus-ring` · `color/focus-error-ring` | 3 · #a1a1a1 50% · đỏ 20% | `@outline-width` · `@outline-color` | 2 · primary | Ghi đè (theo Mục 6) |
| `disabled:opacity-50` | `opacity/disabled` | 50% | — | — | Theo 8.1 #1 |
| web-04 ô tròn `bg-emerald-500` | `color/success` · `color/error-foreground` | #52c41a · #fff | `@success-color` | #52c41a | Chỉ Checkbox tròn |

### 7.5 Radio — `nz-radio`

| shadcn | Figma variable | Giá trị | Biến ng-zorro | Mặc định AntD | TH |
|---|---|---|---|---|---|
| `size-4` | `radio/size` | 16 | `@radio-size` | 16 | 1:1 |
| `size-2` chấm | `radio/dot-size` | 8 | `@radio-dot-size` | 16 − 8 = 8 | 1:1 |
| `border-input` (#e5e5e5) | `color/border-base` | #e5e5e5 · Dark trắng 10% | `@border-color-base` | #d9d9d9 | Theo màu (không dùng `color/input-border` vì biến này trong suốt) |
| `fill-primary` chấm, viền chọn | `color/primary` | #171717 · Dark #e5e5e5 | `@radio-dot-color` · `@radio-solid-checked-color` — tên cần kiểm | theo primary | 1:1 (theo primary) |
| `shadow-xs` | `shadow/xs` | Mục 6 | — | — | Thêm mới |
| `gap-2` nhãn · mô tả cách 2 | `radio/gap` · `radio/desc-gap` | 8 · 2 | `@radio-wrapper-margin-right` — tên cần kiểm | 8 | 1:1 · Thêm mới |
| Nhóm nút (ng-zorro) | `radio/button-padding-x` | 15 (+ viền 1 = 16) | `@radio-button-padding-horizontal` | 15 | 1:1 |
| Nhóm nút cao · bo | `height/base` · `radius/base` | 36 · 8 | `@btn-height-base` · `@border-radius-base` | 32 · 2 | Theo Button |
| Nền nút | `color/body-bg` | #fff · Dark #0a0a0a | `@radio-button-bg` | = btn-default-bg | 1:1 |
| Thẻ chọn `p-3 rounded-lg` | `radio/card-padding` · `radius/lg` | 12 · 10 | — | — | Thêm mới |
| Ô màu `size-6` | `radio/swatch-size` | 24 | — | — | Thêm mới |
| Thẻ/ô đã chọn `border-primary` + `ring-1` | `color/primary` (viền 1 + bóng tràn 1) | 2px tổng | — | — | Thêm mới (CSS) |
| Focus · lỗi | `focus/width` · `color/focus-ring` · `color/focus-error-ring` | 3 · xám 50% · đỏ 20% | — (AntD dùng bóng xanh) | — | Ghi đè (CSS) |
| Vòng cảnh báo (Input, Textarea) | `color/focus-warning-ring` | cam 20% (Dark 40%) | `@warning-color-outline` — tên cần kiểm | 2 | Thêm mới 07/11 (trước gắn `color/warning` + độ mờ 20% → instance mất độ mờ, vòng đặc) |
| Tắt | `opacity/disabled` | 50% | — | — | Ghi đè (CSS riêng, quy tắc 4) |

### 7.6 Switch — `nz-switch`

| shadcn | Figma variable | Giá trị | Biến ng-zorro | Mặc định AntD | TH |
|---|---|---|---|---|---|
| Rãnh (hình trang duyệt; web dùng `h-5 w-11`) | `switch/width` · `switch/height` | 32 · 18 | `@switch-min-width` · `@switch-height` | 44 · 22 | Ghi đè (chốt 07/11) |
| Rãnh nhỏ | `switch/width-sm` · `switch/height-sm` | 24 · 14 | `@switch-sm-min-width` · `@switch-sm-height` | 28 · 16 | Ghi đè (chốt 07/11) |
| Nút tròn `size-4` (theo hình: 14 / 10) | `switch/handle-size` · `switch/handle-size-sm` | 14 · 10 | `@switch-pin-size` · `@switch-sm-pin-size` | = cao − 4 | 1:1 (theo công thức) |
| Khe nút ↔ rãnh | `switch/padding` → `spacing/2` | 2 | `@switch-padding` | 2 | 1:1 |
| `rounded-full` | `switch/radius` → `radius/full` | 9999 | — | bo tròn | 1:1 |
| `data-[state=checked]:bg-primary` | `switch/track-checked-bg` → `color/primary` | #171717 | `@switch-color` | `@primary-color` | 1:1 (theo primary) |
| `data-[state=unchecked]:bg-input` | `switch/track-bg` → `color/border-base` | #e5e5e5 (Dark trắng 10%) | — (`@disabled-color`) | đen 25% | Ghi đè bằng CSS |
| Nút `bg-background` (Dark: tắt `bg-foreground`, bật `bg-primary-foreground`) | `switch/handle-bg` · `switch/handle-checked-bg` | trắng (Dark: `color/text` · `color/primary-foreground`) | `@switch-bg` | trắng | Ghi đè (Dark) |
| `shadow-xs` rãnh · bóng nút | `shadow/xs` · (nút: 0 1 2 đen 20%, chưa có token) | Mục 6 | `@switch-shadow-color` | xanh đậm 20% | Thêm mới |
| `disabled:opacity-50` | `opacity/disabled` | 50% | `@switch-disabled-opacity` | 0.4 | Ghi đè |
| Đang lưu (`nzLoading`) | `switch/loading-opacity` · `switch/spinner-size` · `switch/spinner-size-sm` | 60% · 10 · 8 | — | — | Thêm mới |
| `focus-visible:ring-[3px]` | `focus/width` · `color/focus-ring` | 3 · xám 50% | — | — | Theo Input |

### 7.7 Tag — `nz-tag`

| shadcn | Figma variable | Giá trị | Biến ng-zorro | Mặc định AntD | TH |
|---|---|---|---|---|---|
| Badge `px-2` · `gap-1` | `tag/padding-x` · `tag/gap` | 8 (→ `spacing/xs`) · 4 (→ `spacing/xss`) | `@tag-padding-horizontal` — tên cần kiểm | 7 + viền 1 | Ghi đè (Tô nhạt không viền → 8; Viền 8 − 1) |
| `text-xs font-medium` | `text/sm/medium` | 12/16 Medium | `@tag-font-size` | 12, 400 | Ghi đè độ đậm |
| `secondary` | `color/bg-base` · `color/text` | #f5f5f5 · #0a0a0a | `@tag-default-bg` · `@tag-default-color` | #fafafa, có viền | Ghi đè |
| `outline` | `color/component-bg` · `color/border-base` | #fff · #e5e5e5 | `nzBordered` | — | 1:1 |
| — (Tô nhạt success) | `tag/success-bg` · `tag/success-fg` | #389e0d 10% · #389e0d / Dark #49aa19 20% · #6abe39 | `@success-color-deprecated-bg` — tên cần kiểm | #f6ffed + viền | Thêm mới (CSS riêng `.ant-tag-success`, bỏ viền) |
| — (processing) | `tag/info-bg` · `color/info` | #155dfc 10% / Dark #2b7fff 20% | `@info-color-deprecated-bg` — tên cần kiểm | #e6f7ff | Thêm mới |
| — (warning) | `tag/warning-bg` · `tag/warning-fg` | #d48806 10% · #d48806 / Dark #d89614 20% · #e8b339 | `@warning-color-deprecated-bg` — tên cần kiểm | #fffbe6 | Thêm mới |
| `destructive` (bg-destructive/10) | `color/error-bg` · `color/error` | Mục 2 | `@error-color-deprecated-bg` — tên cần kiểm | #fff2f0 | Ghi đè (dùng chung nút xoá nhạt) |
| chấm `size-1.5` | `tag/dot-size` · màu `color/success\|info\|warning\|error\|text-secondary` | 6 | `@badge-status-size` | 6 | 1:1 |
| icon `size-3` · `opacity-60` | `tag/icon-size` · `tag/icon-opacity` | 12 · 60% | — | — | Thêm mới |
| số đếm `min-w-5 rounded-full` | `tag/count-min-width` · `tag/count-sm-size` · `color/primary` | 20 · 18 · #171717 | `@badge-height` · `@badge-height-sm` · `@badge-color` | 20 · 14 · đỏ | Ghi đè (sm, màu) |
| checkable | `color/primary` · `color/primary-foreground` · `color/item-hover-bg` | #171717 · #fafafa · #f5f5f5 | `@tag-checkable…` — tên cần kiểm (theo primary) | primary | 1:1 (theo primary) |

### 7.8 Tooltip — `nz-tooltip`

| shadcn | Figma variable | Giá trị | Biến ng-zorro | Mặc định AntD | TH |
|---|---|---|---|---|---|
| `bg-primary text-primary-foreground` | `color/primary` · `color/primary-foreground` | #171717 · #fafafa (Dark #e5e5e5 · #171717) | `@tooltip-bg` · `@tooltip-color` | rgba(0,0,0,.75) · #fff | Ghi đè (+ theme tối) |
| `rounded-md` (hình kit) | `tooltip/radius` | `radius/base` 8 | `@tooltip-border-radius` | = border-radius-base (2) | Ghi đè |
| `px-3 py-1.5` | `tooltip/padding-x` · `tooltip/padding-y` | 12 · 6 | — (CSS `.ant-tooltip-inner`) | 8 · 6, min-height 32 | Ghi đè CSS |
| `text-xs` | `text/sm/regular` | 12 / 16 | — (CSS `.ant-tooltip-inner`) | 14 / 22 | Ghi đè CSS |
| `sideOffset` 8 | `tooltip/offset` | `spacing/xs` 8 | `@tooltip-distance` — tên cần kiểm | ≈ 14 (mũi tên − 1 + 4) | Ghi đè |
| Mũi tên: vuông `size-2` xoay 45° | — (vector 10 × 5 trên Figma) | nhô ≈ 5 | `@tooltip-arrow-width` | 8√2 | Ghi đè |
| Mẫu danh sách chỉ số (web-03) | `tooltip/rich-width` · `tooltip/rich-padding` · `tooltip/rich-gap` | 180 · 12 · 8 | — | — | Thêm mới |
| Rộng tối đa | — | 250 | `@tooltip-max-width` | 250 | 1:1 |

### 7.9 Breadcrumb — `nz-breadcrumb`

| shadcn | Figma variable | Giá trị | Biến ng-zorro | Mặc định AntD | TH |
|---|---|---|---|---|---|
| `text-muted-foreground` (mục link) | `color/text-secondary` | #737373 · Dark #a1a1a1 | `@breadcrumb-link-color` · `@breadcrumb-separator-color` | 45% đen | Ghi đè |
| `text-foreground` (trang hiện tại) · `hover:text-foreground` | `color/text` | #171717 | `@breadcrumb-last-item-color` · `@breadcrumb-link-color-hover` | 85% đen · primary (tên cần kiểm) | Ghi đè |
| `text-sm` | `text/base/regular` | 14 / 20 | `@breadcrumb-font-size` | 14 | 1:1 |
| `sm:gap-2.5` · `gap-1.5` (< 640px) | `breadcrumb/gap` | 10 (mobile 6) | `@breadcrumb-separator-margin` | 0 8px | Ghi đè |
| Mục `gap-1.5` (icon + chữ) | `breadcrumb/item-gap` | `spacing/6` 6 | — | — | Thêm mới |
| Separator `[&>svg]:size-3.5` (ChevronRight) | `breadcrumb/separator-size` | 14 | `nzSeparator` = TemplateRef icon `right` | "/" | Ghi đè |
| Icon mục `size={16}` | `breadcrumb/icon-size` | 16 | `@breadcrumb-icon-font-size` | 14 | Ghi đè |
| Ellipsis `size-5`, icon `size-4` | `breadcrumb/ellipsis-size` | 20 | — | — | Thêm mới |
| `focus-visible:ring` quanh link | `breadcrumb/link-radius` · `focus/width` · `color/focus-ring` | `radius/xs` 2 · 3 | — | — | Thêm mới |
| DropdownMenu của "…" | `breadcrumb/menu-min-width` + `select/dropdown-*` | 128 · padding 4 · bo 8 · `shadow/base` | `@dropdown-*` — tên cần kiểm | — | Theo Select |

### 7.10 Card — `nz-card`

| shadcn | Figma variable | Giá trị | Biến ng-zorro | Mặc định AntD | TH |
|---|---|---|---|---|---|
| `rounded-xl` (đo kit) | `card/radius` | `radius/xl` 14 | `@card-radius` | 2 | Ghi đè (đã có Mục 3) |
| `py-6 px-6` | `card/padding` | 24 | `@card-padding-base` | 24 | 1:1 (đã có Mục 5) |
| `data-[size=sm]:py-4 px-4` | `card/padding-sm` | `spacing/md` 16 | `@card-padding-base-sm` — tên cần kiểm | 12 | Ghi đè |
| `gap-6` · sm `gap-4` | `card/gap` · `card/gap-sm` | 24 · 16 | — | — | Thêm mới |
| `CardHeader gap-1.5` | `card/header-gap` | `spacing/6` 6 | — | — | Thêm mới |
| `CardFooter` nút `gap-2` | `card/footer-gap` | `spacing/xs` 8 | — | — | Thêm mới (thay `nzActions`) |
| `bg-card` | `color/component-bg` | #ffffff · Dark #171717 | `@card-background` | #fff | 1:1 (Light) |
| `border` | `color/border-base` | #e5e5e5 · Dark trắng 10% | viền `.ant-card-bordered` — tên cần kiểm | #f0f0f0 | Ghi đè |
| card không bóng; hover đổi viền | `color/input-hover-border` | #a1a1a1 · Dark trắng 30% | `@card-shadow` | bóng 3 lớp | Ghi đè: bỏ bóng, hover đổi viền |
| `CardTitle font-semibold` | `text/lg/semibold` · sm `text/base/semibold` | 16 · 14, đậm 600 | `@card-head-font-size` · `-sm` | 16 · 14 | Ghi đè độ đậm |
| đầu card không vạch kẻ | — | không `border-bottom`, không chiều cao đầu riêng | `@card-head-height` · `@card-head-padding` | 48 · 16 | Ghi đè |

### 7.11 Kbd — `<kbd>` (ng-zorro không có)

| shadcn | Figma variable | Giá trị | Biến ng-zorro | Mặc định AntD | TH |
|---|---|---|---|---|---|
| `h-5` | `kbd/height` | 20 | — (ng-zorro không có Kbd) | — | Thêm mới |
| `min-w-5` | `kbd/min-width` | 20 | — | — | Thêm mới |
| `px-1` | `kbd/padding-x` | 4 | — | — | Thêm mới |
| `gap-1` (KbdGroup) | `kbd/gap` | 4 | — | — | Thêm mới |
| `rounded-sm` | `kbd/radius` | = `radius/sm` 6 | — | — | Thêm mới |
| `bg-muted` | `kbd/bg` | = `color/input-bg` (#f2f2f2; Dark trắng 4,5%) | — | — | Thêm mới (không dùng `item-hover-bg` vì trùng nền dòng menu hover) |
| `text-muted-foreground` | `kbd/fg` | = `color/text-secondary` | — | — | Thêm mới |
| `bg-background/20` trong tooltip | `kbd/on-dark-bg` | `color/primary-foreground` alpha 20% | — | — | Thêm mới |
| `text-background` trong tooltip | `kbd/on-dark-fg` | = `color/primary-foreground` | — | — | Thêm mới |
| `text-xs font-medium` | text style `text/sm/medium` | Geist Medium 12/16 | — | — | Dùng lại |

### 7.12 Label — `nz-form-label`

| shadcn | Figma variable | Giá trị | Biến ng-zorro | Mặc định AntD | TH |
|---|---|---|---|---|---|
| `text-sm leading-none font-medium` (theo mẫu ghép Input/Select: base 14/20) | `color/text` · `text/base/medium` | #171717 · 14/20 Medium | `@label-color` (= `@heading-color`) — tên cần kiểm | #000 85% | Ghi đè (theo token) |
| `*` bắt buộc (`text-destructive`) | `color/error` | đỏ báo lỗi | `@form-required-mark-color` — tên cần kiểm | `@highlight-color` | 1:1, nhưng đặt `*` sau chữ (AntD đặt trước) |
| chữ "(không bắt buộc)", `FieldDescription`, icon ⓘ | `color/text-secondary` · `text/sm/regular` | xám phụ, 12/16 | `@form-help-color` — tên cần kiểm | — | Thêm mới (chữ phụ không có trong ng-zorro) |
| `gap` giữa chữ, `*`, chữ phụ, icon | `label/gap` → `spacing/xss` | 4 | — | — | Thêm mới |
| nhãn ↔ ô `gap-2` | `label/field-gap` → `spacing/6` | 6 | `@form-vertical-label-padding` | 0 0 8px | Ghi đè (6, khớp Input/Select) |
| Nhãn trái: nhãn ↔ cột ô | `label/column-gap` → `spacing/md` | 16 | `nz-col` gutter | — | Thêm mới |
| Nhãn trái: cột nhãn cố định | `label/column-width` | 120 | `nz-col nzSpan` | — | Thêm mới |
| icon ⓘ | `icon/info` 16 + `color/text-secondary` | 16 | `nzTooltipIcon` | — | Dùng lại |
| `peer-disabled:opacity-50` | `opacity/disabled` | 50% | — | — | Theo 8.1 #1 |
| lỗi `FieldError` | `color/error` · `text/sm/regular` | 12/16 | `@form-error-color` — tên cần kiểm | `@error-color` | 1:1 |

### 7.13 Popover — `nz-popover` · `nz-popconfirm`

| shadcn | Figma variable | Giá trị | Biến ng-zorro | Mặc định AntD | TH |
|---|---|---|---|---|---|
| `w-72` | `popover/width` | 288 | `@popover-min-width` — tên cần kiểm (rộng đặt qua `nzPopoverOverlayClassName`) | 177 (tối thiểu) | Thêm mới |
| `p-4` | `popover/padding` | `spacing/md` 16 | `@popover-padding-horizontal` + CSS `.ant-popover-inner-content` | 16 · dọc 12 | Ghi đè |
| `space-y-2` (tiêu đề ↔ nội dung) | `popover/gap` | `spacing/xs` 8 | — (AntD có vạch dưới tiêu đề, bỏ) | — | Thêm mới |
| `rounded-md` | `popover/radius` | `radius/base` 8 | `@border-radius-base` (Mục 3) | 2 | Ghi đè |
| `bg-popover border shadow-md` | `color/popover-bg` · `color/border-base` · `shadow/base` | Mục 1.3 · 1.4 · 6 | `@popover-bg` · CSS border 1px · `@box-shadow-base` | = component-bg · không viền | 1:1 / Thêm mới (viền) |
| `sideOffset` | `popover/offset` | `tooltip/offset` 8 | `@popover-distance` — tên cần kiểm | arrow-width + 4 | Ghi đè |
| Mũi tên (shadcn không có) | — (vector) | 10 × 5, nền popover-bg, 2 cạnh viền border-base | `@popover-arrow-width` — tên cần kiểm | 6 | Ghi đè |

### 7.14 Slider — `nz-slider`

| shadcn | Figma variable | Giá trị | Biến ng-zorro | Mặc định AntD | TH |
|---|---|---|---|---|---|
| Track `h-1.5` | `slider/rail-height` | 6 | — (CSS `.ant-slider-rail` / `-track` `height: 4px`) | 4 | Thêm mới (ghi đè CSS) |
| Track `bg-muted` | `slider/rail-bg` | `switch/track-bg` → `color/border-base` | `@slider-rail-background-color` (+ `-hover` #e1e1e1) | `@background-color-base` | Ghi đè |
| Range `bg-primary` | `slider/track-bg` | `color/primary` | `@slider-track-background-color` (+ `-hover`) | `@primary-3` / `@primary-4` | Ghi đè |
| Thumb `size-4` | `slider/handle-size` | 16 | `@slider-handle-size` · `@slider-handle-margin-top` | 14 · −5 | Ghi đè (margin −5 giữ 1:1) |
| Thumb `bg-white` | `slider/handle-bg` | `color/body-bg` | `@slider-handle-background-color` | `@component-background` | 1:1 |
| Thumb `border border-primary` | `slider/handle-border` · `slider/handle-border-width` | `color/primary` · 1 | `@slider-handle-color` · `@slider-handle-border-width` | `@primary-3` · 2px | Ghi đè |
| `rounded-full` | `slider/radius` | `radius/full` | — | — | Thêm mới |
| Thumb `shadow-sm` | `shadow/xs` | Mục 6 | `@slider-handle-shadow` | 0 | Ghi đè |
| `hover:ring-4 ring-ring/50` | `slider/handle-ring-width` · `color/focus-ring` | 4 · xám 50% | `@slider-handle-color-focus-shadow` | `0 0 0 5px fade(primary, 12%)` | Ghi đè |
| `focus-visible:ring-4` | `focus/width` · `color/focus-ring` | 3 · xám 50% | `@slider-handle-color-focus` | `tint(primary, 20%)` | Ghi đè (theo Input) |
| Tooltip giá trị | `slider/tooltip-offset` | 4 | — | — | Thêm mới |
| Ticks `bg-muted-foreground/70`, `mt-3`, `text-xs` | `slider/mark-color` · `slider/mark-gap` | `color/text-secondary` · `spacing/sm` 12 | `@slider-dot-border-color` | `@border-color-split` | Ghi đè (AntD dùng chấm trên rãnh) |
| `disabled:opacity-50` | `opacity/disabled` | 50% | `@slider-disabled-color` · `@slider-disabled-background-color` | đổi màu xám | Ghi đè |

### 7.15 Sidebar — `nz-sider` + `nz-menu` inline

| shadcn | Figma variable | Giá trị | Biến ng-zorro | Mặc định AntD | TH |
|---|---|---|---|---|---|
| `--sidebar` | `color/sider-bg` (có sẵn) | #fafafa / Dark #171717 | `@layout-sider-background` · `@menu-bg` | #001529 · #fff | Ghi đè |
| `--sidebar-foreground` | `color/sider-text` → `color/text` | #0a0a0a / #fafafa | `@menu-item-color` | text 85% | Ghi đè |
| `hover:bg-sidebar-accent` | `color/sider-item-hover-bg` → `color/item-hover-bg` | #f5f5f5 / #262626 | — (AntD hover chỉ đổi màu chữ) | — | Thêm mới (CSS) |
| `data-[active]:bg-sidebar-accent` | `color/sider-item-active-bg` → `color/item-active-bg` | #f5f5f5 / #262626 | `@menu-item-active-bg` | primary-1 | Ghi đè |
| `--sidebar-accent-foreground` | `color/sider-item-active-text` → `color/accent-foreground` | #171717 / #fafafa | `@menu-highlight-color` | primary | Ghi đè |
| `text-sidebar-foreground/70` (tiêu đề nhóm) | `color/sider-group-title` → `color/text-secondary` | #737373 / #a1a1a1 | `@menu-item-group-title-color` | text-color-secondary | 1:1 |
| `--sidebar-border` | `color/sider-border` → `color/border-split` | #e5e5e5 / trắng 10% | `@border-color-split` | — | Theo màu |
| `--sidebar-primary` · `-foreground` (logo) | `color/sider-primary` · `-foreground` → `color/primary` · `-foreground` | #171717 / Dark #e5e5e5 | — | — | Thêm mới — Dark theo Spartan, không theo shadcn #1447e6 |
| `--sidebar-width` 16rem | `sidebar/width` | 256 | `nzWidth` | 200 | Ghi đè |
| `--sidebar-width-icon` 3rem | `sidebar/collapsed-width` | 48 | `nzCollapsedWidth` · `@menu-collapsed-width` | 80 | Ghi đè |
| `h-8` | `sidebar/item-height` → `height/sm` | 32 | `@menu-item-height` · `@menu-inline-toplevel-item-height` | 40 | Ghi đè |
| `size="lg"` `h-12` (đầu, chân) | `sidebar/item-height-lg` | 48 | — | — | Thêm mới |
| `h-7` (menu-sub-button) | `sidebar/sub-item-height` | 28 | — (CSS cấp con) | 40 | Thêm mới (CSS) |
| `p-2` | `sidebar/item-padding` → `spacing/xs` | 8 | `@menu-item-padding-horizontal` | 20 | Ghi đè |
| `gap-2` | `sidebar/item-gap` → `spacing/xs` | 8 | `@menu-icon-margin-right` | 10 | Ghi đè |
| `rounded-md` | `sidebar/item-radius` → `radius/base` | 8 | — (CSS `.ant-menu-item`) | 0 | Thêm mới |
| `gap-1` (menu) | `sidebar/menu-gap` → `spacing/xss` | 4 | `@menu-item-vertical-margin` | 4 | 1:1 |
| `p-2` (group / header / footer) | `sidebar/group-padding` → `spacing/xs` | 8 | `@menu-item-boundary-margin` | 8 | 1:1 |
| `mx-3.5` | `sidebar/sub-indent` | 14 | `nzInlineIndent` | 24 | Ghi đè |
| `px-2.5 border-l` (menu-sub) | `sidebar/sub-padding-x` | 10 | — | — | Thêm mới (CSS viền trái) |
| `[&>svg]:size-4` | `sidebar/icon-size` | 16 | `@menu-icon-size` | 14 | Ghi đè |
| `size-8 rounded-lg` (logo, ảnh) | `sidebar/logo-size` → `height/sm` · `sidebar/logo-radius` → `radius/lg` | 32 · 10 | — | — | Thêm mới |
| `text-xs font-medium` (tiêu đề nhóm) | `text/sm/medium` | 12/16 | `@menu-item-group-title-font-size` | 14 | Ghi đè |
| `data-[active]:font-medium` | `text/base/medium` | 14/20 | — | — | Thêm mới (CSS) |

> Mục 7.9 – 7.15 ghi 07/11 cho bản **dựng tạm theo đề xuất** (chưa qua trang chọn biến thể) — có thể đổi sau khi user duyệt.

> Mục 7.4 (bổ sung) – 7.8 ghi 07/11 theo đề xuất của agent dựng từng component; tên biến Less "tên cần kiểm" chưa đối chiếu `default.less`.

## 8. Đã chốt

### 8.1 06/11 sáng (trang duyệt foundations)

| # | Câu hỏi | Chốt |
|---|---|---|
| 1 | Trạng thái tắt | **Mờ 50% như shadcn** — `opacity/disabled` 0.5, dev viết CSS riêng cho từng component |
| 2 | Màu info khi màu chính đen | **Xanh Tailwind** #155dfc (Dark #2b7fff), ghi đè cả `@processing-color` |
| 3 | Nhấn nút / hover ô nhập | **Có phản hồi** — nhấn #454545 (Dark #b8b8b8), viền hover #a1a1a1 (Dark trắng 30%) |
| 4 | Nền trang, header | **Trắng như shadcn**, header trắng có viền dưới |
| 5 | Success / warning nền tối | **Bản dịu Ant Design** #49aa19 · #d89614 |
| — | Màu · Kích thước · Đổ bóng | Đồng ý như bảng |
| — | Chữ | Display + heading **Cal Sans**, chữ thường **Inter**, code giữ **Geist Mono** |

Trang duyệt: claude.ai/artifact/XV5xq5YFK21sKFLWHtGTGb · nguồn `design-system-antd/_review/foundations-review.src.html`.

Dòng "Chữ" và "Nhấn nút #454545" ở trên đã được thay ở 8.2.

### 8.2 06/11 chiều (trang so sánh 3 foundation + trang font)

| # | Câu hỏi | Chốt |
|---|---|---|
| 1 | Lấy nền tảng nào | **B — shadcnuikit Figma kit**, trộn các dòng dưới |
| 2 | Chữ thường | **Geist** (thay Inter) |
| 3 | Nút | bo 8, cao 36 · 32 · 40, padding ngang 12 (sm 10, lg 16), gap 6, chữ −0.25px |
| 4 | Ô nhập | nền #f2f2f2, không viền, bo pill (kiểu shadcnuikit web) |
| 5 | Nút xoá | đỏ nhạt: nền 10%, chữ đỏ, hover 20% |
| 6 | Nhấn nút | theo kit: cả nút mờ 60%, bỏ màu #454545 |
| 7 | Card · tag | đo kit: card bo 14, pad 24, không bóng · tag pill cao 20 |

Trang: claude.ai/artifact/Qj8jL1PeqzTCJC2tU9SKWr · claude.ai/artifact/WTpcYA2VQsNsdjS9xRuf17.

## 9. Cần kiểm thêm (máy chưa đọc được)

- Tên biến Less của **select**, **checkbox** (bo góc) trong `default.less` — bảng ghi "tên cần kiểm".
- Kích thước của Spartan nằm trong file style riêng (nova/vega/lyra/maia/mira/luma) — chưa đọc; bảng đang theo shadcn new-york-v4.
- Phiên bản ng-zorro dev đang dùng thực tế, và dev chỉnh theme qua Less hay dynamic theme (`ng-zorro-antd.variable.min.css`).
