---
name: maestro-gen
description: Dùng khi cần sinh flow Maestro (`.yaml`) cho app mobile từ test case có `**Target:** mob`, rồi chạy trên iOS simulator. `/maestro-gen <feature>` hoặc `/maestro-gen <feature> --run`. Khác `/playwright-gen` (web) và `/api-test` (Bruno, API) — đây là tầng app Flutter.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, AskUserQuestion
user-invocable: true
disable-model-invocation: true
argument-hint: "[<feature>] [--run] [--tc CHK-...]"
---

# /maestro-gen — Codegen Maestro từ Test Case (TC .md → flow .yaml → `maestro test`)

## Goal

Biến test case app (`**Target:** mob`, đã duyệt ở `/test-cases`) thành **flow Maestro chạy được**. Codegen một lần ra artifact bền; AI KHÔNG viết flow tay, chỉ gọi engine `.claude/scripts/maestro-gen.mjs`.

## Hard gate

Thiếu `docs/{feature}/test/testcases/testcases-*.md` → từ chối, bảo chạy `/test-cases {feature}` trước. Không có TC nào `Target: mob` → báo "0 flow", không bịa.

## Inputs

- `docs/{feature}/test/testcases/testcases-{scope}.md` — field `**Target:** mob`, tuỳ chọn `**Role:**` (khoá trong `qa/config/roles.json`) và `**Data:**`.
- Subflow dùng chung `qa/mobile/subflows/`: `login-as-role.yaml`, `logout.yaml`, `igas-simulate-pump.yaml`, `open-fuel-dispensing-list.yaml`.
- Biến môi trường (`qa/.env`, không commit): `APP_ID`, `QA_<ROLE>_USER`, `QA_<ROLE>_PASS`, `QA_PHOTO_PATH` (nếu có bước ảnh).

## Output

- `docs/{feature}/test/mobile/maestro/flows/{scope}/{chk-lower}.yaml` · `config.yaml`
- `docs/{feature}/test/mobile/{feature}-mobile-index.md` (Scope | File | Tests | Kết quả; CHK-ID | Flow | Codegen | Kết quả; Skipped CHK-ID | Lý do)
- Khi chạy: `docs/{feature}/test/results/latest.json` (mảng `{chk, target, status, env, build, at, note}`) và `results/maestro-*.xml` (JUnit).

## Ngữ pháp bước (không dấu cũng hiểu)

| Viết trong TC | Ra flow |
|---|---|
| Mở app | `launchApp` (+ permissions; "xoá dữ liệu" → `clearState`) |
| Đăng nhập vai X | `runFlow` login-as-role, env `ROLE` |
| Bấm/Chọn "X" | `tapOn: "X"` (nhãn dạng id `a.b-c` → `id:`) |
| Nhập "V" vào "X" | `tapOn` + `inputText` (`ENV: VAR` → `${VAR}`; mật khẩu viết trần → SKIP) |
| Vuốt lên / xuống | `scroll` / `swipe DOWN` |
| Chờ "X" hiện | `extendedWaitUntil` (30000; 25000 cho trạng thái iGAS/SignalR) |
| Giả lập bơm | `runFlow` igas-simulate-pump (bấm nút trong app) |
| Chụp/đính kèm ảnh | `addMedia` + ghi chú chọn ảnh trong thư viện |
| Expected Hiện / Không hiện "X" | `assertVisible` / `assertNotVisible` |

Bước lạ hoặc Expected không map được thành assert nào → TC bị **skip kèm lý do** (không bịa). Expected phụ không map được chỉ thành comment `# [chưa tự kiểm]` — đó là phần mức nghiệp vụ người phải soi.

## Approach

1. **Hard gate** như trên; resolve feature (không có → picker).
2. **Dry-run lấy số cho L1:** `node .claude/scripts/maestro-gen.mjs gen --dir docs/{feature}/test --dry-run`.
3. **L1 plan preview** (approval-gate): bảng path | action | summary (flows, config, index), số flow + skip. Engine KHÔNG ghi trước khi user Y.
4. Y → `node .claude/scripts/maestro-gen.mjs gen --dir docs/{feature}/test`. Flow là dẫn xuất nên ghi đè qua L1 tổng, không L2 từng file.
5. `--run` → `node .claude/scripts/maestro-gen.mjs run --dir docs/{feature}/test [--tc CHK-..]`. Chưa cài `maestro` → mọi flow ghi `PENDING "maestro chưa cài"` (không FAIL giả). Có → `maestro test … --format junit --output …`, parse JUnit ra status chuẩn (PASS / FAIL_APP / FAIL_DATA / FAIL_DOC).
6. Báo cáo: sinh N, skip M (CHK + lý do), kết quả theo status; "nghi lỗi app" → ticket Jira (CHK, FR, ảnh, log); "nghi lệch tài liệu" → OQ — theo `.claude/rules/test-trace.md`.

## Chạy trên iOS simulator

Điều kiện: Xcode + iOS Simulator; `curl -fsSL https://get.maestro.mobile.dev | bash`; build app Flutter **bản simulator từ nhánh `tuanvv`** (`flutter build ios --simulator`), cài vào simulator (`xcrun simctl install booted Runner.app`). Bundle id iOS UAT: `innvie.delta.app.uat` (đặt `APP_ID`).

```bash
set -a; source qa/.env; set +a
cd docs/{feature}/test/mobile/maestro
maestro test -e APP_ID=$APP_ID -e QA_REQUESTER_MOBILE_USER -e QA_REQUESTER_MOBILE_PASS flows/
```

App chưa có Semantics/`Key` → engine chọn phần tử theo **chữ hiển thị** (lấy từ `lib/translate/vi.dart`). Đổi chữ trong app = flow hỏng → regen; khi dev thêm Semantics id thì dùng nhãn dạng id trong TC.

## Giới hạn đã biết

- Mức đúng: engine chỉ đảm bảo cú pháp + map cơ học; khớp nghiệp vụ (mức 4) do người đối chiếu.
- `Data:` hiện chỉ ghi chú vào flow; dựng dữ liệu do runner/Bruno làm.
- Nút "Đăng nhập" trong login-as-role dùng `index: 1` (giả định chưa kiểm trên máy thật).

References:
- @.claude/rules/approval-gate.md
- @.claude/rules/test-trace.md
