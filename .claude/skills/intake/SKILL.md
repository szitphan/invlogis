---
name: intake
description: Dùng khi khách gửi tài liệu gốc (docx, pdf, xlsx, pptx, ảnh chụp/scan) cần chuyển sang .md đủ nội dung + ảnh, đặt tên chuẩn và xếp vào docs-input/ — kể cả khi đó là bản cập nhật của tài liệu cũ (báo diff trước rồi mới ghi đè). `/intake [<file|thư mục>...]`, không tham số = quét file mới trong docs-input/.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, AskUserQuestion
user-invocable: true
argument-hint: "[<đường dẫn file hoặc thư mục> ...] (trống = quét docs-input/)"
---

# /intake — nạp tài liệu khách vào docs-input

## Goal

Biến 1 hoặc nhiều tài liệu gốc thành **bản Markdown đọc được, không thiếu chữ nào** (kèm ảnh, bản gốc),
đặt tên + xếp đúng nhóm trong `docs-input/`, để mọi skill sau (`/brainstorm`, `/srs`, `/discover`...)
đọc nó thay cho file nhị phân. Nếu tài liệu là **phiên bản mới của tài liệu đã có**: so 2 bản, báo
thay đổi nghiệp vụ cho user, user đồng ý thì ghi đè (giữ mã SRC) và lưu báo cáo thay đổi.

Vì sao quan trọng: docs-input là nguồn sự thật cho cả dự án. Bản .md mất 1 dòng hạn mức, 1 hàng bảng
phí hay số thứ tự mục ("xem mục 3.1.2") thì mọi tài liệu phía sau sai theo mà không ai biết. Nên ở đây
**đủ quan trọng hơn đẹp**.

## Bố cục đầu ra

```
docs-input/{nhóm}/{slug}/
├── {slug}.md             ← nội dung đầy đủ, H1 = tiêu đề gốc, dòng "> Nguồn:" trỏ bản gốc
├── images/               ← ảnh nhúng, ảnh trang scan, ảnh xem trước trang có sơ đồ (nếu có)
└── source/
    ├── {slug}.ext        ← bản gốc hiện hành (+ file đính kèm tách ra: {slug}-dinh-kem-NN.ext)
    └── cu/               ← bản gốc các phiên bản trước: {slug}-{ngày nhận}.ext (không xoá)
docs-input/_changes/{YYYY-MM-DD}-{slug}.md   ← chỉ khi là bản cập nhật: báo cáo thay đổi
```

- Nhóm = thư mục cấp 1 đang có (`sop`, `tich-hop`, `chung-tu-mau`, `du-lieu-mau`, `danh-muc`,
  `ui-common`, `srs-cu`) — danh sách chuẩn ở `GROUPS` trong `_scripts/intake-sync.py`. Không hợp nhóm
  nào → hỏi user, chốt nhóm mới thì thêm vào `GROUPS` (L2) để sổ nguồn hiển thị đúng tên nhóm.
- Slug: kebab-case ASCII không dấu, ≤50 ký tự, theo **chủ đề nội dung**.
  * Tài liệu một lần (chứng từ, công văn, biên bản, dữ liệu mẫu): thêm hậu tố ngày của tài liệu
    `-YYYY-MM-DD` (ngày ghi trong tài liệu/tên file, vd "Sep 18 2026" → `2026-09-18`; không có thì
    ngày nhận).
  * Tài liệu sống, sẽ có bản sau (SOP, quy trình, giải pháp, danh mục): **không** gắn ngày — ngày
    phiên bản nằm trong dòng `> Phiên bản:` của file. Tên cũ đã có ngày thì giữ, chỉ bỏ ngày khi đổi tên.
- Sổ nguồn `docs-input/README.md` và backlog do `_scripts/intake-sync.py` tự cập nhật: file thô biến
  khỏi chỗ cũ mà bản sao nằm trong `source/` của 1 tài liệu → dòng sổ tự trỏ sang `.md`; tài liệu đó
  đã có mã SRC → gộp vào mã cũ và đóng task feed trùng; file .md đổi chỗ mà **nội dung giữ nguyên** →
  dòng sổ đi theo. Vì vậy: **di chuyển** (mv) file thô vào `source/`, đừng copy rồi để lại; và khi
  vừa đổi chỗ vừa đổi nội dung thì làm 2 bước, chạy script ở giữa (xem bước 8).

## Constraints

### Hard rules

- **Đủ nội dung, không tóm tắt, không diễn đạt lại.** Giữ nguyên câu chữ, thứ tự, số thứ tự mục,
  mọi con số, mã, tên riêng, đơn vị, ghi chú chân trang có nghĩa, comment trong file. Được sửa: cấp
  heading, xuống dòng gãy của PDF, bảng vỡ, lỗi dấu do OCR. Không đọc được chữ trong ảnh → ghi
  `[không đọc rõ]`, KHÔNG đoán.
- **`verify.py` phải qua** trước khi trình user — hoặc mỗi dòng còn bị báo thiếu có lý do cụ thể
  (header/footer lặp đã gộp 1 lần, số trang). Đưa con số độ phủ vào L1.
- **Trang scan / chứng từ dạng ảnh phải được NHÌN** — đó là nội dung chính, OCR thô không đủ: mở
  bằng Read, viết lại chữ. **Ảnh nhúng** (minh họa, sơ đồ, ảnh chụp màn hình trong tài liệu có chữ)
  thì chỉ cần trích vào `images/` và chèn link đúng vị trí như các tài liệu cũ — KHÔNG Read, KHÔNG
  dựng lại mermaid (user chốt 2026-10-02). Ngoại lệ: chữ nằm trong shape/SmartArt/text box (không
  phải ảnh) chỉ có trong `_raw.txt` → vẫn chép vào .md, vì không ảnh nào giữ chữ đó.
- **File đính kèm trùng tài liệu đã có: vẫn chép đủ nội dung** vào mục `## Đính kèm`, kèm dòng
  `> Trùng với …` (user đã chốt 2026-10-02: tài liệu phải tự đủ, không bắt người đọc nhảy file).
- **Approval gate** (@.claude/rules/approval-gate.md): làm mọi thứ trong `docs-input/.staging/` trước;
  chỉ ghi vào chỗ thật sau L1. Bản cập nhật → báo thay đổi (đóng vai L2) và chờ user đồng ý rồi mới
  ghi đè. Sửa link trong `docs/` → L2. L1 viết bằng lời nghiệp vụ theo @.claude/rules/ba-conventions.md Mục 5.
- **Không tự quyết "đây là bản mới của X"** và **không tự đổi tên tài liệu cũ** — `match.py` chỉ gợi
  ý; luôn hỏi user.
- **Không xoá bản gốc cũ** — chuyển vào `source/cu/`. docs-input không phải lúc nào cũng có git, và
  bản gốc cũ là thứ duy nhất để diff lại khi cần.
- **Không tự hạ ✅ trong sổ, không sửa cột tự động** của README (@.claude/rules/backlog.md). Cột
  "Ghi chú" sửa được — ghi 1 câu về cách chuyển (vd "docx 14 trang, 9 ảnh nhúng; 2 trang scan đã đọc lại").
- **Không sửa nội dung tài liệu nghiệp vụ trong `docs/`** ngoài việc đổi đường dẫn khi đổi tên. Đối
  chiếu nội dung mới vào research/brainstorm là việc của lượt sau (thêm task backlog, bước 9).

### Pitfalls

- Word: số mục tự động (I., II.1., 3.1.1, a)) — `convert.py` đã dựng lại và chuyển đề mục thành heading
  theo cấp mục lục Word (`outlineLvl`). Đề mục không gắn cấp mục lục mà chỉ in đậm 1 phần sẽ còn là
  đoạn thường — sửa thành heading theo số mục của nó (vd `3.4.4.` cùng cấp `3.4.3.`).
- Ảnh EMF nhỏ (~10 KB) trong Word thường là **icon của file nhúng**, không phải sơ đồ — script đã đổi
  thành file đính kèm; EMF còn sót lại mới là hình vẽ thật.
- Bản nháp Word mất chữ trong text box/shape/SmartArt và ảnh EMF/WMF (sơ đồ vẽ trong Word). Cảnh báo
  trong `_report.json` sẽ nói; chữ đó có trong `_raw.txt` — chép chữ thô vào .md tại chỗ hình (không cần
  mermaid), không bỏ qua.
- PDF có lớp chữ vẫn có thể rơi dòng hoặc vỡ ô bảng (vd nhãn song ngữ trên biểu mẫu) — dựng lại bảng
  theo ảnh trang; `verify.py` bắt chữ rơi. Sổ nguồn ghi "bản scan" chưa chắc đúng — xem `_report.json`.
- Excel: vùng gộp ô làm tiêu đề nhiều tầng bị lệch; sheet ẩn; ô công thức (bảng là giá trị đã tính).
  Bảng rất dài vẫn giữ đủ — không cắt bớt dòng "cho gọn".
- OCR Vision đọc tiếng Việt khá nhưng hay sai dấu và tách bảng thành dòng rời — luôn đối chiếu ảnh.
- Tài liệu song ngữ giữ cả 2 ngôn ngữ, không dịch. Ngày tháng giữ đúng định dạng in trên giấy.
- Diff giữa 2 bản: khác biệt do **cách chuyển** (bản cũ chuyển tay, bản mới chuyển bằng script; bản
  cũ không có heading) không phải thay đổi nghiệp vụ. Khi `diff.py` không ghép được mục (bản cũ thiếu
  heading), so theo đoạn/ý và nói rõ trong báo cáo. Bản gốc cũ có trong `source/` hoặc `source/cu/`
  thì chuyển lại bản cũ bằng `convert.py` để so cùng một cách chuyển.

## Approach

Script nằm ở `.claude/skills/intake/scripts/` (gọi tắt `$S`). Mỗi tài liệu 1 thư mục staging
`docs-input/.staging/{slug-tạm}/`.

### 1. Xác định đầu vào

- Có tham số → từng file/thư mục được chỉ (có thể ngoài repo, vd `~/Downloads/...`).
- Không tham số → quét: file không phải `.md` ở gốc `docs-input/`; dòng sổ nhóm "Chưa phân loại";
  file docx/pdf/xlsx/ảnh trong thư mục nhóm mà chưa có `.md` đi kèm (vd `chung-tu-mau/*.pdf` cũ).
  Liệt kê và hỏi user xử lý những file nào. Không có gì → báo "docs-input không có tài liệu mới".
- File `.md` khách gửi sẵn → bỏ bước chuyển, vẫn làm đặt tên / dò bản cũ / xếp chỗ.
- File trùng y hệt (cùng hash) với bản gốc đã có trong 1 `source/` → báo trùng, bỏ qua.

### 2. Chuyển thô

```bash
python3 -c "import pymupdf, pymupdf4llm, mammoth, markdownify, openpyxl, pptx, xlrd, olefile" 2>/dev/null \
  || pip3 install -q -r $S/requirements.txt
python3 $S/convert.py "<file>" --out docs-input/.staging/<slug-tạm> --slug <slug-tạm>
```

Hỗ trợ: docx/doc (dựng lại số mục tự động, tách file nhúng PDF/Excel/Word), pdf (có lớp chữ hoặc
scan → OCR), xlsx/xlsm/xls/csv, pptx, ảnh png/jpg/heic/tiff. Output in `_report.json`: thống kê +
**cảnh báo** — đọc kỹ, mỗi cảnh báo là 1 việc ở bước 3. Thoát mã 3 = thiếu thư viện (cài theo lệnh
in ra); mã 2 = định dạng chưa hỗ trợ → báo user.

### 3. Hoàn thiện bản .md (phần việc của Claude)

Đọc toàn bộ bản nháp, rồi:
1. **Ảnh**:
   - Trang scan / ảnh chứng từ (PDF scan, ảnh chụp giấy tờ là chính tài liệu): Read từng ảnh trang,
     viết lại chữ đúng như ảnh (sửa dấu OCR), dựng lại bảng/biểu mẫu dạng bảng Markdown hoặc
     `Nhãn: giá trị`; mô tả phần không phải chữ (con dấu, chữ ký, QR, logo) trong 1 dòng `_[…]_`.
     Giữ ảnh gốc nhúng phía trên để đối chiếu. Bỏ comment "OCR thô".
   - Ảnh nhúng trong tài liệu (minh họa, sơ đồ, ảnh chụp màn hình): chỉ kiểm ảnh đã có trong
     `images/` và link `![…](images/…)` nằm đúng vị trí; alt lấy chú thích/tên ảnh có sẵn. Không
     Read ảnh, không dựng mermaid.
   - Chữ trong shape/SmartArt/text box/EMF chỉ có trong `_raw.txt`: chép nguyên chữ vào .md ngay
     chỗ hình (danh sách theo thứ tự đọc), kèm ảnh xem trước nếu script có xuất.
2. **Cấu trúc** — đúng 1 H1 (tiêu đề), bỏ đoạn tiêu đề lặp ngay dưới H1, heading đúng cấp theo
   đánh số của tài liệu, nối dòng gãy, bỏ số trang; header/footer có nghĩa (tên công ty, mã tài liệu,
   phiên bản, "Nội bộ") gộp 1 lần vào dòng `> Thông tin trang: …` dưới dòng Nguồn. PDF nhiều trang có
   lớp chữ: bỏ heading "Trang N" nếu nội dung chảy liên tục, giữ nếu mỗi trang là 1 chứng từ riêng.
   Mục lục của Word: giữ danh sách tên mục, bỏ số trang.
3. **Ghi chú/comment trong bản gốc** (Word comment, ghi chú ô Excel, ghi chú slide) → giữ ở cuối
   mục liên quan hoặc mục `## Ghi chú trong bản gốc`.
4. **File đính kèm nhúng** (Word nhúng PDF/Excel/Word — hiện dưới dạng icon): script đã tách vào
   `source/{slug}-dinh-kem-NN.ext`, chuyển nội dung vào mục `## Đính kèm` cuối tài liệu, thay icon
   bằng dòng 📎, và tự dò trùng với docs-input (ghi `> Trùng với …` — y hệt theo hash, hoặc gần như
   trùng theo nội dung). Việc của Claude: đặt tiêu đề thật cho từng `### Đính kèm NN — …` theo nội
   dung (vd "Danh sách hàng đủ điều kiện qua KVGS — mẫu mã vạch hàng nhập"), sửa OCR như ý 1; với
   "gần như trùng" thì nêu khác ở đâu (vd "bản đính kèm nhiều hơn 3 dòng kho CFS") trong dòng Trùng với.

### 4. Kiểm độ đủ

```bash
python3 $S/verify.py docs-input/.staging/<slug-tạm>
```

Còn thiếu → bổ sung vào .md rồi chạy lại. Lặp tới khi ✅, hoặc mỗi dòng còn lại có lý do (ghi vào
ghi chú cho L1, không ghi vào tài liệu). Phần "Chữ OCR (tham khảo)" không làm fail — nhưng rà các dòng
OCR ít khớp: là chữ đã sửa theo ảnh (bình thường) hay bị bỏ sót (bổ sung). Kiểm thêm bằng mắt: số
bảng, số ảnh, số đính kèm trong `_report.json` khớp với .md.

### 5. Đặt tên, chọn nhóm

Đề xuất `{nhóm}/{slug}` theo mục "Bố cục đầu ra". Đổi tên thư mục staging + file .md + file trong
`source/` theo slug chốt, sửa link `source/…` trong dòng Nguồn.

### 6. Dò bản cũ

```bash
python3 $S/match.py docs-input/.staging/<slug>/<slug>.md
```

Có ứng viên "rất có thể" / "liên quan" → hỏi user (AskUserQuestion): **bản cập nhật của X** /
**tài liệu mới, liên quan X** (ghi vào cột Ghi chú) / **tài liệu mới độc lập**. Nhiều tài liệu
trong 1 lượt thì gom vào 1 câu hỏi.

Là bản cập nhật:
- **Giữ đường dẫn cũ** là mặc định (mã SRC + mọi link không đổi).
- **Phạm vi/tiêu đề đổi rõ** (vd SOP chỉ container → SOP giao nhận mọi loại hàng) → hỏi user có đổi
  tên không, đề xuất slug mới theo chủ đề mới (không gắn ngày). Hỏi cùng câu "bản cập nhật của X".
- **Bản cũ là file đơn** (`{nhóm}/{x}.md`, chưa có thư mục) → phải chuyển vào thư mục
  `{nhóm}/{slug}/{slug}.md` để có chỗ cho `source/` (slug = tên cũ, hoặc tên mới nếu user chọn đổi).

So 2 bản:

```bash
python3 $S/diff.py <bản cũ .md> docs-input/.staging/<slug>/<slug>.md
```

Viết báo cáo `docs-input/.staging/_changes/{hôm nay}-{slug-cuối}.md` (ghi thật ở bước 8):

```markdown
# Thay đổi: {tiêu đề tài liệu}

> Bản cũ: nhận {ngày} (`{tên file gốc cũ}`) · Bản mới: nhận {hôm nay} (`{tên file gốc mới}`) · Tài liệu: [{slug}.md](../{nhóm}/{slug}/{slug}.md)

## Tóm tắt nghiệp vụ
{3-10 gạch đầu dòng, xếp theo mức ảnh hưởng: phạm vi/quy tắc/hạn mức/vai trò/luồng đổi gì, từ → thành.
Đánh dấu ⚠ chỗ mâu thuẫn với SOP khác hoặc quyết định đã ghi trong brainstorm/research, và chỗ cần
hỏi lại khách (vd ghi chú "không cần" bị bỏ mà không rõ ý).}

## Đổi số mục
{chỉ khi số mục đổi: bảng mục cũ → mục mới, để tài liệu đang trích "mục 3" sửa theo}

## Tài liệu đang dùng nguồn này
{cột "Dùng ở" của sổ + grep đường dẫn trong docs/ — mỗi dòng: file · phần nào có thể bị ảnh hưởng}

## Chi tiết
{output diff.py, hoặc so theo ý khi diff.py không ghép được mục}
```

Tóm tắt nghiệp vụ là phần user đọc — viết bằng ngôn ngữ nghiệp vụ, không phải "dòng 12 đổi". Chỉ báo
khác biệt định dạng nếu nó che mất thay đổi thật.

### 7. Trình user

- **Bản cập nhật:** in Tóm tắt nghiệp vụ + bảng Tổng quan thay đổi + danh sách tài liệu bị ảnh hưởng
  trong chat, hỏi "Cập nhật bản mới vào `{đường dẫn}`? (Y / sửa / n)". Có đổi tên → kèm diff các
  dòng link sẽ sửa trong `docs/` (L2).
- **L1** cho cả lượt (prose nghiệp vụ, Mục 5 ba-conventions): mỗi tài liệu 1-2 dòng — tên mới, nhóm,
  nội dung (số mục/bảng/ảnh/đính kèm, trang scan đã đọc lại), độ phủ verify, việc gì còn chưa chắc.

### 8. Ghi

Sau khi user đồng ý. Trước Edit/Write file trong `docs/`, set `CLAUDE_SKILL_NAME=/intake`,
`CLAUDE_CHANGELOG_NOTE`, `CLAUDE_CHANGELOG_AUTHOR` (@.claude/rules/changelog.md).

**Tài liệu mới:**
1. `mv` staging → `docs-input/{nhóm}/{slug}/` (bỏ `_raw.txt`, `_raw_ocr.txt`, `_report.json`).
2. File thô nằm trong `docs-input/` → `mv` vào `source/{slug}.ext` (đè lên bản sao convert đã tạo).
   File thô ngoài repo → giữ bản sao convert đã tạo.

**Bản cập nhật** — làm đúng thứ tự, vì script nhận "đổi chỗ" nhờ nội dung giữ nguyên:
1. *(chỉ khi đổi tên hoặc bản cũ là file đơn)* `mv` bản cũ **nguyên nội dung** sang
   `{nhóm}/{slug}/{slug}.md` (cùng `images/`, `source/` nếu có; sửa link ảnh tương đối nếu đổi cấp
   thư mục — sửa link làm đổi nội dung, nên làm SAU bước 2). Chạy `python3 _scripts/intake-sync.py`
   → phải thấy `↪ đổi chỗ nguồn SRC-xx`. Sửa đường dẫn cũ trong `docs/` (grep) theo diff đã duyệt.
2. Bản gốc cũ trong `source/` → chuyển sang `source/cu/` giữ nguyên tên file (cả file đính kèm cũ); chỉ khi
   trùng tên với file đã có trong `source/cu/` mới thêm `-{ngày nhận cũ}` trước đuôi file.
3. Ghi bản mới: thay `{slug}.md`, chép `source/` + `images/` mới vào (giữ ảnh cũ đang được `docs/`
   trích: grep `docs-input/{nhóm}/{slug}/images/`), chuyển báo cáo vào `docs-input/_changes/`. Dưới
   dòng `> Nguồn:` thêm dòng `> Phiên bản: {ngày tài liệu mới} (nhận {hôm nay}) — thay bản nhận
   {ngày cũ}; xem [thay đổi](../../_changes/{file}).` — giữ các dòng Phiên bản cũ phía dưới.
4. File thô nằm trong `docs-input/` → `mv` vào `source/{slug}.ext`.
5. Chạy `python3 _scripts/intake-sync.py`. Log mong đợi:
   - file thô ở trong docs-input đã có mã SRC riêng → `⤳ SRC-yy … là bản cập nhật của SRC-xx — gộp vào`;
   - file thô từ ngoài repo, đường dẫn không đổi → `không có thay đổi` (đúng — sổ chỉ cập nhật hash).
   Thấy `❌ không thấy file` hoặc `+ nguồn mới` cho file trong `source/` → dừng, kiểm lại thứ tự.

**Cuối cùng:** xoá thư mục staging đã ghi; điền cột "Ghi chú" của dòng sổ (1 câu).

### 9. Báo cáo + bước tiếp

- Tóm tắt từng tài liệu: đường dẫn, mã SRC, nội dung chính 1 câu, trang scan đã đọc lại/chỗ không đọc rõ,
  đính kèm trùng với gì.
- Bản cập nhật: với mỗi tài liệu trong "Tài liệu đang dùng nguồn này", thêm task backlog
  `Rà lại {doc} theo thay đổi {SRC}` với Xong khi `grep:{doc}:_changes/{file báo cáo}` (doc cập nhật
  xong sẽ trích báo cáo thay đổi) — báo 1 dòng "Đã thêm BL-NNN".
- Gợi ý đưa nội dung vào giải pháp (brainstorm/feature đang làm) và chỉ ra chỗ mâu thuẫn với SOP đã
  có — gợi ý thôi, không tự sửa tài liệu nghiệp vụ trong lượt này.

## References

- @.claude/rules/approval-gate.md — L1/L2 trước khi ghi
- @.claude/rules/ba-conventions.md — Mục 5 (L1 bằng lời nghiệp vụ), Mục 2 (không hỏi lại)
- @.claude/rules/backlog.md — sổ nguồn + task tự đóng, điều kiện Xong khi
- @.claude/rules/naming-conventions.md — slug kebab-case ASCII
- @.claude/rules/changelog.md — env trước khi sửa file trong docs/
- `_scripts/intake-sync.py` — đồng bộ sổ nguồn (nhận `source/`, gộp bản cập nhật, bỏ qua `_*`/`.*`)
- `$S/convert.py` (+ `docx_numbering.py`, `ocr.swift`) · `$S/verify.py` · `$S/match.py` · `$S/diff.py`
