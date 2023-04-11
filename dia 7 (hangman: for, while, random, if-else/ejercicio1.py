import random

#step 1:

word_list = ['aardvark','baboon','camel']

#todo-1: Randomly choose a word from the wordlist and assign it to a variable called chosen_word

#todo-2 ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase

#todo-3: check if the letter the user guessed is one of the letters in the chosen_word

chosen_word = random.choice(word_list)
guess = input('Guess one letter for the chosen word: ').lower()

for char in chosen_word:
    if char == guess:
        print('right')
    else:
        print('wrong')
