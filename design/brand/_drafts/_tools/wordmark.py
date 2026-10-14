#!/usr/bin/env python3
"""Đổi chữ thành nét vector (có kerning qua HarfBuzz), không phụ thuộc font:
  python3 wordmark.py font.ttf "invlogis" out.svg [--size 200] [--tracking 0] [--fill "#111"] [--wght 400]
--tracking: đơn vị 1/1000 em. --wght: cho font biến thiên."""
import argparse, uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
a = argparse.ArgumentParser(); a.add_argument("font"); a.add_argument("text"); a.add_argument("out")
a.add_argument("--size", type=float, default=200); a.add_argument("--tracking", type=float, default=0)
a.add_argument("--fill", default="#111111"); a.add_argument("--wght", type=float)
o = a.parse_args()
tt = TTFont(o.font); upm = tt["head"].unitsPerEm
blob = hb.Blob.from_file_path(o.font); face = hb.Face(blob); font = hb.Font(face)
loc = None
if o.wght and "fvar" in tt:
    font.set_variations({"wght": o.wght}); loc = {"wght": o.wght}
buf = hb.Buffer(); buf.add_str(o.text); buf.guess_segment_properties(); hb.shape(font, buf)
gs = tt.getGlyphSet(location=loc) if loc else tt.getGlyphSet()
order = tt.getGlyphOrder(); s = o.size/upm; x = 0; paths = []
for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
    pen = SVGPathPen(gs); gs[order[info.codepoint]].draw(TransformPen(pen, (s, 0, 0, -s, (x+pos.x_offset)*s, 0)))
    paths.append(pen.getCommands()); x += pos.x_advance + o.tracking*upm/1000
asc = tt["hhea"].ascent*s; desc = -tt["hhea"].descent*s; W = (x - o.tracking*upm/1000)*s
d = " ".join(p for p in paths if p)
open(o.out, "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 {-asc:.1f} {W:.1f} {asc+desc:.1f}"><path fill="{o.fill}" d="{d}"/></svg>')
print(o.out, f"rộng {W:.0f} cao {asc+desc:.0f}")
