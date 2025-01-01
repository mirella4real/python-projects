from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
BACKGROUND_COLOR = "#ffffff"
FONT = ("Arial", 20, "italic")
FONT_SCORE = ("Arial", 14, "normal")
SCORE_LABEL = "Score:"
END_MESSAGE = "You've finished the quiz!"
FINAL_SCORE = "Your final score was:"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.app_window = Tk()
        self.app_window.title("Quizzler")
        self.app_window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text=f"{SCORE_LABEL} 0", fg="white", bg=THEME_COLOR, font=FONT_SCORE)
        self.score_label.grid(row=0, column=1, sticky="nsew")

        self.app_canvas = Canvas(width=300, height=250, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.question_text = self.app_canvas.create_text(
            150, 
            125, 
            width=280,
            text=" ", 
            fill="black", 
            font=FONT
        )
        self.app_canvas.grid(row=1, column=0, columnspan=2, pady=30)
        self.show_new_question()

        self.true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=self.true_image, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2, pady=20)

        self.false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=self.false_image, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2, pady=20)

        self.app_window.mainloop()

    def true_pressed(self):
        self.check_answer("true")
    
    def false_pressed(self):
        self.check_answer("false")

    def give_feedback(self, is_correct):
        if is_correct == True:
            self.app_canvas.config(bg="#008000")
        else:
            self.app_canvas.config(bg="#ff0000")

    def check_answer(self, response):
        is_correct = self.quiz.check_answer(response)
        self.give_feedback(is_correct)
        self.app_window.after(1000, self.show_new_question)

    def end_quiz(self):
        self.false_button.config(state="disabled")
        self.true_button.config(state="disabled")
        score = self.quiz.get_score()
        self.app_canvas.itemconfig(self.question_text, text=f"{END_MESSAGE}\n{FINAL_SCORE} {score}")

    def show_new_question(self):
        self.app_canvas.config(bg="#ffffff")
        score = self.quiz.get_score()
        self.score_label.config(text=f"{SCORE_LABEL} {score}")
        if self.quiz.has_questions_left():
            question = self.quiz.next_question()
            self.app_canvas.itemconfig(self.question_text, text=f"Q.{question.number}: {question.text}")
        else:
            self.end_quiz()




    