from turtle import Turtle


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.color('purple')
        self.shape('circle')
        self.x_move = 10
        self.y_move = 10
        self.interval = 0.1

    def roll(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def collide_y(self):
        self.y_move *= -1
        self.interval *= 0.9

    def collide_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.collide_x()
        self.goto(0 + self.x_move, 0 + self.y_move)
        self.interval = 0.1
