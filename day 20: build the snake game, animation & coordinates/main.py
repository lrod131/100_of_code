import time
from turtle import Screen

from food import Food
from scoreboard import ScoreBoard
from snake import Snake

# Creating the objects and initialicing the screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('The snake game')
screen.tracer(0)
game = Snake()
food = Food()
score = ScoreBoard()
game_is_on = True

# Listening to keyEvents
screen.listen()
screen.onkey(key='Up', fun=game.move_up)
screen.onkey(key='Down', fun=game.move_down)
screen.onkey(key='Left', fun=game.move_left)
screen.onkey(key='Right', fun=game.move_right)

# Keep looping the snake's movement
while game_is_on:
    game.ver_elementos()
    screen.update()
    time.sleep(0.1)
    game.move_snake()

    # Detecting collision with food
    if game.head.distance(food) < 15:
        food.refresh()
        game.extend_snake()
        score.add_score()

    # Detecting collision with walls
    if game.head.xcor() > 280 or game.head.xcor() < -280 or \
       game.head.ycor() > 280 or game.head.ycor() < -280:
        game_is_on = False
        score.game_over()


# Exiting on click
screen.exitonclick()
