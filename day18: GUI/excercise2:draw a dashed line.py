'''
    Draw a dashed lines
'''

from turtle import Screen, Turtle

tim = Turtle()
tim.shape(name='turtle')
tim.speed(1)

print(tim.speed)
for _ in range(20):
    tim.fd(10)
    tim.penup()
    tim.fd(10)
    tim.pendown()

print(tim.speed)

screen = Screen()
screen.exitonclick()
