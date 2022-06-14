import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''

   _       ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\.

'''

#Write your code below this line 👇

print("What's your choice? Type 0 for rock, 1 for paper, 2 for scissors.\n")

choice = int(input())
computer = random.randint(0,2)

# for user
if choice == 0:
    print(f"You chose rock\n{rock}")

elif choice == 1:
    print(f"You chose paper\n{paper}")

elif choice == 2:
    print(f"You chose scissors\n{scissors}")

else: 
    print("Invalid input.")

# for computer
if computer == 0:
    print(f"Computer chose rock\n{rock}")

elif computer == 1:
    print(f"Computer chose paper\n{paper}")

else:
    print(f"Computer chose scissors\n{scissors}")


## playing the game 

if choice == computer:
    print("It's a draw!")

elif (choice == computer+1 or (choice == 0 and computer == 2)):
    print("You win!")

else:
    print("You lost. Computer won.")