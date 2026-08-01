# TODO / 아이디어

백로그. **Now는 최대 3개.** 끝나면 `[x]` 후 Done으로 옮기거나 삭제.  
AI·새 세션은 작업 전후 이 파일을 갱신한다.

> **모든 탭 완성** (icon·raster·texture·channel·container). 이제 심화·품질 작업 위주.

## 지금 하기 (Now)

- [ ] (심화) 새 탭 후보: SDF 텍스트/아이콘, 스프라이트 아틀라스 패킹
- [ ] (심화) badge_cloud 비교 세트, 한/영 토글

## 다음에 (Next)

- [ ] 채널 패킹 가이드에 실제 채널 분해 샘플 이미지 추가
- [ ] 가이드 간 상호 링크(텍스처↔채널↔컨테이너) 점검·보강
- [ ] 허브 로드 방식 정리 (루트 단독 파일 vs `guides/` 폴더 — 파일이 늘면)
- [ ] `badge_star_anim.*` 애니 비교 섹션을 래스터/아이콘 가이드에 연동
- [ ] 포맷별 실제 파일 용량 자동 표 (badge 샘플 세트 활용)

## 언젠가 (Later)

- [ ] 한/영 토글
- [ ] repo/표시 이름을 포맷·압축 성격에 맞게 변경 검토 (`format-guide` 등)
- [ ] 플랫폼별 규격 한 줄 (Android / iOS / favicon 세트)

## 완료 (Done) — 최근

- [x] 밉맵·텍스처 필터링 완성 가이드 (`mipmap-filtering-guide.html`, `#mipmap`) — 실측 에일리어싱 데모(`mip-demo/`)
- [x] 5개 가이드 기술 정확성 웹 교차검증 — 12개 항목 전부 VERIFIED(수정 없음), ORM 관례 표현만 미세 조정
- [x] 가이드 간 상호 링크 연결 (`target="_top"`), 푸터 허브 링크 nested 로드 버그 수정
- [x] 소스 에셋 `assets/`로 폴더 정리 (badge_* 18개, git rename)
- [x] 채널 패킹 가이드에 실제 채널 분해 이미지 추가 (`channel-demo/` — 합성 ORM → R/G/B 분해)
- [x] 래스터 탭을 완성 가이드로 승격 (`raster-format-guide.html`) — PNG·JPEG·WebP·AVIF·GIF 실측 용량, JPEG 알파 함정 실제 이미지, WebP 스크러버 링크 (`raster-compare/`)
- [x] 텍스처 가이드에 실제 BC1 압축 아티팩트 비교 이미지 추가 (`texture-artifacts/` — 자체 BC1 인코더로 생성, 밴딩·블록 계단 시각화)
- [x] 컨테이너·전송 포맷 완성 가이드 (`container-format-guide.html`, `#container`) — DDS·KTX2·Basis, 전송 vs GPU 두 축
- [x] 예정(stub) 렌더 머신 제거 — 모든 탭 완성 iframe화
- [x] 채널 패킹 완성 가이드 (`channel-packing-guide.html`, `#channel`) — ORM·노멀·sRGB vs Linear·압축 상호작용
- [x] GPU 텍스처 압축 완성 가이드 (`texture-compression-guide.html`, `#texture`) — BC·ASTC·ETC2 엔진 중립
- [x] 래스터 탭에 WebP 품질별 압축 비교 툴 합류 (`webp-compare/`) — 저작권 텍스처는 자체 에셋 `badge_star.png`(무손실)로 대체
- [x] 언리얼 전용 주제(머티리얼·Nanite·Lumen·VFX·충돌·임포트) 전부 제거, 포맷·압축 허브로 전환
- [x] 아이콘 포맷 완성 가이드 (`format-guide.html`)
- [x] GitHub repo + Pages
- [x] 한국어 가이드 허브 탭 UI (`index.html`)
- [x] 탭 공유 URL `index.html#…` 정착
- [x] `AGENTS.md` 세션 인수인계
- [x] `docs/TODO.md` 백로그
