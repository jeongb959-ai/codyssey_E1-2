
from quiz import Quiz
from quiz_game import QuizGame


def show_menu():
    """메인 메뉴를 출력합니다."""

    print("\n========================================")
    print("        🎯 나만의 퀴즈 게임 🎯")
    print("========================================")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("========================================")


def get_menu_choice():
    """메뉴 번호를 입력받고 유효성을 검사합니다."""

    while True:
        choice = input("선택: ").strip()

        if not choice:
            print("⚠️ 메뉴 번호를 입력해 주세요.")
            continue

        try:
            choice = int(choice)

        except ValueError:
            print("⚠️ 숫자로 입력해 주세요.")
            continue

        if not 1 <= choice <= 5:
            print("⚠️ 1~5 사이의 숫자를 입력해 주세요.")
            continue

        return choice


def add_new_quiz(game):
    """사용자로부터 새 퀴즈를 입력받습니다."""

    print("\n===== 퀴즈 추가 =====")

    topic = input("퀴즈 주제: ").strip()

    if not topic:
        print("주제를 입력해 주세요.")
        return

    question = input("질문: ").strip()

    if not question:
        print("질문을 입력해 주세요.")
        return

    options = []

    print("\n선택지를 4개 입력해 주세요.")

    for index in range(1, 5):
        option = input(f"{index}번 선택지: ").strip()

        if not option:
            print("선택지는 비워둘 수 없습니다.")
            return

        options.append(option)

    while True:
        answer_input = input("정답 번호(1~4): ").strip()

        if not answer_input:
            print("정답 번호를 입력해 주세요.")
            continue

        try:
            answer = int(answer_input)

        except ValueError:
            print("숫자로 입력해 주세요.")
            continue

        if 1 <= answer <= 4:
            break

        print("1~4 사이의 숫자를 입력해 주세요.")

    explanation = input("정답 해설: ").strip()

    if not explanation:
        explanation = "등록된 해설이 없습니다."

    new_quiz = Quiz(
        topic,
        question,
        options,
        answer,
        explanation
    )

    game.add_quiz(new_quiz)


def main():
    """퀴즈 게임을 실행합니다."""

    game = QuizGame()

    print("퀴즈 게임을 시작합니다!")

    while True:
        show_menu()
        choice = get_menu_choice()

        if choice == 1:
            game.play_quiz()

        elif choice == 2:
            add_new_quiz(game)

        elif choice == 3:
            game.show_quizzes()

        elif choice == 4:
            game.show_best_score()

        elif choice == 5:
            print("👋 퀴즈 게임을 종료합니다.")
            break


if __name__ == "__main__":
    try:
        main()

    except (KeyboardInterrupt, EOFError):
        print("\n프로그램 종료 요청을 확인했습니다.")
        print("안전하게 프로그램을 종료합니다.")
