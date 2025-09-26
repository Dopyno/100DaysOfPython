# function with output

def format_name(first_name, last_name):
  print(f"{first_name.title()} {last_name.title()}")
  return f"{first_name.title()} {last_name.title()}"

name = format_name("marius", "iordan")

print(name)
  
