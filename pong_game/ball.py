from turtle import Turtle

MOVE_DISTANCE = 10

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.ball = Turtle("circle")
        self.ball.penup()
        self.ball.shapesize(1,1)
        self.ball.color("white")
        self.ball.setpos(0,0)

    def move_ball(self):
        new_x = self.ball.xcor() + MOVE_DISTANCE
        new_y = self.ball.ycor() + MOVE_DISTANCE
        self.ball.setpos(new_x, new_y)