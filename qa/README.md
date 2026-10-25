# qa/ — phần chạy kiểm thử dùng chung

`qa/` chỉ chứa **runtime dùng chung** (cấu hình môi trường, vai, đăng nhập, helper, subflow). Test do máy sinh nằm trong docs của từng feature để worktree feature ghi được:

| Kênh | Nơi sinh | Công cụ |
|---|---|---|
| Web | `docs/{feature}/test/e2e/` | Playwright |
| API | `docs/{feature}/test/api/bruno-api/` (own API; bảng 3rd-party giữ `test/api/bruno/`) | Bruno CLI (OpenCollection YAML) |
| App | `docs/{feature}/test/mobile/maestro/flows/` | Maestro (subflow chung ở `qa/mobile/subflows/`) |
| Kết quả | `docs/{feature}/test/results/latest.json` | mảng `{chk, target, status, env, build, at, note}` |

## Yêu cầu máy

- Node 24.
- `cd qa && npm install` (người dùng tự chạy; cài Playwright 1.49.1, `@usebruno/cli`, `dotenv`), rồi `npm run pw:install` để tải trình duyệt Chromium.
- Bruno CLI: bản `@usebruno/cli` 3.x (README của `transport-erp/bruno` yêu cầu 3.x; có thể cài global `npm i -g @usebruno/cli`, lệnh `bru`).
- Maestro CLI + Xcode (iOS Simulator) cho test app. Máy hiện chưa có: chỉ sinh flow, chưa chạy được.

## Cấu hình `qa/.env`

1. `cp qa/.env.example qa/.env` (file `.env` đã gitignore, không commit).
2. Điền: `QA_ENV` (dev|sit|local), `QA_TENANT_ID`, `QA_WEB_BASE` (host web FE của môi trường), user/pass từng vai `QA_<ROLE>_USER/_PASS` (tài khoản seed DEV, tự lấy mật khẩu), tuỳ chọn `QA_<ROLE>_ORG_UNIT` / `_FACILITY`, `IGAS_SIM_BASE` + `IGAS_SIM_KEY` (IgasSimulator), `APP_ID` (Maestro).
3. `QA_TENANT_ID` phải **trùng tenant mà bản build FE đang dùng** (FE hard-code giá trị trong `transport-erp-fe/src/app/constants/base.constant.ts`) — lệch thì token đăng nhập theo tenant khác FE, web test rớt giả (401/không thấy dữ liệu). Lấy giá trị từ file đó, không ghi vào tài liệu.
4. Không ghi mật khẩu/khoá vào bất kỳ file nào khác.

## Môi trường (`config/envs.json`)

| Env | API | Web |
|---|---|---|
| dev | https://api-dev-erp.innvie.vn | chưa xác minh — đặt `QA_WEB_BASE` |
| sit | https://api-sit-erp.innvie.vn | chưa xác minh |
| local | http://localhost:8080 | http://localhost:4200 |

Không có prod. Mọi runner từ chối chạy khi `QA_ENV` là prod.

## Vai (`config/roles.json`)

`requester-mobile` (Mobile/Internal), `approver` (Web/Internal), `web-viewer` (Web/Internal), `partner-station` (Mobile/Partner), `finance` (Web/Internal). Test case khai `**Role:** <slug>`; engine đăng nhập sẵn theo vai. Quyền tạo phiếu cấp dầu chỉ cấp cho kênh Mobile nên vai tạo phiếu phải là kênh Mobile.

Đăng nhập BE 3 bước (`qa/web/fixtures/auth.ts`): `POST /api/identity/v1/auth/login` -> nếu `nextStep=workingContextSelectionRequired` thì `POST /auth/working-organization-unit` -> `POST /working-contexts/facility` lấy `X-Working-Context-Id`. Header `X-Tenant-Id`, `Authorization: Bearer`, `X-Working-Context-Id`. Với web, phiên được ghi thành storageState (`qa/.auth/`) theo khoá localStorage của FE; `web/fixtures/runtime-config.ts` chặn `**/assets/runtime-config.js` để trỏ API.

## Cách chạy

Thay `<f>` bằng slug feature (vd `fuel-issuing`). Chạy từ gốc repo.

```bash
# Web (Playwright)
node .claude/scripts/playwright-gen.mjs run --dir docs/<f>/test
# API (Bruno)
node .claude/scripts/bruno-runner.mjs run --dir docs/<f>/test
# App (Maestro)
node .claude/scripts/maestro-gen.mjs run --dir docs/<f>/test
```

Hoặc từ `qa/`: `npm run test:web -- --dir ../docs/<f>/test` (tương tự `test:api`, `test:mobile`; env lấy từ `--env` hoặc `QA_ENV`, mặc định dev). Tham số `--dir` là bắt buộc; đường dẫn tính từ thư mục đang đứng.

## An toàn

Những gì thực sự được máy chặn:

- Web: đăng nhập (`web/fixtures/auth.ts`) từ chối khi `QA_ENV=prod`.
- App: `maestro-gen.mjs run` từ chối khi `QA_ENV` hoặc `--env` là `prod`/`production`.
- API: `bruno-runner.mjs` chỉ chạy env prod khi có `--allow-prod`.
- Playwright: cổng origin khi chạy `run` cho CẢ web (`--base`/`QA_WEB_BASE`) lẫn API (`QA_API_BASE`/`apiBase`) — chỉ host non-prod trong `envs.json` hoặc `.allowed-origins`; `auth.setup.ts` từ chối gửi mật khẩu tới origin API ngoài danh sách đó.
- Playwright chạy bằng `qa/node_modules/.bin/playwright` (gen tạo symlink `e2e/node_modules` → `qa/node_modules`); chưa cài → kết quả PENDING "chưa cài: cd qa && npm install", không tải mạng.
- Khoá/mật khẩu chỉ nằm ở `qa/.env` (gitignore); runner không in giá trị.
- DB chỉ đọc (`qa/db/queries/README.md`).
- Kết quả rớt phân loại: `FAIL_APP` (nghi lỗi app -> ticket Jira dev), `FAIL_DOC` (nghi lệch tài liệu -> OQ), `FAIL_DATA` (QC tự xử).

## Bộ tự kiểm

```bash
node --test .claude/scripts/__tests__/*.test.mjs
```

## Chạy trên UAT (user chốt 26/10/2026)

- `QA_ENV=uat`, app bản simulator `innvie.delta.app.uat` (`APP_ID=innvie.delta.app.uat`).
- UAT **không có giả lập iGAS** và không có seed dev: chỉ chạy luồng không bơm dầu (đăng nhập, danh sách, chi tiết, tạo nháp / gửi, lấy mã iGAS). Bước giả lập bơm sẽ không làm phiếu hoàn thành.
- Hạn chế tạo dữ liệu: UAT có người nghiệm thu. Dùng tài khoản test riêng, đặt tên dữ liệu có tiền tố `QA-`.
- FE bản UAT trỏ API khác app (xem `config/envs.json` › `uat.apiBase_note`); chạy web trên UAT thì xác nhận với dev trước.
