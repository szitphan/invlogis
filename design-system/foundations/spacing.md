---
type: design-foundations
status: draft
updated: 2026-11-02
links:
  - design-system/foundations/README.md
  - design-system/tokens.json

---

# Foundations · Khoảng cách

> Một phần của [[design-system/foundations/README.md|Foundations]]. Giữ số mục cũ (6.x) để các DEC và spec trích "foundations mục 6…" vẫn tra được. Giá trị máy đọc: `design-system/tokens.json` (json thắng).

## 6. Khoảng cách (DEC-135, DEC-164, DEC-166, DEC-173, DEC-192, DEC-194, DEC-196, DEC-232, DEC-234, DEC-239, DEC-242, DEC-243, DEC-244)

- Bảng gốc (Primitives), tên theo px: `space/0 · 2 · 4 · 6 · 8 · 10 · 12 · 16 · 20 · 24 · 32 · 40 · 48 · 64 · 80 · 96 · 128 · 160`.
- **Thang Semantic theo Untitled (DEC-314)**, Web = Mobile, dùng cho mọi lề trong và khoảng giữa phần tử (thay `space/inset-*`,
  `space/gap-*` cũ):

  | `space/…` | none | xxs | xs | sm | md | lg | xl | 2xl | 3xl | 4xl | 5xl | 6xl | 7xl | 8xl | 9xl | 10xl | 11xl |
  |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
  | px | 0 | 2 | 4 | 6 | 8 | 12 | 16 | 20 | 24 | 32 | 40 | 48 | 64 | 80 | 96 | 128 | 160 |

  Tên cũ → mới: `gap-2xs` → `xxs` · `inset-xs`, `gap-xs` → `xs` · `inset-sm`, `gap-sm` → `md` · `inset-md`, `gap-md` → `lg` ·
  `inset-lg`, `gap-lg` → `xl` · `inset-xl`, `gap-xl` → `3xl` · `gap-2xl` → `4xl`.
- **Bậc `size/14`, primitive `space/14` (DEC-329 ic05):** lệch thang Untitled do user chọn, chỉ cho cỡ icon (`icon/size/sm`, `icon/size/chip`), không dùng cho khoảng cách. Không thêm 18 vì cỡ 18 đã bỏ.
- **Thang kích thước `size/…`** (collection `5. Platform · Sizes`, DEC-314): cùng tên, cùng bậc như `space/…`; token component
  dùng cho cao, rộng, cỡ khối. Token component (`6.`) chỉ trỏ `space/…`, `size/…`, `type/…`, `radius/…` Semantic, không trỏ Primitive.
  Số lệch thang chờ chốt ở trang Token ↔ Component (BL-313).

| Token | Web | App | Dùng cho |
|---|---|---|---|
| `grid/margin` | 32 | 16 | Lề màn, trỏ `container/padding-*` (DEC-324) |
| `layout/empty-padding` | 80 | 64 | Lề trên dưới màn trống, màn kết quả, đăng nhập (`space/80`, `space/96` thêm ở DEC-259) |
| `container/max-width-desktop` | 1280 | — | Rộng tối đa màn chi tiết, form, gồm lề; màn bảng trải hết (DEC-324) |
| `layout/card-padding` | 16 | 16 | Lề chứa: lề trong thẻ, nhóm có viền, dòng trong nhóm (app 14 → 16, DEC-164) |
| `layout/list-gap` | 8 | 12 | Giữa các thẻ, dòng trong danh sách |
| `layout/section-gap` | 32 | 24 | Giữa các khối lớn |
| `layout/title-gap` | 16 | 16 | Tiêu đề màn → nội dung |
| `form/field-gap` | 16 | 12 | Giữa 2 ô nhập trong một nhóm |
| `touch/min` | 24 | 44 | Vùng chạm tối thiểu (web: WCAG 2.2 AA 24; app: DEC-138) |
| `focus/width` | 2 | 2 | Độ dày vòng focus |
| `focus/offset` | 2 | 2 | Khoảng cách vòng focus tới mép control |
| `control/height/sm · md · lg` | 28 · 32 · 40 | 36 · 42 · 52 | Cao nút, ô nhập, ô chọn; cùng cỡ thì cùng cao (DEC-173) |
| `control/padding-x/sm · md · lg` | 8 · 12 · 16 | 12 · 16 · 24 | Lề trái phải trong nút theo cỡ (nút app 52 lề 24, DEC-163) |
| `control/padding-x-icon/sm · md · lg` | 6 · 8 · 12 | 8 · 12 · 20 | Lề phía có icon trong nút: lùi một bậc thang |
| `control/icon-gap` | 6 | 8 | Icon → chữ trong nút, tab chip (DEC-161) |
| `tab/padding-x` | 8 | 16 | Lề trái phải trong tab: web tab gạch, app tab chip |
| `tab/padding-x-icon` | 6 | 12 | Lề phía có icon trong tab: lùi một bậc thang |
| `tab/gap` | 8 | 8 | Giữa 2 tab |
| `nav/height` | — (chỉ app) | 64 | Cao thanh điều hướng nổi (DEC-160) |
| `nav/offset-bottom` | — (chỉ app) | 8 | Thanh điều hướng → vùng an toàn đáy màn |
| `nav/padding-x` | — (chỉ app) | 4 | Lề trong thanh điều hướng |
| `nav/item-padding-y` | — (chỉ app) | 4 | Lề trên dưới mục, nên nền mục đang chọn cao 56 |
| `nav/scan-size` | — (chỉ app) | 56 | Nút Quét mã giữa thanh |
| `chip/height-sm` · `size/3xl` · `chip/height-lg` | 22 · 24 · 28 | 22 · 24 · 28 | Cao chip SM · MD · LG theo Untitled (DEC-259; SM 16 → 22, app MD 26 → 24); SM cho chip ở đầu thẻ (DEC-239) |
| `chip/font-size-sm` · `chip/line-height-sm` · `size/11xl` | 12 · 18 · 160 | 12 · 18 · 160 | Chữ chip SM cố định 12/18 cả web và app; nhãn chip tối đa 160 rồi cắt "…" (DEC-239) |
| `chip/padding-x-sm` · `space/lg` · `chip/padding-x-lg` | 10 · 12 · 14 | như web | Badge: lề phía chữ SM · MD · LG (DEC-310) |
| `space/sm` · `space/md` · `chip/padding-x-icon-lg` · `space/xs` · `space/sm` · `space/xxs` · `size/sm` | 6 · 8 · 10 · 4 · 6 · 2 · 6 | như web | Badge: lề phía chấm/icon; icon → chữ 4; chấm → chữ 6 (= 4 + 2); chấm 6 (DEC-310) |
| `table/row-min-height` · `table/cell-padding-y` · `table/cell-padding-x` | 52 · 16 · 24 | 52 · 12 · 16 | Bảng theo Untitled (DEC-259). |
| `size/xl` · `size/xl` · `size/2xl` · `radius/xxs` · `radius/xs` · `chip/count-inset` · `space/xs` · `space/xs` | 16 · 16 · 20 · 2 · 4 · 3 · 4 · 4 | như web | Badge: ô đếm cao SM · MD · LG; bo ô đếm; khi có ô đếm lề phải thu về 3 (SM) · 4 (MD, LG) để ô cách đều trên, dưới, phải; Count Only đệm trái khung số 4 để số cách đều hai bên (DEC-303, DEC-310) |
| `avatar-label/width` | 240 | 240 | Avatar label: rộng mặc định, tên và dòng phụ cắt "…" (DEC-303) |
| `chip/count-font-size` · `chip/count-line-height` · `avatar-label/subtitle-size` · `avatar-label/subtitle-line-height` | 12 · 16 · 12 · 16 | 12 · 16 · 12 · 16 | Chữ số đếm Badge và dòng phụ Avatar label cố định 12/16 cả web và app — không theo `type/caption` (app 13/18) để giữ nhóm A cùng số đo (DEC-304) |
| `avatar/size/xs · sm · md · lg · xl · xxl` | 24 · 32 · 36 · 48 · 64 · 88 | 24 · 32 · 36 · 48 · 64 · 88 | Cỡ avatar thang XS–XXL (DEC-201, DEC-203; thêm SM 32 và đổi tên sm → xs, DEC-303); MD 36 khớp ô đầu dòng 36 (DEC-164); XL, XXL cho ảnh đại diện đổi được |
| `avatar/status-size/xs · sm · md · lg · xl · xxl` · `size/xxs` | 6 · 8 · 10 · 12 · 14 · 16 · 2 | 6 · 8 · 10 · 12 · 14 · 16 · 2 | Chấm trạng thái avatar, thêm viền trắng 2 (DEC-204); SM 8 và đổi tên theo thang XS–XXL; viền chấm Offline rỗng 2 (DEC-303) |
| `avatar/edit-size/md · lg · xl · xxl` | 20 · 24 · 28 · 32 | 20 · 24 · 28 · 32 | Nút đổi ảnh trên avatar (SM không có; DEC-203) |
| `avatar/icon-size/sm · md · lg · xl · xxl` | 14 · 20 · 24 · 24 · 24 | 14 · 20 · 24 · 24 · 24 | Icon trong avatar Content=Icon và Upload (DEC-242) |
| `avatar/edit-icon-size/md · lg · xl · xxl` | 12 · 14 · 16 · 16 | 12 · 14 · 16 · 16 | Icon camera trong nút đổi ảnh (DEC-242) |
| `avatar/spinner-size/sm · md · lg · xl · xxl` | 12 · 16 · 20 · 24 · 28 | 12 · 16 · 20 · 24 · 28 | Vòng quay Uploading (DEC-242) |
| `avatar/group-overlap/sm · md · lg` · `size/xxs` | −6 · −8 · −12 · 2 | −6 · −8 · −12 · 2 | Avatar Group: khoảng giữa là số âm = lùi đè ¼ đường kính, gắn vào itemSpacing; viền trắng 2; bước giữa hai tâm = cỡ + 4 − lùi = 22 · 32 · 40 (DEC-205, DEC-242) |
| `tooltip/padding-x · padding-y` · `space/xs` · `tooltip/max-width` | 8 · 4 · 4 · 240 | 8 · 4 · 4 · 240 | Tooltip: lề, cách đối tượng, rộng tối đa; bo `radius/md` 8, mũi tên 8 × 4 (DEC-206) |
| `progress/height/sm · md` · `space/xxs` · `progress/width-default` | 4 · 6 · 2 · 320 | 4 · 6 · 2 · 361 | `Base / Progress`: cao thanh, khe giữa nhóm đoạn, rộng mặc định (DEC-243) |
| `otp/cell-width` | 40 | 48 | Rộng một ô mã OTP; app dùng, web chưa dựng (DEC-244) |

- Mọi số trên thang 4; DEC-164 bỏ ngoại lệ lề thẻ app 14. Không thêm số lẻ ngoài thang.
- **Ô đầu dòng (DEC-164, app):** ô 24 cho icon 16 và 20, radio, ô chọn, cách chữ 8; ô 36 cho vòng icon, avatar, cách chữ 12.
  Icon đầu dòng luôn đặt giữa ô, không đặt trần. Trừ khung có nền: icon đầu khối phụ, khối tóm tắt (DEC-194), icon đầu
  ô tìm, ô nhập và radio thẻ chọn (DEC-196) chạm mép nội dung; và icon cuối dòng (mục 7, DEC-193). Cỡ ô 24 và 36 chưa có token sau khi bỏ `card/*` (DEC-312), chờ chốt thang kích thước ở trang Token ↔ Component.
- **Form (DEC-166):** đặt trên nền trang (nhóm bằng tiêu đề nhóm, web cách nhau 32) hoặc mỗi nhóm một thẻ (web lề 24
  = `space/3xl`, app theo `layout/card-padding`); người vẽ chọn theo màn.
- **Tiêu đề (DEC-192):** tiêu đề màn → nội dung `layout/title-gap`; tiêu đề khối → nội dung khối 12 (`space/lg`).
  Tiêu đề khối đặt trong thẻ, nhóm, không đặt ngoài.
- **Form (DEC-184, DEC-192):** giữa 2 ô `form/field-gap`; ô → dòng gợi ý 4 (`space/xs`); tiêu đề nhóm → ô 12; giữa 2
  nhóm ô `layout/section-gap`; form web 2 cột cách 24 (`space/3xl`). Chữ gợi ý, chữ lỗi dưới ô: app lùi 16 thẳng chữ
  trong ô (K2 32), web canh mép ô.
- **Nút (DEC-162, DEC-163, DEC-192):** lề `control/padding-x/*` theo cỡ, phía có icon `control/padding-x-icon/*`, icon →
  chữ `control/icon-gap`. Hai nút cạnh nhau trên app cách 12 (`space/lg`).
- **Tab (DEC-161, DEC-164, DEC-192):** tab chip app cao 36 (`control/height/sm`): lề `tab/padding-x`, phía icon
  `tab/padding-x-icon`, icon → nhãn `control/icon-gap`, nhãn → số đếm 6 (`space/6`), các tab cách `tab/gap`. Tab gạch web
  cao 40 (`control/height/lg`), chữ canh giữa, gạch 2 phủ hết bề ngang tab.
- **Ô có icon (DEC-192, DEC-193, DEC-196):** web phía icon 12 → 8 (icon đầu, icon cuối), icon 14 cách chữ 8. App icon đầu:
  khung icon 16 (icon 14 canh giữa khung từ DEC-329, K không đổi) chạm mép nội dung (cách mép ô 16), chữ cách khung 16 → K3 64 (ô ở K1) hoặc K4 80 (ô đặt trong thẻ). Icon cuối
  ô theo đường K bên phải (mục 7). Nút lọc trong ô tìm giữ ôm sát (DEC-165 luật 3: lề 4, bo đồng tâm).
- **Thẻ chọn app (DEC-184, DEC-196):** lề 16; radio 20 chạm mép nội dung (cách mép thẻ 16), chữ cách radio 12 → K3 64.
- **Khối phụ trong thẻ, khối tóm tắt trong sheet (DEC-194):** nền `color/bg/secondary`, bo `radius/inner`, lề
  `layout/card-padding` 16 đều 4 phía. Khối phụ trong thẻ (đặt ở K2 32) có mép nội dung trái **K2b 48**, phải 345; khối tóm
  tắt trong sheet (đặt ở K1 16) có mép nội dung K2 32. Không icon: chữ ở mép nội dung. Có icon: khung icon 16 chạm mép nội
  dung, không đặt trong ô 24; chữ cách icon 16 (khối phụ: chữ K4 80; khối tóm tắt: chữ K3 64). Lề nhìn thấy từ mép nền tới
  icon bằng lề 16.
- **Thanh điều hướng app (DEC-160):** thanh nổi rộng 361 (393 − 2 × 16), cao `nav/height`, bo 24 (28 → 24, DEC-259), cách vùng an toàn
  `nav/offset-bottom`, lề trong `nav/padding-x`; mục lề trên dưới `nav/item-padding-y` nên nền mục đang chọn cao 56, bo
  20 = 24 − 4 (đồng tâm, DEC-165); icon 24; nút Quét mã `nav/scan-size`.

