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
        self.y_move = MOVE_DISTANCE
        self.x_move = MOVE_DISTANCE

    def move_ball(self):
        old_x = self.ball.xcor()
        old_y = self.ball.ycor()
        new_x = old_x + self.x_move
        new_y = old_y + self.y_move
        self.ball.setpos(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def get_x(self):
        return self.ball.xcor()
    
    def get_y(self):
        return self.ball.ycor()
    
    def get_distance(self, target):
        return self.ball.distance(target)