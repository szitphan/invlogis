"""Hướng B — sinh ảnh phương tiện bằng Gemini (Nano Banana), tách nền xanh, thêm bóng đổ → PNG trong suốt.

Khoá API: biến môi trường GEMINI_API_KEY, hoặc dòng `GEMINI_API_KEY=...` trong design/_lab/.env.local
hoặc design/.env.local (.env.* đã nằm trong .gitignore — khoá không lên git).
Chạy:
  python3 design/_lab/vehicles-src/gen_ai.py                 # cả 9 loại
  python3 design/_lab/vehicles-src/gen_ai.py t02 t03         # chỉ vài loại
  python3 design/_lab/vehicles-src/gen_ai.py t02 --ref refs/user/u06.png --model gemini-3-pro-image-preview
Ảnh gốc (nền xanh) giữ ở vehicles-src/raw/ để soát; ảnh dùng ở assets/vehicles/b-ai/.
"""
import argparse, base64, json, os, pathlib, ssl, sys, time, urllib.request, urllib.error
import numpy as np
from PIL import Image
import io
import vehlib

HERE = pathlib.Path(__file__).resolve().parent
API = "https://generativelanguage.googleapis.com/v1beta/models/{m}:generateContent"


def _ssl_ctx():
    """Python cài từ python.org không mang kho chứng chỉ → dùng certifi nếu có, không thì kho của macOS."""
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        return ssl.create_default_context(cafile="/etc/ssl/cert.pem") if os.path.exists("/etc/ssl/cert.pem") else ssl.create_default_context()

VIEW = ("three-quarter front view from the right-hand side, the vehicle's front pointing to the right of the frame, "
        "camera at about 8 degrees elevation, long telephoto lens with minimal perspective distortion")
# ---- Quy chuẩn 2 mặt cắt (refs/vehicle-shot-spec.md) ----
# q = 3/4 trước: đầu xe sang phải, camera lệch ~35° khỏi trục hông về phía đầu xe (thấy mặt trước ~1/3, hông ~2/3),
#     cao ~1,3 m (ngang dưới kính lái, cao 5–7°), tele ~100 mm. Khớp ảnh mẫu refs/angle-q34-user.png.
# s = ngang vuông góc: camera vuông góc với hông xe, ngang tâm bánh (0–2°), đầu xe sang phải, KHÔNG thấy mặt trước.
CUT_VIEW = {
 "q": ("three-quarter front view: the vehicle's front (cab / grille) points to the RIGHT side of the frame and its rear to the LEFT; the camera is turned about 35 degrees "
       "from the side axis toward the front, so the front face takes about one third and the long right-hand side about two thirds "
       "of the visible body; camera height about 1.3 metres (slightly below the windscreen, 5 to 7 degrees looking down); "
       "100 mm telephoto lens, minimal perspective distortion; the whole object fully in frame"),
 "s": ("strict side profile (orthographic-like elevation): the camera is exactly perpendicular to the long side of the object, "
       "at wheel-hub height with 0 to 2 degrees elevation, the front points to the RIGHT of the frame, NO part of the front face "
       "or rear face is visible, wheels appear as perfect circles; long telephoto lens; the whole object fully in frame"),
}
# "Đầu" của vật không phải xe (quay sang phải)
FRONT_OF = {"c40": "the cargo-door end", "c45": "the cargo-door end", "t01": "the kingpin / landing-leg end (front of the trailer)",
            "n01": "the kingpin end", "n03": "the kingpin end", "n04": "the kingpin end", "g-mooc-san": "the kingpin end",
            "t06": "the cargo-door end", "t07": "the refrigeration-unit end", "t08": "the control-panel end",
            "t09": "the open side of the container showing the tank and the pump"}
ANGLE_REF = {"q": HERE.parent / "refs" / "angle-q34-user.png", "s": HERE / "raw" / "t03-s.png"}   # s: ảnh ngang pilot 09/10

STYLE = ("Photorealistic studio product photograph for a logistics app. {subject}. {view}. "
         "Isolated on a perfectly flat, uniform, fully saturated pure chroma-key green background (#00FF00, like a green screen) filling the whole frame, no gradient, no vignette, "
         "no floor, no horizon, no cast shadow, no reflection on the background. Soft large-softbox lighting, "
         "neutral white balance, crisp edges, darkly tinted opaque windows (interior and background not visible through glass), true-to-life proportions and materials, clean unbranded vehicle, "
         "no logos, no text, no license plate characters, no people. The entire object is fully in frame "
         "with generous margin on all sides. Do not use any green color on the object itself. "
         "No studio equipment in frame: no lights, softboxes, stands, cables or props.")

SUBJECT = {
 "t01": "an empty 40-foot skeletal container semi-trailer chassis, dark grey painted steel I-beams, two axles with dual tyres, landing legs lowered, twist locks at the corners, not attached to any truck",
 "t02": "a white heavy-duty cab-over tractor unit, 6x4 with two rear axles, Asian style similar to a Hino 700, fifth-wheel coupling visible on the chassis, no trailer attached",
 "t03": "a medium-duty white cab-over box truck, similar to an Isuzu N-series, with a plain white aluminium dry cargo box",
 "t04": "a Toyota 2.5 tonne diesel counterbalance forklift (Toyota 8FD25 type) with an OPEN operator station: the overhead guard is only four thin black posts and a roof grid, NO cabin, NO glass, NO doors, NO side panels, the seat and steering wheel fully visible from the side; orange-red body sides, dark grey hood and counterweight top, black three-stage mast with load backrest and hydraulic fork positioner, forks lowered, grey solid tyres, orange beacon on top",
 "t05": "a 1.5 tonne electric stand-on reach truck similar to a Komatsu FB15RL: compact short body, operator stands sideways in a small open compartment, tall three-stage mast and forks reaching forward between two long front support legs (outriggers) with small load wheels, body painted deep cobalt blue, black mast and overhead guard, absolutely no white or cream panels",
 "t06": "a standard 20-foot ISO dry cargo shipping container painted plain white, standing alone on the ground (not on any truck or trailer), vertically corrugated steel side walls with NO windows, NO openings and NO panels, dark grey corner posts and corner castings at every corner, closed double cargo doors on the end with vertical locking bars",
 "t07": "a 45-foot high-cube refrigerated reefer shipping container standing alone on the ground (NOT mounted on any truck, chassis or trailer, no wheels), white smooth insulated steel panels, solid sides with NO windows and NO side doors, cargo doors on the rear end, the integrated refrigeration machinery unit (grille, fan, control box) set into the front end wall",
 "t08": "a compact silent diesel generator set of 25 kVA in the style of a Japanese Shindaiwa unit, standing on its flat steel skid base directly on the ground (NO wheels, NO trailer): cream off-white steel canopy with a dark maroon-red roof panel, black steel base frame, hinged side doors with flush black latches, square-grid ventilation openings, small control-panel window on the end",
 "t09": "a containerised fuel station standing on the ground (NOT a truck, NO wheels): a white 20-foot shipping container used as a protective housing, one long side opened with roll-up shutters showing inside a horizontal steel fuel storage tank and a commercial fuel dispenser pump with digital display, hose and nozzle",
 "combo": "a complete container truck combination: a white heavy-duty cab-over 6x4 tractor unit (similar to a Hino 700) coupled to a 40-foot skeletal container semi-trailer with two axles, carrying ONE 20-foot dry shipping container in rust-red corrugated steel locked in the middle of the trailer, landing legs raised",
 "t02-top": "a white heavy-duty semi-truck tractor unit with NO trailer, seen from directly above: short square cab-over cab roof with air deflector at the front, behind it a long exposed black steel chassis frame with a round fifth-wheel coupling plate and two rear axles with dual tyres",
 "combo-45": "a complete container truck combination: a white heavy-duty cab-over 6x4 tractor unit (similar to a Hino 700) coupled to a 45-foot straight skeletal container semi-trailer (not gooseneck) with three axles, carrying ONE 45-foot white refrigerated reefer container whose refrigeration unit is on the front end facing the tractor, landing legs raised",
 "n01": "an empty short 20-foot skeletal container semi-trailer chassis, dark grey steel, two axles with dual tyres, four twist locks, landing legs lowered, not attached to any truck",
 "n03": "an empty 40-foot skeletal container semi-trailer chassis with THREE axles and dual tyres, dark grey steel, twelve twist locks, landing legs lowered, not attached to any truck",
 "n04": "an empty 45-foot straight skeletal container semi-trailer chassis (flat straight main beams, NOT a gooseneck), three axles with dual tyres, dark grey steel, twist locks, landing legs lowered, not attached to any truck",
 "n05": "an older MAZ (Belarus) heavy cab-over tractor unit with a 4x2 axle layout (ONE front steering axle and ONE rear drive axle with dual tyres): flat upright cab face painted plain white, a wide black horizontal-slat grille panel across the lower cab, a light band above the grille, black steel bumper with square headlamps, fifth-wheel visible, no trailer attached",
 "n08": "a Freightliner Cascadia long-nose conventional semi-truck tractor unit: white, sloping aerodynamic hood, large chrome grille with horizontal bars and the Freightliner badge, swept headlamps, grey bumper, high-roof sleeper cab with roof fairing, 6x4, fifth-wheel visible, no trailer attached",
 "n06": "an International ProStar long-nose conventional semi-truck tractor unit (MaxxForce engine): white, rounded aerodynamic hood, tall chrome grille with vertical bars and the diamond International badge, white bumper, high-roof sleeper cab with roof fairing, 6x4, fifth-wheel visible, no trailer attached",
 "n09": "a Dongfeng Chenglong H7 heavy cab-over tractor unit, high-roof wide cab painted plain white with the H7 badge, black grille, 6x4, fifth-wheel visible, no trailer attached",
 "g-truck-s": "a light-duty Isuzu QKR 210 cab-over truck, narrow white cab with black bumper, short silver-grey aluminium closed cargo box, single rear wheels",
 "g-truck-l": "a Thaco Foton Auman AC990 heavy cab-over cargo truck of about 8 to 9 tonnes (older Auman cab): wide flat cab painted plain white with a tall roof deflector, black horizontal-slat grille with the round Foton badge, slotted vents beside the grille, white bumper with rectangular headlamps, two axles with dual rear tyres, long white aluminium closed cargo box",
 "n28": "a Dongfeng Chenglong H5 heavy cab-over cargo truck with an 8x4 FOUR-axle layout (TWO front steering axles and TWO rear drive axles with dual tyres), wide cab painted plain white with roof deflector and black grille, very long white aluminium closed cargo box",
 "n25": "a Dongfeng medium-heavy cab-over cargo truck of about 9 tonnes (Dongfeng B180 type), white cab with a dark grey grille panel, two axles with dual rear tyres, long white aluminium closed cargo box",
 "n26": "a Foton Auman C240 heavy cab-over cargo truck with EXACTLY THREE axles in total: ONE front steering axle under the cab and TWO rear axles close together at the back with dual tyres (6x4); white cab with the V-shaped perforated mesh grille, very long silver-white aluminium closed cargo box",
 "n27": "a Dongfeng Chenglong M3 cab-over cargo truck, cab painted plain white with roof deflector and black honeycomb grille, two axles, long white aluminium cargo box with many hinged side doors along its length",
 "n12": "a TMT Motor (Vietnam) cab-over cargo truck of about 7 to 8 tonnes, cab painted plain white, black grille panel with a chrome bar and the oval TMT badge, wide bumper with a honeycomb insert and square fog lamps, two axles with dual rear tyres, silver-grey aluminium closed cargo box",
 "g-mooc-san": "an empty 40-foot flatbed container semi-trailer (sàn): flat steel deck floor over the whole length with low side rails and twist locks, two axles with dual tyres, dark grey steel, landing legs lowered, not attached to any truck",
 "g-kia": "a Thaco Kia Frontier light cab-over truck (Kia K165 / K140 / K3000 type, Kia Bongo family): narrow cab with a rounded front face, round headlamps set in the corners, chrome Kia grille bar, cab painted plain white, short white aluminium closed cargo box, single rear wheels",
 "n17": "a Hyundai HD72 (Hyundai Mighty) cab-over truck of about 3.5 tonnes: cab painted plain white with a rounded smooth front face, wide grille with the Hyundai badge, large wrap-around headlamps, two axles with dual rear tyres, silver-white aluminium closed cargo box",
 "c40": "a standard 40-foot ISO dry cargo shipping container painted plain white, vertically corrugated steel side walls with NO windows and NO openings, dark grey corner posts and corner castings at every corner, closed double cargo doors on the end with vertical locking bars",
 "c45": "a 45-foot high-cube ISO dry cargo shipping container painted plain white, vertically corrugated steel side walls with NO windows and NO openings, dark grey corner posts and corner castings at every corner, closed double cargo doors on the end with vertical locking bars",
 "n10": "a Thaco Foton Auman AC990 heavy cab-over cargo truck with EXACTLY THREE axles in total: TWO steering axles close together under and just behind the cab, and ONE single rear drive axle with dual tyres at the back (twin-steer 6x2); older Auman cab painted plain white with a tall roof deflector, black horizontal-slat grille with the round Foton badge, long white aluminium closed cargo box",
 "n29": "a Thaco Ollin 700 cab-over cargo truck of about 7 tonnes, white cab with a dark visor band above the windscreen and a roof deflector, chrome grille, two axles, silver-grey aluminium closed cargo box",
 "combo-0": "a complete container truck combination: a white heavy-duty cab-over 6x4 tractor unit (similar to a Hino 700) coupled to an EMPTY 40-foot skeletal container semi-trailer with two axles, no container loaded, twist locks visible, landing legs raised",
 "combo-2": "a complete container truck combination: a white heavy-duty cab-over 6x4 tractor unit (similar to a Hino 700) coupled to a 40-foot skeletal container semi-trailer with two axles, carrying TWO 20-foot dry shipping containers placed end to end (the rear one rust-red, the front one dark blue), landing legs raised",
 "combo-40": "a complete container truck combination: a white heavy-duty cab-over 6x4 tractor unit (similar to a Hino 700) coupled to a 40-foot skeletal container semi-trailer with two axles, carrying ONE 40-foot dry shipping container in dark blue corrugated steel covering the whole trailer, landing legs raised",
}
VIEW_OVR = {
 "combo": "pure side view from the right-hand side, the truck's front pointing to the right of the frame, camera at about 5 degrees elevation, long telephoto lens with minimal perspective distortion",
 "combo-top": "strict top-down orthographic aerial view from directly overhead, the vehicle pointing straight up toward the top of the frame, perfectly centered, no perspective",
 # đồ vật đứng yên không có "đầu xe"
 "t06": "three-quarter view showing the long side and the door end on the right, camera at about 10 degrees elevation, telephoto lens",
 "t07": "three-quarter view showing the long side and the refrigeration-unit end on the right, camera at about 10 degrees elevation, telephoto lens",
 "t08": "three-quarter view, camera at about 12 degrees elevation, telephoto lens",
 "t09": "three-quarter view, camera at about 10 degrees elevation, telephoto lens",
}


# Ảnh thực tế đội xe (user gửi 09/10) — tự đính kèm làm tham chiếu dáng xe khi sinh tên tương ứng
FLEET = HERE.parent / "refs" / "fleet"
REFS = {"t04": "n31-toyota-25t.png", "g-truck-s": "n30-isuzu-qkr210.png", "n29": "n29-ollin-700.png",
        "n27": "n27-chenglong-m3.png", "n26": "n26-auman-c240.png", "g-truck-l": "n10-auman-ac990.png", "n10": "n10-auman-ac990.png",
        "n25": "n25-dongfeng-b180.png", "n09": "n09-chenglong-h7-crop.png", "n12": "n12-tmt-8t-yellow.png",
        "n05": "n05-maz.png", "n06": "n06-maxxforce-prostar.png", "n08": "n08-cascadia.png", "t04": "n31-toyota-25t.png", "t08": "n35-genset-25kva-q34.png", "t02": "n07-hino-700.png"}

ASPECT = {"combo-45": "21:9", "combo": "21:9", "combo-0": "21:9", "combo-2": "21:9", "combo-40": "21:9", "combo-top": "9:16"}


def api_key():
    k = os.environ.get("GEMINI_API_KEY")
    if k:
        return k.strip()
    for env in (HERE.parent / ".env.local", HERE.parent.parent / ".env.local"):   # design/_lab/ hoặc design/
        if env.exists():
            for line in env.read_text().splitlines():
                if line.strip().startswith("GEMINI_API_KEY="):
                    v = line.split("=", 1)[1].strip().strip('"').strip("'")
                    if v:
                        return v
    sys.exit("Thiếu GEMINI_API_KEY (biến môi trường, design/_lab/.env.local hoặc design/.env.local). Lấy khoá ở https://aistudio.google.com/apikey")


LAST_USAGE = {}


def generate(prompt, model, ref=None, aspect="16:9", ref_mode="style", angle_ref=None):
    parts = [{"text": prompt}]
    if angle_ref:
        parts.append({"inline_data": {"mime_type": "image/png", "data": base64.b64encode(pathlib.Path(angle_ref).read_bytes()).decode()}})
        parts[0]["text"] += (" The FIRST attached image is the CAMERA STANDARD for the whole catalogue: copy exactly its camera angle, "
                             "camera height, lens, distance and how the vehicle fills the frame; do not copy its vehicle model.")
    if ref:
        mime = "image/jpeg" if str(ref).lower().endswith((".jpg", ".jpeg")) else "image/png"
        parts.append({"inline_data": {"mime_type": mime, "data": base64.b64encode(pathlib.Path(ref).read_bytes()).decode()}})
        parts[0]["text"] += (" The attached photo shows the REAL vehicle from our fleet: reproduce exactly this vehicle model — same cab shape, "
                             "grille, headlights, bumper, roof deflector, manufacturer badge on the front, cargo body type and proportions — but re-shot as the studio "
                             "product photo described above, from the camera angle described above (not the photo's angle). Use the colours stated in the description above (cabs plain white) even if the photo differs. Remove all company "
                             "logos and lettering on the cargo body, all stickers, papers on the dashboard and the licence plate. Clean, new condition."
                             if ref_mode == "model" else
                             " Match the camera angle, lighting softness and rendering realism of the attached reference image, but not its background.")
    body = {"contents": [{"parts": parts}], "generationConfig": {"responseModalities": ["IMAGE"], "imageConfig": {"aspectRatio": aspect}}}
    req = urllib.request.Request(API.format(m=model), data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json", "x-goog-api-key": api_key()})
    try:
        with urllib.request.urlopen(req, timeout=180, context=_ssl_ctx()) as r:
            data = json.loads(r.read())
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"HTTP {e.code}: {e.read().decode()[:300]}")
    u = data.get("usageMetadata", {})
    LAST_USAGE.clear(); LAST_USAGE.update(u)
    with open(HERE / "usage.log", "a") as f:                       # sổ chi phí: mỗi lượt gọi 1 dòng
        f.write(json.dumps({"t": time.strftime("%Y-%m-%d %H:%M"), "model": model, "usage": u}) + "\n")
    for c in data.get("candidates", []):
        for p in c.get("content", {}).get("parts", []):
            d = p.get("inlineData") or p.get("inline_data")
            if d:
                return Image.open(io.BytesIO(base64.b64decode(d["data"]))).convert("RGB")
    raise RuntimeError("Không có ảnh trong phản hồi: " + json.dumps(data)[:300])


def chroma_key(im: Image.Image) -> Image.Image:
    """Tách nền xanh kể cả khi model trả nền xanh xám có chuyển màu + bóng (không phải #00FF00 thuần).
    1) Điểm 'nền' = lượng xanh lá vượt hẳn đỏ/lam (đo tuyệt đối, không chia tỉ lệ để điểm gần đen không bị đẩy cao); xe trắng/xám/đen gần 0 nên giữ lại.
    2) Chỉ xoá vùng nền NỐI LIỀN với mép ảnh (flood fill) → kính xe ánh xanh bên trong không bị khoét.
    3) Viền: alpha mềm theo độ bão hoà + khử ánh xanh."""
    from PIL import ImageDraw, ImageFilter
    a = np.asarray(im).astype(np.float32) / 255
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    chroma = g - np.maximum(r, b)                      # độ xanh tuyệt đối: nền ≈ .15–.25, xe (trắng/xám/đen) < .04
    green = chroma > 0.02
    # ngưỡng theo độ xanh của nền đo ở viền ảnh: nền xanh xám (~.2) → ~.05–.10; nền xanh đậm (~.8) → ~.28–.48,
    # để sơn trắng ánh xanh không bị khoét
    border = np.concatenate([chroma[:4].ravel(), chroma[-4:].ravel(), chroma[:, :4].ravel(), chroma[:, -4:].ravel()])
    bgc = float(np.median(border[border > 0.02])) if (border > 0.02).any() else 0.2
    lo, hi = max(0.045, bgc * 0.35), max(0.10, bgc * 0.6)
    soft = np.clip((chroma - lo) / (hi - lo), 0, 1)                            # 1 = chắc là nền
    hard = Image.fromarray(((soft > 0.5) * 255).astype(np.uint8), "L").copy()   # copy: ảnh từ numpy là chỉ-đọc, floodfill không ghi được
    H, W = soft.shape
    for x, y in [(0, 0), (W - 1, 0), (0, H - 1), (W - 1, H - 1)] + [(x, 0) for x in range(0, W, 40)] + [(x, H - 1) for x in range(0, W, 40)] \
            + [(0, y) for y in range(0, H, 40)] + [(W - 1, y) for y in range(0, H, 40)]:
        if hard.getpixel((x, y)) == 255:
            ImageDraw.floodfill(hard, (x, y), 128)
    bg = np.asarray(hard) == 128
    # nới vùng nền 2px để ăn viền mềm, chỉ trong vùng có sắc xanh
    grow = np.asarray(Image.fromarray((bg * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(5))) > 0
    alpha = np.where(bg, 0, np.where(grow, 1 - soft, 1))
    g = np.minimum(g, np.maximum(r, b) + 0.01)        # khử ánh xanh toàn ảnh (câu lệnh đã cấm xanh lá trên xe)
    out = (np.dstack([r, g, b, alpha]) * 255).clip(0, 255).astype(np.uint8)
    return Image.fromarray(out, "RGBA")


EDITS = {   # chỉnh trên ảnh đã sinh (raw nền xanh) khi model không chịu vẽ đúng số trục
 "n10": ("This truck currently has FOUR axles (two at the front, two at the rear). Edit it so it has EXACTLY THREE axles: "
         "keep the two front steering axles under and just behind the cab exactly as they are, and replace the two rear axles "
         "with ONE single rear drive axle with dual tyres, placed under the rear part of the cargo box. Fill the freed space with "
         "the chassis frame and the side under-run guard."),
 "n27": ("Fix the cargo box: replace the shipping-container style side doors (vertical locking bars, lever handles, deep black gaps) "
         "with SIX flat smooth aluminium hinged side door panels like the attached real photo of our truck: thin flush seams, slim hinges, "
         "small low-profile latch handles, the box side reads as one continuous flat surface with NO gaps or holes. Keep the cab unchanged."),
 "t06": ("Re-render this container as a STRICT SIDE ELEVATION exactly like the second (reference) image: camera perfectly perpendicular to the long side, the end walls NOT visible at all (no door end, no front end visible), top and bottom edges perfectly horizontal and parallel, only the long side wall with its corner posts at both ends. Keep it a white 20-foot dry container with vertical corrugations."),
 "c45": ("Re-render this container as a STRICT SIDE ELEVATION exactly like the second (reference) image: camera perfectly perpendicular to the long side, the end walls NOT visible at all (no door end, no front end visible), top and bottom edges perfectly horizontal and parallel, only the long side wall with its corner posts at both ends. Keep it a white 45-foot high-cube dry container with vertical corrugations."),
 "t07": ("Re-render this container as a STRICT SIDE ELEVATION exactly like the second (reference) image: camera perfectly perpendicular to the long side, the end walls NOT visible at all (no door end, no front end visible), top and bottom edges perfectly horizontal and parallel, only the long side wall with its corner posts at both ends. Keep it a white 45-foot refrigerated reefer container: smooth flat panels; the refrigeration unit end is at the RIGHT edge but seen only edge-on."),
 "n26": ("This truck currently has only TWO axles. Edit it so it has EXACTLY THREE axles: keep the single front steering axle "
         "under the cab exactly as it is, and replace the single rear axle with TWO rear axles close together (tandem) with dual "
         "tyres, placed under the rear part of the cargo box."),
}
EDIT_REF = {k: HERE / "raw" / "c40-s.png" for k in ("t06", "c45", "t07")}
EDIT_KEEP = (" Keep everything else IDENTICAL: same camera angle and framing, same cab, cargo box, colours, lighting, size, and the "
             "same flat pure green (#00FF00) background. Return the full edited image.")


def edit(tag, model):
    """Chỉnh ảnh raw/{tag}.png theo EDITS[mã]; sao lưu raw/{tag}-before-edit.png; tách nền lại."""
    base = tag.split("-")[0]
    f = HERE / "raw" / f"{tag}.png"
    bak = HERE / "raw" / f"{tag}-before-edit.png"
    if not bak.exists():
        bak.write_bytes(f.read_bytes())
    parts = [{"text": EDITS[base] + EDIT_KEEP + (" The FIRST image is the one to edit; the SECOND is a real photo for reference only." if base in REFS and base not in EDIT_REF else "")},
             {"inline_data": {"mime_type": "image/png", "data": base64.b64encode(f.read_bytes()).decode()}}]
    if base in EDIT_REF:
        parts[0]["text"] += " The FIRST image is the one to edit; the SECOND image shows the required camera angle only."
        parts.append({"inline_data": {"mime_type": "image/png", "data": base64.b64encode(EDIT_REF[base].read_bytes()).decode()}})
    elif base in REFS:
        parts.append({"inline_data": {"mime_type": "image/png", "data": base64.b64encode((FLEET / REFS[base]).read_bytes()).decode()}})
    aspect = "21:9" if tag.endswith("-s") else "16:9"
    body = {"contents": [{"parts": parts}], "generationConfig": {"responseModalities": ["IMAGE"], "imageConfig": {"aspectRatio": aspect}}}
    req = urllib.request.Request(API.format(m=model), data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json", "x-goog-api-key": api_key()})
    with urllib.request.urlopen(req, timeout=180, context=_ssl_ctx()) as r:
        data = json.loads(r.read())
    with open(HERE / "usage.log", "a") as lf:
        lf.write(json.dumps({"t": time.strftime("%Y-%m-%d %H:%M"), "model": model, "edit": tag, "usage": data.get("usageMetadata", {})}) + "\n")
    for c in data.get("candidates", []):
        for p in c.get("content", {}).get("parts", []):
            d = p.get("inlineData") or p.get("inline_data")
            if d:
                im = Image.open(io.BytesIO(base64.b64decode(d["data"]))).convert("RGB")
                im.save(f)
                return vehlib.save(vehlib.trim(chroma_key(im)), "b-ai", tag)
    raise RuntimeError("Không có ảnh trong phản hồi: " + json.dumps(data)[:300])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("names", nargs="*", default=list(SUBJECT))
    ap.add_argument("--model", default=os.environ.get("GEMINI_IMAGE_MODEL", "gemini-2.5-flash-image"))
    ap.add_argument("--ref", help="ảnh tham chiếu phong cách (vd 1 ảnh xe trong mẫu tham khảo)")
    ap.add_argument("--tries", type=int, default=1, help="số phương án mỗi loại (lưu raw/{name}-{i}.png)")
    ap.add_argument("--cut", choices=["q", "s", "both"], help="mặt cắt theo quy chuẩn: q = 3/4 trước, s = ngang; lưu {tên}-q / {tên}-s")
    ap.add_argument("--dry-run", action="store_true", help="chỉ in câu lệnh + ảnh tham chiếu + chi phí ước tính, KHÔNG gọi API")
    ap.add_argument("--shadow", action="store_true", help="thêm bóng tiếp đất (mặc định KHÔNG — user bỏ bóng 09/10)")
    ap.add_argument("--suffix", default="", help="hậu tố tên file, vd --suffix pro → t02-pro.png (không đè ảnh chính)")
    ap.add_argument("--rekey", action="store_true", help="chỉ tách nền lại từ raw/ đã có, không gọi API")
    ap.add_argument("--edit", nargs="+", metavar="TAG", help="chỉnh ảnh đã sinh, vd --edit n10-q n10-s (lệnh ở EDITS)")
    a = ap.parse_args()
    if a.edit:
        for t in a.edit:
            try:
                print(f"✓ edit {t}: {edit(t, a.model).relative_to(vehlib.LAB)}")
            except Exception as ex:
                print(f"✗ edit {t}: {ex}")
        return
    if a.rekey:
        for f in sorted((HERE / "raw").glob("*.png")):
            if a.names != list(SUBJECT) and f.stem.split("-")[0] not in a.names:
                continue
            cut = vehlib.trim(chroma_key(Image.open(f).convert("RGB")))
            p = vehlib.save(vehlib.add_contact_shadow(cut) if a.shadow and "-top" not in f.stem else cut, "b-ai", f.stem)
            print(f"✓ rekey {f.stem}: {p.relative_to(vehlib.LAB)}")
        return
    (HERE / "raw").mkdir(exist_ok=True)
    for n in a.names:
        base = n[:-4] if n.endswith("-top") else n
        if n not in SUBJECT and base not in SUBJECT:
            print(f"✗ {n}: không có trong danh sách {list(SUBJECT)}"); continue
        subj = SUBJECT.get(n) or SUBJECT[base] + ", seen from directly above"
        view = VIEW_OVR.get(n) or (VIEW_OVR["combo-top"] if n.endswith("-top") else VIEW_OVR["combo"] if n.startswith("combo") else VIEW)
        cuts = ["q", "s"] if a.cut == "both" else [a.cut] if a.cut else [None]
        for cut in cuts:
          if cut:
            view = CUT_VIEW[cut] + (f"; for this object the 'front' is {FRONT_OF[base]}" if base in FRONT_OF else "")
          prompt = STYLE.format(subject=subj[0].upper() + subj[1:], view=view)
          for i in range(a.tries):
              try:
                  fleet_ref = FLEET / REFS[n] if n in REFS and not a.ref else None
                  if a.dry_run:
                      print(f"── {n}{'-'+cut if cut else ''}  [{('21:9' if cut == 's' else '16:9') if cut else ASPECT.get(n, '9:16' if n.endswith('-top') else '16:9')}]  mẫu góc: {ANGLE_REF[cut].name if cut in ANGLE_REF else '—'} · mẫu xe: {(fleet_ref.name if fleet_ref else a.ref) or '—'}\n   {view[:90]}…\n   {subj}")
                      continue
                  raw = generate(prompt, a.model, a.ref or fleet_ref, ("21:9" if cut == "s" else "16:9") if cut else ASPECT.get(n, "9:16" if n.endswith("-top") else "16:9"),
                                 "model" if fleet_ref else "style", ANGLE_REF.get(cut) if cut else None)
                  tag = (f"{n}-{cut}" if cut else n) + (f"-{i+1}" if a.tries > 1 else "") + (f"-{a.suffix}" if a.suffix else "")
                  raw.save(HERE / "raw" / f"{tag}.png")
                  cut = vehlib.trim(chroma_key(raw))
                  cut = vehlib.add_contact_shadow(cut) if a.shadow and not n.endswith("-top") else cut
                  p = vehlib.save(cut, "b-ai", tag)
                  tk = {k: LAST_USAGE.get(k) for k in ("promptTokenCount", "candidatesTokenCount", "totalTokenCount")}
                  print(f"✓ {tag}: {p.relative_to(vehlib.LAB)}  ({a.model}) tokens={tk}")
              except Exception as ex:
                  print(f"✗ {n}: {ex}")
              if not a.dry_run:
                  time.sleep(1)
    if a.dry_run:
        k = sum(1 for n in a.names if n in SUBJECT or n[:-4] in SUBJECT) * a.tries * (2 if a.cut == "both" else 1)
        price = 0.137 if "pro" in a.model else 0.039
        print(f"\n{k} ảnh × ≈{price} USD ({a.model}) ≈ {k*price:.2f} USD — chưa gọi API")


if __name__ == "__main__":
    main()
