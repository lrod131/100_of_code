import turtle

import pandas as pd
from states import State

screen = turtle.Screen()
screen.title('U.S. States Game')
IMAGE = 'day 25: working with csv data/us-states-game-start/blank_states_img.gif'
DATA_PATH = 'day 25: working with csv data/us-states-game-start/50_states.csv'
screen.addshape(IMAGE)

turtle.shape(IMAGE)
state = State()


data_file = pd.read_csv(DATA_PATH)
STATE_LIST = data_file.state.tolist()

while True:
    answer_state = screen.textinput("Guess the state", "What's the state's name?")
    answer_state = answer_state.capitalize()
    if answer_state in STATE_LIST:
        state_coor = data_file[data_file.state == answer_state]
        x_position = state_coor['x'].tolist()
        y_position = state_coor['y'].tolist()
        state.move_to_state(answer_state, x_position[0], y_position[0])

screen.exitonclick()