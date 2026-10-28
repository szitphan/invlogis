import json
d = json.load(open('tokens.untitled.json', encoding='utf-8'))

radius = [
 ("--radius-none","0px"),("--radius-xs","0.125rem"),("--radius-sm","0.25rem"),
 ("--radius-DEFAULT","0.25rem"),("--radius-md","0.375rem"),("--radius-lg","0.5rem"),
 ("--radius-xl","0.75rem"),("--radius-2xl","1rem"),("--radius-3xl","1.5rem"),("--radius-full","9999px"),
]
col_radius = {"name":"2. Radius","modes":["Light"],"not_in_theme_css":True,"src_note":"S3 (docs installation) — KHÔNG có trong repo theme.css",
  "variables":[{"name":n,"type":"dimension","values":{"Light":v},"usage":"","src":["S3"]} for n,v in radius]}

col_spacing = {"name":"3. Spacing","modes":["Light"],"not_in_theme_css":True,"src_note":"S3/Tailwind v4 default — --spacing = 0.25rem (4px), mọi calc(var(--spacing)*N) dựa trên biến này; KHÔNG khai trong theme.css",
  "variables":[{"name":"--spacing","type":"dimension","values":{"Light":"0.25rem"},"usage":"Base spacing = 4px","src":["S3"]}]}

# insert radius + spacing after primitives/color-modes (append at end, order cosmetic)
d["collections"].extend([col_radius, col_spacing])
json.dump(d, open('tokens.untitled.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print("added radius(10) + spacing(1); total collections:", len(d["collections"]))
