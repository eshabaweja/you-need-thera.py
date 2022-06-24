from turtle import Turtle, Screen
import random

peewee = Turtle()
colors = ["blue", "pink"]
peewee.pensize(10)
peewee.speed("fast")

for i in range(200):
    turn = random.randint(1,4)
    if turn == 1:
        peewee.forward(50)
    elif turn == 2:
        peewee.right(90)
    elif turn == 3:
        peewee.left(90) 
    else:
        peewee.forward(20)

    # else:
    #     peewee.back(10)
    peewee.pencolor(colors[i%2])

screen = Screen()
screen.exitonclick()
