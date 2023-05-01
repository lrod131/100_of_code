'''
    program will ask who will win the race
    7 turtles will be created and start racing from left to right
    once one of the turtles reaches the end of the window program finsihes
    announcing with turtle won.
    If it was the once the user selected a message will be display for him,
    if not it will say the user lost
'''

from random import randint
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet',
                            prompt='Which turtle will win the race? Enter '
                            'the color: ')
turtle_colors = ["red", 'orange', 'yellow', 'green', 'blue', 'purple']

def start_line_turtles(turtle_color):
    turtles = {}
    y_position = -125
    for index, _ in enumerate(turtle_color):
        turtle_name = f'turtle_{turtle_colors[index]}'
        turtles[turtle_name] = Turtle(shape='turtle')
        turtles[turtle_name].color(turtle_colors[index])
        turtles[turtle_name].penup()
        turtles[turtle_name].goto(-200, y_position)
        y_position += 50
    return turtles


turtles_dic = start_line_turtles(turtle_colors)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle_name, turtle_object in turtles_dic.items():
        if turtle_object.xcor() > 230:
            is_race_on = False
            turtle_result = Turtle()
            turtle_result.penup()
            turtle_result.hideturtle()
            winning_color = turtle_object.pencolor()
            if user_bet == winning_color:
                turtle_result.write("You've won!", align="center", font=("Arial", 20, "bold"))
            else:
                turtle_result.write(f"You've lost, {winning_color} turtle is the winner", align="center", font=("Arial", 20, "bold"))
        random_distance = randint(0, 10)                    
        turtle_object.fd(random_distance)


screen.exitonclick()
