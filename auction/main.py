import os
from art import art_logo

bidding_finished = False
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")  # Windows uses 'cls', Mac/Linux use 'clear'

print(art_logo)
print("\n")

print("Welcome to the secret auction!")
players = {}

def find_highest_bid(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"angela": 123, "marius": 333}
    for bidder in players:
        big_amount = players[bidder]
        if big_amount > highest_bid:
            highest_bid = big_amount
            winner = bidder
    print(f"The winner is {winner}, with a bid of £{highest_bid}")


while not bidding_finished:
    name = input("What is you name?: ")
    bid = int(input("What's your bid?: £"))
    players[name] = bid
    morePlayers = input("Are there any others biders, (Yes / No): \n")
    if morePlayers.lower() == "no":
        bidding_finished = True
        find_highest_bid(players)
    elif morePlayers.lower() == "yes":
        clear() 

# highest_bid = max(players, key=players.get)

# print(f"The winner is {highest_bid}, with a bid of £{players[highest_bid]}")