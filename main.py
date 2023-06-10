from coffeMenue import MENU

off_machine = False

resources = {
    "water": {
        "value": 220,
        "unit": "ml"
    },
    "milk": {
        "value": 400,
        "unit": "ml"
    },
    "coffee": {
        "value": 100,
        "unit": "g"
    },
    "money": {
        "value": 0,
        "unit": "$"
    }
}


def is_resources_sufficient(menu):
    if resources['water']['value'] < menu['ingredients']['water']:
        print("Sorry, there is not enough water.")
        return False
    elif resources['coffee']['value'] < menu['ingredients']['coffee']:
        print("Sorry, there is not enough coffee.")
        return False
    elif 'milk' in menu['ingredients']:
        if resources['milk']['value'] < menu['ingredients']['milk']:
            print("Sorry, there is not enough milk.")
            return False
    return True


def process_coins():
    total = int(input("Quarters:"))*0.25
    total += int(input("Dimes:"))*0.10
    total += int(input("Nickles:"))*0.05
    total += int(input("Pennies:"))*0.01
    return total


def process_money(money_given, coffee_price):
    if money_given - coffee_price > 0:
        change = money_given - coffee_price
        print(f"Here is {change} dollars in change")
    resources['money']['value'] += coffee_price
    return


def make_coffee(data):
    resources['water']['value'] -= data['ingredients']['water']
    resources['coffee']['value'] -= data['ingredients']['coffee']
    if 'milk' in data['ingredients']:
        resources['milk']['value'] -= data['ingredients']['milk']
    return


def make_espresso():
    coffee_data = MENU['espresso']
    if is_resources_sufficient(coffee_data):
        money_paid = process_coins()
        print(money_paid)
        print(coffee_data['cost'])
        if money_paid > coffee_data['cost']:
            process_money(money_paid, coffee_data['cost'])
            make_coffee(coffee_data)
            print('Here is your Espresso. Enjoy!”')
        else:
            print("Sorry that's not enough money. Money refunded.")
    return


def make_latte():
    coffee_data = MENU['latte']
    if is_resources_sufficient(coffee_data):
        money_paid = process_coins()
        print(money_paid)
        print(coffee_data['cost'])
        if money_paid > coffee_data['cost']:
            process_money(money_paid, coffee_data['cost'])
            make_coffee(coffee_data)
            print('Here is your Latte. Enjoy!”')
        else:
            print("Sorry that's not enough money. Money refunded.")
    return


def make_cappuccino():
    coffe_data = MENU['cappuccino']
    if is_resources_sufficient(coffe_data):
        money_paid = process_coins()
        print(money_paid)
        print(coffe_data['cost'])
        if money_paid > coffe_data['cost']:
            process_money(money_paid, coffe_data['cost'])
            make_coffee(coffe_data)
            print('Here is your Cappuccino. Enjoy!”')
        else:
            print("Sorry that's not enough money. Money refunded.")
    return


def print_report():
    for key, value in resources.items():
        print(f"{key.title()}: {value['value']}{value['unit']}")
    return


while off_machine is False:
    user_input = input("What would you like? (espresso/latte/cappuccino):")

    if user_input == "espresso":
        make_espresso()
    elif user_input == "latte":
        make_latte()
    elif user_input == "cappuccino":
        make_cappuccino()
    elif user_input == "off":
        off_machine = True
    elif user_input == "report":
        print_report()
    else:
        print("Please Check input")
