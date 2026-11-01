---
paths:
  - "design-system/**"
  - ".claude/skills/figma-component/**"
  - "_scripts/ds-*.py"
---

# DS stale — component lệch khi con lồng trong nó hoặc foundation nó dùng đổi

> Rule cho DS v2 (DEC-292, DEC-302). Áp cho mọi lượt sửa `design-system/foundations/*.md`, `tokens.*`,
> `design-system/components/**` và cho `/figma-component`. Máy: `_scripts/ds-deps.py` + hook `ds-stale.sh` + KG.

## 1. Khi nào một component bị stale

Component A **stale** khi một trong ba điều sau đúng:

| # | Điều kiện | Ví dụ |
|---|---|---|
| 1 | Một con A dùng trực tiếp (`uses`) có phiên bản khác lúc A được dựng | Avatar đổi → Header navigation |
| 2 | Một mục foundation A dùng có phiên bản khác lúc A được dựng | Mục 10 Chuyển động đổi → Buttons, Form controls |
| 3 | Một con của A (ở bất kỳ tầng nào) đang stale | Avatar đổi → Button stale → Header navigation stale "qua button" |

"Lúc A được dựng" = mốc `built` của A trong `design-system/components/_deps.json` (phiên bản từng con + từng mục foundation).
Mốc chỉ đổi khi chạy `ds-deps.py synced <A>`, không tự đổi.

## 2. Phiên bản

| Thứ | Phiên bản = sha1 của |
|---|---|
| Component | `_work/<slug>` (answers brainstorm + css + values) nếu có, không thì file md (bỏ dòng `updated`/`status`/`status_prev`) |
| Mục foundation | Mục `## N.` tương ứng trong `design-system/foundations/*.md` (cột "Ở đâu" của bảng trạng thái ở `README.md`) + `icon.md` (mục icon) + các dòng `tokens.css` có tiền tố của mục (`FPREFIX` trong script) |

Sửa mục Màu chỉ đánh component dùng màu, không đánh cả bộ.

## 3. Component dùng foundation nào

Máy dò (`ds-deps.py scan`), không khai tay: các `var(--…)` trong CSS/preview của `_work/<slug>/page.json` và token viết
trong md (`` `space/3xl` ``, `` `radius/overlay` ``). Biến component (`--tooltip-bg`) được dò ngược qua `tokens.css`
tới biến foundation. Có nhắc `icons.md`/Lucide thì tính là dùng icon. Kết quả ghi vào `components.<slug>.foundations`.

Trang `_work` dùng biến cục bộ mã màu cứng (`--fg:#171717`) **không gắn foundation nào**, nên foundation đổi không lan tới
chúng. `check` in danh sách này mỗi lần chạy. Sửa bằng cách ráp lại preview từ kho (`ds-kit.py`), không khai tay.

## 4. Mỗi lần check đều tra KG

`python3 _scripts/ds-deps.py check [--write] [--backlog]`:

1. `scan` cập nhật sổ, rồi build lại KG nếu `graph.json` cũ hơn `_deps.json`.
2. So mốc `built` với phiên bản hiện tại → các **seed** lệch (`ds:<con>`, `ds-f:<mục>`).
3. Mỗi seed → `kg-query impact <seed> --depth 8 --all`: mọi `ds_component` phụ thuộc, kèm đường đi (edge
   `USES_COMPONENT`, `USES_FOUNDATION`). Kết quả in dòng `KG: …` dưới mỗi component stale.
4. Đối chiếu KG với tính trực tiếp từ `_deps.json`: KG thiếu thì in `ℹ KG thiếu …` và vẫn đánh theo sổ. KG lỗi thì
   dùng thẳng sổ và báo 1 dòng (`kg-usage.md`: KG-ERROR → flow cũ).

`ds-deps.py impact <slug>` / `impact f:<mục>` = xem trước ai bị ảnh hưởng **trước khi** sửa.

## 5. Đánh stale và gỡ

| Bước | Lệnh / ai | Kết quả |
|---|---|---|
| Đánh | `check --write --backlog` (hook `ds-stale.sh` tự chạy trên `main` sau mỗi Write/Edit vùng DS v2) | md `status: stale` + `status_prev: <cũ>` · `_work/<slug>/page.json` `dsStale` + ⚠ trong `page.kit` · dòng `_workspace/staleness.md` + changelog · task `Sync <slug> (DS stale)` |
| Sync | Claude khi làm task: `ds-kit.py <slug>`, dựng lại preview/Figma, chạy lại bước 3 / review | — |
| Gỡ | `ds-deps.py synced <slug>` | mốc `built` mới · status về `status_prev` · bỏ `dsStale` · task tự đóng (Xong khi `!grep:…:^status: stale`) |
| Component mới | `ds-deps.py synced <slug>` khi dựng xong (hoặc `baseline`) | có mốc để so lần sau |

Sync **từ dưới lên**: con trước, cha sau. Cha stale "qua X" chỉ sync sau khi X đã `synced`, không thì sẽ stale lại.

## Anti-patterns

- ❌ Sửa tay `status: stale` → `draft`/`approved` để tắt cảnh báo. Gỡ chỉ bằng `synced`.
- ❌ Chạy `synced` khi chưa dựng lại preview/Figma theo bản con/foundation mới.
- ❌ Khai tay `foundations` trong `_deps.json`. `scan` ghi đè; sửa nguồn (CSS/md) cho đúng token.
- ❌ Bỏ qua dòng `ℹ không gắn token foundation`. Component đó đang lệch foundation mà máy không thấy.
- ❌ `baseline` toàn bộ để xoá stale. `baseline` không tham số chỉ ghi mốc cho component **chưa có mốc**.

## Tóm tắt 1 dòng

> **Con (bắc cầu) hoặc foundation đổi so với mốc `built` → component `stale` · mỗi `check` tra `kg impact` lấy đường lan ·
> gỡ chỉ bằng `ds-deps.py synced <slug>` sau khi dựng lại, từ dưới lên.**
