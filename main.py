from question_model import Question
from quiz_brain import QuizBrain
from data import Data
from ui import QuizInterface

question_bank = []
ques = Data()
question_list = ques.load_questions_from_api()
for ques in question_list:
    question_bank.append(Question(ques["question"], ques["correct_answer"]))

quiz_brain = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz_brain)
