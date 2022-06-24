from turtle import Turtle, Screen, colormode
import random

sam = Turtle()
colormode(255)
sam.speed("fastest")

for i in range(180):
    sam.circle(100)
    sam.left(2)
    sam.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))

screen = Screen()
screen.exitonclick()