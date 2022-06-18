import blackjack_art as art
import random
import os

############### Our Blackjack House Rules #####################

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10 ,10]

def game():
    play_switch = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play_switch == 'y':
        os.system('cls||clear')
        print(art.logo)
        deal_cards()
        game()
    elif play_switch == 'n':
        print("\nSee you another time! 💕")
        return
    else:
        print("\nPlease enter a valid input.")
        game()

def deal_cards(cards = cards):
    
    your_cards = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards), random.choice(cards)]
    
    print(f"\nYour cards: {your_cards}, current score: {sum(your_cards)}")
    print(f"Computer's 🖥️ first card: {computer_cards[0]}")
    
    while sum(your_cards) < 21:
        redeal = input("\nType 'y' to get another card, type 'n' to pass: ").lower()
        
        if redeal == 'y':
            your_cards.append(random.choice(cards))
            print(f"\nYour cards: {your_cards}, current score: {sum(your_cards)}")
            print(f"Computer's 🖥️ first card: {computer_cards[0]}")

        else:
            break
    
    while sum(computer_cards) < 17:
        computer_cards.append(random.choice(cards))
    final_hands(your_cards, computer_cards)

def final_hands(y_cards, c_cards):
        print(f"\nYour final hand: {y_cards}, final score: {sum(y_cards)}")
        print(f"Computer's final hand: {c_cards}, final score: {sum(c_cards)}")

        if (sum(c_cards) < 21 and sum(y_cards) < 21):
            if sum(c_cards) > sum(y_cards):
                print("Computer wins. 👿")
            elif sum(c_cards) < sum(y_cards):
                print("You win 😁")
            else:
                print("It's a draw. ⚔️")

        elif (sum(y_cards) == 21):
            print("Win with a Blackjack 😎")

        elif (sum(y_cards) > 21):
            print("You overshot! You lose 👿")

        elif(sum(c_cards) > 21):
            print("Opponent went over. You win 😁")

        else:
            print("Computer wins with a Blackjack 👿")
        

### main body
game()
# deal_cards()