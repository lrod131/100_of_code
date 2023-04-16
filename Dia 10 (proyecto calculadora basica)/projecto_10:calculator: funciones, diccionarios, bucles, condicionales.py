#adding logo
from art import logo

print (logo)
#Calculator:
#Add Operations
def add_number(number1,number2):
  return number1 + number2

#Substract operations:
def substract_number(number1,number2):
  return number1 - number2

#Multiply Operations:
def multiply_number(number1,number2):
  return number1 * number2

#Divide Operations
def divide_number(number1,number2):
  return number1 / number2

#Operation dictionary:
operation_dic = {
  '+':add_number,
  '-':substract_number,
  '*':multiply_number,
  '/':divide_number,
}

#setting a function
def calculator():
  #setting a while for continuity and initial variables:
  new_operation = True
  loop = False
  answer = 0.0
  
  while new_operation:
    
  #Enter the numbers
    if not loop:
      number1 = float(input("Enter one number: "))
    number2 = float(input("What's the next number? "))
    
    #show operation symbos
    for _ in operation_dic.keys():
      print (_)
    
    #selecting the type of operationse
    input_operation = input('Pick an operation from the line above: ')
    
    #calculating the operation based on user input
    calculation_operation = operation_dic[input_operation]
    answer = calculation_operation(number1,number2)
    
    #printing the final output  
    print(f'{number1} {input_operation} {number2} = {answer}')
  
    #checking if user wants to continue:
    go_again = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, exit to finish the program: ")
    if go_again == 'n':
      new_operation = False
      calculator()
    elif go_again == 'y':
      number1 = answer
      loop = True
    elif go_again =='exit':
      print('Good bye!')
      break

calculator()