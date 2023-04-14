from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(input_text, shift_position, operation):
    processed_text = []
    encode = True
    for _ in range(len(input_text)):
        
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    
        if not input_text[_].isalpha():
            processed_text.append(input_text[_])
        else:
            if operation == 'encode':
                position = alphabet.index(input_text[_]) + shift_position
            elif operation == 'decode':
                position = alphabet.index(input_text[_]) - shift_position
                encode = False
            else:
                print('You have input a wrong value.')
                break
            wrapped_position = position % len(alphabet)
            processed_text.append(alphabet[wrapped_position])
    processed_text = ''.join(processed_text)
    
    
    print(f'The plain text is {processed_text}' if encode else f'The encoded text is {processed_text}')                    


#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

#TODO-1: Import and print the logo from art.py when the program starts.
print(logo)


user_input = ''
while user_input != 'no':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    #Try running the program and entering a shift number of 45.
    #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
    #Hint: Think about how you can use the modulus (%).

    caesar(text,shift,direction)
    user_input = input('Type "yes" if you want to go again, Otherwise type "no": ').lower()
    print()
