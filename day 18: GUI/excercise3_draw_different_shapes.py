'''
    Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
    all shapes are overlayed on each other and drawn in sequence
'''

from random import choice
from turtle import Screen, Turtle

tim = Turtle()
tim.shape(name='turtle')
tim.speed(3)





def draw_shape(initial_sides,angles):
    for _ in range(initial_sides):
        tim.forward(100)
        tim.right(angles)
    initial_sides += 1

def set_color():
    color_option = ["red", "green", "blue", "yellow", "orange", "purple",
                    "brown", "black", "gray", "cyan", "magenta",
                    "gold", "salmon", "seagreen", "violet", "navy", "olive",
                    "pink", "turquoise"]
    random_color = choice(color_option)
    tim.color(random_color)


sides = 3
for _ in range(8):
    angles = 360 / sides
    set_color()
    draw_shape(sides, angles)
    sides += 1

screen = Screen()
screen.exitonclick()
