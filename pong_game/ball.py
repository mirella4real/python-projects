from turtle import Turtle

MOVE_DISTANCE = 10

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(1,1)
        self.color("white")
        self.y_move = MOVE_DISTANCE
        self.x_move = MOVE_DISTANCE
        self.setpos(0,0)
       

    def reset_ball(self):
        self.setpos(0,0)
        self.bounce_x()

    def move_ball(self):
        old_x = self.xcor()
        old_y = self.ycor()
        new_x = old_x + self.x_move
        new_y = old_y + self.y_move
        self.setpos(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def get_x(self):
        return self.xcor()
    
    def get_y(self):
        return self.ycor()
    
    def get_distance(self, target):
        return self.distance(target)