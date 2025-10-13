from art import logo, espresso, double_espresso, chocolate, latte, clear_screen
from menu import MENU, resources
from account import money
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
    print("=========  MENU  =========")
    print("")

