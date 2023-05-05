from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
PATH = 'day 24: Files, directories and paths/snake-game update/data.txt'

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def get_high_score(self):
        with open(PATH) as f:
            high_score = f.read()
            return int(high_score)

    def set_high_score(self):
        with open(PATH, mode='w') as f:
            f.write(str(self.score))

    def update_scoreboard(self):
        self.clear()
        message = f"Score: {self.score} High Score: {self.high_score}"
        self.write(message, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.set_high_score()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
