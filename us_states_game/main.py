import turtle
import pandas

SCREEN_TITLE = "US States Game"
PROMPT_TITLE = "Can you name all 50 states?"
PROMPT_TEXT = "Enter a state name"
ALIGNMENT = "center"
FONT = ('Arial', 10, 'normal')
score = 0
correct_guesses = []

my_screen = turtle.Screen()
my_screen.title(SCREEN_TITLE)
image = "blank_states_img.gif"
my_screen.addshape(image)
turtle.shape(image)

revealed_state = turtle.Turtle()
revealed_state.penup()
revealed_state.hideturtle()
revealed_state.color("black")

def write_state(name, x, y):
    revealed_state.setpos(x, y)
    revealed_state.write(name, False, ALIGNMENT, FONT)

def get_score(state_name):
    correct_guesses.append(state_name)
    return len(correct_guesses)

def save_remaining_states():
    state_list = state_data["state"].to_list()
    remaining_states = [state for state in state_list if state not in correct_guesses]
    states_to_learn = {
        "state": remaining_states
    }
    states_dataframe = pandas.DataFrame(states_to_learn)
    states_dataframe.to_csv("states_to_learn.csv")
            


state_data = pandas.read_csv("./50_states.csv")

while score < 50:
    # prompt
    state_name = my_screen.textinput(title=f"{PROMPT_TITLE} {score}/50", prompt=PROMPT_TEXT).title()
    
    # exit game
    if state_name == "Exit":
        save_remaining_states()
        break

    # check for duplicate guess
    if not state_name in correct_guesses:
        #check csv data
        retrieved_state = state_data[state_data.state == state_name]
        if not retrieved_state.empty:
            my_series = pandas.Series(retrieved_state.values[0])
            state_n = my_series[0]
            state_x = int(my_series[1])
            state_y = int(my_series[2])
            write_state(state_n, state_x, state_y)
            score = get_score(state_n)
            