FONT = ("Courier", 14, "normal")
from turtle import Turtle
class Turns(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

        self.turn=3

        self.turns()
    def turns(self):
        self.clear()
        self.goto(100, 270)
        self.write(f" Turns: {self.turn}", align="center", font=FONT)

    def lose_turn(self):
        self.turn-=1
        self.turns()