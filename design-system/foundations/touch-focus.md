---
type: design-foundations
status: draft
updated: 2026-11-02
links:
  - design-system/foundations/README.md
  - design-system/tokens.json

---

# Foundations · Vùng chạm và focus

> Một phần của [[design-system/foundations/README.md|Foundations]]. Giữ số mục cũ (9.x) để các DEC và spec trích "foundations mục 9…" vẫn tra được. Giá trị máy đọc: `design-system/tokens.json` (json thắng).

## 9. Vùng chạm và focus (DEC-97, DEC-138, DEC-139, DEC-241, DEC-339)

Ba token giữ tên `touch/min`, `focus/width`, `focus/offset`. Untitled không có token vùng chạm nên không có tên nào để theo; màu `color/focus/ring` đã khớp tên Untitled.

### 9.1 Sàn vùng chạm

Vùng chạm tính theo **phần bấm** (nút, link, icon đứng riêng), không theo icon bên trong. Phần thiếu là vùng bấm vô hình, nút nhìn không đổi. Bù mỗi phía = (`touch/min` − cao phần bấm) / 2.

| Nền tảng | `touch/min` | Phần bấm | Bù mỗi phía |
|---|---|---|---|
| App (ưu tiên iOS, DEC-138; dưới mức 48dp Android khuyên) | 44 | Nút chân màn 52 | không bù |
| | | Nút MD, nút icon 44 | không bù |
| | | Nút SM 36 (tab chip, nút trong Alert) | 4 |
| | | Icon đứng riêng 20 · 16 · 14 · 12 | 12 · 14 · 15 · 16 |
| Web (WCAG 2.2 AA, mục 2.5.8) | 24 | Nút từ 28 trở lên | không bù |
| | | Icon đứng riêng 16 · 14 · 12 | 4 · 5 · 6 |

- **Icon đứng riêng:** bù vô hình tới sàn, không đổi số icon (`icon/size/*` theo DEC-329). Trong nút chữ và nút icon, icon nhỏ đi thì lề trong tăng, cao nút giữ nguyên.
- **Con trỏ thô (mobile web, tablet cảm ứng):** `@media (pointer: coarse)` đặt `--touch-min` = 44 trên chế độ Web, nút nhìn giữ nguyên. Luật sinh trong `tokens.css` từ giá trị Mobile của `touch/min`. **Chưa kiểm trên máy thật.** Chỉ phần bấm có `.touch-target` mới được nới, nên nút web muốn đủ 44 trên máy cảm ứng phải mang lớp này dù ở con trỏ chuột không cần bù.

### 9.2 Cách bù: `.touch-target`

Một lớp dùng chung trong `tokens.css`, không viết số tay trong component:

```css
:where(.touch-target) { position: relative; }
.touch-target::after { content: ""; position: absolute; top: 50%; left: 50%; width: 100%; height: 100%;
  min-width: var(--touch-min); min-height: var(--touch-min); transform: translate(-50%, -50%); }
```

- Đổi sàn thì mọi chỗ đổi theo; phần bấm lớn hơn sàn thì vùng bấm bằng đúng phần bấm.
- **Bị `overflow:hidden` cắt:** khung cha cắt thì phần bù mất, vùng chạm tụt về cỡ nhìn thấy mà không báo lỗi. Kiểm khi đặt phần bấm vào khung có `overflow:hidden`, nhất là thẻ bo góc và hàng cuộn ngang.
- `::after` chỉ có một: phần tử đã dùng `::after` cho việc khác (mũi tên, vùng nối tooltip) thì bọc thêm một lớp.
- Trên Figma không vẽ phần bù; khung tài liệu đánh dấu bằng `Vùng chạm · touch/min` (`design-system/components/README.md`).

### 9.3 Khoảng cách giữa hai vùng chạm

Hai vùng không chồng lên nhau, và trên app hai phần bấm cách nhau tối thiểu 8. Web trên máy cảm ứng: hai nút cạnh nhau cách tối thiểu 12, kể cả trong hàng bảng (user 02/11). Khoảng cách tối thiểu = lớn hơn trong hai số: `touch/min` − cao phần bấm, và 8 (chỉ app).

| Hai phần bấm cạnh nhau | App | Web |
|---|---|---|
| Nút 44 | 8 | — |
| Nút 36 | 8 | — |
| Nút từ 28 | — | 0 |
| Icon đứng riêng 16 | 28 | 8 |

### 9.4 Nút chỉ có icon

- **Web:** từ 28 trở lên, có tooltip.
- **App:** 44, không bù (DEC-341 sp10).
- **Tên đọc:** theo luật nhãn DEC-329, bắt buộc vì không có chữ.

### 9.5 Vòng focus

- **Hình:** `outline` dày `focus/width` 2, cách `focus/offset` 2, màu `color/focus/ring` (than chì) cho mọi khách, không theo dải màu khách (DEC-170). Nút Danger: `color/focus/ring_error` (DEC-198, DEC-318).
- **Khe (DEC-327, thay phần khe của DEC-241, DEC-258):** khe trong suốt nên đúng trên mọi nền không đặc, không có token khe. Trên Figma khung vòng `.focus / Ring` không tô nền. Không thêm style focus-ring gộp bóng của Untitled; vòng là lớp riêng nên bóng thẻ giữ nguyên.
- **Không dùng `box-shadow` để vẽ vòng (DEC-327).** Ngoại lệ duy nhất là viền ô nhập đang gõ, mục 9.7: đó là viền ô, không phải vòng.
- **Mọi chỗ đọc token:** không viết số, không tự đặt biến riêng (`--focus`, `--focus-color`, `--color-focus-gap` đã bỏ).
- **Một vòng cho mọi nền không đặc** (nền phụ, dòng chọn, nền trạng thái nhạt, thẻ): thấp nhất 8,23:1, đủ 3:1 của WCAG 1.4.11. Thẻ bấm được cũng dùng vòng ngoài, không dùng viền 2.
- **Cấm đặt control lên nền đặc** (`*_solid`, `color/action/primary`): vòng than chì rớt còn 1,18:1 trên `color/bg/primary_solid` Sáng, 2,3:1 trên `color/bg/error-solid`, nên không có token vòng đảo. Thân chính nút Primary là nền đặc của nó, vòng nằm ngoài nên không tính. Nút trên ảnh hoặc lớp phủ ảnh (nút xoá Field Upload) không tính là nền đặc (user 02/11).

### 9.6 Vòng ngoài hay vào trong

Phần ló ra ngoài của vòng là 4 (`focus/width` + `focus/offset`). Vào trong: `outline-offset: calc(var(--focus-width) * -1)`.

| Ca | Vòng |
|---|---|
| Nút, link, thẻ bấm được, mặc định | Ngoài, 2 cách 2 |
| **Lề khung cha ≥ 4** | Ngoài |
| **Lề khung cha < 4** (khung có `overflow:hidden`, hoặc phần tử kế bên đè) | Vào trong 2 |
| Dòng và ô bảng tự nhận focus | Vào trong 2 |
| Nút trong ô bảng | Ngoài |
| Mục menu, tab | Vào trong 2 |
| Mục sidebar | Ngoài, thêm `z-index` để nổi lên trên mục kế bên |
| Nút đặc (Primary, Danger) | Luôn ngoài: vào trong sẽ cùng màu với thân nút |

### 9.7 Ô nhập đang gõ

Giữ viền và bóng trong: đổi màu viền sang `color/focus/ring` + `box-shadow: inset 0 0 0 1px`, ra viền 2 mà chữ không nhích (DEC-321). **Không đổi sang outline.** Đây là ngoại lệ của câu "Không dùng `box-shadow` để vẽ vòng" trong DEC-327, vì đây là viền ô, không phải vòng.

### 9.8 Khi nào hiện

- **Web:** mọi control dùng `:focus-visible`, bấm chuột không hiện vòng. Cấm `outline:none` nếu không có vòng thay thế; `ds-token-usage.py --check` WARN khi gặp. Class `.is-focus` trong trang review chỉ vẽ state tĩnh, không phải cách làm cho code.
- **App:** không vẽ state Focus trên Figma; code bật vòng 2 cách 2 khi có bàn phím ngoài; ô đang gõ giữ viền 2.

### 9.9 Bàn phím

- **Thứ tự Tab:** theo DOM, cấm `tabindex` dương.
- **Bảng, menu, tab:** một điểm dừng Tab, mũi tên đi bên trong.
- **Dialog, sheet:** mở thì focus vào nút an toàn hoặc ô đầu; Tab đi vòng trong khung; Esc đóng; đóng thì trả focus về nút đã mở; lớp phủ không nhận focus.
- **Thanh dính che focus (WCAG 2.4.11):** khung cuộn đặt `scroll-padding`, luật ở `design-system/foundations/grids.md`, mục Khung cuộn có thanh dính.

### 9.10 Trạng thái không chỉ bằng màu (WCAG 1.4.1)

Mọi trạng thái có chữ hoặc dấu. Dòng chọn trong danh sách chọn phải có ô chọn hoặc dấu tick, không áp cho mục điều hướng (sidebar đang chọn dùng nền và chữ đậm, user 02/11): `color/bg/selected` so với nền chỉ 1,09:1 Sáng, 1,24:1 Tối.

### 9.11 Dòng kiểm khi đối chiếu foundation

- [ ] Phần bấm thấp hơn `touch/min` có `.touch-target`, khung cha không cắt phần bù.
- [ ] Hai vùng chạm không chồng; trên app cách nhau tối thiểu 8.
- [ ] **Lề khung ≥ 4 thì vòng ngoài, < 4 thì vòng vào trong.** Máy chỉ kiểm khi dòng `focus-offset` trong `values` khai `clipInset` (`ds-foundation-check.py`); dòng không khai thì người soi, vì lề khung thật chưa đo tự động được từ CSS.
- [ ] Control không nằm trên nền đặc.
- [ ] `:focus-visible`, không có `outline:none` trơ.
