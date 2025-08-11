
# * TODO 1 - randomly choose a word from the list
# * TODO 2 - ask the user for a letter and assign to a variable and make it lower
# * TODO 3 - check if the user letter match the word


import random

word_list = ["camel", "elephant", "fireman"]
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


selected_word = random.choice(word_list)
size = len(selected_word)
counter = (size + 7)
user_letter = []
word = []


for x in range(size):
    word += "_"

print(word)
    
user_letter = input("Guess a letter: ").lower()

for index, letter in enumerate(selected_word):
    if letter == user_letter:
        word[index] = user_letter







# print(selected_word)
