# format-guide

**파일 포맷과 텍스처 압축 기법**을 “언제 뭘 쓸지” 고르는 실전 가이드 허브입니다.
한국어 기준이며, 한/영 토글은 추후 지원 예정입니다.

## Preview

| 용도 | URL |
|------|-----|
| **가이드 허브** | https://ageia.github.io/icon-format-guide/index.html#icon |
| **아이콘 포맷 단독** | https://ageia.github.io/icon-format-guide/format-guide.html |
| **저장소** | https://github.com/Ageia/icon-format-guide |

> 참고: 저장소·Pages 경로는 아직 `icon-format-guide`입니다. (리네임은 백로그)

탭 공유는 `index.html#탭이름` 형식을 사용합니다.

### 탭 해시

| 해시 | 가이드 | 상태 | 링크 |
|------|--------|------|------|
| `#icon` | 아이콘 파일 포맷 | 완성 | [열기](https://ageia.github.io/icon-format-guide/index.html#icon) |
| `#raster` | 래스터 이미지 포맷 (PNG·JPEG·WebP·AVIF 실측 + WebP 스크러버) | 완성 | [열기](https://ageia.github.io/icon-format-guide/index.html#raster) |
| `#texture` | GPU 텍스처 압축 (BC·ASTC·ETC2) | 완성 | [열기](https://ageia.github.io/icon-format-guide/index.html#texture) |
| `#channel` | 채널 패킹 (ORM·노멀·sRGB) | 완성 | [열기](https://ageia.github.io/icon-format-guide/index.html#channel) |
| `#container` | 컨테이너·전송 포맷 (DDS·KTX2·Basis) | 완성 | [열기](https://ageia.github.io/icon-format-guide/index.html#container) |

허브 왼쪽 아래 `hub-build …` 문구가 보이면 최신 허브입니다. 예전 페이지가 뜨면 **Ctrl+F5** 로 새로고침하세요.

## Contents

- `index.html` — 허브 (사이드바 탭 + 가이드 패널)
- `format-guide.html` — 아이콘 포맷 완성 가이드 (단독 문서)
- `texture-compression-guide.html` — GPU 텍스처 압축 완성 가이드 (BC·ASTC·ETC2)
- `channel-packing-guide.html` — 채널 패킹 완성 가이드 (ORM·노멀·sRGB vs Linear)
- `container-format-guide.html` — 컨테이너·전송 포맷 완성 가이드 (DDS·KTX2·Basis)
- `raster-format-guide.html` — 래스터 포맷 완성 가이드 (PNG·JPEG·WebP·AVIF 실측·알파 함정)
- `raster-compare/` — 크로스 포맷 실측 세트 + `generate.py` (PNG/WebP/AVIF/JPEG/GIF)
- `webp-compare/` — WebP 품질별 압축 비교 스크러버 툴 + WebP 14단계 (`generate.py`로 재생성)
- `texture-artifacts/` — 실제 BC1 압축 아티팩트 비교 이미지 (`generate.py`, 자체 BC1 인코더)
- `AGENTS.md` — 새 세션·AI용 프로젝트 규칙/맥락
- `docs/TODO.md` — 하고 싶은 일 백로그 (Now / Next / Later)
- `badge_cloud.*` / `badge_star.*` — 멀티 포맷 샘플 에셋 (WebP 비교 소스로도 사용)

## For next session / AI

새 대화에서 이어서 작업할 때는 repo를 연 뒤
**`AGENTS.md` → `docs/TODO.md` → `README.md` → `git log`** 순으로 읽으면 됩니다.

아이디어 추가: `docs/TODO.md` 해당 섹션에 `- [ ] …` 한 줄 넣고 커밋.
