'''
    draw a random walk for your turtle, each time it changes direction it must
    change color. it should be thicker than before
'''
from turtle import Screen

from timmy_custom import NewTurtle

timmy = NewTurtle()
for _ in range(300):
    timmy.random_walk()
    timmy.set_line_color()

screen = Screen()
screen.exitonclick()
