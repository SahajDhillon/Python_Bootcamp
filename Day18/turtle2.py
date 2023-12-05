import random
import turtle
from turtle import *

turtle.colormode(255)
tim = Turtle()
tim.shape('turtle')
tim.pensize(10)
tim.speed('fastest')


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors


directions = [0, 90, 180, 270]

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))
