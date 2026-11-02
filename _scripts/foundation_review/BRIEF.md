# Trang review Foundations theo Untitled — luật chung cho agent

Mục tiêu: mỗi foundation một trang duyệt, cùng khuôn hai trang đã làm (Màu `094ed7ce-45e4-434f-b5f3-5e6b1d012d8c`, Chữ `7cebeed3-cb18-4b27-af8a-dff890d9fb54`):
màn thật → bảng đối chiếu Untitled ↔ mình → bộ đề xuất → các mục cần chọn → chốt. Người duyệt là chủ DS (BA/designer, đọc tiếng Việt), quyết bằng cách bấm trên trang.

## Bạn được làm gì

- CHỈ ghi `_scripts/foundation_review/<slug>.py` (biến `SPEC`). Dựng + kiểm: `python3 _scripts/foundation_review/build.py <slug>`. Lặp tới khi `PASS`, xử lý hết WARN (sửa hoặc có lý do trong báo cáo).
- KHÔNG sửa `kit.py`, `build.py`, `tokens.*`, `design-system/foundations/*`, component, backlog, decisions; KHÔNG publish; KHÔNG chạm Figma. Kit thiếu gì: dùng `css`/`js` của SPEC; lỗi kit thì báo trong kết quả.
- Trang chỉ ĐỀ XUẤT. Không có token nào đổi ở lượt này.

## SPEC

```python
import kit
SPEC = dict(
  slug="spacing", short="phần Khoảng cách",          # short dùng cho tiêu đề "Chốt …"
  title="Foundations · Khoảng cách — đủ token chưa?",
  subtitle="Đối chiếu Untitled UI v8 · chọn từng mục · 01/11/2026",
  lead="html: 2-3 câu, nói trang này giúp quyết gì, kết luận chính, ghi rõ <mark>chưa sửa token nào</mark>",
  kpis=[("11/17", "bậc trùng Untitled", "ok"), ("3", "chỗ lệch", "bad"), ("59", "token Component chờ gộp", "")],
  tag_kind="spacing",  # radius | spacing | effect | icon | None: bật nhãn số đo đọc từ trình duyệt trên màn demo
  screens=dict(intro="…", proposal_css=".tp-f.tp-prop{--layout-card-padding:var(--space-3xl)}", logo_svg=None, gridov=False, overlay_html=None),
  sections=[dict(title="Bảng đối chiếu từng bậc — Untitled ↔ mình", intro="…", html=kit.rows([...],[...])),
            dict(title="Bộ chung đề xuất (nếu chọn hết theo khuyến nghị)", html="…")],
  items=[dict(id="sp00", grp="Cấu trúc", title="…", why="html", untitled="html", ours="html", astryx="html",
              tokens=[("space/xx", "12", "dùng cho …")], note="html", pv=kit.panes(fn, platforms=("web","mobile")),
              opts=[("a", "Nhãn phương án", True), ("b", "Nhãn", False)])],
  final="Khi bạn chốt: mình cập nhật … rồi đặt <b>space = approved</b> (<code>ds-foundation-status.py set space approved</code>). Component đang có bị đánh stale và sync dần (rule ds-stale).",
  css="", js="",
)
```

Helper `kit`: `panes(fn(mode, platform) | html, modes, platforms)` · `rows(headers, rows)` (ô `"n:12"` căn phải; trạng thái dùng lớp `st-ok st-diff st-gap st-own`) · `icon(name, "tp-ic-md")` tải Lucide thật · `cr("color/text/primary","color/bg/primary",min)` đo tương phản trên trang · `t("title-1", text)` chữ theo style thật · `demo_screens()` đã có sẵn khi khai `screens`. Atom sẵn: `tp-card tp-btn(.sec) tp-inp tp-chip(tp-g/b/y) tp-menu tp-dlg tp-scrim`. Đọc `kit.py` trước.

Trang tải `tokens.css` thật. Đề xuất đè trên màn demo qua `.tp-f.tp-prop{--x:…}` (web/mobile riêng thì `.tp-f.tp-prop[data-platform=mobile]`). Mã id mục: `ic` icon · `lg` logo · `ef` effect · `sp` spacing · `rd` radius · `gr` grids, đánh số từ 00, kit lưu lựa chọn theo id.

## Nội dung phải có

1. **Đối chiếu đủ, không chọn lọc**: mọi bậc/biến của Untitled trong mục đó ↔ token của mình, mỗi dòng một trạng thái: Giống · Khác có lý do · Mình thiếu · Chỉ mình có. Có số đếm khớp KPI.
2. **Mỗi lựa chọn đủ khung**: Lý do (`why`) nêu số dùng thật, nguồn trích dẫn, Untitled, mình, Astryx, xem thử, 2-3 phương án, đúng 1 khuyến nghị.
3. **Xem thử dựng từ biến thật**, có Sáng/Tối và Web/Mobile khi giá trị đổi theo chế độ. Không có câu hỏi chỉ bằng chữ; thật sự không dựng được mới khai `pv_none="lý do"`.
4. **Đề xuất phải sát Invlogis**, không chép Untitled máy móc: logistics, web điều vận dày dữ liệu, app lái xe ngoài trời. Không đề xuất token vai brand/marketing không ai dùng (tinh thần DEC-320).
5. Đã có quyết định thì tôn trọng: trích DEC, không mở lại trừ khi có bằng chứng mới và nói rõ lý do mở lại. Hướng đã chốt ở Màu và Chữ: tên theo Untitled, giá trị giữ của mình khi có lý do, gộp một bộ web/app nếu làm được (DEC-316 c01, DEC-320, DEC-322), token theo vai trỏ vào thang (DEC-314, DEC-315). Phần nào còn tách Web/Mobile phải có mục hỏi có gộp không.

## Số liệu: không nhớ, không đoán

| Số | Lấy từ |
|---|---|
| Token của mình | `design-system/tokens.json`, `tokens.css` (0.22.0), `design-system/foundations/<mục>.md` (bảng lệch thì json thắng) |
| Untitled | `design/_ref/untitled-ui/*.md`, `tokens.untitled.json`, `raw/`, `react/` (cách họ dùng thật trong component). Ref ghi `?` hoặc thiếu thì nói thiếu |
| Component dùng | `design-system/_review/token-usage.json` (chạy `python3 _scripts/ds-token-usage.py --summary`, không ghi đè), grep `design-system/components/_work/*/page.json` và `components/{base,application}/*.md` |
| Sổ gộp | `design-system/components/_token-ledger.json` (DEC-319, token Component chờ đợt 2) |
| Astryx | `design/design.md` |

Đếm bằng lệnh rồi mới ghi. Build kiểm token, DEC, đường dẫn, biến CSS viện dẫn phải tồn tại.

## Văn phong (người duyệt phản ánh nhiều lần)

- Tiếng Việt thường, câu ngắn. Mỗi mã (`DEC-…`, token, tên file) đi kèm nghĩa; trích nguyên văn nguồn khi nêu luật; dẫn đường dẫn file.
- Đánh dấu từ khoá `<mark>`/`<b>`, 1-3 chỗ mỗi câu dài. Đổi chữ thành bảng, thang, hình khi được.
- Không nói "cái này", "phần trên". Không gạch đầu dòng dài. Không viết tắt tự chế. Không mở câu bằng phán xét kiểu "đây không phải X".
- Nhãn phương án nói việc sẽ xảy ra ("Thêm `space/…`, mọi màn đổi 2px"), không "Phương án A".
- Màn demo chứa dữ liệu logistics thật; chữ dài không tràn.

## Trả về

Báo cáo ≤ 12 dòng: kết quả build cuối (số mục, fail/warn), 3-5 phát hiện chính, điều chưa chắc (ref thiếu…), lỗi kit nếu có. Không dán SPEC.

## Luật thống nhất sau soát chéo (áp cho cả 6 trang)

- **Không đánh số lại mục**: người duyệt đã có thể lưu lựa chọn theo id. Bỏ mục thì để trống số đó.
- Tên section bắt buộc: `Bảng đối chiếu … — Untitled ↔ mình` · `Đã chốt, không mở lại` (bảng DEC đang hiệu lực, mỗi dòng một câu) · `Bộ chung đề xuất (nếu chọn hết theo khuyến nghị)`. Build chặn nếu thiếu.
- Câu `final` mẫu: "Khi bạn chốt: mình cập nhật `tokens.json` → sinh `tokens.css` + handoff → sửa `design-system/foundations/<file>.md` → cập nhật biến Figma cùng lượt → ghi DEC; rồi đặt <b>x = approved</b> (`ds-foundation-status.py set x approved`). Component đang có bị đánh stale và sync dần (rule ds-stale)." Thêm việc riêng của trang sau câu này.
- Thuật ngữ: nhãn nền tảng hiển thị **Web · App**; chữ "Mobile" chỉ khi nói tên chế độ token. **Sáng · Tối** trong câu chữ; Light/Dark chỉ khi trích tên chế độ. Khung demo gọi **màn mẫu**.
- Khung chuẩn: web **1280**, menu **240** (DEC-039), app **393**. 375 và 320 chỉ là máy thử.
- Mở lại DEC: đọc đúng dòng DEC đó (cả cột Bỏ), kiểm DEC còn hiệu lực hay đã "thay bởi", viết câu **"Mở lại DEC-x:"** kèm bằng chứng mới. DEC đã thay thì trích DEC thay thế. Phương án trùng với phương án DEC đã bỏ cũng tính là mở lại.
- Không thêm bậc Semantic cho số lẻ khi DEC-314 đã bỏ: ghi ngoại lệ. Không mượn token vai khác vì trùng số (cùng tinh thần `ic11`, `rd09`).
- Tên token mới không được trùng tên Untitled mà khác số (lý do của `gr00`).
- Mục phụ thuộc trang khác: thêm dòng `note` "Phụ thuộc <mã>: nếu chọn …, thì …" và ghi số kèm tên, không chỉ tên.
- Điều lấy từ trí nhớ hoặc web: ghi nguồn hoặc ghi "chưa kiểm"; số chỉ đúng trong điều kiện nào thì nói điều kiện.
- Mã, ký hiệu (K1–K4, "đợt 2") giải nghĩa ở lần xuất hiện đầu trên trang.
