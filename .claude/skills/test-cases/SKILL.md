---
name: test-cases
description: Dùng khi cần sinh test case chi tiết 1:1 từ checklist test gần nhất. Bắt buộc có checklist trước (chạy `/test-checklist`), khác với checklist là outline 1 dòng/case — đây là spec chi tiết chạy được.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
user-invocable: true
disable-model-invocation: true
argument-hint: "[<feature>]"
---
<!-- Licensed to test.innvie@gmail.com — Order 56EB8MCXD -->

# /test-cases — Detailed Test Case Generator (bám sát checklist 1:1)‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

## Goal‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

Sinh test case chi tiết **bám sát checklist gần nhất**, mỗi checklist item → đúng 1 TC, KHÔNG thêm/bớt scenario. TC có đủ fields chạy được: title, description, steps (Action/Expected/Test Data), priority, auto flag, trace ngược về checklist item qua CHK-ID.

**TC là nguồn cho codegen Playwright (skill riêng, Đợt sau) → sinh script `.spec.ts` → chạy script test.** Nên TC phải đủ giàu để build script chạy được: mỗi step nêu **element bằng nhãn/vai trò nghiệp vụ** (nút "Đăng nhập", field "Email" — codegen tự map `getByRole`/`getByLabel`; BA KHÔNG viết selector CSS), Expected verifiable + **wording exact** (để sinh `expect(...)`), Test-Data **giá trị thật** (để script có input). `Auto=Yes` = codegen build được; `No` = manual.

**Máy sinh theo kênh (`**Target:**`):** `web` → `/playwright-gen` (`docs/{feature}/test/e2e/`) · `api` → `/api-test` + bruno-runner (`docs/{feature}/test/api/bruno-api/`; bảng 3rd-party vẫn `test/api/bruno/`) · `mob` → `/maestro-gen` (`docs/{feature}/test/mobile/maestro/`). Kết quả chạy chuẩn hoá ở `docs/{feature}/test/results/latest.json`. Hợp đồng đầy đủ (mã, kênh, nhãn đáp án, trạng thái kết quả): `.claude/rules/test-trace.md`.

Workflow QC chuẩn:
1) `/test-checklist` → checklist outline → review.
2) `/test-cases` → TC chi tiết từ checklist → review.
3) Máy sinh theo Target đọc TC → script → chạy DEV (feature cũ: chạy từ worktree `feat/<slug>`). Hoặc import TestRail/Jira.

## Constraints‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

### Hard rules — never violate‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

* **Bảng mô tả màn 5 cột — tra theo `.claude/rules/screen-source.md` Mục 2:** flow có `docs/{feature}/screens/{flow}.md` (đã lên Figma) thì đó là nguồn duy nhất, block `## Screen: {slug}` + `### Trạng thái:`; chưa có thì `html-wireframe/` rồi `ascii-wireframe/`.
* **HARD GATE: phải có checklist matching scope.** Không có `docs/{feature}/test/checklist/checklist-{scope-slug}.md` → refuse + gợi ý chạy `/test-checklist` trước.
* **Bám sát checklist 1:1** — mỗi item trong checklist gốc → đúng 1 TC. KHÔNG split (1 item thành 2 TC), KHÔNG gộp (2 item thành 1 TC), KHÔNG thêm TC không có trong checklist. Số TC = số checklist item.
* **Mapping qua CHK-ID (trace key ổn định)** — mỗi TC bám 1 checklist item qua `CHK-{feature}-NNN`. `**Checklist:**` PHẢI bắt đầu bằng `CHK-{feature}-NNN` (+ nội dung item gốc làm anchor). `**Ref:**` **bắt buộc**, kế thừa nguyên list Ref của item (vd `FR-{feature}-003, E-{feature}-003`; bộ tái lập `FR-{feature}-R003`; mã AC dev `AC:FU-FD-AC-002`), else `—`. `STT` chỉ là số hiển thị, KHÔNG phải khóa trace.
* **Validator (gate trước Write)** — kiểm cardinality theo BLOCK (không chỉ set), chỉ tính **TC active** (loại TC `(retired)` khỏi phép đếm): mỗi TC block parse đủ field bắt buộc; mỗi CHK checklist **active** xuất hiện **đúng 1 lần** trong TC active; `count(TC active) = count(checklist item active)`. Báo riêng `missing`/`duplicate`/`extra`/`malformed`. TC anchor `CHK-...-NNN (retired)` (item đã xóa nhưng user giữ) → hợp lệ, WARNING (không block, không tính vào cardinality); TC anchor CHK không tồn tại + không retired → BLOCKING. TC ref `E-NNN` mà Expected KHÔNG chứa wording/mã khớp Error Matrix → WARNING (bắt lỗi sinh-từ-summary).
  * **Grammar `**Checklist:**`** chấp nhận 2 dạng: `CHK-{feature}-NNN — <text>` (active) HOẶC `CHK-{feature}-NNN (retired) — <text>` (item đã xóa, giữ TC). `(retired)` là biến thể hợp lệ của grammar, KHÔNG phải malformed.
  * **Schema 10 field (+3 tuỳ chọn)**: mỗi TC block phải có đúng 1 lần mỗi key, đúng order STT/Category/Sub-Category/Checklist/Ref/Priority/Title/Description/Auto/Preconditions rồi step blocks. 3 field tuỳ chọn `**Target:**` · `**Role:**` · `**Data:**` (mỗi cái tối đa 1 lần) nằm giữa `Auto` và `Preconditions`, đúng thứ tự đó. Thiếu key bắt buộc / trùng / sai order → malformed. `Target` ∈ `web|mob|api` (thiếu → `web`); `Role` phải là khoá có trong `qa/config/roles.json`; `Data` = danh sách tên dữ liệu tiền đề phẩy-phân-tách. **`Preconditions` — validator kiểm đúng 5 dạng:** `—` · các dòng `ROLE: <role-slug>` / `DATA: <data-key>` (khớp field Role/Data) · `<state> (dựng: <steps>; nguồn: <ID>)` · `<state>` (chỉ khi trỏ named-fixture trong test-strategy) · `TBD (cần BA cấp)`. **Reject:** `(dựng: ...)` rỗng / thiếu `nguồn:` / dùng ngưỡng-quy-tắc không có ID nguồn / plain `<state>` không có fixture-source. `Preconditions: TBD` → TC chưa automation-ready.
* **Read prose là nguồn nội dung — coverage/anchor KHÔNG (HARD CONSTRAINT)** — coverage table + CHK anchor chỉ chọn obligation. Expected/message/side-effect/Test-Data CHỈ lấy từ Read prose gốc: resolve Ref → source block (spec Error Matrix, UC extension, screen desc) → Read nguyên prose → sinh nội dung. Không resolve được / prose không có wording → hỏi BA (clarify-first) hoặc `TBD (cần BA cấp)`, KHÔNG suy diễn.
* **STT per-file, bắt đầu 01, renumber liên tục** — mỗi `testcases-{scope}.md` đánh số `01..N` không gap. Update mode renumber toàn file (trace thật là CHK-ID). Width theo tổng block cuối (≥100 → pad-3 toàn file). Chỉ là số hiển thị nội-file.
* **KG chỉ để định tuyến/chọn file** — resolve Ref → source file bằng graph là OK, nhưng Expected/message/Test-Data LUÔN từ prose đã Read (khớp HARD CONSTRAINT trên). 3 nghĩa vụ khi gọi kg-query: `--all` khi output báo cap; Read TẤT CẢ mục "Phải Read tay"; `KG-ERROR` → quay về flow đọc-trực-tiếp cũ. Per @../../rules/kg-usage.md.
* **Format MD parser-compatible** — strict format cho preview parser + codegen. Mỗi TC block phân cách `---`. Field order (10 field): `**STT:**`, `**Category:**`, `**Sub-Category:**`, `**Checklist:**` (= `CHK-{feature}-NNN — <text>`), `**Ref:**` (= `FR/BR/NFR/E-{feature}-NNN[, ...]` else `—`), `**Priority:**`, `**Title:**`, `**Description:**`, `**Auto:**`, [`**Target:**`, `**Role:**`, `**Data:**` — tuỳ chọn], `**Preconditions:**` (state cần trước Step 1, else `—`), rồi N step: `**Step:** N` / `**Action:** ...` / `**Expected:** ...` / `**Test Data:** ...`.
* **Preconditions — 4 giá trị, phân biệt "không cần" / "dựng được" / "chưa biết cách dựng" (HARD)** — field `**Preconditions:**` nêu state nghiệp vụ trước Step 1:
  * `—` = TC **KHÔNG cần** state/setup đặc biệt (anonymous, trạng thái mặc định).
  * `<state> (dựng: <các bước>; nguồn: <ID>)` = **state DỰNG ĐƯỢC bằng cách GHÉP các transition/action ĐÃ CÓ NGUỒN**. Skill CHỈ được ghép từ hành động/transition có thật trong tài liệu, **kèm provenance**. Vd: `account locked (dựng: tạo account → login sai 5 lần; nguồn: BR-{feature}-006 + UC-login)`. **Mọi mắt xích phải có nguồn** — KHÔNG chỉ con số: nếu **action, thứ tự chuyển state, guard, hoặc cơ chế reset** không có nguồn → `TBD`. CẤM suy diễn luồng tạo account / thứ tự / cách reset.
  * `<state>` (không kèm cách dựng) = **CHỈ** khi trỏ tới **fixture được ĐẶT TÊN trong `test-strategy.md`** (fixture đó lo cách dựng). KHÔNG dùng cho "cách đạt hiển nhiên" tự suy.
  * `TBD (cần BA cấp)` = state cần ngưỡng/quy tắc/action/fixture mà **tài liệu chưa nói** → không dựng được. Validator cảnh báo blocking cho codegen, TC not-ready.
  * `ROLE: <role-slug>` / `DATA: <data-key>` (mỗi dòng 1 mục, đi kèm field `Role`/`Data`) = engine **tự lo**: đăng nhập sẵn theo vai (`qa/config/roles.json`) và gọi hook dựng dữ liệu / đọc testdata có tên. Preconditions chỉ gồm các dòng này (hoặc `—`) thì **KHÔNG phải setup-required** — TC run-ready.
  * **Nguồn (thứ tự resolve, KHÔNG bịa):** `states.md` → BR/FR/E prose → UC precondition → screen state → `test-strategy.md` (fixture). Bất kỳ mắt xích dựng-state thiếu nguồn → TBD.
  * ⚠️ **Ví dụ SAI (không tương đương nghiệp vụ):** "session hết hạn" ≠ "xóa session cookie" (xóa cookie = logout, khác expiry). Chỉ dựng khi có `login → chờ quá TTL (nguồn: NFR/BR)` hoặc fixture time-control trong strategy; thiếu TTL → TBD.
  * Case unverified/locked/fail-counter/onboarding để `—` = SAI. Ưu tiên `<state> (dựng: ...; nguồn: ...)` khi MỌI mắt xích có nguồn; else TBD.
* **Phân biệt codegen-ready vs run-ready (tránh FAIL giả khi chạy)** — 2 khái niệm khác nhau:
  * **codegen-ready** = đủ để sinh test BODY (không TBD ở Expected/Test-Data/Precond). TC có `(dựng: ...)` VẪN codegen-ready.
  * **run-ready** = chạy được ngay: Preconditions là `—` hoặc chỉ gồm dòng `ROLE:`/`DATA:`, HOẶC state đã có fixture/setup xác nhận. TC có `(dựng: ...)` = **setup-required** (cần dựng state trước) → **KHÔNG run-ready mặc định**; `/playwright-gen --run` phải **skip/PENDING với lý do "cần dựng state trước"**, KHÔNG chạy rồi FAIL giả bắt BA đoán.
  * TC có **TBD** (Precond/Expected/Test-Data) → không codegen-ready → `not-ready`.
* **Auto=Yes** — TC kế thừa `Auto` 1:1 từ checklist. TC `Auto=Yes` mà **có TBD** → cảnh báo mismatch, báo user (KHÔNG tự sửa Auto — phá 1:1). TC `Auto=Yes` mà **setup-required** (`dựng:`) → hợp lệ để codegen, nhưng đánh dấu để `--run` biết cần dựng state.
* **Bảng "Cần bổ sung" = HÀNG ĐỢI REVIEW tập trung, KHÔNG thay marker TBD trong TC** — MỌI chỗ thiếu (test-data/threshold/wording/state) gom vào **1 bảng `## Cần bổ sung`** trong `{feature}-testcase-index.md` (Final report chỉ là **bản chiếu**, không phải nguồn thứ 2). **Marker `TBD` VẪN nằm trong TC** (Preconditions/Expected/Test-Data) — vì `/playwright-gen` dựa marker đó để skip; bảng chỉ để BA review 1 chỗ. Mỗi dòng có **khóa định vị**: `File/Scope | CHK-ID | Field/Step | Loại | Thiếu gì | Gợi ý cấp`. Cấp xong → mode `supplement` (xem Update mode). (State DỰNG ĐƯỢC-có-nguồn thì skill tự dựng, KHÔNG vào bảng.)
* **Test steps basic** — chỉ action thiết yếu (1-5 steps/TC). 1 step = 1 user action observable. **Action nêu element bằng nhãn/vai trò nghiệp vụ** (nút "Đăng nhập", field "Email" — lấy từ ascii-wireframe bảng 5 cột Items; codegen Đợt sau map getByRole/getByLabel). KHÔNG selector CSS/test-id.
* **Expected result verifiable + wording exact** — pass/fail dứt khoát, trích message/mã exact từ prose (vd "Hiển thị message 'Email hoặc mật khẩu không đúng' (E-{feature}-003)"), state-change/redirect cụ thể — để codegen sinh assertion. KHÔNG "User thấy lỗi".
* **Test Data cụ thể, không bịa** — thứ tự: source-cấp → synthetic-từ-rule-rõ (ghi rule) → BA-cấp → `TBD (cần BA cấp)`. CẤM bịa credentials/endpoint/URL/threshold/mã-lỗi. Placeholder `<valid_input>` không được. Không applicable → `—`.
* **Bí mật chỉ ghi tên biến môi trường** — mật khẩu, tài khoản thật, khoá API, khoá simulator ghi dạng `ENV: QA_<ROLE>_PASS` (tên biến khai ở `qa/.env.example`, giá trị trong `qa/.env` gitignore). TUYỆT ĐỐI không ghi giá trị thật vào TC/testdata.
* **Step chuẩn bị không có oracle** — step chỉ để đi tới chỗ kiểm (mở trang, nhập field) ghi `**Expected:** —`. Mọi step đều phải là 1 hành động máy làm được (mở, nhập, bấm, chọn, gọi API); CẤM step chỉ "Quan sát …" / "Kiểm tra …" không có hành động — gộp phần kiểm vào Expected của step hành động cuối.
* **Language từ test-strategy.md** (durable) — không hỏi lặp. Chưa có strategy → nhìn ngôn ngữ checklist. Đổi ngôn ngữ khác → warn + confirm.
* **L1 plan preview** dạng table TC count per category.
* **L3 iterate** max 3 vòng render TC trong chat trước Write.
* **L2 diff** khi update file đã tồn tại.
* **Slim frontmatter** ở `{feature}-testcase-index.md` (master). Các file `testcases-*.md` **zero frontmatter** (parser-ready).
* **Activity log** — set env note trước mỗi Write/Edit `testcases-*.md`; hook ghi vào `_workspace/changelog.md` (path là routing).
* **GIỮ NGUYÊN button labels / field names** ngôn ngữ gốc (vd "Đăng nhập", "Submit", "Email") trong steps/expected, chỉ Vietnamese hoá narration.
* **Refuse nếu checklist outdated:** so sánh timestamp `checklist-*.md` vs existing `testcases-*.md`. Checklist mới hơn → warn "checklist đã update sau TC, sẽ regen toàn bộ TC" trước proceed.
* **BA conventions** — per @../../rules/ba-conventions.md.

### Pitfalls — easy to get wrong‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

* **Bám sát 1:1 là HARD CONSTRAINT** — nếu QC muốn thêm scenario ngoài checklist → bảo họ chạy `/test-checklist` update checklist trước, rồi quay lại `/test-cases`. Skill KHÔNG tự thêm.
* **Read prose gốc, KHÔNG dùng coverage/anchor làm nguồn (HARD).** Expected/wording/side-effect chỉ từ Read spec Error Matrix / UC / screen — coverage table + CHK anchor chỉ để CHỌN obligation. Sinh Expected từ ô tóm tắt = mất wording exact + side-effect. Validator warn nếu TC ref E-NNN mà Expected thiếu mã/wording khớp.
* **Element theo nhãn nghiệp vụ cho Playwright codegen** — Action nêu nút/field bằng nhãn thật (nút "Đăng nhập", field "Email" từ ascii-wireframe), KHÔNG selector CSS/test-id. Codegen Đợt sau map getByRole/getByLabel. TC là nguồn sinh `.spec.ts` chạy được → Expected verifiable + Test-Data thật là bắt buộc, không chỉ để người đọc.
* **Title/Description KHÔNG máy móc** — Title copy nguyên checklist text + Description template `"Kiểm tra {cat} — {text}"` là anti-pattern (làm TC vô giá trị đọc). Title thêm điều kiện/intent; Description nêu oracle/rủi ro. Không thêm được gì → giữ ngắn, KHÔNG độn template.
* **STT per-file, bắt đầu 01** — `testcases-{scope}.md` đánh STT từ `01`. Update mode: **renumber toàn file `01..N` liên tục sau update** (xóa TC → không để gap; trace thật là CHK-ID nên renumber STT an toàn). Width theo tổng block cuối cùng (≥100 → pad-3 toàn file, KHÔNG mixed width). STT chỉ là số hiển thị nội-file.
* **Body có `|` hoặc `---` trong test data:** vỡ format. Escape bằng `&#124;` hoặc reformulate. Steps Expected/Test Data tránh dùng `---` trong content.
* **Multi-line Expected:** parser support continuation, nhưng giữ 1-2 dòng cho dễ đọc. Long expected → tách thành step phụ.
* **Language mismatch** checklist vi nhưng QC team work en → warn user, đề xuất 2 option: (a) generate vi giống checklist, (b) generate en + ghi note "translated from vi checklist".
* **Header & Footer items** (khi checklist có — tức source đã xác nhận app-wide chrome) → generate TC cho mỗi item, không skip. Nếu checklist KHÔNG có header/footer (feature non-web / chưa xác nhận) thì cũng không có TC — không tự thêm.
* **Auto=No cho case không tự-chạy qua UI được** — không chỉ "verify color". Bao gồm: cần **DB inspection** (vd "fail counter tăng +1" — không quan sát qua UI), **concurrency/race** (2 request song song), **timing/measurement design** (response-time 2 case tương đương — chống timing-attack), visual/contrast cảm tính, system perf metric, webhook chờ async. Case marked Auto=Yes mà step cần các thứ này → WARNING mismatch, báo user sửa `[Yes]/[No]` ở checklist rồi regen (KHÔNG tự sửa ở TC — phá 1:1).
* **Stale check:** mỗi run, in 1 dòng "Checklist updated: {date} / Existing TC updated: {date}". Nếu TC newer than checklist → OK. Checklist newer → warn regen.
* **Test data fabrication risk:** AI có xu hướng bịa data. Ưu tiên lấy từ brainstorm scenario matrix + SRS error matrix + api-summary error catalog. Không có → mark `Test Data: TBD (cần BA cấp)`.

## Inputs

```
/test-cases                       # skill hỏi feature + scope
/test-cases payment               # skill hỏi scope
/test-cases "viết test cases cho login screen"   # natural language OK
```

Skill hỏi tự nhiên:
1) **Feature** — thiếu thì list ra.
2) **Scope** — feature / 1 màn / 1 user story / 1 use case (list target có checklist sẵn).
3) **Language** — lấy từ `test/test-strategy.md` (durable), KHÔNG hỏi lại (no-re-ask). Chưa có strategy → theo ngôn ngữ checklist; vẫn không rõ → hỏi 1 lần rồi lưu vào strategy. Chỉ hỏi lại khi user chủ động muốn TC khác ngôn ngữ checklist (→ warn + confirm).
4) User intent ngầm: "update lại" → update mode; "review" → review mode.

## Output

```
docs/{feature}/test/
  test-strategy.md                   # input: chiến lược test (durable+per-run) — dùng chung /test-checklist
  checklist/                         # input của skill này (có sẵn)
  testcases/                         # ← OUTPUT
    {feature}-testcase-index.md                          # master metadata + bảng TestCases
    testcases-feature.md               # scope=feature (zero frontmatter, parser-ready)
    testcases-screen-{slug}.md         # scope=screen
    testcases-{us-NNN}.md              # scope=story
    testcases-uc-{slug}.md             # scope=uc
    preview.html                       # viewer (copy literal từ template)
    data.js                            # data cho preview.html (regen mỗi lần)
```

## Context (dynamic)

Today: !`date +%Y-%m-%d`
Features có checklist: !`for d in docs/*/test/checklist/; do [ -d "$d" ] && echo "$d" | sed 's|docs/||;s|/test/checklist/||'; done | head -10`

## Approach

0) **Resolve mode (TRƯỚC mọi thứ).** "review test cases coverage" → **review mode** (analysis-only, branch xuống Review mode + **return, KHÔNG generate/Write**). "update lại/regen" + file tồn tại → update mode. Còn lại → create mode.
1) **Hỏi feature.** Thiếu → list features có folder `test/checklist/`.
2) **Hỏi scope.** List checklist files có sẵn trong `test/checklist/` để user chọn.
3) **Hard gate checklist exists.** Refuse nếu không tìm thấy `checklist-{scope-slug}.md` matching.
4) **Đọc checklist gốc** + parse grammar `[P] [Auto] CHK-{feature}-NNN → {ref} · text [@web|@mob|@api] [[đáp án: …]]` per item (Ref → mảng khi nhiều ID, gồm cả `AC:{mã dev}`; tách đuôi kênh + nhãn đáp án khỏi text), gom category/subcategory headers (`#1. ...` / `##1.1. ...`). **Legacy gate**: checklist còn item không có CHK-ID → hard-gate "checklist chưa ổn định trace, chạy lại `/test-checklist` update trước" — KHÔNG cho legacy vào TC/Coverage/KG như trace hợp lệ.
5) **Ngôn ngữ từ `test/test-strategy.md`** (durable) — không hỏi lặp. Chưa có strategy → theo ngôn ngữ checklist. Đổi ngôn ngữ khác → warn + confirm.
6) **Hỏi update vs replace** nếu `testcases-{scope-slug}.md` đã tồn tại. So sánh timestamp với checklist gốc → in cảnh báo stale nếu checklist mới hơn.
7) **Gom context bổ sung** từ feature folder cho TC enrichment (test data lấy từ đâu?):
   * `srs/{feature}-spec.md` → error messages exact, validation rules, business rules
   * `ascii-wireframe/{feature}-wireframe-index.md` + screen content (gộp theo flow trong `{flow-slug}.md`) → field names, button labels, screen states
   * `brainstorms/*.md` → scenario matrix, interrupted-tx (lấy test data thực tế)
   * `integration/api-summary.md` → error catalog API (test data cho integration TC)
   * `usecases/uc-*.md` → expected results từ "Expected result" section
   * Feature cũ chưa có SRS mới → `docs/_reverse/{feature}/{feature}-reverse-spec.md` + `reverse-gaps.md` thay cho `srs/{feature}-spec.md` (Ref mã R); US/AC sinh từ bộ tái lập đọc như US/AC thường. Ref `AC:{mã dev}` → đọc đúng câu AC đó như bộ tái lập/`reverse-sources.md` trích. Thứ tự ưu tiên khi các nguồn lệch nhau: `.claude/rules/test-trace.md`.
   * `qa/config/roles.json` → khoá vai hợp lệ cho field `Role`.
8) **Generate TC 1:1 từ checklist items** — với MỖI item, TRƯỚC khi viết Expected/Test-Data:
   1) CHK-ID → chọn obligation.
   * **KG định tuyến nguồn Ref.** Với mỗi CHK, chạy `node .claude/skills/kg/engine/kg-query.mjs explore CHK-{feature}-NNN` và khi cần `node .claude/skills/kg/engine/kg-query.mjs trace {feature} --all` để tìm nhanh file nguồn của từng Ref trước khi Read nguyên văn. Nếu output báo `⚠ còn N mục — chạy với --all` thì chạy lại query với `--all`; Read toàn bộ mục `### Phải Read tay (ngoài graph)`; `KG-ERROR` hoặc lỗi bất kỳ → quay về flow resolve Ref/đọc-trực-tiếp cũ. **Read prose là nguồn nội dung** vẫn là hard constraint.
   2) Resolve Ref → source block gốc. Ref có ID → FR/BR/E trong `spec.md` (hoặc `reverse-spec.md` khi mã R), UC extension; `AC:{mã}` → câu AC dev được bộ tái lập trích. **Ref `—`** (item a11y/visual/chrome không map requirement) → fallback resolve theo: screen block trong scope → `test-strategy.md` (env/data) → nếu vẫn không có source → `TBD/OQ`, KHÔNG bịa.
   3) **Read NGUYÊN prose source đó** (KHÔNG dùng ô tóm tắt coverage/anchor làm nguồn).‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍
   4) Sinh Expected/Test-Data từ prose (wording exact + mã E + side-effect).
   5) Không resolve được / prose không có wording → hỏi BA (clarify-first) hoặc `TBD (cần BA cấp)`, KHÔNG suy diễn.
   * Field `STT` sequential: 01, 02, ... (số hiển thị, độc lập CHK-ID).
   * Field `Category` / `Sub-Category` ↔ của item trong checklist. Item không nằm dưới subcategory (chỉ có `#N.` category) → `Sub-Category: —`.
   * Field `Checklist` = `CHK-{feature}-NNN — <nội dung item gốc>`.
   * Field `Ref` = nguyên list Ref của item (kế thừa); item ref `—` → TC ref `—`.
   * Field `Priority` / `Auto` ↔ `[P]` / `[Auto]` của item.
   * Field `Target` (tuỳ chọn) ↔ kênh `@web/@mob/@api` của item (`@web` hoặc thiếu → có thể bỏ field). Nhãn `[đáp án: …]` của item chép vào cuối `Description` (vd "… (đáp án: code FU-FD-AC-002)") để biết test rớt thì FAIL_APP hay FAIL_DOC.
   * Field `Role` (tuỳ chọn) — vai đăng nhập sẵn, khoá trong `qa/config/roles.json` (vd `requester-mobile`, `approver`). Bỏ khi TC tự test đăng nhập hoặc chạy ẩn danh.
   * Field `Data` (tuỳ chọn) — tên dữ liệu tiền đề engine dựng/đọc (vd `vehicle-with-quota`). Chỉ dùng tên đã khai trong testdata/hook của feature hoặc `test-strategy.md`; chưa có → `TBD (cần BA cấp)` ở Preconditions + dòng bảng Cần bổ sung.
   * Field `Title` — verb-object nêu **ý định test** (test cái gì, điều kiện nào). Item có ngữ cảnh nghiệp vụ (validation/error/BR) → thêm điều kiện làm rõ intent, KHÔNG chép nguyên checklist. Vd "Verify sai password → message generic" → Title "Đăng nhập sai mật khẩu **account tồn tại** trả lỗi generic" (thêm "account tồn tại"). **Ngoại lệ trivial**: item hiển-thị/navigation đơn giản (logo, link) không có điều kiện thêm → Title ngắn trùng ý checklist là CHẤP NHẬN (đừng bịa intent giả).
   * Field `Description` — **luôn PHẢI có** (schema 10 field, field bắt buộc). 1-2 câu nêu **mục đích + oracle/rủi ro**, KHÔNG dùng template rập khuôn `"Kiểm tra {category} — {checklist text}"`. Case có rủi ro → nói rõ (vd "anti-enumeration: sai-pwd và email-không-tồn-tại trả CÙNG wording, không leak"). Case trivial → 1 câu ngắn đúng oracle (KHÔNG bỏ trống, KHÔNG độn template).
   * Field `Preconditions` — state/account/env cần trước Step 1 (từ states.md/BR/UC precondition), else `—`. Bắt buộc khi TC test locked/unverified/onboarding/expired.
   * Field `Steps` — 1-5 steps, mỗi step Action/Expected/Test Data:
     * **Action**: nêu element bằng **nhãn/vai trò nghiệp vụ** (nút "Đăng nhập", field "Email" — từ ascii-wireframe bảng 5 cột). KHÔNG selector CSS.
     * **Expected**: verifiable, wording/mã exact từ prose (message "Email hoặc mật khẩu không đúng", state-change, redirect).
     * **Expected** của step chuẩn bị (không phải oracle) = `—`.
     * **Test Data**: value thật (email "abc@def") hoặc `ENV: <TÊN_BIẾN>` cho mật khẩu/bí mật, hoặc `TBD (cần BA cấp)` / `—`. KHÔNG bịa.
9) **L3 iterate** render 5-10 TC đầu tiên trong chat:
   ```
   [/test-cases] Phiên bản 1 (preview 5/{total} TC đầu):
   (⚠️ URL/giá trị/threshold trong ví dụ dưới là minh họa cấu trúc — TC thật chỉ điền value đã có source, else TBD)

   ---
   **STT:** 01
   **Category:** Header & Footer
   **Sub-Category:** Logo & Navigation
   **Checklist:** CHK-{feature}-001 — Verify logo hiển thị đúng tại header
   **Ref:** —
   **Priority:** 1
   **Title:** Verify logo hiển thị tại header
   **Description:** Kiểm tra logo công ty hiển thị đúng vị trí header.
   **Auto:** Yes
   **Preconditions:** —

   **Step:** 1
   **Action:** Truy cập trang có header (theo screen source)
   **Expected:** Logo công ty hiển thị tại góc trên-trái header
   **Test Data:** —
   ---
   **STT:** 02
   **Category:** Header & Footer
   **Sub-Category:** Logo & Navigation
   **Checklist:** CHK-{feature}-002 — Verify click logo redirect về Home
   **Ref:** —
   **Priority:** 2
   **Title:** Verify click logo redirect về Home
   **Description:** Click logo chuyển hướng về Home.
   **Auto:** Yes
   **Preconditions:** —

   **Step:** 1
   **Action:** Click vào logo ở header
   **Expected:** Browser redirect về Home (URL "/" theo screen source)
   **Test Data:** —
   ---
   **STT:** 03
   ...

   (Lưu ý ATOMIC: 2 CHK riêng "hiển thị" + "click redirect" → 2 TC riêng, mỗi TC 1 oracle. KHÔNG gộp thành 1 TC 2 Expected.)
   (Lưu ý Title: 2 TC trên là case TRIVIAL (hiển thị/navigation đơn giản) → Title ngắn trùng ý checklist OK. Case có ngữ cảnh nghiệp vụ (validation/error/BR) thì Title PHẢI thêm điều kiện/intent — xem field Title bước 8.)

   Đồng ý / Sửa: <feedback> / Hủy:
   ```
   * User `Sửa: TC-03 thêm step verify rate-limit lock` → regen v2. **Chạy lại validator sau mỗi vòng.**
   * Max 3 vòng.
9bis. **Validator (gate trước L1/Write) — bắt buộc create + update mode.** Chạy cardinality + schema 10 field + retired + E-wording (xem Constraints "Validator"). Có BLOCKING → fix trước, KHÔNG L1/Write.
10) **L1 plan preview** dạng table:
    ```
    Em sẽ tạo file `docs/{feature}/test/testcases/testcases-{scope-slug}.md`

    Source: checklist-{scope-slug}.md (updated {date}) — {N} items
    Language: {vi | en | other}

    | # | Category                  | TC count | Steps | P1 | P2 | P3 | P4 | Auto |
    |---|---------------------------|----------|-------|----|----|----|----|------|
    | 1 | Header & Footer           |   4      |  8    |  1 |  2 |  1 |  0 | 4/0  |
    | 2 | Truy cập màn Login        |   6      | 18    |  3 |  2 |  1 |  0 | 5/1  |
    | 3 | Nhập credentials          |   8      | 22    |  4 |  3 |  1 |  0 | 7/1  |
    | ... | ...                     | ...      | ...   |... |... |... |... | ...  |
    |   | **Total**                 | **60**   |**165**| 22 | 20 | 13 |  5 |46/14 |

    Apply? (Y / sửa)
    ```
11) **Write/update `{feature}-testcase-index.md`** master. (Trước Write: set env `CLAUDE_CHANGELOG_NOTE=generated {N} TC ({M} steps) from checklist-{scope-slug}` cho hook — KHÔNG viết vào file.) Nội dung file:
    ```yaml
    ---
    type: test-cases-index
    feature: {feature}
    status: draft
    updated: {date}
    links:
      - docs/{feature}/test/checklist/checklist-{scope-slug}.md
      - docs/{feature}/srs/{feature}-spec.md
    ---

    # Test Cases — {feature}

    ## TestCases

    | Scope | Target | File | TC | Steps | P1 | P2 | P3 | P4 | Auto | Source checklist | Status | Updated |
    |-------|--------|------|----|-------|----|----|----|----|------|------------------|--------|---------|
    | feature | — | [testcases-feature.md](testcases-feature.md) | 60 | 165 | 22 | 20 | 13 | 5 | 46/14 | [checklist-feature.md](../checklist/checklist-feature.md) | draft | {date} |

    ## Cần bổ sung (Not-ready)

    > Hàng đợi review tập trung (BA đọc 1 chỗ) — **KHÔNG thay marker TBD trong TC** (marker vẫn ở TC để playwright skip). Cấp xong → `/test-cases` mode `supplement`: cập nhật NGUỒN bền trước (threshold/wording→BR/SRS; test-data→test-strategy), rồi regen TỪ nguồn. Loại: `test-data` · `threshold` · `wording` · `state`.

    | File/Scope | CHK-ID | Field/Step | Loại | Thiếu gì | Cấp vào đâu |
    |------------|--------|-----------|------|----------|-------------|
    | testcases-screen-login.md | CHK-{feature}-030 | Preconditions | threshold | ngưỡng khóa account (mấy lần?) | BR-{feature}-006 (cập nhật SRS rồi regen) |
    | testcases-screen-login.md | CHK-{feature}-045 · Step 2 | test-data | email/mật khẩu case reset | test-strategy.md (tài khoản test) |

    (Bảng rỗng nếu mọi TC ready → bỏ section.)
    ```
12) **Write `testcases-{scope-slug}.md`** — **zero frontmatter**, body parser-ready format (TC blocks phân cách bằng `---`, mỗi block có 10 metadata fields — STT/Category/Sub-Category/Checklist/Ref/Priority/Title/Description/Auto/Preconditions — + N step blocks). KHÔNG có heading H1 dẫn nhập.
13) **Activity.log (hook tự ghi)** — set env `CLAUDE_SKILL_NAME=/test-cases` + `CLAUDE_CHANGELOG_AUTHOR={@author}` + `CLAUDE_CHANGELOG_NOTE=generated {N} TC ({M} steps)` (≤80 ký tự; update mode: `[{scope-slug}] updated {N} TC, regen từ checklist`) trước Write; hook ghép cả dòng.
14) **Generate `preview.html` + `data.js`** — xem section "Preview HTML" dưới.
15) **Final report:**
    ```
    ✅ Test cases created
       Master:    docs/{feature}/test/testcases/{feature}-testcase-index.md
       Content:   docs/{feature}/test/testcases/testcases-{scope-slug}.md
       Preview:   docs/{feature}/test/testcases/preview.html  (double-click mở browser)
       Data:      docs/{feature}/test/testcases/data.js
       {N} TC / {M} total steps
       Priority: P1={a} P2={b} P3={c} P4={d}
       Auto: Yes={x} No={y}
       Source: checklist-{scope-slug}.md ({date})

    ⚠️ CẦN BỔ SUNG — {t} TC chưa ready (gom 1 chỗ, xem bảng "## Cần bổ sung" trong index):
       | TC | Loại | Thiếu gì |
       |----|------|----------|
       | 12 | threshold | ngưỡng khóa account (BR chưa nêu số) |
       | 18 | test-data | tài khoản test cho case reset |
       → Cấp dữ liệu / xác nhận yêu cầu rồi chạy lại `/test-cases {feature}` — skill regen đúng phần chưa ready, giữ TC đã xong.
       (Nếu {t}=0: bỏ dòng này.)

    Recommended next:
      - Mở preview.html → click "Export Excel (merged)" → import vào TestRail/Jira
      - /playwright-gen {feature}   — codegen script web cho các TC đã ready (Auto=Yes, không TBD, Target web)
      - /api-test {feature} + bruno-runner — TC Target api
      - /maestro-gen {feature}      — TC Target mob
    ```

## TC block format (parser-ready, strict)

Mỗi TC là 1 block phân cách bằng `---` (3 dấu trừ, dòng riêng). Trong block:

> ⚠️ Giá trị trong ví dụ dưới (`abc@def`, `< 2 giây`, URL...) là **minh họa cấu trúc**, KHÔNG phải data thật. Khi sinh TC thật: mọi value/threshold/URL/message phải rút từ prose source (spec/screen), else `TBD (cần BA cấp)` — theo hard-constraint "không bịa".

```
---
**STT:** 01
**Category:** Truy cập màn Login
**Sub-Category:** Hiển thị form
**Checklist:** CHK-{feature}-010 — Verify đăng nhập đúng email + mật khẩu chuyển sang Dashboard
**Ref:** FR-{feature}-001
**Priority:** 1
**Title:** Đăng nhập bằng tài khoản hợp lệ chuyển sang Dashboard
**Description:** Luồng chính: tài khoản đang hoạt động đăng nhập thành công và vào màn Dashboard.
**Auto:** Yes
**Target:** web
**Preconditions:** —

**Step:** 1
**Action:** Mở trang Login (step chuẩn bị — KHÔNG assert perf ở đây)
**Expected:** —
**Test Data:** URL: /login

**Step:** 2
**Action:** Nhập field "Email"
**Expected:** —
**Test Data:** ENV: QA_WEB_VIEWER_USER

**Step:** 3
**Action:** Nhập field "Mật khẩu"
**Expected:** —
**Test Data:** ENV: QA_WEB_VIEWER_PASS

**Step:** 4
**Action:** Bấm nút "Đăng nhập"
**Expected:** Chuyển sang màn Dashboard (URL "/dashboard" theo screen source)
**Test Data:** —
---
```

> **1 TC = 1 oracle-cuối.** Ví dụ trên: oracle là "vào Dashboard" (Step 4). Step 1–3 là step chuẩn bị nên Expected `—` (KHÔNG assert "render <2 giây" — đó là oracle perf riêng, thuộc CHK/TC khác nếu có threshold). Mật khẩu chỉ ghi tên biến `ENV: …`, không ghi giá trị. TC kiểm hiển thị (vd "form đủ 3 field") thì gắn Expected đó vào step hành động mở trang, KHÔNG thêm step "Quan sát form".

> **TC dùng vai + dữ liệu có tên (engine tự dựng):**
> ```
> **Auto:** Yes
> **Target:** api
> **Role:** requester-mobile
> **Data:** vehicle-with-quota
> **Preconditions:** ROLE: requester-mobile
> DATA: vehicle-with-quota
> ```
> Preconditions chỉ gồm `ROLE:`/`DATA:` → run-ready, không phải setup-required.

> **Field order chuẩn (10 field + 3 tuỳ chọn)**: STT · Category · Sub-Category · Checklist (= `CHK-{feature}-NNN — <text>`) · **Ref** (= `FR/BR/NFR/E-{feature}-[R]NNN` / `AC:{mã dev}`[, ...] hoặc `—`) · Priority · Title · Description · Auto · [Target · Role · Data] · **Preconditions** (state trước Step 1, else `—`) · rồi N step block. `Ref` bắt buộc (kế thừa item); `Preconditions` bắt buộc khi TC cần state/account cụ thể.

**Strict rules cho parser:**
* Mỗi field key `**Key:**` đứng đầu dòng riêng.
* Multi-line values cho Expected / Test Data: dòng tiếp theo (trước field kế tiếp) coi là continuation.
* `Step` field đánh dấu bắt đầu step block mới.
* Block separator: dòng `---` riêng giữa 2 TC.
* TC đầu file cũng bắt đầu bằng `---`.
* KHÔNG có heading markdown trong block (vd `#`, `##`).

## Preview HTML (`preview.html` + `data.js`)

Pattern giống `/test-checklist`:
* Template: `_templates/test-cases-preview.html` — **self-contained (KHÔNG CDN cho CSS/layout)**, **2 chế độ xem chuyển ngay trên trang** (nút ▤ Card / ▦ Bảng ở toolbar, nhớ lựa chọn qua `localStorage`): **Card** (1 TC/thẻ, bảng steps bên trong — dễ đọc/comment) và **Bảng** (rowspan các field TC-level, mỗi step 1 dòng — nhìn tổng thể nhanh). Light/dark theme, filter/search/pagination, Export Excel (flat + merged, SheetJS nạp lazy chỉ khi bấm). Render đủ field gồm **Preconditions** + badge **retired**; `ref` là **mảng** (dùng `fmtRef` join, backward-compat string).
* **Comment trên từng case:** mỗi card/hàng có nút 💬 mở ô ghi chú; comment lưu `localStorage` (key `tc-comments::{feature}`, KHÔNG đụng file MD), **neo theo CHK-ID** (khóa bền, KHÔNG theo `stt`). Nút **📋 Copy toàn bộ comment** sinh **block feedback tự-hành**: preamble hướng dẫn AI + header `FEEDBACK-PREVIEW · testcase · feature=… · updated=…` + N dòng `- [CHK-ID · TC{stt} | ref=… | file=…] "trích" → comment`. User dán vào chat → AI vào **Feedback intake mode** (xem section riêng). Filter "Comment: chỉ có / chưa" + nút "Xoá hết".
* `preview.html` copy literal lần đầu (skip nếu có). **Nếu `preview.html` đã tồn tại nhưng là bản CŨ** (bảng phẳng 14 cột / nạp Bootstrap CDN / không có nút 💬) → đề xuất user xóa `preview.html` để copy lại bản hiện hành (kiểm nhanh: bản cũ có chuỗi `cdn.jsdelivr.net/npm/bootstrap` trong `<head>`; bản mới không, và có `id="copyComments"`).
* `data.js` regen mỗi lần — chứa (mỗi TC có `preconditions` + `retired` + `ref` mảng):
  ```js
  window.FEATURE = "payment";
  window.UPDATED = "2026-05-28";
  window.LANG    = "vi";
  window.TESTCASES_DATA = [
    { scope: "feature", target: "", file: "testcases-feature.md",
      testcases: [
        { stt: "01", category: "Header & Footer", subcategory: "Logo & Navigation",
          checklist: "CHK-payment-001", ref: ["FR-payment-012"], priority: 1, auto: "Yes", target: "web", role: "", data: [], preconditions: "—", retired: false,  // ref mảng; retired:true → loại khỏi active count/export, hiện ở filter riêng
          title: "Verify logo render và clickable",
          description: "...",
          steps: [
            { step: "1", action: "Mở /dashboard", expected: "—", testData: "URL: /dashboard" },
            { step: "2", action: "Bấm logo", expected: "Redirect về /", testData: "—" }
          ]
        },
        ...
      ]
    },
    ...
  ];
  ```

**Excel export 2 mode** (template đã có sẵn):
* **Flat:** 1 row / step. Dễ filter trong Excel.
* **Merged:** TC-level fields merged across step rows. Đẹp cho report.

**ID prefix toggle** trong preview (default `TC`): user gõ "TC-AUTH-" → render `TC-AUTH-01`. Bỏ tick prefix → STT thô. Hữu ích khi copy sang Jira/TestRail.

> ⚠️ **STT restart 01 mỗi file** → chế độ "Mọi file" / Export Excel merged: `TC-01` TRÙNG giữa `testcases-feature.md` và `testcases-screen-login.md`. Preview/export **ghép scope vào ID** khi gom nhiều file (vd `TC-feature-01`, `TC-screen-login-01`) để không đụng khi import. File vượt 99 TC → TC mới dùng 3-digit (`100`), KHÔNG renumber TC cũ (STT chỉ hiển thị, trace qua CHK-ID).

## Update mode — 3 mode RÕ RÀNG (chọn đúng theo tình huống, KHÔNG lẫn)

Xác định mode TRƯỚC khi sửa (mọi mode: validator cardinality/schema chạy trên **TOÀN BỘ file sau merge**, không chỉ phần vừa đụng):

* **`supplement`** (BA vừa cấp thứ thiếu trong bảng `## Cần bổ sung`, rồi chạy lại) → **CHỈ patch TC `not-ready`** (có TBD): điền giá trị BA cấp, gỡ khỏi bảng. Giữ nguyên TC ready + enrichment. (Điều kiện: nguồn bền đã cập nhật — xem dưới.)
* **`sync`** (checklist đổi — mặc định khi "update lại / checklist mới hơn") → xử lý new/changed/deleted item: item mới→gen TC; item đổi contract kế thừa (Ref/Priority/Auto/Category/text)→cập nhật đồng bộ field đó (giữ enrichment); item xóa→L2 hỏi xóa/giữ (giữ→anchor `(retired)`). Renumber STT.
* **`replace`** (CHỈ khi user yêu cầu rõ "làm lại từ đầu") → regen toàn bộ.

L2 diff per TC. Sau update: validator + cập nhật bảng `## Cần bổ sung` (còn/hết).

> **`supplement` — cập nhật NGUỒN trước, không nhét thẳng vào TC (giữ provenance):** BA cấp `threshold`/business-rule/`wording` → **cập nhật BR/SRS/Error Matrix trước qua approval gate**, rồi TC regen TỪ nguồn (không để TC thành nguồn-yêu-cầu-mới mất trace). `test-data`/account → lưu reference ở `test-strategy.md` (không secret). `fixture`/state → `test-strategy.md`. **Chỉ gỡ dòng khỏi `## Cần bổ sung` sau khi nguồn bền đã tồn tại + Read lại.**

## Review mode (khi user nói "review test cases coverage")

Analysis-only. Đọc `testcases-*.md` + `checklist-*.md` + prose source → findings (KHÔNG chỉ đếm):
* **BLOCKING** (bịa hoặc mất marker — CẤM tuyệt đối) — TC missing cho checklist item (orphan); tập CHK ≠ (cardinality); **TC duplicate (2+ TC cùng CHK active)**; **Test Data placeholder `<...>` / bịa (URL/threshold/mã-lỗi không source)**; **Preconditions `—` cho case rõ ràng cần state** (locked/unverified/expired/fail-counter) — vì để `—` = che mất việc cần setup.
* **not-ready (HIGH, KHÔNG block generate)** — `Auto=Yes` mà có `TBD` (Precond/Expected/Test-Data): TC hợp lệ nhưng chưa hoàn tất, vào bảng `## Cần bổ sung`. Đây là trạng thái bình thường của workflow (chờ BA cấp), KHÔNG phải lỗi cấm-generate. (BLOCKING chỉ áp cho `/playwright-gen` codegen/run TC này — nó skip.)
* **WARNING** — TC ref `E-NNN` mà Expected KHÔNG chứa wording/mã khớp Error Matrix (heuristic, có thể false-positive); steps ngoài 1-5; Expected không verifiable ("User thấy lỗi"); **Title copy nguyên checklist (case non-trivial) / Description template rập khuôn**; Auto=Yes cho case cần DB-inspection/concurrency/measurement.
* **SUGGESTION** — nếu 2 CHK thực sự cùng 1 atomic oracle → đề xuất gộp/retire tại `/test-checklist` rồi regen TC (`/test-cases` KHÔNG tự merge — phá anchor CHK + trái 1:1); thiếu negative/boundary scenario (báo về `/test-checklist`, không tự thêm).

Format @../../rules/review-format.md.

## Feedback intake mode (user dán block "FEEDBACK-PREVIEW" từ preview)

Kích hoạt khi user **dán 1 block bắt đầu bằng `### FEEDBACK-PREVIEW · testcase · feature=…`** (sinh bởi nút "📋 Copy toàn bộ comment" trong `preview.html`). Block gồm: preamble hướng dẫn + header định danh (feature/file/updated) + N dòng `- [CHK-ID · TC{stt} | ref=… | file=…] "trích" → comment`. **Đây KHÔNG phải yêu cầu sinh mới — là feedback để cập nhật TC đã có.**

**Nguyên tắc BẮT BUỘC (report-first, HARD STOP — như `/cr`, KHÔNG auto-apply):**

1) **Anchor theo CHK-ID, KHÔNG theo `TC{stt}`.** `stt` renumber mỗi regen → khóa bền là CHK-ID (phần đầu mỗi dòng). Resolve mỗi dòng về CHK-ID trong file `.md` thật. Dòng chỉ có `TC{stt}` không có CHK → KHÔNG tự đoán, đưa vào nhóm (F).
2) **Stale guard.** So `updated=` trong header block với `updated` file trên disk + tập CHK-ID hiện tại. Lệch (CHK không còn / file đã regen) → dòng đó vào nhóm (F) "bỏ qua", nêu lý do, KHÔNG map sang case gần giống.
3) **Đối chiếu nghiệp vụ TRƯỚC khi đụng Expected/hành vi.** Mỗi dòng có `ref=FR/BR/NFR/E` → Read prose requirement đó trong `srs/{feature}-spec.md`. Comment mâu thuẫn prose đã chốt → nhóm (C), KHÔNG sửa.
4) **Phân 6 nhóm rồi IN BẢNG REPORT, DỪNG chờ user duyệt:**
   * **(A) Apply thẳng** — sửa nội dung 1 case (Expected/Test Data/Preconditions/Title/Description/priority/auto), KHÔNG đổi số case, KHÔNG đụng nghiệp vụ. → Edit `testcases-{scope}.md` qua L2 diff (nội dung mới rút từ prose spec, chống bịa). **KHÔNG renumber STT** khi chỉ sửa nội dung.
   * **(B) Route checklist** — thêm/xóa/tách/gộp case, hoặc đổi `Ref`/priority/auto ở tầng scenario. → **KHÔNG sửa thẳng testcase** (phá 1:1). Route `/test-checklist` (cấp CHK-ID mới từ `next_chk_id` / retire vào `## Retired CHK-IDs`) → rồi `/test-cases` mode `sync`.
   * **(C) CHẶN — lệch nghiệp vụ** — mâu thuẫn FR/BR/NFR/Error Matrix. → Trích ID + điều khoản, route `/cr`. KHÔNG sửa.
   * **(D) Route skill khác** — đòi sửa SRS/wireframe/flow, hoặc thêm scenario chưa có CHK. → Nêu skill đích (`/cr`, `/wireframe-ascii`, `/test-checklist`…), KHÔNG tự làm.
   * **(E) Cần làm rõ** — comment mơ hồ ("chưa ổn", "sửa lại"). → Hỏi lại 1 lượt, KHÔNG đoán. Không trả lời → giữ nguyên case, đánh dấu "chưa xử lý".
   * **(F) Bỏ qua** — CHK không tồn tại / retired / stale / sai scope. → Nêu lý do.
5) **Phát hiện xung đột giữa các comment** trong batch (2 comment cùng CHK / loại trừ nhau, vd "gộp CHK-072+073" vs "sửa Expected CHK-073") → mục "Xung đột", user chọn, KHÔNG apply cả 2.
6) **Apply chỉ nhóm (A)** sau khi user duyệt (L1 plan → L2 diff per-case). "Y all" chỉ áp cho (A); (B)(C)(D) luôn cần bước route riêng. Sau apply: chạy **validator** (cardinality 1:1 + schema 10 field + E-wording) trên toàn file → BLOCKING thì **rollback atomic** (không ghi nửa vời) → regen `data.js` + `testcase-index.md`.
7) **Không im lặng nuốt comment nào** — mọi dòng phải hiện trong report ở đúng 1 nhóm. Xong 1 batch → gợi ý user bấm "🗑 Xoá hết" trên preview (tránh dán lại chồng, apply 2 lần).

> **Provenance (feedback cấp giá trị nghiệp vụ):** comment cung cấp threshold/wording/rule (không chỉ test-data) → theo mode `supplement`: cập nhật NGUỒN bền (BR/SRS/Error Matrix) TRƯỚC (qua `/cr`), rồi regen TC từ nguồn — KHÔNG nhét thẳng vào TC (giữ trace, tránh test thành nguồn rule).

## References

- `.claude/rules/screen-source.md` — bảng 5 cột sau Figma (`screens/`), thứ tự nguồn.
* @../../rules/feature-bootstrap.md
* @../../rules/kg-usage.md
* @../../rules/ba-conventions.md
* @../../rules/approval-gate.md
* @../../rules/naming-conventions.md
* @../../rules/delivery-readiness.md
* @../../rules/changelog.md
* @../../rules/review-format.md
* @../../../_templates/test-cases-preview.html‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍


<!-- wm:60d5580055f5e6dd44329f2c02b7fe5a -->
<sub>Tài liệu thuộc bộ AI4BA BA-Kit — bản quyền hoangphan.blog</sub>
