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
/figma-sync --done                       ảnh PNG 2x → screens/images/, flow `approved`, SRS Phụ lục B
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
      "rows": { "1": {"nodeId": "…", "text": "Dòng quy trình", "component": "Row"} },
      "texts": { "<nodeId>": "chữ hiển thị" },
      "reactions": [ {"from": "<nodeId>", "trigger": "ON_CLICK", "to": "1.2 · web"} ] } } }
```

- Ghi bởi `/figma-screen` (sau Bước 7) và `/figma-sync` (sau mỗi lần sync thành công).
- `rows` = bản đồ row bảng 5 cột → node trên Figma; đây là thứ cho phép sửa đúng row khi chữ trên Figma đổi.
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

Câu chữ mới trên Figma mà trùng nghĩa với E-common/CMP → vẫn ghi theo mã (`ui-common-rules-components.md`).

## 8. SRS

- Mục 10 Screens trỏ sang **Phụ lục B**, không trỏ `html-wireframe/`.
- Phụ lục B nằm giữa marker `<!-- screens:begin -->` / `<!-- screens:end -->`, máy sinh bằng
  `python3 _scripts/screens-md.py appendix <feature> --write` từ flow `approved`: ảnh Figma + link + bảng
  5 cột chép nguyên văn. KHÔNG sửa tay, AI KHÔNG viết lại.
- `/export`, `/preview` chạy `appendix <feature> --check` trước khi xuất; cũ hoặc thiếu ảnh → cảnh báo.

## Tóm tắt 1 dòng

> **Lên Figma rồi thì bảng 5 cột sống ở `screens/{flow}.md`, wireframe flow đó bị xoá · mọi skill đụng
> Figma kết thúc bằng `/figma-sync` · chữ/element/trạng thái/luồng sửa thẳng qua L2, quy tắc nghiệp vụ qua
> `/cr` · done (user nói hoặc đóng task backlog) → ảnh 2x + Phụ lục B máy sinh trong SRS.**
