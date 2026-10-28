#!/usr/bin/env python3
"""Task B (bước 2): gắn dữ liệu S1 (s1-semantic.tsv) vào tokens.untitled.json."""
import json, re

BASE = 'design/_ref/untitled-ui'
tsv_path = f'{BASE}/_task/s1-semantic.tsv'
json_path = f'{BASE}/tokens.untitled.json'

# Đọc tsv -> token -> {light, dark, usage, node}
s1 = {}
node = ''
with open(tsv_path, encoding='utf-8') as f:
    for line in f:
        line = line.rstrip('\n')
        if line.startswith('##'):
            m = re.search(r'node\s+([0-9\-]+)', line)
            node = m.group(1) if m else ''
        elif line.startswith('#') or not line.strip():
            continue
        else:
            parts = line.split('\t')
            if len(parts) >= 4:
                s1[parts[0]] = {
                    'light': parts[1],
                    'dark': parts[2],
                    'usage': parts[3],
                    'node': node,
                }

# 6 chỗ lệch S1<->S2 (theo compare-report.txt; text-white KHÔNG tính)
MISMATCH = {
    'text-placeholder':          {'Light': 'neutral-500', 'Dark': 'neutral-400'},
    'fg-quaternary':             {'Light': 'neutral-400', 'Dark': 'neutral-500'},
    'fg-quaternary_hover':       {'Light': 'neutral-500', 'Dark': 'neutral-400'},
    'bg-primary-solid':          {'Light': 'neutral-950', 'Dark': 'neutral-800'},
    'bg-brand-primary_alt':      {'Light': 'brand-50',    'Dark': 'neutral-800'},
    'bg-brand-section':          {'Light': 'brand-800',   'Dark': 'neutral-800'},
}

TARGET_COLLECTIONS = {
    '1. Color modes / Text',
    '1. Color modes / Border',
    '1. Color modes / Foreground',
    '1. Color modes / Background',
}

with open(json_path, encoding='utf-8') as f:
    data = json.load(f)

n_usage = 0
n_src = 0
n_mismatch = 0
for col in data['collections']:
    if col['name'] not in TARGET_COLLECTIONS:
        continue
    for v in col['variables']:
        token = v['name']
        if token.startswith('--color-'):
            token = token[len('--color-'):]
        else:
            continue
        if token not in s1:
            continue
        v['usage'] = s1[token]['usage']
        n_usage += 1
        if 'S1' not in v.get('src', []):
            v['src'] = ['S1'] + [s for s in v.get('src', []) if s != 'S1']
        n_src += 1
        if token in MISMATCH:
            v['s1'] = MISMATCH[token]
            v['mismatch'] = True
            n_mismatch += 1

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
    f.write('\n')

print(f'usage điền: {n_usage}')
print(f'src thêm S1: {n_src}')
print(f'mismatch: {n_mismatch}')
print(f'tổng token S1 trong tsv: {len(s1)}')
