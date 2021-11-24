from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
BACKGROUND_WIDTH = 800
BACKGROUND_HEIGHT = 526

window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flashy")

# Load images
card_front_img = PhotoImage(file="images/card_front.png")
right_btn_img = PhotoImage(file='images/right.png')
wrong_btn_img = PhotoImage(file='images/wrong.png')

# Card front
canvas = Canvas(width=BACKGROUND_WIDTH, height=BACKGROUND_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(BACKGROUND_WIDTH/2, BACKGROUND_HEIGHT/2, image=card_front_img)

canvas.create_text(400,150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400,260, text="word", font=("Ariel", 60, "bold"))
wrong_button = Button(image=wrong_btn_img, highlightthickness=0)
right_button = Button(image=right_btn_img, highlightthickness=0)

canvas.grid(column=0, row=0, columnspan=2)
wrong_button.grid(column=0, row=1)
right_button.grid(column=1, row=1)

window.mainloop()