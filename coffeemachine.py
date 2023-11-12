
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

# CHOICE = input("What would you like? (espresso/latte/cappuccino): ").lower()

def is_resources_available(ingredients):
    """"Returns true when order can be made, false if ingredients are insufficient"""
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print("Sorry, there is not enough {item}")
            False
    True

def process_coins():
    """"Returns the total calculated from process_coins inserted"""
    print("Please inset process_coins")
    total = int(input("\thow many quarters?: ")) * 0.25
    total += int(input("\thow many dimes?: ")) * 0.10
    total += int(input("\thow many nickels?: ")) * 0.05
    total += int(input("\thow many pennies?: ")) * 0.01
    return total
    

def is_transaction_successful(money_received, drink_cost):
    """"Deduct required ingredients from the resources"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money,money refunded")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")

while True:
    CHOICE = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if CHOICE == "off":
        False
    elif CHOICE == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[CHOICE]
        if is_resources_available(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(CHOICE, drink["ingredients"])