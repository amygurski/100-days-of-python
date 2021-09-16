from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
menu = Menu()
coffee_maker = CoffeeMaker()
keep_vending = True

while keep_vending:
    options = menu.get_items()
    selection = input("What would you like? (espresso/latte/cappuccino/): ")

    if selection == 'report':
        coffee_maker.report()
        money_machine.report()
    elif selection == "off":
        print("Shutting down for maintenance. Goodbye!")
        keep_vending = False
    else:
        drink = menu.find_drink(selection)
        has_ingredients = coffee_maker.is_resource_sufficient(drink)
        
        if has_ingredients:
            paid_enough = money_machine.make_payment(drink.cost)
            if paid_enough:
                coffee_maker.make_coffee(drink)
