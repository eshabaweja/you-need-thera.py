#Number Guessing Game Objectives:

from random import randint

print('''
                           ('-.    .-')     .-')          .-') _    ('-. .-.   ('-.             .-') _             _   .-')   .-. .-')    ('-.  _  .-')   
                         _(  OO)  ( OO ).  ( OO ).       (  OO) )  ( OO )  / _(  OO)           ( OO ) )           ( '.( OO )_ \  ( OO ) _(  OO)( \( -O )  
  ,----.    ,--. ,--.   (,------.(_)---\_)(_)---\_)      /     '._ ,--. ,--.(,------.      ,--./ ,--,' ,--. ,--.   ,--.   ,--.);-----.\(,------.,------.  
 '  .-./-') |  | |  |    |  .---'/    _ | /    _ |       |'--...__)|  | |  | |  .---'      |   \ |  |\ |  | |  |   |   `.'   | | .-.  | |  .---'|   /`. ' 
 |  |_( O- )|  | | .-')  |  |    \  :` `. \  :` `.       '--.  .--'|   .|  | |  |          |    \|  | )|  | | .-') |         | | '-' /_)|  |    |  /  | | 
 |  | .--, \|  |_|( OO )(|  '--.  '..`''.) '..`''.)         |  |   |       |(|  '--.       |  .     |/ |  |_|( OO )|  |'.'|  | | .-. `.(|  '--. |  |_.' | 
(|  | '. (_/|  | | `-' / |  .--' .-._)   \.-._)   \         |  |   |  .-.  | |  .--'       |  |\    |  |  | | `-' /|  |   |  | | |  \  ||  .--' |  .  '.' 
 |  '--'  |('  '-'(_.-'  |  `---.\       /\       /         |  |   |  | |  | |  `---.      |  | \   | ('  '-'(_.-' |  |   |  | | '--'  /|  `---.|  |\  \  
  `------'   `-----'     `------' `-----'  `-----'          `--'   `--' `--' `------'      `--'  `--'   `-----'    `--'   `--' `------' `------'`--' '--' 
''')

print("I'm thinking of a number between 1 and 100.")
num = randint(1,101)
level = input("Pick a level. Enter 'easy' or 'hard': ").lower()

# function definition
def compare(attempts):
    while (attempts>0):
        choice = int(input("Enter your choice: "))
        
        if choice>num:
            print("Too high.")
        elif choice<num:
            print("Too low.")
        else:
            print(f"You're omniscient! The answer was {num}.")
            return
        attempts -= 1
    print("You ran out of guesses :(")

# main body
if level == 'hard':
    attempts = 5
    compare(attempts)

elif level == 'easy':
    attempts = 10
    compare(attempts)

else:
    print("Invalid input.")