import random
from art import logo, vs, clear_screen
from game_data import data


def generate(data_set):
    return random.choice(data_set)


def refine_data(dataSet1):
    print(
        f"Compare A: {dataSet1['name']}, {dataSet1['description']}, {dataSet1['country']}"
    )
    return dataSet1["follower_count"]

def play_game():
    play = True

    while play:
        print(logo)
        a = refine_data(generate(data))
        print(vs)
        b = refine_data(generate(data))

        if a > 
