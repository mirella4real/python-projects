from turtle import Screen
from snake import Snake
import time
snake = Snake()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

MOVE_DISTANCE = 20

def move_up():
    head_coords = snake.get_head_coords()
    snake.can_snake_move(x=0, y=0)
    snake.move(head_coords[0] + MOVE_DISTANCE, 0, "n")
    

def move_down():
    snake.can_snake_move(x=0, y=0)
    #my_turtle.back(10)

def move_left():
    snake.can_snake_move(x=0, y=0)
    #my_turtle.right(90)

def move_right():
    snake.can_snake_move(x=0, y=0)
    #my_turtle.left(90)

# def clear():
#     my_turtle.clear()
#     my_turtle.reset()

def init_screen_listeners():
    screen.listen()
    screen.onkey(key="Up", fun=move_up)
    screen.onkey(key="Down", fun=move_down)
    screen.onkey(key="Left", fun=move_left)
    screen.onkey(key="Right", fun=move_right)


def init_snake():
    snake.init_snake()
    screen.update()
    return snake
    

def init_game():
    snake = init_snake()
    init_screen_listeners()
    in_play = True
    temp_counter = 0
    while in_play == True:
        screen.update()
        time.sleep(0.1)
        temp_counter += 1
        if temp_counter > 200:
            in_play = False

init_game()

screen.exitonclick()