

#reglas
#la meta es sumar cartas hasta tener 21 o el numero mas cercano a 21 para ganar
#si tienes mas de 21 se llama bust y pierdes inmediatamente.
#las cartas del 2 al 10  tienen el mismo valor, la JQK valen 10, la carta A puede valer 1 u 11, puedes decidir que valor toma.
#se reparten 2 cartas (para para el usuario y otra para la pc) y se muestran. se reparten otras 2 cartas y la carta de la pc no se muestra, pero si la propia. 
#se tiene que ir pidiendo mas cartas al dealer hasta que se pida parar.
#luego de eso la computadora revela su mano,
#si hay empate, no se hace nada. Si la pc tiene un valor mas cercano o igual a  21 gana, sino el usuario gana. Si la pc tiene menos de 17, entonces, tomará otra carta. 

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.


#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


import os
import random

from art import logo


def clear_screen():
    os.system('clear')

def start_game():
    print(logo)
    first_hand = True
    while user_continues:
        user_draw =  draw_cards(cards,first_hand)
        computer_draw = draw_cards(cards,first_hand)
        print(f"Computer's cards are: {computer_draw[0]}")
        print(f'Your cards are {user_draw}, current score: {sum_cards(user_draw)}')
        hit_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        while hit_card == 'y':
            first_hand = False
            user_draw.append(draw_cards(cards,first_hand))
            hit_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        print(user_draw)
        break

def sum_cards(card_list):
    hand_total = 0
    for _ in range(len(card_list)):
        hand_total += card_list[_]
    return hand_total


def draw_cards(deck,first_round):
    hand = []
    if first_round:
        hand += random.choices(deck, k=2)
    else:
        hand += random.choices(deck)
    return hand

#    Your cards: [11, 4], current score: 15
#    Computer's first card: 10
# Type 'y' to get another card, type 'n' to pass: 

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_continues = True
play = input('Do you want to play a game of Blackjack? Type "Y" or "N"\n').lower()
if play == 'y':
    clear_screen()
    start_game()
else:
    print('Too bad! come back any time!! ')
