---
paths:
  - "docs/**/screens/**"
  - "docs/**/html-wireframe/**"
  - "docs/**/ascii-wireframe/**"
  - ".claude/skills/figma-*/**"
  - ".claude/skills/wireframe-*/**"
  - ".claude/skills/prototype-*/**"
  - ".claude/skills/srs/**"
  - ".claude/state/figma/**"
---

# Screen Source — bảng mô tả màn sống ở đâu, Figma đổi thì ai sửa tài liệu

> Rule chung cho mọi skill đọc/ghi bảng mô tả màn 5 cột hoặc vẽ màn trên Figma. Trả lời: **giao diện đã
> lên Figma thì wireframe còn vai trò gì, bảng 5 cột nằm ở đâu, sửa trên Figma thì ai cập nhật tài liệu,
> khi nào đưa Figma vào SRS.**

## 1. Vòng đời một flow

```
/wireframe-html | /wireframe-ascii      bảng 5 cột trong html-wireframe/{flow}.html | ascii-wireframe/{flow}.md
        ↓
/figma-screen                            vẽ màn, ghi link Figma, lưu mốc → gọi /figma-sync
        ↓
/figma-sync (lần đầu của flow)           chuyển bảng sang screens/{flow}.md (máy chép), xoá wireframe flow đó
        ↓   ← mỗi lần sửa trên Figma: /figma-sync đối chiếu mốc → sửa screens/{flow}.md + userflow
/figma-sync --done                       ảnh PNG 2x → screens/images/, flow `approved`, SRS Mục 10
```

## 2. Nguồn bảng 5 cột — thứ tự ưu tiên

| Có file | Là nguồn | Ghi chú |
|---|---|---|
| `docs/{feature}/screens/{flow}.md` | **Duy nhất** cho flow đó | Sau khi flow đã lên Figma. Hình = frame Figma |
| `html-wireframe/{flow}.html` | Khi chưa có `screens/{flow}.md` | Bảng HTML thắng ASCII khi có cả hai |
| `ascii-wireframe/{flow}.md` | Khi chưa có hai cái trên | — |

- Skill đọc bảng (`/figma-screen`, `/prototype-html`, `/userstory`, `/test-checklist`, `/test-cases`,
  `@uxui-reviewer`, `/preview`, `/export`…) tra theo thứ tự này. Gặp `screens/{flow}.md` thì KHÔNG đọc
  wireframe cũ của flow đó (đã bị xoá; còn sót lại là lỗi, báo user).
- `/wireframe-html`, `/wireframe-ascii` KHÔNG sinh lại flow đã có `screens/{flow}.md` — đổi bố cục thì
  sửa trên Figma rồi `/figma-sync`.
- Bỏ HTML khi đã có Figma (DEC-053): KHÔNG giữ song song HTML và `screens/`.

## 3. Định dạng `screens/`

```
docs/{feature}/screens/
├── {feature}-screen-index.md   # type: screen-index · bảng Flows: # | Flow | File | Thiết bị | Màn | Figma | Status | Updated
├── {flow-slug}.md              # zero frontmatter, 1 file/flow
└── images/{n-m}-{web|mob}-{slug}.png   # ảnh Figma 2x, chỉ có sau --done
```

Trong `{flow-slug}.md`, mỗi màn:

```markdown
## Screen: {slug} — {tên Việt}

- **screenId:** 1.1 · web
- **Figma:** [1.1 · web](https://www.figma.com/design/{fileKey}/?node-id=…)
- **Mô tả:** {1–2 câu: màn này để làm gì, người dùng thấy khi nào}   ← cột Mô tả của danh mục SRS Mục 10

![1.1 · web · {slug}](images/1-1-web-{slug}.png)      ← chỉ sau --done

| # | Items | Control type | Data type | Description |

### Trạng thái: Loading — {tên Việt}                   ← frame 4 phần của màn đó

- **Figma:** [1.1 · web · {slug} · Loading](…)        ← nhãn = tên frame 4 phần (có slug)
```

- Block `## Screen:` giữ đúng mẫu ASCII để KG và các skill đã parse ASCII đọc được.
- **Status theo flow** nằm ở cột Status của index (`draft` → `approved`), không ở file flow.
- Lần chuyển đầu do máy làm: `python3 _scripts/screens-md.py migrate <feature> <flow> [--write]` —
  chép nguyên văn, đếm row nguồn = row đích; lệch thì không ghi.

## 4. Mốc Figma (baseline)

`.claude/state/figma/{feature}.json` — ảnh chụp trạng thái lần đồng bộ gần nhất, để biết **Figma đã đổi gì**
(Figma không báo cho repo). Commit chung vault, không chứa token.

```json
{ "fileKey": "…", "synced_at": "2026-10-13",
  "screens": { "1.1 · web": {
      "nodeId": "5587:117888", "slug": "record-detail", "flows": ["view-process"], "frames": { "Loading": "5587:118511" },
      "rows": { "1": {"nodeId": "…", "text": "Dòng quy trình", "component": "Row"},
                "8": {"nodeId": "…", "also": ["…"], "text": "Thu hồi / Xoá"} },
      "frame_rows": { "Load error": { "1": {"nodeId": "…", "text": "Thông báo lỗi tại chỗ dòng quy trình"} } },
      "level": "row",
      "texts": { "<nodeId>": "chữ hiển thị" },
      "reactions": [ {"from": "<nodeId>", "trigger": "ON_CLICK", "to": "1.2 · web"} ] } } }
```

- Ghi bởi `/figma-screen` (sau Bước 7) và `/figma-sync` (sau mỗi lần sync thành công).
- `rows` = bản đồ row bảng 5 cột → node trên Figma của frame chính; `frame_rows` = bản đồ tương tự cho từng frame
  trạng thái (khoá = tên trạng thái). Row ứng với nhiều phần tử (vd "Thu hồi / Xoá") ghi phần tử đầu ở `nodeId`,
  phần còn lại ở `also`. Row chưa ghép được ghi `nodeId: null`; row BA xác nhận không có trên màn ghi thêm
  `absent: "<lý do>"`; row ghim tay ghi `manual: true` (Mục 9). Đây là thứ cho phép sửa đúng row khi chữ trên
  Figma đổi, và là chỗ thẻ Spec ghim (Mục 9). Ghép bằng `python3 _scripts/screen-annotations.py match … --write`.
- `level` của từng màn: `row` khi màn đã có bản đồ row; mức chung của file (khoá `level` ngoài cùng) giữ nguyên cho
  các màn chưa ghép.
- Thiếu mốc (màn vẽ trước khi có rule này) → `/figma-sync` lấy Figma hiện tại làm mốc, không coi là thay đổi.

## 5. Ai gọi `/figma-sync` (DEC-052)

Figma không tự báo thay đổi, nên đồng bộ xảy ra khi **có skill đụng vào Figma**:

| Sau khi | Gọi |
|---|---|
| `/figma-screen` vẽ hoặc sửa màn (Bước 7) | `/figma-sync {feature} --flow {flow}` inline, cùng lượt |
| `/figma-userflow` vẽ lại sơ đồ của feature có trong repo | `/figma-sync {feature}` (phần userflow) |
| `/figma-component` đổi component đang dùng trên màn của feature | `/figma-sync {feature}` |
| Designer sửa tay trên Figma | User gọi `/figma-sync {feature}`, hoặc gọi trước khi chạy `/srs`, `/userstory`, `/export` |
| Hook báo task "Chốt giao diện Figma …" đã đóng tay | `/figma-sync {feature} --done --flow {flow}` |
| `/userstory` tạo hoặc sửa story có màn đã lên Figma | `/figma-sync {feature}` để ghi mã US lên thẻ Spec (Mục 9) |
| `/jira --push` ghép story với issue mới | `/figma-sync {feature}` để ghi mã Jira lên thẻ Spec (Mục 9) |

Gọi inline trong main thread (có HITL), KHÔNG Task sub-agent.

## 6. "Done" — hai đường, cùng một kết quả (DEC-054)

1. `/figma-sync` hỏi "Chốt giao diện flow {flow}?" và user trả lời **done**.
2. User đổi Trạng thái task backlog **"Chốt giao diện Figma {feature} · {flow}"** thành ✅. Hook
   `intake-sync` thấy task đóng tay mà flow chưa `approved` → in nhắc; Claude chạy `--done`.

`/figma-screen` tạo task này khi vẽ xong trọn một flow (Xong khi
`grep:docs/{feature}/screens/{feature}-screen-index.md:\({flow}\.md\).*approved`).

## 7. Thay đổi nào sửa thẳng, thay đổi nào qua `/cr`

| Thay đổi trên Figma | Sửa | Duyệt |
|---|---|---|
| Chữ nhãn, placeholder, câu thông báo | Cột Description / Items của row | L2 bảng Trước → Sau |
| Thêm/bỏ element, đổi control | Thêm/bỏ row | L2 |
| Thêm/bỏ frame trạng thái | Block `### Trạng thái` + userflow Mục 2 cột Trạng thái | L2 |
| Thêm màn, đổi/bỏ liên kết prototype | userflow Mục 1, 2, 3.5 (3.6 nếu đổi số bước) | L2 |
| Quy tắc nghiệp vụ (validation, mã lỗi mới, điều kiện, quyền) | KHÔNG sửa thẳng — nháp `/cr` | `/cr` |
| Chỉ màu, vị trí, khoảng cách | Không sửa tài liệu, chỉ cập nhật mốc | — |
| Cùng row đổi cả trên Figma lẫn trong `screens/` | Xung đột — hỏi user từng chỗ | Hỏi |
| Sửa tay thẻ Spec hoặc lớp ghim (Mục 9) | Không giữ: lần sync sau vẽ lại từ `screens/{flow}.md`. Muốn đổi nội dung thì sửa row trong `screens/` | — |

Câu chữ mới trên Figma mà trùng nghĩa với E-common/CMP → vẫn ghi theo mã (`ui-common-rules-components.md`).

## 8. SRS — Mục 10 Screens là Design (Figma), không phụ lục riêng

Mục 10 `## 10. Screens — Design (Figma)` gồm 3 phần theo thứ tự (khung: `_templates/srs-spec.md`):

| Phần | Nội dung | Ai viết |
|---|---|---|
| `### Danh mục màn` (marker `screens-catalog`) | 1 dòng/màn, mọi flow trong index: `# · Slug · Màn (screenId · tên) · Status (của flow) · Thuộc flow · Used by (FR-NNN trích từ bảng 5 cột của màn) · Mô tả (dòng **Mô tả:** của màn) · Figma` | Máy |
| `### Cấu hình UI Common Rules & Components` | CMP/GR áp ở màn nào, override + lý do; E-common dùng | Người / `/srs` |
| Khối marker `screens` | `### Màn hình flow: {tên}` cho mỗi flow `approved`: ảnh Figma + link + bảng 5 cột chép nguyên văn | Máy |

- Hai khối máy sinh bằng 1 lệnh: `python3 _scripts/screens-md.py appendix <feature> --write`. KHÔNG sửa tay,
  AI KHÔNG viết lại; sửa `screens/*.md` (qua `/figma-sync`) rồi chạy lại. Spec thiếu marker → lệnh exit 2,
  thêm 2 cặp marker theo template (L2) rồi chạy lại.
- Không còn "Phụ lục B" và không trỏ `html-wireframe/` / `ascii-wireframe/`.
- Màn mới thiếu dòng **Mô tả:** → `/figma-sync` viết 1–2 câu từ bảng 5 cột (không cần duyệt riêng, user chốt 13/10).
- `/export`, `/preview` chạy `appendix <feature> --check` trước khi xuất; cũ hoặc thiếu ảnh → cảnh báo.
  Preview không có mục Screens/Wireframes/Designs riêng khi đã có `screens/` — chỉ thêm "Màn đang vẽ" cho flow chưa chốt.

## 9. Thẻ Spec trên Figma (DEC-188)

Mỗi frame có bảng 5 cột (màn chính và từng trạng thái) có một **thẻ Spec** bên cạnh và một **lớp ghim** trên màn,
để dev đọc màn trên Figma biết từng phần tử làm gì và màn thuộc use case, story, ticket nào.

| Phần | Nội dung | Nguồn |
|---|---|---|
| Đầu thẻ | `Spec — <tên flow>`, tiêu đề `<screenId> · <slug> — <tên Việt>`, Mô tả (màn chính) | `screens/{flow}.md` |
| Mã | USE CASE · USER STORY (+ mã Jira có link) · YÊU CẦU (FR/BR/NFR) · LỖI (E) · DÙNG CHUNG (CMP/GR). Chưa có story hoặc Jira → một dòng mờ "Chưa có user story, chưa đẩy Jira" | cột Screens của `usecases/{feature}-usecase-index.md` · mục UI / Screen References của `userstories/us-*.md` · `.claude/state/atlassian/sync-state.yaml` · mã trong cột Description |
| Mỗi row | Số tròn + Items, dòng nhỏ `Control type · Data type`, gạch đầu dòng của Description nguyên văn; row chưa ghép được ghi "chưa ghim" | bảng 5 cột |
| Lớp ghim | Khung nét đứt quanh phần tử + số tròn ở góc trên trái, theo bản đồ row ↔ node (Mục 4) | mốc Figma |

- **Tên:** thẻ là frame `Ghi chú · Spec · <nodeId frame>`, lớp ghim là group `Ghi chú · Ghim · <nodeId frame>`. Đuôi là
  nodeId, không phải screenId, để `linkScreens` không khớp nhầm. Lớp ghim là **anh em** của frame màn, nằm đè lên
  màn, không lồng vào frame (prototype, bản xuất HTML, audit màn không dính ghim).
- **Chỗ đặt và cách nhìn:** `design/setup-figma.md` › *Bố cục trong Section flow* (thẻ bên phải frame; ma trận chừa chỗ).
- **Máy sinh, không sửa tay** (Mục 7): `python3 _scripts/screen-annotations.py build <feature> <flow> --json` ra nội
  dung; `match <feature> <flow> <tree.json> --write` ghép row ↔ phần tử theo tên layer và chữ, ghi vào mốc. Vẽ lại
  mỗi lần `/figma-screen` vẽ hoặc sửa màn, mỗi lần `/figma-sync` đổi row hoặc dời frame, và sau `/userstory`,
  `/jira --push` (Mục 5).
- **Ba trạng thái của một row:**

  | Trạng thái | Nghĩa | Thẻ hiện | Ai đặt |
  |---|---|---|---|
  | Đã ghim | ghép được phần tử | số tím trên màn | `match` (hoặc ghim tay `mark --node <nodeId>`, mốc ghi `manual: true`, `match` không ghi đè) |
  | Chưa ghim | máy chưa ghép được, cần xử lý | "chưa ghim" | `match` |
  | Không có trên màn | phần tử có điều kiện, không xuất hiện ở màn mẫu | "không có trên màn mẫu" + lý do, chỗ xem nếu có | BA, một lần: `mark … --absent "<lý do>"`; `match` chạy lại giữ nguyên |

  Row chưa ghim: báo tên row + màn. Phần tử có trên màn nhưng khác tên → đổi tên layer cho khớp cột Items (luật đặt
  tên layer của `/figma-screen`) rồi chạy lại `match`. Phần tử có điều kiện → `mark --absent`. **Không chốt flow
  (`/figma-sync --done`) khi còn row chưa ghim.**

## Tóm tắt 1 dòng

> **Lên Figma rồi thì bảng 5 cột sống ở `screens/{flow}.md`, wireframe flow đó bị xoá · mọi skill đụng
> Figma kết thúc bằng `/figma-sync` · chữ/element/trạng thái/luồng sửa thẳng qua L2, quy tắc nghiệp vụ qua
> `/cr` · done (user nói hoặc đóng task backlog) → ảnh 2x + danh mục và chi tiết màn máy sinh trong SRS Mục 10 ·
> mỗi frame có thẻ Spec + lớp ghim máy sinh từ bảng 5 cột, use case, story, Jira (Mục 9).**
