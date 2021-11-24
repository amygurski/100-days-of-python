from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
BACKGROUND_WIDTH = 800
BACKGROUND_HEIGHT = 526

german_words_dict = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/german_words.csv")
    german_words_dict = original_data.to_dict(orient="records")
else:
    german_words_dict = data.to_dict(orient="records")

def get_new_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(german_words_dict)
    canvas.itemconfig(card_word, text=current_card["German"], fill="black")
    canvas.itemconfig(language, text="German", fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(canvas_image, image=card_back_img)

def remove_word():
    german_words_dict.remove(current_card)
    data = pandas.DataFrame(german_words_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    get_new_word()

# ---------------------------- UI ------------------------------- #
window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flashy")

flip_timer = window.after(3000, flip_card)

# Load images
card_front_img = PhotoImage(file="images/card_front.png")
right_btn_img = PhotoImage(file='images/right.png')
wrong_btn_img = PhotoImage(file='images/wrong.png')
card_back_img = PhotoImage(file='images/card_back.png')

# Card front
canvas = Canvas(width=BACKGROUND_WIDTH, height=BACKGROUND_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(BACKGROUND_WIDTH/2, BACKGROUND_HEIGHT/2, image=card_front_img)

language = canvas.create_text(400,150, text="German", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400,260, text="", font=("Ariel", 60, "bold"))
wrong_button = Button(image=wrong_btn_img, highlightthickness=0, command=get_new_word)
right_button = Button(image=right_btn_img, highlightthickness=0, command=remove_word)

canvas.grid(column=0, row=0, columnspan=2)
wrong_button.grid(column=0, row=1)
right_button.grid(column=1, row=1)

get_new_word()

window.mainloop()