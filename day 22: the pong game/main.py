'''
clases:
player
score
ball
screen
'''


import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from score import Score

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('The pong game')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
score = Score()


screen.listen()
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")


game_is_on = True

while game_is_on:

    screen.update()
    ball.roll()
    time.sleep(ball.interval)
    # Detect a collision with a wall
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.collide_y()

    # Collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or \
       ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.collide_x()

    # Detect a player misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.point_to_l()

    if ball.xcor() < -380:
        ball.reset_position()
        score.point_to_r()


screen.exitonclick()
