from art import logo
import os
import subprocess
import sys


def clear_screen():
    """Clear the terminal screen"""
    os.system("cls" if os.name == "nt" else "clear")




def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operation = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    print(logo)
    first_num = float(input("What is your first number: "))
    for symbol in operation:
        print(symbol)
    calculate = True

    while calculate:
        operation_symbol = input("Pick an operation: ")
        second_num = float(input("What's your next number: "))
        calculation_function = operation[operation_symbol]
        answer = calculation_function(first_num, second_num)

        print(f"\n{first_num} {operation_symbol} {second_num} = {answer}")

        if (
            input(
                f"Type 'Yes' to continue calculation with {answer}, or type 'no' to start a new calculation: "
            ).lower()
            == "yes"
        ):
            clear_screen()
            first_num = answer
        else:
            calculate = False
            calculator()


calculator()

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
