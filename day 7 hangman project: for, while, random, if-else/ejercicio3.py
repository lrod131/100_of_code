import random

word_list = ['aardvark','baboon','camel']
chosen_word = random.choice(word_list)

#test code
print(f'Psst, the solution is {chosen_word}')

#create  blanks
display = []
for each_letter in chosen_word:
    display.append('_')

#todo-1: use a while loop to let the users guess again, the loop should only stop once the user has guessed all the letters in the chosen_word and display has no more
#blanks ("_")m then you can tell the user they've won

while '_' in display:
    guess = input('Guess one letter for the chosen word: ').lower()
    
    #check guessed letter
    for char in range(len(chosen_word)):
        if chosen_word[char] == guess:
            display[char] = guess
    print(display)
    if '_' not in display:
        print("You've won")