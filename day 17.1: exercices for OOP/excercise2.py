# Write an object oriente program to create a precious stone. No more that 5
# preciuos stones can be held in possesion at a given point of time. if
# there are more than 5 precious stones, delete the 1st one and store the
# new one


# CLASSES ##
'''
    Excercise 2 for OOP
'''


class Stone:
    def __init__(self, stone_list) -> None:
        self.stone_list = stone_list


    def __str__(self) -> str:
        return f'{self.stone_list}'


    def add_stone(self, stone_name):
        if len(self.stone_list) >= 5:
            self.stone_list.pop(0)
            self.stone_list.append(stone_name)
        else:
            self.stone_list.append(stone_name)


    def get_stones(self):
        print(self.stone_list)

# MAIN ##


new_stone = Stone(['Diamond'])
new_stone.add_stone('gold')
new_stone.add_stone('copper')
new_stone.add_stone('sapphire')
new_stone.add_stone('emerald')
new_stone.get_stones()
new_stone.add_stone('ruby')
new_stone.get_stones()
