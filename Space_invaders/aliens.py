import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("data/invader1.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2

    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0 or self.rect.x > SCREEN_WIDTH - self.rect.width:
            self.speed = -self.speed
            self.rect.y += self.rect.height