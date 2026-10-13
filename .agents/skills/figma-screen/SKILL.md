---
name: figma-screen
description: Vẽ màn hình giao diện (UI) lên Figma theo đúng design system của dự án — đề xuất 3 phương án bố cục (1 theo mẫu có sẵn trong design/design.md + 2 độc lập) để user chọn, dùng component thật (instance), gắn token theo tên, vẽ đủ trạng thái rỗng/đang tải/lỗi, rồi tự kiểm trước khi trình. Dùng khi ai đó nói "vẽ màn", "dựng màn hình", "vẽ UI", "mock up màn", "làm giao diện cho <tính năng>" trên Figma.
allowed-tools: Read, Glob, Grep, Edit, Write, Bash, Task, AskUserQuestion, mcp__reqwise-figma__figma_status, mcp__reqwise-figma__figma_docs, mcp__reqwise-figma__figma_read, mcp__reqwise-figma__figma_rules, mcp__reqwise-figma__figma_write, mcp__claude_ai_Figma__get_metadata, mcp__claude_ai_Figma__get_screenshot, mcp__claude_ai_Figma__download_assets
user-invocable: true
argument-hint: "<màn hoặc tính năng cần vẽ> [@nguồn: srs, states, userflow]"
---

# /figma-screen — màn hình đúng design system, bố cục do user chọn

Đọc cổng kết nối trong `../reqwise-diagram-rules.md` trước (§ 5, *Before anything else: is the
write path open?*). Tóm tắt: plugin đã kết nối, chỉ một cửa sổ, gọi `figma_status` trước mọi thứ,
và dry run **không** phải phép thử kết nối. Phần còn lại của file đó nói về sơ đồ. Màn hình không
phải sơ đồ, nên các bước dưới đây thay cho luật vẽ sơ đồ.

Cú pháp `figma_write`: `figma_docs(section="api", level="cheat")` và `figma_docs(section="recipes")`.
Đọc một lần trước lần vẽ đầu tiên của phiên.

## Mục tiêu

Một (hoặc vài) artboard trên Figma mà designer/dev nhận vào là dùng được: **khung trang lấy từ
mẫu có sẵn, mọi control là instance của component thật, mọi màu/chữ/khoảng cách gắn token**, có
đủ các trạng thái mà nghiệp vụ cần. Màn phải đọc được như sản phẩm thật: chữ tiếng Việt thật,
dữ liệu mẫu hợp lý, không "Lorem ipsum", không "Button".

__Việc chính là quyết định, không phải thao tác vẽ.__ Bố cục nào (user chọn trong 3 phương án), màn có những vùng gì,
mỗi vùng ở trạng thái nào, nút nào là nút chính. Công cụ vẽ nhanh, còn vẽ sai khung thì phải vẽ
lại cả màn.

## Luật quyết định thành bại

**`design/design.md` là nguồn duy nhất.** Đọc lại từ file mỗi lần chạy, **theo mục** như rule workspace
quy định (Bước 1.2), không trích từ trí nhớ phiên trước (file có thể đã đổi). Mọi giá trị cụ thể (màu, cỡ, mẫu bố cục, tên component, tên biến
Figma, định dạng ngày/tiền) lấy từ đó. Skill này **không** chứa giá trị nào của dự án.

Chưa có `design/design.md` → báo 1 dòng "Chưa có design/design.md — dùng mặc định của skill", rồi
đọc `figma_rules` (token/component đang có trong file) và `figma_docs(section="style")` làm mặc
định. **Không** tự bịa design system.

## Bước 1 — đọc trước, hỏi sau

Không hỏi user những gì đọc được.

1. `figma_status` → xác nhận plugin, file, trang đang mở.
2. Đọc `design/design.md` theo mục (cách đọc: `.claude/rules/design-system.md` § Nguồn duy nhất) —
   file dài, đọc thừa làm chậm và đẩy phần cần dùng ra khỏi tầm chú ý:
   * `Grep -n "^## \|^### "` lấy mục lục; Read từng mục bằng offset/limit.
   * **Luôn đọc:** Typography › Principles, Tên trong Figma, Do's and Don'ts, Iteration Guide,
     Known Gaps.
   * **Của skill này:** Layout (toàn bộ, gồm *Mẫu bố cục* P/M); phần đầu § Components tới hết quy
     ước "Web và Mobile" + mục `###` của nhóm component định dùng; § Phân trang danh sách nếu màn có
     danh sách; trong § Components - <dự án>: *Quy ước chung* + spec của component dự án có trên
     màn; States (+ *Ánh xạ trạng thái nghiệp vụ*); Content & Formatting; Accessibility; Responsive
     Behavior.
   * Không đọc Overview, Colors, Typography Hierarchy, Elevation, Shapes: token gắn theo tên (tên ở
     § Tên trong Figma). Đoạn đã đọc có "xem §…" → đọc luôn đoạn đó.
   * Chi tiết từng Known Gap nằm ngay tại dòng `KG-nn` trong § Known Gaps (không có file backlog riêng).
   Có `design/components.md` thì đọc **Bảng chọn nhanh**, rồi đọc mục riêng của từng component định
   dùng (Usage, Nên/Không nên, Examples). File dài, nên không đọc toàn văn.
3. Tìm nguồn nghiệp vụ trong `docs/{feature}/` (Glob), đọc theo thứ tự ưu tiên:
   * **`srs/{feature}-userflow.md`** — nguồn DUY NHẤT cho danh sách màn, chia flow, chuyển màn
     (Mục 2, 3, 3.5) và tác vụ chính (Mục 3.6). `screenId` = cột `[#]` Mục 2 + ` · ` + thiết bị
     (`[#]` = 1.1, Desktop → `1.1 · web`); slug + tên Việt cũng lấy ở Mục 2.
   * **Wireframe + bảng mô tả 5 cột** của từng màn. Bảng 5 cột là **hợp đồng BA ↔ design**: element
     nào, control gì, validation, trạng thái, wording, mã lỗi, điều hướng. Đọc hết bảng của mọi màn sẽ
     vẽ. Hai renderer ngang hàng, cùng schema 5 cột — màn có ở renderer nào thì đọc renderer đó:
     - **HTML** — `html-wireframe/{flow-slug}.html` + `{feature}-wireframe-html-index.md`. Bố cục =
       khối `<div class="wf-screen" id="s{n}">`; bảng = `<table class="wf-desc-table">`, phân đoạn
       theo hàng `wf-desc-screen-header` "Screen N: …". `n`/`N` là thứ tự màn trong flow → ra `Slug`
       qua cột "Screens (theo thứ tự)" của index (đối chiếu userflow Mục 3). Dùng cho màn phức tạp.
     - **ASCII** — `ascii-wireframe/{flow-slug}.md` + `{feature}-wireframe-index.md`, block
       `## Screen: {slug}`.
     Màn có ở **cả hai** → bảng HTML làm nguồn chính (`/wireframe-html` đã lấy ASCII làm nguồn rồi bổ
     sung); hai bảng lệch nhau (row, wording, mã lỗi) → liệt kê chỗ lệch, hỏi user bản nào đúng, KHÔNG
     tự chọn im lặng.
     - **Flow đã lên Figma** — `screens/{flow-slug}.md` (block `## Screen: {slug}`, trạng thái ở
       `### Trạng thái:`) là nguồn **duy nhất**, thắng cả HTML lẫn ASCII; wireframe cũ của flow đó đã bị
       xoá (`.claude/rules/screen-source.md` Mục 2). Đây thường là lần sửa màn (Bước 5).
   * `srs/{feature}-spec.md` (FR/BR/Error Matrix), `srs/{feature}-states.md`, `usecases/uc-*.md`,
     file user tag bằng `@`.
   * **Bản đồ đối tượng** `{feature}-object-map.md` + `docs/_shared/object-map.md` (nếu có) — nguồn
     **phụ**, bảng 5 cột vẫn là hợp đồng. Dùng cho màn danh sách/thẻ/chi tiết của một đối tượng:
     - Không có bảng 5 cột (vẽ thẳng từ SRS) → Items lấy theo cột "Hiện ở" (Thẻ / Danh sách / Chi
       tiết) Mục 4; "Lọc"/"Sắp" → bộ lọc (CMP-05) / cột sắp được; nút lấy từ Mục 3, chỉ cho vai trò
       được làm.
     - Có bảng 5 cột → đối chiếu: thuộc tính mức Thẻ/Danh sách mà bảng thiếu, nút cho vai trò không có
       quyền theo Mục 3 → **vẫn vẽ theo bảng**, ghi vào báo cáo mục "Đề xuất đổi so với bảng 5 cột".
     - Đối tượng có dòng ở Mục 5 (đề xuất hiển thị dùng chung) → thẻ/dòng danh sách của đối tượng đó
       vẽ giống nhau trên mọi màn (cùng instance nếu đã có component dự án; chưa có thì ghi gợi ý
       `/figma-component` trong báo cáo, không tự dựng component).
     KHÔNG sửa object map — lệch thì đề xuất `/object-map {feature}`.
   Có nguồn thì **dẫn xuất từ nguồn**, chỉ hỏi phần nguồn bỏ trống. Màn sẽ vẽ chưa có wireframe ở
   renderer nào → báo 1 dòng và hỏi: chạy `/wireframe-html` trước (đề xuất cho màn phức tạp) hoặc
   `/wireframe-ascii` (màn đơn giản), hay vẽ thẳng từ SRS (ghi "không có bảng 5 cột" trong báo cáo —
   mất bước khớp đặc tả mục 9 Bước 6 và không ghi được link Figma về repo).
4. **UI Common Rules & Components** (theo `.claude/rules/ui-common-rules-components.md`): đọc bảng
   mục lục `design/ui-common/screen-patterns.md` (CMP) + `conventions.md` (GR, E-common); bảng 5 cột
   ghi `Xem CMP-xx` / `Theo GR-xx` nào thì đọc mục đó. CMP có dòng **Figma** → dùng đúng component +
   node mẫu ghi ở đó.
5. `figma_read` op `get_page_model` trên trang đích. Đã có màn cùng `screenId` thì đây là **sửa**,
   không phải vẽ mới (xem Bước 5). Userflow trên Figma (nếu có) chỉ là bản minh hoạ: lệch với
   userflow repo (thiếu/thừa màn, sai thứ tự) → báo user, **repo thắng**, đề nghị cập nhật bản Figma
   bằng `/figma-userflow`.

## Bước 2 — hỏi user

Chỉ hỏi phần user **chưa nói rõ** và phần nguồn (Bước 1) không trả lời được. Hỏi bằng
`AskUserQuestion`, gộp các câu còn lại vào **một lượt**, rồi trình kế hoạch và chờ `Y`.

### 2.1 Vẽ màn nào, chế độ nào

* Input đã nêu **một hoặc vài màn cụ thể** → **chế độ Nhanh**, danh sách màn đã rõ, không hỏi.
* Input nói **cả tính năng / cả luồng** → hỏi 1 câu: "Vẽ {tính năng}: chỉ trạng thái chính mỗi
  màn (**Nhanh**), hay vẽ **Đầy đủ** kèm trạng thái rỗng / đang tải / lỗi và nút đang xử lý /
  vô hiệu? (nên chọn Đầy đủ nếu có form hoặc validation phức tạp)".
* Input chỉ có **tên tính năng**, không rõ màn → hỏi gộp 1 lần: liệt kê các màn (lấy từ `srs/{feature}-userflow.md`
  Mục 2-3), hỏi "Vẽ hết hay chọn vài màn? Vẽ hết thì cần đủ trạng thái hay chỉ
  trạng thái chính?".

Chế độ **Đầy đủ**:
* Trạng thái đề xuất theo mục *States* của `design.md`; nút có trạng thái khác biệt (đang xử lý,
  vô hiệu) thì thêm biến thể.
* **Gom lỗi cùng kiểu hiển thị** (dòng lỗi dưới ô, banner, toast): mỗi kiểu vẽ 1 artboard đại
  diện, kèm ghi chú liệt kê các lỗi còn lại cùng kiểu.
* **Trạng thái loại trừ nhau** (vd thành công / hết hạn) là **màn riêng**, mỗi cái 1 artboard.
  Nguồn nhồi hai trạng thái loại trừ vào một màn → báo user, không vẽ lẫn lộn.

Chế độ **Nhanh** tính là user **đã bỏ** các trạng thái phụ: ghi rõ trong báo cáo (Bước 7), không
coi là thiếu ở mục tự kiểm (c).

### 2.2 Thiết bị: HARD GATE, luôn hỏi

`design.md` chỉ **đề xuất**, không quyết thay user, kể cả khi file ghi rõ.

* Đề xuất sẵn 1 lựa chọn: ưu tiên `primary_device` trong `srs/{feature}-userflow.md` (nếu có);
  không có thì lấy từ *Responsive Behavior* của `design.md`.
* Các lựa chọn: **Desktop 1920×1080** / **Tablet 768** / **Mobile 375** / **Responsive**. Lựa
  chọn đề xuất đặt đầu, gắn "(Đề xuất, theo {nguồn})".
* Chọn thiết bị mà `design.md` chưa có chuẩn (Known Gaps) → nói rõ trước khi vẽ: vẽ tạm và ghi
  "chưa có chuẩn trong design.md".
* Thiết bị đã chốt → cố định `frameW` cho mọi artboard, không dùng số của thiết bị khác. `frameH`
  theo nội dung, tối thiểu bằng chiều cao thiết bị; riêng nhóm responsive cao cố định
  (`design/setup-figma.md` › *Bố cục trong Section con*).
* Userflow chưa ghi `primary_device` → gợi ý ghi vào để lần sau không hỏi lại.

### 2.3 Câu hỏi riêng của skill này (chỉ hỏi khi cần)

* **Vẽ userflow trước?** Hỏi khi yêu cầu là một *luồng* (≥ 2 màn) và trang chưa có flow. User
  đồng ý thì dừng skill này, đề nghị chạy `/figma-userflow`, rồi quay lại vẽ màn theo flow đã
  chốt. Có flow rồi mà màn mới chưa nằm trong flow thì nhắc user cập nhật flow.
* **Bố cục — 3 phương án**: mẫu trong *Mẫu bố cục* chỉ là một phương án. Đề xuất (a) **A**: mẫu
  gần nhất, chỉnh vùng/nội dung cho hợp màn, nêu giống ở đâu/chỉnh gì; (b) **B, C**: hai phương án
  độc lập, thiết kế từ nhu cầu màn (nhiệm vụ chính, lượng dữ liệu, thiết bị), không xuất phát từ mẫu
  và khác nhau thật về cách tổ chức, mỗi cái kèm lý do và đánh đổi. Cả ba vẫn dùng token, component
  thật và Do's and Don'ts của `design.md`. User chọn; chọn B/C và khung đó dùng lại → đề xuất thêm
  mẫu vào `design.md` theo Iteration Guide.

### 2.4 Chia đợt nếu nhiều

* Nhanh: > 10 màn → liệt kê và hỏi user chọn đợt.
* Đầy đủ: > 15 artboard (màn + trạng thái) → hỏi chọn đợt theo luồng, tránh timeout.

### 2.5 Trình kế hoạch (L1), chờ `Y`

Chế độ Nhanh:

```
Em sẽ vẽ 2 màn cho "Quản lý đơn hàng" lên Figma:
Luồng 2 — Duyệt đơn: 2.1 · web order-list → 2.2 · web order-detail
2.1 · web · order-list     Mẫu P1 · S1 Shell · Side Nav · nút chính [Tạo đơn]
2.2 · web · order-detail   Mẫu P7 · nút chính [Duyệt]
Khung: Desktop 1920×1080
Nơi vẽ: trang "02 · Đơn hàng" › F01 · Duyệt đơn › Web
Token/component: design/design.md (Astryx), instance thư viện
Trạng thái phụ: không vẽ (chế độ Nhanh)
Chưa có chuẩn: (không)
Apply? (Y / sửa / chọn màn cụ thể)
```

Chế độ Đầy đủ:

```
Em sẽ vẽ "Quản lý đơn hàng" theo 1 luồng, tổng 2 màn + 3 trạng thái:
Luồng 1 — Duyệt đơn (mỗi màn một nhóm, state xếp dọc):
  2.1 · web · order-list (có dữ liệu) ↓ Empty ↓ Loading
  2.2 · web · order-detail (bình thường) ↓ Load error
Lỗi đại diện: 2.2 · web banner lỗi tải; ghi chú liệt kê các lỗi còn lại cùng kiểu banner
Trạng thái nghiệp vụ → nhóm: Nháp→Neutral · Chờ duyệt→Warning · Đã duyệt→Success · Từ chối→Error
Khung: Desktop 1920×1080
Nơi vẽ: trang "02 · Đơn hàng" › F01 · Duyệt đơn › Web
Token/component: design/design.md (Astryx), instance thư viện
Chưa có chuẩn: (không)
Prototype: nối theo userflow Mục 3.5 · flow: UC-xem-quy-trinh-cua-ban-ghi · Xem quy trình của một bản ghi (Web), …
Apply? (Y / sửa / chọn luồng cụ thể)
```

User nói "vẽ luôn đi" → dùng đề xuất mặc định, **trừ thiết bị** (vẫn phải chốt), và nói rõ các
giả định trong một đoạn để user sửa một lần.

## Bước 3 — chốt nơi vẽ

Component phải là **instance thật**. File dự án được setup theo `design/setup-figma.md`, theo một
trong hai cách: **A** (bật thư viện đã publish) hoặc **B** (file dự án là bản sao của file thư viện).
Nhận diện cách đang dùng trước khi vẽ:

```js
const local = await figma.findComponent("Button");   // tên component chính trong design.md
return local;
```

* **Tìm thấy trong file (Cách B)** → dùng `figma.instantiate("<Tên>")` như Bước 4.
* **Không thấy trong file** → có thể là Cách A. Read `design/figma-library-keys.json`, lấy key của
  component cần dùng, rồi `figma.getLibraryComponent(key)` và instantiate theo **id** trả về. Nạp
  mỗi component một lần, lưu id vào `state` để dùng lại trong phiên.
* **Không có key, hoặc `getLibraryComponent` lỗi** → file chưa setup. **Dừng**, chỉ user đọc
  `design/setup-figma.md` và chạy mục 3 (Kiểm tra setup). Chỉ vẽ khung tự dựng bằng token khi user
  đồng ý rõ ràng, và phải ghi "không dùng component thư viện" trong báo cáo.

Nơi đặt màn: **trang module** `NN · <Module>`, trong Section feature `Fxx · <tên feature>`, rồi vào
Section con `Web` hoặc `Mobile` theo thiết bị đã chốt. Section chưa có thì tạo. **Chưa có trang
module thì hỏi user** trước khi tạo (`figma.createPage`), đặt trong nhóm `SCREENS`, tên thụt 5 dấu
cách (`"     06 · <Module>"`); tìm trang theo tên thì `trim()` trước khi so. Không tạo trang riêng cho
từng feature. **Không bao giờ** vẽ lên các trang nhóm DESIGN SYSTEMS (component của thư viện),
Sandbox hay Archive. Quy ước đầy đủ: mục *Cấu trúc trang file dự án* của `design/setup-figma.md`.

User nhờ "kiểm tra setup" → chạy đúng bảng ở mục 3 của `design/setup-figma.md` trên một frame tạm
ở góc xa canvas, báo đạt/trượt từng dòng, rồi **xóa frame tạm**.

## Bước 4 — vẽ

Mỗi màn (hoặc trạng thái) vẽ bằng **vài lời gọi `figma_write` nhỏ**, không dồn cả cây vào 1 lệnh:
artboard + khung trang (mục 1-2) là 1 lời gọi, rồi mỗi vùng nội dung (header, bộ lọc, bảng, panel…)
1 lời gọi riêng. Ghi `nodeId` artboard và từng vùng vào `state` để lời gọi sau bám vào.

**Khi lời gọi timeout hoặc lỗi giữa chừng — KHÔNG gọi lại ngay.** Plugin có thể đã ghi một phần lên
canvas (nhất là khi cửa sổ Figma chạy nền, plugin chậm hẳn):
1. `figma_read` op `get_page_model` trên trang đích, xem node nào của lời gọi đó đã có.
2. Có phần dở → xoá phần dở rồi vẽ lại vùng đó, hoặc vẽ tiếp từ chỗ dừng. KHÔNG tạo đè thành bản trùng.
3. Artboard đã vẽ trước đó biến mất → báo user ngay, không lặng lẽ vẽ lại.
4. Timeout lặp lại ≥ 2 lần → nhắc user đưa cửa sổ Figma ra trước (plugin chạy nền bị trình duyệt
   hãm tốc), rồi chia vùng nhỏ hơn nữa.

Thứ tự dựng:

1. **Artboard**: kích thước theo thiết bị đã chốt. Tên frame chính **3 phần** `<[#]> · <web|mob> · <slug>`,
   ví dụ `"1.1 · web · process-line"`, để userflow nối được (`linkScreens`). Desktop, Tablet, Responsive
   dùng `web`; Mobile dùng `mob`; web và mobile cùng màn chung số + slug. `screenId` trong userflow phải
   ghi đủ thiết bị (`1.1 · web`), vì ghi `1.1` sẽ khớp nhầm cả bản `mob`.
   Nền dùng token nền trang của `design.md`. Đặt frame theo *Bố cục trong Section con* của
   `design/setup-figma.md`: mỗi màn một nhóm có thanh title; state xếp dọc dưới frame chính cách
   100px; modal bên phải màn mở ra nó; các nhóm cách nhau 400px. Title nhóm ghi
   `<screenId> · <slug> — <tên Việt> — States`. Frame state và modal **4 phần**
   `<screenId> · <slug> · <tên tiếng Anh>` theo *Tên frame* + bảng từ vựng của `design/setup-figma.md`
   (vd `1.1 · web · process-line · Loading`); state có số riêng trong userflow là màn riêng, 3 phần. Vẽ xong mà frame cao thêm thì canh
   lại khoảng cách cả cột.
2. **Khung trang**: dựng đúng cấu trúc của mẫu S/P đã chọn (vùng, thứ tự, cột, rail), bằng
   `children: [...]` trong một lần `create`. Frame bố cục dùng auto-layout, gap bằng `itemSpacing`
   gắn token spacing, không dùng spacer.
3. **Component**: `figma.instantiate("<Tên>", { parentId })`, rồi
   `figma.setInstanceProperties(id, {...})` **đặt tường minh mọi trục ảnh hưởng hiển thị**, theo
   mục *Tên trong Figma* của `design.md` (cỡ mặc định, bật/tắt icon, nhãn, biến thể). Instance không
   đặt được trong `children`, nên hãy tạo rồi `move` vào frame.
4. **Token**: gắn theo **tên Figma** (quy tắc đổi tên ở `design.md`):
   `fill: "$<biến>"`, `textStyle: "<style>"`, `tokens: { padding, cornerRadius, itemSpacing }`.
   Tên sai thì công cụ báo lỗi trước khi tạo node. Đọc danh sách gợi ý, **không** thay bằng mã hex.
5. **Nội dung**: chữ tiếng Việt thật theo *Content & Formatting* (viết hoa, nhãn nút, ngày giờ,
   số, tiền). Nhãn trạng thái lấy **nguyên văn** từ `srs/{feature}-states.md`, còn nhóm màu lấy từ
   bảng *Ánh xạ trạng thái nghiệp vụ*. Dữ liệu mẫu: 5–8 hàng, giá trị đa dạng, có một giá trị dài
   để thử tràn chữ.
6. **Lớp phủ**: dialog/drawer dùng `figma.overlay({...})` cho scrim, **không** dùng frame bán trong suốt.
   Dialog/drawer vẽ trên **frame riêng bên phải màn mở ra nó** (cả màn + lớp phủ + modal), tên tiếng
   Anh theo việc (`Approve order`). Dropdown, popover, menu vẽ ngay trong frame màn.
7. Đặt tên layer theo **việc nó làm** ("Nút duyệt đơn", "Ô tìm đơn hàng"), không để "Frame 12".
   `a11y_audit` dựa vào tên layer để nhận diện control.
8. **Bám bảng 5 cột** (khi có — Bước 1.3). Bảng là hợp đồng, không phải gợi ý:
   * Mỗi row → 1 element trên màn, đúng `Control type` (tra `design/ba-crosswalk.md` → component).
     Không bỏ row; row không vẽ được → ghi lý do trong báo cáo.
   * Nhãn, placeholder, wording lỗi lấy **nguyên văn** từ cột Description.
   * Trạng thái mặc định theo Description (vd "vô hiệu tới khi chọn đủ tài xế + xe" → artboard chính
     vẽ nút ở trạng thái vô hiệu; bản bật thuộc artboard trạng thái nếu chế độ Đầy đủ).
   * `Xem CMP-xx` → component + node mẫu ở dòng **Figma** của CMP, điền phần "UC phải khai báo".
     `Theo GR-xx` → áp quy tắc đó (bộ đếm ký tự, căn cột số/ngày, thứ tự nút…).
   * Lỗi vẽ đúng loại GR-15 ghi trong bảng (Inline / Popup / Toast) ở artboard lỗi đại diện.
   * Thấy nên khác bảng (đổi chữ, bỏ/thêm element) → vẫn vẽ theo bảng, ghi vào báo cáo mục
     "Đề xuất đổi so với bảng 5 cột" cho user quyết (đổi thật thì qua `/cr`).

## Bước 4b — nối prototype

Chạy khi đã vẽ **trọn một flow** (đủ màn theo userflow Mục 3) ở chế độ Đầy đủ, hoặc khi user nhờ "nối
prototype". Chế độ Nhanh hoặc vài màn lẻ thì không nối, ghi lý do trong báo cáo.

**Nguồn nối:** userflow Mục 3.5, mỗi dòng (Từ màn → Đến màn, Trigger) là một liên kết. Frame tìm theo
`screenId` trong tên (luật *Tên frame* của `design/setup-figma.md`). Không tự thêm liên kết mà Mục 3.5
không có.

**Cách nối theo loại trigger:**
* Người dùng bấm, chọn, chạm (vd "Bấm Thử lại", "Chọn bước") → tìm control trong frame nguồn theo tên
  layer (mục 7 Bước 4) hoặc theo chữ trên control, rồi `figma.setReactions` với `ON_CLICK` → `NAVIGATE`
  tới frame đích, `transition: null`. Không thấy control, hoặc thấy hơn một → không đoán, ghi vào báo cáo.
* Hệ thống tự chuyển ("Tải xong"): chỉ nối **nhánh thành công** bằng `AFTER_TIMEOUT` 1 giây.
  Mỗi frame tối đa một liên kết tự chuyển. Nhánh lỗi do hệ thống gây ra không có thao tác để bấm, nên
  không nối; ghi "mở trực tiếp frame".
* Sự kiện từ nơi khác ("Bước đổi ở nơi khác"), màn đích ngoài feature, màn chưa vẽ → không nối, ghi lý do.
* Dòng "Mở màn" là điểm vào của màn, không phải thao tác. Không nối, vì nối sẽ tạo vòng lặp (vd [1] tự
  chuyển sang [30], rồi [30] tự chuyển về [1]). Màn bắt đầu flow đã thay vai trò này.
* Một control dẫn tới nhiều đích tuỳ điều kiện (vd "Mở màn hình chi tiết" ra [33], [34] hoặc màn ngoài
  feature): một control chỉ giữ được một liên kết click, nên không nối, ghi vào báo cáo kèm danh sách đích.
* Đường quay lại ("Đóng", "Thử lại") nối thẳng tới frame đích ghi trong Mục 3.5, không dùng `BACK`, để
  chạy đúng dù vào từ đâu.

**Flow đặt tên theo use case:**
* Mỗi use case có màn thì có một flow (`figma.setFlowStartingPoints`). Tên flow là
  `UC-<slug> · <tên use case>`: slug lấy ở `usecases/{feature}-usecase-index.md`, tên lấy ở dòng tiêu đề
  `# Use Case: …` của `uc-<slug>.md`. Ví dụ `UC-tra-cuu-quy-trinh · Tra cứu quy trình trên danh sách`.
* Màn bắt đầu flow là màn đầu tiên của use case: theo cột Đường đi của userflow Mục 3.6 nếu có, không có
  thì lấy màn đầu tiên ở cột Screens của index.
* Màn đó đã là điểm bắt đầu của flow khác (Figma cho mỗi frame một flow) → lấy màn kế tiếp có vẽ trên
  đường đi của use case, ghi trong báo cáo.
* Use case có màn ở cả web và app → mỗi thiết bị một flow, thêm hậu tố ` (Web)` / ` (App)`.
* Không dùng `fromUserflow` vì cách đó đặt tên flow theo userflow, không theo use case. Chưa có use case
  → đặt tên theo cột "Tên flow" của userflow Mục 3, ghi trong báo cáo "chưa có use case".

**Flow của sơ đồ userflow:** flow bắt đầu ở một frame sơ đồ userflow (do `linkScreens` của
`/figma-userflow`) mang tên `Userflow · <tiêu đề sơ đồ>`, bỏ chữ "Userflow ·" bị lặp nếu tiêu đề đã có.
Gặp tên mặc định `Flow N` thì đổi bằng `figma.renameFlow`. Sơ đồ userflow có `linkScreens` mà chưa có
flow thì thêm.

**Không ghi đè tay:** control đã có liên kết mà khác Mục 3.5 thì hỏi user trước khi thay. Liên kết
designer nối tay là dữ liệu, như Bước 5.

**Kiểm:** `figma.getFlowStartingPoints` đọc lại tên flow và màn bắt đầu; không còn flow tên `Flow N`. Đếm số dòng Mục 3.5 đã nối trên
tổng số, tách theo lý do bỏ qua.

## Bước 5 — sửa màn đã có

Màn cùng `screenId`/tên đã tồn tại → **sửa tại chỗ**, không vẽ bản thứ hai. Quy trình:
`figma_read read_selection` hoặc `get_design_context` → **`figma_read a11y_audit` màn hiện tại làm
baseline** (số lỗi + danh sách ngoại lệ đã biết theo *Accessibility* của `design.md`) →
`modify` / `setInstanceProperties` → `layout_audit` → **`figma_read a11y_audit` lại sau khi sửa,
so với baseline**: chỉ báo lỗi **MỚI phát sinh** do lần sửa này, không báo lại các ngoại lệ đã chấp
nhận từ trước. Trước khi sửa, hỏi user có chỉnh tay gì trên màn đó không. Chỉnh tay của designer
là dữ liệu, không phải lỗi cần ghi đè.

## Bước 6 — tự kiểm trước khi trình

Kiểm bằng dữ liệu. Ảnh chụp chỉ để người xem, chụp **một lần** ở cuối. Hai lớp theo
`.claude/rules/ui-review.md`: máy đo trước, reviewer chấm sau; mỗi luật đúng một chủ.

**Lớp 1 — audit máy** (FAIL sửa hết trước khi sang lớp 2)

1. **A1** · `figma_read layout_audit` từng artboard: tràn, bị cắt, chữ bị cắt ba chấm. Sửa hết lỗi chặn.
2. **A2** · `figma_read a11y_audit`: tương phản, vùng chạm, control thiếu tên. Các ngoại lệ đã được chấp
   nhận trong *Accessibility* của `design.md` thì **không** tính là lỗi, nhưng liệt kê là "đã biết".
3. **A2** · Gọi skill `accessibility-review` (WCAG 2.1 AA) làm lớp kiểm thứ hai ngay sau `a11y_audit`, trước
   khi báo cáo: bắt thêm lỗi mà audit số liệu của Kit chưa phủ (thứ tự focus, semantic HTML/ARIA,
   khả năng dùng bằng screen reader). Ghi kết quả gộp cùng mục "đã biết" của bước 2, không tách báo cáo riêng.
4. **A3** · `figma.auditDesignSystem(artboardId)`: mục tiêu `compliance` = 1.00. Mỗi giá trị `hardcoded`
   thì gắn lại token. Giá trị `off-system` thì hoặc đổi sang giá trị có token, hoặc ghi vào báo cáo.
5. **A4** · Tự rà **Do's and Don'ts** của `design.md` cho từng màn, tối thiểu:
   - (a) mỗi nhóm hành động đúng **1 nút Primary**;
   - (b) trạng thái có **chữ/icon**, không chỉ màu;
   - (c) có đủ **rỗng / đang tải / lỗi** cho mọi vùng dữ liệu (hoặc user đã bỏ, gồm chế độ Nhanh);
   - (d) form **không trải hết bề rộng** desktop;
   - (e) mỗi component đã dùng không vi phạm dòng **Không nên** nào của nó trong `design/components.md`;
   - (f) **phủ bảng 5 cột**: đếm row có element tương ứng trên màn (theo tên layer, mục 7 Bước 4) —
     phải N/N; thiếu thì vẽ bổ sung hoặc ghi lý do;
   - (f2) **phủ CMP đã gọi**: mỗi row `Xem CMP-xx` → mở bảng 5 cột của CMP đó trong
     `design/ui-common/screen-patterns.md`, liệt kê row có tương tác/trạng thái (Click → tooltip, popover,
     panel, đang tải/lỗi…) mà dữ liệu mẫu của màn có chỗ áp (vd chip "Điều kiện x/y" có trên sơ đồ → tooltip).
     Row đó không có trong bảng feature và không có artboard → báo "CMP có, bảng 5 cột thiếu" trong mục
     "Đề xuất đổi so với bảng 5 cột" (KHÔNG im lặng vì bảng không ghi). Bảng chỉ ghi `Xem CMP-xx` không có
     nghĩa là đã phủ hết hành vi của CMP (sự cố 13/10/2026: tooltip chip Điều kiện CMP-09 #4 lọt khỏi
     wireframe lẫn Figma);
   - (g) **bố cục canvas**: `figma_read get_page_model` trên Section: state cách 100, nhóm cách 400,
     mỗi nhóm có title (kèm tên Việt), mọi frame bắt đầu `<screenId> · <slug>` (chính 3 phần, state/modal
     4 phần với tên tiếng Anh), không còn
     `Frame N`, không có dấu cách đầu tên frame (`design/setup-figma.md` › *Bố cục trong Section con*).
6. **A4** · **Chip trạng thái:** mọi chip là instance `Chip trạng thái` (không tự vẽ pill); icon và chữ đúng màu
   `Status Chip/<Sắc>/Foreground` (đổi icon qua thuộc tính `Icon` xong phải gắn lại màu nét); mã nghiệp vụ
   dùng `Text/Code Small`; chip không đè tên/mã. Màn có trạng thái nghiệp vụ → chạy
   `python3 _scripts/status-chip-lint.py docs/{feature}/srs/{feature}-states.md`; FAIL thì báo trong báo
   cáo, KHÔNG tự đổi nhãn nghiệp vụ (nhãn lấy nguyên văn từ states.md).
7. **A5** · **Luật thị giác đo được:** mỗi artboard chính → `figma_read get_design_context`
   `{nodeId, depth: 20, detail: "full"}`, lưu JSON vào scratchpad → `python3 _scripts/visual-audit.py
   <file.json> [...]`. `FAIL` (chữ < 12px trên mobile) → sửa. `WARN` không tự sửa — giữ nguyên văn để
   truyền cho reviewer ở lớp 2 (luật thị giác có ngoại lệ hợp lý; reviewer quyết giữ hay chấp nhận).
   Tỷ lệ nhận diện < 80% → đọc lại vùng con và chạy lại với `--part <vùng.json>`; vẫn thấp → ghi rõ
   trong báo cáo, không in PASS.
8. Một `figma_read screenshot` cho mỗi màn chính ở cuối, để user xem.

**Lớp 2 — reviewer** (gọi song song trong 1 lượt Task, chỉ đọc, chỉ trả finding). Sửa theo finding
xong → chỉ gọi lại agent có `BLOCKING`, cho màn đã sửa (tối đa 2 vòng); vẫn còn → ghi vào báo cáo.
Cần đổi nghiệp vụ → ghi "cần `/cr`", không tự sửa.

9. **Khớp đặc tả (agent):** có bảng 5 cột → gọi `@uxui-reviewer` (Task) với bảng
   `screenId · slug · nodeId` + đường dẫn file wireframe đã dùng làm nguồn (HTML: file flow + "Screen N"
   của từng màn; ASCII: file flow + `## Screen: {slug}`) của các màn vừa vẽ/sửa. Không có bảng 5 cột →
   `Khớp đặc tả: SKIPPED — không có bảng 5 cột`, không in PASS.
10. **Usability (AI):** vẽ xong **trọn một flow** (đủ màn của flow đó theo `userflow.md` Mục 3) và
   `userflow.md` có **Mục 3.6 Tác vụ chính** chạm flow này → gọi `@usability-reviewer` (Task) với
   userflow + bảng `screenId · slug · nodeId` của flow (kèm artboard trạng thái) + các WARN `H1/H2/M1/M2`
   của A5. Agent đi từng tác vụ theo cognitive walkthrough + rà heuristic Nielsen. Chưa trọn flow (chế độ
   Nhanh, vài màn lẻ) hoặc thiếu Mục 3.6 → KHÔNG gọi, ghi rõ lý do ở báo cáo
   (`Usability (AI): SKIPPED — …`), không in PASS.
11. **Thị giác (agent):** gọi `@visual-reviewer` (Task) với bảng `screenId · slug · nodeId` + báo cáo A5
   của từng artboard. Agent chấm thứ tự mắt đọc, phân cấp màu, 60/30/10, nhóm và nhịp, dễ đọc, vị trí
   nút; quyết giữ/chấp nhận từng WARN A5. Luôn gọi khi lớp 1 không còn FAIL.

## Bước 7 — báo đã vẽ gì

Ngắn, theo mẫu:

```
Đã vẽ: "02 · Đơn hàng" › F01 · Duyệt đơn › Web (file <tên>):
2.1 · web · order-list     P1 · default / Empty / Loading
2.2 · web · order-detail   P7 · default / Load error

Máy đã kiểm: layout 0 lỗi · a11y 0 lỗi mới (2 ngoại lệ đã biết) · DS compliance 1.00 · A5 thị giác 0 FAIL / 3 WARN (nhận diện 92%)
Bảng 5 cột (nguồn: HTML | ASCII): 2.1 · web 12/12, 2.2 · web 9/9 row có trên màn | không có bảng 5 cột — vẽ từ SRS
Đề xuất đổi so với bảng 5 cột: <liệt kê, hoặc "không">
Object map: <n chỗ lệch bảng 5 cột (đã ghi ở Đề xuất đổi) · thẻ dùng chung: … | không có object map>
Khớp đặc tả (@uxui-reviewer): 0 blocking / 1 warning | SKIPPED — <lý do>
Usability (AI, chưa có người dùng thật): 3 tác vụ · 1 vượt tiêu chí bước · 0 blocking / 2 warning | SKIPPED — <lý do>
Thị giác (@visual-reviewer): 0 blocking / 2 warning · A5 đã xét 3 (giữ 1, chấp nhận 2) | SKIPPED — <lý do>
Prototype: 24/31 chuyển màn đã nối · 5 hệ thống tự chuyển (lỗi — mở trực tiếp frame) · 2 ngoài feature · flow: UC-xem-quy-trinh-cua-ban-ghi · Xem quy trình của một bản ghi (Web), … | SKIPPED — <lý do>
Máy KHÔNG kiểm: <xem dưới, kèm mức ưu tiên [Cao]/[Trung]/[Thấp]>
Chưa có chuẩn trong design.md: <liệt kê chỗ vẽ tạm, hoặc "không">
Chế độ: <Nhanh — không vẽ trạng thái phụ | Đầy đủ>
Link Figma: đã ghi {n} màn vào {feature}-wireframe-html-index.md / {feature}-wireframe-index.md | qua /figma-sync | Chưa ghi: <lý do>
Đồng bộ tài liệu (/figma-sync): <tóm tắt báo cáo của figma-sync> | Chưa sync tài liệu — <lý do>
Task chốt: BL-NNN Chốt giao diện Figma {feature} · {flow} | đã có | chưa trọn flow
```

**Ghi link về repo.** Link màn: `[{screenId}](https://www.figma.com/design/{fileKey}/?node-id={nodeId,
":" đổi thành "-"})`. `fileKey`: plugin không trả → lấy từ link node trong
`design/ui-common/screen-patterns.md` (dòng **Figma** của CMP), đối chiếu tên file với `figma_status`;
lệch hoặc không có → hỏi user link. Ghi vào **mọi wireframe index đang có** của feature (gộp 1 L2 diff):

* `html-wireframe/{feature}-wireframe-html-index.md` — bảng Flows, 1 dòng/flow: điền cột `Figma` của
  dòng flow chứa màn, dạng danh sách `[1.1 · web](…) · [1.2 · web](…)` theo thứ tự màn; màn đã có link thì thay
  link cũ, giữ link của màn khác. Index cũ chưa có cột `Figma` → thêm cột trước `Status` trong cùng
  L2 diff. Cập nhật cột `Updated` của dòng đó.
* `ascii-wireframe/{feature}-wireframe-index.md` — bảng Screens, 1 dòng/màn: điền cột `Figma` (khớp
  dòng theo `Slug` — `screenId` ra `Slug` qua userflow Mục 2) + cột `Updated`.

Chỉ sửa đúng cột `Figma` + `Updated`, qua **L2 diff** (`approval-gate.md`). Chưa có index nào (chưa
chạy `/wireframe-html` hay `/wireframe-ascii`) → không tạo mới, ghi 1 dòng "Chưa ghi link: chưa có
wireframe index" trong báo cáo.

Flow đã có `screens/{flow}.md` → không ghi link ở đây; `/figma-sync` (dưới) ghi link vào dòng **Figma** của
từng màn + cột `Figma` của `screens/{feature}-screen-index.md`.

**Đồng bộ ngược về tài liệu — luôn chạy sau khi vẽ hoặc sửa** (`.claude/rules/screen-source.md` Mục 5):
gọi `/figma-sync {feature} --flow {flow}` **inline** (đọc `.claude/skills/figma-sync/SKILL.md`, chạy với
L1/L2 của nó). Lần đầu của flow: chuyển bảng 5 cột sang `screens/{flow}.md`, xoá wireframe flow đó, chụp
mốc. Lần sau: những gì đã vẽ khác bảng (mục "Đề xuất đổi so với bảng 5 cột") và chỉnh tay của designer
(Bước 5) thành đề xuất sửa `screens/` + userflow thay vì chỉ nằm trong báo cáo chat. User từ chối → ghi
"Chưa sync tài liệu" trong báo cáo, không ghi mốc.

**Task chốt:** vẽ xong trọn một flow mà backlog chưa có task cùng flow → thêm (báo 1 dòng, `backlog.md`):
`Chốt giao diện Figma {feature} · {flow}` · Xong khi
`grep:docs/{feature}/screens/{feature}-screen-index.md:\({flow}\.md\).*approved`. User đóng task
này (đổi ✅) hoặc nói "done" → `/figma-sync {feature} --done --flow {flow}`.

## Những gì máy KHÔNG kiểm

Nói rõ với user, đừng gộp vào một chữ "PASS". Mỗi mục kèm mức ưu tiên (cao/trung/thấp) để BA/dev
biết xử lý cái nào trước — mức chỉ là gợi ý chung, tuỳ nghiệp vụ cụ thể mà đổi:

* **[Cao] Màn có khớp nghiệp vụ không.** Audit sạch nghĩa là vẽ đúng kỹ thuật và đúng hệ thống, chứ chưa
  nói gì về việc cột "Tổng tiền" có nên nằm đó hay không. `@uxui-reviewer` đối chiếu với
  bảng 5 cột (mục 9 Bước 6), nhưng đó là AI đọc, chỉ bắt được cái bảng có ghi — bảng sai thì màn sai theo.
* **[Cao] Có thiếu màn/nhánh không.** Chỉ userflow mới lộ ra điều này. Không có flow thì nói thẳng là
  chưa kiểm được.
* **[Trung] Nhãn và dữ liệu mẫu có đúng không.** "Duyệt trong 24 giờ" là một khẳng định về hệ thống; nếu
  spec ghi 48 giờ thì màn đang nói sai.
* **[Thấp] Thẩm mỹ**: `@visual-reviewer` chấm thứ bậc thị giác (mục 11 Bước 6) bằng AI đọc ảnh + số
  liệu A5; gu thẩm mỹ vẫn là việc của designer khi xem ảnh chụp.

## Chế độ chạy (`/run-task`)

Chỉ khi đủ điều kiện chế độ chạy của `approval-gate.md` (worktree `feat/<feature>` + run card đã duyệt).
Thiếu 1 điều kiện → chạy như bình thường, hỏi user.

| Chỗ thường hỏi user | Trong chế độ chạy |
|---|---|
| 2.1 Màn nào, Nhanh/Đầy đủ · 2.4 chia đợt | Lấy từ run card (bước figma-screen + Mục 2). Card không ghi → Cửa 2 |
| 2.2 Thiết bị | Card Mục 2 → `primary_device` trong `srs/{feature}-userflow.md`. Không có → Cửa 2 (HARD GATE vẫn giữ: không đoán) |
| 2.3 Vẽ userflow trước? | Không hỏi; ghi vào card Mục 9 "điểm cần soi" nếu trang chưa có flow |
| 2.3 Bố cục A/B/C | Soạn đủ 3 phương án như thường → gọi `@uxui-reviewer` chọn 1, đối chiếu với bản phác theo thứ tự nguồn của `.claude/rules/screen-source.md` Mục 2 (flow đã lên Figma: `screens/{flow}.md`; chưa: `html-wireframe/{flow}.html` rồi `ascii-wireframe/{flow}.md`) + userflow (Mục 2 vùng/màn, Mục 3.6 tác vụ làm nhiều nhất phải nổi nhất). Ghi vào card Mục 9: phương án chọn, lý do, vì sao bỏ 2 phương án kia. Không có bản phác nào → vẫn chọn theo userflow, ghi "chọn khi chưa có bản phác" |
| 2.5 L1 `Y` | Run card thay; in tóm tắt kế hoạch vào Nhật ký card |
| Finding reviewer đổi giao diện đã duyệt | KHÔNG tự sửa (memory keep-approved-look) → câu hỏi ở card Mục 6, Cửa 2 |

Thêm 3 luật riêng của chế độ chạy:

* **Khoá Figma** — plugin chỉ 1 kết nối. Trước Bước 3: `_scripts/figma-lock.sh acquire <feature>`; đã có
  người giữ → Cửa 2 "Figma đang bận ({ai}, từ {lúc})". Xong hoặc dừng (kể cả lỗi) → `figma-lock.sh release <feature>`.
  `figma_status` báo chưa kết nối → release + Cửa 2 "mở Figma desktop + plugin".
* **Chỉ vẽ trên trang nháp `_run/<feature>`** (tạo nếu chưa có). Figma không nằm trong git — `wt.sh drop`
  không hoàn tác được, nên trang chính chỉ đổi sau khi user duyệt land (`/queue` chuyển frame sang trang chính).
* Bước 6 (tự kiểm) + reviewer chạy đủ như thường; kết quả 4 mức ghi vào card, không chờ user đọc.

## Constraints

### Luật cứng: không được vi phạm

* **Không vẽ khi user chưa chọn bố cục.** Luôn trình 3 phương án (A theo mẫu có sẵn + B, C độc lập)
  và chờ user chọn. Ngoại lệ duy nhất: **Chế độ chạy** (mục dưới) — `@uxui-reviewer` chọn thay, ghi lý do,
  user chọn lại ở Cửa 3. Phương án độc lập chỉ độc lập về khung trang: không tự đặt token, không vẽ lại
  control ngoài thư viện.
* **Không bịa giá trị ở Known Gaps.** Đụng chỗ `design.md` chưa có chuẩn (ví dụ mobile) thì hỏi,
  hoặc vẽ tạm và ghi rõ "chưa có chuẩn trong design.md" trong báo cáo và trong mô tả artboard.
* **Không mã màu, cỡ chữ, khoảng cách cứng** khi đã có token. Không tự vẽ lại một control mà thư
  viện đã có component.
* **Không vẽ lên trang component của thư viện**, và không sửa component chính (main component).
* **Không bịa nội dung nghiệp vụ**: nhãn trạng thái, tên trường, quy tắc phải lấy từ nguồn. Nguồn
  thiếu thì hỏi.
* **Không bỏ row hay đổi wording của bảng 5 cột im lặng.** Muốn khác thì vẽ theo bảng + ghi đề xuất.
* **Chỉ ghi repo ở cột `Figma` + `Updated` của wireframe index** (`{feature}-wireframe-html-index.md`
  và/hoặc `{feature}-wireframe-index.md`), qua L2. Không tự sửa SRS, userflow, file wireframe HTML/ASCII
  hay bảng 5 cột — mọi sửa tài liệu theo Figma đi qua `/figma-sync` (gọi inline ở Bước 7, có L1/L2 riêng).
* **Không lặng lẽ bỏ màn/trạng thái** user đã yêu cầu. Không vẽ được thì nói màn nào và vì sao.
* **Thiết bị luôn hỏi user**. `design.md` chỉ đề xuất.

### Tuân thủ rule workspace

Skill này là một "skill vẽ màn" theo nghĩa của rule `design-system.md` (thư mục `.claude/rules/`
của workspace): đọc `design/design.md` theo mục (mục lục + mục luôn đọc + mục của `/figma-screen` trong bảng của rule),
tuân theo năm *Luật khi sinh màn*, và dùng
Do's and Don'ts làm tiêu chí tự kiểm trước khi trình.

## References

- `../reqwise-diagram-rules.md` § 5: cổng kết nối Figma.
- Rule workspace `.claude/rules/design-system.md`: design system là nguồn chung cho mọi skill vẽ màn.
- Rule workspace `.claude/rules/ui-review.md`: chia việc audit máy (A1–A5) và 3 reviewer, ngưỡng A5.
- `design/design.md`: token, mẫu bố cục, component, trạng thái, định dạng nội dung, Known Gaps.
- `design/components.md`: chọn component theo nhu cầu, cùng Usage, Nên/Không nên và Examples của từng component (dịch từ Astryx, chia theo section).
- `design/design-tokens.css`: cùng bộ token, dạng CSS (cho prototype/code, không dùng khi vẽ Figma).
- `design/setup-figma.md`: setup file Figma cho dự án mới (Cách A thư viện / Cách B bản sao) và bảng kiểm tra setup.
- `docs/_shared/object-map.md` + `docs/{feature}/{feature}-object-map.md` (output `/object-map`): thuộc tính theo mức hiển thị, hành động theo vai trò, thẻ dùng chung — nguồn phụ Bước 1.3.
- `design/figma-library-keys.json`: key component set để nạp từ thư viện đã publish (Cách A). Máy sinh, không sửa tay.
- `.claude/rules/screen-source.md` + skill `/figma-sync`: bảng 5 cột sau Figma (`screens/`), mốc, đồng bộ ngược, chốt flow vào SRS.
- `figma_docs(section="api" | "recipes" | "rules" | "userflow")`: cú pháp công cụ.
