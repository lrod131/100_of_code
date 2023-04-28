'''
    Create a class named square and perform the following tasks:
    1.- Create two objects for this 3rd class squareOne and squareTwo
    2.- Find the result of side of squareOne to the power of side of squareTwo

    Example: if squareOne has length of 2cm each side and squareTwo has a
    length of 4cm each side, squareOne ** squareTwo should return 16, which is
    2 to the power of 4.

    Hint: while performing SquareOne ** SquareTwo, you need to overload
    __pow__() method
'''

class Square:
    def __init__(self, number) -> None:
        self.number = number


    def __pow__(self, other):
        return self.number ** other.number


squareOne = Square(3)
squareTwo = Square(2)

print(f'the result of {squareOne.number} to the power of {squareTwo.number} '
      'is', squareOne**squareTwo)
