from tkinter import *

THEME_COLOR = "#375362"

class QuizIterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        true_btn_img = PhotoImage(file='images/true.png')
        false_btn_img = PhotoImage(file='images/false.png')

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)

        self.question_text = self.canvas.create_text(
            150, 
            125, 
            text="Question Text", 
            font=("Ariel", 20, "italic"), 
            fill=THEME_COLOR
        )
        
        self.true_button = Button(image=true_btn_img, highlightthickness=0)
        self.false_button = Button(image=false_btn_img, highlightthickness=0)
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.score_label.grid(column=1, row=0)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)
        self.window.mainloop()
