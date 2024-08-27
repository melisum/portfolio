import pygame
from dinosaur import Dinosaur #import the class Dinosaur from the file ’dinosaur’
from score import Score

pygame.init() #this ‘starts up’ pygame

#initialize game
size = width,height = 640, 480#creates tuple called size with width 400  and height 230
gameDisplay= pygame.display.set_mode(size) #creates screen
xPos = 0
yPos = 0
GROUND_HEIGHT = height-100

# create Dinosaur
dinosaur = Dinosaur(GROUND_HEIGHT)

#create lastframe variable
lastFrame = pygame.time.get_ticks() #get ticks returns current time in milliseconds

#define game colours
white = 255,255,255
black = 0,0,0

import random
from obstacle import Obstacle
MINGAP = 400
VELOCITY = 300
MAXGAP = 600
obstacles = []
num_of_obstacles = 4
lastObstacle = width
SCORE = 0
obstaclesize = 50
speed=1
for i in range(5):
    lastObstacle += MINGAP+(MAXGAP-MINGAP)*random.random() #Make distance between rocks random
    obstacles.append(Obstacle(lastObstacle, obstaclesize, GROUND_HEIGHT))
#set up score
score=Score()


while True: #gameLoop it draws the frames of the game
    t = pygame.time.get_ticks() #Get current time
    deltaTime = (t-lastFrame)/1000.0*speed #Find difference in time and then convert it to seconds
    lastFrame = t #set lastFrame as the current time for next frame.

    for event in pygame.event.get(): #Check for events
        if event.type == pygame.QUIT:
            pygame.quit() #quits
            quit()
        if event.type == pygame.KEYDOWN: #If user uses the keyboard
            if event.key == pygame.K_SPACE: #If that key is space
                dinosaur.jump() #Make dinosaur jump
    gameDisplay.fill(black)

    dinosaur.update(deltaTime)
    dinosaur.draw(gameDisplay)
    score.draw(gameDisplay)
    for obs in obstacles:
        obs.update(deltaTime, VELOCITY)
        obs.draw(gameDisplay)

        if obs.x - dinosaur.x <= 50:
            dinosaur.jump()

        if obs.checkOver():
            score.update()
            lastObstacle += MINGAP + (MAXGAP - MINGAP) * random.random()
            obs.x = lastObstacle

    lastObstacle -= VELOCITY * deltaTime

    pygame.draw.rect(gameDisplay,white, [0,GROUND_HEIGHT, width, height-GROUND_HEIGHT])
    speed += 0.00001
    pygame.display.update() #updates the screen
