from turtle import Turtle, Screen
import colorgram
import random

my_turtle = Turtle()
my_screen = Screen()
my_screen.colormode(255)

my_colors = [(202, 171, 108), (218, 225, 233), (153, 180, 196), (193, 161, 177), (152, 186, 174), (214, 204, 112), (231, 242, 239), (209, 178, 195), (175, 189, 213), (159, 213, 186), (159, 204, 217), (113, 123, 184), (185, 162, 63), (213, 182, 180), (98, 98, 97), (41, 41, 40), (201, 206, 42), (100, 96, 97)]

def extract_colors():
    hirst_colors = colorgram.extract('image.jpeg', 20)
    for c in hirst_colors:
        my_colors.append((c.rgb[0], c.rgb[1], c.rgb[2]))

def make_hirst_painting(rows, cols, dot, gap):
    x_cord = -225
    y_cord = -225
    my_turtle.penup()
    my_turtle.setpos(x_cord, y_cord)
    for r in range(rows):
        for c in range(cols):
            my_turtle.color(random.choice(my_colors))
            my_turtle.dot(dot)
            my_turtle.penup()
            my_turtle.fd(gap)
        my_turtle.penup()
        row_pos = ((r + 1) * gap) + y_cord
        my_turtle.setpos(x_cord, row_pos)


    


make_hirst_painting(10, 10, 20, 50)
my_screen.exitonclick()
