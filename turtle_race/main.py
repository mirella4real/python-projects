from turtle import Turtle, Screen
import random
import strings
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = {}
screen = Screen()
screen.setup(width=500, height=400)

def announce_winner(bet, winner):
    if bet == winner:
        print(f"{strings.won_message} {(winner).title()} {strings.winner}")
    else:
        print(f"{strings.lost_message} {(winner).title()} {strings.winner}")

def init_turtles():
    for n in range(len(colors)):
        xpos = -230
        ypos = 175 - ((n + 1) * 50)
        turtle_color = colors[n]         
        turtles[turtle_color] = Turtle(shape="turtle")
        turtles[turtle_color].penup()
        turtles[turtle_color].color(turtle_color)
        turtles[turtle_color].goto(x=xpos, y=ypos)
    
def init_race():
    user_bet = screen.textinput(title=strings.popup_title, prompt=strings.popup_prompt).lower()
    init_turtles()
    winner = ""
    is_race_on = True
    while is_race_on == True:
        rand_dist = random.randint (0, 10)
        rand_color = random.choice(colors)
        moved_turtle = turtles[rand_color]
        xpos = moved_turtle.xcor() + rand_dist
        ypos = moved_turtle.ycor()
        moved_turtle.goto(x=xpos, y=ypos)
        if xpos > 200:
            winner = rand_color
            is_race_on = False
    announce_winner(user_bet, winner)

init_race()

screen.exitonclick()
