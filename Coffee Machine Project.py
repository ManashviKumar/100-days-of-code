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
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    money=(quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01)
    return money

def transaction(money,drinks_cost):
    if money >= drinks_cost:
        change=round(money-drinks_cost,2)
        print(f"Here's your change {change}")
        global profit
        profit+=drinks_cost
        return True
    else:
        print("Sorry,not enough money.")
        return False

def quant(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {drink_name},Enjoy!")

is_on = True
while True:
    user_input=input("What would you like?(espresso/latte/cappuccino): ").lower()
    if user_input=="off":
        is_on = False
    elif user_input == "report":
        print("We have the following resources :")
        print(f"water : {resources['water']}ml,")
        print(f"milk: {resources['milk']}ml,")
        print(f"coffee: {resources['coffee']}gm,")
        print(f"Money: ${profit}")
    else:
        drink=MENU[user_input]
        if quant(drink["ingredients"]):
            payment=coins()
            if transaction(payment,drink["cost"]):
                coffee(user_input,drink["ingredients"])


