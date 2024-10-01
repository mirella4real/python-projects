from turtle import Turtle

MOVE_DISTANCE = 20

class Paddle(Turtle):

    def __init__(self, x_pos, y_pos):
       super().__init__()
       self.penup()
       self.goto(x_pos, y_pos)
       self.setheading(90)
       self.shapesize(1, 5)
       self.shape("square")
       self.color("white")

    def move_up(self):
        self.goto((self.xcor(), self.ycor() + MOVE_DISTANCE))
        
    def move_down(self):
        self.goto((self.xcor(), self.ycor() - MOVE_DISTANCE))
       
