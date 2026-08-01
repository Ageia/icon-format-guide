#!/usr/bin/env python3
"""
실제 BC1(DXT1) 컬러 압축을 돌려 아티팩트 비교 이미지를 만든다.

BC1 컬러 경로를 그대로 구현:
  - 4×4 블록마다 RGB565 엔드포인트 2개(블록의 채널별 min/max = bounding box)
  - 4색 팔레트 [c0, c1, (2c0+c1)/3, (c0+2c1)/3]
  - 픽셀마다 가장 가까운 팔레트 인덱스(2bit) 선택 후 디코드
최적 인코더보다 약간 거칠지만 '진짜 BC1 방식'의 밴딩·블록 계단을 보여준다.

출력: 이 폴더에 *_orig.png / *_bc1.png + 확대 크롭. PSNR도 출력.
의존성: Pillow (numpy 불필요).
"""
import os
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))


def to565(r, g, b):
    return ((r >> 3) << 11) | ((g >> 2) << 5) | (b >> 3)


def from565(c):
    r = (c >> 11) & 0x1F
    g = (c >> 5) & 0x3F
    b = c & 0x1F
    return ((r * 255 + 15) // 31, (g * 255 + 31) // 63, (b * 255 + 15) // 31)


def bc1_block(pixels):
    """pixels: list of 16 (r,g,b). return list of 16 decoded (r,g,b)."""
    rs = [p[0] for p in pixels]
    gs = [p[1] for p in pixels]
    bs = [p[2] for p in pixels]
    lo = (min(rs), min(gs), min(bs))
    hi = (max(rs), max(gs), max(bs))
    q_hi = to565(*hi)
    q_lo = to565(*lo)
    # 4-color mode requires color0 > color1
    if q_hi < q_lo:
        q_hi, q_lo = q_lo, q_hi
    c0 = from565(q_hi)
    c1 = from565(q_lo)
    c2 = tuple((2 * c0[i] + c1[i]) // 3 for i in range(3))
    c3 = tuple((c0[i] + 2 * c1[i]) // 3 for i in range(3))
    pal = [c0, c1, c2, c3]
    out = []
    for p in pixels:
        best = 0
        bestd = None
        for i, c in enumerate(pal):
            d = (p[0] - c[0]) ** 2 + (p[1] - c[1]) ** 2 + (p[2] - c[2]) ** 2
            if bestd is None or d < bestd:
                bestd = d
                best = i
        out.append(pal[best])
    return out


def bc1_compress(img):
    img = img.convert("RGB")
    w, h = img.size
    src = img.load()
    dst = Image.new("RGB", (w, h))
    dpx = dst.load()
    for by in range(0, h, 4):
        for bx in range(0, w, 4):
            block = []
            coords = []
            for y in range(by, min(by + 4, h)):
                for x in range(bx, min(bx + 4, w)):
                    block.append(src[x, y])
                    coords.append((x, y))
            dec = bc1_block(block)
            for (x, y), c in zip(coords, dec):
                dpx[x, y] = c
    return dst


def psnr(a, b):
    a = a.convert("RGB"); b = b.convert("RGB")
    pa, pb = a.load(), b.load()
    w, h = a.size
    se = 0
    for y in range(h):
        for x in range(w):
            ca, cb = pa[x, y], pb[x, y]
            se += sum((ca[i] - cb[i]) ** 2 for i in range(3))
    mse = se / (w * h * 3)
    if mse == 0:
        return 99.0
    import math
    return 10 * math.log10((255 ** 2) / mse)


def make_gradient(size=256):
    """부드러운 컬러 그라데이션 — BC1에서 밴딩이 잘 보이는 케이스."""
    img = Image.new("RGB", (size, size))
    px = img.load()
    a = (18, 22, 64)     # deep indigo
    b = (122, 232, 250)  # cyan
    c = (250, 236, 250)  # near white
    for y in range(size):
        ty = y / (size - 1)
        for x in range(size):
            tx = x / (size - 1)
            # diagonal blend a->b->c
            t = (tx * 0.65 + ty * 0.35)
            if t < 0.5:
                u = t / 0.5
                col = tuple(round(a[i] + (b[i] - a[i]) * u) for i in range(3))
            else:
                u = (t - 0.5) / 0.5
                col = tuple(round(b[i] + (c[i] - b[i]) * u) for i in range(3))
            px[x, y] = col
    return img


def zoom(img, box, scale=6):
    """box=(x,y,w,h) 크롭 후 nearest 확대 — 4×4 블록 계단을 크게 보이게."""
    x, y, w, h = box
    crop = img.crop((x, y, x + w, y + h))
    return crop.resize((w * scale, h * scale), Image.NEAREST)


def save(img, name):
    p = os.path.join(HERE, name)
    img.save(p)
    return os.path.getsize(p)


def main():
    results = []

    # 1) gradient
    grad = make_gradient(256)
    grad_bc1 = bc1_compress(grad)
    save(grad, "gradient_orig.png")
    save(grad_bc1, "gradient_bc1.png")
    results.append(("gradient", psnr(grad, grad_bc1)))
    # zoom crop on a smooth region
    zbox = (96, 96, 40, 40)
    save(zoom(grad, zbox), "gradient_orig_zoom.png")
    save(zoom(grad_bc1, zbox), "gradient_bc1_zoom.png")

    # 2) badge asset (flatten alpha over white so it's a pure color-banding demo)
    star = Image.open(os.path.join(HERE, os.pardir, "badge_star.png")).convert("RGBA")
    star = star.resize((256, 256), Image.LANCZOS)
    bg = Image.new("RGBA", star.size, (255, 255, 255, 255))
    flat = Image.alpha_composite(bg, star).convert("RGB")
    flat_bc1 = bc1_compress(flat)
    save(flat, "badge_orig.png")
    save(flat_bc1, "badge_bc1.png")
    results.append(("badge_star", psnr(flat, flat_bc1)))

    print("PSNR (dB, higher = closer to original):")
    for name, val in results:
        print("  %-12s %.2f dB" % (name, val))


if __name__ == "__main__":
    main()
