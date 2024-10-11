from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 20, 'normal')
SCORE = 'Score: '
HIGH_SCORE = 'High Score: '
GAME_OVER = 'GAME OVER'
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0

    def init_scoreboard(self):
        self.penup()
        self.hideturtle()
        self.setpos(0, 240)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{SCORE} {self.score} {HIGH_SCORE} {self.high_score}", False, ALIGNMENT, FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.setpos(0, 0)
    #     self.write(f"{GAME_OVER}", False, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    