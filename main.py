
def show_menu():
    """메인 메뉴를 화면에 출력하는 함수"""

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
    """사용자에게 메뉴 번호를 입력받는 함수"""

    while True:
        choice = input("선택: ").strip()

        # 빈 입력 확인
        if choice == "":
            print("⚠️ 메뉴 번호를 입력해 주세요.")
            continue

        # 숫자 입력 확인
        try:
            choice = int(choice)

        except ValueError:
            print("⚠️ 숫자로 입력해 주세요.")
            continue

        # 메뉴 범위 확인
        if choice < 1 or choice > 5:
            print("⚠️ 1~5 사이의 숫자를 입력해 주세요.")
            continue

        return choice


def main():
    """프로그램 실행 함수"""

    print("퀴즈 게임을 시작합니다!")

    while True:

        # 메뉴 출력
        show_menu()

        # 사용자 입력
        choice = get_menu_choice()

        # 선택에 따른 기능 실행
        if choice == 1:
            print("📝 퀴즈 풀기 기능은 다음 단계에서 구현합니다.")

        elif choice == 2:
            print("📌 퀴즈 추가 기능은 다음 단계에서 구현합니다.")

        elif choice == 3:
            print("📋 퀴즈 목록 기능은 다음 단계에서 구현합니다.")

        elif choice == 4:
            print("🏆 점수 확인 기능은 다음 단계에서 구현합니다.")

        elif choice == 5:
            print("👋 퀴즈 게임을 종료합니다.")
            break


if __name__ == "__main__":
    try:
        main()

    except (KeyboardInterrupt, EOFError):
        print("\n프로그램 종료 요청을 확인했습니다.")
        print("안전하게 프로그램을 종료합니다.")
