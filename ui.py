from tkinter import *

THEME_COLOUR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain):
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOUR)
        self.quiz_brain = quiz_brain

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text="question body", width=280, font=("Arial", 16,
                                                                                                      "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.current_score = 0

        self.score_label = Label(text=f"Score: {self.current_score}", bg=THEME_COLOUR, fg="white")
        self.score_label.grid(row=0, column=1)

        cross_image = PhotoImage(file="images/false.png")
        self.cross_button = Button(image=cross_image, highlightthickness=0, command=self.false_pressed)
        self.cross_button.grid(row=2, column=1)

        check_image = PhotoImage(file="images/true.png")
        self.check_button = Button(image=check_image, highlightthickness=0, command=self.true_pressed)
        self.check_button.grid(row=2, column=0)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            self.check_button.config(state="normal")
            self.cross_button.config(state="normal")
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You have reached the end of the quiz\n\n"
                                                            f"Your Score:{self.current_score}")

    def true_pressed(self):
        is_correct = self.quiz_brain.check_answer(True)
        self.give_feedback(is_correct)

    def false_pressed(self):
        is_correct = self.quiz_brain.check_answer(False)
        self.give_feedback(is_correct)

    def give_feedback(self, is_correct):
        self.check_button.config(state="disabled")
        self.cross_button.config(state="disabled")
        if is_correct:
            self.current_score += 1
            self.score_label.config(text=f"Score: {self.current_score}")
            self.canvas.config(bg="lime green")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="tomato")
            self.window.after(1000, self.get_next_question)


    # def check_answer(self, user_answer):
    #     self.quiz_brain.check_answer(user_answer)