import html


class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = question_list
        self.current_question = ""

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        self.current_question = self.questions_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text} "
        # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        # self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer) -> bool:
        if str(user_answer) == self.current_question.answer:
            return True
        else:
            return False

