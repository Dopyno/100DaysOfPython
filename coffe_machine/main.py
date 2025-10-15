import art
from menu import MENU, resources, actions, extra_steps
from clear import clear_screen
import time
from account import money, receipt, total_receipt
import sys
from authenticate import TECHNICIAN_PASSWORD
import getpass


def authenticate():
    """Require to authenticate if you want to access technician menu"""
    password = getpass.getpass("Enter technician password: ")  # password similar Linux
    if password == TECHNICIAN_PASSWORD:
        print("Password accepted! ✅")
        return True
    else:
        print("❌ Access denied. Incorrect password.")
        return False


def make_coffee(drink):
    """function that select the drink by user selection"""
    if not check_money(drink):
        print("Sorry, insufficient funds for your drink!❌")
        return
    if not check_stock(drink):
        print("Cannot prepare coffee, please refill the machine.")
        return
    print("\n")
    print("Preparing your coffee ⾖ ", end="")
    spinner()
    progress_bar("Heating water: ", 3)
    progress_bar("Brewing coffee: ", 2)
    time.sleep(2)
    for step in extra_steps.get(drink, []):
        print(step)
        time.sleep(1)
    for item in MENU[drink]["ingredients"]:
        resources[item] -= MENU[drink]["ingredients"][item]
    # money["pounds"] += MENU[drink]["cost"]     double line already adding on check_money

    total_receipt.append(MENU[drink]["cost"])
    receipt.append(drink.title())

    print("\nYour coffee has been prepared!")
    print("Please take your drink 🥤!")


def check_stock(coffee):
    for item in MENU[coffee]["ingredients"]:
        required = MENU[coffee]["ingredients"][item]
        available = resources[item]
        if required > available:
            print(
                f"❌Sorry insufficient {item}. Needed:  {required}, Available: {available}"
            )
            return False
    return True


def print_report():
    """Print report for technician only"""
    if not authenticate():
        return
    print("\n======  REPORT  ======")
    print("Resources: ")
    for item in resources:
        print(f"{item}: {resources[item]}")
    print(f"Total money: £{money['pounds'] / 100:.2f}")
    print("=======================")
    input("Press Enter to return to the main menu. ")


def print_menu():
    """Print menu for customers"""
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
    """Refill method only for technicians."""
    if not authenticate():
        return
    print("Please enter the values in ml and g: ")
    for item in resources:
        try:
            value = int(input(f"{item}: ") or "0")
            resources[item] += value
        except ValueError:
            print("Invalid input❌. Enter a number!")
            return

    print("All has been added successfully!✅")


def cash_out():
    """Withdraw the founds only by technicians."""
    if not authenticate():
        return
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
    """Staring the coffee machine"""
    time.sleep(1)
    print(art.logo)
    print("Starting the coffee machine♨️ ", end="")
    for _ in range(5):
        time.sleep(0.5)
        print(".", end="")
        sys.stdout.flush()
    print("\nCoffee machine is ready!☕️")


def progress_bar(task, duration=3):
    print(task, end="")
    for _ in range(duration * 5):
        time.sleep(0.2)
        print("█", end="")
        sys.stdout.flush()
    print()


def print_receipt():
    """Print the receipt only for customers"""
    clear_screen()
    global receipt, total_receipt
    print("\n=====  Receipt  =====")
    for i in receipt:
        price = MENU[i.lower()]["cost"] / 100
        print(f"{receipt.index(i) + 1}. {i}: £{price}")
    print("---------------------")
    print(f"Total: £{sum(total_receipt) / 100}")
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
    """Create effect for preparing the coffee"""
    spinner = ["|", "/", "-", "\\"]

    for _ in range(20):  # se rotește de 20 de ori
        for simbol in spinner:
            sys.stdout.write(simbol)
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write("\b")  # șterge simbolul anterior
    print("")


def loading(x):
    """Create the loading effect"""
    for _ in range(x):
        time.sleep(0.5)
        print(".", end="")
        sys.stdout.flush()


def check_money(drink):
    try:
        one_pound = int(input("Please enter one pound coins: "))
        fifty_pence = int(input("Please enter fifty pence coins: "))
        twenty_pence = int(input("Please enter twenty pence coins: "))
        ten_pence = int(input("Please enter ten pence coins: "))
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
        return False

    total = (
        (one_pound * 100) + (fifty_pence * 50) + (twenty_pence * 20) + (ten_pence * 10)
    )
    drink_price = MENU[drink]["cost"]
    if total < drink_price:
        print("Sorry, insufficient founds for you drink!❌")
        return False
    if total >= drink_price:
        money["pounds"] += drink_price
        refound = round(total - drink_price, 2) / 100
        total_in_pounds = total / 100
        print(f"Total inserted: £{total_in_pounds:.2f}")
        print(f"Here's your change: £{refound:.2f}")
        return True


def start():
    starting_coffee_machine()
    is_on = True

    while is_on:
        print_menu()
        user_action = input(
            "Please select your coffee: (espresso / double / chocolate / latte / receipt or EXIT): "
        )
        if user_action not in actions:
            print("Invalid option, please try again!❌")
            continue

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
