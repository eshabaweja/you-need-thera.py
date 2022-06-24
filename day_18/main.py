from turtle import Turtle, Screen
import turtle
import heroes
from random import randint

# heroes is not a standard library module. It was installed using pip.
print (heroes.gen())
print (heroes.genarr(3))

blinky = Turtle()
blinky.shape("turtle")
blinky.color("brown")
blinky.pencolor(0.3, 0.7, 0.44)

# draw a square
for i in range(4):
    blinky.fd(100)
    blinky.right(90)

blinky.left(45)
# draw a dashed line
for i in range(20):
    blinky.fd(5)
    blinky.penup()
    blinky.fd(5)
    blinky.pendown()

# draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon with random colors
# 360/i where i is number of sides
turtle.colormode(255)
for i in range(3, 11):
    blinky.color(randint(0,255),randint(0,255),randint(0,255))

    for j in range(i):
        blinky.fd(100)
        blinky.right(360/i)


screen = Screen()
screen.exitonclick()