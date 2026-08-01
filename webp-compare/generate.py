#!/usr/bin/env python3
"""
WebP 품질별 비교용 에셋 생성 스크립트.

소스 PNG(무손실) 하나를 받아 WebP Q10~Q100 + 무손실로 인코딩하고,
compression_comparison.html 의 LEVELS 배열에 넣을 JSON을 출력한다.

사용법:
    python generate.py                # 기본: ../assets/badge_star.png 사용
    python generate.py ../badge_cloud.png

의존성: Pillow (WebP 지원 빌드). `python -c "import PIL.features; print(PIL.features.check('webp'))"` → True 여야 함.
저작권: 소스는 반드시 프로젝트가 소유한 에셋(badge_star / badge_cloud 등)을 쓸 것. 외부 텍스처 금지.
"""
import os, sys, shutil, json
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
src = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, os.pardir, "assets", "badge_star.png")
src = os.path.abspath(src)
stem = os.path.splitext(os.path.basename(src))[0]  # e.g. "badge_star"

png_dst = os.path.join(HERE, stem + ".png")
if os.path.abspath(png_dst) != src:
    shutil.copyfile(src, png_dst)

im = Image.open(src).convert("RGBA")
qualities = [10, 20, 30, 40, 50, 60, 70, 75, 80, 85, 90, 95, 100]
levels = []

for q in qualities:
    fn = "%s_q%03d.webp" % (stem, q)
    im.save(os.path.join(HERE, fn), format="WEBP", quality=q, method=6)
    levels.append({"id": "q%03d" % q, "label": "WebP Q%d" % q, "short": "Q%d" % q,
                   "file": fn, "bytes": os.path.getsize(os.path.join(HERE, fn)), "kind": "lossy"})

fn = "%s_lossless.webp" % stem
im.save(os.path.join(HERE, fn), format="WEBP", lossless=True, quality=100, method=6)
levels.append({"id": "lossless", "label": "WebP Lossless", "short": "무손실",
               "file": fn, "bytes": os.path.getsize(os.path.join(HERE, fn)), "kind": "lossless"})

levels.append({"id": "png", "label": "PNG 원본", "short": "PNG",
               "file": stem + ".png", "bytes": os.path.getsize(png_dst), "kind": "png"})

print("ORIG_BYTES =", os.path.getsize(png_dst))
print(json.dumps(levels, ensure_ascii=False, indent=2))
