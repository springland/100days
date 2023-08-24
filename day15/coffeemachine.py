
from coffeedata import MENU
from coffeedata import resources


money = 0.0


COINS = {
    'penny' : 0.01 ,
    'nickle' : 0.05 ,
    'dime' : 0.1 ,
    'quarter': 0.25

}


def print_report():
    print(f"Available water {resources['water']}ml")
    print(f"Available milk {resources['milk']}ml")
    print(f"Available coffee {resources['coffee']}g")
    print(f"Money {money: .2f}")

def check_if_enough_resource_available(coffee_type):

    coffee_info = MENU[coffee_type]

    for ingredient in coffee_info['ingredients']:
        if coffee_info['ingredients'][ingredient] > resources[ingredient]:
            return False

    return True


def collect_money():
    total = 0

    quarter = int(input(" How many quarters"))
    dime = int(input("How many dimes"))
    nickle = int(input("How many nickles"))
    penny = int(input("How many penny"))

    total += quarter * COINS['quarter'] + dime * COINS['dime'] + nickle*COINS['nickle'] + penny*COINS['penny']


    return total



def coffee_machine():

    global money
    global resources

    while(True):
        menu_item = input('What would you like? (espresso/latte/cappauccino):')
        if menu_item == 'report':
            print_report()
        else:
            if menu_item in MENU:
                if check_if_enough_resource_available(menu_item):
                    collected = collect_money()
                    coffee_info = MENU[menu_item]

                    if collected >= coffee_info["cost"]:
                        for ingredient in coffee_info['ingredients']:
                            resources[ingredient] -= coffee_info['ingredients'][ingredient]
                        money += coffee_info["cost"]
                        print(f' Total collected {collected:.2f} , change {collected - coffee_info["cost"]: .2f}')

                    else:
                        print(f" Total collected {collected:.2f} , not enough for {coffee_info['cost']} , refund ")
                else:
                    print(f'Sorry , not enough resource to make {menu_item}')

coffee_machine()
