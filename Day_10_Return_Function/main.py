# function with output

def format_name(first_name, last_name):
  if first_name == "" and last_name == "":
    print("Warning! You need to provide you name!")
    return
#   print(f"{first_name.title()} {last_name.title()}")
  return f"{first_name.title()} {last_name.title()}"

# name = format_name("marius", "iordan")
print(format_name(input("What is your first name: "), input("What is your last name: ")))
  
