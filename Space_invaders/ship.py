import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("data/spaceship2.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5

    def move_left(self):
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.rect.x = 0

    def move_right(self):
        self.rect.x += self.speed
        if self.rect.x > SCREEN_WIDTH - self.rect.width:
            self.rect.x = SCREEN_WIDTH - self.rect.width