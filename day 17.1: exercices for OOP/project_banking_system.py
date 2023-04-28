'''
    Simulate a banking system problem statement:
    1.- Give a prompt to the user asking if they wish to create a new savings
    account or access an existing one.
    2.- If the user would like to create a new account, accept their name,
    Initial deposit, create a 5 random digit number and make it as the account
    number of their saving account.
    3.- If they are accessing an existing account accept their name and account
    number to validate the user, give them options to withdraw, deposit or 
    display their available balance.
'''

# Classes
from random import randint


class User:
    '''
        Satisfies problem statement nº 2
    '''
    def __init__(self, name=None, money=None) -> None:
        self.name = name
        self.account_number = randint(11111, 99999)
        self.money = money

    def __str__(self) -> str:
        return f'{self.name}, {str(self.account_number)}, {str(self.money)}'

    def create_user(self):
        self.name = input('What is your name?: ')
        self.money = int(input('How much will be your initial deposit?: '))
        print(f'Okay! This is your account number {self.account_number}, you'
              f' have to provide your name ({self.name}) and account to access'
              f' your account!')
        input()


class Bank(User):
    '''
        Contains all the operation methods for this problem
    '''
    def __init__(self) -> None:
        super().__init__()

    def display_account_info(self):
        print(f'You currently have {self.money} in your account')
        input()

    def deposit_money(self):
        amount = int(input('How much would you like to deposit? '))
        self.money += amount
        #return self.money

    def withdraw_money(self):
        amount = int(input('How much would you like to withdraw? '))
        self.money -= amount
        #return self.money

    def validate_user(self):
        name = input('Please enter your name: ')
        account = int(input('Please enter your account number: '))
        return (name == self.name) and (account == self.account_number)


# MAIN
RUNNING = True

while RUNNING:
    user_option = input('#### IMPORTANT BANK####\n\nPlease select an option:\n'
                        '1) To create a savings account\n2) To Access an '
                        'existing account\n3) To exit\n\nYou have selected: ')
    match int(user_option):
        case 1:
            new_account = Bank()
            new_account.create_user()
        case 2:
            if new_account.validate_user():
                while True:
                    print('What would you like to do? ')
                    client_option = input('1) Make a deposit \n2) Withdraw  '
                                          'money\n3) Show balance\n4) Go back '
                                          'to main Menu\n\nYou have selected:')
                    match int(client_option):
                        case 1:
                            new_account.deposit_money()
                        case 2:
                            new_account.withdraw_money()
                        case 3:
                            new_account.display_account_info()
                        case 4:
                            break
                        case _:
                            input('You have entered an invalid option, Press '
                                  'enter to continue')
            else:
                input('You have entered an invalid name/number, Press enter '
                      'to continue')
        case 3:
            print('Thanks for using the app')
            RUNNING = False
        case _:
            print('You have entered an invalid option, try again')
