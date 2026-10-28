# S1 Effects — đọc từ panel Properties khi chọn từng card (DOM), trang Effect styles
Thứ tự lớp như panel Figma liệt kê. Màu bóng là BIẾN `Colors/Effects/Shadows/<name>_NN` (collection Color modes → có thể khác ở Dark; giá trị Dark chưa đọc). Light: #000000 + độ mờ.
Card: `_Shadow card` 256×240, radius-xl, border 1px border-secondary_alt (#000000 10%), padding spacing-3xl, fill bg-primary.

| style | lớp | x | y | blur | spread | màu biến | Light |
|---|---|---|---|---|---|---|---|
| shadow-xs | 1 | 0 | 1 | 2 | 0 | shadow-xs | #000 5% |
| shadow-sm | 1 | 0 | 1 | 2 | -1 | shadow-sm_02 | #000 10% |
| shadow-sm | 2 | 0 | 1 | 3 | 0 | shadow-sm_01 | #000 10% |
| shadow-md | 1 | 0 | 2 | 4 | -2 | shadow-md_02 | #000 6% |
| shadow-md | 2 | 0 | 4 | 6 | -1 | shadow-md_01 | #000 10% |
| shadow-lg | 1 | 0 | 2 | 2 | -1 | shadow-lg_03 | #000 4% |
| shadow-lg | 2 | 0 | 4 | 6 | -2 | shadow-lg_02 | #000 3% |
| shadow-lg | 3 | 0 | 12 | 16 | -4 | shadow-lg_01 | #000 8% |
| shadow-xl | 1 | 0 | 3 | 3 | -1.5 | shadow-xl_03 | #000 4% |
| shadow-xl | 2 | 0 | 8 | 8 | -4 | shadow-xl_02 | #000 3% |
| shadow-xl | 3 | 0 | 20 | 24 | -4 | shadow-xl_01 | #000 8% |
| shadow-2xl | 1 | 0 | 4 | 4 | -2 | shadow-2xl_02 | #000 4% |
| shadow-2xl | 2 | 0 | 24 | 48 | -12 | shadow-2xl_01 | #000 18% |
| shadow-3xl | 1 | 0 | 5 | 5 | -2.5 | shadow-3xl_02 | #000 4% |
| shadow-3xl | 2 | 0 | 32 | 64 | -12 | shadow-3xl_01 | #000 14% |
Mọi lớp: drop shadow, "Behind transparent areas: True". Frame Shadows mô tả: shadow tạo chiều sâu, đặt phần tử theo trục z.

## Focus rings (frame 5424-398991) — đọc panel Properties
Mô tả frame: focus ring đơn lớp cho phần tử không cần shadow (toggles, checkboxes). Có phần tử (buttons) cần ring + shadow; Figma không gắn được nhiều effect style một lúc nên ring được gộp sẵn với shadow style. Biến thể skeuomorphic = ring + shadow-xs + bóng trong nhẹ.
| style | lớp (thứ tự panel): x y blur spread · màu |
|---|---|
| focus-ring | 0 0 0 4 · focus-ring #9E77ED (=brand-500) ; 0 0 0 2 · bg-primary #FFFFFF |
| focus-ring-error | 0 0 0 4 · focus-ring-error #EF4444 (=red-500) ; 0 0 0 2 · bg-primary #FFFFFF |
| focus-ring-shadow-xs | ring 4 brand + gap 2 bg-primary ; 0 1 2 0 · shadow-xs #000 5% |
| focus-ring-shadow-sm | ring 4 brand + gap 2 ; 0 1 2 0 · shadow-sm_02 #000 10% ; 0 1 3 0 · shadow-sm_01 #000 10% (⚠ lớp sm_02 ở đây spread 0, còn style shadow-sm spread -1) |
| focus-ring-error-shadow-xs | ring 4 red + gap 2 ; 0 1 2 0 · shadow-xs 5% |
| focus-ring-shadow-xs-skeuomorphic | ring 4 brand + gap 2 ; 0 1 2 0 shadow-xs 5% ; 0 -2 0 0 · shadow-skeumorphic-inner #000 5% ; 0 0 0 1 · shadow-skeumorphic-inner-border #000 18% |
| focus-ring-error-shadow-xs-skeuomorphic | như trên, ring red-500 |
Ghi chú: ring = spread 4 màu brand ngoài + spread 2 màu bg-primary (khoảng hở trắng). Panel không ghi loại inner/drop cho lớp y=-2 và spread 1 (theo tên "inner" → bóng trong). Tên biến có lỗi chính tả gốc "skeumorphic".
⚠ Phát hiện: focus-ring dùng #9E77ED = brand-500 kiểu Untitled (không phải Tailwind violet-500 #8b5cf6) → cần kiểm hex dải Brand trên frame Colors.

## Backdrop blurs (frame Blurs)
| style | blur |
|---|---|
| backdrop-blur-sm | 8 |
| backdrop-blur-md | 16 |
| backdrop-blur-lg | 24 |
| backdrop-blur-xl | 40 |
Card mẫu (sm): fill #FFFFFF 60%, viền 1px #FFFFFF 50%, radius-xl, padding spacing-4xl, cao 320, min-width 800 → kiểu glass trên ảnh nền.

## Notes and documentation — trang Effect styles (node 6721-166239), luật dùng (diễn giải)
- Buttons và featured icons đã chuyển sang kiểu skeuomorphic nhẹ (Version 5.0; flat = Version 4.0). Skeuomorphic = drop shadow + inner shadow + linear stroke + fill. Hiệu ứng cố tình rất nhẹ; điều kiện: không phá accessibility.
- Bỏ skeuomorphic rất dễ: hiệu ứng là effect style riêng; đổi effect style ở master component (vd shadow-xs-skeuomorphic → shadow-xs) để bật/tắt.
- Focus ring = "focus indicator", quan trọng cho người không dùng chuột. Figma không có focus ring sẵn và không gắn nhiều stroke → giải pháp: box-shadow đặc làm effect style; focus ring kết hợp shadow (focus-ring-shadow-*) để không mất bóng nâng.
- Mô tả style trong Figma: focus-ring = trạng thái focus cho toggles, checkboxes; focus-ring-shadow-xs-skeuomorphic = focus cho component có shadow + skeuomorphic (buttons, tabs), có thể thay bằng focus-ring-shadow-xs nếu muốn flat.
- Màu trong effect style gắn biến màu (Figma mới cho phép) → đổi biến là shadow/focus ring tự cập nhật.
- Hạn chế Figma: không tách biến khỏi độ mờ → không alias được primitive (vd neutral-950) với nhiều mức alpha; vì vậy biến shadow là màu riêng, phải cập nhật tay. Mặc định mọi shadow dùng đen #000000 + độ mờ thay đổi, để không phụ thuộc dải xám đang dùng.
- Ảnh panel Variables (cập nhật hơn ảnh ở trang Variables): 1. Color modes 274 → Groups: Colors 100 (Text 21, Border 8, Foreground 19, Background ?), Effects 23, Component colors 174. Biến Effects: shadow-xs 5%, shadow-sm_01 10%, shadow-sm_02 10%, shadow-md_01 10%, shadow-md_02 6%, shadow-lg_01 8%, lg_02 3%, lg_03 4%, xl_01 8%, xl_02 3%, xl_03 4%, 2xl_01 18% (khớp giá trị đọc ở card).
