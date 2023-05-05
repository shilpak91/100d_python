from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()


machine_on = True

while machine_on:
    options = menu.get_items()
    user_choice = input(f"What would you like ? {options} : ")
    if user_choice == "off":
        machine_on = False
    elif user_choice == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_choice)
        # print(f"drink : {drink}")
        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)
