from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.setheading(90)
        self.shape('turtle')
        self.penup()
        self.initial_position()

    def move_up(self):
        self.fd(MOVE_DISTANCE)

    def initial_position(self):
        self.goto(STARTING_POSITION)
