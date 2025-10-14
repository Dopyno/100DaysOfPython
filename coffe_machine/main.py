import art
from menu import MENU, resources
from clear import clear_screen
import time
from account import money, receipt, total_receipt
import sys


def make_coffee(drink):
    print("\n")
    print("Preparing your coffee ⾖ ", end="")
    spinner()
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
    total_receipt.append(MENU[drink]["cost"])
    receipt.append(drink.title())

    print("Your coffee has been prepared!")
    print("Please take your drink 🥤!")


def print_report():
    print("\n======  REPORT  ======")
    print("Resources: ")
    for item in resources:
        print(f"{item}: {resources[item]}")
    for item in money:
        print(f"Total money: {money[item]}")
    print("=======================")


def print_menu():
    print("\n=======  MENU  =======")
    print("1. Espresso: £1.5")
    print("2. Double Espresso: £3")
    print("3. Hot Chocolate: £3.5")
    print("4. Coffee Latte: £4")
    print("5. Receipt")
    print("0. Exit\n")
    print("***  Technician only  ***")
    print("6. Report")
    print("7. Refill")
    print("8. Cash")
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
    time.sleep(1)
    print(art.logo)
    print("Starting the coffee machine♨️ ", end="")
    for _ in range(5):
        time.sleep(0.5)
        print(".", end="")
        sys.stdout.flush()
    print("\nCoffee machine is ready!☕️")


def print_receipt():
    clear_screen()
    global receipt, total_receipt
    print("\n=====  Receipt  =====")
    for i in receipt:
        print(f"{receipt.index(i) + 1}. {i}: £{MENU[i.lower()]["cost"]}")
    print("---------------------")
    print(f"Total: £{sum(total_receipt)}")
    print("=====================")
    print("\nEntering standby mode....")
    input("Press Enter to continue for next customer...")
    print("Waiting for next customer", end="")
    for _ in range(7):
        time.sleep(0.5)
        print(".", end="")
        sys.stdout.flush()
    receipt = []
    total_receipt = []
    clear_screen()


def spinner():
    spinner = ["|", "/", "-", "\\"]

    for _ in range(20):  # se rotește de 20 de ori
        for simbol in spinner:
            sys.stdout.write(simbol)
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write("\b")  # șterge simbolul anterior
    print("")


def loading(x):
    for _ in range(x):
        time.sleep(0.5)
        print(".", end="")
        sys.stdout.flush()


def start():
    starting_coffee_machine()
    is_on = True

    while is_on:
        print_menu()
        user_action = input(
            "Please select your coffee: (espresso / double / chocolate / latte / receipt or EXIT): "
        )

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
            case "receipt":
                print_receipt()
            case "exit":
                print("Thank you for choosing our service!")
                time.sleep(1)
                print("Turning off the machine", end="")
                loading(5)
                is_on = False
    clear_screen()


start()
