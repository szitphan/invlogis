---
type: design-review
status: draft
updated: 2026-10-27
links:
  - design/v2/_review/agent-brief-base.md
  - _workspace/decisions.md
  - design/v2/foundations.md
  - design/v2/tokens.json
  - .claude/skills/figma-component/SKILL.md
---

# Giao việc agent vẽ Application component (DS v2 theo Untitled UI)

> Bản giao việc chung cho mỗi agent vẽ một Application component trên Figma (DEC-260). Biến thể của từng
> component do user tick ở trang vòng 3 (https://claude.ai/artifact/L3pzcVoU11rCka42c9tHoS, db `variants`);
> main thread chép phần đó vào lời gọi agent. **Mọi luật của [agent-brief-base.md](agent-brief-base.md) vẫn áp**
> (§1 luật ghi, §2 luật DEC-260, §2b bố cục + chữ dài, §2c cách C, §2d luật tên + gate, §3 cách dựng, §4 báo cáo);
> file này chỉ ghi chỗ khác.

## 1. Nơi vẽ

- File `[innvie] invlogis v0.3`, trang **`DS · Application components`** (id `6766:190506`). `figma_write` với
  `file: "invlogis v0.3"`, `page: "DS · Application components"`, `sessionId` riêng mỗi agent.
- Section chủ đề đặt ở toạ độ main thread giao; `Demo · <Chủ đề>` ngay bên phải, cách 200.

## 2. Ghép từ Base — không vẽ lại phần con

Application component là **ráp từ instance** của Base trên trang `DS · Base components` (6650:339720) và icon
trên `DS · Foundations` (6681:222300). Id hay dùng:

| Base | Id set |
|---|---|
| Button · Close button · Utility button | 6657:163467 · 6657:164851 · 6657:164908 |
| Badge · Tag | 6657:165736 · 6657:167999 |
| Avatar · Avatar label group · Company avatar | 6657:166192 · 6657:167394 · 6657:167713 |
| Input · Select · Dropdown menu · Dropdown item · Dropdown trigger | 6658:172078 · 6658:194903 · 6658:196389 · 6658:193894 · 6658:197422 |
| Tooltip · Help icon · Featured icon | 6657:165642 · 6657:166386 · 6657:163375 |
| Logo · Company logo | 6681:227878 · 6681:227883 |

Icon: Lucide `icon/<tên>` (khung `Foundations / Icons` trên trang Foundations; tìm bằng `searchNodes`). Thiếu
icon → ghi vào báo cáo, không vẽ tay.

## 3. Khác Base

- Component bố cục (thanh điều hướng, header) dùng **slot**: phần lặp (mục menu, nút) là component con
  `_<Tên> item` có biến thể State; component cha xếp instance con bằng auto layout, không vẽ phẳng.
- **Chữ mẫu trong component trung tính** (`Label`, `Title`) — chữ nghiệp vụ tiếng Việt chỉ ở màn demo và khối
  ví dụ (ds-levels-no-context).
- Màn demo web 1440 × 900 có khung trang thật; app 393 × 852 đặt `Platform` = Mobile, có status bar
  (`.Mobile / Status Bar` 5279:7791) và home indicator (5279:7800).
- Tên master: `<Tên>` cho set chính, `_<Tên> item` cho mục con. Section con theo cách C: `Web`, `Mobile` (nếu
  khác), `Cấu tạo`, `Biến thể`, `Trạng thái`, `Chữ dài`.
