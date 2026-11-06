---
type: design-system-component
status: draft
updated: 2026-11-07
links:
  - design-system-antd/foundations/foundations.md
  - design-system-antd/token-mapping.md
  - design-system-antd/components/button.md
  - design-system-antd/components/input.md
---

# Radio — `nz-radio` · `nz-radio-group` · `nz-radio-button`

> Bộ thử AntD. Giao diện theo **shadcnuikit.com/components/radio-group** (15 ví dụ, registry `radio-group1…15`);
> nhóm nút (radio button) lấy từ **ng-zorro** vì web không có; thuộc tính theo **API ng-zorro 22.x**.
> Lựa chọn giữ/bỏ: trang claude.ai/artifact/3eRLKXBhZLRfpBS1rcJ6Bx tab Radio (user bấm 06/11): theo cột đề xuất,
> **giữ thêm** Nhóm nút đặc (`btn-s`), Thẻ chọn (`card`), web-07, web-11, web-14, web-15; **bỏ** Thanh chuyển
> (`nz-segmented` — để đợt Tabs), web-03, web-06, web-13 (`nz-rate`).
> Nút tròn theo **token** (viền xám + chấm), không theo kiểu web shadcnuikit (nền xám không viền, chọn tô đặc).

## 1. Thuộc tính

| ng-zorro | Figma property | Giá trị dùng | Ghi chú |
|---|---|---|---|
| `nz-radio` + `ngModel` | `Chọn` (variant) | Chưa chọn · Đã chọn | Đã chọn: viền + chấm 8 màu chính |
| `nzDisabled` | `Trạng thái` = Đã tắt | mờ 50% | Tắt cả nhóm: `nz-radio-group nzDisabled` |
| focus bàn phím · lỗi form | `Trạng thái` = Focus · Lỗi | vòng 3px | Lỗi lấy từ `nz-form-control` (radio không có `nzStatus`) |
| nội dung nhãn | `Nhãn` (boolean) + `Nhãn · chữ` | chữ 14 | Tắt khi chỉ cần nút tròn (trong thẻ, dòng bảng) |
| nhãn phụ · mô tả (tự ghép) | `Nhãn phụ` + `Nhãn phụ · chữ` · `Mô tả` + `Mô tả · chữ` | chữ 12 xám | Nhãn phụ nằm cùng dòng nhãn, mô tả xuống dòng cách 2 |
| `nz-radio-group` | khung ghép auto-layout | dọc cách 12 · ngang cách 16 | Không làm component nhóm — instance không thêm/bớt mục |
| `nz-radio-button` | Set `Radio nút`: `Vị trí` | Đầu · Giữa · Cuối | Ghép nhóm: khoảng cách −1, mục đầu nằm trên cùng |
| `nzButtonStyle` | `Kiểu` | `outline` → Viền · `solid` → Đặc | Đặc: mục chọn nền màu chính, chữ trắng |
| `nzSize` | — | chỉ default 36 | sm 32 · lg 40 chưa dựng biến thể — dev đổi theo `height/*` |
| thẻ + `nz-radio` (tự ghép) | Set `Radio thẻ`: `Kiểu` Ngang · Dọc | `Giá` · `Tiêu đề` · `Mô tả thẻ` · `Icon` | Cả thẻ bấm được (`label` bọc `nz-radio`) |
| `nz-radio-button` tự trang trí | Set `Radio ô`: `Kiểu` Icon · Chữ | `Chữ` · `Chữ ô` · `Icon` | Ẩn nút tròn, bấm cả ô |
| ô màu (tự dựng) | Set `Radio màu` | override fill `Màu` + stroke `Vòng chọn` | Màu gắn biến `color/*` |

**Không dùng:** Thanh chuyển `nz-segmented` (component riêng, đợt Tabs) · web-03 đổi màu indigo (một màu chính cho
mọi control chọn) · web-06 lọc theo số sao (chưa có nghiệp vụ) · web-13 chấm sao (`nz-rate`, component khác).

## 2. Radio đơn — set `Radio`

| Phần | Giá trị | Token |
|---|---|---|
| Nút | tròn 16, viền 1px xám, không nền, bóng `shadow/xs`, lệch xuống 2 để giữa dòng chữ 20 | `radio/size` · `color/border-base` · `radius/full` |
| Chấm (đã chọn) | tròn 8 màu chính, viền nút đổi màu chính | `radio/dot-size` · `color/primary` |
| Nhãn | chữ 14/20 Regular, cách nút 8 | `text/base/regular` · `radio/gap` |
| Nhãn phụ | chữ 12 xám, cùng dòng, cách nhãn 4 | `text/sm/regular` · `color/text-secondary` |
| Mô tả | chữ 12 xám, dưới nhãn cách 2 | `text/sm/regular` · `radio/desc-gap` |

| Trạng thái | Cách thể hiện | Token |
|---|---|---|
| Thường | như trên | |
| Focus | vòng 3px ngoài nút (−3) | `focus/width` · `color/focus-ring` |
| Lỗi | viền đỏ + vòng đỏ 20% | `color/error` · `color/focus-error-ring` |
| Đã tắt | mờ cả radio 50% | `opacity/disabled` |

Rê chuột: không đổi hình (shadcn không có hover cho radio) — dev giữ mặc định trình duyệt.

## 3. Nhóm nút — set `Radio nút`

Một ô của `nz-radio-group` dạng nút. Cao `height/base` 36, padding ngang `radio/button-padding-x` 15 (+ viền 1 = 16
như CSS), chữ 14 Medium, nền `color/body-bg`, viền 1px `color/border-base`. Bo `radius/base` 8 chỉ ở mép ngoài:
Đầu bo trái, Cuối bo phải, Giữa vuông.

| Trạng thái | Viền | Đặc |
|---|---|---|
| Chưa chọn | viền xám, chữ `color/text` | như Viền |
| Đã chọn | viền `color/primary` | nền `color/primary`, chữ `color/primary-foreground` |
| Focus | vòng 3px quanh ô (bo theo mép ngoài) | như Viền |
| Đã tắt | mờ 50% | như Viền |

Ghép nhóm: auto-layout ngang, khoảng cách **−1** (viền chồng nhau như AntD), bật *Canvas stacking: first on top*
để mục đang chọn (thường là mục đầu) hiện đủ viền màu chính.

## 4. Thẻ chọn, ô chọn, ô màu

| Set | Hình | Token |
|---|---|---|
| `Radio thẻ` Ngang (web-08) | rộng 240 (kéo giãn được), padding 12, bo 10, viền 1px xám; trong là `Radio` có mô tả + `Giá` chữ 12 xám bên phải | `radio/card-padding` · `radius/lg` · `color/border-base` |
| `Radio thẻ` Dọc (web-14) | rộng 120, giữa: icon 20 · tiêu đề 14 Medium · mô tả 12 · nút tròn dưới cùng, cách 6 | `spacing/6` |
| `Radio ô` Icon (web-09) | rộng 96, padding 12 · 4, bo 8, icon 20 mờ 60% + chữ 12 Medium, cách 8 | `radius/base` · `spacing/sm` · `spacing/xs` |
| `Radio ô` Chữ (web-10) | rộng 72, padding 10 · 4, chữ 14 Medium | `radius/base` |
| `Radio màu` (web-07) | chấm 24 màu; chọn = vòng 2px cùng màu ngoài khung 32 (cách 2) | `radio/swatch-size` |

Đã chọn (thẻ, ô): viền 1px `color/primary` + bóng tràn 1px `color/primary` = viền 2px nhưng không đẩy nội dung
(như CSS `border` + `box-shadow 0 0 0 1px`). Focus: vòng 3px ngoài; Đã tắt: mờ 50%.

## 5. Mẫu ghép

| Mã | Ví dụ | ng-zorro | Dùng ở Invlogis |
|---|---|---|---|
| basic | Tròn | `nz-radio` | Giao tận nơi / Khách tự lấy |
| desc | Kèm mô tả | nhãn + mô tả | Phương án cần giải thích: "Ghép chuyến — rẻ hơn, giao chậm 1 ngày" |
| disabled | Đã tắt | `nzDisabled` | Tuyến cố định không đổi được |
| btn-o | Nhóm nút — viền | `nz-radio-button` | Chuyển nhanh kỳ xem: Hôm nay / Tuần / Tháng |
| btn-s | Nhóm nút — đặc | `nzButtonStyle="solid"` | Như btn-o, cần nhấn mạnh mục đang chọn (giữ 06/11) |
| card | Thẻ chọn | thẻ + `nz-radio` | Chọn loại xe, phương án giao — cả thẻ bấm được (giữ 06/11) |
| web-01 | Nhóm dọc | `nz-radio-group` dọc | Mặc định trong form: kỳ tính cước theo chuyến / ngày / tháng |
| web-02 | Nhóm ngang | `nz-radio-group` ngang | Ít lựa chọn, nhãn ngắn: Giao tận nơi · Khách tự lấy |
| web-04 | Nhãn + nhãn phụ + mô tả | nhãn + mô tả | Hình thức thanh toán: Chuyển khoản (VCB, Techcombank) / Công nợ |
| web-05 | Chọn để mở ô nhập | `nz-radio` + `nz-input` hiện khi chọn | "Giao tận nơi" → hiện ô địa chỉ giao; "Khách tự lấy" → ẩn |
| web-07 | Ô màu | tự dựng | Màu nhãn tuyến / đội xe trên bản đồ (giữ 06/11 — đề xuất cũ bỏ vì chưa có nghiệp vụ) |
| web-08 | Thẻ — nhãn + giá | thẻ + `nz-radio` | Chọn loại xe kèm giá: "Xe tải 5 tấn · 2.400.000 ₫" |
| web-09 | Ô vuông có icon | `nz-radio-button` tự trang trí | Hình thức thanh toán trên app tài xế: Tiền mặt / Chuyển khoản / Công nợ |
| web-10 | Lưới ô chữ, có ô khoá | `nz-radio-button` tự trang trí | Tải trọng xe 1,5 · 2,5 · 3,5 · 5 · 8 · 10 tấn; loại đang hết xe bị khoá |
| web-11 | Thẻ nhỏ xếp hàng | thẻ + `nz-radio` | Khu vực giao Bắc / Trung / Nam (giữ 06/11 — trùng web-08 và btn-o, dùng khi nhãn dài hơn nút) |
| web-12 | Danh sách liền khối + giá + nhãn | `nz-radio-group` + `nz-tag` | Phương án giao Nhanh 4 giờ / Tiêu chuẩn ("Đề xuất") / Tiết kiệm / Ghép chuyến, giá bên phải |
| web-14 | Thẻ dọc có icon | thẻ + `nz-radio` | Nguyên chuyến / Ghép hàng (giữ 06/11 — thẻ dọc tốn chỗ, hợp màn mobile) |
| web-15 | Thẻ gói + giá + tính năng | thẻ + `nz-radio` + `nz-tag` | Chọn gói thuê bao Invlogis cho khách SaaS (giữ 06/11) |

Mẫu ghép là component `Radio mẫu ghép/{mã} …`, ghép từ instance các set trên. web-12 và web-15 là **khung ghép**
cùng token (viền, bo, padding) vì danh sách liền khối / thẻ gói có nội dung tự do; dòng chọn của web-12 dùng nền
`color/item-active-bg` + viền trong 1px `color/primary`. Thẻ "Đề xuất" / giá gói là pill tạm cùng token `tag/*`
(set Tag dựng riêng) — thay bằng instance Tag khi có.

## 6. Figma

File `ElvhTYV3unixPkXky2oKIY`, trang **Radio** (`67:3385`) — dựng 07/11, chờ duyệt:

| Khối | Node | Nội dung |
|---|---|---|
| Frame `Radio` (tài liệu) | `69:408` | Đầu trang · Playground **Light** `69:416` / **Dark** `69:435` · `Ví dụ đã chốt` (18 thẻ) · `Mapping` (12 thuộc tính + 13 token) |
| Section Components | `67:3767` | Set `Radio` `67:3768` = Chọn (2) × Trạng thái (4) = **8** · `Radio nút` `67:6514` = Kiểu (2) × Vị trí (3) × Chọn (2) × Trạng thái (3) = **36** · `Radio thẻ` `67:7131` = Kiểu (2) × Chọn (2) × Trạng thái (3) = **12** · `Radio ô` `67:8833` = Kiểu (2) × Chọn (2) × Trạng thái (3) = **12** · `Radio màu` `67:8863` = Chọn (2) × Trạng thái (3) = **6** |
| Section Mẫu ghép | `67:11466` | 18 component `Radio mẫu ghép/{mã} …` (`67:11467`…`67:11679`, `68:255`…`68:574`) |
| Section Icons (trang Radio) | `67:3398` banknote · `67:3406` landmark · `67:3411` receipt | lucide 16, viền gắn `color/text` |
| Biến mới (collection size) | `radio/size` · `dot-size` · `gap` · `desc-gap` · `button-padding-x` · `card-padding` · `swatch-size` | `VariableID:67:3386…67:3392` |

Thuộc tính `Radio`: `Nhãn` + `Nhãn · chữ` · `Nhãn phụ` + `Nhãn phụ · chữ` · `Mô tả` + `Mô tả · chữ`.
`Radio nút`: `Chữ`. `Radio thẻ`: `Giá` + `Giá · chữ` (Ngang) · `Tiêu đề · chữ` + `Mô tả thẻ · chữ` + `Icon` (Dọc);
`Radio` bên trong được expose để sửa nhãn/mô tả từ thẻ. `Radio ô`: `Chữ` + `Icon` (Icon) · `Chữ ô` (Chữ).

Chưa xong: chưa có biến thể cỡ sm/lg cho `Radio nút`; Focus ở mục giữa nhóm nút bị mục đầu che một phần vòng
(thứ tự lớp "first on top").
