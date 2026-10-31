# 검증·배포 기록

확인일: 2026-10-31. 작업 저장소: `YunSangYeong/Engineer-Water-Environmental-Pollution-Control-CBT`.
최초 상태: `work` 브랜치, HEAD `2b4fac94fa2f41c1fd09918280ab80eeaf909743`, README만 존재, 작업 트리 깨끗함, 기존 AGENTS.md 없음.

## 로컬 결과

작업 디렉터리: `/workspace/Engineer-Water-Environmental-Pollution-Control-CBT`.
Node 24.19.0, npm 11.9.0, 시스템 Chromium, React/TypeScript/Vite 및 고정 package-lock 사용.

| 명령·검증 | 실제 결과 |
|---|---|
| `npm ci --no-audit --no-fund` | 종료 0, 110 packages 설치 |
| `npm test` | 종료 0, 212 통과, 실패·skip 0 |
| `npm run build` | 종료 0, TypeScript·Vite production 성공 |
| `PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH=/usr/bin/chromium npm run test:e2e` | 종료 0, 28 통과, 실패·skip 0 |
| `python3 scripts/generate_bank.py` 재생성 | JSON과 JSON/CSV 양식의 SHA-256 동일 |
| 스킬 전체 비교 | 최신 main의 원본 폴더 파일과 바이트 동일 |

최종 브라우저 검사: desktop 14 + Pixel 7 모바일 에뮬레이션 14. PC·모바일 대시보드 캡처를 직접 열어 확인했다. 실기기·Safari·Firefox 검사는 미실행이다.

실제로 확인한 흐름:

- 5과목 100문항, 150분 타이머, 답안 저장/변경, 새로고침 복원, 제출 취소/확인, 합격 결과·과목 점수·전체 해설, 오답 필터/재학습.
- 만료 자동 제출·만료 재접속·타이머 콜백 전 만료 클릭 차단·중복 제출 방지.
- 랜덤 즉시 채점·연속 정답·기록·오답 정답 재학습 시 해제·북마크·통계.
- 두 모드에서 실제 Space keydown/keyup, 본문 포커스, 미응답/마지막 시험 문제 보호, 버튼 고유 동작, 입력/수정키/메뉴/대화상자 보호, 반복 keydown 검사.
- JSON/CSV 등록·중복 제외·검증 대기·근거 입력 승인·잘못된 입력 거부·초기화.
- 손상 저장 원본 보존·용량 초과 저장 실패 경고 유지.
- 390×480, 740×360, 390×844, 390×480 확대 글자에서 실제 휠과 별도 CDP touchStart/move/end 스와이프. `scrollTop`을 코드로 변경하지 않았다. 아래 이동 후 하단 백업 다운로드·초기화 대화상자 실행, 위 이동 후 대시보드 선택까지 검사했다.
- 학습 기준 선택과 상단 비공식/잠정 규칙 상시 배너 부재. 기록 보관 범위 안내와 실제 오류 경고는 유지.

단위 검사에는 기본 등록 수·과목 분포·ID/정규화 중복·보기 재배치 중복·가져오기 원자성·표시된 계산 답의 독립 역산 200개·평균 합격 경계·과락 경계·저장 복원 검사가 포함된다. 이 검사는 전문가 검수나 공식 출제기준 대조를 대신하지 않는다.

초기 브라우저 실행은 샌드박스의 로컬 서버 실행 제한으로 시작하지 못했다. 허용된 실행 범위에서 서버·Chromium을 실행해 검증했다. 첫 회귀에서는 통계의 기록 보관 안내까지 금지 배너로 간주하던 검사 2개가 실패했다. 요구하는 배너 종류를 검사하도록 수정한 후 전체 28개가 통과했다. 이는 로컬 개발 재검증이며 배포 시도가 아니다.

빌드 경고: 기본 은행 JSON을 포함한 JS chunk 약 539 kB(압축 약 106 kB)로 Vite의 500 kB 안내가 표시된다. 빌드 오류는 아니다.

## 문항 인수 한계

실제 내부 검수 220 / 목표 1,000 / 부족 780. 기출 0·복원 0·자체 제작 220. 숫자 변형 20 family × 10조건 = 200, 개념 20. 전문가 검수와 공식 시험 규칙·공식 출제기준·현행 법령 대조는 미완료. 관계법규는 일반 관리 원칙만 포함한다. 최종 수량·공식 대조 기준을 충족했다고 판단하지 않는다. 상세는 SOURCES.md 참조.

## 배포: 첫 사전 차단에서 중단

처음 수행한 배포 사전 확인:

1. `git ls-remote origin refs/heads/main refs/heads/codex/water-cbt` 성공. 원격 main은 `2b4fac94fa2f41c1fd09918280ab80eeaf909743`, 보존 브랜치는 없었다.
2. 인증 변수 이름/존재만 확인: GH_TOKEN 있음, GITHUB_TOKEN 없음. 값은 출력하지 않았다. 기존 인증을 HTTPS 요청에 사용했다.
3. `GET https://api.github.com/repos/YunSangYeong/Engineer-Water-Environmental-Pollution-Control-CBT` 최초 요청 실패: **`URLError: Tunnel connection failed: 403 Forbidden`**. 사전 확인 명령 종료 20.

사용자 지시와 표준 v1.4.0에 따라 여기서 배포 진행을 중단했다. API 재조회·다른 경로 배포·workflow dispatch·재실행·main push·배포를 유발하는 추가 push는 하지 않았다. Pages Source/최초 활성화/승인 여부는 조회하지 못했으며 추정하지 않는다.

코드는 workflow의 `push: branches: [main]`에 해당하지 않는 **`codex/water-cbt` 보존 브랜치**로 반영한다. PR은 생성하지 않으며 이 보존 push로 배포를 시작하지 않는다. main을 변경하지 않는다. GitHub의 저장소 자체 정책이나 추가 자동화는 API 차단으로 조회 불가다.

- main 원격 반영: 미실행.
- 이 변경의 GitHub CI: 미실행.
- 이 변경의 Pages 배포: 미실행.
- 현재 게시 상태: 미확인.
- 공개 화면 기능 확인: 미실행.
- 예상 기본 주소: https://YunSangYeong.github.io/Engineer-Water-Environmental-Pollution-Control-CBT/ (게시 확인 링크가 아님).
- 이미 배포된 electrician-cbt 및 다른 프로젝트: 수정·push·재배포 없음.

사용자가 지금 할 최소 동작 하나: **환경 설정의 네트워크 허용 도메인에 `api.github.com`을 추가한다.** 이후 사용자가 직접 배포를 마무리한다. 현재 오류는 API 프록시 접근 거부이며 Pages 활성화가 안 됐다는 증거는 아니다. 토큰 추가나 Pages 설정 변경이 필요하다고 단정하지 않는다. 새 명시적 실행 요청 전에는 에이전트가 배포를 재시도하지 않는다.
