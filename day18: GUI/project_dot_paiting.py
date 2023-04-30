# import colorgram

# colors = colorgram.extract('day18: GUI/images.jpg', 10)

# rgb_color = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuple = (r, g, b)
#     rgb_color.append(color_tuple)

color_list = [(226, 230, 236), (59, 105, 148), (224, 201, 111), (231, 223, 203), (222, 234, 229), (220, 146, 74), (131, 84, 57), (195, 145, 171), (141, 176, 201), (141, 79, 104)]

'''
    paint a 10x10 rows of spots canvas
    each spot should be 20 in size and separated in 50 paces 
'''

import turtle as t
from random import randint

from timmy_custom import NewTurtle

tim = NewTurtle()
tim.speed(9)



def draw_spot_painting(size):
    y_position = -250
    X_POSITION = -200
    for _ in range(size):
        tim.penup()
        tim.goto(X_POSITION, y_position)
        for __ in range(size):
            tim.pendown()
            color_used = color_list[randint(0, len(color_list) - 1)]
            tim.dot(20, color_used)
            tim.penup()
            tim.fd(50)
        y_position += 50


draw_spot_painting(10)

screen = t.Screen()
screen.exitonclick()
