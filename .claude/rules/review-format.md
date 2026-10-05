---
paths:
  - ".claude/agents/**"
  - ".claude/skills/urd/**"
  - ".claude/skills/brd/**"
  - ".claude/skills/prd-epic/**"
  - ".claude/skills/srs/**"
  - ".claude/skills/brainstorm/**"
  - ".claude/skills/wireframe-ascii/**"
  - ".claude/skills/wireframe-html/**"
---

# Review Finding Format‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

> Structure cho tất cả agent review outputs. các phase review tự-động trong `/urd`/`/brd`/`/prd-epic`/`/srs` parse format này để aggregate findings across agents.

## Severity levels‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

| Severity | Meaning | Effect on doc status |
|----------|---------|----------------------|
| `BLOCKING` | Must fix trước approve. Doc không proceed được. | Status → `revisions` |
| `WARNING` | Should fix. Approval khả thi với explicit ack. | Status stays `in-review`, ack note |
| `SUGGESTION` | Nice-to-have. Approval not blocked. | Status unchanged |

## Verdict semantics‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

| Verdict | When |
|---------|------|
| `approve` | Zero BLOCKING + zero WARNING (hoặc tất cả WARNING explicitly acknowledged) |
| `revise` | ≥1 WARNING, no BLOCKING |
| `block` | ≥1 BLOCKING |

## Finding anatomy‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

Mỗi finding có:

* __Title__ — 5-10 word descriptor
* __Description__ — what's wrong, why matters (1-3 sentences)
* __Location__ — section reference nếu specific (`Mục 4 Pre-conditions`, `screens/login.md Mục 2.3`)
* __Suggested fix__ — concrete next action (1-2 sentences)‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

## Aggregation rules (used by phase review trong /urd /brd /prd-epic /srs)‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

Khi multiple agents review cùng 1 doc:

1) __Deduplicate__ — same finding từ different agents counts once. Keep most detailed version.
2) __Severity escalation__ — 2+ agents flag same issue at WARNING → promote BLOCKING (consensus signals real problem).
3) __Severity ceiling__ — final verdict = highest severity from any agent.
4) __Conflict__ — Agent A approve, Agent B block → surface as conflict, user decides; không auto-resolve.

## Example output (1 agent)

```markdown
## Review by senior-ba

**Verdict:** revise

**Summary:** Spec solid overall nhưng thiếu rate-limiting consideration và 1 ambiguous actor responsibility.

### [BLOCKING]
- **Missing actor: rate limiter**: Mục 2 lists User, Backend, DB nhưng FR-payment-001 says "limit 10 attempts/hour" — ai enforce? Suggested fix: Thêm Rate Limiter là system actor trong Mục 2 hoặc clarify Mục 6 rằng Backend handles.

### [WARNING]
- **Ambiguous error E-payment-002**: Description nói "user gets error" nhưng không specify screen nào show. Suggested fix: Link error tới specific screen state trong Mục 5 Error Matrix.

### [SUGGESTION]
- **Open question stale**: OQ-2 added 2 tuần trước, chưa update. Suggested fix: ping owner hoặc escalate.
```

## Output location

Phase review aggregate findings rồi __tự fix__ (safe áp thẳng, business decision đánh 🔶 cho user review sau — theo memory `feedback_review_auto_run`). Sự kiện review ghi vào `_workspace/changelog.md` (KHÔNG ghi gì vào doc — set env note trước edit, hook lo):

```
2026-05-12 | /srs | @ba | docs/payment/srs/payment-spec.md | reviewed by @senior-ba, @qa-reviewer: 1 blocking applied, 2 warnings ack
```

## Review độc lập khi skill chạy riêng

> Áp cho skill sinh doc ngoài chuỗi `/srs`: hiện là `/brainstorm`, `/wireframe-ascii`, `/wireframe-html`.
> Lý do: skill vừa hỏi vừa tự chấm, nên tự kiểm chỉ thấy doc **đủ phần**, không thấy doc **sai nghiệp vụ**
> (thiếu vai, lấn phạm vi, thiếu nhánh lỗi, lệch đặc tả). Agent đọc nguồn độc lập để đối chiếu.

1. **Khi chạy:** sau bước tự kiểm của skill, trước khi ghi file đích. Doc chưa có trên đĩa → truyền
   **bản nháp đầy đủ** trong prompt + danh sách đường dẫn nguồn để agent Read đối chiếu.
2. **Bỏ qua khi:** gọi từ `/srs` (Phase G đã soát cả tầng) · user nói "khỏi review" · trường hợp skill tự
   nêu (vd chế độ Micro). Bỏ qua vẫn in `Review: SKIPPED — {lý do}`, không bỏ im lặng.
3. **Agent:** read-only, finding theo *Finding anatomy* ở trên; Location ghi `Mục N` của bản nháp, kèm
   **nguồn đối chiếu** `file:dòng`.
4. **Mức nặng theo bằng chứng:** BLOCKING chỉ khi trích được nguồn mâu thuẫn hoặc nguồn có mà nháp thiếu.
   Suy luận không có nguồn → tối đa WARNING. Văn phong, trình bày → SUGGESTION.
5. **Xử lý:**
   * Lỗi cơ học (mã ID, định dạng, wording lệch nguyên văn nguồn, mã lỗi sai) → skill tự sửa.
   * Finding chạm quyết định nghiệp vụ (thêm/bớt vai, phạm vi, rule, số liệu) → gom thành câu hỏi đánh số
     cho user, KHÔNG tự quyết. User trả lời hoặc "giữ nguyên" từng câu.
   * Tối đa 2 vòng; vòng 2 chỉ soát phần vừa sửa. Mỗi agent tối đa ~8 finding, nặng trước.
6. **Báo:** 1 dòng trong L1 / báo cáo cuối:
   `Review (@a, @b): N chặn · M cảnh báo · K đã tự sửa · J chờ anh quyết` + "AI đối chiếu với nguồn trong
   vault — chưa thay người duyệt" (mức 4 theo `diagram-correctness.md` Mục 2).
7. **Khác Phase G của `/srs`:** `/srs` tự fix + đánh 🔶 để user xem sau (Mục *Output location*). Skill chạy
   riêng hỏi ngay vì user đang có mặt và doc còn ở bản nháp.

## Tools agent CAN'T use directly

Agents read target doc + reference rules/templates. Agents KHÔNG:

* Edit files (orchestrator (phase review của skill sinh doc) làm — tự fix, không chờ user accept từng cái).
* Spawn other agents (tránh recursive loops).
* Run bash commands cho system state (rely on context).

Giữ agents fast + deterministic.

## Extensions (Phase 6 agents)

`@change-tracker` thêm 2 sections optional:

```markdown
### Impacted artifacts
| Path | Impact type | Severity | Recommended action |

### Non-impacted artifacts (extension)
- {path}: {why not impacted}

### Apply order (extension)
1. {first doc/action}
2. {second doc/action}
```

`/cr` analyze phase parses cả 3 sections (severity findings + impacted artifacts + apply order) để build impact report.‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍


<!-- wm:60d5580055f5e6dd44329f2c02b7fe5a -->
<sub>Tài liệu thuộc bộ AI4BA BA-Kit — bản quyền ai4ba.com</sub>
