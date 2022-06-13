# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight/height**2

print(f"Your BMI is {round(bmi,2)} kg/m^2.")

if bmi < 0:
    print("Invalid input. Please enter a valid number.")

elif bmi<= 18.5:
    print("You are underweight.")
elif 18.5<bmi<=25:
    print("Hoorah! normal weight.")
elif 25<bmi<=30:
    print("You're slightly overweight.")
elif 30<bmi<= 35:
    print("You're obese.")
else:
    print("You're clinically obese.")