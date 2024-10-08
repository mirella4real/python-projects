from turtle import Screen
import time

my_screen = Screen()
my_screen.bgcolor("white")
my_screen.setup(600, 600)
my_screen.title("Turtle Crossing")
my_screen.tracer(0)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    my_screen.update()

my_screen.exitonclick()