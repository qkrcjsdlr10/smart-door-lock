# SmartDoor-master_(11.24) — 새 PC·웹 작업 인계

작성: 2026-10-28 (Asia/Seoul).

저장소: https://github.com/qkrcjsdlr10/smart-door-lock

받을 브랜치: `main`.

```powershell
git clone --branch main https://github.com/qkrcjsdlr10/smart-door-lock.git
```

## 새 PC 설정과 현재 제한

먼저 [README.md](README.md)의 미완성·누락 모듈 목록을 확인한다. `requirement.txt`와 `test_requirement.txt`는 비어 있다. 이 파일을 설치했다고 의존성 준비가 끝난 것으로 판단하지 않는다. Python 버전·OpenCV·Pillow·face_recognition·Tkinter 및 GPIO 환경은 대상 장치에서 별도로 확정해야 한다. 이번 인계에서는 패키지 설치나 문 개폐를 수행하지 않았다.

## Git에 없는 항목 복원

| 항목 | 복원 방법 / 한계 |
| --- | --- |
| `SMARTDOOR_ADMIN_PASSWORD` | 소유자가 비밀번호를 정해 OS 환경변수로 안전하게 입력. `src/main.py`는 `os.environ`을 읽으며 `.env` 자동 로더는 없다. 비밀번호를 문서·명령 이력에 넣지 않는다. |
| 얼굴 사진·등록 사용자 데이터 | 본인 동의와 원본을 확보한 장치에서 새로 등록. 개인정보 제거로 삭제한 원본은 Git에서 복구할 수 없다. 가짜 얼굴 데이터로 대체하지 않는다. |
| `person_db.py`, `video.py`, `common.py` | README에 누락으로 기록되어 있다. 자동 생성 가능한 설정 파일이 아니며 원본 복구 또는 별도 구현이 필요하다. |
| Haar Cascade XML·장치 설정 | OpenCV 제공 데이터/해당 장치 설정을 확인해 코드가 요구하는 위치로 준비. 카메라·GPIO·배선은 Raspberry Pi에서 확인한다. |
| 가상환경·캐시 | 의존성 목록을 확정한 뒤 새 PC에서 생성. 기존 `setup.py`의 샘플 설정을 그대로 신뢰하지 않는다. |

Cloud에서는 소스 검토·문법 확인까지만 진행한다. 카메라·GPIO·전체 통합 동작은 실제 장치 검증 전까지 미확인이다.

## 대화와 코드 이어가기

- 이 저장소를 연결한 Cloud 작업은 웹에서 같은 작업을 다시 열어 이어간다. 로컬 채팅이 Git으로 이동하거나 기존 채팅이 Cloud로 자동 이전되는 것은 아니다.
- 작업 시작: `git status --short --branch`로 현재 변경과 브랜치를 확인한다. 다른 작업이 있으면 강제 초기화하지 않는다.
- 처음에는 `git clone` 후 아래 지정 브랜치로 전환한다. 다음부터 같은 브랜치에서 `git pull --ff-only`한다. 충돌·분기가 있으면 중단해 확인한다.
- 작업 종료: HANDOFF.md의 완료·미완료·실행한 검증·다음 명령을 갱신하고 검토한 소스만 commit/push한다. `.env`, 로그인 쿠키, 실제 키, 가상환경은 올리지 않는다.
- 새 로컬 Codex 대화의 첫 요청: “AGENTS.md가 있으면 먼저 읽고, RESTART.md와 HANDOFF.md를 읽어 현재 브랜치·실제 파일을 대조한 뒤 이어서 작업해 줘. 없는 설정은 예시에서 생성하되 기존 파일을 덮어쓰지 말고, 비밀 값은 출력하지 마.”
- Cloud 환경 생성/게시 여부, 패키지 설치 여부, 실제 서비스 동작은 각각 확인한다. 이 문서 파일의 존재만으로 등록·실행 성공을 주장하지 않는다.
