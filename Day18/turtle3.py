import turtle
import random

turtle.colormode(255)
turtle.speed('fastest')
turtle.shape('turtle')


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors


def draw_circle(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.right(size_of_gap)
        # turtle.setheading(turtle.heading()+10)


draw_circle(5)
turtle.exitonclick()
