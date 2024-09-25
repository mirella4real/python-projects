from turtle import Turtle

class Snake:

    def __init__(self):
        self.snake_segments = []

    def init_snake(self):
        for t in range(0, 3):
            turtle = Turtle("square")
            turtle.penup()
            self.snake_segments.append(turtle)
            self.snake_segments[t].color("white")
            self.snake_segments[t].setx(t * -20)
    
    def can_snake_move(self,x, y):
        print("bark!")
        return True
    
    def move(self, x, y, turn):
        start_index = len(self.snake_segments) -1
        for seg_num in range(start_index, 0, -1):
            print(seg_num)
            move_to = self.snake_segments[seg_num -1].pos()
            self.snake_segments[seg_num].setx(move_to[0])
            self.snake_segments[seg_num].sety(move_to[1])
        self.snake_segments[0].setx(x)
        self.snake_segments[0].sety(y)

    def get_head_coords(self):
        return self.snake_segments[0].pos()
# 