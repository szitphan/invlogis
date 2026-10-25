---
type: report
status: draft
updated: 2026-10-25
links:
  - .claude/rules/test-trace.md
  - .claude/scripts/dev-scan.mjs
  - docs/fuel-issuing/test/
---

# Đề nghị cho đội dev — để BA nối yêu cầu → endpoint/màn/DB → test và chạy test tự động

**Vì sao có file này.** BA đang dựng bộ kiểm thử cho DEV: mỗi yêu cầu (FR/AC) có checklist, test case,
rồi máy sinh test API (Bruno), web (Playwright) và app (Maestro). Máy sinh chỉ chạy được khi repo dev có
4 thứ: **dữ liệu test cố định**, **hợp đồng API xuất ra file**, **mã yêu cầu gắn vào test/endpoint**, và
**điểm bám ổn định trên màn** (testid web, `Semantics(identifier:)` app). Bản quét tĩnh ngày 25/10 cho thấy
cả 3 repo đều chưa có: FE `data-testid` = **0**, app `identifier` = **0**, BE `[Trait]` = **1** trên 17.924
test, chỉ **79/706** AC của BE có test nhắc tới. File này liệt kê việc cần làm, chia nhỏ, làm dần được.
Feature chạy đầu tiên là **cấp dầu** (dGas1 cây nội bộ, rồi dGas1 cây ngoài).

**Cách đọc.**

- **Mã việc**: `DM-BE-NN` (BE .NET `transport-erp`), `DM-FE-NN` (Angular `transport-erp-fe`),
  `DM-APP-NN` (Flutter `driver-portal-flutter`, nhánh `tuanvv`), `DM-SEC-NN` (bảo mật, Mục 5).
  Ghi mã này vào ticket Jira và tiêu đề PR để BA lần được.
- **Ưu tiên**: `P0` chặn đợt test cấp dầu · `P1` cần trong 2–3 sprint · `P2` làm khi tiện.
- **Công sức**: `S` ≤ 1 ngày · `M` 2–4 ngày · `L` ≥ 1 tuần.
- **Xong khi**: một lệnh BA chạy được trên repo dev (grep, có file, hoặc một trường trong JSON của
  `.claude/scripts/dev-scan.mjs`). BA đo tiến độ bằng cách chạy lại dev-scan — xem Mục 7.
- **Việc đầu tiên:** DM-BE-01 (không có dữ liệu test cố định thì mọi test khác không chạy lặp lại được); DM-SEC-01..03 làm song song.
- Thứ tự làm: **BE trước, FE sau, app sau cùng**. Bảo mật (Mục 5) không phụ thuộc thứ tự đó — làm sớm.
- Mọi đường dẫn đã đối chiếu với repo ngày 25/10 (BE `master`, FE `main`, app `origin/tuanvv`).

## 1. Bảng tổng

| Mã | Repo | Việc | Ưu tiên | Công sức | Xong khi |
|---|---|---|---|---|---|
| DM-BE-01 | BE | Lệnh dựng dữ liệu test cố định (idempotent) cho cấp dầu | P0 | L | có `QaFixture*Seed` + `docs/qa/test-fixtures.md` |
| DM-BE-02 | BE | Xuất OpenAPI trong CI, commit `contracts/openapi/v1.json`, chạy oasdiff | P0 | M | file có + workflow có `oasdiff` |
| DM-BE-03 | BE | `[Trait("Ac", …)]` trên test xUnit, backfill 79 AC đã có test | P0 | M | `be-tests.json` traits `Ac=*` ≥ 79 |
| DM-BE-04 | BE | Bruno login nhận `channel`/`platform` theo biến | P0 | S | `01-login.yml` có `{{channel}}` |
| DM-BE-05 | BE | Công bố host + cách nhận key IgasSimulator DEV cho QA | P0 | S | `! grep -A1 igasSimulatorBaseURL bruno/environments/dev.yml \| grep -q localhost` |
| DM-BE-06 | BE | Extension `x-requirements` trên OpenAPI qua operation transformer | P1 | M | `contracts/openapi/v1.json` có `x-requirements` |
| DM-BE-07 | BE | Bruno chuỗi cấp dầu dGas1 (tạo → … → kiểm) | P1 | M | có `bruno/99-workflows/04-fuel-dispensing-*` |
| DM-BE-08 | BE | Bruno assert body/`errorCode`, không chỉ 2xx | P1 | M | ≥ 20 file `11-fuel-dispensings` có `errorCode`/body |
| DM-BE-09 | BE | Bỏ/sửa request Bruno trỏ route không còn | P1 | S | Các file/mẫu tên liệt kê ở Mục 2 không còn trong `bruno/` (`ls` theo từng tên/mẫu ra rỗng) |
| DM-BE-10 | BE | Chạy Bruno nightly trong CI với DEV | P1 | S | workflow có `bru run` |
| DM-BE-11 | BE | `/ready` rớt khi thiếu tenant bootstrap | P1 | S | có health check tag `ready` cho tenant |
| DM-BE-12 | BE | Xác nhận nginx DEV nâng cấp WebSocket `/hubs` | P1 | S | xác nhận thủ công: README dev-server có dòng "Đã kiểm DEV" kèm ngày |
| DM-BE-13 | BE | Mở rộng bộ lọc test PR (8 project đang bị loại) | P2 | S | `grep -c "Tools.IgasSimulator\|UnitTests.BuildingBlocks.Realtime\|UnitTests.Modules.Knowledge" TransportERP.PRTests.slnf` ≥ 3 |
| DM-FE-01 | FE | Quy ước `data-testid` + gắn 1 lần ở component dùng chung | P0 | M | `fe-testids.json` folder `components` > 0 |
| DM-FE-02 | FE | Gắn testid màn cấp dầu (`oil-supply-voucher`) | P0 | S | folder `features/oil-supply-voucher` `dataTestId` > 0 |
| DM-FE-03 | FE | Khôi phục `e2e/`, Playwright trỏ DEV qua biến | P1 | S | có `e2e/` + `PW_BASE_URL` trong config |
| DM-FE-04 | FE | Mở drawer theo `?detail=<id>` (cấp dầu trước) | P1 | M | `queryParam` `detail` trong `oil-supply-voucher` |
| DM-FE-05 | FE | `label-item` thành `<label for>` thật | P1 | M | grep `<div class="label-item"` giảm về 0 |
| DM-FE-06 | FE | `aria-label` cho nút chỉ có icon | P1 | S | `fe-testids.json` `ariaLabel` tăng rõ |
| DM-FE-07 | FE | CI: typecheck + unit test cho PR | P1 | S | workflow có `npm run typecheck` |
| DM-FE-08 | FE | `html lang` đúng ngôn ngữ | P2 | S | `src/index.html` không còn `lang="en"` cố định |
| DM-APP-01 | App | Tham số `testId` → `Semantics(identifier:)` trên ~7 widget design system | P0 | M | `app-semantics.json` `identifier` ≥ 7 |
| DM-APP-02 | App | Gắn `testId` màn cấp dầu | P0 | S | module `delta/fuel_dispensing` `identifier` > 0 |
| DM-APP-03 | App | Cờ `E2E` bật nút giả lập bơm / mock dGas3 / tắt Alice | P0 | M | grep `fromEnvironment('E2E'` |
| DM-APP-04 | App | Bản build test cho iOS simulator trỏ DEV bằng `--dart-define` | P0 | M | có `env/dev.json` + script build e2e |
| DM-APP-05 | App | Deep link tới màn cấp dầu | P1 | M | `deep_link.dart` có route `dgas` |
| DM-APP-06 | App | Hỏi lại trạng thái cấp quyền bơm khi mất realtime | P1 | M | `git grep -i "periodic\|poll"` trong `igas_internal_fuel_supply` ra mã chạy |
| DM-APP-07 | App | Khôi phục 38 file test đã xoá | P1 | S | `test/` trên `tuanvv` ≥ 38 file |
| DM-APP-08 | App | Dọn nhánh mặc định (`main` tụt 194 commit so với `tuanvv`) | P1 | S | `git rev-list --count origin/main..origin/tuanvv` ≤ 5 |
| DM-SEC-01 | App | Thu hồi + xoá 2 khoá Apple `.p8` khỏi repo và lịch sử | P0 | S | `git ls-tree` không còn `*.p8` và `git log --all --oneline -- 'AuthKey*'` rỗng (sau khi lọc lịch sử) |
| DM-SEC-02 | App | Mật khẩu keystore ra khỏi `config.json` / `build.gradle` | P0 | S | `! git grep -nE '(store\|key)Password"?\s*[:=]?\s*"[^"$]' origin/tuanvv -- assets/json/config.json android/app/build.gradle` |
| DM-SEC-03 | App | Bỏ key simulator + `X-API-Key` viết cứng trong app | P0 | S | grep 2 file không còn chuỗi key |
| DM-SEC-04 | App | Token sang secure storage | P1 | M | `SharedPrefsKey.token` không còn dùng |
| DM-SEC-05 | BE | Thay dữ liệu seed giống nhân sự thật bằng dữ liệu tổng hợp | P0 | M | `grep 'new(' AccountDevelopmentSeedData.cs \| grep -vc '"dev\.'` = 0 (mọi username có tiền tố `dev.`) và danh sách tên thật BA giữ riêng không còn khớp trong `Seeding/Development/` |
| DM-SEC-06 | BE | Bí mật dev ra khỏi `appsettings.json` | P1 | S | 5 khoá `DefaultConnection`, `MinIO.AccessKey/SecretKey`, `RabbitMq.Password`, `Identity.Jwt.SecretKey` rỗng hoặc `${…}` (lệnh ở Mục 5) |
| DM-SEC-07 | BE | Xoá `db/migrations/20260827_igas_delta_schema.sql` khỏi repo và lịch sử | P0 | M | `git ls-tree -r HEAD --name-only \| grep -c igas_delta_schema` = 0 và `git log --all --oneline -- db/migrations/20260827_igas_delta_schema.sql` rỗng |

## 2. BE — `transport-erp`

### DM-BE-01 · Lệnh dựng dữ liệu test cố định · P0 · L

**Hiện trạng.** Có khung seed (`src/BuildingBlocks/TransportERP.BuildingBlocks.Data/Initialization/IDevelopmentDataSeed.cs`,
`ISystemDataSeed.cs`) và seed dev cho Identity/HRM/Organization. Nhưng `make seed` (`Makefile:116`) **xoá DB
rồi dựng lại** — chỉ dùng được ở máy dev; `docs/modules/identity/development-seeding.md` ghi rõ "không chạy
lên DB remote". DEV hiện không có cách dựng lại đúng bộ dữ liệu test cấp dầu sau khi bị test làm bẩn.

**Cần.** Một seed riêng (vd `QaFixtureDevelopmentSeed` theo module, bật bằng `QaFixtures__Seed=true`) hoặc
tool CLI `tools/TransportERP.Tools.QaFixtures`, chạy được trên DEV, **idempotent** (chạy lại không nhân đôi,
không xoá dữ liệu khác, khoá theo mã cố định). Bộ tối thiểu:

| Nhóm | Dữ liệu | Dùng cho |
|---|---|---|
| Tổ chức | 1 chi nhánh test có **mã viết tắt** (`OrganizationUnit.ShortCode`) — mã phiếu sinh ra đọc được | mọi luồng |
| Cây nội bộ | 1 cây dầu nội bộ khớp DB iGAS test (cảm biến/vòi có trong IgasSimulator) | luồng A dGas1 |
| Cây ngoài | 1 cây ngoài + 1 tài khoản đối tác (Partner) gắn cây đó | luồng C |
| Định mức | định mức dầu nhân viên (`EmployeeFuelQuota`) cho tài khoản tạo phiếu, kỳ hiện tại | kiểm hạn mức |
| Vai "QA cấp dầu" | kênh **Mobile**; quyền `fuel.fuelDispenses.dGas1.maintain` (và dGas2–5 nếu cần), `fuel.fuelDispenses.dispensingAuthorizations.request`, `fuel.fuelDispenses.pumping.record`, `fuel.fuelDispenses.invoices.export` | tạo phiếu trên app/API |
| Vai duyệt | `fuel.fuelDispenses.approval` + quyền xử lý `approval-work-items` | duyệt luồng C |
| Vai xem web | `fuel.fuelDispenses.view`, `fuel.fuelDispenses.outside.view` (kênh Web) | Playwright |
| Kế toán | quyền thanh toán/đối soát cấp dầu (kênh Web) | thanh toán luồng C |
| Đối tác | `fuel.fuelDispenses.partner.view`, `partner.pumping.record`, `partner.invoices.export`, `partner.close` | nhân viên cây đối tác |

Mỗi tài khoản 1 username cố định có tiền tố `qa.`, mật khẩu đọc từ biến môi trường (vd
`TRANSPORTERP_QA_SEED_PASSWORD`), **không** ghi trong repo. Kèm `docs/qa/test-fixtures.md` liệt kê khoá dữ
liệu (username, mã cây, mã chi nhánh, id) để BA map vào `qa/config/roles.json`.

**Xong khi:** `git grep -l "QaFixture" -- src tools` ra file seed **và** `test -f docs/qa/test-fixtures.md`.

### DM-BE-02 · Xuất OpenAPI trong CI + oasdiff · P0 · M

**Hiện trạng.** Host đã có OpenAPI (`src/Host/TransportERP.Api/Extensions/OpenApiExtensions.cs:21` `AddOpenApi("v1")`,
`:60` `MapOpenApi()`) nhưng không file nào được commit; `contracts/` chỉ có `frontend-i18n/`; không workflow
nào trong `.github/workflows/` nhắc `openapi`.

**Cần.** Bước CI sinh tài liệu lúc build (gói `Microsoft.Extensions.ApiDescription.Server`) hoặc khởi động
host rồi tải `/openapi/v1.json`; ghi ra `contracts/openapi/v1.json`, commit cùng PR; chạy `oasdiff breaking`
so với `master`, báo trên PR. BA dùng file này để map endpoint ↔ FR và sinh Bruno.

**Xong khi:** `test -f contracts/openapi/v1.json && grep -l oasdiff .github/workflows/*.yml`.

### DM-BE-03 · Gắn mã AC vào test xUnit · P0 · M

**Hiện trạng.** 79 AC có test nhắc tới — nhưng qua **comment** (vd
`tests/IntegrationTests/Modules/TransportERP.IntegrationTests.Modules.FuelManagement/Api/FuelDispensings/DGas1EmployeeFuelQuotaIntegrationTests.cs:150`
`// FU-FD-AC-120`). Cả repo chỉ có 1 `[Trait]` (`Category=Chaos`). Comment không lọc được khi chạy
(`dotnet test --filter`) và không ra trong báo cáo kết quả.

**Cần.** `[Trait("Ac","FU-FD-AC-120")]` (nhiều AC = nhiều Trait) trên mỗi test; tuỳ chọn
`[Trait("Req","FR-fuel-issuing-R003")]` khi ticket có mã FR của BA. Backfill 79 AC đã có test trước, nhóm
`FU-FD` (cấp dầu, 15 AC) và `FU-EFQ` (định mức, 16 AC) làm đầu. Thêm 1 dòng vào quy ước test của repo
(skill `.agents/skills/dotnet-unit-test`, `.agents/skills/dotnet-integration-test`) để agent tự gắn.

**Xong khi:** `be-tests.json` → `traits` có các khoá `Ac=…` tổng ≥ 79; `totals.traitUsages` ≥ 79.

### DM-BE-04 · Bruno login theo kênh · P0 · S

`bruno/00-auth/01-login.yml` viết cứng `"platform": "Web"`, `"channel": "Web"`. Quyền tạo phiếu cấp dầu chỉ
cấp cho kênh Mobile → không thể dùng collection này để tạo phiếu. Đổi thành `{{channel}}`/`{{platform}}`,
mặc định `Web` trong `bruno/environments/*.yml`.

**Xong khi:** `grep -c "{{channel}}" bruno/00-auth/01-login.yml` ≥ 1.

### DM-BE-05 · IgasSimulator DEV cho QA · P0 · S

`tools/TransportERP.Tools.IgasSimulator/README.md:21` ghi "ask ops for the current host/port" và key
`TRANSPORTERP_IGAS_SIMULATOR_API_KEY`; `bruno/environments/dev.yml` để `igasSimulatorBaseURL` =
`http://localhost:5099`. Cần: ghi host DEV công khai vào README + `dev.yml`; giao key cho QA qua kho bí mật
của đội (không qua chat, không commit). BA chỉ đọc key qua biến môi trường.

**Xong khi:** `! grep -A1 igasSimulatorBaseURL bruno/environments/dev.yml | grep -q localhost`.

### DM-BE-06 · `x-requirements` trên OpenAPI · P1 · M

Thêm attribute (vd `[Requirement("FU-FD-AC-002")]`) trên action controller và một
`RequirementsOperationTransformer` trong `src/Host/TransportERP.Api/Extensions/OpenApi/` (cùng chỗ với
`EndpointSummaryOperationTransformer.cs`, `ErrorResponseOperationTransformer.cs`) ghi
`"x-requirements": ["FU-FD-AC-002"]` vào operation. Làm trước cho `FuelDispensingsController.cs`,
`FuelDispensingAuthorizationsController.cs`, `PartnerFuelDispensingsController.cs`. Phụ thuộc DM-BE-02.

**Xong khi:** `grep -c '"x-requirements"' contracts/openapi/v1.json` ≥ 10.

### DM-BE-07 · Bruno chuỗi cấp dầu · P1 · M

`bruno/FuelManagement/11-fuel-dispensings/` có request lẻ (chủ yếu dGas5), `bruno/Tools/IgasSimulator/` có
`in-use`/`pumped`, nhưng `bruno/99-workflows/` chưa có luồng cấp dầu. Cần 2 thư mục:

- `04-fuel-dispensing-dgas1-internal`: đăng nhập Mobile → `POST /fuel-dispensings` → `POST …/submit` →
  `POST …/dispensing-authorizations` → simulator `in-use` → `pumped` → `GET /fuel-dispensings/{id}` kiểm trạng thái.
- `05-fuel-dispensing-dgas1-external`: tạo + submit (Mobile) → duyệt `POST /api/workflow/v1/approval-work-items/{id}/decisions`
  (Web) → đối tác `PUT …/partner/…/pumping-evidence`, `invoice-evidence`, `POST …/close` → kiểm.

Mỗi bước lưu id sang bước sau bằng `bru.setVar`, dùng dữ liệu của DM-BE-01.

**Xong khi:** `ls bruno/99-workflows | grep -c fuel-dispensing` ≥ 2.

### DM-BE-08 · Assert body và `errorCode` · P1 · M

446 trong 451 request Bruno chỉ assert `res.status` 2xx; chỉ 2 file nhắc `errorCode`. Cần assert trường trạng thái/khoá
trong body cho request thành công và thêm request lỗi có chủ đích (thiếu quyền, sai trạng thái) assert
`errorCode`. Làm trước `FuelManagement/11-fuel-dispensings/` và `15-partner-fuel-dispensings/`.

**Xong khi:** `grep -l "errorCode" -r bruno/FuelManagement | wc -l` ≥ 20.

### DM-BE-09 · Request Bruno cũ · P1 · S

Đối chiếu 451 request với 539 endpoint trong code: khoảng 12 request trỏ route không còn, vd
`FuelManagement/11-fuel-dispensings/19-get-fuel-dispensings-eligible-purpose-sources.yml`,
`22-get-fuel-dispensings-actions-*-availability.yml` (route nay là `actions/{actionToken}/availability`),
`FuelManagement/08-fuel-receivings/14-put-fuel-receivings-id-draft.yml`, `17-post-fuel-receivings-id-submissions.yml`,
`FuelManagement/07-purchase-plans/16-…-revisions-diff.yml`, `18-…-diff.yml`,
`FuelManagement/04-external-fuel-station-creation-requests/02-…-draft.yml`, `11-…-draft.yml`,
`FleetManagement/13-vehicle-transfers/14-post-vehicle-transfers-businessRequestId-complete-signing.yml`.
Sửa hoặc xoá. (Một số request trong `99-workflows/`, `HRM/`, `Inventory/` có URL đặt trong ngoặc kép — máy đối
chiếu của BA chưa đọc được, không tính là lệch.)

**Xong khi:** BA bổ sung bước đối chiếu Bruno↔endpoint vào dev-scan trước; đến lúc đó dev tự xác nhận: `ls` theo từng tên/mẫu liệt kê ở trên (trong `bruno/`) ra rỗng.

### DM-BE-10 · Bruno nightly · P1 · S

`.github/workflows/ci.yml` chỉ chạy `dotnet test` (lịch tuần, thứ Hai 02:00). Thêm job lịch hằng đêm
`bru run --env ci` (hoặc `dev`) với tài khoản QA từ secret; xuất JUnit để BA đọc.

**Xong khi:** `grep -l "bru run" .github/workflows/*.yml`.

### DM-BE-11 · `/ready` kiểm tenant bootstrap · P1 · S

`src/Host/TransportERP.Api/Extensions/ApiEndpointRouteBuilderExtensions.cs:34` map `/ready` theo tag `ready`;
hiện chỉ HRM, ServiceOps, Workflow gắn tag. DEV thiếu tenant bootstrap (`BootstrapTenantOptions`, seed
`ConfiguredTenantsSystemSeed.cs`) mà `/ready` vẫn xanh → test chạy và rớt hàng loạt vì sai lý do. Thêm
health check tag `ready` kiểm tenant cấu hình đã tồn tại.

**Xong khi:** `git grep -n "BootstrapTenant" -- 'src/**/*HealthCheck*.cs'` ra kết quả.

### DM-BE-12 · WebSocket `/hubs` trên DEV · P1 · S

Hub `DispensingAuthorizationStatusHub.cs:28` (`/hubs/v1/fuel/dispensing-authorizations`) cần nginx nâng cấp
WebSocket; cấu hình có ở `deploy/dev-server/nginx/websocket-upgrade.conf`, lệnh kiểm ở
`deploy/dev-server/README.md:388`. Nhờ ops chạy lệnh đó trên DEV, ghi kết quả + ngày vào README. App cấp
dầu chờ trạng thái qua hub này.

**Xong khi:** xác nhận thủ công — `grep -n "Đã kiểm DEV" deploy/dev-server/README.md` ra dòng có ngày (do ops ghi).

### DM-BE-13 · Bộ lọc test PR · P2 · S

`TransportERP.PRTests.slnf` (dùng cho PR thường, `ci.yml:35`) bỏ ngoài 8 project test:
`E2ETests`, `IntegrationTests.Api`, `IntegrationTests.Modules.Dispatch`, `IntegrationTests.Tools.IgasSimulator`,
`UnitTests.BuildingBlocks.Hashing`, `UnitTests.BuildingBlocks.Realtime`, `UnitTests.Modules.Dispatch`,
`UnitTests.Modules.Knowledge`. Ít nhất thêm các unit test + `IntegrationTests.Tools.IgasSimulator` vào PR filter.

**Xong khi:** `grep -c "Tools.IgasSimulator\|UnitTests.BuildingBlocks.Realtime\|UnitTests.Modules.Knowledge" TransportERP.PRTests.slnf` ≥ 3.

## 3. FE — `transport-erp-fe`

### DM-FE-01 · Quy ước testid, gắn ở component dùng chung · P0 · M

**Hiện trạng.** 400 file HTML, **0** `data-testid`; Playwright phải bám chữ hiển thị (đổi i18n là vỡ).

**Quy ước.** `data-testid="{screen-slug}.{element-slug}"`, kebab-case, vd `oil-supply.create-button`,
`oil-supply.table.row`, `oil-supply.filter.status`. Dòng bảng thêm khoá bản ghi bằng `data-row-key="<id>"`
(không nhét id vào testid).

**Làm 1 lần ở component dùng chung** (input `testId` hoặc directive `appTestId` ghi ra `data-testid`):

- `src/app/components/table-common/` (bảng, dòng, ô hành động, phân trang) — kèm `filter-table/`
- `src/app/components/select-server-search/` (ô chọn, ô tìm, từng option)
- `src/app/components/confirm-modal/` (nút xác nhận/huỷ)
- `src/app/components/actions-toolbar-detail/` (từng nút hành động)
- drawer: không có component drawer chung, 28 file dùng `<nz-drawer>` trực tiếp → directive gắn được lên
  `nz-drawer` (thân, nút đóng, chân nút)

Thêm quy tắc vào `.agents/rules/references/angular-convention-html.mdc` để agent tự gắn khi tạo màn mới.
Bản trong `src/app/app-garages/components/` (select-server-search, confirm-modal) làm theo sau.

**Xong khi:** `fe-testids.json` → `byFolder["components"].dataTestId` > 0 **và**
`grep -c testid .agents/rules/references/angular-convention-html.mdc` ≥ 1.

### DM-FE-02 · Testid màn cấp dầu · P0 · S

`src/app/features/oil-supply-voucher/` (15 file HTML; route `oil-supply`): bảng đang xử lý / đã xong, drawer
chi tiết `oil-supply-voucher-detail/` (tab bơm, tab hoá đơn, thẻ cấp quyền), nút duyệt/từ chối. Phụ thuộc DM-FE-01.

**Xong khi:** `fe-testids.json` → `byFolder["features/oil-supply-voucher"].dataTestId` > 0.

### DM-FE-03 · Khôi phục `e2e/` · P1 · S

`playwright.config.ts` trỏ `testDir: './e2e'` nhưng thư mục bị xoá ở commit `24f294d6` (CD-543). Config trỏ
`http://localhost:4200` và tự chạy `npm run start`. Cần: tạo lại `e2e/` (có thể chỉ `README.md` + 1 smoke
test), `baseURL` đọc `PW_BASE_URL` (mặc định DEV), chỉ bật `webServer` khi chạy local. BA sinh test vào repo BA;
thư mục này để dev thêm test riêng và để cấu hình chung khớp nhau.

**Xong khi:** `test -d e2e && grep -c PW_BASE_URL playwright.config.ts` ≥ 1.

### DM-FE-04 · Deep link `?detail=<id>` · P1 · M

Drawer chi tiết phiếu cấp dầu (`oil-supply-voucher-detail.dialog.ts`) chỉ mở bằng bấm dòng; trong feature
không có `queryParams`. Cần: mở drawer khi URL có `?detail=<id>`, đóng drawer thì xoá param. Test vào thẳng
phiếu vừa tạo bằng API, không phải lọc/tìm. Sau cấp dầu: các drawer khác có trong luồng test.

**Xong khi:** `git grep -n "detail" -- src/app/features/oil-supply-voucher | grep -c queryParam` ≥ 1.

### DM-FE-05 · `label-item` thành `<label for>` · P1 · M

833 chỗ dùng class `label-item` (828 là `<div>`) (style ở `src/app/app-garages/_public/styles/legacy/custom.scss:15`,
directive `src/app/directives/required-field-mark.directive.ts` selector `.label-item[appRequiredFieldMark]`).
`div` không nối với ô nhập → Playwright không dùng được `getByLabel`, trình đọc màn hình không đọc nhãn. Đổi
thành `<label class="label-item" [for]="…">` + `id` trên ô nhập; mở rộng selector directive. Làm theo feature,
cấp dầu trước.

**Xong khi:** `git grep -c '<div class="label-item"' -- src/app/features/oil-supply-voucher` = 0 (rồi toàn repo).

### DM-FE-06 · `aria-label` nút icon · P1 · S

Cả repo chỉ 35 `aria-label`. Nút chỉ có icon (sửa, xoá, đóng drawer, mở menu) cần `aria-label` có dịch.
Gắn ở component dùng chung trước (DM-FE-01).

**Xong khi:** `fe-testids.json` → `totals.ariaLabel` ≥ 100.

### DM-FE-07 · CI kiểm PR · P1 · S

`.github/workflows/` chỉ có `dev-release.yml`, `promote-image.yml`, `sit-release.yml`. `package.json` đã có
`typecheck` và `test:ci`. Thêm workflow PR chạy 2 lệnh này.

**Xong khi:** `grep -l "npm run typecheck" .github/workflows/*.yml`.

### DM-FE-08 · `html lang` · P2 · S

`src/index.html:2` là `<html lang="en">` trong khi giao diện tiếng Việt. Đặt `vi` và đổi theo ngôn ngữ người dùng chọn.

**Xong khi:** `grep -c 'lang="en"' src/index.html` = 0.

## 4. App — `driver-portal-flutter` (nhánh `tuanvv`)

### DM-APP-01 · `testId` → `Semantics(identifier:)` · P0 · M

**Hiện trạng.** 1.101 file Dart, **0** `Semantics`, **0** `identifier`, **0** `Key(`. Maestro trên iOS
chỉ bám được chữ hiển thị.

**Cần.** Thêm tham số `String? testId` vào ~7 widget design system ở `lib/core/core/design_system/`:
`custom_button.dart`, `custom_icon_button.dart`, `custom_textfield.dart`, `custom_dropdown.dart`,
`custom_search_box.dart`, `custom_tab_bar.dart`, `custom_bottom_sheet.dart`. Khi có `testId` thì bọc
`Semantics(identifier: testId, child: …)`. Quy ước tên giống web: `{screen-slug}.{element-slug}`
(vd `create-dgas1.submit-button`). Thêm rule `.agents/rules/testability-standard.md` (cạnh
`.agents/rules/null-fallback-standard.md`) để agent tự truyền `testId` khi dựng màn.

**Xong khi:** `app-semantics.json` → `totals.identifier` ≥ 7.

### DM-APP-02 · `testId` màn cấp dầu · P0 · S

`lib/modules/delta/fuel_dispensing/` — màn tạo dGas1 (`create/create_dgas1/presentation/ui/create_dgas1_page.dart`,
`dgas1_draft_page.dart`), màn cấp dầu iGAS nội bộ/ngoài (`igas/igas_internal_fuel_supply/`, `igas/igas_external_fuel_supply/`),
nút nộp, nút xin cấp quyền bơm, mã iGAS hiển thị. Phụ thuộc DM-APP-01.

**Xong khi:** `app-semantics.json` → `byModule["modules/delta/fuel_dispensing"].identifier` > 0.

### DM-APP-03 · Cờ `E2E` · P0 · M

Có sẵn đồ giả lập trong app nhưng không có công tắc rõ:

- giả lập bơm: `igas/igas_internal_fuel_supply/presentation/ui/widgets/igas_fake_pump_bottom_sheet.dart`
- mock dGas3: `create/create_dgas3/domain/usecases/mock_create_transport_order_completion_usecase.dart`
- Alice (soi HTTP, có lớp phủ màn): `lib/core/utils/alice_inspector.dart`, nối ở `lib/main.dart:14`, `:108`

Cần `const bool kE2E = bool.fromEnvironment('E2E')`: bản E2E **hiện** nút giả lập bơm có `testId`, **tắt** Alice
(lớp phủ che nút, làm Maestro bấm trượt); bản phát hành **không bao giờ** có nút giả lập/mock.

**Xong khi:** `git grep -n "fromEnvironment('E2E'" origin/tuanvv -- lib` ra kết quả.

### DM-APP-04 · Bản build test iOS simulator trỏ DEV · P0 · M

Môi trường đổi bằng `switch_environment.sh` (sửa thẳng `assets/json/config.json`, `project.pbxproj`,
`Info.plist`, `build.gradle`) — không lặp lại được trong CI. Cần: `--dart-define-from-file=env/dev.json`
(chỉ URL công khai + `E2E=true`, không bí mật) và script `scripts/build-e2e-ios.sh` ra `.app` cho iOS
simulator trỏ `https://api-dev-erp.innvie.vn`.

**Xong khi:** `git ls-tree -r --name-only origin/tuanvv | grep -c "env/dev.json\|build-e2e-ios"` ≥ 2.

### DM-APP-05 · Deep link màn cấp dầu · P1 · M

`lib/core/core/deeplink/deep_link.dart` chỉ dẫn tới `/main`, `/repair-detail`, `/change-password`,
`/history-activity`, `/login` (scheme Android `Delta://mobileapp`). Route cấp dầu đã có tham số, vd
`/dgas1-draft?fuelDispensingId=` (`lib/core/core/router/delta/delta_routers.dart:120`). Thêm vào deep link để
Maestro mở thẳng phiếu tạo bằng API (`openLink`), không phải đi qua menu.

**Xong khi:** `git show origin/tuanvv:lib/core/core/deeplink/deep_link.dart | grep -c -i dgas` ≥ 1.

### DM-APP-06 · Hỏi lại trạng thái khi mất realtime · P1 · M

Trạng thái cấp quyền bơm chỉ nhận qua SignalR
(`igas/igas_internal_fuel_supply/data/realtime/dispensing_authorization_realtime_service.dart`). Trong `igas_internal_fuel_supply` chưa có hỏi lại trạng thái (chỉ có đếm ngược `Timer.periodic` ở `igas_adhoc_fuel_supply`, không phải hỏi lại). Mạng chập hoặc DEV chưa nâng cấp WebSocket (DM-BE-12) → màn
treo, test rớt ngẫu nhiên. Thêm hỏi lại định kỳ (`GET /api/fuel-management/v1/me/fuel-dispensings/{id}`) khi
hub mất kết nối.

**Xong khi:** `git grep -n -i "periodic\|poll" origin/tuanvv -- lib/modules/delta/fuel_dispensing/igas/igas_internal_fuel_supply` ra kết quả (BA kiểm tay thêm: kết quả phải là mã chạy, không phải dòng chú thích).

### DM-APP-07 · Khôi phục test đã xoá · P1 · S

`test/` trên `tuanvv` hiện **trống**; 38 file test bị xoá: 34 ở `59d825e` (24/10 "fix bugs"), 3 ở `7b780c6`
(12/10), 1 ở `0047e7b` (15/10) — gồm `test/modules/delta/fuel_dispensing/create_dgas1_draft_test.dart`,
`dgas_permission_helper_test.dart`, `fuel_dispensing_action_permissions_test.dart`… Khôi phục, sửa cho chạy được.

**Xong khi:** `git ls-tree -r --name-only origin/tuanvv test | grep -c _test.dart` ≥ 38.

### DM-APP-08 · Nhánh mặc định · P1 · S

`origin/HEAD` = `main` (commit cuối 2026-09-09); `tuanvv` hơn `main` 194 commit, kém 8. Ai clone mặc định
sẽ build bản cũ. Đưa `tuanvv` vào `main` (hoặc đổi nhánh mặc định) và giữ 1 dòng phát triển. Tiện dọn file rác
ở gốc: `.DS_Store`, `.flutter-plugins-dependencies 2`, `.flutter-plugins-dependencies 3`.

**Xong khi:** `git rev-list --count origin/main..origin/tuanvv` ≤ 5.

## 5. Bảo mật

Chỉ ghi vị trí, không ghi giá trị. Nên làm trước hoặc song song mọi việc trên.

| Mã | Repo | Vị trí | Vấn đề | Việc |
|---|---|---|---|---|
| DM-SEC-01 | App | 2 file `AuthKey_*.p8` ở gốc repo, thêm ở commit `653ab8f` (2026-01-19), có trên cả `main` và `tuanvv` | Khoá API App Store Connect / APNs trong git | Thu hồi 2 khoá trên Apple Developer, tạo khoá mới cất ở kho bí mật CI; xoá khỏi lịch sử (`git filter-repo`), thêm `*.p8` vào `.gitignore` |
| DM-SEC-02 | App | `assets/json/config.json` dòng 15, 17, 33, 35, 51, 53, 69, 71 (`storePassword`/`keyPassword`); `android/app/build.gradle:48`, `:50` | Mật khẩu keystore trong repo; `assets/` còn bị **đóng gói vào app** | Đưa ra `key.properties` (gitignore) / secret CI; đổi mật khẩu keystore nếu được |
| DM-SEC-03 | App | `lib/modules/delta/fuel_dispensing/igas/igas_internal_fuel_supply/data/repositories_impl/igas_internal_fuel_supply_repository_impl.dart:51` (khoá simulator); `lib/modules/delta/fuel_dispensing/create/create_dgas3/data/repositories_impl/create_dgas3_repository_impl.dart:247` (`X-API-Key`) | Khoá viết cứng, ai giải nén app cũng lấy được | Bỏ khỏi mã; nếu bản E2E cần thì truyền `--dart-define` chỉ cho bản E2E (DM-APP-03); đổi khoá phía server |
| DM-SEC-04 | App | `lib/core/core/data_local/shared_prefs_key.dart` (`token`, `refresh_token`, `password`), `lib/core/core/manager/account_manager.dart` (lưu `user_model` có `accessToken`) | Token (và có thể mật khẩu "ghi nhớ") nằm trong SharedPreferences không mã hoá; `flutter_secure_storage` đã có trong `pubspec.yaml` mà chưa dùng cho token | Chuyển token sang secure storage; không lưu mật khẩu |
| DM-SEC-05 | BE | `src/Modules/Identity/TransportERP.Modules.Identity.Infrastructure/Seeding/Development/AccountDevelopmentSeedData.cs`, `src/Modules/HRM/TransportERP.Modules.HRM.Infrastructure/Seeding/Development/EmployeeDevelopmentSeedData.cs`, `docs/modules/identity/development-seeding.md` | Dữ liệu có nguồn từ hệ thống thật (mã NV + username + họ tên giống nhân sự thật); đề nghị thay bằng dữ liệu tổng hợp để repo không giữ dữ liệu thật | Thay bằng dữ liệu giả (tên tổng hợp, tiền tố `dev.`) |
| DM-SEC-06 | BE | `src/Host/TransportERP.Api/appsettings.json`: `ConnectionStrings:DefaultConnection` (dòng 61), `MinIO` `AccessKey`/`SecretKey` (~165), RabbitMQ `Password` (~195), `Identity:Jwt:SecretKey` (269) | Giá trị mặc định cho dev nằm trong file đã commit; cần chuyển sang biến để SIT/DEV không dùng chung. | Để rỗng / `${TRANSPORTERP_…}` như các khoá khác trong cùng file đã làm; xác nhận DEV/SIT không dùng chung giá trị |
| DM-SEC-07 | BE | `db/migrations/20260827_igas_delta_schema.sql` (13.546 dòng, ~12.200 `INSERT`; đầu file ghi nguồn là bản dump đầy đủ của DB IGas ngày 27/07) | Dữ liệu có nguồn từ hệ thống thật; đề nghị thay bằng dữ liệu tổng hợp để repo không giữ dữ liệu thật | Xoá khỏi repo + lịch sử (`git filter-repo --path db/migrations/20260827_igas_delta_schema.sql --invert-paths`); thay bằng bộ dữ liệu iGAS tổng hợp nhỏ cho DM-BE-01 |

**Kiểm DM-SEC-06** (trong `src/Host/TransportERP.Api/`, không in giá trị; mỗi lệnh phải ra 0):

- `grep -cE '"DefaultConnection"\s*:\s*"[^$]' appsettings.json`
- `grep -cE '"(AccessKey|SecretKey)"\s*:\s*"[^"$]' appsettings.json` (MinIO và `Identity:Jwt`)
- `grep -cE '"Password"\s*:\s*"[^"$]' appsettings.json` (RabbitMQ)

Ghi chú: `apiKey` trong `lib/firebase_options.dart` là khoá công khai của Firebase — không tính là lộ, nhưng
nên giới hạn theo app ID trên Firebase console.

## 6. Nối mã yêu cầu giữa BA, dev và Jira

Hiện có 3 hệ mã, chưa nối với nhau:

| Hệ mã | Ai đặt | Ở đâu | Ví dụ |
|---|---|---|---|
| FR/BR/NFR của BA | BA | `docs/{feature}/srs/`, bộ tái lập `docs/_reverse/{feature}/` (mã có chữ **R**) | `FR-fuel-issuing-R003` |
| AC của dev | dev | `transport-erp/docs/modules/**/requirements.md` (706 AC, 79 có test) | `FU-FD-AC-002` |
| Jira | PM/dev | ticket `CD-NNN`; quét commit thấy 223 mã: BE 179, FE 56, **app 0** | `CD-482` |

- **BA giữ bảng nối** `docs/_shared/requirements-map` (sẽ lập sau): mỗi FR của BA ↔ AC của dev ↔ ticket CD.
  Test của BA ghi Ref dạng `FR-fuel-issuing-R003, AC:FU-FD-AC-002`, nên khi dev gắn Trait (DM-BE-03) và
  `x-requirements` (DM-BE-06), một test rớt truy được thẳng tới đoạn code và ticket.
- **Đề nghị dev:** ticket Jira ghi mã FR (của BA) và AC (của dev) trong mô tả; tiêu đề PR dạng
  `CD-482 FU-FD-AC-002: …`; commit app cũng mang `CD-NNN` như BE/FE đang làm.
- Đáp án test: chỗ BA đã chốt theo tài liệu BA; chỗ chưa chốt tạm theo AC của dev, nhãn
  `[đáp án: code FU-FD-AC-002]`. BA chốt khác code → test rớt → BA mở CR cho dev, không tự sửa đáp án.

## 7. BA đo tiến độ thế nào

Chạy lại `node .claude/scripts/dev-scan.mjs --out <dir>` (repo BA), so `summary.json` và file chi tiết với
bản 25/10. Việc dev-scan chưa đo được thì BA chạy lệnh ở cột "Xong khi" (Mục 1); BA sẽ bổ sung dần các kiểm
đó vào dev-scan.

| Mã | Bằng chứng | Mốc 25/10 |
|---|---|---|
| DM-BE-01 | grep `QaFixture` trong `src`/`tools` + có `docs/qa/test-fixtures.md` | chưa có |
| DM-BE-02 | có `contracts/openapi/v1.json`; workflow có `oasdiff` | chưa có |
| DM-BE-03 | `summary.json` → `be.traitUsages`; `be-tests.json` → `traits` khoá `Ac=…`; `be.acTraced` | 1 · 0 · 79 |
| DM-BE-04/05/07/08/09/10 | grep trong `bruno/` + `.github/workflows/` (Mục 2) | chưa có |
| DM-BE-06 | đếm `x-requirements` trong `contracts/openapi/v1.json` | 0 |
| DM-BE-11/12/13 | grep như Mục 2 | chưa có |
| DM-FE-01/02 | `summary.json` → `fe.dataTestId`; `fe-testids.json` → `byFolder[…].dataTestId` | 0 |
| DM-FE-05 | `fe-testids.json` → `totals.labelItem` (đếm class) + grep `<div class="label-item"` | 833 |
| DM-FE-06 | `summary.json` → `fe.ariaLabel` | 35 |
| DM-FE-03 | `fe-testids.json` → `playwrightConfigPresent` + có `e2e/` | config có, `e2e/` không |
| DM-FE-04/07/08 | grep như Mục 3 | chưa có |
| DM-APP-01/02 | `summary.json` → `app.identifier`, `app.semantics`; `app-semantics.json` → `byModule[…]` | 0 · 0 |
| DM-APP-05 | `app-routes.json` → `deepLinks.destinationsByFile` (file `deep_link.dart`) có route dgas | 5 route, không có dgas |
| DM-APP-03/04/06/07/08 | grep / `git ls-tree` / `git rev-list` trên `origin/tuanvv` như Mục 4 | chưa có · 0 test · lệch 194 |
| Jira | `summary.json` → `jira.perRepo.app` | 0 |
| DM-SEC-* | `git ls-tree` / grep tên khoá (không in giá trị) | còn đủ |

Mỗi lần quét, BA ghi bảng mốc mới vào cuối file này và báo đội dev mục nào đã đạt.
