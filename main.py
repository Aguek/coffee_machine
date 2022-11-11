from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
while is_on:
    coffee_maker = CoffeeMaker()
    menu_obj = Menu()
    money_machine = MoneyMachine()

    user_choice = input(f"What would you like? {menu_obj.get_items()}: ").lower()
    if user_choice == "report":
        coffee_report = coffee_maker.report()
        money_report = money_machine.report()
    elif user_choice == "off":
        is_on = False
    else:
        # find drink
        drink = menu_obj.find_drink(user_choice)
        # check resources and process payments
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


