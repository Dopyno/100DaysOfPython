
#** Rollercoaster park

def welcomeMsg():
    print("\n===============================")
    print("** Welcome to the rollercoaster **")
    print("===============================")


welcomeMsg()
height = int(input("\nPlease your height in cm: "))
ticket = 0

if height >= 120: 
    print(f"You can ride the rollercoaster!")
    age = int(input("Please enter your age: "))
    if age < 12:
        ticket = 5
        print(f"The ticket price for kids is ${ticket}.")
    elif age <= 18: 
        ticket = 7   
        print(f"The ticket price for youth is ${ticket}.")
    elif age >=45 and age <=55:
        ticket = 0
        print(f"The ticket price is ${ticket}.")
        print(f"Please enjoy your day at the park.")
        print(f"This is a special offer for midage crisis.")
    else:
        ticket = 12
        print(f"The ticket price is ${ticket}.")

    photo = input("Do you want photos while you are is rollercoaster just for $3? (Y / N) ")
    if photo.casefold() == "y":
        if age >=45 and age <=55:
            ticket += 0
        else:
            ticket += 3
    print(f"Total bill is: ${ticket}")
else:
    print(f"Sorry, you have to grow taller before you can ride!")
 
#** BMI calculator

# print("BMI calculator")
# height = float(input("Please enter your height is m: "))
# weight = float(input("Please enter your weight is kg: "))

# bmiResults = round(weight / (height ** 2))

# if bmiResults < 18.5:
#     print(f"Your BMI is: {bmiResults}. You are underweight")
# elif bmiResults < 25:
#     print(f"Your BMI is: {bmiResults}. You have a normal weight! Well done!")
# elif bmiResults < 30:
#     print(f"Your BMI is: {bmiResults}. You are overweight")
# elif bmiResults < 35:
#     print(f"Your BMI is: {bmiResults}. You are obese!")
# else:
#     print(f"Your BMI is: {bmiResults}. You are clinically obese!")

# year = int(input("please enter a year to see if is a leap year: "))

#** Leap year

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"The year {year} is a leap year")
# else:
#     print(f"The year {year} is not a leap year")

#**  Python Pizza Calculator

# def welcome():
#     print("\n---------------------------------------")
#     print("** Welcome to Python Pizza Delivery! **")
#     print("---------------------------------------\n")

# def print_menu():
#     print("=======  PIZZA MENU  =======")
#     print("Small Pizza: $15")
#     print("Medium Pizza: $20")
#     print("Large Pizza: $25\n")
#     print("Pepperoni for Small Pizza: +$2")
#     print("Pepperoni for Medium and Large Pizza: +$3\n")
#     print("Extra cheese for any size of pizza: +$1")

# def calculate_bill(size, pepperoni, cheese):
#     price = 0
#     if size.casefold() == "s":
#         price += 15
#         print(f"You choose a Small Pizza for: ${price}")
#     elif size.casefold() == "m":
#         price += 20
#         print(f"You choose a Medium Pizza for: ${price}")
#     else:
#         price += 25
#         print(f"You choose a Large Pizza for: ${price}")

#     if pepperoni.casefold() == "y":
#         if size.casefold() == "s":
#             price += 2
#             print("Adding pepperoni for: +$2")
#         else:
#             price += 3
#             print("Adding pepperoni for: +$3")

#     if cheese.casefold() == "y":
#             price += 1
#             print("Adding pepperoni for: +$1")
#     print(f"Total bill: ${price}")

# welcome()
# print_menu()

# size = input("What size pizza do you want? S, M or L ")
# pepperoni = input("Do you want pepperoni? (Y / N) ")
# cheese = input("Do you want extra cheese? (Y / N) ")

# calculate_bill(size, pepperoni, cheese)
