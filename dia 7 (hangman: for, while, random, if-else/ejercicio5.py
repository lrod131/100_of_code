import random

import hangman_art as ha
import hangman_words as hw

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(hw.word_list)
#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(ha.logo)
print(f'Psst, the solution is {chosen_word}')

display = []
for each_letter in chosen_word:
    display.append('_')

lives = 6
while '_' in display:
    guess = input('Guess one letter for the chosen word: ').lower()
    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    if guess in display:
        print(f"You've already guess letter {guess}, try again!")
        
    for char in range(len(chosen_word)):
        if chosen_word[char] == guess:
            display[char] = guess

    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -=1
        print(f'the letter {guess} is not in the word, try again!')

    print(display)
    if '_' not in display:
        print("You've won")
    elif lives == 0:
        print("You've lost")
        break

    print(ha.stages[lives])