from turtle import Screen, Turtle

tim = Turtle()



def move_forwards():
    tim.fd(10)

def move_backwards():
    tim.backward(10)

def move_clockwise():
    tim.right(10)

def move_counter_clockwise():
    tim.left(10)

def clear_screen():
    tim.reset()
    tim.goto(0, 0)


screen = Screen()
screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=move_counter_clockwise)
screen.onkey(key='d', fun=move_clockwise)
screen.onkey(key='c', fun=clear_screen)
screen.exitonclick()