# codyssey_E1-2
# 🎯 나만의 Python 퀴즈 게임

## 1. 프로젝트 개요

Python 프로그래밍 언어를 활용하여 제작하는 콘솔 기반 퀴즈 게임입니다.

사용자는 퀴즈를 풀고, 새로운 퀴즈를 등록하고, 등록된 퀴즈 목록과 최고 점수를 확인할 수 있습니다.

## 2. 퀴즈 주제 선정 이유

Python 프로그래밍의 기본 개념과 문법을 퀴즈 형식으로 학습하고 복습하기 위해 이 주제를 선정했습니다.

## 3. 개발 환경

- OS: Windows
- IDE: Visual Studio Code
- Language: Python 3.10 이상
- Version Control: Git / GitHub
- Data Storage: JSON

## 4. 실행 방법

프로젝트 폴더에서 다음 명령어를 실행합니다.

```powershell
py main.py
```

## 5. 주요 기능

- 퀴즈 풀기
- 퀴즈 추가
- 퀴즈 목록 확인
- 최고 점수 확인
- JSON 파일을 이용한 데이터 저장 및 불러오기

## 6. 프로젝트 파일 구조

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
```

## 7. 데이터 파일 설명

### state.json

프로젝트 루트에 위치하며 퀴즈 데이터와 최고 점수를 저장합니다.

기본 데이터 구조:

```json
{
    "quizzes": [],
    "best_score": null
}
```

- quizzes: 퀴즈 목록
- best_score: 최고 점수

## 8. 실행 화면
프로그램 구현 완료 후 실행 화면을 추가할 예정입니다.