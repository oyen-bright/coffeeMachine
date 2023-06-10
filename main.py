from coffeMenue import  MENU

off_machine= False

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


def process_coind():
    quarters= int(input("Quarters:"))
    dimes= int(input("Dimes:"))
    nickles= int(input("Nickles:"))
    pennies= int(input("Pennies:"))
    return (0.25*quarters) + (0.10*dimes) + (0.05*nickles)+ (0.01*pennies)


def make_espresso():
    if is_resources_sufficient(MENU['espresso']):
        money_paid = process_coind()
        print(money_paid)
    return


def make_latte():
    return


def make_cappuccino():
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
        off_machine=True
    elif user_input == "report":
        print_report()
    else:
        print("Please Check input")



