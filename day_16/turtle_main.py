##### Object Oriented Programming #####
# using the Turtle library objects 

from turtle import Turtle, Screen

jonathan = Turtle()
print(jonathan)

my_screen = Screen()
print(my_screen.canvheight)
jonathan.shape("turtle")
jonathan.color("orange")
jonathan.forward(100)

my_screen.exitonclick()