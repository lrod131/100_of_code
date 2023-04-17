

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


#estoy ahora construyendo que cuando el suaurio pida una carta se añada al arreglo

#importing libraries
import os
import random

from art import logo


#defining functions
def clear_screen():
    os.system('clear')

def start_game():
    print(logo)
    first_hand = True
    user_continues = True
    #1st while loop to maintain the program running until user decides to finish
    while user_continues:
        user_draw = draw_cards(cards, first_hand)    
        computer_draw = draw_cards(cards, first_hand)
        sum_draw = sum_cards(user_draw)
        print(f"Computer's cards are: {computer_draw[0]}")
        print(f'Your cards are {user_draw}, current score: {sum_draw}')
        hit_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        
        #2nd while loop to keep adding cards until user decides to stop drawing new ones
        while hit_card == 'y':
            first_hand = False
            user_draw.append(draw_cards(cards, first_hand))
            user_draw = check_ace(user_draw)
            sum_draw = sum_cards(user_draw)
            print(f'Your cards are {user_draw}, current score: {sum_draw}')
            if evaluate_draw(sum_draw):
                print('You lose')
                break
            else:
                hit_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        
        #3rd while loop, evaluating computer score and adding cards until it has 17 or more
        computer_sum_draw = sum_cards(computer_draw)
        computer_draw = add_computer_cards(computer_sum_draw, computer_draw)
        print(evaluate_winner(sum_draw,computer_sum_draw))
        print(f' you have {user_draw}, computer has {computer_draw}')
        play = input('Do you want to play a new game of Blackjack? Type "Y" or "N"\n').lower()
        if play == 'y':
            clear_screen()
            start_game()
        else:
            user_continues = False
            print('Too bad! come back any time!! ')

#evaluates who will be the winner according to the number most proximate to 21
def evaluate_winner(user_cards_sum,computer_cards_sum):
    user_proximity = 21 - user_cards_sum
    computer_proximity = 21 - computer_cards_sum
    print(user_proximity,computer_proximity)
    if computer_proximity < 0:
        return 'Computer loses'
    if user_proximity > computer_proximity:
        return 'Computer wins!'
    elif user_cards_sum == computer_cards_sum:
        return "It's a draw!"
    elif user_proximity == 0:
        return 'You win!'
    elif computer_proximity == 0:
        return 'Computer wins!' 
    else:
        return 'You win!'

#check if there's an 11 on a hand, if the sum is more than 21 then it's converted to 1 
def check_ace(card_list):
    for index, card in enumerate(card_list):
        if card == 11 and (sum(card_list) > 21):
            card_list[index] = 1
    return card_list

#evaluates if the sum of cards is more than 21
def evaluate_draw(sum_draw):
    if sum_draw > 21:
        return True
    return False

#adds a new card to the computer hand if it's under 17
def add_computer_cards(sum_draw, computer_hand):
    while sum_draw < 17:
        sum_draw = sum(computer_hand)
        computer_hand.append(draw_cards(cards,False))
        computer_hand = check_ace(computer_hand)
    return computer_hand

#sums the total of cards in a hand
def sum_cards(card_list):
    hand_total = sum(card_list)
    return hand_total

#draw a new card to a hand
def draw_cards(deck,first_round):
    hand = []
    if first_round:
        hand += random.choices(deck, k=2)
    else:
        hand += random.choices(deck)
        hand = int(hand[0])
    return hand


#declaring initial variables and conditions:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play = input('Do you want to play a game of Blackjack? Type "Y" or "N"\n').lower()
if play == 'y':
    clear_screen()
    start_game()
else:
    print('Too bad! come back any time!! ')
