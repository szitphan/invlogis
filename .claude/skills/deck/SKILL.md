---
name: deck
description: Dùng khi cần chuẩn bị slide họp với khách theo mục tiêu buổi họp (hiện có kịch bản chốt câu hỏi mở — mỗi câu 1 slide) → ra 1 file HTML để chiếu khi họp hoặc gửi khách tự trả lời, ghi quyết định ngay trên slide rồi đưa kết quả về tài liệu. `/deck <mục tiêu họp> [--feature <slug>]` · `/deck import <file-ket-qua.md>`.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, AskUserQuestion
user-invocable: true
argument-hint: "<mục tiêu họp> [--feature <slug>] | import <file-ket-qua.md> | <deck.md>"
---

# /deck — Slide họp khách theo mục tiêu buổi họp

## Goal

Dựng bộ slide cho **một buổi họp với khách**, đi theo kịch bản của loại họp, lấy nội dung từ tài liệu
BA trong vault, và trình chiếu được ngay bằng một file HTML (double-click, chạy offline, share screen).

Khác các công cụ làm slide chung chung ở 3 điểm:

1. **Kịch bản theo mục tiêu họp.** Mỗi loại họp có trình tự slide cố định (`references/recipe-*.md`).
   MVP có một kịch bản: **chốt câu hỏi mở** — mỗi câu hỏi 1 slide, có bối cảnh, phương án và đánh
   đổi, đề xuất của BA, ô ghi quyết định.
2. **Ghi quyết định trong lúc họp.** Bấm chọn phương án / Khác / Hoãn + gõ ghi chú ngay trên slide.
   Slide Tổng kết tự điền, rồi tải ra file kết quả `.md`.
3. **Kết quả quay về tài liệu.** `/deck import` đọc file kết quả → cập nhật câu hỏi gốc (L2) + ghi
   biên bản họp.

Hai hình thức (frontmatter `delivery`), **hỏi user mỗi lần tạo deck mới**:

| `delivery` | Dùng khi | Khác biệt |
|---|---|---|
| `meeting` | BA chiếu trong buổi họp, ghi quyết định thay khách | Có cửa sổ người trình bày (ghi chú, mã, nguồn), đồng hồ |
| `async` | Gửi thẳng file HTML cho khách tự đọc và trả lời | Build tự chèn slide **Hướng dẫn trả lời** sau bìa; có nút ‹ › trên màn; slide Tổng kết có ô tên người trả lời + nút Tải câu trả lời; **không nhúng** ghi chú, nguồn, đề xuất nội bộ vào file |

Output gồm 2 file cạnh nhau: `deck.md` (nguồn, sửa được, diff git được) và `deck.html` (máy sinh từ
`deck.md` qua `engine/build-deck.py`, KHÔNG viết tay).

## Constraints (must follow)

### Hard rules — never violate

- **AI chỉ viết `deck.md`. HTML do `engine/build-deck.py` sinh.** Không tự viết/sửa file `.html`. Muốn
  đổi slide → sửa `deck.md` → build lại.
- **Lint là gate.** `build-deck.py` exit 1 thì KHÔNG giao file: sửa `deck.md` theo từng dòng `✗` rồi
  build lại. Không dùng `--force` trừ khi user yêu cầu rõ.
- **Ẩn mã nội bộ khỏi slide khách.** FR/BR/E/OQ/UC/US/CR/OBJ/CMP…, đường dẫn `docs/…`, tên file `.md`
  chỉ được nằm trong directive (`id`/`src`/`refs`) hoặc `::: notes`. Lint chặn bằng regex
  (`INTERNAL_ID`, `INTERNAL_PATH` trong `build-deck.py`).
- **Không bịa nội dung.** Câu hỏi lấy từ nguồn thật. Phương án, bối cảnh, số liệu phải có gốc (tài liệu,
  SOP, hiện trạng khách đã nói); gốc ghi trong notes. Không có cơ sở thì bỏ phương án (slide thành câu
  hỏi mở với ô trả lời) và không đặt `recommend`. Xem `recipe-open-questions.md` mục "Phương án — chống bịa".
- **Mỗi slide `oq` có dòng `**Tài liệu:**` cho khách đọc lại** — tên tài liệu như khách gọi (kèm ngày bản) +
  số mục và tên mục theo bản gốc của khách. KHÔNG ghi đường dẫn, số dòng của bản `.md` nội bộ (lint chặn), KHÔNG
  dẫn tài liệu do đội tự viết. Câu không có tài liệu gốc → `**Tài liệu:** chưa có trong tài liệu {khách} gửi`.
  Thiếu dòng này → lint cảnh báo (`DOC_LABEL` trong `build-deck.py`).
- **Lời của khách, không phải lời đội.** Câu hỏi viết lại bằng thuật ngữ nghiệp vụ (đọc
  `docs/_shared/project-profile.md` mục "Người dùng & thuật ngữ" theo `project-profile.md`); không hỏi
  khách về DB/API/kỹ thuật (IT-BA framing, `ba-conventions.md` Mục 3).
- **HITL đủ 3 tầng:** L3 dàn ý slide trong chat (tối đa 3 vòng) → L1 prose BA-friendly
  (`ba-conventions.md` Mục 5) → Write `deck.md` → build. File đã có → L2 diff. `/deck import` sửa doc
  nguồn → L2 cho từng file.
- **Không tự chọn câu hỏi im lặng.** Liệt kê câu hỏi tìm được, user chọn câu nào đưa vào buổi họp.
- **Mục tiêu họp chưa có kịch bản** → nói rõ "chưa có kịch bản `{loại}` — hiện chỉ có Chốt câu hỏi
  mở", đề nghị dùng kịch bản đó hoặc dựng deck khung chung (`title`/`goal`/`bullets`/`recap`/`end`) mà
  không bịa cấu trúc riêng.
- **Brand thuộc dự án, không thuộc skill.** Màu + logo đơn vị trình bày đọc từ `design/brand/{slug}/brand.yml`
  (frontmatter `brand:`; xem `deck-format.md` mục Brand). KHÔNG ghi màu/logo/tên công ty vào `.claude/`.
  Logo mới do user cung cấp → tách nền trong suốt, đặt vào `design/brand/{slug}/` qua L1.
- **Hình thức luôn hỏi.** Tạo deck mới → hỏi "họp trực tiếp hay gửi khách tự trả lời" (AskUserQuestion),
  KHÔNG suy từ mục tiêu họp rồi tự chọn. Build lại deck có sẵn → dùng `delivery` trong frontmatter, không hỏi.
- **`async`: slide phải tự đủ nghĩa.** Không có người trình bày để giải thích và ghi chú KHÔNG được gửi đi,
  nên điều khách cần biết (lý do đề xuất, ảnh hưởng) phải nằm trên slide, không chỉ trong notes. Slide
  hướng dẫn do build sinh — AI KHÔNG viết slide hướng dẫn riêng (lint chặn layout `guide` viết tay).
- **Changelog:** set env `CLAUDE_SKILL_NAME=deck`, `CLAUDE_CHANGELOG_NOTE`, `CLAUDE_CHANGELOG_AUTHOR`
  (memory `user-identity`, `ba-conventions.md` Mục 1) trước mỗi Write/Edit.

### Pitfalls — easy to get wrong

- **Copy nguyên văn câu hỏi gốc lên slide.** Câu gốc thường chứa mã + tên mục + trích dẫn
  (`lg-srs-export.md:3059`). Viết lại; giữ trích dẫn trong notes.
- **Một slide hỏi hai quyết định.** Câu gốc có "và"/"hay" nối 2 ý → tách slide, hoặc đưa ý phụ vào notes.
- **Phương án viết từ góc đội** ("dễ làm", "đỡ sửa DB"). Viết theo tác động lên khách: tốc độ, kiểm
  soát, chi phí vận hành, trải nghiệm.
- **Quá giờ.** Tổng `time` các slide `oq` + ~10 phút mở/đóng vượt `duration` → hỏi user bỏ bớt / tách
  buổi, không tự cắt.
- **Verify `SKIPPED` không phải PASS.** Không có Chrome thì báo rõ tầng hiển thị chưa được đo.
- **localStorage theo máy và trình duyệt.** Quyết định ghi trong buổi họp chỉ nằm ở trình duyệt đã chiếu.
  Nhắc user **tải kết quả trước khi đóng tab** (slide Tổng kết hoặc phím E). Với `async` thì slide
  hướng dẫn đã dặn khách mở lại trên cùng máy, cùng trình duyệt.
- **`async`: khách mở trong khung xem trước của email/Zalo** thì có thể không lưu được câu trả lời.
  Slide hướng dẫn dặn "lưu file về máy rồi mở bằng trình duyệt"; trình duyệt chặn lưu thì file tự hiện
  cảnh báo "trả lời hết và tải trong một lần".
- **Sửa `deck.md` sau khi đã họp:** quyết định đã ghi gắn theo `id`, nên đổi `id` thì mất liên kết.
  Giữ nguyên `id`.

## Inputs

| Input | Bắt buộc | Nguồn |
|---|---|---|
| Mục tiêu họp | Có | Arg hoặc hỏi. Hiện nhận diện: câu hỏi mở / open questions / OQ / chốt / làm rõ → kịch bản `open-questions` |
| Phạm vi | Không | `--feature <slug>`, hoặc nói tên feature, hoặc cấp dự án |
| Hình thức: họp / gửi khách tự trả lời | Có | **Luôn hỏi** khi tạo mới (AskUserQuestion) → `delivery: meeting \| async` |
| `meeting`: khách dự họp + thời lượng + ngày | Có | Hỏi 1 lượt (AskUserQuestion), bỏ câu đã có trong arg/profile |
| `async`: khách nhận + người nhận câu trả lời + hạn trả lời | Có (hạn tuỳ chọn) | Hỏi 1 lượt → `client`, `reply_to` (tên/email hiện cho khách), `reply_by`. Không hỏi thời lượng |
| Nguồn câu hỏi | Tự dò | Xem Phase B |

## Context (dynamic)

Today: !`date +%Y-%m-%d`
Features: !`ls -d docs/*/ 2>/dev/null | xargs -I{} basename {} | grep -v '^_' | head -20`
Brand: !`ls design/brand/*/brand.yml 2>/dev/null || echo "(chưa có — deck dùng màu trung tính)"`
Deck đã có: !`ls docs/meetings/decks/*-deck.md 2>/dev/null | tail -10 || echo "(chưa có)"`
File có câu hỏi mở: !`grep -rlE "^\| *OQ-[0-9]+|^[-*] \[ \] *OQ-|^## .*(Open Questions|Câu hỏi mở)" docs --include='*.md' 2>/dev/null | grep -v "/meetings/decks/" | head -20`
Chrome (verify): !`ls ~/Library/Caches/ms-playwright/chromium_headless_shell-*/chrome-headless-shell-*/chrome-headless-shell 2>/dev/null | tail -1 || ls "/Applications/Google Chrome.app" 2>/dev/null || echo "không có — verify sẽ SKIPPED"`

## Approach

### Phase A — Xác định chế độ

1. Arg là `import <file>` → **Phase G**. Arg là đường dẫn `*-deck.md` có sẵn → **build lại**: L1 1 dòng
   ("build lại {file}.html từ {file}.md") → Phase F bước 15.
2. Còn lại là **tạo mới**: xác định kịch bản từ mục tiêu họp. Không khớp kịch bản nào → báo theo Hard
   rule "chưa có kịch bản", hỏi user chọn.
3. Đọc kịch bản `references/recipe-{meeting}.md` + `references/deck-format.md`.

### Phase B — Gom câu hỏi (kịch bản open-questions)

4. Dò nguồn câu hỏi mở theo phạm vi. Có `--feature` → trong `docs/{feature}/` (+ `docs/_reverse/{feature}/`);
   cấp dự án → toàn `docs/`. Thứ tự ưu tiên:
   - `srs/{feature}-spec.md` Mục Open Questions (canonical khi có SRS)
   - `brainstorms/*.md`, `{feature}-brd.md`, `{feature}-urd.md`, `{feature}-prd.md` Mục Open Questions
   - `docs/_shared/object-map.md` / `{feature}-object-map.md` Mục "Câu hỏi mở"
   - `docs/_reverse/{feature}/reverse-gaps.md`
   - `docs/_research/*.md`, `docs/cr/CR-*.md` Mục Open Questions
   Có KG thì `kg facts <feature>` liệt kê OQ (theo `kg-usage.md`: kg để CHỌN, đọc prose để viết).
5. Bỏ câu đã đóng (`[x]`, có cột trả lời, ghi "đã chốt"). Gộp câu trùng nghĩa ở nhiều file (giữ nguồn
   canonical làm `src`, nguồn khác vào notes).
6. Không tìm thấy câu nào → nhóm C (`feature-bootstrap.md`): "Chưa thấy câu hỏi mở nào còn treo trong
   {phạm vi}. Câu hỏi mở thường sinh từ `/brainstorm`, `/srs`, `/object-map`." Dừng.
7. Trình danh sách cho user: bảng `# · câu hỏi (rút gọn) · nguồn · chặn gì`. User chọn câu nào đưa vào
   (mặc định đề xuất câu chặn nhiều nhất trước). Cùng lượt AskUserQuestion, **luôn hỏi hình thức**:
   - **Họp trực tiếp** (`meeting`) → hỏi kèm khách dự là ai, thời lượng, ngày họp.
   - **Gửi khách tự trả lời** (`async`) → hỏi kèm khách nhận là ai, câu trả lời gửi về cho ai (tên +
     email/kênh, hiện nguyên văn trên slide hướng dẫn), hạn trả lời.
   Chỉ hỏi phần chưa biết (no-re-ask), riêng hình thức thì luôn hỏi.

### Phase C — Đọc nguồn để viết slide

8. Với mỗi câu đã chọn: Read **đoạn prose quanh câu hỏi** + mục nó trỏ tới (cột "Liên quan", số mục,
   trích dẫn file:dòng) để có bối cảnh, hiện trạng, các hướng đã nêu. Đây là chỗ lấy phương án, KHÔNG
   suy diễn từ tên câu hỏi.
9. Đọc profile để lấy thuật ngữ khách (`project-profile.md` cơ chế 4 bước; thiếu thì dùng "người
   dùng", không chặn luồng).

### Phase D — L3 dàn ý

10. In dàn ý trong chat theo kịch bản, mỗi slide 1–3 dòng: layout · tiêu đề/câu hỏi · phương án (chữ +
    tên) · đề xuất · thời lượng. Cuối dàn ý: tổng thời lượng so với `duration`, câu nào không có
    phương án (vì sao).
    `Phiên bản N — Đồng ý / Sửa: … / Hủy`. Tối đa 3 vòng (`approval-gate.md` L3).

### Phase E — L1 + viết deck.md

11. L1 theo `ba-conventions.md` Mục 5 (prose, không bảng path/action):
    > Em sẽ tạo bộ slide `docs/meetings/decks/{date}-{meeting-slug}-{slug}-deck.md` (+ bản trình chiếu
    > `.html`) cho buổi họp {ngày} với {khách}: {N} câu hỏi, {M} slide, khoảng {T} phút … Apply? (Y / sửa)
12. Viết `deck.md` theo `deck-format.md` và trình tự slide của hình thức đã chọn
    (`recipe-open-questions.md`). Frontmatter: `type: meeting-deck` · `meeting` · `delivery` · `feature`
    (nếu có) · `title` · `client` · `date` · `duration` (chỉ `meeting`) · `reply_to` + `reply_by` (chỉ `async`) · `brand` (khi có nhiều brand hoặc cần tắt) · `status: draft` · `updated` · `links` (mọi
    file nguồn đã dùng). Mỗi slide `oq` PHẢI có `id` + `src`.

### Phase F — Build + verify

13. ```bash
    python3 .claude/skills/deck/engine/build-deck.py <deck.md> --verify --shots <scratchpad>/deck-shots
    ```
14. Exit 1 → sửa `deck.md` theo từng `✗`, build lại (L2 nếu sửa sau khi user đã xem). Cảnh báo co chữ
    `⚠ … co chữ còn N%` → rút gọn slide đó.
15. Xem ảnh `--shots` của slide bìa, slide Hướng dẫn (`async`), 1–2 slide `oq` và slide Tổng kết (Read PNG) để tự soi trước khi
    giao: chữ đè, thẻ lệch, nhãn đề xuất sai chỗ. Đây là phần "Mức 4" máy không kiểm.
16. `open <deck.html>` để user xem.
17. User cần **bản PDF đọc nhanh** (gửi kèm để khách lướt qua, in, xem trên điện thoại) → build thêm `--pdf`:
    ra `{…}-deck.pdf` cạnh file HTML, mỗi slide 1 trang, BỎ slide hướng dẫn + tổng kết + thanh nút trả lời
    (`?pdf` trong template); bản `async` có dòng "trả lời trong file HTML gửi kèm" ở bìa. Build kiểm số trang
    khớp — lệch là FAIL. PDF chỉ để đọc; câu trả lời vẫn đi qua file HTML.

### Phase G — `/deck import <file-ket-qua.md>` (sau buổi họp)

17. Read file kết quả (frontmatter `type: deck-result`, `deck: <đường dẫn deck.md>`) + deck.md gốc.
    `async` còn có dạng **thư trả lời** khách dán vào email/Zalo (nút "Copy để dán vào email"): khối
    `Câu N. {câu hỏi}` + `Trả lời: …` + `Ý kiến thêm: …`, ký tên cuối thư. User dán vào chat hoặc lưu
    thành file → ghép theo **số thứ tự câu hỏi `oq` trong deck + đối chiếu nguyên văn câu hỏi**; lệch
    (khách sửa chữ, thiếu câu) → báo từng câu, hỏi user, không đoán. Thư không có frontmatter → hỏi user
    deck nào (đề xuất theo tên bộ câu hỏi ở câu mở đầu thư).
    Kiểm tra mọi `Mã` trong bảng có trong deck. Lệch → báo, không đoán. Cột `Nguồn` trống (file `async`
    không mang đường dẫn nội bộ) → lấy `src` từ slide cùng `id` trong deck.md.
    `delivery: async` có thể về **nhiều file** (mỗi người trả lời 1 file, frontmatter `respondent`): nhận
    nhiều file 1 lượt, cùng câu mà các người trả lời khác nhau → trình bảng so sánh, user chọn câu trả lời
    chốt, KHÔNG tự chọn. Câu trả lời của khách ghi kèm tên người trả lời.
18. Với mỗi câu **đã chốt** (không phải "Chưa chốt"/"Chưa trả lời"/"Hoãn"/"Cần trao đổi thêm"): mở file `src`, đánh dấu câu hỏi đã có
    trả lời theo **format sẵn có của file đó**:
    - checklist `- [ ] OQ-n: …` → `- [x] OQ-n: … — **Chốt {date}:** {quyết định}{; ghi chú}`
    - bảng (`| OQ-n | Câu hỏi | … |`) → thêm cột `Trả lời` nếu chưa có, điền `{date}: {quyết định}`
    - format khác → đề xuất cách ghi, hỏi user
    Câu **Hoãn** / **Cần trao đổi thêm** → giữ mở, thêm `(hoãn {date})` / `(khách cần trao đổi thêm {date})`. Mỗi file nguồn 1 L2 diff. Không tự sửa nội dung
    nghiệp vụ khác (FR/BR/flow) — liệt kê "cần cập nhật theo quyết định" và gợi ý `/cr`.
19. Ghi biên bản `docs/meetings/{date}-oq-{slug}.md` (L1; `async` thì là bản ghi nhận câu trả lời, nêu người trả lời + ngày nhận): frontmatter `type: meeting`, `status: draft`,
    `updated`, `links` (deck + file nguồn); bảng Quyết định (câu hỏi · quyết định · ghi chú), bảng Còn
    mở (câu hoãn/chưa chốt · ai trả lời · hạn — hỏi user), bảng Việc tiếp theo.
20. Deck gốc → `status: shipped` (đã dùng trong buổi họp) qua L2.

## Output

| File | Nội dung |
|---|---|
| `docs/meetings/decks/{YYYY-MM-DD}-{meeting-slug}-{slug}-deck.md` | Nguồn slide (`type: meeting-deck`). `meeting-slug`: `oq` cho kịch bản open-questions |
| `docs/meetings/decks/{…}-deck.html` | Bản trình chiếu, máy sinh, 1 file, chạy offline |
| `docs/meetings/decks/{…}-deck.pdf` | Bản đọc nhanh (chỉ khi build `--pdf`), máy sinh — không trả lời được |
| `{…}-ket-qua.md` | Kết quả họp (`meeting`), **user tải từ trình duyệt** (vào thư mục Downloads) — input cho `/deck import` |
| `{…}-tra-loi.md` | Câu trả lời (`async`), **khách tải rồi gửi lại** qua email/Zalo — input cho `/deck import` |
| Thư trả lời (dán) | `async`: khách bấm "Copy để dán vào email" → thư viết thường, đánh số câu (có in đậm khi dán vào Gmail/Outlook) — cũng là input cho `/deck import` |
| `docs/meetings/{YYYY-MM-DD}-oq-{slug}.md` | Biên bản (chỉ khi `/deck import`) |

**Báo cáo cuối** — in tách 4 mức như build-deck.py in ra (cú pháp · lint · hiển thị · nghiệp vụ chưa
được máy kiểm), kèm phím tắt khi trình chiếu:

```
← → / Space  chuyển slide        F  toàn màn hình       O  xem lưới mọi slide
P  mở cửa sổ người trình bày (ghi chú, đồng hồ, slide kế) — chỉ share cửa sổ slide
E  tải kết quả họp (.md)          In (Cmd+P) → mỗi slide 1 trang PDF
```

Nhắc: tải kết quả trước khi đóng trình duyệt, rồi `/deck import <file>`.

Với `async` thay phần phím tắt bằng hướng dẫn gửi đi: gửi **chỉ file `.html`** (không gửi `deck.md`),
khách làm theo slide Hướng dẫn và gửi lại file `{…}-tra-loi.md` (hoặc nội dung Copy dán vào email) →
`/deck import <file>`. Muốn xem trước như khách thấy: mở file `.html` và đi từ slide 2.

## References

- @references/deck-format.md — cú pháp `deck.md`, directive, layout, luật lint
- @references/recipe-open-questions.md — kịch bản chốt câu hỏi mở
- @engine/build-deck.py — parse + lint + render + verify (Chrome headless)
- @engine/deck-template.html — khung trình chiếu (điều hướng, presenter, ghi quyết định, in PDF)
- @fixtures/ — `deck-valid.md` + `deck-async.md` phải PASS, `deck-leak.md` phải FAIL (chạy lại sau khi sửa engine)
- @../../rules/approval-gate.md
- @../../rules/ba-conventions.md
- @../../rules/project-profile.md
- @../../rules/feature-bootstrap.md (nhóm C)
- @../../rules/kg-usage.md
- @../../rules/naming-conventions.md
- @../../rules/design-system.md — màu/chữ lấy từ `design/design-tokens.css` (build tự nhúng; thiếu file thì dùng màu trung tính)
