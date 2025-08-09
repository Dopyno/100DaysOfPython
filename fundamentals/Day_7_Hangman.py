
# * TODO 1 - randomly choose a word from the list
# * TODO 2 - ask the user for a letter and assign to a variable and make it lower
# * TODO 1 - check if the user letter match the word


import random

word_list = ["camel", "elephant", "fireman"]

selected_word = random.choice(word_list)

user_raw_letter = ""

while user_raw_letter == "":
    user_raw_letter = input("Please choose a letter: ")
    user_letter = user_raw_letter.lower()

    for x in selected_word:
        if user_letter == x:
            print(f"{x}", end=" ")
        else:
            print("_", end=" ")







# print(selected_word)
