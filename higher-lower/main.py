import random
from art import logo, vs, clear_screen
from game_data import data


def generate(data_set):
    return random.choice(data_set)


def refine_data(dataSet1):
    """Format the account data."""
    name = dataSet1["name"]
    description = dataSet1["description"]
    country = dataSet1["country"]
    followers = dataSet1["follower_count"]

    return name, description, country, followers

# def format_data(account):
#     acc_name = account["name"]
#     acc_descr = account["description"]
#     acc_country = account["country"]
#     return f"{acc_name}, a {acc_descr}, from {acc_country}"

def play_game():
    play = True
    score = 0
    # clear_screen()
    # print(logo)
    version_a = refine_data(generate(data))
    version_b = refine_data(generate(data))
    if version_a == version_b:
        version_b = refine_data(generate(data))

    while play:
       
        print(logo)
        # version_a = refine_data(generate(data))

        print(f"Score: {score}")

        print(
            f"Compare: A => {version_a[0]}, a {version_a[1]}, from {version_a[2]}"
        )
        print(vs)
        print(
            f"Compare: B => {version_b[0]}, a {version_b[1]}, from {version_b[2]}"
        )

        user = input("Who has more followers? 'A' or 'B': ").lower()

        if version_a[3] >= version_b[3] and user == "a":
            score += 1
            print(f"Great, your current score {score}")
            version_b = refine_data(generate(data))
            clear_screen()
        elif version_a[3] <= version_b[3] and user == "b":
            score += 1
            print(f"You'r right, your current score {score}")
            version_a = refine_data(generate(data))
            clear_screen()
        else:
            print(f"Game over, your final score: {score}")
            play = False
    if input("Do you want to continue? (Y or N): ").lower() == "y":
        play_game()
    else:
        print(f"Game over, your final score: {score}")


play_game()


# from art import logo, vs
# from game_data import data
# import random
# from replit import clear


# def format_data(account):
#     """Takes the account data and returns the printable format."""
#     account_name = account["name"]
#     account_descr = account["description"]
#     account_country = account["country"]
#     return f"{account_name}, a {account_descr}, from {account_country}"


# def check_answer(guess, a_followers, b_followers):
#     """Take the user guess and follower counts and returns if they got it right."""
#     if a_followers > b_followers:
#         return guess == "a"
#     else:
#         return guess == "b"


# # Display art
# print(logo)
# score = 0
# game_should_continue = True
# # Generate a random account from the game data.
# account_b = random.choice(data)

# # Make the game repeatable.
# while game_should_continue:

#     # Making account at position B become the next account at position A.
#     account_a = account_b
#     account_b = random.choice(data)

#     if account_a == account_b:
#         account_b = random.choice(data)

#     print(f"Compare A: {format_data(account_a)}.")
#     print(vs)
#     print(f"Against B: {format_data(account_b)}.")

#     # Ask user for a guess.
#     guess = input("Who has more followers? Type 'A' or 'B': ").lower()

#     # Check if user is correct.
#     ## Get follower count of each account.
#     a_follower_count = account_a["follower_count"]
#     b_follower_count = account_b["follower_count"]
#     is_correct = check_answer(guess, a_follower_count, b_follower_count)

#     # Clear the screen between rounds.
#     clear()
#     print(logo)

#     # Give user feedback on their guess.
#     # Score keeping.
#     if is_correct:
#         score += 1
#         print(f"You're right! Current score: {score}.")
#     else:
#         game_should_continue = False
#         print(f"Sorry, that's wrong. Final score: {score}.")
