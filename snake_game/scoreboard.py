from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 20, 'normal')
SCORE = 'Score: '
GAME_OVER = 'Game Over'
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

    def init_scoreboard(self):
        self.penup()
        self.hideturtle()
        self.setpos(0, 240)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{SCORE} {self.score}", False, ALIGNMENT, FONT)
    
    def game_over(self):
        self.setpos(0, 0)
        self.write(f"{GAME_OVER}", False, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    