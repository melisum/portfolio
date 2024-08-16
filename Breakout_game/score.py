FONT = ("Courier", 14, "normal")
from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score=0

        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(-100, 270)
        self.write(f" Score: {self.score}", align="center", font=FONT)


    def point(self, points):
        self.score+=points
        self.update_score()

    def gameisover(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)