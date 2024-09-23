from turtle import Turtle, Screen

my_turtle = Turtle()
my_screen = Screen()

def move_forward():
    my_turtle.fd(10)

def move_backward():
    my_turtle.back(10)

def turn_clockwise():
    my_turtle.right(10)

def turn_cclockwise():
    my_turtle.left(10)

def clear():
    my_turtle.clear()
    my_turtle.reset()

my_screen.listen()
my_screen.onkey(key="w", fun=move_forward)
my_screen.onkey(key="s", fun=move_backward)
my_screen.onkey(key="a", fun=turn_cclockwise)
my_screen.onkey(key="d", fun=turn_clockwise)
my_screen.onkey(key="", fun=clear)
my_screen.exitonclick()