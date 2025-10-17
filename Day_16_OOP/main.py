from turtle import *

timmy = Turtle()
jim = Turtle()
jim.shape("turtle")

print(timmy)
timmy.shape("turtle")
timmy.color("red")
timmy.pencolor("blue")
move = 100
for _ in range(5):
    timmy.forward(move)
    timmy.left(90)
    timmy.forward(move)
    timmy.left(90)
    timmy.forward(move)
    timmy.left(90)
    timmy.forward(move)
    move -= 10

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
