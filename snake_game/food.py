from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()

    def init_food(self):
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-250, 250)
        random_y = random.randint(-250, 250)
        self.goto(random_x, random_y)
