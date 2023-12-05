from random import *
from turtle import *

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")

my_screen = Screen()
while True:
    timmy.forward(200)
    timmy.left(170)
    if abs(timmy.pos()) < 1:
        break
my_screen.exitonclick()
print(my_screen.canvheight)
