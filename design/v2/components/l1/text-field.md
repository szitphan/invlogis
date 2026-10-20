---
type: design-component
status: draft
updated: 2026-10-20
links:
  - design/v2/architecture.md
  - design/v2/foundations.md
  - design/v2/tokens.json
  - _workspace/decisions.md
---

# Base / Text Field

> L1 · phiên bản 0.2.0 · Nháp · người phụ trách @szitphan · Figma `Base / Text Field` (6423:21911) và
> `Base / Text Field / Mobile` (6423:81962), trang DS · Components · L0–L3, Section `Text Field · L1 · Component Base`
> (6444:24184) · khung tài liệu `Tài liệu · Text Field` (6467:84336, Section `Text Field · Tài liệu` 6444:24190) ·
> DEC-173, DEC-174, DEC-177, DEC-184, DEC-192, DEC-196, DEC-207, DEC-210, DEC-213, DEC-245 (một md cho hai component),
> DEC-246 (chữ mặc định) · cùng họ [OTP Field](otp-field.md)

Hai component vì hai bản khác cấu tạo: web nhãn đặt **trên** ô, app nhãn nằm **trong** ô; nhãn trong hay ngoài ô không
đổi được bằng mode Platform (DEC-207). Phần **Web** tả `Base / Text Field` (khối Web trên Figma đặt mode Platform = Web),
phần **Mobile** tả `Base / Text Field / Mobile` (component đặt sẵn mode Platform = Mobile). Mỗi phần tự đứng được: đọc
phần của nền tảng mình làm là đủ. Màu (collection Component, tiền tố `field/`) giống nhau ở hai nền tảng. Cả hai ráp từ
L0 (DEC-213), không lồng component L1 nào.

## Web

> Khối Web trên Figma đặt mode Platform = Web; mọi số dưới đây là giá trị mode Web.

### Tổng quan

- **Content:** Empty khi chưa nhập (chữ gợi ý `Placeholder`), Filled khi đã có giá trị (`Value`). Hai giá trị khác màu
  chữ nên là biến thể, không phải thuộc tính.
- **State:** Default · Hover · Focus (đang gõ) · Disabled · Error · Read Only.
- **Required:** dấu `*` đỏ đặt **sau** nhãn, cách 4 (DEC-207).
- **Icon:** Leading icon khi icon giúp nhận ra ô (tìm, ngày); Trailing icon cho mũi tên chọn, nút xoá, lịch. Cỡ 14.
- **Helper:** dòng gợi ý dưới ô, tắt bằng `Has Helper`. Ở State=Error chữ lỗi thay chỗ dòng gợi ý và luôn hiện.
- **Cỡ web:** MD 32 là cỡ chuẩn, mặc định khi kéo ra (DEC-210) · SM 28 cho ô lọc trong hàng bảng · LG 40 ở màn đăng
  nhập. Ô và nút cùng cỡ thì cùng cao, đặt cạnh nhau thẳng hàng (DEC-173).
- **Rộng:** mặc định 320 (`field/width-default`); đặt vào form thì kéo Fill theo cột form.
- **Chỉ có ở web:** nhãn trên ô, nền trắng viền 1px, Hover (nền rất nhạt, DEC-210); phía có icon lề lùi 12 → 8, icon →
  chữ 8 (DEC-192).
- **Giữa hai ô:** cách 16 (`form/field-gap`).
- **Chữ:** nhãn danh từ ngắn, viết hoa chữ đầu, không dấu hai chấm; chữ gợi ý là ví dụ thật hoặc "Nhập …"; chữ lỗi nói
  cái sai và cách sửa, không xin lỗi. Nhãn dài cắt "…" ở rộng tối đa 300 (`field/label-max-width`), dấu `*` vẫn ngay sau
  nhãn.
- **Báo lỗi:** ngay tại ô, không khoá nút gửi form (DEC-177).

### Cấu tạo

Hình phóng 2× trên Figma: Size MD · Content Filled · bật Required và Leading icon, tắt Helper (dòng gợi ý xem Trạng
thái); rộng rút còn 200 cho vừa ô hình.

| Phần | Token | Giá trị web |
|---|---|---|
| Nền | `field/bg/web`; Hover `field/bg/hover`; Disabled `field/bg/disabled`; Read Only `field/bg/readonly` | trắng · #F9FAFC · #F2F4F7 · #F2F4F7 |
| Viền | `field/border-width`, `field/border/default`; Focus `field/border-width-active` + `field/border/active`; Error `field/border/error`; Disabled `field/border/disabled`; Read Only không viền | 1px; Focus, Error 2px |
| Nhãn | L0 `.field / Label` Style=Web; thuộc tính Label; `type/label`; `field/fg/label-web`; trên ô cách `space/gap-xs` | 14/20 Medium; cách ô 4; rộng tối đa 300 |
| Dấu bắt buộc | thuộc tính Required; `field/fg/error`; cách nhãn `space/gap-xs` | cùng cỡ chữ nhãn; cách 4 |
| Khung ô | L0 `.field / Input`; cao `control/height/*`; rộng `field/width-default`; bo `radius/field` | 28 · 32 · 40; rộng 320; bo 8 |
| Chữ giá trị, gợi ý | Value `field/fg/value`, Placeholder `field/fg/placeholder`, Disabled `field/fg/disabled`; `type/body`; lề `field/edge-inset` + `field/text-inset` | 14/20; phía không icon chữ cách mép 8 + 4 = 12 |
| Icon | Leading icon, Trailing icon (đổi component, DS · Icons), bật bằng Has Leading Icon, Has Trailing Icon; `icon/size/sm`; `field/fg/icon`; icon → chữ `field/content-gap` + `field/text-inset` | 14; phía có icon lề 8; icon → chữ 4 + 4 = 8 (DEC-192) |
| Dòng gợi ý, lỗi | L0 `.field / Hint`; Helper `field/fg/helper`, Error text `field/fg/error`; `type/caption`; cách ô `space/gap-xs`; lề `field/hint-inset` | 12/16; cách ô 4; lề 0 (canh mép ô) |
| Dấu focus | không có vòng 2 cách 2: viền 2px `field/border/active` khi đang gõ chính là dấu focus (DEC-207) | 2px |

### Biến thể

Size × State × Content = 36 biến thể (3 × 6 × 2). Required, icon, Helper là thuộc tính bật tắt, không phải biến thể.
Lưới trên Figma: Content (Empty, Filled) × cấu hình thuộc tính (Mặc định · Required + Leading icon · Trailing icon không
Helper), Size MD, State Default.

### Trạng thái

| State | Trông thế nào |
|---|---|
| Default | nền trắng `field/bg/web`, viền 1px `field/border/default` |
| Hover | nền `field/bg/hover` (chỉ web; rất nhạt 1,04:1, giữ theo DEC-210) |
| Focus | đang gõ: viền 2px than chì `field/border/active` — cũng là dấu focus bàn phím, không thêm vòng (DEC-207) |
| Disabled | nền `field/bg/disabled`, viền `field/border/disabled`, mọi chữ `field/fg/disabled`; một kiểu xám, không làm mờ (DEC-174) |
| Error | viền 2px `field/border/error`; chữ lỗi caption đỏ thay chỗ dòng gợi ý (DEC-177) |
| Read Only | nền `field/bg/readonly`, không viền; chọn và sao chép được chữ, không sửa |

### Kích thước

| Size | Cao | Rộng mặc định | Chữ cách mép | Phía có icon | Dùng khi |
|---|---|---|---|---|---|
| SM | 28 | 320 | 12 | 8 | ô lọc trong hàng bảng |
| MD | 32 | 320 | 12 | 8 | mặc định (DEC-210) |
| LG | 40 | 320 | 12 | 8 | màn đăng nhập |

Bo 8, icon 14 ở mọi cỡ. Mọi cỡ ≥ `touch/min` 24 (WCAG 2.5.8).

### Nên và không nên

1. **Nên:** nhãn ngắn nêu đúng thứ cần nhập, luôn hiện trên ô; chữ gợi ý là ví dụ thật hoặc "Nhập …". **Không nên:** bỏ
   nhãn, chỉ để chữ gợi ý trong ô — gõ vào là mất nhãn, không còn biết ô này nhập gì.
2. **Nên:** báo lỗi ngay tại ô: viền đỏ 2px + chữ lỗi nói cái sai và cách sửa. **Không nên:** khoá nút Lưu khi ô còn
   thiếu mà không báo ô nào (DEC-177).

### Trợ năng — chấm theo WCAG 2.2

| Tiêu chí | KQ | Số đo, ghi chú |
|---|---|---|
| 1.4.3 Tương phản chữ (AA, ≥ 4,5) | ✓ | giá trị, nhãn 17,73 · chữ gợi ý, dòng gợi ý 5,43 (trên Hover 5,19) · chữ lỗi, dấu `*` 6,57 |
| 1.4.3 ngoại lệ — Disabled | ✓ | 2,34: được miễn (control không hoạt động) |
| 1.4.11 Tương phản ngoài chữ (AA, ≥ 3) | ✓ | viền nghỉ 5,43 · viền đang gõ 15,13 · viền lỗi 6,57 · Read Only không viền (nền 1,10 trên trắng): nhận ra nhờ nhãn và chữ |
| 2.4.7 Focus thấy được (AA) | ✓ | viền 2px than chì 15,13 khi focus bằng bàn phím; chính viền là dấu focus (DEC-207) |
| 2.5.8 Kích thước đích (AA, ≥ 24) | ✓ | SM 28 · MD 32 · LG 40 |
| 1.3.1 Thông tin và quan hệ | ✓ | nhãn là `<label for>`; bắt buộc đặt `aria-required` (dấu `*` chỉ để nhìn) |
| 3.3.1 Nhận biết lỗi · 3.3.3 Gợi ý sửa | ✓ | chữ lỗi dưới ô nói cách sửa; nối bằng `aria-describedby`, ô đặt `aria-invalid` |
| 1.4.1 Không chỉ dùng màu | ✓ | lỗi có viền dày hơn và chữ, không chỉ đổi màu |
| 4.1.2 Tên, vai trò | ✓ | tên lấy từ nhãn; Read Only đặt `readonly` (đọc, chọn được, không sửa) |
| 2.1.1 Bàn phím | ✓ | Tab tới ô theo thứ tự; Read Only vẫn vào được để chọn, sao chép |
| **Điểm web** | | **9/9 đạt** |

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| Size | Biến thể | MD (DEC-210) | SM 28 · MD 32 · LG 40 |
| State | Biến thể | Default | Default · Hover · Focus · Disabled · Error · Read Only |
| Content | Biến thể | Empty | Empty (chữ gợi ý) · Filled (giá trị) |
| Label | Chữ | Label | nhãn trên ô (L0 `.field / Label`) |
| Required | Bật tắt | tắt | dấu `*` đỏ sau nhãn |
| Placeholder | Chữ | Placeholder | chữ gợi ý khi Empty |
| Value | Chữ | Value | giá trị khi Filled |
| Helper | Chữ | Helper text | dòng gợi ý dưới ô |
| Has Helper | Bật tắt | bật | thuộc tính riêng của L1 |
| Error text | Chữ | Error text | chỉ hiện ở State=Error, thay chỗ Helper |
| Has Leading Icon | Bật tắt | tắt | bật icon đầu |
| Leading icon | Đổi component | icon/search · 14 | 4 bộ icon chọn sẵn (DS · Icons) |
| Has Trailing Icon | Bật tắt | tắt | bật icon cuối |
| Trailing icon | Đổi component | icon/chevron-down · 14 | 4 bộ icon chọn sẵn (DS · Icons) |

Chữ mặc định ở L0 là chữ trung tính (DEC-246): Label · Placeholder · Value · Helper text · Error text.

### Thành phần lồng

| Phần | Component · tầng | Cấu hình được phép | Đưa ra panel |
|---|---|---|---|
| Nhãn | `.field / Label` · L0 | Style=Web; State Default, Disabled theo State của ô | Label, Required |
| Khung ô | `.field / Input` · L0 | Size, State, Content theo ô | Placeholder, Value, Has Leading Icon, Leading icon, Has Trailing Icon, Trailing icon |
| Dòng dưới ô | `.field / Hint` · L0 | Type=Helper; State=Error → Type=Error | Helper, Error text (hiện bằng Has Helper) |
| Icon | `icon/*` · DS · Icons (trong `.field / Input`) | 4 bộ chọn sẵn; cỡ 14 | Leading icon, Trailing icon |
| Vòng focus | không có | Focus = viền 2px, không lồng `.focus / Ring` (DEC-207) | — |

Ba instance L0 đều đánh dấu đưa ra panel (`isExposedInstance`). Không lồng component L1 nào; L0 không chứa `Base / …`
(đúng luật lồng c).

### Được dùng trong

Kiểm trên Figma 20/10 (`getInstancesAsync`, cả file): chưa có component cha nào dùng. 26 instance hiện có đều là mẫu trong
khung tài liệu; không Slot, instance swap nào có preferred value là `Base / Text Field`; hàng L2 Text Field ghi "Chưa có".

| Component cha | Chỗ đặt | Cấu hình dùng |
|---|---|---|
| Chưa có component cha dùng | — | — |

### Token

Số đo (collection Platform, mode Web):

| Phần | Token | SM | MD | LG |
|---|---|---|---|---|
| Cao | `control/height/*` | 28 | 32 | 40 |
| Rộng mặc định | `field/width-default` | 320 | 320 | 320 |
| Lề mép ô | `field/edge-inset` | 8 | 8 | 8 |
| Lề chữ thêm | `field/text-inset` | 4 | 4 | 4 |
| Icon → chữ | `field/content-gap` + `field/text-inset` | 4 + 4 | 4 + 4 | 4 + 4 |
| Cỡ icon | `icon/size/sm` | 14 | 14 | 14 |
| Bo | `radius/field` | 8 | 8 | 8 |
| Viền nghỉ · đang gõ | `field/border-width` · `field/border-width-active` | 1 · 2 | 1 · 2 | 1 · 2 |
| Nhãn → ô, ô → gợi ý | `space/gap-xs` | 4 | 4 | 4 |
| Lề dòng gợi ý | `field/hint-inset` | 0 | 0 | 0 |
| Nhãn tối đa | `field/label-max-width` | 300 | 300 | 300 |
| Chữ nhãn | `type/label` | 14/20 Medium | 14/20 Medium | 14/20 Medium |
| Chữ giá trị, gợi ý | `type/body` | 14/20 | 14/20 | 14/20 |
| Chữ dưới ô | `type/caption` | 12/16 | 12/16 | 12/16 |
| Giữa hai ô | `form/field-gap` | 16 | 16 | 16 |
| Vùng chạm | `touch/min` | 24 ✓ | 24 ✓ | 24 ✓ |

Màu (collection Component, tiền tố `field/`): bảng "Màu theo phần" ở [Phần máy](#phần-máy--web-base--text-field).

Tên trong code: `<TextField size="sm|md|lg" label="Label" required placeholder="Placeholder" helper="Helper text"
error="Error text" leadingIcon={…} trailingIcon={…} disabled readOnly />`; biến CSS `--field-*`, `--control-height-*`,
`--radius-field`, `--icon-size-sm`, `--type-*`, `--form-field-gap`.

### Kiểm máy

Chạy `check-mat-hinh.js` trên khung 6467:84336 ngày 20/10 (ngưỡng 1,1:1, tương phản WCAG). Lớp ngoài của Text Field không có
nền nên script đo thêm lớp khung ô `Field` (L0 `.field / Input`), ghi "lớp con".

| Mức | Ô mẫu | Kết quả |
|---|---|---|
| Khung | 25 ô, 26 mẫu (khối Web) | luật A: 0 lỗi, ô nào cũng có nền trắng `color/bg/surface` và viền mảnh |
| ⚠ Nền chìm (lớp "Field") | 21 mẫu: Default, Hover, Focus, Error (cả lưới Biến thể, Kích thước, cảnh Nên, Không nên) | nền khung ô trắng trên ô trắng 1:1 (Hover #F9FAFC 1,04:1); hình giữ nhờ viền 5,43 · 15,13 · 6,57 — đúng thiết kế ô web |
| ✕ Giống Default (lớp "Field") | Hover · Filled | Hover #F9FAFC so với Default #FFFFFF = 1,04:1; đã biết, giữ theo DEC-210 (Hover · Empty cùng giá trị) |
| Cờ ngoài (lớp ngoài) | Hover · Filled | "GIỐNG DEFAULT" 1:1 là báo nhầm: lớp ngoài của Text Field không có nền; số đúng ở dòng trên |
| Sát ngưỡng | Disabled, Read Only (lớp "Field") | 1,10 (Disabled có viền 1,25); **Read Only 1,10 không viền**: chỉ còn nền (chính xác 1,0998), không gì khác giữ hình |

## Mobile

> Khối Mobile trên Figma đặt mode Platform = Mobile; mọi số dưới đây là giá trị mode Mobile.

### Tổng quan

- **Content:** Empty khi chưa nhập (chữ gợi ý `Placeholder`), Filled khi đã có giá trị (`Value`).
- **State:** Default · Focus (đang gõ) · Disabled · Error · Read Only. Hover có trong component, không dùng trên app.
- **Required:** dấu `*` đỏ đặt sau nhãn trong ô, cách 4 (DEC-207).
- **Icon:** Leading icon, Trailing icon như web, cỡ 16.
- **Helper:** dòng gợi ý dưới ô, tắt bằng `Has Helper`. Ở State=Error chữ lỗi thay chỗ dòng gợi ý và luôn hiện.
- **Cỡ app:** một cỡ 52 (`control/height/lg`), không có trục Size (DEC-173).
- **Rộng:** mặc định 361 = 393 − 2 × 16 (`field/width-default`); đặt vào màn thì kéo Fill theo khung.
- **Khác web:** nhãn caption nằm trong ô, trên giá trị; ô nền xám, bo 14, lề 16; icon cách mép 16, chữ cách icon 16, chữ
  đứng ở K3 64 khi ô ở lề màn (DEC-196); dòng gợi ý, chữ lỗi lùi 16 cho thẳng chữ trong ô (DEC-192); không Hover.
- **Giữa hai ô:** cách 12 (`form/field-gap`).
- **Chữ:** nhãn danh từ ngắn, viết hoa chữ đầu, không dấu hai chấm; chữ gợi ý là ví dụ thật hoặc "Nhập …"; chữ lỗi nói
  cái sai và cách sửa, không xin lỗi. Nhãn dài cắt "…" ở rộng tối đa 300, dấu `*` vẫn ngay sau nhãn.
- **Báo lỗi:** ngay tại ô, không khoá nút gửi form (DEC-177).

### Cấu tạo

Hình phóng 2× trên Figma: Content Filled · bật Required và Leading icon, tắt Helper (dòng gợi ý xem Trạng thái, Kích
thước); rộng rút còn 220 cho vừa ô hình.

| Phần | Token | Giá trị app |
|---|---|---|
| Nền | `field/bg/app`; Disabled `field/bg/disabled`; Read Only `field/bg/readonly` (Hover `field/bg/hover` có trong component, không dùng) | #F2F4F7 ở cả ba |
| Viền | `field/border-width`, `field/border/default`; Focus `field/border-width-active` + `field/border/active`; Error `field/border/error`; Disabled `field/border/disabled`; Read Only không viền | 1px; Focus, Error 2px |
| Nhãn trong ô | L0 `.field / Label` Style=App, lồng trong `.field / Input / App`; thuộc tính Label; `type/caption`; `field/fg/label-app` | 13/18 Regular; trên chữ giá trị; rộng tối đa 300 |
| Dấu bắt buộc | thuộc tính Required; `field/fg/error`; cách nhãn `space/gap-xs` | cách 4 |
| Khung ô | L0 `.field / Input / App`; cao `control/height/lg`; rộng `field/width-default`; bo `radius/field`; lề `field/edge-inset`, `field/text-inset` | cao 52; rộng 361; bo 14; lề 16, chữ thêm 0 |
| Chữ giá trị, gợi ý | Value `field/fg/value`, Placeholder `field/fg/placeholder`, Disabled `field/fg/disabled`; `type/body` | 15/22 |
| Icon | Leading icon, Trailing icon (đổi component, DS · Icons); `icon/size/sm`; `field/fg/icon`; icon → chữ `field/content-gap` | 16; cách mép 16; chữ cách icon 16 (DEC-196) |
| Dòng gợi ý, lỗi | L0 `.field / Hint`; Helper `field/fg/helper`, Error text `field/fg/error`; `type/caption`; cách ô `space/gap-xs`; lề `field/hint-inset` | 13/18; cách ô 4; lùi 16 cho thẳng chữ trong ô (DEC-192) |
| Dấu focus | viền 2px `field/border/active` khi đang gõ, hoặc khi điều hướng bằng bàn phím ngoài, công cụ trợ năng; không thêm vòng (DEC-207) | 2px |
| Vùng chạm | `touch/min` | 44: ô cao 52, không cần vùng chạm thêm |

### Biến thể

State × Content = 12 biến thể (6 × 2), không có trục Size. Required, icon, Helper là thuộc tính bật tắt. Lưới trên Figma:
Content × cấu hình thuộc tính như web, State Default.

### Trạng thái

| State | Trông thế nào |
|---|---|
| Default | nền xám `field/bg/app`, viền 1px `field/border/default` |
| Focus | đang gõ (chạm vào ô, hoặc bàn phím ngoài, công cụ trợ năng chuyển tới): viền 2px than chì `field/border/active`, không thêm vòng (DEC-207) |
| Disabled | nền `field/bg/disabled`, viền `field/border/disabled`, mọi chữ `field/fg/disabled`; không làm mờ (DEC-174) |
| Error | viền 2px `field/border/error`; chữ lỗi lùi 16 thay chỗ dòng gợi ý (DEC-177) |
| Read Only | nền `field/bg/readonly`, không viền; chọn và sao chép được chữ, không sửa |

App không dùng Hover (biến thể có trong component, không dùng).

### Kích thước

| Cỡ | Cao | Rộng mặc định | Lề | Vùng chạm | Dùng khi |
|---|---|---|---|---|---|
| một cỡ (LG) | 52 | 361 (Fill theo khung) | 16 | 52 ≥ 44, đủ | mọi ô nhập app (DEC-173) |

Bo 14, icon 16, dòng gợi ý lùi 16.

### Nên và không nên

1. **Nên:** nhãn ngắn nêu đúng thứ cần nhập, luôn hiện trong ô trên giá trị; chữ gợi ý là ví dụ thật hoặc "Nhập …".
   **Không nên:** bỏ nhãn, chỉ để chữ gợi ý trong ô — gõ vào là mất nhãn.
2. **Nên:** báo lỗi ngay tại ô: viền đỏ 2px + chữ lỗi nói cái sai và cách sửa. **Không nên:** khoá nút Lưu khi ô còn
   thiếu mà không báo ô nào (DEC-177).

### Trợ năng — chấm theo WCAG 2.2

| Tiêu chí | KQ | Số đo, ghi chú |
|---|---|---|
| 1.4.3 Tương phản chữ (AA, ≥ 4,5) | ✓ | giá trị trên nền ô 16,09 · nhãn trong ô, chữ gợi ý 4,92 · dấu `*` 5,97 · dòng gợi ý dưới ô (nền trắng) 5,43 · chữ lỗi 6,57 |
| 1.4.3 ngoại lệ — Disabled | ✓ | 2,34: được miễn (control không hoạt động) |
| 1.4.11 Tương phản ngoài chữ (AA, ≥ 3) | ✓ | viền nghỉ 4,92 với nền ô, 5,43 với nền trắng · viền đang gõ 13,73 · viền lỗi 5,97 · Read Only không viền (nền 1,10 trên trắng): nhận ra nhờ nhãn và chữ |
| 2.4.7 Focus thấy được (AA) | ✓ | viền 2px than chì 13,73 khi đang gõ, hoặc khi điều hướng bằng bàn phím ngoài, công cụ trợ năng |
| 2.5.8 Kích thước đích (AA, ≥ 24) | ✓ | 52 |
| 2.5.5 Kích thước đích (AAA, ≥ 44) | ✓ | 52 ≥ `touch/min` 44 |
| 1.3.1 Thông tin và quan hệ | ✓ | nhãn trợ năng của ô lấy từ nhãn (Label); trạng thái bắt buộc đọc được, dấu `*` chỉ để nhìn |
| 3.3.1 Nhận biết lỗi · 3.3.3 Gợi ý sửa | ✓ | chữ lỗi dưới ô nói cách sửa; trình đọc màn hình đọc chữ lỗi cùng ô |
| 1.4.1 Không chỉ dùng màu | ✓ | lỗi có viền dày hơn và chữ, không chỉ đổi màu |
| 4.1.2 Tên, vai trò | ✓ | nhãn trợ năng = nhãn; Read Only báo chỉ đọc |
| 2.1.1 Bàn phím | ✓ | khi có bàn phím ngoài: Tab tới ô theo thứ tự focus, gõ được |
| **Điểm app** | | **10/10 đạt** |

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| State | Biến thể | Default | Default · Focus · Disabled · Error · Read Only; Hover có trong component, không dùng trên app |
| Content | Biến thể | Empty | Empty (chữ gợi ý) · Filled (giá trị) |
| Label | Chữ | Label | nhãn trong ô (L0 `.field / Label`, Style=App) |
| Required | Bật tắt | tắt | dấu `*` đỏ sau nhãn |
| Placeholder | Chữ | Placeholder | chữ gợi ý khi Empty |
| Value | Chữ | Value | giá trị khi Filled |
| Helper | Chữ | Helper text | dòng gợi ý dưới ô |
| Has Helper | Bật tắt | bật | thuộc tính riêng của L1 |
| Error text | Chữ | Error text | chỉ hiện ở State=Error, thay chỗ Helper |
| Has Leading Icon | Bật tắt | tắt | bật icon đầu |
| Leading icon | Đổi component | icon/search · 16 | 4 bộ icon chọn sẵn (DS · Icons) |
| Has Trailing Icon | Bật tắt | tắt | bật icon cuối |
| Trailing icon | Đổi component | icon/chevron-down · 16 | 4 bộ icon chọn sẵn (DS · Icons) |

Như phần Web: chữ mặc định là chữ trung tính (DEC-246).

### Thành phần lồng

| Phần | Component · tầng | Cấu hình được phép | Đưa ra panel |
|---|---|---|---|
| Khung ô | `.field / Input / App` · L0 | State, Content theo ô | Placeholder, Value, Has Leading Icon, Leading icon, Has Trailing Icon, Trailing icon |
| Nhãn trong ô | `.field / Label` · L0 (Style=App, lồng trong `.field / Input / App`) | State Default, Disabled theo ô | Label, Required |
| Dòng dưới ô | `.field / Hint` · L0 | Type=Helper; State=Error → Type=Error; lề `field/hint-inset` 16 | Helper, Error text (hiện bằng Has Helper) |
| Icon | `icon/*` · DS · Icons (trong `.field / Input / App`) | 4 bộ chọn sẵn; cỡ 16 | Leading icon, Trailing icon |
| Vòng focus | không có | Focus = viền 2px, không lồng `.focus / Ring` (DEC-207) | — |

Không lồng component L1 nào; L0 chỉ chứa L0 (`.field / Label` trong `.field / Input / App`) và icon — đúng luật lồng c.

### Được dùng trong

Kiểm trên Figma 20/10 (`getInstancesAsync`, cả file): chưa có component cha nào dùng. 22 instance hiện có đều là mẫu trong
khung tài liệu; không Slot, instance swap nào có preferred value là `Base / Text Field / Mobile`.

| Component cha | Chỗ đặt | Cấu hình dùng |
|---|---|---|
| Chưa có component cha dùng | — | — |

### Token

Số đo (collection Platform, mode Mobile):

| Phần | Token | Mobile |
|---|---|---|
| Cao (một cỡ) | `control/height/lg` | 52 |
| Rộng mặc định | `field/width-default` | 361 (= 393 − 2 × 16) |
| Lề mép ô | `field/edge-inset` | 16 |
| Lề chữ thêm | `field/text-inset` | 0 |
| Icon → chữ | `field/content-gap` | 16 |
| Cỡ icon | `icon/size/sm` | 16 |
| Bo | `radius/field` | 14 |
| Viền nghỉ · đang gõ | `field/border-width` · `field/border-width-active` | 1 · 2 |
| Nhãn → `*`, ô → gợi ý | `space/gap-xs` | 4 |
| Lề dòng gợi ý | `field/hint-inset` | 16 |
| Nhãn tối đa | `field/label-max-width` | 300 |
| Chữ nhãn trong ô | `type/caption` | 13/18 |
| Chữ giá trị, gợi ý | `type/body` | 15/22 |
| Chữ dưới ô | `type/caption` | 13/18 |
| Giữa hai ô | `form/field-gap` | 12 |
| Vùng chạm | `touch/min` | 44: 52 ✓ đủ |

Màu (collection Component, tiền tố `field/`): bảng "Màu theo phần" ở [Phần máy · Mobile](#phần-máy--mobile-base--text-field--mobile); app
bỏ Hover, nền nghỉ `field/bg/app`.

Tên trong code: cùng prop với web (`label`, `required`, `placeholder`, `helper`, `error`, `leadingIcon`, `trailingIcon`,
`disabled`, `readOnly`), không có `size` (luôn cao 52); nhãn là nhãn trợ năng của ô. Tên component phía app chưa chốt.

### Kiểm máy

Chạy `check-mat-hinh.js` trên khung 6467:84336 ngày 20/10 (ngưỡng 1,1:1), đo thêm lớp khung ô `Field` (L0 `.field / Input / App`).

| Mức | Ô mẫu | Kết quả |
|---|---|---|
| Khung | 21 ô, 22 mẫu (khối Mobile) | luật A: 0 lỗi; ô nền trắng `color/bg/surface` + viền — nền thật của ô nhập app theo bảng nền ô |
| Lớp con (lớp "Field") | 22 mẫu | 0 cờ: nền khung ô #F2F4F7 trên ô trắng = 1,10 ở mọi trạng thái (sát ngưỡng, chính xác 1,0998) |
| Sát ngưỡng | Default, Focus, Error, Disabled, Read Only | giữ hình nhờ viền 5,43 · 15,13 · 6,57 · 1,25; **Read Only không viền** — chỉ còn 1,10 |
| Khe vòng focus (C) · Hover (D) | — | không áp: Text Field không có vòng focus; app không dùng Hover |

Base / Button Primary · Disabled 1,10 ở cảnh "Không nên" thuộc Button (xem tài liệu Button).

## Phần máy (chung Web và Mobile)

Tên token giống nhau ở hai nền tảng; số theo mode xem bảng Token của từng phần. Hai khối máy có tên: `web` cho `Base / Text Field`,
`mobile` cho `Base / Text Field / Mobile` (`python3 _scripts/ds-v2-component-doc.py <export.json> <md> --block web|mobile`).
Hai component ráp từ L0 nên bộ xuất không đọc được phần con: hai khối giữ bản máy sinh từ lần xuất đọc được màu và số đo; thuộc
tính Label, Placeholder, Value, Helper, Error text mở ra từ instance L0 (`isExposedInstance`).

**Web — `Base / Text Field`**

<!-- auto:begin web -->
<!-- Máy sinh từ Figma `Base / Text Field` (6423:21911) ngày 2026-10-20 bằng _scripts/ds-v2-component-doc.py. Không sửa tay: sửa trên Figma rồi xuất lại. -->

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| Label | Chữ | Label | — |
| Required | Bật tắt | tắt | — |
| Placeholder | Chữ | Placeholder | — |
| Value | Chữ | Value | — |
| Helper | Chữ | Helper text | — |
| Has Helper | Bật tắt | bật | — |
| Error text | Chữ | Error text | — |
| Has Leading Icon | Bật tắt | tắt | — |
| Leading icon | Đổi component | icon/search · Size=14 | — |
| Has Trailing Icon | Bật tắt | tắt | — |
| Trailing icon | Đổi component | icon/chevron-down · Size=14 | — |
| Size | Biến thể | MD | SM · MD · LG |
| State | Biến thể | Default | Default · Hover · Focus · Disabled · Error · Read Only |
| Content | Biến thể | Empty | Empty · Filled |

36 biến thể · trục Size × State × Content.

### Màu theo phần (token)

| State | Content | Nền | Viền | Chữ |
|---|---|---|---|---|
| Default | Empty | `field/bg/web` | `field/border/default` | `field/fg/placeholder` |
| Default | Filled | `field/bg/web` | `field/border/default` | `field/fg/value` |
| Hover | Empty | `field/bg/hover` | `field/border/default` | `field/fg/placeholder` |
| Hover | Filled | `field/bg/hover` | `field/border/default` | `field/fg/value` |
| Focus | Empty | `field/bg/web` | `field/border/active` | `field/fg/placeholder` |
| Focus | Filled | `field/bg/web` | `field/border/active` | `field/fg/value` |
| Disabled | Empty | `field/bg/disabled` | `field/border/disabled` | `field/fg/disabled` |
| Disabled | Filled | `field/bg/disabled` | `field/border/disabled` | `field/fg/disabled` |
| Error | Empty | `field/bg/web` | `field/border/error` | `field/fg/placeholder` |
| Error | Filled | `field/bg/web` | `field/border/error` | `field/fg/value` |
| Read Only | Empty | `field/bg/readonly` | — | `field/fg/placeholder` |
| Read Only | Filled | `field/bg/readonly` | — | `field/fg/value` |

### Số đo theo phần (token)

| Size | Cao | Rộng | Lề trái | Lề phải | Khoảng giữa | Bo |
|---|---|---|---|---|---|---|
| SM | `control/height/sm` | `field/width-default` | `field/edge-inset` | `field/edge-inset` | `space/gap-xs` | `radius/field` |
| MD | `control/height/md` | `field/width-default` | `field/edge-inset` | `field/edge-inset` | `space/gap-xs` | `radius/field` |
| LG | `control/height/lg` | `field/width-default` | `field/edge-inset` | `field/edge-inset` | `space/gap-xs` | `radius/field` |

### Kiểu chữ

| Lớp chữ | Text style |
|---|---|
| Label | `type/label` |
| Placeholder | `type/body` |
| Value | `type/body` |
| Helper | `type/caption` |
| Error text | `type/caption` |

<!-- auto:end web -->

**Mobile — `Base / Text Field / Mobile`**

<!-- auto:begin mobile -->
<!-- Máy sinh từ Figma `Base / Text Field / Mobile` (6423:81962) ngày 2026-10-20 bằng _scripts/ds-v2-component-doc.py. Không sửa tay: sửa trên Figma rồi xuất lại. -->

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| Label | Chữ | Label | — |
| Required | Bật tắt | tắt | — |
| Placeholder | Chữ | Placeholder | — |
| Value | Chữ | Value | — |
| Helper | Chữ | Helper text | — |
| Has Helper | Bật tắt | bật | — |
| Error text | Chữ | Error text | — |
| Has Leading Icon | Bật tắt | tắt | — |
| Leading icon | Đổi component | icon/search · Size=16 | — |
| Has Trailing Icon | Bật tắt | tắt | — |
| Trailing icon | Đổi component | icon/chevron-down · Size=16 | — |
| State | Biến thể | Default | Default · Hover · Focus · Disabled · Error · Read Only |
| Content | Biến thể | Empty | Empty · Filled |

12 biến thể · trục State × Content.

### Màu theo phần (token)

| State | Content | Nền | Viền | Chữ |
|---|---|---|---|---|
| Default | Empty | `field/bg/app` | `field/border/default` | `field/fg/placeholder` |
| Default | Filled | `field/bg/app` | `field/border/default` | `field/fg/value` |
| Hover | Empty | `field/bg/hover` | `field/border/default` | `field/fg/placeholder` |
| Hover | Filled | `field/bg/hover` | `field/border/default` | `field/fg/value` |
| Focus | Empty | `field/bg/app` | `field/border/active` | `field/fg/placeholder` |
| Focus | Filled | `field/bg/app` | `field/border/active` | `field/fg/value` |
| Disabled | Empty | `field/bg/disabled` | `field/border/disabled` | `field/fg/disabled` |
| Disabled | Filled | `field/bg/disabled` | `field/border/disabled` | `field/fg/disabled` |
| Error | Empty | `field/bg/app` | `field/border/error` | `field/fg/placeholder` |
| Error | Filled | `field/bg/app` | `field/border/error` | `field/fg/value` |
| Read Only | Empty | `field/bg/readonly` | — | `field/fg/placeholder` |
| Read Only | Filled | `field/bg/readonly` | — | `field/fg/value` |

### Số đo theo phần (token)

| Cao | Rộng | Lề trái | Lề phải | Khoảng giữa | Bo |
|---|---|---|---|---|---|
| `control/height/lg` | `field/width-default` | `field/edge-inset` | `field/edge-inset` | `space/gap-xs` | `radius/field` |

### Kiểu chữ

| Lớp chữ | Text style |
|---|---|
| Label | `type/caption` |
| Placeholder | `type/body` |
| Value | `type/body` |
| Helper | `type/caption` |
| Error text | `type/caption` |

<!-- auto:end mobile -->
