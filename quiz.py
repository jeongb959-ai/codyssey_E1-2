class Quiz:
    """퀴즈 하나의 정보를 관리하는 클래스"""

    def __init__(self, topic, question, options, answer, explanation):
        self.topic = topic
        self.question = question
        self.options = options
        self.answer = answer
        self.explanation = explanation

    def check_answer(self, user_answer):
        """정답 여부를 확인합니다."""
        return user_answer == self.answer

    def to_dict(self):
        """퀴즈 객체를 딕셔너리로 변환합니다."""
        return {
            "topic": self.topic,
            "question": self.question,
            "options": self.options,
            "answer": self.answer,
            "explanation": self.explanation
        }

    @classmethod
    def from_dict(cls, data):
        """딕셔너리를 Quiz 객체로 변환합니다."""
        return cls(
            topic=data["topic"],
            question=data["question"],
            options=data["options"],
            answer=data["answer"],
            explanation=data["explanation"]
        )


# quiz.py 파일을 직접 실행했을 때만 테스트합니다.
if __name__ == "__main__":

    quiz = Quiz(
        topic="Python 기초",
        question="Python에서 화면에 글자를 출력하는 함수는?",
        options=["input()", "print()", "int()", "str()"],
        answer=2,
        explanation="print() 함수는 화면에 값을 출력합니다."
    )

    print("주제:", quiz.topic)
    print("질문:", quiz.question)

    for index, option in enumerate(quiz.options, start=1):
        print(f"{index}. {option}")

    print("\n정답 확인:")
    print("2번 선택:", quiz.check_answer(2))
    print("1번 선택:", quiz.check_answer(1))

    quiz_data = quiz.to_dict()
    print("\n딕셔너리 변환:")
    print(quiz_data)

    restored_quiz = Quiz.from_dict(quiz_data)
    print("\n복원된 퀴즈:")
    print(restored_quiz.question)