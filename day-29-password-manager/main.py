import json
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
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

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
search_button = Button(text="Search", width=13, command=find_password)

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
search_button.grid(row=1, column=2)

#Starting settings
website_input.focus()
email_input.insert(0,"myemail@gmail.com")

window.mainloop()
