
# * TODO 1 - randomly choose a word from the list
# * TODO 2 - ask the user for a letter and assign to a variable and make it lower
# * TODO 3 - check if the user letter match the word


import random

hangman = """ _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/                       """
word_list = ["camel", "elephant", "fireman"]
stages = ['''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print(hangman)
selected_word = random.choice(word_list)
# print(selected_word)
size = len(selected_word)
lives = 6
user_letter = []
word = []
end_of_game = False

for _ in range(size):
    word += "_"

while not end_of_game:  
    print(f" ".join(word))
    # print(lives)
    user_letter = input("\nGuess a letter: ").lower()

    for index in range(size):
        letter = selected_word[index]
            
        if letter == user_letter:
            word[index] = user_letter
            

    if "_" not in word:
        end_of_game = True
        print("\nYou win!")

    if user_letter not in word:
        lives -= 1
        print(stages[lives])

    if lives == 0:
        print("You lost!!!")
        break
# print(selected_word)
