'''
    draw a spirograph using circles of 100 in radious
'''

from turtle import Screen

from timmy_custom import NewTurtle

timmy = NewTurtle()
timmy.pensize(3)
timmy.speed('fastest')

draw_circle(10)

screen = Screen()
screen.exitonclick()
