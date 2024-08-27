import pygame


BROWN=(165,42,42)
class Obstacle:
    def __init__(self, x, size, GroundHeight):
        self.x = x
        self.size = size
        self.GroundHeight = GroundHeight

    def draw(self, gameDisplay):
        pygame.draw.rect(gameDisplay, BROWN, [self.x, self.GroundHeight-self.size, self.size, self.size])



    def update(self, deltaTime, velocity):
        self.x -= velocity*deltaTime

    def checkOver(self):
        if self.x < 0:
            return True
        else:
            return False