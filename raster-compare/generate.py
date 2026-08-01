#!/usr/bin/env python3
"""
같은 소스를 여러 래스터 포맷으로 인코딩해 실제 용량·특성을 비교한다.
PNG / WebP(무손실·손실) / AVIF(손실·준무손실) / JPEG(알파 불가) / GIF.

소스: 자체 에셋 badge_star.png에 '원형 알파 마스크'를 적용한 버전(star_alpha.png).
  → 둥근 배지의 네 모서리가 실제 투명이 되므로, JPEG로 저장하면 모서리가 배경색으로 채워진다.
핵심 교훈: JPEG는 알파(투명)를 지원하지 않는다 → 투명 영역이 사각형 배경이 된다.

출력: 이 폴더에 각 포맷 파일 + JSON(파일명·바이트·특성). 저작권: 자체 에셋만 사용.
의존성: Pillow 12+ (AVIF 네이티브). Image.init() 후 'AVIF' in Image.SAVE → True
"""
import os, json
from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, os.pardir, "assets", "badge_star.png")

base = Image.open(SRC).convert("RGBA")
w, h = base.size

# 원형 알파 마스크 (안티에일리어싱: 4배 그린 뒤 축소)
scale = 4
big = Image.new("L", (w * scale, h * scale), 0)
d = ImageDraw.Draw(big)
margin = int(w * 0.015) * scale  # 배지 바깥 링까지 살짝 여유
d.ellipse([margin, margin, w * scale - margin, h * scale - margin], fill=255)
mask = big.resize((w, h), Image.LANCZOS)

star = base.copy()
star.putalpha(mask)  # 모서리 투명
star_path = os.path.join(HERE, "star_alpha.png")
star.save(star_path)

rows = []


def rec(fn, kind, alpha, note):
    rows.append({"file": fn, "kind": kind, "alpha": alpha, "note": note,
                 "bytes": os.path.getsize(os.path.join(HERE, fn))})


# PNG (lossless, alpha) — baseline
rec("star_alpha.png", "PNG", True, "무손실 · 알파")

# WebP
star.save(os.path.join(HERE, "star_webp_lossless.webp"), format="WEBP", lossless=True, method=6)
rec("star_webp_lossless.webp", "WebP 무손실", True, "무손실 · 알파")
star.save(os.path.join(HERE, "star_webp_q80.webp"), format="WEBP", quality=80, method=6)
rec("star_webp_q80.webp", "WebP Q80", True, "손실 · 알파")

# AVIF (Pillow 12 native)
star.save(os.path.join(HERE, "star_avif_q55.avif"), format="AVIF", quality=55)
rec("star_avif_q55.avif", "AVIF Q55", True, "손실 · 알파 · 고효율")
star.save(os.path.join(HERE, "star_avif_q100.avif"), format="AVIF", quality=100)
rec("star_avif_q100.avif", "AVIF Q100", True, "준무손실 · 알파")

# JPEG — no alpha: 투명이 배경으로 채워짐 (흰/검 두 버전으로 시각화)
white = Image.new("RGBA", star.size, (255, 255, 255, 255))
Image.alpha_composite(white, star).convert("RGB").save(
    os.path.join(HERE, "star_jpeg_white.jpg"), format="JPEG", quality=85)
rec("star_jpeg_white.jpg", "JPEG Q85 (흰 배경)", False, "손실 · 알파 없음 → 흰 모서리")
black = Image.new("RGBA", star.size, (0, 0, 0, 255))
Image.alpha_composite(black, star).convert("RGB").save(
    os.path.join(HERE, "star_jpeg_black.jpg"), format="JPEG", quality=85)
rec("star_jpeg_black.jpg", "JPEG Q85 (검은 배경)", False, "손실 · 알파 없음 → 검은 모서리")

# GIF — 256색 팔레트 + 1비트 투명
p = star.convert("RGBA")
alpha = p.getchannel("A")
pal = p.convert("RGB").convert("P", palette=Image.ADAPTIVE, colors=255)
# 투명 픽셀을 인덱스 255로
mask_bin = alpha.point(lambda a: 255 if a < 128 else 0)
pal.paste(255, mask_bin)
pal.save(os.path.join(HERE, "star.gif"), format="GIF", transparency=255)
rec("star.gif", "GIF", True, "256색 · 1비트 투명(모서리 거침)")

rows.sort(key=lambda r: r["bytes"])
print(json.dumps(rows, ensure_ascii=False, indent=2))
