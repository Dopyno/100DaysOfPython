
# * TODO 1 - randomly choose a word from the list
# * TODO 2 - ask the user for a letter and assign to a variable and make it lower
# * TODO 3 - check if the user letter match the word


import random

word_list = ["camel", "elephant", "fireman"]
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


selected_word = random.choice(word_list)
size = len(selected_word)
user_raw_letter = ""
user_letter = []
word = []

size = len(selected_word)
counter = (size + 7)

print(len(selected_word))
print(counter)
while counter > 0:
    for index, letter in enumerate(selected_word):
        if letter == user_letter:
            word[index] = user_letter
            # print("Right")
        else:
            word.append("_ ")  
            # print("Wrong")
        print(word[index], end=" ")

    print()
    user_letter = input("Guess a letter: ").lower()
    counter -= 1
    print(counter)






# print(selected_word)
