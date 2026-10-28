#!/usr/bin/env python3
"""Generate 01-colors-primitives.md (full 27-scale table from s1-primitives.json)."""
import json

prim = json.load(open('_task/s1-primitives.json', encoding='utf-8'))

HUES_17 = ['Red','Orange','Amber','Yellow','Lime','Green','Emerald','Teal','Cyan','Sky','Blue',
           'Indigo','Violet','Purple','Fuchsia','Pink','Rose']
HUES_9 = ['Slate','Gray','Zinc','Neutral','Stone','Taupe','Mauve','Mist','Olive']
STEPS = ['50','100','200','300','400','500','600','700','800','900','950']
NO_TAILWIND = {'Taupe','Mauve','Mist','Olive'}

def wcag_cell(v):
    w = v['wcag'].strip()
    if not w:
        return '—'
    if '4.82?' in w:  # Lime-50 error
        return 'AAA 4.82 ⚠'
    return w

def s2_cell(hue, v):
    if hue == 'Brand':
        return 'khớp repo'
    if hue in NO_TAILWIND:
        return '— (không có trong repo)'
    return 'khớp Tailwind'

def note_cell(hue, step, v):
    notes = []
    if hue == 'Neutral':
        notes.append('Default gray')
    if v.get('default'):
        notes.append('bậc mặc định •')
    if hue == 'Brand' and step == '25':
        pass
    if hue == 'Lime' and step == '50':
        notes.append('lỗi nhãn: 4.82 < 7 nhưng ghi AAA')
    return ', '.join(notes)

lines = []
lines.append('---')
lines.append('type: design-reference')
lines.append('status: draft')
lines.append('updated: 2026-10-26')
lines.append('links:')
lines.append('  - https://www.figma.com/design/QERVV4a2Fpa1FmsZ5LGW3S/ (Colors, node 5225-371288)')
lines.append('  - https://github.com/untitleduico/react (styles/theme.css, .storybook/colors.css)')
lines.append('  - https://www.untitledui.com/react/docs/theming')
lines.append('---')
lines.append('')
lines.append('# 01 — Colors · Primitives (dải màu × bậc)')
lines.append('')
lines.append('> Hex chỉ nằm ở file này (theo spec). Các file 02 trở đi chỉ ghi alias.')
lines.append('> Nguồn: S1 (Figma frame Colors, đọc nhãn trên canvas — hex + nhãn WCAG) · S2 (repo).')
lines.append('> Figma v8 dùng **màu Tailwind CSS v4.1** (ghi trên frame Colors) để đồng bộ design–code;')
lines.append('> Brand vẫn là **tím Untitled** (không phải dải Tailwind). Nhãn WCAG 2.2 in trên từng ô.')
lines.append('')
lines.append('## 1. Base')
lines.append('')
lines.append('| Token | Hex (S1) | Nhãn WCAG (S1) | Ghi chú |')
lines.append('|---|---|---|---|')
for name in ['White','Black','Transparent']:
    v = prim['Base'][name]
    if name == 'Transparent':
        lines.append(f'| {name} | {v["hex"]} 0% | — | trong suốt; repo khai `--color-transparent = rgb(0 0 0 / 0)` |')
    else:
        lines.append(f'| {name} | {v["hex"]} | {wcag_cell(v)} | |')
lines.append('')
lines.append('## 2. 27 dải màu × bậc (50–950)')
lines.append('')
lines.append('| Dải | Bậc | Hex (S1) | Nhãn WCAG (S1) | Hex S2/Tailwind | Ghi chú |')
lines.append('|---|---|---|---|---|---|')
for hue in ['Brand'] + HUES_17 + HUES_9:
    for step in STEPS:
        v = prim[hue][step]
        lines.append(f'| {hue} | {step} | {v["hex"]} | {wcag_cell(v)} | {s2_cell(hue, v)} | {note_cell(hue, step, v)} |')
lines.append('')
lines.append('> Tổng 27 dải × 11 = 297 + Base 3 = 300 màu. Thứ tự dải xám trên canvas: Slate, Gray, Zinc,')
lines.append('> Neutral, Stone, Taupe, Mauve, Mist, Olive (9 xám; spec ghi "8" nhưng liệt kê 9).')
lines.append('> Mô tả: các dải sắc "Can be swapped with the default brand color"; các dải xám "Can be swapped')
lines.append('> with the default gray color". Neutral = "Default gray".')
lines.append('')
lines.append('## 3. So S2 (repo)')
lines.append('')
lines.append('- **Brand**: khớp 100% repo `theme.css` (`--color-brand-50…950`). Repo còn có **bậc 25**')
lines.append('  (`#fcfaff`, chỉ trong `.storybook/colors.css`, không có trong theme.css) — Figma không có bậc 25.')
lines.append('- **17 sắc + 5 xám chuẩn** (Slate/Gray/Zinc/Neutral/Stone): Figma khớp Tailwind v4.1 mặc định;')
lines.append('  repo không khai lại (tham chiếu `--color-<hue>-*` Tailwind native). Đã so từng hex = 0 lệch.')
lines.append('- **4 xám Untitled** (Taupe/Mauve/Mist/Olive): không có trong repo/`.storybook/colors.css` (chỉ có ở Figma).')
lines.append('')
lines.append('## 4. Gradients (S1 — frame 1525-272676)')
lines.append('')
lines.append('- **Neutral gradients** (14 style): tuyến tính giữa 2 primitive, vd `Neutral/600 -> 500 (90deg)`.')
lines.append('  Dùng cho nền, thêm chiều sâu/kết cấu nhẹ.')
lines.append('- **Brand gradients** (7): như trên với primitive Brand (vd `600 -> 500 (90deg)`). Theo màu brand,')
lines.append('  dùng cho phần tử tương tác.')
lines.append('- **Linear gradients 01…33** (thiếu 23, 28 trong danh sách): 2 stop hex cố định, không gắn biến,')
lines.append('  vd `Linear/01` #A5C0EE → #FBC5EC. Nhiều màu cho nền, làm vật thể nổi bật. Stop 02–33: chưa đọc.')
lines.append('- **Mesh gradients**: là ẢNH (fill Image "01.png"…), không phải token. Tạo bằng công cụ Mesh.')
lines.append('- **skeuemorphic-gradient-border**: chưa đọc giá trị.')
lines.append('')
lines.append('## 5. Luật dùng màu')
lines.append('')
lines.append('| # | Luật | Nguồn |')
lines.append('|---|---|---|')
lines.append('| 1 | Hệ màu tối giản cần: neutral, brand, accent và màu phản hồi (xanh = thành công, đỏ = lỗi), nhất là khi có form | S1 |')
lines.append('| 2 | Neutral = nền tảng (chữ, form field, nền, divider thường là xám); Brand = mọi phần tử tương tác (button, link, input) | S1 |')
lines.append('| 3 | Accent = màu phụ gây chú ý/hỗ trợ brand, hợp cho label và badge; Feedback: error = lỗi/destructive, warning = hành động nguy hiểm/on-hold, success = tích cực | S1 |')
lines.append('| 4 | Nếu primary là xanh lá thì chọn sắc khác cho success (tránh nhầm) | S1 |')
lines.append('| 5 | Dùng 8–12 sắc mỗi màu (không cần 50); sinh bằng generator Tailwind (uicolors.app, tailwindshades.com, tints.dev, tailcolor.com) | S1 |')
lines.append('| 6 | WCAG 2.2: A <4.5:1 (không cho chữ); AA ≥4.5:1 (mặc định cho chữ/button/form); AAA ≥7:1 (nice-to-have). Giữ ≥4.5:1 cho phần tử quan trọng | S1 |')
lines.append('| 7 | Đặt tên theo token (`neutral-300`, `brand-600`), không dùng hex rời; nhất quán (vd luôn neutral-300 cho viền input field, neutral-200 cho divider) | S1 |')
lines.append('| 8 | Quản lý màu bằng variables (primitives = nguồn sự thật), không dùng color styles | S1 |')
lines.append('')
lines.append('## 6. Ghi chú')
lines.append('')
lines.append('- ⚠ **Lỗi nhãn Lime-50**: Figma ghi "AAA 4.82" nhưng 4.82 < 7 → nhãn AAA có vẻ sai trong file gốc.')
lines.append('- Bậc mặc định (chấm trắng • trên ô): Brand = 600; 26 dải còn lại = 500.')
lines.append('- Lịch sử: v5.0 xám hơi xanh (B2B/SaaS); v6.0 xám flat; v8.0 chuyển toàn bộ sang Tailwind,')
lines.append('  xám mặc định = neutral (khử bão hoà hoàn toàn). React bỏ 436 biến màu thừa: theme 65KB → 45KB.')
lines.append('- `_Primitives` → Colors = 311 trên Figma nhưng đọc được 300; 11 biến chưa giải thích (xem `00-structure.md`).')

open('01-colors-primitives.md', 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
print('wrote 01-colors-primitives.md, rows:', len(lines))
