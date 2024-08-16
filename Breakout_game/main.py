
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from blocks import Blocks
from score import Score
from turns import Turns
import time
gameison=True
xpos=-150
STARTING_POSITION = (0, 0)
hits=0
screen=Screen()
screen.setup(width=510, height=600)
screen.title("Breakout")
screen.bgcolor("black")
screen.tracer(0)

paddle = Paddle((0,-270))
score=Score()
turns=Turns()
ball=Ball()
blocks=Blocks()

screen.listen()

screen.onkey(paddle.left, "Left")
screen.onkey(paddle.right, "Right")
blocks.create_block()


while gameison:
    time.sleep(ball.movespeed)
    ball.move()
    screen.update()

#detect crash
    for block in blocks.all_blocks:
        if block.distance(ball)<11:
            ball.bounce_y()
            if block.color() == ("yellow", "yellow"):
                 score.point(points=1)
            elif block.color() == ("green", "green"):
                 score.point(points=3)
            elif block.color() == ("orange", "orange"):
                 score.point(points=5)
                 ball.speed_increase()
            elif block.color() == ("red", "red"):
                 score.point(points=7)
                 ball.speed_increase()

            blocks.delete(block)
            blocks.all_blocks.remove(block)
            hits += 1
    if hits== 4 or hits == 12:
        ball.speed_increase()
#bounce
    if ball.xcor() > 235 or ball.xcor() < -235 :
        ball.bounce_x()
    if ball.ycor() > 270 :
        ball.bounce_y()

#colision with paddle
    if ball.distance(paddle) < 40 and ball.ycor() <-250 :
        ball.bounce_y()

#missing the ball
    if  ball.ycor() <-280 :
        turns.lose_turn()
        ball.goto(STARTING_POSITION)
        ball.bounce_y()

#gameover
    if turns.turn == 0:
        score.gameisover()
        gameison=False




screen.exitonclick()
