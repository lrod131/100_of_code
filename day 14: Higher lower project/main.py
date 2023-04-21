#importing initial libraries/resources
import os
import random

from art import logo, vs
from data import data

#Setting initial variables and conditionals
os.system('clear')
correct = True
user_continue = True
score = 0
print(logo)

#setting functions
def get_data(dict_info):
    get_user = random.choices(dict_info,k=2)
    user = f"{get_user[0]['name']}, {get_user[0]['description']}, from {get_user[0]['country']}."
    return user


def printing_options(user1,versus,user2):
    print(user1,versus,user2, sep='\n')
    answer = input('Who has more followers? Type "A" or "B": ')
    return answer

def get_followers(user,users_data):
    colon_index = user.find(':')
    comma_index = user.find(',')
    user_followers = 0
    for index, users in enumerate(data):
        if data[index]['name'] == user[colon_index+1:comma_index].strip():
            user_followers = data[index]['follower_count']
    return user_followers 

def set_winner(user1_followers, user2_followers, option):
    option_a = 'a'
    option_b = 'b'
    if option_a == option:
        if (user1_followers > user2_followers):
            return True
        return False
    elif option_b == option:
        if user2_followers > user1_followers:
            return True
        return False


while correct:
    #set each user value and in case is the same on both it gets another one
    if score <= 0:
        user_a = 'Compare A: ' + get_data(data)
        user_b = 'Against B: ' + get_data(data)
        while user_b[11:] == user_a[11:]:
            user_b = 'Against B: ' + get_data(data)
    else:
        user_a = user_b
        user_a = user_a.replace('Against B: ', 'Compare A: ')
        user_b = 'Against B: ' + get_data(data)
        while user_b[11:] == user_a[11:]:
            user_b = 'Against B: ' + get_data(data)
    #Print each user plus logo, returning the option the user entered
    option = printing_options(user_a, vs, user_b).lower()
    #evaluate if the user won or not, if not the game ends
    win = set_winner(get_followers(user_a, data), get_followers(user_b, data), option)
    if win:
        score += 1
        os.system('clear')
        print(logo)
        print(f'You are right! current score: {score}')        
    else: 
        print(f"Sorry, that's wrong. Final score: {score}")
        correct = False
