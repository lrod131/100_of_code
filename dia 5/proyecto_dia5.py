#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 
           'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#con choices:

easy_pass = ''.join((random.choices(letters, k=nr_letters))+(random.choices(numbers, k=nr_numbers))+(random.choices(symbols, k=nr_symbols)))
print(f'la contraseña facil es {easy_pass}')

hard_pass = list(easy_pass)
random.shuffle(hard_pass)
hard_pass = ''.join(hard_pass)
print(f'la contraseña dificil es {hard_pass}')



#con for:
chars = ''
for each_char in range(0, nr_letters):
    chars += str(random.choice(letters))

number = ''
for each_number in range(0,nr_numbers):
    number += str(random.choice(numbers))

symbol = ''
for each_symbol in range(0,nr_symbols):
    symbol += str(random.choice(symbols))

easy_pass2 = chars+number+symbol
print (f'la contraseña con for es {easy_pass2}')