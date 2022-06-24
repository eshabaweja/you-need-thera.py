# colorgram : extract code from images

# import colorgram
# colors = colorgram.extract('pop_culture.jpeg',10)
# rgb_colors = []


# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

from turtle import Turtle, Screen, colormode
import random

color_list = [(162, 87, 36), (165, 17, 59), (58, 14, 4), (65, 12, 29), (166, 51, 89), (234, 151, 48), (210, 72, 114), (214, 141, 24), (246, 211, 57), (215, 86, 55)]

# painting a 10*10 hirst with radius = 20 units and spacing = 50 units
colormode(255)
nancy = Turtle()
nancy.speed("fastest")
nancy.hideturtle()
for line in range(10):
    nancy.penup()
    nancy.setposition(-200,line*50-200)
    for steps in range (10):
        nancy.pendown()
        nancy.dot(20, random.choice(color_list))
        nancy.penup()
        nancy.fd(50)
screen = Screen()
screen.exitonclick()