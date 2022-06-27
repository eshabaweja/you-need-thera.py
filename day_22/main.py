# create screen
# create and move paddle up and down
# create another paddle
# create the ball and make it move
# detect collision with wall and bounce
# detect collision with paddle
# detect when paddle misses
# keep score

from turtle import Turtle, Screen
import paddle
import ball
import time
import scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Multiplayer Pong")
screen.tracer(0)


paddle_right = paddle.Paddle((350,0))
paddle_left = paddle.Paddle((-350,0))
ball = ball.Ball()
scoreboard = scoreboard.ScoreBoard()

screen.listen()
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")

screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")


game_on = True
while game_on:
    time.sleep(0.01)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor()>290 or ball.ycor()<-290:
        #needs to bounce
        ball.bounce_y()

    # Detect collision with paddle
    if (ball.distance(paddle_right) < 50 and ball.xcor()> 320) or (ball.distance(paddle_left) < 50 and ball.xcor()< -320):
        ball.bounce_x()

    # Detect when right paddle misses
    if (ball.xcor()> 380):
        ball.reset_position()
        scoreboard.l_point()
    
    # Detect when left paddle misses
    if (ball.xcor()< -380):
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()