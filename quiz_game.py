from quiz import Quiz


class QuizGame:
    """여러 퀴즈를 관리하는 클래스"""

    def __init__(self):
        """기본 퀴즈 목록을 생성합니다."""

        self.quizzes = []

        # 기본 퀴즈 5개 추가
        self.load_default_quizzes()

    def load_default_quizzes(self):
        """게임 시작 시 사용할 기본 퀴즈를 준비합니다."""

        default_quizzes = [
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
                "str은 문자열(String)을 나타내는 자료형입니다."
            ),
            Quiz(
                "Python 조건문",
                "조건이 참일 때 실행되는 코드를 작성하는 키워드는?",
                ["for", "while", "if", "def"],
                3,
                "if문은 조건이 참인지 확인하여 코드를 실행합니다."
            ),
            Quiz(
                "Python 반복문",
                "정해진 횟수만큼 반복할 때 주로 사용하는 반복문은?",
                ["if", "for", "class", "return"],
                2,
                "for문은 반복 가능한 객체의 요소를 순서대로 처리합니다."
            ),
            Quiz(
                "Python 리스트",
                "리스트의 마지막에 요소를 추가하는 메서드는?",
                ["add()", "insert()", "append()", "remove()"],
                3,
                "append()는 리스트의 마지막에 요소를 추가합니다."
            )
        ]

        self.quizzes.extend(default_quizzes)

    def add_quiz(self, quiz):
        """새로운 퀴즈를 목록에 추가합니다."""

        if not isinstance(quiz, Quiz):
            raise TypeError("Quiz 객체만 추가할 수 있습니다.")

        self.quizzes.append(quiz)
        print("새로운 퀴즈가 추가되었습니다.")

    def show_quizzes(self):
        """등록된 모든 퀴즈의 목록을 출력합니다."""

        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        print("\n========== 퀴즈 목록 ==========")

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"{index}. [{quiz.topic}] {quiz.question}")

        print(f"\n총 {len(self.quizzes)}개의 퀴즈가 등록되어 있습니다.")

    def get_quizzes_by_topic(self, topic):
        """입력한 주제와 일치하는 퀴즈를 반환합니다."""

        return [
            quiz for quiz in self.quizzes
            if quiz.topic == topic
        ]

    def get_quiz_count(self):
        """등록된 퀴즈의 개수를 반환합니다."""

        return len(self.quizzes)


if __name__ == "__main__":

    # 게임 객체 생성
    game = QuizGame()

    # 기본 퀴즈 목록 출력
    game.show_quizzes()

    # 퀴즈 개수 확인
    print("\n퀴즈 개수:", game.get_quiz_count())

    # 새로운 퀴즈 추가
    new_quiz = Quiz(
        "Python 함수",
        "함수를 정의할 때 사용하는 키워드는?",
        ["class", "def", "import", "return"],
        2,
        "def 키워드로 함수를 정의합니다."
    )

    game.add_quiz(new_quiz)

    # 추가 후 목록 확인
    game.show_quizzes()

    # 주제별 퀴즈 검색
    print("\n========== Python 기초 주제 검색 ==========")
    results = game.get_quizzes_by_topic("Python 기초")

    for quiz in results:
        print(quiz.question)