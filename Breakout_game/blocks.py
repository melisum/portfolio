from turtle import Turtle
distance=4
RIGHT=0
LEFT=180
xpos=-150
COLORS = ["yellow","yellow", "green","green", "orange","orange","red","red"]
XPOSITIONS = [-230,-195,-160,-125,-90,-55,-20,15,50,85,120,155,190,225]



class Blocks(Turtle):
    def __init__(self):
        super().__init__()
        self.all_blocks=[]


    def create_block(self):
        ypos=120
        for color in COLORS:
            for position in XPOSITIONS:
                new_block=Turtle()
                new_block.shape("square")
                new_block.color(color)
                new_block.shapesize(stretch_wid=0.5, stretch_len=1.5)
                new_block.penup()
                new_block.goto(x=position, y=ypos)
                self.all_blocks.append(new_block)
            ypos+=15
    def delete(self, block):
        block.color("black")
        block.penup()
        block.goto(300,300)







