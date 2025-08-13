# std_num = input("Please enter your numbers: ").split(" ")
# count = 0
# total = 0

# for i in range(0, len(std_num)):
#     std_num[i] = int(std_num[i])
#     count += 1
#     total += std_num[i]
#     print(std_num[i])
#     print(count)
#     print(total)
#     print("==========")

# print(f"the total is: {total}")
# print(f"the number of ellerment is: {count}")

# print(f"The average is: {round(total/count)}")

# *. MAX

# numbers = [78, 65, 89, 86, 55, 91, 64, 89, 99, 23, 25]

# max_num = 0

# for i in numbers:
#     if i > max_num:
#         max_num = i 

# print(f"The highest score in the class is: {max_num}")

# ** fizz buzz

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print(f"The number {i} is divisible with 3 and 5: FizzBuzz")
#     elif i % 5 == 0:
#         print(f"The number {i} is divisible with 5: BUZZZ")
#     elif i % 3 == 0:
#         print(f"The number {i} is divisible with 3: FIZZZ")
#     else:
#         print(i)

#** Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# for i in range(0, nr_letters):
#     temp.append(letters[random.randint(0, len(letters) - 1)])
# for i in range(0, nr_symbols):
#     temp.append(letters[random.randint(0, len(letters) - 1)])
# for i in range(0, nr_numbers):
#     temp.append(letters[random.randint(0, len(letters) - 1)])    #     
 

#  Sequence print
# aCEDr+*%%*69939
# Shuffle print
# 9%D**Ea9+r93%6C

password = []

for i in range(0, nr_letters):
    password.append(random.choice(letters))

for i in range(0, nr_symbols):
    password.append(random.choice(symbols))

for i in range(0, nr_numbers):
    password.append(random.choice(numbers))

y = ""
for i in range(0, len(password)):
    y += password[i]

print("Sequence print")
print(y)

# ** Hard

random.shuffle(password)
x = ""
for i in range(0, len(password)):
    x += password[i]

print("Shuffle print")
print(x)

# for i in range(0, len(temp)):
#     x = random.shuffle(temp[i])
#     print(x)

