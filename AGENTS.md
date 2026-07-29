# AGENTS.md — icon-format-guide

새 세션·AI 에이전트가 **채팅 이력 없이** 이 repo만으로 작업할 때 읽는 문서입니다.

## 한 줄 정의

게임 / 언리얼 / TA용 **한국어 실전 가이드 허브**.  
“언제 뭘 쓸지” 비교표·선택 가이드·FAQ 스타일. (공식 문서 대체가 아니라 **결정 치트시트**)

- GitHub: https://github.com/Ageia/icon-format-guide  
- Pages 허브(권장 진입): https://ageia.github.io/icon-format-guide/index.html#icon  
- 아이콘 가이드 단독: https://ageia.github.io/icon-format-guide/format-guide.html  
- 로컬(작성자 PC 기준): `C:\Users\User\Desktop\Icon` (폴더명은 Icon, repo 이름은 icon-format-guide)

## 새 세션 시작 체크리스트

1. `README.md` + 이 파일(`AGENTS.md`) 읽기  
2. `git log -10 --oneline` / `git status`  
3. `index.html` — 탭 목록, `setGuide`, 해시 라우팅, stub(`GUIDES`)  
4. `format-guide.html` — **완성 가이드 톤·UI 레퍼런스**  
5. 작업 후 `main`에 커밋·push → GitHub Pages 자동 반영 (1~2분)

## 파일 역할

| 파일 | 역할 |
|------|------|
| `index.html` | 허브 셸. 사이드바 탭, 해시 라우팅, 예정 가이드 stub UI |
| `format-guide.html` | 아이콘 포맷 **완성** 가이드 (단독 페이지 + 허브 iframe) |
| `README.md` | 사람용 소개·링크 표 |
| `AGENTS.md` | AI/다음 세션용 규칙·맥락 |
| `badge_star.*` / `badge_cloud.*` | 아이콘 포맷 샘플 에셋 |
| `badge_star_anim.*` | 애니 샘플 (가이드 본문 연동은 아직 약함) |

빌드 도구/번들러 없음. **정적 HTML**만 push하면 됨.

## 허브 동작 규칙 (중요)

- 탭 공유 URL은 반드시 **`index.html#탭id`** 형태를 권장.  
  예: `.../index.html#texture`  
  루트 `/#texture` 만 쓰면, **예전에 redirect 하던 index 캐시** 때문에 `format-guide.html`로 튕길 수 있음.
- 아이콘 탭: `#icon` → iframe으로 `format-guide.html` 로드.  
  **다른 탭으로 바꿀 때 iframe은 `about:blank`로 언로드**해야 함 (아이콘 가이드가 덮어 보이는 버그 방지).
- 패널은 absolute 스택 + `.active`만 표시.
- `hub-build …` 스탬프가 사이드바 하단에 있으면 최신 허브.

### 탭 id ↔ 가이드

| id | 제목 | 상태 |
|----|------|------|
| `icon` | 아이콘 파일 포맷 | **완성** (`format-guide.html`) |
| `texture` | 텍스처 포맷 | 예정 (stub) |
| `material` | 머티리얼 블렌드 모드 | 예정 |
| `nanite` | Nanite vs 일반 메시 | 예정 |
| `import` | 텍스처 임포트 세팅 | 예정 |
| `lighting` | Lumen vs 베이크 | 예정 |
| `vfx` | VFX 텍스처·파티클 | 예정 |
| `collision` | 충돌 메시 | 예정 |

## 콘텐츠 컨벤션

- **UI·본문 언어: 한국어.** 한/영 토글은 나중 과제. 지금은 한국어만 유지.
- 톤: 실무 선택 가이드. 표 + “뭐 쓰지?” 결정 리스트 + FAQ + 짧은 치트시트.
- `format-guide.html` 스타일(다크, purple/cyan 액센트, card/table/tag)을 허브·후속 가이드와 맞출 것.
- 예정 가이드는 `index.html`의 `GUIDES` 객체 + 사이드바 버튼 + `#panel-{id}` 섹션을 **세트로** 추가.
- 가이드를 “완성”으로 올릴 때:
  1. 본문 HTML 작성 (단독 파일 권장: 예 `guides/texture-format.html` 또는 아이콘처럼 루트 파일)
  2. 허브에서 iframe/로드 연결
  3. README·이 파일 상태 표를 **완성**으로 갱신
  4. 사이드바 배지 `예정` → `완성`

## 하지 말 것

- 루트 `index.html`을 다시 `format-guide.html`로 **강제 redirect** 하지 말 것.  
- 아이콘 iframe을 숨기지 않은 채 다른 탭을 올리지 말 것.  
- 비밀·토큰·PAT를 repo에 넣지 말 것.  
- 불필요한 프레임워크 도입 금지 (정적 사이트 유지).  
- 요청 없는 대규모 리네임/리팩터 금지.

## 배포

- 원격: `origin` → `https://github.com/Ageia/icon-format-guide.git`  
- 브랜치: `main`  
- GitHub Pages: `main` / `/` (project site)  
- 계정: `Ageia` (작업 시 `gh auth status`로 확인 가능)

## 다음 작업 후보 (우선순위 제안)

1. **텍스처 임포트 세팅** 또는 **텍스처 포맷** 풀 가이드 (아이콘 가이드와 같은 깊이)  
2. 완성 가이드를 `guides/` 폴더로 정리할지 결정  
3. 한/영 토글 (나중)  
4. repo/표시 이름을 허브 성격에 맞게 바꿀지 (`game-dev-guides` 등) — 사용자 확인 후

## 검증

- 로컬: `index.html`을 브라우저로 열고 탭 전환·`#texture` 직접 진입 확인  
- 원격: push 후 `index.html#icon` / `#texture` 가 허브 UI로 여는지 확인 (아이콘 단독 URL로 튕기지 않아야 함)  
- 사이드바에 `hub-build` 문자열 존재 여부
