from turtle import Turtle
from cairo import FONT_SLANT_ITALIC

from yaml import AliasEvent

ALIGN = "center"
FONT = ("Courier", 14, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.curr_score = 0

        self.goto(0.00,270.00)
        self.hideturtle()
        self.color("white")
        self.write(f"Score: {self.curr_score}",align=ALIGN, font= FONT)

    def increase_score(self):
        self.curr_score += 1
        self.clear()
        self.write(f"Score: {self.curr_score}",align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0.00,0.00)
        self.hideturtle()
        self.color("white")
        self.write(f"Game Over.",align=ALIGN, font=FONT)
