from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-210, 250)
        self.update_message(f'Level: {self.score}')

    def update_message(self, message):
        self.clear()
        self.write(message, align='center', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.update_message('Game Over')

    def level_up(self):
        self.level += 1
        self.update_message(f'Score: {self.level}')
