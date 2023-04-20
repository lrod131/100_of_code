alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(input_text, shift_position, operation):
    processed_text = []
    encode = True
    for _ in range(len(input_text)):
        if operation == 'encode':
            position = alphabet.index(input_text[_]) + shift_position
        elif operation == 'decode':
            position = alphabet.index(input_text[_]) - shift_position
        else:
            print('You have input a wrong value.')
            break
        wrapped_position = position % len(alphabet)
        processed_text.append(alphabet[wrapped_position])
    processed_text = ''.join(processed_text)
    print(f'The plain text is {processed_text}' if encode else f'The enconded text is {processed_text}')                    
    
#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

caesar(text,shift,direction)