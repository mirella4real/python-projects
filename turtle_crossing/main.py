from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager
import time
import random

CAR_STARTING_LINE = 280
CAR_END_LINE = -320
ROAD_TOP = 250
ROAD_BOTTOM = -250

my_screen = Screen()
my_screen.bgcolor("white")
my_screen.setup(width=600, height=600)
my_screen.title("Turtle Crossing")
my_screen.tracer(0)

my_player = Player()
my_car_manager = CarManager()



my_screen.listen()
my_screen.onkey(key="Up", fun=my_player.move_player)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    my_screen.update()
    my_car_manager.create_car(CAR_STARTING_LINE, random.randint(ROAD_BOTTOM, ROAD_TOP))
    my_car_manager.move_cars(CAR_END_LINE)

my_screen.exitonclick()