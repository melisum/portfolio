from turtle import Turtle
move_distance=20
RIGHT=0
LEFT=180




class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)


    def create_paddle(self, position):

        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=2)
        self.penup()
        self.goto(position)




    def left(self):
        new_x=self.xcor() - 20
        self.goto(new_x, self.ycor())

    def right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())
