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
| Ô nhập pill (shadcnuikit web) | `input/radius` | `radius/full` | `@input-border-radius` — tên cần kiểm (mặc định theo `@border-radius-base`) | 2 | Thêm mới |
| Card `border-radius/rounded-xl` (đo kit) | `card/radius` | `radius/xl` 14 | `@card-radius` | 2 | Ghi đè |
| Badge `border-radius/rounded-full` (đo kit) | `tag/radius` | `radius/full` | `@tag-border-radius` — tên cần kiểm | 2 | Ghi đè |

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
| Bo pill | `input/radius` | `radius/full` | Mục 3 | 2 | Thêm mới |

### 7.3 Select — `nz-select`

| shadcn | Figma variable | Giá trị | Biến ng-zorro | TH |
|---|---|---|---|---|
| Trigger: `h-9` · sm `h-8`, `px-3`, `gap-2`, `rounded-md`, `shadow-xs` | theo Input | 36 / 32, 12, 8, 8 | `@select-*` + `@input-*` — tên cần kiểm | Theo Input |
| Mũi tên `size-4 opacity-50` | `select/arrow-size` | 16, mờ 50% | — | Thêm mới (độ mờ) |
| Menu: `rounded-md border shadow-md`, `p-1`, rộng tối thiểu 128 | `select/dropdown-padding` | 4 | `@select-dropdown-*` — tên cần kiểm | Ghi đè / Thêm mới |
| Mục: `py-1.5 pl-2 pr-8 rounded-sm text-sm` | `select/item-padding-y·x` | 6 · 8 (phải 32 chừa dấu ✓) | `@select-dropdown-vertical-padding` … — tên cần kiểm | Ghi đè |
| Mục chọn: `focus:bg-accent`, dấu ✓ bên phải | `color/item-hover-bg` | #f5f5f5 | `@select-item-selected-bg` | Ghi đè (AntD nền xanh nhạt, không có ✓) |

### 7.4 Checkbox — `nz-checkbox`

| shadcn | Figma variable | Giá trị | Biến ng-zorro | Mặc định AntD | TH |
|---|---|---|---|---|---|
| `size-4` | `checkbox/size` | 16 | `@checkbox-size` | 16 | 1:1 |
| `rounded-[4px]` | `radius/checkbox` | 4 | Mục 3 | 2 | Ghi đè |
| `checked: bg-primary border-primary` | `color/primary` | #171717 | `@checkbox-check-bg` / theo primary | — | 1:1 (theo primary) |
| Dấu ✓ `size-3.5` | `checkbox/check-size` | 14 | — | — | Thêm mới |
| `shadow-xs` | `shadow/xs` | Mục 6 | — | — | Thêm mới |

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
