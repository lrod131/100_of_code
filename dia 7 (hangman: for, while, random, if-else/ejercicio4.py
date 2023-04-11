import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ['aardvark','baboon','camel']
chosen_word = random.choice(word_list)


#test code
print(f'Psst, the solution is {chosen_word}')

#create  blanks
display = []
for each_letter in chosen_word:
    display.append('_')

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6
while '_' in display:
    guess = input('Guess one letter for the chosen word: ').lower()
    
#TODO-2: - If guess is not a letter in the chosen_word,
#Then reduce 'lives' by 1. 
#If lives goes down to 0 then the game should stop and it should print "You lose."

    #check guessed letter
    for char in range(len(chosen_word)):
        if chosen_word[char] == guess:
            display[char] = guess
           
    if guess not in chosen_word:
        lives -=1
        print(f'the letter {guess} is not in the word')

    print(display)
    if '_' not in display:
        print("You've won")
    elif lives == 0:
        print("You've lost")
        break
        
#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])
    