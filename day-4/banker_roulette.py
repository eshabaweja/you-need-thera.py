import random

# Split string method

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")

# 🚨 Don't change the code above 👆
#Write your code below this line 👇

chosen = names[random.randint(0, len(names)-1)]

print(f"{chosen} will pay the bill.")