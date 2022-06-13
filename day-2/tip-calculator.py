#just like we use commas in real life, we can use underscores in python to split numbers in order to visualize them better
import math
print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? "))
people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip? 10,12, or 15? "))

tip_amt = tip * total_bill / 100
total_due = (total_bill + tip_amt)

split_amount = math.ceil(total_due / people)
print(f"\nEach person should pay: {split_amount}\n")