
import json
from pathlib import Path

from quiz import Quiz


class QuizGame:
    """여러 퀴즈와 최고 점수를 관리하는 클래스"""

    def __init__(self):
        self.quizzes = []
        self.best_score = None

        # 프로젝트 루트의 state.json 경로
        self.state_file = Path(__file__).parent / "state.json"

        # 저장된 데이터 불러오기
        self.load_state()

    def load_default_quizzes(self):
        """기본 퀴즈 5개를 준비합니다."""

        return [
            Quiz(
                "Python 기초",
                "Python에서 화면에 글자를 출력하는 함수는?",
                ["input()", "print()", "int()", "str()"],
                2,
                "print() 함수는 화면에 값을 출력합니다."
            ),
            Quiz(
                "Python 자료형",
                "문자열을 나타내는 자료형은?",
                ["int", "str", "float", "bool"],
                2,
                "str은 문자열을 나타내는 자료형입니다."
            ),
            Quiz(
                "Python 조건문",
                "조건이 참일 때 실행되는 코드를 작성하는 키워드는?",
                ["for", "while", "if", "def"],
                3,
                "if문은 조건이 참인지 확인합니다."
            ),
            Quiz(
                "Python 반복문",
                "정해진 횟수만큼 반복할 때 주로 사용하는 반복문은?",
                ["if", "for", "class", "return"],
                2,
                "for문은 반복 가능한 객체를 순서대로 처리합니다."
            ),
            Quiz(
                "Python 리스트",
                "리스트의 마지막에 요소를 추가하는 메서드는?",
                ["add()", "insert()", "append()", "remove()"],
                3,
                "append()는 리스트의 마지막에 요소를 추가합니다."
            )
        ]

    def load_state(self):
        """JSON 파일에서 퀴즈와 최고 점수를 불러옵니다."""

        try:
            if not self.state_file.exists():
                print("저장 파일이 없습니다. 기본 퀴즈를 불러옵니다.")
                self.quizzes = self.load_default_quizzes()
                self.best_score = None
                self.save_state()
                return

            with self.state_file.open("r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, dict):
                raise ValueError("저장 데이터 형식이 올바르지 않습니다.")

            saved_quizzes = data.get("quizzes", [])
            saved_score = data.get("best_score")

            if not isinstance(saved_quizzes, list):
                raise ValueError("퀴즈 목록 형식이 올바르지 않습니다.")

            if saved_score is not None:
                if (
                    isinstance(saved_score, bool)
                    or not isinstance(saved_score, int)
                    or saved_score < 0
                ):
                    raise ValueError("최고 점수 형식이 올바르지 않습니다.")

            loaded_quizzes = []

            for item in saved_quizzes:
                if not isinstance(item, dict):
                    raise ValueError("퀴즈 데이터 형식이 올바르지 않습니다.")

                quiz = Quiz.from_dict(item)

                if (
                    not isinstance(quiz.topic, str)
                    or not quiz.topic.strip()
                    or not isinstance(quiz.question, str)
                    or not quiz.question.strip()
                    or not isinstance(quiz.options, list)
                    or len(quiz.options) < 2
                    or not all(
                        isinstance(option, str) and option.strip()
                        for option in quiz.options
                    )
                    or isinstance(quiz.answer, bool)
                    or not isinstance(quiz.answer, int)
                    or not 1 <= quiz.answer <= len(quiz.options)
                    or not isinstance(quiz.explanation, str)
                ):
                    raise ValueError("퀴즈 내용이 올바르지 않습니다.")

                loaded_quizzes.append(quiz)

            self.quizzes = loaded_quizzes
            self.best_score = saved_score

            # 저장된 퀴즈가 비어 있으면 기본 퀴즈 사용
            if not self.quizzes:
                self.quizzes = self.load_default_quizzes()

            print("저장된 데이터를 불러왔습니다.")

        except (json.JSONDecodeError, OSError, ValueError, KeyError, TypeError) as error:
            print("저장 파일을 읽을 수 없습니다.")
            print("기본 퀴즈로 다시 시작합니다.")
            print("오류 내용:", error)

            self.quizzes = self.load_default_quizzes()
            self.best_score = None
            self.save_state()

    def save_state(self):
        """퀴즈와 최고 점수를 JSON 파일에 저장합니다."""

        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score
        }

        try:
            with self.state_file.open("w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

            print("데이터를 저장했습니다.")

        except OSError as error:
            print("데이터 저장에 실패했습니다:", error)

    def add_quiz(self, quiz):
        """새로운 퀴즈를 추가합니다."""

        if not isinstance(quiz, Quiz):
            raise TypeError("Quiz 객체만 추가할 수 있습니다.")

        self.quizzes.append(quiz)
        self.save_state()
        print("새로운 퀴즈가 추가되었습니다.")

    def show_quizzes(self):
        """전체 퀴즈 목록을 출력합니다."""

        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        print("\n========== 퀴즈 목록 ==========")

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"{index}. [{quiz.topic}] {quiz.question}")

        print(f"\n총 {len(self.quizzes)}개의 퀴즈가 있습니다.")

    def get_quizzes_by_topic(self, topic):
        """주제별 퀴즈를 검색합니다."""

        return [
            quiz for quiz in self.quizzes
            if quiz.topic == topic
        ]

    def get_quiz_count(self):
        """퀴즈 개수를 반환합니다."""

        return len(self.quizzes)

    def update_best_score(self, score):
        """최고 점수를 갱신합니다."""

        if isinstance(score, bool) or not isinstance(score, int) or score < 0:
            raise ValueError("점수는 0 이상의 정수여야 합니다.")

        if self.best_score is None or score > self.best_score:
            self.best_score = score
            self.save_state()
            print("최고 점수가 갱신되었습니다.")
        else:
            print("기존 최고 점수를 유지합니다.")


if __name__ == "__main__":

    game = QuizGame()

    print("\n현재 퀴즈 개수:", game.get_quiz_count())
    print("현재 최고 점수:", game.best_score)

    game.show_quizzes()

    # 테스트용 퀴즈 추가
    test_quiz = Quiz(
        "Python 함수",
        "함수를 정의할 때 사용하는 키워드는?",
        ["class", "def", "import", "return"],
        2,
        "def 키워드로 함수를 정의합니다."
    )

    game.add_quiz(test_quiz)

    # 최고 점수 저장 테스트
    game.update_best_score(3)

    print("\n저장 테스트가 완료되었습니다.")
