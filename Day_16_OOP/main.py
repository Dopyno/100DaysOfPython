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

table1 = PrettyTable()
table = PrettyTable()

table1.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table1.add_column("Type", ["Electric", "Water", "Fire"])

table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
table.add_row(["Adelaide", 1295, 1158259, 600.5])
table.add_row(["Brisbane", 5905, 1857594, 1146.4])
table.add_row(["Darwin", 112, 120900, 1714.7])
table.add_divider()
table.add_row(["Hobart", 1357, 205556, 619.5])
table.add_row(["Sydney", 2058, 4336374, 1214.8])
table.add_row(["Melbourne", 1566, 3806092, 646.9])
table.add_row(["Perth", 5386, 1554769, 869.4])

table.sortby = "Area"
table.add
print(table1)
print(table)
