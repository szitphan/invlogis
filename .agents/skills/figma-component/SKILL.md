---
name: figma-component
description: Tạo hoặc cập nhật MỘT component bất kỳ của dự án trên Figma (vd Notification Center, Bộ lọc nâng cao, Tuỳ chỉnh cột, thẻ KPI, dòng lịch sử…) — ghép từ instance thật của thư viện đang có, gắn token của dự án, có biến thể + thuộc tính dùng lại được, đủ trạng thái, Desktop/Mobile, kiểm chữ dài — theo spec trong design/design.md (DS cũ) hoặc design-system/ (DS v2 đang dựng lại; chạy được trong agent con ở chế độ đề xuất --propose). `--html` = component mới của DS v2 đi qua trang artifact trước (brainstorm từ Untitled, Astryx và ý tưởng cộng đồng → preview web/mobile → đối chiếu foundation) rồi mới lên Figma. Dùng khi ai đó nói "tạo component", "dựng component <tên>", "brainstorm component", "biến mẫu ghép này thành component", "thêm biến thể/trạng thái cho component", "làm lại component cho file mới". Không dùng để dựng cả design system (dùng /figma-design-system) hay vẽ màn (dùng /figma-screen).
allowed-tools: Read, Glob, Grep, Edit, Write, Bash, Skill, AskUserQuestion, Agent, WebSearch, WebFetch, Artifact, ArtifactData, mcp__reqwise-figma__figma_status, mcp__reqwise-figma__figma_docs, mcp__reqwise-figma__figma_read, mcp__reqwise-figma__figma_rules, mcp__reqwise-figma__figma_write, mcp__claude_ai_Figma__use_figma, mcp__claude_ai_Figma__get_figma_skill, mcp__claude_ai_Figma__get_libraries, mcp__claude_ai_Figma__search_design_system, mcp__claude_ai_Figma__get_metadata, mcp__claude_ai_Figma__download_assets
user-invocable: true
argument-hint: "<tên component> [link file Figma] [desktop|mobile|cả hai] [@spec/srs] [--html | --propose | --build <gói đã duyệt>] [--ds cu]"
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

**Bốn chế độ chạy** (chi tiết: *Chế độ `--html`* và *Chạy trong agent con*):

* **Mặc định** — phiên chính, hỏi user bằng `AskUserQuestion`, làm Bước 1–9.
* **`--html`** — component **mới** của DS v2: vòng 0–5 trên một trang artifact (brainstorm → preview → đối chiếu
  foundation), user chốt rồi mới dựng Figma, cuối cùng 3 agent review. Một component mỗi lần chạy.
* **`--propose`** — agent con (không hỏi được user): Bước 1–4 rồi trả **gói đề xuất**; không ghi repo, không ghi Figma.
* **`--build <gói đã duyệt>`** — dựng theo gói user đã duyệt: Bước 6–9, không hỏi lại.

## Mục tiêu

Một **họ component set** trong file Figma đích mà designer/dev lấy instance là dùng được:

* Ghép từ **instance thật** của thư viện (Button, Badge, Tabs, Popover…), không vẽ lại control. DS v2: thư viện là Base / Application
  của chính DS v2 (DEC-260).
* Mọi màu / khoảng cách / bo góc / chữ **gắn biến và style** của dự án.
* **API rõ**: biến thể (VARIANT) cho khác biệt về hình, thuộc tính TEXT / BOOLEAN / INSTANCE_SWAP cho
  nội dung, instance con được expose khi người dùng cần chỉnh.
* **Đủ trạng thái** theo § States của `design.md` (có dữ liệu / rỗng / đang tải / lỗi…), đủ nền tảng
  đã chốt (Desktop / Mobile), **kiểm chữ dài**.
* Một khung trình bày: master components + mọi trạng thái bằng instance + phần *Chữ dài · kiểm tra*. DS v2: khung tài
  liệu theo khuôn (Bước 6).

__Việc chính là thiết kế API và cấu trúc, không phải thao tác vẽ.__ Tách component con nào, trục biến
thể nào, cái gì là thuộc tính — quyết sai thì người dùng phải detach, và mọi instance đã dùng bị vỡ.

## Chọn nguồn spec — DS cũ hay DS v2

`design-system/architecture.md` tồn tại → **DS v2** (đang dựng lại song song với bộ cũ). Không có file đó, hoặc lời gọi ghi
`--ds cu` (sửa component bộ cũ, chỉ lỗi chặn) → **DS cũ**: bỏ qua mục này, skill chạy đúng như trước.

| Việc | DS cũ | DS v2 |
|---|---|---|
| Nguồn spec | `design/design.md` | `design-system/`: `architecture.md`, `foundations.md`, `tokens.json`, `components/{base,application}/*.md`; lý do từng quyết định ở `_workspace/decisions.md` (Grep theo mã DEC) |
| Ghi spec | mục trong `design.md` | một md mỗi component: `design-system/components/{base,application}/{slug}.md`; **không** ghi vào `design.md` (gộp lúc DS v2 chốt) |
| Nhóm, tên, trục | § Components - <dự án> | architecture Mục 4 (nhóm Base / Application, luật lồng), 5 (tên), 6 (web/mobile), 11 (luật component chung) |
| Token | biến/style theo tên (§ Tên trong Figma) | gắn Semantic (`1.`–`5.`), Brand theo vai, token Component của chính nó (`6.`, `8.`); token Component mới chỉ trỏ Semantic; không gắn Primitives, không số / mã trần (architecture Mục 7, foundations Mục 2, 12, DEC-313) |
| Phần ghép | thư viện (`figma-library-keys.json`) | component Base / Application đã có của DS v2; Astryx chỉ để tham chiếu (dưới) |
| Nơi đặt | hỏi user (Bước 5) | trang `DS · Base components` hoặc `DS · Application components`: Section của họ component (kèm 1 màn web + 1 màn app để duyệt, DEC-260 F12); không đè khung có sẵn, không đụng Section khác, nới Section của mình khi cần |
| Khung trình bày | khung chứa + "Trạng thái & ví dụ" (Bước 6) | khung tài liệu theo khuôn (đầu Bước 6) |
| Quy tắc chung chưa có bản v2 (States, Content & Formatting, Accessibility, Do's and Don'ts) | `design.md` | vẫn đọc mục đó ở `design.md`; lệch với `design-system/` thì v2 thắng |

**Xếp nhóm** theo architecture Mục 4: **Base** = component nguyên thuỷ theo Untitled, không nghiệp vụ, chữ giữ chỗ trung
tính; **Application** = khối ứng dụng ráp từ Base (điều hướng, bảng, upload) và khối nghiệp vụ logistics dùng lại ở nhiều màn.
Ghi nhóm ở dòng meta đầu md.

* **Cấu tạo theo nguồn tham chiếu:** tìm component tương đương (Untitled UI; Astryx trên trang `Astryx · Library` chỉ đọc),
  lấy anatomy — phần, trục biến thể, Slot, trạng thái — rồi gắn token DS v2. Spec có mục đối chiếu: khớp gì, lệch gì, vì sao.
  Lệch mà đổi look đã duyệt → hỏi, không tự đổi. Không đặt instance Astryx vào component v2.
* **Khối nghiệp vụ (Application):** chữ và dữ liệu mẫu lấy từ SRS, `*-states.md`, `screens/{flow}.md` (khớp màn đã duyệt);
  định dạng chưa chốt → "chưa chốt (OQ-n)", mẫu trung tính. Description ghi nguồn (file + mục), dùng ở (feature · màn),
  nhãn tầng SaaS (`.claude/rules/saas-layer.md`).
* **Luật lồng:** lồng bằng instance của component gốc, không sao chép, không vẽ lại; token của component lồng giữ nguyên, cha
  chỉ quyết khoảng cách quanh nó (cần cỡ mới → thêm biến thể ở component gốc); phụ thuộc một chiều, không vòng; quan hệ
  cha–con ghi vào `_deps.json` qua `ds-deps.py` (`.claude/rules/ds-stale.md`).

## Luật quyết định thành bại

* **Nguồn spec duy nhất** là `design/design.md` (DS cũ) hoặc `design-system/` (DS v2, mục trên). Đọc lại từ file mỗi lần
  chạy, **theo mục** (Bước 1.2). Skill này không chứa giá trị nào của dự án (màu, câu mẫu, bề rộng, tên trạng thái…).
* **Không có spec thì không dựng.** Component phải có spec: mục trong `design.md` (thường ở § Components - <dự án>),
  hoặc md ở `design-system/components/` với DS v2. Chưa có → Bước 2 viết spec, trình user duyệt, ghi vào nơi đó
  (approval gate), rồi mới dựng.
* **Không tạo component khi thư viện đã có cái tương đương** (Don't của `design.md`). Kiểm thư viện
  Figma + `design/components.md` trước (DS v2: trang `DS · Base components` / `DS · Application components` + md trong `design-system/components/`); nghi ngờ
  thì kiểm code thư viện (vd repo Astryx).
* Tôn trọng quyết định "mẫu ghép" hay "component thật" đã ghi trong `design.md`. Muốn đổi → hỏi user
  và sửa quy định trong `design.md` (DS v2: trong md component) cùng lượt.

## Bước 1 — đọc trước, hỏi sau

1. `figma_status` → plugin, file, trang đang mở. Rồi `figma_docs` bản cheat + recipes (xem đầu file).
   DS v2: đọc thêm `design-system/foundations/motion.md` mục 10.3, 10.11, 10.12 để biết component này phải chạy thế nào.
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
   * **DS v2** (mục *Chọn nguồn spec*) thay các mục trên bằng: `design-system/architecture.md` Mục 4, 5, 6, 7, 11 và
     `foundations.md` Mục 12 (luôn đọc) + mục foundations liên quan tới component (chữ, bo, khoảng cách, vùng chạm và
     focus); tên token cần dùng thì Grep trong `tokens.json`; spec đang dựng (nếu có) và md cùng họ ở
     `components/{base,application}/` làm tiền lệ — spec mới phải nhất quán, lệch thì nêu lý do; `components/README.md` là
     cách ghi md. Mã DEC trong các file → Grep `_workspace/decisions.md` khi cần lý do. Mục chung chưa có bản v2 → đọc ở
     `design.md` như bảng trên.
3. `design/components.md`: đọc mục của **từng component thành phần** định dùng (Usage, Nên/Không nên). DS v2: đọc md
   của từng thành phần ở `design-system/components/` (khi dùng, nên / không nên, thành phần lồng) thay `components.md`.
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

**DS v2:** spec là md theo khuôn `design-system/components/README.md` (không chép khuôn vào đây; thiếu file khuôn → báo
thiếu, không tự nghĩ ra khuôn). Danh mục câu trên vẫn là thứ cần chốt, với Base bỏ phần mẫu câu nghiệp vụ (chữ giữ
chỗ) và thêm *Đối chiếu Astryx* (mục *Chọn nguồn spec*).

**`--propose`: không phỏng vấn.** Soạn spec từ nguồn đã đọc; mỗi điểm lẽ ra hỏi user thành một dòng trong *Câu cần user
quyết* của gói đề xuất (kèm đề xuất mặc định, lý do, nguồn).

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
* Nền tảng theo DEC-279 (architecture Mục 6): cùng cấu tạo → mode `Platform`, không trục; khác cấu tạo hoặc cách
  thao tác (popover → bottom sheet → màn riêng) → trục biến thể `Platform=Web|Mobile` trong cùng bộ, không dựng set
  `/ Mobile`; chỉ một nền tảng → ghi nền tảng kia dùng gì thay. Phần con chỉ có trên app: tiền tố `_`.
* **DS v2:** tên component tiếng Anh theo Untitled, thuộc tính `Hierarchy=Primary, Size=MD, State=Hover…` (architecture
  Mục 5, DEC-260 F11); phần con chỉ dùng bên trong bắt đầu `_` hoặc `.`; không đặt trục mới khi bộ chuẩn đã có. Chỗ đặt
  component con trong cha = Slot có preferred values; đưa thuộc tính của instance lồng ra panel (`exposeNestedInstance`).

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
* **DS v2:** phần ghép là component Base / Application đã có → `get_components` trang `DS · Base components`,
  `DS · Application components`; không có key thư viện ngoài file. Tìm Section sẽ đặt. Thiếu component con cần dùng → dựng nó
  trước (đợt riêng) hoặc đưa vào *Câu cần user quyết*, không vẽ lại trong component này. Astryx: `get_components` /
  `get_page_model` trên trang `Astryx · Library`, chỉ đọc.

## Bước 5 — hỏi phần còn lại, trình kế hoạch, chờ `Y`

Hỏi một lượt (`AskUserQuestion`): **thiết bị — luôn hỏi**; nơi đặt (trang, vị trí; không đè khung có
sẵn); các điểm spec còn "chờ xác nhận" — dựng theo bản hiện tại hay chờ; **bố cục của ví dụ *Trong
ngữ cảnh*** — 3 phương án theo Luật 1 của `.claude/rules/design-system.md`: A theo mẫu gần nhất trong
§ Layout, B và C độc lập (khác nhau thật về cách tổ chức vùng chứa component), mỗi cái kèm lý do.
Ví dụ ngữ cảnh là nơi dev nhìn để biết component đặt vào màn thế nào, nên khung của nó cũng là một
quyết định bố cục, không mặc định lấy mẫu.

**DS v2:** *nơi đặt* không hỏi (ma trận quyết, mục *Chọn nguồn spec*); *Trong ngữ cảnh* không hỏi 3 phương án — khung
trình bày là khung tài liệu theo khuôn, minh hoạ "Được dùng trong" lấy từ instance cha thật. Vẫn hỏi: thiết bị
(Web, Mobile hay cả hai khối), điểm spec chờ xác nhận, điểm *Đối chiếu Astryx* lệch làm đổi look. Kế hoạch dưới đây:
`Platform` là mode nên không nhân vào số biến thể; thay hai dòng "Khung trạng thái" và "Trong ngữ cảnh" bằng
"Khung tài liệu theo khuôn: Section <hàng × cột>".

**`--propose`: không hỏi.** Điền khung kế hoạch dưới đây; mỗi câu hỏi thành một dòng *Câu cần user quyết*; rồi trả gói
đề xuất, dừng (mục *Chạy trong agent con*).

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

**DS v2 — khung trình bày là khung tài liệu theo khuôn** `design-system/components/README.md` (không chép lại khuôn vào
đây): Web | Mobile dàn ngang, nền trắng, mỗi khối đặt mode `Platform` của mình, mục Cấu tạo (hình phóng có nhãn
token), mọi hình mẫu nằm trong ô mẫu có nền thật (chống mất hình), số liệu đọc từ biến theo mode. Đặt trong Section
cột Tài liệu của hàng. Khung này **thay** bước 1 và khung "Trạng thái & ví dụ" của bước 3 bên dưới (khung chứa, cấp
chữ, `Doc · <tên set>`, ví dụ *Trong ngữ cảnh*); bước 2 (dựng set), các bẫy và phần *Chữ dài* (nội dung cực trị ở bề
rộng của từng khối) vẫn áp. Dựng bằng `figma_write`; phần proxy không làm được mới đi `use_figma`, ghi vào báo cáo.

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

0. DS v2: đổi trạng thái đã gắn chuyển động theo `motion.md` mục 10.12 (`figma_read prototype_audit`, hoặc đọc `reactions`); Smart Animate đúng thời gian và đường cong token, không để `transition` rỗng. Thứ Figma không chạy được thì ghi trong spec cho dev, không vẽ giả.

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
6. **Kiểm tên** (DEC-264, bắt buộc): chạy `_scripts/figma-name-lint.js` (đọc file, thay `ROOTS` = id Section của
   component, dán làm `code` cho `figma_write`). Luật: component ≤ 32 · thuộc tính ≤ 20, giá trị ≤ 16 · layer chữ theo
   vai trò (`Title`, `Label`, `Value`, `Note`…), không theo nội dung, ≤ 24 · màn demo `<Màn> / Web|Mobile[ / <Trạng
   thái>]` ≤ 40 · không mã DEC/mã node trong tên. `fail` = 0 mới trình; FAIL ở giá trị biến thể → *Cần user quyết*.
   Bảng đủ: `design-system/_review/agent-brief-base.md` §2d.
7. **Dark:** một khung mẫu đặt mode Dark bằng `modify(frameId, { explicitVariableModes: { <collection
   màu>: "Dark" } })` (tên collection/mode đọc từ `figma_rules`); không có mode Dark thì bỏ, ghi 1 dòng.

**Tự rà** (máy không kiểm):

8. **Một ảnh chụp mỗi component set**, một ảnh khung trạng thái, một ảnh *Chữ dài*, chụp **một lần** ở
   cuối. Tìm: khoảng trống thừa, nội dung mặc định còn sót ("Button", "Content", giờ kiểu Mỹ…). Đối
   chiếu từng quy tắc chữ dài và hành vi của spec với ảnh.
9. Do's and Don'ts của `design.md`: (a) ≤ 1 nút Primary mỗi nhóm; (b) trạng thái không chỉ dựa vào
   màu; (c) đủ rỗng / đang tải / lỗi; (e) không vi phạm "Không nên" của component thành phần.
10. **Chip trạng thái:** component có trạng thái dùng instance `Chip trạng thái` (không tự vẽ pill); icon và chữ
   đúng màu `Status Chip/<Sắc>/Foreground` (đổi icon qua thuộc tính `Icon` xong kiểm màu nét, quét cả biến
   thể gốc lẫn instance — `findInstances`); mã nghiệp vụ dùng `Text/Code Small`; khung *Chữ dài* thử tên/nhãn dài nhất cho phép
   (14 ký tự) + mã dài nhất. Component gắn với feature có `*-states.md` → chạy
   `python3 _scripts/status-chip-lint.py <file states>`; FAIL thì báo, KHÔNG tự đổi nhãn nghiệp vụ.
11. Sửa lỗi → chạy lại audit của phần đã sửa, chụp lại **chỉ phần đã sửa**.
11a. **A7 · Thứ tự chú ý — chỉ component khung** (header, sidebar, breadcrumb, page header, tab bar, bottom nav): chạy
    trên màn demo Web *Trong ngữ cảnh*, lập vùng như `/figma-screen` Bước 6 mục 7a → `python3 _scripts/attention-audit.py
    --image <png> --regions <vùng.json> --out <scratchpad>`. `K1` FAIL (khung nặng hơn tiêu đề trang) chặn — sửa trước
    khi trình; kết quả truyền cho `visual-reviewer` ở mục 12. Không phải component khung → ghi 1 dòng "A7: không áp".
12. **DS v2 — 3 agent review** (bắt buộc mỗi lần dựng hoặc sửa lớn component DS v2, sau mục 1–11): chạy song song
    `visual-reviewer`, `uxui-reviewer` và một agent `general-purpose` làm accessibility (`figma_read a11y_audit` trên set
    và màn demo, rồi skill `accessibility-review`, chấm WCAG 2.2 riêng Web và Mobile). Prompt mỗi agent: file + node id
    của set và demo, đường dẫn spec md, ảnh preview đã duyệt (nếu chạy `--html`), luật "không đổi look đã duyệt". Mỗi
    điểm trả về: mức Cao/Trung/Thấp, mô tả, node, đề xuất sửa, cờ `changesLook`. Điểm không đổi look và không phải
    quyết định → sửa luôn rồi kiểm lại phần đã sửa; điểm còn lại gom lên **một** trang (tab *Review Figma* khi chạy
    `--html`, không thì một artifact riêng), không rải trong chat.

**DS v2 — thêm / đổi ở Bước 7** (khuôn `design-system/components/README.md`):

* **Kiểm mất hình** bằng script README chỉ tới, trên khung tài liệu, trước khi chụp ảnh: luật A (khung) phải 0 lỗi, sửa
  tới khi đạt. Cờ B–D trên nền thật là sự thật của component — **không** sửa component, không đổi nền ô cho đẹp: ghi
  *Cần user quyết*. Kết quả ghi vào md, không đặt hộp kết quả trên Figma.
* **Kiểm luật lồng** (architecture Mục 4, 7): không mã màu / số trần, không gắn Primitives; Base không mang dữ liệu nghiệp
  vụ; component cha không detach, không override fill / stroke / cỡ trên instance con.
* Số in trong tài liệu đọc từ biến theo mode của khối, không gõ tay. Trợ năng chấm WCAG 2.2 theo mục Trợ năng của khuôn
  (tiêu chí Web và Mobile khác nhau, điểm ghi riêng); lớp thứ hai `accessibility-review` (mục 3) vẫn chạy.
* Mục 5 (`responsive_audit` ví dụ *Trong ngữ cảnh*) và mục 7 (Dark: giá trị Dark chưa điền, architecture Mục 7): bỏ,
  ghi 1 dòng mỗi mục.
* Mục 9: Do's and Don'ts vẫn đọc ở `design.md` (bảng *Chọn nguồn spec*). Mục 10: dùng instance `Base / Status Chip`, Tone
  theo bảng ánh xạ trạng thái nghiệp vụ → sắc, nhãn nguyên văn từ `*-states.md`, không đè màu; kiểm còn lại như mục 9.

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
* **DS v2:** tăng phiên bản `x.y.z` ở md theo architecture Mục 9 — z sửa nhìn hoặc lỗi; y thêm biến thể / thuộc tính (màn
  cũ vẫn đúng); x đổi tên hoặc bỏ thuộc tính (màn phải sửa: báo trước, user duyệt, kèm script đổi). Vòng đời md: Nháp →
  Đang review → Ổn định → Ngừng dùng.

## Bước 9 — báo cáo và cập nhật tài liệu

DS v2: đổi trạng thái dòng của component trong `motion.md` mục 10.12 thành `✅ đã gắn`; component chưa có dòng thì thêm dòng.

```
Đã dựng "<Tên>" trong <file>, trang <trang> (node <id khung>):
<set> <n biến thể> · <set> <n> · …
Máy đã kiểm: biến thể/thuộc tính · layout_audit · a11y_audit · compliance <x> · responsive <w…> · Dark · A7 chú ý <n FAIL / m WARN | không áp>
Tự rà: ảnh chụp <n> · chữ dài ở <w> và 320px · Do's and Don'ts
Đường dự phòng use_figma: <phần nào, vì sao — hoặc "không dùng">
Máy KHÔNG kiểm: nội dung nghiệp vụ đúng chưa [Cao] · thiếu trạng thái nghiệp vụ nào [Cao] · thẩm mỹ [Thấp]
Chưa có chuẩn trong design.md: <…>
```

Rồi cập nhật spec của component trong `design.md` (bảng: tên set, key, biến thể/thuộc tính, dựng
từ gì; các quyết định mới; Known Gaps theo Iteration Guide — dòng `KG-nn` trong `design.md` + hàng chi
tiết ghi ngay tại dòng đó, không có file backlog riêng) — qua approval gate. Quyết định mới lặp lại ở ≥ 2 spec → đề xuất
đưa lên *Quy ước chung của component dự án*.

**DS v2:** cập nhật md `design-system/components/{base,application}/{slug}.md` (component mới thì tạo md) thay cho `design.md` — qua
approval gate (plan preview khi tạo, diff khi sửa). Phần máy giữa `<!-- auto:begin -->` và `<!-- auto:end -->` (thuộc tính, màu và số đo
theo phần) sinh từ Figma bằng `_scripts/figma-component-export.js` rồi `python3 _scripts/ds-v2-component-doc.py`, không
sửa tay; phần người viết (khi dùng, nên / không nên, mục *Đối chiếu Astryx*, `### Kiểm máy`) nằm ngoài hai dấu. Báo cáo
thêm mục đối chiếu nguồn tham chiếu và kết quả kiểm mất hình; dòng cuối đổi thành `Cần user quyết: <…>` (DS v2 không có
Known Gaps `KG-nn`). User chốt giữa ≥ 2 phương án → thêm dòng DEC vào `_workspace/decisions.md`
(`.claude/rules/decision-log.md`).

**Màn của feature đổi theo** (Bước 8 sửa main component → instance trên màn đổi theo): từ
`findInstances(setId, { scope: "document" })`, lấy frame màn có instance (tên `<[#]> · <web|mob> · <slug>`)
→ feature + flow qua cột `Figma` của `screens/{feature}-screen-index.md` hoặc wireframe index. Đổi nhìn
thấy được trên màn (chữ, phần tử thêm/bớt, trạng thái) → gọi `/figma-sync {feature} --flow {flow}` inline cho
từng flow bị chạm (`.claude/rules/screen-source.md` Mục 5). Chỉ đổi hình (màu, bo, khoảng cách) → không gọi,
ghi "màn bị chạm: n, chỉ đổi hình" trong báo cáo.

## Chế độ `--html` — brainstorm và preview trên artifact trước Figma

Dùng cho component **mới** của DS v2 (DEC-285). Lý do: chốt hình trên HTML rẻ hơn sửa trên Figma, và HTML được **vẽ tự
do**, không bị token và foundation hiện tại trói, để thấy được phương án tốt nhất trước; ràng buộc foundation kiểm ở
vòng 3. **Một component mỗi lần chạy**: nhiều component một trang quá nặng để soi.

Mọi thứ nằm trên **một artifact** (4 tab, giữ một link suốt các vòng). Nguồn của trang là thư mục làm việc
`design-system/components/_work/{slug}/`:

| File | Nội dung | Ai ghi |
|---|---|---|
| `page.json` | dữ liệu trang: tham chiếu, ý tưởng, điểm cần quyết, preview, khai giá trị, kết quả review. Khuôn: `html-kit/sample-page.json` | Claude |
| `check.json` | kết quả đối chiếu foundation | `_scripts/ds-foundation-check.py --write` |
| `answers.json` | lựa chọn của user, dump từ db của artifact (`ArtifactData list`, collection `answers`) | Claude, đầu mỗi vòng |
| `state.json` | `{round, artifact_url, approved: {brainstorm, preview, foundation}, figma: {set, demos}}` | Claude |
| `{slug}-review.html` | trang sinh ra — publish file này | `_scripts/ds-component-page.py {slug}` |

**Màn chính là preview toàn màn hình** (user chốt 28/10, khuôn `/prototype-html`): trang mở thẳng vào màn demo full cửa
sổ (web vẽ theo bề rộng cửa sổ, mobile khung điện thoại giữa màn), nút tròn góc dưới phải mở bảng nổi 4 tab: *Bước* (1–4),
*Màn & kịch bản* (mỗi màn → các trạng thái; bước 1 thêm bộ phương án theo nguồn), *Chọn* (việc của bước đang xem: B1 điểm
cần quyết + Chốt tổ hợp · B2 Duyệt/Cần sửa · B3 chế độ xem + nhấp nháy + tô viền + danh sách điểm lệch, mỗi dòng có Soi và
xem Trước/Sau riêng dòng đó · B4 chế độ xem + ghim + Sửa/Bỏ qua), *Hiển thị*. Trang tab cũ chỉ để đối chiếu, mở bằng
*Xem bảng chi tiết*. Tab *Góp ý*: user bấm "Chọn phần tử", trỏ vào đúng component / control trên màn (có "Chọn phần tử
cha"), ghi ý kiến → lưu db collection `comments` (bước, màn, trạng thái, tổ hợp, đường dẫn phần tử, tên phần theo `values`,
chữ đang hiện, ghi chú), ghim G-n tím trên màn. Đầu mỗi lượt sửa: `ArtifactData list comments`, sửa từng góp ý, rồi ghi lại
doc đó với `done: true` + `reply` (1 câu đã sửa gì, từ khoá bọc `**…**` để trang tô nổi) — trang tách 2 khối: tím "Anh góp ý", xanh "✓ Claude đã sửa" (cam "Chờ Claude xử lý" khi chưa có trả lời). **Góp ý thêm** (user chốt 28/10): dưới góp ý đã xử lý có nút "Chưa ổn — góp ý thêm" → trang
nối `{role:"user", text, at}` vào `thread` và đặt `done: false` (ghim hiện lại). Lượt sau Claude đọc cả chuỗi (`note` → `reply` →
`thread`), sửa theo ý mới nhất, rồi **nối** `{role:"claude", text, at}` vào `thread` + `done: true` — không ghi đè `reply` lần
đầu, giữ lịch sử qua lại. **Ghi thay đổi theo từng góp ý** (thay cách chụp cả lượt): trước khi sửa 1 góp ý chép
`page.json` ra scratchpad, sửa xong `python3 _scripts/ds-snap.py change <slug> <bản-chép> <id>` → `cmtChanges[id]` (từng luật
CSS, màn, dòng values) + bản trước `snaps["c-<id>"]`. **Hoàn lại** (user 28/10): góp ý đã xử lý có nút "↶ Hoàn lại bản trước"
(bấm 2 lần) → trang nối `{role:"user", action:"revert"}` + `done:false`. Claude chạy `ds-snap.py revert <slug> <id>` — chỗ
hiện tại còn đúng bản sau thì trả về bản trước, chỗ đã bị góp ý sau sửa tiếp → xung đột, giữ nguyên và báo user; rồi nối
`{role:"claude", action:"reverted", text}` + `done:true` + `reverted:true`. Góp ý đã xoá không hoàn lại. Lượt cũ chụp cả lượt
(r1, r2…) không có `cmtChanges` → hoàn lại tay theo bản trước. **Bản trước khi sửa** (user chốt 28/10):
trước khi sửa, chép `page.json` ra scratchpad; sửa xong chạy `python3 _scripts/ds-snap.py <slug> <bản-chép> r<n> "trước lượt
sửa n (dd/mm)" <id góp ý,…>` → lưu phần đã đổi vào `snaps` + `cmtSnap`, mỗi góp ý có nút *Xem bản trước* cạnh *Xem trên
màn* (màn vẽ lại bằng bản chụp, đúng màn, trạng thái, tổ hợp lúc góp ý; thanh tím "Về bản hiện tại"). Bản chụp trùng phần
lớn bản có sẵn thì tự ghi `base` và chỉ lưu phần khác. `page.json` đã sửa thẳng (proto, `cssScreen`, `sel`, ghim) thì
**không chạy lại `build.py`** — sửa thẳng `page.json`; build.py có chặn khi thấy `proto`. Dữ liệu mới không cần khai thêm — bảng nổi đọc từ `screens`, `states`, `presets`, `decisions`,
check.json, `reviews`.

Gọi lại `/figma-component <tên> --html` → đọc `state.json`, chạy tiếp đúng vòng đang dở, không làm lại vòng đã chốt.
Publish luôn cùng đường dẫn file (giữ link), `capabilities: {db: {}, user: {}}` ở lần đầu; lần sau bỏ trống để giữ.

### Vòng 0 — tham chiếu (chỉ đọc)

1. **Untitled UI:** code `design/_ref/untitled-ui/react/components/` (thiếu thì chạy `_scripts/ref-untitled.sh`) + trang
   `untitledui.com/components/{tên}`: phần cấu tạo, trục biến thể, cỡ, trạng thái, hành vi mobile (breakpoint).
2. **Astryx hiện tại:** mục component trong `design/design.md` + node Figma cũ (memory benchmark Astryx); chụp hoặc vẽ lại.
3. **Nơi dùng thật:** grep tên component / control type trong `docs/*/screens/*.md`, `docs/*/srs/*-spec.md` → danh sách
   feature · màn. Không có nơi dùng → hỏi user có cần dựng không (DEC-260: chỉ dựng component sản phẩm dùng).
4. **Xếp nhóm web/mobile** A/B/C theo DEC-279 (architecture Mục 6).
5. **Lấy kho đã duyệt** (user chốt 28/10): `python3 _scripts/ds-kit.py` in trạng thái 9 mục foundations
   (`design-system/foundations/README.md` mục 0) và mọi component md (`design-system/components/*/`). Preview vòng 1 và vòng 2 **ráp từ kho
   này**: token qua `design-system/tokens.css`, phần con là component đã có (lấy anatomy, CSS, số đo từ md/`_work` của nó),
   không vẽ lại cái đã có. Chốt danh sách component preview dùng → `python3 _scripts/ds-kit.py <slug> --uses a,b` ghi
   `page.kit`; trang hiện khối *Ráp từ kho*, phần chưa `approved` vẫn dùng nhưng gắn nhãn "chưa duyệt".
6. **Component lồng nhau** (DEC-292): khai con trong `design-system/components/_deps.json` (`uses`: child, role `embed`/`anchor`,
   `provisional` khi con chưa dựng, `parts`). Quyết định về hình dạng con thuộc con — cha chỉ quyết cách đặt con; nếu buộc
   phải chốt trước (con chưa dựng) thì ghi vào `inherited.<con>` (id, title, choice, from, dec). Component đang dựng là con
   của ai → `ds-deps.py inherited <slug>`: các điểm đó vào brainstorm làm mặc định (trang hiện khối *Chốt sẵn từ component
   cha*); user đổi thì cha cần sync. `ds-kit.py <slug>` tự lấy con từ sổ, ghi phiên bản từng con. Sau khi chốt / sửa góp ý
   làm đổi hình một component → `python3 _scripts/ds-deps.py check --write --backlog` (hook `ds-stale.sh` cũng tự chạy):
   component có con lồng trong nó (kể cả bắc cầu, tra qua `kg impact`) hoặc foundation nó dùng đổi phiên bản bị đánh
   `status: stale` + ⚠ (trang + dashboard) và có task "Sync <slug> (DS stale)"; làm task = chạy lại `ds-kit.py <slug>`,
   dựng lại preview, chạy lại bước 3 / review, rồi **`python3 _scripts/ds-deps.py synced <slug>`** (ghi mốc, trả status cũ,
   task tự đóng). Component mới dựng xong cũng chạy `synced <slug>` để có mốc. Trên Figma cha dùng instance của con nên tự
   theo. Luật đủ: `.claude/rules/ds-stale.md` (DEC-302).

### Vòng 1 — Brainstorm (tab 1)

* **Ý tưởng cộng đồng — 8 đến 12 mẫu**, không dừng ở 2–3. Nguồn: Dribbble, Behance, 21st.dev, Refero (refero.design —
  màn sản phẩm thật web và app); thêm Mobbin khi cần mẫu app. Tìm bằng `WebSearch` (nhiều truy vấn cùng lượt: tên component tiếng Anh + biến thể +
  "logistics / dashboard / mobile"), đọc trang bằng `WebFetch`. Chọn mẫu **sát tên component nhất** và **nhìn ổn**
  (gọn, không trang trí thừa, đọc được); bỏ shot chỉ là ảnh đẹp không dùng được thật. Mỗi mẫu: nguồn, link bản gốc,
  1–2 câu điều đáng học, và **hình vẽ lại bằng HTML** (không nhúng ảnh của người khác). Phủ đủ web và mobile.
* **Điểm cần quyết** (thường 4–8): cấu tạo, trục biến thể, cỡ, trạng thái, hành vi web/mobile, chi tiết hình (bo, viền,
  icon). Mỗi điểm: lý do phải quyết, nguồn, **2–4 phương án** có hình xem trước (ghi ý tưởng nguồn nếu có), cột
  Untitled và cột "Astryx hiện tại" cùng nội dung để chỉ khác đúng điểm đang hỏi. Một phương án đánh dấu đề xuất.
* Chữ trong hình dùng dữ liệu logistics thật (lệnh vận tải, xe, lái xe), tiếng Việt có dấu; theo memory về câu hỏi
  đủ ngữ cảnh: giải thích mã, trích nguồn.
* **Thử trên màn** (khu đầu tab, học `/prototype-html` và `/wireframe-html`): 2–4 **màn ví dụ trông như sản phẩm thật**
  có dùng component đang bàn (chọn theo danh sách nơi dùng ở vòng 0), cả Web (khung 1280, tự co) và Mobile (khung điện
  thoại 393). Kit tự bọc **vỏ ứng dụng**: web = sidebar invlogis + header (đường dẫn, ô tìm, chuông, tài khoản) + tiêu đề
  trang; app = thanh trạng thái + thanh tiêu đề + thanh tab dưới. Màn chỉ viết phần nội dung. Nút nổi **Bảng chọn** (góc
  dưới phải; mobile mở sheet) mở menu 3 tab: *Biến thể* (bộ chọn sẵn theo nguồn + phương án từng điểm + "Chốt tổ hợp
  này"), *Màn*, *Hiển thị* (trạng thái, Light/Dark). **Màn bấm được như prototype** (mọi tab có màn demo, cả khung
  biến thể lẻ): khai `proto` — bấm ô tìm mở bảng tìm, bấm chuông mở thông báo, bấm một dòng thì đóng; bấm ra ngoài lớp
  đang mở hoặc Esc thì về trạng thái trước; bấm chỗ trống thì nháy viền mọi vùng bấm được. Không khai `proto` → bấm
  phần tử `data-cmp` mở menu như cũ.
  Bộ chọn sẵn: `rec` (đề xuất), `untitled`, `astryx`, mỗi ý tưởng cộng đồng một bộ (id trùng id ý tưởng; card ý tưởng có
  nút "Xem trên màn demo").
  Cách viết trong `page.json` (khuôn: `html-kit/sample-page.json`):
  - `css` chung cho mọi hình; phương án viết bằng bộ chọn thuộc tính: `.pv[data-D1=b] .tg{border-radius:999px}`
    (phương án thứ i = chữ thứ i: a, b, c…).
  - Phần tử chỉ có ở một phương án hoặc trạng thái: `data-show="D2:b"`, `data-show="state:loading"`; nhiều điều kiện
    cách nhau dấu cách = phải đúng hết.
  - `states`: `[{key, label}]` — đủ các trạng thái component có (mặc định, đang tải, rỗng, lỗi, chữ dài…).
  - `screens`: `[{id, name, device: web|mobile, width?, note, title?, nav?, crumb?, back?, tabs?, heading?, shell?, html}]`
    — `nav` = mục sidebar / tab dưới đang chọn; `shell: "none"` bỏ vỏ. Component đang bàn gắn `data-cmp`.
    `presets`: `[{id, label, pick: {D1: "a"}, screen?}]`.
  - `proto`: `[{sel, state?, set?, toggle?, back?, close?}]` — bấm phần tử khớp `sel` sang `state` (và/hoặc biến thể
    `set: {D7: "b"}`); `toggle` bấm lần 2 về `back` hoặc trạng thái trước; `close: true` = phần tử đóng lớp. `protoLayers`
    = bộ chọn các lớp mở (bấm bên trong không đóng); `protoHint` = câu gợi ý trên màn. Mọi trạng thái người dùng tự mở
    được trên sản phẩm thật phải có đường bấm; trạng thái do dữ liệu (rỗng, chữ dài) chọn ở Bảng chọn.
  - Dữ liệu mẫu cố định (không ngày giờ chạy, không ngẫu nhiên); nhãn trạng thái là chữ nghiệp vụ, không mã kỹ thuật;
    không emoji (icon SVG nét); màn chỉ chứa thứ người dùng thật thấy (luật `/prototype-html`).
* Sinh trang (`ds-component-page.py`), publish, rồi **dừng**: báo link, chờ user chọn trên trang.

### Vòng 2 — Preview (tab 2)

User báo đã chọn → `ArtifactData list answers` → ghi `answers.json` → tóm tắt lựa chọn trong chat (1 bảng) → chạy lại
`ds-kit.py <slug> --uses …` (trạng thái kho có thể đã đổi; tổ hợp mới có thể cần thêm component) → dựng preview đúng các lựa chọn:

* **Màn demo đã chốt:** cùng `screens` của vòng 1, khoá theo tổ hợp user chốt (`ds-component-page.py` tự đọc
  `answers.json` ghi vào `preview.pick`), bổ sung màn còn thiếu tới đủ 4 loại (danh sách, chi tiết, form, sheet xác
  nhận) nếu component dùng ở đó; mọi trạng thái trong `states` phải bật được trên màn.
* **Bảng biến thể** (`preview.blocks`): đủ biến thể và trạng thái đã chốt; **khối Web và khối Mobile riêng** (mobile
  trong khung 393); Light/Dark (CSS tự khai `.pv[data-theme=dark]`); kiểm chữ dài cho trường được xuống dòng.
* **Khai giá trị** vào `values` của `page.json` song song khi viết CSS: mỗi phần × thuộc tính × nền tảng × cỡ × trạng
  thái có số hoặc màu riêng (cách ghi: docstring của `ds-foundation-check.py`). Màu chữ/icon/viền mang nghĩa ghi kèm
  `on` (nền) để đo tương phản; control ghi `control: true`; phần bấm được ghi `interactive` và `hitArea`. **Mỗi dòng
  ghi `sel`** (bộ chọn trong CSS nơi giá trị nằm; thêm `cssProp`, `tpl` khi thuộc tính viết gộp) — thiếu `sel` thì tab 3
  không vẽ lại được. CSS chỉ của khung màn demo (vỏ, bảng dữ liệu mẫu) để ở `cssScreen`, không đối chiếu. Thứ tự làm máy:
  (1) `_scripts/ds-css-split.py _work/{slug} --inline --write` — style inline có số trong màn → class phụ, rule chỉ trúng
  phần tử ngoài component (`data-cmp`, `data-show`/`data-any` theo phương án hay trạng thái, bảng biến thể) → `cssScreen`;
  (2) `ds-foundation-check.py … --declare` — gắn `sel` (một ứng viên, hoặc trùng bộ chọn đã gắn cho cùng phần), khai tự
  động giá trị trần còn lại (`"auto": true`, tên phần lấy theo bộ chọn đã học), bỏ dòng auto trùng dòng gốc; (3) dòng còn
  mơ hồ gắn tay; dòng không có trên CSS preview (vd shadow, độ đậm trong shorthand) ghi `noOverride: true` + `why`;
  (4) đặt tên phần dễ đọc cho dòng auto còn mang tên bộ chọn; (5) so ảnh tab 2 trước/sau phải giống từng điểm ảnh.
* **Component khung → A7 trên preview** trước khi dừng chờ duyệt: chụp màn demo Web bằng Playwright/Chrome, hộp vùng lấy
  bằng `getBoundingClientRect` → `attention-audit.py --image --regions`. FAIL thì sửa preview trước — bắt lỗi khung nặng
  hơn nội dung ngay ở bản xem trước, trước khi lên Figma.
* Duyệt kiểu L3: tối đa 3 bản (`preview.version`; ô duyệt của bản n lưu ở `preview-approve-vn`, bản 1 là `preview-approve`), mỗi bản sửa theo ghi chú + comment trên trang (comment chỉ đổi phần
  tử được comment, memory phạm vi comment). Dừng chờ "Duyệt".

### Vòng 3 — Đối chiếu foundation (tab 3)

1. `python3 _scripts/ds-foundation-check.py design-system/components/_work/{slug} --write` → `check.json`.
   **Kiểm kỹ 7 nhóm** (user chốt 28/10): `ds-foundation-check.py` gắn `group` cho mọi dòng (Chữ · Màu · Icon · Hiệu ứng ·
   Khoảng cách & cỡ · Bo góc · Lưới & độ rộng) và nạp `_scripts/ds_foundation_audit.py` kiểm thêm: font ngoài bộ DS, tổ hợp
   cỡ/dòng ngoài thang type/*, viết hoa + giãn chữ sai caption-caps, cỡ icon ngoài 12/14/16/18/20/24, nét khác 1.8, khối icon
   nhấn mạnh khác Featured 48/24, blur ngoài blur/*, bề rộng khung ngoài width/* và lề nội dung khác screen-inset (cả hai chỉ chấm cho component dựng khung trang, `page.json` `"auditInset": true` — lề nằm ở khung màn demo, không thuộc component thường; user 29/10). Báo cáo in
   "Theo nhóm", check.json có `groups`; bảng nổi bước 3 lọc theo nhóm.
   **Mọi dòng phải soi được trên hình** (user 29/10): `ds-foundation-check.py` FAIL khi `sel` của một dòng không trỏ tới
   phần tử nào đang hiện ở tổ hợp đã chốt, đúng nền tảng (in "Không soi được trên hình"). Dòng kiểm thêm chỉ nằm trong
   phương án đã loại (`data-show`/`data-mshow` khác pick, tính cả khối cha) tự bỏ — không phải sai lệch của component.
   Luật `display:none` gắn phương án đã chọn (`.pv[data-D6=c] .sbs{display:none}`) cũng tính là ẩn.
   Sửa bằng `platform`/`sel` đúng chỗ, hoặc thêm ô vào bảng biến thể; bỏ khai báo CSS không phần tử nào dùng.
   Phần chỉ hiện khi tương tác (menu nổi, popover, tooltip): khai `"soi": {"state": "scope", "set": {"ck": "…"},
   "add": {"<sel>": "is-hover"}}` trên dòng values — nút Soi tự bật trạng thái đó. Dòng `noOverride` phải quyết thì
   khai `"at": "<sel>"` (chỗ để soi, không ghi đè). Dòng theme Dark: Soi tự chuyển trang sang Dark.
2. Sinh lại trang, chạy `python3 _scripts/ds-soi-check.py {slug} --all` (bấm Soi thật từng dòng trên trang bằng Chromium
   headless; còn ✗ thì sửa như bước 1 rồi sinh lại), publish, dừng. Tab 3 vẽ lại màn demo + bảng biến thể bằng `design-system/tokens.css`, đổi qua lại 3
   chế độ: *Tự do* (bản tab 2) · *Theo lựa chọn hiện tại* · *Tất cả về token có sẵn*, có nhấp nháy A/B, tô viền chỗ đổi,
   bấm dòng để soi phần tử, Light/Dark, bảng Trước → Sau. User quyết từng dòng ⛔ và ＋, và mọi dòng ↔ **nhìn thấy khác**
   (`must`, viền cam); ↔ không thấy khác thì không chọn = kéo về token đề xuất. Nhóm *Chưa khai* (giá trị trần trên hình
   chưa có dòng) phải về 0 bằng cách khai thêm vào `values` — không chọn thay user. Bỏ qua một giá trị (`cssIgnore`) bắt
   buộc có `why`; trang in ra để user soát.
3. Dump `answers.json`, chạy lại script: exit 0 mới sang vòng 4. Quyết định "đổi luật foundation" hoặc "thêm token" →
   sửa `design-system/tokens.json` + `foundations.md` qua L1/L2 trên `main`, chạy `ds-v2-tokens.py`, ghi DEC; quyết định sửa
   preview → sửa preview, sinh lại (không cần user duyệt lại phần đã khớp).

### Vòng 4 — Figma

* Ghi spec `design-system/components/{base|application}/{slug}.md` từ các lựa chọn đã chốt (L1 plan; số đo ghi bằng **tên
  token** sau đối chiếu, không ghi số trần), thêm DEC cho từng điểm đã chọn giữa ≥ 2 phương án (gom một dòng DEC nếu
  nhỏ). Ảnh preview đã duyệt chụp lưu `_work/{slug}/preview-web.png`, `preview-mobile.png` làm mốc nhìn.
* Dựng theo Bước 6–7 (đường `--build`, gói = spec + ảnh mốc). **Mốc nhìn là chế độ "Theo lựa chọn hiện tại" của tab 3**
  (không phải bản tự do tab 2). Hình Figma khác mốc chỗ nào mà không do token → sửa Figma, không sửa preview (memory
  prototype → Figma).
* **Trạng thái:** md mang `status` draft → in-review (đã lên Figma, đang review) → approved (user duyệt sau vòng 5) →
  shipped; dòng meta `> …` của md cùng nhãn (Nháp · Đang review · Đã duyệt · Đã bàn giao). Trên Figma: dòng đầu mô tả set
  `Trạng thái: …` + frame "Nhãn trạng thái" nằm thẳng trong Section (không đặt tên "Trạng thái": trùng Section con khu demo state). Đổi status qua L2 bảng Trước → Sau.
* **Figma ↔ repo luôn khớp:** sau MỌI lần ghi Figma chụp lại bằng `_scripts/figma-ds-snapshot.js` (qua `use_figma`, chỉ
  đọc; `PAGE_ID=''` → biến + danh sách trang, rồi từng trang DS) → `ds-v2-sync-check.py --merge …` →
  `ds-v2-sync-check.py --figma .claude/state/figma/ds-v2-snapshot.json`. FAIL thì sửa trước khi báo xong.

### Vòng 5 — Review Figma (tab 4)

Bước 7 mục 12 (3 agent). Đưa kết quả vào `reviews` của `page.json` (ảnh chụp node tải lên bằng `assets` hoặc bỏ trống),
link Figma vào `figma`, sinh lại, publish, dừng. User chọn Sửa / Bỏ qua → sửa → kiểm lại phần đã sửa → Bước 9.

Tab 4 **có preview**: hình trái đứng yên (cùng màn demo, vẽ theo mốc tab 3, bấm được như prototype), danh sách điểm cuộn
bên phải. Mỗi điểm review khai thêm khi chỉ được vào hình:

| Trường | Nghĩa |
|---|---|
| `screen` · `state` · `pick` | màn (id), trạng thái, biến thể để thấy chỗ đó — nút *Xem trên hình* nhảy tới |
| `sel` | phần tử trên màn — ghim R-n (đỏ/cam/xanh theo mức) hiện khi đúng màn + trạng thái |
| `after` | CSS "sau khi sửa" (`.pv …{}`) — xem ở chế độ *Sau khi sửa · theo lựa chọn* / *· tất cả* |
| markup `data-fix="R2"` / `data-unfix="R2"` trong `screens` | phần thêm / phần bị thay khi sửa (đổi chữ dùng cặp này) |
| `where` | 1 câu chỗ lệch nằm ở đâu (vd "preview có, Figma chưa vẽ") |

Điểm không chỉ được vào hình (API thuộc tính, nhãn khung Tài liệu, spec trợ năng) để trống các trường trên.

### Luật chặn

| Chưa có | Không được |
|---|---|
| user chọn xong vòng 1 (mọi điểm cần quyết có lựa chọn, hoặc user nói "theo đề xuất") | dựng preview |
| user chọn "Duyệt" ở tab 2 | chạy đối chiếu foundation |
| `ds-soi-check.py {slug} --all` exit 0 (mọi dòng soi ra phần tử trên màn demo / bảng biến thể) | publish trang vòng 3 |
| `ds-foundation-check.py` exit 0 (gồm 0 *Chưa khai*, 0 *Không soi được*, mọi dòng `must` đã chọn) | ghi spec md, đụng Figma |
| `ds-v2-sync-check.py --figma` không FAIL sau lần ghi Figma | báo xong lượt dựng / sửa |
| 3 agent review chạy xong | báo hoàn tất |

Chế độ chạy (`/run-task`) không áp cho `--html`: mọi vòng chờ người chọn trên trang.

## Chạy trong agent con

Agent con không hỏi được user (`AskUserQuestion` bị bỏ qua) và không được ghi file đích trước khi user duyệt
(`.claude/rules/approval-gate.md`, mục *Sub-agent KHÔNG được ghi file đích trước approval*). Nên chia hai pha: agent con
đọc và soạn; phiên chính trình user; user `Y` thì dựng.

**Chế độ đề xuất bật khi** lời gọi ghi `--propose`, hoặc skill chạy trong agent con (không có `AskUserQuestion`).
Không chắc → coi là đề xuất.

### Pha 1 — `--propose`

Làm Bước 1 (đọc) → 2 (soạn spec, không phỏng vấn) → 3 (API) → 4 (dò file) rồi **trả về, dừng**.

* Được: `figma_status`, `figma_docs`, `figma_read`, `figma_rules`, `get_libraries`, `search_design_system`,
  `get_metadata`, đọc repo; `Write` bản nháp **chỉ** vào thư mục nháp phiên chính chỉ định (ngoài repo).
* Cấm: `AskUserQuestion`; ghi / sửa file trong repo (spec md, `design.md`, DEC, changelog); `figma_write`,
  `use_figma` (kể cả lệnh thử slot của Bước 4 — ghi "sẽ thử" vào kế hoạch); xoá / sửa node.

**Gói đề xuất** — văn bản trả về, đủ để phiên chính trình user mà không phải đọc lại nguồn:

1. **Spec md đề xuất:** toàn văn theo khuôn, kèm đường dẫn đích và action (tạo / cập nhật; cập nhật thì kèm bảng
   Trước → Sau).
2. **Bảng API** (Bước 3): set, trục × giá trị = số tổ hợp, thuộc tính TEXT / BOOLEAN / INSTANCE_SWAP / SLOT, instance
   lồng + cấu hình được phép + phần đưa ra panel; component đã có (cập nhật hay dựng mới).
3. **Kế hoạch ghi Figma:** khung Bước 5 đã điền — file, trang, Section (hàng × cột), thứ tự lời gọi `figma_write` (tạo
   set · thuộc tính · xếp + mô tả), phần đi `use_figma` (slot), khung tài liệu; kèm kết quả dò Bước 4 làm căn cứ (id /
   key thành phần, token thiếu, node đã có).
4. **Câu cần user quyết:** mỗi câu có câu hỏi, **đề xuất mặc định**, lý do, nguồn (file + mục hoặc DEC), và nhãn *chặn
   dựng* / *không chặn*. Luôn có: thiết bị; điểm lệch Astryx làm đổi look; token, component con thiếu; điểm spec chờ xác nhận.
5. **Chưa có chuẩn** chạm tới (không bịa giá trị).

**Phiên chính** (không phải agent con) trình gói qua approval gate (plan preview, diff), hỏi *Câu cần user quyết* bằng `AskUserQuestion`, sửa gói
theo ý user, ghi spec md vào repo sau `Y`, rồi mới sang pha 2.

### Pha 2 — `--build <gói đã duyệt>`

Prompt kèm gói (đường dẫn hoặc chép nguyên), câu trả lời của user và dấu "đã duyệt". Agent con — hoặc chính phiên
chính — chạy Bước 6 → 9, không hỏi lại.

* Đọc lại trang đích (`get_page_model`) trước khi ghi: file có thể đã đổi từ lúc dò; khác gói (node đã có, tên trùng,
  token đổi) → dừng, báo.
* Gặp điều gói không phủ (thiếu token / component con, `stuck` không giải thích được, kiểm mất hình có cờ B–D, buộc phải đổi look
  đã duyệt) → **dừng ở chỗ đó**, trả *Cần user quyết*; không tự quyết thay user.
* Đầu ra: báo cáo Bước 9, ảnh chụp lưu vào thư mục nháp, và **md cập nhật dạng đề xuất** (Trước → Sau) — không ghi repo.
  Phiên chính ghi qua approval gate, thêm DEC, gọi `/figma-sync` nếu màn đổi theo.

Song song: nhiều agent chạy pha 1 cùng lúc được (chỉ đọc). Pha 2 trong **cùng một file Figma** chạy tuần tự, mỗi lúc
một agent (luật không ghi song song).

## Constraints

### Luật cứng

* Không dựng khi chưa có spec đã duyệt trong `design.md` (DS v2: md ở `design-system/components/`).
* DS v2: component vẽ cùng chuyển động của nó, không để làm sau (`motion.md` mục 10.12).
* Không tạo component trùng cái thư viện đã có; không vẽ lại control; không sửa main component
  của thư viện.
* Không mã màu/cỡ/khoảng cách cứng khi đã có token.
* Không bịa nội dung nghiệp vụ; không bịa giá trị ở Known Gaps — hỏi, hoặc ghi "chưa có chuẩn trong
  design.md" (DS v2: "chưa có chuẩn trong design-system/").
* Không xoá node mình không tạo; không dựng bản thứ hai khi đã có.
* Thiết bị luôn hỏi user (`--propose`: thành một câu trong gói đề xuất). Không ghi song song (`figma_write` hay `use_figma`).
* `use_figma` chỉ cho việc `figma_write` không làm được (slot); mỗi lần dùng ghi vào báo cáo.
* **DS v2:** spec ghi ở `design-system/components/{base,application}/`, **không** ghi vào `design.md`. Không đặt instance Astryx vào
  component v2. Cha không đè fill / stroke / cỡ của component con.
* **`--propose`:** không hỏi, không ghi repo, không ghi Figma — chỉ trả gói đề xuất. **`--build`:** không hỏi; điều
  gói không phủ → dừng, trả *Cần user quyết*.

### Tuân thủ rule workspace

Skill này là "skill vẽ" theo nghĩa của `.claude/rules/design-system.md`: đọc `design/design.md` theo
mục (mục lục + mục luôn đọc + mục của `/figma-component` trong bảng của rule), tuân theo *Luật khi sinh màn*, dùng Do's and Don'ts làm tiêu chí tự kiểm, đụng
Known Gaps thì hỏi hoặc ghi "chưa có chuẩn trong design.md". Với DS v2, nguồn đọc theo mục *Chọn nguồn spec* (ngoại lệ
có chủ đích so với bảng của rule, tới khi chuyển hẳn sang DS v2). Ghi file qua `.claude/rules/approval-gate.md`
(plan preview, diff; agent con không ghi file đích trước approval).

## References

- Rule workspace `.claude/rules/design-system.md`.
- @.claude/rules/approval-gate.md (plan preview, diff; sub-agent không ghi file đích trước approval).
- DS v2: `design-system/architecture.md` (nhóm, luật lồng, tên, web/mobile, token, tài liệu, luật component) ·
  `design-system/foundations/README.md` · `design-system/tokens.json` · `design-system/components/README.md` (thư mục, cách ghi md) ·
  `design-system/components/{base,application}/*.md` (spec + tiền lệ) · `_workspace/decisions.md` +
  `.claude/rules/decision-log.md` · `.claude/rules/saas-layer.md` (nhãn tầng của khối nghiệp vụ).
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
- `--html`: khung trang `html-kit/review-page.html` + khuôn dữ liệu `html-kit/sample-page.json` · `_scripts/ds-component-page.py`
  (sinh trang) · `_scripts/ds-foundation-check.py` (gate vòng 3) · `_scripts/ref-untitled.sh` (code Untitled) · DEC-285.
- Khai giá trị: `_scripts/ds-css-split.py` (tách CSS khung màn, inline → class) · `ds-foundation-check.py --declare`.
- Đồng bộ Figma ↔ repo: `_scripts/figma-ds-snapshot.js` (chụp Figma, chỉ đọc) · `_scripts/ds-v2-sync-check.py` (gate sau
  mọi lần ghi Figma, `--status` bảng trạng thái).
- Agent review Bước 7 mục 12: `.claude/agents/visual-reviewer.md`, `.claude/agents/uxui-reviewer.md`, skill `accessibility-review`.
