---
paths:
  - "design/**"
  - "prototype/**"
  - "docs/**/ascii-wireframe/**"
  - "docs/**/html-wireframe/**"
  - "docs/**/html-design/**"
  - ".claude/skills/wireframe-*/**"
  - ".claude/skills/prototype-*/**"
  - ".claude/skills/figma-*/**"
  - ".claude/skills/user-flow/**"
  - ".claude/skills/srs/**"
  - ".claude/agents/uxui-reviewer.md"
  - ".claude/agents/usability-reviewer.md"
---

# Design System — nguồn thiết kế chung cho skill sinh giao diện

> Rule chung cho MỌI skill vẽ hoặc review màn hình (`/srs` phần UX, `/user-flow`, `/wireframe-ascii`,
> `/wireframe-html`, `/prototype-html`, `/figma-*` (gồm `/figma-component`), agent `uxui-reviewer`). Mỗi skill đã nối MUST
> reference file này trong Constraints + References.

## Nguồn duy nhất

| File | Vai trò |
|---|---|
| `design/design.md` | **Nguồn chuẩn.** Token (khối YAML đầu file) + quy tắc dùng (thân file). |
| `design/design-tokens.css` | Bản CSS của cùng bộ token, cho prototype và code. Sinh theo `design.md`, không sửa lệch. |
| `design/components.md` | Chọn component nào + dùng thế nào (Usage, Nên/Không nên, Examples, tên set Figma). Lệch với `design.md` thì `design.md` thắng. |
| `design/ba-crosswalk.md` | Tra ngược từ **Control type** trong bảng Screen description của BA sang component ứng viên. Chỉ để tra, không thay `components.md`. |
| `design/figma-library-keys.json` | Key component set của thư viện Figma (máy sinh). Dùng để instantiate, không sửa tay. |

- Chưa có `design/design.md`:
  * Skill **lo-fi** (`/wireframe-ascii`, `/wireframe-html`, `/user-flow`, `/srs`) chạy như cũ, báo 1 dòng
    "Chưa có design/design.md — chạy lo-fi, không áp design system".
  * Skill **vẽ Figma** (`/figma-*`) **dừng**, báo thiếu design system và chỉ cách cài kit.
    KHÔNG dùng bảng màu dự phòng, KHÔNG lấy file `design.md` mẫu của dự án/bộ kit khác làm mặc định.
- Có → **đọc theo mục**, đọc lại từ file mỗi lần chạy. Không trích từ trí nhớ phiên trước (file có
  thể đã đổi). File dài hơn 1.000 dòng; đọc toàn văn cho mọi skill làm lượt chạy chậm và tốn token mà
  phần lớn không dùng tới.
  1. `Grep -n "^## \|^### "` lấy mục lục kèm số dòng.
  2. **Luôn đọc** các mục ngắn chứa quy định áp chung: *Typography › Principles*, *Tên trong Figma*
     (chỉ skill vẽ trên Figma), *Do's and Don'ts*, *Iteration Guide*, *Known Gaps*. Lý do: quy định
     áp chung nằm rải ở mục không trùng tên chủ đề — vd "không viết hoa toàn bộ" ở Typography,
     "biến thể mặc định của thư viện không phải cỡ MD" ở Tên trong Figma, và Known Gaps có thể đánh
     dấu "còn mở" một quy định ở mục khác (vd rút gọn tiền ở Content & Formatting).
  3. Đọc các mục của skill mình theo bảng dưới, bằng Read offset/limit theo số dòng mục lục (một
     mục `##` gồm mọi `###` con của nó).
  4. Đoạn đã đọc có tham chiếu "xem §…" / "xem *…*" → đọc luôn đoạn được chỉ tới.
  5. Bảng ghi **Toàn bộ** → Read toàn văn.
- Thêm quy định áp chung cho mọi skill vào `design.md` → đặt trong một mục "luôn đọc" ở bước 2, hoặc
  thêm mục mới vào danh sách đó cùng lượt. Nếu không, skill đọc theo mục sẽ âm thầm bỏ sót.
- Nội dung cụ thể (màu, cỡ, tên sản phẩm, mẫu bố cục) chỉ sống trong `design/design.md`,
  KHÔNG chép vào `.claude/` (đúng tinh thần `project-profile.md`).

## Mỗi loại skill đọc phần nào

| Skill | Đọc | Không áp |
|---|---|---|
| `/srs` (chọn device), `/user-flow` | Responsive Behavior (Breakpoints, thiết bị chính), Layout (mẫu bố cục) | Màu, chữ |
| `/wireframe-ascii`, `/wireframe-html` (lo-fi B&W) | Layout (mẫu bố cục P/M, Grid & Container, Whitespace), States (đủ trạng thái rỗng/đang tải/lỗi, ánh xạ trạng thái nghiệp vụ → **nhãn chữ**), Components (chọn đúng loại control, thứ tự nút, 1 nút chính/nhóm), Content & Formatting, Do's and Don'ts phần bố cục | **Toàn bộ màu, bóng, font** — B&W strict của skill vẫn thắng |
| `/prototype-html`, code | Toàn bộ; màu/chữ/khoảng cách qua `design/design-tokens.css` | — |
| `/deck` | Không đọc `design.md`; `build-deck.py` nhúng `design/design-tokens.css` (font, màu nền) + brand đơn vị trình bày `design/brand/{slug}/` (màu chính, logo — thắng token khi có). Thiếu cả hai → màu trung tính, báo 1 dòng | Layout, component, States — slide không phải màn sản phẩm |
| `/figma-design-system` | `source:"design_md"`, `learn:{path:"<abs>/design/design.md"}` | — |
| `/figma-screen` (và `/figma-*` vẽ màn) | Layout (toàn bộ: Spacing, Grid & Container, Mẫu bố cục P/M, Whitespace); phần đầu *Components* tới hết quy ước "Web và Mobile" + mục `###` của nhóm component sẽ dùng; *Phân trang danh sách* nếu màn có danh sách; trong *Components - <dự án>*: *Quy ước chung* + spec của component dự án có trên màn; States; Content & Formatting; Accessibility (ngoại lệ đã chấp nhận, cho a11y_audit); Responsive Behavior. Overview / Colors / Typography Hierarchy / Elevation / Shapes không cần đọc: token gắn theo tên (§ Tên trong Figma) | — |
| `/figma-component` | Trong *Components - <dự án>*: mục *Quy ước chung của component dự án* + spec đang dựng (spec khác chỉ đọc khi quy ước dẫn tới hoặc cần làm mẫu khuôn); phần đầu *Components* tới hết quy ước "Web và Mobile"; States; Content & Formatting; Accessibility; Responsive Behavior; *Phân trang danh sách* nếu component có danh sách; Layout khi đề xuất bố cục ví dụ *Trong ngữ cảnh*. Colors / Typography Hierarchy / Elevation / Shapes không cần đọc: giá trị gắn qua biến và style Figma theo tên | — |
| `uxui-reviewer` | States, Components, Accessibility, Do's and Don'ts — làm tiêu chí review | — |

## Luật khi sinh màn

1. **Bố cục: đề xuất 3 phương án để user chọn** trước khi vẽ. Mẫu có sẵn chỉ là một phương án;
   hai phương án kia đề xuất độc lập để user thấy được lựa chọn thật, không phải ba biến thể của
   cùng một mẫu.
   * **A — theo mẫu có sẵn:** mẫu gần nhất trong mục Layout (shell S + trang P desktop / M mobile),
     chỉnh vùng/nội dung cho hợp màn; nêu giống ở đâu, chỉnh gì.
   * **B, C — độc lập:** thiết kế từ nhu cầu của màn (nhiệm vụ chính, lượng dữ liệu, thiết bị),
     không xuất phát từ mẫu. B và C phải khác nhau thật về cách tổ chức (vd bảng + drawer so với
     master–detail), mỗi phương án kèm lý do và đánh đổi.
   * Cả ba vẫn dùng token, component thư viện và Do's and Don'ts của `design.md` — độc lập về khung
     trang, không độc lập về design system.
   * User chọn B/C và khung đó sẽ dùng lại → đề xuất thêm thành mẫu mới theo Iteration Guide (qua
     approval gate).
   * Mẫu M chưa có node Figma → ghi "chưa có chuẩn trong design.md — theo spec M, chưa có node Figma".
2. **Trạng thái nghiệp vụ** → gán nhóm theo bảng "Ánh xạ trạng thái nghiệp vụ"; nhãn lấy nguyên
   văn từ `srs/{feature}-states.md`.
3. **Đụng Known Gaps** (mục cuối `design.md`) → KHÔNG bịa giá trị. Hỏi user, hoặc vẽ tạm và ghi
   rõ "chưa có chuẩn trong design.md" ở cột Description.
4. **Do's and Don'ts** là tiêu chí tự kiểm trước khi trình L3/L1: mỗi màn rà ít nhất (a) đúng 1
   nút chính/nhóm, (b) trạng thái có chữ/icon không chỉ màu, (c) đủ trạng thái rỗng/lỗi/đang tải,
   (d) form không trải hết bề rộng desktop.
5. **Device** vẫn phải hỏi user theo `ba-conventions.md` Mục 7 — `design.md` chỉ để **đề xuất**.
6. **Chọn component**: Control type → `ba-crosswalk.md` → mục component trong `components.md` (áp
   Nên/Không nên) → tên set trong `figma-library-keys.json`. Không có component hợp lệ hoặc tên không có
   trong keys → ghi gap "chưa có chuẩn trong design.md", KHÔNG tự dựng component thay thế im lặng.
7. **Component dùng chung, hành vi theo feature.** Component (thư viện hoặc *Components - <dự án>*)
   chỉ định nghĩa khung: anatomy, biến thể, state, a11y, ràng buộc. Dữ liệu và hành vi trong ngữ cảnh
   (vd bộ lọc: field nào, mặc định, toán tử, phụ thuộc, rỗng/lỗi, áp dụng/xoá) lấy từ SRS + Screen
   description của feature. Thiếu → hỏi user hoặc ghi OQ; KHÔNG chép hành vi của feature khác.

## Sửa design system

- Đổi token → sửa khối YAML đầu `design/design.md` **và** `design/design-tokens.css` cùng lượt.
- Thêm mẫu bố cục / component / trạng thái → thêm vào đúng mục trong `design.md` (theo
  Iteration Guide của file đó), không ghi rải trong wireframe hay spec.
- Mọi sửa qua approval gate (L1, L2) như doc khác.

## Tóm tắt 1 dòng

> **`design/design.md` là nguồn duy nhất, đọc theo mục (mục lục + mục luôn đọc + mục của skill) · wireframe B&W chỉ lấy bố cục/trạng thái/component, không lấy màu ·
> bố cục: 3 phương án (1 theo mẫu có sẵn + 2 độc lập) để user chọn · Known Gaps thì hỏi, không bịa ·
> component: crosswalk → components.md → keys, thiếu thì ghi gap · hi-fi thiếu design.md thì dừng, không fallback.**
