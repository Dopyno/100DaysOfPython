import random
from art import logo, vs, clear_screen
from game_data import data


def generate(data_set):
    return random.choice(data_set)


def refine_data(dataSet1):
    name = dataSet1["name"]
    description = dataSet1["description"]
    country = dataSet1["country"]
    followers = dataSet1["follower_count"]

    return name, description, country, followers


def play_game():
    play = True
    score = 0
    # clear_screen()
    # print(logo)
    version_a = refine_data(generate(data))
    version_b = refine_data(generate(data))

    while play:
        clear_screen()
        print(logo)
        # version_a = refine_data(generate(data))

        print(f"Score: {score}")

        print(
            f"Compare: A => {version_a[0]}, {version_a[1]}, {version_a[2]}"
        )
        print(vs)
        print(
            f"Compare: B => {version_b[0]}, {version_b[1]}, {version_b[2]}"
        )

        user = input("Who has more followers? 'A' or 'B': ").lower()

        if version_a[3] >= version_b[3] and user == "a":
            score += 1
            print(f"Great, your current score {score}")
            version_b = refine_data(generate(data))
        elif version_a[3] <= version_b[3] and user == "b":
            score += 1
            print(f"You'r right, your current score {score}")
            version_a = refine_data(generate(data))
        else:
            print(f"Game over, your final score: {score}")
            play = False
    if input("Do you want to continue? (Y or N): ").lower() == "y":
        play_game()
    else:
        print(f"Game over, your final score: {score}")


play_game()
