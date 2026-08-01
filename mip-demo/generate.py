#!/usr/bin/env python3
"""
밉맵/필터링 설명용 에일리어싱 데모.
고주파 패턴(지멘스 스타)을 축소할 때:
  - point(nearest) 축소 = 밉/필터 없음 → 모아레·계단 에일리어싱
  - 평균(area/lanczos) 축소 = 밉맵이 하는 일 → 깨끗함
또한 밉 체인 썸네일(반씩 줄어드는 이미지)도 생성.

출력: 이 폴더에 pattern.png, alias_point.png, alias_filtered.png, mipchain.png
의존성: Pillow (numpy 불필요).
"""
import os, math
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))


def siemens(size=512, spokes=48):
    img = Image.new("L", (size, size))
    px = img.load()
    c = (size - 1) / 2
    for y in range(size):
        for x in range(size):
            ang = math.atan2(y - c, x - c)
            v = 255 if math.sin(ang * spokes) >= 0 else 0
            # 바깥은 원으로 마스크
            if math.hypot(x - c, y - c) > c:
                v = 30
            px[x, y] = v
    return img.convert("RGB")


def upscale(img, to=288):
    return img.resize((to, to), Image.NEAREST)


def main():
    pat = siemens(512, 48)
    pat.save(os.path.join(HERE, "pattern.png"))

    small = 72  # 강한 축소로 에일리어싱 유발
    point = pat.resize((small, small), Image.NEAREST)
    filt = pat.resize((small, small), Image.LANCZOS)
    upscale(point).save(os.path.join(HERE, "alias_point.png"))
    upscale(filt).save(os.path.join(HERE, "alias_filtered.png"))

    # 밉 체인 썸네일: 512→256→…→8, 가로로 이어 붙임
    sizes = [128, 64, 32, 16, 8]
    pad = 8
    total_w = sum(sizes) + pad * (len(sizes) + 1)
    strip = Image.new("RGB", (total_w, 128 + pad * 2), (13, 18, 24))
    x = pad
    for s in sizes:
        m = pat.resize((s, s), Image.LANCZOS)
        strip.paste(m, (x, pad + (128 - s) // 2))
        x += s + pad
    strip.save(os.path.join(HERE, "mipchain.png"))

    print("generated: pattern.png, alias_point.png, alias_filtered.png, mipchain.png")


if __name__ == "__main__":
    main()
