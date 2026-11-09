# Codyssey_E1-2
# 🎯 나만의 퀴즈 게임

## 1. 프로젝트 개요

Python을 활용하여 제작한 콘솔 기반 퀴즈 게임입니다.

사용자는 주제별 퀴즈를 풀고, 새로운 퀴즈를 추가하며, 자신의 최고 점수를 확인할 수 있습니다.

퀴즈 데이터와 최고 점수는 JSON 파일에 저장되므로 프로그램을 종료하고 다시 실행해도 데이터가 유지됩니다.

## 2. 주제 선정 이유

Python 기초 문법과 객체지향 프로그래밍을 실습하기 위해 퀴즈 게임을 프로젝트 주제로 선정했습니다.

클래스, 함수, 조건문, 반복문, 예외 처리 및 JSON 파일 입출력을 실제 프로그램에 적용하여 Python 프로그래밍의 기본 개념을 익히고자 했습니다.

## 3. 개발 환경

| 항목 | 사용 환경 |
|---|---|
| 프로그래밍 언어 | Python 3.10 이상 |
| 개발 도구 | Visual Studio Code |
| 운영 환경 | Windows / PowerShell |
| 버전 관리 | Git |
| 원격 저장소 | GitHub |
| 데이터 저장 | JSON |
| 라이브러리 | Python 표준 라이브러리 |

## 4. 실행 방법

### 4-1. 프로젝트 다운로드

GitHub 저장소를 Clone 합니다.

```bash
git clone https://github.com/jeongb959-ai/codyssey_E1-2.git
```

### 4-2. 프로젝트 폴더 이동

```bash
cd codyssey_E1-2
```

### 4-3. 프로그램 실행

```bash
py main.py
```

## 5. 주요 기능

### 5-1. 퀴즈 풀기
- 등록된 퀴즈 출제
- 선택지를 통한 정답 입력
- 정답 및 오답 확인
- 정답 해설 출력
- 점수 계산 및 최고 점수 갱신

### 5-2. 퀴즈 추가
- 퀴즈 주제 입력
- 질문 및 선택지 입력
- 정답 번호 입력
- 정답 해설 입력
- 새로운 퀴즈 등록 및 저장

### 5-3. 퀴즈 목록
- 등록된 퀴즈 전체 확인
- 퀴즈 주제 및 질문 확인

### 5-4. 점수 확인
- 최고 점수 확인
- 퀴즈 플레이 결과 확인

### 5-5. 데이터 관리
- JSON 파일에 퀴즈 데이터 저장
- JSON 파일에서 데이터 불러오기
- 프로그램 재실행 후 데이터 유지
- JSON 파일이 없거나 손상된 경우 기본 퀴즈로 실행

### 5-6. 예외 처리
- 잘못된 메뉴 입력 처리
- 숫자가 아닌 입력 처리
- 빈 입력 처리
- 입력 범위 검증
- Ctrl+C 및 EOFError 발생 시 안전 종료

## 6. 파일 구조

```text
codyssey_E1-2/
├── main.py
├── quiz.py
├── quiz_game.py
├── state.json
├── README.md
├── .gitignore
└── docs/
    └── screenshots/
        ├── JSON 데이터 저장.png
        ├── main, quiz.py 등 표시 화면.png
        ├── PowerShell에서 py main.py 실행.png
        ├── Python 코드가 작성된 화면.png
        ├── 깃_버전.png
        ├── 점수 확인.png
        ├── 퀴즈 게임 메뉴 1~5번 표시.png
        ├── 퀴즈 목록 확인.png
        ├── 퀴즈 추가.png
        ├── 퀴즈 플레이.png
        └── 파이썬_버전.png
```

## 7. 주요 클래스

### 7-1. Quiz

퀴즈 하나의 정보를 관리하는 클래스입니다.

- 퀴즈 주제 관리
- 질문 관리
- 선택지 관리
- 정답 및 해설 관리
- 정답 확인
- 퀴즈 데이터를 Dictionary 형태로 변환
- Dictionary 데이터를 Quiz 객체로 변환

### 7-2. QuizGame

퀴즈 게임 전체 기능을 관리하는 클래스입니다.

- 기본 퀴즈 생성
- 퀴즈 추가 및 목록 출력
- 퀴즈 플레이
- 정답 및 점수 계산
- 최고 점수 관리
- JSON 데이터 저장 및 불러오기

## 8. state.json 설명

`state.json`은 프로젝트에서 사용하는 퀴즈 데이터와 최고 점수를 저장하는 파일입니다.

| 항목 | 설명 |
|---|---|
| quizzes | 등록된 퀴즈 목록 |
| best_score | 최고 점수 |

UTF-8 인코딩과 JSON 형식을 사용하여 한글 데이터도 저장할 수 있습니다.

프로그램을 실행하면 저장된 데이터를 불러오며, 퀴즈를 추가하거나 최고 점수가 갱신되면 파일에 변경 내용을 저장합니다.

## 9. 실행 화면 및 테스트 결과

프로그램의 주요 기능과 개발 환경을 확인할 수 있도록 실행 화면을 첨부했습니다.

### 9-1. 개발 환경

**Python 버전**

![Python 버전](<docs/screenshots/파이썬_버전.png>)

**프로젝트 파일 구성**

![프로젝트 파일 구성](<docs/screenshots/main, quiz.py 등 표시 화면.png>)

**Python 코드 작성 화면**

![Python 코드](<docs/screenshots/Python 코드가 작성된 화면.png>)

### 9-2. 프로그램 실행

**PowerShell에서 프로그램 실행**

![프로그램 실행](<docs/screenshots/PowerShell에서 py main.py 실행.png>)

**메인 메뉴**

![메인 메뉴](<docs/screenshots/퀴즈 게임 메뉴 1~5번 표시.png>)

### 9-3. 주요 기능 테스트

**퀴즈 플레이**

![퀴즈 플레이](<docs/screenshots/퀴즈 플레이.png>)

**퀴즈 추가**

![퀴즈 추가](<docs/screenshots/퀴즈 추가.png>)

**퀴즈 목록 확인**

![퀴즈 목록](<docs/screenshots/퀴즈 목록 확인.png>)

**점수 확인**

![점수 확인](<docs/screenshots/점수 확인.png>)

### 9-4. JSON 데이터 저장 확인

**JSON 파일에 퀴즈 및 점수 저장**

![JSON 데이터 저장](<docs/screenshots/JSON 데이터 저장.png>)

### 9-5. Git 및 개발 환경 확인

**Git 버전 확인**

![Git 버전](<docs/screenshots/깃_버전.png>)

## 10. Git 및 GitHub 관리

Git과 GitHub를 활용하여 프로젝트의 소스 코드를 관리했습니다.

- Git 저장소 초기화 및 원격 저장소 연결
- 기능별 커밋을 통한 변경 이력 관리
- 기능 개발 브랜치 생성
- 브랜치 작업 후 기본 브랜치에 병합
- GitHub 원격 저장소에 프로젝트 업로드
- `git clone`을 이용한 저장소 복제
- `git pull`을 이용한 원격 저장소 변경사항 가져오기

GitHub 저장소:

https://github.com/jeongb959-ai/codyssey_E1-2