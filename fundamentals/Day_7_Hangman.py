
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
        if user_letter == letter:
            word[index] = user_letter
        else:
            word.append("_ ")  
        print(word[index], end=" ")

    print()
    user_raw_letter = input("Please choose a letter: ")
    user_letter = user_raw_letter.lower()
    counter -= 1
    print(counter)






# print(selected_word)
