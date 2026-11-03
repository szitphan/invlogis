---
type: design-foundations
status: draft
updated: 2026-11-02
links:
  - design-system/foundations/README.md
  - design-system/tokens.json

---

# Foundations · Khoảng cách

> Một phần của [[design-system/foundations/README.md|Foundations]]. Giữ số mục cũ (6.x) để các DEC và spec trích "foundations mục 6…" vẫn tra được. Giá trị máy đọc: `design-system/tokens.json` (json thắng). Lề trong component theo dạng nội dung đã tách sang [[design-system/foundations/padding.md|Auto layout component]] (DEC-342, DEC-343); token `control/*`, `chip/*`, `tab/*` trong bảng dưới chờ mục đó chốt.

## 6. Khoảng cách (DEC-135, DEC-164, DEC-166, DEC-173, DEC-192, DEC-194, DEC-196, DEC-232, DEC-234, DEC-239, DEC-242, DEC-243, DEC-244, DEC-341)

- Bảng gốc (Primitives), tên theo px, đủ 32 bậc Untitled (DEC-341 sp00): `space/0 · 2 · 4 · 6 · 8 · 12 · 16 · 20 · 24 · 32 · 40 · 48 · 64 · 80 · 96 · 128 · 160 · 192 · 224 · 256 · 320 · 384 · 480 · 560 · 640 · 720 · 768 · 1024 · 1280 · 1440 · 1600 · 1920`. Bậc riêng: `space/10` (Badge), `space/14`, `space/28`, `space/36` (chỉ cho cỡ).
- **Thang Semantic theo Untitled (DEC-314)**, Web = Mobile, dùng cho mọi lề trong và khoảng giữa phần tử (thay `space/inset-*`,
  `space/gap-*` cũ):

  | `space/…` | none | xxs | xs | sm | md | lg | xl | 2xl | 3xl | 4xl | 5xl | 6xl | 7xl | 8xl | 9xl | 10xl | 11xl |
  |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
  | px | 0 | 2 | 4 | 6 | 8 | 12 | 16 | 20 | 24 | 32 | 40 | 48 | 64 | 80 | 96 | 128 | 160 |

  Tên cũ → mới: `gap-2xs` → `xxs` · `inset-xs`, `gap-xs` → `xs` · `inset-sm`, `gap-sm` → `md` · `inset-md`, `gap-md` → `lg` ·
  `inset-lg`, `gap-lg` → `xl` · `inset-xl`, `gap-xl` → `3xl` · `gap-2xl` → `4xl`.
- **Bậc riêng `size/14`, `size/28`, `size/36`, primitive `space/14`, `space/28`, `space/36` (DEC-329 ic05; DEC-341 sp08, mở lại DEC-314):** lệch thang Untitled do user chọn, chỉ cho cao, cỡ khối, cỡ icon, không dùng cho khoảng cách. Không thêm 18 vì cỡ 18 đã bỏ.
- **Thang kích thước `size/…`** (collection `5. Platform · Sizes`, DEC-314): cùng tên, cùng bậc như `space/…`; token component
  dùng cho cao, rộng, cỡ khối. Token component (`6.`) chỉ trỏ `space/…`, `size/…`, `type/…`, `radius/…` Semantic, không trỏ Primitive.
  Token vai (`layout/*`, `form/*`, `control/*`, `tab/*`, `nav/*`) trỏ thang Semantic, thang trỏ Primitive, số khớp Untitled (DEC-341 sp02). Component còn gọi Primitive sửa khi sync.

| Token | Web | App | Dùng cho |
|---|---|---|---|
| `grid/margin` | 32 | 16 | Lề màn, trỏ `container/padding-*` (DEC-324) |
| `layout/empty-padding` | 64 | 64 | Lề trên dưới màn trống, màn kết quả, đăng nhập (Web = App, DEC-341 sp04) |
| `container/max-width-desktop` | 1280 | — | Rộng tối đa màn chi tiết, form, gồm lề; màn bảng trải hết (DEC-324) |
| `layout/card-padding` | 16 | 16 | Lề chứa: lề trong thẻ, nhóm có viền, dòng trong nhóm (app 14 → 16, DEC-164). Thẻ form web `space/3xl` (DEC-166, DEC-341 sp05) |
| `layout/list-gap` | 12 | 12 | Giữa các thẻ, dòng trong danh sách |
| `layout/section-gap` | 24 | 24 | Giữa các khối lớn |
| `layout/title-gap` | 16 | 16 | Tiêu đề màn → nội dung |
| `form/field-gap` | 16 | 16 | Giữa 2 ô nhập trong một nhóm |
| `touch/min` | 24 | 44 | Vùng chạm tối thiểu (web: WCAG 2.2 AA 24; app: DEC-138). Con trỏ thô trên web đọc số của app (DEC-339) |
| `focus/width` | 2 | 2 | Độ dày vòng focus |
| `focus/offset` | 2 | 2 | Khoảng cách vòng focus tới mép control |
| `control/height/sm · md · lg` | 28 · 32 · 40 | 36 · 44 · 52 | Cao nút, ô nhập, ô chọn; cùng cỡ thì cùng cao (DEC-173; app MD 42 → 44, DEC-341 sp10) |
| `control/height/ml` | 36 | 44 | Nút icon, avatar thanh trên web; app không dùng, Mobile bằng MD (user 02/11) |
| `control/padding-x/sm · md · lg` | 10 · 12 · 16 | 12 · 16 · 24 | Lề trái phải trong nút theo cỡ (nút app 52 lề 24, DEC-163; Web SM 10, DEC-346) |
| `control/padding-x-icon/sm · md · lg` | 8 · 10 · 14 | 8 · 12 · 20 | Lề phía có icon trong nút: Web lùi 2 như Untitled, App lùi 4 (DEC-346) |
| `control/label-inset` | 2 | 4 | Bọc chữ của nút; khoảng 4 + bọc = icon → chữ Web 6, App 8 (DEC-346) |
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
| `chip/padding-x-sm` · `chip/padding-x-icon-lg` · `chip/padding-x-lg` | 8 · 10 · 12 | như web | Badge: lề phía chữ SM · MD · LG theo Untitled (DEC-341 sp01, mở lại DEC-310) |
| `space/sm` · `space/md` · `chip/padding-x-icon-lg` · `space/xs` · `space/sm` · `space/xxs` · `size/sm` | 6 · 8 · 10 · 4 · 6 · 2 · 6 | như web | Badge: lề phía chấm/icon; icon → chữ 4; chấm → chữ 6 (= 4 + 2); chấm 6 (DEC-310) |
| `table/row-min-height` · lề ô trên dưới · lề ô trái phải | 52 · `space/xl` 16 · `space/3xl` 24 | 52 · `space/lg` 12 · `space/xl` 16 | Bảng theo Untitled (DEC-259); lề ô gán thẳng bậc (DEC-341 sp06) |
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
| `progress/height/sm · md` · `space/xxs` · `progress/width-default` | 4 · 6 · 2 · 320 | 4 · 6 · 2 · rộng đầy | `Base / Progress`: cao thanh, khe giữa nhóm đoạn, rộng mặc định (DEC-243) |
| Rộng một ô mã OTP | `size/5xl` 40 | `size/6xl` 48 | App dùng, web chưa dựng (DEC-244); gán thẳng bậc (DEC-341 sp06) |

- Thang 4 là mặc định; số lệch thang phải có tên và lý do hoặc công thức trong bảng ngoại lệ dưới đây (DEC-341). DEC-164 bỏ ngoại lệ lề thẻ app 14.
- **Bảng ngoại lệ (DEC-341 sp07, sp08, sp09):**

  | Token | Số | Công thức, lý do |
  |---|---|---|
  | `space/md-lg` · `space/lg-xl` | 10 · 14 | Bậc Semantic ngoài thang Untitled: lề Badge, lề nút Web phía icon (DEC-341, DEC-346) |
  | `nav/child-indent` | 36 | Dòng con `_Nav item`: 8 + 20 + 8 (DEC-346) |
  | Tooltip gap, số trần | −1 | Mũi tên chồng lên khung (DEC-346) |
  | `_Tag close X` · `Map Pin` · `Page header`, số trần | 3 · 3 · −32 | Ngoài thang, giữ nguyên ở đợt DEC-346, chưa xác minh công thức |
  | `command-search/highlight-padding-x` | 1 | Nền chữ khớp, lớn hơn làm giãn chữ |
  | `chip/count-inset` | 3 | (`chip/height-sm` 22 − ô đếm 16) / 2 |
  | `avatar/group-overlap/sm · md · lg` | −6 · −8 · −12 | −¼ đường kính (DEC-205) |
  | `chip/height-sm` | 22 | Chữ 18 + 2 × 2 như Untitled Badge SM |
  | `table/row-min-height` | 52 | Chữ 20 + 2 × 16 |
  | `avatar/size/xxl` | 88 | Đầu trang hồ sơ (DEC-203) |
  | `avatar/status-size/md` | 10 | Untitled cũng dùng `size-2.5` |
  | `header-nav/height` | 44 · 56 | Thanh trên (DEC-305) |
  | `upload/app-tap-min-height` | 72 | Vùng bấm tải lên app (DEC-307) |
  | `avatar-label/width`, `tooltip/max-width`, `breadcrumbs/current-max-width`, `breadcrumbs/menu-min-width` | 240 | Thang không có bậc |
  | `header-nav/account-menu-width`, `command-search/width` | 256, 600 | Giữ riêng (DEC-324) |

- **Đã trỏ bậc (DEC-341 sp08):** 14 `size/14`: `avatar/icon-size/sm`, `avatar/edit-icon-size/lg`, `avatar/status-size/xl`. 28 `size/28`: `chip/height-lg` (chữ 20 + 2 × 4), `avatar/edit-size/xl`, `avatar/spinner-size/xxl`, `control/height/sm` web. 36 `size/36`: `avatar/size/md`, `featured-icon/size-compact`, `control/height/sm` app, `control/height/ml` web.
- **Rộng (DEC-341 sp09):** ô nhập, thanh tiến độ app rộng đầy, không ghi số; ảnh tính theo tỉ lệ (DEC-334). `upload/compact-text-min-width` `size/11xl` 160, `field/label-max-width` 320.
- **Ô nhập, gán thẳng bậc theo khối Web, App (DEC-341 sp06, thay `field/*` theo chế độ):** mép ô → khối đầu Web `space/md` · App `space/xl`; lề vùng chữ Web `space/xs` · App `space/none`; icon → vùng chữ Web `space/xs` · App `space/xl`; lề dòng gợi ý Web `space/none` · App `space/xl`. Hai nút trong Notification: Web `space/lg` · App `space/3xl`. CSS đọc theo `[data-platform]`.
- **Đường canh app (DEC-341 sp11, user 02/11):** bỏ hẳn đường K của DEC-164 và không có luật canh chữ theo cột. Lưới app chỉ canh khối (`grids.md`); khoảng từ phần đầu dòng tới chữ theo token dưới đây.
- **Ô đầu dòng (DEC-164, app):** ô 24 cho icon 16 và 20, radio, ô chọn; ô 36 cho vòng icon, avatar. Ô → chữ `space/md` 8.
  Icon đầu dòng luôn đặt giữa ô, không đặt trần. Trừ khung có nền: icon đầu khối phụ, khối tóm tắt (DEC-194), icon đầu
  ô tìm, ô nhập và radio thẻ chọn (DEC-196) chạm mép nội dung; và icon cuối dòng (mục 7, DEC-193). Cỡ ô: `size/3xl` 24, `size/36` 36 (DEC-341 sp08).
- **Form (DEC-166):** đặt trên nền trang (nhóm bằng tiêu đề nhóm, cách nhau `layout/section-gap` 24) hoặc mỗi nhóm một thẻ (web lề 24
  = `space/3xl`, app theo `layout/card-padding`); người vẽ chọn theo màn.
- **Tiêu đề (DEC-192):** tiêu đề màn → nội dung `layout/title-gap`; tiêu đề khối → nội dung khối 12 (`space/lg`).
  Tiêu đề khối đặt trong thẻ, nhóm, không đặt ngoài.
- **Form (DEC-184, DEC-192):** giữa 2 ô `form/field-gap`; nhãn → ô → dòng gợi ý 6 (`space/sm`, DEC-346 thay DEC-184); tiêu đề nhóm → ô 12; giữa 2
  nhóm ô `layout/section-gap`; form web 2 cột cách 24 (`space/3xl`). Chữ gợi ý, chữ lỗi dưới ô: app lùi `space/xl` 16 thẳng chữ
  trong ô, web canh mép ô.
- **Nút (DEC-162, DEC-163, DEC-192):** lề `control/padding-x/*` theo cỡ, phía có icon `control/padding-x-icon/*`, icon →
  chữ `control/icon-gap`. Hai nút cạnh nhau trên app cách 12 (`space/lg`).
- **Tab (DEC-161, DEC-164, DEC-192):** tab chip app cao 36 (`control/height/sm`): lề `tab/padding-x`, phía icon
  `tab/padding-x-icon`, icon → nhãn `control/icon-gap`, nhãn → số đếm 6 (`space/sm`), các tab cách `tab/gap`. Tab gạch web
  cao 40 (`control/height/lg`), chữ canh giữa, gạch 2 phủ hết bề ngang tab.
- **Ô có icon (DEC-192, DEC-193, DEC-196):** web phía icon 12 → 8 (icon đầu, icon cuối), icon 14 cách chữ 8. App icon đầu:
  khung icon 16 chạm mép nội dung (cách mép ô 16), icon → chữ `space/xl` 16. Icon cuối
  ô canh mép phải nội dung (mục 7). Nút lọc trong ô tìm giữ ôm sát (DEC-165 luật 3: lề 4, bo đồng tâm).
- **Thẻ chọn app (DEC-184, DEC-196):** lề 16; radio 20 chạm mép nội dung (cách mép thẻ 16), radio → chữ `space/lg` 12.
- **Khối phụ trong thẻ, khối tóm tắt trong sheet (DEC-194):** nền `color/bg/secondary`, bo `radius/inner`, lề
  `layout/card-padding` 16 đều 4 phía. Mép nội dung cách mép nền 16 ở cả hai loại. Không icon: chữ ở mép nội dung. Có icon: khung icon 16 chạm mép nội
  dung, không đặt trong ô 24; icon → chữ `space/xl` 16. Lề nhìn thấy từ mép nền tới
  icon bằng lề 16.
- **Thanh điều hướng app (DEC-160):** thanh nổi rộng đầy trừ `grid/margin` (361 ở khung 393), cao `nav/height`, bo 24 (28 → 24, DEC-259), cách vùng an toàn
  `nav/offset-bottom`, lề trong `nav/padding-x`; mục lề trên dưới `nav/item-padding-y` nên nền mục đang chọn cao 56, bo
  20 = 24 − 4 (đồng tâm, DEC-165); icon 24; nút Quét mã `nav/scan-size`.

