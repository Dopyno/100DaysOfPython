import random
from art import clear_screen, logo

# EASY_LEVEL = 20
# HARD_LEVEL = 5
# MASTER = 3

# def set_difficulty():
#     """CHOOSE A LEVEL OF DIFFICULTY"""
#     level = input("Choose a difficulty. Type 'easy', 'hard' or 'master': ")
#     if level == "easy":
#         return EASY_LEVEL
#     else:
#         return HARD_LEVEL


def compare(player_num, random_num, number_to_guess):
    """Compare the numbers for feedback!"""
    if player_num > random_num:
        print("Too big! ⬇️")
        print("Guess again!")
        return False
    elif player_num < random_num:
        print("Too low! ⬆️")
        print("Guess again!")
        return False
    elif player_num == random_num:
        print("You win! 🥇")
        print(f"The number was {number_to_guess}")
        return True


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
        if compare(player_number, number_to_guess, number_to_guess):
            break
        # if player_number == number_to_guess:
        #     print("You win! 🥇")
        #     print(f"The number was {number_to_guess}")
        #     return 0
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


