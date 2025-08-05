import random 
import module

# number = random.randint(1, 10)
# print(number)
# # print(module.PI)
# float_number = random.random() * 2
# print(float_number)

#** Coin game

# coin = random.randint(0, 1)
# # print(coin)
# if coin == 1:
#     print("head")
# else:
#     print("tails")

# fruit = ["orange", "apple", "banana"]

# print(len(fruit))
# print(fruit.count("orange"))
# fruit.extend(["kiwi", "mango", "rasbery"])
# print(fruit)
# fruit.append("mellon")
# fruit.pop()
# print(fruit)

#** bill roulete

# roulete = input("Please enter all names separated by the comma: ")
# our_list = roulete.split(", ")
# choice = random.randint(0, len(our_list) - 1)
# print(f"{our_list[choice]} will pay today for the bill!")

# * map Game

# row1 = ["🌁", "🌁", "🌁"]
# row2 = ["🌁", "🌁", "🌁"]
# row3 = ["🌁", "🌁", "🌁"]

# our_map = [row1, row2, row3]

# print(f"{row1}\n{row2}\n{row3}")
# coord = input("please choose your coordinates: ")
# first = int(coord[0]) - 1
# second = int(coord[1]) - 1
# # print(first, second)
# our_map[second][first] = "❌"
# print(f"{our_map[0]}\n{our_map[1]}\n{our_map[2]}")

# * Rock, Paper Scissor game
# rock wins against scissor
# scissor win against paper
# paper wins against rock

rock = """Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """Paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissor = """Scissor
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

list = [rock, scissor, paper]

player = int(input("What so you choose? Type 1 for Rock, 2 for Paper or 3 for Scissor.\n"))
computer = random.randint(0, 2)

if player < 0 or player >= 3: 
    print("You type another number, you lose!!!")

else:
    print(list[player])
    print("Computer choose")
    print(list[computer])

    if computer == 0 and player == 1:
        print("Computer Win!")
    elif computer == 1 and player == 2:
        print("Computer Win!")
    elif computer == 2 and player == 0:
         print("Computer Win!")
    elif computer == player:
        print("I'ts a draw!")

    if player == 0 and computer == 1:
        print("You Win!")    
    elif player == 1 and computer == 2:
         print("You Win!") 
    elif player == 2 and computer == 0:
        print("You Win!") 
   




