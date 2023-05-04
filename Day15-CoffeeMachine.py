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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

resources_remaining = resources
check_resource_flag = True

machine_toggle = "on"


def report():
    print(f"Water: {resources_remaining['water']}ml\nMilk: {resources_remaining['milk']}ml\nCoffee: {resources_remaining['coffee']}ml")

def check_resources(user_input):
    if user_input == "espresso":
        if resources_remaining["water"] < MENU["espresso"]["ingredients"]["water"]:
            print("Sorry there is not enough water")
            return False
        elif resources_remaining["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee")
            return False
        else :
            print(f"Making your {user_input} !!")
            return True
    elif user_input == "latte":
        if resources_remaining["water"] < MENU["latte"]["ingredients"]["water"]:
            print("Sorry there is not enough water")
            return False
        elif resources_remaining["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee")
            return False
        elif resources_remaining["milk"] < MENU["latte"]["ingredients"]["milk"]:
            print("Sorry there is not enough milk")
            return False
        else :
            print(f"Making your {user_input} !!")
            return True
    elif user_input == "cappuccino":
        if resources_remaining["water"] < MENU["cappuccino"]["ingredients"]["water"]:
            print("Sorry there is not enough water")
            return False
        elif resources_remaining["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee")
            return False
        elif resources_remaining["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
            print("Sorry there is not enough milk")
            return False
        else :
            print(f"Making your {user_input} !!")
            return True



# print(f"check_resource_flag : {check_resource_flag}")

def refactor_resources(user_input):
    if user_input == "espresso":
        resources_remaining["water"] = resources_remaining["water"] - MENU["espresso"]["ingredients"]["water"]
        resources_remaining["coffee"] = resources_remaining["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
    elif user_input == "latte":
        resources_remaining["water"] = resources_remaining["water"] - MENU["latte"]["ingredients"]["water"]
        resources_remaining["milk"] = resources_remaining["milk"] - MENU["latte"]["ingredients"]["milk"]
        resources_remaining["coffee"] = resources_remaining["coffee"] - MENU["latte"]["ingredients"]["coffee"]
    elif user_input == "cappuccino":
        resources_remaining["water"] = resources_remaining["water"] - MENU["cappuccino"]["ingredients"]["water"]
        resources_remaining["milk"] = resources_remaining["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
        resources_remaining["coffee"] = resources_remaining["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]

# refactor_resources(user_input)
# print(resources_remaining)

def process_coins(no_quaters,no_dimes,no_nickels,no_pennies,user_input):

    total_money = (no_quaters * 0.25) + (no_dimes * 0.10) + (no_nickels * 0.05) + (no_pennies * 0.01)

    if user_input == "espresso":
        if total_money > MENU["espresso"]["cost"]:
            change = round(total_money - MENU["espresso"]["cost"],2)
            print(f"Here is ${change} in change.")
            print("Here is your espresso !! Enjoy")
            return True
        elif total_money < MENU["espresso"]["cost"]:
            print("Insuffient fund!!")
            return False
        elif total_money == MENU["espresso"]["cost"]:
            print("Here is your espresso !! Enjoy")
            return True
    elif user_input == "latte":
        if total_money > MENU["latte"]["cost"]:
            change = round(total_money - MENU["latte"]["cost"],2)
            print(f"Here is ${change} in change.")
            print("Here is your latte !! Enjoy")
            return True
        elif total_money < MENU["latte"]["cost"]:
            print("Insuffient fund!!")
            return False
        elif total_money == MENU["latte"]["cost"]:
            print("Here is your latte !! Enjoy")
            return True
    elif user_input == "cappuccino":
        if total_money > MENU["cappuccino"]["cost"]:
            change = round(total_money - MENU["cappuccino"]["cost"],2)
            print(f"Here is ${change} in change.")
            print("Here is your cappuccino !! Enjoy")
            return True
        elif total_money < MENU["cappuccino"]["cost"]:
            print("Insuffient fund!!")
            return False
        elif total_money == MENU["cappuccino"]["cost"]:
            print("Here is your cappuccino !! Enjoy")
            return True
        
suffient_fund = True

while machine_toggle == "on":
    user_input = input("What would you like ? (espresso/latte/cappuccino):")
    if user_input == "off":
        machine_toggle = "off"
    if user_input == "report":
        report()
    check_resource_flag = check_resources(user_input)
    if check_resource_flag:  
        print("Please insert coins:")
        no_quaters = int(input("How many quaters ?"))
        no_dimes = int(input("How many dimes ?"))
        no_nickels = int(input("How many nickels ?"))
        no_pennies = int(input("How many pennies ?"))
        suffient_fund = process_coins(no_quaters,no_dimes,no_nickels,no_pennies,user_input)
        # print(f"suffient_fund : {suffient_fund}")
        if suffient_fund:
            refactor_resources(user_input)