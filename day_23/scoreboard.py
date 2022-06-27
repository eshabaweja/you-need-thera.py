from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.goto(-280,260)
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)
        self.level += 1

    def game_over(self):
        self.goto(-80,0)
        self.write("GAME OVER.", font=FONT)