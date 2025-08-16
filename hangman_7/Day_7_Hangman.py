
# * TODO 1 - randomly choose a word from the list
# * TODO 2 - ask the user for a letter and assign to a variable and make it lower
# * TODO 3 - check if the user letter match the word

import random
import hangman_art
from hangman_words import word_list

import os

def clear():
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # Mac / Linux
    else:
        os.system('clear')


print(hangman_art.hangman)
selected_word = random.choice(word_list)
size = len(selected_word)
lives = 6
user_letter = []
word = []
user_guesses = []
end_of_game = False

for _ in range(size):
    word += "_"

while not end_of_game:  
    print(f" ".join(word))

    user_letter = input("\nGuess a letter: ").lower()
    clear()
    if user_letter in user_guesses:
        print(f"You've already guessed {user_letter}")
        continue  # skip to next loop iteration
    else:
        user_guesses.append(user_letter)
        print(user_guesses)
        print(f"You guessed {user_letter}, tha't not in the word. You lose a life!")



    for index in range(size):
        letter = selected_word[index]
            
        if letter == user_letter:
            word[index] = user_letter
            
    if "_" not in word:
        end_of_game = True
        print("\nYou win!")

    if user_letter not in word:
        lives -= 1
        print(hangman_art.stages[lives])
        if lives == 0:
          end_of_game = True
          print("You lose!!!")
          print(f"The word was '{selected_word}'")
  

