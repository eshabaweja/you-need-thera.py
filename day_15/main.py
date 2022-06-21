################### Coffee Making Machine ###################

# Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# Turn off the Coffee Machine by entering “off” to the prompt.
def prompt_user():
    choice = input("\n\nWhat would you like? (espresso/latte/cappuccino):").lower()
    # if check_resources(choice) == True:
    if choice == 'off':
        return False

    elif choice == 'report':
        report()

    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if transaction_successful(payment, drink['cost']):
                deduct_ingredients(choice, drink['ingredients'])
            
    return True

# Print report.
def report():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}")

# Check resources sufficient?
def check_resources(coffee_choice):

    for item in coffee_choice:

        if coffee_choice[item] >= resources[item]:
            print(f"Sorry! Not enough {item}.")
            return False
    return True
"""     cost_need = MENU[coffee_choice]['cost'] """
    
# Process coins.
def process_coins():
    # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    print("Please insert coins.")
    total = int(input("\nQuarters: "))*0.25 
    total += int(input("\nDimes: "))*0.10 
    total += int(input("\nNickles: "))* 0.05 
    total += int(input("\nPennies: "))*0.01

    return total

# success or failure
def transaction_successful(money_received, drink_cost):
    # true is money accepted, else false
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is ${change} in change.")

        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

# deduct used ingredients
def deduct_ingredients(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")

################### Main ###################
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


################## Running forever ##################
make_coffee = True
while make_coffee:
    make_coffee = prompt_user()