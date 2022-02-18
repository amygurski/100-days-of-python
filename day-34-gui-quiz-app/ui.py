from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizIterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        true_btn_img = PhotoImage(file='images/true.png')
        false_btn_img = PhotoImage(file='images/false.png')

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)

        self.question_text = self.canvas.create_text(
            150, 
            125, 
            width = 280,
            text="Question Text", 
            font=("Ariel", 20, "italic"), 
            fill=THEME_COLOR
        )
        
        self.true_button = Button(image=true_btn_img, highlightthickness=0, command=self.true_pressed)
        self.false_button = Button(image=false_btn_img, highlightthickness=0, command=self.false_pressed)
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.score_label.grid(column=1, row=0)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
        else: 
            self.canvas.itemconfig(
                self.question_text, 
                text=f"You have reached the end of the quiz!\nFinal Score: {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)