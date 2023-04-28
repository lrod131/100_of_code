'''
    program requirements:
    Provide layers of abstraction for a car rental system.
    
    the program should perform the following:
    1.- Hatchback, Sedan, SUV, should be type of cars that are provided for rent
    2.- cost per day: hatchback 30$, Sedan 50$, SUV 100$.
    3.- Give a propt to the customer asking the type of car and the number of days 
    he would like to borrow and provide the fare details to the user.
'''

# Classes

# rent class

class AvailableCars:
    def __init__(self) -> None:
        self.cars_available = {'hatchback': 30, 'sedan': 50, 'suv': 100}


    def __str__(self) -> str:
        return str(self.cars_available)


    def rent_car(self, car_type, car_days):
        pay = 0
        if car_type in self.cars_available:
            pay = self.cars_available[car_type] * car_days
        print(f'You have rented a {car_type} for {car_days}, you are now charged with ${pay} on your credit card')
        self.cars_available.pop(car_type)
    
    def displayAvailableCars(self):
        print('Avaliable cars are: ')
        for each_car in self.cars_available:
            print("- ", each_car.upper())

# customer class
class Customer:
    def __init__(self) -> None:
        self.car_type = (input('which car type would you like to rent? (Hatchback, Sedan or SUV): ')).lower()
        self.car_days = int(input('How many days would you like to borrow the car?: '))


    def __str__(self) -> str:
        return f'{self.car_type}, {self.car_days}'

# Main

deal = AvailableCars()
luis = Customer()
deal.displayAvailableCars()
deal.rent_car(luis.car_type, luis.car_days)
deal.displayAvailableCars()
