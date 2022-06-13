# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# by size
if size == 's' or size == 'S':
    total = 15
elif size == 'm' or size == 'M':
    total = 20
elif size == 'l' or size == 'L':
    total = 25
else:
    print("Please enter a valid size.")

# extra pepperoni
if add_pepperoni == 'y' or add_pepperoni == 'Y':
    if size == 's' or size == 'S':
        total+=2
    else:
        total+=3

# extra cheese
if extra_cheese == 'y' or extra_cheese == 'Y':
    total+=1

print(f"\nThe amount payable is ${total}. Happy Pizza!")