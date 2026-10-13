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
án**. Các trang thư viện (About, Foundation, Icons, Templates, Action… Table & List) chỉ **đổi vị
trí** vào nhóm DESIGN SYSTEMS, **không đổi tên, không sửa nội dung**. Đó là nơi chứa component chính (main
component).

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
——— 01 · FOUNDATIONS ———
     About · Foundation · Icons
——— 02 · COMPONENTS ———
     Action · Chat · Container · Content · Feedback & Status · Form Controls · Layout ·
     Navigation · Overlay · Table & List · Utility
——— 03 · PATTERNS ———
     Templates
```

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

**Bên trong một trang module:**
* Mỗi feature là một Section `Fxx · <tên feature>`, ví dụ `F01 · Lập kế hoạch chuyến`.
* Trong feature có hai Section con `Web` và `Mobile` (chỉ tạo phần có màn).
* Trạng thái feature: tiền tố tên Section `🚧` (đang làm), `👀` (chờ duyệt); đã chốt thì bấm
  **Ready for dev** (Dev Mode). Sửa sau khi đã Ready, Figma tự đổi sang *Changed*.

**Bố cục trong Section con:**
* Mỗi màn là một **nhóm**, có thanh title rộng bằng cả nhóm, ghi `<screenId> · <slug> — States`.
  Thanh title là text/rectangle, **không phải frame**, để `linkScreens` không khớp nhầm. Nhóm
  responsive riêng có title `<screenId> · <slug> — Responsive`.
* State của màn xếp **dọc** dưới frame chính, cách nhau 100px. State vẽ ở 1920, cao theo nội dung;
  sửa nội dung xong thì canh lại khoảng cách cả cột, không để frame dính nhau hoặc cách lung tung.
* Modal (dialog, confirm, form nhỏ) đặt **bên phải màn mở ra nó**, cách 100px. Frame modal là cả màn
  có lớp phủ tối và modal ở trên. Nhiều modal nối tiếp sang phải; state của modal xếp dọc dưới modal.
* Dropdown, popover, menu bám vào một phần tử nằm **bên trong** frame màn, không tách ra ngoài.
* Nhóm responsive: 1920 và 1440 xếp ngang cách 100px, cùng cao cố định 1080, chỉ vẽ cho state mặc
  định. Mobile 393 nằm ở Section con `Mobile`.

| Thành phần | Vị trí |
|---|---|
| Nhóm đầu tiên | cách mép trái section 200px |
| Title của nhóm | cách mép trên section 200px |
| Frame đầu tiên của nhóm | cách mép trên section 352px (ngay dưới title) |
| Frame kế tiếp cùng hàng (modal, breakpoint) | cách frame trước 100px |
| Frame kế tiếp trong cột (state) | cách frame trên 100px |
| Nhóm kế tiếp | cách mép phải nhóm trước **400px** |

**Tên frame:**
* Frame chính (đầu cột, state mặc định): `<screenId> · <slug>`, ví dụ `3.1-web · danh-sach-chuyen`.
* Frame state và modal: tên ngắn **tiếng Anh**, viết hoa chữ đầu, 2–3 từ, nói đúng nó là gì:
  `Empty`, `Loading`, `Error`, `Read-only`, `Approve order`. Không lặp `screenId`.
* Không để `Frame 123`, `state 2`; không có dấu cách thừa đầu tên frame (tên trang module vẫn cố ý thụt).
* **Frame thuộc màn nào:** theo nhóm. Frame không có `screenId` thuộc frame chính của nhóm chứa nó;
  cùng cột với frame chính là state, bên phải là modal (cột dưới modal là state của modal). Skill đọc
  frame (`/prototype-html`, `@usability-reviewer`) khớp theo luật này. Frame cũ còn hậu tố
  `· rỗng` / `· đang tải` / `· lỗi` vẫn được nhận là state của `screenId` đó.

**Mã màn:** `<số>-web` hoặc `<số>-mob`, ví dụ `3.1-web · danh-sach-chuyen`, `3.1-mob · danh-sach-chuyen`.
Desktop, Tablet, Responsive dùng `-web`; Mobile 375 dùng `-mob`. Userflow nối màn theo **tên chứa**
`screenId`, nên `screenId` trong userflow phải ghi đủ hậu tố (`3.1-web`); ghi `3.1` sẽ khớp nhầm cả
`3.1-mob` và `3.10-web`.

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
