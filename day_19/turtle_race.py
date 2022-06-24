from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width = 800, height= 600)
user_bet = screen.textinput(title = "Make your bet.", prompt = "Which turtle will win the race? Enter a color: ")

colors = ["purple", "blue", "green", "yellow", "orange", "red"]
my_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -390, y = turtle_index*40)
    my_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turt in my_turtles:
        random_distance = random.randint(0, 10)
        turt.forward(random_distance)
        if turt.xcor() >= 390:
            is_race_on = False
            winning_color = turt.pencolor()
            if winning_color == user_bet:
                print(f"You won. The {winning_color} turtle won.")
            else:
                print(f"You lost. The {winning_color} turtle won.")


screen.exitonclick()