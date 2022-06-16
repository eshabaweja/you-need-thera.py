import hangman_pics as pics
import hangman_words
import random

# pick a word
chosen_word = random.choice(hangman_words.words).lower()
lives = 6
game_won = True

# testing code
""" print(chosen_word) """
print(f"\nWelcome to HANGMAN!\n{pics.hangman_arr[lives]}")

# create blanks
display = []

for i in range(len(chosen_word)):
    display += '_'

# play game
while '_' in display:
    # ask user input
    guess = input("\nGuess a letter: ").lower()

    # display if correct else kill
    for position in range(len(chosen_word)):
        if guess == chosen_word[position]:
            display[position] = guess
            
        
    if guess not in chosen_word:
        if lives > 1:
            lives -=1
            print(pics.hangman_arr[lives])

        else:
            game_won = False
            break

    print(f"{''.join(display)}")

""" if '_' not in display: """

# after exiting the loop
if game_won:
    print('''
                                               888            
                                               888            
                                               888            
 .d8888b .d88b. 88888b.  .d88b. 888d888 8888b. 888888.d8888b  
d88P"   d88""88b888 "88bd88P"88b888P"      "88b888   88K      
888     888  888888  888888  888888    .d888888888   "Y8888b. 
Y88b.   Y88..88P888  888Y88b 888888    888  888Y88b.      X88 
 "Y8888P "Y88P" 888  888 "Y88888888    "Y888888 "Y888 88888P' 
                             888                              
                        Y8b d88P                              
                         "Y88P"                               
    ''')
    print("You won!")
else:
    print(f"You lost. The word was {chosen_word}.")
    print(pics.hangman_arr[lives-1])