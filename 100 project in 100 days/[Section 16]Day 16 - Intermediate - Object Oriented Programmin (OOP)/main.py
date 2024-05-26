from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
while True:
    while True:
        prompt = input(f"What would you like? ({menu.get_items()}): ").lower()
        if prompt == "espresso" or prompt == "latte" or prompt == "cappuccino" or prompt == "off" or prompt == "report": 
            break
        print(f"There is no {prompt}")
    if prompt == "report":
        coffee_maker.report()
        money_machine.report()
    elif prompt == "off":
        exit()        
    else:
        drink = menu.find_drink(prompt)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
