# data_path = 'day 25: working with csv data/weather_data.csv'

# import csv

# with open(data_path) as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for _,temps in enumerate(data):
#         if temps[1] != 'temp':
#             temperatures.append(int(temps[1]))
#     print(temperatures)
#     for item in data:
#         print(item)
# import pandas as pd

# data = pd.read_csv(data_path)
# # temp_list = data['temp'].to_list()
# # average_temp = data['temp'].mean()
# # print(average_temp)

# # average_temp2 = sum(temp_list)/len(temp_list)
# # print(average_temp2)


# # max_value = data['temp'].max()
# # print(max_value)

# # print(data[data.temp == data.temp.max()])

# data.loc[data.day == 'Monday', 'temp'] = data[data.day == 'Monday'].temp * 9/5 + 32

# print(data[data.day == 'Monday'])


data_path = 'day 25: working with csv data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv'


import pandas as pd

data = pd.read_csv(data_path)

gray_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_count = len(data[data['Primary Fur Color'] == 'Red'])
black_count = len(data[data['Primary Fur Color'] == 'Black'])
data_dict = {
    'Fur color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [2473, 392, 103]
}

df = pd.DataFrame(data_dict)
df.to_csv('./day 25: working with csv data/squirrel_count2.csv')
