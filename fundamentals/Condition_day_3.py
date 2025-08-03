# def welcomeMsg():
#     print("\n===============================")
#     print("** Welcome to the rollercoaster **")
#     print("===============================")


# welcomeMsg()
# height = int(input("\nPlease your height in cm: "))
# ticket = 0

# if height >= 120: 
#     print(f"You can ride the rollercoaster!")
#     age = int(input("Please enter your age: "))
#     if age < 12:
#         ticket = 5
#         print(f"The ticket price for kids is ${ticket}.")
#     elif age <= 18: 
#         ticket = 7   
#         print(f"The ticket price for youth is ${ticket}.")
#     else:
#         ticket = 12
#         print(f"The ticket price is ${ticket}.")

#     photo = input("Do you want photos while you are is rollercoaster just for $3? (Y / N) ")
#     if photo.casefold() == "y":
#         ticket += 3
#     print(f"Total bill is: ${ticket}")
# else:
#     print(f"Sorry, you have to grow taller before you can ride!")
 
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

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"The year {year} is a leap year")
# else:
#     print(f"The year {year} is not a leap year")

