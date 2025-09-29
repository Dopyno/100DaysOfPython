from art import logo
import os
import subprocess
import sys


def clear_screen():
    """Clear the terminal screen"""
    os.system("cls" if os.name == "nt" else "clear")


print(logo)

calculate = True


# def calculator(first_number, operation, second_number):
#     """Calculate basic operations."""
#     if operation == "*":
#         return first_number * second_number
#     elif operation == "/":
#         return first_number / second_number
#     elif operation == "+":
#         return first_number + second_number
#     elif operation == "-":
#         return first_number - second_number


def add(n1, n2):
    return n1 + n2

 
def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operation = {"+": add, "-": subtract, "*": multiply, "/": divide}

first_num = int(input("What is your first number: "))
for symbol in operation:
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
second_num = int(input("What is your second number: "))
calculation_function = operation[operation_symbol]
result = calculation_function(first_num, second_num)




print(f"\n{first_num} {operation_symbol} {second_num} = {result}")
print(f"\n{first_num} {operation_symbol} {second_num} = {result}")







# while calculate:
#     result = calculator(first_num, operation, second_num)
#     answer = input(
#         f"Do you want to continue, and use this result {result} for further calculations? (Yes / No) or (Exit)"
#     ).lower()
#     if answer == "no":
#         clear_screen()
#     elif answer == "yes":
#         operation = input("Please select your operation (*, /, +, -): ")
#         second_num = int(input("What is your second number: "))
#         result1 = calculator(result, operation, second_num)
#         print(f"\n{result} {operation} {second_num} = {result1}")
#         answer = input(
#             f"Do you want to continue, and use this result {result1} for further calculations? (Yes / No) or (Exit)"
#         ).lower()
