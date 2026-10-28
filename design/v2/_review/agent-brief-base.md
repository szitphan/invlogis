---
type: design-review
status: draft
updated: 2026-10-26
links:
  - _workspace/decisions.md
  - design/v2/foundations.md
  - design/v2/tokens.json
  - .claude/skills/figma-component/SKILL.md
---

# Giao việc agent vẽ Base component (DS v2 theo Untitled UI)

> Bản giao việc chung cho mỗi agent vẽ một Base component trên Figma (DEC-260). Biến thể của từng component do
> user tick ở trang vòng 2 (https://claude.ai/artifact/VQDsMrBW37W3QWVTPN79qC); main thread chép phần đó vào lời gọi agent.

## 1. Nơi vẽ

- File Figma `[innvie] invlogis v0.3`, trang `DS · Base components` (id `6650:339720`). Ghi bằng reqwise
  `figma_write` với `file: "invlogis v0.3"`, `page: "DS · Base components"`. Gọi `figma_status` trước tiên.
- Mỗi component một **Section** tên đúng tên component (vd `Buttons`), đặt ở toạ độ main thread giao (cột riêng, không
  chồng agent khác). Mọi thứ của component nằm trong Section đó: component set + 2 màn demo.
- Không sửa, không xoá gì ngoài Section của mình. Không đổi biến, text style, effect style (báo thiếu thì ghi vào báo cáo).
- Window Figma có thể bị chậm (throttled): chia lệnh nhỏ (≤ 20 node mỗi `batch`), không chạy lại lệnh đã thành công.
  Lệnh timeout vẫn có thể chạy xong muộn → kiểm node trùng trước khi dựng lại.
- **Mỗi agent một `sessionId` riêng** cho `figma_write` (vd `"button-agent"`): `state` mặc định dùng chung giữa các agent,
  đã có lần ghi đè id Section của nhau.
- **Không gắn biến tên bắt đầu `zz-old/`** (collection cũ chờ xoá). Gắn bằng VariableID hoặc kiểm tên biến trả về.
  `modify` với `fill: "$…"` có lúc báo thành công mà không đổi màu → dùng `applyVariable`.

## 2. Luật đã chốt (DEC-260) — thay cho luật L0/L1/L2 cũ

- **Bỏ quy ước L0/L1/L2.** Không tên `Base / …`, không tiền tố `.` cho phần con. Tên component theo Untitled, tiếng Anh
  (vd `Button`, `Badge`, `Input`). Phần con dùng nội bộ, không cho dùng riêng: tiền tố `_` (vd `_Button spinner`).
- **Tên thuộc tính theo Untitled, giá trị viết hoa** như v2: `Hierarchy=Primary, Size=MD, Icon=Only, State=Hover,
  Destructive=False`. Thuộc tính không phải biến thể (chữ, bật tắt, đổi icon) tên tiếng Anh viết hoa chữ đầu:
  `Label`, `Icon Leading`, `Has Icon Leading`.
- **Giữ nền tảng v2**: chỉ gắn biến có sẵn trong file (collections `0. Primitives`, `1. Semantic`, `Platform`,
  `7. Brand`, `8. Component`), text style `type/*`, effect style `elev/*`. Không dùng hex rời. Màu hành động chính than chì
  (`color/action/primary`), nút phẳng (không bóng skeuomorphic), focus outline 2px cách 2px (`color/border/focus`,
  `focus/width`, `focus/offset`). Cao control web SM 28 · MD 32 · LG 40; app lấy theo chế độ `Platform` = Mobile.
- **Icon**: Lucide từ trang `✦ DS · Icons` (instance swap). Không vẽ icon tay.
- **Untitled là mẫu cấu tạo**: thứ tự phần, khoảng cách tương đối, trục biến thể, trạng thái. Nguồn: repo
  `untitleduico/react` (đã clone ở `/private/tmp/claude-501/-Users-szit-Desktop-szit-AI-Projects-invlogis/7b86db2e-ecf6-4269-bd23-8355fe286950/scratchpad/uui/repo/components/`, chỉ đọc)
  và ghi chú ở untitledui.com/components/{tên}. Số đo thì lấy token v2, không lấy số Untitled.
- **Dark**: gắn biến đúng là Dark tự chạy; chỉ kiểm Light (DEC-260 F14).
- **App**: một component đổi số đo theo `Platform`, trừ khi lời gọi nói tách `/ Mobile` hoặc chỉ web.
- **Tài liệu và ghi chú viết sau cùng** — không dựng khung tài liệu, không viết `design/v2/components/*.md`.

## 2b. Bố cục Section và chữ dài (user chốt 27/10)

- **Web và Mobile hai khối riêng.** Component có biến thể/bản app thì trong Section chia khối `Web` và khối `Mobile`
  (mỗi khối có tiêu đề nhỏ), không trộn chung một lưới. Bản app (DEC-279): nhóm A = instance đặt mode `Platform` Mobile;
  nhóm B = các biến thể `Platform=Mobile` của cùng bộ (hàng dưới cùng trong bộ, tiêu đề "Platform = Mobile"); không dựng set `/ Mobile`.
- **Màn demo ở khu riêng** bên phải các khối component (khung tiêu đề `Demo`), không xen vào lưới biến thể.
  Sau mỗi lượt, demo phải dùng component thật mới nhất (thay khối tạm).
- **Luật chữ dài bắt buộc.** Mỗi ô chữ trong component khai cách xử lý: mặc định **1 dòng, cắt "…", có rộng tối đa**;
  chỉ trường bắt buộc dài (mô tả, địa chỉ, lý do, họ tên đầy đủ) mới **xuống dòng** (ghi số dòng tối đa). Ghi luật vào mô
  tả component; khung kiểm chữ dài chỉ thử đúng các trường đó, không dựng thêm ca dài ở chỗ khác.

## 2c. Section chủ đề, master, demo (DEC-263, sửa bởi DEC-264)

- **Một Section mỗi chủ đề**, tên chỉ là tên mục (`Typography`, `Buttons`), không tiền tố `Foundations /`.
- Trong Section: bên trái `_Design system header` + các **Section con** (mỗi khối một Section con, tên chỉ là tên khối,
  vd `Họ chữ`; khung nội dung bên trong giữ auto layout); bên phải là **master** (component gốc, tên `Master` hoặc
  `Master · <tên>`), cùng Section, không để ở khung riêng ngoài Section.
- Tài liệu dùng *instance*; component gốc chỉ ở master (cách C).
- Chia **khối Web và khối Mobile** khi hai bên khác nhau; giống nhau thì một khối, ghi "Web = App".
- **Demo tách Section riêng** đặt ngay bên phải Section chủ đề, tên `Demo · <Chủ đề>` (màn thật, chữ tiếng Việt có dấu).
- Không dùng `Khối ·`, `Block ·`, `Section /` trong tên.

## 2d. Luật đặt tên — bắt buộc, kiểm máy (DEC-264)

| Node | Quy định | Tối đa |
|---|---|---|
| Component, component set | Tên Untitled tiếng Anh; phần con dùng nội bộ tiền tố `_` | 32 |
| Thuộc tính / giá trị biến thể | Tên thuộc tính tiếng Anh, giá trị viết hoa | 20 / 16 |
| Layer chữ (trong component **và** ghi chú, màn demo) | Theo **vai trò**, không theo nội dung: `Title`, `Subtitle`, `Group title`, `Row label`, `Col label`, `Label`, `Value`, `Description`, `Note`, `Caption`; dữ liệu mẫu: `Name`, `Route`, `Vehicle`, `Driver`, `Code`, `Time` | 24 |
| Section, Section con | Chỉ tên mục | 32 |
| Màn demo | `<Màn> / Web` hoặc `<Màn> / Mobile`, thêm `/ <Trạng thái>` khi cần; không lặp tên component, không ghi 1440 / 393 | 40 |
| Mọi node | Không chứa mã DEC, mã node, câu giải thích — đưa vào description | — |

- Figma tự lấy nội dung làm tên layer chữ → **đổi tên ngay khi tạo** (`name` trong spec `create`).
- **Gate:** trước khi báo cáo, chạy `_scripts/figma-name-lint.js` (thay `ROOTS` = id Section của mình, dán làm `code` cho
  `figma_write`). `fail` phải = 0; FAIL ở giá trị biến thể thì ghi *Cần user quyết* (đổi giá trị đụng instance), không tự đổi.
  Báo cáo ghi số FAIL trước/sau.

## 3. Cách dựng

Đọc `.claude/skills/figma-component/SKILL.md` để lấy **cách làm** (API biến thể/thuộc tính, gắn token, kiểm chữ dài,
kiểm máy), bỏ các phần nói về L0/L1/L2, khung tài liệu và ghi repo. Thứ tự:

1. `figma_docs(section="api", level="cheat")` và `figma_docs(section="recipes")`.
2. Đọc biến/style thật trong file (`figma_read` `get_variables`, `get_styles`) và component đã có mà mình được dùng lại
   (lời gọi ghi rõ). Dùng instance của component đã có, không vẽ lại.
3. Dựng component set đúng phần user tick (không thêm giá trị không tick; thiếu gì để cấu tạo đúng thì ghi vào báo cáo).
   Sắp lưới biến thể có nhãn hàng/cột để người duyệt đọc được.
4. Hai **màn demo** cạnh component set, dùng instance của component vừa dựng trong ngữ cảnh thật của sản phẩm
   (logistics: lệnh vận tải, xe, lái xe, chứng từ; chữ tiếng Việt có dấu): `{Component} demo / {Màn} / Web 1440` và
   `{Component} demo / {Màn} / Mobile 393` (khung app đặt `Platform` = Mobile). Phần màn chưa có component thì dựng
   khối đơn giản bằng token. Màn demo do lời gọi nêu.
5. Kiểm máy: `layoutAudit` từng component set và màn demo, `figma_read` `a11y_audit`, `text_growth_audit` cho component
   có chữ, **kiểm tên** `_scripts/figma-name-lint.js` (§2d). Sửa lỗi chặn rồi chạy lại một lần.
6. Một `screenshot` component set + một của mỗi màn demo ở cuối.

## 4. Báo cáo trả về (không ghi file repo)

- Node id: Section, component set, từng màn demo.
- Bảng API: thuộc tính · loại · mặc định · giá trị. Số biến thể.
- Token đã gắn theo phần (nền, chữ, viền, bo, khoảng cách) — tên biến.
- Kết quả kiểm máy (layout, a11y, chữ dài): số lỗi trước/sau.
- Chỗ lệch Untitled và lý do; chỗ thiếu token; câu hỏi cho user (nếu có).
