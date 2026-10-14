#!/usr/bin/env python3
"""Xuất HTML/SVG sang PNG hoặc PDF bằng Chrome headless.
  python3 render.py in.html out.png --size 1080x1350 [--scale 2]
  python3 render.py in.svg  out.png --size 32x32          (SVG được bọc vào trang đúng cỡ)
  python3 render.py in.html out.pdf                        (in PDF)"""
import argparse, os, subprocess, tempfile, pathlib
from PIL import Image
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
a = argparse.ArgumentParser(); a.add_argument("src"); a.add_argument("out")
a.add_argument("--size", default="1280x800"); a.add_argument("--scale", type=float, default=1)
o = a.parse_args(); w, h = map(int, o.size.lower().split("x"))
src = pathlib.Path(o.src).resolve()
if src.suffix == ".svg":
    t = tempfile.NamedTemporaryFile("w", suffix=".html", delete=False)
    t.write(f'<html><body style="margin:0;background:transparent"><img src="{src.as_uri()}" style="width:{w}px;height:{h}px;display:block"></body></html>'); t.close()
    src = pathlib.Path(t.name)
out = pathlib.Path(o.out).resolve()
base = [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--allow-file-access-from-files"]
if out.suffix == ".pdf":
    subprocess.run(base + ["--no-pdf-header-footer", f"--print-to-pdf={out}", src.as_uri()], check=True, capture_output=True)
else:
    pad = 200  # chừa thêm chiều cao rồi cắt, tránh lệch viewport của headless
    subprocess.run(base + [f"--force-device-scale-factor={o.scale}", f"--window-size={w},{h+pad}",
                   "--default-background-color=00000000", f"--screenshot={out}", src.as_uri()], check=True, capture_output=True)
    im = Image.open(out); im.crop((0, 0, int(w*o.scale), int(h*o.scale))).save(out)
print(out)
