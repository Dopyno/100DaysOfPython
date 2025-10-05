import random
from art import clear_screen, logo


def compare(player_num, random_num):
    """Compare the numbers!"""
    if player_num > random_num:
        return "Too big! ⬇️"
    elif player_num < random_num:
        return "Too low! ⬆️"
    elif player_num == random_num:
        play = False
        return "You win! 🥇"
    else:
        return "You lose 😭!"

def play_game():
    level = {"easy": 10, "hard": 5}
    number_to_guess = random.randint(1, 100)
    


    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    player_level = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()

    for num in range(level[player_level]):
        print(
            f"You have {level[player_level] - num} attempts remaining to guess the number."
        )
        player_number = int(input("Make a guess: "))
        print(compare(player_number, number_to_guess))
        play_game()
play_game()