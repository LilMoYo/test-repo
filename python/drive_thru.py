menu = [
"🍔 Cheeseburger",
"🍟 Fries",
"🥤 Soda",
"🍦 Ice Cream",
"🍪 Cookie"
]

def get_item(food):
    if food > len(menu):
        print("We don't have that item!")
    else:
        food = menu[food-1]
        print(food)
    return food

def welcome():
    print("Welcome to MocYonalds!")
    print("What would you like to order?")
    for item in menu:
        print(f"{menu.index(item)+1}) {item}")

welcome()
option = int(input("Enter your option: "))
get_item(option)