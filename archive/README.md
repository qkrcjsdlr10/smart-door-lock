# 구버전 및 실험 코드 보관

현재 기준 코드는 루트의 `src/`입니다. 이 폴더에는 이전 사본, 개별 실험 코드, 정리한 압축파일을 보관합니다. 기능 통합은 하지 않았으며 개인정보가 포함된 사진·작성자 정보·캐시를 제거했습니다.

## 위치 변경 안내

| 기존 위치 | 현재 위치 | 내용 |
|---|---|---|
| `새 폴더 (2)/door/` | `versions/door/` | 카메라 영상·등록 패널을 포함한 이전 사본 |
| `새 폴더 (2)/smartdoor/` | `versions/smartdoor/` | 카메라·GUI·검출 스레드 연결 시도 및 OpenCV 보조 코드 |
| `새 폴더 (2)/SmartDoor-master_(11.24)/` | `versions/SmartDoor-master_(11.24)/` | 루트와 동일한 주요 Python 파일을 가진 사본 |
| `새 폴더 (2)/facedetect.py` | `experiments/facedetect.py` | 얼굴·눈 검출 예제 |
| `새 폴더 (2)/facedetect_.py` | `experiments/facedetect_.py` | 이미지 저장 실험 |
| `새 폴더 (2)/facedetect_10_13.py` | `experiments/facedetect_10_13.py` | 얼굴 검출 후 전체 프레임 저장 |
| `새 폴더 (2)/facedetect_10_13 (1).py` | `experiments/facedetect_10_13 (1).py` | 라즈베리파이 절대 경로 사용 사본 |
| `새 폴더 (2)/tkinter_cam.py` | `experiments/tkinter_cam.py` | Tkinter 영상 표시 실험 |
| `새 폴더 (2)/SmartDoor-master_(11.24).zip` | `packages/SmartDoor-master_(11.24).zip` | 내부 개인정보 제거 후 재작성 |
| `새 폴더 (2)/smartdoor10_20.7z` | `packages/smartdoor10_20.zip` | 개인정보 제거 후 ZIP으로 대체 |
| `새 폴더 (2)/smartdoor_1117.7z` | `packages/smartdoor_1117.zip` | 개인정보 제거 후 ZIP으로 대체 |

현재 위치는 `archive/` 기준입니다. 이름의 날짜는 기존 이름을 보존한 것으로 버전 순서나 테스트 완료 여부를 보증하지 않습니다.

## 담당 기능 확인 위치

[experiments/facedetect_10_13.py](experiments/facedetect_10_13.py)에 얼굴 검출·로컬 저장 코드가 있습니다. 얼굴 검출 시 전체 프레임을 `self camera test1.jpg`에 덮어씁니다. 현재 메인 화면에는 연결되지 않았습니다.

## 실행 및 자료 참고

보관 코드는 보조 모듈, Cascade XML, OpenCV 예제 데이터에 의존합니다. 홈 경로의 사용자명은 익명화한 예시로 변경했습니다. 개인 사진 표시를 제거하고 고정 비밀번호는 환경변수로 변경했습니다. 의존성과 장치 경로를 정비한 것은 아니므로 바로 실행된다고 보장하지 않습니다.

개인정보를 제거한 발표자료는 루트의 `docs/presentations/`에 있습니다. HWP는 익명화한 TXT 본문으로 변환해 `docs/reports/`에 보존하고 원본은 삭제했습니다. 텍스트 메모는 `docs/notes/개발환경_참고자료_작업메모.txt`로 제목과 내용을 정리했습니다.
