# improved snake game

import time
from turtle import Turtle, Screen

from more_itertools import padded
from scoreboard import ScoreBoard
from food import Food
from snake import Snake

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snek")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

# playing game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    # detect collision with wall
    if (snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290):
        # game_is_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()


    # detect collision of head with any segment of own body
    # if it collides, trigger game_over
    for segment in snake.segments[1:]: # using slicing to skip the head of the snake
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            # game_is_on: False
            # scoreboard.game_over()
            scoreboard.reset()





screen.exitonclick()