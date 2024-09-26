from turtle import Screen
from snake import Snake
from food import Food
import time
snake = Snake()
food = Food()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


def init_screen_listeners():
    screen.listen()
    screen.onkey(key="Up", fun=snake.move_up)
    screen.onkey(key="Down", fun=snake.move_down)
    screen.onkey(key="Left", fun=snake.move_left)
    screen.onkey(key="Right", fun=snake.move_right)

def play_game():
    in_play = True
    temp_counter = 0
    while in_play == True:
        snake.move_snake()
        screen.update()
        time.sleep(0.1)
        temp_counter += 1
        if temp_counter > 200:
            in_play = False
    print("done")

def init_game():
    snake.init_snake()
    food.init_food()
    screen.update()
    init_screen_listeners()
    play_game()
init_game()

screen.exitonclick()