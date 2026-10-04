---
name: figma-component
description: Tạo hoặc cập nhật MỘT component bất kỳ của dự án trên Figma (vd Notification Center, Bộ lọc nâng cao, Tuỳ chỉnh cột, thẻ KPI, dòng lịch sử…) — ghép từ instance thật của thư viện đang có, gắn token của dự án, có biến thể + thuộc tính dùng lại được, đủ trạng thái, Desktop/Mobile, kiểm chữ dài — theo spec trong design/design.md. Dùng khi ai đó nói "tạo component", "dựng component <tên>", "biến mẫu ghép này thành component", "thêm biến thể/trạng thái cho component", "làm lại component cho file mới". Không dùng để dựng cả design system (dùng /figma-design-system) hay vẽ màn (dùng /figma-screen).
allowed-tools: Read, Glob, Grep, Edit, AskUserQuestion, mcp__claude_ai_Figma__use_figma, mcp__claude_ai_Figma__get_figma_skill, mcp__claude_ai_Figma__get_metadata, mcp__claude_ai_Figma__get_screenshot, mcp__claude_ai_Figma__get_libraries, mcp__claude_ai_Figma__search_design_system, mcp__reqwise-figma__figma_status
user-invocable: true
argument-hint: "<tên component> [link file Figma] [desktop|mobile|cả hai] [@spec/srs]"
---

# /figma-component — một component của dự án, dùng lại được, đúng design system

## Mục tiêu

Một **họ component set** trong file Figma đích mà designer/dev lấy instance là dùng được:

* Ghép từ **instance thật** của thư viện (Button, Badge, Tabs, Popover…), không vẽ lại control.
* Mọi màu / khoảng cách / bo góc / chữ **gắn biến và style** của dự án.
* **API rõ**: biến thể (VARIANT) cho khác biệt về hình, thuộc tính TEXT / BOOLEAN / INSTANCE_SWAP cho
  nội dung, instance con được expose khi người dùng cần chỉnh.
* **Đủ trạng thái** theo § States của `design.md` (có dữ liệu / rỗng / đang tải / lỗi…), đủ nền tảng
  đã chốt (Desktop / Mobile), **kiểm chữ dài**.
* Một khung trình bày: master components + mọi trạng thái bằng instance + phần *Chữ dài · kiểm tra*.

__Việc chính là thiết kế API và cấu trúc, không phải thao tác vẽ.__ Tách component con nào, trục biến
thể nào, cái gì là thuộc tính — quyết sai thì người dùng phải detach, và mọi instance đã dùng bị vỡ.

## Luật quyết định thành bại

* **`design/design.md` là nguồn duy nhất.** Đọc lại từ file mỗi lần chạy, **theo mục** (Bước 1.2).
  Skill này không chứa giá trị nào của dự án (màu, câu mẫu, bề rộng, tên trạng thái…).
* **Không có spec thì không dựng.** Component phải có mục spec trong `design.md` (thường ở
  § Components - <dự án>). Chưa có → Bước 2 phỏng vấn để viết spec, trình user duyệt, ghi vào
  `design.md` (approval gate), rồi mới dựng.
* **Không tạo component khi thư viện đã có cái tương đương** (Don't của `design.md`). Kiểm thư viện
  Figma + `design/components.md` trước; nghi ngờ thì kiểm code thư viện (vd repo Astryx).
* Tôn trọng quyết định "mẫu ghép" hay "component thật" đã ghi trong `design.md`. Muốn đổi → hỏi user
  và sửa quy định trong `design.md` cùng lượt.

## Bước 1 — đọc trước, hỏi sau

1. Nạp luật Plugin API: `get_figma_skill("skill://figma/figma-use/SKILL.md")` và
   `skill://figma/figma-generate-library/SKILL.md` (bắt buộc trước mọi `use_figma`).
2. Đọc `design/design.md` theo mục (cách đọc: `.claude/rules/design-system.md` § Nguồn duy nhất):
   * `Grep -n "^## \|^### "` lấy mục lục; Read từng mục bằng offset/limit.
   * **Luôn đọc:** Typography › Principles, Tên trong Figma, Do's and Don'ts, Iteration Guide,
     Known Gaps.
   * **Của skill này:** trong § Components - <dự án>: mục *Quy ước chung của component dự án* (tiền lệ
     đã chốt — spec mới phải nhất quán, lệch thì nêu lý do) + spec đang dựng; spec khác chỉ đọc khi
     quy ước dẫn tới hoặc cần làm mẫu khuôn (§ Notification Center); phần
     đầu § Components tới hết quy ước "Web và Mobile"; § States; § Content & Formatting;
     § Accessibility; § Responsive Behavior; § Phân trang nếu component có danh sách; § Layout khi
     đề xuất bố cục ví dụ *Trong ngữ cảnh*.
   * Không đọc Colors, Typography Hierarchy, Elevation, Shapes: giá trị gắn qua biến/style Figma theo
     tên. Đoạn đã đọc có "xem §…" → đọc luôn đoạn đó.
3. `design/components.md`: đọc mục của **từng component thành phần** định dùng (Usage, Nên/Không nên).
4. Nguồn nghiệp vụ (Glob): `srs/*`, file user tag `@`, tài liệu quy tắc chung của dự án được
   `design.md` dẫn tới. Có nguồn thì dẫn xuất nội dung mẫu từ đó.

## Bước 2 — chốt spec (chỉ khi spec chưa đủ)

Phỏng vấn bằng `AskUserQuestion`, gộp một lượt, mỗi câu kèm đề xuất:

* **Mục đích + chỗ dùng:** component giải quyết gì, xuất hiện ở màn/vùng nào.
* **Giải phẫu:** các phần (header, dòng, chân…), phần nào bắt buộc/tùy chọn, component thư viện nào
  đảm nhận từng phần.
* **Biến thể:** trục trạng thái nghiệp vụ, trạng thái tương tác (Rest/Hover/Pressed/Selected/Disabled),
  nền tảng (Desktop/Mobile), kích thước.
* **Trạng thái dữ liệu:** có dữ liệu / rỗng / đang tải / lỗi (bắt buộc nếu component chứa dữ liệu).
* **Nội dung:** mẫu câu, thứ tự thông tin, cái gì cần nổi khi lướt (mã, số tiền…).
* **Chữ dài:** mỗi dòng chữ tối đa mấy dòng, cái gì không bao giờ cắt, cái gì co.
* **Hành vi:** click, đếm, gộp, tải thêm, điều hướng.
* **Mở từ đâu:** nút nào, nằm ở màn/vùng nào, vị trí trong header — để dựng điểm kích hoạt và ví dụ ngữ cảnh.

Viết spec theo khuôn của các mục có sẵn trong `design.md`, trình user, duyệt xong mới ghi.

## Bước 3 — thiết kế API (trình trong kế hoạch)

Chia component theo **nguyên tử → phân tử → khối chứa** (dựng từ dưới lên):

| Tầng | Ví dụ (Notification Center) | Quy tắc |
|---|---|---|
| Phần tử lặp | `… / Item` (một dòng) | Trục = trạng thái của một phần tử; nội dung là thuộc tính TEXT |
| Điểm kích hoạt | `… / Bell`, `… / Trigger` | **Bắt buộc** khi khối được mở từ một nút ở chỗ khác trên màn (header, dòng bảng), kể cả khi nút chỉ là Button thư viện: cần trạng thái Rest / Hover (tooltip nếu Icon Only) / Open, cỡ cảm ứng cho Mobile |
| Nội dung khối | `… / Body` | Trục = nền tảng × trạng thái dữ liệu; chứa instance phần tử lặp |
| Vỏ | `… / Panel` | Trục = nền tảng; bọc Body bằng container của thư viện (Popover, Dialog, màn mobile) |

* Tên: `<Tên component> / <Phần>` để gom một nhóm trong panel Assets. Phần nội bộ không cho dùng trực
  tiếp: tiền tố `.` (`.Content`).
* **Biến thể** chỉ cho khác biệt về hình/bố cục. Nội dung chữ → TEXT; bật/tắt một phần → BOOLEAN;
  đổi icon/khối → INSTANCE_SWAP. Mỗi set **≤ 30 tổ hợp**; nhiều hơn thì tách component con.
* Instance con mà người dùng cần chỉnh (Timestamp, Body trong Panel…) → `isExposedInstance = true`.
* Nền tảng theo quy ước Web | Mobile của `design.md`: component tự đổi cách hiển thị (vd popover →
  bottom sheet → màn riêng) thì làm trục `Platform`, không dựng hai họ riêng.

## Bước 4 — dò file Figma (chỉ đọc)

`use_figma` đọc, mỗi trang một lệnh (gọi song song được khi chỉ đọc; mỗi lệnh đổi trang **một lần**):

* Trang: `figma.root.children`.
* Component thành phần theo tên: `id`, `key`, `componentPropertyDefinitions` (khoá có hậu tố `#id`),
  tên biến thể thật (`children.map(c => c.name)`).
* Icon cần dùng (trang Icons, tên `icon/...`).
* Biến và text/effect style: tìm **theo tên** bằng `getLocalVariablesAsync()`,
  `getLocalTextStylesAsync()`, `getLocalEffectStylesAsync()`; không đoán id.
* Component cùng tên đã có → **cập nhật** (Bước 8), không dựng bản thứ hai.
* Không có thư viện cục bộ → `get_libraries` → `search_design_system`. Vẫn không có → **dừng**,
  chỉ user `design/setup-figma.md`.
* Thử nhanh những chỗ chưa chắc (vd đặt node vào slot được không) bằng một lệnh thử có **tự dọn**.

## Bước 5 — hỏi phần còn lại, trình kế hoạch, chờ `Y`

Hỏi một lượt (`AskUserQuestion`): **thiết bị — luôn hỏi**; nơi đặt (trang, vị trí; không đè khung có
sẵn); các điểm spec còn "chờ xác nhận" — dựng theo bản hiện tại hay chờ; **bố cục của ví dụ *Trong
ngữ cảnh*** — 3 phương án theo Luật 1 của `.claude/rules/design-system.md`: A theo mẫu gần nhất trong
§ Layout, B và C độc lập (khác nhau thật về cách tổ chức vùng chứa component), mỗi cái kèm lý do.
Ví dụ ngữ cảnh là nơi dev nhìn để biết component đặt vào màn thế nào, nên khung của nó cũng là một
quyết định bố cục, không mặc định lấy mẫu.

```
Em sẽ dựng "<Tên>" trong <file>, trang <trang>, khung "<Tên> · <dự án>":
<Tên> / Item    Status(3) × State(2) = 6   · TEXT: Title, Meta · BOOLEAN: Has Code
<Tên> / Body    Platform(2) × State(6) = 12 · dùng Tabs, EmptyState, Skeleton
<Tên> / Panel   Platform(2)                  · Desktop: Popover · Mobile: màn riêng 390×844
Khung trạng thái + Chữ dài (<w desktop> và 320px)
Trong ngữ cảnh: A <mẫu + chỉnh gì> · B <…> · C <…> → user chọn
Thiết bị: <…> · Chưa có chuẩn trong design.md: <…>
Apply? (Y / sửa)
```

## Bước 6 — dựng (tuần tự, không ghi song song)

Từ dưới lên, **một lệnh `use_figma` cho mỗi component set**; mỗi lệnh trả về id đã tạo, lệnh sau dùng
id dạng chuỗi.

1. **Khung chứa**: auto-layout dọc, nền surface. Cấp chữ: tên khung `Display 2` → tiêu đề section
   (`Master Components`, `Trạng thái & ví dụ`) `Display 3` → tên từng set / tên từng cảnh `Heading 1`
   → mô tả `Text/Body` secondary.
   * Trong `Master Components`, **mỗi set một khối** `Doc · <tên set>`: tên set → 1–2 câu mục đích
     (dùng ở đâu, khi nào) → bảng **Trường hợp** (viền `Border/Default`, bo `Radius/Container`): mỗi trục
     biến thể một cột, mỗi giá trị một dòng "giá trị — khi nào dùng / khác gì" → các biến thể.
   * Mỗi cảnh trong `Trạng thái & ví dụ`: tên cảnh + **một dòng mô tả** (người dùng đang làm gì, cảnh
     chứng minh điều gì). Không để cảnh nào chỉ có tên.
2. **Mỗi component set**:
   * Tạo từng biến thể bằng `createComponent()` + auto-layout; gắn biến cho fill/stroke/padding/gap/
     radius (`setBoundVariableForPaint`, `setBoundVariable`), text style bằng `setTextStyleIdAsync`.
   * Instance thành phần: `createInstance()` từ đúng biến thể → `setProperties` **tường minh mọi trục
     ảnh hưởng hiển thị** (thư viện mặc định thường không phải cỡ MD — xem § Tên trong Figma).
   * `combineAsVariants` → thêm thuộc tính ở **component set** → gán `componentPropertyReferences` cho
     node trong **từng** biến thể → xếp biến thể bằng auto-layout (wrap) → viết `description`
     (mục đích, cách dùng, cách đổi trạng thái).
3. **Khung trạng thái**: instance của mọi biến thể quan trọng, có chú thích; ví dụ **Trong ngữ cảnh** —
   component đặt trong màn/vùng chứa nó (vd header màn chi tiết + panel mở neo dưới nút; mobile + scrim),
   dựng theo phương án bố cục user đã chọn ở Bước 5 (vẫn bằng token + component thật); phần *Chữ dài · kiểm tra*
   với nội dung cực trị ở bề rộng desktop và 320px (chữ rất dài, mã dài, thiếu dữ liệu tùy chọn).

### Bẫy đã gặp — làm đúng ngay từ đầu

| Bẫy | Cách làm đúng |
|---|---|
| Tên biến thể thư viện có khoảng trắng (`size = md, state = selected`) | Đọc tên thật trước; so khớp bằng `includes` |
| Khoá thuộc tính có hậu tố (`Label#8:11`) | `Object.keys(inst.componentProperties).find(k => k.startsWith('Label'))` |
| `clone()` một biến thể **mất** `componentPropertyReferences` | Gán lại references cho biến thể clone |
| Container thư viện cố định bề rộng (vd Popover Surface 260px), `resize()` không ăn | `layoutSizingHorizontal = 'FILL'` cho lớp trong, slot và nội dung |
| Đặt nội dung vào slot của instance | `slot.appendChild(node)`; ẩn con mặc định của slot |
| Container có INSTANCE_SWAP (vd BottomSheet `Content`) | Swap bằng `setProperties({ [key]: componentId })`, không phải slot |
| `maxLines` + `textAutoResize='HEIGHT'` vẫn tính cao nhiều dòng | Chữ 1 dòng: `textAutoResize='NONE'`, cao = line-height, `FILL`, `textTruncation='ENDING'` |
| Phần tử dài đẩy phần kế bên ra ngoài | Hàng đó `layoutWrap = 'WRAP'` |
| Hàng rỗng vẫn chiếm chỗ | Gắn `visible` của **cả hàng** vào BOOLEAN |
| Chữ trong EmptyState/Banner không xuống dòng | `FILL` + `textAutoResize='HEIGHT'` |
| Badge/nhãn tuyệt đối bị cắt | Component cha `clipsContent = false` |
| Thuộc tính TEXT / INSTANCE_SWAP dùng **một giá trị mặc định cho mọi biến thể** (vd mọi Tone cùng icon `+`) | Nội dung khác nhau theo biến thể (icon theo Tone) → để sẵn trong từng biến thể + `isExposedInstance`, không dùng INSTANCE_SWAP |
| Đổi icon bằng `swapComponent` làm mất màu nét đã override | Sau khi swap, gán lại `strokes` (biến màu) cho vector của icon |
| Đổi biến thể của instance lồng (vd BottomSheet Capped → Tall) không đổi chiều cao; `resize()` lớp lồng không ăn | Cần kích thước khác thì đặt trực tiếp instance của biến thể đó; ghi lưu ý vào `description` |
| Không tìm thấy lớp đang ẩn trong instance (vd `units`, `statusText`), hoặc lỗi "node does not exist" khi đổi `visible` | Đầu mỗi script: `figma.skipInvisibleInstanceChildren = false` |
| Ẩn nhãn/mô tả của control thư viện (Selector, DateRangeInput…) | Ẩn cả khung `Label + Description`, không ẩn từng node con |
| Sửa main component nhưng instance có nội dung trong **slot** không đổi theo | Nội dung slot là bản riêng của từng instance: sửa luôn các instance đã đặt (khung trạng thái, chữ dài) |
| Nhãn của item thư viện (CheckboxListItem) không xuống dòng | Chữ `Label` trong `Label Wrapper`: `layoutSizingHorizontal='FILL'` + `textAutoResize='HEIGHT'`, item `FILL` |
| Khung ôm nội dung có con `layoutGrow = 1` → con bị ép về 0 | Trong component để con `HUG`; chỉ đặt grow trên instance đặt trong vỏ cao cố định (Drawer) để ghim chân |
| Gán lại `fills` cho chữ của control thư viện (đã gắn biến màu) làm chữ biến mất | Chỉ đổi `characters`; giữ nguyên fill gốc. Lỡ hỏng thì thay bằng instance mới |
| Sửa lớp chữ lồng trong main component (vd bật truncation) làm **mất chữ đã override** trên mọi instance | Sửa main trước khi đặt nội dung; nếu sửa sau thì gán lại nội dung cho các instance đã đặt |
| Phần nổi (menu, popover) đặt bên trong một hàng bị hàng vẽ sau đè lên | Trong khung cảnh, đặt phần nổi thành instance riêng ở lớp trên cùng của khung |
| Chip có "+n" bị cắt mất khi nhãn dài | Đưa "+n" vào `End Content` của Token; nhãn 1 dòng + `maxWidth` cho Token |
| Nền nhấn nhẹ trùng nền ở Dark | Kiểm cả mode Dark của biến; đặt khối trên bề mặt có tông khác |
| Lệnh ghi lỗi giữa chừng | Cả lệnh được hoàn tác — đọc lại canvas trước khi chạy lại |
| File vừa bị người khác sửa (id đổi, node trùng) | Đọc lại cấu trúc; không xoá thứ mình không tạo, hỏi user |
| Sửa chữ | `loadFontAsync` mọi font của node (`getStyledTextSegments(['fontName'])`) trước |
| `resize()` sau khi đặt `primaryAxisSizingMode='AUTO'` → component kẹt cao cố định, nội dung con (Banner) tràn | Gọi `resize()` trước, đặt `…SizingMode='AUTO'` sau; hoặc đặt lại sau cùng |
| `isExposedInstance = true` báo "must be contained within a component" | Đặt sau `combineAsVariants` (hoặc sau khi instance đã nằm trong component) |
| `setProperties` trên instance lồng khi đang lặp `findAll` → "node does not exist" | Đổi biến thể xong thì dừng vòng lặp; tìm lại node sau mỗi lần đổi |
| Nhãn `Collapsible` thư viện (`Text/Large`) lấn át tiêu đề khối | Hạ text style trên instance (`Text/Label`, màu secondary), không sửa main thư viện |
| Đọc `description` rồi `replace` và gán lại → dấu `"` thành `&amp;quot;` (giá trị đọc ra đã escape HTML) | Viết lại toàn văn `description`, không đọc–sửa–ghi |
| Hai đường kẻ chồng nhau (Entry có viền dưới + khối cha có viền dưới) | Bỏ viền của phần tử con trong khối có viền riêng |

## Bước 7 — tự kiểm trước khi trình

1. Bằng số liệu trả về: số biến thể, tên thuộc tính, kích thước từng biến thể.
2. **Một ảnh chụp mỗi component set**, một ảnh khung trạng thái, một ảnh *Chữ dài*. Tìm: chữ cắt
   ngoài ý muốn, khoảng trống thừa, phần tử tràn, nội dung mặc định còn sót ("Button", "Content",
   giờ kiểu Mỹ…).
3. Đối chiếu từng quy tắc chữ dài và hành vi của spec với ảnh.
4. Do's and Don'ts của `design.md`: (a) ≤ 1 nút Primary mỗi nhóm; (b) trạng thái không chỉ dựa vào
   màu; (c) đủ rỗng / đang tải / lỗi; (e) không vi phạm "Không nên" của component thành phần.
5. Không còn mã hex; tương phản chữ phụ trên nền nhấn — ghi lại nếu dưới AA.
6. Sửa lỗi → chụp lại **chỉ phần đã sửa**.

## Bước 8 — cập nhật component đã có

Sửa **tại chỗ** để giữ liên kết instance:

* Đổi tên biến thể thay vì xoá-tạo (override đi theo tên mới).
* Thêm biến thể = `clone()` biến thể gần nhất rồi sửa (gán lại references).
* Xoá thuộc tính: xoá/gỡ node gắn với nó rồi `deleteComponentProperty(key)`.
* Đổi nội dung mẫu: `setProperties` trên instance; đổi cấu trúc: sửa main component.
* Hỏi user có chỉnh tay gì không trước khi sửa; chỉnh tay là dữ liệu, không ghi đè.

## Bước 9 — báo cáo và cập nhật tài liệu

```
Đã dựng "<Tên>" trong <file>, trang <trang> (node <id khung>):
<set> <n biến thể> · <set> <n> · …
Máy đã kiểm: biến thể/thuộc tính · ảnh chụp <n> · chữ dài ở <w> và 320px
Máy KHÔNG kiểm: nội dung nghiệp vụ đúng chưa [Cao] · thiếu trạng thái nghiệp vụ nào [Cao] · thẩm mỹ [Thấp]
Chưa có chuẩn trong design.md: <…>
```

Rồi cập nhật spec của component trong `design.md` (bảng: tên set, key, biến thể/thuộc tính, dựng
từ gì; các quyết định mới; Known Gaps theo Iteration Guide — dòng `KG-nn` trong `design.md` + hàng chi
tiết trong `design/design-backlog.md`) — qua approval gate. Quyết định mới lặp lại ở ≥ 2 spec → đề xuất
đưa lên *Quy ước chung của component dự án*.

## Constraints

### Luật cứng

* Không dựng khi chưa có spec đã duyệt trong `design.md`.
* Không tạo component trùng cái thư viện đã có; không vẽ lại control; không sửa main component
  của thư viện.
* Không mã màu/cỡ/khoảng cách cứng khi đã có token.
* Không bịa nội dung nghiệp vụ; không bịa giá trị ở Known Gaps — hỏi, hoặc ghi "chưa có chuẩn trong
  design.md".
* Không xoá node mình không tạo; không dựng bản thứ hai khi đã có.
* Thiết bị luôn hỏi user. Không gọi `use_figma` ghi song song.

### Tuân thủ rule workspace

Skill này là "skill vẽ" theo nghĩa của `.claude/rules/design-system.md`: đọc `design/design.md` theo
mục (mục lục + mục luôn đọc + mục của `/figma-component` trong bảng của rule), tuân theo *Luật khi sinh màn*, dùng Do's and Don'ts làm tiêu chí tự kiểm, đụng
Known Gaps thì hỏi hoặc ghi "chưa có chuẩn trong design.md".

## References

- Rule workspace `.claude/rules/design-system.md`.
- `design/design.md`: spec component, token, § Tên trong Figma, States, Content & Formatting,
  Accessibility, Responsive, Known Gaps, Quy ước chung của component dự án. Ví dụ spec đầy đủ:
  § Notification Center.
- `design/design-backlog.md`: chi tiết Known Gaps (người phụ trách, ngày hẹn) — không cần đọc khi dựng.
- `design/components.md`: Usage / Nên / Không nên của component thành phần.
- `design/setup-figma.md`: khi file đích chưa có thư viện.
- `skill://figma/figma-use/SKILL.md`, `skill://figma/figma-generate-library/SKILL.md`: luật Plugin API
  và quy trình dựng component.
- `/figma-design-system` (dựng cả bộ DS), `/figma-screen` (vẽ màn dùng component này).
