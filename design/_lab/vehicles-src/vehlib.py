"""Hàm dùng chung cho gen_ai.py: cắt viền, xoá đốm, bóng đổ, ghi manifest.
Ảnh ra: design/_lab/assets/vehicles/b-ai/t{mã loại}.png (đại diện loại), n{mã tên}.png (riêng 1 tên), combo*.png."""
import json, pathlib, re
import numpy as np
from PIL import Image, ImageFilter

LAB = pathlib.Path(__file__).resolve().parent.parent
ASSETS = LAB / "assets" / "vehicles"


def drop_specks(im: Image.Image, min_ratio=0.01) -> Image.Image:
    """Xoá đốm rời nhỏ (dấu góc ảnh, bụi tách nền): giữ vùng liền nhau ≥ 1% diện tích vật thể."""
    from PIL import ImageDraw
    a = np.array(im.split()[-1])
    m = Image.fromarray(((a > 8) * 255).astype(np.uint8), "L").copy()
    total = (a > 8).sum()
    if not total:
        return im
    ys, xs = np.where(np.asarray(m) == 255)
    small = np.zeros(a.shape, bool)
    seen = np.zeros(a.shape, bool)
    for y, x in zip(ys[::97], xs[::97]):          # lấy mẫu điểm hạt giống, đủ phủ mọi vùng ≥ vài trăm px
        if seen[y, x]:
            continue
        before = np.asarray(m) == 255
        ImageDraw.floodfill(m, (int(x), int(y)), 100)
        reg = (np.asarray(m) == 100) & before
        seen |= reg
        if reg.sum() < total * min_ratio:
            small |= reg
        m = Image.fromarray(np.where(reg, 50, np.asarray(m)).astype(np.uint8), "L").copy()
    # đốm nhỏ hơn bước lấy mẫu: vùng còn 255 chưa được thăm
    small |= (np.asarray(m) == 255) & ~seen
    # vật rời ở XA thân xe (vd đèn studio lọt khung) → bỏ. Nối các phần sát nhau trước (nới 1,5% cạnh dài)
    # để cabin / gầm / gương không bị coi là vật rời.
    keep = (a > 8) & ~small
    if keep.any():
        r = max(3, int(max(a.shape) * 0.015)) | 1
        dil = Image.fromarray((keep * 255).astype(np.uint8), "L").filter(ImageFilter.MaxFilter(r)).copy()
        ys2, xs2 = np.where(np.asarray(dil) == 255)
        best, best_n = None, 0
        for y, x in zip(ys2[::997], xs2[::997]):
            if dil.getpixel((int(x), int(y))) != 255:
                continue
            ImageDraw.floodfill(dil, (int(x), int(y)), 77)
            reg = np.asarray(dil) == 77
            if reg.sum() > best_n:
                best, best_n = reg, reg.sum()
            dil = Image.fromarray(np.where(reg, 30, np.asarray(dil)).astype(np.uint8), "L").copy()
        if best is not None:
            small |= keep & ~best
    out = np.array(im)
    out[small, 3] = 0
    return Image.fromarray(out, "RGBA")


def trim(im: Image.Image, pad_ratio=0.03) -> Image.Image:
    im = drop_specks(im)
    a = np.array(im.split()[-1])
    ys, xs = np.where(a > 8)
    if not len(xs):
        raise ValueError("ảnh rỗng sau khi tách nền")
    x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
    p = int(max(x1 - x0, y1 - y0) * pad_ratio)
    W, H = im.size
    return im.crop((max(0, x0 - p), max(0, y0 - p), min(W, x1 + p + 1), min(H, y1 + p + 1)))


def add_contact_shadow(im: Image.Image, strength=0.5) -> Image.Image:
    """Bóng tiếp đất bám theo điểm chạm đất thật (không phải elip chung).
    - Mép dưới vật theo từng cột (ybot) → bao lồi dưới = 'đường mặt đất' nối các điểm chạm (bánh, chân, đế).
    - Cột chạm đất (ybot ≈ mặt đất) → bóng đậm, mỏng; cột hở gầm (ybot cao hơn) → nhạt dần theo khoảng hở.
    - Thêm 1 lớp bóng môi trường rất nhạt, rồi làm mờ. Bóng nằm dưới vật, sát mép, không có khe."""
    W, H = im.size
    a = np.asarray(im.split()[-1]).astype(np.float32) / 255
    solid = a > 0.5
    cols = np.where(solid.any(axis=0))[0]
    if len(cols) < 2:
        return im
    ybot = np.full(W, -1.0)
    for x in cols:
        ybot[x] = np.where(solid[:, x])[0].max()
    pts = [(int(x), -ybot[x]) for x in cols]                 # y hướng lên để dùng bao lồi dưới quen thuộc
    hull = []
    for p in pts:
        while len(hull) >= 2 and (hull[-1][0]-hull[-2][0])*(p[1]-hull[-2][1]) - (hull[-1][1]-hull[-2][1])*(p[0]-hull[-2][0]) <= 0:
            hull.pop()
        hull.append(p)
    hx = np.array([h[0] for h in hull], float); hy = -np.array([h[1] for h in hull], float)
    ground = np.interp(np.arange(W), hx, hy)
    obj_h = float(ground.max() - np.where(solid.any(axis=1))[0].min())
    pad = int(obj_h * 0.08) + 4
    sh = np.zeros((H + pad, W), np.float32)
    yy = np.arange(H + pad)[:, None]
    gap = np.clip(ground - ybot, 0, None)
    contact = np.where(ybot >= 0, np.exp(-gap / (obj_h * 0.035)), 0)          # 1 dưới bánh, →0 khi hở gầm
    t_c, t_a = obj_h * 0.022, obj_h * 0.05
    d = yy - ground[None, :]
    inside = (np.arange(W) >= cols.min()) & (np.arange(W) <= cols.max())
    sh += np.where((d > -t_c) & (d < t_c), contact[None, :], 0) * strength          # bóng tiếp đất
    sh += np.where((d > -t_a) & (d < t_a * 0.6) & inside[None, :], 0.10, 0)         # bóng môi trường nhạt
    m = Image.fromarray((np.clip(sh, 0, 1) * 255).astype(np.uint8), "L").filter(ImageFilter.GaussianBlur(float(max(1.5, obj_h * 0.012))))
    out = Image.new("RGBA", (W, H + pad), (0, 0, 0, 0))
    blk = Image.new("RGBA", (W, H + pad), (0, 0, 0, 255)); blk.putalpha(m)
    out.alpha_composite(blk)
    out.alpha_composite(im, (0, 0))
    return trim(out, 0.02)


# Vùng lấy nét cho ảnh thu nhỏ: (x0, x1) theo tỉ lệ bề ngang ảnh đã cắt viền. th = ô danh sách 56px, xs = ô 40px.
# Xe dài lấy đầu xe (bên phải) hoặc cụm bánh (mooc, bên trái); đồ vật gọn lấy cả.
FOCUS = {
 "t01": {"th": (0, .55), "xs": (0, .42)}, "t02": {"th": (.28, 1), "xs": (.45, 1)},
 "t03": {"th": (.42, 1), "xs": (.6, 1)},  "t06": {"th": (.35, 1), "xs": (.5, 1)},
 "t07": {"th": (.35, 1), "xs": (.55, 1)}, "combo": {"th": (.55, 1), "xs": (.74, 1)},
}


# Ảnh theo tên / nhóm dùng vùng lấy nét của loại tương ứng
FOCUS_AS = {"n01": "t01", "n03": "t01", "n04": "t01", "n05": "t02", "n08": "t02", "n09": "t02",
            "g-truck-s": "t03", "g-truck-l": "t03", "g-truck-l3": "t03"}


def make_thumb(im: Image.Image, name: str, size: str, S=256) -> Image.Image:
    name = re.sub(r"-(q|s)$", "", name)
    key = FOCUS_AS.get(name, "combo" if name.startswith("combo") else name)
    x0f, x1f = FOCUS.get(key, {}).get(size, (0, 1))
    W, H = im.size
    c = im.crop((int(W * x0f), 0, int(W * x1f), H))
    bb = c.split()[-1].point(lambda v: 255 if v > 40 else 0).getbbox()
    if bb:
        c = c.crop((bb[0] if x0f == 0 else 0, bb[1], bb[2] if x1f == 1 else c.width, bb[3]))
    bleed_l, bleed_r = x0f > 0, x1f < 1
    fill_w = S * (1.0 if (bleed_l or bleed_r) else (.80 if size == "th" else .92))
    fill_h = S * (.66 if size == "th" else .80)
    k = min(fill_w / c.width, fill_h / c.height)
    c = c.resize((max(1, round(c.width * k)), max(1, round(c.height * k))), Image.LANCZOS)
    x = 0 if bleed_l and not bleed_r else (S - c.width if bleed_r and not bleed_l else (S - c.width) // 2)
    y = round(S * (.88 if size == "th" else .92)) - c.height
    out = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    out.alpha_composite(c, (x, max(0, y)))
    return out


# Khung chuẩn theo mặt cắt — mọi ảnh cùng khổ, cùng lề, cùng đường đáy (đế bánh) để ráp UI đồng nhất.
FRAME = {"q": (1600, 1000, .90, .82, .94), "s": (1800, 720, .92, .80, .93)}   # W, H, tối đa rộng, tối đa cao, đường đáy


def frame(im: Image.Image, cut: str) -> Image.Image:
    W, H, mw, mh, base = FRAME[cut]
    k = min(W * mw / im.width, H * mh / im.height)
    o = im.resize((max(1, round(im.width * k)), max(1, round(im.height * k))), Image.LANCZOS)
    c = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    c.alpha_composite(o, ((W - o.width) // 2, round(H * base) - o.height))
    return c


def save(im: Image.Image, src: str, name: str, max_w=1400) -> pathlib.Path:
    d = ASSETS / src
    d.mkdir(parents=True, exist_ok=True)
    m = re.search(r"-(q|s)(-\d+)?(-[a-z]+)?$", name)
    if m or name.endswith("-top"):   # ảnh theo quy chuẩn: cắt SÁT mép thật (không viền) — chiều dài/chiều cao ảnh = kích thước thật để ghép tổ hợp
        bb = im.split()[-1].point(lambda v: 255 if v > 24 else 0).getbbox()
        if bb: im = im.crop(bb)
        max_w = 1800
    if im.width > max_w:
        im = im.resize((max_w, round(im.height * max_w / im.width)), Image.LANCZOS)
    p = d / f"{name}.png"
    im.save(p, optimize=True)
    if re.fullmatch(r"(t\d\d|n\d\d|g-[a-z0-9-]+?|combo(-0|-2|-40|-45)?)(-q|-s)?", name):                       # ảnh chính → kèm ảnh thu nhỏ
        for sz in ("th", "xs"):
            make_thumb(im, name, sz).save(d / f"{name}-{sz}.png", optimize=True)
    write_manifest()
    return p


def write_manifest():
    m = {}
    for src in ("b-ai",):
        d = ASSETS / src
        m[src] = {p.stem: f"assets/vehicles/{src}/{p.name}" for p in sorted(d.glob("*.png"))} if d.exists() else {}
    (ASSETS / "manifest.js").write_text(
        "/* Máy sinh bởi vehicles-src/vehlib.py — không sửa tay. */\nwindow.VEH_ASSETS=" + json.dumps(m, ensure_ascii=False, indent=1) + ";\n",
        encoding="utf-8")
