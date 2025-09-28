# # function with output

# def format_name(first_name, last_name):
#   if first_name == "" or last_name == "":
#     print("Warning! You need to provide you name!")
#     return
# #   print(f"{first_name.title()} {last_name.title()}")
#   return f"{first_name.title()} {last_name.title()}"

# # name = format_name("marius", "iordan")
# print(format_name(input("What is your first name: "), input("What is your last name: ")))
  



def days_in_month(year, month):
   def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
              print("Leap year!")
              leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
              return leap
            else: 
              print("Not a leap year!")
              not_leap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
              return not_leap
        else: 
          print("Not a leap year!")
          not_leap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
          return not_leap
    else: 
        print("Not a leap year!")
        not_leap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return not_leap


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))