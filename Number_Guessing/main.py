import random
from art import clear_screen, logo


def compare(player_num, random_num):
    """Compare the numbers for feedback!"""
    if player_num > random_num:
        print("Too big! ⬇️")
    elif player_num < random_num:
         print("Too low! ⬆️")


def play_game():
    clear_screen()
    print(logo)
    level = {"easy": 10, "hard": 5, "master": 3}
    level_num = {"easy": 50, "hard": 75, "master": 100}

    print("Welcome to the Number Guessing Game!")
    player_level = input("Choose a difficulty level. Type 'easy', 'hard' or 'master': ").lower()
    print(f"I'm thinking of a number between 1 and {level_num[player_level]}.")
    number_to_guess = random.randint(1, level_num[player_level])
    counter = level[player_level]
    # print(counter)
    while counter:
        print(
            f"You have {counter} attempts remaining to guess the number."
        )
        player_number = int(input("Make a guess: "))
        compare(player_number, number_to_guess)
        if player_number == number_to_guess:
            print("You win! 🥇")
            return 0
        counter -= 1
        if counter == 0:
            print("You lose! 🤪")
            print(f"The number was {number_to_guess}")
            break
    if input("Do you want to play again? (Y / N): ").lower() == 'y':
        clear_screen()
        play_game()
    else:
        print("Thank you for playing today!")
        return 0 
play_game()
