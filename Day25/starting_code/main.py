
# with open("Day25/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("Day25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     for row in data:
#         print(row)

# with open("Day25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))

#     print(temperature)

import pandas
import numpy as np


# data = pandas.read_csv("Day25/weather_data.csv")
# print(data)
# print(data["temp"])

# Avg temp
# print(sum(data["temp"])/len(data["temp"]))

# print(data["temp"].mean())

# max temp
# print(data["temp"].max())

# print(data.condition) # same as data["condition"]

# get a row out of df

# print(data[data.day=="Monday"])

# get row of max temp

# print(data[data.temp == data.temp.max()])

# monday = data[data.day=="Monday"]
# # print(monday)
# # print(monday.condition)

# print((int(monday.temp) * (9/5)) + 32)

data = pandas.read_csv("Day25/starting_code/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = list(data["Primary Fur Color"].unique())
new_fur_color = []

for color in fur_color:
    if str(color) != "nan":
        new_fur_color.append(color)

# print(new_fur_color)

# print(data["Unique Squirrel ID"].count())

count_num = []

for color in new_fur_color :
    color_df = data[data["Primary Fur Color"]==color]
    count_num.append(color_df["Unique Squirrel ID"].count())

data_dict = {"Fur Color" : new_fur_color , "Count": count_num }

pandas.DataFrame(data_dict).to_csv("Day25/starting_code/squirrel_count.csv")




