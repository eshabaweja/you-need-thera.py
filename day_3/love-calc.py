print("Welcome to the Love Calculator!")

your_name = input("Enter your name: ")
their_name = input("Enter their name: ")

combo_name = (your_name+their_name).lower()

units, tens = 0,0

for i in 'true':
    tens += combo_name.count(i)

for i in 'love':
    units += combo_name.count(i)

score = (tens*10+units)
print(f"Your love score is {score}")

if score<10 or score>90:
    print("You go together like pineapple on pizza.")

elif score>=40 and score<=50:
    print("You're alright.")

else:
    print("Drop 'em like hot potatoes.")