import os
from art import art_logo

continue_game = True
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")  # Windows uses 'cls', Mac/Linux use 'clear'

print(art_logo)
print("\n")

print("Welcome to the secret auction!")
players = {}

while continue_game:
    name = input("What is you name: ")
    bid = int(input("What's your bid: £"))
    players[name] = bid
    morePlayers = input("Are there any others biders, (Yes / No): ")
    if morePlayers.lower() == "no":
        continue_game = False
    clear()

highest_bid = max(players, key=players.get)

print(f"The winner is {highest_bid}, with a bid of £{players[highest_bid]}")