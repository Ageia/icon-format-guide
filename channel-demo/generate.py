#!/usr/bin/env python3
"""
채널 패킹 개념 설명용 '합성 ORM' 데모 이미지를 만든다.
서로 다른 3개의 흑백 데이터 맵(AO/Roughness/Metallic)을 각각 R/G/B 채널에 넣어
한 장(ORM)으로 패킹하고, 다시 R/G/B로 분해한 모습을 보여준다.

※ 실제 스캔/베이크 맵이 아니라 '개념 예시용 합성 맵'이다(정직하게 라벨링).
출력: 이 폴더에 orm_ao.png / orm_rough.png / orm_metal.png / orm_packed.png
의존성: Pillow (numpy 불필요).
"""
import os, math
from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
N = 256
cx = cy = (N - 1) / 2
maxd = math.hypot(cx, cy)


def save(img, name):
    img.save(os.path.join(HERE, name))


# R = Ambient Occlusion: 중앙 밝고 가장자리 어두운 방사형(가려짐)
ao = Image.new("L", (N, N))
pa = ao.load()
for y in range(N):
    for x in range(N):
        d = math.hypot(x - cx, y - cy) / maxd  # 0 center .. 1 corner
        v = 255 * (1.0 - 0.85 * (d ** 1.4))
        pa[x, y] = max(0, min(255, int(v)))

# G = Roughness: 대각 그라데이션 + 부드러운 원반 몇 개(부위별 거칠기 차이)
rough = Image.new("L", (N, N))
pr = rough.load()
for y in range(N):
    for x in range(N):
        base = 60 + 150 * ((x + y) / (2 * (N - 1)))
        pr[x, y] = int(base)
dr = ImageDraw.Draw(rough)
for (bx, by, br, val) in [(70, 90, 42, 230), (180, 70, 30, 40), (170, 185, 55, 210)]:
    dr.ellipse([bx - br, by - br, bx + br, by + br], fill=val)
rough = rough.filter(ImageFilter.GaussianBlur(6))

# B = Metallic: 금속 링(annulus) 마스크 — 거의 0/1 데이터
metal = Image.new("L", (N, N), 0)
dm = ImageDraw.Draw(metal)
dm.ellipse([28, 28, N - 28, N - 28], fill=255)
dm.ellipse([70, 70, N - 70, N - 70], fill=0)
metal = metal.filter(ImageFilter.GaussianBlur(1))

save(ao, "orm_ao.png")
save(rough, "orm_rough.png")
save(metal, "orm_metal.png")

# ORM 패킹: R=AO, G=Rough, B=Metal → 한 장 (컬러로 보면 '데이터라서' 이상한 색)
packed = Image.merge("RGB", (ao, rough, metal))
save(packed, "orm_packed.png")

print("generated:", ", ".join(["orm_ao.png", "orm_rough.png", "orm_metal.png", "orm_packed.png"]))
print("packed는 컬러가 아니라 3개 데이터 맵을 R/G/B에 넣은 것 — 셰이더는 tex.r/.g/.b로 꺼내 씀.")
