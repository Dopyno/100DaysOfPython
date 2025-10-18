from random import random
from turtle import *

timmy = Turtle()
jim = Turtle()
my_screen = Screen()

print(timmy)
timmy.shape("turtle")
timmy.color("red")
timmy.width(3)

for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    timmy.right(angle)
    timmy.fd(steps)
print(my_screen.canvheight)
my_screen.exitonclick()
