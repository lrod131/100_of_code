'''
    Draw a 100 x 100 square 
'''

from turtle import Screen, Turtle

tim = Turtle()
tim.shape(name='turtle')
tim.color('blue')
for i in range(0, 4):
    tim.forward(100)
    tim.left(90)


screen = Screen()
screen.exitonclick()
