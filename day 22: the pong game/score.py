from turtle import Turtle


class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.show_scoreboard()


    def show_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.r_score, align="left", font=("Arial", 80, "normal"))
        self.goto(100, 200)
        self.write(self.l_score, align="left", font=("Arial", 80, "normal"))        

    def point_to_l(self):
        self.l_score += 1
        self.show_scoreboard()

    def point_to_r(self):
        self.r_score += 1
        self.show_scoreboard()
