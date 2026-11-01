---
type: design-architecture
status: draft
updated: 2026-10-30
links:
  - _workspace/decisions.md
  - design-system/foundations/README.md
  - design-system/tokens.json
  - design/design.md
  - design/setup-figma.md
  - .claude/rules/design-system.md
---


# Design System v2 — kiến trúc

> Kết quả vòng 1/6 (kiến trúc), chốt 16/10/2026 trên trang phỏng vấn
> https://claude.ai/artifact/D5KS1PPdUih9dsajBo48vU. Mỗi mục dẫn mã DEC trong `_workspace/decisions.md`.
> Vòng 2/6 (nền tảng) chốt 17/10: `design-system/foundations/README.md` (luật) + `design-system/tokens.json` (nguồn máy), DEC-119…139.
> Từ 26/10 DS v2 dựng lại theo Untitled UI v8, chia **Base** rồi **Application**, bỏ quy ước cấp L0–L3 (DEC-260, DEC-312).
> Trong lúc dựng, DS v2 nằm ở `design-system/`. Skill vẫn đọc bộ cũ `design/design.md` tới khi chuyển hẳn (vòng 6).

## 1. Phạm vi

- Một design system cho sản phẩm Invlogis (SaaS logistics bán nhiều khách, DEC-003), dùng cho web và app mobile.
- Component không mang thương hiệu khách. Đổi giao diện theo khách đi qua tầng token (Mục 7).
- Nhìn của bộ cũ không ràng buộc bộ mới (DEC-109: muốn nhìn mới hẳn). Các quyết định nhìn đã chốt trước đây
  (web 12/10, mobile DEC-096…107, màu nhấn DEC-041/042) là đầu vào để giữ hoặc bỏ ở từng vòng, không tự áp.
- Nguồn tham chiếu (DEC-128, DEC-129): app theo Apple HIG và Material 3; web theo Atlassian (hệ dựng ra Jira), Material 3 cho
  web thích ứng, WCAG 2.2 cho trợ năng; Tailwind, Ant Design chỉ để đối chiếu. Chi tiết: `foundations.md` mục 1.


## 2. Lộ trình (DEC-108, DEC-260)

| Vòng | Nội dung | Ra |
|---|---|---|
| 1 · Kiến trúc | Quy ước tên, cấu trúc file, lịch làm | DEC-108…118, file này |
| 2 · Nền tảng | Hướng nhìn, màu ba tầng, chữ (font, thang cỡ, độ đậm theo cỡ), khoảng cách, bo góc, bóng, lưới, canh lề | `foundations.md`, `tokens.json` → `tokens.css`, trang DS · Foundations (xong 17/10) |
| 3 · Icon | Bộ nền, icon nghiệp vụ logistics, cỡ, độ dày nét, tên, bảng theo hành động · đối tượng · trạng thái | `icons.md`, trang ✦ DS · Icons (xong 17/10) |
| 4 · Base components | Component nguyên thuỷ theo Untitled (Buttons, Badges, Tags, Avatars, Inputs, Select, Tooltips…), đủ biến thể × trạng thái | Trang DS · Base components, `components/base/*.md` |
| 5 · Application components, golden | Khối ứng dụng (điều hướng, bảng, header, upload) và khối nghiệp vụ logistics (phương tiện, tổ hợp), màn mẫu, bộ golden cho AI | Trang DS · Application components, `components/application/*.md`, `golden/` |
| 6 · Quy trình, bàn giao | Rule, skill, kiểm bằng máy, chuẩn bàn giao, đổi instance trên màn cũ, xoá bộ cũ | `.claude/rules`, skill, script kiểm |

Mỗi vòng: phỏng vấn có xem trước → dựng trên Figma → review (agent soi riêng, rồi user duyệt) → ghi tài liệu và DEC.

## 3. Cách chuyển sang bộ mới (DEC-109, DEC-110, DEC-111)

- Dựng bộ mới song song trên trang riêng, cùng file Figma `[innvie] invlogis v0.3` (fileKey `FifpyOMpZk9OP8qyNzbRVJ`).
- Không sửa bộ cũ, trừ lỗi chặn. Không vẽ màn mới tới khi DS v2 xong (DEC-111).
- Chuyển (vòng 6): script đổi instance trên màn sang bộ mới theo bảng ánh xạ cũ → mới, soát ảnh trước và sau
  từng màn. Xong thì xoá bộ cũ (`Astryx · Library`, `innvie · Foundations`, `innvie · Components`,
  `innvie · Patterns`, 18 collection theme Astryx, bộ biến Lab) sau khi user duyệt danh sách.
- Repo: bộ mới ở `design-system/` (file này, nền tảng, token CSS, `components/`, `golden/`, `icons/`). Lúc chuyển thì
  đưa lên `design/` thay bộ cũ, sửa `.claude/rules/design-system.md` và các skill trong cùng lượt.
- Tách thư viện: khi DS v2 ổn định, chuyển nhóm trang DS sang file thư viện publish. Figma cho cắt–dán main
  component sang file thư viện rồi publish mà instance vẫn giữ liên kết; thử trên một component trước khi làm thật.
  Cần gói Figma có quyền publish thư viện (chưa xác nhận).

Trang Figma của DS v2, nằm trong nhóm `——— 03 · DESIGN SYSTEM ———`, tên thụt 5 dấu cách:

```
     DS · Foundations              token theo 10 collection (mục 7), chữ, lưới
     ✦ DS · Icons
     DS · Base components          mỗi họ một Section: component + 1 màn web + 1 màn app để duyệt (DEC-260)
     DS · Application components   như trên, cho khối ứng dụng và nghiệp vụ
     ⭐ Golden                      màn mẫu cho AI (vòng 5)
     🗑 DS · Deprecated             bộ cũ dồn về đây lúc chuyển, chờ duyệt xoá
```

## 4. Hai nhóm component (DEC-260, DEC-312)

| Nhóm | Định nghĩa | Ví dụ |
|---|---|---|
| Base | Component nguyên thuỷ theo Untitled UI, không mang nghiệp vụ, chữ giữ chỗ trung tính | Buttons, Badges, Tags, Avatars, Checkboxes, Radio, Toggles, Inputs, Select, Multi-select, Tooltips, Featured icon |
| Application | Khối ứng dụng ráp từ Base; gồm cả khối nghiệp vụ logistics dùng lại ở nhiều màn | Sidebar navigation, Header navigation, Tables, File upload, Vehicle card, Combo figure |

- Danh sách làm và để sau: DEC-260. Quan hệ cha dùng con nào, foundation nào: `components/_deps.json` (máy dò,
  `_scripts/ds-deps.py`), con hoặc foundation đổi thì cha `stale` (DEC-292, DEC-302, `.claude/rules/ds-stale.md`).

**Luật lồng:**

| | Luật |
|---|---|
| a | Lồng bằng instance của component gốc, không sao chép, không vẽ lại thứ component khác đã có |
| b | Cha khoá cấu hình được phép bằng preferred values (Slot, Instance swap) và đưa thuộc tính của instance lồng ra panel (expose nested instances); cấu hình được phép ghi trong tài liệu của cha |
| c | Token của component lồng giữ nguyên; cha chỉ quyết khoảng cách quanh nó. Cần cỡ mới thì thêm biến thể ở component gốc, không ghi đè |
| d | Phụ thuộc một chiều, không vòng |
| e | Phần con chỉ dùng bên trong một component đặt tên bắt đầu `_` hoặc `.` (không publish, ẩn khỏi Assets) |

**Bàn giao cho dev:** Base = thư viện UI dùng chung (đủ biến thể, trạng thái, token, trợ năng); Application = component của
ứng dụng, dữ liệu và quy tắc hiển thị lấy từ SRS. Cấu trúc bộ bàn giao: DEC-255, `design-system/handoff/`.

## 5. Tên (DEC-113, DEC-260)

- Tên component, tên thuộc tính và giá trị thuộc tính bằng tiếng Anh. Mô tả component, tài liệu và chữ trên màn bằng tiếng Việt.
- Tên thuộc tính theo Untitled, giá trị viết hoa: `Hierarchy=Primary, Size=MD, Icon=Leading, State=Hover, Destructive=False` (DEC-260 F11).
- Thuộc tính không phải biến thể (chữ, bật/tắt, đổi icon) đặt tên tiếng Anh, viết hoa chữ đầu (`Label`, `Has Icon`, `Icon`).
- Tên trang và section trên Figma giữ tiếng Việt.

## 6. Web và mobile (DEC-114)

- Collection `Platform` (chế độ Web, Mobile) chứa số đo khác nhau giữa hai nền tảng: cao control, bo góc, cỡ chữ, khoảng cách.
  Khung màn đặt chế độ một lần, mọi instance bên trong tự đổi.
- Xếp mỗi component vào 1 nhóm (DEC-279). **A Dùng chung**: cùng phần, cùng cách thao tác, chỉ khác số đo → một bộ, số đo
  theo mode `Platform`, không có trục nền tảng. **B Lệch**: khác cấu tạo hoặc cách thao tác (menu ↔ bottom sheet, popover ↔
  action sheet) → một bộ có trục `Platform=Web|Mobile`, cùng tên thuộc tính. **C Một nền tảng**: một bộ, mô tả ghi nền tảng
  kia dùng gì thay. Phần con chỉ có trên app thì thêm tiền tố `_`.
- Code: cùng component, token đổi theo nền tảng (vd thuộc tính `data-platform` trên khung trang).

## 7. Token (DEC-115, DEC-116, DEC-257, DEC-313)

Theo đúng 10 collection trên Figma (`tokens.json` › `figma.collections`; Platform trong `tokens.json` là một nhóm, Figma tách 5):

| Tầng | Collection Figma | Chế độ | Chứa | Được trỏ tới |
|---|---|---|---|---|
| Primitive | `0. Primitives` | Value | Bảng màu, thang `space/<px>`, `radius/<px>` (tên theo px, DEC-135, DEC-315) | Chỉ tầng Semantic |
| Semantic | `1. Semantic` | Light, Dark | Màu theo nghĩa: `color/bg/*`, `color/text/*`, `color/action/*`, `color/status/*`… | Component, màn |
| Semantic | `2. Platform · Radius` · `3. Platform · Spacing & Layout` · `4. Platform · Typography` · `5. Platform · Sizes` | Web, Mobile | Thang Untitled `radius/*`, `space/*`, `size/*` (DEC-314, DEC-315) và token theo vai: `radius/card`, `layout/screen-inset`, `type/body/size`, `control/height/md` | Component, màn |
| Theo khách | `7. Brand` | 8 dải | `color/brand/50…950`, chỉ vào các vai ở `foundations.md` mục 3.5 | Component, màn (theo vai) |
| Component | `6. Platform · Component sizes` | Web, Mobile | Số đo riêng còn lại của component, **đang gộp về token chung** (DEC-319): còn 59 token chờ đợt 2, sổ `components/_token-ledger.json` | Chính component đó |
| Thương hiệu | `9. Brand · Invlogis` | Value | Màu logo Invlogis, innvie (DEC-261) | Trang giới thiệu, tài liệu; **không** dùng trong component sản phẩm |

- Component và màn **không gắn Primitives, không mã màu trần, không số trần** (foundations mục 12). Primitive màu, khoảng
  cách, bo góc chỉ để tầng Semantic trỏ tới (DEC-315).
- **Màu: component gắn thẳng token Semantic** (`color/*`) hoặc accent theo vai, không có tầng màu riêng của component
  (DEC-318). **Số đo:** token `6. Platform · Component sizes` chỉ trỏ Semantic (`2.`–`5.`) (DEC-313). Chưa có token Semantic
  đúng vai thì thêm vào Semantic, không trỏ tắt. Máy kiểm: `python3 _scripts/ds-token-usage.py --check`.
- Collection Context đã bỏ (DEC-258); khe vòng focus là `color/focus/gap` ở Semantic.
- Tên và giá trị token: `design-system/foundations/README.md` (luật dùng) và `design-system/tokens.json` (nguồn máy; `tokens.css` sinh bằng
  `python3 _scripts/ds-v2-tokens.py`). Rà token ↔ component định kỳ: `python3 _scripts/ds-token-usage.py` (trang review).
- Tầng Semantic có chế độ Tối ngay từ đầu; giá trị Tối điền và kiểm ở một vòng sau (DEC-116, bản nháp DEC-257).
- Nút chính than chì (DEC-119). Màu khách theo dải riêng của từng khách, kiểu chạm nhẹ, chỉ vào các vai ở
  `foundations.md` mục 3.5; vòng focus, viền đang gõ giữ than chì (DEC-167…170, thay DEC-041, DEC-042).

## 8. Golden data set (DEC-117)

- Mỗi mục là một màn đã duyệt cho một mẫu màn × nền tảng × trạng thái, gồm: mã `G-{nền tảng}-{mẫu}-{nn}` (vd `G-M-LIST-01`),
  node Figma (bản đông cứng trên trang ⭐ Golden, chú thích đánh số), ảnh, cây lắp (vùng → component, thuộc tính đã đặt,
  token khoảng cách), luật đã áp, lỗi hay gặp kèm cách sửa, khi dùng và khi không dùng, nguồn (feature, màn, DEC).
- Kho: Figma trang ⭐ Golden; repo `design/golden/{mã}/` (`shot.png`, `entry.json`, `notes.md`) và chỉ mục
  `design/golden/index.json`. Trong lúc dựng: `design-system/golden/`.
- Cách dùng: khi vẽ màn mới, /figma-screen tìm mục gần nhất theo mẫu màn, nền tảng, trạng thái → clone khung → thay nội dung → kiểm như thường.
- Danh sách v1 chốt ở vòng 5. Đề xuất: danh sách, chi tiết, form một màn, form nhiều bước, màn kết quả, sheet chọn, xác nhận,
  bảng điều khiển; web và mobile; mặc định, rỗng, đang tải, lỗi.


## 9. Tài liệu từng component (DEC-118)

- Figma: mỗi họ component một Section trên trang Base / Application, kèm 1 màn web + 1 màn app để duyệt (DEC-260 F12).
  Ghi chú và tài liệu trên Figma viết sau cùng, khi component đã duyệt.
- Hình mẫu nằm trong **ô mẫu** nền thật của component, luôn có viền; máy kiểm "mất hình" (nền thân so với nền ô, khe vòng
  focus, Hover / Pressed so với Default, ngưỡng 1,1:1) chạy trước khi trình. Kết quả ghi ở mục `### Kiểm máy` cuối mỗi phần
  của md, không đặt hộp kết quả trên Figma.
- Repo: `design-system/components/{base|application}/{slug}.md`: khối **Web** rồi khối **Mobile**, rồi phần máy. Phần máy sinh từ
  Figma bằng `_scripts/ds-v2-component-doc.py`; một md chứa được nhiều khối máy có tên (`<!-- auto:begin web -->` …
  `<!-- auto:end web -->`, chọn bằng `--block web`). Phần tả, nên và không nên do người viết. Phần con chỉ dùng bên trong ghi
  trong file của component cha. Mục "Được dùng trong" (component cha còn tồn tại) và "Thành phần lồng".
- Trong lúc brainstorm, component sống ở `design-system/components/_work/{slug}/` (trang review, `page.json`), chốt xong mới ghi md.
- Vòng đời: Nháp → Đang review → Ổn định → Ngừng dùng.
- Phiên bản `x.y.z`: z sửa nhìn hoặc lỗi, không đổi thuộc tính · y thêm biến thể hoặc thuộc tính, màn cũ vẫn đúng ·
  x đổi tên hoặc bỏ thuộc tính, màn phải sửa (báo trước, có script đổi).
- `design.md` của bộ mới chỉ giữ quy tắc chung (nền tảng, bố cục, chữ trên màn, trợ năng). Lịch sử đổi ghi ở `_workspace/changelog.md`.
- Đợt 1 làm đủ các mục ngay (DEC-183): thuộc tính và token do script sinh từ Figma; khi dùng, nên và không nên do Claude viết,
  user duyệt, mỗi component 2 cặp nên / không nên có hình; thêm mục **chấm điểm trợ năng** theo benchmark (WCAG 2.2) để
  thấy chỗ còn cần cải thiện.

## 10. Ảnh hưởng tới việc đang có

| Việc | Xử lý |
|---|---|
| Vẽ account-access trên Figma (Flow 4–8 web, app 393, responsive) | Tạm dừng (DEC-111); vẽ tiếp bằng bộ mới |
| Đợt thử /figma-proto-check account-access Flow 1–3 | Giữ nguyên sổ đợt thử; quyết cách xử lý ở vòng 4 (user chọn "để sau", 16/10) |
| BL-161 áp chốt Lab ↔ DS mobile lên bộ cũ | Không làm trên bộ cũ; nội dung DEC-096…099 là đầu vào vòng 2–4 |
| BL-169 duyệt xoá phần Astryx thừa | Làm ở vòng 6, cùng lúc xoá bộ cũ |
| BL-175 phần lọc của ô tìm mobile | Chốt khi dựng ô tìm ở đợt 2 của vòng 4 (DEC-171) |
| BL-176 đổi 12 màn mobile cross-process-flow | Làm ở vòng 6, khi đổi instance sang bộ mới |
| Skill dựa trên design system (/figma-screen, /figma-component, /figma-audit, /figma-design-system, /prototype-html, /figma-proto-check, /wireframe-html) và `.claude/rules/design-system.md` | Sửa ở vòng 6 |


## 11. Luật component chung còn hiệu lực

| Chủ đề | Luật | DEC |
|---|---|---|
| Trục biến thể | Tên thuộc tính theo Untitled (mục 5); State = Default · Hover (chỉ web) · Pressed · Focus · Disabled, thêm Loading, Error, Read Only, Selected khi component có | DEC-172, DEC-260 |
| Cao control | `control/height/*` web 28 · 32 · 40 | DEC-173, DEC-260 F7 |
| Màu trạng thái | Gắn thẳng Semantic theo trạng thái (`color/action/*-hover`, `-pressed`, `color/bg/disabled`…); Disabled một kiểu xám, không làm mờ | DEC-174, DEC-318 |
| Nút | 5 kiểu Primary · Secondary · Ghost · Danger (nền đỏ nhạt, chữ đỏ) · Outline; Outline dùng chung thang trạng thái của Secondary | DEC-176, DEC-313 |
| Vòng focus | Outline 2px cách 2 như code Untitled; khe là `color/focus/gap` | DEC-260 F9, DEC-258 |
| Lồng góc, lề đều | Khung lớn tách xa (bo ≤ lề), khung ôm đồng tâm; máy đo kiểm trước khi trình | DEC-165 |
| Theo nền tảng | Nhóm A Dùng chung · B Lệch (trục `Platform`) · C Một nền tảng | DEC-279 |

## 12. Còn mở

- Gói Figma của team có quyền publish thư viện không (DEC-110).
- Gỡ trên Figma các component L0/L1 cũ và biến `card/*`, `list-row/*` (DEC-312); dọn collection theme Astryx, Lab,
  `zz · Platform cũ`, `Thử · vòng 4` sau khi quét không còn layer gắn.
