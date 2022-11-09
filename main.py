from coffee_data import MENU, resources


# TODO 1: Ask the user what they want.


# TODO 2: Print a report


def play_game():
    money = 0
    should_refill = True

    def report():
        water = resources["water"]
        milk = resources["milk"]
        coffee = resources["coffee"]
        return f"Water: {water}ml\nMilk: {milk}ml:\nCoffee: {coffee}g.\nMoney: ${money}"

    # TODO 3: Get the details of the coffee the customer wants
    def type_of_coffee(coffee_type):
        return MENU[coffee_type]

    latte = type_of_coffee("latte")
    espresso = type_of_coffee("espresso")
    cappuccino = type_of_coffee("cappuccino")

    def calculate_money(coffee, milk, water, cost, coffee_type, current_balance):
        quarters = float(input("How many quarters?"))
        dimes = float(input("How many dimes?"))
        nickles = float(input("How many nickles?"))
        pennies = float(input("How many pennies?"))
        total_money = round((0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies), 2)
        change = round(total_money - cost, 2)
        if total_money < cost:
            print("Sorry that's not enough money. Money refunded.")
        else:
            current_balance += total_money
            resources["coffee"] -= coffee
            resources["milk"] -= milk
            resources["water"] -= water
            print(f"Here is ${change} in change.")
            print(f"Here is your {coffee_type}, enjoy!!")
        return current_balance

    while should_refill:
        user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
        if user_choice == "report":
            print(report())
        elif user_choice == "latte":
            l_water = latte["ingredients"]["water"]
            l_milk = latte["ingredients"]["milk"]
            l_coffee = latte["ingredients"]["coffee"]
            l_cost = latte["cost"]
            if resources["water"] >= l_water and resources["milk"] >= l_milk and resources["coffee"] >= l_coffee:
                print("Please insert coins")
                calculate_money(l_coffee, l_milk, l_water, l_cost, "Latte", money)
            elif resources["water"] < l_water:
                print("Sorry, there is not enough water.")
            elif resources["coffee"] < l_coffee:
                print("Sorry, there is not enough coffee.")
            else:
                print("Sorry, there is not enough milk.")

        elif user_choice == "espresso":
            e_water = espresso["ingredients"]["water"]
            e_coffee = espresso["ingredients"]["coffee"]
            e_cost = espresso["cost"]
            if resources["water"] >= e_water and resources["coffee"] >= e_coffee:
                print("Please insert coins")
                calculate_money(e_coffee, 0, e_water, e_cost, "Espresso", money)
            elif resources["water"] < e_water:
                print("Sorry, there is not enough water.")
            else:
                print("Sorry, there is not enough coffee.")

        elif user_choice == "cappuccino":
            c_water = cappuccino["ingredients"]["water"]
            c_milk = cappuccino["ingredients"]["milk"]
            c_coffee = cappuccino["ingredients"]["coffee"]
            c_cost = cappuccino["cost"]
            if resources["water"] >= c_water and resources["coffee"] >= c_coffee and resources["milk"] >= c_milk:
                print("Please insert coins")
                calculate_money(c_coffee, c_milk, c_water, c_cost, "Cappuccino", money)
            elif resources["water"] < c_water:
                print("Sorry, there is not enough water.")
            elif resources["coffee"] < c_coffee:
                print("Sorry, there is not enough coffee.")
            else:
                print("Sorry, there is not enough milk.")
        else:
            should_refill = False
            print("Unable to process coffee.")
    # TODO 4: check if there are enough resources for the user's drink


play_game()
