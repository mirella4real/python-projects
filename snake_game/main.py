from turtle import Screen
from snake import Snake
import time
snake = Snake()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# def clear():
#     my_turtle.clear()
#     my_turtle.reset()

def init_screen_listeners():
    screen.listen()
    screen.onkey(key="Up", fun=snake.move_up)
    screen.onkey(key="Down", fun=snake.move_down)
    screen.onkey(key="Left", fun=snake.move_left)
    screen.onkey(key="Right", fun=snake.move_right)


def init_game():
    snake.init_snake()
    screen.update()
    init_screen_listeners()
    in_play = True
    temp_counter = 0
    while in_play == True:
        screen.update()
        time.sleep(0.1)
        temp_counter += 1
        if temp_counter > 100:
            in_play = False

init_game()

screen.exitonclick()