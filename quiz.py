class Quiz:
    """퀴즈 하나의 정보를 관리하는 클래스"""

    def __init__(self, topic, question, options, answer, explanation):
        """
        퀴즈 객체를 생성합니다.

        topic: 퀴즈 주제
        question: 질문 내용
        options: 보기 목록
        answer: 정답 번호 (1부터 시작)
        explanation: 정답 해설
        """

        self.topic = topic
        self.question = question
        self.options = options
        self.answer = answer
        self.explanation = explanation

    def check_answer(self, user_answer):
        """사용자의 답이 정답인지 확인합니다."""

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
        """딕셔너리 데이터를 Quiz 객체로 변환합니다."""

        return cls(
            topic=data["topic"],
            question=data["question"],
            options=data["options"],
            answer=data["answer"],
            explanation=data["explanation"]
        )
        