#!/usr/bin/env python3
"""Kiểm font có đủ chữ tiếng Việt: python3 vn_glyphs.py font.ttf [...]"""
import sys
from fontTools.ttLib import TTFont
V = "aàáảãạăằắẳẵặâầấẩẫậeèéẻẽẹêềếểễệiìíỉĩịoòóỏõọôồốổỗộơờớởỡợuùúủũụưừứửữựyỳýỷỹỵđ"
CH = V + V.upper()
for f in sys.argv[1:]:
    cmap = TTFont(f).getBestCmap(); miss = [c for c in CH if ord(c) not in cmap]
    print(f"{'ĐỦ' if not miss else 'THIẾU'} · {f}" + (f" · thiếu: {''.join(miss)}" if miss else ""))
