from turtle import Turtle, update
from cairo import FONT_SLANT_ITALIC

from yaml import AliasEvent

ALIGN = "center"
FONT = ("Courier", 14, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.curr_score = 0

# reading saved high score
        prev_high = open("data.txt",'r')
        self.highscore = int(prev_high.read())
        prev_high.close()
        

        self.goto(0.00,270.00)
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()

    def increase_score(self):
        self.curr_score += 1
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.curr_score} High Score: {self.highscore}",align=ALIGN, font= FONT)

    def reset(self):
        if self.curr_score > self.highscore:
            self.highscore = self.curr_score
            high_score = open("data.txt",'w')
            high_score.write(str(self.highscore))
            high_score.close()
        self.curr_score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0.00,0.00)
    #     self.hideturtle()
    #     self.color("white")
    #     self.write(f"Game Over.",align=ALIGN, font=FONT)


