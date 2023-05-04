'''
    Turtle crossing game
'''
import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

# Screen objects
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Player objects
turtle = Player()

# Scrore objects
message = Scoreboard()

# Listeing events
screen.listen()
screen.onkey(turtle.move_up, key="Up")

# Car obstacles objects
obstacles = CarManager()
obstacles.hideturtle()
obstacles.penup()

# Game
counter = 0
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    obstacles.create_cars()

    # Detecting if the turtle crosses the road
    if turtle.ycor() > 280:
        obstacles.speed_up()
        message.level_up()
        turtle.initial_position()

    # Detecting if the turtle collides with a car
    for car in obstacles.car_list:
        if turtle.distance(car) < 20:
            game_is_on = False
            message.game_over()

screen.exitonclick()
