from tkinter import *  # remove all tkinter refs, good if using a lot

def convert_distance():
    miles = float(miles_input.get())
    km_result_label["text"] = "{:.2f}".format(miles * 1.609)

# Setup window
window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=300,height=200)
window.config(padx=20,pady=20)

# Define Widgets
miles_input = Entry(width=10)
miles_input.focus()
miles_unit_label = Label(text="miles", font=("Ariel", 12))
equal_to_label = Label(text="is equal to", font=("Ariel", 12))
km_result_label = Label(text="", font=("Ariel", 12))
km_unit_label = Label(text="km", font=("Ariel", 12))

button = Button(text="Calculate", command = convert_distance)

# Establish layout
miles_input.grid(column=1, row=0) 
miles_unit_label.grid(column=2, row=0)
equal_to_label.grid(column=0, row=1)
km_result_label.grid(column=1, row=1)
km_unit_label.grid(column=2, row=1)
button.grid(column=1, row=2)

window.mainloop()
