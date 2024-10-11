from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
snake = Snake()
food = Food()
score = Scoreboard()
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
        screen.update()
        time.sleep(0.1)
        snake.move_snake()
        if snake.get_head().distance(food) < 15:
            score.increase_score()
            food.refresh()
            snake.extend()

        if snake.get_head().xcor() > 290 or snake.get_head().xcor() < -290 or snake.get_head().ycor() > 290 or snake.get_head().ycor() < -290:
            score.reset()
            snake.reset()

        for segment in snake.snake_segments[1:]:
            if snake.get_head().distance(segment) < 10:
                score.reset()
                snake.reset()

def init_game():
    snake.init_snake()
    food.init_food()
    score.init_scoreboard()
    screen.update()
    init_screen_listeners()
    play_game()
init_game()

screen.exitonclick()