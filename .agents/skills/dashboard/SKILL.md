---
name: dashboard
description: Dùng khi cần dashboard HTML trực quan tổng hợp toàn bộ workspace BA — kanban theo status, coverage/traceability thật (FR↔US↔AC↔test), tiến độ pipeline per-feature, chỉ số chất lượng/rủi ro, và action items ưu tiên. `/dashboard` hoặc `/dashboard <feature>`.
allowed-tools: Read, Write, Bash, Glob, Grep
user-invocable: true
disable-model-invocation: true
argument-hint: "[<feature>]"
---
<!-- Licensed to test.innvie@gmail.com — Order 56EB8MCXD -->

# /dashboard — BA Workspace HTML Dashboard‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

## Goal‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

Sinh 1 file HTML self-contained **đọc là hiểu liền**: mở lên biết ngay vault đang ở giai đoạn nào, nút thắt ở đâu, việc gì chờ bạn — rồi mới tới bằng chứng chi tiết.

Toàn bộ số liệu VÀ HTML do **`_scripts/dashboard-build.py`** sinh tất định (cùng đầu vào → cùng file, chỉ ghi ngày). Claude không tự đếm, không tự ghép HTML: chạy script, duyệt L1, báo cáo. Thiết kế chốt ở đề xuất *Dashboard BA v2* (artifact https://claude.ai/artifact/631W9qLYmsCQ9z8Zyb7Cp7, 3 vòng phản hồi 2026-10-13); việc còn lại theo đợt ở backlog BL-097 (P0) · BL-098 (P1) · BL-099 (P2).

Trang có 4 tab (thứ tự = thứ tự quan trọng):
1) **Hôm nay** — verdict theo giai đoạn + 5 ô (Chờ bạn · Câu hỏi mở · Stale chờ xác nhận · Nguồn chưa feed · Backlog mở) + làn Chờ bạn + việc máy phát hiện.
2) **Feature** — trục tiến độ 8 cột Nguồn → Brainstorm → Chốt OQ → SRS → Userflow → Figma → US/AC → Test (+3 cột ẩn URD/BRD/PRD), bảng OQ còn mở có link tới đúng dòng.
3) **Kanban** — 6 cột Draft · In Review · Revisions · Approved · Shipped · Stale; doc không có status đi theo doc chỉ mục cùng folder.
4) **Sức khỏe vault** — doc stale kèm upstream gây ra, dòng log stale trỏ file đã xoá, độ tươi (chỉ theo tuổi), review quá hạn.

> **Nguyên tắc report tốt (BẮT BUỘC theo):** kết luận lên trên, bằng chứng xuống dưới. Feature/việc **có vấn đề xếp trước**. Giữ mã thật (FR/OQ/BL) + lệnh chạy. Muốn đổi bố cục/logic → sửa `dashboard-build.py`, KHÔNG sửa HTML sinh ra.

> Đây là skill DUY NHẤT cho việc quan sát trạng thái vault (skill `/health` console đã bỏ 2026-07-13).

## Constraints‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

### Hard rules — never violate‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

* **L1 approval** trước khi script ghi file (file generated, vẫn tính action).
* **Output path theo scope** — project-wide: `docs/_shared/dashboard.html` (re-run overwrite). Per-feature: `docs/_shared/dashboard-{feature}.html` (path RIÊNG, KHÔNG đè bản project-wide).
* **Script là nguồn duy nhất** — `dashboard-build.py` gọi `workspace-status.py` (docs, coverage FR↔US↔UC, action items, freshness, quality), `queue.py --json` (làn Chờ bạn), `saas-layer-lint.py` (FAIL/WARN của spec), `kg-query.mjs orphans` (node mồ côi userflow; KG lỗi → ô ghi chú, không crash), và đọc `backlog.md`, `staleness.md`, `docs-input/README.md`, `docs/reports/figma-audit/`. KHÔNG suy diễn lại con số bằng prompt.
* **Self-contained, không CDN** — CSS/JS inline, chạy offline.
* **Read-only data scan** — KHÔNG edit doc nào.
* **Làn "Chờ bạn"** — nguồn duy nhất là `_scripts/queue.py --json`; scope feature thì lọc theo `feature`.
* **Kéo thả** — dashboard HTML tĩnh chỉ để xem. Đổi trạng thái bằng kéo thả (đóng task, duyệt card + chạy, duyệt land) nằm ở board artifact `/board` (cùng nguồn `queue.py`, qua `_scripts/board-snapshot.py`); dashboard ghi link board ở header nếu có `.claude/state/board.json`.
* **Link 2 chế độ** — mặc định `vscode://file/<path>:<dòng>` (file local, luôn mới nhất); nút "Mở bằng: GitHub" làm dự phòng (bản đã push). Nhớ lựa chọn trong localStorage.
* **Vietnamese-first UI** — labels/headers tiếng Việt; doc titles giữ ngôn ngữ gốc.
* **Theme-aware** — token màu 2 tầng + `prefers-color-scheme` + `data-theme`.

### Pitfalls — easy to get wrong‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

* **Verdict theo giai đoạn, DETERMINISTIC** — pha = giai đoạn xa nhất của số đông feature (khám phá / đặc tả & thiết kế / bàn giao); nút thắt = cột có nhiều ô chặn nhất. Feature chỉ bị chấm ở cột đã tới — feature đang brainstorm KHÔNG đỏ vì thiếu US.
* **OQ mở ≠ mọi dòng OQ** — dòng `| OQ-n |` có ô cuối bắt đầu bằng *Đã chốt / Đóng / Bỏ* là đã đóng. Số "Câu hỏi mở" chỉ đếm phần còn lại.
* **Độ tươi chỉ theo tuổi** — cờ stale có đèn/ô riêng; KHÔNG trộn (1 nguyên nhân đỏ 2 đèn).
* **US/AC có FR mà chưa có US nào** = xám "0/N" (chưa tới), không phải đang làm.
* **Coverage `null` ≠ 0%** — feature chưa có FR hiện xám, KHÔNG "0% đỏ".
* **Feature folder nhiễu** — script bỏ folder bắt đầu `_`, `zz-*`, và meta (`meetings`, `exports`, `reports`, `cr`, `inbox`, `userguide`, `guides`).
* **Empty vault** — verdict "Chưa có feature nào" + gợi ý `/brainstorm` hoặc `/intake`. KHÔNG bịa số.

## Inputs

```
/dashboard              # project-wide dashboard
/dashboard <feature>    # scope 1 feature (vd /dashboard cross-process-flow)
```

Feature không tồn tại / vault rỗng → theo `feature-bootstrap.md` Nhóm C: friendly empty-message, KHÔNG bịa data.

## Approach

1) **Resolve scope.** No-arg → project. `<feature>` → `--feature <slug>`.

2) **Lấy số cho L1** (không ghi file):
   ```bash
   python3 _scripts/dashboard-build.py [--feature <slug>] --summary
   ```
   In ra path đích, verdict, số feature/doc/OQ mở/nguồn/task mở, dung lượng.

3) **Approval L1** — in plan preview theo `approval-gate.md` từ output bước 2:
   ```
   [/dashboard] Sẽ thực hiện:
     # | path                              | action | summary
     1 | docs/_shared/dashboard{-feature}.html | update | {verdict ngắn} · {N} OQ mở · {M} doc
   Apply? (Y/n):
   ```

4) **Ghi file**:
   ```bash
   python3 _scripts/dashboard-build.py [--feature <slug>]
   ```

5) **Output report** — path + "mở bằng trình duyệt" + 3 điểm nổi bật lấy từ `--json` (verdict · ô có màu tệ nhất · cột trục tiến độ đang chặn nhiều feature nhất). Scope feature → nhắc "Xem global: `/dashboard`".

## Output

| Scope | File |
|---|---|
| Toàn dự án | `docs/_shared/dashboard.html` |
| 1 feature | `docs/_shared/dashboard-{feature}.html` (path RIÊNG, KHÔNG đè bản project-wide) |

`python3 _scripts/dashboard-build.py --json` in data model (verdict, tiles, lanes, features[].stages, kanban, stale_docs, stale_log…) để debug hoặc trả lời câu hỏi về số liệu.

## Metric definitions (để đọc đúng, không bịa)

| Metric | Cách tính (trong `dashboard-build.py`) |
|--------|------------------|
| Ô trục tiến độ | `done` đậm = bước xong theo điều kiện máy · `part` nhạt + số = đang làm · `block` viền đỏ = đang giữ feature lại · `none` xám = chưa tới |
| Nguồn | Tạm `?` — cần cột feature trong sổ đối chiếu `docs-input/_coverage/` (đợt P1) |
| Brainstorm | `brainstorms/{feature}.md`: approved đậm · stale chặn · còn lại nhạt |
| Chốt OQ | Số OQ mở trong mọi doc của feature; còn mở + đã có brainstorm = chặn |
| SRS | `srs/{feature}-spec.md`: số FR + FAIL/WARN `saas-layer-lint`; FAIL hoặc spec stale = chặn |
| Userflow | `srs/{feature}-userflow.md` + node mồ côi từ KG |
| Figma | Số file `screens/*.md` + audit `figma-audit` mới nhất; còn mục Cao = chặn |
| US/AC · Test | Coverage FR↔US, UC có test (từ `workspace-status.py`); US mồ côi = chặn |
| Stale chờ xác nhận | Doc `status: stale` + dòng `_workspace/staleness.md` có file đích không còn |
| Độ tươi | 100 = mới; −1đ/ngày sau 7 ngày ân hạn; KHÔNG phạt stale |

## References

* @../../../_scripts/dashboard-build.py (nguồn duy nhất: số liệu + HTML)
* @../../../.claude/rules/kg-usage.md (KG: node mồ côi userflow)
* @../../../.claude/rules/naming-conventions.md
* @../../../.claude/rules/status-lifecycle.md
* @../../../.claude/rules/delivery-readiness.md
* @../../../.claude/rules/approval-gate.md
* @../../../.claude/rules/feature-bootstrap.md
* @../kg/SKILL.md (orphans query)
* @../../../_scripts/workspace-status.py (docs, coverage, action items, freshness, quality — script gọi như module)‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍


<!-- wm:60d5580055f5e6dd44329f2c02b7fe5a -->
<sub>Tài liệu thuộc bộ AI4BA BA-Kit — bản quyền hoangphan.blog</sub>
