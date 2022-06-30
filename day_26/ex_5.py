# To convert temp_c into temp_f:
# (temp_c * 9/5) + 32 = temp_f

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

# weather_f = {day : (weather_c[day] * 9/5) + 32 for day in weather_c}
weather_f = {day : (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}


print(weather_f)
