import art
from menu import MENU, resources
from account import money
from clear import clear_screen
import time

def make_coffee(drink):
    print("\n")
    print("Preparing your coffee...⾖")
    time.sleep(2)
    if drink == "chocolate":
        print("Adding milk...🥛")
        time.sleep(1)
    if drink == "latte":
        print("Adding steamed milk...🥛")
        time.sleep(1)
        print("Adding cream..🥤")
        time.sleep(1)
    for item in MENU[drink]["ingredients"]:
        resources[item] -= MENU[drink]["ingredients"][item]
    print("Your coffee has been prepared!")
    print("Please take your drink 🥤!")

def print_report():
    print("Resources: ")
    for item in resources:
        print(f"{item}: {resources[item]}")

def print_menu():
    print("\n=======  MENU  =======")
    print("1. Espresso: £1.5")
    print("2. Double Espresso: £3")
    print("3. Hot Chocolate: £3.5")
    print("4. Coffee Latte: £4\n")
    print("==  Technician only  ==")
    print("5. Report")
    print("6. Refill")
    print("======================")

def refill():
    print("Please enter the values in ml and g: ")
    for item in resources:
        value = int(input(f"{item}: "))
        resources[item] += value
    print("All has been added successfully!✅")

print("Starting the coffee machine...♨️")
time.sleep(2)
print("Coffe machine is ready!")
time.sleep(1)
print(art.logo)
print_menu()
user_action = input("Please select your coffee: (espresso / double / chocolate / latte)")
match user_action:
    case "espresso":
        print(art.espresso)
        make_coffee(user_action)
    case "double":
        print(art.double)
        make_coffee(user_action)
    case "chocolate":
        print(art.chocolate)
        make_coffee(user_action)
    case "latte":
        print(art.latte)
        make_coffee(user_action)
    case "report": print_report()
    case "refill":
        refill()
        print_report()



