---
type: design-architecture
status: draft
updated: 2026-10-20
links:
  - _workspace/decisions.md
  - design/v2/foundations.md
  - design/v2/tokens.json
  - design/design.md
  - design/setup-figma.md
  - .claude/rules/design-system.md
---

# Design System v2 — kiến trúc

> Kết quả vòng 1/6 (kiến trúc), chốt 16/10/2026 trên trang phỏng vấn
> https://claude.ai/artifact/D5KS1PPdUih9dsajBo48vU. Mỗi mục dẫn mã DEC trong `_workspace/decisions.md`.
> Vòng 2/6 (nền tảng) chốt 17/10: `design/v2/foundations.md` (luật) + `design/v2/tokens.json` (nguồn máy), DEC-119…139.
> Vòng 4/6 (L0, L1) chốt luật component 18–20/10: DEC-171…184, DEC-200…213, DEC-231…246, tóm tắt ở mục 11.
> Trong lúc dựng, DS v2 nằm ở `design/v2/`. Skill vẫn đọc bộ cũ `design/design.md` tới khi chuyển hẳn (vòng 6).

## 1. Phạm vi

- Một design system cho sản phẩm Invlogis (SaaS logistics bán nhiều khách, DEC-003), dùng cho web và app mobile.
- Component không mang thương hiệu khách. Đổi giao diện theo khách đi qua tầng token (Mục 7).
- Nhìn của bộ cũ không ràng buộc bộ mới (DEC-109: muốn nhìn mới hẳn). Các quyết định nhìn đã chốt trước đây
  (web 12/10, mobile DEC-096…107, màu nhấn DEC-041/042) là đầu vào để giữ hoặc bỏ ở từng vòng, không tự áp.
- Nguồn tham chiếu (DEC-128, DEC-129): app theo Apple HIG và Material 3; web theo Atlassian (hệ dựng ra Jira), Material 3 cho
  web thích ứng, WCAG 2.2 cho trợ năng; Tailwind, Ant Design chỉ để đối chiếu. Chi tiết: `foundations.md` mục 1.

## 2. Lộ trình (DEC-108)

| Vòng | Nội dung | Ra |
|---|---|---|
| 1 · Kiến trúc | Cấp L0–L3, quy ước tên, cấu trúc file, lịch làm | DEC-108…118, file này |
| 2 · Nền tảng | Hướng nhìn, màu ba tầng, chữ (font, thang cỡ, độ đậm theo cỡ), khoảng cách, bo góc, bóng, lưới, canh lề | `foundations.md`, `tokens.json` → `tokens.css`, trang 🎨 DS · Foundations (xong 17/10) |
| 3 · Icon | Bộ nền, icon nghiệp vụ logistics, cỡ, độ dày nét, tên, bảng theo hành động · đối tượng · trạng thái | `icons.md`, trang ✦ DS · Icons (xong 17/10) |
| 4 · L0 và L1 | 5 component có trên mọi màn trước, đủ biến thể × trạng thái, rồi phần còn lại | Trang L0, L1, tài liệu từng component |
| 5 · L2, L3, golden | Component nghiệp vụ dựng trên L1, màn mẫu, bộ golden cho AI | Trang L2, L3 · Golden, `golden/` |
| 6 · Quy trình, bàn giao | Rule, skill, kiểm bằng máy, chuẩn bàn giao từng cấp, đổi instance trên màn cũ, xoá bộ cũ | `.claude/rules`, skill, script kiểm |

Mỗi vòng: phỏng vấn có xem trước → dựng trên Figma → review (agent soi riêng, rồi user duyệt) → ghi tài liệu và DEC.

## 3. Cách chuyển sang bộ mới (DEC-109, DEC-110, DEC-111)

- Dựng bộ mới song song trên trang riêng, cùng file Figma `[innvie] invlogis v0.3` (fileKey `FifpyOMpZk9OP8qyNzbRVJ`).
- Không sửa bộ cũ, trừ lỗi chặn. Không vẽ màn mới tới khi DS v2 xong (DEC-111).
- Chuyển (vòng 6): script đổi instance trên màn sang bộ mới theo bảng ánh xạ cũ → mới, soát ảnh trước và sau
  từng màn. Xong thì xoá bộ cũ (`Astryx · Library`, `innvie · Foundations`, `innvie · Components`,
  `innvie · Patterns`, 18 collection theme Astryx, bộ biến Lab) sau khi user duyệt danh sách.
- Repo: bộ mới ở `design/v2/` (file này, nền tảng, token CSS, `components/`, `golden/`, `icons/`). Lúc chuyển thì
  đưa lên `design/` thay bộ cũ, sửa `.claude/rules/design-system.md` và các skill trong cùng lượt.
- Tách thư viện: khi DS v2 ổn định, chuyển nhóm trang DS sang file thư viện publish. Figma cho cắt–dán main
  component sang file thư viện rồi publish mà instance vẫn giữ liên kết; thử trên một component trước khi làm thật.
  Cần gói Figma có quyền publish thư viện (chưa xác nhận).

Trang Figma của DS v2, nằm trong nhóm `——— 03 · DESIGN SYSTEM ———`, tên thụt 5 dấu cách:

```
     📖 DS · Bắt đầu        cấp, quy ước tên, phiên bản, changelog
     🎨 DS · Foundations    token 3 tầng, chữ, lưới
     ✦ DS · Icons
     DS · Components · L0–L3  ma trận component: L0, L1, L2 và tài liệu cùng một trang (DEC-213, DEC-245)
     ⭐ L3 · Golden          màn mẫu cho AI
     🗑 DS · Deprecated      bộ cũ dồn về đây lúc chuyển, chờ duyệt xoá
```

**Ma trận component (DEC-213, DEC-245):** trang `DS · Components · L0–L3` xếp hàng = họ component (Button, Status Chip,
Text Field kèm OTP Field, Avatar kèm Avatar Group, Tooltip, Card, List Item, Progress), cột = **L0 · L1 · L2 · Tài liệu**. Mỗi
ô cột là một Section `{Họ} · L0 · Element`, `{Họ} · L1 · Component Base`, `{Họ} · L2 · Content Component`,
`{Họ} · Tài liệu`. Không có cột L3 (màn mẫu ở trang `⭐ L3 · Golden`) và không có cột Xem nhanh. L0 khoá (tên bắt đầu `.`).
Hàng của component dùng lại component khác có dòng "Dùng lại: …" trỏ sang hàng gốc, không vẽ lại (Mục 4, luật lồng g). Hàng
List Row đã bỏ (DEC-231); dòng danh sách là hàng List Item (DEC-232).

## 4. Bốn cấp (DEC-112)

Định nghĩa theo lời user:

| Cấp | Định nghĩa | Mẫu tên | Ví dụ |
|---|---|---|---|
| L0 Element | Cấu phần tạo nên component, không dùng riêng lẻ (khoá); đặt một mình lên màn không đủ nghĩa. Dùng chung được nhiều họ khi tên mang họ riêng (DEC-254) | `.{cha} / {Tên}` | `.card / Media`, `.button / Spinner`, `.progress / Bar`, `.transport-order / Route Row` |
| L1 Base | Không mang ngữ cảnh, là cấu trúc UI nguyên thuỷ, tuỳ biến được để dùng ở nhiều ngữ cảnh (vd thẻ dọc, thẻ ngang) | `Base / {Tên}` | `Base / Card`, `Base / Selectable Card`, `Base / Button`, `Base / List Item` |
| L2 Content | Mang ngữ cảnh, dùng ở đúng một ngữ cảnh (vd hotel card dùng hai thẻ nền dọc và ngang, thêm ngữ cảnh hotel) | `{Đối tượng} / {Tên}` | `Transport Order / Card` (Layout = Horizontal \| Vertical), `Vehicle / Card`, `Notification / Item` |
| L3 Screen | Màn hoàn chỉnh | `{mã màn} · {nền tảng} · {slug}` | `2.1 · mob · order-list`, `1.3 · web · sign-in` |

- Tiền tố dấu chấm làm Figma không publish component đó (ẩn khỏi Assets). L0 khoá trên canvas.
- Element của Base đặt tên theo Base (`.card / …`); Element của Content đặt tên theo đối tượng (`.transport-order / …`).

**Xếp cấp — hỏi lần lượt:**

1. Có ai dùng riêng nó trên màn không? Không → L0 của component cha, kể cả khi nó có mặt ở nhiều màn nhưng chỉ qua cha.
   Có → L1, kể cả khi nó cũng nằm trong component khác: nút ở chân thẻ vẫn là `Base / Button` (DEC-233a).
   Phép thử: đặt một mình lên màn có đủ nghĩa không (vd thanh tiến độ không chữ → không, nên là L0 `.progress / Bar`, DEC-254).
2. Nó có mang dữ liệu hay nghĩa nghiệp vụ không (tên trường, đối tượng, quy tắc)? Có → L2, đặt dưới đối tượng nghiệp vụ.
3. Không mang nghiệp vụ và đã dùng ở 2 ngữ cảnh trở lên? Có → L1 Base.
4. Không mang nghiệp vụ nhưng mới có 1 ngữ cảnh? Để trong L2 của ngữ cảnh đó. Có ngữ cảnh thứ 2 thì tách phần chung lên L1.

Nâng, hạ cấp: L2 cần ở ngữ cảnh thứ 2 → tách phần chung thành L1 mới, L2 cũ dựng lại trên L1 đó. L1 chỉ còn dùng trong một
component cha → hạ thành L0 của cha.

**Luật lắp (máy kiểm ở vòng 6):**

| Cấp | Được chứa | Không được |
|---|---|---|
| L0 | Hình, chữ, icon, L0 cùng họ | Dùng ngoài component cha; chứa L1 (DEC-233c) |
| L1 | L0 của mình, L1 khác (instance của component gốc), icon | Mã màu trần, dữ liệu nghiệp vụ, sao chép L1 khác, vòng phụ thuộc |
| L2 | L1, L0 của chính nó | Detach, tự vẽ lại thứ L1 đã có |
| L3 | L2, L1, khung bố cục | L0 trực tiếp, detach, mã màu trần |

**Luật lồng component (DEC-233, sửa DEC-213 "mọi L1 ráp từ L0" thành "L1 ráp từ L0 và L1 khác"):**

| | Luật |
|---|---|
| a | Tầng theo vai trò dùng, không theo chỗ đặt: component dùng riêng được (Button, Status Chip, Avatar, Tooltip, Text Field) luôn là L1 kể cả khi nằm trong component khác. L0 chỉ cho phần không dùng riêng và thuộc một họ |
| b | Lồng bằng instance của component gốc (`Base / Button`…), không sao chép, không tạo `.card / Button` |
| c | L0 không bao giờ chứa L1. Vùng chứa L1 trong component cha là Slot của L1 cha (chân thẻ = Slot `Footer` của `Base / Record Card`, canh phải, cách `card/action-gap`, nhận `Base / Button`); không có L0 `.card / Footer` |
| d | Cha khoá cấu hình được phép bằng preferred values (Slot, Instance swap) và đưa thuộc tính của instance lồng ra panel (expose nested instances); cấu hình được phép ghi trong tài liệu của cha. Slot nhận được cả icon (hàng nghìn bộ) thì để mở và ghi quy ước ở tài liệu (`Base / List Item`, DEC-232) |
| e | Token của component lồng giữ nguyên; cha chỉ quyết khoảng cách quanh nó. Cần cỡ mới thì thêm biến thể ở component gốc, không ghi đè. Ngoại lệ: lớp Ảnh của `.card / Media` vì ảnh là nội dung (DEC-237) |
| f | Phụ thuộc một chiều, không vòng: L0 → L1 → L2; L1 được chứa L1 khác |
| g | Ma trận: hàng của cha có dòng "Dùng lại: …" trỏ sang hàng component gốc, không vẽ lại. Tài liệu cha, mục Cấu tạo: nhãn chỉ vào phần lồng ghi "Base / Button · SM · Secondary → xem tài liệu Button", không lặp token của nó |

**Phần tuỳ biến của L1 (DEC-175, DEC-233d):** chỗ nhỏ mở bằng thuộc tính (Text, Boolean, Instance swap); vùng chứa nhiều phần mở
bằng Slot của Figma (ô trống có danh sách component được phép, vd Slot `Footer` của `Base / Record Card` chỉ nhận
`Base / Button` 1–2 nút, Slot `Rows` nhận `.card / Row` và `Base / Status Row`, Slot `Start Content` và `End Content` của
`Base / List Item`, Slot `Segments` của `Base / Progress`). L2 lấp slot bằng nội dung nghiệp vụ. Slot đã dùng ở `Base / Card`,
`Base / Record Card`, `Base / Summary Card`, `Base / Selectable Card` (Slot `Body`), `Base / List Item`, `Base / Progress`.

**Bàn giao cho dev theo cấp:**

| Cấp | Phía code | Dev nhận gì |
|---|---|---|
| L0 | Thành phần con bên trong component, không export | Không bàn giao riêng |
| L1 | Thư viện UI dùng chung | Đủ biến thể, trạng thái, token, trợ năng |
| L2 | Component của feature | L1 dùng bên trong, dữ liệu và quy tắc hiển thị lấy từ SRS |
| L3 | Trang, route | Màn đủ trạng thái và luồng (userflow) |

## 5. Tên (DEC-113)

- Tên component, tên thuộc tính và giá trị thuộc tính bằng tiếng Anh. Mô tả component, tài liệu và chữ trên màn bằng tiếng Việt.
- Biến thể theo dạng ảnh tham khảo bước 4: `Type=Primary, Size=MD, State=Hover`. Bộ trục chuẩn và giá trị chuẩn: mục 11 (DEC-172).
- Thuộc tính không phải biến thể (chữ, bật/tắt, đổi icon) đặt tên tiếng Anh, viết hoa chữ đầu (`Label`, `Has Icon`, `Icon`).
- Tên đối tượng ở L2 lấy từ cột tên tiếng Anh sẽ thêm vào `docs/_shared/object-map.md` (vòng 5).
- Tên trang và section trên Figma giữ tiếng Việt.

## 6. Web và mobile (DEC-114)

- Collection `Platform` (chế độ Web, Mobile) chứa số đo khác nhau giữa hai nền tảng: cao control, bo góc, cỡ chữ, khoảng cách.
  Khung màn đặt chế độ một lần, mọi instance bên trong tự đổi.
- Xếp mỗi component vào 1 nhóm (DEC-279). **A Dùng chung**: cùng phần, cùng cách thao tác, chỉ khác số đo → một bộ, số đo
  theo mode `Platform`, không có trục nền tảng. **B Lệch**: khác cấu tạo hoặc cách thao tác (menu ↔ bottom sheet, popover ↔
  action sheet) → một bộ có trục `Platform=Web|Mobile`, cùng tên thuộc tính. **C Một nền tảng**: một bộ, mô tả ghi nền tảng
  kia dùng gì thay. Phần con chỉ có trên app thì thêm tiền tố `_`.
- Code: cùng component, token đổi theo nền tảng (vd thuộc tính `data-platform` trên khung trang).

## 7. Token (DEC-115, DEC-116)

| Collection | Chế độ | Chứa | Ví dụ tên |
|---|---|---|---|
| Primitives | 1 | Giá trị thô: bảng màu, thang số | `neutral/900`, `space/16` (tên theo px, DEC-135) |
| Semantic | Light, Dark | Nghĩa của giá trị | `color/action/primary`, `color/text/secondary` |
| Platform | Web, Mobile | Số đo theo nền tảng | `radius/card`, `type/body/size`, `control/height/md` (DEC-173) |
| Component | 1 | Chỉ cho component nhiều trạng thái (Button, ô nhập, chip…) | `button/bg/primary` |
| Context | Surface, Canvas | Màu đổi theo nền của khung chứa (DEC-241) | `focus/gap` |

- Component chỉ gắn token tầng Semantic, Platform, Component hoặc Context. Không gắn thẳng Primitives, không mã màu trần.
- `Context` (DEC-241): khe vòng focus `focus/gap` = trắng (Surface, mặc định) hoặc xám canvas (Canvas). Khung, màn, ô mẫu nền
  xám đặt explicit mode Canvas một lần, như mode Platform. Code: `data-context="canvas"` trên khung nền xám.
- Tên và giá trị token: `design/v2/foundations.md` (luật dùng) và `design/v2/tokens.json` (nguồn máy; `tokens.css` sinh bằng
  `python3 _scripts/ds-v2-tokens.py`).
- Tầng Semantic có chế độ Tối ngay từ đầu; giá trị Tối điền và kiểm ở một vòng sau (DEC-116).
- Nút chính than chì (DEC-119). Màu khách theo dải riêng của từng khách, kiểu chạm nhẹ, chỉ vào các vai ở
  `foundations.md` mục 3.5; vòng focus, viền đang gõ giữ than chì (DEC-167…170, thay DEC-041, DEC-042).

## 8. Golden data set (DEC-117)

- Mỗi mục là một màn đã duyệt cho một mẫu màn × nền tảng × trạng thái, gồm: mã `G-{nền tảng}-{mẫu}-{nn}` (vd `G-M-LIST-01`),
  node Figma (bản đông cứng trên trang ⭐ L3 · Golden, chú thích đánh số), ảnh, cây lắp (vùng → component, thuộc tính đã đặt,
  token khoảng cách), luật đã áp, lỗi hay gặp kèm cách sửa, khi dùng và khi không dùng, nguồn (feature, màn, DEC).
- Kho: Figma trang ⭐ L3 · Golden; repo `design/golden/{mã}/` (`shot.png`, `entry.json`, `notes.md`) và chỉ mục
  `design/golden/index.json`. Trong lúc dựng: `design/v2/golden/`.
- Cách dùng: khi vẽ màn mới, /figma-screen tìm mục gần nhất theo mẫu màn, nền tảng, trạng thái → clone khung → thay nội dung → kiểm như thường.
- Danh sách v1 chốt ở vòng 5. Đề xuất: danh sách, chi tiết, form một màn, form nhiều bước, màn kết quả, sheet chọn, xác nhận,
  bảng điều khiển; web và mobile; mặc định, rỗng, đang tải, lỗi.

## 9. Tài liệu từng component (DEC-118)

- Figma (khuôn mới, DEC-245; chi tiết `design/v2/components/README.md`): khung `Tài liệu · {Tên}` nằm trong Section
  `{Họ} · Tài liệu` của hàng component trên ma trận (cột Tài liệu), nền trắng, hai khối **Web** và **Mobile** dàn ngang (mỗi
  khối đặt mode Platform; component chỉ có một nền tảng thì một khối). Mỗi khối: tổng quan · cấu tạo (hình phóng có nhãn số
  `phần · token = số`) · biến thể · trạng thái · kích thước · nên và không nên (có hình) · trợ năng (chấm riêng web, app) ·
  thuộc tính · token · thành phần lồng · được dùng trong. Dòng nhỏ đầu khung thống nhất `L1 · BASE · TÀI LIỆU COMPONENT`; tên ·
  cấp · phiên bản · trạng thái · người phụ trách ở đầu khung.
- Hình mẫu nằm trong **ô mẫu** nền thật của component, luôn có viền; máy kiểm "mất hình" (nền thân so với nền ô, khe vòng
  focus, Hover / Pressed so với Default, ngưỡng 1,1:1) chạy trước khi trình. Kết quả ghi ở mục `### Kiểm máy` cuối mỗi phần
  của md, không đặt hộp kết quả trên Figma.
- Repo: `design/components/{l1|l2}/{tên}.md` (trong lúc dựng: `design/v2/components/`): `## Web`, `## Mobile`, rồi phần máy.
  Phần máy sinh từ Figma bằng `_scripts/ds-v2-component-doc.py`; một md chứa được nhiều khối máy có tên
  (`<!-- auto:begin web -->` … `<!-- auto:end web -->`, chọn bằng `--block web`), khối không tên giữ cú pháp cũ. Text Field
  là một md, hai khối `web` (Base / Text Field) và `mobile` (Base / Text Field / Mobile). Phần tả, nên và không nên do người
  viết. L0 ghi trong file của component cha. "Dùng ở đâu" theo nghiệp vụ bỏ, thay bằng "Được dùng trong" (component cha còn
  tồn tại) và "Thành phần lồng" (DEC-233d, g).
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

## 11. Luật component vòng 4 (DEC-165, DEC-171…184, DEC-200…213, DEC-231…246)

| Chủ đề | Luật | DEC |
|---|---|---|
| Đợt dựng | Đợt 1 theo thứ tự phụ thuộc: `Base / Button` → `Base / Status Chip` → `Base / Text Field` (+ `/ Mobile`) → `Base / List Item` → `Base / Card` và thẻ L1, kèm `Base / Avatar`, `Base / Avatar Group`, `Base / Tooltip`; bổ sung L1 trước khi dựng L2: `Base / Progress Card` (thanh là L0 `.progress / Bar`, DEC-254), `Base / OTP Field`. Đợt 2: ô tìm và phần lọc, tab, dialog, bottom sheet, bảng, menu, `Base / Stepper` | DEC-171, DEC-231, DEC-232, DEC-243, DEC-244, DEC-254 |
| Luật lồng | Dùng riêng được thì là L1 kể cả khi nằm trong component khác; lồng bằng instance gốc; L0 không chứa L1; vùng chứa L1 là Slot của L1 cha; phụ thuộc một chiều L0 → L1 → L2 (Mục 4) | DEC-233 |
| Trục biến thể | `Type · Size · State`; State = Default · Hover (chỉ web) · Pressed · Focus · Disabled; thêm Loading, Error, Read Only, Selected khi component có; Tone cho chip; chữ, icon, bật tắt là thuộc tính | DEC-172 |
| Cao control | `control/height/sm · md · lg`: web 28 · 32 · 40, app 36 · 42 · 52 | DEC-173 |
| Màu trạng thái | Token riêng tầng Component cho từng trạng thái; Disabled một kiểu xám, không làm mờ | DEC-174 |
| Nút | 5 kiểu Primary · Secondary · Ghost · Danger (nền đỏ nhạt, chữ đỏ) · Outline; một nút chính mỗi vùng; thứ tự DEC-88; nút icon là `Content=Icon Only` của `Base / Button` (DEC-197); đang tải: vòng quay + nhãn; không khoá nút gửi form. Outline đặt trên nền xám: Hover neutral/300, Pressed neutral/400, Focus nền trong suốt, Disabled giữ viền | DEC-176, DEC-177, DEC-197, DEC-240 |
| Vòng focus | L0 `.focus / Ring` dùng chung; khe giữa control và vòng là `focus/gap` theo collection Context (Surface · Canvas) | DEC-198, DEC-241 |
| Ô nhập | Hai component: web nhãn trên ô, app nhãn trong ô; gợi ý và lỗi dưới ô; viền `color/border/input`; nhìn theo cột "Bản chốt" Figma 6234:13999. Ô mã 6 chữ số của app là `Base / OTP Field` (L1, chỉ Mobile) | DEC-178, DEC-179, DEC-184, DEC-244 |
| Chip trạng thái | Trạng thái chính nền nhạt + icon (mỗi bản ghi một chip); trạng thái phụ, chỗ dày dùng chấm; Size MD 24 (mặc định) · SM 16 cho đầu thẻ, nhãn tối đa 160 | DEC-180, DEC-200, DEC-239 |
| Avatar · Tooltip | `Base / Avatar` Initials · Image · Icon · Upload × SM 24 … XXL 88, chấm trạng thái, nút đổi ảnh, State Focus chỉ ở nút đổi ảnh và ô Upload; `Base / Avatar Group` lùi đè số âm; Tooltip chỉ web | DEC-201…206, DEC-242 |
| Thẻ | `Base / Card` là khung (Slot `Content`; State Default · Hover · Pressed · Focus · Selected · Disabled; Padding None · Compact · Default · Spacious; Elevation None · Low · Med · High; Tone Surface · Muted · Dashed); thẻ L1 `Base / Record Card` (Header → Rows → Related → Slot `Footer`), `Base / Summary Card`, `Base / Selectable Card` ráp trên khung; `Base / Status Row`; không có Nav Card; thẻ có ngữ cảnh là L2 | DEC-181 (đã thay), DEC-211, DEC-234, DEC-235, DEC-237 |
| Thẻ khi nhấn | Nền neutral/300, viền neutral/400, chữ phụ neutral/600; Selectable chưa chọn + Disabled: vòng icon, ruột radio nền trắng | DEC-238 |
| Thẻ chọn | `Base / Selectable Card`: Selected × State; đang chọn viền 1px, radio tô kín, vòng icon nền xám (trắng ở nền nhấn); mở Has Avatar · Has Media · Has Body; nhìn theo cột "Bản chốt" Figma 6234:13999 | DEC-184, DEC-236 |
| Dòng danh sách | `Base / List Item` chung web và app (State 6 × Align 2); đầu dòng `Start Content` (≤ 1) và cuối dòng `End Content` (≤ 2) là Slot mở, quy ước chỉ nhận Avatar, Status Chip, Button, icon; Hover neutral/100; cao theo nội dung, tối thiểu 52 app, 36 web. Hàng List Row và 4 kiểu dòng đã bỏ | DEC-182 (đã thay), DEC-231, DEC-232 |
| Thanh tiến độ | `Base / Progress` Bar · Segmented × MD 6 · SM 4, không mang chữ, rộng mặc định 320 web · 361 app; Astryx không có, thiết kế riêng | DEC-243 |
| Lồng góc, lề đều | Khung lớn tách xa (bo ≤ lề), khung ôm đồng tâm; máy đo kiểm trước khi trình | DEC-165 |
| Chữ mẫu | L1 trung tính, không ngữ cảnh: Tooltip "Thêm", Avatar "Họ tên", Text Field Label · Placeholder · Value · Helper text · Error text | DEC-246 |
| Tài liệu | Đủ mục DEC-118 từ đợt 1, có mục chấm điểm trợ năng; khuôn Web và Mobile, ô mẫu nền thật, kiểm máy mất hình; ma trận 4 cột L0 · L1 · L2 · Tài liệu | DEC-183, DEC-245 |

## 12. Còn mở

- Gói Figma của team có quyền publish thư viện không (DEC-110).
- Trục Density của Astryx chưa dựng cho `Base / Card`, thẻ L1, `Base / List Item` (chưa chốt).
- Lý do bỏ hàng List Row, bỏ Nav Card ("trùng Navigation Row" không còn đứng khi Navigation Row bị bỏ), bỏ cột Xem nhanh và L3
  chưa ghi (DEC-231, DEC-235, DEC-245): chờ user xác nhận.
- `Vehicle / Option Card` (L2) chờ user chọn mẫu lab m4 (DEC-237).
