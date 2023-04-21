#requerimientos
#necesita imprimir cuantos recursos le quedan
#verificar si los recorsos son suficientes para hacer un nuevo café
#procesa monedas (uno de cada uno), sino  es puede pagar le devuelve el dinero al usuario, si peude entonces da el cambio (de haber cambio)
#verificar si la transaccion es satisfactoria
#hacer el cafe (restar los recursos necesarios de los disponibles

from resources import *

#TODO: asking user what would he like


#TODO: turn the coffee machine by entering "off" to the prompt
def turn_off():
    if user_input == 'off': 
        print('Machine is off')
    return

#[x]: print report >>> convertir en funcion
def reporting ():
    if user_input == 'report':
        for key, values in resources.items():
            if key == 'water' or key == 'milk':
                print(f"{key.capitalize()}: {values}ml")
            elif key == 'coffee':
                print(f"{key.capitalize()}: {values}g")
            else:
                print(f'{key.capitalize()}: ${values}')            

#TODO: check for suficient resources
#compares current resource values against a new type of serving. if it's enough it will return True else, it will be false
def check_resources(user_option,current_resources,ingredients):
    if user_option == 'espresso':
        if (current_resources['water'] >= ingredients[user_option]['ingredients']['water']) and (current_resources['coffee'] >= ingredients[user_option]['ingredients']['coffee']):
            return True
        return False
    elif user_option == 'latte':
        if (current_resources['water'] >= ingredients[user_option]['ingredients']['water']) and (current_resources['coffee'] >= ingredients[user_option]['ingredients']['coffee']) and (current_resources['milk'] >= ingredients[user_option]['ingredients']['milk']):
            return True
        return False
    else:
        if (current_resources['water'] >= ingredients[user_option]['ingredients']['water']) and (current_resources['coffee'] >= ingredients[user_option]['ingredients']['coffee']) and (current_resources['milk'] >= ingredients[user_option]['ingredients']['milk']):
            return True
        return False


#[x]: process coins 
def process_coins(money_constant):
    deposited_coins = []
    sum_coins = 0
    #1st for: populates the deposited_coins variable with the coins the user is putting
    for key in money_constant:
        coin = int(input(f'How many {key} will you put in the machine?: '))
        deposited_coins.append(coin)
    #2nd for: multiplies all the coins x its values and then sums it all in the sum_coins value. This variable is later returned    
    for index, key in enumerate(money_constant):
        sum_coins += money_constant[key] * deposited_coins[index]
    return sum_coins

  #TODO: check for successful transaction

#TODO: make coffee


def check_user_input(user_option):
    match user_option:
        case 'espresso' | 'latte' | 'capuccino':
            print('olis')
        case 'report':
            reporting()
        case 'off':
            turn_off()
        case _:
            print(f'Option {user_option} is not valid, please try again')

user_input = input('What would you like ? (espresso/latte/cappuccino): ').lower()
while user_input != 'off':
    check_user_input(user_input)
    user_input = input('What would you like ? (espresso/latte/cappuccino): ').lower()