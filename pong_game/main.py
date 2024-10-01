from turtle import Screen
from paddle import Paddle

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

game_is_on = True
while game_is_on:
    my_screen.update()

my_screen.exitonclick()

