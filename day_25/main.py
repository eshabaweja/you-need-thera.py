# import csv

# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for item in data:
#         # print(item)
#         if item[1] != "temp":
#             temperatures.append(int(item[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(type(data["temp"]))

# data_html = data.to_html
# print(data_html)
temp_list = data["temp"].to_list()
print(temp_list)
# temp_avg = sum(temp_list)/len(temp_list)
# print(f"Average temperature was: {round(temp_avg)}")
print(data["temp"].mean())
print(data["temp"].max())

# Get Data from Columns
print(data["condition"])
# or
print(data.condition)

# Get data from rows
# put condition in [] to filter row
row = data[data.condition == "Sunny"]
print(row)

# print row with max temp
print(data[data.temp == data.temp.max()])
print(data[data.temp == data.temp.max()].condition)
