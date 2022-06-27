from hashlib import new
from turtle import Turtle, speed
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE
        
    def create_car(self):

        if random.randint(1,10) == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(1,2)
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250,250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.speed)

    def speedup(self):
        self.speed += MOVE_INCREMENT