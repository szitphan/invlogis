#!/usr/bin/env python3
"""Tương phản WCAG: python3 contrast.py "#0036B5" "#FFFFFF" [cặp tiếp...]"""
import sys
def L(h):
    h = h.lstrip("#"); c = [int(h[i:i+2], 16)/255 for i in (0, 2, 4)]
    c = [x/12.92 if x <= .03928 else ((x+.055)/1.055)**2.4 for x in c]
    return .2126*c[0] + .7152*c[1] + .0722*c[2]
a = sys.argv[1:]
for f, b in zip(a[::2], a[1::2]):
    l1, l2 = sorted([L(f), L(b)], reverse=True); r = (l1+.05)/(l2+.05)
    print(f"{f} trên {b}: {r:.2f}:1 · chữ thường AA {'đạt' if r>=4.5 else 'trượt'} · chữ lớn AA {'đạt' if r>=3 else 'trượt'}")
