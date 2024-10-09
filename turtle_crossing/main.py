from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager
import time

my_screen = Screen()
my_screen.bgcolor("white")
my_screen.setup(width=600, height=600)
my_screen.title("Turtle Crossing")
my_screen.tracer(0)

my_player = Player()

my_screen.listen()
my_screen.onkey(key="Up", fun=my_player.move_player)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    my_screen.update()

my_screen.exitonclick()