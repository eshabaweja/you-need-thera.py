# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
print(type(two_digit_number))

units = two_digit_number[1]
tens = two_digit_number[0]

print(int(units) + int(tens))