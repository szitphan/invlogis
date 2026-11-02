---
type: design-component
status: stale
status_prev: in-review
updated: 2026-11-02
links:
  - design-system/architecture.md
  - design-system/foundations/README.md
  - design-system/foundations/logo.md
  - design-system/components/base/logo.md
  - design-system/tokens.json
  - design-system/components/base/breadcrumbs.md
  - design-system/components/application/sidebar-navigation.md
  - design-system/components/_work/header-navigation/page.json
  - design/ui-common/screen-patterns.md
  - docs/_shared/system-overview.md
  - _workspace/decisions.md
---

# Header Navigation · thanh trên

> Application · phiên bản 0.4.0 · Đang review · người phụ trách @szitphan · Figma: trang DS · Application components —
> `Header navigation` 6768:191286 · `Breadcrumbs` 6901:20705 (biến thể gốc 6768:190544) · `_Header bell` 6768:190822 ·
> `_Header secondary nav` 6768:190732 · `_Search result` 6900:216895 · `_Header search panel` 6904:20446 · khung tài liệu
> `Tài liệu` 6768:198301 · DEC-291, DEC-293, DEC-305 · trang duyệt
> https://claude.ai/artifact/Ua29VuBKRsRys51EYujU3P · ảnh mốc `_work/header-navigation/preview-web.png`,
> `preview-mobile.png`

Thanh trên của màn web (CMP-11): đường dẫn, **tìm tính năng**, trợ giúp, chuông, tài khoản. Nhóm C (DEC-279): web trên
điện thoại (< 768) đổi cấu tạo nên một bộ có trục `Platform=Web|Mobile`. App Delta Super App **không dùng** bộ này — app
dùng `Mobile header`. Bản này sửa tại chỗ bộ `Header navigation` dựng theo Untitled (giữ id, 23 instance tự cập nhật).

## Web

> Khối Web đặt mode Platform = Web; mọi số là giá trị mode Web.

### Tổng quan

- **Trái:** `Breadcrumbs` Type Text (D1 A, D6 A): đường dẫn nằm ở thanh trên, đầu trang chỉ còn tiêu đề. Page header
  không lặp đường dẫn khi thanh trên đã có. Từ 4 tầng gom tầng giữa thành "…", bấm mở menu tầng ẩn (D7 A).
- **Phải:** nút Tìm · Trợ giúp · Chuông · Avatar, cùng cỡ `control/height/md`, cách nhau `space/md`.
- **Tìm tính năng** (D2 B, D3 C): nút kính lúp, gợi ý ⌘K (Windows: Ctrl K). Bấm nút hoặc ⌘K → **hộp thoại giữa màn**,
  nền mờ, ô nhập ở đầu hộp:
  - chưa gõ: "Dùng gần đây" (tối đa 5 màn đã mở);
  - đang gõ: nhóm **Tính năng** (màn, kèm đường dẫn module › màn), **Hành động** (Tạo …, mở thẳng form) và **Bản ghi**
    (mã lệnh, biển số…); chữ khớp tô nền;
  - không ra: tiêu đề "Không có tính năng “{từ khoá}”" + câu gợi ý (R13);
  - chân hộp: ↑↓ chọn · ↵ mở · "Chỉ hiện tính năng bạn có quyền".
  Tính năng + hành động đọc từ cây menu theo quyền của role + quyền tạo (system-overview: menu theo phân quyền). Bản ghi
  cần **API tìm toàn cục** — chưa có trong SRS, phần này chờ SRS (D3 C). Mục đầu được chọn sẵn; Esc đóng hộp và trả
  focus về nút Tìm.
- **Chuông** (D5 C): số đếm đỏ chỉ đếm việc cần xử lý, tối đa "9+"; 0 việc thì ẩn số. Bấm mở Notification Center
  (component riêng, CMP-02) neo dưới chuông.
- **Tài khoản** (D4 B, DEC-293): chỉ avatar (chữ viết tắt hoặc ảnh); rê chuột hiện tooltip họ tên. Bấm mở menu: đầu menu
  avatar + họ tên + **mã NV · chức vụ** → Thông tin cá nhân · Đổi mật khẩu · Ngôn ngữ (giá trị hiện tại bên phải) · vạch ·
  Đăng xuất (chữ đỏ) (UC01.01–01.06). Hàng Ngôn ngữ: giá trị = cờ `Flag` + tên ngôn ngữ, vẫn có chữ, cờ không đứng một mình;
  theo `P-ngon-ngu-giao-dien`: Tiếng Việt cờ VN, Tiếng Anh cờ US (user 02/11) (DEC-335 ms06,
  [icon-sets.md](../../foundations/icon-sets.md)).
- **Layout = Secondary Nav:** thêm hàng tab dưới thanh (màn chi tiết: Chi tiết · Chi phí · Chứng từ · Lịch sử). Chỉ một
  viền dưới, ở đáy hàng tab.

### Cấu tạo

| Phần | Token | Giá trị (Web) |
|---|---|---|
| Khung thanh | cao `header-nav/height`; nền `color/bg/primary`, viền dưới 1 `color/border/secondary`; lề ngang `space/3xl`, khoảng `space/md` | 44 |
| Hàng tab | cao `control/height/lg`, khoảng `space/2xl`, lề ngang `space/3xl`; tab `type/body` nét 500 (Medium), chưa chọn `color/text/tertiary`, đang chọn `color/text/primary` + vạch dưới `focus/width` `color/focus/ring`; lề dưới chữ `space/md` | 40 |
| Đường dẫn | `Breadcrumbs` Type Text — `base/breadcrumbs.md`: chữ `type/body`, tầng cha nét 400 `color/text/tertiary`, trang hiện tại nét 500 `color/text/primary` cắt ở `breadcrumbs/current-max-width`; dấu phân cách icon `icon/size/sm` `color/border/primary`; nhà icon `icon/size/md` | co lại trước nhóm nút |
| Menu tầng ẩn "…" | nút "…" `touch/min`, đang mở nền `color/bg/selected` (ngoại lệ tương phản, DEC-305); menu rộng tối thiểu `breadcrumbs/menu-min-width`, bo `radius/menu`, lề `space/xs`, bóng `shadow/lg`, viền `shadow/lg-border`; mục cao `control/height/md` bo `radius/menu-item`; mục cuối (tầng sát trang hiện tại) chữ `color/text/tertiary` (R8) | — |
| Nút Tìm · Trợ giúp | `Button` Tertiary Icon Only MD + `Tooltip` ("Tìm tính năng · ⌘K", "Trợ giúp") | `control/height/md`, icon `icon/size/lg`, bo `radius/control`; rê nền `color/bg/selected`, đang mở nền `color/bg/selected` |
| `_Header bell` | `Button` Tertiary Icon Only MD + khối `Count`: nền `color/text/error/primary`, chữ `color/text/inverse` nét 500 cỡ cố định `chip/count-font-size` / `chip/count-line-height` (12/16, không đổi theo mode, như Badge), cao và rộng tối thiểu `size/xl`, lề ngang `space/xs`, bo `radius/full`, viền tách `focus/width` `color/bg/primary` | neo góc trên phải icon, chỉ đè một góc |
| Avatar | `Avatar` Content Initials Size SM (`size/4xl`, chữ và màu theo Avatar) trong nút tròn cùng cỡ, không đệm | 32 |
| Menu tài khoản | `Dropdown menu` rộng `header-nav/account-menu-width`, bo `radius/menu`, lề `space/xs`, bóng `shadow/lg`, viền `shadow/lg-border`; đầu menu avatar + họ tên nét 600 + mã NV · chức vụ `type/caption` `color/text/tertiary`, vạch `color/border/secondary` dưới đầu menu (Base `Dropdown heading` Type=Account, áp cho mọi menu tài khoản, R7); mục cao `control/height/md`, lề `space/md`, icon `icon/size/md` `color/fg/tertiary`; vạch `color/border/secondary`; Đăng xuất `color/text/error/primary` | neo dưới avatar, mép phải thẳng mép phải thanh |
| Hộp thoại tìm | rộng `command-search/width`, cách đỉnh màn 96, bo `radius/overlay`, bóng `shadow/xl`, viền `shadow/xl-border`, nền mờ `color/bg/overlay` + `backdrop-blur/lg`; ô nhập cao 52 chữ `type/title-3` (chữ gợi ý `color/text/tertiary`), gợi ý phím `Kbd` Esc | 600 |
| Kết quả | nhãn nhóm `type/caption-caps` `color/text/tertiary`; dòng cao `control/height/lg`, lề ngang `space/xl`, khoảng `space/md`, ô icon `control/height/sm` bo `radius/inner`; chữ chính `type/body` nét 500, phụ `type/caption` `color/text/tertiary`; đang chọn `color/bg/selected` + vạch trái 2 `color/focus/ring` (R3); chữ khớp nền `color/bg/warning/secondary`, bo `radius/xxs`, lề `command-search/highlight-padding-x`; chân nền `color/bg/secondary` `type/caption` | — |
| Không có kết quả | `Featured icon` kiểu `modern-subtle` 48/24 (DEC-335 ms17; icon.md mục 3.1; `Featured icon` chưa có component), cách tiêu đề `space/md`; tiêu đề `type/heading` nét 600, phụ `type/caption` `color/text/tertiary` ("Thử một từ khác. Màn bạn không có quyền sẽ không hiện ở đây.", R11); chân hộp gợi ý phím bằng `Kbd`; lề dọc `space/3xl` | — |
| Tooltip | `Tooltip` Short (`base/tooltip.md`, DEC-301) | 12/16 |
| Vòng focus | `focus/width` 2, cách `focus/offset` 2, `color/focus/ring` | mọi phần bấm được |

### Biến thể

- `Header navigation`: Platform = Web · Mobile × Layout = Simple · Secondary Nav. Bật tắt: `Has Breadcrumb`, `Has Search`,
  `Has Help`, `Has Bell`, `Has Account`; Mobile thêm `Has Back` (hàng ←), `Title`, `Back label`.
- `_Header bell`: Count = 0 · 3 · 9+ × State = Default · Hover · Focus × Open = No · Yes (R5).
- `_Header search panel` (hộp thoại): Content = Recent · Results · Empty. Nhóm không có kết quả thì ẩn; đang tải dùng trạng
  thái tải chung của trang, không có biến thể riêng (R1).

### Trạng thái

Mặc định · Đang tìm (hộp thoại) · Tìm không thấy · Mở thông báo · Mở menu tài khoản · Mở menu tầng ẩn · Không có thông báo
(ẩn số) · Chữ dài (đường dẫn 5 tầng gom "…", 9+, tên dài trong menu). Nút icon / avatar: Rest · Hover (+ tooltip) · Focus ·
Đang mở (nền `color/bg/selected`).

### Kích thước

Một cỡ. Thanh rộng theo vùng nội dung (1280 − menu 240 = 1040 ở màn chuẩn). Thiếu chỗ thì đường dẫn gom "…" trước, trang
hiện tại giữ tối thiểu 120 rồi mới cắt (R4). Dưới 768 dùng Platform = Mobile.

### Nên và không nên

- Nên: một đường dẫn mỗi màn — ở thanh trên; Page header không lặp lại.
- Nên: kết quả tìm chỉ gồm việc người dùng có quyền; không hiện màn rồi báo "không có quyền".
- Không: dùng hộp tìm này thay ô tìm của bảng — bảng có ô tìm riêng.
- Không: đếm thông báo đã đọc hay tin thường vào số đỏ — chỉ việc cần xử lý.
- Không: đặt nút chi nhánh / phạm vi ở thanh trên — phạm vi ở thẻ chân menu trái (DEC-288).

### Trợ năng — chấm theo WCAG 2.2

- 1.4.3: chữ đường dẫn, chữ gợi ý ô tìm `text/tertiary` 4,74:1; số đếm trắng trên `text/error/primary` 6,5:1; chữ phụ dòng
  đang chọn dùng `text/tertiary_strong`.
- 1.4.11: số đếm tách chuông bằng viền 2 màu nền. Nền "…" đang mở 1,09:1 là tín hiệu phụ (menu đã mở + `aria-expanded`),
  ngoại lệ DEC-305.
- 2.4.7 / 2.4.11: vòng focus 2 cách 2 trên mục đường dẫn, nút, avatar; dòng kết quả đang chọn có vạch trái 2
  `color/focus/ring` (R6). Thanh dính đầu: `scroll-padding-top` = cao thanh (44, 84 khi có hàng tab).
- 2.5.8: nút 32, mục đường dẫn ≥ 24 giữa tâm, dòng kết quả 40.
- 4.1.2: nút icon có tên — "Tìm tính năng (⌘K)", "Trợ giúp", "Thông báo, 3 việc cần xử lý" / "Thông báo, hơn 9 việc",
  "Tài khoản: {họ tên}"; hộp tìm `role="dialog"` có nhãn, ô nhập `role="combobox"` + `aria-activedescendant`, mỗi dòng
  `role="option"` + `aria-selected`, nhóm `role="group"` có nhãn; menu tài khoản `role="menu"`; hàng tab là `nav` +
  liên kết `aria-current` (R11).
- 2.1.1 / 2.1.4: ⌘K / Ctrl K mở hộp tìm; ↑↓ đi trong kết quả, ↵ mở, Esc đóng và trả focus; Tab: đường dẫn → Tìm → Trợ
  giúp → Chuông → Avatar. Không dùng phím tắt một chữ (bỏ "N", R1).
- 4.1.3: số kết quả đọc qua `aria-live="polite"` ("5 kết quả"); không có kết quả đọc câu trạng thái rỗng.
- 1.4.13: tooltip hiện khi focus, Esc đóng, rê vào tooltip không mất.
- 1.3.1 / 4.1.2: chữ bị cắt "…" (trang hiện tại của đường dẫn) giữ tên đủ trong DOM, cắt bằng CSS, kèm tooltip khi rê / focus.
  Tooltip chuông là "Thông báo", tên đọc là "Thông báo, {n} việc cần xử lý".

### Thuộc tính

`Header navigation`: `Has Breadcrumb`, `Has Search`, `Has Help`, `Has Bell`, `Has Account`, `Has Menu`, `Has Back`, `Title`,
`Back label`, Platform, Layout; expose instance lồng `_Header bell`, `Avatar`, `Breadcrumbs` để đổi Count, chữ tắt, các tầng
trên panel (R12, R9). Nhãn tab mặc định Chi tiết · Chi phí · Chứng từ · Lịch sử. `_Header tab` chỉ còn Type = Underline (bỏ
Type = Button, R6).
`_Header search panel`: Content = Results · Recent · Empty; mỗi dòng là instance `_Search result` (State Default ·
Selected; `Title`, `Path`, `Has Match`, `Match`). Chữ khớp tô nền ở code mọi vị trí; Figma mô phỏng bằng khung `Match` ở đầu
tên (`Title` giữ phần còn lại), chữ khớp giữa tên chưa mô phỏng được (R4, R14).

### Thành phần lồng

`Breadcrumbs`, `Button` (Tertiary Icon Only), `Tooltip`, `Avatar`, `Dropdown menu`, `Kbd`, `Featured icon` (chờ BL-253),
`_Header bell`, `_Header secondary nav`, `_Header search panel`, icon Lucide.

### Được dùng trong

CMP-11 Khung trang web — mọi màn web trong module (transport-dispatch, service-delivery, fund-payments…) · CMP-02 In-app
Notification (chuông) · UC01.01–01.06 Tài khoản cá nhân (menu tài khoản) · Page header, Card header, Section header (các
demo trên trang DS · Application components dùng instance bộ này).

### Token

Số đo theo mode ở bảng Cấu tạo; màu ở Phần máy. Token riêng (DEC-305): `header-nav/height`,
`header-nav/account-menu-width`, `breadcrumbs/current-max-width`, `breadcrumbs/menu-min-width`,
`command-search/width`, `radius/xxs`, `command-search/highlight-padding-x`,
`space/md`, `size/xs`, `radius/xxs`. Đối chiếu đủ giá trị:
`_work/header-navigation/check.json` (bước 3 xong 29/10, 0 dòng chờ).

### Kiểm máy

Vẽ lại Figma 29/10 theo tổ hợp DEC-291/293/305 (BL-273).

- `layout_audit` trên `Header navigation`, `_Header bell`, `_Header search panel`: 0 lỗi chặn. Các mục tràn khung có chủ
  đích: số đếm chuông đặt tuyệt đối, tooltip, vòng focus, chấm trạng thái avatar.
- Tương phản: chữ "Esc" trong `Kbd` 4,16:1. Lỗi thuộc component Base `Kbd`, không sửa trong Header nav.
- Hàng tab: `_Header tab` Underline bỏ lề ngang, hàng `Type=Tabs` gắn `space/2xl` 20 (khớp preview).
- Khung `Tài liệu`: thêm mục **Menu** (menu tài khoản 256 có mã NV · chức vụ, menu tầng ẩn "…" 240, đều là instance
  `Dropdown menu`); mục Trạng thái thay ô tìm cũ bằng nút Tìm Hover / Focus; sửa chữ mô tả theo v0.4.0.
- Vòng 5 (30/10): áp R2–R11. `layout_audit` 0 lỗi chặn; `a11y_audit` mục Menu và 2 khung Mobile 0 lỗi; quét 1.369 node
  không dính biến collection thử "Thử · vòng 4" (trùng tên `control/height/*`).
- Đối chiếu Figma ↔ repo (`ds-v2-sync-check.py --figma`, 30/10): Header nav 0 FAIL (7 set + Section mang nhãn
  "Đang review"); 1 WARN khung `Tài liệu` là frame, không phải component.

### Chuyển động

Menu tài khoản, hộp tìm: `duration/fast`, trượt 4; vào `easing/standard`, ra `easing/exit`. Hover, nhấn `duration/fast`; vòng focus hiện ngay. Luật chung: `foundations/motion.md` (DEC-333).

## Mobile

> Khối Mobile đặt mode Platform = Mobile (web trên điện thoại, < 768).

- **Logo:** `Logo` (`base/logo.md`) Type Symbol, Size 24 (`size/3xl`), có ở mọi màn (DEC-326, `foundations/logo.md` mục 14.5), đứng sau nút
  Menu, tiêu đề trang đứng sau logo. Trên khung 393 còn khoảng 153 cho tiêu đề (185 trừ ký hiệu 24 và khoảng 8).
- Thanh `header-nav/height` 56 (D8 A): Menu (☰, "Mở menu") · tiêu đề trang hiện tại `type/body` nét 600, một dòng cắt
  "…" · Tìm (icon) · Chuông (`_Header bell`) · Avatar `size/4xl` trong nút `control/height/sm` có **vùng bấm vô
  hình 44** (DEC-305, theo DEC-138). Không có đường dẫn, Trợ giúp (Trợ giúp ở sheet tài khoản, R3).
- **Hàng ←** (`Has Back`, màn con): "← {tên cấp trên}", cao `control/height/md` (42; preview 40 lệch 2, kéo về token ở bước 3), lề ngang `space/lg`,
  khoảng `space/xs`, chữ `color/text/tertiary_strong`; **vùng bấm vô hình 44**. Màn gốc của module không có hàng này.
- Tìm: chạm icon mở **màn tìm toàn trang** — ô nhập cao 52 chữ `type/title-3`, nút ← đóng; kết quả như web (Tính năng ·
  Hành động · Bản ghi), không có phím tắt, không có chân phím.
- Avatar: chạm mở **sheet tài khoản** từ dưới lên — bo trên `radius/overlay`, thanh kéo 36 × `size/xs` bo
  `radius/xxs`, đầu sheet avatar + họ tên + vai trò, mục cao `touch/min` lề `space/lg` icon `icon/size/md`
  chữ `type/body`, lớp phủ `color/bg/overlay`.
- Chuông: chạm mở màn Thông báo toàn trang của Notification Center (bản Mobile của component đó).

### Trợ năng — chấm theo WCAG 2.2

- 2.5.8: mọi nút (Menu, Tìm, Chuông, Avatar, hàng ←) có vùng chạm 44 (`touch/min`), nút nhìn thấy 42 / avatar 32.
- 4.1.2: tên nút "Mở menu", "Tìm tính năng", "Thông báo, {n} việc cần xử lý", "Tài khoản: {họ tên}", "Quay lại {cấp trên}".
- 1.3.1: tiêu đề trang là `h1`, chữ đủ trong DOM (cắt "…" bằng CSS).
- 2.4.3: sheet tài khoản `role="dialog"` có nhãn, focus vào sheet khi mở, đóng bằng thanh kéo / chạm nền / Esc và trả
  focus về avatar; màn tìm toàn trang: nút ← có tên, đóng trả focus về nút Tìm.

### Kiểm máy

Chung với khối Web (bộ có trục Platform). Khung `Tài liệu` có màn tìm toàn trang (Recent / Results / Empty, ô 52, nút ←) và
sheet tài khoản (Trợ giúp · Thông tin cá nhân · Đổi mật khẩu · Ngôn ngữ · Đăng xuất) (R2); hàng ← gắn `control/height/md` 42.
Hàng Ngôn ngữ của sheet giống web: cờ `Flag` + tên ngôn ngữ (DEC-335 ms06).

## Đối chiếu Astryx

| Astryx (`Khung trang / Thanh trên`) | Bản này | Vì sao |
|---|---|---|
| Thanh 44 | 44 (`header-nav/height`) | Giữ cao Astryx (góp ý 28/10) |
| Đường dẫn trái | Giữ, gom tầng giữa thành "…" | Đường dẫn sâu không đẩy nhóm nút ra ngoài (D7) |
| Nút chi nhánh trên thanh | Bỏ | Phạm vi ở chân menu trái (DEC-288) |
| Ô tìm không có kết quả | Nút kính lúp + hộp thoại ⌘K: tính năng, hành động, bản ghi | User chọn D2 B, D3 C (DEC-291) |
| Chuông chấm đỏ | Số đếm đỏ, tối đa 9+ | User chọn D5 C |
| Avatar 36 + họ tên ≤ 160 + chevron | Chỉ avatar, tên trong tooltip và đầu menu (mã NV · chức vụ) | User chọn D4 B (DEC-293) |

## Phần máy (chung Web và Mobile)

<!-- auto:begin -->
<!-- auto:end -->
