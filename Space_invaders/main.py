from turtle import Turtle, Screen
from aliens import Alien
from ship import Ship
from laser import Laser
import time

gameison=True
lives=3
screen = Screen()
screen.setup(width=500, height=600)
screen.title("Space invaders")
screen.bgcolor("black")
screen.tracer(0)

alien = Alien()
ship = Ship()
ship.create_ship()
laser=Laser()

screen.listen()
screen.onkey(ship.left, "Left")
screen.onkey(ship.right, "Right")
screen.onkey(laser.create_laser(x=ship.xcor(), y=ship.ycor()), "space")


while gameison:
    time.sleep(0.5)
    screen.update()
    alien.create_alien()
    alien.movement()
    laser.move_lasers()





screen.exitonclick()
