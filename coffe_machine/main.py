import art
from menu import MENU, resources
from account import money
from clear import clear_screen
import time
from account import money, receipt
import sys


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
    money["pounds"] += MENU[drink]["cost"]
    print("Your coffee has been prepared!")
    print("Please take your drink 🥤!")


def print_report():
    print("Resources: ")
    for item in resources:
        print(f"{item}: {resources[item]}")
    for item in money:
        print(f"Total money: {money[item]}")


def print_menu():
    print("\n=======  MENU  =======")
    print("1. Espresso: £1.5")
    print("2. Double Espresso: £3")
    print("3. Hot Chocolate: £3.5")
    print("4. Coffee Latte: £4\n")
    print("==  Technician only  ==")
    print("5. Report")
    print("6. Refill")
    print("7. Cash")
    print("======================")


def refill():
    print("Please enter the values in ml and g: ")
    for item in resources:
        value = int(input(f"{item}: "))
        resources[item] += value
    print("All has been added successfully!✅")


def cash_out():
    if (input("Do you want to withdrew all the money (Y / N): ")).lower() == "y":
        money["pounds"] = 0
        print("Processing", end="")
        for _ in range(5):
            time.sleep(0.5)
            print(".", end="")
            sys.stdout.flush()
        print("\nThe money has been withdraw successfully!✅")
    else:
        print("You have been transferred to the main menu!")
        return


def starting_coffee_machine():
    print("Starting the coffee machine♨️ ", end="")
    for _ in range(5):
        time.sleep(0.5)
        print(".", end="")
        sys.stdout.flush()
    print("\nCoffee machine is ready!")
    time.sleep(1)
    print(art.logo)


def print_receipt():
    print("=====  Receipt  =====")
    for i in receipt:
        print(i)
    print("=====================")

def start():
    starting_coffee_machine()
    is_on = True

    while is_on:
        print_menu()
        user_action = input(
            "Please select your coffee: (espresso / double / chocolate / latte or Exit): "
        ).lower()
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
            case "report":
                print_report()
            case "refill":
                refill()
                print_report()
            case "cash":
                cash_out()
        if(user_action) == "exit":

    clear_screen()
