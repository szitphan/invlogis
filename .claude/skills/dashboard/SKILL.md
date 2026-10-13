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

Có **2 bản** cùng dữ liệu: bản local `docs/_shared/dashboard.html` (chỉ xem, link mở VS Code) và **bản artifact**
trên claude.ai (link cố định ở `.claude/state/dashboard.json`) — có thao tác: kéo thẻ kanban, "Đã biết, reset" /
"Cần rà" cho stale, "Đưa vào backlog" / "Đã biết" cho việc máy, kéo thẻ Review Figma. Thao tác thành **yêu cầu**
trong kho của trang; `/dashboard sync` áp vào repo.

Trang có 5 tab (thứ tự = thứ tự quan trọng):
1) **Hôm nay** — verdict theo giai đoạn + 5 ô (Chờ bạn · Câu hỏi mở · Stale chờ xác nhận · Nguồn chưa feed · Hàng việc) + làn Chờ bạn + **hàng việc chung** (task backlog + việc máy phát hiện, xếp theo `priority_score`).
2) **Feature** — trục tiến độ 8 cột Nguồn → Brainstorm → Chốt OQ → SRS → Userflow → Figma → US/AC → Test (+3 cột ẩn URD/BRD/PRD), ô Tầng SaaS · Tham số P chưa chốt · Figma, bảng OQ còn mở có link tới đúng dòng.
3) **Kanban** — 6 cột Draft · In Review · Revisions · Approved · Shipped · Stale; doc không có status đi theo doc chỉ mục cùng folder.
4) **Nguồn khách** — mỗi SRC: tên, nhóm, thanh đối chiếu n/m (link sổ `_coverage/`), trạng thái feed; nguồn ít xử lý nhất lên đầu.
5) **Sức khỏe vault** — doc stale kèm upstream gây ra, dòng log stale trỏ file đã xoá, độ tươi (chỉ theo tuổi), review quá hạn.

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
* **Kéo thả chỉ ở bản artifact, và chỉ tạo yêu cầu** — không gì ghi vào repo khi chưa qua `/dashboard sync` + L1 (duyệt 1 lần cả lô). Đổi status luôn qua engine `/status` (`dashboard-apply.py` gọi `status.py`): luồng hợp lệ, `restore` khi rời stale, upstream chưa duyệt → giữ `pending` chờ anh xác nhận. "Đã biết" (ẩn việc máy) và thẻ Review Figma chỉ lưu trong kho trang, không cần sync.
* **`staleness.md` là file sinh** — xác nhận dòng log trỏ file đã xoá ghi vào `_workspace/stale-ack.md`, không sửa log.
* **Link 2 chế độ** — mặc định `vscode://file/<path>:<dòng>` (file local, luôn mới nhất); nút "Mở bằng: GitHub" làm dự phòng (bản đã push). Nhớ lựa chọn trong localStorage.
* **Vietnamese-first UI** — labels/headers tiếng Việt; doc titles giữ ngôn ngữ gốc.
* **Theme-aware** — token màu 2 tầng + `prefers-color-scheme` + `data-theme`.

### Pitfalls — easy to get wrong‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

* **Verdict theo giai đoạn, DETERMINISTIC** — pha = giai đoạn xa nhất của số đông feature (khám phá / đặc tả & thiết kế / bàn giao); nút thắt = cột có nhiều ô chặn nhất. **Màu** = màu tệ nhất trong 5 ô Hôm nay (bỏ xám); có việc bị chặn chờ trả lời hoặc lint FAIL → đỏ. Feature chỉ bị chấm ở cột đã tới — feature đang brainstorm KHÔNG đỏ vì thiếu US.
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

> `/dashboard sync` → nhảy tới mục **Sync** bên dưới.

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
     2 | artifact {artifact_url | (mới)}   | update | bản có thao tác (chỉ scope project)
   Apply? (Y/n):
   ```

4) **Ghi file**:
   ```bash
   python3 _scripts/dashboard-build.py [--feature <slug>]
   ```

4b) **Audit máy (lớp 1, như /figma-screen Bước 6)** — trước khi publish:
   ```bash
   python3 _scripts/dashboard-audit.py      # → .claude/state/dashboard-audit/report.md + ảnh 5 tab × 1440/400, sáng/tối
   ```
   A1 bố cục (cuộn ngang, tràn, chữ cắt, tab ẩn/hiện đúng) · A2 truy cập (tương phản AA, control thiếu tên, vùng chạm) ·
   A3 design system (màu cứng, font, thang cỡ chữ) · A4 Do's & Don'ts · A5 số liệu thị giác. **FAIL → sửa
   `dashboard-build.py` rồi chạy lại, không publish khi còn FAIL.** "Đã biết" = ngoại lệ trong design.md › Accessibility.

   **`/dashboard --review`** (lớp 2, khi đổi giao diện): sau audit 0 FAIL, gọi song song `@uxui-reviewer`
   (đủ trạng thái, khớp design.md), `@usability-reviewer` (walkthrough 4 tác vụ: hôm nay làm gì · stale xử lý
   thế nào · feature kẹt ở đâu · nguồn nào chưa feed), `@visual-reviewer` (đọc A5 + ảnh). Chỉ đọc, chỉ trả finding.
   Sửa lỗi/bổ sung trạng thái → sửa luôn; finding đổi giao diện user đã duyệt → hỏi trước (không tự áp).

5) **Bản artifact** (chỉ scope project):
   ```bash
   python3 _scripts/dashboard-build.py --artifact     # → .claude/state/dashboard-artifact.html
   ```
   Publish bằng tool Artifact. Có `artifact_url` trong `.claude/state/dashboard.json` → publish với `url` đó
   (cập nhật tại chỗ, giữ kho yêu cầu; lần đầu trong phiên phải `action: read` url trước). Chưa có → publish mới
   (`capabilities: {db: {}}`, `icon: "chart"`), rồi ghi `{"artifact_url": "<url>"}` vào `.claude/state/dashboard.json`.
   Publish là hành động ra ngoài (trang riêng tư) — đã nằm trong L1 bước 3 (thêm 1 dòng `artifact | update`).

6) **Output report** — path + link artifact + 3 điểm nổi bật lấy từ `--json` (verdict · ô có màu tệ nhất · cột trục tiến độ đang chặn nhiều feature nhất). Scope feature → nhắc "Xem global: `/dashboard`".

### Sync — `/dashboard sync`

1) Đọc `artifact_url` từ `.claude/state/dashboard.json` (không có → báo "chưa publish, chạy `/dashboard`").
2) `ArtifactData` `query` collection `requests`, `where state == pending` → ghi mảng JSON (mỗi phần tử = body + `id` = doc_id + `version`) ra file tạm.
3) `python3 _scripts/dashboard-apply.py --check <file>` → in bảng làm **L1** (1 lần cho cả lô). Mục ⚠ upstream chưa duyệt: hỏi anh từng mục; đồng ý → thêm `"confirm_upstream": true` vào yêu cầu đó.
4) Anh `Y` → `CLAUDE_CHANGELOG_AUTHOR=@<handle> python3 _scripts/dashboard-apply.py <file>` → JSON kết quả `{id, state, note}`.
5) `ArtifactData` `batch` cập nhật từng yêu cầu (`update` `state` + `note` + `appliedAt`, pin `if_version`).
6) Chạy `intake-sync.py` (chuẩn hoá backlog nếu có dòng BL mới), build lại cả 2 bản và publish lại artifact (bước 4–5 Approach, không cần L1 thêm — đã gộp trong L1 sync).
7) Báo: số áp dụng / từ chối (kèm lý do) / còn chờ.

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
| Nguồn | Mục sổ `docs-input/_coverage/*.md` thuộc feature: chắc chắn khi `➡ {feature}` hoặc path `docs/{feature}/` ở cột Ở đâu (1 mục có thể thuộc nhiều feature); đoán khi mục còn ⏳/⬜ nhắc đúng 1 tên feature ở Ở đâu/Ghi chú. `✅/tổng`; còn ⬜/⏳ nhạt · có 🔄 chặn · không mục nào xám. Mục còn chờ không gắn được feature → dòng "N mục nguồn chưa gắn feature" (tab Feature) + cột "Chưa gắn feature" (tab Nguồn khách) |
| Hàng việc · `priority_score` | Chặn 40 khi việc chạm **ô chặn chính** (ô viền đỏ đầu tiên) của feature, 25 khi chạm ô viền đỏ khác, 0 nếu không — "chạm" = đường dẫn file của ô hoặc từ khoá cột có trong nội dung việc + Xong khi (KHÔNG xét cột Nguồn; ô OQ chỉ theo từ khoá vì dùng chung file brainstorm) + Hạn 25 (≤7 ngày) / 15 (≤14 ngày) từ cột **Hạn** backlog + Lan 4đ mỗi feature/doc nhắc tới (trần 20) + Tuổi 1đ/2 ngày (trần 15). Cột **Ưu tiên** backlog: `P0` luôn đầu, `để sau` luôn cuối. Việc máy: doc stale (gom theo feature), OQ mở chưa có task, lint FAIL, audit Figma Cao, nguồn 🔄, worktree không theo `feat/*`, việc engine (review kẹt, US thiếu AC…) |
| Tầng SaaS · Tham số P | FAIL/WARN `saas-layer-lint` cộng trên mọi spec · dòng `P-…` trong `docs/_product/tenant-parameters.md` có "chưa chốt" |
| Brainstorm | `brainstorms/{feature}.md`: approved đậm · stale chặn · còn lại nhạt |
| Chốt OQ | Số OQ mở trong mọi doc của feature; còn mở + đã có brainstorm = chặn |
| SRS | `srs/{feature}-spec.md`: số FR + FAIL/WARN `saas-layer-lint`; FAIL hoặc spec stale = chặn |
| Userflow | `srs/{feature}-userflow.md` + node mồ côi từ KG |
| Figma | Số file `screens/*.md` + audit `figma-audit` mới nhất; còn mục Cao = chặn |
| US/AC · Test | Coverage FR↔US, UC có test (từ `workspace-status.py`); US mồ côi = chặn |
| Stale chờ xác nhận | Doc `status: stale` + dòng `_workspace/staleness.md` có file đích không còn |
| Độ tươi | 100 = mới; −1đ/ngày sau 7 ngày ân hạn; KHÔNG phạt stale |
| Câu hỏi mở theo tuần | `git grep` bảng `\| OQ-n \|` tại commit cuối mỗi Chủ nhật (8 tuần, mọi folder feature lúc đó) + working tree hôm nay; ◆ = tuần có file `docs/meetings/decks/` |
| Review Figma | Mục bảng "Mức Cao/Trung/Thấp" của audit mới nhất mỗi feature. Cột máy: Mới · Đang sửa (`_workspace/figma-runs.md` có "bắt đầu" chưa "xong") · Chờ đo lại ("xong" từ ngày audit trở đi) · Xong (audit trước có, audit mới không). Kéo tay lưu ở kho trang, đè cột máy |

## References

* @../../../_scripts/dashboard-build.py (nguồn duy nhất: số liệu + HTML, `--artifact`, `--line`)
* @../../../_scripts/dashboard-audit.py (lớp 1 máy đo: A1–A5 bằng Chromium headless)
* @../../../_scripts/dashboard-apply.py (`/dashboard sync`: kiểm + áp yêu cầu từ trang)
* @../status/SKILL.md (engine đổi status mà dashboard-apply gọi)
* @../../rules/kg-usage.md (KG: node mồ côi userflow)
* @../../rules/naming-conventions.md
* @../../rules/status-lifecycle.md
* @../../rules/delivery-readiness.md
* @../../rules/approval-gate.md
* @../../rules/feature-bootstrap.md
* @../kg/SKILL.md (orphans query)
* @../../../_scripts/workspace-status.py (docs, coverage, action items, freshness, quality — script gọi như module)‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍


<!-- wm:60d5580055f5e6dd44329f2c02b7fe5a -->
<sub>Tài liệu thuộc bộ AI4BA BA-Kit — bản quyền hoangphan.blog</sub>
