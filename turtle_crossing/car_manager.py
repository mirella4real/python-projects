from turtle import Turtle
import random

SPEED = 5
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class CarManager():
    def __init__(self):
        self.cars = []

    def create_car(self, x_coor, y_coor):
        make_car = random.randint(1,6)
        if make_car == 1:
            car = Car()
            car.goto(x_coor, y_coor)
            self.cars.append(car)
        
    def move_cars(self, x_coor):
        for car in self.cars:
            car.forward(SPEED)
            if car.xcor() < x_coor:
                self.cars.remove(car)

    

class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(1, 2)
        self.penup()
        self.setheading(180)
        self.color(random.choice(COLORS))

    def get_ycor(self):
        return self.ycor()

        
        
    
 


    