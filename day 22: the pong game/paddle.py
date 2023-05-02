from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position) -> None:
        super().__init__()
        self.create_paddle(position)


    def create_paddle(self, position):
        self.penup()
        self.setheading(90)
        self.color('white')
        self.shape('square')
        self.goto(position)
        self.shapesize(1, 5)

    def up(self):
        self.fd(20)

    def down(self):
        self.backward(20)
