import os

print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''',
"\nWelcome to the Secret Auction Program.")

bids = {}

def add_bids(bid_dict = bids):
    name = input("What is your name? ")
    bid_price = int(input("\nWhat is your bid price? "))
    
    bid_dict[name] = bid_price
    others = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    
    if others == 'yes':
        os.system('cls||clear')
        add_bids()
    else:
        return

def highest_bid(bid_record):
    max_bid = 0
    for bidder in bid_record:
        if max_bid < bid_record[bidder]:
            max_bid = bid_record[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${max_bid}.")

add_bids()
print(bids)
highest_bid(bids)
