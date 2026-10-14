"""Nội dung 14 slide. Mỗi slide = danh sách phần tử toạ độ px trên khung 1920x1080."""
from lib import *

BG = lambda code: f"assets/bg/bg-{code}_1920x1080.jpg"
LOGO = lambda n: f"assets/logo/{n}.png"

def build_slides():
    S = []

    # 1 · Bìa ------------------------------------------------------------
    s = Slide("Bìa", BG("n6-muc-cobalt"), "Bìa. Khẩu hiệu chính DEC-072. Lockup 'by innvie' chỉ ở bìa và trang cuối (brand-strategy Mục 6).")
    IMG(s, LOGO("invlogis-by-innvie-reverse"), 120, 96, 150 * 2.6856, 150)
    T(s, 120, 360, 1380, 330, "Khai mở\ncách vận hành mới.", size=124, font="d", weight=300, color=WHITE, lh=1.08)
    T(s, 120, 740, 1100, 130, "Nền tảng vận hành cho doanh nghiệp giao nhận, vận tải container Việt Nam. AI đọc chứng từ Việt vào thẳng hồ sơ lô hàng.",
      size=32, color=PERI_L, lh=1.4)
    # chip kính: gợi cảnh AI đọc chứng từ
    for i, (txt, y) in enumerate([("[Booking Note · đã đọc]", 330), ("[eDO · 4 trường]", 410), ("[EIR · đã đọc]", 490)]):
        w = chip(s, 1800, y, txt, color=WHITE, fill=NIGHT, a=0.55, size=22, h=52, line=PERI, align="r", pad=24)
    T(s, 120, 996, 1000, 28, "Bản giới thiệu cho khách hàng  ·  bản nháp 14/10/2026", size=20, font="m", color=PERI_L, lh=1.0)
    T(s, 1100, 996, 700, 28, "Open a new way to operate.", size=22, font="d", weight=300, color=PERI_L, align="r", lh=1.0)
    S.append(s)

    # 2 · Hiện trạng -----------------------------------------------------
    s = Slide("Hiện trạng", BG("n5-giay-lua"), "Nguồn: PRD Mục 2 và mục Vấn đề của landing page (web/index.html). Không trích khách nào.", "light")
    label(s, "[%02d · Hiện trạng]" % (len(S) + 1), False)
    T(s, 120, 140, 800, 330, "Mỗi lô hàng đi qua nhiều tờ giấy, và nhiều lần gõ lại.", size=62, font="d", weight=300, color=INK, lh=1.12)
    T(s, 120, 560, 760, 260, "Cùng một số container xuất hiện ở điều vận, xưởng, công nợ. Mỗi nơi gõ một lần; quá mốc cảng là bị phạt lưu container, lưu vỏ.",
      size=26, color=SLATE_T, lh=1.45)
    items = [("DEM", "Phí lưu container", "Container hàng nhập nằm trong cảng quá hạn miễn phí thì mất phí lưu container."),
             ("DET", "Phí lưu vỏ", "Tính từ giờ trên EIR lúc lấy hàng đến lúc trả vỏ đúng nơi hãng chỉ định; quá hạn thì mất phí lưu vỏ."),
             ("GIẤY", "Giấy về chậm", "EIR, biên bản, phiếu cân về chậm nên chốt Lệnh và tính chi phí cũng chậm."),
             ("NHẬP LẠI", "Excel, Zalo, giấy tờ", "Dữ liệu một lô nằm rải ở nhiều người, nhiều file; giao việc hiện trường qua Zalo, khó tra lại.")]
    y0 = 140
    for i, (n, t, d) in enumerate(items):
        y = y0 + i * 190
        R(s, 1000, y, 800, 2, fill=INK, a=0.16)
        chip(s, 1000, y + 22, n, color=NAVY, size=18, h=34, pad=14)
        T(s, 1000, y + 70, 780, 44, t, size=34, font="d", weight=400, color=INK, lh=1.15)
        T(s, 1000, y + 118, 780, 66, d, size=24, color=SLATE_T, lh=1.35)
    R(s, 1000, y0 + 4 * 190, 800, 2, fill=INK, a=0.16)
    footer(s, len(S) + 1, False); S.append(s)

    # 3 · Cách làm khác --------------------------------------------------
    s = Slide("Cách làm khác", BG("n3-chamtim"), "AI là lý do làm được, kết quả nói trước (brief Mục 5). Thẻ chứng từ vẽ bằng khối, giá trị mẫu hiển nhiên giả.")
    label(s, "[%02d · Cách làm khác]" % (len(S) + 1))
    T(s, 120, 170, 860, 280, "Chứng từ vào.\nHồ sơ sẵn.", size=104, font="d", weight=300, color=WHITE, lh=1.08)
    T(s, 120, 500, 760, 220, "Invlogis dùng AI đọc Booking Note, eDO, EIR, phiếu cân và tờ khai có QR, rồi điền vào hồ sơ lô hàng. Bạn kiểm tra và duyệt, không gõ lại.",
      size=30, color=PERI_L, lh=1.45)
    x = 120
    for t in ["Bớt nhập lại", "Đúng mốc cảng", "Dữ liệu đi tiếp"]:
        x += chip(s, x, 790, t, color=WHITE, fill=NIGHT, a=0.5, size=22, h=52, line=PERI, pad=24) + 14
    def doc(x, y, w, h, tag, rows, tail):
        R(s, x, y, w, h, fill=WHITE, a=0.96, line=INK, la=0.12, r=24)
        chip(s, x + 28, y + 26, tag, size=18, h=36, pad=14)
        for k, (kk, vv) in enumerate(rows):
            T(s, x + 28, y + 84 + k * 70, w - 56, 22, kk, size=16, font="m", color=SLATE_T, ls=0.08, lh=1.0)
            R(s, x + 24, y + 108 + k * 70, w - 48, 40, fill=LAV, r=10)
            T(s, x + 36, y + 108 + k * 70, w - 72, 40, vv, size=24, weight=500, color=INK, anchor="m", lh=1.0)
        T(s, x + 28, y + h - 44, w - 56, 26, tail, size=16, font="m", color=NAVY, align="r", lh=1.0)
    doc(1240, 70, 540, 290, "[eDO]", [("SỐ VẬN ĐƠN", "VD-0000"), ("SỐ CONTAINER", "MSKU 000000-0")], "đã đọc")
    doc(1060, 380, 540, 290, "[Booking Note]", [("SỐ BOOKING", "VD-0000"), ("LOẠI CONT", "40'HC × 0")], "đã đọc")
    doc(1280, 690, 520, 290, "[EIR]", [("SỐ CONTAINER", "MSKU 000000-0"), ("TRỌNG LƯỢNG", "00.000 kg")], "đã đọc · 2 trường")
    footer(s, len(S) + 1, True, "Dữ liệu minh hoạ"); S.append(s)

    # 4 · Cách hoạt động -------------------------------------------------
    s = Slide("Cách hoạt động", BG("n5-giay-lua"), "Ba bước, khớp mục Cách hoạt động của landing page. Bạn duyệt là chốt cuối.", "light")
    label(s, "[%02d · Cách hoạt động]" % (len(S) + 1), False)
    T(s, 120, 130, 1500, 120, "Ba bước, một dữ liệu.", size=72, font="d", weight=300, color=INK, lh=1.1)
    T(s, 120, 255, 1300, 80, "Bạn duyệt trước khi dữ liệu đi tiếp.", size=28, color=SLATE_T, lh=1.4)
    steps = [("01", "Chứng từ vào", "Tải lên hoặc chụp bằng điện thoại. Booking Note, eDO, EIR, phiếu cân, tờ khai có QR."),
             ("02", "AI đọc", "Invlogis đọc từng trường, gắn nhãn đã đọc và chỉ ra chỗ cần kiểm lại."),
             ("03", "Bạn duyệt", "Sửa nếu cần, bấm lưu. Cùng dữ liệu đó chạy sang điều vận, xưởng, công nợ, không nhập lại.")]
    cw, gap, cy, ch = 540, 30, 390, 540
    for i, (n, t, d) in enumerate(steps):
        x = 120 + i * (cw + gap)
        R(s, x, cy, cw, ch, fill=WHITE, a=0.88, line=INK, la=0.14, r=28)
        R(s, x + 24, cy + 24, cw - 48, 230, fill=SMOKE, a=1, r=18)
        gx, gy = x + 24 + 93, cy + 24
        if i in (0, 1):
            R(s, gx + 78, gy + 22, 150, 186, fill=WHITE, line=INK, la=0.2, r=12)
            chip(s, gx + 90, gy + 36, "[eDO]" if i else "[Booking]", size=16, h=30, pad=10)
            for k in range(4):
                R(s, gx + 95, gy + 90 + k * 26, 116 - (k % 2) * 30, 10, fill=INK, a=0.12, r=5)
            if i == 1:
                R(s, gx + 43, gy + 98, 220, 44, grad=(180, [(0, COBALT, 0), (.5, COBALT, .55), (1, COBALT, 0)]))
                chip(s, gx + 190, gy + 170, "[đã đọc]", size=16, h=30, pad=10)
        else:
            field(s, gx, gy + 14, 306, "SỐ CONTAINER", "MSKU 000000-0", fill=WHITE, h=62, vs=22, ks=15)
            field(s, gx, gy + 86, 306, "SỐ VẬN ĐƠN", "VD-0000", fill=WHITE, h=62, vs=22, ks=15)
            R(s, gx, gy + 164, 306, 48, fill=COBALT, r=24)
            T(s, gx, gy + 164, 306, 48, "Duyệt hồ sơ", size=22, font="b", weight=500, color=WHITE, align="c", anchor="m", lh=1.0)
        T(s, x + 32, cy + 282, 120, 28, n, size=20, font="m", color=NAVY, lh=1.0)
        T(s, x + 32, cy + 316, cw - 64, 50, t, size=38, font="d", weight=400, color=INK, lh=1.1)
        T(s, x + 32, cy + 380, cw - 64, 140, d, size=24, color=SLATE_T, lh=1.38)
        if i < 2:
            T(s, x + cw, cy + 110, gap, 40, "→", size=30, font="m", color=NAVY, align="c", anchor="m", lh=1.0)
    footer(s, len(S) + 1, False, "Dữ liệu minh hoạ"); S.append(s)

    # 5 · Một lô từ eDO đến công nợ --------------------------------------
    s = Slide("Một lô", BG("n5-giay-lua"), "Hành trình một lô theo PRD Mục 7 (Điều phối vận tải). Giá trị mẫu hiển nhiên giả.", "light")
    label(s, "[%02d · Một lô hàng]" % (len(S) + 1), False)
    T(s, 120, 126, 1560, 100, "Một lô, từ eDO đến công nợ.", size=68, font="d", weight=300, color=INK, lh=1.1)
    T(s, 120, 236, 1500, 50, "Cùng một số container đi suốt hành trình. Mỗi chặng chỉ nhập một lần.", size=28, color=SLATE_T, lh=1.4)
    legs = [("01", "[eDO]", "Mở hồ sơ", "AI đọc eDO, mở hồ sơ lô hàng. Bạn duyệt."),
            ("02", "[Điều vận]", "Xếp xe, xếp lái", "Đúng mốc cảng; thấy trước mốc lưu container, lưu vỏ."),
            ("03", "[App lái xe]", "Chạy Lệnh", "Nhận việc, chụp chứng từ, ghi chi phí; mất sóng vẫn chạy."),
            ("04", "[EIR]", "Trả vỏ", "AI đọc EIR; hồ sơ cập nhật giờ lấy và trả vỏ."),
            ("05", "[Công nợ]", "Chi phí về đúng lô", "Chi phí, doanh thu gắn đúng lô, sẵn cho bảng kê.")]
    for i, (n, tg, t, d) in enumerate(legs):
        x = 120 + i * 342
        R(s, x, 340, 312, 390, fill=WHITE, a=0.88, line=INK, la=0.14, r=26)
        T(s, x + 28, 368, 100, 26, n, size=20, font="m", color=NAVY, lh=1.0)
        chip(s, x + 28, 408, tg, size=18, h=36, pad=14)
        T(s, x + 28, 474, 256, 80, t, size=30, font="d", weight=400, color=INK, lh=1.15)
        T(s, x + 28, 562, 256, 150, d, size=22, color=SLATE_T, lh=1.38)
        if i < 4: T(s, x + 312, 500, 30, 40, "→", size=26, font="m", color=NAVY, align="c", anchor="m", lh=1.0)
    R(s, 120, 770, 1680, 110, fill=COBALT, r=26)
    T(s, 156, 770, 1000, 110, "Một dữ liệu", size=36, font="d", weight=300, color=WHITE, anchor="m", lh=1.1)
    T(s, 700, 770, 1070, 110, "MSKU 000000-0 · một hồ sơ từ chặng 01 tới 05", size=24, font="m", color=WHITE, anchor="m", lh=1.4, align="r")
    footer(s, len(S) + 1, False, "Dữ liệu minh hoạ"); S.append(s)

    # 5 · Sản phẩm -------------------------------------------------------
    s = Slide("Sản phẩm", BG("n2-cobalt"), "Giao diện minh hoạ theo phong cách thương hiệu; số liệu mẫu, không phải dữ liệu khách.")
    label(s, "[%02d · Sản phẩm]" % (len(S) + 1), c=WHITE)
    T(s, 120, 126, 1500, 100, "Một hồ sơ lô hàng, trên web và trên app.", size=68, font="d", weight=300, color=WHITE, lh=1.1)
    T(s, 120, 236, 1200, 40, "Văn phòng làm trên web. Hiện trường, lái xe làm trên app.", size=28, color=WHITE, lh=1.3)
    # laptop
    R(s, 120, 320, 1100, 600, fill=NIGHT, r=30)
    R(s, 100, 920, 1140, 16, fill=PERI_L, r=8)
    R(s, 142, 342, 1056, 556, fill=PAPER, r=14)
    R(s, 142, 342, 176, 556, fill=SMOKE, r=14)
    for k, nm in enumerate(["Điều phối", "Lệnh vận tải", "Phương tiện", "Công nợ", "Báo cáo"]):
        if k == 0: R(s, 156, 400 + k * 56, 148, 44, fill=COBALT, a=0.14, r=10)
        T(s, 172, 400 + k * 56, 130, 44, nm, size=20, color=INK if k == 0 else SLATE_T, weight=500 if k == 0 else 400, anchor="m", lh=1.0)
    T(s, 350, 370, 700, 50, "Lô hàng · VD-0000", size=36, font="d", weight=300, color=INK, lh=1.1)
    chip(s, 350, 434, "[AI đọc · 3 chứng từ]", size=18, h=36, pad=14)
    field(s, 350, 490, 400, "SỐ CONTAINER", "MSKU 000000-0", fill=LAV)
    field(s, 350, 584, 400, "SỐ VẬN ĐƠN", "VD-0000", fill=LAV)
    field(s, 350, 678, 400, "HẠN LẤY CONTAINER", "00/00/0000", fill=WHITE, line=INK)
    field(s, 780, 490, 392, "CHỨNG TỪ", "Booking Note · eDO · EIR", fill=WHITE, line=INK)
    field(s, 780, 584, 392, "TRẠNG THÁI", "Chờ duyệt", fill=WHITE, line=INK)
    R(s, 780, 686, 392, 56, fill=COBALT, r=28)
    T(s, 780, 686, 392, 56, "Duyệt hồ sơ", size=24, weight=500, color=WHITE, align="c", anchor="m", lh=1.0)
    x = 350
    for k, (t_, on) in enumerate([("Nhận", 1), ("Đọc", 1), ("Duyệt", 2), ("Điều phối", 0)]):
        x += chip(s, x, 796, t_, color=COBALT if on else SLATE_T, fill=COBALT, a=0.14 if on == 2 else 0, size=18, h=38, pad=16, weight=500 if on == 2 else 400) + 14
        if k < 3: T(s, x - 8, 796, 24, 38, "›", size=22, font="m", color=SLATE_T, align="c", anchor="m", lh=1.0); x += 22
    # phone
    R(s, 1380, 270, 340, 660, fill=NIGHT, r=58)
    R(s, 1394, 284, 312, 632, fill=PAPER, r=46)
    R(s, 1496, 298, 108, 28, fill=NIGHT, r=14)
    T(s, 1420, 352, 260, 44, "Hồ sơ lô hàng", size=30, font="d", weight=300, color=INK, lh=1.1)
    chip(s, 1420, 406, "[eDO] đã đọc · 4 trường", size=16, h=34, pad=12)
    field(s, 1420, 462, 260, "SỐ CONTAINER", "MSKU 000000-0", fill=LAV, h=76, vs=22, ks=15)
    field(s, 1420, 552, 260, "CẢNG DỠ", "Cảng mẫu", fill=LAV, h=76, vs=22, ks=15)
    field(s, 1420, 642, 260, "HẠN LẤY CONT", "00/00/0000", fill=WHITE, h=76, vs=22, ks=15, line=INK)
    R(s, 1420, 744, 260, 56, fill=COBALT, r=28)
    T(s, 1420, 744, 260, 56, "Duyệt hồ sơ", size=22, weight=500, color=WHITE, align="c", anchor="m", lh=1.0)
    chip(s, 1800, 226, "[Chạy khi mất sóng]", color=WHITE, fill=NIGHT, a=0.8, size=20, h=48, line=PERI, pad=20, align="r")
    footer(s, len(S) + 1, True, "Dữ liệu minh hoạ", c=WHITE); S.append(s)

    # 6 · Nền tảng -------------------------------------------------------
    s = Slide("Nền tảng", BG("n1-chamdem"), "Nguồn: PRD Mục 6 (theme + gói). Cây dầu và Nhân sự bỏ khỏi deck vì còn mở (PRD OQ-13).")
    label(s, "[%02d · Nền tảng]" % (len(S) + 1))
    T(s, 120, 126, 1500, 100, "AI nằm trên một nền tảng vận hành đủ đầy.", size=68, font="d", weight=300, color=WHITE, lh=1.1)
    T(s, 120, 236, 1400, 90, "Các module dùng chung một dữ liệu: chi phí gắn đúng lô và đúng đầu xe, không nhập lại.",
      size=26, color=PERI_L, lh=1.4)
    R(s, 120, 372, 1680, 104, fill=NIGHT, a=0.6, line=PERI, la=0.5, r=26, blur=14)
    chip(s, 152, 400, "[AI]", color=PERI, size=22, h=48, pad=18)
    T(s, 260, 372, 560, 104, "AI đọc chứng từ", size=36, font="d", weight=400, color=WHITE, anchor="m", lh=1.1)
    T(s, 820, 372, 950, 104, "Booking Note · eDO · EIR · phiếu cân · tờ khai có QR  →  hồ sơ lô hàng", size=24, color=PERI_L, anchor="m", lh=1.35)
    mods = [("Điều phối vận tải", "Lõi", "Xếp xe, xếp lái đúng mốc cảng; giữ danh sách việc ePort và kết quả."),
            ("Phương tiện", "Lõi", "Hồ sơ xe, bàn giao, thu hồi; nối điều vận với xưởng."),
            ("App lái xe", "Lõi", "Nhận việc, chụp chứng từ, ghi chi phí tại hiện trường; chạy cả khi mất sóng."),
            ("Công nợ theo lô", "Lõi", "Chi phí, doanh thu gắn đúng lô hàng để lập bảng kê, công nợ."),
            ("Nền dùng chung", "Lõi", "Tài khoản, phân quyền theo chi nhánh, nhắc việc, xem quy trình dạng cây."),
            ("Xưởng", "Gói", "Mua hàng, kho phụ tùng, lệnh sửa chữa, thanh toán, báo cáo xưởng.")]
    tw_, tg = 540, 30
    for i, (t, tag, d) in enumerate(mods):
        x = 120 + (i % 3) * (tw_ + tg); y = 506 + (i // 3) * 220
        R(s, x, y, tw_, 190, fill=NIGHT, a=0.55 if tag == "Gói" else 0.7, line=PERI, la=0.35, r=24, blur=14)
        T(s, x + 32, y + 28, 360, 44, t, size=32, font="d", weight=400, color=WHITE, lh=1.1)
        chip(s, x + tw_ - 28, y + 26, "[%s]" % tag, color=PERI if tag == "Lõi" else WHITE, size=18, h=36, pad=14, align="r")
        T(s, x + 32, y + 88, tw_ - 64, 90, d, size=22, color=PERI_L, lh=1.38)
    footer(s, len(S) + 1); S.append(s)

    # 7 · Làm cho cảng Việt ----------------------------------------------
    s = Slide("Cảng Việt", BG("n5-giay-lua"), "Nguồn: PRD Mục 4 và Non-goals (không kết nối máy với ePort; hỗ trợ danh sách việc ePort).", "light")
    label(s, "[%02d · Làm cho thực tế cảng Việt]" % (len(S) + 1), False)
    T(s, 120, 126, 1560, 150, "Làm cho thực tế cảng Việt, không bẻ phần mềm nước ngoài cho vừa.", size=62, font="d", weight=300, color=INK, lh=1.14)
    cards = [("6 mẫu quy trình", "FCL, LCL/CFS, hàng air; mỗi loại có xuất và nhập. Chọn mẫu, không dựng lại từ đầu."),
             ("Danh mục cảng, bãi Việt Nam", "Có thuộc tính ePort, dùng chung mọi khách. Phần mềm hỗ trợ danh sách việc ePort và lưu kết quả."),
             ("App chạy khi mất sóng", "Lái xe ở cảng, bãi và trên đường vẫn nhận việc, chụp chứng từ, ghi chi phí."),
             ("Cấu hình theo khách", "Tham số, tên gọi, danh mục, bật/tắt gói. Không sửa code cho từng khách.")]
    for i, (t, d) in enumerate(cards):
        x = 120 + (i % 2) * 860; y = 330 + (i // 2) * 320
        R(s, x, y, 820, 280, fill=WHITE, a=0.88, line=INK, la=0.14, r=28)
        chip(s, x + 36, y + 32, "[0%d]" % (i + 1), size=18, h=36, pad=14)
        T(s, x + 36, y + 90, 748, 48, t, size=38, font="d", weight=400, color=INK, lh=1.1)
        T(s, x + 36, y + 150, 748, 110, d, size=25, color=SLATE_T, lh=1.4)
    footer(s, len(S) + 1, False); S.append(s)

    # 8 · Bằng chứng -----------------------------------------------------
    s = Slide("Bằng chứng", BG("n2-cobalt"), "Cách trích: 'một doanh nghiệp vận tải container khoảng 110.000 lô/năm' (DEC-060). Không nêu tên, logo khách. Số này là quy mô vận hành, không gắn vào AI.")
    label(s, "[%02d · Đã chạy thật]" % (len(S) + 1), c=WHITE)
    T(s, 112, 190, 980, 250, "~110.000", size=210, font="d", weight=300, color=WHITE, lh=1.05)
    T(s, 120, 440, 900, 80, "lô hàng mỗi năm", size=56, font="d", weight=300, color=WHITE, lh=1.1)
    T(s, 120, 540, 900, 140, "Nền tảng vận hành đã chạy thật tại một doanh nghiệp vận tải container.", size=32, color=WHITE, lh=1.4)
    R(s, 1100, 200, 700, 330, fill=NIGHT, a=0.6, line=PERI, la=0.5, r=28, blur=14)
    chip(s, 1140, 236, "[Khách tham chiếu · ẩn danh]", color=PERI, size=18, h=38, pad=16)
    T(s, 1140, 300, 620, 200, "[chờ: nhận xét ngắn của khách tham chiếu; chỉ dùng khi khách đồng ý]", size=34, font="d", weight=300, color=WHITE, lh=1.35)
    R(s, 120, 740, 1680, 150, fill=NIGHT, a=0.5, line=PERI, la=0.35, r=24, blur=14)
    T(s, 156, 766, 1610, 110, [[("Đọc đúng con số. ", {"weight": 600}), "Đây là quy mô vận hành của nền tảng, không phải số lô AI đã đọc."],
                               "[chờ: số liệu AI đọc chứng từ (độ chính xác, thời gian xử lý) khi có đo]"],
      size=26, color=WHITE, lh=1.45, gap=10)
    footer(s, len(S) + 1, c=WHITE); S.append(s)

    # 9 · Một lõi, mỗi khách một cấu hình --------------------------------
    s = Slide("Cấu hình", BG("n5-giay-lua"), "Nguồn: .claude/rules/saas-layer.md Mục 2. Bốn tầng: Lõi, Cấu hình, Gói, Riêng.", "light")
    label(s, "[%02d · Một sản phẩm, nhiều khách]" % (len(S) + 1), False)
    T(s, 120, 126, 1500, 100, "Một lõi, mỗi khách một cấu hình.", size=72, font="d", weight=300, color=INK, lh=1.1)
    T(s, 120, 244, 1500, 90, "Khách thứ hai nhận cùng một sản phẩm. Khác biệt nằm ở tham số, không nằm ở mã nguồn.", size=28, color=SLATE_T, lh=1.4)
    tiers = [("Lõi", "Đúng với mọi doanh nghiệp cùng ngành.", "Viết sẵn trong sản phẩm, mọi khách dùng chung."),
             ("Cấu hình", "Cùng quy tắc, mỗi khách một con số, danh sách, tên gọi hoặc bật/tắt.", "Đọc từ tham số theo khách, có mặc định."),
             ("Gói", "Một nhóm khách cần, ví dụ gói Xưởng.", "Module bật theo hợp đồng."),
             ("Riêng một khách", "Chỉ một khách cần.", "Dữ liệu cấu hình, kết nối riêng hoặc dịch vụ tuỳ chỉnh; không sửa lõi.")]
    for i, (t, m, h_) in enumerate(tiers):
        y = 380 + i * 138
        base = (i == 0)
        R(s, 120, y, 1680, 122, fill=COBALT if base else WHITE, a=1 if base else 0.88, line=None if base else INK, la=0.14, r=26)
        tc, bc, sc = (WHITE, WHITE, PERI_L) if base else (INK, INK, SLATE_T)
        T(s, 156, y, 330, 122, t, size=34, font="d", weight=400, color=tc, anchor="m", lh=1.1)
        T(s, 500, y, 640, 122, m, size=25, color=bc, anchor="m", lh=1.35)
        T(s, 1180, y, 580, 122, h_, size=24, color=sc if not base else "#DCE1FF", anchor="m", lh=1.35)
    footer(s, len(S) + 1, False); S.append(s)

    # 10 · Ba điều giữ ---------------------------------------------------
    s = Slide("Ba giá trị", BG("n6-muc-cobalt"), "Giá trị cốt lõi: Minh bạch · Đáng tin cậy · Đổi mới (brief Mục 4). 'AI agent' chỉ ở dạng hướng đi.")
    label(s, "[%02d · Điều chúng tôi giữ]" % (len(S) + 1))
    T(s, 120, 126, 1500, 100, "Ba điều chúng tôi giữ.", size=72, font="d", weight=300, color=WHITE, lh=1.1)
    vals = [("Minh bạch", "AI đề xuất,\nbạn quyết định.", ["Bạn duyệt hồ sơ trước khi dữ liệu đi tiếp.", "Ai nhận việc gì, làm tới đâu, ảnh chứng từ ở đâu đều tra lại được."]),
            ("Đáng tin cậy", "Đã chạy thật,\nkể cả khi mất sóng.", ["Vận hành ở quy mô khoảng 110.000 lô/năm tại một doanh nghiệp.", "App vẫn chạy ở cảng, bãi, trên đường."]),
            ("Đổi mới", "Đi trước về AI,\ncó cơ sở.", ["Hôm nay: AI đọc chứng từ Việt vào hồ sơ.", "Hướng tới: AI agent làm thay việc lặp, người duyệt điểm quyết định."])]
    for i, (v, st, bl) in enumerate(vals):
        x = 120 + i * 570
        R(s, x, 300, 540, 560, fill=NIGHT, a=0.55, line=PERI, la=0.4, r=30, blur=14)
        chip(s, x + 36, 336, "[%s]" % v, color=PERI, size=20, h=40, pad=16)
        T(s, x + 36, 410, 470, 130, st, size=40, font="d", weight=300, color=WHITE, lh=1.18)
        R(s, x + 36, 566, 468, 2, fill=PERI, a=0.4)
        T(s, x + 36, 590, 468, 250, bl, size=24, color=PERI_L, lh=1.42, gap=16)
    footer(s, len(S) + 1); S.append(s)

    # 11 · Những điều bạn sẽ hỏi ----------------------------------------
    s = Slide("Câu hỏi của bạn", BG("n5-giay-lua"), "Trang này cố ý để chỗ trống nhìn thấy được: chưa có tài liệu nguồn cho bảo mật, SLA, triển khai, giá. Điền trước khi gửi khách.", "light")
    label(s, "[%02d · Trước khi bạn tin chúng tôi]" % (len(S) + 1), False)
    T(s, 120, 126, 1500, 100, "Những điều bạn sẽ hỏi chúng tôi.", size=72, font="d", weight=300, color=INK, lh=1.1)
    T(s, 120, 244, 1500, 50, "Phần chưa chốt được đánh dấu rõ. Chúng tôi không điền cho đẹp.", size=28, color=SLATE_T, lh=1.4)
    T(s, 520, 330, 600, 28, "HÔM NAY CHÚNG TÔI NÓI ĐƯỢC", size=18, font="m", color=SLATE_T, ls=0.08, lh=1.0)
    T(s, 1200, 330, 600, 28, "SẼ CUNG CẤP TRƯỚC KHI KÝ", size=18, font="m", color=SLATE_T, ls=0.08, lh=1.0)
    rows = [("Phân quyền", "Admin của bạn quản lý tài khoản, nhóm quyền, danh mục; mỗi người vào đúng chi nhánh được cấp.", "[chờ: chuẩn bảo mật]"),
            ("Dữ liệu của bạn", "Một dữ liệu dùng chung cho cả vận hành của bạn.", "[chờ: nơi lưu trữ, sao lưu]"),
            ("Mức dịch vụ", "Cam kết và giờ hỗ trợ ghi trong hợp đồng.", "[chờ: cam kết, giờ hỗ trợ]"),
            ("Triển khai", "Cấu hình theo khách, không sửa code.", "[chờ: các bước, thời gian]"),
            ("Giá", "—", "[chờ: hình thức báo giá]")]
    for i, (t, a_, b_) in enumerate(rows):
        y = 372 + i * 114
        R(s, 120, y, 1680, 2, fill=INK, a=0.16)
        T(s, 120, y + 8, 380, 100, t, size=32, font="d", weight=400, color=INK, anchor="m", lh=1.1)
        T(s, 520, y + 8, 620, 100, a_, size=22, color=INK, anchor="m", lh=1.35)
        T(s, 1200, y + 8, 600, 100, b_, size=22, font="m", color=NAVY, anchor="m", lh=1.4)
    R(s, 120, 372 + 5 * 114, 1680, 2, fill=INK, a=0.16)
    footer(s, len(S) + 1, False); S.append(s)

    # 12 · Lộ trình / tầm nhìn ------------------------------------------
    s = Slide("Tầm nhìn", BG("n3-chamtim"), "Tầm nhìn 3–5 năm và dài hạn: brief Mục 4. Đây là hướng đi, không phải cam kết ngày giao. Không hứa màn lãi lỗ theo lô (PRD OQ-3).")
    label(s, "[%02d · Hướng đi]" % (len(S) + 1))
    T(s, 120, 126, 1560, 200, "Từ vận hành bằng kinh nghiệm sang vận hành bằng dữ liệu và AI agent.", size=62, font="d", weight=300, color=WHITE, lh=1.14)
    R(s, 150, 466, 1620, 2, fill=PERI, a=0.55)
    stages = [("Hôm nay", "AI đọc chứng từ Việt vào hồ sơ. Các module chung một dữ liệu. Cấu hình theo khách.", False),
              ("Tiếp theo", "[chờ: lộ trình sản phẩm; mốc và thứ tự]", True),
              ("3–5 năm", "AI agent đề xuất và làm thay việc lặp; người duyệt điểm quyết định.", False),
              ("Dài hạn", "Đích dài hạn: trở thành chuẩn ngành logistics khu vực. Đây là điều chúng tôi hướng tới.", False)]
    for i, (t, d, ph) in enumerate(stages):
        x = 120 + i * 430
        R(s, x + 14, 452, 30, 30, fill=NIGHT if ph else WHITE, line=PERI if ph else None, lw=2, r=15)
        chip(s, x, 520, "[%s]" % t, color=WHITE, size=22, h=44, pad=18)
        T(s, x, 600, 400, 260, d, size=26, font="b", color=WHITE if not ph else PERI_L, lh=1.42)
    T(s, 120, 930, 1500, 36, "Hướng đi của chúng tôi, không phải cam kết ngày giao.", size=22, font="m", color=PERI_L, lh=1.0)
    footer(s, len(S) + 1); S.append(s)

    # Thử trên lô hàng của bạn -------------------------------------------
    s = Slide("Chạy thử", BG("n6-muc-cobalt"), "Phạm vi, thời lượng, tiêu chí thành công chưa chốt: founder điền. Tiêu chí đo cùng khách, không hứa số trước.")
    label(s, "[%02d · Chạy thử cùng bạn]" % (len(S) + 1))
    T(s, 120, 126, 1560, 100, "Thử trên lô hàng của bạn.", size=72, font="d", weight=300, color=WHITE, lh=1.1)
    T(s, 120, 244, 1500, 50, "Bạn mang vài chứng từ thật. Chúng tôi cho bạn xem chúng vào hồ sơ như thế nào.", size=28, color=PERI_L, lh=1.4)
    cols = [("Phạm vi", "Một nhóm lô hàng của bạn, từ chứng từ tới hồ sơ.", "[chờ: số lô, loại chứng từ]"),
            ("Thời lượng", "Đủ để bạn so với cách làm hiện tại.", "[chờ: số ngày hoặc số tuần]"),
            ("Tiêu chí thành công", "Chúng tôi chọn cùng bạn trước khi bắt đầu, ví dụ thời gian nhập liệu, số trường phải sửa lại.", "[chờ: chỉ số và ngưỡng]")]
    for i, (t, d, ph_) in enumerate(cols):
        x = 120 + i * 570
        R(s, x, 350, 540, 480, fill=NIGHT, a=0.55, line=PERI, la=0.4, r=30, blur=14)
        chip(s, x + 36, 386, "[0%d]" % (i + 1), color=PERI, size=20, h=40, pad=16)
        T(s, x + 36, 456, 470, 60, t, size=38, font="d", weight=300, color=WHITE, lh=1.15)
        R(s, x + 36, 530, 468, 2, fill=PERI, a=0.4)
        T(s, x + 36, 554, 468, 170, d, size=26, color=PERI_L, lh=1.42)
        T(s, x + 36, 740, 468, 60, ph_, size=22, font="m", color=WHITE, lh=1.4)
    footer(s, len(S) + 1); S.append(s)

    # 13 · Về chúng tôi --------------------------------------------------
    s = Slide("Về chúng tôi", BG("n4-periwinkle"), "Câu chuyện tên: DEC-072 giữ cả hai nghĩa Na Uy. Brand-strategy Mục 4 khuyến nghị người bản ngữ kiểm trước khi in.", "light")
    label(s, "[%02d · Về chúng tôi]" % (len(S) + 1), False)
    T(s, 120, 140, 1000, 330, "innvie =\ninnovative +\nVietnamese.", size=96, font="d", weight=300, color=INK, lh=1.08)
    T(s, 1100, 160, 700, 380, "Sự sáng tạo và niềm tự hào Việt Nam của thế hệ trẻ phát triển nhanh, mạnh mẽ, luôn hướng tới đổi mới. Trong tiếng Na Uy, innvie còn nghĩa là cống hiến, và khánh thành, khai mở: đưa điều mới vào vận hành.",
      size=28, color=INK, lh=1.5)
    R(s, 120, 600, 1680, 2, fill=INK, a=0.3)
    T(s, 120, 640, 1000, 130, "Invlogis = innvie + logistics.", size=64, font="d", weight=300, color=INK, lh=1.1)
    T(s, 1100, 650, 700, 200, "Chúng tôi dồn sức vào một sản phẩm cho logistics Việt Nam, rồi đưa nó vào vận hành thật.", size=28, color=INK, lh=1.5)
    T(s, 120, 860, 1500, 40, "Invlogis, sản phẩm của innvie.  [chờ: tên pháp nhân đầy đủ · địa chỉ · MST]", size=22, font="m", color=INK, lh=1.3)
    footer(s, len(S) + 1, False); S.append(s)

    # 14 · Kết -----------------------------------------------------------
    s = Slide("Kết", BG("n1-chamdem"), "Trang cuối: lockup 'by innvie' + chữ ký pháp nhân. Hình thức buổi demo/pilot chưa chốt.")
    label(s, "[%02d · Bước tiếp theo]" % (len(S) + 1))
    T(s, 120, 150, 1500, 260, "Khai mở cách\nvận hành mới.", size=112, font="d", weight=300, color=WHITE, lh=1.08)
    T(s, 120, 450, 1000, 150, "Mang đến vài chứng từ thật của bạn. Chúng tôi cho bạn xem hồ sơ lô hàng hiện ra.", size=32, color=PERI_L, lh=1.42)
    T(s, 120, 626, 1100, 40, "[chờ: xác nhận hình thức buổi demo hoặc chạy thử]", size=22, font="m", color=PERI_L, lh=1.0)
    for i, (k, v) in enumerate([("EMAIL", "[chờ: email]"), ("ĐIỆN THOẠI", "[chờ: sđt]"), ("WEBSITE", "[chờ: website]")]):
        x = 120 + i * 440
        R(s, x, 720, 400, 2, fill=PERI, a=0.5)
        T(s, x, 740, 400, 26, k, size=18, font="m", color=PERI_L, ls=0.08, lh=1.0)
        T(s, x, 776, 400, 44, v, size=30, font="d", weight=300, color=WHITE, lh=1.1)
    IMG(s, LOGO("invlogis-by-innvie-reverse"), 120, 890, 110 * 2.6856, 110)
    T(s, 560, 940, 1240, 40, "Invlogis là sản phẩm của [chờ: tên pháp nhân innvie] · [chờ: địa chỉ] · [chờ: MST]", size=20, font="m", color=PERI_L, align="r", lh=1.4)
    S.append(s)
    return S
