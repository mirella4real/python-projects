from turtle import Turtle, Screen
import random
my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("green")
my_colors = ["blue", "red","green","dark cyan","medium spring green","gold","olive","light steel blue","dark salmon","dark violet"]
my_direction = [0, 90, 180, 270]


def draw_shape(length, sides, angle):
    for x in range(sides):
        my_turtle.forward(length)
        my_turtle.right(angle)

def draw_dashed_line():
    draw = True
    for _ in range(15):
        if draw == True:
            my_turtle.pendown()
            draw = False
        else:
            my_turtle.penup()
            draw = True
        my_turtle.forward(10)

def draw_multi_shapes():
    for x in range(3,10):
        angle = 360/x
        my_turtle.color(my_colors[x])
        draw_shape(100, x, angle)

def get_color():
    return random.choice(my_colors)


def random_walk():
    length = 20
    my_turtle.width(10)
    my_turtle.speed("fast")
    for _ in range(200):
        my_turtle.color(get_color())
        my_turtle.forward(length)
        my_turtle.setheading(random.choice(my_direction))
        

random_walk()

my_screen = Screen()
my_screen.exitonclick()



