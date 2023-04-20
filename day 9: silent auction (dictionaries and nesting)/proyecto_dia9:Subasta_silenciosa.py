import os

from art import logo


def Clear_console():
    os.system('clear')

Clear_console()
print(logo)

new_user = True
auction_dic = {}
while new_user:
    name = input("\nwhat is your name? ") 
    value = int(input("what's your bid? "))
    auction_dic[name] = value
    question = input('is there other user who wants to bid? Yes / No \n').lower()
    if question == 'no':
        new_user = False
    else:
        Clear_console()

def set_winner(dict):
    winner = ''
    max_value = max(dict.values())
    for key, value in dict.items():
        if value == max_value:
            winner = key
            break
    return f'The auction winner is {winner}'


print(set_winner(auction_dic))