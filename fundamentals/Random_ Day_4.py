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

row1 = ["🌁", "🌁", "🌁"]
row2 = ["🌁", "🌁", "🌁"]
row3 = ["🌁", "🌁", "🌁"]

our_map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
coord = input("please choose your coordinates: ")
first = int(coord[0]) - 1
second = int(coord[1]) - 1
# print(first, second)
our_map[second][first] = "❌"
print(f"{our_map[0]}\n{our_map[1]}\n{our_map[2]}")