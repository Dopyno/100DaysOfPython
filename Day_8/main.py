# def greet():
#     print("hello")
#     print("How do you do?")
#     print("How is the weather today?")

# greet()


# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}")

# greet_with_name("Angela")

# def greet_with(name, location="Argentina"):
#     print(f"Hello {name}")
#     print(f"How do you do {name}")
#     print(f"Are you from {location}")


# greet_with("marius", "Brasil")

import math

# test_h = int(input("Hight of the wall: "))
# test_w = int(input("Width of the wall: "))
# coverage = 5

# def print_calc(height, width, cover):
#     return float((height * width) / cover)

# result = round(print_calc(test_h, test_w, coverage))
# result = math.ceil(result)
# print(f"You will ned to buy {result} cans of paint!")

n = int(input("Check this number: "))


def prime_checker(number=n):
    if number == 1 or number == 2 or number == 3 or number == 5:
        print(f"This number {number} is a prime number!")
    elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0:
        print(f"This number {number} is not a prime number!")
    elif number % 1 == 0 and number % number == 0:
        print(f"This number {number} is a prime number!")

def prime_check(number=n):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"This number {number} is a prime number!")
    else:
        print(f"This number {number} is not a prime number!")
        

prime_checker(n)
#prime_check(n)