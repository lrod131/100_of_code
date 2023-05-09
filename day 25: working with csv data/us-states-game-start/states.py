from turtle import Turtle


class State():
    def move_to_state(self, state, x, y):
        new_state = Turtle()
        new_state.penup()
        new_state.hideturtle()
        new_state.goto(x, y)
        new_state.write(state, align='center',font=('arial',7,'normal'))