#Number Guessing Game Objectives:

# Include an ASCII art logo. X
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


import os
import random

from art import logo

os.system('clear')
number = random.randint(0,100)
print(logo)
difficulty = input('Choose a difficulty. Type "easy" or "hard": ').lower()
if difficulty == 'easy':
    ATTEMPTS = 10
elif difficulty == 'hard':
    ATTEMPTS = 5
else:
    print('choose between easy and hard')

def start_game(turn):
    while turn > 0:
        user_number = int(input('Make a guess: '))
        if user_number > number:
            print('Too high.')
            turn -= 1
            print(f'You have {turn} left attempts to guess the number' if turn != 0 else f'You ran out of attemps, the number was {number}')
        elif user_number < number:
            print('Too low.')
            turn -= 1
            print(f'You have {turn} left attempts to guess the number' if turn != 0 else f'You ran out of attemps, the number was {number}')
        else:
            print(f"You got it, the answer was {number}")
            break



start_game(ATTEMPTS)