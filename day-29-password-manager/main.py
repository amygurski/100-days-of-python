import pandas
import pyperclip
import string
from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_input.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(string.ascii_letters) for char in range(randint(8,10))]
    password_list += [choice(string.punctuation) for char in range(randint(2, 4))]
    password_list += [choice(string.digits) for char in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        user_confirm = messagebox.askokcancel(title=website, message=f"These are the details you entered:\nEmail: {email} "
                                                                     f"\nPassword: {password}\nIs it ok to save?")
        if user_confirm:
            new_password = [f"{website} | {email} | {password}"]
            new_csv = pandas.DataFrame(new_password)
            new_csv.to_csv("data.txt",header=None, index=None, mode='a')

            website_input.delete(0,END)
            password_input.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title = ("Password Manager")
window.config(padx=20,pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)

#Create widgets
website_label = Label(text="Website:")
website_input = Entry(width=40)
email_label = Label(text="Email/Username:")
email_input = Entry(width=40)
password_label = Label(text="Password:")
password_input = Entry(width=22)
generate_pw_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", width=38, command=save_password)

# Setup grid
canvas.grid(column=1, row=0)
website_label.grid(column=0, row=1, padx=10)
website_input.grid(column=1, row=1, columnspan=2)
email_label.grid(column=0, row=2)
email_input.grid(column=1, row=2, columnspan=2)
password_label.grid(column=0, row=3)
password_input.grid(column=1, row=3, columnspan=1)
generate_pw_button.grid(column=2, row=3)
add_button.grid(column=1,row=4, columnspan=2)

#Starting settings
website_input.focus()
email_input.insert(0,"myemail@gmail.com")

window.mainloop()
