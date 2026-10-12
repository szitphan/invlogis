# SaaS Layer — mỗi quy tắc nghiệp vụ mang nhãn tầng, con số đi qua mã tham số

> Rule chung cho MỌI skill viết hoặc sửa quy tắc nghiệp vụ (`/brainstorm`, `/brd`, `/prd-epic`, `/srs`,
> `/usecase`, `/userstory`, `/ac`, `/cr`) và skill sinh code/kiểm code (`/prototype-next`, `/doc-drift`).
> Áp khi `docs/_shared/project-profile.md` mục "Mô hình kinh doanh" ghi sản phẩm bán cho nhiều khách
> (SaaS). Không ghi → bỏ qua rule này, báo 1 dòng.

## 1. Vì sao là gate, không phải lời dặn

Thói quen viết tài liệu là ghi thẳng con số và cách làm của khách đang làm cùng ("dưới 5 triệu thì
tạm ứng"). Dev đọc tài liệu sẽ viết cứng đúng như thế. Khi bán cho khách thứ hai, mỗi điểm cứng thành
sửa code riêng hoặc tách nhánh. Luật ngược thói quen phải có máy chặn (`diagram-correctness.md` Mục 1),
nên rule này đi kèm `_scripts/saas-layer-lint.py`.

## 2. Bốn tầng + nhãn

| Nhãn | Nghĩa | Phần mềm làm thế nào |
|---|---|---|
| `[Lõi]` | Đúng với mọi doanh nghiệp cùng ngành | Viết cứng trong sản phẩm, mọi khách dùng chung |
| `[Cấu hình]` | Cùng quy tắc, mỗi khách khác con số, danh sách, tên gọi, hoặc bật/tắt | Đọc từ tham số theo khách (mã `P-…`), có mặc định |
| `[Gói: {tên gói}]` | Đúng với một nhóm khách | Module bật theo hợp đồng |
| `[Riêng {khách}]` (vd `[Riêng Delta]`) | Chỉ khách này cần | Dữ liệu cấu hình, kết nối riêng hoặc dịch vụ tuỳ chỉnh; không sửa lõi |

Một quy tắc có thể mang 2 nhãn khi cơ chế và con số khác tầng: `[Lõi] [Cấu hình]` (cơ chế lõi, con số
theo khách), `[Gói: Đường sắt] [Cấu hình]`.

## 3. Ba câu hỏi xếp tầng

1. Có ít nhất 2 doanh nghiệp cùng ngành cần đúng quy tắc này không?
2. Viết được quy tắc mà không có con số, tên riêng, tên đối tác của khách không?
3. Khách khác muốn ngược lại thì tắt hoặc đổi được mà không sửa code không?

Có cả 3 → `[Lõi]` · có 1 và 3 nhưng có con số/tên riêng → `[Lõi] [Cấu hình]` · chỉ đúng một nhóm khách →
`[Gói: …]` · không câu nào → `[Riêng {khách}]`. Không chắc → `[Cấu hình]` (đổi lên Lõi dễ hơn rút xuống).

Phân loại chi tiết của dự án + danh sách gói: `docs/_product/saas-core-vs-tenant.md`. Rule này chỉ giữ cơ chế.

## 4. Con số, danh sách, bật/tắt → mã tham số

- Mọi con số chính sách (ngưỡng tiền, số giờ, ca, kỳ chốt, tỷ lệ), danh sách lựa chọn (lý do, loại) và
  tính năng một khách bật một khách tắt → **một dòng** trong `docs/_product/tenant-parameters.md`, mã `P-{slug}`.
- Tài liệu ghi mã kèm giá trị của khách trong ngoặc: "dưới `P-nguong-tam-ung` (Delta: 5.000.000 ₫) thì tạm ứng".
  Dev thấy mã P → đọc từ cấu hình, không viết số vào code.
- Khách từ chối một tính năng → **không xoá khỏi tài liệu**; tạo tham số bật/tắt, giá trị khách = tắt.
- Dữ liệu danh mục thuần (định mức từng địa điểm, bảng giá) là dữ liệu của khách, không cần mã P —
  ghi nhãn `[Riêng {khách}]` hoặc trỏ tới danh mục.
- Chưa có con số → giá trị "chưa chốt (OQ-n)", KHÔNG bịa mặc định sản phẩm.

## 5. Ghi ở đâu

| Tài liệu | Cách ghi |
|---|---|
| Brainstorm Mục 4 | Nhãn tầng ngay sau nhãn nguồn: `- B7 [SOP+] [Gói: Đa chi nhánh] …` |
| SRS bảng FR, BR | Cột "Tầng" |
| User story | Dòng "Tầng:"; `/jira` đẩy thành label |
| CR | Mỗi yêu cầu mới trả lời 3 câu Mục 3 trước khi apply |

## 6. Gate

```bash
python3 _scripts/saas-layer-lint.py <file.md> [...]
```

| Mức | Máy kiểm | Kết quả |
|---|---|---|
| Có nhãn | Dòng tính năng brainstorm, dòng FR/BR thiếu nhãn tầng | FAIL |
| Mã tham số | Mã `P-…` dùng trong tài liệu nhưng không có trong bảng tham số | FAIL |
| Số trần | Dòng `[Lõi]`/`[Cấu hình]` có con số chính sách hoặc tên riêng khách mà không qua mã P | WARN |
| Đúng tầng | Xếp tầng có hợp lý không | **Máy KHÔNG kiểm** — người/AI tự soi theo Mục 3 |

Skill chạy gate trước L1; FAIL thì sửa trước khi trình. Báo cáo in tách 4 mức, không gộp "PASS".

## Tóm tắt 1 dòng

> **Mỗi quy tắc mang nhãn tầng · con số/danh sách/bật-tắt đi qua mã `P-…` trong bảng tham số · khách
> từ chối thì tắt, không xoá · gate `saas-layer-lint.py` chặn trước L1.**
