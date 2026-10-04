---
name: figma-screen
description: Vẽ màn hình giao diện (UI) lên Figma theo đúng design system của dự án — đề xuất 3 phương án bố cục (1 theo mẫu có sẵn trong design/design.md + 2 độc lập) để user chọn, dùng component thật (instance), gắn token theo tên, vẽ đủ trạng thái rỗng/đang tải/lỗi, rồi tự kiểm trước khi trình. Dùng khi ai đó nói "vẽ màn", "dựng màn hình", "vẽ UI", "mock up màn", "làm giao diện cho <tính năng>" trên Figma.
allowed-tools: Read, Glob, Grep, Edit, Task, AskUserQuestion, mcp__reqwise-figma__figma_status, mcp__reqwise-figma__figma_docs, mcp__reqwise-figma__figma_read, mcp__reqwise-figma__figma_rules, mcp__reqwise-figma__figma_write
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
     (Mục 2, 3, 3.5) và tác vụ chính (Mục 3.6). `screenId` = cột `[#]` Mục 2 + hậu tố thiết bị
     (`[#]` = 3, Desktop → `3-web`).
   * **`ascii-wireframe/{flow-slug}.md`** + `{feature}-wireframe-index.md` — bố cục ASCII và
     **bảng mô tả 5 cột** của từng màn. Bảng 5 cột là **hợp đồng BA ↔ design**: element nào, control
     gì, validation, trạng thái, wording, mã lỗi, điều hướng. Đọc hết bảng của mọi màn sẽ vẽ.
   * `srs/{feature}-spec.md` (FR/BR/Error Matrix), `srs/{feature}-states.md`, `usecases/uc-*.md`,
     file user tag bằng `@`.
   Có nguồn thì **dẫn xuất từ nguồn**, chỉ hỏi phần nguồn bỏ trống. Thiếu ASCII cho màn sẽ vẽ →
   báo 1 dòng và hỏi: chạy `/wireframe-ascii` trước (đề xuất), hay vẽ thẳng từ SRS (ghi
   "không có bảng 5 cột" trong báo cáo).
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
* Thiết bị đã chốt → cố định `frameW`/`frameH` cho mọi artboard, không dùng số của thiết bị khác.
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
Luồng 1 — Duyệt đơn: 2.1-web danh-sach-don → 2.2-web chi-tiet-don
2.1-web · danh-sach-don   Mẫu P1 · S1 Shell · Side Nav · nút chính [Tạo đơn]
2.2-web · chi-tiet-don    Mẫu P7 · nút chính [Duyệt]
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
Luồng 1 — Duyệt đơn (hàng 1):
  2.1-web · danh-sach-don (có dữ liệu) → · rỗng → · đang tải
  2.2-web · chi-tiet-don (bình thường) → · lỗi tải
Lỗi đại diện: 2.2-web banner lỗi tải; ghi chú liệt kê các lỗi còn lại cùng kiểu banner
Trạng thái nghiệp vụ → nhóm: Nháp→Neutral · Chờ duyệt→Warning · Đã duyệt→Success · Từ chối→Error
Khung: Desktop 1920×1080
Nơi vẽ: trang "02 · Đơn hàng" › F01 · Duyệt đơn › Web
Token/component: design/design.md (Astryx), instance thư viện
Chưa có chuẩn: (không)
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

1. **Artboard**: kích thước theo thiết bị đã chốt. Tên chứa `screenId` **kèm hậu tố thiết bị** như
   một token nguyên vẹn, ví dụ `"3.1-web · danh-sach-chuyen"`, để userflow nối được (`linkScreens`).
   Desktop, Tablet, Responsive dùng `-web`; Mobile 375 dùng `-mob`. `screenId` trong userflow phải
   ghi đủ hậu tố (`3.1-web`), vì ghi `3.1` sẽ khớp nhầm cả `3.1-mob` lẫn `3.10-web`.
   Nền dùng token nền trang của `design.md`. Các trạng thái của cùng màn đặt **cạnh nhau trên một hàng**, tên có hậu tố
   `· rỗng`, `· đang tải`, `· lỗi`.
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

## Bước 5 — sửa màn đã có

Màn cùng `screenId`/tên đã tồn tại → **sửa tại chỗ**, không vẽ bản thứ hai. Quy trình:
`figma_read read_selection` hoặc `get_design_context` → **`figma_read a11y_audit` màn hiện tại làm
baseline** (số lỗi + danh sách ngoại lệ đã biết theo *Accessibility* của `design.md`) →
`modify` / `setInstanceProperties` → `layout_audit` → **`figma_read a11y_audit` lại sau khi sửa,
so với baseline**: chỉ báo lỗi **MỚI phát sinh** do lần sửa này, không báo lại các ngoại lệ đã chấp
nhận từ trước. Trước khi sửa, hỏi user có chỉnh tay gì trên màn đó không. Chỉnh tay của designer
là dữ liệu, không phải lỗi cần ghi đè.

## Bước 6 — tự kiểm trước khi trình

Kiểm bằng dữ liệu. Ảnh chụp chỉ để người xem, chụp **một lần** ở cuối.

1. `figma_read layout_audit` từng artboard: tràn, bị cắt, chữ bị cắt ba chấm. Sửa hết lỗi chặn.
2. `figma_read a11y_audit`: tương phản, vùng chạm, control thiếu tên. Các ngoại lệ đã được chấp
   nhận trong *Accessibility* của `design.md` thì **không** tính là lỗi, nhưng liệt kê là "đã biết".
3. Gọi skill `accessibility-review` (WCAG 2.1 AA) làm lớp kiểm thứ hai ngay sau `a11y_audit`, trước
   khi báo cáo: bắt thêm lỗi mà audit số liệu của Kit chưa phủ (thứ tự focus, semantic HTML/ARIA,
   khả năng dùng bằng screen reader). Ghi kết quả gộp cùng mục "đã biết" của bước 2, không tách báo cáo riêng.
4. `figma.auditDesignSystem(artboardId)`: mục tiêu `compliance` = 1.00. Mỗi giá trị `hardcoded`
   thì gắn lại token. Giá trị `off-system` thì hoặc đổi sang giá trị có token, hoặc ghi vào báo cáo.
5. Tự rà **Do's and Don'ts** của `design.md` cho từng màn, tối thiểu:
   - (a) mỗi nhóm hành động đúng **1 nút Primary**;
   - (b) trạng thái có **chữ/icon**, không chỉ màu;
   - (c) có đủ **rỗng / đang tải / lỗi** cho mọi vùng dữ liệu (hoặc user đã bỏ, gồm chế độ Nhanh);
   - (d) form **không trải hết bề rộng** desktop;
   - (e) mỗi component đã dùng không vi phạm dòng **Không nên** nào của nó trong `design/components.md`;
   - (f) **phủ bảng 5 cột**: đếm row có element tương ứng trên màn (theo tên layer, mục 7 Bước 4) —
     phải N/N; thiếu thì vẽ bổ sung hoặc ghi lý do.
6. Một `figma_read screenshot` cho mỗi màn chính ở cuối, để user xem.
7. **Usability (AI):** vẽ xong **trọn một flow** (đủ màn của flow đó theo `userflow.md` Mục 3) và
   `userflow.md` có **Mục 3.6 Tác vụ chính** chạm flow này → gọi `@usability-reviewer` (Task) với
   userflow + bảng `screenId · slug · nodeId` của flow (kèm artboard trạng thái). Agent đi từng tác
   vụ theo cognitive walkthrough + rà heuristic Nielsen, chỉ trả finding, không tự sửa. `BLOCKING`
   không đổi nghiệp vụ → sửa màn rồi gọi lại (tối đa 2 vòng); cần đổi nghiệp vụ → ghi "cần `/cr`",
   không tự sửa. Chưa trọn flow (chế độ Nhanh, vài màn lẻ) hoặc thiếu Mục 3.6 → KHÔNG gọi, ghi rõ
   lý do ở báo cáo (`Usability (AI): SKIPPED — …`), không in PASS.
8. **Khớp đặc tả (agent):** có bảng 5 cột → gọi `@uxui-reviewer` (Task) với bảng
   `screenId · slug · nodeId` + đường dẫn file ASCII của các màn vừa vẽ/sửa. `BLOCKING` → sửa màn rồi
   gọi lại (tối đa 2 vòng); vẫn còn → ghi vào báo cáo. Không có bảng 5 cột → `Khớp đặc tả: SKIPPED —
   không có bảng 5 cột`, không in PASS. Chạy trước mục 7 nếu cả hai cùng chạy (sửa đặc tả trước, rồi
   mới đi tác vụ).

## Bước 7 — báo đã vẽ gì

Ngắn, theo mẫu:

```
Đã vẽ: "02 · Đơn hàng" › F01 · Duyệt đơn › Web (file <tên>):
2.1-web · danh-sach-don   P1 · có dữ liệu / rỗng / đang tải
2.2-web · chi-tiet-don    P7 · bình thường / lỗi tải

Máy đã kiểm: layout 0 lỗi · a11y 0 lỗi mới (2 ngoại lệ đã biết) · DS compliance 1.00
Bảng 5 cột: 2.1-web 12/12 · 2.2-web 9/9 row có trên màn | không có bảng 5 cột — vẽ từ SRS
Đề xuất đổi so với bảng 5 cột: <liệt kê, hoặc "không">
Khớp đặc tả (@uxui-reviewer): 0 blocking / 1 warning | SKIPPED — <lý do>
Usability (AI, chưa có người dùng thật): 3 tác vụ · 1 vượt tiêu chí bước · 0 blocking / 2 warning | SKIPPED — <lý do>
Máy KHÔNG kiểm: <xem dưới, kèm mức ưu tiên [Cao]/[Trung]/[Thấp]>
Chưa có chuẩn trong design.md: <liệt kê chỗ vẽ tạm, hoặc "không">
Chế độ: <Nhanh — không vẽ trạng thái phụ | Đầy đủ>
Link Figma: đã ghi {n} màn vào {feature}-wireframe-index.md | Chưa ghi: <lý do>
```

**Ghi link về repo.** Có `docs/{feature}/ascii-wireframe/{feature}-wireframe-index.md` → điền cột
`Figma` của từng màn vừa vẽ/sửa (khớp dòng theo `Slug` — `screenId` ra `Slug` qua userflow Mục 2):
`[{screenId}](https://www.figma.com/design/{fileKey}/?node-id={nodeId, ":" đổi thành "-"})`, cập nhật
cột `Updated`. `fileKey`: plugin không trả → lấy từ link node trong `design/ui-common/screen-patterns.md`
(dòng **Figma** của CMP), đối chiếu tên file với `figma_status`; lệch hoặc không có → hỏi user link.
Chỉ sửa đúng 2 cột đó, qua **L2 diff** (`approval-gate.md`). Chưa có index (chưa chạy
`/wireframe-ascii`) → không tạo mới, ghi 1 dòng "Chưa ghi link: chưa có wireframe-index" trong báo cáo.

## Những gì máy KHÔNG kiểm

Nói rõ với user, đừng gộp vào một chữ "PASS". Mỗi mục kèm mức ưu tiên (cao/trung/thấp) để BA/dev
biết xử lý cái nào trước — mức chỉ là gợi ý chung, tuỳ nghiệp vụ cụ thể mà đổi:

* **[Cao] Màn có khớp nghiệp vụ không.** Audit sạch nghĩa là vẽ đúng kỹ thuật và đúng hệ thống, chứ chưa
  nói gì về việc cột "Tổng tiền" có nên nằm đó hay không. `@uxui-reviewer` đối chiếu với
  bảng 5 cột (mục 8 Bước 6), nhưng đó là AI đọc, chỉ bắt được cái bảng có ghi — bảng sai thì màn sai theo.
* **[Cao] Có thiếu màn/nhánh không.** Chỉ userflow mới lộ ra điều này. Không có flow thì nói thẳng là
  chưa kiểm được.
* **[Trung] Nhãn và dữ liệu mẫu có đúng không.** "Duyệt trong 24 giờ" là một khẳng định về hệ thống; nếu
  spec ghi 48 giờ thì màn đang nói sai.
* **[Thấp] Thẩm mỹ và thứ bậc thị giác**: đó là việc của designer khi xem ảnh chụp.

## Constraints

### Luật cứng: không được vi phạm

* **Không vẽ khi user chưa chọn bố cục.** Luôn trình 3 phương án (A theo mẫu có sẵn + B, C độc lập)
  và chờ user chọn. Phương án độc lập chỉ độc lập về khung trang: không tự đặt token, không vẽ lại
  control ngoài thư viện.
* **Không bịa giá trị ở Known Gaps.** Đụng chỗ `design.md` chưa có chuẩn (ví dụ mobile) thì hỏi,
  hoặc vẽ tạm và ghi rõ "chưa có chuẩn trong design.md" trong báo cáo và trong mô tả artboard.
* **Không mã màu, cỡ chữ, khoảng cách cứng** khi đã có token. Không tự vẽ lại một control mà thư
  viện đã có component.
* **Không vẽ lên trang component của thư viện**, và không sửa component chính (main component).
* **Không bịa nội dung nghiệp vụ**: nhãn trạng thái, tên trường, quy tắc phải lấy từ nguồn. Nguồn
  thiếu thì hỏi.
* **Không bỏ row hay đổi wording của bảng 5 cột im lặng.** Muốn khác thì vẽ theo bảng + ghi đề xuất.
* **Chỉ ghi repo ở đúng 1 chỗ**: cột `Figma` + `Updated` của `{feature}-wireframe-index.md`, qua L2.
  Không sửa SRS, userflow, ASCII hay bảng 5 cột — muốn đổi thì đề xuất, user chạy skill tương ứng.
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
- `design/design.md`: token, mẫu bố cục, component, trạng thái, định dạng nội dung, Known Gaps.
- `design/components.md`: chọn component theo nhu cầu, cùng Usage, Nên/Không nên và Examples của từng component (dịch từ Astryx, chia theo section).
- `design/design-tokens.css`: cùng bộ token, dạng CSS (cho prototype/code, không dùng khi vẽ Figma).
- `design/setup-figma.md`: setup file Figma cho dự án mới (Cách A thư viện / Cách B bản sao) và bảng kiểm tra setup.
- `design/figma-library-keys.json`: key component set để nạp từ thư viện đã publish (Cách A). Máy sinh, không sửa tay.
- `figma_docs(section="api" | "recipes" | "rules" | "userflow")`: cú pháp công cụ.
