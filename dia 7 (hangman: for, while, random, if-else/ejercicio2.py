import random

word_list = ['aardvark','baboon','camel']
chosen_word = random.choice(word_list)

#test code
print(f'Psst, the solution is {chosen_word}')

#todo-1: create an empty list called display
#for each letter in the chosen_word, add a "_" to display
#so if the chosen_word was apple, display should be ["_","_","_","_","_"], with 5 "_" representing each letter to guess

display = []
for each_letter in chosen_word:
    display.append('_')

guess = input('Guess one letter for the chosen word: ').lower()

#Todo-2: loop through each position in the chosen_word;
#if the letter at that position matches "guess" then reveal the letter in the display at that position
#e.g. If the user guessed "p" and the chosend word was apple, then display should be "_","p","p","_","_"].

for char in range(len(chosen_word)):
    if chosen_word[char] == guess:
        display[char] = guess
    else:
        display[char] = '_'
#todo-3: print display and you should see the guess letter in the correct position and every other letter replace with "_".
#hint: don't worry about getting the user guess the next letter, we'll tackle that in step 3

print(display)