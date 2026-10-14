#!/bin/bash
# Tải font Google (OFL) bản TTF: bash fetch_font.sh "Be Vietnam Pro" 300 400 600  → _drafts/fonts/
FAM="$1"; shift; DIR="$(cd "$(dirname "$0")/.." && pwd)/fonts"; mkdir -p "$DIR"
for W in "$@"; do
  URL=$(curl -s -A "Mozilla/4.0" "https://fonts.googleapis.com/css2?family=${FAM// /+}:wght@$W&subset=vietnamese" | grep -o 'https://[^)]*\.ttf' | head -1)
  [ -z "$URL" ] && { echo "không tải được $FAM $W"; continue; }
  OUT="$DIR/${FAM// /}-$W.ttf"; curl -s -o "$OUT" "$URL" && echo "$OUT"
done
