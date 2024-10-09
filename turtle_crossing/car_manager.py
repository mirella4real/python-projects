from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class CarManager():
    def __init__(self):
        self.cars = []

    def create_car(self, x_coor, y_coor):
        car = Car()
        car.goto(x_coor, y_coor)
        self.cars.append(car)
        print(self.cars)

class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(1, 2)
        self.penup()
        self.setheading(180)
        self.color(random.choice(COLORS))

        
        
    
 


    