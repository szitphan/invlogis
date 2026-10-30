---
type: design-component
status: approved
updated: 2026-10-29
links:
  - design/v2/architecture.md
  - design/v2/foundations.md
  - design/v2/icons.md
  - design/v2/tokens.json
  - design/v2/components/_work/badge-avatar/page.json
  - design/v2/components/l1/avatar.md
  - design/v2/components/l1/avatar-group.md
  - design/v2/components/base/badge.md
  - _workspace/decisions.md
---

# Avatar · Company avatar · Avatar group · Avatar label · Avatar add button

> Base · phiên bản 0.1.0 · Đã duyệt · người phụ trách @szitphan · Figma: Section `Avatars` (6657:165741) trang DS · Base
> components — `Avatar` 6657:166192 · `_Avatar status` 6657:165851 · `Company avatar` 6657:167713 · `Avatar group`
> 6657:166325 · `Avatar label` 6657:167394 · `Avatar add button` 6658:191370 · DEC-201, DEC-303 · thay tài liệu cũ
> [l1/avatar.md](../l1/avatar.md), [l1/avatar-group.md](../l1/avatar-group.md) · trang duyệt
> https://claude.ai/artifact/GcxVBfcfm4imkYbQstd9h2 · ảnh mốc `_work/badge-avatar/preview-web.png`, `preview-mobile.png`

Ảnh đại diện người (Avatar), tổ chức (Company avatar), nhóm người (Avatar group), avatar kèm tên (Avatar label) và nút
thêm người. Nhóm A (DEC-279): một bộ, cùng số đo web và app.

## Web

> Khối Web đặt mode Platform = Web; mọi số là giá trị mode Web.

### Avatar

- **Content:** Image (ảnh thật) · Loading (đang tải ảnh lên: ảnh xem trước + lớp phủ `avatar/scrim` + spinner; nút máy ảnh
  tắt, icon mờ 40%) · Initials (2 chữ cái họ + tên, giữ dấu) · Icon (người) · Upload (chưa có ảnh: Initials + nút máy ảnh
  góc dưới phải). Luồng tải ảnh: Upload → Loading → Image; lỗi thì quay về Upload kèm thông báo. Thứ tự dự phòng khi hiển
  thị: Image → Initials → Icon.
- **Status** là instance lồng `_Avatar status` (None · Online · Offline · Busy · Away). Không bật Status với Upload /
  Loading. Trong **bảng danh sách** avatar không mang chấm trạng thái (góp ý 29/10).

| Phần | XS | SM | MD | LG | XL | XXL | Token |
|---|---|---|---|---|---|---|---|
| Cỡ | 24 | 32 | 36 | 48 | 64 | 88 | `avatar/size/xs · sm · md · lg · xl · xxl` (thang XS–XXL, DEC-303) |
| Initials cỡ chữ | 12 | 12 | 14 | 17 | 20 | 24 | — |
| Initials dòng cao | 20 | 20 | 20 | 28 | 28 | 28 | `type/label/line-height` · `type/title-2/line-height` |
| Chấm trạng thái | 6 | 8 | 10 | 12 | 14 | 16 | `avatar/status-size/xs … xxl` + viền trắng `avatar/ring` 2 |
| Nút máy ảnh (Upload) | 14 | 16 | 16 | 20 | 24 | 32 | `avatar/edit-size/*` (chưa khớp thang mới, BL-281) |

- Chấm trạng thái: tâm chấm nằm trên mép tròn ở góc 45° — cùng vị trí tương đối ở mọi cỡ. Offline = chấm rỗng, viền
  `avatar/status-border` 2 màu `avatar/status/offline`.
- Nền Initials / Icon `avatar/bg`, chữ `avatar/fg`, chữ Initials 500.

### Company avatar

Content Image · Initials · Icon × 6 cỡ như Avatar. Vuông bo theo cỡ, viền 1 `color/border/default`:
XS `radius/badge` 6 · SM, MD 6 · LG 8 · XL `radius/menu` 8 · XXL 16.

### Avatar group

Size XS · MD · LG. Tối đa 4 avatar + ô "+n" (nền `avatar/overflow/bg`, chữ `color/text/secondary-strong`, DEC-304); avatar lồng được lộ ra để đổi Content ngay ở nhóm. Mỗi avatar trong khung trắng đệm `avatar/ring` 2;
chồng `avatar/group-overlap/sm · md · lg` (−6 · −8 · −12). **Avatar sau đè avatar trước** (DEC-303).

### Avatar label

Size SM · MD · LG — avatar 32 · 36 · 48 + khối chữ, cách `space/gap-sm` 8, rộng `avatar-label/width` 240. Tên
`type/label` 14/20 · 600; dòng phụ **12/16** cố định web + app (`avatar-label/subtitle-size`, `/subtitle-line-height`, DEC-303, DEC-304). Mỗi dòng cắt "…" một dòng.
Thuộc tính: Title, Subtitle, **Has Subtitle** (tắt khi chỉ có tên); avatar lồng được lộ ra (đổi Content / Status ngay ở Avatar label; tổ chức thì swap sang Company avatar). Tên set
Figma đổi từ "Avatar label group" thành "Avatar label" (29/10).

### Avatar add button

State Default · **Loading** (spinner thay dấu +, không bấm, aria-busy) · Hover (nền `color/bg/hover`) · Focus · Disabled. Cỡ **48, icon plus Size=24** theo luật Featured icon (icons.md mục 3.1, DEC-303, DEC-304); viền nét
đứt, focus ring 2 cách 4.

### Trợ năng

- Avatar cạnh tên là trang trí (alt rỗng). Đứng một mình: aria-label = họ tên + trạng thái ("Trần Văn Bình, Đang bận").
- **Trạng thái không chỉ bằng màu** (Online / Busy / Away khác nhau chủ yếu ở màu, WCAG 1.4.1): nơi trạng thái quan trọng
  thì ghi chữ trạng thái ở dòng phụ Avatar label hoặc tooltip (web); luôn có trong aria-label. Không bật Status ở XS.
- **Upload / Loading:** cả avatar là vùng chạm "Đổi ảnh đại diện" (nút máy ảnh chỉ để nhìn, không thêm điểm dừng tab
  thứ hai). Loading: `aria-disabled`, thông báo `aria-live="polite"` "Đang tải ảnh…", lỗi "Tải ảnh thất bại" (app dùng
  announcement). Upload chỉ dùng từ LG trở lên — nút máy ảnh XS–MD quá nhỏ để chạm (BL-281).
- **Avatar group:** `role="group"` + aria-label "Phụ trách: A, B, C và 3 người khác"; avatar con `aria-hidden`. Nền ô "+n"
  không đậm hơn `avatar/overflow/bg` (chữ hiện 4,54 : 1, sát ngưỡng).
- **Nút thêm:** aria-label "Thêm người" (đổi theo ngữ cảnh), tooltip cùng chữ trên web; focus ring 2 cách 4; vùng chạm 48.

## Mobile

Cùng số đo Web (nhóm A). Màn hồ sơ dùng XXL: chạm ảnh để đổi; chưa có ảnh thì Upload, đang tải thì Loading.

## Đối chiếu Astryx

- Thang v2 cũ 5 cỡ 24 · 36 · 48 · 64 · 88 → thêm SM 32, đổi tên token theo XS–XXL (DEC-303).
- Thêm Content Loading, Company avatar, Avatar label, Avatar add button. Nhóm avatar đổi từ "avatar đầu nằm trên"
  (DEC-242) sang "avatar sau đè avatar trước".

## Phần máy (chung Web và Mobile)

<!-- auto:begin -->
<!-- auto:end -->
