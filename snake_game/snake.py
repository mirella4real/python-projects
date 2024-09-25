from turtle import Turtle

class Snake:

    def __init__(self):
        self.snake_segments = []
        self.MOVE_DISTANCE = 20

    def init_snake(self):
        for t in range(0, 3):
            turtle = Turtle("square")
            turtle.penup()
            self.snake_segments.append(turtle)
            self.snake_segments[t].color("white")
            self.snake_segments[t].setx(t * -20)
    
    def can_snake_move(self,move_to):
        can_move = True
       # keep head from moving into itself
        snake_body = (self.snake_segments[1].pos())
        if move_to[0] == snake_body[0] and move_to[1] == snake_body[1]:
            can_move = False
        return can_move

    def move_up(self):
        head_coords = self.get_head_coords()
        new_coords = (head_coords[0], head_coords[1] + self.MOVE_DISTANCE)
        if self.can_snake_move(new_coords) == True:
            self.move(new_coords)
        

    def move_down(self):
        head_coords = self.get_head_coords()
        new_coords = (head_coords[0], head_coords[1] - self.MOVE_DISTANCE)
        if self.can_snake_move(new_coords) == True:
            self.move(new_coords)
        

    def move_left(self):
        head_coords = self.get_head_coords()
        new_coords = head_coords[0] - self.MOVE_DISTANCE, head_coords[1]
        if self.can_snake_move(new_coords) == True:
            self.move(new_coords)

    def move_right(self):
        head_coords = self.get_head_coords()
        new_coords = head_coords[0] + self.MOVE_DISTANCE, head_coords[1]
        if self.can_snake_move(new_coords) == True:
            self.move(new_coords)
        
    def move(self, coords):
        start_index = len(self.snake_segments) -1
        for seg_num in range(start_index, 0, -1):
            move_to = self.snake_segments[seg_num -1].pos()
            self.snake_segments[seg_num].setx(move_to[0])
            self.snake_segments[seg_num].sety(move_to[1])
        self.snake_segments[0].setx(coords[0])
        self.snake_segments[0].sety(coords[1])

    def get_head_coords(self):
        return self.snake_segments[0].pos()
# 