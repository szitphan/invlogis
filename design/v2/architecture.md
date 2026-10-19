---
type: design-architecture
status: draft
updated: 2026-10-19
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
> Vòng 4/6 (L0, L1) chốt luật component 18–19/10: DEC-171…184, tóm tắt ở mục 11.
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
     L0 · Elements          khoá, ẩn khi publish
     L1 · Base
     L2 · Content           gom theo đối tượng nghiệp vụ
     ⭐ L3 · Golden          màn mẫu cho AI
     🗑 DS · Deprecated      bộ cũ dồn về đây lúc chuyển, chờ duyệt xoá
```

## 4. Bốn cấp (DEC-112)

Định nghĩa theo lời user:

| Cấp | Định nghĩa | Mẫu tên | Ví dụ |
|---|---|---|---|
| L0 Element | Cấu phần tạo nên component, không dùng riêng lẻ (khoá) | `.{cha} / {Tên}` | `.card / Media`, `.button / Spinner`, `.transport-order / Route Row` |
| L1 Base | Không mang ngữ cảnh, là cấu trúc UI nguyên thuỷ, tuỳ biến được để dùng ở nhiều ngữ cảnh (vd thẻ dọc, thẻ ngang) | `Base / {Tên}` | `Base / Card / Vertical`, `Base / Card / Horizontal`, `Base / Button`, `Base / List Row` |
| L2 Content | Mang ngữ cảnh, dùng ở đúng một ngữ cảnh (vd hotel card dùng hai thẻ nền dọc và ngang, thêm ngữ cảnh hotel) | `{Đối tượng} / {Tên}` | `Transport Order / Card` (Layout = Horizontal \| Vertical), `Vehicle / Card`, `Notification / Item` |
| L3 Screen | Màn hoàn chỉnh | `{mã màn} · {nền tảng} · {slug}` | `2.1 · mob · order-list`, `1.3 · web · sign-in` |

- Tiền tố dấu chấm làm Figma không publish component đó (ẩn khỏi Assets). L0 khoá trên canvas.
- Element của Base đặt tên theo Base (`.card / …`); Element của Content đặt tên theo đối tượng (`.transport-order / …`).

**Xếp cấp — hỏi lần lượt:**

1. Có ai dùng riêng nó trên màn không? Không → L0 của component cha, kể cả khi nó có mặt ở nhiều màn nhưng chỉ qua cha.
2. Nó có mang dữ liệu hay nghĩa nghiệp vụ không (tên trường, đối tượng, quy tắc)? Có → L2, đặt dưới đối tượng nghiệp vụ.
3. Không mang nghiệp vụ và đã dùng ở 2 ngữ cảnh trở lên? Có → L1 Base.
4. Không mang nghiệp vụ nhưng mới có 1 ngữ cảnh? Để trong L2 của ngữ cảnh đó. Có ngữ cảnh thứ 2 thì tách phần chung lên L1.

Nâng, hạ cấp: L2 cần ở ngữ cảnh thứ 2 → tách phần chung thành L1 mới, L2 cũ dựng lại trên L1 đó. L1 chỉ còn dùng trong một
component cha → hạ thành L0 của cha.

**Luật lắp (máy kiểm ở vòng 6):**

| Cấp | Được chứa | Không được |
|---|---|---|
| L0 | Hình, chữ, icon, L0 cùng họ | Dùng ngoài component cha |
| L1 | L0 của mình, L1 khác, icon | Mã màu trần, dữ liệu nghiệp vụ |
| L2 | L1, L0 của chính nó | Detach, tự vẽ lại thứ L1 đã có |
| L3 | L2, L1, khung bố cục | L0 trực tiếp, detach, mã màu trần |

**Phần tuỳ biến của L1 (DEC-175):** chỗ nhỏ mở bằng thuộc tính (Text, Boolean, Instance swap); vùng chứa nhiều phần mở
bằng Slot của Figma (ô trống có danh sách component được phép, vd ô Leading của `Base / List Row` chỉ nhận Avatar, icon
trong ô 24, vòng icon 36, ảnh nhỏ). L2 lấp slot bằng nội dung nghiệp vụ. Thử Slot trên `Base / List Row` trước, ổn mới
dùng cho `Base / Card`.

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
- Cùng cấu tạo → một component. Khác cấu tạo → tách, tên thêm hậu tố nền tảng (vd `Base / Text Field` và `Base / Text Field / Mobile`).
- Code: cùng component, token đổi theo nền tảng (vd thuộc tính `data-platform` trên khung trang).

## 7. Token (DEC-115, DEC-116)

| Collection | Chế độ | Chứa | Ví dụ tên |
|---|---|---|---|
| Primitives | 1 | Giá trị thô: bảng màu, thang số | `neutral/900`, `space/16` (tên theo px, DEC-135) |
| Semantic | Light, Dark | Nghĩa của giá trị | `color/action/primary`, `color/text/secondary` |
| Platform | Web, Mobile | Số đo theo nền tảng | `radius/card`, `type/body/size`, `control/height/md` (DEC-173) |
| Component | 1 | Chỉ cho component nhiều trạng thái (Button, ô nhập, chip…) | `button/bg/primary` |

- Component chỉ gắn token tầng Semantic, Platform hoặc Component. Không gắn thẳng Primitives, không mã màu trần.
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

- Figma: khung tài liệu ngay cạnh component, gồm tên · cấp · phiên bản · trạng thái · người phụ trách · khi dùng ·
  nên và không nên (có hình) · cấu tạo (chú thích token) · thuộc tính · trạng thái hiển thị · trợ năng · chữ trên
  component · dùng ở đâu · tên trong code.
- Repo: `design/components/{l1|l2}/{tên}.md` (trong lúc dựng: `design/v2/components/`). Phần thuộc tính máy sinh từ Figma;
  phần khi dùng, nên và không nên do người viết. L0 ghi trong file của component cha.
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

## 11. Luật component vòng 4 (DEC-165, DEC-171…184)

| Chủ đề | Luật | DEC |
|---|---|---|
| Đợt dựng | Đợt 1 theo thứ tự phụ thuộc: `Base / Button` → `Base / Status Chip` → `Base / Text Field` (+ `/ Mobile`) → `Base / List Row` → `Base / Card`, kèm `Base / Avatar`. Đợt 2: ô tìm và phần lọc, tab, dialog, bottom sheet, bảng, menu | DEC-171 |
| Trục biến thể | `Type · Size · State`; State = Default · Hover (chỉ web) · Pressed · Focus · Disabled; thêm Loading, Error, Read Only, Selected khi component có; Tone cho chip; chữ, icon, bật tắt là thuộc tính | DEC-172 |
| Cao control | `control/height/sm · md · lg`: web 28 · 32 · 40, app 36 · 42 · 52 | DEC-173 |
| Màu trạng thái | Token riêng tầng Component cho từng trạng thái; Disabled một kiểu xám, không làm mờ | DEC-174 |
| Nút | 5 kiểu Primary · Secondary · Ghost · Danger (nền đỏ nhạt, chữ đỏ) · Outline; một nút chính mỗi vùng; thứ tự DEC-088; nút icon là `Type=Icon Only` của `Base / Button`; đang tải: vòng quay + nhãn; không khoá nút gửi form | DEC-176, DEC-177 |
| Ô nhập | Hai component: web nhãn trên ô, app nhãn trong ô; gợi ý và lỗi dưới ô; viền `color/border/input`; nhìn theo cột "Bản chốt" Figma 6234:13999 | DEC-178, DEC-179, DEC-184 |
| Chip trạng thái | Trạng thái chính nền nhạt + icon (mỗi bản ghi một chip); trạng thái phụ, chỗ dày dùng chấm | DEC-180 |
| Thẻ | `Base / Card` có phần lắp sẵn `.card / Header · Row · Related · Footer`; State có Selected; 9 loại thẻ cũ thành L2 | DEC-181 |
| Thẻ chọn | Đang chọn: viền 1px, radio tô kín, vòng icon nền xám như lúc chưa chọn; web giữ cấu tạo Astryx, màu theo token; nhìn theo cột "Bản chốt" Figma 6234:13999 | DEC-184 |
| Dòng danh sách | `Base / List Row` chung web và app; đầu và cuối dòng là Slot; cao theo nội dung, tối thiểu 52 app, 36 web | DEC-182 |
| Lồng góc, lề đều | Khung lớn tách xa (bo ≤ lề), khung ôm đồng tâm; máy đo kiểm trước khi trình | DEC-165 |
| Tài liệu | Đủ mục DEC-118 từ đợt 1, có mục chấm điểm trợ năng | DEC-183 |

## 12. Còn mở

- Gói Figma của team có quyền publish thư viện không (DEC-110).
