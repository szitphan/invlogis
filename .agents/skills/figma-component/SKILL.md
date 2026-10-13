---
name: figma-component
description: Tạo hoặc cập nhật MỘT component bất kỳ của dự án trên Figma (vd Notification Center, Bộ lọc nâng cao, Tuỳ chỉnh cột, thẻ KPI, dòng lịch sử…) — ghép từ instance thật của thư viện đang có, gắn token của dự án, có biến thể + thuộc tính dùng lại được, đủ trạng thái, Desktop/Mobile, kiểm chữ dài — theo spec trong design/design.md. Dùng khi ai đó nói "tạo component", "dựng component <tên>", "biến mẫu ghép này thành component", "thêm biến thể/trạng thái cho component", "làm lại component cho file mới". Không dùng để dựng cả design system (dùng /figma-design-system) hay vẽ màn (dùng /figma-screen).
allowed-tools: Read, Glob, Grep, Edit, Write, Bash, Skill, AskUserQuestion, mcp__reqwise-figma__figma_status, mcp__reqwise-figma__figma_docs, mcp__reqwise-figma__figma_read, mcp__reqwise-figma__figma_rules, mcp__reqwise-figma__figma_write, mcp__claude_ai_Figma__use_figma, mcp__claude_ai_Figma__get_figma_skill, mcp__claude_ai_Figma__get_libraries, mcp__claude_ai_Figma__search_design_system, mcp__claude_ai_Figma__get_metadata, mcp__claude_ai_Figma__download_assets
user-invocable: true
argument-hint: "<tên component> [link file Figma] [desktop|mobile|cả hai] [@spec/srs]"
---

# /figma-component — một component của dự án, dùng lại được, đúng design system

Đọc cổng kết nối trong `../reqwise-diagram-rules.md` trước (§ 5, *Before anything else: is the
write path open?*). Tóm tắt: plugin đã kết nối, chỉ một cửa sổ, gọi `figma_status` trước mọi thứ,
và dry run **không** phải phép thử kết nối. Phần còn lại của file đó nói về sơ đồ; component không
phải sơ đồ, nên các bước dưới đây thay cho luật vẽ sơ đồ.

**Hai đường ghi:**

* **Chính — `figma_write` (reqwise).** Proxy, không phải Plugin API gốc (không `createFrame`,
  `appendChild`, `loadFontAsync`). Cú pháp: `figma_docs(section="api", level="cheat")` và
  `figma_docs(section="recipes")`, đọc một lần trước lần ghi đầu tiên của phiên; lỗi thì đọc
  `hint` rồi `figma_docs(section="api")` bản đầy đủ.
* **Dự phòng — `use_figma` (Figma chính thức)**, chỉ cho việc proxy không có: đặt nội dung vào
  **slot** của instance (Popover Surface, Drawer…). Trước khi dùng lần đầu trong phiên: nạp
  `get_figma_skill("skill://figma/figma-use/SKILL.md")`. Mỗi lần dùng ghi vào báo cáo Bước 9.
  Không dùng `use_figma` cho việc `figma_write` làm được.
  * `use_figma` cần **fileKey**; reqwise trả `fileKey: null` → hỏi user link file một lần trong phiên.
  * Chia việc: **dựng nội dung bằng `figma_write`** (token, text style) → `use_figma` **chỉ
    `appendChild` vào slot** → sửa tiếp bằng `figma_write` (sửa được node trong slot qua id `I…;…`).
    Không tạo chữ/khung mới bằng `use_figma` — không gắn token.

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

1. `figma_status` → plugin, file, trang đang mở. Rồi `figma_docs` bản cheat + recipes (xem đầu file).
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
* Instance con mà người dùng cần chỉnh (Timestamp, Body trong Panel…) → expose
  (`exposeNestedInstance`).
* Nền tảng theo quy ước Web | Mobile của `design.md`: component tự đổi cách hiển thị (vd popover →
  bottom sheet → màn riêng) thì làm trục `Platform`, không dựng hai họ riêng.

## Bước 4 — dò file Figma (chỉ đọc)

Chỉ đọc, gọi song song được:

* Trang đích: `figma_read get_page_model` — khung có sẵn, chỗ trống để đặt.
* Token và style: `figma_rules` (biến, text/effect style đang có trong file). File chỉ tiêu thụ
  thư viện → `figma.getVariables({ includeLibrary: true })`. Gắn theo **tên**, không đoán id.
* Component thành phần: `figma_read get_components` / `get_component` → `id`, `key`, thuộc tính,
  tên biến thể thật. Không có trong file → key trong `design/figma-library-keys.json` (dùng
  `instantiate({ key, variant })` ở Bước 6). Không có key → `get_libraries` → `search_design_system`.
  Vẫn không có → **dừng**, chỉ user `design/setup-figma.md`.
* Icon: `figma.searchIcons` / trang Icons (tên `icon/...`).
* Component cùng tên đã có: `figma.findComponent("<Tên>")` → **cập nhật** (Bước 8), không dựng
  bản thứ hai.
* Component cần **slot** (nội dung đặt vào Popover/Drawer…) → đánh dấu phần đó đi đường dự phòng
  `use_figma`; thử trước bằng một lệnh nhỏ có **tự dọn**.

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
Đi đường dự phòng use_figma: <phần cần slot, hoặc "không">
Apply? (Y / sửa)
```

## Bước 6 — dựng (tuần tự, không ghi song song)

Từ dưới lên, **vài lời gọi `figma_write` nhỏ cho mỗi component set** (tạo set · thuộc tính ·
xếp + mô tả), không dồn cả họ vào một lệnh. Ghi id vào `state` để lời gọi sau bám vào.

**Khi lời gọi timeout hoặc lỗi giữa chừng — KHÔNG gọi lại ngay.** `figma_read get_page_model`
trên trang đích, xem phần nào đã có (proxy lưu `state` khi bị cắt — `stateSaved: true`). Có phần dở
→ xoá phần dở hoặc làm tiếp từ chỗ dừng; không tạo bản trùng. Timeout lặp ≥ 2 lần → nhắc user đưa
cửa sổ Figma ra trước, chia lời gọi nhỏ hơn. `createVariants` bị cắt giữa chừng để lại các component
rời **chưa gộp thành set** (một cái tên kiểu `<Tên>=Trục=…`) → xoá hết rồi gọi lại, không gộp tay.

1. **Khung chứa**: auto-layout dọc, nền surface. Cấp chữ: tên khung `Display 2` → tiêu đề section
   (`Master Components`, `Trạng thái & ví dụ`) `Display 3` → tên từng set / tên từng cảnh `Heading 1`
   → mô tả `Text/Body` secondary.
   * Trong `Master Components`, **mỗi set một khối** `Doc · <tên set>`: tên set → 1–2 câu mục đích
     (dùng ở đâu, khi nào) → bảng **Trường hợp** (viền `Border/Default`, bo `Radius/Container`): mỗi trục
     biến thể một cột, mỗi giá trị một dòng "giá trị — khi nào dùng / khác gì" → các biến thể.
   * Mỗi cảnh trong `Trạng thái & ví dụ`: tên cảnh + **một dòng mô tả** (người dùng đang làm gì, cảnh
     chứng minh điều gì). Không để cảnh nào chỉ có tên.
2. **Mỗi component set**:
   * `figma.createVariants(baseSpec, { Trục: [...] , ... })` — base là cây auto-layout, token gắn
     **lúc tạo**: `fill: "$<biến>"`, `textStyle: "<style>"`, `tokens: { padding, itemSpacing,
     cornerRadius }`. Biến thể khác nhau về hình → ghi đè theo từng biến thể trong `variantsOrAxes`.
     Base và **mọi khung con** đặt `layoutSizingHorizontal` / `layoutSizingVertical: "HUG"` (hoặc
     `FILL`) tường minh — khung con không khai sẽ cố định rộng 100px, chữ tràn và bị cắt.
   * Instance thành phần: `figma.instantiate({ key, variant: {...} })` (thư viện) hoặc
     `instantiate("<Tên>", { props })` (trong file), rồi `move` vào biến thể. `props` **tường minh mọi
     trục ảnh hưởng hiển thị** (thư viện mặc định thường không phải cỡ MD — xem § Tên trong Figma).
     Đổi sau: `setInstanceProperties`.
   * `arrangeComponentSet(setId, { columnsBy })` xếp lưới biến thể. Sửa kích thước biến thể sau đó →
     **chạy lại** `arrangeComponentSet`, nếu không biến thể tràn khỏi set.
   * Thuộc tính: `addComponentProperty(setId, { name, type, defaultValue, path | layerIds })` —
     `path` gắn đúng lớp đó ở **mọi** biến thể. Instance con cần chỉnh → `exposeNestedInstance`.
   * `setComponentDescription(setId, "...")` (mục đích, cách dùng, cách đổi trạng thái) — viết
     toàn văn, không đọc–sửa–ghi.
   * Phần cần **slot** (sau khi set đã dựng xong): (1) `figma_write` dựng khung nội dung có token,
     đặt tạm trong khung chứa; (2) `use_figma` ẩn con mặc định của slot rồi `slot.appendChild(nội dung)`;
     (3) `figma_write`: nội dung `layoutSizingHorizontal: "FILL"`, rồi chạy lại `arrangeComponentSet`.
   * Mẫu ghép đã vẽ sẵn trên canvas cần thành component → `figma.componentize(nodeId, { name,
     replaceCopies })` thay vì dựng lại; hỏi user trước khi thay các bản sao.
3. **Khung trạng thái**: instance của mọi biến thể quan trọng, có chú thích; ví dụ **Trong ngữ cảnh** —
   component đặt trong màn/vùng chứa nó (vd header màn chi tiết + panel mở neo dưới nút; mobile + scrim),
   dựng theo phương án bố cục user đã chọn ở Bước 5 (vẫn bằng token + component thật); phần *Chữ dài · kiểm tra*
   với nội dung cực trị ở bề rộng desktop và 320px (chữ rất dài, mã dài, thiếu dữ liệu tùy chọn).

### Bẫy đã gặp — làm đúng ngay từ đầu

**Đã có hàm lo** (dùng hàm, không tự làm tay):

| Việc | Hàm `figma_write` |
|---|---|
| Thêm biến thể mà giữ liên kết thuộc tính (clone tay làm mất `componentPropertyReferences`) | `addVariant(setId, { from, props })` |
| Gắn thuộc tính cho lớp ở mọi biến thể (khoá có hậu tố `#id`, gán từng biến thể) | `addComponentProperty` / `wireComponentProperty` với `path` hoặc `layerIds`; xem `wired` / `skipped` |
| Expose instance con | `exposeNestedInstance` — từ chối kèm gợi ý khi chỗ đó không ghi được |
| Đặt instance thư viện theo biến thể (tên biến thể có khoảng trắng, id import không sống sang lời gọi sau) | `instantiate({ key, variant })` trong cùng một lời gọi |
| Đổi thuộc tính instance (lỗi khi giá trị đã có, khi đang lặp node) | `setInstanceProperties` — giá trị trùng trả về `unchanged` |
| Đổi tên / mặc định thuộc tính mà không làm mất override của instance | `editComponentProperty` (không xoá rồi thêm lại) |
| Tìm mọi instance đã đặt | `findInstances(setId, { scope: "document" })` |
| Resize/sizing Figma không nhận | Kết quả `stuck` kèm lý do — đọc, đừng coi là xong |

**Vẫn phải tự tránh** (chuyện thiết kế hoặc chuyện của Figma, hàm không lo):

| Bẫy | Cách làm đúng |
|---|---|
| Container thư viện cố định bề rộng (vd Popover Surface 260px), `resize` không ăn (`stuck`) | `layoutSizingHorizontal: "FILL"` cho lớp trong, slot và nội dung |
| Container có INSTANCE_SWAP (vd BottomSheet `Content`) | Swap bằng `setInstanceProperties({ Content: componentId })`, không phải slot |
| Chữ 1 dòng: `maxLines` + `textAutoResize="HEIGHT"` vẫn tính cao nhiều dòng | `textAutoResize: "NONE"`, cao = line-height, `FILL`, `textTruncation: "ENDING"` |
| Phần tử dài đẩy phần kế bên ra ngoài | Hàng đó `layoutWrap: "WRAP"` |
| Hàng rỗng vẫn chiếm chỗ | Gắn BOOLEAN vào `visible` của **cả hàng** |
| Chữ trong EmptyState/Banner không xuống dòng | `FILL` + `textAutoResize: "HEIGHT"` |
| Badge/nhãn tuyệt đối bị cắt | Component cha `clipsContent: false` |
| Thuộc tính TEXT / INSTANCE_SWAP dùng **một giá trị mặc định cho mọi biến thể** (vd mọi Tone cùng icon `+`) | Nội dung khác nhau theo biến thể (icon theo Tone) → để sẵn trong từng biến thể + expose, không dùng INSTANCE_SWAP |
| Đổi icon (`swapComponent`) — override màu nét giữ được khi lớp vector của icon mới cùng tên (đã kiểm 2026-10-13 với icon Astryx: circle-dashed → check → plus) | Icon khác cấu trúc lớp → đọc lại `strokes` của vector sau khi swap; mất thì `applyVariable` |
| Gắn biến màu nét bằng `modify(id, { stroke: "$…" })` trên vector bị **bỏ qua, không báo lỗi** | `applyVariable(id, "strokes", "<biến>")`, rồi đọc lại `boundVariables` |
| Đổi biến thể của instance lồng (vd BottomSheet Capped → Tall) không đổi chiều cao; `resize` lớp lồng không ăn | Cần kích thước khác thì đặt trực tiếp instance của biến thể đó; ghi lưu ý vào description |
| Ẩn nhãn/mô tả của control thư viện (Selector, DateRangeInput…) | Ẩn cả khung `Label + Description`, không ẩn từng node con |
| Sửa main component nhưng instance **đã có nội dung slot riêng** không đổi theo (instance chưa override slot thì vẫn theo main — đã kiểm 2026-10-13) | Nội dung slot đã override là bản riêng của instance đó: `findInstances` rồi sửa luôn các instance đã đặt (khung trạng thái, chữ dài) |
| Nhãn của item thư viện (CheckboxListItem) không xuống dòng | Chữ `Label` trong `Label Wrapper`: `FILL` + `textAutoResize: "HEIGHT"`, item `FILL` |
| Khung ôm nội dung có con `layoutGrow = 1` → con bị ép về 0 | Trong component để con `HUG`; chỉ đặt grow trên instance đặt trong vỏ cao cố định (Drawer) để ghim chân |
| Gán lại `fills` cho chữ của control thư viện (đã gắn biến màu) làm chữ biến mất | Chỉ đổi nội dung chữ (`setText`); giữ nguyên fill gốc. Lỡ hỏng thì thay bằng instance mới |
| Sửa lớp chữ lồng trong main component (vd bật truncation) làm **mất chữ đã override** trên mọi instance | Sửa main trước khi đặt nội dung; nếu sửa sau thì gán lại nội dung cho các instance đã đặt |
| Phần nổi (menu, popover) đặt bên trong một hàng bị hàng vẽ sau đè lên | Trong khung cảnh, đặt phần nổi thành instance riêng ở lớp trên cùng của khung |
| Chip có "+n" bị cắt mất khi nhãn dài | Đưa "+n" vào `End Content` của Token; nhãn 1 dòng + `maxWidth` cho Token |
| Nền nhấn nhẹ trùng nền ở Dark | Kiểm mode Dark (Bước 7); đặt khối trên bề mặt có tông khác |
| File vừa bị người khác sửa (id đổi, node trùng) | Đọc lại cấu trúc; không xoá thứ mình không tạo, hỏi user |
| `resize` rồi đặt sizing `AUTO` → component kẹt cao cố định, nội dung con (Banner) tràn | Resize trước, đặt sizing `AUTO`/`HUG` sau cùng |
| Nhãn `Collapsible` thư viện (`Text/Large`) lấn át tiêu đề khối | Hạ text style trên instance (`Text/Label`, màu secondary), không sửa main thư viện |
| Đọc description rồi sửa và ghi lại → dấu `"` thành `&amp;quot;` (giá trị đọc ra đã escape HTML) | Viết lại toàn văn description, không đọc–sửa–ghi |
| Hai đường kẻ chồng nhau (Entry có viền dưới + khối cha có viền dưới) | Bỏ viền của phần tử con trong khối có viền riêng |
| `auditDesignSystem` báo `cornerRadius` off-system trên chính **khung component set** (Figma tự đặt) | Bỏ qua mục đó; chỉ xử lý giá trị trong biến thể |

**Chỉ khi đi đường dự phòng `use_figma`** (Plugin API gốc):

| Bẫy | Cách làm đúng |
|---|---|
| Đặt nội dung vào slot của instance (đã kiểm 2026-10-13 với Dialog `Body`) | `slot.appendChild(node)`; ẩn con mặc định của slot. Chỉ chuyển nội dung đã dựng bằng `figma_write`; không tạo chữ mới bằng `use_figma` (không gắn token) |
| Không tìm thấy lớp đang ẩn trong instance, hoặc "node does not exist" khi đổi `visible` | Đầu mỗi script: `figma.skipInvisibleInstanceChildren = false` |
| Sửa chữ | `loadFontAsync` mọi font của node (`getStyledTextSegments(['fontName'])`) trước |
| Khoá thuộc tính có hậu tố (`Label#8:11`) | `Object.keys(inst.componentProperties).find(k => k.startsWith('Label'))` |
| `setProperties` trên instance lồng khi đang lặp `findAll` → "node does not exist" | Đổi biến thể xong thì dừng vòng lặp; tìm lại node sau mỗi lần đổi |
| Lệnh ghi lỗi giữa chừng | Cả lệnh được hoàn tác — đọc lại canvas trước khi chạy lại |

## Bước 7 — tự kiểm trước khi trình

Kiểm bằng dữ liệu trước, ảnh chụp sau. **Lớp máy** (lỗi chặn sửa hết trước khi sang phần tự rà):

1. Số liệu trả về: số biến thể, tên thuộc tính (`wired` / `skipped` của từng thuộc tính), kích thước
   từng biến thể, mọi kết quả `stuck`. `getNodes` **không** trả `componentPropertyReferences` —
   kiểm liên kết bằng `wired`, hoặc đặt một instance rồi `setInstanceProperties` thử.
2. `figma_read layout_audit` từng component set, khung trạng thái và khung *Chữ dài*: tràn, bị cắt,
   chữ bị cắt ba chấm ngoài ý muốn.
3. `figma_read a11y_audit`: tương phản (cả chữ phụ trên nền nhấn), vùng chạm, control thiếu tên. Ngoại
   lệ đã chấp nhận trong *Accessibility* của `design.md` liệt kê là "đã biết". Rồi gọi skill
   `accessibility-review` làm lớp thứ hai, gộp kết quả.
4. `figma.auditDesignSystem(setId)`: mục tiêu `compliance` = 1.00 — giá trị `hardcoded` gắn lại token,
   `off-system` đổi sang giá trị có token hoặc ghi vào báo cáo. Thay cho việc soát mã hex bằng mắt.
5. `figma_read responsive_audit` trên ví dụ *Trong ngữ cảnh* (Mobile: 320/360/390/430): bổ sung cho
   khung *Chữ dài*, không thay — chữ cực trị vẫn phải dựng tay.
6. **Dark:** một khung mẫu đặt mode Dark bằng `modify(frameId, { explicitVariableModes: { <collection
   màu>: "Dark" } })` (tên collection/mode đọc từ `figma_rules`); không có mode Dark thì bỏ, ghi 1 dòng.

**Tự rà** (máy không kiểm):

7. **Một ảnh chụp mỗi component set**, một ảnh khung trạng thái, một ảnh *Chữ dài*, chụp **một lần** ở
   cuối. Tìm: khoảng trống thừa, nội dung mặc định còn sót ("Button", "Content", giờ kiểu Mỹ…). Đối
   chiếu từng quy tắc chữ dài và hành vi của spec với ảnh.
8. Do's and Don'ts của `design.md`: (a) ≤ 1 nút Primary mỗi nhóm; (b) trạng thái không chỉ dựa vào
   màu; (c) đủ rỗng / đang tải / lỗi; (e) không vi phạm "Không nên" của component thành phần.
9. **Chip trạng thái:** component có trạng thái dùng instance `Chip trạng thái` (không tự vẽ pill); icon và chữ
   đúng màu `Status Chip/<Sắc>/Foreground` (đổi icon qua thuộc tính `Icon` xong kiểm màu nét, quét cả biến
   thể gốc lẫn instance — `findInstances`); mã nghiệp vụ dùng `Text/Code Small`; khung *Chữ dài* thử tên/nhãn dài nhất cho phép
   (14 ký tự) + mã dài nhất. Component gắn với feature có `*-states.md` → chạy
   `python3 _scripts/status-chip-lint.py <file states>`; FAIL thì báo, KHÔNG tự đổi nhãn nghiệp vụ.
10. Sửa lỗi → chạy lại audit của phần đã sửa, chụp lại **chỉ phần đã sửa**.

## Bước 8 — cập nhật component đã có

Sửa **tại chỗ** để giữ liên kết instance:

* Đổi tên biến thể thay vì xoá-tạo (override đi theo tên mới).
* Thêm biến thể: `addVariant(setId, { from: <biến thể gần nhất>, props })` rồi sửa phần khác.
* Đổi tên / mặc định thuộc tính: `editComponentProperty` — không xoá rồi thêm lại (mất override của
  mọi instance).
* Xoá thuộc tính: gỡ node gắn với nó rồi `deleteComponentProperty(setId, "<tên>")`.
* Đổi nội dung mẫu: `setInstanceProperties`; đổi cấu trúc: sửa main component.
* Trước khi sửa main: `findInstances(setId, { scope: "document" })` — biết instance nào sẽ đổi theo,
  instance nào có nội dung slot phải sửa tay.
* Hỏi user có chỉnh tay gì không trước khi sửa; chỉnh tay là dữ liệu, không ghi đè.

## Bước 9 — báo cáo và cập nhật tài liệu

```
Đã dựng "<Tên>" trong <file>, trang <trang> (node <id khung>):
<set> <n biến thể> · <set> <n> · …
Máy đã kiểm: biến thể/thuộc tính · layout_audit · a11y_audit · compliance <x> · responsive <w…> · Dark
Tự rà: ảnh chụp <n> · chữ dài ở <w> và 320px · Do's and Don'ts
Đường dự phòng use_figma: <phần nào, vì sao — hoặc "không dùng">
Máy KHÔNG kiểm: nội dung nghiệp vụ đúng chưa [Cao] · thiếu trạng thái nghiệp vụ nào [Cao] · thẩm mỹ [Thấp]
Chưa có chuẩn trong design.md: <…>
```

Rồi cập nhật spec của component trong `design.md` (bảng: tên set, key, biến thể/thuộc tính, dựng
từ gì; các quyết định mới; Known Gaps theo Iteration Guide — dòng `KG-nn` trong `design.md` + hàng chi
tiết ghi ngay tại dòng đó, không có file backlog riêng) — qua approval gate. Quyết định mới lặp lại ở ≥ 2 spec → đề xuất
đưa lên *Quy ước chung của component dự án*.

**Màn của feature đổi theo** (Bước 8 sửa main component → instance trên màn đổi theo): từ
`findInstances(setId, { scope: "document" })`, lấy frame màn có instance (tên `<[#]> · <web|mob> · <slug>`)
→ feature + flow qua cột `Figma` của `screens/{feature}-screen-index.md` hoặc wireframe index. Đổi nhìn
thấy được trên màn (chữ, phần tử thêm/bớt, trạng thái) → gọi `/figma-sync {feature} --flow {flow}` inline cho
từng flow bị chạm (`.claude/rules/screen-source.md` Mục 5). Chỉ đổi hình (màu, bo, khoảng cách) → không gọi,
ghi "màn bị chạm: n, chỉ đổi hình" trong báo cáo.

## Constraints

### Luật cứng

* Không dựng khi chưa có spec đã duyệt trong `design.md`.
* Không tạo component trùng cái thư viện đã có; không vẽ lại control; không sửa main component
  của thư viện.
* Không mã màu/cỡ/khoảng cách cứng khi đã có token.
* Không bịa nội dung nghiệp vụ; không bịa giá trị ở Known Gaps — hỏi, hoặc ghi "chưa có chuẩn trong
  design.md".
* Không xoá node mình không tạo; không dựng bản thứ hai khi đã có.
* Thiết bị luôn hỏi user. Không ghi song song (`figma_write` hay `use_figma`).
* `use_figma` chỉ cho việc `figma_write` không làm được (slot); mỗi lần dùng ghi vào báo cáo.

### Tuân thủ rule workspace

Skill này là "skill vẽ" theo nghĩa của `.claude/rules/design-system.md`: đọc `design/design.md` theo
mục (mục lục + mục luôn đọc + mục của `/figma-component` trong bảng của rule), tuân theo *Luật khi sinh màn*, dùng Do's and Don'ts làm tiêu chí tự kiểm, đụng
Known Gaps thì hỏi hoặc ghi "chưa có chuẩn trong design.md".

## References

- Rule workspace `.claude/rules/design-system.md`.
- `design/design.md`: spec component, token, § Tên trong Figma, States, Content & Formatting,
  Accessibility, Responsive, Known Gaps, Quy ước chung của component dự án. Ví dụ spec đầy đủ:
  § Notification Center.
- `design/components.md`: Usage / Nên / Không nên của component thành phần.
- `design/setup-figma.md`: khi file đích chưa có thư viện.
- `../reqwise-diagram-rules.md` § 5: cổng kết nối.
- `figma_docs(section="api" | "recipes")`: cú pháp `figma_write` (component: `createVariants`,
  `addComponentProperty`, `addVariant`, `instantiate`, `componentize`, `findInstances`).
- `skill://figma/figma-use/SKILL.md`: luật Plugin API — chỉ cho đường dự phòng `use_figma`.
- `/figma-design-system` (dựng cả bộ DS), `/figma-screen` (vẽ màn dùng component này).
