# Setup Figma cho dự án mới: dùng design system Astryx

> Làm **một lần** khi bắt đầu dự án, trước lần chạy `/figma-screen` đầu tiên.
> Mục tiêu: file Figma của dự án dùng được **component thật** của Astryx (instance), chứ không
> phải khung tự vẽ. Nếu thiếu bước này, `/figma-screen` sẽ dừng ở Bước 3 ("chốt nơi vẽ") và hỏi lại.

## 0. Chọn cách làm

| | **Cách A: Thư viện dùng chung** | **Cách B: File dự án = bản sao Astryx** |
|---|---|---|
| Gói Figma | Cần quyền **publish thư viện** (thường là gói trả phí; kiểm ở Bước A1) | Gói nào cũng được, kể cả Starter miễn phí |
| File dự án | File mới, trống, **bật** thư viện Astryx | Bản duplicate của file Astryx, vẽ màn ở trang riêng |
| Nhiều dự án dùng chung một DS | Có. Mọi file nhận cập nhật từ một thư viện | Không. Mỗi dự án giữ một bản sao riêng |
| Cập nhật DS về sau | Publish lại thư viện, các file bấm "Update" | Phải chép tay hoặc làm lại bản sao |
| Mức đã kiểm với `/figma-screen` | **Chưa chạy thử** (xem Bước A4) | **Đã chạy thử** ngày 27/09/2026 |

**Chọn A** khi có từ 2 dự án trở lên hoặc team có gói trả phí. **Chọn B** khi làm một mình, dùng
gói miễn phí, hoặc cần bắt đầu ngay.

## 1. Chuẩn bị chung (cả hai cách)

1. **Figma Desktop** (bản trình duyệt không chạy được plugin cục bộ) và **Node.js 18+**.
2. **Reqwise Figma MCP** đã cài vào thư mục dự án, và plugin Reqwise đã được import vào Figma Desktop.
   Xem chương `02-cai-dat.md` trong bộ Kit.
3. Copy vào thư mục dự án mới, giữ nguyên cấu trúc:
   ```
   .claude/skills/                  ← 12 skill của Kit + figma-screen/
   .claude/rules/design-system.md   ← rule dùng design system
   design/design.md                   ← nguồn chuẩn
   design/design-tokens.css
   design/figma-library-keys.json     ← chỉ cần cho Cách A
   design/setup-figma.md              ← file này
   ```
4. Nếu có bản cập nhật, lấy file Astryx trên Figma Community vào **Drafts** hoặc project của team
   (nút *Open in Figma*). Tài liệu `design.md` được trích từ bản đang dùng:
   `fileKey FifpyOMpZk9OP8qyNzbRVJ`. Dùng lại **đúng file này** thì key trong
   `figma-library-keys.json` khớp; duplicate một bản mới thì phải sinh lại key (Mục 5).

## Cách A: Thư viện dùng chung

**A1. Kiểm quyền publish.** Mở file Astryx, vào panel **Assets** rồi bấm biểu tượng
**Libraries** (hình quyển sách). Nếu thấy nút **Publish** thì làm tiếp. Nếu nút bị khóa hoặc Figma
đòi nâng cấp, gói hiện tại không publish được: chuyển sang **Cách B**.

**A2. Đưa file vào đúng chỗ.** Thư viện phải nằm trong **project của team**, không phải Drafts cá
nhân, để thành viên khác bật được. Kéo file vào project, đặt tên dễ nhận, ví dụ `Astryx — Library`.

**A3. Publish.** Trong hộp Libraries, bấm **Publish**, rồi chọn publish cả **components, styles và
variables** (không bỏ variables, vì mọi màu và khoảng cách của Astryx là variable). Ghi mô tả
phiên bản, ví dụ "Astryx — bản trích 27/09/2026".

**A4. Tạo file dự án và bật thư viện.**
1. Tạo file Figma mới trong cùng team, đặt tên `<Tên dự án> — Design`.
2. Mở **Assets → Libraries** và bật **Astryx — Library**.
3. Tạo khung trang theo mục **Cấu trúc trang file dự án**, gồm trang module đầu tiên `01 · <Module>`.
4. Chạy plugin Reqwise trong file này, rồi làm **Mục 3 (Kiểm tra setup)**.

Cách A chưa được chạy thử với `/figma-screen`. Điểm cần xác nhận ở lần đầu: gắn token theo tên
(`fill: "$Text/Primary"`) có nhận **variable của thư viện** không, hay phải nạp variable trước. Nếu
bước kiểm tra báo lỗi ở token, hãy báo lại để cập nhật hướng dẫn và skill.

## Cách B: File dự án = bản sao Astryx

**B1. Tạo bản sao.** Trong Figma, chuột phải vào file Astryx rồi chọn **Duplicate**. Đổi tên bản sao
thành `<Tên dự án> — Design`. Không vẽ vào file gốc dùng để trích tài liệu.

**B2. Thêm trang cho màn hình.** Tạo các trang và dòng phân cách theo mục **Cấu trúc trang file dự
án**. Nội dung các trang thư viện (About, Foundation, Icons, Templates, Action… Table & List) gom về
nhóm DESIGN SYSTEMS theo mục *Design system: innvie và Astryx tách riêng*, **không sửa nội dung component**.
Đó là nơi chứa component chính (main component).

Đoạn này chỉ áp dụng cho gói Starter; gói Edu/Professional không giới hạn số trang. Gói Starter
giới hạn số trang mỗi file. Nếu Figma không cho thêm trang, có hai cách:
- xóa bớt trang thư viện mà dự án không dùng, ví dụ **Chat** (chỉ xóa khi chắc chắn không cần);
- hoặc vẽ màn trên trang **Templates**, trong một Section riêng tên `Screens · <tính năng>`.

**B3. Chạy plugin Reqwise** trong file bản sao, rồi làm **Mục 3**.

**Giới hạn của Cách B:** file dự án không nhận cập nhật khi Astryx đổi. Khi cần cập nhật, xem Mục 5.

## Cấu trúc trang file dự án (cả hai cách)

Thứ tự trang trong file dự án. Mỗi nhóm mở đầu bằng trang trống `---`, rồi trang tên nhóm viết hoa;
trang con thụt đầu dòng **5 dấu cách**. Nhóm DESIGN SYSTEMS có thêm dòng cấp 2 `——— NN · … ———`.

```
📘 Cover                      ← thumbnail: tên dự án, version, trạng thái
📍 Start here                 ← chú giải trạng thái, changelog, link SRS/Confluence, mục lục module
---
BA
     🧭 Sitemap & Flows       ← sitemap, userflow, sequence
---
SCREENS
     01 · <Module>            ← mỗi module một trang, ví dụ 01 · Quản lý xưởng
     02 · <Module>
---
WORK
     🧪 Sandbox               ← nháp, không handoff
     🗄 Archive               ← bản cũ, không xóa
---
DESIGN SYSTEMS
     innvie · Foundations     ← màu, chữ, icon, logo (Logo khách / Delta)
     innvie · Components      ← component dự án dùng thật: mỗi component 1 hàng, Web | Mobile cạnh nhau
     innvie · Patterns        ← khung trang, device frame, cây quy trình, splash, template đang dùng
     Astryx · Library         ← component Astryx chưa xếp, 1 trang, section theo nhóm cũ (Action, Overlay…)
```

**Design system: innvie và Astryx tách riêng** (DEC-103).
* `innvie · Components` chứa mọi component mà màn đang dùng: component dự án (`· innvie`) và component Astryx
  có instance trên trang màn. Mỗi component là một hàng (section trắng, title 112 là tên component), gồm
  hai cột cạnh nhau: `Web` và `Mobile` (cùng nền `#F2F2F2`, phân biệt bằng title), để chỉnh hai bản cùng lúc. Chỉ có
  một bản thì cột còn lại ghi "Chưa có bản Mobile/Web". Hàng xếp theo nhóm (Action, Form Controls,
  Navigation, Overlay, Container, Content, Feedback & Status, Layout, Table & List), trong nhóm theo ABC,
  **trải ngang từ trái sang phải, rộng quá khoảng 16.000px thì xuống dòng**; nhiều frame trong một cột
  Web/Mobile cũng đặt cạnh nhau. Các nhóm xếp thành lưới, cách nhau 1.000px.
* `Astryx · Library`: phần Astryx còn lại. Component không có instance nào trên trang màn (kể cả lồng trong
  component đang dùng) gom vào section `🗑 Không dùng — chờ duyệt xoá`; chỉ xoá sau khi user duyệt danh sách.
  Khi một component Astryx bắt đầu được dùng, chuyển main component sang `innvie · Components`.
* Chuyển main component giữa các trang không làm đứt instance. Chuyển xong thì sửa vị trí ghi trong
  `design/design.md` (dạng "trang …, khung … · innvie") cùng lượt.

Tìm trang theo tên thì so sánh sau khi `trim()` (bỏ dấu cách thụt đầu).

Cách A không có nhóm DESIGN SYSTEMS trong file dự án: các trang đó nằm ở file thư viện, cùng thứ tự.

**Trang Cover và Start here** (mẫu dựng sẵn trong file Astryx, 01/10/2026):
* **Cover:** khung `Thumbnail` 1920×1080, theo bìa gốc Astryx: nền collage thẻ UI (bản detach của `Center`),
  giữa là tên dự án (Cal Sans 180, màu wordmark Astryx) và một dòng: loại hệ thống · nền tảng · phiên bản ·
  ngày · người phụ trách. Bìa không ghi trạng thái; trạng thái theo feature, xem Start here. Khi tạo file dự án:
  sửa hai dòng chữ, rồi chuột phải khung → **Set as thumbnail** (Plugin API không làm được bước này). Bìa gốc
  của Astryx nằm ở trang Archive.
* **Start here:** năm khối — *Liên kết* (SRS/Confluence, Jira, design system, thư viện Figma), *Chú giải
  trạng thái* (Badge 🚧 Đang làm, 👀 Chờ duyệt, Ready for dev, Changed, 🗄 Archive), *Mục lục module*
  (tên trang có link tới trang), *Quy ước trong trang module*, *Changelog* (mới nhất ở trên). Thêm module thì
  thêm một dòng ở Mục lục; gửi duyệt hoặc sửa màn đã Ready for dev thì thêm một dòng Changelog.

**Thứ tự feature** (DEC-103). Số feature tăng dần, nên vị trí phải suy ra được từ PRD, không xếp theo ngày vẽ.
* Trang module theo cột *Theme* của bảng Feature Map (`docs/_product/prd.md` Mục 7):

  | Theme | Trang |
  |---|---|
  | Nền tảng, Quản trị và cấu hình | `00 · Chung` |
  | Bảo dưỡng sửa chữa | `01 · Quản lý xưởng` |
  | Nhân sự | `02 · Nhân sự` |
  | Quản lý phương tiện | `03 · Phương tiện` |
  | Quản lý dầu | `04 · Quản lý dầu` |
  | Danh mục › … | `05 · Danh mục` |
  | Điều phối vận tải | `06 · Điều phối vận tải` (tạo khi vẽ feature đầu tiên) |

  Theme mới chưa có trong bảng → hỏi user, tạo trang số tiếp theo, thêm dòng vào bảng này.
* Mã `Fxx` = số ở cột `#` của bảng Feature Map, 2 chữ số (`account-access` = `F01`, `cross-process-flow` =
  `F03`). Không đánh lại số. Feature chưa có trong Feature Map → hỏi user, thêm vào PRD trước rồi mới vẽ.
* Trong một trang, feature xếp **từ trên xuống** theo `Fxx` tăng dần, mép trái thẳng hàng (x = 0), cách
  nhau 1.000px. Chèn feature số nhỏ hơn vào giữa → dời cả khối các feature bên dưới xuống, không xếp ngang.
* Không để node nào nằm rời ngoài section feature. Component → trang DESIGN SYSTEMS; thử nghiệm → Sandbox.
* `Screens · Index`: mỗi feature một dòng `Fxx · <tên> · <trang> · <trạng thái>`, link tới section feature.

**Bên trong một trang module — 4 cấp section** (DEC-103). Section lồng nhau phân cấp bằng màu nền; title
là **text node đặt trong section**, font heading, cỡ đủ đọc khi zoom xa (nhãn tên section của Figma không
phóng to được). Màu dưới đây là màu canvas để đọc file, không phải token sản phẩm.

| Cấp | Tên section | Nền | Title | Ghi chú |
|---|---|---|---|---|
| L0 Feature | `Fxx · <tên feature> — <slug>` | `#E5E5E5` | 240, dưới là dòng phụ 64: `slug · trạng thái · link SRS · cập nhật dd/mm` | Trạng thái là tiền tố tên: `🚧` đang làm, `👀` chờ duyệt, `✅` đã chốt |
| L1 Khối | `Tài nguyên` · `Web` · `Mobile` (theo thứ tự này, chỉ tạo khối có nội dung) | `#F2F2F2` cho cả ba; title phân biệt khối | 160 | Mobile web 393 thuộc `Web`; `Mobile` dành cho app |
| L2 Flow | `Flow n · <slug flow> — <tên Việt>` | `#FFFFFF` | 112 | Thứ tự theo userflow Mục 3 của feature |
| L3 Cột màn × hàng case | (không phải section) | — | 64 (title cột, thanh hàng) | Xem *Bố cục trong Section flow* |

Chỉ dùng màu trung tính (xám, đen, trắng), không tô màu sắc cho section (DEC-104). Section `🗑 Không dùng — chờ
duyệt xoá` ở `Astryx · Library` nền `#D9D9D9`.

* **Tài nguyên** gồm 3 section L2: `Component phát sinh` (instance của component dự án sinh ra hoặc sửa vì
  feature này; main component vẫn nằm ở `innvie · Components`), `Icon dùng`, `Chip trạng thái dùng`
  (badge/status theo `srs/{feature}-states.md`). Mỗi mục có chú thích một dòng: dùng ở màn nào.
* **Hàng theo flow:** mỗi Section flow là một hàng: **userflow của flow ở cột trái**, khu màn của flow bên
  phải xếp thành **ma trận màn × case** (mục dưới). Người đọc thấy sơ đồ và màn của cùng một flow trên một hàng. Màn dùng chung nhiều flow vẽ ở
  flow đầu tiên dùng nó; các flow sau chỉ trỏ tới bằng userflow (`linkScreens`), không nhân bản frame.
* Đã chốt thì bấm **Ready for dev** (Dev Mode) trên section L0. Sửa sau khi đã Ready, Figma tự đổi sang *Changed*.

**Bố cục trong Section flow — ma trận màn × case** (DEC-185, DEC-186):
* Khu màn là một bảng: **mỗi màn có số là một cột**, **mỗi case là một hàng**. Đọc ngang hàng Luồng chính
  là đi hết luồng chính từ trái sang phải; đọc dọc một cột là mọi trạng thái của một màn.
* **Cột** = màn có số `[#]` ở userflow Mục 2 (kể cả state có số riêng), thứ tự theo cột *Màn hình gồm* của
  userflow Mục 3 (thứ tự đi), màn không có ở đó thì theo số. Đầu cột là title
  `<screenId> · <slug> — <tên Việt>` (tên Việt = cột *Màn hình* Mục 2), ví dụ
  `1.1 · web · record-detail — Màn chi tiết bản ghi có dòng quy trình`. Title là text, **không phải frame**,
  để `linkScreens` không khớp nhầm. Popup mở từ nơi chưa vẽ (màn ngoài feature) gom một cột cuối, title
  `Popups — mở từ <nơi mở>`.
* **Hàng** theo thứ tự `Luồng chính` · `Đang tải` · `Lỗi` · `Tình huống biên` · `Responsive` (chỉ desktop
  web). Hàng không có frame nào trong flow thì bỏ. Mỗi hàng mở đầu bằng **thanh hàng** trải hết bề rộng các
  cột: nền `#1F1F1F`, chữ trắng cỡ 64, chấm tròn màu case trước chữ (Luồng chính `#28A745`, Lỗi `#DC3545`,
  Tình huống biên `#FFC107`, Đang tải và Responsive `#8C8C8C`; cùng màu `classDef` của userflow). Thanh hàng
  là group (hình chữ nhật + chấm + chữ) tên `Hàng · <tên hàng>`, không phải frame.
* **Frame vào hàng nào:** state Loading, `<Khối> loading`, Submitting → `Đang tải`. Frame khác theo màu node
  của nó trong userflow Mục 1 (`class … happy` → Luồng chính, `error` → Lỗi, `edge` → Tình huống biên); node
  tìm theo nhãn `[n]` (frame chính) hoặc `[n] · <State>` (frame state). Frame không có node → cột *Hàng* của
  bảng từ vựng dưới. Màn chỉ có ở nhánh lỗi hoặc biên (vd popup lỗi) thì ô Luồng chính của cột đó để trống.
* **Nhiều frame trong một ô** xếp **dọc**, cách 100px, theo thứ tự node trong userflow. Modal (dialog,
  confirm, form nhỏ; frame cả màn có lớp phủ tối) không có số riêng nằm ở cột của màn mở ra nó, hàng theo
  case của modal. Ô `Responsive` xếp **ngang**: 1280, 1024 rồi mobile web 393 (DEC-324), cách 100px, chỉ state mặc định; 1920
  là frame ở hàng Luồng chính, không nhân bản. Mobile web 393 nằm trong Section `Web`, tên
  `<screenId> · <slug> · 393`; Section `Mobile` dành cho app.
* State vẽ ở 1920, cao theo nội dung. Frame cao thêm → tính lại toạ độ, dời cả cột và các hàng bên dưới;
  không để frame dính nhau hoặc cách lung tung.
* Frame `Ghi chú … · <nodeId>` đặt ngay dưới frame có nodeId đó, cách 100px.
* **Thẻ Spec** `Ghi chú · Spec · <nodeId>` (DEC-188, `.claude/rules/screen-source.md` Mục 9) đặt bên phải frame có
  nodeId đó, cách 40px, cùng mép trên; cột rộng thêm phần thẻ, ô cao bằng phần cao hơn giữa frame và thẻ. Thẻ trắng,
  viền `#D9D9D9`, bo 16, Inter; web rộng 720, mobile 400. **Lớp ghim** `Ghi chú · Ghim · <nodeId>` (group: khung nét
  đứt + số tròn ở góc trên trái mỗi phần tử) nằm đè lên frame nhưng là anh em của frame, không lồng vào; dời frame
  thì lớp ghim dời theo. Màu của lớp ghi chú: tím `#7B61FF`, chỉ dùng cho số và khung ghim.
* Dropdown, popover, menu bám vào một phần tử nằm **bên trong** frame màn, không tách ra ngoài.
* Toạ độ do máy tính, không ước bằng tay: `python3 _scripts/flow-matrix.py plan <feature> <flow> <frames.json>`
  (frames.json = con trực tiếp của Section flow) ra kế hoạch; `check` kiểm mọi frame đúng cột, đúng hàng.

| Thành phần | Vị trí |
|---|---|
| Title của section (L0 / L1 / L2) | cách mép trái và mép trên section 160 / 100 / 80px |
| Section con đầu tiên trong L0 | cách mép trên L0 600px; trong L1: 400px |
| Section L1 kế tiếp / L2 kế tiếp | cách section trước 400px / 300px; đệm phải và đệm dưới mỗi section 200px |
| Userflow của flow | cột trái Section flow: x = 200, y = 320 |
| Cột màn đầu tiên | cách mép phải userflow **400px** |
| Cột kế tiếp | cách mép phải cột trước **400px**; bề rộng cột = frame rộng nhất của cột (ô Responsive: 1280 + 100 + 1024 + 100 + 393) |
| Title cột | y = 320 trong Section flow; rộng bằng cột cộng khoảng trống tới cột kế, chừa 40px (cột cuối tính tới đệm phải); Inter 64 |
| Thanh hàng đầu tiên | y = 472, cao 120, từ mép trái cột đầu tới mép phải cột cuối; title cột xuống nhiều dòng (cột mobile hẹp) thì lùi xuống, cách đáy title cao nhất 40px |
| Frame đầu tiên của hàng | cách đáy thanh hàng 80px |
| Frame kế tiếp trong ô | cách frame trên 100px (ô Responsive: cách frame bên trái 100px) |
| Thẻ Spec | bên phải frame cách 40px, cùng mép trên; web rộng 720, mobile 400 |
| Thanh hàng kế tiếp | cách đáy frame thấp nhất của hàng trên 300px |

Vẽ thêm màn làm Section flow cao/rộng ra → nới section cha và dời các section bên dưới xuống, không để đè.

**Tên frame:**
Mọi frame bắt đầu bằng `<screenId> · <slug>`. Các phần ngăn bằng ` · ` (có dấu cách hai bên); số,
slug, tên Việt lấy từ userflow Mục 2 theo `.claude/rules/naming-conventions.md` mục *Màn hình & flow*.

* Frame chính (đầu cột, state mặc định): **3 phần** `<[#]> · <web|mob> · <slug>`, ví dụ
  `1.1 · web · process-line`.
* Frame state và modal không có số riêng: **4 phần** `<screenId> · <slug> · <tên tiếng Anh>`, ví dụ
  `1.1 · web · process-line · Loading`, `1.1 · web · process-line · Confirm delete`. Tên tiếng Anh viết
  hoa chữ đầu, 2–3 từ, theo bảng từ vựng dưới.
* State có số riêng trong userflow Mục 2 (có chuyển màn riêng ở Mục 3.5) là màn riêng: 3 phần với
  số và slug của nó (`1.3 · web · process-line-error`), có cột riêng như mọi màn có số.
* Không để `Frame 123`, `state 2`; không có dấu cách thừa đầu tên frame (tên trang module vẫn cố ý thụt).
* **Frame thuộc màn nào:** tách tên theo ` · `. Phần 1 là số, phần 2 là thiết bị, phần 3 là slug,
  phần 4 (nếu có) là state/modal. So **từng phần**, không so chuỗi con (`1.1` không khớp `11.1`,
  `1.10`). Vị trí dùng để kiểm chéo theo ma trận: cùng cột là cùng màn (title cột ghi `screenId`), hàng
  cho biết case. Thẻ Spec và lớp ghim kết thúc bằng nodeId của frame (không phải screenId) nên không khớp
  nhầm vào màn. Frame tên bắt đầu bằng `Ghi chú` /
  `Note` là ghi chú, không tính là state. Skill đọc frame (`/prototype-html`, `@usability-reviewer`)
  khớp theo luật này.

**Bảng từ vựng tên state.** Tình huống mới chưa có trong bảng thì đặt theo mẫu *Danh từ + tính chất*,
rồi thêm một dòng vào bảng. Cột *Hàng* là hàng của frame trong ma trận khi frame không có node trong
userflow (Loading và Submitting luôn ở hàng Đang tải).

| Tình huống | Tên | Hàng |
|---|---|---|
| Đang tải | Loading | Đang tải |
| Tải lỗi | Load error | Lỗi |
| Một khối trong màn tải lỗi | `<Block> load error` (vd History load error) | Lỗi |
| Rỗng, chưa có dữ liệu | Empty | Tình huống biên |
| Tìm không ra | No search results | Tình huống biên |
| Lọc không ra | No filter results | Tình huống biên |
| Không có quyền xem | No permission | Lỗi |
| Bị chặn khi mở | Open denied | Lỗi |
| Banner dữ liệu vừa cập nhật | Update banner | Tình huống biên |
| Chỉ xem | Read-only | Tình huống biên |
| Đang sửa | Edit | Luồng chính |
| Đang gửi | Submitting | Đang tải |
| Bản ghi đã xoá | Record deleted | Lỗi |
| Modal | `<Đối tượng> <loại>`: Process diagram, Step sheet, Confirm delete | theo userflow |
| Popup lỗi nghiệp vụ | Theo nguyên nhân: Step already requested, Source revoked | Lỗi |

**Mã màn (`screenId`):** `<[#]> · web` hoặc `<[#]> · mob`, ví dụ `1.1 · web · process-line`,
`1.1 · mob · process-line` (web và mobile cùng màn chung số + slug). Desktop, Tablet, Responsive dùng
`web`; Mobile dùng `mob`. Userflow nối màn theo `screenId`, nên `screenId` phải ghi đủ thiết bị
(`1.1 · web`); ghi `1.1` sẽ khớp nhầm cả bản `mob`.

## 3. Kiểm tra setup (cả hai cách)

Mở Claude Code trong thư mục dự án, mở file dự án trên Figma, chạy plugin Reqwise, rồi nói:

> *Kiểm tra setup Figma cho /figma-screen theo design/setup-figma.md mục 3.*

Claude sẽ tạo một frame tạm ở góc xa canvas, thử 4 việc dưới đây rồi **xóa frame đó**:

| # | Thử | Đạt khi |
|---|---|---|
| 1 | `figma_status` | Plugin kết nối, đúng tên file dự án |
| 2 | Tạo frame với `fill: "$Core/Background Surface"`, `tokens: { padding: "Spacing/4" }` | Không báo "unknown token" |
| 3 | Tạo chữ với `textStyle: "Heading/Heading 1"`, `fill: "$Text/Primary"` | Không báo "unknown style" |
| 4 | Tạo `Button` rồi đặt `Size: "MD"`, `Variant: "Secondary"`, `Label: "Lưu"`. Cách B dùng `figma.instantiate("Button")`; Cách A dùng `figma.getLibraryComponent(<key Button trong figma-library-keys.json>)` rồi instantiate theo id | Instance tạo ra, thuộc tính đặt được |

Đạt cả 4 thì setup xong. Trượt mục nào thì xem Mục 6.

## 4. Sau khi setup

* Vẽ màn: `/figma-screen <màn hoặc tính năng>`.
* Chưa có userflow cho luồng nhiều màn: chạy `/figma-userflow` trước.
* Không sửa component chính trong file dự án. Muốn đổi component thì đổi ở thư viện (Cách A) hoặc
  ghi đề xuất vào `design/design.md` (Iteration Guide), qua duyệt, rồi mới sửa.

## 5. Khi Astryx có bản mới

| | Việc cần làm |
|---|---|
| Cách A | Cập nhật file thư viện, rồi **Publish** lại. Ở file dự án: Assets, bấm **Update** khi Figma báo có cập nhật |
| Cách B | Duplicate bản Astryx mới, rồi chép các trang module (nhóm `SCREENS`), trang `Sitemap & Flows` và `Archive` từ file cũ sang (copy/paste frame). Instance dán sang **chưa chắc** tự trỏ vào component của file mới; phải kiểm từng loại và swap tay nếu cần. Việc này tốn công, nên dự án dài hơi thì nên chọn Cách A ngay từ đầu |
| Cả hai | Trích lại token vào `design/design.md` và `design/design-tokens.css` cùng lượt, qua duyệt. Nếu dùng file Astryx khác, nhờ Claude sinh lại `design/figma-library-keys.json` (đọc `get_design_system_kit` của file thư viện) |

### 5.1 Áp lại các sửa của dự án sau khi đồng bộ

Bản Astryx mới sẽ trả file về mặc định của thư viện. Sau khi cập nhật (Cách A: ở file thư viện; Cách
B: ở bản sao mới), áp lại các sửa sau, rồi kiểm bằng mục 3. Nhờ Claude chạy qua Figma MCP được.

| # | Sửa | Chi tiết | Lý do |
|---|---|---|---|
| 1 | Font | Biến `Font Family/Heading` = Cal Sans, `Font Family/Body` = Inter. Text style `Display/*`, `Heading/Heading 1–3` → Cal Sans Regular; còn lại → Inter (giữ weight) | Figtree thiếu dấu tiếng Việt |
| 2 | Gắn biến cỡ chữ | 13 text style (trừ `Text/Code`): `fontSize` → `Font Size/*`, `lineHeight` → `Line Height/*` theo bảng Typography của `design.md` | Đổi font làm mất liên kết biến |
| 3 | Radius | `Radius/None` = 0 | Code Neutral = 0; thư viện để 4 |
| 4 | Toast | Nền default → `Core/Background Inverted`, chữ → `Core/On Accent`; nền error → `Status/Error Inverted`, chữ → `Text/On Dark` | Thư viện dùng mã cứng #1c2024 / #ce2c31 |
| 5 | Elevation | Biến `Effects/Elevation {Low,Medium,High} {1,2,Ring}` (Light/Dark) và effect style `Elevation/*` = 2 drop shadow + 1 inner shadow 1px theo `{elevation.*}` / `{elevation-dark.*}` | Thư viện theo core cũ, không có bộ Dark |
| 6 | TextInput sm/lg | Nối lại lớp `description`, `startIcon`, `placeholder`, `statusMessage`, `statusText` với thuộc tính cùng tên (như biến thể md) cho 16 biến thể sm/lg | Thư viện chỉ nối ở md: tắt `statusMessage`/`startIcon` trên instance sm không có tác dụng |

Sau khi áp, ghi ngày vào `CHANGELOG.md` của kit.

## 6. Lỗi thường gặp

| Triệu chứng | Nguyên nhân thường gặp | Cách xử lý |
|---|---|---|
| `figma_status` báo plugin chưa kết nối | Chưa chạy plugin trong file đang mở, hoặc đang dùng Figma trên trình duyệt | Mở Figma Desktop, mở file, chạy plugin Reqwise |
| Lệnh nhắm sai file | Mở nhiều cửa sổ Figma có plugin | Đóng bớt, hoặc nói rõ tên file khi yêu cầu |
| "unknown token/style" (mục 3.2, 3.3) | Cách A: variable/style chưa publish hoặc chưa bật thư viện. Cách B: nhầm file | Publish kèm variables (A3), bật thư viện (A4); kiểm đúng file bản sao |
| `findComponent("Button")` không ra (Cách A) | Hàm này chỉ tìm component **trong file**; component thư viện phải nạp bằng key | Dùng `getLibraryComponent(key)` với key trong `figma-library-keys.json` |
| `getLibraryComponent` báo không tìm thấy key | Thư viện được publish từ một bản duplicate khác, nên key khác | Sinh lại `figma-library-keys.json` từ đúng file thư viện (Mục 5) |
| Không tạo được trang mới | Giới hạn trang của gói | Xem B2 |
| Nút vừa tạo có icon lạ, cỡ nhỏ | Mặc định thư viện là SM và bật Icon | Bình thường: `/figma-screen` tự đặt `Size: "MD"`, `Icon: false` (xem *Tên trong Figma* trong `design.md`) |
