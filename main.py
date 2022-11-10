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
    # def type_of_coffee(coffee_type):
    #     return MENU[coffee_type]

    # latte = type_of_coffee("latte")
    # espresso = type_of_coffee("espresso")
    # cappuccino = type_of_coffee("cappuccino")

    def calculate_money(coffee_quantity, milk, water, cost, coffee_type):
        """
        This function asks the user for the money, and the calculates the total, and does computation for the
        resources left :param coffee: :param milk: :param water: :param cost: :param coffee_type: :return: total_money
        """
        quarters = float(input("How many quarters?"))
        dimes = float(input("How many dimes?"))
        nickles = float(input("How many nickles?"))
        pennies = float(input("How many pennies?"))
        total_money = round((0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies), 2)
        change = round(total_money - cost, 2)
        if total_money < cost:
            print("Sorry that's not enough money. Money refunded.")
        else:
            resources["coffee"] -= coffee_quantity
            if coffee_type != "espresso":
                resources["milk"] -= milk
            else:
                # we deduct nothing from milk because espresso doesn't have milk
                resources["milk"] -= 0
            resources["water"] -= water
            print(f"Here is ${change} in change.")
            print(f"Here is your {coffee_type} ☕, enjoy!!")
        return total_money

    def is_resources_enough(coffee):
        """This function gets the type of coffee, and gets the ingredients, checks to see if the ingredients are sufficient
        if they are, gives you a coffee if you have money
        """
        water = MENU[coffee]["ingredients"]["water"]
        # since espresso doesn't have milk, I set milk to "" for expresso
        if coffee != "espresso":
            milk = MENU[coffee]["ingredients"]["milk"]
        else:
            milk = ""
        coffee_quantity = MENU[coffee]["ingredients"]["coffee"]
        cost = MENU[coffee]["cost"]
        # checking against items in the coffee ingredients against the resources available
        for item in MENU[coffee]["ingredients"]:
            if MENU[coffee]["ingredients"][item] > resources[item]:
                print(f"Sorry, there is not enough {item}.")
                # return false if the resources are not enough
                return False
            else:
                if coffee == "espresso":
                    calculate_money(coffee_quantity, 0, water, cost, coffee)
                else:
                    calculate_money(coffee_quantity, milk, water, cost, coffee)
                # return false if the order has been made so that there is no loop
                return False

    while should_refill:
        user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()

        if user_choice == "off":
            should_refill = False
        elif user_choice == "report":
            print(report())
        else:
            is_resources_enough(user_choice)

    # TODO 4: check if there are enough resources for the user's drink

    # TODO 5: Make sure the program asks the user for the coffee everytime


play_game()
