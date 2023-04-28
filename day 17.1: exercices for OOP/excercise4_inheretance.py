'''
    Create a program that performs the following tasks:
    1.- Create a class called chair from the base class furniture
    2.- Teakwood should be the type of furniture that is used by all furnitures
        by default
    3.- The user can given an option to change the type of wood used for a 
        chair if he wishes to
    4.- The number of legs of a chair should be a property that should not be
        altered outside the class
'''

class Furniture:
    def __init__(self) -> None:
        self.wood_type = 'Teakwood'

class Chair(Furniture):
    def __init__(self) -> None:
        super().__init__()
        self.__chair_legs = 4


    def change_wood_type(self):
        self.wood_type = input('Which type of wood would you like to change'
                               'the chair to?: ')


    def display_user_chair(self):
        print(f'The chair has {self.__chair_legs} and it is made of',
              self.wood_type)


new_chair = Chair()
new_chair.display_user_chair()
new_chair.change_wood_type()
new_chair.display_user_chair()
