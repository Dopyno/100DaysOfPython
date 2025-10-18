# from turtle import *
#
# timmy = Turtle()
# jim = Turtle()
# my_screen = Screen()
#
# print(timmy)
# timmy.shape("turtle")
# timmy.color("blue")
# timmy.width(3)
#
# timmy.forward(100)
#
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)
