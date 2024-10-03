from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

TOP = 280
BOTTOM = -280
RIGHT = 320
LEFT = -320
RIGHT_BOUND = 400
LEFT_BOUND = -400
PADDLE_DISTANCE = 50

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(800, 600)
my_screen.title("Pong")
my_screen.tracer(0)

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)

my_screen.listen()
my_screen.onkey(key="Up", fun=right_paddle.move_up)
my_screen.onkey(key="Down", fun=right_paddle.move_down)
my_screen.onkey(key="w", fun=left_paddle.move_up)
my_screen.onkey(key="s", fun=left_paddle.move_down)

my_ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    my_screen.update()
    my_ball.move_ball()

    if my_ball.get_y() > TOP or my_ball.get_y() < BOTTOM:
        my_ball.bounce_y()

    if my_ball.get_distance(right_paddle) < PADDLE_DISTANCE and my_ball.get_x() > RIGHT or my_ball.get_distance(left_paddle) < PADDLE_DISTANCE and my_ball.get_x() < LEFT:
        my_ball.bounce_x()

    if my_ball.get_x() > RIGHT_BOUND:
        my_ball.reset_ball()

    if my_ball.get_x() < LEFT_BOUND:
        my_ball.reset_ball()
   
my_screen.exitonclick()


