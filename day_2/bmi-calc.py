height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

bmi = float(weight)/float(height)**2

print("Your BMI is ",round(bmi,2))

# f-string
# these are like template strings in React/js
print(f"So your bmi is {round(bmi)}kg/m^2 given weight {weight}kg and height {height}m.")