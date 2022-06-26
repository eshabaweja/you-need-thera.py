from pickletools import UP_TO_NEWLINE
from tkinter import LEFT, RIGHT
from turtle import Turtle

STARTING_POS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
# making snake body
# and arranging snake segments
class Snake:
    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POS:
            new_seg = Turtle(shape="square")
            new_seg.color("white")
            new_seg.penup()
            new_seg.goto(position)
            self.segments.append(new_seg)

    def move(self):
        # telling the square to follow the path of one before them
        for seg in range(2,0,-1):
            new_x = self.segments[seg-1].xcor()
            new_y = self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    # direction functions
    def right(self): # east
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def up(self): # north
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def left(self): # west
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def down(self): # south
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


