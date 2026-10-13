---
paths:
  - ".claude/agents/uxui-reviewer.md"
  - ".claude/agents/usability-reviewer.md"
  - ".claude/agents/visual-reviewer.md"
  - ".claude/skills/figma-screen/**"
  - ".claude/skills/prototype-html/**"
  - ".claude/skills/wireframe-*/**"
  - "_scripts/visual-audit.py"
---

# UI Review — ai kiểm luật nào, ở lớp nào

> Rule chung cho mọi skill review màn (`/figma-screen`, `/prototype-html`, `/wireframe-*`) và 3 agent
> `@uxui-reviewer`, `@usability-reviewer`, `@visual-reviewer`. Mục đích: **mỗi luật đúng một chủ**,
> không agent nào kiểm trùng agent khác, không agent nào chấm thay việc máy đo được.

## 1. Hai lớp

| Lớp | Là gì | Ra gì | Khi nào |
|---|---|---|---|
| **1 · Audit máy** | Lệnh/ script tất định, đọc cây node Figma | Số liệu, `FAIL` / `WARN` / `INFO` | Chạy trước. `FAIL` phải sửa xong mới sang lớp 2 |
| **2 · Reviewer** | Agent đọc ảnh + số liệu lớp 1, chấm bằng phán đoán | Finding theo `review-format.md` | Sau lớp 1. 3 agent chạy **song song**, chỉ đọc, không tự sửa |

Nguyên tắc chia: **đo được bằng số → audit máy; cần mắt người → reviewer**. Reviewer không đo lại
cái máy đã đo — chỉ diễn giải con số (vd A5 báo màu nhấn 18% → visual-reviewer nói 18% đó có làm
loãng điểm nhấn không).

### Lớp 1 — audit máy

| Mã | Công cụ | Kiểm |
|---|---|---|
| A1 | `figma_read layout_audit` | Tràn, bị cắt, chữ ba chấm; styleHints: padding chật, bo góc lệch |
| A2 | `figma_read a11y_audit` + skill `accessibility-review` | Tương phản, vùng chạm, control thiếu tên, WCAG 2.1 AA |
| A3 | `figma.auditDesignSystem` | Màu/chữ/khoảng cách gắn token; giá trị off-system |
| A4 | Do's & Don'ts tự rà + `status-chip-lint.py` | 1 Primary mỗi nhóm, trạng thái có chữ/icon, chip trạng thái |
| A5 | `_scripts/visual-audit.py` | Luật thị giác đo được — Mục 2 |
| A6 | `_scripts/figma-audit.py` (`/figma-audit`) | Nhất quán GIỮA nhiều màn đã vẽ: token, vai trò lệch giá trị, biến thể nút, icon (kể cả override), khối tự dựng, mã bản ghi dọc luồng |

### Lớp 2 — reviewer

| Agent | Câu hỏi duy nhất |
|---|---|
| `@uxui-reviewer` | Màn có **khớp đặc tả** không? (trạng thái, CMP/GR, wording, bảng 5 cột) |
| `@usability-reviewer` | Người dùng có **làm xong việc** không, có nhanh không? |
| `@visual-reviewer` | Mắt có **đọc đúng thứ tự ưu tiên** không? (phân cấp, màu, nhịp, dễ đọc) |

## 2. Bảng luật → chủ → ngưỡng

Ngưỡng A5 là hằng số đầu `_scripts/visual-audit.py` — sửa ngưỡng thì sửa cả hai nơi.

| Luật | A5 đo (mã check · ngưỡng · mức) | Reviewer chấm |
|---|---|---|
| **Fitts** | `F1` nút nguy hiểm cách nút chính < 8px · WARN<br>`F2` mobile: nút chính nằm ngoài 40% dưới màn · WARN<br>`F3` nút chính nhỏ hơn nút phụ cùng nhóm · WARN | visual: vị trí có thuận tay, đúng chỗ mắt tìm không |
| **Hick** | `H1` > 5 nút ngang hàng trong 1 nhóm · WARN<br>`H2` menu/dropdown/segmented/tab > 7 lựa chọn · WARN | usability: ở bước đó người dùng có bị quá nhiều lựa chọn không |
| **Miller** | `M1` > 7 field trong 1 khối không có tiêu đề nhóm · WARN<br>`M2` bảng > 9 cột hiện (web) · WARN | usability: có bắt nhớ/so quá nhiều thứ cùng lúc không |
| **Proximity** | `P1` khoảng cách trong nhóm ≥ khoảng cách giữa nhóm cha · WARN | visual: nhìn có ra đúng nhóm không |
| **Spacing** | `S1` mobile: khoảng cách không thuộc lưới 8pt (design.md › Mẫu bố cục M) · WARN. Gắn token → A3 | visual: nhịp đều, đúng tầng (field 16 · nhóm 32) |
| **Readability** | `R1` số cỡ chữ: web > 5, mobile > 4 · WARN<br>`R2` chữ < 12px · FAIL mobile, WARN web (design có heading-6 10px)<br>`R3` dòng > 90 ký tự · WARN | visual: dễ quét, căn lề thẳng, nhãn gọn |
| **60/30/10** | `C1` tỷ lệ diện tích trung tính / phụ / nhấn; nhấn > 15% · WARN; trung tính < 60% · WARN<br>`C2` > 3 sắc độ đậm khác nhau (không tính chip/badge trạng thái) · WARN | visual: diễn giải tỷ lệ theo theme Neutral của dự án |
| **Color hierarchy** | — | visual |
| **Màu cho phản hồi** | A4 (trạng thái có chữ/icon, chip) | visual: màu lỗi/thành công nhất quán, không dùng màu trạng thái cho trang trí |
| **Jakob** | — | usability: control/vị trí giống thói quen app cùng loại không |
| Tương phản, vùng chạm | A2 | — |
| Token | A3 | — |
| Đủ trạng thái, khớp spec, wording | — | uxui |
| Heuristic Nielsen, số bước tác vụ | — | usability |

> Mức A5 tối đa là WARN trừ `R2` — luật thị giác có ngoại lệ hợp lý (bảng nhiều cột theo nghiệp vụ,
> toolbar dày). Reviewer quyết WARN nào thành finding.

**Chạy A5:** `figma_read get_design_context` `{nodeId: <artboard>, depth: 20, detail: "full"}` → lưu
JSON → `python3 _scripts/visual-audit.py <file.json>`. Script in tỷ lệ nhận diện component; < 80% thì
F/H/M có thể thiếu (mainComponent bị cắt ở cây lớn) → đọc lại vùng con (`get_design_context` theo nodeId
của khối) và chạy lại với `--part <vùng.json>` (ghép đè theo id); vẫn < 80% → ghi rõ, không in PASS.
Vỏ thiết bị (Status Bar, Home Indicator) tự bỏ; nội dung trong `SLOT` của khung (Device / Frame, Khung
trang) tính là khung tự dựng.

**Không đo được bằng máy:** độ đậm chữ — cây node của plugin không có `fontWeight`/`fontName` (đã thử
`get_design_context`, `get_node`, `scan_text_nodes`, `get_fonts`). `@visual-reviewer` chấm phân cấp đậm
nhạt qua ảnh (V5).
Sửa script/ngưỡng xong chạy 2 fixture: `_scripts/fixtures/visual-audit/pass-web.json` (exit 0, 0 WARN)
và `fail-mobile.json` (exit 1, đủ mã F1 F2 F3 H1 H2 M1 P1 R1 R2 R3 S1 C1 C2).

## 3. Chạy ở đâu

| Skill | Lớp 1 | uxui | usability | visual |
|---|---|---|---|---|
| `/wireframe-ascii`, `/wireframe-html` | — | ✓ | — | — (lo-fi, chưa có màu) |
| `/prototype-html` | A5 không chạy (script đọc JSON Figma) | ✓ | — | ✓ (chấm bằng ảnh, ghi "không có số liệu A5") |
| `/figma-screen` | A1–A5 | ✓ | ✓ khi trọn flow + có Mục 3.6 | ✓ |
| `/figma-audit` | A6 | — | — | — (chỉ máy đo; sửa theo mục user chọn) |

## 4. Báo cáo

In tách 2 lớp, không gộp "PASS":

```
Lớp 1 — audit máy
  A1 layout: 0 chặn · A2 a11y: 2 đã biết · A3 DS: 1.00 · A4 Do's: OK · A5 visual: 0 FAIL / 3 WARN (nhận diện 92%)
Lớp 2 — reviewer
  Khớp đặc tả (@uxui-reviewer): 0 blocking / 1 warning
  Usability (AI): 3 tác vụ · 0 blocking / 2 warning | SKIPPED — <lý do>
  Thị giác (@visual-reviewer): 0 blocking / 2 warning
```

Agent bị bỏ qua → `SKIPPED — <lý do>`, không in PASS.

## Tóm tắt 1 dòng

> **Máy đo trước (A1–A5), 3 reviewer song song sau · mỗi luật một chủ theo bảng Mục 2 · reviewer
> diễn giải số, không đo lại.**
