import time
from random import choice, randint
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.car_list = []
        
    def set_attributes(self):
        self.penup()
        self.shape('square')
        self.shapesize(1, 2)
        self.color(choice(COLORS))
        self.initial_position()

    def create_cars(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            cars = CarManager()
            cars.set_attributes()
            self.car_list.append(cars)
        for car in self.car_list:
            car.move_left()

    def move_left(self):
        self.backward(STARTING_MOVE_DISTANCE)

    def initial_position(self):
        random_y = randint(-250, 220)
        self.goto(300, random_y)

    def speed_up(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
        self.backward(STARTING_MOVE_DISTANCE)
