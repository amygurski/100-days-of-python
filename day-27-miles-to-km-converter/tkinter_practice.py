from tkinter import *  # remove all tkinter refs, good if using a lot

def button_clicked():
    # my_label["text"] = "I was clicked" # or my_label.config(text="I was clicked")
    my_label["text"] = input.get()

def spinbox_used():
    print(spinbox.get())

def scale_used(value):
    print(value)

def checkbutton_toggled():
    print(checked_state.get()) #prints 1 if On, otherwise 0

def radio_used():
    print(radio_state.get())

def listbox_used(event):
    print(listbox.get(listbox.curselection()))

window = Tk()
window.title("My first GUID program")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)

# Define Widgets
my_label = Label(text="I am a label", font=("Ariel", 24, "bold"))
input = Entry(width=10)
button = Button(text="Click me", command = button_clicked)
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# scale = Scale(from_=0, to=100, command=scale_used)

# textbox = Text(height=5, width=30)
# textbox.focus() # puts cursor in textbox
# textbox.insert(END, "Example of multiline entry") #starter text

# checked_state = IntVar() #this is actually a class!
# checkbutton=Checkbutton(text="Is on?", variable=checked_state, command=checkbutton_toggled)

# radio_state = IntVar() #this is actually a class!
# radiobutton1=Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2=Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)

# listbox = Listbox(height=4)
# fruits = ["apple", "pear", "orange", "banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)

# Pack widgets ("This geometry manager organizes widgets in blocks before placing them in the parent widget.")
# my_label.pack()
# input.pack()
# button.pack()
# textbox.pack()
# spinbox.pack()
# checkbutton.pack()
# radiobutton1.pack()
# radiobutton2.pack()
# listbox.pack()

#alternatives layout managers to pack
# my_label.place(x=100, y=200) #absolute positioning
my_label.grid(column=0, row=0) #relative to other items
button.grid(column=1, row=1)
input.grid(column=2, row=2)

window.mainloop() # keeps it open