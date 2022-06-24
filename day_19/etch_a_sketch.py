from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.fd(10)

def move_back():
    tim.bk(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)
# Set focus on TurtleScreen (in order to collect key-events). 
screen.listen() 
screen.onkey(fun = move_forward, key = "w") 
screen.onkey(fun = turn_left, key = "a") 
screen.onkey(fun = move_back, key = "s") 
screen.onkey(fun = turn_right, key = "d") 

screen.onkey(fun = tim.reset, key = "c") 
# in the above line, we wrote move_forward but not move_forward() because the parentheses are used only when we wanna call the function IMMEDIATELY. Here we want it to happen on key-press


screen.exitonclick()