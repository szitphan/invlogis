#!/usr/bin/env python3
"""So số biến trong raw/theme.css với tokens.untitled.json."""
import re, json, sys

css = open('raw/theme.css', encoding='utf-8').read()

def extract_block(text, start_pat):
    m = re.search(start_pat, text); i = m.end(); depth = 1; j = i
    while j < len(text):
        c = text[j]
        if c == '{': depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0: return text[i:j]
        j += 1
    return text[i:]

light = {}
for m in re.finditer(r'(--[\w-]+)\s*:\s*(.*?);', extract_block(css, r'@theme\s*\{'), re.S):
    light[m.group(1)] = re.sub(r'\s+',' ',m.group(2)).strip()

# define prefix groups (non-overlapping, order matters)
GROUPS = [
 ('--color-utility-','color / utility'),
 ('--color-text-','color / text'),
 ('--color-border-','color / border'),
 ('--color-fg-','color / foreground'),
 ('--color-bg-','color / background'),
 ('--color-brand-','color / brand (primitive)'),
 ('--color-alpha-','color / alpha (primitive)'),
 ('--color-','color / base + component'),
 ('--shadow-','shadow'),
 ('--drop-shadow-','drop-shadow'),
 ('--font-','font family'),
 ('--text-color-','text-color alias'),
 ('--text-','text scale'),
 ('--breakpoint-','breakpoint'),
 ('--max-width-','max-width/container'),
 ('--animate-','animate'),
 ('--background-color-','background-color alias'),
 ('--border-color-','border-color alias'),
 ('--ring-color-','ring-color alias'),
 ('--outline-color-','outline-color alias'),
]

def group_of(n):
    for p,_ in GROUPS:
        if n.startswith(p): return p
    return '--other-'

from collections import Counter
css_counts = Counter(group_of(n) for n in light)

# json: flatten all variables (skip not_in_theme_css and s1_only collections)
d = json.load(open('tokens.untitled.json', encoding='utf-8'))
json_counts = Counter()
json_total = 0
s1_vars = 0
radius_spacing = {}
for col in d['collections']:
    for v in col['variables']:
        n = v['name']
        if col.get('not_in_theme_css') or col.get('s1_only'):
            # still track radius/spacing for informational report
            if n.startswith('--radius-') or n.startswith('--spacing-'):
                radius_spacing[n.split('-')[1] if False else n[:0]] = None
            continue
        json_counts[group_of(n)] += 1
        json_total += 1

# count S1-sourced variables across all collections
for col in d['collections']:
    for v in col['variables']:
        if 'S1' in v.get('src', []):
            s1_vars += 1

# requested top-level counts
def top(name, dct):
    return sum(c for g,c in dct.items() if g.startswith(name))

report = []
report.append("== Kiểm số token: raw/theme.css vs tokens.untitled.json ==")
report.append("")
ok = True
for p, label in GROUPS:
    c = css_counts.get(p,0)
    j = json_counts.get(p,0)
    mark = "OK " if c==j else "MISMATCH"
    if c!=j: ok=False
    report.append(f"  [{mark}] {label:28s} theme.css={c:4d}  json={j:4d}")

report.append("")
report.append("-- Tổng hợp theo yêu cầu task (tiền tố) --")
for pref, label in [('--color-','--color-*'),('--shadow-','--shadow-*'),('--text-','--text-*'),
                    ('--radius-','--radius-*'),('--spacing-','--spacing-*')]:
    c = top(pref, css_counts)
    j = top(pref, json_counts)
    note = ""
    if pref=='--radius-':
        note = " (S3 docs: 10 token radius, KHÔNG có trong theme.css)"
    if pref=='--spacing-':
        note = " (S3/Tailwind default: --spacing=0.25rem, KHÔNG khai trong theme.css)"
    report.append(f"  {pref:14s} theme.css={c:4d}  json={j:4d}{note}")

report.append("")
report.append(f"Tổng biến theme.css (light @theme): {len(light)}")
report.append(f"Tổng biến trong tokens.json (S2, bỏ not_in_theme_css/s1_only): {json_total}")
report.append(f"Tổng biến mang nguồn S1 trong tokens.json (src chứa S1): {s1_vars}")
report.append("KẾT QUẢ: " + ("PASS — khớp" if ok and json_total==len(light) else "FAIL — lệch"))

if json_total != len(light):
    report.append(f"  -> tổng lệch: theme.css={len(light)} json={json_total}")
    ok = False

text = "\n".join(report)
open('_task/verify-report.txt','w',encoding='utf-8').write(text)
print(text)
sys.exit(0 if ok else 1)
