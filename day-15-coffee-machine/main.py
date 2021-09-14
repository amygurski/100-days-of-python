from replit import clear
from coffee_machine_art import logo

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

COIN_VALUES = {
        "quarters" : 0.25,
        "dimes" : 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def vending_machine_ui():
    clear()
    print(logo)
    print(f"""
-------------------------
| ☕ espresso   | {'${:,.2f}'.format(MENU["espresso"]['cost'])} |
| ☕ latte      | {'${:,.2f}'.format(MENU["latte"]['cost'])} |
| ☕ cappuccino | {'${:,.2f}'.format(MENU["cappuccino"]['cost'])} |
-------------------------
""")

def prompt_user():
    return input("What would you like? (espresso/latte/cappuccino): ")

def print_report():
    for resource, qty in resources.items():
        print(resource, ':', qty)

def sufficient_resources(drink_selection):
    for ingredient, qty in MENU[drink_selection]["ingredients"].items():
        if resources[ingredient] < qty:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True

def process_coins():
    print("Insert coins.")
    total_paid = 0
    for coin in COIN_VALUES:
        total_paid += int(input(f"how many {coin}? ")) * COIN_VALUES[coin]
    return round(total_paid,2)

def check_transaction(drink_selection,total_paid):
    if MENU[drink_selection]["cost"] > total_paid:
        print(f"Sorry ${total_paid} is insufficient money. {drink_selection} costs {'${:,.2f}'.format(MENU[drink_selection]['cost'])}.\nMoney refunded.")
        return False

    resources["money"] = MENU[drink_selection]['cost']
    
    if MENU[drink_selection]["cost"] != total_paid:
        change = '${:,.2f}'.format(total_paid - MENU[drink_selection]['cost'])
        print(f"Here is {change} dollars in change.")

    return True

def dispense_coffee(drink_selection):
    for ingredient, qty in MENU[drink_selection]["ingredients"].items():
        resources[ingredient] -= qty
    print(f"Here is your {drink_selection} ☕. Enjoy!")

keep_vending = True
while keep_vending:
    vending_machine_ui()
    drink_selection = prompt_user()

    if drink_selection == 'report':
        print_report()
    else:
        has_ingredients = sufficient_resources(drink_selection)
        
        if has_ingredients:
            total_paid = process_coins()
            paid_enough = check_transaction(drink_selection,total_paid)

            if paid_enough:
                dispense_coffee(drink_selection)
    
    if input("Would you like to make another selection? (y/n) ") != 'y':
        print("Have a good day!")
        keep_vending = False


