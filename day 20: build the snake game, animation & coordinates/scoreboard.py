from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 270)
        self.color('white')
        self.score = 0
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f'Score: {self.score}', align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write('Game over', align="center", font=("Arial", 20, "normal"))

    def add_score(self):
        self.clear()
        self.score += 1
        self.update_score()
