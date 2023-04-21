'''
Coffee machine app:

This program will ask the user for one type of coffee,
depening on the user's input it will check if the resources
are available to process, if so, it will ask for the user's
money (coins only: pennies, dimes, quartes and nickels),
it will check if the sum of these coins are enough to pay
for the coffee if so it will serve it so, if not it will
prompt a message to the user letting him know how much
the coffee cost, how much the user inserted and the money
will be refounded.
'''

from resources import MENU, money, resources


def reporting():
    '''
    Prints the current level for each resource when entering 'report' in the
    main menu.
    '''
    if user_input == 'report':
        for key, values in resources.items():
            if key == 'water' or key == 'milk':
                print(f"{key.capitalize()}: {values}ml")
            elif key == 'coffee':
                print(f"{key.capitalize()}: {values}g")
            else:
                print(f'{key.capitalize()}: ${values}')


def check_resources(user_option, current_resources):
    '''
    Checks if the current resources are enough to make the selected beverage,
    if it's enough it will return a True statement, if not it will return the
    missing resource
    '''
    enough_water = current_resources['water'] >= MENU[user_option]['ingredients']['water']
    enough_coffee = current_resources['coffee'] >= MENU[user_option]['ingredients']['coffee']
    if user_option == 'latte' or user_option == 'cappuccino':
        enough_milk = current_resources['milk'] >= MENU[user_option]['ingredients']['milk']
        check_latte_cappuccino = enough_water and enough_coffee and enough_milk
        if check_latte_cappuccino:
            return True
        else:
            if not enough_coffee:
                return 'coffee'
            elif not enough_water:
                return 'water'
            else:
                return 'milk'
    if user_option == 'espresso':
        check_espressso = enough_water and enough_coffee
        if check_espressso:
            return True
        else:
            if not enough_coffee:
                return 'coffee'
            elif not enough_water:
                return 'water'


def process_coins(user_option):
    '''
    It will ask the user how many of each coin will be inserted, will sum all
    of them, subtract the coffee value and refound the correspondent change.
    Finally if there's not enough for the selected drink, it will prompt the
    user a message letting him know that it was not possible to continue
    and the money will be refounded.
    '''
    deposited_coins = []
    sum_coins = 0
    print('Please insert coins:')
    # 1st for: populates the deposited_coins variable with the coins the
    # user is putting
    for key in money:
        coin = int(input(f'How many {key} will you put in the machine?: '))
        deposited_coins.append(coin)
    # 2nd for: multiplies all the coins x its values and then sums it all in
    # the sum_coins value. This variable is later returned
    for index, key in enumerate(money):
        sum_coins += money[key] * deposited_coins[index]
    if sum_coins < MENU[user_option]['cost']:
        print(f"Sorry, that's not enough money, {user_option} costs ${MENU[user_option]['cost']}\
            and you have put ${round(sum_coins,2)}, your money have been refounded.")
        return False
    else:
        change = sum_coins - MENU[user_option]['cost']
        print(f'Here is ${round(change,2)} in change.')
        resources['money'] += MENU[user_option]['cost']
        return True


def update_resources(user_option):
    '''
    Once there's enough resources and money to make the coffee, the resources
    will be subtracted, according to the amount specified in the MENU variable.
    '''
    resources['water'] -= MENU[user_option]['ingredients']['water']
    resources['coffee'] -= MENU[user_option]['ingredients']['coffee']
    if 'milk' in MENU[user_option]['ingredients']:
        resources['milk'] -= MENU[user_option]['ingredients']['milk']


def make_coffee(user_option):
    '''
    Checks all requirements to make a coffee (money and resources), if all
    of them are True then it will give out the coffee, if not a message
    will be prompt to the user letting him know that there are not enough
    resources
    '''
    resources_available = check_resources(user_option, resources)
    if isinstance(resources_available, bool) and resources_available:
        if process_coins(user_option):
            update_resources(user_option)
            print(f'Here is your {user_option} \u2615, enjoy! ')
            return
    else:
        print(f"Sorry there's not enough {resources_available} to make a {user_option}")
        return


def check_user_input(user_option):
    '''
    This function works as a menu for all cases that user_input would be, in
    case it's not any of the listed then it will provide a message saying
    that it's not a valid option.
    '''
    match user_option:
        case 'espresso' | 'latte' | 'cappuccino':
            make_coffee(user_option)
        case 'report':
            reporting()
        case _:
            print(f'Option {user_option} is not valid, please try again. \n')


user_input = input('What would you like ? (espresso/latte/cappuccino): ').lower()
while user_input != 'off':
    check_user_input(user_input)
    user_input = input('What would you like ? (espresso/latte/cappuccino): ').lower()
