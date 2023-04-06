rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

option = ['rock' , 'paper' , 'scissors']
computer = random.choices(option)
computer = str(computer[0])

human = input('Choose rock, paper or scissors: \n').lower()

if computer == 'rock' and human == 'paper':
    print('you choose: ')
    print(paper)
    print("Computer choose:")
    print(rock)
    print('\nyou win')
elif computer == 'paper' and human == 'scissors':
    print('you choose: ')
    print(scissors)
    print("Computer choose:")
    print(paper)
    print('\nyou win')
elif computer == 'scissors' and human == 'rock':
    print('you choose: ')
    print(rock)
    print("Computer choose:")
    print(scissors)
    print('\nyou win')
elif computer == human:
    if computer == 'rock':
        print('you choose: ')
        print(rock)
        print("Computer choose:")
        print(rock)
        print("\nit's a draw")
    elif computer == 'paper':
        print('you choose: ')
        print(paper)
        print("Computer choose:")
        print(paper)
        print("\nit's a draw")
    else:
        print('you choose: ')
        print(scissors)
        print("Computer choose:")
        print(scissors)
        print("\nit's a draw")
else:
    if human == 'rock':
        print("You choose:")
        print(rock)
    elif human == 'paper':
        print("You choose:")
        print(paper)
    else:
        print("You choose:")
        print(scissors)
    if computer == 'rock':
        print("Computer choose:")
        print(rock)
    elif computer == 'paper':
        print("Computer choose:")
        print(paper)
    else:
        print("Computer choose:")
        print(scissors)
    print('\nyou lose')