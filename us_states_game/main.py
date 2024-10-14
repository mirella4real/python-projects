import turtle

PROMPT_TITLE = "How Many States Can You Name?"
PROMPT_TEXT = "Enter a state name"
my_screen = turtle.Screen()
my_screen.title("US States Game")
image = "blank_states_img.gif"
my_screen.addshape(image)
turtle.shape(image)

answer_state = my_screen.textinput(title=PROMPT_TITLE, prompt=PROMPT_TEXT).lower()

my_screen.exitonclick()