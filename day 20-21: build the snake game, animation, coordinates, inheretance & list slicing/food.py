from random import randint
from turtle import Turtle


class Food(Turtle):
    def __init__(self, shape: str = "circle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed(9)
        self.refresh()

    def refresh(self):
        self.goto((randint(-280, 280)), (randint(-280, 280)))