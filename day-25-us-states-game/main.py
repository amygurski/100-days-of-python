import turtle
from numpy import newaxis
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

IMAGE = "blank_states_img.gif"
DATA = pandas.read_csv("50_states.csv")
STATES = DATA["state"]
NUM_OF_STATES = STATES.count()

# Set background to U.S. map
screen.addshape(IMAGE)
screen.bgpic(IMAGE)

# # Get x & y values for 50_states.csv
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

def add_state_to_map(found_state):
    state_details = DATA[DATA.state == found_state]
    x = int(state_details.x)
    y = int(state_details.y)
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    t.goto(x,y)
    t.write(found_state)

answer_state = screen.textinput(title="Name the States", prompt="What's a state name?")

num_correct = 0
guessed_states = []
while answer_state != None:
    if answer_state.title() in STATES.values:
        num_correct += 1 
        guessed_states.append(answer_state.title())
        add_state_to_map(answer_state.title())

    answer_state = screen.textinput(title=f"{num_correct}/{NUM_OF_STATES} States Correct", prompt="What's another state name?")

    if num_correct == NUM_OF_STATES or answer_state.lower() == "exit":
        break

missing_states = []
for state in STATES.values:
    if state not in guessed_states:
        missing_states.append(state)
    new_csv = pandas.DataFrame(missing_states)
    new_csv.to_csv("states_to_learn.csv")
