# # Data types

# #* String

# print("hello"[0])
# print("123" + "345")

# #* Integer

# print(123 + 345)

# 123_123_123

# #* Float

# 3.1415

# #* Boolean
# True
# False

# two_number_digit = int(input("Please enter your two digit number: "))
# num = str(two_number_digit)
# total = int(num[0]) + int(num[1]) 
# print(total)

# 2 + 3 #Adding
# 2 - 3 #Subtract
# 2 * 3 #Multiply
# 2 / 3 #Division
# 2 ** 3 #Raising to power 2 to the power of 3

# PEMDAS left to right - Operetion order

# ()
# **
# */
# +-
# print("BMI calculator")
# height = float(input("Please enter your height is m: "))
# weight = float(input("Please enter your weight is kg: "))

# bmiResults = round(weight / (height ** 2), 2)
# print(f"BMI for your height = {height}, and the weight = {weight}, is: {bmiResults}")

age = int(input("What is your current age: "))
max_age = 90
days = (max_age - age) * 365
weeks = (max_age - age) * 52
months = (max_age- age) * 12
message = f"You have {days} days, {weeks} weeks, and {months} months left, enjoy the rest of your life!!🎉"
print(message)