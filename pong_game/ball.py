from turtle import Turtle
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.ball = Turtle("circle")
        self.ball.penup()
        self.ball.shapesize(1,1)
        self.ball.color("white")
        self.ball.setpos(0,0)

    def move_ball(self):
        position = self.ball.pos()
        self.ball.setpos(position[0] + 5, position[1] + 5)