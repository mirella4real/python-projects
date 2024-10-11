from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180

class Snake:

    def __init__(self):
        self.snake_segments = []

    def init_snake(self):
        for t in range(0, 3):
            position = (t * -20, 0)
            self.add_segment(position)
    
    def reset(self):
        for segment in self.snake_segments:
            segment.goto(1000, 1000)
        self.snake_segments.clear()
        self.init_snake()

    def can_snake_move(self,move_to):
        can_move = True
       # keep head from moving into itself
        snake_body = (self.snake_segments[1].pos())
        if move_to[0] == snake_body[0] and move_to[1] == snake_body[1]:
            can_move = False
        return can_move

    def move_up(self):
        head = self.get_head()
        if head.heading() != DOWN:
            head.setheading(UP)
        
    def move_down(self):
        head = self.get_head()
        if head.heading() != UP:
            head.setheading(DOWN)
        
    def move_left(self):
        head = self.get_head()
        if head.heading() != RIGHT:
            head.setheading(LEFT)

    def move_right(self):
        head = self.get_head()
        if head.heading() != LEFT:
            head.setheading(RIGHT)

    def move_snake(self):
        start_index = len(self.snake_segments) -1
        for seg_num in range(start_index, 0, -1):
            move_to = self.snake_segments[seg_num -1].pos()
            self.snake_segments[seg_num].setx(move_to[0])
            self.snake_segments[seg_num].sety(move_to[1])
        self.snake_segments[0].forward(MOVE_DISTANCE)
    
    def get_head(self):
        return self.snake_segments[0]
    
    def extend(self):
        self.add_segment(self.snake_segments[-1].position())
    
    def add_segment(self, position):
        turtle = Turtle("square")
        turtle.penup()
        turtle.color("white")
        turtle.goto(position[0], position[1])
        self.snake_segments.append(turtle)
