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

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money:.2f}")

def check_resources(drink):
    resources_score = 3
    if resources['water'] < MENU[drink]['ingredients']['water']:
        print(f"Sorry! There is not enough water.")
        resources_score -= 1
    if resources['coffee'] < MENU[drink]['ingredients']['coffee']:
        print(f"Sorry! There is not enough coffee.")
        resources_score -= 1
    if drink != "espresso":
        if resources['milk'] < MENU[drink]['ingredients']['milk']:
            print(f"Sorry! There is not enough milk.")
            resources_score -= 1
    return resources_score

def calculate_coins():
    quarters = int(input("How any quarters: "))
    dimes = int(input("How any dimes: "))
    nickels = int(input("How any nickels: "))
    pennies = int(input("How any pennies: "))
    calculated_coins = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies)
    return calculated_coins

money = 0
power = True

while power:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        power = False
    elif choice == "report":
        print_report()
    elif choice in ["espresso", "latte", "cappuccino"]:
        score = check_resources(choice)
        if score == 3:
            print(f"Please inset coins.")
            coins = calculate_coins()
            if coins < MENU[choice]['cost']:
                print(f"Sorry! That's not enough money. Money refunded.")
            else:
                resources['water'] = resources['water'] - MENU[choice]['ingredients']['water']
                if choice in ["latte", "cappuccino"]:
                    resources['milk'] = resources['milk'] - MENU[choice]['ingredients']['milk']
                resources['coffee'] = resources['coffee'] - MENU[choice]['ingredients']['coffee']
                money = coins - MENU[choice]['cost']
                print(f"Here is your ${money:.2f} in change.")
                print(f"Here is your {choice} \u2615 Enjoy!")