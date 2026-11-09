
import json
from pathlib import Path
from quiz import Quiz


class QuizGame:
    """퀴즈 게임 전체를 관리하는 클래스"""

    def __init__(self):
        self.quizzes = []
        self.best_score = None
        self.state_file = Path(__file__).parent / "state.json"
        self.load_state()

    def load_default_quizzes(self):
        """기본 퀴즈 5개를 생성합니다."""
        return [
            Quiz(
                "Python 기초",
                "Python에서 화면에 글자를 출력하는 함수는?",
                ["input()", "print()", "int()", "str()"],
                2,
                "print() 함수는 화면에 값을 출력합니다."
            ),
            Quiz(
                "자료형",
                "Python에서 문자열 자료형을 나타내는 것은?",
                ["int", "str", "list", "dict"],
                2,
                "str은 문자열 자료형입니다."
            ),
            Quiz(
                "조건문",
                "조건이 참일 때 실행되는 구문은?",
                ["for", "while", "if", "def"],
                3,
                "if문은 조건에 따라 코드를 실행합니다."
            ),
            Quiz(
                "반복문",
                "정해진 횟수만큼 반복할 때 주로 사용하는 구문은?",
                ["if", "for", "class", "return"],
                2,
                "for문은 반복 가능한 객체의 요소를 순회합니다."
            ),
            Quiz(
                "리스트",
                "Python에서 리스트를 만드는 기호는?",
                ["{}", "()", "[]", "<>"],
                3,
                "대괄호 []를 사용하여 리스트를 만듭니다."
            )
        ]

    def load_state(self):
        """JSON 파일에서 퀴즈와 최고 점수를 불러옵니다."""

        if not self.state_file.exists():
            self.quizzes = self.load_default_quizzes()
            self.save_state()
            return

        try:
            with open(self.state_file, "r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, dict):
                raise ValueError("데이터 형식이 올바르지 않습니다.")

            saved_quizzes = data.get("quizzes", [])

            if not isinstance(saved_quizzes, list):
                raise ValueError("퀴즈 데이터 형식이 올바르지 않습니다.")

            loaded_quizzes = []

            for item in saved_quizzes:
                if not isinstance(item, dict):
                    raise ValueError("퀴즈 항목 형식이 올바르지 않습니다.")

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
                    or not isinstance(quiz.answer, int)
                    or isinstance(quiz.answer, bool)
                    or not 1 <= quiz.answer <= len(quiz.options)
                    or not isinstance(quiz.explanation, str)
                ):
                    raise ValueError("퀴즈 데이터가 올바르지 않습니다.")

                loaded_quizzes.append(quiz)

            saved_score = data.get("best_score")

            if (
                saved_score is not None
                and (
                    not isinstance(saved_score, int)
                    or isinstance(saved_score, bool)
                    or saved_score < 0
                )
            ):
                raise ValueError("최고 점수 데이터가 올바르지 않습니다.")

            self.quizzes = loaded_quizzes or self.load_default_quizzes()
            self.best_score = saved_score

            if not loaded_quizzes:
                self.save_state()

        except (
            json.JSONDecodeError,
            OSError,
            ValueError,
            KeyError,
            TypeError
        ):
            print("저장 데이터에 문제가 있어 기본 퀴즈로 시작합니다.")
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
            with open(self.state_file, "w", encoding="utf-8") as file:
                json.dump(
                    data,
                    file,
                    ensure_ascii=False,
                    indent=4
                )

        except OSError:
            print("데이터 저장 중 오류가 발생했습니다.")

    def add_quiz(self, quiz):
        """새로운 퀴즈를 추가합니다."""

        if not isinstance(quiz, Quiz):
            print("올바른 퀴즈 객체가 아닙니다.")
            return

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
            or not isinstance(quiz.answer, int)
            or isinstance(quiz.answer, bool)
            or not 1 <= quiz.answer <= len(quiz.options)
            or not isinstance(quiz.explanation, str)
        ):
            print("퀴즈 정보가 올바르지 않습니다.")
            return

        self.quizzes.append(quiz)
        self.save_state()
        print("퀴즈가 추가되었습니다.")

    def show_quizzes(self):
        """등록된 퀴즈 목록을 출력합니다."""

        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        print("\n===== 퀴즈 목록 =====")

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"{index}. [{quiz.topic}] {quiz.question}")

        print(f"\n총 {len(self.quizzes)}개의 퀴즈가 등록되어 있습니다.")

    def get_quizzes_by_topic(self, topic):
        """주제에 해당하는 퀴즈를 반환합니다."""

        return [
            quiz for quiz in self.quizzes
            if quiz.topic == topic
        ]

    def get_quiz_count(self):
        """등록된 퀴즈 개수를 반환합니다."""

        return len(self.quizzes)

    def update_best_score(self, score):
        """최고 점수를 갱신하고 저장합니다."""

        if (
            not isinstance(score, int)
            or isinstance(score, bool)
            or score < 0
        ):
            print("올바르지 않은 점수입니다.")
            return

        if self.best_score is None or score > self.best_score:
            self.best_score = score
            self.save_state()

    def show_best_score(self):
        """최고 점수를 출력합니다."""

        if self.best_score is None:
            print("아직 기록된 점수가 없습니다.")
        else:
            print(f"현재 최고 점수: {self.best_score}")

    def play_quiz(self):
        """퀴즈를 진행하고 결과를 출력합니다."""

        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        score = 0
        total = len(self.quizzes)

        print("\n===== 퀴즈 시작 =====")

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[{index}/{total}] [{quiz.topic}]")
            print(quiz.question)

            for option_index, option in enumerate(
                quiz.options, start=1
            ):
                print(f"{option_index}. {option}")

            while True:
                user_input = input("정답 번호를 입력하세요: ").strip()

                if not user_input:
                    print("번호를 입력해 주세요.")
                    continue

                try:
                    user_answer = int(user_input)

                except ValueError:
                    print("숫자로 입력해 주세요.")
                    continue

                if not 1 <= user_answer <= len(quiz.options):
                    print(
                        f"1~{len(quiz.options)} 사이의 번호를 입력해 주세요."
                    )
                    continue

                break

            if quiz.check_answer(user_answer):
                print("정답입니다!")
                score += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

            print("해설:", quiz.explanation)

        print("\n===== 퀴즈 결과 =====")
        print(f"총 문제 수: {total}")
        print(f"맞힌 문제 수: {score}")
        print(f"점수: {score} / {total}")

        if self.best_score is None or score > self.best_score:
            self.update_best_score(score)
            print("최고 점수가 갱신되었습니다!")
        else:
            print(f"현재 최고 점수: {self.best_score}")


if __name__ == "__main__":
    game = QuizGame()

    print("등록된 퀴즈 수:", game.get_quiz_count())
    game.show_quizzes()
    game.show_best_score()
