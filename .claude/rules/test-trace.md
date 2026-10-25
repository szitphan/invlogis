---
paths:
  - "docs/**/test/**"
  - "docs/_reverse/**"
  - "qa/**"
  - ".claude/skills/test-checklist/**"
  - ".claude/skills/test-cases/**"
  - ".claude/skills/playwright-gen/**"
  - ".claude/skills/api-test/**"
  - ".claude/skills/maestro-gen/**"
  - ".claude/skills/reverse-doc/**"
  - ".claude/scripts/*gen*.mjs"
  - ".claude/scripts/bruno-runner.mjs"
---

# Test Trace — từ bộ tái lập tới kết quả chạy DEV, mỗi dòng truy được về nguồn

> Rule chung cho các skill tái lập, viết US/AC, checklist, test case, máy sinh test và phần chạy `qa/`.
> Mục đích: một test rớt thì biết ngay vì sao — lỗi app, lệch tài liệu hay thiếu dữ liệu — và biết đáp án
> của test lấy từ đâu. Định dạng ở đây là hợp đồng giữa skill, máy sinh test và KG; đổi thì đổi ở đây trước.

## 1. Luồng cho feature cũ

```
/reverse-doc  →  /userstory + /ac  →  /test-checklist  →  /test-cases  →  máy sinh test  →  chạy DEV
 (bộ tái lập)     (sinh thẳng từ        (CHK, kênh,        (TC, Target,     web · api · mob
                   bộ tái lập)           nhãn đáp án)       Role, Data)
```

- Mỗi feature 1 worktree `feat/<slug>` (`worktree.md`). Bộ tái lập ghi ở `docs/_reverse/<slug>/`, mọi thứ
  test ghi ở `docs/<slug>/test/`. Cả hai nằm trong vùng ghi của worktree đó.
- Test chạy từ nhánh trong lúc chờ. Land lên `main` khi SRS mới của feature chuẩn hoá xong.
- US/AC không đợi SRS mới: `/userstory`, `/ac` đọc bộ tái lập khi chưa có `srs/{feature}-spec.md`, mỗi
  story/AC ghi `Nguồn: bộ tái lập`. Khi SRS mới ra, chạy lại để đổi nguồn.
- Feature mới (đã có SRS) đi luồng cũ: SRS → US/AC → checklist → test case. Các mục dưới vẫn áp.

## 2. Mã và tham chiếu

| Loại | Dạng | Ghi chú |
|---|---|---|
| Yêu cầu SRS | `FR\|BR\|NFR\|E-{feature}-NNN` | như `naming-conventions.md` |
| Yêu cầu bộ tái lập mới | `FR-{feature}-R001` … | chữ **R** để không trùng SRS mới; 4 bộ tái lập cũ giữ mã đang có |
| Mã AC của dev | `AC:FU-FD-AC-002` | chỉ dùng trong danh sách Ref; lấy từ bộ tái lập (`reverse-sources.md`), không tự đặt |
| UC SRS cũ | `UC06.00.03@M` (app) · `UC12.03.01@W` (web) | khi cần trích bản cũ |
| Checklist | `CHK-{feature}-NNN` | cấp từ `next_chk_id`, không dùng lại |

Ref của 1 dòng checklist/TC có thể trộn các loại trên, phân cách `, `. Mọi mã trong Ref phải tìm thấy trong
SRS, bộ tái lập hoặc US/AC của feature — không thấy là ref ma, validator chặn.

> Lưu ý: KG chưa index mã có chữ R (`FR-{f}-R001`) và tham chiếu `AC:` — truy vấn coverage sẽ bỏ sót chúng
> cho tới khi engine KG được cập nhật (theo dõi trong backlog).

## 3. Dòng checklist

```
[P] [Auto] CHK-{feature}-NNN → {Ref, Ref…|—} · {nội dung} @web|@mob|@api [đáp án: {nguồn}]
```

- Phần đầu tới dấu `·` giữ đúng như cũ — KG và parser cũ đọc được.
- Đuôi đặt **sau** nội dung: kênh trước, nhãn đáp án sau. Thiếu kênh = `@web` (tương thích file cũ).
- 1 dòng = 1 kênh. Cùng oracle trên app và API = 2 dòng.
- `{nguồn}` ∈ `SRS` · `CHG-xx` · `tái lập` · `code FU-FD-AC-NNN` · `UC cũ`. Bắt buộc khi nguồn không phải SRS
  mới đã duyệt.

Ví dụ:
`[1] [Yes] CHK-fuel-issuing-004 → FR-fuel-issuing-R003, AC:FU-FD-AC-002 · Tạo phiếu tại cây nội bộ trả về mã iGAS @api [đáp án: code FU-FD-AC-002]`

## 4. Test case

Giữ khối `---` và field `**Key:**` của `/test-cases`. Thêm 3 field tuỳ chọn, đặt ngay sau `**Auto:**`:

| Field | Giá trị | Engine làm gì |
|---|---|---|
| `**Target:**` | `web` · `mob` · `api` | chọn máy sinh (Mục 5); thiếu = `web` |
| `**Role:**` | khoá trong `qa/config/roles.json` | đăng nhập sẵn theo vai |
| `**Data:**` | tên dữ liệu tiền đề, phân cách `, ` | gọi hook dựng dữ liệu / đọc testdata có tên |

- Preconditions chỉ gồm dòng `ROLE: x` / `DATA: y` hoặc `—` thì **không** phải setup-required — TC chạy được ngay.
- Step chuẩn bị (mở trang, nhập field) có `**Expected:** —`. Không có step chỉ "quan sát" — phần kiểm gắn
  vào step hành động cuối.
- Mật khẩu, khoá, tài khoản thật ghi `ENV: QA_<ROLE>_PASS`, không bao giờ ghi giá trị.

## 5. Nơi sinh test và kết quả

| Kênh | Máy sinh | Thư mục |
|---|---|---|
| web | `/playwright-gen` | `docs/{feature}/test/e2e/` |
| api | `/api-test` + `bruno-runner` | `docs/{feature}/test/api/bruno-api/` (OpenCollection YAML như `transport-erp/bruno`; bảng API bên thứ 3 của `/api-test` giữ `test/api/bruno/`) |
| mob | `/maestro-gen` | `docs/{feature}/test/mobile/maestro/flows/*.yaml`, subflow chung ở `qa/mobile/subflows/` |

Phần chạy dùng chung ở `qa/` (sửa trên `main`): `qa/config/envs.json` (dev/sit/local, không bí mật),
`qa/config/roles.json` (vai → tên biến môi trường), `qa/.env.example` (chỉ tên biến), `qa/.env` (gitignore).

Kết quả chuẩn hoá: `docs/{feature}/test/results/latest.json` = mảng
`{chk, target, status, env, build, at, note}`.

| status | Nghĩa | Màu |
|---|---|---|
| `PASS` | đạt | ✅ |
| `FAIL_APP` | nghi lỗi app — đáp án là `SRS`, `CHG-xx` hoặc `code …` mà app làm khác | 🔴 |
| `FAIL_DATA` | thiếu hoặc sai dữ liệu test | 🟡 |
| `FAIL_OUTDATE` | test cũ so với tài liệu/màn hiện tại | 🟠 |
| `FAIL_DOC` | nghi lệch tài liệu — test rớt và nhãn đáp án là `UC cũ` hoặc `tái lập` chưa chốt | 🟣 |
| `PENDING` | chưa chạy được (thiếu môi trường, dựng state, thiết bị) | ⏳ |

## 6. Đáp án lấy từ đâu

Khi các nguồn nói khác nhau, nguồn trên thắng:

1. SRS mới đã duyệt
2. CHG / DEC đã chốt (kể cả OQ đã đóng)
3. Bộ tái lập
4. UC SRS cũ
5. Quy tắc chung cũ

- `E-common` (mã lỗi chung) thắng câu chữ riêng của từng feature khi trùng tình huống.
- Chỗ **chưa chốt**: đáp án tạm theo hành vi code (AC của dev), nhãn `[đáp án: code FU-FD-AC-002]`, Ref có
  `AC:FU-FD-AC-002`. Tài liệu dev chỉ cho biết code đang làm gì — không phải yêu cầu của khách.
- BA chốt khác code → đổi đáp án + nhãn sang nguồn mới (`SRS`/`CHG-xx`); test rớt lúc đó là `FAIL_APP` → CR cho dev.
- Bộ tái lập lệch nguồn đối chiếu (docs dev, SOP, quyết định) mà chưa chốt → Conflict/OQ trong
  `docs/_reverse/{feature}/reverse-gaps.md` trích cả hai nguồn (`/reverse-doc`).

## 7. Test rớt thì chuyển đi đâu

| Loại | Đi đâu | Kèm gì |
|---|---|---|
| Nghi lỗi app (`FAIL_APP`) | ticket Jira cho dev | CHK, FR/Ref, ảnh, log, env + build |
| Nghi lệch tài liệu (`FAIL_DOC`) | OQ trong doc BA (reverse-gaps hoặc doc feature) | CHK, nhãn đáp án, hành vi thấy được |
| Nghi dữ liệu (`FAIL_DATA`) | QC tự xử (dựng lại dữ liệu, sửa testdata) | — |

`FAIL_OUTDATE` → chạy lại `/test-checklist` / `/test-cases` theo tài liệu mới. Không tự sửa đáp án cho test qua.

## 8. Bí mật

- Không ghi mật khẩu, khoá API, khoá simulator, JWT secret vào bất kỳ file nào trong vault — kể cả testdata,
  kết quả chạy, log đính kèm. Chỉ ghi tên biến môi trường.
- Địa chỉ host DEV công khai được ghi trong file cấu hình mẫu.
- Log/ảnh đưa vào ticket phải che token và dữ liệu cá nhân thật.

## Anti-patterns

- ❌ Lấy tài liệu dev làm đáp án mà không gắn nhãn `[đáp án: code …]`.
- ❌ Sửa đáp án cho test qua khi chưa có quyết định BA.
- ❌ Gộp 2 kênh vào 1 dòng checklist.
- ❌ Đặt mã bộ tái lập mới không có chữ R, hoặc dùng lại mã đã cấp.
- ❌ Test rớt mà ghi chung chung "FAIL" — phải là một trong các status Mục 5.

## Tóm tắt 1 dòng

> **Tái lập → US/AC → checklist (kênh + nhãn đáp án) → test case (Target/Role/Data) → máy sinh → chạy DEV
> trong worktree `feat/<slug>` · đáp án: SRS > CHG > tái lập > UC cũ > quy tắc cũ, chưa chốt tạm theo code có
> nhãn · rớt: app → Jira, tài liệu → OQ, dữ liệu → QC · không ghi bí mật.**
