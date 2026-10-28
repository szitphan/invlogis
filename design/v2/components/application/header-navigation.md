---
type: design-component
status: draft
updated: 2026-10-28
links:
  - design/v2/architecture.md
  - design/v2/foundations.md
  - design/v2/tokens.json
  - design/v2/components/base/breadcrumbs.md
  - design/v2/components/application/sidebar-navigation.md
  - design/v2/components/_work/header-navigation/page.json
  - design/ui-common/screen-patterns.md
  - docs/_shared/system-overview.md
  - _workspace/decisions.md
---

# Header Navigation · thanh trên

> Application · phiên bản 0.3.0 · Nháp · người phụ trách @szitphan · Figma: trang DS · Application components —
> `Header navigation` 6768:191286 · `Breadcrumbs` 6901:20705 (biến thể gốc 6768:190544) · `_Header bell` 6768:190822 ·
> `_Header secondary nav` 6768:190732 · `_Search result` 6900:216895 · `_Header search panel` 6904:20446 · khung tài liệu
> `Tài liệu` 6768:198301 · DEC-290 · trang duyệt
> https://claude.ai/artifact/Ua29VuBKRsRys51EYujU3P · ảnh mốc `_work/header-navigation/preview-web.png`,
> `preview-mobile.png`

Thanh trên của màn web (CMP-11): đường dẫn, **tìm tính năng**, trợ giúp, chuông, tài khoản. Nhóm C (DEC-279): web trên
điện thoại (< 768) đổi cấu tạo nên một bộ có trục `Platform=Web|Mobile`. App Delta Super App **không dùng** bộ này — app
dùng `Mobile header`. Bản này sửa tại chỗ bộ `Header navigation` dựng theo Untitled (giữ id, 23 instance tự cập nhật).

## Web

> Khối Web đặt mode Platform = Web; mọi số là giá trị mode Web.

### Tổng quan

- **Trái:** `Breadcrumbs` Type Text (D1 A, D6 A) — đường dẫn nằm ở thanh trên, đầu trang chỉ còn tiêu đề. Page header
  không lặp đường dẫn khi thanh trên đã có.
- **Phải:** ô tìm tính năng 300 · Trợ giúp · Chuông · Avatar, cách nhau `space/gap-sm`.
- **Tìm tính năng** (D2 A, D3 B): ô luôn hiện, gợi ý ⌘K (Windows: Ctrl K). Bấm ô hoặc ⌘K → bảng kết quả rơi dưới ô:
  - chưa gõ: "Dùng gần đây" (tối đa 5 màn đã mở);
  - đang gõ: nhóm **Tính năng** (màn, kèm đường dẫn module › màn) và **Hành động** (Tạo …, mở thẳng form); chữ khớp tô nền;
  - không ra: "Không có tính năng “{từ khoá}” · Thử từ khác, hoặc tính năng chưa được cấp quyền cho tài khoản này.";
  - chân bảng: ↑↓ chọn · ↵ mở · "Chỉ hiện tính năng bạn có quyền".
  Kết quả đọc từ cây menu theo quyền của role + quyền tạo (system-overview: menu theo phân quyền); **không** gọi API tìm
  toàn cục, không tìm bản ghi (mã lệnh, biển số — D3 C bỏ vì chưa có API trong SRS). Mục đầu được chọn sẵn; Esc đóng
  bảng, Esc lần hai xoá chữ.
- **Chuông** (D5 C): số đếm đỏ chỉ đếm việc cần xử lý, tối đa "9+"; 0 việc thì ẩn số. Bấm mở Notification Center
  (component riêng, CMP-02) neo dưới chuông.
- **Tài khoản** (D4 B): chỉ avatar (chữ viết tắt hoặc ảnh); rê chuột hiện tooltip họ tên. Bấm mở menu 300: đầu menu
  avatar 40 + họ tên + vai trò · chi nhánh → Thông tin cá nhân · Đổi mật khẩu · Ngôn ngữ (giá trị hiện tại bên phải) ·
  vạch · Đăng xuất (chữ đỏ) (UC01.01–01.06).
- **Layout = Secondary Nav:** thêm hàng tab 40 dưới thanh (màn chi tiết: Chi tiết · Chi phí · Chứng từ · Lịch sử). Chỉ
  một viền dưới, ở đáy hàng tab.

### Cấu tạo

| Phần | Token | Giá trị (Web) |
|---|---|---|
| Khung thanh | nền `color/bg/surface`, viền dưới `color/border/default` 1, lề ngang `space/inset-xl`, khoảng `space/inset-sm` | cao 56 (`nav/scan-size`) |
| Hàng tab | `_Header secondary nav` cao `control/height/lg`, khoảng `space/20`, lề ngang `space/inset-xl`; tab `type/heading` nét 600, chưa chọn `color/text/secondary`, đang chọn `color/text/primary` + vạch dưới `focus/width` `color/border/focus` | 40; lề dưới chữ `chip/padding-x` |
| Đường dẫn | `Breadcrumbs` Type Text — xem `base/breadcrumbs.md` | co lại trước ô tìm |
| Ô tìm | `Input` Size MD (`control/height/md`), icon dẫn 16, viền `color/border/input`, bo `radius/field`; lề trái `space/inset-sm` + 2, phải `space/inset-sm`, khoảng `space/inset-sm`; gợi ý phím `Kbd` `type/caption` `color/text/secondary` viền `color/border/strong` bo 4 | 300 × 32, cố định |
| Bảng kết quả `_Header search panel` | nền `color/bg/surface`, viền `color/border/default`, bo `radius/card`, bóng `elev/3`; nhãn nhóm `type/caption` nét 600 chữ hoa `color/text/secondary`; dòng cao `control/height/lg` lề ngang 16 khoảng `chip/padding-x`, ô icon 28 bo `radius/control`; đang chọn `color/bg/selected`; chữ khớp nền `color/status/warning-bg-strong`; chân nền `color/bg/canvas` `type/caption` | rộng 400 (`width/sm`), mép trái thẳng mép trái ô tìm, cách ô 4 |
| Trạng thái rỗng của bảng | tiêu đề `type/heading` nét 600 · phụ `type/caption` `color/text/secondary` | lề dọc `space/inset-xl` |
| Nút Trợ giúp | `Button` Tertiary Icon Only MD + `Tooltip` "Trợ giúp" | 32 (`control/height/md`; preview 36 kéo về luật cao control DEC-173), icon 20 — màu icon của `Button` (không gắn đè) |
| `_Header bell` | `Button` Tertiary Icon Only + khối `Count` riêng (Badge không có bản nền đặc): nền `color/status/danger-solid`, chữ `color/text/inverse` `type/caption-strong`, bo `radius/full`, lề ngang `space/inset-xs`, viền tách 2 `color/bg/surface` | nút 32; số cao 20, rộng tối thiểu 20, đặt tuyệt đối x 18 · y −4 (mép trái số ở giữa chuông, không che chuông) |
| Avatar | khung `Account` bo `radius/full` chứa `Avatar` Content Initials Size SM (màu, chữ theo Avatar) | 32, không lề (thẳng hàng nút 32) |
| Menu tài khoản | `Dropdown menu` rộng 300 (`field/label-max-width`), bo `radius/card`, lề 6, bóng `elev/3`; đầu menu avatar 40, khoảng `chip/padding-x`, vai trò `type/caption` `color/text/secondary`; mục cao 36 lề `chip/padding-x` icon 16 `color/icon/secondary`; Đăng xuất `color/action/danger` | neo dưới avatar, mép phải thẳng mép phải thanh |
| Vòng focus | `focus/width` 2, cách `focus/offset` 2, `color/border/focus` | mọi phần bấm được |

### Biến thể

- `Header navigation`: Platform = Web · Mobile × Layout = Simple · Secondary Nav (giữ). Bật tắt: `Has Breadcrumb`,
  `Has Search`, `Has Help`, `Has Bell`, `Has Account`; Mobile thêm `Has Back` (hàng ←), `Title`, `Back label`.
- `_Header bell`: Count = 0 · 3 · 9+ × State = Default · Hover · Open.
- `_Header search panel`: Content = Recent · Results · Empty.

### Trạng thái

Mặc định · Đang tìm (bảng kết quả) · Tìm không thấy · Mở thông báo · Mở menu tài khoản · Không có thông báo (ẩn số) ·
Chữ dài (đường dẫn 5 tầng gom "…", 9+, tên dài trong menu). Ô tìm: Rest · Hover (viền `color/text/secondary-strong`) ·
Focus chưa gõ · Đang gõ (viền 2 `color/border/focus`) · Focus bàn phím. Nút icon / avatar: Rest · Hover (+ tooltip) ·
Focus · Đang mở (nền `color/bg/selected`).

### Kích thước

Một cỡ. Thanh rộng theo vùng nội dung (1280 − menu 240 = 1040 ở màn chuẩn). Thiếu chỗ thì đường dẫn co và gom trước,
ô tìm giữ 300. Dưới 768 dùng Platform = Mobile.

### Nên và không nên

- Nên: một đường dẫn mỗi màn — ở thanh trên; Page header không lặp lại.
- Nên: kết quả tìm chỉ gồm việc người dùng có quyền; không hiện màn rồi báo "không có quyền".
- Không: dùng ô tìm này để tìm bản ghi trong bảng — bảng có ô tìm riêng.
- Không: đếm thông báo đã đọc hay tin thường vào số đỏ — chỉ việc cần xử lý.
- Không: đặt nút chi nhánh / phạm vi ở thanh trên — phạm vi ở thẻ chân menu trái (DEC-288).

### Trợ năng — chấm theo WCAG 2.2

- 1.4.3: chữ đường dẫn, placeholder ô tìm `text/secondary` 4,74:1; số đếm trắng trên red/700 6,5:1; chữ phụ bảng kết
  quả trên `bg/selected` dùng `text/secondary-strong`.
- 1.4.11: viền ô tìm `border/input` ≥ 3:1; số đếm tách chuông bằng viền 2 màu nền.
- 2.4.7 / 2.4.11: vòng focus 2 cách 2 trên mục đường dẫn, ô tìm, nút, avatar, dòng kết quả.
- 2.5.8: nút 36, ô tìm 32, mục đường dẫn ≥ 24 (Type Text cao 20 + khoảng cách ≥ 24 giữa tâm), dòng kết quả 40.
- 4.1.2: nút icon có tên — "Trợ giúp", "Thông báo, 3 việc cần xử lý" / "Thông báo, hơn 9 việc", "Tài khoản: {họ tên}";
  ô tìm `role="combobox"` `aria-expanded`, bảng `role="listbox"` có nhãn "Tìm tính năng", nhóm `role="group"` có nhãn;
  menu tài khoản `role="menu"`.
- 2.1.1: ⌘K / Ctrl K vào ô tìm; ↑↓ đi trong kết quả, ↵ mở, Esc đóng và trả focus; Tab: đường dẫn → ô tìm → Trợ giúp →
  Chuông → Avatar.
- 4.1.3: số kết quả đọc qua vùng `aria-live="polite"` ("5 kết quả"); không có kết quả đọc câu trạng thái rỗng.
- 1.4.13: tooltip hiện khi focus, Esc đóng, rê vào tooltip không mất.
- 3.3.2: ô tìm có nhãn ẩn "Tìm tính năng", không dựa vào placeholder.

### Thuộc tính

`Header navigation`: `Has Breadcrumb`, `Has Search`, `Has Help`, `Has Bell`, `Has Account`, `Has Menu`, `Has Back`, `Title`,
`Back label`, Platform, Layout; đổi chữ đường dẫn, Count chuông, chữ tắt avatar, Type hàng phụ trên instance lồng.
`_Header search panel`: Content = Results · Recent · Empty; mỗi dòng là instance `_Search result` (State Default ·
Selected; `Title`, `Path`, `Has Shortcut`, `Shortcut`). Chữ khớp tô nền ở code (Figma không có nền theo đoạn chữ).

### Thành phần lồng

`Breadcrumbs`, `Input`, `Kbd`, `Button` (Tertiary Icon Only), `Tooltip`, `Avatar`, `Dropdown menu`, `_Header bell`,
`_Header secondary nav`, `_Header search panel`, icon Lucide.

### Được dùng trong

CMP-11 Khung trang web — mọi màn web trong module (transport-dispatch, service-delivery, fund-payments…) · CMP-02 In-app
Notification (chuông) · UC01.01–01.06 Tài khoản cá nhân (menu tài khoản) · Page header, Card header, Section header (các
demo trên trang DS · Application components dùng instance bộ này).

### Token

Số đo theo mode ở bảng Cấu tạo; màu ở Phần máy. Đối chiếu đủ 170 giá trị: `_work/header-navigation/check.json` (170 khớp).

### Kiểm máy

Chạy 28/10 sau khi dựng (vòng 4):

- **layout_audit** 5 bộ + khung tài liệu: 0 lỗi chặn. Tràn khung có chủ đích: số đếm chuông, tooltip, vòng focus (lớp
  tuyệt đối). Hàng Chữ dài màn 1024 sửa theo luật Sidebar (dưới 1280 menu thu gọn 64 → thanh 960).
- **a11y_audit**: 0 fail. Review: vùng chạm web 32 (đạt 2.5.8), viền popover 1,21:1 (mép popover, không phải viền control).
- **auditDesignSystem**: compliance 0,95–1,00, không giá trị gõ cứng có token tương ứng.
- **Dark**: bỏ (giá trị Dark DS v2 chưa điền).
- **3 agent review**: vòng 5 (trang duyệt tab 4).

## Mobile

> Khối Mobile đặt mode Platform = Mobile (web trên điện thoại, < 768).

- Thanh 56 (D8 A): Menu (☰, "Mở menu") · tiêu đề trang hiện tại `type/heading` (mode Mobile), một dòng cắt "…" · Tìm
  (icon) · Chuông (`_Header bell`) · Avatar SM 32 (preview 28 — Avatar không có cỡ 28). Không có đường dẫn, Trợ giúp.
- **Hàng ←** (`Has Back`, màn con): "← {tên cấp trên}", cao 40, lề ngang `space/inset-md`, khoảng `space/inset-xs`, chữ
  `color/text/secondary-strong`; **vùng bấm vô hình 44** (DEC-290, theo DEC-138). Màn gốc của module không có hàng này.
- Tìm: chạm icon mở **màn tìm toàn trang** — ô nhập cao 52 chữ 17 (`type/title-3`), nút ← đóng; kết quả như web (không có
  chân phím tắt).
- Avatar: chạm mở **sheet tài khoản** từ dưới lên — bo trên `radius/2xl` 16, thanh kéo 36 × 4, đầu sheet avatar 40 + họ tên
  + vai trò, mục cao 48 lề `space/inset-md` icon 20 chữ 15/22, lớp phủ `color/overlay/scrim`.
- Chuông: chạm mở màn Thông báo toàn trang của Notification Center (bản Mobile của component đó).
- Nút icon 42 (`Button` MD mode Mobile).

### Kiểm máy

Chung với khối Web (bộ có trục Platform); a11y_audit: nút 42 dưới mức thoải mái 44 — mức review, đạt 2.5.8.

## Đối chiếu Astryx

| Astryx (`Khung trang / Thanh trên`) | Bản này | Vì sao |
|---|---|---|
| Thanh 44 | 56 | Theo variant page (Height 56), Untitled 64 bản ERP dày hơn |
| Đường dẫn trái | Giữ, gom tầng giữa thành "…" | Đường dẫn sâu không đẩy ô tìm ra ngoài (D7) |
| Nút chi nhánh trên thanh | Bỏ | Phạm vi ở chân menu trái (DEC-288) |
| Ô tìm không có bảng kết quả | Tìm tính năng + hành động theo quyền | Yêu cầu tìm tính năng (D2, D3) |
| Chuông chấm đỏ | Số đếm đỏ, tối đa 9+ | User chọn D5 C |
| Avatar 36 + họ tên ≤ 160 + chevron | Chỉ avatar, tên trong tooltip và đầu menu | User chọn D4 B |

## Phần máy (chung Web và Mobile)

<!-- auto:begin -->
<!-- auto:end -->
